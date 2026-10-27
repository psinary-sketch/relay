# -*- coding: utf-8 -*-
"""b717_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R327)(3): b716's nineteen events after its lock and seal (relay data/b716_events.txt,
rows (1)-(19) at four spaces) and b716's eighteen defects (relay data/b716_defects.txt, (a)-(r)), answered by one generated FINDINGS entry,
each item tagged CLAIM or CLOSE under (R327)(2) (standing clauses v6 row (80)) and NEW or REPEAT with the act and letter of its class. A CLAIM
item names its repair or reads "carried" with its reason; a CLOSE item is listed by its class for the toolset's v1.2.0, recorded and counted,
not repaired. The navigator reads all nineteen events as CLOSE ((R327)(3)); the seat's tags are read from the banks, each difference printed,
the seat's reading standing. The counter line prints CLAIM n and CLOSE m over the thirty-seven items.
### Carried from tools/b716_corrigendum.py by diff (data/b717_carry_corrigendum.txt) and rewritten whole by the Write tool: b716's tool
### lettered b715's events (r)-(z) and named (R326)(3)'s repairs; (R327)(3) orders tags, not letters, and names no repair by clause.
### THE CHECKS BEFORE ANY WRITE: the events bank's rows at four spaces number nineteen, (1)-(19), each head carrying its needle; the defects
### bank's letters (a)-(r), each head carrying its needle; each REPEAT's cited row present in the bank it names (the letter's row at four
### spaces, or the event's row); the corrigenda bank's last row (36). Any miss: nothing composed.
### Routes: `dry` prints the entry, the bank and the corrigenda row; `write` lands the entry on FINDINGS through b717_record's guarded landing
### and writes data/b717_corrigendum.txt (.json). The corrigenda bank's row (37) is appended by the seat through the Edit tool from the row
### this tool prints.
"""
import json
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b678_corrigendum as C78   # noqa: E402  ### b678's tool, imported unchanged: rd
from b652_record import conv     # noqa: E402  ### the one conversion
import b717_record as REC         # noqa: E402  ### the guarded landing, the letters reader

TITLE = ('## Corrigendum to b716’s record (relay data/b716_events.txt and data/b716_defects.txt): nineteen events and eighteen defects, '
         'each CLAIM or CLOSE and NEW or REPEAT, under (R327)(2)-(3)')
PREV_LETTERS = list('abcdefghijklmnopqr')
CORRIGENDA_LAST = 36

# ### the classes of the CLOSE items, gathered for tools/standing/ v1.2.0 ((R327)(3), (11))
CLASSES = {
    'READ': 'a file read outside the Read tool or outside its limit and offset (row (19)): a shell filter, a grep, the Grep tool, git diff, an interpreter`s print, a limit with no offset',
    'HOOK': 'a call the hook refused before it ran (row (77)): a pipe, a redirect, an environment prefix, a Read with no limit -- its refusal written into the act`s refusal bank',
    'CARRY': 'a figure, needle or floor carried by the act-name substitution and not bumped to the act it now serves',
    'FORM': 'a writer and its reader in two forms: a bank, a face line, a trail sentence or a table row written outside the form the standing reader takes',
    'CONTROL': 'an arm`s pattern or control that cannot fire, or fires on a bank it should not read',
    'ORDER': 'the close`s own sequencing: a step omitted, a commit read on the wrong side of the lock, two remote reads in one command, a stale capture, prompts counted two ways',
}

# ### b716's events: (row, the head's needle, the seat's tag, NEW or (act, letter) of its class, the class)
EVENTS = [
    (1, 'AT THE PRE-RUN: G-NOTHING-RAN-AHEAD', 'CLOSE', ('b711', 'event', 'the face names every pre-lock commit (b711`s trap 2)'), 'ORDER'),
    (2, 'AT THE PRE-RUN: G-ROOTDRY-READY', 'CLOSE', None, 'FORM'),
    (3, 'AT THE PRE-RUN: G-RECEIPT-IN-FULL', 'CLOSE', ('b716', 'n', None), 'CARRY'),
    (4, 'AT THE PRE-RUN: G-PRIOR-CLOSED-PUSHED', 'CLOSE', ('b716', '(3)', None), 'CARRY'),
    (5, 'AT THE PRE-RUN: G-CLOSING-DRY-STEP', 'CLOSE', ('b716', '(3)', None), 'CARRY'),
    (6, 'AT THE PRE-RUN: G-REGISTRATIONS-FIRST', 'CLOSE', None, 'CONTROL'),
    (7, 'AT THE PRE-RUN: G-SCORER-READS-BANKS', 'CLOSE', None, 'FORM'),
    (8, 'AT THE PRE-RUN: G-RULE-REMOTE-REREAD', 'CLOSE', None, 'ORDER'),
    (9, 'THE GREP TOOL, AFTER THE LOCK', 'CLOSE', ('b716', 'f', None), 'READ'),
    (10, 'AFTER THE SEAL', 'CLOSE', ('b716', 'm', None), 'HOOK'),
    (11, "THE TRAIL'S WORDING", 'CLOSE', ('b716', 'r', None), 'FORM'),
    (12, "THE DESK'S N4 FIGURES", 'CLOSE', ('b715', 'event', 'b715`s desk printed the same shapes (the row`s own words)'), 'ORDER'),
    (13, "G-PP-SCOPE'S POSITIVE CONTROL PASSES", 'CLOSE', None, 'CONTROL'),
    (14, 'G-ARM-SECONDS-BANKED FAILS', 'CLOSE', None, 'ORDER'),
    (15, 'G-ANSWERS-BEFORE-WRITES FAILS', 'CLOSE', None, 'ORDER'),
    (16, 'G-SEALED-AFTER-COMPONENTS FAILS', 'CLOSE', None, 'ORDER'),
    (17, "THE MIRROR'S MANIFEST CONTROL", 'CLOSE', None, 'CONTROL'),
    (18, 'THIS BANK WRITTEN OUTSIDE', 'CLOSE', None, 'FORM'),
    (19, "THE CLOSING'S STANDING REPORT LINE", 'CLOSE', ('b716', '(3)', None), 'CARRY'),
]

# ### b716's defects: (letter, the head's needle, the seat's tag, NEW or (act, letter), the class, the repair or carried for a CLAIM item)
REPAIRED_BEFORE = 'repaired at b716 before any commit carried it (the bank as committed is the second run`s, data/b716_defects.txt row (%s))'
DEFECTS = [
    ('a', 'A COMMAND WITH A REDIRECT', 'CLOSE', ('b715', 'a', None), 'HOOK', None),
    ('b', 'A FILE READ THROUGH A SHELL FILTER', 'CLOSE', ('b708', 'python -c', 'b708`s trap: a read through an interpreter, row (19)`s class'), 'READ', None),
    ('c', "A FILE'S LINES PRINTED BY A SHELL GREP", 'CLOSE', ('b716', 'b', None), 'READ', None),
    ('d', "TRACKED FILES' CHANGED LINES READ THROUGH", 'CLOSE', ('b716', 'c', None), 'READ', None),
    ('e', 'A COMMAND PREFIXED BY AN ENVIRONMENT VARIABLE', 'CLOSE', ('b716', 'a', None), 'HOOK', None),
    ('f', "FILES' LINES PRINTED BY THE GREP TOOL", 'CLOSE', ('b716', 'c', None), 'READ', None),
    ('g', "A TOOL'S LINES PRINTED BY `git grep`", 'CLOSE', ('b716', 'c', None), 'READ', None),
    ('h', "FILES READ THROUGH AN INTERPRETER'S PRINT", 'CLOSE', ('b716', 'b', None), 'READ', None),
    ('i', 'A LISTING WITH A REDIRECT AND A PIPE', 'CLOSE', ('b716', 'a', None), 'HOOK', None),
    ('j', "ERRATA'S LINES PRINTED BY `git grep`", 'CLOSE', ('b716', 'c', None), 'READ', None),
    ('k', "THE FEDERATION PRICE'S FIRST BANK CLAIMED A CONTROL", 'CLAIM', None, None, REPAIRED_BEFORE % 'k'),
    ('l', "THE LEAN-COUNT PRICE'S FIRST BANK READ MATCHER MISSES", 'CLAIM', ('b505', 'trap', 'b505`s fixture bar and the standing trap "print the needle`s yield" (the row`s own words)'), None, REPAIRED_BEFORE % 'l'),
    ('m', 'A READ CALL WITH NO LIMIT', 'CLOSE', ('b716', 'e', None), 'HOOK', None),
    ('n', "THE CARRIED WORKLIST KEPT b715'S STEP-ZERO HASHES", 'CLOSE', ('b713', 'trap', 'b713`s trap "bump carried figures" and b715`s carried constants (the row`s own words)'), 'CARRY', None),
    ('o', 'READ CALLS GIVEN A LIMIT AND NO OFFSET', 'CLOSE', ('b715', 'm', None), 'READ', None),
    ('p', 'THE COVERAGE TABLE NAMES THE WRONG MODULE', 'CLOSE', None, 'FORM', None),
    ('q', "A TOOL'S LINES PRINTED BY THE GREP TOOL", 'CLOSE', ('b716', 'f', None), 'READ', None),
    ('r', "THE TRAIL'S RESOLVED LINE WRITTEN OUTSIDE", 'CLOSE', None, 'FORM', None),
]
NAVIGATOR_EVENTS = 'CLOSE'


def _event_rows(text):
    """the events bank's rows: {n: head}, a row a line opening four spaces and '(n) '."""
    out = {}
    for l in text.replace(chr(13), '').split(NL):
        m = re.match(r'^    \((\d+)\) (.*)$', l)
        if m:
            out[int(m.group(1))] = m.group(2)
    return out


def _letter_rows(act):
    p = os.path.join(D, '%s_defects.txt' % act)
    t = C78.rd(p).replace(chr(13), '') if os.path.exists(p) else ''
    return dict((m.group(1), m.group(2)) for m in re.finditer(r"(?m)^\s{4}\(([a-z]'?)\) (.*)$", t))


def _ref_ok(ref):
    """a REPEAT's cited row present: an act's letter in its defects bank, b716's event (n) in its events bank, or a trap or event named by
    the row's own words (read from the item's head, checked in compose)."""
    if not ref:
        return True
    act, what, words = ref
    if words:
        return True
    if what.startswith('('):
        return int(what.strip('()')) in _event_rows(C78.rd(os.path.join(D, '%s_events.txt' % act)))
    return what in _letter_rows(act)


def compose():
    ev = _event_rows(C78.rd(os.path.join(D, 'b716_events.txt')))
    miss_e = [n for n, h, _t, _r, _c in EVENTS if not ev.get(n, '').startswith(h)]
    dl = _letter_rows('b716')
    miss_d = [x for x, h, _t, _r, _c, _w in DEFECTS if h not in dl.get(x, '')]
    bad_ref = [r[:2] for r in [e[3] for e in EVENTS] + [d[3] for d in DEFECTS] if not _ref_ok(r)]
    cr = [int(m.group(1)) for m in re.finditer(r'(?m)^  \((\d+)\) ', C78.rd(os.path.join(D, 'b675_corrigenda.txt')))]
    bad = [k for k, v in (('the nineteen event rows', sorted(ev) == list(range(1, 20))), ('each event`s head', not miss_e),
                          ('b716`s eighteen letters', sorted(dl) == PREV_LETTERS), ('each defect`s head', not miss_d),
                          ('each REPEAT`s cited row', not bad_ref), ('the corrigenda bank`s last row (%d)' % CORRIGENDA_LAST, cr and max(cr) == CORRIGENDA_LAST)) if not v]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (events %s ; event heads missed %s ; letters %s ; defect heads missed %s ; refs %s)' % (
            bad, sorted(ev), miss_e, sorted(dl), miss_d, bad_ref))
    return dict(events=ev, letters=dl)


def _col(ref):
    if not ref:
        return 'NEW'
    act, what, words = ref
    if words:
        return 'REPEAT of %s, %s' % (act, words)
    if what.startswith('('):
        return 'REPEAT of %s event %s (relay data/%s_events.txt)' % (act, what, act)
    return 'REPEAT of %s (%s) (relay data/%s_defects.txt)' % (act, what, act)


def counts():
    items = [e[2] for e in EVENTS] + [d[2] for d in DEFECTS]
    rep = sum(1 for e in EVENTS if e[3]) + sum(1 for d in DEFECTS if d[3])
    return items.count('CLAIM'), items.count('CLOSE'), rep, len(items)


def differences():
    return [(n, t) for n, _h, t, _r, _c in EVENTS if t != NAVIGATOR_EVENTS]


def _entry_lines(s):
    nc, nl, rep, n = counts()
    diff = differences()
    L = ['*b716’s events bank (relay data/b716_events.txt) carries nineteen rows (1)-(19), entered after its lock and seal and not lettered, '
         'and its defects bank (relay data/b716_defects.txt) eighteen letters (a)-(r). Under (R327)(2) each item is tagged CLAIM, where it touches '
         'a statement, a pin, a grade, a registration, a computed figure, or a sentence a reader of the corpus meets, or CLOSE, where it touches '
         'the close’s own record of itself and nothing a reader of the corpus meets; and NEW or REPEAT with the act and letter of its class. A '
         'CLAIM item names its repair or reads carried with its reason; a CLOSE item is recorded and counted, its class gathered for the '
         'toolset’s v1.2.0 and not repaired, and no arm is added for it. The navigator reads all nineteen events as CLOSE; the seat’s tags, '
         'read from the banks, differ from that reading at %s.*' % ('no event' if not diff else ', '.join('(%d)' % d[0] for d in diff)), '',
         '**b716’s events:**', '']
    for k, h, t, r, c in EVENTS:
        L += ['**(%d) %s** (relay data/b716_events.txt, row (%d); %s; %s; class %s).' % (k, h, k, t, _col(r), c)]
    L += ['', '**b716’s defects:**', '']
    for x, _h, t, r, c, w in DEFECTS:
        head = re.split(r'\. ', s['letters'][x], 1)[0].replace("THE SEAT'S: ", '')
        L += ['**(%s) %s** (relay data/b716_defects.txt; %s; %s%s).%s' % (
            x, head.rstrip('.'), t, _col(r), ('; class %s' % c) if c else '', (' ' + w[0].upper() + w[1:] + '.') if t == 'CLAIM' else '')]
    L += ['', '**The CLOSE classes for the toolset’s v1.2.0** (b718’s, (R327)(11)):', '']
    for k, v in CLASSES.items():
        ev = ['(%d)' % e[0] for e in EVENTS if e[4] == k]
        de = ['(%s)' % d[0] for d in DEFECTS if d[4] == k]
        L += ['- **%s** -- %s: events %s; defects %s.' % (k, v, ', '.join(ev) or 'none', ', '.join(de) or 'none')]
    L += ['', '**The counter:** CLAIM %d, CLOSE %d over the %d items (nineteen events, eighteen defects); REPEAT %d of %d. The CLAIM items, '
          'b716’s (k) and (l), each a price bank’s first run, were repaired before any commit carried them; nothing is carried.' % (nc, nl, n, rep, n), '',
          ('*Filed at b717 on the author’s ruling `(R327)`(2)-(3): generated by relay `tools/b717_corrigendum.py`, written whole at b717 in the '
           'form (R327)(3) orders, from b716’s events and defects banks read unedited; banked as relay `data/b717_corrigendum.txt`, the '
           'corrigenda bank `data/b675_corrigenda.txt` appended at row (37). It answers b716’s record; no sealed tool, face, trail or root-named '
           'bank of b716 is edited.*')]
    return L


def entry_text(s):
    return NL + TITLE + NL + NL + NL.join(_entry_lines(s)) + NL


def bank_landed(s, ln):
    """the banks for an entry already on FINDINGS at :ln (b717's first `write` landed it without its leading blank line and stopped before
    its banks, defect (p); the blank line added by the Edit tool): the text at :ln on is read and must equal the entry's, line for line."""
    import io
    import b717_worklist as K
    F = io.open(os.path.join(K.PP, 'FINDINGS.md'), encoding='utf-8').read().replace(chr(13), '').split(NL)
    want = conv(entry_text(s)).strip(NL).split(NL)
    have = F[ln - 1:ln - 1 + len(want)]
    if have != want:
        sys.exit('### FINDINGS :%d DOES NOT CARRY THE ENTRY LINE FOR LINE -- NOTHING BANKED' % ln)
    return True


ROW = ('  (37) b716\'s record (relay data/b716_events.txt, rows (1)-(19), and data/b716_defects.txt, (a)-(r)): every item tagged CLAIM or\n'
       '      CLOSE under (R327)(2) and NEW or REPEAT; CLAIM %d ((k), (l), each repaired at b716 before any commit), CLOSE %d, by class for\n'
       '      v1.2.0 (READ, HOOK, CARRY, FORM, CONTROL, ORDER); REPEAT %d of %d; the navigator`s reading of the events (all CLOSE) and the seat`s\n'
       '      differ at %s. THE CORRECTION: FINDINGS :%s, relay data/b717_corrigendum.txt.')


def _row_text(ln):
    nc, nl, rep, n = counts()
    d = differences()
    return ROW % (nc, nl, rep, n, 'no event' if not d else ', '.join('(%d)' % x[0] for x in d), ln)


def bank_lines(s, landed_line=None):
    nc, nl, rep, n = counts()
    L = ['b717 -- THE CORRIGENDUM ENTRY FOR b716`S EVENTS AND DEFECTS, (R327)(2)-(3) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the figures read before the write: the event rows %s ; b716`s letters %s ; every REPEAT`s cited row found ; the corrigenda bank`s last row (%d).' % (
             len(s['events']), ''.join(sorted(s['letters'])), CORRIGENDA_LAST),
         '### THE NAVIGATOR`S READING AND THE SEAT`S: all nineteen events CLOSE by the navigator ; the seat`s differences %s.' % (differences() or 'NONE'), '']
    L += ['  ' + l for l in _entry_lines(s)]
    L += ['', '### ### **ITEMS %d: EVENTS 19, DEFECTS 18 ; CLAIM %d, CLOSE %d ; REPEAT %d, NEW %d ; THE EVENTS AND DEFECTS BANKS UNEDITED ; THE ENTRY AT FINDINGS :%s.**' % (
        n, nc, nl, rep, n - rep, landed_line if landed_line else 'NOT YET WRITTEN')]
    return L


def _put(name, data):
    import act_membrane as MEM
    p = os.path.join(D, name)
    MEM.guard_path('b717', p, REC.R.ROOT_EXCLUDE)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data.encode('utf-8'))
    os.replace(p + '.tmp', p)


def main(route):
    s = compose()
    text = entry_text(s)
    if route == 'dry':
        REC.R.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text))
        print(NL.join(bank_lines(s)))
        print(_row_text('NOT YET WRITTEN'))
        return
    if route == 'banked' and len(sys.argv) > 2:
        ln = int(sys.argv[2])
        bank_landed(s, ln)
    elif route == 'write':
        REC.land([('FINDINGS.md', TITLE, text)], 'b717_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
        ln = (REC.jl('b717_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    else:
        sys.exit('usage: b717_corrigendum.py dry | write | banked <line>')
    L = bank_lines(s, ln)
    _put('b717_corrigendum.txt', NL.join(L) + NL)
    nc, nl, rep, n = counts()
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE, claim=nc, close=nl, repeat=rep, items=n,
             events=[dict(row=e[0], tag=e[2], navigator=NAVIGATOR_EVENTS, column=_col(e[3]), cls=e[4]) for e in EVENTS],
             defects=[dict(letter=d[0], tag=d[2], column=_col(d[3]), cls=d[4], repair=d[5]) for d in DEFECTS],
             classes=CLASSES, differences=differences(), row=37)
    _put('b717_corrigendum.json', json.dumps(j, indent=1, ensure_ascii=False) + NL)
    print(L[-1])
    print(_row_text(ln))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'dry')
