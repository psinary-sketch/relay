# -*- coding: utf-8 -*-
"""b515_window.py -- THE WINDOW WITH A ZERO AT THE ON-LINE POINT. ### `python tools/b515_window.py fixture | matched | run`

### THE WINDOW (READING (1)). phi, a uniform B-spline bump of order M = 6 on [-L, L], L = log a, spacing s = 2L/M, integral 1,
### phi-hat(z) = sinc(z s / 2)^M; h = phi'' + gamma_0^2 phi, C^2 because phi is C^(M-2) = C^4; in the kernel's convention
### INT f(u) e^{izu} du, (phi'')-hat(z) = -z^2 phi-hat(z), so h-hat(z) = (gamma_0^2 - z^2) phi-hat(z), zero at z = gamma_0 with
### slope -2 gamma_0 phi-hat(gamma_0). k = h * h~ = h * h (h real and even); k-hat = h-hat^2 in closed form. No pole
### annihilation. ### THE CHAIN is b511's `cell` with the window replaced, as at b514: b511's grids, kernels, banks and
### prime channels IMPORTED from `b511_families.py`, b514's split and bound IMPORTED from `b514_window.py`'s helpers where
### they carry over (gammaOf, images), not copied.
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
import b514_window as B14   # noqa: E402

NL = chr(10)
OUT = os.path.join(D, 'b515_cells.jsonl')
G0 = dict(xi=14.1347, q=16.290216)
M = 6                                             # ### READING (1): order 6, so phi is C^4 and h = phi'' + g0^2 phi is C^2
QL, QH = 12, 18                                   # ### READING (6): h is piecewise polynomial of degree 5; both orders exceed exactness
PAIR = B14.PAIR
DELTA = PAIR[0] - 0.5
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


class ZWindow:
    """### h = phi'' + gamma_0^2 phi, phi the order-M B-spline bump on [-log a, log a]."""

    def __init__(self, a, g0, m=M):
        self.a, self.g0, self.m = a, float(g0), m
        self.L = math.log(a)
        self.h = 2.0 * self.L / m                 # ### the knot spacing (b511's name for it)
        self.knots = np.linspace(-self.L, self.L, m + 1)
        self.half = self.L

    def phihat(self, z):
        return F.sinc(np.asarray(z, dtype=complex) * self.h / 2.0) ** self.m

    def ghat(self, z):
        z = np.asarray(z, dtype=complex)
        return (self.g0 ** 2 - z * z) * self.phihat(z)

    def khat(self, z):
        return self.ghat(z) ** 2

    def slope(self):
        return float((-2.0 * self.g0 * self.phihat(self.g0)).real)

    def phi_d(self, t, d=0):
        y = (np.asarray(t, dtype=float) - self.knots[0]) / self.h
        return (F.nbs(self.m, y) if d == 0 else F.dnbs(self.m, d, y)) / (self.h ** (d + 1))

    def g(self, t):
        return self.phi_d(t, 2) + self.g0 ** 2 * self.phi_d(t, 0)

    def g_d(self, t, d):
        return self.phi_d(t, d + 2) + self.g0 ** 2 * self.phi_d(t, d)

    def k(self, xs, q):
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


def majorant(W, t, s=0.0):
    """### |k-hat(t + is)| <= ((g0^2 + t^2 + s^2) (cosh(s h/2) min(1, 2/(|t| h)))^M)^2, from |sinc(w)| <= cosh(Im w) min(1, 1/|Re w|)."""
    t = np.asarray(t, dtype=float)
    w = np.abs(t) * W.h / 2.0
    ph = (math.cosh(s * W.h / 2.0) * np.minimum(1.0, 1.0 / np.maximum(w, 1e-300))) ** W.m
    return ((W.g0 ** 2 + t * t + s * s) * ph) ** 2


def tail(W, top, obj):
    t = np.geomspace(top, top * 1e8, 200001)
    if obj == 'xi':
        dens, s = np.log(t / (2 * math.pi)) / (2 * math.pi), 0.0
    else:
        dens, s = np.log(t * math.sqrt(23) / (2 * math.pi)) / math.pi, 0.5
    return float(np.trapezoid(2.0 * majorant(W, t, s) * dens, t))


def shortfall(W, kz):
    K1200 = float(abs(F.KER[kz + '_wide'][-1]))
    u = np.geomspace(1200.0, 1200.0 * 1e8, 200001)
    f = majorant(W, u) * K1200 * np.log(u) / math.log(1200.0)
    return float(2.0 * np.trapezoid(f, u) / (2.0 * math.pi))


def cell(a):
    out = dict(a=a)
    for obj in ('xi', 'q'):
        W = ZWindow(a, G0[obj])
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
                t = float(sum(W.khat(B14.gamma_of(r)).real for r in B14.images(b, gg)))
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
        rest = Z - pair
        out[obj] = dict(gamma0=G0[obj], A=A, PR=PR, P=P, Z=Z, Z_on=Zon, pair=pair, pair_kind=pair_kind, others=others,
                        on_rest=on_rest, rest=rest, ratio=pair / rest if rest else None, m=A - PR, h2=P - PR + A, r=r, B=B,
                        Eu=Eu, Ek=Ek, Etail=Etail, Eround=Eround, shortfall=shortfall(W, kz), verified=bool(abs(r) <= B),
                        slope=W.slope(), growth=math.exp(2.0 * DELTA * W.L))
    return out


def fixture():
    """### READING (7): the closed form against INT k(x) cos(u x) dx, k from h by its own quadrature; at a = 5, each gamma_0."""
    res = []
    for obj in ('xi', 'q'):
        W = ZWindow(5.0, G0[obj])
        kb = np.unique(np.round((W.knots[:, None] + W.knots[None, :]).ravel(), 14))
        kb = kb[(kb >= -2 * W.half) & (kb <= 2 * W.half)]
        nodes, wts = np.polynomial.legendre.leggauss(24)
        a0, b0 = kb[:-1], kb[1:]
        mid, rad = (a0 + b0) / 2.0, (b0 - a0) / 2.0
        xx = (mid[:, None] + rad[:, None] * nodes[None, :]).ravel()
        ww = (rad[:, None] * wts[None, :]).ravel()
        kx = W.k(xx, QH)
        G = F.GAM if obj == 'xi' else F.GQ
        near = [x for x in G[np.argsort(np.abs(G - G0[obj]))[:3]].tolist() if abs(x - G0[obj]) > 1e-3][:2]
        us = np.array([0.0, 1.0, G0[obj]] + sorted(near) + [30.0, 60.0])
        num = np.array([float(np.sum(ww * kx * np.cos(u * xx))) for u in us])
        cf = W.khat(us).real
        scale = float(np.max(np.abs(cf)))
        eps = 1e-9
        jumps = {}
        for d in (0, 1, 2, 3):
            jk = [abs(float(W.g_d([x + eps], d)[0] - W.g_d([x - eps], d)[0])) for x in W.knots[1:-1]]
            jumps['D%d' % d] = max(jk)
        res.append(dict(object=obj, a=5.0, gamma0=G0[obj], order=W.m, u=us.tolist(), closed=cf.tolist(), numeric=num.tolist(),
                        maxdiff=float(np.max(np.abs(cf - num))), scale=scale, bar=1e-10, meets=bool(np.max(np.abs(cf - num)) <= 1e-10),
                        even=float(abs(W.k([0.7], QH)[0] - W.k([-0.7], QH)[0])), knot_jumps=jumps, support=[-2 * W.half, 2 * W.half],
                        generating_h='h(u) = phi``(u) + %s^2 phi(u), phi the order-%d B-spline on [-log 5, log 5]' % (G0[obj], W.m)))
    io.open(os.path.join(D, 'b515_fixture.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    for r in res:
        print('  %-3s gamma0 %.6f order %d : max |closed - numeric| over %d u = %.2e (scale %.2e ; bar 1e-10: %s) ; |k(.7) - k(-.7)| %.1e ; knot jumps %s'
              % (r['object'], r['gamma0'], r['order'], len(r['u']), r['maxdiff'], r['scale'], r['meets'], r['even'],
                 {k: '%.1e' % v for k, v in r['knot_jumps'].items()}))
    return 0


def matched():
    """### READING (8): h-hat on the line at gamma_0 (the control, must read 0), its slope, and at the two nearest on-line ordinates."""
    A = F.ladder()
    res = []
    for a in (A[0], A[59], A[118]):
        for obj in ('xi', 'q'):
            W = ZWindow(a, G0[obj])
            G = F.GAM if obj == 'xi' else F.GQ
            near = sorted(x for x in G[np.argsort(np.abs(G - G0[obj]))[:3]].tolist() if abs(x - G0[obj]) > 1e-3)[:2]
            v0 = complex(W.ghat(G0[obj]))
            num_slope = float(((W.ghat(G0[obj] + 1e-6) - W.ghat(G0[obj] - 1e-6)) / 2e-6).real)
            vn = [complex(W.ghat(x)) for x in near]
            peak = float(np.max(np.abs(W.ghat(np.linspace(0, 60, 6001)))))
            row = dict(a=a, object=obj, gamma0=G0[obj], at_gamma0=[v0.real, v0.imag], slope=W.slope(), slope_numeric=num_slope,
                       nearest=near, at_nearest=[[v.real, v.imag] for v in vn], line_peak=peak)
            if obj == 'q':
                z = B14.gamma_of(complex(*PAIR))
                row['gammaOf_rho'] = [z.real, z.imag]
                row['hhat_at_gammaOf_rho'] = [complex(W.ghat(z)).real, complex(W.ghat(z)).imag]
            res.append(row)
            print('  a=%-9.6f %-3s h^(g0) %+.3e (peak %.3e) ; slope %+.4e (numeric %+.4e) ; nearest %s -> %s%s'
                  % (a, obj, v0.real, peak, row['slope'], num_slope, ['%.4f' % x for x in near], ['%+.3e' % v.real for v in vn],
                     (' ; h^(gammaOf rho) %+.3e %+.3ei' % tuple(row['hhat_at_gammaOf_rho'])) if obj == 'q' else ''))
    io.open(os.path.join(D, 'b515_matched.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    return 0


def run():
    A = F.ladder()
    done = set()
    if os.path.exists(OUT):
        done = {round(json.loads(l)['a'], 9) for l in io.open(OUT, encoding='utf-8') if l.strip()}
    t0 = time.time()
    print('[%s] widths %d ; pair %s ; order %d' % (time.strftime('%H:%M:%S'), len(A), PAIR, M), flush=True)
    for i, a in enumerate(A):
        if round(a, 9) in done:
            continue
        c = cell(a)
        with io.open(OUT, 'a', encoding='utf-8', newline=NL) as fh:
            fh.write(json.dumps(c) + NL)
        if i % 20 == 0:
            print('[%s] %d/%d a=%.4f ; elapsed %.0f s' % (time.strftime('%H:%M:%S'), i + 1, len(A), a, time.time() - t0), flush=True)
    print('[%s] done ; elapsed %.0f s' % (time.strftime('%H:%M:%S'), time.time() - t0), flush=True)
    return 0


if __name__ == '__main__':
    sys.exit({'fixture': fixture, 'matched': matched, 'run': run}[sys.argv[1]]())
