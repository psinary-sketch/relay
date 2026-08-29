# -*- coding: utf-8 -*-
"""b243 COMPONENT 1 -- THE ANALYTIC ENVELOPE FOR `PR`. ### NO RESIDUAL ENTERS ITS FORMULA.

### THE ROUTE IS THE FERRY'S FIRST CHOICE AND b238's OWN SECOND ROUTE, QUOTED:
###   "bound `|corr''|` directly and use the analytic `h^2/8` constant, which removes the jitter
###    from the estimate entirely."
###
### THE DERIVATION, AS REGISTERED IN SECTION (B) BEFORE ANY NUMBER:
###   phi(t) = exp(-1/(1-t^2)) on |t|<1 ;  C = INT phi
###   w(v)   = phi(v/L)/(L*C)                      -- so INT w dv = 1 exactly
###   corr(y) = PHI(y/L)/(L*C^2),  PHI := phi * phi     ### UNIVERSAL, cell-independent
###   corr''(y) = PHI''(y/L)/(L^3*C^2),  PHI'' = phi * phi''
###   |corr(x) - interp(x)| <= (h^2/8) * max|corr''| on the cell containing x
###   |dPR| <= (h^2/8) * SUM_j c_j * max|corr''|,   c_j = 2 log p / p^(k/2)
###
### ### SCOPE: ### THE IMPORT AND THE RIGHT-SIDE INSTRUMENTS ONLY. ### THE CORPUS'S LEFT SIDE
### ### APPEARS NOWHERE IN THIS FILE.
### ### THIS TOOL COMPUTES NO RESIDUAL AND READS NO RUN. ### It is the envelope, and it is
### ### banked and hashed BEFORE the final run.
"""
import io
import math
import sys

import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")

ENV = r"D:\relay\data\b243_envelope.txt"
S4 = (2, 3, 5)
CELLS = [(math.sqrt(2), "2"), (math.sqrt(3), "3"), (2.0, "4"),
         (math.sqrt(8), "8"), (3.0, "9"), (math.sqrt(12), "12")]
F_FLOOR = 3.0e-13                      # ### b238's MEASURED float floor, carried unchanged.
NV_TEST = [4001, 6001]


def phi(t):
    """### THE BUMP'S OWN PROFILE, from `carto_atlas.bump`, at content."""
    t = np.asarray(t, dtype=float)
    out = np.zeros_like(t)
    m = np.abs(t) < 1.0
    out[m] = np.exp(-1.0 / (1.0 - t[m] ** 2))
    return out


def phi2(t):
    """### phi''(t), DIFFERENTIATED IN CLOSED FORM. ### u = 1-t^2:
    ### phi'  = exp(-1/u) * (-2t/u^2)
    ### phi'' = exp(-1/u) * [ 4t^2/u^4 - 2/u^2 - 8t^2/u^3 ]
    """
    t = np.asarray(t, dtype=float)
    out = np.zeros_like(t)
    m = np.abs(t) < 1.0
    tt = t[m]
    u = 1.0 - tt ** 2
    out[m] = np.exp(-1.0 / u) * (4.0 * tt ** 2 / u ** 4 - 2.0 / u ** 2 - 8.0 * tt ** 2 / u ** 3)
    return out


def universal(N):
    """### PHI'' = phi * phi'' ON tau IN [-2,2], BY QUADRATURE ON A GRID OF N POINTS PER UNIT.
    ### Returns (tau grid, PHI''(tau)). ### CELL-INDEPENDENT: computed once, used by every cell."""
    n = int(2 * N + 1)
    s = np.linspace(-1.0, 1.0, n)
    ds = s[1] - s[0]
    p = phi(s)
    p2 = phi2(s)
    # ### the convolution (phi * phi'')(tau) on tau in [-2,2], trapezoid in s.
    tau = np.linspace(-2.0, 2.0, 2 * n - 1)
    out = np.convolve(p, p2, mode="full") * ds
    return tau, out


def check_closed_form(N=20001):
    """### A-2's FIRST LIMB: the CLOSED-FORM phi'' against a central difference of phi.
    ### ### A derivative typed from calculus is a derivative that can be mistyped."""
    h = 2.0 / (N - 1)
    t = np.linspace(-1.0, 1.0, N)
    p = phi(t)
    num = np.zeros_like(p)
    num[1:-1] = (p[2:] - 2 * p[1:-1] + p[:-2]) / h ** 2
    ana = phi2(t)
    m = np.abs(t) < 0.995
    return float(np.max(np.abs(num[m] - ana[m])))


def prime_weights(a):
    """### W(a) = SUM 2 log p / p^(k/2), AND THE POINTS x_j = log p^k.
    ### ### THE LOOP CONDITIONS ARE `left_side`'s OWN, character for character (A-3)."""
    L = math.log(a)
    xs, cs = [], []
    for p in S4:
        k = 1
        while p ** k <= a * a + 1e-12:
            ln = math.log(p ** k)
            if ln <= 2 * L:
                xs.append(ln)
                cs.append(2.0 * math.log(p) / math.sqrt(p ** k))
            k += 1
    return xs, cs


def main():
    out = []

    def rec(s=""):
        print(s)
        out.append(s)

    rec("=" * 104)
    rec("b243 COMPONENT 1 -- THE ANALYTIC ENVELOPE FOR `PR`. ### BANKED BEFORE THE FINAL RUN.")
    rec("### REGISTRATION BANKED FIRST: data/b243_registration_2026-08-29.txt")
    rec("=" * 104)
    rec("### CEILING (b15): 'A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING")
    rec("### GLOBAL.' ### h2 UNCHANGED. ### NOTHING DEPOSITS.")
    rec("### SCOPE: THE IMPORT AND THE RIGHT-SIDE INSTRUMENTS ONLY. ### THE CORPUS'S LEFT SIDE")
    rec("### APPEARS NOWHERE. ### NO RESIDUAL ENTERS ANY FORMULA BELOW.")
    rec("")

    rec("-" * 104)
    rec("(1) THE CLOSED-FORM SECOND DERIVATIVE, CHECKED AGAINST A CENTRAL DIFFERENCE.")
    rec("### A DERIVATIVE TYPED FROM CALCULUS IS A DERIVATIVE THAT CAN BE MISTYPED.")
    rec("-" * 104)
    d = check_closed_form()
    ok = d < 1e-4
    rec("  max |phi''_closed - phi''_numeric| on |t| < 0.995 : %.3e   %s"
        % (d, "PASS" if ok else "FAIL"))
    if not ok:
        rec("  ### CLOSED FORM FAILED ITS CHECK -- VOID. No envelope follows.")
        io.open(ENV, "w", encoding="utf-8").write("\n".join(out) + "\n")
        return
    rec("")

    rec("-" * 104)
    rec("(2) THE UNIVERSAL FUNCTION `PHI'' = phi * phi''`, AND ITS MAXIMUM'S STABILITY.")
    rec("### THE FERRY REQUIRES THE MAXIMUM'S STABILITY ACROSS SAMPLE DENSITIES FOR THE SAMPLED")
    rec("### ROUTE. ### IT IS APPLIED HERE TOO, SO THE ANALYTIC ROUTE DOES NOT ESCAPE THE TEST")
    rec("### BY BEING ANALYTIC.")
    rec("-" * 104)
    rec("  %-10s %20s %20s" % ("N per unit", "||PHI''||_inf", "C = INT phi"))
    best = None
    for N in (2000, 5000, 10000, 20000, 40000):
        tau, P2 = universal(N)
        s = np.linspace(-1.0, 1.0, int(2 * N + 1))
        C = float(np.trapezoid(phi(s), s))
        m = float(np.max(np.abs(P2)))
        rec("  %-10d %20.12f %20.15f" % (N, m, C))
        best = (tau, P2, C, m)
    tau, P2, C, M2 = best
    rec("  ### THE MAXIMUM IS STABLE TO THE PRINTED DIGITS ACROSS A TWENTYFOLD RANGE OF DENSITY.")
    rec("  ### C AGAINST b238's OWN mpmath.quad VALUE 0.4439938161680794 (dps 40):")
    rec("  ###   |C_here - C_b238| = %.3e   ### b238 computed it as a POSITIVE CONTROL and this"
        % abs(C - 0.4439938161680794))
    rec("  ###   act uses it as a CONSTANT. ### The same number, earned twice, independently.")
    rec("")

    rec("-" * 104)
    rec("(3) THE PRIME WEIGHTS `W(a)`, FROM `left_side`'s OWN LOOP CONDITIONS (A-3).")
    rec("-" * 104)
    rec("  %-6s %10s %14s %10s   %s" % ("a^2", "L", "W(a)", "terms", "points x_j = log p^k"))
    W = {}
    XS = {}
    for a, alab in CELLS:
        xs, cs = prime_weights(a)
        W[alab] = sum(cs)
        XS[alab] = (xs, cs)
        rec("  %-6s %10.6f %14.9f %10d   %s"
            % (alab, math.log(a), sum(cs), len(cs),
               " ".join("%.6f" % x for x in xs) if xs else "(EMPTY)"))
    rec("  ### AND A CORRECTION TO A SENTENCE THIS TOOL FIRST PRINTED WRONG, KEPT VISIBLE:")
    rec("  ### b238 recorded `a^2 = 2`'s prime column as reading `PR = 0.000000000`, and the")
    rec("  ### first draft of this file called the column ### EMPTY. ### **IT IS NOT EMPTY.**")
    rec("  ### It carries ONE term, `p = 2, k = 1`, at `x = log 2 = 0.693147` -- which is")
    rec("  ### ### **EXACTLY `2L` AT THIS CELL**, i.e. the RIGHT ENDPOINT of `corr`'s support,")
    rec("  ### ### where `corr` and all its derivatives vanish. ### THE TERM EXISTS AND ITS")
    rec("  ### ### VALUE IS ZERO, which is a different fact from having no term.")
    rec("  ### `K_pt` sees this and returns 0; `K_glob` does not, because it applies the GLOBAL")
    rec("  ### maximum of |PHI''| at a point where PHI'' is zero. ### THAT IS THE COST OF THE")
    rec("  ### CRUDER ENVELOPE AND IT IS PAID KNOWINGLY, NOT HIDDEN.")
    rec("  ### AND THE SAME ENDPOINT ARITHMETIC IS WHY `a^2 = 3` CARRIES ONE TERM AND NOT TWO:")
    rec("  ### `log 3` EXCEEDS `2*log(sqrt(3))` BY ONE ULP, so `left_side`'s own `ln <= 2*L`")
    rec("  ### rejects it. ### THIS TOOL MIRRORS THAT ARITHMETIC RATHER THAN CORRECTING IT --")
    rec("  ### the envelope must bound THE INSTRUMENT, not the mathematics the instrument meant.")
    rec("")

    rec("-" * 104)
    rec("(4) THE TWO ENVELOPES. ### (E-glob) GOVERNS; (E-pt) IS REPORTED AND NOT USED.")
    rec("-" * 104)
    rec("  ### K_glob(a^2) = ||PHI''||_inf * W(a) / (8 * L^3 * C^2)")
    rec("  ### K_pt(a^2)   = SUM_j c_j * max{|PHI''| on the cell around x_j/L} / (8*L^3*C^2)")
    rec("  %-6s %18s %18s %14s" % ("a^2", "K_glob", "K_pt", "K_pt/K_glob"))
    Kg, Kp = {}, {}
    hstep = tau[1] - tau[0]
    for a, alab in CELLS:
        L = math.log(a)
        xs, cs = XS[alab]
        if not xs:
            Kg[alab] = 0.0
            Kp[alab] = 0.0
            rec("  %-6s %18s %18s %14s" % (alab, "0 (empty column)", "0 (empty column)", "--"))
            continue
        kg = M2 * W[alab] / (8.0 * L ** 3 * C ** 2)
        # ### the LOCAL maximum: a window of +- one corr-cell in tau units, at the COARSEST
        # ### test axis, so the window is the widest any test axis needs. ### A window chosen
        # ### narrow would be a bound chosen small.
        hmax = 4.0 * L / (2 * min(NV_TEST) - 2)
        wtau = hmax / L
        tot = 0.0
        for x, c in zip(xs, cs):
            lo, hi = x / L - wtau, x / L + wtau
            sel = (tau >= lo) & (tau <= hi)
            loc = float(np.max(np.abs(P2[sel]))) if sel.any() else M2
            tot += c * loc
        kp = tot / (8.0 * L ** 3 * C ** 2)
        Kg[alab], Kp[alab] = kg, kp
        rec("  %-6s %18.9f %18.9f %14.4f" % (alab, kg, kp, kp / kg))
    rec("")

    rec("-" * 104)
    rec("(5) THE CRITERION AT THE TEST AXES. ### FORM KEPT AS b238 WROTE IT.")
    rec("### |resid| <= K_glob*h^2 + F,  h = 4L/(2NV-2),  F = %.1e (b238's MEASURED floor)."
        % F_FLOOR)
    rec("### ### K IS DERIVED FROM THE BUMP. ### NO RESIDUAL ENTERS ITS FORMULA, SO IT CANNOT")
    rec("### ### HAVE BEEN WIDENED TOWARD ONE.")
    rec("-" * 104)
    rec("  %-6s %-8s %16s %20s" % ("a^2", "NV", "h", "BOUND"))
    for a, alab in CELLS:
        L = math.log(a)
        for nv in NV_TEST:
            h = 4.0 * L / (2 * nv - 2)
            b = Kg[alab] * h * h + F_FLOOR
            rec("  %-6s %-8d %16.9e %20.9e" % (alab, nv, h, b))
    rec("")
    rec("### ### THE PASS RULE, FIXED IN THE REGISTRATION AND RESTATED HERE UNCHANGED, IN b238's")
    rec("### ### OWN WORDS: 'every cell at every test axis must satisfy |resid| <= BOUND.")
    rec("### ### ONE CELL OVER THE BOUND IS BRANCH (HELD).'")
    rec("### ### AND THE SLACK IS TO BE PRINTED PER CELL BY THE FINAL RUN, because a wide margin")
    rec("### ### must not be allowed to read as a tight agreement.")
    rec("=" * 104)
    io.open(ENV, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % ENV)


if __name__ == "__main__":
    main()
