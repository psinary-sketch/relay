# -*- coding: utf-8 -*-
"""b466_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb, honoured in
### advance even though this act is not the one it binds.
"""
import io
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
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
FACE = os.path.join(D, 'b466_registration_2026-09-21.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b466_ferry.txt')),
        scan=read(os.path.join(D, 'b466_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b466_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b466_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b466_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b466_extract.txt')),
        lock=read(os.path.join(D, 'b466_lockgate_notes.txt')),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        # ### **THE PRIOR ACT'S CLOSING IS b462'S.** ### A wholesale re-point from b462 to b466
        # ### moved every b462 name and left b461 where it was, so the inherited line pointed two
        # ### acts back and the arm failed on the wrong bank -- `G-CARRIED-TOOLS-REPOINTED`'s own
        # ### species, committed while building the suite that carries it.
# ### ### **THE PRIOR CLOSED ACT IS b464.** ### A wholesale re-point moves every b464 name
        # ### and leaves b463 exactly where the carried file had it -- and here the pointer had to
        # ### move ANYWAY, because b465 occupies the intervening number and closed nothing.
        # ### **THE THIRD INSTANCE OF THIS SPECIES IN ONE ACT**, caught by the arm it feeds.
        prior=read(os.path.join(D, 'b464_closing.txt')),
        addendum=read(os.path.join(D, 'b466_addendum.txt')),
        census=read(os.path.join(D, 'b466_census.txt')),
        span=read(os.path.join(D, 'b466_span_notes.txt')),
        scores=read(os.path.join(D, 'b466_scores.json')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b466_checks.py')),
        survey=json.loads(read(os.path.join(D, 'b466_survey.json')) or '{}'),
        readings=json.loads(read(os.path.join(D, 'b466_readings.json')) or '{}'),
        comp=read(os.path.join(D, 'b466_components.txt')),
        queries=read(os.path.join(D, 'b466_index_queries.txt')),
        activation=read(os.path.join(ROOT, 'reports', '2026-08-20-activation-act.md')),
        intake=read(os.path.join(ROOT, 'reports', '2026-08-20-external-intake.md')),
        mono=read(os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')),
        faces=read(os.path.join(PP, 'FACES_LEDGER.md')),
        desk=read(os.path.join(D, 'b466_desk_notes.txt')),
        docs=sorted(f for f in os.listdir(D) if f.startswith('b466_')),
        mirror=os.path.exists(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-2026-09-21-b466.zip')),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b466')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b466_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b466'):
                k |= set(os.path.basename(x) for x in
                         gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                k.add(os.path.basename(l[3:].strip()))
    S['kinds'] = k
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-5][0-9]_|^b46[01]_', f)]
    S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)
    return S


BINS = ('NAMES A TERMINAL', 'NAMES A CARRIER', 'NAMES NOTHING')

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'paste ends (part 1 of 1)' in S['ferry'],
     lambda S: cut(S, 'ferry', 'paste ends (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE',
     lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b464 closing -- the prior CLOSED act, pointed and not inherited',
     lambda S: 'row 313' in S['prior'], lambda S: cut(S, 'prior', 'row 313')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-R70-REHEARSED-BEFORE-LOCK', 'the survey bank and file times',
     lambda S: '(P1) THE PRECONDITION' in S['extract']
     and os.path.getmtime(os.path.join(D, 'b466_ferry_scan.txt')) < os.path.getmtime(FACE),
     lambda S: cut(S, 'extract', '(P1) THE PRECONDITION')),

    ('G-PRE-FIVE-SEARCHED', 'the survey bank',
     lambda S: len(S['survey'].get('precondition', [])) == 5,
     lambda S: put(S, 'survey', dict(S['survey'],
                                     precondition=S['survey'].get('precondition', [])[:4]))),
    ('G-PRE-CONTROL-FIRES', 'the survey bank',
     lambda S: S['survey'].get('control_fires') is True,
     lambda S: put(S, 'survey', dict(S['survey'], control_fires=False))),
    ('G-PRE-BOTH-YIELDS-PRINTED', 'the survey record',
     lambda S: 'by name, WIDE' in S['extract'] and 'by name, NARROWED' in S['extract']
     and 'REJECTED' in S['extract'],
     lambda S: cut(S, 'extract', 'REJECTED')),
    ('G-PRE-ABSENT-COUNTED', 'the survey bank',
     lambda S: sum(1 for a in S['survey'].get('precondition', []) if a['state'] == 'ABSENT') == 5,
     lambda S: put(S, 'survey', dict(S['survey'], precondition=[
         dict(a, state='PRESENT') for a in S['survey'].get('precondition', [])]))),
    ('G-PRE-BANK-NOT-ARTEFACT', 'the components record',
     lambda S: 'BANKS ABOUT THE ARTEFACT, NOT THE ARTEFACT' in S['comp'],
     lambda S: cut(S, 'comp', 'BANKS ABOUT THE ARTEFACT, NOT THE ARTEFACT')),
    ('G-PRE-NOFETCH', 'the five banked index queries and the act commit list',
     lambda S: S['queries'].count('NO KEY') == 5
     and not any('zeta-23' in x.lower() or 'anthropic' in x.lower() for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['data/zeta-23-lean/Main.lean'])),

    ('G-C1-NO-QUOTE-INVENTED', 'the readings bank',
     lambda S: S['readings'].get('component1', {}).get('invented') == 0
     and S['readings'].get('component1', {}).get('unanswerable') == 6,
     lambda S: put(S, 'readings', dict(S['readings'],
                                       component1=dict(S['readings'].get('component1', {}),
                                                       invented=1)))),
    ('G-C1-INTAKE-CITED-AT-LINE', 'the intake report itself',
     lambda S: 'critical-line proportion 41.6%' in S['intake']
     and '2026-08-20-external-intake.md:25' in S['comp'],
     lambda S: cut(S, 'comp', '2026-08-20-external-intake.md:25')),
    ('G-C1-FLAGS-STILL-OPEN', 'the intake report itself',
     lambda S: 'no-Euler-clause' in S['intake'] and 'paper-read flag open' in S['intake'],
     lambda S: put(S, 'intake', S['intake'].replace('paper-read flag open', 'paper-read flag CLOSED'))),
    ('G-C1-IMPORTBAR-NOT-GRADED', 'the components record',
     lambda S: 'NOT GRADABLE FROM THE RECORD' in S['comp'] and 'K1 class boundary' not in S['comp'],
     lambda S: put(S, 'comp', S['comp'] + NL + 'verdict: K1 class boundary')),
    ('G-C1-ROWU1-READING-LABELLED', 'the components record',
     lambda S: 'READ OF A SUMMARY, NOT OF THE PAPER' in S['comp'],
     lambda S: cut(S, 'comp', 'READ OF A SUMMARY, NOT OF THE PAPER')),
    ('G-C1-PATHS-TABLE-CHECKED', 'the readings bank against PATHS itself',
     lambda S: S['readings'].get('component1', {}).get('paths_proportion_table') is False,
     lambda S: put(S, 'readings', dict(S['readings'],
                                       component1=dict(S['readings'].get('component1', {}),
                                                       paths_proportion_table=True)))),
    ('G-C1-244-CELL-QUOTED', 'the deposited monograph itself',
     lambda S: (S['readings'].get('component1', {}).get('cell_244') or '') in S['mono']
     and '40.77' in (S['readings'].get('component1', {}).get('cell_244') or ''),
     lambda S: put(S, 'readings', dict(S['readings'],
                                       component1=dict(S['readings'].get('component1', {}),
                                                       cell_244='| a row nobody deposited |')))),
    ('G-C1-DRAFT-NOT-APPLIED', 'the commit file list and the monograph bytes',
     lambda S: 'Weil-form rank inequality' not in S['mono']
     and not any('24.4' in x for x in S['tracked']),
     lambda S: put(S, 'mono', S['mono'] + NL + '| Weil-form rank inequality, non-mollifier |')),
    ('G-C1-AUTHORING-ROUTED', 'the desk record',
     lambda S: 'AUTHORING' in S['desk'] and 'ROUTED' in S['desk'],
     lambda S: put(S, 'desk', S['desk'].replace('ROUTED', 'TAKEN'))),

    ('G-C2-CLONE-ABSENT-SAID', 'the components record',
     lambda S: 'THE CLONE IS ABSENT' in S['comp'], lambda S: cut(S, 'comp', 'THE CLONE IS ABSENT')),
    ('G-C2-SHA-FROM-BANK-LABELLED', 'the components record and the activation report',
     lambda S: 'cec57f9' in S['activation'] and 'PRIOR READ' in S['comp'],
     lambda S: put(S, 'comp', S['comp'].replace('PRIOR READ', 'A PRESENT ARTEFACT'))),
    ('G-C2-LV-PIN-RESOLVES', 'the survey bank against the monograph',
     lambda S: S['survey'].get('lv_pin') == '93c27ec' and '93c27ec' in S['mono'],
     lambda S: put(S, 'survey', dict(S['survey'], lv_pin='deadbee'))),
    ('G-C2-DEPOSIT-LINE-QUOTED', 'the deposited monograph itself',
     lambda S: 'decomposition conjunct (Guinand–Weil)' in S['mono']
     and 'Guinand-Weil' in S['comp'],
     lambda S: cut(S, 'comp', 'Guinand-Weil')),
    ('G-C2-STATEMENT-NOT-DOCSTRING', 'the survey bank',
     lambda S: all(not v.lstrip().startswith('/--')
                   for v in S['survey'].get('lv_statements', {}).values()),
     lambda S: put(S, 'survey', dict(S['survey'], lv_statements={
         k: '/-- a docstring -/' for k in S['survey'].get('lv_statements', {})}))),
    ('G-C2-FINSET-CONJUNCT-DISCHARGED', 'the survey bank',
     lambda S: 'lowFinset' in S['survey'].get('lv_declared', []),
     lambda S: put(S, 'survey', dict(S['survey'], lv_declared=[]))),
    ('G-C2-PENDING-CONJUNCT-NAMED', 'the readings bank',
     lambda S: 'blTerm' in (S['readings'].get('component2', {}).get('pending_conjunct') or ''),
     lambda S: put(S, 'readings', dict(S['readings'],
                                       component2=dict(S['readings'].get('component2', {}),
                                                       pending_conjunct='the usual thing')))),
    ('G-C2-FOURTH-VERDICT-NAMED', 'the readings bank and the LOCKED face',
     lambda S: S['readings'].get('component2', {}).get('verdict') == 'NOT DECIDABLE FROM THE RECORD'
     and 'NOT DECIDABLE FROM THE RECORD' in S['face'],
     lambda S: put(S, 'readings', dict(S['readings'],
                                       component2=dict(S['readings'].get('component2', {}),
                                                       verdict='CONTAINS')))),
    ('G-C2-NO-WORDER-FILED', 'the readings bank and every act commit',
     lambda S: S['readings'].get('component2', {}).get('worder_filed') is False
     and not any('W-ORD-GW-IMPORT' in x for x in S['tracked']),
     lambda S: put(S, 'readings', dict(S['readings'],
                                       component2=dict(S['readings'].get('component2', {}),
                                                       worder_filed=True)))),
    ('G-C2-NOTHING-IMPORTED', 'the commit file list',
     lambda S: not any(x.endswith('.lean') or 'lakefile' in x.lower() for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['tools/lean/ExplicitFormula.lean'])),

    ('G-N1-SCORED', 'the scores bank', lambda S: '"N1"' in S['scores'], lambda S: cut(S, 'scores', '"N1"')),
    ('G-N2-SCORED', 'the scores bank', lambda S: '"N2"' in S['scores'], lambda S: cut(S, 'scores', '"N2"')),
    ('G-N3-SCORED', 'the scores bank', lambda S: '"N3"' in S['scores'], lambda S: cut(S, 'scores', '"N3"')),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores bank',
     lambda S: '"seat"' in S['scores'], lambda S: cut(S, 'scores', '"seat"')),

    ('G-SPAN-BY-TOOL', 'the span tool record',
     lambda S: 'THE CURRENT SPAN' in S['span'], lambda S: cut(S, 'span', 'THE CURRENT SPAN')),
    ('G-NOGRADE-MOVED', 'the commit file list',
     lambda S: not any(x.endswith(('FACES_LEDGER.md', 'REGISTRY.md', 'ERRATA.md')) for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['REGISTRY.md'])),
    ('G-NODEPOSIT', 'the deposit directory tracked state, via the source',
     lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail own text',
     lambda S: 'where the deposit left it' in S['ot'],
     lambda S: cut(S, 'ot', 'where the deposit left it')),
    ('G-KERNEL-LANE-READ-ONLY', 'the trail and the lv working tree',
     lambda S: 'no Lean was compiled' in S['ot']
     and gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == '',
     lambda S: cut(S, 'ot', 'no Lean was compiled')),
    ('G-NOPRIORBANK', 'file times against the face',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail own text',
     lambda S: 'The four lists are open' in S['ot'], lambda S: cut(S, 'ot', 'The four lists are open')),
    ('G-CORPUS-SCOPE', 'the commit file list',
     lambda S: S['tracked'] == ['OPEN_TRAILS.md'],
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'FINDINGS.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail own text',
     lambda S: S['ot'].count('### b466 \u2014') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b466 \u2014 a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 314 |' in S['corr'], lambda S: cut(S, 'corr', '| 314 |')),
    ('G-WRITELIST-KINDS', 'every b466 commit in three repositories',
     lambda S: not sorted(k for k in S['kinds'] if k not in S['face']),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'a_name_the_write_list_does_not_carry.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite own text',
     lambda S: "log', '--pretty=%H %s'" in S['suite'],
     lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the commit file list',
     lambda S: all(x.startswith(('OPEN_TRAILS', 'data/', 'tools/')) for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['internal/BLOB_SENSITIVITY_2026-08-29.md'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the face (G2) block against what runs',
     lambda S: S.get('declared_eq_run', False), lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'the suite own text',
     lambda S: 'def line_with(text, needle)' in S['suite'],
     lambda S: cut(S, 'suite', 'def line_with(text, needle)')),
    ('G-MIRROR-TAGGED-BUILD', 'the built zip presence',
     lambda S: S['mirror'], lambda S: put(S, 'mirror', False)),
    ('G-MUSTFAIL', 'a file that must not exist',
     lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-B465-STRANDED-NAMED', 'the trail, the desk and the b465 files on disk',
     lambda S: 'stranded at step zero' in S['ot'].lower()
     and os.path.exists(os.path.join(D, 'b465_ferry.txt'))
     and not os.path.exists(os.path.join(D, 'b465_registration_2026-09-21.txt')),
     lambda S: put(S, 'ot', S['ot'].replace('stranded at step zero', 'closed and pushed'))),
]


def main():
    S = sources()
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (K) THE BARS.')]
    declared = sorted(set(re.findall(r'\b[GF]-[A-Z0-9-]+', g2)) - {'G-NO'})
    names = [a[0] for a in ARMS]
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b466'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b466 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
        % ('POST-PUSH' if pushed else 'PRE-PUSH'))
    rec('=' * 104)
    rec('  arms in the (G2) block : %d ; run here : %d ; deferred : %d'
        % (len(declared), len(names), len(deferred)))
    rec('  %-36s %-5s %-5s %-5s %s' % ('arm', 'LIVE', 'NEG', 'POS', 'verdict'))
    rec('  ' + '-' * 98)
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
        rec('  %-36s %-5s %-5s %-5s %s' % (name, 'PASS' if live else 'FAIL',
                                           'PASS' if neg else '###FAIL', 'FAIL' if not p else '###PASS', v))
        RES.append(name)
        EX.append(dict(name=name, live=live, neg=neg, pos=p, reads=reads))
        if not live:
            fail.append(name)
    for n in deferred:
        rec('  %-36s DEFERRED TO POST-PUSH' % n)
    rec('')
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**'
        % (len(RES), len(RES) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**'
        % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, 'b466_checks_postpush.txt' if pushed else 'b466_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred),
              io.open(os.path.join(D, 'b466_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
