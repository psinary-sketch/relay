# -*- coding: utf-8 -*-
"""b554_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b554_*` and `relay/tools/b554_*` file, the seven PLACE-papers
### documents this act writes and the two relay files it edits, and the patch and message of every commit of this act (subject
### beginning `b554`) in four repositories, plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, math, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-kernel')
FILES = [os.path.join(PP, f) for f in ('ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md', 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md',
                                        'phase1.5/proofs/THE_RESIDUE_OF_RH.md', 'phase2/method/THE_KEYSTONE_CENSUS.md',
                                        'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md')] + [
    os.path.join(ROOT, 'tools', f) for f in ('corr_row.README.md', 'terminal_table.py')]
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
        files = sorted(set(glob.glob(os.path.join(D, 'b554_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b554_*')) + FILES))
        files = [f for f in files if not f.endswith('b554_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40', 'HEAD').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b554'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b554_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b554_scores.json'))
BD = json.loads(read('b554_bd2.json'))
ER = json.loads(read('b554_erratum.json'))
SY = json.loads(read('b554_synonym.json'))
TS = json.loads(read('b554_trailsup.json'))
BF = json.loads(read('b554_table_before.json'))
R1 = json.loads(read('b554_reading_one.json'))
SP = json.loads(read('b554_sign_pattern.json'))
PRC = json.loads(read('b554_prices.json'))
ST = json.loads(read('b554_simp_tiers.json'))
SB = json.loads(read('b554_simp_block.json'))
SR = json.loads(read('b554_simp_reading.json'))
SM = json.loads(read('b554_stems.json'))
FND = json.loads(read('b554_findings.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
ORDER = ['T0', 'T1-open', 'T1-lit', 'T2', 'T3', 'T4']
L = ['=' * 104, 'b554 -- THE CLOSING RECORD. ### **THE CASCADE, ACT EIGHT, UNDER (R164).**', '=' * 104,
     '    bd2ae1a : %s %s ; "%s" ; E-2026-09-27-1 at ERRATA :%s ; lines PATHS :%s, RESIDUE :%s, CENSUS :%s' % (
         BD['hash'][:12], BD['date'], BD['subject'].split(':')[0], ER['erratum']['line'], ER['lines']['PATHS_TO_THE_CRITICAL_LINE.md']['line'],
         ER['lines']['THE_RESIDUE_OF_RH.md']['line'], ER['lines']['THE_KEYSTONE_CENSUS.md']['line']),
     '    the conflicts : CONFLICT %d -> %d (synonym map) -> %d (trail line) ; moved %s then %s' % (
         len(BF['conflicts']), len(SY['conflicts_after']), len(TS['conflicts_after']), list(SY['changed']), list(TS['changed'])),
     '    Reading One closed : FINDINGS :%s' % R1['line'],
     '    H8 %s : positive intervals %s ; floor at most %.3f ; controls %s' % (
         'REFUTED' if SP['refuted'] else 'NOT REFUTED', ['a %.4f-%.4f' % (math.exp(a), math.exp(b)) for a, b in SP['pos']],
         max(f['floor'] for f in SP['floor']), SP['controls']),
     '    the prices : detection OPEN_TRAILS :%s (the cheaper: %s) ; hazard :%s ; Anomaly 1 :%s' % (
         PRC['detection']['line'], PRC['cheaper'], PRC['hazard']['line'], PRC['anomaly']['line']),
     '    SIMPLICITY : %d rows ; tiers %s ; rows %s ; CARRIED %d MOVED %d ; block :%s ; reading FINDINGS :%s ; pointer :%s ; stems %s' % (
         ST['count'], {k: ST['term_tiers'][k] for k in ORDER}, {k: ST['row_tiers'][k] for k in ORDER}, ST['disp']['CARRIED'], ST['disp']['MOVED'],
         SB['line'], SR['findings']['line'], SR['pointer']['line'], SM['per']),
     '    the probes : %s' % ' ; '.join('%s %s %.0fs' % (k, v['exit'], v['seconds']) for k, v in sorted(ST['probes'].items())),
     '    the worktree : %s' % lw(read('b554_worktree.txt'), '### after:'),
     '    FINDINGS : the entry :%s ; next %s' % (FND['line'], FND['next']),
     '    the branches : %s' % ' ; '.join(l for l in read('b554_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s (N7) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b554_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
     '    pre-push : %s' % lw(read('b554_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b554_checks_postpush.txt'), 'ARMS RUN :')]
for n in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-simplicity', 'SIDE-grh-transfer'):
    p = ROOT if n == 'relay' else (PP if n == 'PLACE-papers' else os.path.join('D:', os.sep, n))
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b554_census_closing.txt'), 'TOTAL MISSING'), lw(read('b554_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b554_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT**: %s, the census`s next untiered keystone.' % FND['next'],
      '    (b) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping.',
      '    (c) Under (R157)(6) the seat`s memory is not refreshed at this act.',
      '=' * 104]
io.open(os.path.join(D, 'b554_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
