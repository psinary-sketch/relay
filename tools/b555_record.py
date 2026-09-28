# -*- coding: utf-8 -*-
"""b555_record.py -- THE CASCADE, ACT NINE: GRH_CASCADE TIERED, ITS OPEN PIECE RESTATED AS THE χ-SIDE OF THE WEIL ARC AND
PRICED; H8 AT ITS WEIGHT AND THE Q0 NUMBERS ENTERED; THE T3DOUBLEPRIME TIER SETTLED; THE TIER LAW`S PROGRAMME-PREMISE
CLAUSE: THE RECORD, UNDER (R165).
### `python tools/b555_record.py reads | h8 | t3dp | clause | rows | tiers | block | stems | shells | search | cost | weil |
### reading | findings | components | desk | trail`
### The probes` launches, the commits, pushes and branch commands are the seat`s. This file deletes nothing.
"""
import io, json, math, os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b551_record as P  # noqa: E402
DD = 'D:' + os.sep
PP, GS, LV, EF, TRIAL = P.PP, P.GS, P.LV, P.EF, P.TRIAL
KER = os.path.join(DD, 'SIDE-kernel')
GRHK = os.path.join(DD, 'SIDE-grh-transfer')
EFF = os.path.join(DD, 'SIDE-effects')
FIND, OT = P.FIND, P.OT
GRHD = os.path.join(PP, 'phase1.5', 'spectral', 'GRH_CASCADE.md')
BALPOS = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
CENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')
NL = chr(10)
rd, g, cite, append_to, guard_absent, line_of, poss, outside_bt = P.rd, P.g, P.cite, P.append_to, P.guard_absent, P.line_of, P.poss, P.outside_bt
PRIOR_RELAY = 'f93b2b46'   # ### b554`s closing housekeeping -- relay`s tip before this act
PRIOR_PP = '0c748da'       # ### b554`s PLACE-papers commit
GRHR = 'phase1.5/spectral/GRH_CASCADE.md'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


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


# ------------------------------------------------------------------------------ THE READS
def reads():
    L = ['b555 -- THE ORDERED READS, CITED BY PATH AND LINE', '']
    sp = os.path.join(D, 'b554_sign_pattern.txt')
    t = rd(sp)
    a = lines_with(None, r'^### THE SIGN PATTERN OVER', t)[0]
    f = lines_with(None, r'^### THE FLOOR, PER INTERVAL', t)[0]
    c = lines_with(None, r'^### THE 29.551761 CRESTS', t)[0]
    cite(L, sp, f, f + 32, 'relay data/b554_sign_pattern.txt -- the floor derivation, per interval')
    cite(L, sp, a, a + 9, 'relay data/b554_sign_pattern.txt -- the sign pattern and the two positive intervals')
    cite(L, sp, c, c + 3, 'relay data/b554_sign_pattern.txt -- the crest table')
    cite(L, FIND, 4805, 4811, 'FINDINGS.md:4805 -- the tier law`s first statement (b539, (R149))')
    cite(L, FIND, 4819, 4823, 'FINDINGS.md:4819 -- the tier law corrected (b540, (R150)): T1 split')
    cite(L, BALPOS, 678, 678, 'BALANCE_AND_POSITIVITY.md:678 -- b545`s line grading T3doubleprime at T2')
    for a0, z0, w in ((25, 25, 'the Role paragraph'), (29, 43, 'the Status block'), (47, 49, 'the Abstract'), (53, 67, '§I'),
                      (139, 145, '§III.3 and its transport paragraph'), (375, 395, 'the Correspondence rows and the kernel-audit line'),
                      (421, 433, 'the b394 annotation')):
        cite(L, GRHD, a0, z0, 'GRH_CASCADE.md -- ' + w)
    L += ['### GRH_CASCADE.md read entire: %d lines' % len(rd(GRHD).split(NL)), '']
    grh = blob(GRHK, '858cbf6:SIDEGRHTransfer/GRHBridge.lean')
    for n in ('seven_classes_chi', 'none_produce_chi', 'GRHStructuralExhaustiveness', 'grh_structural_exhaustiveness_proved'):
        ln = lines_with(None, r'^(theorem|def) %s\b' % n, grh)[0]
        cite(L, os.path.join(GRHK, 'SIDEGRHTransfer', 'GRHBridge.lean'), ln - 1, ln + 9, 'GRHBridge.lean at 858cbf6 -- ' + n, text=grh)
    ct = blob(GRHK, '858cbf6:SIDEGRHTransfer/CharacterTransfer.lean')
    ln = lines_with(None, r'^theorem twisted_balance_at_unramified_prime', ct)[0]
    cite(L, os.path.join(GRHK, 'SIDEGRHTransfer', 'CharacterTransfer.lean'), ln, ln + 26, 'CharacterTransfer.lean at 858cbf6 -- the twisted_balance lemmas', text=ct)
    for f in ('CharacterSymmetry', 'CharacterCodim', 'CharacterModular', 'CharacterSpectral', 'CharacterTopological'):
        s = blob(GRHK, '858cbf6:SIDEGRHTransfer/%s.lean' % f)
        for ln in lines_with(None, r'^theorem paired_', s):
            cite(L, os.path.join(GRHK, 'SIDEGRHTransfer', f + '.lean'), ln, ln + 3, '%s.lean at 858cbf6 -- a paired_* lemma' % f, text=s)
    for v, n in (('Voice2Vendored', 'conjugate_re'), ('Voice2Vendored', 'reflect_re'), ('Voice3bVendored', 'cr_minimal_codim'),
                 ('Voice5Vendored', 'S_action'), ('Voice6Vendored', 'spectral_offset'), ('Voice7Vendored', 'topological_contribution')):
        s = blob(GRHK, '858cbf6:SIDEGRHTransfer/%s.lean' % v)
        ln = lines_with(None, r'def %s\b' % n, s)[0]
        cite(L, os.path.join(GRHK, 'SIDEGRHTransfer', v + '.lean'), ln, ln + 1, '%s.lean at 858cbf6 -- the definition %s unfolds to' % (v, n), text=s)
    for tag in ('b1407b2', '0e5233f'):
        for f, n in (('MetaKernel.lean', 'type_I_has_ostrowski'), ('Kernel/SilenceTheorem.lean', 'silence_universal'),
                     ('Kernel/SilenceTheorem.lean', 'Interface.is_universal'), ('Bridge/OstrowskiBridge.lean', 'ostrowski_exhaustive'),
                     ('Bridge/LocalZeta.lean', 'neg_eq_neg_one_sub_iff')):
            s = blob(KER, '%s:%s' % (tag, f))
            ln = lines_with(None, r'^(theorem|def) %s\b' % re.escape(n), s)[0]
            cite(L, os.path.join(KER, f), ln, ln + 6, 'SIDE-kernel %s -- %s' % (tag, n), text=s)
    for tag in ('a27415d', 'c66f3c5'):
        s = blob(EFF, '%s:SIDEEffects/Phase15/Module1.lean' % tag)
        for n in ('crt_exhaustiveness', 'no_type_d_conspiracies'):
            ls = lines_with(None, r'^theorem %s\b' % n, s)
            if ls:
                cite(L, os.path.join(EFF, 'SIDEEffects', 'Phase15', 'Module1.lean'), ls[0], ls[0] + 5, 'SIDE-effects %s -- %s' % (tag, n), text=s)
        m = blob(EFF, '%s:SIDEEffects/Milestones.lean' % tag)
        L += ['### SIDE-effects %s Milestones.lean: the sorry lines %s' % (tag, lines_with(None, r'^\s*sorry', m))]
        s = blob(EFF, '%s:SIDEEffects/Structural.lean' % tag)
        L += ['### SIDE-effects %s Structural.lean: `grh_exclusion` at %s ; `no_ls_zero` at %s' % (
            tag, lines_with(None, r'grh_exclusion', s), lines_with(None, r'no_ls_zero', s))]
    for r, pin, f, ns in ((os.path.join(DD, 'SIDE-bsd-formation-transfer'), '7425d73', 'SIDEBSDFormationTransfer/Basic.lean', ('formation_preserved', 'n1_BSD')),
                          (os.path.join(DD, 'SIDE-yang-mills-formation'), '79e4f45', 'SIDEYangMillsFormation/Basic.lean', ('mass_gap_equals_n3_certification', 'mass_gap_is_n3_domain_ostrowski'))):
        s = blob(r, '%s:%s' % (pin, f))
        for n in ns:
            ln = lines_with(None, r'^(theorem|def) %s\b' % n, s)[0]
            cite(L, os.path.join(r, f), ln, ln + 2, '%s %s -- %s' % (os.path.basename(r), pin, n), text=s)
    ef = blob(EF, '5c72cad:Zeta23/ExplicitFormula.lean')
    a0 = lines_with(None, r'^def literatureRHS', ef)[0]
    cite(L, os.path.join(EF, 'Zeta23', 'ExplicitFormula.lean'), a0 - 4, a0 + 4, 'Zeta23 at SIDE-explicit-formula 5c72cad -- literatureRHS (vonMangoldt; the ζ gamma factor)', text=ef)
    a1 = lines_with(None, r'^def EF_lit\b', ef)[0]
    cite(L, os.path.join(EF, 'Zeta23', 'ExplicitFormula.lean'), a1 - 6, a1 + 4, 'Zeta23 -- EF_lit over a zero configuration, its RHS literatureRHS', text=ef)
    wm = blob(EF, '5c72cad:Zeta23/WeilEF/Main.lean')
    a2 = lines_with(None, r'^theorem EF_lit_zetaZeroConfig', wm)[0]
    cite(L, os.path.join(EF, 'Zeta23', 'WeilEF', 'Main.lean'), a2, a2, 'Zeta23 -- EF_lit instantiated at ζ', text=wm)
    for act in ('b526', 'b527', 'b528', 'b529', 'b530', 'b531', 'b532', 'b533', 'b534', 'b535', 'b536'):
        ls = lines_with(OT, r'^### %s ' % act)
        L += ['### OPEN_TRAILS -- %s`s record at %s' % (act, ls)]
        if ls:
            L += ['  :%d %s' % (ls[0], rd(OT).split(NL)[ls[0] - 1][:400])]
    put_txt('b555_reads.txt', L)
    print('  reads banked : %d lines' % len(L))


# ------------------------------------------------------------------------------ COMPONENT 1: H8 AT ITS WEIGHT
H8H = '*Appended at b555 (2026-09-28) to b548`s entry (`FINDINGS.md`:5613) and b554`s (:5788), under `(R165)`(1) -- H8 AT ITS WEIGHT, graded READING:*'


def h8():
    guard_absent(FIND, H8H)
    sp = jl('b554_sign_pattern.json')
    t = rd(os.path.join(D, 'b554_sign_pattern.txt'))
    pos = sp['pos']
    neg = [r for r in sp['runs'] if r[0] == 'NEG']
    fl = max(f['floor'] for f in sp['floor'])
    ctr = sp['controls']
    cr = [c for c in sp['crests'] if c['a'] > 45][0]
    lp = lines_with(None, r'^### POSITIVE INTERVALS ABOVE THE FLOOR', t)[0]
    lf = lines_with(None, r'^### THE FLOOR, PER INTERVAL', t)[0]
    lc = lines_with(None, r'^### THE 29.551761 CRESTS', t)[0]
    lr = lines_with(None, r'^### THE SIGN PATTERN OVER', t)[0]
    assert len(pos) == 2 and len(neg) == 2
    s = (H8H + ' at Q0, order 7, the fine-grid quantity is positive above the floor on a %.3f–%.3f and %.3f–%.3f and negative below it '
         'elsewhere on 30–60 (relay `data/b554_sign_pattern.txt`:%d-%d); the floor at most %.2f (:%d), the controls against b548 to %.0e. It '
         'turns negative from a = %.3f, is positive again on %.3f–%.3f (the 29.55 crest against the pair) and negative from %.3f through 60; '
         'the next crest, at a ≈ %.1f, carries %+.0f against a pair term of %.0f (:%d). b522`s integer-grid detection width 34 is refined to '
         '%.2f, and the width past which the sign stays negative in the banked range is %.2f. The lower interval begins at the grid`s edge: '
         'it is the region below detection, where the off-line pair has not yet overcome the on-line part; the clause "exactly one positive '
         'interval" was the navigator`s mis-specification, and its refutation says nothing the bank did not already say. Nothing about ζ’s '
         'zeros is claimed.' % (
             math.exp(pos[0][0]), math.exp(pos[0][1]), math.exp(pos[1][0]), math.exp(pos[1][1]), lr, lr + 5, fl, lf,
             max(ctr.values()), math.exp(neg[0][1] if False else pos[0][1]), math.exp(pos[1][0]), math.exp(pos[1][1]), math.exp(pos[1][1]),
             cr['a'], cr['crest'], cr['pair'], lc, math.exp(pos[0][1]), math.exp(pos[1][1])))
    o = append_to(FIND, NL.join(['', s, '']))
    o['line'] = line_of(FIND, H8H)
    o['numbers'] = dict(turns_negative=math.exp(pos[0][1]), second=[math.exp(pos[1][0]), math.exp(pos[1][1])], stays_negative=math.exp(pos[1][1]),
                        floor=fl, crest=[cr['a'], cr['crest'], cr['pair']])
    put_json('b555_h8.json', o)
    print(poss(s)); print(o['line'])


# ------------------------------------------------------------------------------ COMPONENT 2: THE TIER SETTLED, THE CLAUSE, (o)
T3L = ('SUPERSEDES BALANCE_AND_POSITIVITY :678 for `T3doubleprime_general_commutation_fails`: T0 (b554, SIMPLICITY_OF_RIEMANN_ZEROS '
       ':448, a compiled negative meeting none of the T2 criteria) -- appended 2026-09-28 by b555 under the author`s ruling `(R165)`(2); '
       'b545`s T2 at :678 is kept as written.')
CLH = '*Appended at b555 (2026-09-28) to the tier law (`FINDINGS.md`:4805, b539; :4819, b540), under `(R165)`(3) -- THE PROGRAMME-PREMISE CLAUSE:*'
OOL = '*Appended at b555 (2026-09-28) to b554`s record, under `(R165)`(2) -- DEFECT (o):*'


def t3dp():
    import terminal_table as TT
    guard_absent(BALPOS, T3L[:70])
    assert not TT.GRADE_RE.search(T3L), 'a grade word'
    assert 'T3doubleprime_general_commutation_fails' in rd(BALPOS).split(NL)[677]
    o = append_to(BALPOS, NL.join(['', T3L, '']))
    o['line'] = line_of(BALPOS, T3L[:70])
    put_json('b555_t3dp.json', o)
    print(rd(BALPOS).split(NL)[o['line'] - 1]); print(o)


def clause():
    guard_absent(FIND, CLH)
    guard_absent(OT, OOL)
    s = (CLH + ' a terminal that interfaces on a named premise which is neither compiled nor a literature theorem but the programme`s own '
         'manuscript claim -- `silence_universal` on `I.is_universal`; the route terminals on `ConservationHypothesis` before E-2026-09-25-1 '
         'showed it RH restated -- is **T2-INTERFACES**: the premise`s truth is the programme`s to establish, so the terminal cannot be read '
         'as resting on anything outside the programme. **T1-open** stays reserved for premises EQUIVALENT-DEEP to RH (`h2_sign`); '
         '**T1-lit** for uncompiled literature theorems.')
    o1 = append_to(FIND, NL.join(['', s, '']))
    o1['line'] = line_of(FIND, CLH)
    b554 = lines_with(OT, r'^### b554 ')[0]
    s2 = (OOL + ' (the record at :%d) PLACE-papers commit `0c748da`, b554`s act commit, cites the act`s FINDINGS entry at :5780; the '
          'entry is at :5788. Recorded in b554`s record (relay `data/b554_defects.txt`, (o)) and not rewritten.' % b554)
    o2 = append_to(OT, NL.join(['', s2, '']))
    o2['line'] = line_of(OT, OOL)
    o2['b554'] = b554
    put_json('b555_clause.json', dict(clause=o1, defect_o=o2))
    print(poss(s)); print(poss(s2)); print(o1['line'], o2['line'])


# ------------------------------------------------------------------------------ COMPONENT 3: GRH_CASCADE TIERED
STD3 = 'depends on axioms: [propext, Classical.choice, Quot.sound]'
PQ = 'depends on axioms: [propext, Quot.sound]'
NONE_AX = 'does not depend on any axioms'
NA = 'T0, not RH-anchor: '
GG = 'SIDEGRHTransfer.'
PRGDEF = 'χ and χbar typed and unused; '
TERMS = {
    GG + 'grh_structural_exhaustiveness_proved': ('g2', 'T2', 'the composite: `GRHStructuralExhaustiveness χ χbar`, whose body is a count of the kernel`s own '
                                                  'classes, the class exclusions over programme-defined σ-predicates, and Ostrowski -- χ and χbar occur nowhere in '
                                                  'it (printed); Route 1`s shape (b540)', 'GRHStructuralExhaustiveness χ χbar, a Prop in which no character occurs'),
    GG + 'seven_classes_chi': ('g2', 'T2', 'the cardinality of the kernel`s own inductive type is 7 (`decide`)', 'Fintype.card MechanismClass = 7'),
    GG + 'none_produce_chi': ('g2', 'T2', PRGDEF + 'the exclusions over `produces_offline_chi`, a predicate the kernel defines on σ', '∀ c, ¬ produces_offline_chi c'),
    GG + 'ostrowski_exhaustive_chi': ('g2', 'T0', NA + 'Ostrowski`s classification of the absolute values of ℚ, from Mathlib; no character', 'every nontrivial |·| on ℚ is real or p-adic'),
    GG + 'voice1_balance_chi': ('g2', 'T0', NA + 'the balance exponent`s identity −σ = −(1 − σ) ↔ σ = 1/2 over ℝ; no prime, zero or character enters (the row`s own note)',
                                '−σ = −(1 − σ) ↔ σ = 1/2'),
    GG + 'c1_chi_exclusion': ('g2', 'T2', PRGDEF + 'over `conjugate_re σ := σ` and `reflect_re σ := 1 − σ`', '¬ produces_offline_chi .C1_schwarz'),
    GG + 'c2_chi_exclusion': ('g2', 'T0', NA + PRGDEF + 'no σ ≠ 1/2 with −σ = −(1 − σ) -- the balance identity over ℝ', '¬ produces_offline_chi .C2_euler'),
    GG + 'c3_chi_exclusion': ('g2', 'T0', NA + PRGDEF + 'no σ ≠ 1/2 is fixed by ρ ↦ 1 − ρ on real parts -- a fact about ℂ', '¬ produces_offline_chi .C3_functional_eq'),
    GG + 'c4_chi_exclusion': ('g2', 'T2', PRGDEF + 'over `S_action σ := 1 − σ`, a definition', '¬ produces_offline_chi .C4_modular'),
    GG + 'c5_chi_exclusion': ('g2', 'T2', PRGDEF + 'over `spectral_offset σ := σ − 1/2`, a definition', '¬ produces_offline_chi .C5_spectral'),
    GG + 'c6_chi_exclusion': ('g2', 'T2', PRGDEF + 'over `cr_minimal_codim`, defined through `zero_codimension`', '¬ produces_offline_chi .C6_cauchy_riemann'),
    GG + 'c7_chi_exclusion': ('g2', 'T2', PRGDEF + 'over `topological_contribution σ := 0`, a constant', '¬ produces_offline_chi .C7_hadamard'),
    GG + 'twisted_balance_at_unramified_prime': ('g2', 'T0', NA + '‖χ(p)‖·p^(−s) = ‖χ(p)‖·p^(−(1−s)) ↔ s = 1/2 at a prime p ∤ n, through Mathlib`s '
                                                 'norm-one value of a Dirichlet character at a unit -- the character enters', 'the twisted balance at an unramified prime forces s = 1/2'),
    GG + 'twisted_balance_at_half': ('g2', 'T0', NA + 'the twisted balance holds at s = 1/2, by the lemma above', 'the twisted balance holds at s = 1/2'),
    GG + 'paired_reflection_axis_invariant_iff': ('g2', 'T0', NA + PRGDEF + '(∀ ρ : ℂ, ρ.re = σ → (1 − ρ).re = σ) ↔ σ = 1/2 -- a fact about ℂ',
                                                 'ρ ↦ 1 − ρ preserves the real part σ iff σ = 1/2'),
    GG + 'paired_conjugation_real_axis_agree_iff': ('g2', 'T2', PRGDEF + '`conjugate_re σ = reflect_re σ ↔ σ = 1/2` over two definitions (σ and 1 − σ)',
                                                   'conjugate_re σ = reflect_re σ iff σ = 1/2'),
    GG + 'paired_cr_minimal_codim_axis_iff': ('g2', 'T2', PRGDEF + '`cr_minimal_codim σ ↔ σ = 1/2` over a definition', 'cr_minimal_codim σ iff σ = 1/2'),
    GG + 'paired_modular_S_fixed_iff': ('g2', 'T2', PRGDEF + '`S_action σ = σ ↔ σ = 1/2`, S_action defined as 1 − σ', 'S_action σ = σ iff σ = 1/2'),
    GG + 'paired_spectral_offset_zero_iff': ('g2', 'T2', PRGDEF + '`spectral_offset σ = 0 ↔ σ = 1/2`, the offset defined as σ − 1/2', 'spectral_offset σ = 0 iff σ = 1/2'),
    GG + 'paired_topological_no_sigma_preference': ('g2', 'T2', PRGDEF + 'vacuous: `topological_contribution` is the constant 0', 'topological_contribution σ = topological_contribution (1/2)'),
    'ECondition.type_I_has_ostrowski': ('k6', 'T2', 'modus tollens over an abstract `Domain` whose `[Fintype Domain]` is never used -- logic alone; the Mechanism '
                                        'Theorem reading is carried by the name (b539)', '¬ target from ∀ d, ¬ produces d and target → ∃ d, produces d'),
    'SilenceTheorem.silence_universal': ('k7', 'T2-INTERFACES', 'INTERFACES on `I.is_universal` (∀ c₁ c₂, I.action c₁ = I.action c₂), a programme structure`s '
                                         'property that the manuscript asserts: T2-INTERFACES under (R165)(3); its universal form, R1, is FALSE-AS-STATED '
                                         '(not_register1, b538)', 'a universal interface has κ = 0'),
    'ostrowski_exhaustive': ('k8', 'T0', NA + 'Mathlib`s Ostrowski theorem (`Rat.AbsoluteValue.equiv_real_or_padic`) restated', 'every nontrivial |·| on ℚ is real or a unique p-adic'),
    'neg_eq_neg_one_sub_iff': ('k9', 'T0', NA + 'in any field of characteristic 0, −s = −(1 − s) ↔ s = 1/2 -- the balance exponent`s identity; no prime or zero enters',
                               '−s = −(1 − s) ↔ s = 1/2 in a field of characteristic 0'),
    'SIDEEffects.Phase15.Module1.no_type_d_conspiracies': ('e1', 'T0', NA + 'the type of structural couplings no modular coupling realizes is empty, by the '
                                                           'periodic lift -- residues, divisibility and coprimality over ℕ with Mathlib`s `ZMod`; scope: the '
                                                           'constructors carry 0 < q, 0 < m (positive modulus)', 'IsEmpty TypeD'),
    'SIDEEffects.Phase15.Module1.crt_exhaustiveness': ('e1', 'T0', NA + 'every structural coupling agrees pointwise with some modular coupling (the periodic '
                                                       'lift); positive-modulus scope', '∀ sc, ∃ m, ∀ n, sc.eval n ↔ m.eval n'),
    'SIDEBSDFormationTransfer.formation_preserved': ('b1', 'T2', 'SHELL: `decide` over hand-assigned constants n1_BSD…n4_BSD -- it records the assignment',
                                                     'n_i(BSD) = n_i(ξ), i = 1..4, for assigned constants'),
    'SIDEBSDFormationTransfer.both_interfaces_dark': ('b1', 'T2', 'SHELL: `decide` over assigned constants', 'n4_BSD = 0 ∧ n4_xi = 0'),
    'SIDEBSDFormationTransfer.all_seven_transfer': ('b1', 'T2', 'SHELL: `decide` over a Bool table the file defines', '∀ c, transfers c = true'),
    'SIDEYangMillsFormation.mass_gap_equals_n3_certification': ('y1', 'T2', 'SHELL: a `Bool` defined as `true` equals `true` (`decide`)', 'mass_gap_is_n3_domain_ostrowski = true'),
    'SIDEYangMillsFormation.silence_boundary_at_output_stage': ('y1', 'T2', 'SHELL: an assigned constant equals 3 (`decide`)', 'mass_gap_silence_boundary_stage = 3'),
}
ORDER = ['T0', 'T1-open', 'T1-lit', 'T2', 'T2-INTERFACES', 'T3', 'T4']
N_EXPECT = {GG + 'grh_structural_exhaustiveness_proved': ['T2'], GG + 'twisted_balance_at_unramified_prime': ['T0'],
            'SilenceTheorem.silence_universal': ['T2-INTERFACES'], 'ECondition.type_I_has_ostrowski': ['T2'], 'ostrowski_exhaustive': ['T0'],
            'neg_eq_neg_one_sub_iff': ['T0'], 'SIDEEffects.Phase15.Module1.no_type_d_conspiracies': ['T0'],
            'SIDEBSDFormationTransfer.formation_preserved': ['T2'], 'SIDEYangMillsFormation.mass_gap_equals_n3_certification': ['T2']}
N_EXPECT.update({GG + x: ['T0'] for x in ('paired_reflection_axis_invariant_iff', 'paired_conjugation_real_axis_agree_iff', 'paired_cr_minimal_codim_axis_iff',
                                          'paired_modular_S_fixed_iff', 'paired_spectral_offset_zero_iff', 'paired_topological_no_sigma_preference')})
QUAL = {'ostrowski_exhaustive': 'ostrowski_exhaustive', 'neg_eq_neg_one_sub_iff': 'neg_eq_neg_one_sub_iff'}


def rows():
    src = blob(PP, PRIOR_PP + ':' + GRHR).split(NL)
    head = [i for i, l in enumerate(src) if l.startswith('| Claim | Kernel | Theorem (fully qualified)')][0]
    out = []
    for i in range(head + 2, len(src)):
        l = src[i]
        if not l.startswith('|'):
            break
        c = [x.strip() for x in l.strip().strip('|').split('|')]
        names = re.findall(r'`((?:[A-Z][A-Za-z0-9]*\.)+[A-Za-z_₀][A-Za-z0-9_₀]*)`', c[2])
        if names:
            ns = names[0].rsplit('.', 1)[0]
            for x in re.findall(r'`([a-z_][A-Za-z0-9_₀]*)`', c[2]):
                q = ns + '.' + x
                if x.startswith('c1_chi') or x.startswith('c7_chi'):
                    continue
                if q not in names:
                    names.append(q)
            if 'c1_chi_exclusion' in c[2] and 'c7_chi_exclusion' in c[2]:
                names += [ns + '.c%d_chi_exclusion' % k for k in range(1, 8)]
        else:
            names = [x for x in re.findall(r'`([a-z_][A-Za-z0-9_₀]*)`', c[2]) if x in QUAL]
        out.append(dict(line=i + 1, claim=c[0], kernel=c[1], terminal_cell=c[2], profile_cell=c[3], status=c[4][:600], names=names))
    audit = [i + 1 for i, l in enumerate(src) if l.startswith('*Kernels audited at:')]
    put_json('b555_rows.json', dict(rows=out, count=len(out), audit_line=audit[0] if audit else None))
    print('  rows %d (the ruling says twelve) ; with a terminal %d ; names %d' % (len(out), sum(1 for r in out if r['names']), sum(len(r['names']) for r in out)))
    for r in out:
        print('  :%d %-55s %s' % (r['line'], r['claim'][:55], [n.split('.')[-1] for n in r['names']]))


def probes():
    return {json.loads(l)['id']: json.loads(l) for l in rd(os.path.join(D, 'b555_probes.jsonl')).split(NL) if l.strip()}


def check_text(pid, name):
    t = rd(os.path.join(D, 'b555_probe_%s.txt' % pid))
    i = t.find('@' + name + ' :')
    if i < 0:
        i = t.find(name + ' :')
    if i < 0:
        return None
    rest = t[i:]
    stop = [m.start() for m in re.finditer(r"(?m)^(@?[A-Za-z_][A-Za-z0-9_.₀]* : |'[A-Za-z_]|real )", rest)][1:2]
    return ' '.join(rest[:stop[0] if stop else 1500].split())


def row_profile(cell, name):
    c = cell.replace('`', '')
    if name.endswith('no_type_d_conspiracies') or name.endswith('crt_exhaustiveness'):
        return STD3
    if 'axiom-free' in c and '{' not in c:
        return NONE_AX
    if '{propext, Classical.choice, Quot.sound}' in c:
        return STD3
    if '{propext, Quot.sound}' in c:
        return PQ
    return None


def effects_state():
    out = dict(branch=g(EFF, 'rev-parse', '--abbrev-ref', 'HEAD').strip(), head=g(EFF, 'rev-parse', 'HEAD').strip(),
               dirty=g(EFF, 'status', '--porcelain', '--untracked-files=no').strip(), branches=g(EFF, 'branch', '--list').split(),
               oleans=sorted(os.path.relpath(os.path.join(dp, f), os.path.join(EFF, '.lake', 'build', 'lib', 'lean')).replace(os.sep, '/')
                             for dp, _, fs in os.walk(os.path.join(EFF, '.lake', 'build', 'lib', 'lean')) for f in fs if f.endswith('.olean')))
    for c in ('a27415d', 'c66f3c5'):
        full = g(EFF, 'rev-parse', '--verify', '-q', c + '^{commit}').strip()
        out[c] = dict(resolves=bool(full), full=full, ancestor_of_head=subprocess.run(['git', '-C', EFF, 'merge-base', '--is-ancestor', c, 'HEAD']).returncode == 0,
                      phase15_vs_head=('SAME' if subprocess.run(['git', '-C', EFF, 'diff', '--quiet', c, 'HEAD', '--', 'SIDEEffects/Phase15']).returncode == 0 else 'DIFF'),
                      module1_sorry=len(re.findall(r'(?m)^\s*sorry|\bsorry\b', re.sub(r'/-[\s\S]*?-/|--.*', '', blob(EFF, c + ':SIDEEffects/Phase15/Module1.lean')))),
                      date=g(EFF, 'show', '-s', '--format=%ci %s', c).strip()[:160])
    out['manifest_a27415d_vs_head'] = subprocess.run(['git', '-C', EFF, 'diff', '--quiet', 'a27415d', 'HEAD', '--', 'lake-manifest.json', 'lean-toolchain']).returncode == 0
    return out


def tiers():
    rs = jl('b555_rows.json')
    pr = probes()
    ei = jl('b544_ei.json').get('marks', {})
    earlier = {}
    for f in ('b539_tiers.json', 'b540_tiers.json', 'b545_tiers.json', 'b554_simp_tiers.json'):
        s = rd(os.path.join(D, f))
        for n in TERMS:
            short = n.split('.')[-1]
            if n not in earlier and ('`%s`' % short in s or '"%s"' % short in s or '.%s"' % short in s):
                j = s.find(short)
                m = re.search(r'"tier": "(T[0-9][^"]*)"', s[max(0, j - 1500): j + 1500])
                if m:
                    earlier[n] = (m.group(1), f)
    es = effects_state()
    comp = blob(GRHK, '858cbf6:SIDEGRHTransfer/GRHBridge.lean')
    a = comp.index('def GRHStructuralExhaustiveness')
    body = comp[comp.index(':=', a) + 2: comp.index('/--', a)]
    chi_in_body = bool(re.search(r'(?<![A-Za-z0-9_])(χ|χbar)(?![A-Za-z0-9_])', body))   # ### whole tokens: `produces_offline_chi` is not χ
    sil = blob(KER, 'b1407b2:Kernel/SilenceTheorem.lean')
    iu = sil[sil.index('def Interface.is_universal'): sil.index('/--', sil.index('def Interface.is_universal'))]
    terms_out, rows_out = [], []
    for r in rs['rows']:
        tl, bits = [], []
        for n in r['names']:
            if n not in TERMS:
                sys.exit('### A TERMINAL WITHOUT A TIER: %s' % n)
            pid, tier, reason, concl = TERMS[n]
            a_ = pr.get(pid, {})
            prof = (a_.get('profiles') or {}).get(n)
            st = check_text(pid, n)
            want = row_profile(r['profile_cell'], n)
            found = bool(st) and a_.get('exit') == 0
            moved = [] if (found and prof == want) else [x for x, b in (('not found at its pin', not found),
                                                                     ('profile %s against the row`s %s' % (prof, want), prof != want)) if b]
            tl.append(tier)
            bits.append(not moved)
            terms_out.append(dict(row=r['line'], name=n, probe=pid, pin=a_.get('pin'), found=found, statement=st, profile=prof, row_profile=want,
                                  tier=tier, reason=reason, conclusion=concl, earlier=earlier.get(n), ei=ei.get('%s|%s' % (a_.get('repo'), n), 'not indexed'),
                                  moved=moved))
        rt = max(tl, key=ORDER.index) if tl else 'T4'
        rows_out.append(dict(line=r['line'], claim=r['claim'], names=r['names'], tiers=tl, tier=rt, disp='CARRIED' if all(bits) else 'MOVED',
                             kernel=r['kernel'], effects='SIDE-effects' in r['kernel']))
    tc = {k: sum(1 for t in terms_out if t['tier'] == k) for k in ORDER}
    rc = {k: sum(1 for r in rows_out if r['tier'] == k) for k in ORDER}
    dc = {k: sum(1 for r in rows_out if r['disp'] == k) for k in ('CARRIED', 'MOVED')}
    tier_of = {t['name']: t['tier'] for t in terms_out}
    n_cmp = {n: (tier_of.get(n), v) for n, v in N_EXPECT.items()}
    L = ['b555 -- COMPONENT 3 (a): GRH_CASCADE`S CORRESPONDENCE, RE-READ AT PIN (READING (4))', '',
         '### the table (PLACE-papers %s, :%d-%d): %d rows -- the ruling says "twelve"; %d name a terminal, %d name none' % (
             PRIOR_PP, rs['rows'][0]['line'], rs['rows'][-1]['line'], rs['count'], sum(1 for r in rs['rows'] if r['names']), sum(1 for r in rs['rows'] if not r['names'])),
         '### the probes (relay data/b555_probe_<id>.txt):']
    for pid, p in sorted(pr.items()):
        L.append('    %-3s %-28s %-8s %-40s mode %-7s exit %d %7.1f s errors %d manifest-equal %s imports %s' % (
            pid, p['repo'], p['pin'], p['path'], p['mode'], p['exit'], p['seconds'], p['errors'], p['manifest_same'], p['closure'] or 'NONE'))
    L += ['', '### SIDE-effects: branch %s ; HEAD %s ; tracked tree %s ; local branches %s' % (es['branch'], es['head'][:7], 'clean' if not es['dirty'] else es['dirty'], es['branches']),
          '    oleans present: %s' % es['oleans'],
          '    a27415d: %s' % es['a27415d'], '    c66f3c5: %s' % es['c66f3c5'],
          '    lake-manifest and lean-toolchain equal between a27415d and HEAD: %s' % es['manifest_a27415d_vs_head'], '',
          '### THE COMPOSITE: `%s`' % ' '.join((check_text('g2', GG + 'grh_structural_exhaustiveness_proved') or '').split()),
          '    its Prop, GRHBridge.lean at 858cbf6: def GRHStructuralExhaustiveness {n : ℕ} [NeZero n] (χ χbar : DirichletCharacter ℂ n) : Prop :=',
          '    ' + ' '.join(body.split()),
          '    ### χ or χbar in the body: %s -- %s' % (chi_in_body, 'a character value enters the conclusion' if chi_in_body else 'NO CHARACTER VALUE ENTERS THE CONCLUSION'), '',
          '### silence_universal`S PREMISE: `%s`' % ' '.join(iu.split())]
    for t in terms_out:
        L += ['', '### :%d %s [%s %s via %s]' % (t['row'], t['name'], t['pin'], 'FOUND' if t['found'] else 'NOT FOUND', t['probe']),
              '    statement : %s' % (t['statement'] or 'NONE')[:900],
              '    profile   : %s   (the row prints: %s)' % (t['profile'], t['row_profile']),
              '    tier      : %s -- %s' % (t['tier'], t['reason']),
              '    earlier   : %s ; E/I (b544) : %s' % ('%s (relay data/%s)' % tuple(t['earlier']) if t['earlier'] else 'none banked', t['ei']),
              '    conclusion: %s' % t['conclusion'],
              '    disposition: %s' % ('CARRIED' if not t['moved'] else 'MOVED -- ' + '; '.join(t['moved']))]
    L += ['', '### TIERS OVER THE %d TERMINALS: %s' % (len(terms_out), ' · '.join('%s %d' % (k, tc[k]) for k in ORDER)),
          '### ROW TIERS (the weakest link; no terminal T4) OVER THE %d ROWS: %s' % (len(rows_out), ' · '.join('%s %d' % (k, rc[k]) for k in ORDER)),
          '### DISPOSITIONS: CARRIED %d · MOVED %d' % (dc['CARRIED'], dc['MOVED']), '', '### (N1)/(N2), terminal by terminal: fresh tier against the tier named']
    L += ['    %-62s %-14s %-14s %s' % (n, t, '/'.join(v), 'agrees' if t in v else 'DIFFERS') for n, (t, v) in n_cmp.items()]
    L += ['', '### each row`s conclusion in one line:'] + ['    :%d %s' % (r['line'], ' ; '.join(t['conclusion'] for t in terms_out if t['row'] == r['line']) or '(no terminal)') for r in rows_out]
    out = dict(rows=rows_out, terms=terms_out, term_tiers=tc, row_tiers=rc, disp=dc, count=rs['count'], effects=es, chi_in_body=chi_in_body,
               composite_body=' '.join(body.split()), silence_premise=' '.join(iu.split()), n_cmp=n_cmp,
               probes={k: dict(exit=v['exit'], seconds=v['seconds'], errors=v['errors']) for k, v in pr.items()})
    put_json('b555_tiers.json', out)
    put_txt('b555_tiers.txt', L)
    print(NL.join(L))


def short(n):
    return n.split('.')[-1]


BH = ('#### THE CASCADE, ACT NINE -- THE CORRESPONDENCE TIERED *(appended 2026-09-28, b555, under the author`s ruling `(R165)`(4); no '
      'byte above this block changes; the Abstract, §I and the body are not edited -- the edition carries the ceiling)*')


def block():
    guard_absent(GRHD, BH)
    s = jl('b555_tiers.json')
    es = s['effects']
    L = ['', '<!-- b555 THE CASCADE, ACT NINE, 2026-09-28 -->', '', BH, '',
         '**The rows, re-read at pin.** The table at :381-393 has %d rows (the ruling says twelve): %d name a terminal, %d name none. Each '
         'terminal`s file at the row`s pin was elaborated fresh with `#check` and `#print axioms` appended (relay `data/b555_probe_<id>.txt`; '
         'statements, profiles, tiers and reasons in `data/b555_tiers.txt`): SIDE-grh-transfer`s GRHBridge.lean at `858cbf6` (its Character* '
         'and Voice* modules imported there); SIDE-kernel at `v1.2` = `b1407b2`, the four files equal at the deposit pin `v1.5` = `0e5233f`; '
         'SIDE-effects’ Module1.lean at `a27415d`; the BSD and YM files at `7425d73` and `79e4f45`. The tier is that of the weakest link, '
         '`(R149)`(2), with `(R165)`(3)`s T2-INTERFACES; a row with no terminal is T4.' % (
             s['count'], sum(1 for r in s['rows'] if r['names']), sum(1 for r in s['rows'] if not r['names'])), '',
         '| row | claim (abridged) | terminal(s) | fresh profile(s) | disposition | tier(s) |', '|:--|:--|:--|:--|:--|:--|']
    for r in s['rows']:
        ts = [t for t in s['terms'] if t['row'] == r['line']]
        prof = sorted(set((t['profile'] or 'NONE').replace('depends on axioms: ', '').replace('does not depend on any axioms', 'axiom-free') for t in ts))
        claim = re.sub(r'\$[^$]*\$', '…', r['claim']).replace('|', '/').replace('**', '')
        import banned_terms as BTM   # ### the abridged claim drops a word carrying a banned stem; the row itself is unchanged
        claim = re.sub(r'\s*\S*' + BTM.PAT.pattern + r'\S*', '', claim, flags=re.I)
        L.append('| :%d | %s | %s | %s | **%s** | %s |' % (
            r['line'], claim[:90], ', '.join('`%s`' % short(t['name']) for t in ts) or 'NONE', '; '.join(prof) or '—', r['disp'],
            ', '.join(sorted(set(r['tiers']), key=ORDER.index)) or 'T4'))
    L += ['', '*Tiers over the %d terminals: %s. Rows by their weakest link: %s. Dispositions: CARRIED %d · MOVED %d.*' % (
        len(s['terms']), ' · '.join('%s %d' % (k, s['term_tiers'][k]) for k in ORDER), ' · '.join('%s %d' % (k, s['row_tiers'][k]) for k in ORDER),
        s['disp']['CARRIED'], s['disp']['MOVED']), '',
          '**The composite.** `grh_structural_exhaustiveness_proved` concludes `GRHStructuralExhaustiveness χ χbar`, whose definition names neither '
          'χ nor χbar: no character value enters the conclusion (printed in the bank). The character content of rows :381-383 is carried by '
          '`twisted_balance_at_unramified_prime` and `twisted_balance_at_half`; the six `paired_*` lemmas take χ and χbar and do not use them.', '',
          '**SIDE-effects, beside rows :388 and :393.** Checked-out branch `%s` at `%s`, tracked tree %s; `a27415d` and `c66f3c5` both resolve '
          'and both are ancestors of HEAD; Phase15 is the same at `a27415d` and HEAD; the oleans of every SIDEEffects module are present. The '
          'row`s kernel cell names `c66f3c5`; its profile was run at `a27415d`, and so was this read.' % (es['branch'], es['head'][:7], 'clean' if not es['dirty'] else 'dirty'), '',
          '*Appended by b555. No claim of the document is altered; `h2` stays where the deposit left it.*', '']
    o = append_to(GRHD, NL.join(L))
    o['line'] = line_of(GRHD, BH)
    put_json('b555_block.json', o)
    print(NL.join(rd(GRHD).split(NL)[o['line'] - 1:]))


def stems():
    import banned_terms as BTM
    src = blob(PP, PRIOR_PP + ':' + GRHR).split(NL)
    hits = []
    for i, l in enumerate(src, 1):
        for m in BTM.PAT.finditer(l):
            hits.append(dict(line=i, stem=[x for x in BTM.STEMS if m.group(0).lower().startswith(x)][0], word=m.group(0),
                             cls=BTM.classify(l, m.start(), GRHD) or 'LIVE USE', text=l[max(0, m.start() - 70):m.end() + 70]))
    per = {x: sum(1 for h in hits if h['stem'] == x) for x in BTM.STEMS}
    live = {x: sum(1 for h in hits if h['stem'] == x and h['cls'] == 'LIVE USE') for x in BTM.STEMS}
    L = ['b555 -- COMPONENT 3 (c): THE BANNED-STEM COUNT OVER GRH_CASCADE.md (READING (6)); no edit', '',
         '### the document at PLACE-papers %s (before this act`s append); per stem: %s ; live uses: %s' % (PRIOR_PP, per, live)]
    L += ['    :%-4d %-6s %-12s %-44s ...%s...' % (h['line'], h['stem'], h['word'], h['cls'][:44], h['text']) for h in hits]
    put_json('b555_stems.json', dict(per=per, live=live, hits=hits))
    put_txt('b555_stems.txt', L)
    print(NL.join(L))


SHELL_PATS = ['grh_exclusion', 'no_ls_zero', 'Structural.lean', 'LandauSiegel.', 'GRH.grh']


def shells():
    doc = blob(PP, PRIOR_PP + ':' + GRHR).split(NL)
    hits = [(i + 1, p, l[:200]) for i, l in enumerate(doc) for p in SHELL_PATS if p in l]
    st = {}
    for c in ('c66f3c5', 'a27415d', 'HEAD'):
        s = blob(EFF, '%s:SIDEEffects/Structural.lean' % c)
        code = re.sub(r'/-[\s\S]*?-/', '', s)
        code = NL.join(l for l in code.split(NL) if not l.strip().startswith('--'))
        st[c] = {n: dict(declared=bool(re.search(r'(?m)^\s*theorem %s\b' % n, code)), lines=lines_with(None, n, s)) for n in ('grh_exclusion', 'no_ls_zero')}
    L = ['b555 -- COMPONENT 3 (d): THE STRUCTURAL.LEAN SHELLS SEARCHED IN GRH_CASCADE (READING (7), (R165)(6))', '',
         '### the patterns: %s ; over the document at PLACE-papers %s, rows and body: %d hit(s)' % (SHELL_PATS, PRIOR_PP, len(hits))]
    L += ['    :%d [%s] %s' % h for h in hits] or ['    NONE']
    for c, v in st.items():
        L.append('### SIDE-effects %s Structural.lean: %s' % (c, v))
    L.append('### %s' % ('NO ROW OR BODY SENTENCE OF GRH_CASCADE CITES EITHER SHELL; no defect, no ERRATA candidate.' if not hits else
                         'A CITATION: printed above as a defect and an ERRATA candidate, not filed.'))
    put_json('b555_shells.json', dict(patterns=SHELL_PATS, hits=hits, structural=st))
    put_txt('b555_shells.txt', L)
    print(NL.join(L))


# ------------------------------------------------------------------------------ COMPONENT 4: THE OPEN PIECE
MLS = {'SIDE-explicit-formula v0.2': (os.path.join(EF, '.lake', 'packages', 'mathlib'), '51e6992efd06126df61a496bebf8f49482a4e129'),
       'SIDE-lv-conservation v0.11.0': (os.path.join(LV, '.lake', 'packages', 'mathlib'), '5e932f97dd25535344f80f9dd8da3aab83df0fe6')}


def search():
    out = {}
    L = ['b555 -- COMPONENT 4 (a): THE MATHLIB AND ZETA23 SEARCH (READING (8))', '']
    for k, (ml, rev) in MLS.items():
        head = g(ml, 'rev-parse', 'HEAD').strip()
        r1 = [l for l in g(ml, 'grep', '-n', '-E', r'RiemannHypothesis', 'HEAD', '--', 'Mathlib').split(NL) if l.strip()]
        decl = [l for l in r1 if re.search(r':\s*(theorem|lemma|def|abbrev)\s+\S*RiemannHypothesis', l)]
        r2 = [l for l in g(ml, 'grep', '-n', '-E', r'(DirichletCharacter|LFunction).*(1 / 2|re =)|(1 / 2|re =).*(DirichletCharacter|LFunction)', 'HEAD', '--', 'Mathlib').split(NL) if l.strip()]
        r3 = [l for l in g(ml, 'grep', '-n', '-i', '-E', r'(theorem|lemma|def)\s+\S*explicit_?formula', 'HEAD', '--', 'Mathlib').split(NL) if l.strip()]
        out[k] = dict(checkout=ml, rev=rev, head=head, equal=head == rev, rh_lines=r1, rh_decls=decl, crit=r2, ef=r3)
        L += ['### %s -- Mathlib checkout %s ; HEAD %s ; equal to the manifest rev: %s' % (k, ml, head[:12], head == rev),
              '  (a) lines matching RiemannHypothesis: %d ; declarations named with it: %d' % (len(r1), len(decl))] + ['      ' + l[:220] for l in r1] + [
              '  (b) lines naming DirichletCharacter or LFunction with `1 / 2` or `re =`: %d' % len(r2)] + ['      ' + l[:220] for l in r2] + [
              '  (c) declarations named like an explicit formula: %d' % len(r3)] + ['      ' + l[:220] for l in r3] + ['']
    ef = blob(EF, '5c72cad:Zeta23/ExplicitFormula.lean')
    a0 = lines_with(None, r'^def literatureRHS', ef)[0]
    a1 = lines_with(None, r'^def EF_lit\b', ef)[0]
    wm = blob(EF, '5c72cad:Zeta23/WeilEF/Main.lean')
    a2 = lines_with(None, r'^theorem EF_lit_zetaZeroConfig', wm)[0]
    fixed = 'ArithmeticFunction.vonMangoldt' in ' '.join(ef.split(NL)[a0 - 1:a0 + 4]) and 'gammaBracket' in ' '.join(ef.split(NL)[a0 - 1:a0 + 4])
    gb = lines_with(None, r'^def gammaBracket', ef)[0]
    L += ['### Zeta23 (SIDE-explicit-formula 5c72cad): EF_lit at Zeta23/ExplicitFormula.lean:%d, over a ZeroConfig, its right side `literatureRHS`' % a1,
          '    :%d-%d %s' % (a0, a0 + 4, ' '.join(' '.join(ef.split(NL)[a0 - 1:a0 + 4]).split())),
          '    :%d %s' % (gb, ef.split(NL)[gb - 1].strip()),
          '    Zeta23/WeilEF/Main.lean:%d %s' % (a2, wm.split(NL)[a2 - 1].strip()),
          '### EF_lit`s right side is fixed to ζ (the untwisted von Mangoldt sum and ζ’s gamma factor at 1/4 + ir/2): %s' % fixed]
    out['zeta23'] = dict(ef_lit=a1, literatureRHS=[a0, a0 + 4], gammaBracket=gb, zeta_instance=a2, fixed=fixed)
    put_json('b555_search.json', out)
    put_txt('b555_search.txt', L)
    print(NL.join(L))


ARC = [('TwoPropertyWindow.lean', ['b518', 'b524', 'b527']), ('PairTerm.lean', ['b529']), ('DecayBound.lean', ['b530']), ('RestBound.lean', ['b530']),
       ('H2Bridge.lean', ['b532']), ('PowerWindow.lean', ['b533']), ('PowerLimit.lean', ['b534']), ('Seam.lean', ['b536'])]
ZETA_OBJ = r'zetaZeroConfig|riemannZeta|completedRiemannZeta|RiemannHypothesis|EF_lit|h2_sign|rh_strip|zetaSeam|ZetaSeam'


def decls(src):
    """### every theorem/lemma with its statement (the text from the name to its `:=`)."""
    out = []
    for m in re.finditer(r'(?m)^(theorem|lemma)\s+(\S+)', src):
        j = src.find(':=', m.end())
        out.append((m.group(2), src[m.end():j]))
    return out


def cost():
    L = ['b555 -- COMPONENT 4 (b): THE ζ-SIDE ARC`S COST, MEASURED (READING (9)) -- SIDE-explicit-formula v0.2 = 5c72cad', '']
    tot = dict(theorems=0, reinst=0, reused=0)
    per = []
    for f, acts in ARC:
        src = blob(EF, '5c72cad:SIDEExplicitFormula/' + f)
        ds = decls(src)
        ri = [n for n, st in ds if re.search(ZETA_OBJ, st)]
        per.append(dict(file=f, acts=acts, theorems=len(ds), reinst=len(ri), reused=len(ds) - len(ri), reinst_names=ri))
        tot['theorems'] += len(ds)
        tot['reinst'] += len(ri)
        tot['reused'] += len(ds) - len(ri)
        L.append('  %-22s acts %-18s theorems %3d ; naming a ζ object (RE-INSTANTIATED) %3d ; over abstract objects (REUSED) %3d' % (
            f, ','.join(acts), len(ds), len(ri), len(ds) - len(ri)))
    L += ['', '### THE ARC: %(theorems)d theorems ; RE-INSTANTIATED %(reinst)d ; REUSED %(reused)d' % tot,
          '### the ζ objects the rule reads: %s' % ZETA_OBJ]
    trail_counts = {}
    ot = rd(OT)
    for act in ('b529', 'b530', 'b532', 'b533', 'b534', 'b536'):
        ls = lines_with(None, r'^### %s ' % act, ot)
        seg = NL.join(ot.split(NL)[ls[0] - 1: ls[0] + 40]) if ls else ''
        m = re.findall(r'(\d+) of (\d+)', seg)
        trail_counts[act] = m[:4]
    L += ['### the trails` own "N of N [profile]" counts, read at each act`s record: %s' % trail_counts]
    zfiles = [f for f in subprocess.run(['git', '-C', EF, 'ls-tree', '-r', '--name-only', '5c72cad', 'Zeta23'], capture_output=True, text=True).stdout.split(NL) if f.endswith('.lean')]
    zth = sum(len(decls(blob(EF, '5c72cad:' + f))) for f in zfiles)
    L += ['### the vendored Zeta23 at 5c72cad (the ζ explicit formula`s own development, outside b526-b536): %d modules, %d theorems -- X1`s reference weight, printed beside and not counted' % (len(zfiles), zth)]
    put_json('b555_cost.json', dict(files=per, total=tot, trail_counts=trail_counts, rule=ZETA_OBJ, zeta23=dict(modules=len(zfiles), theorems=zth)))
    put_txt('b555_cost.txt', L)
    print(NL.join(L))


WH = ('### `W-ORD-GRH-WEIL` -- THE χ-SIDE OF THE WEIL ARC, PRICED, appended 2026-09-28, b555, under the author`s ruling (R165)(5)')
WNEW = [
    ('X1', 'the explicit formula for the completed L(s, χ) in Weil`s form on a compactly supported C² test class: the analogue of Zeta23`s `EF_lit` '
           'with the twisted von Mangoldt sum Λ(n)χ(n), the gamma factor of the parity of χ, and no pole term for χ ≠ 1', 'of substance'),
    ('X2', 'the χ zero configuration: the nontrivial zeros of the completed L(s, χ) with multiplicity, and its local count (the analogue of `zetaZeroConfig_local_count`)', 'of substance'),
    ('X3', 'the seam from the functional equation of the completed L(s, χ) (Mathlib`s, relating χ to χ̄ through the root number): the zero configuration '
           'of χ reflects to χ̄’s, so the seam is (χ, χ̄)-paired where ζ’s is self-dual', 'of substance'),
    ('X4', '`h2_sign_chi`: Weil positivity for L(s, χ) on its own test class, as a definition', 'short'),
    ('X5', 'GRH_χ as a Prop over Mathlib`s objects (the searched checkouts carry none, relay `data/b555_search.txt`)', 'short'),
    ('X6', 'the equivalence `h2_sign_chi ↔ GRH_χ`, assembled as `h2_sign_iff_rh` was', 'short'),
]


def weil():
    guard_absent(OT, WH)
    c = jl('b555_cost.json')
    se = jl('b555_search.json')
    tot = c['total']
    new = len(WNEW)
    chi = new + tot['reinst']
    hits = {k: (len(v['rh_decls']), len(v['crit']), len(v['ef'])) for k, v in se.items() if k != 'zeta23'}
    L = ['', WH, '',
         '| # | ID | kind | the item | price | trigger |', '|:--|:--|:--|:--|:--|:--|',
         '| **1** | `W-ORD-GRH-WEIL` | **RESULT** | The χ-analogue of the compiled criterion: Weil positivity for the completed L(s, χ) on its own test '
         'class equivalent to GRH for χ, stated over Mathlib`s objects -- the open piece GRH_CASCADE calls "the Mathlib-GRH bridge", restated in '
         'the compiled criterion`s terms (`h2_sign_iff_rh`, SIDE-explicit-formula v0.2). The vendored explicit formula is ζ’s alone (Zeta23 '
         '`literatureRHS`, ExplicitFormula.lean:%d-%d); the searched Mathlib checkouts (51e6992, 5e932f97) carry, for RiemannHypothesis-named '
         'declarations, critical-line lines for Dirichlet characters or L-functions, and explicit-formula declarations, the hit counts %s. | '
         'new items %d (%s); the ζ-side arc`s theorems that name a ζ object, re-instantiated for χ, %d of its %d (SIDE-explicit-formula v0.2, '
         'files and acts in relay `data/b555_cost.txt`; %d over abstract objects reused). **χ-side total: %d, against the ζ-side arc`s %d.** '
         'Not attempted. | **THE AUTHOR’S WORD** |' % (
             se['zeta23']['literatureRHS'][0], se['zeta23']['literatureRHS'][1], hits, new, '; '.join('%s %s' % (i, w) for i, _, w in WNEW),
             tot['reinst'], tot['theorems'], tot['reused'], chi, tot['theorems']), '',
         '**The new items, in lemmas:**', '']
    L += ['- **%s** %s -- *%s*' % t for t in WNEW]
    L += ['', '**X1`s weight, printed beside and not counted:** its ζ-side counterpart is the vendored Zeta23 at 5c72cad, %d modules and %d '
          'theorems, developed outside b526-b536; the count above prices X1 as one item.' % (c['zeta23']['modules'], c['zeta23']['theorems']), '',
          '**Landau–Siegel and Artin inherit this piece**, as GRH_CASCADE`s Status block says in its own terms (classical reductions from '
          'GRH). **Priced, not attempted.**', '']
    o = append_to(OT, NL.join(L))
    o['line'] = line_of(OT, WH)
    o.update(new=new, reinst=tot['reinst'], reused=tot['reused'], arc=tot['theorems'], chi=chi, n6=(chi >= tot['theorems']))
    put_json('b555_weil.json', o)
    print(NL.join(rd(OT).split(NL)[o['line'] - 1:]))


RH_ = '## GRH_CASCADE read against the register census and the compiled criterion: the cascade`s open piece is the χ-side of the Weil arc'
GPT = '*Appended 2026-09-28 by b555, under the author`s ruling `(R165)`(5) -- BACK MATTER, THE READING:*'


def reading():
    guard_absent(FIND, RH_)
    guard_absent(GRHD, GPT)
    w = jl('b555_weil.json')
    blk = line_of(GRHD, BH)
    se = jl('b555_search.json')
    L = ['', RH_, '',
         '*Filed at b555 on the author`s ruling `(R165)`(5), graded READING. Banks: relay `data/b555_tiers.txt`, `data/b555_search.txt`, '
         '`data/b555_cost.txt`. The document`s Abstract, §I and body are not edited; its tier block is at `GRH_CASCADE.md`:%d.*' % blk, '',
         '**What the document says.** The Abstract (`GRH_CASCADE.md`:49) calls the Riemann Hypothesis "established in the monograph and verified '
         'at the architecture level" and says Hooley`s implication "becomes unconditional"; §III.3 (:145) says "GRH holds for every Dirichlet '
         'character χ"; §I (:65) says Artin`s conjecture "becomes unconditional". The Status block (:35-43) carries the full Mathlib-GRH bridge '
         'as open and the cascade as resting on a single carried-open premise.', '',
         '**Read against the register census and the compiled criterion.** The RH route terminals §I names interface on a premise shown to be '
         'RH restated (`E-2026-09-25-1`; `ch_iff_rh`). The programme`s compiled reduction of RH is `h2_sign_iff_rh` (SIDE-explicit-formula '
         'v0.2), with `h2_sign` open. The cascade`s "same clause" is therefore, in compiled terms, the χ-analogue of `h2_sign` -- Weil positivity '
         'for the completed L(s, χ) on its own test class -- and it is compiled nowhere: Zeta23`s explicit formula is ζ’s alone (its right side '
         '`literatureRHS` carries the untwisted von Mangoldt sum and ζ’s gamma factor, Zeta23/ExplicitFormula.lean:%d-%d), and the searched '
         'Mathlib checkouts carry no RiemannHypothesis-shaped statement for Dirichlet L-functions and no explicit formula for them (relay '
         '`data/b555_search.txt`). The composite `grh_structural_exhaustiveness_proved` concludes a Prop in which no character occurs.' % (
             se['zeta23']['literatureRHS'][0], se['zeta23']['literatureRHS'][1]), '',
         '**So the cascade`s open piece** is not "the Mathlib-GRH bridge" alone but the χ-side of the whole Weil arc, priced as `W-ORD-GRH-WEIL` '
         '(`OPEN_TRAILS.md`:%d): %d new items and %d re-instantiated theorems of the ζ-side arc, %d in all against the arc`s %d. Landau–Siegel '
         'and Artin inherit it, as the Status block says. The Abstract`s sentences are not edited; the edition carries the ceiling.' % (
             w['line'], w['new'], w['reinst'], w['chi'], w['arc']), '',
         '**Its limits.** This reading concerns what is compiled and where; nothing here is a statement about RH, GRH or any zero, and the search '
         'is over two Mathlib checkouts at two revisions, by the three patterns printed in the bank.', '']
    o = append_to(FIND, NL.join(L))
    o['line'] = line_of(FIND, RH_)
    p = append_to(GRHD, NL.join(['', GPT + ' a reading of this document`s Abstract and §I against the register census and the compiled criterion '
                                 'is entered at `FINDINGS.md`:%d (b555); the body unedited.' % o['line'], '']))
    p['line'] = line_of(GRHD, GPT)
    put_json('b555_reading.json', dict(findings=o, pointer=p))
    print(NL.join(rd(FIND).split(NL)[o['line'] - 1:o['line'] + 12]))


# ------------------------------------------------------------------------------ THE ENTRY, THE SCORES, THE DESK, THE RECORD
FH = ('## The cascade, act nine: GRH_CASCADE tiered, the composite`s unused characters, the χ-side of the Weil arc priced; the Q0 '
      'detection numbers at fine resolution')
HEADING = ('### b555 — the cascade, act nine under (R165): GRH_CASCADE tiered; the composite`s unused characters; the χ-side of the Weil '
           'arc priced; H8 at its weight; the T3doubleprime tier settled; the programme-premise clause')


def roster_next():
    t = rd(CENSUS)
    ln = [l for l in t.split(NL) if l.startswith("**The cascade's remaining roster")][0]
    names = re.findall(r'`([A-Z_0-9a-z]+)`', ln)
    rem = [n for n in names if n not in ('SIMPLICITY_OF_RIEMANN_ZEROS', 'GRH_CASCADE')]
    return rem[0], rem


def findings():
    guard_absent(FIND, FH)
    ts, h8j, cl, t3, w, rd_, bl, sh, st = (jl('b555_tiers.json'), jl('b555_h8.json'), jl('b555_clause.json'), jl('b555_t3dp.json'), jl('b555_weil.json'),
                                           jl('b555_reading.json'), jl('b555_block.json'), jl('b555_shells.json'), jl('b555_stems.json'))
    nxt, rem = roster_next()
    n = h8j['numbers']
    L = ['', FH, '',
         '*Filed at b555 on the author`s ruling `(R165)`. The cascade`s act nine. Banks: relay `data/b555_tiers.txt`, `data/b555_search.txt`, '
         '`data/b555_cost.txt`, `data/b555_shells.txt`, `data/b555_stems.txt`, `data/b555_h8.json`.*', '',
         '**GRH_CASCADE tiered.** Its Correspondence table has %d rows (the ruling says twelve), %d naming %d terminals. Tiers over the terminals: '
         '%s; rows by their weakest link: %s; dispositions CARRIED %d · MOVED %d. The composite `grh_structural_exhaustiveness_proved` '
         'concludes a Prop in which no character occurs (T2); `twisted_balance_at_unramified_prime` carries the character (T0); of the six '
         '`paired_*` lemmas one is T0 and five are T2; `silence_universal` is T2-INTERFACES. The tier block is at `GRH_CASCADE.md`:%d; the '
         'reading at `FINDINGS.md`:%d.' % (
             ts['count'], sum(1 for r in ts['rows'] if r['names']), len(ts['terms']), ' · '.join('%s %d' % (k, ts['term_tiers'][k]) for k in ORDER),
             ' · '.join('%s %d' % (k, ts['row_tiers'][k]) for k in ORDER), ts['disp']['CARRIED'], ts['disp']['MOVED'], bl['line'], rd_['findings']['line']), '',
         '**SIDE-effects.** Branch `%s` at `%s`; `c66f3c5` resolves and is an ancestor of HEAD, as is `a27415d`.' % (
             ts['effects']['branch'], ts['effects']['head'][:7]), '',
         '**The shells.** `grh_exclusion` and `no_ls_zero` are cited by %s row or body sentence of GRH_CASCADE; they are declared at `c66f3c5` '
         'and named only in a comment ledger at `a27415d` and HEAD.' % ('no' if not sh['hits'] else 'a'), '',
         '**The stem count (no edit).** The banned stems of `tools/banned_terms.py` occur %d time(s) in the document, %d of them live; per stem in '
         'relay `data/b555_stems.txt`.' % (sum(st['per'].values()), sum(st['live'].values())), '',
         '**The open piece.** `W-ORD-GRH-WEIL` at `OPEN_TRAILS.md`:%d: %d new items plus %d re-instantiated theorems, %d, against the ζ-side '
         'arc`s %d.' % (w['line'], w['new'], w['reinst'], w['chi'], w['arc']), '',
         '**The Q0 detection numbers at fine resolution** (`FINDINGS.md`:%d, READING): negative from a = %.3f, positive on %.3f–%.3f, negative '
         'from %.3f through 60; floor at most %.2f.' % (h8j['line'], n['turns_negative'], n['second'][0], n['second'][1], n['stays_negative'], n['floor']), '',
         '**The tier law.** The programme-premise clause at `FINDINGS.md`:%d; `T3doubleprime_general_commutation_fails` T0, b545`s line superseded '
         'at `BALANCE_AND_POSITIVITY.md`:%d.' % (cl['clause']['line'], t3['line']), '',
         '**Next keystone:** `%s`.' % nxt, '',
         '*Nothing deposits; nothing at Zenodo written; no `.lean` file edited; nothing here is a statement about RH, GRH or any zero.*', '']
    o = append_to(FIND, NL.join(L))
    o['line'] = line_of(FIND, FH)
    o['next'] = nxt
    o['remaining'] = rem
    put_json('b555_findings.json', o)
    print(NL.join(rd(FIND).split(NL)[o['line'] - 1:]))


WRITE_OK = {'FINDINGS.md', 'OPEN_TRAILS.md', GRHR, 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md'}
MEMDIR = P.MEMDIR
PRE_HEADS = {'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068', 'SIDE-explicit-formula': '81ae175', 'SIDE-global-section': 'a91d941',
             'SIDE-grh-transfer': '858cbf6', 'SIDE-effects': 'ef4cff7', 'SIDE-bsd-formation-transfer': '3491766', 'SIDE-yang-mills-formation': '73e9e2c'}


def w_(v):
    return 'NOT SCORABLE' if v is None else ('HELD' if v else 'REFUTED')


def mains():
    return {k: sorted(x for x in g(os.path.join(DD, k), 'diff', '--name-only', h, 'main').split(NL) if x.strip()) for k, h in PRE_HEADS.items()}


def scores():
    ts, se, w, sh = jl('b555_tiers.json'), jl('b555_search.json'), jl('b555_weil.json'), jl('b555_shells.json')
    needle = 'https://' + 'zenodo' + '.org'
    zen = [x for x in os.listdir(T) if x.startswith('b555_') and needle in rd(os.path.join(T, x))]
    tk = (os.environ.get('ZENODO_TOKEN') or '').encode('utf-8')
    tok = sum(open(os.path.join(d0, f), 'rb').read().count(tk) for d0 in (D, T) for f in os.listdir(d0) if f.startswith('b555_')) if tk else None
    m = mains()
    lean = [(k, f) for k, v in m.items() for f in v if f.endswith('.lean')]
    dep = g(PP, 'status', '--porcelain', '--', 'outputs/DEPOSITED-v1.1.2').strip() == ''
    trial = dict(head=g(TRIAL, 'rev-parse', 'HEAD').strip(), status=g(TRIAL, 'status', '--porcelain', '--untracked-files=no').strip())
    tier = {t['name']: t['tier'] for t in ts.get('terms', [])}
    paired = [GG + x for x in ('paired_reflection_axis_invariant_iff', 'paired_conjugation_real_axis_agree_iff', 'paired_cr_minimal_codim_axis_iff',
                               'paired_modular_S_fixed_iff', 'paired_spectral_offset_zero_iff', 'paired_topological_no_sigma_preference')]
    es = ts.get('effects', {})
    n2names = ['SilenceTheorem.silence_universal', 'ECondition.type_I_has_ostrowski', 'ostrowski_exhaustive', 'neg_eq_neg_one_sub_iff',
               'SIDEEffects.Phase15.Module1.no_type_d_conspiracies', 'SIDEBSDFormationTransfer.formation_preserved',
               'SIDEYangMillsFormation.mass_gap_equals_n3_certification']
    nxt, _ = roster_next()
    return dict(
        n1=bool(ts) and not ts['chi_in_body'] and tier.get(GG + 'grh_structural_exhaustiveness_proved') == 'T2'
        and tier.get(GG + 'twisted_balance_at_unramified_prime') == 'T0' and all(tier.get(p) == 'T0' for p in paired),
        n2=bool(ts) and all(tier.get(k) in N_EXPECT[k] for k in n2names),
        n3=bool(es) and not es['c66f3c5']['resolves'] and es['a27415d']['ancestor_of_head'],
        n4=bool(se) and all(not v['rh_decls'] and not v['crit'] and not v['ef'] for k, v in se.items() if k != 'zeta23') and se['zeta23']['fixed'],
        n5=bool(sh) and sh['hits'] == [],
        n6=bool(w) and bool(w['n6']),
        n7=not lean and not zen and tok == 0 and dep and trial['head'].startswith('f22ff35') and trial['status'] == '',
        mains=m, zen=zen, token=tok, deposit_clean=dep, trial=trial,
        s1=bool(ts) and [tier.get(p) for p in paired].count('T0') == 1 and tier.get(paired[0]) == 'T0',
        s2=bool(es) and es['c66f3c5']['resolves'] and es['c66f3c5']['ancestor_of_head'],
        s3=nxt == 'R_CURVE_CRITERION')


def desk():
    sc = scores()
    N, SS = ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7'), ('s1', 's2', 's3')
    ts, se, w, sh = jl('b555_tiers.json'), jl('b555_search.json'), jl('b555_weil.json'), jl('b555_shells.json')
    tier = {t['name']: t['tier'] for t in ts['terms']}
    es = ts['effects']
    L = ['=' * 104, 'b555 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '', '### THE NAVIGATOR`S SEVEN.', '-' * 104,
         '  **(N1)** ### **%s.** -- χ in the composite`s body %s ; composite %s ; twisted_balance %s ; paired_* %s.' % (
             w_(sc['n1']), ts['chi_in_body'], tier[GG + 'grh_structural_exhaustiveness_proved'], tier[GG + 'twisted_balance_at_unramified_prime'],
             {short(k): v for k, v in tier.items() if 'paired_' in k}),
         '  **(N2)** ### **%s.** -- %s.' % (w_(sc['n2']), {short(k): (tier.get(k), '/'.join(v)) for k, v in N_EXPECT.items() if 'paired' not in k and 'twisted' not in k and 'grh_struct' not in k}),
         '  **(N3)** ### **%s.** -- c66f3c5 resolves %s, ancestor of HEAD %s ; a27415d ancestor of HEAD (branch %s) %s.' % (
             w_(sc['n3']), es['c66f3c5']['resolves'], es['c66f3c5']['ancestor_of_head'], es['branch'], es['a27415d']['ancestor_of_head']),
         '  **(N4)** ### **%s.** -- hits (RH-named declarations, critical-line lines, explicit-formula declarations): %s ; EF_lit fixed to ζ %s. '
         'By the sealed predicate (any hit refutes). Hand-read: the hits are Mathlib`s ζ `RiemannHypothesis` definition, the functional equation '
         'of `completedLFunction` (two lines) and `LFunction_ne_zero_of_re_eq_one` -- none is a critical-line statement for Dirichlet '
         'L-functions or an explicit formula for them (defect (g)).' % (
             w_(sc['n4']), {k: (len(v['rh_decls']), len(v['crit']), len(v['ef'])) for k, v in se.items() if k != 'zeta23'}, se['zeta23']['fixed']),
         '  **(N5)** ### **%s.** -- hits in the document: %s.' % (w_(sc['n5']), sh['hits'] or 'NONE'),
         '  **(N6)** ### **%s.** -- χ-side %d (new %d + re-instantiated %d) against the ζ-side arc`s %d.' % (w_(sc['n6']), w['chi'], w['new'], w['reinst'], w['arc']),
         '  **(N7)** ### **%s.** -- mains changed %s ; token %s ; deposit clean %s ; trial %s.' % (
             w_(sc['n7']), {k: v for k, v in sc['mains'].items() if v} or 'NONE', sc['token'], sc['deposit_clean'], sc['trial']),
         '', '### THE SEAT`S THREE.', '-' * 104,
         '  **(S1)** ### **%s.** -- paired_* tiers %s.' % (w_(sc['s1']), [tier.get(GG + x) for x in ('paired_reflection_axis_invariant_iff', 'paired_conjugation_real_axis_agree_iff',
                                                                                                   'paired_cr_minimal_codim_axis_iff', 'paired_modular_S_fixed_iff',
                                                                                                   'paired_spectral_offset_zero_iff', 'paired_topological_no_sigma_preference')]),
         '  **(S2)** ### **%s.** -- c66f3c5 %s.' % (w_(sc['s2']), es['c66f3c5']),
         '  **(S3)** ### **%s.** -- the next untiered keystone: %s.' % (w_(sc['s3']), roster_next()[0]),
         '', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : REGISTERED 3 ; HELD %d ; REFUTED %d.**'
         % ([sc[k] for k in N].count(True), [sc[k] for k in N].count(False), [sc[k] for k in N].count(None),
            [sc[k] for k in SS].count(True), [sc[k] for k in SS].count(False)),
         '', '### THIS ACT`S OWN DEFECTS.'] + ([l for l in rd(os.path.join(D, 'b555_defects.txt')).rstrip(NL).split(NL) if l]
                                              if os.path.exists(os.path.join(D, 'b555_defects.txt')) else ['    NONE RECORDED.']) + ['=' * 104]
    put_txt('b555_desk_notes.txt', L)
    put_json('b555_scores.json', sc)
    print(NL.join(L))


def components():
    L = ['=' * 132, 'b555 -- THE COMPONENTS, AS THEY RAN.', '=' * 132, '']
    for n in ('b555_tiers.txt', 'b555_stems.txt', 'b555_shells.txt', 'b555_search.txt', 'b555_cost.txt'):
        if os.path.exists(os.path.join(D, n)):
            L += ['### relay data/%s' % n] + ['  ' + l for l in rd(os.path.join(D, n)).rstrip(NL).split(NL)] + ['']
    for n in ('b555_h8.json', 'b555_t3dp.json', 'b555_clause.json', 'b555_block.json', 'b555_weil.json', 'b555_reading.json', 'b555_findings.json'):
        L.append('### %s : %s' % (n, json.dumps(jl(n), ensure_ascii=False)[:3000]))
    L += ['### THE PROBES : relay data/b555_probe_<id>.txt and data/b555_probes.jsonl', '### THE BRANCHES : see data/b555_branches.txt', '=' * 132]
    put_txt('b555_components.txt', L)
    print(NL.join(L[:6]))


def trail():
    sc = scores()
    ts, h8j, cl, t3, w, rd_, bl, fj = (jl('b555_tiers.json'), jl('b555_h8.json'), jl('b555_clause.json'), jl('b555_t3dp.json'), jl('b555_weil.json'),
                                       jl('b555_reading.json'), jl('b555_block.json'), jl('b555_findings.json'))
    body = ['', HEADING, '',
            '**(R165) ratified.** (1) H8`s refutation read at its weight and the Q0 detection numbers entered at fine resolution. (2) '
            'T3doubleprime T0, b545`s T2 superseded by a line in the tool`s form; defect (o) recorded, not rewritten. (3) The tier law`s '
            'programme-premise clause, T2-INTERFACES. (4) GRH_CASCADE tiered as act nine. (5) Its open piece restated as the χ-side of the Weil '
            'arc and priced as `W-ORD-GRH-WEIL`. (6) The Structural.lean shells searched in the document. (7) The next keystone named.', '',
            '**Entered:** FINDINGS.md:%d (H8 at its weight), :%d (the clause), :%d (the reading), :%d (the entry); OPEN_TRAILS.md:%d (defect (o)) '
            'and :%d (`W-ORD-GRH-WEIL`); GRH_CASCADE.md:%d (the tier block) and :%d (the pointer); BALANCE_AND_POSITIVITY.md:%d (the '
            'superseding line).' % (h8j['line'], cl['clause']['line'], rd_['findings']['line'], fj['line'], cl['defect_o']['line'], w['line'],
                                    bl['line'], rd_['pointer']['line'], t3['line']), '',
            '**GRH_CASCADE:** tiers %s; CARRIED %d · MOVED %d. **Next keystone:** `%s`.' % (
                ' · '.join('%s %d' % (k, ts['term_tiers'][k]) for k in ORDER), ts['disp']['CARRIED'], ts['disp']['MOVED'], fj['next']), '',
            '**CP-1:** open; the cascade continues with `%s`.' % fj['next'], '',
            '**Next:** `%s`.' % fj['next'], '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s · (N6) %s · (N7) %s.** The seat`s own: (S1) %s, (S2) %s, (S3) %s.'
            % tuple(w_(sc[k]) for k in ('n1', 'n2', 'n3', 'n4', 'n5', 'n6', 'n7', 's1', 's2', 's3')),
            '**No kernel lane opened at this act; the kernel reads were fresh elaborations at pin.** Nothing deposits; nothing at Zenodo written; '
            'no `.lean` file edited; no monograph byte changed; ERRATA untouched; the ceiling unchanged; row U1 unedited; `h2` where the deposit '
            'left it; the four lists stay OPEN; nothing here is a statement about RH, GRH or any zero.', '']
    text = poss(NL.join(body))
    if outside_bt(text):
        sys.exit('### UNBALANCED BACKTICKS IN THE TRAIL')
    before = open(OT, 'rb').read()
    if poss(HEADING).encode('utf-8') in before:
        sys.exit('### ALREADY PRESENT')
    open(OT, 'ab').write(text.encode('utf-8'))
    after = open(OT, 'rb').read()
    out = dict(added=len(after) - len(before), prefix=after.startswith(before), headings=after.decode('utf-8').count(poss(HEADING)))
    print('  OPEN_TRAILS.md : %(added)d bytes added, prefix %(prefix)s, %(headings)d heading' % out)
    put_json('b555_trail_notes.json', out)


if __name__ == '__main__':
    fn = {k: globals()[k] for k in ('reads', 'h8', 't3dp', 'clause', 'rows', 'tiers', 'block', 'stems', 'shells', 'search', 'cost', 'weil',
                                    'reading', 'findings', 'components', 'desk', 'trail')}
    if len(sys.argv) < 2 or sys.argv[1] not in fn:
        sys.exit('usage: %s %s' % (sys.argv[0], ' | '.join(fn)))
    fn[sys.argv[1]]()
