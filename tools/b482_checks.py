# -*- coding: utf-8 -*-
"""b482_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
FACE = os.path.join(D, 'b482_registration_2026-09-22.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b482_ferry.txt')),
        ferry2=read(os.path.join(D, 'b482_ferry_amendment.txt')),
        scan=read(os.path.join(D, 'b482_ferry_amendment_scan.txt')),
        scan1=read(os.path.join(D, 'b482_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b482_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b482_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b482_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b482_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b482_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b485_closing.txt')),
        addendum=read(os.path.join(D, 'b482_addendum.txt')),
        comp=read(os.path.join(D, 'b482_components.txt')),
        desk=read(os.path.join(D, 'b482_desk_notes.txt')),
        span=read(os.path.join(D, 'b482_span_notes.txt')),
        res=json.loads(read(os.path.join(D, 'b482_results.json')) or '{}'),
        sc=json.loads(read(os.path.join(D, 'b482_scores.json')) or '{}'),
        sv=json.loads(read(os.path.join(D, 'b482_survey.json')) or '{}'),
        xp=read(os.path.join(D, 'anthropic-zeta23', 'formal-math', 'zeta23',
                             'Challenge', 'XiPrime.lean')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b482_checks.py')),
        tools482=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b482_') and f.endswith('.py') and f != 'b482_checks.py'),
        rtracked=gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-simplicity'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b482.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b482 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b482_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b482 --'):
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
             if re.match(r'^b4[0-7][0-9]_|^b48[0-9]_', f) and not f.startswith('b482_') and f not in LIVE]
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


def P(S):
    return (S['res'] or {}).get('placement') or {}


def C(S):
    return (S['res'] or {}).get('counts') or {}


ARMS = [
    ('G-RECEIPT-IN-FULL', 'both banked ferries',
     lambda S: ('paste ends (part 2 of 2)' in S['ferry']
                and 'paste ends (part 1 of 1)' in S['ferry2']),
     lambda S: cut(S, 'ferry2', 'paste ends (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE from each scan',
     lambda S: ('0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:')
                and '0 HIT(S) REPORTED' in line_with(S['scan1'], 'VERDICT:')),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-ZERO', 'both banked scans',
     lambda S: '(R81) FLAGS : 0' in S['scan'] and '(R81) FLAGS : 0' in S['scan1'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b485`s closing AND the ledger',
     lambda S: ('THE COMMITS, EACH READ BACK BY ls-remote' in S['prior']
                and S['corr'].count('| 332 |') == 1),
     lambda S: cut(S, 'prior', 'THE COMMITS, EACH READ BACK BY ls-remote')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, for the act`s own registration',
     lambda S: (os.path.exists(os.path.join(D, 'b482_ferry.txt')) and 'b482' in S['face']
                and not os.path.exists(os.path.join(D, 'b479_registration_2026-09-22.txt'))),
     lambda S: cut(S, 'face', 'b482')),

    # -------------------------------------------------- the b479 halt
    ('G-B479-HALT-PROVED', 'the survey bank -- the search over every ferry file',
     lambda S: len(S['sv']['b479_hits']) == 0,
     lambda S: put(S, 'sv', dict(S['sv'], b479_hits=['b477_ferry.txt']))),
    ('G-B479-CONTROL-RAN', 'the survey bank -- the POSITIVE control the halt rests on',
     lambda S: len(S['sv']['b479_control']) >= 1 and 'b482_ferry.txt' in S['sv']['b479_control'],
     lambda S: put(S, 'sv', dict(S['sv'], b479_control=[]))),
    ('G-B479-NOT-RECONSTRUCTED', 'this act`s components and trail, for any b479 content',
     lambda S: not re.search(r'b479[^\n]{0,40}(?:Component|finds|found|verdict|scored)',
                             S['comp'] + S['desk'], re.I),
     lambda S: put(S, 'comp', S['comp'] + NL + 'b479 Component 1 finds the seven classes')),

    # -------------------------------------------------- component 1
    ('G-C1-PIN-MATCHES', 'the survey bank against the face',
     lambda S: S['sv']['pin'].startswith('fbdc36b') and 'fbdc36b' in S['face'],
     lambda S: put(S, 'sv', dict(S['sv'], pin='deadbeef'))),
    ('G-C1-SIX-VERBATIM', 'the clone file itself against the components record',
     lambda S: (len(S['sv']['six']) == 6
                and all(d['stmt'].split(NL)[0] in S['comp'] for d in S['sv']['six'])
                and all(d['name'] in S['xp'] for d in S['sv']['six'])),
     lambda S: put(S, 'sv', dict(S['sv'], six=S['sv']['six'][:3]))),
    ('G-C1-ALL-SORRY-SAID', 'the clone file and the components record',
     lambda S: (S['xp'].count('sorry') >= 6 and S['sv']['sorries'] >= 6
                and 'sorry' in S['comp'] and 'NOT THEOREMS HELD' in S['comp']),
     lambda S: cut(S, 'comp', 'NOT THEOREMS HELD')),
    ('G-C1-COMPARATOR-SAME-SET', 'the comparator against the file`s own theorems',
     lambda S: (sorted(S['sv']['comparator']['theorem_names'])
                == sorted(d['name'] for d in S['sv']['six'])),
     lambda S: put(S, 'sv', dict(S['sv'], comparator=dict(
         S['sv']['comparator'], theorem_names=['x'])))),
    ('G-C1-AXIOMS-PRINTED', 'the comparator against the components record',
     lambda S: all(a in S['comp'] for a in S['sv']['comparator']['permitted_axioms']),
     lambda S: cut(S, 'comp', 'Classical.choice')),

    # -------------------------------------------------- component 2
    ('G-C2-STATEMENTS-NOT-DOCSTRINGS', 'the components record, for docstring syntax',
     lambda S: ('/--' not in S['comp'] and 'theorem spectral_cannon' in S['comp']
                and 'theorem transversal_generic_empty' in S['comp']),
     lambda S: put(S, 'comp', S['comp'] + NL + '/-- a docstring that must not be here -/')),
    ('G-C2-REHEARSED-BOTH-POLARITIES', 'the survey bank, for the (R70) rehearsal`s two halves',
     lambda S: ('THE NEGATIVE HALF' in S['extract'] and 'DID NOT RETURN' in S['extract']
                and 'xiPrime_over_xi_re_pos' in S['extract']),
     lambda S: cut(S, 'extract', 'DID NOT RETURN')),
    ('G-C2-TAGS-NAMED', 'the components record, for every tag read at',
     lambda S: ('v1.5' in S['comp'] and 'v0.1.0' in S['comp']
                and 'DEPOSITED-v1.1.2' in S['comp'] + S['face']),
     lambda S: cut(S, 'comp', 'v0.1.0')),
    ('G-C2-SIMPLICITY-IS-INTEGER-ONLY', 'the survey`s own quoted statements',
     lambda S: all(('ξ' not in c['text'] and 'ℂ' not in c['text'])
                   for c in S['sv']['corpus'] if 'codim' in c['name'] or 'transversal' in c['name']),
     lambda S: put(S, 'sv', dict(S['sv'], corpus=[
         dict(c, text=c['text'] + ' ξ') if 'codim' in c['name'] else c
         for c in S['sv']['corpus']]))),

    # -------------------------------------------------- component 3
    ('G-C3-EVERY-CELL-SCORED', 'the results bank',
     lambda S: (len(P(S)) == 6 and all(len(v) == 4 for v in P(S).values())
                and sum(C(S).values()) == 24),
     lambda S: put(S, 'res', dict(S['res'], counts={'APART': 3}))),
    ('G-C3-DECIDING-CLAUSE-QUOTED', 'the components record, for every non-APART kind',
     lambda S: ('THE DECIDING CLAUSE FOR EVERY NON-' in S['comp']
                and 'THE SHARED TERM IS' in S['comp']
                and C(S).get('TOUCHES', 0) > 0),
     lambda S: cut(S, 'comp', 'THE SHARED TERM IS')),
    ('G-C3-TWO-REVERSE-READS', 'the components record',
     lambda S: ('WHAT THE SIX STATE THAT THE CORPUS DOES NOT' in S['comp']
                and 'WHAT THE CORPUS STATES THAT THE SIX DO NOT' in S['comp']),
     lambda S: cut(S, 'comp', 'WHAT THE CORPUS STATES THAT THE SIX DO NOT')),
    ('G-C3-NO-GRADE-CONFERRED', 'the components record, for any grade word on a corpus object',
     lambda S: not re.search(r'\b(?:DERIVES|PROVED AT|graded|GRADE CONFERRED ON)\b',
                             S['comp'].replace('NO GRADE IS CONFERRED', '')),
     lambda S: put(S, 'comp', S['comp'] + NL + 'spectral_cannon is graded DERIVES by this act')),

    # -------------------------------------------------- the expectations
    ('G-N1-SCORED', 'the scores bank against the results bank',
     lambda S: sc(S, 'N1') == 'REFUTED' and C(S).get('SAME OBJECT', 0) == 0,
     lambda S: put(S, 'res', dict(S['res'], counts=dict(C(S), **{'SAME OBJECT': 2})))),
    ('G-N2-SCORED', 'the scores bank against the clone file itself',
     lambda S: sc(S, 'N2') == 'HELD' and 'transversal' not in S['xp'],
     lambda S: put(S, 'xp', S['xp'] + NL + 'theorem transversal_uniform : True')),
    ('G-N3-SCORED', 'the scores bank against the clone file`s own counting functions',
     lambda S: ('FALSE OF TWO OF ITS SIX MEMBERS' in sc(S, 'N3')
                and 'Ncount' in S['xp'] and 'N0simple' in S['xp']),
     lambda S: put(S, 'sc', dict(S['sc'], N3=dict(S['sc']['N3'], verdict='HELD')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk bank',
     lambda S: ("THE SEAT'S OWN" in S['face']
                and 'REGISTERED 3 ; HELD 1 ; HELD-IN-PART 1 ; REFUTED 1' in S['desk']),
     lambda S: cut(S, 'desk', 'REGISTERED 3 ; HELD 1 ; HELD-IN-PART 1 ; REFUTED 1')),

    # -------------------------------------------------- the standing arms
    ('G-NOTHING-IMPORTED', 'the commit file lists, for any .lean or clone path',
     lambda S: not any(x.endswith('.lean') or 'anthropic-zeta23' in x
                       for x in list(S['tracked']) + list(S['rtracked'])),
     lambda S: put(S, 'rtracked', list(S['rtracked']) + ['data/anthropic-zeta23/x.lean'])),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked tree, read in the source',
     lambda S: S['artefacts_tracked'] == '',
     lambda S: put(S, 'artefacts_tracked', 'data/anthropic-zeta23/claude_paper_2026-08-11.pdf')),
    ('G-NO-LEAN-RUN', 'this act`s own tools, for a build or a Lean invocation',
     # ### **THE FIRST PATTERN REQUIRED WHITESPACE ITS OWN POSITIVE CONTROL DID NOT HAVE.**
     # ### `lake\s+build` cannot match `["lake","build"]`, which is how a build is actually spelled in a
     # ### `subprocess` call -- so the arm could not fail, and its control said so.
     # ### **AN ARM THAT CANNOT FAIL IS NOT AN ARM.** ### Widened to allow the separators
     # ### a real invocation puts between the two words.
     lambda S: not re.search(r'\blake\b[^\n]{0,12}\bbuild\b|lean\s+--|LEAN_PATH|subprocess[^\n]{0,40}\blean\b',
                             S['tools482']),
     lambda S: put(S, 'tools482', S['tools482'] + NL + 'subprocess.run(["lake","build","Zeta23"])')),
    ('G-NOB475LOG', 'this act`s own tools, for the other run`s log by name',
     lambda S: 'b475_zeta23_build.log' not in S['tools482'],
     lambda S: put(S, 'tools482', S['tools482'] + NL + "open('b475_zeta23_build.log')")),
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
    ('G-CORPUS-SCOPE', 'the commit file list',
     lambda S: S['tracked'] == ['OPEN_TRAILS.md'],
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'FINDINGS.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail own text',
     lambda S: S['ot'].count('### b482 —') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b482 — a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 333 |' in S['corr'] and S['corr'].count('| 333 |') == 1,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 333 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b482 commit in three repositories, against (R91)`s STEM GLOB',
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
    ('G-CORPUS-LEAN-UNTOUCHED', 'the lv, kernel AND simplicity working trees, in the source',
     lambda S: S['corpus_lean_clean'] is True, lambda S: put(S, 'corpus_lean_clean', False)),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'the suite`s own text -- b472`s repair, carried',
     lambda S: "data/b482_components.txt' in gits(ROOT, 'show'" in S['suite'],
     lambda S: cut(S, 'suite', "data/b482_components.txt' in gits(ROOT, 'show'")),
]


def main():
    S = sources()
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (K) THE BARS.')]
    declared = sorted(set(x.rstrip('-') for x in
                          re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})
    names = [a[0] for a in ARMS]
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b482')
              and 'data/b482_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b482 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b482_checks_postpush.txt' if pushed else 'b482_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b482_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
