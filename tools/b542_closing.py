# -*- coding: utf-8 -*-
"""b542_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b542_*` and `relay/tools/b542_*` file, the three PLACE-papers
### documents this act writes, the correspondence ledger, and the patch and message of every commit of this act (subject beginning
### `b542`) in four repositories, plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
FILES = [os.path.join(PP, f) for f in ('ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md')] + [os.path.join(SIDE, 'CORRESPONDENCE.md')]
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
        files = sorted(set(glob.glob(os.path.join(D, 'b542_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b542_*')) + FILES))
        files = [f for f in files if not f.endswith('b542_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b542'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        push_logs = sorted(os.path.basename(f) for f in files if os.path.basename(f).startswith('b542_push'))
        warnings = [f for f in push_logs if b'WARNING' in open(os.path.join(D, f), 'rb').read()]
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()),
                   push_logs=push_logs, warnings=warnings)
    io.open(os.path.join(D, 'b542_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b542_scores.json'))
FJ = json.loads(read('b542_file.json'))
CJ = json.loads(read('b542_census.json'))
DJ = json.loads(read('b542_dichotomy.json'))
PJ = json.loads(read('b542_probe.json'))
RJ = json.loads(read('b542_rows.json'))
W = lambda v: 'HELD' if v else 'REFUTED'
K = CJ['kinds']
L = ['=' * 104, 'b542 -- THE CLOSING RECORD. ### **E-2026-09-25-5 FILED; THE INHERITANCE CENSUS, UNDER (R152).**', '=' * 104,
     '    E-2026-09-25-5 : FILED at ERRATA.md:%d-%d ; DEPOSIT-FACING bullet at :%d ; backticks %d, outside code spans %d ; kind words in the heading %s'
     % (FJ['entry_lines'][0], FJ['entry_lines'][1], FJ['bullet_line'], FJ['backticks'], FJ['backticks_outside_code'], FJ['heading_kind_words']),
     '    the census : %d repositories ; %d declarations ; %d candidates ; %d residue ; %d rows -- INHERITS %d ; FORCES %d ; BOTH %d ; NEITHER %d'
     % (len(CJ['pins']), CJ['run4']['decls'], CJ['candidates'], len(CJ['residue']), len(CJ['rows']), K['INHERITS'], K['FORCES'], K['BOTH'], K['NEITHER']),
     '      lineage : run 4 equals the third pre-seal probe row for row %s (digest %s)' % (CJ['lineage_equal'], CJ['run4']['digest'][:12]),
     '      INHERITS : %s' % [(r['repo'], r['file'], r['line'], r['name']) for r in CJ['rows'] if r['kind'] == 'INHERITS'],
     '      FORCES   : %s' % [(r['repo'], r['file'], r['line'], r['name']) for r in CJ['rows'] if r['kind'] == 'FORCES'],
     '    the dichotomy : one constraint in both columns only at %s, its INHERITS side NEITHER (PREM) ; the stop : %s'
     % ([d['cls'] for d in DJ['table'] if d['same_constraint']], DJ['stop_fired'] or 'NOT FIRED'),
     '    the axiom probe : exit %d ; %s' % (PJ['exit'], PJ['profiles']),
     '    Correspondence rows : %s' % [(r['number'], r['name'], r['exit']) for r in RJ['rows']],
     '    the branches : %s' % ' ; '.join(l for l in read('b542_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else
                           'hits %s over %s files, %s commits and %s push logs ; limb WARNINGs %s'
                           % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'], len(TK['push_logs']), TK['warnings'] or 'NONE')),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s ; (S1) %s (S2) %s (S3) %s'
     % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [
     l for l in read('b542_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
     '    pre-push, first run (committed) : %s' % lw(read('b542_checks.txt'), 'ARMS RUN :'),
     '    pre-push, after the repair of (g) : 63 of 63 on the console, its bytes overwritten by the post-push run (defect (h))',
     '    post-push : %s' % lw(read('b542_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE), ('SIDE-explicit-formula', KER),
             ('SIDE-kernel', os.path.join('D:', os.sep, 'SIDE-kernel')), ('SIDE-lv-conservation', os.path.join('D:', os.sep, 'SIDE-lv-conservation'))):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    censuses : %s / %s' % (lw(read('b542_census_closing.txt'), 'TOTAL MISSING'), lw(read('b542_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b542_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **FOR THE AUTHOR**: FINDINGS.md:1109 carries a declaration name that only TECHNE-Core holds (no public repository of',
      '        the census declares it); the line entered FINDINGS through b143`s archival split (commit 3263767) from earlier text. The name',
      '        is withheld here under (R152)(3); whether the line stays is the author`s to rule.',
      '    (b) (N3) is REFUTED on two clauses: lv-conservation holds no reflection field (its seven couplings are predicates on Phi, not',
      '        on zeros), and ZetaSeam.one_le_mult_holds is an INHERITS row that is not a reflection or conjugation fact.',
      '    (c) ### **THE NEXT ACT**: the monograph read`s second act, Chapter 26 to the end with §27.3, read with this census in hand',
      '        ((R152)(5)); then BALANCE_AND_POSITIVITY.',
      '=' * 104]
io.open(os.path.join(D, 'b542_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
