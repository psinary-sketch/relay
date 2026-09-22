# -*- coding: utf-8 -*-
"""b481_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb.
### ### **THE ARMS ARE RE-POINTED ONE AT A TIME, NOT WHOLESALE** -- b480 recorded three instances
### of `G-CARRIED-TOOLS-REPOINTED` in a single act from a global substitution, and this file was
### written by reading each carried arm against THIS act's banks before its pointer moved.
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
FACE = os.path.join(D, 'b481_registration_2026-09-22.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b481_ferry.txt')),
        ferry2=read(os.path.join(D, 'b482_ferry.txt')),
        scan=read(os.path.join(D, 'b481_ferry_scan.txt')),
        scan2=read(os.path.join(D, 'b482_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b481_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b481_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b481_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b481_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b481_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        # ### **THE PRIOR CLOSED ACT IS b477**, not b480: b477 was re-issued under (R87) and closed
        # ### after b480's bank was written. ### Read from the record, not from the carried pointer.
        prior=read(os.path.join(D, 'b477_closing.txt')),
        prior480=read(os.path.join(D, 'b480_closing.txt')),
        addendum=read(os.path.join(D, 'b481_addendum.txt')),
        comp=read(os.path.join(D, 'b481_components.txt')),
        desk=read(os.path.join(D, 'b481_desk_notes.txt')),
        bank=read(os.path.join(D, 'b481_the_circulation_gate_read.txt')),
        span=read(os.path.join(D, 'b481_span_notes.txt')),
        scores=json.loads(read(os.path.join(D, 'b481_scores.json')) or '{}'),
        sv=json.loads(read(os.path.join(D, 'b481_survey.json')) or '{}'),
        wl=json.loads(read(os.path.join(D, 'b481_worklist.json')) or '{}'),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b481_checks.py')),
        reg=read(os.path.join(PP, 'REGISTRY.md')),
        instr=read(os.path.join(PP, 'phase1.5', 'method', 'INSTRUMENTS.md')),
        b395=read(os.path.join(D, 'b395_components.txt')) + read(os.path.join(D, 'b395_closing.txt')),
        tools481=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b481_') and f.endswith('.py') and f != 'b481_checks.py'),
        # ### ### **THE FOUR SITES' BYTES, AS GIT SEES THEM.** ### (R89) forbids no read, but this
        # ### act forbids itself every WRITE to a site -- so the arm asks git, not the act's own word.
        sites_clean=(gits(PP, 'status', '--porcelain', '--', 'README.md', 'SPIRAL_MAP.md',
                          'REGISTRY.md') == ''),
        rtracked=gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b481.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b481 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b481_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b481 --'):
                k |= set(os.path.basename(x) for x in
                         gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                k.add(os.path.basename(l[3:].strip()))
    # ### **b475's LOG IS STILL BEING WRITTEN AND IS NOT THIS ACT'S**; b482's banked ferry belongs to
    # ### the act it names. ### Both are excluded BY NAME so the collector reports this act's writes.
    k -= {'b475_zeta23_build.log', 'b477_entries.jsonl', 'b477_gram.log',
          'b482_ferry.txt', 'b482_ferry_scan.txt'}
    S['kinds'] = k
    # ### ### **THE ARM IS NARROWED ON A STATED GROUND, NOT WEAKENED.** ### Its widened regex now
    # ### reaches b475's and b477's banks, and `b475_zeta23_build.log` is NEWER than the face --
    # ### because **A DETACHED PROCESS STARTED BY ANOTHER ACT IS STILL APPENDING TO IT.** ### That is
    # ### not this act touching a prior bank, and the arm is meant to catch this act. ### The three
    # ### files the two live runs own are excluded BY NAME, exactly as the kinds collector excludes
    # ### them; ### **EVERY OTHER PRIOR BANK, b400 THROUGH b480, IS STILL CHECKED.**
    LIVE = {'b475_zeta23_build.log', 'b477_entries.jsonl', 'b477_gram.log'}
    prior = [f for f in os.listdir(D)
             if re.match(r'^b4[0-7][0-9]_|^b48[0]_', f) and f not in LIVE]
    S['prior_checked'] = len(prior)
    S['live_excluded'] = sorted(f for f in LIVE if os.path.exists(os.path.join(D, f)))
    S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)
    return S


def globs_of(face):
    """### (R85): THE FACE'S (W) SECTION AS A LIST OF GLOBS. ### Every backticked path in the write-list
    ### table is a pattern -- TOOL NAMES INCLUDED, since a tool this act creates is itself written."""
    w = face[face.index('### (W) THE WRITE LIST'):face.index('### (Z) THE NOTHINGS')]
    return [g.split('/')[-1] for g in re.findall(r'`([^`]+)`', w)]


CP = "(c')"

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'paste ends (part 1 of 2)' in S['ferry'],
     lambda S: cut(S, 'ferry', 'paste ends (part 1 of 2)')),
    ('G-PART2-BANKED-NOT-RUN', 'b482`s banked ferry and this act`s own banks',
     lambda S: ('paste ends (part 2 of 2)' in S['ferry2']
                and 'ACT b482' in S['ferry2']
                and not os.path.exists(os.path.join(D, 'b482_registration_2026-09-22.txt'))
                and not os.path.exists(os.path.join(D, 'b482_components.txt'))),
     lambda S: cut(S, 'ferry2', 'paste ends (part 2 of 2)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE',
     lambda S: ('0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:')
                and '0 HIT(S) REPORTED' in line_with(S['scan2'], 'VERDICT:')),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-ZERO', 'both banked scans',
     lambda S: '(R81) FLAGS : 0' in S['scan'] and '(R81) FLAGS : 0' in S['scan2'],
     lambda S: put(S, 'scan2', S['scan2'].replace('(R81) FLAGS : 0', '(R81) FLAGS : 1'))),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b477 closing -- the prior closed act',
     lambda S: 'row 328' in S['prior'], lambda S: cut(S, 'prior', 'row 328')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),

    # ---------------------------------------------------------------- (R89)'s three conditions
    ('G-R89-NO-BUILD-STARTED', 'this act`s own tools, for any build or launch',
     lambda S: not re.search(r'lake\s+build|Start-Process|subprocess\.Popen|detached_run|LEAN_PATH',
                             S['tools481']),
     lambda S: put(S, 'tools481', S['tools481'] + NL + 'subprocess.Popen(["lake", "build", "Zeta23"])')),
    ('G-R89-NO-LOG-READ', 'this act`s own tools, for either running log by name',
     lambda S: not re.search(r'b475_zeta23_build\.log|b477_entries\.jsonl|b477_gram\.log', S['tools481']),
     lambda S: put(S, 'tools481', S['tools481'] + NL + "read(os.path.join(D, 'b475_zeta23_build.log'))")),
    ('G-R89-NOTHING-FETCHED', 'this act`s own tools, for any network call',
     lambda S: not re.search(r'urllib|requests\.|http[s]?://[a-z].*\)|curl |Invoke-WebRequest',
                             S['tools481']),
     lambda S: put(S, 'tools481', S['tools481'] + NL + 'urllib.request.urlopen(url)')),

    # ---------------------------------------------------------------- Component 1
    ('G-C1-GATE-QUOTED-WHOLE', 'REGISTRY.md itself against the components record',
     lambda S: (str(len(S['reg'].split(NL)[522])) in S['comp']
                and 'circulation gate' in S['comp']
                and 'a disagreement found is a finding filed, not a silent fix' in S['comp']),
     lambda S: cut(S, 'comp', 'a disagreement found is a finding filed, not a silent fix')),
    ('G-C1-TRIGGER-NAMED', 'REGISTRY.md itself against the components record',
     lambda S: ('Run when the %s validation job clears.' % CP) in S['reg'].split(NL)[522]
     and ('Run when the %s validation job clears.' % CP) in S['comp'],
     lambda S: cut(S, 'comp', 'Run when the %s validation job clears.' % CP)),
    ('G-C1-CPRIME-SEARCHED-WIDE', 'the survey bank against INSTRUMENTS.md itself',
     # ### **THE SEARCH MUST SEE THE CURLY APOSTROPHE.** ### A plain-ASCII matcher finds only the
     # ### gate's own line and would report the job "unique", which is the opposite conclusion.
     lambda S: (S['sv']['cprime_hits'] >= 4
                and any('INSTRUMENTS' in h[0] for h in S['sv']['cprime_lines'])
                and '(c′)' in S['instr']),
     lambda S: put(S, 'sv', dict(S['sv'], cprime_lines=[h for h in S['sv']['cprime_lines']
                                                        if 'INSTRUMENTS' not in h[0]]))),
    ('G-C1-ABSENT-NOT-FILLED', 'the components record and the worklist bank',
     lambda S: (S['wl']['cprime_state'] == 'ABSENT'
                and 'A NEAR NAME IS NOT THE' in S['comp']
                and 'WHAT WOULD SETTLE IT' in S['comp']),
     lambda S: put(S, 'wl', dict(S['wl'], cprime_state='CLEARED'))),

    # ---------------------------------------------------------------- Component 2
    ('G-C2-BOTH-RECORDS-QUOTED', 'the components record, for both record ids',
     lambda S: '21432399' in S['comp'] and '19675356' in S['comp']
     and 'Historical note:' in S['comp'] and 'NOWHERE IN THE CORPUS' in S['comp'],
     lambda S: cut(S, 'comp', '19675356')),
    ('G-C2-DECIDING-SENTENCE-QUOTED', 'b395`s bank against the components record',
     lambda S: ('A SEAT WITH CREDENTIALS AND A LIVE ROUTE' in S['b395']
                and 'A SEAT WITH CREDENTIALS AND A LIVE ROUTE' in S['comp']),
     lambda S: cut(S, 'comp', 'A SEAT WITH CREDENTIALS AND A LIVE ROUTE')),
    ('G-C2-VERDICT-FROM-THE-BANK', 'the worklist bank and b395`s own words',
     lambda S: (S['wl']['bar'] == 'CAPABILITY' and 'NOT THIS SEAT' in S['b395']
                and 'NO REASON GIVEN' not in S['comp']),
     lambda S: put(S, 'wl', dict(S['wl'], bar='PERMISSION'))),
    ('G-C2-FETCHES-CITED', 'the components record, for both fetching acts at their addresses',
     lambda S: ('b145' in S['comp'] and 'b337' in S['comp'] and 'b389' in S['comp']
                and 'b337_record.json' in S['comp']),
     lambda S: cut(S, 'comp', 'b337_record.json')),

    # ---------------------------------------------------------------- Component 3
    ('G-C3-FOUR-SITES-READ', 'the worklist bank',
     lambda S: (len(S['wl']['states']) == 5
                and 'README.md' in S['wl']['states'] and 'SPIRAL_MAP.md' in S['wl']['states']
                and 'REGISTRY.md' in S['wl']['states']
                and sum(1 for k in S['wl']['states'] if k.startswith('memory')) == 2),
     lambda S: put(S, 'wl', dict(S['wl'], states={'README.md': {}}))),
    ('G-C3-FIELD-TABLE', 'the components record, for all three fields at every site',
     lambda S: (S['comp'].count('AGREES') >= 10 and 'NOT STATED' in S['comp']
                and 'DISAGREEMENTS WITH REGISTRY : %d' % len(S['wl']['disagreements']) in S['comp']),
     lambda S: cut(S, 'comp', 'NOT STATED')),
    ('G-C3-NOT-STATED-DISTINCT', 'the components record',
     lambda S: ('`NOT STATED` IS NOT A DISAGREEMENT' in S['comp']
                and 'IT IS ALSO NOT A MATCH' in S['comp']),
     lambda S: cut(S, 'comp', 'IT IS ALSO NOT A MATCH')),
    ('G-C3-NO-SITE-EDITED', 'the four sites` working trees, read through git',
     lambda S: S['sites_clean'] is True, lambda S: put(S, 'sites_clean', False)),

    # ---------------------------------------------------------------- the expectations
    ('G-N1-SCORED', 'the scores bank against the worklist bank',
     lambda S: S['scores']['N1']['verdict'] == 'HELD' and S['wl']['cprime_state'] == 'ABSENT',
     lambda S: put(S, 'scores', dict(S['scores'], N1=dict(S['scores']['N1'], verdict='REFUTED')))),
    ('G-N2-SCORED', 'the scores bank against the worklist bank',
     lambda S: S['scores']['N2']['verdict'] == 'REFUTED' and S['wl']['bar'] == 'CAPABILITY',
     lambda S: put(S, 'scores', dict(S['scores'], N2=dict(S['scores']['N2'], verdict='HELD')))),
    ('G-N3-SCORED', 'the scores bank against the worklist bank',
     lambda S: (S['scores']['N3']['verdict'] == 'REFUTED'
                and len(S['wl']['disagreements']) < 2),
     lambda S: put(S, 'wl', dict(S['wl'], disagreements=[['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h']]))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk bank',
     lambda S: ('HELD' in S['desk'] and 'REFUTED' in S['desk']
                and 'REGISTERED 3 ; HELD 1 ; REFUTED 2' in S['desk']),
     lambda S: cut(S, 'desk', 'REGISTERED 3 ; HELD 1 ; REFUTED 2')),

    # ---------------------------------------------------------------- the standing arms
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
     lambda S: 'four lists stay OPEN' in S['ot'] or 'The four lists are open' in S['ot'],
     lambda S: put(S, 'ot', S['ot'].replace('four lists stay OPEN', 'x')
                   .replace('The four lists are open', 'x'))),
    ('G-CORPUS-SCOPE', 'the commit file list',
     lambda S: S['tracked'] == ['OPEN_TRAILS.md'],
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'FINDINGS.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail own text',
     lambda S: S['ot'].count('### b481 —') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b481 — a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 329 |' in S['corr'] and S['corr'].count('| 329 |') == 1,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 329 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b481 commit in three repositories, against (R85)`s GLOBS',
     lambda S: not sorted(k for k in S['kinds']
                          if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face']))),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'a_name_no_glob_covers.zzz'})),
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
     lambda S: "data/b481_components.txt' in gits(ROOT, 'show'" in S['suite'],
     lambda S: cut(S, 'suite', "data/b481_components.txt' in gits(ROOT, 'show'")),
]


def main():
    S = sources()
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (K) THE BARS.')]
    declared = sorted(set(x.rstrip('-') for x in
                          re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})
    names = [a[0] for a in ARMS]
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b481')
              and 'data/b481_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b481 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
        % ('POST-PUSH' if pushed else 'PRE-PUSH'))
    rec('=' * 104)
    rec('  arms in the (G2) block : %d ; run here : %d ; deferred : %d'
        % (len(declared), len(names), len(deferred)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    rec('  %-38s %-5s %-5s %-5s %s' % ('arm', 'LIVE', 'NEG', 'POS', 'verdict'))
    rec('  ' + '-' * 96)
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
        rec('  %-38s %-5s %-5s %-5s %s' % (name, 'PASS' if live else 'FAIL',
                                           'PASS' if neg else '###FAIL', 'FAIL' if not p else '###PASS', v))
        RES.append(name)
        EX.append(dict(name=name, live=live, neg=neg, pos=p, reads=reads))
        if not live:
            fail.append(name)
    for n in deferred:
        rec('  %-38s DEFERRED TO POST-PUSH' % n)
    stray = sorted(k for k in S['kinds']
                   if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face'])))
    rec('')
    rec('  ### files written that NO (W) GLOB COVERS : %d %s' % (len(stray), stray or ''))
    rec('  ### G-NOPRIORBANK checked %d prior banks; EXCLUDED BY NAME, as owned by the two live'
        % S['prior_checked'])
    rec('  ### detached runs and not by this act : %s' % ', '.join(S['live_excluded']))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**'
        % (len(RES), len(RES) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**'
        % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, 'b481_checks_postpush.txt' if pushed else 'b481_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b481_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
