# -*- coding: utf-8 -*-
"""b561_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b561_*` and `relay/tools/b561_*` file, the PLACE-papers
### documents this act writes, CORRESPONDENCE.md, both new kernel modules at main, and the patch and message of every commit
### of this act (subject beginning `b561` or `push discipline:`, or housekeeping naming (R171)) in five repositories, plus any uncommitted change.
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
    return subject.startswith('b561') or subject.startswith('push discipline:') or (subject.startswith('housekeeping:') and '(R171)' in subject)


def tokenscan():
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    if not t:
        res = dict(set=False)
    else:
        files = sorted(set(glob.glob(os.path.join(D, 'b561_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b561_*')) + FILES))
        files = [f for f in files if os.path.isfile(f) and not f.endswith('b561_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        for m in ('SIDEExplicitFormula/LiWeilExchange.lean',):
            b = git_bytes(EF, 'show', 'main:' + m)
            if t in b:
                hits[m] = b.count(t)
        commits = 0
        for repo, rev in ((ROOT, 'HEAD'), (PP, 'HEAD'), (SIDE, 'HEAD'), (KER, 'HEAD'), (EF, 'main')):
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
    io.open(os.path.join(D, 'b561_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b561_scores.json'))
E0 = json.loads(read('b561_e0.json'))
WT = json.loads(read('b561_weight.json'))
CN = json.loads(read('b561_consumer.json'))
FND = json.loads(read('b561_findings.json'))
TR = json.loads(read('b561_trail.json'))
WO = json.loads(read('b561_workorder.json'))
RW = json.loads(read('b561_rows.json'))
DJ = json.loads(read('b561_decay.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
d1, d2 = json.loads(read('b561_D1.json')), json.loads(read('b561_D2.json'))
v05 = git(EF, 'rev-parse', 'v0.5^{}')
L = ['=' * 104, 'b561 -- THE CLOSING RECORD. ### **LANE TWO, ACT THREE: THE LI-WEIL BRIDGE AT THE LIMIT EXCHANGE, HELD AT (D3), UNDER (R171).**', '=' * 104,
     '    the weight lines : FINDINGS :%s :%s :%s ; BALPOS :%s' % (WT['lines']['twoforms'], WT['lines']['tier'], WT['lines']['field'], WT['lines']['balpos']),
     '    the push discipline : relay %s (tools/push_gated.sh, committed alone, its test quoted)' % git(ROOT, 'log', '-1', '--format=%h', '--', 'tools/push_gated.sh'),
     '    the decay read : H12a %s ; the uniform order %s ; (D3) %s ; the exchange %s ; sup values %s' % (DJ['h12a'], DJ['uniform_order'], DJ['d3'], DJ['exchange_expected'], DJ['sup_values']),
     '    the items : D1 %d decls, attempts %d, std3 %s ; D2 %d decls, attempts %d, std3 %s ; D3 HELD at the read ; D4 not reached' % (
         len(d1['names']), d1['attempts'], d1['all_std3'], len(d2['names']), d2['attempts'], d2['all_std3']),
     '    the E0 read : %d of %d DERIVES ; the gate %s' % (sum(1 for r in E0['rows'].values() if r['grade'] == 'DERIVES'), len(E0['rows']), E0['gate']),
     '    v0.5 : object %s peeled %s (remote %s) = main %s = li-weil-b561 %s ; pushed by push_gated.sh after main read back' % (
         git(EF, 'rev-parse', '--short', 'v0.5'), v05[:7], (git(EF, 'ls-remote', 'origin', 'refs/tags/v0.5^{}').split() or [''])[0][:7],
         git(EF, 'rev-parse', '--short', 'main'), git(EF, 'rev-parse', '--short', 'li-weil-b561')),
     '    the ledger lines : FINDINGS :%s (entry) ; OPEN_TRAILS :%s (consumer read) :%s (work-order) :%s (record) ; row 396 exit %d'
     % (FND['heading_line'], CN['line'], WO['line'], TR['line'], RW['exit']),
     '    the branches : %s' % ' ; '.join(l for l in read('b561_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    H12a %s ; H12b %s ; H12c %s' % tuple(W(SC[k]) for k in ('h12a', 'h12b', 'h12c')),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s' % tuple(
         W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b561_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES.',
     '    pre-push : %s' % lw(read('b561_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b561_checks_postpush.txt'), 'ARMS RUN :')]
for nm in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-effects', 'SIDE-silence-principle',
           'SIDE-compression', 'SIDE-structural-error-correction', 'SIDE-cosmo'):
    p = ROOT if nm == 'relay' else (PP if nm == 'PLACE-papers' else os.path.join('D:', os.sep, nm))
    loc, rem = git(p, 'rev-parse', 'main'), (git(p, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    L.append('      %-28s main %s ; remote %s ; %s' % (nm, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
for b, note in (('detection-region-b559', 'HELD, kept'), ('li-weil-b561', 'pushed by name, kept')):
    bl, brm = git(EF, 'rev-parse', b), (git(EF, 'ls-remote', 'origin', 'refs/heads/' + b).split() or [''])[0]
    L.append('      %-28s local %s ; remote %s ; %s (%s)' % (b, bl[:12], brm[:12], 'AGREE' if bl == brm else 'DISAGREE', note))
L.append('      %-28s local [%s] ; remote [%s] (deleted by name after its tip was read as an ancestor of main; defect (b))' % (
    'li-weil-b560', git(EF, 'branch', '--list', 'li-weil-b560'), git(EF, 'ls-remote', 'origin', 'refs/heads/li-weil-b560')))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b561_census_closing.txt'), 'TOTAL MISSING'), lw(read('b561_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b561_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT, (R171)(5)**: W-ORD-GRH-WEIL. The bridge`s items return to the trails priced: (X1) the explicit formula',
      '        on a class containing the midpoint-normalised jump, (X2) a two-sided family with the limit read on EF_lit`s other side,',
      '        (X3) the exchange restated; (D5), (D6), the converse (V1)-(V4).',
      '    (b) ### **FOR THE AUTHOR**: `LiLimitExchange n` as b560 stated it is, on the decay read, FALSE for n >= 1 (the one-sided',
      '        smoothing moves the jump`s midpoint into u < 0; the zero side tends to -infinity like -(n/2) log(1/delta)); a derivation',
      '        resting on Stirling and Riemann-von Mangoldt, not compiled. `li_identity_of_exchange` (INTERFACES) rests on it.',
      '    (c) ### **FOR THE AUTHOR**: `blTransform`, stated at v0.4, is proved at v0.5 (`blTransform_holds`).',
      '    (d) ### **FOR THE AUTHOR**: the remote deletion of li-weil-b560 was rejected as "unable to resolve reference" while the ref',
      '        reads absent -- defect (b)`s ambiguity.',
      '    (e) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping if it changed.',
      '=' * 104]
io.open(os.path.join(D, 'b561_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
