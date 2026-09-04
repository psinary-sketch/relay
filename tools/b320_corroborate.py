# -*- coding: utf-8 -*-
"""b320_corroborate.py -- THE WEIL SIDE, BY A SECOND AND INDEPENDENT ROUTE.

### ### **WHY THIS EXISTS, AND IT IS NOT DECORATION.** ### This act's `W_infinity` is built from the
### source's (38) and (53): a real-side Hadamard integral with a principal-value constant measured
### from a Gaussian pairing. ### **TWO DEFECTS LIVED IN THAT ONE FUNCTION AND EACH SURVIVED A ROUND
### ### OF FIXTURES.** ### The first made the act's control FAIL; the second put `1.9e9` into a
### data table. ### A single route with good fixtures was not enough.

### ### ### **SO THE SAME QUANTITY IS COMPUTED A SECOND WAY, SHARING NO CODE WITH THE FIRST.**
### The archimedean term of the explicit formula is a transform-side integral against the digamma
### kernel, ### `A(f) = (1/2 pi) INT f-hat(u) [Re psi(1/4 + i u/2) - log pi] du`, and the corpus's
### own `tools/e16/carto_atlas.py` forms exactly that kernel in `def kernel`. ### **THIS FILE READS
### ### THAT KERNEL FROM ITS EMITTING FILE** and pairs it with `f-hat` computed by b318's `fhat`.
### ### Nothing in this path touches the Hadamard integral, the split radius, or `C_R`.

### ### **WHAT AN AGREEMENT HERE DOES AND DOES NOT BUY.** ### It does not make either route right.
### ### **IT MAKES A SILENT DEFECT IN EITHER ONE VISIBLE**, which is the only thing a second route
### ever buys, and it is the thing this act found it needed.
### ### **AND THE TRANSFORM RANGE IS ITS OWN HAZARD:** ### `f-hat` for these test functions carries
### mass far out in `u`, and a first diagnostic truncated at `u = 600` on a grid of spacing `10` --
### far too coarse to resolve `f-hat`, which varies on scale `2`. ### **THAT COARSE GRID LOOKED
### ### STABLE BECAUSE IT WAS EQUALLY WRONG AT EVERY RANGE.** ### The range and the spacing are
### both declared below and the convergence in the range is printed.
"""
import io
import math
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, os.path.join(ROOT, 'tools', 'e16'))

import b317_smear as SM   # noqa: E402
import b318_square as SQ  # noqa: E402
import b320_weil as WE    # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

DU = 0.1            # ### `f-hat` varies on scale `1/(2L) ~ 2`; this resolves it by twenty
UMAX = 1500.0       # ### and the convergence in this range is printed rather than assumed
NVT = 32768         # ### `w` is RE-GRIDDED to this many nodes before transforming: see below
BLOCK = 64

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def kernel(U):
    """### ### **THE CORPUS'S OWN DIGAMMA KERNEL, READ FROM ITS EMITTING FILE.**

    ### `tools/e16/carto_atlas.py`, `def kernel`: ### *"Re psi(1/4 + i u/2) - log pi"*. ### It is
    ### re-formed here at this act's own `u` grid rather than reused at the atlas's, because the
    ### atlas's grid was built for the atlas's test function.
    """
    from mpmath import mp, digamma, mpc, re as mre
    mp.dps = 15
    return (np.array([float(mre(digamma(mpc(0.25, uu / 2.0)))) for uu in U])
            - math.log(math.pi))


def fhat_blocked(v, w, t, block=BLOCK, nvt=NVT):
    """### `INT w(v) cos(u v) dv`, blocked so the transform matrix is never formed whole.

    ### ### **AND `w` IS RE-GRIDDED FIRST, WHICH IS A CHOICE AND NOT AN ACCIDENT.** ### `f` is
    ### carried on ~200000 nodes across a support of width ~1.4, i.e. `dv ~ 7e-06`. ### The
    ### highest frequency this integral ever sees is `u = %g`, which needs `dv <= 2 pi / (10 u)
    ### ~ 4e-04`. ### The native grid is over-resolved by three orders and the full transform
    ### matrix would be `3e04 x 2e05`. ### **THE RE-GRID IS TESTED, NOT ASSUMED**: fixture (v)
    ### runs the whole integral at `NVT` and at `2 NVT` and requires them to agree.
    """ % UMAX
    vv = np.linspace(v[0], v[-1], int(nvt))
    ww = np.interp(vv, v, w, left=0.0, right=0.0)
    out = np.empty(t.size)
    for s0 in range(0, t.size, block):
        e0 = min(s0 + block, t.size)
        out[s0:e0] = np.trapezoid(np.cos(np.outer(t[s0:e0], vv)) * ww[None, :], vv, axis=1)
    return out


def digamma_side(f, umax=UMAX, du=DU, ker=None, U=None, nvt=NVT):
    """### `A(f)` -- the archimedean term by the transform-side route."""
    if U is None:
        U = np.arange(-umax, umax + du / 2.0, du)
    if ker is None:
        ker = kernel(U)
    return float(np.trapezoid(fhat_blocked(f.v, f.w, U, nvt=nvt) * ker, U) / (2.0 * math.pi))


def self_test(verbose=False):
    ok, lines = [], []

    def note(s):
        lines.append(s)

    g = SM.mean_zero_variant(SM.FIXTURE_A)
    f = SQ.autocorrelation(g)
    w = WE.weil(f)[0]

    # ### (i) the two routes agree at a NON-BANKED cell.
    U = np.arange(-UMAX, UMAX + DU / 2.0, DU)
    K = kernel(U)
    A = digamma_side(f, U=U, ker=K)
    ok.append(abs(A - w) < 1e-3 * max(abs(w), 1.0))
    note('(i)    at a = %g : (38) route %.9f ; digamma route %.9f ; difference %.3e'
         % (SM.FIXTURE_A, w, A, abs(A - w)))

    # ### (ii) ### **AND THE AGREEMENT CAN FAIL** -- a halved kernel misses by half. ### A second
    # ### route that agreed with anything would corroborate nothing.
    Ab = digamma_side(f, U=U, ker=0.5 * K)
    ok.append(abs(Ab - w) > 1e-1 * max(abs(w), 1.0))
    note('(ii)   the same with the kernel deliberately halved : %.9f ; difference %.3e'
         % (Ab, abs(Ab - w)))

    # ### (iii) ### **THE RANGE IS CONVERGED, AND SHOWN SO RATHER THAN ASSUMED.**
    a1 = digamma_side(f, umax=600.0)
    ok.append(abs(a1 - A) < 1e-6 * max(abs(A), 1.0))
    note('(iii)  range convergence: u to 600 gives %.9f against u to %.0f giving %.9f'
         % (a1, UMAX, A))

    # ### (iv) ### **AND A COARSE GRID IS WRONG AND MUST LOOK WRONG.** ### The first diagnostic in
    # ### this act used `du = 10` and it looked stable at every range because it was equally wrong
    # ### at each; this arm makes that visible.
    a2 = digamma_side(f, du=10.0)
    ok.append(abs(a2 - A) > 1e-3 * max(abs(A), 1.0))
    note('(iv)   at du = 10 the same integral gives %.9f -- wrong by %.3e, as it must be'
         % (a2, abs(a2 - A)))

    # ### (v) ### **THE RE-GRID IS CONVERGED.** ### Halving `dv` must not move the answer.
    a3 = digamma_side(f, U=U, ker=K, nvt=2 * NVT)
    ok.append(abs(a3 - A) < 1e-6 * max(abs(A), 1.0))
    note('(v)    re-grid convergence: %d nodes gives %.9f against %d giving %.9f ; diff %.3e'
         % (NVT, A, 2 * NVT, a3, abs(a3 - A)))

    if verbose:
        for s in lines:
            print('    ' + s)
    return all(ok), ok, lines


def main():
    good, arms, ls = self_test()
    rec('=' * 100)
    rec('b320_corroborate.py -- THE WEIL SIDE, BY A SECOND AND INDEPENDENT ROUTE.')
    rec('=' * 100)
    rec('  ### FIXTURES : %s  %s' % (arms, 'PASS' if good else '### FAIL ###'))
    for s in ls:
        rec('    ' + s)
    if not good:
        return 1
    rec('')
    rec('  ### **THE TWO ROUTES SHARE NO CODE.** ### (38) is a real-side Hadamard integral with a')
    rec('  ### measured principal-value constant; the digamma route is a transform-side integral')
    rec('  ### against the corpus\'s own kernel. ### **NEITHER CHECKS THE OTHER\'S ARITHMETIC; EACH')
    rec('  ### ### WOULD EXPOSE A SILENT DEFECT IN THE OTHER**, which is what this act needed.')
    rec('')
    rec('    %-6s %-9s %-18s %-18s %-14s'
        % ('a', 'supp ok', 'W_inf by (38)', 'A by digamma', 'difference'))
    U = np.arange(-UMAX, UMAX + DU / 2.0, DU)
    K = kernel(U)
    worst = 0.0
    for r in SM.atlas_cells():
        a = r['a']
        g = SM.mean_zero_variant(a)
        f = SQ.autocorrelation(g)
        w = WE.weil(f)[0]
        A = digamma_side(f, U=U, ker=K)
        worst = max(worst, abs(A - w))
        rec('    %-6g %-9s %-18.9f %-18.9f %-14.3e'
            % (a, 'YES' if a <= SQ.SUPPORT_G_HI else 'no', w, A, abs(A - w)))
    rec('    ### ### **WORST DIFFERENCE ACROSS ALL THIRTEEN CELLS : %.3e**' % worst)
    rec('    ### **THAT IS THE CORROBORATION, AND IT IS ALL IT IS.** ### It does not make either')
    rec('    ### route right; it makes a silent defect in either one visible.')
    rec('=' * 100)
    return 0


if __name__ == '__main__':
    code = main()
    io.open(os.path.join(ROOT, 'data', 'b320_corroboration.txt'), 'w',
            encoding='utf-8', newline='\n').write('\n'.join(LINES) + '\n')
    sys.exit(code)
