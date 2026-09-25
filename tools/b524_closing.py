# -*- coding: utf-8 -*-
"""b524_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
SC = json.loads(read('b524_scores.json'))
AT = json.loads(read('b524_attempts.json'))
PR = json.loads(read('b524_profile.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b524 -- THE CLOSING RECORD. ### **(f)(i) STATED ON VARIANT (B) IN THE KERNEL, UNDER (R133) AND (R134).**', '=' * 104,
     '    attempts : 0 STOPPED BY HOST ; ' + ' ; '.join('%d exit %d, %d errors, %.1f s' % (a['attempt'], a['exit'], a['errors'], a['seconds']) for a in AT),
     '    profile : %d of %d theorems the standard three on the whole string' % (sum(1 for v in PR['std3'].values() if v), len(PR['std3'])),
     '    grades by statement-read : kWin_classK, paperFT_window_zero, paperFT_window DERIVES ; f_pair_hypothesis STATED, no grade',
     '    (N1) %s (N2) %s (N3) %s (N4) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b524_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b524_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b524_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b524_census_closing.txt'), 'TOTAL MISSING'), lw(read('b524_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b524_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE KERNEL LANE IS SHUT; THE FOLD FOLLOWS AT SPAN NINE** (R133)(5).',
      '    (b) ### **(f)(ii), (f)(iii), (f)(iv) REMAIN**: the pair`s term bounded, the other zeros bounded, the assembly.',
      '    (c) ### **THE KERNEL`S PLATEAU IS THE SMOOTH BUMP, NOT THE INSTRUMENT`S B-SPLINE**; W-ORD-XI-P7 filed (R134)(1).',
      '=' * 104]
io.open(os.path.join(D, 'b524_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
