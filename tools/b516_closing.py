# -*- coding: utf-8 -*-
"""b516_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
FO = json.loads(read('b516_fold.json'))
SC = json.loads(read('b516_scores.json'))
TD = json.loads(read('b516_table_diff_vs_b515.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b516 -- THE CLOSING RECORD. ### **THE FOLD AT SPAN EIGHT, b508 THROUGH b515, UNDER (R125).**', '=' * 104,
     '    fold : %s ; columns %s ; verdict strings %d matched %d ; defects %d ; rulings %d'
     % (FO['heading'], FO['columns'], len(FO['quotes']), sum(q['found'] for q in FO['quotes']), sum(d['n'] for d in FO['defects']), len(FO['rulings'])),
     '    writes : ' + ' ; '.join('%(file)s +%(added)d prefix %(prefix)s removed %(removed)d' % w for w in FO['writes']),
     '    table against b515`s close : added %d ; gone %d ; profile changed %d' % (len(TD['added']), len(TD['gone']), len(TD['changed'])),
     '    (N1) %s (N2) %s (N3) %s (N4) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS -- THREE (the desk).'] + [l for l in read('b516_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b516_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b516_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b516_census_closing.txt'), 'TOTAL MISSING'), lw(read('b516_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b516_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE INSTRUMENT LANE IS SHUT; THE KERNEL LANE REOPENS FOR (d)**, the growth bound, one lemma (R125)(4).',
      '    (b) ### **W-ORD-WEIL-CONVERSE`S (f) IS PRICED AT WEEKS**; classK admits the real-valued variant the construction needs.',
      '    (c) ### **terminal_table.py`S THREE PRE-EXISTING ESCAPE WARNINGS ARE ROUTED**, and the suite`s regeneration overwrites the',
      '        fold-time diff at every close -- the comparison against b515`s close is banked as b516_table_diff_vs_b515.json.',
      '=' * 104]
io.open(os.path.join(D, 'b516_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
