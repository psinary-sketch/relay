# -*- coding: utf-8 -*-
"""b535_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b535_registration_2026-09-25.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'a54a9075'      # ### b534's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = 'baed4df'           # ### the kernel's tip before this act
PRIOR_PP = '3b5532a'           # ### b534's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b535 —'
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


PPFILES = ['ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md', 'README.md', 'REGISTRY.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md']


def sources():
    import html as _html
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b535_ferry.txt')),
        scan=read(os.path.join(D, 'b535_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b535_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b535_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b535_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b535_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b534_closing.txt')),
        addendum=read(os.path.join(D, 'b535_addendum.txt')),
        comp=read(os.path.join(D, 'b535_components.txt')),
        desk=read(os.path.join(D, 'b535_desk_notes.txt')),
        sc=json.loads(read(os.path.join(D, 'b535_scores.json')) or '{}'),
        er=json.loads(read(os.path.join(D, 'b535_erratum.json')) or '{}'),
        draft=read(os.path.join(D, 'b532_erratum_draft.md')),
        errata=read(os.path.join(PP, 'ERRATA.md')),
        errata_prior=blob(PP, PRIOR_PP + ':ERRATA.md').decode('utf-8', 'replace').replace(chr(13), ''),
        zres=json.loads(read(os.path.join(D, 'b535_zenodo_results.json')) or '{}'),
        intended=json.loads(read(os.path.join(D, 'b535_intended.json')) or '{}'),
        fetch={r: json.loads(read(os.path.join(D, 'b535_fetchback_%s.json' % r)) or '{}') for r in ('21520474', '21539167')},
        before={r: json.loads(read(os.path.join(D, 'b535_before_%s.json' % r)) or '{}') for r in ('21520474', '21539167')},
        times={n: os.path.getmtime(os.path.join(D, n)) for n in ('b535_fetchback_21520474.json', 'b535_fetchback_21539167.json',
                                                                 'b535_platform_record.json', 'b535_rows.json', 'b535_finding.json',
                                                                 'b535_before_21520474.json', 'b535_before_21539167.json')
               if os.path.exists(os.path.join(D, n))},
        platform=json.loads(read(os.path.join(D, 'b535_platform_record.json')) or '{}'),
        finding=json.loads(read(os.path.join(D, 'b535_finding.json')) or '{}'),
        find=read(os.path.join(PP, 'FINDINGS.md')),
        dig=read(os.path.join(PP, 'phase2', 'method', 'THE_FINDINGS_AS_THEY_STAND.md')),
        ce=json.loads(read(os.path.join(D, 'b535_ceiling.json')) or '{}'),
        readme=read(os.path.join(PP, 'README.md')),
        registry=read(os.path.join(PP, 'REGISTRY.md')),
        fold=json.loads(read(os.path.join(D, 'b535_fold.json')) or '{}'),
        span_after=json.loads(read(os.path.join(D, 'b535_span_after.json')) or '{}'),
        span_now=subprocess.run([sys.executable, os.path.join(T, 'b363_span.py'), '--act', '535'], capture_output=True, text=True,
                                encoding='utf-8', errors='replace').stdout,
        tagbank=read(os.path.join(D, 'b535_tag.txt')),
        ls_tags=gits(KER, 'ls-remote', '--tags', 'origin', 'refs/tags/v0.1*'),
        baed_full=gits(KER, 'rev-parse', 'baed4df'),
        ker_head=gits(KER, 'rev-parse', 'HEAD'),
        ker_porcelain=[p for p in git(KER, 'status', '--porcelain').split(NL) if p.strip() and not p.startswith('??')],
        tok=json.loads(read(os.path.join(D, 'b535_tokenscan.json')) or '{}'),
        tok_self=sum(open(p, 'rb').read().count(tok) for p in glob.glob(os.path.join(D, 'b535_*')) if tok) if tok else -1,
        push_logs={os.path.basename(p): read(p) for p in glob.glob(os.path.join(D, 'b535_*push*.txt'))},
        rows=json.loads(read(os.path.join(D, 'b535_rows.json')) or '{}'),
        prof534=json.loads(read(os.path.join(D, 'b534_profile.json')) or '{}'),
        ker_h2sign=subprocess.run(['git', '-C', KER, 'show', 'baed4df:SIDEExplicitFormula/H2Sign.lean'], capture_output=True,
                                  text=True, encoding='utf-8').stdout,
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f).decode('utf-8', 'replace').replace(chr(13), '') for f in PPFILES},
        pp_now={f: read(os.path.join(PP, f)) for f in PPFILES},
        ot_prior_bytes=blob(PP, PRIOR_PP + ':OPEN_TRAILS.md'),
        ot_now_bytes=open(os.path.join(PP, 'OPEN_TRAILS.md'), 'rb').read(),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b535_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads', 'mirror-refresh-*-b535.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b535 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b535_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b535_tag.txt', 'b535_zenodo_c0.txt', 'b535_before_21520474.json',
                                                               'b535_erratum.json', 'b535_finding.json', 'b535_fold.json'))),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b535 --'):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-9]_|^b52[0-9]_|^b53[0-4]_|^b334_', f)]
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
EID1, EID2 = 'E-2026-09-25-1', 'E-2026-09-25-2'
FHEAD = ("## Weil positivity on classK and RH on the kernel's zero configuration: the equivalence compiled both ways; the seam "
         "to Mathlib's RiemannHypothesis named")
FOLDH = '## THE WEIL CONVERSE ARC, b526–b534 — THE FOLD'
DMARK = '<!-- b535 orientation refresh: the Weil converse arc -->'
OLD_CEIL = ('RH and Weil positivity on classK are one Prop apart in the kernel, RH → h2_sign compiled, h2_sign → RH compiled to '
            "its last step; the deposit's Route 3 premise is RH restated, E-2026-09-25-1 drafted.")
README_OLD = 'Supportable: *RH reduced to a single located clause, reduction machine-verified.*'
STATUS_ADD = ('The equivalence the programme holds after b534, Weil positivity on classK ↔ RH on the kernel\'s configuration, '
              'is a finding and is recorded in FINDINGS, not here.')
TAGS = ['Z21520474-01', 'Z21520474-02', 'Z21539167-01']


def wsj(s):
    return ' '.join((s or '').split())


def ceiling_from_ferry(S):
    f = wsj(S['ferry'])
    i = f.find('Supportable: "')
    j = f.find('" Not supportable:', i)
    return f[i + len('Supportable: "'):j] if i >= 0 and j > i else ''


def subseq(old, new):
    it = iter(new.split(NL))
    return all(any(l == m for m in it) for l in old.split(NL))


def entry(S):
    t = S['errata'].split(NL)
    try:
        a = next(i for i, l in enumerate(t) if l.startswith('## ' + EID1))
        b = next(i for i, l in enumerate(t) if l.startswith('*Filed 2026-09-25 by `b535`'))
    except StopIteration:
        return ''
    return NL.join(t[a:b + 1])


def outside_code_ticks(text):
    return sum(re.sub(r'`[^`\n]+`', '', l).count('`') for l in (text or '').split(NL))


def expected_filed(S):
    t = re.sub(r'([A-Za-z])`([sS])\b', r"\1'\2", S['draft'].rstrip(NL))
    return t


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def trail_raw(S):
    return seg(S['ot'], TRAILH, 99999)


def corr_row(S, n):
    return next((l for l in S['corr'].split(NL) if l.startswith('| %s |' % n)), '')


def cell(S, n, k):
    c = corr_row(S, n).strip().strip('|').split(' | ')
    return c[k] if len(c) == 6 else ''


def table_row(S, n):
    return next((l for l in S['table'].split(NL) if '`%s%s`' % (NS, n) in l), '')


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 14).split('.')[0].split(',')[0]


def word_of(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def span_now(S):
    m = re.search(r'THE CURRENT SPAN : (-?\d+)', S['span_now'])
    return int(m.group(1)) if m else None


def peeled(S):
    m = re.search(r'^([0-9a-f]{40})\s+refs/tags/v0\.1\^\{\}', S['ls_tags'], re.M)
    return m.group(1) if m else ''


def zmatch(S):
    out = {}
    for p in (S['zres'].get('c1') or {}).get('plan', []):
        rid = p['record']
        d = ((S['fetch'].get(rid) or {}).get('metadata') or {}).get('description')
        out[p['tag']] = (d is not None and d == S['intended'].get(rid) and d.count(p['new']) == 1 and p['old'] not in d)
    return out


def n_recomputed(S):
    return dict(
        n1=outside_code_ticks(entry(S)) == 0 and bool(entry(S)),
        n2=sorted(zmatch(S)) == TAGS and all(zmatch(S).values()),
        n3=bool(ceiling_from_ferry(S)) and ceiling_from_ferry(S) == S['ce'].get('ceiling') and ceiling_from_ferry(S) in wsj(trail_raw(S))
        and OLD_CEIL in wsj(trail_raw(S)) and ceiling_from_ferry(S) in wsj(S['readme']) and README_OLD in S['readme']
        and ceiling_from_ferry(S) in wsj(S['registry']),
        n4=span_now(S) == 1,
        n5=bool(peeled(S)) and peeled(S) == S['baed_full'],
        n6=S['dep_clean'] and (S['tok'].get('hits_total') == 0) and S['tok'].get('files_scanned', 0) > 0 and S['tok_self'] == 0
        and not any('WARNING' in v for v in S['push_logs'].values()),
        s1=span_now(S) == 0,
        s2=len(re.findall(r'[A-Za-z]`[sS]\b', S['draft'])) == 9,
        s3=all(((((S['zres'].get('c2') or {}).get('records') or {}).get(r) or {}).get('tries') or [{}])[0].get('identical') is True
               for r in ('21520474', '21539167')))


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == n_recomputed(S)[k]


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R145) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b535' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-ZERO', 'this act`s banked scan', lambda S: '(R81) FLAGS : 0' in line_with(S['scan'], '(R81) FLAGS'),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b534`s closing AND the ledger',
     lambda S: 'THE COMMITS, THE MIRROR, THE CENSUSES' in S['prior'] and S['corr'].count('| 383 |') == 1,
     lambda S: put(S, 'corr', S['corr'].replace('| 383 |', '| 3830 |'))),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b535' in S['ferry'] and 'ACT b535' in S['face'] and not glob.glob(os.path.join(D, 'b536_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b535')),
    ('G-PEEK-DECLARED', 'the face`s (C) block and the live reads` times -- every Zenodo read after the lock',
     lambda S: 'NO LIVE ZENODO READ WAS MADE BEFORE THE SEAL' in flat(S['face']) and S['after_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R145-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R145) END' in S['ferry'] and S['ot'].count('**(R145) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R145) ratified', '(R145) noted'))),
    ('G-FINDING-ENTERED', 'FINDINGS against the kernel at baed4df -- the heading once, h2_sign verbatim, the axioms line, the tag, the closing sentence',
     lambda S: S['find'].count(FHEAD) == 1 and NL.join(S['ker_h2sign'].split(NL)[28:31]) in S['find']
     and "'%sh2_sign_iff_rh_strip' depends on axioms: [propext, Classical.choice, Quot.sound]" % NS in S['find']
     and S['baed_full'] in S['find'] and "This is Weil's criterion (1952) in the kernel's own objects" in S['find'],
     lambda S: put(S, 'find', S['find'].replace(FHEAD, '## ghost'))),
    ('G-ERRATUM-FILED', 'ERRATA against the draft recomputed HERE -- every line of the draft, possessives changed, present; the Status sentence; the filing line',
     lambda S: bool(entry(S)) and S['errata'].count('## ' + EID1) == 1 and STATUS_ADD in entry(S)
     and all(l in entry(S) for l in expected_filed(S).split(NL) if l.strip() and not l.startswith('**Status.**'))
     and 'from this line the entry is FILED' in entry(S),
     lambda S: put(S, 'errata', S['errata'].replace(STATUS_ADD, ''))),
    ('G-ERRATUM-POSSESSIVES', 'the filed entry and the draft -- 0 backticks outside code spans; the count banked equals the draft`s',
     lambda S: outside_code_ticks(entry(S)) == 0 and bool(entry(S))
     and S['er'].get('possessives_found') == len(re.findall(r'[A-Za-z]`[sS]\b', S['draft'])),
     lambda S: put(S, 'errata', S['errata'].replace("The deposited kernel's Route 3", "The deposited kernel`s Route 3"))),
    ('G-PARTITION-APPENDED', 'ERRATA against its blob at b534`s commit -- the bullet right after the list`s last; every prior line kept in order',
     lambda S: (lambda t: any(t[i].startswith('- `E-2026-08-24-2` —') and t[i + 1].startswith('- `%s` —' % EID1)
                              for i in range(len(t) - 1)))(S['errata'].split(NL)) and subseq(S['errata_prior'], S['errata']),
     lambda S: put(S, 'errata', S['errata'].replace('- `%s` —' % EID1, '- ghost —'))),
    ('G-PLATFORM-RECORD-FILED', 'ERRATA -- E-2026-09-25-2 once, both records, the three tags each MATCH',
     lambda S: S['errata'].count('**`%s`' % EID2) == 1 and all(('[%s] **description sentence**' % t) in S['errata'] for t in TAGS)
     and seg(S['errata'], '**`%s`' % EID2, 99999).count('**MATCH**') >= 5,
     lambda S: put(S, 'errata', S['errata'].replace('[Z21539167-01] **description sentence**', '[ghost]'))),
    ('G-ZENODO-BEFORE-BANKED', 'the before banks and the dry plan -- both records banked, three spans found once',
     lambda S: all(((S['before'].get(r) or {}).get('metadata') or {}).get('description') for r in ('21520474', '21539167'))
     and (S['zres'].get('c1') or {}).get('once') == 3 and (S['zres'].get('c1') or {}).get('stop') is False,
     lambda S: put(S, 'zres', dict(S['zres'], c1=dict(S['zres'].get('c1') or {}, once=2)))),
    ('G-ZENODO-MATCH', 'the fetched-back bytes against the intended bytes, recomputed HERE, per replacement',
     lambda S: sorted(zmatch(S)) == TAGS and all(zmatch(S).values()),
     lambda S: put(S, 'intended', dict(S['intended'], **{'21539167': (S['intended'].get('21539167') or '') + ' '}))),
    ('G-FETCHBACK-BEFORE-ROW', 'file times -- both fetch-backs banked before the ERRATA record, the rows and the finding were written',
     lambda S: len([k for k in S['times'] if 'fetchback' in k]) == 2
     and max(S['times'][k] for k in S['times'] if 'fetchback' in k) < min(S['times'].get(k, 0) for k in
                                                                          ('b535_platform_record.json', 'b535_rows.json', 'b535_finding.json')),
     lambda S: put(S, 'times', dict(S['times'], **{'b535_rows.json': 0}))),
    ('G-TOKEN-ABSENT', 'the scan bank AND a scan HERE of every b535 data bank -- counts only',
     lambda S: S['tok'].get('set') is True and S['tok'].get('hits_total') == 0 and S['tok'].get('files_scanned', 0) > 0 and S['tok_self'] == 0,
     lambda S: put(S, 'tok_self', 1)),
    ('G-GUARD-RAN', 'the banked push outputs -- at least one, none carrying the limb`s WARNING',
     lambda S: bool(S['push_logs']) and not any('WARNING' in v for v in S['push_logs'].values()),
     lambda S: put(S, 'push_logs', dict(S['push_logs'], x='pre-push: WARNING — ZENODO_TOKEN is not set'))),
    ('G-CEILING-VERBATIM', 'the ferry`s sentence (whitespace-joined) against the bank, README, REGISTRY and the trail',
     lambda S: bool(ceiling_from_ferry(S)) and ceiling_from_ferry(S) == S['ce'].get('ceiling') and all(
         ceiling_from_ferry(S) in wsj(x) for x in (S['readme'], S['registry'], trail_raw(S))),
     lambda S: put(S, 'readme', S['readme'].replace('both directions compiled', 'both directions proved'))),
    ('G-CEILING-SIDE-BY-SIDE', 'README`s old line kept beside the new; the trail`s old and new quoted together; REGISTRY citing the old',
     lambda S: README_OLD in S['readme'] and 'Reworded under the author' in S['readme'] and '> old (b532):' in trail_raw(S)
     and '> new (R145)(2):' in trail_raw(S) and 'OPEN_TRAILS.md`:10790' in S['registry'],
     lambda S: put(S, 'readme', S['readme'].replace(README_OLD, ''))),
    ('G-FOLD-CHECKED', 'the fold bank -- its check passed, 18 verdict strings and 10 rulings matched',
     lambda S: S['fold'].get('ok') is True and sum(q['found'] for q in S['fold'].get('quotes', [])) == 18
     and sum(r['found'] for r in S['fold'].get('rulings', [])) == 10,
     lambda S: put(S, 'fold', dict(S['fold'], ok=False))),
    ('G-FOLD-APPENDED', 'FINDINGS and the digest -- the heading and the marker once each, after the finding; prefixes and no line removed',
     lambda S: S['find'].count(FOLDH) == 1 and S['dig'].count(DMARK) == 1 and S['find'].index(FHEAD) < S['find'].index(FOLDH)
     and all(w.get('prefix') and w.get('removed') == 0 for w in S['fold'].get('writes', [])),
     lambda S: put(S, 'find', S['find'] + NL + FOLDH)),
    ('G-SPAN-READ', 'the span tool RUN HERE against the bank and the trail',
     lambda S: span_now(S) is not None and span_now(S) == S['span_after'].get('current_span') and ('reads **%s** after it' % span_now(S)) in trail(S),
     lambda S: put(S, 'span_after', dict(S['span_after'], current_span=7))),
    ('G-TAG-PEELED', 'the remote READ HERE -- the peeled line equals baed4df`s full SHA and the bank',
     lambda S: bool(peeled(S)) and peeled(S) == S['baed_full'] and peeled(S) in S['tagbank'],
     lambda S: put(S, 'ls_tags', '')),
    ('G-KERNEL-TREE-UNCHANGED', 'the kernel`s git state -- HEAD at baed4df, no tracked change',
     lambda S: S['ker_head'] == S['baed_full'] and not S['ker_porcelain'],
     lambda S: put(S, 'ker_porcelain', [' M SIDEExplicitFormula/PowerLimit.lean'])),
    ('G-ROWS-GRADED', 'rows 384 and 385 -- their grade cells, and both theorems std3 in b534`s profile',
     lambda S: cell(S, 384, 4).startswith('`h2_sign_iff_rh_strip` DERIVES') and cell(S, 385, 4).startswith('`h2_sign_imp_rh_of_seam` INTERFACES on rh_strip_imp_rh')
     and (S['prof534'].get('std3') or {}).get(NS + 'h2_sign_iff_rh_strip') is True
     and (S['prof534'].get('std3') or {}).get(NS + 'h2_sign_imp_rh_of_seam') is True,
     lambda S: put(S, 'corr', S['corr'].replace('`h2_sign_imp_rh_of_seam` INTERFACES', '`h2_sign_imp_rh_of_seam` SHELL'))),
    ('G-TABLE-ROW', 'the regenerated terminal table -- both theorems PROFILED, with DERIVES and INTERFACES among their cells',
     lambda S: 'DERIVES' in table_row(S, 'h2_sign_iff_rh_strip') and 'INTERFACES' in table_row(S, 'h2_sign_imp_rh_of_seam')
     and 'NOT PROFILED' not in table_row(S, 'h2_sign_iff_rh_strip') + table_row(S, 'h2_sign_imp_rh_of_seam'),
     lambda S: put(S, 'table', S['table'].replace('`%sh2_sign_imp_rh_of_seam`' % NS, '`ghost`'))),
    ('G-LINES-KEPT', 'every PLACE-papers file written, against its blob at b534`s commit -- every prior line present, in order',
     lambda S: all(subseq(S['pp_prior'][f], S['pp_now'][f]) for f in PPFILES),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'README.md': S['pp_now']['README.md'].replace(README_OLD, '')}))),
    ('G-MIRROR-NOT-BUILT', 'the zip`s absence and the trail`s words -- (R145)(7)',
     lambda S: not S['mirror'] and 'no mirror built' in trail(S),
     lambda S: put(S, 'mirror', True)),
    ('G-N1-SCORED', 'the desk against the filed entry', lambda S: nscored(S, 'n1'),
     lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the fetch-backs', lambda S: nscored(S, 'n2'),
     lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the ceiling`s locations', lambda S: nscored(S, 'n3'),
     lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the span tool run HERE', lambda S: nscored(S, 'n4'),
     lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the remote`s peeled line', lambda S: nscored(S, 'n5'),
     lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the scans and the deposit tree', lambda S: nscored(S, 'n6'),
     lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2')
     and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b535 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('stay OPEN', 'are closed'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the six named files; no kernel file; the one tag at HEAD',
     lambda S: sorted(S['tracked']) == sorted(PPFILES) and not S['ker_porcelain'] and gits(KER, 'tag', '--points-at', 'HEAD') == 'v0.1',
     lambda S: put(S, 'tracked', list(S['tracked']) + ['SPIRAL_MAP.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS` bytes against its blob at b534`s commit -- a true prefix; one heading',
     lambda S: S['ot_now_bytes'].startswith(S['ot_prior_bytes']) and S['ot'].count(TRAILH) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + TRAILH + ' a second record')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger -- rows 384 and 385 once each, six cells each',
     lambda S: S['corr'].count('| 384 |') == 1 and S['corr'].count('| 385 |') == 1
     and all(len(corr_row(S, n).strip().strip('|').split(' | ')) == 6 for n in (384, 385)),
     lambda S: put(S, 'corr', S['corr'] + NL + '| 385 | a duplicate row |')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b534`s close -- none modified',
     lambda S: S['tools_edited'] == [], lambda S: put(S, 'tools_edited', ['errata_append.py'])),
    ('G-WRITELIST-KINDS', 'every b535 commit in four repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b535')" in S['suite']
                and "data/b535_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b535_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b535')
              and 'data/b535_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b535 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b535_checks_postpush.txt' if pushed else 'b535_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b535_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
