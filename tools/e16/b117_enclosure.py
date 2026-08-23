# -*- coding: utf-8 -*-
"""b117 -- THE ENCLOSURE INSTRUMENT.

Rigorous interval arithmetic (mpmath.iv, every rounding OUTWARD) on the
scale-average of the open step:

    I(L) := int_0^2 PhiK(sigma) Psi(L*sigma) d sigma
    dN/dL = -(2/L^2) * L * I(L)   [equivalently -(2/L^2) int_0^{2L} PhiK(u/L) Psi(u) du]

THE GRADE HAZARD, carried from the registration and repeated here because it
governs the verdict: interval arithmetic over the QUADRATURE yields a theorem
about the quadrature's value GIVEN ITS INPUTS. The inputs are Psi's sampled
values, from a floating-point prolate quadrature and a floating-point epsilon
integral, for which THE RECORD HOLDS NO RIGOROUS ERROR BOUND. This script
therefore produces (i) a rigorous enclosure conditional on the samples, and
(ii) a SEPARATELY MEASURED refinement floor, and reports the margin between
them. It does not call the result certified-numerics unless (i) and (ii)
together close the shortfall, and they do not.

THE GATE, applied to this instrument itself before any new claim:
reproduce int_0^2 K = 1/2, int_0^2 PhiK = 0, PhiK's single crossover, and the
sign of dN/dL at the banked cells.
"""
import math, sys
import numpy as np
from mpmath import iv, mp, mpf

sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38
import qeps_layer as Q

# Psi is rebuilt here rather than imported: the prior modules run their own
# main() at import, and an enclosure instrument must not carry another act's
# side effects into its own run.
RHO_MAX = 48.001


def psi_on(ug, n_rho, sig):
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(B38.TRIPLE[1][0])
    nm = min(NMODE, xi.shape[1])
    A = np.zeros((nm, len(ug)))
    for n in range(nm):
        f = xi[:, n]
        for i, u in enumerate(ug):
            lamd = math.exp(u)
            fy = np.interp(lamd * x, x, f, left=0.0, right=0.0)
            A[n, i] = math.sqrt(lamd) * 0.5 * float((w * f * fy).sum())
    rr = np.exp(np.linspace(1e-4, math.log(RHO_MAX), n_rho))
    ee = B38.per_mode_eps_grids(rr)
    E = np.zeros((nm, len(ug)))
    for n in range(nm):
        E[n] = np.interp(np.exp(ug), rr, ee[n])
    return (A[0::2].sum(0) - sig * A.sum(0)) - (E[0::2].sum(0) - sig * E.sum(0))

iv.dps = 40
mp.dps = 40

NMODE = B38.TRIPLE[1][1]
UMAX = 2.0 * math.log(math.sqrt(48.001))
CELLS = [2, 3, 4, 8, 9, 12, 16, 24, 48]


def ivq(x):
    """A point float as a tight interval (the float itself is exact in binary)."""
    return iv.mpf(float(x))


def trap_iv(y, x):
    """Trapezoid rule in INTERVAL arithmetic: every add/mul rounds outward."""
    tot = iv.mpf(0)
    for i in range(len(x) - 1):
        h = ivq(x[i + 1]) - ivq(x[i])
        tot = tot + h * (y[i] + y[i + 1]) / iv.mpf(2)
    return tot


def build_K(n=2001):
    a0 = math.sqrt(12)
    v, w2, corr, vc, L0 = B38.family(a0)
    sg = np.linspace(0.0, 2.0, n)
    K = L0 * np.interp(L0 * sg, vc, corr)
    Phi = np.gradient(sg * K, sg)
    return sg, K, Phi


def main():
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(B38.EPS_NQ)
    t = lam2 / (1 - lam2) * xi1 ** 2
    s = t[:NMODE] / float(t[:NMODE].sum())
    sig = float(s[0::2].sum())

    sg, K, Phi = build_K()
    Kiv = [ivq(z) for z in K]
    Piv = [ivq(z) for z in Phi]

    print("=" * 78)
    print("b117 -- THE ENCLOSURE INSTRUMENT (mpmath.iv, dps=%d, all rounding outward)" % iv.dps)
    print("=" * 78)

    # ---------------- THE GATE ----------------
    print("\n--- THE GATE ON THIS INSTRUMENT (coarse features reproduced first) ---")
    IK = trap_iv(Kiv, sg)
    IP = trap_iv(Piv, sg)
    print("  int_0^2 K      enclosure = [%.12f, %.12f]   target 1/2" % (IK.a, IK.b))
    g1 = (IK.a <= 0.5 <= IK.b) or abs(float(IK.mid) - 0.5) < 1e-9
    print("     contains 1/2 (or agrees to 1e-9): %s" % g1)
    print("  int_0^2 PhiK   enclosure = [%.3e, %.3e]   target 0" % (IP.a, IP.b))
    g2 = (IP.a <= 0 <= IP.b) or abs(float(IP.mid)) < 1e-9
    print("     contains 0 (or agrees to 1e-9): %s" % g2)
    cross = [i for i in range(len(Phi) - 1) if Phi[i] * Phi[i + 1] < 0]
    print("  PhiK sign changes: %d  at sigma = %s   (target: exactly 1)"
          % (len(cross), [round(float(sg[i]), 4) for i in cross]))
    # NOTE: PhiK's tail is EXACTLY zero (the bump's support ends inside the grid,
    # so sigma*K vanishes identically there). The gate therefore asks the right
    # question -- positive before the crossover, never positive after it -- rather
    # than a strict endpoint comparison, which a legitimate exact zero would fail.
    j = cross[0] if cross else 0
    before_pos = bool((Phi[:j + 1] >= 0).all() and Phi[0] > 0)
    after_nonpos = bool((Phi[j + 1:] <= 0).all() and (Phi[j + 1:] < 0).any())
    print("  PhiK >= 0 before the crossover and > 0 at 0 : %s" % before_pos)
    print("  PhiK <= 0 after it, strictly negative somewhere : %s" % after_nonpos)
    print("  (PhiK's tail is EXACTLY 0 past the bump's support -- stated, not hidden)")
    g3 = (len(cross) == 1 and before_pos and after_nonpos)
    if not (g1 and g2 and g3):
        print("\n  *** GATE FAILED -- HALT. No new claim is made. ***")
        return
    print("  *** GATE PASSES on the coarse features. ***")

    # ---------------- THE FLOOR, MEASURED ----------------
    print("\n--- THE REFINEMENT-STABLE SCALE (the floor), MEASURED not assumed ---")
    ug = np.linspace(0.0, UMAX, 400)
    prev, worst = None, 0.0
    for nr in (400, 800, 1600, 3200):
        psi_n = psi_on(ug, nr, sig)
        if prev is not None:
            worst = max(worst, float(np.abs(psi_n - prev).max()))
        prev = psi_n
    FLOOR = worst
    print("  max |Psi(N_rho) - Psi(2*N_rho)| over 400->3200 : %.3e" % FLOOR)
    print("  ### THE REFINEMENT-STABLE SCALE FOR Psi IS %.1e. Every Psi claim below" % FLOOR)
    print("      states this scale, per the act's scale law.")
    psi_ref = prev

    absP = trap_iv([abs(z) for z in Piv], sg)
    print("  int_0^2 |PhiK| enclosure = [%.9f, %.9f]" % (absP.a, absP.b))
    print("  => a uniform perturbation of Psi by the floor moves I(L) by at most")
    print("     floor * int|PhiK| = %.3e" % (FLOOR * float(absP.b)))
    PERT = FLOOR * float(absP.b)

    # ---------------- P1: THE ENCLOSURE ----------------
    print("\n--- P1: THE ENCLOSURE OF I(L) ACROSS THE LICENSED RANGE ---")
    print("%6s %9s %26s %13s %11s" % ("a^2", "L", "I(L) enclosure", "width", "margin/floor"))
    rows = []
    for a2 in CELLS:
        L = math.log(math.sqrt(a2))
        uq = L * sg
        psiq = np.interp(uq, ug, psi_ref, right=psi_ref[-1])
        yi = [Piv[i] * ivq(psiq[i]) for i in range(len(sg))]
        I = trap_iv(yi, sg)
        lo, hi = float(I.a), float(I.b)
        width = hi - lo
        margin = min(abs(lo), abs(hi)) if lo * hi > 0 else 0.0
        rows.append((a2, L, lo, hi, margin))
        print("%6d %9.6f  [%+.9f, %+.9f] %13s %11.1f"
              % (a2, L, lo, hi, ("%.1e" % width if width > 0 else "<1e-30"),
                 (margin / PERT) if PERT > 0 else float('inf')))

    allneg = all(hi < 0 for _, _, lo, hi, _ in rows)
    allpos = all(lo > 0 for _, _, lo, hi, _ in rows)
    minmargin = min(m for *_, m in rows)
    print("\n  enclosure strictly NEGATIVE at every cell: %s" % allneg)
    print("  enclosure strictly POSITIVE at every cell: %s" % allpos)
    print("  smallest margin to zero: %.6f ; floor-induced uncertainty: %.3e"
          % (minmargin, PERT))
    print("  ### MARGIN EXCEEDS THE FLOOR BY A FACTOR OF %.0f" % (minmargin / PERT))
    print("  and dN/dL = -(2/L) * I(L), so I(L) < 0 at every cell means dN/dL > 0.")

    # ---------------- P2: THE TREND ----------------
    # ---------------- P1b: A DENSE SWEEP OF L ----------------
    print("\n--- P1b: A DENSE SWEEP OF L ACROSS THE LICENSED RANGE ---")
    Ls = np.linspace(math.log(math.sqrt(2)), math.log(math.sqrt(48.001)), 60)
    worst_hi, worst_L, allneg2 = -1e9, None, True
    for L in Ls:
        pq = np.interp(L * sg, ug, psi_ref, right=psi_ref[-1])
        I = trap_iv([Piv[i] * ivq(pq[i]) for i in range(len(sg))], sg)
        hi = float(I.b)
        if hi >= 0:
            allneg2 = False
        if hi > worst_hi:
            worst_hi, worst_L = hi, L
    print("  60 values of L spanning a^2 = 2 to 48.001")
    print("  enclosure upper bound NEGATIVE at every sampled L: %s" % allneg2)
    print("  least negative upper bound: %+.9f at L = %.6f (a^2 = %.3f)"
          % (worst_hi, worst_L, math.exp(2 * worst_L)))
    print("  margin there / floor-induced uncertainty: %.0f" % (abs(worst_hi) / PERT))
    print("  *** SAMPLED, NOT EXHAUSTIVE: 60 points do not certify the continuum,")
    print("      and the verdict says so. ***")

    print("\n--- P2: THE GROSS RISE, ENCLOSED ---")
    lo_end = ivq(psi_ref[-1]) - ivq(psi_ref[0])
    print("  Psi(umax) - Psi(0) enclosure = [%+.9f, %+.9f]" % (lo_end.a, lo_end.b))
    print("  bounded below away from zero: %s (by %.6f, floor %.1e)"
          % (float(lo_end.a) > 0, float(lo_end.a), FLOOR))
    inc = all(psi_ref[i] <= psi_ref[i + 1] for i in range(len(psi_ref) - 1))
    print("  ### IS Psi MONOTONE INCREASING POINTWISE? %s" % inc)
    desc = [(ug[i], psi_ref[i] - psi_ref[i + 1]) for i in range(len(psi_ref) - 1)
            if psi_ref[i] > psi_ref[i + 1]]
    big = [(u, d) for u, d in desc if d > FLOOR]
    print("  descending steps at all: %d ; ABOVE THE FLOOR: %d" % (len(desc), len(big)))
    if big:
        lo_u = min(u for u, _ in big); hi_u = max(u for u, _ in big)
        print("  ### THE FAILURE WINDOW, NAMED: u in [%.4f, %.4f]" % (lo_u, hi_u))
        print("      largest above-floor descent: %.6f at u = %.4f"
              % (max(d for _, d in big), [u for u, d in big if d == max(dd for _, dd in big)][0]))
        insid = [u for u, _ in big if u < 0.75]
        print("      of %d above-floor descents, %d lie at u < 0.75" % (len(big), len(insid)))


main()
