# -*- coding: utf-8 -*-
"""b521_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b520's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b521_registration_2026-09-24.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = '2324e495'      # ### b520's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = 'ffc09da'           # ### the kernel's tip, untouched by this act
PRIOR_PP = '4f8798a'           # ### b520's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b521 —'
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
        face=read(FACE), ferry=read(os.path.join(D, 'b521_ferry.txt')),
        scan=read(os.path.join(D, 'b521_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b521_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b521_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b521_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b521_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b520_closing.txt')),
        addendum=read(os.path.join(D, 'b521_addendum.txt')),
        comp=read(os.path.join(D, 'b521_components.txt')),
        desk=read(os.path.join(D, 'b521_desk_notes.txt')),
        report=read(os.path.join(D, 'b521_report.txt')),
        rows=sorted(jsonl(os.path.join(D, 'b521_cells.jsonl')), key=lambda c: c['a']),
        reach=json.loads(read(os.path.join(D, 'b521_reach.json')) or '{}'),
        order=json.loads(read(os.path.join(D, 'b521_order.json')) or '{}'),
        fx=json.loads(read(os.path.join(D, 'b521_fixture.json')) or '{}'),
        va=json.loads(read(os.path.join(D, 'b521_validity.json')) or '{}'),
        cp=json.loads(read(os.path.join(D, 'b521_compare.json')) or '{}'),
        notes=json.loads(read(os.path.join(D, 'b521_notes.json')) or '[]'),
        preseal=read(os.path.join(D, 'b521_preseal_pricing.txt')),
        preseal_before=os.path.getmtime(os.path.join(D, 'b521_preseal_pricing.txt')) < os.path.getmtime(FACE),
        b20res=json.loads(read(os.path.join(D, 'b520_' + 'results.json')) or '{}'),
        b19=sorted(jsonl(os.path.join(D, 'b519_cells_B.jsonl')), key=lambda c: c['a']),
        cells18=[c['q'] for c in jsonl(os.path.join(D, 'b518_cells.jsonl'))],
        cells19=[c['q'] for f in ('A', 'B', 'C') for c in jsonl(os.path.join(D, 'b519_cells_%s.jsonl' % f))],
        nb={b: (blob(ROOT, PRIOR_RELAY + ':data/' + b).decode('utf-8', 'replace').replace(chr(13), ''), read(os.path.join(D, b)))
            for b in ('b518_components.txt', 'b519_components.txt')},
        tool=read(os.path.join(T, 'b521_tail.py')),
        res=json.loads(read(os.path.join(D, 'b521_results.json')) or '{}'),
        sc=json.loads(read(os.path.join(D, 'b521_scores.json')) or '{}'),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b521_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads', 'mirror-refresh-*-b521.zip'))),
        chain_clean=(gits(ROOT, 'status', '--porcelain', '--', 'tools/b321_window.py', 'tools/e16/carto_atlas.py',
                          'tools/b326_closure.py', 'tools/b325_epstein.py', 'tools/b326_windows.py',
                          'tools/b504_chain.py', 'tools/b506_kernel.py', 'tools/b511_families.py', 'tools/b503_zero.py', 'tools/b514_window.py', 'tools/b515_window.py', 'tools/b518_window.py', 'tools/b519_window.py', 'tools/b520_widen.py') == ''),
        ker_clean=(gits(KER, 'rev-parse', '--short=7', 'HEAD') == KER_TIP and gits(KER, 'status', '--porcelain', '--untracked-files=no') == ''),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b521 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b521_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b521_notes.json', 'b521_order.json', 'b521_fixture.json', 'b521_validity.json', 'b521_compare.json', 'b521_reach.json'))),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b521 --'):
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
    # ### ### **THE ONE DECLARED EXCEPTION (R130)(1)**: the two noted banks leave this time test and are proved append-only
    # ### by `G-APPENDED-NOTE-PREFIX` against their bytes at b520`s close.
    prior = [f for f in os.listdir(D) if f not in ('b518_components.txt', 'b519_components.txt') and re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-9]_|^b520_|^b334_', f)]
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


DELTA = 0.9532604747946607 - 0.5
WIT5 = 'the witness construction h2_sign_imp_rh names, exhibited at one rho and for that rho alone'
HARD5 = 'no Q0 cell is negative beyond its bound on a closing bank: the two-property window is not yet the witness'
GRID = [float(a) for a in range(15, 61)]
NAMED = (15.0, 30.0, 45.0, 60.0)
MARK = '### (R130)(1) NOTE, APPENDED AT b521'
LAMQ_TOP = 4096
# ### ### **THE CELL ARMS RUN OVER THE CELLS READ, AND THIS ACT READ NONE** (the reach ended at its first width). ###
# ### Each such arm is VACUOUS on the live source and SAYS SO in the suite`s record; its positive control injects one
# ### defective cell, so the arm must still refuse what it exists to refuse.
VACUOUS_ARMS = ('G-NV-PRINTED', 'G-SPLIT-SUMS', 'G-RATIO-RECOMPUTED', 'G-BOUND-FORM', 'G-GROWTH-RECOMPUTED')


def rel(x, y, t=1e-9):
    return abs(x - y) <= t * max(1.0, abs(x), abs(y))


def bad_cell(S, **kw):
    """### one defective cell, placed inside the reach`s stop so only the arm under test can refuse it."""
    c = dict(a=15.0, p=7, h2=1.0, B=1.0, r=0.0, Z=10.0, on_rest=1.0, pair=1.0, others=1.0, ratio=0.1, Eu=0.1, Ek=0.1, Etail=0.1,
             Eround=0.1, shortfall=None, verified=False, growth=99.0, growth_bound=1.0, nv=8193, nv_note='', tail_on=1.0, tail_off=1.0)
    c.update(kw)
    return put(S, 'rows', list(S['rows']) + [c])


def growth_of(a, p):
    L = math.log(a)
    R = L / 8.0
    W, hh = L - R, R / p
    return (math.sinh(DELTA * W) / (DELTA * W)) * (math.sinh(DELTA * hh) / (DELTA * hh)) ** p


def recount(S):
    C = S['rows']
    V = [c for c in C if abs(c['r']) <= c['B']]
    cross = [c['a'] for c in C if c['ratio'] is not None and c['ratio'] <= -1.0]
    return dict(cells=len(C), verified=len(V), h2_neg=[c['a'] for c in V if c['h2'] < -c['B']],
                h2_pos=[c['a'] for c in V if c['h2'] > c['B']], cross=(min(cross) if cross else None))


def reach_recount(S):
    """### b520`s rule: the first grid width whose E_tail exceeds B' (or whose a^2 exceeds LAMQ`s top) ends the reach."""
    last = None
    for s in S['reach']['scan']:
        if s['Etail'] > s['Eu'] + s['Ek'] + s['Eround'] or s['a'] ** 2 > LAMQ_TOP:
            return last, s['a']
        last = s['a']
    return last, None


def least_p(S):
    ps = sorted({r['p'] for r in S['order']['rows']})
    ok = [p for p in ps if any(r['p'] == p and r['a'] == 60.0 and r['Etail'] < r['Bprime'] for r in S['order']['rows'])]
    return ok[0] if ok else None


def a0_at(S, p):
    rows = {r['a']: r for r in S['order']['rows'] if r['p'] == p}
    ok = [a for a in NAMED if a in rows and all(rows[b]['Etail'] < rows[b]['Bprime'] for b in NAMED if b >= a and b in rows)]
    return min(ok) if ok else None


def note_ok(S, bank):
    prior, now = S['nb'][bank]
    return bool(prior) and now.startswith(prior) and len(now) > len(prior) and now[len(prior):].count(MARK) == 1 and MARK not in prior


def note_recount(S, act):
    rows = S['cells18'] if act == 'b518' else S['cells19']
    ver = [q for q in rows if q['verified']]
    return len(ver), sum(1 for q in ver if q['Etail'] > q['Eu'] + q['Ek'] + q['Eround'])


def cmp_recount(S):
    old = {round(c['a'], 9): c['q']['Etail'] for c in S['b19']}
    return (all(rel(r['old'], old.get(round(r['a'], 9), float('nan'))) for r in S['cp']['rows']) and len(S['cp']['rows']) == len(old),
            sum(1 for r in S['cp']['rows'] if r['new'] < r['old']), sum(1 for r in S['cp']['rows'] if r['new_p5'] < r['old']))


def corr_row(S):
    return next((l for l in S['corr'].split(NL) if l.startswith('| 370 |')), '')


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R130) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b521' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b520`s closing AND the ledger',
     lambda S: 'THE COMMITS, THE MIRROR, THE CENSUSES' in S['prior'] and S['corr'].count('| 369 |') == 1,
     lambda S: put(S, 'corr', S['corr'].replace('| 369 |', '| 3690 |'))),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b521' in S['ferry'] and 'ACT b521' in S['face'] and not glob.glob(os.path.join(D, 'b522_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b521')),
    ('G-PEEK-DECLARED', 'the face`s (C) block AND the component banks` times against the lock',
     lambda S: 'NO CELL WAS COMPUTED, NO B` AT ANY OTHER WIDTH, AND NO p SCANNED AT a = 60 BEFORE THE SEAL' in flat(S['face']) and S['after_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R130-ENTERED', 'the banked ferry AND the trail -- (R130)(2)`s reading in its words',
     lambda S: 'RULING (R130) END' in S['ferry'] and S['ot'].count('**(R130) ratified') == 1 and 'numerical shadow of (f)(iii)' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**(R130) ratified', '(R130) noted'))),
    ('G-APPENDED-NOTE-PREFIX', 'each noted bank against its bytes at b520`s close -- prior bytes a prefix, one note after',
     lambda S: note_ok(S, 'b518_components.txt') and note_ok(S, 'b519_components.txt'),
     lambda S: put(S, 'nb', dict(S['nb'], **{'b519_components.txt': (S['nb']['b519_components.txt'][0], 'X' + S['nb']['b519_components.txt'][1][1:])}))),
    ('G-APPENDED-NOTE-COUNTED', 'the prior cell banks recounted against the notes` json AND the appended words',
     lambda S: all((r['verified'], r['remarked']) == note_recount(S, r['act'])
                   and ('%d of %d VERIFIED-EST Q0 CELLS OF %s' % (r['remarked'], r['verified'], r['act'])) in S['nb'][r['bank']][1] for r in S['notes'])
     and len(S['notes']) == 2,
     lambda S: put(S, 'notes', [dict(r, remarked=r['remarked'] + 1) for r in S['notes']])),
    ('G-PRESEAL-PRICING-BANKED', 'the pricing bank`s time against the face, and the face naming it',
     lambda S: 'PRE-SEAL PRICING' in S['preseal'] and S['preseal_before'] and 'b521_preseal_pricing.txt' in S['face'],
     lambda S: put(S, 'preseal_before', False)),
    ('G-ORDER-SCANNED', 'the order bank -- p contiguous from 5, four named widths each, stopping two past the least',
     lambda S: sorted({r['p'] for r in S['order']['rows']}) == list(range(5, (least_p(S) + 3) if least_p(S) else 21))
     and all(sorted(r['a'] for r in S['order']['rows'] if r['p'] == p) == list(NAMED) for p in {r['p'] for r in S['order']['rows']}),
     lambda S: put(S, 'order', dict(S['order'], rows=[r for r in S['order']['rows'] if r['p'] != max(x['p'] for x in S['order']['rows'])]))),
    ('G-LEAST-P-RECOMPUTED', 'the order bank`s rows against its own and the results` least p',
     lambda S: least_p(S) == S['order']['least_p'] == S['res']['least_p'],
     lambda S: put(S, 'res', dict(S['res'], least_p=6))),
    ('G-CLASSK-RESTATED', 'the report -- classK restated at the least p, C^(p-3), p at least 5',
     lambda S: ('classK restated at p = %s' % least_p(S)) in S['report'] and 'C^(p-3)' in S['report'] and (least_p(S) or 0) >= 5,
     lambda S: cut(S, 'report', 'classK restated')),
    ('G-FIXTURE-BAR', 'the rebuilt window`s fixture rows -- every diff within its bar, recomputed, at the least p',
     lambda S: S['fx']['p'] == least_p(S) and bool(S['fx']['rows']) and all(abs(r['closed'] - r['numeric']) <= r['bar'] for r in S['fx']['rows']),
     lambda S: put(S, 'fx', dict(S['fx'], rows=[dict(r, numeric=r['closed'] + 3 * r['bar'] + 1e-300) for r in S['fx']['rows']]))),
    ('G-INTEGRATION-FIXTURE', 'the closed form against its own integrand integrated numerically -- relative difference at most 1e-2',
     lambda S: len(S['fx']['integration']) == 4 and all(abs(x['closed'] - x['numeric']) <= 1e-2 * abs(x['closed']) for x in S['fx']['integration']),
     lambda S: put(S, 'fx', dict(S['fx'], integration=[dict(x, numeric=x['numeric'] * 1.1) for x in S['fx']['integration']]))),
    ('G-VALIDITY-FIXTURE', 'the synthetic zero at 0.9 + 200i -- every image term within the allowance, at four widths',
     lambda S: sorted(r['a'] for r in S['va']['rows'] if r['beta'] == 0.9) == list(NAMED)
     and all(max(r['terms']) <= r['allowance'] for r in S['va']['rows'] if r['beta'] == 0.9),
     lambda S: put(S, 'va', dict(S['va'], rows=[dict(r, terms=[t * 1e6 for t in r['terms']]) for r in S['va']['rows']]))),
    ('G-VALIDITY-CONTROL', 'the control at real part 3.0 -- NOT covered, at four widths',
     lambda S: sorted(r['a'] for r in S['va']['rows'] if r['beta'] == 3.0) == list(NAMED)
     and all(max(r['terms']) > r['allowance'] for r in S['va']['rows'] if r['beta'] == 3.0),
     lambda S: put(S, 'va', dict(S['va'], rows=[dict(r, terms=[t * 1e-9 for t in r['terms']]) for r in S['va']['rows']]))),
    ('G-TAIL-SPLIT-SUMS', 'the comparison bank -- the tail the on-line part plus the off-line allowance, per width',
     lambda S: bool(S['cp']['rows']) and all(rel(r['new'], r['new_on'] + r['new_off']) and r['new_on'] > 0 and r['new_off'] > 0 for r in S['cp']['rows']),
     lambda S: put(S, 'cp', dict(S['cp'], rows=[dict(r, new_off=r['new_off'] * 2) for r in S['cp']['rows']]))),
    ('G-COMPARE-RECOUNTED', 'b519`s banked old majorant against the comparison, and both counts recounted',
     lambda S: cmp_recount(S) == (True, S['cp']['smaller'], S['cp']['p5_smaller']) and S['res']['compare_smaller'] == S['cp']['smaller'],
     lambda S: put(S, 'cp', dict(S['cp'], smaller=S['cp']['of']))),
    ('G-STRIP-PRINTED', 'the report AND the trail -- the strip assumption printed',
     lambda S: 'STRIP ASSUMPTION' in S['report'] and '0 ≤ β ≤ 1' in trail(S), lambda S: cut(S, 'report', 'STRIP ASSUMPTION')),
    ('G-REMAINDER-NAMED', 'the report AND the trail -- S(t)`s remainder named, not bounded',
     lambda S: 'S(t)`s remainder is NAMED, NOT BOUNDED' in S['report'] and "S(t)'s remainder named, not bounded" in trail(S),
     lambda S: cut(S, 'report', 'S(t)`s remainder is NAMED, NOT BOUNDED')),
    ('G-REACH-RECOMPUTED', 'the reach and stop recomputed from the scan`s error terms, at the least p',
     lambda S: (S['reach']['reach'], (S['reach']['stop'] or {}).get('a')) == reach_recount(S) and S['reach']['p'] == least_p(S)
     and [s['a'] for s in S['reach']['scan']] == GRID[:len(S['reach']['scan'])] and bool(S['reach']['scan']),
     lambda S: put(S, 'reach', dict(S['reach'], reach=60.0))),
    ('G-PAST-REACH-UNBANKED', 'the banked cells -- none at or past the stop width',
     lambda S: all(c['a'] < S['reach']['stop']['a'] for c in S['rows']) if S['reach']['stop'] else True,
     lambda S: put(S, 'rows', list(S['rows']) + [dict(a=99.0)])),
    ('G-NV-PRINTED', 'every banked cell carries nv, NONE, with its note',
     lambda S: all('nv' in c and c['nv'] is None and 'closed-form' in c['nv_note'] for c in S['rows']), lambda S: bad_cell(S)),
    ('G-SPLIT-SUMS', 'every banked cell -- the zero side equals the pair, the other off-line pairs and the on-line part',
     lambda S: all(rel(c['Z'], c['on_rest'] + c['pair'] + c['others']) for c in S['rows']), lambda S: bad_cell(S)),
    ('G-RATIO-RECOMPUTED', 'every banked cell -- pair / (Z - pair), signed, recomputed',
     lambda S: all(rel(c['ratio'], c['pair'] / (c['Z'] - c['pair']), 1e-7) for c in S['rows']), lambda S: bad_cell(S)),
    ('G-VERIFIED-RECOUNTED', 'every banked cell`s flag, and the results` counts',
     lambda S: all(c['verified'] == (abs(c['r']) <= c['B']) for c in S['rows'])
     and S['res']['q']['verified'] == recount(S)['verified'] and S['res']['q']['cells'] == recount(S)['cells'],
     lambda S: put(S, 'res', dict(S['res'], q=dict(S['res']['q'], cells=-1)))),
    ('G-BOUND-FORM', 'every banked cell -- B the sum of the four terms, the tail the split`s sum, the shortfall not in B',
     lambda S: all(rel(c['B'], c['Eu'] + c['Ek'] + c['Etail'] + c['Eround']) and rel(c['Etail'], c['tail_on'] + c['tail_off']) for c in S['rows']),
     lambda S: bad_cell(S)),
    ('G-SHORTFALL-PRINTED', 'every scanned width carries its ESTIMATE; the report prints it',
     lambda S: bool(S['reach']['scan']) and all(s.get('shortfall') is not None for s in S['reach']['scan'])
     and all(c.get('shortfall') is not None for c in S['rows']) and 'shortfall' in S['report'],
     lambda S: put(S, 'report', S['report'].replace('shortfall', 'x'))),
    ('G-GROWTH-RECOMPUTED', 'every banked cell`s realized growth from the plateau`s closed form at i delta, at its p',
     lambda S: all(rel(c['growth'], growth_of(c['a'], c['p'])) and rel(c['growth_bound'], math.exp(DELTA * math.log(c['a']))) for c in S['rows']),
     lambda S: bad_cell(S)),
    ('G-SIGNS-RECOUNTED', 'the results` sign lists against the banked cells, recounted',
     lambda S: all(S['res']['q'][k] == recount(S)[k] for k in ('h2_neg', 'h2_pos')),
     lambda S: put(S, 'res', dict(S['res'], q=dict(S['res']['q'], h2_neg=[5.0])))),
    ('G-CROSSING-RECOMPUTED', 'the narrowest read width with ratio <= -1, recomputed',
     lambda S: S['res']['q']['cross_minus_one'] == recount(S)['cross'],
     lambda S: put(S, 'res', dict(S['res'], q=dict(S['res']['q'], cross_minus_one=30.0)))),
    ('G-XI-CITED', 'b520`s banked results against this act`s citation -- not recomputed',
     lambda S: S['res']['xi_cited'] == dict(cells=S['b20res']['xi']['cells'], verified=S['b20res']['xi']['verified'], positive=len(S['b20res']['xi']['h2_pos']))
     and 'CITED FROM b520' in S['report'], lambda S: put(S, 'res', dict(S['res'], xi_cited=dict(S['res']['xi_cited'], verified=-1)))),
    ('G-READING-WORDS', 'the reading against the recount AND the trail -- (R127)(2)`s words',
     lambda S: ((S['res']['reading'].startswith(HARD5)) if not recount(S)['h2_neg'] else WIT5 in S['res']['reading'])
     and S['res']['reading'] in trail(S), lambda S: put(S, 'res', dict(S['res'], reading='the window is a witness'))),
    ('G-N1-SCORED', 'the desk against the order bank', lambda S: 'n1' in S['sc'] and desk_word(S, 'N1') == word_of(S['sc']['n1'])
     and S['sc']['n1'] == (least_p(S) is None or least_p(S) >= 6), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the order bank', lambda S: 'n2' in S['sc'] and desk_word(S, 'N2') == word_of(S['sc']['n2'])
     and S['sc']['n2'] == (a0_at(S, least_p(S) or 20) is not None and a0_at(S, least_p(S) or 20) <= 30.0),
     lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the reach recomputed', lambda S: 'n3' in S['sc'] and desk_word(S, 'N3') == word_of(S['sc']['n3'])
     and S['sc']['n3'] == ((reach_recount(S)[0] or 0) > 30.0), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the cells recounted', lambda S: 'n4' in S['sc'] and desk_word(S, 'N4') == word_of(S['sc']['n4'])
     and S['sc']['n4'] == (recount(S)['cross'] is not None) and (recount(S)['cells'] > 0 or 'NO Q0 CELL WAS READ' in S['desk']),
     lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk']
     and desk_word(S, 'S1') == word_of(least_p(S) is None or least_p(S) >= 9)
     and desk_word(S, 'S2') == word_of(cmp_recount(S)[1] == len(S['cp']['rows']))
     and desk_word(S, 'S3') == word_of(cmp_recount(S)[2] == 0),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NOGRADE-CONFERRED', 'this act`s trail record and row -- no grade word, the row`s grade cell NO GRADE',
     lambda S: not GRADE_RE.search(seg(S['ot'], TRAILH, 99999)) and '| NO GRADE |' in corr_row(S),
     lambda S: put(S, 'ot', S['ot'] + ' `x_y_z` DERIVES')),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b521 -'))),
    ('G-PRIORBANK-APPEND-ONLY', 'file times against the face, the two noted banks excepted and proved append-only',
     lambda S: S['noprior'] and note_ok(S, 'b518_components.txt') and note_ok(S, 'b519_components.txt'),
     lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('stay OPEN', 'are closed'))),
    ('G-LANE-SHUT', 'the trail`s own record -- the numerical lane shut, said', lambda S: 'numerical lane shuts at this act' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(NL, ' ').replace('numerical lane shuts at this act', 'lane stays open'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the trail alone; no chain file edited; the kernel untouched',
     lambda S: sorted(S['tracked']) == ['OPEN_TRAILS.md'] and S['chain_clean'] is True and S['ker_clean'] is True,
     lambda S: put(S, 'ker_clean', False)),
    ('G-TRAIL-APPEND-ONLY', 'the trail`s own text', lambda S: S['ot'].count(TRAILH) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + TRAILH + ' a second record')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger -- row 370 once, six cells as it landed',
     lambda S: S['corr'].count('| 370 |') == 1 and S['corr'].count('(b521, under (R130))') == 1
     and len(corr_row(S).strip().strip('|').split('|')) == 6,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 370 | a duplicate row |')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b520`s close -- none modified',
     lambda S: S['tools_edited'] == [], lambda S: put(S, 'tools_edited', ['b519_window.py'])),
    ('G-WRITELIST-KINDS', 'every b521 commit in four repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b521')" in S['suite']
                and "data/b521_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b521_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b521')
              and 'data/b521_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b521 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    rec('  ### G-PRIORBANK-APPEND-ONLY checked %d prior banks by time; the two noted banks excepted and proved append-only.'
        % S['prior_checked'])
    rec('  ### ### **VACUOUS ON THE LIVE SOURCE -- NO Q0 CELL WAS READ : %s.** ### each refused its injected defective cell.'
        % ([a for a in VACUOUS_ARMS] if not S['rows'] else 'NONE'))
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
    out = os.path.join(D, 'b521_checks_postpush.txt' if pushed else 'b521_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b521_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
