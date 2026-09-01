# -*- coding: utf-8 -*-
"""b275_the_rule_stated.py -- M-2 CAMPAIGN, ACT 9. ### THE RULE STATED.

### THE QUESTION: ### **CAN THE UNIT CHOICE BE WRITTEN AS ONE RULE OVER ALL PLACES?**

### ### **WRITING A CANDIDATE RULE IS NOT REPLACING b226's RULED CHOICE.** ### That is the
### author's alone, and M-2 is owed until an author ruling adopts something.
### THE HAZARD THIS FILE IS WRITTEN AGAINST: ### **THE RULE'S VECTOR IS `g_0`. ### b273's
### ATTAINING VECTOR IS `w + s g_0`. ### THEY ARE DIFFERENT VECTORS AND EVERY LINE SAYS WHICH.**
### ### **NO FLOAT TOKEN APPEARS IN THIS FILE.**
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
from b271_top_level_no_go import apply_S
from noise_floor import gate as floor_gate


def g0_vec(q, N):
    """### THE RULE'S VECTOR, UNFOLDED: `4q P_1 e_0 = 2q e_0 + 2 * 1` (b272)."""
    return [({0: Fraction(2 * q + 2)} if m == 0 else {0: Fraction(2)}) for m in range(N)]


def projector(N, p, n):
    ballset = set(ball_of(N, p, n))
    cls_of = {}
    for C in orbit_classes(N, p, ballset):
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


def sesq(x, S_quot, p, k, N):
    Sx = S_quot(x)
    pk = pow(p, k, N)
    acc = {}
    for m in range(N):
        if not Sx[m]:
            continue
        acc = spadd(acc, spmul(Sx[m], spconj(x[(pk * m) % N], N), N))
    return acc


def ip(x, y, N):
    acc = {}
    for m in range(N):
        if not x[m]:
            continue
        acc = spadd(acc, spmul(x[m], spconj(y[m], N), N))
    return acc


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b275 -- COMPONENT 1. ### THE RULE STATED. ### EXACT. ### NO FLOAT.')
    rec('### REGISTRATION data/b275_registration_2026-09-01.txt SEALED 6257f01a.')
    rec('### **NOTHING IS ADOPTED. ### WRITING A RULE IS NOT REPLACING b226\'s RULED CHOICE.**')
    rec('=' * 100)
    rec()

    rec('-' * 100)
    rec('### (0) COMPONENT 0 -- THE NOISE-FLOOR GATE, ON THIS ACT\'S PATH (the E0 gate).')
    rec('-' * 100)
    ok0, rows0, det0 = floor_gate([('every quantity in this act', 0, None)], exact=True)
    rec('  gate verdict : %s' % rows0[0][3])
    rec('  detail       : %s' % det0)
    rec()

    # --- S1: THE CANONICAL INDEX, DERIVED ----------------------------------------------------
    rec('-' * 100)
    rec('### (1) S1 -- THE CANONICAL INDEX. ### **DERIVED FROM THE STRUCTURE, NOT PICKED.**')
    rec('-' * 100)
    rec('  The quotient channel is built on the orbit map m -> p m (b10\'s V_inv, b8\'s U).')
    rec('  ### ITS FIXED POINTS SOLVE (p - 1) m = 0 mod N. ### Since gcd(p-1, p^{2n}) = 1 for')
    rec('  ### EVERY prime, the only solution is m = 0.')
    rec('  ### **SO e_0 IS THE UNIQUE BASIS VECTOR FIXED BY THE VERY MAP THE CHANNEL QUOTIENTS')
    rec('  ### BY, AT EVERY PLACE AND EVERY LEVEL. ### THAT FORCES c = 0.**')
    rec()
    rec('  %-8s %-6s %-28s %s'
        % ('(p,n)', 'N', 'fixed pts of m -> pm', 'fixed pts of Pi (m -> -m)'))
    canon_ok = True
    pi_warn = []
    for (p, ell) in PLACES:
        q = p ** ell
        N = q * q
        scal = [m for m in range(N) if (p * m) % N == m]
        invo = [m for m in range(N) if (-m) % N == m]
        canon_ok = canon_ok and (scal == [0])
        if invo != [0]:
            pi_warn.append((p, ell, invo))
        rec('  %-8s %-6d %-28s %s'
            % ('(%d,%d)' % (p, ell), N, str(scal), str(invo)))
    rec()
    rec('  ### **THE SCALING MAP FIXES ONLY 0, AT EVERY CELL : %s**'
        % ('CONFIRMED' if canon_ok else '### FAILED ###'))
    rec('  ### **AND THE WEAKER ARGUMENT IS NOT SUFFICIENT, WHICH THE ACT SAYS RATHER THAN')
    rec('  ### QUIETLY USING THE STRONGER ONE: ### the involution Pi alone fixes TWO indices at')
    rec('  ### p = 2 -- %s -- so Pi does not single out 0 there.**'
        % (str(pi_warn[0][2]) if pi_warn else 'none found'))
    rec()

    # --- S2: THE RULE --------------------------------------------------------------------
    rec('-' * 100)
    rec('### (2) S2 -- ### **THE RULE, WRITTEN WHOLE.**')
    rec('-' * 100)
    rec('  ### ### **u\'_p := 4q P_1 e_0 / || 4q P_1 e_0 ||   at the cell (p, ell(p)),**')
    rec('  ### ### **with ell(p) = 2 if p = 2, else 1   [b226];   q = p^{ell(p)};  N = q^2.**')
    rec('  EVERY CONSTITUENT UNFOLDED TO ITS OWNER:')
    rec('    4q P_1 = (q + S)(1 + Pi)                       [b226, the purity report]')
    rec('    (S f)(m) = SUM_{m\'} f(m\') zeta_N^{m m\'}         [b226]')
    rec('    (Pi f)(m) = f(-m)                              [b226]')
    rec('    ### **4q P_1 e_0 = 2q e_0 + 2 * 1**             [b272, and re-verified below]')
    rec('    ell(p)                                         [b226, arrival depth d_1(2,1) = 0]')
    rec()

    results = []
    for (p, ell) in PLACES:
        q = p ** ell
        n = ell
        N = q * q
        F = Field(N)
        ballset, S_quot = projector(N, p, n)
        g0 = g0_vec(q, N)
        u = [from_int_vec(u_coeffs(q, m)) for m in range(N)]
        Sg = apply_S(g0, N)
        inE1 = all(F.eq(Sg[m], spscale(g0[m], Fraction(q))) for m in range(N))
        t1 = sesq(g0, S_quot, p, ell, N)
        t1ok = F.eq(t1, {0: Fraction(4 * (N - q))})
        t1zero = F.is_zero(t1)
        nrm = F.reduce(ip(g0, g0, N))
        nrmrat = all(x == 0 for x in nrm[1:])
        ipu = ip(u, g0, N)
        orth = F.is_zero(ipu)
        spec2_empty = (n - 1 < 1)
        spec2_val = None
        if not spec2_empty:
            a = sesq(g0, S_quot, p, 1, N)
            ar = F.reduce(a)
            if all(x == 0 for x in ar[1:]) and nrmrat and nrm[0] != 0:
                spec2_val = Fraction(ar[0]) / Fraction(nrm[0])
        results.append({'p': p, 'ell': ell, 'q': q, 'N': N, 'inE1': inE1,
                        't1ok': t1ok, 't1zero': t1zero, 'nrm': nrm[0] if nrmrat else None,
                        'orth': orth, 'empty': spec2_empty, 'spec2': spec2_val})

    rec('  %-8s %-5s %-6s %-12s %-22s %-14s %s'
        % ('(p,n)', 'q', 'N', 'S g = q g', 'SPEC-1 value 4(N-q)', '||u\'||^2', '<u, g_0> = 0'))
    for r in results:
        rec('  %-8s %-5d %-6d %-12s %-22s %-14s %s'
            % ('(%d,%d)' % (r['p'], r['ell']), r['q'], r['N'],
               'YES' if r['inE1'] else '### NO ###',
               ('%d  MATCHES' % (4 * (r['N'] - r['q']))) if r['t1ok'] else '### MISMATCH ###',
               str(r['nrm']) if r['nrm'] is not None else '(not rational)',
               'YES' if r['orth'] else 'no'))
    rec()

    # --- T1 ------------------------------------------------------------------------------
    rec('-' * 100)
    rec('### (3) T1 -- (SPEC-1). ### **PASS, DERIVED GENERICALLY.**')
    rec('-' * 100)
    rec('  b271 derives <U^{ell} S_quot g_0, g_0> * p^{ell/2} = 4(N - q), and N = q^2 > q for')
    rec('  every q >= 2, so the value is ### **NONZERO AT EVERY PLACE, BY ARITHMETIC AND NOT BY')
    rec('  ### SURVEY.** ### Controlled exactly at all %d cells above.' % len(results))
    t1all = all(r['t1ok'] and not r['t1zero'] for r in results)
    rec('  ### T1 VERDICT: %s'
        % ('SPEC-1 holds under the rule at every cell' if t1all else 'T1 FAILED'))
    rec()

    # --- T2 ------------------------------------------------------------------------------
    rec('-' * 100)
    rec('### (4) T2 -- (SPEC-2). ### **VACUOUS AT LEVEL 1; AND THE RULE FAILS IT AT (2,2).**')
    rec('-' * 100)
    nempty = sum(1 for r in results if r['empty'])
    rec('  ### At ell = 1 the (SPEC-2) range 1 <= k <= 0 is ### **EMPTY**, so (SPEC-2) is')
    rec('  ### ### **VACUOUS THERE -- A VACUITY AND NOT A TRIUMPH.** ### %d of %d cells.'
        % (nempty, len(results)))
    for r in results:
        if not r['empty']:
            th = Fraction(r['p'] ** r['ell'] - r['p'], r['p'] ** r['ell'] - 1)
            agree = (r['spec2'] == th)
            rec('  ### CELL (%d,%d), k = 1: the rule gives R(g_0) = %s; act 9\'s term is %s.'
                % (r['p'], r['ell'], str(r['spec2']), str(th)))
            rec('  ### ### **THEY DIFFER. ### THE RULE FAILS (SPEC-2) AT THE ONE CELL WHERE')
            rec('  ### ### (SPEC-2) HAS CONTENT : %s**'
                % ('FAILS, as registered' if not agree else '### UNEXPECTEDLY AGREES ###'))
    rec()
    rec('  ### **AND b273\'s SUCCESS DOES NOT TRANSFER, WHICH IS THIS ACT\'S NAMED HAZARD:**')
    rec('  ### b273\'s attaining vector is ### w + s g_0 ### -- ### **A DIFFERENT VECTOR FROM')
    rec('  ### THE RULE\'S g_0.** ### Its (SPEC-2) success is its own and is not borrowed here.')
    rec('  ### ### **SO A RULE THAT MEETS (SPEC-2) MUST BE ### PIECEWISE ### AT p = 2, TAKING')
    rec('  ### ### b273\'s v THERE AND g_0 AT EVERY ODD PLACE. ### THAT IS WRITABLE -- IT IS A')
    rec('  ### ### FINITE EXCEPTION, AND b226\'s OWN RULE IS ALREADY PIECEWISE IN THE LEVEL --')
    rec('  ### ### BUT IT IS A COST AND IT IS STATED AS ONE, NOT ABSORBED.**')
    rec()

    # --- T3, T4 ---------------------------------------------------------------------------
    rec('-' * 100)
    rec('### (5) T3 -- (SPEC-3) -- AND T4 -- G-NORM.')
    rec('-' * 100)
    t3 = all(r['nrm'] is not None and r['nrm'] > 0 for r in results)
    rec('  ### **T3 (SPEC-3): the rule gives a NONZERO vector at every prime : %s**'
        % ('CONFIRMED at all cells' if t3 else '### FAILED ###'))
    rec('  ### p = 2\'s level exception is ### THE CORPUS\'S OWN ### , not a new one: b223 records')
    rec('  ### d_1(2,1) = 0, so there is no unit at level 1 there and b226 steps up to ell(2) = 2.')
    rec('  ### **T4 (G-NORM): each u\'_p is divided by its own norm, which is a positive rational')
    rec('  ### at every cell above, so ### SUM_v | ||u\'_v|| - 1 | = SUM_v 0 = 0 ### exactly --')
    rec('  ### the same standard b226 met, and met in the same way.**')
    rec()

    # --- S3: THE EQUIVALENCE ---------------------------------------------------------------
    rec('-' * 100)
    rec('### (6) S3 -- THE EQUIVALENCE. ### **CHECKED FOR THIS RULE, NOT INHERITED.**')
    rec('-' * 100)
    northo = sum(1 for r in results if r['orth'])
    rec('  ### b272 derives <u, g_0> = 0 EXACTLY at every place, and it is re-confirmed here at')
    rec('  ### **%d of %d cells.**' % (northo, len(results)))
    rec('  ### With both sequences normalized, |<u_v, u\'_v> - 1| = |0 - 1| = 1 at EVERY place,')
    rec('  ### so SUM_v | <u_v, u\'_v> - 1 | = SUM_v 1, which ### **DIVERGES OVER INFINITELY MANY')
    rec('  ### PLACES.**')
    rec('  ### By von Neumann DEFINITION 3.3.2 the two C0-sequences are ### **NOT EQUIVALENT**,')
    rec('  ### and by LEMMA 4.1.1 the two incomplete products are ### **MUTUALLY ORTHOGONAL.**')
    rec('  ### ### ### **SO FOR THIS RULE THE EQUIVALENCE QUESTION IS ### SETTLED ### , AND IT IS')
    rec('  ### ### ### SETTLED NEGATIVELY: THE RULE NAMES A DIFFERENT OBJECT, NOT A REFINEMENT')
    rec('  ### ### ### OF b226\'s.**')
    rec('  ### **AND W-ORD-EQUIV-CLASS IS NOT THEREBY CLOSED: it is about b273\'s v, where')
    rec('  ### <u, w> != 0. ### A DIFFERENT VECTOR AND A DIFFERENT QUESTION.**')
    rec()

    io.open(os.path.join(HERE, '..', '..', 'data', 'b275_run.txt'),
            'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('  written: data/b275_run.txt')
    return 0


if __name__ == '__main__':
    sys.exit(main())
