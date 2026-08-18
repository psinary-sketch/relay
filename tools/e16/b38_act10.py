# -*- coding: utf-8 -*-
"""W-CONSTRUCTION-1 act 10 -- b38: THE APPORTIONMENT JOINT.

Registration: data/b38_registration_2026-08-18.txt (banked FIRST; the apportionment
DEFINITION and its warrant fixed there). Computes and records; decides nothing.
No sign sentence at complete roster.
"""
import math, sys
import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import carto_atlas as C
import carto_auto as CA
import qeps_layer as Q
import b8_sonin_dim as B8
import b10_cells as B10

BANK = r"D:\relay\data\b38_2026-08-18.txt"
CELLS = [(math.sqrt(2), "2"), (math.sqrt(3), "3"), (2.0, "4"),
         (math.sqrt(8), "8"), (3.0, "9"), (math.sqrt(12), "12")]
S4 = (2, 3, 5)
TRIPLE = [(500, 8), (700, 10), (900, 11)]
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
    Pc = float(np.trapezoid(w * np.cosh(v / 2.0), v))
    P = 2.0 * Pc * Pc
    PR = 0.0
    for p in primes:
        k = 1
        while p ** k <= a * a + 1e-12:
            ln = math.log(p ** k)
            if ln <= 2 * L:
                PR += 2.0 * math.log(p) / math.sqrt(p ** k) * float(np.interp(ln, vc, corr))
            k += 1
    return A, P, PR


def trace_modes(a, corr, vc, L, NQ, NMODE):
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(NQ)
    NMODE = min(NMODE, xi.shape[1])
    uu = np.linspace(0.0, 2 * L, NU_HALF)
    cu = np.interp(uu, vc, corr)
    tr = np.zeros(NMODE)
    for n in range(NMODE):
        f = xi[:, n]
        An = np.empty(len(uu))
        for i, u in enumerate(uu):
            lamd = math.exp(u)
            fy = np.interp(lamd * x, x, f, left=0.0, right=0.0)
            An[i] = math.sqrt(lamd) * 0.5 * float((w * f * fy).sum())
        tr[n] = 2.0 * float(np.trapezoid(cu * An, uu))
    return tr


def per_mode_eps_grids(rr):
    """eps_n(rho) grids, one per mode (the single-mode masks; mode-diagonal, exact)."""
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(EPS_NQ)
    NT = len(lam2)
    gx, gw = np.polynomial.legendre.leggauss(EPS_NG)
    out = np.zeros((NT, len(rr)))
    for k, r in enumerate(rr):
        lo, hi = 1.0 / r, 1.0
        if hi - lo <= 0:
            continue
        u = 0.5 * (hi - lo) * gx + 0.5 * (hi + lo)
        jac = 0.5 * (hi - lo)
        I = ((an(u) * an(r * u)) * (gw[:, None] * jac)).sum(0)
        out[:, k] = lam2 / (1 - lam2) * (r ** -0.5) * I
    return out


def e2_of_grid(a, corr, vc, L, rr, ee):
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
    rec("b38 RUN - THE APPORTIONMENT JOINT. Registration banked first; definition + warrant fixed there.")
    rec("=" * 100)

    rec("\n--- C0: VOID GATES ---")
    void = False
    for a in (1.30, 3.50):
        r = CA.channels_auto(a)
        ok = abs(r["residual"]) <= C.TOL
        void |= not ok
        rec("  carto far-end a=%.2f residual=%+.3e %s" % (a, r["residual"], "PASS" if ok else "FAIL"))
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(EPS_NQ)
    t_n = lam2 / (1 - lam2) * xi1 ** 2
    gates = [("sum lam2", abs(float(lam2.sum()) - 2.237484835), 1e-6),
             ("sum lam2 xi1^2", abs(float((lam2 * xi1 ** 2).sum()) - 2.0), 1e-6),
             ("epsprime1", abs(float(t_n.sum()) - 22.9964757), 1e-3)]
    for name, gval, tol in gates:
        ok = gval <= tol
        void |= not ok
        rec("  pin %-16s |delta|=%.2e (tol %.0e) %s" % (name, gval, tol, "PASS" if ok else "FAIL"))
    if void:
        rec("\n  C0 FAILED - VOID.")
        open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
        return

    rr = np.exp(np.linspace(1e-4, math.log(12.001), EPS_NRHO))
    ee_full = np.atleast_1d(Q.eps(rr, NQ=EPS_NQ, NG=EPS_NG))
    ee_modes = per_mode_eps_grids(rr)
    mode_alg = float(np.max(np.abs(ee_modes.sum(0) - ee_full)))
    rec("\n  per-mode mask algebra: max|sum_n eps_n - eps_full| = %.2e  %s"
        % (mode_alg, "PASS" if mode_alg <= 1e-10 else "FAIL"))
    if mode_alg > 1e-10:
        rec("  MASK GATE FAILED - VOID.")
        open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
        return

    rec("\n" + "=" * 100)
    rec("ITEMS 1 + 3 (place set {inf,2,3,5}; headline triple middle; spreads over the triple)")
    rec("=" * 100)
    rec("%-6s %10s %10s %10s | %9s %9s %8s %8s | %12s %12s %9s"
        % ("a^2", "A", "P(pole)", "PR", "W_plus", "W_minus", "f_cell", "resid47", "D_dictated", "D_closed", "spread"))
    for a, alab in CELLS:
        v, w2, corr, vc, L = family(a)
        A, P, PR = left_side(a, S4, v, w2, corr, vc, L)
        Thq = theta_quotient(a, S4, corr, vc, L)
        Dcs, det = [], None
        for (NQ, NMODE) in TRIPLE:
            tr = trace_modes(a, corr, vc, L, NQ, NMODE)
            N = len(tr)
            E2n = np.array([e2_of_grid(a, corr, vc, L, rr, ee_modes[n]) for n in range(N)])
            E2N = float(E2n.sum())
            E2full = e2_of_grid(a, corr, vc, L, rr, ee_full)
            E2even = float(E2n[0::2].sum())
            E2odd = float(E2n[1::2].sum())
            TrN = float(tr.sum())
            resid = TrN - A - E2N
            s = t_n[:N] / float(t_n[:N].sum())
            wmode = tr - E2n - s * resid
            Wp = float(wmode[0::2].sum())
            Wm = float(wmode[1::2].sum())
            sum_gate = abs(Wp + Wm - A)
            D_dict = (Thq - PR) + (E2odd - 2.0 * E2full)
            D_closed = (A - PR) - ((Wp + E2even) - Thq)
            D_closed_alt = Wm - E2even + (Thq - PR)
            Dcs.append(D_closed)
            if (NQ, NMODE) == TRIPLE[1]:
                det = (Wp, Wm, resid, D_dict, D_closed, D_closed_alt, sum_gate, E2even, E2odd)
        Wp, Wm, resid, D_dict, D_closed, D_closed_alt, sum_gate, E2even, E2odd = det
        spread = max(abs(d - Dcs[1]) for d in Dcs)
        if sum_gate > 1e-10:
            rec("  SUM GATE FAILED at a^2=%s: |W+ + W- - A| = %.2e - VOID" % (alab, sum_gate))
            open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
            return
        rec("%-6s %10.6f %10.6f %10.6f | %9.5f %9.5f %8.4f %8.4f | %12.6f %12.6f %9.5f"
            % (alab, A, P, PR, Wp, Wm, Wp / A, resid, D_dict, D_closed, spread))
        rec("        exact-algebra check: D_closed - [W_minus - E2even + (Thq-PR)] = %+.2e   sum gate |W+ + W- - A| = %.1e"
            % (D_closed - D_closed_alt, sum_gate))
        rec("        components: W_minus = %+.5f   -E2even = %+.5f   (Thq - PR) = %+.5f"
            % (Wm, -E2even, theta_quotient(a, S4, corr, vc, L) - PR))
    rec("\nITEM 2 - the pole column beside the banked W_pole = -2.000127 (the reconciliation's")
    rec("family; different families, exact equality NOT expected, consistency of sign/magnitude")
    rec("recorded): the P column above runs ~2.0 per cell; the atlas arrangement holds P")
    rec("SEPARATE from A (residual 1e-13) - the atlas's W_inf is pole-free by its own")
    rec("bookkeeping; the pole functional acts through ball directions (Tate; act-4 (beta)")
    rec("PROVED) and ball is orthogonal to Son (vanilla, no axioms): (P-ball) closes")
    rec("STRUCTURALLY; the verdict sentence lives in the act report.")
    rec("\nRecorded as data. Verdicts per the registered map in the act report.")
    rec("NO SIGN SENTENCE AT COMPLETE ROSTER. h2 UNCHANGED. NOTHING DEPOSITS.")
    open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)


if __name__ == "__main__":
    main()
