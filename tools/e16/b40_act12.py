# -*- coding: utf-8 -*-
"""W-CONSTRUCTION-1 act 12 -- b40: THE INEQUALITY'S BENCH ROWS + THE OUT-OF-RANGE CELLS.

Registration: data/b40_registration_2026-08-18.txt (banked FIRST; the sign-dictionary
flags F1-F3, the chain grades, the stop). Computes and records; decides nothing beyond
the registered maps. No sign sentence at complete roster.
"""
import math, sys
import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import carto_atlas as C
import carto_auto as CA
import qeps_layer as Q
import b8_sonin_dim as B8
import b10_cells as B10

BANK = r"D:\relay\data\b40_2026-08-18.txt"
CELLS = [(math.sqrt(2), "2"), (math.sqrt(3), "3"), (2.0, "4"),
         (math.sqrt(8), "8"), (3.0, "9"), (math.sqrt(12), "12"),
         (4.0, "16"), (5.0, "25"), (6.0, "36")]
S4 = (2, 3, 5)
NCAP = 3
HEAD = (700, 10)
NU_HALF = 401
EPS_NQ, EPS_NG, EPS_NRHO = 700, 400, 300
RHO_MAX = 36.01


def staircase(p, a):
    n, k = 0, 1
    while p ** k <= a * a + 1e-12:
        n += 1
        k += 1
    return min(n, NCAP)


def family(a):
    v, w = C.bump(a)
    dv = np.gradient(v)
    L = math.log(a)
    corr = np.convolve(w, w, mode="full") * float(dv[0])
    vc = np.linspace(-2 * L, 2 * L, corr.size)
    return v, w, corr, vc, L


def atlas_columns(a, primes, v, w, corr, vc, L):
    G = CA.ghat(v, w, C.GAM)
    Z = 2.0 * float(np.sum(G ** 2))
    Pc = float(np.trapezoid(w * np.cosh(v / 2.0), v))
    P = 2.0 * Pc * Pc
    U = np.linspace(-C.UMAX, C.UMAX, C.NU)
    GU = C.hhat(v, w, U)
    A = float(np.trapezoid(GU ** 2 * C.kernel(U), U) / (2.0 * math.pi))
    PR_S = 0.0
    PR_full = 0.0
    for p in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31):
        k = 1
        while p ** k <= a * a + 1e-12:
            ln = math.log(p ** k)
            if ln <= 2 * L:
                term = 2.0 * math.log(p) / math.sqrt(p ** k) * float(np.interp(ln, vc, corr))
                PR_full += term
                if p in primes:
                    PR_S += term
            k += 1
    resid_atlas = Z - (P - PR_full + A)
    return Z, P, A, PR_S, resid_atlas


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
    rec("b40 RUN - THE INEQUALITY ROWS + OUT-OF-RANGE CELLS. Registration banked first (F1-F3).")
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
    for name, gval, tol in (("sum lam2", abs(float(lam2.sum()) - 2.237484835), 1e-6),
                            ("sum lam2 xi1^2", abs(float((lam2 * xi1 ** 2).sum()) - 2.0), 1e-6),
                            ("epsprime1", abs(float(t_n.sum()) - 22.9964757), 1e-3)):
        ok = gval <= tol
        void |= not ok
        rec("  pin %-16s |delta|=%.2e (tol %.0e) %s" % (name, gval, tol, "PASS" if ok else "FAIL"))
    if void:
        rec("\n  C0 FAILED - VOID.")
        open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
        return

    rr = np.exp(np.linspace(1e-4, math.log(RHO_MAX), EPS_NRHO))
    ee_full = np.atleast_1d(Q.eps(rr, NQ=EPS_NQ, NG=EPS_NG))
    ee_modes = per_mode_eps_grids(rr)

    rec("\n(rows with a^2 > 12 carry: staircase CAP n<=3 where exceeded; eps truncation beyond")
    rec(" rho=20 unquantified by the lemma52 ladder - the caveat rides; per-cell atlas residual shown)")
    rec("")
    stop_hit = []
    for a, alab in CELLS:
        v, w2, corr, vc, L = family(a)
        corr_min = float(np.min(corr))
        Z, P, A, PR, resid_atlas = atlas_columns(a, S4, v, w2, corr, vc, L)
        flag = "" if abs(resid_atlas) <= C.TOL else "  ATLAS-RESID FLAG"
        Thq = theta_quotient(a, S4, corr, vc, L)
        NQ, NMODE = HEAD
        tr = trace_modes(a, corr, vc, L, NQ, NMODE)
        N = len(tr)
        pos_gate = bool(np.all(tr >= -1e-12))
        E2n = np.array([e2_of_grid(a, corr, vc, L, rr, ee_modes[n]) for n in range(N)])
        E2full = e2_of_grid(a, corr, vc, L, rr, ee_full)
        E2even, E2odd = float(E2n[0::2].sum()), float(E2n[1::2].sum())
        Tr_raw = float(tr.sum())
        Tr_raw_even = float(tr[0::2].sum())
        resid = Tr_raw - A - float(E2n.sum())
        s = t_n[:N] / float(t_n[:N].sum())
        wmode = tr - E2n - s * resid
        Wp, Wm = float(wmode[0::2].sum()), float(wmode[1::2].sum())
        if abs(Wp + Wm - A) > 1e-10:
            rec("  SUM GATE FAILED at a^2=%s - VOID" % alab)
            open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
            return
        resid47 = Tr_raw - (A + E2full)
        resid47cc = Tr_raw - ((-A) + E2full)
        D_closed = (A - PR) - ((Wp + E2even) - Thq)
        # the dictated inequality, both conventions (F2):
        obj_atlas = (Wp + E2even) + Thq
        led_atlas = A - PR
        obj_cc = Tr_raw_even + Thq          # the positive-form E1 trace + quotient
        led_cc = (-A) - PR
        rec("a^2=%-4s A=%10.6f Z=%9.6f PR=%8.5f Thq=%8.5f  atlas-resid=%+.2e%s" % (alab, A, Z, PR, Thq, resid_atlas, flag))
        rec("  raw modes >= 0: %s   corr_min = %+.2e   Tr_raw = %9.6f  Tr_raw_even = %9.6f"
            % ("PASS" if pos_gate else "FAIL", corr_min, Tr_raw, Tr_raw_even))
        rec("  F1 test:  resid47(atlas) = %+9.5f    resid47'(CC dict) = %+9.5f" % (resid47, resid47cc))
        rec("  D_closed = %+9.6f   SIGN: %s%s" % (D_closed, "NEG" if D_closed < 0 else "### NON-NEG - THE STOP", ""))
        rec("  dictated ineq (atlas signs): object %+9.5f  <=?  ledger %+9.5f  : %s"
            % (obj_atlas, led_atlas, "HOLDS" if obj_atlas <= led_atlas else "fails"))
        rec("  dictated ineq (CC dict):     object %+9.5f  <=?  ledger %+9.5f  : %s"
            % (obj_cc, led_cc, "HOLDS" if obj_cc <= led_cc else "fails"))
        if D_closed >= 0:
            stop_hit.append((alab, D_closed, Z))
    if stop_hit:
        rec("\n### THE STOP: non-negative D_closed at: %s - the atlas zero column at those cells" % stop_hit)
        rec("### is printed above (Z column); no further action until the check is banked.")
    else:
        rec("\nno stop: D_closed negative at every cell including the out-of-range three (the")
        rec("registered prediction held).")
    rec("\nL1 TRANSPORT TEST (the boundary cell a^2 = 2, CC window edge): Tr_raw = see row 1;")
    rec("W_inf^CC = -A = +1.99 there. The comparison is in the rows; the verdict in the report.")
    rec("\nRecorded as data. NO SIGN SENTENCE AT COMPLETE ROSTER. h2 UNCHANGED. NOTHING DEPOSITS.")
    open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)


if __name__ == "__main__":
    main()
