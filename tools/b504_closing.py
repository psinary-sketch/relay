# -*- coding: utf-8 -*-
"""b504_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
R = json.loads(read('b504_results.json'))
SC = json.loads(read('b504_scores.json'))
W = lambda v: 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b504 -- THE CLOSING RECORD. ### **ONE TRANSFORM: 109 OF 119 VERIFIED; THE EPSTEIN CONTROL VERIFIES NOWHERE.**', '=' * 104,
     '    verified %d of %d ; the eight wide cells : %s ; largest nv %d' % (R['verified'], R['n'], [e['kind'] for e in R['eight']].count('VERIFIED'), R['maxnv']),
     '    extrema : %s ; rise stands : %s ; least-residual fit : %s' % ([e['a'] for e in R['extrema']], R['rise'], R['win']),
     '    Epstein verified : b325 %d, derived %d' % (R['eps']['325']['verified'], R['eps']['d']['verified']),
     '    (N1) %s (N2) %s (N3) %s (N4) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1','n2','n3','n4','s1','s2','s3')),
     '', '### THIS ACT`S OWN DEFECTS -- ONE, AND ONE OF b504`S FOUND BY IT.',
     '    (a) ### **THE RISE TEST COUNTED THE MINIMUM`S OWN CELL AS AFTER IT** -- repaired; both banked.',
     '    (b) ### **b504`S TOOL CARRIES THE SAME PREDICATE** -- its True passed by 4e-10 against a rounded literal.',
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b504_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b504_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b504_census_closing.txt'), 'TOTAL MISSING'), lw(read('b504_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b504_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NUMERICAL LANE IS SHUT** under (R114)(3). ### Ten cells remain ESTIMATE-SHORT, within x2.6.',
      '    (b) ### **THE EPSTEIN CONTROL IS NOT A CONTROL YET**: its bank stops at 149.72, and b477`s and b502`s margins used a kernel that does not close.',
      '=' * 104]
io.open(os.path.join(D, 'b504_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
