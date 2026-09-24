# -*- coding: utf-8 -*-
"""b511_families.py -- TWO FAMILIES INSIDE THE COMPILED CLASS. ### `python tools/b511_families.py fixture | run | report`

### THE WINDOW. For width a and B-spline order m: three uniform order-m B-spline bumps phi_L (knots evenly over [-L, L],
### integral 1, transform sinc(u h / 2)^m with h = 2L/m) at L = log(a^e), e in (1, 1/2, 1/4) -- the ladder's own three
### widths -- combined as g = phi_1 + c1 phi_2 + c2 phi_3 with c1, c2 solving INT g = 0 and INT g cosh(v/2) = 0 (the
### ladder's pole-annihilating construction, carried over). ### THE NOTCH: g_notch = PROD_j (1 + gamma_j^-2 d^2/dv^2) g,
### whose transform is g-hat(u) PROD_j (1 - u^2/gamma_j^2) -- zero at +-gamma_j, and still zero at 0 and at +-i/2.
### ### THE TEST FUNCTION IS k = g * g~ (g real and even, so g~ = g): k-hat = g-hat^2, EXACT IN CLOSED FORM, analytic,
### evaluated at real and complex arguments alike. ### k(x) itself, for the prime sums, by Gauss-Legendre on the pieces
### between the breakpoints of t -> g(t) g(x - t), exact for its polynomial degree, at two orders.
### ### THE CHAIN. Z, A, PR, P and the residual r = Z - (P - PR + A) exactly as b504's `cell` forms them, with b504's
### u-grids and banked kernels (`b504_kernels.npz`: the atlas kernel for xi, b326's derived kernel for Q0) and b325's
### LAMQ for Q0's finite channel -- the transform replaced by the closed form and nothing else.
### ### THE BOUND (sealed on the face): B = E_u + E_k + E_tail + E_round, where E_u is b504's u-grid term (half and wide
### grids), E_k the difference of the prime channel at two quadrature orders, E_tail the zero-side truncation above the
### bank's top priced by a majorant of |k-hat| against the zero density, and E_round the float floor, 4 eps times the sum
### of the absolute sizes of every term summed, plus the ordinates' own precision times |k-hat'|.
"""
import io
import json
import math
import os
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'e16'))
NL = chr(10)
EPS = 2.220446049250313e-16
OUT = os.path.join(D, 'b511_cells.jsonl')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import carto_atlas as AT        # noqa: E402
import b325_epstein as EP       # noqa: E402
import b503_zero as BZ          # noqa: E402

EXPS = (1.0, 0.5, 0.25)
KER = np.load(os.path.join(D, 'b504_kernels.npz'))
U_BASE = np.linspace(-AT.UMAX, AT.UMAX, AT.NU)
U_HALF = np.linspace(-AT.UMAX, AT.UMAX, 2 * AT.NU - 1)
U_WIDE = np.linspace(-2 * AT.UMAX, 2 * AT.UMAX, 2 * AT.NU - 1)
GAM = np.asarray(AT.GAM, dtype=np.float64)                  # xi: 10,000 ordinates, float-accurate
LIB = json.loads(io.open(os.path.join(D, 'b326_epstein_zeros.json'), encoding='utf-8').read())
GQ = np.sort(np.array([z['gamma_a'] for z in LIB['zeros']], dtype=np.float64))   # Q0 on-line, complete below 150 (b506)
C2 = json.loads(io.open(os.path.join(D, 'b506_c2_results.json'), encoding='utf-8').read())
OFFQ = [tuple(z['rho']) for z in C2['found'] if z.get('rho') and z['col'] == 'R']  # Q0's 17 off-line zeros, sigma > 1/2
DELTA_XI = 2.0 * EPS               # the xi bank's relative ordinate precision (float-accurate)
DELTA_Q = 6.1e-11                  # the Q0 bank's largest distance to its Newton zeros (b506)


def sinc(w):
    w = np.asarray(w, dtype=complex)
    out = np.ones_like(w)
    nz = np.abs(w) > 1e-12
    out[nz] = np.sin(w[nz]) / w[nz]
    return out


def nbs(m, x):
    """### the unit-knot cardinal B-spline N_m on [0, m] by the Cox-de Boor recursion, tabulated over shifts (O(m^2))."""
    x = np.asarray(x, dtype=float)
    B = [np.where((x - sft >= 0.0) & (x - sft < 1.0), 1.0, 0.0) for sft in range(m)]
    for j in range(2, m + 1):
        B = [((x - sft) * B[sft] + (j - (x - sft)) * B[sft + 1]) / (j - 1) for sft in range(m - j + 1)]
    return B[0]


def dnbs(m, d, x):
    """### D^d N_m(x) = SUM_j (-1)^j C(d, j) N_{m-d}(x - j) -- unit knots."""
    x = np.asarray(x, dtype=float)
    out = np.zeros_like(x)
    for j in range(d + 1):
        out = out + ((-1) ** j) * math.comb(d, j) * nbs(m - d, x - j)
    return out


class Window:
    """### one window: order m, width a, notch ordinates (possibly none)."""

    def __init__(self, a, m, notch=()):
        self.a, self.m, self.notch = a, m, tuple(float(x) for x in notch)
        self.L = [math.log(a ** e) for e in EXPS]
        self.h = [2.0 * Li / m for Li in self.L]
        I = [1.0, 1.0, 1.0]
        M = [float(np.real(self.phihat(i, 0.5j))) for i in range(3)]
        A2 = np.array([[I[1], I[2]], [M[1], M[2]]])
        c12 = np.linalg.solve(A2, np.array([-I[0], -M[0]]))
        self.c = np.array([1.0, c12[0], c12[1]])
        self.spl = []
        for i in range(3):
            kn = np.linspace(-self.L[i], self.L[i], m + 1)
            self.spl.append((None, self.h[i], kn))
        self.knots = np.unique(np.concatenate([s[2] for s in self.spl]))
        self.half = max(self.L)                  # g's support is [-half, half]; k's is [-2 half, 2 half]

    def phihat(self, i, z):
        return sinc(np.asarray(z) * self.h[i] / 2.0) ** self.m

    def notchfac(self, z):
        z = np.asarray(z, dtype=complex)
        f = np.ones_like(z)
        for gj in self.notch:
            f = f * (1.0 - z * z / (gj * gj))
        return f

    def ghat(self, z):
        z = np.asarray(z, dtype=complex)
        return (self.c[0] * self.phihat(0, z) + self.c[1] * self.phihat(1, z) + self.c[2] * self.phihat(2, z)) * self.notchfac(z)

    def khat(self, z):
        return self.ghat(z) ** 2

    def g(self, t):
        """### g_notch(t) = SUM_i c_i PROD_j (1 + gamma_j^-2 D^2) phi_i (t), by the B-splines' own derivatives."""
        t = np.asarray(t, dtype=float)
        # expand PROD_j (1 + x_j D^2) = SUM_r e_r D^{2r}, e_r the elementary symmetric sums of x_j = gamma_j^-2
        x = [1.0 / (gj * gj) for gj in self.notch]
        e = [1.0]
        for xj in x:
            e = [a + (xj * e[r - 1] if r >= 1 else 0.0) for r, a in enumerate(e + [0.0])]
        out = np.zeros_like(t)
        for i, (_b, h, kn) in enumerate(self.spl):
            y = (t - kn[0]) / h                      # ### phi_i(t) = N_m((t + L_i)/h_i) / h_i ; D_t = D_y / h
            for r, er in enumerate(e):
                if er == 0.0:
                    continue
                val = dnbs(self.m, 2 * r, y) / (h ** (2 * r))
                out = out + self.c[i] * er * val / h
        return out

    def k(self, xs, q):
        """### k(x) = INT g(t) g(x - t) dt, Gauss-Legendre of order q on each piece between breakpoints."""
        nodes, wts = np.polynomial.legendre.leggauss(q)
        out = []
        for x in np.atleast_1d(xs):
            bp = np.unique(np.concatenate([self.knots, x - self.knots]))
            lo, hi = max(-self.half, x - self.half), min(self.half, x + self.half)
            bp = bp[(bp >= lo) & (bp <= hi)]
            bp = np.unique(np.concatenate([[lo], bp, [hi]]))
            if hi <= lo:
                out.append(0.0)
                continue
            a0, b0 = bp[:-1], bp[1:]
            mid, rad = (a0 + b0) / 2.0, (b0 - a0) / 2.0
            tt = (mid[:, None] + rad[:, None] * nodes[None, :]).ravel()
            ww = (rad[:, None] * wts[None, :]).ravel()
            out.append(float(np.sum(ww * self.g(tt) * self.g(x - tt))))
        return np.array(out)


def primes_to(n):
    s = bytearray([1]) * (n + 1)
    s[0:2] = b'\x00\x00'
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(range(i * i, n + 1, i)))
    return [i for i in range(n + 1) if s[i]]


def prime_channel_xi(W, q):
    Lk = 2.0 * W.half
    ns, lp = [], []
    for p in primes_to(int(math.exp(Lk) + 1e-12)):
        j = 1
        while p ** j <= math.exp(Lk) + 1e-12:
            ns.append(p ** j)
            lp.append(math.log(p))
            j += 1
    if not ns:
        return 0.0, 0.0
    kv = W.k(np.log(np.array(ns, dtype=float)), q)
    terms = 2.0 * np.array(lp) / np.sqrt(ns) * kv
    return float(np.sum(terms)), float(np.sum(np.abs(terms)))


def prime_channel_q(W, q):
    Lk = 2.0 * W.half
    nmax = min(int(math.exp(Lk) + 1e-12), len(EP.LAMQ) - 1)
    ns = [n for n in range(2, nmax + 1) if EP.LAMQ[n] != 0.0]
    if not ns:
        return 0.0, 0.0
    kv = W.k(np.log(np.array(ns, dtype=float)), q)
    terms = 2.0 * np.array([EP.LAMQ[n] for n in ns]) / np.sqrt(ns) * kv
    return float(np.sum(terms)), float(np.sum(np.abs(terms)))


def arch(H, U, K):
    return float(np.trapezoid(H * K, U) / (2.0 * math.pi))


def majorant(W, t, imag=0.0):
    """### |k-hat(t + i s)| <= (SUM |c_i| (cosh(s h_i / 2) ...)^m ...)^2 -- a bound from |sin w| <= cosh(Im w)."""
    t = np.asarray(t, dtype=float)
    s = 0.0
    for i in range(3):
        w = t * W.h[i] / 2.0
        s = s + abs(W.c[i]) * (math.cosh(imag * W.h[i] / 2.0) * np.minimum(1.0, 1.0 / np.maximum(w, 1e-300))) ** W.m
    nf = np.ones_like(t)
    for gj in W.notch:
        nf = nf * (1.0 + (t * t + imag * imag) / (gj * gj))      # ### |1 - z^2/g^2| <= 1 + |z|^2/g^2, an upper bound
    return (s * nf) ** 2


def tail(W, top, density, imag=0.0):
    """### INT_top^inf 2 majorant(t) density(t) dt, trapezoid on a geometric grid to 1e8 top (the integrand falls at
    ### least as t^-8 log t, so the remainder beyond is below 1e-40 of the part kept)."""
    t = np.geomspace(top, top * 1e8, 200001)
    dens = (np.log(t / (2 * math.pi)) / (2 * math.pi)) if density is dens_xi else (np.log(t * math.sqrt(23) / (2 * math.pi)) / math.pi)
    f = 2.0 * majorant(W, t, imag) * dens
    return float(np.trapezoid(f, t))


def dens_xi(t):
    return math.log(t / (2 * math.pi)) / (2 * math.pi)


def dens_q(t):
    return math.log(t * math.sqrt(23) / (2 * math.pi)) / math.pi


def cell(a, m, notch_xi=(), notch_q=()):
    out = dict(a=a, m=m)
    for obj, notch in (('xi', notch_xi), ('q', notch_q)):
        W = Window(a, m, notch)
        Hb, Hh, Hw = W.khat(U_BASE).real, W.khat(U_HALF).real, W.khat(U_WIDE).real
        kz = 'z' if obj == 'xi' else 'qd'
        A = arch(Hb, U_BASE, KER[kz + '_base'])
        Eu = abs(arch(Hh, U_HALF, KER[kz + '_half']) - A) + abs(arch(Hw, U_WIDE, KER[kz + '_wide']) - A)
        q0 = W.m + 2
        if obj == 'xi':
            PR, PRabs = prime_channel_xi(W, q0)
            PR2, _ = prime_channel_xi(W, q0 + 6)
            G = GAM
            zt = 2.0 * W.khat(G).real
            Zon, Zoff = float(np.sum(zt)), 0.0
            offterms = []
            Etail = tail(W, float(G[-1]), dens_xi)
            dk = np.abs(2.0 * (W.khat(G * (1 + DELTA_XI)).real - W.khat(G).real))
        else:
            PR, PRabs = prime_channel_q(W, q0)
            PR2, _ = prime_channel_q(W, q0 + 6)
            G = GQ
            zt = 2.0 * W.khat(G).real
            Zon = float(np.sum(zt))
            offterms = []
            for b, gg in OFFQ:
                t = 0.0
                for rho in (complex(b, gg), complex(b, -gg), complex(1 - b, gg), complex(1 - b, -gg)):
                    t += float(W.khat((rho - 0.5) / 1j).real)
                offterms.append(t)
            Zoff = float(np.sum(offterms))
            Etail = tail(W, 150.0, dens_q, imag=0.5)
            dk = np.abs(2.0 * (W.khat(G + DELTA_Q).real - W.khat(G).real))
        P = float((W.khat(0.5j) + W.khat(-0.5j)).real)
        Z = Zon + Zoff
        r = Z - (P - PR + A)
        Ek = abs(PR - PR2)
        Aabs = float(np.trapezoid(np.abs(Hb * KER[kz + '_base']), U_BASE) / (2.0 * math.pi))
        Eround = 4.0 * EPS * (float(np.sum(np.abs(zt))) + float(np.sum(np.abs(offterms))) + Aabs + PRabs) + float(np.sum(dk))
        B = Eu + Ek + Etail + Eround
        nk = len(notch)
        notched = float(np.sum(zt[:nk])) if nk else 0.0
        out[obj] = dict(A=A, PR=PR, P=P, Z=Z, Z_on=Zon, Z_off=Zoff, m=A - PR, r=r, B=B, Eu=Eu, Ek=Ek, Etail=Etail,
                        Eround=Eround, verified=bool(abs(r) <= B), notched=notched, on_rest=Zon - notched,
                        low=[float(x) for x in zt[:6]], c=[float(x) for x in W.c], order=W.m)
    return out


def ladder():
    return [x['a'] for x in sorted(BZ.rows_all(), key=lambda r: r['a'])]


FAMILIES = [('bspline', 4, 0), ('notch1', 6, 1), ('notch3', 10, 3), ('notch5', 14, 5)]


def fixture():
    """### Component 0: the closed-form transform against a numerical integral of the window itself, one B-spline and one
    ### notch window; the numerical side integrates k(x) cos(u x) over k`s support by high-order Gauss-Legendre on k`s own
    ### breakpoints, with k(x) formed from g by its own quadrature -- a route that never touches the closed form."""
    res = []
    for fam, m, nk, a in (('bspline', 4, 0, 5.0), ('notch5', 14, 5, 5.0)):
        W = Window(a, m, tuple(GAM[:nk]))
        # k's breakpoints: pairwise sums of g's knots
        kb = np.unique(np.round((W.knots[:, None] + W.knots[None, :]).ravel(), 14))
        kb = kb[(kb >= -2 * W.half) & (kb <= 2 * W.half)]
        nodes, wts = np.polynomial.legendre.leggauss(24)
        a0, b0 = kb[:-1], kb[1:]
        mid, rad = (a0 + b0) / 2.0, (b0 - a0) / 2.0
        xx = (mid[:, None] + rad[:, None] * nodes[None, :]).ravel()
        ww = (rad[:, None] * wts[None, :]).ravel()
        kx = W.k(xx, m + 6)
        us = np.array([0.0, 1.0, 5.0, 14.134725141734695, 30.0, 60.0])
        num = np.array([float(np.sum(ww * kx * np.cos(u * xx))) for u in us])
        cf = W.khat(us).real
        res.append(dict(family=fam, a=a, m=m, notch=list(W.notch), u=us.tolist(), closed=cf.tolist(), numeric=num.tolist(),
                        maxdiff=float(np.max(np.abs(cf - num))), even=bool(abs(W.k([0.7], m + 2)[0] - W.k([-0.7], m + 2)[0]) < 1e-14),
                        pole=float(abs(W.khat(0.5j))), mean=float(abs(W.khat(0.0))), c=W.c.tolist()))
    io.open(os.path.join(D, 'b511_fixture.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    for r in res:
        print('  %-8s a=%.1f m=%d notch %s : max |closed - numeric| over %d u = %.2e ; even %s ; |k^(i/2)| %.1e ; |k^(0)| %.1e'
              % (r['family'], r['a'], r['m'], [round(x, 4) for x in r['notch']], len(r['u']), r['maxdiff'], r['even'], r['pole'], r['mean']))
    return 0


def run():
    A = ladder()
    done = set()
    if os.path.exists(OUT):
        done = {(json.loads(l)['family'], round(json.loads(l)['a'], 9)) for l in io.open(OUT, encoding='utf-8') if l.strip()}
    t0 = time.time()
    print('[%s] widths %d ; families %s' % (time.strftime('%H:%M:%S'), len(A), [f[0] for f in FAMILIES]), flush=True)
    for fam, m, nk in FAMILIES:
        for a in A:
            if (fam, round(a, 9)) in done:
                continue
            t1 = time.time()
            c = cell(a, m, tuple(GAM[:nk]), tuple(GQ[:nk]))
            c['family'], c['seconds'] = fam, round(time.time() - t1, 2)
            with io.open(OUT, 'a', encoding='utf-8', newline=NL) as fh:
                fh.write(json.dumps(c) + NL)
        print('[%s] %s done ; elapsed %.0f s' % (time.strftime('%H:%M:%S'), fam, time.time() - t0), flush=True)
    return 0


if __name__ == '__main__':
    sys.exit({'fixture': fixture, 'run': run}[sys.argv[1]]())
