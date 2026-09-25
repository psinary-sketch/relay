# -*- coding: utf-8 -*-
"""b514_window.py -- THE MATCHED WINDOW. ### `python tools/b514_window.py fixture | matched | run`

### THE WINDOW (READING (1)). For width a: phi, one uniform cubic B-spline bump on [-L, L], L = log a, h = 2L/4, integral 1,
### phi-hat(z) = sinc(z h / 2)^4; g(u) = cos(gamma_0 u) phi(u); g-hat(z) = (phi-hat(z - gamma_0) + phi-hat(z + gamma_0)) / 2;
### k = g * g~ = g * g (g real and even); k-hat = g-hat^2, closed form at real and complex arguments. NO pole annihilation.
### THE CHAIN (READING (5)) is b511's `cell` with the window replaced: b511's grids, kernels, banks and prime channels are
### IMPORTED from `b511_families.py`, not copied. ### THE BOUND (READING (6)): B = E_u + E_k + E_tail + E_round, with the
### u > 1200 shortfall printed beside it and kept out of it.
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
import b511_families as F   # noqa: E402

NL = chr(10)
OUT = os.path.join(D, 'b514_cells.jsonl')
G0 = dict(xi=14.1347, q=16.290216)
QL, QH = 40, 60                                   # ### READING (6): the prime channel at two Gauss-Legendre orders
PAIR = min(F.OFFQ, key=lambda z: abs(z[1] - G0['q']))   # ### Q0's zero at 0.95326 + 16.29022 i (b506)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


class MWindow:
    """### g(u) = cos(gamma_0 u) phi(u), phi the cubic B-spline bump on [-log a, log a]."""

    def __init__(self, a, g0, m=4):
        self.a, self.g0, self.m = a, float(g0), m
        self.L = math.log(a)
        self.h = 2.0 * self.L / m
        self.knots = np.linspace(-self.L, self.L, m + 1)
        self.half = self.L

    def phihat(self, z):
        return F.sinc(np.asarray(z, dtype=complex) * self.h / 2.0) ** self.m

    def ghat(self, z):
        z = np.asarray(z, dtype=complex)
        return 0.5 * (self.phihat(z - self.g0) + self.phihat(z + self.g0))

    def khat(self, z):
        return self.ghat(z) ** 2

    def phi_d(self, t, d=0):
        y = (np.asarray(t, dtype=float) - self.knots[0]) / self.h
        return (F.nbs(self.m, y) if d == 0 else F.dnbs(self.m, d, y)) / (self.h ** (d + 1))

    def g(self, t):
        t = np.asarray(t, dtype=float)
        return np.cos(self.g0 * t) * self.phi_d(t)

    def g_d(self, t, d):
        """### D^d g by Leibniz: D^j cos(g0 t) = g0^j cos(g0 t + j pi / 2)."""
        t = np.asarray(t, dtype=float)
        out = np.zeros_like(t)
        for j in range(d + 1):
            out = out + math.comb(d, j) * (self.g0 ** j) * np.cos(self.g0 * t + j * math.pi / 2.0) * self.phi_d(t, d - j)
        return out

    def k(self, xs, q):
        """### k(x) = INT g(t) g(x - t) dt, Gauss-Legendre of order q on each piece between breakpoints."""
        nodes, wts = np.polynomial.legendre.leggauss(q)
        out = []
        for x in np.atleast_1d(xs):
            lo, hi = max(-self.half, x - self.half), min(self.half, x + self.half)
            if hi <= lo:
                out.append(0.0)
                continue
            bp = np.unique(np.concatenate([self.knots, x - self.knots]))
            bp = bp[(bp >= lo) & (bp <= hi)]
            bp = np.unique(np.concatenate([[lo], bp, [hi]]))
            a0, b0 = bp[:-1], bp[1:]
            mid, rad = (a0 + b0) / 2.0, (b0 - a0) / 2.0
            tt = (mid[:, None] + rad[:, None] * nodes[None, :]).ravel()
            ww = (rad[:, None] * wts[None, :]).ravel()
            out.append(float(np.sum(ww * self.g(tt) * self.g(x - tt))))
        return np.array(out)


def gamma_of(rho):
    return (rho - 0.5) / 1j


def images(b, gg):
    return (complex(b, gg), complex(b, -gg), complex(1 - b, gg), complex(1 - b, -gg))


def majorant(W, t, s=0.0):
    """### |k-hat(t + i s)| <= (SUM_+- cosh(s h/2)^4 min(1, 2/|(t -+ g0) h|)^4 / 2)^2, from |sinc(w)| <= cosh(Im w) min(1, 1/|Re w|)."""
    t = np.asarray(t, dtype=float)
    tot = 0.0
    for sg in (1.0, -1.0):
        w = np.abs(t - sg * W.g0) * W.h / 2.0
        tot = tot + (math.cosh(s * W.h / 2.0) * np.minimum(1.0, 1.0 / np.maximum(w, 1e-300))) ** W.m
    return (0.5 * tot) ** 2


def tail(W, top, obj):
    t = np.geomspace(top, top * 1e8, 200001)
    if obj == 'xi':
        dens, s = np.log(t / (2 * math.pi)) / (2 * math.pi), 0.0
    else:
        dens, s = np.log(t * math.sqrt(23) / (2 * math.pi)) / math.pi, 0.5
    return float(np.trapezoid(2.0 * majorant(W, t, s) * dens, t))


def shortfall(W, kz):
    """### READING (6): (1/2pi) INT_{|u| > 1200} majorant * |K(1200)| log u / log 1200 -- an ESTIMATE, out of B."""
    K1200 = float(abs(F.KER[kz + '_wide'][-1]))
    u = np.geomspace(1200.0, 1200.0 * 1e8, 200001)
    f = majorant(W, u) * K1200 * np.log(u) / math.log(1200.0)
    return float(2.0 * np.trapezoid(f, u) / (2.0 * math.pi))


def cell(a):
    out = dict(a=a)
    for obj in ('xi', 'q'):
        W = MWindow(a, G0[obj])
        kz = 'z' if obj == 'xi' else 'qd'
        Hb, Hh, Hw = W.khat(F.U_BASE).real, W.khat(F.U_HALF).real, W.khat(F.U_WIDE).real
        A = F.arch(Hb, F.U_BASE, F.KER[kz + '_base'])
        Eu = abs(F.arch(Hh, F.U_HALF, F.KER[kz + '_half']) - A) + abs(F.arch(Hw, F.U_WIDE, F.KER[kz + '_wide']) - A)
        chan = F.prime_channel_xi if obj == 'xi' else F.prime_channel_q
        PR, PRabs = chan(W, QL)
        PR2, _ = chan(W, QH)
        if obj == 'xi':
            G = F.GAM
            zt = 2.0 * W.khat(G).real
            Zon = float(np.sum(zt))
            ip = int(np.argmin(np.abs(G - G0['xi'])))
            pair, others, offterms, on_rest = float(zt[ip]), 0.0, [], Zon - float(zt[ip])
            Etail = tail(W, float(G[-1]), 'xi')
            dk = np.abs(2.0 * (W.khat(G * (1 + F.DELTA_XI)).real - W.khat(G).real))
            pair_kind = 'ON-LINE'
        else:
            G = F.GQ
            zt = 2.0 * W.khat(G).real
            Zon = float(np.sum(zt))
            offterms, pair = [], None
            for b, gg in F.OFFQ:
                t = float(sum(W.khat(gamma_of(r)).real for r in images(b, gg)))
                offterms.append(t)
                if (b, gg) == PAIR:
                    pair = t
            others = float(np.sum(offterms)) - pair
            on_rest = Zon
            Etail = tail(W, 150.0, 'q')
            dk = np.abs(2.0 * (W.khat(G + F.DELTA_Q).real - W.khat(G).real))
            pair_kind = 'OFF-LINE'
        P = float((W.khat(0.5j) + W.khat(-0.5j)).real)
        Z = Zon + float(np.sum(offterms))
        r = Z - (P - PR + A)
        Ek = abs(PR - PR2)
        Aabs = float(np.trapezoid(np.abs(Hb * F.KER[kz + '_base']), F.U_BASE) / (2.0 * math.pi))
        Eround = 4.0 * F.EPS * (float(np.sum(np.abs(zt))) + float(np.sum(np.abs(offterms))) + Aabs + PRabs) + float(np.sum(dk))
        B = Eu + Ek + Etail + Eround
        out[obj] = dict(gamma0=G0[obj], A=A, PR=PR, P=P, Z=Z, Z_on=Zon, pair=pair, pair_kind=pair_kind, others=others,
                        on_rest=on_rest, share=abs(pair) / on_rest if on_rest else None, m=A - PR, h2=P - PR + A, r=r, B=B,
                        Eu=Eu, Ek=Ek, Etail=Etail, Eround=Eround, shortfall=shortfall(W, kz), verified=bool(abs(r) <= B))
    return out


def fixture():
    """### READING (7): the closed form against INT k(x) cos(u x) dx, k from g by its own quadrature; at a = 5, each gamma_0."""
    res = []
    for obj in ('xi', 'q'):
        W = MWindow(5.0, G0[obj])
        kb = np.unique(np.round((W.knots[:, None] + W.knots[None, :]).ravel(), 14))
        kb = kb[(kb >= -2 * W.half) & (kb <= 2 * W.half)]
        nodes, wts = np.polynomial.legendre.leggauss(80)
        a0, b0 = kb[:-1], kb[1:]
        mid, rad = (a0 + b0) / 2.0, (b0 - a0) / 2.0
        xx = (mid[:, None] + rad[:, None] * nodes[None, :]).ravel()
        ww = (rad[:, None] * wts[None, :]).ravel()
        kx = W.k(xx, QH)
        G = F.GAM if obj == 'xi' else F.GQ
        near = sorted(G[np.argsort(np.abs(G - G0[obj]))[:3]].tolist())
        near = [x for x in near if abs(x - G0[obj]) > 1e-3][:2]
        us = np.array([0.0, 1.0, G0[obj]] + near + [30.0, 60.0])
        num = np.array([float(np.sum(ww * kx * np.cos(u * xx))) for u in us])
        cf = W.khat(us).real
        eps = 1e-9
        jumps = {}
        for d in (0, 1, 2, 3):
            jk = [abs(float(W.g_d([x + eps], d)[0] - W.g_d([x - eps], d)[0])) for x in W.knots[1:-1]]
            jumps['D%d' % d] = max(jk)
        res.append(dict(object=obj, a=5.0, gamma0=G0[obj], u=us.tolist(), closed=cf.tolist(), numeric=num.tolist(),
                        maxdiff=float(np.max(np.abs(cf - num))), bar=1e-10, meets=bool(np.max(np.abs(cf - num)) <= 1e-10),
                        even=float(abs(W.k([0.7], QH)[0] - W.k([-0.7], QH)[0])), knot_jumps=jumps,
                        support=[-2 * W.half, 2 * W.half], generating_h='g(u) = cos(%s u) * phi_[-log 5, log 5](u)' % G0[obj]))
    io.open(os.path.join(D, 'b514_fixture.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    for r in res:
        print('  %-3s gamma0 %.6f : max |closed - numeric| over %d u = %.2e (bar 1e-10: %s) ; |k(.7) - k(-.7)| %.1e ; knot jumps %s'
              % (r['object'], r['gamma0'], len(r['u']), r['maxdiff'], r['meets'], r['even'],
                 {k: '%.1e' % v for k, v in r['knot_jumps'].items()}))
    return 0


def matched():
    """### READING (8): k-hat at gamma_0, at gammaOf rho (Q0), at the two nearest on-line ordinates; three ladder widths."""
    A = F.ladder()
    res = []
    for a in (A[0], A[59], A[118]):
        for obj in ('xi', 'q'):
            W = MWindow(a, G0[obj])
            G = F.GAM if obj == 'xi' else F.GQ
            near = [x for x in G[np.argsort(np.abs(G - G0[obj]))[:3]].tolist() if abs(x - G0[obj]) > 1e-3][:2]
            v0 = complex(W.khat(G0[obj]))
            vn = [complex(W.khat(x)) for x in near]
            row = dict(a=a, object=obj, gamma0=G0[obj], at_gamma0=[v0.real, v0.imag], nearest=near,
                       at_nearest=[[v.real, v.imag] for v in vn], ratio=abs(v0) / max(abs(v) for v in vn))
            if obj == 'q':
                vr = complex(W.khat(gamma_of(complex(*PAIR))))
                row['gammaOf_rho'] = [gamma_of(complex(*PAIR)).real, gamma_of(complex(*PAIR)).imag]
                row['at_gammaOf_rho'] = [vr.real, vr.imag]
            res.append(row)
            print('  a=%-9.6f %-3s k^(g0) %+.4e ; nearest %s -> %s ; ratio %.3e%s'
                  % (a, obj, v0.real, ['%.4f' % x for x in near], ['%+.3e' % v.real for v in vn], row['ratio'],
                     (' ; k^(gammaOf rho) %+.4e %+.4ei' % tuple(row['at_gammaOf_rho'])) if obj == 'q' else ''))
    io.open(os.path.join(D, 'b514_matched.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    return 0


def run():
    A = F.ladder()
    done = set()
    if os.path.exists(OUT):
        done = {round(json.loads(l)['a'], 9) for l in io.open(OUT, encoding='utf-8') if l.strip()}
    t0 = time.time()
    print('[%s] widths %d ; pair %s' % (time.strftime('%H:%M:%S'), len(A), PAIR), flush=True)
    for i, a in enumerate(A):
        if round(a, 9) in done:
            continue
        t1 = time.time()
        c = cell(a)
        c['seconds'] = round(time.time() - t1, 2)
        with io.open(OUT, 'a', encoding='utf-8', newline=NL) as fh:
            fh.write(json.dumps(c) + NL)
        if i % 20 == 0:
            print('[%s] %d/%d a=%.4f ; elapsed %.0f s' % (time.strftime('%H:%M:%S'), i + 1, len(A), a, time.time() - t0), flush=True)
    print('[%s] done ; elapsed %.0f s' % (time.strftime('%H:%M:%S'), time.time() - t0), flush=True)
    return 0


if __name__ == '__main__':
    sys.exit({'fixture': fixture, 'matched': matched, 'run': run}[sys.argv[1]]())
