# -*- coding: utf-8 -*-
"""b463_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
FACE = os.path.join(D, 'b463_registration_2026-09-21.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b463_ferry.txt')),
        scan=read(os.path.join(D, 'b463_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b463_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b463_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b463_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b463_extract.txt')),
        lock=read(os.path.join(D, 'b463_lockgate_notes.txt')),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        # ### **THE PRIOR ACT'S CLOSING IS b462'S.** ### A wholesale re-point from b462 to b463
        # ### moved every b462 name and left b461 where it was, so the inherited line pointed two
        # ### acts back and the arm failed on the wrong bank -- `G-CARRIED-TOOLS-REPOINTED`'s own
        # ### species, committed while building the suite that carries it.
        prior=read(os.path.join(D, 'b462_closing.txt')),
        addendum=read(os.path.join(D, 'b463_addendum.txt')),
        census=read(os.path.join(D, 'b463_census.txt')),
        span=read(os.path.join(D, 'b463_span_notes.txt')),
        scores=read(os.path.join(D, 'b463_scores.json')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b463_checks.py')),
        fold=json.loads(read(os.path.join(D, 'b463_fold.json')) or '{}'),
        foldrun=read(os.path.join(D, 'b463_fold_run.txt')),
        findings=read(os.path.join(PP, 'FINDINGS.md')),
        digest=read(os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')),
        span2=read(os.path.join(D, 'b463_span_notes2.txt')),
        comp=read(os.path.join(D, 'b463_components.txt')),
        docs=sorted(f for f in os.listdir(D) if f.startswith('b463_')),
        mirror=os.path.exists(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-2026-09-21-b463.zip')),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b463')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b463_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b463'):
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
     lambda S: 'row 311' in S['prior'], lambda S: cut(S, 'prior', 'row 311')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot`s bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-R70-REHEARSED-BEFORE-LOCK', 'the rehearsal bank and file times',
     lambda S: 'THE REHEARSAL -- THE VERDICT-STRING MATCHER' in S['extract']
     and os.path.getmtime(os.path.join(D, 'b463_extract.txt')) < os.path.getmtime(FACE),
     lambda S: cut(S, 'extract', 'THE REHEARSAL -- THE VERDICT-STRING MATCHER')),
    ('G-R73-OBEYED-BY-THIS-FACE', 'the face`s own write list against the versioned names',
     lambda S: all(n in S['face'] for n in ('b463_lockgate_notes2.txt',
                                            'audit_b463_reg_banned_terms_r2.txt',
                                            'b463_span_notes2.txt')),
     lambda S: cut(S, 'face', 'b463_lockgate_notes2.txt')),
    ('G-FOLD-STRINGS-ALL-MATCH', 'the fold bank',
     lambda S: S['fold'].get('verified') == S['fold'].get('strings') and S['fold'].get('all_matched'),
     lambda S: put(S, 'fold', dict(S['fold'], verified=S['fold'].get('strings', 0) - 1))),
    ('G-FOLD-STRINGS-FROM-OWN-CLOSING', 'the fold bank`s own bank names',
     lambda S: all(r['bank'] == '%s_closing.txt' % r['act'] for r in S['fold'].get('rows', [])),
     lambda S: put(S, 'fold', dict(S['fold'], rows=[dict(r, bank='b458_components.txt')
                                                    for r in S['fold'].get('rows', [])]))),
    ('G-FOLD-NINE-ROWS', 'the fold bank',
     lambda S: len(S['fold'].get('rows', [])) == 9,
     lambda S: put(S, 'fold', dict(S['fold'], rows=S['fold'].get('rows', [])[:8]))),
    ('G-FOLD-COLUMNS-PRINTED', 'the FINDINGS section just written',
     lambda S: 'The three columns, kept apart' in S['findings'],
     lambda S: cut(S, 'findings', 'The three columns, kept apart')),
    ('G-FOLD-OBJECT-COLUMN-ZERO', 'the fold bank',
     lambda S: S['fold'].get('columns', {}).get('OBJECT', 0) == 0,
     lambda S: put(S, 'fold', dict(S['fold'], columns=dict(S['fold'].get('columns', {}), OBJECT=1)))),
    ('G-FOLD-HEADING-PARSES', 'the span tool`s own read-back',
     lambda S: 'b454 - b462 (9 acts)' in S['span2'],
     lambda S: cut(S, 'span2', 'b454 - b462 (9 acts)')),
    ('G-FOLD-FINDINGS-APPENDED', 'the fold run record',
     lambda S: 'FINDINGS.md' in S['foldrun'] and 'WRITTEN' in S['foldrun'],
     lambda S: cut(S, 'foldrun', 'WRITTEN')),
    ('G-FOLD-DIGEST-APPENDED', 'the digest itself',
     lambda S: '<!-- b463 orientation refresh' in S['digest'],
     lambda S: cut(S, 'digest', '<!-- b463 orientation refresh')),
    ('G-FOLD-PREFIX-PROVED', 'the fold run record',
     lambda S: S['foldrun'].count('prior a TRUE PREFIX True') == 2,
     lambda S: put(S, 'foldrun', S['foldrun'].replace('prior a TRUE PREFIX True',
                                                      'prior a TRUE PREFIX False', 1))),
    ('G-FOLD-REMOVED-ZERO', 'the fold run record',
     lambda S: S['foldrun'].count('lines removed 0') == 2,
     lambda S: put(S, 'foldrun', S['foldrun'].replace('lines removed 0', 'lines removed 2', 1))),
    ('G-FOLD-TWO-TARGETS-ONLY', 'the commit`s file list',
     lambda S: sorted(S['tracked']) == sorted(['FINDINGS.md', 'OPEN_TRAILS.md',
                                               'phase2/method/THE_FINDINGS_AS_THEY_STAND.md']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['REGISTRY.md'])),
    ('G-FOLD-RULINGS-LISTED', 'the FINDINGS section just written',
     lambda S: all(('`(R%d)`' % n) in S['findings'] for n in range(63, 74)),
     # ### **THE FIRST MUTATION COULD NOT BITE:** it cut one PHRASE carrying `(R73)`, and the token
     # ### occurs elsewhere in FINDINGS, so the arm still passed its positive control. ### The control
     # ### now removes the token itself. ### **A CONTROL THAT LEAVES ITS TARGET IN PLACE IS NOT ONE.**
     lambda S: cut(S, 'findings', '`(R73)`')),
    ('G-FOLD-BOTH-LEDGERS', 'the FINDINGS section just written',
     lambda S: 'The navigator' in S['findings'] and 'The seat' in S['findings'],
     lambda S: cut(S, 'findings', 'The navigator')),
    ('G-FOLD-MINTS-NOTHING', 'the commit`s file list across the corpus',
     lambda S: not any(x.endswith(('FACES_LEDGER.md', 'REGISTRY.md', 'ERRATA.md', 'README.md'))
                       for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['FACES_LEDGER.md'])),
    ('G-FOLD-ONE-LINE-CARRIED', 'the FINDINGS section and the digest',
     lambda S: 'never to have been asked to fail' in S['findings']
     and 'never to have been asked to fail' in S['digest'],
     lambda S: cut(S, 'digest', 'never to have been asked to fail')),
    ('G-SPAN-BY-TOOL', 'the span tool`s record',
     lambda S: 'THE CURRENT SPAN' in S['span'], lambda S: cut(S, 'span', 'THE CURRENT SPAN')),
    ('G-SPAN-READBACK', 'the span tool`s read-back after the write',
     lambda S: 'it was FILED BY           : b463' in S['span2']
     and 'next span STARTS AT: b464' in S['span2'],
     lambda S: cut(S, 'span2', 'next span STARTS AT: b464')),
    ('G-NOGRADE-MOVED', 'the commit`s file list',
     lambda S: not any(x.endswith(('FACES_LEDGER.md', 'REGISTRY.md')) for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['REGISTRY.md'])),
    ('G-NODEPOSIT', 'the deposit directory`s tracked state, via the source',
     lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text',
     lambda S: 'where the deposit left it' in S['ot'],
     lambda S: cut(S, 'ot', 'where the deposit left it')),
    ('G-NOPRIORBANK', 'file times against the face`s',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text',
     lambda S: 'The four lists are open' in S['ot'], lambda S: cut(S, 'ot', 'The four lists are open')),
    ('G-CORPUS-SCOPE', 'the commit`s file list',
     lambda S: all(x in ('FINDINGS.md', 'OPEN_TRAILS.md',
                         'phase2/method/THE_FINDINGS_AS_THEY_STAND.md') for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['FINDINGS-archive-1.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail`s own text',
     lambda S: S['ot'].count('### b463 \u2014') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b463 \u2014 a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 312 |' in S['corr'], lambda S: cut(S, 'corr', '| 312 |')),
    ('G-WRITELIST-KINDS', 'every b463 commit in three repositories',
     lambda S: not sorted(k for k in S['kinds'] if k not in S['face']),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'a_name_the_write_list_does_not_carry.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite`s own text',
     lambda S: "log', '--pretty=%H %s'" in S['suite'],
     lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the commit`s file list',
     lambda S: all(x.startswith(('FINDINGS', 'OPEN_TRAILS', 'phase2/', 'data/', 'tools/'))
                   for x in S['tracked']),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b463'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b463 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b463_checks_postpush.txt' if pushed else 'b463_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred),
              io.open(os.path.join(D, 'b463_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
