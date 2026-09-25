# -*- coding: utf-8 -*-
"""b534_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
SC = json.loads(read('b534_scores.json'))
AT = json.loads(read('b534_attempts.json'))
PR = json.loads(read('b534_profile.json'))
RW = json.loads(read('b534_rows.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b534 -- THE CLOSING RECORD. ### **f4, THE POWER-WINDOW ROUTE, ACT TWO OF TWO: THE LIMIT AND THE ASSEMBLY, UNDER (R144).**', '=' * 104,
     '    the module : ' + ' ; '.join('attempt %d exit %d, %d errors, %.1f s, failing %s' % (a['attempt'], a['exit'], a['errors'], a['seconds'],
                                                                                           a.get('failed_decls') or 'NONE') for a in AT)
     + ' ; std3 %d of %d ; halted %s' % (sum(1 for v in PR['std3'].values() if v), len(PR['std3']), SC['halted'] or 'NONE'),
     '    row %s : %s' % (RW['cells'][0], RW['cells'][4]),
     '    the three statements : ' + ' | '.join(' '.join(((PR.get('checks') or {}).get(n) or '').split()) for n in ('h2_sign_iff_rh_strip', 'h2_sign_imp_rh_of_seam', 'rh_strip_imp_rh')),
     '    (N1) %s (N2) %s%s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s'
     % (W(SC['n1']), W(SC['n2']), ' VACUOUS' if SC.get('n2_vacuous') else '', W(SC['n3']), W(SC['n4']), W(SC['n5']), W(SC['n6']),
        W(SC['s1']), W(SC['s2']), W(SC['s3'])),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b534_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    pre-push : %s' % lw(read('b534_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b534_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'),
             ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula'), ('SIDE-kernel', 'D:/SIDE-kernel')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b534_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b534_census_closing.txt'), 'TOTAL MISSING'), lw(read('b534_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b534_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE KERNEL LANE IS SHUT.** The f4 attempt closes with h2_sign <-> rh_strip compiled and h2_sign -> RH compiled',
      '        from the seam Prop rh_strip_imp_rh; the seam (the left half-plane: zeros with re <= 0 are the trivial zeros) is ABSENT',
      '        from Mathlib by name and is not attempted (R144)(4).',
      '    (b) ### **THE UPDATE ACT IS NEXT (R144)(5)**: E-2026-09-25-1`s filing, the three (R110) rows, the ceiling`s wording, each in',
      '        the words this outcome allows; and the fold of b526-b534 (span nine).',
      '    (c) ### **THE CEILING SENTENCE, PRINTED UNCHANGED IN THE TRAIL**, now reads "h2_sign -> RH compiled to its last step" beside a',
      '        kernel that compiles h2_sign -> RH from the seam Prop; its next wording is the author`s.',
      '=' * 104]
io.open(os.path.join(D, 'b534_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
