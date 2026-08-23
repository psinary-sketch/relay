# -*- coding: utf-8 -*-
"""b126 -- THE LOCALIZATION ACT: the two-factor freeze, the per-mode
attribution, and the cliff test.

DIAGNOSTIC ONLY. Nothing is repaired. The evaluation used throughout is THE
INCUMBENT (np.interp with zero-fill), because the quantity being decomposed is
the incumbent's own 4.361e-01 excursion.

THE TWO KNOBS, independent:
  eval_NQ   -- which quadrature the eigenvectors and the A_n sum come from
  wt_NQ     -- which quadrature the mass weights (sigma_even) come from
  baseline  : eval=NQ, wt=NQ      (b121's configuration)
  F1        : eval=NQ, wt=REF     (weights frozen)
  F2        : eval=REF, wt=NQ     (evaluation frozen)
"""
import hashlib, math, sys, functools
import numpy as np

print = functools.partial(print, flush=True)
sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38
import qeps_layer as Q

UMAX = 2.0 * math.log(math.sqrt(48.001))
RHO_MAX = 48.001
NMODE = B38.TRIPLE[1][1]
REF = 700
NQS = (600, 800, 900, 1100)
_cache = {}


def layer(NQ):
    if NQ not in _cache:
        _cache[NQ] = Q.layer(NQ)
    return _cache[NQ]


def sigma_of(NQ, nm=NMODE):
    x, w, lam, lam2, xi, xi1, an, dan = layer(NQ)
    tn = lam2 / (1 - lam2) * xi1 ** 2
    s = tn[:nm] / float(tn[:nm].sum())
    return float(s[0::2].sum()), lam2[:nm], tn[:nm]


def A_modes(ug, NQ, nm=NMODE):
    """The INCUMBENT evaluation: np.interp with zero-fill. Unchanged."""
    x, w, lam, lam2, xi, xi1, an, dan = layer(NQ)
    out = np.zeros((nm, len(ug)))
    for n in range(nm):
        f = xi[:, n]
        for i, u in enumerate(ug):
            ld = math.exp(u)
            fy = np.interp(ld * x, x, f, left=0.0, right=0.0)
            out[n, i] = math.sqrt(ld) * 0.5 * float((w * f * fy).sum())
    return out


def E_modes(ug, nm=NMODE, n_rho=800):
    rr = np.exp(np.linspace(1e-4, math.log(RHO_MAX), n_rho))
    ee = B38.per_mode_eps_grids(rr)
    E = np.zeros((nm, len(ug)))
    for n in range(min(nm, ee.shape[0])):
        E[n] = np.interp(np.exp(ug), rr, ee[n])
    return E


def psi_from(A, E, sig):
    return (A[0::2].sum(0) - sig * A.sum(0)) - (E[0::2].sum(0) - sig * E.sum(0))


def main():
    ug = np.linspace(0.0, UMAX, 200)

    # ---------- the reference run, md5-banked ----------
    print("=" * 78)
    print("b126 -- THE LOCALIZATION ACT   (diagnostic only; incumbent evaluation)")
    print("=" * 78)
    x, w, lam, lam2, xi, xi1, an, dan = layer(REF)
    sig_ref, lam2_ref, tn_ref = sigma_of(REF)
    print("\n--- THE REFERENCE RUN (NQ = %d), md5-banked ---" % REF)
    for nm_, arr in (("x", x), ("w", w), ("lam2[0:11]", lam2[:NMODE]),
                     ("xi", xi[:, :NMODE]), ("xi1[0:11]", xi1[:NMODE])):
        print("  %-12s md5 %s" % (nm_, hashlib.md5(np.ascontiguousarray(arr)).hexdigest()))
    print("  sigma_even   %.12f" % sig_ref)
    print("  (deterministic layer: leggauss + eigh; NO random draw, NO seed)")

    A_ref = A_modes(ug, REF)
    E = E_modes(ug)
    psi_ref = psi_from(A_ref, E, sig_ref)
    print("  Psi(0) = %+.9f   (known answer -1.165002987)" % psi_ref[0])

    # ---------- COMPONENT 1: the freezes ----------
    print("\n--- COMPONENT 1 (P1): THE TWO-FACTOR FREEZE ---")
    print("%6s %14s %14s %14s %14s" %
          ("NQ", "baseline", "F1 wts frozen", "F2 eval frozen", "interaction"))
    rows = []
    A_cache = {REF: A_ref}
    for NQ in NQS:
        A_cache[NQ] = A_modes(ug, NQ)
        sig_nq, _, _ = sigma_of(NQ)
        base = float(np.abs(psi_from(A_cache[NQ], E, sig_nq) - psi_ref).max())
        f1 = float(np.abs(psi_from(A_cache[NQ], E, sig_ref) - psi_ref).max())
        f2 = float(np.abs(psi_from(A_ref, E, sig_nq) - psi_ref).max())
        inter = base - (f1 + f2)
        rows.append((NQ, base, f1, f2, inter))
        print("%6d %14.6e %14.6e %14.6e %+14.6e" % (NQ, base, f1, f2, inter))
    B = max(r[1] for r in rows); F1 = max(r[2] for r in rows); F2 = max(r[3] for r in rows)
    print("\n  worst baseline excursion : %.6e   (b121 recorded 4.361e-01)" % B)
    print("  worst F1 share (evaluation, weights frozen) : %.6e  = %.1f%% of baseline"
          % (F1, 100 * F1 / B))
    print("  worst F2 share (weights, evaluation frozen) : %.6e  = %.1f%% of baseline"
          % (F2, 100 * F2 / B))
    print("  ### THE SPLIT IS %s" % ("EVALUATION-DOMINATED" if F1 > 10 * F2
                                     else ("WEIGHT-DOMINATED" if F2 > 10 * F1 else "MIXED")))
    print("  sum reconciliation: F1+F2 = %.6e against baseline %.6e ; interaction %+.3e"
          % (F1 + F2, B, B - F1 - F2))

    # ---------- COMPONENT 2a: the attribution table ----------
    print("\n--- COMPONENT 2 (P2): PER-MODE ATTRIBUTION ACROSS NQ ---")
    print("%4s %14s %14s %16s %10s" %
          ("n", "lam2", "1/(1-lam2)", "max|dA_n|", "share%"))
    contrib = []
    for n in range(NMODE):
        d = max(float(np.abs(A_cache[NQ][n] - A_ref[n]).max()) for NQ in NQS)
        contrib.append(d)
    tot = sum(contrib)
    for n in range(NMODE):
        l2 = float(lam2_ref[n])
        print("%4d %14.6e %14.6e %16.6e %10.2f" %
              (n, l2, 1.0 / (1.0 - l2), contrib[n], 100 * contrib[n] / tot))
    top = int(np.argmax(contrib))
    print("\n  largest contributor: mode %d (lam2 = %.3e)" % (top, lam2_ref[top]))
    head = sum(contrib[:3]) / tot
    tail = sum(contrib[7:]) / tot
    print("  share from modes 0-2 (largest lam2)  : %.1f%%" % (100 * head))
    print("  share from modes 7-10 (floor tail)   : %.1f%%" % (100 * tail))
    print("  ### H1 signature (largest modes, scaling with 1/(1-lam2)): %s"
          % ("MATCHES" if head > 0.6 else "does NOT match"))
    print("  ### H2 signature (floor tail):                            %s"
          % ("MATCHES" if tail > 0.6 else "does NOT match"))

    # ---------- COMPONENT 2b: the cliff test ----------
    print("\n--- COMPONENT 2 (P3): THE CLIFF TEST (hard truncation) ---")
    print("%7s %16s %18s %16s" % ("NMODE", "excursion", "Psi(0) truncated", "known answer"))
    for nm in (NMODE, 7, 6, 3):
        sg_r, l2_r, _ = sigma_of(REF, nm)
        Ar = A_modes(ug, REF, nm)
        Er = E_modes(ug, nm)
        pr = psi_from(Ar, Er, sg_r)
        exc = 0.0
        for NQ in NQS:
            sg_n, _, _ = sigma_of(NQ, nm)
            exc = max(exc, float(np.abs(psi_from(A_modes(ug, NQ, nm), Er, sg_n) - pr).max()))
        n_even = len(range(0, nm, 2))
        known = n_even - sg_r * nm
        print("%7d %16.6e %18.9f %16.9f" % (nm, exc, pr[0], known))
    print("  ### H2's removal signature: the excursion %s under cliff truncation."
          % ("COLLAPSES" if False else "is to be read from the column above"))


main()
