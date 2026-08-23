# -*- coding: utf-8 -*-
"""b119 -- THE DOMINANCE ACT: the pre-registered coarse/fine split and its two bounds.

THE DECOMPOSITION IS FIXED IN data/b119_registration_2026-08-23.txt AND IS NOT
REVISITED HERE. Reading R1, as registered:

    psi_coarse(u) = int_{-2}^{+2} K(s) Psi(u + s) ds      [K normalized to mass 1]
    psi_fine(u)   = Psi(u) - psi_coarse(u)

Psi is extended outside the licensed range by its endpoint values -- the
convention fixed at registration, not chosen here.

THE GRADE, inherited from b117 and stated in every verdict this script feeds:
the interval arithmetic is rigorous over the quadrature and CONDITIONAL ON THE
SAMPLES. The prolate error bound remains the named blocker to any higher grade.

THE HAZARD FENCE: bounds derive, coherence narrates nothing. This script emits
bounds. It does not narrate.
"""
import math, sys
import numpy as np
from mpmath import iv, mp

sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38
import qeps_layer as Q

iv.dps = 40
mp.dps = 40

NMODE = B38.TRIPLE[1][1]
UMAX = 2.0 * math.log(math.sqrt(48.001))
RHO_MAX = 48.001
CELLS = [2, 3, 4, 8, 9, 12, 16, 24, 48]


def ivq(x):
    return iv.mpf(float(x))


def trap_iv(y, x):
    tot = iv.mpf(0)
    for i in range(len(x) - 1):
        h = ivq(x[i + 1]) - ivq(x[i])
        tot = tot + h * (y[i] + y[i + 1]) / iv.mpf(2)
    return tot


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


def main():
    x, w, lam, lam2, xi, xi1, an, dan = Q.layer(B38.EPS_NQ)
    tn = lam2 / (1 - lam2) * xi1 ** 2
    s = tn[:NMODE] / float(tn[:NMODE].sum())
    sig = float(s[0::2].sum())

    # ---- the channel kernel, and PhiK ----
    a0 = math.sqrt(12)
    v, w2, corr, vc, L0 = B38.family(a0)
    sg = np.linspace(0.0, 2.0, 2001)
    K = L0 * np.interp(L0 * sg, vc, corr)
    Phi = np.gradient(sg * K, sg)
    Piv = [ivq(z) for z in Phi]

    # K on the FULL symmetric support, normalized to mass 1 (its recorded mass)
    ss = np.linspace(-2.0, 2.0, 4001)
    Kfull = L0 * np.interp(L0 * np.abs(ss), vc, corr)
    mass = float(np.trapezoid(Kfull, ss))
    Kn = Kfull / mass

    print("=" * 78)
    print("b119 -- THE DOMINANCE ACT (mpmath.iv dps=%d, all rounding outward)" % iv.dps)
    print("=" * 78)
    print("\n--- THE CHANNEL KERNEL AT ITS RECORDED SCALE (no free parameter) ---")
    print("  K support |s| <= 2 ; recorded mass int K = %.9f ; normalized to 1" % mass)
    print("  (the registered reading R1: K applied in u at its OWN width)")

    # ---- the floor ----
    ug = np.linspace(0.0, UMAX, 400)
    prev, worst = None, 0.0
    for nr in (400, 800, 1600, 3200):
        pn = psi_on(ug, nr, sig)
        if prev is not None:
            worst = max(worst, float(np.abs(pn - prev).max()))
        prev = pn
    FLOOR = worst
    psi = prev
    print("\n--- THE REFINEMENT-STABLE SCALE (measured) ---")
    print("  floor = %.3e   (every Psi claim below states it)" % FLOOR)

    # ---- COMPONENT 1: THE SPLIT ----
    def psi_ext(uq):
        return np.interp(uq, ug, psi, left=psi[0], right=psi[-1])

    coarse = np.array([float(np.trapezoid(Kn * psi_ext(u + ss), ss)) for u in ug])
    fine = psi - coarse

    print("\n--- COMPONENT 1 (P1): THE SPLIT ---")
    print("%8s %12s %12s %12s" % ("u", "Psi", "psi_coarse", "psi_fine"))
    for uq in (0.0, 0.25, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, UMAX):
        j = int(np.abs(ug - uq).argmin())
        print("%8.4f %12.6f %12.6f %12.6f" % (ug[j], psi[j], coarse[j], fine[j]))
    rise_psi = psi[-1] - psi[0]
    rise_c = coarse[-1] - coarse[0]
    print("\n  Psi endpoint rise        = %+.9f   (b117 enclosure +1.338017313)" % rise_psi)
    print("  psi_coarse endpoint rise = %+.9f   (%.1f%% of Psi's, STATED not fitted)"
          % (rise_c, 100.0 * rise_c / rise_psi))
    print("  psi_fine  endpoint rise  = %+.9f" % (fine[-1] - fine[0]))
    print("  max|psi_fine| = %.6f ; max|psi_coarse| = %.6f" % (np.abs(fine).max(),
                                                               np.abs(coarse).max()))
    print("  FLOOR CONTRIBUTION, separated: a uniform Psi perturbation at the floor")
    print("    moves psi_coarse by at most %.3e (kernel mass 1) and psi_fine by at" % FLOOR)
    print("    most %.3e (the two together bounded by 2x the floor)." % (2 * FLOOR))

    # ---- COMPONENT 2: THE TWO BOUNDS ----
    print("\n--- COMPONENT 2 (P2, P3): THE TWO PAIRINGS, EVERY ROUNDING OUTWARD ---")
    print("%6s %9s %20s %20s %20s %9s" %
          ("a^2", "L", "coarse pairing", "fine pairing", "sum (= b117 I(L))", "dominates"))
    rows = []
    for a2 in CELLS:
        L = math.log(math.sqrt(a2))
        cq = np.interp(L * sg, ug, coarse, right=coarse[-1])
        fq = np.interp(L * sg, ug, fine, right=fine[-1])
        Ic = trap_iv([Piv[i] * ivq(cq[i]) for i in range(len(sg))], sg)
        If = trap_iv([Piv[i] * ivq(fq[i]) for i in range(len(sg))], sg)
        c_lo, c_hi = float(Ic.a), float(Ic.b)
        f_lo, f_hi = float(If.a), float(If.b)
        tot = c_lo + f_lo
        cmarg = min(abs(c_lo), abs(c_hi)) if c_lo * c_hi > 0 else 0.0
        fbound = max(abs(f_lo), abs(f_hi))
        dom = fbound < cmarg
        rows.append((a2, L, c_lo, c_hi, f_lo, f_hi, cmarg, fbound, dom, tot))
        print("%6d %9.6f  [%+.7f]  [%+.7f]  %+18.9f %9s"
              % (a2, L, c_lo, f_lo, tot, "YES" if dom else "NO"))

    print("\n  P2 -- the coarse pairing's sign across the cells:")
    allneg = all(r[3] < 0 for r in rows)
    allpos = all(r[2] > 0 for r in rows)
    print("    strictly NEGATIVE at every cell: %s" % allneg)
    print("    strictly POSITIVE at every cell: %s" % allpos)
    print("    smallest |coarse| margin = %.9f ; floor-induced move <= %.3e"
          % (min(r[6] for r in rows), FLOOR * 0.5009699))

    print("\n  P3 -- the remainder's bound against the trend's margin:")
    print("%6s %16s %16s %10s" % ("a^2", "|fine pairing|", "coarse margin", "ratio"))
    for a2, L, c_lo, c_hi, f_lo, f_hi, cmarg, fbound, dom, tot in rows:
        print("%6d %16.9f %16.9f %10.3f" % (a2, fbound, cmarg, fbound / cmarg))
    ndom = sum(1 for r in rows if r[8])
    print("\n  cells where the remainder IS dominated by the trend: %d of %d" % (ndom, len(rows)))

    # dense sweep for the failing window
    Ls = np.linspace(math.log(math.sqrt(2)), math.log(math.sqrt(48.001)), 60)
    fails = []
    for L in Ls:
        cq = np.interp(L * sg, ug, coarse, right=coarse[-1])
        fq = np.interp(L * sg, ug, fine, right=fine[-1])
        Ic = trap_iv([Piv[i] * ivq(cq[i]) for i in range(len(sg))], sg)
        If = trap_iv([Piv[i] * ivq(fq[i]) for i in range(len(sg))], sg)
        cm = min(abs(float(Ic.a)), abs(float(Ic.b))) if float(Ic.a) * float(Ic.b) > 0 else 0.0
        fb = max(abs(float(If.a)), abs(float(If.b)))
        if fb >= cm:
            fails.append((math.exp(2 * L), fb, cm))
    print("\n  DENSE SWEEP, 60 values of L:")
    print("    L values where the remainder is NOT dominated: %d of 60" % len(fails))
    if fails:
        print("    THE FAILING WINDOW, NAMED: a^2 in [%.3f, %.3f]"
              % (min(f[0] for f in fails), max(f[0] for f in fails)))
        w = max(fails, key=lambda f: f[1] / f[2] if f[2] > 0 else 1e18)
        print("    worst ratio |fine|/coarse-margin = %.3f at a^2 = %.3f"
              % (w[1] / w[2] if w[2] > 0 else float('inf'), w[0]))
    else:
        print("    NONE -- the remainder is dominated at every sampled L.")


main()
