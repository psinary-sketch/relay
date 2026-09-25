# -*- coding: utf-8 -*-
"""b517_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
P = json.loads(read('b517_profile.json'))
SC = json.loads(read('b517_scores.json'))
RD = json.loads(read('b517_read.json'))
TT = json.loads(read('terminal_table.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
rows = [r for r in TT['rows'] if r['name'] in ('SIDEExplicitFormula.B321.paperFT_growth', 'SIDEExplicitFormula.B321.paperFT_growth_at')]
s3 = len(rows) == 2 and all(r['profile_state'] == 'PROFILED' and r['grade'] == 'DERIVES' for r in rows)
L = ['=' * 104, 'b517 -- THE CLOSING RECORD. ### **(d), THE GROWTH BOUND, COMPILED, UNDER (R126).**', '=' * 104,
     '    ' + ' ; '.join(P.get('lines') or ['NO PROFILE']),
     '    attempts %s, the first to succeed %s ; paperFT_growth %s lines ; vendored lemmas %s ; definitions %s'
     % (SC['attempts'], SC['first_ok'], SC['proof_lines'], RD.get('lemma_refs') or 'NONE', RD.get('def_refs')),
     '    the table post-push : ' + ' ; '.join('%s %s %s via %s' % (r['name'].split('.')[-1], r['grade'], r['profile_state'], r.get('profile_source')) for r in rows),
     '    (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s, read post-push' % (tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 's1', 's2')) + (W(s3),)),
     '', '### THIS ACT`S OWN DEFECTS -- THREE (the desk).'] + [l for l in read('b517_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b517_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b517_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b517_census_closing.txt'), 'TOTAL MISSING'), lw(read('b517_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b517_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE KERNEL LANE IS SHUT; THE NUMERICAL LANE REOPENS FOR THE TWO-PROPERTY WINDOW** (R126)(1),(3): the zero factor',
      '        applied to the cosine window, real, the numerical candidate for (f)(i).',
      '    (b) ### **(d) IS COMPILED; (f) STAYS PRICED AT WEEKS**, its four lemmas as b516 lists them.',
      '    (c) ### **THE WEEK`S HONEST SUMMARY, (R126)(2)**: the programme built and corrected instruments; it did not move a statement about zeta.',
      '=' * 104]
io.open(os.path.join(D, 'b517_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
