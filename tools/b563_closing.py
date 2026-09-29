# -*- coding: utf-8 -*-
"""b563_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b563_*` and `relay/tools/b563_*` file, the PLACE-papers
### documents this act writes, CORRESPONDENCE.md, the new kernel module and its axiom-check file at main, and the patch and
### message of every commit of this act (subject beginning `b563`, or housekeeping naming (R173) or b563) in five
### repositories, plus any uncommitted change. Carried from b562_closing.py and re-pointed.
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
    return subject.startswith('b563') or (subject.startswith('housekeeping:') and ('(R173)' in subject or 'b563' in subject))


def tokenscan():
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    if not t:
        res = dict(set=False)
    else:
        files = sorted(set(glob.glob(os.path.join(D, 'b563_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b563_*')) + FILES))
        files = [f for f in files if os.path.isfile(f) and not f.endswith('b563_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        mods = ('SIDEExplicitFormula/LiWeilSym.lean', 'AxiomCheckLiWeilSym.lean')
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
    io.open(os.path.join(D, 'b563_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
J = lambda n: json.loads(read(n))
SC, E0, FND, TR, WO, RW, PN, SUP, DA, BL, AJ = (J('b563_%s.json' % n) for n in (
    'scores', 'e0', 'findings', 'trail', 'workorder', 'rows', 'per_n', 'supline', 'defect_a_line', 'b562_lines', 'findsup_after'))
PT = {x: J('b563_%s.json' % x) for x in ('D1', 'D2', 'stmt', 'D3', 'D4')}
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
v07 = git(EF, 'rev-parse', 'v0.7^{}')
ratios = [r['ratio'] for r in PN['rows'] if r['classical']]
L = ['=' * 104, 'b563 -- THE CLOSING RECORD. ### **LANE TWO, ACT FIVE: THE LI-WEIL BRIDGE AT THE SYMMETRIC FAMILY, UNDER (R173).**', '=' * 104,
     '    the supersession form : terminal_table.py %s (the file alone) ; the line FINDINGS :%s ; CONFLICT %d -> %d ; grades changed %s'
     % (git(ROOT, 'rev-parse', '--short', '348a115d'), SUP['line'], len(AJ['conflict_before']), len(AJ['conflict_after']), AJ['changed'] or 'NONE'),
     '    the table : %s' % lw(read('b563_checks_postpush.txt'), 'the regenerated table`s line for li_identity_of_exchange'),
     '    at the b562 record : OPEN_TRAILS :%s (defect (a)) :%s (H13b) :%s (H13a)' % (DA['line'], BL['h13b']['line'], BL['h13a']['line']),
     '    the per-n re-score (FROM b562`S BANK ALONE) : H15d %s ; misses %s ; |Z(n,0) - lambda_n|/floor %.3f .. %.3f at the classical n'
     % (W(PN['h15d']), PN['misses'] or 'NONE', min(ratios), max(ratios)),
     '    the decay read (before any build) : H15a %s' % W(SC['h15a']),
     '    the kernel : %s ; every print std3 %s' % (' ; '.join('%s %d decls' % (x, len(PT[x]['names'])) for x in PT),
                                                  all(PT[x]['all_std3'] for x in PT)),
     '    the E0 read : %d DERIVES, %d INTERFACES (exchange_of_bound, on SymPairBound, discharged), %d definitions ; the salt-check %s ; the gate %s' % (
         sum(1 for r in E0['rows'].values() if r['grade'] == 'DERIVES'), sum(1 for r in E0['rows'].values() if r['grade'] == 'INTERFACES'),
         sum(1 for r in E0['rows'].values() if r['grade'] == 'DEF'), E0['salt'], E0['gate']),
     '    v0.7 : object %s peeled %s (remote %s) = main %s = li-weil-b563 %s ; pushed by push_gated.sh after main read back' % (
         git(EF, 'rev-parse', '--short', 'v0.7'), v07[:7], (git(EF, 'ls-remote', 'origin', 'refs/tags/v0.7^{}').split() or [''])[0][:7],
         git(EF, 'rev-parse', '--short', 'main'), git(EF, 'rev-parse', '--short', 'li-weil-b563')),
     '    the ledger lines : FINDINGS :%s (supersession) :%s (entry) ; OPEN_TRAILS :%s (work-order) :%s (record) ; row 399 exit %d'
     % (SUP['line'], FND['heading_line'], WO['line'], TR['line'], RW['exit_act']),
     '    the branches : %s' % ' ; '.join(l for l in read('b563_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    H15a %s ; H15b %s ; H15c %s ; H15d %s' % tuple(W(SC[k]) for k in ('h15a', 'h15b', 'h15c', 'h15d')),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s' % tuple(
         W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b563_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES.',
     '    pre-push : %s (the first pre-push run NOT CLEAN, 78 of 80, defect (e))' % lw(read('b563_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b563_checks_postpush.txt'), 'ARMS RUN :')]
for nm in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-effects', 'SIDE-silence-principle',
           'SIDE-compression', 'SIDE-structural-error-correction', 'SIDE-cosmo'):
    p = ROOT if nm == 'relay' else (PP if nm == 'PLACE-papers' else os.path.join('D:', os.sep, nm))
    loc, rem = git(p, 'rev-parse', 'main'), (git(p, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    L.append('      %-28s main %s ; remote %s ; %s' % (nm, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
for b, note in (('detection-region-b559', 'HELD, kept'), ('li-weil-b561', 'kept'), ('grh-weil-b562', 'kept'), ('li-weil-b563', 'pushed by name, kept')):
    bl, brm = git(EF, 'rev-parse', b), (git(EF, 'ls-remote', 'origin', 'refs/heads/' + b).split() or [''])[0]
    L.append('      %-28s local %s ; remote %s ; %s (%s)' % (b, bl[:12], brm[:12], 'AGREE' if bl == brm else 'DISAGREE', note))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b563_census_closing.txt'), 'TOTAL MISSING'), lw(read('b563_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b563_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT, (R173)(7)**: GRH-WEIL act two -- the 38 generic Zeta23 modules re-instantiated for L(s, chi), staged',
      '        by import order, held at the earliest zeta-specific dependency.',
      '    (b) ### **FOR THE AUTHOR**: li_identity_of_exchange still reads CONFLICT. The FINDINGS supersession removed FINDINGS :6048`s',
      '        cell, but b562`s own trail line at OPEN_TRAILS :11577 is read by the table as two cells (a compound and a plain one),',
      '        and row 397 grades SHELL. A trail-line supersession for :11577 (the b554 form) would clear it; it is not written here.',
      '    (c) ### **THE BRIDGE`S IDENTITY SIDE IS CLOSED IN LIMIT FORM** at v0.7 (li_identity_sym, no premise). The work-order`s',
      '        positivity side (the sign of the Li coefficients) is not attempted.',
      '    (d) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping if it changed.',
      '=' * 104]
io.open(os.path.join(D, 'b563_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
