# -*- coding: utf-8 -*-
"""b113 -- THE EXTENSION INSTRUMENT ACT.

The author's two rulings executed: the epsilon layer rebuilt on a wider rho
domain, the six banked cells reproduced FIRST (the gate), then the author's
refinement cells (a^2 = 10, 11) and extension cells (a^2 = 16, 24, 48).

THE REBUILD, per the registration: qeps_layer.eps(rho) has no domain
restriction -- it integrates on [1/rho, 1] at any rho > 1. b38's ceiling was
only its SAMPLING GRID (240 points to rho = 12.001, consumed by np.interp,
which clamps silently past the end). So the rebuild widens the grid to cover
rho_max = 48 at no lower log-density than the original (~0.010399 per step;
400 points to log(48) is finer), with a 600-point convergence variant.

Everything else is b38's own machinery, imported. b38's verdicts are fenced;
this script computes and records, and decides nothing.
Registration: data/b113_registration_2026-08-22.txt.
"""
import math, sys
import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38
import qeps_layer as Q

S4 = B38.S4
NQ, NMODE = B38.TRIPLE[1]           # the headline triple middle, as banked
EPS_NQ, EPS_NG = B38.EPS_NQ, B38.EPS_NG

RHO_MAX = 48.001                    # covers the author's largest cell
N_RHO_MAIN = 400                    # log-density finer than the original
N_RHO_CONV = 600                    # convergence variant

BANKED = [(math.sqrt(2), "2", 0.6923), (math.sqrt(3), "3", 0.6638),
          (2.0, "4", 0.6533), (math.sqrt(8), "8", 0.6260),
          (3.0, "9", 0.6204), (math.sqrt(12), "12", 0.6092)]
REFINE = [(math.sqrt(10), "10"), (math.sqrt(11), "11")]
EXTEND = [(4.0, "16"), (math.sqrt(24), "24"), (math.sqrt(48), "48")]

GATE_F_TOL = 1e-4                   # registered before computing
GATE_SUM_TOL = 1e-10                # b38's own


def build_grid(n_rho):
    rr = np.exp(np.linspace(1e-4, math.log(RHO_MAX), n_rho))
    ee_modes = B38.per_mode_eps_grids(rr)
    ee_full = np.atleast_1d(Q.eps(rr, NQ=EPS_NQ, NG=EPS_NG))
    return rr, ee_modes, ee_full


def cell(a, rr, ee_modes, t_n):
    v, w2, corr, vc, L = B38.family(a)
    A, P, PR = B38.left_side(a, S4, v, w2, corr, vc, L)
    tr = B38.trace_modes(a, corr, vc, L, NQ, NMODE)
    N = len(tr)
    E2n = np.array([B38.e2_of_grid(a, corr, vc, L, rr, ee_modes[n]) for n in range(N)])
    E2N = float(E2n.sum())
    TrN = float(tr.sum())
    resid = TrN - A - E2N
    s = t_n[:N] / float(t_n[:N].sum())
    wmode = tr - E2n - s * resid
    Wp, Wm = float(wmode[0::2].sum()), float(wmode[1::2].sum())
    sigma_even = float(s[0::2].sum())
    lhs = Wp - sigma_even * A
    rhs = (float(tr[0::2].sum()) - sigma_even * TrN) - (float(E2n[0::2].sum()) - sigma_even * E2N)
    return dict(A=A, Wp=Wp, Wm=Wm, f=Wp / A, sigma=sigma_even,
                sum_gate=abs(Wp + Wm - A), red_lhs=lhs, red_rhs=rhs,
                red_res=abs(lhs - rhs))


def main():
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(EPS_NQ)
    t_n = lam2 / (1 - lam2) * xi1 ** 2

    print("=" * 78)
    print("b113 -- THE EXTENSION INSTRUMENT ACT")
    print("REBUILT DOMAIN: rho in (1, %.3f], %d log-spaced points" % (RHO_MAX, N_RHO_MAIN))
    print("  original: (1, 12.001], 240 points; log-step %.6f" % ((math.log(12.001) - 1e-4) / 239))
    print("  rebuilt : log-step %.6f  (FINER, never coarser)"
          % ((math.log(RHO_MAX) - 1e-4) / (N_RHO_MAIN - 1)))
    print("=" * 78)

    rr, ee_modes, ee_full = build_grid(N_RHO_MAIN)
    mask = float(np.max(np.abs(ee_modes.sum(0) - ee_full)))
    print("\n--- REBUILD GATES ---")
    print("  per-mode mask algebra on the rebuilt grid: max|sum_n eps_n - eps_full| = %.2e  %s"
          % (mask, "PASS" if mask <= 1e-10 else "FAIL"))
    if mask > 1e-10:
        print("  MASK GATE FAILED -- HALT."); return

    print("\n--- THE REBUILD GATE: the six banked cells reproduced FIRST ---")
    print("%-5s %10s %10s %11s %11s %s" % ("a^2", "f_rebuilt", "f_banked", "|delta|", "sum_gate", "verdict"))
    worst_f, worst_sum, gate_ok = 0.0, 0.0, True
    for a, lab, fb in BANKED:
        r = cell(a, rr, ee_modes, t_n)
        d = abs(r["f"] - fb)
        worst_f = max(worst_f, d); worst_sum = max(worst_sum, r["sum_gate"])
        ok = (d <= GATE_F_TOL) and (r["sum_gate"] <= GATE_SUM_TOL)
        gate_ok &= ok
        print("%-5s %10.6f %10.4f %11.2e %11.2e %s" % (lab, r["f"], fb, d, r["sum_gate"],
                                                       "PASS" if ok else "FAIL"))
    print("  worst |delta f| = %.2e (tol %.0e); worst sum gate = %.2e (tol %.0e)"
          % (worst_f, GATE_F_TOL, worst_sum, GATE_SUM_TOL))
    if not gate_ok:
        print("\n  *** REBUILD GATE FAILED -- ACT HALTS. No new cell is computed. ***")
        return
    print("  *** REBUILD GATE PASSES. New cells may run. ***")

    sigma = None
    print("\n--- THE NEW CELLS (author's: refinement 10, 11; extension 16, 24, 48) ---")
    print("%-5s %11s %11s %12s %11s %11s" % ("a^2", "A", "f_cell", "f - sigma", "sum_gate", "red_resid"))
    results = []
    for a, lab in REFINE + EXTEND:
        r = cell(a, rr, ee_modes, t_n)
        sigma = r["sigma"]
        dev = r["f"] - r["sigma"]
        results.append((lab, r["f"], dev, r["red_res"]))
        print("%-5s %11.6f %11.6f %+12.6f %11.2e %11.2e"
              % (lab, r["A"], r["f"], dev, r["sum_gate"], r["red_res"]))

    print("\n  sigma_even (rebuilt grid) = %.9f" % sigma)

    print("\n--- CONVERGENCE VARIANT (N_RHO = %d) at the three extension cells ---" % N_RHO_CONV)
    rr2, ee2, _ = build_grid(N_RHO_CONV)
    for a, lab in EXTEND:
        r2 = cell(a, rr2, ee2, t_n)
        base = dict((l, f) for l, f, _, _ in results)[lab]
        print("  a^2=%-3s f=%.6f   |f(400) - f(600)| = %.2e" % (lab, r2["f"], abs(base - r2["f"])))

    print("\n--- THE FULL DEVIATION SERIES (banked + new), for the branch read ---")
    banked_dev = [("2", 0.075845), ("3", 0.047312), ("4", 0.036824),
                  ("8", 0.009496), ("9", 0.003946), ("12", -0.007261)]
    allser = banked_dev + [(l, d) for l, _, d, _ in results]
    allser.sort(key=lambda p: float(p[0]))
    for lab, d in allser:
        print("  a^2=%-3s  f - sigma = %+0.6f" % (lab, d))
    devs = [d for _, d in allser]
    print("\n  strictly decreasing across all cells:",
          all(devs[i] > devs[i + 1] for i in range(len(devs) - 1)))
    print("  sign changes:", sum(1 for i in range(len(devs) - 1) if devs[i] * devs[i + 1] < 0))


main()
