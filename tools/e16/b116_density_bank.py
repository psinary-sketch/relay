# -*- coding: utf-8 -*-
"""b116 -- THE DENSITY BANKING (the thirteenth seam close's strikeable).

Psi is banked as a first-class object at BENCH grade. This script emits its
profile only; it decides nothing, derives nothing, and asserts nothing about
any location or resemblance. THE GUARD: no location sentence, no resemblance,
ZERO interpretive weight on any numerical coincidence.

Provenance of every quantity below: b38's own machinery (family, trace_modes,
per_mode_eps_grids, e2_of_grid) and carto_atlas.bump, via b115's extraction.
"""
import math, sys
import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38
import b115_mechanism as M
import qeps_layer as Q

NMODE = B38.TRIPLE[1][1]


def main():
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(B38.EPS_NQ)
    t_n = lam2 / (1 - lam2) * xi1 ** 2
    s = t_n[:NMODE] / float(t_n[:NMODE].sum())
    sig = float(s[0::2].sum())

    umax = 2.0 * math.log(math.sqrt(48.001))
    ug = np.linspace(0.0, umax, 400)
    psi, phiA, phiE = M.psi_density(ug, sig)

    print("=" * 78)
    print("b116 -- THE DENSITY BANK: Psi's profile at BENCH grade")
    print("  NMODE = %d, sigma_even = %.12f, u range [0, %.6f]" % (NMODE, sig, umax))
    print("=" * 78)

    print("\n--- PROFILE (bench; u = log of the dilation ratio) ---")
    print("%8s %12s %12s %12s" % ("u", "Psi", "phi_A", "phi_e"))
    for uq in (0.0, 0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 2.5, 3.0, 3.5, umax):
        j = int(np.abs(ug - uq).argmin())
        print("%8.4f %12.6f %12.6f %12.6f" % (ug[j], psi[j], phiA[j], phiE[j]))

    sc = [i for i in range(len(psi) - 1) if psi[i] * psi[i + 1] < 0]
    dpsi = np.gradient(psi, ug)
    dsc = [i for i in range(len(dpsi) - 2) if dpsi[i + 1] * dpsi[i + 2] < 0]
    print("\n--- SIGN STRUCTURE (bench) ---")
    print("  Psi sign changes on the range: %d" % len(sc))
    print("  Psi' sign changes on the range: %d" % len(dsc))
    print("  Psi(0) = %+.9f   Psi(umax) = %+.9f" % (psi[0], psi[-1]))
    print("  min Psi = %+.9f ; max Psi = %+.9f" % (psi.min(), psi.max()))

    print("\n--- MEAN STRUCTURE (bench) ---")
    mean = float(np.trapezoid(psi, ug) / umax)
    l1 = float(np.trapezoid(np.abs(psi), ug) / umax)
    print("  unweighted mean of Psi over the range      = %+.9f" % mean)
    print("  unweighted mean of |Psi| over the range    = %+.9f" % l1)
    print("  ratio |mean| / mean|Psi|                   =  %.6f" % (abs(mean) / l1))
    print("  (the ratio is reported as a descriptor of how much of Psi survives an")
    print("   unweighted average; it is NOT the mean-zero average of the open step)")

    print("\n--- phi_e's STRUCTURE (bench), the derived reading beside it ---")
    print("  max |phi_e| = %.9f at u = %.4f" % (np.abs(phiE).max(), ug[int(np.abs(phiE).argmax())]))
    print("  phi_e(0) = %.3e  [DERIVED: e_n(0) = 0 exactly, empty integration range]" % phiE[0])
    print("  phi_e -> %.3e at umax" % phiE[-1])
    print("  [DERIVED: phi_e measures departure from t-proportionality and would")
    print("   vanish identically if e_n were t_n times a mode-independent function,")
    print("   because sigma_even IS the t-mass even share.]")

    print("\n--- K's PROVENANCE AND THE EXACT HALF (bench + derived) ---")
    a0 = math.sqrt(12)
    v, w2, corr, vc, L0 = B38.family(a0)
    sg = np.linspace(0.0, 2.0, 4001)
    K = L0 * np.interp(L0 * sg, vc, corr)
    print("  K(sigma) := L * C_a(L*sigma), the rescaled window autocorrelation")
    print("  provenance: carto_atlas.bump -> conv(w,w); a-free (b115 check 3, 5.96e-14)")
    print("  K(0) = %.9f   K(2) = %.3e   min K = %.3e" % (K[0], K[-1], K.min()))
    print("  int_0^2 K d sigma = %.9f   [DERIVED: exactly 1/2, K even with total 1]"
          % float(np.trapezoid(K, sg)))

    print("\nTHE GUARD: no location is asserted; no resemblance is asserted; every")
    print("number above carries BENCH grade and ZERO interpretive weight.")


main()
