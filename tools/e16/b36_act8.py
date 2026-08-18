# -*- coding: utf-8 -*-
"""W-CONSTRUCTION-1 act 8 -- b36: BOTH SIDES AT THE MODEL.

Registration: data/b36_registration_2026-08-18.txt (banked FIRST; formulas fixed there).
This instrument computes and records; it decides nothing. No sign sentence at complete
roster. h2 unchanged. Nothing deposits. Nothing circulates.
"""
import math, sys
import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import carto_atlas as C
import carto_auto as CA
import qeps_layer as Q
import b8_sonin_dim as B8
import b10_cells as B10

BANK = r"D:\relay\data\b36_2026-08-18.txt"
CELLS = [(math.sqrt(2), "2"), (math.sqrt(3), "3"), (2.0, "4"),
         (math.sqrt(8), "8"), (3.0, "9"), (math.sqrt(12), "12")]
S3, S4 = (2, 3), (2, 3, 5)
TRIPLE = [(500, 8), (700, 10), (900, 11)]   # (NQ, NMODE); headline = middle
                                             # (the qeps layer holds NTERM = 11 modes;
                                             #  the registered 12 is capped to 11, said so)
NU_HALF = 401                                # u >= 0 points (801-grid's half)
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


def trace_modes(a, corr, vc, L, NQ, NMODE):
    """per-mode trace terms <xi_n, theta(f_a) xi_n>, P2 half-line convention."""
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(NQ)
    NMODE = min(NMODE, xi.shape[1])
    uu = np.linspace(0.0, 2 * L, NU_HALF)
    cu = np.interp(uu, vc, corr)
    tr = np.zeros(NMODE)
    sanity = np.zeros(NMODE)
    for n in range(NMODE):
        f = xi[:, n]
        An = np.empty(len(uu))
        for i, u in enumerate(uu):
            lamd = math.exp(u)
            fy = np.interp(lamd * x, x, f, left=0.0, right=0.0)
            An[i] = math.sqrt(lamd) * 0.5 * float((w * f * fy).sum())
        sanity[n] = An[0]                      # should be ~1 (norm)
        tr[n] = 2.0 * float(np.trapezoid(cu * An, uu))
    return tr, sanity


def eps_grid():
    rr = np.exp(np.linspace(1e-4, math.log(12.001), EPS_NRHO))
    ee = Q.eps(rr, NQ=EPS_NQ, NG=EPS_NG)
    return rr, np.atleast_1d(ee)


def e2_term(a, corr, vc, L, rr, ee):
    uu = np.linspace(0.0, 2 * L, NU_HALF)
    cu = np.interp(uu, vc, corr)
    eu = np.interp(np.exp(uu), rr, ee)
    return 2.0 * float(np.trapezoid(cu * eu, uu))


def theta_quotient(a, primes, corr, vc, L):
    total = 0.0
    shape_rows = []
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
            shape_rows.append((p, n, k, tq, tq * p ** (k / 2.0)))
    return total, shape_rows


def main():
    out = []
    def rec(s):
        print(s)
        out.append(s)

    rec("=" * 100)
    rec("b36 RUN - BOTH SIDES AT THE MODEL. Registration banked first; formulas fixed there.")
    rec("=" * 100)

    # C0 VOID gates
    rec("\n--- C0: VOID GATES ---")
    void = False
    for a in (1.30, 3.50):
        r = CA.channels_auto(a)
        ok = abs(r["residual"]) <= C.TOL
        void |= not ok
        rec("  carto far-end a=%.2f residual=%+.3e %s" % (a, r["residual"], "PASS" if ok else "FAIL"))
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(EPS_NQ)
    g1 = abs(float(lam2.sum()) - 2.237484835)
    g2 = abs(float((lam2 * xi1 ** 2).sum()) - 2.0)
    g3 = abs(Q.epsprime1(EPS_NQ) - 22.9964757)
    for name, gval, tol in (("sum lam2", g1, 1e-6), ("sum lam2 xi1^2", g2, 1e-6),
                            ("epsprime1", g3, 1e-3)):
        ok = gval <= tol
        void |= not ok
        rec("  prolate pin %-16s |delta|=%.2e (tol %.0e) %s" % (name, gval, tol, "PASS" if ok else "FAIL"))
    if void:
        rec("\n  C0 FAILED - THE RUN IS VOID. No table follows.")
        open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
        return

    rec("\n--- eps grid (fixed, NQ=%d NG=%d, %d pts on (1,12]) ---" % (EPS_NQ, EPS_NG, EPS_NRHO))
    rr, ee = eps_grid()
    for rprobe in (1.5, 2.5):
        e_hi = Q.eps(rprobe, NQ=EPS_NQ, NG=2 * EPS_NG)
        e_lo = float(np.interp(rprobe, rr, ee))
        rec("  eps convergence probe rho=%.1f: grid=%.8f NGx2=%.8f  |d|=%.2e" %
            (rprobe, e_lo, e_hi, abs(e_hi - e_lo)))

    # the table
    for Sname, primes in (("S3={inf,2,3}", S3), ("S4={inf,2,3,5}", S4)):
        rec("\n" + "=" * 100)
        rec("PLACE SET %s" % Sname)
        rec("=" * 100)
        hdr = ("%-6s %10s %10s %10s | %10s %10s %10s %10s | %12s %10s %8s"
               % ("a^2", "A", "PR", "LEFT", "Tr_full", "E2", "Dneg", "Thq", "RIGHT", "D", "spread"))
        rec(hdr)
        for a, alab in CELLS:
            v, w2, corr, vc, L = family(a)
            A, PR = left_side(a, primes, v, w2, corr, vc, L)
            LEFT = A - PR
            Ds = []
            det = None
            for (NQ, NMODE) in TRIPLE:
                tr, sanity = trace_modes(a, corr, vc, L, NQ, NMODE)
                Tr_full = float(tr.sum())
                Dneg = float(tr[1::2].sum())
                E2 = e2_term(a, corr, vc, L, rr, ee)
                Thq, shape = theta_quotient(a, primes, corr, vc, L)
                RIGHT = (Tr_full + E2 - Dneg) - Thq
                D = LEFT - RIGHT
                Ds.append(D)
                if (NQ, NMODE) == TRIPLE[1]:
                    det = (Tr_full, E2, Dneg, Thq, RIGHT, D, tr, sanity, shape)
            Tr_full, E2, Dneg, Thq, RIGHT, D, tr, sanity, shape = det
            spread = max(abs(d - Ds[1]) for d in Ds)
            rec("%-6s %10.6f %10.6f %10.6f | %10.6f %10.6f %10.6f %10.6f | %12.6f %10.6f %8.5f"
                % (alab, A, PR, LEFT, Tr_full, E2, Dneg, Thq, RIGHT, D, spread))
            resid47 = Tr_full - (A + E2)
            rec("        C1 resid47 = Tr_full - (A + E2) = %+.6f   |  C3 Dneg/Tr_full = %s"
                % (resid47, ("%.4f" % (Dneg / Tr_full)) if abs(Tr_full) > 1e-12 else "n/a"))
            rec("        mode terms: %s  (mode-0 norm sanity: %.6f)"
                % (" ".join("%+.5f" % t for t in tr), sanity[0]))
            if shape:
                rec("        C2 tau_q shape: " + "  ".join(
                    "p=%d n=%d k=%d tq=%.5f tq*p^{k/2}=%.5f" % s for s in shape))
    rec("\nRecorded as data. The verdict per the registered map is written in the act report,")
    rec("not here. NO SIGN SENTENCE AT COMPLETE ROSTER. h2 UNCHANGED. NOTHING DEPOSITS.")
    open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)


if __name__ == "__main__":
    main()
