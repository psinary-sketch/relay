# -*- coding: utf-8 -*-
"""W-CONSTRUCTION-1 act 11 -- b39: THE ZERO SIDE AGAINST THE MASSES; THE SECTOR SCAN.

Registration: data/b39_registration_2026-08-18.txt (banked FIRST). Computes and
records; decides nothing beyond the registered maps. No sign sentence at complete
roster.
"""
import math, sys
import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import carto_atlas as C
import carto_auto as CA
import qeps_layer as Q
import b8_sonin_dim as B8
import b10_cells as B10

BANK = r"D:\relay\data\b39_2026-08-18.txt"
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


def atlas_columns(a, primes, v, w, corr, vc, L):
    G = CA.ghat(v, w, C.GAM)
    Z = 2.0 * float(np.sum(G ** 2))
    Pc = float(np.trapezoid(w * np.cosh(v / 2.0), v))
    P = 2.0 * Pc * Pc
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
    return Z, P, A, PR


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
    rec("b39 RUN - THE ZERO SIDE AGAINST THE MASSES; THE SECTOR SCAN. Registration banked first.")
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

    rr = np.exp(np.linspace(1e-4, math.log(12.001), EPS_NRHO))
    ee_full = np.atleast_1d(Q.eps(rr, NQ=EPS_NQ, NG=EPS_NG))
    ee_modes = per_mode_eps_grids(rr)

    rec("\n" + "=" * 100)
    rec("ITEM 1 (reading b) + ITEM 2 (reading a) - place set {inf,2,3,5}; headline triple middle")
    rec("=" * 100)
    for a, alab in CELLS:
        v, w2, corr, vc, L = family(a)
        Z, P, A, PR = atlas_columns(a, S4, v, w2, corr, vc, L)
        Thq = theta_quotient(a, S4, corr, vc, L)
        det, prims = None, []
        for (NQ, NMODE) in TRIPLE:
            tr = trace_modes(a, corr, vc, L, NQ, NMODE)
            N = len(tr)
            E2n = np.array([e2_of_grid(a, corr, vc, L, rr, ee_modes[n]) for n in range(N)])
            E2full = e2_of_grid(a, corr, vc, L, rr, ee_full)
            E2even = float(E2n[0::2].sum())
            E2odd = float(E2n[1::2].sum())
            resid = float(tr.sum()) - A - float(E2n.sum())
            s = t_n[:N] / float(t_n[:N].sum())
            wmode = tr - E2n - s * resid
            Wp, Wm = float(wmode[0::2].sum()), float(wmode[1::2].sum())
            if abs(Wp + Wm - A) > 1e-10:
                rec("  SUM GATE FAILED at a^2=%s - VOID" % alab)
                open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
                return
            prim = Z - (Wm - E2even)
            prims.append(prim)
            if (NQ, NMODE) == TRIPLE[1]:
                det = (Wp, Wm, E2even, E2odd, E2full, prim)
        Wp, Wm, E2even, E2odd, E2full, prim = det
        spread = max(abs(p_ - prims[1]) for p_ in prims)
        bracket = Wp + E2even - Thq
        D_closed = (A - PR) - bracket
        D_i = (Thq - PR) - E2full
        DT = (Wp + E2even) - (Wm + E2odd)
        half = 0.5 * (A + E2full)
        D_iii0 = (A - PR) - (half - Thq)
        D_iii1 = (A - PR) - (0.5 * ((A + E2full) + DT) - Thq)
        denom = 0.5 * DT
        kstar = ((A - PR) - (half - Thq)) / denom if abs(denom) > 1e-15 else float("inf")
        rec("a^2=%-4s Z=%9.6f  P=%9.6f  A=%10.6f  PR=%9.6f  Thq=%9.6f" % (alab, Z, P, A, PR, Thq))
        rec("  READING (b): (W_minus - E2even) = %+10.6f   PRIMARY  Z - (W_minus - E2even) = %+10.6f  spread %.5f"
            % (Wm - E2even, prim, spread))
        rec("  aux: E1-bracket = %+10.6f   (bracket - Z) = %+10.6f   (bracket - (Z-P)) = %+10.6f   (D_closed + Z) = %+10.6f"
            % (bracket, bracket - Z, bracket - (Z - P), D_closed + Z))
        rec("  READING (a): D_i(=D_ii, full even Sonin) = %+10.6f   D_iii(k=0) = %+10.6f   D_iii(k=1) = %+10.6f   kappa* = %+8.3f  admissible(|k*|<=1): %s"
            % (D_i, D_iii0, D_iii1, kstar, "YES" if abs(kstar) <= 1.0 else "NO"))
    rec("\nRecorded as data. Verdicts per the registered maps in the act report.")
    rec("NO SIGN SENTENCE AT COMPLETE ROSTER. h2 UNCHANGED. NOTHING DEPOSITS.")
    open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)


if __name__ == "__main__":
    main()
