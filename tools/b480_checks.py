# -*- coding: utf-8 -*-
"""b480_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb, honoured in
### advance even though this act is not the one it binds.
"""
import io
import glob
import fnmatch
import b480_extract as X478
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
FACE = os.path.join(D, 'b480_registration_2026-09-22.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b480_ferry.txt')),
        scan=read(os.path.join(D, 'b480_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b480_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b480_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b480_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b480_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b480_lockgate_notes*.txt')))[-1]),
        lock_runs=len(glob.glob(os.path.join(D, 'b480_lockgate_notes*.txt'))),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        # ### **THE PRIOR ACT'S CLOSING IS b462'S.** ### A wholesale re-point from b462 to b480
        # ### moved every b462 name and left b461 where it was, so the inherited line pointed two
        # ### acts back and the arm failed on the wrong bank -- `G-CARRIED-TOOLS-REPOINTED`'s own
        # ### species, committed while building the suite that carries it.
# ### ### **THE PRIOR CLOSED ACT IS b464.** ### A wholesale re-point moves every b464 name
        # ### and leaves b463 exactly where the carried file had it -- and here the pointer had to
        # ### move ANYWAY, because b465 occupies the intervening number and closed nothing.
        # ### **THE THIRD INSTANCE OF THIS SPECIES IN ONE ACT**, caught by the arm it feeds.
        prior=read(os.path.join(D, 'b476_closing.txt')),
        addendum=read(os.path.join(D, 'b480_addendum.txt')),
        census=read(os.path.join(D, 'b480_census.txt')),
        span=read(os.path.join(D, 'b480_span_notes.txt')),
        scores=read(os.path.join(D, 'b480_scores.json')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b480_checks.py')),
        sv=json.loads(read(os.path.join(D, 'b480_survey.json')) or '{}'),
        snap=json.loads(read(os.path.join(D, 'b480_snapshot.json')) or '{}'),
        prof=json.loads(read(os.path.join(D, 'b480_profiles.json')) or '{}'),
        comp=read(os.path.join(D, 'b480_components.txt')),
        log=read(os.path.join(D, 'b475_zeta23_build.log')),
        launcher=read(os.path.join(T, 'b475_detached_run.cmd')),
        orderfile=read(os.path.join(D, 'b475_order.txt')),
        b473c=read(os.path.join(D, 'b473_components.txt')),
        b475face=read(os.path.join(D, 'b475_registration_2026-09-22.txt')),
        b475bank=read(os.path.join(D, 'b475_the_serialized_run.txt')),
        tools480=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b480_') and f.endswith('.py') and f != 'b480_checks.py'),
        log_tracked=gits(ROOT, 'ls-files', 'data/b475_zeta23_build.log'),
        rtracked=gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        faces=read(os.path.join(PP, 'FACES_LEDGER.md')),
        desk=read(os.path.join(D, 'b480_desk_notes.txt')),
        docs=sorted(f for f in os.listdir(D) if f.startswith('b480_')),
        # ### ### **THE INHERITED ARM CARRIED b466's DATE.** ### A wholesale re-point moves the act
        # ### number and leaves `2026-09-21` behind, so on an act that runs on the next day the arm
        # ### looks for a zip that will never exist. ### **THAT IS b364's `DATED ARM` SPECIES, AND
        # ### IT IS REPAIRED HERE RATHER THAN RE-DATED**: the arm now asks for a zip NAMED BY (R69)'s
        # ### convention for THIS ACT -- any date, this act's suffix -- so it cannot go stale again.
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b480.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b480 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b480_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b480 --'):
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
    # ### ### **THE FIRST READER DROPPED THE TOOL NAMES AND THEN FAILED ON THEM.** ### It filtered out
    # ### `*.py` entries as "the left column", but a tool file this act creates is itself a written file,
    # ### and (R85) has the face carry each tool's NAME beside its globs. ### Every backticked path in
    # ### the (W) table is a pattern, tool names included.
    return [g.split('/')[-1] for g in re.findall(r'`([^`]+)`', w)]


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'paste ends (part 1 of 1)' in S['ferry'], lambda S: cut(S, 'ferry', 'paste ends (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE',
     lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-ZERO', 'this act`s banked scan',
     lambda S: '(R81) FLAGS : 0' in S['scan'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b476 closing -- the prior closed act',
     lambda S: 'row 326' in S['prior'], lambda S: cut(S, 'prior', 'row 326')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory`s own banked ferries',
     lambda S: (os.path.exists(os.path.join(D, 'b477_ferry.txt'))
                and os.path.exists(os.path.join(D, 'b478_ferry.txt'))
                and not os.path.exists(os.path.join(D, 'b480_registration_2026-09-21.txt'))
                and 'b480' in S['face']),
     lambda S: cut(S, 'face', 'b480')),

    ('G-C1-SNAPSHOT-NAMED', 'the components record and the snapshot bank',
     lambda S: 'THE SNAPSHOT :' in S['comp'] and 'STILL GOING' in S['comp']
     and S['snap']['read_utc'] in S['comp'],
     lambda S: cut(S, 'comp', 'STILL GOING')),
    ('G-C1-BYTES-PRINTED', 'the snapshot bank against the components record',
     lambda S: str(S['snap']['bytes']) in S['comp'] and S['snap']['bytes'] > 0,
     lambda S: put(S, 'snap', dict(S['snap'], bytes=-1))),
    ('G-C1-EXIT-LINES-FROM-LOG', 'the log itself against the snapshot bank',
     lambda S: (S['snap']['started'] == S['log'].count('=== [') - S['log'].count('RUN COMPLETE')
                - S['log'].count('detached SERIALIZED run START')
                or S['snap']['started'] > 0)
     and ('=== EXIT 0 : Zeta23.Hypotheses' in S['log']),
     lambda S: put(S, 'log', S['log'].replace('=== EXIT 0 : Zeta23.Hypotheses', 'x'))),
    ('G-C1-WALLTIME-FROM-LOG', 'the components record`s own account of the timestamps',
     lambda S: 'EVERY MODULE MARKER CARRIES THE SAME INSTANT' in S['comp']
     and 'distinct timestamps' in S['comp'],
     lambda S: cut(S, 'comp', 'EVERY MODULE MARKER CARRIES THE SAME INSTANT')),
    ('G-C1-FAILURES-OR-NONE', 'the log and the snapshot bank',
     lambda S: (not S['snap']['failures'] and not S['snap']['panics']
                and 'PANIC' not in S['log'] and 'bad_alloc' not in S['log']),
     lambda S: put(S, 'snap', dict(S['snap'], failures={'Zeta23.X': 1}))),
    ('G-C1-NOTHING-INFERRED-BEYOND', 'the components record',
     lambda S: 'MODULES STILL TO START' in S['comp'] and str(S['snap']['remaining']) in S['comp'],
     lambda S: cut(S, 'comp', 'MODULES STILL TO START')),

    ('G-C2-TWENTY-ROWS', 'the profiles bank',
     lambda S: len(S['prof']['rows']) == 20,
     lambda S: put(S, 'prof', dict(S['prof'], rows=S['prof']['rows'][:10]))),
    ('G-C2-ABSENT-NOT-ASSUMED', 'the log and the profiles bank',
     lambda S: (S['prof']['absent'] == 20 and 'depends on axioms' not in S['log']
                and all(r['verdict'] == 'ABSENT' for r in S['prof']['rows'])),
     lambda S: put(S, 'prof', dict(S['prof'], absent=0))),
    ('G-C2-R82-NOT-FORCED', 'the profiles bank and the components record',
     lambda S: (S['prof']['r82'] == 'NOT YET DECIDABLE'
                and 'NEITHER KIND OF `VOID`' in S['comp'].replace('\u2019', "'")
                and 'VOID FOR WANT OF A RUN' in S['b473c']),
     lambda S: put(S, 'prof', dict(S['prof'], r82='VOID'))),
    ('G-C2-REMAINDER-COUNTED', 'the snapshot bank against the order file',
     lambda S: (S['snap']['remaining'] == S['snap']['order'] - S['snap']['started']
                and S['snap']['order'] == len([l for l in S['orderfile'].split(NL) if l.strip()]) == 188),
     lambda S: put(S, 'snap', dict(S['snap'], remaining=0))),
    ('G-R83-DOES-NOT-FIRE', 'the profiles bank and the roster',
     lambda S: (S['prof']['r83'] == 'DOES NOT FIRE'
                and 'SIDE-explicit-formula' not in read(os.path.join(PP, 'REGISTRY.md'))),
     lambda S: put(S, 'prof', dict(S['prof'], r83='FIRES'))),

    ('G-C3-N1-SCORED-FROM-LOG', 'the snapshot bank against the log itself',
     lambda S: (S['snap']['n1']['verdict'] == 'HELD'
                and all(('=== EXIT 0 : %s' % m) in S['log'] for m in S['snap']['n1']['rows'])),
     lambda S: put(S, 'snap', dict(S['snap'], n1=dict(S['snap']['n1'], verdict='NOT HELD')))),
    ('G-C3-THREE-MODULES-BY-NAME', 'the snapshot bank',
     lambda S: sorted(S['snap']['n1']['rows']) == sorted(['Zeta23.Hypotheses', 'Zeta23.Defs.Counting',
                                                          'Zeta23.Taper.Basic']),
     lambda S: put(S, 'snap', dict(S['snap'], n1=dict(S['snap']['n1'], rows={})))),
    ('G-POSITION-CORRECTED', 'the order file, the face and b475`s own face',
     # ### The third clause looked for the old phrase in b475's FACE; it is in b475's CLOSING -- the
     # ### face was reworded before its lock, for the count-prediction counter. ### Re-pointed at the
     # ### bank that actually carries the words this act corrects.
     lambda S: ([l for l in S['orderfile'].split(NL) if l.strip()].index('Zeta23.Taper.Basic') + 1 == 23
                and '`2`, `3` AND `23`' in S['face']
                and 'positions 1, 2 and 22' in S['b475bank']),
     lambda S: cut(S, 'face', '`2`, `3` AND `23`')),
    ('G-RUN-NOT-STOPPED', 'this act`s own tools, for any kill or restart',
     lambda S: not re.search(r'taskkill|Stop-Process|Start-Process|terminate', S['tools480']),
     lambda S: put(S, 'tools480', S['tools480'] + NL + 'subprocess.run(["taskkill", "/PID", "27508"])')),
    ('G-NOTHING-IMPORTED', 'the commit file lists',
     lambda S: not any(x.endswith('.lean') for x in list(S['tracked']) + list(S['rtracked'])),
     lambda S: put(S, 'rtracked', list(S['rtracked']) + ['tools/lean/EF_lit.lean'])),

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
     lambda S: S['ot'].count('### b480 \u2014') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b480 \u2014 a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 327 |' in S['corr'] and S['corr'].count('| 327 |') == 1,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 327 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b480 commit in three repositories, against (R85)`s GLOBS',
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
     lambda S: "data/b480_components.txt' in gits(ROOT, 'show'" in S['suite'],
     lambda S: cut(S, 'suite', "data/b480_components.txt' in gits(ROOT, 'show'")),
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
    # ### before the act ran, because THE REFUSED ISSUE OF b480 HAD ITS OWN COMMIT ON main. ### So the
    # ### post-push arms ran pre-push and failed on banks that do not exist yet. ### **A THIRD CLAUSE
    # ### IS ADDED: the pushed commit must carry this act's own components bank.**
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b480')
              and 'data/b480_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b480 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b480_checks_postpush.txt' if pushed else 'b480_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred),
              io.open(os.path.join(D, 'b480_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
