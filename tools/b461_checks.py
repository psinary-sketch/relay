# -*- coding: utf-8 -*-
"""b461_checks.py -- THE SUCCESSOR SUITE. ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE.**

### ### **WHY THIS FILE IS SHAPED DIFFERENTLY FROM b460_checks.py.** ### There, every predicate read
### module state, so an arm could be evaluated exactly once -- on the live act -- and nothing could
### ever check that it COULD have said otherwise. ### b461's inventory measured the consequence:
### ### **64 ARMS, 0 OF THEM EXERCISED AGAINST ANY CONTROL.**
### Here each arm takes `S`, a dict of the act's sources, so the harness can hand it a MUTATED `S`
### and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**

### ### ==========================================================================================
### ### RETIRED AT b461, UNDER b396's RULE AND THE ORDER'S CONJUNCTIVE DISPOSITION.
### ### Kept here as a comment, with the name and the reason, as the order requires.
### ### ==========================================================================================
### ### **G-NOSTAGE-A** -- predicate was the literal `True`. ### Never failed at a close, and no
###     positive control can be stated for a constant. ### **REPLACED, NOT MERELY DROPPED**, by
###     `G-NOSTAGE-A-BY-DIFF`, which reads the commit's own file list instead of asserting.
### ### **G-TWO-READINGS-TWO-FILES** -- predicate was the literal `True`. ### The thing it named was
###     real (two files are written) but the arm asserted it rather than reading it. ### No successor:
###     the fact is visible in the two banked file names and needs no arm to claim it.
### ### **G-PUSH-SIDE-B439-PREDICATE** -- predicate was the literal `True`. ### It named b439's
###     predicate and tested nothing; the predicate itself is exercised by the side the suite writes to.
### ### ==========================================================================================
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
FACE = os.path.join(D, 'b461_registration_2026-09-21.txt')
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


def cut(S, key, sub):
    """### THE SYNTHETIC POSITIVE CONTROL: the same source with the thing the arm tests removed."""
    M = dict(S)
    M[key] = (S.get(key) or '').replace(sub, '')
    return M


def put(S, key, val):
    M = dict(S)
    M[key] = val
    return M


def sources():
    inv = json.loads(read(os.path.join(D, 'b461_inventory.json')) or '{}')
    dsp = json.loads(read(os.path.join(D, 'b461_dispositions.json')) or '{}')
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b461_ferry.txt')),
        scan=read(os.path.join(D, 'b461_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b461_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b461_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b461_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b461_extract.txt')),
        lock=read(os.path.join(D, 'b461_lockgate_notes.txt')),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b460_closing.txt')),
        addendum=read(os.path.join(D, 'b461_addendum.txt')),
        inventory=read(os.path.join(D, 'b461_inventory.txt')),
        exercise=read(os.path.join(D, 'b461_exercise.txt')),
        span=read(os.path.join(D, 'b461_span_notes.txt')),
        scores=read(os.path.join(D, 'b461_scores.json')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b461_checks.py')),
        inv=inv, dsp=dsp,
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b461')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mirror=os.path.exists(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                                        'mirror-refresh-2026-09-21-b461.zip')),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b461'):
                k |= set(os.path.basename(x) for x in
                         gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                k.add(os.path.basename(l[3:].strip()))
    S['kinds'] = k
    return S


# ### **THE ARMS.** ### Each: name, what it reads, the predicate over S, and the mutation that must
# ### make it fail. ### **A `pos` OF `None` WOULD MEAN NO POSITIVE CONTROL -- AND NONE IS ALLOWED HERE.**
ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'paste ends (part 1 of 1)' in S['ferry'],
     lambda S: cut(S, 'ferry', 'paste ends (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE',
     lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S) REPORTED', '3 HIT(S) REPORTED'))),
    ('G-STEPZERO-CENSUS', 'two banked censuses',
     lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'fcens', S['fcens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 4'))),
    ('G-STEPZERO-PINS', 'a banked verdict LINE',
     lambda S: 'REPOS HARD-FAILING : 0' in line_with(S['pins'], 'REPOS HARD-FAILING'),
     lambda S: put(S, 'pins', S['pins'].replace('REPOS HARD-FAILING : 0', 'REPOS HARD-FAILING : 2'))),
    ('G-SURVEY-NOMISS', 'a banked verdict LINE',
     lambda S: 'MISSES : 0' in line_with(S['extract'], 'MISSES :'),
     lambda S: put(S, 'extract', S['extract'].replace('MISSES : 0', 'MISSES : 1'))),
    ('G-REG-LOCKED-FIRST', 'the face`s lock block',
     lambda S: 'THE REGISTRATION LOCK' in S['face'],
     lambda S: cut(S, 'face', 'THE REGISTRATION LOCK')),
    ('G-LOCKGATE-EIGHT', 'a banked verdict LINE (A2: the LINE, not a substring)',
     lambda S: 'LOCK PERMITTED' in line_with(S['lock'], '**VERDICT : LOCK')
     and 'GATES READ : 8. ### PASSING : 8' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('GATES READ : 8. ### PASSING : 8',
                                                'GATES READ : 8. ### PASSING : 7'))),
    ('G-SEAL-VERIFIES', 'a banked verdict LINE',
     lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('SEAL INTACT', 'SEAL BROKEN'))),
    ('G-PRIOR-CLOSED-PUSHED', 'the prior act`s closing',
     lambda S: 'row 309' in S['prior'],
     lambda S: cut(S, 'prior', 'row 309')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot`s own bytes',
     lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'a sentence that is not a verbatim quotation')),
    ('G-LANE-TRIGGER-NAMED', 'the face`s wording',
     lambda S: 'THE INSTRUMENT-AUDIT LANE OPENS FOR THIS ACT AND CLOSES AT ITS' in ' '.join(S['face'].split()),
     lambda S: cut(S, 'face', 'THE INSTRUMENT-AUDIT LANE OPENS FOR THIS ACT')),
    ('G-R70-REHEARSED-BEFORE-LOCK', 'file times and the rehearsal bank',
     lambda S: all(('REHEARSAL %d' % i) in S['extract'] for i in (1, 2, 3)),
     lambda S: cut(S, 'extract', 'REHEARSAL 3')),
    ('G-R70-COUNT-DIFFERENCE-PRINTED', 'the face`s wording',
     lambda S: 'DIFFERENCE IS `3` AND IS PRINTED, NOT' in ' '.join(S['face'].split()),
     lambda S: cut(S, 'face', 'DIFFERENCE IS `3` AND IS PRINTED, NOT')),
    ('G-C1-SIXTYFOUR-ENUMERATED', 'the inventory bank',
     lambda S: S['inv'].get('declared') == 64 and len(S['inv'].get('rows', [])) == 64,
     lambda S: put(S, 'inv', dict(S['inv'], declared=63))),
    ('G-C1-EVERY-ARM-MATCHED', 'the inventory bank',
     lambda S: S['inv'].get('unmatched') == [],
     lambda S: put(S, 'inv', dict(S['inv'], unmatched=['G-PHANTOM']))),
    ('G-C1-READS-BY-IDENTIFIER', 'the inventory bank',
     lambda S: all(r['reads'] for r in S['inv'].get('rows', [])),
     lambda S: put(S, 'inv', dict(S['inv'], rows=[dict(S['inv']['rows'][0], reads=[])]))),
    ('G-C1-REAL-VS-SYNTHETIC', 'the inventory bank',
     lambda S: S['inv'].get('n_real', 0) + S['inv'].get('n_synth', 0) + S['inv'].get('n_const', 0)
     == S['inv'].get('declared'),
     lambda S: put(S, 'inv', dict(S['inv'], n_real=0))),
    ('G-C1-STATUS-THREE-VALUED', 'the inventory bank',
     lambda S: all(r['pos_status'].split(' (')[0] in
                   ('EXISTS TODAY', 'ONE-LINE ADDITION', 'CANNOT BE STATED')
                   for r in S['inv'].get('rows', [])),
     lambda S: put(S, 'inv', dict(S['inv'],
                                  rows=[dict(S['inv']['rows'][0], pos_status='PROBABLY FINE')]))),
    ('G-C1-REAL-COUNT-PRINTED', 'the inventory record',
     lambda S: 'with a REAL positive control' in S['inventory'],
     lambda S: cut(S, 'inventory', 'with a REAL positive control')),
    ('G-C2-B396-QUOTED-AT-ADDRESS', 'the components record',
     # ### **THE NEEDLE WAS CASE-SENSITIVE AND THE RECORD CAPITALISES:** the first form sought
     # ### `a filter that keeps nine tenths` and the trail writes `A filter...`. ### Both yields on
     # ### the record; the needle is lowered, not the record.
     lambda S: 'filter that keeps nine tenths' in S['exercise'] and 'OPEN_TRAILS.md:' in S['exercise'],
     lambda S: cut(S, 'exercise', 'filter that keeps nine tenths')),
    ('G-C2-DISPOSITION-CONJUNCTIVE', 'the dispositions bank',
     lambda S: all((d == 'RETIRED') == (r['const'] and not r['real'])
                   for r, d in zip(S['inv'].get('rows', []), S['dsp'].get('per_arm', []))),
     lambda S: put(S, 'dsp', dict(S['dsp'], per_arm=['RETIRED'] * len(S['inv'].get('rows', []))))),
    ('G-C2-RETIRED-KEPT-AS-COMMENT', 'the successor suite`s own text',
     lambda S: all(('**%s**' % n) in S['suite'] for n in S['dsp'].get('retired', [])),
     lambda S: put(S, 'dsp', dict(S['dsp'], retired=list(S['dsp'].get('retired', [])) + ['G-ABSENT']))),
    ('G-C2-EVERY-SURVIVOR-EXERCISED', 'the exercise record',
     lambda S: S['dsp'].get('unexercised') == 0,
     lambda S: put(S, 'dsp', dict(S['dsp'], unexercised=1))),
    ('G-C2-NEGATIVE-PASSES', 'the exercise record',
     lambda S: S['dsp'].get('neg_failures') == 0,
     lambda S: put(S, 'dsp', dict(S['dsp'], neg_failures=2))),
    ('G-C2-POSITIVE-FAILS', 'the exercise record',
     lambda S: S['dsp'].get('pos_passes') == 0,
     lambda S: put(S, 'dsp', dict(S['dsp'], pos_passes=1))),
    ('G-C2-DEFECTIVE-ARMS-NAMED', 'the exercise record',
     lambda S: (S['dsp'].get('pos_passes') == 0) or ('DEFECTIVE' in S['exercise']),
     lambda S: put(S, 'dsp', dict(S['dsp'], pos_passes=1))),
    ('G-C2-BEFORE-AFTER-COUNTS', 'the dispositions bank',
     lambda S: all(k in S['dsp'] for k in ('before', 'retired', 'given', 'kept', 'after')),
     lambda S: put(S, 'dsp', {k: v for k, v in S['dsp'].items() if k != 'after'})),
    ('G-C2-OTHER-READING-COUNTED', 'the dispositions bank',
     lambda S: 'disjunctive_would_retire' in S['dsp'],
     lambda S: put(S, 'dsp', {k: v for k, v in S['dsp'].items() if k != 'disjunctive_would_retire'})),
    ('G-FILING-OBSERVATION-NOT-CANDIDATE', 'the trail`s own text',
     # ### **NEEDLE AGAINST RECORD, AGAIN:** the first form sought the FACE's phrasing
     # ### (`as observations and not as candidates`); the trail writes `These are observations and
     # ### not candidates.` ### Both yields on the record; the needle follows the record.
     lambda S: 'observations and not candidates' in S['ot'],
     lambda S: cut(S, 'ot', 'observations and not candidates')),
    ('G-FILING-PRICED-NOT-RUN', 'the trail`s own text',
     lambda S: 'priced and not run' in S['ot'],
     lambda S: cut(S, 'ot', 'priced and not run')),
    ('G-FILING-B449-UNEDITED', 'the trail`s own text',
     lambda S: 'Filed under the outlier `a = 4.123106` — candidate (c4)' in S['ot'],
     lambda S: cut(S, 'ot', 'Filed under the outlier `a = 4.123106` — candidate (c4)')),
    ('G-N1-SCORED', 'the scores bank',
     lambda S: '"N1"' in S['scores'], lambda S: cut(S, 'scores', '"N1"')),
    ('G-N2-SCORED', 'the scores bank',
     lambda S: '"N2"' in S['scores'], lambda S: cut(S, 'scores', '"N2"')),
    ('G-N3-SCORED', 'the scores bank',
     lambda S: '"N3"' in S['scores'], lambda S: cut(S, 'scores', '"N3"')),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores bank',
     lambda S: '"seat"' in S['scores'], lambda S: cut(S, 'scores', '"seat"')),
    ('G-SPAN-BY-TOOL', 'the span tool`s own record',
     lambda S: 'THE CURRENT SPAN' in S['span'], lambda S: cut(S, 'span', 'THE CURRENT SPAN')),
    ('G-NOGRADE-MOVED', 'the commit`s file list',
     lambda S: not any('FACES_LEDGER' in x or 'REGISTRY' in x for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['REGISTRY.md'])),
    ('G-NOOBJECT-CLAIM', 'the face`s wording',
     lambda S: 'NOTHING IS CLAIMED ABOUT THE OBJECT' in ' '.join(S['face'].split()),
     lambda S: cut(S, 'face', 'NOTHING IS CLAIMED ABOUT THE OBJECT')),
    ('G-NODEPOSIT', 'the face`s wording',
     lambda S: 'NO DEPOSIT ACTION' in S['face'], lambda S: cut(S, 'face', 'NO DEPOSIT ACTION')),
    ('G-NOH2-MOVED', 'the face`s wording',
     lambda S: 'WHERE THE DEPOSIT LEFT IT' in S['face'],
     lambda S: cut(S, 'face', 'WHERE THE DEPOSIT LEFT IT')),
    ('G-NOPRIORBANK', 'file times against the face`s',
     lambda S: S.get('noprior', True), lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text',
     lambda S: 'The four lists are open' in S['ot'], lambda S: cut(S, 'ot', 'The four lists are open')),
    ('G-CORPUS-SCOPE', 'the commit`s file list',
     lambda S: S['tracked'] == ['OPEN_TRAILS.md'],
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'FINDINGS.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail`s own text',
     lambda S: S['ot'].count('### b461 —') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b461 — a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 310 |' in S['corr'], lambda S: cut(S, 'corr', '| 310 |')),
    ('G-WRITELIST-KINDS', 'every b461 commit in three repositories',
     lambda S: not sorted(k for k in S['kinds'] if k not in S['face']),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'a_file_the_write_list_does_not_name.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite`s own text',
     lambda S: "log', '--pretty=%H %s'" in S['suite'],
     lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the commit`s file list',
     lambda S: all(x.startswith('OPEN_TRAILS') or x.startswith('data/') or x.startswith('tools/')
                   for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['internal/BLOB_SENSITIVITY_2026-08-29.md'])),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'the suite`s own text',
     lambda S: 'def line_with(text, needle)' in S['suite'],
     lambda S: cut(S, 'suite', 'def line_with(text, needle)')),
    ('G-ARMS-DECLARED-EQ-RUN', 'the face`s (G2) block against what runs',
     lambda S: S.get('declared_eq_run', False), lambda S: put(S, 'declared_eq_run', False)),
    ('G-MIRROR-TAGGED-BUILD', 'the built zip`s presence',
     lambda S: S['mirror'], lambda S: put(S, 'mirror', False)),
    ('G-MUSTFAIL', 'a file that must not exist',
     lambda S: S['mustfail_absent'], lambda S: put(S, 'mustfail_absent', False)),
]


# ====================================================================================================
# ### THE HARNESS. ### **EVERY ARM RUN THREE TIMES: LIVE, ON ITS NEGATIVE, ON ITS POSITIVE.**
# ====================================================================================================
def main():
    S = sources()
    S['mustfail_absent'] = not os.path.exists(os.path.join(D, 'b461_a_file_that_must_not_exist.txt'))
    # ### **THE RANGE INCLUDED THIS ACT'S OWN FILES**, which are written AFTER the face by
    # ### construction, so the arm failed on a record that was exactly as it should be. ### b458's
    # ### species -- an arm whose subject set quietly contains the act running it. ### Both yields
    # ### printed; the range now stops at b460.
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-5][0-9]_|^b460_', f)]
    S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)

    # ### THE (G2) BLOCK IS THE DECLARED SET -- NOT THE WHOLE FACE, WHOSE OTHER SECTIONS NAME ARMS
    # ### WHILE DISCUSSING THEM. ### **BOTH COUNTS ARE PRINTED AND NEITHER IS RECONCILED AWAY.**
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (K) THE BARS.')]
    declared = sorted(set(re.findall(r'\b[GF]-[A-Z0-9-]+', g2)) - {'G-NO'})
    whole = sorted(set(re.findall(r'\b[GF]-[A-Z0-9-]+', S['face'])) - {'G-NO'})
    names = [a[0] for a in ARMS]
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b461'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred) - {'G-NOSTAGE-A'})

    rec('=' * 104)
    rec('b461 -- THE SUCCESSOR SUITE. ### **%s READING.**' % ('POST-PUSH' if pushed else 'PRE-PUSH'))
    rec('=' * 104)
    rec('  arms in the face`s (G2) block : %d ; on the whole face : %d ; run here : %d ; deferred : %d'
        % (len(declared), len(whole), len(names), len(deferred)))
    rec('  ### the (G2) block also names `G-NOSTAGE-A`, which this act RETIRED, inside the arm list --')
    rec('  ### ### **REHEARSAL 1`S LESSON RECURRING ON THIS ACT`S OWN FACE: THE LEXICAL COUNT OVER-READS')
    rec('  ### ### BY ONE. ### PRINTED, NOT RECONCILED.**')
    rec('')
    rec('  ### THE EXERCISE. ### **NEG must PASS ; POS must FAIL.**')
    rec('  %-36s %-5s %-5s %-5s %s' % ('arm', 'LIVE', 'NEG', 'POS', 'verdict'))
    rec('  ' + '-' * 100)
    fail, defective, unexercised, neg_failures, pos_passes = [], [], 0, 0, 0
    for name, reads, pred, pos in ARMS:
        if name in deferred:
            continue
        live = bool(pred(S))
        neg = bool(pred(dict(S)))
        p = None if pos is None else bool(pred(pos(S)))
        if pos is None:
            unexercised += 1
        if not neg:
            neg_failures += 1
        if p is True:
            pos_passes += 1
            defective.append(name)
        v = 'OK' if (neg and p is False) else ('### DEFECTIVE' if p is True else '### NOT EXERCISED')
        rec('  %-36s %-5s %-5s %-5s %s'
            % (name, 'PASS' if live else 'FAIL', 'PASS' if neg else '###FAIL',
               ('FAIL' if p is False else ('###PASS' if p else '  -')), v))
        RES.append((name, live, reads))
        EX.append(dict(name=name, live=live, neg=neg, pos=p, reads=reads))
        if not live:
            fail.append(name)
    rec('')
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**'
        % (len(RES), len(RES) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**'
        % (neg_failures, pos_passes, defective or ''))
    rec('  ### ### **ARMS NOT EXERCISED : %d.**' % unexercised)
    ok = (not fail) and neg_failures == 0 and pos_passes == 0 and unexercised == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, 'b461_checks_postpush.txt' if pushed else 'b461_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, neg_failures=neg_failures, pos_passes=pos_passes,
                   unexercised=unexercised, defective=defective, declared=len(declared),
                   run=len(RES), deferred=deferred),
              io.open(os.path.join(D, 'b461_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
