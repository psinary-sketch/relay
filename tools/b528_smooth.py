# -*- coding: utf-8 -*-
"""b528_smooth.py -- BOTH OBJECTS ON THE KERNEL`S FUNCTION. ### `python tools/b528_smooth.py check | fixture | run <obj> <lo> <hi>`

### THE WINDOW: phi = the kernel`s `plateau (1/4) (log a)` through b527`s `phi_chain` (re-checked in `check`); h = (gamma_0^2 + D^2)
### (cos(gamma_0 u) phi) = cos(gamma_0 u) phi'' - 2 gamma_0 sin(gamma_0 u) phi' (the gamma_0^2 terms cancel), phi' and phi'' in closed
### form from the logistic form of smoothTransition: S(y) = sigma(l), l = 1/(1-y) - 1/y, y = (L - |u|)/(F L);
### S' = S(1-S) l', S'' = S(1-S)(l'' + (1-2S) l'^2). ### k = h * h, k-hat = h-hat^2 (h real and even).
### THE TRANSFORM (route 1): h-hat(z) = 2 INT_0^L h(u) cos(z u) du by the trapezoid on a uniform half-grid (h vanishes with every
### derivative at L, so the rule is spectrally accurate below its Nyquist frequency pi/du); a second grid at 2 du gives E_ft.
### THE CUT: T_cut, the least t >= 500 past which the computed |k-hat| stays below 1e-22 on the search grid to 6000 (every s used);
### zeros past T_cut are priced in the tail ESTIMATE, not summed. ### THE TAIL -- AN ESTIMATE, NOT A MAJORANT (R138)(2):
### an envelope (the bin maximum over the sampled t and s) of the computed |k-hat(t - i s)| times the count -- Q0: above 150,
### the RvM main term M0, s up to 1/2 (strip; the reach and B) and, for the survival column, s up to sigma_max - 1/2 with b523`s
### E(T) and N_bank(150) = 180; xi: the bank`s own zeros past T_cut, s = 0, and above the atlas`s top the main term, zeros there
### on the line (as b519-b526 read xi). ### The prime channel k(log n) by Gauss-Legendre panels in real space (QL = 40, QH = 60).
"""
import io
import json
import math
import os
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T_ = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T_)
import b511_families as F   # noqa: E402
import b514_window as B14   # noqa: E402
import b519_window as B19   # noqa: E402
import b523_caveats as C23  # noqa: E402
import b527_values as V     # noqa: E402

NL = chr(10)
FR = 0.25
G0 = dict(xi=14.1347, q=16.290216)
DELTA = B19.DELTA
GRID = [float(a) for a in range(15, 61)]
QL, QH = 40, 60
KCUT = 1e-22                 # ### above the quadrature`s own roundoff floor for |k-hat| (about 1e-26)
T_SEARCH = 6000.0
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def logistic_parts(y):
    """### S, S', S'' in y for y in (0, 1); S = 1 at y >= 1, 0 at y <= 0, derivatives 0 there."""
    y = np.asarray(y, dtype=float)
    S, S1, S2 = np.zeros_like(y), np.zeros_like(y), np.zeros_like(y)
    S[y >= 1] = 1.0
    m = (y > 0) & (y < 1)
    yy = y[m]
    l = 1.0 / (1.0 - yy) - 1.0 / yy
    lc = np.clip(l, -700, 700)
    s = 1.0 / (1.0 + np.exp(-lc))
    e = np.exp(-np.abs(lc))
    s1ms = e / (1.0 + e) ** 2                          # ### S(1 - S), stable at both ends
    lp = 1.0 / (1.0 - yy) ** 2 + 1.0 / yy ** 2
    lpp = 2.0 / (1.0 - yy) ** 3 - 2.0 / yy ** 3
    S[m], S1[m], S2[m] = s, s1ms * lp, s1ms * (lpp + (1.0 - 2.0 * s) * lp * lp)
    return S, S1, S2


class SmoothWindow:
    def __init__(self, a, obj, du=None):
        self.a, self.obj, self.g0 = a, obj, G0[obj]
        self.L = math.log(a)
        self.half = self.L
        self.FL = FR * self.L
        self.rin = (1 - FR) * self.L
        self.set_grid(du or math.pi / (2 * 1300.0))

    def set_grid(self, du):
        n = int(math.ceil(self.L / du))
        self.du = self.L / n
        self.uh = np.linspace(0.0, self.L, n + 1)
        w = np.full(n + 1, self.du)
        w[0] = w[-1] = self.du / 2.0
        self.wh = 2.0 * w * self.h(self.uh)             # ### 2 x trapezoid weights x h: h-hat(z) = SUM wh cos(z u)

    def phi_parts(self, u):
        u = np.asarray(u, dtype=float)
        S, S1, S2 = logistic_parts((self.L - np.abs(u)) / self.FL)
        sg = np.sign(u)
        return S, -sg * S1 / self.FL, S2 / self.FL ** 2

    def phi(self, u):
        return self.phi_parts(u)[0]

    def h(self, u):
        u = np.asarray(u, dtype=float)
        _p, p1, p2 = self.phi_parts(u)
        return np.cos(self.g0 * u) * p2 - 2.0 * self.g0 * np.sin(self.g0 * u) * p1

    def g(self, u):
        return np.cos(self.g0 * np.asarray(u, dtype=float)) * self.phi(u)

    def hhat(self, z):
        z = np.atleast_1d(np.asarray(z))
        cplx = np.iscomplexobj(z) and np.any(np.imag(z) != 0)
        out = np.zeros(z.shape, dtype=complex if cplx else float)
        for i in range(0, z.size, 256):
            zz = z.ravel()[i:i + 256]
            out.ravel()[i:i + 256] = np.cos(np.outer(zz, self.uh)) @ self.wh
        return out

    def khat(self, z):
        return self.hhat(z) ** 2

    def k(self, xs, q):
        """### k(x) = INT h(t) h(x - t) dt, Gauss-Legendre of order q on each piece between the ramp breakpoints."""
        nodes, wts = np.polynomial.legendre.leggauss(q)
        kn = np.array([-self.L, -self.rin, self.rin, self.L])
        out = []
        for x in np.atleast_1d(xs):
            lo, hi = max(-self.L, x - self.L), min(self.L, x + self.L)
            if hi <= lo:
                out.append(0.0)
                continue
            bp = np.unique(np.concatenate([kn, x - kn, np.linspace(lo, hi, 9)]))
            bp = bp[(bp >= lo) & (bp <= hi)]
            a0, b0 = bp[:-1], bp[1:]
            mid, rad = (a0 + b0) / 2.0, (b0 - a0) / 2.0
            tt = (mid[:, None] + rad[:, None] * nodes[None, :]).ravel()
            ww = (rad[:, None] * wts[None, :]).ravel()
            out.append(float(np.sum(ww * self.h(tt) * self.h(x - tt))))
        return np.array(out)

    def growth(self):
        u = np.linspace(-self.L, self.L, 400001)
        p = self.phi(u)
        return float(np.trapezoid(p * np.cosh(DELTA * u), u) / np.trapezoid(p, u)), math.exp(DELTA * self.L)


def envelope(W, s_list, t0=150.0, t1=T_SEARCH, step=1.0):
    """### |k-hat(t - i s)| on a t grid for each s, from cos and sin tables shared across s."""
    ts = np.arange(t0, t1 + step / 2, step)
    ch = [np.cosh(s * W.uh) for s in s_list]
    sh = [np.sinh(s * W.uh) for s in s_list]
    out = np.zeros((len(s_list), ts.size))
    for i in range(0, ts.size, 256):
        tt = ts[i:i + 256]
        C, Sn = np.cos(np.outer(tt, W.uh)), np.sin(np.outer(tt, W.uh))
        for j in range(len(s_list)):
            re = C @ (W.wh * ch[j])
            im = -(Sn @ (W.wh * sh[j]))
            out[j, i:i + 256] = re * re + im * im
    return ts, out


def tcut_of(ts, env):
    big = np.where(env.max(axis=0) >= KCUT)[0]
    last = ts[big[-1]] if big.size else ts[0]
    return float(max(500.0, last + 1.0)), bool(big.size and big[-1] == ts.size - 1)


def bins_estimate(ts, e, counts):
    """### SUM over unit bins of the bin`s envelope maximum times the bin`s count."""
    return float(np.sum(np.maximum(e[:-1], e[1:]) * counts))


def cell(a, obj):
    t0 = time.time()
    W = SmoothWindow(a, obj, du=math.pi / (2 * T_SEARCH))
    smax = C23.smax() - 0.5
    s_strip = [0.0, 0.125, 0.25, 0.375, 0.5] if obj == 'q' else [0.0]
    s_sig = list(np.linspace(0.0, smax, 6)) if obj == 'q' else [0.0]
    ts, env_all = envelope(W, sorted(set(s_strip + s_sig)))
    sl = sorted(set(s_strip + s_sig))
    e_strip = env_all[[sl.index(s) for s in s_strip]].max(axis=0)
    e_sig = env_all[[sl.index(s) for s in s_sig]].max(axis=0)
    tcut, runaway = tcut_of(ts, env_all)
    W.set_grid(math.pi / (2.5 * max(tcut, 1300.0)))
    W2 = SmoothWindow(a, obj, du=2 * W.du)
    kz = 'z' if obj == 'xi' else 'qd'

    def sides(Wx):
        Hb, Hh, Hw = Wx.khat(F.U_BASE), Wx.khat(F.U_HALF), Wx.khat(F.U_WIDE)
        A = F.arch(Hb, F.U_BASE, F.KER[kz + '_base'])
        Eu = abs(F.arch(Hh, F.U_HALF, F.KER[kz + '_half']) - A) + abs(F.arch(Hw, F.U_WIDE, F.KER[kz + '_wide']) - A)
        if obj == 'xi':
            G = F.GAM[F.GAM <= tcut]
            zt = 2.0 * Wx.khat(G)
            offterms, pair = [], float(zt[int(np.argmin(np.abs(G - G0['xi'])))])
            dk = np.abs(2.0 * (Wx.khat(G * (1 + F.DELTA_XI)) - Wx.khat(G)))
        else:
            G = F.GQ
            zt = 2.0 * Wx.khat(G)
            offterms, pair = [], None
            for b, gg in F.OFFQ:
                t = float(np.sum(Wx.khat(np.array([B14.gamma_of(r) for r in B14.images(b, gg)]))).real)
                offterms.append(t)
                if (b, gg) == B19.PAIR:
                    pair = t
            dk = np.abs(2.0 * (Wx.khat(G + F.DELTA_Q) - Wx.khat(G)))
        P = float(np.sum(Wx.khat(np.array([0.5j, -0.5j]))).real)
        Aabs = float(np.trapezoid(np.abs(Hb * F.KER[kz + '_base']), F.U_BASE) / (2.0 * math.pi))
        return dict(A=A, Eu=Eu, zt=zt, offterms=offterms, pair=pair, dk=dk, P=P, Aabs=Aabs, Hb=Hb)

    s1, s2 = sides(W), sides(W2)
    chan = F.prime_channel_xi if obj == 'xi' else F.prime_channel_q
    PR, PRabs = chan(W, QL)
    PR2, _ = chan(W, QH)
    Zon = float(np.sum(s1['zt']))
    Z = Zon + float(np.sum(s1['offterms']))
    Z2 = float(np.sum(s2['zt'])) + float(np.sum(s2['offterms']))
    Eft = abs(Z - Z2) + abs(s1['P'] - s2['P']) + abs(s1['A'] - s2['A'])
    A, P = s1['A'], s1['P']
    r = Z - (P - PR + A)
    Ek = abs(PR - PR2)
    Eround = 4.0 * F.EPS * (float(np.sum(np.abs(s1['zt']))) + float(np.sum(np.abs(s1['offterms']))) + s1['Aabs'] + PRabs) + float(np.sum(s1['dk']))
    Bprime = s1['Eu'] + Ek + Eround + Eft
    # ### THE TAIL, AN ESTIMATE
    if obj == 'q':
        edges = ts
        cnt = np.diff(np.array([C23.M0(t) for t in edges]))
        tail = 2.0 * bins_estimate(ts, e_strip, cnt)
        pp = json.loads(io.open(os.path.join(D, 'b523_count.json'), encoding='utf-8').read())['params']
        cntE = np.diff(np.array([C23.E_of(pp, t) for t in edges]))
        tail_full = 2.0 * (bins_estimate(ts, e_sig, cnt) + e_sig[0] * (C23.M0(150.0) + C23.E_of(pp, 150.0) - C23.n_bank(150.0))
                           + bins_estimate(ts, e_sig, cntE))
        beyond = 2.0 * float(np.max(e_sig[ts >= min(tcut, ts[-1])])) * (C23.M0(1e7) - C23.M0(T_SEARCH))  # ### past the edge: the edge`s value (READING (4)); defect D3
        tail += beyond
        tail_full += beyond
    else:
        above = F.GAM[F.GAM > tcut]
        tail = 2.0 * float(np.sum(np.interp(above, ts, env_all[0], right=float(env_all[0][-1]))))
        tail += 2.0 * float(env_all[0][-1]) * ((1e7 / (2 * math.pi)) * math.log(1e7 / (2 * math.pi * math.e)))
        tail_full = tail
    B = Bprime + tail
    Bfull = Bprime + tail_full
    gr, bound = W.growth()
    K1200 = float(abs(F.KER[kz + '_wide'][-1]))
    m = ts >= 1200.0
    shortfall = float(2.0 * np.trapezoid(env_all[0][m] * K1200 * np.log(ts[m]) / math.log(1200.0), ts[m]) / (2.0 * math.pi)) if m.sum() > 1 else 0.0
    pair = s1['pair']
    others = float(np.sum(s1['offterms'])) - pair if obj == 'q' else 0.0
    on_rest = Zon if obj == 'q' else Zon - pair
    rest = Z - pair
    h2 = P - PR + A
    return dict(a=a, obj=obj, window='the kernel`s plateau (1/4, log a), phi_chain', gamma0=G0[obj], A=A, PR=PR, P=P, Z=Z, Z_on=Zon,
                pair=pair, others=others, on_rest=on_rest, rest=rest, ratio=pair / rest if rest else None, h2=h2, r=r,
                Eu=s1['Eu'], Ek=Ek, Eround=Eround, Eft=Eft, Bprime=Bprime, tail_est=tail, tail_full_est=tail_full, B=B, B_full=Bfull,
                tail_status='ESTIMATE', within=bool(tail <= Bprime), verified=bool(abs(r) <= B), neg=bool(abs(r) <= B and h2 < -B),
                neg_full=bool(abs(r) <= Bfull and h2 < -Bfull), pos=bool(abs(r) <= B and h2 > B), tail_share=tail / B,
                tcut=tcut, tcut_at_search_edge=runaway, du=W.du, growth=gr, growth_bound=bound, growth_fraction=gr / bound,
                shortfall=shortfall, nv=None, nv_note='transform by quadrature on a fixed grid: no v-grid -- (R114)`s rule has no object',
                seconds=round(time.time() - t0, 1))


def check():
    """### Component 0 (i): phi_chain against b527`s banked mpmath values, and the window`s phi against phi_chain."""
    b = json.loads(io.open(os.path.join(D, 'b527_values.json'), encoding='utf-8').read())
    rows = []
    for r in b['rows']:
        c = float(V.phi_chain(r['u'], b['a']))
        w = float(SmoothWindow(b['a'], 'q').phi(np.array([r['u']]))[0])
        rows.append(dict(u=r['u'], kernel=r['kernel'], chain=c, window=w, d_chain=abs(c - r['kernel']), d_window=abs(w - r['kernel'])))
    res = dict(a=b['a'], n=len(rows), max_chain=max(x['d_chain'] for x in rows), max_window=max(x['d_window'] for x in rows))
    res['agree'] = res['max_chain'] <= 1e-14 and res['max_window'] <= 1e-14
    io.open(os.path.join(D, 'b528_check.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(dict(res, rows=rows), indent=1) + NL)
    print('  forty points at a = %s : phi_chain vs the kernel (mp) max %.2e ; the window`s phi vs the kernel max %.2e ; within 1e-14 %s'
          % (b['a'], res['max_chain'], res['max_window'], res['agree']))
    return 0


def fixture():
    """### Component 0 (ii): h-hat by route 1 (trapezoid of h cos, half-grid) against route 2 (Gauss-Legendre panels of g cos times
    ### (gamma_0^2 - z^2)), at a = 15, 34, 60, both objects; the bar sqrt(n) x eps x SUM |terms of route 2| ((R125)(2))."""
    nodes, wts = np.polynomial.legendre.leggauss(80)
    out = []
    for a in (15.0, 34.0, 60.0):
        for obj in ('q', 'xi'):
            W = SmoothWindow(a, obj, du=math.pi / (2.5 * 1300.0))
            bp = np.unique(np.concatenate([np.linspace(0, W.rin, 65), np.linspace(W.rin, W.L, 65)]))
            a0, b0 = bp[:-1], bp[1:]
            mid, rad = (a0 + b0) / 2.0, (b0 - a0) / 2.0
            uu = (mid[:, None] + rad[:, None] * nodes[None, :]).ravel()
            ww = (rad[:, None] * wts[None, :]).ravel()
            gu = W.g(uu)
            rows = []
            for z in [0.0, 1.0, G0[obj], 30.0, 60.0, 150.0, 600.0, 0.5j]:
                terms = 2.0 * (G0[obj] ** 2 - z * z) * ww * gu * np.cos(z * uu)
                r2 = complex(np.sum(terms))
                r1 = complex(W.hhat(np.array([z]))[0])
                floor = F.EPS * float(np.sum(np.abs(terms)))
                bar = floor * math.sqrt(terms.size)
                # ### at z = gamma_0 route 2`s factor vanishes: its terms are all zero, its bar is 0 -- NOT SCORABLE, not met
                rows.append(dict(z=str(z), route1=[r1.real, r1.imag], route2=[r2.real, r2.imag], diff=abs(r1 - r2), floor=floor, bar=bar,
                                 meets=(abs(r1 - r2) <= bar) if bar > 0 else None))
            sc = [x for x in rows if x['meets'] is not None]
            out.append(dict(a=a, obj=obj, du=W.du, nodes=int(uu.size), rows=rows, scored=len(sc), not_scorable=[x['z'] for x in rows if x['meets'] is None],
                            meets=all(x['meets'] for x in sc)))
            print('  a=%-4.0f %-3s : bar met at every scorable z %s (%d of %d; NOT SCORABLE %s, |route 1| there %s) ; largest diff/bar %.3f'
                  % (a, obj, out[-1]['meets'], len(sc), len(rows), out[-1]['not_scorable'], ['%.1e' % x['diff'] for x in rows if x['meets'] is None],
                     max(x['diff'] / x['bar'] for x in sc)))
    io.open(os.path.join(D, 'b528_fixture.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out, indent=1) + NL)
    return 0


def run(obj, lo, hi):
    out = os.path.join(D, 'b528_cells_%s.jsonl' % obj)
    done = set()
    if os.path.exists(out):
        done = {json.loads(l)['a'] for l in io.open(out, encoding='utf-8') if l.strip()}
    for a in GRID:
        if a < lo or a > hi or a in done:
            continue
        c = cell(a, obj)
        with io.open(out, 'a', encoding='utf-8', newline=NL) as fh:
            fh.write(json.dumps(c) + NL)
        print('[%s] %s a=%-4.0f h2 %+.4e B %.2e tail(EST)/B` %.1e IN %s VER %s neg %s ratio %+.3f G %.4f Tcut %.0f ; %.0f s'
              % (time.strftime('%H:%M:%S'), obj, a, c['h2'], c['B'], c['tail_est'] / c['Bprime'], c['within'], c['verified'], c['neg'],
                 c['ratio'] or 0, c['growth'], c['tcut'], c['seconds']), flush=True)
    return 0


if __name__ == '__main__':
    m = sys.argv[1]
    if m == 'run':
        sys.exit(run(sys.argv[2], float(sys.argv[3]), float(sys.argv[4])))
    sys.exit({'check': check, 'fixture': fixture}[m]())
