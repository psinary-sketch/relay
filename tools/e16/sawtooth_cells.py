"""THE DISCRIMINATING CELLS — L = 32, 64, 128 against the sawtooth.

Relay-only, bench-grade. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.
This is about the remainder route's failure COUNT only.

WHY THESE THREE
================
The derived count for the pure lag form is NPOS(S_k) = (M - nullity)/2 with
M = q k + s and nullity = s (q even) or k - s (q odd). In the continuum r = M/k:

    q = 2m-1 -> fraction 1 - m/r        q = 2m -> fraction m/r

so the fraction is a sawtooth with peaks 1/2 at r = 2m (L = 4, 16, 64, ...) and troughs
m/(2m+1) at r = 2m+1 (L = 8, 32, 128, ...) with values 1/3, 2/5, 3/7, ...

2026-08-17 measured r <= 4.32 (L <= 20), covering teeth q = 1..4.
### L = 32, 64, 128 ARE r = 5, 6, 7 EXACTLY — the fifth, sixth and seventh teeth, and the
### first cells of the third trough, the third peak, and the fourth trough.

    THE METHOD LINE THIS SITTING IS RUN UNDER, minted from the day's two failures:
    ### A LAW READ OFF A RANGE IS A LAW ABOUT THAT RANGE — ONE CELL OUTSIDE IS THE CHEAP
    ### DEFENCE. These are those cells.

REGISTERED PREDICTIONS, COMPUTED FROM THE ACTUAL (M, k) AND PRINTED BEFORE ANY MEASUREMENT
===========================================================================================
C1  L = 32  (r = 5, an ODD tooth):  fraction -> 2/5 = 0.400000
C2  L = 64  (r = 6, an EVEN tooth): fraction -> 1/2 = 0.500000   ### THE THIRD APEX
C3  L = 128 (r = 7, an ODD tooth):  fraction -> 3/7 = 0.428571

    Tolerance, fixed in advance: ### the measured count is within 3 offenders of the
    integer chain prediction (M - nullity)/2 at every cell. Three is the slack already
    measured for A_main (2-3 positive directions) plus one for the V compression.

BOTH BRANCHES, LONGHAND
========================
IF all three land: the sawtooth is confirmed on teeth 5, 6 and 7, i.e. on cells chosen
BEFORE the measurement and outside every range the law was ever fitted to. The peak at
L = 64 in particular is a return to exactly 1/2 at a window sixteen times the one where
the first apex was found, and the derived law would then have been tested at r = 1..7
without a miss.
IF any fails: the path-graph decomposition is right about S_k (that is a theorem) and
### wrong about the operator at that r, which localizes A_main's contribution to a named
### window length rather than leaving it as a general slack. The failing cell is the
finding and correction twenty is written from it.

Usage:  python sawtooth_cells.py register
        python sawtooth_cells.py run
"""
import math
import sys
import time

import numpy as np

import qeps_layer as Q
import phi_layer as P
import exp1_two_prime as E1
from wonder1_freeze import chain_npos

LOG2 = math.log(2.0)
LS = [32.0, 64.0, 128.0]
OMEGAS = [2.0e-3, 1.0e-3]
TOL = 3


def predictions():
    print("=" * 112)
    print("THE PREDICTIONS, FROM THE ACTUAL (M, k) — BEFORE ANY MEASUREMENT")
    print("=" * 112)
    print("  %-7s %-10s %-8s %-7s %-5s %-7s %-7s %-10s %-12s %s"
          % ("L", "omega", "M", "k", "q", "s", "null", "CHAIN", "fraction", "continuum"))
    for L in LS:
        r_exact = math.log(L) / LOG2
        m = (int(round(r_exact)) + 1) // 2
        cont = (1 - m / r_exact) if int(round(r_exact)) % 2 == 1 else (m / r_exact)
        for om in OMEGAS:
            M = int(round(math.log(L) / om))
            k = int(round(LOG2 / om))
            c, q, s, nul = chain_npos(M, k)
            print("  %-7.1f %-10.1e %-8d %-7d %-5d %-7d %-7d %-10d %-12.6f %.6f"
                  % (L, om, M, k, q, s, nul, c, c / (M - 1), cont))
    print("=" * 112)
    sys.stdout.flush()


def registration():
    print("=" * 112)
    print("THE DISCRIMINATING CELLS — REGISTRATION. NO MEASURED NUMBER IN THIS BLOCK.")
    print("=" * 112)
    print(__doc__)
    predictions()


def run():
    e1p = Q.epsprime1()
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    qvs = {}
    for om in OMEGAS:
        need = int(round(math.log(max(LS)) / om))
        t0 = time.time()
        qvs[om] = P._qvals(om, need, E1.NG_Q)
        print("      [Q_eps table: omega=%.1e, nmax=%d, %.1f s]" % (om, need, time.time() - t0))
        sys.stdout.flush()

    print("\n" + "=" * 112)
    print("THE MEASUREMENT — one lag (log 2), on V")
    print("=" * 112)
    print("  %-7s %-10s %-8s %-14s %-10s %-12s %-12s %s"
          % ("L", "omega", "M", "measured", "CHAIN", "fraction", "predicted", "verdict"))
    rows = []
    for L in LS:
        lags = [x for x in E1.lag_schedule(L) if x[0] == "log 2"]
        for om in OMEGAS:
            t0 = time.time()
            n, dim, frac, M = E1.measure(L, om, lags, qvs[om], e1p)
            k = int(round(LOG2 / om))
            c, q, s, nul = chain_npos(M, k)
            ok = abs(n - c) <= TOL
            rows.append((L, om, M, n, dim, frac, c, ok))
            print("  %-7.1f %-10.1e %-8d %-14s %-10d %-12.6f %-12.6f %s  [%.0fs]"
                  % (L, om, M, "%d/%d" % (n, dim), c, frac, c / dim,
                     "### LANDS (%+d)" % (n - c) if ok else "### FAILS (%+d)" % (n - c),
                     time.time() - t0))
            sys.stdout.flush()

    print("=" * 112)
    good = sum(1 for r in rows if r[7])
    print("  cells landing within %d offenders: %d of %d" % (TOL, good, len(rows)))
    print("\n  --- against the exact continuum values ---")
    print("  %-7s %-10s %-14s %-14s %s" % ("L", "r", "measured", "predicted", "target"))
    for L, om, M, n, dim, frac, c, ok in rows:
        k = int(round(LOG2 / om))
        tgt = {32.0: 2 / 5, 64.0: 1 / 2, 128.0: 3 / 7}[L]
        print("  %-7.1f %-10.4f %-14.6f %-14.6f %.6f (%s)"
              % (L, M / k, frac, c / dim, tgt,
                 {32.0: "2/5", 64.0: "1/2", 128.0: "3/7"}[L]))


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    run()


if __name__ == "__main__":
    main()
