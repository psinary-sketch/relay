# -*- coding: utf-8 -*-
"""b501_bound.py -- COMPONENTS 1 TO 4: THE PLACES-SIDE QUADRATURE BOUND, BUILT AND TESTED.

### `python tools/b501_bound.py quote | cells I J | controls | report`
### ### **THE RULE IS THE FACE`S, SEALED BEFORE THIS RAN** -- `B = E_v + E_u`; E_v by Richardson over
### `nv` = 8193, 16385, 32769 with the NON-ASYMPTOTIC fallback `2(|d1|+|d2|)`; E_u by halving the
### u-spacing and doubling the u-range. ### **NO CHAIN INSTRUMENT IS EDITED**: `b321_window`,
### `carto_atlas`, `b318_square` and `b317_smear` are imported and called; the u-grid is changed by
### computing A with `carto_atlas.kernel` on the new grid after RESETTING its one-grid cache, and the
### cache is restored to the base grid after every use.
### ### **EACH CELL IS APPENDED TO `b501_cells.jsonl` AS IT FINISHES**, so the run is resumable in
### chunks and no long job needs to live in the background.
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
sys.path.insert(0, os.path.join(T, 'e16'))
import carto_atlas as AT        # noqa: E402
import b317_smear as SM         # noqa: E402
import b318_square as SQ        # noqa: E402
import b321_window as WI        # noqa: E402

NL = chr(10)
LEVELS = (8193, 16385, 32769)
COARSE = (2049, 4097, 8193)
CELLS = os.path.join(D, 'b501_cells.jsonl')
U_BASE = np.linspace(-AT.UMAX, AT.UMAX, AT.NU)
U_HALF = np.linspace(-AT.UMAX, AT.UMAX, 2 * AT.NU - 1)
U_WIDE = np.linspace(-2 * AT.UMAX, 2 * AT.UMAX, 2 * AT.NU - 1)
_K = {}

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def kern(name, U):
    """### ### **THE INSTRUMENT`S OWN `kernel`, ON A NAMED GRID, WITH ITS CACHE RESET FIRST.**"""
    if name not in _K:
        AT._KERN = None
        K = AT.kernel(U)
        if len(K) != len(U):
            raise SystemExit('### THE KERNEL CACHE RETURNED %d VALUES FOR A GRID OF %d' % (len(K), len(U)))
        _K[name] = np.array(K)
        AT._KERN = None
    AT._KERN = _K.get('base') if 'base' in _K else None   # ### restored to the base grid
    return _K[name]


def arch(v, w, U, K):
    return float(np.trapezoid(WI.hhat_blocked(v, w, U) * K, U) / (2.0 * math.pi))


def margin_at(v, w, K):
    A = arch(v, w, U_BASE, K)
    PR, _ = WI.prime_sum(v, w, 'corpus')
    return A, PR, A - PR


def richardson(x1, x2, x3):
    """### ### **THE SEALED RULE.**"""
    d1, d2 = x1 - x2, x2 - x3
    if d1 == 0.0 and d2 == 0.0:
        return 0.0, 'EXACT', None
    if d1 * d2 > 0 and abs(d1) > abs(d2) > 0:
        r = abs(d1) / abs(d2)
        xR = x3 - d2 / (r - 1.0)
        return abs(x1 - xR), 'ASYMPTOTIC', math.log2(r)
    return 2.0 * (abs(d1) + abs(d2)), 'NON-ASYMPTOTIC', None


def bound_for(make_vw, levels):
    """### `make_vw(nv) -> (v, w)`; returns the level values and the bound on the FIRST level."""
    Kb = kern('base', U_BASE)
    xs, parts = [], []
    for nv in levels:
        v, w = make_vw(nv)
        A, PR, m = margin_at(v, w, Kb)
        xs.append(m)
        parts.append(dict(nv=nv, A=A, PR=PR, m=m, points=len(v)))
    Ev, kind, order = richardson(*xs)
    v, w = make_vw(levels[0])
    A0 = parts[0]['A']
    Ah = arch(v, w, U_HALF, kern('half', U_HALF))
    Aw = arch(v, w, U_WIDE, kern('wide', U_WIDE))
    Eu = abs(Ah - A0) + abs(Aw - A0)
    return dict(levels=parts, E_v=Ev, kind=kind, order=order, A_half=Ah, A_wide=Aw, E_u=Eu,
                B=Ev + Eu, trunc=float(WI.trunc_bound(v, w)))


def seed_maker(a):
    g = SM.mean_zero_variant(a)

    def mk(nv):
        f = SQ.autocorrelation(g, nv)
        return f.v, f.w
    return mk


# ================================================================================================ quote
def quote():
    L = []
    src = io.open(os.path.join(T, 'b321_window.py'), encoding='utf-8').read().split(NL)
    at = io.open(os.path.join(T, 'e16', 'carto_atlas.py'), encoding='utf-8').read().split(NL)
    sq = io.open(os.path.join(T, 'b318_square.py'), encoding='utf-8').read().split(NL)

    def q(name, lines, pred):
        for i, l in enumerate(lines, 1):
            if pred(l):
                L.append('    %-22s :%-4d %s' % (name, i, l.rstrip()))
    L.append('=' * 104)
    L.append('COMPONENT 1 -- THE INSTRUMENT AS IT STANDS, QUOTED AT ITS LINES.')
    L.append('=' * 104)
    q('carto_atlas.py', at, lambda l: l.startswith('NV, NU, UMAX'))
    q('carto_atlas.py', at, lambda l: 'return np.cos(np.outer(u, v)) @ (w * dv)' in l)
    q('carto_atlas.py', at, lambda l: l.strip().startswith('_KERN = np.array('))
    q('b318_square.py', sq, lambda l: l.startswith('AUTOCORR_NV'))
    q('b321_window.py', src, lambda l: l.strip().startswith(('U = np.linspace(-AT.UMAX', 'A = float(np.trapezoid(hhat_blocked',
                                                             "val = 2.0 * math.log(p) / math.sqrt(n) * float(np.interp",
                                                             'tail = hhat_blocked(v, w, np.linspace(T, T + 200.0',
                                                             'return float(2.0 * np.max(np.abs(tail)) * 200.0)',
                                                             'Z = 2.0 * float(np.sum(hhat_blocked(v, w, AT.GAM)))')))
    L.append('')
    L.append('    ### ### **WHAT `trunc_bound` BOUNDS:** the zero side`s truncation at the last banked ordinate T --')
    L.append('    ### twice the largest |hhat| on [T, T + 200] times the width 200.')
    L.append('    ### ### **WHAT IT DOES NOT BOUND:** anything on the places side -- neither A`s u-quadrature nor')
    L.append('    ### the v-grid under hhat and the prime interpolation -- nor the zero tail beyond T + 200.')
    L.append('=' * 104)
    io.open(os.path.join(D, 'b501_components_c1.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L))


# ================================================================================================ cells
def cells(i, j):
    rows = json.loads(io.open(os.path.join(D, 'b492_cells.json'), encoding='utf-8').read())['rows']
    done = set()
    if os.path.exists(CELLS):
        for l in io.open(CELLS, encoding='utf-8'):
            if l.strip():
                done.add(json.loads(l)['i'])
    for r in rows[i:j]:
        if r['i'] in done:
            print('  %2d  a=%-10s  already banked' % (r['i'], r['a']))
            continue
        t0 = time.time()
        b = bound_for(seed_maker(r['a']), LEVELS)
        base = b['levels'][0]
        achieved = abs(r['zero'] + r['prime'] - r['arch'])
        row = dict(i=r['i'], a=r['a'], exact=r.get('exact'), m=base['m'], m_b492=r['m'],
                   A=base['A'], PR=base['PR'], A_b492=r['arch'], PR_b492=r['prime'],
                   repro=(base['A'] == r['arch'] and base['PR'] == r['prime']),
                   achieved=achieved, seconds=round(time.time() - t0, 1), **b)
        with io.open(CELLS, 'a', encoding='utf-8', newline=NL) as fh:
            fh.write(json.dumps(row, ensure_ascii=False) + NL)
        print('  %2d  a=%-10.6f  m=%.9f  E_v=%.2e %-15s E_u=%.2e  B=%.2e  |W+Z|=%.2e  B>=|W+Z| %-5s  repro %s  %.0fs'
              % (r['i'], r['a'], base['m'], b['E_v'], b['kind'], b['E_u'], b['B'], achieved,
                 b['B'] >= achieved, row['repro'], row['seconds']), flush=True)


# ================================================================================================ controls
def controls():
    import mpmath as mp
    out = {}
    L, s = 2.2, 2.2 / 8.0

    def gauss(N):
        v = np.linspace(-L, L, 2 * N - 1)
        return v, np.exp(-v ** 2 / (2 * s * s))
    t0 = time.time()
    b = bound_for(gauss, LEVELS)
    mp.mp.dps = 30
    ss = mp.mpf(s)
    hh = lambda u: ss * mp.sqrt(2 * mp.pi) * mp.exp(-ss ** 2 * u ** 2 / 2)
    kk = lambda u: mp.re(mp.digamma(mp.mpc(0.25, u / 2))) - mp.log(mp.pi)
    Aref = float(2 * mp.quad(lambda u: hh(u) * kk(u), [0, 5, 20, 60, mp.inf]) / (2 * mp.pi))
    PRref = 0.0
    for p in WI.primes_to(math.exp(L) + WI.PRIME_TOL):
        k = 1
        while p ** k <= math.exp(L) + WI.PRIME_TOL:
            n = p ** k
            if math.log(n) <= L:
                PRref += 2.0 * math.log(p) / math.sqrt(n) * math.exp(-math.log(n) ** 2 / (2 * s * s))
            k += 1
    mref = Aref - PRref
    err = abs(b['levels'][0]['m'] - mref)
    out['positive'] = dict(L=L, s=s, m_grid=b['levels'][0]['m'], A_grid=b['levels'][0]['A'],
                           PR_grid=b['levels'][0]['PR'], A_ref=Aref, PR_ref=PRref, m_ref=mref,
                           true_error=err, B=b['B'], E_v=b['E_v'], E_u=b['E_u'], kind=b['kind'],
                           passes=b['B'] >= err, seconds=round(time.time() - t0, 1))
    neg = []
    rows = {r['a']: r for r in (json.loads(l) for l in io.open(CELLS, encoding='utf-8') if l.strip())}
    for a in (1.3, 4.061553, 5.656854):
        t1 = time.time()
        bc = bound_for(seed_maker(a), COARSE)
        neg.append(dict(a=a, B_coarse=bc['B'], B_base=rows[a]['B'], kind=bc['kind'],
                        grows=bc['B'] > rows[a]['B'], seconds=round(time.time() - t1, 1)))
    out['negative'] = neg
    io.open(os.path.join(D, 'b501_controls.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(out, indent=1, ensure_ascii=False) + NL)
    print(json.dumps(out, indent=1))


# ================================================================================================ report
def report():
    rows = sorted((json.loads(l) for l in io.open(CELLS, encoding='utf-8') if l.strip()), key=lambda r: r['i'])
    C = json.loads(io.open(os.path.join(D, 'b501_controls.json'), encoding='utf-8').read())
    L = ['=' * 104, 'COMPONENTS 2 TO 4 -- THE BOUND, THE TEST, THE FLOOR.', '=' * 104,
         '    cells banked : %d' % len(rows),
         '    base reproduces b492 (A and PR bit for bit) : %d of %d' % (sum(r['repro'] for r in rows), len(rows)),
         '',
         '    %-3s %-10s %-13s %-9s %-15s %-9s %-9s %-9s %-6s %-9s %-6s %-5s'
         % ('i', 'a', 'm', 'E_v', 'kind', 'E_u', 'B', '|W+Z|', 'B>=', 'B+trunc', '>=', 'm>B')]
    for r in rows:
        L.append('    %-3d %-10.6f %-13.9f %-9.2e %-15s %-9.2e %-9.2e %-9.2e %-6s %-9.2e %-6s %-5s'
                 % (r['i'], r['a'], r['m'], r['E_v'], r['kind'], r['E_u'], r['B'], r['achieved'],
                    r['B'] >= r['achieved'], r['B'] + r['trunc'], r['B'] + r['trunc'] >= r['achieved'],
                    r['m'] > r['B']))
    aim = [r for r in rows if r['a'] <= 3.0 + 1e-9]
    lad = [r for r in rows if r['a'] > 3.0 + 1e-9]
    n_ok = sum(r['B'] >= r['achieved'] for r in rows)
    n_comp = sum(r['B'] + r['trunc'] >= r['achieved'] for r in rows)
    n_na = sum(r['kind'] == 'NON-ASYMPTOTIC' for r in rows)
    mn = min(rows, key=lambda r: r['m'])
    L += ['',
          '    ### ### **THE ORDER`S TEST, B >= |W+Z| : %d OF %d CELLS.**' % (n_ok, len(rows)),
          '    ### the composite B + trunc_bound >= |W+Z| : %d of %d' % (n_comp, len(rows)),
          '    ### NON-ASYMPTOTIC cells : %d' % n_na,
          '    ### max B over the AIM PLANE (%d cells) : %.3e   against b483`s 4.562e-05' % (len(aim), max(r['B'] for r in aim)),
          '    ### max B over the LADDER (%d cells)    : %.3e   against b483`s 3.169e-06' % (len(lad), max(r['B'] for r in lad)),
          '    ### B in range : %.2e .. %.2e ; E_u in range %.2e .. %.2e'
          % (min(r['B'] for r in rows), max(r['B'] for r in rows), min(r['E_u'] for r in rows), max(r['E_u'] for r in rows)),
          '',
          '    ### POSITIVE CONTROL (Gaussian, closed-form hhat, exact prime sum, A by mpmath.quad at 30 digits):',
          '      m_grid %.15f ; m_ref %.15f ; true error %.3e ; B %.3e (%s) ; ### **PASSES : %s**'
          % (C['positive']['m_grid'], C['positive']['m_ref'], C['positive']['true_error'], C['positive']['B'],
             C['positive']['kind'], C['positive']['passes']),
          '    ### NEGATIVE CONTROL (levels 2049, 4097, 8193):']
    for n in C['negative']:
        L.append('      a=%-10s B_coarse %.3e  B_base %.3e  ### **GROWS : %s**' % (n['a'], n['B_coarse'], n['B_base'], n['grows']))
    L += ['',
          '    ### ### **THE FLOOR (COMPONENT 4): each cell`s new floor is its B, beside b477`s 1.49e-08.**',
          '    ### ### **CELLS WHOSE MARGIN EXCEEDS ITS NEW FLOOR : %d OF %d.**' % (sum(r['m'] > r['B'] for r in rows), len(rows)),
          '    ### the minimum-margin cell a = %s : m %.9f ; new floor %.3e ; old floor 1.49e-08' % (mn['a'], mn['m'], mn['B']),
          '    ### total compute : %.0f s over the cells, %.0f s in the controls'
          % (sum(r['seconds'] for r in rows), C['positive']['seconds'] + sum(n['seconds'] for n in C['negative'])),
          '=' * 104]
    io.open(os.path.join(D, 'b501_components_c234.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(n=len(rows), repro=sum(r['repro'] for r in rows), test_ok=n_ok, composite_ok=n_comp,
                   nonasymptotic=n_na, aim_maxB=max(r['B'] for r in aim), ladder_maxB=max(r['B'] for r in lad),
                   aim_cells=len(aim), ladder_cells=len(lad), floors_exceeded=sum(r['m'] > r['B'] for r in rows),
                   min_cell=dict(a=mn['a'], m=mn['m'], B=mn['B']),
                   floors={str(r['a']): r['B'] for r in rows}, positive=C['positive'], negative=C['negative'],
                   seconds=sum(r['seconds'] for r in rows)),
              io.open(os.path.join(D, 'b501_results.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


if __name__ == '__main__':
    cmd = sys.argv[1]
    if cmd == 'quote':
        quote()
    elif cmd == 'cells':
        cells(int(sys.argv[2]), int(sys.argv[3]))
    elif cmd == 'controls':
        controls()
    else:
        report()
