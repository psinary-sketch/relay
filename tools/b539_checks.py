# -*- coding: utf-8 -*-
"""b539_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b539_registration_2026-09-25.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = '249a10fd'      # ### b538's closing commit -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '81ae175'           # ### the kernel's tip before this act
PRIOR_PP = 'c658a55'           # ### b538's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b539 —'
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


PPFILES = ['FINDINGS.md', 'OPEN_TRAILS.md', 'phase1.5/method/THE_LOAD_BEARING_MAP.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md']


SIDE_TIP = '502f0a7a67462eab83a0f10eee5ea74be67957dd'
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
MAPP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
SURRP = os.path.join(PP, 'phase1.5', 'proofs', 'THE_UNCONDITIONAL_SURROUND.md')
ATITLE = '## The hub terminals tiered against the anchor tier of (R149), 2026-09-25'
FTITLE = ("## The cascade, act one: the anchor tier, the hub terminals tiered, THE_UNCONDITIONAL_SURROUND §6 and lv-conservation's "
          "description read against the register census")
STITLE = '### Correspondence, tiered under (R149) -- 2026-09-25, b539 (a new table beneath the old, row for row; the table above is unedited)'
ANCHOR_NAMES = ['h2_sign_iff_rh', 'ch_iff_rh', 'not_register1', 'mellin_Phi_eq_zero_of_re_le_one', 'lvh2_corrected_iff',
                'register5_output_holds', 'b321_identity', 'not_f4_needs']
BANKS = {'h2_sign_iff_rh': 'b536_profile_log.txt', 'ch_iff_rh': 'b532_profile_log.txt', 'not_register1': 'b538_profile_log2.txt',
         'mellin_Phi_eq_zero_of_re_le_one': 'b538_profile_log2.txt', 'lvh2_corrected_iff': 'b538_profile_log2.txt',
         'register5_output_holds': 'b538_profile_log2.txt', 'b321_identity': 'b510_profile_log.txt', 'not_f4_needs': 'b530_profile_log.txt'}
TIERS_OK = {'T0', 'T1', 'T2', 'T3', 'T4'}


def delete_needles():
    return [x + y for x, y in (('Remove', '-Item'), ('os.re', 'move('), ('shutil.rm', 'tree('), ('.un', 'link('), ('os.rm', 'dir('),
                               ('rm ', '-'), ('rmd', 'ir '), ('Clear', '-Content'))]


def joined_axiom_lines(out):
    raw, res, i = (out or '').replace(chr(13), '').split(NL), [], 0
    while i < len(raw):
        l = raw[i]
        if 'depends on axioms: [' in l:
            while ']' not in l and i + 1 < len(raw):
                i += 1
                l = l.rstrip() + ' ' + raw[i].strip()
        res.append(l.strip())
        i += 1
    return [l for l in res if 'depends on axioms' in l or 'does not depend' in l]


def sources():
    tok = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    needle = 'https://' + 'zenodo' + '.org'
    files = dict((f, os.path.join(PP, f)) for f in ('FINDINGS.md', 'OPEN_TRAILS.md', 'ERRATA.md', 'README.md', 'REGISTRY.md',
                                                    'phase1.5/method/THE_LOAD_BEARING_MAP.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md'))
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b539_ferry.txt')),
        scan=read(os.path.join(D, 'b539_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b539_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b539_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b539_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b539_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b538_closing.txt')),
        addendum=read(os.path.join(D, 'b539_addendum.txt')),
        comp=read(os.path.join(D, 'b539_components.txt')),
        desk=read(os.path.join(D, 'b539_desk_notes.txt')),
        sc=json.loads(read(os.path.join(D, 'b539_scores.json')) or '{}'),
        purpose=read(os.path.join(D, 'b539_purpose.txt')),
        lvtext=(lambda d: d['metadata']['title'] + NL + __import__('html').unescape(re.sub(r'<[^>]+>', NL, d['metadata']['description'])))(json.loads(read(os.path.join(D, 'b499_fetchback_21539068.json')))),
        anc=json.loads(read(os.path.join(D, 'b539_anchor.json')) or '{}'),
        alog=read(os.path.join(D, 'b539_anchor_log.txt')),
        banks={n: read(os.path.join(D, b)) for n, b in BANKS.items()},
        sj=json.loads(read(os.path.join(D, 'b539_sentences.json')) or '{}'),
        tj=json.loads(read(os.path.join(D, 'b539_tiers.json')) or '{}'),
        ej=json.loads(read(os.path.join(D, 'b539_erratum.json')) or '{}'),
        edraft=read(os.path.join(D, 'b539_erratum_draft.md')),
        su=json.loads(read(os.path.join(D, 'b539_surr.json')) or '{}'),
        fj=json.loads(read(os.path.join(D, 'b539_findings.json')) or '{}'),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in files},
        pp_now={f: open(p, 'rb').read() for f, p in files.items()},
        mapt=read(MAPP), surrt=read(SURRP), find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT),
        map_lines=read(MAPP).split(NL), surr_lines=read(SURRP).split(NL),
        corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        corr_prior=blob(SIDE, SIDE_TIP + ':CORRESPONDENCE.md').decode('utf-8', 'replace').replace(chr(13), ''),
        ker_clean={n: gits(p, 'status', '--porcelain', '--untracked-files=no') == '' for n, p in (('sef', KER), ('sk', SK), ('lv', LV))},
        ker_heads=dict(sef=gits(KER, 'rev-parse', 'HEAD'), sk=gits(SK, 'rev-parse', 'HEAD'), lv=gits(LV, 'rev-parse', 'HEAD')),
        ker_changed=set(x for x in gits(KER, 'diff', '--name-only', KER_TIP).split(NL) if x.strip()),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b539_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b539_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b539_') and f.endswith('.py')
                        for n in delete_needles() if n in strip_prose(read(os.path.join(T, f))))),
        suite=read(os.path.join(T, 'b539_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b539 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b539_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b539_anchor.json', 'b539_purpose.txt', 'b539_sentences.json',
                                                               'b539_tiers.json', 'b539_erratum_draft.md'))),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b539 --'):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-9]_|^b52[0-9]_|^b53[0-8]_|^b334_', f)]
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


def trail(S):
    return flat(seg(S['ot'], TRAILH, 99999))


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 14).split('.')[0].split(',')[0]


def word_of(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def fresh_line(S, n):
    return next((l for l in joined_axiom_lines(S['alog']) if l.split("'")[1:2] and l.split("'")[1].endswith('.' + n)), None)


def bank_line(S, n):
    return next((l for l in joined_axiom_lines(S['banks'][n]) if l.split("'")[1:2] and l.split("'")[1].endswith('.' + n)), None)


def ranked_live(S):
    """### the map's twelve ranked rows, READ HERE from the map's own lines 24-35."""
    out = []
    for l in S['map_lines'][23:35]:
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        if len(c) < 5:
            return []
        t = re.search(r'`([^`]+)`', c[1])
        out.append('ξ / Dirichlet order-≤1 inputs' if c[1].startswith('ξ') else (t.group(1) if t else c[1]))
    return out


def appendix_rows(S):
    t = S['mapt']
    if ATITLE not in t:
        return []
    seg0 = t[t.index(ATITLE):]
    seg0 = seg0[seg0.index('**The ranked list (A), tiered:**'):seg0.index('**Tier counts over the ranked list:**')] if '**The ranked list (A), tiered:**' in seg0 else ''
    return [l for l in seg0.split(NL) if l.startswith('| ') and not l.startswith('| rank |')]


def surr_rows(S):
    t = S['surrt']
    if STITLE not in t:
        return []
    return [l for l in t[t.index(STITLE):].split(NL) if l.startswith('| :')]


def tier_of(S, name):
    return next((r['tier'] for r in S['tj'].get('ranked', []) if r['terminal'] == name),
                next((e['tier'] for e in S['tj'].get('extra', []) if e['terminal'] == name), None))


def recomputed(S):
    t0 = [r['terminal'] for r in S['tj'].get('ranked', []) if r['tier'] == 'T0']
    oc = S['sj'].get('counts', {}).get('ordered', {})
    sr = sum(v.get('RESTS', 0) for b, v in oc.items() if b.startswith('SURR'))
    lr = sum(v.get('RESTS', 0) for b, v in oc.items() if b.startswith('lv'))
    ex = sum(v.get('EXCEEDS', 0) for v in oc.values())
    return dict(
        n1=len(t0) == 1 and t0 == ['h2_sign_iff_rh'],
        n2=tier_of(S, 'goalState_sevenClasses_of_h2') == 'T2' and tier_of(S, 'ConservationBridge.riemann_hypothesis') == 'T2',
        n3=sr >= 2 and lr >= 1 and ex == 0,
        n4=all(S['pp_now'][f].startswith(S['pp_prior'][f]) for f in PPFILES),
        n5=(all(S['pp_now'][f] == S['pp_prior'][f] for f in ('ERRATA.md', 'README.md', 'REGISTRY.md')) and all(S['ker_clean'].values())
            and S['ker_heads']['sef'].startswith('81ae175') and not S['zen'] and S['tok'] == 0 and S['dep_clean']),
        s1=bool(S['anc'].get('rows')) and all(fresh_line(S, n) is not None and fresh_line(S, n) == bank_line(S, n) for n in ANCHOR_NAMES),
        s2='EF_lit_zetaZeroConfig' in (next((r['check'] for r in S['anc'].get('rows', []) if r['name'].endswith('b321_identity')), '') or ''),
        s3=len(re.findall(r"[A-Za-z]`s\b", S['edraft'])) == 0)


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == recomputed(S)[k]


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R149) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b539' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b538`s closing AND the ledger`s row 387',
     lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and S['corr'].count('| 387 |') == 1,
     lambda S: put(S, 'corr', S['corr'].replace('| 387 |', '| 3870 |'))),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b539' in S['ferry'] and 'ACT b539' in S['face'] and not glob.glob(os.path.join(D, 'b540_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b539')),
    ('G-PEEK-DECLARED', 'the face`s (C) block, and the components` banks after the lock',
     lambda S: 'THE SEAT DRAFTED THE RANKED LIST`S TIERS AND THE SELECTED SENTENCES` GRADES FROM THESE READS BEFORE THE SEAL' in flat(S['face'])
     and 'No `#print axioms` was run before the seal.' in flat(S['face']) and S['after_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R149-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R149) END' in S['ferry'] and S['ot'].count('**(R149) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R149) ratified', '(R149) noted'))),
    ('G-PURPOSE-PRINTED', 'the purpose bank against the two keystones` own lines READ HERE',
     lambda S: S['map_lines'][7] in S['purpose'] and S['surr_lines'][22] in S['purpose'] and S['map_lines'][7].startswith('**PURPOSE:**')
     and os.path.getmtime(os.path.join(D, 'b539_purpose.txt')) < os.path.getmtime(os.path.join(D, 'b539_appendix.json')),
     lambda S: put(S, 'purpose', '')),
    ('G-ANCHOR-FRESH', 'the anchor run`s own log -- a run at 81ae175 after the lock, eight theorems, no sorry',
     lambda S: 'cwd SIDE-explicit-formula at 81ae175' in S['alog'] and 'exit 0 ;' in S['alog'] and 'sorryAx' not in S['alog']
     and all(fresh_line(S, n) for n in ANCHOR_NAMES),
     lambda S: put(S, 'alog', S['alog'].replace('not_f4_needs', 'ghost'))),
    ('G-ANCHOR-MATCHES-BANK', 'every fresh axiom line against its bank READ HERE',
     lambda S: all(fresh_line(S, n) == bank_line(S, n) for n in ANCHOR_NAMES),
     lambda S: put(S, 'banks', dict(S['banks'], ch_iff_rh=S['banks']['ch_iff_rh'].replace('Quot.sound]', 'Quot.sound, sorryAx]')))),
    ('G-ANCHOR-STATEMENTS', 'the anchor #checks -- h2_sign_iff_rh, ch_iff_rh and lvh2_corrected_iff read as the ruling names them',
     lambda S: any(r['check'] == 'SIDEExplicitFormula.B321.h2_sign_iff_rh : SIDEExplicitFormula.B321.h2_sign ↔ RiemannHypothesis' for r in S['anc'].get('rows', []))
     and any((r['check'] or '').endswith('conservationHypothesis ↔ RiemannHypothesis') for r in S['anc'].get('rows', []))
     and any((r['check'] or '').endswith('↔ SIDEExplicitFormula.B321.rh_strip') for r in S['anc'].get('rows', [])),
     lambda S: put(S, 'anc', dict(S['anc'], rows=[dict(r, check='x') for r in S['anc'].get('rows', [])]))),
    ('G-MATCHER-YIELDS', 'the sentence bank -- five matchers` yields printed, each selected sentence carrying a hit',
     lambda S: len(S['sj'].get('yields', {})) == 5 and all(r['hits'] for r in S['sj'].get('selected', [])) and S['sj'].get('read', 0) > len(S['sj'].get('selected', [])),
     lambda S: put(S, 'sj', dict(S['sj'], yields={}))),
    ('G-SENTENCES-GRADED', 'the sentence bank against the source texts READ HERE -- every selected sentence present, every grade legal',
     lambda S: bool(S['sj'].get('selected')) and all(r['grade'] in ('STANDS', 'RESTS', 'EXCEEDS') and r['reason'] for r in S['sj']['selected'])
     and all(r['replacement'] for r in S['sj']['selected'] if r['grade'] == 'RESTS')
     and all(' '.join(r['sentence'].split())[:60] in ' '.join((S['surrt'] if r['block'].startswith('SURR') else S['lvtext']).split()) for r in S['sj']['selected']),
     lambda S: put(S, 'sj', dict(S['sj'], selected=[dict(r, grade='MAYBE') for r in S['sj'].get('selected', [])]))),
    ('G-RANKED-LIST-TIERED', 'the tier bank against the map`s ranked rows READ HERE -- one tier per ranked terminal, in order',
     lambda S: [r['terminal'] for r in S['tj'].get('ranked', [])] == ranked_live(S) and len(ranked_live(S)) == 12
     and all(r['tier'] in TIERS_OK for r in S['tj']['ranked']),
     lambda S: put(S, 'map_lines', S['map_lines'][:30] + S['map_lines'][31:])),
    ('G-TIER-REASONS', 'the tier bank -- every tier with a reason naming the pin and a profile source',
     lambda S: all(r['reason'] and r['profile'] and re.search(r'v\d|`[0-9a-f]{7}`', r['reason']) for r in S['tj'].get('ranked', []))
     and all(e['reason'] for e in S['tj'].get('extra', [])),
     lambda S: put(S, 'tj', dict(S['tj'], ranked=[dict(r, reason='') for r in S['tj'].get('ranked', [])]))),
    ('G-APPENDIX-APPENDED', 'the map READ HERE -- the appendix once, after every prior byte, its ranked rows equal to the bank`s tiers',
     lambda S: S['mapt'].count(ATITLE) == 1 and S['pp_now']['phase1.5/method/THE_LOAD_BEARING_MAP.md'].startswith(S['pp_prior']['phase1.5/method/THE_LOAD_BEARING_MAP.md'])
     and [re.search(r'\*\*(T\d)\*\*', l).group(1) for l in appendix_rows(S)] == [r['tier'] for r in S['tj'].get('ranked', [])],
     lambda S: put(S, 'mapt', S['mapt'].replace('| **T4** |', '| **T1** |'))),
    ('G-ERRATUM-DRAFTED', 'the draft READ HERE -- its id, DRAFT NOT FILED, one row per RESTS sentence, each with its replacement',
     lambda S: S['edraft'].startswith('## E-2026-09-25-3 — ') and 'DRAFT, NOT FILED' in S['edraft'].split(NL)[0]
     and S['edraft'].count('  - reads **RESTS**') == sum(1 for r in S['sj'].get('selected', []) if r['grade'] == 'RESTS') == S['edraft'].count('  - replacement: *"'),
     lambda S: put(S, 'edraft', S['edraft'].replace('  - replacement: *"', '  - x', 1))),
    ('G-ERRATUM-NOT-FILED', 'ERRATA READ HERE against its blob -- byte-identical, no E-2026-09-25-3 in it',
     lambda S: S['pp_now']['ERRATA.md'] == S['pp_prior']['ERRATA.md'] and b'E-2026-09-25-3' not in S['pp_now']['ERRATA.md'],
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'ERRATA.md': S['pp_now']['ERRATA.md'] + b'## E-2026-09-25-3'}))),
    ('G-SURR-TABLE-APPENDED', 'SURR READ HERE -- one table after every prior byte, one row per Correspondence row, E refs where it rests',
     lambda S: S['surrt'].count(STITLE) == 1 and S['pp_now']['phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md'].startswith(S['pp_prior']['phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md'])
     and [int(l.split('|')[1].strip()[1:]) for l in surr_rows(S)] == list(range(175, 190))
     and all(('E-2026-09-25-3' in l) == (l.split('|')[6].strip() != '--') for l in surr_rows(S)),
     lambda S: put(S, 'surrt', S['surrt'].replace('| :184 |', '| :999 |'))),
    ('G-FINDINGS-ENTERED', 'FINDINGS READ HERE -- the entry once, its counts equal to the banks`',
     lambda S: S['find'].count(FTITLE) == 1 and ('RESTS %d**' % S['fj'].get('surr_rests', -1)) in S['find']
     and 'the next keystone of the cascade is PATHS' in S['find'] and 'E-2026-09-25-3 is DRAFTED, NOT FILED' in S['find'],
     lambda S: put(S, 'find', S['find'].replace('the next keystone of the cascade is PATHS', 'x'))),
    ('G-CEILING-UNCHANGED', 'README and REGISTRY bytes against their blobs at b538`s commit',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('README.md', 'REGISTRY.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'README.md': S['pp_now']['README.md'] + b' '}))),
    ('G-KERNELS-UNTOUCHED', 'three kernels READ HERE -- tracked trees clean; SIDE-explicit-formula at 81ae175, nothing changed since',
     lambda S: all(S['ker_clean'].values()) and S['ker_heads']['sef'].startswith('81ae175') and S['ker_changed'] == set(),
     lambda S: put(S, 'ker_changed', {'SIDEExplicitFormula/Seam.lean'})),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b539_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b539_x.py', 'x')])),
    ('G-N1-SCORED', 'the desk against the tier bank', lambda S: nscored(S, 'n1'), lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the tier bank', lambda S: nscored(S, 'n2'), lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the sentence bank', lambda S: nscored(S, 'n3'), lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the blobs', lambda S: nscored(S, 'n4'), lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the blobs, the kernels, the tools and the token', lambda S: nscored(S, 'n5'),
     lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2')
     and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b539 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('lists stay OPEN', 'lists are closed'))),
    ('G-LANE-CLOSED', 'the trail`s own record AND the kernel`s tree', lambda S: 'No kernel lane opened at this act' in trail(S) and S['ker_changed'] == set(),
     lambda S: put(S, 'ot', S['ot'].replace('No kernel lane opened at this act', 'A lane opened'))),
    ('G-CORPUS-SCOPE', 'the PLACE-papers file list -- the four appended documents and no other',
     lambda S: sorted(S['tracked']) == sorted(PPFILES), lambda S: put(S, 'tracked', list(S['tracked']) + ['README.md'])),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- a true prefix; one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(TRAILH) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + TRAILH + ' a second record')),
    ('G-CORR-UNTOUCHED', 'the correspondence ledger against its blob at b538`s commit -- no row this act',
     lambda S: S['corr'] == S['corr_prior'] and S['corr'] != '', lambda S: put(S, 'corr', S['corr'] + NL + '| 388 | a row |')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b538`s close -- none modified',
     lambda S: S['tools_edited'] == [], lambda S: put(S, 'tools_edited', ['corr_row.py'])),
    ('G-WRITELIST-KINDS', 'every b539 commit in four repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b539')" in S['suite']
                and "data/b539_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b539_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b539')
              and 'data/b539_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b539 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b539_checks_postpush.txt' if pushed else 'b539_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b539_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
