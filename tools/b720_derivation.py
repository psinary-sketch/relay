# -*- coding: utf-8 -*-
"""b720_derivation.py -- (R330)(4): THE DERIVATION'S -2, from data/b719_derivation.txt :70, with the two configurations the five cases show
(2 split at -23, -15, -39, -47: b(n0) = 4 - 12/2; 2 ramified at -20: b(n0) = 3 - 10/2), the navigator's recomputation reproduced before use,
the step taken so that it accounts for both configurations and, after (3), for -35 and -40; each check printed before its step, a planted
error failing as wanted; graded at its end. Written whole at b720 by the Write tool, after tools/b719_derivation.py (read :1-:269; the
carried copy, data/b720_carry_derivation.txt, replaced whole). Writes data/b720_derivation.txt (route `bank`); `dry` writes nothing.

THE STEPS:
 (0) THE NAVIGATOR'S RECOMPUTATION, REPRODUCED BEFORE USE. At each of the five, from r_Q1(n)/2 by enumeration: a(n0), the ordered pair sum
     SUM_{d | n0, 1 < d < n0} a(d) a(n0/d), and the number of ordered factorizations of n0 into three or more parts each with a != 0.
     WANTED (the navigator's): a = 4 and the pair sum 12 where 2 splits, a = 3 and 10 at -20, no such factorization at any of the five.
     PLANT: the pair sum counted unordered (each pair {d, n0/d} once), wanted to fail.
 (1)-(3) b719's identities, checked again at the seven discriminants (the five and -35, -40): the turns, the pair sum by characters, and
     b = 2a - (a*a)/2 = a - (pair sum)/2 on the bad-supported n with Omega <= 5; each with b719's plant.
 (4) THE VALUE AT THE LEAST INSTANCE at the seven, each prime's turn per character; CHECK: b(n0) as banked (data/b711_coeffs.txt :12,
     data/b713_coeffs.txt :13, data/b717_coeffs.txt :16, data/b719_coeffs.txt, data/b720_coeffs.txt). PLANT: the least prime's kind flipped.
 (5) WHAT THE GROUP FIXES: b719's census of minimal negative shapes at Omega 4 and 5 over C2-C7 and C2 x C2, re-run unedited.
 (6) THE STEP TAKEN, IN C2 AT OMEGA 4, IN CLOSED FORM. With every prime of n non-principal (its ideals in the class g of order 2), an ideal
     of norm n lies in the class (Omega(n) mod 2) g, so a(n) = tau_s(n) [Omega(n) even], tau_s(n) = PROD over n's split primes of (e + 1).
     At Omega(n) = 4 a factorization into three or more parts each with a != 0 needs parts of even Omega >= 2, Omega >= 6 in all: there is
     none, so b(n) = a(n) - P(n)/2 with P(n) = SUM over the divisors d of Omega 2 of tau_s(d) tau_s(n/d). Every exponent pattern and kind
     at Omega 4 tabled; CHECK: the closed form equal to b718's group-ring model (tools/b718_abstract.py b_lattice) at every row, and
     minimality read from the same model. PLANT: tau counting a ramified prime as (e + 1), wanted to fail.
 (7) THE INSTANCES READ BY THE TABLE: the shape and closed-form value of n0 at the five C2-or-split cases and at -35 and -40, and at the two
     C2 discriminants of the act the least instance of each negative Omega-4 shape over D's least bad primes of each kind, beside the
     computed n0.
THE GRADE at the end.
"""
import cmath
import itertools
import math
import os
import sys
import time
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D_ = os.path.join(ROOT, 'data')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b718_classgroup as CG      # noqa: E402  ### b718's, unedited
import b718_abstract as AB        # noqa: E402  ### b718's, unedited
import b720_coeffs as CO          # noqa: E402  ### this act's (3) tool: its counts (b716's enumeration)

CUT = 32532
P = CG.primes_upto(CUT)
SEVEN = [(-23, (1, 1, 6), 48, '-2', 'data/b711_coeffs.txt :12'), (-15, (1, 1, 4), 24, '-2', 'data/b713_coeffs.txt :13'),
         (-39, (1, 1, 10), 120, '-2', 'data/b717_coeffs.txt :16'), (-20, (1, 0, 5), 36, '-2', 'data/b719_coeffs.txt :16'),
         (-47, (1, 1, 12), 168, '-2', 'data/b719_coeffs.txt :24'), (-35, (1, 1, 9), 135, '-2', 'data/b720_coeffs.txt'),
         (-40, (1, 0, 10), 100, '-1/2', 'data/b720_coeffs.txt')]
FIVE_D = (-23, -15, -39, -20, -47)
NAV = {-23: (4, 12), -15: (4, 12), -39: (4, 12), -47: (4, 12), -20: (3, 10)}   # ### the navigator's a(n0) and ordered pair sum
TOL = 1e-7


class Disc:
    def __init__(self, D, q1):
        self.D, self.q1 = D, q1
        F, e, T, ok = CG.group(D)
        self.h, self.e, self.T, self.ok = len(F), e, T, ok
        gen = [x for x in F if CG.order(x, e, T) == self.h]
        if not gen:
            sys.exit('### Cl(%d) NOT CYCLIC' % D)
        self.g = gen[0]
        self._cache = {}
        self.log, y = {e: 0}, e
        for k in range(1, self.h):
            y = T[(y, self.g)]
            self.log[y] = k
        self.kind = {}
        for p in P:
            t, f = CG.prime_class(D, p)
            self.kind[p] = (t, None if f is None else self.log[f])
        self.r1 = CO.counts(q1, D, CUT)
        self.a = [0] + [self.r1[n] // 2 for n in range(1, CUT + 1)]
        self.a[1] = 1
        self.spf = list(range(CUT + 1))
        for p in P:
            if p * p > CUT:
                break
            for m in range(p * p, CUT + 1, p):
                if self.spf[m] == m:
                    self.spf[m] = p

    def fac(self, n):
        out = {}
        while n > 1:
            p = self.spf[n]
            out[p] = out.get(p, 0) + 1
            n //= p
        return out

    def local(self, j, p, e, shift=None, flip=()):
        t, c = self.kind[p]
        if shift and p in shift:
            c = (c + shift[p]) % self.h
        if p in flip and t != 'inert':
            t = 'ram' if t == 'split' else 'split'
        key = (j, t, c, e)
        if key in self._cache:
            return self._cache[key]
        if t == 'inert':
            v = complex(1.0 if e % 2 == 0 else 0.0)
        elif t == 'ram':
            v = cmath.exp(2j * math.pi * j * c / self.h) ** e
        else:
            th = 2 * math.pi * j * c / self.h
            if abs(math.sin(th)) < 1e-12:
                v = complex((e + 1) * (math.cos(th) ** e))     # ### theta = 0 or pi: U_e(+-1) = (+-1)^e (e + 1)
            else:
                v = complex(math.sin((e + 1) * th) / math.sin(th))
        self._cache[key] = v
        return v

    def R(self, j, n, shift=None, flip=()):
        v = 1 + 0j
        for p, e in self.fac(n).items():
            v *= self.local(j, p, e, shift, flip)
        return v

    def a_chi(self, n, shift=None, flip=()):
        return sum(self.R(j, n, shift, flip) for j in range(self.h)).real / self.h

    def aa_chi(self, n, inv=None, flip=()):
        h = self.h
        f = self.fac(n)
        tot = 0j
        for j in range(h):
            for k in range(h):
                v = 1 + 0j
                for p, e in f.items():
                    v *= sum(self.local(j, p, i, None, flip) * self.local(k, p, e - i, None, flip) for i in range(e + 1))
                tot += v
        return (tot / (inv if inv else h * h)).real


def isint(x):
    return abs(x - round(x)) < TOL


# ================================================================================ (6): C2 AT OMEGA 4 IN CLOSED FORM
def tau_s(kinds, e, plant=False):
    v = 1
    for t, x in zip(kinds, e):
        if t == 'split' or plant:
            v *= x + 1
    return v


def closed_b(kinds, k, plant=False):
    """(a, P, b) at the exponent vector k over primes of the given kinds, every prime non-principal in C2: a = tau_s [Omega even],
    P = SUM over the Omega-2 divisors d of tau_s(d) tau_s(k - d), b = a - P/2 (no factorization into three or more nonzero parts at
    Omega 4)."""
    Om = sum(k)
    a = tau_s(kinds, k, plant) if Om % 2 == 0 else 0
    Psum = 0
    for d in itertools.product(*[range(x + 1) for x in k]):
        if sum(d) == 2:
            Psum += tau_s(kinds, d, plant) * tau_s(kinds, tuple(x - y for x, y in zip(k, d)), plant)
    return a, Psum, Fraction(a) - Fraction(Psum, 2)


def omega4_table():
    """every Omega-4 exponent pattern over r distinct primes, each split or ramified, up to the order of equal exponents."""
    rows = []
    for k in [(4,), (3, 1), (2, 2), (2, 1, 1), (1, 1, 1, 1)]:
        for kinds in itertools.product(('split', 'ram'), repeat=len(k)):
            key = sorted(zip(k, kinds), key=lambda x: (-x[0], x[1]))
            if list(zip(k, kinds)) != key:
                continue
            rows.append((k, kinds))
    return rows


def shape_name(k, kinds):
    return ' . '.join('%s%s' % ('S' if t == 'split' else 'R', ('^%d' % x) if x > 1 else '') for x, t in zip(k, kinds))


def run():
    t0 = time.time()
    L = ['b720 -- (R330)(4): THE DERIVATION`S -2 WITH BOTH CONFIGURATIONS, THE NAVIGATOR`S RECOMPUTATION REPRODUCED BEFORE USE, THE STEP EXTENDED TO -35 AND -40 (%s)' % (
        time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### from data/b719_derivation.txt :70 (the grade) and (R330)(4) ; the seven discriminants` n0 from data/b711_coeffs.txt :12, data/b713_coeffs.txt :13,',
         '### data/b717_coeffs.txt :16, data/b719_coeffs.txt and data/b720_coeffs.txt ; a(n) = r_Q1(n)/2 by enumeration (tools/b716_genus_control.py counts) ;',
         '### b exact by tools/b718_classgroup.py log_coeffs. Each CHECK is printed before its step is used; each PLANT must fail. Characters in floating',
         '### point, every character sum required integral (or a rational with denominator 2) to %g before it is compared.' % TOL, '']
    DS = [(Disc(D, q1), n0, bw, src) for D, q1, n0, bw, src in SEVEN]
    allok = True
    # ### (0)
    L += ['## STEP (0): THE NAVIGATOR`S RECOMPUTATION, REPRODUCED BEFORE USE -- a(n0), the ordered pair sum, factorizations into three or more nonzero parts']
    for d, n0, _bw, src in DS:
        if d.D not in FIVE_D:
            continue
        a0 = d.a[n0]
        pair = CG.pair_sum(d.a, n0)
        k3 = CG.ordered_factorizations(d.a, n0)
        unord = sum(d.a[x] * d.a[n0 // x] for x in range(2, n0) if n0 % x == 0 and x <= n0 // x)
        wa, wp = NAV[d.D]
        ok = a0 == wa and pair == wp and k3 == 0
        plok = unord != wp
        allok &= ok and plok
        L += ['  CHECK D = %d, n0 = %d (%s): a(n0) %d, the ordered pair sum %d, three-or-more-part factorizations %d (the navigator`s %d, %d, 0) ; b = a - pair/2 = %s -- %s ; PLANT the pair sum unordered: %d -- %s' % (
            d.D, n0, src, a0, pair, k3, wa, wp, Fraction(a0) - Fraction(pair, 2), 'REPRODUCED' if ok else '### NOT REPRODUCED', unord,
            'FAILS AS WANTED' if plok else '### DOES NOT FAIL')]
    # ### (1)
    L += ['', '## STEP (1): THE TURNS -- a(n) = (1/h) SUM_j R_j(n), R_j(p^e) = sin((e+1) theta)/sin(theta) split, chi^e ramified, [e even] inert']
    for d, _n0, _bw, _s in DS:
        miss = [n for n in range(1, CUT + 1) if not isint(d.a_chi(n)) or round(d.a_chi(n)) != d.a[n]]
        # ### the plant moves the class above the least prime that has one (b719's: 2; at -35 the prime 2 is inert and carries none, so 3)
        pp = min(p for p in P if d.kind[p][1] is not None)
        pl = [n for n in range(1, 2001) if round(d.a_chi(n, shift={pp: 1})) != d.a[n]]
        ok = not miss and bool(pl) and all(d.ok.values())
        allok &= ok
        L += ['  CHECK D = %d (Cl C%d, generator %s): (1/h) SUM_j R_j(n) against r_Q1(n)/2 at every n <= %d: mismatches %d %s ; PLANT the class above %d moved one step: mismatches %d through 2000 -- %s' % (
            d.D, d.h, d.g, CUT, len(miss), miss[:5], pp, len(pl), 'AS WANTED, FAILS AS WANTED' if ok else '### NOT AS WANTED')]
    # ### (2)
    L += ['', '## STEP (2): THE PAIR SUM THE SAME WAY -- (a*a)(n) = (1/h^2) SUM_{j,k} (R_j * R_k)(n), the ordered pair sum (a*a)(n) - 2 a(n)']
    for d, _n0, _bw, _s in DS:
        conv = [0] * (CUT + 1)
        nz = [k for k in range(1, CUT + 1) if d.a[k]]
        for x in nz:
            for y in nz:
                if x * y > CUT:
                    break
                conv[x * y] += d.a[x] * d.a[y]
        miss = []
        for n in range(1, CUT + 1):
            v = d.aa_chi(n)
            if not isint(v) or round(v) != conv[n]:
                miss.append(n)
        pl = [n for n in range(2, 2001) if conv[n] and round(d.aa_chi(n, inv=d.h)) != conv[n]]
        ok = not miss and bool(pl)
        allok &= ok
        L += ['  CHECK D = %d: the character form of (a*a)(n) against SUM_{d|n} a(d) a(n/d) at every n <= %d: mismatches %d %s ; PLANT 1/h for 1/h^2: mismatches %d through 2000 -- %s' % (
            d.D, CUT, len(miss), miss[:5], len(pl), 'AS WANTED, FAILS AS WANTED' if ok else '### NOT AS WANTED')]
    # ### (3)
    L += ['', '## STEP (3): b AT OMEGA <= 5 ON THE BAD-SUPPORTED n -- b(n) = (1/h) SUM_j 2 R_j(n) - (1/(2 h^2)) SUM_{j,k} (R_j * R_k)(n)']
    for d, _n0, _bw, _s in DS:
        bex, Om = CG.log_coeffs(d.a, CUT, P)
        bad = set(p for p, (t, c) in d.kind.items() if t != 'inert' and c != 0)
        pts = [n for n in range(2, CUT + 1) if Om[n] <= 5 and all(p in bad for p in d.fac(n))]
        miss, pl = [], 0
        for n in pts:
            v = 2 * d.a_chi(n) - d.aa_chi(n) / 2
            if abs(v - float(bex[n])) > TOL:
                miss.append(n)
            if abs((2 * d.a_chi(n) - d.aa_chi(n)) - float(bex[n])) > TOL:
                pl += 1
        ok = not miss and pl > 0
        allok &= ok
        L += ['  CHECK D = %d: at the %d bad-supported n <= %d with Omega <= 5, the character form of b against the exact b: mismatches %d %s ; PLANT the 1/2 dropped: mismatches %d -- %s' % (
            d.D, len(pts), CUT, len(miss), miss[:5], pl, 'AS WANTED, FAILS AS WANTED' if ok else '### NOT AS WANTED')]
    # ### (4)
    L += ['', '## STEP (4): THE VALUE AT THE LEAST INSTANCE, IN h AND THE CLASSES THE SHAPE USES (each prime p^e: kind, class g^c, its order, and R_j(p^e) for j = 0..h-1)']
    for d, n0, bw, src in DS:
        f = d.fac(n0)
        aN, aaN = d.a_chi(n0), d.aa_chi(n0)
        bN = 2 * aN - aaN / 2
        pairN = aaN - 2 * aN
        ok = isint(aN) and isint(aaN) and abs(bN - float(Fraction(bw))) < TOL and round(aN) == d.a[n0]
        fl = (min(f),)
        bpl = 2 * d.a_chi(n0, flip=fl) - d.aa_chi(n0, flip=fl) / 2
        plok = abs(bpl - float(Fraction(bw))) > TOL
        allok &= ok and plok
        L += ['  D = %d, h = %d, n0 = %d (%s): ' % (d.D, d.h, n0, src) + ' ; '.join(
            '%d^%d %s g^%s (order %s): R_j = [%s]' % (p, e, d.kind[p][0], d.kind[p][1], d.h // math.gcd(d.kind[p][1], d.h) if d.kind[p][1] is not None else '-',
                                                    ', '.join('%g' % round(complex(d.local(j, p, e)).real, 9) for j in range(d.h))) for p, e in sorted(f.items())),
              '      a(n0) = (1/%d) SUM_j PROD = %s ; (a*a)(n0) = %s ; the pair sum %s ; b(n0) = 2a - (a*a)/2 = a - pair/2 = %s -- %s ; PLANT the kind of %d flipped (split <-> ramified), in a and the pair sum: b %s -- %s' % (
                  d.h, round(aN, 9), round(aaN, 9), round(pairN, 9), round(bN, 9), ('AS WANTED (%s)' % bw) if ok else '### NOT AS WANTED', min(f), round(bpl, 9),
                  'FAILS AS WANTED' if plok else '### DOES NOT FAIL')]
    # ### (5)
    L += ['', '## STEP (5): WHAT THE GROUP FIXES -- the minimal negative shapes at Omega 4 and 5 by exponent pattern (tools/b718_abstract.py), b719`s census re-run']
    other_somewhere = []
    for orders in [(2,), (3,), (4,), (5,), (6,), (7,), (2, 2)]:
        G = AB.Group(orders)
        by = {}
        for Om in (4, 5):
            for primes, k in AB.configs(G, Om):
                a, b = AB.b_lattice(G, primes, k)
                if b[k] < 0 and not any(b[x] < 0 for x in b if x != k):
                    key = (Om, tuple(sorted(k, reverse=True)))
                    by.setdefault(key, set()).add(str(b[k]))
        L += ['  %-8s ' % G.name() + ' ; '.join('Omega %d %s: %s' % (key[0], key[1], ', '.join(sorted(v, key=lambda s: Fraction(s)))) for key, v in sorted(by.items()))]
        if any(v != {'-2'} for v in by.values()):
            other_somewhere.append(G.name())
    census_ok = len(other_somewhere) == 7
    allok &= census_ok
    L += ['  values other than -2 in all seven groups, as b719 read: %s' % census_ok]
    # ### (6)
    L += ['', '## STEP (6): THE STEP TAKEN -- C2 AT OMEGA 4 IN CLOSED FORM: a = tau_s(n) [Omega even] ; P = SUM_{d | n, Omega(d) = 2} tau_s(d) tau_s(n/d) ; b = a - P/2',
          '  (every prime non-principal, its ideals in the class g of order 2; no factorization into three or more parts with a != 0 at Omega 4: each part needs even Omega >= 2)']
    G2 = AB.Group((2,))
    tab, miss6, plant6 = [], [], 0
    for k, kinds in omega4_table():
        primes = [(t, (1,)) for t in kinds]
        am, bm = AB.b_lattice(G2, primes, k)
        a_, P_, b_ = closed_b(kinds, k)
        minimal = bm[k] < 0 and not any(bm[x] < 0 for x in bm if x != k)
        if am[k] != a_ or bm[k] != b_ or AB.pair_sum(am, k) != P_:
            miss6.append(shape_name(k, kinds))
        if closed_b(kinds, k, plant=True)[2] != bm[k]:
            plant6 += 1
        tab.append((shape_name(k, kinds), a_, P_, b_, minimal))
    ok6 = not miss6 and plant6 > 0
    allok &= ok6
    L += ['  CHECK: the closed form against the group-ring model (tools/b718_abstract.py b_lattice, pair_sum) at all %d rows: mismatches %d %s ; PLANT tau counting a ramified prime as (e + 1): mismatches %d -- %s' % (
        len(tab), len(miss6), miss6, plant6, 'AS WANTED, FAILS AS WANTED' if ok6 else '### NOT AS WANTED')]
    for nm, a_, P_, b_, mn in tab:
        L += ['    %-22s a %2d ; P %3d ; b = %d - %d/2 = %-5s %s' % (nm, a_, P_, a_, P_, b_, ('MINIMAL NEGATIVE' if mn else ('negative, not minimal' if b_ < 0 else '')))]
    vals = dict((nm, b_) for nm, _a, _P, b_, mn in tab)
    neg2 = sorted(nm for nm, _a, _P, b_, mn in tab if mn and b_ == -2)
    other = sorted('%s (%s)' % (nm, b_) for nm, _a, _P, b_, mn in tab if mn and b_ != -2)
    L += ['  THE MINIMAL NEGATIVE SHAPES OF VALUE -2: %s ; OF ANOTHER VALUE: %s' % (', '.join(neg2), ', '.join(other))]
    both_ok = vals.get('S^3 . R') == -2 and vals.get('R^2 . S^2') == -2 and vals.get('R^2 . R^2') == Fraction(-1, 2)
    allok &= both_ok
    L += ['  THE TWO CONFIGURATIONS IN C2: S^3 . R (2 split, -15`s 2^3 . 3): a = 4, P = 12, b = 4 - 12/2 = -2 ; R^2 . S^2 (2 ramified, -20`s 2^2 . 3^2): a = 3,',
          '  P = 10, b = 3 - 10/2 = -2 ; AND THE THIRD, R^2 . R^2 (two ramified primes): a = 1, P = 3, b = 1 - 3/2 = -1/2 -- READ FROM THE TABLE: %s' % both_ok]
    minimal_rows = [(k, kinds, b_) for (k, kinds), (_nm, _a, _P, b_, mn) in zip(omega4_table(), tab) if mn]
    # ### (7)
    L += ['', '## STEP (7): THE INSTANCES READ BY THE TABLE']
    for d, n0, bw, _src in DS:
        if d.h != 2:
            continue
        f = sorted(d.fac(n0).items(), key=lambda x: (-x[1], x[0]))
        kinds = tuple(d.kind[p][0] for p, _e in f)
        k = tuple(e for _p, e in f)
        key = sorted(zip(k, kinds), key=lambda x: (-x[0], x[1]))
        nm = shape_name(tuple(x for x, _t in key), tuple(t for _x, t in key))
        L += ['  D = %d (C2): n0 = %d = %s, the shape %s, the table`s value %s, banked %s -- %s' % (
            d.D, n0, ' . '.join('%d^%d' % pe for pe in f), nm, vals.get(nm), bw, 'EQUAL' if str(vals.get(nm)) == bw else '### NOT EQUAL')]
        allok &= str(vals.get(nm)) == bw
        if d.D in (-35, -40):
            badp = [p for p in P if p < 200 and d.kind[p][0] != 'inert' and d.kind[p][1] != 0]
            S = [p for p in badp if d.kind[p][0] == 'split'][:4]
            Rr = [p for p in badp if d.kind[p][0] == 'ram'][:4]
            cand = []
            for k_, kinds_, b_ in minimal_rows:
                best = None
                pools = [S if t == 'split' else Rr for t in kinds_]
                for choice in itertools.product(*pools):
                    if len(set(choice)) < len(choice):
                        continue
                    v = 1
                    for p_, x_ in zip(choice, k_):
                        v *= p_ ** x_
                    best = v if best is None or v < best else best
                if best is not None:
                    cand.append((shape_name(k_, kinds_), best, b_))
            cand.sort(key=lambda x: x[1])
            allok &= bool(cand) and cand[0][1] == n0 and str(cand[0][2]) == bw
            L += ['      the least bad primes: split %s, ramified %s (D`s ramified primes are its divisors alone) ; the least instance of each minimal negative Omega-4 shape: %s ;'
                  ' THE LEAST %s = %d (b %s), the computed n0 %d -- %s' % (
                      S, Rr, ' ; '.join('%s %d (b %s)' % c_ for c_ in cand), cand[0][0], cand[0][1], cand[0][2], n0,
                      'EQUAL' if cand[0][1] == n0 else '### NOT EQUAL')]
    L += ['', '## THE GRADE',
          '  (0) the navigator`s recomputation reproduced at the five: a(n0) = 4 and the pair sum 12 where 2 splits, 3 and 10 at -20, no factorization',
          '  into three or more nonzero parts at any. (1)-(3) b719`s identities, checked again at seven discriminants. (4) b(n0) evaluated at the seven:',
          '  -2 at six, -1/2 at -40.',
          '  THEOREM, WITH ITS HYPOTHESES (a written proof, each step checked; nothing compiled): in Cl(K) = C2, at a bad-supported n with Omega(n) = 4',
          '  and every prime of n non-principal, a(n) = tau_s(n) and b(n) = a(n) - P(n)/2 in closed form (step (6), the table of %d rows equal to the' % len(tab),
          '  group-ring model). Of its minimal negative shapes, those of value -2 are %s; the others %s.' % (', '.join(neg2), ', '.join(other)),
          '  The two configurations are rows of the table -- S^3 . R, 4 - 12/2, and R^2 . S^2, 3 - 10/2 -- so the derivation`s -2 holds for both as a',
          '  theorem in C2 at Omega 4; and the same table gives -40`s value: R^2 . R^2, 1 - 3/2 = -1/2. At -40 the ramified primes are 2 and 5 alone, the',
          '  least split bad prime 7, and 2^2 . 5^2 = 100 is the least instance of any minimal negative Omega-4 shape (step (7)); at -35 it is 3^3 . 5 = 135.',
          '  At -23 (C3), -39 (C4) and -47 (C5), where 2 splits at Omega 5, the values a = 4, P = 12 are evaluated at the instances (step (4)), not',
          '  derived as a table: THE STEP THAT REMAINS THERE, NAMED -- the closed form of a and P over a cyclic group of order h > 2 at the shapes',
          '  p^4 q, p^3 q r (the turns of step (1) give them; the table is not written).',
          '  CLAUSE 1 (b(n0) = -2) IS REFUTED AT -40 (data/b720_coeffs.txt) and is not a theorem: which shape n0 instantiates is decided by the sizes of',
          '  the least bad primes of each kind; in C2 with Omega(n0) = 4, b(n0) = -2 exactly when n0`s shape is one of the %d rows of value -2 above.' % len(neg2),
          '  Clause 2 holds at the seven.', '',
          '### ### **CHECKS 5 STEPS x 7 DISCRIMINANTS AND THE C2 TABLE: %s ; PLANTS: %s ; THE GRADE: THE -2 OF BOTH CONFIGURATIONS A THEOREM IN C2 AT OMEGA 4 WITH '
          'ITS HYPOTHESES, -40`S -1/2 FROM THE SAME TABLE ; CLAUSE 1 REFUTED AT -40 ; THE STEP THAT REMAINS AT h > 2 NAMED ; %d s.**' % (
              'ALL AS WANTED' if allok else 'NOT ALL AS WANTED', 'ALL FAIL AS WANTED' if allok else 'NOT ALL', int(time.time() - t0))]
    return L, allok


if __name__ == '__main__':
    route = sys.argv[1] if len(sys.argv) > 1 else 'dry'
    L, ok = run()
    print(NL.join(L))
    if route == 'bank':
        if not ok:
            sys.exit('### NOT ALL AS WANTED -- NOTHING WRITTEN')
        p = os.path.join(D_, 'b720_derivation.txt')
        with open(p + '.tmp', 'wb') as fh:
            fh.write((NL.join(L) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/b720_derivation.txt')
