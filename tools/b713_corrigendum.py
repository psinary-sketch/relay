# -*- coding: utf-8 -*-
"""b713_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R323)(3): b712's events after its seal (relay data/b712_events.txt, nine starting
lines) and the one item the navigator adds, answered by one generated FINDINGS entry in b678's corrigendum form, in the banks' words. Eight are
lettered as defects, each with its owner, (w)-(z) and (a')-(d') after b712's twenty-two letters (a)-(v) (relay data/b712_defects.txt; the
letter after (z) primed, the form the defects reader reads, `\\(([a-z]'?)\\)`); two are entered as records, unlettered. Each lettered item
names the repair of (R323)(4) that takes it up, by its row in relay data/standing_clauses_v4.txt (committed alone at step zero, 89bea621); the
repairs' diffs and two-instance controls are banked after this entry in data/b713_tool_repairs.txt, Component 1's order. b712's events bank,
its defects bank, its sealed face (relay data/b712_registration_2026-10-25.txt), its trail record (PLACE-papers OPEN_TRAILS :15890) and every
root-named bank unedited.

### Written whole by the Write tool at b713, its items rewritten for b712's events (b708-b712 wrote theirs the same way). b678's reader `rd`
### IMPORTED unchanged; its form -- one generated entry, each item quoted with its place, the corrected reading and its source, the figures read
### from their banks and checked before any write, `dry` then `land`. Every figure is read, none typed:
###   the starting lines: data/b712_events.txt, a line opening four spaces and a capital; each item's head checked by its needle;
###   b712's letters: data/b712_defects.txt by tools/b713_record.py letters_of (twenty-two, (a)-(v));
###   the repairs: data/standing_clauses_v4.txt, each row's head naming its (R323)(4) item;
###   the added item: data/b712_ferry.txt :11 carrying "the act’s step bank row marked gate" once, and data/b712_steps.json carrying the
###   gate's two commits afe3903a (phase gate) and dcb3b286 (phase component 5).
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b713_record's
### guarded landing, data/b713_corrigendum.txt (.json). The corrigenda bank's row (33) is appended by the seat through the Edit tool from the
### bank line this tool prints (ROW). It writes those two banks and the one FINDINGS entry.
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
import b713_worklist as K         # noqa: E402
import b713_record as REC         # noqa: E402  ### the guarded landing, the letters reader

TITLE = ('## Corrigendum to b712’s record after its seal (relay data/b712_events.txt): nine events and one added item, eight lettered '
         '(w)-(z) and (a′)-(d′) with their owners, two entered as records, under (R323)(3)')
PREV_LETTERS = list('abcdefghijklmnopqrstuv')
# ### the repairs of (R323)(4) by their rows of standing clauses v4
V4_ROWS = {'i': 62, 'ii': 63, 'iii': 64, 'iv': 65, 'v': 66, 'vi': 67}
# ### the lettered items, (R323)(3)'s order: (letter, events line or None for the added item, the head's needle, the owner, the repair's
# ### (R323)(4) item, the item's words as the ruling names it)
LETTERED = (
    ("w", 3, 'THE GATE IN TWO COMMITS.', 'THE ARM’S', 'ii', 'the gate’s work in two commits read as one'),
    ("x", 10, 'N5 REFUTED BY THE SCORER\'S LIST.', 'THE SCORER’S', 'i', 'N5 refuted by the scorer’s own file list where the (W) bank names the write'),
    ("y", 28, 'THE ROOT ROUTE\'S DRY RUN RUN AGAIN.', 'THE SEAT’S', 'iv', 'rootdry run twice, its pre-lock bank overwritten'),
    ("z", 32, 'TWO SEALED TOOLS ON (h)\'S OWNER.', 'THE TOOLS’', 'iii', 'the two sealed tools counting the defects 22 and 21'),
    ("a'", 36, 'THE COMPONENTS ROUTE MISSED BEFORE THE RECORD COMMIT.', 'THE SEAT’S', 'vi',
     'the components route skipped before the record commit, a second record push following'),
    ("b'", 44, 'N4\'S CLOSE CLAUSE READS A BANK NOT YET WRITTEN.', 'THE ORDER’S', 'vi', 'N4 reading the events bank’s absence at scores close'),
    ("c'", 48, 'NO PUSH CAPTURE.', 'PUSH_GATED’S', 'v', 'no capture written by any push but the closing’s'),
    ("d'", None, '', 'THE NAVIGATOR’S', 'ii', '(R322)(3)(ii)’s wording “the step bank row marked gate” in the singular'),
)
RECORDS = ((18, 'THE ROOT\'S PROMPT AND THE THROUGHSTONE.', 'the root’s prompt and the throughstone'),
           (41, 'THE AUTO-MODE NOTE A SEVENTH TIME.', 'the harness note not followed'))
GATE_WORDS = 'the act’s step bank row marked gate'
GATE_COMMITS = ('afe3903a', 'dcb3b286')
ROW = ('  (33) b712\'s record after its seal (relay data/b712_events.txt, nine starting lines, and (R322)(3)(ii)`s wording): lettered\n'
       '      (w) the gate`s work in two commits read as one, the arm`s, and (d\') the wording "the step bank row marked gate" in the singular,\n'
       '      the navigator`s, both taken up by (R323)(4)(ii) (v4 row (63)); (x) N5 refuted by the scorer`s own list, the scorer`s, by (i) (62);\n'
       '      (y) rootdry run twice, the seat`s, by (iv) (65); (z) the two sealed tools counting 22 and 21, the tools`, by (iii) (64); (a\') the\n'
       '      components route skipped before the record commit, the seat`s, and (b\') N4 reading the events bank`s absence, the order`s, both by\n'
       '      (vi) (67); (c\') no push capture, push_gated`s, by (v) (66). Records, unlettered: :18, :41. THE CORRECTION: relay\n'
       '      data/standing_clauses_v4.txt rows (61)-(68), the repairs` diffs and controls data/b713_tool_repairs.txt. The generated\n'
       '      corrigendum entry stands at FINDINGS.md :%s.')


def compose():
    ev = C78.rd(os.path.join(D, 'b712_events.txt')).replace(chr(13), '').split(NL)
    starts = [i for i, l in enumerate(ev, 1) if re.match(r'^    [A-Z]', l)]
    want_starts = sorted([n for _x, n, *_r in LETTERED if n] + [n for n, _h, _w in RECORDS])
    heads = dict((n, ev[n - 1].strip()) for n in starts)
    miss_heads = [n for _x, n, h, *_r in LETTERED if n and not heads.get(n, '').startswith(h)] + \
                 [n for n, h, _w in RECORDS if not heads.get(n, '').startswith(h)]
    dt = C78.rd(os.path.join(D, 'b712_defects.txt'))
    prev = [re.match(r"\(([a-z]'?)\)", x).group(1) for x in REC.letters_of(dt)]
    v4 = C78.rd(os.path.join(D, 'standing_clauses_v4.txt')).split(NL)
    rows = {}
    for i, l in enumerate(v4, 1):
        m = re.match(r"^  \((6[2-7])\) STANDING STOP SOURCE \(R323\)\(4\)\(([iv]+)\) ;", l)
        if m:
            rows[m.group(2)] = (int(m.group(1)), i)
    bad_rows = [(x, r) for x, _n, _h, _o, r, _w in LETTERED if rows.get(r, (0,))[0] != V4_ROWS[r]]
    f12 = C78.rd(os.path.join(D, 'b712_ferry.txt')).split(NL)
    gate_words = f12[10].count(GATE_WORDS) if len(f12) > 10 else 0
    st = json.load(open(os.path.join(D, 'b712_steps.json'), encoding='utf-8')).get('rows') or []
    gate = [(r.get('commit', '')[:8], r.get('phase')) for r in st if r.get('commit', '')[:8] in GATE_COMMITS]
    s = dict(starts=starts, heads=heads, prev=prev, rows=rows, gate_words=gate_words, gate=gate)
    bad = [k for k, v in (('the nine starting lines', starts == want_starts), ('each item`s head', not miss_heads),
                          ('b712`s twenty-two letters', prev == PREV_LETTERS), ('the v4 rows of the six repairs', not bad_rows),
                          ('b712`s ferry :11 carrying the singular wording once', gate_words == 1),
                          ('the gate`s two commits in b712`s step bank', sorted(gate) == [('afe3903a', 'gate'), ('dcb3b286', 'component 5')])) if not v]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (heads missed %s ; rows %s ; starts %s ; gate %s)' % (bad, miss_heads, bad_rows, starts, gate))
    return s


def entry_text(s):
    return NL + NL.join(_entry_lines(s)) + NL


def _repair_words(s, r):
    return ('TAKEN UP BY (R323)(4)(%s), relay data/standing_clauses_v4.txt row (%d) (:%d); its diff and its two-instance control in relay '
            'data/b713_tool_repairs.txt' % (r, s['rows'][r][0], s['rows'][r][1]))


def _letter_words(x):
    return x.replace("'", '′')


def _entry_lines(s):
    L = [TITLE, '',
         ('b712’s events bank (relay data/b712_events.txt) carries nine starting lines (:%s), entered after its seal and not lettered, '
          'for this act’s corrigendum under standing clauses v2 row (52). (R323)(3) letters seven of them as defects, each with its owner, and '
          'adds one; b712’s defects bank carries (a)-(v), so these are (w)-(z) and (a′)-(d′). Two are entered as records. b712’s events bank, '
          'its defects bank, its face, its trail record (PLACE-papers OPEN_TRAILS :%d) and every root-named bank are not edited.' % (
              ', :'.join(str(n) for n in s['starts']), K.B711_TRAIL)), '']
    why = {
        'w': ('The gate’s work before the lock went into two relay commits, afe3903a (its step row phase gate) and dcb3b286 (phase component 5); '
              'the face declared neither, so G-NOTHING-RAN-AHEAD read dcb3b286 undeclared and failed pre-push and post-push. A step bank row now '
              'carries the list of its commits, and every arm reading a step reads all of them.'),
        'x': ('The scores read N5 REFUTED on data/b711_steps.json, whose one change was the step-zero commit the ferry ordered and the face’s (W) '
              'named; the sealed record tool’s own list N5_RELAY_DATA did not name it. The scorer’s allowed writes now derive from the (W) bank '
              'of the act’s ruling and its banks, with no list of its own.'),
        'y': ('A second rootdry before the root rewrote data/b712_root_banks_dry.json/.txt, the pre-lock reading at afe3903a, so G-ROOTDRY-READY '
              'read the bank’s time after the lock and failed. A bank written before the lock now refuses to be rewritten after it.'),
        'z': ('The record tool counted the seat’s defects 22 and G-TRAIL-LINES-EQUAL-DEFECTS counted 21 on the owner of (h), so the trail arm '
              'failed on the landed trail. The defects bank is now counted by one function every tool imports.'),
        "a'": ('The components route was not run before b712’s record commit 755b03aa, so the act part read PRE-PUSH; it ran after, and a second '
               'record push (603a3b63) followed. The close’s steps now stand as one numbered row of the standing clauses, each closing tool '
               'refusing to run ahead of an unfinished step.'),
        "b'": ('scores close read N4 HELD on the events bank’s absence (“none found”), the events bank being written after the close in '
               'Component 6’s order when the events had been found. The close’s order now puts the events bank before scores close.'),
        "c'": ('Every push ran tools/push_gated.sh without PUSH_GATED_LOG, so no capture exists but the closing’s, and the closing’s head line read '
               '“none read”. The push tool now writes its capture on every push, named from the repository, the branch and the act, and the '
               'head line reads each repository’s main at the remote by ls-remote.'),
        "d'": ('relay data/b712_ferry.txt :11 carries “%s” once, a row in the singular, where b712’s gate was two rows of its step bank (%s). The '
               'repair reads every commit of a step.' % (GATE_WORDS, ', '.join('%s phase %s' % g_ for g_ in sorted(s['gate'])))),
    }
    for x, n, _h, own, r, words in LETTERED:
        place = 'relay data/b712_events.txt :%d' % n if n else 'the item (R323)(3) adds'
        L += ['**(%s) %s** (%s; %s). %s %s.' % (_letter_words(x), words[0].upper() + words[1:], place, own, why[x], _repair_words(s, r)), '']
    L += ['**Records, unlettered:** ' + '; '.join(':%d %s' % (n, w) for n, _h, w in RECORDS) + ' (relay data/b712_events.txt).', '',
          'The sealed face, the events and defects banks, the trail record and every root-named bank are not edited -- this entry is their '
          'correction. Nothing here proves RH or GRH.', '',
          ('*Filed at b713 on the author’s ruling `(R323)`(3): generated by relay `tools/b713_corrigendum.py`, written whole at b713 in the '
           'corrigendum form of relay `tools/b678_corrigendum.py` (its reader imported unchanged), banked as relay `data/b713_corrigendum.txt`, '
           'the corrigenda bank `data/b675_corrigenda.txt` appended at row (33); it answers b712’s events after its seal.*')]
    return L


def bank_lines(s, landed_line=None):
    L = ['b713 -- THE CORRIGENDUM ENTRY FOR b712`S EVENTS AFTER ITS SEAL, (R323)(3) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the figures read before the write: the starting lines :%s ; b712`s letters %s ;' % (', :'.join(str(n) for n in s['starts']), ''.join(s['prev'])),
         '### the v4 rows %s ;' % ' '.join('(%s) row (%d) :%d' % (r, s['rows'][r][0], s['rows'][r][1]) for r in ('i', 'ii', 'iii', 'iv', 'v', 'vi')),
         '### b712`s ferry :11 carrying the singular wording %d time(s) ; b712`s gate commits %s.' % (s['gate_words'], sorted(s['gate'])), '']
    L += ['  ' + l for l in _entry_lines(s)]
    L += ['', '### ### **ITEMS %d: LETTERED %d (w)-(d′), EACH TAKEN UP BY A REPAIR OF (R323)(4) ; RECORDS %d ; '
              'THE FACE, THE EVENTS AND DEFECTS BANKS, THE TRAIL AND THE ROOT-NAMED BANKS UNEDITED ; THE ENTRY AT FINDINGS :%s.**' % (
                  len(LETTERED) + len(RECORDS), len(LETTERED), len(RECORDS), landed_line if landed_line else 'NOT YET WRITTEN')]
    return L


def _membrane(p):
    """standing clauses v2 row (53): the membrane before a write under relay data/ (tools/act_membrane.py guard_path)."""
    import act_membrane as MEM
    MEM.guard_path('b713', p, REC.R.ROOT_EXCLUDE)


def _put(name, data):
    p = os.path.join(D, name)
    _membrane(p)
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
        print(ROW % 'NOT YET WRITTEN')
        return
    REC.land([('FINDINGS.md', TITLE, text)], 'b713_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b713_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    _put('b713_corrigendum.txt', NL.join(L) + NL)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE,
             lettered=[dict(letter=x, line=n, owner=o, repair=r, v4_row=V4_ROWS[r]) for x, n, _h, o, r, _w in LETTERED],
             records=[n for n, _h, _w in RECORDS], starts=s['starts'], row=33)
    _put('b713_corrigendum.json', json.dumps(j, indent=1, ensure_ascii=False) + NL)
    print(L[-1])
    print(ROW % ln)


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b713_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
