# -*- coding: utf-8 -*-
"""b525_closing.py -- THE CLOSING RECORD. ### Figures READ from the banks, not retyped."""
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
SC = json.loads(read('b525_scores.json'))
FO = json.loads(read('b525_fold.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b525 -- THE CLOSING RECORD. ### **THE WITNESS ARC FOLDED, b517-b524, UNDER (R135).**', '=' * 104,
     '    span : b%d-b%d, %d acts ; the tool reads %d' % (FO['span']['lo'], FO['span']['hi'], FO['span']['acts'], FO['span']['tool_reads']),
     '    verdicts matched %d of %d ; rulings matched %d of %d ; defects %d ; columns %s'
     % (sum(q['found'] for q in FO['quotes']), len(FO['quotes']), sum(r['found'] for r in FO['rulings']), len(FO['rulings']),
        sum(d['n'] for d in FO['defects']), FO['columns']),
     '    writes : ' + ' ; '.join('%(file)s +%(added)d bytes, prefix %(prefix)s' % w for w in FO['writes']),
     '    (N1) %s (N2) %s (N3) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b525_defects.txt').rstrip(chr(10)).split(chr(10)) if l] + [
     '', '### THE COMMITS, THE MIRROR, THE CENSUSES.',
     '    post-push : %s' % lw(read('b525_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', 'D:/relay'), ('PLACE-papers', 'D:/MY-DOwnloads/PLACE-papers'), ('SIDE-global-section', 'D:/SIDE-global-section'), ('SIDE-explicit-formula', 'D:/SIDE-explicit-formula')):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-20s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    mirror : %s' % lw(read('b525_mirror.txt'), 'VERDICT:'),
      '    censuses : %s / %s' % (lw(read('b525_census_closing.txt'), 'TOTAL MISSING'), lw(read('b525_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b525_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT IS (R135)(3)(a)**: W-ORD-XI-P7 and the instance discrepancy, both objects on the kernel`s phi.',
      '    (b) ### **THEN (f)(ii) IN THE KERNEL** on the kernel`s instance; f3 and f4 after it.',
      '    (c) ### **THE FOLD`S ONE STATEMENT LACKS THE INSTANCE SENTENCE** (defect (a)), routed for the navigator.',
      '=' * 104]
io.open(os.path.join(D, 'b525_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
