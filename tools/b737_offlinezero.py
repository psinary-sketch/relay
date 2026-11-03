# -*- coding: utf-8 -*-
"""b737_offlinezero.py -- W-ORD-ZQ-OFFLINE-ZERO's PLAN FIGURES, (R347)(3)(a)-(b): NO BUILD, NO LEAN FILE, NO DISPATCH.

Figures for the plan bank data/b737_offlinezero_plan.txt, each printed with the route that took it; none is a proof and none is a Lean statement.
  criteria   (a): the three leading candidates of data/b725_interference.txt :32-:34 (decreasing beta - 1/2): beta - 1/2, gamma, the distance to
             the nearest other zero of Z_Q0 in b711's list (on, off and reflected rows to height 445), the distances to the nearest zeros of
             zeta_K = (Z_Q0 + 2 Z_Q1)/2 and of L(psi) = (Z_Q0 - Z_Q1)/2 on the line (sign changes of Lambda's real form, (sqrt23/2pi)^s Gamma(s)
             times the function, in |t - gamma| <= 8), |Z_Q0'(rho)| by a central difference, and the bits b725 took
  box        (b): two boxes around the candidate named, A a square centred on it and B a rectangle whose right edge sits at Re s = 3/2 (where
             Growth.lean's zq_sub_two_le bounds |Z_Q - 2| <= totQ - 2 < 2); each with its corners, the list's zeros inside, the least |Z_Q0| on a
             boundary sample (the printed margin), the largest sampled |Z_Q0'| there (a Lipschitz figure, sampled, not a bound), and the sample
             count a Lipschitz argument-principle route (R1) would want; for A the Rouche radius of the linear model (R2), sampled
  --bank     writes data/b737_offlinezero_<route>.txt, nothing else
Z_Q0 by tools/b667_epstein_certify.py zq_point and Z_Q1 by tools/b725_interference.py zq_form, both imported unedited. Free memory printed
before each computation, under the 2,560 MB hold. Written by the Write tool at b737.
"""
import io
import math
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

from flint import acb, arb, ctx    # noqa: E402
import b667_epstein_certify as CERT   # noqa: E402
import b725_interference as INT       # noqa: E402

BANK = os.path.join(D, 'b737_offlinezero_%s.txt')
PREC = 200
WIN = 8.0
STEP = 0.05
CANDIDATES = ('off0', 'off12', 'off52')
OUT = []


def say(s=''):
    OUT.append(s)
    print(s, flush=True)


def guard(where):
    f = INT.free_mb()
    say('  free MB %d at %s ; one process ; hold %d -- %s' % (f, where, INT.HOLD_MB, 'MET' if f >= INT.HOLD_MB else 'REFUSED'))
    if f < INT.HOLD_MB:
        sys.exit('### FREE MEMORY BENEATH THE HOLD -- REFUSED (nothing computed after this line)')


def z0(s):
    ctx.prec = PREC
    v = CERT.zq_point(acb(s))
    ctx.prec = PREC
    return v


def z1(s):
    v, _M = INT.zq_form(acb(s), 2, 1, 23, PREC)
    ctx.prec = PREC
    return v


def rot(t):
    """the phase making Lambda real on the line: (sqrt23 / 2pi)^(it) Gamma(1/2 + it) / |...|."""
    ctx.prec = PREC
    s = acb(arb(1) / 2, arb(t))
    th = arb(t) * (arb(23).sqrt() / (2 * arb.pi())).log() + s.lgamma().imag
    return acb(th.cos(), th.sin())


def rows():
    zs, top = INT.zeros()
    import b709_pairs as P9
    import b711_list as L11
    allr = P9.extended_rows(L11.units(), top)[0]
    return zs, allr, top


def nearest(name, sg, tt, allr):
    best = None
    for n, s2, t2 in allr:
        if n == name:
            continue
        d = math.hypot(float(s2.mid()) - float(sg.mid()), float(t2.mid()) - float(tt.mid()))
        if best is None or d < best[0]:
            best = (d, n, float(s2.mid()), float(t2.mid()))
    return best


def line_zeros(F, g):
    """the sign changes of Re(rot(t) F(1/2 + it)) on |t - g| <= WIN, step STEP, each refined by bisection to 1e-8; (t, |Im| over |Re| at the
    grid's largest) for the reality check."""
    pts, imr = [], 0.0
    t = g - WIN
    while t <= g + WIN + 1e-12:
        v = rot(t) * F(acb(arb(1) / 2, arb(t)))
        re, im = float(v.real.mid()), float(v.imag.mid())
        imr = max(imr, abs(im) / max(abs(re), 1e-30) if abs(re) > 1e-3 else 0.0)
        pts.append((t, re))
        t += STEP
    out = []
    for (ta, ra), (tb, rb) in zip(pts, pts[1:]):
        if ra == 0 or ra * rb < 0:
            lo, hi, flo = ta, tb, ra
            for _ in range(24):
                mid = (lo + hi) / 2
                fm = float((rot(mid) * F(acb(arb(1) / 2, arb(mid)))).real.mid())
                if fm * flo <= 0:
                    hi = mid
                else:
                    lo, flo = mid, fm
            out.append((lo + hi) / 2)
    return out, imr


def zk(s):
    return (z0(s) + 2 * z1(s)) / 2


def lpsi(s):
    return (z0(s) - z1(s)) / 2


def deriv(F, s, h=arb('1e-12')):
    ctx.prec = PREC
    return (F(acb(s) + h) - F(acb(s) - h)) / (2 * h)


def criteria(*a):
    say('## (a) THE CANDIDATES: the three leading rows of data/b725_interference.txt :32-:34, in decreasing beta - 1/2 (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    guard('criteria')
    zs, allr, top = rows()
    say('  b711`s list complete to %s ; rows %d ; off-line with beta > 1/2: %d' % (top, len(allr), len(zs)))
    by = dict((n, (sg, tt)) for n, sg, tt in zs)
    for name in CANDIDATES:
        sg, tt = by[name]
        g = float(tt.mid())
        t0 = time.time()
        nz = nearest(name, sg, tt, allr)
        kz, kim = line_zeros(zk, g)
        lz, lim = line_zeros(lpsi, g)
        b = float(sg.mid()) - 0.5
        dk = min((math.hypot(b, g - t) for t in kz), default=None)
        dl = min((math.hypot(b, g - t) for t in lz), default=None)
        rho = acb(sg.mid(), tt.mid())
        d0 = deriv(z0, rho)
        zr = z0(rho)
        say('  %-6s beta - 1/2 %s ; gamma %s' % (name, (sg - arb(1) / 2).mid().str(10, radius=False), tt.mid().str(10, radius=False)))
        say('         the nearest other zero of Z_Q0: %s at (%.6f, %.6f), distance %.6f' % (nz[1], nz[2], nz[3], nz[0]))
        say('         zeta_K`s zeros on the line in |t - gamma| <= %.0f: %d %s ; the nearest at distance %s ; the reality check |Im|/|Re| %.1e' % (
            WIN, len(kz), ['%.6f' % t for t in kz], '%.6f' % dk if dk is not None else 'NONE', kim))
        say('         L(psi)`s zeros on the line in |t - gamma| <= %.0f: %d %s ; the nearest at distance %s ; the reality check |Im|/|Re| %.1e' % (
            WIN, len(lz), ['%.6f' % t for t in lz], '%.6f' % dl if dl is not None else 'NONE', lim))
        say('         |Z_Q0(rho)| at the banked centre %s ; |Z_Q0`(rho)| %s (central difference, h 1e-12) ; %.1f s' % (
            abs(zr).mid().str(5, radius=False), abs(d0).mid().str(8, radius=False), time.time() - t0))


def _edge_pts(c0, c1, n):
    return [c0 + (c1 - c0) * k / n for k in range(n)]


def _box(label, x0, x1, y0, y1, allr, n_edge, rho=None):
    say('  ## BOX %s: [%.6f, %.6f] x [%.6f, %.6f]' % (label, x0, x1, y0, y1))
    say('     corners (%.6f, %.6f) (%.6f, %.6f) (%.6f, %.6f) (%.6f, %.6f)' % (x0, y0, x1, y0, x1, y1, x0, y1))
    inside = [(n, float(s.mid()), float(t.mid())) for n, s, t in allr if x0 < float(s.mid()) < x1 and y0 < float(t.mid()) < y1]
    say('     the list`s zeros inside: %d %s' % (len(inside), ['%s (%.6f, %.6f)' % z for z in inside]))
    near = min(min(abs(float(s.mid()) - x) for x in (x0, x1)) if y0 <= float(t.mid()) <= y1 else
               (min(abs(float(t.mid()) - y) for y in (y0, y1)) if x0 <= float(s.mid()) <= x1 else
                min(math.hypot(float(s.mid()) - x, float(t.mid()) - y) for x in (x0, x1) for y in (y0, y1))) for n, s, t in allr)
    say('     the nearest listed zero to the boundary: %.6f' % near)
    C = [complex(x0, y0), complex(x1, y0), complex(x1, y1), complex(x0, y1)]
    per = 2 * ((x1 - x0) + (y1 - y0))
    mn, mx_d, args, prev, wind = None, 0.0, [], None, 0.0
    t0 = time.time()
    for i in range(4):
        a, b = C[i], C[(i + 1) % 4]
        for z in _edge_pts(a, b, n_edge):
            s = acb(arb(z.real), arb(z.imag))
            v = z0(s)
            m = float(abs(v).mid())
            mn = m if mn is None else min(mn, m)
            dv = deriv(z0, s, arb('1e-8'))
            mx_d = max(mx_d, float(abs(dv).mid()))
            w = complex(float(v.real.mid()), float(v.imag.mid()))
            if prev is not None:
                q = w / prev
                wind += math.atan2(q.imag, q.real)
            prev = w
    if prev is not None:
        s = acb(arb(C[0].real), arb(C[0].imag))
        v = z0(s)
        w = complex(float(v.real.mid()), float(v.imag.mid()))
        q = w / prev
        wind += math.atan2(q.imag, q.real)
    need = int(math.ceil(per * mx_d / mn)) + 1
    say('     sampled %d points a side (%d in all), %.1f s: the least |Z_Q0| on the boundary %.6f (THE MARGIN, sampled) ; the largest |Z_Q0`| %.4f' % (
        n_edge, 4 * n_edge, time.time() - t0, mn, mx_d))
    say('     the winding of the sample, (1/2pi) SUM arg ratios: %.6f (a float, not a count) ; the perimeter %.6f' % (wind / (2 * math.pi), per))
    say('     R1, a Lipschitz route: steps of length delta with L delta < m keep each step`s argument change below pi/2 ; at L = %.4f, m = %.6f the '
        'sample count wanted is perimeter L / m + 1 = %d (with a rigorous L on the boundary in place of the sampled one)' % (mx_d, mn, need))
    if rho is not None:
        d1 = deriv(z0, rho)
        r = min(x1 - float(rho.real.mid()), float(rho.real.mid()) - x0, y1 - float(rho.imag.mid()), float(rho.imag.mid()) - y0)
        m2 = 0.0
        for k in range(32):
            th = 2 * math.pi * k / 32
            s = rho + acb(arb(r / 2 * math.cos(th)), arb(r / 2 * math.sin(th)))
            dd = (deriv(z0, s + arb('1e-6')) - deriv(z0, s - arb('1e-6'))) / (2 * arb('1e-6'))
            m2 = max(m2, float(abs(dd).mid()))
        rr = 2 * float(abs(d1).mid()) / m2 if m2 else float('inf')
        say('     R2, Rouche against the linear model Z_Q0`(rho)(s - rho): |Z_Q0`(rho)| %.6f ; the largest sampled |Z_Q0``| on |s - rho| = %.4f: %.4f ; '
            'the admissible radius r < 2|Z`|/max|Z``| = %.6f (sampled, not a bound) ; the square`s inscribed radius %.6f' % (float(abs(d1).mid()), r / 2, m2, rr, r))
    return mn, mx_d, need


def box(*a):
    say('## (b) THE BOX around off0 (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    guard('box')
    zs, allr, top = rows()
    by = dict((n, (sg, tt)) for n, sg, tt in zs)
    sg, tt = by['off0']
    b, g = float(sg.mid()), float(tt.mid())
    rho = acb(sg.mid(), tt.mid())
    h = 0.1
    _box('A (a square of half-side %.2f centred on off0)' % h, b - h, b + h, g - h, g + h, allr, 40, rho)
    x0 = 0.75
    hb = 1.0
    _box('B (the right edge at Re s = 3/2, the left at %.2f between the line and off0, half-height %.2f)' % (x0, hb), x0, 1.5, g - hb, g + hb, allr, 80)


def main():
    a = sys.argv[1:]
    bank = '--bank' in a
    a = [x for x in a if x != '--bank']
    route = a[0] if a else ''
    if route not in ('criteria', 'box', 'both'):
        sys.exit('usage: b737_offlinezero.py criteria|box|both [--bank]')
    say('b737 -- W-ORD-ZQ-OFFLINE-ZERO`S PLAN FIGURES, (R347)(3)(a)-(b); no build, no Lean file, no dispatch; each figure sampled or banked as named, none a proof')
    say('')
    if route in ('criteria', 'both'):
        criteria()
        say('')
    if route in ('box', 'both'):
        box()
        say('')
    if bank:
        txt = NL.join(OUT) + NL
        with io.open(BANK % route, 'w', encoding='utf-8', newline='') as fh:
            fh.write(txt)
        print('  banked %s, %d lines' % (os.path.relpath(BANK % route, ROOT), len(OUT)))


if __name__ == '__main__':
    main()
