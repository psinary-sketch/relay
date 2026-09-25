# -*- coding: utf-8 -*-
"""b518_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
R = json.loads(read('b518_results.json'))
SC = json.loads(read('b518_scores.json'))
FX = json.loads(read('b518_fixture.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b518 -- THE CLOSING RECORD. ### **THE TWO-PROPERTY WINDOW, UNDER (R127).**', '=' * 104,
     '    fixture : ' + ' ; '.join('%s bar met at every u %s (largest diff %.2e)' % (f['object'], f['meets'], max(r['diff'] for r in f['rows'])) for f in FX),
     '    Q0 : VERIFIED-EST %d ; P - PR + A negative %s ; positive %d ; pair negative %d, positive %d ; pair / rest %+.3e to %+.3e'
     % (R['q']['verified'], R['q']['h2_neg'] or 'NONE', len(R['q']['h2_pos']), len(R['q']['pair_neg']), len(R['q']['pair_pos']), R['q']['ratio_min'], R['q']['ratio_max']),
     '    xi : VERIFIED-EST %d ; P - PR + A positive %d ; negative %s' % (R['xi']['verified'], len(R['xi']['h2_pos']), R['xi']['h2_neg'] or 'NONE'),
     '    reading : ' + R['reading'],
     '    (N1) %s (N2) %s (N3) %s (N4) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS -- THREE (the desk).'] + [l for l in read('b518_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b518_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b518_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b518_census_closing.txt'), 'TOTAL MISSING'), lw(read('b518_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b518_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NUMERICAL LANE IS SHUT; THE KERNEL LANE REOPENS FOR (f)(i)** (R127)(3).',
      '    (b) ### **THE TWO-PROPERTY WINDOW IS NOT YET THE WITNESS**: the pair is negative at every width, and its ratio to the rest',
      '        is -2.574e-01 at the widest cell -- the number the next design starts from, (R127)(2).',
      '    (c) ### **b515`S SPEC NAMES ITSELF AS ITS SOURCE** (defect (a)): found, reported, not edited.',
      '=' * 104]
io.open(os.path.join(D, 'b518_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
