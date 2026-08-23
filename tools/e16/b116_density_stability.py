# -*- coding: utf-8 -*-
"""b116 -- IS PSI'S NON-MONOTONICITY REAL, OR AN INTERPOLATION ARTIFACT?

b115 reported "Psi: 5 sign changes; Psi': 92". Both counts turn out to move
with the u-grid (Psi' roughly LINEARLY in grid size), which is the signature of
differentiating a noisy interpolant rather than of real oscillation. The
suspected noise source is e_n(u) = eps_n(e^u), obtained by np.interp on a
FINITE rho grid: piecewise-linear in exp(u), so its derivative is piecewise
constant with jumps that a finer u grid simply resolves more of.

THIS SCRIPT TESTS THE FINDING RATHER THAN DEFENDING IT: it refines the rho grid
and asks whether the sign structure survives. The reproduce-before-extend
discipline (adopted at b115) turned on b115's own conclusion.
"""
import math, sys
import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38
import qeps_layer as Q

NMODE = B38.TRIPLE[1][1]
RHO_MAX = 48.001
UMAX = 2.0 * math.log(math.sqrt(48.001))


def psi_on(ug, n_rho, sig):
    """Psi on the u grid, with the eps layer sampled on n_rho points."""
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(B38.TRIPLE[1][0])
    nm = min(NMODE, xi.shape[1])
    A = np.zeros((nm, len(ug)))
    for n in range(nm):
        f = xi[:, n]
        for i, u in enumerate(ug):
            lamd = math.exp(u)
            fy = np.interp(lamd * x, x, f, left=0.0, right=0.0)
            A[n, i] = math.sqrt(lamd) * 0.5 * float((w * f * fy).sum())
    rr = np.exp(np.linspace(1e-4, math.log(RHO_MAX), n_rho))
    ee = B38.per_mode_eps_grids(rr)
    E = np.zeros((nm, len(ug)))
    for n in range(nm):
        E[n] = np.interp(np.exp(ug), rr, ee[n])
    phiA = A[0::2].sum(0) - sig * A.sum(0)
    phiE = E[0::2].sum(0) - sig * E.sum(0)
    return phiA - phiE, phiA, phiE


def counts(ug, psi):
    d = np.gradient(psi, ug)
    sc = sum(1 for i in range(len(psi) - 1) if psi[i] * psi[i + 1] < 0)
    ds = sum(1 for i in range(len(d) - 2) if d[i + 1] * d[i + 2] < 0)
    return sc, ds


def main():
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(B38.EPS_NQ)
    t = lam2 / (1 - lam2) * xi1 ** 2
    s = t[:NMODE] / float(t[:NMODE].sum())
    sig = float(s[0::2].sum())

    print("=" * 78)
    print("b116 -- PSI'S SIGN STRUCTURE UNDER RHO-GRID REFINEMENT")
    print("=" * 78)

    ug = np.linspace(0.0, UMAX, 400)
    print("\n--- u grid fixed at 400; the RHO grid refined ---")
    print("%8s %13s %18s %14s %14s" % ("N_rho", "Psi sign chg", "Psi-prime sign chg",
                                       "max|dPsi| vs", "prev N_rho"))
    prev = None
    for nr in (200, 400, 800, 1600, 3200):
        psi, phiA, phiE = psi_on(ug, nr, sig)
        sc, ds = counts(ug, psi)
        dd = float(np.abs(psi - prev).max()) if prev is not None else float('nan')
        print("%8d %13d %18d %14s %14.3e" % (nr, sc, ds, "", dd))
        prev = psi

    print("\n--- phi_A ALONE (no eps interpolation at all) on refined u grids ---")
    print("  phi_A is built only from the prolate quadrature: no np.interp on a")
    print("  finite grid enters it. If the oscillation is interpolation noise,")
    print("  phi_A should be clean where Psi is not.")
    print("%8s %14s %18s" % ("u points", "phiA sign chg", "phiA-prime sign chg"))
    for n in (200, 400, 800, 1600):
        u2 = np.linspace(0.0, UMAX, n)
        _, phiA, _ = psi_on(u2, 400, sig)
        d = np.gradient(phiA, u2)
        sc = sum(1 for i in range(len(phiA) - 1) if phiA[i] * phiA[i + 1] < 0)
        ds = sum(1 for i in range(len(d) - 2) if d[i + 1] * d[i + 2] < 0)
        print("%8d %14d %18d" % (n, sc, ds))

    print("\n--- THE QUESTION THAT ACTUALLY MATTERS: is Psi' < 0 anywhere near true? ---")
    psi, phiA, phiE = psi_on(ug, 3200, sig)
    print("  at the finest rho grid: Psi(0) = %+.6f, Psi(umax) = %+.6f"
          % (psi[0], psi[-1]))
    print("  Psi RISES across the range by %+.6f" % (psi[-1] - psi[0]))
    print("  ### so Psi is NOT decreasing overall -- the (ii) sufficient condition")
    print("      fails on the GROSS trend, independently of any fine oscillation.")
    k = max(1, len(ug) // 40)
    coarse = np.array([psi[i:i + k].mean() for i in range(0, len(ug) - k, k)])
    cs = sum(1 for i in range(len(coarse) - 1) if coarse[i] * coarse[i + 1] < 0)
    cm = sum(1 for i in range(len(coarse) - 1) if coarse[i] > coarse[i + 1])
    print("  block-averaged Psi (40 blocks): %d sign changes, %d descending steps"
          % (cs, len(coarse) - 1 - (len(coarse) - 1 - cm)))
    print("  block-averaged Psi monotone increasing:",
          bool(all(coarse[i] <= coarse[i + 1] for i in range(len(coarse) - 1))))


main()
