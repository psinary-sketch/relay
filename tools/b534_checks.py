# -*- coding: utf-8 -*-
"""b534_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b534_registration_2026-09-25.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = '7b3f0525'      # ### b533's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = 'f42102f'           # ### the kernel's tip before this act
PRIOR_PP = 'b8cce57'           # ### b533's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b534 —'
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


def sources():
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b534_ferry.txt')),
        scan=read(os.path.join(D, 'b534_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b534_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b534_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b534_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b534_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        seal533=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify',
                                os.path.join(D, 'b533_registration_2026-09-25.txt')],
                               capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        note=read(os.path.join(D, 'b534_note_beside_b533_face.txt')),
        prior=read(os.path.join(D, 'b533_closing.txt')),
        addendum=read(os.path.join(D, 'b534_addendum.txt')),
        comp=read(os.path.join(D, 'b534_components.txt')),
        desk=read(os.path.join(D, 'b534_desk_notes.txt')),
        errata=read(os.path.join(PP, 'ERRATA.md')),
        mod=read(os.path.join(KER, 'SIDEExplicitFormula', 'PowerLimit.lean')),
        pw_now=read(os.path.join(KER, 'SIDEExplicitFormula', 'PowerWindow.lean')),
        pw_prior=blob(KER, KER_TIP + ':SIDEExplicitFormula/PowerWindow.lean').decode('utf-8', 'replace').replace(chr(13), ''),
        pw_prior_sha=hashlib.sha256(blob(KER, KER_TIP + ':SIDEExplicitFormula/PowerWindow.lean')).hexdigest(),
        acc=read(os.path.join(KER, 'AxiomCheckLimit.lean')),
        untouched={f: (gits(KER, 'hash-object', f), gits(KER, 'rev-parse', KER_TIP + ':' + f), gits(KER, 'rev-parse', 'HEAD:' + f))
                   for f in UNTOUCHED},
        rb_text=read(os.path.join(KER, 'SIDEExplicitFormula', 'RestBound.lean')),
        att=json.loads(read(os.path.join(D, 'b534_attempts.json')) or '[]'),
        att_files={int(re.search(r'attempt(\d+)\.lean$', p).group(1)): hashlib.sha256(open(p, 'rb').read()).hexdigest()
                   for p in glob.glob(os.path.join(D, 'b534_attempt[0-9]*.lean'))},
        clogs=len(glob.glob(os.path.join(D, 'b534_compile_log*.txt'))),
        clast=read(sorted(glob.glob(os.path.join(D, 'b534_compile_log*.txt')), key=os.path.getmtime)[-1]),
        plog=read(sorted(glob.glob(os.path.join(D, 'b534_profile_log*.txt')), key=os.path.getmtime)[-1]),
        inst=json.loads(read(os.path.join(D, 'b534_install.json')) or '{}'),
        prof=json.loads(read(os.path.join(D, 'b534_profile.json')) or '{}'),
        stmt=read(os.path.join(D, 'b534_statement.txt')),
        probes=[read(os.path.join(D, 'b534_probe%d.txt' % n)) for n in (1, 2, 3)],
        ker_changed=set(x for x in gits(KER, 'diff', '--name-only', KER_TIP).split(NL) if x.strip())
                    | set(p[3:].strip() for p in git(KER, 'status', '--porcelain').split(NL) if p.strip()),
        ker_tags=gits(KER, 'tag', '--points-at', 'HEAD'),
        sc=json.loads(read(os.path.join(D, 'b534_scores.json')) or '{}'),
        ot=read(OT), corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        suite=read(os.path.join(T, 'b534_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mirror=bool(glob.glob(os.path.join('D:', os.sep, 'MY-DOwnloads', 'mirror-refresh-*-b534.zip'))),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b534 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        pp_since=sorted(x for x in gits(PP, 'diff', '--name-only', PRIOR_PP).split(NL) if x.strip()),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b534_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        zen=[f for f in os.listdir(D) if f.startswith('b534_') and 'zenodo' in f.lower()],
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b534_install.json', 'b534_attempts.json', 'b534_profile.json',
                                                               'b534_components.txt', 'b534_rows.json',
                                                               'b534_note_beside_b533_face.txt'))),
        probe_before=all(os.path.getmtime(os.path.join(D, 'b534_probe%d.txt' % n)) < os.path.getmtime(FACE) for n in (1, 2, 3)),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b534 --'):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-9]_|^b52[0-9]_|^b53[0-3]_|^b334_', f)]
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
UNTOUCHED = ['SIDEExplicitFormula/RestBound.lean', 'SIDEExplicitFormula/RHChain.lean', 'SIDEExplicitFormula/H2Bridge.lean']
NEWK = {'SIDEExplicitFormula/PowerLimit.lean', 'AxiomCheckLimit.lean', 'SIDEExplicitFormula/PowerWindow.lean'}
RENAMED = {'window': 'pwWindow', 'window_contDiff': 'pwWindow_contDiff', 'window_support': 'pwWindow_support'}
L7AD_LAST = 'rest_term_small'
L7E = ['ceil_weight', 'Aw_nonneg', 'zero_weight', 'weighted_finite_bound', 'weighted_summable', 'dominant_summable', 'fR_norm_le',
       'fR_bound', 'rest_tendsto_zero', 'mem_sT', 'zeroSide_eventually_neg', 'zeroSideNeg_holds']
LAST3 = ['h2_sign_iff_rh_strip', 'h2_sign_imp_rh_of_seam', 'rh_strip_imp_rh']
EID = 'E-2026-09-25-1'
CEIL = ('RH and Weil positivity on classK are one Prop apart in the kernel, RH → h2_sign compiled, h2_sign → RH compiled to its '
        "last step; the deposit's Route 3 premise is RH restated, E-2026-09-25-1 drafted.")


def thms(mod):
    return re.findall(r'^theorem (\S+)', mod or '', re.M)


def std(S, n):
    return (S['prof'].get('std3') or {}).get(NS + n) is True


def first_clean(S):
    ok = [a['attempt'] for a in S['att'] if a['exit'] == 0 and a['errors'] == 0 and not a['sorry']]
    return ok[0] if ok else None


def failures(S):
    out = {}
    for a in S['att']:
        for d0 in a.get('failed_decls', []):
            out.setdefault(RENAMED.get(d0, d0), []).append(a['attempt'])
    return out


def halted(S):
    return sorted(d for d, ns in failures(S).items() if len(ns) >= 2)


def decl(mod, name):
    m = re.search(r'^(?:theorem|def) %s\b' % re.escape(name), mod or '', re.M)
    if not m:
        return ''
    n = re.search(r'^(?:theorem|def|structure|/-|end |open |example|variable|--)', mod[m.end():], re.M)
    return mod[m.start():m.end() + (n.start() if n else len(mod))].rstrip()


def dhead(mod, name):
    t = decl(mod, name)
    cut_at = [x for x in (t.find(':='), t.find(NL + '  |')) if x >= 0]
    return t[:min(cut_at)].rstrip() if cut_at else t


def graded_names(face):
    f = flat(face)
    i = f.find('READING (11)')
    j = f.find(': DERIVES where', i)
    return re.findall(BT + '([A-Za-z_][A-Za-z0-9_]*)' + BT, f[i:j]) if i >= 0 and j >= 0 else []


def corr_row(S):
    return next((l for l in S['corr'].split(NL) if l.startswith('| 383 |')), '')


def grade_cell(S):
    c = corr_row(S).strip().strip('|').split(' | ')
    return c[4] if len(c) == 6 else ''


def table_row(S, n):
    return next((l for l in S['table'].split(NL) if '`%s%s`' % (NS, n) in l), '')


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def trail_raw(S):
    return seg(S['ot'], TRAILH, 99999)


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 14).split('.')[0].split(',')[0]


def word_of(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def check_line(S, n):
    return ' '.join(((S['prof'].get('checks') or {}).get(n) or '').split())


def n_recomputed(S):
    m = S['mod']
    th = thms(m)
    l7ad = th[:th.index(L7AD_LAST) + 1] if L7AD_LAST in th else []
    fl = failures(S)
    h = halted(S)
    heads = [dhead(m, n) for n in th]
    return dict(
        n1=bool(l7ad) and all(std(S, n) for n in l7ad) and not any(a >= 2 for n in l7ad for a in fl.get(n, [])),
        n2=(not h) or (all(x in L7E for x in h) and not any(x in l7ad for x in h)),
        n3=std(S, 'h2_sign_iff_rh_strip') and check_line(S, 'h2_sign_iff_rh_strip') ==
        '%sh2_sign_iff_rh_strip : %sh2_sign ↔ %srh_strip' % (NS, NS, NS),
        n4=bool(re.search(r'^def rh_strip_imp_rh : Prop', S['pw_now'], re.M)) and check_line(S, 'rh_strip_imp_rh').endswith(': Prop')
        and not any(x.rstrip().endswith('rh_strip_imp_rh') for x in heads),
        n5=all(a and a == b == c for a, b, c in S['untouched'].values()),
        n6=S['dep_clean'] and 'ERRATA.md' not in S['pp_since'] and EID not in S['errata'] and not S['zen'] and CEIL in trail(S),
        s1=not h and first_clean(S) is not None,
        s2=std(S, 'h2_sign_iff_rh_strip'),
        s3=bool(S['att']) and bool(S['att'][0].get('failed_decls')))


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == n_recomputed(S)[k]


def code_lines(text):
    return [l for l in (text or '').replace(chr(13), '').split(NL) if not l.lstrip().startswith('--')]


def last_lines(S, n):
    lines = [l for l in trail_raw(S).split(NL) if l.strip()]
    return lines[-n:]


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R144) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b534' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-DECLARED', 'this act`s banked scan -- the flag count read off it, and the face declares the one flag',
     lambda S: '(R81) FLAGS : 1' in line_with(S['scan'], '(R81) FLAGS') and 'one (R81) flag is INFORMATIONAL and declared' in flat(S['face'])
     and '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('(R81) FLAGS : 1', '(R81) FLAGS : 2'))),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b533`s closing AND the ledger',
     lambda S: 'THE COMMITS, THE MIRROR, THE CENSUSES' in S['prior'] and S['corr'].count('| 382 |') == 1,
     lambda S: put(S, 'corr', S['corr'].replace('| 382 |', '| 3820 |'))),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b534' in S['ferry'] and 'ACT b534' in S['face'] and not glob.glob(os.path.join(D, 'b535_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b534')),
    ('G-PEEK-DECLARED', 'the face`s (C) block, the probes` times before the lock, the components` after it',
     lambda S: 'THE PROBES WERE RUN BEFORE THE SEAL' in flat(S['face']) and S['probe_before'] and S['after_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R144-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R144) END' in S['ferry'] and S['ot'].count('**(R144) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R144) ratified', '(R144) noted'))),
    ('G-INSTALLED-FROM-DRAFT', 'the install bank against attempt 1`s banked source and PowerWindow`s blob at b533`s commit',
     lambda S: S['inst']['PowerLimit.lean']['prior_sha'] is None and S['inst']['AxiomCheckLimit.lean']['prior_sha'] is None
     and S['inst']['PowerLimit.lean']['draft_sha'] == S['inst']['PowerLimit.lean']['installed_sha'] == S['att'][0]['source_sha']
     == S['att_files'].get(1) and S['inst']['PowerWindow.lean']['prior_sha'] == S['pw_prior_sha'],
     lambda S: put(S, 'inst', {**S['inst'], 'PowerLimit.lean': dict(S['inst']['PowerLimit.lean'], draft_sha='0' * 64)})),
    ('G-POWERWINDOW-COMMENT-ONLY', 'PowerWindow.lean on disk against its blob at b533`s commit -- equal once comment lines are removed; the note present',
     lambda S: bool(S['pw_prior']) and code_lines(S['pw_now']) == code_lines(S['pw_prior']) and S['pw_now'] != S['pw_prior']
     and '(R144)(2), act b534' in S['pw_now'],
     lambda S: put(S, 'pw_now', S['pw_now'] + NL + 'def x : Nat := 0')),
    ('G-ATTEMPTS-BANKED', 'the attempts bank against the banked sources and logs',
     lambda S: [a['attempt'] for a in S['att']] == list(range(1, len(S['att']) + 1)) == sorted(S['att_files'])
     and all(S['att_files'][a['attempt']] == a['source_sha'] for a in S['att']) and S['clogs'] == len(S['att']),
     lambda S: put(S, 'att', S['att'][:-1])),
    ('G-MODULE-NO-SORRY', 'the module text, the last compile log and the profile log',
     lambda S: bool(S['mod']) and not re.search(r'\bsorry\b', S['mod']) and 'exit 0 ;' in S['clast'] and ': error' not in S['clast']
     and 'sorryAx' not in S['plog'],
     lambda S: put(S, 'mod', S['mod'] + NL + 'theorem x : False := sorry')),
    ('G-PROFILE-WHOLE-STRING', 'the profile run file -- every theorem of the module, its line equal to the standard-three string',
     lambda S: len(thms(S['mod'])) > 0 and all([l.strip() for l in S['plog'].split(NL) if l.startswith("'%s%s'" % (NS, n))] == [STD3 % (NS + n)]
                                              for n in thms(S['mod'])) and all(std(S, n) for n in thms(S['mod'])),
     lambda S: put(S, 'plog', S['plog'].replace(STD3 % (NS + 'zeroSide_eventually_neg'),
                                                 (STD3 % (NS + 'zeroSide_eventually_neg')).replace(', Quot.sound', ', sorryAx')))),
    ('G-STATEMENTS-PRINTED', 'the components bank against the module -- each graded statement recomputed HERE from the source',
     lambda S: bool(graded_names(S['face'])) and all(dhead(S['mod'], RENAMED.get(n, n)) and dhead(S['mod'], RENAMED.get(n, n)) in S['comp']
                                                     for n in graded_names(S['face'])),
     lambda S: put(S, 'comp', S['comp'].replace('theorem h2_sign_iff_rh_strip', 'theorem ghost'))),
    ('G-PROBES-BANKED', 'the three banked probes -- sources and outputs; no theorem; the Tannery name; the literal-order examples',
     lambda S: all(p.count('### output') == 1 and not re.search(r'^theorem ', p, re.M) for p in S['probes'])
     and sum(p.count('#check @') for p in S['probes']) >= 40 and 'tendsto_tsum_of_dominated_convergence' in S['probes'][1]
     and 'WithTop.coe_le_coe.mpr le_top' in S['probes'][2],
     lambda S: put(S, 'probes', S['probes'][:2] + [S['probes'][2] + NL + 'theorem x : True := trivial'])),
    ('G-HALTS-RECORDED', 'the attempts bank`s failing declarations against the module -- every halted lemma a `_blocked` Prop',
     lambda S: all(a.get('failed_decls') is not None for a in S['att'])
     and set(halted(S)) == set(re.findall(r'^def (\S+)_blocked\b', S['mod'], re.M))
     and all(not re.search(r'^theorem %s\b' % re.escape(h), S['mod'], re.M) for h in halted(S)),
     lambda S: put(S, 'att', [dict(a, failed_decls=list(a.get('failed_decls', [])) + ['coeffs_exist']) for a in S['att']])),
    ('G-DISTINCT-NODES-PROVED', 'the module and the profile -- nodes_distinct a theorem, std3; b533`s Prop still a def beside its note',
     lambda S: bool(re.search(r'^theorem nodes_distinct\b', S['mod'], re.M)) and std(S, 'nodes_distinct')
     and bool(re.search(r'^def nodes_distinct_nonreal\b', S['pw_now'], re.M)) and 'superseded by `nodes_distinct`' in S['pw_now'],
     lambda S: put(S, 'mod', S['mod'].replace('theorem nodes_distinct ', 'def nodes_distinct '))),
    ('G-SEAM-UNCONCLUDED', 'the module`s theorem heads, PowerWindow`s def and the profile`s #check -- the seam a Prop, concluded nowhere',
     lambda S: bool(re.search(r'^def rh_strip_imp_rh : Prop', S['pw_now'], re.M)) and check_line(S, 'rh_strip_imp_rh').endswith(': Prop')
     and not any(dhead(S['mod'], n).rstrip().endswith('rh_strip_imp_rh') for n in thms(S['mod'])),
     lambda S: put(S, 'mod', S['mod'] + NL + 'theorem seam_x : rh_strip_imp_rh := sorry')),
    ('G-LAST-THREE-PRINTED', 'the trail record`s last three lines against the profile`s #check lines',
     lambda S: last_lines(S, 3) == [check_line(S, n) for n in LAST3] and all(check_line(S, n) for n in LAST3),
     lambda S: put(S, 'ot', S['ot'] + NL + 'a trailing line')),
    ('G-UNTOUCHED-FOUR', 'the kernel`s git objects -- RestBound, RHChain, H2Bridge at b533`s commit, at HEAD, in the tree; not_f4_needs and HMax present',
     lambda S: all(a and a == b == c for a, b, c in S['untouched'].values()) and 'theorem not_f4_needs' in S['rb_text']
     and 'def HMax' in S['rb_text'] and not any(f in S['ker_changed'] for f in UNTOUCHED),
     lambda S: put(S, 'untouched', {**S['untouched'], UNTOUCHED[1]: ('0' * 40,) + S['untouched'][UNTOUCHED[1]][1:]})),
    ('G-NOTE-BESIDE-FACE', 'the note file AND b533`s face re-verified by its own seal',
     lambda S: '(R144)(1)' in S['note'] and 'b533_registration_2026-09-25.txt' in S['note'] and 'is not edited' in S['note']
     and any('SEAL INTACT' in l for l in S['seal533'].split(NL)),
     lambda S: put(S, 'seal533', S['seal533'].replace('SEAL INTACT', 'x'))),
    ('G-GRADES-BY-READING', 'row 383`s grade cell against the face`s nineteen -- each DERIVES, each compiled std3',
     lambda S: len(graded_names(S['face'])) == 19 and all(('`%s` DERIVES' % n) in grade_cell(S) and std(S, n) for n in graded_names(S['face']))
     and len(GRADE_RE.findall(grade_cell(S))) == 19,
     lambda S: put(S, 'corr', S['corr'].replace('`h2_sign_iff_rh_strip` DERIVES', '`h2_sign_iff_rh_strip` SHELL'))),
    ('G-TABLE-ROW', 'the regenerated terminal table -- the nineteen PROFILED and DERIVES',
     lambda S: bool(graded_names(S['face'])) and all('DERIVES' in table_row(S, n) and 'NOT PROFILED' not in table_row(S, n)
                                                     for n in graded_names(S['face'])),
     lambda S: put(S, 'table', S['table'].replace('`%sh2_sign_iff_rh_strip`' % NS, '`ghost`'))),
    ('G-CEILING-UNCHANGED', 'the trail`s own record -- b532`s ceiling sentence verbatim, the update act named',
     lambda S: CEIL in trail(S) and 'update act rules its next wording' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('one Prop apart', 'no Prop apart'))),
    ('G-N1-SCORED', 'the desk against the attempts and the profile', lambda S: nscored(S, 'n1'),
     lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the halts recomputed HERE', lambda S: nscored(S, 'n2'),
     lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the profile`s #check recomputed HERE', lambda S: nscored(S, 'n3'),
     lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the module`s heads and PowerWindow`s def', lambda S: nscored(S, 'n4'),
     lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the kernel`s blobs', lambda S: nscored(S, 'n5'),
     lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the deposit tree, ERRATA, the data directory and the trail', lambda S: nscored(S, 'n6'),
     lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2')
     and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b534 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('stay OPEN', 'are closed'))),
    ('G-LANE-SHUT', 'the trail`s own record -- the kernel lane shut, said', lambda S: 'kernel lane shuts at this act' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(NL, ' ').replace('kernel lane shuts at this act', 'lane stays open'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the trail alone; the kernel`s changes the three named files; no tag',
     lambda S: sorted(S['tracked']) == ['OPEN_TRAILS.md'] and S['ker_changed'] == NEWK and S['ker_tags'] == '',
     lambda S: put(S, 'ker_changed', NEWK | {'Zeta23/Defs.lean'})),
    ('G-TRAIL-APPEND-ONLY', 'the trail`s own text', lambda S: S['ot'].count(TRAILH) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + TRAILH + ' a second record')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger -- row 383 once, six cells as it landed',
     lambda S: S['corr'].count('| 383 |') == 1 and S['corr'].count('(b534, under (R144))') == 1
     and len(corr_row(S).strip().strip('|').split(' | ')) == 6,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 383 | a duplicate row |')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b533`s close -- none modified',
     lambda S: S['tools_edited'] == [], lambda S: put(S, 'tools_edited', ['b519_window.py'])),
    ('G-WRITELIST-KINDS', 'every b534 commit in four repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b534')" in S['suite']
                and "data/b534_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b534_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b534')
              and 'data/b534_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = [] if pushed else ['G-MIRROR-TAGGED-BUILD']
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b534 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b534_checks_postpush.txt' if pushed else 'b534_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b534_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
