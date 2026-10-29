# -*- coding: utf-8 -*-
"""standing/orders.py -- THE OPEN ORDERS GENERATED FROM THE RECORD ((R333)(3)(i), v1.3.0). Reads every W-ORD entry in PLACE-papers
OPEN_TRAILS.md at a revision (HEAD by default, never the working copy) and prints each order OPEN or CLOSED by the rule below, the rule
printed before the output. From b723 the trail's open-orders line is written from this tool's output (`line`).

THE RULE: an order is a name W-ORD-<A-Z0-9 and hyphens>; its entry the first line of OPEN_TRAILS naming it, where it is OPEN. Its
status is read from the latest later line (a roll line "**The open orders:**" excepted) that names it with a status word: a closing
word (DISCHARGED, CLOSED, RETIRED, SUPERSEDED, or a successor order that replaces it: "replaced by", "superseded by", "succeeded by",
"its successor" and a W-ORD name) reads CLOSED; an entry word (ENTERED, OPENED, RE-ENTERED, CARRIED) reads OPEN -- the author's
ruling of b723 (data/b723_author_words_preseal.txt (3)). A status word counts in the clause that names the order -- the words after the
name up to the next order's name not coordinated with it, a ';', or the clause's end at '. ', within 160 characters -- or standing
directly before the name; not negated (no "not", "no", "never", "nor", "unless" or "un-" within the 14 characters before it). Where
one line carries several, the last in reading order decides.

  orders.py read [--at REV] [--bank]     the orders, each OPEN or CLOSED with its closing line; --bank writes data/<act>_orders.txt
  orders.py line [--at REV]              the trail's open-orders line, from the output
  orders.py control [--at REV] [--bank]  (R333)(3)(i)'s controls: the output contains the last roll line's names (OPEN_TRAILS :16250's
                                         ten at b723) and the twenty of (R332)(14) as the previous act's events bank names them; a
                                         planted closing line (in memory) removes its order; a planted negated line does not
  ... [--beside REV2]                    read or control: the same rule at REV2 printed beside, its counts and the orders moved
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
ENTRY = re.compile(r'\b(RE-ENTERED|ENTERED|OPENED|CARRIED)\b(?!-)')   # ### the ruling's four entry words, matched as the closing words are
ENTRY_ANYCASE = re.compile(r'(?i)\b(RE-ENTERED|ENTERED|OPENED|CARRIED)\b(?!-)')   # ### printed beside as a yield, not a status
NEG = re.compile(r'(?i)(\bnot\b|\bno\b|\bnever\b|\bnor\b|\bunless\b|\bun-)')
SUCC = re.compile(r'(?i)(replaced by|superseded by|succeeded by|its successor)\W{0,12}`?(W-ORD-[A-Z0-9]+(?:-[A-Z0-9]+)*)')
ROLL = '**The open orders:**'
RULE = ('THE RULE (amended at b723 by the author`s ruling, data/b723_author_words_preseal.txt (3)): an order is a name W-ORD-<...>; its '
        'entry the first line of OPEN_TRAILS naming it, where it is OPEN; its status read from the latest later line, a roll line '
        'excepted, that names it with a status word -- a closing word (DISCHARGED, CLOSED, RETIRED, SUPERSEDED, or a successor replacing '
        'it) reading CLOSED, an entry word (ENTERED, OPENED, RE-ENTERED, CARRIED) reading OPEN -- in the clause naming it (after the name '
        'up to the next order`s name not coordinated with it, or a `;` or `. ` outside parentheses, within 160 characters; or the word '
        'standing directly before the name), not negated (not, no, never, nor, unless, un- within 14 characters before the word), the '
        'last in reading order deciding where a line carries several; the words read as a status in capitals (not a hyphenated compound, '
        'not "CLOSED FORM"). PRINTED BESIDE, NOT A STATUS: the roll lines carrying a CLOSED order after its closing line, and the lines '
        'carrying an entry word in lower or mixed case in a clause naming an order')


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


BEFORE = re.compile(r'\b(DISCHARGED|CLOSED|RETIRED|SUPERSEDED|RE-ENTERED|ENTERED|OPENED|CARRIED)\b[\s:*`—–-]*$')


LOCATOR = re.compile(r'(?i)\b(beneath|beside|above|below)\b((?:[\s`*"“”]|W-ORD-[A-Z0-9]+(?:-[A-Z0-9]+)*|,|\band\b|&)*)$')
LOCATOR_ON = False  # ### the author's ruling (3) of b723 (data/b723_author_words_preseal.txt (4)), TRIED and BROKEN by the record
#                   # ### (locator_trial below prints the cases), so the rule as ruled earlier stands; True reads the locator reading


def _in_locator(line, start):
    """True where the mention starting at `start` stands inside a locator phrase: a locator word before it with nothing between but
    spaces, backticks, asterisks, quotes and other order names coordinated with it (',', 'and', '&')."""
    return bool(LOCATOR.search(line[max(0, start - 200):start]))


def _state(word):
    return 'OPEN' if ENTRY.fullmatch(word) else 'CLOSED'


def _status(line, name):
    """the status a line gives `name` -- ('CLOSED' or 'OPEN', the word) -- or None: every status word in the clause after each mention of
    the name, or standing directly before it (nothing but spaces, ':', '*', '`' or a dash between), not negated; the last in reading
    order decides."""
    found = []
    for m in re.finditer(re.escape(name) + r'(?![A-Z0-9-])', line):
        if LOCATOR_ON and _in_locator(line, m.start()):
            continue
        after = _clause_after(line, m.end())
        for rx in (CLOSE, ENTRY):
            for c in rx.finditer(after):
                if not NEG.search(after[max(0, c.start() - 14):c.start()]):
                    found.append((m.end() + c.start(), c.group(1)))
        b0 = max(0, m.start() - 40)
        before = line[b0:m.start()]
        b = BEFORE.search(before)
        if b and not NEG.search(before[max(0, b.start() - 14):b.start()]):
            found.append((b0 + b.start(), b.group(1)))
        s = SUCC.search(after)
        if s and s.group(2) != name:
            found.append((m.end() + s.start(), 'successor %s' % s.group(2)))
    if not found:
        return None
    word = max(found)[1]
    return ('CLOSED' if word.startswith('successor ') else _state(word)), word


def _closer(line, name):
    """the closing reason a line gives `name`, or None (read beside by the controls)."""
    st = _status(line, name)
    return st[1] if st and st[0] == 'CLOSED' else None


def read(lines):
    """{name: dict(entry, status, decided_at, why, closed_at, reopened_at, named, rolls_after)} over every order the trail names, in entry
    order: the status from the latest line giving one (decided_at, why); closed_at the latest closing line; reopened_at the first line
    reading OPEN after a closing line."""
    orders, order = {}, []
    for i, l in enumerate(lines, 1):
        for n in set(NAME.findall(l)):
            if n not in orders:
                orders[n] = dict(entry=i, status='OPEN', decided_at=None, why=None, closed_at=None, reopened_at=None, named=0)
                order.append(n)
            orders[n]['named'] += 1
    for i, l in enumerate(lines, 1):
        if l.lstrip().startswith(ROLL):
            continue
        for n in set(NAME.findall(l)):
            o = orders[n]
            if i <= o['entry']:
                continue
            st = _status(l, n)
            if not st:
                continue
            if st[0] == 'OPEN' and o['status'] == 'CLOSED' and o['reopened_at'] is None:
                o['reopened_at'] = i
            o.update(status=st[0], decided_at=i, why=st[1])
            if st[0] == 'CLOSED':
                o['closed_at'] = i
    # ### beside the status, not changing it: the roll lines naming a CLOSED order after its closing line
    for n in order:
        o = orders[n]
        o['rolls_after'] = 0
        if o['status'] != 'CLOSED':
            continue
        for l in lines[o['decided_at']:]:
            if n in l and l.lstrip().startswith(ROLL):
                o['rolls_after'] += 1
    return [(n, orders[n]) for n in order]


def locator_trial(lines):
    """the author's ruling (3) of b723 tried: the orders read with the locator reading on and off, its two named controls, and every order
    whose status moves, with its deciding lines under the rule as ruled earlier; BROKEN where a moved order is not one the ruling names."""
    global LOCATOR_ON
    keep = LOCATOR_ON
    try:
        LOCATOR_ON = True
        on = dict(read(lines))
        LOCATOR_ON = False
        off = dict(read(lines))
    finally:
        LOCATOR_ON = keep
    e1, et = on.get('W-ORD-E1-CFG'), on.get('W-ORD-ENTRY-TAG-PRINTS')
    c1 = bool(e1) and e1['status'] == 'CLOSED' and e1['decided_at'] == 14068
    c2 = bool(et) and et['status'] == 'OPEN' and et['decided_at'] == 15684
    L = ['## THE LOCATOR READING TRIED (the author`s ruling (3) of b723: a name inside a line`s locator phrase -- after beneath, beside, above or '
         'below, other names coordinated with it -- takes no status from that line)',
         '  its control: W-ORD-E1-CFG CLOSED on its b659 discharge (:14068): %s (read %s, decided :%s %s)' % (
             'AS WANTED' if c1 else 'NOT AS WANTED', e1['status'], e1['decided_at'], e1['why']),
         '  its control: W-ORD-ENTRY-TAG-PRINTS OPEN on b707`s remainder (:15684): %s (read %s, decided :%s %s%s)' % (
             'AS WANTED' if c2 else 'NOT AS WANTED', et['status'], et['decided_at'], et['why'],
             ' -- OPEN BY DEFAULT ONLY: its discharge :15642 and its remainder :15684 both name it inside a locator phrase' if not et['decided_at'] else '')]
    moved = [n for n in on if on[n]['status'] != off[n]['status']]
    breaking = [n for n in moved if n not in ('W-ORD-E1-CFG', 'W-ORD-ENTRY-TAG-PRINTS')]
    L.append('  orders whose status moves under it: %d ; outside the two the ruling names: %d' % (len(moved), len(breaking)))
    for n in moved:
        d = off[n]['decided_at']
        t = lines[d - 1] if d else ''
        k = t.find(n)
        L.append('    %s: %s as ruled earlier (:%s %s) -> %s under the locator reading%s ; %s' % (
            n, off[n]['status'], d, off[n]['why'], on[n]['status'], ' -- BREAKS THE LOCATOR READING' if n in breaking else '',
            t[max(0, k - 60):k + 140].strip()))
    ok = c1 and c2 and not breaking
    L.append('### ### **THE LOCATOR READING: CONTROLS %d OF 2 AS WANTED ; CASES BREAKING IT %d ; %s.**' % (
        c1 + c2, len(breaking), 'HELD, IN FORCE' if ok else 'BROKEN BY THE RECORD, NOT IN FORCE: THE RULE AS RULED EARLIER STANDS'))
    return L, ok


def anycase_yield(lines):
    """the lines (a roll line excepted) carrying an entry word in lower or mixed case in a clause naming an order: printed, not read."""
    out = 0
    for l in lines:
        if l.lstrip().startswith(ROLL):
            continue
        for n in set(NAME.findall(l)):
            if any(ENTRY_ANYCASE.search(c) and not ENTRY.search(c) for c in
                   (_clause_after(l, m.end()) for m in re.finditer(re.escape(n) + r'(?![A-Z0-9-])', l))):
                out += 1
                break
    return out


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
         '### ' + RULE, '', '## THE ORDERS (name ; entry ; status ; the line deciding it and its word ; lines naming it)']
    for n, o in rows:
        beside = ''
        if o['reopened_at']:
            beside += ' ; OPEN AGAIN at :%d after a closing line' % o['reopened_at']
        if o['status'] == 'CLOSED' and o['rolls_after']:
            beside += ' ; ### ON %d ROLL LINE(S) AFTER ITS CLOSE' % o['rolls_after']
        L.append('  %-40s entry :%-6d %-7s %s ; named %d%s' % (n, o['entry'], o['status'],
                                                            (':%d %s' % (o['decided_at'], o['why'])) if o['decided_at'] else '-', o['named'], beside))
    conflict = [n for n, o in rows if o['status'] == 'CLOSED' and o['rolls_after']]
    reopened = [n for n, o in rows if o['reopened_at']]
    L += ['', '### PRINTED BESIDE, NOT READ: lines carrying an entry word in lower or mixed case in a clause naming an order: %d' % anycase_yield(
              trail(rev)),
          '', '### ### **ORDERS %d ; OPEN %d ; CLOSED %d ; OPEN AGAIN AFTER A CLOSING LINE %d%s ; CLOSED AND ON A ROLL AFTER %d%s.**' % (
              len(rows), len(op), len(rows) - len(op), len(reopened), (': ' + ', '.join(reopened)) if reopened else '',
              len(conflict), (': ' + ', '.join(conflict)) if conflict else '')]
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
        # ### THE SEAT'S, beside the five: the ruling's own clause, a closing line then an entry line, read OPEN
        again = dict(read(lines + ['PLANTED (in memory): `%s` DISCHARGED at the plant.' % x, 'PLANTED (in memory): `%s` RE-ENTERED after it.' % x]))
        case(again[x]['status'] == 'OPEN', 'PLANTED (THE SEAT`S, BESIDE THE FIVE): a closing line for %s, then a line naming it RE-ENTERED: the order OPEN' % x)
    L += ['', '### ### **THE ORDERS` CONTROLS: CASES %d ; AS WANTED %d ; %s.**' % (n, good, 'ALL AS WANTED' if good == n else 'NOT ALL AS WANTED')]
    return L, good == n


def main(argv):
    rev = argv[argv.index('--at') + 1] if '--at' in argv else 'HEAD'
    verb = argv[0] if argv else ''
    lines = trail(rev)
    if verb == 'read' or verb == 'control':
        rows = read(lines)
        L, op = report(rows, rev)
        L += ['', '## THE DECIDING LINES OF THE CLOSED ORDERS AND OF THE ORDERS OPEN AGAIN, EACH FOR A HAND READ (the order ; the line ; its '
                  'text, 300 characters around the name)']
        for nm, o in rows:
            if o['status'] == 'CLOSED' or o['reopened_at']:
                t = lines[o['decided_at'] - 1]
                k = t.find(nm)
                L.append('  %s ; %s :%d %s ; %s' % (nm, o['status'], o['decided_at'], o['why'], t[max(0, k - 120):k + 180].strip()))
        if verb == 'control':
            C, ok = control(lines, rev)
            L += [''] + C
            L += [''] + locator_trial(lines)[0]
        if '--beside' in argv:
            rev2 = argv[argv.index('--beside') + 1]
            rows2 = read(trail(rev2))
            st1, st2 = dict(rows), dict(rows2)
            op2 = [n for n, o in rows2 if o['status'] == 'OPEN']
            moved = [n for n in st2 if st1.get(n, {}).get('status') != st2[n]['status']]
            L += ['', '## BESIDE: THE SAME RULE AT %s (%s)' % (rev2, subprocess.run(['git', '-C', PP, 'rev-parse', '--short=8', rev2],
                                                                                   capture_output=True, text=True).stdout.strip())]
            L += ['  %s: %s at %s -> %s at %s ; :%s %s' % (n, st1[n]['status'] if n in st1 else 'ABSENT', rev, st2[n]['status'], rev2,
                                                       st2[n]['decided_at'], st2[n]['why']) for n in moved]
            L += ['### ### **AT %s: ORDERS %d ; OPEN %d ; CLOSED %d ; STATUS MOVED FROM %s %d.**' % (
                rev2, len(rows2), len(op2), len(rows2) - len(op2), rev, len(moved))]
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
