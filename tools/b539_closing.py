# -*- coding: utf-8 -*-
"""b539_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b539_*` and `relay/tools/b539_*` file, the four PLACE-papers
### documents this act appends to, and the patch and message of every commit of this act (subject beginning `b539`) in four
### repositories, plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
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
        extra = [os.path.join(PP, f) for f in ('FINDINGS.md', 'OPEN_TRAILS.md', os.path.join('phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md'),
                                                os.path.join('phase1.5', 'proofs', 'THE_UNCONDITIONAL_SURROUND.md'))]
        files = sorted(set(glob.glob(os.path.join(D, 'b539_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b539_*')) + extra))
        files = [f for f in files if not f.endswith('b539_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b539'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        push_logs = sorted(os.path.basename(f) for f in files if os.path.basename(f).startswith('b539_push'))
        warnings = [f for f in push_logs if b'WARNING' in open(os.path.join(D, f), 'rb').read()]
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()),
                   push_logs=push_logs, warnings=warnings)
    io.open(os.path.join(D, 'b539_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b539_scores.json'))
AJ = json.loads(read('b539_anchor.json'))
TJ = json.loads(read('b539_tiers.json'))
FJ = json.loads(read('b539_findings.json'))
SU = json.loads(read('b539_surr.json'))
W = lambda v: 'HELD' if v else 'REFUTED'
L = ['=' * 104, 'b539 -- THE CLOSING RECORD. ### **THE CASCADE, ACT ONE, UNDER (R149).**', '=' * 104,
     '    the anchor tier : fresh at SIDE-explicit-formula %s ; %d of %d equal to their banks ; R3 UNDECIDED'
     % (AJ['head'][:7], sum(1 for r in AJ['rows'] if r['equal']), len(AJ['rows'])),
     '    the ranked list : %s ; T0 by criterion, none in (R149)(1)`s list : %s'
     % (TJ['counts'], [r['terminal'] for r in TJ['ranked'] if r['tier'] == 'T0']),
     '    beside the list : ' + ' ; '.join('%s %s' % (e['terminal'], e['tier']) for e in TJ['extra']),
     '    the sentences : SURR STANDS %d RESTS %d ; lv STANDS %d RESTS %d ; EXCEEDS %d ; outside RESTS %d'
     % (FJ['surr_stands'], FJ['surr_rests'], FJ['lv_stands'], FJ['lv_rests'], FJ['exceeds'], FJ['outside_rests']),
     '    E-2026-09-25-3 : DRAFTED at relay data/b539_erratum_draft.md, NOT FILED ; ' + read('b539_erratum.json').replace(NL, ' '),
     '    the writes : map appendix at line %s ; SURR tier table at line %s %s ; FINDINGS entry at line %s'
     % (json.loads(read('b539_appendix.json'))['heading_line'], SU['heading_line'], SU['counts'], FJ['heading_line']),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else
                           'hits %s over %s files, %s commits and %s push logs ; limb WARNINGs %s'
                           % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'], len(TK['push_logs']), TK['warnings'] or 'NONE')),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s ; (S1) %s (S2) %s (S3) %s'
     % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b539_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
     '    pre-push : %s' % lw(read('b539_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b539_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE), ('SIDE-explicit-formula', KER),
             ('SIDE-kernel', os.path.join('D:', os.sep, 'SIDE-kernel')), ('SIDE-lv-conservation', os.path.join('D:', os.sep, 'SIDE-lv-conservation'))):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    censuses : %s / %s' % (lw(read('b539_census_closing.txt'), 'TOTAL MISSING'), lw(read('b539_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b539_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **FOR THE AUTHOR, AT THE ACT AFTER**: the filing of E-2026-09-25-3 (relay data/b539_erratum_draft.md).',
      '    (b) ### **FOR THE AUTHOR**: five ranked terminals meet the T0 criterion by statement and are not in (R149)(1)`s',
      '        anchor list; whether the list widens is the author`s. partialPositivity_finiteRange is T4 unless named classical',
      '        premises count as (R149)(2)`s "named and open".',
      '    (c) ### **THE NEXT KEYSTONE**: PATHS_TO_THE_CRITICAL_LINE, per (R149)(3).',
      '=' * 104]
io.open(os.path.join(D, 'b539_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
