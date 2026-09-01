# -*- coding: utf-8 -*-
"""b274_straddle_generally.py -- M-2 CAMPAIGN, ACT 8. ### THE STRADDLE, GENERALLY.

### THE QUESTION: ### **DOES THE (SPEC-2) RANGE STRADDLE act 9's TERM AT EVERY PLACE AND LEVEL?**

### ### **b273 ANSWERED ONE CELL. ### NOTHING HERE WIDENS THAT BY ASSERTION.**
### A comparison the order channel cannot certify is reported ### UNCERTIFIED ### , NEVER AS
### FALSE (`W-ORD-ORDER-CHANNEL`). ### **A FLOAT PROBE IS NOT A CERTIFICATE AND IS NOT BANKED.**

### ### **NO FLOAT TOKEN APPEARS IN THIS FILE.** ### Component 0 is CALLED on this path.
"""
import io
import os
import sys
from fractions import Fraction

sys.stdout.reconfigure(encoding='utf-8', errors='replace')
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, '..'))

from b270_ambient_pairing import (Field, ball_of, orbit_classes, spadd, spconj, spmul, spscale)
from b271_top_level_no_go import apply_S
from noise_floor import gate as floor_gate

CELLS = [(2, 2), (3, 2), (2, 3), (2, 4)]
PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
NMAX = 8


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


def vsub(a, b):
    return [spadd(a[m], spscale(b[m], Fraction(-1))) for m in range(len(a))]


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


def ip(x, N):
    acc = {}
    for m in range(N):
        if not x[m]:
            continue
        acc = spadd(acc, spmul(x[m], spconj(x[m], N), N))
    return acc


def theta(p, n, k):
    return Fraction(p ** n - p ** k, p ** n - 1)


def R_g0_closed(q):
    """### S1's CLOSED FORM, DERIVED FROM THE OWNERS: `R(g_0) = (q-1)/(2(q+1))`."""
    return Fraction(q - 1, 2 * (q + 1))


def main():
    out = []

    def rec(s=''):
        print(s)
        out.append(s)

    rec('=' * 100)
    rec('b274 -- COMPONENT 1. ### THE STRADDLE, GENERALLY. ### EXACT. ### NO FLOAT.')
    rec('### REGISTRATION data/b274_registration_2026-09-01.txt SEALED 3abf4af9.')
    rec('### **b273 ANSWERED ONE CELL. ### NOTHING HERE WIDENS THAT BY ASSERTION.**')
    rec('=' * 100)
    rec()

    rec('-' * 100)
    rec('### (0) COMPONENT 0 -- THE NOISE-FLOOR GATE, ON THIS ACT\'S PATH.')
    rec('-' * 100)
    ok0, rows0, det0 = floor_gate([('every quantity in this act', 0, None)], exact=True)
    rec('  gate verdict : %s' % rows0[0][3])
    rec('  detail       : %s' % det0)
    rec()

    # ---------------------------------------------------------------------------------------
    rec('-' * 100)
    rec('### (1) S1 -- `R(g_0)` IN CLOSED FORM, DERIVED FROM THE OWNERS.')
    rec('-' * 100)
    rec('  b272 gives g_0(m) = 2q[m=0] + 2, so g_0 is CONSTANT 2 off the ball and')
    rec('  S_quot g_0 = 2 * 1_offball.')
    rec('  ### For 1 <= k <= n-1 NO off-ball m has p^k m = 0: that needs p^{2n-k} | m, and')
    rec('  ### 2n - k > n, so it would force p^n | m. ### **HENCE EVERY FACTOR g_0(p^k m) IS 2.**')
    rec('  <A g_0, g_0> = 4(N - q)   and   <g_0, g_0> = (2q+2)^2 + 4(N-1),   N = q^2')
    rec('  ### ### **R(g_0) = 4q(q-1) / (4(q+1)^2 + 4(q^2-1)) = (q-1) / (2(q+1)),')
    rec('  ### ### INDEPENDENT OF k.**')
    rec()
    rec('  %-8s %-5s %-6s %-4s %-14s %-16s %s'
        % ('(p,n)', 'q', 'N', 'k', 'closed form', 'exact <A g0,g0>', 'closed form holds?'))
    s1_all = True
    cellinfo = {}
    for (p, n) in CELLS:
        q = p ** n
        N = q * q
        F = Field(N)
        ballset, S_quot = projector(N, p, n)
        g0 = g_c(0, q, N)
        nrm = ip(g0, N)
        cellinfo[(p, n)] = (q, N, F, ballset, S_quot)
        for k in range(1, n):
            a = sesq(g0, S_quot, p, k, N)
            cl = R_g0_closed(q)
            okc = F.eq(a, spscale(nrm, cl))
            aq = F.reduce(a)
            s1_all = s1_all and okc
            rec('  %-8s %-5d %-6d %-4d %-14s %-16s %s'
                % ('(%d,%d)' % (p, n), q, N, k, str(cl),
                   str(aq[0]) if all(x == 0 for x in aq[1:]) else '(not rational)',
                   'YES' if okc else '### NO ###'))
    rec()
    rec('  ### F-CONTROL: the closed form gives %s at (2,2), which is b273\'s banked 3/10 : %s'
        % (R_g0_closed(4), 'CONFIRMED' if R_g0_closed(4) == Fraction(3, 10) else '### FAILED ###'))
    rec('  ### S1 VERDICT: %s at every cell and every k computed'
        % ('the closed form holds exactly' if s1_all else 'S1 CLOSED FORM FAILED'))
    rec()

    # ---------------------------------------------------------------------------------------
    rec('-' * 100)
    rec('### (2) S3 LOW SIDE -- ### **DERIVED GENERALLY, BY RATIONAL ALGEBRA ALONE.**')
    rec('-' * 100)
    rec('  CLAIM. For every prime p, every n >= 2 and every 1 <= k <= n-1:')
    rec('  ### ### **R(g_0) = (q-1)/(2(q+1))  <  (q - p^k)/(q - 1) = act 9\'s term.**')
    rec('  PROOF. Both denominators are positive, so the claim is')
    rec('    2(q+1)(q - p^k) - (q-1)^2 > 0.')
    rec('  Expanding: ### **2(q+1)(q-p^k) - (q-1)^2 = q^2 - 2q p^k + 4q - 2p^k - 1.**')
    rec('  Since k <= n-1 we have p^k <= p^{n-1} = q/p <= q/2, hence')
    rec('    2q p^k <= q^2   and   2 p^k <= q,')
    rec('  so the expression is ### **>= q^2 - q^2 + 4q - q - 1 = 3q - 1 > 0.**   QED')
    rec()
    bad = 0
    tot = 0
    idbad = 0
    bdbad = 0
    worst = None
    for p in PRIMES:
        for n in range(2, NMAX + 1):
            q = p ** n
            for k in range(1, n):
                tot += 1
                pk = p ** k
                lhs = 2 * (q + 1) * (q - pk) - (q - 1) ** 2
                rhs = q * q - 2 * q * pk + 4 * q - 2 * pk - 1
                if lhs != rhs:
                    idbad += 1
                if not (2 * q * pk <= q * q and 2 * pk <= q):
                    bdbad += 1
                if lhs < 3 * q - 1:
                    bdbad += 1
                th = theta(p, n, k)
                r0 = R_g0_closed(q)
                if not (r0 < th):
                    bad += 1
                margin = th - r0
                if worst is None or margin < worst[0]:
                    worst = (margin, p, n, k)
    rec('  ### THE PROOF\'S TWO STEPS, CHECKED AS RATIONAL FACTS OVER A SWEEP -- ### THE CONTROL')
    rec('  ### CHECKS THE DERIVATION AND IS NEVER ITS EVIDENCE:')
    rec('    primes %s, n = 2..%d, all k in range : ### **%d (p,n,k) TRIPLES**'
        % (PRIMES, NMAX, tot))
    rec('    the polynomial identity failed in : %d cases' % idbad)
    rec('    the two bounds or the 3q-1 floor failed in : %d cases' % bdbad)
    rec('    ### **R(g_0) < act 9\'s term failed in : %d cases**' % bad)
    rec('    tightest margin over the sweep : %s at (p,n,k) = (%d,%d,%d)'
        % (worst[0], worst[1], worst[2], worst[3]))
    rec()
    rec('  ### ### **LOW SIDE VERDICT: %s**'
        % ('DERIVED FOR ALL p AND ALL n >= 2, WITH THE SWEEP AS A CONTROL AND THE ALGEBRA AS '
           'THE PROOF' if bad == 0 and idbad == 0 and bdbad == 0
           else 'LOW SIDE FAILED -- SEE THE COUNTS ABOVE'))
    rec()

    # ---------------------------------------------------------------------------------------
    rec('-' * 100)
    rec('### (3) S2 -- THE FAMILY NAMED FROM b272\'s STRUCTURE, AND ### **WHAT IT DOES NOT DO.**')
    rec('-' * 100)
    rec('  b273\'s high vector at (2,2) is g_2 - g_6 = g_c - g_{c+q} with c = p^{n-1}, q = p^n.')
    rec('  ### THE FAMILY: ### **w_c := g_c - g_{c+q}.**')
    rec('  DERIVED, AND VERIFIED BELOW: on the ball (m = jq) the exponentials of g_c and')
    rec('  g_{c+q} COINCIDE, because zeta^{jq(c+q)} = zeta^{jqc + jN} = zeta^{jqc}; and the delta')
    rec('  parts miss the ball when q does not divide c. ### **SO w_c VANISHES ON THE BALL;**')
    rec('  and S w_c = q w_c, so its TRANSFORM vanishes there too.')
    rec('  ### ### **THEREFORE w_c LIES IN Son(p,n) -- b226\'s OWN SECTOR -- WHILE g_0 LIES IN')
    rec('  ### ### b271\'s ESCAPE CLASS. ### THE STRADDLE AT (2,2) IS BETWEEN THE TWO.**')
    rec()
    rec('  %-8s %-4s %-12s %-10s %-14s %-16s %s'
        % ('(p,n)', 'k', 'c = p^{n-1}', 'in Son?', 'act 9 term', 'R(w_c)', 'above the term?'))
    s2rows = []
    for (p, n) in CELLS:
        q, N, F, ballset, S_quot = cellinfo[(p, n)]
        c = p ** (n - 1)
        w = vsub(g_c(c, q, N), g_c((c + q) % N, q, N))
        vanish = all(F.is_zero(w[m]) for m in sorted(ballset))
        Sw = apply_S(w, N)
        inE1 = all(F.eq(Sw[m], spscale(w[m], Fraction(q))) for m in range(N))
        nw = F.reduce(ip(w, N))
        for k in range(1, n):
            aw = F.reduce(sesq(w, S_quot, p, k, N))
            th = theta(p, n, k)
            israt = all(x == 0 for x in aw[1:]) and all(x == 0 for x in nw[1:])
            if israt and nw[0] != 0:
                val = Fraction(aw[0]) / Fraction(nw[0])
                above = val > th
                shown = str(val)
            else:
                val = None
                above = None
                shown = '(not rational -- see (2,2) note)'
            s2rows.append(((p, n), k, vanish, inE1, th, val, above))
            rec('  %-8s %-4d %-12d %-10s %-14s %-16s %s'
                % ('(%d,%d)' % (p, n), k, c,
                   'YES' if (vanish and inE1) else '### NO ###', str(th), shown,
                   ('YES' if above else 'no') if above is not None else 'UNCERTIFIED HERE'))
    rec()
    rec('  ### **AT (2,2) THE VALUE IS NOT RATIONAL -- IT IS (1 + sqrt2)/3, WHICH b273 CERTIFIED')
    rec('  ### EXACTLY AND WHICH IS ABOVE 2/3. ### THAT ROW IS b273\'s, NOT RE-DERIVED HERE.**')
    nunc = sum(1 for r in s2rows if r[6] is None)
    rec('  ### ### **R(w_c) IS NOT RATIONAL AT ANY CELL COMPUTED -- IT CARRIES SEVERAL NONZERO')
    rec('  ### ### CYCLOTOMIC COEFFICIENTS -- SO THE ORDER CHANNEL DOES NOT REACH IT AND EVERY')
    rec('  ### ### ROW IS REPORTED ### UNCERTIFIED ### : %d OF %d.**' % (nunc, len(s2rows)))
    rec('  ### **THE (2,2) ROW IS THE EXCEPTION IN SUBSTANCE THOUGH NOT IN FORM: b273 CERTIFIED')
    rec("  ### IT SEPARATELY AS (1 + sqrt2)/3 > 2/3, AND THAT ROW IS b273's, NOT RE-DERIVED.**")
    rec('  ### ### **SO THIS ACT DERIVES NO CLOSED FORM FOR THE FAMILY AND CERTIFIES NO HIGH')
    rec("  ### ### WITNESS BEYOND b273's. ### THE FAMILY NAMED FROM b272's STRUCTURE IS NOT")
    rec('  ### ### SHOWN TO WORK ANYWHERE ELSE, AND IS NOT SHOWN TO FAIL EITHER.**')
    rec()

    # ---------------------------------------------------------------------------------------
    rec('-' * 100)
    rec('### (4) LEVEL 1, STATED AND NOT SKIPPED. ### AND THE CELLS THE RULED CHOICE ACTUALLY USES.')
    rec('-' * 100)
    rec('  At n = 1 the (SPEC-2) range 1 <= k <= n-1 = 0 is ### **EMPTY**, so (SPEC-2) is')
    rec('  ### VACUOUS ### there -- not satisfied, not violated. ### b270 established this and')
    rec('  it is carried, not re-derived.')
    rec('  ### **b226 PUTS EVERY ODD PRIME AT LEVEL 1 AND p = 2 AT LEVEL 2.**')
    rec('  ### ### **SO UNDER THE RULED CHOICE THE ONLY CELL WITH ANY (SPEC-2) CONTENT AT ALL IS')
    rec('  ### ### (2,2) -- THE CELL b273 ALREADY SETTLED. ### THE "GENERALLY" OF THIS ACT IS A')
    rec('  ### ### QUESTION ABOUT CELLS THE AGGREGATION DOES NOT VISIT UNDER b226\'s CHOICE.**')
    rec()

    rec('-' * 100)
    rec('### (5) THE HIGH SIDE, AND THE UNCERTIFIED REGION CHARACTERIZED.')
    rec('-' * 100)
    rec('  ### **CERTIFIED HIGH WITNESS: (2,2), k = 1, by b273\'s g_2 - g_6 at (1+sqrt2)/3.**')
    rec('  ### **NO GENERAL HIGH FAMILY IS DERIVED BY THIS ACT.**')
    rec('  ### THE UNCERTIFIED REGION, CHARACTERIZED RATHER THAN LISTED:')
    rec('    ### **EVERY (p, n >= 2, k) EXCEPT (2,2,1) LACKS A CERTIFIED HIGH WITNESS HERE.**')
    rec('    The obstruction sharpens as act 9\'s term approaches 1: the term at k = 1 is')
    rec('    (q - p)/(q - 1), which tends to 1 as q grows, while the vectors this act can name')
    rec('    exactly do not follow it up. ### **SO THE HARD ROW IS k = 1 AT LARGE n.**')
    rec('  ### ### **THIS IS AN ABSENCE OF CERTIFICATION, NOT A REFUTATION.** ### No cell is')
    rec('  ### claimed to fail the straddle, and `W-ORD-ORDER-CHANNEL` governs: ### **A')
    rec('  ### COMPARISON THE CHANNEL CANNOT CERTIFY IS UNCERTIFIED, NEVER FALSE.**')
    rec()

    io.open(os.path.join(HERE, '..', '..', 'data', 'b274_run.txt'),
            'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print('  written: data/b274_run.txt')
    return 0


if __name__ == '__main__':
    sys.exit(main())
