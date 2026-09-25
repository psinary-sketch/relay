# -*- coding: utf-8 -*-
"""b538_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b538_*` and `relay/tools/b538_*` file, FINDINGS, OPEN_TRAILS,
### CORRESPONDENCE, the new kernel files, the seat`s memory entry, and the patch and message of every commit of this act
### (subject beginning `b538`) in four repositories, plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
MEM = os.path.join('C:', os.sep, 'Users', 'echo chamber', '.claude', 'projects', 'D--', 'memory')
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
        extra = [os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md'), os.path.join(SIDE, 'CORRESPONDENCE.md'),
                 os.path.join(KER, 'SIDEExplicitFormula', 'RegisterDepth.lean'), os.path.join(KER, 'AxiomCheckRegisterDepth.lean'),
                 os.path.join(MEM, 'feedback_mirror_after_last_push.md')]
        files = sorted(set(glob.glob(os.path.join(D, 'b538_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b538_*')) + extra))
        files = [f for f in files if not f.endswith('b538_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b538'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        push_logs = sorted(os.path.basename(f) for f in files if os.path.basename(f).startswith('b538_push'))
        warnings = [f for f in push_logs if b'WARNING' in open(os.path.join(D, f), 'rb').read()]
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()),
                   push_logs=push_logs, warnings=warnings)
    io.open(os.path.join(D, 'b538_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b538_scores.json'))
CEN = json.loads(read('b538_census.json'))['rows']
PR = json.loads(read('b538_profile.json'))
W = lambda v: 'HELD' if v else 'REFUTED'
L = ['=' * 104, 'b538 -- THE CLOSING RECORD. ### **W-ORD-REGISTER-DEPTH, UNDER (R148).**', '=' * 104,
     '    the pins : SIDE-lv-conservation v0.10.0 (peeled 93c27ec; the cited files identical at HEAD 2f71068) ; SIDE-kernel v1.5 = 0e5233f',
     '    the module : RegisterDepth.lean at SIDE-explicit-formula %s ; attempts %d ; standard three or fewer %d of %d'
     % (git(KER, 'rev-parse', '--short', 'HEAD'), len(json.loads(read('b538_attempts.json'))),
        sum(PR['within_std3'].values()), len(PR['within_std3'])),
     '    the census : FINDINGS.md:%s' % json.loads(read('b538_findings.json')).get('heading_line')] + [
     '      %-10s %s' % (r['reg'], r['grade']) for r in CEN] + [
     '    the row : CORRESPONDENCE row 387 ; the pointer : %s' % lw(read('b538_components.txt'), 'THE POINTER'),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else
                           'hits %s over %s files, %s commits and %s push logs ; limb WARNINGs %s'
                           % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'], len(TK['push_logs']), TK['warnings'] or 'NONE')),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s'
     % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b538_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
     '    pre-push : %s' % lw(read('b538_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b538_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE), ('SIDE-explicit-formula', KER),
             ('SIDE-kernel', os.path.join('D:', os.sep, 'SIDE-kernel')), ('SIDE-lv-conservation', os.path.join('D:', os.sep, 'SIDE-lv-conservation'))):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    censuses : %s / %s' % (lw(read('b538_census_closing.txt'), 'TOTAL MISSING'), lw(read('b538_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b538_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **(R148)(4), ON THE AUTHOR`S WORD**: the deposited sentences lv`s h2 result touches (lv-conservation`s own',
      '        description; THE_UNCONDITIONAL_SURROUND §6`s "goal ⇐ h1 ∧ h2") are read against it at the act after.',
      '    (b) ### **R3 UNDECIDED**: the missing piece is per-class exclusion at re s ≤ 1 and whether the seven couplings jointly',
      '        pin Φ to Phi; the seat`s C3 observation (R3 vacuous at 1/2 ≤ re s ≤ 1) is NOT COMPILED.',
      '    (c) ### **W-ORD-SEAM-UPSTREAM** waits on the author`s word.',
      '=' * 104]
io.open(os.path.join(D, 'b538_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
