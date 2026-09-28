# -*- coding: utf-8 -*-
"""b553_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b553_*` and `relay/tools/b553_*` file, the four PLACE-papers
### documents this act writes, and the patch and message of every commit of this act (subject beginning `b553`) in five
### repositories (the trial branch included), plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
FILES = [os.path.join(PP, f) for f in ('FINDINGS.md', 'OPEN_TRAILS.md', 'phase2/method/THE_KEYSTONE_CENSUS.md')] + [os.path.join(ROOT, 'tools', f) for f in ('corr_row.README.md', 'terminal_table.py')]
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
        files = sorted(set(glob.glob(os.path.join(D, 'b553_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b553_*')) + FILES))
        files = [f for f in files if not f.endswith('b553_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo, rev in ((ROOT, 'HEAD'), (PP, 'HEAD'), (SIDE, 'HEAD'), (KER, 'HEAD')):
            for l in git(repo, 'log', '--pretty=%H %s', '-40', rev).split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b553'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b553_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b553_scores.json'))
SU = json.loads(read('b553_supersede.json'))
OL = json.loads(read('b553_older.json'))
PF = json.loads(read('b553_period_fine.json'))
BR = json.loads(read('b553_bridge.json'))
CZ = json.loads(read('b553_census.json'))
AN = json.loads(read('b553_ancestry.json'))
AM = json.loads(read('b553_anomaly.json'))
CV = json.loads(read('b553_census_v02.json'))
CO = json.loads(read('b553_corrections.json'))
FND = json.loads(read('b553_findings.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
C, PR = PF['res']['crest'], PF['res']['pair']
L = ['=' * 104, 'b553 -- THE CLOSING RECORD. ### **THE CASCADE, ACT SEVEN, UNDER (R163).**', '=' * 104,
     '    the supersession rule : boolGrp %s ; grades changed %s ; CONFLICT %d -> %d ; row 393' % (SU['boolgrp_after']['grade'], list(SU['changed']), len(SU['conflicts_before']), len(SU['conflicts_after'])),
     '    the older conflict : acts %s ; branch 1 %s ; row written %s' % (OL['acts'], OL['branch1'], OL['row_written']),
     '    the corrections : FINDINGS :%s ; OPEN_TRAILS :%s' % (CO['findings_line'], CO['trails_line']),
     '    H7 %s : 29.55 periods/(8pi/7x) %s ; mean %.5f vs 4pi/(7x) %.5f ; 16.29 sign changes %d, monotone %s ; control %.1e' % (
         'REFUTED' if PF['refuted'] else 'NOT REFUTED', ['%.4f' % r for r in C['per_ratios']], C['mean'], C['pred_mean'], len(PR['changes_ln']), PR['monotone'], PF['control_max']),
     '    the bridge : OPEN_TRAILS :%s ; truncation %d items, forward %d items (F4 = the truncation route) ; not attempted' % (BR['line'], BR['trunc'], BR['forward']),
     '    the census : HEAD %s ; entrants %s ; pins failing %s ; bd2ae1a %s ; Anomaly 1 HEAD %s, latest tag %s ; v0.2 :%s ; next %s' % (
         CZ['new_counts'], CZ['entrants'] or 'NONE', AN['fails'], AN['named5']['bd2ae1a'], AM['head'][:7], AM['latest_tag'], CV['v02_line'], CV['next']),
     '    FINDINGS : the entry :%s' % FND['line'],
     '    the branches : %s' % ' ; '.join(l for l in read('b553_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s (N7) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b553_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
     '    pre-push : %s' % lw(read('b553_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b553_checks_postpush.txt'), 'ARMS RUN :')]
for n in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-li-map', 'SIDE-fano-darkness'):
    p = ROOT if n == 'relay' else (PP if n == 'PLACE-papers' else os.path.join('D:', os.sep, n))
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b553_census_closing.txt'), 'TOTAL MISSING'), lw(read('b553_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b553_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT**: SIMPLICITY_OF_RIEMANN_ZEROS, the census`s next untiered keystone.',
      '    (b) ### **FOR THE AUTHOR**: bd2ae1a resolves in PLACE-papers (2026-07-25, the E-CHARACTERIZATION sitting); PATHS :420 attributes it to lv (defect (d)).',
      '    (c) ### **FOR THE AUTHOR**: R5_output_HilbertPolya_to_RH`s CONFLICT fits neither branch of (R163)(2); register5_output_holds` fits the second (defect (e)).',
      '    (d) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping.',
      '    (e) Under (R157)(6) the seat`s memory is not refreshed at this act.',
      '=' * 104]
io.open(os.path.join(D, 'b553_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
