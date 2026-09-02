# -*- coding: utf-8 -*-
"""b295 -- THE SECOND MECHANISM. ### WHY DOES `Son(p,n; -1, 0)` GIVE ZERO?

### ### **THE INSTRUMENT THIS RUNNER CHANGES, AND WHY (falsifier Z3).**
### b294 asked whether a member "gives zero" and answered by computing `<A v, v>` on each vector
### of ONE basis. ### b281 (emitting) decided the form's type: ### **"`A != A^T`, so
### `A* = A^T != A`. THE FORM IS NEITHER HERMITIAN NOR SYMMETRIC"**. ### ### **A NON-SYMMETRIC
### ### FORM IS NOT DETERMINED BY ITS DIAGONAL ON A BASIS: the cross terms `<A v_i, v_j>` are
### ### not recovered from `<A v_i, v_i>`.** ### So this runner computes ### THE WHOLE MATRIX ###
### and separates three questions that b294's instrument could not:
###   (F) ### **THE FORM** ### `<A v_i, v_j>` -- is `M` identically zero?
###   (D) ### **THE FIRST-LEVEL VALUE ON THE WHOLE MEMBER** -- is `M + M^T` identically zero?
###       (`<A f, f>` for `f = SUM c_i v_i` with rational `c` is `c^T (M) c = c^T ((M+M^T)/2) c`,
###       so the diagonal value vanishes on the WHOLE member exactly when `M + M^T = 0`.)
###   (B) ### **b294's OWN SCAN** -- how many basis vectors have `<A v_i, v_i> != 0`.
### ### **ALL THREE ARE PRINTED FOR EVERY MEMBER SO THAT THEY ARE COMPARED, NEVER CONFLATED.**

### ### **THE DERIVED CRITERION THIS RUN CONTROLS (registered before any code existed):**
### With `q = p^n`, `A f` is ball-supported and `g(q m mod N)` depends on `m` only mod `q`, so
###   ### **`<A f, g> = SUM over r in Z/q of conj(g(q r)) * G_f(r)`,
###       `G_f(r) = SUM over m = r mod q of (S_quot f)(m)`.**
### `a >= 0` makes `g` vanish on the ball, killing every `conj(g(q r))`. ### And with
### `e0 = v_p(r)`, `r0 = r/p^{e0}`, `|C| = (p^n-1)/(p-1)`,
###   ### **`G_f(r) = (p^{n-e0-1}/|C|) * SUM over e in [0,n-1] of Fib_{n+e-e0}(p^e r0)`**,
### and the transform-side condition at exponent `b` kills every term with `e <= b + e0`.
###   ### ### **SO THE FORM VANISHES IDENTICALLY WHENEVER `a >= 0` OR `b >= n - 1`.**
### ### **THE TWO THRESHOLDS ARE NOT THE SAME NUMBER. ### THE FUNCTION-SIDE ONE IS THE OBJECT'S
### ### OWN RADIUS AND DOES NOT MOVE; THE TRANSFORM-SIDE ONE IS `n - 1` AND MOVES WITH THE LEVEL.
### ### THEY COINCIDE AT LEVEL 1 AND NOWHERE ELSE, WHICH IS WHY `(2,3)` IS IN THE CELL LIST.**

### ### **EXPOSURE TO THE ESCAPED-MASS ARTIFACT (Z5): ### NONE, AND THE REASON IS GIVEN.** ###
### This runner applies ### **NO LEVEL-SHIFTING MAP.** ### Members are defined by radii, not by
### scaling; the pairing is b273's `A` at `k = n`, within one level, the same operator b270, b281
### and b294 used. ### **THE ARTIFACT LIVES IN `g` AND `h`, WHICH DO NOT APPEAR IN THIS FILE.**

### ### **ZERO FLOAT TOKENS.** ### Members by exact Gaussian elimination over `Fraction`; the
### form matrix over `Fraction` (b281: `A` is a RATIONAL matrix, and on the rational span the
### `conj` is the identity -- said here rather than left as a silent omission); the exhibited
### witnesses re-valued independently in `Q(zeta_N)`.
"""
import os
import sys
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(ROOT, 'tools'))

import noise_floor                                                    # noqa: E402
from b270_ambient_pairing import Field, ball_of                       # noqa: E402
from b281_compression import matrix_A, apply_A                        # noqa: E402
from b293_finite_family import (basis_family, in_family,              # noqa: E402
                                transform_vanishes)
from b294_family_value import pair_at_n                               # noqa: E402

# ### b294's FIVE, KEPT FOR COMPARABILITY, PLUS THE LEVEL-3 DISCRIMINATOR, DECLARED AT
# ### REGISTRATION AND NOT SLIPPED IN.
CELLS = [(2, 1), (2, 2), (3, 1), (3, 2), (5, 1), (2, 3)]

# ### THE TWO WITNESSES WRITTEN INTO THE SEALED REGISTRATION BEFORE ANY CODE EXISTED.
# ### (cell, (a,b), {index: coefficient}, predicted exact value)
REGISTERED_WITNESSES = [
    ((2, 2), (-1, 0), {2: 1, 6: -1, 4: 1, 12: -1}, Fraction(4, 3)),
    ((2, 3), (-1, 1), {4: 1, 20: -1, 8: 1, 24: -1}, Fraction(4, 7)),
]


def forced_zero(a, b, n):
    """### THE DERIVED CRITERION. ### **SUFFICIENT, DERIVED. ### NECESSITY IS NOT CLAIMED.**"""
    return (a >= 0) or (b >= n - 1)


def form_matrix(A, basis, N, ballset):
    """### `M[i][j] = <A v_i, v_j>`, EXACT OVER `Fraction`.

    ### **`A f` IS SUPPORTED ON THE BALL** -- `A`'s row index is `l = p^n m`, which lies in
    ### `ball_n` for every `m` (b281's own sentence) -- so each entry is a sum over `q` indices
    ### and no dense `N x N` object is formed."""
    Av = [apply_A(A, v, N) for v in basis]
    M = []
    for i in range(len(basis)):
        row = []
        for j in range(len(basis)):
            s = Fraction(0)
            for l in ballset:
                if Av[i][l] and basis[j][l]:
                    s += Av[i][l] * basis[j][l]
            row.append(s)
        M.append(row)
    return M


def first_nonzero(M):
    for i, row in enumerate(M):
        for j, x in enumerate(row):
            if x != 0:
                return (i, j, x)
    return None


def diag_witness(M, basis, N):
    """### **A WITNESS FOR THE FIRST-LEVEL VALUE, EXHIBITED AS A VECTOR AND NOT AS A NUMBER
    ### (Z4).** ### `<A f, f>` for `f = SUM c_i v_i` is `c^T M c`, so a nonzero diagonal value
    ### exists exactly when `M + M^T != 0`, and `(i,i)` or `v_i + v_j` realizes it."""
    d = len(M)
    for i in range(d):
        if M[i][i] != 0:
            return basis[i], M[i][i], ('e_%d' % i)
    for i in range(d):
        for j in range(i + 1, d):
            s = M[i][j] + M[j][i]
            if s != 0:
                v = [basis[i][k] + basis[j][k] for k in range(N)]
                return v, s, ('v_%d + v_%d' % (i, j))
    return None, None, None


def run_cell(p, n, rec, tally):
    N = p ** (2 * n)
    q = p ** n
    ballset = sorted(ball_of(N, p, n))
    A = matrix_A(N, p, n, n)
    F = Field(N)
    csize = (p ** n - 1) // (p - 1)
    rec('  ---- CELL (p,n) = (%d,%d):  N = %d,  q = %d,  |class| = %d,  n-1 = %d ----'
        % (p, n, N, q, csize, n - 1))

    # ### Z1's NOT-DEAD WITNESS, BEFORE ANY ZERO IS REPORTED. ### A zero from a dead instrument
    # ### is not a zero.
    g0 = [Fraction(2)] * N
    g0[0] += 2 * q
    w = F.reduce(pair_at_n(A, g0, N, F))
    banked = 4 * (N - q)
    ok1 = bool(w) and w[0] == banked and all(c == 0 for c in w[1:])
    tally['z1'].append(ok1)
    rec('    Z1 NOT-DEAD WITNESS: <A g_0, g_0> = %-8s  b271 banked 4(N-q) = %-8s  %s'
        % (w[0] if w else 0, banked, 'MATCH' if ok1 else '### NO ###'))

    rec('    %-9s %-6s %-5s %-16s %-24s %-11s %s'
        % ('(a,b)', 'dim', 'crit', 'FORM <Av_i,v_j>', 'FIRST-LEVEL VALUE (M+M^T)',
           "b294's scan", 'agreement'))
    for a in range(-n, n + 1):
        for b in range(-n, n + 1):
            basis = [v for v in basis_family(p, n, a, b) if any(x != 0 for x in v)]
            if not basis:
                rec('    (%+d,%+d)   %-6s ### **EMPTY MEMBER -- CANNOT TEST** (Z2)'
                    % (a, b, '-'))
                tally['cannot_test'] += 1
                continue
            M = form_matrix(A, basis, N, ballset)
            fnz = first_nonzero(M)
            Msym_w, Msym_v, Msym_lbl = diag_witness(M, basis, N)
            bscan = sum(1 for i in range(len(basis)) if M[i][i] != 0)
            crit = forced_zero(a, b, n)

            form_s = 'ZERO' if fnz is None else 'NONZERO'
            val_s = 'ZERO ON THE MEMBER' if Msym_w is None else ('NONZERO = %s' % Msym_v)

            # ### THE AGREEMENT CELL. ### **A CRITERION THAT FORCES A ZERO WHERE THE FORM IS
            # ### NONZERO IS A REFUTED DERIVATION, AND IT IS COUNTED SEPARATELY.**
            if crit and fnz is not None:
                agree = '### REFUTES THE DERIVATION ###'
                tally['refute_derivation'].append((p, n, a, b))
            elif crit:
                agree = 'derived zero, confirmed'
                tally['derived_confirmed'] += 1
            elif Msym_w is None:
                agree = 'NOT FORCED, zero anyway'
                tally['not_necessary'].append((p, n, a, b))
            else:
                agree = '### NOT FORCED, AND NONZERO ###'
                tally['live_nonzero'].append((p, n, a, b, Msym_v))

            rec('    (%+d,%+d)   %-6d %-5s %-16s %-24s %-11s %s'
                % (a, b, len(basis), 'ZERO' if crit else '-', form_s, val_s,
                   '%d/%d' % (bscan, len(basis)), agree))

            # ### Z8 -- THE BARRIER MUST SURVIVE THIS ACT'S OWN INSTRUMENT.
            if a >= 0:
                tally['z8'].append((p, n, a, b, fnz is None))

            # ### THE SEPARATION b294's INSTRUMENT COULD NOT SEE, NAMED WHERE IT OCCURS.
            if bscan == 0 and Msym_w is not None:
                tally['basis_blind'].append((p, n, a, b, Msym_v, Msym_lbl))
                rec('        ### ### **b294\'s INSTRUMENT WOULD REPORT THIS MEMBER ZERO.** ###'
                    ' The whole-member value is %s, carried by %s.' % (Msym_v, Msym_lbl))
                sup = [(k, Msym_w[k]) for k in range(N) if Msym_w[k]]
                rec('        witness support : %s' % sup[:8])
                rec('        witness lies in the member (both conditions, exact) : %s'
                    % ('YES' if in_family(Msym_w, p, n, a, b) else '### NO ###'))
                rec('        witness transform really vanishes on B_b in Q(zeta_%d)  : %s'
                    % (N, 'YES' if transform_vanishes(Msym_w, p, n, b) else '### NO ###'))
                cyc = F.reduce(pair_at_n(A, Msym_w, N, F))
                rec('        SAME VALUE THROUGH THE CYCLOTOMIC INSTRUMENT          : %s  %s'
                    % (cyc[:3] if cyc else [0],
                       'AGREE' if (cyc and cyc[0] == Msym_v and all(c == 0 for c in cyc[1:]))
                       else '### DISAGREE ###'))
                onball = [k for k in ballset if Msym_w[k]]
                rec('        witness mass ON the ball (the object forbids it)      : %s'
                    % (onball[:6] if onball else '### NONE ###'))

    cls, _ = noise_floor.classify(0, exact=True)
    rec('    noise-floor gate : %s   (exact rational form matrix, exact cyclotomic re-valuation)'
        % cls)


def registered_witnesses(rec, tally):
    """### **THE TWO VECTORS WRITTEN INTO THE SEALED REGISTRATION, CHECKED AS WRITTEN (Z4).**"""
    rec('=' * 100)
    rec('### THE REGISTERED WITNESSES. ### **WRITTEN BEFORE ANY CODE EXISTED; CHECKED HERE.**')
    rec('=' * 100)
    for (p, n), (a, b), spec, predicted in REGISTERED_WITNESSES:
        N = p ** (2 * n)
        F = Field(N)
        A = matrix_A(N, p, n, n)
        f = [Fraction(0)] * N
        for k, c in spec.items():
            f[k] = Fraction(c)
        inf = in_family(f, p, n, a, b)
        tv = transform_vanishes(f, p, n, b)
        cyc = F.reduce(pair_at_n(A, f, N, F))
        got = cyc[0] if cyc else Fraction(0)
        pure = bool(cyc) and all(c == 0 for c in cyc[1:])
        hit = inf and tv and pure and got == predicted
        tally['registered'].append(hit)
        rec('  (p,n) = (%d,%d)   member (a,b) = (%+d,%+d)   f = %s'
            % (p, n, a, b, ' '.join('%+d*e_%d' % (c, k) for k, c in sorted(spec.items()))))
        rec('    in the member by BOTH conditions (exact)              : %s'
            % ('YES' if inf else '### NO ###'))
        rec('    transform really vanishes on B_b, computed in Q(zeta_%d) : %s'
            % (N, 'YES' if tv else '### NO ###'))
        rec('    <A f, f>  PREDICTED %-8s   COMPUTED %-8s          : %s'
            % (predicted, got, 'MATCH' if hit else '### NO ###'))
        # ### THE NEGATIVE CONTROL: a non-member must be rejected by the same test.
        spike = [Fraction(0)] * N
        spike[p ** n] = Fraction(1)          # ### a lone spike ON the ball
        rec('    NEGATIVE CONTROL -- a lone on-ball spike is rejected   : %s'
            % ('YES' if not in_family(spike, p, n, a, b) else '### NO ###'))


def main():
    out = []

    def rec(s=''):
        out.append(s)
        print(s)

    tally = dict(z1=[], z8=[], registered=[], cannot_test=0, derived_confirmed=0,
                 refute_derivation=[], not_necessary=[], live_nonzero=[], basis_blind=[])

    rec('=' * 100)
    rec('b295 -- THE SECOND MECHANISM. ### THE FORM, NOT THE DIAGONAL ON ONE BASIS.')
    rec('=' * 100)
    rec('### **NO LEVEL-SHIFTING MAP APPEARS. ### NOT EXPOSED TO THE ESCAPED-MASS ARTIFACT (Z5).**')
    rec('### THE DERIVED CRITERION UNDER TEST: ### **THE FORM VANISHES IF `a >= 0` OR `b >= n-1`.**')
    rec('### `crit` = ZERO means the criterion FORCES a zero. ### A NONZERO FORM IN A `crit = ZERO`')
    rec('### row REFUTES THE DERIVATION and is counted separately.')
    rec()
    for p, n in CELLS:
        run_cell(p, n, rec, tally)
        rec()

    registered_witnesses(rec, tally)
    rec()

    rec('=' * 100)
    rec('### THE CLOSING TALLY.')
    rec('=' * 100)
    rec('  Z1 not-dead witness, cells matching b271     : %d/%d'
        % (sum(1 for x in tally['z1'] if x), len(tally['z1'])))
    z8ok = sum(1 for r in tally['z8'] if r[4])
    rec('  Z8 THE BARRIER -- `a >= 0` members with the  ')
    rec('     WHOLE FORM identically zero              : %d/%d  %s'
        % (z8ok, len(tally['z8']), 'PASS' if z8ok == len(tally['z8']) else '### FAIL ###'))
    rec('  Z2 empty members reporting CANNOT TEST       : %d' % tally['cannot_test'])
    rec('  criterion forces zero, confirmed             : %d' % tally['derived_confirmed'])
    rec('  ### CRITERION FORCES ZERO BUT FORM NONZERO   : %d  %s'
        % (len(tally['refute_derivation']),
           'NONE -- THE DERIVATION SURVIVES' if not tally['refute_derivation']
           else '### THE DERIVATION IS REFUTED ###'))
    for r in tally['refute_derivation']:
        rec('      ### (p,n)=(%d,%d) member (%+d,%+d)' % r)
    rec('  not forced, and the value is NONZERO         : %d'
        % len(tally['live_nonzero']))
    for r in tally['live_nonzero']:
        rec('      (p,n)=(%d,%d) member (%+d,%+d)  value %s' % r)
    rec('  not forced, zero anyway (SUFFICIENT-NOT-')
    rec('     NECESSARY, printed rather than absorbed)  : %d'
        % len(tally['not_necessary']))
    for r in tally['not_necessary']:
        rec('      (p,n)=(%d,%d) member (%+d,%+d)' % r)
    rec('  ### MEMBERS b294\'s INSTRUMENT WOULD CALL ZERO')
    rec('  ### AND WHOSE FIRST-LEVEL VALUE IS NOT ZERO  : %d' % len(tally['basis_blind']))
    for r in tally['basis_blind']:
        rec('      (p,n)=(%d,%d) member (%+d,%+d)  value %s  carried by %s' % r)
    rec('  registered witnesses landing exactly         : %d/%d'
        % (sum(1 for x in tally['registered'] if x), len(tally['registered'])))
    rec('=' * 100)

    with open(os.path.join(ROOT, 'data', 'b295_mechanism_run.txt'), 'w',
              encoding='utf-8') as fh:
        fh.write('\n'.join(out) + '\n')

    bad = (not all(tally['z1'])) or (not all(r[4] for r in tally['z8'])) \
        or bool(tally['refute_derivation'])
    return 1 if bad else 0


if __name__ == '__main__':
    sys.exit(main())
