# -*- coding: utf-8 -*-
r"""b630_nb_bench.py -- THE NYMAN–BEURLING DISTANCES d_N² IN ARB BALLS, UNDER (R240)(6). A T3/T4 BENCH WITH NO CLAIM.

### THE OBJECT. The kernel's d_N (SIDE-explicit-formula v0.24, NymanBeurling.lean :94): the distance in L²(0, 1) from the constant 1
### to the span of rho(1/n), n = 1 … N, where rho θ is the class of rhoFun θ x = {θ/x} − θ{1/x} (:41). rho(1/1) is the zero function,
### so the span is that of n = 2 … N, and d_1 = 1. d_N² = 1 − bᵀ G⁻¹ b, G the Gram matrix of rho(1/n), n = 2 … N, and b their inner
### products with 1: the minimisation as a linear solve (arb_mat.solve, in balls).
### THE INNER PRODUCTS, IN CLOSED FORM PER PIECE. With t = 1/x on (1, ∞), dx = dt/t², rho(1/n) reads u_n(t) = {t/n} − {t}/n, and
###   J(a)   = ∫_1^∞ {t/a} t⁻² dt = (log a + 1 − γ)/a,
###   I(a,b) = ∫_1^∞ {t/a}{t/b} t⁻² dt = (1/g)[(1 − 1/g)/(a'b') + I(a',b')],  g = gcd(a,b), a = g a', b = g b'.
### For coprime a, b the integrand F(t) = {t/a}{t/b} has period L = ab and is a quadratic on each piece between consecutive multiples
### of a or b, so I(a,b) = ∫_1^L F t⁻² dt + L⁻² ∫_0^L F(s) ψ'(1 + s/L) ds, the second term the periods beyond the first summed. Per piece
### the first is elementary (a quadratic over t², logarithms) and the second is [e₂A₂ + e₁A₁ + e₀A₀] at its ends in z = 1 + s/L, with
###   A₀ = ψ(z), A₁ = zψ(z) − lnΓ(z), A₂ = z²ψ(z) − 2 ln G(1 + z) + z(1 − z) + z log 2π,
### G Barnes' function (acb.log_barnes_g); each Aₖ' = zᵏψ'(z). The fixtures check each against acb.integral, Arb's own rigorous
### integrator, on pieces of three pairs, and I(1,1) against log 2π − 1 − γ.
### THE NUMBERS PRINTED. Per N: d_N² as midpoint and radius, d_N² · log N, the conditioning of G (the ∞-norm product of the midpoint
### matrix and its ball inverse, as log10), and whether the ball keeps six certified digits (rad ≤ 10⁻⁶ · |mid|). N_max is the largest
### N ≤ N_CAP at which it does. Beside them the kernel's 2λ₁ (Keiper.lean :239 at v0.20) in balls, with 2 + γ − log 4π as a check.
### The output carries no clock: two runs are compared byte for byte.
### Usage: python tools/b630_nb_bench.py selftest | run <out-file>
"""
import io
import os
import sys
import time
from math import gcd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
from flint import acb, arb, arb_mat, ctx  # noqa: E402

import b630_worklist as K  # noqa: E402

ctx.prec = K.PREC
NL = chr(10)
GAMMA = arb.const_euler()
LOG2PI = (2 * arb.pi()).log()
_ZC = {}


def _special(z):
    """### ψ(z), lnΓ(z), ln G(1 + z) for a real ball z ≥ 1, cached by the exact rational the caller passes."""
    k = z.mid().str(60, radius=False)
    if k not in _ZC:
        _ZC[k] = (z.digamma(), z.lgamma(), acb(z + 1).log_barnes_g().real)
    return _ZC[k]


def A(k, z):
    psi, lg, lbg = _special(z)
    if k == 0:
        return psi
    if k == 1:
        return z * psi - lg
    return z * z * psi - 2 * lbg + z * (1 - z) + z * LOG2PI


def pieces(a, b):
    """### the breakpoints of {t/a}{t/b} on [0, ab] for coprime a, b: every multiple of a or of b."""
    L = a * b
    return sorted(set(list(range(0, L + 1, a)) + list(range(0, L + 1, b))))


def coeffs(a, b, p, q):
    """### F = c2 t² + c1 t + c0 on the piece (p, q): i = ⌊t/a⌋, j = ⌊t/b⌋ there."""
    i, j = p // a, p // b   # ### p is a breakpoint: on (p, q) the floors are those at p
    return arb(1) / (a * b), -(arb(i) / b + arb(j) / a), arb(i * j)


def I_coprime(a, b):
    L = a * b
    br = pieces(a, b)
    s1, s2 = arb(0), arb(0)
    for p, q in zip(br, br[1:]):
        c2, c1, c0 = coeffs(a, b, p, q)
        if q > 1:
            pp = max(p, 1)
            s1 += c2 * (q - pp) + c1 * (arb(q) / pp).log() + c0 * (arb(1) / pp - arb(1) / q)
        e2 = c2 * L * L
        e1 = -2 * c2 * L * L + c1 * L
        e0 = c2 * L * L - c1 * L + c0
        zp, zq = 1 + arb(p) / L, 1 + arb(q) / L
        s2 += L * (e2 * (A(2, zq) - A(2, zp)) + e1 * (A(1, zq) - A(1, zp)) + e0 * (A(0, zq) - A(0, zp)))
    return s1 + s2 / (L * L)


_IC = {}


def I(a, b):
    g = gcd(a, b)
    a1, b1 = min(a, b) // g, max(a, b) // g
    if (a1, b1) not in _IC:
        _IC[(a1, b1)] = I_coprime(a1, b1)
    return (_IC[(a1, b1)] + (1 - arb(1) / g) / (a1 * b1)) / g


def J(a):
    return (arb(a).log() + 1 - GAMMA) / a


def gram(n_cap):
    idx = list(range(2, n_cap + 1))
    G = arb_mat(len(idx), len(idx))
    bv = arb_mat(len(idx), 1)
    I11 = I(1, 1)
    for x, m in enumerate(idx):
        bv[x, 0] = J(m) - J(1) / m
        for y, n in enumerate(idx):
            if y < x:
                G[x, y] = G[y, x]
                continue
            G[x, y] = I(m, n) - I(m, 1) / n - I(1, n) / m + I11 / (m * n)
    return G, bv


def sub(M, k, cols=None):
    cols = k if cols is None else cols
    S = arb_mat(k, cols)
    for i in range(k):
        for j in range(cols):
            S[i, j] = M[i, j]
    return S


def norm_inf(M):
    return max(sum(abs(float(M[i, j].mid())) for j in range(M.ncols())) for i in range(M.nrows()))


def s(x, n=20):
    return x.mid().str(n, radius=False)


def r(x):
    return x.rad().str(3, radius=False)


def run():
    G, bv = gram(K.N_CAP)
    lam1 = 1 + GAMMA / 2 - (4 * arb.pi()).log() / 2
    two = 2 * lam1
    chk = 2 + GAMMA - (4 * arb.pi()).log()
    L = ['# b630 -- THE NYMAN–BEURLING DISTANCES d_N² IN ARB BALLS (tools/b630_nb_bench.py), working precision %d bits, N = 1 … %d' % (
        K.PREC, K.N_CAP),
         '# 2λ₁ = 2(1 + γ/2 − ½ log 4π) = %s +/- %s ; 2 + γ − log 4π = %s +/- %s ; difference contains 0: %s' % (
             s(two, 30), r(two), s(chk, 30), r(chk), (two - chk).contains(0)),
         '# I(1,1) = %s +/- %s ; log 2π − 1 − γ = %s' % (s(I(1, 1), 30), r(I(1, 1)), s(LOG2PI - 1 - GAMMA, 30)),
         '# columns: N | d_N² (mid) | radius | d_N² · log N (mid) | radius | above 2λ₁ (certified) | log10 cond∞(G_N) | six digits']
    rows = []
    for N in range(1, K.N_CAP + 1):
        if N == 1:
            d2, cond = arb(1), 0.0
        else:
            k = N - 1
            Gk, bk = sub(G, k), sub(bv, k, 1)
            c = Gk.solve(bk)
            d2 = 1 - sum((bk[i, 0] * c[i, 0] for i in range(k)), arb(0))
            Gi = Gk.inv()
            cond = norm_inf(Gk) * norm_inf(Gi)
        prod = d2 * arb(N).log()
        six = d2.rad() <= arb(10) ** (-K.REL_DIGITS) * abs(d2.mid())
        above = (prod - two) > 0
        rows.append((N, d2, prod, above, cond, six))
        L.append('%d | %s | %s | %s | %s | %s | %.2f | %s' % (N, s(d2), r(d2), s(prod), r(prod), 'yes' if above else 'no',
                                                           __import__('math').log10(cond) if cond > 0 else 0.0, 'yes' if six else 'no'))
    nmax = max([N for N, d2, prod, above, cond, six in rows if six] or [0])
    mono = [N for (N, d2, _p, _a, _c, _s), (N2, e2, _p2, _a2, _c2, _s2) in zip(rows, rows[1:]) if not (d2 - e2 >= 0)]
    L.append('# N_max (the largest N <= %d whose ball keeps six certified digits): %d' % (K.N_CAP, nmax))
    L.append('# the steps N -> N+1 whose decrease is not certified (d_N² − d_{N+1}² ≥ 0 not certified), N < N_max: %s' % (
        [N for N in mono if N < nmax] or 'NONE'))
    L.append('# N >= 2 with N <= N_max whose d_N² · log N is not certified above 2λ₁: %s' % (
        [N for N, d2, prod, above, cond, six in rows if 2 <= N <= nmax and not above] or 'NONE'))
    return NL.join(L) + NL


def selftest():
    """### fixtures before use: the closed forms against acb.integral on pieces of three pairs; I(1,1) against log 2π − 1 − γ; J(2)
    ### against the piece method; the cost of one pair timed."""
    ok = []

    def want(label, cond):
        ok.append(bool(cond))
        print('  %-104s %s' % (label, 'PASS' if cond else '### FAIL'))

    for a, b in ((1, 1), (2, 3), (3, 7)):
        L = a * b
        br = pieces(a, b)
        worst = arb(0)
        for p, q in list(zip(br, br[1:]))[:6]:
            c2, c1, c0 = coeffs(a, b, p, q)
            e2, e1, e0 = c2 * L * L, -2 * c2 * L * L + c1 * L, c2 * L * L - c1 * L + c0
            zp, zq = 1 + arb(p) / L, 1 + arb(q) / L
            closed = L * (e2 * (A(2, zq) - A(2, zp)) + e1 * (A(1, zq) - A(1, zp)) + e0 * (A(0, zq) - A(0, zp)))
            f = lambda t, _: (acb(c2) * t * t + acb(c1) * t + acb(c0)) * (1 + t / L).polygamma(1)
            num = acb.integral(f, p, q).real
            worst = max(worst, abs(closed - num).upper(), key=lambda x: float(x.mid()))
        want('(1) the trigamma pieces of (%d,%d) in closed form against acb.integral, worst difference %s' % (a, b, worst.str(3)),
             float(worst.mid()) < 1e-25)
    want('(2) I(1,1) = %s against log 2π − 1 − γ = %s' % (s(I(1, 1), 25), s(LOG2PI - 1 - GAMMA, 25)),
         (I(1, 1) - (LOG2PI - 1 - GAMMA)).contains(0) and I(1, 1).rad() < arb(10) ** -30)
    t0 = time.time()
    v = I_coprime(13, 97)
    secs = time.time() - t0
    want('(3) one coprime pair (13, 97), 110 pieces, in %.2f s: %s +/- %s' % (secs, s(v, 15), r(v)), v.rad() < arb(10) ** -25)
    want('(4) I(a,b) symmetric: I(4,6) = I(6,4)', (I(4, 6) - I(6, 4)).contains(0))
    g15 = I(1, 5) - I(1, 1) / 5 - I(1, 5) / 1 + I(1, 1) / 5
    b1 = J(1) - J(1) / 1
    want('(5) rho(1/1) is zero: its Gram entry against n = 5 reads %s and its b entry %s, each a ball containing 0' % (g15.str(3), b1.str(3)),
         g15.contains(0) and b1.contains(0))
    n = sum(ok)
    print('  ### %d of %d cases as wanted -- %s' % (n, len(ok), 'PASS' if n == len(ok) else 'FAIL'))
    return 0 if n == len(ok) else 1


if __name__ == '__main__':
    if sys.argv[1:2] == ['selftest']:
        sys.exit(selftest())
    if sys.argv[1:2] == ['run'] and len(sys.argv) == 3:
        t0 = time.time()
        out = run()
        io.open(sys.argv[2], 'w', encoding='utf-8', newline='\n').write(out)
        sys.stderr.write('### written %s (%d bytes) in %d s\n' % (sys.argv[2], len(out.encode('utf-8')), int(time.time() - t0)))
        sys.exit(0)
    print('usage: b630_nb_bench.py selftest | run <out-file>')
    sys.exit(2)
