# -*- coding: utf-8 -*-
"""b715_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R325)(2): b714's events after its seal (relay data/b714_events.txt, twelve starting
lines) and the two items the navigator adds, answered by one generated FINDINGS entry in b678's corrigendum form, in the banks' words, every
item carrying a column NEW or REPEAT. Nine are lettered as defects, each with its owner, (r)-(z) after b714's seventeen letters (a)-(q) (relay
data/b714_defects.txt), the letters from tools/act_letters.py (the one lettering the suite imports too); five are entered as records,
unlettered. Each lettered item names the repair of (R325)(3) or (4) that takes it up, by its line in relay data/b715_ferry.txt, or reads
"carried" with its reason; the repairs' diffs and two-instance controls are banked at Components 2 and 3 in data/b715_tool_repairs.txt.
b714's events bank, its defects bank, its sealed face, its trail record (PLACE-papers OPEN_TRAILS :15962) and every root-named bank unedited.

### THE NEW OR REPEAT COLUMN: an item is REPEAT where the corrigenda bank (relay data/b675_corrigenda.txt, rows (1)-(34), the record of every
### earlier act's lettered corrections since b675) carries an item of its class, and the column names that act, its letter and the row; the
### row's text is read and its needle checked before any write. NEW where no row carries one. The evidence set is that bank alone.
### The added items' sources: the ferry :9 (relay data/b715_ferry.txt), the author's word (5) (relay data/b714_author_words_preseal.txt :83),
### b714's records (15)-(17) (relay data/b714_records.txt :91, :97, :107) and its event (5) (relay data/b714_events.txt :22), read at compose time.
### Written whole by the Write tool at b715 in b714's form (tools/b714_corrigendum.py); b678's reader `rd` IMPORTED unchanged. Routes: `dry` ->
### the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b715_record's guarded landing,
### data/b715_corrigendum.txt (.json). The corrigenda bank's row (35) is appended by the seat through the Edit tool from the line this tool
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
import b715_worklist as K         # noqa: E402
import b715_record as REC         # noqa: E402  ### the guarded landing, the letters reader
import act_letters as AL          # noqa: E402  ### the one lettering

TITLE = ('## Corrigendum to b714’s record after its seal (relay data/b714_events.txt): twelve events and two added items, nine lettered '
         '(r)-(z) with their owners, five entered as records, each NEW or REPEAT, under (R325)(2)')
PREV_LETTERS = list('abcdefghijklmnopq')
# ### the repairs of (R325) by their lines in relay data/b715_ferry.txt
FERRY_LINES = {'3': 11, '3(iii)': 14, '4(ii)': 20, '4(iii)': 21, '4(iv)': 22}
FERRY_NEEDLES = {'3': '(3) ONE STANDING CLOSE TOOLSET', '3(iii)': '(iii) Each act seals the toolset by hash',
                 '4(ii)': '(ii) THE WITHHELD PATH, CONDITION-BOUND', '4(iii)': '(iii) THE HOOK LOGS TO AN EXCLUDED BANK',
                 '4(iv)': '(iv) THE COMPONENTS COMPOSER READS THE RULING'}
# ### the lettered items, in the events bank's order and then the two added: (events line or None for an added item, the head's needle, the
# ### owner, the repair's (R325) clause or None for carried, the item's words, the column: None for NEW or (act, letter, corrigenda row, the
# ### row's needle), the reason where carried)
LETTERED = (
    (6, "THE ENTRY'S HEAD CLAUSE MISREADS THE WORD", 'THE RECORD TOOL’S', None, 'the entry’s head clause composed against the author’s word',
     ('b711', 'l', 32, '(l) the entry`s question count read at its landing, the sealed record tool`s form, carried'),
     'the entry’s text is composed by the act’s own finding route, and (R325) orders no repair to it; the clause read from the author’s '
     'word bank is carried to b716, whose entry the standing toolset composes'),
    (10, 'THE PRE-PUSH SUITE', 'THE SUITE’S AND THE SEAT’S', None, 'five arms failing on real state beyond the face at the pre-push suite',
     ('b705', 'o', 26, 'G-ENTRY-TITLE-FORM (its needle in lower case against the entry'),
     'the five are two omissions of the seat’s and three predicates of the copied suite, and (R325) names no repair for them; the '
     'replay of (R325)(3)(iv) reads the same predicates over b714’s banks, and each that differs there is entered as a finding of the old tool'),
    (22, 'STEP [18] RAISED, NOTHING WRITTEN; HALTED', 'THE RECORD TOOL’S', '4(iv)', 'the components route raising on a predecessor’s worklist key',
     ('b713', 'q', 34, '(q) the next act, (r) the chain row count and (s) the root-check range carried unbumped into the sealed suite'), None),
    (28, "THE SEAT'S: A ROOT ITEM EDITED AFTER THE ROOT", 'THE SEAT’S', None, 'a root-named bank edited after the root by the Edit tool and restored',
     ('b698', 'd', 12, 'the Edit tool restored it'),
     'the Edit tool’s write passes through no tool’s membrane, and (R325) names no repair for it; the bank is equal to its blob at the '
     'root’s commit, and the class stands for the author’s ruling'),
    (52, 'THE UNSEALED TOOLS AT THE CLOSE', 'THE CLOSING TOOL’S', '3(iii)', 'the sealed closing naming one unsealed tool by fixed text',
     ('b711', 't', 32, 'for an unchanged blob, the closing tool`s'), None),
    (66, 'THE POST-PUSH SUITE', 'THE HOOK’S', '4(iii)', 'a refused command appended to a root-named bank after the root',
     ('b710', 'j', 31, '(j) a root-named bank written after the root, repaired by the membrane'), None),
    (75, "THE PRE-RUN, STATED AS THE AUTHOR'S WORD (7) ORDERS IT", 'THE CLOSING TOOL’S', '4(ii)', 'the sealed closing carrying no line for the withheld arm',
     None, None),
    (None, 'no tool is edited for this', 'THE NAVIGATOR’S', '4(ii)', 'word (5)’s clause “no tool is edited for this”, which assumed a path the seal lacked',
     ('b699', 'e', 16, "Lettered the navigator's (e)"), None),
    (None, 'a close computed in copied tools', 'THE COPIED TOOLS’', '3', 'the act’s four halts at the seal and at step [18], one class: a close computed in copied tools',
     ('b713', 'q', 34, '(q) the next act, (r) the chain row count and (s) the root-check range carried unbumped into the sealed suite'), None),
)
# ### the records: (events line, the head's needle, the words, the column)
RECORDS = (
    (3, "THE ROOT'S PROMPT DISPLAYED CUT", 'the root’s prompt displayed cut at its second sentence', None),
    (9, "THE REPORT TOOL'S TWO LINES RESTATED BEFORE ITS BANK", 'the unsealed report tool’s two lines restated before its bank',
     ('b711', 'm', 32, '(m) the report tool`s two misreads')),
    (33, "THE AUTHOR'S WORD AT STEP [18]", 'the author’s word at step [18], route 1 by a stand-in tool', ('b712', ':18', 33, 'Records, unlettered: :18, :41')),
    (63, "THE HARNESS'S AUTO-MODE NOTE AGAIN", 'the harness note not followed', ('b712', ':41', 33, 'Records, unlettered: :18, :41')),
    (80, "THE CLOSE'S STEPS [20]-[24]", 'the close’s steps [20]-[24], the closing’s dry run refused after the lock', None),
)
HALTS = ((91, '(15) THE SEAL REFUSED, NOTHING RECORDED'), (97, "(16) THE AUTHOR'S WORD AT THE SEAL, AND THE SEAL'S TOOL WITH NO ROUTE FOR IT"),
         (107, '(17) THE WORD (6) CARRIED IN THE CHECKS TOOL; THE SEAL HELD ON ITS LAST SENTENCE'))
WORD5_LINE = 83
ROW = ('  (35) b714\'s record after its seal (relay data/b714_events.txt, twelve starting lines, and the two items (R325)(2) adds): lettered\n'
       '      (r) the entry`s head clause composed against the author`s word, the record tool`s, carried; (s) five arms failing on real state\n'
       '      beyond the face at the pre-push suite, the suite`s and the seat`s, carried; (t) the components route raising on a predecessor`s\n'
       '      worklist key, the record tool`s, by (R325)(4)(iv); (u) a root-named bank edited after the root by the Edit tool and restored, the\n'
       '      seat`s, carried; (v) the sealed closing naming one unsealed tool by fixed text, the closing tool`s, by (3)(iii); (w) a refused\n'
       '      command appended to a root-named bank after the root, the hook`s, by (4)(iii); (x) the sealed closing carrying no line for the\n'
       '      withheld arm, the closing tool`s, and (y) word (5)`s clause "no tool is edited for this", the navigator`s, both by (4)(ii); (z) the\n'
       '      act`s four halts at the seal and at step [18], one class, a close computed in copied tools, the copied tools`, by (3). Records,\n'
       '      unlettered: :3, :9, :33, :63, :80. NEW OR REPEAT: REPEAT %s ; THE REPEAT FRACTION %s.\n'
       '      THE CORRECTION: the standing close toolset of (R325)(3) and the class repairs of (R325)(4), their diffs and controls\n'
       '      data/b715_tool_repairs.txt. The generated corrigendum entry stands at FINDINGS.md :%s.')


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


def compose():
    ev = C78.rd(os.path.join(D, 'b714_events.txt')).replace(chr(13), '').split(NL)
    starts = [i for i, l in enumerate(ev, 1) if re.match(r'^\(\d+\) ', l)]
    want_starts = sorted([x[0] for x in LETTERED if x[0]] + [x[0] for x in RECORDS])
    heads = dict((n, re.sub(r'^\(\d+\) ', '', ev[n - 1])) for n in starts)
    miss_heads = [x[0] for x in LETTERED if x[0] and not heads.get(x[0], '').startswith(x[1])] + \
                 [x[0] for x in RECORDS if not heads.get(x[0], '').startswith(x[1])]
    dt = C78.rd(os.path.join(D, 'b714_defects.txt'))
    prev = [re.match(r"\(([a-z]'?)\)", x).group(1) for x in REC.letters_of(dt)]
    letters = AL.after(prev, len(LETTERED)) if prev == PREV_LETTERS else []
    cr = _corrigenda_rows()
    cols = [x[5] for x in LETTERED] + [x[3] for x in RECORDS]
    bad_cols = [(c[0], c[1], c[2]) for c in cols if c and _flat(c[3]) not in cr.get(c[2], '')]
    f15 = C78.rd(os.path.join(D, 'b715_ferry.txt')).split(NL)
    l9 = f15[8] if len(f15) > 8 else ''
    added = [l9.count(x[1]) for x in LETTERED if x[0] is None]
    w5 = C78.rd(os.path.join(D, 'b714_author_words_preseal.txt')).split(NL)
    w5_ok = len(w5) >= WORD5_LINE and 'no tool is edited for this' in w5[WORD5_LINE - 1]
    rc = C78.rd(os.path.join(D, 'b714_records.txt')).split(NL)
    halts_ok = [n for n, h in HALTS if not (len(rc) >= n and rc[n - 1].startswith(h))]
    ferry_ok = [k for k, n in FERRY_LINES.items() if not (len(f15) >= n and f15[n - 1].startswith(FERRY_NEEDLES[k]))]
    s = dict(starts=starts, heads=heads, prev=prev, letters=letters, added=added, w5=w5_ok,
             corrigenda_last=max(cr) if cr else 0)
    bad = [k for k, v in (('the twelve starting lines', starts == want_starts), ('each item`s head', not miss_heads),
                          ('b714`s seventeen letters', prev == PREV_LETTERS), ('the nine letters after them', letters == list('rstuvwxyz')),
                          ('each REPEAT`s row and needle', not bad_cols), ('the ferry :9 carrying each added item once', added == [1, 1]),
                          ('word (5)`s clause at its line', w5_ok), ('the three halts` records at their lines', not halts_ok),
                          ('each repair`s ferry line', not ferry_ok),
                          ('the corrigenda bank`s last row (34)', max(cr) == 34 if cr else False)) if not v]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (heads missed %s ; columns %s ; starts %s ; added %s ; halts %s ; ferry %s)' % (
            bad, miss_heads, bad_cols, starts, added, halts_ok, ferry_ok))
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


def _repair_words(r, why):
    if not r:
        return 'CARRIED: %s.' % why
    return ('TAKEN UP BY (R325)(%s) (relay data/b715_ferry.txt :%d); its diff and its two-instance control in relay '
            'data/b715_tool_repairs.txt.' % (r.replace('(', ')(', 1), FERRY_LINES[r]))


WHY = {
    6: ('The sealed record tool’s _finding_text (tools/b714_record.py :2307-:2308) composed “held in its bank and carried, the author’s word '
        'at the root not given for it” whenever no heads commit stood; the word was given, and was to hold (data/b714_author_words.txt); the '
        'clause landed as composed at FINDINGS :10512.'),
    10: ('Beyond the three the face declared and the pre-run’s, five failed, each read from its predicate: G-ANSWERS-CHECKED and '
         'G-ANSWERS-BEFORE-WRITES on no mid-act answer check before the root, the seat’s; G-ENTRY-TITLE-FORM on a needle written before the '
         'corrigendum’s figure; G-DEFECTS-LETTERED on owners outside its rows; G-ARM-SECONDS-BANKED on the seconds bank not gathered, the '
         'seat’s (data/b714_events.txt :10-:21).'),
    22: ('`tools/b714_record.py components` passed its order gate and raised AttributeError on the worklist key C1_PP_FACES (:2643): the route '
         '(:2630-:2656, sealed) was b713’s composer carried unrewritten; data/b714_components.txt was written by a stand-in tool on the author’s '
         'word (7).'),
    28: ('Records (20) and (21) were appended by the Edit tool to data/b714_records.txt, a bank the root names, after the root, then taken out '
         'exactly as added before any commit; the bank equals its blob at the root’s commit 61225f71 and its text stands at events (4)-(5).'),
    52: ('The sealed closing’s line for the unsealed tools is fixed text naming the report tool alone (tools/b714_closing.py :513); the '
         'stand-in tool of word (7) and its bank were listed with their sha256 in the events bank instead.'),
    66: ('G-ACTROOT-LAST failed post-push on two root-named banks written after the root: data/b714_records.txt by (u), and '
         'data/b714_hook_refusals.txt, to which the hook appended a refused command after the root; the hook writes its refusals to a bank '
         'the root names.'),
    75: ('The combined pre-run read 100 passing, of which G-RULE-LONG-PHASE-SPLIT was since WITHHELD, NOT EXERCISABLE; the sealed closing '
         'carries no line for a withheld arm (no `withheld` in tools/b714_closing.py), so the fact stood in the events bank alone.'),
    'no tool is edited for this': ('Word (5) took route 2, the arm withheld at the seal, and closed “no tool is edited for this” '
                                   '(relay data/b714_author_words_preseal.txt :83); the seal’s tool had no withheld path, so the route '
                                   'could not be carried out unedited, and word (6) edited the checks tool for it.'),
    'a close computed in copied tools': ('The seal refused and the act halted at step [8] (relay data/b714_records.txt (15) :91), halted '
                                         'there again for want of a route (16) :97 and held on its last sentence (17) :107; step [18] raised and '
                                         'halted (data/b714_events.txt (5) :22). Each halt stood in a per-act tool copied from its predecessor '
                                         'and carrying that act’s path or objects.'),
}


def _entry_lines(s):
    L = [TITLE, '',
         ('b714’s events bank (relay data/b714_events.txt) carries twelve starting lines (:%s), entered after its seal and not lettered, '
          'for this act’s corrigendum under standing clauses v2 row (52); (R325)(2) adds two items, the navigator’s. Seven events and the two '
          'added items are lettered as defects, each with its owner; b714’s defects bank carries (a)-(q), so these are (r)-(z), lettered by '
          'relay tools/act_letters.py. Five are entered as records. Each item carries NEW or REPEAT, a REPEAT naming the earlier act and letter '
          'of its class and the row of relay data/b675_corrigenda.txt that records it; the evidence set is that bank’s rows (1)-(%d). Each '
          'lettered item names the repair of (R325)(3) or (4) that takes it up, or reads CARRIED with its reason. b714’s events bank, its '
          'defects bank, its face, its trail record (PLACE-papers OPEN_TRAILS :%d) and every root-named bank are not edited.' % (
              ', :'.join(str(n) for n in s['starts']), s['corrigenda_last'], K.B711_TRAIL)), '']
    for (n, h, own, r, words, col, why), x in zip(LETTERED, s['letters']):
        place = 'relay data/b714_events.txt :%d' % n if n else 'the item (R325)(2) adds'
        L += ['**(%s) %s** (%s; %s; %s). %s %s' % (x, words[0].upper() + words[1:], place, own, _column(col), WHY[n if n else h],
                                                   _repair_words(r, why)), '']
    L += ['**Records, unlettered:** ' + '; '.join(':%d %s (%s)' % (n, w, _column(c)) for n, _h, w, c in RECORDS) +
          ' (relay data/b714_events.txt).', '',
          '**The repeat fraction:** REPEAT %s.' % fraction_words(), '',
          'The sealed face, the events and defects banks, the trail record and every root-named bank are not edited -- this entry is their '
          'correction. Nothing here proves RH or GRH.', '',
          ('*Filed at b715 on the author’s ruling `(R325)`(2): generated by relay `tools/b715_corrigendum.py`, written whole at b715 in the '
           'corrigendum form of relay `tools/b678_corrigendum.py` (its reader imported unchanged), its letters from relay `tools/act_letters.py`, '
           'banked as relay `data/b715_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at row (35); it answers b714’s '
           'events after its seal.*')]
    return L


def bank_lines(s, landed_line=None):
    L = ['b715 -- THE CORRIGENDUM ENTRY FOR b714`S EVENTS AFTER ITS SEAL, (R325)(2) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the figures read before the write: the starting lines :%s ; b714`s letters %s ; the letters after them %s ;' % (
             ', :'.join(str(n) for n in s['starts']), ''.join(s['prev']), ''.join(s['letters'])),
         '### the ferry :9 carrying each added item %s time(s) ; word (5)`s clause at :%d %s ; the halts` records %s and event (5) :22 ; the '
         'corrigenda bank`s last row (%d).' % (s['added'], WORD5_LINE, s['w5'], [n for n, _h in HALTS], s['corrigenda_last']), '']
    L += ['  ' + l for l in _entry_lines(s)]
    L += ['', '### ### **ITEMS %d: LETTERED %d (r)-(z), EACH WITH ITS OWNER AND ITS REPAIR OR CARRIED ; RECORDS %d ; REPEAT %s ; '
              'THE FACE, THE EVENTS AND DEFECTS BANKS, THE TRAIL AND THE ROOT-NAMED BANKS UNEDITED ; THE ENTRY AT FINDINGS :%s.**' % (
                  len(LETTERED) + len(RECORDS), len(LETTERED), len(RECORDS), fraction_words(), landed_line if landed_line else 'NOT YET WRITTEN')]
    return L


def _membrane(p):
    """standing clauses v2 row (53): the membrane before a write under relay data/ (tools/act_membrane.py guard_path)."""
    import act_membrane as MEM
    MEM.guard_path('b715', p, REC.R.ROOT_EXCLUDE)


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
    REC.land([('FINDINGS.md', TITLE, text)], 'b715_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b715_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    _put('b715_corrigendum.txt', NL.join(L) + NL)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE,
             lettered=[dict(letter=x, line=n, owner=o, repair=r, ferry_line=FERRY_LINES.get(r) if r else None,
                            column=('REPEAT' if c else 'NEW'), repeat_of=(list(c[:3]) if c else None), carried=(why if not r else None))
                       for (n, _h, o, r, _w, c, why), x in zip(LETTERED, s['letters'])],
             records=[dict(line=n, column=('REPEAT' if c else 'NEW'), repeat_of=(list(c[:3]) if c else None)) for n, _h, _w, c in RECORDS],
             starts=s['starts'], row=35, fraction=list(fraction()))
    _put('b715_corrigendum.json', json.dumps(j, indent=1, ensure_ascii=False) + NL)
    print(L[-1])
    print(_row_text(ln))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'dry')
