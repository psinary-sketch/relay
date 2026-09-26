# -*- coding: utf-8 -*-
"""b547_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b547_*` and `relay/tools/b547_*` file, the four PLACE-papers
### documents this act writes, and the patch and message of every commit of this act (subject beginning `b547`) in four
### repositories, plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
FILES = [os.path.join(PP, f) for f in ('FINDINGS.md', 'OPEN_TRAILS.md', 'FACES_LEDGER.md', 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE.md')]
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
        files = sorted(set(glob.glob(os.path.join(D, 'b547_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b547_*')) + FILES))
        files = [f for f in files if not f.endswith('b547_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b547'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b547_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b547_scores.json'))
FJ = json.loads(read('b547_faces.json'))
CT = json.loads(read('b547_census_table.json'))
CRJ = json.loads(read('b547_credit.json'))
LJ = json.loads(read('b547_ledger.json'))
BJ = json.loads(read('b547_banks.json'))
FDJ = json.loads(read('b547_field.json'))
FND = json.loads(read('b547_findings.json'))
WJ = json.loads(read('b547_window.json'))
W = lambda v: 'HELD' if v else 'REFUTED'
L = ['=' * 104, 'b547 -- THE CLOSING RECORD. ### **THE CASCADE, ACT FOUR: FACES_OF_H2 AND FACES_LEDGER TIERED, UNDER (R157).**', '=' * 104,
     '    FACES_OF_H2 (Tier N, kept) : tier block :%d ; tiers %s ; CARRIED %d ; the h1 pin row ; census table %s'
     % (FJ['write']['heading_line'], FND['faces_tiers'], FND['carried'], FND['census']),
     '    the credit : FINDINGS.md:%d' % CRJ['heading_line'],
     '    FACES_LEDGER : %s -- %s ; tiers %s ; R-pair lines %d' % (LJ['status'], LJ['detail'], FND['ledger_tiers'], len(LJ['rpair_lines'])),
     '    the cited banks : %d checked, missing %s' % (len(BJ['rows']), BJ['missing'] or 'none'),
     '    the field : FINDINGS.md:%d ; Liu record found %s (NAVIGATOR-READ) ; nothing at Zenodo read' % (FDJ['heading_line'], FDJ['liu_found']),
     '    the checkout : %s' % WJ['counts'],
     '    the act : FINDINGS.md:%d ; next THE_RESIDUE_OF_RH' % FND['write']['heading_line'],
     '    the branches : %s' % ' ; '.join(l for l in read('b547_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b547_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
     '    pre-push : %s' % lw(read('b547_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b547_checks_postpush.txt'), 'ARMS RUN :')]
for n in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-li-map', 'SIDE-fano-darkness'):
    p = ROOT if n == 'relay' else (PP if n == 'PLACE-papers' else os.path.join('D:', os.sep, n))
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b547_census_closing.txt'), 'TOTAL MISSING'), lw(read('b547_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b547_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT**: THE_RESIDUE_OF_RH (CP-1), then the remaining tables, then CP-1b.',
      '    (b) ### **FOR THE AUTHOR**: the search found no Liu record by the ruling`s title; the nearest is Zhu, arXiv:2608.24827',
      '        (certified two-sided bounds in compact windows) -- the author`s word on whether that is the paper read.',
      '    (c) ### **FOR THE AUTHOR**: the two Zenodo records lack a title (de Bastos) and an author and date (the other) in the ruling.',
      '    (d) Under (R157)(6) the seat`s memory is not refreshed at this act.',
      '=' * 104]
io.open(os.path.join(D, 'b547_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
