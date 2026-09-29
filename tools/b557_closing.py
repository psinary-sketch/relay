# -*- coding: utf-8 -*-
"""b557_closing.py -- THE CLOSING RECORD, AND THE TOKEN SCAN. ### Figures READ from the banks, not retyped.

### The token is read from `os.environ['ZENODO_TOKEN']` and compared against bytes; it is never printed, and nothing derived
### from it except COUNTS is written. Scanned: every `relay/data/b557_*` and `relay/tools/b557_*` file, the five PLACE-papers
### documents this act writes, and the patch and message of every commit of this act (subject beginning `b557`) in four
### repositories, plus any uncommitted change there. ### This file deletes nothing.
"""
import glob, io, json, os, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KER = os.path.join('D:', os.sep, 'SIDE-kernel')
import sys as _s
_s.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
import b557_record as RR
DOCS = dict(RR.DOCS, GRH=RR.GRHR, CEN=RR.CENR)
FILES = [os.path.join(PP, f) for f in ['FINDINGS.md', 'OPEN_TRAILS.md'] + list(DOCS.values())]
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
        files = sorted(set(glob.glob(os.path.join(D, 'b557_*')) + glob.glob(os.path.join(ROOT, 'tools', 'b557_*')) + FILES))
        files = [f for f in files if not f.endswith('b557_tokenscan.json')]
        hits = {}
        for f in files:
            b = open(f, 'rb').read()
            if t in b:
                hits[os.path.basename(f)] = b.count(t)
        commits = 0
        for repo in (ROOT, PP, SIDE, KER):
            for l in git(repo, 'log', '--pretty=%H %s', '-40', 'HEAD').split(NL):
                if l.strip() and l.split(' ', 1)[-1].startswith('b557'):
                    commits += 1
                    b = git_bytes(repo, 'show', '-p', '--format=%H%n%B', l.split()[0])
                    if t in b:
                        hits['commit %s %s' % (os.path.basename(repo), l.split()[0][:10])] = b.count(t)
            b = git_bytes(repo, 'diff', 'HEAD')
            if t in b:
                hits['uncommitted %s' % os.path.basename(repo)] = b.count(t)
        res = dict(set=True, files_scanned=len(files), commits_scanned=commits, hits=hits, hits_total=sum(hits.values()))
    io.open(os.path.join(D, 'b557_tokenscan.json'), 'w', encoding='utf-8', newline=NL).write(json.dumps(res, indent=1))
    return res


TK = tokenscan()
SC = json.loads(read('b557_scores.json'))
TS = json.loads(read('b557_tiers.json'))
BL = json.loads(read('b557_blocks.json'))
PJ = json.loads(read('b557_prints.json'))
RO = json.loads(read('b557_roster.json'))
SP = json.loads(read('b557_supersede.json'))
AN = json.loads(read('b557_anchor.json'))
CE = json.loads(read('b557_census.json'))
FND = json.loads(read('b557_findings.json'))
RDN = json.loads(read('b557_replace_done.json'))
PR = [json.loads(l) for l in read('b557_probes.jsonl').split(NL) if l.strip()]
W = lambda v: 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')
ORDER = RR.ORDER
L = ['=' * 104, 'b557 -- THE CLOSING RECORD. ### **THE CASCADE, ACT ELEVEN, BATCH TWO, UNDER (R167).**', '=' * 104,
     '    the no_type_d settlement : GRH_CASCADE :%s' % SP['line'],
     '    the rebuild : exit %s ; prints %d ; banked and agreeing %d ; disagreeing %d ; artefacts replaced %d, digests equal %s ; m4r %s' % (
         PJ['build_exit'], len(PJ['prints']), PJ['agree'], len(PJ['disagree']), RDN['count'], RDN['all_equal'], SC['m4r']),
     '    the anchor scope : FINDINGS :%s ; the census line :%s and its correction :%s' % (AN['line'], CE['append']['line'], CE['correction']['line'])]
for k in RR.DOCS:
    s_ = TS[k]
    L.append('    %-8s : block :%s ; %d rows ; tiers %s ; CARRIED %d MOVED %d %s' % (
        k, BL[k]['line'], len(s_['rows']), {x: s_['term_tiers'][x] for x in ORDER if s_['term_tiers'][x]}, s_['disp']['CARRIED'], s_['disp']['MOVED'],
        [r['line'] for r in s_['rows'] if r['disp'] == 'MOVED']))
L += ['    the T0 terminals : %s' % TS['t0'],
      '    the probes : %d records -- elaborated %d, compared at the tag %d ; non-zero exits %s' % (
          len(PR), sum(1 for r in PR if not r.get('identical_to')), sum(1 for r in PR if r.get('identical_to')),
          ['%s %s' % (r['id'], r['exit']) for r in PR if r.get('exit') not in (0, None)]),
      '    CP-1 : %s ; roster %d' % ('CLOSED' if RO['closed'] else 'NOT CLOSED %s' % RO['missing'], len(RO['roster'])),
      '    the entry : FINDINGS :%s ; next b558 (CP-1b)' % FND['line'],
      '    the branches : %s' % ' ; '.join(l for l in read('b557_branches.txt').split(NL) if l.startswith('Deleted branch')),
      '    the token : %s' % ('NOT SET -- THE SCAN DID NOT RUN' if not TK['set'] else 'hits %s over %s files and %s commits' % (TK['hits_total'], TK['files_scanned'], TK['commits_scanned'])),
      '    (N1) %s (N2) %s (N3) %s (N4) %s (N5) %s (N6) %s ; (S1) %s (S2) %s (S3) %s' % tuple(W(SC[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
      '', '### THIS ACT`S OWN DEFECTS (the desk).'] + [l for l in read('b557_defects.txt').rstrip(NL).split(NL) if l] + [
      '', '### THE COMMITS, THE CENSUSES. ### NO MIRROR ZIP AT THIS ACT.',
      '    pre-push : %s' % lw(read('b557_checks.txt'), 'ARMS RUN :'),
      '    post-push : %s' % lw(read('b557_checks_postpush.txt'), 'ARMS RUN :')]
for nm in ('relay', 'PLACE-papers', 'SIDE-global-section', 'SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-effects', 'SIDE-silence-principle',
           'SIDE-compression', 'SIDE-structural-error-correction', 'SIDE-cosmo'):
    p = ROOT if nm == 'relay' else (PP if nm == 'PLACE-papers' else os.path.join('D:', os.sep, nm))
    loc, rem = git(p, 'rev-parse', 'HEAD'), (git(p, 'ls-remote', 'origin', 'main').split() or [''])[0]
    L.append('      %-28s local %s ; remote %s ; %s' % (nm, loc[:12], rem[:12], 'AGREE' if loc == rem else 'DISAGREE'))
held = git(ROOT, 'show', '--name-only', '--pretty=format:', '6eada6a').split(NL)
tree = git(ROOT, 'ls-tree', '-r', '--name-only', 'HEAD').split(NL)
L += ['    the HELD commit 6eada6a : its files in the pushed tree : %d of %d' % (sum(1 for f in held if f and f in tree), len([f for f in held if f])),
      '    censuses : %s / %s' % (lw(read('b557_census_closing.txt'), 'TOTAL MISSING'), lw(read('b557_faces_census_closing.txt'), 'TOTAL MISSING')),
      '    pins : %s' % lw(read('b557_pins_closing.txt'), 'REPOS HARD-FAILING'),
      '', '### CARRIED FORWARD.',
      '    (a) ### **THE NEXT ACT**: b558, CP-1b -- the implication pass; then the memory and the mirror are refreshed per (R157)(6) and the author clears the context.',
      '    (b) ### **FOR THE AUTHOR**: FOUNDATIONS :628 cites SIDESilencePrinciple.Universal.silence_universal at v0.1.0, where it is absent; it exists at HEAD 667c254, untagged.',
      '    (c) ### **FOR THE AUTHOR**: ProductFormula.conservation_of_spectra, which FOUNDATIONS and TECHNE lean on, states `1 ^ s = 1` over ℤ; graded T2.',
      '    (d) At this close the suite`s regeneration of terminal_table.* is committed as housekeeping if it changed.',
      '    (e) Under (R157)(6) the seat`s memory is not refreshed at this act; b558 refreshes it.',
      '=' * 104]
io.open(os.path.join(D, 'b557_closing.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
print(NL.join(L))
sys.exit(0 if TK.get('set') and TK['hits_total'] == 0 else 1)
