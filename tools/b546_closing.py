# -*- coding: utf-8 -*-
"""b546_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b546_*` and `relay/tools/b546_*` file, the four PLACE-papers
### documents this act writes, and the patch and message of every commit of this act (subject beginning `b546`) in four
### repositories, plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
FILES = [os.path.join(PP, f) for f in ('FINDINGS.md', 'OPEN_TRAILS.md', 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md', 'SPIRAL_MAP.md')]
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(p):
    return io.open(os.path.join(D, p), encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def lw(t, n):
    return next((l.strip() for l in t.split(NL) if n in l), '')


def git(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def git_bytes(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True).stdout


def tokenscan():
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    if not t:
        res = dict(set=False)
    else:
        files = sorted(set(glob.glob(os.path.join(D, 'b546_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b546_*')) + FILES))
        files = [f for f in files if not f.endswith('b546_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b546'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b546_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b546_scores.json'))
EJ = json.loads(read('b546_eight.json'))
AM = json.loads(read('b546_amend.json'))
SP = json.loads(read('b546_spiral.json'))
FP = json.loads(read('b546_forms_probe.json'))
MJ = json.loads(read('b546_mathlib.json'))
FO = json.loads(read('b546_forms.json'))
CR = json.loads(read('b546_credit.json'))
GE = json.loads(read('b546_geometry.json'))
W = lambda v: 'HELD' if v else 'REFUTED'
L = ['=' * 104, 'b546 -- THE CLOSING RECORD. ### **CP-2 EXTENDED; THE TWO FORMS; THE CREDIT; THE GEOMETRIES, UNDER (R156).**', '=' * 104,
     '    the eight : %d declarations, subjects %s ; union %d ; old subjects both ways %s / %s ; moved %d'
     % (EJ['count_eight'], EJ['subjects_eight'], EJ['count_union'], EJ['subjects_old_b544'], EJ['subjects_old_union'], len(EJ['moved'])),
     '    CP-2 amended at FINDINGS.md:%d ; CP-3 at :%d ; totals now %s ; SPIRAL_MAP rows %d at :%d'
     % (AM['cp2']['heading_line'], AM['cp3']['heading_line'], AM['new_totals'], SP['rows'], SP['heading_line']),
     '    the probes : ' + ' ; '.join('%s %s (%s s, exit %s)' % (r, {k.split('.')[-1]: v.replace('depends on axioms: ', '') for k, v in FP[r]['profiles'].items()}, FP[r].get('seconds'), FP[r]['exit'])
                                    for r in ('SIDE-li-map', 'SIDE-explicit-formula', 'SIDE-lv-conservation')),
     '    Mathlib %s : %s' % (MJ['head'][:12], {k: MJ['counts'][k] for k in ('Li coefficient (an identifier)', 'Keiper', 'Taylor coefficients of zeta', 'xi / riemannXi')}),
     '    the two forms : FINDINGS.md:%d ; the credit line :%d, BALPOS :%d ; the geometries :%d (2T² %.2f and %.1f ; narrowest %s)'
     % (FO['heading_line'], CR['after']['find_line'], CR['after']['bal_line'], GE['write']['heading_line'], GE['n0'], GE['ntop'], GE['narrowest']),
     '    Component 5 : held at the seal ; released on the author`s word (data/b546_author_word.txt) ; the line is in the trail',
     '    the branches : %s' % ' ; '.join(l for l in read('b546_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b546_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
     '    pre-push : %s' % lw(read('b546_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b546_checks_postpush.txt'), 'ARMS RUN :')]
for n in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-li-map', 'SIDE-fano-darkness'):
    p = ROOT if n == 'relay' else (PP if n == 'PLACE-papers' else os.path.join('D:', os.sep, n))
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b546_census_closing.txt'), 'TOTAL MISSING'), lw(read('b546_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b546_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT**: FACES_OF_H2_AT_FINITE_INSTANCE with FACES_LEDGER ((R156)(6)).',
      '    (b) ### **FOR THE AUTHOR**: a Lean probe past 600 s cannot finish in one foreground tool call; the harness moves it to the',
      '        background. This act watched each from the foreground until it printed (defect (c)).',
      '    (c) W-ORD-LI-WEIL-BRIDGE is priced at FINDINGS.md:%d; its trigger stays the author`s word.' % FO['heading_line'],
      '=' * 104]
io.open(os.path.join(D, 'b546_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
