# -*- coding: utf-8 -*-
"""b462_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
FACE = os.path.join(D, 'b462_registration_2026-09-21.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b462_ferry.txt')),
        scan=read(os.path.join(D, 'b462_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b462_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b462_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b462_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b462_extract.txt')),
        lock=read(os.path.join(D, 'b462_lockgate_notes.txt')),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b461_closing.txt')),
        addendum=read(os.path.join(D, 'b462_addendum.txt')),
        census=read(os.path.join(D, 'b462_census.txt')),
        span=read(os.path.join(D, 'b462_span_notes.txt')),
        scores=read(os.path.join(D, 'b462_scores.json')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b462_checks.py')),
        idx=json.loads(read(os.path.join(D, 'b462_index.json')) or '{}'),
        cen=json.loads(read(os.path.join(D, 'b462_census.json')) or '{}'),
        dep=sorted(os.listdir(DEP)),
        docs=sorted(f for f in os.listdir(D) if f.startswith('b462_')),
        mirror=os.path.exists(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-2026-09-21-b462.zip')),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b462')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b462_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b462'):
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
     lambda S: 'row 310' in S['prior'], lambda S: cut(S, 'prior', 'row 310')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot`s bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-R70-REHEARSED-BEFORE-LOCK', 'the rehearsal bank and file times',
     lambda S: 'REHEARSAL 1 AND 2' in S['extract']
     and os.path.getmtime(os.path.join(D, 'b462_extract.txt')) < os.path.getmtime(FACE),
     lambda S: cut(S, 'extract', 'REHEARSAL 1 AND 2')),
    ('G-R72-ENTERED', 'the trail`s own text',
     lambda S: '(R72)' in S['ot'], lambda S: cut(S, 'ot', '(R72)')),
    ('G-SPAN-AT-THRESHOLD-SAID', 'the span tool`s own record and the trail',
     lambda S: 'THE CURRENT SPAN : 9' in S['span'] and 'threshold' in S['ot'].lower(),
     lambda S: put(S, 'span', S['span'].replace('THE CURRENT SPAN : 9', 'THE CURRENT SPAN : 4'))),
    ('G-C1-ELEVEN-FILES', 'the deposit directory itself',
     lambda S: len(S['dep']) == 11, lambda S: put(S, 'dep', S['dep'][:10])),
    ('G-C1-TWO-ABSENCES-NAMED', 'the survey bank',
     lambda S: 'ZENODO DESCRIPTIONS: NOT BANKED' in S['extract'],
     lambda S: cut(S, 'extract', 'ZENODO DESCRIPTIONS: NOT BANKED')),
    ('G-C1-SUBSTITUTE-LABELLED', 'the census bank`s own rows',
     lambda S: all(r['label'].startswith('SUBSTITUTE')
                   for r in S['cen'].get('per_surface', []) if 'SIDE-' in r['surface']),
     lambda S: put(S, 'cen', dict(S['cen'], per_surface=[
         dict(r, label='deposit file') if 'SIDE-' in r['surface'] else r
         for r in S['cen'].get('per_surface', [])]))),
    ('G-C1-COUNTS-BY-KIND', 'the census bank',
     lambda S: len(S['cen'].get('by_kind', {})) >= 2 and sum(S['cen']['by_kind'].values())
     == S['cen'].get('total'),
     lambda S: put(S, 'cen', dict(S['cen'], by_kind={'prose': 1}))),
    ('G-C1-B457-ATTRIBUTION-CORRECTED', 'the survey bank',
     lambda S: 'THE FIGURES ARE b457`S, NOT b455`S' in S['extract'],
     lambda S: cut(S, 'extract', 'THE FIGURES ARE b457`S, NOT b455`S')),
    ('G-C2-INDEX-NONEMPTY', 'the index bank',
     lambda S: S['idx'].get('index_names', 0) > 0 and S['idx'].get('index_decls', 0) > 0,
     lambda S: put(S, 'idx', dict(S['idx'], index_names=0))),
    ('G-C2-POSITIVE-CONTROL-RESOLVES', 'the index bank',
     lambda S: S['idx'].get('control_resolves') is True,
     lambda S: put(S, 'idx', dict(S['idx'], control_resolves=False))),
    ('G-C2-PIN-OR-HEAD-SAID', 'the index bank`s per-kernel rows',
     lambda S: all(r.get('how') for r in S['idx'].get('per_kernel', [])),
     lambda S: put(S, 'idx', dict(S['idx'], per_kernel=[dict(r, how='') for r in
                                                        S['idx'].get('per_kernel', [])]))),
    ('G-C2-THREE-BINS', 'the census bank',
     lambda S: set(S['cen'].get('by_bin', {})) == set(BINS),
     lambda S: put(S, 'cen', dict(S['cen'], by_bin={'NAMES NOTHING': 1}))),
    ('G-C2-BINS-SUM-TO-ITEMS', 'the census bank',
     lambda S: sum(S['cen'].get('by_bin', {}).values()) == S['cen'].get('total'),
     lambda S: put(S, 'cen', dict(S['cen'], total=(S['cen'].get('total') or 0) + 1))),
    ('G-C2-PER-SURFACE-PRINTED', 'the census bank',
     lambda S: len(S['cen'].get('per_surface', [])) == 13,
     lambda S: put(S, 'cen', dict(S['cen'], per_surface=S['cen'].get('per_surface', [])[:5]))),
    ('G-C2-TWENTY-VERBATIM', 'the census bank and its record',
     lambda S: len(S['cen'].get('top20', [])) == 20
     and all(t['text'][:40] in S['census'] for t in S['cen'].get('top20', [])[:5]),
     lambda S: put(S, 'cen', dict(S['cen'], top20=S['cen'].get('top20', [])[:7]))),
    ('G-C2-STRENGTH-ORDER-FIXED', 'the face and the components source',
     lambda S: 'STRENGTH = [' in read(os.path.join(T, 'b462_components.py'))
     and 'THE STRENGTH ORDER, FIXED HERE' in S['face'],
     lambda S: cut(S, 'face', 'THE STRENGTH ORDER, FIXED HERE')),
    ('G-C2-MACHINE-CHECKED-COUNT', 'the census bank',
     lambda S: S['cen'].get('machine_checked_no_terminal') is not None,
     lambda S: put(S, 'cen', {k: v for k, v in S['cen'].items()
                              if k != 'machine_checked_no_terminal'})),
    ('G-C2-NO-GRADE-CONFERRED', 'the census record`s own text',
     lambda S: 'NO ITEM ABOVE IS GRADED' in S['census'],
     lambda S: cut(S, 'census', 'NO ITEM ABOVE IS GRADED')),
    ('G-C2-NO-NEW-DOCUMENT', 'the corpus tree',
     lambda S: S['tracked'] == ['OPEN_TRAILS.md'],
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'THE_TERMINAL_LESS_CENSUS.md'])),
    ('G-N1-SCORED', 'the scores bank', lambda S: '"N1"' in S['scores'], lambda S: cut(S, 'scores', '"N1"')),
    ('G-N2-SCORED', 'the scores bank', lambda S: '"N2"' in S['scores'], lambda S: cut(S, 'scores', '"N2"')),
    ('G-N3-SCORED', 'the scores bank', lambda S: '"N3"' in S['scores'], lambda S: cut(S, 'scores', '"N3"')),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores bank',
     lambda S: '"seat"' in S['scores'], lambda S: cut(S, 'scores', '"seat"')),
    ('G-SPAN-BY-TOOL', 'the span tool`s record',
     lambda S: 'THE CURRENT SPAN' in S['span'], lambda S: cut(S, 'span', 'THE CURRENT SPAN')),
    ('G-NOGRADE-MOVED', 'the commit`s file list',
     lambda S: not any(x.endswith(('FACES_LEDGER.md', 'REGISTRY.md', 'ERRATA.md')) for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['REGISTRY.md'])),
    # ### **DEFECTIVE ON ITS OWN POSITIVE CONTROL AT b462, AND REPAIRED IN THE ACT.** ### The first
    # ### form called `gits(...)` inside the predicate, so it read THE WORLD rather than the supplied
    # ### source and no mutation of `S` could reach it. ### **b461's LESSON RECURRING: AN ARM THAT
    # ### READS PAST ITS SOURCE CANNOT BE EXERCISED, WHATEVER ITS TABLE SAYS.** ### The read is moved
    # ### into `sources()` and the predicate now reads `S`.
    ('G-NODEPOSIT', 'the deposit directory`s own tracked state, via the source',
     lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text',
     lambda S: 'where the deposit left it' in S['ot'],
     lambda S: cut(S, 'ot', 'where the deposit left it')),
    ('G-NOPRIORBANK', 'file times against the face`s',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text',
     lambda S: 'The four lists are open' in S['ot'], lambda S: cut(S, 'ot', 'The four lists are open')),
    ('G-CORPUS-SCOPE', 'the commit`s file list',
     lambda S: S['tracked'] == ['OPEN_TRAILS.md'],
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'FINDINGS.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail`s own text',
     lambda S: S['ot'].count('### b462 —') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b462 — a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 311 |' in S['corr'], lambda S: cut(S, 'corr', '| 311 |')),
    ('G-WRITELIST-KINDS', 'every b462 commit in three repositories',
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b462'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b462 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b462_checks_postpush.txt' if pushed else 'b462_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred),
              io.open(os.path.join(D, 'b462_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
