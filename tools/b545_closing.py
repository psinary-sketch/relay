# -*- coding: utf-8 -*-
"""b545_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b545_*` and `relay/tools/b545_*` file, the four PLACE-papers
### documents this act writes, and the patch and message of every commit of this act (subject beginning `b545`) in four
### repositories, plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
FILES = [os.path.join(PP, f) for f in ('phase1.5/spectral/BALANCE_AND_POSITIVITY.md', 'FINDINGS.md', 'OPEN_TRAILS.md',
                                       'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md')]
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
        files = sorted(set(glob.glob(os.path.join(D, 'b545_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b545_*')) + FILES))
        files = [f for f in files if not f.endswith('b545_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b545'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b545_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b545_scores.json'))
TJ = json.loads(read('b545_tiers.json'))
SJ = json.loads(read('b545_sentences.json'))
FH = json.loads(read('b545_fano_hits.json'))
PRB = json.loads(read('b545_probes.json'))
CJ = json.loads(read('b545_credit.json'))
FJ = json.loads(read('b545_findings.json'))
WT, WS, WJ = (json.loads(read(n)) for n in ('b545_write_tiers.json', 'b545_write_sentences.json', 'b545_write_joint.json'))
W = lambda v: 'HELD' if v else 'REFUTED'
L = ['=' * 104, 'b545 -- THE CLOSING RECORD. ### **THE CASCADE, ACT THREE: BALANCE_AND_POSITIVITY TIERED, UNDER (R155).**', '=' * 104,
     '    the table : B.5 (BALANCE_AND_POSITIVITY.md:339-348) ; tier block at :%d ; rows %s ; terminals %s ; %s'
     % (WT['heading_line'], TJ['counts']['rows'], TJ['counts']['terminals'], TJ['counts']['carried']),
     '    the sentences : %d segments (%d numerals) ; %d selected ; %d rows %s ; supplementary %s ; %d rectifications at :%d ; no erratum'
     % (SJ['read'], SJ['numerals'], SJ['selected'], SJ['rows'], SJ['counts'], SJ['counts_supp'], SJ['rectifications'], WS['heading_line']),
     '    the joint in two forms : :%d ; RH-anchor tier references %d (§I :41, h2_sign_iff_rh)' % (WJ['heading_line'], SJ['anchor_tier_refs']),
     '    the credit : FINDINGS.md:%d ; SURR line :%d' % (CJ['findings']['heading_line'], CJ['surr_line']),
     '    the Fano theorem : COMPILED %s -- SIDE-fano-darkness %s ; second_moment %s ; %d repositories, %d revisions, %d files, %d hits'
     % (TJ['fano_compiled'], PRB['SIDE-fano-darkness']['full'][:10], PRB['SIDE-fano-darkness']['profiles']['FanoTwoDarkness.second_moment'],
        len(FH['repos']), FH['revisions'], FH['files'], len(FH['hits'])),
     '    the li-map probe : lam_add %s' % PRB['SIDE-li-map']['profiles']['LiLinearMap.lam_add'],
     '    FINDINGS : the act at :%d' % FJ['heading_line'],
     '    the branches : %s' % ' ; '.join(l for l in read('b545_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b545_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
     '    pre-push : %s' % lw(read('b545_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b545_checks_postpush.txt'), 'ARMS RUN :')]
for n in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-li-map', 'SIDE-fano-darkness'):
    p = ROOT if n == 'relay' else (PP if n == 'PLACE-papers' else os.path.join('D:', os.sep, n))
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'origin/main').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b545_census_closing.txt'), 'TOTAL MISSING'), lw(read('b545_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b545_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT**: CP-1 in the order of (R154)(3) -- FACES_OF_H2_AT_FINITE_INSTANCE with FACES_LEDGER.',
      '    (b) ### **FOR THE AUTHOR**: READING (6)`s flag -- read literally, :357`s "RH-strength on the half-plane where T1 holds" is C₂ at',
      '        Φ (proved); the clause that anticipated b538 is :274`s continuation clause. The ruling`s STANDS is entered; no grade moved.',
      '    (c) ### **FOR THE AUTHOR**: eight SIDE-* repositories on D:\\ stand outside b542`s enumeration (SIDE-fano-darkness among them),',
      '        so CP-2`s T0 inventory did not count them.',
      '    (d) ### **FOR THE AUTHOR**: W-ORD-MARGIN-BRIDGE is the trail W-ORD-LI-WEIL-BRIDGE under a second ID.',
      '=' * 104]
io.open(os.path.join(D, 'b545_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
