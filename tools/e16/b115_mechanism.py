# -*- coding: utf-8 -*-
"""b115 -- THE MECHANISM ACT: the instrument check of a derivation already written.

THE CIRCULARITY GATE: this script checks the DERIVED factorization against
b38's own machinery. The b113 deviation pattern is not read, not imported and
not used anywhere in this file. The only recorded quantities consumed are
b38's own function definitions.

The derivation being checked (written longhand in the bank BEFORE this ran):

  b109:  N(a) := W+ - sigma_even * A
                = [sum_even tr_n - sigma_even*Tr_N] - [sum_even E2_n - sigma_even*E2_N]

  b38:   tr_n  = 2 * int_0^{2L} C_a(u) A_n(u) du       A_n takes no a
         E2_n  = 2 * int_0^{2L} C_a(u) e_n(u) du       e_n takes no a

  => (STEP 1, the collapse to one density)
         N(a)  = 2 * int_0^{2L} C_a(u) Psi(u) du
         Psi(u) := [sum_even A_n(u) - sigma_even*sum_n A_n(u)]
                 - [sum_even e_n(u) - sigma_even*sum_n e_n(u)]
         Psi TAKES NO a PARAMETER.

  carto_atlas.bump: w(v) = beta(v/L)/(L*c_beta), a PURE DILATION
  => C_a(u) = (w*w)(u) = K(u/L)/L with K FIXED, even, nonneg, int K = 1
  => (STEP 2, the scale-average form)
         N(L) = 2 * int_0^2 K(sigma) Psi(L*sigma) d sigma      [L = log a]

Checks run here: (1) Psi is a-independent as claimed; (2) STEP 1 reproduces
b38's N at every banked cell; (3) the dilation collapse of STEP 2 holds;
(4) the derived small-L limit N -> Psi(0) = N_even - sigma_even*N_modes;
(5) Psi's sign structure, reported at BENCH grade as evidence on the NAMED
OPEN STEP and never as its discharge.
"""
import math, sys
import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38
import qeps_layer as Q

S4 = B38.S4
NQ, NMODE = B38.TRIPLE[1]
EPS_NQ, EPS_NG = B38.EPS_NQ, B38.EPS_NG
NU_HALF = B38.NU_HALF

CELLS = [(math.sqrt(2), "2"), (math.sqrt(3), "3"), (2.0, "4"),
         (math.sqrt(8), "8"), (3.0, "9"), (math.sqrt(12), "12")]

RHO_MAX, N_RHO = 48.001, 400


def A_modes(uu):
    """A_n(u) on the u grid -- b38's trace_modes integrand, extracted verbatim."""
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(NQ)
    nm = min(NMODE, xi.shape[1])
    out = np.zeros((nm, len(uu)))
    for n in range(nm):
        f = xi[:, n]
        for i, u in enumerate(uu):
            lamd = math.exp(u)
            fy = np.interp(lamd * x, x, f, left=0.0, right=0.0)
            out[n, i] = math.sqrt(lamd) * 0.5 * float((w * f * fy).sum())
    return out


def e_modes(uu):
    """e_n(u) = eps_n(e^u) -- b38's e2_of_grid integrand, extracted verbatim."""
    rr = np.exp(np.linspace(1e-4, math.log(RHO_MAX), N_RHO))
    ee = B38.per_mode_eps_grids(rr)
    nm = min(NMODE, ee.shape[0])
    out = np.zeros((nm, len(uu)))
    for n in range(nm):
        out[n] = np.interp(np.exp(uu), rr, ee[n])
    return out


def psi_density(uu, sigma_even):
    A = A_modes(uu)
    E = e_modes(uu)
    phiA = A[0::2].sum(0) - sigma_even * A.sum(0)
    phiE = E[0::2].sum(0) - sigma_even * E.sum(0)
    return phiA - phiE, phiA, phiE


def main():
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(EPS_NQ)
    t_n = lam2 / (1 - lam2) * xi1 ** 2
    s = t_n[:NMODE] / float(t_n[:NMODE].sum())
    sig = float(s[0::2].sum())
    n_even = len(range(0, NMODE, 2))

    print("=" * 78)
    print("b115 -- THE MECHANISM ACT: instrument check of the derived factorization")
    print("  NMODE = %d, N_even = %d, sigma_even = %.12f" % (NMODE, n_even, sig))
    print("=" * 78)

    # ---- CHECK 1: Psi is a-independent (built on a grid with no a in it) ----
    print("\n--- CHECK 1: Psi's construction takes no a parameter ---")
    print("  A_n and e_n are evaluated on a bare u grid; no cell enters. By construction.")

    # ---- CHECK 2: STEP 1 reproduces b38's N at every banked cell ----
    print("\n--- CHECK 2: STEP 1  N = 2*int_0^{2L} C_a(u) Psi(u) du  vs b38's own N ---")
    print("%-5s %14s %14s %11s" % ("a^2", "N_direct", "N_factorized", "|diff|"))
    rr = np.exp(np.linspace(1e-4, math.log(RHO_MAX), N_RHO))
    ee_modes = B38.per_mode_eps_grids(rr)
    worst = 0.0
    for a, lab in CELLS:
        v, w2, corr, vc, L = B38.family(a)
        A, P, PR = B38.left_side(a, S4, v, w2, corr, vc, L)
        tr = B38.trace_modes(a, corr, vc, L, NQ, NMODE)
        nm = len(tr)
        E2n = np.array([B38.e2_of_grid(a, corr, vc, L, rr, ee_modes[n]) for n in range(nm)])
        # b109's identity, right-hand side, computed from b38's own outputs:
        n_direct = (float(tr[0::2].sum()) - sig * float(tr.sum())) \
                   - (float(E2n[0::2].sum()) - sig * float(E2n.sum()))
        # STEP 1, the collapse to one density:
        uu = np.linspace(0.0, 2 * L, NU_HALF)
        cu = np.interp(uu, vc, corr)
        psi, _, _ = psi_density(uu, sig)
        n_fact = 2.0 * float(np.trapezoid(cu * psi, uu))
        d = abs(n_direct - n_fact)
        worst = max(worst, d)
        print("%-5s %14.9f %14.9f %11.2e" % (lab, n_direct, n_fact, d))
    print("  worst |diff| = %.2e   %s" % (worst, "PASS" if worst < 1e-9 else "REVIEW"))

    # ---- CHECK 3: the dilation collapse  L*C_a(L*sigma) = K(sigma), a-free ----
    print("\n--- CHECK 3: the dilation collapse  K(sigma) = L*C_a(L*sigma) is a-free ---")
    sg = np.linspace(0.0, 2.0, 201)
    Ks = []
    for a, lab in CELLS:
        v, w2, corr, vc, L = B38.family(a)
        Ks.append(L * np.interp(L * sg, vc, corr))
    Ks = np.array(Ks)
    spread = float(np.abs(Ks - Ks.mean(0)).max())
    print("  max deviation of L*C_a(L*sigma) across the six cells: %.2e  %s"
          % (spread, "PASS (a-free)" if spread < 1e-6 else "REVIEW"))
    print("  K >= 0 everywhere:", bool((Ks.min() >= -1e-12)))
    print("  int_0^2 K d sigma = %.9f  (derivation says 1/2, K even with int_-2^2 K = 1)"
          % float(np.trapezoid(Ks.mean(0), sg)))

    # ---- CHECK 4: the derived small-L limit ----
    print("\n--- CHECK 4: the derived limit  N -> Psi(0) = N_even - sigma_even*NMODE ---")
    psi0, phiA0, phiE0 = psi_density(np.array([0.0]), sig)
    print("  Psi(0) computed          = %.12f" % float(psi0[0]))
    print("  N_even - sigma_even*NMODE = %.12f" % (n_even - sig * NMODE))
    print("  |diff| = %.2e" % abs(float(psi0[0]) - (n_even - sig * NMODE)))
    print("  e_n(0) = 0 exactly (empty integration range):  phi_e(0) = %.2e" % float(phiE0[0]))

    # ---- CHECK 5: Psi's sign structure -- BENCH evidence on the NAMED OPEN step ----
    print("\n--- CHECK 5: Psi's shape -- BENCH GRADE, evidence on the named open step,")
    print("                             NOT its discharge ---")
    umax = 2.0 * math.log(math.sqrt(48.001))
    ug = np.linspace(0.0, umax, 240)
    psi, phiA, phiE = psi_density(ug, sig)
    dpsi = np.gradient(psi, ug)
    sc = int(sum(1 for i in range(len(psi) - 1) if psi[i] * psi[i + 1] < 0))
    dsc = int(sum(1 for i in range(len(dpsi) - 2) if dpsi[i + 1] * dpsi[i + 2] < 0))
    print("  u range [0, %.4f] (covers the recorded family through a^2 = 48)" % umax)
    print("  Psi(0) = %+.6f   Psi(umax) = %+.6f" % (psi[0], psi[-1]))
    print("  Psi sign changes on the range: %d" % sc)
    print("  Psi' < 0 throughout:", bool((dpsi < 0).all()))
    print("  Psi' sign changes on the range: %d" % dsc)
    print("  min Psi = %+.6f at u = %.4f ; max Psi = %+.6f at u = %.4f"
          % (psi.min(), ug[int(psi.argmin())], psi.max(), ug[int(psi.argmax())]))
    for uq in (0.0, 0.25, 0.5, 1.0, 1.5, 2.0, 3.0, 3.87):
        if uq <= umax:
            j = int(np.abs(ug - uq).argmin())
            print("    u = %.2f   Psi = %+.6f   phi_A = %+.6f   phi_e = %+.6f"
                  % (ug[j], psi[j], phiA[j], phiE[j]))


main()
