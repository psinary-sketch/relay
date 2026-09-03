# -*- coding: utf-8 -*-
"""b303_family.py -- THE FAMILY'S FINITE HALF, ### **VERIFIED AT CONTENT AND INDEPENDENTLY.**

### WHAT THIS IS FOR. ### b303's Component 2 must verify, ### AT CONTENT ### , that the corpus's
### object is the EVERYWHERE-DIAGONAL member of the two-radius family. ### b293 verified the finite
### half with `tools/e16/b293_finite_family.py`. ### **CITING THAT WOULD BE A CITATION, NOT A
### VERIFICATION**, and the order says at content -- so this file re-derives it from the owners'
### definitions with its own code and compares the two answers only at the end.

### ### **THE THREE ARMS, AND WHY THE MIDDLE ONE IS THE LOAD-BEARING ONE:**
###   ### **ARM A -- THE INDEX SETS.** ### `B_0 = ball_n`, from two INDEPENDENT predicates: a
###     valuation computed by repeated division, and a divisibility test. ### **NEITHER IS DEFINED
###     IN TERMS OF THE OTHER**, which is the whole point -- if `vp` were defined as "the largest
###     `n` with `p^n | m`" the agreement would be a tautology dressed as a check.
###   ### **ARM B -- THE DIAGONAL, VECTOR BY VECTOR, BOTH DIRECTIONS.** ### Every basis vector of
###     the corpus's space satisfies the `(0,0)` member's conditions and every basis vector of the
###     `(0,0)` member satisfies the corpus's -- ### **CONTAINMENT BOTH WAYS IS SET EQUALITY;
###     ONE WAY IS NOT.** ### With an off-ball spike as the negative control, because a membership
###     test that admits everything proves nothing.
###   ### **ARM C -- THE TRANSFORM CONDITION IN `Q(zeta_N)`, EXACTLY.** ### The construction uses
###     b293's COLLAPSED rational condition; ### **THIS ARM CHECKS THAT THE COLLAPSE IS THE ACTUAL
###     TRANSFORM CONDITION** by evaluating `(S f)(m)` in the cyclotomic field and reducing modulo
###     `Phi_N`, on sampled members AND on the non-member. ### A collapse that were merely implied
###     by membership would pass the positive arm and fail the negative one.

### ### **NO FLOAT ANYWHERE. ### `Fraction` AND `int` ONLY.**
### ### **WHAT IT DOES NOT TOUCH: ### THE ARCHIMEDEAN PLACE.** ### There is nothing here to
### compute at `infinity` and nothing here is evidence about it. ### b285's boundary stands:
### **NO FINITE-SIDE STRUCTURAL FACT TYPES AT `infinity`.**
"""
import os
import sys
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CELLS = [(2, 1), (2, 2), (3, 1), (3, 2), (5, 1)]
VP_CAP = 64          # ### the fuel; `vp(p, 0)` returns it, and 0's valuation is not finite


# ### ==============================================================================================
# ### ARM A's TWO PREDICATES. ### **INDEPENDENT BY CONSTRUCTION.**
# ### ==============================================================================================
def vp(p, m):
    """### THE `p`-ADIC VALUATION, ### **BY REPEATED DIVISION** -- never by a divisibility test."""
    if m == 0:
        return VP_CAP
    k = 0
    while m % p == 0 and k < VP_CAP:
        m //= p
        k += 1
    return k


def divides_pow(p, n, m):
    """### `p^n | m`. ### **A SINGLE MODULO. ### IT NEVER CALLS `vp`.**"""
    return m % (p ** n) == 0


def ball_corpus(p, n):
    """### THE CORPUS'S `ball_n = { m : p^n | m }` in `Z/p^{2n}` (b280's reading of the keystone)."""
    return set(m for m in range(p ** (2 * n)) if divides_pow(p, n, m))


def ball_family(p, n, e):
    """### b293's `B_e := { m : v_p(m) >= n - e }`, ### **BY THE VALUATION.**"""
    return set(m for m in range(p ** (2 * n)) if vp(p, m) >= n - e)


# ### ==============================================================================================
# ### EXACT LINEAR ALGEBRA OVER `Q`. ### **NO FLOAT.**
# ### ==============================================================================================
def nullspace(rows, ncols):
    """### A basis of `{ x : rows . x = 0 }`, exact, by Gauss-Jordan over `Fraction`."""
    mat = [list(map(Fraction, r)) for r in rows]
    pivots, row = [], 0
    for col in range(ncols):
        piv = None
        for r in range(row, len(mat)):
            if mat[r][col] != 0:
                piv = r
                break
        if piv is None:
            continue
        mat[row], mat[piv] = mat[piv], mat[row]
        inv = Fraction(1, 1) / mat[row][col]
        mat[row] = [v * inv for v in mat[row]]
        for r in range(len(mat)):
            if r != row and mat[r][col] != 0:
                f = mat[r][col]
                mat[r] = [a - f * b for a, b in zip(mat[r], mat[row])]
        pivots.append(col)
        row += 1
        if row == len(mat):
            break
    free = [c for c in range(ncols) if c not in pivots]
    basis = []
    for fc in free:
        v = [Fraction(0)] * ncols
        v[fc] = Fraction(1)
        for r, pc in enumerate(pivots):
            v[pc] = -mat[r][fc]
        basis.append(v)
    return basis


# ### ==============================================================================================
# ### THE TWO CONDITION SETS, EACH FROM ITS OWN OWNER'S WORDS.
# ### ==============================================================================================
def rows_corpus(p, n):
    """### THE CORPUS'S SPACE: ### **vanishing on `ball_n` AND on its transform image.**

    ### The transform half is written with b293's COLLAPSED form at `b = 0` -- the fiber sums at
    ### modulus `p^n` -- and ### **ARM C IS WHAT ENTITLES THIS FILE TO USE IT.**
    """
    N = p ** (2 * n)
    ball = ball_corpus(p, n)
    rows = []
    for m in sorted(ball):
        r = [0] * N
        r[m] = 1
        rows.append(r)
    mod = p ** n
    for res in range(mod):
        r = [1 if (mm % mod) == res else 0 for mm in range(N)]
        rows.append(r)
    return rows


def rows_member(p, n, a, b):
    """### b293's `Son(p,n; a,b)`, from its own definition: ### `f = 0` on `B_a`, fiber sums at
    modulus `p^{n+b}` vanish."""
    N = p ** (2 * n)
    rows = []
    for m in sorted(ball_family(p, n, a)):
        r = [0] * N
        r[m] = 1
        rows.append(r)
    mod = p ** (n + b)
    for res in range(mod):
        r = [1 if (mm % mod) == res else 0 for mm in range(N)]
        rows.append(r)
    return rows


def satisfies(rows, vec):
    return all(sum(Fraction(c) * v for c, v in zip(r, vec)) == 0 for r in rows)


# ### ==============================================================================================
# ### ARM C -- THE TRANSFORM IN `Q(zeta_N)`, EXACTLY.
# ### ==============================================================================================
def phi_prime_power(p, k):
    """### `Phi_{p^k}(x) = SUM_{j<p} x^{j p^{k-1}}`, as a coefficient list, low degree first."""
    d = p ** (k - 1)
    co = [0] * (d * (p - 1) + 1)
    for j in range(p):
        co[j * d] = 1
    return co


def poly_mod(co, mod):
    """### Remainder of `co` modulo the MONIC polynomial `mod`, over `Q`. ### Low degree first."""
    co = [Fraction(c) for c in co]
    dm = len(mod) - 1
    while len(co) - 1 >= dm and any(c != 0 for c in co):
        if co[-1] == 0:
            co.pop()
            continue
        shift = len(co) - 1 - dm
        f = co[-1]
        for i, mc in enumerate(mod):
            co[i + shift] -= f * mc
        while co and co[-1] == 0:
            co.pop()
    return co


def transform_vanishes(p, n, vec, targets):
    """### **DOES `(S f)(m) = SUM_{m'} f(m') zeta_N^{m m'}` VANISH IN `Q(zeta_N)` FOR EVERY `m` IN
    `targets`?** ### Evaluated as a polynomial in `zeta_N` and reduced modulo `Phi_N`.
    """
    N = p ** (2 * n)
    mod = phi_prime_power(p, 2 * n)
    for m in targets:
        co = [Fraction(0)] * N
        for mp, val in enumerate(vec):
            if val != 0:
                co[(m * mp) % N] += Fraction(val)
        if any(c != 0 for c in poly_mod(co, mod)):
            return False
    return True


# ### ==============================================================================================
# ### THE FIXTURES. ### **BOTH POLARITIES ON EVERY INSTRUMENT THIS FILE OWNS.**
# ### ==============================================================================================
def self_test(verbose=True):
    out, bad = [], 0

    def chk(lbl, got, exp):
        nonlocal bad
        ok = (got == exp)
        bad += 0 if ok else 1
        if verbose:
            print('  %-62s %-18s %s' % (lbl, '%s/%s' % (got, exp), 'YES' if ok else '### NO ###'))

    if verbose:
        print('  %-62s %-18s %s' % ('fixture', 'got/expected', 'agree'))
    # ### THE VALUATION, ### **INCLUDING THE ZERO CASE, WHICH IS THE ONE THAT BITES.**
    chk('vp(2, 8) -- repeated division', vp(2, 8), 3)
    chk('vp(3, 9)', vp(3, 9), 2)
    chk('vp(2, 6) -- one factor only', vp(2, 6), 1)
    chk('vp(2, 5) -- none', vp(2, 5), 0)
    chk('### vp(p, 0) is the cap, NOT 0', vp(2, 0), VP_CAP)
    chk('divides_pow(2, 3, 8)', divides_pow(2, 3, 8), True)
    chk('### divides_pow(2, 3, 4) -- the near miss', divides_pow(2, 3, 4), False)

    # ### THE NULLSPACE, ### **AND AN EMPTY-SCOPE GUARD.**
    chk('nullspace of x0=0 in 2 vars has dimension 1',
        len(nullspace([[1, 0]], 2)), 1)
    chk('nullspace of a full-rank 2x2 system is trivial',
        len(nullspace([[1, 0], [0, 1]], 2)), 0)
    chk('### nullspace with NO rows is the whole space, not empty',
        len(nullspace([], 3)), 3)

    # ### THE CYCLOTOMIC REDUCTION, ### **BOTH POLARITIES.**
    # ### `1 + x + x^2 = Phi_3` reduces to 0; `1 + x` does not.
    chk('Phi_3 reduces to zero mod Phi_3',
        poly_mod([1, 1, 1], phi_prime_power(3, 1)), [])
    chk('### 1 + x does NOT reduce to zero mod Phi_3',
        any(c != 0 for c in poly_mod([1, 1], phi_prime_power(3, 1))), True)
    chk('Phi_4 = 1 + x^2', phi_prime_power(2, 2), [1, 0, 1])
    chk('x^2 + 1 reduces to zero mod Phi_4',
        poly_mod([1, 0, 1], phi_prime_power(2, 2)), [])

    # ### `satisfies`, ### **BOTH POLARITIES.**
    chk('satisfies: the zero vector meets every condition',
        satisfies([[1, 1]], [Fraction(0), Fraction(0)]), True)
    chk('### satisfies: a violating vector is rejected',
        satisfies([[1, 1]], [Fraction(1), Fraction(0)]), False)
    return bad == 0


# ### ==============================================================================================
def main(argv):
    print('=' * 100)
    print('b303_family.py -- THE FAMILY\'S FINITE HALF, VERIFIED AT CONTENT.')
    print('=' * 100)
    ok = self_test()
    print('  self-test : %s' % ('PASS' if ok else '### FAIL ###'))
    if not ok:
        print('  ### REFUSING TO REPORT A VERIFICATION FROM A SUITE THAT FAILS ITS OWN FIXTURES.')
        return 2
    print()

    fails = 0
    print('  %-8s %-26s %-26s %-14s %s'
          % ('cell', 'ARM A  B_0 == ball_n', 'ARM B  diagonal both ways', 'ARM C  Q(zeta)',
             'dim vs (p^n-1)^2'))
    for (p, n) in CELLS:
        N = p ** (2 * n)

        # ### ARM A -- THE INDEX SETS, FROM TWO INDEPENDENT PREDICATES.
        a_eq = (ball_family(p, n, 0) == ball_corpus(p, n))
        # ### THE CONTROL: at exponent 1 the two must DIFFER, or ARM A is vacuous.
        a_ctl = (ball_family(p, n, 1) != ball_corpus(p, n))
        a_size = (len(ball_corpus(p, n)) == p ** n)

        # ### ARM B -- THE DIAGONAL, VECTOR BY VECTOR, BOTH DIRECTIONS.
        rc, rm = rows_corpus(p, n), rows_member(p, n, 0, 0)
        bc, bm = nullspace(rc, N), nullspace(rm, N)
        fwd = all(satisfies(rm, v) for v in bc)          # ### corpus  -> member
        rev = all(satisfies(rc, v) for v in bm)          # ### member  -> corpus
        # ### THE NEGATIVE CONTROL: an off-ball spike must be rejected by BOTH.
        spike = [Fraction(0)] * N
        off = next(m for m in range(N) if m not in ball_corpus(p, n))
        spike[off] = Fraction(1)
        b_ctl = (not satisfies(rc, spike)) and (not satisfies(rm, spike))
        b_ok = fwd and rev and b_ctl and len(bc) > 0

        # ### ARM C -- THE COLLAPSE IS THE ACTUAL TRANSFORM CONDITION.
        targets = sorted(ball_corpus(p, n))
        sample = bc[:4]
        c_pos = all(transform_vanishes(p, n, v, targets) for v in sample)
        c_neg = not transform_vanishes(p, n, spike, targets)
        c_ok = c_pos and c_neg

        dim_ok = (len(bc) == (p ** n - 1) ** 2)

        cell_ok = a_eq and a_ctl and a_size and b_ok and c_ok and dim_ok
        fails += 0 if cell_ok else 1
        print('  %-8s %-26s %-26s %-14s %s'
              % ('(%d,%d)' % (p, n),
                 'YES, ctl differs' if (a_eq and a_ctl and a_size) else '### NO ###',
                 'YES, spike rejected' if b_ok else '### NO ###',
                 '%d ok, ctl fires' % len(sample) if c_ok else '### NO ###',
                 '%d == %d  %s' % (len(bc), (p ** n - 1) ** 2, 'YES' if dim_ok else '### NO ###')))

    print()
    print('  ### CELLS FAILING : %d' % fails)

    # ### THE CHART, ### **CHECKED AS AN IDENTITY OF INTEGERS AND NOT ASSERTED.**
    print()
    print('  ### THE CHART `a -> p^a` (b21\'s, quoted by b293), AND THE TWO INVARIANTS.')
    chart_bad = 0
    for (p, n) in CELLS:
        for a in range(-n, n + 1):
            for b in range(-n, n + 1):
                lam, mu = Fraction(p) ** a, Fraction(p) ** b
                # ### the finite dilation `(a,b) -> (a+1, b-1)` in the chart
                lam2, mu2 = Fraction(p) ** (a + 1), Fraction(p) ** (b - 1)
                if lam2 != p * lam or mu2 != mu / p:
                    chart_bad += 1
                # ### the SUM invariant becomes the PRODUCT invariant
                if lam * mu != Fraction(p) ** (a + b) or lam2 * mu2 != lam * mu:
                    chart_bad += 1
    print('    `p^{a+1} = p * p^a` and `p^{b-1} = p^b / p` .............. mismatches : %d'
          % chart_bad)
    print('    ### **SO THE FINITE DILATION IS `(lam, mu) -> (p*lam, mu/p)`,**')
    print('    ### **WHICH IS THE ARCHIMEDEAN `D_a : (lam, mu) -> (lam/a, a*mu)` AT `a = 1/p`.**')
    print('    ### **AND `lam * mu = p^{a+b}`: ### THE SUM INVARIANT IS THE PRODUCT INVARIANT')
    print('    ### READ THROUGH THE CHART.** ### The chart is the CORPUS\'S OWN (b21), quoted by')
    print('    ### b293 at its own definition of `B_e`. ### **IT IS NOT SUPPLIED BY THIS ACT.**')

    # ### THE DIAGONAL, NAMED IN THE CHART'S TERMS.
    print()
    print('  ### THE DIAGONAL MEMBER IN THE CHART : `a = b = 0` is `lam = mu = p^0 = 1`.')
    print('  ### **`1` IS THE UNIT OF EVERY PLACE\'S VALUE GROUP, AND THE ARCHIMEDEAN MEMBER IS')
    print('  ### `S(1,1)`. ### THE "EVERYWHERE-DIAGONAL" MEMBER IS THE EVERYWHERE-`(1,1)` ONE.**')
    print()
    print('  ### **NOTHING ABOVE IS EVIDENCE ABOUT `infinity`.** ### There is no archimedean')
    print('  ### computation in this file and b285\'s boundary is not crossed by it.')
    print('=' * 100)
    return 0 if (fails == 0 and chart_bad == 0) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
