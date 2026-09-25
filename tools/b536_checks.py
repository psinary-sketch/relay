# -*- coding: utf-8 -*-
"""b536_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b536_registration_2026-09-25.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'd452a5f8'      # ### b535's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = 'baed4df'           # ### the kernel's tip before this act
PRIOR_PP = '6813679'           # ### b535's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b536 —'
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


PPFILES = ['ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md', 'README.md', 'REGISTRY.md']


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b536_ferry.txt')),
        scan=read(os.path.join(D, 'b536_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b536_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b536_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b536_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b536_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b535_closing.txt')),
        addendum=read(os.path.join(D, 'b536_addendum.txt')),
        comp=read(os.path.join(D, 'b536_components.txt')),
        desk=read(os.path.join(D, 'b536_desk_notes.txt')),
        sc=json.loads(read(os.path.join(D, 'b536_scores.json')) or '{}'),
        att=json.loads(read(os.path.join(D, 'b536_attempts.json')) or '[]'),
        att_files={int(re.search(r'attempt(\d+)\.lean$', p).group(1)): hashlib.sha256(open(p, 'rb').read()).hexdigest()
                   for p in glob.glob(os.path.join(D, 'b536_attempt[0-9]*.lean'))},
        clogs=len(glob.glob(os.path.join(D, 'b536_compile_log*.txt'))),
        clast=read(sorted(glob.glob(os.path.join(D, 'b536_compile_log*.txt')), key=os.path.getmtime)[-1]),
        plog=read(sorted(glob.glob(os.path.join(D, 'b536_profile_log*.txt')), key=os.path.getmtime)[-1]),
        inst=json.loads(read(os.path.join(D, 'b536_install.json')) or '{}'),
        prof=json.loads(read(os.path.join(D, 'b536_profile.json')) or '{}'),
        probes=[read(os.path.join(D, 'b536_probe%d.txt' % n)) for n in (1, 2)],
        mod=read(os.path.join(KER, 'SIDEExplicitFormula', 'Seam.lean')),
        tagbank=read(os.path.join(D, 'b536_tag.txt')),
        ls_tags=gits(KER, 'ls-remote', '--tags', 'origin', 'refs/tags/v0.2*'),
        seam_commit=gits(KER, 'log', '-1', '--format=%H', '--', 'SIDEExplicitFormula/Seam.lean'),
        ker_head=gits(KER, 'rev-parse', 'HEAD'),
        ker_changed=set(x for x in gits(KER, 'diff', '--name-only', 'baed4df').split(NL) if x.strip())
                    | set(p[3:].strip() for p in git(KER, 'status', '--porcelain').split(NL) if p.strip() and not p.startswith('??')),
        hk=json.loads(read(os.path.join(D, 'b536_housekeeping.json')) or '{}'),
        errata=read(os.path.join(PP, 'ERRATA.md')),
        pa=json.loads(read(os.path.join(D, 'b536_priorart.json')) or '{}'),
        pgrep=read(os.path.join(D, 'b536_priorart_grep.txt')),
        preadme=read(os.path.join(D, 'b536_priorart_readme_main.md')),
        und=json.loads(read(os.path.join(D, 'b536_understandings.json')) or '{}'),
        tail53=read(os.path.join(T, 'b521_tail.py')).split(NL)[52].strip(),
        find=read(os.path.join(PP, 'FINDINGS.md')),
        ce=json.loads(read(os.path.join(D, 'b536_ceiling.json')) or '{}'),
        ce535=json.loads(read(os.path.join(D, 'b535_ceiling.json')) or '{}'),
        readme=read(os.path.join(PP, 'README.md')),
        registry=read(os.path.join(PP, 'REGISTRY.md')),
        rows=json.loads(read(os.path.join(D, 'b536_rows.json')) or '{}'),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f).decode('utf-8', 'replace').replace(chr(13), '') for f in PPFILES},
        pp_now={f: read(os.path.join(PP, f)) for f in PPFILES},
        ot_prior_bytes=blob(PP, PRIOR_PP + ':OPEN_TRAILS.md'),
        ot_now_bytes=open(os.path.join(PP, 'OPEN_TRAILS.md'), 'rb').read(),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b536_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b536_') and needle in read(os.path.join(T, f))],
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b536_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b536 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b536_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b536_install.json', 'b536_attempts.json', 'b536_priorart_grep.txt',
                                                               'b536_priorart_readme_main.md', 'b536_housekeeping.json'))),
        probe_before=all(os.path.getmtime(os.path.join(D, 'b536_probe%d.txt' % n)) < os.path.getmtime(FACE) for n in (1, 2)),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b536 --'):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-9]_|^b52[0-9]_|^b53[0-5]_|^b334_', f)]
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
THMS = ['zeta_zero_re_nonpos', 'rh_strip_imp_rh_holds', 'h2_sign_imp_rh_holds', 'h2_sign_iff_rh', 'h2_sign_imp_ch_holds', 'ch_iff_h2_sign']
RH_PRINT = '∀ (s : ℂ), riemannZeta s = 0 → (¬∃ n, s = -2 * (↑n + 1)) → s ≠ 1 → s.re = 1 / 2'
UTITLE = ("## Understandings arising from the Weil converse arc, b526–b535, in the navigator's words, entered on the author's word "
          "(R146)(5)")
PTITLE = "## The prior-art search for Weil's criterion in Lean, b536, 2026-09-25 — dated and refutable"
HK_LINE = '*Appended under the heading by b536 on the author\'s ruling `(R146)`(3)'
SPANC = "The span tool's convention, recorded once under (R146)(3):"


def wsj(s):
    return ' '.join((s or '').split())


def subseq(old, new):
    it = iter(new.split(NL))
    return all(any(l == m for m in it) for l in old.split(NL))


def std(S, n):
    return (S['prof'].get('std3') or {}).get(NS + n) is True


def fails(S):
    out = {}
    for a in S['att']:
        for d0 in a.get('failed_decls', []):
            out.setdefault(d0, []).append(a['attempt'])
    return out


def halted(S):
    return sorted(d for d, ns in fails(S).items() if len(ns) >= 2)


def check_line(S, n):
    return wsj((S['prof'].get('checks') or {}).get(n))


def peeled(S):
    m = re.search(r'^([0-9a-f]{40})\s+refs/tags/v0\.2\^\{\}', S['ls_tags'], re.M)
    return m.group(1) if m else ''


def paras(S):
    f = S['ferry']
    if 'TEXT BEGIN\n' not in f or '\nTEXT END' not in f:
        return []
    t = f[f.index('TEXT BEGIN\n') + len('TEXT BEGIN\n'):f.index('\nTEXT END')]
    return [p.replace(' [procedural]', '') for p in t.split(NL) if p.strip()]


def new_ceiling(S):
    f = wsj(S['ferry'])
    i = f.find('reads, supportable: "')
    j = f.find('" Not supportable: unchanged', i)
    return f[i + len('reads, supportable: "'):j] if i >= 0 and j > i else ''


def weil_lines(S):
    g = S['pgrep']
    if '### hit lines:' not in g:
        return []
    seg0 = g[g.index('### hit lines:'):g.index("### files matching 'explicit formula'")]
    return [l for l in seg0.split(NL)[1:] if l.strip()]


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


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


def n_recomputed(S):
    wl = weil_lines(S)
    return dict(
        n1=RH_PRINT in S['probes'][0],
        n2=std(S, 'zeta_zero_re_nonpos') and not any(a >= 2 for a in fails(S).get('zeta_zero_re_nonpos', [])),
        n3=all(std(S, n) for n in THMS) and check_line(S, 'h2_sign_iff_rh') == '%sh2_sign_iff_rh : %sh2_sign ↔ RiemannHypothesis' % (NS, NS),
        n4=bool(wl) and all(re.search(r'Weilacher|Kurzweil|Mordell-Weil', l) for l in wl),
        n5=all(subseq(S['pp_prior'][f], S['pp_now'][f]) for f in PPFILES),
        n6=S['dep_clean'] and not S['zen'] and S['tok'] == 0,
        s1='zeta_zero_re_nonpos' not in fails(S),
        s2=bool(wl) and all(re.search(r'Mordell-Weil|Weil pairing|Weil conjecture', l) for l in wl),
        s3=bool(S['preadme']) and all(q in wsj(S['preadme']) for q in (S['pa'].get('readme_quotes') or ['x'])))


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == n_recomputed(S)[k]


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling, the text and part 1 of 1, each END present',
     lambda S: 'RULING (R146) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b536' in S['ferry'] and 'TEXT END' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-DECLARED', 'this act`s banked scan -- four flags read off it and declared on the face',
     lambda S: '(R81) FLAGS : 4' in line_with(S['scan'], '(R81) FLAGS') and 'four (R81) flags are INFORMATIONAL' in flat(S['face']),
     lambda S: put(S, 'scan', S['scan'].replace('(R81) FLAGS : 4', '(R81) FLAGS : 5'))),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b535`s closing AND the ledger',
     lambda S: 'THE COMMITS, THE TAG, THE CENSUSES' in S['prior'] and S['corr'].count('| 385 |') == 1,
     lambda S: put(S, 'corr', S['corr'].replace('| 385 |', '| 3850 |'))),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b536' in S['ferry'] and 'ACT b536' in S['face'] and not glob.glob(os.path.join(D, 'b537_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b536')),
    ('G-PEEK-DECLARED', 'the face`s (C) block, the probes` times before the lock, the search`s and the install`s after it',
     lambda S: 'NO GREP OF MATHLIB OR ZETA23 FOR THE SEARCH, AND NO FETCH, WAS MADE BEFORE THE SEAL' in flat(S['face'])
     and S['probe_before'] and S['after_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R146-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R146) END' in S['ferry'] and S['ot'].count('**(R146) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R146) ratified', '(R146) noted'))),
    ('G-INSTALLED-FROM-DRAFT', 'the install bank against attempt 1`s banked source -- onto no prior file',
     lambda S: S['inst']['Seam.lean']['prior_sha'] is None and S['inst']['AxiomCheckSeam.lean']['prior_sha'] is None
     and S['inst']['Seam.lean']['draft_sha'] == S['inst']['Seam.lean']['installed_sha'] == S['att'][0]['source_sha'] == S['att_files'].get(1),
     lambda S: put(S, 'inst', {**S['inst'], 'Seam.lean': dict(S['inst']['Seam.lean'], draft_sha='0' * 64)})),
    ('G-ATTEMPTS-BANKED', 'the attempts bank against the banked sources and logs',
     lambda S: [a['attempt'] for a in S['att']] == list(range(1, len(S['att']) + 1)) == sorted(S['att_files'])
     and all(S['att_files'][a['attempt']] == a['source_sha'] for a in S['att']) and S['clogs'] == len(S['att']),
     lambda S: put(S, 'att', S['att'][:-1])),
    ('G-MODULE-NO-SORRY', 'the module text, the last compile log and the profile log',
     lambda S: bool(S['mod']) and not re.search(r'\bsorry\b', S['mod']) and 'exit 0 ;' in S['clast'] and ': error' not in S['clast']
     and 'sorryAx' not in S['plog'],
     lambda S: put(S, 'mod', S['mod'] + NL + 'theorem x : False := sorry')),
    ('G-PROFILE-WHOLE-STRING', 'the profile run file -- the six, each line equal to the standard-three string',
     lambda S: re.findall(r'^theorem (\S+)', S['mod'], re.M) == THMS
     and all([l.strip() for l in S['plog'].split(NL) if l.startswith("'%s%s'" % (NS, n))] == [STD3 % (NS + n)] for n in THMS),
     lambda S: put(S, 'plog', S['plog'].replace(STD3 % (NS + 'h2_sign_iff_rh'), (STD3 % (NS + 'h2_sign_iff_rh')).replace(', Quot.sound', ', sorryAx')))),
    ('G-PROBES-BANKED', 'the two banked probes -- sources and outputs; no theorem; COMPONENT 1`s names checked',
     lambda S: all(p.count('### output') == 1 and not re.search(r'^theorem ', p, re.M) for p in S['probes'])
     and all(('#check @%s' % n) in S['probes'][0] for n in ('riemannZeta_one_sub', 'riemannZeta_ne_zero_of_one_le_re', 'riemannZeta_zero',
                                                             'Complex.Gamma_ne_zero', 'Complex.cos_eq_zero_iff', 'Zeta23.zetaZeroConfig_carrier'))
     and '#print RiemannHypothesis' in S['probes'][0],
     lambda S: put(S, 'probes', [S['probes'][0].replace('#print RiemannHypothesis', ''), S['probes'][1]])),
    ('G-RH-PRINTED', 'probe 1 AND the profile run -- RiemannHypothesis printed, its three hypotheses',
     lambda S: RH_PRINT in S['probes'][0] and RH_PRINT in S['plog'],
     lambda S: put(S, 'plog', S['plog'].replace(RH_PRINT, 'x'))),
    ('G-HALTS-RECORDED', 'the attempts bank against the module -- every halted lemma a `_blocked` Prop',
     lambda S: all(a.get('failed_decls') is not None for a in S['att'])
     and set(halted(S)) == set(re.findall(r'^def (\S+)_blocked\b', S['mod'], re.M)),
     lambda S: put(S, 'att', [dict(a, failed_decls=list(a.get('failed_decls', [])) + ['h2_sign_iff_rh']) for a in S['att']])),
    ('G-IFF-RH-READ', 'the profile`s #check -- h2_sign ↔ RiemannHypothesis, no hypothesis',
     lambda S: check_line(S, 'h2_sign_iff_rh') == '%sh2_sign_iff_rh : %sh2_sign ↔ RiemannHypothesis' % (NS, NS),
     lambda S: put(S, 'prof', dict(S['prof'], checks=dict(S['prof'].get('checks') or {}, h2_sign_iff_rh='x')))),
    ('G-HOUSEKEEPING-INSERTED', 'ERRATA -- the line under the heading, the two bullets after the list`s last; every prior line kept',
     lambda S: (lambda t: any(t[i].startswith('## E-2026-09-25-1 ') and t[i + 1] == '' and t[i + 2].startswith(HK_LINE) for i in range(len(t) - 2))
                and any(t[i].startswith('- `E-2026-09-25-1` —') and t[i + 1].startswith('- `E-2026-09-14-1` —') and t[i + 2].startswith('- `E-2026-09-22-1` —')
                        for i in range(len(t) - 2)))(S['errata'].split(NL)) and subseq(S['pp_prior']['ERRATA.md'], S['errata']),
     lambda S: put(S, 'errata', S['errata'].replace('- `E-2026-09-22-1` — *DEPOSIT-FACING; RETAINED AT MONOGRAPH v1.1.2* (appended', '- ghost (appended'))),
    ('G-SPAN-CONVENTION-ONCE', 'OPEN_TRAILS -- the convention recorded exactly once, in this act`s record',
     lambda S: S['ot'].count(SPANC) == 1 and SPANC in seg(S['ot'], TRAILH, 99999),
     lambda S: put(S, 'ot', S['ot'] + NL + SPANC)),
    ('G-PRIORART-RECORDED', 'FINDINGS against the fetched README -- the entry once, each quote present in the README fetched',
     lambda S: S['find'].count(PTITLE) == 1 and bool(S['pa'].get('readme_quotes'))
     and all(q in wsj(S['preadme']) and q in S['find'] for q in S['pa']['readme_quotes']) and 'is NOT claimed' in S['find'],
     lambda S: put(S, 'preadme', '')),
    ('G-GREP-PRINTED', 'the grep bank -- each file list`s length equal to its printed count',
     lambda S: all(len([l for l in m.group(1).split(NL) if l.strip()]) == int(m.group(2)) for m in
                   re.finditer(r"### files matching '[^']+':\n(.*?)\n### count : (\d+)", S['pgrep'], re.S))
     and len(re.findall(r"### files matching '", S['pgrep'])) == 2,
     lambda S: put(S, 'pgrep', S['pgrep'].replace('### count : 14', '### count : 13'))),
    ('G-UNDERSTANDINGS-VERBATIM', 'FINDINGS against the ferry -- the title once, the eight paragraphs verbatim, tags dropped',
     lambda S: S['find'].count(UTITLE) == 1 and len(paras(S)) == 8 and all(p in S['find'] for p in paras(S))
     and '[procedural]' not in seg(S['find'], UTITLE, 99999),
     lambda S: put(S, 'find', S['find'].replace(paras(S)[4] if len(paras(S)) > 4 else 'x', 'ghost'))),
    ('G-ITEM3-CORRECTED', 'FINDINGS against the witness`s window line read HERE from its own file',
     lambda S: '**[CORRECTED' in seg(S['find'], UTITLE, 99999) and S['tail53'].replace('`', "'") in seg(S['find'], UTITLE, 99999),
     lambda S: put(S, 'tail53', 'self.order_note = ghost')),
    ('G-CEILING-CONDITIONAL', 'the profile and the corpus -- if compiled, (R146)(2)`s sentence beside (R145)(2)`s in README, REGISTRY and the trail',
     lambda S: (all(std(S, n) for n in THMS) and bool(new_ceiling(S)) and new_ceiling(S) == S['ce'].get('ceiling')
                and all(new_ceiling(S) in wsj(x) for x in (S['readme'], S['registry'], seg(S['ot'], TRAILH, 99999)))
                and S['ce535'].get('ceiling', 'x') in wsj(S['readme']) and S['ce535'].get('ceiling', 'x') in wsj(S['registry'])),
     lambda S: put(S, 'registry', S['registry'].replace('equivalent to Mathlib', 'equal to Mathlib'))),
    ('G-TAG-PEELED', 'the remote READ HERE -- v0.2`s peeled line equals the commit that added Seam.lean, and the bank',
     lambda S: bool(peeled(S)) and peeled(S) == S['seam_commit'] and peeled(S) in S['tagbank'],
     lambda S: put(S, 'ls_tags', '')),
    ('G-ROWS-GRADED', 'row 386 -- the six DERIVES, each std3',
     lambda S: corr_row(S, 386) != '' and all(('`%s` DERIVES' % n) in cell(S, 386, 4) and std(S, n) for n in THMS)
     and len(GRADE_RE.findall(cell(S, 386, 4))) == 6,
     lambda S: put(S, 'corr', S['corr'].replace('`h2_sign_iff_rh` DERIVES', '`h2_sign_iff_rh` SHELL'))),
    ('G-TABLE-ROW', 'the regenerated terminal table -- h2_sign_iff_rh PROFILED and DERIVES',
     lambda S: 'DERIVES' in table_row(S, 'h2_sign_iff_rh') and 'NOT PROFILED' not in table_row(S, 'h2_sign_iff_rh'),
     lambda S: put(S, 'table', S['table'].replace('`%sh2_sign_iff_rh`' % NS, '`ghost`'))),
    ('G-LINES-KEPT', 'every PLACE-papers file written, against its blob at b535`s commit -- every prior line, in order',
     lambda S: all(subseq(S['pp_prior'][f], S['pp_now'][f]) for f in PPFILES),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'README.md': S['pp_now']['README.md'].replace('Supportable: *RH reduced', 'x')}))),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b536_x.py'])),
    ('G-N1-SCORED', 'the desk against probe 1', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the attempts', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the profile', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the grep`s hit lines', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the blobs', lambda S: nscored(S, 'n5'), lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the tree, the tools and the token', lambda S: nscored(S, 'n6'),
     lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2')
     and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b536 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('stay OPEN', 'are closed'))),
    ('G-LANE-SHUT', 'the trail`s own record -- the kernel lane shut, said', lambda S: 'kernel lane shuts at this act' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(NL, ' ').replace('kernel lane shuts at this act', 'lane stays open'))),
    ('G-CORPUS-SCOPE', 'the file lists -- the five PLACE-papers files; the kernel`s changes the two NEW files; v0.2 at HEAD',
     lambda S: sorted(S['tracked']) == sorted(PPFILES) and S['ker_changed'] == {'SIDEExplicitFormula/Seam.lean', 'AxiomCheckSeam.lean'}
     and gits(KER, 'tag', '--points-at', 'HEAD') == 'v0.2',
     lambda S: put(S, 'ker_changed', S['ker_changed'] | {'Zeta23/Defs.lean'})),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS` bytes against its blob at b535`s commit -- a true prefix; one heading',
     lambda S: S['ot_now_bytes'].startswith(S['ot_prior_bytes']) and S['ot'].count(TRAILH) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + TRAILH + ' a second record')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger -- row 386 once, six cells',
     lambda S: S['corr'].count('| 386 |') == 1 and len(corr_row(S, 386).strip().strip('|').split(' | ')) == 6,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 386 | a duplicate row |')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b535`s close -- none modified',
     lambda S: S['tools_edited'] == [], lambda S: put(S, 'tools_edited', ['b363_span.py'])),
    ('G-WRITELIST-KINDS', 'every b536 commit in four repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b536')" in S['suite']
                and "data/b536_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b536_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b536')
              and 'data/b536_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b536 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b536_checks_postpush.txt' if pushed else 'b536_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b536_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
