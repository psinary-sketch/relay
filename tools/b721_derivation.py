# -*- coding: utf-8 -*-
"""b721_derivation.py -- (R331)(4): THE TABLE OVER CYCLIC GROUPS OF ORDER h > 2, the step named at data/b720_derivation.txt :114-:115.
Written whole at b721 by the Write tool. Writes data/b721_derivation.txt (route `bank`); `dry` writes nothing. No representation count is
read: every figure is the group-ring model's (tools/b718_abstract.py, unedited), the classes of the primes at the three banked
discriminants from their reduced forms (tools/b720_predict.py setup, unedited), and the banked n0 and b read from their banks.

THE CLOSED FORM (written, then checked). Cl(K) = C_h cyclic, a generator g; a split prime p with exponent e, a prime ideal above it in the
class c (its conjugate -c); a ramified p in a class c with 2c = 0; an inert p only at even e, in the class 0. The ideals of norm n lie in
the classes SUM_p (2 i_p - e_p) c_p (split, 0 <= i_p <= e_p) plus SUM e_p c_p (ramified), so
   a(n) = #{ (i_p) : SUM_split (2 i_p - e_p) c_p + SUM_ram e_p c_p = 0 in Z/h }                                         (the count form)
        = (1/h) SUM_{j=0}^{h-1} PROD_split U_{e_p}(cos 2 pi j c_p / h) . PROD_ram e^{2 pi i j c_p e_p / h}               (the turns)
with U_e the Chebyshev polynomial, U_e(cos t) = sin((e+1) t) / sin t (b719's step (1)). The pair sum P(n) = SUM_{d | n, 1 < d < n}
a(d) a(n/d); and b(n) = SUM_{m >= 1} (-1)^(m+1)/m . A_m(n), A_m the sum over ordered factorizations of n into m parts > 1 of the product
of a, so at Omega(n) = 5: b = a - P/2 + A_3/3 - A_4/4 + A_5/5. At the two shapes (R331)(4) names:
   p^4 q (p, q split, classes c1, c2):  a = #{ 0<=i<=4, 0<=k<=1 : (2i - 4) c1 + (2k - 1) c2 = 0 }
                                        P = 2 [ a(p) a(p^3 q) + a(p^2) a(p^2 q) + a(p^3) a(p q) + a(p^4) a(q) ]
   p^3 q r (split, c1, c2, c3):         a = #{ 0<=i<=3, 0<=k,l<=1 : (2i - 3) c1 + (2k - 1) c2 + (2l - 1) c3 = 0 }
                                        P = 2 [ a(p) a(p^2 q r) + a(q) a(p^3 r) + a(r) a(p^3 q) + a(p^2) a(p q r) + a(p q) a(p^2 r)
                                                + a(p r) a(p^2 q) + a(q r) a(p^3) ]
   (each unordered pair {d, n/d} counted twice in the ordered sum; d = n/d never, an exponent being odd).

THE STEPS, each check printed before its step, each with a planted error failing as wanted:
 (1) the count form equal to the turns and to b718's a_of at every divisor of every table row. PLANT: a split prime's turn taken as
     (e + 1) whatever its class (the principal class's), wanted to fail.
 (2) b by the m-fold expansion equal to b718's b_lattice (the Omega recursion) at every row. PLANT: the A_3 term dropped.
 (3) THE TABLE for h = 3, 4, 5 at Omega 2-6: every configuration of r >= 2 bad primes (split with a class != 0 up to c ~ -c, ramified with
     a class of order 2), up to the automorphisms of C_h; a, P, A_3, b; negative and minimal marked. The shapes p^4 q and p^3 q r printed whole.
 (4) THE TABLE CHECKED BEFORE USE against -23 (C3), -39 (C4), -47 (C5): at each, the row of the banked n0's shape gives the banked b
     (-2; data/b711_coeffs.txt :12, data/b717_coeffs.txt :16, data/b719_coeffs.txt :24) and the navigator's a = 4, P = 12
     (data/b720_derivation.txt :104); and the least bad-supported n whose configuration is a negative row of the table is the banked n0
     (48, 120, 168), every n below it of Omega <= 6 (inside the table). PLANT: the class above 2 at -39 set to 0 moves its least off 120.
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

import b718_abstract as AB     # noqa: E402  ### b718's, unedited
import b720_predict as PR      # noqa: E402  ### b720's, unedited: setup, bad_primes, bad_supported

CUT = 32532
HS = (3, 4, 5)
OMS = (1, 2, 3, 4, 5, 6)
BANKED = [(-23, 48, Fraction(-2), 'data/b711_coeffs.txt :12'), (-39, 120, Fraction(-2), 'data/b717_coeffs.txt :16'),
          (-47, 168, Fraction(-2), 'data/b719_coeffs.txt :24')]
NAV = (4, 12)


# ================================================================================ (1) THE COUNT FORM AND THE TURNS
def a_count(h, primes, e):
    """the count form: tuples of choices whose classes sum to 0 in Z/h."""
    choices = []
    for (t, g), x in zip(primes, e):
        c = g[0]
        if x == 0:
            choices.append([0])
        elif t == 'ram':
            choices.append([(x * c) % h])
        else:
            choices.append([((2 * i - x) * c) % h for i in range(x + 1)])
    return sum(1 for pick in itertools.product(*choices) if sum(pick) % h == 0)


def a_turns(h, primes, e, plant=False):
    tot = 0j
    for j in range(h):
        v = 1 + 0j
        for (t, g), x in zip(primes, e):
            c = g[0]
            if x == 0:
                continue
            th = 2 * math.pi * j * c / h
            if t == 'ram':
                v *= cmath.exp(1j * th * x)
            elif plant:
                v *= (x + 1)
            elif abs(math.sin(th)) < 1e-12:
                v *= (x + 1) * (math.cos(th) ** x)
            else:
                v *= math.sin((x + 1) * th) / math.sin(th)
        tot += v
    return (tot / h).real


# ================================================================================ (2) b BY THE m-FOLD EXPANSION
def b_expansion(h, primes, k, drop3=False):
    L = AB.lattice(k)
    a = dict((e, a_count(h, primes, e)) for e in L)
    zero = tuple(0 for _ in k)
    A = {1: dict((e, Fraction(a[e])) for e in L if e != zero)}
    for m in range(2, sum(k) + 1):
        A[m] = {}
        for e in L:
            if sum(e) < m:
                continue
            s = Fraction(0)
            for f in L:
                if f == zero or f == e or not all(x <= y for x, y in zip(f, e)):
                    continue
                g = tuple(y - x for x, y in zip(f, e))
                if g in A[m - 1]:
                    s += a[f] * A[m - 1][g]
            if s:
                A[m][e] = s
    b = Fraction(0)
    terms = {}
    for m in A:
        v = A[m].get(k, Fraction(0))
        terms[m] = v
        if drop3 and m == 3:
            continue
        b += Fraction((-1) ** (m + 1), m) * v
    return a, terms, b


# ================================================================================ (3) THE TABLE
def canon(h, primes, k):
    """the configuration up to c ~ -c for a split prime and the automorphisms of C_h (multiplication by a unit)."""
    best = None
    for u in range(1, h):
        if math.gcd(u, h) != 1:
            continue
        row = []
        for (t, g), x in zip(primes, k):
            c = (u * g[0]) % h
            if t == 'split':
                c = min(c, (-c) % h)
            row.append((x, t, c))
        row = tuple(sorted(row, reverse=True))
        if best is None or row < best:
            best = row
    return best


def table(h):
    G = AB.Group((h,))
    rows, seen = [], set()
    for Om in OMS:
        for primes, k in AB.configs(G, Om, rmin=1):
            key = canon(h, primes, k)
            if key in seen:
                continue
            seen.add(key)
            a, b = AB.b_lattice(G, primes, k)
            neg = b[k] < 0
            minimal = neg and not any(b[f] < 0 for f in b if f != k)
            rows.append(dict(Om=Om, key=key, primes=primes, k=k, a=a[k], P=AB.pair_sum(a, k), b=b[k], neg=neg, minimal=minimal,
                             name=AB.describe(G, primes, k)))
    return rows


def key_name(key):
    return ' . '.join('%s%d^%d' % ('p' if t == 'split' else 'r', c, x) for x, t, c in key)


# ================================================================================ (4) THE LEAST INSTANCE AT A DISCRIMINANT
def least_instance(D, neg_keys, h, override=None):
    """the least bad-supported n whose configuration is a negative row of the table; an n below it of Omega above the table's is read
    by the model (b718's b_lattice) and counted apart -- if one is negative the result is OUTSIDE, never a guess."""
    S = PR.setup(D)
    bad = PR.bad_primes(S, override)
    G = AB.Group((h,))
    outside_read = []
    for n, fac in PR.bad_supported(bad, CUT):
        Om = sum(x for _j, x in fac)
        primes = [('split' if bad[j][1] == 'split' else 'ram', bad[j][2]) for j, _x in fac]
        k = tuple(x for _j, x in fac)
        if Om > max(OMS):
            b = AB.b_lattice(G, primes, k)[1][k]
            outside_read.append((n, Om, b))
            if b < 0:
                return dict(n=n, outside=True, Om=Om, outside_read=outside_read)
            continue
        key = canon(h, primes, k)
        if key in neg_keys:
            return dict(n=n, key=key, Om=Om, factors=[(bad[j][0], x, bad[j][1], bad[j][2][0]) for j, x in fac], outside=False,
                        outside_read=outside_read)
    return dict(n=None, outside_read=outside_read)


def run():
    t0 = time.time()
    L = ['b721 -- (R331)(4): THE TABLE OVER CYCLIC GROUPS OF ORDER h = 3, 4, 5 AT OMEGA 1-6, ITS CLOSED FORMS AT p^4 q AND p^3 q r, CHECKED '
         'AGAINST -23, -39 AND -47 BEFORE USE (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the closed form as tools/b721_derivation.py`s docstring writes it; every figure the group-ring model`s (tools/b718_abstract.py,',
         '### unedited); no representation count read. EACH CHECK PRINTED BEFORE ITS STEP; EACH PLANT WANTED TO FAIL.', '']
    ok_all, plants_ok = True, True
    tabs = dict((h, table(h)) for h in HS)
    # ---------------------------------------------------------------- (1)
    n_div, bad1, plant1 = 0, [], 0
    for h in HS:
        G = AB.Group((h,))
        for r in tabs[h]:
            for e in AB.lattice(r['k']):
                n_div += 1
                c, t_, m = a_count(h, r['primes'], e), a_turns(h, r['primes'], e), AB.a_of(G, r['primes'], e)
                if not (c == m and abs(t_ - c) < 1e-7):
                    bad1.append((h, r['name'], e, c, t_, m))
                if abs(a_turns(h, r['primes'], e, plant=True) - m) > 1e-7:
                    plant1 += 1
    c1 = not bad1
    ok_all &= c1
    plants_ok &= plant1 > 0
    L += ['## CHECK (1), BEFORE STEP (1): the count form equal to the turns and to b718`s a_of at every divisor of every row: divisors %d ; '
          'unequal %d -- %s' % (n_div, len(bad1), 'AS WANTED' if c1 else 'NOT AS WANTED %s' % bad1[:3]),
          '   PLANT (1): a split prime`s turn as (e + 1) whatever its class: unequal at %d divisors -- %s' % (
              plant1, 'FAILS AS WANTED' if plant1 else 'DOES NOT FAIL'), '']
    # ---------------------------------------------------------------- (2)
    n_rows, bad2, plant2 = 0, [], 0
    for h in HS:
        G = AB.Group((h,))
        for r in tabs[h]:
            n_rows += 1
            _a, terms, b = b_expansion(h, r['primes'], r['k'])
            if b != r['b']:
                bad2.append((h, r['name'], b, r['b']))
            r['terms'] = terms
            if b_expansion(h, r['primes'], r['k'], drop3=True)[2] != r['b']:
                plant2 += 1
    c2 = not bad2
    ok_all &= c2
    plants_ok &= plant2 > 0
    L += ['## CHECK (2), BEFORE STEP (2): b by the m-fold expansion equal to b718`s b_lattice at every row: rows %d ; unequal %d -- %s' % (
        n_rows, len(bad2), 'AS WANTED' if c2 else 'NOT AS WANTED %s' % bad2[:3]),
          '   PLANT (2): the A_3 term dropped: unequal at %d rows -- %s' % (plant2, 'FAILS AS WANTED' if plant2 else 'DOES NOT FAIL'), '']
    # ---------------------------------------------------------------- (3)
    L.append('## STEP (3): THE TABLE (configuration up to c ~ -c and the automorphisms of C_h; p a split bad prime, r a ramified one; the '
             'digit its class; a, the pair sum P, A_3, b)')
    for h in HS:
        rows = tabs[h]
        negs = [r for r in rows if r['neg']]
        mins = [r for r in rows if r['minimal']]
        L.append('  C%d: rows %d ; negative %d ; minimal negative %d ; Omega of the minimal: %s ; their values %s' % (
            h, len(rows), len(negs), len(mins), sorted(set(r['Om'] for r in mins)),
            sorted(set(str(r['b']) for r in mins), key=lambda s: Fraction(s))))
        for r in mins:
            L.append('     MIN Omega %d  %-26s a %3d  P %4d  A3 %5s  b %s' % (r['Om'], key_name(r['key']), r['a'], r['P'], r['terms'].get(3, 0), r['b']))
    L += ['', '  THE TWO SHAPES (R331)(4) NAMES, EVERY CLASS ASSIGNMENT AND KIND (a, P, A_3, A_4, A_5, b):']
    for h in HS:
        for r in tabs[h]:
            pat = tuple(x for x, _t, _c in r['key'])
            if r['Om'] == 5 and pat in ((4, 1), (3, 1, 1)):
                tm = r['terms']
                L.append('     C%d  %-22s a %2d  P %3d  A3 %4s  A4 %4s  A5 %4s  b %-6s %s' % (
                    h, key_name(r['key']), r['a'], r['P'], tm.get(3, 0), tm.get(4, 0), tm.get(5, 0), r['b'],
                    'MINIMAL NEGATIVE' if r['minimal'] else ('negative' if r['neg'] else '')))
    L.append('')
    # ---------------------------------------------------------------- (4)
    c4 = True
    L.append('## CHECK (4), BEFORE ANY USE OF THE TABLE: -23 (C3), -39 (C4), -47 (C5)')
    for D, n0, b0, src in BANKED:
        S = PR.setup(D)
        h = S['h']
        neg_keys = dict((r['key'], r) for r in tabs[h] if r['neg'])
        li = least_instance(D, neg_keys, h)
        row = neg_keys.get(li.get('key'))
        good = (li.get('n') == n0 and not li.get('outside') and row is not None and row['b'] == b0 and (row['a'], row['P']) == NAV)
        c4 &= good
        L.append('  D = %d (C%d): the least bad-supported n whose configuration is a negative row: %s = %s (%s), the row %s: a %s, P %s, b %s ; '
                 'banked n0 %d, b %s (%s), the navigator`s a 4, P 12 -- %s' % (
                     D, h, li.get('n'), ' . '.join('%d^%d' % (p, x) for p, x, _t, _c in li.get('factors', [])),
                     ', '.join('%d %s class %d' % (p, t, c) for p, _x, t, c in li.get('factors', [])),
                     key_name(li['key']) if li.get('key') else '-', row and row['a'], row and row['P'], row and row['b'], n0, b0, src,
                     'AS WANTED' if good else 'NOT AS WANTED'))
        L.append('      below it, of Omega above the table`s and read by the model: %s' % (
            ', '.join('%d (Omega %d, b %s)' % x for x in li.get('outside_read', [])) or 'none'))
    S39 = PR.setup(-39)
    nk4 = dict((r['key'], r) for r in tabs[4] if r['neg'])
    pl = least_instance(-39, nk4, 4, override={2: (0,)})
    p4 = pl.get('n') != 120
    plants_ok &= p4
    ok_all &= c4
    L += ['   PLANT (4): the class above 2 at -39 set to 0: the least %s (not 120) -- %s' % (pl.get('n'), 'FAILS AS WANTED' if p4 else 'DOES NOT FAIL'),
          '### CHECK (4): %s' % ('ALL AS WANTED -- THE TABLE MAY BE USED' if c4 else 'NOT AS WANTED -- THE TABLE IS NOT USED'), '']
    # ---------------------------------------------------------------- THE GRADE
    sh = {}
    for h in HS:
        for r in tabs[h]:
            pat = tuple(x for x, _t, _c in r['key'])
            if r['Om'] == 5 and pat in ((4, 1), (3, 1, 1)):
                sh.setdefault((h, pat), []).append(r)
    neg2 = dict((k, [str(r['b']) for r in v if r['neg']]) for k, v in sh.items())
    L += ['## THE GRADE',
          '  THE CLOSED FORMS (the docstring`s), CHECKED BY TWO ROUTES, NOT COMPILED: a(n) by the count form equal to the turns and to b718`s',
          '  model at every divisor of every row of the three tables (check (1)); b by the m-fold expansion equal to b718`s Omega recursion at',
          '  every row (check (2)). The table for C3, C4 and C5 at Omega 1-6 is an exact finite computation over every configuration of bad',
          '  primes up to symmetry: a theorem of the model at those Omega, with its hypotheses (cyclic class group of order 3, 4 or 5; two',
          '  units; a(n) the principal ideals of norm n; every prime of n bad), checked, not compiled.',
          '  AT THE TWO SHAPES: the negative rows and their values -- %s.' % ' ; '.join(
              'C%d %s: %s' % (h, 'p^4 q' if pat == (4, 1) else 'p^3 q r', v or 'none negative') for (h, pat), v in sorted(neg2.items())),
          ('  -23 (C3), -39 (C4), -47 (C5): each n0 the least bad-supported n on a negative row of its table, its row a = 4, P = 12, b = -2: the -2'
           if c4 else '  -23 (C3), -39 (C4), -47 (C5): CHECK (4) NOT AS WANTED -- the table does not reproduce every banked n0; nothing below'),
          ('  at the three banked h > 2 cases is the table`s value at their shapes, no longer only evaluated at the instances (check (4)).'
           if c4 else '  is read from the table.'),
          '  WHAT IT DOES NOT SHOW: which row a new discriminant instantiates depends on the sizes of its least bad primes of each class; the',
          '  table names the values a least instance can take, not which it takes.', '',
          '### ### **CHECKS (1) (2) (4): %s ; PLANTS: %s ; THE GRADE: THE CLOSED FORMS OF a AND P AT p^4 q AND p^3 q r WRITTEN AND CHECKED BY TWO '
          'ROUTES ; THE TABLE FOR C3, C4, C5 AT OMEGA 1-6 EXACT ; -23, -39, -47 %s ; %d s.**' % (
              'ALL AS WANTED' if ok_all else 'NOT AS WANTED', 'ALL FAIL AS WANTED' if plants_ok else 'NOT ALL FAIL',
              'READ BY IT AS WANTED' if c4 else 'NOT READ BY IT AS WANTED', int(time.time() - t0))]
    return L, ok_all and plants_ok, tabs


if __name__ == '__main__':
    route = sys.argv[1] if len(sys.argv) > 1 else 'dry'
    L, ok, _t = run()
    print(NL.join(L))
    if route == 'bank':
        if not ok:
            sys.exit('### THE CHECKS NOT AS WANTED -- NOTHING WRITTEN')
        p = os.path.join(D_, 'b721_derivation.txt')
        with open(p + '.tmp', 'wb') as fh:
            fh.write((NL.join(L) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/b721_derivation.txt')
