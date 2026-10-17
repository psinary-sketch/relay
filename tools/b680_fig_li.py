# -*- coding: utf-8 -*-
"""b680_fig_li.py -- (R290)(7): THE LI INDEX AT Q0 -- P_n + U_n OVER THE WINDOW, n_obs AND n*' MARKED. Writes data/b680_fig_li.png and nothing else.

### The inputs, read as committed (no computation re-run; no lean):
###   data/b675_li_bench.json -- `rows` (rows are n: P_n, U_n and P_n + U_n as Arb balls, the sign), every 100th n over [1, 63876] and the window
###     [63676, 63876] whole, as data/b675_li_bench.txt :3-:7 states; `runs`, the sign run-length line over every n; `window`. The midpoint of
###     each P_n + U_n ball is plotted (every ball`s sign certified, UNDECIDED 0: data/b675_li_bench.txt :848).
###   n_obs = 10034, the least n with P_n + U_n certified below 0: data/b675_li_bench.txt :848.
###   n*' = 63676: data/b679_onset.txt :12 (b675`s n* 63676 beside it). U_n is the plan`s inequality under T-COUNT, an ASSUMPTION
###     (data/b675_li_bench.txt :4-:5).
### Panel (a): [1, 63876], the value as sign(v)·log10(1 + |v|), the sign runs drawn as a strip beneath. THE CURVE IN (a) IS AN ALIAS: the
###     rows sample every 100th n, and P_n + U_n oscillates with period 2π/θ ≈ 102.47 (θ = 0.0613198770..., data/b673_v4_control.txt :26), so
###     the sampled curve shows the beat, period 1/|1/100 - θ/2π| ≈ 4150 n, not the n-dependence; the strip (every n, from `runs`) and panel
###     (b) (every n of the window) carry the true signs. Printed on the figure. Panel (b): the window [63676, 63876],
### the value in units of 1e47. Drawn with PIL (matplotlib is not installed on this host). A bank for the keystones` later use, in no document;
### strikeable. Run: `python -X utf8 tools/b680_fig_li.py`.
"""
import json
import math
import os
import re
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b680_fig_li.png')
N_OBS, N_STAR_P = 10034, 63676       # ### data/b675_li_bench.txt :848 ; data/b679_onset.txt :12
MID = re.compile(r'^\[([-+0-9.e]+)')
NEG_C, POS_C, LINE_C = (200, 40, 40), (40, 110, 60), (30, 60, 160)


def font(n):
    try:
        return ImageFont.load_default(size=n)
    except TypeError:
        return ImageFont.load_default()


def slog(v):
    return math.copysign(math.log10(1 + abs(v)), v)


def dashed(dr, x, ya, yb, col):
    for y in range(int(ya), int(yb), 10):
        dr.line((x, y, x, min(y + 5, yb)), fill=col, width=2)


def main():
    B = json.load(open(os.path.join(D, 'b675_li_bench.json'), encoding='utf-8'))
    if B['n_obs'] != N_OBS or B['n_star'] != N_STAR_P:
        sys.exit('### THE BENCH`S n_obs %s OR n* %s DIFFERS FROM THE CITED %d, %d -- NOTHING WRITTEN' % (B['n_obs'], B['n_star'], N_OBS, N_STAR_P))
    rows = [(r['n'], float(MID.match(r['PU']).group(1)), r['sign']) for r in B['rows']]
    lo, hi = B['window']['window']
    W, H = 1800, 760
    im = Image.new('RGB', (W, H), 'white')
    dr = ImageDraw.Draw(im)
    f14, f18 = font(14), font(18)
    dr.text((20, 10), 'b680 -- the Li index at Q0: P_n + U_n (U_n under T-COUNT, an assumption), n_obs and n*\' marked', fill='black', font=f18)
    # ### panel (a): the whole bench range
    x0, y0, x1, y1 = 90, 70, 1000, 620
    nl, nh = 1, B['hi']
    yl, yh = -50.0, 50.0
    X = lambda n: x0 + (n - nl) * (x1 - x0) / float(nh - nl)
    Y = lambda v: y1 - (v - yl) * (y1 - y0) / (yh - yl)
    dr.rectangle((x0, y0, x1, y1), outline='black')
    dr.text((x0, y0 - 22), '(a) n in [1, %d]: sign(v) log10(1 + |v|), every 100th n and the window; strip: the sign of every n' % nh, fill='black', font=f14)
    dr.line((x0, Y(0), x1, Y(0)), fill=(150, 150, 150))
    for v in range(-50, 51, 10):
        dr.line((x0 - 5, Y(v), x0, Y(v)), fill='black')
        dr.text((x0 - 40, Y(v) - 7), '%d' % v, fill='black', font=f14)
    for n in range(0, nh + 1, 10000):
        dr.line((X(max(n, 1)), y1, X(max(n, 1)), y1 + 5), fill='black')
        dr.text((X(max(n, 1)) - 16, y1 + 30), '%d' % n, fill='black', font=f14)
    for s, a, b in B['runs']:
        dr.rectangle((X(a), y1 + 8, max(X(b), X(a) + 0.5), y1 + 22), fill=NEG_C if s == 'NEG' else POS_C)
    seq = [(X(n), Y(slog(v))) for n, v, _s in rows]
    dr.line(seq, fill=LINE_C, width=1)
    for (n, v, s), (px, py) in zip(rows, seq):
        dr.ellipse((px - 1.5, py - 1.5, px + 1.5, py + 1.5), fill=NEG_C if s == 'NEG' else LINE_C)
    for n, lab in ((N_OBS, 'n_obs %d' % N_OBS), (N_STAR_P, 'n*\' %d' % N_STAR_P)):
        dashed(dr, X(n), y0, y1, (0, 0, 0))
        dr.text((X(n) + 4 if n < 50000 else X(n) - 110, y0 + 6), lab, fill='black', font=f14)
    dr.text(((x0 + x1) / 2 - 4, y1 + 50), 'n', fill='black', font=f14)
    # ### panel (b): the window
    u0, v0, u1, v1 = 1110, 70, 1760, 620
    vals = [(n, v / 1e47, s) for n, v, s in rows if lo <= n <= hi]
    ml, mh = math.floor(min(v for _n, v, _s in vals)), math.ceil(max(v for _n, v, _s in vals))
    U = lambda n: u0 + (n - lo) * (u1 - u0) / float(hi - lo)
    V = lambda v: v1 - (v - ml) * (v1 - v0) / float(mh - ml)
    dr.rectangle((u0, v0, u1, v1), outline='black')
    dr.text((u0, v0 - 22), '(b) the window [%d, %d], all %d n: P_n + U_n / 1e47' % (lo, hi, len(vals)), fill='black', font=f14)
    dr.line((u0, V(0), u1, V(0)), fill=(150, 150, 150))
    for v in range(ml, mh + 1):
        dr.line((u0 - 5, V(v), u0, V(v)), fill='black')
        dr.text((u0 - 30, V(v) - 7), '%d' % v, fill='black', font=f14)
    for n in range(lo, hi + 1, 50):
        dr.line((U(n), v1, U(n), v1 + 5), fill='black')
        dr.text((U(n) - 20, v1 + 8), '%d' % n, fill='black', font=f14)
    sq = [(U(n), V(v)) for n, v, _s in vals]
    dr.line(sq, fill=LINE_C, width=1)
    for (n, v, s), (px, py) in zip(vals, sq):
        dr.ellipse((px - 2, py - 2, px + 2, py + 2), fill=NEG_C if s == 'NEG' else POS_C)
    dashed(dr, U(N_STAR_P), v0, v1, (0, 0, 0))
    dr.text((U(N_STAR_P) + 4, v0 + 6), 'n*\' %d' % N_STAR_P, fill='black', font=f14)
    dr.text(((u0 + u1) / 2 - 4, v1 + 30), 'n', fill='black', font=f14)
    theta = 0.0613198770021965645581628       # ### data/b673_v4_control.txt :26
    dr.text((560, H - 42), '(a)`s curve is an ALIAS: rows every 100th n against the period 2pi/theta = %.2f; the beat %.0f n is not the '
            'n-dependence -- the strip and (b) carry the true signs' % (2 * math.pi / theta, 1 / abs(1 / 100.0 - theta / (2 * math.pi))),
            fill=(160, 20, 20), font=f14)
    for k, (c, lab) in enumerate(((NEG_C, 'NEG (certified below 0)'), (POS_C, 'NONNEG'))):
        dr.rectangle((40 + k * 260, H - 40, 54 + k * 260, H - 28), fill=c)
        dr.text((60 + k * 260, H - 42), lab, fill='black', font=f14)
    im.save(OUT + '.tmp.png', format='PNG')
    os.replace(OUT + '.tmp.png', OUT)
    print('  data/b680_fig_li.png written: %d bytes ; rows %d ; window rows %d (NEG %d) ; runs %d ; n_obs %d ; n*` %d' % (
        os.path.getsize(OUT), len(rows), len(vals), sum(1 for x in vals if x[2] == 'NEG'), len(B['runs']), N_OBS, N_STAR_P))


if __name__ == '__main__':
    main()
