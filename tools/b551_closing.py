# -*- coding: utf-8 -*-
"""b551_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b551_*` and `relay/tools/b551_*` file, the four PLACE-papers
### documents this act writes, and the patch and message of every commit of this act (subject beginning `b551`) in five
### repositories (the trial branch included), plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
FILES = [os.path.join(PP, f) for f in ('FINDINGS.md', 'OPEN_TRAILS.md', 'SPIRAL_MAP.md', 'phase2/method/THE_IDENTITY_CHAIN.md')]
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
        files = sorted(set(glob.glob(os.path.join(D, 'b551_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b551_*')) + FILES))
        files = [f for f in files if not f.endswith('b551_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo, rev in ((ROOT, 'HEAD'), (PP, 'HEAD'), (SIDE, 'HEAD'), (KER, 'HEAD'), (LV, 'toolchain-trial-b551')):
            for l in git(repo, 'log', '--pretty=%H %s', '-40', rev).split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b551'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b551_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b551_scores.json'))
TC = json.loads(read('b551_toolchains.json'))
IC = json.loads(read('b551_iface.json'))
TG = json.loads(read('b551_tag.json'))
RW = json.loads(read('b551_rows.json'))
SP = json.loads(read('b551_spiral.json'))
IDJ = json.loads(read('b551_idc.json'))
TR = json.loads(read('b551_trial.json'))
PR = json.loads(read('b551_price.json'))
FND = json.loads(read('b551_findings.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b551 -- THE CLOSING RECORD. ### **THE TOOLCHAINS, UNDER (R161).**', '=' * 104,
     '    the census : 45 repositories ; distinct Mathlib revs among non-VANILLA %d ; not building from cache %d (%s) ; runs %d, all guarded %s'
     % (TC['distinct'], len(TC['fails']), ', '.join(TC['fails']), TC['runs'], TC['guarded']),
     '    the Interfaces pin : the olean built (exit %s) ; %s'
     % (IC['build_exit'], ' ; '.join('%s exit %s, prints equal %s' % (f, v['exit'], v['equal']) for f, v in IC['files'].items())),
     '    the tag : SIDE-global-section v0.2.0 -> remote peeled %s ; remote main at read-back %s ; row %d (CORRESPONDENCE.md) ; SPIRAL_MAP :%s ; THE_IDENTITY_CHAIN :%s'
     % (TG['remote_peeled'][:12], TG['remote_main'][:12], RW['number'], SP['line'], IDJ['line']),
     '    the trial : toolchain-trial-b551 at %s ; exit %s ; errors %d in %d module(s) %s ; not attempted downstream %d of %d ; Mathlib modules compiled %d'
     % (TR['branch_tip'][:12], TR['exit'], TR['total'], len(TR['modules']), [m['file'] for m in TR['modules']], len(TR['downstream']), TR['lib_modules'], len(TR['mathlib_compiled'])),
     '    OPEN_TRAILS : the price :%s ; FINDINGS : the entry :%s ; next THE_KEYSTONE_CENSUS' % (PR['line'], FND['line']),
     '    the branches : %s' % ' ; '.join(l for l in read('b551_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '    (N6) read literally, its first clause ("main of every repository unchanged"): %s -- SIDE-global-section`s main moved by row 391, as (R161)(4) ordered.'
     % W(SC['n6_literal_first_clause']),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b551_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
     '    pre-push : %s' % lw(read('b551_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b551_checks_postpush.txt'), 'ARMS RUN :')]
for n in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-li-map', 'SIDE-fano-darkness'):
    p = ROOT if n == 'relay' else (PP if n == 'PLACE-papers' else os.path.join('D:', os.sep, n))
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
tb = git(LV, 'rev-parse', 'toolchain-trial-b551')
trem = (git(LV, 'ls-remote', 'origin', 'refs/heads/toolchain-trial-b551').split() or [''])[0]
L.append('      %-22s local %s ; remote %s ; %s (HELD, not merged)' % ('lv toolchain-trial-b551', tb[:12], trem[:12], 'AGREE' if tb == trem else 'DISAGREE'))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b551_census_closing.txt'), 'TOTAL MISSING'), lw(read('b551_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b551_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT**: THE_KEYSTONE_CENSUS.',
      '    (b) ### **FOR THE AUTHOR**: row 391`s grade cell makes tools/terminal_table.py read AggregationCircularityShadow.boolGrp as CONFLICT (defect (j)); a later row or a table exception is the author`s to choose.',
      '    (c) ### **FOR THE AUTHOR**: the alignment`s price is a floor -- GammaBounds.lean:177 fails at Mathlib 51e6992 and 11 of 25 modules downstream were not attempted; toolchain-trial-b551 is HELD.',
      '    (d) ### **FOR THE AUTHOR**: seven non-VANILLA repositories do not build from cache at HEAD, each on its own stale module(s); SIDE-explicit-formula and SIDE-lv-conservation among them.',
      '    (e) Under (R157)(6) the seat`s memory is not refreshed at this act.',
      '=' * 104]
io.open(os.path.join(D, 'b551_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
