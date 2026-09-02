# -*- coding: utf-8 -*-
"""b293 -- THE FINITE TWO-RADIUS FAMILY. ### THE CONSTRUCTION AND ITS CONTROLS.

### ### **EVERY DEFINITION BELOW IS IN THE CORPUS'S OWN `p`-ADIC TERMS, AT THE CORPUS'S OWN LEVEL
### ### INDEXING. ### THE ARCHIMEDEAN FAMILY IS THE TEMPLATE AND APPEARS NOWHERE AS A REASON
### ### (falsifier V4).**

### THE CORPUS'S SPACE, from the keystone: `Son(p,n)` on `Z/p^{2n}`, the vectors vanishing on a
### ball AND on its transform image, ### **BOTH HALVES USING THE SAME `ball_n = {m : p^n | m}`**
### (b280's reading, quoted).

### ### **THE FAMILY.** ### Two independent radii `a`, `b`, as integer exponents of `p`, at the
### corpus's own indexing. ### A ball of exponent `e` is `{ m : v_p(m) >= n - e }` -- which is
### `{ x : |x| <= p^e }` in b21's chart, and at `e = 0` is exactly `ball_n`.
###   ### **`Son(p,n; a,b) := { f : f(m) = 0 whenever v_p(m) >= n - a,`**
###   ### **                    `and (S f)(m) = 0 whenever v_p(m) >= n - b }`.**
### ### **THE DIAGONAL `a = b = 0` IS THE CORPUS'S `Son(p,n)` BY CONSTRUCTION -- and that is
### ### CHECKED VECTOR BY VECTOR BELOW RATHER THAN ASSERTED (V1).**

### ### **THE SECOND CONDITION, COLLAPSED -- DERIVED HERE, CONTROLLED BELOW (V2):** ### at
### `m` with `v_p(m) >= n - b`, write `m = p^{n-b} j`; then `zeta_N^{m m'} = zeta_{p^{n+b}}^{j m'}`,
### which depends on `m'` only mod `p^{n+b}`. ### So the condition says the order-`p^{n+b}` DFT of
### the folded function vanishes identically, hence
###   ### **`SUM_{m' = r mod p^{n+b}} f(m') = 0` for every `r`** -- ### **A RATIONAL CONDITION.**

### ### **ZERO FLOAT TOKENS. ### Ranks are computed by exact elimination over `Fraction`.**
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
from b271_top_level_no_go import apply_S                     # noqa: E402
from b279_local_space import son_basis, son_conditions_hold   # noqa: E402
from b279_son_control import as_field_vector                 # noqa: E402
from b284_scaling_domain import vp, scale_g, scale_h          # noqa: E402

CELLS = [(2, 1), (2, 2), (3, 1), (3, 2), (5, 1)]


def vanish_set(p, n, e):
    """### THE BALL OF EXPONENT `e`: ### `{ m : v_p(m) >= n - e }`. ### At `e = 0` this is
    ### `ball_n = { m : p^n | m }`, the corpus's own ball."""
    N = p ** (2 * n)
    thr = n - e
    return [m for m in range(N) if vp(m, p, 2 * n + 1) >= thr]


def constraints(p, n, a, b):
    """### THE FAMILY'S TWO CONDITIONS AS EXACT RATIONAL ROWS."""
    N = p ** (2 * n)
    rows = []
    for m in vanish_set(p, n, a):                    # ### condition one
        r = [Fraction(0)] * N
        r[m] = Fraction(1)
        rows.append(r)
    mod = p ** (n + b)
    if 0 <= n + b <= 2 * n:                          # ### condition two, collapsed
        for res in range(mod):
            r = [Fraction(0)] * N
            for m in range(res, N, mod):
                r[m] = Fraction(1)
            rows.append(r)
    return rows


def rank_exact(rows, N):
    """### EXACT GAUSSIAN ELIMINATION OVER `Fraction`. ### **NO FLOAT ANYWHERE.**"""
    rows = [r[:] for r in rows]
    rank = 0
    for col in range(N):
        piv = None
        for i in range(rank, len(rows)):
            if rows[i][col] != 0:
                piv = i
                break
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        pr = rows[rank]
        inv = Fraction(1, 1) / pr[col]
        pr = [x * inv for x in pr]
        rows[rank] = pr
        for i in range(len(rows)):
            if i != rank and rows[i][col] != 0:
                f = rows[i][col]
                rows[i] = [x - f * y for x, y in zip(rows[i], pr)]
        rank += 1
        if rank == len(rows):
            break
    return rank


def dim_family(p, n, a, b):
    N = p ** (2 * n)
    return N - rank_exact(constraints(p, n, a, b), N)


def in_family(f, p, n, a, b):
    """### MEMBERSHIP BY THE TWO CONDITIONS, EXACTLY."""
    N = p ** (2 * n)
    for m in vanish_set(p, n, a):
        if f[m] != 0:
            return False
    mod = p ** (n + b)
    if not (0 <= n + b <= 2 * n):
        return False
    for res in range(mod):
        if sum(f[m] for m in range(res, N, mod)) != 0:
            return False
    return True


def transform_vanishes(f, p, n, b):
    """### THE OWNERS' LITERAL SECOND CONDITION, COMPUTED IN `Q(zeta_N)` (V2's control)."""
    N = p ** (2 * n)
    F = Field(N)
    Sf = apply_S(as_field_vector(f), N)
    for m in vanish_set(p, n, b):
        if not F.is_zero(Sf[m]):
            return False
    return True


def basis_family(p, n, a, b):
    """### AN EXPLICIT BASIS, BY SOLVING THE CONSTRAINTS EXACTLY."""
    N = p ** (2 * n)
    rows = constraints(p, n, a, b)
    # ### reduce to row echelon, then read the null space.
    R = [r[:] for r in rows]
    piv_cols, rank = [], 0
    for col in range(N):
        piv = None
        for i in range(rank, len(R)):
            if R[i][col] != 0:
                piv = i
                break
        if piv is None:
            continue
        R[rank], R[piv] = R[piv], R[rank]
        inv = Fraction(1, 1) / R[rank][col]
        R[rank] = [x * inv for x in R[rank]]
        for i in range(len(R)):
            if i != rank and R[i][col] != 0:
                fct = R[i][col]
                R[i] = [x - fct * y for x, y in zip(R[i], R[rank])]
        piv_cols.append(col)
        rank += 1
    free = [c for c in range(N) if c not in piv_cols]
    out = []
    for fc in free:
        v = [Fraction(0)] * N
        v[fc] = Fraction(1)
        for i, pc in enumerate(piv_cols):
            v[pc] = -R[i][fc]
        out.append(v)
    return out


def run_cell(p, n, rec):
    N = p ** (2 * n)
    rec('  ---- CELL (p,n) = (%d,%d):  N = %d ----' % (p, n, N))

    # ### (1) THE DIMENSION LAW, over the range the indexing supports.
    rec('    (1) dim Son(p,n;a,b) against the derived law `(p^n - p^a)(p^n - p^b)`:')
    bad = 0
    for a in range(-n, n + 1):
        for b in range(-n, n + 1):
            if a + b < 0:
                continue                     # ### law derived only for a+b >= 0; see the bank
            got = dim_family(p, n, a, b)
            want = (p ** n - p ** a) * (p ** n - p ** b) if a >= 0 and b >= 0 else None
            if want is not None and got != want:
                bad += 1
                rec('        ### MISMATCH (a,b)=(%d,%d): got %d, law %d' % (a, b, got, want))
    rec('        mismatches over the tested range : %d  %s'
        % (bad, 'NONE' if bad == 0 else '### PRESENT ###'))
    rec('        diagonal dim Son(p,n;0,0) = %-6d   owner\'s (p^n-1)^2 = %-6d  %s'
        % (dim_family(p, n, 0, 0), (p ** n - 1) ** 2,
           'AGREE' if dim_family(p, n, 0, 0) == (p ** n - 1) ** 2 else '### DISAGREE ###'))

    # ### (2) THE DIAGONAL, VECTOR BY VECTOR, BOTH POLARITIES (V1).
    corpus = son_basis(p, n)
    fwd = all(in_family(v, p, n, 0, 0) for v in corpus)
    mine = basis_family(p, n, 0, 0)
    bwd = all(son_conditions_hold([int(x) if x.denominator == 1 else x for x in v], p, n)[0]
              for v in mine)
    spike = [0] * N
    off = [m for m in range(N) if m % (p ** n) != 0]
    spike[off[0]] = 1
    neg = not in_family(spike, p, n, 0, 0)
    rec('    (2) DIAGONAL, vector by vector:')
    rec('        every corpus Son vector is in the (0,0) member   : %s' % ('YES' if fwd else '### NO ###'))
    rec('        every (0,0) member vector satisfies the corpus    : %s' % ('YES' if bwd else '### NO ###'))
    rec('        NEGATIVE CONTROL -- an off-ball spike is rejected : %s' % ('YES' if neg else '### NO ###'))

    # ### (3) V2's CONTROL: the collapsed condition IS the transform condition.
    smp = mine[:4]
    posc = all(transform_vanishes([x for x in v], p, n, 0) for v in smp)
    negc = not transform_vanishes(spike, p, n, 0)
    rec('    (3) V2 -- collapsed condition vs the ACTUAL transform, both ways:')
    rec('        members: transform really vanishes on ball_n      : %s  (%d sampled)'
        % ('YES' if posc else '### NO ###', len(smp)))
    rec('        non-member spike: transform does NOT vanish       : %s' % ('YES' if negc else '### NO ###'))

    cls, _ = noise_floor.classify(0, exact=True)
    rec('    noise-floor gate : %s   (exact rational elimination)' % cls)
    return (bad == 0) and fwd and bwd and neg and posc and negc


def dilation_and_reflection(p, n, rec):
    N = p ** (2 * n)
    rec('    (4) DILATION -- does the image land in the neighbouring member?')
    base = basis_family(p, n, 0, 0)
    for nm, fn, da, db in [('g = D_p  f', scale_g, +1, -1), ('h = D_1/p f', scale_h, -1, +1)]:
        live = [v for v in base if any(fn(v, p, n))]
        dead = len(base) - len(live)
        if not live:
            rec('        %-11s ### **NO LIVE IMAGE -- CELL CANNOT TEST** (%d dead)' % (nm, dead))
            continue
        ok = sum(1 for v in live if in_family(fn(v, p, n), p, n, da, db))
        rec('        %-11s lands in (%+d,%+d) : %d/%d live  (%d dead, excluded)  sum a+b = %d'
            % (nm, da, db, ok, len(live), dead, da + db))

    rec('    (5) REFLECTION -- does `S` carry (a,b) to (b,a)?')
    F = Field(N)
    for (a, b) in [(0, 0), (1, 0)] if n >= 1 else []:
        mem = basis_family(p, n, a, b)
        if not mem:
            rec('        (a,b)=(%d,%d): ### **EMPTY MEMBER -- CANNOT TEST**' % (a, b))
            continue
        good = 0
        for v in mem[:6]:
            Sv = apply_S(as_field_vector(v), N)
            c1 = all(F.is_zero(Sv[m]) for m in vanish_set(p, n, b))
            SSv = apply_S(Sv, N)
            c2 = all(F.is_zero(SSv[m]) for m in vanish_set(p, n, a))
            if c1 and c2:
                good += 1
        rec('        (a,b)=(%d,%d) -> (%d,%d) : %d/%d sampled members land'
            % (a, b, b, a, good, min(6, len(mem))))


def main():
    out = []

    def rec(s=''):
        out.append(s)
        print(s)

    rec('=' * 100)
    rec('b293 -- THE FINITE TWO-RADIUS FAMILY. ### CONSTRUCTED IN THE CORPUS\'S OWN TERMS.')
    rec('=' * 100)
    rec('### **NO ARCHIMEDEAN STEP APPEARS BELOW (V4).** ### Every condition is `p`-adic and every')
    rec('### control is exact rational or exact cyclotomic arithmetic.')
    rec()
    allok = True
    for p, n in CELLS:
        allok &= run_cell(p, n, rec)
        dilation_and_reflection(p, n, rec)
        rec()
    rec('=' * 100)
    rec('### ALL CELLS: %s' % ('PASS' if allok else '### SOME CHECK FAILED ###'))
    rec('=' * 100)
    with open(os.path.join(ROOT, 'data', 'b293_family_run.txt'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')
    return 0 if allok else 1


if __name__ == '__main__':
    sys.exit(main())
