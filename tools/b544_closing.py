# -*- coding: utf-8 -*-
"""b544_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b544_*` and `relay/tools/b544_*` file, the two PLACE-papers
### documents this act writes, and the patch and message of every commit of this act (subject beginning `b544`) in four
### repositories, plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
FILES = [os.path.join(PP, f) for f in ('ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md')]
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
        files = sorted(set(glob.glob(os.path.join(D, 'b544_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b544_*')) + FILES))
        files = [f for f in files if not f.endswith('b544_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b544'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b544_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b544_scores.json'))
DJ = json.loads(read('b544_decls.json'))
PJ = json.loads(read('b544_premises.json'))
IJ = json.loads(read('b544_index.json'))
FJ = json.loads(read('b544_file.json'))
NJ = json.loads(read('b544_note.json'))
TB = json.loads(read('b544_table.json'))
FN = json.loads(read('b544_findings.json'))
W = lambda v: 'HELD' if v else 'REFUTED'
PR = {r: json.loads(read('b544_probe_%s.json' % r)) for r in ('SIDE-explicit-formula', 'SIDE-lv-conservation', 'SIDE-spinor-calibration-mathlib', 'SIDE-kernel')}
L = ['=' * 104, 'b544 -- THE CLOSING RECORD. ### **E-6 FILED; THE :1109 NOTE; CP-2 AND CP-3, UNDER (R154).**', '=' * 104,
     '    E-2026-09-25-6 : FILED at ERRATA.md:%d-%d ; bullet at :%d ; %d rows ; backticks %d' % (FJ['entry_lines'][0], FJ['entry_lines'][1], FJ['bullet_line'], FJ['rows'], FJ['backticks']),
     '    the :1109 note : FINDINGS.md:%d beneath :1109 (unchanged %s) ; the name not printed' % (NJ['note_line'], NJ['line_1109_unchanged']),
     '    the enumeration : %d declarations (b542: 5293, equal %s) ; subjects %s' % (DJ['count'], DJ['equal'], DJ['subjects']),
     '    the probes : ' + ' ; '.join('%s printed %d in %s s (exit %s)' % (r, len(p.get('profiles') or {}), p.get('seconds'), p.get('exit')) for r, p in PR.items()),
     '    CP-2 : %s ; premises %s' % (PJ['counts'], PJ['premise_props']),
     '    CP-3 : %s ; I rows concluding re = 1/2 : %s' % (IJ['counts'], [x[0] for x in IJ['i_concluding_location']]),
     '    the table : %s' % TB,
     '    FINDINGS : CP-2 at :%s ; CP-3 at :%s' % (FN['cp2']['heading_line'], FN['cp3']['heading_line']),
     '    the branches : %s' % ' ; '.join(l for l in read('b544_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b544_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
     '    pre-push : %s' % lw(read('b544_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b544_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE), ('SIDE-explicit-formula', KER),
             ('SIDE-kernel', os.path.join('D:', os.sep, 'SIDE-kernel')), ('SIDE-lv-conservation', os.path.join('D:', os.sep, 'SIDE-lv-conservation'))):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    censuses : %s / %s' % (lw(read('b544_census_closing.txt'), 'TOTAL MISSING'), lw(read('b544_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b544_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT**: CP-1 in the order of (R154)(3) -- the Phase 1.5 keystones` tables, BALANCE_AND_POSITIVITY next.',
      '    (b) ### **FOR THE AUTHOR**: 24 SIDE-kernel ZETA terminals under legacy/ have no library target and no profile at the pin;',
      '        one Zeta23 declaration is private and is not printable by name.',
      '=' * 104]
io.open(os.path.join(D, 'b544_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
