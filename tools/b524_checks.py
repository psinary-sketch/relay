# -*- coding: utf-8 -*-
"""b524_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b523's AND RE-POINTED ARM BY ARM.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb.
### ### The kernel arms read the kernel's own tree and git state, and Lean's own output in the run files.
"""
import io
import glob
import hashlib
import fnmatch
import json
import math
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
FACE = os.path.join(D, 'b524_registration_2026-09-25.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'fd975837'      # ### b523's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = 'ffc09da'           # ### the kernel's tip, untouched by this act
PRIOR_PP = '9538a41'           # ### b523's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b524 —'
GRADE_RE = re.compile(r'\b(DERIVES|INTERFACES|SHELL|ENCODES-CONCLUSION|ENCODES)\b')
G0 = dict(xi=14.1347, q=16.290216)
WIT = 'the window is the witness construction h2_sign_imp_rh names, exhibited at one rho'


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


def blob(repo, spec):
    return subprocess.run(['git', '-C', repo, 'show', spec], capture_output=True).stdout


def flat(s):
    return (s or '').replace(NL + '### ', ' ').replace(NL, ' ')


def jsonl(p):
    return [json.loads(l) for l in read(p).split(NL) if l.strip()]


def sources():
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b524_ferry.txt')),
        scan=read(os.path.join(D, 'b524_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b524_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b524_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b524_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b524_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b523_closing.txt')),
        addendum=read(os.path.join(D, 'b524_addendum.txt')),
        comp=read(os.path.join(D, 'b524_components.txt')),
        desk=read(os.path.join(D, 'b524_desk_notes.txt')),
        report=read(os.path.join(D, 'b524_report.txt')),
        mod=read(os.path.join(KER, 'SIDEExplicitFormula', 'TwoPropertyWindow.lean')),
        acc=read(os.path.join(KER, 'AxiomCheckWindow.lean')),
        att=json.loads(read(os.path.join(D, 'b524_attempts.json')) or '[]'),
        att_files={int(re.search(r'attempt(\d+)\.lean$', p).group(1)): hashlib.sha256(open(p, 'rb').read()).hexdigest()
                   for p in glob.glob(os.path.join(D, 'b524_attempt[0-9]*.lean')) if re.search(r'attempt(\d+)\.lean$', p)},
        att0=read(os.path.join(D, 'b524_attempt0_stopped_by_host.txt')),
        clogs=len(glob.glob(os.path.join(D, 'b524_compile_log*.txt'))),
        clast=read(sorted(glob.glob(os.path.join(D, 'b524_compile_log*.txt')), key=os.path.getmtime)[-1]),
        plog=read(sorted(glob.glob(os.path.join(D, 'b524_profile_log*.txt')), key=os.path.getmtime)[-1]),
        inst=json.loads(read(os.path.join(D, 'b524_install.json')) or '{}'),
        prof=json.loads(read(os.path.join(D, 'b524_profile.json')) or '{}'),
        rd=json.loads(read(os.path.join(D, 'b524_read.json')) or '{}'),
        stmt=read(os.path.join(D, 'b524_statement.txt')),
        r134=read(os.path.join(D, 'b524_ferry_R134.txt')),
        ker_changed=set(x for x in gits(KER, 'diff', '--name-only', 'ffc09da').split(NL) if x.strip())
                    | set(p[3:].strip() for p in git(KER, 'status', '--porcelain').split(NL) if p.strip()),
        ker_tags=gits(KER, 'tag', '--points-at', 'HEAD'),
        res=json.loads(read(os.path.join(D, 'b524_results.json')) or '{}'),
        sc=json.loads(read(os.path.join(D, 'b524_scores.json')) or '{}'),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b524_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads', 'mirror-refresh-*-b524.zip'))),
        chain_clean=(gits(ROOT, 'status', '--porcelain', '--', 'tools/b321_window.py', 'tools/e16/carto_atlas.py',
                          'tools/b326_closure.py', 'tools/b325_epstein.py', 'tools/b326_windows.py',
                          'tools/b504_chain.py', 'tools/b506_kernel.py', 'tools/b511_families.py', 'tools/b503_zero.py', 'tools/b514_window.py', 'tools/b515_window.py', 'tools/b518_window.py', 'tools/b519_window.py', 'tools/b520_widen.py', 'tools/b521_tail.py', 'tools/b522_reach.py') == ''),
        ker_clean=(gits(KER, 'rev-parse', '--short=7', 'HEAD') == KER_TIP and gits(KER, 'status', '--porcelain', '--untracked-files=no') == ''),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b524 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b524_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b524_install.json', 'b524_attempts.json', 'b524_profile.json', 'b524_read.json'))),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b524 --'):
                k |= set(os.path.basename(x) for x in
                         gits(repo, 'show', '--name-only', '--pretty=format:', l.split()[0]).split(NL) if x.strip())
        for l in git(repo, 'status', '--porcelain').split(NL):
            if l.strip() and not l.lstrip().startswith('??'):
                rel = l[3:].strip()
                try:
                    if os.path.getmtime(os.path.join(repo, rel)) < os.path.getmtime(FACE):
                        continue
                except OSError:
                    pass
                k.add(os.path.basename(rel))
    S['kinds'] = k
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-9]_|^b52[0-3]_|^b334_', f)]
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








def c2(S, k, d=None):
    return (S['c2'] or {}).get(k, d)


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 14).split('.')[0]


def word_of(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def c2_closed(S):
    f = c2(S, 'found') or []
    return (c2(S, 'not_near') == 0 and all(c2(S, 'control') or [False]) and all(z.get('inside') for z in f)
            and all(z.get('rho') and z.get('route_a', 1) < 1e-10 for z in f) and abs(c2(S, 'whole', 0) - c2(S, 'total', -9)) < 0.05)


def least_nv(L):
    nv = 8193
    while 2 * math.pi * (nv - 1) / L <= 350.0:
        nv += 1
    return nv


def population(S):
    return [c for c in S['cells'] if c['tail_inside']]


def log_span(log):
    ts = re.findall(r'^\[(\d{4}-\d\d-\d\d \d\d:\d\d:\d\d)\]', log, re.M)
    if not ts:
        return None
    import datetime
    f = lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
    return (f(ts[-1]) - f(ts[0])).total_seconds()


def edge_secs(log):
    m = re.findall(r'edges 1051 / 1051  (\d+) s', log)
    return int(m[-1]) if m else -1


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


VACUOUS_ARMS = ()
NS = 'SIDEExplicitFormula.B321.'
STD3 = "'%s' depends on axioms: [propext, Classical.choice, Quot.sound]"
THMS = ['kWin_classK', 'paperFT_window_zero', 'paperFT_window', 'paperFT_second_order', 'ibp_step', 'weilTest_ofReal_even',
        'plateau_contDiff', 'plateau_even', 'plateau_hasCompactSupport', 'plateau_eq_one']
GRADED = ['kWin_classK', 'paperFT_window_zero', 'paperFT_window']
NEWK = {'SIDEExplicitFormula/TwoPropertyWindow.lean', 'AxiomCheckWindow.lean'}
ALLOWED_I = {'cosWin_contDiff', 'window_contDiff', 'windowC_contDiff', 'cosWin_hasCompactSupport', 'window_hasCompactSupport',
             'windowC_hasCompactSupport'}


def heads(mod):
    return [mod[m.start():mod.index(':=', m.start()) + 2] for m in re.finditer(r'^theorem \S+', mod, re.M)]


def body(mod, name):
    m = re.search(r'^theorem %s\b[\s\S]*?(?=\n\n|\Z)' % re.escape(name), mod, re.M)
    return m.group(0) if m else ''


def refs_i(S):
    b = body(S['mod'], 'kWin_classK').split(':=', 1)[-1]
    names = re.findall(r'^theorem (\S+)', S['mod'], re.M)
    return {n for n in names if n != 'kWin_classK' and re.search(r'\b%s\b' % re.escape(n), b)}


def vrefs(mod):
    code = re.sub(r'/-[\s\S]*?-/', ' ', mod)
    code = NL.join(l for l in code.split(NL) if not l.startswith('import '))
    code = re.sub(r'--[^\n]*', ' ', code)
    return sorted(set(re.findall(r'\bZeta23\.[A-Za-z_][A-Za-z0-9_.]*', code)))


def first_clean(S):
    ok = [a['attempt'] for a in S['att'] if a['exit'] == 0 and a['errors'] == 0 and not a['sorry']]
    return ok[0] if ok else None


def quoted(S):
    rec = S['ot'][S['ot'].index(TRAILH):]
    return [l[2:] for l in rec.split(NL) if l.startswith('> ')]


def earlier(S):
    pre = S['ot'][:S['ot'].index(TRAILH)]
    i = pre.index('### b522 —')
    return set(pre[i:].split(NL))


def xi_form(r134):
    i = r134.index('"positive for xi')
    j = r134.index('numerical."', i) + len('numerical."')
    return ' '.join(r134[i:j].split())


def table_row(S, n):
    return next((l for l in S['table'].split(NL) if '`%s%s`' % (NS, n) in l), '')


def corr_row(S):
    return next((l for l in S['corr'].split(NL) if l.startswith('| 373 |')), '')


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R133) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b524' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-ZERO', 'this act`s banked scan', lambda S: '(R81) FLAGS : 0' in S['scan'],
     lambda S: put(S, 'scan', S['scan'].replace('(R81) FLAGS : 0', '(R81) FLAGS : 1'))),
    ('G-STEPZERO-CENSUS', 'two banked censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'fcens', S['fcens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 3'))),
    ('G-STEPZERO-PINS', 'a banked verdict LINE -- the pins tool RUN ALONE',
     lambda S: 'REPOS HARD-FAILING : 0' in line_with(S['pins'], 'REPOS HARD-FAILING'),
     lambda S: put(S, 'pins', S['pins'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-REG-LOCKED-FIRST', 'the face lock block', lambda S: 'THE REGISTRATION LOCK' in S['face'],
     lambda S: cut(S, 'face', 'THE REGISTRATION LOCK')),
    ('G-LOCKGATE-EIGHT', 'a banked verdict LINE (A2)',
     lambda S: 'LOCK PERMITTED' in line_with(S['lock'], '**VERDICT : LOCK') and 'GATES READ : 8. ### PASSING : 8' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 6'))),
    ('G-SEAL-VERIFIES', 'a banked verdict LINE', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)),
     lambda S: put(S, 'seal', S['seal'].replace('SEAL INTACT', 'x'))),
    ('G-PRIOR-CLOSED-PUSHED', 'b523`s closing AND the ledger',
     lambda S: 'THE COMMITS, THE MIRROR, THE CENSUSES' in S['prior'] and S['corr'].count('| 372 |') == 1,
     lambda S: put(S, 'corr', S['corr'].replace('| 372 |', '| 3720 |'))),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b524' in S['ferry'] and 'ACT b524' in S['face'] and not glob.glob(os.path.join(D, 'b525_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b524')),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b524 -'))),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('stay OPEN', 'are closed'))),
    ('G-TRAIL-APPEND-ONLY', 'the trail`s own text', lambda S: S['ot'].count(TRAILH) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + TRAILH + ' a second record')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger -- row 373 once, six cells as it landed',
     lambda S: S['corr'].count('| 373 |') == 1 and S['corr'].count('(b524, under (R133) and (R134))') == 1
     and len(corr_row(S).strip().strip('|').split('|')) == 6,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 373 | a duplicate row |')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b523`s close -- none modified',
     lambda S: S['tools_edited'] == [], lambda S: put(S, 'tools_edited', ['b519_window.py'])),
    ('G-WRITELIST-KINDS', 'every b524 commit in four repositories, against (R91)`s STEM GLOB',
     lambda S: not sorted(k for k in S['kinds'] if not any(fnmatch.fnmatch(k, g) for g in globs_of(S['face']))),
     lambda S: put(S, 'kinds', set(S['kinds']) | {'b471_someone_elses_bank.txt'})),
    ('G-WRITELIST-SPANS-ACT', 'the suite`s own text', lambda S: "log', '--pretty=%H %s'" in S['suite'],
     lambda S: cut(S, 'suite', "log', '--pretty=%H %s'")),
    ('G-NOSTAGE-A-BY-DIFF', 'the PLACE-papers file list -- no internal document, no `.lean`',
     lambda S: all(not x.startswith('internal/') and not x.endswith('.lean') for x in S['tracked']),
     lambda S: put(S, 'tracked', list(S['tracked']) + ['internal/BLOB_SENSITIVITY_2026-08-29.md'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the face (G2) block against what runs',
     lambda S: S.get('declared_eq_run', False), lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-SUBSTRING-VERDICT', 'the suite`s own text', lambda S: 'def line_with(text, needle)' in S['suite'],
     lambda S: cut(S, 'suite', 'def line_with(text, needle)')),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness itself -- the positive control is RUN on every arm',
     lambda S: not live_limb_guard(S['suite']), lambda S: put(S, 'suite', S['suite'].replace('defective.append(name)', 'pass'))),
    ('G-MIRROR-TAGGED-BUILD', 'the built zip presence, UNDATED', lambda S: S['mirror'], lambda S: put(S, 'mirror', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked tree -- (R58)', lambda S: S['artefacts_tracked'] == '',
     lambda S: put(S, 'artefacts_tracked', 'data/anthropic-zeta23/formal-math/LICENSE')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'the suite`s own text -- b472`s repair, carried',
     lambda S: ("rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                and "log', '-1', '--pretty=%s').startswith('b524')" in S['suite']
                and "data/b524_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b524_components.txt' in gits(ROOT, 'show'")),
    ('G-PEEK-DECLARED', 'the face`s (C) block AND the component files` times against the lock',
     lambda S: 'no Lean process was started in this act before the seal' in flat(S['face']) and S['after_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R133-ENTERED', 'the two banked rulings AND the trail -- (R133) and (R134) each ratified once',
     lambda S: 'RULING (R133) END' in S['ferry'] and 'RULING (R134) END' in S['r134'] and S['ot'].count('**(R133) ratified') == 1
     and '**(R134) ratified, in this act:**' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**(R133) ratified', '(R133) noted'))),
    ('G-INSTALLED-FROM-DRAFT', 'the install bank against attempt 1`s banked source -- the sealed draft is what first ran',
     lambda S: S['inst']['TwoPropertyWindow.lean']['draft_sha'] == S['inst']['TwoPropertyWindow.lean']['installed_sha']
     == S['att'][0]['source_sha'] == S['att_files'].get(1),
     lambda S: put(S, 'inst', {**S['inst'], 'TwoPropertyWindow.lean': dict(S['inst']['TwoPropertyWindow.lean'], draft_sha='0' * 64)})),
    ('G-ATTEMPTS-BANKED', 'the attempts bank against the banked sources and logs; attempt 0 recorded STOPPED BY HOST',
     lambda S: [a['attempt'] for a in S['att']] == list(range(1, len(S['att']) + 1)) == sorted(S['att_files'])
     and all(S['att_files'][a['attempt']] == a['source_sha'] for a in S['att']) and S['clogs'] == len(S['att'])
     and 'STOPPED BY HOST' in S['att0'],
     lambda S: put(S, 'att', S['att'][:-1])),
    ('G-MODULE-NO-SORRY', 'the module text, the last compile log and the profile log',
     lambda S: bool(S['mod']) and not re.search(r'\bsorry\b', S['mod']) and 'exit 0 ;' in S['clast'] and ': error' not in S['clast']
     and 'sorryAx' not in S['plog'],
     lambda S: put(S, 'mod', S['mod'] + NL + 'theorem x : False := sorry')),
    ('G-PROFILE-WHOLE-STRING', 'the profile run file -- each theorem`s line equal to the standard-three string',
     lambda S: all([l.strip() for l in S['plog'].split(NL) if l.startswith("'%s%s'" % (NS, n))] == [STD3 % (NS + n)] for n in THMS)
     and all((S['prof'].get('std3') or {}).get(NS + n) is True for n in THMS),
     lambda S: put(S, 'plog', S['plog'].replace(STD3 % (NS + 'kWin_classK'), (STD3 % (NS + 'kWin_classK')).replace(', Quot.sound', ', sorryAx')))),
    ('G-STATEMENTS-PRINTED', 'the banked statements against the module -- each theorem from its line to its `:=`, recomputed',
     lambda S: bool(re.findall(r'^theorem ', S['mod'], re.M)) and all(h in S['stmt'] for h in heads(S['mod'])),
     lambda S: put(S, 'stmt', S['stmt'].replace('theorem kWin_classK', 'theorem ghost'))),
    ('G-PLATEAU-DIVERGENCE-SAID', 'the module`s docstring AND the trail -- the ramp is the smooth bump, not the B-spline',
     lambda S: "ITS RAMP IS MATHLIB'S SMOOTH BUMP" in S['mod'] and "not the numerical instrument's B-spline" in trail(S),
     lambda S: cut(S, 'mod', "ITS RAMP IS MATHLIB'S SMOOTH BUMP")),
    ('G-PROP-NOT-PROVED', 'the module`s text -- f_pair_hypothesis a def of type Prop, and no theorem states it',
     lambda S: 'def f_pair_hypothesis' in S['mod'] and re.search(r'def f_pair_hypothesis[^\n]*\)\s*:\s*Prop\s*:=', S['mod'])
     and not any('f_pair_hypothesis' in h for h in heads(S['mod'])),
     lambda S: put(S, 'mod', S['mod'] + NL + NL + 'theorem cheat : f_pair_hypothesis 0 id 0 := by' + NL + '  sorry')),
    ('G-GROWTH-BY-INTEGRAL', 'Lean`s own #check and #print in the profile run',
     lambda S: (S['prof'].get('check_prop') or '').split(NL)[0].rstrip().endswith('Prop') and '∫' in (S['prof'].get('print_growth') or '')
     and 'Real.cosh' in (S['prof'].get('print_growth') or '') and 'Real.exp' not in (S['prof'].get('print_growth') or ''),
     lambda S: put(S, 'prof', dict(S['prof'], print_growth='fun φ δ => Real.exp (δ * L)'))),
    ('G-REMAINING-LEMMAS-NAMED', 'the module`s docstring -- (f)(ii)-(iv) by the fold`s names, (R133)(4)`s two ingredients beside (f)(iii)',
     lambda S: all(x in S['mod'] for x in ('(f)(ii)  = (f2)', '(f)(iii) = (f3)', '(f)(iv)  = (f4)', 'closed strip 0 <= beta <= 1',
                                         'Zeta23.RvM.zetaZeroConfig_local_count')),
     lambda S: cut(S, 'mod', '(f)(iii) = (f3)')),
    ('G-REFS-RESOLVED', 'the module`s Zeta23 names, each resolved in the vendored tree by the read bank',
     lambda S: sorted(r['name'] for r in S['rd'].get('refs', [])) == vrefs(S['mod']) and all(r['resolved'] for r in S['rd'].get('refs', [])),
     lambda S: put(S, 'rd', dict(S['rd'], refs=[dict(r, resolved=[]) for r in S['rd'].get('refs', [])]))),
    ('G-STEP9-NOTE-QUOTED', 'the trail -- every quoted line a line of b522`s or b523`s record as it stands',
     lambda S: len(quoted(S)) >= 5 and all(q_ in earlier(S) for q_ in quoted(S)) and 'NO BANK at `OPEN_TRAILS.md:9270`' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('> **COMPONENT 5 — 24 of b522', '> **COMPONENT 5 — 25 of b522'))),
    ('G-XI-FORM-OF-WORDS', 'the trail against (R134)`s pasted form -- the corrected form entered, W-ORD-XI-P7 filed',
     lambda S: xi_form(S['r134']) in trail(S) and 'W-ORD-XI-P7' in trail(S) and 'CORRECTED' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('at ramp order 5, where', 'where'))),
    ('G-GRADES-BY-READ', 'the row, the profile and the trail -- DERIVES beside each of (i)-(iii), each std3',
     lambda S: all(('`%s` DERIVES' % n) in corr_row(S) and (S['prof'].get('std3') or {}).get(NS + n) is True for n in GRADED)
     and 'Grades by statement-read: (i) DERIVES, (ii) DERIVES, (iii) DERIVES.' in trail(S),
     lambda S: put(S, 'corr', S['corr'].replace('`kWin_classK` DERIVES', '`kWin_classK` SHELL'))),
    ('G-TABLE-ROW', 'the regenerated terminal table -- a row per graded theorem, DERIVES, PROFILED',
     lambda S: all(table_row(S, n) and 'DERIVES' in table_row(S, n) and 'NOT PROFILED' not in table_row(S, n)
                   and 'theorem %s' % n in table_row(S, n) for n in GRADED),
     lambda S: put(S, 'table', S['table'].replace('`%skWin_classK`' % NS, '`ghost`'))),
    ('G-NOGRADE-CONFERRED', 'this act`s trail record and row -- grade words only the three DERIVES of (i)-(iii)',
     lambda S: GRADE_RE.findall(trail(S)) == ['DERIVES'] * 3 and GRADE_RE.findall(corr_row(S)) == ['DERIVES'] * 3,
     lambda S: put(S, 'ot', S['ot'] + ' `x_y_z` SHELL')),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the trail alone; no chain file edited; the kernel`s changes the two new files',
     lambda S: sorted(S['tracked']) == ['OPEN_TRAILS.md'] and S['chain_clean'] is True and S['ker_changed'] == NEWK
     and S['ker_tags'] == '',
     lambda S: put(S, 'ker_changed', NEWK | {'Zeta23/Defs.lean'})),
    ('G-LANE-SHUT', 'the trail`s own record -- the kernel lane shut, said', lambda S: 'kernel lane shuts at this act' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(NL, ' ').replace('kernel lane shuts at this act', 'lane stays open'))),
    ('G-N1-SCORED', 'the desk against the attempts and the profile', lambda S: 'n1' in S['sc'] and desk_word(S, 'N1') == word_of(S['sc']['n1'])
     and S['sc']['n1'] == (first_clean(S) is not None and first_clean(S) <= 2
                           and all((S['prof'].get('std3') or {}).get(NS + n) is True for n in ('paperFT_window', 'paperFT_window_zero'))),
     lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against (i)`s proof in the module', lambda S: 'n2' in S['sc'] and desk_word(S, 'N2') == word_of(S['sc']['n2'])
     and S['sc']['n2'] == (refs_i(S) <= ALLOWED_I), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the read bank', lambda S: 'n3' in S['sc'] and desk_word(S, 'N3') == word_of(S['sc']['n3'])
     and S['sc']['n3'] == (S['rd'].get('lemmas_beyond_b513') == []), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against Lean`s #check and #print', lambda S: 'n4' in S['sc'] and desk_word(S, 'N4') == word_of(S['sc']['n4'])
     and S['sc']['n4'] == ((S['prof'].get('check_prop') or '').split(NL)[0].rstrip().endswith('Prop')
                           and '∫' in (S['prof'].get('print_growth') or '') and 'Real.exp' not in (S['prof'].get('print_growth') or '')),
     lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk']
     and desk_word(S, 'S1') == word_of(first_clean(S) is not None and first_clean(S) <= 4
                                       and all((S['prof'].get('std3') or {}).get(NS + n) is True for n in THMS))
     and desk_word(S, 'S2') == word_of(not (refs_i(S) <= ALLOWED_I))
     and desk_word(S, 'S3') == word_of(S['rd'].get('lemmas_beyond_b513') != []),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
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
    # ### ### **THE TABLE IS READ AFTER IT IS REGENERATED (b512's own defect, repaired post-push).** ### `sources()`
    # ### read `terminal_table.md` BEFORE `regenerate()` rewrote it, so `G-TABLE-ROW` scored the previous close's
    # ### table; the first post-push run is banked as `b512_checks_postpush_first.txt`.
    S['table'] = read(os.path.join(D, 'terminal_table.md'))
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b524')
              and 'data/b524_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b524 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    rec('  ### G-PRIORBANK-UNCHANGED checked %d prior banks by time, none excepted.'
        % S['prior_checked'])
    rec('  ### ### **VACUOUS ON THE LIVE SOURCE (NO Q0 CELL READ) : %s.** ### each refused its injected defective cell.'
        % ([a for a in VACUOUS_ARMS] or 'NONE'))
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
    out = os.path.join(D, 'b524_checks_postpush.txt' if pushed else 'b524_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b524_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
