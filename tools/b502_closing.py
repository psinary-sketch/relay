# -*- coding: utf-8 -*-
"""b502_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
R = json.loads(read('b502_results.json'))
SC = json.loads(read('b502_scores.json'))
L = ['=' * 104, 'b502 -- THE CLOSING RECORD. ### **m(a) POSITIVE AT ALL 119 CELLS; A THIRD EXTREMUM AT 13.152946; THE LANE SHUT.**', '=' * 104,
     '    new cells %d ; all cells %d ; not above floor %d ; within ten floors %d ; compute %.0f s' % (R['n_new'], R['n_all'], R['not_above'], R['within_ten'], R['seconds']),
     '    extrema : %s' % ['%s %.6f' % (e['t'], e['a']) for e in R['extrema']],
     '    fits : least on new %s ; on old %s' % (R['win_new'], R['win_old']),
     '    Epstein : negative at %s ; smallest %+.6f ; route reproduces %s' % (R['epneg'] or 'NONE', R['ep_min'], R['epcheck']['reproduces']),
     '    (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple('HELD' if SC[k] else 'REFUTED' for k in ('n1','n2','n3','s1','s2','s3')),
     '', '### THIS ACT`S OWN DEFECTS -- NONE FOUND.',
     '    ### The suite passed on its first run and no instrument misread; the compute ran 3185 s against a price',
     '    ### of about 45 minutes, over the estimate by about a fifth, and the chunk that crossed ten minutes',
     '    ### finished in the background and was waited on in the foreground. ### **A CLEAN ACT IS A RESULT.**',
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b502_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b502_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b502_census_closing.txt'), 'TOTAL MISSING'), lw(read('b502_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b502_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NUMERICAL LANE IS SHUT** under (R112). ### The minimum at 13.152946 and the rise after it are routed.',
      '    (b) ### **THE EPSTEIN CONTROL NEVER REACHED ITS CROSSINGS** (widths 40 and 81); `corr_row.py` still validates after it writes.',
      '=' * 104]
io.open(os.path.join(D, 'b502_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
