# -*- coding: utf-8 -*-
"""b712_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R322)(2): b711's events after its seal (relay data/b711_events.txt, sixteen starting
lines) and the one item the navigator adds, answered by one generated FINDINGS entry in b678's corrigendum form, in the banks' words. Ten are
lettered as defects, each with its owner, (k)-(t) after b711's ten letters (a)-(j) (relay data/b711_defects.txt); seven are entered as
records, unlettered. Each lettered item names the repair of (3) that takes it up (relay data/b712_tool_repairs.txt by its row) or "carried"
with its reason. b711's events bank, its defects bank, its sealed face (relay data/b711_registration_2026-10-25.txt), its trail record
(PLACE-papers OPEN_TRAILS :15850) and every root-named bank unedited.

### Written whole by the Write tool at b712, its items rewritten for b711's events (b708-b711 wrote theirs the same way). b678's reader `rd`
### IMPORTED unchanged; its form -- one generated entry, each item quoted with its place, the corrected reading and its source, the figures read
### from their banks and checked before any write, `dry` then `land`. Every figure is read, none typed:
###   the starting lines: data/b711_events.txt, a line opening four spaces and a non-space; each item's head checked by its needle;
###   b711's letters: data/b711_defects.txt by tools/b712_record.py letters_of (ten, (a)-(j));
###   the repairs: data/b712_tool_repairs.txt, each row's label and the events line it answers ("Answers b711`s events :<n>");
###   the controls: data/b712_repair_controls.json, every case AS WANTED, each section present;
###   the added item: tools/mirror_prevbuild.json's blob at b707 (b5898a61) and at b711's closing (4a383ac8), read by git rev-parse.
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b712_record's
### guarded landing, data/b712_corrigendum.txt (.json). The corrigenda bank's row (32) is appended by the seat through the Edit tool from the
### bank line this tool prints (ROW). It writes those two banks and the one FINDINGS entry.
"""
import json
import os
import re
import subprocess
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
import b712_worklist as K         # noqa: E402
import b712_record as REC         # noqa: E402  ### the guarded landing, the letters reader

TITLE = ('## Corrigendum to b711’s record after its seal (relay data/b711_events.txt): sixteen events and one added item, ten lettered '
         '(k)-(t) with their owners, seven entered as records, under (R322)(2)')
PREV_LETTERS = list('abcdefghij')
# ### the lettered items, (R322)(2)'s order: (letter, events line or None for the added item, the head's needle, the owner, the repair row or
# ### 'carried', the item's words as the ruling names it)
LETTERED = (
    ('k', 3, 'FOUR PIPES AT COMPONENT 5, BEFORE THE SEAL, FOUND AFTER IT.', 'THE SEAT’S', '(60)', 'the four pipes at Component 5'),
    ('l', 11, 'THE ENTRY\'S QUESTION COUNT READ AT ITS LANDING.', 'THE SEALED RECORD TOOL’S FORM, CARRIED', 'carried',
     'the entry’s question count read at its landing'),
    ('m', 15, 'THE REPORT TOOL\'S FIRST TWO RUNS MISREAD TWO OF ITS OWN SOURCES.', 'THE SEAT’S', 'REPORT', 'the report tool’s two misreads'),
    ('n', 22, 'THE NAVIGATOR\'S: S2 NOT SCORABLE BEFORE THE ROOT', 'THE NAVIGATOR’S', 'REPORT', 'S2 asked before the root'),
    ('o', 46, 'THE NEXT LINE\'S PORT CLAUSE IS CARRIED BESIDE IT, NOT IN IT.', 'THE NAVIGATOR’S', 'NEXT',
     'the port clause made b712’s after the seal, outside the sealed NEXT line'),
    ('p', 61, 'THE FACE NAMES NO POST-SEAL PROMPT, AND THE ROOT\'S PROMPT IS POST-SEAL (G-ANSWERS-BANKED).', 'THE FACE BUILDER’S', '(56)',
     'the face naming no post-seal prompt'),
    ('q', 66, 'A COMMIT AHEAD OF THE LOCK WHOSE HASH THE FACE DOES NOT CARRY (G-NOTHING-RAN-AHEAD).', 'THE FACE BUILDER’S', '(57)',
     'the gate’s commit absent from the face'),
    ('r', 75, 'THE MIRROR BANKED ONCE BEFORE ITS ROOT LINE.', 'THE SEAT’S', '(59)', 'the mirror banked before its root line'),
    ('s', 79, 'THE CLOSING\'S HEAD LINE: NO SCORE, AND THE ROOT\'S PROMPT COUNTED TWICE.',
     'THE SCORE FIELD THE NAVIGATOR’S WORD, THE PROMPT COUNT THE CLOSING TOOL’S', '(58)', 'the head line'),
    ('t', None, '', 'THE CLOSING TOOL’S', '(60)',
     'the closing’s sentence “committed with this closing” for tools/mirror_prevbuild.json when its blob was unchanged since b707'),
)
RECORDS = ((29, 'THE AUTHOR\'S WORD ON S2, DELIVERED', 'the author’s word on S2'),
           (39, 'THE WORD\'S CITES, CHECKED BEFORE THE SEAT ACTS ON IT', 'its cites checked'),
           (43, 'THE AUTO-MODE NOTE AFTER THE ROOT\'S PUSH, NOT FOLLOWED.', 'the harness note not followed'),
           (51, 'THE PRE-PUSH SUITE HELD AT ITS FIRST PART BY THE MEMORY HOLD.', 'the memory hold refusing'),
           (55, 'THE RE-READ AFTER THE AUTHOR\'S WORD ON MEMORY, STILL BENEATH THE HOLD.', 'the memory hold holding'),
           (58, 'THE SUITE RESUMED ON THE AUTHOR\'S "continue"', 'the suite resumed'),
           (71, 'THE SUITE AND THE SCORES AT THE CLOSE.', 'the suite and scores at the close'))
STATE_FILE = 'tools/mirror_prevbuild.json'
B707, B711_CLOSING = 'b5898a61', '4a383ac8'
ROW = ('  (32) b711\'s record after its seal (relay data/b711_events.txt, sixteen starting lines, and the closing`s sentence on\n'
       '      tools/mirror_prevbuild.json): lettered (k) the four pipes at Component 5, the seat`s, repaired by (60); (l) the entry`s question count\n'
       '      read at its landing, the sealed record tool`s form, carried; (m) the report tool`s two misreads, the seat`s, and (n) S2 asked before\n'
       '      the root, the navigator`s, both taken up by the standing report tool (data/b712_report.txt); (o) the port clause outside the sealed\n'
       '      NEXT, the navigator`s, repaired by the NEXT line; (p) the face naming no post-seal prompt and (q) the gate`s commit absent from the\n'
       '      face, the face builder`s, repaired by (56) and (57); (r) the mirror banked before its root line, the seat`s, repaired by (59); (s) the\n'
       '      head line, its score field the navigator`s word and its prompt count the closing tool`s, repaired by (58); (t) "committed with this\n'
       '      closing" for an unchanged blob, the closing tool`s, repaired by (60). Records, unlettered: :29, :39, :43, :51, :55, :58, :71. THE\n'
       '      CORRECTION: relay data/b712_tool_repairs.txt rows (56)-(60) and NEXT, their controls data/b712_repair_controls.txt. The generated\n'
       '      corrigendum entry stands at FINDINGS.md :%s.')


def _g(*a):
    return subprocess.run(('git', '-C', ROOT) + a, capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def compose():
    ev = C78.rd(os.path.join(D, 'b711_events.txt')).replace(chr(13), '').split(NL)
    starts = [i for i, l in enumerate(ev, 1) if re.match(r'^    \S', l)]
    want_starts = sorted([n for _x, n, *_r in LETTERED if n] + [n for n, _h, _w in RECORDS])
    heads = dict((n, ev[n - 1].strip()) for n in starts)
    miss_heads = [n for _x, n, h, *_r in LETTERED if n and not heads.get(n, '').startswith(h)] + \
                 [n for n, h, _w in RECORDS if not heads.get(n, '').startswith(h)]
    dt = C78.rd(os.path.join(D, 'b711_defects.txt'))
    prev = [re.match(r'\((\w)\)', x).group(1) for x in REC.letters_of(dt)]
    tr = C78.rd(os.path.join(D, 'b712_tool_repairs.txt')).split(NL)
    rows = {}
    for i, l in enumerate(tr, 1):
        m = re.match(r'^  (\(\d+\)|NEXT) ', l)
        if m:
            body = []
            for x in tr[i:i + 8]:
                if not x.startswith('      '):
                    break
                body.append(x.strip())
            body = ' '.join(body)
            rows[m.group(1)] = (i, sorted(set(int(x) for x in re.findall(r':(\d+)', re.sub(r'.*Answers b711`s events', '', body)[:60]))))
    need = [(x, n, r) for x, n, _h, _o, r, _w in LETTERED if r not in ('carried', 'REPORT')]
    bad_rows = [(x, r) for x, n, r in need if r not in rows or (n and n not in rows[r][1])]
    ctl = json.load(open(os.path.join(D, 'b712_repair_controls.json'), encoding='utf-8'))
    cases = ctl.get('cases') or []
    secs = sorted(set(c.get('section') for c in cases))
    nots = [c for c in cases if not c.get('as_wanted')]
    blob7 = _g('rev-parse', '%s:%s' % (B707, STATE_FILE)).strip()
    blob11 = _g('rev-parse', '%s:%s' % (B711_CLOSING, STATE_FILE)).strip()
    cl11 = C78.rd(os.path.join(D, 'b711_closing.txt')).split(NL)
    said = next((i for i, l in enumerate(cl11, 1) if 'mirror_prevbuild.json' in l and 'committed with this closing' in l), 0)
    s = dict(starts=starts, heads=heads, prev=prev, rows=rows, secs=secs, n_cases=len(cases), nots=len(nots), blob7=blob7, blob11=blob11, said=said)
    bad = [k for k, v in (('the sixteen starting lines', starts == want_starts), ('each item`s head', not miss_heads),
                          ('b711`s ten letters', prev == PREV_LETTERS), ('the repair rows answering their lines', not bad_rows),
                          ('the controls every case as wanted', cases and not nots),
                          ('the control sections', set(secs) >= {'i', 'ii', 'iii', 'iv', 'v', 'NEXT'}),
                          ('the blob unchanged b707 to b711`s closing', blob7 and blob7 == blob11),
                          ('b711`s closing saying "committed with this closing"', said)) if not v]
    if bad:
        sys.exit('### THE BANKS NOT AS READ: %s -- NOTHING COMPOSED (heads missed %s ; rows %s ; starts %s)' % (bad, miss_heads, bad_rows, starts))
    return s


def entry_text(s):
    return NL + NL.join(_entry_lines(s)) + NL


def _repair_words(s, r):
    if r == 'carried':
        return 'CARRIED'
    if r == 'REPORT':
        return 'TAKEN UP BY THE STANDING REPORT TOOL of (R322)(3) (relay data/b712_report.txt, written at Component 5)'
    return 'REPAIRED by relay data/b712_tool_repairs.txt row %s (:%d), its control data/b712_repair_controls.txt' % (r, s['rows'][r][0])


def _entry_lines(s):
    L = [TITLE, '',
         ('b711’s events bank (relay data/b711_events.txt) carries sixteen starting lines (:%s), entered after its seal and not lettered, '
          'for this act’s corrigendum under standing clauses v2 row (52). (R322)(2) letters ten of them as defects, each with its owner, and '
          'adds one; b711’s defects bank carries (a)-(j), so these are (k)-(t). Seven are entered as records. b711’s events bank, its defects '
          'bank, its face, its trail record (PLACE-papers OPEN_TRAILS :%d) and every root-named bank are not edited.' % (
              ', :'.join(str(n) for n in s['starts']), K.B711_TRAIL)), '']
    why = dict(
        k=('Four PowerShell pipes sent before the seal (the command bank’s rows 322, 323, 343, 355), read after it; the face’s spec read seven '
           'from a command bank last written before row 355. Nothing was banked from any of them.'),
        l=('The entry’s foot counts the questions put before the root, read when the entry lands; the root’s prompt follows by the act’s order. '
           'The foot names what it counts, so the form is carried and the closing’s head line counts every prompt.'),
        m=('Its pattern stopped inside “r(rho)” and it compared counts above 325 with totals above 150, so it printed four DIFFERS of its own '
           'making before its third run read 21 of 21 EQUAL. The standing report tool recomputes each line from its bank with path, line and '
           'sha256.'),
        n=('Check (g) of the author’s word asked for a score the root itself produces. The standing report tool prints its scores line after '
           'the root.'),
        o=('The author’s word on S2 made DirichletC7Order.lean :501:31 b712’s port clause after the seal; the sealed NEXT named b712 without it. '
           'The NEXT line now prints every open-orders row whose status names the next act, read at closing time.'),
        p=('The face read NONE; the root’s prompt followed the lock by the act’s order, so G-ANSWERS-BANKED failed. The face builder now '
           'prints the row from the order.'),
        q=('relay 85c26c1c, the gate before the lock, could not be on the face it stamps. G-NOTHING-RAN-AHEAD now reads it from the step bank’s '
           'row marked gate.'),
        r=('mbank ran before mroot and banked THE ROOT LINE : ### NONE, then was rewritten. The mirror bank now refuses while the act’s root is '
           'appended and the export carries no root line for it.'),
        s=('“2 prompts answered” for one prompt (b700’s “+ 1” carried) and no score. The head line now counts the answers bank’s rows with '
           'nothing added and carries “scores <k> of 8 HELD” from the scores-close bank.'),
        t=('b711’s closing (relay data/b711_closing.txt :%d) says the state file was committed with the closing, but its blob %s is the same '
           'at b707 (relay %s) and at b711’s closing (relay %s). The closing now reads the blob against its last commit before it says '
           '“committed”.' % (s['said'], s['blob7'][:8], B707, B711_CLOSING)))
    for x, n, _h, own, r, words in LETTERED:
        place = 'relay data/b711_events.txt :%d' % n if n else 'the item (R322)(2) adds'
        L += ['**(%s) %s** (%s; %s). %s %s.' % (x, words[0].upper() + words[1:], place, own, why[x], _repair_words(s, r)), '']
    L += ['**Records, unlettered:** ' + '; '.join(':%d %s' % (n, w) for n, _h, w in RECORDS) + ' (relay data/b711_events.txt).', '',
          'The sealed face, the events and defects banks, the trail record and every root-named bank are not edited -- this entry is their '
          'correction. Nothing here proves RH or GRH.', '',
          ('*Filed at b712 on the author’s ruling `(R322)`(2): generated by relay `tools/b712_corrigendum.py`, written whole at b712 in the '
           'corrigendum form of relay `tools/b678_corrigendum.py` (its reader imported unchanged), banked as relay `data/b712_corrigendum.txt`, '
           'the corrigenda bank `data/b675_corrigenda.txt` appended at row (32); it answers b711’s events after its seal.*')]
    return L


def bank_lines(s, landed_line=None):
    L = ['b712 -- THE CORRIGENDUM ENTRY FOR b711`S EVENTS AFTER ITS SEAL, (R322)(2) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the figures read before the write: the starting lines :%s ; b711`s letters %s ;' % (', :'.join(str(n) for n in s['starts']), ''.join(s['prev'])),
         '### the repair rows %s ;' % ' '.join('%s :%d answers %s' % (r, s['rows'][r][0], s['rows'][r][1]) for r in sorted(s['rows'])),
         '### the controls %d cases, %d not as wanted, sections %s ; %s blob %s at %s and %s at %s ; b711`s closing :%d.' % (
             s['n_cases'], s['nots'], ' '.join(s['secs']), STATE_FILE, s['blob7'][:8], B707, s['blob11'][:8], B711_CLOSING, s['said']), '']
    L += ['  ' + l for l in _entry_lines(s)]
    up = [x for x, _n, _h, _o, r, _w in LETTERED if r != 'carried']
    car = [x for x, _n, _h, _o, r, _w in LETTERED if r == 'carried']
    L += ['', '### ### **ITEMS %d: LETTERED %d (%s)-(%s) -- REPAIRED OR TAKEN UP %d, CARRIED %d (%s) ; RECORDS %d ; '
              'THE FACE, THE EVENTS AND DEFECTS BANKS, THE TRAIL AND THE ROOT-NAMED BANKS UNEDITED ; THE ENTRY AT FINDINGS :%s.**' % (
                  len(LETTERED) + len(RECORDS), len(LETTERED), LETTERED[0][0], LETTERED[-1][0], len(up), len(car),
                  ' '.join('(%s)' % x for x in car), len(RECORDS), landed_line if landed_line else 'NOT YET WRITTEN')]
    return L


def _membrane(p):
    """standing clauses v2 row (53): the membrane before a write under relay data/ (tools/act_membrane.py guard_path)."""
    import act_membrane as MEM
    MEM.guard_path('b712', p, REC.R.ROOT_EXCLUDE)


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
    REC.land([('FINDINGS.md', TITLE, text)], 'b712_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b712_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    _put('b712_corrigendum.txt', NL.join(L) + NL)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE,
             lettered=[dict(letter=x, line=n, owner=o, repair=r) for x, n, _h, o, r, _w in LETTERED],
             records=[n for n, _h, _w in RECORDS], starts=s['starts'], row=32)
    _put('b712_corrigendum.json', json.dumps(j, indent=1, ensure_ascii=False) + NL)
    print(L[-1])
    print(ROW % ln)


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b712_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
