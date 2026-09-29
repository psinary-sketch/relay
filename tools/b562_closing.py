# -*- coding: utf-8 -*-
"""b562_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b562_*` and `relay/tools/b562_*` file, the PLACE-papers
### documents this act writes, CORRESPONDENCE.md, the new kernel module and LiWeil.lean at main, and the patch and message of
### every commit of this act (subject beginning `b562`, or housekeeping naming (R172) or b562) in five repositories, plus any
### uncommitted change. Carried from b561_closing.py and re-pointed.
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
    return subject.startswith('b562') or (subject.startswith('housekeeping:') and ('(R172)' in subject or 'b562' in subject))


def tokenscan():
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    if not t:
        res = dict(set=False)
    else:
        files = sorted(set(glob.glob(os.path.join(D, 'b562_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b562_*')) + FILES))
        files = [f for f in files if os.path.isfile(f) and not f.endswith('b562_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        mods = ('SIDEExplicitFormula/GRHWeil.lean', 'AxiomCheckGRHWeil.lean', 'SIDEExplicitFormula/LiWeil.lean')
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
    io.open(os.path.join(D, 'b562_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
J = lambda n: json.loads(read(n))
SC, E0, FND, TR, WO, RW, DJ, MJ, X2, SP = (J('b562_%s.json' % n) for n in (
    'scores', 'e0', 'findings', 'trail', 'workorders', 'rows', 'drift', 'zeta23_modules', 'x2', 'species'))
GA, GB, GC = J('b562_GRH_a.json'), J('b562_GRH_b.json'), J('b562_GRH_c.json')
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
v06 = git(EF, 'rev-parse', 'v0.6^{}')
L = ['=' * 104, 'b562 -- THE CLOSING RECORD. ### **LANE TWO, ACT FOUR: b561 AT ITS WEIGHT, THE DRIFT BENCHED, GRH-WEIL ACT ONE, UNDER (R172).**', '=' * 104,
     '    b561 at its weight : docstring commits %s ; %s ; row %s SUPERSEDES row 395: T2 (exit %d) ; the species entry FINDINGS :%s'
     % (', '.join(c[:7] for c in ('3968ae7', '61e3551')), lw(read('b562_doc_push.txt'), 'diff lines'), '397', RW['exit_sup'], SP['line']),
     '    the table : %s' % lw(read('b562_checks_postpush.txt'), 'the regenerated table`s line for li_identity_of_exchange'),
     '    the drift (A MEASUREMENT AT xi) : N %d ; H13a %s ; symmetric max |D| %s ; b3 within floor %s ; %.1f s' % (
         DJ['N'], W(DJ['h13a_holds']), DJ['sym_max'], DJ['b3'], DJ['secs']),
     '    (X2) filed : OPEN_TRAILS :%s' % X2['line'],
     '    GRH-WEIL act one : (a) %d decls, attempts %d ; (b) %d, attempts %d ; (c) %d, attempts %d ; every print std3 %s' % (
         len(GA['names']), GA['attempts'], len(GB['names']), GB['attempts'], len(GC['names']), GC['attempts'],
         GA['all_std3'] and GB['all_std3'] and GC['all_std3']),
     '    the E0 read : %d of %d DERIVES, %d definitions ; the salt-check %s ; the gate %s' % (
         sum(1 for r in E0['rows'].values() if r['grade'] == 'DERIVES'), len(E0['rows']),
         sum(1 for r in E0['rows'].values() if r['grade'] == 'DEF'), E0['salt'], E0['gate']),
     '    the Zeta23 files : %d classified, %d GENERIC' % (MJ['files'], MJ['generic']),
     '    v0.6 : object %s peeled %s (remote %s) = main %s = grh-weil-b562 %s ; pushed by push_gated.sh after main read back' % (
         git(EF, 'rev-parse', '--short', 'v0.6'), v06[:7], (git(EF, 'ls-remote', 'origin', 'refs/tags/v0.6^{}').split() or [''])[0][:7],
         git(EF, 'rev-parse', '--short', 'main'), git(EF, 'rev-parse', '--short', 'grh-weil-b562')),
     '    the ledger lines : FINDINGS :%s (species) :%s (entry) ; OPEN_TRAILS :%s ((X2)) :%s (work-order) :%s (record) ; rows 397 398 exit %d %d'
     % (SP['line'], FND['heading_line'], X2['line'], WO['line'], TR['line'], RW['exit_sup'], RW['exit_act']),
     '    the branches : %s' % ' ; '.join(l for l in read('b562_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    H13a %s ; H13b %s ; H14a %s ; H14b %s ; H14c %s ; H14d %s' % tuple(W(SC[k]) for k in ('h13a', 'h13b', 'h14a', 'h14b', 'h14c', 'h14d')),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s (N7) %s ; (S1) %s (S2) %s (S3) %s' % tuple(
         W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b562_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES.',
     '    pre-push : %s' % lw(read('b562_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b562_checks_postpush.txt'), 'ARMS RUN :')]
for nm in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-effects', 'SIDE-silence-principle',
           'SIDE-compression', 'SIDE-structural-error-correction', 'SIDE-cosmo'):
    p = ROOT if nm == 'relay' else (PP if nm == 'PLACE-papers' else os.path.join('D:', os.sep, nm))
    loc, rem = git(p, 'rev-parse', 'main'), (git(p, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    L.append('      %-28s main %s ; remote %s ; %s' % (nm, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
for b, note in (('detection-region-b559', 'HELD, kept'), ('li-weil-b561', 'kept'), ('grh-weil-b562', 'pushed by name, kept')):
    bl, brm = git(EF, 'rev-parse', b), (git(EF, 'ls-remote', 'origin', 'refs/heads/' + b).split() or [''])[0]
    L.append('      %-28s local %s ; remote %s ; %s (%s)' % (b, bl[:12], brm[:12], 'AGREE' if bl == brm else 'DISAGREE', note))
L.append('      %-28s local [%s] ; remote [%s] (absent at the remote; its deletion recorded as done at b561, by inference)' % (
    'li-weil-b560', git(EF, 'branch', '--list', 'li-weil-b560'), git(EF, 'ls-remote', 'origin', 'refs/heads/li-weil-b560')))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b562_census_closing.txt'), 'TOTAL MISSING'), lw(read('b562_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b562_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT, (R172)(7)**: H13b is REFUTED, so the bridge`s (X1) comes next: the explicit formula on a class',
      '        containing the midpoint-normalised jump. After it, GRH-WEIL`s second act (the chi-explicit formula, priced by the module count).',
      '    (b) ### **FOR THE AUTHOR**: after row 397 the table reads CONFLICT (INTERFACES / SHELL) for li_identity_of_exchange, not',
      '        SHELL. b560`s FINDINGS entry at :6048 grades it INTERFACES, and the supersession form reaches no FINDINGS line (defect (f)).',
      '    (c) ### **FOR THE AUTHOR**: H14d is REFUTED. 38 of the 57 Zeta23 files are GENERIC by the face`s lexical rule, so',
      '        GRH-WEIL`s second act re-uses more than the threshold assumed. The rule`s limit is printed in its bank.',
      '    (d) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping if it changed.',
      '=' * 104]
io.open(os.path.join(D, 'b562_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
