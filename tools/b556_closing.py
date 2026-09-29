# -*- coding: utf-8 -*-
"""b556_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b556_*` and `relay/tools/b556_*` file, the five PLACE-papers
### documents this act writes, and the patch and message of every commit of this act (subject beginning `b556`) in four
### repositories, plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-kernel')
DOCS = {'RCURVE': 'phase1.5/rcurve/R_CURVE_CRITERION.md', 'INDEX': 'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md',
        'AMC': 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md'}
FILES = [os.path.join(PP, f) for f in ['FINDINGS.md', 'OPEN_TRAILS.md'] + list(DOCS.values())]
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
        files = sorted(set(glob.glob(os.path.join(D, 'b556_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b556_*')) + FILES))
        files = [f for f in files if not f.endswith('b556_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40', 'HEAD').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b556'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b556_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b556_scores.json'))
TS = json.loads(read('b556_tiers.json'))
BL = json.loads(read('b556_blocks.json'))
PA = json.loads(read('b556_path.json'))
RC = json.loads(read('b556_rcurve.json'))
FND = json.loads(read('b556_findings.json'))
PR = [json.loads(l) for l in read('b556_probes.jsonl').split(NL) if l.strip()]
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
ORDER = ['T0', 'T1-open', 'T1-lit', 'T2', 'T2-INTERFACES', 'T3', 'T4']
L = ['=' * 104, 'b556 -- THE CLOSING RECORD. ### **THE CASCADE, ACT TEN, BATCH ONE, UNDER (R166).**', '=' * 104,
     '    the critical path : OPEN_TRAILS :%s ; pointer FINDINGS :%s ; work-orders cited %d ; none started' % (
         PA['trail']['line'], PA['pointer']['line'], len(PA['work']))]
for k in DOCS:
    s = TS[k]
    L.append('    %-6s : block :%s ; %d rows ; tiers %s ; rows %s ; CARRIED %d MOVED %d %s' % (
        k, BL[k]['line'], len(s['rows']), {x: s['term_tiers'][x] for x in ORDER if s['term_tiers'][x]}, {x: s['row_tiers'][x] for x in ORDER if s['row_tiers'][x]},
        s['disp']['CARRIED'], s['disp']['MOVED'], [r['line'] for r in s['rows'] if r['disp'] == 'MOVED']))
L += ['    SIDE-rcurve v0.1.0 : %s' % {x: v for x, v in RC['split'].items() if v},
      '    the probes : %d records -- elaborated %d, compared at the tag %d ; non-zero exits %s' % (
          len(PR), sum(1 for r in PR if not r.get('identical_to')), sum(1 for r in PR if r.get('identical_to')),
          ['%s %s' % (r['id'], r['exit']) for r in PR if r.get('exit') not in (0, None)]),
      '    no_type_d_conspiracies : a27415d %s ; c66f3c5 %s ; the wrong table :%s' % (SC['pa'], SC['pc'], BL['wrong']),
      '    the citations : %s' % {k: v['resolved'] for k, v in RC['citations'].items()},
      '    the entry : FINDINGS :%s ; next b557' % FND['line'],
      '    the branches : %s' % ' ; '.join(l for l in read('b556_branches.txt').split(NL) if l.startswith('Deleted branch')),
      '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
      '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
      '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b556_defects.txt').rstrip(NL).split(NL) if l] + [
      '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
      '    pre-push : %s' % lw(read('b556_checks.txt'), 'ARMS RUN :'),
      '    post-push : %s' % lw(read('b556_checks_postpush.txt'), 'ARMS RUN :')]
for nm in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-effects', 'SIDE-rcurve',
           'SIDE-meta', 'SIDE-silence-principle', 'SIDE-compression'):
    p = ROOT if nm == 'relay' else (PP if nm == 'PLACE-papers' else os.path.join('D:', os.sep, nm))
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-28s local %s ; remote %s ; %s' % (nm, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b556_census_closing.txt'), 'TOTAL MISSING'), lw(read('b556_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b556_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT**: b557, the eight method keystones (batch two of CP-1), then b558 CP-1b.',
      '    (b) ### **FOR THE AUTHOR**: no_type_d_conspiracies and crt_exhaustiveness read T2 by the ferry`s criterion where b555 banked T0; not settled by the seat.',
      '    (c) ### **FOR THE AUTHOR**: SIDE-lv-conservation`s checkout carries a RegisterPentagon olean that does not match its source (defect (b)); no build was run.',
      '    (d) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping.',
      '    (e) Under (R157)(6) and (R166)(2) the seat`s memory is not refreshed at this act; b558 refreshes it.',
      '=' * 104]
io.open(os.path.join(D, 'b556_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
