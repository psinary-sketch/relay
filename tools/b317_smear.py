# -*- coding: utf-8 -*-
"""b317_smear.py -- THE ASSEMBLY. ### **THE SOURCE'S SMEARED TRACE, ON THE TRUNCATED SPACE.**

### ### **WHAT THIS FILE IS.** ### b316 built a computable truncation of `S(1,1)` from Definition
### 4.4 and declared what it could and could not do. ### **THIS FILE POINTS IT**, at the one
### quantity b316 named and refused to compute: ### `Tr(theta(f) S)` ### of the source's Theorem
### 4.7, for a stated test function, on that truncation.

### ### ### **THE ASSEMBLY, FROM THE SOURCE'S OWN DEFINITIONS AND NOTHING ELSE.**
### ### The source's eq. (61) gives the scaling action ### `(theta(lam) xi)(v) = lam^{-1/2}
### ### xi(lam^{-1} v)`. ### Integrating it against a test function in the multiplicative group's
### own measure `d*lam = dlam/lam` gives an operator with a KERNEL, and the kernel is where every
### factor has to be right:
###
###     ### `(theta(f) xi)(x) = INT f(lam) lam^{-1/2} xi(x/lam) d*lam`
###     ###                  ### `= INT f(x/u) u^{1/2} x^{-1/2} xi(u) du/u`      [ u = x/lam ]
###     ### ### **`= INT K(x,u) xi(u) du`,   `K(x,u) = f(x/u) / sqrt(x u)`.**
###
### ### **THAT SUBSTITUTION IS THE WHOLE OF THE ASSEMBLY AND IT IS CHECKED TWO WAYS**, because a
### derivation that only appears in a docstring is not a check: ### `smear_by_kernel` builds `K`
### and `smear_by_scaling` integrates ### **the instrument's own `scaling`** ### over `v = log lam`,
### and the fixtures require them to agree AND require the agreement to break under a deliberately
### wrong normalization.

### ### **THE COMPRESSION AND THE TRACE.** ### `S` is b316's projector: kill the coordinates with
### `x <= 1`, then project off the row space of the transform condition. ### On the free
### coordinates `S = I - Q Q^T`, so
###     ### ### **`Tr(S theta(f) S) = Tr(theta(f) S) = Tr(A_HH) - Tr(Q^T A_HH Q)`**
### which needs only `A`'s DIAGONAL and `rank` matrix-vector products -- ### **so the operator is
### never formed whole**, and the row-blocking below is what keeps the allocation bounded.

### ### **THE TWO TEST FUNCTIONS, BOTH IN THE SOURCE'S VARIABLE.** ### The source's test functions
### live on `R*_+` and its measure is `d*rho`, so `v = log rho` is the source's own coordinate and
### `INT f(rho) d*rho = INT w(v) dv`. ### **THE FIRST IS THE CORPUS'S OWN BUMP, TAKEN FROM THE
### ### CORPUS'S OWN EMITTING FILE** (`tools/e16/carto_atlas.py`, `def bump`) and not rewritten
### here -- integral one, support `[1/a, a]`. ### **THE SECOND IS A MEAN-ZERO VARIANT BUILT OUT OF
### ### THREE OF THAT SAME BUMP** at three widths, with the coefficients solved so that BOTH
### moments vanish:
###   ### `INT f d*rho = 0` -- the transform at zero, and
###   ### `INT f(rho) rho^{+-1/2} d*rho = 0` -- ### **THE SOURCE'S OWN eq. (54)**, which for an EVEN
###     test function is the single condition `INT w(v) cosh(v/2) dv = 0`.
### ### **THE CORPUS'S BUMP SATISFIES NEITHER, AND THAT IS THE SOURCE'S CLASS BOUNDARY** -- reported
### as a measurement in the run rather than asserted here.

### ### **WHAT THIS FILE MAY NOT BE USED FOR.** ### b316 declared its instrument ### **NOT
### ### CERTIFIED FOR MEMBERSHIP QUESTIONS**, and nothing here decides one. ### The trace is a
### number on a TRUNCATION; whether that truncation's answer is the object's answer is
### `W-ORD-ARCH-MEMBERSHIP` and is not settled by computing on it. ### **AND NO UNIT IS USED
### ### ANYWHERE IN THIS FILE** -- b300's derived archimedean unit is never constructed, never
### projected and never traced.
"""
import io
import json
import math
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E16 = os.path.join(ROOT, 'tools', 'e16')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, E16)

import b316_instrument as INS   # noqa: E402  ### the four normalizations, IMPORTED not re-typed

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### ==============================================================================================
# ### THE DECLARED CONSTANTS. ### **NONE OF THEM IS A FINDING.**
# ### ==============================================================================================
EQ_WEIL, EQ_VANISH, EQ_THEOREM = '(53)', '(54)', 'Theorem 4.7'

# ### The three widths the mean-zero variant is built from, as EXPONENTS on the cell's own `a`.
# ### `a**1` is the corpus's own bump at the cell; the two narrower ones live inside its support,
# ### so ### **THE VARIANT NEVER LEAVES THE SUPPORT THE CORPUS'S BUMP OCCUPIES.**
MZ_EXPONENTS = (1.0, 0.5, 0.25)

# ### The row-block used to apply the kernel. ### A memory parameter and nothing else.
BLOCK = 512

# ### The cell the FIXTURES run at. ### **DELIBERATELY NOT ONE OF THE ATLAS'S BANKED CELLS**, so
# ### that no value at a banked cell can exist before the registration is sealed.
FIXTURE_A = 1.75

# ### ==============================================================================================
# ### THE BARS AND THE FRAMES, ### **AS SEALED IN `data/b317_registration_2026-09-04.txt` (4) AND
# ### (5).** ### They live here so that the deciding runner carries no float literal of its own and
# ### so that the suite reads them off ONE file. ### **NONE OF THEM IS A FINDING.**
# ### ==============================================================================================
BAR_SMALL = 10.0      # ### (B1) `small` means `|T| <= |A| / BAR_SMALL`
BAR_REACH = 0.05      # ### (B2) five per cent, relative, on BOTH axes
NY_FIXED = 512        # ### one NY throughout, so each axis moves one thing

# ### (5) THE GRID AXIS -- `X` held at 32, `h` halving from 1/64 to 1/512.
GRID_AXIS = ((2048, 32.0, NY_FIXED), (4096, 32.0, NY_FIXED),
             (8192, 32.0, NY_FIXED), (16384, 32.0, NY_FIXED))
# ### (5) THE DOMAIN AXIS -- `h` held at 1/128, `X` doubling from 8 to 128.
DOMAIN_AXIS = ((1024, 8.0, NY_FIXED), (2048, 16.0, NY_FIXED), (4096, 32.0, NY_FIXED),
               (8192, 64.0, NY_FIXED), (16384, 128.0, NY_FIXED))
# ### THE SHARED CELL OF THE TWO AXES, and the reference frame for the thirteen-cell sweep.
REFERENCE = (4096, 32.0, NY_FIXED)
# ### The three cells the full two-axis tables are built at: one inside the source's support
# ### condition, one exactly at its boundary, one outside it.
DETAIL_CELLS = (1.5, 2.0, 3.0)
# ### The domain frames the BAND is taken over for all thirteen cells.
# ### ### **IT IS THE WHOLE DOMAIN AXIS, AND THAT IS WHAT THE SEAL SAYS.** ### (B1) scores the
# ### prediction against ### *the largest `|T|` the domain sweep produces at the cell*, and ### **THE
# ### ### DOMAIN SWEEP IS THE REGISTERED DOMAIN AXIS, ALL FIVE `X`** -- not a cheaper subset of it.
# ### A first draft banded over three of the five and would have scored the narrowest cell on a
# ### smaller number than the registration demands.
SWEEP_FRAMES = DOMAIN_AXIS
# ### The source's eq. (53) support condition, quoted: `supp f` inside `[1/2, 2]`.
SUPPORT_LO, SUPPORT_HI = 0.5, 2.0

ATLAS_BANK = os.path.join(ROOT, 'data', 'carto_atlas.jsonl')


# ### ==============================================================================================
# ### THE TEST FUNCTIONS.
# ### ==============================================================================================
class TestFunction(object):
    """### A test function on `R*_+`, carried as `w(v)` on a grid of `v = log rho`.

    ### **EVALUATION IS PIECEWISE-LINEAR INTERPOLATION OF THAT GRID AND ZERO OUTSIDE IT**, which is
    ### exactly how the corpus's own atlas uses its bump (`np.interp` against `v, w`), so the
    ### function this act integrates is the function the corpus's number was formed from.
    """

    def __init__(self, name, v, w, provenance):
        self.name, self.v, self.w, self.provenance = name, v, w, provenance
        self.support = float(np.exp(v[-1]))

    def __call__(self, rho):
        return np.interp(np.log(rho), self.v, self.w, left=0.0, right=0.0)

    # ### the two moments the source's class is defined by -- ### **REPORTED, NEVER ASSUMED**
    def at_zero(self):
        """### `INT f(rho) d*rho` -- the transform at zero."""
        return float(np.trapezoid(self.w, self.v))

    def vanishing_54(self):
        """### `INT f(rho) rho^{+-1/2} d*rho`, which for an EVEN `f` is one number."""
        return (float(np.trapezoid(self.w * np.exp(self.v / 2.0), self.v)),
                float(np.trapezoid(self.w * np.exp(-self.v / 2.0), self.v)))

    def l1(self):
        return float(np.trapezoid(np.abs(self.w), self.v))


def corpus_bump(a):
    """### **THE CORPUS'S OWN INTEGRAL-ONE BUMP, FROM THE CORPUS'S OWN EMITTING FILE.**

    ### `tools/e16/carto_atlas.py`, `def bump` -- imported, never re-implemented. ### Its
    ### normalization is `np.trapezoid(w, v) = 1` on its own 4001-node grid, and that convention
    ### travels with the number the atlas banked from it.
    """
    import carto_atlas
    v, w = carto_atlas.bump(a)
    return TestFunction('corpus bump a=%g' % a, v, w,
                        'tools/e16/carto_atlas.py::bump (the corpus\'s own emitting file)')


def mean_zero_variant(a):
    """### **THE VARIANT INSIDE THE SOURCE'S CLASS.** ### Three of the corpus's own bumps, at
    ### widths `a**1`, `a**(1/2)`, `a**(1/4)`, combined so that both of the source's moments vanish.

    ### ### **THE UNION GRID IS NOT A CONVENIENCE EITHER.** ### Each bump is piecewise linear on its
    ### own nodes; the union of the three node sets contains every breakpoint, and the trapezoid
    ### rule is EXACT on a piecewise-linear function over a grid containing its breakpoints. ### **SO
    ### ### REFINING ONTO THE UNION PRESERVES EACH BUMP'S OWN INTEGRAL EXACTLY**, and the corpus's
    ### normalization is carried rather than re-imposed.

    ### The scale is fixed by ### **`INT |f| dv = 1`**, which is the same number the integral-one
    ### bump carries (its `L1` norm IS its integral, since it is non-negative). ### **SO THE TWO
    ### ### COLUMNS ARE NORMALISED THE SAME WAY AND THE COMPARISON BETWEEN THEM IS NOT A SCALE.**
    """
    import carto_atlas
    grids = []
    for e in MZ_EXPONENTS:
        v, w = carto_atlas.bump(a ** e)
        grids.append((v, w))
    V = grids[0][0]
    for v, _w in grids[1:]:
        V = np.union1d(V, v)
    phi = [np.interp(V, v, w, left=0.0, right=0.0) for v, w in grids]
    I = np.array([np.trapezoid(p, V) for p in phi])
    M = np.array([np.trapezoid(p * np.cosh(V / 2.0), V) for p in phi])
    # ### `c_0` is fixed to one and the other two solve the two vanishing conditions.
    A2 = np.array([[I[1], I[2]], [M[1], M[2]]])
    b2 = np.array([-I[0], -M[0]])
    c12 = np.linalg.solve(A2, b2)
    c = np.array([1.0, c12[0], c12[1]])
    W = c[0] * phi[0] + c[1] * phi[1] + c[2] * phi[2]
    scale = np.trapezoid(np.abs(W), V)
    tf = TestFunction('mean-zero variant a=%g' % a, V, W / scale,
                      'three of the corpus\'s own bumps at widths a, a^(1/2), a^(1/4); '
                      'coefficients solved for eq. (54) and the transform at zero')
    tf.coeffs = (float(c[0]), float(c[1]), float(c[2]))
    tf.cond = float(np.linalg.cond(A2))
    return tf


# ### ==============================================================================================
# ### THE CORPUS'S BANKED TRACE VALUES.
# ### ==============================================================================================
def atlas_cells():
    """### THE ROWS THE CORPUS BANKED, READ BACK FROM ITS OWN FILE. ### **NOT RE-COMPUTED.**"""
    rows = []
    for ln in io.open(ATLAS_BANK, encoding='utf-8'):
        ln = ln.strip()
        if ln:
            rows.append(json.loads(ln))
    return rows


ATLAS_CONVENTION = (
    "the atlas forms `A` as `INT hhat(u) kernel(u) du / (2 pi)` and closes its own arrangement as "
    "`residual = Z - (P - PR + A)`; ### **THAT ARRANGEMENT IS THE CONVENTION, AND IT IS THE ONE "
    "b233 ANNOTATED AND b235 RESTRICTED.**")


# ### ==============================================================================================
# ### THE SMEARED OPERATOR, TWO ROUTES.
# ### ==============================================================================================
def kernel_rows(fr, f, rows_x, cols_x, half=False):
    """### `A_ij = h * f(x_i/x_j) / sqrt(x_i x_j)` for a block of rows.

    ### `half` is ### **THE DISCRIMINATION ARM** ### -- a deliberately halved kernel, which must
    ### make every check below FAIL.
    """
    R = rows_x[:, None]
    C = cols_x[None, :]
    K = fr.h * f(R / C) / np.sqrt(R * C)
    return K * 0.5 if half else K


def smear_by_kernel(fr, f, g, half=False):
    """### `theta(f) g` BY THE KERNEL, over the whole grid."""
    out = np.zeros(fr.N)
    for s in range(0, fr.N, BLOCK):
        e = min(s + BLOCK, fr.N)
        out[s:e] = kernel_rows(fr, f, fr.x[s:e], fr.x, half) @ g
    return out


def smear_by_scaling(fr, f, g, nv=None):
    """### `theta(f) g` BY THE INSTRUMENT'S OWN `scaling`, integrated over `v = log lam`.

    ### **A SECOND AND INDEPENDENT ROUTE THROUGH THE SAME DEFINITION.** ### It never forms a kernel
    ### and never performs the substitution; it evaluates eq. (61) at each `lam` and integrates.
    """
    V = f.v if nv is None else np.linspace(f.v[0], f.v[-1], int(nv))
    acc = np.zeros((V.size, fr.N))
    for i, v in enumerate(V):
        lam = math.exp(v)
        acc[i] = float(f(np.array([lam]))[0]) * fr.scaling(lam, g)
    return np.trapezoid(acc, V, axis=0)


def route_agreement(fr, f, g, half=False):
    """### THE TWO ROUTES, COMPARED ### **WHERE THE TRACE ACTUALLY EVALUATES.**

    ### Returns `(rel_all, rel_hi, window_at_first_node)`.

    ### ### **AND THE SPLIT IS NOT A CONVENIENCE -- IT IS A PROPERTY OF THE KERNEL.** ### The
    ### kernel route integrates in `u`, and for output `x` the integrand is supported on
    ### `[x/a, a x]`, a window of width `x (a - 1/a)` carrying `x (a - 1/a) / h` grid points.
    ### ### **AT THE FIRST NODE `x = h/2` THAT COUNT IS BELOW ONE**, so the kernel quadrature there
    ### is not resolved at all, while the scaling route -- which integrates in `lambda` on the test
    ### function own grid -- is. ### **THE TWO ROUTES THEREFORE DISAGREE NEAR THE ORIGIN BY
    ### ### CONSTRUCTION, AND THAT DISAGREEMENT IS REPORTED RATHER THAN AVERAGED AWAY.**
    ### ### **IT REACHES NO NUMBER IN THIS ACT**, because condition one kills every coordinate with
    ### `x <= ALPHA` before the compression is applied, so `compressed_trace` never evaluates the
    ### kernel there. ### The gated figure is therefore `rel_hi`, over `x > ALPHA`, and `rel_all` is
    ### printed beside it so a reader can see the size of what was excluded and why.
    """
    k1 = smear_by_kernel(fr, f, g, half)
    k2 = smear_by_scaling(fr, f, g)
    d = np.abs(k1 - k2)
    m = max(float(np.max(np.abs(k2))), 1e-300)
    hi = fr.x > INS.ALPHA
    a = f.support
    return (float(np.max(d)) / m, float(np.max(d[hi])) / m,
            float(fr.x[0] * (a - 1.0 / a) / fr.h))


def compressed_trace(fr, sub, f, half=False):
    """### ### **`Tr(theta(f) S)` ON THE TRUNCATION.**

    ### Returns `(trace, uncompressed, correction)` where `uncompressed = Tr(A_HH)` is the trace
    ### over the half line `x > 1` with condition ONE imposed and condition TWO not, and
    ### `correction = Tr(Q^T A_HH Q)` is what condition two removes. ### **BOTH HALVES ARE RETURNED
    ### ### BECAUSE THEIR SIZES ARE THE FINDING**, not just their difference.
    """
    hi = sub['hi']
    xh = fr.x[hi]
    Q = sub['Q']
    one = np.ones_like(xh)
    diag = fr.h * f(one) / xh
    if half:
        diag = diag * 0.5
    uncompressed = float(diag.sum())
    corr = 0.0
    for s in range(0, xh.size, BLOCK):
        e = min(s + BLOCK, xh.size)
        K = kernel_rows(fr, f, xh[s:e], xh, half)
        corr += float(np.sum(Q[s:e] * (K @ Q)))
    return uncompressed - corr, uncompressed, corr


def identity_trace(fr, sub):
    """### **THE POSITIVE CONTROL THE ORDER NAMES.** ### A scaling by the identity alone is the
    ### identity operator, so the same trace must return `Tr(S)` -- the truncation's DIMENSION.

    ### It goes through the SAME two terms as `compressed_trace`: the diagonal of `A_HH`, which for
    ### the identity is `free`, minus `Tr(Q^T Q)`, which for orthonormal columns is `rank`.
    """
    Q = sub['Q']
    free = int(sub['hi'].sum())
    corr = float(np.sum(Q * Q))
    return free - corr, free, corr


# ### ==============================================================================================
# ### THE FIXTURES. ### **EVERY ARM MUST BE ABLE TO REPORT THE OTHER ANSWER.**
# ### ==============================================================================================
def self_test(verbose=False):
    """### ### **THE FIXTURES RUN AT A CELL THE CORPUS NEVER BANKED (`a = 1.75`), ON PURPOSE.**

    ### The order fixes this act's bar in a SEALED registration before any value exists. ### A
    ### fixture that exercised the machinery at one of the atlas's own cells would have produced
    ### exactly such a value, in a self-test, before the seal. ### **SO THE FIXTURES USE A
    ### ### PARAMETER THAT IS NOT IN `data/carto_atlas.jsonl`**, and nothing they print can be read
    ### as this act's answer.
    """
    ok, lines = [], []

    def note(s):
        lines.append(s)

    a = FIXTURE_A
    bp = corpus_bump(a)
    mz = mean_zero_variant(a)

    # ### (i) the corpus's bump has integral ONE, in the source's own measure.
    i1 = bp.at_zero()
    ok.append(abs(i1 - 1.0) < 1e-10)
    note('(i)    corpus bump, INT f d*rho = %.12f' % i1)

    # ### (ii) ### **AND THE MEAN-ZERO VARIANT HAS INTEGRAL ZERO** -- the transform at zero.
    i2 = mz.at_zero()
    ok.append(abs(i2) < 1e-10)
    note('(ii)   mean-zero variant, INT f d*rho = %.3e' % i2)

    # ### (iii) ### **THE SOURCE'S eq. (54): the variant satisfies it and the corpus's bump does
    # ### NOT.** ### The second half is the arm -- a class test that everything passes is not one.
    m_bp = bp.vanishing_54()
    m_mz = mz.vanishing_54()
    ok.append(abs(m_mz[0]) < 1e-10 and abs(m_mz[1]) < 1e-10 and abs(m_bp[0]) > 1e-3)
    note('(iii)  eq. (54): bump %.6f / %.6f ; variant %.3e / %.3e'
         % (m_bp[0], m_bp[1], m_mz[0], m_mz[1]))

    # ### (iv) both vanish outside the cell's support, so the source's support condition is a
    # ### property of the function and not of the quadrature.
    out = float(np.max(np.abs(bp(np.array([a * 1.01, 1.0 / (a * 1.01)])))))
    out2 = float(np.max(np.abs(mz(np.array([a * 1.01, 1.0 / (a * 1.01)])))))
    ok.append(out == 0.0 and out2 == 0.0)
    note('(iv)   outside the support : %.1e / %.1e' % (out, out2))

    fr = INS.Frame(256, 8.0, 64)
    sub = fr.subspace()

    # ### (v) ### **THE ORDER'S POSITIVE CONTROL** -- the identity recovers the dimension EXACTLY.
    tr_i, free_i, corr_i = identity_trace(fr, sub)
    ok.append(abs(tr_i - sub['dim']) < 1e-9)
    note('(v)    identity trace %.9f against dim %d (free %d, rank-term %.6f)'
         % (tr_i, sub['dim'], free_i, corr_i))

    # ### (vi) ### **THE TWO SMEARING ROUTES AGREE WHERE THE TRACE EVALUATES.** ### The kernel and
    # ### the instrument's own `scaling` are independent paths through eq. (61) and the
    # ### substitution. ### The gated figure is over `x > ALPHA`; the whole-grid figure is carried
    # ### beside it and is larger, for the reason `route_agreement` states in its own docstring.
    g = np.exp(-(fr.x - 3.0) ** 2)
    rel_all, rel, nwin = route_agreement(fr, bp, g)
    ok.append(rel < 1e-4)
    note('(vi)   kernel vs scaling route : %.3e over x > %g ; %.3e over the whole grid ; '
         'u-window at the first node holds %.3f point(s)' % (rel, INS.ALPHA, rel_all, nwin))

    # ### (vii) ### **AND THEY DISAGREE UNDER A HALVED KERNEL.** ### A route agreement that cannot
    # ### fail is not a check.
    _ra, rel_bad, _nw = route_agreement(fr, bp, g, half=True)
    ok.append(rel_bad > 1e-1)
    note('(vii)  the same, with the kernel deliberately halved : %.3e' % rel_bad)

    # ### (viii) the kernel is SYMMETRIC for an even test function, which is what makes the
    # ### compressed trace real and the operator self-adjoint.
    K = kernel_rows(fr, bp, fr.x, fr.x)
    sym = float(np.max(np.abs(K - K.T)))
    ok.append(sym < 1e-12)
    note('(viii) kernel symmetry, worst |K - K^T| : %.3e' % sym)

    # ### (ix) ### **AND THE TRACE ROUTINE ANSWERS TO THE KERNEL**: halving it halves the trace.
    t_a = compressed_trace(fr, sub, bp)[0]
    t_b = compressed_trace(fr, sub, bp, half=True)[0]
    ok.append(abs(t_b - t_a / 2.0) < 1e-9 * max(abs(t_a), 1.0) and abs(t_a) > 1e-9)
    note('(ix)   trace %.9f ; halved kernel %.9f' % (t_a, t_b))

    # ### (x) the block size does not decide anything -- the trace is the same when the operator
    # ### is applied in one block or in many.
    global BLOCK
    keep = BLOCK
    BLOCK = 7
    t_c = compressed_trace(fr, sub, bp)[0]
    BLOCK = keep
    ok.append(abs(t_c - t_a) < 1e-9 * max(abs(t_a), 1.0))
    note('(x)    same trace at block 7 : %.9f' % t_c)

    if verbose:
        for s in lines:
            print('    ' + s)
    return all(ok), ok, lines


if __name__ == '__main__':
    good, arms, ls = self_test(verbose=True)
    print('  arms : %s  %s' % (arms, 'PASS' if good else '### FAIL ###'))
    sys.exit(0 if good else 1)
