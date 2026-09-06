# -*- coding: utf-8 -*-
"""b339_price.py -- THE PRICE OF THE EXPONENT, UNDER b322's SEALED RULE. ### NO FRAME IS BUILT HERE.

### ### **WHAT IS PRICED.** ### At each covered cell the identity residual `R(X) = (W_inf - Tr(X)) - INT_EF`
### along b320's domain ladder (`X = 8, 16, 32, 64, 128`, `N = 128 X`, `NY = 512`), the left side b320's banked
### `weil` on `f = autocorrelation(mean_zero_variant(a))`, the right side b320's banked `Tr` of the square on
### the stable cut, the remainder b321's banked value under the SOURCE convention -- so that `R` is exactly
### the column b321 printed as *residual to -INT*, reproduced here from the record and not retyped.
### ### **THE RATE** is `fit_power` (b322's, IMPORTED) on `R` against `X`, its `rms` beside it, and the last
### step's slope as the conservative reading. ### **THE SPLIT CRITERION** (sealed, section (C)): `R <= s/2`
### with `s` the candidates' separation, b321's *apart by* column. ### **THE PRICE**: `X_req = 128 (R(128) /
### (s/2))^(1/|p|)`, an EXTRAPOLATION OF A FITTED SLOPE AND LABELLED AS ONE. ### **THE CEILING**: `X = 512`,
### sealed before this file ran. ### The run that this file gates is `b339_resolve.py`, which reads this
### file's JSON and builds a frame only at the cells this file says fit.
"""
import io
import json
import math
import os
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))
import b322_ladder as LA        # noqa: E402  ### fit_power, IMPORTED never edited
import b317_smear as SM         # noqa: E402  ### DOMAIN_AXIS, NY_FIXED, READ

D = os.path.join(ROOT, 'data')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

RUN = os.path.join(D, 'b339_price_run.txt')
OUT = os.path.join(D, 'b339_price.json')
RECORD = os.path.join(D, 'b320_rows.json')

# ### b321's banked values, quoted from `data/b321_the_window_opened.txt` (the separation table; located
# ### by `b339_extract.py`): the remainder under the source convention, and the two copies' distance.
INT_EF = {1.3: 0.158889558, 1.35: 0.186481766, 1.41: 0.221284108}
INT_ER = {1.3: 0.157908477, 1.35: 0.184544767, 1.41: 0.217290580}
APART = {1.3: 0.000981080, 1.35: 0.001936999, 1.41: 0.003993528}
# ### b321's ladder column *residual to -INT*, the reproduction target (first and last frame per cell).
LADDER_ENDS = {1.3: (0.896556824, 0.023223882), 1.35: (0.671666, 0.020793), 1.41: (0.524907, 0.018808)}

CEILING_X = 512.0           # ### sealed in section (C); `N = 128 X`, `NY = 512`
SPLIT = 0.5                 # ### `R <= s/2`, sealed in section (C)


def next_pow2(x):
    return float(2 ** int(math.ceil(math.log(x, 2) - 1e-12)))


def main():
    t0 = time.time()
    lines = []

    def rec(s=''):
        lines.append(s)

    J = json.load(io.open(RECORD, encoding='utf-8'))
    XS = [fk[1] for fk in SM.DOMAIN_AXIS]
    rec('=' * 100)
    rec('b339 -- THE PRICE OF THE EXPONENT. ### b322\'s SEALED RULE: UNDER-RESOLVED, NOT OPEN; THE PRICE IS THE RATIO.')
    rec('=' * 100)
    rec('  ### the domain ladder, b317\'s DOMAIN_AXIS : X = %s ; N = 128 X ; NY = %d' % (XS, SM.NY_FIXED))
    rec('  ### the record read : data/b320_rows.json (`rows[].weil`, `axes[a].domain`) ; the remainders and the')
    rec('  ### separation quoted from b321\'s bank (located by b339_extract.py) ; the fitter b322_ladder.fit_power, IMPORTED.')
    rec('  ### the ceiling, sealed : X = %g (N = %d, NY = %d) ; the split criterion, sealed : R <= s/2.' % (CEILING_X, 128 * CEILING_X, SM.NY_FIXED))
    rec('')
    weil = {float(r['a']): float(r['weil']) for r in J['rows']}
    out = {}
    fits = []
    repro_ok = True
    for a in J['covered']:
        a = float(a)
        tr = [float(t) for t in J['axes'][str(a)]['domain']]
        m = [weil[a] - t for t in tr]                     # ### margin W - Tr
        R = [mm - INT_EF[a] for mm in m]                  # ### residual to -INT, the source convention
        s = APART[a]
        p, A, rms = LA.fit_power(XS, R)
        p_last = math.log(R[-1] / R[-2]) / math.log(XS[-1] / XS[-2])
        e0, e1 = LADDER_ENDS[a]
        rep = abs(R[0] - e0) < 5e-7 and abs(R[-1] - e1) < 5e-7
        repro_ok = repro_ok and rep
        ratio_now = R[-1] / s
        x_req = XS[-1] * (R[-1] / (SPLIT * s)) ** (1.0 / abs(p))
        x_req_last = XS[-1] * (R[-1] / (SPLIT * s)) ** (1.0 / abs(p_last))
        x_run = next_pow2(x_req)
        fit = x_req <= CEILING_X
        rec('  ### a = %-5g   W_inf = %.9f   INT_EF = %.9f   INT_ER = %.9f   s (apart by) = %.9f' % (a, weil[a], INT_EF[a], INT_ER[a], s))
        rec('    %-6s %-8s %-16s %-16s %-16s' % ('X', 'N', 'Tr (square)', 'margin W - Tr', 'R = margin - INT_EF'))
        for X, t, mm, r in zip(XS, tr, m, R):
            rec('    %-6g %-8d %-16.9f %-16.9f %-16.9f' % (X, 128 * X, t, mm, r))
        rec('    ### reproduces b321\'s ladder ends (%.9g, %.9g) : %s' % (e0, e1, 'YES' if rep else '### NO ###'))
        rec('    ### the fitted rate  : R ~ X^%+.6f   (fit rms %.4f)     the last step 64 -> 128 : X^%+.6f' % (p, rms, p_last))
        rec('    ### the ratio today  : R(128) / s = %.3f   (b321\'s figure; the question UNDER-RESOLVED by b322\'s rule)' % ratio_now)
        rec('    ### THE PRICE        : X_req = 128 x (R(128) / (s/2))^(1/%.6f) = %.1f   ratio X_req / 128 = %.2f' % (abs(p), x_req, x_req / XS[-1]))
        rec('    ###   by the last step\'s slope instead : X_req = %.1f   ratio %.2f   (the conservative reading)' % (x_req_last, x_req_last / XS[-1]))
        rec('    ### AGAINST THE CEILING X = %g : %s' % (CEILING_X, 'FITS -- the run is at X = %g and X = %g (N = %d, %d)' % (x_run / 2, x_run, 64 * x_run, 128 * x_run) if fit else 'DOES NOT FIT -- UNAFFORDABLE at this ceiling; the price banked'))
        rec('    ### **AN EXTRAPOLATION OF A FITTED SLOPE, LABELLED AS ONE. A PRICE IS NOT A PREDICTION.**')
        rec('')
        out[str(a)] = dict(a=a, weil=weil[a], tr=tr, margin=m, R=R, int_ef=INT_EF[a], int_er=INT_ER[a], s=s,
                           p=p, A=A, rms=rms, p_last=p_last, ratio_now=ratio_now, x_req=x_req, x_req_last=x_req_last,
                           x_run=x_run if fit else None, fits=bool(fit), reproduces=bool(rep))
        if fit:
            fits.append(a)
    rec('  ### ### **THE GATE ON THE RUN (sealed): the cells whose X_req <= %g : %s**' % (CEILING_X, fits if fits else 'NONE -- UNAFFORDABLE'))
    rec('  ### ### **THE LADDER REPRODUCED FROM THE RECORD AT EVERY CELL : %s**' % ('YES' if repro_ok else '### NO ###'))
    rec('  ### elapsed : %.1f s' % (time.time() - t0))
    rec('=' * 100)
    res = dict(cells=out, fits=fits, ceiling_x=CEILING_X, split=SPLIT, xs=XS, ny=SM.NY_FIXED, reproduces=repro_ok)
    io.open(RUN, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(lines) + chr(10))
    txt = json.dumps(res, indent=1)
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(txt)
    print(chr(10).join(lines))
    return 0 if repro_ok else 1


if __name__ == '__main__':
    sys.exit(main())
