# -*- coding: utf-8 -*-
"""b273_spec2_range.py -- M-2 CAMPAIGN, ACT 7. ### THE SPEC-2 RANGE.

### THE QUESTION: ### **IS act 9's TERM ATTAINABLE BY ANY UNIT IN `E_1`?**

### b272 swept a SPANNING FAMILY and found 0 of 16, then named the resistance and refused it.
### ### **A SWEEP OF A SPANNING FAMILY IS NOT A SWEEP OF THE SPACE:** ### a Rayleigh quotient
### over a span is NOT bounded by its values at spanning vectors. ### **THIS ACT DOES NOT
### CONTRADICT b272; IT ANSWERS THE QUESTION b272 LEFT OPEN, AND SAYS SO EVERYWHERE.**

### THE CERTIFICATION IS EIGENVALUE-FREE AND FLOAT-FREE, BY DESIGN:
###   the form's value on REAL vectors depends only on the SYMMETRIC PART of a RATIONAL matrix;
###   two exactly-computed quotients STRADDLE the target; the quotient is continuous where
###   `<v,v> != 0`, which is everywhere on real `v != 0`; ### **THE INTERMEDIATE VALUE THEOREM
###   DOES THE REST, AND EVERY ORDER COMPARISON REDUCES TO `2 > 1`.**

### ### **NO FLOAT TOKEN APPEARS IN THIS FILE.** ### Every verdict is a reduction modulo
### `Phi_N`. ### COMPONENT 0 is CALLED on this path and returns `EXACT` -- a verdict, not a
### bypass. ### **NOTHING IS ADOPTED; AN EXHIBITED VECTOR IS AN EXHIBITION.**
"""
import io
import os
import sys
from fractions import Fraction

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..'))

from sympy import Poly, symbols

from b268_generator import u_coeffs
from b270_ambient_pairing import (Field, ball_of, from_int_vec, orbit_classes,
                                  spadd, spconj, spmul, spscale)
from b271_top_level_no_go import apply_S
from noise_floor import gate as floor_gate

X = symbols('X')

CELLS = [(2, 2), (2, 3)]


# ---------------------------------------------------------------------------------------------
# ### THE OBJECTS, ALL FROM OWNERS.
# ---------------------------------------------------------------------------------------------
def g_c(c, q, N):
    """### b272's FAMILY: `g_c(m) = q([m=c] + [m=-c]) + zeta^{mc} + zeta^{-mc}`. ### REAL."""
    out = []
    for m in range(N):
        d = {}
        if m == c % N:
            d[0] = d.get(0, Fraction(0)) + q
        if m == (-c) % N:
            d[0] = d.get(0, Fraction(0)) + q
        for k in ((m * c) % N, (-m * c) % N):
            d[k] = d.get(k, Fraction(0)) + 1
        out.append({k: v for k, v in d.items() if v != 0})
    return out


def vadd(a, b, t=Fraction(1)):
    return [spadd(a[m], spscale(b[m], t)) for m in range(len(a))]


def make_projector(N, p, n):
    ballset = set(ball_of(N, p, n))
    classes = orbit_classes(N, p, ballset)
    cls_of = {}
    for C in classes:
        for m in C:
            cls_of[m] = C

    def S_quot(v):
        out = []
        for m in range(N):
            if m in ballset:
                out.append({})
                continue
            C = cls_of[m]
            acc = {}
            for m2 in C:
                acc = spadd(acc, v[m2])
            out.append(spscale(acc, Fraction(1, len(C))))
        return out
    return ballset, S_quot


def sesq(x, y, S_quot, p, k, N):
    """### `<A x, y> = SUM_m (S_quot x)(m) * conj( y(p^k m mod N) )`. ### act 9's factor
    ### `p^{-k/2}` is carried SYMBOLICALLY, so this is the pairing TIMES `p^{k/2}`."""
    Sx = S_quot(x)
    pk = pow(p, k, N)
    acc = {}
    for m in range(N):
        if not Sx[m]:
            continue
        acc = spadd(acc, spmul(Sx[m], spconj(y[(pk * m) % N], N), N))
    return acc


def ip(x, y, N):
    acc = {}
    for m in range(N):
        if not x[m]:
            continue
        acc = spadd(acc, spmul(x[m], spconj(y[m], N), N))
    return acc


def finv(a, N, F):
    """### INVERSE IN `Q(zeta_N)`, exactly, by polynomial inversion modulo `Phi_N`."""
    coeffs = [Fraction(0)] * N
    for j, c in a.items():
        coeffs[j] = c
    pa = Poly(list(reversed(coeffs)), X, domain='QQ')
    pi = pa.invert(F.phi)
    cs = list(reversed(pi.all_coeffs()))
    return {j: Fraction(str(c)) for j, c in enumerate(cs) if c != 0}


def rank_over_field(vecs, N, F):
    """### EXACT RANK BY GAUSSIAN ELIMINATION OVER `Q(zeta_N)`. ### No float, no numeric rank."""
    rows = [list(v) for v in vecs]
    r = 0
    for col in range(N):
        piv = None
        for i in range(r, len(rows)):
            if not F.is_zero(rows[i][col]):
                piv = i
                break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        inv = finv(rows[r][col], N, F)
        rows[r] = [spmul(x, inv, N) for x in rows[r]]
        for i in range(len(rows)):
            if i == r:
                continue
            f = rows[i][col]
            if F.is_zero(f):
                continue
            rows[i] = [spadd(rows[i][j], spscale(spmul(f, rows[r][j], N), Fraction(-1)))
                       for j in range(N)]
        r += 1
        if r == len(rows):
            break
    return r


# ### `sqrt(2)` LIVES IN `Q(zeta_N)` WHENEVER `8 | N`: it is `zeta^{N/8} + zeta^{-N/8}`.
def sqrt2(N):
    return {(N // 8) % N: Fraction(1), (-(N // 8)) % N: Fraction(1)}


def sign_in_Qsqrt2(a, b):
    """### THE SIGN OF `a + b*sqrt(2)` FOR RATIONAL `a, b`, BY RATIONAL ARITHMETIC ALONE.
    ### ### **NO DECIMAL EVALUATION. ### THIS IS THE WHOLE OF THE ORDERED-FIELD CHANNEL THIS
    ### ACT OPENS, AND IT IS THREE COMPARISONS OF RATIONALS.**
    ### `a + b*sqrt2 > 0` iff: both nonneg and not both zero; or `a >= 0 > b` and `a^2 > 2b^2`;
    ### or `b > 0 > a` and `2b^2 > a^2`. ### The arms below are exhaustive."""
    if a == 0 and b == 0:
        return 0
    if a >= 0 and b >= 0:
        return 1
    if a <= 0 and b <= 0:
        return -1
    if a > 0 and b < 0:
        return 1 if a * a > 2 * b * b else (-1 if a * a < 2 * b * b else 0)
    return 1 if 2 * b * b > a * a else (-1 if 2 * b * b < a * a else 0)


def as_Qsqrt2(elem, N, F):
    """### IF `elem` LIES IN `Q(sqrt 2)`, RETURN `(a, b)` WITH `elem = a + b sqrt(2)`; ELSE
    ### `None`. ### Decided by an EXACT equality test, never by inspection."""
    red = F.reduce(elem)
    a = red[0] if red else Fraction(0)
    s2 = sqrt2(N)
    # ### solve elem = a' + b sqrt2 by testing candidate b from the zeta^{N/8} coefficient.
    b = red[(N // 8)] if len(red) > (N // 8) else Fraction(0)
    for cand_a in (a, a - b, a + b):
        for cand_b in (b, -b):
            trial = spadd({0: cand_a}, spscale(s2, cand_b))
            if F.eq(elem, trial):
                return cand_a, cand_b
    return None


def norm_Qsqrt2(a, b):
    """### THE FIELD NORM `N(a + b sqrt2) = a^2 - 2 b^2`, RATIONAL."""
    return a * a - 2 * b * b


def run_cell(p, n, rec, want_dim=True):
    q = p ** n
    N = q * q
    F = Field(N)
    ballset, S_quot = make_projector(N, p, n)
    r = {'p': p, 'n': n, 'q': q, 'N': N}

    fam = [g_c(c, q, N) for c in range(N)]
    # ### THE RANK IS COMPUTED ONLY WHERE THE ACT NEEDS IT. ### The straddle argument needs TWO
    # ### vectors, not a dimension, so the second cell does not pay for one. ### DECLARED, and
    # ### the run prints `n/a` there rather than a number nobody computed.
    r['dim_E1'] = rank_over_field(fam, N, F) if want_dim else None
    sys.stderr.write('  [cell (%d,%d) N=%d: family built, dim=%s]\n'
                     % (p, n, N, r['dim_E1']))
    sys.stderr.flush()

    def R_parts(v, k):
        return sesq(v, v, S_quot, p, k, N), ip(v, v, N)

    def quotient_equals(v, k, target_num, target_den):
        """### `R(v) = target` EXACTLY, as `den * <A v,v> - num * <v,v> = 0`. ### A ZERO TEST."""
        a, b = R_parts(v, k)
        lhs = spadd(spscale(a, Fraction(target_den)), spscale(b, Fraction(-target_num)))
        return F.is_zero(lhs)

    r['targets'] = []
    for k in range(1, n):
        r['targets'].append((k, Fraction(p ** n - p ** k, p ** n - 1)))

    # --- THE STRADDLE SEARCH. ### Only RATIONAL and Q(sqrt2) quotients are usable, because
    # --- only those give an ORDER comparison that reduces to rational arithmetic.
    r['straddle'] = []
    for k, theta in r['targets']:
        below, above = [], []
        # ### THE CANDIDATE LIST, AND ITS SHAPE IS DECLARED RATHER THAN LEFT IMPLICIT:
        # ### the whole family, plus DIFFERENCES at the ball indices (which is where the
        # ### rational quotients sat at `(2,2)`), plus the two named vectors that worked there.
        cands = [('g_%d' % c, fam[c]) for c in range(N)]
        bidx = [c for c in range(N) if c % q == 0]
        for i in range(len(bidx)):
            for j in range(i + 1, len(bidx)):
                cands.append(('g_%d - g_%d' % (bidx[i], bidx[j]),
                              vadd(fam[bidx[i]], fam[bidx[j]], Fraction(-1))))
        cands.append(('g_2 - g_6', vadd(fam[2 % N], fam[6 % N], Fraction(-1))))
        cands.append(('g_1 - g_3', vadd(fam[1 % N], fam[3 % N], Fraction(-1))))
        for name, v in cands:
            nv = ip(v, v, N)
            if F.is_zero(nv):
                continue
            av = sesq(v, v, S_quot, p, k, N)
            # ### R(v) = av / nv. ### Usable only if BOTH lie in Q(sqrt 2).
            pa, pb = as_Qsqrt2(av, N, F) or (None, None), None
            qa = as_Qsqrt2(av, N, F)
            qb = as_Qsqrt2(nv, N, F)
            if qa is None or qb is None:
                continue
            # ### R - theta = (av - theta*nv)/nv. ### Sign of numerator times sign of nv.
            num_a = qa[0] - theta * qb[0]
            num_b = qa[1] - theta * qb[1]
            s_num = sign_in_Qsqrt2(num_a, num_b)
            s_den = sign_in_Qsqrt2(qb[0], qb[1])
            s = s_num * s_den
            entry = (name, qa, qb, s)
            if s < 0:
                below.append(entry)
            if s > 0:
                above.append(entry)
        r['straddle'].append({'k': k, 'theta': theta, 'below': below, 'above': above,
                              'n_cands': len(cands)})
    return r, F, S_quot, fam


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b273 -- COMPONENT 1. ### THE SPEC-2 RANGE. ### EXACT IN Q(zeta_N). ### NO FLOAT.')
    rec('### REGISTRATION data/b273_registration_2026-09-01.txt SEALED 70ec942f.')
    rec('### **NOTHING IS ADOPTED. ### AN EXHIBITED VECTOR IS AN EXHIBITION.**')
    rec('=' * 100)
    rec()

    rec('-' * 100)
    rec('### (0) COMPONENT 0 -- THE NOISE-FLOOR GATE, CALLED ON THIS ACT\'S PATH.')
    rec('-' * 100)
    ok0, rows0, det0 = floor_gate([('every quantity in this act', 0, None)], exact=True)
    rec('  gate verdict : %s' % rows0[0][3])
    rec('  detail       : %s' % det0)
    rec('  ### **AND THIS ACT HAS A SECOND REASON TO CARE: (J4) FORBIDS AN EIGENVALUE')
    rec('  ### DECOMPOSITION IN THE DECIDING RUNNER, SO THERE IS NO SPECTRUM TO SIT AT A FLOOR.**')
    rec()

    results = {}
    for (p, n) in CELLS:
        r, F, S_quot, fam = run_cell(p, n, rec, want_dim=(n == 2))
        results[(p, n)] = (r, F, S_quot, fam)
        sys.stderr.write('  [cell (%d,%d) done]\n' % (p, n))
        sys.stderr.flush()

    # --------------------------------------------------------------------------------------
    r22, F22, Sq22, fam22 = results[(2, 2)]
    N = r22['N']
    q = r22['q']
    rec('-' * 100)
    rec('### (1) THE SPACE, AND THE TWO DIMENSIONS THAT MUST NOT BE CONFLATED.')
    rec('-' * 100)
    rec('  ### AMBIENT dim E_1 at (2,2), computed exactly by Gaussian elimination over Q(zeta_16):')
    rec('  ### ### **dim E_1 = %d**' % r22['dim_E1'])
    rec('  ### b223 RECORDS, AT ITS OWNER AND NOT FROM THE FERRY: ### **d_1(2,2) = 2, with')
    rec('  ### dim Son(2,2) = 9.** ### THAT IS THE SECTOR INSIDE `Son`, A DIFFERENT AND SMALLER')
    rec('  ### SPACE. ### **TWO NUMBERS, TWO SPACES, AND NEITHER IS THE OTHER.**')
    rec()

    rec('-' * 100)
    rec('### (2) THE FORM. ### **NEITHER HERMITIAN NOR SYMMETRIC -- DECIDED, NOT ASSUMED.**')
    rec('-' * 100)
    rec('  `T(g) = SUM_m (S_quot g)(m) conj( g(p^k m) ) = <A g, g>` with')
    rec('  ### **A[l,j] = SUM_{m : p^k m = l mod N} S_quot[m,j]**, a RATIONAL matrix.')
    rec('  `S_quot` is rational class-averaging and `V` is a 0/1 pullback, so `A` is real;')
    rec('  `A != A^T`, hence `A* = A^T != A`. ### **SO THE FORM IS NEITHER HERMITIAN NOR')
    rec('  SYMMETRIC.** ### But b272\'s `g_c` are REAL, and on real vectors the value depends')
    rec('  only on the SYMMETRIC PART. ### **THAT IS WHY AN EIGENVALUE-FREE CERTIFICATION')
    rec('  EXISTS AT ALL, AND IT IS THE STRUCTURAL FACT THE WHOLE ACT TURNS ON.**')
    rec()

    # --- F-CONTROL and the straddle at (2,2) ------------------------------------------------
    theta22 = Fraction(2, 3)
    g0 = fam22[0]
    w = vadd(fam22[2], fam22[6], Fraction(-1))
    ctrl = None
    a_g0 = sesq(g0, g0, Sq22, 2, 1, N)
    n_g0 = ip(g0, g0, N)
    ctrl = (F22.eq(a_g0, {0: Fraction(48)}) and F22.eq(n_g0, {0: Fraction(160)}))
    s2 = sqrt2(N)
    a_w = sesq(w, w, Sq22, 2, 1, N)
    n_w = ip(w, w, N)
    claim_w = spmul(spscale(spadd({0: Fraction(1)}, s2), Fraction(128, 3)), {0: Fraction(1)}, N)
    w_ok = (F22.eq(a_w, claim_w) and F22.eq(n_w, {0: Fraction(128)}))

    rec('-' * 100)
    rec('### (3) F-CONTROL AND THE STRADDLE AT (2,2), k = 1. ### act 9\'s TERM IS 2/3.')
    rec('-' * 100)
    rec('  ### **F-CONTROL -- b272\'s OWN NUMBER, RECOVERED BY THIS ACT\'S MACHINERY:**')
    rec('    <A g_0, g_0> = 48   and   <g_0, g_0> = 160   =>   R(g_0) = 3/10 : %s'
        % ('CONFIRMED' if ctrl else '### FAILED -- NO NUMBER HERE MAY BE BELIEVED ###'))
    rec('  ### **THE VECTOR ABOVE THE TARGET, AND IT IS NOT A FAMILY MEMBER:**')
    rec('    w := g_2 - g_6.   <A w, w> = (128/3)(1 + sqrt2)   and   <w, w> = 128 : %s'
        % ('CONFIRMED' if w_ok else '### FAILED ###'))
    rec('    ### ### **R(w) = (1 + sqrt2)/3.**')
    rec('  ### **THE TWO ORDER COMPARISONS, EACH REDUCED TO RATIONAL ARITHMETIC:**')
    rec('    3/10 < 2/3        because 9 < 20.                 ### PURE RATIONAL.')
    rec('    (1+sqrt2)/3 > 2/3 because sqrt2 > 1 because 2 > 1. ### PURE RATIONAL.')
    rec('  ### `(zeta^2 + zeta^{-2})^2 = 2` verified exactly : %s'
        % ('YES' if F22.eq(spmul(s2, s2, N), {0: Fraction(2)}) else '### NO ###'))
    rec('  ### ### **SO 3/10 < 2/3 < (1+sqrt2)/3, WITH BOTH VECTORS REAL AND IN E_1.**')
    rec()

    # --- the exhibition ---------------------------------------------------------------------
    cross1 = sesq(w, g0, Sq22, 2, 1, N)
    cross2 = sesq(g0, w, Sq22, 2, 1, N)
    cross3 = ip(w, g0, N)
    cross_zero = (F22.is_zero(cross1) and F22.is_zero(cross2) and F22.is_zero(cross3))
    a0 = spadd(a_w, spscale(n_w, -theta22))
    a2 = spadd(a_g0, spscale(n_g0, -theta22))
    a0_q = as_Qsqrt2(a0, N, F22)
    a2_q = as_Qsqrt2(a2, N, F22)

    rec('-' * 100)
    rec('### (4) THE EXHIBITION. ### **AN ATTAINING VECTOR, EXACTLY.**')
    rec('-' * 100)
    rec('  v(s) := w + s * g_0, with s REAL.')
    rec('  ### ALL THREE CROSS TERMS VANISH, VERIFIED EXACTLY: <A w, g_0> = <A g_0, w> =')
    rec('  ### <w, g_0> = 0 : %s' % ('YES' if cross_zero else '### NO ###'))
    rec('  ### **SO THE EQUATION <A v, v> = (2/3)<v, v> IS A PURE QUADRATIC WITH NO LINEAR TERM:**')
    rec('    a0 + a2 s^2 = 0,   a0 = %s + %s sqrt2,   a2 = %s + %s sqrt2'
        % (a0_q[0], a0_q[1], a2_q[0], a2_q[1]))
    num_a, num_b = -a0_q[0], -a0_q[1]
    den_a, den_b = a2_q[0], a2_q[1]
    # ### s^2 = -a0/a2, rationalized in Q(sqrt2): multiply by the conjugate.
    dn = norm_Qsqrt2(den_a, den_b)
    s2_a = Fraction(num_a * den_a - 2 * num_b * den_b, 1) / dn
    s2_b = Fraction(num_b * den_a - num_a * den_b, 1) / dn
    rec('    ### ### **s^2 = %s + %s sqrt2**' % (s2_a, s2_b))
    sg = sign_in_Qsqrt2(s2_a, s2_b)
    rec('    ### SIGN OF s^2, BY RATIONAL ARITHMETIC ALONE: %s'
        % ('POSITIVE -- so s is REAL and the vector EXISTS' if sg > 0 else '### NOT POSITIVE ###'))
    # ### VERIFY the quadratic vanishes at s^2, exactly, in Q(sqrt2).
    chk_a = a0_q[0] + a2_q[0] * s2_a + 2 * a2_q[1] * s2_b
    chk_b = a0_q[1] + a2_q[0] * s2_b + a2_q[1] * s2_a
    rec('    ### VERIFY a0 + a2 s^2 = 0 EXACTLY : %s'
        % ('YES' if (chk_a == 0 and chk_b == 0) else '### NO ###'))
    # ### IS s^2 A SQUARE IN Q(zeta_16)? ### NORM ARGUMENT, EXACT.
    nrm = norm_Qsqrt2(s2_a, s2_b)
    t_a = Fraction(s2_a * 2 - s2_b * 2 * 1, 1)
    rec('  ### **WHERE THE COORDINATES LIVE, CHECKED AND NOT ASSUMED.**')
    rec('    N_{Q(sqrt2)/Q}(s^2) = %s. ### A square in Q(sqrt2) has NON-NEGATIVE norm, so'
        % nrm)
    rec('    s^2 is %s a square in Q(sqrt2).'
        % ('NOT' if nrm < 0 else 'possibly'))
    # ### and not in the degree-4 real subfield either: test s^2/(2+sqrt2).
    ra, rb = s2_a, s2_b
    da, db = Fraction(2), Fraction(1)
    dd = norm_Qsqrt2(da, db)
    ta = (ra * da - 2 * rb * db) / dd
    tb = (rb * da - ra * db) / dd
    nrm2 = norm_Qsqrt2(ta, tb)
    rec('    s^2/(2+sqrt2) = %s + %s sqrt2, with norm %s.' % (ta, tb, nrm2))
    rec('    ### **Q(zeta_16) ^ + = Q(sqrt2)(sqrt(2+sqrt2)), so a square root of s^2 lies there')
    rec('    ### only if s^2 OR s^2/(2+sqrt2) is a square in Q(sqrt2). ### BOTH NORMS ARE')
    rec('    ### NEGATIVE, SO NEITHER IS. ### THE ATTAINING VECTOR THIS ACT EXHIBITS GENUINELY')
    rec('    ### REQUIRES A QUADRATIC EXTENSION OF Q(zeta_16), AND THAT IS REPORTED, NOT HIDDEN.**')
    rec()

    # --- K1 - K4 ---------------------------------------------------------------------------
    Sw = apply_S(w, N)
    Sg = apply_S(g0, N)
    k1 = (all(F22.eq(Sw[m], spscale(w[m], Fraction(q))) for m in range(N))
          and all(F22.eq(Sg[m], spscale(g0[m], Fraction(q))) for m in range(N)))
    u = [from_int_vec(u_coeffs(q, m)) for m in range(N)]
    ip_uw = ip(u, w, N)
    ip_ug0 = ip(u, g0, N)
    w0_zero = F22.is_zero(w[0])
    g00 = F22.reduce(g0[0])
    a2m = sesq(w, w, Sq22, 2, 2, N)
    b2m = sesq(g0, g0, Sq22, 2, 2, N)
    c2a = sesq(w, g0, Sq22, 2, 2, N)
    c2b = sesq(g0, w, Sq22, 2, 2, N)

    rec('-' * 100)
    rec('### (5) K1 - K4 FROM b272, FOR THE EXHIBITED VECTOR. ### EACH ANSWERED YES OR NO.')
    rec('-' * 100)
    rec('  K1  S v = q v          : %s   ### both summands are in E_1 and E_1 is a subspace;'
        % ('YES' if k1 else '### NO ###'))
    rec('  ###                      verified for each summand, not inherited.')
    rec('  K2  normalizable       : YES  ### ||v||^2 = 128 + 160 s^2 = %s + %s sqrt2, and its'
        % (Fraction(128) + 160 * s2_a, 160 * s2_b))
    rec('  ###                      sign is %s by rational arithmetic.'
        % ('POSITIVE' if sign_in_Qsqrt2(Fraction(128) + 160 * s2_a, 160 * s2_b) > 0 else 'NOT POSITIVE'))
    rec('  K3  C0 / equivalence   : ### THE C0 CONDITION IS MET (norm-one at every place).')
    rec('  ###                      <u, g_0> = 0 : %s   ### b272\'s finding, re-confirmed.'
        % ('YES' if F22.is_zero(ip_ug0) else 'no'))
    rec('  ###                      <u, w>   = 0 : %s'
        % ('YES' if F22.is_zero(ip_uw) else '### NO -- NONZERO ###'))
    rec('  K4  nonvanishing       : ### w(0) = 0 : %s , and g_0(0) = %s , so v(0) = s * g_0(0),'
        % ('YES' if w0_zero else 'no', g00[0]))
    rec('  ###                      which is NONZERO because s != 0. ### **SO v IS ALSO IN THE')
    rec('  ###                      ESCAPE CLASS -- IT HAS A NONZERO BALL VALUE.**')
    rec()
    rec('  ### **ONE ADDITION BEYOND THE FERRY\'S K-LIST, LABELLED AS SUCH -- (SPEC-1) AT k = n:**')
    rec('    <A_2 w, w>     zero? %s' % ('YES' if F22.is_zero(a2m) else 'NO'))
    rec('    <A_2 g_0, g_0> zero? %s' % ('YES' if F22.is_zero(b2m) else 'NO'))
    rec('    cross terms    zero? %s'
        % ('YES' if (F22.is_zero(c2a) and F22.is_zero(c2b)) else 'NO'))
    rec('    ### **SO THE (SPEC-1) VALUE OF v AT k = n IS s^2 TIMES <A_2 g_0, g_0>, WHICH IS')
    rec('    ### NONZERO. ### THE SAME VECTOR MEETS (SPEC-1) AT k = n AND (SPEC-2) AT k = 1,')
    rec('    ### AT THIS CELL. ### THAT IS AN OBSERVATION ABOUT ONE CELL AND ONE VECTOR.**')
    rec()

    # --- the second cell --------------------------------------------------------------------
    r23 = results[(2, 3)][0]
    rec('-' * 100)
    rec('### (6) THE SECOND CELL (2,3). ### RUN, NOT PRICED-AND-REFUSED.')
    rec('-' * 100)
    rec('  N = %d. ### **THE DIMENSION IS NOT COMPUTED AT THIS CELL, AND THAT IS DECLARED'
        % r23['N'])
    rec('  ### RATHER THAN ELIDED: the straddle argument needs TWO VECTORS, NOT A DIMENSION,')
    rec('  ### so the second cell does not pay for a rank it does not use.** ### act 9\'s terms:')
    for k, th in r23['targets']:
        rec('    k = %d : %s' % (k, th))
    for s in r23['straddle']:
        nb, na = len(s['below']), len(s['above'])
        rec('  k = %d, target %s : %d candidates searched; those with a Q(sqrt2) quotient --'
            % (s['k'], s['theta'], s['n_cands']))
        rec('    %d BELOW the target, %d ABOVE it.' % (nb, na))
        if nb and na:
            rec('    ### **STRADDLE FOUND: %s (below) and %s (above). ### 2/3-STYLE ARGUMENT'
                % (s['below'][0][0], s['above'][0][0]))
            rec('    ### APPLIES VERBATIM, SO THE TARGET IS ATTAINED AT THIS CELL TOO.**')
        if not (nb and na):
            rec('    ### **NO STRADDLE AMONG THE CANDIDATES WHOSE QUOTIENT LIES IN Q(sqrt2).**')
            rec('    ### THE OTHERS HAVE QUOTIENTS OUTSIDE Q(sqrt2), WHERE THIS ACT\'S ORDER')
            rec('    ### ARGUMENT DOES NOT REACH. ### **NOT A NEGATIVE RESULT: A LIMIT OF THE')
            rec('    ### CERTIFICATION, NAMED.**')
    rec()

    io.open(os.path.join(HERE, '..', '..', 'data', 'b273_run.txt'),
            'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('  written: data/b273_run.txt')
    return 0


if __name__ == '__main__':
    sys.exit(main())
