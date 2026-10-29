# -*- coding: utf-8 -*-
"""standing/orders.py -- THE OPEN ORDERS GENERATED FROM THE RECORD ((R333)(3)(i), v1.3.0). Reads every W-ORD entry in PLACE-papers
OPEN_TRAILS.md at a revision (HEAD by default, never the working copy) and prints each order OPEN or CLOSED by the rule below, the rule
printed before the output. From b723 the trail's open-orders line is written from this tool's output (`line`).

THE RULE: an order is a name W-ORD-<A-Z0-9 and hyphens>; its entry the first line of OPEN_TRAILS naming it. It is OPEN unless a later
line (after its entry, a roll line "**The open orders:**" excepted) CLOSES it: names it with DISCHARGED, CLOSED, RETIRED or SUPERSEDED
in the clause that names it -- the words after the name up to the next order's name, a ';', or the clause's end at '. ', within 160
characters, or the 40 characters before it with no other order's name between -- the word not negated (no "not", "no", "never", "nor",
"unless" or "un-" within the 14 characters before it); or names a successor order that replaces it ("replaced by", "superseded by",
"succeeded by", "its successor" and a W-ORD name, in that clause).

  orders.py read [--at REV] [--bank]     the orders, each OPEN or CLOSED with its closing line; --bank writes data/<act>_orders.txt
  orders.py line [--at REV]              the trail's open-orders line, from the output
  orders.py control [--at REV] [--bank]  (R333)(3)(i)'s controls: the output contains the last roll line's names (OPEN_TRAILS :16250's
                                         ten at b723) and the twenty of (R332)(14) as the previous act's events bank names them; a
                                         planted closing line (in memory) removes its order; a planted negated line does not
It reads and prints; with --bank it writes its one bank.
"""
import json
import os
import re
import subprocess
import sys
import time

NL = '\n'
T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
PP = 'D:/MY-DOwnloads/PLACE-papers'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NAME = re.compile(r'W-ORD-[A-Z0-9]+(?:-[A-Z0-9]+)*')
# ### the words as a status: not a hyphenated compound ("DISCHARGED-BY-READING", a triage class) and not "CLOSED FORM" (an adjective)
CLOSE = re.compile(r'\b(DISCHARGED|CLOSED|RETIRED|SUPERSEDED)\b(?!-)(?![ -](?i:form))')
REENTRY = re.compile(r'(?i)\b(ENTERED|RE-?OPENED|REMAINDER)\b')
NEG = re.compile(r'(?i)(\bnot\b|\bno\b|\bnever\b|\bnor\b|\bunless\b|\bun-)')
SUCC = re.compile(r'(?i)(replaced by|superseded by|succeeded by|its successor)\W{0,12}`?(W-ORD-[A-Z0-9]+(?:-[A-Z0-9]+)*)')
ROLL = '**The open orders:**'
RULE = ('THE RULE: an order is a name W-ORD-<...>; its entry the first line of OPEN_TRAILS naming it; OPEN unless a later line, a roll '
        'line excepted, names it with DISCHARGED, CLOSED, RETIRED or SUPERSEDED in the clause naming it (after the name up to the next '
        'order`s name not coordinated with it, or a `;` or `. ` outside parentheses, within 160 characters; or the word standing directly '
        'before the name), not negated (not, no, '
        'never, nor, unless, un- within 14 characters before the word), or names a successor replacing it in that clause; the words '
        'read as a status (not a hyphenated compound, not "CLOSED FORM"). PRINTED BESIDE, NOT A STATUS: a line after the closing line '
        'naming the order with ENTERED, REOPENED or REMAINDER in its clause (RE-ENTERED), and the roll lines carrying a CLOSED order')


def act():
    return json.load(open(os.path.join(D, 'act_current.json'), encoding='utf-8'))


def trail(rev='HEAD'):
    out = subprocess.run(['git', '-C', PP, 'show', '%s:OPEN_TRAILS.md' % rev], capture_output=True).stdout
    return out.decode('utf-8', 'replace').replace('\r', '').split(NL)


COORD = re.compile(r'(?i)^`?\s*(\([^()]*\))?\s*(,|and|, and|&)\s*`?$')


def _clause_after(line, end):
    """the clause after a name ending at `end`, at most 160 characters: to the next order's name -- unless that name is coordinated with
    this one ("A and B", "A, B", a parenthesis between), when the clause runs on past it -- or to a ';' or '. ' outside parentheses."""
    s = line[end:end + 160]
    depth, stop = 0, len(s)
    for i, ch in enumerate(s):
        depth += (ch == '(') - (ch == ')')
        if depth <= 0 and (ch == ';' or (ch == '.' and s[i + 1:i + 2] == ' ')):
            stop = i
            break
    s, at = s[:stop], 0
    while True:
        m = NAME.search(s, at)
        if not m:
            return s
        if COORD.match(s[at:m.start()].strip(' `*')) or COORD.match(s[at:m.start()]):
            at = m.end()
            continue
        return s[:m.start()]


BEFORE = re.compile(r'\b(DISCHARGED|CLOSED|RETIRED|SUPERSEDED)\b[\s:*`—–-]*$')


def _closer(line, name):
    """the reason a line closes `name` ('DISCHARGED', 'successor W-ORD-X', ...), or None: the word in the clause after the name, or
    standing directly before it (nothing but spaces, ':', '*', '`' or a dash between)."""
    for m in re.finditer(re.escape(name) + r'(?![A-Z0-9-])', line):
        after = _clause_after(line, m.end())
        for c in CLOSE.finditer(after):
            if not NEG.search(after[max(0, c.start() - 14):c.start()]):
                return c.group(1)
        before = line[max(0, m.start() - 40):m.start()]
        b = BEFORE.search(before)
        if b and not NEG.search(before[max(0, b.start() - 14):b.start()]):
            return b.group(1)
        s = SUCC.search(after)
        if s and s.group(2) != name:
            return 'successor %s' % s.group(2)
    return None


def read(lines):
    """{name: dict(entry, status, closed_at, why, named)} over every order the trail names, in entry order."""
    orders, order = {}, []
    for i, l in enumerate(lines, 1):
        for n in set(NAME.findall(l)):
            if n not in orders:
                orders[n] = dict(entry=i, status='OPEN', closed_at=None, why=None, named=0)
                order.append(n)
            orders[n]['named'] += 1
    for i, l in enumerate(lines, 1):
        if l.lstrip().startswith(ROLL):
            continue
        for n in set(NAME.findall(l)):
            o = orders[n]
            if i <= o['entry'] or o['closed_at']:
                continue
            why = _closer(l, n)
            if why:
                o.update(status='CLOSED', closed_at=i, why=why)
    # ### beside the status, not changing it: a re-entry after the closing line, and the roll lines naming a CLOSED order after it
    for n in order:
        o = orders[n]
        o['reentered'], o['rolls_after'] = None, 0
        if not o['closed_at']:
            continue
        for i, l in enumerate(lines[o['closed_at']:], o['closed_at'] + 1):
            if n not in l:
                continue
            if l.lstrip().startswith(ROLL):
                o['rolls_after'] += 1
            elif o['reentered'] is None:
                for m in re.finditer(re.escape(n) + r'(?![A-Z0-9-])', l):
                    if REENTRY.search(_clause_after(l, m.end())):
                        o['reentered'] = i
                        break
    return [(n, orders[n]) for n in order]


def last_roll(lines):
    rows = [(i, l) for i, l in enumerate(lines, 1) if l.lstrip().startswith(ROLL)]
    return rows[-1] if rows else (None, '')


def the_twenty(prev):
    """the twenty of (R332)(14) as the previous act's events bank names them ("W-ORD-<name> -- OPEN; entry")."""
    p = os.path.join(D, '%s_events.txt' % prev)
    t = open(p, encoding='utf-8').read() if os.path.isfile(p) else ''
    out = []
    for m in re.finditer(r'(?m)^\s+(W-ORD-[A-Z0-9-]+) -- OPEN; entry', t):
        if m.group(1) not in out:
            out.append(m.group(1))
    return out


def report(rows, rev):
    op = [n for n, o in rows if o['status'] == 'OPEN']
    L = ['%s -- THE OPEN ORDERS GENERATED FROM THE RECORD ((R333)(3)(i); tools/standing/orders.py) (%s)' % (
        act()['act'], time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### PLACE-papers OPEN_TRAILS.md at %s (%s), read through git, the working copy not read' % (
             rev, subprocess.run(['git', '-C', PP, 'rev-parse', '--short=8', rev], capture_output=True, text=True).stdout.strip()),
         '### ' + RULE, '', '## THE ORDERS (name ; entry ; status ; the closing line and its word ; lines naming it)']
    for n, o in rows:
        beside = ''
        if o['closed_at'] and (o['reentered'] or o['rolls_after']):
            beside = ' ; ### RE-ENTERED at :%s, ON %d ROLL LINE(S) AFTER ITS CLOSE' % (o['reentered'] or '-', o['rolls_after'])
        L.append('  %-40s entry :%-6d %-7s %s ; named %d%s' % (n, o['entry'], o['status'],
                                                            (':%d %s' % (o['closed_at'], o['why'])) if o['closed_at'] else '-', o['named'], beside))
    conflict = [n for n, o in rows if o['closed_at'] and (o['reentered'] or o['rolls_after'])]
    L += ['', '### ### **ORDERS %d ; OPEN %d ; CLOSED %d ; CLOSED BY THE RULE AND CARRIED OR RE-ENTERED AFTER %d%s.**' % (
        len(rows), len(op), len(rows) - len(op), len(conflict), (': ' + ', '.join(conflict)) if conflict else '')]
    return L, op


def open_line(op):
    return ROLL + ' ' + '; '.join('`%s`' % n for n in op) + '.'


def _bank(name, L):
    p = os.path.join(D, name)
    with open(p + '.tmp', 'wb') as f:
        f.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print('written data/%s' % name)


def control(lines, rev):
    a = act()
    rows = read(lines)
    st = dict(rows)
    ln, roll = last_roll(lines)
    ten = NAME.findall(roll)
    tw = the_twenty(a['prev'])
    L, good, n = ['## THE CONTROLS ((R333)(3)(i))'], 0, 0

    def case(ok, what):
        nonlocal good, n
        n += 1
        good += bool(ok)
        L.append('  %s -- %s' % (what, 'AS WANTED' if ok else 'NOT AS WANTED'))
    miss10 = [x for x in ten if st.get(x, {}).get('status') != 'OPEN']
    case(len(ten) == 10 and not miss10, 'the last roll line`s names (:%s, %d): each OPEN in the output%s' % (
        ln, len(ten), (' ; NOT OPEN: ' + ' '.join(miss10)) if miss10 else ''))
    miss20 = [x for x in tw if st.get(x, {}).get('status') != 'OPEN']
    case(len(tw) == 20 and not miss20, 'the twenty of (R332)(14) (data/%s_events.txt, %d named): each OPEN in the output%s' % (
        a['prev'], len(tw), (' ; NOT OPEN: ' + ', '.join('%s (:%s %s)' % (x, st[x]['closed_at'], st[x]['why']) for x in miss20 if x in st)) if miss20 else ''))
    if ten:
        x = ten[0]
        planted = dict(read(lines + ['PLANTED (in memory): `%s` DISCHARGED at the plant.' % x]))
        case(planted[x]['status'] == 'CLOSED', 'PLANTED: a closing line for %s appended in memory: the order CLOSED' % x)
        negated = dict(read(lines + ['PLANTED (in memory): `%s` is not DISCHARGED by this line.' % x]))
        case(negated[x]['status'] == 'OPEN', 'PLANTED: a negated line for %s ("not DISCHARGED"): the order stays OPEN' % x)
        other = dict(read(lines + ['PLANTED (in memory): `%s` carried; `W-ORD-PLANT-OTHER` DISCHARGED.' % x]))
        case(other[x]['status'] == 'OPEN', 'PLANTED: a line naming %s beside another order DISCHARGED: %s stays OPEN' % (x, x))
    L += ['', '### ### **THE ORDERS` CONTROLS: CASES %d ; AS WANTED %d ; %s.**' % (n, good, 'ALL AS WANTED' if good == n else 'NOT ALL AS WANTED')]
    return L, good == n


def main(argv):
    rev = argv[argv.index('--at') + 1] if '--at' in argv else 'HEAD'
    verb = argv[0] if argv else ''
    lines = trail(rev)
    if verb == 'read' or verb == 'control':
        rows = read(lines)
        L, op = report(rows, rev)
        L += ['', '## THE CLOSING LINES ACCEPTED, EACH FOR A HAND READ (the order ; the line ; its text, 300 characters around the name)']
        for nm, o in rows:
            if o['closed_at']:
                t = lines[o['closed_at'] - 1]
                k = t.find(nm)
                L.append('  %s ; :%d %s ; %s' % (nm, o['closed_at'], o['why'], t[max(0, k - 120):k + 180].strip()))
        if verb == 'control':
            C, ok = control(lines, rev)
            L += [''] + C
        print(NL.join(L))
        if '--bank' in argv:
            _bank('%s_orders.txt' % act()['act'], L)
        return 0
    if verb == 'line':
        print(open_line(report(read(lines), rev)[1]))
        return 0
    sys.exit(__doc__)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
