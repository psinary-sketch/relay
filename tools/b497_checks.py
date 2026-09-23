# -*- coding: utf-8 -*-
"""b497_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb.
### ### **THE CARRIED ARMS WERE RE-POINTED ONE AT A TIME**, each read against THIS act's banks
### before its pointer moved -- b480 recorded three instances of the wholesale-substitution species
### in a single act, and this file is written against that.
"""
import io
import glob
import hashlib
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
KERNEL = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
FACE = os.path.join(D, 'b497_registration_2026-09-23.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b497_ferry.txt')),
        scan=read(os.path.join(D, 'b497_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b497_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b497_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b497_pins_stepzero.txt')),
        extract=read(os.path.join(D, 'b497_extract.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b497_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b493_closing.txt')),
        addendum=read(os.path.join(D, 'b497_addendum.txt')),
        comp=read(os.path.join(D, 'b497_components.txt')),
        desk=read(os.path.join(D, 'b497_desk_notes.txt')),
        span=read(os.path.join(D, 'b497_span_notes2.txt'))
        + read(os.path.join(D, 'b497_span_notes.txt')),
        res=json.loads(read(os.path.join(D, 'b497_results.json')) or '{}'),
        sc=json.loads(read(os.path.join(D, 'b497_scores.json')) or '{}'),
        # ### ### **THE LOG IS A SOURCE OF THIS ACT, AND OF NO OTHER.** ### b495 was forbidden to
        # ### read it and b496 was forbidden to poll it; (R108)'s order hands it here.
        # ### ### **THE WORLD IS READ INTO A SOURCE SO THE HARNESS CAN MUTATE IT.** ### An arm
        # ### that calls `tasklist` inside its own predicate cannot be falsified by a control over
        # ### `S`, and its first version took a NO-OP control and duly PASSED it. ### b496's
        # ### lesson, immediately: ### **A PROPERTY OF THE WORLD MUST ENTER AS A SOURCE.**
        pid_alive=('7860' in subprocess.run(
            ['tasklist', '/FI', 'PID eq 7860'], capture_output=True, text=True,
            errors='replace').stdout),
        log=read(os.path.join(D, 'b495_ef_build.log')),
        logbytes=(os.path.getsize(os.path.join(D, 'b495_ef_build.log'))
                  if os.path.exists(os.path.join(D, 'b495_ef_build.log')) else 0),
        comptool=read(os.path.join(T, 'b497_components.py')),
        tblj=json.loads(read(os.path.join(D, 'terminal_table.json')) or '{}'),
        gen=read(os.path.join(T, 'terminal_table.py')),
        registry=read(os.path.join(PP, 'REGISTRY.md')),

        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b497_checks.py')),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        # ### ### **`G-CORPUS-LEAN-UNTOUCHED` RETURNS.** ### b495 retired it because that
        # ### act created a repository OF Lean files; THIS act writes none anywhere, so the
        # ### arm is meaningful again and the source it reads comes back with it.
        corpus_lean_clean=all(
            gits(os.path.join('D:', os.sep, r), 'status', '--porcelain') == ''
            for r in ('SIDE-lv-conservation', 'SIDE-kernel', 'SIDE-explicit-formula')),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b497.zip'))),
        spantool_clean=(gits(ROOT, 'status', '--porcelain', '--', 'tools/b363_span.py') == ''),
        tools497=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b497_') and f.endswith('.py')
                         and f != 'b497_checks.py'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b497 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b497_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b497 --'):
                k |= set(os.path.basename(x) for x in
                         gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
        # ### ### **A FILE DIRTY BEFORE THIS ACT BEGAN WAS NOT WRITTEN BY IT.**
        # ### `b475_zeta23_build.log` has been modified-but-uncommitted since b475's run died,
        # ### and a bare `status` reading calls it one of THIS act's writes forever. ### The
        # ### write list bounds what the ACT writes, so the population is narrowed to files
        # ### whose mtime is AT OR AFTER the sealed face's -- and the ground is printed.
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                rel = l[3:].strip()
                full = os.path.join(repo, rel)
                try:
                    if os.path.getmtime(full) < os.path.getmtime(FACE):
                        continue
                except OSError:
                    pass
                k.add(os.path.basename(rel))
    # ### b475's log is still being written by another act's live process; excluded BY NAME.
    S['kinds'] = k
    # ### ### **NO EXCLUSION. THE GROUND LAPSED AND THIS ACT RE-TESTED IT.**
    # ### b481 to b489 excused `b475_zeta23_build.log` because "another act's live process is
    # ### still appending to it". ### Component 0 finds pid 27508 ABSENT at two readings sixty
    # ### seconds apart, no `lean` or `lake` process at either, and the file cold for hours.
    # ### **AN EXCEPTION IS A CLAIM ABOUT THE WORLD AND DECAYS LIKE ONE**, so it is retired and
    # ### the arm runs at full width over every prior bank.
    LIVE = set()
    prior = [f for f in os.listdir(D)
             if re.match(r'^b4[0-7][0-9]_|^b48[0-9]_', f) and not f.startswith('b497_') and f not in LIVE]
    S['prior_checked'] = len(prior)
    S['noprior'] = all(os.path.getmtime(os.path.join(D, f)) < os.path.getmtime(FACE) for f in prior)
    return S


def declared_arms(face):
    """### ### **THE ARMS THE FACE DECLARES, MINUS THE ONES IT EXPRESSLY RETIRES.**
    ### This face says in its own (G2) block that `G-NOB475LOG` ### *"IS NOT CARRIED FORWARD
    ### UNDER THAT NAME"* ### and names its replacement. ### **AN ARM A FACE RETIRES IN WORDS IS
    ### NOT AN ARM IT DECLARES**, and a counter that reads only the token disagrees with the
    ### sentence beside it. ### The face is sealed; the COUNTER is what was wrong."""
    names = set(re.findall(r'`(G-[A-Z0-9-]+)`', face))
    for m in re.finditer(r'`(G-[A-Z0-9-]+)` IS NOT CARRIED FORWARD', face):
        names.discard(m.group(1))
    return names


def globs_of(face):
    """### (R85) as (R91) amends it: THE FACE'S (W) SECTION AS A LIST OF GLOBS, the act's own stem
    ### glob included -- which is the whole point of (R91)."""
    w = face[face.index('### (W) THE WRITE LIST'):face.index('### (Z) THE NOTHINGS')]
    return [g.split('/')[-1] for g in re.findall(r'`([^`]+)`', w)]


def sc(S, k):
    return (S['sc'] or {})


def res(S, k, d=None):
    return (S['res'] or {}).get(k, d)


def seg(text, marker, n=220):
    """### ### **THE TEXT AFTER A MARKER, OR EMPTY WHEN THE MARKER IS GONE.**
    ### A negative control removes the marker; a bare `split(...)[1]` then RAISES instead of
    ### failing, and ### **AN ARM THAT CRASHES UNDER ITS CONTROL HAS NOT BEEN EXERCISED.**"""
    parts = (text or '').split(marker)
    return parts[1][:n] if len(parts) > 1 else ''


def res(S, k, d=None):
    return (S['res'] or {}).get(k, d)


def seg(text, marker, n=260):
    """### the text after a marker, or EMPTY when the control removes it."""
    parts = (text or '').split(marker)
    return parts[1][:n] if len(parts) > 1 else ''


def rows(S):
    return (S['cells'] or {}).get('rows') or []
def res(S, k, d=None):
    return (S['res'] or {}).get(k, d)


def seg(text, marker, n=300):
    parts = (text or '').split(marker)
    return parts[1][:n] if len(parts) > 1 else ''


PIN_SHA = '3635e74826a4c1fcece7d1cd2b6fa75e43a00510'
STMT_SHA = '0255fa699a72c941d7dcb70e0232a0184fb9e0c48c66659a6a237c4022000fe6'
NAMES3 = ('EF_lit_zetaZeroConfig', 'Zeta23.EF.EF_lit', 'EF_lit_zeta')

def top_level_assign(text):
    """### ### **IS THERE A `:=` AT BRACKET DEPTH 0?** ### `(C := C)` is a NAMED ARGUMENT and
    ### `let n := c.1` inside a `fun` is a binding; neither hands a declaration to its proof."""
    depth = 0
    i = 0
    while i < len(text) - 1:
        c = text[i]
        if c in '([{':
            depth += 1
        elif c in ')]}':
            depth -= 1
        elif c == ':' and text[i + 1] == '=' and depth <= 0:
            return True
        i += 1
    return False


def strip_prose(text):
    """### ### **A `G-NO*` ARM MUST NOT READ THE ACT'S OWN SENTENCE SAYING IT DID NOT DO IT.**

    ### The trail writer holds its record in a module-level string; scanning that string for the
    ### forbidden word finds the DENIAL. ### This removes triple-quoted blocks and comments, so
    ### what remains is CODE, which is the only place a call can be. ### b487 minted this rule and
    ### this act re-learned it by being caught twice on one run.
    """
    t = re.sub(r'"""[\s\S]*?"""', ' ', text or '')
    t = re.sub(r"'''[\s\S]*?'''", ' ', t)
    t = re.sub(r'^\s*#.*$', ' ', t, flags=re.M)
    return t


def live_limb_guard(suite):
    """### ### **THE GUARD AGAINST A CONTROL THAT LEAVES A LIVE LIMB, AND WHERE IT ACTUALLY IS.**

    ### b495's `G-PUSHED-PREDICATE-THREE-CLAUSED` passed its own positive control because its
    ### predicate was `A or B` and the mutation falsified only `B`. ### This act declared a new arm
    ### to catch that species BY READING THE SUITE'S TEXT, and ### **FOUR REVISIONS LATER THE
    ### ### TEXTUAL PROXY STILL COULD NOT DO IT**: it fired on `x or []` none-defaults, on the word
    ### `or` inside quoted strings, on its own source, and on `any(A or B for ...)` whose control
    ### DOES falsify both limbs.
    ### ### **THE REASON IS THAT THE PROPERTY IS NOT TEXTUAL.** ### Whether a control falsifies
    ### every limb is a fact about what the control DOES, and the only thing that can decide it is
    ### ### **RUNNING THE CONTROL** -- which this harness already does for every arm, and whose
    ### result is the `POS` column and the `POSITIVE-CONTROL PASSES` count. ### **b495 WAS CAUGHT
    ### ### BY THAT COLUMN AND BY NOTHING ELSE.**
    ### So this arm no longer proxies. ### It asserts that the guard IS RUN: that the harness
    ### exercises a positive control on every arm, counts the passes, and ### **FAILS THE WHOLE
    ### ### SUITE ON A SINGLE ONE.**
    """
    need = ['p = bool(pred(pos(S)))',
            'defective.append(name)',
            'not defective']
    return [n for n in need if n not in suite]


def res(S, k, d=None):
    return (S['res'] or {}).get(k, d)


def seg(text, marker, n=300):
    parts = (text or '').split(marker)
    return parts[1][:n] if len(parts) > 1 else ''


def tb(S, k, d=None):
    return (S['tblj'] or {}).get(k, d)


def cnt(S, k, d=None):
    return ((S['tblj'] or {}).get('counts') or {}).get(k, d)


def trows(S):
    return (S['tblj'] or {}).get('rows') or []



# ### ### **THESE TWO PATTERNS ARE ASSEMBLED FROM `chr()` ON PURPOSE.** ### Two attempts to
# ### write them as literals were destroyed in transit -- one lost a backslash to a heredoc,
# ### one had its `[^\n]` turned into a real newline that split the string. ### **A PATTERN
# ### ### THAT DOES NOT SURVIVE BEING WRITTEN IS NOT A PATTERN**, and this is the third time
# ### this programme has paid for that (b483, b490, here).
_CALL = r'(?:subprocess\.|os\.system|Popen|check_output)[^' + chr(10) + r']{0,80}'
_Q = '[' + chr(39) + chr(34) + ']'
LAKE_CALL = _CALL + _Q + r'lake' + _Q + r'|lake\s+(?:build|env|exe|update)'
POLL_CALL = _CALL + r'(?:tasklist|taskkill)|import\s+psutil'

COLS = ('repo', 'name', 'pin', 'head', 'statement', 'profile', 'grade', 'refs')

_CALL = r'(?:subprocess\.|os\.system|Popen|check_output)[^' + chr(10) + r']{0,80}'
_Q = '[' + chr(39) + chr(34) + ']'
LAKE_CALL = _CALL + _Q + r'lake' + _Q + r'|lake\s+(?:build|env|exe|update)'
POLL_CALL = _CALL + r'(?:tasklist|taskkill)|import\s+psutil'

def res(S, k, d=None):
    return (S['res'] or {}).get(k, d)


def seg(text, marker, n=300):
    parts = (text or '').split(marker)
    return parts[1][:n] if len(parts) > 1 else ''


def prof(S, n):
    return ((res(S, 'profiles') or {}).get(n) or {}).get('verdict')


NAMES3 = ('EF_lit_zetaZeroConfig', 'EF_lit', 'EF_lit_zeta')
CTRLC = 3221225786

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'paste ends (part 1 of 1)' in S['ferry'] and 'ACT b497' in S['ferry'],
     lambda S: cut(S, 'ferry', 'ACT b497')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE',
     lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-ZERO', 'this act`s banked scan',
     lambda S: '(R81) FLAGS : 0' in S['scan'],
     lambda S: put(S, 'scan', S['scan'].replace('(R81) FLAGS : 0', '(R81) FLAGS : 1'))),
    ('G-STEPZERO-CENSUS', 'two banked censuses',
     lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'fcens', S['fcens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 3'))),
    ('G-STEPZERO-PINS', 'a banked verdict LINE -- the pins tool RUN ALONE',
     lambda S: 'REPOS HARD-FAILING : 0' in line_with(S['pins'], 'REPOS HARD-FAILING'),
     lambda S: put(S, 'pins', S['pins'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-SURVEY-NOMISS', 'the components bank -- both components present',
     lambda S: ('COMPONENT 1 -- THE LOG' in S['comp']
                and 'COMPONENT 2 -- THE THREE PROFILES' in S['comp']),
     lambda S: cut(S, 'comp', 'COMPONENT 2 -- THE THREE PROFILES')),
    ('G-REG-LOCKED-FIRST', 'the face lock block',
     lambda S: 'THE REGISTRATION LOCK' in S['face'],
     lambda S: cut(S, 'face', 'THE REGISTRATION LOCK')),
    ('G-LOCKGATE-EIGHT', 'a banked verdict LINE (A2)',
     lambda S: 'LOCK PERMITTED' in line_with(S['lock'], '**VERDICT : LOCK')
     and 'GATES READ : 8. ### PASSING : 8' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 6'))),
    ('G-SEAL-VERIFIES', 'a banked verdict LINE',
     lambda S: any('LOCKED.' in l or 'SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('LOCKED.', 'x').replace('SEAL INTACT', 'x'))),
    ('G-PRIOR-CLOSED-PUSHED', 'b496`s closing AND the ledger',
     lambda S: ('the commits, each read back by `ls-remote`' in S['prior']
                and S['corr'].count('| 345 |') == 1),
     lambda S: cut(S, 'prior', 'the commits, each read back by `ls-remote`')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: ('ACT b497' in S['ferry'] and 'b497' in S['face']
                and not os.path.exists(os.path.join(D, 'b499_ferry.txt'))),
     lambda S: cut(S, 'face', 'b497')),

    # -------------------------------------------------- component 0
    ('G-PID-CHECKED-NOT-ASSUMED', 'the face -- the pid state is a READING, and the tool is named',
     lambda S: '`tasklist` reports no task matching it' in S['face'],
     lambda S: cut(S, 'face', '`tasklist` reports no task matching it')),
    # ### ### **THIS ARM PASSED ITS OWN POSITIVE CONTROL ON THE FIRST RUN**, because its control
    # ### was a NO-OP and its predicate called `tasklist` directly. ### The world now enters as
    # ### the source `pid_alive`, which the harness can and does falsify.
    ('G-PROCESS-GONE', 'the world, read into a source at suite time',
     lambda S: S['pid_alive'] is False,
     lambda S: put(S, 'pid_alive', True)),
    ('G-PEEK-DECLARED', 'the face -- the read taken BEFORE the seal is declared, not hidden',
     lambda S: ('THIS FACE DECLARES A READ IT ALREADY MADE' in S['face']
                and 'FIRST EIGHT and LAST SIX lines' in S['face']),
     lambda S: cut(S, 'face', 'THIS FACE DECLARES A READ IT ALREADY MADE')),

    # -------------------------------------------------- component 1
    ('G-LOG-COMMITTED-UNCHANGED', 'the log on disk against the digest the components banked',
     lambda S: (res(S, 'sha256') == hashlib.sha256(
         io.open(os.path.join(D, 'b495_ef_build.log'), 'rb').read()).hexdigest()),
     lambda S: put(S, 'res', dict(S['res'], sha256='0' * 64))),
    ('G-LOG-BYTES-MATCH', 'the log`s size on disk against the face and the bank',
     lambda S: res(S, 'bytes') == S['logbytes'] == 27734,
     lambda S: put(S, 'res', dict(S['res'], bytes=1))),
    ('G-EXITS-COUNTED', 'the components bank against the log itself',
     lambda S: len(res(S, 'ends') or []) == S['log'].count('### **END '),
     lambda S: put(S, 'res', dict(S['res'], ends=[]))),
    ('G-NONZERO-COUNTED', 'the components bank -- and the count is not zero',
     lambda S: (res(S, 'nonzero_exits')
                == len([e for e in (res(S, 'ends') or []) if e['exit'] != 0]) == 2),
     lambda S: put(S, 'res', dict(S['res'], nonzero_exits=0))),
    ('G-FAILED-MODULES-BY-NAME', 'the components bank -- NONE, and the log agrees',
     lambda S: res(S, 'failure_lines') == 0 and 'error:' not in S['log'],
     lambda S: put(S, 'res', dict(S['res'], failure_lines=4))),
    ('G-WALL-VS-SUMMED-BOTH', 'the components bank -- BOTH numbers present, neither omitted',
     lambda S: (isinstance(res(S, 'wall_seconds'), float)
                and isinstance(res(S, 'lake_summed'), float)
                and res(S, 'lake_spans') > 0),
     lambda S: put(S, 'res', dict(S['res'], lake_summed=None))),
    ('G-DISTINCT-INSTANTS-COUNTED', 'the components bank against the log`s own stamps',
     lambda S: (res(S, 'distinct_instants')
                == len(set(l[:23] for l in S['log'].split(NL) if l[:4] == '2026'))),
     lambda S: put(S, 'res', dict(S['res'], distinct_instants=1))),
    ('G-B495-N3-CELL-PAID', 'the desk bank -- b495`s owed cell is paid, and said to be',
     lambda S: ('THIS IS THE CELL b495 OWED' in S['desk']
                and 'NOT SCORABLE' in S['desk']),
     lambda S: cut(S, 'desk', 'THIS IS THE CELL b495 OWED')),
    ('G-B495-S2-CELL-PAID', 'the desk bank -- and answered on the log, not on a substitute',
     lambda S: 'NOT ONE ZETA23 MODULE WAS REACHED' in S['desk'],
     lambda S: cut(S, 'desk', 'NOT ONE ZETA23 MODULE WAS REACHED')),

    # -------------------------------------------------- component 2
    ('G-THREE-NAMES-SOUGHT', 'the components tool -- all three names, none dropped',
     lambda S: all(n in S['comptool'] for n in NAMES3)
     and sorted(res(S, 'profiles') or {}) == sorted(NAMES3),
     lambda S: put(S, 'res', dict(S['res'], profiles={NAMES3[0]: {'verdict': 'ABSENT'}}))),
    ('G-WHOLE-AXIOM-STRING', 'the components tool -- the whole string, never a prefix',
     lambda S: ("STD3 = ('propext', 'Classical.choice', 'Quot.sound')" in S['comptool']
                and 'got == STD3' in S['comptool']
                and 'startswith' not in seg(S['comptool'], 'got = tuple', 400)),
     lambda S: cut(S, 'comptool', 'got == STD3')),
    ('G-EACH-PROFILE-CLASSIFIED', 'the components bank -- every name has one of the three words',
     lambda S: all(prof(S, n) in ('STANDARD THREE', 'OTHER', 'ABSENT') for n in NAMES3),
     lambda S: put(S, 'res', dict(S['res'], profiles={
         n: {'verdict': 'PROBABLY FINE'} for n in NAMES3}))),

    # -------------------------------------------------- the stop
    ('G-STOP-OBEYED', 'the components bank -- the stop is PRINTED, not merely taken',
     lambda S: ('STOP. ### COMPONENT 3 IS NOT RUN' in S['comp']
                and res(S, 'all_standard_three') is False),
     lambda S: cut(S, 'comp', 'STOP. ### COMPONENT 3 IS NOT RUN')),
    ('G-COMPONENT3-NOT-RUN-IF-STOPPED', 'the bank AND this act`s own tool list',
     lambda S: (res(S, 'component3_run') is False
                and not os.path.exists(os.path.join(T, 'b497_registry.py'))),
     lambda S: put(S, 'res', dict(S['res'], component3_run=True))),
    ('G-R82-NOT-CLAIMED', 'the components bank -- neither claimed NOR refuted',
     lambda S: ('(R82) IS NOT CLAIMED BY THIS ACT' in S['comp']
                and 'NOR IS (R82) REFUTED' in S['comp']),
     lambda S: cut(S, 'comp', 'NOR IS (R82) REFUTED')),
    ('G-REGISTRY-UNTOUCHED-IF-STOPPED', 'REGISTRY itself -- the row still reads PENDING',
     lambda S: ('**PROFILE: `PENDING`.**' in S['registry']
                and 'EF_lit_zetaZeroConfig' not in S['registry']),
     lambda S: put(S, 'registry', S['registry'].replace(
         '**PROFILE: `PENDING`.**', '**PROFILE:** EF_lit_zetaZeroConfig std3'))),
    ('G-NOCITE-BEFORE-PROFILE', 'REGISTRY -- no terminal of the kernel is named anywhere in it',
     lambda S: not any(n in S['registry'] for n in NAMES3),
     lambda S: put(S, 'registry', S['registry'] + NL + '`EF_lit_zeta` DERIVES')),

    # -------------------------------------------------- the expectations
    ('G-N1-SCORED', 'the desk bank against the components bank',
     lambda S: 'REFUTED' in seg(S['desk'], '**(N1)**') and (S['sc'] or {}).get('n1') is False,
     lambda S: put(S, 'sc', dict(S['sc'], n1=True))),
    ('G-N2-SCORED', 'the desk bank -- and the ABSENT/OTHER distinction it rests on',
     lambda S: ('REFUTED' in seg(S['desk'], '**(N2)**')
                and 'ABSENT IS NOT OTHER' in S['desk']),
     lambda S: cut(S, 'desk', 'ABSENT IS NOT OTHER')),
    ('G-N3-SCORED', 'the desk bank against the counted instants',
     lambda S: ('HELD' in seg(S['desk'], '**(N3)**')
                and (S['sc'] or {}).get('n3') is True
                and res(S, 'distinct_instants') > 50),
     lambda S: put(S, 'sc', dict(S['sc'], n3=False))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk bank -- INCLUDING THE REFUTED ONE',
     lambda S: ("THE SEAT`S OWN EXPECTATIONS" in S['face']
                and 'REGISTERED 3 ; HELD 2 ; REFUTED 1' in S['desk']
                and 'WITH THE SIGN BACKWARDS' in S['desk']),
     lambda S: cut(S, 'desk', 'WITH THE SIGN BACKWARDS')),

    # -------------------------------------------------- the nothings
    ('G-NOTHING-COMPILED', 'every tool of this act, for a BUILD CALL',
     lambda S: not re.search(r'(?:subprocess|os\.system|Popen|check_output|run)\s*\([^)]{0,80}'
                             r'(?:lake|LEAN_PATH)\b|lean\s+--\w|lake\s+build',
                             strip_prose(S['tools497'])),
     lambda S: put(S, 'tools497', S['tools497'] + NL + 'subprocess.run(["lake","build"])')),
    ('G-NOLAKE', 'every tool of this act, for a `lake` INVOCATION and not the word',
     lambda S: not re.search(LAKE_CALL, strip_prose(S['tools497'])),
     lambda S: put(S, 'tools497', S['tools497'] + NL
                   + 'subprocess.run(["lake", "env", "lean", "AxiomCheck.lean"])')),
    ('G-NOTHING-FETCHED', 'every tool of this act, for a network call',
     lambda S: not re.search(r'urllib|requests\.|Invoke-WebRequest|curl |zenodo\.org',
                             strip_prose(S['tools497'])),
     lambda S: put(S, 'tools497', S['tools497'] + NL + 'requests.get("https://zenodo.org/x")')),
    ('G-NOZENODO-WRITE', 'every tool of this act, for a platform WRITE CALL',
     lambda S: not re.search(r'requests\.(?:post|put|patch|delete)\s*\(|'
                             r'zenodo.{0,60}/(?:publish|newversion|files)\b',
                             strip_prose(S['tools497']), re.I),
     lambda S: put(S, 'tools497', S['tools497'] + NL
                   + 'requests.post("https://zenodo.org/api/deposit/1/actions/publish")')),
    ('G-NOGRADE-CONFERRED', 'the face and the components bank',
     lambda S: 'THIS ACT CONFERS NO GRADE' in S['face']
     and 'No corpus grade' not in S['comp'],
     lambda S: cut(S, 'face', 'THIS ACT CONFERS NO GRADE')),
    ('G-NODEPOSIT', 'the deposit directory tracked state',
     lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text',
     lambda S: 'where the deposit left it' in S['ot'],
     lambda S: cut(S, 'ot', 'where the deposit left it')),
    ('G-NOPRIORBANK', 'file times against the face',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text',
     lambda S: 'four lists' in S['ot'] and 'stay OPEN' in S['ot'],
     lambda S: put(S, 'ot', S['ot'].replace('stay OPEN', 'are closed'))),
    ('G-SPAN-BY-TOOL', 'the span tool record',
     lambda S: 'THE CURRENT SPAN' in S['span'],
     lambda S: cut(S, 'span', 'THE CURRENT SPAN')),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- ONE document, REGISTRY untouched',
     lambda S: sorted(S['tracked']) == ['OPEN_TRAILS.md'],
     lambda S: put(S, 'tracked', sorted(S['tracked']) + ['REGISTRY.md'])),
    ('G-CORPUS-LEAN-UNTOUCHED', 'the lv, kernel and explicit-formula trees',
     lambda S: S['corpus_lean_clean'] is True,
     lambda S: put(S, 'corpus_lean_clean', False)),
    ('G-TRAIL-APPEND-ONLY', 'the trail`s own text',
     lambda S: S['ot'].count('### b497 —') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b497 — a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: ('| 346 |' in S['corr'] and S['corr'].count('| 346 |') == 1
                and S['corr'].count('b497, under (R108)') == 1),
     lambda S: put(S, 'corr', S['corr'] + NL + '| 346 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b497 commit in three repositories, against (R91)`s STEM GLOB',
     lambda S: not sorted(k for k in S['kinds']
                          if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face']))),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'b471_someone_elses_bank.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite`s own text',
     lambda S: "log', '--pretty=%H %s'" in S['suite'],
     lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the PLACE-papers file list -- no internal document, no `.lean`',
     lambda S: all(not x.startswith('internal/') and not x.endswith('.lean')
                   for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['internal/BLOB_SENSITIVITY_2026-08-29.md'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the face (G2) block against what runs',
     lambda S: S.get('declared_eq_run', False), lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'the suite`s own text',
     lambda S: 'def line_with(text, needle)' in S['suite'],
     lambda S: cut(S, 'suite', 'def line_with(text, needle)')),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness itself -- the positive control is RUN on every arm',
     lambda S: not live_limb_guard(S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace('defective.append(name)', 'pass'))),
    ('G-MIRROR-TAGGED-BUILD', 'the built zip presence, UNDATED',
     lambda S: S['mirror'], lambda S: put(S, 'mirror', False)),
    ('G-MUSTFAIL', 'a file that must not exist',
     lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked tree -- (R58)',
     lambda S: S['artefacts_tracked'] == '',
     lambda S: put(S, 'artefacts_tracked', 'data/anthropic-zeta23/formal-math/LICENSE')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'the suite`s own text -- b472`s repair, carried',
     lambda S: ("rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                and "log', '-1', '--pretty=%s').startswith('b497')" in S['suite']
                and "data/b497_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b497_components.txt' in gits(ROOT, 'show'")),
]


def regenerate():
    """### ### **(R107): THE GENERATOR IS PART OF THE CLOSING SUITE.**

    ### *"the generator added to the closing suite so every later close regenerates it and diffs
    ### against the prior run"* -- the ruling's own words. ### The suite therefore RE-RUNS
    ### `tools/terminal_table.py` before it scores anything, and the diff it emits is a cell of
    ### this act's record. ### **A TABLE REGENERATED ONLY WHEN SOMEONE REMEMBERS IS A TABLE THAT
    ### ### DRIFTS**, and the whole point of an instrument output is that it cannot.
    """
    r = subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    d = os.path.join(D, 'terminal_table_diff.json')
    diff = json.loads(read(d) or '{}')
    return r.returncode, diff


def main():
    S = sources()
    rc_gen, gen_diff = regenerate()
    g2 = S['face'][S['face'].index('### (G2) THE GATE ARMS.'):S['face'].index('### (W) THE WRITE LIST.')]
    # ### ### **AN ARM THE FACE RETIRES IN WORDS IS NOT AN ARM IT DECLARES.** ### This face's
    # ### (G2) block says `G-NOB475LOG` *"IS NOT CARRIED FORWARD UNDER THAT NAME"* and names its
    # ### replacement. ### A counter that reads only the token disagreed with the sentence beside
    # ### it, and reported an arm declared-but-not-run. ### The face is sealed and correct; the
    # ### COUNTER was wrong, and it now honours the retirement it is reading.
    retired = set(re.findall(r'`(G-[A-Z0-9-]+)` IS NOT CARRIED FORWARD', S['face']))
    declared = sorted(set(x.rstrip('-') for x in
                          re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'} - retired)
    if retired:
        rec('  ### arms the face RETIRES in its own words : %s' % sorted(retired))
    names = [a[0] for a in ARMS]
    pushed = (gits(ROOT, 'rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b497')
              and 'data/b497_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b497 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
        % ('POST-PUSH' if pushed else 'PRE-PUSH'))
    rec('=' * 104)
    rec('  arms in the (G2) block : %d ; run here : %d ; deferred : %d'
        % (len(declared), len(names), len(deferred)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    rec('  %-42s %-5s %-5s %-5s %s' % ('arm', 'LIVE', 'NEG', 'POS', 'verdict'))
    rec('  ' + '-' * 92)
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
        rec('  %-42s %-5s %-5s %-5s %s' % (name, 'PASS' if live else 'FAIL',
                                           'PASS' if neg else '###FAIL', 'FAIL' if not p else '###PASS', v))
        RES.append(name)
        EX.append(dict(name=name, live=live, neg=neg, pos=p, reads=reads))
        if not live:
            fail.append(name)
    for n in deferred:
        rec('  %-42s DEFERRED TO POST-PUSH' % n)
    stray = sorted(k for k in S['kinds']
                   if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face'])))
    rec('')
    rec('  ### files written that NO (W) GLOB COVERS : %d %s' % (len(stray), stray or ''))
    rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
    if gen_diff.get('first_run'):
        rec('  ###   ### **NO PRIOR RUN TO DIFF AGAINST -- THIS CLOSE IS THE FIRST.** ### From')
        rec('  ###   ### the next close the diff is a cell; saying "no change" now would be a')
        rec('  ###   ### reassuring line about nothing.')
    else:
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d'
            % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
               len(gen_diff.get('changed') or [])))
    rec('  ### G-NOPRIORBANK checked %d prior banks. ### ### **0 EXCLUDED BY NAME.**'
        % S['prior_checked'])
    rec('  ### ### **THE b475 LOG EXCEPTION STAYS RETIRED.** ### b481-b489 excused')
    rec('  ###   `b475_zeta23_build.log` as still being appended to by a live process. ### b490')
    rec('  ### found pid 27508 ABSENT at two readings sixty seconds apart and the file cold, and')
    rec('  ### b491 read the log COMPLETE. ### **AN EXCEPTION IS A CLAIM ABOUT THE WORLD AND')
    rec('  ### DECAYS LIKE ONE.** ### b487`s second exclusion is not carried either: it was')
    rec('  ### b485`s bank, which (R97) directed b487 to append to. ### The arm runs at FULL WIDTH.')
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**'
        % (len(RES), len(RES) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**'
        % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    out = os.path.join(D, 'b497_checks_postpush.txt' if pushed else 'b497_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b497_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
