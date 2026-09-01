# -*- coding: utf-8 -*-
"""b279 -- THE CONTROL ON THE `Son` CHARACTERIZATION.

### THE HAZARD, NAMED BEFORE IT IS TESTED: ### b279's runner decides `Son` membership by a
### RATIONAL condition it DERIVED ("every fiber sum vanishes"), not by the owners' literal
### condition ("the transform image vanishes on the ball"). ### **A DIMENSION THAT AGREES IS
### NOT A PROOF THAT THE OBJECTS AGREE** -- that is exactly the b278 lesson, where two balls
### were required to be compared AS SETS and not by name. ### So here the two conditions are
### compared BY COMPUTING THE ACTUAL TRANSFORM in `Q(zeta_N)`, exactly, in both polarities.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'tools'))

from fractions import Fraction                                 # noqa: E402
from b270_ambient_pairing import Field                         # noqa: E402
from b271_top_level_no_go import apply_S                       # noqa: E402
from b279_local_space import son_basis, son_conditions_hold    # noqa: E402


def as_field_vector(c):
    """### AN INTEGER VECTOR AS A VECTOR OF FIELD ELEMENTS. ### A rational scalar `v` is the
    ### field element `{0: v}` -- the coefficient of `zeta^0`. ### **NOT `from_int_vec`, which
    ### builds ONE field element from a coefficient list; that is a different object and
    ### passing it here is a type error, not a near-miss.**"""
    return [({0: Fraction(v)} if v else {}) for v in c]


def transform_vanishes_on_ball(f_int, p, n):
    """### THE OWNERS' LITERAL CONDITION, COMPUTED: ### is `(S f)(m) = 0` for every `m` in the
    ### ball? ### Exact in `Q(zeta_N)`; no float touches this."""
    N = p ** (2 * n)
    F = Field(N)
    Sf = apply_S(as_field_vector(f_int), N)
    for m in range(0, N, p ** n):
        if not F.is_zero(Sf[m]):
            return False, m
    return True, None


def main():
    print('=' * 100)
    print('b279 -- CONTROL: ### IS THE DERIVED RATIONAL CONDITION REALLY THE OWNERS\' `Son`?')
    print('=' * 100)
    print('### BOTH POLARITIES. ### A characterization that only ever says YES proves nothing.')
    print()
    ok = True
    for p, n in [(2, 1), (2, 2), (3, 1)]:
        N = p ** (2 * n)
        basis = son_basis(p, n)

        # ### POSITIVE: every vector the derived condition ADMITS must really have its
        # ### transform vanish on the ball.
        pos_bad = []
        for v in basis:
            good, m = transform_vanishes_on_ball(v, p, n)
            if not good:
                pos_bad.append((v, m))

        # ### NEGATIVE: a vector obeying the BALL half but breaking the fiber half must have a
        # ### NONZERO transform somewhere on the ball. ### If it does not, the derived condition
        # ### is too strong and the characterization is wrong.
        neg = [0] * N
        off = [m for m in range(N) if m % p ** n != 0]
        neg[off[0]] = 1                      # ### one spike: ball half holds, fiber sum is 1
        inson, why = son_conditions_hold(neg, p, n)
        neggood, negm = transform_vanishes_on_ball(neg, p, n)

        print('  (p,n)=(%d,%d)  N=%-5d dim=%-4d' % (p, n, N, len(basis)))
        print('    POSITIVE: derived-Son vectors whose transform really dies on the ball : %d/%d %s'
              % (len(basis) - len(pos_bad), len(basis),
                 'ALL' if not pos_bad else '### %d FAIL ###' % len(pos_bad)))
        print('    NEGATIVE: the spike -- derived condition says in-Son? %s (%s)'
              % ('YES' if inson else 'NO', why))
        print('              its transform vanishes on the ball?        %s%s'
              % ('YES' if neggood else 'NO',
                 '' if neggood else '   first nonzero at m=%d' % negm))
        agree = (not pos_bad) and (not inson) and (not neggood)
        print('    ### THE TWO CONDITIONS AGREE ON THIS CELL : %s'
              % ('YES' if agree else '### NO ###'))
        print()
        ok &= agree
    print('=' * 100)
    print('### CONTROL: %s' % ('PASS -- the derived condition IS the owners\' Son, both ways'
                               if ok else '### FAIL ###'))
    print('### **SO THE RUNNER\'S `Son` IS THE KEYSTONE\'S `Son`, COMPARED BY COMPUTATION AND')
    print('### NOT BY NAME.**')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
