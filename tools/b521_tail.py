# -*- coding: utf-8 -*-
"""b521_tail.py -- Q0'S TAIL TIGHTENED, THEN THE WIDTH PASS RE-RUN. ### `python tools/b521_tail.py order | fixture | validity | compare | run`

### THE WINDOW (READING (1)): b519's variant (B) -- the plateau (indicator of [-W, W] convolved with the order-p B-spline of
### half-width R = L/8, W = L - R) under the zero factor at gamma_0 -- with the ramp's order p as the parameter (b519: p = 5).
### THE NEW TAIL (READING (2)), for Q0's zeros above T = 150, CLOSED FORM:
###   |sinc(x + iy)| <= cosh(y) min(1, 1/|x|); |t -+ gamma_0| >= t (1 -+ gamma_0/T); |gamma_0^2 - z^2| <= kappa_s t^2,
###   kappa_s = 1 + (gamma_0^2 + s^2)/T^2; so |k-hat(t - is)| <= c1^2 t^2 on [T, t2] (the ramp factor saturated) and
###   <= c2^2 t^(2 - 2p) on [t2, inf), t2 = gamma_0 + 2/h; integrated against 2 dN, dN = (1/pi) log(t sqrt 23 / 2pi) dt,
###   INT t^k log(ct) dt = t^(k+1)/(k+1) (log(ct) - 1/(k+1)). ### ON-LINE part: s = 0; OFF-LINE allowance: s = 1/2 (real part
###   up to 1) less the on-line part -- both over the full count, because the off-line share above 150 is unknown; their SUM is
###   the worst case, and that sum is the tail used.
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
import b325_epstein as EP   # noqa: E402

NL = chr(10)
TOP = 150.0
G0 = 16.290216
CDEN = math.sqrt(23.0) / (2.0 * math.pi)
P_RANGE = list(range(5, 21))
NAMED = (15.0, 30.0, 45.0, 60.0)
GRID = [float(a) for a in range(15, 61)]
LAMQ_TOP = len(EP.LAMQ) - 1
QL, QH = 40, 60
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


class PWindow(B19.VWindow):
    """### variant (B) with the ramp's B-spline order p."""

    def __init__(self, a, obj, p):
        B19.VWindow.__init__(self, a, obj, 'B')
        self.m = p
        self.h = 2.0 * self.R / p
        ks = np.linspace(-self.R, self.R, p + 1)
        self.knots = np.unique(np.concatenate([ks - self.W, ks + self.W]))
        self.order_note = 'plateau: indicator of [-W, W] (W = %.6f) convolved with the order-%d B-spline of half-width R = %.6f' % (self.W, p, self.R)


def F_int(t, k):
    return t ** (k + 1) / (k + 1) * (math.log(CDEN * t) - 1.0 / (k + 1))


def consts(W, s):
    kap = 1.0 + (W.g0 ** 2 + s * s) / TOP ** 2
    Ks = kap * math.cosh(s * W.W) * math.cosh(s * W.h / 2.0) ** W.m / W.W
    mu = lambda q: 0.5 * (1.0 + (1.0 - W.g0 / TOP) ** (-q))
    c1 = Ks * mu(1)
    c2 = Ks * mu(W.m + 1) * (2.0 / W.h) ** W.m
    t2 = W.g0 + 2.0 / W.h
    return c1, c2, t2


def allowance(W, t, s):
    """### the per-zero bound on |k-hat(t - is)| for t >= T, |s| <= s -- the pointwise form of the closed-form tail."""
    c1, c2, t2 = consts(W, s)
    return (c1 * t) ** 2 if t < t2 else (c2 * t ** (1 - W.m)) ** 2


def tail_s(W, s):
    c1, c2, t2 = consts(W, s)
    tot = 0.0
    if t2 > TOP:
        tot += c1 ** 2 * (F_int(t2, 2) - F_int(TOP, 2))
    lo = max(TOP, t2)
    k = 2 - 2 * W.m
    tot += c2 ** 2 * (0.0 - F_int(lo, k))
    return 2.0 * tot / math.pi


def new_tail(W):
    on = tail_s(W, 0.0)
    total = tail_s(W, 0.5)
    return dict(on=on, off=total - on, total=total)


def cell_q(a, p):
    """### b519's cell for Q0 alone, the window at order p, the tail replaced by the new closed form (the old printed beside)."""
    W = PWindow(a, 'q', p)
    kz = 'qd'
    Hb, Hh, Hw = W.khat(F.U_BASE).real, W.khat(F.U_HALF).real, W.khat(F.U_WIDE).real
    A = F.arch(Hb, F.U_BASE, F.KER[kz + '_base'])
    Eu = abs(F.arch(Hh, F.U_HALF, F.KER[kz + '_half']) - A) + abs(F.arch(Hw, F.U_WIDE, F.KER[kz + '_wide']) - A)
    PR, PRabs = F.prime_channel_q(W, QL)
    PR2, _ = F.prime_channel_q(W, QH)
    G = F.GQ
    zt = 2.0 * W.khat(G).real
    Zon = float(np.sum(zt))
    offterms, pair = [], None
    for b, gg in F.OFFQ:
        t = float(sum(W.khat(B14.gamma_of(r)).real for r in B14.images(b, gg)))
        offterms.append(t)
        if (b, gg) == B19.PAIR:
            pair = t
    others = float(np.sum(offterms)) - pair
    nt = new_tail(W)
    Etail = nt['total']
    dk = np.abs(2.0 * (W.khat(G + F.DELTA_Q).real - W.khat(G).real))
    P = float((W.khat(0.5j) + W.khat(-0.5j)).real)
    Z = Zon + float(np.sum(offterms))
    r = Z - (P - PR + A)
    Ek = abs(PR - PR2)
    Aabs = float(np.trapezoid(np.abs(Hb * F.KER[kz + '_base']), F.U_BASE) / (2.0 * math.pi))
    Eround = 4.0 * F.EPS * (float(np.sum(np.abs(zt))) + float(np.sum(np.abs(offterms))) + Aabs + PRabs) + float(np.sum(dk))
    B = Eu + Ek + Etail + Eround
    gr, bound = W.growth()
    rest = Z - pair
    return dict(a=a, p=p, gamma0=G0, A=A, PR=PR, P=P, Z=Z, Z_on=Zon, pair=pair, others=others, on_rest=Zon, rest=rest,
                ratio=pair / rest if rest else None, m=A - PR, h2=P - PR + A, r=r, B=B, Bprime=Eu + Ek + Eround, Eu=Eu, Ek=Ek,
                Etail=Etail, tail_on=nt['on'], tail_off=nt['off'], Etail_old=B19.tail(W, 150.0, 'q'), Eround=Eround,
                shortfall=B19.shortfall(W, kz), verified=bool(abs(r) <= B), growth=gr, growth_bound=bound, growth_fraction=gr / bound,
                nv=None, nv_note='closed-form transform: no v-grid -- (R114)`s rule has no object, as b511-b520 read it')


def order():
    """### Component 0: p = 5, 6, ... at the four named widths; the least p with the new tail below B' at a = 60; stop 2 after."""
    rows, least = [], None
    for p in P_RANGE:
        for a in NAMED:
            c = cell_q(a, p)
            rows.append(dict(p=p, a=a, Etail=c['Etail'], Etail_old=c['Etail_old'], Bprime=c['Bprime'], pair=c['pair']))
            print('  p=%-2d a=%-4.0f new tail %.3e ; old majorant %.3e ; B` %.3e ; pair %+.3e' % (p, a, c['Etail'], c['Etail_old'], c['Bprime'], c['pair']), flush=True)
        at60 = rows[-1]
        if least is None and at60['Etail'] < at60['Bprime']:
            least = p
        if least is not None and p >= least + 2:
            break
    res = dict(rows=rows, least_p=least, range=[P_RANGE[0], P_RANGE[-1]])
    io.open(os.path.join(D, 'b521_order.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print('### LEAST p WITH THE NEW TAIL BELOW B` AT a = 60 : %s' % least)
    return 0


def least_p():
    return json.loads(io.open(os.path.join(D, 'b521_order.json'), encoding='utf-8').read())['least_p']


def fixture():
    """### the (R125)(2) fixture of the rebuilt window at a = 5, Q0; and the closed-form tail against its own integrand integrated
    ### numerically at a = 15 and 60."""
    p = least_p()
    W = PWindow(5.0, 'q', p)
    kb = np.unique(np.round((W.knots[:, None] + W.knots[None, :]).ravel(), 14))
    kb = kb[(kb >= -2 * W.half) & (kb <= 2 * W.half)]
    nodes, wts = np.polynomial.legendre.leggauss(80)
    a0, b0 = kb[:-1], kb[1:]
    mid, rad = (a0 + b0) / 2.0, (b0 - a0) / 2.0
    xx = (mid[:, None] + rad[:, None] * nodes[None, :]).ravel()
    ww = (rad[:, None] * wts[None, :]).ravel()
    kx = W.k(xx, QH)
    us = np.array([0.0, 1.0, G0] + B19.notches('q') + [30.0, 60.0])
    rows = []
    for u in us:
        terms = ww * kx * np.cos(u * xx)
        num = float(np.sum(terms))
        cf = float(W.khat(u).real)
        floor = F.EPS * float(np.sum(np.abs(terms)))
        bar = floor * math.sqrt(len(terms))
        rows.append(dict(u=float(u), closed=cf, numeric=num, diff=abs(cf - num), floor=floor, bar=bar, meets=abs(cf - num) <= bar))
    integ = []
    for a in (15.0, 60.0):
        Wa = PWindow(a, 'q', p)
        for s in (0.0, 0.5):
            t = np.geomspace(TOP, TOP * 1e7, 400001)
            f = np.array([allowance(Wa, x, s) for x in t[::400]])
            tt = t[::400]
            dens = np.log(CDEN * tt) / math.pi
            num = float(2.0 * np.trapezoid(f * dens, tt))
            cf = tail_s(Wa, s)
            integ.append(dict(a=a, s=s, closed=cf, numeric=num, rel=abs(cf - num) / cf))
    res = dict(p=p, a=5.0, rows=rows, meets=all(r['meets'] for r in rows), nodes=len(xx),
               even=float(abs(W.k([0.7], QH)[0] - W.k([-0.7], QH)[0])), scale=float(max(abs(r['closed']) for r in rows)),
               generating_h='h(u) = (%.6f^2 + d^2/du^2)(cos(%.6f u) phi(u)), phi the %s at a = 5' % (G0, G0, W.order_note),
               support=[-2 * W.half, 2 * W.half], integration=integ)
    io.open(os.path.join(D, 'b521_fixture.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print('  p=%d : bar met at every u %s ; largest diff/bar %.3f' % (p, res['meets'], max(r['diff'] / r['bar'] for r in rows)))
    for x in integ:
        print('  closed-form tail a=%.0f s=%.1f : %.4e ; its integrand integrated numerically %.4e ; rel %.1e' % (x['a'], x['s'], x['closed'], x['numeric'], x['rel']))
    return 0


def validity():
    """### Component 1`s fixture: a synthetic zero at 0.9 + 200 i -- its four images` true terms against the allowance at s = 1/2
    ### (must cover); a negative control at real part 3.0, which the allowance at s = 1/2 must NOT cover."""
    p = least_p()
    out = []
    for a in NAMED:
        W = PWindow(a, 'q', p)
        for beta, must in ((0.9, True), (3.0, False)):
            imgs = B14.images(beta, 200.0)
            terms = [abs(complex(W.khat(B14.gamma_of(r)))) for r in imgs]
            allow = allowance(W, 200.0, 0.5)
            covered = all(x <= allow for x in terms)
            out.append(dict(a=a, beta=beta, terms=terms, allowance=allow, covered=covered, must_cover=must, ok=(covered == must)))
            print('  a=%-4.0f real part %.1f : largest image term %.3e ; allowance %.3e ; covered %s (must %s)' % (a, beta, max(terms), allow, covered, must))
    io.open(os.path.join(D, 'b521_validity.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(dict(p=p, rows=out), indent=1) + NL)
    return 0


def compare():
    """### Component 1: the new tail at the least p, and at p = 5, against b519`s banked old majorant, at b519`s widths."""
    p = least_p()
    b19 = sorted((json.loads(l) for l in io.open(os.path.join(D, 'b519_cells_B.jsonl'), encoding='utf-8') if l.strip()), key=lambda c: c['a'])
    rows = []
    for c in b19:
        a = c['a']
        nt = new_tail(PWindow(a, 'q', p))
        n5 = new_tail(PWindow(a, 'q', 5))
        rows.append(dict(a=a, old=c['q']['Etail'], new=nt['total'], new_on=nt['on'], new_off=nt['off'], new_p5=n5['total']))
    smaller = [r['a'] for r in rows if r['new'] < r['old']]
    res = dict(p=p, rows=rows, smaller=len(smaller), of=len(rows), not_smaller=[r['a'] for r in rows if r['new'] >= r['old']],
               p5_smaller=sum(1 for r in rows if r['new_p5'] < r['old']))
    io.open(os.path.join(D, 'b521_compare.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1) + NL)
    print('  at p = %d the new tail is below b519`s old majorant at %d of %d widths ; not below at %s' % (p, res['smaller'], res['of'], res['not_smaller'][:20]))
    print('  at p = 5 (the closed form alone) below at %d of %d' % (res['p5_smaller'], res['of']))
    return 0


def run():
    """### Component 2: the reach as b520 registered it, the new tail, one pass a = 15..60; Q0 alone (xi cited from b520)."""
    p = least_p()
    out = os.path.join(D, 'b521_cells.jsonl')
    if os.path.exists(out):
        os.remove(out)
    scan, reach, stop = [], None, None
    t0 = time.time()
    for a in GRID:
        c = cell_q(a, p)
        e = dict(a=a, Etail=c['Etail'], Bprime=c['Bprime'], Eu=c['Eu'], Ek=c['Ek'], Eround=c['Eround'], shortfall=c['shortfall'],
                 lamq_ok=a * a <= LAMQ_TOP, tail_over_Bprime=c['Etail'] / c['Bprime'])
        scan.append(e)
        if c['Etail'] > c['Bprime'] or not e['lamq_ok']:
            stop = dict(e, why=('E_tail > B`' if c['Etail'] > c['Bprime'] else 'a^2 beyond LAMQ'))
            print('[%s] a=%.0f STOP : %s' % (time.strftime('%H:%M:%S'), a, stop['why']), flush=True)
            break
        reach = a
        with io.open(out, 'a', encoding='utf-8', newline=NL) as fh:
            fh.write(json.dumps(c) + NL)
        print('[%s] a=%.0f ; tail/B` %.2e ; elapsed %.0f s' % (time.strftime('%H:%M:%S'), a, e['tail_over_Bprime'], time.time() - t0), flush=True)
    io.open(os.path.join(D, 'b521_reach.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(dict(p=p, reach=reach, stop=stop, scan=scan), indent=1) + NL)
    print('### Q0`S REACH : %s (stop %s)' % (reach, stop and stop['a']))
    return 0


if __name__ == '__main__':
    sys.exit({'order': order, 'fixture': fixture, 'validity': validity, 'compare': compare, 'run': run}[sys.argv[1]]())
