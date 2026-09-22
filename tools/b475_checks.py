# -*- coding: utf-8 -*-
"""b475_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb, honoured in
### advance even though this act is not the one it binds.
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
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
FACE = os.path.join(D, 'b475_registration_2026-09-22.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b475_ferry.txt')),
        scan=read(os.path.join(D, 'b475_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b475_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b475_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b475_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b475_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b475_lockgate_notes*.txt')))[-1]),
        lock_runs=len(glob.glob(os.path.join(D, 'b475_lockgate_notes*.txt'))),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        # ### **THE PRIOR ACT'S CLOSING IS b462'S.** ### A wholesale re-point from b462 to b475
        # ### moved every b462 name and left b461 where it was, so the inherited line pointed two
        # ### acts back and the arm failed on the wrong bank -- `G-CARRIED-TOOLS-REPOINTED`'s own
        # ### species, committed while building the suite that carries it.
# ### ### **THE PRIOR CLOSED ACT IS b464.** ### A wholesale re-point moves every b464 name
        # ### and leaves b463 exactly where the carried file had it -- and here the pointer had to
        # ### move ANYWAY, because b465 occupies the intervening number and closed nothing.
        # ### **THE THIRD INSTANCE OF THIS SPECIES IN ONE ACT**, caught by the arm it feeds.
        prior=read(os.path.join(D, 'b474_closing.txt')),
        addendum=read(os.path.join(D, 'b475_addendum.txt')),
        census=read(os.path.join(D, 'b475_census.txt')),
        span=read(os.path.join(D, 'b475_span_notes.txt')),
        scores=read(os.path.join(D, 'b475_scores.json')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b475_checks.py')),
        sv=json.loads(read(os.path.join(D, 'b475_survey.json')) or '{}'),
        launch=json.loads(read(os.path.join(D, 'b475_launch.json')).lstrip('\ufeff') or '{}'),
        state=json.loads(read(os.path.join(D, 'b475_state.json')) or '{}'),
        close=json.loads(read(os.path.join(D, 'b475_close_state.json')) or '{}'),
        comp=read(os.path.join(D, 'b475_components.txt')),
        launcher=read(os.path.join(T, 'b475_detached_run.cmd')),
        orderfile=read(os.path.join(D, 'b475_order.txt')),
        pidfile=read(os.path.join(D, 'b475_zeta23_build.pid')),
        named=read(os.path.join(D, 'b471_named_axioms.txt')),
        log473=read(os.path.join(D, 'b471_zeta23_build.log')),
        tools475=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b475_') and f.endswith('.py') and f != 'b475_checks.py'),
        clone_clean=gits(os.path.join(D, 'anthropic-zeta23', 'formal-math'), 'status', '--porcelain') == '',
        log_exists=os.path.exists(os.path.join(D, 'b475_zeta23_build.log')),
        log_tracked=gits(ROOT, 'ls-files', 'data/b475_zeta23_build.log'),
        rtracked=gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        faces=read(os.path.join(PP, 'FACES_LEDGER.md')),
        desk=read(os.path.join(D, 'b475_desk_notes.txt')),
        docs=sorted(f for f in os.listdir(D) if f.startswith('b475_')),
        # ### ### **THE INHERITED ARM CARRIED b466's DATE.** ### A wholesale re-point moves the act
        # ### number and leaves `2026-09-21` behind, so on an act that runs on the next day the arm
        # ### looks for a zip that will never exist. ### **THAT IS b364's `DATED ARM` SPECIES, AND
        # ### IT IS REPAIRED HERE RATHER THAN RE-DATED**: the arm now asks for a zip NAMED BY (R69)'s
        # ### convention for THIS ACT -- any date, this act's suffix -- so it cannot go stale again.
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b475.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b475')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b475_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b475'):
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

def globs_of(face):
    """### (R85): THE FACE'S (W) SECTION AS A LIST OF GLOBS. ### Every backticked path in the write-list
    ### table is a pattern; a written file matches if its basename matches any pattern's basename."""
    w = face[face.index('### (W) THE WRITE LIST'):face.index('### (Z) THE NOTHINGS')]
    return [g.split('/')[-1] for g in re.findall(r'`([^`]+)`', w) if not g.endswith('.py') or '*' in g]


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'paste ends (part 2 of 2)' in S['ferry'], lambda S: cut(S, 'ferry', 'paste ends (part 2 of 2)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE',
     lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAG-LABELLED', 'the banked scan',
     lambda S: '(R81) FLAGS : 1' in S['scan'] and 'Bare in the act text : 0' in S['scan'],
     lambda S: put(S, 'scan', S['scan'].replace('Bare in the act text : 0', 'Bare in the act text : 1'))),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b474 closing -- the prior closed act',
     lambda S: 'row 323' in S['prior'], lambda S: cut(S, 'prior', 'row 323')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),

    ('G-C1-LAUNCHED-AFTER-SEAL', 'the launch bank and the face`s own recorded time',
     lambda S: bool(S['launch'].get('started_utc')) and bool(re.search(r'locked at \(UTC\) : (\S+)', S['face']))
     and re.search(r'locked at \(UTC\) : (\S+)', S['face']).group(1) < S['launch'].get('started_utc', ''),
     lambda S: put(S, 'launch', dict(S['launch'], started_utc=''))),
    ('G-C1-PID-BANKED', 'the pid file against the launch bank',
     lambda S: S['pidfile'].strip() == str(S['launch'].get('pid')) and S['pidfile'].strip().isdigit(),
     lambda S: put(S, 'pidfile', '0')),
    ('G-C1-LOG-NAMED', 'the launcher and the launch bank',
     lambda S: 'D:\\relay\\data\\b475_zeta23_build.log' in S['launcher'] and S['log_exists'],
     lambda S: put(S, 'log_exists', False)),
    ('G-C1-THREADS-ONE', 'the launcher`s own text and the launch bank',
     lambda S: 'set "LEAN_NUM_THREADS=1"' in S['launcher'] and S['launch'].get('lean_num_threads') == '1',
     lambda S: cut(S, 'launcher', 'set "LEAN_NUM_THREADS=1"')),
    ('G-C1-ORDER-FROM-FILE', 'the launcher against the banked order file',
     lambda S: ('%%ORDER%%' in S['launcher'] or '"%ORDER%"' in S['launcher'])
     and len([l for l in S['orderfile'].split(NL) if l.strip()]) == S['sv']['modules'] == 188,
     lambda S: put(S, 'orderfile', '')),
    ('G-C1-ONE-CALL-PER-MODULE', 'the launcher`s own loop',
     lambda S: 'for /f' in S['launcher'] and 'call lake build %%M' in S['launcher'],
     lambda S: cut(S, 'launcher', 'call lake build %%M')),
    ('G-C1-STEPS-AS-NAMED', 'the launcher`s own text, in order',
     lambda S: 0 < S['launcher'].find('call lake build %%M') < S['launcher'].find('scripts\\PrintAxioms.lean')
     < S['launcher'].find('"%NAMED%"'),
     lambda S: cut(S, 'launcher', 'scripts\\PrintAxioms.lean')),
    ('G-C1-NOT-POLLED', 'this act`s own tools, for any open of the new log',
     lambda S: not re.search(r'open\([^)]*b475_zeta23_build\.log', S['tools475'])
     and 'the log was not opened' in S['state'].get('how', '') and S['log_tracked'] == '',
     lambda S: put(S, 'tools475', S['tools475'] + "open('b475_zeta23_build.log')")),
    ('G-C1-STATE-AT-CLOSE', 'the close-state bank',
     lambda S: S['close'].get('state') in ('RUNNING', 'EXITED') and S['close'].get('pid') == S['launch'].get('pid'),
     lambda S: put(S, 'close', dict(S['close'], state=''))),
    ('G-C1-NAMED-FILE-OUTSIDE-CLONE', 'the launcher and the clone`s tracked tree',
     lambda S: 'scratchpad' in S['launcher'] and S['clone_clean'] is True and 'EF_lit_zetaZeroConfig' in S['named'],
     lambda S: put(S, 'clone_clean', False)),
    ('G-C1-CLONE-UNTOUCHED', 'the clone`s own git status',
     lambda S: S['clone_clean'] is True, lambda S: put(S, 'clone_clean', False)),

    ('G-C2-ORDER-COMPUTED', 'the survey tool`s own text and its yield',
     lambda S: 'def order_from(root)' in S['tools475'] and S['sv']['modules'] == 188
     and S['sv']['order'][0] == 'Zeta23.Defs',
     lambda S: put(S, 'sv', dict(S['sv'], modules=0))),
    ('G-C2-ORDER-CONTROL', 'the survey bank',
     lambda S: S['sv']['inversions'] == 0, lambda S: put(S, 'sv', dict(S['sv'], inversions=2))),
    ('G-C2-THREE-PLACED', 'the survey bank and the components record',
     lambda S: (S['sv']['failed_positions'] == {'Zeta23.Hypotheses': 1, 'Zeta23.Defs.Counting': 2,
                                                'Zeta23.Taper.Basic': 22}
                and 'position 22 of 188' in S['comp']),
     lambda S: put(S, 'sv', dict(S['sv'], failed_positions={}))),
    ('G-C2-CEILING-NOT-IN-LOG', 'b473`s log itself',
     lambda S: S['sv']['memory_figures'] == 0
     and not re.search(r'\d[\d,\.]*\s*(?:MB|GB|MiB|GiB|bytes)\b', S['log473']),
     lambda S: put(S, 'log473', S['log473'] + NL + 'peak memory 12.5 GB')),
    ('G-C2-PANICS-QUOTED', 'the components record against b473`s log',
     lambda S: all(p in S['log473'] and p in S['comp'] for p in S['sv']['panic_lines']),
     lambda S: cut(S, 'comp', S['sv']['panic_lines'][0])),
    ('G-C2-NO-CEILING-SUPPLIED', 'the components record and the trail',
     lambda S: 'NOT IN THE LOG' in S['comp'].upper() and 'NOT IN THE LOG' in S['ot'].upper()
     and 'known by kind and not by size' in S['ot'],
     lambda S: cut(S, 'comp', 'NOT IN THE LOG')),

    ('G-R85-WRITELIST-BY-GLOB', 'the face`s (W) table and this suite`s own reader',
     lambda S: len(globs_of(S['face'])) >= 15 and any('*' in g for g in globs_of(S['face']))
     and 'def globs_of(face)' in S['suite'],
     # ### The first control renamed the heading, and `globs_of` still found it as a prefix -- a control
     # ### that cannot fail its own arm. ### It now empties the table between the two headings, which is
     # ### the state the arm exists to catch: a face that names tools and no patterns.
     lambda S: put(S, 'face', S['face'][:S['face'].index('### (W) THE WRITE LIST')]
                   + '### (W) THE WRITE LIST' + NL
                   + S['face'][S['face'].index('### (Z) THE NOTHINGS'):])),
    ('G-N1-SCORED-LATER', 'the scores bank',
     lambda S: '"N1"' in S['scores'] and 'SCORED BY THE ACT THAT READS THE LOG' in S['scores'],
     lambda S: cut(S, 'scores', 'SCORED BY THE ACT THAT READS THE LOG')),
    ('G-SEAT-EXPECTATION-STATED', 'the scores bank',
     lambda S: '"seat"' in S['scores'] and 'refuted' in S['scores'],
     lambda S: cut(S, 'scores', '"seat"')),

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
     lambda S: 'The four lists are open' in S['ot'], lambda S: cut(S, 'ot', 'The four lists are open')),
    ('G-CORPUS-SCOPE', 'the commit file list',
     lambda S: S['tracked'] == ['OPEN_TRAILS.md'],
     lambda S: put(S, 'tracked', ['OPEN_TRAILS.md', 'FINDINGS.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail own text',
     lambda S: S['ot'].count('### b475 \u2014') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b475 \u2014 a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 324 |' in S['corr'], lambda S: cut(S, 'corr', '| 324 |')),
    ('G-WRITELIST-KINDS', 'every b475 commit in three repositories, against (R85)`s GLOBS',
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
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'the suite`s own text -- b472`s repair, carried',
     lambda S: "data/b475_components.txt' in gits(ROOT, 'show'" in S['suite'],
     lambda S: cut(S, 'suite', "data/b475_components.txt' in gits(ROOT, 'show'")),
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
    # ### before the act ran, because THE REFUSED ISSUE OF b475 HAD ITS OWN COMMIT ON main. ### So the
    # ### post-push arms ran pre-push and failed on banks that do not exist yet. ### **A THIRD CLAUSE
    # ### IS ADDED: the pushed commit must carry this act's own components bank.**
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b475')
              and 'data/b475_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD', 'G-C1-STATE-AT-CLOSE']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b475 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b475_checks_postpush.txt' if pushed else 'b475_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred),
              io.open(os.path.join(D, 'b475_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
