# -*- coding: utf-8 -*-
"""b320_weil.py -- THE ARCHIMEDEAN WEIL DISTRIBUTION, FROM THE SOURCE'S OWN FORMULA.

### ### **EVERY ACT FROM b316 TO b319 CAPPED ITSELF AT ZERO EVALUATIONS OF `W_infinity`.** ### This
### one computes it, and may only do so from the paper.

### ### ### **THE SOURCE'S TWO DISPLAYS, AND WHY BOTH ARE NEEDED.**
###   ### **(39)** ### `tau(rho) = (rho^{1/2}/2) ( 1/(1+rho) + 1/|1-rho| )` ### -- singular at
###     `rho = 1`. ### A bare `1/|1-rho|` is not a distribution, and a reader who regularises it
###     from memory has supplied a constant the paper did not.
###   ### **(38)** ### `tau(rho) = rho^{1/2} INT_R (e^{2 pi i(1+rho)t} + e^{2 pi i(1-rho)t})
###     (-log|t|) dt` ### -- i.e. `tau(rho) = rho^{1/2}(W(1+rho) + W(1-rho))` with
###     `W = F(-log|t|)`. ### **THAT FIXES THE CONSTANT, AND IT IS THE ONLY THING THAT DOES.**
### ### The paper says exactly this: *"With this definition of the principal value, (38) gives the
### Weil distribution"*.

### ### ### **HOW THE TWO ARE USED HERE, AND WHY IT IS NOT THE OBVIOUS WAY.** ### The obvious route
### is to pair every test function against `-log|t|` on the transform side. ### **IT DOES NOT WORK
### ### FOR THIS CORPUS'S FUNCTIONS, AND THE FIXTURES CAUGHT IT.** ### Every `TestFunction` here is
### evaluated by `np.interp` -- it is numerically PIECEWISE LINEAR -- so its transform decays like
### `1/t^2` and the pairing cannot be truncated at any tolerable `t`. ### A first draft tried it, ran
### its tail search to `t = 2^20`, and returned a number two orders of magnitude wrong.
###
### ### **SO (38) IS USED ONCE, WHERE IT CONVERGES, TO FIX THE CONSTANT:**
###   ### on a GAUSSIAN, whose transform is a Gaussian, `INT (-log|t|) phi-hat(t) dt` is an ordinary
###     convergent quadrature with no tail and no oscillation;
###   ### matching it against the real-side Hadamard form
###     ### `H(phi) = INT_{|x|<R} (phi(x)-phi(0))/(2|x|) dx + INT_{|x|>R} phi(x)/(2|x|) dx`
###     gives ### **`<W, phi> = H(phi) + C_R phi(0)`**, with `C_R` a UNIVERSAL constant;
###   ### ### **AND IT IS MEASURED, NOT REMEMBERED** -- the fixtures require the same `C_R` from
###     Gaussians of two different widths, which is what "universal" means, and require a DIFFERENT
###     constant at a different split radius, which is what stops the arm being vacuous.
### ### Thereafter the act's own functions go through `H` alone: no transform, no tail, no
### oscillation, the singularity handled by one subtraction.

### ### **THE ASSEMBLY.** ### eq. (53) is `W_infinity(f) = - INT f(rho^{-1}) tau(rho) d*rho`. ###
### Splitting `tau` by (38) and substituting `x = 1 - rho` in the singular half:
###   ### `W_infinity(f) = - [ INT w_f(v) e^{v/2}/(2(1+e^v)) dv  +  <W, phi> ]`
###   ### with ### **`phi(x) := f((1-x)^{-1}) (1-x)^{-1/2}`**, supported in `[1-A, 1-1/A]` when `f`
###     is supported in `[1/A, A]` -- straddling zero, bounded away from one.
### The first term is regular because `1 + rho >= 1`, and there `W` IS the function `(1/2)/|x|`.

### ### **WHAT THIS FILE MAY NOT DO.** ### It may not tune anything to make an inequality hold.
"""
import math
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))

import b317_smear as SM   # noqa: E402
import b318_square as SQ  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### ==============================================================================================
# ### THE DECLARED QUADRATURE CONSTANTS. ### **NONE OF THEM IS A FINDING.**
# ### ==============================================================================================
NX = 200001         # ### nodes across a test function's own support, real side
NT = 200001         # ### nodes for the Gaussian calibration on the transform side
TGAUSS = 12.0       # ### the Gaussian's transform is below 1e-60 there; no truncation question
RSPLIT = 1.0        # ### the Hadamard split radius. ### `C_R` depends on it and both are printed
NV = 200001         # ### nodes for the regular half, in the source's own variable `v = log rho`
THM1_TOL = 1e-9     # ### (B2): Theorem 1's two vanishing conditions on `g`, tested at this
                    # ### ABSOLUTE bar and for the same reason as PD_FLOOR -- the moments are
                    # ### quadratures and a strict `== 0` would be a bar on rounding.
PD_FLOOR = 1e-9     # ### Definition 3.1 asks `f-hat >= 0`. ### `f-hat` here is formed by
                    # ### correlating and then transforming, so a value at `-4e-17` against a
                    # ### maximum of `3e-09` is zero. ### **THE RAW MINIMUM IS ALWAYS PRINTED.**


def gauss(s, x):
    """### `exp(-pi (x/s)^2)`, whose transform is `s exp(-pi (s t)^2)`."""
    return np.exp(-math.pi * (x / s) ** 2)


def pair_W_fourier_gauss(s):
    """### ### **`<W, phi_s>` BY (38), FOR A GAUSSIAN.** ### `phi_s-hat(t) = s exp(-pi s^2 t^2)`, so
    ### the pairing is `2 INT_0^inf (-log t) s exp(-pi s^2 t^2) dt`. ### **NO TAIL, NO OSCILLATION,
    ### ### NO TRUNCATION QUESTION.** ### This is the only place (38) is evaluated, and the only
    ### place a constant enters the act.
    """
    # ### ### **THE `-log t` SINGULARITY IS SUBTRACTED, NOT OUT-GRIDDED.** ### A raw trapezoid
    # ### through it left the constant disagreeing between two Gaussians at `5e-05` -- caught by
    # ### fixture (i). ### `INT_0^t0 (-log t) dt = t0 (1 - log t0)` exactly, and the remainder
    # ### `G(t) - G(0)` is `O(t^2)`, which the same trapezoid integrates without effort.
    t0 = 1e-3 / s
    G0 = s
    ti = np.linspace(0.0, t0, 20001)[1:]
    Gi = s * np.exp(-math.pi * (s * ti) ** 2)
    inner = G0 * t0 * (1.0 - math.log(t0)) + float(np.trapezoid(-np.log(ti) * (Gi - G0), ti))
    t = np.linspace(t0, TGAUSS / s, NT)
    outer = float(np.trapezoid(-np.log(t) * s * np.exp(-math.pi * (s * t) ** 2), t))
    return 2.0 * (inner + outer)


def hadamard(phi_fn, x_lo, x_hi, phi0, R=RSPLIT, nx=None):
    """### `H(phi) = INT_{|x|<R} (phi - phi(0))/(2|x|) dx + INT_{|x|>R} phi/(2|x|) dx`.

    ### `phi` is a CALLABLE, and that is not a style choice. ### **A SECOND DEFECT LIVED HERE AND
    ### ### THE UNCOVERED CELLS EXPOSED IT.** ### The first version sampled `phi` on one grid and
    ### then integrated on another, re-interpolating between them. ### When an integration node
    ### landed `1e-16` from the origin -- which it does for some cells and not others, purely by
    ### where `linspace` falls -- the subtracted integrand `(phi(x)-phi(0))/(2|x|)` became a `0/0`
    ### limit evaluated by LINEAR INTERPOLATION ACROSS NODES `1e-5` APART. ### The numerator picked
    ### up `O(1e-5 * slope)` of interpolation error and the denominator was `2e-16`.
    ### ### **AT `a = 2.1` THAT RETURNED `1.9e9`; AT `a = 2.15`, `1.98e293`.**
    ### Evaluating `phi` at the integration nodes themselves keeps the quotient bounded: the
    ### numerator is then `O(x)` by construction and the ratio tends to the one-sided slope.

    ### ### **THE INNER REGION IS ALWAYS THE WHOLE OF `[-R, R]`, NOT JUST WHERE `phi` LIVES.** ###
    ### The subtracted term is there on ALL of `|x| < R`, including where `phi` is zero. ### A first
    ### draft integrated only over `phi`'s support and dropped `-phi(0) INT_supp^R dx/(2|x|)`; at
    ### `a = 1.3` that missing piece is `-2.9465`, and it was the whole of this act's first failure.
    """
    lo, hi = min(x_lo, -R), max(x_hi, R)
    total = 0.0
    for (a, b, sub) in ((lo, -R, False), (-R, R, True), (R, hi, False)):
        if not (b > a):
            continue
        xs = np.linspace(a, b, int(nx or NX))
        ps = phi_fn(xs)
        ax = np.abs(xs)
        y = np.zeros_like(xs)
        nz = ax > 0.0
        y[nz] = ((ps[nz] - phi0) if sub else ps[nz]) / (2.0 * ax[nz])
        for i in np.where(~nz)[0]:
            if 0 < i < xs.size - 1:
                y[i] = 0.5 * (y[i - 1] + y[i + 1])
        total += float(np.trapezoid(y, xs))
    return total



def calibrate(R=RSPLIT, widths=(1.0, 0.5)):
    """### ### **`C_R`, MEASURED FROM (38) AND NOT REMEMBERED.**

    ### Returns `(C_R, spread, per_width)`. ### **THE SPREAD ACROSS WIDTHS IS THE ARM:** ### a
    ### universal constant must not depend on which Gaussian measured it.
    """
    vals = []
    for s in widths:
        vals.append(pair_W_fourier_gauss(s)
                    - hadamard(lambda xx, ss=s: gauss(ss, xx), -12.0 * s, 12.0 * s, 1.0, R))
    return float(np.mean(vals)), float(np.max(vals) - np.min(vals)), [float(v) for v in vals]


C_R, C_SPREAD, C_EACH = calibrate()


def pair_W(phi_fn, x_lo, x_hi, phi0, R=RSPLIT, c=None, nx=None):
    """### ### **`<W, phi> = H(phi) + C_R phi(0)`.** ### No transform, no tail, no oscillation."""
    return hadamard(phi_fn, x_lo, x_hi, phi0, R, nx) + (C_R if c is None else c) * phi0


def phi_of(f):
    """### `phi` AS A CALLABLE, with its support bounds and `phi(0) = f(1)`.

    ### ### **A CALLABLE, SO THE INTEGRATOR EVALUATES IT WHERE IT INTEGRATES** -- see `hadamard`.
    """
    A = f.support

    def phi_fn(xx):
        rho = 1.0 - xx
        out = np.zeros_like(rho)
        ok = rho > 0.0
        out[ok] = f(1.0 / rho[ok]) * rho[ok] ** -0.5
        return out

    return phi_fn, 1.0 - A, 1.0 - 1.0 / A, float(f(np.array([1.0]))[0])


def weil(f):
    """### ### **`W_infinity(f)` FROM (53), (38) AND (39). ### RETURNS `(value, reg, sing, phi0)`.**"""
    v = np.linspace(f.v[0], f.v[-1], NV)
    w = np.interp(v, f.v, f.w, left=0.0, right=0.0)
    reg = float(np.trapezoid(w * np.exp(v / 2.0) / (2.0 * (1.0 + np.exp(v))), v))
    pf, xl, xh, ph0 = phi_of(f)
    sing = pair_W(pf, xl, xh, ph0)
    return -(reg + sing), reg, sing, ph0


def self_test(verbose=False):
    ok, lines = [], []

    def note(s):
        lines.append(s)

    # ### (i) ### **THE CONSTANT IS UNIVERSAL, WHICH IS WHAT MAKES IT A CONSTANT.**
    ok.append(C_SPREAD < 1e-6 * max(abs(C_R), 1.0))
    note('(i)    C_R from widths 1.0 and 0.5 : %s ; spread %.3e ; C_R = %.12f'
         % (['%.10f' % v for v in C_EACH], C_SPREAD, C_R))

    # ### (i-b) ### **AND IT MUST HOLD FOR A GAUSSIAN NARROWER THAN THE SPLIT RADIUS.** ### That
    # ### is the arm the first draft did not have: with a narrow `phi` the grid never reached `+-R`,
    # ### the subtracted term's own tail was dropped, and `C_R` came back at `1.904` instead of
    # ### `2.415`. ### **THE MISSING PIECE WAS EXACTLY `-phi(0) log(R/supp)`.**
    cn, spn, en = calibrate(widths=(1.0, 0.05))
    ok.append(spn < 1e-6 * max(abs(cn), 1.0))
    note('(i-b)  C_R from widths 1.0 and 0.05 : %s ; spread %.3e'
         % (['%.10f' % v for v in en], spn))

    # ### (ii) ### **AND THE ARM CAN FIRE** -- a different split radius must give a different
    # ### constant, or the calibration is returning the same number whatever it is handed.
    c2, sp2, _e = calibrate(R=2.0)
    ok.append(abs(c2 - C_R) > 1e-3 and sp2 < 1e-6 * max(abs(c2), 1.0))
    note('(ii)   at R = 2 the constant is %.12f -- different, as it must be; spread %.3e'
         % (c2, sp2))

    # ### (iii) ### **(39) AGAINST THE ASSEMBLY, AWAY FROM THE SINGULARITY.** ### For a `phi`
    # ### supported away from zero, `phi(0) = 0` and the pairing must reduce EXACTLY to (39).
    def farf(xx):
        tt = xx - 3.0
        return np.exp(-1.0 / np.maximum(1.0 - tt ** 2, 1e-300)) * (np.abs(tt) < 1.0)
    a1 = pair_W(farf, 2.0, 4.0, 0.0)
    xf = np.linspace(2.0, 4.0, NX)
    a2 = float(np.trapezoid(farf(xf) / (2.0 * np.abs(xf)), xf))
    # ### the bar is `1e-9` RELATIVE and not `1e-12`: the assembly re-grids onto its own
    # ### sub-intervals and interpolates, which costs about `1e-11`. ### **THAT IS A QUADRATURE
    # ### TOLERANCE ON AN IDENTITY, NOT A BAR ON THE CONTROL**, and nine significant figures is
    # ### what the method delivers.
    ok.append(abs(a1 - a2) < 1e-9 * max(abs(a2), 1.0))
    note('(iii)  away from zero: assembly %.12f vs (39) %.12f ; relative %.3e'
         % (a1, a2, abs(a1 - a2) / abs(a2)))

    # ### (iv) ### **AND THAT CHECK CAN FAIL** -- a halved kernel misses by half.
    ok.append(abs(a1 - 0.5 * a2) > 1e-3 * abs(a2))
    note('(iv)   the same against a deliberately halved (39) : difference %.3e'
         % abs(a1 - 0.5 * a2))

    # ### (v) linearity, with the constant riding on `phi(0)`.
    d = abs(pair_W(lambda xx: 2.0 * gauss(0.8, xx), -2.0, 2.0, 2.0)
            - 2.0 * pair_W(lambda xx: gauss(0.8, xx), -2.0, 2.0, 1.0))
    ok.append(d < 1e-9)
    note('(v)    linearity: <W,2phi> - 2<W,phi> = %.3e' % d)

    # ### (vi) `W_infinity` at a NON-BANKED cell is finite, and both halves are finite.
    g = SM.mean_zero_variant(SM.FIXTURE_A)
    f = SQ.autocorrelation(g)
    val, reg, sing, p0 = weil(f)
    ok.append(np.isfinite(val) and np.isfinite(reg) and np.isfinite(sing))
    note('(vi)   W_inf at the fixture cell : %.9f  (regular %.9f, singular %.9f, phi(0) %.9f)'
         % (val, reg, sing, p0))

    # ### (vi-b) ### **THE ANSWER MUST NOT DEPEND ON WHERE THE INTEGRATION GRID FALLS.** ### That is
    # ### the arm the first draft did not have. ### The second defect was a node landing `1e-16` from
    # ### the origin -- an accident of `linspace`, which happened at some cells and not others -- and
    # ### a run that changed only the node count would have exposed it at once.
    pf, xl, xh, p0b = phi_of(f)
    v1 = pair_W(pf, xl, xh, p0b)
    v2 = pair_W(pf, xl, xh, p0b, nx=NX + 1)
    ok.append(abs(v1 - v2) < 1e-6 * max(abs(v1), 1.0))
    note('(vi-b) grid invariance: %.9f at NX and %.9f at NX+1 ; difference %.3e'
         % (v1, v2, abs(v1 - v2)))

    # ### (vii) ### **THE TWO SIDES ARE FORMED FROM THE SAME OBJECT**, and Definition 3.1 holds for
    # ### `f` to the declared floor.
    mn, tm, h0, pd = SQ.positive_definite(f)
    mx = float(np.max(SQ.fhat(f, np.linspace(0.0, 1.0, 3))))
    ok.append(mn >= -PD_FLOOR * max(abs(mx), 1.0))
    note('(vii)  f = g conv g# by Definition 3.1 : min f-hat = %.3e ; max %.3e ; strict >=0 : %s'
         % (mn, mx, pd))

    if verbose:
        for s in lines:
            print('    ' + s)
    return all(ok), ok, lines


if __name__ == '__main__':
    good, arms, ls = self_test(verbose=True)
    print('  arms : %s  %s' % (arms, 'PASS' if good else '### FAIL ###'))
    sys.exit(0 if good else 1)
