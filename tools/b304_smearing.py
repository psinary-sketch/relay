# -*- coding: utf-8 -*-
"""b304_smearing.py -- THE FINITE ANALOGUE OF THE SOURCE'S MOVE, COMPRESSED AND COMPUTED.

### THE SOURCE'S MOVE, IN ITS OWN WORDS (CC, arXiv:2006.13771, Introduction, read at content this
### act):
### ### **"Even though the scaling action `theta` does not restrict to this subspace, one can
### ### associate to a test function `f in C_c^infinity(R*_+)` the trace `Tr(theta(f) S)`, and one
### ### sees that this functional is positive definite by construction."**
### `S` there is ### **"the orthogonal projection of the Hilbert space `L^2(R)_ev` ... on the
### subspace of functions which, together with their Fourier transform, vanish identically in the
### interval `[-1,1]`"** -- Sonin's space.

### ### **THE FINITE ANALOGUE, BUILT FROM THAT DESCRIPTION AND NOT BY ANALOGY WITH ANYTHING ELSE:**
###   ### the place's multiplicative group ..... `(Z/N)^x`, `N = p^{2n}`, the model's units
###   ### the scaling action ................... `(theta(t) f)(m) = f(t^{-1} m)`, so
###                                              `theta(t) e_j = e_{t j}`
###   ### the test function .................... `f` on that group; `theta(f) = SUM_t f(t) theta(t)`
###   ### the projection ...................... `Pi`, orthogonal projection onto `Son(p,n)`
###   ### ### **THE OBJECT: `T(f) := Tr(theta(f) Pi)`.**

### ### **WHY `Pi` IS THE PROJECTION ONTO `Son` AND NOT ONTO THE SECTOR.** ### The source compresses
### by the projection onto ### SONIN'S SPACE ### , not onto a sector of it. ### **THE FAITHFUL
### ANALOGUE IS THEREFORE `Son(p,n)`'s PROJECTION**, and the sector refinement `E_1` is NOT computed
### here -- its projector `P_1 = (1 + M + M^2 + M^3)/4` carries `zeta_N` in every entry, so it is
### not a rational matrix and this file's exactness would be lost. ### **DECLARED, NOT SKIPPED.**

### ### ### **THE ESCAPED-MASS ARTIFACT, AND IT DECIDES WHAT THIS FILE MAY COMPUTE.**
### b21 named it and b284 met it: scaling by `p` sends `f` to a function whose genuine support is
### `p^{-n-1} Z_p`, ### **STRICTLY BIGGER THAN `p^{-n} Z_p`** -- it ESCAPES the level -- and
### ### **"THE MODEL'S mod-N WRAPAROUND IS EXACTLY THIS ESCAPED MASS FOLDED BACK IN."**
### ### **SO THE MODEL CANNOT CARRY THE NON-UNIT PART OF `Q_p^x` WITHOUT THE ARTIFACT.**
### ### **BUT MULTIPLICATION BY A UNIT `t` IS A BIJECTION OF `Z/N` AND PRESERVES EVERY LEVEL: ###
### ### NOTHING ESCAPES AND NOTHING IS FOLDED.** ### That is not a hope -- it is checked below, by
### verifying that `m -> t m` is a permutation of `Z/N` at every `t` used.
### ### ### **THEREFORE THIS FILE COMPUTES THE `Z_p^x` PART EXACTLY AND REFUSES THE `p^Z` PART**,
### and says per cell which is which. ### **AND THE PART IT REFUSES IS THE PART THAT CARRIES THE
### SCALING**, which is a finding and not an excuse; the bank states it as one.

### ### **NO FLOAT. ### `Fraction` AND `int` ONLY.** ### Every number below is exact.
"""
import os
import sys
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b303_family as FAM  # noqa: E402  ### Son's conditions are READ from b303, never copied

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CELLS = [(2, 1), (2, 2), (3, 1), (3, 2), (5, 1), (7, 1)]


# ### ==============================================================================================
# ### THE PROJECTION, EXACTLY. ### **GRAM-SCHMIDT OVER `Q`, SO `Pi` IS A RATIONAL MATRIX.**
# ### ==============================================================================================
def orthogonalise(basis):
    """### Gram-Schmidt over `Q`. ### Returns orthogonal vectors spanning the same space."""
    out = []
    for v in basis:
        w = list(v)
        for u in out:
            nu = sum(x * x for x in u)
            if nu == 0:
                continue
            c = sum(a * b for a, b in zip(w, u)) / nu
            if c != 0:
                w = [a - c * b for a, b in zip(w, u)]
        if any(x != 0 for x in w):
            out.append(w)
    return out


def projector(basis, dim_n):
    """### `Pi = SUM_c (b_c b_c^T) / <b_c, b_c>` over an ORTHOGONAL basis. ### An `N x N` rational
    matrix. ### **BUILT ONCE PER CELL**, because every trace below is then `N` lookups."""
    orth = orthogonalise(basis)
    P = [[Fraction(0)] * dim_n for _ in range(dim_n)]
    for b in orth:
        nb = sum(x * x for x in b)
        for i in range(dim_n):
            if b[i] == 0:
                continue
            bi = b[i] / nb
            row = P[i]
            for j in range(dim_n):
                if b[j] != 0:
                    row[j] += bi * b[j]
    return P, len(orth)


def trace_scaled(P, t, N):
    """### ### **`Tr(theta(t) Pi) = SUM_m Pi[t^{-1} m][m]`.**

    ### DERIVED, NOT GUESSED: ### `theta(t) e_j = e_{t j}`, so `theta(t)[m][k] = [k = t^{-1} m]`,
    ### hence `(theta(t) Pi)[m][m] = Pi[t^{-1} m][m]`. ### **THE INVERSE IS TAKEN MOD `N` AND ITS
    ### EXISTENCE IS CHECKED BY THE CALLER** -- a `t` sharing a factor with `N` has no inverse and
    ### is exactly the escaping case this file refuses.
    """
    tinv = pow(t, -1, N)
    return sum(P[(tinv * m) % N][m] for m in range(N))


def fixed_points(t, N):
    """### `#{ m : t^{-1} m = m } = #{ m : (t-1) m = 0 mod N } = gcd(t-1, N)`.

    ### ### **COUNTED DIRECTLY, AND COMPARED WITH THE `gcd` FORMULA AS A CONTROL** -- two routes to
    ### one integer, and if they disagree the permutation is not the one the derivation describes.
    """
    return sum(1 for m in range(N) if (t * m - m) % N == 0)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def is_permutation(t, N):
    """### **DOES `m -> t m` PERMUTE `Z/N`?** ### This is the escaped-mass test, made mechanical:
    a unit permutes and nothing is folded; a non-unit collapses and the model folds the escaped
    mass back onto the ball."""
    return len(set((t * m) % N for m in range(N))) == N


def shell(p, n, j, N):
    """### THE VALUATION SHELL `{ m : v_p(m) = j }`, as a 0/1 vector. ### `j = 2n` is `{0}`."""
    return [Fraction(1) if FAM.vp(p, m) == j else Fraction(0) for m in range(N)]


def invariant_reason(p, n, N, basis):
    """### ### **WHY THE SMEARED VALUE IS ZERO -- DERIVED, THEN CHECKED.**

    ### `SUM_{t in U} theta(t) = |U| * Q`, where `Q` is the orthogonal projection onto the
    ### `U`-INVARIANTS, because `theta` restricted to `U = (Z/N)^x` is a representation of a finite
    ### group and the averaged sum of a representation is the projection onto its fixed vectors.
    ### So `T = |U| * Tr(Q Pi)`, and for two orthogonal projections `Tr(Q Pi) = 0` iff their ranges
    ### are ORTHOGONAL.
    ### ### **THE INVARIANTS ARE SPANNED BY THE VALUATION SHELLS** -- the orbits of `m -> t m` on
    ### `Z/N` are exactly the sets of constant `v_p`.
    ### ### **AND EVERY `Son` VECTOR IS ORTHOGONAL TO EVERY SHELL, FOR THE SPACE'S OWN TWO REASONS:**
    ###   ### a shell with `j >= n` sits inside the ball, where every `Son` vector VANISHES;
    ###   ### a shell with `j < n` is a UNION OF RESIDUE CLASSES MOD `p^n` (it is cut out by a
    ###     condition mod `p^{j+1}`, and `p^{j+1}` divides `p^n`), so the sum of a `Son` vector over
    ###     it is a sum of FIBER SUMS, each of which is zero by the transform condition.
    ### ### ### **SO THE ZERO IS NOT AN ACCIDENT OF THE CELLS. ### IT IS THE TWO DEFINING
    ### ### ### CONDITIONS OF `Son`, ONE PER SHELL RANGE.**

    ### Returns `(orthogonal, shells_checked, shell_is_union_of_classes)`.
    """
    orth, unions = True, True
    for j in range(0, 2 * n + 1):
        s = shell(p, n, j, N)
        if all(x == 0 for x in s):
            continue
        for v in basis:
            if sum(a * b for a, b in zip(s, v)) != 0:
                orth = False
        if j < n:
            # ### the shell must be a union of classes mod p^n, or the argument above does not run
            mod = p ** n
            classes = {}
            for m in range(N):
                classes.setdefault(m % mod, []).append(s[m])
            for _r, vals in classes.items():
                if len(set(vals)) != 1:
                    unions = False
    return orth, 2 * n + 1, unions


def self_test(verbose=True):
    out, bad = [], 0

    def chk(lbl, got, exp):
        nonlocal bad
        ok = (got == exp)
        bad += 0 if ok else 1
        if verbose:
            print('  %-64s %-20s %s' % (lbl, '%s/%s' % (got, exp), 'YES' if ok else '### NO ###'))

    if verbose:
        print('  %-64s %-20s %s' % ('fixture', 'got/expected', 'agree'))
    # ### THE PROJECTOR, ON A SPACE SMALL ENOUGH TO CHECK BY HAND.
    P, r = projector([[Fraction(1), Fraction(0), Fraction(0)]], 3)
    chk('projector onto e0: rank 1', r, 1)
    chk('projector onto e0: Pi[0][0] = 1', P[0][0], Fraction(1))
    chk('projector onto e0: Pi[1][1] = 0', P[1][1], Fraction(0))
    chk('projector onto e0: trace = 1', sum(P[i][i] for i in range(3)), Fraction(1))
    # ### AN OBLIQUE BASIS: Gram-Schmidt must still give an ORTHOGONAL projector of the right rank.
    P2, r2 = projector([[Fraction(1), Fraction(1), Fraction(0)],
                        [Fraction(1), Fraction(0), Fraction(0)]], 3)
    chk('projector onto span(e0+e1, e0): rank 2', r2, 2)
    chk('projector onto that span: trace = 2', sum(P2[i][i] for i in range(3)), Fraction(2))
    chk('### and it is IDEMPOTENT',
        all(sum(P2[i][k] * P2[k][j] for k in range(3)) == P2[i][j]
            for i in range(3) for j in range(3)), True)
    chk('### and SYMMETRIC', all(P2[i][j] == P2[j][i] for i in range(3) for j in range(3)), True)
    # ### THE FIXED-POINT COUNT, BOTH ROUTES.
    chk('fixed points of t=1 mod 9 is all of Z/9', fixed_points(1, 9), 9)
    chk('and the gcd formula agrees at t=1', gcd(0, 9), 9)
    chk('fixed points of t=4 mod 9', fixed_points(4, 9), gcd(3, 9))
    chk('fixed points of t=2 mod 9 is 1', fixed_points(2, 9), 1)
    # ### THE PERMUTATION TEST, ### **BOTH POLARITIES, AND THIS IS THE ESCAPE TEST.**
    chk('a unit permutes Z/9', is_permutation(2, 9), True)
    chk('### a non-unit does NOT permute Z/9', is_permutation(3, 9), False)
    chk('### and 0 certainly does not', is_permutation(0, 9), False)
    return bad == 0


def main(argv):
    print('=' * 100)
    print('b304_smearing.py -- THE FINITE ANALOGUE, COMPRESSED. ### EXACT RATIONALS, NO FLOAT.')
    print('=' * 100)
    ok = self_test()
    print('  self-test : %s' % ('PASS' if ok else '### FAIL ###'))
    if not ok:
        print('  ### REFUSING TO REPORT A COMPUTATION FROM A SUITE THAT FAILS ITS OWN FIXTURES.')
        return 2
    print()
    print('  ### b303_family\'s SELF-TEST, RE-RUN HERE BEFORE ITS CONDITIONS ARE USED:')
    if not FAM.self_test(verbose=False):
        print('  ### REFUSING -- the imported condition builder fails its own fixtures.')
        return 2
    print('    b303_family self-test : PASS')

    fails = 0
    print()
    for (p, n) in CELLS:
        N = p ** (2 * n)
        rows = FAM.rows_member(p, n, 0, 0)          # ### Son(p,n) = the (0,0) member (b293/b303)
        basis = FAM.nullspace(rows, N)
        P, rank = projector(basis, N)

        dim_law = (p ** n - 1) ** 2
        tr = sum(P[i][i] for i in range(N))
        idem = all(sum(P[i][k] * P[k][j] for k in range(N)) == P[i][j]
                   for i in range(0, N, max(1, N // 8)) for j in range(0, N, max(1, N // 8)))
        symm = all(P[i][j] == P[j][i] for i in range(N) for j in range(N))
        fixes_basis = all(
            all(sum(P[i][j] * v[j] for j in range(N)) == v[i] for i in range(N))
            for v in basis[:3])
        # ### THE NEGATIVE CONTROL: an off-ball spike is NOT fixed by Pi.
        off = next(m for m in range(N) if m not in FAM.ball_corpus(p, n))
        spike = [Fraction(1) if m == off else Fraction(0) for m in range(N)]
        proj_spike = [sum(P[i][j] * spike[j] for j in range(N)) for i in range(N)]
        spike_moved = (proj_spike != spike)

        units = [t for t in range(N) if gcd(t, N) == 1]
        all_perm = all(is_permutation(t, N) for t in units)
        traces = {t: trace_scaled(P, t, N) for t in units}
        smeared = sum(traces.values())
        nonzero_t = [t for t in units if traces[t] != 0]

        # ### THE FIXED-POINT CONTROL, TWO ROUTES TO ONE INTEGER.
        fp_ok = all(fixed_points(t, N) == gcd(t - 1, N) for t in units)

        orth, nshells, unions = invariant_reason(p, n, N, basis)
        reason_ok = orth and unions and (smeared == 0)

        good = (rank == dim_law and tr == dim_law and idem and symm and fixes_basis
                and spike_moved and all_perm and fp_ok and reason_ok)
        fails += 0 if good else 1

        print('-' * 100)
        print('  CELL (p,n) = (%d,%d)   N = %d   |(Z/N)^x| = %d' % (p, n, N, len(units)))
        print('    dim Son (built)        : %d      the law (p^n - 1)^2 : %d      %s'
              % (rank, dim_law, 'AGREE' if rank == dim_law else '### DISAGREE ###'))
        print('    Tr(Pi)                 : %s      ### the positive control: Pi is not dead'
              % tr)
        print('    Pi idempotent / symmetric / fixes its basis : %s / %s / %s'
              % (idem, symm, fixes_basis))
        print('    ### NEGATIVE CONTROL: an off-ball spike is MOVED by Pi : %s' % spike_moved)
        print('    every unit permutes Z/N (nothing escapes)   : %s' % all_perm)
        print('    fixed-point count == gcd(t-1, N) at every t : %s' % fp_ok)
        print('    ### ESCAPED-MASS EXPOSURE AT THIS CELL:')
        print('        the `Z_p^x` part (%d elements) : ### **NOT EXPOSED** -- each acts as a'
              % len(units))
        print('          permutation of Z/N, so no mass leaves the level and none is folded back.')
        print('        the `p^Z` part                : ### **EXPOSED, AND THEREFORE NOT COMPUTED**')
        print('          -- b21\'s artifact, met at b284. ### THE MODEL FOLDS THE ESCAPED MASS.')
        print('    ### **Tr(theta(t) Pi) OVER THE UNITS:**')
        shown = units if len(units) <= 12 else units[:12]
        for t in shown:
            print('        t = %-4d  Tr(theta(t) Pi) = %-14s  fixed points = %d'
                  % (t, traces[t], fixed_points(t, N)))
        if len(units) > len(shown):
            print('        ... %d further units not printed; the sum below is over ALL of them.'
                  % (len(units) - len(shown)))
        print('    ### **THE SMEARED VALUE against the constant test function on the units:**')
        print('        T = SUM_{t in (Z/N)^x} Tr(theta(t) Pi) = ### **%s**' % smeared)
        print('        units with a NONZERO trace : %d of %d' % (len(nonzero_t), len(units)))
        print('        ### ONE-LEVEL PLACE (n = 1)? : %s' % ('YES' if n == 1 else 'no'))
        print('    ### **WHY IT IS ZERO -- DERIVED, THEN CHECKED AT THIS CELL:**')
        print('        shells checked                              : %d' % nshells)
        print('        every Son vector orthogonal to every shell  : %s' % orth)
        print('        each shell below the level is a union of classes mod p^n : %s' % unions)
        print('        ### **SO `SUM_t theta(t) = |U| * Q` MEETS `Son` ORTHOGONALLY AND THE')
        print('        ### SMEARED VALUE IS ZERO BY `Son`\'s OWN TWO CONDITIONS, NOT BY THE CELLS.**')
        print('    %s' % ('PASS' if good else '### FAIL ###'))

    print('-' * 100)
    print('  ### CELLS FAILING : %d' % fails)
    print()
    print('  ### **WHAT THIS FILE DOES NOT SAY.** ### A value is a value. ### **NO NONZERO NUMBER')
    print('  ### HERE IS A ROUTE**, none of it is an aggregation, and none of it bears on `M-2`.')
    print('  ### **AND THE SECTOR REFINEMENT `E_1` IS NOT COMPUTED** -- its projector carries')
    print('  ### `zeta_N` in every entry and this file is exact over `Q`. ### Declared, not skipped.')
    print('=' * 100)
    return 0 if fails == 0 else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
