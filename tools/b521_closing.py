# -*- coding: utf-8 -*-
"""b521_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
R = json.loads(read('b521_results.json'))
SC = json.loads(read('b521_scores.json'))
RE = json.loads(read('b521_reach.json'))
CP = json.loads(read('b521_compare.json'))
NO = json.loads(read('b521_notes.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b521 -- THE CLOSING RECORD. ### **Q0`S TAIL TIGHTENED, THEN THE WIDTH PASS RE-RUN, UNDER (R130).**', '=' * 104,
     '    notes : ' + ' ; '.join('%s %d of %d re-marked, prefix proved %s' % (r['bank'], r['remarked'], r['verified'], r.get('prefix_proved')) for r in NO),
     '    least p : %s ; new tail below b519`s old majorant at %d of %d widths ; validity fixture and control %s' % (SC['least_p'], CP['smaller'], CP['of'], R['validity_ok']),
     '    reach : Q0 %s (stopped at a = %s, tail / B` %.3g) at p = %s ; xi cited from b520, positive %d of %d'
     % (RE['reach'], (RE['stop'] or {}).get('a'), (RE['stop'] or {}).get('tail_over_Bprime', float('nan')), RE['p'], R['xi_cited']['positive'], R['xi_cited']['cells']),
     '    Q0 : %d cells read' % R['q']['cells'],
     '    reading : ' + R['reading'],
     '    (N1) %s (N2) %s (N3) %s (N4) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS -- FIVE (the desk).'] + [l for l in read('b521_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b521_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b521_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b521_census_closing.txt'), 'TOTAL MISSING'), lw(read('b521_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b521_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NUMERICAL LANE IS SHUT; THE KERNEL LANE REOPENS FOR (f)(i) ON VARIANT (B)** (R130)(4).',
      '    (b) ### **AT p = 7 THE CLOSED-FORM TAIL IS BELOW B` FROM a = 30 TO 60 AND ABOVE IT AT a = 15**: the tail falls with width,',
      '        so b520`s increasing-width stop rule ends at the grid`s first width; the priced order at a = 15 is p = 9 (pre-seal).',
      '    (c) ### **XI STAYS POSITIVE TO a = 60** on variant (B), cited from b520.',
      '=' * 104]
io.open(os.path.join(D, 'b521_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
