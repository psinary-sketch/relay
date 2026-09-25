# -*- coding: utf-8 -*-
"""b537_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b537_*` and `relay/tools/b537_*` file, OPEN_TRAILS, the seat`s
### new memory entry and index, the zip, and the patch and message of every commit of this act (subject beginning `b537`) in
### four repositories, plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
MEM = os.path.join('C:', os.sep, 'Users', 'echo chamber', '.claude', 'projects', 'D--', 'memory')
ZIP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'mirror-refresh-2026-09-25-b537.zip')
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
        extra = [os.path.join(PP, 'OPEN_TRAILS.md'), os.path.join(MEM, 'project_criterion_b533_b536.md'), os.path.join(MEM, 'MEMORY.md'), ZIP]
        files = sorted(set(glob.glob(os.path.join(D, 'b537_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b537_*')) + extra))
        files = [f for f in files if not f.endswith('b537_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b537'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        push_logs = sorted(os.path.basename(f) for f in files if os.path.basename(f).startswith('b537_push'))
        warnings = [f for f in push_logs if b'WARNING' in open(os.path.join(D, f), 'rb').read()]
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()),
                   push_logs=push_logs, warnings=warnings)
    io.open(os.path.join(D, 'b537_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b537_scores.json'))
MJ = json.loads(read('b537_mirror.json'))
MM = json.loads(read('b537_memory.json'))
W = lambda v: 'HELD' if v else 'REFUTED'
L = ['=' * 104, 'b537 -- THE CLOSING RECORD. ### **THE MIRROR EXPORT AND THE MEMORY REFRESH, UNDER (R147).**', '=' * 104,
     '    the last export read : mirror-refresh-2026-09-25-b534.zip, built by b534 at PLACE-papers 3b5532a',
     '    the export : %s ; %s entries (%s files + MANIFEST) ; sha256 %s' % (MJ['zip'], MJ['entries'], MJ['files_excl_manifest'], MJ['zip_sha256']),
     '    additions since the last export : %s ; %s' % (MJ['additions_since_3b5532a'] or 'NONE', MJ['roster_line']),
     '    verify before the push : %s' % lw(read('b537_mirror_verify.txt'), '### VERDICT:'),
     '    verify after the push  : %s ; %s' % (lw(read('b537_mirror_verify_postpush.txt'), 'CLAUSE 2 :'), lw(read('b537_mirror_verify_postpush.txt'), '### VERDICT:')),
     '    the memory : %s ; %s lines ; earlier entries changed %s' % (MM['path'], MM['lines'], [f for f in MM['changed'] if f != 'MEMORY.md'] or 'NONE'),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else
                           'hits %s over %s files (the zip and the memory entry among them), %s commits and %s push logs ; limb WARNINGs %s'
                           % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'], len(TK['push_logs']), TK['warnings'] or 'NONE')),
     '    (N1) %s (N2) %s (N3) %s (N4) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk, and (c) after the push).'] + [l for l in read('b537_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES.',
     '    pre-push : %s' % lw(read('b537_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b537_checks_postpush.txt'), 'ARMS RUN :'),
     '    ### the post-push suite`s G-VERIFY-THREE-CLAUSES reads the PRE-push verification bank; the post-push verification is the line above.']
for n, p in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE), ('SIDE-explicit-formula', KER),
             ('SIDE-kernel', os.path.join('D:', os.sep, 'SIDE-kernel'))):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    censuses : %s / %s' % (lw(read('b537_census_closing.txt'), 'TOTAL MISSING'), lw(read('b537_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b537_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **FOR THE AUTHOR, DEFECT (c)**: whether to rebuild the export after this closing, so the mirror carries b537`s',
      '        own record and the two work-orders -- which needs this act`s zip and the builder`s stage folder removed first.',
      '    (b) ### **W-ORD-REGISTER-DEPTH** is triggered at the act after this one unless the author rules otherwise;',
      '        **W-ORD-SEAM-UPSTREAM** waits on the author`s word.',
      '    (c) ### The ledgers on D: remain the currency authority until the author uploads the mirror ((R147)(2)).',
      '=' * 104]
io.open(os.path.join(D, 'b537_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
