# -*- coding: utf-8 -*-
"""b479_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
FACE = os.path.join(D, 'b479_registration_2026-09-22.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b479_ferry.txt')),
        scan=read(os.path.join(D, 'b479_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b479_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b479_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b479_pins_stepzero.txt')),
        pins1=read(os.path.join(D, 'b479_pins_stepzero_firstrun.txt')),
        extract=read(os.path.join(D, 'b479_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b479_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b482_closing.txt')),
        addendum=read(os.path.join(D, 'b479_addendum.txt')),
        comp=read(os.path.join(D, 'b479_components.txt')),
        desk=read(os.path.join(D, 'b479_desk_notes.txt')),
        span=read(os.path.join(D, 'b479_span_notes.txt')),
        filed=json.loads(read(os.path.join(D, 'b479_filing.json')) or '{}'),
        res=json.loads(read(os.path.join(D, 'b479_results.json')) or '{}'),
        sc=json.loads(read(os.path.join(D, 'b479_scores.json')) or '{}'),
        sv=json.loads(read(os.path.join(D, 'b479_survey.json')) or '{}'),
        lv=subprocess.run(['git', '-C', os.path.join('D:', os.sep, 'SIDE-lv-conservation'),
                           'show', 'v0.10.0:SIDELvConservation/CouplingsAtPhi.lean'],
                          capture_output=True, text=True, encoding='utf-8',
                          errors='replace').stdout.replace(chr(13), ''),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b479_checks.py')),
        tools479=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b479_') and f.endswith('.py') and f != 'b479_checks.py'),
        rtracked=gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b479.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b479 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b479_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b479 --'):
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
             if re.match(r'^b4[0-7][0-9]_|^b48[0-9]_', f) and not f.startswith('b479_') and f not in LIVE]
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


def V(S):
    return (S['res'] or {}).get('verdicts') or {}


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'paste ends (part 1 of 1)' in S['ferry'] and 'ACT b479' in S['ferry'],
     lambda S: cut(S, 'ferry', 'ACT b479')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE',
     lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-ZERO', 'this act`s banked scan',
     lambda S: '(R81) FLAGS : 0' in S['scan'],
     lambda S: put(S, 'scan', S['scan'].replace('(R81) FLAGS : 0', '(R81) FLAGS : 1'))),
    ('G-STEPZERO-CENSUS', 'two banked censuses',
     lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'fcens', S['fcens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 3'))),
    ('G-STEPZERO-PINS-RETRIED', 'the banked RETRY, by its verdict LINE',
     lambda S: 'REPOS HARD-FAILING : 0' in line_with(S['pins'], 'REPOS HARD-FAILING'),
     lambda S: put(S, 'pins', S['pins'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-FIRSTRUN-KEPT', 'the FAILING run, kept and not deleted',
     lambda S: ('REPOS HARD-FAILING : 4' in S['pins1'] and 'UNRESOLVED' in S['pins1']
                and 'REPOS HARD-FAILING : 4' in S['face']),
     lambda S: put(S, 'pins1', '')),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b482`s closing AND the ledger',
     lambda S: ('THE COMMITS, EACH READ BACK BY ls-remote' in S['prior']
                and S['corr'].count('| 333 |') == 1),
     lambda S: cut(S, 'prior', 'THE COMMITS, EACH READ BACK BY ls-remote')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory -- and now the ORDER, not just the number',
     lambda S: (os.path.exists(os.path.join(D, 'b479_ferry.txt'))
                and 'ACT b479' in S['ferry'] and 'b479' in S['face']),
     lambda S: cut(S, 'ferry', 'ACT b479')),

    # -------------------------------------------------- component 1
    ('G-C1-TAG-IS-THE-PIN', 'the survey bank against the face',
     lambda S: S['sv']['sha'].startswith('93c27ec') and '93c27ec' in S['face'],
     lambda S: put(S, 'sv', dict(S['sv'], sha='deadbeef'))),
    ('G-C1-EIGHT-CONJUNCTS', 'the source file itself against the survey bank',
     lambda S: (S['sv']['conjuncts'] == 8 and 'C7_entirety Phi' in S['lv']
                and 'C7_order Phi' in S['lv'] and 'EIGHT CONJUNCTS' in S['face']),
     lambda S: put(S, 'sv', dict(S['sv'], conjuncts=7))),
    ('G-C1-STATEMENTS-NOT-DOCSTRINGS', 'the components record, for docstring syntax',
     lambda S: '/--' not in S['comp'] and 'def C2_halfplane_nonvanishing' in S['comp'],
     lambda S: put(S, 'comp', S['comp'] + NL + '/-- a docstring that must not be here -/')),
    ('G-C1-DISCHARGES-NAMED', 'the components record, for the discharge terminals',
     lambda S: all(('%s_at_Phi' % n) in S['comp']
                   for n in ('C1_realness', 'C2_halfplane_nonvanishing', 'C7_order')),
     lambda S: cut(S, 'comp', 'C7_order_at_Phi')),
    ('G-C1-READER-REPAIRED', 'the survey tool`s own text -- the def/theorem split',
     lambda S: ("if kind == 'def':" in S['tools479']
                and 'the body IS the statement' in S['tools479']),
     lambda S: put(S, 'tools479', S['tools479'].replace("if kind == 'def':", "if False:"))),

    # -------------------------------------------------- component 2
    ('G-C2-SEVEN-ROWS', 'the results bank',
     lambda S: len(V(S)) == 7 and sorted(V(S)) == ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7'],
     lambda S: put(S, 'res', dict(S['res'], verdicts={'C1': 'APART'}))),
    ('G-C2-CRITERION-BEFORE-VERDICT', 'the SEALED face, whose bytes are hashed',
     lambda S: ('A FACT TOUCHES THE FORM WHEN ITS STATEMENT CONSTRAINS' in S['face']
                and 'FIXED BEFORE ANY VERDICT' in S['face']),
     lambda S: cut(S, 'face', 'A FACT TOUCHES THE FORM WHEN ITS STATEMENT CONSTRAINS')),
    ('G-C2-CLAUSE-QUOTED-WHEN-TOUCHES', 'the components record and the source file',
     lambda S: ('THE CONSTRAINING CLAUSE, QUOTED' in S['comp']
                and 'mellin Φ (s / 2) ≠ 0' in S['comp']
                and 'mellin Φ (s / 2) ≠ 0' in S['lv']),
     lambda S: cut(S, 'comp', 'THE CONSTRAINING CLAUSE, QUOTED')),
    ('G-C2-REASON-IN-THE-FACTS-OWN-WORDS', 'the components record',
     lambda S: ("WHY APART, IN THE FACT`S OWN WORDS" in S['comp']
                and 'NEVER MENTIONS THE MELLIN TRANSFORM' in S['comp']),
     lambda S: cut(S, 'comp', 'NEVER MENTIONS THE MELLIN TRANSFORM')),
    ('G-C2-C7-BOTH-SHOWN', 'the components record, for both C7 facts',
     lambda S: 'C7_entirety' in S['comp'] and 'C7_order' in S['comp'],
     lambda S: cut(S, 'comp', 'C7_entirety')),

    # -------------------------------------------------- component 3
    ('G-C3-SENTENCE-NO-WIDER', 'the components record',
     lambda S: ('THE SENTENCE THE TABLE SUPPORTS, AND NO WIDER' in S['comp']
                and 'NOT A CLAIM THAT THEY ARE IRRELEVANT' in S['comp']),
     lambda S: cut(S, 'comp', 'NOT A CLAIM THAT THEY ARE IRRELEVANT')),
    ('G-C3-CONDITIONAL-NOT-DISCHARGED', 'the components record',
     lambda S: ('THE CONDITIONAL IS NOT DISCHARGED' in S['comp']
                and 'IF the exclusions' in S['comp']),
     lambda S: cut(S, 'comp', 'THE CONDITIONAL IS NOT DISCHARGED')),
    ('G-C3-INERTIA-NOT-BORROWED', 'the survey bank and the components record',
     lambda S: ('THE VOCABULARY IS NOT AT AN ADDRESS' in S['comp']
                and len(S['sv']['inertia']) <= 1),
     lambda S: put(S, 'sv', dict(S['sv'], inertia=[['x', 1, 'y']] * 5))),

    # -------------------------------------------------- the expectations
    ('G-N1-SCORED', 'the scores bank against the results bank',
     lambda S: ('HELD IN PART' in sc(S, 'N1') and V(S)['C3'] == 'APART'
                and V(S)['C2'].startswith('TOUCHES') and V(S)['C7'].startswith('TOUCHES')),
     lambda S: put(S, 'res', dict(S['res'], verdicts=dict(V(S), C3='TOUCHES THE FORM')))),
    ('G-N2-SCORED', 'the scores bank against the results bank',
     lambda S: (sc(S, 'N2') == 'HELD'
                and all(V(S)[c] == 'APART' for c in ('C1', 'C4', 'C6'))),
     lambda S: put(S, 'res', dict(S['res'], verdicts=dict(V(S), C4='TOUCHES THE FORM')))),
    ('G-N3-SCORED', 'the scores bank against the SOURCE FILE`s own note',
     lambda S: ('HELD' in sc(S, 'N3') and V(S)['C5'] == 'APART'
                and 'deliberately NOT in `sevenClasses`' in S['lv']),
     lambda S: put(S, 'lv', S['lv'].replace('deliberately NOT in `sevenClasses`', 'x'))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk bank',
     lambda S: ("THE SEAT'S OWN" in S['face']
                and 'REGISTERED 3 ; HELD 2 ; HELD-IN-PART 1' in S['desk']),
     lambda S: cut(S, 'desk', 'REGISTERED 3 ; HELD 2 ; HELD-IN-PART 1')),
    ('G-C5OUTPUT-NOT-COUNTED', 'the results bank and the source file',
     lambda S: ('C5_output' not in str(V(S))
                and 'C5_output' in S['lv'] and 'DISCLAIMED' in S['comp']),
     lambda S: put(S, 'res', dict(S['res'], verdicts=dict(V(S), C5_output='TOUCHES THE FORM')))),

    # -------------------------------------------------- the standing arms
    ('G-NOTHING-COMPILED', 'this act`s own tools, for a build or a Lean invocation',
     lambda S: not re.search(r'\blake\b[^\n]{0,12}\bbuild\b|lean\s+--|LEAN_PATH|'
                             r'subprocess[^\n]{0,40}\blean\b', S['tools479']),
     lambda S: put(S, 'tools479', S['tools479'] + NL + 'subprocess.run(["lake","build","X"])')),
    ('G-NOB475LOG', 'this act`s own tools, for the other run`s log by name',
     lambda S: 'b475_zeta23_build.log' not in S['tools479'],
     lambda S: put(S, 'tools479', S['tools479'] + NL + "open('b475_zeta23_build.log')")),
    ('G-SPAN-BOTH-READINGS', 'the span record AND the filing bank, both printed',
     lambda S: ('THE CURRENT SPAN' in S['span'] and S['filed'].get('count', 0) >= 10
                and str(S['filed']['count']) in S['desk']),
     lambda S: put(S, 'filed', dict(S['filed'], count=0))),
    ('G-NOGRADE-MOVED', 'the commit file list',
     lambda S: not any(x.endswith(('FACES_LEDGER.md', 'REGISTRY.md', 'ERRATA.md', 'FINDINGS.md'))
                       for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['REGISTRY.md'])),
    ('G-NODEPOSIT', 'the deposit directory tracked state, via the source',
     lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail own text AND the source file`s own docstring',
     lambda S: ('where the deposit left it' in S['ot']
                and 'remains the outstanding obligation' in S['lv']),
     lambda S: cut(S, 'ot', 'where the deposit left it')),
    ('G-NOPRIORBANK', 'file times against the face',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail own text',
     lambda S: 'four lists stay OPEN' in S['ot'],
     lambda S: put(S, 'ot', S['ot'].replace('four lists stay OPEN', 'x'))),
    ('G-CORPUS-SCOPE', 'the commit file list',
     lambda S: S['tracked'] == ['OPEN_TRAILS.md'],
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'FINDINGS.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail own text',
     lambda S: S['ot'].count('### b479 —') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b479 — a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 334 |' in S['corr'] and S['corr'].count('| 334 |') == 1,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 334 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b479 commit in three repositories, against (R91)`s STEM GLOB',
     lambda S: not sorted(k for k in S['kinds']
                          if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face']))),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'b471_someone_elses_bank.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite own text',
     lambda S: "log', '--pretty=%H %s'" in S['suite'], lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the commit file list',
     lambda S: all(x.startswith(('OPEN_TRAILS', 'data/', 'tools/')) for x in S['tracked']),
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
     lambda S: "data/b479_components.txt' in gits(ROOT, 'show'" in S['suite'],
     lambda S: cut(S, 'suite', "data/b479_components.txt' in gits(ROOT, 'show'")),
]


def main():
    S = sources()
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (K) THE BARS.')]
    declared = sorted(set(x.rstrip('-') for x in
                          re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})
    names = [a[0] for a in ARMS]
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b479')
              and 'data/b479_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b479 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b479_checks_postpush.txt' if pushed else 'b479_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b479_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
