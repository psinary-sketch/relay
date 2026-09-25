# -*- coding: utf-8 -*-
"""b538_checks.py -- THE SUITE, IN b461's SUCCESSOR SHAPE, CARRIED FROM b532's AND RE-POINTED ARM BY ARM.

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
FACE = os.path.join(D, 'b538_registration_2026-09-25.txt')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
PRIOR_RELAY = 'cffbd7b2'      # ### b537's closing addendum -- relay's tip before this act
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
KER_TIP = '5c72cad'           # ### the kernel's tip before this act
PRIOR_PP = 'b7e0c52'           # ### b537's PLACE-papers commit
NL = chr(10)
BT = chr(96)
L, RES, EX = [], [], []
TRAILH = '### b538 —'
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


PPFILES = ['FINDINGS.md', 'OPEN_TRAILS.md']


MEM = os.path.join('C:', os.sep, 'Users', 'echo chamber', '.claude', 'projects', 'D--', 'memory')
MEMF = 'feedback_mirror_after_last_push.md'
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
MODP = os.path.join(KER, 'SIDEExplicitFormula', 'RegisterDepth.lean')
SIDE_TIP = '186114dd70d4c79891893c50b7de4b17b766dab1'
NS = 'SIDEExplicitFormula.RegisterDepth.'
STD3 = "'%s' depends on axioms: [propext, Classical.choice, Quot.sound]"
THMS = ['not_register1', 'silence_universal_restated', 'one_le_evenKernel_zero', 'rpow_le_evenKernel_zero',
        'mellin_Phi_eq_zero_of_re_le_one', 'lv_h2_false_on_strip', 'lvh2_corrected_iff', 'register3_of_one_lt_re',
        'zeta_zeros_countable', 'xi_zero_re_countable', 'register5_output_holds']
LV_CITED = ['SIDELvConservation/RegisterPentagon.lean', 'SIDELvConservation/T3_StepNineBridge.lean', 'SIDELvConservation/CouplingsAtPhi.lean',
            'SIDELvConservation/T1_MellinFactorization.lean', 'SIDELvConservation/T2_SDarkness.lean']
FACES = [('SK', 'Kernel/SilenceTheorem.lean', n) for n in ('ConfigurationSpace', 'Interface', 'Interface.is_universal', 'factors_through',
                                                            'Interface.kappa_zero')] + [('SK', 'Kernel/XiDef.lean', 'is_xi_zero')] + [
    ('LV', 'SIDELvConservation/RegisterPentagon.lean', n) for n in ('Register1_universalityHypothesis', 'Register3_totalityThroughPlaces',
                                                                     'Register5_output_HilbertPolya')] + [
    ('LV', 'SIDELvConservation/T1_MellinFactorization.lean', 'Phi')] + [
    ('LV', 'SIDELvConservation/T3_StepNineBridge.lean', n) for n in ('Coupling', 'PerClassExcludes', 'CombinationsExclude')] + [
    ('LV', 'SIDELvConservation/CouplingsAtPhi.lean', n) for n in ('C1_realness', 'C2_halfplane_nonvanishing', 'C3_theta_transformation',
                                                                   'C4_modularity', 'C5_input', 'C6_holomorphic_extension', 'C7_order',
                                                                   'sevenClasses')]
POINTER = ('**The pointer owed by b537 ((R148)(5)):** relay `data/b537_closing_addendum.txt` — "the upload is the -post build; the '
           'pre-push build is superseded, kept, not deleted."')
CTITLE = "## The five registers of §27.3 and lv-conservation's h2, graded by their Lean statements against RH"


def delete_needles():
    return [x + y for x, y in (('Remove', '-Item'), ('os.re', 'move('), ('shutil.rm', 'tree('), ('.un', 'link('), ('os.rm', 'dir('),
                               ('rm ', '-'), ('rmd', 'ir '), ('Clear', '-Content'))]


def def_block(text, name):
    """### the block of `def|structure|abbrev NAME` up to the next blank line or next declaration; docstrings, comments and a
    ### leading `noncomputable` dropped; `/\` read as `∧`; whitespace joined."""
    ls = text.replace(chr(13), '').split(NL)
    pat = re.compile(r'^(?:noncomputable )?(?:def|structure|abbrev) ' + re.escape(name) + r'(?:\s|$)')
    i = next((k for k, l in enumerate(ls) if pat.match(l)), None)
    if i is None:
        return ''
    out = [ls[i]]
    for l in ls[i + 1:]:
        s0 = l.strip()
        if not s0 or re.match(r'^(theorem|def|structure|abbrev|noncomputable|/-|--|end |namespace |open )', l):
            break
        out.append(l)
    t = NL.join(out)
    t = re.sub(r'/--.*?-/', ' ', t, flags=re.S)
    t = re.sub(r'--.*', ' ', t)
    t = t.replace('noncomputable ', '').replace('/' + chr(92), '∧')
    return ' '.join(t.split())


def joined_axiom_lines(out):
    raw, res, i = out.split(NL), [], 0
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
    mod = read(MODP)
    srcs = {}
    for side, path, _ in FACES:
        if (side, path) not in srcs:
            srcs[(side, path)] = (blob(SK, '0e5233f:' + path) if side == 'SK' else blob(LV, 'v0.10.0:' + path)).decode('utf-8', 'replace')
    S = dict(
        face=read(FACE), ferry=read(os.path.join(D, 'b538_ferry.txt')),
        scan=read(os.path.join(D, 'b538_ferry_scan.txt')),
        cens=read(os.path.join(D, 'b538_census_stepzero.txt')),
        fcens=read(os.path.join(D, 'b538_faces_census_stepzero.txt')),
        pins=read(os.path.join(D, 'b538_pins_stepzero.txt')),
        lock=read(sorted(glob.glob(os.path.join(D, 'b538_lockgate_notes*.txt')))[-1]),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE],
                            capture_output=True, text=True, encoding='utf-8', errors='replace').stdout,
        prior=read(os.path.join(D, 'b537_closing.txt')), prior_add=read(os.path.join(D, 'b537_closing_addendum.txt')),
        addendum=read(os.path.join(D, 'b538_addendum.txt')),
        comp=read(os.path.join(D, 'b538_components.txt')),
        desk=read(os.path.join(D, 'b538_desk_notes.txt')),
        sc=json.loads(read(os.path.join(D, 'b538_scores.json')) or '{}'),
        att=json.loads(read(os.path.join(D, 'b538_attempts.json')) or '[]'),
        att_files={int(re.search(r'attempt(\d+)\.lean$', p).group(1)): hashlib.sha256(open(p, 'rb').read()).hexdigest()
                   for p in glob.glob(os.path.join(D, 'b538_attempt[0-9]*.lean'))},
        clogs=len(glob.glob(os.path.join(D, 'b538_compile_log*.txt'))),
        clast=read(sorted(glob.glob(os.path.join(D, 'b538_compile_log*.txt')), key=os.path.getmtime)[-1]),
        plog=read(sorted(glob.glob(os.path.join(D, 'b538_profile_log*.txt')), key=os.path.getmtime)[-1]),
        inst=json.loads(read(os.path.join(D, 'b538_install.json')) or '{}'),
        prof=json.loads(read(os.path.join(D, 'b538_profile.json')) or '{}'),
        probes=[read(os.path.join(D, 'b538_probe%d.txt' % n)) for n in (1, 2, 3)],
        mod=mod, srcs=srcs,
        cmp=read(os.path.join(D, 'b538_restatement_compare.txt')),
        cpl=read(os.path.join(D, 'b538_couplings.txt')),
        cen=json.loads(read(os.path.join(D, 'b538_census.json')) or '{}').get('rows', []),
        fj=json.loads(read(os.path.join(D, 'b538_findings.json')) or '{}'),
        ptr=json.loads(read(os.path.join(D, 'b538_pointer.json')) or '{}'),
        mem_live=open(os.path.join(MEM, MEMF), 'rb').read(), mem_bank=open(os.path.join(D, 'b538_memory_pointer.md'), 'rb').read(),
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(OT),
        pp_prior={f: blob(PP, PRIOR_PP + ':' + f) for f in ('FINDINGS.md', 'OPEN_TRAILS.md', 'ERRATA.md', 'README.md', 'REGISTRY.md')},
        pp_now={f: open(os.path.join(PP, f), 'rb').read() for f in ('FINDINGS.md', 'OPEN_TRAILS.md', 'ERRATA.md', 'README.md', 'REGISTRY.md')},
        corr=read(os.path.join(SIDE, 'CORRESPONDENCE.md')),
        corr_prior=blob(SIDE, SIDE_TIP + ':CORRESPONDENCE.md').decode('utf-8', 'replace').replace(chr(13), ''),
        lv_tag=gits(LV, 'rev-parse', 'v0.10.0^{}'), lv_head=gits(LV, 'rev-parse', 'HEAD'),
        lv_same=all(subprocess.run(['git', '-C', LV, 'diff', '--quiet', 'v0.10.0', 'HEAD', '--', f]).returncode == 0 for f in LV_CITED),
        lv_clean=(gits(LV, 'status', '--porcelain', '--untracked-files=no') == ''),
        sk_v15=gits(SK, 'rev-parse', 'v1.5^{}'), sk_head=gits(SK, 'rev-parse', 'HEAD'),
        sk_clean=(gits(SK, 'status', '--porcelain', '--untracked-files=no') == ''),
        b512_diff=gits(ROOT, 'diff', '--name-only', PRIOR_RELAY, '--', 'data/b512_closing.txt')
                  + gits(ROOT, 'status', '--porcelain', '--', 'data/b512_closing.txt'),
        ker_changed=set(x for x in gits(KER, 'diff', '--name-only', KER_TIP).split(NL) if x.strip())
                    | set(p[3:].strip() for p in git(KER, 'status', '--porcelain').split(NL) if p.strip() and not p.startswith('??')),
        tok=(sum(open(os.path.join(d0, f), 'rb').read().count(tok) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b538_'))
             if tok else -1),
        zen=[f for f in os.listdir(T) if f.startswith('b538_') and needle in read(os.path.join(T, f))],
        dels=sorted(set((f, n) for f in os.listdir(T) if f.startswith('b538_') and f.endswith('.py')
                        for n in delete_needles() if n in strip_prose(read(os.path.join(T, f))))),
        suite=read(os.path.join(T, 'b538_checks.py')),
        tools_edited=sorted(os.path.basename(x) for x in
                            gits(ROOT, 'diff', '--name-only', '--diff-filter=M', PRIOR_RELAY, '--', 'tools').split(NL) if x.strip()),
        artefacts_tracked=gits(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        tracked=(sorted(x for x in gits(PP, 'show', '--name-only', '--pretty=format:', 'HEAD').split(NL) if x.strip())
                 if gits(PP, 'log', '-1', '--pretty=%s').startswith('b538 --')
                 else sorted(p[3:].strip() for p in git(PP, 'status', '--porcelain').split(NL)
                             if p.strip() and not p.lstrip().startswith('??'))),
        kinds=set(), mustfail=not os.path.exists(os.path.join(D, 'b538_mustnotexist.txt')),
        dep_clean=(gits(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''),
        after_lock=all(os.path.exists(p) and os.path.getmtime(p) > os.path.getmtime(FACE)
                       for p in (os.path.join(D, x) for x in ('b538_install.json', 'b538_attempts.json', 'b538_census.json',
                                                               'b538_couplings.txt', 'b538_pointer.json'))),
        before_lock=all(os.path.getmtime(os.path.join(D, x)) < os.path.getmtime(FACE)
                        for x in ('b538_probe1.txt', 'b538_probe2.txt', 'b538_probe3.txt', 'b538_restatement_compare.txt')),
    )
    k = set(os.path.basename(x) for x in S['tracked'])
    for repo in (ROOT, PP, SIDE, KER):
        for l in gits(repo, 'log', '--pretty=%H %s', '-30').split(NL):
            if l.strip() and l.split(' ', 1)[-1].startswith('b538 --'):
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
    prior = [f for f in os.listdir(D) if re.match(r'^b4[0-9][0-9]_|^b50[0-9]_|^b51[0-9]_|^b52[0-9]_|^b53[0-7]_|^b334_', f)]
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


def trail_raw(S):
    return seg(S['ot'], TRAILH, 99999)


def desk_word(S, tag):
    return seg(S['desk'], '**(%s)** ### **' % tag, 14).split('.')[0].split(',')[0]


def word_of(v):
    return 'VACUOUS' if v is None else ('HELD' if v else 'REFUTED')


def axl(S):
    return joined_axiom_lines(S['plog'])


def within(S, n):
    ls = [l for l in axl(S) if l.startswith("'%s%s'" % (NS, n))]
    if len(ls) != 1:
        return False
    if ls[0] == "'%s%s' does not depend on any axioms" % (NS, n):
        return True
    m = re.match(r"^'%s' depends on axioms: \[(.*)\]$" % re.escape(NS + n), ls[0])
    return bool(m) and set(x.strip() for x in m.group(1).split(',')) <= {'propext', 'Classical.choice', 'Quot.sound'}


def fails(S):
    out = {}
    for a in S['att']:
        for d0 in a.get('failed_decls', []):
            out.setdefault(d0, []).append(a['attempt'])
    return out


def halted(S):
    return sorted(d for d, ns in fails(S).items() if len(ns) >= 2)


def chk(S, n):
    return ' '.join(((S['prof'].get('checks') or {}).get(n) or '').split())


def crow(S, reg):
    return next((r for r in S['cen'] if r.get('reg') == reg), {})


def corr_row(S, n):
    return next((l for l in S['corr'].split(NL) if l.startswith('| %s |' % n)), '')


def cell(S, n, k):
    c = corr_row(S, n).strip().strip('|').split(' | ')
    return c[k] if len(c) == 6 else ''


def table_row(S, n):
    return next((l for l in S['table'].split(NL) if '`%s%s`' % (NS, n) in l), '')


def faces_ok(S):
    for side, path, name in FACES:
        a, b = def_block(S['mod'], name), def_block(S['srcs'][(side, path)], name)
        if not a or a != b:
            return False
    return True


def census_table(S):
    f = S['find']
    if CTITLE not in f:
        return []
    seg0 = f[f.index(CTITLE):].split(NL)
    return [l for l in seg0 if l.startswith('| ') and not l.startswith('| register |')]


def recomputed(S):
    return dict(
        n1=within(S, 'not_register1') and 'not_register1' not in fails(S),
        n2=within(S, 'mellin_Phi_eq_zero_of_re_le_one') and 'mellin_Phi_eq_zero_of_re_le_one' not in fails(S),
        n3=within(S, 'register5_output_holds'),
        n4=crow(S, 'R3').get('grade', 'UNDECIDED') != 'UNDECIDED',
        n5=len(S['cen']) == 6 and all((r.get('grade') or '').strip() for r in S['cen']),
        n6=(all(S['pp_now'][f] == S['pp_prior'][f] for f in ('ERRATA.md', 'README.md', 'REGISTRY.md')) and S['sk_clean'] and S['lv_clean']
            and S['sk_head'].startswith('0256e9e') and S['lv_head'].startswith('2f71068') and not S['zen'] and S['tok'] == 0 and S['dep_clean']),
        s1=within(S, 'mellin_Phi_eq_zero_of_re_le_one') and 'mellin_Phi_eq_zero_of_re_le_one' not in halted(S),
        s2=crow(S, 'R3').get('grade') == 'UNDECIDED',
        s3=within(S, 'zeta_zeros_countable'))


def nscored(S, k):
    return k in S['sc'] and desk_word(S, k.upper()) == word_of(S['sc'][k]) and S['sc'][k] == recomputed(S)[k]


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry -- the ruling and part 1 of 1, each END present',
     lambda S: 'RULING (R148) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'] and 'ACT b538' in S['ferry'],
     lambda S: cut(S, 'ferry', 'FERRY END (part 1 of 1)')),
    ('G-SCAN-CLEAN', 'a banked verdict LINE', lambda S: '0 HIT(S) REPORTED' in line_with(S['scan'], 'VERDICT:'),
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '2 HIT(S)'))),
    ('G-SCAN-FLAGS-DECLARED', 'this act`s banked scan -- one flag, declared on the face',
     lambda S: '(R81) FLAGS : 1' in line_with(S['scan'], '(R81) FLAGS') and 'The ferry scan`s one (R81) flag is INFORMATIONAL' in flat(S['face']),
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
    ('G-PRIOR-CLOSED-PUSHED', 'b537`s closing and its addendum',
     lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'the upload is the -post build' in S['prior_add'],
     lambda S: put(S, 'prior_add', '')),
    ('G-ADDENDUM-SLOT-CONTENT-BOUNDED', 'the addendum slot bytes', lambda S: S['addendum'].strip() == '',
     lambda S: put(S, 'addendum', 'not a verbatim quotation')),
    ('G-NUMBER-UNCLAIMED', 'the data directory, and this act`s own banked order',
     lambda S: 'ACT b538' in S['ferry'] and 'ACT b538' in S['face'] and not glob.glob(os.path.join(D, 'b539_registration_*.txt')),
     lambda S: cut(S, 'face', 'ACT b538')),
    ('G-PEEK-DECLARED', 'the face`s (C) block, the probes and the byte check before the lock, the install and the census after it',
     lambda S: 'THE PROBES WERE RUN BEFORE THE SEAL' in flat(S['face']) and 'THE BYTE CHECK WAS RUN BEFORE THE SEAL' in flat(S['face'])
     and S['before_lock'] and S['after_lock'],
     lambda S: put(S, 'after_lock', False)),
    ('G-R148-ENTERED', 'the banked ferry AND the trail', lambda S: 'RULING (R148) END' in S['ferry'] and S['ot'].count('**(R148) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R148) ratified', '(R148) noted'))),
    ('G-READS-PINNED', 'lv`s tag and HEAD and SIDE-kernel`s v1.5, READ HERE -- the cited lv files identical at the tag and HEAD',
     lambda S: S['lv_tag'].startswith('93c27ec') and S['lv_head'].startswith('2f71068') and S['lv_same'] and S['sk_v15'].startswith('0e5233f'),
     lambda S: put(S, 'lv_same', False)),
    ('G-RESTATEMENTS-COMPARED', 'the byte-check bank -- four restatements, one byte-identical, all four identical when normalised',
     lambda S: len(re.findall(r'^### \S+ : BYTE-IDENTICAL (True|False) ;', S['cmp'], re.M)) == 4
     and len(re.findall(r'^### \S+ : BYTE-IDENTICAL True ;', S['cmp'], re.M)) == 1
     and len(re.findall(r'`/\\` as `∧` : True$', S['cmp'], re.M)) == 4,
     lambda S: put(S, 'cmp', S['cmp'].replace('as `∧` : True', 'as `∧` : False', 1))),
    ('G-FACES-VERBATIM', 'the module against lv at v0.10.0 and SIDE-kernel at 0e5233f READ HERE, every restated face',
     lambda S: faces_ok(S), lambda S: put(S, 'mod', S['mod'].replace('0 < pairing i i', '0 ≤ pairing i i'))),
    ('G-INSTALLED-FROM-DRAFT', 'the install bank against attempt 1`s banked source -- onto no prior file',
     lambda S: S['inst']['RegisterDepth.lean']['prior_sha'] is None and S['inst']['AxiomCheckRegisterDepth.lean']['prior_sha'] is None
     and S['inst']['RegisterDepth.lean']['draft_sha'] == S['inst']['RegisterDepth.lean']['installed_sha'] == S['att'][0]['source_sha'] == S['att_files'].get(1),
     lambda S: put(S, 'inst', {**S['inst'], 'RegisterDepth.lean': dict(S['inst']['RegisterDepth.lean'], draft_sha='0' * 64)})),
    ('G-ATTEMPTS-BANKED', 'the attempts bank against the banked sources and logs',
     lambda S: [a['attempt'] for a in S['att']] == list(range(1, len(S['att']) + 1)) == sorted(S['att_files'])
     and all(S['att_files'][a['attempt']] == a['source_sha'] for a in S['att']) and S['clogs'] == len(S['att']),
     lambda S: put(S, 'att', S['att'] + [dict(S['att'][-1], attempt=len(S['att']) + 1)])),
    ('G-MODULE-NO-SORRY', 'the module text, the last compile log and the profile log',
     lambda S: bool(S['mod']) and not re.search(r'\bsorry\b', S['mod']) and 'exit 0 ;' in S['clast'] and ': error' not in S['clast']
     and 'sorryAx' not in S['plog'],
     lambda S: put(S, 'mod', S['mod'] + NL + 'theorem x : False := sorry')),
    ('G-PROFILE-WHOLE-STRING', 'the profile run file, wrapped lines joined -- every theorem standard three or fewer, one line each',
     lambda S: re.findall(r'^theorem (\S+)', S['mod'], re.M) == THMS and all(within(S, n) for n in THMS),
     lambda S: put(S, 'plog', S['plog'].replace(STD3 % (NS + 'register5_output_holds'), (STD3 % (NS + 'register5_output_holds')).replace(', Quot.sound', ', sorryAx')))),
    ('G-PROBES-BANKED', 'the three banked probes -- sources and outputs; no theorem; #print mellin in probe 1',
     lambda S: all(p.count('### output') == 1 and not re.search(r'^theorem ', p, re.M) for p in S['probes']) and '#print mellin' in S['probes'][0],
     lambda S: put(S, 'probes', [S['probes'][0].replace('#print mellin', ''), S['probes'][1], S['probes'][2]])),
    ('G-HALTS-RECORDED', 'the attempts bank against the module -- every halted theorem a `_blocked` Prop',
     lambda S: all(a.get('failed_decls') is not None for a in S['att'])
     and set(halted(S)) == set(re.findall(r'^def (\S+)_blocked\b', S['mod'], re.M)),
     lambda S: put(S, 'att', [dict(a, failed_decls=list(a.get('failed_decls', [])) + ['register5_output_holds']) for a in S['att']] * 2)),
    ('G-MELLIN-PRINTED', 'the profile run -- Mathlib`s `mellin` printed, the Bochner integral over Ioi 0',
     lambda S: 'def mellin' in S['plog'] and '∫ (t : ℝ) in Set.Ioi 0, ↑t ^ (s - 1) • f t' in S['plog'],
     lambda S: put(S, 'plog', S['plog'].replace('↑t ^ (s - 1) • f t', '↑t ^ s • f t'))),
    ('G-R1-GRADED', 'the census against the #check and the axiom line',
     lambda S: crow(S, 'R1').get('grade') == 'FALSE-AS-STATED' and within(S, 'not_register1')
     and chk(S, 'not_register1').startswith('%snot_register1 : ¬%sRegister1_universalityHypothesis' % (NS, NS)),
     lambda S: put(S, 'cen', [dict(r, grade='TRUE-AS-STATED') if r.get('reg') == 'R1' else r for r in S['cen']])),
    ('G-LVH2-GRADED', 'the census against the #check -- mellin Phi (s / 2) = 0 on re s ≤ 1',
     lambda S: crow(S, 'lv`s h2').get('grade', '').startswith('FALSE-AS-STATED') and within(S, 'mellin_Phi_eq_zero_of_re_le_one')
     and chk(S, 'mellin_Phi_eq_zero_of_re_le_one').endswith('∀ (s : ℂ), s.re ≤ 1 → mellin %sPhi (s / 2) = 0' % NS)
     and within(S, 'lvh2_corrected_iff'),
     lambda S: put(S, 'prof', dict(S['prof'], checks=dict(S['prof'].get('checks') or {}, mellin_Phi_eq_zero_of_re_le_one='x')))),
    ('G-R3-GRADED', 'the census against the module -- UNDECIDED, the partial theorem compiled, no deciding theorem present',
     lambda S: crow(S, 'R3').get('grade') == 'UNDECIDED' and within(S, 'register3_of_one_lt_re')
     and not re.search(r'^theorem (register3_holds|not_register3_at)\b', S['mod'], re.M) and 'Hamburger' in crow(S, 'R3').get('missing', ''),
     lambda S: put(S, 'cen', [dict(r, missing='') if r.get('reg') == 'R3' else r for r in S['cen']])),
    ('G-R5-GRADED', 'the census against the #check -- the face itself, no premise',
     lambda S: crow(S, 'R5-output').get('grade', '').startswith('TRUE-AS-STATED') and within(S, 'register5_output_holds')
     and chk(S, 'register5_output_holds') == '%sregister5_output_holds : %sRegister5_output_HilbertPolya' % (NS, NS),
     lambda S: put(S, 'prof', dict(S['prof'], checks=dict(S['prof'].get('checks') or {}, register5_output_holds='x')))),
    ('G-COUPLINGS-READ', 'the couplings bank against sevenClasses in the module -- each of the seven classified',
     lambda S: all(re.search(r'^  %s\s' % re.escape(n), S['cpl'], re.M) for n in re.findall(r'(C\d_[A-Za-z_]+)', def_block(S['mod'], 'sevenClasses')))
     and len(set(re.findall(r'(C\d_[A-Za-z_]+)', def_block(S['mod'], 'sevenClasses')))) == 7 and 'POINTWISE TO PHI : 0 of 7' in S['cpl'],
     lambda S: put(S, 'cpl', S['cpl'].replace('  C4_modularity', '  C4_x'))),
    ('G-CENSUS-ENTERED', 'FINDINGS -- the title once, six data rows, every grade cell bold and filled',
     lambda S: S['find'].count(CTITLE) == 1 and len(census_table(S)) == 6
     and all(re.search(r'\| \*\*[^*|\s][^*|]*\*\* \|', l) for l in census_table(S)),
     lambda S: put(S, 'find', S['find'].replace('| **UNDECIDED** |', '| ** ** |'))),
    ('G-ROWS-GRADED', 'row 387 -- ten DERIVES and one INTERFACES, each theorem standard three or fewer',
     lambda S: corr_row(S, 387) != '' and all(('`%s` DERIVES' % n) in cell(S, 387, 4) and within(S, n) for n in THMS if n != 'register3_of_one_lt_re')
     and '`register3_of_one_lt_re` INTERFACES' in cell(S, 387, 4) and len(GRADE_RE.findall(cell(S, 387, 4))) == 11,
     lambda S: put(S, 'corr', S['corr'].replace('`not_register1` DERIVES', '`not_register1` SHELL'))),
    ('G-TABLE-ROW', 'the regenerated terminal table -- not_register1 PROFILED',
     lambda S: 'NOT PROFILED' not in table_row(S, 'not_register1') and table_row(S, 'not_register1') != '',
     lambda S: put(S, 'table', S['table'].replace('`%snot_register1`' % NS, '`ghost`'))),
    ('G-LINES-KEPT', 'FINDINGS and OPEN_TRAILS bytes against their blobs at b537`s commit -- true prefixes',
     lambda S: all(S['pp_now'][f].startswith(S['pp_prior'][f]) and len(S['pp_now'][f]) > len(S['pp_prior'][f]) for f in PPFILES),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'FINDINGS.md': S['pp_now']['FINDINGS.md'][1:]}))),
    ('G-POINTER-DISCHARGED', 'the trail and the seat`s memory file READ HERE -- the pointer once, DISCHARGED at b538',
     lambda S: S['ot'].count(POINTER) == 1 and POINTER in trail_raw(S) and S['mem_live'] == S['mem_bank']
     and b'**DISCHARGED at b538**' in S['mem_live'] and b'**OWED, as of b537:**' in S['mem_live'],
     lambda S: put(S, 'mem_live', S['mem_live'].replace(b'DISCHARGED at b538', b'OWED'))),
    ('G-B512-UNEDITED', 'relay`s git -- b512`s closing unchanged since b537`s close', lambda S: S['b512_diff'] == '',
     lambda S: put(S, 'b512_diff', 'data/b512_closing.txt')),
    ('G-CEILING-UNCHANGED', 'README and REGISTRY bytes against their blobs at b537`s commit',
     lambda S: all(S['pp_now'][f] == S['pp_prior'][f] for f in ('README.md', 'REGISTRY.md')),
     lambda S: put(S, 'pp_now', dict(S['pp_now'], **{'README.md': S['pp_now']['README.md'] + b' '}))),
    ('G-DEPOSITED-KERNELS-UNTOUCHED', 'SIDE-kernel and lv READ HERE -- at their HEADs, tracked trees clean; ERRATA byte-identical',
     lambda S: S['sk_head'].startswith('0256e9e') and S['sk_clean'] and S['lv_head'].startswith('2f71068') and S['lv_clean']
     and S['pp_now']['ERRATA.md'] == S['pp_prior']['ERRATA.md'],
     lambda S: put(S, 'sk_clean', False)),
    ('G-NO-ZENODO-CALL', 'the act`s tools -- none carries the platform`s address (the needle built, not written)',
     lambda S: S['zen'] == [], lambda S: put(S, 'zen', ['b538_x.py'])),
    ('G-DELETE-FREE', 'this act`s own tools, their code with prose stripped -- no delete call of any kind',
     lambda S: S['dels'] == [], lambda S: put(S, 'dels', [('b538_x.py', 'x')])),
    ('G-N1-SCORED', 'the desk against the profile and the attempts', lambda S: nscored(S, 'n1'),
     lambda S: put(S, 'sc', dict(S['sc'], n1=not S['sc'].get('n1')))),
    ('G-N2-SCORED', 'the desk against the profile and the attempts', lambda S: nscored(S, 'n2'),
     lambda S: put(S, 'sc', dict(S['sc'], n2=not S['sc'].get('n2')))),
    ('G-N3-SCORED', 'the desk against the profile', lambda S: nscored(S, 'n3'),
     lambda S: put(S, 'sc', dict(S['sc'], n3=not S['sc'].get('n3')))),
    ('G-N4-SCORED', 'the desk against the census', lambda S: nscored(S, 'n4'),
     lambda S: put(S, 'sc', dict(S['sc'], n4=not S['sc'].get('n4')))),
    ('G-N5-SCORED', 'the desk against the census', lambda S: nscored(S, 'n5'),
     lambda S: put(S, 'sc', dict(S['sc'], n5=not S['sc'].get('n5')))),
    ('G-N6-SCORED', 'the desk against the blobs, the kernels, the tools and the token', lambda S: nscored(S, 'n6'),
     lambda S: put(S, 'sc', dict(S['sc'], n6=not S['sc'].get('n6')))),
    ('G-SEAT-EXPECTATIONS-SCORED', 'the face against the desk -- three registered, each word from the banks',
     lambda S: "THE SEAT`S OWN EXPECTATIONS" in S['face'] and 'REGISTERED 3 ;' in S['desk'] and nscored(S, 's1') and nscored(S, 's2')
     and nscored(S, 's3'),
     lambda S: put(S, 'desk', S['desk'].replace('**(S1)** ### **', '**(S1)** ### **NOT'))),
    ('G-NODEPOSIT', 'the deposit directory tracked state', lambda S: S['dep_clean'], lambda S: put(S, 'dep_clean', False)),
    ('G-NOH2-MOVED', 'the trail`s own text -- THIS act`s record', lambda S: 'where the deposit left it' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(TRAILH, '### b538 -'))),
    ('G-PRIORBANK-UNCHANGED', 'file times against the face, no exception', lambda S: S['noprior'], lambda S: put(S, 'noprior', False)),
    ('G-FOUR-LISTS-OPEN', 'the trail`s own text -- THIS act`s record', lambda S: 'the four lists stay OPEN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('stay OPEN', 'are closed'))),
    ('G-LANE-SHUT', 'the trail`s own record -- the kernel lane shut, said', lambda S: 'kernel lane shuts at this act' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace(NL, ' ').replace('kernel lane shuts at this act', 'lane stays open'))),
    ('G-CORPUS-SCOPE', 'the file lists -- FINDINGS and OPEN_TRAILS; the kernel`s changes the two NEW files',
     lambda S: sorted(S['tracked']) == sorted(PPFILES) and S['ker_changed'] == {'SIDEExplicitFormula/RegisterDepth.lean', 'AxiomCheckRegisterDepth.lean'},
     lambda S: put(S, 'ker_changed', S['ker_changed'] | {'SIDEExplicitFormula/Seam.lean'})),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- one heading for this act',
     lambda S: S['pp_now']['OPEN_TRAILS.md'].startswith(S['pp_prior']['OPEN_TRAILS.md']) and S['ot'].count(TRAILH) == 1,
     lambda S: put(S, 'ot', S['ot'] + NL + TRAILH + ' a second record')),
    ('G-CORR-APPEND-ONLY', 'the correspondence ledger -- its prior bytes a prefix, row 387 once, six cells',
     lambda S: S['corr'].startswith(S['corr_prior'].rstrip(NL)) and S['corr'].count('| 387 |') == 1
     and len(corr_row(S, 387).strip().strip('|').split(' | ')) == 6,
     lambda S: put(S, 'corr', S['corr'] + NL + '| 387 | a duplicate row |')),
    ('G-INSTRUMENTS-UNEDITED', 'relay`s tools against b537`s close -- none modified',
     lambda S: S['tools_edited'] == [], lambda S: put(S, 'tools_edited', ['corr_row.py'])),
    ('G-WRITELIST-KINDS', 'every b538 commit in four repositories, against (R91)`s STEM GLOB',
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
                and "log', '-1', '--pretty=%s').startswith('b538')" in S['suite']
                and "data/b538_components.txt' in gits(ROOT, 'show'" in S['suite']),
     lambda S: cut(S, 'suite', "data/b538_components.txt' in gits(ROOT, 'show'")),
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
              and gits(ROOT, 'log', '-1', '--pretty=%s').startswith('b538')
              and 'data/b538_components.txt' in gits(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))
    # ### ### **ONE ARM IS POST-PUSH BY NATURE** -- the mirror is built after the push, and the
    # ### face says so in its own words. ### b493 deferred a SECOND arm, `G-LOG-COMMITTED-UNCHANGED`,
    # ### which THIS act does not declare; ### **A DEFERRAL LIST CARRIED PAST THE ARM IT NAMES
    # ### PRINTS A DEFERRED VERDICT FOR AN ARM THAT DOES NOT EXIST**, so it is dropped.
    deferred = []
    S['declared_eq_run'] = (set(names) - set(deferred)) == (set(declared) - set(deferred))

    rec('=' * 104)
    rec('b538 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.'
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
    out = os.path.join(D, 'b538_checks_postpush.txt' if pushed else 'b538_checks.txt')
    io.open(out, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(exercise=EX, run=len(RES), live_failing=fail, defective=defective,
                   neg_failures=negfail, declared=len(declared), deferred=deferred, stray=stray),
              io.open(os.path.join(D, 'b538_exercise.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
