# -*- coding: utf-8 -*-
"""b511_report.py -- COMPONENTS 1-3 READ OFF `b511_cells.jsonl`, ON VERIFIED CELLS ALONE. ### `python tools/b511_report.py`"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
OLD = (('MIN', 4.061553), ('MAX', 5.196152), ('MIN', 13.152946))
FAMS = ('bspline', 'notch1', 'notch3', 'notch5')


def load():
    rows = [json.loads(l) for l in io.open(os.path.join(D, 'b511_cells.jsonl'), encoding='utf-8') if l.strip()]
    by = {}
    for r in rows:
        by.setdefault(r['family'], []).append(r)
    for f in by:
        by[f].sort(key=lambda r: r['a'])
    return by


def extrema(cells):
    """### local extrema of m over the VERIFIED cells, sorted by a."""
    v = [c for c in cells if c['xi']['verified']]
    out = []
    for i in range(1, len(v) - 1):
        m0, m1, m2 = v[i - 1]['xi']['m'], v[i]['xi']['m'], v[i + 1]['xi']['m']
        if m1 < m0 and m1 < m2:
            out.append(('MIN', v[i]['a']))
        elif m1 > m0 and m1 > m2:
            out.append(('MAX', v[i]['a']))
    return out


def main():
    by = load()
    A = [c['a'] for c in by['bspline']]
    idx = {round(a, 6): i for i, a in enumerate(A)}
    res = dict(cells={f: len(by.get(f, [])) for f in FAMS})
    L = ['=' * 104, 'b511 -- COMPONENTS 1-3, READ ON VERIFIED CELLS ALONE.', '=' * 104]
    for f in FAMS:
        cs = by.get(f, [])
        vx = [c for c in cs if c['xi']['verified']]
        vq = [c for c in cs if c['q']['verified']]
        ux = [(c['a'], abs(c['xi']['r']) / c['xi']['B']) for c in cs if not c['xi']['verified']]
        uq = [(c['a'], abs(c['q']['r']) / c['q']['B']) for c in cs if not c['q']['verified']]
        negq = [c['a'] for c in vq if c['q']['m'] < 0]
        negx = [c['a'] for c in vx if c['xi']['m'] <= 0]
        ctl_x = max((abs(c['xi']['notched']) for c in cs), default=0.0)
        ctl_q = max((abs(c['q']['notched']) for c in cs), default=0.0)
        cross = [c['a'] for c in vq if abs(c['q']['Z_off']) > abs(c['q']['on_rest'])]
        res[f] = dict(n=len(cs), xi_verified=len(vx), q_verified=len(vq), xi_unverified=ux, q_unverified=uq,
                      q_neg=negq, xi_nonpos=negx, xi_min=min((c['xi']['m'] for c in vx), default=None),
                      xi_min_a=min(vx, key=lambda c: c['xi']['m'])['a'] if vx else None,
                      q_min=min((c['q']['m'] for c in vq), default=None),
                      q_min_a=min(vq, key=lambda c: c['q']['m'])['a'] if vq else None,
                      notched_ctl_xi=ctl_x, notched_ctl_q=ctl_q, crossings=cross,
                      ratio=[(c['a'], c['q']['Z_off'] / c['q']['on_rest'] if c['q']['on_rest'] else None) for c in vq])
        L += ['', '### FAMILY %s (order %s)' % (f.upper(), cs[0]['xi']['order'] if cs else '?'),
              '    cells %d ; xi VERIFIED %d ; Q0 VERIFIED %d' % (len(cs), len(vx), len(vq)),
              '    xi unverified (a, |r|/B) : %s' % ', '.join('%.6f:%.3g' % u for u in ux),
              '    Q0 unverified (a, |r|/B) : %s' % ', '.join('%.6f:%.3g' % u for u in uq),
              '    xi margin over VERIFIED cells : smallest %s at a = %s ; cells with m <= 0 : %s' % (res[f]['xi_min'], res[f]['xi_min_a'], negx or 'NONE'),
              '    ### Q0 (EPSTEIN) MARGIN over VERIFIED cells : smallest %s at a = %s ; CELLS WHERE IT IS NEGATIVE : %s'
              % (res[f]['q_min'], res[f]['q_min_a'], negq or 'NONE')]
        # ### ### **READINGS BESIDE THE SEALED VERDICT (b511, after the first read) -- THEY RE-SCORE NOTHING.** ###
        # ### (i) the bound's dominant term; (ii) VACUOUS where B >= |m| (a pass that cannot say the identity closes to the
        # ### margin's size); (iii) the margin's sign decided on its OWN error E_u + E_k, which involves no zero at all.
        for obj in ('xi', 'q'):
            dom = {}
            for c in cs:
                t = max(('Eu', 'Ek', 'Etail', 'Eround'), key=lambda k: c[obj][k])
                dom[t] = dom.get(t, 0) + 1
            vac = [c['a'] for c in cs if c[obj]['verified'] and c[obj]['B'] >= abs(c[obj]['m'])]
            dec = [c for c in cs if abs(c[obj]['m']) > c[obj]['Eu'] + c[obj]['Ek']]
            neg_dec = [c['a'] for c in dec if c[obj]['m'] < 0]
            ratio = [abs(c[obj]['r']) / c[obj]['B'] for c in cs if not c[obj]['verified']]
            res[f][obj + '_reading'] = dict(dominant=dom, vacuous=len(vac), sign_decided=len(dec), neg_decided=neg_dec,
                                            unverified_ratio_max=max(ratio) if ratio else None)
            L.append('    [reading] %-3s bound dominated by %s ; VERIFIED-BUT-VACUOUS (B >= |m|) %d ; sign of m decided on its own error %d of %d, negative at %s ; unverified |r|/B at most %s'
                     % (obj, dom, len(vac), len(dec), len(cs), neg_dec or 'NONE', ('%.3f' % max(ratio)) if ratio else '-'))
        if f != 'bspline':
            L += ['    CONTROL -- the notched zeros` part, largest |.| over all cells : xi %.2e ; Q0 %.2e' % (ctl_x, ctl_q),
                  '    COMPONENT 3 -- Q0`s off-line part over its remaining on-line part, a : ratio (every tenth verified cell):',
                  '      ' + ' ; '.join('%.3f: %+.3e' % (a, r) for a, r in res[f]['ratio'][::10] if r is not None),
                  '    ### widths where |Z_off| exceeds |Z_on,rest| : %s' % (cross or 'NONE')]
            L += ['    %-10s %-16s %-16s %-16s %-14s %-14s' % ('a', 'Q0 m', 'Q0 Z_off', 'Q0 Z_on,rest', 'xi m', 'xi Z_on,rest')]
            for c in cs[::6]:
                L.append('    %-10.6f %+.9e %+.9e %+.9e %+.7e %+.7e %s' % (c['a'], c['q']['m'], c['q']['Z_off'], c['q']['on_rest'],
                                                                         c['xi']['m'], c['xi']['on_rest'],
                                                                         '' if c['q']['verified'] and c['xi']['verified'] else '(unverified)'))
        else:
            ex = extrema(cs)
            surv = []
            for kind, a0 in OLD:
                i0 = idx.get(round(a0, 6))
                hit = [a for k, a in ex if k == kind and i0 is not None and abs(idx[round(a, 6)] - i0) <= 1]
                surv.append(dict(kind=kind, a=a0, survives=bool(hit), at=hit))
            res[f]['extrema'] = ex
            res[f]['survival'] = surv
            L += ['    xi`s extrema over the verified cells : %s' % ', '.join('%s %.6f' % e for e in ex),
                  '    the old three within one cell : %s' % ', '.join('%s %.6f -> %s' % (s['kind'], s['a'], 'SURVIVES %s' % s['at'] if s['survives'] else 'DOES NOT')
                                                                    for s in surv)]
            L += ['    %-10s %-16s %-12s %-12s %-16s %-12s %-12s' % ('a', 'xi m', 'xi |r|', 'xi B', 'Q0 m', 'Q0 |r|', 'Q0 B')]
            for c in cs:
                L.append('    %-10.6f %+.9e %-12.3e %-12.3e %+.9e %-12.3e %-12.3e' % (c['a'], c['xi']['m'], abs(c['xi']['r']), c['xi']['B'],
                                                                                  c['q']['m'], abs(c['q']['r']), c['q']['B']))
    bs = res['bspline']
    res['n1'] = bs['xi_verified'] >= 105 and bs['q_verified'] >= 85
    res['n2'] = all(s['survives'] for s in bs['survival'])
    res['n3'] = len(res['notch5']['q_neg']) >= 1
    res['n4'] = all(not res[f]['xi_nonpos'] for f in FAMS)
    res['s1'] = bs['xi_verified'] == 119
    res['s2'] = all(not res[f]['q_neg'] for f in ('notch1', 'notch3', 'notch5'))
    res['s3'] = not res['n2']
    L += ['', '### THE EXPECTATIONS ON THESE CELLS : ' + ' ; '.join('(%s) %s' % (k.upper(), 'HELD' if res[k] else 'REFUTED')
                                                                  for k in ('n1', 'n2', 'n3', 'n4', 's1', 's2', 's3')), '=' * 104]
    io.open(os.path.join(D, 'b511_report.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    d = (json.dumps(res, indent=1, default=lambda o: o.item()) + NL).encode('utf-8')
    open(os.path.join(D, 'b511_results.json.tmp'), 'wb').write(d)
    os.replace(os.path.join(D, 'b511_results.json.tmp'), os.path.join(D, 'b511_results.json'))
    print(NL.join(l for l in L if not l.startswith('    1') and not l[4:5].isdigit()))
    return 0


if __name__ == '__main__':
    sys.exit(main())
