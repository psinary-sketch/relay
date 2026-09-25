# -*- coding: utf-8 -*-
"""b529_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
SC = json.loads(read('b529_scores.json'))
AT = json.loads(read('b529_attempts.json'))
PR = json.loads(read('b529_profile.json'))
RD = json.loads(read('b529_read.json'))
VA = json.loads(read('b529_values.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b529 -- THE CLOSING RECORD. ### **(f)(ii), THE PAIR`S TERM, AS FAR AS IT DERIVES, UNDER (R139).**', '=' * 104,
     '    attempts : ' + ' ; '.join('%d exit %d, %d errors, %.1f s%s' % (a['attempt'], a['exit'], a['errors'], a['seconds'], (' (STOPPED: ' + a['stopped_by'] + ')') if a.get('stopped_by') else '') for a in AT),
     '    profile : %d of %d theorems the standard three on the whole string ; #check farSmall : %s' % (sum(1 for v in PR['std3'].values() if v), len(PR['std3']), PR.get('check_prop')),
     '    vendored lemmas : %s ; beyond b524`s : %s' % (RD['lemma_refs'], RD['lemmas_beyond_b524'] or 'NONE'),
     '    the named hypothesis at a = 34 : eps_delta %.3e ; eps_zero %.3e ; c - eps` %.6f ; bound %.4f beside the pair term %.4f'
     % (VA['eps_delta'], VA['eps_zero'], VA['c_minus_eps'], VA['rhs'], VA['pairTwo_khat'][0]),
     '    (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b529_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b529_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b529_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b529_census_closing.txt'), 'TOTAL MISSING'), lw(read('b529_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b529_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE KERNEL LANE IS SHUT** (R139)(4).',
      '    (b) ### **f2 STANDS AT DERIVES (Components 1, 2) AND INTERFACES (Component 3, on farSmall)**; f3 and f4 OPEN.',
      '    (c) ### **W-ORD-BSPLINE-INSTANCE is filed by the author (R139)(3)**; not taken.',
      '=' * 104]
io.open(os.path.join(D, 'b529_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
