# -*- coding: utf-8 -*-
"""b566_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b566_*` and `relay/tools/b566_*` file, the PLACE-papers
### documents this act writes, CORRESPONDENCE.md, and the patch and message of every commit of this act (subject beginning
### `b566`, or housekeeping naming (R176) or b566) in four repositories (the kernel`s main and its backport branch), plus any
### uncommitted change. Carried from b565_closing.py and re-pointed. This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
EF = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(p):
    return io.open(os.path.join(D, p), encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


FILES = [os.path.join(PP, f) for f in ('FINDINGS.md', 'OPEN_TRAILS.md', 'README.md', 'REGISTRY.md')] + [os.path.join(SIDE, 'CORRESPONDENCE.md')]


def lw(t, n):
    return next((l.strip() for l in t.split(NL) if n in l), '')


def git(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def git_bytes(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True).stdout


def ours(subject):
    return subject.startswith('b566') or (subject.startswith('housekeeping:') and ('(R176)' in subject or 'b566' in subject))


def tokenscan():
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    if not t:
        res = dict(set=False)
    else:
        files = sorted(set(glob.glob(os.path.join(D, 'b566_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b566_*')) + FILES))
        files = [f for f in files if os.path.isfile(f) and not f.endswith('b566_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        seen = set()
        for repo, rev in ((ROOT, 'HEAD'), (PP, 'HEAD'), (SIDE, 'HEAD'), (EF, 'main'), (EF, 'vendor-bulka-backport-b566')):
            for l in git(repo, 'log', '--pretty=%H %s', '-40', rev).split(NL):
                if l.strip() and ours(l.split(' ', 1)[-1]) and l.split()[0] not in seen:
                    seen.add(l.split()[0])
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b566_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
J = lambda n: json.loads(read(n))
SC, TRJ, RT, E0, FND, TR, WJ, CL, PJ, CJ, RW, RH = (J('b566_%s.json' % n) for n in (
    'scores', 'trials', 'route', 'e0', 'findings', 'trail', 'weight', 'complete_line', 'price', 'ceiling', 'rows', 'arda_rehash'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
K = SC['kstate']
L = ['=' * 104, 'b566 -- THE CLOSING RECORD. ### **THE CONVERSE VENDORED, UNDER (R176).**', '=' * 104,
     '    step zero : b565`s closing push output committed alone (f0e41d7d) ; the process listing (no orphan) ; this act`s pushes'
     ' captured to data/b566_push_out.txt, data/b566_kernel_push_out.txt and data/b566_relay_push_out.txt',
     '    component 1 : the weight line FINDINGS :%s ; the ceiling sentence README :%s, REGISTRY :%s ; Arda`s banks %d of %d re-verified,'
     ' the clone deleted (%s)' % (WJ.get('line'), CJ['files']['README.md']['new_line'], CJ['files']['REGISTRY.md']['new_line'],
                                 RH.get('agree'), RH.get('total'), lw(read('b566_arda_delete.txt'), 'arda ABSENT')),
     '    step one : the licence Apache 2.0 (H19a %s) ; the converse`s closure %s modules, the vendored set 33 ; the distance %s'
     % (W(SC['h19a']), SC.get('n_conv'), lw(read('b566_step1_distance.txt'), 'THE DISTANCE:')[:120]),
     '        trial (a) backport : modules %d, exit 0 %d, non-zero %s, errors %d, blocked %d'
     % (TRJ['a']['modules'], TRJ['a']['ok'], TRJ['a']['bad'], TRJ['a']['errors'], sum(1 for r in TRJ['a']['rows'] if r['rc'] == 'BLOCKED')),
     '        trial (b) forward : modules %d, exit 0 %d, errors %d' % (TRJ['b']['modules'], TRJ['b']['ok'], TRJ['b']['errors']),
     '        %s' % RT['word'],
     '    step two : li_coeff_eq_taylorCoeff, its statement banked before the build (sha256 991c0428) ; (E1)-(E4) at the standard three',
     '    step three : %s' % lw(read('b566_e0.txt'), 'THE GATE:')[:200],
     '    the kernel : main = v0.9 = %s (tag object %s, %s), read back at the remote before the tag ; backport branch %s and route'
     ' branch %s pushed by name ; existing .lean files changed %s' % (K['v09'][:7], K['v09obj'][:7], K['v09type'], K['back'][:7],
                                                                    K['fwd'][:7], K['lean_changed'] or 'NONE'),
     '    the re-prints at the new pins : %s' % lw(read('b566_reprint_summary.txt'), 'parsed by')[:200],
     '    the ledger lines : FINDINGS :%s (weight) :%s (composition) :%s (entry) ; OPEN_TRAILS :%s (the residue chain priced) :%s'
     ' (record) ; rows %s' % (WJ['line'], CL['line'], FND['heading_line'], PJ['line'], TR['line'],
                             ', '.join('%s exit %s' % (r['row'], r['exit']) for r in RW['rows'])),
     '    the rowgen diff : %s' % ' ; '.join(l.strip() for l in read('b566_rowgen.txt').split(NL) if l.strip().startswith("('")),
     '    the branches : %s' % ' ; '.join(l for l in read('b566_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits'
                             % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    H19a %s ; H19b %s ; H19c %s ; H19d %s' % (W(SC['h19a']), W(SC['h19b']), W(SC['h19c']), W(SC['h19d'])),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s' % tuple(
         W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b566_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES.',
     '    pre-push : %s' % lw(read('b566_checks.txt'), 'ARMS RUN :'),
     '    pre-push : %s' % lw(read('b566_checks.txt'), 'VERDICT :'),
     '    post-push : %s' % lw(read('b566_checks_postpush.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b566_checks_postpush.txt'), 'VERDICT :')]
for nm in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-effects',
           'SIDE-silence-principle', 'SIDE-compression', 'SIDE-structural-error-correction', 'SIDE-cosmo'):
    p = ROOT if nm == 'relay' else (PP if nm == 'PLACE-papers' else os.path.join('D:', os.sep, nm))
    loc, rem = git(p, 'rev-parse', 'main'), (git(p, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    L.append('      %-28s main %s ; remote %s ; %s' % (nm, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
for b, note in (('detection-region-b559', 'HELD, kept'), ('li-weil-b561', 'kept'), ('grh-weil-b562', 'kept'), ('li-weil-b563', 'kept'),
                ('grh-weil-b564', 'kept'), ('vendor-bulka-backport-b566', 'trial (a), kept as data'),
                ('vendor-bulka-forward-b566', 'trial (b), the route, = main')):
    bl, brm = git(EF, 'rev-parse', b), (git(EF, 'ls-remote', 'origin', 'refs/heads/' + b).split() or [''])[0]
    L.append('      %-28s local %s ; remote %s ; %s (%s)' % (b, bl[:12], brm[:12], 'AGREE' if bl == brm else 'DISAGREE', note))
tg, trm = git(EF, 'rev-parse', 'v0.9^{}'), (git(EF, 'ls-remote', 'origin', 'refs/tags/v0.9^{}').split() or [''])[0]
L.append('      %-28s peeled %s ; remote %s ; %s' % ('v0.9', tg[:12], trm[:12], 'AGREE' if tg == trm else 'DISAGREE'))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'origin/main').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b566_census_closing.txt'), 'TOTAL MISSING'), lw(read('b566_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b566_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '    the clones : D:/audit-b565/bulka @%s KEPT (its deletion not ordered at this act) ; D:/audit-b565/arda DELETED ;'
      ' the worktree D:/b566-forward (branch vendor-bulka-forward-b566) KEPT, outside the corpus' % git('D:/audit-b565/bulka', 'rev-parse', '--short=8', 'HEAD'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **FOR THE AUTHOR, (R176)(3)**: the composition LANDED at v0.9. The ceiling`s second amendment -- "Li`s criterion is',
      '        compiled over Mathlib`s zeros in the programme`s kernel, its converse vendored from Bulka at 35df682f" -- is the author`s',
      '        word at this closing; it is not written.',
      '    (b) ### **FOR THE AUTHOR**: the suite is NOT CLEAN, 72 of 74 -- G-WRITELIST-KINDS (the face`s (W) omits Vendored/Bulka/LICENSE,',
      '        defect (g)) and G-LICENCE-PRINTED (the licence bank`s sha256 is the CRLF working file`s, defect (h)); both true, neither',
      '        arm edited, the face and the pre-seal bank left as they are.',
      '    (c) ### **THE NEXT ACT, (R176)(7)**: b567 is GRH-WEIL act three as (R175)(6) fixed it -- LFunction χ on 0 < Re s by Abel',
      '        summation (H18a-H18c). It runs on the kernel at Lean v4.34.0-rc1 / Mathlib de5ce8a9: D:/b566-forward holds the built',
      '        tree; the main checkout D:/SIDE-explicit-formula holds the v0.8-era .lake and would re-fetch on a lake call.',
      '    (d) The residue chain`s Li-channel premise is priced at OPEN_TRAILS :%s ((L1)-(L3)); inequalityToPositivity stays the' % PJ['line'],
      '        bridge`s last item.',
      '    (e) Bulka`s clone stays under D:/audit-b565 until the author`s word; Arda`s is gone.',
      '    (f) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping if it changed.',
      '=' * 104]
io.open(os.path.join(D, 'b566_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
