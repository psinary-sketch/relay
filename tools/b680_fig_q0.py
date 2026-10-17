# -*- coding: utf-8 -*-
"""b680_fig_q0.py -- (R290)(7): THE Q0 CONFIGURATION -- THE 163 NARROWED POINTS, THE DOMINANT PAIR MARKED, THE STRIP (-1/2, 3/2) DRAWN.
Writes data/b680_fig_q0.png and nothing else.

### The inputs, read as committed (no computation re-run; no lean):
###   data/b671_epstein_zeros_narrowed.json.gz -- rows are certified points (kind ON or OFF, re, im, half-width h); its sha256 51d9e6322510b738
###     and the JSON inside cd3a8ea1dcc7660c (data/b671_epstein_zeros_narrowed_hashes.txt :2-:3), checked here before reading; rows 163
###     (ON 146, OFF 17), as data/b679_q0_membership.txt :4 prints them.
###   data/b673_v4_control.txt :7 (idx 0, rho = 0.953260474794660686 + 16.29021572039039079i) and :24 ("the dominant pair: rho` of idx 0 and
###     its conjugate", rho` = 1 - conj rho) -- the pair is drawn at rho` and conj rho`, located here as the OFF row whose re and im match :7.
### The 163 points are plotted as the bank holds them (the upper half-plane, sigma >= 1/2); the dominant pair`s two points are the bank`s
### idx-0 point reflected, drawn apart. Drawn with PIL (matplotlib is not installed on this host). A bank for the keystones` later use, in no
### document; strikeable. Run: `python -X utf8 tools/b680_fig_q0.py`.
"""
import gzip
import hashlib
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
SRC = os.path.join(D, 'b671_epstein_zeros_narrowed.json.gz')
OUT = os.path.join(D, 'b680_fig_q0.png')
SHA_GZ, SHA_JSON = '51d9e6322510b738', 'cd3a8ea1dcc7660c'
IDX0 = (0.953260474794660686, 16.29021572039039079)      # ### data/b673_v4_control.txt :7


def font(n):
    try:
        return ImageFont.load_default(size=n)
    except TypeError:
        return ImageFont.load_default()


def main():
    raw = open(SRC, 'rb').read()
    inner = gzip.decompress(raw)
    hg, hj = hashlib.sha256(raw).hexdigest(), hashlib.sha256(inner).hexdigest()
    if not (hg.startswith(SHA_GZ) and hj.startswith(SHA_JSON)):
        sys.exit('### THE INPUT`S HASHES DIFFER FROM b671`s BANK (%s, %s) -- NOTHING WRITTEN' % (hg[:16], hj[:16]))
    rows = json.loads(inner.decode('utf-8'))['rows']
    pts = [(r['kind'], float(r['re']), float(r['im'])) for r in rows]
    dom = [p for p in pts if p[0] == 'OFF' and abs(p[1] - IDX0[0]) < 1e-12 and abs(p[2] - IDX0[1]) < 1e-12]
    if len(rows) != 163 or len(dom) != 1:
        sys.exit('### ROWS %d (163 expected), THE idx-0 POINT FOUND %d TIMES (1 expected) -- NOTHING WRITTEN' % (len(rows), len(dom)))
    pr = (1 - dom[0][1], dom[0][2])                       # ### rho` = 1 - conj rho
    pair = (pr, (pr[0], -pr[1]))
    W, H = 900, 1500
    x0, y0, x1, y1 = 110, 70, W - 40, H - 90
    xl, xh, yl, yh = -1.0, 2.0, -25.0, 155.0
    X = lambda s: x0 + (s - xl) * (x1 - x0) / (xh - xl)
    Y = lambda t: y1 - (t - yl) * (y1 - y0) / (yh - yl)
    im = Image.new('RGB', (W, H), 'white')
    dr = ImageDraw.Draw(im)
    f14, f18 = font(14), font(18)
    dr.text((20, 10), 'b680 -- the Q0 configuration: the 163 narrowed points (b671), the dominant pair (b673), the strip (-1/2, 3/2)',
            fill='black', font=f14)
    dr.rectangle((X(-0.5), y0, X(1.5), y1), fill=(238, 244, 252))
    dr.rectangle((x0, y0, x1, y1), outline='black')
    for s in (-0.5, 1.5):
        for ys in range(int(y0), int(y1), 12):
            dr.line((X(s), ys, X(s), min(ys + 6, y1)), fill=(60, 90, 160), width=2)
    for ys in range(int(y0), int(y1), 6):
        dr.point((X(0.5), ys), fill=(150, 150, 150))
    dr.line((x0, Y(0), x1, Y(0)), fill=(150, 150, 150))
    for s in (-1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0):
        dr.line((X(s), y1, X(s), y1 + 5), fill='black')
        dr.text((X(s) - 12, y1 + 8), '%g' % s, fill='black', font=f14)
    for t in range(-20, 160, 20):
        dr.line((x0 - 5, Y(t), x0, Y(t)), fill='black')
        dr.text((x0 - 40, Y(t) - 7), '%d' % t, fill='black', font=f14)
    dr.text(((x0 + x1) / 2 - 30, y1 + 30), 'Re s', fill='black', font=f14)
    dr.text((20, (y0 + y1) / 2), 'Im s', fill='black', font=f14)
    for k, s, t in pts:
        c = (40, 40, 40) if k == 'ON' else (200, 40, 40)
        dr.ellipse((X(s) - 3, Y(t) - 3, X(s) + 3, Y(t) + 3), fill=c)
    for s, t in pair:
        dr.ellipse((X(s) - 9, Y(t) - 9, X(s) + 9, Y(t) + 9), outline=(20, 130, 40), width=3)
        dr.text((X(s) + 12, Y(t) - 8), '%s rho`' % ('' if t > 0 else 'conj'), fill=(20, 130, 40), font=f14)
    for n, (c, lab) in enumerate((((40, 40, 40), 'ON (146)'), ((200, 40, 40), 'OFF (17)'), ((20, 130, 40), 'the dominant pair: rho` = 1 - conj rho of idx 0, and its conjugate'))):
        yy = H - 40 + 0 * n
        xx = 30 + n * 160
        dr.ellipse((xx, yy, xx + 8, yy + 8), fill=c)
        dr.text((xx + 14, yy - 4), lab, fill='black', font=f14)
    dr.text((30, H - 20), 'shaded, dashed: the strip -1/2 < Re s < 3/2 ; dotted: Re s = 1/2', fill='black', font=f14)
    im.save(OUT + '.tmp.png', format='PNG')
    os.replace(OUT + '.tmp.png', OUT)
    print('  data/b680_fig_q0.png written: %d bytes ; points %d (ON %d, OFF %d) ; the pair at %.6f +/- %.6fi ; inputs sha256 %s %s EQUAL' % (
        os.path.getsize(OUT), len(pts), sum(1 for p in pts if p[0] == 'ON'), sum(1 for p in pts if p[0] == 'OFF'), pr[0], pr[1], hg[:16], hj[:16]))


if __name__ == '__main__':
    main()
