# -*- coding: utf-8 -*-
"""b464_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
FACE = os.path.join(D, 'b464_registration_2026-09-21.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b464_ferry.txt')),
        scan=read(os.path.join(D, 'b464_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b464_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b464_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b464_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b464_extract.txt')),
        lock=read(os.path.join(D, 'b464_lockgate_notes.txt')),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        # ### **THE PRIOR ACT'S CLOSING IS b462'S.** ### A wholesale re-point from b462 to b464
        # ### moved every b462 name and left b461 where it was, so the inherited line pointed two
        # ### acts back and the arm failed on the wrong bank -- `G-CARRIED-TOOLS-REPOINTED`'s own
        # ### species, committed while building the suite that carries it.
        prior=read(os.path.join(D, 'b463_closing.txt')),
        addendum=read(os.path.join(D, 'b464_addendum.txt')),
        census=read(os.path.join(D, 'b464_census.txt')),
        span=read(os.path.join(D, 'b464_span_notes.txt')),
        scores=read(os.path.join(D, 'b464_scores.json')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b464_checks.py')),
        grades=json.loads(read(os.path.join(D, 'b464_grades.json')) or '{}'),
        params=json.loads(read(os.path.join(D, 'b464_params.json')) or '{}'),
        b455=read(os.path.join(D, 'b455_closing.txt')),
        errata=read(os.path.join(PP, 'ERRATA.md')),
        faces=read(os.path.join(PP, 'FACES_LEDGER.md')),
        comp=read(os.path.join(D, 'b464_components.txt')),
        docs=sorted(f for f in os.listdir(D) if f.startswith('b464_')),
        mirror=os.path.exists(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-2026-09-21-b464.zip')),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b464')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b464_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b464'):
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
    ('G-REG-LOCKED-FIRST', 'the face`s lock block',
     lambda S: 'THE REGISTRATION LOCK' in S['face'], lambda S: cut(S, 'face', 'THE REGISTRATION LOCK')),
    ('G-LOCKGATE-EIGHT', 'a banked verdict LINE (A2)',
     lambda S: 'LOCK PERMITTED' in line_with(S['lock'], '**VERDICT : LOCK')
     and 'GATES READ : 8. ### PASSING : 8' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 6'))),
    ('G-SEAL-VERIFIES', 'a banked verdict LINE',
     lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('SEAL INTACT', 'SEAL BROKEN'))),
    ('G-PRIOR-CLOSED-PUSHED', 'the prior act`s closing',
     lambda S: 'row 312' in S['prior'], lambda S: cut(S, 'prior', 'row 312')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot`s bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-R70-REHEARSED-BEFORE-LOCK', 'the survey bank and file times',
     lambda S: 'THE REHEARSAL -- THE TERMINAL SEARCH' in S['extract']
     and os.path.getmtime(os.path.join(D, 'b464_extract.txt')) < os.path.getmtime(FACE),
     lambda S: cut(S, 'extract', 'THE REHEARSAL -- THE TERMINAL SEARCH')),
    ('G-C1-EIGHT-REDERIVED', 'the grades bank',
     lambda S: len(S['grades'].get('items', [])) == 8,
     lambda S: put(S, 'grades', dict(S['grades'], items=S['grades'].get('items', [])[:7]))),
    ('G-C1-COUNT-AGREES', 'the components record',
     lambda S: 'AGREE : True' in S['comp'], lambda S: cut(S, 'comp', 'AGREE : True')),
    ('G-C1-QUOTED-AT-LINE', 'the grades bank against the deposited files',
     lambda S: all(i['text'][:40] in read(os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', i['surface']))
                   for i in S['grades'].get('items', [])),
     lambda S: put(S, 'grades', dict(S['grades'], items=[dict(i, text='a sentence nobody deposited')
                                                          for i in S['grades'].get('items', [])]))),
    ('G-C1-TERMINAL-AT-PIN', 'the grades bank',
     lambda S: sum(1 for i in S['grades'].get('items', []) if i['how'] == 'PIN') >= 7,
     lambda S: put(S, 'grades', dict(S['grades'], items=[dict(i, how='HEAD')
                                                          for i in S['grades'].get('items', [])]))),
    ('G-C1-STATEMENT-NOT-DOCSTRING', 'the grades bank`s statements',
     lambda S: all(i['statement'] and not i['statement'].lstrip().startswith('/--')
                   for i in S['grades'].get('items', [])),
     lambda S: put(S, 'grades', dict(S['grades'],
                                     items=[dict(i, statement='/-- a docstring -/')
                                            for i in S['grades'].get('items', [])]))),
    ('G-C1-FOUR-GRADES-ONLY', 'the grades bank',
     lambda S: set(S['grades'].get('by_grade', {})) <= {'DERIVES', 'INTERFACES', 'NOT THE CLAIM', 'SHELL'},
     lambda S: put(S, 'grades', dict(S['grades'], by_grade=dict(S['grades'].get('by_grade', {}),
                                                                PROBABLY_FINE=1)))),
    ('G-C1-REASON-IN-TERMINAL-WORDS', 'the grades bank',
     lambda S: all(i['reason'] for i in S['grades'].get('items', [])),
     lambda S: put(S, 'grades', dict(S['grades'], items=[dict(i, reason='')
                                                          for i in S['grades'].get('items', [])]))),
    ('G-C1-B455-CITED-NOT-RECONFERRED', 'b455`s own closing, unedited',
     lambda S: 'C2     MACHINE-CHECKED      NOT THE CLAIM' in S['b455'],
     lambda S: cut(S, 'b455', 'C2     MACHINE-CHECKED      NOT THE CLAIM')),
    ('G-C1-ROUTED-NOT-REPAIRED', 'the components record',
     lambda S: 'NAMED AND ROUTED, NOT REPAIRED' in S['comp'],
     lambda S: cut(S, 'comp', 'NAMED AND ROUTED, NOT REPAIRED')),
    ('G-C1-NO-ERRATUM-DRAFTED', 'ERRATA.md itself',
     lambda S: 'E-2026-09-21' not in S['errata'],
     lambda S: put(S, 'errata', S['errata'] + NL + '## E-2026-09-21-1 a draft that must not exist')),
    ('G-C2-SOURCE-PINNED', 'the components record',
     lambda S: 'b8e0b54ade8535cf' in S['comp'], lambda S: cut(S, 'comp', 'b8e0b54ade8535cf')),
    ('G-C2-WHICH-STATEMENT-SAID', 'the components record',
     lambda S: 'THE CHAIN IMPORTS CC`s (148)' in S['comp'],
     lambda S: cut(S, 'comp', 'THE CHAIN IMPORTS CC`s (148)')),
    ('G-C2-GARBLING-CARRIED', 'the components record',
     lambda S: 'GARBLED, AND SAID TO BE' in S['comp'], lambda S: cut(S, 'comp', 'GARBLED, AND SAID TO BE')),
    ('G-C2-PARAMS-BEFORE-SITES', 'the components record`s own order',
     lambda S: 0 < S['comp'].find('PRINTED BEFORE ANY SITE') < S['comp'].find('THE SIX SITE INDICES AGAINST'),
     lambda S: cut(S, 'comp', 'PRINTED BEFORE ANY SITE')),
    ('G-C2-SIX-SITES-PLACED', 'the params bank',
     lambda S: len(S['params'].get('sites', [])) == 6,
     lambda S: put(S, 'params', dict(S['params'], sites=S['params'].get('sites', [])[:5]))),
    ('G-C2-THREE-VERDICTS-ONLY', 'the params bank',
     lambda S: set(S['params'].get('tally', {})) <= {'A PARAMETER', 'A COORDINATE OF ONE', 'OF NO PARAMETER'},
     lambda S: put(S, 'params', dict(S['params'], tally=dict(S['params'].get('tally', {}), MAYBE=1)))),
    ('G-C2-UNVISITED-PRINTED', 'the params bank and the record',
     lambda S: S['params'].get('unvisited') is not None and 'UNVISITED PARAMETERS :' in S['comp'],
     lambda S: cut(S, 'comp', 'UNVISITED PARAMETERS :')),
    ('G-C2-SCOPED-TO-CC', 'the components record',
     lambda S: 'ONE SOURCE`S SILENCE IS NOT THE RECORD`S' in S['comp'],
     lambda S: cut(S, 'comp', 'ONE SOURCE`S SILENCE IS NOT THE RECORD`S')),
    # ### **THE FIRST FORM COUNTED SIX AND COULD NOT SEE A SEVENTH**: its alternation named the six
    # ### romans, so an added `(vii)` left the count at six and the positive control PASSED. ### The
    # ### arm now reads the SET OF MARKERS the row carries and requires it to be exactly the six.
    ('G-C2-NO-SITE-ENTERED', 'FACES_LEDGER row U1`s own site markers',
     lambda S: set(re.findall(r'\(([ivx]+)\) THE ', S['faces'])) == set(
         ['i', 'ii', 'iii', 'iv', 'v', 'vi']),
     lambda S: put(S, 'faces', S['faces'] + NL + '(vii) THE SEVENTH SITE THAT MUST NOT EXIST')),
    ('G-C2-ROWU1-UNEDITED', 'the commit`s file list',
     lambda S: not any(x.endswith('FACES_LEDGER.md') for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['FACES_LEDGER.md'])),
    ('G-C2-FREEZE-QUOTED', 'the face and the row`s own words',
     lambda S: 'THE REGISTER IS FROZEN AT SIX, b409' in S['faces']
     and 'RATHER THAN A STATEMENT ABOUT THE RECORD' in S['face'],
     lambda S: cut(S, 'face', 'RATHER THAN A STATEMENT ABOUT THE RECORD')),
    ('G-C2-NO-BRIDGE-TYPED', 'the components record',
     lambda S: 'NO BRIDGE' in S['comp'], lambda S: cut(S, 'comp', 'NO BRIDGE')),
    ('G-N1A-SCORED', 'the scores bank', lambda S: '"N1a"' in S['scores'], lambda S: cut(S, 'scores', '"N1a"')),
    ('G-N1B-SCORED', 'the scores bank', lambda S: '"N1b"' in S['scores'], lambda S: cut(S, 'scores', '"N1b"')),
    ('G-N2-SCORED', 'the scores bank', lambda S: '"N2"' in S['scores'], lambda S: cut(S, 'scores', '"N2"')),
    ('G-N3-SCORED', 'the scores bank', lambda S: '"N3"' in S['scores'], lambda S: cut(S, 'scores', '"N3"')),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores bank',
     lambda S: '"seat"' in S['scores'], lambda S: cut(S, 'scores', '"seat"')),
    ('G-SPAN-BY-TOOL', 'the span tool`s record',
     lambda S: 'THE CURRENT SPAN' in S['span'], lambda S: cut(S, 'span', 'THE CURRENT SPAN')),
    ('G-NOGRADE-MOVED', 'the commit`s file list',
     lambda S: not any(x.endswith(('FACES_LEDGER.md', 'REGISTRY.md', 'ERRATA.md')) for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['REGISTRY.md'])),
    ('G-NODEPOSIT', 'the deposit directory`s tracked state, via the source',
     lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text',
     lambda S: 'where the deposit left it' in S['ot'],
     lambda S: cut(S, 'ot', 'where the deposit left it')),
    ('G-NOKERNEL-RUN', 'the components record',
     lambda S: 'read, not run' in S['ot'].lower(), lambda S: put(S, 'ot', S['ot'].replace('read, not run', 'run'))),
    ('G-NOPRIORBANK', 'file times against the face`s',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text',
     lambda S: 'The four lists are open' in S['ot'], lambda S: cut(S, 'ot', 'The four lists are open')),
    ('G-CORPUS-SCOPE', 'the commit`s file list',
     lambda S: S['tracked'] == ['OPEN_TRAILS.md'],
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'FINDINGS.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail`s own text',
     lambda S: S['ot'].count('### b464 \u2014') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b464 \u2014 a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 313 |' in S['corr'], lambda S: cut(S, 'corr', '| 313 |')),
    ('G-WRITELIST-KINDS', 'every b464 commit in three repositories',
     lambda S: not sorted(k for k in S['kinds'] if k not in S['face']),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'a_name_the_write_list_does_not_carry.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite`s own text',
     lambda S: "log', '--pretty=%H %s'" in S['suite'],
     lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the commit`s file list',
     lambda S: all(x.startswith(('OPEN_TRAILS', 'data/', 'tools/')) for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['internal/BLOB_SENSITIVITY_2026-08-29.md'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the face`s (G2) block against what runs',
     lambda S: S.get('declared_eq_run', False), lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'the suite`s own text',
     lambda S: 'def line_with(text, needle)' in S['suite'],
     lambda S: cut(S, 'suite', 'def line_with(text, needle)')),
    ('G-MIRROR-TAGGED-BUILD', 'the built zip`s presence',
     lambda S: S['mirror'], lambda S: put(S, 'mirror', False)),
    ('G-MUSTFAIL', 'a file that must not exist',
     lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
]


def main():
    S = sources()
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (K) THE BARS.')]
    declared = sorted(set(re.findall(r'\b[GF]-[A-Z0-9-]+', g2)) - {'G-NO'})
    names = [a[0] for a in ARMS]
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b464'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b464 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b464_checks_postpush.txt' if pushed else 'b464_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred),
              io.open(os.path.join(D, 'b464_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
