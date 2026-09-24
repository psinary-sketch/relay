# -*- coding: utf-8 -*-
"""b502_ladder.py -- COMPONENTS 1 TO 4: THE LADDER PAST sqrt(32), THE TAIL, THE FITS, THE EPSTEIN CONTROL.

### `python tools/b502_ladder.py plan | epcheck | cells I J | report`
### ### **THE FITS ARE THE FACE`S, REGISTERED BEFORE THIS FILE RAN**: four one-parameter forms, least
### squares, root-mean-square absolute residual, on the old thirty-five and the new cells separately.
### ### **NOTHING OF THE CHAIN IS EDITED**; `b501_bound`, `b325_epstein`, `b321_window`, `b318_square`
### and `b317_smear` are imported and called. ### Each cell is appended to `b502_cells.jsonl` as it
### finishes, so the run is resumable in chunks.
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
import b501_bound as BB      # noqa: E402
import b317_smear as SM      # noqa: E402
import b318_square as SQ     # noqa: E402
import b321_window as WI     # noqa: E402
import b325_epstein as EP    # noqa: E402
import b437_components as GEN  # noqa: E402

NL = chr(10)
CELLS = os.path.join(D, 'b502_cells.jsonl')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def new_cells():
    """### ### **b437`S GENERATOR, ON EXACT a.** ### Boundaries sqrt(n) for prime powers n in (32, 200],
    ### and the midpoint of each consecutive pair starting from sqrt(32); EXACT a, rounded beside."""
    ns = [n for n in GEN.prime_powers_upto(200) if 32 < n <= 200]
    B = [math.sqrt(n) for n in ns]
    pts = [math.sqrt(32)] + B
    M = [(pts[i] + pts[i + 1]) / 2.0 for i in range(len(pts) - 1)]
    out = [dict(a=b, kind='boundary', n0=n) for b, n in zip(B, ns)] + [dict(a=m, kind='midpoint', n0=None) for m in M]
    out.sort(key=lambda c: c['a'])
    for i, c in enumerate(out):
        c['i'] = i
        c['rounded'] = round(c['a'], 6)
    return out


def plan():
    cs = new_cells()
    L = ['=' * 104, 'COMPONENT 1 -- THE PLAN: b437`S GENERATOR ON EXACT a, PRIME POWERS IN (32, 200].', '=' * 104,
         '    boundaries %d ; midpoints %d ; ### **NEW CELLS : %d** ; a from %.9f to %.9f'
         % (sum(c['kind'] == 'boundary' for c in cs), sum(c['kind'] == 'midpoint' for c in cs), len(cs),
            cs[0]['a'], cs[-1]['a'])]
    for c in cs:
        L.append('    %2d  %-9s n0=%-4s  exact %.15f  rounded %.6f' % (c['i'], c['kind'], c['n0'], c['a'], c['rounded']))
    io.open(os.path.join(D, 'b502_plan.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(cs, io.open(os.path.join(D, 'b502_plan.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L[:4]))


def epcheck():
    """### ### **THE EPSTEIN ROUTE`S POSITIVE CONTROL** -- a = 3.0 recomputed against b477`s bank."""
    rows = [json.loads(l) for l in io.open(os.path.join(D, 'b477_entries.jsonl'), encoding='utf-8') if l.strip()]
    ref = next(r for r in rows if r.get('kind') == 'control_diagonal' and r['a'] == 3.0)
    g = SM.mean_zero_variant(3.0)
    f = SQ.autocorrelation(g)
    q = EP.channels_q(f.v, f.w)
    d = max(abs(q['arch'] - ref['arch']), abs(q['finite'] - ref['finite']))
    out = dict(a=3.0, arch=q['arch'], finite=q['finite'], arch_b477=ref['arch'], finite_b477=ref['finite'],
               max_diff=d, reproduces=d <= 1e-12)
    json.dump(out, io.open(os.path.join(D, 'b502_epcheck.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(json.dumps(out, indent=1))


def cells(i, j):
    cs = json.loads(io.open(os.path.join(D, 'b502_plan.json'), encoding='utf-8').read())
    done = set()
    if os.path.exists(CELLS):
        done = {json.loads(l)['i'] for l in io.open(CELLS, encoding='utf-8') if l.strip()}
    for c in cs[i:j]:
        if c['i'] in done:
            continue
        t0 = time.time()
        a = c['a']
        g = SM.mean_zero_variant(a)
        f = SQ.autocorrelation(g)
        ch = WI.channels(f.v, f.w)
        Lv = float(f.v[-1])
        terms = {}
        for p in WI.primes_to(math.exp(Lv) + WI.PRIME_TOL):
            k = 1
            while p ** k <= math.exp(Lv) + WI.PRIME_TOL:
                n = p ** k
                ln = math.log(n)
                if ln <= Lv:
                    terms[n] = 2.0 * math.log(p) / math.sqrt(n) * float(np.interp(ln, f.v, f.w))
                k += 1
        t1 = time.time()
        b = BB.bound_for(BB.seed_maker(a), BB.LEVELS)
        t2 = time.time()
        q = EP.channels_q(f.v, f.w)
        t3 = time.time()
        W = ch['prime'] - ch['arch']
        row = dict(c, W=W, m=-W, arch=ch['arch'], prime=ch['prime'], zero=ch['zero'], pole=ch['pole'],
                   residual=ch['residual'], L=Lv, terms={str(n): x for n, x in sorted(terms.items())},
                   terms_sum=sum(terms.values()), B=b['B'], E_v=b['E_v'], E_u=b['E_u'], kind_R=b['kind'],
                   bound_base_agrees=(b['levels'][0]['A'] == ch['arch'] and b['levels'][0]['PR'] == ch['prime']),
                   trunc=b['trunc'], achieved=abs(ch['zero'] + W),
                   ep_arch=q['arch'], ep_finite=q['finite'], ep_pole=q['pole'], m_Q=q['arch'] - q['finite'],
                   s_chain=round(t1 - t0, 1), s_bound=round(t2 - t1, 1), s_epstein=round(t3 - t2, 1))
        with io.open(CELLS, 'a', encoding='utf-8', newline=NL) as fh:
            fh.write(json.dumps(row, ensure_ascii=False) + NL)
        print('  %2d  a=%-10.6f %-9s m=%+.9f  B=%.2e  m>B %-5s  m_Q=%+.6f  terms %-3d  %.0f+%.0f+%.0fs'
              % (c['i'], a, c['kind'], row['m'], row['B'], row['m'] > row['B'], row['m_Q'], len(terms),
                 row['s_chain'], row['s_bound'], row['s_epstein']), flush=True)


def fit(xs, ys, g):
    """### ### **ONE-PARAMETER LEAST SQUARES, `y = c g(x)`; LOSS = RMS ABSOLUTE RESIDUAL.**"""
    G = np.array([g(x) for x in xs])
    Y = np.array(ys)
    c = float(np.dot(G, Y) / np.dot(G, G))
    r = Y - c * G
    return c, float(math.sqrt(np.mean(r * r)))


FORMS = [('(a) c', lambda a: 1.0), ('(b) c/a', lambda a: 1.0 / a),
         ('(c) c/log a', lambda a: 1.0 / math.log(a)), ('(d) c/a^2', lambda a: 1.0 / (a * a))]


def report():
    new = sorted((json.loads(l) for l in io.open(CELLS, encoding='utf-8') if l.strip()), key=lambda r: r['a'])
    old = sorted((json.loads(l) for l in io.open(os.path.join(D, 'b501_cells.jsonl'), encoding='utf-8') if l.strip()),
                 key=lambda r: r['a'])
    ep_old = {r['a']: r for r in (json.loads(l) for l in io.open(os.path.join(D, 'b477_entries.jsonl'), encoding='utf-8')
                                  if l.strip()) if r.get('kind') == 'control_diagonal'}
    epc = json.loads(io.open(os.path.join(D, 'b502_epcheck.json'), encoding='utf-8').read())
    allc = [dict(a=r['a'], m=r['m'], B=r['B'], src='old', m_Q=ep_old[r['a']]['arch'] - ep_old[r['a']]['finite'])
            for r in old] + [dict(a=r['a'], m=r['m'], B=r['B'], src='new', m_Q=r['m_Q']) for r in new]
    allc.sort(key=lambda r: r['a'])
    L = ['=' * 104, 'COMPONENTS 1 TO 4 -- THE LADDER, THE TAIL, THE FITS, THE EPSTEIN CONTROL.', '=' * 104,
         '    ### **NEW CELLS : %d** ; compute %.0f s (chain %.0f, bound %.0f, Epstein %.0f)'
         % (len(new), sum(r['s_chain'] + r['s_bound'] + r['s_epstein'] for r in new), sum(r['s_chain'] for r in new),
            sum(r['s_bound'] for r in new), sum(r['s_epstein'] for r in new)),
         '    bound base agrees with the chain at every new cell : %s' % all(r['bound_base_agrees'] for r in new),
         '    worst |sum(terms) - PR| : %.3e' % max(abs(r['terms_sum'] - r['prime']) for r in new),
         '', '### COMPONENT 2 -- THE TAIL, ALL %d CELLS IN ORDER OF a.' % len(allc), '-' * 104,
         '    %-4s %-12s %-5s %-14s %-10s %-6s %-8s %-12s' % ('#', 'a', 'set', 'm', 'floor B', 'm>B', 'm/B', 'm_Q')]
    for k, r in enumerate(allc):
        L.append('    %-4d %-12.6f %-5s %+.9f  %-10.2e %-6s %-8.1e %+.6f' % (k, r['a'], r['src'], r['m'], r['B'],
                                                                         r['m'] > r['B'], r['m'] / r['B'], r['m_Q']))
    ext = []
    for k in range(1, len(allc) - 1):
        p, c, n = allc[k - 1]['m'], allc[k]['m'], allc[k + 1]['m']
        if c > p and c > n:
            ext.append(('MAX', allc[k]))
        if c < p and c < n:
            ext.append(('MIN', allc[k]))
    L += ['', '    ### ### **EVERY LOCAL EXTREMUM (interior cells, neighbours on both sides):**']
    for t, r in ext:
        L.append('      %s  a=%.6f  m=%+.9f  (%s)' % (t, r['a'], r['m'], r['src']))
    L.append('      the last cell, a=%.6f, m=%+.9f -- an endpoint, not classified.' % (allc[-1]['a'], allc[-1]['m']))
    neg = [r for r in allc if r['m'] <= r['B']]
    ten = [r for r in allc if r['m'] < 10 * r['B']]
    L += ['    ### ### **CELLS WHERE m IS NOT ABOVE ITS FLOOR : %d** %s' % (len(neg), [round(r['a'], 6) for r in neg]),
          '    ### ### **CELLS WHERE m IS WITHIN TEN FLOORS OF ZERO : %d** %s' % (len(ten), [round(r['a'], 6) for r in ten]),
          '    smallest m/B over all cells : %.3e at a = %.6f' % min((r['m'] / r['B'], r['a']) for r in allc),
          '', '### COMPONENT 3 -- THE FITS, AS REGISTERED. ### LOSS: RMS ABSOLUTE RESIDUAL.', '-' * 104]
    fits = {}
    for name, g in FORMS:
        co, ro = fit([r['a'] for r in old], [r['m'] for r in old], g)
        cn, rn = fit([r['a'] for r in new], [r['m'] for r in new], g)
        fits[name] = dict(c_old=co, rms_old=ro, c_new=cn, rms_new=rn)
        L.append('    %-12s  OLD c=%+.6e rms=%.6e    NEW c=%+.6e rms=%.6e' % (name, co, ro, cn, rn))
    win_new = min(fits, key=lambda k: fits[k]['rms_new'])
    win_old = min(fits, key=lambda k: fits[k]['rms_old'])
    L += ['    ### ### **LEAST RESIDUAL ON THE NEW CELLS ALONE : %s** ; ON THE OLD : %s ; ### **SAME : %s**'
          % (win_new, win_old, win_new == win_old),
          '    ### A FIT IS A DESCRIPTION OF THE CHART AND NOT A BOUND.',
          '', '### COMPONENT 4 -- THE EPSTEIN CONTROL.', '-' * 104,
          '    the route`s positive control, a = 3.0 against b477 : max diff %.2e ; ### **REPRODUCES : %s**'
          % (epc['max_diff'], epc['reproduces'])]
    epneg = [r for r in allc if r['m_Q'] < 0]
    L += ['    ### ### **CELLS WHERE THE EPSTEIN MARGIN IS NEGATIVE : %s**'
          % ('NONE' if not epneg else [(round(r['a'], 6), r['m_Q']) for r in epneg]),
          '    smallest Epstein margin : %+.6f at a = %.6f' % min((r['m_Q'], r['a']) for r in allc),
          '    ### the ladder`s last width is %.6f; b334`s crossings sit at widths 40 and 81.' % allc[-1]['a'],
          '=' * 104]
    io.open(os.path.join(D, 'b502_components.txt'), 'w', encoding='utf-8', newline=NL).write(
        io.open(os.path.join(D, 'b502_plan.txt'), encoding='utf-8').read() + NL.join(L) + NL)
    json.dump(dict(n_new=len(new), n_all=len(allc), seconds=sum(r['s_chain'] + r['s_bound'] + r['s_epstein'] for r in new),
                   new_not_above=[r['a'] for r in new if r['m'] <= r['B']], not_above=len(neg), within_ten=len(ten),
                   extrema=[dict(t=t, a=r['a'], m=r['m'], src=r['src']) for t, r in ext],
                   fits=fits, win_new=win_new, win_old=win_old, epneg=[r['a'] for r in epneg],
                   ep_min=min(r['m_Q'] for r in allc), epcheck=epc,
                   base_agrees=all(r['bound_base_agrees'] for r in new)),
              io.open(os.path.join(D, 'b502_results.json'), 'w', encoding='utf-8', newline=NL), indent=1)
    print(NL.join(L))


if __name__ == '__main__':
    cmd = sys.argv[1]
    {'plan': plan, 'epcheck': epcheck, 'report': report}.get(cmd, lambda: cells(int(sys.argv[2]), int(sys.argv[3])))()
