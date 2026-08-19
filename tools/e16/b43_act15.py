# -*- coding: utf-8 -*-
"""W-CONSTRUCTION-1 act 15 -- b43: THE BALL AT CC'S SCALE.

Registration: data/b43_registration_2026-08-18.txt (banked FIRST: the derived relation
R1-R4, the gram gate as the derivation's own check, the branches with no prediction).
Computes and records; decides nothing beyond the registered maps.
"""
import math, sys
import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import carto_atlas as C
import carto_auto as CA

BANK = r"D:\relay\data\b43_2026-08-18.txt"
CELLS = [(math.sqrt(2), "2"), (math.sqrt(3), "3"), (2.0, "4"),
         (math.sqrt(8), "8"), (3.0, "9"), (math.sqrt(12), "12")]
NQ_TRIPLE = (500, 700, 900)
NMODE_MAIN, NMODE_TAIL = 8, 11
NU_HALF = 401
S4 = (2, 3, 5)


def family(a):
    v, w = C.bump(a)
    dv = np.gradient(v)
    L = math.log(a)
    corr = np.convolve(w, w, mode="full") * float(dv[0])
    vc = np.linspace(-2 * L, 2 * L, corr.size)
    return v, w, corr, vc, L


def arch_A(a, v, w):
    U = np.linspace(-C.UMAX, C.UMAX, C.NU)
    GU = C.hhat(v, w, U)
    return float(np.trapezoid(GU ** 2 * C.kernel(U), U) / (2.0 * math.pi))


def PR_of(a, corr, vc, L):
    PR = 0.0
    for p in S4:
        k = 1
        while p ** k <= a * a + 1e-12:
            ln = math.log(p ** k)
            if ln <= 2 * L:
                PR += 2.0 * math.log(p) / math.sqrt(p ** k) * float(np.interp(ln, vc, corr))
            k += 1
    return PR


def thq_of(a, corr, vc, L):
    import b8_sonin_dim as B8
    import b10_cells as B10
    total = 0.0
    for p in S4:
        n, k = 0, 1
        while p ** k <= a * a + 1e-12:
            n += 1
            k += 1
        n = min(n, 3)
        if n < 1:
            continue
        N, K, d = B10.quotient_basis(p, n)
        U = B8.scaling_matrix(p, n)
        S = K @ K.T
        Uk = np.eye(N)
        for kk in range(1, 2 * n):
            Uk = U @ Uk
            tq = abs(complex(np.trace(Uk @ S))) / d
            ln = kk * math.log(p)
            if ln <= 2 * L:
                total += math.log(p) * tq * 2.0 * float(np.interp(ln, vc, corr))
    return total


def prolate_c(NQ, c):
    x, wq = np.polynomial.legendre.leggauss(NQ)
    XX = np.subtract.outer(x, x)
    K = np.where(np.abs(XX) < 1e-14, c / math.pi, np.sin(c * XX) / (math.pi * XX))
    sw = np.sqrt(wq)
    A = (sw[:, None] * K) * sw[None, :]
    vals, V = np.linalg.eigh(A)
    idx = np.argsort(vals)[::-1]
    return x, wq, vals[idx], (V / sw[:, None])[:, idx]


def cell_rows(a, corr, vc, L, NQ, c, nmode, ymax):
    """per-E1-mode tr_n, x_n, gram_n at bandwidth c; the corrected sum."""
    x, wq, mu, psi = prolate_c(NQ, c)
    uu = np.linspace(0.0, 2 * L, NU_HALF)
    cu = np.interp(uu, vc, corr)
    yg = np.linspace(0.0, ymax, 2400)
    rows = []
    for n in range(0, nmode, 1):
        if n % 2 == 1:
            continue                                  # E1 = even CC index
        f = psi[:, 2 * n]
        nrm2 = float((wq * f * f).sum())              # full-line norm^2 (=1)
        f = f / math.sqrt(nrm2)
        # eta = F_c f on the fine y-grid (even mode: cosine kernel), normalization
        # sqrt(c/2pi): eta(y) = sqrt(c/2pi) * int cos(c y t) f(t) dt
        eta = math.sqrt(c / (2 * math.pi)) * (np.cos(c * np.outer(yg, x)) @ (wq * f))
        gram = float(np.interp(np.abs(x), yg, eta) @ (wq * f))   # <f, eta> full line
        lam_signed = ((-1) ** n) * math.sqrt(max(mu[2 * n], 0.0))
        trn = 0.0
        xn = 0.0
        for i, u in enumerate(uu):
            lamd = math.exp(u)
            fy = np.interp(lamd * np.abs(x), np.append(np.abs(x[x >= 0]), 2.0),
                           np.append(f[x >= 0], 0.0)) if False else \
                 np.interp(lamd * x, x, f, left=0.0, right=0.0)
            An = math.sqrt(lamd) * 0.5 * float((wq * f * fy).sum())
            ey = np.interp(np.abs(lamd * x), yg, eta, right=0.0)
            Bn = math.sqrt(lamd) * 0.5 * float((wq * f * ey).sum())
            trn += (2.0 if i not in (0, len(uu) - 1) else 1.0) * cu[i] * An
            xn += (2.0 if i not in (0, len(uu) - 1) else 1.0) * cu[i] * Bn
        du = uu[1] - uu[0]
        trn = trn * du * 2.0 * 0.5 * 2.0              # trapezoid *2 (sym) -- match b41: 2*trapz
        xn = xn * du * 2.0 * 0.5 * 2.0
        # NOTE: the trapezoid assembly above equals 2*np.trapezoid(cu*An_vec, uu); the
        # A_n(1)=norm sanity is carried by the gram gate instead (An at u=0 = 0.5*<f,f>*2)
        corrected = (gram * trn - xn) / (1.0 + gram)
        rows.append((n, trn, xn, gram, lam_signed, corrected))
    return rows


def main():
    out = []
    def rec(s):
        print(s)
        out.append(s)

    rec("=" * 100)
    rec("b43 RUN - THE BALL AT CC'S SCALE. Registration banked first (R1-R4; the gram gate;")
    rec("no prediction registered).")
    rec("=" * 100)

    rec("\n--- G2: VOID GATES ---")
    void = False
    for a in (1.30, 3.50):
        r = CA.channels_auto(a)
        ok = abs(r["residual"]) <= C.TOL
        void |= not ok
        rec("  carto far-end a=%.2f residual=%+.3e %s" % (a, r["residual"], "PASS" if ok else "FAIL"))
    x, wq, mu, psi = prolate_c(700, 2 * math.pi)
    g1 = abs(float(mu[0::2][:11].sum()) - 2.237484835)
    ok = g1 <= 1e-6
    void |= not ok
    rec("  anchor battery |sum lam2 - pin| = %.2e %s" % (g1, "PASS" if ok else "FAIL"))
    if void:
        rec("\n  G2 FAILED - VOID.")
        open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
        return

    for a, alab in CELLS:
        v, w, corr, vc, L = family(a)
        A = arch_A(a, v, w)
        bound = -A
        PR = PR_of(a, corr, vc, L)
        Thq = thq_of(a, corr, vc, L)
        c = math.pi * a * a
        ymax = (a * a) * 1.05 + 0.1
        sums, det = [], None
        for NQ in NQ_TRIPLE:
            rows = cell_rows(a, corr, vc, L, NQ, c, NMODE_MAIN, ymax)
            s = sum(r[5] for r in rows)
            sums.append(s)
            if NQ == 700:
                det = rows
        rows = det
        s_main = sums[1]
        spread = max(abs(s - s_main) for s in sums)
        rows_tail = cell_rows(a, corr, vc, L, 700, c, NMODE_TAIL, ymax)
        s_tail = sum(r[5] for r in rows_tail)
        marg = bound - s_main
        dcov = (bound - PR) - (s_main + Thq)
        g1max = max(abs(r[3] - r[4]) for r in rows)
        rec("\na^2=%-4s c=%5.2fpi  bound=%8.5f  PR=%7.5f  Thq=%7.5f" % (alab, c / math.pi, bound, PR, Thq))
        rec("  G1 gram gate: max|gram_n - signed lam_n| = %.2e  %s"
            % (g1max, "PASS" if g1max <= 5e-3 else "### FLAG - the derivation check misses"))
        rec("  per-mode (n, tr, x, gram, corrected): %s"
            % "  ".join("(%d, %.4f, %.4f, %+.4f, %.4f)" % (r[0], r[1], r[2], r[3], r[5]) for r in rows))
        rec("  Tr_corrected(E1) = %9.6f  (tail NMODE=11: %9.6f)   spread %.5f" % (s_main, s_tail, spread))
        rec("  margin' = %+9.6f   D_cov' = %+9.6f   %s"
            % (marg, dcov, "STABLE" if spread < max(0.05 * abs(marg), 5e-3) else "UNSTABLE - indeterminate"))
    rec("\nRecorded as data. Verdicts per the registered maps in the act report.")
    rec("NO SIGN SENTENCE AT COMPLETE ROSTER. h2 UNCHANGED. NOTHING DEPOSITS.")
    open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)


if __name__ == "__main__":
    main()
