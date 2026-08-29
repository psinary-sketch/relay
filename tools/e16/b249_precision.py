# -*- coding: utf-8 -*-
"""b249 -- THE PRECISION VEIL LIFTED. ### A BOUNDED INSTRUMENT CONSTRUCTION AND MEASUREMENT.

### **NO DERIVATION AND NO THEOREM.** ### The statement measured is b247's, unchanged.
###
### THE ROUTE, AND ITS REASON, REGISTERED BEFORE CONSTRUCTION (registration section A):
### ### **A DIRECT EXTENSION OF THE CORPUS'S OWN PROLATE INSTRUMENT INTO EXTENDED PRECISION.**
### `prolate_layer.prolate` builds the symmetrised Gauss-Legendre matrix of the corpus's own
### kernel and eigendecomposes it. ### THIS TOOL DOES THE SAME IN mpmath AT A REGISTERED dps.
### ### **b205's STEPPER IS *NOT* REUSED: it solves the RRJT EXTERIOR ODE on [1, infinity), and
### ### b247 ruled its `alpha` and the prolate `xi_n(1)` (DOUBLE-NAME). ### REUSING IT HERE WOULD
### ### BE THE DOUBLE-NAME ERROR THIS PROGRAMME RULED AGAINST ONE ACT AGO.**
### ### **ONE THING CHANGES -- THE ARITHMETIC** -- which is why G-REPRO can catch any error by
### ### comparison against b242's float64 table.
###
### RESUMABLE: every completed (dps, NQ) setting is banked to JSON and re-read, never remembered.
"""
import io
import json
import os
import sys
import time

from mpmath import mp, mpf

BANK = r"D:\relay\data\b249_precision_run.txt"
CACHE = r"D:\relay\data\b249_precision_points.json"

DPS_LADDER = [60, 120]            # ### G-SELF: two settings, agreement quoted.
NQ_LADDER = [40, 60, 80]          # ### the largest that completes is used AND PRINTED.
NMODES = 26                       # ### N >= 20 as the instrument affords.

# ### b242's BANKED float64 PER-MODE VALUES -- axes: NQ = 700, NTERM = 11, EPS_NQ = 700, S4.
# ### G-REPRO compares modes 0-6 to these BEFORE any new mode is read.
B242_LAM2 = [9.999427534e-01, 9.593903454e-01, 2.746660266e-01, 3.478238072e-03,
             7.465620360e-06, 5.820371503e-09, 2.072073661e-12]
B242_XI1 = [0.026179996, 0.609479254, 2.413226271, 3.526143743,
            4.099362227, 4.571835018, 4.994344471]


def leggauss_mp(n):
    """### GAUSS-LEGENDRE NODES AND WEIGHTS IN mpmath, BY NEWTON ON THE LEGENDRE POLYNOMIAL.
    ### numpy's leggauss is float64 and would re-impose the very floor this act exists to lift."""
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


def kern(d, c):
    """### THE CORPUS'S OWN KERNEL: sin(c*d)/(pi*d), with the removable singularity at d = 0."""
    if abs(d) < mp.mpf(10) ** (-(mp.dps - 5)):
        return c / mp.pi
    return mp.sin(c * d) / (mp.pi * d)


def solve(dps, nq):
    """### ONE SETTING. ### Returns (mu list, psi1 list, residuals) for the top NMODES modes."""
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
    E, V = mp.eigsy(A)                      # ### symmetric eigendecomposition, ascending
    order = sorted(range(nq), key=lambda k: -E[k])
    mus, psi1s, res = [], [], []
    k1 = [kern(mp.one - x[j], c) for j in range(nq)]
    for m in order[:NMODES]:
        mu = E[m]
        # ### psi (L^2[-1,1]-normalised) from the symmetrised eigenvector: psi = V / sqrt(w)
        psi = [V[j, m] / sw[j] for j in range(nq)]
        # ### THE ENDPOINT FROM THE EIGENFUNCTION EQUATION, exactly as the corpus's layer does it:
        # ###   psi(1) = (1/mu) INT K(1,y) psi(y) dy
        s = mp.fsum(k1[j] * w[j] * psi[j] for j in range(nq))
        p1 = s / mu if mu != 0 else mp.mpf('nan')
        # ### G-EQ: the residual of the eigenvalue equation at the nodes.
        r = mp.mpf(0)
        for i in range(nq):
            qi = mp.fsum(kern(x[i] - x[j], c) * w[j] * psi[j] for j in range(nq))
            r = max(r, abs(qi - mu * psi[i]))
        mus.append(mu)
        psi1s.append(p1)
        res.append(r)
    return mus, psi1s, res


def main():
    cache = json.load(io.open(CACHE, encoding='utf-8')) if os.path.exists(CACHE) else {}
    out = []

    def rec(s=""):
        print(s, flush=True)
        out.append(s)

    def save():
        io.open(BANK, "w", encoding="utf-8").write("\n".join(out) + "\n")

    rec("=" * 104)
    rec("b249 -- THE PRECISION VEIL LIFTED. ### THE RUN.")
    rec("### RUN AT %s (local)." % time.strftime("%Y-%m-%dT%H:%M:%S"))
    rec("=" * 104)
    rec("### CEILING (b15): 'A FINITE-PLACE-SET OBJECT AT A FINITE CUTOFF DECIDES NOTHING GLOBAL.'")
    rec("### h2 UNCHANGED. ### NOTHING DEPOSITS. ### **NO DERIVATION AND NO THEOREM.**")
    rec("### ROUTE: the corpus's OWN prolate instrument extended into mpmath. ### b205's stepper")
    rec("### is NOT reused -- it is the RRJT EXTERIOR ODE and b247 ruled it (DOUBLE-NAME).")
    rec("")

    results = {}
    for dps in DPS_LADDER:
        for nq in NQ_LADDER:
            key = "%d|%d" % (dps, nq)
            if key in cache:
                results[key] = cache[key]
                rec("  resumed from bank: dps=%d NQ=%d" % (dps, nq))
                continue
            t0 = time.time()
            try:
                mus, p1s, res = solve(dps, nq)
            except Exception as e:
                rec("  ### setting dps=%d NQ=%d DID NOT COMPLETE: %s" % (dps, nq, e))
                save()
                continue
            d = dict(mu=[mp.nstr(v, 40) for v in mus],
                     psi1=[mp.nstr(v, 40) for v in p1s],
                     res=[mp.nstr(v, 12) for v in res],
                     secs=round(time.time() - t0, 1))
            cache[key] = d
            results[key] = d
            json.dump(cache, io.open(CACHE, "w", encoding="utf-8"), indent=1, sort_keys=True)
            rec("  completed: dps=%d NQ=%d in %.1fs" % (dps, nq, d["secs"]))
            save()
    save()
    rec("")
    rec("### SETTINGS COMPLETED: %s" % sorted(results.keys()))
    rec("### (the tables, G-REPRO, G-SELF, G-EQ and the verdict are assembled by the reader tool")
    rec("###  b249_report.py, which consumes this bank and does not recompute it.)")
    save()
    print("\nbanked: %s" % BANK)


if __name__ == "__main__":
    main()
