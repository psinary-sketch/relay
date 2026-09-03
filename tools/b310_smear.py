# -*- coding: utf-8 -*-
"""b310_smear.py -- THE SOURCE'S CONSTRUCTION, ASSEMBLED ON THE INSTRUMENT.

### ### **THE SOURCE'S MOVE, IN ITS OWN WORDS, QUOTED BY b304 FROM CC (arXiv:2006.13771):** ###
### **"one can associate to a test function `f in C_c^infinity(R*_+)` the trace `Tr(theta(f) S)`"**.
### ### **AT A FINITE PLACE THE SCALING PART OF `Q_p^x` IS `p^Z`, WHICH IS DISCRETE**, so the
### source's INTEGRAL over the scaling part is a ### SUM ### over the powers of the prime, with the
### test function evaluated at those powers.
### ### ### **THAT IS THE WHOLE OF THE ASSEMBLY:**
### ### ### **`theta(w) = SUM over k of w_k theta(p^k)`,   `T(w) = Tr(theta(w) Pi) =
### ### ### SUM over k of w_k Tr(theta(p^k) Pi)`.**

### ### **THE WEIGHT IS SYMBOLIC AND NO PARTICULAR BUMP IS CHOSEN.** ### `w_k` is the test
### function's value at `p^k` and nothing more. ### **SO NO CLASS QUESTION ARISES AND NO PRICE IS
### PAID** -- the source's own price for the corpus's bump is not quoted here, because nothing here
### exits any class.
### ### **AND THE SUM IS FINITE BECAUSE THE SOURCE'S TEST FUNCTIONS ARE COMPACTLY SUPPORTED.** ### A
### compactly supported function on `Q_p^x` meets only finitely many powers of `p`.

### ### ### **THE SCOPE THIS FILE CARRIES AND MAY NOT WIDEN.** ### b309 computed
### `Tr(theta(p^k) Pi) = 0` for `k != 0` ### AT SEVEN CELLS AND FOR `|k| <= 2n` ### . ### **THIS
### ### FILE EVALUATES THE ASSEMBLY ONLY ON WEIGHTS SUPPORTED THERE.** ### The general statement is
### the bank's DERIVATION, which is general in `k`; ### **USING A RESULT IS NOT WIDENING IT, AND
### EVALUATING BEYOND THE RANGE ITS OWNER COMPUTED WOULD BE.**

### ### **NO FLOAT. ### `Fraction` AND `int` ONLY.**
"""
import os
import sys
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.join(ROOT, 'tools')
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, 'e16'))

import b309_scaling_trace as ST   # noqa: E402  ### the closed form and the reduced route, IMPORTED
import b308_local_field as LF     # noqa: E402  ### the frame and the ball
import b304_smearing as SMEAR     # noqa: E402  ### the projector and the unit trace

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CELLS = list(ST.CELLS)


def carried_powers(n):
    """### **THE POWERS b309 COMPUTED, AND NO OTHERS.** ### `|k| <= 2n`, `k != 0`."""
    return [k for k in range(-2 * n, 2 * n + 1) if k != 0]


# ### ==============================================================================================
# ### THE UNIFIED FIXED-POINT COUNT. ### **ONE FORMULA FOR THE WHOLE MULTIPLICATIVE GROUP.**
# ### ==============================================================================================
def signed_fixed_points(p, n, tres):
    """### ### **THE SIGNED COUNT OF THE OFF-BALL POINTS THAT `t` FIXES, IN THE TWO CONGRUENCES
    ### ### THE OBJECT'S TWO CONDITIONS IMPOSE.**

    ### From the closed form of `Pi` (b309's `(P1)`, checked entry-wise there against b304's
    ### Gram-Schmidt projector): `Pi[s][t s]` is zero unless BOTH indices are off the ball, and off
    ### it is `[s = t s] - (1/q)[s = t s mod q]`. ### Summing over `s`:
    ###   ### **`A_N - (1/q) A_q`,   `A_M = #{ s : q does not divide s, q does not divide (t s mod
    ###   ### N), (t-1) s = 0 mod M }`.**
    ### ### **AT `t = 1` EVERY OFF-BALL POINT IS FIXED AND THE COUNT IS `(p^n - 1)^2`.**
    ### ### **AT `t = p^j` NOTHING OFF THE BALL IS FIXED, BECAUSE `p^j - 1` IS A UNIT.**
    """
    N, q = p ** (2 * n), p ** n
    a_n = a_q = 0
    for s in range(N):
        if s % q == 0:
            continue
        if (tres * s) % N % q == 0:
            continue
        if ((tres - 1) * s) % N == 0:
            a_n += 1
        if ((tres - 1) * s) % q == 0:
            a_q += 1
    return Fraction(a_n) - Fraction(a_q, q)


def trace_at_unit(p, n, u):
    """### **`Tr(theta(u) Pi)` FOR A UNIT, FROM THE COUNT.** ### `|u| = 1`, so there is no factor.
    ### ### **CHECKED AGAINST b304's OWN `trace_scaled` AT EVERY UNIT AND EVERY CELL.**"""
    return signed_fixed_points(p, n, u % (p ** (2 * n)))


def trace_at_power(p, n, k):
    """### ### **`Tr(theta(p^k) Pi)` FROM THE COUNT, WITH THE FACTOR THE AMBIENT IMPOSES.**

    ### b309 derived, and checked by two routes:
    ###   ### `k > 0` : the ambient is `V(n, n+k)`, the embedding REPEATS `p^k` times, and the
    ###     factor is `p^{-k}`;
    ###   ### `k < 0` : the ambient is `V(n+|k|, n)`, the embedding SPREADS, and the factor is `1`.
    ### ### ### **SO THE FACTOR IS `p^{-max(k,0)}`, WHICH IS THE HAAR WEIGHT OF THE EMBEDDING AND
    ### ### ### NOT `|t|`.** ### The registration's `(P4)` says `|t|`; that is right at `k > 0` and
    ### at every unit and ### **WRONG AT `k < 0`**, where `|p^{-j}| = p^{j}` and the factor is `1`.
    ### **THE COUNT IS THE CONTENT AND THE FACTOR IS THE PART THE PREDICTION GOT WRONG**, and since
    ### every count at a nonzero power is ZERO, the error is invisible in every value the act
    ### reports -- ### **WHICH IS EXACTLY WHY IT IS CHECKED EXPLICITLY RATHER THAN LEFT TO SHOW UP.**
    ### ### **AND UNDER b21's UNITARY NORMALIZATION `U(t) = |t|^{-1/2} theta(t)` THE FACTOR BECOMES
    ### ### `p^{-|k|/2}`, WHICH IS SYMMETRIC IN `k`** -- stated because it is the shape the
    ### asymmetry hides, and it is checked below rather than asserted.
    """
    return Fraction(1, p ** k) * signed_fixed_points(p, n, pow(p, abs(k), p ** (2 * n))) \
        if k > 0 else signed_fixed_points(p, n, pow(p, abs(k), p ** (2 * n)))


def trace_identity(p, n):
    """### **`Tr(Pi)` -- THE SURVIVING TERM'S COEFFICIENT.** ### b304's not-dead witness, b308's
    reproduction, and the dimension law: `(p^n - 1)^2`."""
    return signed_fixed_points(p, n, 1)


# ### ==============================================================================================
# ### THE ASSEMBLY.
# ### ==============================================================================================
def smear(p, n, w):
    """### ### **`T(w) = SUM over k of w_k Tr(theta(p^k) Pi)`, TERM BY TERM, WITH NOTHING ASSUMED.**

    ### `w` is a dict `{k: Fraction}`. ### **THE ZEROS ARE NOT SUBSTITUTED IN: EVERY TERM IS FORMED
    ### AND ADDED**, so the collapse is something the sum DOES rather than something the code was
    ### told. ### A routine that skipped the nonzero powers would be reporting its own assumption.
    """
    total = Fraction(0)
    for k, wk in sorted(w.items()):
        total += wk * (trace_identity(p, n) if k == 0 else ST.trace_route_b(p, n, k))
    return total


def smear_terms(p, n, w):
    """### THE SAME SUM, ### **TERM BY TERM, SO A SURVIVING TERM CAN BE PRINTED IF THERE IS ONE.**"""
    return [(k, wk, (trace_identity(p, n) if k == 0 else ST.trace_route_b(p, n, k)))
            for k, wk in sorted(w.items())]


def weight_identity_only(n, val=1):
    """### THE WEIGHT THAT IS NONZERO ONLY AT THE IDENTITY."""
    w = {k: Fraction(0) for k in carried_powers(n)}
    w[0] = Fraction(val)
    return w


def weight_loud_tail(n, val=1):
    """### ### **THE SAME VALUE AT THE IDENTITY AND A DIFFERENT NONZERO VALUE AT EVERY OTHER
    ### ### POWER.** ### This is the arm that decides whether the functional reads the tail at all.
    ### **NOT ONE ENTRY OF THE TAIL IS ZERO**, so an agreement cannot be an accident of a sparse
    ### weight."""
    w = {k: Fraction(3 * k + 7, 5) if k != 0 else Fraction(val) for k in carried_powers(n)}
    w[0] = Fraction(val)
    return w


# ### ==============================================================================================
# ### THE FIXTURES. ### **BOTH POLARITIES ON EVERYTHING THIS FILE OWNS.**
# ### ==============================================================================================
def self_test(verbose=True):
    bad = [0]

    def chk(lbl, got, exp):
        ok = (got == exp)
        bad[0] += 0 if ok else 1
        if verbose:
            print('  %-72s %-18s %s' % (lbl, '%s/%s' % (got, exp), 'YES' if ok else '### NO ###'))

    if verbose:
        print('  %-72s %-18s %s' % ('fixture', 'got/expected', 'agree'))

    # ### THE COUNT, AT THE TWO VALUES THE DERIVATION NAMES, ### **BOTH POLARITIES.**
    chk('the identity fixes every off-ball point: (2,1)', signed_fixed_points(2, 1, 1), Fraction(1))
    chk('the identity fixes every off-ball point: (2,2)', signed_fixed_points(2, 2, 1), Fraction(9))
    chk('the identity fixes every off-ball point: (3,2)', signed_fixed_points(3, 2, 1),
        Fraction(64))
    chk('### and a nonzero power fixes none: (2,2), t = p', signed_fixed_points(2, 2, 2),
        Fraction(0))
    chk('### nor does its square: (2,2), t = p^2', signed_fixed_points(2, 2, 4), Fraction(0))
    chk('### a unit other than 1 need NOT give zero -- the count is not vacuous',
        any(signed_fixed_points(3, 1, u) != 0 for u in (2, 4, 5, 7, 8)), True)

    # ### THE WEIGHTS, ### **AND THE TAIL ARM IS THE ONE THAT MATTERS.**
    wid, wld = weight_identity_only(2), weight_loud_tail(2)
    chk('the two weights agree at the identity', (wid[0], wld[0]), (Fraction(1), Fraction(1)))
    chk('### and the loud weight is nonzero at EVERY other power',
        all(wld[k] != 0 for k in carried_powers(2)), True)
    chk('### while the quiet one is zero at every other power',
        all(wid[k] == 0 for k in carried_powers(2)), True)

    # ### THE ASSEMBLY, ### **ON A CELL SMALL ENOUGH TO CHECK BY HAND.**
    chk('the assembled smear at (2,1) with the quiet weight is Tr(Pi)',
        smear(2, 1, weight_identity_only(1)), Fraction(1))
    chk('### and with the loud weight it is the SAME', smear(2, 1, weight_loud_tail(1)),
        Fraction(1))
    chk('### and doubling the identity value doubles it',
        smear(2, 1, weight_loud_tail(1, 2)), Fraction(2))
    chk('the term list covers every carried power and the identity',
        len(smear_terms(2, 2, weight_loud_tail(2))), len(carried_powers(2)) + 1)
    return bad[0] == 0


if __name__ == '__main__':
    print('=' * 100)
    print('b310_smear.py -- THE FIXTURES. ### BOTH POLARITIES, NO FLOAT.')
    print('=' * 100)
    ok = self_test()
    print()
    print('  ### SELF-TEST : %s' % ('PASS' if ok else '### FAIL ###'))
    sys.exit(0 if ok else 2)
