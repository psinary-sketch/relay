# -*- coding: utf-8 -*-
"""b755, (R365)(4)(c), (j), (k), (l): THE FOUR CANDIDATES' GENERATOR, written by the seat from the statements alone ((S3), data/b754_rules.txt
(3)) and committed before any of its runs; each reproduction a run of its own, each plant a separate run after it. No value of an Epstein
zeta function is computed: representation numbers, Kronecker symbols and sums over primes alone.

THE STATEMENTS (data/b755_ferry.txt :16, :18-:20; (c) also data/b753_registrations.txt :73-:77), and the seat's reading of each:
  (c) "at a product of four distinct split primes whose prime ideals lie in one non-principal class and its inverse, b is -32, -4 or -6 as
      that class has order 2, order 4 or another order": at -15 (2.17.23.47), -39 (2.5.11.41) and -23 (2.3.13.29). b(n) the coefficient of
      log(Z_Q/2) = SUM b(n) n^-s, Q the principal form (data/b753_registrations.txt :15-:16, cQ(n) = b(n) log n), by the divisor recursion
      Omega(n) b(n) = Omega(n) a(n) - SUM over d | n, d < n, of Omega(d) b(d) a(n/d), a(m) = r_Q(m)/2, in exact rationals (Omega is additive,
      so it is a derivation of the Dirichlet product as log is). A prime's class: the set of reduced forms representing it (a class and its
      inverse are represented by a form and its opposite); its order: the least k with p^k primitively represented by the principal form.
      CONTROLS FIRST: b(48) at -23 and b(80) at -31 against the walk's -2 (data/b753_registrations.txt :30-:31), b(24) at -15 against -2
      (data/b721_registrations.txt :31). PLANT: the largest of the four replaced by the least split prime the principal form represents.
  (j) the real part sigma solving SUM e_p arctan(p^-sigma) = pi/2 over the primes outside the principal class, e_p = 2 at a split prime and
      1 at a ramified one, the primes to P = 10^8 with the tail (1/2) E1((sigma - 1) log P) (a quarter of the primes split outside the
      principal class, each of weight 2). THREE CONTROLS AGAINST PRINT before any row, each wanted within 1e-6 of the print: Bombieri and
      Ghosh 2011, Theorem 7 at xi = 0, SUM over p = 2, 3 mod 5 of arctan(p^-sigma) = pi/2, Table 1's 1.067026 (data/b755_literature.txt
      T1.f, T1.h; the tail (1/2) E1); Arias de Reyna and van de Lune, Theorem 9.2, SUM over all p of arcsin(p^-sigma) = pi/2, 1.19234 73371
      (T6.a: its equation an arcsine as printed; the tail E1). And -20 beside 1.133906322, the ruling's figure, which stands in no source
      the literature bank read: no control. THE ROWS: the eighteen fields of class number 2 (data/b721_registrations.txt :31-:48), each class
      number recounted as reduced forms; the value at P = 10^7 printed beside. PLANT: the tail dropped.
  (k) at -24, r0 and r1 the representation numbers of x^2 + 6y^2 and 2x^2 + 3y^2: r0(n) + r1(n) = 2 SUM over d | n of chi_-24(d) and
      r0(n) - r1(n) = 2 SUM over d | n of chi_-3(d) chi_8(n/d), for n up to 3000, mismatches 0 wanted, the characters Kronecker symbols.
      PLANT: chi_-8 in place of chi_8.
  (l) over the 69 heights of data/b725_interference.txt, S the count of pairs whose difference of heights, times log 2 / 2 pi and times
      log 3 / 2 pi, lies within 1/18 of a whole number in both; THE NULL 4,000 draws of 69 heights uniform on the heights' own range (the
      least to the greatest), numpy's default generator with seed 755. PLANT: log 5 in place of log 3, AS WANTED where the planted S is not
      above the largest draw of the null drawn with the same two logarithms and the same seed.
USAGE: b755_cands.py <c|j|k|l> [plant]
"""
import json
import math
import os
import re
import sys
import time
from fractions import Fraction

import mpmath
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAVW = "the navigator's workspace, in no bank ((R365)(4)(%s), data/b755_ferry.txt :%d)"
C2_FIELDS = [-15, -20, -24, -35, -40, -51, -52, -88, -91, -115, -123, -148, -187, -232, -235, -267, -403, -427]


def write(path, text):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(text)
    os.replace(tmp, path)


def kron(D, p):
    """the Kronecker symbol (D/p) at a prime p; at p = 2, D = 0 or 1 mod 4."""
    p = int(p)
    if p == 2:
        return 0 if D % 2 == 0 else (1 if D % 8 in (1, 7) else -1)
    if D % p == 0:
        return 0
    return 1 if pow(D % p, (p - 1) // 2, p) == 1 else -1


def factor(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def divisors(n):
    ds = [1]
    for p, e in factor(n).items():
        ds = [d * p ** k for d in ds for k in range(e + 1)]
    return sorted(ds)


def char(D, n):
    v = 1
    for p, e in factor(n).items():
        v *= kron(D, p) ** e
    return v


def reduced_forms(D):
    out, a = [], 1
    while 3 * a * a <= -D:
        for b in range(-a + 1, a + 1):
            if (b - D) % 2:
                continue
            num = b * b - D
            if num % (4 * a):
                continue
            c = num // (4 * a)
            if c < a or (b < 0 and a == c) or math.gcd(math.gcd(a, abs(b)), c) != 1:
                continue
            out.append((a, b, c))
        a += 1
    return out


def reps(f, m, primitive=False):
    a, b, c = f
    Dabs = 4 * a * c - b * b
    out = []
    ymax = math.isqrt(4 * a * m // Dabs) + 1
    for y in range(-ymax, ymax + 1):
        disc = 4 * a * m - Dabs * y * y
        if disc < 0:
            continue
        s = math.isqrt(disc)
        if s * s != disc:
            continue
        for sg in ((0,) if s == 0 else (s, -s)):
            num = -b * y + sg
            if num % (2 * a) == 0:
                x = num // (2 * a)
                if not primitive or math.gcd(x, y) == 1:
                    out.append((x, y))
    return out


def b_coeff(n, Q):
    divs = divisors(n)
    a = {m: Fraction(len(reps(Q, m)), 2) for m in divs}
    if a[1] != 1:
        raise SystemExit('### r_Q(1) is not 2 -- REFUSED')
    om = {m: sum(factor(m).values()) for m in divs}
    b = {1: Fraction(0)}
    for m in divs[1:]:
        s = om[m] * a[m] - sum(om[d] * b[d] * a[m // d] for d in divs if d < m and m % d == 0)
        b[m] = s / om[m]
    return b[n]


def class_of(D, p):
    return frozenset(f for f in reduced_forms(D) if reps(f, p))


def order_of(Q, p, cap=24):
    for k in range(1, cap + 1):
        if reps(Q, p ** k, primitive=True):
            return k
    return None


def fr(x):
    return str(x) if x.denominator != 1 else str(x.numerator)


# ---------------------------------------------------------------- (c)
C_CASES = [(-15, (2, 17, 23, 47)), (-39, (2, 5, 11, 41)), (-23, (2, 3, 13, 29))]
C_WANT = {2: -32, 4: -4}


def run_c(plant):
    L, J, ok = [], {'controls': [], 'rows': []}, True
    L.append('THE CONTROLS FIRST (the divisor recursion against the record):')
    for D, n, want, src in ((-23, 48, -2, 'data/b753_registrations.txt :30'), (-31, 80, -2, 'data/b753_registrations.txt :31'),
                            (-15, 24, -2, 'data/b721_registrations.txt :31')):
        Q = reduced_forms(D)[0]
        b = b_coeff(n, Q)
        good = b == want
        ok &= good
        J['controls'].append({'D': D, 'n': n, 'b': fr(b), 'want': want, 'ok': good})
        L.append('  D = %d, Q = %s: b(%d) = %s ; the record %d (%s): %s' % (D, Q, n, fr(b), want, src, 'AS WANTED' if good else 'NOT AS WANTED'))
    L.append('')
    L.append('THE ROWS%s:' % (' -- THE PLANT: the largest of the four replaced by the least split prime the principal form represents' if plant else ''))
    for D, ps in C_CASES:
        forms = reduced_forms(D)
        Q = forms[0]
        ps = list(ps)
        k0 = {order_of(Q, p) for p in ps}
        want0 = C_WANT.get(k0.pop(), -6) if len(k0) == 1 else None  # the statement's value at the stated four, the plant read against it
        swapped = None
        if plant:
            q = 2
            while not (factor(q) == {q: 1} and kron(D, q) == 1 and reps(Q, q) and q not in ps):  # a prime: defect (k), repaired
                q += 1
            swapped = (max(ps), q)
            ps[ps.index(max(ps))] = q
        n = math.prod(ps)
        kinds = [(p, kron(D, p), bool(reps(Q, p)), sorted(class_of(D, p)), order_of(Q, p)) for p in ps]
        split_np = all(k == 1 and not r for _, k, r, _, _ in kinds)
        one_class = len({tuple(c) for *_, c, _ in kinds}) == 1 and Q not in kinds[0][3]
        orders = {o for *_, o in kinds}
        k = kinds[0][4] if len(orders) == 1 else None
        want = C_WANT.get(k, -6) if not plant else want0
        b = b_coeff(n, Q)
        cond = split_np and one_class and len(set(ps)) == 4 and k is not None
        agree = b == want
        J['rows'].append({'D': D, 'h': len(forms), 'primes': ps, 'n': n, 'kinds': [[p, kk, r, [list(f) for f in c], o] for p, kk, r, c, o in kinds],
                          'conditions': cond, 'order': k, 'want': want, 'b': fr(b), 'agree': agree, 'swapped': swapped})
        L.append('  D = %d (h = %d, the reduced forms %s), Q = %s ; n = %s = %d%s' % (
            D, len(forms), forms, Q, '.'.join(map(str, ps)), n, ('   [THE PLANT: %d -> %d]' % swapped) if swapped else ''))
        for p, kk, r, c, o in kinds:
            L.append('      p = %d: Kronecker %d ; represented by Q %s ; the reduced forms representing it %s ; order of its class %s' % (
                p, kk, 'YES' if r else 'no', c, o))
        L.append('    the statement\'s conditions (four distinct split primes outside the principal class, one class and its inverse): %s ;'
                 ' the class\'s order %s, so b %d wanted ; b(n) = %s : %s' % (
                     'MET' if cond else 'NOT MET', k, want, fr(b), 'AGREES' if agree else 'DIFFERS'))
        if plant:
            ok &= not agree
        else:
            ok &= agree and cond
    if plant:
        verdict = 'EACH PLANTED n DIFFERS FROM THE STATEMENT\'S VALUE: AS WANTED' if ok else 'A PLANTED n AGREES: NOT AS WANTED'
    else:
        verdict = ('THE CONTROLS AS WANTED ; b = -32, -4, -6 AT THE THREE FIELDS AS STATED' if ok else 'NOT AS STATED')
    return L, J, ok, verdict, ' (the statement\'s own values; the navigator kept no output, %s)' % (NAVW % ('c', 16))


# ---------------------------------------------------------------- (j)
def primes_upto(n):
    s = np.ones(n + 1, dtype=bool)
    s[:2] = False
    for i in range(2, math.isqrt(n) + 1):
        if s[i]:
            s[i * i::i] = False
    return np.nonzero(s)[0].astype(np.int64)


def principal_values(D, n):
    Dabs, bq = -D, (0 if D % 4 == 0 else 1)
    rep = np.zeros(n + 1, dtype=bool)
    for y in range(0, math.isqrt(4 * n // Dabs) + 1):
        rem = 4 * n - Dabs * y * y
        if rem < 0:
            break
        u = np.arange((bq * y) % 2, math.isqrt(rem) + 1, 2, dtype=np.int64)
        v = (u * u + Dabs * y * y) // 4
        rep[v[v >= 1]] = True
    return rep


def kron_vec(D, ps):
    out = np.zeros(len(ps), dtype=np.int8)
    odd = ps > 2
    p = ps[odd]
    a = D % p
    res, base, e = np.ones_like(p), a.copy(), (p - 1) // 2
    while np.any(e > 0):
        m = (e & 1) == 1
        res = np.where(m, (res * base) % p, res)
        base = (base * base) % p
        e >>= 1
    out[odd] = np.where(a == 0, 0, np.where(res == 1, 1, -1))
    out[~odd] = kron(D, 2)
    return out


def solve(logp, w, P, fn, tail_coef):
    L = math.log(P)

    def F(sg):
        x = np.exp(-sg * logp)
        if fn == 'atan':
            v, dv = np.sum(w * np.arctan(x)), np.sum(w * (-logp) * x / (1 + x * x))
        else:
            v, dv = np.sum(w * np.arcsin(x)), np.sum(w * (-logp) * x / np.sqrt(1 - x * x))
        if tail_coef:
            z = (sg - 1) * L
            v += tail_coef * float(mpmath.e1(z))
            dv += tail_coef * (-math.exp(-z) / (sg - 1))
        return v - math.pi / 2, dv

    lo, hi = 1.0 + 1e-9, 3.0
    if F(lo)[0] < 0:
        return None
    sg = 1.1
    for _ in range(200):
        f, df = F(sg)
        if f > 0:
            lo = sg
        else:
            hi = sg
        new = sg - f / df
        if not (lo < new < hi):
            new = (lo + hi) / 2
        if abs(new - sg) < 1e-14:
            return new
        sg = new
    return sg


def sv(x):
    return '%.10f' % x if x is not None else 'NO ROOT ABOVE 1'


def run_j(plant):
    t0 = time.time()
    P, P2 = 10 ** 8, 10 ** 7
    ps = primes_upto(P)
    lp = np.log(ps.astype(np.float64))
    small = ps <= P2
    t_sieve = time.time() - t0
    tc = 0.0 if plant else 1.0
    L, J, ok = [], {'P': P, 'P2': P2, 'primes': int(len(ps)), 'tail': not plant, 'controls': [], 'rows': []}, True
    L.append('THE CONTROLS AGAINST PRINT, BEFORE ANY ROW (primes to %d: %d ; to %d: %d ; the sieve %.1f s ; tail %s):' % (
        P, len(ps), P2, int(small.sum()), t_sieve, 'ON' if not plant else 'DROPPED (THE PLANT)'))
    ctl = [('Bombieri-Ghosh 2011 Theorem 7 at xi = 0: SUM over p = 2, 3 mod 5 of arctan(p^-sigma) = pi/2 (data/b755_literature.txt T1.f, T1.h)',
            (ps % 5 == 2) | (ps % 5 == 3), 'atan', 0.5, 1.067026, '1.067026 (Table 1; 1.06702646637238 in section 9, T1.i)', 1.0670264),
           ('Arias de Reyna-van de Lune Theorem 9.2: SUM over all p of arcsin(p^-sigma) = pi/2 (T6.a)',
            np.ones(len(ps), dtype=bool), 'asin', 1.0, 1.1923473371, '1.19234 73371 86193 (Theorem 9.2)', 1.19234736)]
    for name, mask, fn, coef, prt, prt_words, nav in ctl:
        w = np.ones(int(mask.sum()))
        s1 = solve(lp[mask], w, P, fn, coef * tc)
        s2 = solve(lp[mask & small], np.ones(int((mask & small).sum())), P2, fn, coef * tc)
        good = s1 is not None and abs(s1 - prt) < 1e-6
        if plant:
            ok &= not good
        else:
            ok &= good
        J['controls'].append({'name': name, 'sigma': s1, 'sigma_P2': s2, 'print': prt, 'within_1e-6': good, 'nav': nav})
        L.append('  %s:' % name)
        L.append('    sigma = %s at P = 10^8 (%s at 10^7) ; in print %s ; the difference %s: %s   | beside it %s: %s' % (
            sv(s1), sv(s2), prt_words, ('%.2e' % (s1 - prt)) if s1 is not None else '-',
            ('WITHIN 1e-6' if good else 'NOT WITHIN 1e-6'), NAVW % ('j', 18), nav))
    L.append('')
    L.append('THE ROWS, the eighteen fields of class number 2 (data/b721_registrations.txt :31-:48); e_p = 2 split, 1 ramified, outside the principal class:')
    nav_rows = {-15: 1.17955, -20: 1.13391, -427: 1.01206}
    for D in C2_FIELDS:
        forms = reduced_forms(D)
        if len(forms) != 2:
            raise SystemExit('### D = %d: %d reduced forms, not 2 -- REFUSED' % (D, len(forms)))
        rep = principal_values(D, P)
        notrep = ~rep[ps]
        del rep
        k = kron_vec(D, ps)
        sel_s = (k == 1) & notrep
        sel_r = (k == 0) & notrep
        sel = sel_s | sel_r
        w = np.where(sel_s[sel], 2.0, 1.0)
        s1 = solve(lp[sel], w, P, 'atan', 0.5 * tc)
        sel2 = sel & small
        s2 = solve(lp[sel2], np.where(sel_s[sel2], 2.0, 1.0), P2, 'atan', 0.5 * tc)
        ram = [int(p) for p in ps[sel_r]]
        first = [int(p) for p in ps[sel_s][:3]]
        J['rows'].append({'D': D, 'forms': forms, 'ramified_outside': ram, 'least_split_outside': first, 'sigma': s1, 'sigma_P2': s2,
                          'split_outside_to_P': int(sel_s.sum()), 'nav': nav_rows.get(D)})
        extra = ''
        if D == -20:
            extra = ' ; beside it 1.133906322, the ruling\'s figure as relayed from Bombieri and Mueller 2008, in no source read (data/b755_literature.txt N1)'
        if D in nav_rows:
            extra += ' ; beside it %s: %s' % (NAVW % ('j', 18), nav_rows[D])
        L.append('  %5d  forms %s ; ramified outside %s ; least split outside %s ; split outside to 10^8: %d ; sigma %s (10^7: %s)%s' % (
            D, forms, ram, first, int(sel_s.sum()), sv(s1), sv(s2), extra))
        J['seconds'] = round(time.time() - t0, 1)
    if plant:
        verdict = ('BOTH CONTROLS LEAVE 1e-6 OF THE PRINT WITH THE TAIL DROPPED: AS WANTED' if ok else 'A CONTROL STAYS WITHIN 1e-6: NOT AS WANTED')
    else:
        verdict = ('BOTH CONTROLS WITHIN 1e-6 OF THE PRINT ; THE EIGHTEEN ROWS COMPUTED' if ok else 'A CONTROL NOT WITHIN 1e-6 OF THE PRINT')
    L.append('')
    L.append('  %.1f s' % (time.time() - t0))
    return L, J, ok, verdict, ''


# ---------------------------------------------------------------- (k)
def run_k(plant):
    N = 3000
    r0, r1 = [0] * (N + 1), [0] * (N + 1)
    for x in range(-60, 61):
        for y in range(-32, 33):
            v = x * x + 6 * y * y
            if 1 <= v <= N:
                r0[v] += 1
            v = 2 * x * x + 3 * y * y
            if 1 <= v <= N:
                r1[v] += 1
    D8 = -8 if plant else 8
    bad1, bad2 = [], []
    for n in range(1, N + 1):
        ds = divisors(n)
        s1 = 2 * sum(char(-24, d) for d in ds)
        s2 = 2 * sum(char(-3, d) * char(D8, n // d) for d in ds)
        if r0[n] + r1[n] != s1:
            bad1.append(n)
        if r0[n] - r1[n] != s2:
            bad2.append(n)
    L = ['  the forms x^2 + 6y^2 (r0) and 2x^2 + 3y^2 (r1), n = 1..%d ; the second identity with chi_%d%s' % (N, D8, ' (THE PLANT)' if plant else ''),
         '  r0 + r1 = 2 SUM chi_-24(d): mismatches %d%s' % (len(bad1), (' (first %s)' % bad1[:8]) if bad1 else ''),
         '  r0 - r1 = 2 SUM chi_-3(d) chi_%d(n/d): mismatches %d%s' % (D8, len(bad2), (' (first %s)' % bad2[:8]) if bad2 else ''),
         '  beside it %s: %s' % (NAVW % ('k', 19), '1,523 with chi_-8 planted' if plant else '0')]
    J = {'N': N, 'chi': D8, 'mismatch_1': len(bad1), 'mismatch_2': len(bad2), 'first_1': bad1[:20], 'first_2': bad2[:20]}
    if plant:
        ok = len(bad2) > 0
        verdict = 'THE PLANT BREAKS THE SECOND IDENTITY: AS WANTED' if ok else 'THE PLANT DOES NOT BREAK IT: NOT AS WANTED'
    else:
        ok = not bad1 and not bad2
        verdict = 'BOTH IDENTITIES 0 MISMATCHES' if ok else 'MISMATCHES'
    return L, J, ok, verdict, ''


# ---------------------------------------------------------------- (l)
def heights_23():
    hs = []
    for line in open(os.path.join(ROOT, 'data', 'b725_interference.txt'), encoding='utf-8'):
        m = re.match(r'^\s+off(\d+)\s+([0-9.]+)\s+([0-9.]+)\s', line)
        if m:
            hs.append(float(m.group(3)))
    if len(hs) != 69:
        raise SystemExit('### %d heights read, wanted 69 -- REFUSED' % len(hs))
    return np.array(sorted(hs))


def S_count(h, l1, l2):
    i, j = np.triu_indices(len(h), 1)
    d = np.abs(h[i] - h[j])
    v1, v2 = d * l1 / (2 * math.pi), d * l2 / (2 * math.pi)
    return int(np.sum((np.abs(v1 - np.round(v1)) <= 1 / 18) & (np.abs(v2 - np.round(v2)) <= 1 / 18))), len(d)


def run_l(plant):
    h = heights_23()
    l1, l2 = math.log(2), math.log(5 if plant else 3)
    S, npairs = S_count(h, l1, l2)
    rng = np.random.default_rng(755)
    lo, hi = float(h.min()), float(h.max())
    draws = np.array([S_count(np.sort(rng.uniform(lo, hi, len(h))), l1, l2)[0] for _ in range(4000)])
    above = S > draws.max()
    L = ['  the 69 heights of data/b725_interference.txt, from %.6f to %.6f ; the logarithms log 2 and log %d%s' % (lo, hi, 5 if plant else 3,
                                                                                                                  ' (THE PLANT)' if plant else ''),
         '  S = %d of %d pairs ; THE NULL, 4,000 draws uniform on [%.6f, %.6f], seed 755: mean %.2f, largest %d ; S %s the largest draw' % (
             S, npairs, lo, hi, draws.mean(), draws.max(), 'ABOVE' if above else 'NOT ABOVE'),
         '  beside it %s: %s' % (NAVW % ('l', 20), 'no figure kept for the plant' if plant else '168 of 2,346 pairs, the null\'s mean 28.9, its largest 56')]
    J = {'S': S, 'pairs': npairs, 'logs': [2, 5 if plant else 3], 'null_mean': float(draws.mean()), 'null_max': int(draws.max()),
         'seed': 755, 'range': [lo, hi], 'above': bool(above)}
    if plant:
        ok = not above
        verdict = 'THE PLANTED S IS NOT ABOVE ITS NULL: AS WANTED' if ok else 'THE PLANTED S IS ABOVE ITS NULL: NOT AS WANTED'
    else:
        ok = True
        verdict = 'S = %d AGAINST THE NULL\'S LARGEST %d, %s' % (S, draws.max(), 'ABOVE' if above else 'NOT ABOVE')
    return L, J, ok, verdict, ''


RUNS = {'c': (run_c, '(R365)(4)(c): FOUR DISTINCT SPLIT PRIMES IN ONE CLASS AND ITS INVERSE, AT -15, -39 AND -23', 16),
        'j': (run_j, '(R365)(4)(j): HOW FAR TO THE RIGHT THE ZEROS REACH AT CLASS NUMBER 2, THE EQUATION OVER THE PRIMES', 18),
        'k': (run_k, '(R365)(4)(k): THE TWO IDENTITIES AT -24', 19),
        'l': (run_l, '(R365)(4)(l): THE RECURRENCE OF HEIGHTS AT -23', 20)}


def main(argv):
    if not argv or argv[0] not in RUNS or argv[1:] not in ([], ['plant']):
        sys.exit(__doc__)
    key, plant = argv[0], argv[1:] == ['plant']
    fn, title, line = RUNS[key]
    stamp = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    t0 = time.time()
    L, J, ok, verdict, note = fn(plant)
    J.update({'mode': key + (' plant' if plant else ''), 'stamp': stamp, 'seconds': round(time.time() - t0, 1), 'ok': ok})
    head = ('b755 -- %s%s (%s)\n\n'
            '### by tools/b755_cands.py %s%s, written from the statement alone (data/b755_ferry.txt :%d) and committed before its run%s;\n'
            '### no value of an Epstein zeta function computed. The navigator\'s figures stand beside, in no bank; none is a banked figure.\n\n'
            % (title, ' -- THE PLANT' if plant else '', stamp, key, ' plant' if plant else '', line,
               ', the plant a separate run after the reproduction' if plant else '', ))
    text = head + '\n'.join(L) + '\n\n### ### **(4)(%s)%s: %s%s ; %.1f s.**\n' % (key, ' THE PLANT' if plant else '', verdict, note, time.time() - t0)
    print(text)
    name = 'b755_cand_%s%s' % (key, '_plant' if plant else '')
    write(os.path.join(ROOT, 'data', name + '.txt'), text)
    write(os.path.join(ROOT, 'data', name + '.json'), json.dumps(J, indent=1, default=str) + '\n')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
