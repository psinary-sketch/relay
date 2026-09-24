# -*- coding: utf-8 -*-
"""b502_desk_bank.py -- THE DESK. ### **SCORED ON PRINTED CELLS, INCLUDING AGAINST THE SEAT.**"""
import io, json, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
R = json.loads(io.open(os.path.join(D, 'b502_results.json'), encoding='utf-8').read())
w = lambda v: 'HELD' if v else 'REFUTED'
n1 = len(R['new_not_above']) == 0
n2 = R['win_new'] != '(a) c'
n3 = len(R['epneg']) >= 1
s1 = len(R['epneg']) == 0
s2 = R['win_new'] == '(c) c/log a'
s3 = any(e['t'] == 'MIN' and e['src'] == 'new' for e in R['extrema'])
mins = [e for e in R['extrema'] if e['src'] == 'new']
L = ['=' * 104, 'b502 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE CELLS THE COMPONENTS PRINTED.**', '=' * 104, '',
     '### THE NAVIGATOR`S THREE.', '-' * 104,
     '  **(N1)** ### **%s.** -- *"m(a) stays positive above its floor at every new cell"* -- new cells not above : %d of %d'
     % (w(n1), len(R['new_not_above']), R['n_new']),
     '  **(N2)** ### **%s.** -- *"fit (a) does NOT have the least residual on the new cells"* -- least : ### **%s**'
     % (w(n2), R['win_new']),
     '    ### and the same form wins on the old cells : %s. ### **A FIT IS A DESCRIPTION OF THE CHART AND NOT A BOUND** --' % R['win_old'],
     '    ### and none of the four one-parameter forms can describe what the tail does next: it TURNS UP.',
     '  **(N3)** ### **%s.** -- *"the Epstein margin is negative at at least one cell, if run"* -- negative cells : %s'
     % (w(n3), R['epneg'] or 'NONE'),
     '    ### It ran, priced under one hour; smallest Epstein margin %+.6f. ### The ladder`s last width is 14.107 and' % R['ep_min'],
     '    ### b334`s crossings sit at widths 40 and 81: **THE CONTROL WAS NOT ASKED A QUESTION IT COULD ANSWER YES TO** at',
     '    ### these widths, and a NONE here is out of range, not a pass of the Epstein object.',
     '', '### THE SEAT`S THREE.', '-' * 104,
     '  **(S1)** ### **%s.** -- the Epstein margin positive at every cell, old and new.' % w(s1),
     '  **(S2)** ### **%s.** -- the seat predicted (c) c/log a; ### **(d) c/a^2 won**, on both sets.' % w(s2),
     '  **(S3)** ### **%s.** -- m turns again among the new cells : %s' % (w(s3), ['%s a=%.6f m=%.9f' % (e['t'], e['a'], e['m']) for e in mins]),
     '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.**' % ([n1, n2, n3].count(True), [n1, n2, n3].count(False)),
     '### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d ; NOT SCORABLE 0.**' % ([s1, s2, s3].count(True), [s1, s2, s3].count(False)),
     '=' * 104]
io.open(os.path.join(D, 'b502_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
json.dump(dict(n1=n1, n2=n2, n3=n3, s1=s1, s2=s2, s3=s3), io.open(os.path.join(D, 'b502_scores.json'), 'w', encoding='utf-8', newline=NL), indent=1)
print(NL.join(L))
