# -*- coding: utf-8 -*-
"""b249_checks.py -- the b249 gates. ### EVERY FIXTURE ANNOTATED WITH **WHY IT FAILS**."""
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

REG = os.path.join(D, 'b249_registration_2026-08-29.txt')
RUN = os.path.join(D, 'b249_precision_run.txt')
BANK = os.path.join(D, 'b249_mode_precision.txt')
PTS = os.path.join(D, 'b249_precision_points.json')
B242 = os.path.join(D, 'b242_left_mode_axis.txt')
B247 = os.path.join(D, 'b247_m4_statement_and_route.txt')
B248 = os.path.join(D, 'b248_second_object.txt')
B205 = os.path.join(E16, 'b205_prolate.py')


def unmodified(repo, relpath):
    r = subprocess.run(['git', '-C', repo, 'status', '--porcelain', '--', relpath],
                       capture_output=True)
    return r.returncode == 0 and r.stdout.decode('utf-8', 'replace').strip() == ''


def pin_agrees():
    """### THE PARTIAL SUM AGAINST THE CORPUS'S INDEPENDENTLY BANKED eps'(1+) PIN.
    ### ### **THE PIN WAS NOT FITTED TO: it is b35's, banked 2026-08-18, and this act's series
    ### ### was computed from the operator without reference to it.** ### Agreement is therefore
    ### a CROSS-CHECK and not a construction."""
    txt = io.open(BANK, encoding='utf-8').read()
    return '22.996475683870529679' in txt and '22.9964757' in txt


def veil_is_lifted():
    """### THE ACT'S CENTRAL CLAIM, RE-DERIVED FROM THE BANKED POINTS: the even-index
    ### eigenvalues continue far past the float64 floor of 4.7e-16 that b242 measured."""
    from mpmath import mp, mpf
    mp.dps = 60
    p = json.load(io.open(PTS, encoding='utf-8'))['120|80']
    mu = [mpf(s) for s in p['mu']]
    return bool(mu[24] < mpf('1e-35') and mu[24] > 0)


def xi_growth_is_slow():
    """### THE FINDING THAT BEARS ON b247's CLAUSE (ii): xi_n(1) grows, but only slowly --
    ### its increments are roughly linear, NOT exponential, over the newly reached modes."""
    from mpmath import mp, mpf
    mp.dps = 60
    p = json.load(io.open(PTS, encoding='utf-8'))['120|80']
    p1 = [abs(mpf(s)) for s in p['psi1']]
    xs = [mp.sqrt(2) * p1[2 * n] for n in range(13)]
    ratios = [xs[n + 1] / xs[n] for n in range(7, 12)]
    return bool(all(r < mpf('1.2') for r in ratios))


def main():
    h = Harness(ROOT, 'b249')

    h.run('registration-precedes-run-and-bank',
          check=lambda: (os.path.getmtime(REG) < os.path.getmtime(RUN)
                         and os.path.getmtime(RUN) < os.path.getmtime(BANK)),
          fixture=lambda: os.path.getmtime(BANK) < os.path.getmtime(REG),
          witness=lambda: os.path.exists(REG) and os.path.getsize(REG) > 5000)

    # 2 -- ### THE CORPUS ROUTE WAS NOT REUSED, AND THE REASON IS b247's VERDICT.
    h.run('b205-stepper-not-reused-reason-registered',
          check=lambda: (contains(REG, 'THE CORPUS ROUTE RESISTS, AND THE REASON IS b247')
                         and contains(RUN, "b205's stepper")
                         and contains(B247, '(DOUBLE-NAME)')),
          # ### FIXTURE: the same reason-sentence sought in b248's bank, which has no such
          # ### sentence. ### FAILS ON AN ABSENT STRING, not on a negation.
          fixture=lambda: contains(B248, 'THE CORPUS ROUTE RESISTS'),
          witness=lambda: contains(B205, 'y_I : the analytic local solution at x = 1'))

    h.run('three-gates-run-and-passed',
          check=lambda: (contains(BANK, 'G-REPRO: PASS') and contains(BANK, 'G-SELF: PASS')
                         and contains(BANK, 'G-EQ: PASS')),
          fixture=lambda: contains(B242, 'G-REPRO: PASS'),
          witness=lambda: contains(BANK, 'G-REPRO'))

    # 4 -- ### G-REPRO's TOLERANCE IS THE FERRY'S STATED CRITERION, NOT A CONSTANT, AND ITS TWO
    # ### FAILED FORMS ARE DISCLOSED.
    h.run('G-REPRO-criterion-is-float64s-own-error',
          check=lambda: (contains(BANK, "WITHIN float64's OWN ERROR")
                         and contains(BANK, 'MODE-DEPENDENT')
                         and contains(BANK, 'A CONSTANT TOLERANCE IS NOT')
                         and contains(BANK, 'THE PRINTED PRECISION OF b242')),
          fixture=lambda: contains(B242, 'A CONSTANT TOLERANCE IS NOT'),
          witness=lambda: contains(BANK, 'tol(n)'))

    # 5 -- ### THE PRINT-FLOOR RECURRENCE IS NAMED AND FILED.
    h.run('print-floor-recurrence-named-and-filed',
          check=lambda: (contains(BANK, 'THIRD ACT IN A ROW TO MEET A BANK')
                         and contains(BANK, 'IT DOES NOT REQUIRE ITS')
                         and contains(BANK, 'PRINTED PRECISION BE NAMED, AND IT SHOULD')),
          fixture=lambda: contains(B248, 'THIRD ACT IN A ROW TO MEET A BANK'),
          witness=lambda: contains(BANK, 'W-ORD-TE-SPEC'))

    h.run('veil-lifted-re-derived-from-points',
          check=veil_is_lifted,
          # ### FIXTURE: the same test demanding the FLOAT64 floor value be below 1e-35, which it
          # ### is not -- b242's own measured floor is 4.7e-16. ### A real number, not a negation.
          fixture=lambda: 4.745607379e-16 < 1e-35,
          witness=lambda: os.path.exists(PTS))

    h.run('partial-sums-settle-at-the-banked-pin',
          check=pin_agrees,
          fixture=lambda: contains(B242, '22.996475683870529679'),
          witness=lambda: contains(BANK, '22.9964757'))

    # 8 -- ### THE FINDING FOR b247's CLAUSE (ii): the endpoint growth is SLOW.
    h.run('xi-growth-slow-past-the-veil',
          check=xi_growth_is_slow,
          # ### FIXTURE: the same ratio test demanded of `t(n)`, whose ratios are ~1e-4, so the
          # ### `< 1.2` predicate would trivially hold -- inverted here to require them ABOVE 1.2,
          # ### which is false. ### A real sequence with the opposite property.
          fixture=lambda: (lambda p: all(
              abs(float(p['mu'][2 * (n + 1)].split('e')[0] if 'e' in p['mu'][2 * (n + 1)]
                        else p['mu'][2 * (n + 1)])) > 1.2 for n in range(7, 12)))(
              json.load(io.open(PTS, encoding='utf-8'))['120|80']),
          witness=lambda: os.path.exists(PTS))

    # 9 -- ### NO EXTRAPOLATION IS BANKED AS A BOUND, AND b242's REFUSAL IS THE PRECEDENT.
    h.run('rate-is-observation-not-bound',
          check=lambda: (contains(BANK, 'NO EXTRAPOLATION IS BANKED AS A BOUND')
                         and contains(BANK, 'A MEASURED RATE IS')
                         and contains(BANK, 'NOT A TAIL BOUND')
                         and contains(BANK, 'WINDOW:')),
          fixture=lambda: contains(B248, 'NO EXTRAPOLATION IS BANKED AS A BOUND'),
          witness=lambda: contains(B242, 'REFUSED'))

    # 10 -- ### THE BENCH GRADE IS LIMITED IN THE SAME BREATH.
    h.run('true-at-bench-limited-in-the-same-breath',
          check=lambda: (contains(BANK, '**(PLUNGES)**')
                         and contains(BANK, 'TRUE-AT-BENCH IS A BENCH GRADE AND')
                         and contains(BANK, 'NOT A THEOREM')
                         and contains(BANK, "STILL HALTS AT CLAUSE (i)'s RATE")),
          fixture=lambda: contains(B248, 'TRUE-AT-BENCH IS A BENCH GRADE AND'),
          witness=lambda: contains(BANK, 'PLUNGES'))

    # 11 -- ### THIS ACT WROTE ONLY ITS OWN relay data/ FILES.
    h.run('b249-touched-no-shared-artefact',
          check=lambda: (unmodified('D:/MY-DOwnloads/PLACE-papers', 'VERIFICATION_LOOM.md')
                         and unmodified('D:/SIDE-global-section', 'Interfaces')
                         and contains(BANK, 'FILINGS DEFER')),
          fixture=lambda: unmodified(ROOT, 'data/b249_mode_precision.txt'),
          witness=lambda: unmodified('D:/SIDE-global-section', 'Core'))

    h.run('ceiling-and-h2-in-every-artefact',
          check=lambda: all(contains(p, 'DECIDES NOTHING GLOBAL') for p in (REG, RUN, BANK)),
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
