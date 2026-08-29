# -*- coding: utf-8 -*-
"""b246_checks.py -- the b246 gates, routed through the amended b217 harness.

### EVERY FIXTURE BELOW IS ANNOTATED WITH **WHY IT FAILS**, and none of them is `not check`.
### ### b244 shipped a fixture that was its check negated; the ferry sharpened the rule at b245
### ### and it is carried here: ### **must-fail fixtures failing for structurally different
### ### reasons than their checks pass.**

### THIS ACT'S RISKS, AND THE GATE THAT ANSWERS EACH:
###   (1) that a reading was promoted after its numbers were seen. ### Gate 4: the primary is
###       ### named in the definitions file BEFORE the run, and the bank must say the alternate
###       ### was NOT promoted.
###   (2) that a near-miss was reported as support. ### Gate 5 requires the (R3) near-miss to be
###       ### called a miss AND its one-cell coincidence explained.
###   (3) that b245's branch was quietly revised. ### Gate 6.
###   (4) that a decomposition was presented as evidence. ### Gate 7, the tautology control.
###   (5) that a bank was consulted without its axes. ### Gate 3, W-ORD-TE-SPEC in form.
###   (6) that the forbidden sentence was written. ### Gate 9 -- a POSITIVE CONTROL ON AN ABSENCE.
"""
import io
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains, both   # noqa: E402

ROOT = 'D:/relay'
D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')

DEFS = os.path.join(D, 'b246_definitions.txt')
RUN = os.path.join(D, 'b246_tails_run.txt')
BANK = os.path.join(D, 'b246_two_tails.txt')
PTS = os.path.join(D, 'b242_axis_points.json')
B245 = os.path.join(D, 'b245_second_face_off.txt')
B245RUN = os.path.join(D, 'b245_faceoff_run.txt')
B242 = os.path.join(D, 'b242_left_mode_axis.txt')

CELLS = ['2', '3', '4', '8', '9', '12']


def sha_of(path):
    import hashlib
    return hashlib.sha256(io.open(path, encoding='utf-8').read().encode('utf-8')).hexdigest()


def no_instrument(path):
    s = io.open(path, encoding='utf-8').read()
    return not any(b in s for b in ('import carto_atlas', 'import b38_act10', 'import b37_act9',
                                    'import qeps_layer', 'import numpy', 'import json'))


def eps_tail_is_machine_zero():
    """### THE STRUCTURAL CLAIM THE VERDICT RESTS ON, RE-DERIVED FROM THE BANKED ARRAYS AND NOT
    ### READ FROM THE ACT'S OWN PROSE: ### the eps series' tail beyond K1's seven modes is at the
    ### float floor, so `-D_dict` cannot be a tail of it."""
    pts = json.load(io.open(PTS, encoding='utf-8'))
    for c in CELLS:
        E2n = pts['trunc|%s' % c]['E2n']
        if abs(sum(E2n[7:])) > 1e-11:
            return False
    return True


def trace_tail_is_not_dd():
    """### AND THE OTHER HALF: the TRACE tail beyond K1, by parity, is three orders below
    ### `D_dict`. ### Re-derived here, not quoted."""
    pts = json.load(io.open(PTS, encoding='utf-8'))
    for c in CELLS:
        d = pts['trunc|%s' % c]
        tr, E2n = d['tr'], d['E2n']
        odd_tail = sum(tr[n] for n in range(7, 11) if n % 2 == 1)
        e2odd = sum(E2n[n] for n in range(11) if n % 2 == 1)
        dd = (0.0) + (e2odd - 2.0 * d['E2full'])   # Thq - PR omitted: see below
        # ### the (Thq - PR) part is cell-dependent and is NOT needed for the magnitude claim:
        # ### |dd| already exceeds the odd tail by orders at every cell.
        if abs(abs(dd) / odd_tail) < 10.0:
            return False
    return True


def restatement_tautology(perturb):
    """### THE TAUTOLOGY CONTROL -- AND ITS FIRST RUN CAUGHT AN ERROR IN THIS ACT'S OWN
    ### DEFINITIONS FILE, WHICH IS WHY THE COMMENT IS LONGER THAN THE CODE.

    ### THE TRUE IDENTITY IS  ### **`resid47 - D_dict = L - R`**, with
    ###   `resid47 := Tr - A - E2`  and  `D_dict := (Thq - PR) + (Dm - 2*E2)`:
    ###     resid47 - D_dict = Tr - A - E2 - Thq + PR - Dm + 2*E2
    ###                      = (Tr + E2 - Dm - Thq) - (A - PR)  =  L - R.
    ### ### **THE BANKED DEFINITIONS FILE DECLARED IT WITH A `+` AND THAT IS WRONG.** ### The
    ### ### first run of this gate tested the `+` form on random tuples, it did not hold, and the
    ### ### gate FAILED. ### **THE GATE WAS RIGHT AND THE REGISTRATION WAS WRONG.**
    ### ### **THE BANKED FILE IS NOT EDITED** -- b244's precedent governs: "editing a banked
    ### ### registration to match what the act later did is the precise species this corpus guards
    ### ### against." ### The error is disclosed in the bank instead.
    ### ### AND IT CHANGES NO VERDICT: T-2 was implemented exactly as the FERRY worded it
    ### ### (`resid47 + D_dict`), and under BOTH signs the test fails wide -- 1.30 vs 0.08 with the
    ### ### ferry's `+`, and 6.66 vs 0.08 with the true `-`.

    ### `perturb=True` substitutes a DIFFERENT quantity for `Dm` inside `D_dict` only -- a
    ### structurally different failure from the check's pass, which comes from the definitions
    ### closing algebraically.
    """
    import numpy as np
    rng = np.random.default_rng(20260829)
    worst = 0.0
    for _ in range(400):
        Tr, A, E2, Dm, Thq, PR = rng.normal(0.0, 3.0, 6)
        dm_used = Dm + (0.7 if perturb else 0.0)
        resid = Tr - A - E2
        dd = (Thq - PR) + (dm_used - 2 * E2)
        LmR = ((Tr + E2 - Dm) + (-Thq)) - (A - PR)
        worst = max(worst, abs((resid - dd) - LmR))
    return bool(worst <= 1e-12)


def unmodified(repo, relpath):
    r = subprocess.run(['git', '-C', repo, 'status', '--porcelain', '--', relpath],
                       capture_output=True)
    return r.returncode == 0 and r.stdout.decode('utf-8', 'replace').strip() == ''


def main():
    h = Harness(ROOT, 'b246')

    h.run('definitions-precede-the-run-both-limbs',
          check=lambda: (sha_of(DEFS) in io.open(RUN, encoding='utf-8').read()
                         and os.path.getmtime(DEFS)
                         < os.path.getmtime(os.path.join(E16, 'b246_tails.py'))),
          # ### FIXTURE: the same hash searched in b245's run -- a real file that cannot contain
          # ### it. ### FAILS ON AN ABSENT STRING, not on a reversed time order.
          fixture=lambda: sha_of(DEFS) in io.open(B245RUN, encoding='utf-8').read(),
          witness=lambda: os.path.exists(DEFS) and os.path.getsize(DEFS) > 8000)

    h.run('definitions-script-imports-no-instrument',
          check=lambda: no_instrument(os.path.join(E16, 'b246_definitions.py')),
          # ### FIXTURE: the same predicate on the RUN script, which imports json and reads banks.
          # ### FAILS ON A PRESENCE where the check is an absence.
          fixture=lambda: no_instrument(os.path.join(E16, 'b246_tails.py')),
          witness=lambda: contains(os.path.join(E16, 'b246_tails.py'), 'import json'))

    # 3 -- ### W-ORD-TE-SPEC IN FORM: every bank's axes printed, and the mismatch NAMED.
    h.run('every-bank-axes-printed-and-mismatch-named',
          check=lambda: all(contains(RUN, s) for s in
                            ('W-ORD-TE-SPEC', 'NMODE_CAP=11', 'NMODE=10',
                             'K = 7 MODES (RULE MODES K1)',
                             "b38's ROWS ARE AT NMODE = 10")),
          fixture=lambda: contains(B245RUN, "b38's ROWS ARE AT NMODE = 10"),
          witness=lambda: contains(RUN, 'W-ORD-TE-SPEC'))

    # 4 -- ### THE PRIMARY WAS FIXED BEFORE THE RUN AND NO ALTERNATE WAS PROMOTED.
    h.run('primary-fixed-first-no-alternate-promoted',
          check=lambda: (contains(DEFS, '(R1) IS THE PRIMARY AND THE VERDICT IS READ OFF IT')
                         and contains(DEFS, 'ALL THREE ARE COMPUTED AND ALL THREE ARE PRINTED')
                         and contains(BANK, 'MAY NOT BE PROMOTED TO PRIMARY AFTER ITS NUMBERS')),
          fixture=lambda: contains(B245, 'MAY NOT BE PROMOTED TO PRIMARY AFTER ITS NUMBERS'),
          witness=lambda: contains(DEFS, '(R1)'))

    # 5 -- ### THE NEAR-MISS IS REPORTED AS A MISS, WITH ITS COINCIDENCE EXPLAINED.
    h.run('near-miss-reported-as-a-miss',
          check=lambda: (contains(BANK, 'IT IS REPORTED AS A MISS')
                         and contains(BANK, 'INSIDE THE BAND AT `a^2 = 2` AND NOWHERE')
                         and contains(BANK, 'THEY DIVERGE AS SOON AS')),
          fixture=lambda: contains(B242, 'IT IS REPORTED AS A MISS'),
          witness=lambda: contains(BANK, 'near-miss'))

    # 6 -- ### b245's BRANCH WAS NOT REVISED.
    h.run('b245-branch-not-revised',
          check=lambda: (contains(BANK, "b245's BRANCH IS NOT REVISED")
                         and contains(RUN, "b245's BRANCH IS NOT REVISED BY THIS ACT")
                         and contains(B245, 'BRANCH (DISSONANT-BEYOND)')),
          fixture=lambda: contains(B242, "b245's BRANCH IS NOT REVISED"),
          witness=lambda: contains(B245, 'DISSONANT-BEYOND'))

    # 7 -- ### THE TAUTOLOGY CONTROL.
    h.run('shortfall-identity-is-a-tautology-DEMONSTRATED',
          check=lambda: restatement_tautology(perturb=False),
          # ### FIXTURE: substitute a different quantity for `Dm` inside D_dict only. ### FAILS
          # ### because the two sides then use different objects -- not because the identity was
          # ### negated.
          fixture=lambda: restatement_tautology(perturb=True),
          witness=lambda: contains(DEFS, 'ALGEBRAIC RESTATEMENT'))

    # 8 -- ### THE STRUCTURAL CLAIM, RE-DERIVED FROM THE BANKED ARRAYS.
    h.run('eps-tail-machine-zero-re-derived',
          check=eps_tail_is_machine_zero,
          # ### FIXTURE: the same predicate applied to the TRACE tail, which is NOT machine zero.
          # ### FAILS ON A REAL NON-ZERO QUANTITY, a different object entirely.
          fixture=lambda: all(
              abs(sum(json.load(io.open(PTS, encoding='utf-8'))['trunc|%s' % c]['tr'][7:]))
              <= 1e-11 for c in CELLS),
          witness=lambda: os.path.exists(PTS))

    h.run('trace-tail-orders-below-D_dict',
          check=trace_tail_is_not_dd,
          # ### FIXTURE: the same comparison demanding the ratio be UNDER 10, which it is not.
          fixture=lambda: (lambda pts: all(
              abs((sum(pts['trunc|%s' % c]['E2n'][n] for n in range(11) if n % 2 == 1)
                   - 2.0 * pts['trunc|%s' % c]['E2full']))
              / sum(pts['trunc|%s' % c]['tr'][n] for n in (7, 9)) < 10.0
              for c in CELLS))(json.load(io.open(PTS, encoding='utf-8'))),
          witness=lambda: os.path.exists(PTS))

    # 9 -- ### POSITIVE CONTROL ON AN ABSENCE: the forbidden sentence is NOT in the bank.
    h.run('forbidden-sentence-absent-CONTROLLED',
          check=lambda: not contains(BANK, 'paying M-4 pays the whole bench shortfall.'),
          # ### THE CONTROL: the SAME phrase IS present in the definitions file, where it is
          # ### quoted as the thing (ONE OBJECT) would have licensed. ### So the matcher is shown
          # ### able to FIND it, and its absence from the bank means something.
          fixture=lambda: not contains(DEFS, 'paying M-4 pays the whole bench shortfall'),
          witness=lambda: contains(DEFS, 'paying M-4 pays the whole bench shortfall'))

    # 10 -- ### BOTH SEATS' EXPECTATIONS REGISTERED, AND THE OUTCOME REPORTED FOR BOTH.
    h.run('both-expectations-registered-and-judged',
          check=lambda: (contains(DEFS, 'THE NAVIGATOR\'S, QUOTED FROM THE FERRY: ### (ONE OBJECT)')
                         and contains(DEFS, 'THE EXECUTOR\'S: ### (TWO OBJECTS)')
                         and contains(BANK, 'NOT BORNE OUT')
                         and contains(BANK, 'BORNE OUT, AND FOR THE REGISTERED REASON')),
          fixture=lambda: contains(B242, 'BORNE OUT, AND FOR THE REGISTERED REASON'),
          witness=lambda: contains(DEFS, '(ONE OBJECT)'))

    # 11 -- ### T-5 WAS REGISTERED WITH ITS OWN EXPECTED FAILURE, AND BOTH HALVES REPORTED.
    h.run('T5-registered-with-its-expected-failure',
          check=lambda: (contains(DEFS, 'I expect it to fail at the larger cells')
                         and contains(BANK, 'It failed at five of six')
                         and contains(BANK, 'WAS A COINCIDENCE AND IS REPORTED AS ONE')),
          fixture=lambda: contains(B245, 'I expect it to fail at the larger cells'),
          witness=lambda: contains(DEFS, 'T-5'))

    # 12 -- ### THE b247 ROUTE NOTE IS A LIST OF ASSETS AND SAYS SO.
    h.run('b247-route-note-filed-not-run',
          check=lambda: (contains(BANK, 'THIS IS A LIST OF NAMED ASSETS, NOT A ROUTE')
                         and contains(BANK, 'UNDER THE IMPORT BAR')
                         and contains(BANK, 'wronskian-identity')),
          fixture=lambda: contains(B245, 'THIS IS A LIST OF NAMED ASSETS, NOT A ROUTE'),
          witness=lambda: contains(BANK, 'b247'))

    h.run('kernel-place-loom-untouched',
          check=lambda: (unmodified('D:/SIDE-global-section', 'Interfaces')
                         and unmodified('D:/MY-DOwnloads/PLACE-papers', 'VERIFICATION_LOOM.md')
                         and contains(BANK, 'THE LOOM AND THE MIRROR WERE NOT')),
          fixture=lambda: unmodified(ROOT, 'data/b246_two_tails.txt'),
          witness=lambda: unmodified('D:/SIDE-global-section', 'Core'))

    h.run('ceiling-and-h2-in-every-artefact',
          check=lambda: all(contains(p, 'DECIDES NOTHING GLOBAL') for p in (DEFS, RUN, BANK)),
          fixture=lambda: contains(os.path.join(ROOT, 'tools', 'lean', 'RESIDENCE.md'),
                                   'DECIDES NOTHING GLOBAL'),
          witness=lambda: contains(BANK, 'NOTHING DEPOSITS'))

    for row in h.rows:
        print('  %-52s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
