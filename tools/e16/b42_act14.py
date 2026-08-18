# -*- coding: utf-8 -*-
"""W-CONSTRUCTION-1 act 14 -- b42: THE RESOLUTION SWEEP at the stable cells.

Registration: data/b42_registration_2026-08-18.txt (banked FIRST; the prediction:
(N-floor) at the anchor ~ 0.126). Computes and records; decides nothing beyond the
registered maps. No sign sentence at complete roster.
"""
import math, sys
import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import carto_atlas as C
import carto_auto as CA

BANK = r"D:\relay\data\b42_2026-08-18.txt"
CELLS = [(math.sqrt(2), "2"), (math.sqrt(3), "3"), (2.0, "4")]
NQ_LADDER = (300, 500, 700, 900, 1100)
NMODE_LADDER = (8, 11, 14)
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


def e1_trace(a, corr, vc, L, x, wq, psi, nCC):
    uu = np.linspace(0.0, 2 * L, NU_HALF)
    cu = np.interp(uu, vc, corr)
    tot = 0.0
    for n in range(0, nCC, 2):                      # E1 = even CC index (rule verified
        f = math.sqrt(2) * psi[:, 2 * n]            # at these c's in b41)
        nrm = 0.5 * float((wq * f * f).sum())
        An = np.empty(len(uu))
        for i, u in enumerate(uu):
            lamd = math.exp(u)
            fy = np.interp(lamd * x, x, f, left=0.0, right=0.0)
            An[i] = math.sqrt(lamd) * 0.5 * float((wq * f * fy).sum())
        tot += 2.0 * float(np.trapezoid(cu * (An / nrm), uu))
    return tot


def main():
    out = []
    def rec(s):
        print(s)
        out.append(s)

    rec("=" * 100)
    rec("b42 RUN - THE RESOLUTION SWEEP (stable cells; NQ x NMODE ladder). Registration banked first.")
    rec("=" * 100)

    rec("\n--- C0 ---")
    void = False
    for a in (1.30, 3.50):
        r = CA.channels_auto(a)
        ok = abs(r["residual"]) <= C.TOL
        void |= not ok
        rec("  carto far-end a=%.2f residual=%+.3e %s" % (a, r["residual"], "PASS" if ok else "FAIL"))
    for NQ in (500, 700, 900, 1100):
        x, wq, mu, psi = prolate_c(NQ, 2 * math.pi)
        g = abs(float(mu[0::2][:11].sum()) - 2.237484835)
        ok = g <= 1e-6
        void |= not ok
        rec("  anchor battery at NQ=%d: |sum lam2 - pin| = %.2e %s" % (NQ, g, "PASS" if ok else "FAIL"))
    if void:
        rec("\n  C0 FAILED - VOID.")
        open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
        return

    for a, alab in CELLS:
        v, w, corr, vc, L = family(a)
        A = arch_A(a, v, w)
        bound = -A
        PR = PR_of(a, corr, vc, L)
        Thq = thq_of(a, corr, vc, L)
        c = math.pi * a * a
        rec("\na^2 = %s   c = %.3f   bound (-A) = %.6f   PR = %.5f   Thq = %.5f" % (alab, c, bound, PR, Thq))
        rec("  %-6s %-7s %12s %12s %12s" % ("NQ", "NMODE", "Tr_E1", "margin", "D_cov"))
        margins = {}
        for NQ in NQ_LADDER:
            x, wq, mu, psi = prolate_c(NQ, c)
            shq = abs(float(mu[mu > 1e-13].sum()) - 2 * c / math.pi)
            for NM in NMODE_LADDER:
                tr = e1_trace(a, corr, vc, L, x, wq, psi, NM)
                marg = bound - tr
                dcov = (bound - PR) - (tr + Thq)
                margins[(NQ, NM)] = marg
                rec("  %-6d %-7d %12.6f %12.6f %12.6f%s"
                    % (NQ, NM, tr, marg, dcov,
                       ("   [Shannon gate %.1e]" % shq) if NM == NMODE_LADDER[0] else ""))
        vals = [margins[(NQ, 11)] for NQ in NQ_LADDER]
        drift = max(vals) - min(vals)
        top3 = [margins[(NQ, 11)] for NQ in NQ_LADDER[-3:]]
        flat = max(top3) - min(top3)
        rec("  margin at NMODE=11 across NQ ladder: %s" % " ".join("%+.6f" % vv for vv in vals))
        rec("  full-ladder drift %.2e; top-3-rung flatness %.2e -> %s"
            % (drift, flat, "FLOOR-shaped (flat to precision)" if flat < 5e-3 else "still moving"))
    rec("\nRecorded as data. Verdicts per the registered maps in the act report.")
    rec("NO SIGN SENTENCE AT COMPLETE ROSTER. h2 UNCHANGED. NOTHING DEPOSITS.")
    open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)


if __name__ == "__main__":
    main()
