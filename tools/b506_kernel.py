# -*- coding: utf-8 -*-
"""b506_kernel.py -- COMPONENT 3: b326`S DERIVED KERNEL ON THE COMPLETED Q0 BANK, AT THE WIDE CELLS (a >= 5).

### `python tools/b506_kernel.py run | report`
### ### RUNS ONLY IF COMPONENT 2 CLOSED THE BANK: its whole-strip count equal to the located count, every box near
### an integer, the positive control recovered, and every located zero confirmed by route A within 1e-9 in the
### object`s units (|Z_A| / |Z`|, under (R116)(2)). Otherwise it refuses.
### The zero side: the banked on-line zeros, any on-line zero C2 located, and every off-line zero C2 located in the
### R column with its three images (conjugate, 1 - rho, 1 - conj rho) -- `b326_closure.hhat_exact` and `ftilde`,
### as b504. The grid: (R114)`s rule with T = 150, i.e. the least nv >= 8193 putting 2 pi (nv - 1)/L above 350.
### The places side: `b325_epstein.finite_channel` (LAMQ) and `b326_windows.kernel_q_derived`; the pole term
### `mellin_exact` at +-1/2. The bound: b501`s rule under the exact transform, as b504`s `B_qd`.
### ### The truncation above 150 is estimated per cell -- 2 INT_150^UMAX |hhat(t)| (1/pi) log(t sqrt 23 / 2 pi) dt,
### UMAX = 600 the places side`s own u-range -- and printed beside the bound; the ferry says it lies inside the
### bound at a >= 5, and each cell tests that.
"""
import io
import json
import math
import os
import sys
import multiprocessing as mpr
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'e16'))
import b317_smear as SM         # noqa: E402
import b318_square as SQ        # noqa: E402
import b325_epstein as EP       # noqa: E402
import b326_closure as BC       # noqa: E402
import b501_bound as BB         # noqa: E402
import b503_zero as BZ          # noqa: E402
import b504_chain as CH         # noqa: E402  ### kernels (banked npz), U grids, arch, pole -- imported

NL = chr(10)
TQ = 150.0
CELLS = os.path.join(D, 'b506_cells.jsonl')
C2 = os.path.join(D, 'b506_c2_results.json')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def bank_complete():
    r = json.loads(io.open(C2, encoding='utf-8').read())
    found = [z for z in r['found'] if z.get('rho')]
    ok = (r['not_near'] == 0 and all(r['control']) and all(z.get('inside') for z in r['found'])
          and all(z.get('route_a_dist', 1) < 1e-9 for z in found) and len(found) == len(r['found'])
          and abs(r['whole'] - r['total']) < 0.05)
    on = [z['gamma_a'] for z in CH.LIB['zeros']] + [z['rho'][1] for z in found if z['col'] == 'M']
    off = [z['rho'] for z in found if z['col'] == 'R']
    return ok, np.array(sorted(on)), off, r


def choose_nv(L):
    nv = 8193
    while 2 * math.pi * (nv - 1) / L <= TQ + 200.0:
        nv += 1
    return nv


def tail(v, w):
    t = np.linspace(TQ, float(CH.AT.UMAX), int(round((CH.AT.UMAX - TQ) / 0.05)) + 1)
    h = np.abs(BC.hhat_exact(v, w, t))
    dens = np.log(t * math.sqrt(23) / (2 * math.pi)) / math.pi
    return float(2.0 * np.trapezoid(h * dens, t))


def cell(a, K, on, off):
    g = SM.mean_zero_variant(a)
    L = 2.0 * abs(float(g.v[-1]))
    nv = choose_nv(L)
    lv = []
    for n in (nv, 2 * nv - 1, 4 * nv - 3):
        f = SQ.autocorrelation(g, n)
        v, w = np.asarray(f.v), np.asarray(f.w)
        H = BC.hhat_exact(v, w, CH.U_BASE)
        FQ = EP.finite_channel(v, w)[0]
        Ad = CH.arch(H, CH.U_BASE, K['qd_base'])
        lv.append(dict(v=v, w=w, H=H, FQ=FQ, Ad=Ad, md=Ad - FQ))
    b = lv[0]
    v, w = b['v'], b['w']
    Zon = 2.0 * float(np.sum(BC.hhat_exact(v, w, on)))
    Zoff = 0.0
    for bb, gg in off:
        for rho in (complex(bb, gg), complex(bb, -gg), complex(1 - bb, gg), complex(1 - bb, -gg)):
            Zoff += BC.ftilde(v, w, rho)[0].real
    P = CH.pole(v, w)
    Ev, kind, _o = BB.richardson(*[l['md'] for l in lv])
    Hh, Hw = BC.hhat_exact(v, w, CH.U_HALF), BC.hhat_exact(v, w, CH.U_WIDE)
    Eu = abs(CH.arch(Hh, CH.U_HALF, K['qd_half']) - b['Ad']) + abs(CH.arch(Hw, CH.U_WIDE, K['qd_wide']) - b['Ad'])
    B = Ev + Eu
    r = (Zon + Zoff) - (P - b['FQ'] + b['Ad'])
    tr = tail(v, w)
    return dict(a=a, nv=nv, image=2 * math.pi * (nv - 1) / L, Z_on=Zon, Z_off=Zoff, P=P, FQ=b['FQ'], Ad=b['Ad'],
                md=b['md'], B=B, kindR=kind, r=r, tail=tr, tail_inside=tr <= B, verified=abs(r) <= B)


def wide():
    return [x['a'] for x in BZ.rows_all() if x['a'] >= 5]


_K = _ON = _OFF = None


def _init():
    global _K, _ON, _OFF
    _K = CH.kernels()
    _ok, _ON, _OFF, _r = bank_complete()


def _one(a):
    t0 = time.time()
    c = cell(a, _K, _ON, _OFF)
    c['seconds'] = round(time.time() - t0, 1)
    return c


def run():
    ok, on, off, r = bank_complete()
    if not ok:
        print('### COMPONENT 2 DID NOT CLOSE THE BANK -- COMPONENT 3 IS NOT RUN.')
        return 2
    CH.kernels()
    A = wide()
    done = set()
    if os.path.exists(CELLS):
        done = {round(json.loads(l)['a'], 9) for l in io.open(CELLS, encoding='utf-8') if l.strip()}
    todo = [a for a in A if round(a, 9) not in done]
    print('wide cells %d ; to run %d ; on-line zeros %d ; off-line zeros (sigma > 1/2) %d'
          % (len(A), len(todo), len(on), len(off)), flush=True)
    with mpr.Pool(5, initializer=_init) as pool:
        for c in pool.imap_unordered(_one, todo):
            with io.open(CELLS, 'a', encoding='utf-8', newline=NL) as fh:
                fh.write(json.dumps(c) + NL)
            print('  a=%-10.6f nv %d  md %+.6f  |r| %.2e  B %.2e  tail %.1e %s  %s  %.0fs'
                  % (c['a'], c['nv'], c['md'], abs(c['r']), c['B'], c['tail'], 'in' if c['tail_inside'] else 'OUT',
                     'VERIFIED' if c['verified'] else '-', c['seconds']), flush=True)
    return 0


def report():
    """### the Component 3 bank read: the population of READING (5), the count verified, and WHERE it fails."""
    cs = sorted((json.loads(l) for l in io.open(CELLS, encoding='utf-8') if l.strip()), key=lambda c: c['a'])
    pop = [c for c in cs if c['tail_inside']]
    ver = [c for c in pop if c['verified']]
    bad = [c for c in pop if not c['verified']]
    L = ['=' * 104, 'b506 COMPONENT 3 -- b326`S DERIVED KERNEL ON THE COMPLETED BANK, THE WIDE CELLS.', '=' * 104,
         '  wide cells run : %d ; nv used : %s' % (len(cs), sorted(set(c['nv'] for c in cs))),
         '  TRUNCATION-OUTSIDE (tail above bound) : %d %s' % (len(cs) - len(pop), ['a=%.6f' % c['a'] for c in cs if not c['tail_inside']]),
         '  POPULATION : %d' % len(pop),
         '  VERIFIED IN THE POPULATION : %d' % len(ver),
         '  UNVERIFIED IN THE POPULATION : %s' % ' '.join('a=%.6f(|r| %.1e B %.1e)' % (c['a'], abs(c['r']), c['B']) for c in bad),
         '  VERIFIED OUTSIDE THE POPULATION (not counted) : %d' % sum(1 for c in cs if c['verified'] and not c['tail_inside'])]
    if bad:
        L.append('  ### ### **IT FAILS THERE -- STOP. THE KERNEL IS Q0`S OWN AND THERE IS NO FACTOR-WISE SUBSTITUTE.**')
    L.append('=' * 104)
    io.open(os.path.join(D, 'b506_c3.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L))
    return 0


if __name__ == '__main__':
    sys.exit({'run': run, 'report': report}[sys.argv[1]]())
