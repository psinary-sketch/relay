# -*- coding: utf-8 -*-
"""b513_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
P = json.loads(read('b513_profile.json'))
TB = json.loads(read('b513_table.json'))
SC = json.loads(read('b513_scores.json'))
DF = json.loads(read('terminal_table_diff.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b513 -- THE CLOSING RECORD. ### **RH -> h2_sign COMPILED, UNDER (R122).**', '=' * 104,
     '    ' + ' ; '.join(P.get('lines') or ['NO PROFILE']),
     '    attempts %s, the first to succeed %s ; the proof %s lines' % (SC['attempts'], SC['first_ok'], SC['proof_lines']),
     '    the converse`s needs ABSENT : %s' % ', '.join('(%s) %s' % (n['key'], n['what']) for n in TB['needs'] if not n['found']),
     '    the terminal table, regenerated post-push : rows added %d %s' % (len(DF.get('added') or []), [a[1] for a in DF.get('added') or []]),
     '    (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS -- THREE (the desk).'] + [l for l in read('b513_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b513_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b513_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b513_census_closing.txt'), 'TOTAL MISSING'), lw(read('b513_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b513_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE KERNEL LANE IS SHUT.** ### RH -> h2_sign and RH -> cell form are compiled; h2_sign -> RH is a Prop, its (d) and (f) ABSENT.',
      '    (b) ### **THE NUMERICAL LANE OPENS FOR b514, THE MATCHED WINDOW** (R122)(1); by (R122)(2) it is the converse`s construction attempted at Q0`s pair.',
      '    (c) ### **THE TABLE`S PROFILE COLUMN READS NOT PROFILED FOR THE THREE LINKS**: it takes profiles from captured stdout only, and an',
      '        `AxiomCheck*.lean` gives presence; the profiles are banked in `b513_profile.json`. The two short-name rows are ledger rows the table',
      '        makes for any backticked name that resolves in a kernel -- carried as observed, the tool unedited.',
      '=' * 104]
io.open(os.path.join(D, 'b513_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
