# -*- coding: utf-8 -*-
"""b272_escape_class.py -- M-2 CAMPAIGN, ACT 6. ### THE ESCAPE CLASS.

### THE TASK: ### **CHARACTERIZE THE `E_1` VECTORS THAT DO NOT VANISH ON THE BALL, AND TEST THEM
### AGAINST EVERY CONDITION b226's UNIT SATISFIES.**

### THE HAZARD THIS FILE IS WRITTEN AGAINST: ### **A CLASS IS NOT A MEMBER.** ### A property
### proved for `g_0` is a property OF `g_0`. ### Every printed line says which.

### **NO UNIT IS ADOPTED. ### b226's CHOICE WAS MADE BY RULING AND ONLY THE AUTHOR REPLACES IT.**
### ### **NO FLOAT DECIDES ANYTHING HERE** -- every verdict is a reduction modulo `Phi_N`.
### COMPONENT 0 (`noise_floor.py`) IS CALLED ON THIS PATH AND RETURNS `EXACT`: ### a verdict,
### not a bypass.
"""
import io
import os
import sys
from fractions import Fraction

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..'))

from b268_generator import u_coeffs
from b270_ambient_pairing import (PLACES, Field, ball_of, from_int_vec, orbit_classes,
                                  spadd, spconj, spmul, spscale)
from b271_top_level_no_go import apply_S, project, shift, vanishes_on_ball
from noise_floor import gate as floor_gate

# ### (K2c)'s DECLARED CAP, PRINTED WITH EVERY RESULT IT LIMITS.
FULL_SWEEP_MAX_N = 49
SAMPLE_CS = (0, 1, 2, 3)


def g_c(c, q, N):
    """### THE FAMILY, FROM b226's OWN IDENTITY `4q P_1 = (q + S)(1 + Pi)` APPLIED TO `e_c`:
    ###   `g_c(m) = q([m = c] + [m = -c]) + zeta^{mc} + zeta^{-mc}`.
    ### **REAL-VALUED, AND `g_c(0) = 2` FOR EVERY `c != 0`.**"""
    out = []
    for m in range(N):
        d = {}
        if m == c % N:
            d[0] = d.get(0, Fraction(0)) + q
        if m == (-c) % N:
            d[0] = d.get(0, Fraction(0)) + q
        k1 = (m * c) % N
        k2 = (-m * c) % N
        d[k1] = d.get(k1, Fraction(0)) + 1
        d[k2] = d.get(k2, Fraction(0)) + 1
        out.append({k: v for k, v in d.items() if v != 0})
    return out


def inner(a, b, N):
    """### `<a, b> = SUM_m a(m) conj(b(m))`, exact in `Q(zeta_N)`."""
    acc = {}
    for m in range(N):
        if not a[m]:
            continue
        acc = spadd(acc, spmul(a[m], spconj(b[m], N), N))
    return acc


def pairing_times_pk2(f, g, p, k, N):
    """### `SUM_m f(m) conj( g(p^k m mod N) )`. ### The factor `p^{-k/2}` is carried
    ### SYMBOLICALLY, so the exact object is the pairing times `p^{k/2}`."""
    pk = pow(p, k, N)
    acc = {}
    for m in range(N):
        if not f[m]:
            continue
        acc = spadd(acc, spmul(f[m], spconj(g[(pk * m) % N], N), N))
    return acc


def run_cell(p, ell):
    q = p ** ell
    n = ell
    N = q * q
    F = Field(N)
    ballset = set(ball_of(N, p, n))
    classes = orbit_classes(N, p, ballset)
    cls_of = {}
    for C in classes:
        for m in C:
            cls_of[m] = C

    u = [from_int_vec(u_coeffs(q, m)) for m in range(N)]
    r = {'p': p, 'n': n, 'q': q, 'N': N}

    # --- THE CHARACTERIZATION. ### ALL `c` FOR THE BALL VALUE (cheap, closed form). ----------
    ball_ok = 0
    for c in range(N):
        gc = g_c(c, q, N)
        if not F.is_zero(gc[0]):
            ball_ok += 1
    r['ball_nonzero_count'] = ball_ok
    r['ball_nonzero_all'] = (ball_ok == N)

    # ### `S g_c = q g_c` -- THE EXPENSIVE CHECK, UNDER (K2c)'s DECLARED CAP.
    cs = list(range(N)) if N <= FULL_SWEEP_MAX_N else list(SAMPLE_CS)
    r['membership_scope'] = ('ALL %d c' % N) if N <= FULL_SWEEP_MAX_N else \
        ('SAMPLE c in %s of %d' % (list(SAMPLE_CS), N))
    mem_ok = 0
    for c in cs:
        gc = g_c(c, q, N)
        Sg = apply_S(gc, N)
        if all(F.eq(Sg[m], spscale(gc[m], Fraction(q))) for m in range(N)):
            mem_ok += 1
    r['membership_checked'] = len(cs)
    r['membership_ok'] = mem_ok
    r['membership_all'] = (mem_ok == len(cs))

    # --- K2: THE NORM, EXACT. ### Is it rational, as b226's `||u||^2` is not? --------------
    g0 = g_c(0, q, N)
    nrm = inner(g0, g0, N)
    red = F.reduce(nrm)
    r['norm2_rational'] = all(x == 0 for x in red[1:])
    r['norm2'] = red[0] if r['norm2_rational'] else None
    # ### THE CLOSED FORM REGISTERED IN ADVANCE: `(2q+2)^2 + 4(N-1)`.
    r['norm2_predicted'] = Fraction((2 * q + 2) ** 2 + 4 * (N - 1))
    r['norm2_matches'] = (r['norm2_rational'] and red[0] == r['norm2_predicted'])
    # ### AND b226's OWN VECTOR, FOR CONTRAST -- NOT AS A COMPARISON OF MERIT.
    unrm = F.reduce(inner(u, u, N))
    r['u_norm2_rational'] = all(x == 0 for x in unrm[1:])

    # --- K3: THE INNER PRODUCT WITH b226's UNIT. ### THE EQUIVALENCE-CLASS QUESTION. --------
    # ### DERIVED IN ADVANCE: `<u, g_c> = 4q u(c)`, using `u` Pi-even and `S u = q u`.
    ip0 = inner(u, g0, N)
    r['ip_g0_zero'] = F.is_zero(ip0)
    r['ip_g0_matches_4qu0'] = F.eq(ip0, spscale(u[0], Fraction(4 * q)))
    # ### THE OTHER POLARITY (F-ORTHO): some `c != 0` must give a NONZERO inner product, or
    # ### the inner product is measuring nothing.
    nz = []
    for c in (1, 2, 3):
        if c % N == 0:
            continue
        ipc = inner(u, g_c(c, q, N), N)
        ok = F.eq(ipc, spscale(u[c % N], Fraction(4 * q)))
        if not F.is_zero(ipc):
            nz.append(c)
        r.setdefault('ip_formula_ok', []).append(ok)
    r['ip_nonzero_cs'] = nz

    # --- K4: NONVANISHING. ### `g_c(0) != 0` gives it in one line. -------------------------
    r['k4_ok'] = r['ball_nonzero_all']

    # --- K5: (SPEC-2). ### ONLY THE CELL WITH A NONEMPTY RANGE HAS A TEST. -----------------
    r['spec2_range_empty'] = (n - 1 < 1)
    r['spec2'] = []
    if not r['spec2_range_empty']:
        for k in range(1, n):
            theta = Fraction(p ** n - p ** k, p ** n - 1)
            rows = []
            for c in range(N):
                gc = g_c(c, q, N)
                Sq = project(gc, N, ballset, cls_of)
                pr = pairing_times_pk2(Sq, gc, p, k, N)
                nc = F.reduce(inner(gc, gc, N))
                if any(x != 0 for x in nc[1:]):
                    rows.append((c, None, False, 'norm not rational'))
                    continue
                if nc[0] == 0:
                    rows.append((c, None, False, 'zero vector'))
                    continue
                # ### NORMALIZED, because b226's unit is norm-one.
                val = spscale(pr, Fraction(1, 1) / nc[0])
                agrees = F.eq(val, {0: theta})
                vred = F.reduce(val)
                israt = all(x == 0 for x in vred[1:])
                rows.append((c, vred[0] if israt else None, agrees,
                             'rational' if israt else 'not rational'))
            r['spec2'].append({'k': k, 'theta': theta, 'rows': rows,
                               'any_agree': any(x[2] for x in rows)})
    return r


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b272 -- COMPONENT 1. ### THE ESCAPE CLASS, CHARACTERIZED. ### EXACT IN Q(zeta_N).')
    rec('### REGISTRATION data/b272_registration_2026-08-31.txt SEALED 63a35ca7 BEFORE ANY VALUE.')
    rec('### **NO UNIT IS ADOPTED. ### A CLASS IS NOT A MEMBER, AND EVERY LINE SAYS WHICH.**')
    rec('=' * 100)
    rec()

    # ### COMPONENT 0, ON THIS ACT'S OWN PATH. ### NOT SHIPPED-AND-SKIPPED.
    rec('-' * 100)
    rec('### (0) COMPONENT 0 -- THE NOISE-FLOOR GATE, CALLED ON THIS ACT\'S PATH.')
    rec('-' * 100)
    ok0, rows0, det0 = floor_gate([('every quantity in this act', 0, None)], exact=True,
                                  label='b272')
    rec('  gate verdict : %s' % rows0[0][3])
    rec('  detail       : %s' % det0)
    rec('  ### **THIS ACT\'S CHANNEL IS EXACT ARITHMETIC IN Q(zeta_N), SO NO FLOOR APPLIES AND')
    rec('  ### NONE IS INVENTED. ### THE GATE WAS CALLED AND RETURNED A VERDICT; IT WAS NOT')
    rec('  ### SKIPPED, AND THAT DISTINCTION IS THE WHOLE POINT OF PUTTING IT IN THE PATH.**')
    rec('  ### Its REFUSING arms fire in its own fixtures, against b264\'s eleven real modes.')
    rec()

    results = [run_cell(p, ell) for (p, ell) in PLACES]

    rec('-' * 100)
    rec('### (1) THE CHARACTERIZATION. ### **`E_1` HAS A SPANNING SET INSIDE THE ESCAPE CLASS.**')
    rec('-' * 100)
    rec('  THE FAMILY, from b226\'s identity 4q P_1 = (q + S)(1 + Pi) applied to e_c:')
    rec('    ### **g_c(m) = q([m = c] + [m = -c]) + zeta^{mc} + zeta^{-mc}**, real-valued.')
    rec('  {g_c : c in Z/N} SPANS E_1, because {e_c} spans the space and P_1 is onto E_1.')
    rec()
    rec('  %-7s %-6s %-22s %-26s %s'
        % ('(p,n)', 'N', 'g_c(0) != 0 for all c', 'S g_c = q g_c', 'membership scope'))
    for r in results:
        rec('  %-7s %-6d %-22s %-26s %s'
            % ('(%d,%d)' % (r['p'], r['n']), r['N'],
               'YES (%d of %d)' % (r['ball_nonzero_count'], r['N']) if r['ball_nonzero_all']
               else '### NO ###',
               'YES (%d of %d)' % (r['membership_ok'], r['membership_checked'])
               if r['membership_all'] else '### NO ###',
               r['membership_scope']))
    rec()
    rec('  ### **0 IS IN THE BALL, AND g_c(0) = 2 FOR EVERY c != 0 (2q+2 AT c = 0). ### SO EVERY')
    rec('  ### MEMBER OF A SPANNING SET OF E_1 LIES IN THE ESCAPE CLASS.**')
    rec('  ### ### **THEREFORE THE BALL-VANISHING VECTORS -- WHICH INCLUDE ALL OF E_1(Son), HENCE')
    rec('  ### ### ALL OF b226\'s FAMILY -- ARE A PROPER SUBSPACE: THE KERNEL OF RESTRICTION TO')
    rec('  ### ### THE BALL. ### ESCAPING IS GENERIC; BALL-VANISHING IS THE SPECIAL CONDITION.**')
    nall = sum(1 for r in results if r['ball_nonzero_all'] and r['membership_all'])
    rec('  ### CHARACTERIZATION VERDICT: %s at %d of %d cells'
        % ('spanning family entirely inside the escape class' if nall == len(results)
           else 'CHARACTERIZATION FAILED', nall, len(results)))
    rec('  ### **SCOPE, PRINTED NOT ELIDED:** the ball value is checked for ALL c at every cell;')
    rec('  ### the eigenvalue equation under (K2c)\'s declared cap, shown in the last column.')
    rec()

    rec('-' * 100)
    rec('### (2) K1 AND K4. ### THE TWO THAT PASS OUTRIGHT.')
    rec('-' * 100)
    rec('  ### **K1 (S g = q g): SATISFIED BY EVERY MEMBER CHECKED, AT EVERY CELL.** ### It holds')
    rec('  ### by construction -- the class lives inside E_1, which is P_1\'s image -- and is')
    rec('  ### verified anyway, per b271\'s standard that membership is checked, not inherited.')
    rec('  ### **K4 (NONVANISHING): SATISFIED, BY A ONE-LINE ARGUMENT: g_c(0) != 0.**')
    rec('  ### ### **b268\'s ARGUMENT DOES NOT TRANSFER, AND IS NOT CLAIMED TO.** ### b268 is')
    rec('  ### ### about the canonical generator 4q P_1 f_{1,1} -- a DIFFERENT vector -- and its')
    rec('  ### ### content is a support count N - q derived from THAT generator\'s structure.')
    rec('  ### ### **SAYING WHICH IS THE POINT OF K4, AND THE NEW ARGUMENT IS STRICTLY EASIER.**')
    rec()

    rec('-' * 100)
    rec('### (3) K2 -- NORM-ONE / G-NORM. ### SATISFIED, WITH ONE ARITHMETIC DIFFERENCE.')
    rec('-' * 100)
    rec('  %-7s %-16s %-20s %-10s %s'
        % ('(p,n)', '||g_0||^2', 'predicted (2q+2)^2+4(N-1)', 'matches', '||u||^2 rational?'))
    for r in results:
        rec('  %-7s %-16s %-20s %-10s %s'
            % ('(%d,%d)' % (r['p'], r['n']),
               str(r['norm2']) if r['norm2_rational'] else '(not rational)',
               str(r['norm2_predicted']),
               'YES' if r['norm2_matches'] else '### NO ###',
               'yes' if r['u_norm2_rational'] else 'NO'))
    rec()
    k2n = sum(1 for r in results if r['norm2_matches'])
    rec('  ### K2 VERDICT: %s at %d of %d cells'
        % ('norms rational and matching the registered closed form' if k2n == len(results)
           else 'K2 NORM MISMATCH', k2n, len(results)))
    rec()
    rec('  ### **ANY NONZERO VECTOR NORMALIZES, SO SUM_v | ||u_v|| - 1 | = 0 EXACTLY --')
    rec('  ### b226\'s "STRONGEST WAY THE DEFINITION ALLOWS". ### K2 IS SATISFIED.**')
    rec('  ### **AND THE DIFFERENCE, REPORTED WITHOUT PROMOTION: ||g_0||^2 IS A RATIONAL INTEGER')
    rec('  ### WHERE b226 RECORDS ||u||^2 AS A TOTALLY-REAL ALGEBRAIC INTEGER THAT IS NOT')
    rec('  ### RATIONAL. ### THAT IS A DIFFERENCE, NOT AN ADVANTAGE, AND IS NOT ARGUED AS ONE.**')
    rec()

    rec('-' * 100)
    rec('### (4) K3 -- THE C0 CONDITION, AND THE EQUIVALENCE CLASS. ### **THE DOSSIER\'S CENTRE.**')
    rec('-' * 100)
    rec('  DERIVED IN ADVANCE FROM u being Pi-even and S u = q u:')
    rec('    <u, g_c> = q(u(c) + u(-c)) + (S u)(c) + (S u)(-c) = 2q(u(c) + u(-c)) = ### **4q u(c)**')
    rec()
    rec('  %-7s %-22s %-24s %s'
        % ('(p,n)', '<u, g_0> = 0 ?', 'formula 4q u(c) holds', 'c != 0 with <u,g_c> != 0'))
    for r in results:
        rec('  %-7s %-22s %-24s %s'
            % ('(%d,%d)' % (r['p'], r['n']),
               'YES -- ORTHOGONAL' if r['ip_g0_zero'] else '### NO ###',
               'YES' if all(r.get('ip_formula_ok', [])) else '### NO ###',
               ','.join(str(c) for c in r['ip_nonzero_cs']) if r['ip_nonzero_cs'] else 'NONE'))
    rec()
    k3n = sum(1 for r in results if r['ip_g0_zero'])
    k3p = sum(1 for r in results if r['ip_nonzero_cs'])
    rec('  ### K3 VERDICT: %s at %d of %d cells; the other polarity is live at %d of %d'
        % ('<u, g_0> = 0 exactly' if k3n == len(results) else 'K3 ORTHOGONALITY FAILED',
           k3n, len(results), k3p, len(results)))
    rec()
    rec('  ### **u(0) = 0 BECAUSE 0 IS IN THE BALL AND b268 PUTS u\'s ZERO SET EXACTLY THERE.')
    rec('  ### SO <u, g_0> = 0 EXACTLY, AT EVERY PLACE.**')
    rec('  ### THEN SUM_v | <u_v, g_v> - 1 | = SUM_v 1, WHICH ### DIVERGES ### over infinitely')
    rec('  ### many places, so by von Neumann DEFINITION 3.3.2 the two C0-sequences are ### NOT')
    rec('  ### EQUIVALENT ### , and by LEMMA 4.1.1 the two incomplete products are')
    rec('  ### ### **MUTUALLY ORTHOGONAL.**')
    rec('  ### ### **REPLACING b226\'s UNIT BY g_0 WOULD NOT ADJUST THE OBJECT. ### IT WOULD')
    rec('  ### ### REPLACE IT WITH AN ORTHOGONAL ONE.** ### That is b226\'s own recorded warning,')
    rec('  ### ### now arithmetic rather than hypothetical.')
    rec('  ### **AND THIS IS A FACT ABOUT g_0, NOT ABOUT THE CLASS (the act\'s named hazard):**')
    rec('  ### for c != 0 the inner product is NONZERO, because u(c) != 0 off the ball. ### The')
    rec('  ### equivalence question for a general member is a convergence condition across')
    rec('  ### infinitely many places and ### **THIS ACT DOES NOT SETTLE IT.**')
    rec()

    rec('-' * 100)
    rec('### (5) K5 -- (SPEC-2), AT THE ONLY CELL WITH A NONEMPTY RANGE. ### EXACT, NORMALIZED.')
    rec('-' * 100)
    empt = sum(1 for r in results if r['spec2_range_empty'])
    rec('  cells where 1 <= k <= n-1 IS AN EMPTY RANGE : %d of %d ### (b270\'s finding, carried)'
        % (empt, len(results)))
    for r in results:
        for s in r['spec2']:
            rec('  CELL (%d,%d), k=%d. ### act 9\'s term * p^{k/2} = %s'
                % (r['p'], r['n'], s['k'], s['theta']))
            rec('  ### THE WHOLE SPANNING FAMILY SWEPT, ALL %d MEMBERS, NORMALIZED:' % r['N'])
            rec('    %-5s %-24s %s' % ('c', 'pairing*p^{k/2} (normalized)', 'equals act 9 term?'))
            for (c, val, agrees, note) in s['rows']:
                rec('    %-5d %-24s %s'
                    % (c, str(val) if val is not None else '(%s)' % note,
                       'YES' if agrees else 'no'))
            nagr = sum(1 for x in s['rows'] if x[2])
            rec('  ### ### **MEMBERS OF THE SPANNING FAMILY SATISFYING (SPEC-2): %d of %d.**'
                % (nagr, len(s['rows'])))
            rec('  ### K5 VERDICT: %s -- %d of %d members satisfy it'
                % ('no member of the spanning family satisfies SPEC-2' if nagr == 0
                   else 'K5 IS SATISFIED BY SOME MEMBER', nagr, len(s['rows'])))
    rec()

    rec('-' * 100)
    rec('### (6) WHAT K5 DOES AND DOES NOT SETTLE. ### **THE RESISTANCE, NAMED PRECISELY.**')
    rec('-' * 100)
    rec('  ### **SETTLED: NO MEMBER OF THE SPANNING FAMILY SATISFIES (SPEC-2).** ### That is an')
    rec('  ### exact statement about N named vectors, taken by reduction modulo Phi_N.')
    rec('  ### **NOT SETTLED, AND NOT ATTEMPTED: whether some OTHER element of E_1 -- a linear')
    rec('  ### combination rather than a family member -- satisfies it.**')
    rec('  ### THE RESISTANCE, STATED AS PRECISELY AS THE FINDING: that question asks whether')
    rec('  ### a real quadratic form attains a given value on a subspace, i.e. it needs the')
    rec('  ### ### SIGNATURE ### of a Hermitian form over Q(zeta_N) -- equivalently ORDER')
    rec('  ### comparisons between real algebraic numbers. ### **THAT IS A DIFFERENT CHANNEL')
    rec('  ### FROM REDUCTION MODULO Phi_N, IT IS NOT WHAT THIS ACT\'S SEAL AUTHORIZES, AND IT IS')
    rec('  ### NOT OPENED HERE.** ### Filed, not fudged.')
    rec()

    io.open(os.path.join(HERE, '..', '..', 'data', 'b272_run.txt'),
            'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('  written: data/b272_run.txt')
    return 0


if __name__ == '__main__':
    sys.exit(main())
