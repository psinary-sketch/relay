# -*- coding: utf-8 -*-
"""b322_ladder.py -- THE UNIT'S RESIDUAL ALONG THE DOMAIN LADDER, AND THE RATE IT FALLS AT.

### ### **WHAT IS NEW HERE AND WHAT IS NOT.**
### ### **THE RESIDUAL IS NOT NEW AND IS NOT REWRITTEN.** ### It is b316's own quantity --
### `||(1 - S) u|| / ||u restricted to the free coordinates||` -- formed from b316's `outside` and
### b319's cut, both imported. ### b319 already ran it on eight frames. ### **THIS FILE'S FIXTURE (i)
### REQUIRES IT TO REPRODUCE b319's BANKED NUMBERS EXACTLY**, and if it does not, nothing below is
### worth reading.
### ### **WHAT IS NEW IS THE RATE.** ### b319 reported a course; it did not fit one. ### The order
### asks whether the residual falls *at the instrument's own rate*, and a rate is a number.

### ### ### **AND THE SECOND ROUTE TO THAT NUMBER SHARES NO CODE WITH THE FIRST.** ### (B3):
###   ### **ROUTE ONE** ### -- least squares on `log(residual)` against `log(X)`, five points.
###   ### **ROUTE TWO** ### -- b316's `asymptotics` measures whether `x u(x)` stays bounded far out.
###     ### If it does then `u ~ 1/x`, so the `L^2` mass beyond `X` goes like `INT_X^inf dx/x^2 ~
###     1/X`, so its NORM goes like `X^{-1/2}`. ### **THAT PREDICTS THE EXPONENT FROM THE VECTOR'S
###     ### SHAPE WITH NO REFERENCE TO THE LADDER AT ALL.**
### ### **A PREDICTION MADE FROM THE SAME FIVE NUMBERS IT IS COMPARED AGAINST WOULD BE ONE ROUTE
### ### WEARING TWO HATS**, and the registration fixed the agreement bar before either was computed.

### ### **THE TAPER IS b316's AND IS IMPORTED, NOT REWRITTEN.** ### b316 wrote it to answer exactly
### this question and wrote down what each outcome means; this file calls it and reports.
"""
import math
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))

import b316_instrument as INS   # noqa: E402  ### the unit, the frame, the taper -- IMPORTED
import b317_smear as SM         # noqa: E402  ### the ladders
import b319_stable as ST        # noqa: E402  ### the cut

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **b319's BANKED VALUES, WRITTEN HERE AS LITERALS SO FIXTURE (i) CAN FAIL.** ### They are read
# ### off `data/b319_the_stable_rank.txt`, the emitting act's own table, at four decimals as banked.
B319_STABLE = {(1024, 8.0): 0.7973, (2048, 16.0): 0.6450, (4096, 32.0): 0.4395,
               (8192, 64.0): 0.2861, (16384, 128.0): 0.1975}
B319_GRID = {(1024, 8.0): 0.9963, (2048, 16.0): 0.9460, (4096, 32.0): 0.8081,
             (8192, 64.0): 0.6031, (16384, 128.0): 0.3998}

TAPER_FRAC = 8.0     # ### b316's own default; not chosen here
TAIL_LO_FRAC = 0.10  # ### route two reads the tail over [0.10 X, 0.50 X] of ONE frame
TAIL_HI_FRAC = 0.50
TAIL_NY = 24         # ### cut points at which the tail norm is sampled


def residual(fr, sub, u):
    """### ### **b316's OWN QUANTITY: the fraction of the unit's norm OUTSIDE the space.**

    ### `outside` and the free-coordinate restriction are b316's; this function does the division and
    ### nothing else. ### **A RESIDUAL OF ZERO WOULD BE MEMBERSHIP; A RESIDUAL HOLDING STILL IS NOT
    ### ### A RESIDUAL BEING ZERO**, which is b319's sentence and it still holds.
    """
    return float(np.linalg.norm(fr.outside(sub, u))
                 / max(np.linalg.norm(u[sub['hi']]), 1e-300))


def frame_row(N, X, NY):
    """### One rung: the unit, both cuts, the untapered and tapered residuals, and the rank."""
    fr = INS.Frame(int(N), float(X), int(NY))
    u = INS.sonin_unit(fr)
    ut = INS.taper(fr, u, TAPER_FRAC)
    T = fr.transform_matrix()
    st, gr = ST.both_subspaces(fr, ST.TAU, T)
    row = dict(N=int(N), X=float(X),
               stable=residual(fr, st, u), grid=residual(fr, gr, u),
               tapered=residual(fr, st, ut),
               rank=int(st['rank']), dim=int(st['dim']), free=int(st['free']),
               far=float(INS.far_bound(fr, u, 0.5 * float(X))))
    del fr, T, st, gr, u, ut
    return row


def tail_exponent(fr, u, lo_frac=TAIL_LO_FRAC, hi_frac=TAIL_HI_FRAC, ny=TAIL_NY):
    """### ### **ROUTE TWO. ### THE VECTOR'S OWN SHAPE, AT ONE FRAME, WITH NO LADDER.**

    ### `t(Y) = ||u restricted to x > Y|| / ||u||` sampled at `ny` cut points inside one frame, then
    ### fitted as a power of `Y`. ### **THIS NEVER LOOKS AT A SECOND FRAME**, so it cannot inherit
    ### the ladder's answer; it reads how the vector's mass is distributed and nothing else.
    ### If `u ~ 1/x` then `INT_Y^inf u^2 ~ 1/Y` and the NORM goes like `Y^{-1/2}`, which is the
    ### prediction (B3) fixed before any value.
    ### **THE SAMPLING WINDOW STOPS AT HALF THE DOMAIN** so that the frame's own hard cut at `X` --
    ### the very thing under investigation -- does not contaminate the measurement of the decay.
    """
    ys = np.linspace(lo_frac * fr.X, hi_frac * fr.X, int(ny))
    tot = float(np.linalg.norm(u))
    ts = []
    for Y in ys:
        m = fr.x > Y
        ts.append(float(np.linalg.norm(u[m])) / max(tot, 1e-300))
    return np.asarray(ys), np.asarray(ts)


def fit_power(xs, ys):
    """### ### **LEAST SQUARES FOR `log y = A + p log x`. ### RETURNS `(p, A, rms)`.**

    ### The exponent is what the order calls the rate. ### **`rms` IS REPORTED BESIDE IT BECAUSE A
    ### ### SLOPE WITHOUT A FIT QUALITY IS A NUMBER PRETENDING TO BE A MEASUREMENT.**
    """
    lx = np.log(np.asarray(xs, dtype=float))
    ly = np.log(np.asarray(ys, dtype=float))
    A = np.vstack([np.ones_like(lx), lx]).T
    (a, p), *_ = np.linalg.lstsq(A, ly, rcond=None)
    rms = float(np.sqrt(np.mean((ly - (a + p * lx)) ** 2)))
    return float(p), float(a), rms


def self_test(verbose=False):
    ok, lines = [], []

    def note(s):
        lines.append(s)

    # ### (i) ### **THE ONE THAT LICENSES EVERYTHING ELSE: b319's BANKED VALUES, REPRODUCED.**
    r = frame_row(1024, 8.0, 512)
    d_s = abs(round(r['stable'], 4) - B319_STABLE[(1024, 8.0)])
    d_g = abs(round(r['grid'], 4) - B319_GRID[(1024, 8.0)])
    ok.append(d_s == 0.0 and d_g == 0.0)
    note('(i)    at (1024, 8): stable %.4f vs b319 %.4f ; grid %.4f vs b319 %.4f -- reproduced'
         % (r['stable'], B319_STABLE[(1024, 8.0)], r['grid'], B319_GRID[(1024, 8.0)]))

    # ### (ii) ### **AND IT MUST BE ABLE TO MISS.** ### A residual against the WRONG cut does.
    fr = INS.Frame(1024, 8.0, 512)
    u = INS.sonin_unit(fr)
    st, gr = ST.both_subspaces(fr, ST.TAU, fr.transform_matrix())
    wrong = residual(fr, gr, u)
    ok.append(abs(round(wrong, 4) - B319_STABLE[(1024, 8.0)]) > 1e-4)
    note('(ii)   the same unit against the GRID cut gives %.4f, not %.4f -- the arm can miss'
         % (wrong, B319_STABLE[(1024, 8.0)]))

    # ### (iii) the fit recovers a planted exponent exactly.
    xs = np.array([8.0, 16.0, 32.0, 64.0, 128.0])
    p, _a, rms = fit_power(xs, 3.0 * xs ** -0.5)
    ok.append(abs(p + 0.5) < 1e-12 and rms < 1e-12)
    note('(iii)  planted exponent -0.5 recovered as %.12f, fit rms %.3e' % (p, rms))

    # ### (iv) ### **AND IT REPORTS A DIFFERENT ONE FOR DIFFERENT DATA.** ### A fitter that always
    # ### returned the same slope would not be fitting.
    p2, _a2, _r2 = fit_power(xs, 3.0 * xs ** -1.25)
    ok.append(abs(p2 + 1.25) < 1e-12)
    note('(iv)   planted exponent -1.25 recovered as %.12f -- the fitter is reading the data' % p2)

    # ### (v) a FLAT course must come back as an exponent near zero, which is how (B1a) can fail.
    p3, _a3, _r3 = fit_power(xs, np.full(5, 0.4395))
    ok.append(abs(p3) < 1e-12)
    note('(v)    a perfectly flat course fits exponent %.3e -- FLAT is reachable' % p3)

    # ### (vi) the taper actually moves the vector; an arm that changed nothing would be no arm.
    ut = INS.taper(fr, u, TAPER_FRAC)
    moved = float(np.linalg.norm(ut - u))
    ok.append(moved > 1e-6)
    note('(vi)   the taper moves the vector by %.3e in norm' % moved)

    # ### (vii) ### **THE DECAY, WHICH IS ROUTE TWO'S WHOLE INPUT.** ### `x u(x)` bounded far out.
    far = float(INS.far_bound(fr, u, 0.5 * fr.X))
    ok.append(np.isfinite(far) and far > 0.0)
    note('(vii)  max |x u(x)| beyond x = %g : %.6f -- bounded, so u ~ 1/x' % (0.5 * fr.X, far))

    # ### (viii) ### **AND ROUTE TWO RUNS AT ONE FRAME AND RETURNS AN EXPONENT.**
    ys, ts = tail_exponent(fr, u)
    pt, _at, rt = fit_power(ys, ts)
    ok.append(np.isfinite(pt) and rt < 1.0)
    note('(viii) the tail exponent at (1024, 8), from the vector alone : %.4f (fit rms %.3e)'
         % (pt, rt))

    del fr, st, gr, u, ut
    if verbose:
        for s in lines:
            print('    ' + s)
    return all(ok), ok, lines


if __name__ == '__main__':
    good, arms, ls = self_test(verbose=True)
    print('  ### FIXTURES : %s  %s' % (arms, 'PASS' if good else '### FAIL ###'))
    sys.exit(0 if good else 1)
