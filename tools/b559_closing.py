# -*- coding: utf-8 -*-
"""b559_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b559_*` and `relay/tools/b559_*` file, the PLACE-papers
### documents this act writes, CORRESPONDENCE.md, the branch module, and the patch and message of every commit of this act
### (subject beginning `b559`, or housekeeping naming (R169)) in five repositories, plus any uncommitted change there.
### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-kernel')
EF = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(p):
    return io.open(os.path.join(D, p), encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


FILES = [os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md'), os.path.join(SIDE, 'CORRESPONDENCE.md')]


def lw(t, n):
    return next((l.strip() for l in t.split(NL) if n in l), '')


def git(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def git_bytes(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True).stdout


def ours(subject):
    return subject.startswith('b559') or (subject.startswith('housekeeping:') and '(R169)' in subject)


def tokenscan():
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    if not t:
        res = dict(set=False)
    else:
        files = sorted(set(glob.glob(os.path.join(D, 'b559_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b559_*')) + FILES))
        files = [f for f in files if os.path.isfile(f) and not f.endswith('b559_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        b = git_bytes(EF, 'show', 'detection-region-b559:SIDEExplicitFormula/DetectionRegion.lean')
        if t in b:
            hits['DetectionRegion.lean'] = b.count(t)
        commits = 0
        for repo, rev in ((ROOT, 'HEAD'), (PP, 'HEAD'), (SIDE, 'HEAD'), (KER, 'HEAD'), (EF, 'detection-region-b559')):
            for l in git(repo, 'log', '--pretty=%H %s', '-40', rev).split(NL):
                if l.strip() and ours(l.split(' ', 1)[-1]):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        res = dict(set=True, files_scanned=len(files) + 1, commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b559_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b559_scores.json'))
C = json.loads(read('b559_constants.json'))
E0 = json.loads(read('b559_e0.json'))
FND = json.loads(read('b559_findings.json'))
PC = json.loads(read('b559_price.json'))
TR = json.loads(read('b559_trail.json'))
RW = json.loads(read('b559_rows.json'))
HK = json.loads(read('b559_housekeeping.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
br = read('b559_branch.txt')
L = ['=' * 104, 'b559 -- THE CLOSING RECORD. ### **LANE TWO, ACT ONE: W-ORD-DETECTION-REGION, STATED AND HELD, UNDER (R169).**', '=' * 104,
     '    the housekeeping : relay %s (the refresh record) ; %s (G-PEEK-DECLARED by content digests) ; the re-run on b558`s push 63 of 63: %s'
     % (HK['refresh'], HK['tool'], HK['rerun_63']),
     '    the constants : %d rows ; %s ; reach THE CONFIGURATION %d ; the step %s' % (
         len(C['rows']), ' ; '.join('%s %d' % (k, sum(1 for r in C['rows'] if r['kind'] == k)) for k in ('EXPLICIT', 'EXISTENTIAL-WITH-WITNESS', 'NON-CONSTRUCTIVE')),
         len(C['configuration']), C['step']),
     '    the branch : %s' % ' ; '.join(l for l in br.split(NL) if l.startswith(('local ', 'parent', 'remote ', 'branch an ancestor', 'tags v0.3'))),
     '    the E0 grade : %s ; the companions %s' % (E0['grade'], ', '.join('%s %s' % (k, v) for k, v in E0['grades'].items() if v == 'DERIVES')),
     '    the price line : OPEN_TRAILS :%d ; the entry : FINDINGS :%d ; the reading :%d ; the trail record : OPEN_TRAILS :%d ; row 394 exit %d'
     % (PC['line'], FND['heading_line'], FND['reading_line'], TR['line'], RW['exit']),
     '    the branches : %s' % ' ; '.join(l for l in read('b559_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    H9a %s H9b %s H9c %s H9d %s' % tuple(W(SC[k]) for k in ('h9a', 'h9b', 'h9c', 'h9d')),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s' % tuple(
         W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b559_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES.',
     '    pre-push : %s' % lw(read('b559_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s -- its G-WRITELIST-KINDS pass is defect (i)`s artefact' % lw(read('b559_checks_postpush.txt'), 'ARMS RUN :')]
for nm in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-effects', 'SIDE-silence-principle',
           'SIDE-compression', 'SIDE-structural-error-correction', 'SIDE-cosmo'):
    p = ROOT if nm == 'relay' else (PP if nm == 'PLACE-papers' else os.path.join('D:', os.sep, nm))
    loc, rem = git(p, 'rev-parse', 'main'), (git(p, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    L.append('      %-28s main %s ; remote %s ; %s' % (nm, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
bl, brm = git(EF, 'rev-parse', 'detection-region-b559'), (git(EF, 'ls-remote', 'origin', 'refs/heads/detection-region-b559').split() or [''])[0]
L.append('      %-28s local %s ; remote %s ; %s (HELD, kept)' % ('detection-region-b559', bl[:12], brm[:12], 'AGREE' if bl == brm else 'DISAGREE'))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b559_census_closing.txt'), 'TOTAL MISSING'), lw(read('b559_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b559_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT**: W-ORD-LI-WEIL-BRIDGE, (R169)(7); the order of lane two does not change on a HELD.',
      '    (b) ### **FOR THE AUTHOR**: W-ORD-DETECTION-REGION`s price is corrected on the trail (OPEN_TRAILS :%d): (E1) one lemma gives an' % PC['line'],
      '        index relative to the configuration; (E2), the per-zero bound, needs a separation estimate no compiled lemma carries.',
      '    (c) ### **FOR THE AUTHOR**: the branch detection-region-b559 is kept, HELD; no `sorry` is on any main.',
      '    (d) ### **FOR THE AUTHOR**: the suite`s file-time arms other than G-PEEK-DECLARED (G-WRITELIST-KINDS, G-PRIORBANK-UNCHANGED) read',
      '        the checkout`s rewrite after a push -- defect (i); (R169)(1)(b)`s cure covered one arm.',
      '    (e) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping, since it changed.',
      '=' * 104]
io.open(os.path.join(D, 'b559_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
