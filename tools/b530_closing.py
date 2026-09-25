# -*- coding: utf-8 -*-
"""b530_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
SC = json.loads(read('b530_scores.json'))
AT = {w: json.loads(read('b530_attempts_%s.json' % w)) for w in ('decay', 'rest')}
PR = json.loads(read('b530_profile.json'))
VA = json.loads(read('b530_values.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b530 -- THE CLOSING RECORD. ### **f3, THE OTHER ZEROS BOUNDED ABOVE, WITH ITS LIMIT PRINTED, UNDER (R140).**', '=' * 104]
for w in ('decay', 'rest'):
    L.append('    attempts %s : ' % w + ' ; '.join('%d exit %d, %d errors, %.1f s' % (a['attempt'], a['exit'], a['errors'], a['seconds']) for a in AT[w]))
L += ['    profile : %d of %d theorems the standard three on the whole string' % (sum(1 for v in PR['std3'].values() if v), len(PR['std3'])),
      '    rest_bound`s hypotheses on Z : %s' % SC['rest_z_hyps'],
      '    at a = 34 : R %.4e ; the measured rest %.4f ; R / rest %.4e ; A0 %.1f (measured, not proved) ; G / e^(delta L) %.4f'
      % (VA['R'], VA['rest_measured'], VA['ratio_R_rest'], VA['A0_measured'], VA['G_over_exp']),
      '    (N1) %s (N2) %s (N3) %s (N4) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 's1', 's2', 's3')),
      '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b530_defects.txt').rstrip(NL).split(NL) if l] + [
      '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
      '    post-push : %s' % lw(read('b530_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b530_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b530_census_closing.txt'), 'TOTAL MISSING'), lw(read('b530_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b530_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE KERNEL LANE IS SHUT** (R140)(3).',
      '    (b) ### **f3 STANDS AT DERIVES UNDER H-STRIP AND H-COUNT (rest_bound)**; rest_bound_closed and rest_bound_zeta',
      '        (no hypothesis for zeta) compiled and UNGRADED, the author`s to rule.',
      '    (c) ### **f4 OPEN**: not_f4_needs proves the growth comparison fails for delta < 1/2; (A) HMax UNKNOWN; (B) priced,',
      '        two lemmas ABSENT.',
      '=' * 104]
io.open(os.path.join(D, 'b530_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
