# -*- coding: utf-8 -*-
"""b526_xi7.py -- COMPONENT 1: XI ON VARIANT (B) AT RAMP ORDER 7, THE REACH PER WIDTH. ### `python tools/b526_xi7.py run [a_lo a_hi]`

### The window is b521`s `PWindow(a, 'xi', 7)` -- b519`s variant (B) with the inner B-spline at order 7, gamma_0 = 14.1347 --
### IMPORTED; the cell is b519`s xi branch with that window: the atlas bank to 9877.78, the exact transform, the prime channel
### by Gauss-Legendre (QL = 40, QH = 60), the tail b519`s numerical majorant above the bank`s top (zeros there taken ON the line,
### as b519 and b520 read xi), the u > 1200 shortfall an ESTIMATE outside B. ### (R131)(2): IN iff E_tail <= B` at the width.
### Resumable: widths already banked are skipped, so the pass runs in chunks inside the tool`s time limit.
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
import b519_window as B19   # noqa: E402
import b521_tail as B21     # noqa: E402

NL = chr(10)
P = 7
GRID = [float(a) for a in range(15, 61)]
OUT = os.path.join(D, 'b526_xi7_cells.jsonl')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def cell_xi(a):
    W = B21.PWindow(a, 'xi', P)
    kz = 'z'
    Hb, Hh, Hw = W.khat(F.U_BASE).real, W.khat(F.U_HALF).real, W.khat(F.U_WIDE).real
    A = F.arch(Hb, F.U_BASE, F.KER[kz + '_base'])
    Eu = abs(F.arch(Hh, F.U_HALF, F.KER[kz + '_half']) - A) + abs(F.arch(Hw, F.U_WIDE, F.KER[kz + '_wide']) - A)
    PR, PRabs = F.prime_channel_xi(W, B19.QL)
    PR2, _ = F.prime_channel_xi(W, B19.QH)
    G = F.GAM
    zt = 2.0 * W.khat(G).real
    Zon = float(np.sum(zt))
    ip = int(np.argmin(np.abs(G - B19.G0['xi'])))
    pair, others, on_rest = float(zt[ip]), 0.0, Zon - float(zt[ip])
    Etail = B19.tail(W, float(G[-1]), 'xi')
    dk = np.abs(2.0 * (W.khat(G * (1 + F.DELTA_XI)).real - W.khat(G).real))
    P_ = float((W.khat(0.5j) + W.khat(-0.5j)).real)
    Z = Zon
    r = Z - (P_ - PR + A)
    Ek = abs(PR - PR2)
    Aabs = float(np.trapezoid(np.abs(Hb * F.KER[kz + '_base']), F.U_BASE) / (2.0 * math.pi))
    Eround = 4.0 * F.EPS * (float(np.sum(np.abs(zt))) + Aabs + PRabs) + float(np.sum(dk))
    B = Eu + Ek + Etail + Eround
    gr, bound = W.growth()
    rest = Z - pair
    return dict(a=a, p=P, gamma0=B19.G0['xi'], A=A, PR=PR, P=P_, Z=Z, Z_on=Zon, pair=pair, others=others, on_rest=on_rest,
                rest=rest, ratio=pair / rest if rest else None, h2=P_ - PR + A, r=r, B=B, Bprime=Eu + Ek + Eround, Eu=Eu, Ek=Ek,
                Etail=Etail, Eround=Eround, tail_share=Etail / B, shortfall=B19.shortfall(W, kz), verified=bool(abs(r) <= B),
                within=bool(Etail <= Eu + Ek + Eround), growth=gr, growth_bound=bound, growth_fraction=gr / bound,
                nv=None, nv_note='closed-form transform: no v-grid -- (R114)`s rule has no object, as b511-b525 read it')


def run(lo=15.0, hi=60.0):
    done = set()
    if os.path.exists(OUT):
        done = {json.loads(l)['a'] for l in io.open(OUT, encoding='utf-8') if l.strip()}
    t0 = time.time()
    for a in GRID:
        if a < lo or a > hi or a in done:
            continue
        c = cell_xi(a)
        with io.open(OUT, 'a', encoding='utf-8', newline=NL) as fh:
            fh.write(json.dumps(c) + NL)
        print('[%s] a=%-4.0f h2 %+.4e B %.2e VER %s IN %s tail/B` %.1e ; %.0f s'
              % (time.strftime('%H:%M:%S'), a, c['h2'], c['B'], c['verified'], c['within'], c['Etail'] / c['Bprime'], time.time() - t0), flush=True)
    return 0


if __name__ == '__main__':
    if sys.argv[1] == 'run':
        lo, hi = (float(sys.argv[2]), float(sys.argv[3])) if len(sys.argv) > 3 else (15.0, 60.0)
        sys.exit(run(lo, hi))
