# -*- coding: utf-8 -*-
"""b284 -- THE SCALING'S DOMAIN. ### DOES THE GENUINE SCALING PRESERVE `S-bar_p`?

### THE DOUBLE NAME, KEPT AT EVERY USE:
###   ### **THE MODEL'S `U` ON `Z/N`** -- index arithmetic WITH WRAPAROUND. ### **A CONTROL.**
###   ### **THE GENUINE SCALING ON `Q_p`** -- where the derivation lives.
###   ### **`iota`** -- b283: the identity on functions, NOT a scaling. ### Not used here.
###   ### **THE TWO DIRECTIONS** -- `g(x) = f(px)` and `h(x) = f(x/p)`. ### **NOT THE SAME MAP**,
###     treated separately, never conflated.

### ### **THE CHART DICTIONARY, FROM b21's `x = p^{-n} m`, USED THROUGHOUT:**
###   ### `Z_p`      (the ball)  <->  `{ m : p^n | m }`
###   ### `Z_p^x`    (the units) <->  `{ m : v_p(m) = n exactly }`
###   ### `p Z_p`                <->  `{ m : v_p(m) >= n+1 }`
### ### **THE UNITS ARE THE BALL MINUS `p Z_p`, AND THEY ARE WHERE THIS ACT'S ANSWER LIVES.**

### ### **ZERO FLOAT TOKENS.**
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'tools'))

import noise_floor                                          # noqa: E402
from b270_ambient_pairing import Field, ball_of              # noqa: E402
from b271_top_level_no_go import apply_S                     # noqa: E402
from b279_local_space import son_basis                       # noqa: E402
from b279_son_control import as_field_vector                 # noqa: E402

CELLS = [(2, 1), (2, 2), (3, 1), (3, 2), (5, 1), (7, 1)]


def vp(m, p, cap):
    """### `v_p(m)`, capped. ### `v_p(0)` is infinite and is returned as the cap."""
    if m == 0:
        return cap
    v = 0
    while m % p == 0:
        m //= p
        v += 1
    return v


def units_of(N, p, n):
    """### `Z_p^x` IN THE CHART: ### indices divisible by `p^n` EXACTLY."""
    return [m for m in range(N) if m % (p ** n) == 0 and vp(m, p, 2 * n + 1) == n]


def scale_g(f, p, n):
    """### `g(x) = f(p x)`. ### In the chart the value at index `m` is `f` at index `p m`.
    ### ### **THE WRAPAROUND IS b21's DECLARED ARTIFACT AND IS CARRIED, NOT HIDDEN.**"""
    N = p ** (2 * n)
    return [f[(p * m) % N] for m in range(N)]


def scale_h(f, p, n):
    """### `h(x) = f(x/p)`. ### Nonzero only where `x/p` is a chart point, i.e. `p | m`."""
    N = p ** (2 * n)
    return [f[m // p] if m % p == 0 else 0 for m in range(N)]


def vanishes_on_ball_int(v, ballset):
    return all(v[m] == 0 for m in ballset)


def transform_vanishes_on_ball(v, p, n):
    N = p ** (2 * n)
    F = Field(N)
    Sv = apply_S(as_field_vector(v), N)
    bad = [m for m in range(0, N, p ** n) if not F.is_zero(Sv[m])]
    return (not bad), bad


def run_cell(p, n, rec):
    N = p ** (2 * n)
    ballset = set(ball_of(N, p, n))
    units = set(units_of(N, p, n))
    basis = son_basis(p, n)
    rec('  ---- CELL (p,n) = (%d,%d):  N = %-5d ball |%d|  units |%d|  dim Son = %d ----'
        % (p, n, N, len(ballset), len(units), len(basis)))

    res = {}
    for name, fn in [('g(x)=f(px)', scale_g), ('h(x)=f(x/p)', scale_h)]:
        fn_ok = tr_ok = 0
        fn_gap_units = tr_gap_units = 0
        fn_wit = tr_wit = None
        for f in basis:
            im = fn(f, p, n)
            # ### S1 -- THE FUNCTION-SIDE CONDITION.
            if vanishes_on_ball_int(im, ballset):
                fn_ok += 1
            else:
                nz = [m for m in ballset if im[m] != 0]
                if fn_wit is None:
                    fn_wit = (nz[0], im[nz[0]])
                if all(m in units for m in nz):
                    fn_gap_units += 1
            # ### S2 -- THE TRANSFORM-SIDE CONDITION.
            ok, bad = transform_vanishes_on_ball(im, p, n)
            if ok:
                tr_ok += 1
            else:
                if tr_wit is None:
                    tr_wit = bad[0]
                if all(m in units for m in bad):
                    tr_gap_units += 1
        # ### THE VACUITY ARM (falsifier J5, and b270's F-NONTRIV species). ### **AN IMAGE
        # ### THAT IS IDENTICALLY ZERO SATISFIES BOTH CONDITIONS AND PROVES NOTHING.**
        dead = sum(1 for f in basis if not any(fn(f, p, n)))
        res[name] = (fn_ok, tr_ok, fn_gap_units, tr_gap_units, fn_wit, tr_wit, dead)
        rec('    %-12s  ### VACUITY: images identically zero : %d of %d%s'
            % ('', dead, len(basis),
               '   ### **EVERY READING ABOVE IS VACUOUS HERE** ###' if dead == len(basis)
               else ''))
        rec('    %-12s  S1 function side : %2d/%-2d vanish on ball_n%s'
            % (name, fn_ok, len(basis),
               '' if fn_ok == len(basis)
               else '   ### FAILS ### first witness m=%d, value %s' % fn_wit))
        if fn_ok != len(basis):
            rec('                    ### every failing index lies in the UNITS : %s (%d of %d)'
                % ('YES' if fn_gap_units == len(basis) - fn_ok else '### NO ###',
                   fn_gap_units, len(basis) - fn_ok))
        rec('    %-12s  S2 transform side: %2d/%-2d vanish on ball_n%s'
            % ('', tr_ok, len(basis),
               '' if tr_ok == len(basis)
               else '   ### FAILS ### first witness m=%d' % tr_wit))
        if tr_ok != len(basis):
            rec('                    ### every failing index lies in the UNITS : %s (%d of %d)'
                % ('YES' if tr_gap_units == len(basis) - tr_ok else '### NO ###',
                   tr_gap_units, len(basis) - tr_ok))

    cls, _ = noise_floor.classify(0, exact=True)
    rec('    noise-floor gate : %s' % cls)
    return res


def main():
    out = []

    def rec(s=''):
        out.append(s)
        print(s)

    rec('=' * 100)
    rec('b284 -- THE SCALING\'S DOMAIN. ### BOTH DIRECTIONS, BOTH CONDITIONS, SEPARATELY.')
    rec('=' * 100)
    rec('### THE DERIVATION LIVES ON `Q_p`. ### **THIS RUNNER IS A CONTROL AND NEVER THE')
    rec('### EVIDENCE (falsifier J5).** ### b21 records the model wraparound as THE ARTIFACT.')
    rec()
    allres = {}
    for p, n in CELLS:
        allres[(p, n)] = run_cell(p, n, rec)
        rec()
    rec('=' * 100)
    rec('### THE PATTERN ACROSS ALL SIX CELLS:')
    for name in ('g(x)=f(px)', 'h(x)=f(x/p)'):
        s1 = all(allres[c][name][0] == len(son_basis(*c)) for c in CELLS)
        s2 = all(allres[c][name][1] == len(son_basis(*c)) for c in CELLS)
        rec('  %-12s  S1 function side holds everywhere : %-5s   S2 transform side holds : %s'
            % (name, s1, s2))
    rec('=' * 100)
    with open(os.path.join(ROOT, 'data', 'b284_scaling_run.txt'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())
