# -*- coding: utf-8 -*-
"""b528_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
SC = json.loads(read('b528_scores.json'))
R = json.loads(read('b528_results.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
Q, X = R['q'], R['xi']
L = ['=' * 104, 'b528 -- THE CLOSING RECORD. ### **BOTH OBJECTS ON THE KERNEL`S PLATEAU, UNDER (R138).**', '=' * 104,
     '    phi : %d points, max %.1e against the kernel ; fixture : %s' % (R['check']['n'], R['check']['max_chain'], ' ; '.join('a=%.0f %s %d/%d %s' % (f['a'], f['obj'], f['scored'], f['of'], f['meets']) for f in R['fixture'])),
     '    Q0 : IN %d of %d ; tail EST / B` %.1e .. %.1e ; negative %s ; crossing %s' % (len(Q['within']), Q['cells'], Q['tail_over_Bprime_min'], Q['tail_over_Bprime_max'], Q['neg'] or 'NONE', Q['cross'] or 'NONE'),
     '    xi : IN %d of %d ; VERIFIED-EST %d ; positive %d ; negative %s' % (len(X['within']), X['cells'], X['verified'], len(X['pos']), X['neg'] or 'NONE'),
     '    form : %s' % R['form'],
     '    (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b528_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b528_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b528_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b528_census_closing.txt'), 'TOTAL MISSING'), lw(read('b528_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b528_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NUMERICAL LANE IS SHUT; THE KERNEL LANE TAKES (f)(ii)** (R138)(4).',
      '    (b) ### **W-ORD-SMOOTH-TAIL STAYS OPEN**: every b528 cell`s tail is an ESTIMATE (R138)(2).',
      '=' * 104]
io.open(os.path.join(D, 'b528_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
