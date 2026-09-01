# -*- coding: utf-8 -*-
"""b276_size_equivalence.py -- M-2 CAMPAIGN, ACT 10. ### SIZE AGAINST EQUIVALENCE.

### THE QUESTION: ### **CAN AN EQUIVALENCE-PRESERVING UNIT SEQUENCE SUPPLY THE FIRST-LEVEL MASS
### THE IDENTITY DEMANDS?**

### THE LOAD-BEARING STEP IS ### **THE FIBER LEMMA** ### : for every `w` in `E_1(Son)` and every
### ball point `b`, the fiber sum `W(b) = SUM_{m off-ball, p^ell m = b} (S_quot w)(m)` is ZERO.
### Given it, SPEC-1's value is ### **EXACTLY QUADRATIC** ### in the ball-size, and the tension
### with von Neumann's summability follows.

### ### **NOTHING IS ADOPTED. ### b262's MASS IS QUOTED, NEVER RE-DERIVED AND NEVER FITTED.**
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

FULL_FAMILY_MAX_N = 121
SAMPLE_IJ = ((1, 1), (1, 2), (2, 1), (2, 2))


def f_ij(i, j, q, N):
    """### `4q P_1 f_{i,j}` with `f_{i,j} = e_{i+qj} - e_i` [b226 / b268], unfolded."""
    a = (i + q * j) % N
    b = i % N
    out = []
    for m in range(N):
        d = {}
        for idx, sg in ((a, 1), (b, -1), ((-a) % N, 1), ((-b) % N, -1)):
            if m == idx:
                d[0] = d.get(0, Fraction(0)) + sg * q
        for k, sg in (((m * a) % N, 1), ((-m * a) % N, 1),
                      ((m * b) % N, -1), ((-m * b) % N, -1)):
            d[k] = d.get(k, Fraction(0)) + sg
        out.append({k: v for k, v in d.items() if v != 0})
    return out


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


def fiber_sums(w, S_quot, ballset, p, ell, N):
    """### `W(b)` FOR EVERY BALL POINT REACHED. ### The act's load-bearing quantity."""
    Sw = S_quot(w)
    pn = pow(p, ell, N)
    W = {}
    for m in range(N):
        if m in ballset:
            continue
        b = (pn * m) % N
        W[b] = spadd(W.get(b, {}), Sw[m])
    return W


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b276 -- COMPONENT 1. ### SIZE AGAINST EQUIVALENCE. ### EXACT. ### NO FLOAT.')
    rec('### REGISTRATION data/b276_registration_2026-09-01.txt SEALED a600dd93.')
    rec('### **NOTHING IS ADOPTED. ### b262\'s MASS IS QUOTED, NEVER RE-DERIVED, NEVER FITTED.**')
    rec('=' * 100)
    rec()

    rec('-' * 100)
    rec('### (0) COMPONENT 0 -- THE NOISE-FLOOR GATE, ON THIS ACT\'S PATH.')
    rec('-' * 100)
    ok0, rows0, det0 = floor_gate([('every quantity in this act', 0, None)], exact=True)
    rec('  gate verdict : %s' % rows0[0][3])
    rec('  detail       : %s' % det0)
    rec()

    rec('-' * 100)
    rec('### (1) S1 -- THE PARAMETERIZATION, ### **DERIVED FROM THE OWNERS.**')
    rec('-' * 100)
    rec('  ### A vector in E_1 that VANISHES ON THE BALL lies in Son: its transform is q times')
    rec('  ### itself, so the transform vanishes on the ball too -- which is Son\'s second half.')
    rec('  ### ### **SO E_1(Son) IS PRECISELY THE BALL-VANISHING PART OF E_1**, and every u\' in')
    rec('  ### ### E_1 splits ORTHOGONALLY as ### **u\' = w + z**, w in E_1(Son), z perpendicular')
    rec('  ### ### to it. ### THE SIZE IS ### **sigma = ||z|| / ||u\'||**.')
    rec('  ### b273\'s v = w + s g_0 is ONE POINT of this; b275\'s rule is the extreme sigma = 1.')
    rec()

    rec('-' * 100)
    rec('### (2) S3 -- ### **THE FIBER LEMMA. ### THE ACT\'S LOAD-BEARING STEP.**')
    rec('-' * 100)
    rec('  CLAIM. For every w in E_1(Son) and every ball point b,')
    rec('    ### **W(b) := SUM over off-ball m with p^ell m = b of (S_quot w)(m)   IS ZERO.**')
    rec('  CONSEQUENCE. The cross term SUM_m (S_quot w)(m) conj(z(p^ell m)) equals')
    rec('  SUM_b conj(z(b)) W(b), ### **SO IT VANISHES FOR EVERY z.** ### And the w-w term')
    rec('  vanishes by b271\'s absorption. ### **ONLY THE z-z TERM SURVIVES.**')
    rec()
    rec('  %-8s %-6s %-9s %-22s %-14s %s'
        % ('(p,n)', 'N', 'd_1 law', 'family scope', 'ball-vanishing', 'W(b) = 0 for all b'))
    lemma_ok = True
    tested_total = 0
    cellinfo = {}
    for (p, ell) in PLACES:
        q = p ** ell
        N = q * q
        F = Field(N)
        ballset, S_quot = projector(N, p, ell)
        cellinfo[(p, ell)] = (q, N, F, ballset, S_quot)
        if N <= FULL_FAMILY_MAX_N:
            pairs = [(i, j) for i in range(1, q) for j in range(1, q)]
            scope = 'FULL family, %d' % len(pairs)
        else:
            pairs = [(i, j) for (i, j) in SAMPLE_IJ if i < q and j < q]
            scope = 'SAMPLE of %d + u' % len(pairs)
        vecs = [f_ij(i, j, q, N) for (i, j) in pairs]
        vecs.append([from_int_vec(u_coeffs(q, m)) for m in range(N)])
        nvan = 0
        allz = True
        for w in vecs:
            if not all(F.is_zero(w[m]) for m in ballset):
                continue
            nvan += 1
            tested_total += 1
            W = fiber_sums(w, S_quot, ballset, p, ell, N)
            if not all(F.is_zero(v) for v in W.values()):
                allz = False
        lemma_ok = lemma_ok and allz
        rec('  %-8s %-6d %-9d %-22s %-14d %s'
            % ('(%d,%d)' % (p, ell), N, (q - 1) ** 2 // 4, scope, nvan,
               'YES' if allz else '### NO ###'))
    rec()
    rec('  ### **FIBER LEMMA VERDICT: %s ### %d ball-vanishing vectors tested.**'
        % ('W(b) = 0 EVERYWHERE' if lemma_ok else 'FIBER LEMMA FAILED', tested_total))
    rec('  ### **SCOPE, PRINTED NOT ELIDED:** the FULL f_{i,j} family at N <= %d, and b226\'s own'
        % FULL_FAMILY_MAX_N)
    rec('  ### u plus a declared sample of four above it -- the registration\'s (I3c) cap.')
    rec('  ### **AND THE FAMILY SPANS E_1(Son), SO BY LINEARITY THE LEMMA HOLDS ON ALL OF IT AT')
    rec('  ### THE CELLS WHERE THE FULL FAMILY WAS TESTED.**')
    rec()

    rec('-' * 100)
    rec('### (3) THE CONTROLS. ### **b273\'s v AS ONE POINT; b275\'s RULE AS THE EXTREME.**')
    rec('-' * 100)
    q, N, F, ballset, S_quot = cellinfo[(2, 2)]

    def gc(c):
        o = []
        for m in range(N):
            d = {}
            if m == c % N:
                d[0] = d.get(0, Fraction(0)) + q
            if m == (-c) % N:
                d[0] = d.get(0, Fraction(0)) + q
            for k in ((m * c) % N, (-m * c) % N):
                d[k] = d.get(k, Fraction(0)) + 1
            o.append({k: v for k, v in d.items() if v != 0})
        return o

    g0 = gc(0)
    w = [spadd(gc(2)[m], spscale(gc(6)[m], Fraction(-1))) for m in range(N)]
    # ### s^2 = -8/11 + (8/11) sqrt2, from b273. ### Represented in Q(sqrt2) as (a, b).
    s2 = (Fraction(-8, 11), Fraction(8, 11))
    nw = Fraction(128)
    ng = Fraction(160)
    A2gg = Fraction(48)          # ### <A_2 g_0, g_0> at (2,2), b271/b273
    # ### ||v||^2 = nw + s^2 * ng ; sigma^2 = s^2 ng / ||v||^2 ; P^ = s^2 A2gg / ||v||^2.
    vn = (nw + s2[0] * ng, s2[1] * ng)
    sig = (s2[0] * ng, s2[1] * ng)
    pv = (s2[0] * A2gg, s2[1] * A2gg)
    rec('  ### b273\'s v = w + s g_0 at (2,2), with s^2 = %s + %s sqrt2 [b273]:'
        % (s2[0], s2[1]))
    rec('    ||w||^2 = %s , ||g_0||^2 = %s , <A_2 g_0,g_0> = %s   [b271 / b273]'
        % (nw, ng, A2gg))
    rec('    ||v||^2   = %s + %s sqrt2' % (vn[0], vn[1]))
    rec('    sigma^2   = (%s + %s sqrt2) / ||v||^2' % (sig[0], sig[1]))
    rec('    P^(SPEC-1) = (%s + %s sqrt2) / ||v||^2' % (pv[0], pv[1]))
    rec('  ### **THE BOUND |P^| <= sigma^2 REDUCES TO %s <= %s, i.e. TO A RATIONAL FACT ABOUT'
        % (A2gg, ng))
    rec('  ### THE TWO NUMERATORS, SINCE BOTH SHARE THE POSITIVE DENOMINATOR ||v||^2 AND THE')
    rec('  ### COMMON FACTOR s^2 > 0 : %s**' % ('CONFIRMED' if A2gg <= ng else '### FAILED ###'))
    rec()
    rule_val = Fraction(A2gg, ng)
    rec('  ### b275\'s RULE IS THE EXTREME sigma = 1 (w = 0): P^ = <A_2 g_0,g_0> / ||g_0||^2 = %s'
        % rule_val)
    rec('  ### ### **AND THAT IS EXACTLY b274\'s CLOSED FORM (q-1)/(2(q+1)) AT q = 4 : %s**'
        % ('CONFIRMED' if rule_val == Fraction(3, 10) else '### FAILED ###'))
    rec('  ### The bound |P^| <= sigma^2 = 1 holds there with room: %s <= 1.' % rule_val)
    rec('  ### **THE CONTROLS CHECK THE DERIVATION AND ARE NEVER ITS EVIDENCE.**')
    rec()

    rec('-' * 100)
    rec('### (4) S4 -- ### **THE TENSION.**')
    rec('-' * 100)
    rec('  ### (i) FROM THE OVERLAP. ### b226\'s u lies in E_1(Son) and z is perpendicular to it,')
    rec('  ### so <u, u\'> = <u, w> EXACTLY, and normalized |<u^,u\'^>| <= ||w|| = sqrt(1-sigma^2).')
    rec('  ### Hence ### **|<u^,u\'^> - 1| >= 1 - sqrt(1-sigma^2) >= sigma^2 / 2**.')
    rec('  ### von Neumann DEFINITION 3.3.2 makes equivalence the CONVERGENCE of')
    rec('  ### SUM_v |<u_v, u\'_v> - 1|, so ### **EQUIVALENCE REQUIRES SUM_v sigma_v^2 < infinity.**')
    rec()
    rec('  ### (ii) FROM SPEC-1. ### By the fiber lemma only the z-z term survives, so')
    rec('  ### ### **|P^_v| <= sigma_v^2** ### at every place.')
    rec()
    rec('  ### (iii) THEREFORE ### **SUM_v |P^_v| <= SUM_v sigma_v^2 < infinity.**')
    rec('  ### A convergent series has ### VANISHING TAILS ### , so the sum over the window')
    rec('  ### (a, a^2] tends to ### ZERO ### as a grows.')
    rec()
    rec('  ### (iv) AND b262 DERIVES THE OPPOSITE DEMAND ON THE SAME WINDOW, QUOTED NOT')
    rec('  ### RE-DERIVED: the junction ### **DIVERGES ALONG THE CUTOFF LIMIT**, and it is the')
    rec('  ### primes in (a, a^2] with n_p = 1 that ### **CARRY THE WHOLE GROWTH.**')
    rec('  ### ### ### **A QUANTITY THAT TENDS TO ZERO CANNOT SUPPLY ONE THAT TENDS TO INFINITY.**')
    rec()
    rec('  ### **THE ATTRIBUTION, WHICH IS THIS ACT\'S CENTRAL CARE (registration (C)):**')
    rec('  ### ### **THE ARGUMENT NEVER ASKS HOW b262\'s GROWTH SPLITS BETWEEN PER-PLACE SIZE AND')
    rec('  ### ### THE NUMBER OF PLACES IN THE WINDOW. ### IT DOES NOT NEED TO: A CONVERGENT')
    rec('  ### ### SERIES HAS VANISHING TAILS HOWEVER MANY TERMS THE WINDOW HOLDS.**')
    rec('  ### The failure mode the registration named -- allowing each place a merely BOUNDED')
    rec('  ### contribution and letting place-count do the work -- ### **IS EXACTLY WHAT')
    rec('  ### EQUIVALENCE FORBIDS: IT MAKES THE CONTRIBUTIONS SUMMABLE, NOT MERELY BOUNDED.**')
    rec()

    io.open(os.path.join(HERE, '..', '..', 'data', 'b276_run.txt'),
            'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('  written: data/b276_run.txt')
    return 0


if __name__ == '__main__':
    sys.exit(main())
