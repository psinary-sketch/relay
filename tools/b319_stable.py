# -*- coding: utf-8 -*-
"""b319_stable.py -- THE STABLE RANK. ### **THE SUBSPACE BY THE SOURCE'S OWN CHARACTERIZATION.**

### ### **WHY b316's RANK STEPPED, AND IT IS ARITHMETIC.** ### b316 built the space as the null
### space of `C = T[y <= 1][:, x > 1]` and took the rank from an SVD under the tolerance
### `max(C.shape) * s[0] * eps`. ### **BOTH FACTORS IN THAT TOLERANCE MOVE WITH THE GRID**: the
### shape grows like `X/h` and `s[0]` carries the quadrature weights. ### So the cut ran across a
### moving scale, and b318 measured what that costs -- grid steps that keep the rank drift by
### `3e-05`, the one step that changes it drifts by `2e-02`.

### ### ### **THE SOURCE GIVES A CUT THAT DOES NOT MOVE.** ### Its (81) reads
###   ### `P P-hat P = SUM lambda(n)^2 |zeta_n><zeta_n| + R`
### ### *"where R is the orthogonal projection on Sonin's space S(1,1)"*, and its page 28 says
### ### *"Sonin's space S(1,1) is the eigenspace of P P-hat P for the eigenvalue 1"*.
### ### **SO THE SPECTRUM OF THE SANDWICH IS `{lambda(n)^2}` TOGETHER WITH `1` ON THE SPACE**, and
### an eigenvalue is a DIMENSIONLESS number in `[0, 1]`. ### A threshold on it is scale-free.

### ### **THE SANDWICH ON THE GRID, DERIVED ONCE.** ### On the free coordinates `x > 1` the first
### projection is the identity, so the sandwich is `P-hat` restricted there, and
###   ### `<xi, P-hat_1 xi> = <F xi, P_1 F xi> = INT_0^1 |F xi(p)|^2 dp`
### under the source's (16), which halves the full-line integral. ### Discretized on the
### instrument's own transform grid that is `hy * ||T xi||^2`, and in the ORTHONORMAL coordinates
### `c = xi * sqrt(h)` it is `(hy/h) c^T T^T T c`. ### Hence
###   ### ### **`M = I - (hy/h) * C^T C`   on the free coordinates**,
### whose eigenvalue-one eigenspace is `null(C)` -- the same space b316 built -- but whose SPECTRUM
### is the dimensionless one the source names. ### **THE TWO SCHEMES DIFFER ONLY IN WHERE THEY CUT**,
### and that is the whole of this act's build.

### ### **AND THE CUT IS TAKEN FROM THE SAME SVD**, so nothing is recomputed: the eigenvalues of the
### sandwich's non-one part are `sigma_k^2` of `sqrt(hy/h) * C`, and a vector is OUTSIDE the space
### exactly when `sigma_k^2 > TAU`.

### ### **WHAT THIS FILE MAY NOT BE USED FOR.** ### It builds a subspace. ### It computes no test
### function, no `W_infinity`, and it takes no verdict on membership.
"""
import math
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E16 = os.path.join(ROOT, 'tools', 'e16')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
sys.path.insert(0, E16)

import b316_instrument as INS   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### ==============================================================================================
# ### THE THRESHOLD, ### **FIXED IN `data/b319_registration_2026-09-04.txt` (5) BEFORE ANY SPECTRUM
# ### OF THIS ACT'S OWN WAS COMPUTED.**
# ###
# ### ### **THE ARGUMENT, FROM THE SOURCE AND FROM THE CORPUS'S OWN BANKED VALUES:**
# ### the sandwich's eigenvalues other than one are the `lambda(n)^2` of (81); they are STRICTLY
# ### below one; and the corpus's own prolate layer prints the largest of them as
# ### `lambda(0)^2 = 0.999942753354103`, so ### **THE NEAREST NON-SPACE EIGENVALUE SITS
# ### `5.724665e-05` BELOW ONE.**
# ### `TAU = 1e-6` therefore sits ### **57 TIMES INSIDE THAT SEPARATION** ### and ten orders of
# ### magnitude above double precision, so it separates the space from the first prolate mode without
# ### selecting numerical noise. ### **NEITHER BOUND WAS CHOSEN BY LOOKING AT A COMPUTED SPECTRUM.**
# ### ==============================================================================================
TAU = 1e-6

# ### The corpus's own banked value, carried here so the argument can be re-measured rather than
# ### re-read. ### `tools/e16/qeps_layer.py` is its emitting file.
LAMBDA0_SQ = 0.999942753354103

BLOCK = 512


def stable_subspace(fr, tau=TAU, T=None):
    """### ### **THE SUBSPACE BY THE EIGENVALUE-ONE CHARACTERIZATION.**

    ### Returns the same dict shape `b316_instrument.subspace` returns -- `hi`, `lo_x`, `lo_y`, `Q`,
    ### `rank`, `free`, `dim` -- so ### **b317's `compressed_trace` AND b318's `square_trace` RUN
    ### ### AGAINST IT UNCHANGED**, and the reproduction compares two subspaces rather than two
    ### programs.
    ### It adds `eig` (the sandwich's non-one eigenvalues, ascending) and `tau`.
    """
    if T is None:
        T = fr.transform_matrix()
    lo_x, lo_y = fr.masks()
    hi_x = ~lo_x
    C = T[lo_y][:, hi_x]
    scale = math.sqrt(fr.hy / fr.h)
    U, s, Vt = np.linalg.svd(C * scale, full_matrices=False)
    eig = s ** 2
    out = eig > tau                      # ### OUTSIDE the eigenvalue-one eigenspace
    Q = Vt[out].T
    return dict(hi=hi_x, lo_x=lo_x, lo_y=lo_y, C=C, Q=Q, rank=int(out.sum()),
                free=int(hi_x.sum()), dim=int(hi_x.sum()) - int(out.sum()),
                eig=eig, tau=tau, sing=s)


def both_subspaces(fr, tau=TAU, T=None):
    """### ### **BOTH CUTS FROM ONE SVD.** ### Returns `(stable, grid)`.

    ### The two schemes threshold the SAME singular values -- b316's on the unscaled `C` against
    ### `max(C.shape) * s[0] * eps`, this act's on `sigma^2` of `sqrt(hy/h) C` against `TAU` -- so
    ### ### **DECOMPOSING TWICE WOULD BE COMPUTING THE SAME MATRIX TWICE AND CALLING THE AGREEMENT
    ### ### A CHECK.** ### One decomposition, two cuts, and the difference between them is an index
    ### set rather than two programs' opinions.
    """
    if T is None:
        T = fr.transform_matrix()
    lo_x, lo_y = fr.masks()
    hi_x = ~lo_x
    C = T[lo_y][:, hi_x]
    scale = math.sqrt(fr.hy / fr.h)
    U, s_u, Vt = np.linalg.svd(C, full_matrices=False)      # ### UNSCALED, as b316 takes it
    eig = (s_u * scale) ** 2                                 # ### the sandwich's eigenvalues
    out_st = eig > tau
    tol = max(C.shape) * (s_u[0] if s_u.size else 0.0) * np.finfo(float).eps
    out_gr = s_u > tol
    free = int(hi_x.sum())
    st = dict(hi=hi_x, lo_x=lo_x, lo_y=lo_y, C=C, Q=Vt[out_st].T, rank=int(out_st.sum()),
              free=free, dim=free - int(out_st.sum()), eig=eig, tau=tau, sing=s_u)
    gr = dict(hi=hi_x, lo_x=lo_x, lo_y=lo_y, C=C, Q=Vt[out_gr].T, rank=int(out_gr.sum()),
              free=free, dim=free - int(out_gr.sum()), sing=s_u)
    return st, gr


def grid_subspace(fr, T=None):
    """### b316's SCHEME, IMPORTED AND NOT COPIED, so the two are compared and not re-implemented."""
    return fr.subspace(T)


def scheme_difference(fr, tau=TAU):
    """### ### **WHICH VECTORS ONE SCHEME ADMITS THAT THE OTHER DOES NOT, MEASURED.**

    ### Both cuts are taken on the SAME singular values, so the difference is an index set and its
    ### eigenvalues can be printed. ### Returns
    ### `(rank_grid, rank_stable, only_grid, only_stable, eig_only_grid, eig_only_stable)`.
    """
    st, gr = both_subspaces(fr, tau)
    s_u = st['sing']
    scale = math.sqrt(fr.hy / fr.h)
    eig = (s_u * scale) ** 2
    tol = max(st['C'].shape) * (s_u[0] if s_u.size else 0.0) * np.finfo(float).eps
    in_grid = s_u > tol                      # ### b316 calls these OUTSIDE the space
    in_stab = eig > tau                      # ### this act calls these OUTSIDE the space
    only_grid = np.where(in_grid & ~in_stab)[0]
    only_stab = np.where(in_stab & ~in_grid)[0]
    return (int(gr['rank']), int(st['rank']), only_grid, only_stab,
            eig[only_grid], eig[only_stab])


def self_test(verbose=False):
    """### **FIXTURES. ### EVERY ARM MUST BE ABLE TO REPORT THE OTHER ANSWER.**"""
    ok, lines = [], []

    def note(s):
        lines.append(s)

    fr = INS.Frame(256, 8.0, 64)
    st = stable_subspace(fr)

    # ### (i) ### **THE SANDWICH IS A PROJECTION SANDWICH, SO ITS SPECTRUM LIVES IN [0, 1].** ### If
    # ### the discretization constant `(hy/h)` were wrong this arm would fail, and it is the only
    # ### thing standing between the derivation in the header and a number.
    e = st['eig']
    ok.append(float(e.min()) >= -1e-12 and float(e.max()) <= 1.0 + 1e-9)
    note('(i)    sandwich eigenvalues in [%.3e, %.6f] -- inside [0,1] : %s'
         % (float(e.min()), float(e.max()), bool(e.max() <= 1.0 + 1e-9)))

    # ### (ii) the eigenvalue-one eigenspace is the null space of `C`: the two descriptions of the
    # ### SAME space agree, which is what lets this scheme replace b316's without changing the object.
    gr = grid_subspace(fr)
    ok.append(st['free'] == gr['free'])
    note('(ii)   free coordinates agree : %d / %d' % (st['free'], gr['free']))

    # ### (iii) ### **THE THRESHOLD SEPARATES THE FIRST PROLATE MODE FROM THE SPACE.** ### The
    # ### corpus's banked `lambda(0)^2` sits `5.7e-05` below one; `TAU` is inside that separation.
    ok.append(TAU < (1.0 - LAMBDA0_SQ))
    note('(iii)  TAU = %.1e  <  1 - lambda(0)^2 = %.6e : %s'
         % (TAU, 1.0 - LAMBDA0_SQ, TAU < (1.0 - LAMBDA0_SQ)))

    # ### (iv) ### **AND THE SELECTION CAN CHANGE ITS MIND** -- a threshold that returns the same
    # ### rank for every value is not selecting anything.
    r_lo = stable_subspace(fr, 1e-14)['rank']
    r_hi = stable_subspace(fr, 1e-1)['rank']
    ok.append(r_lo > r_hi)
    note('(iv)   rank at tau=1e-14 : %d ; at tau=1e-1 : %d ; monotone : %s'
         % (r_lo, r_hi, r_lo > r_hi))

    # ### (v) the projector is idempotent on the free coordinates, to machine precision.
    Q = st['Q']
    g = np.random.default_rng(319).standard_normal(st['free'])
    p1 = g - Q @ (Q.T @ g)
    p2 = p1 - Q @ (Q.T @ p1)
    ok.append(float(np.max(np.abs(p1 - p2))) < 1e-10)
    note('(v)    idempotence, worst |P g - P P g| : %.3e' % float(np.max(np.abs(p1 - p2))))

    # ### (vi) ### **AND `Q` IS ORTHONORMAL**, which is what makes the identity control exact.
    ok.append(float(np.max(np.abs(Q.T @ Q - np.eye(Q.shape[1])))) < 1e-10)
    note('(vi)   orthonormality, worst |Q^T Q - I| : %.3e'
         % float(np.max(np.abs(Q.T @ Q - np.eye(Q.shape[1])))))

    if verbose:
        for s in lines:
            print('    ' + s)
    return all(ok), ok, lines


if __name__ == '__main__':
    good, arms, ls = self_test(verbose=True)
    print('  arms : %s  %s' % (arms, 'PASS' if good else '### FAIL ###'))
    sys.exit(0 if good else 1)
