# -*- coding: utf-8 -*-
"""b556_record.py -- THE CASCADE, ACT TEN, BATCH ONE: R_CURVE_CRITERION, INDEX_ARITY_AT_THE_CRITICAL_LINE AND
ADDITIVE_MULTIPLICATIVE_CONSPIRACY TIERED; THE CRITICAL PATH ENTERED ON THE TRAILS: THE RECORD, UNDER (R166).
### `python tools/b556_record.py reads | path | rows | tiers | rcurve | blocks | stems | findings | components | desk | trail`
### The probes` launches, the commits, pushes and branch commands are the seat`s. This file deletes nothing.
"""
import io, json, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b551_record as P  # noqa: E402
DD = 'D:' + os.sep
PP, LV, TRIAL = P.PP, P.LV, P.TRIAL
KER = os.path.join(DD, 'SIDE-kernel')
EFF = os.path.join(DD, 'SIDE-effects')
RCK = os.path.join(DD, 'SIDE-rcurve')
FIND, OT = P.FIND, P.OT
MAP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
CENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')
ERR = os.path.join(PP, 'ERRATA.md')
NL = chr(10)
rd, g, cite, append_to, guard_absent, line_of, poss, outside_bt = P.rd, P.g, P.cite, P.append_to, P.guard_absent, P.line_of, P.poss, P.outside_bt
PRIOR_RELAY = 'be9adfc8'   # ### b555`s closing housekeeping -- relay`s tip before this act
PRIOR_PP = '2d650c3'       # ### b555`s PLACE-papers commit
RCR = 'phase1.5/rcurve/R_CURVE_CRITERION.md'
IXR = 'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md'
AMR = 'phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md'
DOCS = {'RCURVE': RCR, 'INDEX': IXR, 'AMC': AMR}
TITLE = {'RCURVE': 'R_CURVE_CRITERION', 'INDEX': 'INDEX_ARITY_AT_THE_CRITICAL_LINE', 'AMC': 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY'}
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def dp(k):
    return os.path.join(PP, *DOCS[k].split('/'))


def jl(n):
    p = os.path.join(D, n)
    return json.loads(rd(p)) if os.path.exists(p) else {}


def put_json(n, obj):
    open(os.path.join(D, n), 'wb').write((json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8'))


def put_txt(n, lines):
    open(os.path.join(D, n), 'wb').write((NL.join(lines) + NL).encode('utf-8'))


def lines_with(path, pat, text=None):
    return [i + 1 for i, l in enumerate((text if text is not None else rd(path)).split(NL)) if re.search(pat, l)]


def blob(repo, spec):
    return subprocess.run(['git', '-C', repo, 'show', spec], capture_output=True).stdout.decode('utf-8-sig', 'replace').replace(chr(13), '')


# ------------------------------------------------------------------------------ READING (1): THE READS
WORK = [('W-ORD-DETECTION-REGION', [11151, 11332]), ('W-ORD-LI-WEIL-BRIDGE', [3548, 11203, 11230, 11265, 11290]),
        ('W-ORD-GRH-WEIL', [11373]), ('W-ORD-POWER-SWEEP', [11195]), ('W-ORD-WINDOW-CERTIFY', [11152]),
        ('W-ORD-SEAM-UPSTREAM', [10972]), ('W-ORD-STORMER-CLASH', [11257])]


def reads():
    L = ['b556 -- THE ORDERED READS, CITED BY PATH AND LINE', '',
         '### R_CURVE_CRITERION.md is at `%s` (PLACE-papers; not in the mirror)' % RCR, '']
    for k, spans in (('RCURVE', [(1, 13, 'head and the claim-status correction'), (343, 360, 'the Kernel Correspondence'), (462, 474, 'versions and the b397 block')]),
                     ('INDEX', [(1, 29, 'head, abstract, §1 (the reduction sentence at :29)'), (359, 397, 'the Correspondence, its two standards and rows'),
                                (631, 644, 'the era annotations')]),
                     ('AMC', [(400, 417, 'the original Correspondence and its audit line'), (442, 456, 'the 2026-08-12 table at the standard'),
                              (457, 478, 'the era and proofreading annotations')])):
        for a, z, w in spans:
            cite(L, dp(k), a, z, '%s -- %s' % (TITLE[k], w))
        L += ['### %s read entire: %d lines' % (TITLE[k], len(rd(dp(k)).split(NL))), '']
    for a, z, w in ((18, 18, 'the abbreviations'), (24, 34, 'the ranked terminals'), (53, 53, 'the RCURVE row'), (134, 146, 'the tier law and the RH-anchor list')):
        cite(L, MAP, a, z, 'THE_LOAD_BEARING_MAP.md -- ' + w)
    mp = rd(MAP)
    L += ['### THE_LOAD_BEARING_MAP rows naming each document: RCURVE %s ; INDEX_ARITY %s ; ADDITIVE_MULTIPLICATIVE %s' % (
        lines_with(None, r'RCURVE', mp), lines_with(None, r'INDEX_ARITY|IDX\b', mp), lines_with(None, r'ADDITIVE|CONSPIR|AMC\b', mp)), '']
    cite(L, CENSUS, 279, 279, 'THE_KEYSTONE_CENSUS.md -- v0.2`s roster')
    cite(L, ERR, 483, 492, 'ERRATA.md -- E-2026-09-25-1')
    cite(L, ERR, 754, 764, 'ERRATA.md -- E-2026-09-27-1')
    ot = rd(OT).split(NL)
    for wid, lns in WORK:
        for ln in lns:
            L += ['### OPEN_TRAILS.md:%d -- %s named on the line: %s' % (ln, wid, wid in ot[ln - 1]), '  :%d %s' % (ln, ot[ln - 1][:700]), '']
    cr = blob(RCK, 'd5f33b4:SIDERCurve/Criterion.lean')
    cite(L, os.path.join(RCK, 'SIDERCurve', 'Criterion.lean'), 1, len(cr.split(NL)), 'SIDE-rcurve v0.1.0 = d5f33b4 -- Criterion.lean whole', text=cr)
    bd = {k: lines_with(dp(k), r'bd2ae1a') for k in DOCS}
    L += ['### `bd2ae1a` in the batch documents: %s' % bd]
    put_json('b556_bd2.json', dict(hits=bd, total=sum(len(v) for v in bd.values())))
    put_txt('b556_reads.txt', L)
    print('  reads banked : %d lines ; bd2ae1a hits %s' % (len(L), bd))


# ------------------------------------------------------------------------------ READING (2): THE CRITICAL PATH
PH = ('### The critical path after the cascade`s ninth act: lane one CP-1 close and CP-1b, lane two the five work-orders in '
      'dependency order, lane three the clarified layer -- entered 2026-09-28, b556, under the author`s ruling (R166)(2)')
FPL = '*Appended 2026-09-28 by b556, under the author`s ruling `(R166)`(2) -- THE CRITICAL PATH:*'
PRICE = [
    ('(a)', 'W-ORD-DETECTION-REGION', 'four lemmas by the PowerLimit finite-j₀ route, one of substance (P1, the explicit j₀ inequality); the closed-form route '
     'priced beside it at three of substance', [11151, 11332]),
    ('(b)', 'W-ORD-LI-WEIL-BRIDGE', 'T1-T9 by the truncation route inside SIDE-explicit-formula, the paired-sum hazard at T6 (the zero sum grouped by ρ and '
     '1 − ρ̄); its leading item the explicit formula on a class wider than EF_lit`s; the toolchain forward F1-F4 priced above it and not the route; '
     'three consumers (the residue premise, the two detection costs, the Li form made T0)', [3548, 11203, 11230, 11265, 11290]),
    ('(c)', 'W-ORD-GRH-WEIL', '31: six new items and 25 re-instantiated theorems of the ζ-side arc, against that arc`s 211', [11373]),
    ('(d)', 'W-ORD-POWER-SWEEP', 'about 9287 s of cells at b548`s cost, a new window class (the n-th convolution power), tail constants re-derived, a '
     'fixture; it runs when the self-convolution class exists in the ladder', [11195]),
    ('(e)', 'W-ORD-WINDOW-CERTIFY', 'four items, a verified quadrature lemma the one of substance; not scheduled', [11152]),
    ('housekeeping', 'W-ORD-SEAM-UPSTREAM', 'one Mathlib-shaped lemma priced for upstream; trigger the author`s word', [10972]),
    ('housekeeping', 'W-ORD-STORMER-CLASH', 'one test module renamed and a fresh profile; trigger the next SIDE-kernel tag', [11257]),
]


def r166_2():
    t = rd(os.path.join(D, 'b556_ferry.txt'))
    seg = t[t.index('(2) THE THREE LANES, in order.'): t.index('(3) BATCH ONE.')].strip()
    return [' '.join(p.split()) for p in seg.split(NL + NL) if p.strip()]


def path():
    guard_absent(OT, PH)
    guard_absent(FIND, FPL)
    ot = rd(OT).split(NL)
    for _, wid, _, lns in PRICE:
        for ln in lns:
            assert wid in ot[ln - 1], (wid, ln)
    paras = r166_2()
    L = ['', PH, '', '**(R166)(2), verbatim** (relay `data/b556_ferry.txt`, its hard wrap joined, one paragraph per lane):', '']
    L += [x for p in paras for x in ('> ' + p, '>')][:-1]
    L += ['', '**Each work-order`s current price, cited to its trail line (each line re-read at this write, its ID on it):**', '',
          '| lane | work-order | the current price | trail line(s) |', '|:--|:--|:--|:--|']
    L += ['| %s | `%s` | %s | %s |' % (a, w, p, ', '.join(':%d' % x for x in lns)) for a, w, p, lns in PRICE]
    L += ['', '**Lane one, in acts:** b556 (this act) tiers R_CURVE_CRITERION, INDEX_ARITY_AT_THE_CRITICAL_LINE and '
          'ADDITIVE_MULTIPLICATIVE_CONSPIRACY; b557 the eight method keystones; b558 is CP-1b, the implication pass; then the seat`s '
          'memory and the mirror are refreshed per `(R157)`(6) and the author clears the seat`s context at that boundary.', '',
          '*Entered, not started: no work-order is begun at b556. `h2` stands where the deposit left it.*', '']
    o = append_to(OT, NL.join(L))
    o['line'] = line_of(OT, PH)
    f = append_to(FIND, NL.join(['', FPL + ' the critical path after the cascade`s ninth act -- lane one the close of CP-1 and CP-1b, lane two '
                                 'the five work-orders in dependency order with their prices cited to their trail lines, lane three the clarified '
                                 'layer -- is entered at `OPEN_TRAILS.md`:%d with `(R166)`(2) verbatim; no work-order is started.' % o['line'], '']))
    f['line'] = line_of(FIND, FPL)
    put_json('b556_path.json', dict(trail=o, pointer=f, paragraphs=len(paras), work=[(w, lns) for _, w, _, lns in PRICE]))
    print(NL.join(rd(OT).split(NL)[o['line'] - 1:])); print(f)


# ------------------------------------------------------------------------------ READING (3): THE ROWS AND THE TERMINALS
S = 'SIDELvConservation.'
RP = S + 'RegisterPentagon.'
M1 = 'SIDEEffects.Phase15.Module1.'
RC = 'SIDERCurve.'
# ### row line -> [(qualified name, pin probe, current-tag probe or None)] -- checked against the cells by `rows`
ROWMAP = {
    'RCURVE': {349: [(RC + 'monotone_unique_zero', 'r1', None), (RC + 'online_zero_codim_one', 'r1', None), (RC + 'offline_zero_codim_two', 'r1', None)],
               350: [('SIDEDerivative.exactly_c1_derives', 'kd', None)], 351: [('SIDEDerivative.onLine_doubleZero_iff_imDeriv_zero', 'kd', None)],
               352: [('SIDEDerivative.no_onLine_double_iff_transversal', 'kd', None)],
               353: [(S + 'exists_norm_completedRiemannZeta₀_le_exp', 'l1', 'l1t')],
               354: [(S + 'PartialPositivity.blTerm_nonneg_of_onLine', 'l2', 'l2t')],
               355: [(S + 'PartialPositivity.partialPositivity_finiteRange', 'l2', 'l2t')],
               356: [(S + 'exists_norm_completedLFunction_le_exp', 'l3', 'l3t')], 357: [(S + 'h1_complete_at_Phi', 'l4', 'l4t')],
               358: [(RP + 'R4_positivity_to_RH', 'l5', 'l5t')], 359: [(S + 'C7_finite_type_false', 'l6', 'l6t')], 360: []},
    'INDEX': {369: [('ConservationBridge.riemann_hypothesis', 'k1', None)], 370: [(S + 'C7_finite_type_false', 'm1', 'm1t')],
              371: [(S + 'T3.T3doubleprime_general_commutation_fails', 'm2', 'm2t')], 372: [(RP + 'certifiedInput_not_zeroRealizing', 'm3', 'm3t')],
              373: [(RP + 'escape_kind_discriminates', 'm4', 'm4t'), (RP + 'horizon_kind_shared', 'm4', 'm4t')],
              374: [('InvarianceBarrier.derivability_barrier', 'k2', None)], 375: [('SieveCeilingWitness.dh_witness', 'k3', None)],
              376: [], 377: [], 378: [], 379: [],
              380: [(RP + 'edge_drift_nonneg', 'm4', 'm4t'), (RP + 'edge_drift_neg_for_signNeutral', 'm4', 'm4t')],
              381: [(S + 'CompositionBarrier.composition_barrier', 'm5', 'm5t'), (S + 'CompositionBarrier.barrier_witnesses', 'm5', 'm5t')], 382: [],
              383: [(S + 'LeadLaw.lead_law', 'n1', None), (S + 'FieldLayer.top_coeff_of_expansion', 'n1', None), (S + 'FieldLayer.norml_top', 'n1', None),
                    (S + 'LeadLaw.leadingCoeff_hOf', 'n1', None)],
              384: [(S + 'Genus5.classification', 'n2', None), (S + 'Genus5Confinement.golay_confined', 'n3', None),
                    (S + 'Genus5Confinement.w16_confined', 'n3', None), (S + 'Genus5Confinement.e8_confined', 'n3', None)],
              385: [(S + 'TwoSides.' + x, 'n4', None) for x in ('heine_three', 'heine_one', 'heine_two', 'ladder_three', 'two_sides_balance')],
              **{x: [] for x in range(386, 398)}},
    'AMC': {408: [(M1 + 'no_type_d_conspiracies', 'e1', None), (M1 + 'crt_exhaustiveness', 'e1', None)], 409: [('AddMult.no_type_d', 'e3', None)],
            410: [('AddMult.no_conspiracy_twins', 'e3', None), ('AddMult.no_conspiracy_goldbach', 'e3', None), ('AddMult.no_conspiracy_sg', 'e3', None)],
            411: [('AddMult.twin_primes_infinite', 'e4', None)], 412: [('AddMult.goldbach', 'e4', None)], 413: [('AddMult.sophie_germain_infinite', 'e4', None)],
            414: [('ECondition.type_I_has_ostrowski', 'k6', 'k6t')], 415: [('SilenceTheorem.silence_universal', 'k7', 'k7t')],
            446: [(M1 + 'no_type_d_conspiracies', 'e2', None)], 447: [], 448: [], 449: [], 450: [], 451: []},
}
ROWNOTE = {('INDEX', 380): 'the row names no commit ("deposited line"); read on the release line, main = v0.11.0 = 2f71068, and at 5a14205 where '
                          'both are present; both are ABSENT at the deposit tag v0.10.0 = 93c27ec (printed)',
           ('AMC', 408): 'the kernel cell names c66f3c5; the profile cell says the profile was run at a27415d, and the row is compared there; '
                         'c66f3c5 printed beside it'}
HEADS = {'RCURVE': '| Claim | Kernel / pin |', 'INDEX': '| Claim (as stated here) |', 'AMC': ('| Claim | Kernel | Theorem', '| claim | kernel |')}


def short(n):
    return n.split('.')[-1]


def rows():
    out = {}
    for k in DOCS:
        src = blob(PP, PRIOR_PP + ':' + DOCS[k]).split(NL)
        heads = HEADS[k] if isinstance(HEADS[k], tuple) else (HEADS[k],)
        rs = []
        for h in heads:
            hi = [i for i, l in enumerate(src) if l.startswith(h)][0]
            for i in range(hi + 2, len(src)):
                l = src[i]
                if not l.startswith('|'):
                    break
                c = [x.strip() for x in l.strip().strip('|').split('|')]
                names = ROWMAP[k].get(i + 1)
                assert names is not None, (k, i + 1, 'a row the map lacks')
                for n, _, _ in names:
                    assert short(n) in (c[2] + c[3]).replace('\\', ''), (k, i + 1, n)
                cellnames = re.findall(r'`((?:[A-Za-z0-9_]+\.)*[a-z_][A-Za-z0-9_₀]*)`', c[2])
                rs.append(dict(line=i + 1, table=h, claim=c[0], kernel=c[1], terminal_cell=c[2], profile_cell=c[3], status=c[4][:700],
                               names=[n for n, _, _ in names], probes=[(p, t) for _, p, t in names], cell_names=cellnames))
        assert sorted(r['line'] for r in rs) == sorted(ROWMAP[k]), (k, 'map and table disagree')
        out[k] = rs
        print('  %s : rows %d ; naming a terminal %d ; terminals %d' % (k, len(rs), sum(1 for r in rs if r['names']), sum(len(r['names']) for r in rs)))
    put_json('b556_rows.json', out)


# ------------------------------------------------------------------------------ THE TIERS
STD3 = 'depends on axioms: [propext, Classical.choice, Quot.sound]'
PQ = 'depends on axioms: [propext, Quot.sound]'
NONE_AX = 'does not depend on any axioms'
NA = 'T0, not RH-anchor: '
ORDER = ['T0', 'T1-open', 'T1-lit', 'T2', 'T2-INTERFACES', 'T3', 'T4']
NAMEREAD = 'that the objects are the R-curve`s is carried by the identifiers (b540`s reading of `monotone_unique_zero`)'
# ### name -> (tier, reason, zero-in-conclusion: None | EXPLICIT | BY-DEFINITION | PER-ZERO)
TERMS = {
    RC + 'monotone_unique_zero': ('T2', 'a strictly monotone V : ℝ → ℝ vanishes at most once -- one direction over an abstract V; ' + NAMEREAD, None),
    RC + 'monotonicity_formula': ('T2', 'α²/β + β = (α² + β²)/β over ℝ -- field algebra; ' + NAMEREAD, None),
    RC + 'beta_V_re': ('T2', 'Re((α + βi)/(Vi)) = β/V for real α, β, V ≠ 0 -- arithmetic in ℂ; that α + βi is ξ′ and iV is ξ on the curve is carried by the identifiers', None),
    RC + 'singular_repulsion': ('T2', '0 < n/β from 0 < n and 0 < β -- `div_pos`; ' + NAMEREAD, None),
    RC + 'online_zero_codim_one': ('T2', '`zero_codim true = 1` by `rfl` over a function the file defines -- a stipulation', None),
    RC + 'offline_zero_codim_two': ('T2', '`zero_codim false = 2` by `rfl` over a function the file defines -- a stipulation', None),
    RC + 'second_zero_breaks_monotone': ('T2', 'a strictly monotone V has no second zero -- `monotone_unique_zero` again; ' + NAMEREAD, None),
    RC + 'zero_codim': ('T2', 'a definition: `if onLine then 1 else 2`', None),
    'SIDEDerivative.exactly_c1_derives': ('T2', 'a count over a grade map the file itself defines -- a stipulation (b554)', None),
    'SIDEDerivative.onLine_doubleZero_iff_imDeriv_zero': ('T0', NA + 'for complex z with Re z = 0, z = 0 ↔ Im z = 0 -- a fact about ℂ (b554)', None),
    'SIDEDerivative.no_onLine_double_iff_transversal': ('T0', NA + 'for complex z with Re z = 0, z ≠ 0 ↔ Im z ≠ 0 -- a fact about ℂ; simplicity is not a hypothesis (b554)', None),
    S + 'exists_norm_completedRiemannZeta₀_le_exp': ('T0', NA + 'the order-≤1 growth of Mathlib`s `completedRiemannZeta₀`, no premise', None),
    S + 'PartialPositivity.blTerm_nonneg_of_onLine': ('T0', NA + '0 ≤ Re[1 − (1 − 1/ρ)^n] at a zero with Re ρ = 1/2 -- a fact about on-line zeros', 'PER-ZERO'),
    S + 'PartialPositivity.partialPositivity_finiteRange': ('T1-lit', 'INTERFACES on `ExplicitFormulaDecomp` (Bombieri–Lagarias) and `TailBoundPremise` (Voros), '
                                                         'literature theorems not compiled, and the numerical `VerifiedZerosTo T` (b540, b554)', None),
    S + 'exists_norm_completedLFunction_le_exp': ('T0', NA + 'the order-≤1 growth of Mathlib`s `completedLFunction`, no premise but χ ≠ 1', None),
    S + 'h1_complete_at_Phi': ('T0', NA + 'the eight coupling facts of lv`s theta-kernel `Phi`, built from Mathlib`s `evenKernel` (b539, b554)', None),
    RP + 'R4_positivity_to_RH': ('T1-lit', 'INTERFACES on Li`s criterion (`Register4_positivity lam → RiemannHypothesis`), a literature theorem not in Mathlib (b540)', 'EXPLICIT'),
    S + 'C7_finite_type_false': ('T0', NA + '¬ ∃ C A, ∀ s, ‖completedRiemannZeta₀ s‖ ≤ C·exp(A‖s‖)', None),
    'ConservationBridge.riemann_hypothesis': ('T2', 'INTERFACES on `ConservationHypothesis`, which is RH restated (`ch_iff_rh`; E-2026-09-25-1): ENCODES-CONCLUSION (b539-b541)', 'EXPLICIT'),
    S + 'T3.T3doubleprime_general_commutation_fails': ('T0', NA + 'a countermodel against Mathlib`s `mellin` at s = 3 (b554; b545`s T2 superseded at b555)', None),
    RP + 'certifiedInput_not_zeroRealizing': ('T1-lit', 'INTERFACES on its one named classical premise `NontrivialZeroExistsInStrip` (∃ σ, is_xi_zero σ ∧ 0 < σ < 1), '
                                               'a literature theorem (Riemann`s computed zeros; Hardy 1914) not compiled -- the tier follows the premise`s kind (b540)', 'BY-DEFINITION'),
    RP + 'escape_kind_discriminates': ('T2', '`decide` over an enumeration the file defines (`wallEscapeKind`) -- a stipulation (b549)', None),
    RP + 'horizon_kind_shared': ('T2', '`decide` over the same enumeration (b549)', None),
    'InvarianceBarrier.derivability_barrier': ('T2', 'a general schema over an abstract α with `agree`, `P` and the file`s `Derives` -- logic; the toolkit and Epstein readings are '
                                               'carried by names (the row: no ξ/Epstein instantiation)', None),
    'SieveCeilingWitness.dh_witness': ('T2', 'over the file`s `Config`, `iIndist` and `allOnLine`, whose value at `.dh` is the stipulated Davenport–Heilbronn datum', None),
    RP + 'edge_drift_nonneg': ('T2', 'nonnegativity of the file`s `driftSum` for nonnegative ledger and weights -- over an abstract ledger (b549)', None),
    RP + 'edge_drift_neg_for_signNeutral': ('T2', 'a negative `driftSum` for the file`s model ledger `dhModelLedger` (b549)', None),
    S + 'CompositionBarrier.composition_barrier': ('T2', 'over the file`s `SymForm` (2×2 forms) and `DerivesFromCriterion` -- the model-level schema the row names', None),
    S + 'CompositionBarrier.barrier_witnesses': ('T2', 'two explicit `SymForm`s the file defines agree on the diagonal, one a carrier, one not', None),
    S + 'LeadLaw.lead_law': ('T2', 'over the file`s `hOf`, `norml` and `IsExpansion` for an arbitrary p with `SelfDualFE q g p` as a hypothesis -- no literature theorem is '
                             'assumed or applied; that p is a code`s zeta polynomial is carried by the names', None),
    S + 'FieldLayer.top_coeff_of_expansion': ('T2', 'the top coefficient of the file`s `IsExpansion` -- over programme-defined objects', None),
    S + 'FieldLayer.norml_top': ('T2', 'the top normalized coefficient of the file`s `norml` under `SelfDualFE` -- over programme-defined objects', None),
    S + 'LeadLaw.leadingCoeff_hOf': ('T2', 'Mathlib`s `leadingCoeff` of the file`s `hOf` -- over a programme-defined polynomial', None),
    S + 'Genus5.classification': ('T2', 'arithmetic over the file`s structure `TypeIIParams`, whose field `MS` stipulates the Mallows–Sloane bound', None),
    S + 'Genus5Confinement.golay_confined': ('T2', 'the roots of an explicit real polynomial the file defines lie in (0, 4); that it is the Golay certificate and that (0, 4) '
                                              'transports to Duursma`s circle (not compiled, the row`s shortfall) are carried by names', None),
    S + 'Genus5Confinement.w16_confined': ('T2', 'as `golay_confined`, for the file`s `Hw16`', None),
    S + 'Genus5Confinement.e8_confined': ('T2', 'as `golay_confined`, for the file`s `He8`', None),
    S + 'TwoSides.heine_three': ('T0', NA + 'the Heine/Vandermonde identity at depth 3 as a polynomial identity over ℚ in six free variables -- the spectral side', None),
    S + 'TwoSides.heine_one': ('T0', NA + 'the identity at depth 1 over ℚ', None),
    S + 'TwoSides.heine_two': ('T0', NA + 'the identity at depth 2 over ℚ', None),
    S + 'TwoSides.ladder_three': ('T2', 'restates the Hankel-ratio definition, closed by `field_simp` -- no second route (the row`s own words)', None),
    S + 'TwoSides.two_sides_balance': ('T0', NA + 'the depth-3 identity at an explicit rational measure, the value non-zero -- a computation over ℚ', None),
    M1 + 'no_type_d_conspiracies': ('T2', 'the ferry`s criterion ((R166) COMPONENT 4): `IsEmpty TypeD`, TypeD a programme-defined type over `StructuralCoupling` -- '
                                   'not over Mathlib types; b555 banked T0, the difference flagged for the author', None),
    M1 + 'crt_exhaustiveness': ('T2', 'the ferry`s criterion: bound variables range over the programme types `StructuralCoupling` and `ModularCoupling`; the '
                                'content, per b433, is the periodic lift at the coupling`s own modulus; b555 banked T0, the difference flagged for the author', None),
    'AddMult.no_type_d': ('T2', 'a propositional schema over an arbitrary α with `coupling`, `modular` -- logic whose weight is its hypothesis', None),
    'AddMult.no_conspiracy_twins': ('T2', 'SHELL: `TypeD Nat (fun _ => True) (fun _ => True)` refuted -- uniformly-True predicates', None),
    'AddMult.no_conspiracy_goldbach': ('T2', 'SHELL: as `no_conspiracy_twins`', None),
    'AddMult.no_conspiracy_sg': ('T2', 'SHELL: as `no_conspiracy_twins`', None),
    'AddMult.twin_primes_infinite': ('T4', 'proved by `sorry` (sorryAx): the statement, over Mathlib`s `Nat.Prime`, is the open conjecture itself; it establishes nothing', None),
    'AddMult.goldbach': ('T4', 'proved by `sorry` (sorryAx): the statement is binary Goldbach itself', None),
    'AddMult.sophie_germain_infinite': ('T4', 'proved by `sorry` (sorryAx): the statement is the Sophie Germain conjecture itself', None),
    'ECondition.type_I_has_ostrowski': ('T2', 'modus tollens over an abstract `Domain` whose `[Fintype Domain]` is never used -- logic alone (b539, b555)', None),
    'SilenceTheorem.silence_universal': ('T2-INTERFACES', 'INTERFACES on `I.is_universal`, a programme structure`s property the manuscript asserts ((R165)(3); b555)', None),
}
EARLIER = {RC + 'monotone_unique_zero': ('T2', 'b540_tiers.json'), RP + 'R4_positivity_to_RH': ('T1-lit', 'b540_tiers.json'),
           RP + 'certifiedInput_not_zeroRealizing': ('T1-lit', 'b540_tiers.json'), 'ConservationBridge.riemann_hypothesis': ('T2', 'b539_tiers.json, b540_tiers.json'),
           RP + 'escape_kind_discriminates': ('T2', 'b549_tiers.json'), RP + 'horizon_kind_shared': ('T2', 'b549_tiers.json'),
           RP + 'edge_drift_nonneg': ('T2', 'b549_tiers.json'), RP + 'edge_drift_neg_for_signNeutral': ('T2', 'b549_tiers.json'),
           'SIDEDerivative.exactly_c1_derives': ('T2', 'b554_simp_tiers.json'), 'SIDEDerivative.onLine_doubleZero_iff_imDeriv_zero': ('T0', 'b554_simp_tiers.json'),
           'SIDEDerivative.no_onLine_double_iff_transversal': ('T0', 'b554_simp_tiers.json'), S + 'h1_complete_at_Phi': ('T0', 'b554_simp_tiers.json'),
           S + 'PartialPositivity.partialPositivity_finiteRange': ('T1-lit', 'b554_simp_tiers.json'), S + 'exists_norm_completedLFunction_le_exp': ('T0', 'b554_simp_tiers.json'),
           S + 'exists_norm_completedRiemannZeta₀_le_exp': ('T0', 'b554_simp_tiers.json'), S + 'PartialPositivity.blTerm_nonneg_of_onLine': ('T0', 'b554_simp_tiers.json'),
           S + 'C7_finite_type_false': ('T0', 'b554_simp_tiers.json'), S + 'T3.T3doubleprime_general_commutation_fails': ('T0', 'b554_simp_tiers.json'),
           M1 + 'no_type_d_conspiracies': ('T0', 'b555_tiers.json'), M1 + 'crt_exhaustiveness': ('T0', 'b555_tiers.json'),
           'ECondition.type_I_has_ostrowski': ('T2', 'b555_tiers.json'), 'SilenceTheorem.silence_universal': ('T2-INTERFACES', 'b555_tiers.json')}
ANCHOR = ['h2_sign_iff_rh', 'ch_iff_rh', 'not_register1', 'mellin_Phi_eq_zero_of_re_le_one', 'lvh2_corrected_iff', 'register5_output_holds', 'b321_identity', 'not_f4_needs']


def probes():
    out = {}
    p = os.path.join(D, 'b556_probes.jsonl')
    for l in (rd(p).split(NL) if os.path.exists(p) else []):
        if l.strip():
            r = json.loads(l)
            out[r['id']] = r
    return out


def ptext(pid):
    p = os.path.join(D, 'b556_probe_%s.txt' % pid)
    return rd(p) if os.path.exists(p) else ''


def resolve(pid, pr):
    """### a pin probe that exited non-zero is read from its control `<pid>b` when that control elaborated clean (defect (b))."""
    r = pr.get(pid, {})
    if r.get('exit') not in (0, None):
        for sfx in ('b', 'c'):
            c = pr.get(pid + sfx)
            if c and c.get('exit') == 0:
                return pid + sfx
    return pid


def check_text(pid, name, pr=None):
    pr = pr or probes()
    pid = resolve(pid, pr)
    r = pr.get(pid, {})
    if r.get('identical_to'):
        return check_text(r['identical_to'], name, pr)
    t = ptext(pid)
    i = t.find('@' + name + ' :')
    if i < 0:
        i = t.find(name + ' :')
    if i < 0:
        return None
    rest = t[i:]
    stop = [m.start() for m in re.finditer(r"(?m)^(@?[A-Za-z_][A-Za-z0-9_.₀]* : |'[A-Za-z_]|real |<stdin>|[a-z]+ [A-Za-z_.]+ :|def |theorem |structure )", rest)][1:2]
    return ' '.join(rest[:stop[0] if stop else 1500].split())


def fresh_profile(pid, name, pr):
    pid = resolve(pid, pr)
    r = pr.get(pid, {})
    if r.get('identical_to'):
        return fresh_profile(r['identical_to'], name, pr)
    return (r.get('profiles') or {}).get(name)


def found_at(pid, name, pr):
    pid = resolve(pid, pr)
    r = pr.get(pid, {})
    if r.get('identical_to'):
        return found_at(r['identical_to'], name, pr)
    return r.get('exit') == 0 and bool(check_text(pid, name, pr))


def row_profile(cell, name):
    c = cell.replace('`', '')
    if name.endswith('online_zero_codim_one') or name.endswith('offline_zero_codim_two'):
        return NONE_AX
    if '0 sorry, 0 axioms' in c:
        return NONE_AX
    if 'carries sorry' in c.lower():
        return 'SORRY'
    if 'catalogue {propext, Quot.sound}' in c:
        return PQ if name.endswith('classification') else STD3
    if '{propext, Classical.choice, Quot.sound}' in c:
        return STD3
    if '{propext, Quot.sound}' in c:
        return PQ
    if 'axiom-free' in c:
        return NONE_AX
    return None


def prof_eq(fresh, want):
    if want is None:
        return True
    if want == 'SORRY':
        return bool(fresh) and 'sorryAx' in fresh
    return fresh == want


def unused_warnings(pid, pr):
    """### every `unused variable` warning the elaborator printed, attributed to the enclosing declaration of the fed file."""
    r = pr.get(pid, {})
    if not r or r.get('identical_to') or r.get('inlined'):
        return []
    repo = os.path.join(DD, r['repo'])
    src = blob(repo, '%s:%s' % (r['full'], r['path'])).split(NL)
    out = []
    for m in re.finditer(r'<stdin>:(\d+):(\d+): warning: unused variable `([^`]+)`', ptext(pid)):
        ln = int(m.group(1))
        decl = None
        for j in range(min(ln, len(src)) - 1, -1, -1):
            dm = re.match(r'^\s*(?:private\s+|protected\s+)?(?:noncomputable\s+)?(?:theorem|lemma|def)\s+(\S+)', src[j])
            if dm:
                decl = dm.group(1)
                break
        out.append(dict(line=ln, var=m.group(3), decl=decl))
    return out


def tiers():
    rs = jl('b556_rows.json')
    pr = probes()
    ei = jl('b544_ei.json').get('marks', {})
    missing = sorted({pid for k in rs for r in rs[k] for (pid, tid) in r['probes'] for x in (pid, tid) if x and x not in pr})
    if missing:
        sys.exit('### PROBES NOT YET BANKED: %s' % missing)
    out, L = {}, ['b556 -- READING (3): THE CORRESPONDENCE ROWS OF THE BATCH, RE-READ AT PIN', '']
    L += ['### the probes (relay data/b556_probe_<id>.txt):']
    for pid, p in sorted(pr.items()):
        if p.get('identical_to'):
            L.append('    %-4s %-22s %-8s %-44s IDENTICAL to %s (the file and its imports byte-equal at the tag)' % (pid, p['repo'], p['pin'], p['path'], p['identical_to']))
        else:
            L.append('    %-4s %-22s %-8s %-44s mode %-10s exit %d %7.1f s errors %d manifest-equal %s imports %s' % (
                pid, p['repo'], p['pin'], p['path'], (p['mode'] or '')[:10], p['exit'], p['seconds'], p['errors'], p['manifest_same'], p['closure'] or 'NONE'))
    uw = {pid: unused_warnings(pid, pr) for pid in pr}
    for k in DOCS:
        terms, rows_out = [], []
        for r in rs[k]:
            tl, ok, why_row = [], True, []
            for (n, (pid, tid)) in zip(r['names'], r['probes']):
                if n not in TERMS:
                    sys.exit('### A TERMINAL WITHOUT A TIER: %s' % n)
                tier, reason, zero = TERMS[n]
                fnd = found_at(pid, n, pr)
                prof = fresh_profile(pid, n, pr)
                want = row_profile(r['profile_cell'], n)
                st = check_text(pid, n, pr)
                tag = None
                if tid:
                    tr = pr[tid]
                    tst = check_text(tid, n, pr)
                    tag = dict(probe=tid, pin=tr['pin'], identical=bool(tr.get('identical_to')), found=found_at(tid, n, pr),
                               same_statement=(tst == st) if tst and st else False, profile=fresh_profile(tid, n, pr))
                moved = [x for x, b in (('not found at its pin', not fnd),
                                        ('fresh profile %s against the row`s %s' % (prof, want), fnd and not prof_eq(prof, want)),
                                        ('statement differs at the tag %s' % (tag or {}).get('pin'), bool(tag) and not tag['same_statement'])) if b]
                decl_uw = [w for w in uw.get(pid, []) if w['decl'] and w['decl'].split('.')[-1] == short(n)]
                terms.append(dict(row=r['line'], name=n, probe=resolve(pid, pr), probe_first=pid, pin=pr[pid]['pin'], found=fnd, statement=st, profile=prof, row_profile=want,
                                  tier=tier, reason=reason, zero=zero, tag=tag, earlier=EARLIER.get(n), moved=moved, unused=decl_uw,
                                  ei=ei.get('%s|%s' % (pr[pid]['repo'], n), 'not indexed')))
                tl.append(tier)
                ok = ok and not moved
                why_row += ['%s: %s' % (short(n), '; '.join(moved)) for _ in [0] if moved]
            ruling = k == 'INDEX' and 'ConservationBridge.riemann_hypothesis' in r['names'] and 'the reduction' in r['status']
            if ruling:
                why_row.append('(R166)(3)(i): the row calls the terminal "the reduction"; its premise is RH restated (E-2026-09-25-1) and the programme`s compiled '
                               'reduction of RH is `h2_sign_iff_rh`')
            rt = max(tl, key=ORDER.index) if tl else 'T4'
            rows_out.append(dict(line=r['line'], table=r['table'], claim=r['claim'], names=r['names'], tiers=tl, tier=rt,
                                 disp='CARRIED' if (ok and not ruling) else 'MOVED', why=why_row, kernel=r['kernel'], note=ROWNOTE.get((k, r['line']))))
        tc = {x: sum(1 for t in terms if t['tier'] == x) for x in ORDER}
        rc = {x: sum(1 for r in rows_out if r['tier'] == x) for x in ORDER}
        dc = {x: sum(1 for r in rows_out if r['disp'] == x) for x in ('CARRIED', 'MOVED')}
        out[k] = dict(rows=rows_out, terms=terms, term_tiers=tc, row_tiers=rc, disp=dc)
        L += ['', '=' * 100, '### %s (%s at PLACE-papers %s): %d rows; %d name a terminal; %d terminal readings' % (
            TITLE[k], DOCS[k], PRIOR_PP, len(rows_out), sum(1 for r in rows_out if r['names']), len(terms)), '=' * 100]
        for t in terms:
            L += ['', '### :%d %s [%s at %s via %s]' % (t['row'], t['name'], 'FOUND' if t['found'] else 'NOT FOUND', t['pin'], t['probe']),
                  '    statement : %s' % (t['statement'] or 'NONE')[:1000],
                  '    profile   : %s   (the row prints: %s)' % (t['profile'], t['row_profile']),
                  '    at the tag: %s' % (t['tag'] or 'no tag beyond the pin'),
                  '    tier      : %s -- %s' % (t['tier'], t['reason']),
                  '    earlier   : %s ; E/I (b544) : %s' % ('%s (relay data/%s)' % t['earlier'] if t['earlier'] else 'none banked', t['ei']),
                  '    unused-variable warnings in the declaration: %s' % (t['unused'] or 'NONE'),
                  '    a zero of ζ in the conclusion: %s' % (t['zero'] or 'no'),
                  '    disposition: %s' % ('CARRIED' if not t['moved'] else 'MOVED -- ' + '; '.join(t['moved']))]
        L += ['', '### ROWS:'] + ['    :%d %-8s %-14s %s%s' % (r['line'], r['disp'], r['tier'], r['claim'][:70], ('  -- ' + ' | '.join(r['why'])) if r['why'] else '')
                                   for r in rows_out]
        L += ['### TIERS OVER THE %d TERMINAL READINGS: %s' % (len(terms), ' · '.join('%s %d' % (x, tc[x]) for x in ORDER)),
              '### ROW TIERS (the weakest link; no terminal T4): %s' % ' · '.join('%s %d' % (x, rc[x]) for x in ORDER),
              '### DISPOSITIONS: CARRIED %d · MOVED %d' % (dc['CARRIED'], dc['MOVED'])]
    allw = [dict(probe=pid, **w) for pid, ws in uw.items() for w in ws]
    out['unused_all'] = allw
    out['probes'] = {k: dict(exit=v.get('exit'), seconds=v.get('seconds'), errors=v.get('errors'), identical_to=v.get('identical_to')) for k, v in pr.items()}
    L += ['', '### EVERY UNUSED-VARIABLE WARNING THE PROBES PRINTED (all declarations of the fed files): %d' % len(allw)] + ['    %s' % w for w in allw]
    put_json('b556_tiers.json', out)
    put_txt('b556_tiers.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ READING (4), (8), (9): R_CURVE`S KERNEL, THE PINS, THE CITATIONS
def rcurve():
    src = blob(RCK, 'd5f33b4:SIDERCurve/Criterion.lean')
    decls = [(i + 1, m.group(1), m.group(2)) for i, l in enumerate(src.split(NL)) for m in [re.match(r'^(theorem|lemma|def|structure|inductive|abbrev)\s+(\S+)', l)] if m]
    files = [f for f in g(RCK, 'ls-tree', '-r', '--name-only', 'd5f33b4').split(NL) if f.endswith('.lean')]
    pr = probes()
    rows_ = []
    for ln, kind, n in decls:
        q = RC + n
        tier, reason, _ = TERMS[q]
        rows_.append(dict(line=ln, kind=kind, name=q, tier=tier, reason=reason, profile=fresh_profile('r1', q, pr), statement=check_text('r1', q, pr),
                          xi_or_holomorphic=False))
    split = {x: sum(1 for r in rows_ if r['tier'] == x) for x in ORDER}
    L = ['b556 -- READING (4): SIDE-rcurve v0.1.0 = d5f33b4, EVERY DECLARATION', '', '### the tree`s Lean files: %s' % files,
         '### the library`s declarations (SIDERCurve/Criterion.lean; SIDERCurve.lean and AxiomCheck.lean declare nothing): %d' % len(rows_)]
    for r in rows_:
        L += ['    :%-3d %-8s %-45s %-4s %s' % (r['line'], r['kind'], short(r['name']), r['tier'], r['profile']), '        statement: %s' % (r['statement'] or 'NONE')[:400],
              '        about ξ on the line or a general holomorphic function: NO ; ' + r['reason']]
    L += ['### THE SPLIT: %s ; statements about ξ on the line or a general holomorphic function: 0 -- (N3)`s exception clause is VACUOUS' % split]
    # ### READING (8): the pins` branches and tags; READING (9): the name citations
    pins = {}
    for c in ('a27415d', 'c66f3c5'):
        pins[c] = dict(branches=[b.strip().lstrip('* ') for b in g(EFF, 'branch', '-a', '--contains', c).split(NL) if b.strip()],
                       tags=[t for t in g(EFF, 'tag', '--contains', c).split(NL) if t.strip()], date=g(EFF, 'show', '-s', '--format=%ci %s', c).strip()[:150],
                       module1_imports=re.findall(r'(?m)^import\s+(\S+)', blob(EFF, c + ':SIDEEffects/Phase15/Module1.lean')))
    etags = {t: g(EFF, 'rev-parse', '--short', t + '^{commit}').strip() for t in g(EFF, 'tag').split() if t}
    cites = {}
    for repo, want in (('SIDE-meta', 'v0.3'), ('SIDE-silence-principle', 'v0.1'), ('SIDE-compression', 'v0.1')):
        rp = os.path.join(DD, repo)
        tags = g(rp, 'tag').split()
        exact = g(rp, 'rev-parse', '--verify', '-q', want + '^{commit}').strip()
        cites[repo] = dict(cited=want, tags=tags, exact=exact[:7] or None,
                           nearest=[t for t in tags if t.startswith(want + '.') or t == want],
                           resolved=('pin: tag %s = %s' % (want, exact[:7])) if exact else 'CITATION BY NAME WITHOUT A PIN (no tag `%s`; tags %s)' % (want, tags))
    mil = {}
    for c in ('c66f3c5', 'a27415d'):
        m = blob(EFF, c + ':SIDEEffects/Milestones.lean')
        mil[c] = {n: dict(line=lines_with(None, r'^theorem %s\b' % n, m), sorry=bool(re.search(r'theorem %s\b[\s\S]*?:= by\s*\n\s*sorry' % n, m)))
                  for n in ('twin_primes_infinite', 'goldbach', 'sophie_germain_infinite')}
    lvabs = {c: bool(g(LV, 'grep', '-l', 'theorem edge_drift_nonneg', c, '--', 'SIDELvConservation').strip()) for c in ('93c27ec', '14720d9', '5a14205', '2f71068')}
    L += ['', 'b556 -- READING (8): THE SIDE-effects PINS']
    for c, v in pins.items():
        L += ['    %s : %s' % (c, v)]
    L += ['    SIDE-effects tags: %s' % etags, '    Milestones.lean: %s' % mil,
          '', 'b556 -- READING (9): THE NAME CITATIONS'] + ['    %s %s : %s' % (k, v['cited'], v['resolved']) for k, v in cites.items()]
    L += ['', '### INDEX :380`s terminals on SIDE-lv-conservation (edge_drift_nonneg present): %s' % lvabs]
    put_json('b556_rcurve.json', dict(decls=rows_, split=split, files=files, pins=pins, effects_tags=etags, citations=cites, milestones=mil, edge_drift=lvabs))
    put_txt('b556_rcurve.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ READING (5), (7), (10): THE BLOCKS
BH = ('#### THE CASCADE, ACT TEN -- THE CORRESPONDENCE TIERED *(appended 2026-09-28, b556, under the author`s ruling `(R166)`(3); no byte '
      'above this block changes; the body is not edited)*')


def cleanclaim(c):
    import banned_terms as BTM
    c = re.sub(r'\$[^$]*\$', '…', c).replace('|', '/').replace('**', '').replace('###', '').replace('`', '')
    c = re.sub(r'\s*\S*' + BTM.PAT.pattern + r'\S*', '', c, flags=re.I)
    return ' '.join(c.split())


def table(s):
    L = ['| row | claim (abridged) | terminal(s) | fresh profile(s) | disposition | tier(s) |', '|:--|:--|:--|:--|:--|:--|']
    for r in s['rows']:
        ts = [t for t in s['terms'] if t['row'] == r['line']]
        prof = sorted(set((t['profile'] or 'NONE').replace('depends on axioms: ', '').replace('does not depend on any axioms', 'axiom-free') for t in ts))
        L.append('| :%d | %s | %s | %s | **%s** | %s |' % (r['line'], cleanclaim(r['claim'])[:90], ', '.join('`%s`' % short(t['name']) for t in ts) or 'NONE',
                                                          '; '.join(prof) or '—', r['disp'], ', '.join(sorted(set(r['tiers']), key=ORDER.index)) or 'T4'))
    L += ['', '*Tiers over the %d terminal readings: %s. Rows by their weakest link: %s. Dispositions: CARRIED %d · MOVED %d.*' % (
        len(s['terms']), ' · '.join('%s %d' % (k, s['term_tiers'][k]) for k in ORDER), ' · '.join('%s %d' % (k, s['row_tiers'][k]) for k in ORDER),
        s['disp']['CARRIED'], s['disp']['MOVED'])]
    return L


def moved_lines(s):
    return ['*Row :%d MOVED:* %s' % (r['line'], '; '.join(r['why'])) for r in s['rows'] if r['disp'] == 'MOVED']


def overhyp_paragraph(ts):
    allw = ts['unused_all']
    mine = [(k, t['name'], t['unused']) for k in DOCS for t in ts[k]['terms'] if t['unused']]
    prem = [(k, n, u) for k, n, u in mine if TERMS[n][0] in ('T1-lit', 'T1-open', 'T2-INTERFACES')]
    return ('**OVER-HYPOTHESIZED, read against the tier law (READING (7)).** The grade (:365) is met when a statement carries a hypothesis its proof '
            'does not use, and its test is stated there as "a check, not a reading: delete the hypothesis and recompile". The cascade`s two marks read '
            'the statement: the E/I mark sorts the conclusion`s kind, and the tier reads what the statement assumes and concludes -- a hypothesis present '
            'is read as load-bearing. So the grade is not detected by the statement-read; it is a proof-side check. Nor is it a fourth axis of the tier: '
            'deleting an unused hypothesis over Mathlib`s objects or an instance argument leaves the tier where it was, and the one case that could move a '
            'tier is an unused NAMED premise that sets the weakest link (T1-lit, T1-open, T2-INTERFACES), whose deletion would lower the tier -- there the '
            'grade corrects the tier rather than adding to it. The measure beside this reading: the elaborator printed %d unused-variable warning(s) across '
            'the probed files; %d fall inside a terminal of these three tables (%s); %d on a named premise that sets a tier. The count is a floor, not the '
            'grade`s test: an unused instance argument draws no such warning, and the grade`s own first application -- `ECondition.type_I_has_ostrowski`, '
            'its `[Fintype Domain]` never used (ADDITIVE_MULTIPLICATIVE_CONSPIRACY :414) -- is invisible to it; the linters were live in the probes (the '
            'unused-simp-argument and unused-tactic linters printed in two of them). The delete-and-recompile test was not run.' % (len(allw), len(mine), '; '.join('%s `%s`: %s' % (k, short(n), ', '.join(w['var'] for w in u)) for k, n, u in mine) or 'none',
                              len(prem)))


def blocks():
    ts = jl('b556_tiers.json')
    rc = jl('b556_rcurve.json')
    bd = jl('b556_bd2.json')
    out = {}
    done = {k for k in DOCS if poss(BH).encode('utf-8') in open(dp(k), 'rb').read()}   # ### a block already appended is not appended again
    print('  blocks already present: %s' % sorted(done))
    # ------------------------------------------------------------------ R_CURVE
    s = ts['RCURVE']
    L = ['', '<!-- b556 THE CASCADE, ACT TEN, 2026-09-28 -->', '', BH, '',
         '**The rows, re-read at pin.** The Kernel Correspondence at :349-360 has %d rows, %d naming a terminal. Each terminal`s file at the row`s pin '
         'was elaborated fresh with `#check` and `#print axioms` appended (relay `data/b556_probe_<id>.txt`; statements, profiles, tiers and reasons in '
         '`data/b556_tiers.txt`): SIDE-rcurve`s Criterion.lean at `d5f33b4` = v0.1.0; SIDE-kernel`s DerivativeEngine.lean at `27a3ae7` (branch '
         '`derivative-engine`, fed from the main checkout, its one import Mathlib`s); SIDE-lv-conservation at each row`s tag and, where the file '
         'differs, at v0.11.0 = `2f71068`. The tier is the weakest link, `(R149)`(2), with `(R165)`(3); a row with no terminal is T4.' % (
             len(s['rows']), sum(1 for r in s['rows'] if r['names'])), ''] + table(s) + ['']
    L += moved_lines(s)
    L += ['**The kernel whole (SIDE-rcurve v0.1.0).** %d declarations in `SIDERCurve/Criterion.lean`: %s. By `(R166)` COMPONENT 2(b): none is stated '
          'about ξ on the line or about a general holomorphic function; each is real or complex arithmetic over abstract V, α, β, or a stipulated '
          'definition, and that its objects are the R-curve`s is carried by the identifiers -- split %s.' % (
              len(rc['decls']), ', '.join('`%s` %s' % (short(d['name']), d['tier']) for d in rc['decls']),
              ' · '.join('%s %d' % (x, rc['split'][x]) for x in ORDER if rc['split'][x])), '',
          '**`bd2ae1a`.** This document cites `bd2ae1a` nowhere (%d hits); no row gains the E-2026-09-27-1 line.' % len(bd['hits']['RCURVE']), '',
          '*Appended by b556. No claim of the document is altered; `h2` stays where the deposit left it.*', '']
    out['RCURVE'] = dict(present_before=True) if 'RCURVE' in done else append_to(dp('RCURVE'), NL.join(L))
    # ------------------------------------------------------------------ INDEX_ARITY
    s = ts['INDEX']
    prem = [t for t in s['terms'] if t['name'].endswith('certifiedInput_not_zeroRealizing')][0]
    tagl = []
    for r in s['rows']:
        if any(x in r['kernel'] for x in ('5a14205', '2f71068')):
            tt = [t for t in s['terms'] if t['row'] == r['line']]
            pres = all((t['tag'] or {}).get('found', t['pin'] == 'v0.11.0' and t['found']) for t in tt)
            tagl.append('*Row :%d (pinned `%s`):* SIDE-lv-conservation `%s` is now tagged -- `v0.11.0` = `2f71068`; the row`s terminals at the tag: %s.' % (
                r['line'], '5a14205' if '5a14205' in r['kernel'] else '2f71068', '2f71068' if '2f71068' in r['kernel'] else 'main (5a14205 an ancestor)',
                'present, statements as at the pin' if pres else 'NOT ALL PRESENT'))
    L = ['', '<!-- b556 THE CASCADE, ACT TEN, 2026-09-28 -->', '', BH, '', overhyp_paragraph(ts), '',
         '**The rows, re-read at pin.** The Correspondence at :369-397 has %d rows, %d naming a terminal. Files elaborated fresh at the row`s pin '
         '(relay `data/b556_probe_<id>.txt`, `data/b556_tiers.txt`): SIDE-kernel at `v1.7` = `2957e7d` (fed from the checkout at HEAD `0256e9e`, the '
         'imports compared and printed); SIDE-lv-conservation at `93c27ec` (v0.10.0), `5a14205`, `14720d9` and `2f71068` (v0.11.0), each earlier pin '
         'compared with v0.11.0. Row :380 names no commit ("deposited line"): its two terminals are read on the release line, main = v0.11.0, and are '
         'absent at the deposit tag v0.10.0.' % (len(s['rows']), sum(1 for r in s['rows'] if r['names'])), ''] + table(s) + ['']
    L += moved_lines(s) + [''] + tagl + ['',
          '**The premise of `certifiedInput_not_zeroRealizing`.** `NontrivialZeroExistsInStrip` -- `∃ σ, is_xi_zero σ ∧ 0 < σ ∧ σ < 1` -- a classical '
          'theorem (Riemann`s computed zeros; Hardy 1914) not compiled: its kind is literature, so the terminal is %s.' % prem['tier'], '',
          '**`bd2ae1a`.** Cited nowhere in this document (%d hits).' % len(bd['hits']['INDEX']), '',
          '*Appended by b556. No claim of the document is altered; `h2` stays where the deposit left it.*', '']
    out['INDEX'] = dict(present_before=True) if 'INDEX' in done else append_to(dp('INDEX'), NL.join(L))
    # ------------------------------------------------------------------ ADDITIVE_MULTIPLICATIVE
    s = ts['AMC']
    pr = probes()
    na = M1 + 'no_type_d_conspiracies'
    pa, pc = fresh_profile('e1', na, pr), fresh_profile('e2', na, pr)
    wrong = []
    if pc and 'sorryAx' in pc:
        wrong.append(446)
    if not (pa and 'sorryAx' not in pa and pa == STD3):
        wrong.append(408)
    corr = []
    if wrong == [446]:
        corr = ['*Correction to the table at :444 (2026-08-12), row :446, under `(R166)`(3):* at `c66f3c5` `Module1.no_type_d_conspiracies` prints '
                '`%s` -- it carries `sorryAx` (through `to_modular_correct`, as this document`s own correction of 2026-07-13 at :417 says), and Module1.lean '
                'there imports Mathlib (`%s`), so "`0 sorry, 0 axioms` (vanilla Lean 4, no Mathlib)" is wrong at that pin; the clean profile, `%s`, is '
                'at `a27415d`, as the table at :406 has it (row :408). The table at :406 is the right one.' % (
                    pc, '`, `'.join(rc['pins']['c66f3c5']['module1_imports']), pa)]
    cites = rc['citations']
    L = ['', '<!-- b556 THE CASCADE, ACT TEN, 2026-09-28 -->', '', BH, '',
         '**The rows, re-read at pin.** The original Correspondence (:406-415) has 8 rows and the table at the standard (:444-451) has 6; %d rows in all, '
         '%d naming a terminal. Files elaborated fresh (relay `data/b556_probe_<id>.txt`, `data/b556_tiers.txt`): SIDE-effects`s Module1.lean at '
         '`a27415d` and at `c66f3c5`; Structural.lean at `c66f3c5` (no import); Milestones.lean at `c66f3c5` with that pin`s Structural.lean put ahead '
         'of it, and at `a27415d`; SIDE-kernel`s MetaKernel.lean and SilenceTheorem.lean at `v1.2`, compared with `v1.7`.' % (
             len(s['rows']), sum(1 for r in s['rows'] if r['names'])), ''] + table(s) + ['']
    L += moved_lines(s) + [''] + corr + ['',
          '**`no_type_d_conspiracies` at both pins.** `a27415d`: `%s`; `c66f3c5`: `%s`. `a27415d` is on %s; `c66f3c5` on %s. No tag of SIDE-effects '
          'contains either.' % (pa, pc, ', '.join('`%s`' % b for b in rc['pins']['a27415d']['branches']), ', '.join('`%s`' % b for b in rc['pins']['c66f3c5']['branches'])), '',
          '**Milestones.lean.** `twin_primes_infinite`, `goldbach`, `sophie_germain_infinite`, each proved by `sorry` at both pins (profiles in the '
          'bank); their statements are the conjectures themselves, T4.', '',
          '**The two SIDE-effects terminals, by the ferry`s criterion.** `no_type_d_conspiracies` and `crt_exhaustiveness` range over the programme`s '
          '`StructuralCoupling` and `ModularCoupling`, so T2; b555 banked both T0 -- the difference is flagged for the author, not settled here.', '',
          '**The name citations.** ' + '; '.join('%s %s: %s' % (k, v['cited'], v['resolved']) for k, v in cites.items()) + '.', '',
          '*Appended by b556. No claim of the document is altered; `h2` stays where the deposit left it.*', '']
    out['AMC'] = dict(present_before=True) if 'AMC' in done else append_to(dp('AMC'), NL.join(L))
    for k in DOCS:
        out[k]['line'] = line_of(dp(k), BH)
    out['wrong'] = wrong
    put_json('b556_blocks.json', out)
    for k in DOCS:
        print(k, out[k])


# ------------------------------------------------------------------------------ READING (11): THE STEMS
def stems():
    import banned_terms as BTM
    res, L = {}, ['b556 -- READING (11): THE BANNED-STEM COUNT OVER THE BATCH DOCUMENTS (before this act`s appends); no edit', '']
    for k in DOCS:
        src = blob(PP, PRIOR_PP + ':' + DOCS[k]).split(NL)
        hits = []
        for i, l in enumerate(src, 1):
            for m in BTM.PAT.finditer(l):
                hits.append(dict(line=i, stem=[x for x in BTM.STEMS if m.group(0).lower().startswith(x)][0], word=m.group(0),
                                 cls=BTM.classify(l, m.start(), dp(k)) or 'LIVE USE', text=l[max(0, m.start() - 60):m.end() + 60]))
        per = {x: sum(1 for h in hits if h['stem'] == x) for x in BTM.STEMS}
        live = {x: sum(1 for h in hits if h['stem'] == x and h['cls'] == 'LIVE USE') for x in BTM.STEMS}
        res[k] = dict(per=per, live=live, hits=hits)
        L += ['### %s: per stem %s ; live uses %s' % (TITLE[k], per, live)] + ['    :%-4d %-6s %-12s %-40s ...%s...' % (
            h['line'], h['stem'], h['word'], h['cls'][:40], h['text']) for h in hits] + ['']
    put_json('b556_stems.json', res)
    put_txt('b556_stems.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ READING (12): THE ENTRY
FH = ('## The cascade, act ten: R_CURVE_CRITERION, INDEX_ARITY and ADDITIVE_MULTIPLICATIVE_CONSPIRACY tiered; the critical path entered')
HEADING = ('### b556 — the cascade, act ten under (R166): R_CURVE_CRITERION, INDEX_ARITY_AT_THE_CRITICAL_LINE and ADDITIVE_MULTIPLICATIVE_CONSPIRACY '
           'tiered; the critical path entered on the trails')


def findings():
    guard_absent(FIND, FH)
    ts, bl, pa, st, rc = jl('b556_tiers.json'), jl('b556_blocks.json'), jl('b556_path.json'), jl('b556_stems.json'), jl('b556_rcurve.json')
    L = ['', FH, '', '*Filed at b556 on the author`s ruling `(R166)`. The cascade`s act ten, CP-1`s batch one. Banks: relay `data/b556_tiers.txt`, '
         '`data/b556_rcurve.txt`, `data/b556_stems.txt`, `data/b556_probes.jsonl`.*', '']
    for k in DOCS:
        s = ts[k]
        L += ['**%s** (tier block at `%s`:%d): %d rows; tiers over %d terminal readings %s; rows by weakest link %s; CARRIED %d · MOVED %d%s; banned '
              'stems %s (live %s).' % (TITLE[k], DOCS[k], bl[k]['line'], len(s['rows']), len(s['terms']), ' · '.join('%s %d' % (x, s['term_tiers'][x]) for x in ORDER),
                                       ' · '.join('%s %d' % (x, s['row_tiers'][x]) for x in ORDER), s['disp']['CARRIED'], s['disp']['MOVED'],
                                       (' (' + ', '.join(':%d' % r['line'] for r in s['rows'] if r['disp'] == 'MOVED') + ')') if s['disp']['MOVED'] else '',
                                       sum(st[k]['per'].values()), sum(st[k]['live'].values())), '']
    L += ['**SIDE-rcurve v0.1.0 whole:** %s -- no declaration about ξ on the line or a general holomorphic function.' % (
              ' · '.join('%s %d' % (x, rc['split'][x]) for x in ORDER if rc['split'][x])), '',
          '**The critical path** is entered at `OPEN_TRAILS.md`:%d, its pointer at `FINDINGS.md`:%d; no work-order started.' % (pa['trail']['line'], pa['pointer']['line']), '',
          '**Next:** b557, the eight method keystones (FOUNDATIONS_OF_THE_SIDE_PROGRAMME, INVARIANCE_BARRIERS, SILENCE_STAGES_DEALIGNMENT, TECHNE_TOOLKIT, '
          'E_DIFFICULTY_THEOREM, REPARAMETERIZATION_BARRIERS_v0_1, ENUMERA, EXHAUSTIVENESS_LICENSE).', '',
          '*Nothing deposits; nothing at Zenodo written; no `.lean` file edited; nothing here is a statement about RH or any zero.*', '']
    o = append_to(FIND, NL.join(L))
    o['line'] = line_of(FIND, FH)
    put_json('b556_findings.json', o)
    print(NL.join(rd(FIND).split(NL)[o['line'] - 1:]))


# ------------------------------------------------------------------------------ THE SCORES, THE DESK, THE RECORD
WRITE_OK = {'FINDINGS.md', 'OPEN_TRAILS.md', RCR, IXR, AMR}
MEMDIR = P.MEMDIR
PRE_HEADS = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-explicit-formula': '81ae175', 'SIDE-global-section': 'a91d941',
             'SIDE-effects': 'ef4cff7', 'SIDE-rcurve': 'd5f33b4', 'SIDE-meta': '6bb7b23', 'SIDE-silence-principle': '667c254', 'SIDE-compression': 'e9a5a36'}


def w_(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def mains():
    return {k: sorted(x for x in g(os.path.join(DD, k), 'diff', '--name-only', h, 'main').split(NL) if x.strip()) for k, h in PRE_HEADS.items()}


def scores():
    ts, rc, bl = jl('b556_tiers.json'), jl('b556_rcurve.json'), jl('b556_blocks.json')
    pr = probes()
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b556_') and needle in rd(os.path.join(T, x))]
    tk = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    tok = sum(open(os.path.join(d0, f), 'rb').read().count(tk) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b556_')) if tk else None
    m = mains()
    lean = [(k, f) for k, v in m.items() for f in v if f.endswith('.lean')]
    dep = g(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2').strip() == ''
    trial = dict(head=g(TRIAL, 'rev-parse', 'HEAD').strip(), status=g(TRIAL, 'status', '--porcelain', '--untracked-files=no').strip())
    moved = [(k, r['line']) for k in DOCS for r in ts.get(k, {}).get('rows', []) if r['disp'] == 'MOVED']
    na = M1 + 'no_type_d_conspiracies'
    pa, pc = fresh_profile('e1', na, pr), fresh_profile('e2', na, pr)
    terms = [t for k in DOCS for t in ts.get(k, {}).get('terms', [])]
    zero = sorted({(t['name'], t['zero']) for t in terms if t['zero'] in ('EXPLICIT', 'BY-DEFINITION', 'PER-ZERO')})
    anchor = [t['name'] for t in terms if short(t['name']) in ANCHOR]
    prem_uw = [t['name'] for t in terms if t['unused'] and t['tier'] in ('T1-lit', 'T1-open', 'T2-INTERFACES')]
    lvterms = [t for t in terms if t['name'].startswith(S) and t['tag']]
    return dict(
        n1=bool(ts) and moved == [('INDEX', 369)],
        n2=bool(pa) and bool(pc) and 'sorryAx' in pc and pa == STD3 and bl.get('wrong') == [446],
        n3=bool(rc) and all(d['tier'] == 'T2' for d in rc['decls'] if not d['xi_or_holomorphic']) and all(d['tier'] == 'T0' for d in rc['decls'] if d['xi_or_holomorphic']),
        n3_vacuous=bool(rc) and not any(d['xi_or_holomorphic'] for d in rc['decls']),
        n4=False,   # ### clause (i) fails on :365`s own words ("a check, not a reading"); clause (ii) printed beside
        n4_ii=not prem_uw, prem_uw=prem_uw,
        n5=not zero, zero=zero, anchor=anchor,
        n6=not lean and not zen and tok == 0 and dep and trial['head'].startswith('f22ff35') and trial['status'] == '',
        mains=m, zen=zen, token=tok, deposit_clean=dep, trial=trial, moved=moved, pa=pa, pc=pc,
        s1=('ConservationBridge.riemann_hypothesis', 'EXPLICIT') in zero,
        s2=bool(ts) and all(t['tier'] == 'T2' for t in terms if t['name'] in (na, M1 + 'crt_exhaustiveness')),
        s3=bool(lvterms) and all(t['tag']['same_statement'] for t in lvterms))


def desk():
    sc = scores()
    N, SS = ('n1', 'n2', 'n3', 'n4', 'n5', 'n6'), ('s1', 's2', 's3')
    L = ['=' * 104, 'b556 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S SIX.', '-' * 104,
         '  **(N1)** ### **%s.** -- rows MOVED: %s.' % (w_(sc['n1']), sc['moved']),
         '  **(N2)** ### **%s.** -- no_type_d_conspiracies at a27415d `%s` ; at c66f3c5 `%s`.' % (w_(sc['n2']), sc['pa'], sc['pc']),
         '  **(N3)** ### **%s.** -- every SIDE-rcurve theorem T2; the exception clause (ξ on the line, a general holomorphic function) %s.' % (
             w_(sc['n3']), 'VACUOUS: no declaration of that kind' if sc['n3_vacuous'] else 'non-empty'),
         '  **(N4)** ### **%s.** -- clause (i) fails: :365 states the grade`s test as "a check, not a reading: delete the hypothesis and recompile"; '
         'clause (ii) %s (unused warnings on a tier-setting premise: %s). The grade is a proof-side check; it adds no tier axis and can only correct '
         'a tier through an unused named premise.' % (w_(sc['n4']), 'holds' if sc['n4_ii'] else 'fails', sc['prem_uw'] or 'NONE'),
         '  **(N5)** ### **%s.** -- conclusions naming a zero of ζ: %s ; RH-anchor terminals among them: %s.' % (w_(sc['n5']), sc['zero'] or 'NONE', sc['anchor'] or 'NONE'),
         '  **(N6)** ### **%s.** -- mains changed %s ; token %s ; deposit clean %s ; trial %s.' % (
             w_(sc['n6']), {k: v for k, v in sc['mains'].items() if v} or 'NONE', sc['token'], sc['deposit_clean'], sc['trial']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- riemann_hypothesis`s conclusion EXPLICIT: %s.' % (w_(sc['s1']), sc['s1']),
         '  **(S2)** ### **%s.** -- the two SIDE-effects terminals T2 under the ferry`s criterion.' % w_(sc['s2']),
         '  **(S3)** ### **%s.** -- every lv terminal`s statement the same at v0.11.0 as at its row`s pin.' % w_(sc['s3']),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in N].count(None),
            [sc[k] for k in SS].count(True), [sc[k] for k in SS].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b556_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b556_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    put_txt('b556_desk_notes.txt', L)
    put_json('b556_scores.json', sc)
    print(NL.join(L))


def components():
    L = ['=' * 132, 'b556 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    for n in ('b556_tiers.txt', 'b556_rcurve.txt', 'b556_stems.txt'):
        if os.path.exists(os.path.join(D, n)):
            L += ['### relay data/%s' % n] + ['  ' + l for l in rd(os.path.join(D, n)).rstrip(NL).split(NL)] + ['']
    for n in ('b556_bd2.json', 'b556_path.json', 'b556_blocks.json', 'b556_findings.json'):
        L.append('### %s : %s' % (n, json.dumps(jl(n), ensure_ascii=False)[:3000]))
    L += ['### THE PROBES : relay data/b556_probe_<id>.txt and data/b556_probes.jsonl', '### THE BRANCHES : see data/b556_branches.txt', '=' * 132]
    put_txt('b556_components.txt', L)
    print(NL.join(L[:6]))


def trail():
    sc = scores()
    ts, bl, pa, fj = jl('b556_tiers.json'), jl('b556_blocks.json'), jl('b556_path.json'), jl('b556_findings.json')
    body = ['', HEADING, '',
            '**(R166) ratified.** (1) The principle: the cascade is the audit, the work-orders are the research, the editions wait for the work-orders. '
            '(2) The critical path in three lanes, entered. (3) Batch one tiered, the three readings applied. (4) b557 next.', '',
            '**Entered:** OPEN_TRAILS.md:%d (the critical path); FINDINGS.md:%d (its pointer) and :%d (the entry); %s.' % (
                pa['trail']['line'], pa['pointer']['line'], fj['line'], '; '.join('%s:%d (the tier block)' % (TITLE[k] + '.md', bl[k]['line']) for k in DOCS)), '']
    for k in DOCS:
        s = ts[k]
        body.append('**%s:** tiers %s; CARRIED %d · MOVED %d.' % (TITLE[k], ' · '.join('%s %d' % (x, s['term_tiers'][x]) for x in ORDER), s['disp']['CARRIED'], s['disp']['MOVED']))
    body += ['', '**CP-1:** open; batch two (b557) takes the eight method keystones, then CP-1b (b558).', '', '**Next:** b557.', '',
             '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
             % tuple(w_(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 's1', 's2', 's3')),
             '**No kernel lane opened at this act; the kernel reads were fresh elaborations at pin.** Nothing deposits; nothing at Zenodo written; '
             'no `.lean` file edited; no monograph byte changed; ERRATA untouched; the ceiling unchanged; row U1 unedited; no work-order started; `h2` '
             'where the deposit left it; the four lists stay OPEN; nothing here is a statement about RH or any zero.', '']
    text = poss(NL.join(body))
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE TRAIL')
    import banned_terms as BT
    if [m.group(0) for m in BT.PAT.finditer(text)]:
        sys.exit('### A BANNED STEM IN THE TRAIL')
    before = open(OT, 'rb').read()
    if poss(HEADING).encode('utf-8') in before:
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(text.encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(poss(HEADING)))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b556_trail_notes.json', out)


if __name__ == '__main__':
    fn = {k: globals()[k] for k in ('reads', 'path', 'rows', 'tiers', 'rcurve', 'blocks', 'stems', 'findings', 'components', 'desk', 'trail')}
    if len(sys.argv) < 2 or sys.argv[1] not in fn:
        sys.exit('usage: %s %s' % (sys.argv[0], ' | '.join(fn)))
    fn[sys.argv[1]]()
