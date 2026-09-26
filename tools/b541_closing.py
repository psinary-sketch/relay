# -*- coding: utf-8 -*-
"""b541_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b541_*` and `relay/tools/b541_*` file, the four PLACE-papers
### documents this act writes, and the patch and message of every commit of this act (subject beginning `b541`) in four
### repositories, plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
FILES = ['ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md', os.path.join('phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')]
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
        files = sorted(set(glob.glob(os.path.join(D, 'b541_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b541_*'))
                           + [os.path.join(PP, f) for f in FILES]))
        files = [f for f in files if not f.endswith('b541_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b541'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        push_logs = sorted(os.path.basename(f) for f in files if os.path.basename(f).startswith('b541_push'))
        warnings = [f for f in push_logs if b'WARNING' in open(os.path.join(D, f), 'rb').read()]
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()),
                   push_logs=push_logs, warnings=warnings)
    io.open(os.path.join(D, 'b541_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b541_scores.json'))
FJ = json.loads(read('b541_file.json'))
LJ = json.loads(read('b541_law.json'))
CJ = json.loads(read('b541_census.json'))
E5 = json.loads(read('b541_erratum5.json'))
MJ = json.loads(read('b541_map.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
H = CJ['halt']
L = ['=' * 104, 'b541 -- THE CLOSING RECORD. ### **THE MONOGRAPH READ AGAINST THE RH-ANCHOR, ACT ONE, UNDER (R151).**', '=' * 104,
     '    E-2026-09-25-4 : FILED at ERRATA.md:%d-%d ; DEPOSIT-FACING bullet at :%d ; backticks outside code spans %d'
     % (FJ['entry_lines'][0], FJ['entry_lines'][1], FJ['bullet_line'], FJ['backticks_outside_code']),
     '    the tier-law line : map +%d bytes ; the R5 finding : FINDINGS :%d' % (LJ['map']['added'], LJ['findings']['heading_line']),
     '    the census : run 1 selected %d, run 2 selected %d, agree %s ; halt before the live heading :%d "%s" (act two`s first selected :%d)'
     % (CJ['run1']['selected'], CJ['run2']['selected'], CJ['lineage_agree'], H['line'], H['section'], H['first_act_two']),
     '      act one %d rows (%d live, %d DEPOSIT-SOLE ; LIVE-SOLE %d ; %d by the declared default) ; grades %s ; RESTS by erratum %s ; tiers %s'
     % (len(CJ['rows']), CJ['live_rows'], CJ['deposit_sole'], CJ['live_sole'], CJ['defaults'], CJ['counts'], CJ['by_erratum'], CJ['tiers']),
     '      deposited act-one sentences whose live copy lies past the halt : %d (read at act two)' % len(CJ['past_halt']),
     '    the chapter tier map : FINDINGS :%s' % MJ['heading_line'],
     '    E-2026-09-25-5 : DRAFTED at relay data/b541_erratum_draft.md, NOT FILED ; %d rows' % E5['rows'],
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else
                           'hits %s over %s files, %s commits and %s push logs ; limb WARNINGs %s'
                           % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'], len(TK['push_logs']), TK['warnings'] or 'NONE')),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s'
     % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [
     l for l in read('b541_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
     '    pre-push : %s' % lw(read('b541_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b541_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE), ('SIDE-explicit-formula', KER),
             ('SIDE-kernel', os.path.join('D:', os.sep, 'SIDE-kernel')), ('SIDE-lv-conservation', os.path.join('D:', os.sep, 'SIDE-lv-conservation'))):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    censuses : %s / %s' % (lw(read('b541_census_closing.txt'), 'TOTAL MISSING'), lw(read('b541_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b541_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **FOR THE AUTHOR**: the filing of E-2026-09-25-5 (relay data/b541_erratum_draft.md), which the read`s second act',
      '        may extend by a further entry.',
      '    (b) ### **THE READ`S SECOND ACT**: Chapter 26 to the file`s end, %d live sentences, §27.3 among them ((N2) scored there),' % H['act_two_live'],
      '        and the %d deposited front-matter sentences whose live copy is at :2219.' % len(CJ['past_halt']),
      '    (c) ### **THEN THE CASCADE RESUMES**: BALANCE_AND_POSITIVITY, per (R151)(6).',
      '=' * 104]
io.open(os.path.join(D, 'b541_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
