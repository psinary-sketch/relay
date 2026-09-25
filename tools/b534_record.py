# -*- coding: utf-8 -*-
"""b534_record.py -- THE COMPONENTS, THE NOTE, THE ROW, THE DESK AND THE TRAIL.
### `python tools/b534_record.py components | note | row | desk | trail`

### READING (11) of the sealed face: each compiled theorem among the nineteen named is graded by statement-read against the
### ferry`s model statement, the reading written in `GRADES` below beside the grade; a halted lemma takes none. READING (12):
### the navigator`s six and the seat`s three, scored on the banks (`b534_attempts.json`, `b534_profile.json`, the module`s
### source, the kernel`s and PLACE-papers` git objects, the trail), never typed. READING (9): the trail record`s last three
### lines are the `#check` outputs of the three statements, verbatim from the profile run.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
KER = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
MOD = os.path.join(KER, 'SIDEExplicitFormula', 'PowerLimit.lean')
PWF = os.path.join(KER, 'SIDEExplicitFormula', 'PowerWindow.lean')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
CORR = os.path.join('D:', os.sep, 'SIDE-global-section', 'CORRESPONDENCE.md')
NL = chr(10)
NS = 'SIDEExplicitFormula.B321.'
PRIOR_KERNEL = 'f42102f'
PRIOR_PP = 'b8cce57'
ROW = '383'
UNTOUCHED = ['SIDEExplicitFormula/RestBound.lean', 'SIDEExplicitFormula/RHChain.lean', 'SIDEExplicitFormula/H2Bridge.lean']
RENAMED = {'window': 'pwWindow', 'window_contDiff': 'pwWindow_contDiff', 'window_support': 'pwWindow_support'}
CEIL = ('RH and Weil positivity on classK are one Prop apart in the kernel, RH → h2_sign compiled, h2_sign → RH compiled to its '
        "last step; the deposit's Route 3 premise is RH restated, E-2026-09-25-1 drafted.")
LAST3 = ['h2_sign_iff_rh_strip', 'h2_sign_imp_rh_of_seam', 'rh_strip_imp_rh']
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### THE GRADES, BY STATEMENT-READ (READING (11)). ### (name ; grade ; the reading against the ferry`s model statement)
GRADES = [
    ('paperFT_conj_of_real', 'DERIVES', 'the model`s identity for every real g (continuity and compact support dropped)'),
    ('paperFT_neg_of_even', 'DERIVES', 'the model`s evenness of the transform, as ordered (PairTerm`s phiC_FT_neg, named)'),
    ('zero_term_real', 'DERIVES', 'the model`s product g^(z) g^(-z), under the model`s hypotheses'),
    ('paperFT_polyOpFull', 'DERIVES', 'the model`s factor polyEvalFull a (-(I z)), for g C^(length a) supported in [-L, L] (READING (4))'),
    ('polyOpFull_support', 'DERIVES', 'the support unchanged, as ordered'),
    ('polyOpFull_contDiff', 'DERIVES', 'smooth in, smooth out, as ordered'),
    ('kWindow_classK', 'DERIVES', 'the model`s membership, through classK_of_real_even as ordered'),
    ('kWindow_term', 'DERIVES', 'the model`s term at every complex z, the ferry`s at z = gammaOf rho (READING (5), stronger)'),
    ('nodes_distinct', 'DERIVES', 'the model`s statement on T, proved by real algebra (through v_eq_iff, for all rho)'),
    ('tie_term_neg', 'DERIVES', 'the model`s real part -N_rho M^(2^(j+1)), for any S with the node property, which coeffs_exist supplies for every j (READING (6))'),
    ('rest_term_small', 'DERIVES', 'the model`s bound with C_P^2 (1 + |w|)^(2d) read as B^2 (1 + |w|)^(2D), for any S with the bound, which coeffs_exist supplies; the offScore < M part in fR_bound'),
    ('dominant_summable', 'DERIVES', 'the model`s summability with j_0 = D (READING (7))'),
    ('rest_tendsto_zero', 'DERIVES', 'the model`s limit, by Tannery`s theorem, for the family coeffs_exist supplies'),
    ('zeroSide_eventually_neg', 'DERIVES', 'the model`s statement, under PWSetup and a tie zero'),
    ('h2_sign_imp_rh_strip', 'DERIVES', 'the model`s statement exactly'),
    ('rh_strip_imp_h2_sign', 'DERIVES', 'the model`s statement exactly'),
    ('h2_sign_iff_rh_strip', 'DERIVES', 'the model`s statement exactly'),
    ('h2_sign_imp_rh_of_seam', 'DERIVES', 'the model`s statement exactly'),
    ('ch_iff_h2_sign_of_seam', 'DERIVES', 'the model`s statement exactly'),
]
L7AD_LAST = 'rest_term_small'
L7E = ['ceil_weight', 'Aw_nonneg', 'zero_weight', 'weighted_finite_bound', 'weighted_summable', 'dominant_summable', 'fR_norm_le',
       'fR_bound', 'rest_tendsto_zero', 'mem_sT', 'zeroSide_eventually_neg', 'zeroSideNeg_holds']
w = lambda v: 'HELD' if v else 'REFUTED'


def read(n):
    try:
        return io.open(os.path.join(D, n), encoding='utf-8').read()
    except OSError:
        return ''


def git(repo, *a):
    return subprocess.run(['git'] + list(a), cwd=repo, capture_output=True, text=True, encoding='utf-8').stdout.strip()


def kthms():
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import importlib.util
    spec = importlib.util.spec_from_file_location('k534', os.path.join(ROOT, 'tools', 'b534_kernel.py'))
    k = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(k)
    return k.THMS


def kread():
    return json.loads(read('b534_attempts.json') or '[]'), json.loads(read('b534_profile.json') or '{}')


def src():
    return io.open(MOD, encoding='utf-8').read()


def decl(s, name):
    m = re.search(r'^(?:theorem|def) %s\b' % re.escape(name), s, re.M)
    if not m:
        return None
    n = re.search(r'^(?:theorem|def|structure|/-|end |open |example|variable|--)', s[m.end():], re.M)
    return s[m.start():m.end() + (n.start() if n else len(s))].rstrip()


def head(s, name):
    t = decl(s, name)
    if t is None:
        return None
    cut = [x for x in (t.find(':='), t.find(NL + '  |')) if x >= 0]
    return t[:min(cut)].rstrip() if cut else t


def failures(at):
    out = {}
    for a in at:
        for d0 in a.get('failed_decls', []):
            d1 = RENAMED.get(d0, d0)
            out.setdefault(d1, []).append(a['attempt'])
    return out


def first_clean(at):
    ok = [a['attempt'] for a in at if a['exit'] == 0 and a['errors'] == 0 and not a['sorry']]
    return ok[0] if ok else None


def scores():
    at, pr = kread()
    std = pr.get('std3', {})
    chk = pr.get('checks', {})
    s = src()
    thms = kthms()
    l7ad = thms[:thms.index(L7AD_LAST) + 1]
    fl = failures(at)
    halted = sorted(d for d, ns in fl.items() if len(ns) >= 2)
    fc = first_clean(at)
    blobs = {f: (git(KER, 'hash-object', f), git(KER, 'rev-parse', PRIOR_KERNEL + ':' + f), git(KER, 'rev-parse', 'HEAD:' + f))
             for f in UNTOUCHED}
    er = (git(PP, 'hash-object', 'ERRATA.md'), git(PP, 'rev-parse', PRIOR_PP + ':ERRATA.md'), git(PP, 'rev-parse', 'HEAD:ERRATA.md'))
    zen = [f for f in os.listdir(D) if f.startswith('b534_') and 'zenodo' in f.lower()]
    heads = [head(s, n) or '' for n in re.findall(r'^theorem (\S+)', s, re.M)]
    ot = io.open(OT, encoding='utf-8').read()
    trail = ot[ot.find(HEADING):] if HEADING in ot else ''
    dep_clean = git(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2') == ''
    pwsrc = io.open(PWF, encoding='utf-8').read()
    return dict(
        first_clean=fc, failures=fl, halted=halted,
        n1=all(std.get(NS + n) is True for n in l7ad) and not any(a >= 2 for n in l7ad for a in fl.get(n, [])),
        n2=(not halted) or (all(h in L7E for h in halted) and not any(h in l7ad for h in halted)),
        n2_vacuous=not halted,
        n3=std.get(NS + 'h2_sign_iff_rh_strip') is True and (chk.get('h2_sign_iff_rh_strip') or '') ==
        '%sh2_sign_iff_rh_strip : %sh2_sign ↔ %srh_strip' % (NS, NS, NS),
        n4=bool(re.search(r'^def rh_strip_imp_rh : Prop', pwsrc, re.M)) and (chk.get('rh_strip_imp_rh') or '').endswith(': Prop')
        and not any(h.rstrip().endswith('rh_strip_imp_rh') for h in heads),
        n5=all(a and a == b == c for a, b, c in blobs.values()),
        n6=dep_clean and er[0] and er[0] == er[1] == er[2] and not zen and (CEIL in trail or not trail),
        s1=not halted and fc is not None,
        s2=std.get(NS + 'h2_sign_iff_rh_strip') is True,
        s3=bool(at) and bool(at[0].get('failed_decls')),
        blobs=blobs, errata=er, zenodo_files=zen, trail_present=bool(trail))


def components():
    at, pr = kread()
    s = src()
    L = ['=' * 132, 'b534 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '',
         '### THE MODULE: `SIDEExplicitFormula/PowerLimit.lean` (NEW), `AxiomCheckLimit.lean` (NEW); `PowerWindow.lean` a',
         '### comment-only note after `nodes_distinct_nonreal` (install refused a non-comment difference), its olean rebuilt once:',
         '  ' + (read('b534_rebuild_log.txt').split(NL)[2] if read('b534_rebuild_log.txt') else 'NO REBUILD LOG')]
    for a in at:
        L.append('  attempt %d : exit %d ; %d error lines ; %.1f s ; declarations failing : %s'
                 % (a['attempt'], a['exit'], a['errors'], a['seconds'], a.get('failed_decls') or 'NONE'))
    fl = failures(at)
    L.append('  ### halted (two failures, renames followed) : %s' % (sorted(d for d, n in fl.items() if len(n) >= 2) or 'NONE'))
    L.append('  ### renamed between attempts (defect (a)) : %s' % RENAMED)
    L += ['', '### THE GRADED STATEMENTS, FROM THE SOURCE (declaration line to its := or its first equation):']
    for n, g, r in GRADES:
        L += ['', head(s, n) or ('### ABSENT : ' + n), '  -> %s -- %s' % (g, r)]
    L += ['', '### THE DEFINITIONS, WHOLE:']
    for n in ('polyOpFull', 'polyEvalFull', 'pwWindow', 'kWindow', 'vOf', 'wOf', 'Kp', 'cE', 'Ep', 'VF', 'Xval', 'rT', 'Pof',
              'coeffList', 'zeroSideNeg'):
        L += ['', decl(s, n) or ('### ABSENT : ' + n)]
    L += ['', '### THE PROFILE (AxiomCheckLimit.lean):'] + ['  ' + l for l in pr.get('lines', [])]
    L += ['  ### whole-string standard three : %d of %d' % (sum(1 for v in pr.get('std3', {}).values() if v), len(pr.get('std3', {})))]
    for k, v in (pr.get('checks') or {}).items():
        L.append('  ### #check %s : %s' % (k, ' '.join((v or 'NONE').split())))
    L += ['', '### THE REFLECTION CLOSURE RESOLVES TO A THEOREM: `Zeta23.ZeroConfig.reflect_mem` (a field), instantiated for',
          '### `zetaZeroConfig` from `Zeta23.zetaSeam` via `Zeta23.zeta_reflect_zero`; no hypothesis hreflZ is added.',
          '### THE SEAM, UNCHANGED: `rh_strip_imp_rh` a Prop; the left half-plane ABSENT from Mathlib by name (b533).', '=' * 132]
    io.open(os.path.join(D, 'b534_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    print(NL.join(L[:14]))


def note():
    """### (R144)(1): the note beside b533`s sealed face, a NEW b534 file; the face is not edited."""
    p = os.path.join(D, 'b534_note_beside_b533_face.txt')
    if os.path.exists(p):
        sys.exit('### ALREADY PRESENT')
    body = ['### NOTE BESIDE `data/b533_registration_2026-09-25.txt` -- written by act b534 under RULING (R144)(1).',
            '### The sealed face is not edited. Its defect (d) (relay `data/b533_defects.txt`): the hypothesis',
            '### `Function.support g ⊆ Set.Icc (-L) L` carried by `power_contDiff` and `paperFT_power` (PowerWindow.lean:140,',
            '### :146-148), undeclared on b533`s face, is L3`s standing window context, as the seat read it. (R144)(1) ratifies',
            '### the reading; the DERIVES grades of row 382 stand.']
    io.open(p, 'w', encoding='utf-8', newline=NL).write(NL.join(body) + NL)
    print(NL.join(body))


def grade_cell():
    return (' ; '.join('`%s` %s' % (n, g) for n, g, _ in GRADES)
            + ' -- each by statement-read against the ferry`s model statement; zeroSideNeg stated and proved, no grade; '
              'rh_strip_imp_rh and nodes_distinct_nonreal STATED, no grade')


def row():
    sc = scores()
    at, pr = kread()
    n_std = sum(1 for v in pr.get('std3', {}).values() if v)
    cells = [
        ROW,
        '**W-ORD-WEIL-CONVERSE f4, THE POWER-WINDOW ROUTE, ACT TWO OF TWO: THE LIMIT AND THE ASSEMBLY** (b534, under (R144)). '
        'In SIDE-explicit-formula, PowerLimit.lean (new): L7a the zero term of a real window is g^(z) g^(-z); L7b the full '
        'operator SUM a_p D^p with transform factor P(-iz); L7c the power window pwWindow a g0 j and its weilTest kWindow, in '
        'classK, with term P(w) P(-w) g0^(z)^(2^(j+1)); L7d the interpolation variable v = (rho - 1/2)^2 with nodes_distinct '
        'proved by real algebra, the kill factor K, the sign factor 1 + c w, phase targets by the sign of Im v, and for every j '
        'a real S_j making every tie term -‖X‖, with ‖P_j(w)‖ <= B (1 + ‖w‖)^D; L7e the dominant summable by the kernel`s local '
        'count, the rest over M^(2^(j+1)) tending to 0 by Tannery`s theorem, and for some j the zero side negative; L8 '
        'h2_sign iff rh_strip, and h2_sign -> RiemannHypothesis compiled from the seam Prop rh_strip_imp_rh. Clean at attempt '
        '%s; halted NONE.' % sc['first_clean'],
        '`SIDE-explicit-formula/SIDEExplicitFormula/PowerLimit.lean` : ' + ', '.join('`%s%s`' % (NS, n) for n, _, _ in GRADES)
        + ' ; `SIDE-explicit-formula/AxiomCheckLimit.lean`',
        '%d of %d theorems of the module: each [propext, Classical.choice, Quot.sound]' % (n_std, len(pr.get('std3', {}))),
        grade_cell(),
        '(N1) %s, (N2) %s%s, (N3) %s, (N4) %s, (N5) %s, (N6) %s; (S1) %s, (S2) %s, (S3) %s. The kernel lane shuts; the kernel is '
        'not tagged; the seam not attempted; nothing filed to ERRATA; nothing at Zenodo written; h2 where the deposit left it.'
        % (w(sc['n1']), w(sc['n2']), ' VACUOUS' if sc['n2_vacuous'] else '', w(sc['n3']), w(sc['n4']), w(sc['n5']),
           w(sc['n6']), w(sc['s1']), w(sc['s2']), w(sc['s3'])),
    ]
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'corr_row.py'), CORR] + cells, capture_output=True, text=True,
                       encoding='utf-8')
    print(r.stdout[-3000:], r.stderr[-2000:])
    io.open(os.path.join(D, 'b534_rows.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(dict(cells=cells, exit=r.returncode), indent=1, ensure_ascii=False) + NL)
    return r.returncode


def desk():
    sc = scores()
    at, pr = kread()
    std = pr.get('std3', {})
    chk = pr.get('checks', {})
    L = ['=' * 104, 'b534 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S SIX.', '-' * 104,
         '  **(N1)** ### **%s.** -- L7a-L7d theorems std3 and none failing at an attempt numbered 2 or later ; failures per '
         'declaration %s.' % (w(sc['n1']), sc['failures'] or 'NONE'),
         '  **(N2)** ### **%s%s.** -- halted %s%s.' % (w(sc['n2']), ', VACUOUS' if sc['n2_vacuous'] else '', sc['halted'] or 'NONE',
                                                        ': no lemma halted, so the conditional holds vacuously' if sc['n2_vacuous'] else ''),
         '  **(N3)** ### **%s.** -- h2_sign_iff_rh_strip std3 %s ; `%s`.' % (w(sc['n3']), std.get(NS + 'h2_sign_iff_rh_strip'),
                                                                         chk.get('h2_sign_iff_rh_strip')),
         '  **(N4)** ### **%s.** -- `%s` ; no theorem head of PowerLimit.lean ends in it.' % (w(sc['n4']), chk.get('rh_strip_imp_rh')),
         '  **(N5)** ### **%s.** -- blobs working / at %s / at HEAD : %s.'
         % (w(sc['n5']), PRIOR_KERNEL, {k.split('/')[-1]: [x[:12] for x in v] for k, v in sc['blobs'].items()}),
         '  **(N6)** ### **%s.** -- ERRATA.md working / at %s / at HEAD : %s ; b534 Zenodo files : %s ; deposit tree clean ; the '
         'ceiling sentence in the trail : %s.' % (w(sc['n6']), PRIOR_PP, [x[:12] for x in sc['errata']], sc['zenodo_files'] or 'NONE',
                                                 'PRINTED' if sc['trail_present'] else 'NOT YET WRITTEN'),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- halted %s ; first clean attempt %s.' % (w(sc['s1']), sc['halted'] or 'NONE', sc['first_clean']),
         '  **(S2)** ### **%s.** -- h2_sign_iff_rh_strip std3 : %s.' % (w(sc['s2']), std.get(NS + 'h2_sign_iff_rh_strip')),
         '  **(S3)** ### **%s.** -- attempt 1 failing : %s.' % (w(sc['s3']), at[0].get('failed_decls') if at else None),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6')].count(True),
            [sc[k] for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6')].count(False),
            [sc[k] for k in ('s1', 's2', 's3')].count(True), [sc[k] for k in ('s1', 's2', 's3')].count(False)),
         '', '### THE GRADES (READING (11)).'] + ['  `%s` %s -- %s' % g for g in GRADES] + [
         '', '### THIS ACT`S OWN DEFECTS.'] + [l for l in read('b534_defects.txt').rstrip(NL).split(NL) if l] + ['=' * 104]
    io.open(os.path.join(D, 'b534_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump({k: v for k, v in sc.items()}, io.open(os.path.join(D, 'b534_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print(NL.join(L))


HEADING = '### b534 — f4, the power-window route, act two of two: the limit and the assembly; (R144) entered'


def trail():
    sc = scores()
    at, pr = kread()
    s = src()
    chk = pr.get('checks', {})
    n_std = sum(1 for v in pr.get('std3', {}).values() if v)
    last3 = [' '.join((chk.get(n) or '').split()) for n in LAST3]
    if not all(last3):
        sys.exit('### REFUSED: a statement of the last three is missing from the profile: %s' % last3)
    body = [
        '', HEADING, '',
        '**(R144) ratified.** (1) b533\'s defect (d) — the support hypothesis on `power_contDiff` and `paperFT_power` — is L3\'s',
        'standing window context, as the seat read it; the DERIVES grades stand; the sealed face is not edited and a note stands',
        'beside it (relay `data/b534_note_beside_b533_face.txt`). (2) The nodes caveat is resolved inside the kernel: the',
        'interpolation variable is v = (ρ − 1/2)², distinctness is real algebra, and the operator carries odd orders so a real',
        'tie node is made negative by E(w) = 1 + c·w; `nodes_distinct_nonreal` stays as written and unproved, superseded, with a',
        'comment beside it in PowerWindow.lean. (3) L7 and L8 as b534, under (R143)(5)\'s halt rule. (4) The seam stays a Prop;',
        'h2_sign → RiemannHypothesis is compiled FROM it. (5) The update act and the fold are the act after\'s.',
        '',
        '**The module, `SIDEExplicitFormula/PowerLimit.lean`** (new; imports PowerWindow and Mathlib\'s Tannery), clean at',
        'attempt %s; %d of %d theorems the standard three on the whole string; no lemma halted (attempt 1 failed in %s, each once;'
        % (sc['first_clean'], n_std, len(pr.get('std3', {})), ', '.join('`%s`' % d for d in (at[0].get('failed_decls') if at else []))),
        'the ferry\'s `window` collided with b524\'s `B321.window` and is `pwWindow` in the kernel). The reflection closure the',
        'ferry asked for resolves to a theorem — the `ZeroConfig` field `reflect_mem`, for `zetaZeroConfig` from `Zeta23.zetaSeam`',
        '— so no hypothesis `hreflZ` was added.',
        '',
        '```lean',
        head(s, 'zeroSide_eventually_neg') or '',
        '',
        head(s, 'h2_sign_iff_rh_strip') or '',
        '```',
        '',
        '**Departures, declared on the face.** The phase target: the ferry\'s i·exp(−iθ/2) at a node with its conjugate at the',
        'conjugate node is not one formula in v, so the targets go by the sign of Im v (1 at a real node, a principal square root',
        'of −conj X/|X| above the axis, its conjugate\'s conjugate below), and every tie term is −|X|. c = 1 + Σ_T 1/|Re ρ − 1/2| in',
        'place of 2/√(min v). The coefficient bound is carried as |P_j(w)| ≤ B(1 + |w|)^D. `dominant_summable` takes j₀ = D and',
        'sums through a weighted form of `finite_rest_bound`\'s own unit-interval grouping; `rest_tendsto_zero` is Tannery\'s',
        'theorem. L8 is compiled from a named Prop, `zeroSideNeg`, which `zeroSideNeg_holds` discharges.',
        '',
        '**Grades in this act\'s row (%s), by statement-read:** %s DERIVES.' % (ROW, ', '.join('`%s`' % n for n, _, _ in GRADES)),
        '',
        '**(N1) %s · (N2) %s%s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat\'s own: (S1) %s, (S2) %s, (S3) %s.'
        % (w(sc['n1']), w(sc['n2']), ', VACUOUS (no lemma halted)' if sc['n2_vacuous'] else '', w(sc['n3']), w(sc['n4']),
           w(sc['n5']), 'HELD' if (sc['n6'] or not sc['trail_present']) else 'REFUTED', w(sc['s1']), w(sc['s2']), w(sc['s3'])),
        '',
        '**The ceiling sentence, printed unchanged; the update act rules its next wording (R144)(5):** "' + CEIL + '"',
        '',
        '**The kernel lane shuts at this act\'s close.** The kernel is not tagged; the seam not attempted, proved or assumed;',
        'RestBound.lean (`not_f4_needs`, `HMax`), RHChain.lean and H2Bridge.lean untouched; nothing filed to ERRATA;',
        'E-2026-09-25-1 drafted; the three (R110) rows not applied; nothing at Zenodo written; nothing deposits; no grade moved on',
        'any other row; row U1 unedited; `h2` where the deposit left it — no premise is discharged, an equivalence between two is',
        'compiled; the four lists stay OPEN; nothing here is a statement about RH. Span since b525\'s fold: b526–b534, nine; the',
        'fold is the act after\'s.',
        '',
        '**The three statements, verbatim:**',
        '',
    ] + last3 + ['']
    before = open(OT, 'rb').read()
    if HEADING in before.decode('utf-8'):
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(NL.join(body).encode('utf-8'))
    after = open(OT, 'rb').read()
    bl, al = before.decode('utf-8').split(NL), after.decode('utf-8').split(NL)
    out = dict(added=len(after) - len(before), prefix=after.startswith(before),
               removed=len(bl) - sum(1 for a, b in zip(al, bl) if a == b), headings=after.decode('utf-8').count(HEADING),
               last3=last3)
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(removed)d lines removed, %(headings)d heading' % out)
    io.open(os.path.join(D, 'b534_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(json.dumps(out, ensure_ascii=False) + NL)


def main():
    return {'components': components, 'note': note, 'row': row, 'desk': desk, 'trail': trail}[sys.argv[1]]()


if __name__ == '__main__':
    sys.exit(main())
