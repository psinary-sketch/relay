# -*- coding: utf-8 -*-
"""b549_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b549_*` and `relay/tools/b549_*` file, the four PLACE-papers
### documents this act writes, and the patch and message of every commit of this act (subject beginning `b549`) in four
### repositories, plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
FILES = [os.path.join(PP, f) for f in ('FINDINGS.md', 'OPEN_TRAILS.md', 'phase1.5/proofs/THE_RESIDUE_OF_RH.md')]
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
        files = sorted(set(glob.glob(os.path.join(D, 'b549_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b549_*')) + FILES))
        files = [f for f in files if not f.endswith('b549_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b549'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b549_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b549_scores.json'))
TJ = json.loads(read('b549_tiers.json'))
BJ = json.loads(read('b549_budget.json'))
FJ = json.loads(read('b549_family.json'))
FND = json.loads(read('b549_findings.json'))
RR = json.loads(read('b549_residue_rows.json'))
W = lambda v: 'HELD' if v else 'REFUTED'
L = ['=' * 104, 'b549 -- THE CLOSING RECORD. ### **THE CASCADE, ACT FIVE: THE_RESIDUE_OF_RH TIERED, UNDER (R159).**', '=' * 104,
     '    the residue : %d terminals ; rows %s ; tiers %s ; the block at THE_RESIDUE_OF_RH.md:%d'
     % (len(TJ['terminals']), TJ['disp_counts'], TJ['tier_counts'], RR['heading_line']),
     '    the trees : on main %d ; at the tip %d ; in the tag v0.10.0 %d'
     % (sum(t['main'] for t in TJ['terminals']), sum(t['tip'] for t in TJ['terminals']), sum(t['tag'] for t in TJ['terminals'])),
     '    the budget : xi order 3 VERIFY %d of %d ; Q0 order 3 changed %s' % (BJ['xi']['verified'], BJ['xi']['n'], BJ['q_changed'] or 'NONE'),
     '    the family : self-convolution %s ; H3 %s ; the sweep priced at %.0f s of cells' % (FJ['self_convolution'], FJ['h3'], FJ['cost_total']['q'] + FJ['cost_total']['xi']),
     '    FINDINGS : (R159)(1) :%s ; (R159)(2) :%s ; the act :%d ; next THE_IDENTITY_CHAIN' % (FND['r1_line'][0], FND['r2_line'][0], FND['act']['heading_line']),
     '    the stray : %s' % SC['housekeeping'][:120],
     '    the branches : %s' % ' ; '.join(l for l in read('b549_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s (N7) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b549_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
     '    pre-push : %s' % lw(read('b549_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b549_checks_postpush.txt'), 'ARMS RUN :')]
for n in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-li-map', 'SIDE-fano-darkness'):
    p = ROOT if n == 'relay' else (PP if n == 'PLACE-papers' else os.path.join('D:', os.sep, n))
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b549_census_closing.txt'), 'TOTAL MISSING'), lw(read('b549_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b549_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT**: THE_IDENTITY_CHAIN (CP-1), then the remaining tables, then CP-1b.',
      '    (b) ### **FOR THE AUTHOR**: the order names v0.10.0; the residue`s terminals are on main and in no tree of the tag (defect (f)).',
      '    (c) ### **FOR THE AUTHOR**: the re-parametrized sweep is priced, not filed; the route`s family needs its own window class.',
      '    (d) Under (R157)(6) the seat`s memory is not refreshed at this act.',
      '=' * 104]
io.open(os.path.join(D, 'b549_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
