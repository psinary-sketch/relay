# -*- coding: utf-8 -*-
"""b540_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b540_*` and `relay/tools/b540_*` file, the six PLACE-papers
### documents this act writes, and the patch and message of every commit of this act (subject beginning `b540`) in four
### repositories, plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
FILES = ['ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md', os.path.join('phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md'),
         os.path.join('phase1.5', 'proofs', 'THE_UNCONDITIONAL_SURROUND.md'), os.path.join('phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md')]
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
        files = sorted(set(glob.glob(os.path.join(D, 'b540_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b540_*'))
                           + [os.path.join(PP, f) for f in FILES]))
        files = [f for f in files if not f.endswith('b540_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b540'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        push_logs = sorted(os.path.basename(f) for f in files if os.path.basename(f).startswith('b540_push'))
        warnings = [f for f in push_logs if b'WARNING' in open(os.path.join(D, f), 'rb').read()]
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()),
                   push_logs=push_logs, warnings=warnings)
    io.open(os.path.join(D, 'b540_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b540_scores.json'))
FJ = json.loads(read('b540_file.json'))
LJ = json.loads(read('b540_law.json'))
TJ = json.loads(read('b540_tiers.json'))
SJ = json.loads(read('b540_sentences.json'))
E4 = json.loads(read('b540_erratum4.json'))
W = lambda v: 'HELD' if v else 'REFUTED'
L = ['=' * 104, 'b540 -- THE CLOSING RECORD. ### **THE CASCADE, ACT TWO, UNDER (R150).**', '=' * 104,
     '    E-2026-09-25-3 : FILED at ERRATA.md:%d-%d ; DEPOSIT-FACING bullet at :%d ; backticks outside code spans %d'
     % (FJ['entry_lines'][0], FJ['entry_lines'][1], FJ['bullet_line'], FJ['backticks_outside_code']),
     '    the tier law : map %s ; SURR %s' % (LJ['map_counts'], LJ['surr_counts']),
     '    PATHS : block at line %s ; §III %s ; ANNEX A %s ; ANNEX B %s ; Correspondence %s ; withdrawn extrema %d'
     % (json.loads(read('b540_paths.json'))['heading_line'], TJ['counts']['siii'], TJ['counts']['annex_a'], TJ['counts']['annex_b'],
        TJ['counts']['corr'], TJ['extrema']),
     '    the sentences : read %d ; selected %d ; REPEATS %s ; RESTS by erratum %s ; PATHS-own %d ; outside E-1 / E-3 coverage %d'
     % (SJ['read'], len(SJ['selected']), SJ['counts'], SJ['rests_by_erratum'], SJ['own'], len(SJ['outside_coverage'])),
     '    E-2026-09-25-4 : DRAFTED at relay data/b540_erratum_draft.md, NOT FILED ; rows %s' % [(r['id'], r['line']) for r in E4['rows']],
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else
                           'hits %s over %s files, %s commits and %s push logs ; limb WARNINGs %s'
                           % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'], len(TK['push_logs']), TK['warnings'] or 'NONE')),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s'
     % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk). ### (a) is the :1788 -> :1787 correction, standing here.'] + [
     l for l in read('b540_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
     '    pre-push : %s' % lw(read('b540_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b540_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE), ('SIDE-explicit-formula', KER),
             ('SIDE-kernel', os.path.join('D:', os.sep, 'SIDE-kernel')), ('SIDE-lv-conservation', os.path.join('D:', os.sep, 'SIDE-lv-conservation'))):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    censuses : %s / %s' % (lw(read('b540_census_closing.txt'), 'TOTAL MISSING'), lw(read('b540_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b540_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **FOR THE AUTHOR**: the filing of E-2026-09-25-4 (relay data/b540_erratum_draft.md), scoped to the deposited',
      '        monograph §27.3 sentences PATHS repeats (A_Place_to_Stand.md:1787, :1794, :1800); a whole read of the deposited monograph',
      '        against b538 is the author`s to order.',
      '    (b) ### **FOR THE AUTHOR**: the reading of READING (3) -- a premise that is RH restated by a rewording lemma makes its',
      '        terminal ENCODES-CONCLUSION, T2, not T1-open -- applied to ConservationBridge.riemann_hypothesis and to',
      '        R5_output_HilbertPolya_to_RH, whose "disclaimed" face Register5_output_HilbertPolya is a theorem (register5_output_holds).',
      '    (c) ### **THE NEXT KEYSTONE**: BALANCE_AND_POSITIVITY, per (R149)(3).',
      '=' * 104]
io.open(os.path.join(D, 'b540_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
