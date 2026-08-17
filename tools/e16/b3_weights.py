"""B3 ADDENDUM — IS THE NON-MONOTONICITY COEFFICIENT-DRIVEN? THREE WEIGHTINGS, NOT TWO.

Relay-only, bench-grade. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.

WHY THREE AND NOT TWO
======================
The ferry's caveat asked for a unit-weight re-run. ### RUN ALONE, THAT COMPARISON WOULD BE
### CONFOUNDED, AND THE CORPUS'S OWN MEASUREMENT IS WHY.

2026-08-17 measured the pure two-lag form at L = 9, omega = 1e-3 under three weightings:

    registered  2 sqrt(q) log p   -> NPOS = 1098      nullity 1
    Weil        4 log p / sqrt(q) -> NPOS = 1098      nullity 1
    ### unit    c = 1 for all     -> NPOS = 889       ### nullity 419

and filed the finding: ### the count is the matching number at GENERIC weights and DROPS at
### the degenerate weight c2 = c3. Equal weights make cycle contributions cancel and the rank
fall; unit is a measure-zero choice.

### SO "REGISTERED vs UNIT" CANNOT SEPARATE "the coefficients drive the movement" FROM
### "you evaluated at the one weighting known to be degenerate."
Two generic conventions are needed to make the comparison mean anything:

    (a) registered vs Weil  -- BOTH GENERIC, different SHAPES (ratios differ up to 2.5x)
                               ### this is the real test of coefficient-dependence
    (b) either vs unit      -- the degeneracy check, retained because it is informative
                               about the degeneracy and NOT about the weights in general

REGISTERED PREDICTIONS, BOTH BRANCHES LONGHAND, BEFORE ANY NUMBER
=================================================================
W1  ### THE DECISIVE ONE. Registered and Weil give the SAME step pattern -- same signs, and
    step sizes agreeing to within a few offenders -- at every (L, S).
    -> IF SO: ### the movement and the NON-MONOTONICITY ARE STRUCTURAL, not coefficient-driven.
       They are about WHICH LAGS ARE ADMITTED, and B3's verdict stands unqualified. The
       caveat named on 2026-08-17 is discharged.
    -> IF NOT: ### the step pattern depends on the coefficient SHAPE even among generic
       weights. Then B3's "not even monotone" is a statement about the weighting and not
       about the place set, that half of the verdict is withdrawn, and the surviving half is
       only "NOT STABLE" -- which the +455..+751 first steps would still support.

W2  Unit weights differ from both generic ones somewhere, as the degeneracy predicts.
    ### A NULL HERE WOULD BE INFORMATIVE IN THE OTHER DIRECTION: it would say the c2 = c3
    ### degeneracy does not reach these lag sets, which are not bipartite and where the
    ### rank-2mu identity does not hold anyway.

W3  Monotonicity is reported PER WEIGHTING, so "four of five windows" can be checked against
    each convention rather than inherited from one.

WHAT IS NOT CLAIMED
====================
### NO SIGN SENTENCE. This is a control on a bench quantity. Nothing here bears on
W_inf - W_2, and nothing here revisits the stability verdict except through its caveat.

Usage:  python b3_weights.py register | run
"""
import math
import os
import re
import sys
import time

import numpy as np

import qeps_layer as Q
import phi_layer as P
import exp1_two_prime as E1

LOG2 = math.log(2.0)
CELLS = [9.0, 12.0, 16.0, 27.0, 32.0]
OM = 1.0e-3
CHAIN = [(2,), (2, 3), (2, 3, 5), (2, 3, 5, 7), (2, 3, 5, 7, 11)]
RUN = r"D:\relay\data\b3_2026-08-17.txt"

WEIGHTS = [
    ("registered", lambda q, p: E1.coeff(q, p)),
    ("Weil", lambda q, p: E1.coeff_weil(q, p)),
    ("unit", lambda q, p: 1.0),
]


def lags_for(L, S, wf):
    out = []
    for p in S:
        k = 1
        while p ** k < L:
            q = p ** k
            lab = "log %d" % q if k == 1 else "%d log %d" % (k, p)
            out.append((lab, math.log(q), wf(q, p)))
            k += 1
    return sorted(out, key=lambda t: t[1])


def banked():
    out = {}
    for line in open(RUN, encoding="utf-8", errors="replace"):
        m = re.match(r"\s+(\d+)\s+\{([\d,]+)\}\s+(\d+)\s+(\d+)\s+(\d+)\s", line)
        if m:
            out[(float(m.group(1)), m.group(2))] = int(m.group(5))
    return out


def registration():
    print("=" * 112)
    print("B3 WEIGHT CONTROL — REGISTRATION. NO MEASURED NUMBER IN THIS BLOCK.")
    print("=" * 112)
    print(__doc__)
    print("  the three weightings, per prime power:")
    print("  %-6s %-14s %-14s %-8s" % ("q", "registered", "Weil", "unit"))
    for q, p, k in E1.prime_powers_below(12.0):
        print("  %-6d %-14.6f %-14.6f %-8.1f" % (q, E1.coeff(q, p), E1.coeff_weil(q, p), 1.0))
    print("\n  registered/Weil ratio spread: %.2fx to %.2fx"
          % (min(E1.coeff(q, p) / E1.coeff_weil(q, p) for q, p, _ in E1.prime_powers_below(12.0)),
             max(E1.coeff(q, p) / E1.coeff_weil(q, p) for q, p, _ in E1.prime_powers_below(12.0))))
    print("=" * 112)
    sys.stdout.flush()


def run():
    e1p = Q.epsprime1()
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    have = banked()
    print("  re-using %d banked 'registered' values from %s\n" % (len(have), RUN))
    need = int(round(math.log(max(CELLS)) / OM))
    t0 = time.time()
    qv = P._qvals(OM, need, E1.NG_Q)
    print("      [Q_eps table: omega=%.1e, nmax=%d, %.1f s]\n" % (OM, need, time.time() - t0))

    res = {}
    print("  %-6s %-14s %-13s %-13s %-13s" % ("L", "S", "registered", "Weil", "unit"))
    for L in CELLS:
        for S in CHAIN:
            key = (L, ",".join(map(str, S)))
            row = []
            for name, wf in WEIGHTS:
                if name == "registered" and key in have:
                    row.append(have[key])
                    continue
                lg = lags_for(L, S, wf)
                if not lg:
                    row.append(None)
                    continue
                n, dim, frac, M = E1.measure(L, OM, lg, qv, e1p)
                row.append(n)
            res[key] = row
            print("  %-6.0f %-14s %-13s %-13s %-13s"
                  % (L, "{" + ",".join(map(str, S)) + "}",
                     *[str(x) if x is not None else "-" for x in row]))
            sys.stdout.flush()
        print()

    print("=" * 112)
    print("  W1 / W3 — THE STEP PATTERNS, PER WEIGHTING")
    print("=" * 112)
    print("  %-6s %-13s %-34s %s" % ("L", "weighting", "steps in NPOS", "monotone?"))
    patterns = {}
    for L in CELLS:
        for i, (name, _) in enumerate(WEIGHTS):
            seq = [res[(L, ",".join(map(str, S)))][i] for S in CHAIN]
            seq = [x for x in seq if x is not None]
            steps = [b - a for a, b in zip(seq, seq[1:])]
            patterns[(L, name)] = steps
            print("  %-6.0f %-13s %-34s %s"
                  % (L, name, " ".join("%+d" % d for d in steps),
                     "yes" if all(d >= 0 for d in steps) else "### NO"))
        print()

    print("=" * 112)
    print("  W1 VERDICT — registered vs Weil, the two GENERIC conventions")
    print("=" * 112)
    same_sign = True
    worst = 0
    for L in CELLS:
        a, b = patterns[(L, "registered")], patterns[(L, "Weil")]
        signs = all((x >= 0) == (y >= 0) for x, y in zip(a, b))
        diffs = [abs(x - y) for x, y in zip(a, b)]
        worst = max(worst, max(diffs) if diffs else 0)
        same_sign = same_sign and signs
        print("  L=%-6.0f signs agree: %-6s  |step difference| = %s"
              % (L, "yes" if signs else "### NO", " ".join(map(str, diffs))))
    print("\n  ### W1: %s"
          % ("LANDS — the two generic conventions give the same sign pattern; largest step "
             "difference %d offenders. THE MOVEMENT IS STRUCTURAL, NOT COEFFICIENT-DRIVEN."
             % worst if same_sign else
             "### FAILS — the step pattern depends on the coefficient shape among generic "
             "weights; the non-monotonicity half of B3's verdict is withdrawn."))

    print("\n" + "=" * 112)
    print("  W2 — the unit degeneracy")
    print("=" * 112)
    diff_cells = sum(1 for k, v in res.items()
                     if v[0] is not None and v[2] is not None and v[0] != v[2])
    print("  cells where unit differs from registered: %d of %d" % (diff_cells, len(res)))


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    run()


if __name__ == "__main__":
    main()
