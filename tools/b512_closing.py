# -*- coding: utf-8 -*-
"""b512_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
P = json.loads(read('b512_profile.json'))
TB = json.loads(read('b512_table.json'))
SC = json.loads(read('b512_scores.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b512 -- THE CLOSING RECORD. ### **THE REGISTER-EQUIVALENCE READ; THE RECTIFICATION ENTERED.**', '=' * 104,
     '    h2_sign_imp_cell : %s' % (P.get('new') or ['NONE'])[0],
     '    forms : ' + ' ; '.join('%s %s' % (r['key'], r['status']) for r in TB['C1']),
     '    implications : ' + ' ; '.join('%s %s' % (r['pair'], r['status']) for r in TB['C2']),
     '    weakest : %s -- a statement about derivability, not a theorem' % TB['weakest'],
     '    (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS -- TWO (the desk).'] + [l for l in read('b512_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b512_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b512_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b512_census_closing.txt'), 'TOTAL MISSING'), lw(read('b512_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b512_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE KERNEL LANE IS SHUT.** ### RH -> h2_sign has every lemma FOUND and is not compiled: the order asked for a read.',
      '    (b) ### **W-ORD-FAMILY-SENSITIVITY (the matched window) is next by (R121)(4); W-ORD-STRICT-BOUND and P-PL stand.**',
      '    (c) ### **EVERY CELL OF THE RECORD IS VERIFIED-EST**; b334`s crossings stay UNVERIFIED.',
      '=' * 104]
io.open(os.path.join(D, 'b512_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
