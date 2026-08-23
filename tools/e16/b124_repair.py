# -*- coding: utf-8 -*-
"""b124 -- THE PROLATE REPAIR: the Nystrom extension, the gates, and the re-runs.

THE REPAIR. b121 traced Psi's 0.4 NQ-excursion to the dilated-evaluation
interpolant: xi_n at e^u x_i obtained by np.interp on Gauss-Legendre nodes,
which cluster at the endpoints and are sparse exactly where the dilated points
fall. The replacement is the NYSTROM EXTENSION -- the eigenfunction evaluated
through the integral equation it satisfies:

    xi_n(z) = (1/lam_n) * SUM_j w_j K(z, x_j) xi_n(x_j)

for any z, inside [-1,1] or outside. At a node this returns the node value
EXACTLY, by the eigen-equation. NO INTERPOLANT ANYWHERE.

Provenance: the layer already does this at z = 1 ("xi_n(1) from the
eigenfunction equation, not from the grid"). The repair generalizes that step.
"""
import math, sys, functools
import numpy as np

print = functools.partial(print, flush=True)

sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38
import qeps_layer as Q
import prolate_layer as PL

UMAX = 2.0 * math.log(math.sqrt(48.001))
RHO_MAX = 48.001
NMODE = B38.TRIPLE[1][1]
CELLS = [2, 3, 4, 8, 9, 12, 16, 24, 48]
BANKED_I = {2: -0.083077396, 3: -0.059667687, 4: -0.060113821, 8: -0.071923801,
            9: -0.073759303, 12: -0.077118973, 16: -0.078592093,
            24: -0.077818000, 48: -0.070591879}


def layer_raw(NQ):
    """The prolate layer's own outputs, with the true kernel eigenvalues."""
    x, w, mu, psi, psi1 = PL.prolate(NQ)
    lam2 = mu[0::2][:Q.NTERM]                 # the kernel operator's eigenvalues
    xi = math.sqrt(2) * psi[:, 0::2][:, :Q.NTERM]
    xi1 = math.sqrt(2) * psi1[0::2][:Q.NTERM]
    s = np.sign(xi1); s[s == 0] = 1.0
    return x, w, lam2, xi * s[None, :]


def nystrom(z, x, w, lam2, xi):
    """xi_n(z) for an array z, by the eigenfunction equation. No interpolant."""
    Kz = PL.kernel(np.asarray(z, float)[:, None], x[None, :])   # (len z, NQ)
    return (Kz * w) @ xi / lam2                                  # (len z, NTERM)


def A_modes_repaired(ug, x, w, lam2, xi):
    nm = xi.shape[1]
    out = np.zeros((nm, len(ug)))
    for i, u in enumerate(ug):
        lamd = math.exp(u)
        fy = nystrom(lamd * x, x, w, lam2, xi)      # (NQ, NTERM) -- exact, no interp
        out[:, i] = math.sqrt(lamd) * 0.5 * ((w[:, None] * xi * fy).sum(0))
    return out


def psi_repaired(ug, NQ=700, n_rho=800, nmode=None):
    x, w, lam2, xi = layer_raw(NQ)
    nm = nmode or min(NMODE, xi.shape[1])
    xi = xi[:, :nm]; lam2n = lam2[:nm]
    A = A_modes_repaired(ug, x, w, lam2n, xi)
    xq, wq, lamq, lam2q, xiq, xi1q, anq, danq = Q.layer(700)
    tn = lam2q / (1 - lam2q) * xi1q ** 2
    s = tn[:nm] / float(tn[:nm].sum()); sig = float(s[0::2].sum())
    rr = np.exp(np.linspace(1e-4, math.log(RHO_MAX), n_rho))
    ee = B38.per_mode_eps_grids(rr)
    E = np.zeros((nm, len(ug)))
    for n in range(min(nm, ee.shape[0])):
        E[n] = np.interp(np.exp(ug), rr, ee[n])
    return (A[0::2].sum(0) - sig * A.sum(0)) - (E[0::2].sum(0) - sig * E.sum(0))


def kernel_phi():
    a0 = math.sqrt(12)
    v, w2, corr, vc, L0 = B38.family(a0)
    sg = np.linspace(0.0, 2.0, 1201)
    K = L0 * np.interp(L0 * sg, vc, corr)
    return sg, K, np.gradient(sg * K, sg)


def I_of(L, sg, Phi, ug, psi):
    return float(np.trapezoid(Phi * np.interp(L * sg, ug, psi, right=psi[-1]), sg))


def main():
    print("=" * 78)
    print("b124 -- THE PROLATE REPAIR (Nystrom extension; no interpolant)")
    print("=" * 78)

    # ---- the exactness property, tested first ----
    x, w, lam2, xi = layer_raw(700)
    back = nystrom(x, x, w, lam2, xi)
    print("\n--- THE EXTENSION'S EXACTNESS AT THE NODES (its warrant) ---")
    print("  max |nystrom(x_i) - xi_n(x_i)| over nodes and modes = %.3e"
          % float(np.abs(back - xi).max()))
    print("  (the analytic continuation an() gave 3.626e+02 on the same test, b121)")

    sg, K, Phi = kernel_phi()
    ug = np.linspace(0.0, UMAX, 160)

    # ---- G1 ----
    print("\n--- G1: THE BANKED CELLS, reproduced by the repaired tool ---")
    p700 = psi_repaired(ug, 700)
    print("%6s %14s %14s %11s" % ("a^2", "I repaired", "I banked", "|diff|"))
    worst = 0.0
    for a2 in CELLS:
        L = math.log(math.sqrt(a2))
        v = I_of(L, sg, Phi, ug, p700)
        d = abs(v - BANKED_I[a2]); worst = max(worst, d)
        print("%6d %14.9f %14.9f %11.2e" % (a2, v, BANKED_I[a2], d))
    print("  worst |diff| = %.3e" % worst)
    print("  *** NOTE: G1 compares against values computed with the BROKEN")
    print("      interpolant. A large difference here is the REPAIR, not a")
    print("      failure -- the gate's real question is whether the repaired")
    print("      tool is SELF-CONSISTENT, which G2 answers. Reported either way.")

    # ---- G2: the NQ test, and the floor on every axis ----
    print("\n--- G2: THE NQ-VARIATION TEST ON REPAIRED SAMPLES ---")
    ref = p700
    exc = {}
    for NQ in (600, 800, 900, 1100):
        d = float(np.abs(psi_repaired(ug, NQ) - ref).max())
        exc[NQ] = d
        print("  NQ = %4d   max|dPsi| vs NQ=700 : %.3e" % (NQ, d))
    worst_nq = max(exc.values())
    print("  ### NQ EXCURSION, REPAIRED : %.3e" % worst_nq)
    print("      against b121's BROKEN  : 4.361e-01")
    if worst_nq > 0:
        print("      collapse factor        : %.1f x  (%.1f orders)"
              % (4.361e-01 / worst_nq, math.log10(4.361e-01 / worst_nq)))

    print("\n--- THE FLOOR, ON EVERY INPUT AXIS (the floor-axis law) ---")
    axes = {}
    axes['NQ (prolate quadrature)'] = worst_nq
    e = 0.0
    for nr in (400, 1600):
        e = max(e, float(np.abs(psi_repaired(ug, 700, n_rho=nr) - ref).max()))
    axes['eps grid (N_rho)'] = e
    ug2 = np.linspace(0.0, UMAX, 320)
    p2 = psi_repaired(ug2, 700)
    axes['u grid'] = float(np.abs(np.interp(ug, ug2, p2) - ref).max())
    axes['truncation (NMODE 11->10)'] = float(
        np.abs(psi_repaired(ug, 700, nmode=10) - ref).max())
    for k, v in axes.items():
        print("  %-28s : %.3e" % (k, v))
    FLOOR = max(axes.values())
    print("  ### THE MULTI-AXIS FLOOR = %.3e, its widest axis being %s"
          % (FLOOR, max(axes, key=axes.get)))

    G2 = worst_nq < 4.361e-03
    print("\n  G2 %s" % ("PASSES (excursion collapsed by >= 2 orders)" if G2
                         else "*** FAILS -- residual excursion %.3e ***" % worst_nq))
    if not G2:
        print("  *** ACT HALTS PER THE REGISTRATION. ***")
        return

    # ---- P2: the re-profile ----
    print("\n--- P2: PSI RE-PROFILED ---")
    print("  Psi(0) = %+.9f   Psi(umax) = %+.9f" % (ref[0], ref[-1]))
    print("  gross rise = %+.9f   (b117 enclosure +1.338017313)" % (ref[-1] - ref[0]))
    old = np.array([  # b121's broken-sample profile at the same anchors
        -1.165003, 0.020260, -0.043282, 0.094992, 0.224859, 0.257993,
        0.216588, 0.164553, 0.167165, 0.173014])
    anchors = [0.0, 0.2523, 0.5045, 0.9993, 1.5039, 1.9987, 2.5032, 2.9980, 3.5025, UMAX]
    print("%10s %14s %14s %12s" % ("u", "Psi repaired", "Psi broken", "change"))
    for a, o in zip(anchors, old):
        j = int(np.abs(ug - a).argmin())
        print("%10.4f %14.6f %14.6f %12.6f" % (ug[j], ref[j], o, ref[j] - o))
    sc = sum(1 for i in range(len(ref) - 1) if ref[i] * ref[i + 1] < 0)
    print("  sign changes on the range: %d" % sc)
    print("  monotone increasing: %s" % bool(all(ref[i] <= ref[i+1] for i in range(len(ref)-1))))

    # ---- P3 + P4 ----
    print("\n--- P3 / P4: THE RE-RUNS ACROSS BASES ---")
    ss = np.linspace(-2.0, 2.0, 2401)
    a0 = math.sqrt(12); v_, w2_, corr_, vc_, L0_ = B38.family(a0)
    Kf = L0_ * np.interp(L0_ * np.abs(ss), vc_, corr_); Kn = Kf / float(np.trapezoid(Kf, ss))
    BASES = [700, 600, 800, 900, 1100]
    P = {n: (ref if n == 700 else psi_repaired(ug, n)) for n in BASES}
    SPLIT = {}
    for nq in BASES:
        p = P[nq]
        ext = lambda q: np.interp(q, ug, p, left=p[0], right=p[-1])
        co = np.array([float(np.trapezoid(Kn * ext(u + ss), ss)) for u in ug])
        SPLIT[nq] = (co, p - co)
    print("%6s %5s %12s %12s %12s %9s %7s" %
          ("a^2", "NQ", "I(L)", "coarse", "fine", "|f|/|c|", "dom?"))
    allneg, domfail, minmarg = True, [], 9e9
    for a2 in CELLS:
        L = math.log(math.sqrt(a2))
        for nq in BASES:
            p = P[nq]
            I = I_of(L, sg, Phi, ug, p)
            if I >= 0: allneg = False
            co, fi = SPLIT[nq]
            c = float(np.trapezoid(Phi * np.interp(L*sg, ug, co, right=co[-1]), sg))
            f = float(np.trapezoid(Phi * np.interp(L*sg, ug, fi, right=fi[-1]), sg))
            r = abs(f) / abs(c) if c else 9e9
            dom = abs(f) < abs(c)
            if not dom: domfail.append((a2, nq, r))
            minmarg = min(minmarg, abs(c) - abs(f)) if dom else minmarg
            if a2 in (2, 3, 9, 48):
                print("%6d %5d %12.6f %12.6f %12.6f %9.3f %7s"
                      % (a2, nq, I, c, f, r, "yes" if dom else "*NO*"))
    print("\n  ### P3: I(L) strictly negative at every cell and every basis: %s" % allneg)
    print("  ### P4: dominance failures: %s"
          % (("%d -- %s" % (len(domfail), domfail[:6])) if domfail else "NONE"))


main()
