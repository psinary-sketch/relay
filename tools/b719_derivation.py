# -*- coding: utf-8 -*-
"""b719_derivation.py -- (R329)(7): THE DERIVATION'S REMAINING STEP, from data/b718_derivation.txt :128-:136 (the step named: "that the least
n, over the bad primes of D with their classes, instantiating a minimal negative shape of Cl(K) instantiates one of value -2"), taken
through the class-group characters: a(n) = (1/h) SUM_chi SUM_{N A = n} chi(A), the principal count as the average of the characters'
turns around the class circle, the pair sum written the same way; each step checked against -23, -15, -39, -20 and -47 (the last two
after (6)(ii): data/b719_coeffs.txt) before it is used, a planted error failing as wanted; graded at its end. Writes
data/b719_derivation.txt (route `bank`); `dry` prints and writes nothing.

THE STEPS:
 (1) THE TURNS. For Cl(K) cyclic of order h with generator g, chi_j(g^k) = exp(2 pi i j k / h). A prime ideal above p in the class g^c turns
     the class circle by theta = 2 pi j c / h under chi_j; R_j(n) = SUM_{N A = n} chi_j(A) is multiplicative, with R_j(p^e) =
     sin((e + 1) theta) / sin(theta) (the Chebyshev value U_e(cos theta); e + 1 at theta = 0 mod 2 pi, (-1)^e (e + 1) at theta = pi) for p split,
     chi_j(g^c)^e for p ramified, [e even] for p inert. By orthogonality a(n) = (1/h) SUM_j R_j(n). CHECK: equal to r_Q1(n)/2 at every
     n <= 32532 at the five. PLANT: the class above 2 moved by one step.
 (2) THE PAIR SUM THE SAME WAY. (a*a)(n) = (1/h^2) SUM_{j, k} (R_j * R_k)(n), (R_j * R_k) multiplicative with local factor
     SUM_{i=0}^{e} R_j(p^i) R_k(p^(e-i)); the ordered pair sum is (a*a)(n) - 2 a(n). CHECK: equal to SUM_{d | n} a(d) a(n/d) at every
     n <= 32532 at the five. PLANT: 1/h in place of 1/h^2.
 (3) b AT OMEGA <= 5. On a bad-supported n with Omega(n) <= 5 (data/b718_derivation.txt (ii), :124), b(n) = 2 a(n) - (a*a)(n)/2, so
     b(n) = (1/h) SUM_j 2 R_j(n) - (1/(2 h^2)) SUM_{j, k} (R_j * R_k)(n). CHECK: equal to the exact b (tools/b718_classgroup.py log_coeffs)
     at every bad-supported n <= 32532 with Omega(n) <= 5 at the five. PLANT: the coefficient 1/2 of (a*a) dropped.
 (4) THE VALUE AT THE LEAST INSTANCE. At each discriminant's n0 (48, 24, 120, 36, 168), (1)-(3) evaluated, each prime's turn printed
     per character: a(n0), the pair sum and b(n0) in closed form in h and the classes the shape uses. CHECK: b(n0) = -2 as banked.
     PLANT: the least prime's kind flipped, split <-> ramified, in a and the pair sum alike (a class moved by one step is
     vacuous at -20's n0 = 36, both exponents even in C2: the first run's plant, which did not fail there).
 (5) WHAT THE GROUP FIXES. The census of minimal negative shapes (tools/b718_abstract.py, unedited) at Omega 4 and 5 over C2-C7 and
     C2 x C2, grouped by the exponent pattern: which patterns carry a value other than -2, in each group.
THE GRADE at the end: what (1)-(5) establish, and the step that remains, named.
"""
import cmath
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
import b719_coeffs as CO          # noqa: E402  ### b719's (6)(ii) tool: its counts (b716's enumeration) and forms

CUT = 32532
P = CG.primes_upto(CUT)
FIVE = [(-23, (1, 1, 6), 48, 'data/b711_coeffs.txt :12'), (-15, (1, 1, 4), 24, 'data/b713_coeffs.txt :13'),
        (-39, (1, 1, 10), 120, 'data/b717_coeffs.txt :16'), (-20, (1, 0, 5), 36, 'data/b719_coeffs.txt'),
        (-47, (1, 1, 12), 168, 'data/b719_coeffs.txt')]
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


def run():
    t0 = time.time()
    L = ['b719 -- (R329)(7): THE DERIVATION`S REMAINING STEP THROUGH THE CLASS-GROUP CHARACTERS, EACH STEP CHECKED AT -23, -15, -39, -20, -47 BEFORE USE (%s)' % (
        time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### from data/b718_derivation.txt :128-:136 (the step named) ; the five discriminants` n0 from data/b711_coeffs.txt :12, data/b713_coeffs.txt :13,',
         '### data/b717_coeffs.txt :16 and data/b719_coeffs.txt ; a(n) = r_Q1(n)/2 by enumeration (tools/b716_genus_control.py counts) ; b exact by',
         '### tools/b718_classgroup.py log_coeffs. Each CHECK is printed before its step is used; each PLANT must fail. Characters in floating point,',
         '### every character sum required integral (or a rational with denominator 2) to %g before it is compared.' % TOL, '']
    DS = [(Disc(D, q1), n0, src) for D, q1, n0, src in FIVE]
    allok = True
    # ### (1)
    L += ['## STEP (1): THE TURNS -- a(n) = (1/h) SUM_j R_j(n), R_j(p^e) = sin((e+1) theta)/sin(theta) split, chi^e ramified, [e even] inert']
    for d, _n0, _s in DS:
        miss = [n for n in range(1, CUT + 1) if not isint(d.a_chi(n)) or round(d.a_chi(n)) != d.a[n]]
        pl = [n for n in range(1, 2001) if round(d.a_chi(n, shift={2: 1})) != d.a[n]]
        ok = not miss and bool(pl) and all(d.ok.values())
        allok &= ok
        L += ['  CHECK D = %d (Cl C%d, generator %s): (1/h) SUM_j R_j(n) against r_Q1(n)/2 at every n <= %d: mismatches %d %s ; PLANT the class above 2 moved one step: mismatches %d through 2000 -- %s' % (
            d.D, d.h, d.g, CUT, len(miss), miss[:5], len(pl), 'AS WANTED, FAILS AS WANTED' if ok else '### NOT AS WANTED')]
    # ### (2)
    L += ['', '## STEP (2): THE PAIR SUM THE SAME WAY -- (a*a)(n) = (1/h^2) SUM_{j,k} (R_j * R_k)(n), the ordered pair sum (a*a)(n) - 2 a(n)']
    for d, _n0, _s in DS:
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
    for d, _n0, _s in DS:
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
    for d, n0, src in DS:
        f = d.fac(n0)
        aN, aaN = d.a_chi(n0), d.aa_chi(n0)
        bN = 2 * aN - aaN / 2
        pairN = aaN - 2 * aN
        ok = isint(aN) and isint(aaN) and abs(bN + 2) < TOL and round(aN) == d.a[n0]
        fl = (min(f),)
        bpl = 2 * d.a_chi(n0, flip=fl) - d.aa_chi(n0, flip=fl) / 2
        plok = abs(bpl + 2) > TOL
        allok &= ok and plok
        L += ['  D = %d, h = %d, n0 = %d (%s): ' % (d.D, d.h, n0, src) + ' ; '.join(
            '%d^%d %s g^%s (order %s): R_j = [%s]' % (p, e, d.kind[p][0], d.kind[p][1], d.h // math.gcd(d.kind[p][1], d.h) if d.kind[p][1] is not None else '-',
                                                    ', '.join('%g' % round(complex(d.local(j, p, e)).real, 9) for j in range(d.h))) for p, e in sorted(f.items())),
              '      a(n0) = (1/%d) SUM_j PROD = %s ; (a*a)(n0) = %s ; the pair sum %s ; b(n0) = 2a - (a*a)/2 = %s -- %s ; PLANT the kind of %d flipped (split <-> ramified), in a and the pair sum: b %s -- %s' % (
                  d.h, round(aN, 9), round(aaN, 9), round(pairN, 9), round(bN, 9), 'AS WANTED (-2)' if ok else '### NOT AS WANTED', min(f), round(bpl, 9),
                  'FAILS AS WANTED' if plok else '### DOES NOT FAIL')]
    # ### (5)
    L += ['', '## STEP (5): WHAT THE GROUP FIXES -- the minimal negative shapes at Omega 4 and 5 by exponent pattern (tools/b718_abstract.py), values other than -2 marked']
    odd_narrow, other_somewhere = [], []
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
        if len(orders) == 1 and orders[0] % 2:
            o4 = dict((k[1], v) for k, v in by.items() if k[0] == 4)
            other = dict((k, v) for k, v in o4.items() if v != {'-2'})
            odd_narrow.append(other == {(1, 1, 1, 1): {'-6'}})
            L += ['           odd h: no bad ramified prime (a ramified prime`s class has order <= 2); at Omega 4 the patterns %s ; values other than -2 at %s' % (
                sorted(o4), other or 'NONE')]
        if any(v != {'-2'} for v in by.values()):
            other_somewhere.append(G.name())
    census_ok = len(odd_narrow) == 3 and all(odd_narrow) and len(other_somewhere) == 7
    allok &= census_ok
    L += ['', '### THE CENSUS READ AS THE GRADE STATES IT (values other than -2 in all 7 groups; the odd groups` Omega-4 exception the pattern (1, 1, 1, 1) at -6 alone): %s' % census_ok]
    L += ['', '## THE GRADE',
          '  WRITTEN PROOF, EACH STEP CHECKED AT FIVE DISCRIMINANTS (nothing compiled):',
          '  (1)-(3) are identities: the principal count a(n) is the average over the h characters of the products of each prime`s turn,',
          '  sin((e+1) theta)/sin theta for a split prime whose ideal turns the class circle by theta, chi^e for a ramified one; the pair sum',
          '  is the double average of the products of the local convolutions; and on a bad-supported n with Omega(n) <= 5, b(n) is their',
          '  combination 2a - (a*a)/2. (4) evaluates them at each of the five least instances, b(n0) = -2 at each, in h and the classes used.',
          '  (5) reads the census: in each group listed, minimal negative shapes of value other than -2 exist at Omega 4 or 5; in the odd',
          '  groups C3, C5, C7 at Omega 4 the only such pattern is (1, 1, 1, 1), value -6, four distinct bad primes.',
          '  CLAUSE 1 (b(n0) = -2) IS NOT DERIVED. THE STEP THAT REMAINS, NAMED: the characters give the value of every shape in h and its',
          '  classes, and the value is -2 at some shapes and not at others in every group read; which shape the least bad-supported n',
          '  instantiates is decided by the sizes of the least bad primes in each class (the order of the products p^2 q r, p^3 q, p q r s',
          '  and the rest), a statement on the distribution of primes among the classes -- the splitting of primes in the Hilbert class field --',
          '  and not on h or the orders. Narrowed in the odd groups read (C3, C5, C7) at Omega(n0) = 4: clause 1 fails there only if n0 is a',
          '  product of four distinct bad primes. The law stands REGISTERED, HELD at -23, -15, -39, -20 and -47.', '',
          '### ### **CHECKS 4 STEPS x 5 DISCRIMINANTS: %s ; PLANTS: %s ; THE GRADE: THE CHARACTER FORMS OF a, THE PAIR SUM AND b A WRITTEN PROOF, CHECKED ; CLAUSE 1 NOT DERIVED, ITS STEP NAMED AND NARROWED ; %d s.**' % (
              'ALL AS WANTED' if allok else 'NOT ALL AS WANTED', 'ALL FAIL AS WANTED' if allok else 'NOT ALL', int(time.time() - t0))]
    return L, allok


if __name__ == '__main__':
    route = sys.argv[1] if len(sys.argv) > 1 else 'dry'
    L, ok = run()
    print(NL.join(L))
    if route == 'bank':
        if not ok:
            sys.exit('### NOT ALL AS WANTED -- NOTHING WRITTEN')
        p = os.path.join(D_, 'b719_derivation.txt')
        with open(p + '.tmp', 'wb') as fh:
            fh.write((NL.join(L) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/b719_derivation.txt')
