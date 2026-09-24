# -*- coding: utf-8 -*-
"""b509_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
P = json.loads(read('b509_profile.json'))
C = json.loads(read('b509_clauses.json'))
SC = json.loads(read('b509_scores.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b509 -- THE CLOSING RECORD. ### **b321`S IDENTITY DERIVED; INTERFACES AGAINST THE LADDER; THE TABLE ROW NOT MADE.**', '=' * 104,
     '    terminal : SIDEExplicitFormula.B321.b321_identity ; profile %s' % (P.get('new') or ['NONE'])[0],
     '    clauses : SAME %d ; DIFFERS %s ; constant b321Norm := %s' % (len(C['clauses']) - len(C['differs']), C['differs'], C['norm_constant']),
     '    grade : %s on %s' % (C['grade'], C['premise'].split(':')[0]),
     '    (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS -- SIX; THE SIXTH LEAVES A POST-PUSH ARM FAILING.'] + [l for l in read('b509_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '    (f) ### **`G-TABLE-ROW` FAILS POST-PUSH: THE REGENERATED TABLE ADDED 0 ROWS.** ### Its tight matcher pairs a backticked',
     '        name with a grade word IN ONE CELL WITHIN 120 CHARACTERS; row 358 names the terminal in its third cell and grades',
     '        it in its fifth, and the trail states INTERFACES without the name. ### The order`s "regenerated with the new row"',
     '        is NOT MET. ### No ledger text was added after the fact to satisfy the matcher. ### ROUTED.',
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b509_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b509_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b509_census_closing.txt'), 'TOTAL MISSING'), lw(read('b509_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b509_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE KERNEL LANE IS SHUT.** ### (R104)`s act 4 is next: h2 stated as one Prop.',
      '    (b) ### **THE TABLE ROW IS OWED**: a ledger cell pairing the name with its grade, or an AxiomCheck file in the kernel.',
      '    (c) ### **P-PL IS NAMED AND NOT DISCHARGED**; W-ORD-FAMILY-SENSITIVITY is filed; b334`s crossings stay UNVERIFIED.',
      '=' * 104]
io.open(os.path.join(D, 'b509_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
