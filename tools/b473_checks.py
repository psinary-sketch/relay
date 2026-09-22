# -*- coding: utf-8 -*-
"""b473_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb, honoured in
### advance even though this act is not the one it binds.
"""
import io
import glob
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
FACE = os.path.join(D, 'b473_registration_2026-09-22.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b473_ferry.txt')),
        scan=read(os.path.join(D, 'b473_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b473_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b473_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b473_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b473_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b473_lockgate_notes*.txt')))[-1]),
        lock_runs=len(glob.glob(os.path.join(D, 'b473_lockgate_notes*.txt'))),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        # ### **THE PRIOR ACT'S CLOSING IS b462'S.** ### A wholesale re-point from b462 to b473
        # ### moved every b462 name and left b461 where it was, so the inherited line pointed two
        # ### acts back and the arm failed on the wrong bank -- `G-CARRIED-TOOLS-REPOINTED`'s own
        # ### species, committed while building the suite that carries it.
# ### ### **THE PRIOR CLOSED ACT IS b464.** ### A wholesale re-point moves every b464 name
        # ### and leaves b463 exactly where the carried file had it -- and here the pointer had to
        # ### move ANYWAY, because b465 occupies the intervening number and closed nothing.
        # ### **THE THIRD INSTANCE OF THIS SPECIES IN ONE ACT**, caught by the arm it feeds.
        prior=read(os.path.join(D, 'b472_closing.txt')),
        addendum=read(os.path.join(D, 'b473_addendum.txt')),
        census=read(os.path.join(D, 'b473_census.txt')),
        span=read(os.path.join(D, 'b473_span_notes.txt')),
        scores=read(os.path.join(D, 'b473_scores.json')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b473_checks.py')),
        sv=json.loads(read(os.path.join(D, 'b473_survey.json')) or '{}'),
        build=json.loads(read(os.path.join(D, 'b473_build.json')) or '{}'),
        prof=json.loads(read(os.path.join(D, 'b473_profiles.json')) or '{}'),
        comp=read(os.path.join(D, 'b473_components.txt')),
        cmp_bank=read(os.path.join(D, 'b473_comparator.txt')),
        log=read(os.path.join(D, 'b471_zeta23_build.log')),
        pins_first=read(os.path.join(D, 'b473_pins_stepzero_firstrun.txt')),
        scan_tool=read(os.path.join(T, 'ferry_scan.py')),
        tools473=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b473_') and f.endswith('.py') and f != 'b473_checks.py'),
        faces=read(os.path.join(PP, 'FACES_LEDGER.md')),
        desk=read(os.path.join(D, 'b473_desk_notes.txt')),
        rtracked=gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        log_tracked=gits(ROOT, 'ls-files', 'data/b471_zeta23_build.log'),
        log_bytes_raw=os.path.getsize(os.path.join(D, 'b471_zeta23_build.log')),
        cache_present=os.path.isdir(os.path.join(D, 'anthropic-zeta23', 'formal-math', 'zeta23',
                                                 '.cache', 'palomar-comparator')),
        roster=read(os.path.join(PP, 'REGISTRY.md')),
        printaxioms=read(os.path.join(D, 'anthropic-zeta23', 'formal-math', 'zeta23',
                                      'scripts', 'PrintAxioms.lean')),
        faces_dirty=(gits(PP, 'status', '--porcelain', '--', 'FACES_LEDGER.md') != ''),
        docs=sorted(f for f in os.listdir(D) if f.startswith('b473_')),
        # ### ### **THE INHERITED ARM CARRIED b466's DATE.** ### A wholesale re-point moves the act
        # ### number and leaves `2026-09-21` behind, so on an act that runs on the next day the arm
        # ### looks for a zip that will never exist. ### **THAT IS b364's `DATED ARM` SPECIES, AND
        # ### IT IS REPAIRED HERE RATHER THAN RE-DATED**: the arm now asks for a zip NAMED BY (R69)'s
        # ### convention for THIS ACT -- any date, this act's suffix -- so it cannot go stale again.
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b473.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b473')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b473_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b473'):
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
     lambda S: 'paste ends (part 1 of 1)' in S['ferry'], lambda S: cut(S, 'ferry', 'paste ends (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE',
     lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-ZERO', 'the banked scan against the survey bank',
     lambda S: '(R81) FLAGS : 0' in S['scan'] and S['sv'].get('act_bare') == 0 and S['sv'].get('flags') == [],
     lambda S: put(S, 'sv', dict(S['sv'], act_bare=1))),
    ('G-STEPZERO-CENSUS', 'two banked censuses',
     lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'fcens', S['fcens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 3'))),
    ('G-STEPZERO-PINS-RETRY', 'both roster runs, the first kept whole',
     lambda S: 'REPOS HARD-FAILING : 0' in line_with(S['pins'], 'REPOS HARD-FAILING')
     and 'REPOS HARD-FAILING : 1' in line_with(S['pins_first'], 'REPOS HARD-FAILING')
     and 'UNRESOLVED' in S['pins_first'],
     lambda S: put(S, 'pins_first', '')),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b472 closing -- the prior closed act',
     lambda S: 'row 321' in S['prior'], lambda S: cut(S, 'prior', 'row 321')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),

    ('G-C1-LOG-READ-WHOLE', 'the build bank against the log`s RAW bytes',
     lambda S: S['build'].get('bytes') == S['log_bytes_raw']
     and S['build'].get('lines') == len(S['log'].split(NL)),
     lambda S: put(S, 'build', dict(S['build'], bytes=1))),
    ('G-C1-LOG-BYTES-MATCH', 'the log on disk against the survey`s pre-seal reading',
     lambda S: os.path.getsize(os.path.join(D, 'b471_zeta23_build.log')) == S['sv']['log']['bytes'],
     lambda S: put(S, 'sv', dict(S['sv'], log=dict(S['sv']['log'], bytes=0)))),
    ('G-C1-EXIT-LINES-QUOTED', 'the components record against the log`s own exit lines',
     lambda S: all(('=== EXIT %d : %s' % (v, k)) in S['log'] for k, v in S['build']['exits'].items())
     and S['build']['exits'].get('lake build Solution') == 1,
     lambda S: put(S, 'build', dict(S['build'], exits={'lake build Solution': 0}))),
    ('G-C1-LAST-FORTY', 'the components record against the log`s own tail',
     lambda S: S['log'].split(NL)[-2].strip() in S['comp'] and S['comp'].count('(1d) THE LAST FORTY LINES') == 1
     and len([l for l in S['comp'].split(NL) if re.match(r'    :\d+ ', l)]) >= 40,
     lambda S: cut(S, 'comp', '(1d) THE LAST FORTY LINES')),
    ('G-C1-FAILURES-OR-NONE', 'the build bank against the log`s own summary list',
     lambda S: len(S['build']['failures']) == len(S['build']['summary']) == 3
     and all(('- ' + f['module']) in S['log'] for f in S['build']['failures'])
     and all(f['stderr'] for f in S['build']['failures']),
     lambda S: put(S, 'build', dict(S['build'], failures=S['build']['failures'][:1]))),
    ('G-C1-WALLTIME-FROM-LOG', 'the build bank against the log`s own timestamp lines',
     lambda S: abs(S['build']['wall_s'] - 1383.05) < 0.01
     and '12:38:44.54' in S['log'] and '13:01:47.59' in S['log'],
     lambda S: put(S, 'build', dict(S['build'], wall_s=0.0))),
    ('G-C1-LOG-COMMITTED', 'relay`s tracked tree',
     lambda S: S['log_tracked'].strip() == 'data/b471_zeta23_build.log',
     lambda S: put(S, 'log_tracked', '')),

    ('G-C2-TWENTY-ROWS', 'the profiles bank',
     lambda S: len(S['prof']['rows']) == 20 and len(S['sv']['seventeen']) == 17 and len(S['sv']['ef']) == 3,
     lambda S: put(S, 'prof', dict(S['prof'], rows=S['prof']['rows'][:19]))),
    ('G-C2-NAMES-FROM-BOTH-LISTS', 'the source`s own two lists',
     lambda S: S['sv']['lists_agree'] is True and S['sv']['seventeen'] == S['sv']['comparator_names'],
     lambda S: put(S, 'sv', dict(S['sv'], lists_agree=False))),
    ('G-C2-LINES-VERBATIM', 'every non-ABSENT row against the log itself',
     lambda S: all(r['line'] and r['line'] in S['log'] for r in S['prof']['rows'] if r['verdict'] != 'ABSENT'),
     lambda S: put(S, 'prof', dict(S['prof'], rows=[dict(r, verdict='STANDARD THREE', line='invented line')
                                                    for r in S['prof']['rows']]))),
    ('G-C2-ABSENT-NOT-ASSUMED', 'the profiles bank against the log`s own text',
     lambda S: ('depends on axioms' not in S['log']
                and all(r['verdict'] == 'ABSENT' and r['line'] == '' for r in S['prof']['rows'])),
     lambda S: put(S, 'prof', dict(S['prof'], rows=[dict(r, verdict='STANDARD THREE')
                                                    for r in S['prof']['rows']]))),
    ('G-C2-STANDARD-THREE-QUOTED', 'the source`s own script, supplied',
     lambda S: 'propext, Classical.choice, Quot.sound' in S['printaxioms']
     and 'Every line must print exactly' in S['printaxioms'],
     lambda S: put(S, 'printaxioms', '')),
    ('G-C2-R82-DECIDED', 'the profiles bank',
     lambda S: S['prof']['r82']['verdict'] in ('HOLDS', 'VOID') and S['prof']['r82']['holds'] is False,
     lambda S: put(S, 'prof', dict(S['prof'], r82=dict(S['prof']['r82'], verdict='')))),
    ('G-C2-VOID-KIND-NAMED', 'the profiles bank and the components record',
     lambda S: S['prof']['r82']['kind'] == 'FOR WANT OF A RUN'
     and 'VOID FOR WANT OF A RUN' in S['comp'] and 'NOT BECAUSE A' in S['comp'],
     lambda S: put(S, 'prof', dict(S['prof'], r82=dict(S['prof']['r82'], kind='')))),
    ('G-C2-GRADE-DISPOSED', 'the components record and the commit file list',
     lambda S: 'DERIVES, CONDITIONAL' in S['comp']
     and not any(x.endswith(('FACES_LEDGER.md', 'REGISTRY.md')) for x in list(S['tracked']) + list(S['rtracked'])),
     lambda S: cut(S, 'comp', 'DERIVES, CONDITIONAL')),

    ('G-C3-COMPARATOR-PRICED', 'the comparator bank',
     lambda S: 'NOT RUN' in S['cmp_bank'] and 'Requires Linux' in S['cmp_bank']
     and all(t in S['cmp_bank'] for t in ('go', 'cargo', 'landrun')),
     lambda S: put(S, 'cmp_bank', 'NOT RUN')),
    ('G-C3-NOTHING-FETCHED', 'the clone`s own tree',
     lambda S: S['cache_present'] is False and S['prof']['comparator']['cache_present'] is False,
     lambda S: put(S, 'cache_present', True)),
    ('G-R83-NO-KERNEL-MADE', 'the roster and the working trees',
     lambda S: 'SIDE-explicit-formula' not in S['roster']
     and not os.path.isdir(os.path.join('D:', os.sep, 'SIDE-explicit-formula'))
     and not any('explicit-formula' in x for x in list(S['tracked']) + list(S['rtracked'])),
     lambda S: put(S, 'roster', S['roster'] + NL + '| SIDE-explicit-formula |')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'the suite`s own text -- b472`s repair, carried',
     lambda S: "data/b473_components.txt' in gits(ROOT, 'show'" in S['suite'],
     lambda S: cut(S, 'suite', "data/b473_components.txt' in gits(ROOT, 'show'")),

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
     lambda S: 'where the deposit left it' in S['ot'], lambda S: cut(S, 'ot', 'where the deposit left it')),
    ('G-NOPRIORBANK', 'file times against the face',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail own text',
     lambda S: 'The four lists are open' in S['ot'], lambda S: cut(S, 'ot', 'The four lists are open')),
    ('G-CORPUS-SCOPE', 'the commit file list',
     lambda S: S['tracked'] == ['OPEN_TRAILS.md'],
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'FINDINGS.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail own text',
     lambda S: S['ot'].count('### b473 \u2014') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b473 \u2014 a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 322 |' in S['corr'], lambda S: cut(S, 'corr', '| 322 |')),
    ('G-WRITELIST-KINDS', 'every b473 commit in three repositories',
     lambda S: not sorted(k for k in S['kinds'] if k not in S['face']),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'a_name_the_write_list_does_not_carry.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite own text',
     lambda S: "log', '--pretty=%H %s'" in S['suite'], lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the commit file list',
     lambda S: all(x.startswith(('OPEN_TRAILS', 'data/', 'tools/')) for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['internal/BLOB_SENSITIVITY_2026-08-29.md'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the face (G2) block against what runs',
     lambda S: S.get('declared_eq_run', False), lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'the suite own text',
     lambda S: 'def line_with(text, needle)' in S['suite'], lambda S: cut(S, 'suite', 'def line_with(text, needle)')),
    ('G-MIRROR-TAGGED-BUILD', 'the built zip presence, UNDATED',
     lambda S: S['mirror'], lambda S: put(S, 'mirror', False)),
    ('G-MUSTFAIL', 'a file that must not exist',
     lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked tree, read in the source',
     lambda S: S['artefacts_tracked'] == '',
     lambda S: put(S, 'artefacts_tracked', 'data/anthropic-zeta23/claude_paper_2026-08-11.pdf')),
    ('G-CORPUS-LEAN-UNTOUCHED', 'the lv and kernel working trees, read in the source',
     lambda S: S['corpus_lean_clean'] is True, lambda S: put(S, 'corpus_lean_clean', False)),
]


def main():
    S = sources()
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (K) THE BARS.')]
    # ### ### **THE ARM-NAME REGEX COULD NOT SEE ONE OF THE FACE'S OWN ARMS.** ### `[A-Z0-9-]+`
    # ### stops at the first lowercase letter, so `G-C1-FORM-MATCHES-b456` was read as
    # ### `G-C1-FORM-MATCHES-` and the declared set disagreed with the run set by exactly that arm.
    # ### **THE FACE IS RIGHT AND THE COUNTER WAS WRONG** -- an act id is lowercase by this record's
    # ### own convention, and an arm may be named after one. ### Widened here, and the trailing
    # ### hyphen a bare name would leave is stripped so the two spellings cannot both survive.
    declared = sorted(set(x.rstrip('-') for x in
                          re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})
    names = [a[0] for a in ARMS]
    # ### ### **THE CARRIED PUSH PREDICATE READ THIS ACT AS ALREADY PUSHED.** ### Its two clauses --
    # ### origin/main == HEAD, and the last subject starting with this act's number -- were BOTH true
    # ### before the act ran, because THE REFUSED ISSUE OF b473 HAD ITS OWN COMMIT ON main. ### So the
    # ### post-push arms ran pre-push and failed on banks that do not exist yet. ### **A THIRD CLAUSE
    # ### IS ADDED: the pushed commit must carry this act's own components bank.**
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b473')
              and 'data/b473_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD', 'G-C1-LOG-COMMITTED']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b473 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b473_checks_postpush.txt' if pushed else 'b473_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred),
              io.open(os.path.join(D, 'b473_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
