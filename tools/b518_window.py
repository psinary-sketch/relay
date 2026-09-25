# -*- coding: utf-8 -*-
"""b518_window.py -- THE TWO-PROPERTY WINDOW. ### `python tools/b518_window.py fixture | matched | run`

### THE WINDOW (READING (1)). phi, the uniform B-spline bump of order M = 6 on [-L, L], L = log a, spacing s = 2L/6;
### g(u) = cos(gamma_0 u) phi(u); h = g'' + gamma_0^2 g = cos(gamma_0 u) phi'' - 2 gamma_0 sin(gamma_0 u) phi', C^2 because phi
### is C^4. In the kernel's convention, h-hat(z) = (gamma_0^2 - z^2) g-hat(z), g-hat(z) = (phi-hat(z - gamma_0) + phi-hat(z +
### gamma_0)) / 2: zero at z = gamma_0 with slope -2 gamma_0 g-hat(gamma_0), band-limited near +-gamma_0 by the cosine.
### k = h * h~ = h * h (h real and even); k-hat = h-hat^2. No pole annihilation. ### THE CHAIN is b515's with the window
### replaced: b511's grids, kernels, banks and prime channels and b514's helpers IMPORTED, not copied.
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
OUT = os.path.join(D, 'b518_cells.jsonl')
G0 = dict(xi=14.1347, q=16.290216)
M = 6
QL, QH = 40, 60                    # ### READING (5): h is cos/sin times a polynomial per piece -- not exact; two orders
PAIR = B14.PAIR
DELTA = PAIR[0] - 0.5
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


class TWindow(B14.MWindow):
    """### h = (gamma_0^2 + D^2)(cos(gamma_0 u) phi), phi the order-6 B-spline bump on [-log a, log a]."""

    def __init__(self, a, g0):
        B14.MWindow.__init__(self, a, g0, M)

    def ghat_cos(self, z):
        return B14.MWindow.ghat(self, z)

    def ghat(self, z):
        z = np.asarray(z, dtype=complex)
        return (self.g0 ** 2 - z * z) * self.ghat_cos(z)

    def khat(self, z):
        return self.ghat(z) ** 2

    def slope(self):
        return float((-2.0 * self.g0 * self.ghat_cos(self.g0)).real)

    def gcos_d(self, t, d):
        return B14.MWindow.g_d(self, t, d)

    def g(self, t):
        return self.gcos_d(t, 2) + self.g0 ** 2 * self.gcos_d(t, 0)

    def g_d(self, t, d):
        return self.gcos_d(t, d + 2) + self.g0 ** 2 * self.gcos_d(t, d)


def majorant(W, t, s=0.0):
    """### |k-hat(t + is)| <= ((g0^2 + t^2 + s^2) SUM_+- (cosh(s sp/2) min(1, 2/(|t -+ g0| sp)))^6 / 2)^2."""
    t = np.asarray(t, dtype=float)
    tot = 0.0
    for sg in (1.0, -1.0):
        w = np.abs(t - sg * W.g0) * W.h / 2.0
        tot = tot + (math.cosh(s * W.h / 2.0) * np.minimum(1.0, 1.0 / np.maximum(w, 1e-300))) ** W.m
    return ((W.g0 ** 2 + t * t + s * s) * 0.5 * tot) ** 2


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
    return float(2.0 * np.trapezoid(majorant(W, u) * K1200 * np.log(u) / math.log(1200.0), u) / (2.0 * math.pi))


def cell(a):
    out = dict(a=a)
    for obj in ('xi', 'q'):
        W = TWindow(a, G0[obj])
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
    """### READING (7): the closed form against INT k(x) cos(u x) dx; the floor eps * SUM|terms| of the numerical route, the bar
    ### sqrt(n) times it, both printed per u; at a = 5, each gamma_0."""
    res = []
    for obj in ('xi', 'q'):
        W = TWindow(5.0, G0[obj])
        kb = np.unique(np.round((W.knots[:, None] + W.knots[None, :]).ravel(), 14))
        kb = kb[(kb >= -2 * W.half) & (kb <= 2 * W.half)]
        nodes, wts = np.polynomial.legendre.leggauss(80)
        a0, b0 = kb[:-1], kb[1:]
        mid, rad = (a0 + b0) / 2.0, (b0 - a0) / 2.0
        xx = (mid[:, None] + rad[:, None] * nodes[None, :]).ravel()
        ww = (rad[:, None] * wts[None, :]).ravel()
        kx = W.k(xx, QH)
        G = F.GAM if obj == 'xi' else F.GQ
        near = sorted(x for x in G[np.argsort(np.abs(G - G0[obj]))[:3]].tolist() if abs(x - G0[obj]) > 1e-3)[:2]
        us = np.array([0.0, 1.0, G0[obj]] + near + [30.0, 60.0])
        rows = []
        for u in us:
            terms = ww * kx * np.cos(u * xx)
            num = float(np.sum(terms))
            cf = float(W.khat(u).real)
            floor = F.EPS * float(np.sum(np.abs(terms)))
            bar = floor * math.sqrt(len(terms))
            rows.append(dict(u=float(u), closed=cf, numeric=num, diff=abs(cf - num), floor=floor, bar=bar, meets=abs(cf - num) <= bar))
        eps = 1e-9
        jumps = {}
        for d in (0, 1, 2, 3):
            jk = [abs(float(W.g_d([x + eps], d)[0] - W.g_d([x - eps], d)[0])) for x in W.knots[1:-1]]
            jumps['D%d' % d] = max(jk)
        res.append(dict(object=obj, a=5.0, gamma0=G0[obj], order=W.m, nodes=len(xx), rows=rows, meets=all(r['meets'] for r in rows),
                        even=float(abs(W.k([0.7], QH)[0] - W.k([-0.7], QH)[0])), scale=float(max(abs(r['closed']) for r in rows)),
                        knot_jumps=jumps, support=[-2 * W.half, 2 * W.half],
                        generating_h='h(u) = (%s^2 + d^2/du^2)(cos(%s u) phi(u)), phi the order-%d B-spline on [-log 5, log 5]'
                        % (G0[obj], G0[obj], W.m)))
    io.open(os.path.join(D, 'b518_fixture.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    for r in res:
        print('  %-3s gamma0 %.6f order %d, %d nodes : bar met at every u %s ; |k(.7)-k(-.7)| %.1e ; knot jumps %s'
              % (r['object'], r['gamma0'], r['order'], r['nodes'], r['meets'], r['even'], {k: '%.1e' % v for k, v in r['knot_jumps'].items()}))
        for x in r['rows']:
            print('      u=%-8.4f diff %.2e ; floor eps*SUM|t| %.2e ; bar sqrt(n)*floor %.2e ; %s' % (x['u'], x['diff'], x['floor'], x['bar'], 'MET' if x['meets'] else 'NOT MET'))
    return 0


def matched():
    """### READING (8): h-hat on the line at gamma_0 (0, the control), its slope, and |h-hat| / |slope| at 14.63, 18.83 and
    ### the object's lowest on-line zero other than gamma_0; h-hat at gammaOf rho for Q0. Three ladder widths."""
    A = F.ladder()
    res = []
    for a in (A[0], A[59], A[118]):
        for obj in ('xi', 'q'):
            W = TWindow(a, G0[obj])
            G = F.GAM if obj == 'xi' else F.GQ
            near = sorted(x for x in G[np.argsort(np.abs(G - G0[obj]))[:3]].tolist() if abs(x - G0[obj]) > 1e-3)[:2]
            low = float(next(x for x in sorted(G.tolist()) if abs(x - G0[obj]) > 1e-3))
            v0 = complex(W.ghat(G0[obj]))
            sl = W.slope()
            num_slope = float(((W.ghat(G0[obj] + 1e-6) - W.ghat(G0[obj] - 1e-6)) / 2e-6).real)
            pts = near + [low]
            ratios = [abs(complex(W.ghat(x))) / abs(sl) for x in pts]
            peak = float(np.max(np.abs(W.ghat(np.linspace(0, 60, 6001)))))
            row = dict(a=a, object=obj, gamma0=G0[obj], at_gamma0=[v0.real, v0.imag], slope=sl, slope_numeric=num_slope,
                       line_peak=peak, points=pts, ratio_to_slope=ratios)
            if obj == 'q':
                z = B14.gamma_of(complex(*PAIR))
                row['hhat_at_gammaOf_rho'] = [complex(W.ghat(z)).real, complex(W.ghat(z)).imag]
            res.append(row)
            print('  a=%-9.6f %-3s h^(g0) %+.1e (peak %.3e) ; slope %+.4e (numeric %+.4e) ; |h^|/|slope| at %s -> %s'
                  % (a, obj, v0.real, peak, sl, num_slope, ['%.4f' % x for x in pts], ['%.3e' % x for x in ratios]))
    io.open(os.path.join(D, 'b518_matched.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
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
