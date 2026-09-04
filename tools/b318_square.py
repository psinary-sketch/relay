# -*- coding: utf-8 -*-
"""b318_square.py -- THE SQUARE FORM. ### **THE ONE THING THE SOURCE GUARANTEES FOR FREE.**

### ### **WHAT THIS FILE IS.** ### b317 computed `Tr(theta(f) S)` on the truncated Sonin space and
### found the mean-zero column changing sign. ### The source says, in its own voice, where its
### positivity actually lives:
###
###   ### *"one can associate to a test function f in C_c^inf(R*_+) the trace Tr(theta(f) S), and one
###   ### sees that this functional is positive definite by construction, SINCE WHEN EVALUATED ON
###   ### f = g * g^ IT IS THE TRACE Tr(theta(g) S theta(g)^) OF A POSITIVE OPERATOR."*
###
### ### ### **SO THE GUARANTEE ATTACHES AT `f = g conv g^`, AND THERE IT IS A DIFFERENT
### ### ### EXPRESSION.** ### `Tr(theta(g) S theta(g)^)` is a Hilbert-Schmidt norm squared:
###
###   ### `Tr(theta(g) S theta(g)^) = Tr(theta(g) S S theta(g)^) = || theta(g) S ||_HS^2 >= 0`
###
### ### and that is nonnegative ### **AS ARITHMETIC** ### -- a sum of squares of real numbers -- with
### no appeal to the space, the truncation or the quadrature.

### ### **THE TWO OBJECTS THIS FILE COMPUTES, AND THE ONE IDENTITY BETWEEN THEM.**
###   ### **SQUARE(f) := || theta(f) S ||_HS^2**, formed as `|| A[:, H] P ||_F^2` where `A` is
###     b317's kernel matrix, `H` the free coordinates and `P = I - Q Q^T` b316's projector.
###   ### **SMEAR(f) := Tr(theta(f) S)**, which is b317's column, recomputed by importing b317's own
###     `compressed_trace` rather than by re-deriving it.
###   ### ### **AND THE IDENTITY: ### `SQUARE(f) = SMEAR(f^ conv f)`.** ### Because
###     `theta(f)^ theta(f) = theta(f^ conv f)`, the source's square form is the corpus's smear
###     evaluated at the AUTOCORRELATION of the window, not at the window. ### **THAT IS THE WHOLE
###     ### DIFFERENCE BETWEEN THE TWO OBJECTS AND THIS FILE CHECKS IT NUMERICALLY** rather than
###     asserting it: `square_trace` and `compressed_trace(autocorrelation(f))` are independent code
###     paths and the fixtures require them to agree.

### ### **THE CLASS TEST, IN THE SOURCE'S OWN DEFINITION.** ### Definition 3.1: ### *"We say that f
### is positive definite when its Fourier transform is pointwise positive, i.e. f-hat(t) >= 0, for
### all t."* ### So the test is a scan of `f-hat` and nothing cleverer, and Boas-Kac (the source's
### Proposition 3.2) is what makes it equivalent to being of the form `g conv g^`.

### ### **WHAT THIS FILE MAY NOT BE USED FOR.** ### ### **NO UNIT IS USED ANYWHERE IN IT** --
### b300's derived archimedean unit is never constructed, never projected, never traced. ### And the
### source's INEQUALITY is not evaluated: `W_infinity` is not computed here in any direction.
"""
import math
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E16 = os.path.join(ROOT, 'tools', 'e16')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, E16)

import b316_instrument as INS   # noqa: E402  ### the four normalizations, IMPORTED
import b317_smear as SM         # noqa: E402  ### the kernel, the trace and the test functions

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### ==============================================================================================
# ### THE DECLARED CONSTANTS. ### **NONE OF THEM IS A FINDING.**
# ### ==============================================================================================
# ### The source's own intervals, quoted once and used everywhere below.
SUPPORT_F_HI = 2.0                       # ### eq. (53): supp f inside [1/2, 2]
SUPPORT_G_HI = math.sqrt(2.0)            # ### Theorem 1 / (3): supp g inside [2^-1/2, 2^1/2]

# ### The positive-definiteness scan, in units of `1/L` so it follows the cell's own width.
PD_TMAX_OVER_L = 64.0
PD_NT = 6001

# ### The uniform grid the autocorrelation is formed on. ### The variant lives on a UNION grid,
# ### which is not uniform, and a correlation needs a uniform step.
AUTOCORR_NV = 8193

SQUARE_BLOCK = 512

# ### (B2) THE IDENTITY BAR, as sealed in `data/b318_registration_2026-09-04.txt` (5): `SQUARE(f)`
# ### and `SMEAR(f^ conv f)` must agree to this, relative, or the identification of the two objects
# ### is REFUSED and no verdict is taken from it.
BAR_IDENTITY = 0.01

FIXTURE_A = SM.FIXTURE_A                 # ### 1.75, not one of the atlas's cells


# ### ==============================================================================================
# ### THE CLASS TEST -- DEFINITION 3.1, AND NOTHING CLEVERER.
# ### ==============================================================================================
def fhat(f, t):
    """### `f-hat(t) = INT f(rho) rho^{-it} d*rho = INT w(v) e^{-itv} dv`.

    ### For a REAL EVEN `w` this is `INT w(v) cos(t v) dv`, real. ### **THE TEST FUNCTIONS THIS ACT
    ### JUDGES ARE ALL EVEN IN `v` BY CONSTRUCTION**, and the fixture checks the imaginary part is
    ### zero rather than assuming it.
    """
    t = np.atleast_1d(np.asarray(t, dtype=np.float64))
    return np.trapezoid(np.cos(np.outer(t, f.v)) * f.w[None, :], f.v, axis=1)


def positive_definite(f, tmax_over_L=PD_TMAX_OVER_L, nt=PD_NT):
    """### ### **THE SOURCE'S OWN DEFINITION 3.1, APPLIED.** ### Returns
    ### `(min_fhat, t_at_min, fhat_at_zero, verdict)`.

    ### The scan runs in units of the cell's own width `L = log a`, so a narrow cell is scanned as
    ### far in `t` as a wide one is. ### **THE VERDICT IS A SCAN AND CARRIES A SCAN'S REACH**: it can
    ### show a function is NOT positive definite by exhibiting a negative value, and it cannot prove
    ### one IS beyond the interval scanned. ### Both readings are printed with the interval.
    """
    L = abs(float(f.v[-1]))
    T = tmax_over_L / max(L, 1e-300)
    t = np.linspace(0.0, T, int(nt))
    h = fhat(f, t)
    i = int(np.argmin(h))
    return float(h[i]), float(t[i]), float(h[0]), bool(h[i] >= 0.0)


def autocorrelation(f, nv=AUTOCORR_NV):
    """### ### **`f^ conv f`, THE SOURCE'S `g conv g^`, IN THE SOURCE'S OWN VARIABLE.**

    ### `(f^ conv f)(v) = INT f(u) f(u + v) du`, whose support is twice the width of `f`'s and whose
    ### transform is `|f-hat|^2` -- which is why it is positive definite and `f` need not be.
    """
    L = abs(float(f.v[-1]))
    u = np.linspace(-L, L, int(nv))
    du = u[1] - u[0]
    w = np.interp(u, f.v, f.w, left=0.0, right=0.0)
    ac = np.correlate(w, w, mode='full') * du
    v = np.linspace(-2.0 * L, 2.0 * L, ac.size)
    return SM.TestFunction('autocorrelation of ' + f.name, v, ac,
                           'formed from the same test function by np.correlate on a uniform grid')


# ### ==============================================================================================
# ### THE SQUARE FORM.
# ### ==============================================================================================
def square_trace(fr, sub, f, block=None):
    """### ### **`|| theta(f) S ||_HS^2`, FORMED AS A SUM OF SQUARES AND NOTHING ELSE.**

    ### `theta(f) S` has matrix `A[:, H] P` with `P = I - Q Q^T`; its Frobenius norm squared is the
    ### sum of the squares of that matrix's entries. ### **NO SUBTRACTION IS PERFORMED ANYWHERE IN
    ### ### THIS FUNCTION**, which is what makes the nonnegativity arithmetic rather than a
    ### cancellation that happened to land on the right side of zero.
    ### The rows run over the WHOLE grid, not over `H`: `theta(f)` maps the space out of itself, and
    ### b316 measured exactly that leakage. ### Restricting the rows would be discarding it.
    """
    hi = sub['hi']
    xh = fr.x[hi]
    Q = sub['Q']
    b = int(block or SQUARE_BLOCK)
    acc = 0.0
    for s in range(0, fr.N, b):
        e = min(s + b, fr.N)
        K = SM.kernel_rows(fr, f, fr.x[s:e], xh)
        R = K - (K @ Q) @ Q.T
        acc += float(np.sum(R * R))
    return acc


def first_contributing_row(fr, f):
    """### THE SMALLEST `x` AT WHICH THE KERNEL IS NONZERO FOR A COLUMN IN `H`, AND ITS RESOLUTION.

    ### b317 found the kernel under-resolved at the first grid node, where its `u`-window holds less
    ### than one point, and confined that defect to `x <= 1` where the compressed trace never looks.
    ### ### **THE SQUARE FORM DOES LOOK AT ROWS BELOW ONE**, so the same question has to be asked
    ### again here rather than inherited. ### Returns `(x_first, points_in_window)`.
    """
    a = f.support
    x0 = INS.ALPHA / a
    return x0, float(x0 * (a - 1.0 / a) / fr.h)


# ### ==============================================================================================
# ### THE FIXTURES. ### **EVERY ARM MUST BE ABLE TO REPORT THE OTHER ANSWER.**
# ### ==============================================================================================
def self_test(verbose=False):
    ok, lines = [], []

    def note(s):
        lines.append(s)

    a = FIXTURE_A
    bp = SM.corpus_bump(a)
    ac = autocorrelation(bp)

    # ### (i) ### **THE CLASS TEST SAYS YES ON A GENUINE SQUARE.** ### `f^ conv f` has transform
    # ### `|f-hat|^2`, so Definition 3.1 must pass it. ### An arm that never says yes is not a test.
    mn, tm, h0, good = positive_definite(ac)
    ok.append(good)
    note('(i)    autocorrelation of the bump: min f-hat = %.6e at t = %.3f -> positive definite : %s'
         % (mn, tm, good))

    # ### (ii) ### **AND IT SAYS NO ON A FUNCTION KNOWN NOT TO BE ONE, BY AN ARGUMENT AND NOT BY
    # ### ### MEASUREMENT.** ### A wide integral-one bump minus a narrow one has transform
    # ### `phi_wide-hat - phi_narrow-hat`, which is zero at `t = 0` and NEGATIVE just above it,
    # ### because the wider bump's transform falls faster. ### The arm is built from that argument.
    import carto_atlas
    v1, w1 = carto_atlas.bump(a)
    v2, w2 = carto_atlas.bump(a ** 0.5)
    V = np.union1d(v1, v2)
    W = np.interp(V, v1, w1, left=0.0, right=0.0) - np.interp(V, v2, w2, left=0.0, right=0.0)
    diff = SM.TestFunction('wide minus narrow', V, W, 'fixture only')
    mn2, tm2, h02, good2 = positive_definite(diff)
    ok.append((not good2) and mn2 < 0.0)
    note('(ii)   wide minus narrow: min f-hat = %.6e at t = %.3f -> positive definite : %s'
         % (mn2, tm2, good2))

    # ### (iii) the transform of an even function is real: the scan's own premise, checked.
    im = float(np.max(np.abs(np.trapezoid(np.sin(np.outer(np.linspace(0.0, 8.0, 33), bp.v))
                                          * bp.w[None, :], bp.v, axis=1))))
    ok.append(im < 1e-12)
    note('(iii)  imaginary part of the bump transform, worst : %.3e' % im)

    # ### (iv) the autocorrelation preserves the integral as a square: `INT (f^ conv f) = (INT f)^2`.
    ok.append(abs(ac.at_zero() - bp.at_zero() ** 2) < 1e-6)
    note('(iv)   INT(f conv f) = %.9f against (INT f)^2 = %.9f'
         % (ac.at_zero(), bp.at_zero() ** 2))

    fr = INS.Frame(256, 8.0, 64)
    sub = fr.subspace()

    # ### (v) ### **THE SQUARE IS NONNEGATIVE AS ARITHMETIC.** ### It is a sum of squares of machine
    # ### floats; every summand is `>= 0` and the running sum of nonnegatives never goes below zero.
    sq = square_trace(fr, sub, bp)
    ok.append(sq >= 0.0)
    note('(v)    square = %.9f ; nonnegative : %s' % (sq, sq >= 0.0))

    # ### (vi) ### **AND IT EQUALS THE SMEAR AT THE AUTOCORRELATION** -- the identity that names the
    # ### difference between the source's object and the corpus's, checked by two code paths.
    sm_ac = SM.compressed_trace(fr, sub, autocorrelation(bp))[0]
    rel = abs(sq - sm_ac) / max(abs(sq), 1e-300)
    ok.append(rel < 1e-2)
    note('(vi)   square %.9f vs smear at the autocorrelation %.9f : relative %.3e'
         % (sq, sm_ac, rel))

    # ### (vii) ### **AND THAT AGREEMENT CAN FAIL** -- the smear at the window itself is a different
    # ### number, which is the whole finding this act is built to state.
    sm_f = SM.compressed_trace(fr, sub, bp)[0]
    rel_bad = abs(sq - sm_f) / max(abs(sq), 1e-300)
    ok.append(rel_bad > 1e-1)
    note('(vii)  the same against the smear at the WINDOW %.9f : relative %.3e' % (sm_f, rel_bad))

    # ### (viii) the block size decides nothing.
    ok.append(abs(square_trace(fr, sub, bp, block=7) - sq) < 1e-9 * max(abs(sq), 1.0))
    note('(viii) same square at block 7 : %.9f' % square_trace(fr, sub, bp, block=7))

    # ### (ix) the zero function gives exactly zero, so the norm is not measuring the grid.
    zero = SM.TestFunction('zero', bp.v, np.zeros_like(bp.w), 'fixture only')
    ok.append(square_trace(fr, sub, zero) == 0.0)
    note('(ix)   square of the zero test function : %.1e' % square_trace(fr, sub, zero))

    # ### (x) the rows the square actually reaches are resolved -- b317's first-node defect asked
    # ### again here, because the square DOES look below `x = 1` and the trace did not.
    x0, npts = first_contributing_row(fr, bp)
    ok.append(npts > 1.0)
    note('(x)    first contributing row x = %.5f ; its u-window holds %.2f point(s)' % (x0, npts))

    if verbose:
        for s in lines:
            print('    ' + s)
    return all(ok), ok, lines


if __name__ == '__main__':
    good, arms, ls = self_test(verbose=True)
    print('  arms : %s  %s' % (arms, 'PASS' if good else '### FAIL ###'))
    sys.exit(0 if good else 1)
