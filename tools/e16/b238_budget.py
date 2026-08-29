# -*- coding: utf-8 -*-
"""b238_budget.py -- EVERY ERROR SOURCE IN THE IMP-1 BENCH, PRICED BY MEASUREMENT.

### THE ORDER-OF-OPERATIONS LAW GOVERNS THIS ACT: this file MEASURES. It does not decide a
### criterion and it does not run the final verification. ### THE CRITERION IS DERIVED FROM
### THIS OUTPUT AND BANKED IN ITS OWN FILE BEFORE THE FINAL RUN EXISTS.

### THE INSTRUMENTS ARE IMPORTED UNMODIFIED. ### One local helper is defined here --
### `hhat_chunked` -- because `C.hhat` builds an NU x NV outer product and the reference grid
### would need ~3 GB. ### IT IS A MEMORY STRATEGY, NOT A DIFFERENT FORMULA, AND IT CARRIES A
### POSITIVE CONTROL AGAINST `C.hhat` AT A GRID WHERE BOTH FIT.

### THE FIVE SOURCES (clause b):
###   S1  uniform grid discretization -- order measured by refinement, PER TERM (A, P, PR, Z),
###       because "which term carries the error" is the question a summed residual hides.
###   S2  the bump's edge behaviour -- quadrature order on a KNOWN integral of the same species,
###       with an exact answer from mpmath.quad. ### THE POSITIVE CONTROL.
###   S3  interpolation -- np.interp's own error at the actual evaluation points log p^k.
###   S4  zero truncation -- N varied over a factor >= 4, and the tail bound re-derived.
###   S5  float species -- the zeros recomputed at doubled precision.
"""
import io
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import carto_atlas as C        # noqa: E402
import b38_act10 as B38        # noqa: E402

CACHE = (r"C:\Users\ECHOCH~1\AppData\Local\Temp\claude\D--"
         r"\2bde398e-07cf-4dd0-8608-0a3b93e6f10a\scratchpad\b233_zeros.json")
CELLS = [(2, "2"), (3, "3"), (4, "4")]
PRIMES = (2, 3, 5)
NV_SEQ = [2001, 4001, 8001, 16001]
NV_REF = 32001


def hhat_chunked(v, w, u, block=400):
    """### SAME FORMULA AS `C.hhat`, EVALUATED IN BLOCKS OVER u. ### Controlled below."""
    u = np.atleast_1d(np.asarray(u, dtype=np.float64))
    dv = np.gradient(v)
    wd = w * dv
    out = np.empty(u.shape[0], dtype=np.float64)
    for i in range(0, u.shape[0], block):
        uu = u[i:i + block]
        out[i:i + block] = np.cos(np.outer(uu, v)) @ wd
    return out


def columns(a, nv, gam):
    """### THE FOUR COLUMNS AT A GIVEN v-GRID, WITH EVERY OTHER AXIS HELD."""
    old = C.NV
    C.NV = nv
    C._KERN = None
    try:
        v, w = C.bump(a)
        L = math.log(a)
        dv = np.gradient(v)
        corr = np.convolve(w, w, mode="full") * float(dv[0])
        vc = np.linspace(-2 * L, 2 * L, corr.size)
        U = np.linspace(-C.UMAX, C.UMAX, C.NU)
        GU = hhat_chunked(v, w, U)
        A = float(np.trapezoid(GU ** 2 * C.kernel(U), U) / (2.0 * math.pi))
        Pc = float(np.trapezoid(w * np.cosh(v / 2.0), v))
        P = 2.0 * Pc * Pc
        PR = 0.0
        for p in PRIMES:
            k = 1
            while p ** k <= a * a + 1e-12:
                ln = math.log(p ** k)
                if ln <= 2 * L:
                    PR += 2.0 * math.log(p) / math.sqrt(p ** k) * float(np.interp(ln, vc, corr))
                k += 1
        g = hhat_chunked(v, w, gam)
        Z = 2.0 * float(np.sum(g * g))
    finally:
        C.NV = old
        C._KERN = None
    return dict(A=A, P=P, PR=PR, Z=Z, resid=Z - (P - PR + A))


def order_of(errs, hs):
    """### MEASURED ORDER between successive refinements: p = log(e1/e2)/log(h1/h2)."""
    out = []
    for i in range(len(errs) - 1):
        e1, e2 = abs(errs[i]), abs(errs[i + 1])
        if e1 > 0 and e2 > 0:
            out.append(math.log(e1 / e2) / math.log(hs[i] / hs[i + 1]))
        else:
            out.append(float('nan'))
    return out


def s2_bump_control():
    """### S2 -- THE POSITIVE CONTROL WITH AN EXACT ANSWER.
    ### `I = INT_{-1}^{1} exp(-1/(1-t^2)) dt` to high precision by mpmath.quad, against the
    ### instrument's own trapezoid rule on the same species of grid.
    ### ### THE REGISTERED EXPECTATION IS THAT THIS IS SUPER-ALGEBRAIC (Euler-Maclaurin: every
    ### derivative vanishes at the endpoints, so there are NO boundary terms at any order)."""
    from mpmath import mp, quad, exp as mexp, mpf
    mp.dps = 40
    exact = quad(lambda t: mexp(-1 / (1 - t ** 2)), [mpf(-1), mpf(1)])
    rows = []
    for n in NV_SEQ + [NV_REF]:
        t = np.linspace(-1.0, 1.0, n)
        f = np.zeros_like(t)
        m = np.abs(t) < 1.0
        f[m] = np.exp(-1.0 / (1.0 - t[m] ** 2))
        rows.append((n, float(np.trapezoid(f, t)), abs(float(np.trapezoid(f, t)) - float(exact))))
    return float(exact), rows


def s3_interp(a):
    """### S3 -- np.interp's OWN ERROR at the actual evaluation points log p^k."""
    L = math.log(a)
    pts = []
    for p in PRIMES:
        k = 1
        while p ** k <= a * a + 1e-12:
            ln = math.log(p ** k)
            if ln <= 2 * L:
                pts.append(ln)
            k += 1
    if not pts:
        return None
    old = C.NV
    ref = None
    rows = []
    try:
        for nv in NV_SEQ + [NV_REF]:
            C.NV = nv
            C._KERN = None
            v, w = C.bump(a)
            dv = np.gradient(v)
            corr = np.convolve(w, w, mode="full") * float(dv[0])
            vc = np.linspace(-2 * L, 2 * L, corr.size)
            vals = np.array([float(np.interp(x, vc, corr)) for x in pts])
            rows.append((nv, vals))
        ref = rows[-1][1]
    finally:
        C.NV = old
        C._KERN = None
    return pts, [(nv, float(np.max(np.abs(vals - ref)))) for nv, vals in rows[:-1]]


def main():
    print("=" * 104)
    print("b238 -- THE IMP-1 ERROR BUDGET. ### MEASUREMENT ONLY. NO CRITERION IS DECIDED HERE.")
    print("=" * 104)
    gam = np.array(json.load(io.open(CACHE, encoding='utf-8'))[:1000], dtype=float)

    print("\n### CONTROL 0 -- the chunked transform against the instrument's own `C.hhat`.")
    print("### IF THESE DISAGREE, EVERY REFERENCE VALUE BELOW IS UNGROUNDED.")
    C.NV = 4001
    C._KERN = None
    v0, w0 = C.bump(math.sqrt(3))
    u0 = np.linspace(-50.0, 50.0, 601)
    d0 = float(np.max(np.abs(hhat_chunked(v0, w0, u0) - C.hhat(v0, w0, u0))))
    print("   max |chunked - C.hhat| = %.3e   -> %s" % (d0, "CONTROL PASSES" if d0 < 1e-14
                                                        else "### CONTROL FAILS -- STOP"))
    if d0 >= 1e-14:
        return 1

    print("\n" + "=" * 104)
    print("### S1 -- UNIFORM GRID DISCRETIZATION, PER TERM. Reference at NV = %d." % NV_REF)
    print("### 'which term carries the error' is the question a summed residual hides.")
    print("=" * 104)
    s1 = {}
    for a_sq, tag in CELLS:
        a = math.sqrt(a_sq)
        ref = columns(a, NV_REF, gam)
        rows = [(nv, columns(a, nv, gam)) for nv in NV_SEQ]
        print("\n  diagonal a^2 = %s   (reference NV=%d)" % (tag, NV_REF))
        print("    %-8s %13s %13s %13s %13s %13s" % ("NV", "|dA|", "|dP|", "|dPR|", "|dZ|",
                                                     "residual"))
        for nv, c in rows:
            print("    %-8d %13.3e %13.3e %13.3e %13.3e %13.3e"
                  % (nv, abs(c['A'] - ref['A']), abs(c['P'] - ref['P']),
                     abs(c['PR'] - ref['PR']), abs(c['Z'] - ref['Z']), c['resid']))
        hs = [1.0 / (nv - 1) for nv in NV_SEQ]
        for key in ('A', 'P', 'PR', 'Z'):
            errs = [c[key] - ref[key] for _nv, c in rows]
            os_ = order_of(errs, hs)
            print("    measured order %-3s : %s" % (key, ", ".join("%.2f" % o for o in os_)))
        s1[tag] = dict(ref=ref, rows=[(nv, c) for nv, c in rows])

    print("\n" + "=" * 104)
    print("### S2 -- THE BUMP'S EDGE BEHAVIOUR, ON A KNOWN INTEGRAL WITH AN EXACT ANSWER.")
    print("### THE REGISTERED EXPECTATION: super-algebraic, NOT half-order (Euler-Maclaurin).")
    print("=" * 104)
    exact, rows = s2_bump_control()
    print("  exact (mpmath.quad, dps 40) = %.16f" % exact)
    print("    %-8s %20s %13s" % ("N", "trapezoid", "|error|"))
    for n, val, err in rows:
        print("    %-8d %20.16f %13.3e" % (n, val, err))
    errs = [r[2] for r in rows[:-1]]
    hs = [1.0 / (r[0] - 1) for r in rows[:-1]]
    print("    measured order     : %s" % ", ".join("%.2f" % o for o in order_of(errs, hs)))

    print("\n" + "=" * 104)
    print("### S3 -- INTERPOLATION AT THE ACTUAL EVALUATION POINTS log p^k.")
    print("=" * 104)
    for a_sq, tag in CELLS:
        r = s3_interp(math.sqrt(a_sq))
        if r is None:
            print("  diagonal a^2 = %s : ### NO EVALUATION POINTS (the prime column is EMPTY)" % tag)
            continue
        pts, rows = r
        print("  diagonal a^2 = %s   points: %s" % (tag, ", ".join("%.4f" % x for x in pts)))
        for nv, e in rows:
            print("      NV=%-8d max |interp - ref| = %.3e" % (nv, e))
        print("      measured order : %s"
              % ", ".join("%.2f" % o for o in order_of([e for _n, e in rows],
                                                       [1.0 / (n - 1) for n, _e in rows])))

    print("\n" + "=" * 104)
    print("### S4 -- ZERO TRUNCATION, N VARIED OVER A FACTOR >= 4.")
    print("=" * 104)
    for a_sq, tag in CELLS:
        a = math.sqrt(a_sq)
        line = []
        for n in (250, 500, 1000):
            line.append((n, columns(a, 4001, gam[:n])['resid']))
        print("  diagonal a^2 = %-3s  " % tag
              + "   ".join("N=%d resid=%.3e" % (n, r) for n, r in line))
    print("  ### THE TAIL BOUND, RE-DERIVED at N=1000 (gamma_N = %.2f):" % gam[999])
    for a_sq, tag in CELLS:
        v, w = C.bump(math.sqrt(a_sq))
        T = float(gam[999])
        u = np.linspace(T, 4000.0, 20001)
        g = C.hhat(v, w, u)
        dens = np.log(np.maximum(u, 7.0) / (2.0 * math.pi)) / (2.0 * math.pi)
        print("     a^2=%-3s tail <= %.3e" % (tag, float(2.0 * np.trapezoid(g * g * dens, u))))

    print("\n" + "=" * 104)
    print("### S5 -- FLOAT SPECIES: the zeros recomputed at DOUBLED precision (dps 25 -> 50).")
    print("### THE a^2=2 FLOOR IS NV-INVARIANT AND ITS PRIME COLUMN IS EMPTY -- if anything is")
    print("### left there, it is this.")
    print("=" * 104)
    from mpmath import mp, zetazero
    mp.dps = 50
    hi = np.array([float(zetazero(k).imag) for k in range(1, 201)], dtype=float)
    dev = float(np.max(np.abs(hi - gam[:200])))
    print("  max |zeros(dps50) - zeros(dps25)| over first 200 = %.3e" % dev)
    for a_sq, tag in CELLS:
        a = math.sqrt(a_sq)
        r25 = columns(a, 4001, gam[:200])['resid']
        r50 = columns(a, 4001, hi)['resid']
        print("  diagonal a^2 = %-3s  resid(dps25)=%.6e  resid(dps50)=%.6e  |diff|=%.3e"
              % (tag, r25, r50, abs(r25 - r50)))
    print("\n### MEASUREMENT COMPLETE. ### NO CRITERION WAS DECIDED IN THIS FILE.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
