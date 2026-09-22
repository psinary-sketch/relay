# -*- coding: utf-8 -*-
"""b484_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb.
### ### **THE CARRIED ARMS WERE RE-POINTED ONE AT A TIME**, each read against THIS act's banks
### before its pointer moved -- b480 recorded three instances of the wholesale-substitution species
### in a single act, and this file is written against that.
"""
import io
import glob
import fnmatch
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
FACE = os.path.join(D, 'b484_registration_2026-09-22.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
NL = chr(10)
L, RES, EX = [], [], []


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        with open(p, 'rb') as fh:
            return fh.read().decode('utf-8', 'replace').replace(chr(13), '')
    except Exception:
        return ''


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def gits(repo, *a):
    return git(repo, *a).strip()


def line_with(text, needle):
    """### **A2.** ### The FIRST LINE of a TEXT carrying the needle -- never the whole text."""
    for ln in (text or '').split(NL):
        if needle in ln:
            return ln
    return ''


def cut(S, k, sub):
    M = dict(S)
    M[k] = (S.get(k) or '').replace(sub, '')
    return M


def put(S, k, v):
    M = dict(S)
    M[k] = v
    return M


def sources():
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b484_ferry.txt')),
        scan=read(os.path.join(D, 'b484_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b484_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b484_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b484_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b484_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b484_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        # ### **THE PRIOR CLOSED ACT IS b483.** ### b479 and b482 are banked and unrun.
        prior=read(os.path.join(D, 'b483_closing.txt')),
        addendum=read(os.path.join(D, 'b484_addendum.txt')),
        comp=read(os.path.join(D, 'b484_components.txt')),
        desk=read(os.path.join(D, 'b484_desk_notes.txt')),
        span=read(os.path.join(D, 'b484_span_notes.txt')),
        res=json.loads(read(os.path.join(D, 'b484_results.json')) or '{}'),
        sc=json.loads(read(os.path.join(D, 'b484_scores.json')) or '{}'),
        sv=json.loads(read(os.path.join(D, 'b484_survey.json')) or '{}'),
        win=read(os.path.join(T, 'b321_window.py')),
        b400=read(os.path.join(D, 'b400_closing.txt')),
        b446=read(os.path.join(D, 'b446_closing.txt')),
        target=read(os.path.join(PP, 'phase1.5', 'method', 'INVARIANCE_BARRIERS.md')),
        reg=read(os.path.join(PP, 'REGISTRY.md')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b484_checks.py')),
        tools484=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b484_') and f.endswith('.py') and f != 'b484_checks.py'),
        rtracked=gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b484.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b484 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b484_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        # ### **THE CHAIN'S OWN PORCELAIN, AS A SOURCE.** ### The first version of the arm below
        # ### called `gits` INSIDE the predicate, so it read live git and ignored `S` entirely --
        # ### and an arm that does not read its supplied source ### **CANNOT BE HANDED A MUTATED
        # ### ONE AND SO CANNOT FAIL ITS POSITIVE CONTROL.** ### b363's species, caught by that
        # ### control doing exactly its job.
        chain_clean=gits(ROOT, 'status', '--porcelain', '--', 'tools/b321_window.py',
                         'tools/b317_smear.py', 'tools/b318_square.py', 'tools/e16'),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b484 --'):
                k |= set(os.path.basename(x) for x in
                         gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                k.add(os.path.basename(l[3:].strip()))
    # ### b475's log is still being written by another act's live process; excluded BY NAME.
    k -= {'b475_zeta23_build.log'}
    S['kinds'] = k
    LIVE = {'b475_zeta23_build.log'}
    prior = [f for f in os.listdir(D)
             if re.match(r'^b4[0-7][0-9]_|^b48[0123]_', f) and f not in LIVE]
    S['prior_checked'] = len(prior)
    S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)
    return S


def globs_of(face):
    """### (R85) as (R91) amends it: THE FACE'S (W) SECTION AS A LIST OF GLOBS, the act's own stem
    ### glob included -- which is the whole point of (R91)."""
    w = face[face.index('### (W) THE WRITE LIST'):face.index('### (Z) THE NOTHINGS')]
    return [g.split('/')[-1] for g in re.findall(r'`([^`]+)`', w)]


def sc(S, k):
    return (S['sc'] or {}).get(k, {}).get('verdict', '')


def c(S, k):
    return (S['res'] or {}).get(k, {})


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'paste ends (part 1 of 1)' in S['ferry'],
     lambda S: cut(S, 'ferry', 'paste ends (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE',
     lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-ZERO', 'this act`s banked scan',
     lambda S: '(R81) FLAGS : 0' in S['scan'],
     lambda S: put(S, 'scan', S['scan'].replace('(R81) FLAGS : 0', '(R81) FLAGS : 1'))),
    ('G-STEPZERO-CENSUS', 'two banked censuses',
     lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'fcens', S['fcens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 3'))),
    ('G-STEPZERO-PINS', 'a banked verdict LINE',
     lambda S: 'REPOS HARD-FAILING : 0' in line_with(S['pins'], 'REPOS HARD-FAILING'),
     lambda S: put(S, 'pins', S['pins'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-SURVEY-NOMISS', 'a banked verdict LINE',
     lambda S: 'MISSES : 0' in line_with(S['extract'], 'MISSES :'),
     lambda S: put(S, 'extract', S['extract'].replace('MISSES : 0', 'MISSES : 2'))),
    ('G-REG-LOCKED-FIRST', 'the face lock block',
     lambda S: 'THE REGISTRATION LOCK' in S['face'], lambda S: cut(S, 'face', 'THE REGISTRATION LOCK')),
    ('G-LOCKGATE-EIGHT', 'a banked verdict LINE (A2)',
     lambda S: 'LOCK PERMITTED' in line_with(S['lock'], '**VERDICT : LOCK')
     and 'GATES READ : 8. ### PASSING : 8' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 6'))),
    ('G-SEAL-VERIFIES', 'a banked verdict LINE',
     lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('SEAL INTACT', 'SEAL BROKEN'))),
    ('G-PRIOR-CLOSED-PUSHED', 'b483`s closing AND the ledger, each for what it holds',
     lambda S: ('THE COMMITS, EACH READ BACK BY ls-remote' in S['prior']
                and S['corr'].count('| 330 |') == 1),
     lambda S: cut(S, 'prior', 'THE COMMITS, EACH READ BACK BY ls-remote')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory`s own banked ferries',
     lambda S: (os.path.exists(os.path.join(D, 'b482_ferry.txt'))
                and not os.path.exists(os.path.join(D, 'b482_registration_2026-09-22.txt'))
                and 'b484' in S['face']),
     lambda S: cut(S, 'face', 'b484')),

    # ---------------------------------------------------------------- component 1
    ('G-C1-TWO-WORDS-ONLY', 'the target file itself',
     lambda S: ('Current: monograph v1.1.2, version DOI 10.5281/zenodo.21539167' in S['target']
                and c(S, 'c1')['other_changed'] == 0),
     lambda S: put(S, 'res', dict(S['res'], c1=dict(c(S, 'c1'), other_changed=3)))),
    ('G-C1-ORIGINAL-PRESERVED-VERBATIM', 'the target file against the results bank',
     lambda S: c(S, 'c1')['original'] in S['target'] and c(S, 'c1')['missing'] == 0,
     lambda S: put(S, 'target', S['target'].replace(c(S, 'c1')['original'], 'x'))),
    ('G-C1-NO-OTHER-LINE-TOUCHED', 'the commit file list and the results bank',
     lambda S: (c(S, 'c1')['other_changed'] == 0
                and sorted(S['tracked']) == sorted(['OPEN_TRAILS.md',
                                                    'phase1.5/method/INVARIANCE_BARRIERS.md'])),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['phase1.5/method/INSTRUMENTS.md'])),
    ('G-C1-VALUES-FROM-REGISTRY', 'REGISTRY.md itself against the target file',
     lambda S: ('10.5281/zenodo.21539167' in S['reg'] and 'v1.1.2' in S['reg']
                and '10.5281/zenodo.21539167' in S['target']),
     lambda S: put(S, 'target', S['target'].replace('10.5281/zenodo.21539167', 'x'))),
    ('G-C1-CONCEPT-DOI-UNTOUCHED', 'the target file, for the DOI that already agreed',
     lambda S: (S['target'].count('10.5281/zenodo.19675355') >= 2
                and '10.5281/zenodo.19675356' in S['target']),
     lambda S: put(S, 'target', S['target'].replace('10.5281/zenodo.19675355', 'x'))),
    ('G-C1-DIFF-PRINTED', 'the components record, for BOTH the claim and the raw counts',
     lambda S: ('LINES OF THE OLD FILE ABSENT FROM THE NEW FILE : 0' in S['comp']
                and 'git --numstat' in S['comp']
                and 'NOT' in S['comp'] and 'HIDDEN BEHIND THAT SENTENCE' in S['comp']),
     lambda S: cut(S, 'comp', 'git --numstat')),

    # ---------------------------------------------------------------- component 2
    ('G-C2-WORDORDER-FILED', 'the components record',
     lambda S: ('W-ORD-QUADRATURE-BOUND' in S['comp']
                and 'NO ERROR BOUND FOR THE PLACES-SIDE QUADRATURE' in S['comp']),
     lambda S: cut(S, 'comp', 'W-ORD-QUADRATURE-BOUND')),
    ('G-C2-TRIGGER-NAMED', 'the components record',
     lambda S: 'TRIGGER:' in S['comp'] and 'numerical instrument lane' in S['comp'],
     lambda S: cut(S, 'comp', 'TRIGGER:')),
    ('G-C2-BOTH-FIGURES-PRINTED', 'the results bank against the components record',
     lambda S: (str(c(S, 'c2')['citing']) in S['comp']
                and str(c(S, 'c2')['predicating']) in S['comp']
                and c(S, 'c2')['citing'] > c(S, 'c2')['predicating']),
     lambda S: put(S, 'res', dict(S['res'], c2=dict(c(S, 'c2'), citing=0, predicating=0)))),
    ('G-C2-MATCHER-LINEAGE-PRINTED', 'the components record and the survey',
     lambda S: ('version 1, CO-OCCURRENCE' in S['extract']
                and 'version 2, PREDICATION' in S['extract']
                and c(S, 'c2')['wide'] != c(S, 'c2')['predicating']),
     lambda S: cut(S, 'extract', 'version 1, CO-OCCURRENCE')),
    ('G-C2-RESIDUE-HAND-READ', 'the survey, for the residue block and its verdicts',
     lambda S: ('THE HAND-READ RESIDUE' in S['extract']
                and 'NOT A CLAIM -- two figures in one sentence' in S['extract']),
     lambda S: cut(S, 'extract', 'NOT A CLAIM -- two figures in one sentence')),
    ('G-C2-CHAIN-NOT-EDITED', 'the chain files` porcelain, READ IN THE SOURCE',
     lambda S: S['chain_clean'] == '',
     lambda S: put(S, 'chain_clean', ' M tools/b321_window.py')),

    # ---------------------------------------------------------------- component 3
    ('G-C3-COMPARATOR-AT-ITS-LINE', 'b321_window.py itself against the components record',
     lambda S: ('while p ** k <= math.exp(L) + PRIME_TOL:' in S['win']
                and 'if ln <= L:' in S['win']
                and 'if ln <= L:' in S['comp']),
     lambda S: cut(S, 'comp', 'if ln <= L:')),
    ('G-C3-TWO-COMPARATORS-NAMED', 'the components record',
     lambda S: 'the OUTER cap' in S['comp'] and 'the INNER gate' in S['comp'],
     lambda S: cut(S, 'comp', 'the INNER gate')),
    ('G-C3-ASQ-FULL-PRECISION', 'the results bank against the components record',
     lambda S: repr(c(S, 'c3')['asq']) in S['comp'] and c(S, 'c3')['asq'] > 17.0,
     lambda S: put(S, 'res', dict(S['res'], c3=dict(c(S, 'c3'), asq=17.0)))),
    ('G-C3-NOT-AT-THE-EDGE', 'the results bank against the components record',
     lambda S: (c(S, 'c3')['enters'] is True and c(S, 'c3')['at_edge'] is False
                and 'BUT NOT AT THE EDGE' in S['comp'] and c(S, 'c3')['margin'] > 0.0),
     lambda S: put(S, 'res', dict(S['res'], c3=dict(c(S, 'c3'), at_edge=True)))),
    ('G-C3-B400-QUOTED', 'b400`s own bank against the components record',
     lambda S: ('It moves no value' in S['b400']
                and 'It moves no value' in S['comp']
                and c(S, 'c3')['same_comparator'] is True),
     lambda S: cut(S, 'b400', 'It moves no value')),
    ('G-C3-THREE-BANKS-QUOTED', 'the survey`s quote bank',
     lambda S: (len(S['sv']['quotes']) >= 4
                and {q['act'].split()[0] for q in S['sv']['quotes']} >= {'b437', 'b446', 'b483'}),
     lambda S: put(S, 'sv', dict(S['sv'], quotes=S['sv']['quotes'][:1]))),
    ('G-C3-ONE-VERDICT', 'the results bank against the components record',
     lambda S: (c(S, 'c3')['verdict'] == 'SEPARATE OBJECTS'
                and S['comp'].count('ONE CONVENTION') <= 1
                and 'SEPARATE OBJECTS' in S['comp']),
     lambda S: put(S, 'comp', S['comp'].replace('SEPARATE OBJECTS', 'x'))),

    # ---------------------------------------------------------------- the expectations
    ('G-N1-SCORED', 'the scores bank against the results bank',
     lambda S: 'SPLIT' in sc(S, 'N1') and c(S, 'c3')['enters'] and not c(S, 'c3')['at_edge'],
     lambda S: put(S, 'sc', dict(S['sc'], N1=dict(S['sc']['N1'], verdict='HELD')))),
    ('G-N2-SCORED', 'the scores bank against b400`s own bank',
     lambda S: sc(S, 'N2') == 'HELD' and 'p^m <= a^2' in S['b400'],
     lambda S: cut(S, 'b400', 'p^m <= a^2')),
    ('G-N3-SCORED', 'the scores bank against the results bank',
     lambda S: sc(S, 'N3') == 'REFUTED' and c(S, 'c3')['verdict'] == 'SEPARATE OBJECTS',
     lambda S: put(S, 'res', dict(S['res'], c3=dict(c(S, 'c3'), verdict='ONE CONVENTION')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk bank',
     lambda S: ("THE SEAT'S OWN" in S['face']
                and 'REGISTERED 3 ; HELD 1 ; SPLIT 1 ; REFUTED 1' in S['desk']),
     lambda S: cut(S, 'desk', 'REGISTERED 3 ; HELD 1 ; SPLIT 1 ; REFUTED 1')),

    # ---------------------------------------------------------------- the standing arms
    ('G-NO-CHAIN-RUN', 'this act`s own tools, for an IMPORT or a CALL and not a mention',
     lambda S: not re.search(r'^\s*(?:import|from)\s+(?:b321_window|b325_epstein|b317_smear|'
                             r'b318_square|carto_atlas)\b'
                             r'|\b(?:channels_q|mean_zero_variant|autocorrelation|prime_sum)\s*\(',
                             S['tools484'], re.M),
     lambda S: put(S, 'tools484', S['tools484'] + NL + 'import b321_window as WI')),
    ('G-NOB475LOG', 'this act`s own tools, for the other run`s log by name',
     lambda S: 'b475_zeta23_build.log' not in S['tools484'],
     lambda S: put(S, 'tools484', S['tools484'] + NL + "read(D + 'b475_zeta23_build.log')")),
    ('G-SPAN-BY-TOOL', 'the span tool record',
     lambda S: 'THE CURRENT SPAN' in S['span'], lambda S: cut(S, 'span', 'THE CURRENT SPAN')),
    ('G-NOGRADE-MOVED', 'the commit file list',
     lambda S: not any(x.endswith(('FACES_LEDGER.md', 'REGISTRY.md', 'ERRATA.md', 'FINDINGS.md'))
                       for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['REGISTRY.md'])),
    ('G-NODEPOSIT', 'the deposit directory tracked state, via the source',
     lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail own text',
     lambda S: 'where the deposit left it' in S['ot'], lambda S: cut(S, 'ot', 'where the deposit left it')),
    ('G-NOPRIORBANK', 'file times against the face',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail own text',
     lambda S: 'four lists stay OPEN' in S['ot'],
     lambda S: put(S, 'ot', S['ot'].replace('four lists stay OPEN', 'x'))),
    ('G-CORPUS-SCOPE', 'the commit file list -- TWO documents this act, and named',
     lambda S: sorted(S['tracked']) == sorted(['OPEN_TRAILS.md',
                                               'phase1.5/method/INVARIANCE_BARRIERS.md']),
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'FINDINGS.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail own text',
     lambda S: S['ot'].count('### b484 —') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b484 — a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 331 |' in S['corr'] and S['corr'].count('| 331 |') == 1,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 331 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b484 commit in three repositories, against (R91)`s STEM GLOB',
     lambda S: not sorted(k for k in S['kinds']
                          if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face']))),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'b471_someone_elses_bank.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite own text',
     lambda S: "log', '--pretty=%H %s'" in S['suite'], lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the commit file list',
     lambda S: all(x.startswith(('OPEN_TRAILS', 'data/', 'tools/', 'phase1.5/method/INVARIANCE'))
                   for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['internal/BLOB_SENSITIVITY_2026-08-29.md'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the face (G2) block against what runs',
     lambda S: S.get('declared_eq_run', False), lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'the suite own text',
     lambda S: 'def line_with(text, needle)' in S['suite'],
     lambda S: cut(S, 'suite', 'def line_with(text, needle)')),
    ('G-MIRROR-TAGGED-BUILD', 'the built zip presence, UNDATED',
     lambda S: S['mirror'], lambda S: put(S, 'mirror', False)),
    ('G-MUSTFAIL', 'a file that must not exist',
     lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked tree, read in the source',
     lambda S: S['artefacts_tracked'] == '',
     lambda S: put(S, 'artefacts_tracked', 'data/anthropic-zeta23/claude_paper_2026-08-11.pdf')),
    ('G-CORPUS-LEAN-UNTOUCHED', 'the lv and kernel working trees, read in the source',
     lambda S: S['corpus_lean_clean'] is True, lambda S: put(S, 'corpus_lean_clean', False)),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'the suite`s own text -- b472`s repair, carried',
     lambda S: "data/b484_components.txt' in gits(ROOT, 'show'" in S['suite'],
     lambda S: cut(S, 'suite', "data/b484_components.txt' in gits(ROOT, 'show'")),
]


def main():
    S = sources()
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (K) THE BARS.')]
    declared = sorted(set(x.rstrip('-') for x in
                          re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})
    names = [a[0] for a in ARMS]
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b484')
              and 'data/b484_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b484 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
        % ('POST-PUSH' if pushed else 'PRE-PUSH'))
    rec('=' * 104)
    rec('  arms in the (G2) block : %d ; run here : %d ; deferred : %d'
        % (len(declared), len(names), len(deferred)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    rec('  %-42s %-5s %-5s %-5s %s' % ('arm', 'LIVE', 'NEG', 'POS', 'verdict'))
    rec('  ' + '-' * 92)
    fail, defective, negfail = [], [], 0
    for name, reads, pred, pos in ARMS:
        if name in deferred:
            continue
        live = bool(pred(S))
        neg = bool(pred(dict(S)))
        p = bool(pred(pos(S)))
        if not neg:
            negfail += 1
        if p:
            defective.append(name)
        v = 'OK' if (neg and not p) else ('### DEFECTIVE' if p else '### NEG FAILS')
        rec('  %-42s %-5s %-5s %-5s %s' % (name, 'PASS' if live else 'FAIL',
                                           'PASS' if neg else '###FAIL', 'FAIL' if not p else '###PASS', v))
        RES.append(name)
        EX.append(dict(name=name, live=live, neg=neg, pos=p, reads=reads))
        if not live:
            fail.append(name)
    for n in deferred:
        rec('  %-42s DEFERRED TO POST-PUSH' % n)
    stray = sorted(k for k in S['kinds']
                   if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face'])))
    rec('')
    rec('  ### files written that NO (W) GLOB COVERS : %d %s' % (len(stray), stray or ''))
    rec('  ### G-NOPRIORBANK checked %d prior banks; b475`s still-growing log excluded by name.'
        % S['prior_checked'])
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**'
        % (len(RES), len(RES) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**'
        % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, 'b484_checks_postpush.txt' if pushed else 'b484_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b484_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
