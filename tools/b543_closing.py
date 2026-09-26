# -*- coding: utf-8 -*-
"""b543_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b543_*` and `relay/tools/b543_*` file, the two PLACE-papers
### documents this act writes, and the patch and message of every commit of this act (subject beginning `b543`) in four
### repositories, plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
FILES = [os.path.join(PP, f) for f in ('FINDINGS.md', 'OPEN_TRAILS.md')]
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
        files = sorted(set(glob.glob(os.path.join(D, 'b543_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b543_*')) + FILES))
        files = [f for f in files if not f.endswith('b543_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b543'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b543_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b543_scores.json'))
CJ = json.loads(read('b543_census.json'))
TJ = json.loads(read('b543_terms.json'))
E6 = json.loads(read('b543_erratum6.json'))
MJ = json.loads(read('b543_map.json'))
W = lambda v: 'HELD' if v else 'REFUTED'
C = CJ['counts']
L = ['=' * 104, 'b543 -- THE CLOSING RECORD. ### **THE MONOGRAPH READ, ACT TWO, UNDER (R153).**', '=' * 104,
     '    the census : %d rows from live :%d ; STANDS %d ; STANDS-AS-HISTORY %d ; RESTS %d ; EXCEEDS %d ; RESTS by erratum %s'
     % (CJ['act_two'], CJ['first_line'], C['STANDS'], C['STANDS-AS-HISTORY'], C['RESTS'], C['EXCEEDS'], CJ['by_erratum']),
     '      §27.3 RESTS : %d rows across %s' % (len(CJ['s273']['rows']), CJ['s273']['ids']),
     '      supplementary : %s' % [(x['name'], x['grade']) for x in CJ['supplementary']],
     '      vocabulary moves under (R153)(2) : %s' % CJ['vocab_moves'],
     '    the terminals re-read : %d ; CARRIED %d ; MOVED %d' % (len(TJ['terms']), sum(1 for x in TJ['terms'] if x['word'] == 'CARRIED'),
                                                             sum(1 for x in TJ['terms'] if x['word'] == 'MOVED')),
     '    the RH-anchor : %s' % lw(read('b543_anchor.txt'), 'FRESH #check'),
     '    E-2026-09-25-6 : DRAFTED at relay data/b543_erratum_draft.md, NOT FILED ; %d rows ; backticks %d' % (E6['rows'], E6['backticks']),
     '    the map`s second half : FINDINGS :%s ; the CP-1 line in FINDINGS and OPEN_TRAILS' % MJ['heading_line'],
     '    FINDINGS.md:1109 : HELD -- the ordered note would be false (the name is declared in SIDE-kernel v1.0 and v1.1, MetaKernel.lean:138,',
     '      and cited in other PLACE-papers files and earlier relay banks); nothing written there ; b542`s carried item corrected',
     '    the branches : %s' % ' ; '.join(l for l in read('b543_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits'
                           % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s'
     % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
     '', '### THE NAVIGATOR`S READINGS, ROW BY ROW:'] + [l for l in read('b543_desk_notes.txt').split(NL) if '-> [' in l] + [
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b543_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
     '    pre-push : %s' % lw(read('b543_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b543_checks_postpush.txt'), 'ARMS RUN :')]
for n, p in (('relay', ROOT), ('PLACE-papers', PP), ('SIDE-global-section', SIDE), ('SIDE-explicit-formula', KER),
             ('SIDE-kernel', os.path.join('D:', os.sep, 'SIDE-kernel')), ('SIDE-lv-conservation', os.path.join('D:', os.sep, 'SIDE-lv-conservation'))):
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-22s local %s ; remote %s ; %s' % (n, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
L += ['    censuses : %s / %s' % (lw(read('b543_census_closing.txt'), 'TOTAL MISSING'), lw(read('b543_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b543_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **FOR THE AUTHOR**: (R153)(5)`s note at FINDINGS.md:1109 is held. The declaration named there is public (SIDE-kernel',
      '        v1.0 and v1.1, MetaKernel.lean:138) and cited elsewhere; the note as ordered would be false on two clauses. The author`s',
      '        word on what, if anything, is appended there.',
      '    (b) ### **FOR THE AUTHOR**: the filing of E-2026-09-25-6 (relay data/b543_erratum_draft.md).',
      '    (c) ### **THE NEXT ACT**: CP-2 and CP-3 together, from b542`s enumeration; then BALANCE_AND_POSITIVITY.',
      '=' * 104]
io.open(os.path.join(D, 'b543_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
