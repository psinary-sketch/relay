# -*- coding: utf-8 -*-
"""b471_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
FACE = os.path.join(D, 'b471_registration_2026-09-22.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b471_ferry.txt')),
        scan=read(os.path.join(D, 'b471_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b471_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b471_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b471_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b471_extract.txt')),
        lock=read(os.path.join(D, 'b471_lockgate_notes.txt')),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        # ### **THE PRIOR ACT'S CLOSING IS b462'S.** ### A wholesale re-point from b462 to b471
        # ### moved every b462 name and left b461 where it was, so the inherited line pointed two
        # ### acts back and the arm failed on the wrong bank -- `G-CARRIED-TOOLS-REPOINTED`'s own
        # ### species, committed while building the suite that carries it.
# ### ### **THE PRIOR CLOSED ACT IS b464.** ### A wholesale re-point moves every b464 name
        # ### and leaves b463 exactly where the carried file had it -- and here the pointer had to
        # ### move ANYWAY, because b465 occupies the intervening number and closed nothing.
        # ### **THE THIRD INSTANCE OF THIS SPECIES IN ONE ACT**, caught by the arm it feeds.
        prior=read(os.path.join(D, 'b470_closing.txt')),
        addendum=read(os.path.join(D, 'b471_addendum.txt')),
        census=read(os.path.join(D, 'b471_census.txt')),
        span=read(os.path.join(D, 'b471_span_notes.txt')),
        scores=read(os.path.join(D, 'b471_scores.json')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b471_checks.py')),
        sv=json.loads(read(os.path.join(D, 'b471_survey.json')) or '{}'),
        price=json.loads(read(os.path.join(D, 'b471_price.json')) or '{}'),
        launch=json.loads(read(os.path.join(D, 'b471_launch.json')).lstrip('\ufeff') or '{}'),
        close=json.loads(read(os.path.join(D, 'b471_close_state.json')).lstrip('\ufeff') or '{}'),
        pidfile=read(os.path.join(D, 'b471_zeta23_build.pid')),
        launcher=read(os.path.join(T, 'b471_detached_run.cmd')),
        tools471=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b471_') and f.endswith('.py') and f != 'b471_checks.py'),
        named=read(os.path.join(D, 'b471_named_axioms.txt')),
        comp=read(os.path.join(D, 'b471_components.txt')),
        spiral=read(os.path.join(PP, 'SPIRAL_MAP.md')),
        lic=read(os.path.join(D, 'anthropic-zeta23', 'formal-math', 'zeta23', 'LICENSE')),
        desk=read(os.path.join(D, 'b471_desk_notes.txt')),
        faces=read(os.path.join(PP, 'FACES_LEDGER.md')),
        rtracked=gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        clone_clean=gits(os.path.join(D, 'anthropic-zeta23', 'formal-math'), 'status', '--porcelain') == '',
        log_exists=os.path.exists(os.path.join(D, 'b471_zeta23_build.log')),
        log_tracked=gits(ROOT, 'ls-files', 'data/b471_zeta23_build.log'),
        docs=sorted(f for f in os.listdir(D) if f.startswith('b471_')),
        # ### ### **THE INHERITED ARM CARRIED b466's DATE.** ### A wholesale re-point moves the act
        # ### number and leaves `2026-09-21` behind, so on an act that runs on the next day the arm
        # ### looks for a zip that will never exist. ### **THAT IS b364's `DATED ARM` SPECIES, AND
        # ### IT IS REPAIRED HERE RATHER THAN RE-DATED**: the arm now asks for a zip NAMED BY (R69)'s
        # ### convention for THIS ACT -- any date, this act's suffix -- so it cannot go stale again.
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b471.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b471')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b471_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b471'):
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
    ('G-PRIOR-CLOSED-PUSHED', 'b470 closing -- the prior closed act',
     lambda S: 'row 319' in S['prior'], lambda S: cut(S, 'prior', 'row 319')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-R81-FLAGS-CHECKED', 'the survey bank',
     lambda S: len(S['sv'].get('flags', [])) == 7 and S['sv'].get('navigator_flags') == 0,
     lambda S: put(S, 'sv', dict(S['sv'], navigator_flags=1))),
    ('G-R81-CLAIMS-CHECKED', 'the survey bank against the kernels` own toolchain files',
     lambda S: S['sv'].get('pins', {}).get('SIDE-kernel') == read(os.path.join('D:', os.sep, 'SIDE-kernel', 'lean-toolchain')).strip()
     and 'divergence' in S['sv'].get('rules', {}).get('4', {}).get('text', ''),
     lambda S: put(S, 'sv', dict(S['sv'], pins={}))),

    ('G-C1-LAUNCHED-AFTER-SEAL', 'the launch bank and the face`s time',
     # ### ### **THE FIRST FORM COMPARED FILE MTIMES, AND A GIT BRANCH SWITCH REWROTE BOTH FILES AT ONE
     # ### INSTANT (16:47:11), SO IT FAILED ON EVIDENCE THAT SAYS NOTHING ABOUT WHEN THE ACT ACTED.** ### It
     # ### now compares the two times the record itself wrote: the seal's `locked at (UTC)` and the
     # ### launch's `started_utc` -- ISO strings in one zone, so string order is time order.
     lambda S: bool(S['launch'].get('started_utc')) and bool(re.search(r'locked at \(UTC\) : (\S+)', S['face']))
     and re.search(r'locked at \(UTC\) : (\S+)', S['face']).group(1) < S['launch'].get('started_utc', ''),
     lambda S: put(S, 'launch', dict(S['launch'], started_utc=''))),
    ('G-C1-PID-BANKED', 'the pid file against the launch bank',
     lambda S: S['pidfile'].strip() == str(S['launch'].get('pid')) and S['pidfile'].strip().isdigit(),
     lambda S: put(S, 'pidfile', '0')),
    ('G-C1-LOG-NAMED', 'the launcher and the launch bank',
     lambda S: 'D:\\relay\\data\\b471_zeta23_build.log' in S['launcher'] and S['log_exists'],
     lambda S: put(S, 'log_exists', False)),
    ('G-C1-THREADS-UNSET', 'the launcher`s own text',
     lambda S: 'set "LEAN_NUM_THREADS="' in S['launcher'] and S['launch'].get('lean_num_threads') == 'UNSET',
     lambda S: cut(S, 'launcher', 'set "LEAN_NUM_THREADS="')),
    ('G-C1-STEPS-AS-NAMED', 'the launcher`s own text, in order',
     lambda S: 0 < S['launcher'].find('lake build Solution') < S['launcher'].find('scripts\\PrintAxioms.lean')
     < S['launcher'].find('"%NAMED%"'),
     lambda S: cut(S, 'launcher', 'lake build Solution')),
    ('G-C1-NOT-POLLED', 'the act`s own tools, for any open of the log',
     lambda S: not re.search(r'open\([^)]*zeta23_build\.log', S['tools471']) and S['log_tracked'] == '',
     lambda S: put(S, 'tools471', S['tools471'] + "open('b471_zeta23_build.log')")),
    ('G-C1-STATE-AT-CLOSE', 'the close-state bank',
     lambda S: S['close'].get('state') in ('RUNNING', 'EXITED') and S['close'].get('pid') == S['launch'].get('pid'),
     lambda S: put(S, 'close', dict(S['close'], state=''))),
    ('G-C1-ELAPSED-PRINTED', 'the close-state bank',
     lambda S: isinstance(S['close'].get('elapsed_s'), (int, float)) and S['close'].get('elapsed_s', -1) >= 0,
     lambda S: put(S, 'close', dict(S['close'], elapsed_s=None))),
    ('G-C1-NAMED-FILE-OUTSIDE-CLONE', 'the launcher and the clone`s tracked tree',
     lambda S: 'scratchpad' in S['launcher'] and S['clone_clean'] is True and 'EF_lit_zetaZeroConfig' in S['named'],
     lambda S: put(S, 'clone_clean', False)),

    ('G-C2-RULES-AT-LINES', 'SPIRAL_MAP.md itself',
     lambda S: len(S['spiral'].split(NL)) > 380
     and S['spiral'].split(NL)[363].strip().startswith('2. **No Lake cross-dependencies')
     and S['spiral'].split(NL)[379].strip().startswith('7. **Composites vendor with attribution'),
     lambda S: put(S, 'spiral', '')),
    ('G-C2-CLOSURE-COUNTS', 'the price bank',
     lambda S: S['price'].get('closure_modules') == 57 and S['price'].get('zeta23_modules') == 316
     and S['price'].get('closure_lines', 0) > 0,
     lambda S: put(S, 'price', dict(S['price'], closure_modules=0))),
    ('G-C2-MATHLIB-DIRECT', 'the survey bank',
     lambda S: len(S['sv'].get('mathlib_direct', [])) == S['price'].get('mathlib_direct') == 89
     and all(x.startswith('Mathlib') for x in S['sv'].get('mathlib_direct', [])),
     lambda S: put(S, 'sv', dict(S['sv'], mathlib_direct=[]))),
    ('G-C2-LICENCE-QUOTED', 'the survey bank against LICENSE itself',
     lambda S: S['sv'].get('licence_s4', '')[:60] in re.sub(r'\s+', ' ', S['lic']) and '(d)' in S['sv'].get('licence_s4', ''),
     lambda S: put(S, 'sv', dict(S['sv'], licence_s4='nothing'))),
    ('G-C2-NOTICE-QUOTED', 'the components record',
     lambda S: 'PrimeNumberTheoremAnd' in S['comp'] and 'Copyright 2026 Anthropic, PBC' in S['comp'],
     lambda S: cut(S, 'comp', 'Copyright 2026 Anthropic, PBC')),
    ('G-C2-THREE-FIXES', 'the components record',
     lambda S: all(k in S['comp'] for k in ('(i) THE PIN', '(ii) THE ATTRIBUTION HEADER', '(iii) THE TOOLCHAIN')),
     lambda S: cut(S, 'comp', '(iii) THE TOOLCHAIN')),
    ('G-C2-EXTRA-RULES', 'the components record',
     lambda S: 'rule 8 --' in S['comp'] and 'rule 9 --' in S['comp'],
     lambda S: cut(S, 'comp', 'rule 9 --')),
    ('G-C2-NOTHING-COPIED', 'the commit file lists',
     lambda S: not any(x.endswith('.lean') for x in list(S['tracked']) + list(S['rtracked'])),
     lambda S: put(S, 'rtracked', list(S['rtracked']) + ['tools/lean/EF_lit.lean'])),

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
     lambda S: S['ot'].count('### b471 \u2014') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b471 \u2014 a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 320 |' in S['corr'], lambda S: cut(S, 'corr', '| 320 |')),
    ('G-WRITELIST-KINDS', 'every b471 commit in three repositories',
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
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b471'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD', 'G-C1-STATE-AT-CLOSE', 'G-C1-ELAPSED-PRINTED']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b471 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b471_checks_postpush.txt' if pushed else 'b471_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred),
              io.open(os.path.join(D, 'b471_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
