# -*- coding: utf-8 -*-
"""b707_corrigendum.py -- THE CORRIGENDUM ENTRY OF (R317)(2): b706's items found after its seal -- (i) the retired copies placed inside the
terminal table's ledger reach (12 rows added, 15 grades moved at the final regeneration; S1 REFUTED, G-TABLE-FINAL failing), (j) the
root-bank arm's required list naming a bank the root route excludes (G-ACTROOT-BANKED), (k) fifteen rename commits named by their range in
the face's (0) (G-NOTHING-RAN-AHEAD), (l) the split parts named with letters where the rule arm admits numbered halves alone
(G-RULE-SUITE-PARTS), (m) the mirror's roster naming the 17 retired versioned paths (the export NOT CLEAN on clause 3), and the three
trail-equality arms (G-TRAIL-DEFECTS-EQUAL, G-TRAIL-RESOLVED-EQUAL, G-TRAIL-LINES-EQUAL-DEFECTS) failing because (j)-(m) were lettered after
the trail landed -- answered by one generated FINDINGS entry in b678's corrigendum form, in the bank's words; b706's sealed face (relay
data/b706_registration_2026-10-22.txt), its trail record (PLACE-papers OPEN_TRAILS :15644) and every root-named bank unedited.

### Carried from tools/b706_corrigendum.py, its rows rewritten for b706's record. b678's tool (tools/b678_corrigendum.py) is IMPORTED and
### unchanged: its reader `rd`; its form -- one generated entry, each line it corrects quoted with its place, the corrected reading and its source,
### the figures read from their banks and checked before any write, `dry` then `land`. Every figure is read, none typed:
###   (i)-(m): the rows of data/b706_defects.txt by letter and line (the repaired reader of b703, through b707_record);
###   the eleven failing arms: data/b706_checks_postpush.txt's LIVE FAILING list; the four declared on the face: the face's declaration line;
###   the trail's Defects line: PLACE-papers OPEN_TRAILS from the trail head at :15644, its letters read; the trail's own line number;
###   the repairs: data/b707_tool_repairs.txt's rows (1), (2), (3) (written before this entry).
### Routes: `dry` -> the entry printed through the screens, nothing written; `land` -> the entry appended to FINDINGS through b707_record's
### guarded landing, data/b707_corrigendum.txt (.json). The corrigenda bank's row (27) is appended by the seat through the Edit tool from the
### bank line this tool prints (ROW). Written by the Write tool at b707; it writes those two banks and the one FINDINGS entry.
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
import b707_worklist as K         # noqa: E402
import b707_record as REC         # noqa: E402  ### the guarded landing and the repaired defects reader

TITLE = ('## Corrigendum to b706’s record after its seal (relay data/b706_defects.txt, data/b706_checks_postpush.txt): the retired copies in the '
         'table’s ledger reach, the root-bank arm’s list, the rename commits named by range, the lettered split parts, the mirror’s roster and the '
         'three trail-equality arms')
TRAIL_ARMS = ('G-TRAIL-DEFECTS-EQUAL', 'G-TRAIL-RESOLVED-EQUAL', 'G-TRAIL-LINES-EQUAL-DEFECTS')
SEVEN = ('G-NOTHING-RAN-AHEAD', 'G-TABLE-FINAL', 'G-ACTROOT-BANKED', 'G-RULE-SUITE-PARTS') + TRAIL_ARMS
LETTERS = ('i', 'j', 'k', 'l', 'm')


def _row(L, letter):
    s = next((i + 1 for i, l in enumerate(L) if l.startswith('    (%s) ' % letter)), 0)
    if not s:
        return 0, 0, ''
    e = next((i for i in range(s, len(L)) if re.match(r'^    \([a-z]\) ', L[i]) or L[i].startswith('###')), len(L))
    return s, e, ' '.join(x.strip() for x in L[s - 1:e])


def compose():
    df = C78.rd(os.path.join(D, 'b706_defects.txt')).split(NL)
    rows = dict((x, _row(df, x)) for x in LETTERS)
    ck = C78.rd(os.path.join(D, 'b706_checks_postpush.txt'))
    m11 = re.search(r'LIVE FAILING : (\d+) \[(.*?)\]', ck)
    fails = [x.strip().strip("'") for x in (m11.group(2) if m11 else '').split(',') if x.strip()]
    face = C78.rd(os.path.join(ROOT, *K.B706_FACE.split('/')))
    md = re.search(r'THE ARMS FAILING THERE ON REAL STATE ARE DECLARED BEFORE THE LOCK, BY NAME:\*\* ([^.]*)\.', ' '.join(face.split()))
    declared = sorted(set(re.findall(r'`([GF]-[A-Z0-9-]+)`', md.group(1)))) if md else []
    ot = C78.rd(os.path.join(K.PP, 'OPEN_TRAILS.md')).split(NL)
    th = next((i + 1 for i, l in enumerate(ot) if l.startswith('### b706 — lane two, act one hundred and thirty-three')), 0)
    dl = next((i + 1 for i in range(th, len(ot)) if ot[i].startswith('**Defects** (relay data/b706_defects.txt)')), 0) if th else 0
    rl = next((i + 1 for i in range(th, len(ot)) if ot[i].startswith('**Resolved by the seat')), 0) if th else 0
    letters = re.findall(r'\(([a-z])\) THE (?:SEAT|NAVIGATOR)', ot[dl - 1]) if dl else []
    short = REC._defect_short('b706')
    bank_letters = [re.match(r'^\(([a-z])\)', x).group(1) for x in short]
    repairs = C78.rd(os.path.join(D, 'b707_tool_repairs.txt'))
    post_seal = [a for a in fails if a not in declared]
    ok = (all(rows[x][0] for x in LETTERS) and 'LEDGER REACH' in rows['i'][2] and 'REQUIRED LIST' in rows['j'][2] and 'RANGE' in rows['k'][2]
          and 'LETTERS' in rows['l'][2] and 'ROSTER' in rows['m'][2] and len(fails) == 11 and len(declared) == 4
          and sorted(post_seal) == sorted(SEVEN) and th == K.B706_TRAIL and dl and rl
          and letters == list('abcdefghi') and bank_letters == list('abcdefghijklm')
          and '(1) ' in repairs and 'mirror_roster' in repairs and '(2) ' in repairs and 'terminal_table' in repairs and '(3) ' in repairs and 'rule_arms' in repairs)
    if not ok:
        sys.exit('### A SOURCE LINE IS NOT AS READ (rows %s, failing %s, declared %s, trail :%s, Defects :%s letters %s, bank %s, repairs %s) -- NOTHING WRITTEN' % (
            dict((x, rows[x][0]) for x in LETTERS), fails, declared, th, dl, ''.join(letters), ''.join(bank_letters),
            ('mirror_roster' in repairs, 'terminal_table' in repairs, 'rule_arms' in repairs)))
    return dict(rows=dict((x, (rows[x][0], rows[x][1] - 1 if rows[x][1] > rows[x][0] else rows[x][0], rows[x][2])) for x in LETTERS), fails=fails,
                declared=declared, post_seal=post_seal, trail=th, defects_line=dl, resolved_line=rl, letters=''.join(letters), bank_letters=''.join(bank_letters))


def entry_text(s):
    r = s['rows']
    L = ['', TITLE, '',
         'b706’s face was locked after Components 1-4 (relay data/b706_registration_2026-10-22.txt) with four failures declared on it by name '
         '(%s); its pre-push and post-push suites found seven more, none editable in a sealed tool, and its trail record (PLACE-papers OPEN_TRAILS '
         ':%d) landed with its Defects line reading (a)-(i) before (j)-(m) were lettered. This entry answers the seven in the bank’s words, each '
         'with its cause by line; the face, the trail record and every root-named bank are not edited.' % (', '.join(s['declared']), s['trail']), '',
         '**(i) THE NAVIGATOR’S: THE RETIRED COPIES PLACED INSIDE THE TERMINAL TABLE’S LEDGER REACH** (relay data/b706_defects.txt :%d-:%d). '
         '(R316)(3) retired each pair’s unversioned copy to archive/ by git mv; tools/terminal_table.py reads PLACE-papers’ archive/ as a ledger, '
         'so the seventeen retired copies entered the table at the final regeneration: 12 rows added and 15 grades moved, every one citing a '
         'retired copy (data/b706_table_final.txt; G-TABLE-FINAL failing, S1 REFUTED). THE CORRECTION: the table’s scope bounded at b707’s carry '
         '-- the retired copies’ directory excluded by path, the table regenerated and its diff against b706’s final table printing the 12 added '
         'rows gone and the 15 moved grades restored, no other row changed (relay data/b707_tool_repairs.txt row (2), its control).' % r['i'][:2], '',
         '**(j) THE SEAT’S: THE ROOT-BANK ARM’S REQUIRED LIST NAMES A BANK THE ROOT ROUTE EXCLUDES** (relay data/b706_defects.txt :%d-:%d). '
         'G-ACTROOT-BANKED required data/b706_root_banks_dry.txt among the root’s items where the root route excludes every root_banks* bank by '
         'name, so the arm failed once a root existed. THE CORRECTION: the arm’s required list read against ROOT_EXCLUDE before the seal at b707 '
         '(no bank the route excludes required); b706’s root stands as computed, its items the route’s own list.' % r['j'][:2], '',
         '**(k) THE SEAT’S: FIFTEEN RENAME COMMITS NAMED BY THEIR RANGE AND NOT EACH BY HASH IN THE FACE’S (0)** (relay data/b706_defects.txt '
         ':%d-:%d). G-NOTHING-RAN-AHEAD reads every commit before the lock for its hash in the face; the face named “1dfd9bc..cedf7e9, seventeen '
         'commits”, so the arm failed on the fifteen between. THE CORRECTION: the fifteen are named here by hash -- d5fb24d, 6663b0b, 194e40a, '
         '8a4727f, eb26449, 6f4dfb3, b5339c4, e97faed, f915d6d, 372034c, efcd80b, 773090a, 41c4f90, 8ade57e, 374198e (the PLACE-papers log '
         '1dfd9bc..cedf7e9) -- and b707’s face names every pre-lock commit by hash.' % r['k'][:2], '',
         '**(l) THE SEAT’S: THE SPLIT PARTS NAMED WITH LETTERS WHERE THE RULE ARM ADMITS NUMBERED HALVES ALONE** (relay data/b706_defects.txt '
         ':%d-:%d). standing-b2 was split into standing-b2a and standing-b2b; G-RULE-SUITE-PARTS groups a part by stripping one trailing digit, so '
         'the lettered halves read as families of their own and b706’s run banks fail the arm at every later act. THE CORRECTION: the arm’s '
         'family reading repaired at b707’s carry under (R317)(2) -- a lettered half read as a half of the numbered half it splits -- passing on '
         'b706’s run banks and on b705’s unsplit banks alike, its NEG control a part named outside any family (relay data/b707_tool_repairs.txt '
         'row (3), its control).' % r['l'][:2], '',
         '**(m) THE NAVIGATOR’S: THE MIRROR EXPECTED CLEAN WITH ITS ROSTER NAMES AS RENAMED, WHERE THE ROSTER’S CHANGE WAS PLACED AT THE NEXT '
         'MIRROR SORT** (relay data/b706_defects.txt :%d-:%d). tools/mirror_roster.json named the 17 retired versioned paths and the face’s (W) '
         'list admitted no roster write, so b706’s export verified NOT CLEAN on clause 3 alone. THE CORRECTION: the roster rewritten at b707’s '
         'carry on the author’s word under (R317)(2) (relay data/b707_tool_repairs.txt row (1), its control the mirror’s dry run against b706’s '
         'export), the export rebuilt at b707’s mirror sort.' % r['m'][:2], '',
         '**The three trail-equality arms** (%s). The trail record (OPEN_TRAILS :%d) landed with its Defects line (:%d) and its Resolved line '
         '(:%d) reading (a)-(i), and (j)-(m) were lettered after it, so the arms reading those lines against data/b706_defects.txt ((a)-(m)) fail '
         'by that order (relay data/b706_checks_postpush.txt). THE CORRECTION: no repair -- the sequence rule of (R315)(2) binds and is read by '
         'the gate: no defect is lettered after the trail’s dry run without that dry run re-read.' % (
             ', '.join(TRAIL_ARMS), s['trail'], s['defects_line'], s['resolved_line']), '',
         'The sealed face, the trail record and every root-named bank are not edited -- this entry is their correction. Nothing here proves RH '
         'or GRH.', '',
         '*Filed at b707 on the author’s ruling `(R317)`(2): generated by relay `tools/b707_corrigendum.py`, carried from '
         '`tools/b706_corrigendum.py`, in the corrigendum form of relay `tools/b678_corrigendum.py` (its reader imported unchanged), banked as '
         'relay `data/b707_corrigendum.txt`, the corrigenda bank `data/b675_corrigenda.txt` appended at row (27); it answers b706’s seven items '
         'after its seal.*', '']
    return NL.join(L)


ROW = ('  (27) b706\'s suite after its seal (relay data/b706_checks_postpush.txt, LIVE FAILING 11, seven beyond the face): G-TABLE-FINAL on the\n'
       '      retired copies read as ledgers ((i), THE NAVIGATOR\'S; 12 rows added, 15 grades moved), G-ACTROOT-BANKED on a required bank the root\n'
       '      route excludes ((j)), G-NOTHING-RAN-AHEAD on fifteen rename commits named by range ((k)), G-RULE-SUITE-PARTS on the lettered halves\n'
       '      standing-b2a/b2b ((l)), and the three trail-equality arms failing because (j)-(m) were lettered after the trail (OPEN_TRAILS :15644)\n'
       '      landed; the mirror NOT CLEAN on clause 3 by its roster\'s 17 retired names ((m), THE NAVIGATOR\'S). THE CORRECTION: the table\'s scope,\n'
       '      the roster and the split arm repaired at b707\'s carry under (R317)(2) (relay data/b707_tool_repairs.txt rows (1)-(3), their controls\n'
       '      data/b707_repair_controls.txt); (j) and (k) answered by b707\'s own face and arm list; the trail arms no repair, the sequence rule\n'
       '      binding. The generated corrigendum entry stands at FINDINGS.md :%s.')


def bank_lines(s, landed_line=None):
    r = s['rows']
    return ['b707 -- THE CORRIGENDUM, (R317)(2): b706`S SEVEN POST-SEAL ITEMS, (i)-(m) AND THE THREE TRAIL-EQUALITY ARMS, ANSWERED BY ONE GENERATED '
            'FINDINGS ENTRY IN b678`s FORM', '',
            '### rows are the corrected lines and the lines that correct them, each read from its source by line; the face, the trail and the '
            'root-named banks are not rewritten.', '',
            '  (i) THE TABLE`S REACH     relay data/b706_defects.txt :%d-:%d | G-TABLE-FINAL, tools/terminal_table.py ledger_files over archive/ | repaired at b707`s carry: '
            'data/b707_tool_repairs.txt row (2)' % r['i'][:2],
            '  (j) THE ROOT-BANK ARM     relay data/b706_defects.txt :%d-:%d | G-ACTROOT-BANKED, tools/b706_checks.py REQUIRED_BANKS | b707`s list read against ROOT_EXCLUDE before the seal' % r['j'][:2],
            '  (k) THE RANGE             relay data/b706_defects.txt :%d-:%d | G-NOTHING-RAN-AHEAD, the face`s (0) | the fifteen named by hash in the entry' % r['k'][:2],
            '  (l) THE LETTERED HALVES   relay data/b706_defects.txt :%d-:%d | G-RULE-SUITE-PARTS, tools/rule_arms.py :551 | repaired at b707`s carry: '
            'data/b707_tool_repairs.txt row (3)' % r['l'][:2],
            '  (m) THE ROSTER            relay data/b706_defects.txt :%d-:%d | the mirror`s clause 3, tools/mirror_roster.json | repaired at b707`s carry: '
            'data/b707_tool_repairs.txt row (1)' % r['m'][:2],
            '  THE TRAIL ARMS           %s | the trail OPEN_TRAILS :%d, its Defects line :%d (%s) and Resolved line :%d against the bank (%s) | no repair; the sequence rule' % (
                ', '.join(TRAIL_ARMS), s['trail'], s['defects_line'], s['letters'], s['resolved_line'], s['bank_letters']),
            '  THE FAILING ELEVEN       relay data/b706_checks_postpush.txt | %s | declared on the face %s ; found after the seal %s' % (
                ', '.join(s['fails']), ', '.join(s['declared']), ', '.join(s['post_seal'])),
            '  THE CORRIGENDA BANK     relay data/b675_corrigenda.txt, row (27) appended by this act through the Edit tool',
            '', '### ### **SEVEN ITEMS ANSWERED ((i)-(m), THREE TRAIL ARMS) ; THE FACE, THE TRAIL AND THE ROOT-NAMED BANKS UNEDITED ; THE ENTRY AT FINDINGS :%s.**' % (
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
    REC.land([('FINDINGS.md', TITLE, text)], 'b707_corrigendum_landing.json', 'corrigendum', entry=None, dry=False)
    ln = (REC.jl('b707_corrigendum_landing.json').get('lines') or [{}])[0].get('line')
    L = bank_lines(s, ln)
    p = os.path.join(D, 'b707_corrigendum.txt')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), entry_line=ln, title=TITLE, lettered=list(LETTERS), event=None,
             trail_arms=list(TRAIL_ARMS), failing=s['fails'], declared=s['declared'], post_seal=s['post_seal'], trail=s['trail'],
             defects_line=s['defects_line'], row=27)
    p = os.path.join(D, 'b707_corrigendum.json')
    with open(p + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    print(L[-1])
    print(ROW % ln)


if __name__ == '__main__':
    r = sys.argv[1] if len(sys.argv) > 1 else ''
    if r not in ('dry', 'land'):
        print('usage: b707_corrigendum.py dry | land')
        sys.exit(2)
    main(r)
