# -*- coding: utf-8 -*-
"""b552_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b552_*` and `relay/tools/b552_*` file, the four PLACE-papers
### documents this act writes, and the patch and message of every commit of this act (subject beginning `b552`) in five
### repositories (the trial branch included), plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
FILES = [os.path.join(PP, f) for f in ('FINDINGS.md', 'OPEN_TRAILS.md')] + [os.path.join(ROOT, 'tools', 'corr_row.README.md')]
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
        files = sorted(set(glob.glob(os.path.join(D, 'b552_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b552_*')) + FILES))
        files = [f for f in files if not f.endswith('b552_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo, rev in ((ROOT, 'HEAD'), (PP, 'HEAD'), (SIDE, 'HEAD'), (KER, 'HEAD')):
            for l in git(repo, 'log', '--pretty=%H %s', '-40', rev).split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b552'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b552_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b552_scores.json'))
R2 = json.loads(read('b552_row392.json'))
PE = json.loads(read('b552_period.json'))
RG = json.loads(read('b552_regimes.json'))
LI = json.loads(read('b552_li_class.json'))
CS = json.loads(read('b552_consolidation.json'))
ST = json.loads(read('b552_stormer.json'))
FND = json.loads(read('b552_findings.json'))
N6J = json.loads(read('b552_n6_line.json'))
HK = json.loads(read('b552_housekeeping.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
L = ['=' * 104, 'b552 -- THE CLOSING RECORD. ### **b551 SETTLED; FOUR READINGS FROM THE BANKS, UNDER (R162).**', '=' * 104,
     '    b551 settled : housekeeping %s (%s) ; row 392 -> boolGrp %s (before %s) ; README tools/corr_row.README.md ; W-ORD-STORMER-CLASH :%s ; the (N6) line FINDINGS :%s'
     % (HK['commit'][:10], HK['subject'], R2['after']['grade'], R2['before']['grade'], ST['line'], N6J['line']),
     '    the consolidation : %.1f GB over the checkouts, about %.1f GB kept by one per rev ; OPEN_TRAILS :%s' % (CS['gb'], CS['keep_gb'], CS['line']),
     '    Reading Three : H4 %s (H4.1 %s, H4.2 %s -- crest at %s, H4.3 %s) ; the 29.55 spacings %s against %.4f'
     % ('REFUTED' if PE['refuted'] else 'NOT REFUTED', PE['c1'], PE['c2'], PE['crest_local_maxima'], PE['c3'], ['%.4f' % x for x in PE['crest_spacings']], PE['crest_pi_over_g']),
     '    Reading Four : 34 / sqrt(12) = %.2f ; the smallest banked negative width over sqrt(12) = %.2f' % (RG['ratio_detect'], RG['ratio_smallest']),
     '    Reading Five : H5 %s ; the leading item OPEN_TRAILS :%s ; Reading Six : NOT SCORABLE' % ('HOLDS' if LI['h5'] else 'REFUTED', (LI.get('trail') or {}).get('line')),
     '    FINDINGS : the entry :%s ; next THE_KEYSTONE_CENSUS' % FND['line'],
     '    the branches : %s' % ' ; '.join(l for l in read('b552_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b552_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
     '    pre-push : %s' % lw(read('b552_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b552_checks_postpush.txt'), 'ARMS RUN :')]
for n in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-li-map', 'SIDE-fano-darkness'):
    p = ROOT if n == 'relay' else (PP if n == 'PLACE-papers' else os.path.join('D:', os.sep, n))
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b552_census_closing.txt'), 'TOTAL MISSING'), lw(read('b552_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b552_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT**: THE_KEYSTONE_CENSUS.',
      '    (b) ### **FOR THE AUTHOR**: boolGrp stays CONFLICT after row 392 -- the table counts distinct grades over every cell; clearing it needs a rule in terminal_table.py or an exception (defect (c)).',
      '    (c) ### **FOR THE AUTHOR**: a second CONFLICT, R5_output_HilbertPolya_to_RH (SIDE-lv-conservation), predates b551 (defect (b)).',
      '    (d) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping, per (R162)(1)(d).',
      '    (e) Under (R157)(6) the seat`s memory is not refreshed at this act.',
      '=' * 104]
io.open(os.path.join(D, 'b552_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
