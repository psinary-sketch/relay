"""WONDER TWO — SILENCE ACROSS THE BRANCH: is the negative count coefficient-independent, and why?

Relay-only, bench-grade. NO SIGN SENTENCE. h2 UNCHANGED. NOTHING DEPOSITS.

THE MEASUREMENT THE FERRY ORDERS
=================================
Vary every prime coefficient by 2.5x ON THE LAG BRANCH, L in {4.6, 5.5, 7.0}.
### REGISTERED EXPECTATION: the offender count moves by <= 2 in ~1,945, as it did below the
### branch on 2026-08-17 (0, 0, 1, 1, 2, 2 offenders across six L).

THE DERIVATION, WRITTEN BEFORE THE RUN — AND IT SPLITS THE QUESTION IN TWO
==========================================================================
On the grid the matrix is

    A = A_main + sum_q c_q * (omega/2) * S_{k_q},        A_main = omega * Y^T N_I Y

with S_k the symmetric |i-j| = k shift form of Wonder One, and c_q the prime coefficient.

STEP 1 — SCALE INVARIANCE IS EXACT, AND IT IS SYLVESTER'S LAW.
For t > 0, t*S has the same inertia as S: t*S = (sqrt(t) I) S (sqrt(t) I)^T is a congruence.
### SO IF A_main WERE ABSENT, MULTIPLYING EVERY COEFFICIENT BY A COMMON FACTOR WOULD CHANGE
### NOTHING AT ALL — not approximately, EXACTLY, for every factor and every window.
That is not a measurement waiting to be made; it is a two-line theorem, and it means the
UNIFORM part of "vary the coefficients" cannot possibly move the count except through A_main.

STEP 2 — SHAPE INVARIANCE IS NOT DERIVED AND MUST BE MEASURED.
Changing the coefficients' RATIOS (registered 2 sqrt(q) log p vs Weil 4 log p / sqrt(q)) is
not a congruence. It is a different matrix. ### NOTHING ABOVE PREDICTS IT.

STEP 3 — WHAT A_main CAN DO, AND THE ONE FACT THAT WOULD CLOSE IT.
If A_main is NEGATIVE SEMIDEFINITE then, by Weyl, lam_j(A_main + cS) <= lam_j(cS), so
    ### NPOS(A) <= NPOS(cS) = (M - nullity)/2      for every c > 0,
and in the other direction lam_j(A_main + cS) >= lam_j(cS) - |lam_min(A_main)|, so every
eigenvalue of cS exceeding |lam_min(A_main)| survives. The positive eigenvalues of cS scale
linearly in c while |lam_min(A_main)| is fixed, hence
    ### there is a finite c* above which NPOS(A) = NPOS(S) EXACTLY, and above c* the count is
    ### rigorously coefficient-independent.
### THE WHOLE DERIVATION THEREFORE TURNS ON ONE CHECKABLE FACT: IS A_main NEGATIVE
### SEMIDEFINITE ON V? That is measured below as its own blocking row, not assumed.

REGISTERED PREDICTIONS
=======================
W2-A  (blocking, and it decides the grade) NPOS(A_main alone, on V) = 0 at every L tested,
      i.e. A_main is negative definite on V. IF IT IS NOT, step 3 collapses and the result
      stays MEASURED-AT-BANK with the obstacle named.
W2-B  Uniform rescaling of every coefficient by 2.5x and by 0.4x moves the count by ZERO
      offenders — exactly, not approximately. ### This is the derived half; a single offender
      of movement refutes the claim that A_main is negligible at the working scale.
W2-C  The convention change (registered -> Weil, a change of RATIOS of up to 2.5x) moves the
      count by <= 2 offenders. ### This is the measured half; it is not derived and is not
      claimed to be.
W2-D  Sweeping a common factor t over decades, NPOS(A) locks onto the pure-shift value
      (M - nullity)/2 above some finite t*, and t* is reported as a measured constant.

GRADE RULE, FIXED IN ADVANCE
=============================
* IF W2-A and W2-B both land: the coefficient-independence of the count is ### DERIVED for
  the uniform direction (Sylvester + Weyl, with A_main's definiteness measured), and the
  shape direction stays MEASURED. The self-limit is filed at that split grade and no wider.
* IF W2-A fails: everything stays MEASURED-AT-BANK, said so, obstacle named.

Usage:  python wonder2_silence.py register
        python wonder2_silence.py run
"""
import math
import sys
import time

import numpy as np

import qeps_layer as Q
import phi_layer as P
import exp1_two_prime as E1

LOG2 = math.log(2.0)
LS = [4.6, 5.5, 7.0]
OM = 1.0e-3
SCALES = [0.4, 1.0, 2.5]
TSWEEP = [1e-3, 1e-2, 1e-1, 1.0, 10.0, 100.0]


def scaled(lags, t):
    return [(lab, ell, t * c) for lab, ell, c in lags]


def registration():
    print("=" * 104)
    print("WONDER TWO — REGISTRATION. NO MEASURED NUMBER IN THIS BLOCK.")
    print("=" * 104)
    print(__doc__)
    print("  L values (lag branch):", LS, "   omega =", OM)
    print("  uniform scale factors:", SCALES, "   t-sweep:", TSWEEP)
    print("  registered coefficients vs Weil, per prime power:")
    for q, p, k in E1.prime_powers_below(8.0):
        print("      q=%d  registered %.6f   Weil %.6f   ratio %.3f"
              % (q, E1.coeff(q, p), E1.coeff_weil(q, p), E1.coeff(q, p) / E1.coeff_weil(q, p)))
    print("=" * 104)
    sys.stdout.flush()


def run():
    e1p = Q.epsprime1()
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")
    nmax = int(round(math.log(max(LS)) / OM))
    t0 = time.time()
    qv = P._qvals(OM, nmax, E1.NG_Q)
    print("      [Q_eps table: omega=%.1e, nmax=%d, %.1f s]\n" % (OM, nmax, time.time() - t0))

    # ------------------------------------------------------------------ W2-A, blocking
    print("=" * 104)
    print("W2-A (BLOCKING) — IS A_main NEGATIVE DEFINITE ON V?  (no prime term at all)")
    print("=" * 104)
    print("  %-6s %-8s %-14s %-16s %-16s %s" % ("L", "M", "NPOS(A_main)", "lam_max", "lam_min", "verdict"))
    a_ok = True
    lmins = {}
    for L in LS:
        A, M = E1.phi_matrix_V(L, OM, [], qv, e1p)
        ev = np.linalg.eigvalsh(A)
        npos = int((ev > 0).sum())
        lmins[L] = float(ev[0])
        good = (npos == 0)
        a_ok = a_ok and good
        print("  %-6.1f %-8d %-14d %-16.6e %-16.6e %s"
              % (L, M, npos, float(ev[-1]), float(ev[0]),
                 "NEGATIVE DEFINITE" if good else "### NOT — step 3 collapses"))
        del A, ev
        sys.stdout.flush()
    print("\n  W2-A: %s" % ("PASS — Weyl gives NPOS(A) <= NPOS(cS) for every c > 0"
                            if a_ok else "### FAIL"))

    # ------------------------------------------------------------------ W2-B, uniform scale
    print("\n" + "=" * 104)
    print("W2-B — UNIFORM RESCALING OF EVERY COEFFICIENT (the derived half)")
    print("=" * 104)
    print("  %-6s %-8s %-14s %-14s %-14s %s" % ("L", "M", "x0.4", "x1.0", "x2.5", "spread (offenders)"))
    b_ok = True
    for L in LS:
        lags = E1.lag_schedule(L)
        got = []
        for t in SCALES:
            n, dim, frac, M = E1.measure(L, OM, scaled(lags, t), qv, e1p)
            got.append((n, dim, frac, M))
        spread = max(g[0] for g in got) - min(g[0] for g in got)
        b_ok = b_ok and (spread == 0)
        print("  %-6.1f %-8d %-14s %-14s %-14s %d %s"
              % (L, got[0][3], "%d" % got[0][0], "%d" % got[1][0], "%d" % got[2][0], spread,
                 "" if spread == 0 else "### NONZERO"))
        sys.stdout.flush()
    print("\n  W2-B: %s" % ("PASS — exactly zero movement, as Sylvester requires"
                            if b_ok else "### FAIL — A_main is not negligible at this scale"))

    # ------------------------------------------------------------------ W2-C, shape
    print("\n" + "=" * 104)
    print("W2-C — THE CONVENTION CHANGE, registered -> Weil (the measured half)")
    print("=" * 104)
    print("  %-6s %-8s %-16s %-16s %s" % ("L", "M", "registered", "Weil", "difference"))
    for L in LS:
        n1, d1, f1, M = E1.measure(L, OM, E1.lag_schedule(L, E1.coeff), qv, e1p)
        n2, d2, f2, _ = E1.measure(L, OM, E1.lag_schedule(L, E1.coeff_weil), qv, e1p)
        print("  %-6.1f %-8d %-16s %-16s %+d offenders in %d"
              % (L, M, "%d = %.6f" % (n1, f1), "%d = %.6f" % (n2, f2), n2 - n1, d1))
        sys.stdout.flush()

    # ------------------------------------------------------------------ W2-D, threshold
    print("\n" + "=" * 104)
    print("W2-D — THE LOCK-ON THRESHOLD t*, and the pure-shift target")
    print("=" * 104)
    for L in LS:
        lags = [x for x in E1.lag_schedule(L) if x[0] == "log 2"]   # one lag: the clean case
        M = int(round(math.log(L) / OM))
        k = int(round(LOG2 / OM))
        q, s = divmod(M, k)
        nullity = s if q % 2 == 0 else k - s
        target = (M - nullity) // 2
        print("  L=%.1f  M=%d  k=%d  pure-shift NPOS = (M - nullity)/2 = %d" % (L, M, k, target))
        print("       %-12s %-12s %s" % ("t", "NPOS", "vs pure-shift"))
        for t in TSWEEP:
            n, dim, frac, _ = E1.measure(L, OM, scaled(lags, t), qv, e1p)
            print("       %-12.1e %-12d %+d" % (t, n, n - target))
            sys.stdout.flush()
        print()


def main():
    what = sys.argv[1] if len(sys.argv) > 1 else "run"
    registration()
    if what == "register":
        return
    run()


if __name__ == "__main__":
    main()
