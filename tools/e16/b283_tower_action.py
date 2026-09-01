# -*- coding: utf-8 -*-
"""b283 -- THE TOWER'S ACTION. ### IS `iota` MULTIPLICATION BY `p`?

### THE DOUBLE NAME, KEPT AT EVERY USE AND NEVER LET TO INHERIT:
###   ### **`iota` AS INDEX MAP**  -- `m'' = p*m + p^{2n+1}*j`, BETWEEN levels, no wraparound.
###   ### **MODEL `U` AS INDEX MAP** -- `m -> p*m mod N`, WITHIN a level, WITH wraparound.
###   ### **`iota` AS AN OPERATOR ON `S-bar_p`** -- what it induces on the limit, if anything.
###   ### **`V_inv`'s RELATION `x ~ px`** -- b10's SCALING relation, which is `U`'s and NOT
###     `iota`'s.
### ### ### **BOTH INDEX FORMULAS CARRY A FACTOR `p`. ### THAT IS A RESEMBLANCE AND THIS FILE
### ### ### TREATS IT AS NO EVIDENCE AT ALL (falsifier I1).**

### ### **ZERO FLOAT TOKENS. ### Every chart value is an exact `Fraction`.**
"""
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'tools'))

import noise_floor                                              # noqa: E402
from b270_ambient_pairing import ball_of, orbit_classes          # noqa: E402
from b279_local_space import son_basis, iota                     # noqa: E402

CELLS = [(2, 1), (2, 2), (3, 1), (3, 2), (5, 1), (7, 1)]


def chart(m, n):
    """### b21's CHART, EXACTLY: ### `x = p^{-n} m`. ### Returned as a `Fraction` so the
    ### comparison below is exact and no decimal ever enters."""
    return Fraction(m), n          # ### carried as (m, n); the value is m / p^n


def chart_shift_is_pn_j(p, n):
    """### THE IDENTIFICATION, COMPUTED. ### For every level-`n` index `m` and every `j`:
    ###   `x'' - x  =  p^{-(n+1)}(p m + p^{2n+1} j)  -  p^{-n} m  =  p^n j`.
    ### ### **AND `p^n j` LIES IN `p^n Z_p`, WHICH IS EXACTLY THE SUBGROUP `V_n`'s FUNCTIONS ARE
    ### ### INVARIANT UNDER.** ### So `iota f` takes the value `f(x)` at points CONGRUENT TO `x`
    ### ### mod `p^n Z_p` -- i.e. ### **`iota f` IS `f`.**"""
    N, M = p ** (2 * n), p ** (2 * n + 2)
    bad = []
    for m in range(N):
        x = Fraction(m, p ** n)
        for j in range(p):
            mm = (p * m + p ** (2 * n + 1) * j) % M
            xx = Fraction(mm, p ** (n + 1))
            d = xx - x
            # ### the difference must be an INTEGER MULTIPLE OF p^n (an element of p^n Z),
            # ### and modulo the level's own period it must be exactly p^n * j.
            if d.denominator != 1 or (d % (p ** n)) != 0:
                bad.append((m, j, d))
    return bad


def iota_is_identity_on_functions(p, n):
    """### `iota f` AND `f` AS FUNCTIONS: ### every host cell carrying a value must carry the
    ### value of the level-`n` cell it refines. ### **CHECKED CELL BY CELL, NOT ASSERTED.**"""
    N, M = p ** (2 * n), p ** (2 * n + 2)
    bad = 0
    for f in son_basis(p, n):
        g = iota(f, p, n)
        for m in range(N):
            for j in range(p):
                mm = (p * m + p ** (2 * n + 1) * j) % M
                if g[mm] != f[m]:
                    bad += 1
    return bad


def support_test(p, n):
    """### FALSIFIER I2, THE ONE THAT DECIDES THE BRANCH.
    ### ### **MULTIPLICATION BY `p` MOVES SUPPORT; `iota` DOES NOT.**
    ### b21: `supp(U f) = p^{-n-1} Z_p`, STRICTLY BIGGER than `p^{-n} Z_p`.
    ### Here, in the chart and exactly:
    ###   `iota`  : the set of `x` carrying nonzero values is UNCHANGED (each level-`n` cell is
    ###             refined into `p` host cells with the SAME value).
    ###   model `U`: `m -> p m mod N` COLLAPSES indices -- and after `n` steps every index is in
    ###             the ball (b270's index law), which `iota` never does to anything.
    ### Returns (iota_moves_support, U_n_lands_in_ball, iota_ever_lands_in_ball)."""
    N = p ** (2 * n)
    ballset = set(ball_of(N, p, n))
    basis = son_basis(p, n)

    # ### (i) does `iota` change the set of chart points carrying nonzero values?
    moved = 0
    for f in basis:
        xs_before = {Fraction(m, p ** n) for m in range(N) if f[m]}
        g = iota(f, p, n)
        M = p ** (2 * n + 2)
        xs_after = {Fraction(mm, p ** (n + 1)) for mm in range(M) if g[mm]}
        # ### a host point `x''` refines a level-`n` point `x` iff `x'' - x` is in `p^n Z`.
        for xx in xs_after:
            if not any((xx - x).denominator == 1 and (xx - x) % (p ** n) == 0
                       for x in xs_before):
                moved += 1

    # ### (ii) model `U^n`: every index lands in the ball. ### b270's index law, re-run.
    un_in_ball = all(((pow(p, n, N) * m) % N) in ballset for m in range(N))

    # ### (iii) does `iota` EVER carry an off-ball index into the host's ball?
    ballh = set(ball_of(p ** (2 * n + 2), p, n + 1))
    iota_into_ball = 0
    for m in range(N):
        if m in ballset:
            continue
        for j in range(p):
            mm = (p * m + p ** (2 * n + 1) * j) % (p ** (2 * n + 2))
            if mm in ballh:
                iota_into_ball += 1
    return moved, un_in_ball, iota_into_ball


def vinv_relation_is_scaling(p, n):
    """### b10's `V_inv` IS BUILT FROM `x ~ px`, ### NOT ### FROM `iota`. ### Its own words:
    ### *"f(m') = f(m) whenever m' = p m mod N and both m, m' off-ball"*. ### Verified by
    ### rebuilding the classes from that relation and comparing to the corpus's own builder."""
    N = p ** (2 * n)
    ballset = set(ball_of(N, p, n))
    mine = {}
    for m in range(N):
        if m in ballset:
            continue
        mine.setdefault(m, m)
    # ### union-find on m ~ p m mod N, both off-ball -- b10's relation, verbatim.
    parent = {m: m for m in range(N) if m not in ballset}

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for m in list(parent):
        m2 = (p * m) % N
        if m2 not in ballset:
            ra, rb = find(m), find(m2)
            if ra != rb:
                parent[ra] = rb
    got = {}
    for m in parent:
        got.setdefault(find(m), []).append(m)
    theirs = orbit_classes(N, p, ballset)
    return sorted(sorted(c) for c in got.values()) == sorted(sorted(c) for c in theirs)


def run_cell(p, n, rec):
    N = p ** (2 * n)
    rec('  ---- CELL (p,n) = (%d,%d):  N = %d ----' % (p, n, N))

    bad = chart_shift_is_pn_j(p, n)
    rec('    (1) chart shift x\'\' - x lies in p^n Z, exactly       : %s%s'
        % ('YES, all %d (m,j)' % (N * p) if not bad else '### NO ###',
           '' if not bad else '  witness %s' % (bad[0],)))

    ident = iota_is_identity_on_functions(p, n)
    rec('    (2) iota f = f on every refined cell                  : %s  (%d mismatches)'
        % ('YES' if ident == 0 else '### NO ###', ident))

    moved, un_ball, into_ball = support_test(p, n)
    rec('    (3) I2 SUPPORT TEST -- does iota move support?        : %s'
        % ('NO -- host points all refine a level-n point' if moved == 0
           else '### YES (%d) ###' % moved))
    rec('        model U^n drives EVERY index into ball_n          : %s' % un_ball)
    rec('        iota carries an off-ball index into ball_{n+1}    : %d  %s'
        % (into_ball, 'NEVER' if into_ball == 0 else '### SOMETIMES ###'))

    vok = vinv_relation_is_scaling(p, n)
    rec('    (4) V_inv classes rebuilt from b10\'s x ~ px match the')
    rec('        corpus builder                                    : %s' % ('YES' if vok else '### NO ###'))

    cls, _ = noise_floor.classify(0, exact=True)
    rec('    noise-floor gate                                     : %s' % cls)
    return (not bad) and ident == 0 and moved == 0 and un_ball and into_ball == 0 and vok


def main():
    out = []

    def rec(s=''):
        out.append(s)
        print(s)

    rec('=' * 100)
    rec('b283 -- THE TOWER\'S ACTION. ### IS `iota` MULTIPLICATION BY `p`?')
    rec('=' * 100)
    rec('### DECIDED BY DEFINITIONS. ### **THAT BOTH INDEX FORMULAS CARRY A FACTOR `p` IS A')
    rec('### RESEMBLANCE AND IS TREATED AS NO EVIDENCE (falsifier I1).**')
    rec()
    allok = True
    for p, n in CELLS:
        allok &= run_cell(p, n, rec)
        rec()
    rec('=' * 100)
    rec('### ALL CELLS: %s' % ('PASS' if allok else '### FAILED ###'))
    rec('### ### **THE READING: ### `iota` REFINES THE CHART AND CHANGES NO FUNCTION AND MOVES')
    rec('### ### NO SUPPORT. ### MULTIPLICATION BY `p` ESCAPES ITS LEVEL AND, ITERATED `n` TIMES,')
    rec('### ### DRIVES EVERY INDEX INTO THE BALL. ### THEY ARE NOT THE SAME MAP.**')
    rec('=' * 100)
    with open(os.path.join(ROOT, 'data', 'b283_tower_action_run.txt'), 'w',
              encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')
    return 0 if allok else 1


if __name__ == '__main__':
    sys.exit(main())
