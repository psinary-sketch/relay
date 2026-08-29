# -*- coding: utf-8 -*-
"""b252 COMPONENT 1 -- THE INSTRUMENT. ### b249's EIGENSOLVE EXTENDED TO THE MODE RANGE THIS
### ACT NEEDS, PLUS THE OVERLAP MACHINERY `trace_modes` COULD NOT CARRY IN FLOAT64.

### ### **WHY AN EXTENSION IS NEEDED AT ALL, FROM THE MEANINGS FILE (F.1):** ### b242 measured
### `n_last = 6` at every NQ from 500 to 1300. ### Beyond mode 6 float64 cannot resolve the
### eigenPAIR, so ### **b38's `xi[:, n]` FOR `n >= 7` IS NOISE AND ANY `tr[n]` BUILT FROM IT IS
### NOISE.** ### `tr[n]` does NOT involve `mu_n` at all -- only the eigenFUNCTION -- so the object
### is perfectly well-scaled; ### **what fails in float64 is the SOLVE, not the integral.**
### ### **HENCE THE SPLIT THIS INSTRUMENT IS BUILT ON: SOLVE AT HIGH PRECISION, INTEGRATE AT LOW.**
### The eigenvectors are `O(1)` and well-conditioned once resolved. ### **THAT CLAIM IS TESTED BY
### G-SELF RATHER THAN ASSUMED.**

### TWO SCHEME DIFFERENCES FROM `trace_modes`, BOTH NAMED IN THE MEANINGS FILE BEFORE MEASURING:
###   (1) `trace_modes` runs Gauss-Legendre over the FULL `[-1,1]` while the integrand has been
###       ZEROED outside `|x| <= 1/lambda` -- ### **A QUADRATURE ACROSS A KINK.** ### This tool
###       puts its nodes ON the true support.
###   (2) `trace_modes` interpolates `xi_n` LINEARLY. ### This tool uses BARYCENTRIC LAGRANGE
###       interpolation on the Legendre nodes.
### ### **BOTH ARE REPORTED AS SCHEME DIFFERENCES, NOT AS CORRECTIONS THIS ACT MAY IMPOSE.**
"""
import io
import json
import math
import os
import sys

import numpy as np
from mpmath import mp, mpf

CACHE = r"D:\relay\data\b252_modes.json"

SETTINGS = [(120, 120), (60, 100)]      # ### (dps, NQ_e). ### REGISTERED. ### FIRST IS PRIMARY.
NTARGET = 20                            # ### N = 20 -> prolate index 40. ### REGISTERED TARGET.


def kern(d, c):
    """### THE CORPUS'S OWN KERNEL, from b249: sin(c d)/(pi d), removable singularity at 0."""
    if abs(d) < mp.mpf(10) ** (-(mp.dps - 5)):
        return c / mp.pi
    return mp.sin(c * d) / (mp.pi * d)


def leggauss_mp(n):
    """### b249's NODES AND WEIGHTS: Newton on the Legendre polynomial. ### numpy's leggauss is
    ### float64 and would re-impose the very floor this act exists to lift."""
    xs, ws = [], []
    for i in range(1, n + 1):
        x = mp.cos(mp.pi * (i - mpf(1) / 4) / (n + mpf(1) / 2))
        for _ in range(100):
            p0, p1 = mp.one, mp.zero
            for k in range(1, n + 1):
                p0, p1 = ((2 * k - 1) * x * p0 - (k - 1) * p1) / k, p0
            dp = n * (x * p0 - p1) / (x * x - 1)
            dx = p0 / dp
            x -= dx
            if abs(dx) < mp.mpf(10) ** (-(mp.dps + 5)):
                break
        p0, p1 = mp.one, mp.zero
        for k in range(1, n + 1):
            p0, p1 = ((2 * k - 1) * x * p0 - (k - 1) * p1) / k, p0
        dp = n * (x * p0 - p1) / (x * x - 1)
        xs.append(x)
        ws.append(2 / ((1 - x * x) * dp * dp))
    return xs, ws


def solve(dps, nq, ntarget):
    """### ONE SETTING. ### Returns nodes, weights, and `xi_n = sqrt(2) psi_{2n}` at the nodes,
    ### for n = 0..ntarget, all as decimal STRINGS so nothing is lost to the cache.
    ### ### **SIGN IS NOT FIXED AND NEED NOT BE: `A_n(u)` IS QUADRATIC IN `xi_n`, SO IT IS
    ### ### SIGN-INVARIANT.** ### Stated rather than silently relied on."""
    mp.dps = dps
    c = 2 * mp.pi
    x, w = leggauss_mp(nq)
    sw = [mp.sqrt(wi) for wi in w]
    A = mp.matrix(nq, nq)
    for i in range(nq):
        for j in range(i, nq):
            v = kern(x[i] - x[j], c) * sw[i] * sw[j]
            A[i, j] = v
            A[j, i] = v
    E, V = mp.eigsy(A)
    order = sorted(range(nq), key=lambda k: -E[k])
    need = 2 * ntarget + 1
    if len(order) < need:
        raise RuntimeError("### nq too small: %d modes needed, %d available" % (need, len(order)))
    mus, xis, res = [], [], []
    for n in range(ntarget + 1):
        m = order[2 * n]                       # ### PIN P1: THE EVEN SUB-SEQUENCE.
        mu = E[m]
        psi = [V[j, m] / sw[j] for j in range(nq)]
        # ### G-EQ, PER MODE: the eigenfunction equation's residual, carried as evidence that the
        # ### vector is a real eigenvector and not solver noise.
        r = mp.zero
        for i in range(nq):
            s = mp.fsum(kern(x[i] - x[j], c) * w[j] * psi[j] for j in range(nq))
            r = max(r, abs(s - mu * psi[i]))
        mus.append(mp.nstr(mu, 20))
        res.append(mp.nstr(r, 6))
        xis.append([mp.nstr(mp.sqrt(2) * p, dps - 5) for p in psi])
    return ([mp.nstr(xi, dps - 5) for xi in x], [mp.nstr(wi, dps - 5) for wi in w],
            mus, xis, res)


def main():
    cache = json.load(io.open(CACHE, encoding='utf-8')) if os.path.exists(CACHE) else {}
    for dps, nq in SETTINGS:
        key = '%d|%d' % (dps, nq)
        if key in cache:
            sys.stderr.write("  cached: %s\n" % key)
            continue
        sys.stderr.write("  solving %s (this is the slow part)...\n" % key)
        xs, ws, mus, xis, res = solve(dps, nq, NTARGET)
        cache[key] = dict(x=xs, w=ws, mu=mus, xi=xis, res=res, dps=dps, nq=nq,
                          ntarget=NTARGET)
        json.dump(cache, io.open(CACHE, 'w', encoding='utf-8'))
        sys.stderr.write("  done: %s\n" % key)
    print("cached settings: %s" % ", ".join(sorted(cache)))


if __name__ == "__main__":
    main()
