# -*- coding: utf-8 -*-
"""b520_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
R = json.loads(read('b520_results.json'))
SC = json.loads(read('b520_scores.json'))
RE = json.loads(read('b520_reach.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b520 -- THE CLOSING RECORD. ### **VARIANT (B) WIDENED PAST THE LADDER, UNDER (R129).**', '=' * 104,
     '    reach : Q0 %s (stopped at a = %s, tail / B` %.3g) ; xi %s' % (RE['reach']['q'], (RE['stop']['q'] or {}).get('a'),
                                                                   (RE['stop']['q'] or {}).get('tail_over_Bprime', float('nan')), RE['reach']['xi']),
     '    Q0 : %d cells read ; xi : VERIFIED-EST %d of %d, positive %d' % (R['q']['cells'], R['xi']['verified'], R['xi']['cells'], len(R['xi']['h2_pos'])),
     '    reading : ' + R['reading'],
     '    (N1) %s (N2) %s (N3) %s (N4) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS -- FOUR (the desk).'] + [l for l in read('b520_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b520_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b520_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b520_census_closing.txt'), 'TOTAL MISSING'), lw(read('b520_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b520_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NUMERICAL LANE IS SHUT; THE KERNEL LANE REOPENS FOR (f)(i) ON VARIANT (B)** (R129)(3).',
      '    (b) ### **Q0`S VERIFICATION IS THE TAIL MAJORANT`S**: its bound above 150 exceeds the quadrature`s at every width measured,',
      '        b518 through b520 -- the witness question at greater width waits on a tighter tail or a longer Q0 bank.',
      '    (c) ### **XI STAYS POSITIVE TO a = 60** on variant (B), 46 of 46 verified.',
      '=' * 104]
io.open(os.path.join(D, 'b520_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
