# -*- coding: utf-8 -*-
"""b528_report.py -- COMPONENTS 0-3 FROM THE BANKED RUN. ### `python tools/b528_report.py`
### Every figure recomputed from `b528_check.json`, `b528_fixture.json` and `b528_cells_{q,xi}.jsonl`; the reach, the
### signs and the scores are READINGS (5) and (8) of the sealed face. ### An OUT width is banked as its error terms and NOT
### READ: its sign, pair and ratio are not printed. ### A missing cell file is read as no cell (b521`s defect (b), carried).
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
G_BSPLINE = 1.361
WIN = 'the kernel`s plateau (1/4, log a)'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def load(n):
    return json.loads(io.open(os.path.join(D, n), encoding='utf-8').read())


def cells(obj):
    p = os.path.join(D, 'b528_cells_%s.jsonl' % obj)
    return sorted((json.loads(l) for l in io.open(p, encoding='utf-8') if l.strip()), key=lambda c: c['a']) if os.path.exists(p) else []


def sign(v, B):
    return '+' if v > B else ('-' if v < -B else '?')


def W(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def component(obj, name, cs, L):
    L += ['', '### %s -- %s at gamma_0 = %s on %s, a = 15..60. ### REACH (R131)(2): IN iff tail ESTIMATE <= B` ; B = B` + tail ; every tail an ESTIMATE.'
          % (name, 'Q0' if obj == 'q' else 'XI', cs[0]['gamma0'] if cs else '?', WIN),
          '  %-4s %-9s %-9s %-9s %-5s | %-13s %-2s %-9s %-4s %-13s %-13s %-13s %-10s %-7s %-7s %-6s %s' %
          ('a', 'B`', 'tail EST', 'tail/B`', 'reach', 'P - PR + A', 's', 'B', 'VER', 'pair', 'others', 'on-line', 'pair/rest', 'G', 'e^dL', 'tail%', 'status')]
    for c in cs:
        head = '  %-4.0f %-9.2e %-9.2e %-9.2e %-5s |' % (c['a'], c['Bprime'], c['tail_est'], c['tail_est'] / c['Bprime'], 'IN' if c['within'] else 'OUT')
        if c['within']:
            L.append(head + ' %+.6e %-2s %-9.2e %-4s %+.6e %+.6e %+.6e %+.3e %-7.4f %-7.4f %-6.3f %s'
                     % (c['h2'], sign(c['h2'], c['B']), c['B'], 'YES' if c['verified'] else 'no', c['pair'], c['others'], c['on_rest'],
                        c['ratio'] or 0.0, c['growth'], c['growth_bound'], c['tail_share'], c['tail_status']))
        else:
            L.append(head + ' NOT READ (banked: its error terms only) ; G %.4f (a property of phi, not of the cell) ; %s' % (c['growth'], c['tail_status']))
    inn = [c for c in cs if c['within']]
    ver = [c for c in inn if c['verified']]
    neg = [c for c in ver if c['h2'] < -c['B']]
    pos = [c for c in ver if c['h2'] > c['B']]
    cross = [c for c in inn if c['ratio'] is not None and c['ratio'] <= -1.0]
    R = dict(cells=len(cs), within=[c['a'] for c in inn], outside=[c['a'] for c in cs if not c['within']], verified=len(ver),
             neg=[c['a'] for c in neg], pos=[c['a'] for c in pos], undecided=[c['a'] for c in ver if abs(c['h2']) <= c['B']],
             narrowest_neg=(neg[0]['a'] if neg else None), G_at_narrowest=(neg[0]['growth'] if neg else None),
             cross=(cross[0]['a'] if cross else None), G_at_cross=(cross[0]['growth'] if cross else None),
             neg_full=[c['a'] for c in inn if c['neg_full']],
             tail_over_Bprime_min=(min(c['tail_est'] / c['Bprime'] for c in cs) if cs else None),
             tail_over_Bprime_max=(max(c['tail_est'] / c['Bprime'] for c in cs) if cs else None),
             tcut_at_edge=[c['a'] for c in cs if c['tcut_at_search_edge']],
             shortfall_over_B=[c['a'] for c in cs if c['shortfall'] > c['B']],
             statuses=sorted(set(c['tail_status'] for c in cs)),
             G_range=([min(c['growth'] for c in cs), max(c['growth'] for c in cs)] if cs else None))
    L += ['  ### IN %d of %d ; OUT at %s' % (len(inn), len(cs), R['outside'] if len(R['outside']) < 12 else '%d widths, %s..%s' % (len(R['outside']), R['outside'][0], R['outside'][-1])),
          '  ### tail ESTIMATE / B` over every width : %.2e .. %.2e ; T_cut at the search edge at : %s' % (R['tail_over_Bprime_min'], R['tail_over_Bprime_max'], R['tcut_at_edge'] or 'NONE'),
          '  ### READ: VERIFIED-EST %d ; negative beyond B %s ; positive %d ; undecided %s ; negative beyond the sigma_max bound %s'
          % (R['verified'], R['neg'] or 'NONE', len(R['pos']), R['undecided'] or 'NONE', R['neg_full'] or 'NONE'),
          '  ### the narrowest negative width : %s ; the pair`s ratio at or below -1 first at : %s (G there %s, beside the B-spline`s %.3f)'
          % (R['narrowest_neg'] or 'NONE', R['cross'] or 'NONE', R['G_at_cross'], G_BSPLINE),
          '  ### G over every width (a property of phi alone) : %.4f .. %.4f ; tail status of every cell : %s' % (R['G_range'][0], R['G_range'][1], R['statuses'])]
    return R


def main():
    ck, fx = load('b528_check.json'), load('b528_fixture.json')
    q, xi = cells('q'), cells('xi')
    res = dict(check=dict(n=ck['n'], max_chain=ck['max_chain'], max_window=ck['max_window'], agree=ck['agree']),
               fixture=[dict(a=f['a'], obj=f['obj'], scored=f['scored'], of=len(f['rows']), not_scorable=f['not_scorable'], meets=f['meets'],
                             worst=max(x['diff'] / x['bar'] for x in f['rows'] if x['meets'] is not None)) for f in fx])
    L = ['=' * 150, 'b528 -- BOTH OBJECTS ON THE KERNEL`S FUNCTION, UNDER (R138).', '=' * 150,
         '### COMPONENT 0 (i) -- phi at %d points, a = %s : phi_chain vs the kernel`s definition (mpmath) max %.2e ; the window`s phi max %.2e ; within 1e-14 %s'
         % (ck['n'], ck['a'], ck['max_chain'], ck['max_window'], ck['agree']),
         '### COMPONENT 0 (ii) -- the transform by two independent quadratures (trapezoid of h ; Gauss-Legendre of g x (gamma_0^2 - z^2)), bar sqrt(n) eps SUM|terms|, floor eps SUM|terms|:']
    for f in res['fixture']:
        L.append('  a=%-4.0f %-3s : %d of %d z scored, bar met at every scored z %s ; worst diff/bar %.3f ; NOT SCORABLE (route 2 identically 0) at z = %s'
                 % (f['a'], f['obj'], f['scored'], f['of'], f['meets'], f['worst'], f['not_scorable']))
    res['q'] = component('q', 'COMPONENT 1', q, L)
    res['xi'] = component('xi', 'COMPONENT 2', xi, L)
    Q, X = res['q'], res['xi']
    # ### READING (8)
    xi_in_ver = [c for c in xi if c['within'] and c['verified']]
    n1 = (len(xi_in_ver) > 0 and all(c['h2'] > c['B'] for c in xi_in_ver)) if xi else None
    n2 = (len(Q['neg']) > 0) if q else None
    n3 = (abs(Q['G_at_cross'] / G_BSPLINE - 1.0) <= 0.2 if Q['cross'] is not None else False) if q else None
    s1 = (len(Q['within']) == 0) if q else None
    s2 = (len(xi) == 46 and len(xi_in_ver) == 46) if xi else None
    s3 = all(f['meets'] and not f['not_scorable'] for f in res['fixture'])
    res['scores'] = dict(n1=n1, n2=n2, n3=n3, s1=s1, s2=s2, s3=s3)
    # ### READING (7) -- the form of words, from Components 1 and 2 alone
    if X['within']:
        xi_s = ('xi at 14.1347 on %s: tail ESTIMATE within B` at %d of %d widths (%s..%s), VERIFIED-EST at %d, positive beyond its estimated bound at %d, negative at %s'
                % (WIN, len(X['within']), X['cells'], X['within'][0], X['within'][-1], X['verified'], len(X['pos']), X['neg'] or 'none'))
    else:
        xi_s = 'xi at 14.1347 on %s: no width within reach, no xi cell read' % WIN
    if Q['within']:
        q_s = ('Q0 at 16.290216 on %s: tail ESTIMATE within B` at %d of %d widths, negative beyond its estimated bound at %s, the narrowest %s'
               % (WIN, len(Q['within']), Q['cells'], Q['neg'] or 'none', Q['narrowest_neg'] or 'NONE'))
    else:
        q_s = ('Q0 at 16.290216 on %s: no width within reach -- the tail ESTIMATE exceeds B` by %.1e to %.1e at every width of 15..60 -- no Q0 cell read, '
               'the narrowest negative width NONE, no G at a crossing' % (WIN, Q['tail_over_Bprime_min'], Q['tail_over_Bprime_max']))
    form = ('On %s, every tail an ESTIMATE (W-ORD-SMOOTH-TAIL open), %s; %s. The instances differ from b522`s and b526`s, which were taken on the '
            'order-7 B-spline ramp with the tail a majorant. No cell is a statement about RH.' % (WIN, xi_s, q_s))
    res['form'] = form
    L += ['', '### COMPONENT 3 -- THE FORM OF WORDS, RE-DERIVED FROM COMPONENTS 1 AND 2 ALONE (window and tail status tagged):', '    ' + form,
          '', '### SCORES (READING (8)): (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(res['scores'][k]) for k in ('n1', 'n2', 'n3', 's1', 's2', 's3')),
          '    (N3) is REFUTED when no read Q0 width reaches ratio -1, as READING (8) declared ; (S3) as worded "at every z" -- one z per pair is NOT SCORABLE (defect D1).',
          '=' * 150]
    io.open(os.path.join(D, 'b528_report.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    txt = json.dumps(res, indent=1, default=lambda o: o.item()) + NL
    io.open(os.path.join(D, 'b528_results.json'), 'w', encoding='utf-8', newline=NL).write(txt)
    print(NL.join(L))
    return 0


if __name__ == '__main__':
    sys.exit(main())
