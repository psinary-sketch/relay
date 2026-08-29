# -*- coding: utf-8 -*-
"""b254_checks.py -- the b254 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### ### **EVERY CHECK IS A PURE CONJUNCTION; NO `or` APPEARS IN ANY CHECK** (b251's gate 4, the
### decorative-gate species). ### **EVERY NUMPY-VALUED PREDICATE IS `bool()`-WRAPPED** (b242's).

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that the branch is an artefact of the bar. ### Gates 4-5 re-derive it from the arrays and
###       ### **GATE 3 IS THE TAUTOLOGY CONTROL: the composition holds on ARBITRARY values (so it
###       ### is restatement and no evidence) while the SIGN PROFILE does NOT (so it has content).**
###   (2) that a realization was quietly chosen. ### Gate 8.
###   (3) that deficit language crept in under R-III. ### Gate 11, a positive control on an absence.
###   (4) that the rider's mis-citations were softened. ### Gate 10 checks them against b246's text.
###   (5) that the QUOTED-N law was preached and not observed. ### Gate 13.
###   (6) that a prediction that did not fire got claimed anyway. ### Gate 9.
"""
import hashlib
import io
import os
import re
import subprocess
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains   # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')

MEAN = os.path.join(D, 'b254_meanings.txt')
REG = os.path.join(D, 'b254_registration_2026-08-29.txt')
CACHE = os.path.join(D, 'b254_cache.npz')
RUN = os.path.join(D, 'b254_run.txt')
BANK = os.path.join(D, 'b254_fourth_face_off.txt')
B246 = os.path.join(D, 'b246_two_tails.txt')
B251 = os.path.join(D, 'b251_third_face_off.txt')
B253 = os.path.join(D, 'b253_m2inf_ruling.txt')
TOOL = os.path.join(E16, 'b254_faceoff.py')

MEAN_SHA = '75e731e3ab44e9786fc093d7a6a7ae433c8a09d2957ea41eb1ce77b7b0d5cb97'
CELLS = ['2', '3', '4', '8', '9', '12']
NQS = (500, 700, 900, 1100)


def cells():
    """### RE-DERIVE EVERY HEADLINE FIGURE FROM THE CACHED ARRAYS, NOT FROM THE ACT'S PROSE."""
    c = dict(np.load(CACHE, allow_pickle=True))
    mask = float(np.max(np.abs(c['ee_modes'].sum(0) - c['ee_full'])))
    out = []
    for lab in CELLS:
        A, PR, Thq, E2 = c['c_%s' % lab]
        E2n = c['c_%s_E2n' % lab]
        dn = {q: float(c['c_%s_tr_%d' % (lab, q)][1:11:2].sum()) for q in NQS}
        out.append(dict(lab=lab, A=A, PR=PR, Thq=Thq, E2=E2,
                        E2even=float(E2n[0::2].sum()), E2odd=float(E2n[1::2].sum()),
                        dn=dn, dneg=dn[700],
                        dbar=max(abs(dn[q] - dn[700]) for q in NQS), mask=mask))
    return out


def resid(r, which):
    d = r['E2odd'] if which == 'A' else r['dneg']
    return (d - r['E2']) - (r['PR'] - r['Thq'])


def bar(r, which):
    import math
    b = r['mask'] if which == 'A' else r['dbar']
    return math.sqrt(b ** 2 + r['mask'] ** 2)


def composition_is_restatement_but_profile_is_not():
    """### THE TAUTOLOGY CONTROL, BOTH HALVES.

    ### HALF ONE: `L - R == (E2 - D) + (PR - Thq)` must hold on ARBITRARY values, with
    ### `L = (A + E2 - D) - Thq` and `R = A - PR`. ### **THAT PROVES IT IS RESTATEMENT AND
    ### THEREFORE NO EVIDENCE**, which the meanings file said before the run.
    ### HALF TWO: the SIGN of the residual must NOT be determined by that algebra -- on arbitrary
    ### values it must take BOTH signs. ### ### **OTHERWISE "UNIFORMLY NEGATIVE AT TWELVE ENTRIES"
    ### ### WOULD BE A PROPERTY OF THE FORMULA RATHER THAN OF THE OPERATOR.**
    """
    import random
    rng = random.Random(20260829)
    ok, saw_pos, saw_neg = True, False, False
    for _ in range(500):
        A, E2, Dm, PR, Thq = (rng.uniform(-9, 9) for _ in range(5))
        L, R = (A + E2 - Dm) + (-Thq), A - PR
        ok &= abs((L - R) - ((E2 - Dm) + (PR - Thq))) < 1e-9
        s = (Dm - E2) - (PR - Thq)
        saw_pos |= s > 0
        saw_neg |= s < 0
    return bool(ok and saw_pos and saw_neg)


def deficit_language_absent():
    """### R-III GOVERNS THE VOCABULARY: ### **NO DEFICIT LANGUAGE.**

    ### The word DOES appear in this act -- in the RULE that forbids it and in explicit denials.
    ### ### **A SCAN THAT BANNED THE TOKEN OUTRIGHT WOULD HAVE BANNED THE RULE'S OWN STATEMENT**,
    ### so the test is that every occurrence sits inside a NEGATION or a QUOTATION, and none
    ### describes the measured residual.
    """
    t = io.open(BANK, encoding='utf-8').read()
    hits = [m for m in re.finditer(r'[Dd]eficit', t)]
    if not hits:
        return False          # ### the rule must be STATED, so zero hits is itself wrong
    for m in hits:
        seg = t[max(0, m.start() - 160):m.end() + 60]
        if not re.search(r'\bNO\b|\bnot\b|\bNOT\b|neither', seg):
            return False
    return True


def main():
    h = Harness(ROOT, 'b254')
    C = cells()

    # 1 -- ### THE MEANINGS FILE IS BYTE-FOR-BYTE WHAT THE REGISTRATION BANKED.
    h.run('meanings-hash-unchanged-since-registration',
          check=lambda: bool(hashlib.sha256(io.open(MEAN, 'rb').read()).hexdigest() == MEAN_SHA
                             and contains(REG, MEAN_SHA)
                             and os.path.getsize(MEAN) == 11666),
          # ### FIXTURE: the registration's OWN bytes hashed against the meanings' hash.
          # ### FAILS ON A REAL FILE, not on a negation of the check.
          fixture=lambda: bool(hashlib.sha256(io.open(REG, 'rb').read()).hexdigest() == MEAN_SHA),
          witness=lambda: contains(REG, '75e731e3'))

    # 2 -- ### MEANINGS -> REGISTRATION -> RUN -> VERDICT, IN THAT ORDER ON DISK.
    h.run('meanings-and-registration-precede-the-run',
          check=lambda: bool(os.path.getmtime(MEAN) < os.path.getmtime(REG)
                             < os.path.getmtime(RUN) < os.path.getmtime(BANK)),
          fixture=lambda: bool(os.path.getmtime(BANK) < os.path.getmtime(MEAN)),
          witness=lambda: bool(os.path.getsize(MEAN) > 5000))

    # 3 -- ### THE TAUTOLOGY CONTROL, BOTH HALVES.
    h.run('composition-is-restatement-but-sign-profile-is-not',
          check=composition_is_restatement_but_profile_is_not,
          # ### FIXTURE: the vacuous form -- `x == x` on a real cell, true for every input.
          fixture=lambda: bool(abs(C[0]['E2'] - C[0]['E2']) > 1e-30),
          witness=lambda: contains(MEAN, 'AN IDENTITY THAT CANNOT FAIL\n### ### ### CANNOT '
                                         'TESTIFY'))

    # 4 -- ### THE BRANCH RE-DERIVED: (IMBALANCED) AT EVERY CELL UNDER BOTH REALIZATIONS.
    h.run('imbalanced-at-every-cell-under-both-realizations',
          check=lambda: bool(all(abs(resid(r, 'A')) > bar(r, 'A') for r in C)
                             and all(abs(resid(r, 'B')) > bar(r, 'B') for r in C)),
          # ### FIXTURE: the same battery with bars inflated 100x. ### At that width realization
          # ### (B)'s marginal `a^2 = 2` cell (1.50x) falls INSIDE, so the branch is shown to
          # ### depend on the REGISTERED bar and not on any bar.
          fixture=lambda: bool(all(abs(resid(r, 'B')) > 100 * bar(r, 'B') for r in C)),
          witness=lambda: bool(len(C) == 6))

    # 5 -- ### THE SIGN PROFILE RE-DERIVED. ### TWELVE ENTRIES, ONE SIGN.
    h.run('sign-uniformly-negative-across-twelve-entries',
          check=lambda: bool(all(resid(r, w) < 0 for r in C for w in ('A', 'B'))
                             and contains(BANK, 'SIX CELLS, TWO')
                             and contains(BANK, 'REALIZATIONS, TWELVE ENTRIES, ONE SIGN')),
          # ### FIXTURE: claim uniform POSITIVITY -- a real property that genuinely fails.
          fixture=lambda: bool(all(resid(r, w) > 0 for r in C for w in ('A', 'B'))),
          witness=lambda: bool(len(C) * 2 == 12))

    # 6 -- ### THE PURE-ARCHIMEDEAN CELL: `PR = Theta_q = 0` EXACTLY, RE-DERIVED.
    h.run('pure-archimedean-cell-has-primes-identically-zero',
          check=lambda: bool(C[0]['lab'] == '2' and C[0]['PR'] == 0.0 and C[0]['Thq'] == 0.0
                             and abs(resid(C[0], 'A') + C[0]['E2even']) < 1e-12
                             and contains(RUN, 'PURE-ARCHIMEDEAN CELL')),
          # ### FIXTURE: demand the SAME of `a^2 = 3`, where `PR = 0.106484` -- a real cell that
          # ### genuinely fails, so the flag is shown to mark something.
          fixture=lambda: bool(C[1]['PR'] == 0.0 and C[1]['Thq'] == 0.0),
          witness=lambda: bool(C[0]['E2even'] > 0.5))

    # 7 -- ### THE STRUCTURAL FINDING: UNDER (A) NOTHING IN THE BALANCE MOVES WITH `NQ`.
    h.run('realization-a-carries-no-mode-sum',
          check=lambda: bool(all(r['dbar'] > 1e-3 for r in C)          # ### (B) DOES move
                             and contains(BANK, 'NOTHING IN THE BALANCE IS A MODE SUM')
                             and contains(RUN, 'DO NOT')
                             and contains(RUN, 'MOVE WITH `NQ` AT ALL')
                             # ### and (A)'s bar is the mask certificate alone
                             and all(abs(bar(r, 'A') - r['mask'] * 2 ** 0.5) < 1e-18 for r in C)),
          # ### FIXTURE: claim (B) is ALSO NQ-independent. ### It is not -- its spread runs
          # ### 1.6e-2 to 4.1e-2 -- so a gate that accepted it would be reading no arrays at all.
          fixture=lambda: bool(all(r['dbar'] < 1e-6 for r in C)),
          witness=lambda: bool(C[0]['mask'] < 1e-10))

    # 8 -- ### NEITHER REALIZATION WAS CHOSEN, AND THE DISAGREEMENT IS RE-DERIVED.
    h.run('both-realizations-computed-and-neither-chosen',
          check=lambda: bool(abs(resid(C[0], 'A') / resid(C[0], 'B')) > 10.0
                             and contains(BANK, 'COMPUTED BOTH AND CHOSE NEITHER')
                             and contains(MEAN, 'THIS ACT COMPUTES *BOTH* COLUMNS AND CHOOSES')
                             and contains(B246, 'this act computed both rather than choosing')),
          # ### FIXTURE: claim the two realizations agree to 10% -- they differ by 16.3x at
          # ### `a^2 = 2`, so this fails on the real arrays.
          fixture=lambda: bool(abs(resid(C[0], 'A') / resid(C[0], 'B')) < 1.1),
          witness=lambda: bool(abs(resid(C[0], 'B')) > 0))

    # 9 -- ### A PREDICTION WHOSE CONDITION DID NOT FIRE IS NOT CLAIMED.
    #      ### **THE EASIEST SELF-FLATTERY AVAILABLE TO THIS ACT.**
    h.run('unfired-prediction-reported-as-unfired',
          check=lambda: bool(contains(MEAN, 'IF THE TWO REALIZATIONS DISAGREE ENOUGH TO FLIP THE '
                                            'BRANCH')
                             and contains(BANK, 'THEY DO NOT FLIP THE BRANCH')
                             and contains(BANK, 'I DO NOT GET TO PROMOTE THE')
                             # ### and it is TRUE: both realizations give the same branch
                             and all(abs(resid(r, 'A')) > bar(r, 'A')
                                     and abs(resid(r, 'B')) > bar(r, 'B') for r in C)
                             # ### and the "shrinking" mis-word is owned
                             and contains(BANK, 'IT DOES NOT SHRINK MONOTONICALLY')),
          fixture=lambda: contains(B251, 'THEY DO NOT FLIP THE BRANCH'),
          witness=lambda: contains(MEAN, 'OUTRANKS THE BRANCH ITSELF'))

    # 10 -- ### THE RIDER'S MIS-CITATIONS, CHECKED AGAINST b246's OWN TEXT.
    h.run('rider-miscitations-recorded-and-true',
          # ### THIS GATE'S FIRST FORM RESTED ON A FALSE PREMISE AND ### **THE HARNESS REFUSED IT**:
          # ### its fixture `contains(b246, "by mode 6")` PASSED, because b246 contains BOTH
          # ### phrases, in two different sentences about two different quantities.
          # ### ### **THAT REFUSAL IS EXACTLY WHAT MUST-FAIL FIXTURES EXIST FOR, AND WHAT IT
          # ### ### CAUGHT WAS THIS ACT'S OWN CHARGE AGAINST THE FERRY.**
          # ### The gate now checks the CORRECTED position: both phrases are in b246, particular
          # ### (ii) is WITHDRAWN in the bank, and the hash-gated meanings file is left as banked.
          check=lambda: bool(contains(B246, 'by mode 7')
                             and contains(B246, 'CONVERGED BY MODE 6')
                             and contains(B246, 'this act computed both rather than choosing')
                             and contains(B246, '5.481e-13')
                             and contains(BANK, 'WITHDRAWN. ### THIS PARTICULAR WAS WRONG')
                             and contains(BANK, 'HAS *NOT* BEEN EDITED')
                             and contains(BANK, 'FUSES TWO SEPARATE b246 SENTENCES INTO ONE')
                             and contains(BANK, 'THAT IS THE ERROR, AND IT IS MINE')
                             and contains(BANK, 'A COUNT OF THREE CORRECTIONS BECAME A COUNT OF '
                                                'TWO')),
          # ### FIXTURE: claim b246 LACKS the ledger-row phrase. ### It has it, so this fails on
          # ### the real file rather than on a negation of the check.
          fixture=lambda: bool(not contains(B246, 'by mode 7')),
          witness=lambda: contains(MEAN, '3.9e-16'))

    # 11 -- ### POSITIVE CONTROL ON AN ABSENCE. ### NO DEFICIT LANGUAGE UNDER R-III.
    h.run('no-deficit-language-only-its-prohibition',
          check=deficit_language_absent,
          # ### FIXTURE: the naive form -- ban the TOKEN outright. ### That fails, because the
          # ### rule forbidding deficit language must itself say the word.
          fixture=lambda: bool(not re.search(r'[Dd]eficit',
                                             io.open(BANK, encoding='utf-8').read())),
          witness=lambda: bool(len(re.findall(r'[Dd]eficit',
                                              io.open(BANK, encoding='utf-8').read())) > 0))

    # 12 -- ### NO EARLIER ACT IS RE-VERDICTED, AND THE IDENTITY IS NEITHER REFUTED NOR PROVED.
    h.run('no-re-verdicts-and-no-global-claim',
          check=lambda: bool(contains(BANK, 'IT IS NOT EVIDENCE AGAINST THE IDENTITY')
                             and contains(BANK, 'DECIDES\n### **NOTHING GLOBAL.**')
                             and contains(BANK, 'It did not re-verdict b251, b252 or b253')
                             and contains(BANK, 'neither refuted nor')
                             # ### THIS GATE'S FIRST FORM DEMANDED b253 NOT MENTION b254. ### IT
                             # ### DOES -- b253 PREPARED THE FORK AND NAMED b254 FOUR TIMES -- SO
                             # ### THE FIXTURE PASSED AND ### **THE HARNESS REFUSED THE CHECK.**
                             # ### The real claim is that the EARLIER BANKS ARE UNTOUCHED BY THIS
                             # ### ACT, and that is a structural fact git can answer.
                             and subprocess.run(
                                 ['git', '-C', ROOT, 'diff', '--quiet', 'HEAD', '--',
                                  'data/b251_third_face_off.txt',
                                  'data/b253_m2inf_ruling.txt']).returncode == 0),
          # ### FIXTURE: demand the SAME of this act's OWN bank, which is new and untracked --
          # ### a real file whose state genuinely differs.
          fixture=lambda: bool(subprocess.run(
              ['git', '-C', ROOT, 'status', '--porcelain', '--',
               'data/b254_fourth_face_off.txt'],
              capture_output=True).stdout.decode().strip() == ''),
          witness=lambda: contains(BANK, 'b15'))

    # 13 -- ### b253's QUOTED-N LAW IS OBSERVED, NOT MERELY CITED.
    h.run('quoted-n-law-observed-in-this-act',
          check=lambda: bool(contains(B253, 'THE QUOTED-N LAW')
                             and contains(BANK, 'Dneg(N = 11, float64 modes,')
                             and contains(BANK, 'suspect above n = 6)')
                             and contains(REG, '(N = 11, float64 modes, suspect above')),
          # ### FIXTURE: b246 predates the law and carries no such qualifier.
          fixture=lambda: contains(B246, 'Dneg(N = 11, float64 modes,'),
          witness=lambda: contains(B253, 'UNGRADED'))

    # 14 -- ### THE AXES MATCH THE REGISTRATION, AND b250's ENVELOPE IS NAMED AND NOT APPLIED.
    h.run('axes-match-and-envelope-named-not-applied',
          check=lambda: bool(contains(REG, 'NQ = 1100')
                             and 'NQS = (500, 700, 900, 1100)' in
                             io.open(TOOL, encoding='utf-8').read()
                             and 'NMODE = 11' in io.open(TOOL, encoding='utf-8').read()
                             and contains(RUN, '1.158e-14')
                             and contains(RUN, 'NAMED AND NOT APPLIED TO ANY SERIES HERE')
                             and not contains(RUN, 'Delta_- <= 1.158e-14')),
          fixture=lambda: bool('NQS = (500, 700, 900, 1300)' in
                               io.open(TOOL, encoding='utf-8').read()),
          witness=lambda: contains(REG, 'EPS_NRHO = 240'))

    h.emit()
    c = h.counts()
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
