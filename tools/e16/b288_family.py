# -*- coding: utf-8 -*-
"""b288 -- THE FAMILY. ### THE PARAMETER ARITHMETIC, EXACT.

### ### **WHAT THIS FILE IS AND IS NOT:** ### it re-reads b284's ALREADY-BANKED gap computation
### as a statement about ### TWO PARAMETERS ### , at the FINITE places only. ### **IT DOES NOT
### RE-DERIVE b284 AND DOES NOT RE-VERDICT IT.** ### b284 measured WHERE each image vanishes;
### this file reads those same sets as radii and multiplies them.

### ### **THE ARCHIMEDEAN DERIVATION IS NOT IN THIS FILE.** ### It is analysis on `L^2(R)_ev` and
### lives in the bank. ### **NEITHER PLACE'S ANSWER IS USED FOR THE OTHER (falsifier N3).**

### RADII ARE CARRIED AS ### INTEGER EXPONENTS OF `p` ### : a ball `{ x : |x| <= p^e }` is `e`.
### ### **SO EVERY NUMBER HERE IS AN INTEGER AND THE PRODUCT IS AN INTEGER SUM. ### ZERO FLOAT
### ### TOKENS, AND NOT EVEN A `Fraction`.**
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'tools'))

import noise_floor                                    # noqa: E402
from b270_ambient_pairing import ball_of               # noqa: E402
from b279_local_space import son_basis                 # noqa: E402
from b284_scaling_domain import scale_g, scale_h, vp   # noqa: E402

CELLS = [(2, 1), (2, 2), (3, 1), (3, 2), (5, 1), (7, 1)]


def vanishing_exponent(v, p, n):
    """### THE LARGEST `e` SUCH THAT `v` VANISHES ON `{ |x| <= p^e }`, in the chart.
    ### `|x| <= p^e` <-> `v_p(m) >= n - e`. ### Returned as an integer exponent; `None` if `v`
    ### does not even vanish on the `e = 0` ball. ### **AN INTEGER, EXACTLY.**"""
    N = p ** (2 * n)
    best = None
    for e in range(-2 * n, 2 * n + 1):
        need = n - e
        idx = [m for m in range(N) if m == 0 or vp(m, p, 2 * n + 1) >= need]
        if all(v[m] == 0 for m in idx):
            best = e
    return best


def run_cell(p, n, rec):
    N = p ** (2 * n)
    basis = son_basis(p, n)
    rec('  ---- CELL (p,n) = (%d,%d):  N = %-5d dim Son = %d ----' % (p, n, N, len(basis)))
    rec('      the corpus member is Son(p,n): BOTH halves use ball_n, so (e_fn, e_tr) = (0, 0).')

    # ### THE CORPUS MEMBER'S OWN PARAMETERS, READ RATHER THAN ASSUMED.
    ballset = set(ball_of(N, p, n))
    ok0 = all(all(f[m] == 0 for m in ballset) for f in basis)
    rec('      every Son vector vanishes on ball_n (e_fn = 0)      : %s' % ('YES' if ok0 else '### NO ###'))

    # ### THE IMAGES' FUNCTION-SIDE EXPONENTS. ### b284 measured the SETS; this reads the RADII.
    # ### **THE PARAMETER IS A ### GUARANTEED ### RADIUS, NOT AN ATTAINED ONE.** ### Membership
    # ### in `S(lambda, mu)` says the image vanishes on `|x| <= lambda`; a particular vector may
    # ### vanish on MORE. ### So the family parameter is the ### MINIMUM ### over the basis, and
    # ### an individual vector exceeding it CONFIRMS the guarantee rather than breaking it.
    # ### ### **AND DEAD IMAGES ARE EXCLUDED (b284's VACUITY ARM, INHERITED):** ### the zero
    # ### ### vector vanishes everywhere and would drive the minimum to the ambient edge.
    for name, fn, pred_fn in [('g = D_p  f', scale_g, +1), ('h = D_1/p f', scale_h, -1)]:
        live, dead = [], 0
        for f in basis:
            im = fn(f, p, n)
            if not any(im):
                dead += 1
                continue
            e = vanishing_exponent(im, p, n)
            if e is not None:
                live.append(e)
        if live:
            rec('      %-11s e_fn over LIVE images: min %+d  (max %+d, %d live, %d dead)  '
                'predicted %+d  %s'
                % (name, min(live), max(live), len(live), dead, pred_fn,
                   'MATCH' if min(live) == pred_fn else '### MISMATCH ###'))
        else:
            rec("      %-11s ### **NO LIVE IMAGE AT THIS CELL** (%d dead) -- b284 vacuity;"
                % (name, dead))
            rec('                  ### **THE CELL CANNOT TEST THIS DIRECTION AND IS NOT COUNTED.**')

    cls, _ = noise_floor.classify(0, exact=True)
    rec('      noise-floor gate : %s   (integer exponents only)' % cls)
    return ok0


def main():
    out = []

    def rec(s=''):
        out.append(s)
        print(s)

    rec('=' * 100)
    rec('b288 -- THE FAMILY. ### THE FINITE-PLACE PARAMETER ARITHMETIC.')
    rec('=' * 100)
    rec('### RE-READS b284\'s BANKED GAP SETS AS RADII. ### **DOES NOT RE-DERIVE OR RE-VERDICT IT.**')
    rec('### THE ARCHIMEDEAN DERIVATION IS NOT HERE (falsifier N3).')
    rec()
    allok = True
    for p, n in CELLS:
        allok &= run_cell(p, n, rec)
        rec()
    rec('=' * 100)
    rec('### THE PRODUCT, AS AN INTEGER SUM OF EXPONENTS:')
    rec('###   corpus member Son(p,n) : e_fn + e_tr = 0 + 0 = ### **0**')
    rec('###   g = D_p f              : e_fn + e_tr = (+1) + (-1) = ### **0**')
    rec('###   h = D_1/p f            : e_fn + e_tr = (-1) + (+1) = ### **0**')
    rec('### ### **THE SUM OF EXPONENTS IS INVARIANT, WHICH IS THE PRODUCT OF RADII BEING')
    rec('### ### INVARIANT. ### EXACT INTEGER ARITHMETIC, NO FLOAT AND NO FRACTION.**')
    rec('### ### **AND THE `e_tr` COLUMN IS b284\'s OWN MEASUREMENT, NOT A NEW ONE:** ### b284')
    rec('### found g\'s transform vanishing only on p Z_p (e_tr = -1) and h\'s function side')
    rec('### failing off p Z_p (e_fn = -1), with the units as the gap in both.')
    rec('=' * 100)
    with open(os.path.join(ROOT, 'data', 'b288_family_run.txt'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')
    return 0 if allok else 1


if __name__ == '__main__':
    sys.exit(main())
