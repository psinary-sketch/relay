# -*- coding: utf-8 -*-
"""b522_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
R = json.loads(read('b522_results.json'))
SC = json.loads(read('b522_scores.json'))
RE = json.loads(read('b522_reach.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
Q = R['q']
L = ['=' * 104, 'b522 -- THE CLOSING RECORD. ### **VARIANT (B) AT p = 7, THE REACH READ PER WIDTH, UNDER (R131).**', '=' * 104,
     '    reach : %d of 46 IN ; OUT at %s' % (len(RE['within']), RE['outside'] or 'NONE'),
     '    Q0 : %d cells read ; VERIFIED-EST %d ; negative beyond bound %s ; ratio crosses -1 at %s ; most negative %s ; widest (a = %s) %s'
     % (Q['cells'], Q['verified'], Q['h2_neg'] or 'NONE', Q['cross_minus_one'] or 'NONE', Q['ratio_min'], Q['widest_a'], Q['widest_ratio']),
     '    xi : cited from b520, positive %d of %d' % (R['xi_cited']['positive'], R['xi_cited']['cells']),
     '    reading : ' + R['reading'],
     '    (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + ([l for l in read('b522_defects.txt').rstrip(chr(10)).split(chr(10)) if l] if os.path.exists(os.path.join(D, 'b522_defects.txt')) else ['    NONE FOUND.']) + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b522_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b522_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b522_census_closing.txt'), 'TOTAL MISSING'), lw(read('b522_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b522_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NUMERICAL LANE IS SHUT; THE KERNEL LANE TAKES (f)(i) ON VARIANT (B)** (R131)(4).',
      '    (b) ### **THE INCREASING-WIDTH STOP RULE IS RETIRED; THE REACH IS READ PER WIDTH** (R131)(1)-(2).',
      '    (c) ### **XI STAYS POSITIVE TO a = 60** on variant (B), cited from b520.',
      '=' * 104]
io.open(os.path.join(D, 'b522_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
