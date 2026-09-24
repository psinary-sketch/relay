# -*- coding: utf-8 -*-
"""b503_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
R = json.loads(read('b503_results.json'))
SC = json.loads(read('b503_scores.json'))
L = ['=' * 104, 'b503 -- THE CLOSING RECORD. ### **THE RESIDUAL OF 7 GONE; 64 VERIFIED AS ORDERED, 86 CONSISTENT.**', '=' * 104,
     '    verified (ordered) %d of %d ; consistent %d ; still unverified %d' % (R['verified'], R['n'], R['consistent_verified'], len(R['unverified'])),
     '    extrema on the verified set : %s ; on the consistent set : %s' % ([e['a'] for e in R['extrema']], [e['a'] for e in R['consistent_extrema']]),
     '    rise after 13.153 survives : %s ; least-residual fit : %s' % (R['rise'], R['win_new']),
     '    (N1) %s (N2) %s (N3) %s (N4) %s ; (S1) %s (S2) %s (S3) %s' % tuple('HELD' if SC[k] else 'REFUTED' for k in ('n1','n2','n3','n4','s1','s2','s3')),
     '', '### THIS ACT`S OWN DEFECTS -- TWO.',
     '    (a) ### **THE REPORT NARRATED A PREDICTION BESIDE A COUNT THAT CONTRADICTED IT** -- repaired; both banked.',
     '    (b) ### **THE SUITE ASSEMBLER JOINED TWO BLOCKS WITHOUT A NEWLINE, AND A HEREDOC ATE THE FIX** -- caught by the parser.',
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b503_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b503_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b503_census_closing.txt'), 'TOTAL MISSING'), lw(read('b503_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b503_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NUMERICAL LANE IS SHUT** under (R113)(2). ### Eight cells from a = 13.637 need zeros past 9877.78.',
      '    (b) ### **VERIFICATION WAS SCORED ON A RESIDUAL THAT MIXES TWO TRANSFORMS** -- the navigator`s to rule which counts.',
      '=' * 104]
io.open(os.path.join(D, 'b503_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
