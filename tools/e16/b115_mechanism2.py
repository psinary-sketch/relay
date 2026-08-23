# -*- coding: utf-8 -*-
"""b115 -- the derivative's sharpened form, checked.

Written AFTER check 5 refuted the obvious sufficient condition (Psi' < 0),
and BEFORE any verdict was recorded. The circularity gate stands: the b113
deviation pattern is not read here either.

  N(L) = 2 * int_0^2 K(sigma) Psi(L sigma) d sigma
  dN/dL = 2 * int_0^2 K(sigma) sigma Psi'(L sigma) d sigma
        = (2/L^2) * int_0^{2L} K(u/L) u Psi'(u) du
  integrate by parts, using K(2) = 0 (the autocorrelation vanishes at its
  support edge) and the u = 0 endpoint term vanishing:
        = -(2/L^2) * int_0^{2L} PhiK(u/L) Psi(u) du,  PhiK(s) := d/ds [ s K(s) ]
  and  int_0^2 PhiK ds = [ s K(s) ]_0^2 = 0.
  ### So dN/dL is a MEAN-ZERO scale-average of Psi: insensitive to Psi's
  constant part, sensitive to its trend -- which is how an OSCILLATING Psi can
  produce a MONOTONE N.
"""
import math, sys
import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38
import b115_mechanism as M
import qeps_layer as Q

CELLS = [math.sqrt(2), math.sqrt(3), 2.0, math.sqrt(8), 3.0, math.sqrt(12),
         4.0, math.sqrt(24), math.sqrt(48)]


def main():
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(B38.EPS_NQ)
    t_n = lam2 / (1 - lam2) * xi1 ** 2
    s = t_n[:B38.TRIPLE[1][1]] / float(t_n[:B38.TRIPLE[1][1]].sum())
    sig = float(s[0::2].sum())

    # K on [0,2], from the window's own autocorrelation (a-free, check 3)
    a0 = math.sqrt(12)
    v, w2, corr, vc, L0 = B38.family(a0)
    sg = np.linspace(0.0, 2.0, 4001)
    K = L0 * np.interp(L0 * sg, vc, corr)

    print("=" * 78)
    print("b115 -- THE DERIVATIVE'S SHARPENED FORM")
    print("=" * 78)
    print("\n--- the kernel's endpoint and the mean-zero property, both DERIVED ---")
    print("  K(2) = %.3e   (derivation: 0, the autocorrelation's support edge)" % K[-1])
    PhiK = np.gradient(sg * K, sg)
    print("  int_0^2 PhiK ds = %.3e   (derivation: [s K(s)]_0^2 = 0)"
          % float(np.trapezoid(PhiK, sg)))
    print("  PhiK changes sign: %d time(s) -- a MEAN-ZERO kernel, as derived"
          % int(sum(1 for i in range(len(PhiK) - 1) if PhiK[i] * PhiK[i + 1] < 0)))

    print("\n--- dN/dL by the two derived forms, and by direct difference ---")
    print("%-8s %14s %14s %14s" % ("a^2", "dN/dL direct", "form A (Psi')", "form B (PhiK)"))
    for a in CELLS:
        L = math.log(a)
        h = 1e-4
        ug = np.linspace(0.0, 2 * L, 2001)
        psi, _, _ = M.psi_density(ug, sig)

        def Nof(Lx):
            uq = Lx * sg
            return 2.0 * float(np.trapezoid(K * np.interp(uq, ug, psi, right=psi[-1]), sg))

        direct = (Nof(L + h) - Nof(L - h)) / (2 * h)
        dpsi = np.gradient(psi, ug)
        formA = 2.0 * float(np.trapezoid(
            K * sg * np.interp(L * sg, ug, dpsi, right=dpsi[-1]), sg))
        formB = -(2.0 / L ** 2) * float(np.trapezoid(
            np.interp(ug / L, sg, PhiK, right=0.0) * psi, ug))
        print("%-8.0f %14.6f %14.6f %14.6f" % (a * a, direct, formA, formB))

    print("\n--- the sign question, stated as the derivation leaves it ---")
    print("  MONOTONICITY OF N  <=>  the MEAN-ZERO scale-average of Psi keeps one sign")
    print("  on the licensed L-range. Psi itself oscillates (5 sign changes; Psi' 92),")
    print("  so NO pointwise condition on Psi delivers it. THE STEP IS NAMED AND OPEN.")


main()
