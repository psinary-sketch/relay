# -*- coding: utf-8 -*-
"""b121 -- THE INSTRUMENT SITTING.

Component 1: the prolate bound (P1), including THE EIGENBASIS CHECK registered
in data/b121_registration_2026-08-23.txt -- the one perturbation the record has
never varied.

Component 2: the continuum step (P2) -- a Lipschitz modulus for I(L), the mesh
times the modulus, and the total against b117/b119's margins.

THE GATE, per the standing law, applied to this tool before any new claim: it
must reproduce the banked cells at NQ = 700 (the recorded configuration) before
any varied-NQ number is read.
"""
import math, sys
import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38
import qeps_layer as Q

UMAX = 2.0 * math.log(math.sqrt(48.001))
RHO_MAX = 48.001
NMODE = B38.TRIPLE[1][1]
CELLS = [2, 3, 4, 8, 9, 12, 16, 24, 48]

# b117/b119 banked values, for the gate (reproduce before extend)
BANKED_I = {2: -0.083077396, 3: -0.059667687, 4: -0.060113821, 8: -0.071923801,
            9: -0.073759303, 12: -0.077118973, 16: -0.078592093,
            24: -0.077818000, 48: -0.070591879}


def psi_at(NQ, ug, n_rho=800):
    """Psi on the u grid with the prolate layer built at quadrature size NQ."""
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(NQ)
    nm = min(NMODE, xi.shape[1])
    tn = lam2 / (1 - lam2) * xi1 ** 2
    s = tn[:nm] / float(tn[:nm].sum())
    sig = float(s[0::2].sum())
    A = np.zeros((nm, len(ug)))
    for n in range(nm):
        f = xi[:, n]
        for i, u in enumerate(ug):
            lamd = math.exp(u)
            fy = np.interp(lamd * x, x, f, left=0.0, right=0.0)
            A[n, i] = math.sqrt(lamd) * 0.5 * float((w * f * fy).sum())
    rr = np.exp(np.linspace(1e-4, math.log(RHO_MAX), n_rho))
    # the eps layer is built at its own fixed quadrature; only the prolate
    # basis is being varied here, which is the registered perturbation
    ee = B38.per_mode_eps_grids(rr)
    E = np.zeros((nm, len(ug)))
    for n in range(min(nm, ee.shape[0])):
        E[n] = np.interp(np.exp(ug), rr, ee[n])
    psi = (A[0::2].sum(0) - sig * A.sum(0)) - (E[0::2].sum(0) - sig * E.sum(0))
    return psi, sig


def build_kernel():
    a0 = math.sqrt(12)
    v, w2, corr, vc, L0 = B38.family(a0)
    sg = np.linspace(0.0, 2.0, 2001)
    K = L0 * np.interp(L0 * sg, vc, corr)
    Phi = np.gradient(sg * K, sg)
    return sg, K, Phi


def I_of_L(L, sg, Phi, ug, psi):
    q = np.interp(L * sg, ug, psi, right=psi[-1])
    return float(np.trapezoid(Phi * q, sg))


def main():
    sg, K, Phi = build_kernel()
    ug = np.linspace(0.0, UMAX, 400)

    print("=" * 78)
    print("b121 -- THE INSTRUMENT SITTING")
    print("=" * 78)

    # ---------- THE GATE ----------
    print("\n--- THE GATE ON THIS TOOL (banked cells reproduced at NQ = 700 first) ---")
    psi700, sig700 = psi_at(700, ug)
    worst = 0.0
    for a2 in CELLS:
        L = math.log(math.sqrt(a2))
        val = I_of_L(L, sg, Phi, ug, psi700)
        d = abs(val - BANKED_I[a2])
        worst = max(worst, d)
    print("  worst |I(L) reproduced - I(L) banked| over the nine cells = %.2e" % worst)
    ok = worst < 1e-6
    print("  %s" % ("*** GATE PASSES. Varied-NQ numbers may be read. ***" if ok
                    else "*** GATE FAILED -- HALT. ***"))
    if not ok:
        return

    # ---------- THE EIGENBASIS CHECK ----------
    print("\n--- THE EIGENBASIS CHECK (registered; NQ has never been varied) ---")
    ref = psi700
    print("%6s %14s %14s %14s" % ("NQ", "max|dPsi|", "Psi(0)", "Psi(umax)"))
    print("%6d %14s %14.9f %14.9f" % (700, "(reference)", ref[0], ref[-1]))
    spreads = {}
    for NQ in (600, 800, 900):
        p, s = psi_at(NQ, ug)
        d = float(np.abs(p - ref).max())
        spreads[NQ] = d
        print("%6d %14.3e %14.9f %14.9f" % (NQ, d, p[0], p[-1]))
    worst_basis = max(spreads.values())
    print("\n  ### WORST |Psi(NQ) - Psi(700)| ACROSS THE VARIED BASES = %.3e" % worst_basis)
    print("  (b117's measured refinement floor, for comparison: 2.774e-05)")

    # what it does to the verdicts
    print("\n  Effect on the verdict quantities (I(L) at the nine cells):")
    print("%6s %16s %16s %12s" % ("a^2", "I(L) @NQ=700", "worst |dI| over NQ", "b119 margin"))
    B119_MARGIN = {2: 0.064826976, 3: 0.095154244, 4: 0.111534989, 8: 0.133564668,
                   9: 0.135216620, 12: 0.137327894, 16: 0.137215854,
                   24: 0.134217931, 48: 0.123962521}
    psis = {NQ: psi_at(NQ, ug)[0] for NQ in (600, 800, 900)}
    worst_dI = 0.0
    for a2 in CELLS:
        L = math.log(math.sqrt(a2))
        base = I_of_L(L, sg, Phi, ug, ref)
        dmax = max(abs(I_of_L(L, sg, Phi, ug, psis[NQ]) - base) for NQ in psis)
        worst_dI = max(worst_dI, dmax)
        print("%6d %16.9f %16.3e %12.6f" % (a2, base, dmax, B119_MARGIN[a2]))
    print("\n  ### WORST |dI| FROM EIGENBASIS VARIATION = %.3e" % worst_dI)
    print("  smallest b119 coarse margin = %.6f" % min(B119_MARGIN.values()))
    print("  ratio (basis wobble / smallest margin) = %.3e"
          % (worst_dI / min(B119_MARGIN.values())))

    # ---------- P2: THE CONTINUUM STEP ----------
    print("\n--- P2: THE CONTINUUM STEP (a Lipschitz modulus for I(L) in L) ---")
    print("  dI/dL = int_0^2 PhiK(s) * s * Psi'(L s) ds, so")
    print("  |dI/dL| <= (max_s |s PhiK(s)|) * int_0^2 |Psi'| ... bounded below by the")
    print("  data-driven modulus computed directly:")
    Ls = np.linspace(math.log(math.sqrt(2)), math.log(math.sqrt(48.001)), 601)
    Ivals = np.array([I_of_L(L, sg, Phi, ug, ref) for L in Ls])
    dI = np.gradient(Ivals, Ls)
    Lip = float(np.abs(dI).max())
    mesh60 = (Ls[-1] - Ls[0]) / 59.0
    print("  measured max |dI/dL| over 601 points  = %.6f" % Lip)
    print("  b119's sweep mesh (60 points)          = %.6f" % mesh60)
    print("  Lipschitz x half-mesh                  = %.6f" % (Lip * mesh60 / 2))
    print("  worst-case I(L) between b119's samples = %.6f"
          % (max(Ivals) + Lip * mesh60 / 2))
    print("  (max I over the fine sweep = %.6f, so the interpolated worst case)" % max(Ivals))
    print("  stays strictly negative: %s" % (max(Ivals) + Lip * mesh60 / 2 < 0))
    print("\n  AND ON THE FINE SWEEP ITSELF (601 points, mesh %.6f):" % ((Ls[-1]-Ls[0])/600))
    fine_mesh = (Ls[-1] - Ls[0]) / 600.0
    print("  Lipschitz x half-mesh = %.3e ; max I = %.6f ; worst case = %.6f"
          % (Lip * fine_mesh / 2, max(Ivals), max(Ivals) + Lip * fine_mesh / 2))
    print("  strictly negative across the continuum (modulo the modulus's own grade): %s"
          % (max(Ivals) + Lip * fine_mesh / 2 < 0))


main()
