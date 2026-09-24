# -*- coding: utf-8 -*-
"""b510_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
P = json.loads(read('b510_profile.json'))
R = json.loads(read('b510_price.json'))
SC = json.loads(read('b510_scores.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b510 -- THE CLOSING RECORD. ### **h2 STATED AS ONE Prop; THE TABLE ROW MADE; W-ORD-PL-CLASS PRICED.**', '=' * 104,
     '    h2_sign_imp_aim : %s' % (P.get('new') or ['NONE'])[0],
     '    AxiomCheck : %d lines, each the standard three : %s' % (len(json.loads(read('b510_axiomcheck.json'))['lines']),
        all(l.endswith('[propext, Classical.choice, Quot.sound]') for l in json.loads(read('b510_axiomcheck.json'))['lines'])),
     '    table row : %s' % ('PRESENT' if 'SIDEExplicitFormula.B321.b321_identity' in read('terminal_table.md') else 'ABSENT'),
     '    Component 3 : NONE ; Component 4 : (b) %.0f cell-seconds on xi, %.0f jointly' % (R['b504_cell_seconds'], R['joint_cell_seconds']),
     '    (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS -- FIVE.'] + [l for l in read('b510_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '    (d) ### **THE SUITE READ THE TERMINAL TABLE BEFORE REGENERATING IT**, so the first post-push `G-TABLE-ROW` scored the previous',
     '        close`s table and FAILED while the regenerated table held the row. ### Carried from b509`s suite verbatim; b509`s own failure',
     '        was real (its regenerated table held no row). ### Repaired post-push; the first run banked as `b510_checks_postpush_first.txt`.',
     '    (e) ### **THIS CLOSING TOOL WAS FIRST ASSEMBLED THROUGH A QUOTED HEREDOC THAT COLLAPSED A BACKSLASH** -- caught by the parser; rewritten.',
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b510_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b510_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b510_census_closing.txt'), 'TOTAL MISSING'), lw(read('b510_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b510_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE KERNEL LANE IS SHUT.** ### b509`s G-TABLE-ROW failure is CLOSED by AxiomCheck.lean, under (R119)(1).',
      '    (b) ### **W-ORD-PL-CLASS IS PRICED AND NOT TAKEN**; its trigger is the act after b510, on the author`s word.',
      '    (c) ### **h2 IS STATED, NOT PROVED**; the zero quantifier enters only through b321_identity; b334`s crossings stay UNVERIFIED.',
      '=' * 104]
io.open(os.path.join(D, 'b510_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
