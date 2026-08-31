# -*- coding: utf-8 -*-
"""b264_checks.py -- the b264 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### ### **EVERY CHECK IS A PURE CONJUNCTION. ### NO `or` APPEARS IN ANY CHECK.**
### ### **EVERY NUMERIC PREDICATE IS `bool()`-WRAPPED.**
### ### **EVERY MULTI-NEEDLE CHECK GOES THROUGH `verify_all`, WHICH NAMES THE ABSENT NEEDLE.**
### ### **AND GATE NAMES ARE TERM-SCANNED TOO -- b262's defect, carried forward.**

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that the registration was edited after sealing. ### Gate 1 -- the SEAL verifies.
###   (2) that the envelope's constants were measured rather than derived. ### Gate 2.
###   (3) that a verdict rests on a falsifier implemented differently from how it was sealed.
###       ### Gate 3 -- F1's ABSOLUTE VALUE, and the one-sided defect DISCLOSED not hidden.
###   (4) that cells were counted converged on an axis that cannot see the error that binds.
###       ### Gate 4 -- the SECOND axis exists, and the rejected cells are named.
###   (5) that the ceiling was inherited as a number rather than measured, or mis-attributed.
###       ### Gate 5 -- `EPS_NQ` named as the binding one, `EPS_NG` shown NOT to depart.
###   (6) that F6 was read on modes the instrument cannot compute. ### Gate 6 -- the
###       ### resolution boundary is MEASURED, and the near-miss is disclosed against itself.
###   (7) that b263's branch was DECIDED rather than borne on. ### Gate 7.
###   (8) that a compile was claimed without a printed profile. ### Gate 8 -- b227's standard.
###   (9) that h2 moved, or that a refused misreading crept back. ### Gate 9.
###  (10) that an owner instrument was edited or the patent tree swept in. ### Gate 10.
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

REG = os.path.join(D, 'b264_registration_2026-08-31.txt')
BANK = os.path.join(D, 'b264_eps_even_decay.txt')
FIL = os.path.join(D, 'b264_filings.txt')
RUN = os.path.join(D, 'b264_run.txt')
ROWS = os.path.join(D, 'b264_rows.json')
PROF = os.path.join(D, 'b264_shadow_profile.txt')
SHADOW = os.path.join(RES, 'Core', 'ArchimedeanTwinShadow.lean')
SEAL = os.path.join(ROOT, 'tools', 'reg_seal.py')
SRC = os.path.join(E16, 'b264_eps_decay.py')

INSTRUMENTS = ['b38_act10.py', 'qeps_layer.py', 'carto_atlas.py', 'prolate_layer.py',
               'b261_e2even.py']


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
    h = Harness(repo_root=ROOT, act='b264')
    R = json.load(io.open(ROWS, encoding='utf-8'))
    lad = R['ladder']
    conv = [r for r in lad if r['rel_conv'] <= 1e-8 and r['rel_convq'] <= 1e-8]
    ngonly = [r for r in lad if r['rel_conv'] <= 1e-8 and r['rel_convq'] > 1e-8]

    # 1 -- ### THE SEAL VERIFIES, AND THE ACT'S DEVIATIONS FROM IT ARE DECLARED.
    h.run('registration-sealed-and-every-deviation-declared',
          check=lambda: verify_all(BANK, [
              'CLAUSE (I) WAS INTERNALLY UNSATISFIABLE AS WRITTEN',
              'F1 WAS IMPLEMENTED ONE-SIDED AND THE REGISTRATION IS NOT',
              'THE REGISTERED CONVERGENCE TEST CANNOT SEE',
              'THE REGISTERED LADDER TARGET `x >= 1000` IS NOT MET',
          ]) if bool(seal_ok()[0] and 'SEAL INTACT' in seal_ok()[1]) else (
              'FAIL', '### the registration seal does not verify'),
          # ### FIXTURE: the BANK carries no seal block, so verifying IT must FAIL (exit 1).
          fixture=lambda: bool(subprocess.run([sys.executable, SEAL, '--verify', BANK],
                                              capture_output=True, text=True,
                                              cwd=ROOT).returncode == 0),
          witness=lambda: bool(seal_ok()[0]))

    # 2 -- ### THE ENVELOPE'S CONSTANTS ARE DERIVED FROM `lam` ALONE, NOT MEASURED.
    h.run('envelope-constants-derived-not-measured',
          check=lambda: bool(abs(R['C_even'] - 132.781908429) < 1e-6
                             and R['f1_master'] == 0
                             and len([r for r in conv
                                      if abs(r['eps_even']) - r['env'] > 1e-9]) == 0
                             and float(R['env_tightness']) < 1.0
                             and contains(BANK, 'IT CONTAINS NO ENDPOINT VALUE `xi_n(1)^2`')
                             and contains(BANK, 'ROUTES AROUND')),
          # ### FIXTURE: claim the envelope is VIOLATED somewhere on the master curve.
          # ### It is violated nowhere -- 0 of 1210 points.
          fixture=lambda: bool(R['f1_master'] > 0),
          # ### WITNESS: the bound is LOOSE and is reported loose -- tightness < 1 means the
          # ### curve never reaches its own envelope.
          witness=lambda: bool(float(R['env_tightness']) < 1.0))

    # 3 -- ### F1 IS THE SEALED FALSIFIER (ABSOLUTE VALUE), AND THE ONE-SIDED DEFECT IS DISCLOSED.
    h.run('f1-tested-on-absolute-value-and-the-defect-disclosed',
          check=lambda: verify_all(BANK, [
              'WITH the absolute\nvalue',
              'THAT WAS THE ONLY REASON F1 DID NOT FIRE ON THE FIRST RUN',
              'THE FIRST RUN\'S `(DECAYS)` WAS THEREFORE UNSOUND WHEN PRINTED',
          ]) if bool(contains(RUN, 'violations (|eps_even| - C_even/rho')
                     and contains(FIL, 'A DEFECT SET THAT LEANS ENTIRELY ONE WAY')) else (
              'FAIL', '### the run does not test F1 on |eps_even|, or the defect is undisclosed'),
          # ### FIXTURE: claim the run still carries the ONE-SIDED test. ### It does not:
          # ### the printed line reads `|eps_even| - C_even/rho`.
          fixture=lambda: bool(contains(RUN, 'violations (eps_even - C_even/rho')),
          witness=lambda: contains(RUN, 'violations (|eps_even| - C_even/rho'))

    # 4 -- ### THE SECOND CONVERGENCE AXIS EXISTS AND THE CELLS IT REJECTS ARE NAMED.
    h.run('second-convergence-axis-rejects-and-names-its-cells',
          check=lambda: bool(len(ngonly) == 5
                             and all(r['rel_conv'] <= 1e-8 for r in ngonly)
                             and all(r['rel_convq'] > 1e-8 for r in ngonly)
                             and len(conv) == 6
                             and contains(RUN, 'THE CELLS THE REGISTERED TEST ALONE WOULD HAVE PASSED')
                             and contains(RUN, 'A FALSE PASS, NOT A LOOSE ONE')),
          # ### FIXTURE: claim the rejected cells FAILED the registered NG axis too. ### They did
          # ### not -- every one of them PASSED `NG` vs `2 NG` at ~1e-12 while being wrong by
          # ### orders of magnitude. ### **THAT IS THE WHOLE POINT OF THE GATE.**
          fixture=lambda: bool(any(r['rel_conv'] > 1e-8 for r in ngonly)),
          witness=lambda: bool(len(ngonly) == 5))

    # 5 -- ### THE CEILING IS MEASURED, AND ATTRIBUTED TO `EPS_NQ` RATHER THAN `EPS_NG`.
    h.run('ceiling-measured-and-attributed-to-nq-not-ng',
          check=lambda: bool(abs(R['ceiling_nq'] - 238.4) < 1.0
                             and R['ceiling_rho'] is None
                             and contains(RUN, 'THE `EPS_NG = 400` CEILING IS NOT THE')
                             and contains(BANK, 'IT IS NOT THE CEILING THIS ACT WAS SENT TO MEASURE')
                             and contains(FIL, 'RAISING `NG` DOES NOT REPAIR IT')
                             and contains(FIL, 'W-ORD-NQ-CEILING')),
          # ### FIXTURE: claim `NG = 400` DID depart on some valid cell. ### It departs on none
          # ### -- `ceiling_rho` is None precisely because no VALID cell shows a departure.
          fixture=lambda: bool(R['ceiling_rho'] is not None),
          witness=lambda: bool(R['ceiling_nq'] > 200.0))

    # 6 -- ### F6 IS READ ONLY WHERE IT CAN BE READ, AND THE NEAR-MISS IS DISCLOSED.
    h.run('f6-read-on-resolved-modes-and-the-near-miss-disclosed',
          check=lambda: verify_all(FIL, [
              'THAT WOULD\n### HAVE BEEN WRONG',
              'PIN P1 IS NOT IMPEACHED BY THIS ACT',
              'A PRE-AUTHORISED\n### HEADLINE IS EXACTLY THE THING AN ACT WILL REACH FOR',
          ]) if bool(R['nres'] == 7
                     and R['f6'] is True
                     and contains(RUN, 'NOISE FLOOR -- not an eigenvalue')) else (
              'FAIL', '### F6 was not read on the resolved modes, or the near-miss is undisclosed'),
          # ### FIXTURE: claim all eleven modes are resolved. ### Four are at `sqrt(eps)` and
          # ### MOVE when `NQ` moves, which no eigenvalue does.
          fixture=lambda: bool(R['nres'] == 11),
          witness=lambda: bool(R['nres'] == 7))

    # 7 -- ### b263's BRANCH IS BORNE ON, NOT DECIDED.
    h.run('b263-branch-borne-on-never-decided',
          check=lambda: verify_all(BANK, [
              'BEARING, NEVER DECISION',
              '`E2even` IS NOT THE OBJECT THAT ABSORBS `J`',
              'AND IT IS ### NOT ### "THE ARCHIMEDEAN SIDE"',
              'THE BRANCH IS NOT DECIDED',
          ]) if bool(contains(FIL, 'b263\'s sentence stands EXACTLY as b263 wrote it')
                     and contains(BANK, 'W-ORD-TQ-IDENTIFY` IS OPEN')) else (
              'FAIL', '### the bearing is stated as a decision, or TQ-IDENTIFY is not inherited'),
          # ### FIXTURE: claim the bank DECIDES the branch. ### It says the opposite, twice.
          fixture=lambda: bool(contains(BANK, 'THE BRANCH IS DECIDED')),
          witness=lambda: contains(BANK, 'BEARING, NEVER DECISION'))

    # 8 -- ### THE SHADOW'S PROFILE, PRINTED, ZERO-AXIOM, POLARITY REFUSED. ### b227's STANDARD.
    h.run('shadow-profile-printed-and-polarity-refused',
          check=lambda: bool(io.open(PROF, encoding='utf-8').read()
                             .count('does not depend on any axioms') == 12
                             and contains(PROF, 'ALL FOUR REFUSED. lean exit code 1')
                             and 'sorry' not in io.open(SHADOW, encoding='utf-8').read()
                             and 'sorryAx' not in io.open(PROF, encoding='utf-8').read()
                             and contains(SHADOW, 'the_sign_law_over_the_eleven_indices')
                             and contains(SHADOW, 'THIS FILE PROVES THE ARITHMETIC AND')
                             and contains(BANK, 'TWELVE TERMINALS')),
          # ### FIXTURE: demand 13 terminals. ### There are 12.
          fixture=lambda: bool(io.open(PROF, encoding='utf-8').read()
                               .count('does not depend on any axioms') == 13),
          witness=lambda: contains(PROF, 'import took'))

    # 9 -- ### h2 AND THE REGISTER SENTENCE DID NOT MOVE; THE FOUR MISREADINGS ARE REFUSED.
    h.run('register-sentence-exact-and-four-misreadings-refused',
          check=lambda: verify_all(BANK, [
              'RH reduced to a single located clause, reduction machine-verified. h2 is the clause.',
              'NOT evidence against the identity',
              'it does NOT move `h2`',
              'it does NOT say `Theta_q`\n### is the wrong object',
              'NOTHING DEPOSITS',
          ]) if bool('h2 is proved' not in io.open(BANK, encoding='utf-8').read().lower()) else (
              'FAIL', '### the bank asserts h2'),
          # ### FIXTURE: claim the bank asserts h2. ### It does not, anywhere.
          fixture=lambda: bool('h2 is proved'
                               in io.open(BANK, encoding='utf-8').read().lower()),
          witness=lambda: contains(BANK, 'NOTHING DEPOSITS'))

    # 10 -- ### NO OWNER INSTRUMENT EDITED; NOTHING STAGED UNDER THE PATENT OR PAPERS TREES.
    h.run('owner-instruments-unedited-and-foreign-trees-untouched',
          check=lambda: bool(all(git_unchanged('tools/e16/' + f) for f in INSTRUMENTS)
                             and 'patent-package' not in staged()
                             and 'PLACE-papers' not in staged()
                             and contains(FIL, 'STAGING IS BY EXPLICIT PATH')
                             and contains(BANK, 'READ AND IMPORTED, NEVER WRITTEN')),
          # ### FIXTURE: claim a patent path IS staged. ### None is.
          fixture=lambda: bool('patent-package' in staged()),
          witness=lambda: bool(all(git_unchanged('tools/e16/' + f) for f in INSTRUMENTS)))

    # 11 -- ### THE REGISTERED EXPECTATIONS THAT CAME OUT WRONG ARE REPORTED WRONG.
    # ### ### **THIS GATE EXISTS BECAUSE AN ACT THAT SCORES ITS OWN PREDICTIONS HAS EVERY
    # ### ### INCENTIVE TO SCORE THE MISSES QUIETLY.**
    h.run('wrong-registered-expectations-reported-wrong',
          check=lambda: verify_all(FIL, [
              'S2 (sharp-rate half) -- ### WRONG, AND WRONG IN ITS REASON',
              'S3 -- ### WRONG',
              'THE ACT WAS SENT TO MEASURE A CEILING AND FOUND THAT CEILING IS NOT THE ONE THAT',
          ]) if bool(contains(BANK, 'CAME OUT WRONG AND IS REPORTED')) else (
              'FAIL', '### a registered expectation that failed is not reported as failed'),
          # ### FIXTURE: claim the filings score S3 as CONFIRMED. ### They score it WRONG.
          fixture=lambda: bool(contains(FIL, 'S3 -- CONFIRMED')),
          witness=lambda: contains(FIL, 'TWO CONFIRMED, ONE WRONG'))

    h.emit()
    c = h.counts()
    print()
    print(h.table())
    print()
    print('  counts: %s' % c)
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
