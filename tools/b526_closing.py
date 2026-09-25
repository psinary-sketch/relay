# -*- coding: utf-8 -*-
"""b526_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
SC = json.loads(read('b526_scores.json'))
R = json.loads(read('b526_results.json'))
BP = json.loads(read('b526_bump.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b526 -- THE CLOSING RECORD. ### **XI AT ORDER 7; THE KERNEL`S phi FOUND TO BE A CHOICE, UNDER (R136).**', '=' * 104,
     '    xi at order 7 : IN %d of %d ; VERIFIED-EST %d ; positive %d ; negative %s' % (R['within'], R['cells'], R['verified'], len(R['positive']), R['negative'] or 'NONE'),
     '    Component 2 HALTED : %s ; bases differ by %.4f ; both pass %s ; bad rejected %s' % (BP['halt'], BP['max_pointwise_diff'], BP['both_pass'], BP['bad_rejected']),
     '    form : %s' % R['form'],
     '    (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b526_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b526_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b526_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b526_census_closing.txt'), 'TOTAL MISSING'), lw(read('b526_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b526_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NUMERICAL LANE IS SHUT; (f)(ii) IN THE KERNEL FOLLOWS** (R136)(3).',
      '    (b) ### **THE KERNEL NAMES NO SPECIFIC phi**: its plateau is a Classical.choice base; a concrete definition is the navigator`s call.',
      '    (c) ### **W-ORD-XI-P7 IS CLOSED BY COMPONENT 1**: xi positive at every verified width to 60 at order 7.',
      '=' * 104]
io.open(os.path.join(D, 'b526_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
