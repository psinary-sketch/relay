# -*- coding: utf-8 -*-
"""b508_margin.py -- THE EPSTEIN MARGIN READ ON A BANK THAT CLOSES, BESIDE XI'S. ### `python tools/b508_margin.py pairs | report`

### `pairs`  -- at each of b506's wide cells, the Epstein zero side's OFF-LINE part split by pair: for each of the off-line
###             zeros b506 located with sigma > 0.52 (each with its three images: conjugate, 1 - rho, 1 - conj rho), its
###             term by `b326_closure.ftilde` at b506's own grid (the same `v, w` b506 used: `mean_zero_variant(a)`,
###             `autocorrelation(g, nv)`, nv from b506's cell). ### THE FIXTURE: the pair terms summed agree with b506's
###             banked `Z_off` to within 1e-12 at every cell, against a floor near 1e-17 (the same function at the same
###             grid, summed in another order); a cell that fails is printed and the report REFUSES. ### Nothing of the
###             places side is recomputed: A, PR, the pole, the residual and the bound are b506's and b504's banks.
### `report` -- Components 1-3 of the order, from `b504_cells.jsonl`, `b506_cells.jsonl` and `b508_pairs.jsonl`.
"""
import io
import json
import math
import multiprocessing as mpr
import os
import sys
import time

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
sys.path.insert(0, os.path.join(T, 'e16'))
NL = chr(10)
PAIRS = os.path.join(D, 'b508_pairs.jsonl')
FIX_BAR = 1e-12
PAIR16 = (0.9532604747946607, 16.290215720390393)     # ### b326's banked off-line zero, recovered by b506's control
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rows(name):
    return sorted((json.loads(l) for l in io.open(os.path.join(D, name), encoding='utf-8') if l.strip()), key=lambda c: c['a'])


def off_zeros():
    r = json.loads(io.open(os.path.join(D, 'b506_c2_results.json'), encoding='utf-8').read())
    return [tuple(z['rho']) for z in r['found'] if z.get('rho') and z['col'] == 'R']


_OFF = None


def _init():
    global _OFF
    _OFF = off_zeros()


def _one(c):
    import b317_smear as SM
    import b318_square as SQ
    import b326_closure as BC
    t0 = time.time()
    g = SM.mean_zero_variant(c['a'])
    f = SQ.autocorrelation(g, c['nv'])
    v, w = np.asarray(f.v), np.asarray(f.w)
    terms = []
    for b, gg in _OFF:
        t = 0.0
        for rho in (complex(b, gg), complex(b, -gg), complex(1 - b, gg), complex(1 - b, -gg)):
            t += BC.ftilde(v, w, rho)[0].real
        terms.append(dict(rho=[b, gg], term=t))
    s = float(sum(x['term'] for x in terms))
    return dict(a=c['a'], nv=c['nv'], terms=terms, sum_off=s, banked_off=c['Z_off'], diff=s - c['Z_off'],
                fixture=abs(s - c['Z_off']) < FIX_BAR, seconds=round(time.time() - t0, 1))


def pairs():
    cells = rows('b506_cells.jsonl')
    off = off_zeros()
    done = set()
    if os.path.exists(PAIRS):
        done = {round(json.loads(l)['a'], 9) for l in io.open(PAIRS, encoding='utf-8') if l.strip()}
    todo = [c for c in cells if round(c['a'], 9) not in done]
    print('[%s] cells %d ; to run %d ; off-line zeros (sigma > 0.52) %d' % (time.strftime('%H:%M:%S'), len(cells), len(todo), len(off)), flush=True)
    t0 = time.time()
    with mpr.Pool(5, initializer=_init) as pool:
        for i, r in enumerate(pool.imap_unordered(_one, todo), 1):
            with io.open(PAIRS, 'a', encoding='utf-8', newline=NL) as fh:
                fh.write(json.dumps(r) + NL)
            print('[%s] %3d a=%-10.6f sum_off %+.12e banked %+.12e diff %.1e %s %.0fs'
                  % (time.strftime('%H:%M:%S'), i, r['a'], r['sum_off'], r['banked_off'], abs(r['diff']),
                     'OK' if r['fixture'] else '### FIXTURE FAILS', r['seconds']), flush=True)
    print('[%s] done in %.0f s' % (time.strftime('%H:%M:%S'), time.time() - t0), flush=True)
    return 0


def spearman(x, y):
    rx = np.argsort(np.argsort(x)).astype(float)
    ry = np.argsort(np.argsort(y)).astype(float)
    return float(np.corrcoef(rx, ry)[0, 1])


def fit_pow(a, y):
    """### least squares of log|y| on log a -- a CENTRE LINE, NOT A BOUND."""
    p, c = np.polyfit(np.log(a), np.log(np.abs(y)), 1)
    return float(p), float(c)


def report():
    xi = rows('b504_cells.jsonl')
    q0 = rows('b506_cells.jsonl')
    pr = {round(r['a'], 9): r for r in rows('b508_pairs.jsonl')}
    fix_fail = [r['a'] for r in pr.values() if not r['fixture']]
    if len(pr) != len(q0) or fix_fail:
        print('### REFUSED -- THE PAIR SPLIT DOES NOT REPRODUCE b506`S Z_off AT %s (or cells missing: %d of %d).'
              % (fix_fail, len(pr), len(q0)))
        return 2
    xmap = {round(c['a'], 6): c for c in xi}
    both = []
    for c in q0:
        x = xmap.get(round(c['a'], 6))
        if x is not None and x['verified'] and c['verified']:
            both.append((c, x, pr[round(c['a'], 9)]))
    A = np.array([c['a'] for c, _x, _p in both])
    mq = np.array([c['md'] for c, _x, _p in both])
    zq = np.array([c['Z_on'] + c['Z_off'] for c, _x, _p in both])
    P = np.array([c['P'] for c, _x, _p in both])
    rq = np.array([c['r'] for c, _x, _p in both])
    Bq = np.array([c['B'] for c, _x, _p in both])
    zon = np.array([c['Z_on'] for c, _x, _p in both])
    zoff = np.array([c['Z_off'] for c, _x, _p in both])
    diff = mq - (zq - P)
    i16 = [k for k, (b, g) in enumerate(off_zeros()) if abs(b - PAIR16[0]) < 1e-8 and abs(g - PAIR16[1]) < 1e-8]
    t16 = np.array([p['terms'][i16[0]]['term'] for _c, _x, p in both]) if i16 else np.array([])
    frac16 = t16 / zoff if len(t16) else np.array([])
    res = dict(cells_119=len(xi), xi_verified=sum(1 for c in xi if c['verified']), q0_cells=len(q0),
               q0_verified=sum(1 for c in q0 if c['verified']), both=len(both),
               min_mq=float(mq.min()), min_mq_a=float(A[mq.argmin()]), neg_mq=int((mq < 0).sum()),
               max_diff_plus_r=float(np.max(np.abs(diff + rq))), max_abs_diff=float(np.max(np.abs(diff))),
               max_abs_P=float(np.max(np.abs(P))), diff_within_r=bool(np.all(np.abs(diff) <= np.abs(rq) * (1 + 1e-9) + 1e-15)),
               diff_within_B=bool(np.all(np.abs(diff) <= Bq)),
               zoff_neg=int((zoff < 0).sum()), zoff_pos=int((zoff > 0).sum()),
               spearman_a_abs_zoff=spearman(A, np.abs(zoff)), zoff_first=float(zoff[0]), zoff_last=float(zoff[-1]),
               zoff_rising_steps=int(np.sum(np.diff(np.abs(zoff)) > 0)), steps=len(zoff) - 1,
               pair16_found=bool(i16), t16_sign_pos=int((t16 > 0).sum()), t16_sign_neg=int((t16 < 0).sum()),
               frac16_min=float(frac16.min()) if len(frac16) else None, frac16_max=float(frac16.max()) if len(frac16) else None,
               a_min=float(A.min()), a_max=float(A.max()))
    p16, c16 = fit_pow(A, t16)
    pon, con = fit_pow(A, zon)
    res.update(fit_t16=dict(p=p16, c=c16), fit_zon=dict(p=pon, c=con))
    # ### the extrapolated crossing |T16| = |Z_on| under both centre lines: log a* = (con - c16) / (p16 - pon)
    # ### ### **ONLY FORWARD:** "if the present growth continued" names widths beyond the ladder, so a crossing exists
    # ### only when the ratio |T16|/|Z_on| GROWS with a under the centre lines; if it falls, the width is NONE.
    res['ratio_grows'] = bool(p16 > pon)
    if p16 > pon:
        la = (con - c16) / (p16 - pon)
        res['extrap_a'] = float(math.exp(la)) if la < 700 else float('inf')
        res['extrap_beyond_ladder'] = bool(res['extrap_a'] > float(A.max()))
    gamma, delta = PAIR16[1], PAIR16[0] - 0.5
    res['law'] = dict(gamma=gamma, delta=delta, n_law=5.9 * gamma ** 2 / delta, n_sitting=3379, coordinate='Li index n, not a width a')
    res['ratio_first'] = float(abs(t16[0]) / abs(zon[0]))
    res['ratio_last'] = float(abs(t16[-1]) / abs(zon[-1]))
    res['fixture_max_diff'] = float(max(abs(r['diff']) for r in pr.values()))
    res['pairs_off'] = len(off_zeros())
    # ### (N)/(S) scores, each on the population named on the face
    res['n1'] = res['neg_mq'] == 0 and len(both) > 0
    res['n2'] = res['diff_within_r']
    res['n3'] = bool((res['zoff_neg'] > len(both) / 2) and (abs(zoff[-1]) > abs(zoff[0]) and res['spearman_a_abs_zoff'] > 0))
    res['n3_clause1'] = res['zoff_neg'] > len(both) / 2
    res['n3_clause2'] = bool(abs(zoff[-1]) > abs(zoff[0]) and res['spearman_a_abs_zoff'] > 0)
    res['s1'] = res['zoff_pos'] == len(both)
    res['s2'] = bool(len(frac16) and frac16.min() > 0.5)
    res['s3'] = not res['ratio_grows']
    L = ['=' * 104, 'b508 -- THE EPSTEIN MARGIN ON THE COMPLETED BANK, BESIDE XI`S. ### COMPONENTS 1-3.', '=' * 104,
         '### THE FIXTURE: the %d off-line pair terms summed against b506`s banked Z_off, %d cells: largest difference %.1e (bar 1e-12, floor near 1e-17).'
         % (res['pairs_off'], len(pr), res['fixture_max_diff']),
         '', '### COMPONENT 1 -- WHERE BOTH KERNELS VERIFY.',
         '    cells in the ladder : %(cells_119)d ; xi verified (b504) : %(xi_verified)d ; Q0 cells run on the completed bank (b506) : %(q0_cells)d, verified %(q0_verified)d' % res,
         '    ### ### **CELLS WHERE BOTH VERIFY : %d** (a from %.6f to %.6f)' % (len(both), res['a_min'], res['a_max']),
         '    %-10s %-14s %-10s %-10s %-14s %-10s %-10s' % ('a', 'm_Q0', '|r_Q0|', 'B_Q0', 'm_xi', '|r_xi|', 'B_xi')]
    for (c, x, _p) in both:
        L.append('    %-10.6f %+.9f %-10.2e %-10.2e %+.9f %-10.2e %-10.2e' % (c['a'], c['md'], abs(c['r']), c['B'], x['m'], abs(x['r']), x['B_z']))
    L += ['    ### SMALLEST EPSTEIN MARGIN : %+.9f at a = %.6f' % (res['min_mq'], res['min_mq_a']),
          '    ### CELLS WHERE IT IS NEGATIVE : %s' % (res['neg_mq'] if res['neg_mq'] else 'NONE'),
          '', '### COMPONENT 2 -- THE ZERO CHANNEL BESIDE THE MARGIN, AND ITS OFF-LINE PART.',
          '    %-10s %-14s %-14s %-11s %-11s %-11s %-14s %-14s' % ('a', 'Z_Q0', 'm_Q0', 'P', 'm-(Z-P)', '|r|', 'Z_on', 'Z_off')]
    for (c, _x, _p), d in zip(both, diff):
        L.append('    %-10.6f %+.9f %+.9f %+.2e %+.2e %.2e %+.9f %+.9e' % (c['a'], c['Z_on'] + c['Z_off'], c['md'], c['P'], d, abs(c['r']), c['Z_on'], c['Z_off']))
    L += ['    ### m_Q0 - (Z_Q0 - P) equals -r at every cell to %.1e: ### **BY CONSTRUCTION**, since b506 defines r = Z - (P - PR + A).' % res['max_diff_plus_r'],
          '    ### largest |m - (Z - P)| %.2e ; largest |P| %.2e ; within |r| at every cell : %s ; within B at every cell : %s'
          % (res['max_abs_diff'], res['max_abs_P'], res['diff_within_r'], res['diff_within_B']),
          '    ### THE OFF-LINE PART : positive at %d, negative at %d of %d cells ; |Z_off| from %.3e (a = %.6f) to %.3e (a = %.6f) ; rising steps %d of %d ; Spearman(a, |Z_off|) %+.4f'
          % (res['zoff_pos'], res['zoff_neg'], len(both), abs(res['zoff_first']), res['a_min'], abs(res['zoff_last']), res['a_max'],
             res['zoff_rising_steps'], res['steps'], res['spearman_a_abs_zoff']),
          '', '### COMPONENT 3 -- THE PAIR AT 0.953 + 16.29i AGAINST THE ON-LINE PART. ### **AN EXTRAPOLATION, AND LABELLED AS ONE.**',
          '    its term (the zero with its three images) : positive at %d, negative at %d ; share of Z_off from %.3f to %.3f'
          % (res['t16_sign_pos'], res['t16_sign_neg'], res['frac16_min'], res['frac16_max']),
          '    |T16| / |Z_on| : %.4e at a = %.6f ; %.4e at a = %.6f' % (res['ratio_first'], res['a_min'], res['ratio_last'], res['a_max']),
          '    centre lines, log|y| on log a over the %d cells : |T16| ~ a^(%.4f) ; |Z_on| ~ a^(%.4f)' % (len(both), p16, pon),
          '    ### ### **THE EXTRAPOLATED WIDTH WHERE |T16| WOULD EQUAL |Z_on| IF THESE CENTRE LINES CONTINUED : %s**'
          % (('%.6g' % res['extrap_a']) if 'extrap_a' in res else 'NONE -- under the centre lines the ratio falls with a'),
          '    ### ratio grows with a under the fits : %s ; the extrapolated width lies beyond the ladder : %s'
          % (res.get('ratio_grows'), res.get('extrap_beyond_ladder')),
          '    ### ### **A FIT IS NOT A BOUND AND AN EXTRAPOLATION IS NOT A CROSSING. NO CROSSING WIDTH IS ASSERTED.**',
          '    ### the detection law F.2026-08-05-p for this pair : 5.9 gamma^2 / delta = %.1f (gamma %.6f, delta %.7f); the sitting measured 3379.'
          % (res['law']['n_law'], gamma, delta),
          '    ### THAT IS A LI INDEX n, NOT A SUPPORT WIDTH a. ### This act does not map one to the other; the two are printed side by side and not compared.',
          '=' * 104]
    io.open(os.path.join(D, 'b508_report.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    d = (json.dumps(res, indent=1, default=lambda o: o.item()) + NL).encode('utf-8')   # ### numpy scalars (b328's husk)
    open(os.path.join(D, 'b508_results.json.tmp'), 'wb').write(d)
    os.replace(os.path.join(D, 'b508_results.json.tmp'), os.path.join(D, 'b508_results.json'))
    print(NL.join(L[-24:]))
    return 0


if __name__ == '__main__':
    sys.exit({'pairs': pairs, 'report': report}[sys.argv[1]]())
