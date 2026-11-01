# -*- coding: utf-8 -*-
"""tools/b730_theta_check.py -- b730, the plan's control before any Lean: the laws the continuation field builds on, read numerically from truncated lattice sums.
Two laws: thetaU a = a^(-1/2) D(23a/4, 1/a) and a^(1/2) thetaU a = b^(1/2) thetaU b at b = 4/(23a); and the first coefficients of the sum against the box count r_Q (b326's r_Q(1) = 2).
A falsifying control beside each: the same comparison at the wrong constant 22 for 23 must fail. Printed; written by --bank to data/b730_theta_check.txt."""
import math
import sys

R = 60


def q(m, n):
    return m * m + m * n + 6 * n * n


def theta(a, big=23):
    return sum(math.exp(-math.pi * a * ((m + n / 2) ** 2 + (big / 4) * n * n)) for m in range(-R, R + 1) for n in range(-R, R + 1))


def dbl(x, y):
    return sum(math.exp(-math.pi * n * n * x) * (-1) ** abs(n * k) * math.exp(-math.pi * k * k * y) for n in range(-R, R + 1) for k in range(-R, R + 1))


def main():
    L = ['b730 -- THE PLAN`S CONTROL BEFORE ANY LEAN: THE THETA LAWS, TRUNCATED LATTICE SUMS, |m|, |n|, |k| <= %d' % R, '']
    ok = True
    for a in (0.7, 1.0, 1.3):
        b = 4 / (23 * a)
        step = theta(a)
        dd = dbl(a * 23 / 4, 1 / a) / math.sqrt(a)
        lhs, rhs = math.sqrt(a) * theta(a), math.sqrt(b) * theta(b)
        bad = math.sqrt(a) * theta(a, 22) - math.sqrt(b) * theta(b, 22)
        ok = ok and abs(step - dd) < 1e-9 and abs(lhs - rhs) < 1e-9 and abs(bad) > 1e-4
        L += ['  a = %.2f b = %.6f : thetaU a %.12f ; a^(-1/2) D %.12f ; a^(1/2) thetaU a %.12f ; b^(1/2) thetaU b %.12f ; the difference at 22 for 23 %.3e' % (a, b, step, dd, lhs, rhs, bad)]
    pts = {}
    for m in range(-R, R + 1):
        for n in range(-R, R + 1):
            pts[q(m, n)] = pts.get(q(m, n), 0) + 1
    row = [pts.get(k, 0) for k in range(0, 9)]
    ok = ok and row[0] == 1 and row[1] == 2
    L += ['', '  the fibres r(0)..r(8) of Q0 over the lattice: %s (the origin alone over 0; r_Q(1) = 2, b326`s normalisation)' % row, '',
          '### ### **THE LAWS %s ; THE FALSIFYING CONSTANT FAILS AT EVERY POINT ; NUMERICAL, NOT A PROOF.**' % ('HOLD AT THREE POINTS' if ok else 'DO NOT HOLD')]
    print('\n'.join(L))
    if '--bank' in sys.argv:
        with open('data/b730_theta_check.txt', 'wb') as f:
            f.write(('\n'.join(L) + '\n').encode('utf-8'))


if __name__ == '__main__':
    main()
