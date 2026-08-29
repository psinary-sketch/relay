# -*- coding: utf-8 -*-
"""b252_checks.py -- the b252 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### ### **EVERY CHECK BELOW IS A PURE CONJUNCTION.** ### b251's gate 4 read
### `(A and B and C and D) or E`, and `and` binds tighter than `or`, so a true `E` carried the whole
### thing. ### **THAT WAS THE THIRD APPEARANCE OF THE DECORATIVE-GATE SPECIES AND THIS FILE
### CONTAINS NO `or` IN ANY CHECK.**
### ### **AND EVERY NUMPY-VALUED PREDICATE IS `bool()`-WRAPPED** -- b242's species, which REFUSED
### three of b251's gates on the first run.

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that the settling threshold was chosen to produce the branch. ### Gates 1-2 (the hash and
###       ### the ordering) plus ### **GATE 3, WHICH RUNS THE SETTLING TEST ON ARBITRARY SEQUENCES
###       ### AND REQUIRES IT TO SEPARATE THEM.**
###   (2) that a headline figure does not match the arrays. ### Gates 4-9 RE-DERIVE every one.
###   (3) that b250's envelope leaked into a bar. ### Gate 10, a positive control on an absence.
###   (4) that a gate's NAME claimed more than it checked. ### Gate 11: G-SELF's coverage limit.
###   (5) that b251 was re-verdicted under cover of a later fact. ### Gate 12.
###   (6) that the append rewrote what it appended to. ### Gate 13.
###   (7) that an axis or a print floor moved. ### Gates 14-15.
"""
import hashlib
import io
import os
import re
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains   # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')

MEAN = os.path.join(D, 'b252_meanings.txt')
REG = os.path.join(D, 'b252_registration_2026-08-29.txt')
MODES = os.path.join(D, 'b252_modes.json')
MEAS = os.path.join(D, 'b252_measure.json')
RUN = os.path.join(D, 'b252_run.txt')
BANK = os.path.join(D, 'b252_mode_sum_limit.txt')
DOSS = os.path.join(D, 'b251_m2inf_dossier.txt')
B251 = os.path.join(D, 'b251_third_face_off.txt')
RPT = os.path.join(E16, 'b252_report.py')
INST = os.path.join(E16, 'b252_instrument.py')

MEAN_SHA = '0c562286ea9a170cb74206614bc5bb1c2560af22cb95ba8909f24ab2e04d77be'
CELLS = ['2', '3', '4', '8', '9', '12']
SETTLE_FRAC = 0.01


def _r():
    import json
    return json.load(io.open(MEAS, encoding='utf-8'))


def settled(S, frac=SETTLE_FRAC):
    """### THE REGISTERED SETTLING TEST, RE-IMPLEMENTED HERE FROM THE MEANINGS FILE'S WORDS
    ### rather than imported from the report tool -- ### **SO THAT A GATE AND THE THING IT GATES
    ### ARE NOT THE SAME CODE.**"""
    N = len(S) - 1
    m = N - N // 3
    return bool(abs(S[N] - S[m]) < frac * abs(S[N]))


def settling_test_separates():
    """### THE TAUTOLOGY CONTROL. ### **"S_N SETTLES" MUST NOT BE TRUE BY CONSTRUCTION.**

    ### The registered test is run on ARBITRARY POSITIVE SEQUENCES. ### It MUST report a `C/n`
    ### sequence as NOT settled and a geometric one as settled.
    ### ### **A SETTLING TEST THAT PASSED EVERY SEQUENCE WOULD BE MEASURING ITS OWN TOLERANCE, AND
    ### ### THE BRANCH WOULD BE AN ARTEFACT OF THE THRESHOLD RATHER THAN A FACT ABOUT THE OBJECT.**
    """
    n = np.arange(1, 22)
    harmonic = np.cumsum(1.0 / n)                 # ### must be NOT settled
    geometric = np.cumsum(0.5 ** n)               # ### must be settled
    constant = np.cumsum(np.ones(21))             # ### must be NOT settled
    return bool((not settled(harmonic)) and settled(geometric) and (not settled(constant)))


def main():
    h = Harness(ROOT, 'b252')
    r = _r()
    W = {c: np.array(r['120|120|%s|401' % c]) for c in CELLS}
    S = {c: np.cumsum(W[c]) for c in CELLS}
    rep = r['repro|2']
    b38 = np.array(rep['b38'])
    ea = np.array(rep['emul_b38vec'])
    ec = np.array(rep['emul_clean'])

    # 1 -- ### THE MEANINGS FILE IS BYTE-FOR-BYTE WHAT THE REGISTRATION BANKED.
    h.run('meanings-hash-unchanged-since-registration',
          check=lambda: bool(hashlib.sha256(io.open(MEAN, 'rb').read()).hexdigest() == MEAN_SHA
                             and contains(REG, MEAN_SHA)
                             and os.path.getsize(MEAN) == 10898),
          # ### FIXTURE: the registration's OWN bytes hashed against the meanings' hash.
          # ### FAILS ON A REAL FILE, not on a negation of the check.
          fixture=lambda: bool(hashlib.sha256(io.open(REG, 'rb').read()).hexdigest() == MEAN_SHA),
          witness=lambda: contains(REG, '0c562286'))

    # 2 -- ### MEANINGS -> REGISTRATION -> SOLVE -> MEASURE -> RUN -> VERDICT, ON DISK.
    h.run('meanings-and-registration-precede-every-computation',
          check=lambda: bool(os.path.getmtime(MEAN) < os.path.getmtime(REG)
                             < os.path.getmtime(MODES) < os.path.getmtime(MEAS)
                             < os.path.getmtime(RUN) < os.path.getmtime(BANK)),
          fixture=lambda: bool(os.path.getmtime(BANK) < os.path.getmtime(MEAN)),
          witness=lambda: bool(os.path.getsize(MEAN) > 5000))

    # 3 -- ### THE TAUTOLOGY CONTROL.
    h.run('settling-test-separates-arbitrary-sequences',
          check=settling_test_separates,
          # ### FIXTURE: the same test with a tolerance so wide it accepts EVERYTHING, including
          # ### the harmonic series. ### That is the failure mode the control exists to exclude.
          fixture=lambda: bool((not settled(np.cumsum(1.0 / np.arange(1, 22)), frac=10.0))),
          witness=lambda: contains(MEAN, 'A SETTLING TEST THAT PASSED EVERY SEQUENCE'))

    # 4 -- ### G-EXACT: `A_n(0) = 1`, THE FACT DERIVED FROM SOURCE BEFORE THE INSTRUMENT EXISTED.
    h.run('a-n-of-zero-is-one-for-every-mode',
          check=lambda: bool(abs(np.array(r['a0']['120|120']) - 1).max() < 1e-11
                             and len(r['a0']['120|120']) == 21),
          # ### FIXTURE: the same tolerance demanded of `A_n(0)` against 2 instead of 1 -- a real
          # ### quantity that genuinely fails, not a negation.
          fixture=lambda: bool(abs(np.array(r['a0']['120|120']) - 2).max() < 1e-11),
          witness=lambda: contains(MEAN, 'A_n(0) = 1, EXACTLY, FOR EVERY n'))

    # 5 -- ### G-EQ: THE VECTORS ARE EIGENVECTORS, NOT SOLVER NOISE.
    h.run('eigenfunction-equation-residual-is-machine-clean',
          check=lambda: bool(max(float(s) for s in r['eqres']['120|120']) < 1e-100),
          fixture=lambda: bool(max(float(s) for s in r['eqres']['120|120']) < 1e-125),
          witness=lambda: bool(len(r['eqres']['120|120']) == 21))

    # 6 -- ### G-REPRO-A RE-DERIVED. ### THIS ACT'S ARITHMETIC AGAINST b38's, n <= 6.
    h.run('g-repro-a-reproduces-b38-at-machine-precision',
          check=lambda: bool((abs(b38[:7] - ea[:7]) / abs(b38[:7])).max() < 1e-13),
          # ### FIXTURE: the SAME comparison over n >= 7, where it genuinely fails -- and its
          # ### failure is this act's central finding, not a defect.
          fixture=lambda: bool((abs(b38[7:11] - ec[7:11]) / abs(b38[7:11])).max() < 1e-13),
          witness=lambda: bool(len(b38) == 11))

    # 7 -- ### THE NOISE FINDING, RE-DERIVED. ### REGISTERED AT (F.1) BEFORE MEASURING.
    h.run('b38-float64-modes-past-six-are-noise',
          check=lambda: bool(abs(ec[:7] - ea[:7]).max() < 1e-5
                             and min(ec[n] / b38[n] for n in range(7, 11)) > 4.0
                             # ### b38's values WANDER; the clean ones DECAY MONOTONICALLY.
                             and (not all(b38[n] > b38[n + 1] for n in range(7, 10)))
                             and all(ec[n] > ec[n + 1] for n in range(7, 10))),
          # ### FIXTURE: claim the clean values wander too. ### They do not, and the gate must
          # ### distinguish the two behaviours rather than assert one of them.
          fixture=lambda: bool(not all(ec[n] > ec[n + 1] for n in range(7, 10))),
          witness=lambda: contains(MEAN, 'IS NOISE, AND ANY `tr[n]` BUILT FROM IT IS NOISE'))

    # 8 -- ### THE BRANCH, RE-DERIVED: NOT SETTLED AT ANY CELL, AND NOT MARGINALLY.
    h.run('diverges-wanders-at-every-cell-re-derived',
          check=lambda: bool(all(not settled(S[c]) for c in CELLS)
                             and min(abs(S[c][20] - S[c][14]) / (SETTLE_FRAC * abs(S[c][20]))
                                     for c in CELLS) > 7.0),
          # ### FIXTURE: the same battery under a 20% threshold, where cells DO settle -- so the
          # ### branch is shown to depend on the REGISTERED threshold and not on any threshold.
          fixture=lambda: bool(all(not settled(S[c], frac=0.20) for c in CELLS)),
          witness=lambda: bool(all(len(S[c]) == 21 for c in CELLS)))

    # 9 -- ### THE DECAY LAW, RE-DERIVED: `n*w(n)` RISES TOWARD A NONZERO CONSTANT.
    h.run('n-times-w-rises-to-a-nonzero-constant',
          check=lambda: bool(all(20 * W[c][20] > 17 * W[c][17] > 14 * W[c][14] > 0.4
                                 for c in CELLS)
                             # ### and it is FLATTENING: the last increment is the smallest
                             and all((20 * W[c][20] - 17 * W[c][17])
                                     < (17 * W[c][17] - 14 * W[c][14]) for c in CELLS)),
          # ### FIXTURE: demand `n*w(n) -> 0`, the falsifier the meanings file registered.
          # ### It does not, so the falsifier did not fire -- and the gate proves that.
          fixture=lambda: bool(all(20 * W[c][20] < 14 * W[c][14] for c in CELLS)),
          witness=lambda: contains(MEAN, 'FALSIFIER: IF `tr[n]` DECAYS FASTER THAN `1/n`'))

    # 10 -- ### POSITIVE CONTROL ON AN ABSENCE. ### b250's ENVELOPE NAMED AND NEVER APPLIED.
    h.run('b250-envelope-named-and-never-applied',
          check=lambda: bool(contains(RUN, '1.158e-14')
                             and contains(RUN, 'IS NOT APPLIED TO THIS SERIES AT ANY')
                             and contains(MEAN, 'NAMED AND NOT USED, AND NO BAR CARRIES IT')
                             and contains(BANK, 'named, and not used, at any point')
                             and not contains(RUN, 'tr[n] <= 1.158e-14')
                             and not contains(BANK, 'tr[n] <= 1.158e-14')),
          fixture=lambda: contains(B251, 'IS NOT APPLIED TO THIS SERIES AT ANY'),
          witness=lambda: contains(RUN, '1.158e-14'))

    # 11 -- ### A GATE'S NAME MAY NOT CLAIM MORE THAN IT CHECKED. ### G-SELF's COVERAGE LIMIT.
    h.run('g-self-coverage-limit-disclosed-and-true',
          check=lambda: bool(contains(RUN, 'THE TWO SETTINGS AGREE TO BETTER THAN 1e-6 UP TO n = 15')
                             and contains(BANK, 'SO G-SELF')
                             and contains(BANK, 'COVERS `n <= 15` AND NOT THE WHOLE RANGE')
                             # ### and the disclosure is TRUE, re-derived from the arrays
                             and (abs(np.array(r['120|120|2|401'])[:16]
                                      - np.array(r['60|100|2|401'])[:16])
                                  / abs(np.array(r['120|120|2|401'])[:16])).max() < 1e-6
                             and (abs(np.array(r['120|120|2|401'])[16]
                                      - np.array(r['60|100|2|401'])[16])
                                  / abs(np.array(r['120|120|2|401'])[16])) > 1e-6),
          fixture=lambda: bool((abs(np.array(r['120|120|2|401'])
                                    - np.array(r['60|100|2|401']))
                                / abs(np.array(r['120|120|2|401']))).max() < 1e-6),
          witness=lambda: contains(BANK, 'G-SELF'))

    # 12 -- ### b251 IS NOT RE-VERDICTED. ### THE FACT IS FILED; THE BRANCH STANDS AS BANKED.
    h.run('b251-branch-not-re-verdicted',
          check=lambda: bool(contains(BANK, 'b251')
                             and contains(BANK, 'A BANKED BRANCH IS NOT')
                             and contains(BANK, 'RE-VERDICTED BECAUSE A LATER ACT EXPLAINS IT')
                             and contains(DOSS, 'b251\'s BRANCH IS NOT RE-VERDICTED')
                             # ### and b251's own verdict text is untouched
                             and contains(B251, '(IMPOSTER-NAMED)')
                             and not contains(B251, 'b252')),
          fixture=lambda: contains(B251, 'b252'),
          witness=lambda: contains(BANK, 'b246'))

    # 13 -- ### THE APPEND DID NOT REWRITE WHAT IT APPENDED TO.
    h.run('dossier-appended-with-prefix-intact',
          check=lambda: bool(contains(DOSS, 'APPENDED AT b252')
                             and contains(DOSS, 'OPENED AND *NOT* DECIDED')
                             and contains(DOSS, 'EXPRESSES NO PREFERENCE AMONG THE THREE')
                             and contains(DOSS, 'b252 EXPRESSES NO PREFERENCE, CLOSES NOTHING')
                             and contains(DOSS, '(R-I)') and contains(DOSS, '(R-III)')),
          # ### FIXTURE: b252's own verdict bank carries no dossier appendix marker.
          fixture=lambda: contains(BANK, 'APPENDED AT b252'),
          witness=lambda: bool(os.path.getsize(DOSS) > 9000))

    # 14 -- ### THE AXES MATCH THE REGISTRATION.
    h.run('axes-match-the-registration',
          check=lambda: bool(contains(REG, 'dps 120, NQ_e = 120')
                             and contains(REG, 'dps 60, NQ_e = 100')
                             and contains(REG, 'NQ_in = 200')
                             and 'SETTINGS = [(120, 120), (60, 100)]' in
                             io.open(INST, encoding='utf-8').read()
                             and 'NQ_IN = 200' in
                             io.open(os.path.join(E16, 'b252_measure.py'),
                                     encoding='utf-8').read()),
          fixture=lambda: bool('SETTINGS = [(120, 140), (60, 100)]' in
                               io.open(INST, encoding='utf-8').read()),
          witness=lambda: contains(REG, 'NTARGET') is False)

    # 15 -- ### THE PRINT FLOORS WERE NAMED BEFORE MEASURING. ### THE b249 EXTENSION.
    h.run('print-floors-named-before-measuring',
          check=lambda: bool(contains(REG, 'PRINTS `resid47` TO FOUR DECIMALS -> PRINT FLOOR 5e-5')
                             and contains(REG, 'TO TEN SIGNIFICANT DIGITS AND `xi` TO NINE')
                             and contains(RUN, 'PRINTS resid47 TO FOUR DECIMALS -> FLOOR 5e-5')
                             and os.path.getmtime(REG) < os.path.getmtime(MEAS)),
          fixture=lambda: contains(B251, 'PRINTS `resid47` TO FOUR DECIMALS -> PRINT FLOOR 5e-5'),
          witness=lambda: contains(REG, '5e-5'))

    h.emit()
    c = h.counts()
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
