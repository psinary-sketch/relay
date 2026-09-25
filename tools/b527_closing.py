# -*- coding: utf-8 -*-
"""b527_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
SC = json.loads(read('b527_scores.json'))
AT = json.loads(read('b527_attempts.json'))
PR = json.loads(read('b527_profile.json'))
DF = json.loads(read('b527_statement_diff.json'))
VA = json.loads(read('b527_values.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b527 -- THE CLOSING RECORD. ### **THE PLATEAU MADE CONCRETE, UNDER (R137).**', '=' * 104,
     '    attempts : ' + ' ; '.join('%d exit %d, %d errors, %.1f s%s' % (a['attempt'], a['exit'], a['errors'], a['seconds'], ' (STOPPED by the seat`s timeout)' if a.get('stopped_by') else '') for a in AT),
     '    profile : %d of %d theorems the standard three on the whole string ; #print plateau : %s' % (sum(1 for v in PR['std3'].values() if v), len(PR['std3']), (PR.get('print_plateau') or '').split(chr(10))[-1]),
     '    b524 statements : %s of %s byte-identical ; diff lines %s ; new %s' % (DF['identical'], DF['b524_theorems'], DF['diff_lines'], DF['new_theorems']),
     '    values : max |diff| %.2e over %d points' % (VA['max_diff'], len(VA['rows'])),
     '    (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b527_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b527_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b527_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b527_census_closing.txt'), 'TOTAL MISSING'), lw(read('b527_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b527_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE KERNEL LANE IS SHUT; THE NUMERICAL LANE REOPENS FOR b528** on the concrete plateau (R137)(4).',
      '    (b) ### **b528 IMPORTS `phi_chain` FROM tools/b527_values.py** -- the kernel`s function, agreeing to 4.4e-16.',
      '    (c) ### **(f)(ii) FOLLOWS**, for every C^4 phi >= 0 with the realized G as hypothesis (R137)(3).',
      '=' * 104]
io.open(os.path.join(D, 'b527_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
