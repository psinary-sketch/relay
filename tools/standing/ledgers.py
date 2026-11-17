# -*- coding: utf-8 -*-
"""tools/standing/ledgers.py -- v1.35.0, (R366)(6)[U2]: THE LEDGERS CARRY FINDINGS (relay data/b754_rules.txt (11)), in force from b757, the
act that follows its change (the author's word beside the row, relay data/b754_author_answers.txt :121).

THE RULE, as the row quotes it: "The corrigendum's entry in FINDINGS is its head line, its counts, every CLAIM item in full and the repairs
landed with their controls, its CLOSE items by count with the relay bank that holds them; the weight line is the closing's head line and one
sentence; an act's trail prints its defects by count and by the letters of the CLAIM items, the sealed tools and the open orders by count with
their banks, and the Next in full. The relay's banks hold every row as now; no past entry or trail is rewritten."

WHAT THIS MODULE WRITES, from b757 (before it every function returns the form the act's composer gives, unchanged):
  the trail      trail(): the composed trail's three long lines put by count -- the Defects line (relay data/<act>_defects.txt): the
                 lettered rows by count, the CLAIM items by letter, the CLOSE items by count, and the two owners' counts the suite's arm
                 reads (defects_body); the sealed tools' line: their count and the count agreeing with the seal's hashes, each tool by name
                 and sha256 in relay data/<act>_seal_hashes.json; the open orders' roll line: their count, each by name in relay
                 data/<act>_trail.json (`open_orders`), which the record's trail route writes beside the landing (rows()). Every other line,
                 the Next in full among them, stands as composed.
  the entry      corrigendum(): the corrigendum's entry for the previous act composed from its banks -- the head line, the counts by bank,
                 every CLAIM item in full, the repairs landed with their controls, the CLOSE items by count with the banks that hold them
                 -- for the act's c1 route to land (carry.py stubs the route at every act; the act writes it under its ruling).
  the readers    defects_body() and owners_of() are the one reading of the Defects line for the record's dry check and the suite's two
                 trail arms (G-TRAIL-DEFECTS, the trail-equality arm), so the line and its readers move together.
The weight line is the act's c1 route's under (R366)(1) already: the closing's head line and one sentence. No past entry or trail is read or
rewritten by anything here.
"""
import os
import re
import sys

NL = '\n'
VERSION = 'v1.35.0'
FROM_ACT = 757
RULE = 'relay data/b754_rules.txt (11)'
DEFECTS_LINE = re.compile(r'^\*\*Defects\*\* \(relay data/(b\d+)_defects\.txt\): (.*)\.$')
SEALED_LINE = re.compile(r'^\*\*The sealed tools at the record:\*\* (.*)\.$')
SEALED_ITEM = re.compile(r'([\w.-]+) (agree|differ|absent)\b')   # ### v1.36.2: the one pattern of trail()'s rows and seal_carried()'s names
ROLL = '**The open orders:**'
ORDER = re.compile(r'`(W-ORD-[A-Z0-9-]+)`')
TAG = re.compile(r"^\(([a-z]'*|\d+)\) (THE [A-Z’' ]+?) \[(CLAIM|CLOSE) ; ([^\]]*)\]:? ?(.*)$")
KIND = re.compile(r"\(([a-z])\) THE (NAVIGATOR|SEAT)[’']S")
OWNERS = re.compile(r'the navigator’s (\d+), the seat’s (\d+)')
LAST = {}   # ### the rows of the last trail() composition, for rows()


def in_force(act):
    try:
        return int(str(act).lstrip('b')) >= FROM_ACT
    except ValueError:
        return False


def _owners(rows):
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import act_close as AC
    o = AC.defect_owners(rows)
    return o['NAVIGATOR'], o['SEAT']


def tags(rows):
    """[(letter, CLAIM|CLOSE)] of the defects' heads as the trail carries them."""
    out = []
    for r in rows or []:
        m = TAG.match((r or '').strip())
        if m:
            out.append((m.group(1), m.group(3)))
    return out


def defects_body(act, rows):
    """the Defects line's text after its colon: before b757 every row's head joined (the form b652 to b756 printed); from b757 the rows by
    count, the CLAIM items by letter, the CLOSE items by count, and the owners' counts."""
    if not in_force(act):
        return '; '.join(rows or []) or 'none'
    t = tags(rows)
    claim = ['(%s)' % x for x, k in t if k == 'CLAIM']
    nav, seat = _owners(rows or [])
    return '%d lettered; CLAIM %d%s; CLOSE %d; the navigator’s %d, the seat’s %d; each row in full in the bank' % (
        len(rows or []), len(claim), (': ' + ', '.join(claim)) if claim else '', sum(1 for _x, k in t if k == 'CLOSE'), nav, seat)


def owners_of(act, body):
    """(navigator, seat) as the Defects line's text carries them: before b757 by the heads' owner words, from b757 by the counts printed."""
    if not in_force(act):
        got = KIND.findall(body or '')
        return sum(1 for _x, o in got if o == 'NAVIGATOR'), sum(1 for _x, o in got if o == 'SEAT')
    m = OWNERS.search(body or '')
    return (int(m.group(1)), int(m.group(2))) if m else (None, None)


def trail(act, text, rows):
    """the composed trail with its three long lines by count, from b757; before, the text unchanged. LAST holds the rows the lines leave."""
    LAST.clear()
    if not in_force(act):
        return text
    out = []
    for l in (text or '').split(NL):
        d, s = DEFECTS_LINE.match(l), SEALED_LINE.match(l)
        if d and d.group(1) == act:
            LAST['defects'] = list(rows or [])
            l = '**Defects** (relay data/%s_defects.txt): %s.' % (act, defects_body(act, rows))
        elif s:
            items = SEALED_ITEM.findall(s.group(1))
            LAST['sealed'] = [dict(tool=t_, at_record=v) for t_, v in items]
            l = '**The sealed tools at the record:** %d, %d of them agreeing with the hash recorded at the seal (relay data/%s_seal_hashes.json, each tool by name and sha256).' % (
                len(items), sum(1 for _t, v in items if v == 'agree'), act)
        elif l.lstrip().startswith(ROLL) and ORDER.search(l):
            names = ORDER.findall(l)
            LAST['open_orders'] = names
            l = '%s %d open at PLACE-papers main with this trail’s lines (tools/standing/orders.py’s output), each by name in relay data/%s_trail.json.' % (
                ROLL, len(names), act)
        out.append(l)
    return NL.join(out)


def rows(act):
    """the trail bank's fields for the rows the trail puts by count (from b757; else none)."""
    if not in_force(act) or not LAST:
        return {}
    return dict(open_orders=list(LAST.get('open_orders') or []), sealed=list(LAST.get('sealed') or []), ledgers=VERSION)


def trail_name(tool):
    """the name trail() writes a sealed tool under: what SEALED_ITEM captures from "<tool> agree" (a path's last part: standing/act.py is
    act.py, acts/b757.py is b757.py). Pure."""
    m = SEALED_ITEM.findall('%s agree' % tool)
    return m[-1][0] if m else tool


def seal_carried(sealed, tail, tj):
    """v1.36.2, (R368)(6), b757 events (29): G-TRAIL-CARRIES-SEAL's one reading. Where the trail bank carries the sealed tools by name (its
    `sealed` rows, written by trail() and rows() since v1.35.0, from b757): every tool the act seals among them under the name trail() writes
    (trail_name), as many rows of that name as tools, each `agree`. Where it carries none (a trail before v1.35.0, b756's and earlier):
    "<tool> agree" in the trail record's text for each, as the arm read before. `sealed` the act's sealed tools (the worklist's SEALED),
    `tail` the trail record's text, `tj` the trail bank. Pure."""
    if not sealed:
        return False
    rows = (tj or {}).get('sealed')
    if rows is None:
        return all(('%s agree' % t) in (tail or '') for t in sealed)
    by, want = {}, {}
    for r in rows:
        by.setdefault(r.get('tool'), []).append(r.get('at_record'))
    for t in dict.fromkeys(sealed):   # ### each distinct tool once (a worklist's SEALED may name a tool twice)
        want[trail_name(t)] = want.get(trail_name(t), 0) + 1
    return all(by.get(n) == ['agree'] * k for n, k in want.items())


# ================================================================================ THE CORRIGENDUM'S ENTRY
ROW = re.compile(r"^    \(((?:[a-z]'*)|\d+)\) (THE [A-Z’' ]+?) \[(CLAIM|CLOSE) ; ([^\]]*)\]:? ?(.*)$")


def bank_rows(path):
    """the lettered or numbered rows of a defects or events bank, each row's continuation lines (five spaces or more) joined:
    [(id, owner, CLAIM|CLOSE, column, the row's text whole)]."""
    L = open(path, encoding='utf-8').read().replace('\r', '').split(NL)
    out = []
    for i, l in enumerate(L):
        m = ROW.match(l)
        if not m:
            continue
        j = i + 1
        while j < len(L) and L[j].startswith('     ') and not ROW.match(L[j]):
            j += 1
        whole = ' '.join(x.strip() for x in L[i:j])
        out.append((m.group(1), m.group(2), m.group(3), m.group(4), whole))
    return out


def corrigendum(prev, d_dir, title, repairs, banks=('defects', 'events')):
    """the corrigendum's entry for act `prev`, composed from its banks in [U2]'s form: (lines, tally). `repairs`: [(what, relay commit,
    controls as wanted, controls run, the controls' bank)]."""
    tally, claims, lines = {}, [], [title, '']
    for b in banks:
        name = '%s_%s.txt' % (prev, b)
        rs = bank_rows(os.path.join(d_dir, name))
        tally[b] = dict(rows=len(rs), claim=sum(1 for r in rs if r[2] == 'CLAIM'), close=sum(1 for r in rs if r[2] == 'CLOSE'), name=name)
        claims += [(name, r) for r in rs if r[2] == 'CLAIM']
    lines.append('**The counts:** %s.' % '; '.join('relay data/%s, %d %s: CLAIM %d, CLOSE %d' % (
        t['name'], t['rows'], 'lettered' if b == 'defects' else 'rows', t['claim'], t['close']) for b, t in tally.items()))
    lines += ['', '**The CLAIM items, in full:** %s' % ('none.' if not claims else '')]
    for name, r in claims:
        lines.append('- relay data/%s %s' % (name, r[4]))
    lines += ['', '**The repairs landed, with their controls:** %s' % ('none.' if not repairs else '')]
    for what, commit, good, n, bank in repairs or ():
        lines.append('- %s, relay %s, its controls %d of %d as wanted (relay data/%s).' % (what, commit[:8], good, n, bank))
    lines += ['', '**The CLOSE items, by count:** %d, every row in full in %s.' % (
        sum(t['close'] for t in tally.values()), ' and '.join('relay data/%s' % t['name'] for t in tally.values()))]
    return lines, dict(tally=tally, claims=len(claims), repairs=len(repairs or ()))
