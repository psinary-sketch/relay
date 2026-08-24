# -*- coding: utf-8 -*-
"""b131 -- G1: does CM's W (arXiv 2112.05500 eq. 1) commute with THE LAYER'S
ACTUAL INTEGRAL KERNEL at the recorded parameters?

THE GATE IS NOT AN ARITHMETIC MATCH. The layer stores no differential operator,
so there is nothing to compare symbol-to-symbol. The gate asks whether CM's W,
instantiated at the layer's own parameters, has THE LAYER'S OWN EIGENVECTORS --
the ones its integral kernel actually produced.

CM eq. (1), read at content at b130:
    (W_l xi)(x) = -d_x (l^2 - x^2) d_x xi(x) + (2 pi l)^2 x^2 xi(x)
At l = 1 (the layer's interval is [-1,1]) this is
    W xi = -d_x (1 - x^2) d_x xi + (2 pi)^2 x^2 xi
and the layer's c = 2 pi gives c^2 = (2 pi)^2. THAT ARITHMETIC IS NOT THE GATE;
the commutation is.

METHOD, chosen so no second derivative is ever taken numerically. In the
orthonormal Legendre basis P~_k:
  (i)  -d_x(1-x^2)d_x P_k = k(k+1) P_k                    [Legendre's equation]
       so the first term is EXACTLY diag(k(k+1)).
  (ii) x P~_k = a_k P~_{k+1} + a_{k-1} P~_{k-1},  a_k = (k+1)/sqrt((2k+1)(2k+3))
       so multiplication by x is the tridiagonal X, and x^2 is X @ X, EXACT.
  => W = diag(k(k+1)) + c^2 (X @ X), exact in this basis, no differentiation.
Then the layer's own xi_n are expanded in that basis and tested as eigenvectors.
"""
import functools, math, sys
import numpy as np

print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import qeps_layer as Q
import prolate_layer as PL

NQ = 700
NLEG = 80
C = PL.C
NMODE = 10


def legendre_vals(nleg, x):
    """orthonormal Legendre P~_k(x), k = 0..nleg-1, by the standard recurrence."""
    P = np.zeros((nleg, len(x)))
    P[0] = 1.0
    if nleg > 1:
        P[1] = x
    for k in range(1, nleg - 1):
        P[k + 1] = ((2 * k + 1) * x * P[k] - k * P[k - 1]) / (k + 1)
    for k in range(nleg):
        P[k] *= math.sqrt((2 * k + 1) / 2.0)
    return P


def main():
    print("=" * 78)
    print("b131 -- G1: CM's W against THE LAYER'S ACTUAL KERNEL")
    print("=" * 78)
    print("\n  layer parameters read at content: c = %.12f  (= 2*pi: %s)"
          % (C, abs(C - 2 * math.pi) < 1e-15))
    print("  CM eq.(1) at lambda = 1 gives the x^2 coefficient (2*pi*1)^2 = %.9f" % (2 * math.pi) ** 2)
    print("  the layer's c^2                                    = %.9f" % (C ** 2))
    print("  ### the two numbers meet: %s" % (abs((2 * math.pi) ** 2 - C ** 2) < 1e-12))
    print("  *** BUT THAT IS NOT THE GATE. The gate is commutation. ***")

    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(NQ)

    # W in the orthonormal Legendre basis -- exact, no numerical differentiation
    k = np.arange(NLEG)
    a = (k + 1) / np.sqrt((2 * k + 1) * (2 * k + 3))
    X = np.zeros((NLEG, NLEG))
    for j in range(NLEG - 1):
        X[j + 1, j] = a[j]
        X[j, j + 1] = a[j]
    W = np.diag((k * (k + 1)).astype(float)) + (C ** 2) * (X @ X)

    # the layer's own eigenvectors, expanded in that basis
    P = legendre_vals(NLEG, x)
    A = (P * w) @ xi[:, :NMODE]          # A[k, n] = <P~_k, xi_n>

    print("\n--- THE CHAIN ---")
    print("  (1) Legendre completeness of the layer's own modes (how much of each")
    print("      xi_n the %d-term basis captures; 1.000000 = fully captured):" % NLEG)
    cap = (A ** 2).sum(axis=0)
    print("      " + "  ".join("%.6f" % v for v in cap))
    if cap.min() < 1 - 1e-9:
        print("      *** basis truncation is not clean; the test below is invalid. ***")

    print("\n  (2) IS EACH LAYER EIGENVECTOR AN EIGENVECTOR OF W?")
    print("      Rayleigh quotient chi_n, and the relative residual |W a - chi a|/|a|")
    print("%6s %18s %18s %16s" % ("n", "lambda^2 (layer)", "chi_n (from W)", "rel residual"))
    worst = 0.0
    chis = []
    for n in range(NMODE):
        v = A[:, n]
        nv = np.linalg.norm(v)
        Wv = W @ v
        chi = float(v @ Wv) / float(nv ** 2)
        chis.append(chi)
        r = float(np.linalg.norm(Wv - chi * v) / nv)
        worst = max(worst, r)
        print("%6d %18.9e %18.9f %16.3e" % (n, lam2[n], chi, r))
    print("\n  ### WORST RELATIVE RESIDUAL OVER THE TEN MODES = %.3e" % worst)

    print("\n  (3) THE ORDERING CHECK -- a commuting operator must order the modes")
    print("      the same way. chi_n increasing while lambda^2 decreases:")
    inc = all(chis[i] < chis[i + 1] for i in range(len(chis) - 1))
    dec = all(lam2[i] > lam2[i + 1] for i in range(NMODE - 1))
    print("      chi strictly increasing : %s ; lambda^2 strictly decreasing : %s" % (inc, dec))

    print("\n  (4) THE OFF-DIAGONAL CHECK -- W in the layer's own basis must be")
    print("      DIAGONAL if the two operators share eigenvectors:")
    Wmn = A.T @ W @ A
    d = np.diag(np.diag(Wmn))
    off = float(np.abs(Wmn - d).max())
    print("      max |<xi_m, W xi_n>| for m != n = %.3e" % off)
    print("      (diagonal entries range %.3f .. %.3f)" % (np.diag(Wmn).min(), np.diag(Wmn).max()))

    print("\n" + "=" * 78)
    ok = worst < 1e-6 and off < 1e-6 and inc and dec
    print("### G1 VERDICT: %s" % ("MATCHED-UP-TO-NAMED-NORMALIZATION" if ok else "NOT-MATCHED"))
    if ok:
        print("### THE NAMED NORMALIZATION, stated exactly:")
        print("    (i)  lambda = 1 -- CM's half-width is the layer's interval [-1,1];")
        print("    (ii) the layer's c = 2*pi enters as CM's (2*pi*lambda)^2 = c^2;")
        print("    (iii) SIGN/AFFINE: W as written is POSITIVE and orders the modes")
        print("         OPPOSITELY to lambda^2 -- largest lambda^2 at SMALLEST chi.")
        print("    The classical Slepian form is the negative of CM's expression.")
    print("=" * 78)


main()
