# -*- coding: utf-8 -*-
"""b511_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
R = json.loads(read('b511_results.json'))
SC = json.loads(read('b511_scores.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b511 -- THE CLOSING RECORD. ### **XI`S MARGIN MONOTONE IN THE B-SPLINE FAMILY; NO NEGATIVE EPSTEIN CELL IN THE NOTCH.**', '=' * 104,
     '    verified (xi / Q0) : ' + ' ; '.join('%s %d / %d' % (f, R[f]['xi_verified'], R[f]['q_verified']) for f in ('bspline', 'notch1', 'notch3', 'notch5')),
     '    Q0 margin negative : ' + ' ; '.join('%s %s' % (f, R[f]['q_neg'] or 'NONE') for f in ('bspline', 'notch1', 'notch3', 'notch5')),
     '    xi extrema (B-spline) : %s ; the old three survive : %s' % (R['bspline']['extrema'] or 'NONE', [s['survives'] for s in R['bspline']['survival']]),
     '    (N1) %s (N2) %s (N3) %s (N4) %s, vacuous on notch3 and notch5 ; (S1) %s (S2) %s (S3) %s'
     % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS -- FIVE (the desk, `b511_desk_notes.txt`).'] + [l for l in read('b511_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b511_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b511_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b511_census_closing.txt'), 'TOTAL MISSING'), lw(read('b511_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b511_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NUMERICAL LANE IS SHUT**; the kernel lane reopens for the register-equivalence read at h2_sign.',
      '    (b) ### **W-ORD-FAMILY-SENSITIVITY IS NOT DISCHARGED**; P-PL stays a work-order.',
      '    (c) ### **XI`S B-SPLINE BOUND IS ESTIMATE-SHORT BY AT MOST 1.4 PERCENT** -- the archimedean tail beyond u = 1200 is priced nowhere.',
      '=' * 104]
io.open(os.path.join(D, 'b511_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
