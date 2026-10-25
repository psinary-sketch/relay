# -*- coding: utf-8 -*-
"""b712_genus_control.py -- THE CONTROL OF (R322)(6)(i), ON THE AUTHOR'S WORD AT b712'S FIRST PROMPT (the -15 text, option 2 carried with a control).

### The identity checked, as the author's word states it (genus theory, written by the navigator, no text cited):
###     Z_Q1(s) + Z_Q2(s) = 2 zeta(s) L(s, chi_-15) ;  Z_Q1(s) - Z_Q2(s) = 2 L(s, chi_-3) L(s, chi_5)
### with Q1 = x^2 + xy + 4y^2, Q2 = 2x^2 + xy + 2y^2, Z_Q(s) the sum over (x, y) != (0, 0) of Q(x, y)^(-s), chi_D the Kronecker symbol (D/.).
### Read coefficient by coefficient: r_Q1(n) + r_Q2(n) = 2 sum_{d|n} chi_-15(d) and r_Q1(n) - r_Q2(n) = 2 sum_{d|n} chi_-3(d) chi_5(n/d),
### for 1 <= n <= N, r_Q(n) by direct enumeration. Exact integers throughout. It computes no zero, no log-derivative coefficient and no
### onset (the word: "This control checks the identity only"). Writes its own banks alone: data/b712_genus_control.txt and .json.
"""
import hashlib
import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
ACT = 'b712'
N = 400
Q1 = (1, 1, 4)
Q2 = (2, 1, 2)


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def jacobi(a, n):
    """the Jacobi symbol (a/n) for odd n > 0."""
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
    """the Kronecker symbol (D/n) for n >= 1 and D a discriminant (D = 0 or 1 mod 4)."""
    k = 1
    while n % 2 == 0:
        n //= 2
        if D_ % 2 == 0:
            return 0
        k *= 1 if D_ % 8 in (1, 7) else -1
    return k * jacobi(D_, n) if n > 1 else k


def counts(f, n_max):
    """r_f(n) for 1 <= n <= n_max by direct enumeration over the box the form's minimum bounds (a, c >= 1, 4ac - b^2 = 15)."""
    a, b, c = f
    r = [0] * (n_max + 1)
    # ### f(x, y) >= (15 / (4c)) x^2 and >= (15 / (4a)) y^2, so |x| <= sqrt(4c n / 15), |y| <= sqrt(4a n / 15)
    X = int((4 * c * n_max / 15.0) ** 0.5) + 2
    Y = int((4 * a * n_max / 15.0) ** 0.5) + 2
    for x in range(-X, X + 1):
        for y in range(-Y, Y + 1):
            v = a * x * x + b * x * y + c * y * y
            if 1 <= v <= n_max:
                r[v] += 1
    return r


def compute(n_max=N):
    r1 = counts(Q1, n_max)
    r2 = counts(Q2, n_max)
    rows, misses = [], []
    for n in range(1, n_max + 1):
        divs = [d for d in range(1, n + 1) if n % d == 0]
        s = 2 * sum(kronecker(-15, d) for d in divs)
        t = 2 * sum(kronecker(-3, d) * kronecker(5, n // d) for d in divs)
        ok_s = r1[n] + r2[n] == s
        ok_t = r1[n] - r2[n] == t
        rows.append(dict(n=n, r1=r1[n], r2=r2[n], sum=r1[n] + r2[n], rhs_sum=s, diff=r1[n] - r2[n], rhs_diff=t))
        if not (ok_s and ok_t):
            misses.append(n)
    return rows, misses


def controls():
    """the word's hand checks and two planted controls that must fail (a form of another discriminant; a wrong sign on the difference)."""
    rows, _ = compute(2)
    hand = (rows[0]['sum'], rows[0]['diff'], rows[1]['sum'], rows[1]['diff']) == (2, 2, 4, -4)
    r3 = counts((1, 1, 6), 60)   # ### Q0 = x^2 + xy + 6y^2 (disc -23): it must miss the -15 sum's right side
    planted_form = [n for n in range(1, 61) if r3[n] + counts(Q2, 60)[n] != 2 * sum(kronecker(-15, d) for d in range(1, n + 1) if n % d == 0)]
    r1, r2 = counts(Q1, 60), counts(Q2, 60)
    planted_sign = [n for n in range(1, 61) if r2[n] - r1[n] != 2 * sum(kronecker(-3, d) * kronecker(5, n // d) for d in range(1, n + 1) if n % d == 0)]
    return hand, len(planted_form), len(planted_sign)


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
    rows, misses = compute()
    hand, pf, ps = controls()
    L = ['%s -- THE CONTROL OF (R322)(6)(i): THE GENUS IDENTITY AT DISCRIMINANT -15 READ COEFFICIENT BY COEFFICIENT THROUGH n = %d (%s)' % (ACT, N, utc()), '',
         '### the author`s word at b712`s first prompt (option 2 carried with a control): r_Q1(n) + r_Q2(n) = 2 sum_{d|n} chi_-15(d) and',
         '### r_Q1(n) - r_Q2(n) = 2 sum_{d|n} chi_-3(d) chi_5(n/d), Q1 = x^2 + xy + 4y^2, Q2 = 2x^2 + xy + 2y^2, r_Q by direct enumeration,',
         '### chi_D the Kronecker symbol (D/.), exact integers. The identity only: no zero, no log-derivative coefficient, no onset is computed.', '',
         '  THE HAND CHECKS (the word`s: n = 1 sum 2 difference 2; n = 2 sum 4 difference -4): %s' % ('EQUAL' if hand else 'DIFFER'),
         '  THE PLANTED CONTROLS, each must miss: Q0 = x^2 + xy + 6y^2 in place of Q1 in the sum, n <= 60: %d misses (%s); the difference`s sign '
         'reversed, n <= 60: %d misses (%s)' % (pf, 'FAILS AS WANTED' if pf else 'DID NOT FAIL', ps, 'FAILS AS WANTED' if ps else 'DID NOT FAIL'), '',
         '  n | r_Q1 | r_Q2 | sum | 2 sum chi_-15(d) | difference | 2 sum chi_-3(d) chi_5(n/d)']
    L += ['  %d | %d | %d | %d | %d | %d | %d' % (r['n'], r['r1'], r['r2'], r['sum'], r['rhs_sum'], r['diff'], r['rhs_diff']) for r in rows[:30]]
    L += ['  (rows 31-%d in the json bank)' % N, '',
          '  THE MISSES THROUGH n = %d: %d %s' % (N, len(misses), ('(' + ', '.join(str(m) for m in misses) + ')') if misses else ''), '',
          '### ### **THE IDENTITY READ THROUGH n = %d ; MISSES %d ; HAND CHECKS %s ; PLANTED CONTROLS %s ; NOTHING OF THE ZEROS COMPUTED.**' % (
              N, len(misses), 'EQUAL' if hand else 'DIFFER', 'BOTH FAIL AS WANTED' if (pf and ps) else 'NOT BOTH FAILING')]
    print(NL.join(L))
    if 'dry' in a:
        return
    j = dict(at=utc(), n_max=N, forms=dict(Q1=Q1, Q2=Q2), misses=misses, hand=hand, planted_form_misses=pf, planted_sign_misses=ps,
             rows=rows, seconds=round(time.time() - t0, 3))
    h1 = _put('%s_genus_control.txt' % ACT, (NL.join(L) + NL).encode('utf-8'))
    h2 = _put('%s_genus_control.json' % ACT, (json.dumps(j, indent=1) + NL).encode('utf-8'))
    print('  sha256 %s data/%s_genus_control.txt ; %s data/%s_genus_control.json' % (h1, ACT, h2, ACT))


if __name__ == '__main__':
    if (sys.argv[1] if len(sys.argv) > 1 else '') != 'run':
        print('usage: b712_genus_control.py run [dry]')
        sys.exit(2)
    run(*sys.argv[2:])
