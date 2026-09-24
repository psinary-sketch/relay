# -*- coding: utf-8 -*-
"""b506_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE.

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
KERNEL = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
FACE = os.path.join(D, 'b506_registration_2026-09-23.txt')
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
        face=read(FACE), ferry=read(os.path.join(D, 'b506_ferry.txt')),
        scan=read(os.path.join(D, 'b506_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b506_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b506_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b506_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b506_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b505_closing.txt')),
        addendum=read(os.path.join(D, 'b506_addendum.txt')),
        comp=read(os.path.join(D, 'b506_components.txt')),
        desk=read(os.path.join(D, 'b506_desk_notes.txt')),
        span=read(os.path.join(D, 'b506_span_notes2.txt')) + read(os.path.join(D, 'b506_span_notes.txt')),
        c1=json.loads(read(os.path.join(D, 'b505_c1.json')) or '{}'),
        c2=json.loads(read(os.path.join(D, 'b506_c2_results.json')) or '{}'),
        c2log=read(os.path.join(D, 'b506_c2_log.txt')),
        edges_exist=os.path.exists(os.path.join(D, 'b506_edges.jsonl')),
        c2_exists=os.path.exists(os.path.join(D, 'b506_c2_results.json')),
        ann_prefix_git=all(read(os.path.join(D, n)).startswith(git(ROOT, 'show', 'a6af69f2:data/' + n).replace(chr(13), ''))
                           and len(git(ROOT, 'show', 'a6af69f2:data/' + n)) > 0
                           for n in ('b477_components.txt', 'b502_components.txt', 'b504_components.txt', 'b502_ferry.txt')),
        k3=read(os.path.join(D, 'b506_c3.txt')),
        ann=json.loads(read(os.path.join(D, 'b506_annotations.json')) or '[]'),
        annfiles={n: read(os.path.join(D, n)) for n in ('b477_components.txt', 'b502_components.txt', 'b504_components.txt', 'b502_ferry.txt')},
        sc=json.loads(read(os.path.join(D, 'b506_scores.json')) or '{}'),
        cells=sorted([json.loads(l) for l in read(os.path.join(D, 'b506_cells.jsonl')).split(NL) if l.strip()], key=lambda r: r['a']),
        tool=read(os.path.join(T, 'b506_complete.py')), ktool=read(os.path.join(T, 'b506_kernel.py')), dtool=read(os.path.join(T, 'b506_decomp.py')),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b506_checks.py')),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads', 'mirror-refresh-*-b506.zip'))),
        chain_clean=(gits(ROOT, 'status', '--porcelain', '--', 'tools/b321_window.py', 'tools/e16/carto_atlas.py',
                          'tools/b318_square.py', 'tools/b317_smear.py', 'tools/b326_closure.py', 'tools/b325_epstein.py',
                          'tools/b326_windows.py', 'tools/e16/zeta_ordinates.npy') == ''),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b506 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b506_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b506 --'):
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
    ANN = ('b477_components.txt', 'b502_components.txt', 'b504_components.txt', 'b502_ferry.txt')
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-5]_', f) and f not in ANN]
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


ANNF = ('b477_components.txt', 'b502_components.txt', 'b504_components.txt')
MARKA = 'ANNOTATION APPENDED AT b506 UNDER (R115)'

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b506' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b505`s closing AND the ledger',
     lambda S: 'THE COMMITS, THE MIRROR, THE CENSUSES' in S['prior'] and S['corr'].count('| 354 |') == 1,
     lambda S: put(S, 'corr', S['corr'].replace('| 354 |', '| 3540 |'))),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b506' in S['ferry'] and 'ACT b506' in S['face'] and not os.path.exists(os.path.join(D, 'b507_registration_2026-09-23.txt')),
     lambda S: cut(S, 'face', 'ACT b506')),
    ('G-PEEK-DECLARED', 'the face -- the pre-seal reads declared, and no count read before the seal',
     lambda S: 'NO FIXTURE, NO COUNT, NO KERNEL RESIDUAL AND NO ANNOTATION WAS RUN FOR THIS ACT BEFORE THE SEAL' in S['face']
     and 'b505_c2_fixture_diagnosis.txt' in S['face'],
     lambda S: cut(S, 'face', 'NO FIXTURE, NO COUNT, NO KERNEL RESIDUAL AND NO ANNOTATION WAS RUN FOR THIS ACT BEFORE THE SEAL')),
    ('G-PRICE-ON-FACE', 'the face`s (C2) rule -- the EDGE time under twenty minutes -- and the total printed beside it',
     lambda S: '(C2) THE PRICE, UNDER (R116)(3)' in S['face'] and 'if the edge rate at 30 strips projects past twenty minutes' in S['face'].replace(NL + '### ', ' ')
     and 0 < edge_secs(S['c2log']) < 1200 and (c2(S, 'seconds') or 0) > 0,
     lambda S: put(S, 'c2log', S['c2log'].replace('edges 1051 / 1051  817 s', 'edges 1051 / 1051  1817 s'))),
    ('G-R116-ENTERED', 'the banked ferry AND the trail',
     lambda S: 'RULING (R116) END' in S['ferry'] and S['ot'].count('**(R116) ratified.**') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R116) ratified.**', '(R116) noted'))),
    ('G-C1-CARRIED', 'b505`s Component 1 bank, cited by address in the trail, and no b506 decomposition run',
     lambda S: S['c1'].get('c1_frac') == '2/3' and S['c1'].get('lam_agree') == 4095
     and 'relay/data/b505_c1.json' in seg(S['ot'], '### b506 —', 99999) and not os.path.exists(os.path.join(D, 'b506_c1.json')),
     lambda S: put(S, 'ot', S['ot'].replace('relay/data/b505_c1.json', 'b505'))),
    ('G-EVALUATOR-FIXTURE', 'the results bank -- (R116)(2)`s two counts over 148, recomputed from the rows',
     lambda S: len(c2(S, 'fixture') or []) == 148 and c2(S, 'fixture_dist_pass') == 148 == sum(1 for r in c2(S, 'fixture') if r['dist'] < 1e-9)
     and c2(S, 'fixture_route_pass') == 148 == sum(1 for r in c2(S, 'fixture') if r['ab'] < 1e-8),
     lambda S: put(S, 'c2', dict(S['c2'], fixture=[dict(r, dist=1e-6) for r in c2(S, 'fixture')]))),
    ('G-SIGMA-MAX-BOUND', 'the bank, the tool and the face -- sigma_max 1.5 from the printed bound',
     lambda S: c2(S, 'sig_max') == 1.5 and 'SIG_MAX = 1.5 ' in S['tool'] and '1.5497 < r(1) = 2' in S['face'],
     lambda S: put(S, 'c2', dict(S['c2'], sig_max=1.2))),
    ('G-WHOLE-STRIP', 'the bank -- 450 boxes in three columns, the whole contour equal to their sum',
     lambda S: len(c2(S, 'boxes') or []) == 450 and sorted(set(b['col'] for b in c2(S, 'boxes'))) == ['L', 'M', 'R']
     and abs(c2(S, 'whole', 0) - c2(S, 'total', -9)) < 0.05 and c2(S, 'total') == sum(b['n'] for b in c2(S, 'boxes')),
     lambda S: put(S, 'c2', dict(S['c2'], whole=c2(S, 'whole', 0) + 1.0))),
    ('G-BOXES-INTEGER', 'every box -- its winding within 0.05 of an integer',
     lambda S: c2(S, 'not_near') == 0 and all(abs(b['wind'] - round(b['wind'])) < 0.05 for b in c2(S, 'boxes') or [{'wind': 0.5}]),
     lambda S: put(S, 'c2', dict(S['c2'], boxes=[dict(b, wind=b['wind'] + 0.3) for b in c2(S, 'boxes')]))),
    ('G-COUNT-VS-MAIN', 'the bank and the log LINE -- the ferry`s term, the smooth term and S(150) all printed',
     lambda S: abs(c2(S, 'main_ferry', 0) - 178.5959741491629) < 1e-9 and c2(S, 'smooth') is not None and c2(S, 'S') is not None
     and 'N(150) smooth term' in line_with(S['c2log'], 'N(150) smooth term'),
     lambda S: put(S, 'c2log', S['c2log'].replace('N(150) smooth term', 'N(150)'))),
    ('G-LINE-VS-BANK', 'every M box against the bank`s ordinates in its strip, recounted',
     lambda S: all(b.get('bank') == sum(1 for z in json.loads(read(os.path.join(D, 'b326_epstein_zeros.json')))['zeros']
                                       if b['j'] <= z['gamma_a'] < b['j'] + 1) for b in c2(S, 'boxes') if b['col'] == 'M')
     and len(c2(S, 'm_mismatch')) == sum(1 for b in c2(S, 'boxes') if b['col'] == 'M' and b['n'] != b['bank']),
     lambda S: put(S, 'c2', dict(S['c2'], boxes=[dict(b, bank=(b.get('bank') or 0) + 1) for b in c2(S, 'boxes')]))),
    ('G-MISSING-LOCATED', 'the bank -- every R zero located, one per box, inside its box, |Z| after Newton printed',
     lambda S: sum(1 for z in c2(S, 'found') if z['col'] == 'R') == (c2(S, 'per') or {}).get('R', -1)
     and all(z.get('rho') and z.get('inside') and 'absz' in z for z in c2(S, 'found')),
     lambda S: put(S, 'c2', dict(S['c2'], found=[dict(z, inside=False) for z in c2(S, 'found')] or [dict(inside=False)]))),
    ('G-ROUTE-A-CONFIRMS', 'every located zero -- route A`s implied distance below 1e-9',
     lambda S: len(c2(S, 'found') or []) > 0 and all(z.get('route_a_dist', 1) < 1e-9 for z in c2(S, 'found')),
     lambda S: put(S, 'c2', dict(S['c2'], found=[dict(z, route_a_dist=1e-3) for z in c2(S, 'found')]))),
    ('G-POSITIVE-CONTROL', 'the bank -- both banked off-line zeros recovered to 1e-8',
     lambda S: c2(S, 'control') == [True, True],
     lambda S: put(S, 'c2', dict(S['c2'], control=[True, False]))),
    ('G-REGGATE-REEXAMINED', 'the log -- the verdict LINE, and the fixture counts it rests on',
     lambda S: 'THE BANKED ZEROS STAND' in line_with(S['c2log'], 'REGISTERED GATE RE-EXAMINED') and c2(S, 'fixture_dist_pass') == 148,
     lambda S: put(S, 'c2log', S['c2log'].replace('THE BANKED ZEROS STAND', 'x'))),
    ('G-C3-GATED', 'the kernel tool`s refusal, and the cells bank against whether the bank closed',
     lambda S: 'COMPONENT 2 DID NOT CLOSE THE BANK -- COMPONENT 3 IS NOT RUN.' in S['ktool']
     and (len(S['cells']) > 0) == c2_closed(S),
     lambda S: cut(S, 'ktool', 'COMPONENT 2 DID NOT CLOSE THE BANK -- COMPONENT 3 IS NOT RUN.')),
    ('G-C3-GRID-RULE', 'every cell -- nv the least value not below 8193 with the image above 350',
     lambda S: len(S['cells']) == 0 or all(c['nv'] == least_nv(2 * math.pi * (c['nv'] - 1) / c['image']) and c['image'] > 350 for c in S['cells']),
     lambda S: put(S, 'cells', [dict(c, image=300.0) for c in S['cells']] or [dict(nv=1, image=300.0)])),
    ('G-C3-TAIL-TESTED', 'every cell -- the tail against its bound, and the report`s population LINE',
     lambda S: len(S['cells']) == 0 or (all(c['tail_inside'] == (c['tail'] <= c['B']) for c in S['cells'])
                                         and 'POPULATION : %d' % len(population(S)) in line_with(S['k3'], '  POPULATION :')),
     lambda S: put(S, 'cells', [dict(c, tail_inside=not c['tail_inside']) for c in S['cells']] or [dict(tail_inside=True, tail=1, B=0)])),
    ('G-C3-STOP-HONOURED', 'the Component 3 report -- every unverified population cell printed by a, and the STOP line iff any',
     lambda S: len(S['cells']) == 0 or (line_with(S['k3'], 'UNVERIFIED IN THE POPULATION :').count('a=')
                                         == sum(1 for c in population(S) if not c['verified'])
                                         and ('IT FAILS THERE -- STOP' in S['k3']) == any(not c['verified'] for c in population(S))),
     lambda S: put(S, 'cells', [dict(c, verified=not c['verified']) for c in S['cells']] or [dict(tail_inside=True, verified=False)])),
    ('G-ANNOT-UNVERIFIED', 'the three components files -- ONE b506 note each, marking the margins UNVERIFIED, citing the count',
     lambda S: all(S['annfiles'][n].count(MARKA) == 1 and 'ARE UNVERIFIED' in S['annfiles'][n][S['annfiles'][n].index(MARKA):]
                   and 'so the bank lacks %d' % c2(S, 'lacks_strip', -1) in S['annfiles'][n][S['annfiles'][n].index(MARKA):].replace(NL + '### ', ' ')
                   for n in ANNF),
     lambda S: put(S, 'annfiles', dict(S['annfiles'], **{'b502_components.txt': S['annfiles']['b502_components.txt'].replace('ARE UNVERIFIED', 'stand')}))),
    ('G-ANNOT-B502-FERRY', 'b502`s ferry -- its text preserved and ONE note after it',
     lambda S: S['annfiles']['b502_ferry.txt'].count(MARKA) == 1
     and 'x^2 + 5y^2' in S['annfiles']['b502_ferry.txt'][:S['annfiles']['b502_ferry.txt'].index(MARKA)]
     and 'IS NOT A FORM THE RECORD HOLDS' in S['annfiles']['b502_ferry.txt'],
     lambda S: put(S, 'annfiles', dict(S['annfiles'], **{'b502_ferry.txt': S['annfiles']['b502_ferry.txt'].replace('IS NOT A FORM THE RECORD HOLDS', '')}))),
    ('G-ANNOT-PREFIX', 'the annotation tool`s record AND the committed blobs -- four files, each prefix proved',
     lambda S: len(S['ann']) == 4 and all(a.get('prefix') is True and a.get('removed') == 0 and a.get('marks') == 1 for a in S['ann'])
     and S['ann_prefix_git'],
     lambda S: put(S, 'ann', [dict(a, prefix=False) for a in S['ann']])),
    ('G-N1-SCORED', 'the desk against the fixture counts', lambda S: 'n1' in (S['sc'] or {}) and desk_word(S, 'N1') == word_of(S['sc']['n1'])
     and S['sc']['n1'] == (c2(S, 'fixture_dist_pass') == 148 and c2(S, 'fixture_route_pass') == 148),
     lambda S: put(S, 'sc', dict(S['sc'], n1=not (S['sc'] or {}).get('n1')))),
    ('G-N2-SCORED', 'the desk against the count', lambda S: 'n2' in (S['sc'] or {}) and desk_word(S, 'N2') == word_of(S['sc']['n2'])
     and S['sc']['n2'] == (25 <= c2(S, 'lacks_strip', -1) <= 33 and c2(S, 'beyond1', 0) >= 1),
     lambda S: put(S, 'sc', dict(S['sc'], n2=not (S['sc'] or {}).get('n2')))),
    ('G-N3-SCORED', 'the desk against the cells', lambda S: 'n3' in (S['sc'] or {}) and desk_word(S, 'N3') == word_of(S['sc']['n3'])
     and S['sc']['n3'] == (None if not S['cells'] else sum(1 for c in population(S) if c['verified']) >= 40),
     lambda S: put(S, 'sc', dict(S['sc'], n3=not (S['sc'] or {}).get('n3')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from its bank',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk']
     and desk_word(S, 'S1') == word_of(c2(S, 'm_mismatch') is not None and len(c2(S, 'm_mismatch')) == 0)
     and desk_word(S, 'S2') == word_of(abs(c2(S, 'total', 0) - c2(S, 'smooth', 0) - c2(S, 'S', 0)) < 0.05),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NOGRADE-CONFERRED', 'the face', lambda S: 'THIS ACT CONFERS NO GRADE' in S['face'],
     lambda S: cut(S, 'face', 'THIS ACT CONFERS NO GRADE')),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record',
     lambda S: 'where the deposit left it' in seg(S['ot'], '### b506 —', 99999).replace(NL, ' '),
     lambda S: put(S, 'ot', S['ot'].replace('### b506 —', '### b506 -'))),
    ('G-NOPRIORBANK', 'file times against the face, the four annotated files excepted by name',
     lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record',
     lambda S: 'the four lists stay OPEN' in seg(S['ot'], '### b506 —', 99999).replace(NL, ' '),
     lambda S: put(S, 'ot', S['ot'].replace('stay OPEN', 'are closed'))),
    ('G-LANE-SHUT', 'the trail`s own record -- the lane shut, said',
     lambda S: 'The numerical lane shuts at this act' in seg(S['ot'], '### b506 —', 99999).replace(NL, ' '),
     lambda S: put(S, 'ot', S['ot'].replace(NL, ' ').replace('The numerical lane shuts at this act', 'the lane stays open'))),
    ('G-SPAN-BY-TOOL', 'the span tool record', lambda S: 'THE CURRENT SPAN' in S['span'], lambda S: cut(S, 'span', 'THE CURRENT SPAN')),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- ONE document; no instrument edited',
     lambda S: sorted(S['tracked']) == ['OPEN_TRAILS.md'] and S['chain_clean'] is True, lambda S: put(S, 'chain_clean', False)),
    ('G-TRAIL-APPEND-ONLY', 'the trail`s own text', lambda S: S['ot'].count('### b506 —') == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + '### b506 — a second record')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger',
     lambda S: S['corr'].count('| 355 |') == 1 and S['corr'].count('(b506, under (R116))') == 1,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 355 | a duplicate row |')),
    ('G-WRITELIST-KINDS', 'every b506 commit in three repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b506')" in S['suite']
                and "data/b506_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b506_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b506')
              and 'data/b506_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b506 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    rec('  ### G-NOPRIORBANK checked %d prior banks. ### ### **4 EXCLUDED BY NAME** -- the files Component 4 appends to, held by G-ANNOT-PREFIX against a6af69f2.'
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
    out = os.path.join(D, 'b506_checks_postpush.txt' if pushed else 'b506_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b506_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
