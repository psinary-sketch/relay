# -*- coding: utf-8 -*-
"""tools/b731_bound_check.py -- b731, (R341)(3): THE FLOAT CONTROL OF Z_Q(3/2) < 4, PRINTED BEFORE ANY LEAN: a false step found here costs no dispatch. Written by the Write tool.
Floats and no proof. Prints: the lattice sum; the two pointwise steps of the row bound on a grid; the closed total the Lean route reaches.
  python -X utf8 -u tools/b731_bound_check.py [--bank]      --bank writes data/b731_bound_check.txt
"""
import math
import os
import sys
import time

R = 2.0 ** -1
D = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data')
RATIO = 1.38
RATIO_SQ = 1.239


def Q(m, n):
    return m * m + m * n + 6 * n * n


def lattice(r):
    s = 0.0
    for n in range(-r, r + 1):
        for m in range(-2 * r, 2 * r + 1):
            q = Q(m, n)
            if 0 < q <= r * r:
                s += q ** -1.5
    return s, 4 * math.pi / math.sqrt(23) / r


def G(a, x):
    return x / (a * a * math.sqrt(x * x + a * a))


def f(a, x):
    return (x * x + a * a) ** -1.5


def main(argv):
    L = ['b731 -- THE FLOAT CONTROL OF Z_Q(3/2) < 4, (R341)(3), BEFORE ANY LEAN (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### floats, no proof. The Lean route: n = 0 gives 2 zeta(3); each row n != 0 is bounded pointwise by r (G(x + 1/2) - G(x - 1/2)), G(x) = x / (A^2 sqrt(x^2 + A^2)), A^2 = 23 n^2 / 4, r = %.2f, which telescopes to 2 r / A^2.' % RATIO, '']
    L.append('## (1) THE LATTICE SUM, BY THE TRUNCATION Q <= R^2 AND THE TAIL 2 (2 pi / sqrt 23) / R')
    for r in (200, 800):
        s, t = lattice(r)
        L.append('  R %-5d partial %.6f tail %.6f total %.6f' % (r, s, t, s + t))
    L += ['', '## (2) THE POINTWISE STEP f(x) <= r (G(x + 1/2) - G(x - 1/2)), GRID x IN [-60, 60], STEP 1/8, A = sqrt(23) n / 2, n = 1..12']
    worst, bad = 0.0, 0
    for n in range(1, 13):
        a = math.sqrt(23) * n / 2
        for i in range(-480, 481):
            x = i / 8
            q = f(a, x) / (G(a, x + R) - G(a, x - R))
            worst = max(worst, q)
            bad += q > RATIO
    L.append('  the largest f / (G difference) %.6f ; points above r: %d' % (worst, bad))
    L += ['', '## (3) THE ALGEBRAIC STEP ((y + 1/2)^2 + A^2) <= %.3f (y^2 + A^2), y >= 0, A^2 >= 23/4, AND %.3f^3 <= %.2f^2' % (RATIO_SQ, RATIO_SQ, RATIO)]
    wr = max(((i / 100 + R) ** 2 + 5.75) / ((i / 100) ** 2 + 5.75) for i in range(0, 4000))
    L.append('  the largest ratio %.6f <= %.3f: %s ; %.6f <= %.6f: %s' % (wr, RATIO_SQ, wr <= RATIO_SQ, RATIO_SQ ** 3, RATIO ** 2, RATIO_SQ ** 3 <= RATIO ** 2))
    z3 = 1 + 1 / 8 + 1 / 27 + 1 / 24
    z2 = 1.645
    tot = 2 * z3 + RATIO * (16 / 23) * z2
    L += ['', '## (4) THE CLOSED TOTAL',
          '  zeta(3) <= 1 + 1/8 + 1/27 + 1/24 = %.6f (k^-3 <= (1/2)(1/((k-1)k) - 1/(k(k+1))) from k = 4), zeta(2) <= %.3f' % (z3, z2),
          '  2 zeta(3) + r (16/23) zeta(2) <= %.6f < 4: %s ; the margin %.6f' % (tot, tot < 4, 4 - tot), '',
          '### ### **Z_Q(3/2) ABOUT %.4f ; THE ROUTE`S TOTAL %.4f ; POINTWISE STEP HOLDS ON THE GRID %s.**' % (lattice(800)[0] + lattice(800)[1], tot, bad == 0)]
    print('\n'.join(L))
    if '--bank' in argv:
        with open(os.path.join(D, 'b731_bound_check.txt'), 'wb') as fh:
            fh.write(('\n'.join(L) + '\n').encode('utf-8'))
        print('written data/b731_bound_check.txt')


if __name__ == '__main__':
    main(sys.argv[1:])
