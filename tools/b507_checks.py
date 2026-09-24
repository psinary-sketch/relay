# -*- coding: utf-8 -*-
"""b507_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b506's AND RE-POINTED ARM BY ARM.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, so the harness can hand it a mutated
### source and require it to fail. ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **AND NO ARM HERE READS ONLY THE ACT'S OWN FACE** -- `(R72)`'s second limb.
### ### The harness helpers below `sources()` are b506's, carried verbatim; the ARMS are this act's.
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
FACE = os.path.join(D, 'b507_registration_2026-09-24.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
FIND = os.path.join(PP, 'FINDINGS.md')
DIG = os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')
PRIOR_RELAY = '1b393867'      # ### b506's closing commit -- relay's tip before this act
PRIOR_PP = 'e057a91'          # ### b506's PLACE-papers commit -- its tip before this act
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
MARK1 = 'NOTE APPENDED AT b507 UNDER (R117)(1)'
MARK3 = 'NOTE APPENDED AT b507 UNDER (R117)(3)'
R115 = 'ANNOTATION APPENDED AT b506 UNDER (R115)(1)'
ANNF = ('b477_components.txt', 'b502_components.txt', 'b504_components.txt')
NOTEF = ANNF + ('b334_the_aim_map.txt',)
DMARK = '<!-- b507 orientation refresh: the margin and its control arc -->'
TRAILH = '### b507 —'
CROSS = re.compile(r'(?i)\bwidths?\s+(?:of\s+)?(?:40|81)\b|\b40 and 81\b|\(\s*(?:40|81)\s*,|\ba\s*=\s*(?:40|81)\b')


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


def norm(s):
    s = (s or '').replace('’', '').replace("'", '').replace('`', '').replace('*', '').replace('#', '')
    return re.sub(r'\s+', ' ', s).strip().lower()


def flat(s):
    return (s or '').replace(NL + '### ', ' ').replace(NL, ' ')


def sources():
    import b363_span as SP
    F = SP.folds()
    fold = json.loads(read(os.path.join(D, 'b507_fold.json')) or '{}')
    ft = read(FIND)
    sec = ft[ft.index(fold.get('heading', '\x00')):] if fold.get('heading', '\x00') in ft else ''
    dg = read(DIG)
    ot = read(OT)
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b507_ferry.txt')), ferry8=read(os.path.join(D, 'b508_ferry.txt')),
        scan=read(os.path.join(D, 'b507_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b507_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b507_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b507_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b507_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b506_closing.txt')),
        addendum=read(os.path.join(D, 'b507_addendum.txt')),
        comp=read(os.path.join(D, 'b507_components.txt')),
        desk=read(os.path.join(D, 'b507_desk_notes.txt')),
        span=read(os.path.join(D, 'b507_span_notes.txt')),
        spanj=json.loads(read(os.path.join(D, 'b507_span.json')) or '{}'),
        last_fold=(F[-1]['lo'], F[-1]['hi'], SP.filed_by(F[-1]['hi'])) if F else None,
        fold=fold, sec=sec, ft=ft, dg=dg, ot=ot,
        find_prefix=(open(FIND, 'rb').read().startswith(blob(PP, PRIOR_PP + ':FINDINGS.md'))
                     and open(DIG, 'rb').read().startswith(blob(PP, PRIOR_PP + ':phase2/method/THE_FINDINGS_AS_THEY_STAND.md'))),
        closings={a: read(os.path.join(D, 'b%d_closing.txt' % a)) for a in range(487, 507)},
        notes=json.loads(read(os.path.join(D, 'b507_notes.json')) or '[]'),
        notefiles={n: read(os.path.join(D, n)) for n in NOTEF},
        # ### ### **COMPARED AS GIT WILL STORE IT (b507's own defect, repaired pre-push).** ### The first
        # ### version compared WORKING bytes with the committed BLOB; `b334_the_aim_map.txt`'s working copy is
        # ### CRLF under `eol=lf` (i/lf w/crlf), so a pure append read as a broken prefix. ### The working bytes
        # ### are normalised CRLF -> LF, as the attribute makes git store them, and git's own numstat is the
        # ### second witness: 0 deleted lines in each file.
        notes_prefix_git=all(open(os.path.join(D, n), 'rb').read().replace(bytes([13, 10]), bytes([10])).startswith(
                                 blob(ROOT, PRIOR_RELAY + ':data/' + n))
                             and len(blob(ROOT, PRIOR_RELAY + ':data/' + n)) > 0
                             and gits(ROOT, 'diff', '--numstat', PRIOR_RELAY, '--', 'data/' + n).split(chr(9))[1:2] == ['0']
                             for n in NOTEF),
        fix=json.loads(read(os.path.join(D, 'b507_fixtures.json')) or '{}'),
        regtool=read(os.path.join(T, 'registration_gate.py')), corrtool=read(os.path.join(T, 'corr_row.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL)
                            if x.strip()),
        corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b507_checks.py')),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads', 'mirror-refresh-*-b507.zip'))),
        chain_clean=(gits(ROOT, 'status', '--porcelain', '--', 'tools/b321_window.py', 'tools/e16/carto_atlas.py',
                          'tools/b326_closure.py', 'tools/b325_epstein.py', 'tools/b326_windows.py',
                          'tools/b504_chain.py', 'tools/b506_kernel.py') == ''),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b507 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b507_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.getmtime(os.path.join(D, n)) > os.path.getmtime(FACE)
                       for n in ('b507_fold.json', 'b507_notes.json', 'b507_fixtures.json')
                       if os.path.exists(os.path.join(D, n))) and os.path.exists(os.path.join(D, 'b507_fold.json')),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b507 --'):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-6]_|^b334_', f) and f not in NOTEF]
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

def fold_quotes_ok(S):
    q = (S['fold'] or {}).get('quotes') or []
    return (len(q) == 33 and all(norm(x['quote']) in norm(S['closings'].get(x['act'], '')) for x in q)
            and all(norm(x['quote'].replace('`', "'").replace('|', '/')) in norm(S['sec']) for x in q))


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def statement(S):
    return seg(S['sec'], '### The arc in one statement\n\n', 2000).split('\n')[0]


def corr_row_356(S):
    rows = [l for l in S['corr'].split(NL) if l.startswith('| 356 |')]
    return rows


def b504_line(S):
    lines = S['ot'].split(NL)
    return lines[9776] if len(lines) > 9776 else ''


FORM_A = re.compile(r'^## (.*?), b(\d+)–b(\d+) — THE FOLD\s*$', re.M)

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the two banked ferry files -- the ruling and both parts, each END present',
     lambda S: 'RULING (R117) END' in S['ferry'] and 'FERRY END (part 1 of 2)' in S['ferry'] and 'ACT b507' in S['ferry']
     and 'FERRY END (part 2 of 2)' in S['ferry8'] and 'ACT b508' in S['ferry8'],
     lambda S: cut(S, 'ferry8', 'FERRY END (part 2 of 2)')),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b506`s closing AND the ledger',
     lambda S: 'THE COMMITS, THE MIRROR, THE CENSUSES' in S['prior'] and S['corr'].count('| 355 |') == 1,
     lambda S: put(S, 'corr', S['corr'].replace('| 355 |', '| 3550 |'))),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b507' in S['ferry'] and 'ACT b507' in S['face'] and not os.path.exists(os.path.join(D, 'b508_registration_2026-09-24.txt')),
     lambda S: cut(S, 'face', 'ACT b507')),
    ('G-PEEK-DECLARED', 'the face`s (C) block AND the component records` times against the lock',
     lambda S: 'NO NOTE, NO REPAIR, NO FIXTURE AND NO FOLD WRITE WAS RUN FOR THIS ACT BEFORE THE SEAL' in flat(S['face'])
     and 'UNDER (R70)' in S['face'] and S['after_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R117-ENTERED', 'the banked ferry AND the trail',
     lambda S: 'RULING (R117) END' in S['ferry'] and S['ot'].count('**(R117) ratified.**') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R117) ratified.**', '(R117) noted'))),
    ('G-SPAN-READ-NOT-TYPED', 'the span record against the fold record and the heading written',
     lambda S: (S['fold'].get('span') or {}).get('lo') == S['spanj'].get('span_starts_at') == 487
     and (S['fold'].get('span') or {}).get('hi') == S['spanj'].get('this_act', 0) - 1
     and ('b%d–b%d — THE FOLD' % (S['spanj'].get('span_starts_at', 0), S['spanj'].get('this_act', 0) - 1)) in S['sec'][:200],
     lambda S: put(S, 'fold', dict(S['fold'], span=dict(S['fold'].get('span') or {}, lo=475)))),
    ('G-SPAN-CONFLICT-ENTERED', 'the face, the section and the trail -- the ferry`s b475 entered in all three',
     lambda S: 'b475 THROUGH b506' in S['face'] and '“b475 THROUGH b506”' in S['sec'] and 'navigator chose' in trail(S),
     lambda S: put(S, 'sec', S['sec'].replace('“b475 THROUGH b506”', 'the span'))),
    ('G-FOLD-QUOTES-MATCHED', 'every quote RE-MATCHED in its own closing bank, and each present in the section',
     fold_quotes_ok,
     lambda S: put(S, 'fold', dict(S['fold'], quotes=[dict(q, quote=q['quote'] + ' NOT IN THE BANK') for q in (S['fold'].get('quotes') or [])]))),
    ('G-FOLD-HEADING-SPAN-TOOL', 'the span tool`s own reading of FINDINGS after the write',
     lambda S: S['last_fold'] == (487, 506, 507) and len(FORM_A.findall(S['sec'][:200])) == 1
     and S['ft'].count(S['fold'].get('heading', '\x00')) == 1 and '*Filed by b507' in S['sec'],
     lambda S: put(S, 'last_fold', (475, 479, 486))),
    ('G-FOLD-APPEND-ONLY', 'the fold record AND the committed blobs of b506`s PLACE-papers tip',
     lambda S: len(S['fold'].get('writes') or []) == 2 and all(w['prefix'] and w['bom'] and w['removed'] == 0 for w in S['fold']['writes'])
     and S['find_prefix'],
     lambda S: put(S, 'find_prefix', False)),
    ('G-DIGEST-BLOCK-ONCE', 'the digest -- one block, carrying the section`s own statement verbatim',
     lambda S: S['dg'].count(DMARK) == 1 and len(statement(S)) > 100 and statement(S) in S['dg'][S['dg'].find(DMARK):],
     lambda S: put(S, 'dg', S['dg'] + NL + DMARK)),
    ('G-NO-CROSSING-WIDTH', 'every text this act wrote -- section, digest block, trail record, notes, face',
     lambda S: not any(CROSS.search(t) for t in (S['sec'], S['dg'][S['dg'].find(DMARK):], seg(S['ot'], TRAILH, 99999), S['face'],
                                                 *[v[v.find('NOTE APPENDED AT b507'):] for v in S['notefiles'].values()])),
     lambda S: put(S, 'sec', S['sec'] + ' the crossings at widths 40 and 81')),
    ('G-NOTES-R117-1', 'the three components files -- ONE b507 note each, after b506`s, saying the derived kernel closes',
     lambda S: all(S['notefiles'][n].count(MARK1) == 1 and S['notefiles'][n].count(R115) == 1
                   and S['notefiles'][n].index(MARK1) > S['notefiles'][n].index(R115)
                   and 'CLOSES ON THE BANK COMPLETED AT b506 -- 93 OF 93' in S['notefiles'][n][S['notefiles'][n].index(MARK1):]
                   for n in ANNF),
     lambda S: put(S, 'notefiles', dict(S['notefiles'], **{'b502_components.txt': S['notefiles']['b502_components.txt'].replace('93 OF 93', 'ALL')}))),
    ('G-NOTE-R117-3', 'b334`s aim map -- its crossings text preserved and ONE note after it',
     lambda S: S['notefiles']['b334_the_aim_map.txt'].count(MARK3) == 1
     and 'THE EPSTEIN CROSSING REGION' in S['notefiles']['b334_the_aim_map.txt'][:S['notefiles']['b334_the_aim_map.txt'].index(MARK3)]
     and 'ARE UNVERIFIED' in S['notefiles']['b334_the_aim_map.txt'][S['notefiles']['b334_the_aim_map.txt'].index(MARK3):],
     lambda S: put(S, 'notefiles', dict(S['notefiles'], **{'b334_the_aim_map.txt': S['notefiles']['b334_the_aim_map.txt'].replace('ARE UNVERIFIED', 'stand')}))),
    ('G-NOTES-PREFIX', 'the notes record AND relay`s committed blobs at b506`s close -- four files, each prefix proved',
     lambda S: len(S['notes']) == 4 and all(n.get('prefix') is True and n.get('removed') == 0 and n.get('marks') == 1 for n in S['notes'])
     and S['notes_prefix_git'],
     lambda S: put(S, 'notes', [dict(n, prefix=False) for n in S['notes']])),
    ('G-B504-TRAIL-CORRECTED', 'the trail -- b504`s line unedited, and this act`s record correcting it by address',
     lambda S: 'near 1e-7' in b504_line(S) and 'OPEN_TRAILS.md:9777' in trail(S) and 'about 1e-6' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('about 1e-6', 'about 1e-7'))),
    ('G-GATE-GE-REPAIRED', 'the gate`s source AND the fixture record, both polarities, b505`s bar the positive control',
     lambda S: '<=|≤|>=|≥|(?<![-=])>)' in S['regtool'] and S['fix'].get('ok') is True
     and all(r['ok'] for r in S['fix'].get('bar_floor') or [{'ok': False}]) and S['fix'].get('bar_floor_discriminates') is True
     and (S['fix'].get('bar_floor') or [{}])[0].get('new_fires') is True,
     lambda S: cut(S, 'regtool', '|>=|≥|(?<![-=])>')),
    ('G-CORR-VALIDATE-FIRST', 'the writer`s source (the split BEFORE the write) AND the fixture record',
     lambda S: 0 <= S['corrtool'].find('would = [c for c in row.strip().strip(') < S['corrtool'].find("open(path + '.tmp', 'wb')")
     and (S['fix'].get('corr_row') or {}).get('pipe_code') == 2 and (S['fix'].get('corr_row') or {}).get('pipe_file_unchanged') is True
     and (S['fix'].get('corr_row') or {}).get('clean_code') == 0 and (S['fix'].get('corr_row') or {}).get('carried_self_test') is True,
     lambda S: put(S, 'fix', dict(S['fix'], corr_row=dict(S['fix'].get('corr_row') or {}, pipe_file_unchanged=False)))),
    ('G-CORR-ROW-LIVE', 'the ledger -- row 356, written by the repaired writer, six cells as it landed',
     lambda S: len(corr_row_356(S)) == 1 and len(corr_row_356(S)[0].strip().strip('|').split('|')) == 6
     and '(b507, under (R117))' in corr_row_356(S)[0],
     lambda S: put(S, 'corr', S['corr'].replace('| 356 | **THE MARGIN', '| 356 | a | b | **THE MARGIN'))),
    ('G-INSTRUMENTS-EDITED-TWO', 'relay`s tools against b506`s close -- exactly the two (R117) names modified',
     lambda S: S['tools_edited'] == ['corr_row.py', 'registration_gate.py'],
     lambda S: put(S, 'tools_edited', S['tools_edited'] + ['b321_window.py'])),
    ('G-NO-EXPECTATIONS', 'the face AND the desk -- none registered, none scored',
     lambda S: not re.search(r'\*\*\((?:N|S)\d\)\*\*', S['face']) and 'REGISTERED 0. ### THE SEAT`S : REGISTERED 0.' in S['desk'],
     lambda S: put(S, 'desk', S['desk'].replace('REGISTERED 0.', 'REGISTERED 3.'))),
    ('G-NOGRADE-CONFERRED', 'the face AND the section', lambda S: 'THIS ACT CONFERS NO GRADE' in S['face']
     and 'no grade is conferred by a seat' in S['sec'],
     lambda S: put(S, 'sec', S['sec'].replace('no grade is conferred by a seat', ''))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record',
     lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b507 -'))),
    ('G-NOPRIORBANK', 'file times against the face, the four noted files excepted by name',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record',
     lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('stay OPEN', 'are closed'))),
    ('G-LANE-SHUT', 'the trail`s own record -- the instrument lane shut, said',
     lambda S: 'The instrument lane shuts at this act' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(NL, ' ').replace('The instrument lane shuts at this act', 'the lane stays open'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the three documents; no chain file edited',
     lambda S: sorted(S['tracked']) == ['FINDINGS.md', 'OPEN_TRAILS.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md']
     and S['chain_clean'] is True, lambda S: put(S, 'chain_clean', False)),
    ('G-TRAIL-APPEND-ONLY', 'the trail`s own text', lambda S: S['ot'].count(TRAILH) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + TRAILH + ' a second record')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: S['corr'].count('| 356 |') == 1 and S['corr'].count('(b507, under (R117))') == 1,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 356 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b507 commit in three repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b507')" in S['suite']
                and "data/b507_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b507_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b507')
              and 'data/b507_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b507 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    rec('  ### G-NOPRIORBANK checked %d prior banks. ### ### **4 EXCLUDED BY NAME** -- the files the notes append to, held by G-NOTES-PREFIX against 1b393867.'
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
    out = os.path.join(D, 'b507_checks_postpush.txt' if pushed else 'b507_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b507_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
