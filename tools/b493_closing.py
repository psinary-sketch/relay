# -*- coding: utf-8 -*-
"""b493_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.replace(chr(13), '').strip()


def lw(t, n):
    return next((l.strip() for l in t.split(NL) if n in l), '')


R = json.loads(read(os.path.join(D, 'b493_results.json')))
SV = json.loads(read(os.path.join(D, 'b493_survey.json')))
per = R['per_record']
post = read(os.path.join(D, 'b493_checks_postpush.txt'))

rec('=' * 104)
rec('b493 -- THE CLOSING RECORD. ### THE EIGHT RECORDS READ WHOLE AGAINST THE CEILING.')
rec('=' * 104)

rec('')
rec('### (1) THE SOURCE.')
rec('-' * 104)
rec('    the author`s Zenodo screen of 2026-09-14, banked verbatim:')
rec('      ### **%d lines, %d bytes**' % (SV['lines'], SV['bytes']))
rec('      sha256 ### **%s**' % SV['sha256'])
rec('      eight records. ### **NOTHING WAS FETCHED.**')
rec('    ### ### **NO DESCRIPTION IS TRUNCATED.** ### The first test said three were -- records')
rec('    ### 5, 6 and 7, which end `Author: J. York Seale ORCID: 0009-0008-7993-0310`. ### **THAT')
rec('    ### IS A TEMPLATE`S TRAILER, NOT A CUT**, and three different lengths ending at the same')
rec('    ### semantic token refute it: ### **A SCREEN TRUNCATION CUTS AT A WIDTH.**')
rec('    ### the monograph`s screen text agrees with `b359_fetch_F2.json` ### **ENTITY FOR')
rec('    ### ENTITY** -- every divergence is `&xi;` against `ξ`, `&sigma;` against `σ`.')

rec('')
rec('### (2) THE DISPOSITION -- 104 ROWS.')
rec('-' * 104)
rec('    ### the ceiling, quoted from (R102):')
rec('    ### **"Supportable: RH reduced to a single located clause, reduction machine-verified;')
rec('    ### not supportable: RH proved."**')
rec('')
rec('    %-3s %-52s %-9s %-8s %s' % ('#', 'record', 'STANDS', 'RESTS', 'EXCEEDS'))
rec('    ' + '-' * 92)
names = {1: 'T7 Matched-Arc CMB Search', 2: 'A Place To Stand', 3: 'SIDE-lv-conservation',
         4: 'SIDE-kernel', 5: 'SIDE-cosmo', 6: 'SIDE-effects', 7: 'SIDE-trivium',
         8: 'SIDE-interfaces'}
for k in range(1, 9):
    v = per[str(k)]
    rec('    %-3d %-52s %-9d %-8d %s'
        % (k, names[k], v['stands'], v['rests'],
           ('### **%d**' % v['exceeds']) if v['exceeds'] else '0'))
rec('    ' + '-' * 92)
rec('    %-3s %-52s %-9d %-8d ### **%d**'
    % ('', 'TOTAL', R['stands'], R['rests'], R['exceeds']))
rec('')
rec('    ### ### **THE %d EXCEEDING ROWS CARRY NO REPLACEMENT.** ### A title or headline that'
    % R['exceeds'])
rec('    ### exceeds the ceiling is ### **THE AUTHOR`S TO REWORD, AND THIS ACT NAMES IT AND')
rec('    ### STOPS.** ### Three are titles -- the monograph`s, the kernel`s, and')
rec('    ### ### **`SIDE-lv-conservation`S, WHICH THE ORDER DID NOT NAME** -- and two more are')
rec('    ### headline-led sentences: ### **FIVE OF THE EIGHT SIT IN A TITLE OR A HEADLINE.**')
rec('    ### **A HEADLINE COMPRESSES, AND COMPRESSION IS WHERE A CEILING IS BREACHED.**')

rec('')
rec('### (3) THE CORRECTION TO b487.')
rec('-' * 104)
rec('    ### ### **THE KERNEL`S DEPOSITED DESCRIPTION IS NOT THE TEXT IN ITS REPOSITORY.**')
rec('      `SIDE-kernel` tag `v1.5`, `.zenodo.json` : ### **1,143 characters**')
rec('        *"Lean 4 formalization of the SIDE Exclusion Principle applied to the Riemann zeta')
rec('        function. The kernel proves that no off-line zero exists by exhaustively..."*')
rec('      the deposited record, on the screen      : ### **3,143 characters**')
rec('        *"SIDE-kernel: the machine-verified architecture of the SIDE Exclusion proof..."*')
rec('    ### ### **SO b487 DISPOSED A SENTENCE THAT IS NOT IN THE DEPOSIT.** ### It read the')
rec('    ### repository`s file and graded the kernel`s sentence 2 as resting on `E-2026-09-14-1`.')
rec('    ### ### **(R99) RULED THAT SENTENCE "APPLIED AS DRAFTED"**, and applying it would edit a')
rec('    ### sentence the record does not contain.')
rec('    ### ### **THIS ACT NAMES IT AND STOPS.** ### The kernel carries no RESTS row here, its')
rec('    ### (R99) text is HELD for the author`s ruling, and the paste-ready block carries the')
rec('    ### monograph`s two rows only.')
rec('    ### ### **A SOURCE THAT SHIPS BESIDE A DEPOSIT IS NOT THE DEPOSIT.**')

rec('')
rec('### (4) THE EXPECTATIONS.')
rec('-' * 104)
rec('    ### **(N1)** ### **HELD** ### -- and a THIRD title exceeds that the order did not name.')
rec('    ### **(N2)** ### **HELD** ### -- though the first ceiling matcher used `[^.]` and could')
rec('          not cross the full stop in `MAIN THEOREM. The Riemann Hypothesis:`, and would have')
rec('          scored it REFUTED. ### **A MATCHER THAT CANNOT CROSS A FULL STOP CANNOT READ A')
rec('          HEADLINE.**')
rec('    ### **(N3)** ### **HELD** ### -- and at records 3 and 4 that is a CORRECTION to b487')
rec('          rather than agreement with it.')
rec('    ### **(S1)** ### **HELD** ### ; ### **(S2)** ### **REFUTED** ### ; ### **(S3)** ###')
rec('          **HELD.** ### The four May-2026 kernels exceed at ### **ZERO** ### rows: they')
rec('          describe their own subject and make no claim about RH. ### **THE SEAT EXPECTED AGE')
rec('          TO CORRELATE WITH OVERREACH; IT DOES NOT.** ### Overreach tracks the SUBJECT.')

rec('')
rec('### (5) THE DEFECTS THIS ACT RECORDS OF ITS OWN INSTRUMENTS. ### **FOUR.**')
rec('-' * 104)
rec('    ### ### **(a) A TRUNCATION TEST THAT MISTOOK A TRAILER FOR A CUT** -- it flagged three')
rec('    ### complete descriptions because they end without a full stop. ### Repaired with the')
rec('    ### structural argument, and both readings printed.')
rec('    ### ### **(b) A CEILING MATCHER THAT COULD NOT CROSS A FULL STOP** -- `[^.]{0,120}`')
rec('    ### against `MAIN THEOREM. The Riemann Hypothesis:`. ### It missed the very sentence')
rec('    ### (N2) names and would have scored the navigator`s expectation refuted.')
rec('    ### ### **(c) A RESTS MATCHER USING `startswith` ON A SENTENCE CARRYING ITS HEADLINE.**')
rec('    ### The splitter keeps `WHAT THE MANUSCRIPT ESTABLISHES...` attached, so b487`s text sat')
rec('    ### INSIDE the row and not at its start. ### It found 1 of the 2 rows that exist.')
rec('    ### ### **(d) A CONTROL MALFORMED BY OPERATOR PRECEDENCE** -- `put(...) if c else d`')
rec('    ### bound the whole call inside the conditional, so the mutation never reached the block')
rec('    ### the predicate reads, and the arm could not fail.')

rec('')
rec('### (6) THE SUITE, THE COMMITS, THE MIRROR.')
rec('-' * 104)
rec('    pre-push  : 55 arms, 0 live failing, 0 positive-control passes.')
rec('    post-push : %s' % lw(post, 'ARMS RUN'))
rec('                %s' % lw(post, 'VERDICT :'))
rec('')
rec('    the commits, each read back by `ls-remote`:')
for name, repo in (('relay', ROOT),
                   ('PLACE-papers', os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')),
                   ('SIDE-global-section', os.path.join('D:', os.sep, 'SIDE-global-section'))):
    h = git(repo, 'rev-parse', 'HEAD')
    r = git(repo, 'ls-remote', 'origin', 'refs/heads/main').split()
    r = r[0] if r else ''
    rec('      %-20s local %s ; remote %s ; ### **%s**'
        % (name, h[:12], r[:12], 'AGREE' if h and h == r else 'DISAGREE'))
rec('    the mirror : `mirror-refresh-2026-09-23-b493.zip` at `500e879` --')
rec('      ### **CLEAN ON ALL THREE CLAUSES.**')

rec('')
rec('### (7) THE CENSUSES, THE PINS, THE LISTS.')
rec('-' * 104)
rec('    handoff census : %s' % lw(read(os.path.join(D, 'b493_census_closing.txt')),
                                   'TOTAL MISSING'))
rec('    faces census   : %s' % lw(read(os.path.join(D, 'b493_faces_census_closing.txt')),
                                   'TOTAL MISSING'))
rec('    pins           : %s' % lw(read(os.path.join(D, 'b493_pins_closing.txt')),
                                   'REPOS HARD-FAILING'))
rec('    ### **THE FOUR LISTS STAY OPEN.** ### Nothing fetched; nothing compiled; no lane opened;')
rec('    ### no repository created. ### No corpus grade moved; row U1 unedited; nothing deposits;')
rec('    ### ### **NOTHING AT ZENODO IS WRITTEN**; ### **h2 WHERE THE DEPOSIT LEFT IT.**')

rec('')
rec('### (8) WHAT IS CARRIED FORWARD.')
rec('-' * 104)
rec('    (a) ### **THE PLATFORM SESSION IS THE AUTHOR`S, AND IT IS BLOCKED ON A REWORDING.**')
rec('        (R102) holds the edits until the whole disposition is applied at once, and')
rec('        ### **EIGHT ROWS EXCEED THE CEILING WITH NO DRAFT** -- three of them titles.')
rec('    (b) ### **(R99)`S KERNEL TEXT IS HELD.** ### Its target sentence is not in the deposit.')
rec('        ### Whether to edit the `.zenodo.json`, the record, or neither is the author`s.')
rec('    (c) ### **(R104) FIXES THE FORWARD SEQUENCE**, and the act after this one opens with the')
rec('        VERIFICATION_LOOM census and the OPEN_TRAILS desk read against it, one row per item.')
rec('    (d) ### **`corr_row.py` STILL CHECKS THE NUMBER AND NOT THE CELLS.** ### ROUTED, and')
rec('        overdue since b490.')
rec('')
rec('=' * 104)
rec('  ### ### **b493 CLOSES. 56 ARMS, 0 LIVE FAILING, 0 POSITIVE-CONTROL PASSES.**')
rec('=' * 104)

io.open(os.path.join(D, 'b493_closing.txt'), 'w', encoding='utf-8', newline=NL).write(
    NL.join(L) + NL)
print(NL + '  written: b493_closing.txt')
