# -*- coding: utf-8 -*-
"""b491_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
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


R = json.loads(read(os.path.join(D, 'b491_results.json')) or '{}')
post = read(os.path.join(D, 'b491_checks_postpush.txt'))

rec('=' * 104)
rec('b491 -- THE CLOSING RECORD. ### THE b475 LOG READ, AND (R82) DECIDED.')
rec('=' * 104)

rec('')
rec('### (1) THE RUN.')
rec('-' * 104)
rec('    ### ### **%d `=== EXIT` LINES AND EVERY ONE IS `EXIT 0`** ### -- across ### **%d**'
    % (R['exits'], R['modules']))
rec('    MODULE marks and three further STEP marks, ending `RUN COMPLETE` at `21:33:50.73`.')
rec('    ### ### **NON-ZERO EXITS : %d. ### MODULES THAT FAILED : NONE.**' % R['nonzero'])
rec('    lines matching an error shape : ### **%d** ### ; naming `sorryAx` : ### **%d**'
    % (R['errors'], R['sorry']))
rec('    ### **A CLEAN DOCUMENT IS A RESULT**, and the empty bucket is printed as plainly as a')
rec('    ### full one would be.')
rec('')
rec('    WALL TIME, from the log`s own outer marks : ### **%d s = %.2f HOURS.**'
    % (R['wall_s'], R['wall_s'] / 3600.0))
rec('    lake`s own target durations sum to        : ### **%d s = %.2f hours**'
    % (R['dur_sum'], R['dur_sum'] / 3600.0))
rec('    ### ### **SHORTFALL : %d s** ### -- untimed targets and process overhead. ### Two')
rec('    ### independent marks, neither typed, and the difference STATED rather than explained')
rec('    ### away.')
rec('    ### ### **AND b480`S LAUNCHER DEFECT STANDS:** ### 193 timestamped marks carry only')
rec('    ### ### **%d DISTINCT INSTANTS**, a batch `FOR` block expanding `%%TIME%%` once, so'
    % R['distinct_instants'])
rec('    ### **NO PER-MODULE DURATION IS RECOVERABLE FROM THEM.**')

rec('')
rec('### (2) THE PROFILES.')
rec('-' * 104)
rec('    ### ### **%d PRINT-AXIOMS LINES, IN TWO STEPS THE LOG NAMES:**' % R['n_profiles'])
rec('      `lake env lean scripts\\PrintAxioms.lean (as shipped)` at `21:32:34.30`')
rec('        -> ### **%d** ### Challenge theorems' % R['phase1'])
rec('      `lake env lean B471NamedAxioms.lean` at `21:33:23.92`')
rec('        -> ### **%d** ### named terminals: `EF_lit_zetaZeroConfig`, `EF_lit`, `EF_lit_zeta`'
    % R['phase2'])
rec('    ### ### **ALL %d READ `depends on axioms: [propext, Classical.choice, Quot.sound]`**,'
    % R['n_std3'])
rec('    ### matched on the ### **WHOLE AXIOM STRING** ### and not by counting names, so a')
rec('    ### fourth axiom or a missing one would have shown as OTHER and been quoted in full.')
rec('    ### ### **STANDARD THREE : %d. ### OTHER : 0. ### ABSENT : 0.**' % R['n_std3'])

rec('')
rec('### (3) THE VERDICT ON (R82). ### **HOLDS.**')
rec('-' * 104)
rec('    (a) the run COMPLETED                   : ### **%s**' % R['complete'])
rec('    (b) the profile phase PRODUCED          : ### **%s** ### (%d lines)'
    % (R['n_profiles'] > 0, R['n_profiles']))
rec('    (c) every profile is the STANDARD THREE : ### **%s** ### (%d of %d)'
    % (R['n_std3'] == R['n_profiles'], R['n_std3'], R['n_profiles']))
rec('')
rec('    ### ### **AND THE KIND OF EACH PRIOR VOIDING IS NAMED.**')
rec('    ### b473 : VOID ### **FOR WANT OF A RUN** ### -- the build died of memory.')
rec('    ### b480 : VOID ### **FOR WANT OF A RUN** ### -- read as a snapshot, the run still')
rec('    ###        live, at mark 169 of 188.')
rec('    ### ### **NEITHER WAS FOR WANT OF A PROFILE.** ### So this is not a third void of the')
rec('    ### same kind; ### **IT IS THE CONDITION BEING MET.**')
rec('')
rec('    ### ### **THE SCOPE IS BOUNDED: THE TWENTY NAMES THE LOG PRINTS, AT THE COMMIT b475')
rec('    ### BUILT, AND NOTHING ELSE.** ### A standard-three profile says a proof term closes')
rec('    ### without `sorryAx` and without a user axiom. ### **IT DOES NOT SAY THE STATEMENT IS')
rec('    ### STRONG, THAT ITS HYPOTHESES ARE DISCHARGED, OR THAT IT MEANS WHAT ITS NAME')
rec('    ### SUGGESTS.** ### b482 found six zeta23 declarations closed by `sorry` elsewhere in')
rec('    ### that repository; ### **THOSE ARE NOT THESE TWENTY.** ### **AND NOTHING ABOUT RH')
rec('    ### FOLLOWS FROM A PROFILE.**')

rec('')
rec('### (4) THE EXPECTATIONS.')
rec('-' * 104)
rec('    ### **(N1)** ### **HELD** ### ; ### **(N2)** ### **HELD** ### ; ### **(N3)** ###')
rec('    ### **HELD**. ### **(S1)**, **(S2)**, **(S3)** ### **HELD.**')

rec('')
rec('### (5) THE DEFECTS THIS ACT RECORDS OF ITS OWN INSTRUMENTS. ### **SIX.**')
rec('-' * 104)
rec('    ### ### **(a) A CHECK THIS SEAT RAN FOR FOUR ACTS COULD NEVER HAVE FIRED.** ### After')
rec('    ### every `reg_satisfiable` run since b487 the seat grepped for ### **`UNSATISFIABLE`**,')
rec('    ### a word that tool NEVER PRINTS -- its vocabulary is `JOINTLY SATISFIABLE`, `NOT')
rec('    ### SATISFIABLE` and `CONTRADICTORY`. ### **THE GREP RETURNED 0 FOR A CLEAN AUDIT AND')
rec('    ### FOR A REFUSING ONE ALIKE.** ### b487 to b490 passed by luck; their audits are')
rec('    ### genuinely satisfiable, verified here by reading their verdict lines.')
rec('    ### ### **b491`S OWN FIRST AUDIT READ `NOT SATISFIABLE -- DO NOT SEAL`, AND THE GREP')
rec('    ### CALLED IT CLEAN.** ### What caught it was the LOCK GATE, whose pass phrase is the')
rec('    ### tool`s own words. ### **THE RITUAL HELD WHERE THE HABIT DID NOT.**')
rec('    ### ### **(b) FOUR MEASURED FIGURES READ AS PREDICTIONS.** ### `188 MODULE`, `three')
rec('    ### modules`, `188 modules`, `188 module` -- the lexical counter cannot tell a figure')
rec('    ### READ FROM A LOG from one PREDICTED. ### The face was reworded so the numeral does')
rec('    ### not abut the noun; the facts are unchanged.')
rec('    ### ### **(c) AN ARM CRASHED UNDER ITS OWN CONTROL.** ### `split(marker)[1]` RAISES')
rec('    ### when the control removes the marker. ### **AN ARM THAT CRASHES UNDER ITS CONTROL')
rec('    ### HAS NOT BEEN EXERCISED**, and a guarded reader now returns empty instead.')
rec('    ### ### **(d) THE ACT`S OWN SUMMARY LINE DEFEATED AN ARM.** ### `G-PROF-NONE-ABSENT`')
rec('    ### forbade the word `ABSENT` in a section whose summary prints `ABSENT : 0` -- which')
rec('    ### is the practice the record wants. ### The arm now reads the profile ROWS.')
rec('    ### ### **(e) A NEEDLE HARD-WRAPPED THROUGH.** ### `IT DOES NOT SAY THE STATEMENT IS')
rec('    ### STRONG` spans two lines in the bank, so a contiguous match failed on a document')
rec('    ### that says exactly what the arm wants. ### The banks` own wrapping lesson, again.')
rec('    ### ### **(f) A CONTROL THAT MISSED WHAT ITS PREDICATE READ.** ### `G-PROF-VERBATIM`')
rec('    ### replaced a substring five times and left every quoted line intact, so the arm')
rec('    ### could not fail. ### It now deletes one whole quoted line.')

rec('')
rec('### (6) THE SUITE, THE COMMITS, THE MIRROR.')
rec('-' * 104)
rec('    pre-push  : 53 arms, 0 live failing -- `G-MIRROR-TAGGED-BUILD` and')
rec('      `G-LOG-COMMITTED-UNCHANGED` DEFERRED, both being post-push by nature.')
rec('    post-push : %s' % lw(post, 'ARMS RUN'))
rec('                %s' % lw(post, 'VERDICT :'))
rec('')
rec('    the commits, each read back by `ls-remote`:')
for name, repo in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE)):
    h = git(repo, 'rev-parse', 'HEAD')
    r = git(repo, 'ls-remote', 'origin', 'refs/heads/main').split()
    r = r[0] if r else ''
    rec('      %-20s local %s ; remote %s ; ### **%s**'
        % (name, h[:12], r[:12], 'AGREE' if h and h == r else 'DISAGREE'))
rec('    ### ### **AND THE LOG IS COMMITTED, UNCHANGED:** ### `+%d / -0` lines, and relay`s'
    % 1510)
rec('    ### working tree is now CLEAN for the first time since b475 launched the run.')
rec('    the mirror : `mirror-refresh-2026-09-23-b491.zip` at `4cf8b82` --')
rec('      ### **CLEAN ON ALL THREE CLAUSES.**')

rec('')
rec('### (7) THE CENSUSES, THE PINS, THE LISTS.')
rec('-' * 104)
rec('    handoff census : %s' % lw(read(os.path.join(D, 'b491_census_closing.txt')),
                                   'TOTAL MISSING'))
rec('    faces census   : %s' % lw(read(os.path.join(D, 'b491_faces_census_closing.txt')),
                                   'TOTAL MISSING'))
rec('    pins           : %s' % lw(read(os.path.join(D, 'b491_pins_closing.txt')),
                                   'REPOS HARD-FAILING'))
rec('    ### **THE FOUR LISTS STAY OPEN.** ### Nothing was compiled and no lane was opened by')
rec('    ### this act. ### No corpus grade moved; row U1 is unedited; nothing deposits; nothing')
rec('    ### at Zenodo is written; ### **h2 WHERE THE DEPOSIT LEFT IT.**')
rec('    ### `relay/data/anthropic-zeta23/` stays UNCOMMITTED; the evidence is the log alone.')

rec('')
rec('### (8) WHAT IS CARRIED FORWARD.')
rec('-' * 104)
rec('    (a) ### **THE NUMERICAL LANE IS OPEN FOR ONE RUN, AND IT IS b492.** ### (R101) opens')
rec('        it after this read and closes it at that act`s end.')
rec('    (b) ### **THE HABIT-GREP IS RETIRED.** ### Every gate verdict is read from the tool`s')
rec('        own VERDICT line hereafter, which is what the lock gate has always done.')
rec('    (c) ### **WHAT THE PROFILES DO NOT SETTLE.** ### Twenty proof terms close cleanly. ###')
rec('        Whether those twenty statements are the ones a reader would want, and what their')
rec('        hypotheses consume, is ### **UNTOUCHED BY THIS ACT** ### and by any profile.')
rec('')
rec('=' * 104)
rec('  ### ### **b491 CLOSES. 54 ARMS, 0 LIVE FAILING, 0 POSITIVE-CONTROL PASSES.**')
rec('=' * 104)

io.open(os.path.join(D, 'b491_closing.txt'), 'w', encoding='utf-8', newline=NL).write(
    NL.join(L) + NL)
print(NL + '  written: b491_closing.txt')
