# -*- coding: utf-8 -*-
"""W-CONSTRUCTION-1 act 9 -- b37: THE ACT-8 RE-RUN UNDER THE REGULARIZED TRACE.

Registration: data/b37_registration_2026-08-18.txt (banked FIRST). The archimedean
trace is substituted at content (CC Thm 4.7, banked statement); Delta_- is the series
object (odd-index mask). Two bracket readings, both registered. Computes and records;
decides nothing. No sign sentence at complete roster.
"""
import math, sys
import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import carto_atlas as C
import carto_auto as CA
import qeps_layer as Q
import b8_sonin_dim as B8
import b10_cells as B10

BANK = r"D:\relay\data\b37_2026-08-18.txt"
CELLS = [(math.sqrt(2), "2"), (math.sqrt(3), "3"), (2.0, "4"),
         (math.sqrt(8), "8"), (3.0, "9"), (math.sqrt(12), "12")]
S3, S4 = (2, 3), (2, 3, 5)
NU_HALF = 401
EPS_NQ, EPS_NG, EPS_NRHO = 700, 400, 240


def staircase(p, a):
    n, k = 0, 1
    while p ** k <= a * a + 1e-12:
        n += 1
        k += 1
    return n


def family(a):
    v, w = C.bump(a)
    dv = np.gradient(v)
    L = math.log(a)
    corr = np.convolve(w, w, mode="full") * float(dv[0])
    vc = np.linspace(-2 * L, 2 * L, corr.size)
    return v, w, corr, vc, L


def left_side(a, primes, v, w, corr, vc, L):
    U = np.linspace(-C.UMAX, C.UMAX, C.NU)
    GU = C.hhat(v, w, U)
    A = float(np.trapezoid(GU ** 2 * C.kernel(U), U) / (2.0 * math.pi))
    PR = 0.0
    for p in primes:
        k = 1
        while p ** k <= a * a + 1e-12:
            ln = math.log(p ** k)
            if ln <= 2 * L:
                PR += 2.0 * math.log(p) / math.sqrt(p ** k) * float(np.interp(ln, vc, corr))
            k += 1
    return A, PR


def eps_masked(rho_arr, mask):
    """eps(rho) with the CC-index mask (True = keep mode n). Mirrors Q.eps exactly."""
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(EPS_NQ)
    sel = np.asarray(mask, dtype=bool)
    out = np.empty(len(rho_arr))
    gx, gw = np.polynomial.legendre.leggauss(EPS_NG)
    for k, r in enumerate(rho_arr):
        lo, hi = 1.0 / r, 1.0
        if hi - lo <= 0:
            out[k] = 0.0
            continue
        u = 0.5 * (hi - lo) * gx + 0.5 * (hi + lo)
        jac = 0.5 * (hi - lo)
        I = ((an(u) * an(r * u)) * (gw[:, None] * jac)).sum(0)
        term = lam2 / (1 - lam2) * (r ** -0.5) * I
        out[k] = float(term[sel].sum())
    return out


def e2_from_grid(a, corr, vc, L, rr, ee):
    uu = np.linspace(0.0, 2 * L, NU_HALF)
    cu = np.interp(uu, vc, corr)
    eu = np.interp(np.exp(uu), rr, ee)
    return 2.0 * float(np.trapezoid(cu * eu, uu))


def theta_quotient(a, primes, corr, vc, L):
    total = 0.0
    for p in primes:
        n = staircase(p, a)
        if n < 1:
            continue
        N, K, d = B10.quotient_basis(p, n)
        U = B8.scaling_matrix(p, n)
        S = K @ K.T
        Uk = np.eye(N)
        for k in range(1, 2 * n):
            Uk = U @ Uk
            tq = abs(complex(np.trace(Uk @ S))) / d
            ln = k * math.log(p)
            if ln <= 2 * L:
                total += math.log(p) * tq * 2.0 * float(np.interp(ln, vc, corr))
    return total


def main():
    out = []
    def rec(s):
        print(s)
        out.append(s)

    rec("=" * 100)
    rec("b37 RUN - THE RE-RUN UNDER THE REGULARIZED TRACE. Registration banked first.")
    rec("=" * 100)

    rec("\n--- C0: VOID GATES ---")
    void = False
    for a in (1.30, 3.50):
        r = CA.channels_auto(a)
        ok = abs(r["residual"]) <= C.TOL
        void |= not ok
        rec("  carto far-end a=%.2f residual=%+.3e %s" % (a, r["residual"], "PASS" if ok else "FAIL"))
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(EPS_NQ)
    NT = len(lam2)
    even_mask = np.array([n % 2 == 0 for n in range(NT)])
    odd_mask = ~even_mask
    t_n = lam2 / (1 - lam2) * xi1 ** 2
    ep_full = float(t_n.sum())
    ep_even = float(t_n[even_mask].sum())
    ep_odd = float(t_n[odd_mask].sum())
    gates = [("sum lam2", abs(float(lam2.sum()) - 2.237484835), 1e-6),
             ("sum lam2 xi1^2", abs(float((lam2 * xi1 ** 2).sum()) - 2.0), 1e-6),
             ("epsprime1", abs(ep_full - 22.9964757), 1e-3),
             ("epsprime1_even (b35 pin)", abs(ep_even - 14.177305), 1e-3),
             ("epsprime1_odd  (b35 pin)", abs(ep_odd - 8.819138), 1e-3)]
    for name, gval, tol in gates:
        ok = gval <= tol
        void |= not ok
        rec("  pin %-26s |delta|=%.2e (tol %.0e) %s" % (name, gval, tol, "PASS" if ok else "FAIL"))
    if void:
        rec("\n  C0 FAILED - THE RUN IS VOID. No table follows.")
        open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
        return

    rec("\n--- eps grids (full / even / odd; fixed 240 pts on (1,12]) ---")
    rr = np.exp(np.linspace(1e-4, math.log(12.001), EPS_NRHO))
    ee_full = np.atleast_1d(Q.eps(rr, NQ=EPS_NQ, NG=EPS_NG))
    ee_even = eps_masked(rr, even_mask)
    ee_odd = eps_masked(rr, odd_mask)
    mask_err = float(np.max(np.abs(ee_even + ee_odd - ee_full)))
    rec("  mask algebra: max|eps_even + eps_odd - eps_full| = %.2e  %s"
        % (mask_err, "PASS" if mask_err <= 1e-12 else "FAIL"))
    if mask_err > 1e-12:
        rec("  MASK GATE FAILED - VOID.")
        open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
        return

    for Sname, primes in (("S3={inf,2,3}", S3), ("S4={inf,2,3,5}", S4)):
        rec("\n" + "=" * 100)
        rec("PLACE SET %s" % Sname)
        rec("=" * 100)
        rec("%-6s %10s %10s | %10s %10s %10s %10s | %12s %12s"
            % ("a^2", "A", "PR", "E2", "E2even", "E2odd", "Thq", "D_dictated", "D_sector"))
        for a, alab in CELLS:
            v, w2, corr, vc, L = family(a)
            A, PR = left_side(a, primes, v, w2, corr, vc, L)
            E2 = e2_from_grid(a, corr, vc, L, rr, ee_full)
            E2e = e2_from_grid(a, corr, vc, L, rr, ee_even)
            E2o = e2_from_grid(a, corr, vc, L, rr, ee_odd)
            Thq = theta_quotient(a, primes, corr, vc, L)
            D_dict = (Thq - PR) + (E2o - 2.0 * E2)
            D_sect = (Thq - PR) - E2e
            rec("%-6s %10.6f %10.6f | %10.6f %10.6f %10.6f %10.6f | %12.6f %12.6f"
                % (alab, A, PR, E2, E2e, E2o, Thq, D_dict, D_sect))
            rec("        components: (Thq - PR) = %+.6f   -E2even = %+.6f   (E2odd - 2 E2) = %+.6f"
                % (Thq - PR, -E2e, E2o - 2 * E2))
            rec("        resid47: 0 by construction (substitution at content)")
    rec("\nRecorded as data. Verdict per the registered map is written in the act report.")
    rec("NO SIGN SENTENCE AT COMPLETE ROSTER. h2 UNCHANGED. NOTHING DEPOSITS.")
    open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)


if __name__ == "__main__":
    main()
