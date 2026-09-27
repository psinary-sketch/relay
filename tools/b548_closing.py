# -*- coding: utf-8 -*-
"""b548_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b548_*` and `relay/tools/b548_*` file, the four PLACE-papers
### documents this act writes, and the patch and message of every commit of this act (subject beginning `b548`) in four
### repositories, plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
FILES = [os.path.join(PP, f) for f in ('FINDINGS.md', 'OPEN_TRAILS.md')]
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
        files = sorted(set(glob.glob(os.path.join(D, 'b548_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b548_*')) + FILES))
        files = [f for f in files if not f.endswith('b548_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b548'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b548_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b548_scores.json'))
IJ = json.loads(read('b548_interference.json'))
SJ = json.loads(read('b548_sweep.json'))
FDJ = json.loads(read('b548_field.json'))
FND = json.loads(read('b548_findings.json'))
W = lambda v: 'HELD' if v else 'REFUTED'
H2 = SJ['H2']
L = ['=' * 104, 'b548 -- THE CLOSING RECORD. ### **THE BENCH AT Q0 AND XI, UNDER (R158); GRADED READING.**', '=' * 104,
     '    Component 1 : match against b522 at 30-45 %s ; k* %s ; H1 %s' % (IJ['all_match'], IJ['kstar'], IJ['H1']),
     '    Component 2 : cells Q0 %d xi %d ; smallest negative width at Q0 %s ; H2 x1 %s x2 %s q1 %s q2 %s ref3 %s'
     % (sum(v['n'] for v in SJ['q'].values()), sum(v['n'] for v in SJ['xi'].values()), H2['smallest_negative'], H2['x1'], H2['x2'], H2['q1'], H2['q2'], H2['ref3']),
     '    xi statuses : %s' % {k: v['status'] for k, v in SJ['xi'].items()},
     '    the field sources : FINDINGS.md:%d ; the act : FINDINGS.md:%d ; the pointer from :5529 at FINDINGS.md:%d ; next THE_RESIDUE_OF_RH'
     % (FDJ['heading_line'], FND['write']['heading_line'], FND['pointer']['line']),
     '    the branches : %s' % ' ; '.join(l for l in read('b548_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b548_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
     '    pre-push : %s' % lw(read('b548_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b548_checks_postpush.txt'), 'ARMS RUN :')]
for n in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-li-map', 'SIDE-fano-darkness'):
    p = ROOT if n == 'relay' else (PP if n == 'PLACE-papers' else os.path.join('D:', os.sep, n))
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b548_census_closing.txt'), 'TOTAL MISSING'), lw(read('b548_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b548_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT**: THE_RESIDUE_OF_RH (CP-1), then the remaining tables, then CP-1b.',
      '    (b) ### **FOR THE AUTHOR**: xi at order 3 does not verify on this instrument (|r| > B by up to 1.17; defect (c)).',
      '    (c) ### **FOR THE AUTHOR**: relay data/b546_scores.json carries an uncommitted change found at this act (defect (f)).',
      '    (d) Under (R157)(6) the seat`s memory is not refreshed at this act.',
      '=' * 104]
io.open(os.path.join(D, 'b548_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
