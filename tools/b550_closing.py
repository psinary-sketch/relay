# -*- coding: utf-8 -*-
"""b550_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b550_*` and `relay/tools/b550_*` file, the four PLACE-papers
### documents this act writes, and the patch and message of every commit of this act (subject beginning `b550`) in four
### repositories, plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
FILES = [os.path.join(PP, f) for f in ('FINDINGS.md', 'OPEN_TRAILS.md', 'phase1.5/proofs/THE_RESIDUE_OF_RH.md', 'phase2/method/THE_IDENTITY_CHAIN.md')]
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
        files = sorted(set(glob.glob(os.path.join(D, 'b550_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b550_*')) + FILES))
        files = [f for f in files if not f.endswith('b550_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b550'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b550_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b550_scores.json'))
TJ = json.loads(read('b550_tiers.json'))
TG = json.loads(read('b550_tag.json'))
FND = json.loads(read('b550_findings.json'))
IB = json.loads(read('b550_identity_block.json'))
TR = json.loads(read('b550_trails.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b550 -- THE CLOSING RECORD. ### **THE CASCADE, ACT SIX: THE_IDENTITY_CHAIN TIERED, UNDER (R160).**', '=' * 104,
     '    THE_IDENTITY_CHAIN : %d terminals ; tiers %s ; grades %s ; dispositions %s ; the block at :%d'
     % (len(TJ['rows']), TJ['tier_counts'], TJ['grade_counts'], TJ['disp_counts'], IB['heading_line']),
     '    AllPrints equal to its bank : %s ; named terminals absent from v0.1.0 : %d' % (TJ['allprints_equal'], len(TJ['not_in_tag'])),
     '    the tag : SIDE-lv-conservation v0.11.0 -> remote peeled %s ; remote main %s' % (TG['remote_peeled'][:12], TG['remote_main'][:12]),
     '    FINDINGS : the reading :%d ; the act :%d ; OPEN_TRAILS : W-ORD-POWER-SWEEP :%d ; the bridge :%d ; next THE_KEYSTONE_CENSUS'
     % (FND['reading_line'], FND['act_line'], TR['power_line'], TR['bridge_line']),
     '    the branches : %s' % ' ; '.join(l for l in read('b550_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b550_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
     '    pre-push : %s' % lw(read('b550_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b550_checks_postpush.txt'), 'ARMS RUN :')]
for n in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-li-map', 'SIDE-fano-darkness'):
    p = ROOT if n == 'relay' else (PP if n == 'PLACE-papers' else os.path.join('D:', os.sep, n))
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b550_census_closing.txt'), 'TOTAL MISSING'), lw(read('b550_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b550_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT**: THE_KEYSTONE_CENSUS.',
      '    (b) ### **FOR THE AUTHOR**: SIDE-global-section has one tag, v0.1.0, and SPIRAL_MAP cites no pin of it; 17 of 26 named terminals postdate the tag.',
      '    (c) ### **FOR THE AUTHOR**: the declared Interfaces pin`s checkout (D:/mathlib4 cecd0c4) cannot elaborate RestrictedTensorLayer1 (one olean missing).',
      '    (d) Under (R157)(6) the seat`s memory is not refreshed at this act.',
      '=' * 104]
io.open(os.path.join(D, 'b550_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
