"""LEMMA 5.2, ADDENDUM — is the term-tail a SERIES tail or a QUADRATURE floor?

Relay-only, bench-grade. NO SIGN SENTENCE. NOTHING DEPOSITS.

WHY THIS ADDENDUM EXISTS
=========================
lemma52_probe.py reported that the number of terms needed for 1e-11 relative accuracy grows
with rho — 7 terms at rho = 1.5, 14 at rho = 3, "> 48" at rho = 6 and 8. Read as a series
statement that is a REGIME-BOUND verdict.

### BUT THE TERM LADDER DOES NOT LOOK LIKE A SLOWLY-CONVERGING SERIES. It looks like a fast
### one sitting on a floor:

    rho=20   1.0e+02  8.0e+01  3.8e+01  6.5e+00  3.7e-01  1.1e-02  1.5e-04  2.7e-07
             3.2e-09 | 1.1e-07  6.3e-08  5.0e-09  2.1e-07  5.6e-07  4.3e-08  1.2e-09

Terms 0..8 fall by eleven orders, monotonically. Terms 9.. sit at ~1e-7 and do NOT decay —
and the level of that plateau GROWS with rho (about 1e-14 at rho = 1.5, about 1e-7 at
rho = 20), which is the signature of a QUADRATURE ERROR, not of a series.

### THE STANDING LAW THIS SITS UNDER: a false negative in a verification instrument is worse
### than no instrument, since it invites a repair of something that is not broken. Reporting
### "the series needs 48 terms at rho = 8" when the instrument's own noise is 1e-7 would be
### exactly that.

REGISTERED PREDICTION, BEFORE THE RUN
======================================
F1  IF the plateau is quadrature, refining NQ (the prolate grid) and NG (the C_n integral)
    ### LOWERS THE PLATEAU AND LEAVES TERMS 0..8 UNCHANGED to the digits they already agree
    on. The "terms needed" count then falls back toward ~9 at every rho, and Lemma F.1's
    11-term claim survives at every rho tested.
F2  IF the plateau is the series, refinement ### DOES NOT MOVE IT: the terms at n >= 9 are
    real and the truncation requirement genuinely grows with rho. That is the REGIME-BOUND
    verdict, and it would be named at the truncation rather than at the formula.

    ### F1 IS THE EXPECTED OUTCOME AND IS WRITTEN DOWN AS SUCH, so landing it counts for
    ### less and failing it counts for more.

Usage:  python lemma52_floor.py
"""
import math
import sys

import numpy as np

import lemma52_probe as LP

RHOS = [3.0, 8.0, 20.0]
SETTINGS = [(500, 300), (700, 400), (1000, 700), (1400, 1000)]


def main():
    print("=" * 104)
    print("LEMMA 5.2 ADDENDUM — QUADRATURE FLOOR vs SERIES TAIL")
    print("=" * 104)
    print(__doc__)
    print("\n### REGISTRATION CLOSED. MEASUREMENT BEGINS.\n")

    cache = {}
    for nq, ng in SETTINGS:
        if nq not in cache:
            cache[nq] = LP.layer(LP.NMAX, nq)
        lam2, A, D = cache[nq]
        print("=" * 104)
        print("NQ = %d (prolate nodes)   NG = %d (C_n quadrature)" % (nq, ng))
        print("=" * 104)
        for r in RHOS:
            c = LP.chat(r, lam2, A, D, ng)
            term = np.abs(c / (1 - lam2))
            head = " ".join("%8.1e" % v for v in term[:9])
            plateau = float(np.median(term[12:40]))
            total = float((c / (1 - lam2)).sum())
            p11 = float((c[:11] / (1 - lam2[:11])).sum())
            need = LP.NMAX
            for N in range(1, LP.NMAX + 1):
                if abs(float((c[:N] / (1 - lam2[:N])).sum()) - total) <= 1e-11 * abs(total):
                    need = N
                    break
            print("  rho=%-6.1f n=0..8: %s" % (r, head))
            print("           plateau (median |term|, n=12..39) = %.2e   11-term rel err = %.2e   n needed = %s"
                  % (plateau, abs(p11 - total) / abs(total),
                     need if need < LP.NMAX else ">%d" % LP.NMAX))
            sys.stdout.flush()
        print()

    print("=" * 104)
    print("READ: if the n=0..8 columns are stable across the four settings while the plateau")
    print("falls, F1 lands and the tail is the instrument. If the plateau is stable, F2 lands.")
    print("=" * 104)


if __name__ == "__main__":
    main()
