# -*- coding: utf-8 -*-
"""b326_checks.py -- THE GATE SUITE FOR A REACH THAT CLOSED THE FORMULA AND STILL SAW NOTHING.

### ### **THE ARMS THAT CARRY THIS ACT:**
###   ### ### **`G-NOTMETHOD`** ### -- ### **THE ONE THIS ACT WOULD MOST EASILY HAVE BREACHED.** ###
###     `DOES NOT SEE IT` at twenty-six cells and a declared aimed family reads as a verdict on the
###     method; it is a verdict on families, with the reason from the numbers and the family that
###     could see it priced. ### Bank, table, index must all carry the refusal by name.
###   ### ### **`G-KERNEL`** ### -- the derivation of section (1) was written BEFORE any run, and the
###     closure decided it: the derived kernel closes, b325's fails by the missing half at every cell
###     below the ceiling. ### The bank must carry both tallies and the link walked.
###   ### ### **`G-ORDER`** ### -- the registration was sealed before any instrument of this act ran:
###     the seal verifies, the bank says so, and the seal's file predates every instrument's record.
###   ### **`G-CONTROL`** ### -- zeta permitted at every cell under the full prime set.
###   ### **`G-COMPLETE`** ### -- the completeness census reaches the library's top and the count
###     closes by the argument principle; the library the order named is reported as failing.
###   ### **`G-SCOPE`** ### -- the lore rule this act mechanized: the prime set is generated to the
###     reach, the scope is in the header, and the lore's self-test fires in both polarities.
###   ### **`G-OWNDEFECT`** ### -- three of the act's own estimates failed their own gates; each is
###     declared in the bank and each is kept on disk under its own name.
###   ### **`G-AIMED`** ### -- the declared family is reported on its own line, never merged.
"""
import hashlib
import io
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import needle_pull       # noqa: E402
import hedge_audit       # noqa: E402
import ferry_scan        # noqa: E402
import banned_terms      # noqa: E402
import b306_stem_scope   # noqa: E402
import b317_checks as K7  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
DEPOSIT = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
CONFINE_DEP = os.path.join(DEPOSIT, 'Which_Structure_Confines.md')
CONFINE_INT = os.path.join(PP, 'day1', 'Which_Structure_Confines.md')
CENSUS_TOOL = os.path.join(ROOT, 'tools', 'e16', 'epstein_census.py')
ATLAS = os.path.join(ROOT, 'tools', 'e16', 'carto_atlas.py')
WINDOW = os.path.join(ROOT, 'tools', 'b321_window.py')
LORE = os.path.join(ROOT, 'tools', 'lore_rules.py')
TWIN_MD5 = '6b18d69bcf9e619d3b2fb22376ccc432'

# ### owner instruments READ and never edited -- b321_window.py is the ONE ordered edit and is checked apart.
OWNERS = ['tools/e16/epstein_census.py', 'tools/e16/epstein_li_v3.py', 'tools/e16/carto_atlas.py',
          'tools/e16/epstein_census_bank.jsonl', 'tools/b316_instrument.py', 'tools/b317_smear.py',
          'tools/b318_square.py', 'tools/b319_stable.py', 'tools/b320_weil.py', 'tools/b322_ladder.py',
          'tools/b323_fold.py', 'tools/b324_reread.py', 'tools/b325_epstein.py', 'tools/noise_floor.py']


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


BANK = d('b326_the_reach.txt')
REG = d('b326_registration_2026-09-04.txt')
ZRUN = d('b326_zeros_run.txt')
ORUN = d('b326_offline_run_150.txt')
WRUN = d('b326_windows_run.txt')
CRUN = d('b326_closure_run.txt')
FIL = d('b326_filings_run.txt')
SCAN = d('b326_ferry_scan.txt')
FERRY = d('b326_ferry_2026-09-04.txt')
CENSUS = d('b326_census.txt')
REGSPEC = d('b326_regspec_run.txt')
SATIS = d('b326_satisfiable_run.txt')
LORERUN = d('b326_lore_run.txt')

OWNED = [ZRUN, ORUN, WRUN, CRUN, FIL, CENSUS, REGSPEC, SATIS, LORERUN, d('b326_filings_rerun.txt'),
         d('b326_index_run.txt'), d('b326_pins_stepzero.txt'), d('b326_reg_termscan.txt'),
         d('b326_satisfiable.json'), d('b326_window_fixtures.txt'), d('b326_zeros_box_run.txt'),
         d('b326_offline_run.txt'), d('b326_closure_run_first_defective.txt'),
         t('b326_regspec.py'), t('b326_correspondence.py'), t('b326_zeros.py'), t('b326_zeros_box.py'),
         t('b326_offline.py'), t('b326_windows.py'), t('b326_closure.py'), t('b326_filings.py'),
         t('b326_lore_append.py'), t('b321_window.py')]

CARRIERS = [
    (t('b326_checks.py'), 'its own fixtures'),
    (t('b326_index_append.py'), 'its own fixtures'),
    (BANK, "it is the act's own voice and is scanned as such"),
    (REG, 'it is the sealed registration'),
    (FERRY, "IT IS THE ORDER -- not this act's writing"),
    (SCAN, "it is the scan's own log"),
]

OWNER_NEEDLES = [
    ("the census's own caveat, at the census", CENSUS_TOOL, 'critical-line scan would IMPOSE the real part'),
    ("### and its factor", CENSUS_TOOL, 'Lambda(s) = (sqrt(23)/2pi)^s Gamma(s) Z_Q(s)'),
    ("### and its own step", CENSUS_TOOL, 'T_LO, T_HI, T_STEP = 0.5, 60.0, 0.5'),
    ("the atlas's kernel, at the atlas", ATLAS, "Re psi(1/4 + i u/2) - log pi"),
    ("### and its prime loop", ATLAS, 'for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):'),
    ("the ordered edit's scope sentence, at the edited file", WINDOW,
     'THE PRIME SET IS GENERATED TO THE REACH, NEVER FIXED'),
    ("### and the generator the prime sum now reads", WINDOW, 'for p in primes_to(math.exp(L) + PRIME_TOL)'),
    ("the lore rule, at the lore", LORE, "rule='A constant is scope-bound and its scope is written down."),
    ("### and its fixture", LORE, "('scope-bound constant (b325/b326)', _fixture_scope_bound)]:"),
    ("the confinement keystone's finding, AT THE VERIFIED DEPOSIT COPY", CONFINE_DEP,
     'it does not confine zeros to it'),
    ("b325's priced crossing, in b325's own bank", d('b325_the_negative_control.txt'),
     'THE EPSTEIN SIGN CROSSES AT `a = 22`'),
    ("### and b325's kernel, in b325's own tool", t('b325_epstein.py'),
     'return (np.array([float(mre(digamma(mpc(0.5, uu)))) for uu in U]) - c)'),
    ("b321 -- the forced sign", d('b321_the_window_opened.txt'),
     'THAT COUNT IS FORCED BY THE SHAPE OF THE COMPUTATION'),
]

SELF_NEEDLES = [
    ('bank states the answers first', BANK, 'THE ANSWERS, FIRST.'),
    ('### the verdict', BANK, "TWENTY-SIX CELLS TO `a = 400` : DOES NOT SEE IT"),
    ('### the expectation split', BANK, 'REFUTED IN ITS FIRST HALF'),
    ('### the kernel', BANK, 'THE PRICED CROSSING WAS AN ARTEFACT, AND THE CLOSURE DECIDED IT'),
    ('### the count', BANK, '146 ON THE LINE TO `T = 150`, 17 OFF IT, AND THE COUNT'),
    ('### the closure for both', BANK, 'THE EXPLICIT FORMULA CLOSES FOR BOTH'),
    ('### the aimed family', BANK, 'DECLARED AND SEPARATE : DOES NOT SEE IT EITHER'),
    ('### three own estimates', BANK, "THREE OF THIS ACT'S OWN ESTIMATES FAILED THEIR OWN GATES"),
    ('bank says what it does not say', BANK, 'WHAT THIS ACT DOES NOT SAY.'),
    ('### the theorem does not transfer', BANK, 'IT DOES NOT SAY THE SOURCE\'S INEQUALITY OR THE OBJECT\'S DECOMPOSITION TRANSFER'),
    ('### b325 not re-verdicted', BANK, 'IT DOES NOT RE-VERDICT b325'),
    ('### the census not called wrong', BANK, "IT DOES NOT CALL THE CORPUS'S CENSUS WRONG"),
    ('bank keeps the order', BANK, 'THE ORDER OF THIS ACT, KEPT.'),
    ('### sealed before any run', BANK, 'THE REGISTRATION WAS SEALED BEFORE ANY INSTRUMENT OF THIS ACT RAN'),
    ('bank gives step zero', BANK, 'STEP ZERO.'),
    ('bank gives the zeros', BANK, 'COMPONENT 1 -- THE ZEROS.'),
    ('### the gate fired', BANK, 'THE REGISTERED PRECISION FAILED ITS OWN GATE, AND THE GATE WAS REGISTERED SO THAT IT'),
    ('### the pole-term cancellation', BANK, 'IS `e^{pi t/2}/t^2` TIMES LARGER THAN `Lambda(1/2 + i t)` ITSELF'),
    ('### the two routes agree', BANK, 'EVERY ONE AGREED BY BOTH ROUTES TO THE LAST'),
    ('### the caveat quoted', BANK, 'A critical-line scan would IMPOSE the real'),
    ('### the boxes', BANK, '299 OF 299 BOXES HOLDING EXACTLY THEIR SIGN-CHANGE'),
    ('### the count short of the main term, measured', BANK, 'AND THE COUNT FALLS SHORT OF THE MAIN TERM, WHICH IS A MEASUREMENT AND NOT A'),
    ('### the completeness census', BANK, 'THE COMPLETENESS CENSUS -- THE FOURTH LINK, MEASURED TO THE LIBRARY'),
    ('### the abscissa', BANK, 'THE ABSCISSA `1.50` IS NOT A CHOICE'),
    ('### fifteen unbanked', BANK, 'FIFTEEN OF THE SEVENTEEN WERE UNBANKED'),
    ('### the count closes', BANK, 'THE COUNT NOW CLOSES BY THE ARGUMENT PRINCIPLE'),
    ('bank gives the windows', BANK, 'COMPONENT 2 -- THE TWO WINDOWS, SIDE BY SIDE.'),
    ('### the prime set no longer a constant', BANK, 'THE PRIME SET IS NO LONGER A CONSTANT.'),
    ('### zeta control', BANK, 'THE ZETA CONTROL, UNDER THE FULL PRIME SET: THE PERMITTED SIGN AT EVERY ONE OF THE'),
    ('### no crossing', BANK, 'NO CROSSING AT THIS REACH.'),
    ('### b325 kernel crossing reproduced', BANK, "THE EPSTEIN SIGN, b325's KERNEL: POSITIVE AT `22, 24, 28, 32, 50, 64` AND NEGATIVE AGAIN"),
    ('bank gives the corroboration', BANK, 'COMPONENT 3 -- THE CORROBORATION. ### THE EXPLICIT FORMULA CLOSED FOR BOTH.'),
    ('### the method change declared', BANK, 'DECLARED CHANGE OF METHOD FROM THE REGISTERED QUADRATURE PAIR'),
    ('### the aliasing incident', BANK, '`7.400774` WHERE THE PLACES SUM SAID `0.003447`'),
    ('### one f on both sides', BANK, 'AND ONE `f` ON BOTH SIDES.'),
    ('### the omitted truncation', BANK, "REGISTRATION'S LIST OF TRUNCATIONS OMITTED AND WHICH IS `3.6e-05` AT `a = 1.3`"),
    ('### zeta closes', BANK, 'ZETA: CLOSES AT TWENTY-SIX OF TWENTY-SIX CELLS.'),
    ("### the order's library fails", BANK, 'CLOSES AT 6, FAILS AT 15, BEYOND THE CEILING AT 5'),
    ('### every located zero closes', BANK, 'CLOSES AT TWENTY-ONE OF TWENTY-ONE CELLS'),
    ('### the ceiling honest', BANK, 'TOO SHORT FOR THEM, AND THE ACT SAYS SO RATHER THAN CLOSING THEM'),
    ("### b325's kernel fails by the half", BANK, 'MISSING HALF, TO WITHIN THE BAR'),
    ('### section (1) decided', BANK, 'SECTION (1) OF THE REGISTRATION IS DECIDED, AND AGAINST THE PRIOR ACT'),
    ('bank gives the verdict', BANK, 'COMPONENT 4 -- THE VERDICT, AT EXACTLY ITS SCOPE.'),
    ('### the reason named', BANK, 'THE REASON, NAMED'),
    ('### off-line terms positive', BANK, 'CONTRIBUTE THE WRONG SIGN TO SEE IT WITH'),
    ('### the aimed family separate', BANK, 'THE AIMED FAMILY (DECLARED, SEPARATE, NEVER MERGED) : DOES NOT SEE IT.'),
    ('### the family that could', BANK, 'A FAMILY THAT SEES THE FAILURE NEEDS A SIGN'),
    ('### the entailment', BANK, 'IT IS A TEST THIS FAMILY CANNOT FAIL'),
    ('### the ceiling printed', BANK, 'THE CEILING, PRINTED:'),
    ('bank states the shadow', BANK, 'THE SHADOW.'),
    ('### and that nothing is kept', BANK, 'NOTHING IS KEPT'),
    ('bank keeps M-2 under its cap', BANK, 'M-2 REMAINS OWED UNDER'),
    ('bank restates the seam debt item 1', BANK, "THE SEAM'S DEBT, ITEM 1"),
    ('bank restates the patent clock', BANK, 'THE PATENT CLOCK IS RESTATED'),
    ('bank keeps h2 where the deposit left it', BANK, 'h2 STANDS EXACTLY WHERE THE DEPOSIT LEFT IT'),
    ('bank keeps the deposit shut', BANK, 'NOTHING DEPOSITS'),
    ('bank gives the in-flight register', BANK, 'THE IN-FLIGHT REGISTER.'),
    ('### declared against itself', BANK, 'DECLARED AGAINST THIS ACT ITSELF'),
    ('bank says what is due next', BANK, 'WHAT IS DUE NEXT.'),
    ('### the bridge read next', BANK, 'THE BRIDGE READ IS NAMED NEXT BY THE ORDER'),
    ('### the exhaustion module after it', BANK, 'THE FINITE-SIDE EXHAUSTION MODULE IS NAMED AS THE KERNEL ACT AFTER IT'),
    ('### the withdrawn entry', BANK, '[WITHDRAWN]'),
    ('### no recommendation', BANK, 'NO RECOMMENDATION AND NO RANKING'),
    ('registration names the act', REG, 'THE REACH. ### THE REGISTRATION.'),
    ('### sealed before any run', REG, 'THIS REGISTRATION IS SEALED BEFORE ANY INSTRUMENT OF THIS ACT RUNS'),
    ('### the derivation as a bar', REG, 'ONE HALF OF'),
    ('### the expectation verbatim', REG, 'SEES IT near the priced crossing, with zeta'),
    ('the zeros run: the gate fired', ZRUN, 'THE REGISTERED PRECISION FAILS ITS OWN GATE'),
    ('### 146 located', ZRUN, 'on-line zeros located : 144 ; route disagreements above 1e-08 : 0'),
    ('the box resolved', d('b326_zeros_box_run.txt'), 'on-line zeros now 146 ; box mismatches now 0'),
    ('the census to 150', ORUN, 'off-line zeros located : 17 ; sub-boxes where fewer were located than wound : 0'),
    ('### banked reappear', ORUN, 'the two banked off-line zeros reappear : 2 of 2'),
    ('the windows: zeta control', WRUN, 'cells with a CERTIFIED positive zeta places sum : NONE ; cells not certified : NONE'),
    ('### no crossing', WRUN, 'THE CROSSING CELL, FROM THE NUMBERS (derived kernel) : NO CROSSING AT THIS REACH'),
    ("### b325's kernel positive", WRUN, 'THE EPSTEIN SIGN, b325 KERNEL   : certified POSITIVE at [22.0, 24.0, 28.0, 32.0, 50.0, 64.0]'),
    ('the closure: zeta', CRUN, 'CLOSURE TALLY  zeta : 26 CLOSES / 0 FAILS / 0 BEYOND CEILING'),
    ("### the order's library", CRUN, 'CLOSURE TALLY  Epstein, DERIVED kernel : 6 CLOSES / 15 FAILS / 5 BEYOND CEILING'),
    ('### every located', CRUN, 'CLOSURE TALLY  Epstein, DERIVED kernel, EVERY located off-line zero : 21 CLOSES / 0 FAILS / 5 BEYOND CEILING'),
    ("### b325's kernel", CRUN, 'CLOSURE TALLY  Epstein, b325 kernel,    EVERY located off-line zero : 0 CLOSES / 21 FAILS / 5 BEYOND CEILING'),
    ('### the link walked', CRUN, 'equals A_q - A_q(b325) to within the bar : True'),
    ('### the verdict', CRUN, "VERDICT, THE ARC'S FAMILY : DOES NOT SEE IT"),
    ('### the aimed verdict', CRUN, 'AIMED : DOES NOT SEE IT'),
    ('### the count by the argument principle', CRUN, '146 on the line + 2 x 17 off = 180'),
    ('the filing reports append-only', FIL, 'APPEND-ONLY : True'),
    ('### and the deposit byte-unchanged', FIL, 'THE DEPOSIT IS BYTE-UNCHANGED : True'),
    ('### and the correction carried', FIL, 'the block carries the kernel correction : True'),
    ('the lore fired both ways', LORERUN, 'scope-bound constant (b325/b326)     fires: True   stays quiet: True   PASS'),
    ('the satisfiability run passes', SATIS, 'JOINTLY SATISFIABLE'),
    ('the regspec found no predictions', REGSPEC, 'ARTIFACT-COUNT PREDICTIONS FOUND : 0'),
    ('the census found nothing missing', CENSUS, 'TOTAL MISSING : 0'),
    ('the ferry scan was clean', SCAN, 'STRUCK-CLAUSE HITS : 0'),
    ('### on stems too', SCAN, 'BANNED/RETIRED-STEM HITS : 0'),
    ("b321_window's fixtures after the edit", d('b326_window_fixtures.txt'),
     'FIXTURES : [True, True, True, True, True, True, True, True]  PASS'),
]

MUST_FAIL = [
    ('the instrument is not said to see it', BANK, 'THE INSTRUMENT SEES IT.'),
    ('### nor the method condemned', BANK, 'THE METHOD CANNOT SEE A FAILURE.'),
    ('b325 is not re-verdicted', BANK, 'b325 IS RE-VERDICTED.'),
    ('the census is not called wrong', BANK, 'THE CENSUS WAS WRONG.'),
    ('the theorem is not said to cover Z_Q', BANK, 'THEOREM 1 COVERS Z_Q.'),
    ('the zeta window is not called a passed test', BANK, 'THE ZETA WINDOW IS A PASSED TEST.'),
    ('the sealed b325 file is not edited', BANK, "b325's REGISTRATION IS EDITED."),
    ('no deposited text is edited', BANK, 'THE DEPOSIT IS EDITED.'),
    ('no grade is moved', BANK, 'A GRADE IS MOVED.'),
    ('the wave is not started', BANK, 'THE WAVE IS STARTED.'),
    ('no aggregation is stated', BANK, 'M-2 IS STATED.'),
    ('nothing about h2', BANK, 'h2 IS AFFECTED.'),
    ('RH is not addressed', BANK, 'RH HOLDS.'),
    ('### either way', BANK, 'RH FAILS.'),
]

TOOLNUM = [
    ("the zero library: two routes, every box, the precision gate", 'tools/b326_zeros.py'),
    ("the one mismatched box, resolved", 'tools/b326_zeros_box.py'),
    ("the completeness census over the right half-strip", 'tools/b326_offline.py'),
    ("the two windows, both kernels, the gate", 'tools/b326_windows.py'),
    ("the closure, the exact transform, the verdict", 'tools/b326_closure.py'),
    ("the ordered edit: the prime set to the reach", 'tools/b321_window.py'),
    ("the lore rule with its fixture", 'tools/b326_lore_append.py'),
    ("the evaluator the census owns, rebound not edited", 'tools/e16/epstein_census.py'),
    ("the artifact-count prediction demand (ruling 1)", 'tools/b326_regspec.py'),
    ("the satisfiability verdict over the declared caps", 'tools/reg_satisfiable.py'),
    ("the noise-floor gate", 'tools/noise_floor.py'),
    ("what is missing from the ledger, counted", 'tools/b307_handoff_census.py'),
    ("the shared-target sweep's hits", 'tools/b306_stem_scope.py'),
    ("the ferry scan's counts", 'tools/ferry_scan.py'),
    ("the banned/retired stem counts", 'tools/banned_terms.py'),
    ("the gate, needle and hedge counts", 'tools/b326_checks.py'),
    ("### the stripper those gates read code with", 'tools/b317_checks.py'),
    ("the correspondence rows' numbers", 'tools/b326_correspondence.py'),
    ("the index keys' read-back arms", 'tools/b326_index_append.py'),
    ("the append-only filing and its prefix checks", 'tools/b326_filings.py'),
    ("the registration's seal hash", 'tools/reg_seal.py'),
]
NEW_THIS_ACT = tuple(x for _w, x in TOOLNUM if '/b326' in x)

SEAL = '52f3ac4be6cde32e010d50e0af263126e56a6ea8ee4fc502003ecea5381e758c'


def main():
    fails = []
    print('=' * 100)
    print('b326 -- GATE SUITE (THE REACH: THE FORMULA CLOSED FOR BOTH, AND THE INSTRUMENT SAW NOTHING)')
    print('=' * 100)

    unpullable = 0
    print('\n  OWNER NEEDLES (each at the file that EMITTED it; the deposit at its VERIFIED copy):')
    for lbl, path, anchor in OWNER_NEEDLES:
        try:
            needle_pull.pull(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))

    print('\n  SELF NEEDLES:')
    for lbl, path, anchor in SELF_NEEDLES:
        try:
            needle_pull.pull_self(path, anchor)
            print('    PASS  %s' % lbl)
        except LookupError:
            unpullable += 1
            fails.append(lbl)
            print('    ### FAIL (UNPULLABLE)  %s  anchor=%r' % (lbl, anchor))

    print('\n  MUST-FAIL FIXTURES (whole-line equality, never substring):')
    for lbl, path, line in MUST_FAIL:
        if needle_pull.absent_exact(path, line):
            print('    PASS  %s' % lbl)
        else:
            fails.append(lbl)
            print('    ### FAIL  %s -- the forbidden line IS present' % lbl)

    bank = io.open(BANK, encoding='utf-8').read()
    reg = io.open(REG, encoding='utf-8').read()
    crun = io.open(CRUN, encoding='utf-8').read()
    wrun = io.open(WRUN, encoding='utf-8').read()
    tbl = io.open(TABLE, encoding='utf-8').read()
    idx = io.open(t('banked_index.py'), encoding='utf-8').read()
    rows = [ln for ln in tbl.split('\n') if ln.startswith('| 164 |') or ln.startswith('| 165 |')]
    rowtxt = '\n'.join(rows)

    print('\n  G-NOTMETHOD (a family verdict is not a method verdict):')
    nm = ('IT DOES NOT SAY THE INSTRUMENT CANNOT SEE A FAILURE' in bank
          and 'A FAMILY VERDICT IS NOT A METHOD VERDICT' in idx
          and 'priced at one act, not built' in rowtxt
          and 'SIGN CHANGE ACROSS beta AND 1 - beta' in rowtxt
          and 'NOT A PASSED TEST' in rowtxt and len(rows) == 2)
    print('    bank refuses it, index refuses it BY NAME, rows carry the priced family and the entailment : %s' % nm)
    if not nm:
        fails.append('G-NOTMETHOD')

    print('\n  G-KERNEL (derived before any run; decided by the closure; the link walked):')
    gk = ('ONE HALF OF' in reg
          and reg.index('ONE HALF OF') < reg.index('(8) THE CAPS')
          and 'DERIVED kernel, EVERY located off-line zero : 21 CLOSES / 0 FAILS' in crun
          and 'b325 kernel,    EVERY located off-line zero : 0 CLOSES / 21 FAILS' in crun
          and 'equals A_q - A_q(b325) to within the bar : True' in crun
          and 'MISSING HALF' in rowtxt and 'MISSING HALF' in idx.upper()
          and 'b325 IS NOT RE-VERDICTED' in rowtxt and 'b325 IS NOT RE-VERDICTED' in idx)
    print('    registration carries the derivation; closure decides it both ways; the missing half matches; b325 unmoved : %s' % gk)
    if not gk:
        fails.append('G-KERNEL')

    print('\n  G-ORDER (the registration was sealed before any instrument of this act ran):')
    rs = subprocess.run([sys.executable, t('reg_seal.py'), '--verify', REG],
                        capture_output=True, text=True, encoding='utf-8', errors='replace')
    intact = 'SEAL INTACT' in (rs.stdout or '')
    same = SEAL in reg
    seal_m = os.path.getmtime(REG)
    firsts = [os.path.getmtime(p) for p in (ZRUN, WRUN, ORUN, d('b326_offline_run.txt'), d('b326_zeros_box_run.txt'))
              if os.path.exists(p)]
    precedes = all(seal_m < m for m in firsts)
    print('    seal verifies : %s ; hash matches the literal in this gate : %s ; the sealed file predates every instrument record : %s'
          % (intact, same, precedes))
    print("    ### the bank's own sentence : %s" % ('THE REGISTRATION WAS SEALED BEFORE ANY INSTRUMENT OF THIS ACT RAN' in bank))
    if not (intact and same and precedes):
        fails.append('G-ORDER')

    print('\n  G-CONTROL (zeta permitted at every cell under the full prime set):')
    gc = ('cells with a CERTIFIED positive zeta places sum : NONE ; cells not certified : NONE' in wrun
          and 'CLOSURE TALLY  zeta : 26 CLOSES / 0 FAILS / 0 BEYOND CEILING' in crun)
    print('    windows and closure : %s' % gc)
    if not gc:
        fails.append('G-CONTROL')

    print('\n  G-COMPLETE (the census reaches the library top; the count closes; the ordered library reported failing):')
    gq = ('146 on the line + 2 x 17 off = 180' in crun
          and 'DERIVED kernel : 6 CLOSES / 15 FAILS / 5 BEYOND CEILING' in crun
          and 'CLOSES AT 6, FAILS AT 15, BEYOND THE CEILING AT 5' in bank
          and 'FIFTEEN OF THE SEVENTEEN WERE UNBANKED' in bank)
    print('    count by the argument principle; the failing ordered library in run and bank : %s' % gq)
    if not gq:
        fails.append('G-COMPLETE')

    print('\n  G-SCOPE (the mechanized lore rule: a constant is scope-bound and its scope is written down):')
    wsrc = io.open(WINDOW, encoding='utf-8').read()
    lr = subprocess.run([sys.executable, LORE], capture_output=True, text=True, encoding='utf-8', errors='replace')
    fired = any('scope-bound constant' in ln and 'fires: True' in ln and 'stays quiet: True' in ln
                for ln in (lr.stdout or '').splitlines())
    gs = ('THE PRIME SET IS GENERATED TO THE REACH, NEVER FIXED' in wsrc
          and 'for p in primes_to(math.exp(L) + PRIME_TOL)' in wsrc
          and 'for p in PRIMES:' not in wsrc
          and fired and lr.returncode == 0)
    print('    header carries the scope, the loop reads the generator, the lore fires both ways : %s' % gs)
    if not gs:
        fails.append('G-SCOPE')

    print('\n  G-OWNDEFECT (three of the act\'s own estimates, declared and kept on disk):')
    od = ("THREE OF THIS ACT'S OWN ESTIMATES FAILED THEIR OWN GATES" in bank
          and 'THE REGISTERED PRECISION FAILS ITS OWN GATE' in io.open(ZRUN, encoding='utf-8').read()
          and os.path.exists(d('b326_closure_run_first_defective.txt'))
          and os.path.exists(d('b326_epstein_zeros_before_box.json'))
          and 'arch u-tail' in crun)
    print('    declared in the bank; the gate line in the zeros run; the defective first closure and the pre-resolution library kept : %s' % od)
    if not od:
        fails.append('G-OWNDEFECT')

    print('\n  G-AIMED (the declared family on its own line, never merged):')
    ga = ('AIMED : DOES NOT SEE IT' in crun and 'NEVER MERGED' in bank
          and 'reported separately and never merged' in io.open(CONFINE_INT, encoding='utf-8', errors='replace').read())
    print('    run, bank and keystone block keep it separate : %s' % ga)
    if not ga:
        fails.append('G-AIMED')

    print('\n  G-DEPOSIT (no file under outputs/DEPOSITED-v1.1.2/ is written):')
    st = subprocess.run(['git', '-C', PP, 'status', '--porcelain', 'outputs/DEPOSITED-v1.1.2'],
                        capture_output=True, text=True).stdout.strip()
    twin = hashlib.md5(open(CONFINE_DEP, 'rb').read()).hexdigest()
    print('    git status over the deposit path : %r ; twin md5 %s (verified %s)' % (st, twin, TWIN_MD5))
    if st or twin != TWIN_MD5:
        fails.append('G-DEPOSIT')

    print('\n  G-APPEND (the internal keystone append-only; b325\'s block still visible above b326\'s):')
    rel = 'day1/Which_Structure_Confines.md'
    blob = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + rel], capture_output=True).stdout.decode('utf-8', 'replace')
    now = io.open(CONFINE_INT, encoding='utf-8', errors='replace').read()
    pfx = now.replace('\r\n', '\n').startswith(blob.replace('\r\n', '\n').rstrip('\n'))
    once = now.count('<!-- b326 cross-reference -->')
    order_ok = now.find('<!-- b325 cross-reference -->') < now.find('<!-- b326 cross-reference -->')
    print('    blob is a TRUE PREFIX : %s ; b326 block appears %d time(s) ; b325 block precedes it : %s' % (pfx, once, order_ok))
    if not (pfx and once == 1 and order_ok):
        fails.append('G-APPEND')

    print('\n  G-NOEDIT (no owner instrument edited beyond the ONE ordered edit):')
    dirty = subprocess.run(['git', '-C', ROOT, 'status', '--porcelain'] + OWNERS, capture_output=True, text=True).stdout.strip()
    stat = subprocess.run(['git', '-C', ROOT, 'diff', '--stat', 'HEAD', '--', 'tools/b321_window.py'],
                          capture_output=True, text=True).stdout.strip()
    print('    git status over the untouched owners : %r' % dirty)
    print('    the ordered edit, by git diff --stat : %s' % (stat.splitlines()[-1] if stat else 'already committed'))
    if dirty:
        fails.append('G-NOEDIT')

    print('\n  G-ONCE (run files written once per path):')
    once_ok = (os.path.exists(d('b326_filings_run.txt')) and os.path.exists(d('b326_filings_rerun.txt'))
               and os.path.exists(d('b326_closure_run_first_defective.txt'))
               and '_rerun.txt' in io.open(t('b326_filings.py'), encoding='utf-8').read()
               and '_rerun.txt' in io.open(t('b326_lore_append.py'), encoding='utf-8').read())
    print('    two-path writers name two files; the defective first closure kept under its own name : %s' % once_ok)
    if not once_ok:
        fails.append('G-ONCE')

    print('\n  G-PAPERS (only the internal keystone changed in PLACE-papers):')
    pp = subprocess.run(['git', '-C', PP, 'status', '--porcelain'], capture_output=True, text=True).stdout
    tracked = sorted(x[3:].strip() for x in pp.splitlines() if x.strip() and not x.startswith('??'))
    only = tracked in ([], [rel])
    print('    tracked changes : %s ; exactly the internal keystone, or already committed : %s' % (tracked, only))
    if not only:
        fails.append('G-PAPERS')

    print('\n  G-ANCESTOR (the correspondence table is a true prefix of its blob):')
    head = subprocess.run(['git', '-C', SIDE, 'show', 'HEAD:CORRESPONDENCE.md'], capture_output=True).stdout.decode('utf-8', 'replace')
    pfx2 = tbl.startswith(head.rstrip('\n'))
    print('    table is a TRUE PREFIX : %s' % pfx2)
    if not pfx2:
        fails.append('G-ANCESTOR')

    struck, unconf = ferry_scan.parse_record()
    stem_list = ferry_scan.stems()
    print('\n  G-STRUCK / G-STEM (record: %d struck, %d patterns, %d unconfirmed not loaded):'
          % (len(struck), sum(len(x['patterns']) for x in struck), unconf))
    total, stem_total, scanned = 0, 0, 0
    for p in OWNED:
        if not os.path.exists(p):
            continue
        scanned += 1
        txt = io.open(p, encoding='utf-8', errors='replace').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        total += len(ch)
        stem_total += len(sh)
        if ch or sh:
            print('    ### %-40s struck : %d   stem : %d' % (os.path.basename(p), len(ch), len(sh)))
            for h in sh:
                print('        line %d  |  %s' % (h[1], h[3][:88]))
    print('    files scanned %d   struck-clause hits %d   stem hits %d  %s'
          % (scanned, total, stem_total, 'PASS' if not (total or stem_total) else '### FAIL ###'))
    for p, why in CARRIERS:
        txt = io.open(p, encoding='utf-8').read()
        ch, _ = ferry_scan.scan_text(txt, struck, stem_list)
        _c, sh = ferry_scan.scan_text(txt, [], stem_list)
        print('    %-30s struck : %d  stem : %d  ### CARRIER -- %s' % (os.path.basename(p), len(ch), len(sh), why))
    fired_disc = 0
    for eid, text in [('S-1', 'a title must name its objects and conditions, not claim an achieved property'),
                      ('U-1', 'PREDICTED TERMINAL COUNT: ### 10.'),
                      ('U-2', 'HANDOFF CURRENT. ### TWENTY ACTS.')]:
        if ferry_scan.scan_text(text, struck, stem_list)[0]:
            fired_disc += 1
    ctrl = bool(ferry_scan.scan_text('the %s in the argument' % banned_terms.STEMS[0], [], stem_list)[1])
    print('    discrimination arms firing : %d of 3 ; stem control fires : %s' % (fired_disc, ctrl))
    if total or stem_total or fired_disc != 3 or not ctrl:
        fails.append('G-STRUCK/G-STEM')

    print('\n  G-STEM-APPENDED (the appended block, swept):')
    blk = now[now.index('<!-- b326 cross-reference -->'):] if '<!-- b326 cross-reference -->' in now else ''
    ch, _ = ferry_scan.scan_text(blk, struck, stem_list)
    _c, sh = ferry_scan.scan_text(blk, [], stem_list)
    print('    %-40s struck : %d   stem : %d' % (rel, len(ch), len(sh)))
    if ch or sh:
        fails.append('G-STEM-APPENDED')

    print('\n  G-SHARED:')
    got = set()
    for name, path, _unit in b306_stem_scope.TARGETS:
        if os.path.exists(path):
            for label, _s, _txt in b306_stem_scope.sweep(path):
                got.add((name, label))
    allowed = {('CORRESPONDENCE.md', 'row 2'), ('CORRESPONDENCE.md', 'row 101')}
    extra = got - allowed
    print('    hits : %s ; UNEXPECTED : %d  %s' % (sorted(got), len(extra), 'PASS' if not extra else '### FAIL ###'))
    if extra:
        fails.append('G-SHARED')

    print('\n  G-TOOLNUM:')
    orphan = 0
    for what, tool in TOOLNUM:
        ex = os.path.exists(os.path.join(ROOT, tool.replace('/', os.sep)))
        tr = K7.git_tracked(ROOT, tool)
        if not (ex and (tr or tool in NEW_THIS_ACT)):
            orphan += 1
        print('    %-58s %-34s exists=%s tracked=%s' % (what[:58], tool, ex, tr))
    print('    numbers with no committed producer : %d  %s' % (orphan, 'PASS' if not orphan else '### FAIL ###'))
    if orphan:
        fails.append('G-TOOLNUM')

    print('\n  HEDGE AUDIT (over every file this act wrote):')
    for lbl, path in [('the bank', BANK), ('the registration', REG), ('the zeros run', ZRUN), ('the census run', ORUN),
                      ('the windows run', WRUN), ('the closure run', CRUN), ('the filing', FIL)]:
        n, gh, ua = hedge_audit.audit(path)
        print('    %-24s sentences=%-5d graded-hedges=%-3d ungraded-shapes=%d' % (lbl, n, len(gh), len(ua)))
        for s in gh:
            print('      ### GRADED HEDGE: %s' % s[:110])
        if gh:
            fails.append('HEDGE (%s)' % lbl)

    print('\n' + '=' * 100)
    print('  ### GATES FAILING : %d %s' % (len(fails), fails if fails else ''))
    print('  ### needles unpullable : %d' % unpullable)
    print('=' * 100)
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
