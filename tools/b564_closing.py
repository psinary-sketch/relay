# -*- coding: utf-8 -*-
"""b564_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b564_*` and `relay/tools/b564_*` file, the PLACE-papers
### documents this act writes, CORRESPONDENCE.md, the new kernel files at main, and the patch and
### message of every commit of this act (subject beginning `b564`, or housekeeping naming (R174) or b564) in five
### repositories, plus any uncommitted change. Carried from b563_closing.py and re-pointed.
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


FILES = [os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md'), os.path.join(PP, 'README.md'),
         os.path.join(PP, 'REGISTRY.md'), os.path.join(SIDE, 'CORRESPONDENCE.md')]


def lw(t, n):
    return next((l.strip() for l in t.split(NL) if n in l), '')


def git(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def git_bytes(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True).stdout


def ours(subject):
    return subject.startswith('b564') or (subject.startswith('housekeeping:') and ('(R174)' in subject or 'b564' in subject))


def tokenscan():
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    if not t:
        res = dict(set=False)
    else:
        files = sorted(set(glob.glob(os.path.join(D, 'b564_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b564_*')) + FILES))
        files = [f for f in files if os.path.isfile(f) and not f.endswith('b564_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        mods = ('SIDEExplicitFormula/Chi/ZeroConfig.lean', 'SIDEExplicitFormula/Chi/Generic.lean', 'SIDEExplicitFormula/Chi/ZetaBounds.lean',
                'AxiomCheckChi.lean')
        for m in mods:
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
        res = dict(set=True, files_scanned=len(files) + len(mods), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b564_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
J = lambda n: json.loads(read(n))
SC, E0, FND, TR, WO, RW, SUP, TA, CE, FA, CV, DG = (J('b564_%s.json' % n) for n in (
    'scores', 'e0', 'findings', 'trail', 'workorder', 'rows', 'supline', 'trailsup_after', 'ceiling', 'fieldappend', 'converse_price', 'dag'))
PT = {x: J('b564_%s.json' % x) for x in ('a', 'b', 'c1')}
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
v08 = git(EF, 'rev-parse', 'v0.8^{}')
L = ['=' * 104, 'b564 -- THE CLOSING RECORD. ### **LANE TWO, ACT SIX: GRH-WEIL ACT TWO, UNDER (R174).**', '=' * 104,
     '    the ceiling : the author`s sentence at README :%s and REGISTRY :%s ; b563 at its weight at FINDINGS :%s'
     % (CE['files']['README.md']['new_line'], CE['files']['REGISTRY.md']['new_line'], FND['weight']['heading_line']),
     '    the conflict : the trail-line supersession at OPEN_TRAILS :%s ; CONFLICT %d -> %d ; grades changed %s'
     % (SUP['line'], len(TA['conflict_committed']), len(TA['conflict_regenerated']), TA['changed']),
     '    the table : %s' % lw(read('b564_checks_postpush.txt'), 'the regenerated table`s line for li_identity_of_exchange'),
     '    prior art : (N2) %s -- Mathlib and Zeta23 none ; two public Lean developments (Li`s criterion both ways ; the Bombieri-Lagarias'
     ' explicit formula) ; the field entry at FINDINGS :%s' % (W(SC['n2']), FA['line']),
     '    the converse : (V1) compiled, (V2) (V3) one lemma each, (V4) absent ; H16d %s ; OPEN_TRAILS :%s (price) :%s (pointer)'
     % (W(SC['h16d']), CV['appends']['workorder']['line'], CV['appends']['pointer']['line']),
     '    the frontier : %s ; H16c %s' % (' -> '.join('%s (%s)' % (f['module'], f['kind']) for f in DG['frontier']), W(SC['h16c'])),
     '    the kernel : %s' % ' ; '.join('part (%s) %d decls, closed at attempt %d' % (x, len(PT[x]['rows']), len(PT[x]['attempts'])) for x in PT),
     '    the E0 read : %d DERIVES, %d INTERFACES (each on a premise its vendored module names), %d definitions ; the salt-check %s ; the gate %s' % (
         sum(1 for r in E0['rows'].values() if r['grade'] == 'DERIVES'), sum(1 for r in E0['rows'].values() if r['grade'] == 'INTERFACES'),
         sum(1 for r in E0['rows'].values() if r['grade'] == 'DEF'), E0['salt'], E0['gate']),
     '    H16a %s (re-classified %d: %s) ; H16b %s' % (W(SC['h16a']), len(PT['b']['reclassified']), ', '.join(PT['b']['reclassified']), W(SC['h16b'])),
     '    the held point : %s (%s)' % (PT['c1']['held_at'], PT['c1']['kind']),
     '    v0.8 : object %s peeled %s (remote %s) = main %s = grh-weil-b564 %s ; pushed by push_gated.sh after main read back' % (
         git(EF, 'rev-parse', '--short', 'v0.8'), v08[:7], (git(EF, 'ls-remote', 'origin', 'refs/tags/v0.8^{}').split() or [''])[0][:7],
         git(EF, 'rev-parse', '--short', 'main'), git(EF, 'rev-parse', '--short', 'grh-weil-b564')),
     '    the ledger lines : FINDINGS :%s (weight) :%s (entry) ; OPEN_TRAILS :%s (work-order) :%s (record) ; row 400 exit %d'
     % (FND['weight']['heading_line'], FND['entry']['heading_line'], WO['line'], TR['line'], RW['exit_act']),
     '    the branches : %s' % ' ; '.join(l for l in read('b564_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    H16a %s ; H16b %s ; H16c %s ; H16d %s' % tuple(W(SC[k]) for k in ('h16a', 'h16b', 'h16c', 'h16d')),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s (N7) %s ; (S1) %s (S2) %s (S3) %s' % tuple(
         W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b564_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES.',
     '    pre-push : %s' % lw(read('b564_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b564_checks_postpush.txt'), 'ARMS RUN :')]
for nm in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-effects', 'SIDE-silence-principle',
           'SIDE-compression', 'SIDE-structural-error-correction', 'SIDE-cosmo'):
    p = ROOT if nm == 'relay' else (PP if nm == 'PLACE-papers' else os.path.join('D:', os.sep, nm))
    loc, rem = git(p, 'rev-parse', 'main'), (git(p, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    L.append('      %-28s main %s ; remote %s ; %s' % (nm, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
for b, note in (('detection-region-b559', 'HELD, kept'), ('li-weil-b561', 'kept'), ('grh-weil-b562', 'kept'), ('li-weil-b563', 'kept'),
                ('grh-weil-b564', 'pushed by name, kept')):
    bl, brm = git(EF, 'rev-parse', b), (git(EF, 'ls-remote', 'origin', 'refs/heads/' + b).split() or [''])[0]
    L.append('      %-28s local %s ; remote %s ; %s (%s)' % (b, bl[:12], brm[:12], 'AGREE' if bl == brm else 'DISAGREE', note))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b564_census_closing.txt'), 'TOTAL MISSING'), lw(read('b564_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b564_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT, (R174)(7)**: the frontier is held at ZetaBounds`s analogue of HasDerivAtZeta0, on the growth side,',
      '        not at an archimedean fact; by the ruling`s words GRH-WEIL act three at the frontier -- the author rules on the closing.',
      '    (b) ### **FOR THE AUTHOR**: li_identity_of_exchange now reads row 397`s cell alone, SHELL; the ruling`s words on the line',
      '        are T2-INTERFACES-on-false-premise, which the table does not read as a cell. Whether the table`s SHELL stands is the',
      '        author`s.',
      '    (c) ### **FOR THE AUTHOR**: two public Lean developments formalize Li`s criterion (both directions) and the Bombieri-Lagarias',
      '        explicit formula (FINDINGS :%s). The ceiling sentence entered this act says the converse is T1-lit; a public' % FA['line'],
      '        formalization of it now exists outside this programme, read and not built here.',
      '    (d) The generic instantiations carrying a vendored premise (TailHyp, EF_lit, PaperInputs, ...) are statements conditional on',
      '        those premises for chi; nothing here proves them for chi.',
      '    (e) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping if it changed.',
      '=' * 104]
io.open(os.path.join(D, 'b564_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
