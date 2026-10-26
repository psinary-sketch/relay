# -*- coding: utf-8 -*-
"""b714_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R324)(5): b713's events after its seal (relay data/b713_events.txt, sixteen starting
lines) and the one item the ruling adds, answered by one generated FINDINGS entry in b678's corrigendum form, in the banks' words, every item
carrying a column NEW or REPEAT. Twelve are lettered as defects, each with its owner, (o)-(z) after b713's fourteen letters (a)-(n) (relay
data/b713_defects.txt), the letters from tools/act_letters.py (repair (v), the one lettering the suite imports too); five are entered as
records, unlettered. Each lettered item names the repair of (R324)(6) that takes it up, by its row in relay data/standing_clauses_v5.txt
(committed alone at step zero, 8b8c7217), or states that (R324)(5) names none; the repairs' diffs and two-instance controls are banked after
this entry in data/b714_tool_repairs.txt, Component 1's order. b713's events bank, its defects bank, its sealed face, its trail record
(PLACE-papers OPEN_TRAILS :15928) and every root-named bank unedited.

### THE NEW OR REPEAT COLUMN: an item is REPEAT where the corrigenda bank (relay data/b675_corrigenda.txt, rows (1)-(33), the record of every
### earlier act's lettered corrections since b675) carries an item of its class, and the column names that act, its letter and the row; the
### row's text is read and its needle checked before any write. NEW where no row carries one. The evidence set is that bank alone: a class
### that stood only as an unlettered event of an earlier act, in no row, reads NEW here, and the entry says so.
### The added item's source: the ferry :15 (relay data/b714_ferry.txt) and three Edit calls on relay data/b713_closing.txt in the session's
### transcript (lines 18835, 18836, 18850), read at compose time.
### Written whole by the Write tool at b714 (b708-b713 wrote theirs the same way). b678's reader `rd` IMPORTED unchanged. Routes: `dry` -> the
### entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b714_record's guarded landing,
### data/b714_corrigendum.txt (.json). The corrigenda bank's row (34) is appended by the seat through the Edit tool from the line this tool
### prints (ROW). It writes those two banks and the one FINDINGS entry.
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
import b714_worklist as K         # noqa: E402
import b714_record as REC         # noqa: E402  ### the guarded landing, the letters reader
import act_letters as AL          # noqa: E402  ### (R324)(6)(v): the one lettering

TITLE = ('## Corrigendum to b713’s record after its seal (relay data/b713_events.txt): sixteen events and one added item, twelve lettered '
         '(o)-(z) with their owners, five entered as records, each NEW or REPEAT, under (R324)(5)')
PREV_LETTERS = list('abcdefghijklmn')
# ### the repairs of (R324)(6) by their rows of standing clauses v5
V5_ROWS = {'i': 74, 'ii': 75, 'iii': 76, 'iv': 77, 'v': 78}
# ### the lettered items, (R324)(5)'s order: (events line or None for the added item, the head's needle, the owner, the repair's (R324)(6)
# ### item or None, the item's words as the ruling names it, the column: None for NEW or (act, letter, corrigenda row, the row's needle))
LETTERED = (
    (3, "THE PRE-RUN'S standing-a", 'THE ARMS’', None, 'four arms failing on real state at the pre-run',
     ('b691', 'l', 5, "Lettered b691's defect (l)")),
    (21, "THE PRE-RUN ON b712'S BANKS", 'THE ARM’S', None, 'G-TOOL-REPAIRS’ TypeError on b712’s banks',
     ('b712', 'w', 33, '(w) the gate`s work in two commits read as one, the arm`s')),
    (54, 'THE PRE-PUSH SUITE, standing-a: G-NEXT-ACT-NAMED', 'THE SUITE’S', 'ii', 'the next act carried unbumped into the sealed suite',
     ('b702', 'j', 22, "lettered b702's (j), THE SEAT'S -- the last export before b702's")),
    (56, 'THE PRE-PUSH SUITE, standing-a: G-ACTROOT-BANKED', 'THE SUITE’S', 'ii', 'the chain row count carried unbumped into the sealed suite',
     ('b702', 'j', 22, "lettered b702's (j), THE SEAT'S -- the last export before b702's")),
    (58, 'THE PRE-PUSH SUITE, standing-b3', 'THE SUITE’S', 'ii', 'the root-check range carried unbumped into the sealed suite',
     ('b702', 'j', 22, "lettered b702's (j), THE SEAT'S -- the last export before b702's")),
    (61, 'THE COMBINED PRE-RUN BANK', 'THE ORDER’S', 'iii', '--combine not run before the seal',
     ('b712', "a'", 33, 'components route skipped before the record commit, the seat`s')),
    (64, 'THE PRE-PUSH SUITE, act: G-CORRIGENDUM-ENTERED', 'THE LETTERING’S', 'v', 'the corrigendum lettered a’ where the suite reads a′',
     ('b705', 'o', 26, 'G-ENTRY-TITLE-FORM (its needle in lower case against the entry')),
    (68, 'G-ROOTDRY-READY fails on the record as it stands', 'THE FACE’S', 'iii', 'the root’s dry run READY False undeclared on the face’s list',
     ('b698', 'c', 11, "Lettered b698's defect (c)")),
    (25, 'THE THROUGHSTONE (b)', 'THE NAVIGATOR’S', None,
     'the author’s word at the root’s prompt assuming a committed n* for the pairs beyond reach',
     ('b699', 'e', 16, "Lettered the navigator's (e)")),
    (29, 'THE THROUGHSTONE (e)', 'THE NAVIGATOR’S', None, 'the author’s word at the root’s prompt assuming a certified point for pair 7',
     ('b699', 'e', 16, "Lettered the navigator's (e)")),
    (32, "THE SEAT'S OWN WORDING", 'THE SEAT’S', None, 'the root’s prompt naming pair 7 without its footing',
     ('b698', 'a', 13, "Lettered b698's defect (a)")),
    (None, '', 'THE NAVIGATOR’S', 'i', 'the closing bank edited by the Edit tool to carry the author’s word after the seal, ordered by that word',
     ('b698', 'd', 12, "Lettered b698's defect (d)")),
)
# ### the records: (events line, the head's needle, the words, the column)
RECORDS = (
    (11, "THE HARNESS'S AUTO-MODE NOTE", 'the harness note not followed', ('b712', ':41', 33, 'Records, unlettered: :18, :41')),
    (13, "THE PRE-RUN'S standing-c", 'the read offences counted 9 beside the face’s seven', ('b701', 'h', 18, "lettered (h), THE SEAT'S")),
    (17, 'THE STANDING REPORT TOOL', 'the unsealed report tool rewritten after the lock', None),
    (35, "THE AUTHOR'S WORD ON (b) AND (e)", 'the author’s word after the report bank', ('b712', ':18', 33, 'Records, unlettered: :18, :41')),
    (72, 'THE SUITE, PRE-PUSH', 'the suite’s two readings, 129 of 140', ('b704', 'r', 25, "lettered b704's (r) and (s), THE SEAT'S")),
)
ADDED_WORDS = 'the closing bank edited by the Edit tool to carry the author’s word after the seal'
ADDED_EDITS = (18835, 18836, 18850)
ADDED_NEEDLE = 'b713_closing.txt","old_string'
ROW = ('  (34) b713\'s record after its seal (relay data/b713_events.txt, sixteen starting lines, and the item (R324)(5) adds): lettered\n'
       '      (o) four arms failing on real state at the pre-run, the arms`, and (p) G-TOOL-REPAIRS` TypeError on b712`s banks, the arm`s, no\n'
       '      repair named; (q) the next act, (r) the chain row count and (s) the root-check range carried unbumped into the sealed suite, the\n'
       '      suite`s, by (R324)(6)(ii) (v5 row (75)); (t) --combine not run before the seal, the order`s, and (v) the root`s dry run READY False\n'
       '      undeclared on the face`s list, the face`s, both by (iii) (76); (u) the corrigendum lettered a\' where the suite reads a\u2032, the\n'
       '      lettering`s, by (v) (78); (w) and (x) the author`s word at the root`s prompt assuming a committed n* for the pairs beyond reach and\n'
       '      a certified point for pair 7, the navigator`s; (y) the root`s prompt naming pair 7 without its footing, the seat`s; (z) the closing\n'
       '      bank edited by the Edit tool to carry the author`s word after the seal, the navigator`s, by (i) (74). Records, unlettered: :11,\n'
       '      :13, :17, :35, :72. NEW OR REPEAT: REPEAT %s ; THE REPEAT FRACTION %s.\n'
       '      THE CORRECTION: relay data/standing_clauses_v5.txt rows (73)-(78), the repairs` diffs and controls data/b714_tool_repairs.txt.\n'
       '      The generated corrigendum entry stands at FINDINGS.md :%s.')


def _flat(t):
    return re.sub(r'\s+', ' ', t)


def _corrigenda_rows():
    """the corrigenda bank's rows by number, each row's lines joined and its whitespace collapsed."""
    rows, cur = {}, None
    for l in C78.rd(os.path.join(D, 'b675_corrigenda.txt')).replace(chr(13), '').split(NL):
        m = re.match(r'^  \((\d+)\) ', l)
        if m:
            cur = int(m.group(1))
            rows[cur] = l
        elif cur is not None and l.startswith('      '):
            rows[cur] += ' ' + l.strip()
        elif not l.strip() or l.startswith('###'):
            cur = None
    return dict((k, _flat(v)) for k, v in rows.items())


def _transcript_lines(nums):
    p = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
    want, got = set(nums), {}
    with open(p, encoding='utf-8', errors='replace') as fh:
        for i, l in enumerate(fh, 1):
            if i in want:
                got[i] = ADDED_NEEDLE in l and '"name":"Edit"' in l
            if i > max(want):
                break
    return got


def compose():
    ev = C78.rd(os.path.join(D, 'b713_events.txt')).replace(chr(13), '').split(NL)
    starts = [i for i, l in enumerate(ev, 1) if re.match(r'^\(\d+\) ', l)]
    want_starts = sorted([x[0] for x in LETTERED if x[0]] + [x[0] for x in RECORDS])
    heads = dict((n, re.sub(r'^\(\d+\) ', '', ev[n - 1])) for n in starts)
    miss_heads = [x[0] for x in LETTERED if x[0] and not heads.get(x[0], '').startswith(x[1])] + \
                 [x[0] for x in RECORDS if not heads.get(x[0], '').startswith(x[1])]
    dt = C78.rd(os.path.join(D, 'b713_defects.txt'))
    prev = [re.match(r"\(([a-z]'?)\)", x).group(1) for x in REC.letters_of(dt)]
    letters = AL.after(prev, len(LETTERED)) if prev == PREV_LETTERS else []
    v5 = C78.rd(os.path.join(D, 'standing_clauses_v5.txt')).split(NL)
    rows = {}
    for i, l in enumerate(v5, 1):
        m = re.match(r"^  \((7[4-8])\) STANDING STOP SOURCE \(R324\)\(6\)\(([iv]+)\) ;", l)
        if m:
            rows[m.group(2)] = (int(m.group(1)), i)
    bad_rows = [x[3] for x in LETTERED if x[3] and rows.get(x[3], (0,))[0] != V5_ROWS[x[3]]]
    cr = _corrigenda_rows()
    cols = [x[5] for x in LETTERED] + [x[3] for x in RECORDS]
    bad_cols = [(c[0], c[1], c[2]) for c in cols if c and _flat(c[3]) not in cr.get(c[2], '')]
    f14 = C78.rd(os.path.join(D, 'b714_ferry.txt')).split(NL)
    added_words = f14[14].count(ADDED_WORDS) if len(f14) > 14 else 0
    edits = _transcript_lines(ADDED_EDITS)
    s = dict(starts=starts, heads=heads, prev=prev, letters=letters, rows=rows, added_words=added_words, edits=edits,
             corrigenda_last=max(cr) if cr else 0)
    bad = [k for k, v in (('the sixteen starting lines', starts == want_starts), ('each item`s head', not miss_heads),
                          ('b713`s fourteen letters', prev == PREV_LETTERS), ('the twelve letters after them', letters == list('opqrstuvwxyz')),
                          ('the v5 rows of the five repairs', not bad_rows), ('each REPEAT`s row and needle', not bad_cols),
                          ('the ferry :15 carrying the added item once', added_words == 1),
                          ('the three Edit calls on b713`s closing', all(edits.get(n) for n in ADDED_EDITS)),
                          ('the corrigenda bank`s last row (33)', max(cr) == 33 if cr else False)) if not v]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (heads missed %s ; rows %s ; columns %s ; starts %s ; edits %s)' % (
            bad, miss_heads, bad_rows, bad_cols, starts, edits))
    return s


def _column(c):
    if not c:
        return 'NEW (no row of relay data/b675_corrigenda.txt carries its class)'
    act, letter, row, _n = c
    what = ('%s’s record %s' % (act, letter)) if letter.startswith(':') else ('%s (%s)' % (act, AL.canon(letter)))
    return 'REPEAT of %s, relay data/b675_corrigenda.txt row (%d)' % (what, row)


def fraction(s=None):
    """the repeat fraction: (REPEAT among the lettered, lettered; REPEAT among all items, all items)."""
    rl = sum(1 for x in LETTERED if x[5])
    ra = rl + sum(1 for x in RECORDS if x[3])
    return rl, len(LETTERED), ra, len(LETTERED) + len(RECORDS)


def fraction_words():
    rl, nl, ra, na = fraction()
    return '%d of %d (%.2f) ; among the lettered %d of %d (%.2f)' % (ra, na, ra / float(na), rl, nl, rl / float(nl))


def entry_text(s):
    return NL + NL.join(_entry_lines(s)) + NL


def _repair_words(s, r):
    if not r:
        return '(R324)(5) names no repair for it.'
    return ('TAKEN UP BY (R324)(6)(%s), relay data/standing_clauses_v5.txt row (%d) (:%d); its diff and its two-instance control in relay '
            'data/b714_tool_repairs.txt.' % (r, s['rows'][r][0], s['rows'][r][1]))


WHY = {
    3: ('The pre-run’s standing-a read four arms failing on real state beyond the face’s three declared: G-PRIOR-CLOSED-PUSHED raised '
        'AttributeError on a b709 constant its carried predicate kept, G-BRANCHES-DELETED read b712’s figure of two repositories, '
        'G-PROCS-LISTED read needles the step-zero bank’s words do not carry, and G-PP-SCOPE waited on the trail’s landing.'),
    21: ('On b712’s banks (`--prev --part act`) G-TOOL-REPAIRS raised TypeError sorting rows of another form, and the suite recorded the raise '
         'as FAIL.'),
    54: 'G-NEXT-ACT-NAMED read “**Next:** b713”, b712’s figure, where b713’s closing names b714.',
    56: 'G-ACTROOT-BANKED expected the chain’s 89th row where b713’s act root is the 90th.',
    58: 'G-ACTROOT-VERIFY iterated range(624, 713), ending at b712, so b713’s own root stood outside its reach.',
    61: ('`--combine` was not run before the seal, so data/b713_arms_prerun.txt and its seconds bank were never written; G-ARMS-PRERUN, '
         'G-PARTS-PRERUN and G-ARM-SECONDS-BANKED failed on the absence.'),
    64: ('data/b713_corrigendum.json lettered “a\'”-“d\'” (U+0027) where G-CORRIGENDUM-ENTERED wanted “a′”-“d′” (U+2032); every other clause '
         'of the arm held.'),
    68: ('data/b713_root_banks_dry.json read ready False before the lock; the face’s (0) printed it, but the declared-failure list named only '
         'G-READ-RULE-STANDING and G-PRIORBANK-UNCHANGED.'),
    25: ('The word read “each with its committed prediction n*” for the 29 pairs beyond reach; data/b713_predictions.txt at be4db146 :18-:46 '
         'marks each BEYOND REACH and forms no prediction.'),
    29: ('The word read pair 7’s point as certified; its row in data/b713_list.json reads certified False, a Newton candidate at 200 bits, and '
         'what is certified is its band’s count (data/b713_list.txt :22).'),
    32: ('The root’s prompt (transcript line 17284) and the report’s CERTIFIED line as first banked said “one with Re rho > 1” without the '
         'point’s status; the prompt is put once and was not put again.'),
    None: ('After the seal the author’s word on (b) and (e) was carried into relay data/b713_closing.txt, a tool-written bank, by three Edit '
           'calls (the session’s transcript lines %s) before its one commit 2f76d11c, as that word ordered.' % ', '.join(str(n) for n in ADDED_EDITS)),
}


def _entry_lines(s):
    L = [TITLE, '',
         ('b713’s events bank (relay data/b713_events.txt) carries sixteen starting lines (:%s), entered after its seal and not lettered, '
          'for this act’s corrigendum under standing clauses v2 row (52). (R324)(5) letters eleven of them as defects, each with its owner, '
          'and adds one; b713’s defects bank carries (a)-(n), so these are (o)-(z), lettered by relay tools/act_letters.py. Five are entered '
          'as records. Each item carries NEW or REPEAT, a REPEAT naming the earlier act and letter of its class and the row of relay '
          'data/b675_corrigenda.txt that records it; the evidence set is that bank’s rows (1)-(%d). b713’s events bank, its defects bank, its '
          'face, its trail record (PLACE-papers OPEN_TRAILS :%d) and every root-named bank are not edited.' % (
              ', :'.join(str(n) for n in s['starts']), s['corrigenda_last'], K.B711_TRAIL)), '']
    for (n, _h, own, r, words, col), x in zip(LETTERED, s['letters']):
        place = 'relay data/b713_events.txt :%d' % n if n else 'the item (R324)(5) adds'
        L += ['**(%s) %s** (%s; %s; %s). %s %s' % (x, words[0].upper() + words[1:], place, own, _column(col), WHY[n], _repair_words(s, r)), '']
    L += ['**Records, unlettered:** ' + '; '.join(':%d %s (%s)' % (n, w, _column(c)) for n, _h, w, c in RECORDS) +
          ' (relay data/b713_events.txt).', '',
          '**The repeat fraction:** REPEAT %s.' % fraction_words(), '',
          'The sealed face, the events and defects banks, the trail record and every root-named bank are not edited -- this entry is their '
          'correction. Nothing here proves RH or GRH.', '',
          ('*Filed at b714 on the author’s ruling `(R324)`(5): generated by relay `tools/b714_corrigendum.py`, written whole at b714 in the '
           'corrigendum form of relay `tools/b678_corrigendum.py` (its reader imported unchanged), its letters from relay `tools/act_letters.py`, '
           'banked as relay `data/b714_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at row (34); it answers b713’s '
           'events after its seal.*')]
    return L


def bank_lines(s, landed_line=None):
    L = ['b714 -- THE CORRIGENDUM ENTRY FOR b713`S EVENTS AFTER ITS SEAL, (R324)(5) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the figures read before the write: the starting lines :%s ; b713`s letters %s ; the letters after them %s ;' % (
             ', :'.join(str(n) for n in s['starts']), ''.join(s['prev']), ''.join(s['letters'])),
         '### the v5 rows %s ;' % ' '.join('(%s) row (%d) :%d' % (r, s['rows'][r][0], s['rows'][r][1]) for r in ('i', 'ii', 'iii', 'iv', 'v')),
         '### the ferry :15 carrying the added item %d time(s) ; the transcript`s Edit calls on b713`s closing %s ; the corrigenda bank`s last row (%d).' % (
             s['added_words'], sorted(s['edits'].items()), s['corrigenda_last']), '']
    L += ['  ' + l for l in _entry_lines(s)]
    L += ['', '### ### **ITEMS %d: LETTERED %d (o)-(z), EACH WITH ITS OWNER AND ITS REPAIR OR NONE ; RECORDS %d ; REPEAT %s ; '
              'THE FACE, THE EVENTS AND DEFECTS BANKS, THE TRAIL AND THE ROOT-NAMED BANKS UNEDITED ; THE ENTRY AT FINDINGS :%s.**' % (
                  len(LETTERED) + len(RECORDS), len(LETTERED), len(RECORDS), fraction_words(), landed_line if landed_line else 'NOT YET WRITTEN')]
    return L


def _membrane(p):
    """standing clauses v2 row (53): the membrane before a write under relay data/ (tools/act_membrane.py guard_path)."""
    import act_membrane as MEM
    MEM.guard_path('b714', p, REC.R.ROOT_EXCLUDE)


def _put(name, data):
    p = os.path.join(D, name)
    _membrane(p)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data.encode('utf-8'))
    os.replace(p + '.tmp', p)


def _row_text(ln):
    rl, nl, ra, na = fraction()
    return ROW % ('%d of %d' % (ra, na), '%.2f, among the lettered %d of %d' % (ra / float(na), rl, nl), ln)


def main(route):
    s = compose()
    text = entry_text(s)
    if route == 'dry':
        REC.R.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text))
        print(NL.join(bank_lines(s)))
        print(_row_text('NOT YET WRITTEN'))
        return
    REC.land([('FINDINGS.md', TITLE, text)], 'b714_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b714_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    _put('b714_corrigendum.txt', NL.join(L) + NL)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE,
             lettered=[dict(letter=x, line=n, owner=o, repair=r, v5_row=V5_ROWS.get(r) if r else None,
                            column=('REPEAT' if c else 'NEW'), repeat_of=(list(c[:3]) if c else None))
                       for (n, _h, o, r, _w, c), x in zip(LETTERED, s['letters'])],
             records=[dict(line=n, column=('REPEAT' if c else 'NEW'), repeat_of=(list(c[:3]) if c else None)) for n, _h, _w, c in RECORDS],
             starts=s['starts'], row=34, fraction=list(fraction()))
    _put('b714_corrigendum.json', json.dumps(j, indent=1, ensure_ascii=False) + NL)
    print(L[-1])
    print(_row_text(ln))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'dry')
