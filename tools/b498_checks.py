# -*- coding: utf-8 -*-
"""b498_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
FACE = os.path.join(D, 'b498_registration_2026-09-23.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
NL = chr(10)
BT = chr(96)
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
        face=read(FACE), ferry=read(os.path.join(D, 'b498_ferry.txt')),
        scan=read(os.path.join(D, 'b498_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b498_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b498_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b498_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b498_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b497_closing.txt')),
        addendum=read(os.path.join(D, 'b498_addendum.txt')),
        comp=read(os.path.join(D, 'b498_components.txt')),
        desk=read(os.path.join(D, 'b498_desk_notes.txt')),
        span=read(os.path.join(D, 'b498_span_notes2.txt'))
        + read(os.path.join(D, 'b498_span_notes.txt')),
        res=json.loads(read(os.path.join(D, 'b498_results.json')) or '{}'),
        sc=json.loads(read(os.path.join(D, 'b498_scores.json')) or '{}'),
        b495log=read(os.path.join(D, 'b495_ef_build.log')),
        b495push=read(os.path.join(T, 'b495_push.py')),
        cacheraw=read(os.path.join(D, 'b498_cache_get.txt')),
        closureraw=read(os.path.join(D, 'b498_closure_build.txt')),
        launchsrc=read(os.path.join(T, 'b498_launch.py')),
        # ### ### **THE WORLD IS READ INTO A SOURCE SO THE HARNESS CAN MUTATE IT** (b497`s lesson).
        vendored_live=sum(1 for dp, _, fs in os.walk(os.path.join(KERNEL, 'Zeta23'))
                          for f in fs if f.endswith('.lean')),
        kernel_clean=(gits(KERNEL, 'status', '--porcelain') == ''),
        log_tracked=gits(ROOT, 'ls-files', 'data/b498_ef_build.log', 'data/b498_printaxioms.lean'),
        errata_clean=(gits(PP, 'status', '--porcelain', '--', 'ERRATA.md') == ''),
        tblj=json.loads(read(os.path.join(D, 'terminal_table.json')) or '{}'),
        registry=read(os.path.join(PP, 'REGISTRY.md')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b498_checks.py')),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads',
                                           'mirror-refresh-*-b498.zip'))),
        tools498=''.join(read(os.path.join(T, f)) for f in sorted(os.listdir(T))
                         if f.startswith('b498_') and f.endswith('.py')
                         and f not in ('b498_checks.py', 'b498_launch.py')),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b498 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b498_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b498 --'):
                k |= set(os.path.basename(x) for x in
                         gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
        # ### ### **A FILE DIRTY BEFORE THIS ACT BEGAN WAS NOT WRITTEN BY IT** (b497, carried).
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
    S['kinds'] = k
    LIVE = set()
    prior = [f for f in os.listdir(D)
             if re.match(r'^b4[0-8][0-9]_|^b49[0-7]_', f) and f not in LIVE]
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
    """### (R85) as (R91) amends it: THE FACE'S (W) SECTION AS A LIST OF GLOBS.

    ### ### **THE CORPUS WRITES A POSSESSIVE WITH A BACKTICK** -- `this act`s record`, `b496`s
    ### face`, `(R108)`s first line` -- a convention adopted so that ground strings survive being
    ### written into Python. ### ### **EVERY SUCH POSSESSIVE MAKES THE BACKTICK COUNT ODD**, and a
    ### naive `` `([^`]+)` `` pairing then DESYNCHRONISES: it pairs the closing backtick of one
    ### path with the possessive of the next sentence and returns a multi-line blob of prose as
    ### though it were a glob.
    ### ### **MEASURED ACROSS THE LAST FIVE FACES: b493 EVEN (0 malformed), b494 EVEN (0), b495
    ### ### ODD (5 malformed), b496 ODD (4), b497 ODD (6).** ### So `G-WRITELIST-KINDS` has been
    ### reading a partly-garbled glob list for three acts, and at b497 it reported a file
    ### UNDECLARED that the face declares by name in its own (W).
    ### ### **THE REPAIR IS TO PAIR WITHIN A LINE AND TO KEEP ONLY WHAT LOOKS LIKE A PATH.**
    ### A glob has no spaces and no newlines; a possessive's neighbourhood has both.
    ### ### **THIS WIDENS NOTHING.** ### It lets the tool read declarations that were already
    ### written; a file the face does not name is still uncovered.
    """
    w = face[face.index('### (W) THE WRITE LIST'):face.index('### (Z) THE NOTHINGS')]
    out = []
    for line in w.split(NL):
        for g in re.findall(BT + '([^' + BT + NL + ']+)' + BT, line):
            g = g.strip()
            if not g or ' ' in g or len(g) > 120:
                continue          # ### prose, not a path
            if not re.match(r'^[A-Za-z0-9_./*?\[\]{}-]+$', g):
                continue
            out.append(g.split('/')[-1])
    return out


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




def c(S, n):
    return (S['res'] or {}).get(n) or {}


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 14).split('.')[0]


def word_of(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def b495_ends(S):
    out = []
    for l in S['b495log'].split(NL):
        m = re.search(r'### \*\*END (.+?)\*\* : EXIT (-?\d+)', l)
        if l[:4] == '2026' and m:
            out.append((l[:23], int(m.group(2))))
    return out


def fetch_line_ok(S):
    f = c(S, 'c2').get('fetched')
    ln = c(S, 'c2').get('fetched_line') or ''
    if f is None:
        return False
    if f == 0 and 'No files to download' in S['cacheraw']:
        return True
    digits = re.findall(r'[\d,]+', ln)
    return bool(ln) and ln in S['cacheraw'] and any(d.replace(',', '') == str(f) for d in digits)


NAMES3 = ('EF_lit_zetaZeroConfig', 'EF_lit', 'EF_lit_zeta')

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry',
     lambda S: 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b498' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
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
    ('G-REG-LOCKED-FIRST', 'the face lock block',
     lambda S: 'THE REGISTRATION LOCK' in S['face'],
     lambda S: cut(S, 'face', 'THE REGISTRATION LOCK')),
    ('G-LOCKGATE-EIGHT', 'a banked verdict LINE (A2)',
     lambda S: 'LOCK PERMITTED' in line_with(S['lock'], '**VERDICT : LOCK')
     and 'GATES READ : 8. ### PASSING : 8' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 6'))),
    ('G-SEAL-VERIFIES', 'a banked verdict LINE',
     lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('SEAL INTACT', 'x'))),
    ('G-PRIOR-CLOSED-PUSHED', 'b497`s closing AND the ledger',
     lambda S: ('the commits, each read back by `ls-remote`' in S['prior']
                and S['corr'].count('| 346 |') == 1),
     lambda S: cut(S, 'prior', 'the commits, each read back by `ls-remote`')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes',
     lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: ('ACT b498' in S['ferry'] and 'ACT b498' in S['face']
                and not os.path.exists(os.path.join(D, 'b499_ferry.txt'))),
     lambda S: cut(S, 'face', 'ACT b498')),
    ('G-PEEK-DECLARED', 'the face -- the reads taken BEFORE the seal are declared, not hidden',
     lambda S: ('THIS FACE DECLARES READS IT ALREADY MADE' in S['face']
                and 'FIRST TWELVE and LAST EIGHT lines' in S['face']),
     lambda S: cut(S, 'face', 'THIS FACE DECLARES READS IT ALREADY MADE')),
    ('G-R109-ENTERED', 'the banked ferry AND the trail',
     lambda S: 'RULING (R109) END' in S['ferry'] and S['ot'].count('**(R109) ratified.**') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R109) ratified.**', '(R109) noted'))),

    # -------------------------------------------------- component 1
    ('G-B495-FLAGS-READ', 'the components bank against b495`s own code',
     lambda S: (c(S, 'c1').get('new_group') is True and c(S, 'c1').get('detached') is True
                and (c(S, 'c1').get('flags_line') or '#') in S['b495push']),
     lambda S: put(S, 'res', dict(S['res'], c1=dict(c(S, 'c1'), detached=False)))),
    ('G-KILL-INSTANTS-READ', 'the components bank against the b495 log itself',
     lambda S: ([(e['t'], e['exit']) for e in c(S, 'c1').get('ends') or []] == b495_ends(S)
                and len(b495_ends(S)) == 2),
     lambda S: put(S, 'res', dict(S['res'], c1=dict(c(S, 'c1'), ends=[])))),
    ('G-TURN-END-READ', 'the components bank -- the turn end read and the interval printed',
     lambda S: (bool(c(S, 'c1').get('turn_end'))
                and 0 <= (c(S, 'c1').get('kill_after_turn_end_s') or -1) < 60
                and 'THE SEAT`S b495 TURN ENDS' in S['comp']),
     lambda S: put(S, 'res', dict(S['res'], c1=dict(c(S, 'c1'), turn_end=None)))),
    ('G-BOTH-CLOCKS', 'the components bank -- 15:02 read in both clocks',
     lambda S: '15:02 read as LOCAL' in S['comp'] and '15:02 read as UTC' in S['comp'],
     lambda S: cut(S, 'comp', '15:02 read as UTC')),
    ('G-LAUNCHER-SURVIVED', 'the components bank against the log`s last line',
     lambda S: (c(S, 'c1').get('launcher_survived') is True
                and 'BUILD EXIT' in [l for l in S['b495log'].split(NL) if l.strip()][-1]),
     lambda S: put(S, 'res', dict(S['res'], c1=dict(c(S, 'c1'), launcher_survived=False)))),
    ('G-SENDER-NOT-GUESSED', 'the components bank -- NOT ESTABLISHED, in the cell and the prose',
     lambda S: (c(S, 'c1').get('sender') == 'NOT ESTABLISHED'
                and 'THE SENDER STAYS NOT ESTABLISHED' in S['comp']),
     lambda S: put(S, 'res', dict(S['res'], c1=dict(c(S, 'c1'), sender='a window was closed')))),

    # -------------------------------------------------- component 2
    ('G-CACHE-GET-RUN', 'the cache tool`s own output, banked whole',
     lambda S: 'cache_exit' in c(S, 'c2') and len(S['cacheraw'].strip()) > 0,
     lambda S: put(S, 'cacheraw', '')),
    ('G-CACHE-EXIT-PRINTED', 'the components bank -- the exit printed as the bank records it',
     lambda S: ('**EXIT : %s**' % c(S, 'c2').get('cache_exit')) in S['comp'],
     lambda S: put(S, 'res', dict(S['res'], c2=dict(c(S, 'c2'), cache_exit=-99)))),
    ('G-FETCH-COUNT-FROM-LINE', 'the count against the tool`s own line in the raw output',
     lambda S: fetch_line_ok(S),
     lambda S: put(S, 'res', dict(S['res'], c2=dict(c(S, 'c2'), fetched=987654321)))),
    ('G-CLOSURE-COMPUTED', 'the bank against the kernel`s own files, counted now',
     lambda S: (len(c(S, 'c2').get('closure_roots') or []) > 0
                and c(S, 'c2').get('vendored') == S['vendored_live'] == 57),
     lambda S: put(S, 'vendored_live', 1)),
    ('G-CLOSURE-TIMED', 'the components bank -- a wall time, or the fallback`s b475 line',
     lambda S: ((c(S, 'c2').get('closure_run') is True
                 and isinstance(c(S, 'c2').get('closure_wall'), float)
                 and len(S['closureraw']) > 0)
                or (c(S, 'c2').get('closure_run') is False
                    and 'RUN COMPLETE' in (c(S, 'c2').get('b475_line') or ''))),
     lambda S: put(S, 'res', dict(S['res'], c2=dict(c(S, 'c2'), closure_run=None)))),
    ('G-COMPILED-COUNTED', 'the bank against the closure build`s own output',
     lambda S: ((c(S, 'c2').get('closure_run') is not True)
                or c(S, 'c2').get('built_mathlib')
                == len(re.findall(r'\bBuilt Mathlib\.', S['closureraw']))),
     lambda S: put(S, 'res', dict(S['res'], c2=dict(c(S, 'c2'), closure_run=True, built_mathlib=-1)))),
    ('G-FALLBACK-OBEYED', 'the bank -- the closure ran iff the cache was available',
     lambda S: (isinstance(c(S, 'c2').get('cache_available'), bool)
                and c(S, 'c2').get('closure_run') is c(S, 'c2').get('cache_available')),
     lambda S: put(S, 'res', dict(S['res'], c2=dict(
         c(S, 'c2'), closure_run=not c(S, 'c2').get('cache_available'))))),
    ('G-KERNEL-TREE-CLEAN', 'the world, read into a source at suite time, AND the bank',
     lambda S: S['kernel_clean'] is True and c(S, 'c2').get('kernel_status') == '',
     lambda S: put(S, 'kernel_clean', False)),

    # -------------------------------------------------- component 3
    ('G-LAUNCH-NEW-GROUP', 'the launch cell -- the flag`s own bit',
     lambda S: bool((c(S, 'c3').get('flags') or 0) & 0x200),
     lambda S: put(S, 'res', dict(S['res'], c3=dict(c(S, 'c3'), flags=0x10)))),
    ('G-LAUNCH-NEW-CONSOLE', 'the launch cell -- the flag`s own bit',
     lambda S: bool((c(S, 'c3').get('flags') or 0) & 0x10),
     lambda S: put(S, 'res', dict(S['res'], c3=dict(c(S, 'c3'), flags=0x200)))),
    ('G-LAUNCH-NOT-DETACHED-FLAG', 'the launch cell -- b495`s flag NOT carried',
     lambda S: 'flags' in c(S, 'c3') and not (c(S, 'c3')['flags'] & 0x8),
     lambda S: put(S, 'res', dict(S['res'], c3=dict(c(S, 'c3'), flags=0x208)))),
    ('G-PID-PRINTED', 'the components bank against the launch cell',
     lambda S: bool(c(S, 'c3').get('pid')) and ('**pid : %s**' % c(S, 'c3').get('pid')) in S['comp'],
     lambda S: put(S, 'res', dict(S['res'], c3=dict(c(S, 'c3'), pid=0)))),
    ('G-LOG-PATH-PRINTED', 'the components bank',
     lambda S: '**log : data/b498_ef_build.log**' in S['comp'],
     lambda S: cut(S, 'comp', '**log : data/b498_ef_build.log**')),
    ('G-INSTANT-AT-MARK', 'the launcher`s own code -- the clock read inside stamp(), called per line',
     lambda S: ('time.time()' in seg(S['launchsrc'], 'def stamp():', 300)
                and 'stamp()' in seg(S['launchsrc'], 'def say(fh, s):', 80)),
     lambda S: put(S, 'launchsrc', S['launchsrc'].replace("line = '%s  %s' % (stamp(), s)",
                                                         "line = '%s  %s' % (T0, s)"))),
    ('G-THREE-NAMES-PROBED', 'the launcher`s own code',
     lambda S: all(n in S['launchsrc'] for n in ('Zeta23.WeilEF.EF_lit_zetaZeroConfig',
                                                 'Zeta23.EF.EF_lit', 'Zeta23.WeilEF.EF_lit_zeta')),
     lambda S: cut(S, 'launchsrc', 'Zeta23.EF.EF_lit')),
    ('G-LOG-NOT-READ', 'every tool of this act but the launcher, for a READ of the launch log',
     lambda S: (not any(('open(' in l or 'read(' in l)
                        for l in strip_prose(S['tools498']).split(NL) if 'b498_ef_build' in l)
                and not re.search(r'(?:open|read)\(\s*log\b', strip_prose(S['tools498']))),
     lambda S: put(S, 'tools498', S['tools498'] + NL + "x = read(os.path.join(D, 'b498_ef_build.log'))")),
    ('G-LOG-NOT-COMMITTED', 'relay`s tracked tree',
     lambda S: S['log_tracked'] == '',
     lambda S: put(S, 'log_tracked', 'data/b498_ef_build.log')),
    ('G-NOTHREADS-SET', 'the launcher`s own code -- no environment written for the child',
     lambda S: not re.search(r'environ\[[^]]*LEAN_NUM_THREADS[^]]*\]\s*=|\benv\s*=',
                             strip_prose(S['launchsrc'])),
     lambda S: put(S, 'launchsrc', S['launchsrc'] + NL + "os.environ['LEAN_NUM_THREADS'] = '2'")),

    # -------------------------------------------------- the expectations
    ('G-N1-SCORED', 'the desk bank against the scores',
     lambda S: 'n1' in (S['sc'] or {}) and desk_word(S, 'N1') == word_of(S['sc']['n1']),
     # ### ### **THE FIRST CONTROL SET n1 TO 'x', WHICH IS TRUTHY, SO `word_of` STILL SAID HELD AND
     # ### THE ARM PASSED ITS OWN POSITIVE CONTROL.** ### The control now FLIPS the score.
     lambda S: put(S, 'sc', dict(S['sc'], n1=not (S['sc'] or {}).get('n1')))),
    ('G-N2-SCORED', 'the desk bank against the scores -- REPLAYED IS NOT COMPILED said',
     lambda S: ('n2' in (S['sc'] or {}) and desk_word(S, 'N2') == word_of(S['sc']['n2'])
                and ('REPLAYED IS NOT COMPILED' in S['desk'] or S['sc']['n2'] is None)),
     lambda S: put(S, 'sc', dict(S['sc'], n2=not (S['sc'] or {}).get('n2')))),
    ('G-N3-SCORED', 'the desk bank against the launch cell',
     lambda S: ('n3' in (S['sc'] or {}) and desk_word(S, 'N3') == word_of(S['sc']['n3'])
                and S['sc']['n3'] == bool((c(S, 'c3').get('flags') or 0) & 0x200)),
     lambda S: put(S, 'sc', dict(S['sc'], n3='x'))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk bank',
     lambda S: ("THE SEAT`S OWN EXPECTATIONS" in S['face']
                and 'REGISTERED 3 ;' in S['desk']
                and all(desk_word(S, t) for t in ('S1', 'S2', 'S3'))),
     lambda S: cut(S, 'desk', 'REGISTERED 3 ;')),

    # -------------------------------------------------- the nothings
    ('G-NOZENODO-WRITE', 'every tool of this act, for a platform WRITE CALL',
     lambda S: not re.search(r'requests\.(?:post|put|patch|delete)\s*\(|'
                             r'zenodo.{0,60}/(?:publish|newversion|files|edit)\b',
                             strip_prose(S['tools498'] + S['launchsrc']), re.I),
     lambda S: put(S, 'tools498', S['tools498'] + NL
                   + 'requests.post("https://zenodo.org/api/deposit/1/actions/publish")')),
    ('G-NOERRATA', 'ERRATA.md`s tracked state and the PLACE-papers file list',
     lambda S: S['errata_clean'] is True and 'ERRATA.md' not in S['tracked'],
     lambda S: put(S, 'errata_clean', False)),
    ('G-NOGRADE-CONFERRED', 'the face',
     lambda S: 'THIS ACT CONFERS NO GRADE' in S['face'],
     lambda S: cut(S, 'face', 'THIS ACT CONFERS NO GRADE')),
    ('G-NOCITE-BEFORE-PROFILE', 'REGISTRY -- no terminal of the kernel is named anywhere in it',
     lambda S: not any(n in S['registry'] for n in NAMES3),
     lambda S: put(S, 'registry', S['registry'] + NL + '`EF_lit_zeta` DERIVES')),
    ('G-NODEPOSIT', 'the deposit directory tracked state',
     lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record',
     lambda S: 'where the deposit left it' in seg(S['ot'], '### b498 —', 99999),
     lambda S: put(S, 'ot', S['ot'].replace('### b498 —', '### b498 -'))),
    ('G-NOPRIORBANK', 'file times against the face',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record',
     lambda S: 'the four lists stay OPEN' in seg(S['ot'], '### b498 —', 99999),
     lambda S: put(S, 'ot', S['ot'].replace('stay OPEN', 'are closed'))),
    ('G-SPAN-BY-TOOL', 'the span tool record',
     lambda S: 'THE CURRENT SPAN' in S['span'],
     lambda S: cut(S, 'span', 'THE CURRENT SPAN')),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- ONE document',
     lambda S: sorted(S['tracked']) == ['OPEN_TRAILS.md'],
     lambda S: put(S, 'tracked', sorted(S['tracked']) + ['REGISTRY.md'])),
    ('G-TRAIL-APPEND-ONLY', 'the trail`s own text',
     lambda S: S['ot'].count('### b498 —') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b498 — a second record that must not exist')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: (S['corr'].count('| 347 |') == 1 and S['corr'].count('b498, under (R109)') == 1),
     lambda S: put(S, 'corr', S['corr'] + NL + '| 347 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b498 commit in three repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b498')" in S['suite']
                and "data/b498_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b498_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b498')
              and 'data/b498_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b498 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b498_checks_postpush.txt' if pushed else 'b498_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b498_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
