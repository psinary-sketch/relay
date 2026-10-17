# -*- coding: utf-8 -*-
"""b680_fig_tie.py -- (R290)(7): THE TIE DIAGNOSTIC, RADIUS PER j, b671 AGAINST b677'S ANGLE FORM. Writes data/b680_fig_tie.png and nothing else.

### The inputs, read as committed (no computation re-run; no lean):
###   data/b671_tie_diagnostic.txt (relay f8f2901d) -- rows are tie controls (the cell, the precision, j), :7-:129: the control Z1(0.8, 29.6) at
###     200 bits :7-:47, Q0 at qE0 at 200 bits :48-:88, Q0 at qE0 at 400 bits :89-:129; the column read is `rad max` (the separation`s ball`s
###     largest radius over the four tie nodes, b667`s map).
###   data/b677_map.txt (relay 7e328ed2) -- rows are ties in the same list, :6-:128 (:6-:46, :47-:87, :88-:128); the column read is `rad max`
###     in the angle form; the bar is each row`s `rad max` over its `rad/bar`, printed as the dashed line.
### One panel per cell, log10 of the radius against j. Drawn with PIL (matplotlib is not installed on this host). A bank for the keystones`
### later use, in no document; strikeable. Run: `python -X utf8 tools/b680_fig_tie.py`.
"""
import io
import math
import os
import re

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b680_fig_tie.png')
ROW = re.compile(r'^  (.+?)\s+(\d+) j (\d+) : .*rad max ([0-9.e+-]+) ; rad/bar ([0-9.e+-]+)')
CELLS = (('THE CONTROL Z₁(0.8, 29.6)', '200', 'control Z1(0.8, 29.6), 200 bits'), ('Q0 AT qE0', '200', 'Q0 at qE0, 200 bits'),
         ('Q0 AT qE0', '400', 'Q0 at qE0, 400 bits'))
SERIES = (('b671_tie_diagnostic.txt', (200, 40, 40), 'b671 (b667 map)'), ('b677_map.txt', (30, 80, 200), 'b677 (angle form)'))


def read(name):
    out = {}
    for i, l in enumerate(io.open(os.path.join(D, name), encoding='utf-8').read().replace(chr(13), '').split(chr(10)), 1):
        m = ROW.match(l)
        if m:
            rad, ratio = float(m.group(4)), float(m.group(5))
            out.setdefault((m.group(1).strip(), m.group(2)), []).append((int(m.group(3)), rad, rad / ratio, i))
    return out


def font(n):
    try:
        return ImageFont.load_default(size=n)
    except TypeError:
        return ImageFont.load_default()


def main():
    data = [(read(f), col, lab) for f, col, lab in SERIES]
    W, H, PW = 1800, 640, 560
    im = Image.new('RGB', (W, H), 'white')
    dr = ImageDraw.Draw(im)
    f14, f18 = font(14), font(18)
    dr.text((20, 10), 'b680 -- the tie diagnostic: log10 of the radius (rad max) per j, b671 against b677`s angle form; dashed: the bar', fill='black', font=f18)
    for k, (cell, prec, title) in enumerate(CELLS):
        x0, y0, x1, y1 = 40 + k * (PW + 30) + 50, 60, 40 + k * (PW + 30) + PW, H - 60
        pts = [(j, math.log10(r), math.log10(b)) for d, _c, _l in data for (j, r, b, _i) in d[(cell, prec)]]
        jl, jh = min(p[0] for p in pts), max(p[0] for p in pts)
        yl = math.floor(min(min(p[1], p[2]) for p in pts) / 5) * 5
        yh = math.ceil(max(max(p[1], p[2]) for p in pts) / 5) * 5
        X = lambda j: x0 + (j - jl) * (x1 - x0) / float(jh - jl)
        Y = lambda v: y1 - (v - yl) * (y1 - y0) / float(yh - yl)
        dr.rectangle((x0, y0, x1, y1), outline='black')
        dr.text((x0, y0 - 22), title, fill='black', font=f14)
        for v in range(int(yl), int(yh) + 1, 10):
            dr.line((x0 - 4, Y(v), x0, Y(v)), fill='black')
            dr.text((x0 - 44, Y(v) - 7), '%d' % v, fill='black', font=f14)
        for j in range(jl, jh + 1, 10):
            dr.line((X(j), y1, X(j), y1 + 4), fill='black')
            dr.text((X(j) - 8, y1 + 6), '%d' % j, fill='black', font=f14)
        dr.text(((x0 + x1) / 2 - 4, y1 + 24), 'j', fill='black', font=f14)
        bar = data[1][0][(cell, prec)][0][2]
        for xs in range(int(x0), int(x1), 12):
            dr.line((xs, Y(math.log10(bar)), min(xs + 6, x1), Y(math.log10(bar))), fill=(120, 120, 120))
        for d, col, _lab in data:
            seq = [(X(j), Y(math.log10(r))) for (j, r, _b, _i) in d[(cell, prec)]]
            dr.line(seq, fill=col, width=2)
            for (px, py) in seq:
                dr.ellipse((px - 2, py - 2, px + 2, py + 2), fill=col)
    for n, (_d, col, lab) in enumerate(data):
        dr.line((1200 + n * 260, 20, 1230 + n * 260, 20), fill=col, width=3)
        dr.text((1236 + n * 260, 12), lab, fill='black', font=f14)
    im.save(OUT + '.tmp.png', format='PNG')
    os.replace(OUT + '.tmp.png', OUT)
    print('  data/b680_fig_tie.png written: %d bytes ; series %s ; rows per series %s' % (
        os.path.getsize(OUT), [s[2] for s in SERIES], [sum(len(v) for v in d.values()) for d, _c, _l in data]))


if __name__ == '__main__':
    main()
