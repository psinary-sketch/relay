# -*- coding: utf-8 -*-
"""b555_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b555_*` and `relay/tools/b555_*` file, the four PLACE-papers
### documents this act writes, and the patch and message of every commit of this act (subject beginning `b555`) in four
### repositories, plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, math, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-kernel')
FILES = [os.path.join(PP, f) for f in ('FINDINGS.md', 'OPEN_TRAILS.md', 'phase1.5/spectral/GRH_CASCADE.md', 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md')]
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
        files = sorted(set(glob.glob(os.path.join(D, 'b555_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b555_*')) + FILES))
        files = [f for f in files if not f.endswith('b555_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40', 'HEAD').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b555'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b555_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b555_scores.json'))
H8 = json.loads(read('b555_h8.json'))
T3 = json.loads(read('b555_t3dp.json'))
CL = json.loads(read('b555_clause.json'))
TS = json.loads(read('b555_tiers.json'))
BL = json.loads(read('b555_block.json'))
SH = json.loads(read('b555_shells.json'))
SE = json.loads(read('b555_search.json'))
CO = json.loads(read('b555_cost.json'))
WE = json.loads(read('b555_weil.json'))
RD = json.loads(read('b555_reading.json'))
FND = json.loads(read('b555_findings.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
ORDER = ['T0', 'T1-open', 'T1-lit', 'T2', 'T2-INTERFACES', 'T3', 'T4']
n = H8['numbers']
L = ['=' * 104, 'b555 -- THE CLOSING RECORD. ### **THE CASCADE, ACT NINE, UNDER (R165).**', '=' * 104,
     '    H8 at its weight : FINDINGS :%s ; negative from %.3f, positive %.3f-%.3f, negative from %.3f ; floor %.2f' % (
         H8['line'], n['turns_negative'], n['second'][0], n['second'][1], n['stays_negative'], n['floor']),
     '    the tier law : the clause FINDINGS :%s ; T3doubleprime line BALANCE_AND_POSITIVITY :%s ; defect (o) OPEN_TRAILS :%s' % (
         CL['clause']['line'], T3['line'], CL['defect_o']['line']),
     '    GRH_CASCADE : %d rows ; tiers %s ; rows %s ; CARRIED %d MOVED %d ; block :%s ; χ in the composite`s body %s' % (
         TS['count'], {k: TS['term_tiers'][k] for k in ORDER}, {k: TS['row_tiers'][k] for k in ORDER}, TS['disp']['CARRIED'], TS['disp']['MOVED'],
         BL['line'], TS['chi_in_body']),
     '    SIDE-effects : branch %s HEAD %s ; c66f3c5 resolves %s ancestor %s ; a27415d ancestor %s' % (
         TS['effects']['branch'], TS['effects']['head'][:7], TS['effects']['c66f3c5']['resolves'], TS['effects']['c66f3c5']['ancestor_of_head'],
         TS['effects']['a27415d']['ancestor_of_head']),
     '    the probes : %s' % ' ; '.join('%s %s %.0fs' % (k, v['exit'], v['seconds']) for k, v in sorted(TS['probes'].items())),
     '    the shells : hits in the document %s' % (SH['hits'] or 'NONE'),
     '    the search : %s ; EF_lit fixed to ζ %s' % ({k: (len(v['rh_decls']), len(v['crit']), len(v['ef'])) for k, v in SE.items() if k != 'zeta23'},
                                                 SE['zeta23']['fixed']),
     '    the arc : %s ; Zeta23 %s' % (CO['total'], CO['zeta23']),
     '    W-ORD-GRH-WEIL : OPEN_TRAILS :%s ; χ-side %d (new %d + re-instantiated %d) against %d' % (WE['line'], WE['chi'], WE['new'], WE['reinst'], WE['arc']),
     '    the reading : FINDINGS :%s ; pointer GRH_CASCADE :%s ; the entry :%s ; next %s' % (RD['findings']['line'], RD['pointer']['line'], FND['line'], FND['next']),
     '    the branches : %s' % ' ; '.join(l for l in read('b555_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s (N7) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b555_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
     '    pre-push : %s' % lw(read('b555_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b555_checks_postpush.txt'), 'ARMS RUN :')]
for nm in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-grh-transfer', 'SIDE-effects',
           'SIDE-bsd-formation-transfer', 'SIDE-yang-mills-formation'):
    p = ROOT if nm == 'relay' else (PP if nm == 'PLACE-papers' else os.path.join('D:', os.sep, nm))
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-28s local %s ; remote %s ; %s' % (nm, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b555_census_closing.txt'), 'TOTAL MISSING'), lw(read('b555_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b555_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT**: %s, the census`s next untiered keystone.' % FND['next'],
      '    (b) ### **FOR THE AUTHOR**: (N4) is REFUTED by its sealed predicate while the hand-read finds no Dirichlet critical-line statement or explicit formula (defect (g)).',
      '    (c) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping.',
      '    (d) Under (R157)(6) the seat`s memory is not refreshed at this act.',
      '=' * 104]
io.open(os.path.join(D, 'b555_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
