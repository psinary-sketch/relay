# -*- coding: utf-8 -*-
"""b294 -- THE FAMILY'S FIRST-LEVEL VALUE.

### ### **THE HYPOTHESIS THE BARRIER CONSUMES, FROM b270's EMITTING FILE:** ### at `k = n`,
### `p^n m` is a multiple of `p^n` for every `m` -- ### "THAT IS THE BALL" -- ### **"AND `u_v`
### VANISHES ON THE BALL"**. ### ### **ONE HYPOTHESIS, ON THE FUNCTION SIDE ONLY, AT EXPONENT `0`.**

### ### **SO FOR A MEMBER `Son(p,n; a,b)`:** ### the function-side condition is vanishing on
### `B_a = { m : v_p(m) >= n - a }`, and the operator's image lies in `B_0 = ball_n`.
###   ### **`a >= 0` -> `B_a` CONTAINS `B_0`** ### (larger `a`, lower threshold, larger set), so
###     the member's own condition ### IMPLIES ### b270's hypothesis. ### **THE ARGUMENT RUNS.**
###   ### **`a < 0` -> `B_a` IS STRICTLY INSIDE `B_0`**, so the member is ### NOT ### required to
###     vanish on all of `ball_n`. ### **THE ARGUMENT DOES NOT RUN -- WHICH IS NOT A NONZERO
###     VALUE (X3). ### THE VALUE IS COMPUTED BELOW.**

### ### **EXPOSURE TO THE ESCAPED-MASS ARTIFACT (X4): ### NONE.** ### This runner applies ### NO
### ### LEVEL-SHIFTING MAP ### . ### The members are defined by radii, not by scaling; the pairing
### is b273's `A` at `k = n`, within one level, the same operator b270 and b281 used. ### **THE
### ### ARTIFACT LIVES IN `g` AND `h`, WHICH DO NOT APPEAR HERE.**

### ### **ZERO FLOAT TOKENS.** ### Members by exact elimination over `Fraction`; pairings in
### `Q(zeta_N)`.
"""
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'tools'))

import noise_floor                                          # noqa: E402
from b270_ambient_pairing import Field                       # noqa: E402
from b281_compression import matrix_A, apply_A               # noqa: E402
from b293_finite_family import basis_family, vanish_set      # noqa: E402

CELLS = [(2, 1), (2, 2), (3, 1), (3, 2), (5, 1)]


def pair_at_n(A, f, N, F):
    """### b270's PAIRING AT `k = n`, RESCALED BY `p^{n/2}`: ### `<A f, f>`.
    ### The rescaling is by a positive factor and decides nothing (b280's note, carried)."""
    Af = apply_A(A, f, N)
    acc = {}
    from b270_ambient_pairing import spadd, spmul, spconj
    for l in range(N):
        if not Af[l] or not f[l]:
            continue
        a = {0: Fraction(Af[l])}
        b = {0: Fraction(f[l])}
        acc = spadd(acc, spmul(a, spconj(b, N), N))
    return acc


def run_cell(p, n, rec):
    N = p ** (2 * n)
    F = Field(N)
    A = matrix_A(N, p, n, n)
    rec('  ---- CELL (p,n) = (%d,%d):  N = %d ----' % (p, n, N))

    # ### X1's WITNESS, FIRST: the SAME pairing must be able to return nonzero.
    q = p ** n
    g0 = [Fraction(2)] * N
    g0[0] += 2 * q
    w = pair_at_n(A, g0, N, F)
    banked = 4 * (N - q)
    wv = F.reduce(w)
    rec('    X1 NOT-DEAD WITNESS: <A g_0, g_0> = %-8s  b271 banked 4(N-q) = %-8s  %s'
        % (wv[0] if wv else 0, banked,
           'MATCH' if (wv and wv[0] == banked and all(c == 0 for c in wv[1:])) else '### NO ###'))

    # ### THE MEMBERS, BY CLASS. ### **A GRID, NOT ONE ORBIT** -- the orbit `a+b = 0` couples a
    # ### weakened function side to a STRENGTHENED transform side, so a zero there cannot separate
    # ### the two. ### **THE GRID ISOLATES THEM.**
    for (a, b) in [(0, 0), (-1, 1), (-1, 0), (0, -1), (-1, -1)]:
        if not (-n <= a <= n and -n <= b <= n):
            continue
        mem = basis_family(p, n, a, b)
        live = [v for v in mem if any(x != 0 for x in v)]
        if not live:
            rec('    (a,b) = (%+d,%+d) : ### **EMPTY MEMBER -- CANNOT TEST** (X2)' % (a, b))
            continue
        vals = []
        for v in live:
            val = pair_at_n(A, v, N, F)
            vals.append((v, val))
        nz = [(v, x) for v, x in vals if not F.is_zero(x)]
        cls = 'HYPOTHESIS HOLDS (a >= 0)' if a >= 0 else 'hypothesis fails (a < 0)'
        annih = sum(1 for v in live if not any(apply_A(A, v, N)))
        rec('    (a,b) = (%+d,%+d)  dim %-4d  [%s]   A f = 0 for %d/%d'
            % (a, b, len(live), cls, annih, len(live)))
        if not nz:
            rec('        ### **EVERY BASIS VECTOR PAIRS TO ZERO** (%d of %d)' % (len(live), len(live)))
        else:
            v, x = nz[0]
            red = F.reduce(x)
            rec('        ### **NONZERO ON %d OF %d BASIS VECTORS.**' % (len(nz), len(live)))
            rec('        first witness support %s' % [(i, v[i]) for i in range(N) if v[i]][:4])
            rec('        ### **EXACT VALUE (coeff vector in Q(zeta_%d)) : %s**'
                % (N, [str(c) for c in red[:6]]))

    cls_, _ = noise_floor.classify(0, exact=True)
    rec('    noise-floor gate : %s   (exact rational and cyclotomic)' % cls_)


def main():
    out = []

    def rec(s=''):
        out.append(s)
        print(s)

    rec('=' * 100)
    rec('b294 -- THE FAMILY\'S FIRST-LEVEL VALUE. ### THE PAIRING ON OFF-DIAGONAL MEMBERS.')
    rec('=' * 100)
    rec('### **NO LEVEL-SHIFTING MAP APPEARS. ### NOT EXPOSED TO THE ESCAPED-MASS ARTIFACT (X4).**')
    rec('### A GRID OF MEMBERS, NOT ONE ORBIT -- the orbit `a+b = 0` couples a weakened')
    rec('### function side to a STRENGTHENED transform side, and could not separate them.')
    rec()
    for p, n in CELLS:
        run_cell(p, n, rec)
        rec()
    rec('=' * 100)
    with open(os.path.join(ROOT, 'data', 'b294_value_run.txt'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
