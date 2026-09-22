# -*- coding: utf-8 -*-
"""b477_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb, honoured in
### advance even though this act is not the one it binds.
"""
import io
import glob
import fnmatch
import b477_extract as X478
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
FACE = os.path.join(D, 'b477_registration_2026-09-22.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b477_ferry.txt')),
        scan=read(os.path.join(D, 'b477_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b477_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b477_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b477_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b477_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b477_lockgate_notes*.txt')))[-1]),
        lock_runs=len(glob.glob(os.path.join(D, 'b477_lockgate_notes*.txt'))),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        # ### **THE PRIOR ACT'S CLOSING IS b462'S.** ### A wholesale re-point from b462 to b477
        # ### moved every b462 name and left b461 where it was, so the inherited line pointed two
        # ### acts back and the arm failed on the wrong bank -- `G-CARRIED-TOOLS-REPOINTED`'s own
        # ### species, committed while building the suite that carries it.
# ### ### **THE PRIOR CLOSED ACT IS b464.** ### A wholesale re-point moves every b464 name
        # ### and leaves b463 exactly where the carried file had it -- and here the pointer had to
        # ### move ANYWAY, because b465 occupies the intervening number and closed nothing.
        # ### **THE THIRD INSTANCE OF THIS SPECIES IN ONE ACT**, caught by the arm it feeds.
        prior=read(os.path.join(D, 'b480_closing.txt')),
        addendum=read(os.path.join(D, 'b477_addendum.txt')),
        census=read(os.path.join(D, 'b477_census.txt')),
        span=read(os.path.join(D, 'b477_span_notes.txt')),
        scores=read(os.path.join(D, 'b477_scores.json')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b477_checks.py')),
        sv=json.loads(read(os.path.join(D, 'b477_survey.json')) or '{}'),
        st=json.loads(read(os.path.join(D, 'b477_state.json')) or '{}'),
        launch=json.loads(read(os.path.join(D, 'b477_launch.json')).lstrip('\ufeff') or '{}'),
        close=json.loads(read(os.path.join(D, 'b477_close_state.json')) or '{}'),
        comp=read(os.path.join(D, 'b477_components.txt')),
        runner=read(os.path.join(T, 'b477_gram.py')),
        launcher=read(os.path.join(T, 'b477_detached_run.cmd')),
        pidfile=read(os.path.join(D, 'b477_gram.pid')),
        refused=read(os.path.join(D, 'b477_ferry_refused.txt')),
        prior_ferry=read(os.path.join(D, 'b477_ferry_prior.txt')),
        b476reg=read(os.path.join(D, 'b476_registration_2026-09-22.txt')),
        b476seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
                                 os.path.join(D, 'b476_registration_2026-09-22.txt')],
                                capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        chain=read(os.path.join(T, 'b321_window.py')),
        square=read(os.path.join(T, 'b318_square.py')),
        tools477=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b477_') and f.endswith('.py') and f != 'b477_checks.py'),
        log_tracked=gits(ROOT, 'ls-files', 'data/b477_gram.log'),
        rtracked=gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL),
        corpus_lean_clean=(gits(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'status', '--porcelain') == ''
                           and gits(os.path.join('D:', os.sep, 'SIDE-kernel'), 'status', '--porcelain') == ''),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        faces=read(os.path.join(PP, 'FACES_LEDGER.md')),
        desk=read(os.path.join(D, 'b477_desk_notes.txt')),
        docs=sorted(f for f in os.listdir(D) if f.startswith('b477_')),
        # ### ### **THE INHERITED ARM CARRIED b466's DATE.** ### A wholesale re-point moves the act
        # ### number and leaves `2026-09-21` behind, so on an act that runs on the next day the arm
        # ### looks for a zip that will never exist. ### **THAT IS b364's `DATED ARM` SPECIES, AND
        # ### IT IS REPAIRED HERE RATHER THAN RE-DATED**: the arm now asks for a zip NAMED BY (R69)'s
        # ### convention for THIS ACT -- any date, this act's suffix -- so it cannot go stale again.
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b477.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b477 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b477_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b477 --'):
                k |= set(os.path.basename(x) for x in
                         gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                name = os.path.basename(l[3:].strip())
                # ### **A FILE ANOTHER ACT'S RUNNING PROCESS IS WRITING IS NOT THIS ACT'S WRITE.**
                # ### b475's detached build still appends to its log, which shows as modified here.
                if name == 'b475_zeta23_build.log':
                    continue
                k.add(name)
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
    # ### ### **THE OPERATIVE FERRY IS THE ONE THAT ORDERED THE RUN**, part 1 of 1, and the act's own
    # ### bank now holds it. ### The PRIOR re-issue (part 1 of 2, carrying the author's `:15`
    # ### substitution) is kept as `b477_ferry_prior.txt`, and the refused text beside it.
    ('G-SUBSTITUTION-APPLIED', 'the prior re-issue against the refused text',
     lambda S: ('the diagonal before any off-diagonal entry:' in S['prior_ferry']
                and 'the diagonal first:' not in S['prior_ferry']
                and 'the diagonal first:' in S['refused']),
     lambda S: put(S, 'prior_ferry', S['refused'])),
    ('G-REFUSED-TEXT-KEPT', 'the refused ferry, kept whole beside the re-issue',
     lambda S: 'paste ends (part 1 of 2)' in S['refused'] and S['refused'] != S['ferry'],
     lambda S: put(S, 'refused', S['ferry'])),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b480 closing -- the prior closed act',
     lambda S: 'row 327' in S['prior'], lambda S: cut(S, 'prior', 'row 327')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '', lambda S: put(S, 'addendum', 'not a verbatim quotation')),

    ('G-R87-APPENDED-BELOW-LOCK', 'b476`s registration itself',
     # ### `.index` raises when the control removes the needle; `find` with a guard does not.
     lambda S: (0 <= S['b476reg'].find('THE REGISTRATION LOCK')
                < S['b476reg'].find('THE AMENDMENT UNDER (R87)')),
     lambda S: put(S, 'b476reg', S['b476reg'].replace('THE AMENDMENT UNDER (R87)', 'x'))),
    ('G-R87-SEAL-STILL-INTACT', 'reg_seal --verify on b476, run in the source',
     lambda S: 'SEAL INTACT' in S['b476seal'],
     lambda S: put(S, 'b476seal', S['b476seal'].replace('SEAL INTACT', 'SEAL BROKEN'))),
    ('G-R87-ORIENTATION-CARRIED', 'the face, the components record and the scores',
     lambda S: all('-G' in x for x in (S['face'], S['comp']))
     and 'LARGEST' in S['face'] and 'largest eigenvalue of g' in S['scores'].lower(),
     lambda S: put(S, 'scores', S['scores'].replace('LARGEST eigenvalue of G', 'x'))),

    ('G-BUILDER-CONTROL-EXACT', 'the survey bank',
     lambda S: (S['sv']['control']['within'] is True and S['sv']['control']['diff'] < 1.49e-08
                and S['sv']['control']['window_diff'] < 1.49e-08),
     lambda S: put(S, 'sv', dict(S['sv'], control=dict(S['sv']['control'], within=False, diff=1.0)))),
    ('G-CHAIN-UNEDITED', 'b321_window.py and b318_square.py, by their working state',
     lambda S: (gits(ROOT, 'status', '--porcelain', '--', 'tools/b321_window.py') == ''
                and gits(ROOT, 'status', '--porcelain', '--', 'tools/b318_square.py') == ''
                and 'def channels(v, w)' in S['chain'] and 'def autocorrelation(f' in S['square']),
     lambda S: put(S, 'chain', '')),
    ('G-DIAGONAL-BY-THE-CHAIN', 'the runner`s own source',
     lambda S: 'f = SQ.autocorrelation(seeds[a])' in S['runner']
     and 'def cross(' in S['runner'],
     lambda S: cut(S, 'runner', 'f = SQ.autocorrelation(seeds[a])')),
    ('G-CONTROL-SIDE-STATED', 'the components record and the survey bank',
     lambda S: ('NO ZERO SIDE' in S['comp'] and 'places' in S['sv']['control_keys']
                and 'zero' not in S['sv']['control_keys']),
     lambda S: put(S, 'sv', dict(S['sv'], control_keys=S['sv']['control_keys'] + ['zero']))),
    ('G-CONTROL-CHAIN-IS-EPSTEIN', 'the runner`s own source',
     lambda S: 'import b325_epstein as EP' in S['runner'] and 'EP.channels_q(' in S['runner'],
     lambda S: cut(S, 'runner', 'EP.channels_q(')),

    ('G-RUN-LAUNCHED-AFTER-SEAL', 'the launch bank against the face`s own recorded time',
     lambda S: bool(re.search(r'locked at \(UTC\) : (\S+)', S['face']))
     and re.search(r'locked at \(UTC\) : (\S+)', S['face']).group(1) < S['launch'].get('started_utc', ''),
     lambda S: put(S, 'launch', dict(S['launch'], started_utc='2000-01-01T00:00:00Z'))),
    ('G-RUN-PID-BANKED', 'the pid file against the launch bank',
     lambda S: S['pidfile'].strip() == str(S['launch'].get('pid')) and S['pidfile'].strip().isdigit(),
     lambda S: put(S, 'pidfile', '0')),
    ('G-RUN-LOG-NAMED', 'the launcher and the launch bank',
     lambda S: 'b477_gram.log' in S['launcher'] and S['launch']['log'].endswith('b477_gram.log')
     and os.path.exists(os.path.join(D, 'b477_gram.log')),
     lambda S: put(S, 'launcher', '')),
    ('G-RUN-DETACHED', 'the launch bank and the launcher',
     lambda S: S['launch'].get('detached') is True and 'b477_gram.py' in S['launcher'],
     lambda S: put(S, 'launch', dict(S['launch'], detached=False))),
    ('G-RUN-ORDER-DIAGONAL-FIRST', 'the runner`s own source, in order',
     lambda S: 0 <= S['runner'].find('THE DIAGONAL FIRST') < S['runner'].find('THE OFF-DIAGONALS'),
     lambda S: put(S, 'runner', S['runner'].replace('THE DIAGONAL FIRST', 'x'))),
    ('G-RUN-HALT-RULE-IN-CODE', 'the runner`s own source',
     lambda S: 'NO OFF-DIAGONAL ENTRY IS COMPUTED' in S['runner'] and 'return 2' in S['runner'],
     lambda S: cut(S, 'runner', 'return 2')),
    ('G-RUN-ENTRIES-FLUSHED', 'the runner`s own source and the entries file',
     lambda S: 'out.flush()' in S['runner']
     and os.path.exists(os.path.join(D, 'b477_entries.jsonl')),
     lambda S: cut(S, 'runner', 'out.flush()')),
    ('G-RUN-TIMESTAMPS-REAL', 'the runner`s own source against b475`s launcher',
     lambda S: 'datetime.datetime.now' in S['runner']
     and '%time%' in read(os.path.join(T, 'b475_detached_run.cmd')),
     lambda S: cut(S, 'runner', 'datetime.datetime.now')),
    ('G-NO-EIGENVALUE-HERE', 'this act`s own tools',
     # ### `eigh` matched inside `weight` -- the same substring trap as `gram` inside `program`.
     # ### The arm now looks for a CALL or an import, not for letters inside a word.
     lambda S: not re.search(r'\beigvalsh?\(|\beigh\(|linalg\.eig|scipy\.linalg',
                             S['tools477']),
     lambda S: put(S, 'tools477', S['tools477'] + NL + 'np.linalg.eigh(G)')),
    ('G-NOT-POLLED', 'this act`s own tools, for any read of the gram log',
     lambda S: not re.search(r'open\([^)]*b477_gram\.log', S['tools477'])
     and 'the log was not opened' in S['st'].get('how', '').replace('neither the log nor the entries file was read',
                                                                    'the log was not opened'),
     lambda S: put(S, 'tools477', S['tools477'] + "open('b477_gram.log')")),
    ('G-STATE-AT-CLOSE', 'the close-state bank',
     lambda S: S['close'].get('state') in ('RUNNING', 'EXITED') and S['close'].get('pid') == S['launch'].get('pid'),
     lambda S: put(S, 'close', dict(S['close'], state=''))),

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
     lambda S: S['ot'].count('### b477 \u2014') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b477 \u2014 a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: '| 328 |' in S['corr'] and S['corr'].count('| 328 |') == 1,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 328 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b477 commit in three repositories, against (R85)`s GLOBS',
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
     lambda S: "data/b477_components.txt' in gits(ROOT, 'show'" in S['suite'],
     lambda S: cut(S, 'suite', "data/b477_components.txt' in gits(ROOT, 'show'")),
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
    # ### before the act ran, because THE REFUSED ISSUE OF b477 HAD ITS OWN COMMIT ON main. ### So the
    # ### post-push arms ran pre-push and failed on banks that do not exist yet. ### **A THIRD CLAUSE
    # ### IS ADDED: the pushed commit must carry this act's own components bank.**
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b477')
              and 'data/b477_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD', 'G-STATE-AT-CLOSE']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b477 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b477_checks_postpush.txt' if pushed else 'b477_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred),
              io.open(os.path.join(D, 'b477_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
