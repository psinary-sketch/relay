# -*- coding: utf-8 -*-
"""b514_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
R = json.loads(read('b514_results.json'))
SC = json.loads(read('b514_scores.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b514 -- THE CLOSING RECORD. ### **THE MATCHED WINDOW, UNDER (R123).**', '=' * 104,
     '    Q0 : VERIFIED-EST %d ; margin negative %s ; P - PR + A negative %s ; pair negative %s ; share max %.4f ; above 0.50 at %d widths'
     % (R['q']['verified'], R['q']['m_neg'] or 'NONE', R['q']['h2_neg'] or 'NONE', R['q']['pair_neg'] or 'NONE', R['q']['share_max'], len(R['q']['share_over_half'])),
     '    xi : VERIFIED-EST %d ; margin positive %d ; negative %s' % (R['xi']['verified'], len(R['xi']['m_pos']), R['xi']['m_neg'] or 'NONE'),
     '    reading : ' + R['reading'],
     '    (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS -- FOUR (the desk).'] + [l for l in read('b514_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b514_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b514_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b514_census_closing.txt'), 'TOTAL MISSING'), lw(read('b514_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b514_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NUMERICAL LANE IS SHUT.** ### The cosine-matched window put the far off-line pair on the positive side at every width.',
      '    (b) ### **(R123)(2)`S TWO WORK-ORDERS STAND**, trigger the next fold; (d) and (f) of b513 stay ABSENT.',
      '    (c) ### **EVERY CELL OF THE RECORD IS VERIFIED-EST**; W-ORD-STRICT-BOUND stands.',
      '=' * 104]
io.open(os.path.join(D, 'b514_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
