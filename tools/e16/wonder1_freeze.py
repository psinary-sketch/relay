"""WONDER ONE — THE COUNT-FREEZING CONJECTURE: stated, DERIVED at Toeplitz level, then tested.

Relay-only, bench-grade. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.
This is about the remainder route's failure COUNT only.

THE CONJECTURE, AS THE FERRY STATES IT
=======================================
    "for the lag form (eta * eta^*)(l) on a window of length Lambda >= 2l, the number of
     negative directions on V is a fixed function of l/omega, independent of Lambda"

Named precisely, with the object named: let k = round(l/omega) be the lag's address in grid
points and M = round(Lambda/omega) the window's. The measured object is

    NPOS(M, k) := #{ positive eigenvalues of the Phi matrix restricted to V }

and 2026-08-17 measured NPOS = min(k, M - k) to within one grid point, over
Lambda/l = M/k in [1.68, 2.81]. The conjecture is the M >= 2k half of that: NPOS = k,
independent of M.

### THE DERIVATION BELOW SETTLES THE CONJECTURE AND SHOWS IT IS FALSE AS STATED — the
### freezing is real but it is a WINDOW PHENOMENON, not a law, and it ends at Lambda = 3l.

THE DERIVATION — EXACT, ELEMENTARY, AND COMPLETE FOR THE PURE LAG FORM
=======================================================================
The lag term in Phi is, on the grid, a constant times the symmetric matrix

    (S_k)_{ij} = 1 if |i - j| = k,  else 0        (M x M, 1 <= k < M)

STEP 1 — S_k DECOUPLES INTO PATHS. i ~ j only when i = j +/- k, so the index set
{0,...,M-1} splits into the k residue classes mod k, and S_k acts on each class
{r, r+k, r+2k, ...} as the adjacency matrix of a PATH GRAPH on its members.
Writing M = q k + s with 0 <= s < k: ### s chains have length q+1 and k - s have length q.

STEP 2 — THE PATH SPECTRUM IS CLASSICAL AND SYMMETRIC. The adjacency matrix of P_m has
eigenvalues 2 cos(pi j/(m+1)), j = 1..m. They are symmetric about 0, and
### nullity(P_m) = 1 if m is ODD, 0 if m is EVEN (the j = (m+1)/2 mode).

STEP 3 — INERTIA BY COUNTING. Symmetry gives #positive = #negative, so

    ### NPOS(S_k) = ( M - nullity(S_k) ) / 2,     nullity(S_k) = #odd-length chains
                                                 = s      if q is EVEN
                                                 = k - s  if q is ODD

STEP 4 — EVALUATE. With M = qk + s:
    q = 1 :  NPOS = (M - (k - s))/2 = s      = M - k        <- the ROOM branch
    q = 2 :  NPOS = (M - s)/2       = k                     <- the LAG branch
    q = 3 :  NPOS = (M - (k - s))/2 = k + s   = M - 2k
    q = 4 :  NPOS = (M - s)/2       = 2k
    generally, q = 2m-1 : NPOS = M - m k        q = 2m : NPOS = m k

### SO min(k, M-k) IS EXACTLY RIGHT FOR k <= M < 3k AND EXACTLY WRONG BEYOND IT.

STEP 5 — THE CONTINUUM FORM. With r := M/k = log L / log 2 = Lambda/l,
    r in [2m-1, 2m) : fraction -> 1 - m/r        r in [2m, 2m+1) : fraction -> m/r
### A SAWTOOTH. Peaks at exactly 1/2 at r = 2m, i.e. L = 4, 16, 64, ...
### Troughs at m/(2m+1) at r = 2m+1, i.e. L = 8, 32, 128, ... (values 1/3, 2/5, 3/7, ...)
The 2026-08-17 "two-branch law" is ### THE FIRST TWO TEETH, and every L measured that day
had r < 3.

### WHAT THIS DERIVATION IS AND IS NOT
It is an exact theorem about the PURE lag form S_k. The measured object is
A = A_main + c*(omega/2)*S_k restricted to V, where A_main = omega * Y^T N_I Y. The
derivation says nothing about A_main. Empirically A_main moved the count by at most one
offender for r < 3; ### WHETHER THAT PERSISTS FOR r > 3 IS EXACTLY WHAT IS MEASURED BELOW,
### AND IT IS NOT PREDICTED BY THE DERIVATION.
Two further slacks, both bounded: the V restriction is a rank-one compression, so by Cauchy
interlacing it changes NPOS by at most 1; and rounding gives k, M as integers, handled by
evaluating the chain formula on the actual integers rather than in the continuum.

REGISTERED PREDICTIONS, BEFORE ANY NUMBER
==========================================
For each L the two candidates are computed from the ACTUAL (M, k) and printed first:
    CHAIN  := (M - nullity)/2 from step 3          MIN := min(k, M - k)
They coincide for r < 3 and separate sharply above it.

P1  At L = 8.0 (r = 3.000, the trough) CHAIN and MIN agree; the row is a CONTINUITY CHECK
    and discriminates nothing. Registered as non-discriminating so it cannot later be
    counted as support.
P2  At L = 9, 12, 16, 20 the two differ by 0.054, 0.163, 0.250, 0.231 in fraction.
    ### THE MEASUREMENT FALLS WITHIN 3 OFFENDERS OF CHAIN AND FAR FROM MIN.
    Then: the lag branch and the room branch are both DERIVED as the q = 2 and q = 1 cases
    of one exact combinatorial theorem, the 2026-08-17 "two-branch law" is superseded by the
    sawtooth, and the freezing conjecture is answered NO — the count freezes only while
    2 <= r < 3.
P3  IF the measurement instead tracks MIN, the derivation is right about S_k and wrong about
    the operator: A_main would then be doing work of order the whole count, not one offender,
    and ### the finding is that the lag form does NOT govern the count outside r < 3.
P4  IF it tracks NEITHER, both are refuted, the numbers are reported as measured, and the
    obstacle is named as A_main's uncontrolled contribution at large r.

Usage:  python wonder1_freeze.py register
        python wonder1_freeze.py run
"""
import math
import sys
import time

import numpy as np

import qeps_layer as Q
import phi_layer as P
import exp1_two_prime as E1

LOG2 = math.log(2.0)
LS = [8.0, 9.0, 12.0, 16.0, 20.0]
OMEGAS = [2.0e-3, 1.0e-3]
OMEGA_FINE = {9.0: 5.0e-4}          # one convergence check, priced and stated


def chain_npos(M, k):
    """Exact NPOS of the pure lag form S_k on M points, from the derivation (steps 1-3)."""
    q, s = divmod(M, k)
    nullity = s if q % 2 == 0 else k - s
    return (M - nullity) // 2, q, s, nullity


def predictions():
    print("=" * 108)
    print("THE TWO CANDIDATES, COMPUTED FROM THE ACTUAL (M, k) — BEFORE ANY MEASUREMENT")
    print("=" * 108)
    print("  %-6s %-10s %-7s %-6s %-6s %-6s %-5s %-10s %-10s %s"
          % ("L", "omega", "M", "k", "q", "s", "null", "CHAIN", "MIN", "fractions (chain | min)"))
    for L in LS:
        oms = OMEGAS + ([OMEGA_FINE[L]] if L in OMEGA_FINE else [])
        for om in oms:
            M = int(round(math.log(L) / om))
            k = int(round(LOG2 / om))
            c, q, s, nul = chain_npos(M, k)
            mn = min(k, M - k)
            dim = M - 1
            print("  %-6.1f %-10.1e %-7d %-6d %-6d %-6d %-5d %-10d %-10d %.6f | %.6f"
                  % (L, om, M, k, q, s, nul, c, mn, c / dim, mn / dim))
    print("=" * 108)
    sys.stdout.flush()


def registration():
    print("=" * 108)
    print("WONDER ONE — REGISTRATION. NO MEASURED NUMBER IN THIS BLOCK.")
    print("=" * 108)
    print(__doc__)
    predictions()


def run():
    e1p = Q.epsprime1()
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    print("  eps'(1+) = %.7f\n" % e1p)

    allom = sorted({om for L in LS for om in (OMEGAS + ([OMEGA_FINE[L]] if L in OMEGA_FINE else []))},
                   reverse=True)
    qvs = {}
    for om in allom:
        need = max(int(round(math.log(L) / om)) for L in LS
                   if om in OMEGAS or OMEGA_FINE.get(L) == om)
        t0 = time.time()
        qvs[om] = P._qvals(om, need, E1.NG_Q)
        print("      [Q_eps table: omega=%.1e, nmax=%d, %.1f s]" % (om, need, time.time() - t0))
        sys.stdout.flush()

    W = 118
    print("\n" + "=" * W)
    print("THE MEASUREMENT — one lag (log 2), on V, all rows")
    print("=" * W)
    print("  %-6s %-10s %-7s %-12s %-10s %-10s %-11s %-11s %s"
          % ("L", "omega", "M", "measured", "CHAIN", "MIN", "meas-CHAIN", "meas-MIN", "verdict"))
    rows = []
    for L in LS:
        lags = [x for x in E1.lag_schedule(L) if x[0] == "log 2"]
        oms = OMEGAS + ([OMEGA_FINE[L]] if L in OMEGA_FINE else [])
        for om in oms:
            n, dim, frac, M = E1.measure(L, om, lags, qvs[om], e1p)
            k = int(round(LOG2 / om))
            c, q, s, nul = chain_npos(M, k)
            mn = min(k, M - k)
            v = ("### CHAIN" if abs(n - c) <= 3 else
                 ("### MIN" if abs(n - mn) <= 3 else "### NEITHER"))
            rows.append((L, om, M, n, dim, frac, c, mn, v))
            print("  %-6.1f %-10.1e %-7d %-12s %-10d %-10d %-11s %-11s %s"
                  % (L, om, M, "%d/%d" % (n, dim), c, mn,
                     "%+d" % (n - c), "%+d" % (n - mn), v))
            sys.stdout.flush()

    print("=" * W)
    nch = sum(1 for r in rows if r[8] == "### CHAIN")
    nmn = sum(1 for r in rows if r[8] == "### MIN")
    nnn = sum(1 for r in rows if r[8] == "### NEITHER")
    print("  cells tracking CHAIN: %d   MIN: %d   NEITHER: %d   (of %d)" % (nch, nmn, nnn, len(rows)))
    disc = [r for r in rows if r[0] != 8.0]
    dch = sum(1 for r in disc if r[8] == "### CHAIN")
    print("  DISCRIMINATING cells only (L != 8.0, where the candidates differ): %d of %d track CHAIN"
          % (dch, len(disc)))
    print("\n  --- fractions against the sawtooth, continuum form ---")
    print("  %-6s %-10s %-12s %-12s %-12s" % ("L", "r = M/k", "measured", "sawtooth", "min-law"))
    for L, om, M, n, dim, frac, c, mn, v in rows:
        k = int(round(LOG2 / om))
        r = M / k
        print("  %-6.1f %-10.4f %-12.6f %-12.6f %-12.6f" % (L, r, frac, c / (M - 1), mn / (M - 1)))


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    run()


if __name__ == "__main__":
    main()
