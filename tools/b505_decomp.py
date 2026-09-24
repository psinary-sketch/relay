# -*- coding: utf-8 -*-
"""b505_decomp.py -- COMPONENT 1: Q0`S REPRESENTATION NUMBERS AGAINST ITS DECOMPOSITION, AND THE PLACES SIDE CHECKED.

### `python tools/b505_decomp.py`
### r_Q0(n), n <= 10^4, by b325`s own `rep_counts`, against c1 A(n) + c2 a(n), where
###   A(n) = SUM_{d | n} chi_{-23}(d)   (the coefficients of zeta(s) L(s, chi_{-23})),
###   a(n) = the q^n coefficient of eta(z) eta(23z) = q PROD (1 - q^k)(1 - q^{23k})   (of L(s, psi)).
### c1 and c2 by least squares over all n, then tested EXACTLY in integers: 3 r(n) - 3 c1 A(n) - 3 c2 a(n) = 0.
### ### Then -Z0'/Z0 from the decomposition`s coefficients by a DIFFERENT algorithm from b325`s -- the exact
### Dirichlet inverse of b = r/2 in rationals, convolved with b(n) log n -- compared with `von_mangoldt_q` to 4096.
"""
import io
import json
import math
import os
import sys
from fractions import Fraction

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b325_epstein as EP       # noqa: E402
NL = chr(10)
N = 10000
NL4 = 4096
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def kronecker(a, n):
    """### the Kronecker symbol (a / n), n >= 1."""
    if n == 1:
        return 1
    res = 1
    while n % 2 == 0:
        n //= 2
        if a % 2 == 0:
            return 0
        res *= 1 if a % 8 in (1, 7) else -1
    a %= n
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                res = -res
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            res = -res
        a %= n
    return res if n == 1 else 0


def eta_eta23(K):
    """### coefficients of q PROD_k (1 - q^k)(1 - q^{23k}) up to q^K, by Euler`s pentagonal series."""
    e = [0] * (K + 1)
    k = 0
    while True:
        done = True
        for kk in ((k, ) if k == 0 else (k, -k)):
            p = kk * (3 * kk - 1) // 2
            if p <= K:
                e[p] += (-1) ** abs(kk)
                done = False
        if done and k > 0:
            break
        k += 1
    out = [0] * (K + 1)
    for i in range(K):                     # ### the product e(q) e(q^23), shifted by one
        if e[i] == 0:
            continue
        for j in range(0, (K - 1 - i) // 23 + 1):
            if e[j]:
                out[1 + i + 23 * j] += e[i] * e[j]
    return out


def main():
    r = EP.rep_counts(N)
    A = [0] * (N + 1)
    chi = [0] + [kronecker(-23, d) for d in range(1, N + 1)]
    for d in range(1, N + 1):
        if chi[d]:
            for m in range(d, N + 1, d):
                A[m] += chi[d]
    a = eta_eta23(N)
    X = np.array([[A[n], a[n]] for n in range(1, N + 1)], dtype=float)
    y = np.array(r[1:N + 1], dtype=float)
    (c1, c2), *_ = np.linalg.lstsq(X, y, rcond=None)
    f1, f2 = Fraction(c1).limit_denominator(12), Fraction(c2).limit_denominator(12)
    exact_bad = [n for n in range(1, N + 1) if Fraction(r[n]) != f1 * A[n] + f2 * a[n]]
    L = ['=' * 104, 'b505 COMPONENT 1 -- r_Q0 AGAINST c1 zeta L(chi_-23) + c2 L(psi), n <= %d.' % N, '=' * 104,
         '  r(1..12) %s' % r[1:13], '  A(1..12) %s' % A[1:13], '  a(1..12) %s  (eta(z) eta(23z))' % a[1:13],
         '  least squares : c1 = %.15f  c2 = %.15f' % (c1, c2),
         '  as fractions  : c1 = %s  c2 = %s' % (f1, f2),
         '  the exact integer test r(n) = c1 A(n) + c2 a(n) : fails at %d of %d n %s' % (len(exact_bad), N, exact_bad[:10])]
    # ### the places side, by the exact Dirichlet inverse
    b = [Fraction(0)] + [f1 * A[n] / 2 + f2 * a[n] / 2 for n in range(1, NL4 + 1)]
    inv = [Fraction(0)] * (NL4 + 1)
    inv[1] = 1 / b[1]
    for n in range(2, NL4 + 1):
        s = Fraction(0)
        for d in range(2, n + 1):
            if n % d == 0 and b[d]:
                s += b[d] * inv[n // d]
        inv[n] = -s / b[1]
    lam = [0.0] * (NL4 + 1)
    for n in range(2, NL4 + 1):
        s = 0.0
        for d in range(2, n + 1):
            if n % d == 0 and b[d] and inv[n // d]:
                s += float(b[d]) * math.log(d) * float(inv[n // d])
        lam[n] = s
    ref = EP.von_mangoldt_q(K=NL4, rq=EP.rep_counts(NL4))
    diffs = [abs(lam[n] - ref[n]) for n in range(2, NL4 + 1)]
    tol = [1e-9 * max(1.0, abs(ref[n])) for n in range(2, NL4 + 1)]
    agree = sum(1 for d, t in zip(diffs, tol) if d <= t)
    worst = max(range(len(diffs)), key=lambda i: diffs[i]) + 2
    L += ['  -Z0`/Z0 from the decomposition (exact Dirichlet inverse) against b325`s LAMQ, n = 2..%d :' % NL4,
          '    agreeing to 1e-9 relative : %d of %d ; largest disagreement %.3e at n = %d (LAMQ %.6f)'
          % (agree, NL4 - 1, diffs[worst - 2], worst, ref[worst]),
          '    nonzero LAMQ entries %d ; LAMQ(2..12) %s' % (sum(1 for n in range(2, NL4 + 1) if abs(ref[n]) > 1e-12),
                                                         ['%.4f' % ref[n] for n in range(2, 13)]), '=' * 104]
    res = dict(N=N, c1=float(c1), c2=float(c2), c1_frac=str(f1), c2_frac=str(f2), exact_fail=len(exact_bad),
               lam_n=NL4 - 1, lam_agree=agree, lam_worst=diffs[worst - 2], lam_worst_n=worst)
    io.open(os.path.join(D, 'b505_c1.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(os.path.join(D, 'b505_c1.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print(NL.join(L))


if __name__ == '__main__':
    main()
