# -*- coding: utf-8 -*-
"""b558_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b558_*` file (the work-lists included) and `relay/tools/b558_*`
### file, the PLACE-papers documents this act writes, and the patch and message of every commit of this act (subject beginning
### `b558`) in four repositories, plus any uncommitted change there. ### The refresh -- the memory and the mirror -- runs AFTER
### this record`s own push and is named here as OWED. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-kernel')
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(p):
    return io.open(os.path.join(D, p), encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


ED = json.loads(read('b558_editions.json'))
FILES = sorted(set(os.path.join(PP, *f.split('/')) for f in ['FINDINGS.md', 'OPEN_TRAILS.md', 'SPIRAL_MAP.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md',
                                                              'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md'] +
                   [v['pointer']['file'] for v in ED['lists'].values()]))


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
        files = sorted(set(glob.glob(os.path.join(D, 'b558_*')) + glob.glob(os.path.join(D, 'b558_editions', '*')) +
                           glob.glob(os.path.join(ROOT, 'tools', 'b558_*')) + FILES))
        files = [f for f in files if os.path.isfile(f) and not f.endswith('b558_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40', 'HEAD').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b558'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b558_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b558_scores.json'))
U = json.loads(read('b558_union.json'))
CP = json.loads(read('b558_cp1b.json'))
ST = json.loads(read('b558_settle.json'))
CR = json.loads(read('b558_credits.json'))
FND = json.loads(read('b558_findings.json'))
MR = json.loads(read('b558_maprow.json'))
MS = json.loads(read('b558_mapsection.json'))
MF = json.loads(read('b558_mapfix.json'))
TR = json.loads(read('b558_trail_notes.json'))
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
co = CP['counts_own']
L = ['=' * 104, 'b558 -- THE CLOSING RECORD. ### **CP-1b, THE IMPLICATION PASS, UNDER (R168).**', '=' * 104,
     '    the tag : SIDE-silence-principle v0.2.0 -- tag object %s, peeled %s (remote) = %s (local)' % (ST['tag']['remote_obj'][:10], ST['tag']['remote_peeled'][:10], ST['tag']['local_peeled'][:10]),
     '    the settlement lines : FOUNDATIONS :%d ; SPIRAL_MAP :%d ; OPEN_TRAILS :%d and :%d ; the table naming no_type_d or crt : %d lines' % (
         ST['appends'][0]['line'], ST['appends'][1]['line'], ST['appends'][2]['line'], ST['appends'][3]['line'], ST['table_lines']),
     '    the union : %d terminals ; over-counted %d (%s) ; additions %d (%s)' % (len(U['union']), len(U['over']), '; '.join(e[0] for e in U['over']), len(U['add']), ', '.join(U['add'])),
     '    the citers : %d rows ; the documents` own %d ; the cascade`s %d' % (len(CP['rows']), sum(co.values()), len(CP['rows']) - sum(co.values())),
     '    the readings (the documents` own) : STANDS %d ; MOVED-IN-MEANING %d ; CREDIT %d ; the cascade`s rows STANDS by default' % (co['STANDS'], co['MOVED-IN-MEANING'], co['CREDIT']),
     '    the map : rows :%d (%d terminals) ; the CP-1b section :%d ; its same-act line :%d' % (MR['line'], len(MR['rows']), MS['line'], MF['line']),
     '    the credits : FINDINGS %s' % ', '.join(':%d (%s)' % (o['line'], o['id']) for o in CR['entered']),
     '    the work-lists : %d -- %s' % (len(ED['lists']), ' ; '.join('%s %d' % (k, v['rows']) for k, v in ED['lists'].items())),
     '    no work-list : %s' % ', '.join(ED['none']),
     '    the entry : FINDINGS :%s ; the trail record : OPEN_TRAILS :%s ; next W-ORD-DETECTION-REGION under (R169)' % (FND['line'], TR['line']),
     '    the branches : %s' % ' ; '.join(l for l in read('b558_branches.txt').split(NL) if l.startswith('Deleted branch')),
     '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
     '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s (N7) %s before the commit, its mirror clause OWED ; (S1) %s (S2) %s (S3) %s' % tuple(
         W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 's1', 's2', 's3')),
     '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b558_defects.txt').rstrip(NL).split(NL) if l] + [
     '', '### THE COMMITS, THE CENSUSES.',
     '    pre-push : %s' % lw(read('b558_checks.txt'), 'ARMS RUN :'),
     '    post-push : %s' % lw(read('b558_checks_postpush.txt'), 'ARMS RUN :')]
for nm in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-effects', 'SIDE-silence-principle',
           'SIDE-compression', 'SIDE-structural-error-correction', 'SIDE-cosmo'):
    p = ROOT if nm == 'relay' else (PP if nm == 'PLACE-papers' else os.path.join('D:', os.sep, nm))
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-28s local %s ; remote %s ; %s' % (nm, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b558_census_closing.txt'), 'TOTAL MISSING'), lw(read('b558_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b558_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### OWED AFTER THIS RECORD`S OWN PUSH -- READING (11), THE REFRESH.',
      '    (a) the seat`s memory rewritten from the ledgers (MEMORY.md and one project file for b547-b558), its headings and line count printed before and after;',
      '    (b) the mirror built by `tools/mirror_build.ps1 -DateTag 2026-09-29-b558` and verified from PLACE-papers; its MANIFEST md5 and last-commit printed;',
      '    (c) their figures are the closing paste`s and are banked in relay `data/b558_refresh.txt`, left for the next act`s first commit; nothing is',
      '        written to PLACE-papers after this push.',
      '', '### CARRIED FORWARD.',
      '    (d) ### **THE NEXT ACT**: W-ORD-DETECTION-REGION, lane two`s first, its hypotheses fixed in (R169).',
      '    (e) ### **FOR THE AUTHOR**: the work-lists (relay `data/b558_editions/`) are CP-7`s inputs; no edition is written before its informing work-orders land.',
      '    (f) ### **FOR THE AUTHOR**: (N4)`s second clause is REFUTED -- ENUMERA`s h2 closure lines ("RH ... PROVED under h2") read MOVED-IN-MEANING.',
      '    (g) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping only if it changed.',
      '=' * 104]
io.open(os.path.join(D, 'b558_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
