# -*- coding: utf-8 -*-
"""b515_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
R = json.loads(read('b515_results.json'))
SC = json.loads(read('b515_scores.json'))
FX = json.loads(read('b515_fixture.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b515 -- THE CLOSING RECORD. ### **THE WINDOW WITH A ZERO AT THE ON-LINE POINT, UNDER (R124).**', '=' * 104,
     '    fixture : ' + ' ; '.join('%s %s %.2e' % (f['object'], 'MET' if f['meets'] else 'NOT MET', f['maxdiff']) for f in FX) + ' (bar 1e-10)',
     '    Q0 : VERIFIED-EST %d ; P - PR + A negative %s ; positive %d ; pair negative %d, positive %d ; pair / rest %+.2e to %+.2e'
     % (R['q']['verified'], R['q']['h2_neg'] or 'NONE', len(R['q']['h2_pos']), len(R['q']['pair_neg']), len(R['q']['pair_pos']), R['q']['ratio_min'], R['q']['ratio_max']),
     '    xi : VERIFIED-EST %d ; P - PR + A positive %d ; negative %s' % (R['xi']['verified'], len(R['xi']['h2_pos']), R['xi']['h2_neg'] or 'NONE'),
     '    reading : ' + R['reading'],
     '    (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS -- THREE (the desk).'] + [l for l in read('b515_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b515_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b515_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b515_census_closing.txt'), 'TOTAL MISSING'), lw(read('b515_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b515_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE SUITE CLOSED NOT CLEAN ON ONE ARM, G-FIXTURE-BAR** -- the registered 1e-10 bar, not met at Q0 by 1.24x; not weakened.',
      '    (b) ### **THE NUMERICAL LANE IS SHUT; THE FOLD FOLLOWS AT SPAN 8** (R124)(3), carrying (R123)(2)`s two table work-orders and',
      '        W-ORD-WEIL-CONVERSE; the kernel lane reopens after it.',
      '    (c) ### **THE ZERO-AT-THE-POINT WINDOW TURNS THE PAIR`S SIGN BUT NOT THE SUM**: a window whose transform is largest at the low',
      '        on-line ordinates cannot let one off-line pair carry Z; the dominance (f) needs the line transform small everywhere else.',
      '=' * 104]
io.open(os.path.join(D, 'b515_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
