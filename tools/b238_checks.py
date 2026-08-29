# -*- coding: utf-8 -*-
"""b238_checks.py -- the b238 gates, routed through the amended b217 harness.

### THIS ACT'S RISK IS THE OPPOSITE OF b233's, AND IT IS SHARPER.
### ### b233 FAILED A CRITERION THAT WAS WRONG. ### b238's risk was PASSING A CRITERION IT
### ### QUIETLY AUTHORED TO BE PASSED -- and the criterion came out 4% short at one cell, so
### ### the temptation was real and one keystroke wide.
### THE GATES THEREFORE CHECK THE **ORDER OF OPERATIONS** AND THE **UNWIDENED CONSTANTS**,
### not merely the outcome:
###   - the criterion file must PRECEDE the final run on disk;
###   - its fit axes must EXCLUDE its test axes;
###   - its banked K must equal K RECOMPUTED from the banked measurements.
"""
import io
import math
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_harness import Harness, contains, both   # noqa: E402

ROOT = 'D:/relay'
SGS = 'D:/SIDE-global-section'
PLACE = 'D:/MY-DOwnloads/PLACE-papers'
D = os.path.join(ROOT, 'data')
E16 = os.path.join(ROOT, 'tools', 'e16')

BANK = os.path.join(D, 'b238_imp1_budget.txt')
REG = os.path.join(D, 'b238_registration_2026-08-28.txt')
BUDGET = os.path.join(D, 'b238_budget_run.txt')
CRIT = os.path.join(D, 'b238_criterion.txt')
FINAL = os.path.join(D, 'b238_final_run.txt')
B233 = os.path.join(D, 'b233_the_arrangement.txt')
B237 = os.path.join(D, 'b237_left_side_assets.txt')

CHAIN = os.path.join(PLACE, 'phase2', 'method', 'THE_IDENTITY_CHAIN.md')
CRITPY = os.path.join(E16, 'b238_criterion.py')
FINALPY = os.path.join(E16, 'b238_final.py')
B38 = os.path.join(E16, 'b38_act10.py')


def mtime(p):
    return os.path.getmtime(p) if os.path.isfile(p) else -1.0


def unmodified(repo, relpath):
    try:
        r = subprocess.run(['git', '-C', repo, 'status', '--porcelain', '--', relpath],
                           capture_output=True)
    except Exception:
        return False
    return r.returncode == 0 and r.stdout.decode('utf-8', 'replace').strip() == ''


def banked_K():
    """### K AS THE CRITERION FILE STATES IT."""
    out = {}
    for line in io.open(CRIT, encoding='utf-8', errors='replace'):
        m = re.search(r'K\(a\^2=(\d)\)\s*=\s*([0-9.]+)', line)
        if m:
            out[m.group(1)] = float(m.group(2))
    return out


def recomputed_K():
    """### K RECOMPUTED FROM THE BANKED MEASUREMENTS IN b238_criterion.py's OWN TABLE.
    ### ### IF THE BANKED K WERE EVER NUDGED UPWARD TO ADMIT A RESIDUAL, THESE WOULD DIVERGE."""
    src = io.open(CRITPY, encoding='utf-8', errors='replace').read()
    block = src[src.index('MEASURED = {'):src.index('A_SQ = {')]
    out = {}
    for tag in ('3', '4'):
        seg = re.search(r"'%s':\s*\{([^}]*)\}" % tag, block)
        if not seg:
            return {}
        best = 0.0
        for nv, val in re.findall(r'(\d+):\s*([0-9.e+-]+)', seg.group(1)):
            L = math.log(math.sqrt(float(tag)))
            h = (4.0 * L) / (2 * int(nv) - 2)
            best = max(best, float(val) / (h * h))
        out[tag] = best
    return out


def fit_excludes_test():
    """### THE FIT AXES MUST NOT CONTAIN THE TEST AXES."""
    src = io.open(CRITPY, encoding='utf-8', errors='replace').read()
    block = src[src.index('MEASURED = {'):src.index('A_SQ = {')]
    fit = set(int(n) for n, _v in re.findall(r'(\d+):\s*([0-9.e+-]+)', block))
    return fit.isdisjoint({4001, 6001}) and fit == {2001, 8001, 16001}


def main():
    h = Harness(ROOT, 'b238')

    # 1 -- ### THE CRITERION PRECEDES THE RESULT ON DISK. ### THE ACT'S CENTRAL GUARD.
    h.run('criterion-precedes-final-run',
          check=lambda: 0 < mtime(CRIT) < mtime(FINAL),
          fixture=lambda: 0 < mtime(FINAL) < mtime(CRIT),
          witness=lambda: mtime(CRIT) > 0 and mtime(FINAL) > 0)

    # 2 -- ### THE FIT AXES EXCLUDE THE TEST AXES: the prediction is OUT OF SAMPLE.
    h.run('fit-axes-exclude-test-axes',
          check=lambda: fit_excludes_test(),
          fixture=lambda: not fit_excludes_test(),
          witness=lambda: contains(CRIT, 'EXCLUDED FROM THE FIT'))

    # 3 -- ### THE BANKED K EQUALS K RECOMPUTED FROM THE BANKED MEASUREMENTS.
    # ### ### THIS IS THE 'NO PROJECTION WIDENED' GATE, AND IT IS ARITHMETIC, NOT A PROMISE.
    h.run('banked-K-not-widened',
          check=lambda: (banked_K() and recomputed_K()
                         and all(abs(banked_K()[t] - recomputed_K()[t]) < 1e-3
                                 for t in ('3', '4'))),
          fixture=lambda: (banked_K() and recomputed_K()
                           and all(banked_K()[t] > recomputed_K()[t] + 1e-3
                                   for t in ('3', '4'))),
          witness=lambda: bool(banked_K()) and bool(recomputed_K()))

    # 4 -- ### THE EDGE HYPOTHESIS IS REFUTED **WITH ITS POSITIVE CONTROL** in the same run.
    h.run('edge-hypothesis-refuted-with-control',
          check=lambda: (contains(BUDGET, '0.4439938161680794')
                         and contains(BANK, 'DOES NOT EXIST')
                         and contains(REG, 'I EXPECT IT TO BE REFUTED')),
          fixture=lambda: contains(B233, '0.4439938161680794'),
          witness=lambda: contains(BUDGET, '0.4439938161680794'))

    # 5 -- ### THE BUDGET COLLAPSES TO ONE SOURCE, and the act says which.
    h.run('budget-collapses-to-one-source',
          check=lambda: both(BANK, 'CARRIES THE ENTIRE RESIDUAL', 'MACHINE'),
          fixture=lambda: both(B237, 'CARRIES THE ENTIRE RESIDUAL', 'MACHINE'),
          witness=lambda: contains(BANK, 'CARRIES THE ENTIRE RESIDUAL'))

    # 6 -- ### THE VERDICT IS (HELD) AND THE OVER-CELL IS REPORTED, NOT SMOOTHED.
    h.run('verdict-held-with-over-cell-shown',
          check=lambda: (contains(FINAL, '### OVER')
                         and contains(BANK, 'BRANCH (HELD)')
                         and contains(BANK, 'OVER BY A FACTOR OF 1.04')),
          fixture=lambda: contains(B233, 'OVER BY A FACTOR OF 1.04'),
          witness=lambda: contains(FINAL, '### OVER'))

    # 7 -- ### THE REFUSAL IS ON THE RECORD: the one keystroke that would have promoted it.
    h.run('widening-named-and-refused',
          check=lambda: both(BANK, 'ONE KEYSTROKE AWAY',
                             'I WILL NOT WIDEN A PROJECTION TO COVER A RESIDUAL'),
          fixture=lambda: contains(B233, 'ONE KEYSTROKE AWAY'),
          witness=lambda: contains(REG, 'I WILL NOT WIDEN A PROJECTION TO COVER A RESIDUAL'))

    # 8 -- ### NO ERROR SPEC FILED, because the ferry files it on (PROMOTED) only.
    h.run('no-error-spec-filed-on-held',
          check=lambda: contains(BANK, 'NO RIGHT-SIDE ERROR SPEC IS FILED'),
          fixture=lambda: contains(B237, 'NO RIGHT-SIDE ERROR SPEC IS FILED'),
          witness=lambda: contains(BANK, 'on (PROMOTED) only'))

    # 9 -- ### IMP-1 STAYS TRUSTED-AT-CITE: the ledger cell is not promoted.
    h.run('imp1-stays-trusted-at-cite',
          check=lambda: (contains(CHAIN, 'TRUSTED-AT-CITE')
                         and contains(BANK, 'IMP-1 STAYS `TRUSTED-AT-CITE`')),
          fixture=lambda: contains(BANK, 'IMP-1 graded VERIFIED-AT-BENCH'),
          witness=lambda: contains(CHAIN, 'TRUSTED-AT-CITE'))

    # 10 -- ### THE OLD WORK-ORDER IS DISCHARGED AND A NEW, NAMED ONE REPLACES IT.
    h.run('budget-discharged-envelope-filed',
          check=lambda: both(BANK, 'W-ORD-IMP1-BUDGET` -- DISCHARGED', 'W-ORD-IMP1-ENVELOPE'),
          fixture=lambda: contains(B233, 'W-ORD-IMP1-ENVELOPE'),
          witness=lambda: contains(BANK, 'W-ORD-IMP1-ENVELOPE'))

    # 11 -- ### THE CORPUS'S LEFT SIDE APPEARS NOWHERE IN THE BENCH SCRIPTS.
    h.run('left-side-absent-from-the-bench',
          check=lambda: not any(contains(p, s) for p in (CRITPY, FINALPY)
                                for s in ('QuotientTrace', 'ArchimedeanE1Trace', 'theta_quotient')),
          fixture=lambda: any(contains(B38, s) for s in ('theta_quotient',)) is False,
          witness=lambda: contains(B38, 'theta_quotient'))

    # 12 -- ### THE INSTRUMENTS WERE IMPORTED UNMODIFIED, and the kernel is untouched.
    h.run('instruments-and-kernel-unmodified',
          check=lambda: (unmodified(ROOT, 'tools/e16/b38_act10.py')
                         and unmodified(ROOT, 'tools/e16/carto_atlas.py')
                         and unmodified(SGS, 'Interfaces')),
          fixture=lambda: not unmodified(ROOT, 'tools/e16/b38_act10.py'),
          witness=lambda: unmodified(SGS, 'Interfaces'))

    for row in h.rows:
        print('  %-42s %-8s %s' % row)
    blk, path = h.emit()
    print(blk)
    print('sidecar: %s' % path)


if __name__ == '__main__':
    main()
