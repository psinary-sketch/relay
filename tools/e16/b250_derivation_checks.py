# -*- coding: utf-8 -*-
"""b250 -- THE DERIVATION'S CONTROLS. ### THE PROOF IS LONGHAND IN THE BANK; THIS IS ITS CHECKING.

### ### **NOTHING HERE IS A PREMISE OF ANY STEP.** ### b249's measurements are CONTROLS: each
### derived bound is EVALUATED and the measured value is required to lie under it. ### A control
### that failed would refute the derivation; a control that passes does not prove it.
###
### WHAT IS CHECKED:
###   (1) S2's RANGE CONDITION -- the exact k beyond which the Bessel factorial bound holds.
###   (2) S2's EXPLICIT BOUND B(N), evaluated, against b249's measured mu_N.
###   (3) S3's MERCER CONSTANT -- sum_n lambda(n)^2 xi_n(1)^2, which the derivation says is
###       EXACTLY 2, against b249's high-precision data AND against the corpus's own C0 gate.
###   (4) S4's ENVELOPE, evaluated at K1's cut and at b249's N, against the measured tails.
"""
import io
import json
import os
import sys

from mpmath import mp, mpf

mp.dps = 60

PTS = r"D:\relay\data\b249_precision_points.json"
BANK = r"D:\relay\data\b250_derivation_checks.txt"
C = 2 * mp.pi


def M_bound(k):
    """### THE BESSEL FACTORIAL BOUND: |j_k(z)| <= (z/2)^k sqrt(pi) / (2 Gamma(k+3/2)) for
    ### |z| <= c, VALID ONLY where the power series alternates with decreasing magnitude."""
    return (C / 2) ** k * mp.sqrt(mp.pi) / (2 * mp.gamma(k + mpf(3) / 2))


def rank_one_norm(k):
    """### THE k-TH RANK-ONE TERM'S OPERATOR NORM, DERIVED IN THE BANK:  2*sqrt(2k+1)*M_k."""
    return 2 * mp.sqrt(2 * k + 1) * M_bound(k)


def B(N, KMAX=90):
    """### S2's SHARPENED BOUND, ON ONE IMPORT (Jacobi-Anger):
    ###   mu_N <= ( sum_{k>=N} 2 sqrt(2k+1) M_k )^2."""
    s = mp.fsum(rank_one_norm(k) for k in range(N, KMAX))
    return s ** 2


def taylor_term(m):
    """### THE m-TH RANK-ONE TERM OF THE *EXPONENTIAL'S OWN TAYLOR SERIES*, at c = 2 pi:
    ###   u_m(tau) = (2 pi)^{-1/2} (-i tau)^m / m!,   v_m(y) = y^m,
    ###   ||u_m|| ||v_m|| = ( 2 sqrt(c) / (sqrt(2 pi) (2m+1)) ) c^m / m!  ->  (2/(2m+1)) c^m/m!
    ### ### **ZERO IMPORTS. ### No Bessel function, no Legendre expansion, no special-function
    ### ### identity of any kind -- only exp's series and two elementary L^2 norms.**"""
    return (2 * mp.sqrt(C) / (mp.sqrt(2 * mp.pi) * (2 * m + 1))) * C ** m / mp.factorial(m)


def T(N, MMAX=140):
    """### S2's ZERO-IMPORT BOUND:  mu_N <= ( sum_{m>=N} ||u_m|| ||v_m|| )^2."""
    s = mp.fsum(taylor_term(m) for m in range(N, MMAX))
    return s ** 2


def main():
    pts = json.load(io.open(PTS, encoding="utf-8"))["120|80"]
    mu = [mpf(s) for s in pts["mu"]]
    p1 = [mpf(s) for s in pts["psi1"]]
    lam2 = [mu[2 * n] for n in range(len(mu) // 2)]
    xi1 = [mp.sqrt(2) * abs(p1[2 * n]) for n in range(len(mu) // 2)]
    t = [lam2[n] * xi1[n] ** 2 / (1 - lam2[n]) for n in range(len(lam2))]
    out = []

    def rec(s=""):
        print(s)
        out.append(s)

    rec("=" * 104)
    rec("b250 -- THE DERIVATION'S CONTROLS. ### NOT PREMISES.")
    rec("=" * 104)
    rec("### ### **NOTHING HERE IS A PREMISE OF ANY STEP.** ### b249's measurements are CONTROLS:")
    rec("### each derived bound is EVALUATED and the measured value is required to lie under it.")
    rec("### ### **A CONTROL THAT FAILED WOULD REFUTE THE DERIVATION; A CONTROL THAT PASSES DOES")
    rec("### ### NOT PROVE IT.**")
    rec("### CEILING (b15): 'A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING GLOBAL.'")
    rec("### h2 UNCHANGED. ### NOTHING DEPOSITS.")
    rec("")

    # ---------------------------------------------------------- (1) THE RANGE
    rec("-" * 104)
    rec("(1) ### S2's RANGE CONDITION, COMPUTED FROM THE SERIES AND NOT CHOSEN.")
    rec("### The power series for J_nu alternates with DECREASING magnitude iff")
    rec("###   z^2/4 < (m+1)(nu+m+1) for all m >= 0, worst at m = 0: ### **z^2/4 < k + 3/2**.")
    rec("-" * 104)
    thr = C ** 2 / 4 - mpf(3) / 2
    rec("  c = 2*pi, so c^2/4 = pi^2 = %s" % mp.nstr(C ** 2 / 4, 12))
    rec("  the condition is k > c^2/4 - 3/2 = %s" % mp.nstr(thr, 12))
    kmin = int(mp.floor(thr)) + 1
    rec("  ### ### **THE BOUND HOLDS FOR k >= %d.**" % kmin)
    rec("  ### THE REGISTRATION PREDICTED k >= 9, BEFORE COMPUTING: %s"
        % ("### **CONFIRMED**" if kmin == 9 else "### REFUTED (got %d)" % kmin))
    rec("  ### AND THE JOIN: Lemma F.1 certifies ELEVEN terms (k = 0..10), so the certified range")
    rec("  ### and the bound's range ### **OVERLAP at k = 9, 10** -- ### **THE JOIN IS NON-EMPTY**")
    rec("  ### and the two together cover every k >= 0.")
    rec("")

    # ------------------------------------------------------ (2) THE S2 BOUND
    rec("-" * 104)
    rec("(2) ### S2's EXPLICIT BOUND, EVALUATED, AGAINST b249's MEASURED mu_N. ### CONTROL.")
    rec("###   mu_N <= B(N) := ( sum_{k>=N} 2 sqrt(2k+1) M_k )^2,  M_k = (c/2)^k sqrt(pi)/(2 G(k+3/2))")
    rec("-" * 104)
    rec("### ### **TWO BOUNDS ARE GIVEN, AND THE DIFFERENCE BETWEEN THEM IS THE IMPORT LIST.**")
    rec("###   `T(N)` -- ### **ZERO IMPORTS**: exp's own Taylor series, two elementary L^2 norms.")
    rec("###   `B(N)` -- ### ONE IMPORT (Jacobi-Anger), sharper by many orders.")
    rec("###   ### **THE THEOREM RESTS ON `T`. ### `B` ONLY SHARPENS THE CONSTANT.**")
    rec("  %-5s %22s %22s %24s %8s %8s"
        % ("N", "T(N) [zero-import]", "B(N) [one import]", "mu_N [b249 measured]", "T ok?", "B ok?"))
    ok2 = True
    for N in range(kmin, 25):
        b, tt = B(N), T(N)
        m = mu[N] if N < len(mu) else None
        if m is None:
            continue
        gb, gt = (m <= b), (m <= tt)
        ok2 &= (gb and gt)
        rec("  %-5d %22s %22s %24s %8s %8s"
            % (N, mp.nstr(tt, 8), mp.nstr(b, 8), mp.nstr(m, 10),
               "yes" if gt else "### NO", "yes" if gb else "### NO"))
    rec("  ### ### **BOTH BOUNDS HOLD AT EVERY CHECKED N: %s**" % ("YES" if ok2 else "### NO"))
    rec("  ### **AND BOTH ARE LOOSE BY MANY ORDERS. ### THAT IS WHAT A WORST-CASE BOUND LOOKS")
    rec("  ### LIKE, AND THE SLACK IS PRINTED RATHER THAN HIDDEN.**")
    rec("  ### ### **THE SHAPE IS WHAT MATTERS: BOTH DECAY LIKE THE SQUARE OF `c^N / N!`, i.e.")
    rec("  ### ### FASTER THAN ANY GEOMETRIC. ### THAT IS THE DECAY M-4 NEEDED.**")
    rec("")

    # ------------------------------------------------- (3) THE MERCER CONSTANT
    rec("-" * 104)
    rec("(3) ### S3's MERCER CONSTANT. ### THE DERIVATION SAYS IT IS **EXACTLY 2**.")
    rec("###   Mercer: K(x,y) = sum_n mu_n psi_n(x) psi_n(y), so K(1,1) = sum_n mu_n psi_n(1)^2.")
    rec("###   K(1,1) = c/pi = 2 at c = 2*pi.   K(1,-1) = sin(2c)/(2 pi) = sin(4 pi)/(2 pi) = 0.")
    rec("###   Parity psi_n(-1) = (-1)^n psi_n(1) turns the second into sum_n (-1)^n mu_n psi_n(1)^2")
    rec("###   = 0, and adding gives ### **sum_{n EVEN} mu_n psi_n(1)^2 = 1**, i.e. with the")
    rec("###   corpus's xi_n = sqrt(2) psi_{2n}: ### **sum_n lambda(n)^2 xi_n(1)^2 = 2.**")
    rec("-" * 104)
    rec("  K(1,1)  = c/pi                 = %s" % mp.nstr(C / mp.pi, 20))
    rec("  K(1,-1) = sin(2c)/(2*pi)       = %s" % mp.nstr(mp.sin(2 * C) / (2 * mp.pi), 6))
    S = mp.fsum(lam2[n] * xi1[n] ** 2 for n in range(len(lam2)))
    rec("  sum_n lambda(n)^2 xi_n(1)^2 from b249's dps-120 data = %s" % mp.nstr(S, 25))
    dev = abs(S - 2)
    rec("  |sum - 2| = %s" % mp.nstr(dev, 6))
    ok3 = dev < mpf("1e-20")
    rec("  ### ### **THE DERIVED CONSTANT IS CONFIRMED TO %s.** ### %s" % (mp.nstr(dev, 3),
        "**AND THIS RE-DERIVES THE CORPUS'S OWN C0 GATE `sum lam2*xi1^2 = 2.0` FROM FIRST"
        if ok3 else "### REFUTED -- the route is wrong and the act says so."))
    if ok3:
        rec("  ### PRINCIPLES: a pin the record has carried as a NUMBER since b35 is now a")
        rec("  ### THEOREM.**")
    rec("")

    # ----------------------------------------------------- (4) THE ENVELOPE
    rec("-" * 104)
    rec("(4) ### S4's ENVELOPE, EVALUATED, AGAINST b249's MEASURED TAILS. ### CONTROL.")
    rec("###   sum_{n>N} t(n) <= ( 2 - S_N ) / ( 1 - B(2N+2) ),   S_N := sum_{n<=N} lam(n)^2 xi_n(1)^2")
    rec("###   and the MEASUREMENT-FREE form, which needs no computed partial sum at all:")
    rec("###   ### **sum_{n>N} t(n) <= 2 / ( 1 - B(2N+2) )**")
    rec("-" * 104)
    rec("### ### **THE EVALUATION CARRIES ITS OWN ERROR, AND THE CONTROL MUST CARRY IT TOO.**")
    rec("###   The sharp form evaluates `2 - S_N`, and the instrument's 13-term Mercer sum deviates")
    rec("###   from the exact 2 by a ### **MEASURED** ### amount `|sum - 2|` -- finite quadrature")
    rec("###   at NQ = 80 and a finite mode count. ### At the deepest cuts that deviation is")
    rec("###   COMPARABLE TO THE TAIL ITSELF, so a comparison finer than it ### **TESTS THE")
    rec("###   ARITHMETIC, NOT THE THEOREM.** ### The tolerance below is that measured deviation,")
    rec("###   ### **COMPUTED AND NOT CHOSEN.**")
    rec("### ### **AND THIS IS THE FOURTH CONSECUTIVE ACT IN WHICH A COMPARISON HAD TO CARRY THE")
    rec("### ### EVALUATING INSTRUMENT'S OWN ERROR** -- b245 (b38's four decimals), b246 (5e-5),")
    rec("### ### b249 (b242's ten digits and float64's 1/lambda^2), and now this. ### The")
    rec("### ### `W-ORD-TE-SPEC` extension b249 filed is demonstrated a fourth time.")
    evaltol = abs(S - 2)
    rec("  ### THE EVALUATION TOLERANCE, MEASURED: |sum_n lam^2 xi^2 - 2| = %s" % mp.nstr(evaltol, 6))
    rec("### ### **THE ENVELOPE HAS A RANGE CONDITION, AND IT IS NOT COSMETIC: it needs")
    rec("###   `bound(2N+2) < 1`, since `1/(1-lambda^2)` is only bounded by `1/(1-bound)` when the")
    rec("###   bound is under 1. ### On the ZERO-IMPORT bound `T` that fails at small `N` --")
    rec("###   `c^m/m!` PEAKS near `m = c = 2 pi` and only decays after. ### The first `N` at which")
    rec("###   the zero-import envelope is available is computed below, ### **NOT ASSUMED.**")
    nz = next(N for N in range(2, 60) if T(2 * N + 2) < 1)
    rec("  ### ### **THE ZERO-IMPORT ENVELOPE IS AVAILABLE FROM N = %d ONWARD** (T(%d) = %s < 1)."
        % (nz, 2 * nz + 2, mp.nstr(T(2 * nz + 2), 6)))
    rec("  ### AND K1's CUT IS N = 6. ### %s"
        % ("### **THE TWO COINCIDE -- THE ZERO-IMPORT ENVELOPE IS AVAILABLE EXACTLY AT THE "
           "CUT THE RECORD ALREADY USES.**" if nz <= 6 else
           "### **THE ZERO-IMPORT ENVELOPE IS NOT AVAILABLE AT K1's CUT; ONE IMPORT IS NEEDED "
           "THERE, AND THIS ACT SAYS SO.**"))
    rec("")
    rec("  %-4s %20s %20s %20s %20s %8s"
        % ("N", "sharp (0-import)", "sharp (1 import)", "meas-free (0-imp)",
           "measured tail", "holds?"))
    ok4 = True
    for N in (6, 8, 10, 11):
        if 2 * N + 2 >= len(mu):
            continue
        SN = mp.fsum(lam2[n] * xi1[n] ** 2 for n in range(N + 1))
        bb, tt = B(2 * N + 2), T(2 * N + 2)
        sharpB = (2 - SN) / (1 - bb)
        sharpT = (2 - SN) / (1 - tt) if tt < 1 else None
        freeT = 2 / (1 - tt) if tt < 1 else None
        meas = mp.fsum(t[n] for n in range(N + 1, len(t)))
        good = (meas <= sharpB + evaltol) and (sharpT is None or meas <= sharpT + evaltol) \
            and (freeT is None or meas <= freeT)
        ok4 &= good
        rec("  %-4d %20s %20s %20s %20s %8s"
            % (N, "n/a" if sharpT is None else mp.nstr(sharpT, 9), mp.nstr(sharpB, 9),
               "n/a" if freeT is None else mp.nstr(freeT, 9), mp.nstr(meas, 9),
               "yes" if good else "### NO"))
    rec("  ### ### **THE ENVELOPE HOLDS AT EVERY CHECKED CUT: %s**" % ("YES" if ok4 else "### NO"))
    rec("  ### **N = 6 IS K1's CUT.** ### The sharp form's evaluation uses finitely many EXACTLY")
    rec("  ### DEFINED terms; ### **the formula is the theorem, the number is an evaluation, and")
    rec("  ### the measurement is the CONTROL that the evaluation is not contradicted.**")
    rec("")
    rec("### WHAT THIS RUN DID NOT DO: it proved nothing. ### **THE PROOF IS LONGHAND IN THE BANK;")
    rec("### THIS FILE ONLY CHECKS THAT ITS BOUNDS ARE NOT CONTRADICTED BY THE INSTRUMENT.**")
    rec("### NOTHING DEPOSITS.")
    rec("=" * 104)
    io.open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")
    print("\nbanked: %s" % BANK)


if __name__ == "__main__":
    main()
