# -*- coding: utf-8 -*-
"""b567_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b567_*` and `relay/tools/b567_*` file, the shared addendum tools,
### the PLACE-papers documents this act writes, CORRESPONDENCE.md, and the patch and message of every commit of this act (subject
### beginning `b567`, or housekeeping naming (R177) or b567) in four repositories (the kernel`s main and its residue branch),
### plus any uncommitted change. Carried from b566_closing.py and re-pointed. This file deletes nothing.
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
FILES = [os.path.join(PP, f) for f in ('FINDINGS.md', 'OPEN_TRAILS.md', 'README.md', 'REGISTRY.md', 'phase1.5/proofs/THE_RESIDUE_OF_RH.md')] + \
        [os.path.join(SIDE, 'CORRESPONDENCE.md')] + [os.path.join(ROOT, 'tools', f) for f in ('addenda.py', 'test_addenda_writelist.py',
                                                                                             'test_addenda_licence.py')]


def read(p):
    p = p if os.path.isabs(p) else os.path.join(D, p)
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace('\r\n', NL)
    except OSError:
        return ''


def lw(t, n):
    return next((l.strip() for l in t.split(NL) if n in l), '### NOT FOUND: ' + n)


def git(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def git_bytes(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True).stdout


def ours(subject):
    return subject.startswith('b567') or (subject.startswith('housekeeping:') and ('(R177)' in subject or 'b567' in subject))


def tokenscan():
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    if not t:
        res = dict(set=False)
    else:
        files = sorted(set(glob.glob(os.path.join(D, 'b567_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b567_*')) + FILES))
        files = [f for f in files if os.path.isfile(f) and not f.endswith('b567_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        seen = set()
        for repo, rev in ((ROOT, 'HEAD'), (PP, 'HEAD'), (SIDE, 'HEAD'), (EF, 'main'), (EF, 'residue-discharge-b567')):
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
    io.open(os.path.join(D, 'b567_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
J = lambda n: json.loads(read(n))
SC, E3, E4, FND, TR, WJ, CJ, FJ, SJ, RLJ, T2, RV, DJ, BV, RW, ZB = (J('b567_%s.json' % n) for n in (
    'scores', 'e0_residue', 'e0_chi', 'findings', 'trail', 'weight', 'ceiling', 'field', 's7', 'residue_line', 'trails2', 'census_revs',
    'deprecations', 'bulka_verify', 'rows', 'zb_consumers'))
W = lambda k: SC[k].split(' --')[0]
K = SC['kstate']
L = ['=' * 104, 'b567 -- THE CLOSING RECORD. ### **GRH-WEIL ACT THREE; THE CEILING AMENDED; THE ADDENDUM FORMS; THE FORWARD MOVE; '
     'THE RESIDUE PREMISE, UNDER (R177).**', '=' * 104,
     '    step zero : b566`s closing push output committed alone (401bb062) ; the process listing (no orphan) ; the face sealed'
     ' 2026-10-01T01:37:20Z with section (0) declaring what ran ahead',
     '    component 1 : the weight FINDINGS :%s ; the ceiling sentence README :%s, REGISTRY :%s, its record FINDINGS :%s ; the field line'
     ' FINDINGS :%s' % (WJ.get('line'), CJ['files']['README.md']['new_line'], CJ['files']['REGISTRY.md']['new_line'], CJ.get('findings_line'),
                        FJ.get('line')),
     '        the addendum forms : (g) relay 0e50bd19, (h) relay 90373807, each with its test (%s ; %s)'
     % (lw(read('b567_test_writelist.txt'), 'cases as wanted'), lw(read('b567_test_licence.txt'), 'cases as wanted')),
     '        b566`s suite re-run on b566`s push : before %s ; after %s' % (lw(read('b567_b566_rerun_before.txt'), 'ARMS RUN :'),
                                                                        lw(read('b567_b566_rerun_after.txt'), 'ARMS RUN :')),
     '    component 2 : distinct Mathlib revs %d (b551 %d) ; toolchain-trial-b551 STALE OPEN_TRAILS :%s ; W-ORD-DEPRECATIONS OPEN_TRAILS :%s'
     ' (%d lines, %d classes, top %s -> %s)' % (RV['count'], RV['b551'], T2.get('stale_line'), T2.get('wo_line'), DJ['lines'], DJ['classes'],
                                                DJ['top'][0][0], ', '.join(DJ['top'][0][3])),
     '        the cache : %s ; %s' % (lw(read('b567_cache.txt'), 'after: checkout .lake mathlib'), lw(read('b567_cache_nobuild.txt'), 'CONTROL')[:160]),
     '        Bulka : bodies %d of %d agreeing, LICENSE %s ; %s' % (BV['agree'], BV['total'], BV['licence'], lw(read('b567_bulka_delete.txt'), 'END ')),
     '    component 3 : %s' % lw(read('b567_e0_residue.txt'), 'THE GATE:')[:200],
     '        THE_RESIDUE_OF_RH.md :%s (the discharge line) ; the §7 reading FINDINGS :%s' % (RLJ.get('line'), SJ.get('line')),
     '    component 4 : %s' % lw(read('b567_e0_chi.txt'), 'THE GATE:')[:200],
     '        ZetaBounds` consumers %d of %d, every analogue present %s' % (len(ZB['consumed']), ZB['total'], ZB['complete']),
     '    the kernel : main = v0.10 = %s (tag object %s), read back at the remote before the tag ; residue-discharge-b567 %s and'
     ' grh-weil-b567 %s pushed by name ; existing .lean files modified %s' % (K['v010'][:7], K['v010obj'][:7], K['res'][:7], K['grh'][:7],
                                                                             SC.get('edited_lean') or 'NONE'),
     '    the ledger lines : FINDINGS :%s (entry) ; OPEN_TRAILS :%s (record) ; rows %s' % (FND['heading_line'], TR['line'],
                                                                                      ', '.join('%s exit %s' % (r['row'], r['exit']) for r in RW['rows'])),
     '    the rowgen diff : %s' % ' ; '.join(l.strip() for l in read('b567_rowgen.txt').split(NL) if l.strip().startswith("('")),
     '    the branches : %s' % ' ; '.join(l for l in read('b567_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits'
                             % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    H18a %s ; H18b %s ; H18c %s' % (W('h18a'), W('h18b'), W('h18c')),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s (N7) %s ; (S1) %s (S2) %s (S3) %s' % tuple(
         W(k) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b567_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES.',
     '    pre-push : %s' % lw(read('b567_checks.txt'), 'ARMS RUN :'),
     '    pre-push : %s' % lw(read('b567_checks.txt'), 'VERDICT :'),
     '    post-push : %s' % lw(read('b567_checks_postpush.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b567_checks_postpush.txt'), 'VERDICT :')]
for nm in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-effects',
           'SIDE-silence-principle', 'SIDE-compression', 'SIDE-structural-error-correction', 'SIDE-cosmo'):
    p = ROOT if nm == 'relay' else (PP if nm == 'PLACE-papers' else os.path.join('D:', os.sep, nm))
    loc, rem = git(p, 'rev-parse', 'main'), (git(p, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    L.append('      %-28s main %s ; remote %s ; %s' % (nm, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
for b, note in (('detection-region-b559', 'HELD, kept'), ('li-weil-b561', 'kept'), ('grh-weil-b562', 'kept'), ('li-weil-b563', 'kept'),
                ('grh-weil-b564', 'kept'), ('vendor-bulka-backport-b566', 'kept as data'), ('vendor-bulka-forward-b566', 'kept'),
                ('residue-discharge-b567', 'Component 3, kept'), ('grh-weil-b567', 'Component 4, = main')):
    bl, brm = git(EF, 'rev-parse', b), (git(EF, 'ls-remote', 'origin', 'refs/heads/' + b).split() or [''])[0]
    L.append('      %-28s local %s ; remote %s ; %s (%s)' % (b, bl[:12], brm[:12], 'AGREE' if bl == brm else 'DISAGREE', note))
tg, trm = git(EF, 'rev-parse', 'v0.10^{}'), (git(EF, 'ls-remote', 'origin', 'refs/tags/v0.10^{}').split() or [''])[0]
L.append('      %-28s peeled %s ; remote %s ; %s' % ('v0.10', tg[:12], trm[:12], 'AGREE' if tg == trm else 'DISAGREE'))
L += ['    censuses : %s / %s' % (lw(read('b567_census_closing.txt'), 'TOTAL MISSING'), lw(read('b567_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b567_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '    the clones : D:/audit-b565/bulka %s ; the old build tree aside at D:/b567-lake-51e6992e %s (not deleted: no ruling orders it) ;'
      ' the worktree D:/b566-forward KEPT (its .lake moved to the checkout)' % ('ABSENT' if not os.path.exists('D:/audit-b565/bulka') else '### PRESENT',
                                                                                'PRESENT' if os.path.isdir('D:/b567-lake-51e6992e') else 'ABSENT'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT, (R177)(7)**: lane three opens for the ζ-leg alongside GRH-Weil -- CP-4, the page without narrative, the',
      '        ceiling as its last derived line; the author rules on the closing.',
      '    (b) GRH-WEIL: EF_lit_chi is STATED and HELD at its proof. The next ζ-specific input in Zeta23`s order is RvM/ZetaGrowth (the',
      '        growth of ζ in vertical strips); the χ-analogues of the three ZetaBounds names it consumes are now compiled.',
      '    (c) The residue chain: liCriterion discharged at λ := LiCoeff; inequalityToPositivity stays the bridge`s last item.',
      '    (d) ### **FOR THE AUTHOR**: b566`s suite, re-run on b566`s push after the addendum forms, reads 72 of 74 -- its two defect arms',
      '        clear, two other arms (G-NUMBER-UNCLAIMED, G-PEEK-DECLARED) fail because b567 exists; neither was edited.',
      '    (e) ### **FOR THE AUTHOR**: the old build tree D:/b567-lake-51e6992e (Mathlib 51e6992e) is kept aside, unordered either way.',
      '    (f) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping if it changed.',
      '=' * 104]
io.open(os.path.join(D, 'b567_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
