# -*- coding: utf-8 -*-
"""b560_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b560_*` and `relay/tools/b560_*` file, the PLACE-papers
### documents this act writes, CORRESPONDENCE.md, both new kernel modules at main, and the patch and message of every commit
### of this act (subject beginning `b560`, or housekeeping naming (R170)) in five repositories, plus any uncommitted change.
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
    return subject.startswith('b560') or (subject.startswith('housekeeping:') and '(R170)' in subject)


def tokenscan():
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    if not t:
        res = dict(set=False)
    else:
        files = sorted(set(glob.glob(os.path.join(D, 'b560_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b560_*')) + FILES))
        files = [f for f in files if os.path.isfile(f) and not f.endswith('b560_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        for m in ('SIDEExplicitFormula/LiWeil.lean', 'SIDEExplicitFormula/DetectionRegion.lean'):
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
        res = dict(set=True, files_scanned=len(files) + 2, commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b560_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b560_scores.json'))
E0 = json.loads(read('b560_e0.json'))
CJ = json.loads(read('b560_clean.json'))
FND = json.loads(read('b560_findings.json'))
L1 = json.loads(read('b560_ledger1.json'))
TR = json.loads(read('b560_trail.json'))
WO = json.loads(read('b560_workorder.json'))
RW = json.loads(read('b560_rows.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
st = {x: json.loads(read('b560_stage%s.json' % x)) for x in 'ABCD'}
v03, v04 = git(EF, 'rev-parse', 'v0.3^{}'), git(EF, 'rev-parse', 'v0.4^{}')
L = ['=' * 104, 'b560 -- THE CLOSING RECORD. ### **LANE TWO, ACT TWO: THE LI-WEIL BRIDGE, STAGED AND HELD AT THE LIMIT EXCHANGE, UNDER (R170).**', '=' * 104,
     '    the suite change : relay %s ; the re-run on b559`s push : %s' % (
         git(ROOT, 'log', '-1', '--format=%h', '--', 'tools/b559_checks.py'), lw(read('b560_b559_postpush_rerun.txt'), 'ARMS RUN :')),
     '    the clean merge : v0.3 object %s peeled %s (remote %s) ; the gate %s ; from main %s' % (
         git(EF, 'rev-parse', '--short', 'v0.3'), v03[:7], (git(EF, 'ls-remote', 'origin', 'refs/tags/v0.3^{}').split() or [''])[0][:7], CJ['gate'], CJ['parent'][:7]),
     '    the stages : ' + ' ; '.join('%s %d decls, attempts %d, std3 %s' % (x, len(st[x]['names']), st[x]['attempts'], st[x]['all_std3']) for x in 'ABCD'),
     '    the E0 read : %s ; the salt-check %s ; the gate %s' % (E0['counts'], E0['salt'], E0['gate']),
     '    v0.4 : object %s peeled %s (remote %s) = main %s = li-weil-b560 %s' % (
         git(EF, 'rev-parse', '--short', 'v0.4'), v04[:7], (git(EF, 'ls-remote', 'origin', 'refs/tags/v0.4^{}').split() or [''])[0][:7],
         git(EF, 'rev-parse', '--short', 'main'), git(EF, 'rev-parse', '--short', 'li-weil-b560')),
     '    the ledger lines : FINDINGS :%s (clean reading) :%s (entry) ; OPEN_TRAILS :%s (HELD line) :%s (re-scope) :%s (research arc) :%s (work-order) :%s (record) ; row 395 exit %d'
     % (L1['lines']['findings'], FND['heading_line'], L1['lines']['held'], L1['lines']['rescope'], L1['lines']['arc'], WO['line'], TR['line'], RW['exit']),
     '    the branches : %s' % ' ; '.join(l for l in read('b560_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    H11a REFUTED as first worded, %s as amended ; H11b %s ; H11c %s ; H11d %s ; H11e %s' % tuple(W(SC[k]) for k in ('h11a', 'h11b', 'h11c', 'h11d', 'h11e')),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s' % tuple(
         W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b560_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES.',
     '    pre-push : %s' % lw(read('b560_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b560_checks_postpush.txt'), 'ARMS RUN :')]
for nm in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-effects', 'SIDE-silence-principle',
           'SIDE-compression', 'SIDE-structural-error-correction', 'SIDE-cosmo'):
    p = ROOT if nm == 'relay' else (PP if nm == 'PLACE-papers' else os.path.join('D:', os.sep, nm))
    loc, rem = git(p, 'rev-parse', 'main'), (git(p, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    L.append('      %-28s main %s ; remote %s ; %s' % (nm, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
for b, note in (('detection-region-b559', 'HELD, kept'), ('li-weil-b560', 'pushed by name, kept')):
    bl, brm = git(EF, 'rev-parse', b), (git(EF, 'ls-remote', 'origin', 'refs/heads/' + b).split() or [''])[0]
    L.append('      %-28s local %s ; remote %s ; %s (%s)' % (b, bl[:12], brm[:12], 'AGREE' if bl == brm else 'DISAGREE', note))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b560_census_closing.txt'), 'TOTAL MISSING'), lw(read('b560_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b560_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT, (R170)(7)**: the bridge continued at (D1)-(D4) -- the exchange is priced, its lemma of substance (D3) a',
      '        dominant for the conjugate-paired truncated transforms uniform along the family -- if the author so rules; else W-ORD-GRH-WEIL.',
      '    (b) ### **FOR THE AUTHOR**: SIDE-explicit-formula v0.3 and v0.4 are tagged; `rh_imp_li_nonneg` is the forward half over the',
      '        genuine zeros; `LiLimitExchange` and `blTransform` stand on main as Props, stated and not proved; `li_identity_of_exchange`',
      '        is INTERFACES on the first.',
      '    (c) ### **FOR THE AUTHOR**: the navigator`s citations corrected in the record: (R170)(1)`s "from v0.2" (main sat one commit past',
      '        it); BALPOS C.7.3 is the detection threshold, the Bombieri-Lagarias formula stands at :70 and :422.',
      '    (d) ### **FOR THE AUTHOR**: the re-run on b559`s push by digests fails G-WRITELIST-KINDS on terminal_table.json by content',
      '        (b559`s defect (h) stands, now read without file times) and G-NUMBER-UNCLAIMED on this act`s own face (defect (c)).',
      '    (e) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping if it changed.',
      '=' * 104]
io.open(os.path.join(D, 'b560_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
