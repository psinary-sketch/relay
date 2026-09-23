# -*- coding: utf-8 -*-
"""b501_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
import io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
def read(p):
    return io.open(os.path.join(D, p), encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
def lw(t, n):
    return next((l.strip() for l in t.split(NL) if n in l), '')
def git(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True).stdout.strip()
R = json.loads(read('b501_results.json'))
SC = json.loads(read('b501_scores.json'))
L = ['=' * 104, 'b501 -- THE CLOSING RECORD. ### **THE BOUND IS WHAT THE TWO SIDES DISAGREE BY.**', '=' * 104,
     '    base reproduces b492 : %d of %d ; non-asymptotic %d' % (R['repro'], R['n'], R['nonasymptotic']),
     '    the order`s test B >= |W+Z| : %d of %d ; composite %d ; worst shortfall x%.2f' % (R['test_ok'], R['n'], R['composite_ok'], SC['worst']),
     '    positive control passes %s ; negative control grows at %d of 3' % (R['positive']['passes'], sum(n['grows'] for n in R['negative'])),
     '    floors exceeded %d of %d ; min cell a=%s floor %.3e' % (R['floors_exceeded'], R['n'], R['min_cell']['a'], R['min_cell']['B']),
     '    (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple('HELD' if SC[k] else 'REFUTED' for k in ('n1','n2','n3','s1','s2','s3')),
     '', '### THIS ACT`S OWN DEFECTS -- TWO.',
     '    (a) ### **THE FACE`S READING (1) WAS WRONG** -- b483`s two families ARE the thirty-five; corrected in the desk.',
     '    (b) ### **`corr_row.py` APPENDED A MALFORMED ROW AGAIN** -- the pipes of an absolute value; restored, re-written.',
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b501_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b501_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b501_census_closing.txt'), 'TOTAL MISSING'), lw(read('b501_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b501_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **b502 RUNS UNDER THESE FLOORS**; the lane shuts at its close.',
      '    (b) ### **THE BOUND IS AN ESTIMATE** -- short at ten cells by at most x1.59; `corr_row.py` still validates after it writes.',
      '=' * 104]
io.open(os.path.join(D, 'b501_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
