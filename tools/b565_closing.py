# -*- coding: utf-8 -*-
"""b565_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b565_*` and `relay/tools/b565_*` file, the PLACE-papers
### documents this act writes, CORRESPONDENCE.md, and the patch and message of every commit of this act (subject beginning
### `b565`, or housekeeping naming (R175) or b565) in four repositories, plus any uncommitted change. Carried from
### b564_closing.py and re-pointed. This file deletes nothing.
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


FILES = [os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md'), os.path.join(SIDE, 'CORRESPONDENCE.md')]


def lw(t, n):
    return next((l.strip() for l in t.split(NL) if n in l), '')


def git(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout.strip()


def git_bytes(r, *a):
    return subprocess.run(['git', '-C', r] + list(a), capture_output=True).stdout


def ours(subject):
    return subject.startswith('b565') or (subject.startswith('housekeeping:') and ('(R175)' in subject or 'b565' in subject))


def tokenscan():
    t = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    if not t:
        res = dict(set=False)
    else:
        files = sorted(set(glob.glob(os.path.join(D, 'b565_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b565_*')) + FILES))
        files = [f for f in files if os.path.isfile(f) and not f.endswith('b565_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo, rev in ((ROOT, 'HEAD'), (PP, 'HEAD'), (SIDE, 'HEAD'), (EF, 'main')):
            for l in git(repo, 'log', '--pretty=%H %s', '-40', rev).split(NL):
                if l.strip() and ours(l.split(' ', 1)[-1]):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b565_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
J = lambda n: json.loads(read(n))
SC, AU, FND, TR, CJ, FA, RW, SR, SA = (J('b565_%s.json' % n) for n in (
    'scores', 'audit', 'findings', 'trail', 'conditional', 'fieldline', 'rows', 'suprow', 'supersede_after'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
B, A = AU['bulka'], AU['arda']
grades = lambda r: ', '.join('%s %s' % (n.split('.')[-1], t['grade']) for n, t in r['rows'].items())
L = ['=' * 104, 'b565 -- THE CLOSING RECORD. ### **THE AUDIT OF TWO PUBLIC FORMALIZATIONS, UNDER (R175).**', '=' * 104,
     '    housekeeping : b564`s push output committed alone (80346ab6) ; push_gated.sh`s capture (9de84b16) ; FERRY_STANDING A4 ;'
     ' SUITE_README.md ; this act`s pushes captured to data/b565_push_out.txt and data/b565_relay_push_out.txt',
     '    the superseded grade : the synonym entry (7a2defb1) ; row 401 at CORRESPONDENCE :%s ; CONFLICT %d -> %d ; grades changed %s'
     % (SR.get('line'), len(SA['conflict_committed']), len(SA['conflict_regenerated']), SA['changed']),
     '    the table : %s' % lw(read('b565_checks_postpush.txt'), 'the regenerated table`s line for li_identity_of_exchange')[:220],
     '    Bulka : %s @%s (HEAD committed %s) ; %d modules built, every exit %d ; closure %d modules sorry %d axioms %s'
     % (B['url'], B['head'][:8], B['head_date'], B['build_modules'], B['build_exit'], B['closure_modules'], B['sorry']['sorry'], B['sorry']['axioms'] or 0),
     '        grades : %s' % grades(B),
     '    Arda : %s @%s (HEAD committed %s) ; %d modules built, every exit %d ; closure %d + Zeta23 %d modules sorry %d axioms %s'
     % (A['url'], A['head'][:8], A['head_date'], A['build_modules'], A['build_exit'], A['closure_modules'], A['zeta23_modules'],
        A['sorry']['sorry'], A['sorry']['axioms'] or 0),
     '        grades : %s' % grades(A),
     '    the prints : %d of %d audited terminals at [propext, Classical.choice, Quot.sound]' % (AU['std3_count'], AU['terminal_count']),
     '    the comparisons : Bulka`s forward direction vs rh_imp_li_nonneg %s ; Arda`s bl_explicit_formula vs li_identity_sym %s'
     % (AU['comparisons']['bulka_vs_fwd']['word'], AU['comparisons']['arda_vs_sym']['word']),
     '    the Zeta23 pins : ours v1.0 = 3635e748 (every vendored body the v1.0 file: %d of %d), Arda`s fbdc36bb : %d identical, %d in a'
     ' header comment alone, code differing %s -> no pin-refresh work-order'
     % (AU['zeta23']['ours_is_v10'], AU['zeta23']['vendored'], AU['zeta23']['identical'], AU['zeta23']['comment_only'], AU['zeta23']['code_differs'] or 'NONE'),
     '    the ledger lines : FINDINGS :%s (field line) :%s (entry) ; OPEN_TRAILS :%s (the (R175)(3) conditional) :%s (record) ;'
     ' rows 401 and 402 (exit %d)' % (FA['line'], FND['heading_line'], CJ['line'], TR['line'], RW['exit_act']),
     '    the branches : %s' % ' ; '.join(l for l in read('b565_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits'
                             % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    H17a %s ; H17b %s' % (W(SC['h17a']), W(SC['h17b'])),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s' % tuple(
         W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b565_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES.',
     '    pre-push : %s' % lw(read('b565_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b565_checks_postpush.txt'), 'ARMS RUN :')]
for nm in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-effects',
           'SIDE-silence-principle', 'SIDE-compression', 'SIDE-structural-error-correction', 'SIDE-cosmo'):
    p = ROOT if nm == 'relay' else (PP if nm == 'PLACE-papers' else os.path.join('D:', os.sep, nm))
    loc, rem = git(p, 'rev-parse', 'main'), (git(p, 'ls-remote', 'origin', 'refs/heads/main').split() or [''])[0]
    L.append('      %-28s main %s ; remote %s ; %s' % (nm, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
for b, note in (('detection-region-b559', 'HELD, kept'), ('li-weil-b561', 'kept'), ('grh-weil-b562', 'kept'), ('li-weil-b563', 'kept'),
                ('grh-weil-b564', 'kept')):
    bl, brm = git(EF, 'rev-parse', b), (git(EF, 'ls-remote', 'origin', 'refs/heads/' + b).split() or [''])[0]
    L.append('      %-28s local %s ; remote %s ; %s (%s)' % (b, bl[:12], brm[:12], 'AGREE' if bl == brm else 'DISAGREE', note))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'origin/main').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b565_census_closing.txt'), 'TOTAL MISSING'), lw(read('b565_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b565_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '    the clones : D:/audit-b565/bulka @%s and D:/audit-b565/arda @%s, outside the corpus, KEPT until the author`s word' % (B['head'][:8], A['head'][:8]),
      '', '### CARRIED FORWARD.',
      '    (a) ### **FOR THE AUTHOR, (R175)(3)**: H17a is REFUTED -- the Bulka converse is genuine at its pin. The conditional is at',
      '        OPEN_TRAILS :%s with both branches; the vendoring, if the word is to vendor, opens with the equality lemma (four lemmas,' % CJ['line'],
      '        one of substance: the multiplicity of ζ against that of ξ on the strip) and meets a toolchain divergence (v4.34.0-rc1 /',
      '        de5ce8a9 against the kernel`s v4.33.0-rc2 / 51e6992e).',
      '    (b) ### **THE NEXT ACT, (R175)(6)**: b566 is GRH-WEIL act three -- LFunction χ on 0 < Re s by Abel summation (H18a-H18c).',
      '    (c) The clones stay under D:/audit-b565 until the author`s word; nothing of either repository is in the corpus.',
      '    (d) The standing lines of this act (memory): Lake at these toolchains has no job cap -- one module per call, free memory',
      '        printed, held below 2.5 GB; cache fetch and unpack steps never run under a time slot.',
      '    (e) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping if it changed.',
      '=' * 104]
io.open(os.path.join(D, 'b565_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
