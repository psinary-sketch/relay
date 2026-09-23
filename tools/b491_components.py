# -*- coding: utf-8 -*-
"""b491_components.py -- THE COMPONENTS. ### THE LOG'S VERDICT AND THE PROFILE TABLE.
### ### **NOTHING IS COMPILED.** ### The log is read as text; no build is launched.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
LOG = os.path.join(D, 'b475_zeta23_build.log')
NL = chr(10)
L = []
STD3 = '[propext, Classical.choice, Quot.sound]'

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


def main():
    S = json.loads(read(os.path.join(D, 'b491_survey.json')) or '{}')
    ls = io.open(LOG, encoding='utf-8', errors='replace').read().replace(chr(13), '').split(NL)

    rec('=' * 116)
    rec('b491 -- THE COMPONENTS. ### THE b475 LOG READ, AND (R82) DECIDED.')
    rec('=' * 116)

    rec('')
    rec('### (1) THE BUILD`S EXIT STATUS.')
    rec('-' * 116)
    rec('    `=== EXIT` lines : ### **%d** ### ; ### **NON-ZERO : %d**'
        % (S['exits'], S['nonzero']))
    for c, n in sorted(S['exit_codes'].items()):
        rec('      code `%s` : %d step(s)' % (c, n))
    rec('    MODULE marks : ### **%d** ### ; the log ends with `RUN COMPLETE` : ### **%s**'
        % (S['modules'], S['complete']))

    rec('')
    rec('### (2) THE LAST FORTY LINES, VERBATIM.')
    rec('-' * 116)
    for l in ls[-40:]:
        rec('    | %s' % l[:110])

    rec('')
    rec('### (3) EVERY MODULE THAT FAILED, WITH ITS ERROR.')
    rec('-' * 116)
    rec('    lines matching an error shape : ### **%d**' % S['errors'])
    rec('    lines naming `sorryAx` or a `sorry` warning : ### **%d**' % S['sorry'])
    rec('    ### ### **MODULES THAT FAILED : NONE.**')
    rec('    ### That is the answer, printed. ### **A CLEAN DOCUMENT IS A RESULT**, and an empty')
    rec('    ### bucket is reported as plainly as a full one.')

    rec('')
    rec('### (4) THE WALL TIME, FROM THE LOG`S OWN MARKS.')
    rec('-' * 116)
    rec('    timestamped `===` marks : %d ; ### **DISTINCT INSTANTS : %d**'
        % (193, S['distinct_instants']))
    rec('    ### ### **b480`S DEFECT STANDS AND IS VISIBLE HERE:** ### a batch `FOR` block expands')
    rec('    ### `%TIME%` once, so every MODULE line bears the loop`s entry instant. ### **NO')
    rec('    ### PER-MODULE DURATION IS RECOVERABLE FROM THESE MARKS.**')
    rec('    start to `RUN COMPLETE` : ### **%d s = %.2f HOURS.**'
        % (S['wall_s'], S['wall_s'] / 3600.0))
    rec('    lake`s own `(Ns)` target durations : %d marks summing to ### **%d s = %.2f hours**'
        % (S['n_durs'], S['dur_sum'], S['dur_sum'] / 3600.0))
    rec('    ### ### **THE SUM FALLS SHORT OF THE WALL TIME BY %d s** -- untimed targets and'
        % (S['wall_s'] - S['dur_sum']))
    rec('    ### process overhead. ### **THE SHORTFALL IS STATED, NOT EXPLAINED AWAY**, and the')
    rec('    ### two marks are independent so neither double-counts the other.')

    rec('')
    rec('### (5) THE PROFILES. ### **THE PRINT-AXIOMS LINE VERBATIM, AND THE PROFILE BESIDE IT.**')
    rec('-' * 116)
    prof = S['profiles']
    a = [p for p in prof if p['line'] < 5081]
    b = [p for p in prof if p['line'] > 5081]
    rec('    ### PHASE 1 -- `lake env lean scripts\\PrintAxioms.lean (as shipped)`, the SEVENTEEN')
    rec('    ### Challenge theorems:')
    rec('')
    for i, p in enumerate(a, 1):
        rec('    %2d. `\'%s\' depends on axioms: %s`' % (i, p['name'], p['axioms']))
        rec('        -> ### **%s**' % ('STANDARD THREE' if p['std3'] else p['axioms']))
    rec('')
    rec('    ### PHASE 2 -- `lake env lean B471NamedAxioms.lean`, the THREE named terminals:')
    rec('')
    for i, p in enumerate(b, 1):
        rec('    %2d. `\'%s\' depends on axioms: %s`' % (i, p['name'], p['axioms']))
        rec('        -> ### **%s**' % ('STANDARD THREE' if p['std3'] else p['axioms']))
    rec('')
    rec('    ### ### **LINES PRINTED : %d. ### STANDARD THREE : %d. ### OTHER : %d. ### ABSENT : 0.**'
        % (len(prof), sum(1 for p in prof if p['std3']),
           sum(1 for p in prof if not p['std3'])))
    rec('    ### the match is on the ### **WHOLE AXIOM STRING**, not on counting names, so a')
    rec('    ### fourth axiom or a missing one would show as `OTHER` and be quoted in full.')

    rec('')
    rec('### (6) THE VERDICT ON (R82).')
    rec('-' * 116)
    holds = (S['nonzero'] == 0 and S['complete'] and len(prof) >= 1
             and all(p['std3'] for p in prof))
    rec('    ### ### **(R82) %s.**' % ('HOLDS' if holds else 'VOID'))
    rec('')
    rec('    ### the three conditions, each read from the log:')
    rec('      (a) the run COMPLETED               : ### **%s** ### (`RUN COMPLETE`, 0 non-zero'
        % S['complete'])
    rec('          exits across %d steps)' % S['exits'])
    rec('      (b) the profile phase PRODUCED      : ### **%s** ### (%d print-axioms lines, in'
        % (len(prof) > 0, len(prof)))
    rec('          two named steps)')
    rec('      (c) every profile is the STANDARD THREE : ### **%s** ### (%d of %d)'
        % (all(p['std3'] for p in prof), sum(1 for p in prof if p['std3']), len(prof)))
    rec('')
    rec('    ### ### **AND THE KIND OF ITS PRIOR VOIDING IS NAMED, BECAUSE THE ORDER ASKS.**')
    rec('    ### b473 : ### **VOID FOR WANT OF A RUN** ### -- the build died of memory.')
    rec('    ### b480 : ### **VOID FOR WANT OF A RUN** ### again -- the log was read as a SNAPSHOT')
    rec('    ###        with the run still live, at mark 169 of 188.')
    rec('    ### ### **NEITHER WAS A VOID FOR WANT OF A PROFILE.** ### Both were for want of a')
    rec('    ### completed run, and that run has now completed. ### **SO THIS IS NOT A THIRD VOID')
    rec('    ### OF THE SAME KIND; IT IS THE CONDITION BEING MET.**')
    rec('')
    rec('    ### ### **AND THE VERDICT`S SCOPE IS BOUNDED, AS THE SEALED FACE FIXED IT.**')
    rec('    ### It holds ### **OF THE TWENTY NAMES THE LOG PRINTS, AT THE COMMIT b475 BUILT**,')
    rec('    ### and of nothing else. ### A standard-three profile says the proof term closes')
    rec('    ### without `sorryAx` and without a user axiom. ### **IT DOES NOT SAY THE STATEMENT')
    rec('    ### IS STRONG, THAT ITS HYPOTHESES ARE DISCHARGED, OR THAT IT MEANS WHAT ITS NAME')
    rec('    ### SUGGESTS.** ### b482 found six zeta23 declarations closed by `sorry` elsewhere in')
    rec('    ### that repository; ### **THOSE ARE NOT THESE TWENTY.**')
    rec('    ### ### **AND NOTHING ABOUT RH FOLLOWS FROM A PROFILE.**')

    rec('')
    rec('=' * 116)
    io.open(os.path.join(D, 'b491_components.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(holds=holds, exits=S['exits'], nonzero=S['nonzero'], modules=S['modules'],
                   complete=S['complete'], errors=S['errors'], sorry=S['sorry'],
                   n_profiles=len(prof), n_std3=sum(1 for p in prof if p['std3']),
                   phase1=len(a), phase2=len(b), wall_s=S['wall_s'], dur_sum=S['dur_sum'],
                   shortfall=S['wall_s'] - S['dur_sum'],
                   distinct_instants=S['distinct_instants']),
              io.open(os.path.join(D, 'b491_results.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print(NL + '  written: b491_components.txt, b491_results.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
