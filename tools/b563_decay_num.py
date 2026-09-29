# -*- coding: utf-8 -*-
"""b563_decay_num.py -- COMPONENT 3'S ILLUSTRATION (the face's READING (4)). ### AN ILLUSTRATION, NOT EVIDENCE FOR A THEOREM.
### The excess E(ρ) = ∫ (s(u) - 1_{u<0}) P_n(u) e^{ρu} du of a member over the jump, by numpy Gauss-Legendre quadrature:
### SYMMETRIC s_δ(u) = st(1/2 - u/δ) st(δu + 2) (the face's family), ONE-SIDED s(u) = st(-u/δ) (b561's, left edge omitted),
### st = Real.smoothTransition. The far left (u < -2/δ) in closed form: ∫_{-∞}^{a} P e^{ρu} = e^{ρa} Σ_k (-1)^k P^(k)(a)/ρ^(k+1).
### ρ = 1/2 + iγ at the chain bank's first ordinate and γ = 100, 1000; and, HYPOTHETICAL POINTS (not zeros), β = 0.01 at
### γ = 14.134725, 100 to show the left edge as Re ρ -> 0. δ on a log grid in [1e-3, 1]. This file deletes nothing.
"""
import io, json, math, os, sys
import numpy as np
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def eng(x):
    x = np.asarray(x, float)
    out = np.zeros_like(x)
    m = x > 0
    out[m] = np.exp(-1.0 / x[m])
    return out


def st(x):
    a, b = eng(x), eng(1.0 - np.asarray(x, float))
    return a / (a + b)


def pcoef(n):
    return [math.comb(n, j + 1) / math.factorial(j) for j in range(n)]


def P(n, u, k=0):
    c = pcoef(n)
    out = np.zeros_like(np.asarray(u, float))
    for j in range(k, n):
        out = out + c[j] * (math.factorial(j) // math.factorial(j - k)) * np.asarray(u, float) ** (j - k)
    return out


X, W = np.polynomial.legendre.leggauss(64)


def gl(f, a, b, panels):
    edges = np.linspace(a, b, panels + 1)
    tot = 0j
    for lo, hi in zip(edges[:-1], edges[1:]):
        u = 0.5 * (hi - lo) * X + 0.5 * (hi + lo)
        tot += 0.5 * (hi - lo) * np.sum(W * f(u))
    return tot


def far_left(n, rho, a):
    return np.exp(rho * a) * sum((-1) ** k * P(n, np.array([a]), k)[0] / rho ** (k + 1) for k in range(n))


def E_sym(n, rho, d):
    gam = abs(rho.imag)
    pj = max(8, int(gam * d / (2 * math.pi) * 2) + 8)
    jump = gl(lambda u: (st(0.5 - u / d) - (u < 0)) * P(n, u) * np.exp(rho * u), -d / 2, d / 2, pj)
    L = 1.0 / d
    if rho.real * L > 700:
        left = 0j
    else:
        pl = max(8, int(gam * L / (2 * math.pi) * 2) + 8)
        left = gl(lambda u: (st(d * u + 2) - 1.0) * P(n, u) * np.exp(rho * u), -2 * L, -L, pl) - far_left(n, rho, -2 * L)
    return jump, left


def E_one(n, rho, d):
    gam = abs(rho.imag)
    pj = max(8, int(gam * d / (2 * math.pi) * 2) + 8)
    return gl(lambda u: (st(-u / d) - 1.0) * P(n, u) * np.exp(rho * u), -d, 0.0, pj)


def main():
    deltas = np.logspace(-3, 0, 31)
    L = ['=' * 112, 'b563 -- THE DECAY READ`S ILLUSTRATION. ### AN ILLUSTRATION, NOT EVIDENCE FOR A THEOREM.', '=' * 112,
         '### E = the member`s transform at gammaOf ρ minus the jump`s; 2 Re E the paired excess; δ over 31 points of [1e-3, 1].',
         '### SYM: sup_δ ‖ρ‖² |2 Re E| (jump side and left edge together) ; ONE: sup_δ ‖ρ‖ |2 Re E| of b561`s one-sided cut.', '',
         '    n  β       γ            sup ‖ρ‖²|2ReE| SYM   at δ       sup ‖ρ‖²|2ReE_left| SYM   sup ‖ρ‖|2ReE| ONE   sup ‖ρ‖²|2ReE| ONE']
    out = []
    for beta, gams, label in ((0.5, (14.134725, 100.0, 1000.0), 'zero-like'), (0.01, (14.134725, 100.0), 'HYPOTHETICAL')):
        for gam in gams:
            rho = complex(beta, gam)
            r = abs(rho)
            for n in (1, 2, 3):
                vs, vl, vo1, vo2, at = [], [], [], [], []
                for d in deltas:
                    j, l = E_sym(n, rho, d)
                    vs.append(r * r * abs(2 * (j + l).real))
                    vl.append(r * r * abs(2 * l.real))
                    e1 = E_one(n, rho, d)
                    vo1.append(r * abs(2 * e1.real))
                    vo2.append(r * r * abs(2 * e1.real))
                k = int(np.argmax(vs))
                row = dict(n=n, beta=beta, gamma=gam, sym=max(vs), at=float(deltas[k]), left=max(vl), one1=max(vo1), one2=max(vo2), label=label)
                out.append(row)
                L.append('    %d  %-6g  %-11.6g  %-22.6g %-10.4g %-25.6g %-19.6g %.6g%s' % (n, beta, gam, row['sym'], row['at'], row['left'], row['one1'], row['one2'],
                                                                                     '   (HYPOTHETICAL POINT)' if label == 'HYPOTHETICAL' else ''))
    L += ['', '### read: SYM`s sup ‖ρ‖² |2 Re E| stays of one size as γ grows at fixed n (the 1/‖ρ‖² decay, uniform in δ);',
          '### ONE`s ‖ρ‖² |2 Re E| grows with γ while its ‖ρ‖ |2 Re E| stays of one size (b561`s order n/‖ρ‖).', '=' * 112]
    io.open(os.path.join(D, 'b563_decay_num.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(out, io.open(os.path.join(D, 'b563_decay_num.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


if __name__ == '__main__':
    main()
