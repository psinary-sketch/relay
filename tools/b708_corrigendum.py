# -*- coding: utf-8 -*-
"""b708_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R318)(2): b707's item found after its seal -- (i) the write list omitting the mirror
builder's own state file tools/mirror_prevbuild.json (G-WRITELIST-KINDS failing at the post-push run; N5 REFUTED at the close) -- and the
three trail-equality arms (G-TRAIL-DEFECTS-EQUAL, G-TRAIL-RESOLVED-EQUAL, G-TRAIL-LINES-EQUAL-DEFECTS) failing because (i) was lettered after
the trail landed -- answered by one generated FINDINGS entry in b678's corrigendum form, in the bank's words; b707's sealed face (relay
data/b707_registration_2026-10-22.txt), its trail record (PLACE-papers OPEN_TRAILS :15688) and every root-named bank unedited.

### Carried from tools/b707_corrigendum.py, its rows rewritten for b707's record. b678's tool (tools/b678_corrigendum.py) is IMPORTED and
### unchanged: its reader `rd`; its form -- one generated entry, each line it corrects quoted with its place, the corrected reading and its source,
### the figures read from their banks and checked before any write, `dry` then `land`. Every figure is read, none typed:
###   (i): the row of data/b707_defects.txt by letter and line (the repaired reader of b703, through b708_record);
###   the eight failing arms: data/b707_checks_postpush.txt's LIVE FAILING list; the four declared on the face: the face's declaration line;
###   the trail's Defects line: PLACE-papers OPEN_TRAILS from the trail head at :15688, its letters read; the trail's own line number;
###   the correction: data/b708_rules.txt (the rules bank) and this act's face's (W) row ((R318)(2)), named by path.
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b708_record's
### guarded landing, data/b708_corrigendum.txt (.json). The corrigenda bank's row (28) is appended by the seat through the Edit tool from the
### bank line this tool prints (ROW). Written by the Write tool at b708; it writes those two banks and the one FINDINGS entry.
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
import b708_worklist as K         # noqa: E402
import b708_record as REC         # noqa: E402  ### the guarded landing and the repaired defects reader

TITLE = ('## Corrigendum to b707’s record after its seal (relay data/b707_defects.txt, data/b707_checks_postpush.txt): the write list omitting the '
         'mirror builder’s state file and the three trail-equality arms')
TRAIL_ARMS = ('G-TRAIL-DEFECTS-EQUAL', 'G-TRAIL-RESOLVED-EQUAL', 'G-TRAIL-LINES-EQUAL-DEFECTS')
FOUR = ('G-WRITELIST-KINDS',) + TRAIL_ARMS
LETTERS = ('i',)


def _row(L, letter):
    s = next((i + 1 for i, l in enumerate(L) if l.startswith('    (%s) ' % letter)), 0)
    if not s:
        return 0, 0, ''
    e = next((i for i in range(s, len(L)) if re.match(r'^    \([a-z]\) ', L[i]) or L[i].startswith('###')), len(L))
    return s, e, ' '.join(x.strip() for x in L[s - 1:e])


def compose():
    df = C78.rd(os.path.join(D, 'b707_defects.txt')).split(NL)
    rows = dict((x, _row(df, x)) for x in LETTERS)
    ck = C78.rd(os.path.join(D, 'b707_checks_postpush.txt'))
    m8 = re.search(r'LIVE FAILING : (\d+) \[(.*?)\]', ck)
    fails = [x.strip().strip("'") for x in (m8.group(2) if m8 else '').split(',') if x.strip()]
    face = C78.rd(os.path.join(ROOT, *K.B707_FACE.split('/')))
    md = re.search(r'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME:\*\* ([^.]*)\.', ' '.join(face.split()))
    declared = sorted(set(re.findall(r'`([GF]-[A-Z0-9-]+)`', md.group(1)))) if md else []
    ot = C78.rd(os.path.join(K.PP, 'OPEN_TRAILS.md')).split(NL)
    th = next((i + 1 for i, l in enumerate(ot) if l.startswith('### b707 — lane two, act one hundred and thirty-four')), 0)
    dl = next((i + 1 for i in range(th, len(ot)) if ot[i].startswith('**Defects** (relay data/b707_defects.txt)')), 0) if th else 0
    rl = next((i + 1 for i in range(th, len(ot)) if ot[i].startswith('**Resolved by the seat')), 0) if th else 0
    letters = re.findall(r'\(([a-z])\) THE (?:SEAT|NAVIGATOR)', ot[dl - 1]) if dl else []
    short = REC._defect_short('b707')
    bank_letters = [re.match(r'^\(([a-z])\)', x).group(1) for x in short]
    rules = C78.rd(os.path.join(D, 'b708_rules.txt'))
    wrow = ' '.join(face.split())
    post_seal = [a for a in fails if a not in declared]
    ok = (rows['i'][0] and 'WRITE LIST OMITS THE MIRROR BUILDER' in rows['i'][2] and len(fails) == 8 and len(declared) == 4
          and sorted(post_seal) == sorted(FOUR) and th == K.B707_TRAIL and dl and rl and letters == list('abcdefgh') and bank_letters == list('abcdefghi')
          and '(1) THE REPORT TOOL IS KEPT OUT OF THE SEALED LIST' in rules and 'tools/mirror_build.ps1` (the b670 tool, unedited) | `D:/MY-DOwnloads/mirror-refresh-2026-10-22-b707.zip` and its stage' in wrow)
    if not ok:
        sys.exit('### A SOURCE LINE IS NOT AS READ (row %s, failing %s, declared %s, trail :%s, Defects :%s letters %s, bank %s) -- NOTHING WRITTEN' % (
            rows['i'][0], fails, declared, th, dl, ''.join(letters), ''.join(bank_letters)))
    return dict(rows=dict((x, (rows[x][0], rows[x][1] - 1 if rows[x][1] > rows[x][0] else rows[x][0], rows[x][2])) for x in LETTERS), fails=fails,
                declared=declared, post_seal=post_seal, trail=th, defects_line=dl, resolved_line=rl, letters=''.join(letters), bank_letters=''.join(bank_letters))


def entry_text(s):
    r = s['rows']
    L = ['', TITLE, '',
         'b707’s face was locked after Components 1-4 (relay data/b707_registration_2026-10-22.txt) with four failures declared on it by name '
         '(%s); its post-push suite found four more, none editable in a sealed tool, and its trail record (PLACE-papers OPEN_TRAILS :%d) landed '
         'with its Defects line reading (a)-(h) before (i) was lettered. This entry answers the four in the bank’s words, each with its cause '
         'by line; the face, the trail record and every root-named bank are not edited.' % (', '.join(s['declared']), s['trail']), '',
         '**(i) THE SEAT’S: THE WRITE LIST OMITS THE MIRROR BUILDER’S POINTER FILE** (relay data/b707_defects.txt :%d-:%d). tools/mirror_prevbuild.json '
         'is written by tools/mirror_build.ps1 at every build (the previous build’s name, read for the span line) and committed at every closing; '
         'b707’s face’s (W) row for the builder named the zip and its stage alone, and b707 built its mirror before its post-push suite (the '
         'ferry’s order), so G-WRITELIST-KINDS read the file uncovered at the post-push standing-c part and N5 read REFUTED at the close on it '
         'alone. THE CORRECTION: under (R318)(2) this act’s face carries the row `tools/mirror_build.ps1 | the zip, its stage, '
         'tools/mirror_prevbuild.json` -- the builder’s own state file, written at every build and committed with the closing -- so the arm and '
         'N5 read it as the builder’s and not as a stray write; the file stands as b707 committed it (relay b5898a61), not edited.' % r['i'][:2], '',
         '**The three trail-equality arms** (%s). The trail record (OPEN_TRAILS :%d) landed with its Defects line (:%d) and its Resolved line '
         '(:%d) reading (a)-(h), and (i) was lettered after it at the post-push run, so the arms reading those lines against data/b707_defects.txt '
         '((a)-(i)) fail by that order (relay data/b707_checks_postpush.txt). THE CORRECTION: no repair -- the sequence rule of (R315)(2) binds '
         'and is read by the gate: no defect is lettered after the trail’s dry run without that dry run re-read; a post-seal failure is '
         'lettered and never hidden (b707’s trap 3).' % (', '.join(TRAIL_ARMS), s['trail'], s['defects_line'], s['resolved_line']), '',
         'The sealed face, the trail record and every root-named bank are not edited -- this entry is their correction. Nothing here proves RH '
         'or GRH.', '',
         '*Filed at b708 on the author’s ruling `(R318)`(2): generated by relay `tools/b708_corrigendum.py`, carried from '
         '`tools/b707_corrigendum.py`, in the corrigendum form of relay `tools/b678_corrigendum.py` (its reader imported unchanged), banked as '
         'relay `data/b708_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at row (28); it answers b707’s four items '
         'after its seal.*', '']
    return NL.join(L)


ROW = ('  (28) b707\'s suite after its seal (relay data/b707_checks_postpush.txt, LIVE FAILING 8, four beyond the face): G-WRITELIST-KINDS on\n'
       '      tools/mirror_prevbuild.json, the mirror builder\'s own state file written at every build and committed at every closing, which the\n'
       '      face\'s (W) row for the builder did not name ((i), THE SEAT\'S; N5 REFUTED at the close on it alone), and the three trail-equality\n'
       '      arms failing because (i) was lettered after the trail (OPEN_TRAILS :15688) landed. THE CORRECTION: the (W) row of b708\'s face names\n'
       '      the state file beside the zip and its stage under (R318)(2); the trail arms no repair, the sequence rule binding. The generated\n'
       '      corrigendum entry stands at FINDINGS.md :%s.')


def bank_lines(s, landed_line=None):
    r = s['rows']
    return ['b708 -- THE CORRIGENDUM, (R318)(2): b707`S POST-SEAL ITEM (i) AND THE THREE TRAIL-EQUALITY ARMS, ANSWERED BY ONE GENERATED '
            'FINDINGS ENTRY IN b678`s FORM', '',
            '### rows are the corrected lines and the lines that correct them, each read from its source by line; the face, the trail and the '
            'root-named banks are not rewritten.', '',
            '  (i) THE WRITE LIST       relay data/b707_defects.txt :%d-:%d | G-WRITELIST-KINDS, the face`s (W) row for tools/mirror_build.ps1 (relay data/b707_registration_2026-10-22.txt :320) | '
            'this act`s face names tools/mirror_prevbuild.json beside the zip and its stage ((R318)(2))' % r['i'][:2],
            '  THE TRAIL ARMS           %s | the trail OPEN_TRAILS :%d, its Defects line :%d (%s) and Resolved line :%d against the bank (%s) | no repair; the sequence rule' % (
                ', '.join(TRAIL_ARMS), s['trail'], s['defects_line'], s['letters'], s['resolved_line'], s['bank_letters']),
            '  THE FAILING EIGHT        relay data/b707_checks_postpush.txt | %s | declared on the face %s ; found after the seal %s' % (
                ', '.join(s['fails']), ', '.join(s['declared']), ', '.join(s['post_seal'])),
            '  THE CORRIGENDA BANK     relay data/b675_corrigenda.txt, row (28) appended by this act through the Edit tool',
            '', '### ### **FOUR ITEMS ANSWERED ((i), THREE TRAIL ARMS) ; THE FACE, THE TRAIL AND THE ROOT-NAMED BANKS UNEDITED ; THE ENTRY AT FINDINGS :%s.**' % (
                landed_line or 'NOT YET WRITTEN')]


def main(route):
    s = compose()
    text = entry_text(s)
    if route == 'dry':
        REC.R.screens([('FINDINGS.md', TITLE, conv(text))], 'corrigendum', True)
        print(conv(text))
        print(NL.join(bank_lines(s)))
        print(ROW % 'NOT YET WRITTEN')
        return
    REC.land([('FINDINGS.md', TITLE, text)], 'b708_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b708_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    p = os.path.join(D, 'b708_corrigendum.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE, lettered=list(LETTERS), event=None,
             trail_arms=list(TRAIL_ARMS), failing=s['fails'], declared=s['declared'], post_seal=s['post_seal'], trail=s['trail'],
             defects_line=s['defects_line'], row=28)
    p = os.path.join(D, 'b708_corrigendum.json')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])
    print(ROW % ln)


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b708_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
