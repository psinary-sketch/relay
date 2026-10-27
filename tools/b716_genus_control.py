# -*- coding: utf-8 -*-
"""b716_genus_control.py -- THE REPRESENTATION-COUNT CONTROL OF (R326)(4)(i), RUN BEFORE data/b716_registrations.txt IS COMMITTED, AS b712'S
CONTROL WAS RUN (tools/b712_genus_control.py, carried to discriminant -39 by the Write tool; b712's tool unedited).

### The forms: the reduced forms of discriminant -39 enumerated here (|b| <= a <= c, b >= 0 where |b| = a or a = c): Q1 = x^2 + xy + 10y^2
### (principal), Q2 = 2x^2 + xy + 5y^2 and its inverse 2x^2 - xy + 5y^2, Q3 = 3x^2 + 3xy + 4y^2; the class group of order 4, cyclic (two
### ambiguous classes, Q1 and Q3: the 2-rank 1 with -39 = (-3)(13) two prime discriminants), Q3 its element of order 2.
### The decomposition by the group's characters, read from Murty-Osburn arXiv:math/0412237v1 Theorem 2.3 (data/b713_source_pin.txt) at
### -39's two decompositions -39 = -39 . 1 and (-3)(13), with b713's bridge zeta(s, C) = Z_Q(s) / w, w = 2 units (:38-:39):
###     Z_Q1 + Z_Q3 + 2 Z_Q2 = 2 zeta(s) L(s, chi_-39)                (the trivial character)
###     Z_Q1 + Z_Q3 - 2 Z_Q2 = 2 L(s, chi_-3) L(s, chi_13)             (the genus character chi_{-3,13}: +1 on Q1, Q3; -1 on Q2, Q2')
###     Z_Q1 - Z_Q3          = 2 L_K(s, psi)                           (the two quartic characters psi, psi-bar, their L-functions equal
###                                                                     since Z_Q2 = Z_Q2'; a Hecke L-function of K = Q(sqrt(-39)), NOT a
###                                                                     product of Dirichlet L-functions: Theorem 2.3 does not reach it)
### so Z_Q1 = (1/2)(zeta L(chi_-39) + L(chi_-3) L(chi_13)) + L_K(s, psi).
### Read coefficient by coefficient for 1 <= n <= N, r_Q(n) by direct enumeration, exact integers: the first two lines against their
### Dirichlet coefficients; the third, which no Dirichlet product reaches, by the Hecke L-function's own laws -- a(n) = (r_Q1(n) - r_Q3(n))/2
### multiplicative on coprime m, n and a(p^(k+1)) = a(p) a(p^k) - chi_-39(p) a(p^(k-1)) at each prime. It computes no zero, no
### log-derivative coefficient and no onset ((R326)(4): nothing of -39 computed beyond this count control). Writes its own banks alone:
### data/b716_genus_control.txt and .json.
"""
import hashlib
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
ACT = 'b716'
DISC = -39
N = 400


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def jacobi(a, n):
    """the Jacobi symbol (a/n) for odd n > 0 (b712's)."""
    a %= n
    t = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                t = -t
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            t = -t
        a %= n
    return t if n == 1 else 0


def kronecker(D_, n):
    """the Kronecker symbol (D/n) for n >= 1 and D a discriminant (D = 0 or 1 mod 4) (b712's)."""
    k = 1
    while n % 2 == 0:
        n //= 2
        if D_ % 2 == 0:
            return 0
        k *= 1 if D_ % 8 in (1, 7) else -1
    return k * jacobi(D_, n) if n > 1 else k


def reduced_forms(disc):
    """every reduced form (a, b, c) of discriminant disc < 0: b^2 - 4ac = disc, |b| <= a <= c, b >= 0 where |b| = a or a = c."""
    out = []
    a = 1
    while 3 * a * a <= -disc:
        for b in range(-a + 1, a + 1):
            if (b * b - disc) % (4 * a):
                continue
            c = (b * b - disc) // (4 * a)
            if c < a or (b < 0 and a == c):
                continue
            out.append((a, b, c))
        a += 1
    return out


def ambiguous(f):
    a, b, c = f
    return b == 0 or b == a or a == c


def counts(f, n_max):
    """r_f(n) for 1 <= n <= n_max by direct enumeration over the box the form's minimum bounds (b712's, its 15 the discriminant's -disc)."""
    a, b, c = f
    r = [0] * (n_max + 1)
    X = int((4 * c * n_max / float(-DISC)) ** 0.5) + 2
    Y = int((4 * a * n_max / float(-DISC)) ** 0.5) + 2
    for x in range(-X, X + 1):
        for y in range(-Y, Y + 1):
            v = a * x * x + b * x * y + c * y * y
            if 1 <= v <= n_max:
                r[v] += 1
    return r


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def factor(n):
    out, p = {}, 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def hecke_laws(a, n_max):
    """the two laws of a Hecke L-function's coefficients a(n), n <= n_max: the coprime pairs (m, k), m k <= n_max, with a(mk) != a(m) a(k),
    and the prime powers p^(j+1) <= n_max with a(p^(j+1)) != a(p) a(p^j) - chi_-39(p) a(p^(j-1))."""
    bad_mult, bad_rec = [], []
    for m in range(2, n_max + 1):
        for k in range(m + 1, n_max // m + 1):
            if gcd(m, k) == 1 and a[m * k] != a[m] * a[k]:
                bad_mult.append((m, k))
    for p in range(2, n_max + 1):
        if len(factor(p)) != 1 or factor(p).get(p) != 1:
            continue
        q, prev, cur = p, 1, a[p]
        while q * p <= n_max:
            nxt = a[p] * cur - kronecker(DISC, p) * prev
            if a[q * p] != nxt:
                bad_rec.append(q * p)
            prev, cur, q = cur, a[q * p], q * p
    return bad_mult, bad_rec


def compute(n_max=N):
    F = reduced_forms(DISC)
    Q1, Q2, Q2i, Q3 = (1, 1, 10), (2, 1, 5), (2, -1, 5), (3, 3, 4)
    r1, r2, r2i, r3 = counts(Q1, n_max), counts(Q2, n_max), counts(Q2i, n_max), counts(Q3, n_max)
    rows, misses = [], []
    for n in range(1, n_max + 1):
        ds = divisors(n)
        s = 2 * sum(kronecker(DISC, d) for d in ds)
        t = 2 * sum(kronecker(-3, d) * kronecker(13, n // d) for d in ds)
        lhs_s, lhs_t = r1[n] + r3[n] + 2 * r2[n], r1[n] + r3[n] - 2 * r2[n]
        rows.append(dict(n=n, r1=r1[n], r2=r2[n], r2i=r2i[n], r3=r3[n], trivial=lhs_s, rhs_trivial=s, genus=lhs_t, rhs_genus=t,
                         quartic=(r1[n] - r3[n]) // 2 if (r1[n] - r3[n]) % 2 == 0 else None))
        if not (lhs_s == s and lhs_t == t and r2[n] == r2i[n] and (r1[n] - r3[n]) % 2 == 0):
            misses.append(n)
    a = [0] + [row['quartic'] if row['quartic'] is not None else 0 for row in rows]
    bad_mult, bad_rec = hecke_laws(a, n_max)
    return dict(forms=F, ambiguous=[f for f in F if ambiguous(f)], rows=rows, misses=misses, bad_mult=bad_mult, bad_rec=bad_rec, a=a)


def controls():
    """the hand checks, and three planted controls that must fail: a form of another discriminant in the trivial line, the genus line's
    sign reversed, and the principal form's own coefficients r_Q1(n)/2 read as a Hecke L-function (an Epstein zeta of class number 4 has
    no Euler product)."""
    c2 = compute(2)
    rw = c2['rows']
    hand = (rw[0]['trivial'], rw[0]['genus'], rw[1]['trivial'], rw[1]['genus']) == (2, 2, 4, -4)
    n60 = 60
    r0 = counts((1, 1, 6), n60)   # ### Q0 = x^2 + xy + 6y^2 (disc -23) in Q1's place
    r1, r2, r3 = counts((1, 1, 10), n60), counts((2, 1, 5), n60), counts((3, 3, 4), n60)
    planted_form = [n for n in range(1, n60 + 1) if r0[n] + r3[n] + 2 * r2[n] != 2 * sum(kronecker(DISC, d) for d in divisors(n))]
    planted_sign = [n for n in range(1, n60 + 1) if -(r1[n] + r3[n] - 2 * r2[n]) != 2 * sum(kronecker(-3, d) * kronecker(13, n // d) for d in divisors(n))]
    b1 = [0] + [x // 2 for x in counts((1, 1, 10), N)[1:]]
    pm, pr = hecke_laws(b1, N)
    return hand, len(planted_form), len(planted_sign), (len(pm), len(pr))


def _put(name, data):
    p = os.path.join(D, name)
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import act_membrane as MEM
    MEM.guard_path(ACT, p, None)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(data)
    os.replace(p + '.tmp', p)
    return hashlib.sha256(data).hexdigest()


def run(*a):
    t0 = time.time()
    c = compute()
    rows, misses = c['rows'], c['misses']
    hand, pf, ps, (pm, pr) = controls()
    forms_ok = c['forms'] == [(1, 1, 10), (2, -1, 5), (2, 1, 5), (3, 3, 4)] and len(c['ambiguous']) == 2
    L = ['%s -- THE CONTROL OF (R326)(4)(i): THE CHARACTER DECOMPOSITION AT DISCRIMINANT -39 READ COEFFICIENT BY COEFFICIENT THROUGH n = %d (%s)' % (ACT, N, utc()), '',
         '### Murty-Osburn arXiv:math/0412237v1 Theorem 2.3 at -39 = -39 . 1 and (-3)(13), b713`s bridge zeta(s, C) = Z_Q / 2 (data/b713_source_pin.txt',
         '### :38-:39): r_Q1 + r_Q3 + 2 r_Q2 = 2 sum_{d|n} chi_-39(d) ; r_Q1 + r_Q3 - 2 r_Q2 = 2 sum_{d|n} chi_-3(d) chi_13(n/d) ; and the quartic',
         '### pair`s a(n) = (r_Q1 - r_Q3)/2 read by the Hecke laws (multiplicative on coprime m, n; a(p^(j+1)) = a(p) a(p^j) - chi_-39(p) a(p^(j-1))).',
         '### r_Q by direct enumeration, chi_D the Kronecker symbol (D/.), exact integers. The count control only: no zero, no log-derivative',
         '### coefficient, no onset is computed ((R326)(4)).', '',
         '  THE REDUCED FORMS OF DISCRIMINANT -39 (enumerated): %s ; h = %d ; ambiguous %s -- the class group of order 4, cyclic (2-rank 1) ; %s' % (
             c['forms'], len(c['forms']), c['ambiguous'], 'AS WANTED' if forms_ok else 'NOT AS WANTED'),
         '  THE HAND CHECKS (n = 1: trivial 2, genus 2 ; n = 2: trivial 4, genus -4): %s' % ('EQUAL' if hand else 'DIFFER'),
         '  THE PLANTED CONTROLS, each must fail: Q0 = x^2 + xy + 6y^2 in place of Q1 in the trivial line, n <= 60: %d misses (%s) ; the genus line`s '
         'sign reversed, n <= 60: %d misses (%s) ; r_Q1(n)/2 read as a Hecke L-function, n <= %d: %d coprime pairs and %d prime powers off its laws (%s)' % (
             pf, 'FAILS AS WANTED' if pf else 'DID NOT FAIL', ps, 'FAILS AS WANTED' if ps else 'DID NOT FAIL', N, pm, pr,
             'FAILS AS WANTED' if (pm or pr) else 'DID NOT FAIL'), '',
         '  n | r_Q1 | r_Q2 | r_Q2` | r_Q3 | trivial | 2 sum chi_-39(d) | genus | 2 sum chi_-3(d) chi_13(n/d) | a(n) = (r_Q1 - r_Q3)/2']
    L += ['  %d | %d | %d | %d | %d | %d | %d | %d | %d | %s' % (r['n'], r['r1'], r['r2'], r['r2i'], r['r3'], r['trivial'], r['rhs_trivial'],
                                                               r['genus'], r['rhs_genus'], r['quartic']) for r in rows[:30]]
    L += ['  (rows 31-%d in the json bank)' % N, '',
          '  THE MISSES OF THE TWO GENUS LINES (and r_Q2 = r_Q2`, r_Q1 - r_Q3 even) THROUGH n = %d: %d %s' % (
              N, len(misses), ('(' + ', '.join(str(m) for m in misses[:20]) + ')') if misses else ''),
          '  THE QUARTIC PAIR`S LAWS THROUGH n = %d: coprime pairs off multiplicativity %d ; prime powers off the recursion %d' % (N, len(c['bad_mult']), len(c['bad_rec'])), '',
          '### ### **THE FORMS h = 4 %s ; THE DECOMPOSITION READ THROUGH n = %d ; MISSES %d ; THE QUARTIC LAWS OFF %d ; HAND CHECKS %s ; PLANTED CONTROLS %s ; '
          'NOTHING OF THE ZEROS COMPUTED.**' % ('AS WANTED' if forms_ok else 'NOT AS WANTED', N, len(misses), len(c['bad_mult']) + len(c['bad_rec']),
                                                'EQUAL' if hand else 'DIFFER', 'ALL THREE FAIL AS WANTED' if (pf and ps and (pm or pr)) else 'NOT ALL FAILING')]
    print(NL.join(L))
    if 'dry' in a:
        return
    j = dict(at=utc(), disc=DISC, n_max=N, forms=c['forms'], ambiguous=c['ambiguous'], misses=misses, bad_mult=c['bad_mult'], bad_rec=c['bad_rec'],
             hand=hand, planted_form_misses=pf, planted_sign_misses=ps, planted_hecke=[pm, pr], rows=rows, seconds=round(time.time() - t0, 3))
    h1 = _put('%s_genus_control.txt' % ACT, (NL.join(L) + NL).encode('utf-8'))
    h2 = _put('%s_genus_control.json' % ACT, (json.dumps(j, indent=1) + NL).encode('utf-8'))
    print('  sha256 %s data/%s_genus_control.txt ; %s data/%s_genus_control.json' % (h1, ACT, h2, ACT))


if __name__ == '__main__':
    if (sys.argv[1] if len(sys.argv) > 1 else '') != 'run':
        print('usage: b716_genus_control.py run [dry]')
        sys.exit(2)
    run(*sys.argv[2:])
