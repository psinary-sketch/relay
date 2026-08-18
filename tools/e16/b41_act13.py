# -*- coding: utf-8 -*-
"""W-CONSTRUCTION-1 act 13 -- b41: THE SCALE-COVARIANT ARCHIMEDEAN FAMILY.

Registration: data/b41_registration_2026-08-18.txt (banked FIRST: the dictionary D1-D4,
the anchor-invariance, the longhand prediction, the next-name candidate). Computes and
records; decides nothing beyond the registered maps. No sign sentence at complete
roster.
"""
import math, sys
import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import carto_atlas as C
import carto_auto as CA
import qeps_layer as Q

BANK = r"D:\relay\data\b41_2026-08-18.txt"
CELLS = [(math.sqrt(2), "2"), (math.sqrt(3), "3"), (2.0, "4"),
         (math.sqrt(8), "8"), (3.0, "9"), (math.sqrt(12), "12")]
NQ_TRIPLE = (500, 700, 900)
NU_HALF = 401


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


def prolate_c(NQ, c):
    """the certified prolate machinery with c a parameter (mirrors prolate_layer)."""
    x, wq = np.polynomial.legendre.leggauss(NQ)
    XX = np.subtract.outer(x, x)
    K = np.where(np.abs(XX) < 1e-14, c / math.pi, np.sin(c * XX) / (math.pi * XX))
    sw = np.sqrt(wq)
    A = (sw[:, None] * K) * sw[None, :]
    vals, V = np.linalg.eigh(A)
    idx = np.argsort(vals)[::-1]
    mu = vals[idx]
    psi = (V / sw[:, None])[:, idx]
    return x, wq, mu, psi


def fourier_phases(x, wq, psi, c, nmodes):
    """phase of <psi_k, F_c psi_k> per mode (the E1-rule measurement)."""
    ph = []
    for k in range(nmodes):
        f = psi[:, k]
        Ff = (np.exp(1j * c * np.outer(x, x)) * (wq * f)).sum(axis=1)
        num = complex((wq * np.conj(f) @ Ff))
        den = float((wq * f * f).sum())
        z = num / den
        ph.append(z)
    return ph


def e1_trace(a, corr, vc, L, x, wq, psi, mu, e1_modes):
    """raw band trace terms over the given CC-index mode list (xi_n = sqrt2 psi_{2n})."""
    uu = np.linspace(0.0, 2 * L, NU_HALF)
    cu = np.interp(uu, vc, corr)
    terms = []
    for n in e1_modes:
        f = math.sqrt(2) * psi[:, 2 * n]
        nrm = 0.5 * float((wq * f * f).sum())          # half-line norm; should be ~1
        An = np.empty(len(uu))
        for i, u in enumerate(uu):
            lamd = math.exp(u)
            fy = np.interp(lamd * x, x, f, left=0.0, right=0.0)
            An[i] = math.sqrt(lamd) * 0.5 * float((wq * f * fy).sum())
        terms.append(2.0 * float(np.trapezoid(cu * (An / nrm), uu)))
    return terms


def main():
    out = []
    def rec(s):
        print(s)
        out.append(s)

    rec("=" * 100)
    rec("b41 RUN - THE SCALE-COVARIANT FAMILY. Registration banked first (D1-D4; the anchor;")
    rec("the longhand prediction; the next-name candidate).")
    rec("=" * 100)

    rec("\n--- C0: VOID GATES (the anchor layer must reproduce the battery) ---")
    void = False
    for a in (1.30, 3.50):
        r = CA.channels_auto(a)
        ok = abs(r["residual"]) <= C.TOL
        void |= not ok
        rec("  carto far-end a=%.2f residual=%+.3e %s" % (a, r["residual"], "PASS" if ok else "FAIL"))
    x0, w0, mu0, psi0 = prolate_c(700, 2 * math.pi)
    lam2_anchor = mu0[0::2][:11]
    g1 = abs(float(lam2_anchor.sum()) - 2.237484835)
    g2 = abs(float(mu0[mu0 > 1e-13].sum()) - 4.0)     # tr Q_{2pi} = 4 (Shannon, D1)
    for name, gval, tol in (("anchor sum lam2 (even 11)", g1, 1e-6),
                            ("anchor tr Q_c vs 2c/pi=4", g2, 4e-2)):
        ok = gval <= tol
        void |= not ok
        rec("  pin %-26s |delta|=%.2e (tol %.0e) %s" % (name, gval, tol, "PASS" if ok else "FAIL"))
    if void:
        rec("\n  C0 FAILED - VOID.")
        open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
        return

    rec("\n%-6s %8s %8s %10s %10s | %12s %10s | %s"
        % ("a^2", "c/pi", "trQ gate", "N_eff=2c/pi", "-A (bound)", "Tr_E1 (band)", "spread", "verdict row"))
    results = []
    for a, alab in CELLS:
        v, w, corr, vc, L = family(a)
        A = arch_A(a, v, w)
        bound = -A
        c = math.pi * a * a
        neff = 2 * c / math.pi
        vals = []
        det = None
        for NQ in NQ_TRIPLE:
            x, wq, mu, psi = prolate_c(NQ, c)
            trq = float(mu[mu > 1e-13].sum())
            # the E1 rule measured: phases of the even ladder
            nCC = min(int(neff) + 4, (len(mu) // 2) - 1)
            ph = fourier_phases(x, wq, psi, c, 2 * nCC)
            even_ph = [ph[2 * n] for n in range(nCC)]
            # normalized phases: z / |z| real part pattern; the rule: alternation of sign
            pat = ["+" if z.real > 0 else "-" for z in even_ph]
            alt = all(pat[i] != pat[i + 1] for i in range(len(pat) - 1))
            e1_modes = [n for n in range(nCC) if (n % 2 == 0) == (pat[0] == "+")] \
                if alt else [n for n in range(nCC) if n % 2 == 0]
            terms = e1_trace(a, corr, vc, L, x, wq, psi, mu, e1_modes)
            tr_e1 = float(sum(terms))
            vals.append(tr_e1)
            if NQ == 700:
                det = (trq, pat, alt, e1_modes, terms, tr_e1)
        trq, pat, alt, e1_modes, terms, tr_e1 = det
        spread = max(abs(t - vals[1]) for t in vals)
        gate = abs(trq - neff)
        row_ok = tr_e1 <= bound
        rec("%-6s %8.2f %8.3f %10.1f %10.5f | %12.5f %10.5f | band form %s bound  %s"
            % (alab, c / math.pi, gate, neff, bound, tr_e1, spread,
               "<=" if row_ok else ">", "REPAIRED" if row_ok else "fails"))
        rec("        E1 rule per c: even-ladder phase pattern %s  alternation %s  E1 modes %s"
            % ("".join(pat[:10]), "YES" if alt else "NO (fallback: even n)", e1_modes[:6]))
        rec("        E1 terms: %s" % " ".join("%+.4f" % t for t in terms[:8]))
        results.append((alab, tr_e1, bound, row_ok))
    n_rep = sum(1 for r in results if r[3])
    rec("\nrepaired cells: %d of %d" % (n_rep, len(results)))
    if n_rep == len(results):
        rec("(COV-repairs) numerically indicated - AGAINST the registered anchor argument;")
        rec("the anchor row above must be re-examined before any verdict. The report rules.")
    elif n_rep > 0:
        rec("(COV-partial) numerically indicated; the failing cells' addresses in the rows.")
    else:
        rec("(COV-none) numerically indicated, per the registered longhand prediction;")
        rec("the next-name candidate (THE SONIN SUBTRACTION) stands as registered - a")
        rec("candidate, not a conclusion. Item 3 NOT licensed.")
    rec("\nRecorded as data. NO SIGN SENTENCE AT COMPLETE ROSTER. h2 UNCHANGED. NOTHING DEPOSITS.")
    open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)


if __name__ == "__main__":
    main()
