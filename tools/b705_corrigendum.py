# -*- coding: utf-8 -*-
"""b705_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R315)(2): b704's five post-seal items -- (r) G-ACTROOT-BANKED's predicate requiring a bank
the root excludes by design, (s) G-ANSWERS-CHECKED's predicate leaving no room for the root prompt's checks, and the three trail-equality arms
(G-TRAIL-DEFECTS-EQUAL, G-TRAIL-RESOLVED-EQUAL, G-TRAIL-LINES-EQUAL-DEFECTS) failing because (r) was lettered after the trail landed -- answered
by one generated FINDINGS entry in b678's corrigendum form, in the bank's words; b704's sealed face (relay data/b704_registration_2026-10-21.txt),
its trail record (PLACE-papers OPEN_TRAILS :15552) and every root-named bank unedited.

### Carried from tools/b704_corrigendum.py, its rows rewritten for b704's record. b678's tool (tools/b678_corrigendum.py) is IMPORTED and
### unchanged: its reader `rd`; its form -- one generated entry, each line it corrects quoted with its place, the corrected reading and its source,
### the figures read from their banks and checked before any write, `dry` then `land`. Every figure is read, none typed:
###   (r), (s): the rows of data/b704_defects.txt by letter and line (the repaired reader of b703, through b705_record);
###   the eight failing arms: data/b704_checks.txt's LIVE FAILING list; the three declared on the face: the face's declaration line;
###   the trail's Defects line: PLACE-papers OPEN_TRAILS from the trail head at :15552, its letters read; the trail's own line number;
###   the repairs: data/b705_tool_repairs.txt's rows (1), (2) and data/b705_arm_sort.txt (both written before this entry).
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b705_record's
### guarded landing, data/b705_corrigendum.txt (.json). The corrigenda bank's row (25) is appended by the seat through the Edit tool from the
### bank line this tool prints (ROW). Written by the Write tool at b705; it writes those two banks and the one FINDINGS entry.
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
import b705_worklist as K         # noqa: E402
import b705_record as REC         # noqa: E402  ### the guarded landing and the repaired defects reader

TITLE = ('## Corrigendum to b704’s record after its seal (relay data/b704_defects.txt, data/b704_checks.txt): two arm predicates and the three '
         'trail-equality arms')
TRAIL_ARMS = ('G-TRAIL-DEFECTS-EQUAL', 'G-TRAIL-RESOLVED-EQUAL', 'G-TRAIL-LINES-EQUAL-DEFECTS')


def _row(L, letter):
    s = next((i + 1 for i, l in enumerate(L) if l.startswith('    (%s) ' % letter)), 0)
    if not s:
        return 0, 0, ''
    e = next((i for i in range(s, len(L)) if re.match(r'^    \([a-z]\) ', L[i]) or L[i].startswith('###')), len(L))
    return s, e, ' '.join(x.strip() for x in L[s - 1:e])


def compose():
    df = C78.rd(os.path.join(D, 'b704_defects.txt')).split(NL)
    sr, er, tr = _row(df, 'r')
    ss, es, ts = _row(df, 's')
    ck = C78.rd(os.path.join(D, 'b704_checks.txt'))
    m8 = re.search(r'LIVE FAILING : (\d+) \[(.*?)\]', ck)
    fails = [x.strip().strip("'") for x in (m8.group(2) if m8 else '').split(',') if x.strip()]
    face = C78.rd(os.path.join(D, 'b704_registration_2026-10-21.txt'))
    md = re.search(r'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME:\*\* ([^.]*)\.', ' '.join(face.split()))
    declared = sorted(set(re.findall(r'`([GF]-[A-Z0-9-]+)`', md.group(1)))) if md else []
    ot = C78.rd(os.path.join(K.PP, 'OPEN_TRAILS.md')).split(NL)
    th = next((i + 1 for i, l in enumerate(ot) if l.startswith('### b704 — lane two, act one hundred and thirty-one')), 0)
    dl = next((i + 1 for i in range(th, len(ot)) if ot[i].startswith('**Defects** (relay data/b704_defects.txt)')), 0) if th else 0
    rl = next((i + 1 for i in range(th, len(ot)) if ot[i].startswith('**Resolved by the seat')), 0) if th else 0
    letters = re.findall(r'\(([a-z])\) THE (?:SEAT|NAVIGATOR)', ot[dl - 1]) if dl else []
    short = REC._defect_short('b704')
    bank_letters = [re.match(r'^\(([a-z])\)', x).group(1) for x in short]
    arm_sort = C78.rd(os.path.join(D, 'b705_arm_sort.txt'))
    repairs = C78.rd(os.path.join(D, 'b705_tool_repairs.txt'))
    post_seal = [a for a in fails if a not in declared]
    ok = (sr and ss and 'found after the seal' in tr.lower() and 'found after the seal' in ts.lower() and len(fails) == 8 and len(declared) == 3
          and sorted(post_seal) == sorted(['G-ACTROOT-BANKED', 'G-ANSWERS-CHECKED'] + list(TRAIL_ARMS)) and th == K.B704_TRAIL and dl and rl
          and letters == list('abcdefghijklmnopq') and bank_letters == list('abcdefghijklmnopqrs') and 'G-ACTROOT-BANKED' in arm_sort
          and '(1) tools/b705_checks.py `root_banked_ok`' in repairs and '(2) tools/b705_checks.py `answers_checked_ok`' in repairs)
    if not ok:
        sys.exit('### A SOURCE LINE IS NOT AS READ ((r) :%s, (s) :%s, failing %s, declared %s, trail :%s, Defects :%s letters %s, bank %s, sort %s, repairs %s) '
                 '-- NOTHING WRITTEN' % (sr, ss, fails, declared, th, dl, ''.join(letters), ''.join(bank_letters), 'G-ACTROOT-BANKED' in arm_sort,
                                         '(1) tools/b705_checks.py `root_banked_ok`' in repairs))
    return dict(r=(sr, er - 1 if er > sr else sr, tr), s=(ss, es - 1 if es > ss else ss, ts), fails=fails, declared=declared, post_seal=post_seal,
                trail=th, defects_line=dl, resolved_line=rl, letters=''.join(letters), bank_letters=''.join(bank_letters))


def entry_text(s):
    L = ['', TITLE, '',
         'b704’s face was locked after Components 1-4 (relay data/b704_registration_2026-10-21.txt) with three failures declared on it by name '
         '(%s); its pre-push suite found five more, none editable in a sealed tool, and its trail record (PLACE-papers OPEN_TRAILS :%d) landed '
         'before the last two defects were lettered. This entry answers the five in the bank’s words, each with its cause by line; the face, '
         'the trail record and every root-named bank are not edited.' % (', '.join(s['declared']), s['trail']), '',
         '**(r) THE SEAT’S: G-ACTROOT-BANKED’S PREDICATE, WRITTEN AT THE CARRY, REQUIRES A BANK THE ROOT EXCLUDES BY DESIGN; FOUND AFTER THE '
         'SEAL** (relay data/b704_defects.txt :%d-:%d). The arm required data/b704_read_calls.txt among the root’s items where the root route '
         '(relay tools/b698_record.py :1285-:1293, rebound at tools/b704_record.py :56-:58) excludes read banks by name; every other clause held. '
         'THE CORRECTION: the predicate is the navigator’s design, repaired at b705’s carry to read the root route’s own item list (relay '
         'data/b705_tool_repairs.txt row (1)), its control on b704’s banks printed (data/b705_repair_controls.txt).' % s['r'][:2], '',
         '**(s) THE SEAT’S: G-ANSWERS-CHECKED’S PREDICATE, WRITTEN AT THE CARRY, ALLOWS NO CHECK AFTER THE CUT’S COMMIT BUT THE README FIGURE’S, '
         'SO THE ROOT PROMPT’S TWO CHECKS FAIL IT; FOUND AFTER THE SEAL** (relay data/b704_defects.txt :%d-:%d). The root’s prompt, the one prompt '
         'the ferry allows after the seal, was checked before the step it governs, as b703’s was; the arm left it no room. THE CORRECTION: the '
         'navigator’s design, repaired at b705’s carry to admit the checks the root prompt requires, each printed with its time (relay '
         'data/b705_tool_repairs.txt row (2); data/b705_repair_controls.txt).' % s['s'][:2], '',
         '**The three trail-equality arms** (%s). The trail record (OPEN_TRAILS :%d) landed with its Defects line (:%d) and its Resolved line '
         '(:%d) reading (a)-(q), and (r) and (s) were lettered after it, so the arms reading those lines against data/b704_defects.txt '
         '((a)-(s)) fail by that order (relay data/b704_checks.txt; data/b704_checks_postpush.txt). THE CORRECTION: no repair -- the sequence '
         'rule binds from b705: no defect is lettered after the trail lands without the trail’s dry run re-read (relay data/b705_arm_sort.txt).' % (
             ', '.join(TRAIL_ARMS), s['trail'], s['defects_line'], s['resolved_line']), '',
         'The sealed face, the trail record and every root-named bank are not edited -- this entry is their correction. Nothing here proves RH '
         'or GRH.', '',
         '*Filed at b705 on the author’s ruling `(R315)`(2): generated by relay `tools/b705_corrigendum.py`, carried from '
         '`tools/b704_corrigendum.py`, in the corrigendum form of relay `tools/b678_corrigendum.py` (its reader imported unchanged), banked as '
         'relay `data/b705_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at row (25); it answers b704’s five items '
         'after its seal.*', '']
    return NL.join(L)


ROW = ('  (25) b704\'s suite after its seal (relay data/b704_checks.txt, LIVE FAILING 8): G-ACTROOT-BANKED (tools/b704_checks.py root_banked_ok,\n'
       '      requiring data/b704_read_calls.txt among the root\'s items where the root route excludes read banks by name) and G-ANSWERS-CHECKED\n'
       '      (answers_checked_ok, allowing no check after the cut\'s commit but the README figure\'s, so the root prompt\'s two checks fail it),\n'
       '      and the three trail-equality arms failing because (r) was lettered after the trail (OPEN_TRAILS :15552) landed. THE CORRECTION:\n'
       '      lettered b704\'s (r) and (s), THE SEAT\'S -- the two predicates the navigator\'s design, repaired at b705\'s carry (relay\n'
       '      data/b705_tool_repairs.txt rows (1), (2), their controls data/b705_repair_controls.txt); the trail arms no repair, the sequence rule\n'
       '      binding from b705 (data/b705_arm_sort.txt). The generated corrigendum entry stands at FINDINGS.md :%s.')


def bank_lines(s, landed_line=None):
    return ['b705 -- THE CORRIGENDUM, (R315)(2): b704`S FIVE POST-SEAL ITEMS, (r), (s) AND THE THREE TRAIL-EQUALITY ARMS, ANSWERED BY ONE GENERATED '
            'FINDINGS ENTRY IN b678`s FORM', '',
            '### rows are the corrected lines and the lines that correct them, each read from its source by line; the face, the trail and the '
            'root-named banks are not rewritten.', '',
            '  (r) THE PREDICATE        relay data/b704_defects.txt :%d-:%d | G-ACTROOT-BANKED, tools/b704_checks.py root_banked_ok | the root route tools/b698_record.py :1285-:1293 ; '
            'tools/b704_record.py :56-:58 | repaired at b705`s carry: data/b705_tool_repairs.txt row (1)' % s['r'][:2],
            '  (s) THE PREDICATE        relay data/b704_defects.txt :%d-:%d | G-ANSWERS-CHECKED, tools/b704_checks.py answers_checked_ok | repaired at b705`s carry: '
            'data/b705_tool_repairs.txt row (2)' % s['s'][:2],
            '  THE TRAIL ARMS           %s | the trail OPEN_TRAILS :%d, its Defects line :%d (%s) and Resolved line :%d against the bank (%s) | no repair; the sequence rule' % (
                ', '.join(TRAIL_ARMS), s['trail'], s['defects_line'], s['letters'], s['resolved_line'], s['bank_letters']),
            '  THE FAILING EIGHT        relay data/b704_checks.txt | %s | declared on the face %s ; found after the seal %s' % (
                ', '.join(s['fails']), ', '.join(s['declared']), ', '.join(s['post_seal'])),
            '  THE CORRIGENDA BANK     relay data/b675_corrigenda.txt, row (25) appended by this act through the Edit tool',
            '', '### ### **FIVE ITEMS ANSWERED ((r), (s), THREE TRAIL ARMS) ; THE FACE, THE TRAIL AND THE ROOT-NAMED BANKS UNEDITED ; THE ENTRY AT FINDINGS :%s.**' % (
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
    REC.land([('FINDINGS.md', TITLE, text)], 'b705_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b705_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    p = os.path.join(D, 'b705_corrigendum.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE, lettered=['r', 's'], trail_arms=list(TRAIL_ARMS),
             failing=s['fails'], declared=s['declared'], post_seal=s['post_seal'], trail=s['trail'], defects_line=s['defects_line'], row=25)
    p = os.path.join(D, 'b705_corrigendum.json')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])
    print(ROW % ln)


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b705_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
