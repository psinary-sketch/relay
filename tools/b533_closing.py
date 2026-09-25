# -*- coding: utf-8 -*-
"""b533_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
SC = json.loads(read('b533_scores.json'))
AT = json.loads(read('b533_attempts.json'))
PR = json.loads(read('b533_profile.json'))
RW = json.loads(read('b533_rows.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b533 -- THE CLOSING RECORD. ### **f4, THE POWER-WINDOW ROUTE, ACT ONE OF TWO: THE WINDOW AND THE DOMINANT ZERO, UNDER (R143).**', '=' * 104,
     '    the module : ' + ' ; '.join('attempt %d exit %d, %d errors, %.1f s, failing %s' % (a['attempt'], a['exit'], a['errors'], a['seconds'],
                                                                                           a.get('failed_decls') or 'NONE') for a in AT)
     + ' ; std3 %d of %d ; halted %s' % (sum(1 for v in PR['std3'].values() if v), len(PR['std3']), SC['halted'] or 'NONE'),
     '    row %s : %s' % (RW['cells'][0], RW['cells'][4]),
     '    stated, not proved : nodes_distinct_nonreal (%s) ; rh_strip_imp_rh (%s)'
     % ((PR.get('checks') or {}).get('nodes_distinct_nonreal'), (PR.get('checks') or {}).get('rh_strip_imp_rh')),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s'
     % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b533_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    pre-push : %s' % lw(read('b533_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b533_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'),
             ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula'), ('SIDE-kernel', 'D:/SIDE-kernel')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b533_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b533_census_closing.txt'), 'TOTAL MISSING'), lw(read('b533_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b533_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE KERNEL LANE IS SHUT.** L7 (the limit) and L8 (the assembly) are b534`s, under (R143)`s halt rule.',
      '    (b) ### **nodes_distinct_nonreal CARRIES A CAVEAT FOR b534**: the square of gammaOf rho is real when Im rho = 0, which the',
      '        kernel`s configuration does not exclude; b534`s nodes need Im rho /= 0 from somewhere, or a statement that avoids it.',
      '    (c) ### **THE SEAM`S LEFT HALF-PLANE IS ABSENT FROM MATHLIB BY NAME**; priced as derivable from the trivial zeros and the',
      '        functional equation, not attempted (R143)(4).',
      '    (d) ### **E-2026-09-25-1 STAYS DRAFTED; THE THREE (R110) EDITS UNAPPLIED; THE CEILING`S NEXT WORDING UNRULED** until the',
      '        f4 attempt closes (R143)(1).',
      '    (e) ### **defect (d)`s reading waits on the author**: power_contDiff and paperFT_power carry the window`s support in',
      '        [-L, L], undeclared on the face, graded DERIVES as L3`s standing context.',
      '=' * 104]
io.open(os.path.join(D, 'b533_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
