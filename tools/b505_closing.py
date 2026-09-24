# -*- coding: utf-8 -*-
"""b505_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
C1 = json.loads(read('b505_c1.json'))
SC = json.loads(read('b505_scores.json'))
L = ['=' * 104, 'b505 -- THE CLOSING RECORD. ### **CLOSED AS REGISTERED UNDER (R116)(1): C1 HELD; C2 REFUSED AT ITS FIXTURE.**', '=' * 104,
     '    c1 %s c2 %s ; exact test fails at %d of %d ; LAMQ agree %d of %d, worst %.1e' % (C1['c1_frac'], C1['c2_frac'], C1['exact_fail'], C1['N'], C1['lam_agree'], C1['lam_n'], C1['lam_worst']),
     '    C2 : %s' % lw(read('b505_c2_log.txt'), 'FIXTURE FAILED'),
     '    (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple(('HELD' if SC[k] is True else SC[k]) for k in ('n1','n2','n3','s1','s2','s3')),
     '', '### THIS ACT`S OWN DEFECTS -- TWO.',
     '    (a) ### **THE FIXTURE BAR |Z| < 1e-10 WAS FINER THAN THE BANK CARRIES** (|Z`| x 6.1e-11 ~ 5e-10); the refusal was correct.',
     '    (b) ### **THE FACE SAID ROUTE A AT 22 BANKED ZEROS; THE TOOL`S STRIDE TOOK 23** (2 off-line + every seventh of 146).',
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b505_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b505_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b505_census_closing.txt'), 'TOTAL MISSING'), lw(read('b505_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b505_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NUMERICAL LANE IS SHUT**; it reopens for b506 under (R116)(3).',
      '    (b) ### **THE (R115)(1)/(2) ANNOTATIONS WAIT FOR b506`S MEASURED COUNT.**',
      '=' * 104]
io.open(os.path.join(D, 'b505_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
