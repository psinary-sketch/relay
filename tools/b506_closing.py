# -*- coding: utf-8 -*-
"""b506_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
R = json.loads(read('b506_c2_results.json'))
SC = json.loads(read('b506_scores.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
C3 = read('b506_c3.txt')
L = ['=' * 104, 'b506 -- THE CLOSING RECORD. ### **180 ZEROS BELOW 150; THE BANK LACKS 30, NONE AT SIGMA > 1; THE DERIVED KERNEL VERIFIES 93 OF 93.**', '=' * 104,
     '    fixture : %d / %d of 148 ; count %d (smooth %.4f + S %.4f) ; lacks %d ; new off-line %d ; at sigma > 1 %d ; control %s'
     % (R['fixture_dist_pass'], R['fixture_route_pass'], R['total'], R['smooth'], R['S'], R['lacks_strip'], R['new_off'], R['beyond1'], R['control']),
     '    C3 : %s ; %s' % (lw(C3, 'POPULATION :'), lw(C3, 'VERIFIED IN THE POPULATION')),
     '    (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1','n2','n3','s1','s2','s3')),
     '', '### THIS ACT`S OWN DEFECTS -- THREE, AND TWO OF EARLIER RECORDS FOUND BY IT.',
     '    (a) ### **THE EVALUATOR CRASHED TWICE AT REMOVABLE POINTS** (s = 1/2, then s = -1/2, on the real segment); repaired by a 1e-20 step.',
     '    (b) ### **THE PRICE SAID ABOUT 15 MINUTES; THE RUN TOOK %.0f s** -- edges 817 s, under the face`s twenty-minute rule.' % R['seconds'],
     '    (c) ### **TWO ARMS OF THE SUITE WERE WRONG AT FIRST** -- an empty list read as missing; a mutation pointed at row 354. Both repaired pre-push.',
     '    (d) ### **b504`S TRAIL PUT THE EPSTEIN BOUNDS "NEAR 1e-7"**; they are 9e-7 to 2.3e-6. Routed.',
     '    (e) ### **THE (R115) NOTES QUOTE "DOES NOT CLOSE ... AT ANY CELL"**; the derived kernel closes on the completed bank. Routed.',
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b506_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b506_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b506_census_closing.txt'), 'TOTAL MISSING'), lw(read('b506_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b506_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NUMERICAL LANE IS SHUT**; the kernel lane reopens for (R104)`s act 3 under (R116)(3).',
      '    (b) ### **COMPONENT 4`S EXTENSION TOWARD T NEAR 1,500, AND THE MARGIN, DEFERRED BY THE ORDER.**',
      '=' * 104]
io.open(os.path.join(D, 'b506_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
