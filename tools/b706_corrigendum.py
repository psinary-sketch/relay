# -*- coding: utf-8 -*-
"""b706_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R316)(2): b705's six post-seal items -- G-WRITELIST-KINDS on data/b706_rules.txt (a rules
file ordered mid-act after the (W) list was sealed, an event in b705's bank), (n) G-ANSWERS-CHECKED's checker reading a sha256 prefix as a
commit, (o) G-ENTRY-TITLE-FORM's needle in lower case against the entry's "The", and the three trail-equality arms (G-TRAIL-DEFECTS-EQUAL,
G-TRAIL-RESOLVED-EQUAL, G-TRAIL-LINES-EQUAL-DEFECTS) failing because (o) was lettered after the trail landed -- answered by one generated
FINDINGS entry in b678's corrigendum form, in the bank's words; b705's sealed face (relay data/b705_registration_2026-10-22.txt), its trail
record (PLACE-papers OPEN_TRAILS :15592) and every root-named bank unedited.

### Carried from tools/b705_corrigendum.py, its rows rewritten for b705's record. b678's tool (tools/b678_corrigendum.py) is IMPORTED and
### unchanged: its reader `rd`; its form -- one generated entry, each line it corrects quoted with its place, the corrected reading and its source,
### the figures read from their banks and checked before any write, `dry` then `land`. Every figure is read, none typed:
###   (n), (o): the rows of data/b705_defects.txt by letter and line (the repaired reader of b703, through b706_record); the event: its line;
###   the ten failing arms: data/b705_checks_postpush.txt's LIVE FAILING list; the four declared on the face: the face's declaration line;
###   the trail's Defects line: PLACE-papers OPEN_TRAILS from the trail head at :15592, its letters read; the trail's own line number;
###   the repairs: data/b706_tool_repairs.txt's rows (1), (2), (3) and data/b706_arm_sort.txt (both written before this entry).
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b706_record's
### guarded landing, data/b706_corrigendum.txt (.json). The corrigenda bank's row (26) is appended by the seat through the Edit tool from the
### bank line this tool prints (ROW). Written by the Write tool at b706; it writes those two banks and the one FINDINGS entry.
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
import b706_worklist as K         # noqa: E402
import b706_record as REC         # noqa: E402  ### the guarded landing and the repaired defects reader

TITLE = ('## Corrigendum to b705’s record after its seal (relay data/b705_defects.txt, data/b705_checks_postpush.txt): the write-list arm on a '
         'rules file ordered mid-act, the answer checker, the title needle and the three trail-equality arms')
TRAIL_ARMS = ('G-TRAIL-DEFECTS-EQUAL', 'G-TRAIL-RESOLVED-EQUAL', 'G-TRAIL-LINES-EQUAL-DEFECTS')
SIX = ('G-WRITELIST-KINDS', 'G-ANSWERS-CHECKED', 'G-ENTRY-TITLE-FORM') + TRAIL_ARMS


def _row(L, letter):
    s = next((i + 1 for i, l in enumerate(L) if l.startswith('    (%s) ' % letter)), 0)
    if not s:
        return 0, 0, ''
    e = next((i for i in range(s, len(L)) if re.match(r'^    \([a-z]\) ', L[i]) or L[i].startswith('###')), len(L))
    return s, e, ' '.join(x.strip() for x in L[s - 1:e])


def compose():
    df = C78.rd(os.path.join(D, 'b705_defects.txt')).split(NL)
    sn, en, tn = _row(df, 'n')
    so, eo, to = _row(df, 'o')
    ev = next((i + 1 for i, l in enumerate(df) if l.strip().startswith('G-WRITELIST-KINDS fails after the seal, pre-push and post-push, on relay/data/b706_rules.txt alone')), 0)
    ck = C78.rd(os.path.join(D, 'b705_checks_postpush.txt'))
    m10 = re.search(r'LIVE FAILING : (\d+) \[(.*?)\]', ck)
    fails = [x.strip().strip("'") for x in (m10.group(2) if m10 else '').split(',') if x.strip()]
    face = C78.rd(os.path.join(ROOT, *K.B705_FACE.split('/')))
    md = re.search(r'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME:\*\* ([^.]*)\.', ' '.join(face.split()))
    declared = sorted(set(re.findall(r'`([GF]-[A-Z0-9-]+)`', md.group(1)))) if md else []
    ot = C78.rd(os.path.join(K.PP, 'OPEN_TRAILS.md')).split(NL)
    th = next((i + 1 for i, l in enumerate(ot) if l.startswith('### b705 — lane two, act one hundred and thirty-two')), 0)
    dl = next((i + 1 for i in range(th, len(ot)) if ot[i].startswith('**Defects** (relay data/b705_defects.txt)')), 0) if th else 0
    rl = next((i + 1 for i in range(th, len(ot)) if ot[i].startswith('**Resolved by the seat')), 0) if th else 0
    letters = re.findall(r'\(([a-z])\) THE (?:SEAT|NAVIGATOR)', ot[dl - 1]) if dl else []
    short = REC._defect_short('b705')
    bank_letters = [re.match(r'^\(([a-z])\)', x).group(1) for x in short]
    arm_sort = C78.rd(os.path.join(D, 'b706_arm_sort.txt'))
    repairs = C78.rd(os.path.join(D, 'b706_tool_repairs.txt'))
    post_seal = [a for a in fails if a not in declared]
    ok = (sn and so and ev and 'sha256' in tn.lower() and 'lower case' in to.lower() and len(fails) == 10 and len(declared) == 4
          and sorted(post_seal) == sorted(SIX) and th == K.B705_TRAIL and dl and rl
          and letters == list('abcdefghijklmn') and bank_letters == list('abcdefghijklmno') and 'G-WRITELIST-KINDS' in arm_sort
          and '(1) ' in repairs and 'G-WRITELIST-KINDS' in repairs and '(2) ' in repairs and 'G-ANSWERS-CHECKED' in repairs
          and '(3) ' in repairs and 'G-ENTRY-TITLE-FORM' in repairs)
    if not ok:
        sys.exit('### A SOURCE LINE IS NOT AS READ ((n) :%s, (o) :%s, the event :%s, failing %s, declared %s, trail :%s, Defects :%s letters %s, bank %s, '
                 'sort %s, repairs %s) -- NOTHING WRITTEN' % (sn, so, ev, fails, declared, th, dl, ''.join(letters), ''.join(bank_letters),
                                                              'G-WRITELIST-KINDS' in arm_sort, 'G-WRITELIST-KINDS' in repairs))
    return dict(n=(sn, en - 1 if en > sn else sn, tn), o=(so, eo - 1 if eo > so else so, to), event=ev, fails=fails, declared=declared, post_seal=post_seal,
                trail=th, defects_line=dl, resolved_line=rl, letters=''.join(letters), bank_letters=''.join(bank_letters))


def entry_text(s):
    L = ['', TITLE, '',
         'b705’s face was locked after Components 1-4 (relay data/b705_registration_2026-10-22.txt) with four failures declared on it by name '
         '(%s); its pre-push and post-push suites found six more, none editable in a sealed tool, and its trail record (PLACE-papers OPEN_TRAILS '
         ':%d) landed before the last defect was lettered. This entry answers the six in the bank’s words, each with its cause by line; the '
         'face, the trail record and every root-named bank are not edited.' % (', '.join(s['declared']), s['trail']), '',
         '**G-WRITELIST-KINDS on relay data/b706_rules.txt** (relay data/b705_defects.txt :%d, an event, unlettered). The bank was written on '
         'the author’s word at the root’s second call, after the face’s (W) list was sealed naming relay/data/b705_* and no b706_ file; the '
         'write as ordered, the arm correct on the sealed list. THE CORRECTION: the navigator’s, a rules file ordered mid-act after the (W) '
         'list was sealed -- repaired at b706’s carry by a (W) list that admits the next act’s rules file by form, `relay/data/b707_rules.txt` '
         '(relay data/b706_tool_repairs.txt row (1), its control data/b706_repair_controls.txt).' % s['event'], '',
         '**(n) THE SEAT’S: THE CITATION TOOL READ THE PDF’S SHA256 PREFIX AS A COMMIT** (relay data/b705_defects.txt :%d-:%d). The root '
         'prompt’s second answer named the fetched source’s sha256 as “b8e0b54a…” (data/b705_source_cc_2006_13771.txt :2); the answer route, '
         'b682’s, read the eight hex characters as a commit and printed a MISS beside the later act’s bank, so G-ANSWERS-CHECKED read the check '
         'as not all later-act banks and failed after the seal. THE CORRECTION: the checker repaired at b706’s carry to tell a root prefix or a '
         'file hash from a commit by its bank’s row -- a token a bank names as a sha256 is checked against that row and masked from the commit '
         'reading (relay data/b706_tool_repairs.txt row (2); data/b706_repair_controls.txt).' % s['n'][:2], '',
         '**(o) THE SEAT’S: THE TITLE ARM’S NEEDLE WRITTEN IN LOWER CASE AGAINST THE ENTRY’S CAPITALISED FIRST WORD** (relay '
         'data/b705_defects.txt :%d-:%d). G-ENTRY-TITLE-FORM required ‘the faces joined by closure at SIDE-faces-join’ in a title that opens '
         '“## The faces joined by closure …”; the landed title equals the record tool’s, and the arm failed on its own needle after the seal. '
         'THE CORRECTION: the predicate repaired at b706’s carry to compare after case-folding the article alone (relay '
         'data/b706_tool_repairs.txt row (3); data/b706_repair_controls.txt).' % s['o'][:2], '',
         '**The three trail-equality arms** (%s). The trail record (OPEN_TRAILS :%d) landed with its Defects line (:%d) and its Resolved line '
         '(:%d) reading (a)-(n), and (o) was lettered after it, so the arms reading those lines against data/b705_defects.txt ((a)-(o)) fail '
         'by that order (relay data/b705_checks_postpush.txt). THE CORRECTION: no repair -- the sequence rule of (R315)(2) binds and is read by '
         'the gate: no defect is lettered after the trail’s dry run without that dry run re-read (relay data/b706_arm_sort.txt).' % (
             ', '.join(TRAIL_ARMS), s['trail'], s['defects_line'], s['resolved_line']), '',
         'The sealed face, the trail record and every root-named bank are not edited -- this entry is their correction. Nothing here proves RH '
         'or GRH.', '',
         '*Filed at b706 on the author’s ruling `(R316)`(2): generated by relay `tools/b706_corrigendum.py`, carried from '
         '`tools/b705_corrigendum.py`, in the corrigendum form of relay `tools/b678_corrigendum.py` (its reader imported unchanged), banked as '
         'relay `data/b706_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at row (26); it answers b705’s six items '
         'after its seal.*', '']
    return NL.join(L)


ROW = ('  (26) b705\'s suite after its seal (relay data/b705_checks_postpush.txt, LIVE FAILING 10, six beyond the face): G-WRITELIST-KINDS on\n'
       '      relay/data/b706_rules.txt (a rules file written on the author\'s word after the (W) list was sealed; an event, unlettered),\n'
       '      G-ANSWERS-CHECKED (the answer route reading the PDF\'s sha256 prefix "b8e0b54a" as a commit, (n)), G-ENTRY-TITLE-FORM (its needle\n'
       '      in lower case against the entry\'s "The", (o)), and the three trail-equality arms failing because (o) was lettered after the trail\n'
       '      (OPEN_TRAILS :15592) landed. THE CORRECTION: the write-list arm the navigator\'s, repaired at b706\'s carry by a (W) list admitting\n'
       '      the next act\'s rules file by form; (n) and (o) THE SEAT\'S, the checker and the predicate repaired at b706\'s carry (relay\n'
       '      data/b706_tool_repairs.txt rows (1)-(3), their controls data/b706_repair_controls.txt); the trail arms no repair, the sequence rule\n'
       '      binding (data/b706_arm_sort.txt). The generated corrigendum entry stands at FINDINGS.md :%s.')


def bank_lines(s, landed_line=None):
    return ['b706 -- THE CORRIGENDUM, (R316)(2): b705`S SIX POST-SEAL ITEMS, THE WRITE-LIST EVENT, (n), (o) AND THE THREE TRAIL-EQUALITY ARMS, ANSWERED '
            'BY ONE GENERATED FINDINGS ENTRY IN b678`s FORM', '',
            '### rows are the corrected lines and the lines that correct them, each read from its source by line; the face, the trail and the '
            'root-named banks are not rewritten.', '',
            '  THE EVENT                relay data/b705_defects.txt :%d | G-WRITELIST-KINDS on relay/data/b706_rules.txt, the (W) list sealed before the word | repaired at '
            'b706`s carry: data/b706_tool_repairs.txt row (1), the (W) list admitting data/b707_rules.txt by form' % s['event'],
            '  (n) THE CHECKER          relay data/b705_defects.txt :%d-:%d | G-ANSWERS-CHECKED, tools/b705_citation.py answer (b682`s route) | repaired at b706`s carry: '
            'data/b706_tool_repairs.txt row (2)' % s['n'][:2],
            '  (o) THE PREDICATE        relay data/b705_defects.txt :%d-:%d | G-ENTRY-TITLE-FORM, tools/b705_checks.py entry_title_ok | repaired at b706`s carry: '
            'data/b706_tool_repairs.txt row (3)' % s['o'][:2],
            '  THE TRAIL ARMS           %s | the trail OPEN_TRAILS :%d, its Defects line :%d (%s) and Resolved line :%d against the bank (%s) | no repair; the sequence rule' % (
                ', '.join(TRAIL_ARMS), s['trail'], s['defects_line'], s['letters'], s['resolved_line'], s['bank_letters']),
            '  THE FAILING TEN          relay data/b705_checks_postpush.txt | %s | declared on the face %s ; found after the seal %s' % (
                ', '.join(s['fails']), ', '.join(s['declared']), ', '.join(s['post_seal'])),
            '  THE CORRIGENDA BANK     relay data/b675_corrigenda.txt, row (26) appended by this act through the Edit tool',
            '', '### ### **SIX ITEMS ANSWERED (THE EVENT, (n), (o), THREE TRAIL ARMS) ; THE FACE, THE TRAIL AND THE ROOT-NAMED BANKS UNEDITED ; THE ENTRY AT FINDINGS :%s.**' % (
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
    REC.land([('FINDINGS.md', TITLE, text)], 'b706_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b706_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    p = os.path.join(D, 'b706_corrigendum.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE, lettered=['n', 'o'], event='G-WRITELIST-KINDS',
             trail_arms=list(TRAIL_ARMS), failing=s['fails'], declared=s['declared'], post_seal=s['post_seal'], trail=s['trail'],
             defects_line=s['defects_line'], row=26)
    p = os.path.join(D, 'b706_corrigendum.json')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])
    print(ROW % ln)


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b706_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
