# -*- coding: utf-8 -*-
"""b252 COMPONENT 2 -- THE MEASUREMENT. ### CONSUMES COMPONENT 1.

### `A_n(u)` IS CELL-INDEPENDENT -- it involves only the eigenfunction and the dilation. ### Only
### `corr` and the range `[0, 2L]` are per-cell. ### **THAT IS A PROPERTY OF THE OBJECT, READ OFF
### ITS DEFINITION, AND IT IS WHY THE OVERLAP IS COMPUTED ONCE PER `u` AND NOT ONCE PER CELL.**

### THE SUBSTITUTION, WRITTEN OUT SO THE NODES CAN BE PUT ON THE TRUE SUPPORT:
###   A_n(u) = (sqrt(L)/2) * int_{-1/L}^{1/L} xi_n(x) xi_n(L x) dx      [L := lambda = e^u]
### with `s = t/L`, `t` on `[-1,1]` at Gauss-Legendre nodes `t_k`, weights `v_k`:
###   ### **A_n(u) = (1/(2 sqrt(L))) * sum_k v_k xi_n(t_k) xi_n(t_k / L)**
### ### At `L = 1` this is `0.5 * ||xi_n||^2 = 1` for every `n` -- ### **THE EXACT FACT THE
### ### MEANINGS FILE BANKED AT SECTION (B), NOW ALSO A RUNNING SELF-CHECK OF THE INSTRUMENT.**
"""
import io
import json
import math
import os
import sys

import numpy as np

sys.path.insert(0, r"D:\relay\tools\e16")
import b38_act10 as B38          # noqa: E402  ### G-INDEP: the quadrature column's OWN owner
import qeps_layer as Q           # noqa: E402

MODES = r"D:\relay\data\b252_modes.json"
OUT = r"D:\relay\data\b252_measure.json"
NQ_IN = 200                      # ### REGISTERED
NUS = (401, 801)                 # ### b38's own NU_HALF, PLUS ONE REFINEMENT


def bary_weights(x):
    """### BARYCENTRIC WEIGHTS FOR GAUSS-LEGENDRE NODES (Berrut-Trefethen):
    ###   beta_j = (-1)^j sqrt( (1 - x_j^2) * w_j ).
    ### ### **THE NAIVE PRODUCT FORM `1/prod(x_j - x_k)` UNDER/OVERFLOWS FLOAT64 AT n = 120 AND
    ### ### WOULD HAVE PUT A SILENT FLOOR UNDER THIS ACT'S WHOLE POINT.**"""
    n = len(x)
    j = np.arange(n)
    # ### recovered from the nodes alone, so a wrong cached weight cannot slip through
    lw = np.zeros(n)
    for k in range(n):
        d = x[k] - x
        d[k] = 1.0
        lw[k] = -np.sum(np.log(np.abs(d)))
    lw -= lw.max()
    return ((-1.0) ** j) * np.exp(lw)


def bary_eval(x, beta, F, y):
    """### EVALUATE the interpolants of every column of `F` at every point of `y`.
    ### `F` is (nodes x modes); returns (len(y) x modes). ### Exact at nodes."""
    d = y[:, None] - x[None, :]
    hit = np.isclose(d, 0.0, atol=0.0, rtol=0.0)
    d[hit] = 1.0
    W = beta[None, :] / d
    W[hit.any(1)] = 0.0
    rows, cols = np.nonzero(hit)
    W[rows, cols] = 1.0
    return (W @ F) / W.sum(1)[:, None]


def load(setting):
    d = json.load(io.open(MODES, encoding='utf-8'))[setting]
    x = np.array([float(s) for s in d['x']])
    w = np.array([float(s) for s in d['w']])
    XI = np.array([[float(s) for s in row] for row in d['xi']]).T   # (nodes x modes)
    mu = [float(s) for s in d['mu']]
    res = [float(s) for s in d['res']]
    return x, w, XI, mu, res


def A_of_u(x, beta, XI, uu, t, v):
    """### `A_n(u)` FOR EVERY MODE AND EVERY `u`, WITH THE NODES ON THE TRUE SUPPORT."""
    XT = bary_eval(x, beta, XI, t)                    # ### xi_n(t_k), u-independent
    out = np.empty((len(uu), XI.shape[1]))
    for i, u in enumerate(uu):
        lam = math.exp(u)
        XL = bary_eval(x, beta, XI, t / lam)          # ### xi_n(t_k / lambda)
        out[i] = (v[:, None] * XT * XL).sum(0) / (2.0 * math.sqrt(lam))
    return out


def A_of_u_b38mode(x, w, XI, uu):
    """### **b38-EMULATION MODE, FOR G-REPRO-A.** ### The SAME restricted-Gauss-node scheme and the
    ### SAME linear interpolation as `trace_modes`, driven by THIS act's clean eigenvectors.
    ### ### **ITS PURPOSE IS TO SEPARATE TWO QUESTIONS THAT WOULD OTHERWISE BE ONE:** ### is this
    ### ### act's ARITHMETIC right, and does its SCHEME differ from b38's? ### Only the first is a
    ### ### question about correctness."""
    out = np.empty((len(uu), XI.shape[1]))
    for i, u in enumerate(uu):
        lam = math.exp(u)
        for n in range(XI.shape[1]):
            fy = np.interp(lam * x, x, XI[:, n], left=0.0, right=0.0)
            out[i, n] = math.sqrt(lam) * 0.5 * float((w * XI[:, n] * fy).sum())
    return out


def main():
    res = json.load(io.open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    t, v = np.polynomial.legendre.leggauss(NQ_IN)

    for setting in ('120|120', '60|100'):
        x, w, XI, mu, eqres = load(setting)
        beta = bary_weights(x)
        # ### THE RUNNING SELF-CHECK: A_n(0) MUST BE 1 FOR EVERY MODE. ### banked at (B).
        a0 = A_of_u(x, beta, XI, np.array([0.0]), t, v)[0]
        res.setdefault('a0', {})[setting] = a0.tolist()
        res.setdefault('mu', {})[setting] = mu
        res.setdefault('eqres', {})[setting] = eqres

        for a, alab in B38.CELLS:
            L = math.log(a)
            v_, w2, corr, vc, LL = B38.family(a)
            for NU in NUS:
                key = '%s|%s|%d' % (setting, alab, NU)
                if key in res:
                    continue
                uu = np.linspace(0.0, 2 * L, NU)
                cu = np.interp(uu, vc, corr)
                An = A_of_u(x, beta, XI, uu, t, v)
                tr = 2.0 * np.trapezoid(cu[:, None] * An, uu, axis=0)
                res[key] = tr.tolist()
                sys.stderr.write("  %s done\n" % key)
                json.dump(res, io.open(OUT, 'w', encoding='utf-8'))

    # ------------------------------------------------------------ G-REPRO, BOTH FORMS
    x, w, XI, mu, eqres = load('120|120')
    beta = bary_weights(x)
    for a, alab in B38.CELLS:
        key = 'repro|%s' % alab
        if key in res:
            continue
        L = math.log(a)
        v_, w2, corr, vc, LL = B38.family(a)
        uu = np.linspace(0.0, 2 * L, B38.NU_HALF)
        cu = np.interp(uu, vc, corr)
        # ### b38's OWN float64 result, from its OWN owner. ### NOT re-implemented.
        tr_b38 = B38.trace_modes(a, corr, vc, LL, 700, 11)
        # ### G-REPRO-A: b38's scheme, this act's clean vectors, on b38's own node set.
        xb, wb, lamb, lam2b, xib, xi1b, anb, danb = Q.layer(700)
        Ab = A_of_u_b38mode(xb, wb, xib[:, :11], uu)
        tr_emul_b38vec = 2.0 * np.trapezoid(cu[:, None] * Ab, uu, axis=0)
        # ### and the same scheme driven by THIS act's vectors, interpolated to b38's nodes
        XIb = bary_eval(x, beta, XI, xb)
        Ac = A_of_u_b38mode(xb, wb, XIb, uu)
        tr_emul_clean = 2.0 * np.trapezoid(cu[:, None] * Ac, uu, axis=0)
        res[key] = dict(b38=tr_b38.tolist(), emul_b38vec=tr_emul_b38vec.tolist(),
                        emul_clean=tr_emul_clean.tolist())
        sys.stderr.write("  %s done\n" % key)
        json.dump(res, io.open(OUT, 'w', encoding='utf-8'))

    # ------------------------------------------------- THE QUADRATURE COLUMN, ITS OWN OWNERS
    if 'quad' not in res:
        rr = np.exp(np.linspace(1e-4, math.log(12.001), B38.EPS_NRHO))
        ee_full = np.atleast_1d(Q.eps(rr, NQ=B38.EPS_NQ, NG=B38.EPS_NG))
        quad = {}
        for a, alab in B38.CELLS:
            v_, w2, corr, vc, L = B38.family(a)
            A, P, PR = B38.left_side(a, B38.S4, v_, w2, corr, vc, L)
            E2 = B38.e2_of_grid(a, corr, vc, L, rr, ee_full)
            quad[alab] = dict(A=A, E2=E2, AplusE2=A + E2)
        res['quad'] = quad
        json.dump(res, io.open(OUT, 'w', encoding='utf-8'))
    print("measured: %d keys" % len(res))


if __name__ == "__main__":
    main()
