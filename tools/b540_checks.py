# -*- coding: utf-8 -*-
"""b540_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b540_registration_2026-09-25.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = '2aec26d8'      # ### b539's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = '2293ca2'           # ### b539's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b540 —'
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


SK = os.path.join('D:', os.sep, 'SIDE-kernel')
SK_TIP = '0256e9e'
PREM = ['Bridge/ConservationBridge.lean', 'Kernel/XiDef.lean', 'Kernel/Voice1.lean']


PPFILES = ['ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md', 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md']


SIDE_TIP = '502f0a7a67462eab83a0f10eee5ea74be67957dd'
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
MAPP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
SURRP = os.path.join(PP, 'phase1.5', 'proofs', 'THE_UNCONDITIONAL_SURROUND.md')
PATHSP = os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md')
DEPM = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
MAPH = '### The tier law corrected under (R150), 2026-09-25 -- the RH-anchor named, T1 split (appended by b540; the appendix above is unedited)'
SURRH = '### The tier table corrected under (R150), 2026-09-25 (appended by b540; the table above is unedited)'
PATHSH = '## The tiers of (R149)-(R150), appended 2026-09-25 by b540 -- PATHS tiered against the RH-anchor (no line above this block changes)'
FTITLE = '## The cascade, act two: the tier law corrected, PATHS_TO_THE_CRITICAL_LINE tiered against the RH-anchor'
FIVE = ['h1_complete_at_Phi', 'C7_finite_type_false', 'blTerm_nonneg_of_onLine', 'spectral_cannon', 'ξ / Dirichlet order-≤1 inputs']
TIERS = ('T0', 'T1-open', 'T1-lit', 'T2', 'T3', 'T4')
E1, E3, E4, E914 = 'E-2026-09-25-1', 'E-2026-09-25-3', 'E-2026-09-25-4', 'E-2026-09-14-1'
N1TEXT = 'Route 3: RH restated (ch_iff_rh); Route 1: T2 by the decide-count conjunct and the C7 stand-in'


def delete_needles():
    """### regexes built from parts, so the suite cannot match its own source; `rm` needs no letter before it (defect (d))."""
    return [re.escape(x + y) for x, y in (('Remove', '-Item'), ('os.re', 'move('), ('shutil.rm', 'tree('), ('.un', 'link('), ('os.rm', 'dir('),
                                          ('Clear', '-Content'))] + ['(?<![A-Za-z])r' + 'm -', '(?<![A-Za-z])r' + 'mdir ']


def rd8(b):
    return b.decode('utf-8-sig', 'replace').replace(chr(13), '')


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    files = PPFILES + ['README.md', 'REGISTRY.md']
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b540_ferry.txt')),
        scan=read(os.path.join(D, 'b540_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b540_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b540_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b540_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b540_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b539_closing.txt')),
        addendum=read(os.path.join(D, 'b540_addendum.txt')),
        comp=read(os.path.join(D, 'b540_components.txt')),
        desk=read(os.path.join(D, 'b540_desk_notes.txt')),
        sc=json.loads(read(os.path.join(D, 'b540_scores.json')) or '{}'),
        purpose=read(os.path.join(D, 'b540_purpose.txt')),
        astat=read(os.path.join(D, 'b540_anchor_statements.txt')),
        fj=json.loads(read(os.path.join(D, 'b540_file.json')) or '{}'),
        lawj=json.loads(read(os.path.join(D, 'b540_law.json')) or '{}'),
        sj=json.loads(read(os.path.join(D, 'b540_sentences.json')) or '{}'),
        tj=json.loads(read(os.path.join(D, 'b540_tiers.json')) or '{}'),
        e4j=json.loads(read(os.path.join(D, 'b540_erratum4.json')) or '{}'),
        e4=read(os.path.join(D, 'b540_erratum_draft.md')), e3draft=read(os.path.join(D, 'b539_erratum_draft.md')),
        findj=json.loads(read(os.path.join(D, 'b540_findings.json')) or '{}'),
        pathsj=json.loads(read(os.path.join(D, 'b540_paths.json')) or '{}'),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in files},
        pp_now={f: open(os.path.join(PP, f), 'rb').read() for f in files},
        errata=read(os.path.join(PP, 'ERRATA.md')), mapt=read(MAPP), surrt=read(SURRP), pathst=read(PATHSP),
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT), dep=read(DEPM),
        corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        corr_prior=blob(SIDE, SIDE_TIP + ':CORRESPONDENCE.md').decode('utf-8', 'replace').replace(chr(13), ''),
        ker_clean={n: gits(p, 'status', '--porcelain', '--untracked-files=no') == '' for n, p in (('sef', KER), ('sk', SK), ('lv', LV))},
        ker_head=gits(KER, 'rev-parse', 'HEAD'),
        ker_changed=set(x for x in gits(KER, 'diff', '--name-only', KER_TIP).split(NL) if x.strip()),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b540_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b540_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b540_') and f.endswith('.py')
                        for n in delete_needles() if re.search(n, strip_prose(read(os.path.join(T, f)))))),
        suite=read(os.path.join(T, 'b540_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b540 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b540_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b540_purpose.txt', 'b540_file.json', 'b540_sentences.json',
                                                               'b540_tiers.json', 'b540_erratum_draft.md'))),
        before_lock=os.path.getmtime(os.path.join(D, 'b540_anchor_statements.txt')) < os.path.getmtime(FACE),
    )
    S['paths_lines'] = S['pathst'].split(NL)
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b540 --'):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-9]_|^b52[0-9]_|^b53[0-9]_|^b334_', f)]
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
        line = re.sub(r'(?<=[A-Za-z0-9])' + BT + r's\b', "'s", line)   # ### defect (e) of b540: a possessive no longer desyncs the pairing
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


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def above(S):
    """### PATHS`s lines above this act`s appended block."""
    L = S['paths_lines']
    return L[:L.index(PATHSH)] if PATHSH in L else L


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 14).split('.')[0].split(',')[0]


def word_of(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def subseq(old, new):
    it = iter(new.split(NL))
    return all(any(l == m for m in it) for l in old.split(NL))


def kept(S, f):
    old, new = rd8(S['pp_prior'][f]), rd8(S['pp_now'][f])
    ok = subseq(old, new)
    if f != 'ERRATA.md':
        ok = ok and S['pp_now'][f].startswith(S['pp_prior'][f])
    return ok


def entry(S):
    t = S['errata']
    i = t.find('## E-2026-09-25-3 ')
    j = t.find('**Filed 2026-09-25 by b540', i)
    if i < 0 or j < 0:
        return ''
    return t[i:t.find(NL, j) if t.find(NL, j) >= 0 else len(t)]


def outside_bt(text):
    return sum(l.count('`') % 2 for l in text.split(NL))


def block(S, text, h):
    return text[text.index(h):] if h in text else ''


def live_rows(S, lines, cols=1):
    out = []
    for ln in lines:
        l = S['paths_lines'][ln - 1] if ln - 1 < len(S['paths_lines']) else ''
        if not l.startswith('|'):
            return None
        out.append([x.strip() for x in l.strip().strip('|').split('|')][0])
    return out


def rows_ok(S, key):
    rows = S['tj'].get(key, [])
    if not rows:
        return False
    live = live_rows(S, [r['line'] for r in rows])
    if live is None or live != [r['cells'][0] for r in rows]:
        return False
    blk = block(S, S['pathst'], PATHSH)
    return all(r['tier'] in TIERS and ('| :%d | ' % r['line']) in blk and ('| **%s** |' % r['tier']) in blk for r in rows)


def recomputed(S):
    siii = S['tj'].get('siii', [])
    head = next((r for r in siii if r['line'] == 131), {})
    ii7 = next((r for r in siii if r['line'] == 139), {})
    a325 = next((r for r in S['tj'].get('annex_a', []) if r['line'] == 325), {})
    rep = [r for r in S['sj'].get('selected', []) if r.get('kind') == 'REPEATS']
    outside = [r for r in rep if r.get('verdict') == 'RESTS' and r.get('erratum') not in (E1, E3, E914)]
    return dict(
        n1=head.get('tier') == 'T2' and head.get('reason') == N1TEXT,
        n2=[r['line'] for r in siii if 'h2_sign_iff_rh' in r['reason']] == [139] and 'not compiled' in ii7.get('reason', ''),
        n3='`TailBoundPremise` (Voros) and `ExplicitFormulaDecomp` (Bombieri–Lagarias) are **T1-lit**' in a325.get('reason', ''),
        n4=any(r.get('verdict') == 'RESTS' and r.get('erratum') == E1 for r in rep) and bool(outside) == bool(S['e4']),
        n5=all(kept(S, f) for f in PPFILES),
        n6=(all(S['pp_now'][f] == S['pp_prior'][f] for f in ('README.md', 'REGISTRY.md')) and all(S['ker_clean'].values())
            and S['ker_head'].startswith('81ae175') and not S['zen'] and S['tok'] == 0 and S['dep_clean']),
        s1=outside_bt(entry(S)) == 0 and bool(entry(S)),
        s2=sum(len(re.findall(r'4\.062|5\.196|13\.153', l)) for l in above(S)) == 0,
        s3=S['lawj'].get('map_counts', {}).get('T4', 1) == 0)


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == recomputed(S)[k]


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R150) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b540' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-DECLARED', 'this act`s banked scan -- no flag, and the face says so',
     lambda S: '(R81) FLAGS : 0' in line_with(S['scan'], '(R81) FLAGS') and 'The ferry scan carries no (R81) flag' in flat(S['face']),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b539`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'E-2026-09-25-3 : DRAFTED' in S['prior'],
     lambda S: put(S, 'prior', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b540' in S['ferry'] and 'ACT b540' in S['face'] and not glob.glob(os.path.join(D, 'b541_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b540')),
    ('G-PEEK-DECLARED', 'the face`s (C) block, the anchor read before the lock, the components` banks after it',
     lambda S: 'A FRESH `#check` OF THE RH-ANCHOR`S STATEMENTS WAS RUN BEFORE THE SEAL' in flat(S['face']) and S['before_lock'] and S['after_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R150-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R150) END' in S['ferry'] and S['ot'].count('**(R150) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R150) ratified', '(R150) noted'))),
    ('G-PURPOSE-PRINTED', 'the purpose bank against the three keystones` own lines READ HERE',
     lambda S: S['paths_lines'][10] in S['purpose'] and S['mapt'].split(NL)[7] in S['purpose'] and S['surrt'].split(NL)[22] in S['purpose']
     and os.path.getmtime(os.path.join(D, 'b540_purpose.txt')) < os.path.getmtime(os.path.join(D, 'b540_file.json')),
     lambda S: put(S, 'purpose', '')),
    ('G-ANCHOR-STATEMENTS-FRESH', 'the pre-seal #check bank -- eight statements at 81ae175, exit 0',
     lambda S: 'at SIDE-explicit-formula 81ae175' in S['astat'] and '### exit 0' in S['astat']
     and len([l for l in S['astat'].split(NL) if re.match(r'^@?SIDEExplicitFormula\.\S+ :', l)]) == 8 and 'h2_sign ↔ RiemannHypothesis' in S['astat'],
     lambda S: put(S, 'astat', S['astat'].replace('### exit 0', '### exit 1'))),
    ('G-E3-FILED', 'ERRATA READ HERE -- the b539 draft`s bytes once, then the b540 Status line, after the prior last byte',
     lambda S: S['errata'].count(S['e3draft'].rstrip(NL)) == 1 and bool(entry(S)) and S['errata'].rstrip(NL).endswith(entry(S).split(NL)[-1])
     and "whether side-lv-conservation's zenodo description is edited under (r110) is a separate ruling, not taken here" in entry(S).lower() and bool(entry(S)),
     lambda S: put(S, 'errata', S['errata'].replace('**Filed 2026-09-25 by b540', '**Noted by b540'))),
    ('G-E3-LISTED', 'ERRATA READ HERE -- the bullet once, directly after E-2026-09-22-1`s',
     lambda S: (lambda t: NL.join(t).count('- `E-2026-09-25-3` —') == 1 and any(t[i].startswith('- `E-2026-09-22-1` —') and t[i + 1].startswith('- `E-2026-09-25-3` —')
                                                                      for i in range(len(t) - 1)))(S['errata'].split(NL)),
     lambda S: put(S, 'errata', S['errata'].replace('- `E-2026-09-25-3` —', '- `E-2026-09-25-3x` —'))),
    ('G-E3-BACKTICKS', 'the filed entry READ HERE -- no backtick left open on its line, equal to the bank',
     lambda S: bool(entry(S)) and outside_bt(entry(S)) == 0 == S['fj'].get('backticks_outside_code'),
     lambda S: put(S, 'errata', S['errata'].replace('**Filed 2026-09-25 by b540', '**Filed 2026-09-25 by b540`s'))),
    ('G-MAP-LAW-APPENDED', 'the map READ HERE -- the block once, after every prior byte; the anchor at its head; five sentences; counts',
     lambda S: S['mapt'].count(MAPH) == 1 and S['pp_now']['phase1.5/method/THE_LOAD_BEARING_MAP.md'].startswith(S['pp_prior']['phase1.5/method/THE_LOAD_BEARING_MAP.md'])
     and '**ranked here at the head of the hub terminals**' in block(S, S['mapt'], MAPH)
     and all(('- `%s` -- **T0**:' % n) in block(S, S['mapt'], MAPH) for n in FIVE)
     and block(S, S['mapt'], MAPH).count('says nothing about') + block(S, S['mapt'], MAPH).count('say nothing about') == 5
     and (' · '.join('%s %d' % kv for kv in S['lawj']['map_counts'].items())) in block(S, S['mapt'], MAPH),
     lambda S: put(S, 'mapt', S['mapt'].replace('**ranked here at the head of the hub terminals**', 'ranked'))),
    ('G-SURR-LAW-APPENDED', 'SURR READ HERE -- the block once, after every prior byte; :187 re-marked T1-lit; counts',
     lambda S: S['surrt'].count(SURRH) == 1 and S['pp_now']['phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md'].startswith(S['pp_prior']['phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md'])
     and '`:187` `PartialPositivity.partialPositivity_finiteRange` -- T4 → T1-lit' in block(S, S['surrt'], SURRH)
     and (' · '.join('%s %d' % kv for kv in S['lawj']['surr_counts'].items())) in block(S, S['surrt'], SURRH),
     lambda S: put(S, 'surrt', S['surrt'].replace('T4 → T1-lit', 'T4 → T4'))),
    ('G-PATHS-APPENDED', 'PATHS READ HERE -- the block once, after every prior byte',
     lambda S: S['pathst'].count(PATHSH) == 1 and S['pp_now']['phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md'].startswith(S['pp_prior']['phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md']),
     lambda S: put(S, 'pathst', S['pathst'].replace(PATHSH, PATHSH + ' ' + NL + PATHSH))),
    ('G-SI-READING', 'the PATHS block -- §I`s reading as banked, Route 3 struck, zero routes to σ = 1/2',
     lambda S: bool(S['tj'].get('si_reading')) and S['tj']['si_reading'] in block(S, S['pathst'], PATHSH)
     and 'with Route 3 struck' in S['tj']['si_reading'] and 'Zero compiled routes to σ = 1/2' in S['tj']['si_reading'],
     lambda S: put(S, 'pathst', S['pathst'].replace('Zero compiled routes to σ = 1/2', 'x'))),
    ('G-SIII-TIERED', 'the §III tiers against PATHS`s own rows READ HERE, row for row', lambda S: rows_ok(S, 'siii') and len(S['tj']['siii']) == 12,
     lambda S: put(S, 'paths_lines', S['paths_lines'][:131] + S['paths_lines'][132:])),
    ('G-ANNEXA-TIERED', 'the ANNEX A tiers against PATHS`s own rows READ HERE', lambda S: rows_ok(S, 'annex_a') and len(S['tj']['annex_a']) == 11,
     lambda S: put(S, 'tj', dict(S['tj'], annex_a=[dict(r, tier='T9') for r in S['tj'].get('annex_a', [])]))),
    ('G-ANNEXB-TIERED', 'the ANNEX B terminal rows against PATHS`s own lines READ HERE',
     lambda S: len(S['tj'].get('annex_b', [])) == 3 and all(S['paths_lines'][r['line'] - 1].startswith('| %s |' % r['row']) and r['tier'] in TIERS
                                                          and ('| :%d | %s | **%s** |' % (r['line'], r['row'], r['tier'])) in block(S, S['pathst'], PATHSH)
                                                          for r in S['tj']['annex_b']),
     lambda S: put(S, 'tj', dict(S['tj'], annex_b=[dict(r, row='A0') for r in S['tj'].get('annex_b', [])]))),
    ('G-LADDER-CHECK', 'PATHS READ HERE for the withdrawn extrema, with a control that finds them in FINDINGS',
     lambda S: sum(len(re.findall(r'4\.062|5\.196|13\.153', l)) for l in above(S)) == 0 == S['tj'].get('extrema')
     and len(re.findall(r'13\.153', S['find'])) > 0,
     lambda S: put(S, 'paths_lines', ['a window minimum at 13.153'] + S['paths_lines'])),
    ('G-CORR-TIERED', 'the Correspondence tiers against PATHS`s own rows READ HERE', lambda S: rows_ok(S, 'corr') and len(S['tj']['corr']) == 28,
     lambda S: put(S, 'tj', dict(S['tj'], corr=S['tj'].get('corr', [])[:-1]))),
    ('G-SENTENCES-READ', 'the sentence bank against PATHS READ HERE -- six yields; every row kinded; every RESTS naming its erratum',
     lambda S: len(S['sj'].get('yields', {})) == 6 and bool(S['sj'].get('selected'))
     and all(r['kind'] in ('REPEATS', 'OWN') for r in S['sj']['selected'])
     and all(r['verdict'] in ('STANDS', 'RESTS', 'EXCEEDS') and r['repeats'] for r in S['sj']['selected'] if r['kind'] == 'REPEATS')
     and all(r['erratum'] for r in S['sj']['selected'] if r.get('verdict') == 'RESTS')
     and all(' '.join(r['sentence'].split())[:50] in ' '.join(S['pathst'].split()) for r in S['sj']['selected']),
     lambda S: put(S, 'sj', dict(S['sj'], selected=[dict(r, kind='MAYBE') for r in S['sj'].get('selected', [])]))),
    ('G-E4-DRAFTED', 'the E-2026-09-25-4 draft READ HERE against the deposited monograph READ HERE',
     lambda S: S['e4'].startswith('## E-2026-09-25-4 — ') and 'DRAFT, NOT FILED' in S['e4'].split(NL)[0]
     and len(S['e4j'].get('rows', [])) == 4 and all(r['text'] in S['dep'].replace('**', '') and r['replacement'] for r in S['e4j']['rows'])
     and S['e4'].count('  - replacement: *"') == 4 and outside_bt(S['e4']) == 0,
     lambda S: put(S, 'dep', S['dep'].replace('it pinned the remaining content to a single goal state', 'x'))),
    ('G-E4-NOT-FILED', 'ERRATA READ HERE -- no E-2026-09-25-4 in it', lambda S: 'E-2026-09-25-4' not in S['errata'],
     lambda S: put(S, 'errata', S['errata'] + NL + '## E-2026-09-25-4')),
    ('G-FINDINGS-ENTERED', 'FINDINGS READ HERE -- the entry once; E-4 drafted; the next keystone',
     lambda S: S['find'].count(FTITLE) == 1 and '**E-2026-09-25-4 is DRAFTED, NOT FILED**' in S['find']
     and 'the next keystone of the cascade is BALANCE_AND_POSITIVITY' in S['find'],
     lambda S: put(S, 'find', S['find'].replace('BALANCE_AND_POSITIVITY', 'x'))),
    ('G-LINES-KEPT', 'the six written files against their blobs at b539`s commit, BOM stripped both sides',
     lambda S: all(kept(S, f) for f in PPFILES),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'FINDINGS.md': S['pp_now']['FINDINGS.md'][:200] + S['pp_now']['FINDINGS.md'][260:]}))),
    ('G-CEILING-UNCHANGED', 'README and REGISTRY bytes against their blobs', lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('README.md', 'REGISTRY.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'README.md': S['pp_now']['README.md'] + b' '}))),
    ('G-KERNELS-UNTOUCHED', 'three kernels READ HERE', lambda S: all(S['ker_clean'].values()) and S['ker_head'].startswith('81ae175') and S['ker_changed'] == set(),
     lambda S: put(S, 'ker_changed', {'SIDEExplicitFormula/Seam.lean'})),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b540_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b540_x.py', 'x')])),
    ('G-N1-SCORED', 'the desk against the tier bank', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the tier bank', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the tier bank', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the sentence bank and the draft', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the blobs', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the blobs, the kernels, the tools and the token', lambda S: nscored(S, 'n6'),
     lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2')
     and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b540 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernel`s tree', lambda S: 'No kernel lane opened at this act' in trail(S) and S['ker_changed'] == set(),
     lambda S: put(S, 'ot', S['ot'].replace('No kernel lane opened at this act', 'A lane opened'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the six written documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(TRAILH) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + TRAILH + ' a second record')),
    ('G-CORR-UNTOUCHED', 'the correspondence ledger against its blob -- no row this act',
     lambda S: S['corr'] == S['corr_prior'] and S['corr'] != '', lambda S: put(S, 'corr', S['corr'] + NL + '| 388 | a row |')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b539`s close -- none modified',
     lambda S: S['tools_edited'] == [], lambda S: put(S, 'tools_edited', ['corr_row.py'])),
    ('G-WRITELIST-KINDS', 'every b540 commit in four repositories, against (R91)`s STEM GLOB',
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
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked tree -- (R58)', lambda S: S['artefacts_tracked'] == '',
     lambda S: put(S, 'artefacts_tracked', 'data/anthropic-zeta23/formal-math/LICENSE')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'the suite`s own text -- b472`s repair, carried',
     lambda S: ("rev-parse', 'origin/main') == gits(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                and "log', '-1', '--pretty=%s').startswith('b540')" in S['suite']
                and "data/b540_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b540_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b540')
              and 'data/b540_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b540 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    rec('  ### ### **VACUOUS ARMS : %s.**'
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
    out = os.path.join(D, 'b540_checks_postpush.txt' if pushed else 'b540_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b540_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
