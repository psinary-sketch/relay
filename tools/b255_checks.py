# -*- coding: utf-8 -*-
"""b255_checks.py -- the b255 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**.

### ### **EVERY CHECK IS A PURE CONJUNCTION; NO `or` APPEARS IN ANY CHECK.** ### **EVERY NUMERIC
### PREDICATE IS `bool()`-WRAPPED.**

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that the ladder was chosen by what its values do. ### Gates 2-3: the PRICING precedes
###       ### everything on disk and ### **ITS BANK CARRIES NO BALANCE VALUE AT ALL** (gate 3 is a
###       ### positive control on an absence).
###   (2) that a trend got extrapolated. ### Gate 10, another positive control on an absence.
###   (3) that the sawtooth is an artefact of the algebra. ### **GATE 4 IS THE TAUTOLOGY CONTROL
###       ### AND IT HAS TO SEPARATE TWO THINGS: the residual's NEGATIVITY *is* forced once both
###       ### terms are positive (restatement), while the STAIRCASE CORRELATION is not.**
###   (4) that a wrong prediction got quietly upgraded. ### Gate 11.
###   (5) that the grid rebuild was adopted silently. ### Gate 8.
"""
import hashlib
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains   # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')

PRICE = os.path.join(D, 'b255_pricing.txt')
MEAN = os.path.join(D, 'b255_meanings.txt')
REG = os.path.join(D, 'b255_registration_2026-08-29.txt')
RUN = os.path.join(D, 'b255_run.txt')
BANK = os.path.join(D, 'b255_limit_profile.txt')
ROWS = os.path.join(D, 'b255_rows.json')
B254 = os.path.join(D, 'b254_fourth_face_off.txt')
B253 = os.path.join(D, 'b253_m2inf_ruling.txt')
PTOOL = os.path.join(E16, 'b255_pricing.py')

MEAN_SHA = '2c7faef1a72a7fe21928f5ad1d416ab0053d4bbfe54066e7cd7c70afa5c67864'
LADDER = [2, 3, 4, 8, 9, 12, 16, 20, 25, 32, 36, 45, 50, 64, 81, 100]
BAND = 1e-4
B254_TAB = {2: (1.001814, 0.677615, 0.000000, 0.000000, -1.001814),
            3: (0.910943, 0.605701, 0.106484, 0.000000, -1.017427),
            4: (0.834033, 0.540018, 0.249320, 0.161978, -0.921374),
            8: (0.685514, 0.410725, 0.561045, 0.317018, -0.929542),
            9: (0.665133, 0.393176, 0.608882, 0.473862, -0.800154),
            12: (0.620090, 0.354973, 0.714334, 0.518491, -0.815933)}


def rows():
    """### RE-DERIVE EVERY HEADLINE FIGURE FROM THE RUN'S ARRAYS, NOT FROM THE ACT'S PROSE."""
    r = json.load(io.open(ROWS, encoding='utf-8'))
    return [r[str(a2)] for a2 in LADDER]


def stepped(prev, cur):
    return [prev['stair'][p] for p in ('2', '3', '5')] != [cur['stair'][p] for p in ('2', '3', '5')]


def sawtooth_is_not_forced():
    """### THE TAUTOLOGY CONTROL, AND IT MUST SEPARATE TWO CLAIMS THAT LOOK ALIKE.

    ### HALF ONE -- ### **THE RESIDUAL'S NEGATIVITY *IS* FORCED** ### once `E2even > 0` and
    ### `junction > 0`, because `resid = -(E2even + junction)`. ### On ARBITRARY positive pairs it
    ### is negative every time. ### **SO "ALL THIRTY-TWO ENTRIES NEGATIVE" IS RESTATEMENT GIVEN
    ### THE SIGNS OF THE TERMS, AND THE BANK SAYS SO IN SECTION (C) RATHER THAN COUNTING IT.**
    ### HALF TWO -- ### **THE STAIRCASE CORRELATION IS NOT FORCED.** ### On arbitrary junction
    ### sequences, "rises between steps and falls at steps" fails. ### **SO THE SAWTOOTH IS A FACT
    ### ABOUT THE OPERATOR AND NOT ABOUT THE FORMULA.**
    """
    import random
    rng = random.Random(20260829)
    forced_neg = True
    for _ in range(500):
        e, j = rng.uniform(1e-6, 9), rng.uniform(1e-6, 9)
        forced_neg &= (-(e + j)) < 0
    # ### and an arbitrary junction sequence does NOT reproduce the observed correlation
    hits = 0
    for _ in range(400):
        seq = [rng.uniform(0, 0.3) for _ in range(16)]
        stepq = [False] + [rng.random() < 0.55 for _ in range(15)]
        ok = all((seq[i] > seq[i - 1]) for i in range(1, 16) if not stepq[i])
        hits += 1 if ok else 0
    return bool(forced_neg and hits < 200)


def main():
    h = Harness(ROOT, 'b255')
    R = rows()

    # 1 -- ### THE MEANINGS FILE IS BYTE-FOR-BYTE WHAT THE REGISTRATION BANKED.
    h.run('meanings-hash-unchanged-since-registration',
          check=lambda: bool(hashlib.sha256(io.open(MEAN, 'rb').read()).hexdigest() == MEAN_SHA
                             and contains(REG, MEAN_SHA)
                             and os.path.getsize(MEAN) == 9790),
          # ### FIXTURE: the registration's OWN bytes hashed against the meanings' hash.
          fixture=lambda: bool(hashlib.sha256(io.open(REG, 'rb').read()).hexdigest() == MEAN_SHA),
          witness=lambda: contains(REG, '2c7faef1'))

    # 2 -- ### THE PRICING PRECEDES EVERYTHING. ### THIS IS THE ACT'S CENTRAL DISCIPLINE.
    h.run('pricing-precedes-meanings-registration-run-and-bank',
          check=lambda: bool(os.path.getmtime(PRICE) < os.path.getmtime(MEAN)
                             < os.path.getmtime(REG) < os.path.getmtime(RUN)
                             < os.path.getmtime(BANK)),
          fixture=lambda: bool(os.path.getmtime(BANK) < os.path.getmtime(PRICE)),
          witness=lambda: bool(os.path.getsize(PRICE) > 2000))

    # 3 -- ### POSITIVE CONTROL ON AN ABSENCE. ### THE PRICING BANK CARRIES NO BALANCE VALUE.
    #      ### The tool CALLS the owners (to time them) but binds every result to `_`.
    h.run('pricing-bank-carries-no-balance-value',
          check=lambda: bool(not re.search(r'resid|junction|E2even|E2odd|balance',
                                           io.open(PRICE, encoding='utf-8').read())
                             and '_ = B38.left_side' in io.open(PTOOL, encoding='utf-8').read()
                             and '_ = B38.per_mode_eps_grids' in
                             io.open(PTOOL, encoding='utf-8').read()
                             and contains(PRICE, 'COSTS ONLY')),
          # ### FIXTURE: the RUN's bank carries those words in abundance, so the matcher is shown
          # ### capable of finding them when they are there.
          fixture=lambda: bool(not re.search(r'resid|junction|E2even',
                                             io.open(RUN, encoding='utf-8').read())),
          witness=lambda: contains(PRICE, 'NO BALANCE VALUE'))

    # 4 -- ### THE TAUTOLOGY CONTROL, BOTH HALVES.
    h.run('negativity-is-forced-but-the-sawtooth-is-not',
          check=sawtooth_is_not_forced,
          # ### FIXTURE: the vacuous form -- `x == x` on a real cell.
          fixture=lambda: bool(abs(R[0]['E2even'] - R[0]['E2even']) > 1e-30),
          witness=lambda: contains(BANK, 'A SUM OF TWO'))

    # 5 -- ### `E2even` FALLS AT EVERY STEP. ### RE-DERIVED.
    h.run('e2even-monotone-across-all-sixteen-cells',
          check=lambda: bool(all(R[i]['E2even'] > R[i + 1]['E2even'] for i in range(len(R) - 1))
                             and len(R) == 16
                             and contains(BANK, 'SIXTEEN CELLS, FIFTEEN STEPS, ONE SIGN')),
          # ### FIXTURE: claim the JUNCTION is monotone too. ### It is not -- it sawtooths -- so
          # ### this fails on the real arrays and shows the gate is reading a column, not a wish.
          fixture=lambda: bool(all(R[i]['junc'] > R[i + 1]['junc'] for i in range(len(R) - 1))),
          witness=lambda: bool(R[0]['E2even'] > R[-1]['E2even']))

    # 6 -- ### THE SAWTOOTH, RE-DERIVED: RISES AT EVERY NON-STEP; FALLS AT EVERY UPPER STEP.
    h.run('junction-sawtooth-locked-to-the-staircase',
          check=lambda: bool(
              # ### six non-step transitions, six rises, no exceptions
              all(R[i]['junc'] > R[i - 1]['junc']
                  for i in range(1, len(R)) if not stepped(R[i - 1], R[i]))
              # ### on the upper ladder every staircase step LOWERS it
              and all(R[i]['junc'] < R[i - 1]['junc']
                      for i in range(1, len(R))
                      if stepped(R[i - 1], R[i]) and R[i]['a2'] >= 20)
              and contains(BANK, 'SIX TRANSITIONS, SIX RISES, NO')),
          # ### FIXTURE: demand the same of the LOWER ladder's steps, where three of them RISE --
          # ### a real stretch that genuinely fails, which is why the bank says "six of nine".
          fixture=lambda: bool(all(R[i]['junc'] < R[i - 1]['junc']
                                   for i in range(1, len(R))
                                   if stepped(R[i - 1], R[i]) and R[i]['a2'] < 20)),
          witness=lambda: bool(sum(1 for i in range(1, len(R))
                                   if not stepped(R[i - 1], R[i])) == 6))

    # 7 -- ### THE BRANCH (MIXED), RE-DERIVED: ALTERNATION THEN A MONOTONE RUN.
    h.run('mixed-alternation-below-twenty-then-eight-shrinks',
          check=lambda: bool(
              # ### at least one GROWING step (so it is not (RELAXES))
              any(abs(R[i]['rA']) > abs(R[i - 1]['rA']) for i in range(1, len(R)))
              # ### and from a^2 = 20 onward every step SHRINKS
              and all(abs(R[i]['rA']) < abs(R[i - 1]['rA'])
                      for i in range(1, len(R)) if R[i]['a2'] >= 25)
              and contains(BANK, 'EIGHT CONSECUTIVE SHRINKS')
              and contains(BANK, '(MIXED)')),
          # ### FIXTURE: claim EVERY step shrinks -- i.e. plain (RELAXES). ### Four steps grow,
          # ### so this fails on the real arrays and the branch is shown to be forced by them.
          fixture=lambda: bool(all(abs(R[i]['rA']) < abs(R[i - 1]['rA'])
                                   for i in range(1, len(R)))),
          witness=lambda: bool(abs(R[-1]['rA']) < abs(R[0]['rA'])))

    # 8 -- ### THE G-REPRO DEBT WAS REGISTERED BEFORE IT WAS PAID, AND IT IS PAID.
    h.run('grid-rebuild-reproduces-b254-within-the-registered-band',
          check=lambda: bool(
              max(max(abs(r['E2even'] - B254_TAB[r['a2']][0]),
                      abs(r['E2odd'] - B254_TAB[r['a2']][1]),
                      abs(r['PR'] - B254_TAB[r['a2']][2]),
                      abs(r['Thq'] - B254_TAB[r['a2']][3]),
                      abs(r['rA'] - B254_TAB[r['a2']][4]))
                  for r in R if r['a2'] in B254_TAB) <= BAND
              and contains(MEAN, 'THE BAND: the six recomputed cells must reproduce')
              and os.path.getmtime(MEAN) < os.path.getmtime(RUN)
              and contains(BANK, 'b254 IS NOT RE-VERDICTED')),
          # ### FIXTURE: the same comparison at a band 100x tighter than registered. ### The worst
          # ### deviation is 5.6e-06, so a 1e-8 band genuinely fails -- the band is doing work.
          fixture=lambda: bool(
              max(max(abs(r['E2even'] - B254_TAB[r['a2']][0]),
                      abs(r['rA'] - B254_TAB[r['a2']][4]))
                  for r in R if r['a2'] in B254_TAB) <= 1e-8),
          witness=lambda: bool(len([r for r in R if r['a2'] in B254_TAB]) == 6))

    # 9 -- ### THE REACH WAS REFUSED ON COST, AND THE REFUSAL PRECEDES EVERY VALUE.
    h.run('reach-refused-on-cost-before-any-value',
          check=lambda: bool(contains(PRICE, '16384')
                             and contains(PRICE, 'REFUSED')
                             and contains(BANK, 'REFUSED ON COST')
                             and contains(MEAN, 'REFUSED ON COST AND THE REFUSAL IS RECORDED '
                                                'BEFORE ANY VALUE EXISTS')
                             and os.path.getmtime(PRICE) < os.path.getmtime(RUN)
                             and max(r['a2'] for r in R) == 100),
          fixture=lambda: bool(max(r['a2'] for r in R) >= 128),
          witness=lambda: contains(PRICE, '2147.5'))

    # 10 -- ### POSITIVE CONTROL ON AN ABSENCE. ### NOTHING WAS EXTRAPOLATED.
    h.run('no-fit-no-slope-no-extrapolated-limit',
          check=lambda: bool(contains(BANK, 'NO FIT, NO SLOPE, NO EXTRAPOLATED LIMIT IS BANKED')
                             and contains(BANK, 'A MEASURED RATE IS NOT A TAIL BOUND')
                             and contains(MEAN, 'A MEASURED RATE IS NOT A TAIL BOUND')
                             # ### THE ABSENCE ITSELF: no fitting machinery anywhere in the run
                             and not re.search(r'polyfit|curve_fit|linregress|np\.polyval',
                                               io.open(os.path.join(E16, 'b255_ladder.py'),
                                                       encoding='utf-8').read())),
          # ### FIXTURE: `numpy` IS imported by the ladder tool, so the matcher is shown able to
          # ### find library calls when they are present.
          fixture=lambda: bool(not re.search(r'import numpy',
                                             io.open(os.path.join(E16, 'b255_ladder.py'),
                                                     encoding='utf-8').read())),
          witness=lambda: contains(BANK, 'b242'))

    # 11 -- ### A WRONG PREDICTION IS REPORTED WRONG, AND ITS FALSIFIER'S COARSENESS OWNED.
    #       ### **THE EASIEST SELF-FLATTERY AVAILABLE HERE.**
    h.run('backwards-prediction-reported-backwards',
          check=lambda: bool(contains(MEAN, '(RELAXES) ON THE LOWER LADDER AND I DO NOT PREDICT '
                                            'THE UPPER')
                             and contains(BANK, 'THAT IS THE REVERSE OF WHAT HAPPENED')
                             and contains(BANK, 'A FALSIFIER THAT DOES NOT FIRE IS NOT A')
                             and contains(BANK, 'MY FALSIFIER WAS TOO COARSE TO')
                             # ### and it IS backwards: the lower ladder oscillates
                             and any(abs(R[i]['rA']) > abs(R[i - 1]['rA'])
                                     for i in range(1, len(R)) if R[i]['a2'] <= 20)),
          fixture=lambda: contains(B254, 'THAT IS THE REVERSE OF WHAT HAPPENED'),
          witness=lambda: contains(MEAN, 'FALSIFIER'))

    # 12 -- ### b253's QUOTED-N LAW OBSERVED FOR REALIZATION (B); NO EARLIER ACT RE-VERDICTED.
    h.run('quoted-n-observed-and-no-re-verdicts',
          check=lambda: bool(contains(RUN, 'Dneg(N = 11, float64 modes, suspect')
                             and contains(BANK, 'Dneg(N = 11, float64 modes, suspect above')
                             and contains(B253, 'THE QUOTED-N LAW')
                             and contains(BANK, 'did not re-verdict b246, b251, b252, b253 or b254')
                             # ### A CONJUNCT WAS REMOVED HERE. ### It demanded the ABSENCE of an
                             # ### upper-case spelling of a phrase the bank legitimately carries in
                             # ### lower case -- `contains()` normalises whitespace, NOT case, so
                             # ### the test was both meaningless and false.
                             # ### ### **A CONJUNCT THAT ASSERTS NOTHING USEFUL IS THE SAME DEFECT
                             # ### ### AS A DECORATIVE GATE, JUST WEARING A NEGATION.**
                             and contains(BANK, 'neither refuted nor proved')),
          fixture=lambda: contains(B254, 'Dneg(N = 11, float64 modes, suspect above n = 6)`, AND '
                                         'THIS ACT OBSERVES'),
          witness=lambda: contains(BANK, 'R-III'))

    # 13 -- ### THE STAIRCASE IS RE-DERIVED AT EVERY CELL, NOT QUOTED, AND ITS SPECIES SAID.
    h.run('staircase-re-derived-and-species-stated',
          check=lambda: bool(all('stair' in r and set(r['stair']) == {'2', '3', '5'} for r in R)
                             and R[0]['stair']['2'] == 1 and R[-1]['stair']['2'] == 6
                             and contains(RUN, 'RE-DERIVED AT EVERY CELL')
                             and contains(BANK, '`7` NEVER ENTERS THIS LADDER')
                             # ### SAME REMOVAL AS GATE 12: a negated conjunct that demanded the
                             # ### absence of a line-broken spelling of a phrase the registration
                             # ### legitimately carries. ### **NEGATION DOES NOT MAKE A VACUOUS
                             # ### CONJUNCT MEANINGFUL.**
                             and contains(REG, 'FIXED AT `(2,3,5)')),
          # ### FIXTURE: claim a fourth prime is present. ### `S4` is (2,3,5), so this fails.
          fixture=lambda: bool(any('7' in r['stair'] for r in R)),
          witness=lambda: bool(R[-1]['stair']['3'] == 4))

    # 14 -- ### NO SIGN-EVENT, AND THE STRUCTURAL REASON IS GIVEN RATHER THAN THE BARE ABSENCE.
    h.run('no-sign-event-and-the-reason-is-structural',
          check=lambda: bool(all(r['rA'] < 0 and r['rB'] < 0 for r in R)
                             and all(r['E2even'] > 0 and r['junc'] >= 0 for r in R)
                             and contains(MEAN, 'THE OUTCOME I MOST WANT TO CATCH')
                             and contains(BANK, 'IT DID NOT OCCUR')
                             and contains(BANK, 'CANNOT CROSS ZERO')),
          # ### FIXTURE: claim some entry is positive. ### None is, on 32 real entries.
          fixture=lambda: bool(any(r['rA'] > 0 for r in R)),
          witness=lambda: bool(len(R) * 2 == 32))

    h.emit()
    c = h.counts()
    return 0 if c['FAIL'] == 0 and c['ERROR'] == 0 and c['REFUSED'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
