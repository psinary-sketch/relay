# -*- coding: utf-8 -*-
"""b523_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
R = json.loads(read('b523_results.json'))
SC = json.loads(read('b523_scores.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b523 -- THE CLOSING RECORD. ### **THE WITNESS`S THREE CAVEATS PRICED, UNDER (R132).**', '=' * 104,
     '    sigma_max %.3f (control %s) ; E(150) %.2f (controls %s, Stirling pad %s)' % (R['sigma_max'], R['control'], R['E150'], R['controls_ok'], R['stirling_ok']),
     '    negative : b522 %d ; under sigma %d ; under the full bound %d ; largest shortfall / margin %.2e' % (R['neg522'], R['neg_sigma'], R['neg_full'], R['shortfall_ratio_max']),
     '    surviving all three : %d, narrowest %s ; VERIFIED-EST-TAIL at %d of 33' % (len(R['survivors']), R['narrowest'], len(R['tail_led_full'])),
     '    verdict : ' + R['verdict'],
     '    (N1) %s (N2) %s (N3) %s (N4) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b523_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b523_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b523_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b523_census_closing.txt'), 'TOTAL MISSING'), lw(read('b523_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b523_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NUMERICAL LANE IS SHUT; THE KERNEL LANE TAKES (f)(i) ON VARIANT (B)** (R132)(5), naming G`s mechanism.',
      '    (b) ### **THE WITNESS IS HELD, NOT ANNOUNCED**: the seat printed the verdict its numbers give; the navigator rules on the bar.',
      '    (c) ### **Q0`S STRIP IS [1 - 1.425, 1.425] AND ITS COUNT IS BOUNDED ABOVE 150** -- instruments for any later Q0 tail.',
      '=' * 104]
io.open(os.path.join(D, 'b523_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
