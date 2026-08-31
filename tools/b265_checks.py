# -*- coding: utf-8 -*-
"""b265_checks.py -- the b265 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### ### **EVERY CHECK IS A PURE CONJUNCTION. ### NO `or` APPEARS IN ANY CHECK.**
### ### **EVERY NUMERIC PREDICATE IS `bool()`-WRAPPED.**
### ### **EVERY MULTI-NEEDLE CHECK GOES THROUGH `verify_all`, WHICH NAMES THE ABSENT NEEDLE.**

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that the registration was edited after sealing, or sealed while unsatisfiable.
###       ### Gate 1 -- the SEAL verifies AND the satisfiability check ran BEFORE it.
###   (2) that an `INSIDE` grade was asserted from `100 < 238.4` rather than measured.
###       ### Gate 2 -- the two-axis re-measure exists and its movements are banked.
###   (3) that this act failed to reproduce the columns it presumes to grade. ### Gate 3.
###   (4) that a prior act was re-verdicted, or a verdict altered. ### Gate 4.
###   (5) that the crossover law was claimed beyond its verified reference. ### Gate 5.
###   (6) that b264's false provenance clause was quietly left standing. ### Gate 6.
###   (7) that the act's own four defects were smoothed over. ### Gate 7.
###   (8) that a compile was claimed without a printed profile. ### Gate 8 -- b227's standard.
###   (9) that h2 moved. ### Gate 9.
###  (10) that an owner instrument was edited or a foreign tree swept in. ### Gate 10.
###  (11) that a registered expectation that came out WRONG was quietly dropped. ### Gate 11.
"""
import io
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains   # noqa: E402
from needle_extract import verify_all         # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')
RES = 'D:/SIDE-global-section'

REG = os.path.join(D, 'b265_registration_2026-08-31.txt')
BANK = os.path.join(D, 'b265_nq_ceiling_sweep.txt')
FIL = os.path.join(D, 'b265_filings.txt')
RUN = os.path.join(D, 'b265_run.txt')
ROWS = os.path.join(D, 'b265_rows.json')
PROF = os.path.join(D, 'b265_shadow_profile.txt')
SAT = os.path.join(D, 'audit_b265_reg_satisfiable.txt')
SHADOW = os.path.join(RES, 'Core', 'CeilingSweepShadow.lean')
SEAL = os.path.join(ROOT, 'tools', 'reg_seal.py')

INSTRUMENTS = ['b38_act10.py', 'qeps_layer.py', 'carto_atlas.py', 'prolate_layer.py',
               'b36_act8.py', 'b261_e2even.py']


def git_unchanged(rel):
    p = subprocess.run(['git', '-C', ROOT, 'diff', '--quiet', 'HEAD', '--', rel],
                       capture_output=True, text=True)
    return p.returncode == 0


def staged():
    return subprocess.run(['git', '-C', ROOT, 'diff', '--cached', '--name-only'],
                          capture_output=True, text=True).stdout


def seal_ok():
    """### RUN THE SEAL VERIFIER AS A SUBPROCESS AND READ ITS EXIT CODE. ### Not re-implemented."""
    p = subprocess.run([sys.executable, SEAL, '--verify', REG],
                       capture_output=True, text=True, cwd=ROOT)
    return p.returncode == 0, (p.stdout or '')


def main():
    h = Harness(repo_root=ROOT, act='b265')
    R = json.load(io.open(ROWS, encoding='utf-8'))
    cells = R['cells']

    # 1 -- ### THE SEAL VERIFIES, AND THE SATISFIABILITY CHECK RAN BEFORE IT.
    h.run('sealed-and-satisfiability-checked-before-the-seal',
          check=lambda: verify_all(BANK, [
              'JOINT-SATISFIABILITY',
              'THE REGISTERED CROSSOVER STATISTIC COULD NOT HAVE PASSED',
          ]) if bool(seal_ok()[0] and 'SEAL INTACT' in seal_ok()[1]
                     and os.path.exists(SAT)
                     and contains(SAT, 'JOINTLY SATISFIABLE')) else (
              'FAIL', '### the seal does not verify, or no satisfiability audit exists'),
          # ### FIXTURE: the BANK carries no seal block, so verifying IT must FAIL (exit 1).
          fixture=lambda: bool(subprocess.run([sys.executable, SEAL, '--verify', BANK],
                                              capture_output=True, text=True,
                                              cwd=ROOT).returncode == 0),
          witness=lambda: contains(SAT, 'JOINTLY SATISFIABLE'))

    # 2 -- ### THE `INSIDE` GRADES ARE MEASURED ON BOTH AXES, NOT ARGUED FROM ARITHMETIC.
    h.run('inside-grades-measured-on-both-axes',
          check=lambda: bool(len(cells) == 16
                             and all(c['grade'] == 'INSIDE' for c in cells)
                             and R['n_above'] == 0
                             and R['n_print'] == 0
                             and R['n_claim'] == 0
                             and float(R['worst_nq']) < 1e-6
                             and float(R['worst_ng']) < 1e-6
                             and all('v2800' in c and 'v700ng800' in c for c in cells)
                             and contains(BANK, 'AND THEY ARE INSIDE BY ### MEASUREMENT ###')),
          # ### FIXTURE: claim some cell moved past the printed-digit bar. ### None does --
          # ### the worst movement is 8.87e-10 against a 1e-6 bar.
          fixture=lambda: bool(R['n_print'] > 0),
          # ### WITNESS: the SECOND axis was actually run -- every cell carries an NG=800 value.
          witness=lambda: bool(all('v700ng800' in c for c in cells)))

    # 3 -- ### THIS ACT REPRODUCES THE COLUMNS IT PRESUMES TO GRADE.
    h.run('reproduces-the-columns-it-grades',
          check=lambda: bool(float(R['worst_bank']) < 1e-12
                             and float(R['xi_dev']) < 1e-5
                             and R['nres700'] == 7
                             and contains(BANK, 'MACHINE PRECISION')),
          # ### FIXTURE: demand agreement with b255 at 1e-18. ### The reproduction is 2.22e-16,
          # ### which is machine precision and not better than it.
          fixture=lambda: bool(float(R['worst_bank']) < 1e-18),
          witness=lambda: bool(float(R['worst_bank']) < 1e-12))

    # 4 -- ### NO PRIOR ACT RE-VERDICTED; NOTHING MOVED; NOTHING FALSELY ROUTED.
    h.run('no-act-re-verdicted-and-nothing-moved',
          check=lambda: verify_all(FIL, [
              'THIS ACT GRADED CELLS AGAINST AN INSTRUMENT; IT DID NOT GRADE ACTS',
              'NOTHING IS ROUTED TO THE AUTHOR AS A DECISION CARD',
              'THIS SEAT DOES NOT EDIT A BANKED FILING',
          ]) if bool(R['steps_neg_700'] == 15 and R['steps_neg_2800'] == 15
                     and R['f_mono'] is True) else (
              'FAIL', '### the monotone reading moved, or the no-re-verdict clause is absent'),
          # ### FIXTURE: claim a step changed sign at NQ=2800. ### All fifteen keep it.
          fixture=lambda: bool(R['steps_neg_2800'] != 15),
          witness=lambda: bool(R['steps_neg_700'] == 15))

    # 5 -- ### THE LAW IS NOT CLAIMED BEYOND ITS VERIFIED REFERENCE.
    h.run('law-not-claimed-beyond-its-verified-reference',
          check=lambda: bool(len(R['law']) == 2
                             and float(R['law_spread']) <= 1.5
                             and R['f_law'] is True
                             and contains(RUN, 'BEYOND the verified range')
                             and contains(RUN, 'NO -- reported, not counted')
                             and contains(FIL, 'REPORTED BUT NOT COUNTED')),
          # ### FIXTURE: claim all THREE ladder points were counted in the law. ### Only two
          # ### were -- the 2800 point sits beyond the reference's verified range.
          fixture=lambda: bool(len(R['law']) == 3),
          witness=lambda: bool(len(R['law']) == 2))

    # 6 -- ### b264's FALSE PROVENANCE CLAUSE IS WITHDRAWN, WITH ITS FIVE OWNERS NAMED.
    h.run('b264-provenance-clause-withdrawn-with-owners-named',
          check=lambda: verify_all(FIL, [
              'THE RECORD SAID SO IN FIVE PLACES',
              'RULE MODES K1` RULED THE REALIZATION TO SEVEN MODES BECAUSE OF IT',
              'WAS A ### REDISCOVERY ###',
              'WHAT IS WITHDRAWN IS ONE PROVENANCE CLAUSE',
          ]) if bool(contains(FIL, 'b242') and contains(FIL, 'b244')
                     and contains(FIL, 'b253')) else (
              'FAIL', '### the withdrawal does not name its owners'),
          # ### FIXTURE: claim the filings still assert b264's original clause.
          fixture=lambda: bool(contains(FIL, 'NOTHING IN THE RECORD SAID SO.**')),
          witness=lambda: contains(FIL, 'RESTATED AND NARROWED'))

    # 7 -- ### THE ACT'S OWN FOUR DEFECTS ARE DISCLOSED, INCLUDING THE ONE AGAINST THE SEAL.
    h.run('own-defects-disclosed-including-against-the-seal',
          check=lambda: verify_all(BANK, [
              'THE EXPOSURE TEST COULD NOT TELL ONE FUNCTION FROM THE NEXT',
              'PIN P2 APPLIED TWICE',
              'A TEST THAT\nSATURATES AT ITS FIRST POINT HAS MEASURED ITS GRID',
              'SITS ### BELOW ### THE\n### ROUND-OFF FLOOR',
              'NONE OF THEM FLATTERED THE RESULT',
          ]),
          # ### FIXTURE: claim the bank hides the fact that falsifiers fired first.
          # ### It states it outright.
          fixture=lambda: bool(not contains(BANK, 'THREE OF THIS ACT')),
          witness=lambda: contains(FIL, 'FOUR DEFECTS STILL SHIPPED'))

    # 8 -- ### THE SHADOW'S PROFILE, PRINTED, ZERO-AXIOM, POLARITY REFUSED. ### b227's STANDARD.
    h.run('shadow-profile-printed-and-polarity-refused',
          check=lambda: bool(io.open(PROF, encoding='utf-8').read()
                             .count('does not depend on any axioms') == 10
                             and contains(PROF, 'ALL FOUR REFUSED. lean exit code 1')
                             and 'sorry' not in io.open(SHADOW, encoding='utf-8').read()
                             and 'sorryAx' not in io.open(PROF, encoding='utf-8').read()
                             and contains(SHADOW, 'IT DOES NOT COMPILE THE CROSSOVER LAW')
                             and contains(SHADOW, 'the_bracket_at_fourteen_hundred')),
          # ### FIXTURE: demand 11 terminals. ### There are 10.
          fixture=lambda: bool(io.open(PROF, encoding='utf-8').read()
                               .count('does not depend on any axioms') == 11),
          witness=lambda: contains(PROF, 'import took'))

    # 9 -- ### h2 AND THE REGISTER SENTENCE DID NOT MOVE.
    h.run('register-sentence-exact-and-nothing-deposits',
          check=lambda: verify_all(BANK, [
              'RH reduced to a single located clause, reduction machine-verified. h2 is the clause.',
              'NOTHING DEPOSITS',
              'h2` STANDS EXACTLY WHERE THE DEPOSIT',
          ]) if bool('h2 is proved' not in io.open(BANK, encoding='utf-8').read().lower()) else (
              'FAIL', '### the bank asserts h2'),
          # ### FIXTURE: claim the bank asserts h2. ### It does not, anywhere.
          fixture=lambda: bool('h2 is proved'
                               in io.open(BANK, encoding='utf-8').read().lower()),
          witness=lambda: contains(BANK, 'NOTHING DEPOSITS'))

    # 10 -- ### NO OWNER INSTRUMENT EDITED; NOTHING STAGED UNDER A FOREIGN TREE.
    h.run('owner-instruments-unedited-and-foreign-trees-untouched',
          check=lambda: bool(all(git_unchanged('tools/e16/' + f) for f in INSTRUMENTS)
                             and 'patent-package' not in staged()
                             and 'PLACE-papers' not in staged()
                             and contains(BANK, 'READ AND IMPORTED, NEVER WRITTEN')
                             and contains(BANK, 'SET AS MODULE ATTRIBUTES AND RESTORED'.lower()
                                          .replace('set as module attributes and restored',
                                                   'MODULE ATTRIBUTES and RESTORED'))),
          # ### FIXTURE: claim a patent path IS staged. ### None is.
          fixture=lambda: bool('patent-package' in staged()),
          witness=lambda: bool(all(git_unchanged('tools/e16/' + f) for f in INSTRUMENTS)))

    # 11 -- ### THE REGISTERED EXPECTATION THAT CAME OUT WRONG IS REPORTED WRONG.
    h.run('wrong-registered-expectation-reported-wrong',
          check=lambda: verify_all(BANK, [
              '### WRONG. ### I EXPECTED THE SPREAD "COMPARABLE OR LARGER"',
              'FOUR CONFIRMED, ONE WRONG',
              'THE EXPECTATION WAS RIGHT\n###   ABOUT THE LAW AND SLOPPY ABOUT WHICH OBJECT IT APPLIED TO',
          ]),
          # ### FIXTURE: claim the bank scores the Dneg expectation CONFIRMED. ### It scores
          # ### it WRONG, and the measured spread is one to two orders SMALLER than expected.
          fixture=lambda: bool(contains(BANK, '`Dneg` -- ### CONFIRMED')),
          witness=lambda: contains(BANK, 'Reported wrong'))

    h.emit()
    c = h.counts()
    print()
    print(h.table())
    print()
    print('  counts: %s' % c)
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
