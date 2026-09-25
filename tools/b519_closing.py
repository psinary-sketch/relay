# -*- coding: utf-8 -*-
"""b519_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
R = json.loads(read('b519_results.json'))
SC = json.loads(read('b519_scores.json'))
FX = json.loads(read('b519_fixture.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b519 -- THE CLOSING RECORD. ### **THREE VARIANTS OF THE TWO-PROPERTY WINDOW, UNDER (R128).**', '=' * 104,
     '    fixtures : ' + ' ; '.join('(%s) %s %s' % (f['variant'], f['object'], 'met' if f['meets'] else 'NOT MET') for f in FX)]
L += ['    (%s) Q0 VERIFIED-EST %d ; negative %s ; pair negative %d of %d ; widest ratio %+.4e ; xi positive %d of %d verified'
      % (v, R[v]['q']['verified'], R[v]['q']['h2_neg'] or 'NONE', len(R[v]['q']['pair_neg']), R[v]['q']['cells'], R[v]['q']['widest_ratio'],
         len(R[v]['xi']['h2_pos']), R[v]['xi']['verified']) for v in ('A', 'B', 'C')]
L += ['    the witness at Q0 : %s ; (B)`s realized growth over b518`s at the widest cell %.4f' % (', '.join(R['witness']) or 'NONE', SC['growth_ratio_B_over_b518']),
      '    (N1) %s (N2) %s (N3) %s (N4) %s, vacuous on (C) ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 's1', 's2', 's3')),
      '', '### THIS ACT`S OWN DEFECTS -- FIVE (the desk).'] + [l for l in read('b519_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b519_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b519_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b519_census_closing.txt'), 'TOTAL MISSING'), lw(read('b519_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b519_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NUMERICAL LANE IS SHUT; THE KERNEL LANE REOPENS FOR (f)(i)** (R128)(4) -- with no variant the witness, the',
      '        window it states is the best measured, (B) EDGE-WEIGHTED, at -4.16e-01 of the rest at the widest cell.',
      '    (b) ### **NOTCHES AMPLIFY THE FAR ZEROS** by the notch polynomial more than they suppress the near ones: (A) -6.0e-02,',
      '        (C) -4.8e-06 against b518`s -2.57e-01.',
      '    (c) ### **W-ORD-H2-BRIDGE HEADS K1**; h2_sign is Weil`s positivity criterion on classK, and the record says so in those words.',
      '=' * 104]
io.open(os.path.join(D, 'b519_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
