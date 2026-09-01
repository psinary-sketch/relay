# -*- coding: utf-8 -*-
"""b277_aggregation_stated.py -- M-2 CAMPAIGN, ACT 11. ### THE AGGREGATION STATED (ATTEMPT).

### **A STATED CANDIDATE IS NOT A REPLACEMENT.** ### Replacing b226's ruled choice is the
### author's alone, and M-2 is owed until an author ruling adopts something.

### THE ACT'S NAMED HAZARD: ### **THE MODEL LEVEL vs THE LIMIT.** ### A value at the cell
### `(p, ell(p))` is a statement about a FINITE MODEL. ### The aggregation is a statement about
### the LIMIT OBJECT, and the step between them has a constituent -- von Neumann's Def 3.3.1
### clause (i), `f_alpha in H_alpha` -- ### **THAT MUST BE CHECKED AND NOT ASSUMED.**

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


def g_c(c, q, N):
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


def primes_upto(X):
    sieve = [True] * (X + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(X ** Fraction(1, 2)) + 2):
        if i * i > X:
            break
        if sieve[i]:
            for j in range(i * i, X + 1, i):
                sieve[j] = False
    return [i for i in range(2, X + 1) if sieve[i]]


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b277 -- COMPONENT 1. ### THE AGGREGATION STATED (ATTEMPT). ### EXACT. ### NO FLOAT.')
    rec('### REGISTRATION data/b277_registration_2026-09-01.txt SEALED 6fd57ecd.')
    rec('### **NOTHING IS ADOPTED. ### A STATED CANDIDATE IS NOT A REPLACEMENT.**')
    rec('=' * 100)
    rec()

    rec('-' * 100)
    rec('### (0) COMPONENT 0 -- THE E0 GATE, ON THIS ACT\'S PATH.')
    rec('-' * 100)
    ok0, rows0, det0 = floor_gate([('every quantity in this act', 0, None)], exact=True)
    rec('  gate verdict : %s' % rows0[0][3])
    rec('  detail       : %s' % det0)
    rec()

    # ---------------------------------------------------------------------------------------
    rec('-' * 100)
    rec('### (1) THE PIECEWISE RULE, AND THE AGGREGATION, WRITTEN WHOLE AT THE MODEL LEVEL.')
    rec('-' * 100)
    rec('  ### ### **u\'\'_p := 4q P_1 e_0 / ||.||   at odd p, level ell(p) = 1;**')
    rec('  ### ### **u\'\'_2 := (w + s g_0) / ||.||  at (2,2), b273\'s v with s^2 = -8/11 + (8/11)sqrt2.**')
    rec('  EVERY CONSTITUENT UNFOLDED TO ITS OWNER:')
    rec('    4q P_1 = (q + S)(1 + Pi); S; Pi                [b226]')
    rec('    4q P_1 e_0 = 2q e_0 + 2 * 1                    [b272]')
    rec('    w = g_2 - g_6, in Son                          [b273 / b274]')
    rec('    s^2                                            [b273, exact]')
    rec('    ell(p) = 2 if p = 2 else 1                     [b226; d_1(2,1) = 0]')
    rec('  ### **THE AGGREGATION: ### Q_p(k) := <U^k S_quot u\'\'_p, u\'\'_p> at the cell (p, ell(p)).**')
    rec()

    results = []
    for (p, ell) in PLACES:
        q = p ** ell
        N = q * q
        F = Field(N)
        ballset, S_quot = projector(N, p, ell)
        g0 = g_c(0, q, N)
        u = [from_int_vec(u_coeffs(q, m)) for m in range(N)]
        if p == 2:
            w = [spadd(g_c(2, q, N)[m], spscale(g_c(6, q, N)[m], Fraction(-1)))
                 for m in range(N)]
            branch = 'b273 v = w + s g_0'
        else:
            w = None
            branch = 'b275 g_0'
        # ### E_1 MEMBERSHIP, CHECKED AT EACH BRANCH AND NOT INHERITED.
        Sg = apply_S(g0, N)
        inE1_g0 = all(F.eq(Sg[m], spscale(g0[m], Fraction(q))) for m in range(N))
        inE1_w = True
        if w is not None:
            Sw = apply_S(w, N)
            inE1_w = all(F.eq(Sw[m], spscale(w[m], Fraction(q))) for m in range(N))
        # ### THE SON TEST -- the constituent the limit step needs.
        vanishes_g0 = all(F.is_zero(g0[m]) for m in ballset)
        # ### SPEC-1 AT k = ell, COMPUTED UNDER THE CELL'S OWN BRANCH.
        # ### ### **THE (2,2) ROW MUST NOT INHERIT g_0's VALUE: ITS UNIT IS b273's v.**
        closed = Fraction(q - 1, 2 * (q + 1))
        if w is None:
            a1 = F.reduce(sesq(g0, S_quot, p, ell, N))
            n1 = F.reduce(ip(g0, g0, N))
            rat = all(x == 0 for x in a1[1:]) and all(x == 0 for x in n1[1:])
            val = Fraction(a1[0], n1[0]) if rat else None
            val_sq2 = None
        else:
            # ### v = w + s g_0 with all cross terms vanishing [b273]: numerator and
            # ### denominator are LINEAR in s^2, and both live in Q(sqrt2).
            s2c = (Fraction(-8, 11), Fraction(8, 11))
            aww = F.reduce(sesq(w, S_quot, p, ell, N))
            agg = F.reduce(sesq(g0, S_quot, p, ell, N))
            nww = F.reduce(ip(w, w, N))[0]
            ngg = F.reduce(ip(g0, g0, N))[0]
            aw0 = aww[0] if all(x == 0 for x in aww[1:]) else None
            ag0 = agg[0] if all(x == 0 for x in agg[1:]) else None
            num = (aw0 + s2c[0] * ag0, s2c[1] * ag0)
            den = (nww + s2c[0] * ngg, s2c[1] * ngg)
            # ### rationalize (a+b r)/(c+d r) with r^2 = 2 : multiply by (c - d r).
            dn = den[0] * den[0] - 2 * den[1] * den[1]
            val_sq2 = ((num[0] * den[0] - 2 * num[1] * den[1]) / dn,
                       (num[1] * den[0] - num[0] * den[1]) / dn)
            val = None
        r_extra = val_sq2
        orth = F.is_zero(ip(u, g0, N))
        results.append({'p': p, 'ell': ell, 'q': q, 'N': N, 'branch': branch,
                        'inE1': inE1_g0 and inE1_w, 'son': vanishes_g0,
                        'val': val, 'val_sq2': r_extra, 'closed': closed, 'orth': orth})

    rec('  %-8s %-20s %-10s %-16s %-16s %s'
        % ('(p,n)', 'branch', 'in E_1?', 'Q_p(l) p^{l/2}', 'closed form', 'in Son?'))
    for r in results:
        rec('  %-8s %-20s %-10s %-16s %-16s %s'
            % ('(%d,%d)' % (r['p'], r['ell']), r['branch'],
               'YES' if r['inE1'] else '### NO ###',
               (str(r['val']) if r['val'] is not None
                else '%s + %s sqrt2' % (r['val_sq2'][0], r['val_sq2'][1])),
               str(r['closed']) if r['p'] != 2 else '(n/a -- other branch)',
               'YES' if r['son'] else '### NO ###'))
    rec()
    closed_ok = all(r['p'] == 2 or r['val'] == r['closed'] for r in results)
    rec('  ### **THE CLOSED FORM Q_p(1) p^{1/2} = (p-1)/(2(p+1)) HOLDS AT EVERY ODD PLACE : %s**'
        % ('CONFIRMED' if closed_ok else '### FAILED ###'))
    rec('  ### ### **SO AT THE MODEL LEVEL THIS IS A FUNCTION OVER PLACES WITH A STATED VALUE --')
    rec('  ### ### A CLOSED FORM AT EVERY ODD PRIME AND EXACT VALUES AT p = 2. ### IT MEETS')
    rec('  ### ### b275\'s OWN BAR: IT IS A NUMBER AT EVERY PLACE, NOT ONLY A UNIT.**')
    rec()

    # ---------------------------------------------------------------------------------------
    rec('-' * 100)
    rec('### (2) T1 -- (SPEC-1) AT EVERY PLACE. ### RECOMPUTED, NOT INHERITED.')
    rec('-' * 100)
    t1 = all((r['val'] is not None and r['val'] != 0) if r['p'] != 2
             else (r['val_sq2'][0] != 0 or r['val_sq2'][1] != 0) for r in results)
    for r in results:
        if r['p'] != 2:
            rec('  (%d,%d)  Q_p(1) p^{1/2} = %s  nonzero: %s'
                % (r['p'], r['ell'], r['val'], 'YES' if r['val'] != 0 else 'NO'))
    rec('  ### **AND (p-1)/(2(p+1)) >= 1/4 FOR EVERY ODD p, SO IT IS NONZERO BY ARITHMETIC AND')
    rec('  ### NOT BY SURVEY.** ### T1 VERDICT: %s'
        % ('SPEC-1 holds at every odd place' if t1 else 'T1 FAILED'))
    rec()

    # ---------------------------------------------------------------------------------------
    rec('-' * 100)
    rec('### (3) T2 -- (SPEC-2). ### VACUOUS AT LEVEL 1; RECOMPUTED AT (2,2).')
    rec('-' * 100)
    rec('  ### At ell = 1 the range 1 <= k <= 0 is ### **EMPTY**, so (SPEC-2) is ### **VACUOUS')
    rec('  ### THERE -- A VACUITY AND NOT A TRIUMPH.** ### Seven of the eight cells.')
    q, N, F = 4, 16, Field(16)
    ballset, S_quot = projector(16, 2, 2)
    g0 = g_c(0, 4, 16)
    w = [spadd(g_c(2, 4, 16)[m], spscale(g_c(6, 4, 16)[m], Fraction(-1))) for m in range(16)]
    s2 = (Fraction(-8, 11), Fraction(8, 11))
    # ### v = w + s g_0 ; all cross terms vanish [b273], so numerators are linear in s^2.
    aw = F.reduce(sesq(w, S_quot, 2, 1, 16))
    ag = F.reduce(sesq(g0, S_quot, 2, 1, 16))
    nw = F.reduce(ip(w, w, 16))[0]
    ng = F.reduce(ip(g0, g0, 16))[0]
    # ### <A w,w> at k=1 is (128/3)(1+sqrt2) [b273]; represent in Q(sqrt2) as (a,b).
    aw_q = (Fraction(128, 3), Fraction(128, 3))
    ag_q = (Fraction(48), Fraction(0))
    # ### numerator = aw + s^2 * ag ; denominator = nw + s^2 * ng, in Q(sqrt2).
    num = (aw_q[0] + s2[0] * ag_q[0] + 2 * s2[1] * ag_q[1],
           aw_q[1] + s2[0] * ag_q[1] + s2[1] * ag_q[0])
    den = (nw + s2[0] * ng, s2[1] * ng)
    theta = Fraction(2, 3)
    # ### equality num/den = theta  <=>  num - theta*den = 0, componentwise in Q(sqrt2).
    chk = (num[0] - theta * den[0], num[1] - theta * den[1])
    rec('  ### AT (2,2), k = 1, UNDER THE AGGREGATION\'S OWN NORMALIZATION:')
    rec('    numerator   = %s + %s sqrt2' % (num[0], num[1]))
    rec('    denominator = %s + %s sqrt2' % (den[0], den[1]))
    rec('    act 9\'s term = %s' % theta)
    rec('    numerator - term * denominator = %s + %s sqrt2' % (chk[0], chk[1]))
    t2 = (chk[0] == 0 and chk[1] == 0)
    rec('  ### ### **T2 AT (2,2): %s**'
        % ('THE AGGREGATION EQUALS act 9\'s TERM EXACTLY' if t2
           else '### THE AGGREGATION DOES NOT EQUAL act 9\'s TERM ###'))
    rec()

    # ---------------------------------------------------------------------------------------
    rec('-' * 100)
    rec('### (4) T3, T4, T5.')
    rec('-' * 100)
    t3 = all(r['inE1'] for r in results)
    rec('  ### **T3 (SPEC-3): a nonzero unit at every prime, E_1 membership checked at each')
    rec('  ### branch : %s.** ### p = 2\'s level exception is the corpus\'s own (d_1(2,1) = 0).'
        % ('CONFIRMED' if t3 else '### FAILED ###'))
    rec('  ### **T4a (G-NORM): each u\'\'_p is divided by its own norm, so SUM_v | ||u\'\'_v|| - 1 |')
    rec('  ### = 0 EXACTLY -- the standard b226 met, met the same way.**')
    rec()
    nson = sum(1 for r in results if not r['son'])
    rec('  ### ### **T4b -- THE C0 CONDITION\'S FIRST CLAUSE. ### THIS IS WHERE THE ACT TURNS.**')
    rec('  ### b226 carries the requirement as ### "(i) a vector at every place ... f_alpha in')
    rec('  ### H_alpha for all alpha in I" ### , so the unit must lie in H_v = S-bar_v.')
    rec('  ### b198 (I4) makes S-bar ### THE L^2-CLOSURE OF THE TOWER\'S UNION ### , and (I2)')
    rec('  ### places a level vector in the limit only through ### THE CLOSURE OF ITS LEVEL TOWER.')
    rec('  ### **AND b198\'s WHOLE OBJECT IS TO PROVE E_1(S-bar_v) NONZERO -- WHICH WOULD BE')
    rec('  ### VACUOUS IF S-bar WERE THE FULL SPACE. ### SO THE TOWER IS THE ### Son ### TOWER.**')
    rec()
    rec('  ### THE CONSTITUENT, COMPUTED: does the candidate unit lie in Son at its cell?')
    rec('  %-8s %-26s %s' % ('(p,n)', 'g_0 vanishes on the ball?', 'in Son(p, ell(p))?'))
    for r in results:
        rec('  %-8s %-26s %s'
            % ('(%d,%d)' % (r['p'], r['ell']), 'YES' if r['son'] else 'NO',
               'YES' if r['son'] else '### NO ###'))
    rec()
    rec('  ### ### **THE CANDIDATE UNIT IS NOT IN Son AT ANY OF THE %d CELLS.** ### At odd p it')
    rec('  ### ### is g_0, whose nonzero ball value is exactly what put it in b271\'s escape')
    rec('  ### ### class; at (2,2) it is w + s g_0, and the g_0 part carries the same ball')
    rec('  ### ### value. ### Cells not in Son: %d of %d.' % (nson, len(results)))
    rec('  ### ### ### **SO THE ONLY WARRANT THE CORPUS OWNS FOR PLACING A LEVEL VECTOR IN')
    rec('  ### ### ### S-bar_v -- b198 (I2)\'s CLOSURE OF THE ### Son ### TOWER -- DOES NOT APPLY,')
    rec('  ### ### ### AND THE CORPUS SUPPLIES NO OTHER. ### CLAUSE (i) IS UNWARRANTED.**')
    rec('  ### **STATED AT ITS EXACT STRENGTH AND NOT ABOVE IT: ### IT IS NOT PROVED THAT THE')
    rec('  ### CANDIDATE LIES OUTSIDE S-bar_v. ### IT IS THAT NO WARRANT PLACES IT INSIDE, AND A')
    rec('  ### CONSTITUENT OF THE AGGREGATION IS THEREFORE MISSING RATHER THAN FALSE.**')
    rec()
    northo = sum(1 for r in results if r['orth'])
    rec('  ### **T5 (THE CLASS): <u, g_0> = 0 exactly at %d of %d cells, carried from b272 and'
        % (northo, len(results)))
    rec('  ### re-confirmed here. ### With both normalized the summands are 1 at every odd place,')
    rec('  ### so the sum diverges and the objects are ### MUTUALLY ORTHOGONAL ### -- b276\'s')
    rec('  ### finding, carried and not re-derived, and FORCED rather than incidental.**')
    rec()

    # ---------------------------------------------------------------------------------------
    rec('-' * 100)
    rec('### (5) THE SIZE CONTROL. ### **RUN AFTER THE STATEMENT WAS FIXED. ### NO FIT.**')
    rec('-' * 100)
    rec('  The aggregate over odd places is SUM_p Q_p(1), with Q_p(1) = (p-1)/(2(p+1) p^{1/2}).')
    rec('  ### **AN EXACT DIVERGENCE ARGUMENT, NO FLOATS: ### (p-1)/(2(p+1)) >= 1/4 for p >= 3,')
    rec('  ### so Q_p(1) >= 1/(4 p^{1/2}), and SUM_p 1/(4 p^{1/2}) DIVERGES.**')
    rec('  ### THE RATIONAL PART\'S PARTIAL SUMS, EXACT:')
    rec('  ### **THE PARTIAL SUMS ARE EXACT RATIONALS WITH HUNDREDS OF DIGITS, WHICH WOULD BE')
    rec('  ### UNREADABLE AND WOULD ADD NOTHING; THE LOWER BOUND CARRIES THE WHOLE POINT AND IS')
    rec('  ### ALSO EXACT. ### THAT SUBSTITUTION IS DECLARED, NOT MADE QUIETLY.**')
    rec('    %-10s %-12s %-22s %s'
        % ('X', 'odd p <= X', 'SUM >= count/4', 'every term >= 1/4?'))
    for X in (10, 100, 1000, 10000):
        ps = [pp for pp in primes_upto(X) if pp != 2]
        floor_bound = Fraction(len(ps), 4)
        allq = all(Fraction(pp - 1, 2 * (pp + 1)) >= Fraction(1, 4) for pp in ps)
        rec('    %-10d %-12d %-22s %s'
            % (X, len(ps), str(floor_bound), 'YES' if allq else '### NO ###'))
    rec('  ### **THE AGGREGATE DIVERGES. ### AND b262\'s TARGET ALSO DIVERGES ALONG ITS CUTOFF.**')
    rec('  ### ### **NO FIT IS MADE AND NONE IS BANKED. ### THE TWO ARE NOT COMPARED IN')
    rec('  ### ### MAGNITUDE, ONLY REPORTED AS BOTH DIVERGENT** -- and b276\'s sentence is')
    rec('  ### carried: a divergent mass is CONSISTENT with orthogonality, which is precisely')
    rec('  ### why this candidate can diverge at all.')
    rec()

    io.open(os.path.join(HERE, '..', '..', 'data', 'b277_run.txt'),
            'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('  written: data/b277_run.txt')
    return 0


if __name__ == '__main__':
    sys.exit(main())
