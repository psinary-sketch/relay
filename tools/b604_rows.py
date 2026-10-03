# -*- coding: utf-8 -*-
"""b604_rows.py -- THE SIEVE TABLE'S DATA, UNDER (R214)(4) AND THE AUTHOR'S THREE ANSWERS BEFORE THE SEAL. ### DATA ONLY.

### Read by tools/b604_record.py (the mapping bank, the edition, the scores) and by tools/b604_checks.py. Every row is ONE
### conclusion: the current version's conclusions (CV, each re-read as it stands), one row per page theorem whose statement is
### a conclusion (plumbing in its conclusion's row as the compiled face, the author's answer), and the four readings the
### record carries that are not compiled (graded as readings). Every shape is hand-read (H) at this act; every test is read
### by hand against its instrument at its pin. No act number in any body cell (H38b): act numbers live in ACTS, which only
### the back matter's Correspondence prints.
"""

# ### the five tests, as the author defined them in the answer before the seal (relay data/b604_author_answers.txt), the
# ### instruments at their pins; the ruling's grouping of Theorem 3.1 with 3.7 is the navigator's, recorded at the act record
PP_I7 = '847e433'       # PLACE-papers commit last touching phase1.5/method/INSTRUMENTS.md
PP_IB = '1d0109f'       # PLACE-papers commit of phase1.5/method/INVARIANCE_BARRIERS_v1_4.md
TESTS = {
    1: dict(name='Placement register', q='the conclusion carries each zero’s real part, not an average over zeros',
            inst='INSTRUMENTS.md I-7, the placement screen (:93, its second run :148), and INVARIANCE_BARRIERS v1.4 Theorem 3.1 (:148) '
                 'with Proposition 3.5’s witness (:188), one test as I-7’s own cross-reference reads them',
            pin='PLACE-papers %s (I-7) and %s (INVARIANCE_BARRIERS v1.4)' % (PP_I7, PP_IB), short='I-7 @ %s; IB Thm 3.1 @ %s' % (PP_I7, PP_IB)),
    2: dict(name='Prime side', q='the route would fail on the Epstein configuration',
            inst='`detector` and `epstein_not_h2_sign_cfg`, and INVARIANCE_BARRIERS v1.4 Theorem 3.7 (:259): no derivation confined to the '
                 'named toolkit succeeds without the Euler product',
            pin='SIDE-explicit-formula v0.16 = c404e72; PLACE-papers %s' % PP_IB, short='detector, epstein @ v0.16 = c404e72; IB Thm 3.7 @ %s' % PP_IB),
    3: dict(name='Conductor uniformity', q='the conductor enters once per summand',
            inst='`EF_lit_chi_holds` and `family_theorem`; read for a row over a character or a family, n/a for a row with none',
            pin='SIDE-explicit-formula v0.13 = ac157c1 and v0.21 = 1d5d4dd', short='EF_lit_chi_holds @ v0.13 = ac157c1; family_theorem @ v0.21 = 1d5d4dd'),
    4: dict(name='Quantifier', q='UNIVERSAL, or a ladder of FINITE rungs whose limit is UNIVERSAL',
            inst='`h2_sign_iff_forall_upto` and `forall_upto_iff_rh` (the forall_upto pair), and `li_nonneg_iff_rh`',
            pin='SIDE-explicit-formula v0.3 = 04eda4a and v0.9 = e5a5a83', short='forall_upto pair @ v0.3 = 04eda4a; li_nonneg_iff_rh @ v0.9 = e5a5a83'),
    5: dict(name='Compiled face', q='the conclusion attaches to a declaration at a pin',
            inst='the pages’ node lists -- the ζ page’s at its own pin, the χ page’s at v0.21 -- and, for the Core shadows the current '
                 'version cites, the SIDE-global-section correspondence; it is also the compiled-face column’s source',
            pin='SIDE-explicit-formula v0.20 = 914c413 (the ζ list) and v0.21 = 1d5d4dd (the χ list); SIDE-global-section 3528bcf',
            short='node lists @ v0.20 = 914c413, v0.21 = 1d5d4dd'),
}

# ### the clusters, as SPIRAL_MAP §4A's refreshed table carries them (b388, re-anchored at (R21)); the order of the table
CLUSTERS = [
    ('RH', 'Simplicity / RH cascade'), ('FD', 'Foundations'), ('MT', 'Methodology'), ('CT', 'Cubit / Trivium'),
    ('MC', 'Matter / cosmology'), ('PH', 'Philosophy / cognition / interfaces'), ('TS', 'theory-space'), ('XD', 'cross-domain'),
]

# ### the registers: the three bright ones the ruling names, the three dark ones its bench carries, and the current version's
# ### own objects (VERIFICATION_LOOM's findings pass, the seven objects) with multiplicity, restatement and the record
REGISTERS = [
    ('prime-side control', 'bright', 'statements carrying the explicit formula’s prime side: Weil positivity, the χ instance, the family, the product of configurations'),
    ('the Li ladder', 'bright', 'the λ_n, the Keiper face, the Bombieri–Lagarias arithmetic limits, the register-4 and Taylor forms'),
    ('crossing geometry', 'bright', 'where a window or a sign meets a zero’s height: the finite-support ladder, the detector and its windows, the margin’s crossings'),
    ('the super-repulsion fit', 'dark', 'spacing statistics of the ordinates'),
    ('the 0.6725 ceiling', 'dark', 'proportions of the zeros simple and on the line'),
    ('the Epstein witnesses', 'dark', 'the control function with off-line zeros, numerical and compiled'),
    ('multiplicity', 'own', 'simplicity and the weight a zero’s multiplicity carries'),
    ('restatement', 'own', 'a clause shown to be RH restated'),
    ('the identity and its terms', 'own', 'the finite-instance identity, its archimedean term, the apportionment family and its share'),
    ('the density and its channel', 'own', 'the deviation’s one density, its kernel, the balanced window, the bench lane'),
    ('the towers, the junction and the plane', 'own', 'cross-place structure, the coherence premise, the assembly'),
    ('the boundary', 'own', 'the licensing question at the carrier’s edge'),
    ('the archimedean place', 'own', 'the archimedean place’s values, its Sonin sector and its channel'),
    ('the codes and the substrate', 'own', 'the Steane/Fano labelling and its arithmetic'),
    ('the constants and the empirical layer', 'own', 'Ω_b, ΔH₀, α_t: empirically anchored tags'),
    ('the record', 'own', 'statements about the corpus’s own work, its instruments, folds and limits -- not about its object'),
]

# ### tag -> (commit, the act its tag message names), read from SIDE-explicit-formula's tags at this act
TAGS = {'v0.1': ('baed4df', 'b534'), 'v0.2': ('5c72cad', 'b536'), 'v0.3': ('04eda4a', 'b560'), 'v0.4': ('941503b', 'b560'),
        'v0.6': ('de1f175', 'b562'), 'v0.7': ('1e4a007', 'b563'), 'v0.8': ('6ec71b3', 'b564'), 'v0.9': ('e5a5a83', 'b566'),
        'v0.10': ('6baed63', 'b567'), 'v0.11': ('19b7d1e', 'b569'), 'v0.13': ('ac157c1', 'b571'), 'v0.14': ('4dce7b9', 'b572'),
        'v0.15': ('21c8c52', 'b573'), 'v0.16': ('c404e72', 'b590'), 'v0.17': ('5a1630b', 'b596'), 'v0.18': ('1dd5cd7', 'b600'),
        'v0.19': ('5fc0c87', 'b601'), 'v0.20': ('914c413', 'b602'), 'v0.21': ('1d5d4dd', 'b603')}
GS_PIN = '3528bcf'

EF = 'SIDEExplicitFormula.'
P_ZETA, P_CHI = 'zeta', 'chi'


def F(name, tag, page=None, role='face'):
    """### a compiled face: the declaration's full name, its entry tag, the page that carries it ('zeta', 'chi', 'chi-corr' for
    ### a χ Correspondence row, None for a declaration on neither page) and its role (the row's 'face' or 'plumbing')."""
    return dict(name=name, tag=tag, page=page, role=role)


def G(name, row):
    """### a Core shadow on the SIDE-global-section correspondence at 3528bcf, by its row."""
    return dict(name=name, tag='SIDE-global-section %s' % GS_PIN, page=None, role='face', corr_row=row)


def T(*runs):
    """### the tests as run, in order: (n, 'PASS'|'FAIL'|'n/a', why). The sieve stops at the first FAIL."""
    return [dict(n=n, r=r, why=w) for n, r, w in runs]


NOZERO = 'no zero is named: the conclusion is about %s'
AGG = 'one aggregate over the zeros (%s), not each zero’s real part'
IDAGG = 'an identity between aggregates over the zeros, true wherever the zeros lie'
MULT = 'it carries each zero’s multiplicity, not its real part'
GENERIC = 'generic over configurations: the same route goes through at the Epstein configuration'
ZEROSIDE = 'a zero-side route naming no prime: Li’s criterion runs the same way for the Epstein function’s own coefficients'
RESTATE = 'a restatement: the same ten-line route restates the Epstein function’s own clause'
EACH = 'it is equivalent at its compiled face to every zero (or point) on the line'
EULER = 'its route consumes %s, which the Epstein configuration carries only as a premise'
UNI = 'UNIVERSAL'
LADDER = 'a ladder of FINITE rungs whose limit is UNIVERSAL'
FAM_U = 'a FAMILY of UNIVERSAL statements, one per character'
FACE_OK = 'a declaration at its pin on the %s page'
NA3 = 'no character enters'


def bright(why1, why2, why3, why4, why5):
    return T((1, 'PASS', why1), (2, 'PASS', why2), (3, 'n/a' if why3 is None else 'PASS', why3 or NA3), (4, 'PASS', why4), (5, 'PASS', why5))


ROWS = []


def R(id_, register, sentence, shape, shape_src, tests, faces, acts, cv=(), grade=None, strike=None, note=None):
    ROWS.append(dict(id=id_, cluster=id_.split('-')[0], register=register, sentence=sentence, shape=shape, shape_src=shape_src,
                     tests=tests, faces=list(faces), acts=list(acts), cv=list(cv), grade=grade, strike=strike, note=note))


# ================================================================ SIMPLICITY / RH CASCADE -- the compiled conclusions of the pages
R('RH-01', 'prime-side control',
  'Weil positivity on classK (h2_sign) is equivalent to RH, both directions compiled, the clause the reduction locates; it is open, and neither side is established.',
  UNI, 'h2_sign ↔ RiemannHypothesis', bright(EACH + ' (RiemannHypothesis)', EULER % 'ζ’s explicit formula with its prime sum (EF_lit_zetaZeroConfig)', None, UNI,
                                             FACE_OK % 'ζ'),
  [F(EF + 'B321.h2_sign_iff_rh', 'v0.2', P_ZETA), F(EF + 'Schema.h2_sign_cfg_zeta_statement', 'v0.15', P_CHI)], ['b536', 'b573'])
R('RH-02', 'restatement',
  'The deposit’s Route 3 clause, the conservation hypothesis, is RH restated by a compiled lemma.',
  UNI, 'conservationHypothesis ↔ RiemannHypothesis', T((1, 'PASS', EACH + ' (RiemannHypothesis)'), (2, 'FAIL', RESTATE)),
  [F(EF + 'B321.ch_iff_rh', 'v0.1', P_ZETA)], ['b534'])
R('RH-03', 'prime-side control',
  'The explicit formula holds at ζ’s zero configuration, the literature formula vendored and compiled.',
  UNI, 'EF_lit zetaZeroConfig (∀ test function in the class)', T((1, 'FAIL', IDAGG)),
  [F('Zeta23.WeilEF.EF_lit_zetaZeroConfig', 'v0.1', P_ZETA)], ['b495', 'b534'])
R('RH-04', 'crossing geometry',
  'Weil positivity is equivalent to its finite-support rungs holding at every support length.',
  UNI, 'h2_sign ↔ ∀ L₀, h2_sign_upto L₀', bright(EACH + ' (through h2_sign_iff_rh)', EULER % 'the prime sum in every rung', None, LADDER, FACE_OK % 'ζ'),
  [F(EF + 'B321.h2_sign_iff_forall_upto', 'v0.3', P_ZETA)], ['b560'])
R('RH-05', 'crossing geometry',
  'Every finite-support rung holding is equivalent to RH.',
  UNI, '(∀ L₀, h2_sign_upto L₀) ↔ RiemannHypothesis', bright(EACH + ' (RiemannHypothesis)', EULER % 'the prime sum in every rung', None, LADDER, FACE_OK % 'ζ'),
  [F(EF + 'B321.forall_upto_iff_rh', 'v0.3', P_ZETA)], ['b560'])
R('RH-06', 'the Li ladder',
  'For every n, the arithmetic limit of the symmetric test members converges to λ_n, the Li–Weil bridge.',
  'LIMIT', '∀ n, Filter.Tendsto (δ ↦ literatureRHS (symMember n δ)) (𝓝[>] 0) (𝓝 (LiCoeff n))', T((1, 'FAIL', AGG % 'λ_n for each n')),
  [F(EF + 'LiWeil.li_identity_sym', 'v0.7', P_ZETA)], ['b563'])
R('RH-07', 'the Li ladder',
  'λ_n ≥ 0 for every n is equivalent to RH (Li’s criterion), both directions compiled, the converse vendored.',
  UNI, '(∀ n, 0 ≤ LiCoeff n) ↔ RiemannHypothesis', T((1, 'PASS', EACH + ' (RiemannHypothesis)'), (2, 'FAIL', ZEROSIDE)),
  [F(EF + 'LiCriterionBridge.li_nonneg_iff_rh', 'v0.9', P_ZETA), F(EF + 'LiWeil.rh_imp_li_nonneg', 'v0.4', P_ZETA, 'plumbing'),
   F(EF + 'LiCriterionBridge.li_coeff_eq_taylorCoeff', 'v0.9', P_ZETA, 'plumbing'), F('LiCriterion.positivity_implies_RH', 'v0.9', P_ZETA, 'plumbing')],
  ['b560', 'b566'])
R('RH-08', 'the Li ladder',
  'RH is equivalent to the nonnegativity of the Bombieri–Lagarias arithmetic limits.',
  UNI, '(∀ n, 0 ≤ arithmetic limit n) ↔ RiemannHypothesis',
  bright(EACH + ' (RiemannHypothesis)', EULER % 'the explicit formula’s prime side through the Li–Weil bridge', None, LADDER + ' (the λ_n)', FACE_OK % 'ζ'),
  [F(EF + 'LiCriterionBridge.arith_limit_nonneg_iff_rh', 'v0.9', P_ZETA)], ['b566'])
R('RH-09', 'the Li ladder',
  'The register-4 positivity at λ := LiCoeff is equivalent to RH.',
  UNI, 'Register4_positivity LiCoeff ↔ RiemannHypothesis', T((1, 'PASS', EACH + ' (RiemannHypothesis)'), (2, 'FAIL', ZEROSIDE)),
  [F(EF + 'PageConverses.register4_positivity_liCoeff_iff_rh', 'v0.11', P_ZETA),
   F(EF + 'ResidueDischarge.register4_positivity_liCoeff_imp_rh', 'v0.10', P_ZETA, 'plumbing')], ['b567', 'b569'])
R('RH-10', 'the Li ladder',
  'Nonnegativity of ξ’s Taylor coefficients in the Li expansion is equivalent to RH.',
  UNI, '(∀ n, 0 ≤ (taylorCoeff riemannXi n).re) ↔ RiemannHypothesis', T((1, 'PASS', EACH + ' (RiemannHypothesis)'), (2, 'FAIL', ZEROSIDE)),
  [F(EF + 'PageConverses.taylorCoeff_nonneg_iff_rh', 'v0.11', P_ZETA)], ['b569'])
R('RH-11', 'the Li ladder',
  'Keiper’s Taylor identity for the Li coefficients follows from named obligations, none discharged.',
  UNI, 'KeiperObligations → KeiperTaylorIdentity (∀ n)', T((1, 'FAIL', IDAGG)),
  [F(EF + 'Keiper.keiperTaylorIdentity_of', 'v0.19', P_ZETA), F(EF + 'Keiper.keiperTaylor_zero', 'v0.19', P_ZETA, 'plumbing')], ['b601'])
R('RH-12', 'the Li ladder',
  'λ₁ = 1 + γ/2 − ½ log 4π.',
  'FINITE', 'LiCoeff 1 = 1 + γ/2 − ½ log 4π', T((1, 'FAIL', AGG % 'λ₁')),
  [F(EF + 'Keiper.liCoeff_one_keiper', 'v0.19', P_ZETA)], ['b601'])
R('RH-13', 'the Li ladder',
  'λ₁ > 0, compiled with no premise.',
  'FINITE', '0 < LiCoeff 1', T((1, 'FAIL', AGG % 'λ₁, one rung')),
  [F(EF + 'KeiperSign.liCoeff_one_pos', 'v0.20', P_ZETA), F(EF + 'KeiperSign.liCoeff_one_pos_iff', 'v0.20', P_ZETA, 'plumbing'),
   F(EF + 'KeiperSign.threshold_lt_gamma', 'v0.20', P_ZETA, 'plumbing')], ['b602'])
R('RH-14', 'the Li ladder',
  'The Keiper bounds follow from named bound premises.',
  'FINITE', 'BoundPremises → KeiperBounds', T((1, 'FAIL', AGG % 'finitely many Stieltjes and ζ values')),
  [F(EF + 'KeiperBounds.keiperBounds_of', 'v0.19', P_ZETA)], ['b601'])
R('RH-15', 'multiplicity',
  'Simplicity of ζ’s configuration is every nontrivial zero of multiplicity one, a Prop beside the faces.',
  UNI, 'simplicity ↔ ∀ ρ, IsNontrivialZero ρ → zeroMult ρ = 1', T((1, 'FAIL', MULT)),
  [F(EF + 'Simplicity.simplicity_iff', 'v0.17', P_ZETA)], ['b596'])
R('RH-16', 'the 0.6725 ceiling',
  'Under the two-thirds proportion premise, the zeros of a dyadic window not simple and on the line are at most a third plus ε of them.',
  'DENSITY', 'SimpleProportion → ∀ ε > 0, ∃ T₀, ∀ T ≥ T₀, N − N₀simple ≤ (1/3 + ε)·N', T((1, 'FAIL', AGG % 'a proportion over a window')),
  [F(EF + 'Simplicity.exceptional_mass_le_third', 'v0.17', P_ZETA)], ['b596'])
R('RH-17', 'prime-side control',
  'Weil positivity of a sum of two configurations holds exactly when it holds for each.',
  'FAMILY', '∀ C₁ C₂, h2_sign_cfg (sum C₁ C₂) ↔ h2_sign_cfg C₁ ∧ h2_sign_cfg C₂', T((1, 'PASS', EACH + ' (the two targets)'), (2, 'FAIL', GENERIC)),
  [F(EF + 'Product.productLemma_holds', 'v0.18', P_ZETA), F(EF + 'Product.sum_ef', 'v0.18', P_ZETA, 'plumbing'),
   F(EF + 'Product.h2_sign_cfg_sum_iff_targets', 'v0.18', P_ZETA, 'plumbing')], ['b600'])
R('RH-18', 'multiplicity',
  'A configuration summed with itself doubles every multiplicity and leaves Weil positivity unchanged.',
  'FAMILY', '∀ C, (∀ ρ ∈ C, (sum C C).mult ρ = 2·C.mult ρ) ∧ (h2_sign_cfg (sum C C) ↔ h2_sign_cfg C)',
  T((1, 'PASS', EACH + ' (positivity on both sides)'), (2, 'FAIL', GENERIC)),
  [F(EF + 'Doubling.doubling_holds', 'v0.19', P_ZETA)], ['b601'])
R('RH-19', 'multiplicity',
  'Within the schema, Weil positivity does not imply simplicity.',
  'FAMILY', '¬ ∀ C, h2_sign_cfg C → allSimple C', T((1, 'FAIL', MULT)),
  [F(EF + 'Doubling.positivity_not_imp_simplicity', 'v0.19', P_ZETA)], ['b601'])
R('RH-20', 'prime-side control',
  'The explicit formula holds at every primitive χ ≠ 1.',
  'FAMILY', '∀ χ primitive, χ ≠ 1, EF_lit_chi χ', T((1, 'FAIL', IDAGG)),
  [F(EF + 'GRHWeil.EF_lit_chi_holds', 'v0.13', P_CHI), F(EF + 'GRHWeil.rectangle_identity_chi', 'v0.13', P_CHI, 'plumbing'),
   F(EF + 'GRHWeil.full_line_identity_chi', 'v0.13', P_CHI, 'plumbing')], ['b571'])
R('RH-21', 'prime-side control',
  'For each primitive χ ≠ 1, Weil positivity on classK for χ is equivalent to GRH_chi; neither side is established.',
  'FAMILY', '∀ χ primitive, χ ≠ 1, h2_sign_chi χ ↔ GRH_chi χ',
  bright(EACH + ' (GRH_chi)', EULER % 'L(s,χ)’s explicit formula with its prime sum (EF_lit_chi_holds)', 'one χ at its own conductor: log (N/π) once', FAM_U,
         FACE_OK % 'χ'),
  [F(EF + 'GRHWeil.h2_sign_chi_iff_grh_chi', 'v0.14', P_CHI), F(EF + 'Schema.h2_sign_cfg_chi_statement', 'v0.15', P_CHI),
   F(EF + 'GRHWeil.zeroSide_chi_eq', 'v0.14', P_CHI, 'plumbing'), F(EF + 'GRHWeil.grh_chi_imp_h2_sign_chi', 'v0.14', P_CHI, 'plumbing'),
   F(EF + 'GRHWeil.h2_sign_chi_imp_grh_chi', 'v0.14', P_CHI, 'plumbing')], ['b572', 'b573'])
R('RH-22', 'prime-side control',
  'For every configuration of the schema, Weil positivity is equivalent to its target, every point on the line.',
  'FAMILY', '∀ C, h2_sign_cfg C ↔ C.target', T((1, 'PASS', EACH + ' (the target)'), (2, 'FAIL', GENERIC)),
  [F(EF + 'Schema.h2_sign_cfg_iff_target', 'v0.15', P_CHI), F(EF + 'Schema.online_imp_h2_sign_cfg', 'v0.15', P_CHI, 'plumbing')], ['b573'])
R('RH-23', 'prime-side control',
  'Weil positivity of a finite sum of configurations holds exactly when it holds for every summand.',
  'FAMILY', '∀ s f, h2_sign_cfg (finsetSum s f) ↔ ∀ i ∈ s, h2_sign_cfg (f i)', T((1, 'PASS', EACH + ' (every summand’s target)'), (2, 'FAIL', GENERIC)),
  [F(EF + 'Schema.Family.finsetSum_productLemma', 'v0.21', P_CHI), F(EF + 'Schema.Family.finsetSum_insert', 'v0.21', 'chi-corr', 'plumbing')], ['b603'],
  note='the sum`s commutativity and associativity (sum_comm, sum_assoc) are plumbing of this row, on neither page')
R('RH-24', 'prime-side control',
  'Weil positivity of the summed configuration of the non-trivial characters mod q, each at its primitive inducer, holds exactly when GRH_chi holds for every one of them.',
  'FAMILY', '∀ q, h2_sign_cfg (familyConfig q) ↔ ∀ χ ∈ family q, GRH_chi χ.primitiveCharacter',
  bright(EACH + ' (GRH_chi for every member)', EULER % 'each member’s explicit formula with its prime sum', 'log (N/π) once per summand at its own conductor (familyConfig_arith)',
         FAM_U, FACE_OK % 'χ'),
  [F(EF + 'Schema.Family.family_theorem', 'v0.21', P_CHI), F(EF + 'Schema.Family.familyConfig_arith', 'v0.21', P_CHI, 'plumbing'),
   F(EF + 'Schema.Family.family_three', 'v0.21', P_CHI, 'plumbing')], ['b603'],
  note='family_three is the instance q = 3, carried in this row as plumbing of its face')
R('RH-25', 'crossing geometry',
  'Every off-line point of any configuration is met by a classK window on which the zero side is negative.',
  'FAMILY', '∀ C, ∀ ρ₀ ∈ C, ρ₀.re ≠ 1/2 → ∃ a j, classK window ∧ support bound ∧ zeroSide < 0',
  T((1, 'PASS', 'it names the off-line point’s real part'), (2, 'FAIL', GENERIC)),
  [F(EF + 'Schema.detector', 'v0.16', P_CHI)], ['b590'])
R('RH-26', 'crossing geometry',
  'A configuration with an off-line point is not Weil-positive.',
  'FAMILY', '∀ C, (∃ ρ ∈ C, ρ.re ≠ 1/2) → ¬ h2_sign_cfg C', T((1, 'PASS', 'it names the off-line point’s real part'), (2, 'FAIL', GENERIC)),
  [F(EF + 'Schema.not_h2_sign_cfg_of_offline', 'v0.16', 'chi-corr')], ['b590'])
R('RH-27', 'crossing geometry',
  'The plateau-ramp window lies in classK with its closed-form transform, carried on two named obligations.',
  'FAMILY', '∀ W h, 0 ≤ W → 0 < h → WindowObligations W h → PlateauRampWindow W h', T((1, 'FAIL', NOZERO % 'a window')),
  [F(EF + 'Schema.PlateauRamp.plateauRampWindow_of', 'v0.20', P_CHI)], ['b602'],
  note='the window`s evenness and support (window_even, window_hasCompactSupport) are plumbing of this row, on neither page')
# ### the readings the record carries that are not compiled (the author's answer): graded as readings
R('RH-28', 'multiplicity',
  'Multiplicity is carried as weight by each compiled face and constrained by none; simplicity stands beside the faces as its own Prop.',
  UNI, 'the sentence: every face’s zero sum weighted by mult; no face’s statement names it', T((1, 'FAIL', MULT)),
  [], ['b596'], grade='reading (the ζ page’s back-matter line, at its pin)')
R('RH-29', 'prime-side control',
  'Positivity is conjunctive over sums of configurations, so no part’s positivity is borrowed from another’s, and within the schema it does not imply simplicity.',
  'FAMILY', 'the sentence: every sum of configurations', T((1, 'PASS', EACH + ' (every part’s target)'), (2, 'FAIL', GENERIC)),
  [], ['b600', 'b601'], grade='reading (FINDINGS :6970)', strike='the author’s strike item')
R('RH-30', 'prime-side control',
  'The q-th cyclotomic field’s Dedekind zeta as the product over all characters mod q would need two premises the schema does not supply, both named and neither discharged.',
  'FAMILY', 'the sentence: every character mod q, imprimitive ones included',
  T((1, 'PASS', EACH + ' (every factor’s zeros)'), (2, 'PASS', EULER % 'each factor’s Euler product'),
    (3, 'FAIL', 'an imprimitive character enters at its level, not its conductor (EulerFactorPremise), and the trivial character with ζ’s pole term')),
  [], ['b603'], grade='reading (FINDINGS :7026; TrivialSummandPremise and EulerFactorPremise named at v0.21)', strike='the author’s strike item')
# ================================================================ SIMPLICITY / RH CASCADE -- the current version's own conclusions
R('RH-31', 'the identity and its terms',
  'File E states the finite-instance identity and does not establish it; its truth at complete roster is h2, which is open.',
  'FINITE', 'the sentence: one identity at a finite instance', T((1, 'FAIL', NOZERO % 'a trace and a ledger at a finite instance')),
  [G('FiniteInstanceIdentity', 24)], ['the file’s own', 'b163'], grade='INTERFACES-on-named-premise (row 24, sorry-count 0)')
R('RH-32', 'the identity and its terms',
  'The one recorded check of the identity at finite instance returned a stable nonzero difference at every cell, decomposed into three computed pieces, so the closure protocol’s step one is not triggered.',
  'FINITE', 'the sentence: every tested cell', T((1, 'FAIL', NOZERO % 'tested cells of the finite instance')),
  [], ['b38'], grade='computed at finite instance, cited at its own grade')
R('RH-33', 'the identity and its terms',
  'The identity’s archimedean term reaches the corpus through one reading, the E₁-apportioned part of the certified column, and that reading sits at the grade barrier.',
  'FINITE', 'the sentence: one route', T((1, 'FAIL', NOZERO % 'the archimedean term’s route')),
  [], ['b107'], grade='a reading at the grade barrier')
R('RH-34', 'the identity and its terms',
  'The apportionment admits a one-parameter family, and the void gate forces only its normalisation.',
  'FAMILY', 'the sentence: a one-parameter family of apportionments', T((1, 'FAIL', NOZERO % 'the apportionment family')),
  [G('ApportionmentShadow', 69)], ['b154'], grade='DERIVED, exact algebra')
R('RH-35', 'the identity and its terms',
  'The family’s freedom is physical, not gauge: at most one member admits the identity at a cell.',
  'FINITE', 'the sentence: at a cell', T((1, 'FAIL', NOZERO % 'the apportionment’s share at a cell')),
  [G('ShareDependenceShadow', 70)], ['b155'], grade='DERIVED, conditional on the reading at the grade barrier')
R('RH-36', 'the identity and its terms',
  'No owner-quotable requirement selects a member of the family.',
  'FINITE', 'the sentence: four candidate classes', T((1, 'FAIL', NOZERO % 'the owners’ requirements')),
  [G('RefinementArityShadow', 72)], ['b158'], grade='DERIVED (reads at owners)')
R('RH-37', 'the identity and its terms',
  'The last read-route is closed: the E₁/even bridge derives from banked ground and delivers only completeness, which the void gate already gives.',
  'FINITE', 'the sentence: one bridge', T((1, 'FAIL', NOZERO % 'the E₁/even bridge')),
  [G('SectorOccupancyShadow', 73)], ['b159'], grade='DERIVED')
R('RH-38', 'the identity and its terms',
  'The archimedean term is fixed only up to a definitional choice, and the choice is open.',
  'FAMILY', 'the sentence: the members of the family', T((1, 'FAIL', NOZERO % 'the archimedean term’s definition')),
  [], ['b154', 'b159'], grade='a consequence of the four rows above, a reading')
R('RH-39', 'the density and its channel',
  'The deviation’s whole window-dependence collapses to a fixed-kernel scale-average of one density carrying no window parameter.',
  UNI, 'the sentence: every window parameter', T((1, 'FAIL', NOZERO % 'a density over the window parameter')),
  [G('MechanismShadow', 68)], ['b115'], grade='DERIVED; verified at 2.91e−16 against the instrument’s values')
R('RH-40', 'the density and its channel',
  'The kernel is mean-zero with one sign change, so a monotone Ψ would make the balanced window unique, and that antecedent is not verified.',
  UNI, 'the sentence: Ψ monotone over the window parameter', T((1, 'FAIL', NOZERO % 'the kernel and Ψ')),
  [], ['b116'], grade='DERIVED, longhand; no terminal')
R('RH-41', 'the density and its channel',
  'The density lane’s reduction was derived from one member of the apportionment family, so its chain is conditional on that member.',
  'FINITE', 'the sentence: one dependence', T((1, 'FAIL', NOZERO % 'the lane’s scope')),
  [], ['b163'], grade='a scope location by the findings pass, not a re-grade')
R('RH-42', 'the boundary',
  'No boundary license derives: every routed candidate was a reading, and the license needs a construction.',
  UNI, 'the sentence: no amount of further reading', T((1, 'FAIL', NOZERO % 'a license at the carrier’s edge')),
  [], ['b151'], grade='a refusal; no terminal')
R('RH-43', 'the density and its channel',
  'The mechanism’s remainder is open, priced at quantitative control of Ψ’s profile through two functionals, its engineering head an ε-extension at 7.389× the validated cap.',
  'FINITE', 'the sentence: one open with its price', T((1, 'FAIL', NOZERO % 'Ψ’s profile')),
  [], ['b121', 'b142'], grade='open, priced')
R('RH-44', 'the boundary',
  'The unlicensed boundary is open and wants a construction reaching the carrier’s edge.',
  'FINITE', 'the sentence: one open', T((1, 'FAIL', NOZERO % 'the carrier’s edge')),
  [], ['b151'], grade='open, a type and not a quantity')
R('RH-45', 'the identity and its terms',
  'Route A, fixing a member by principle, is open and is the author’s ruling to make.',
  'FINITE', 'the sentence: one route', T((1, 'FAIL', NOZERO % 'the member’s choice')),
  [], ['b158', 'b159'], grade='open, a ruling')
R('RH-46', 'the identity and its terms',
  'Route B, defining the residual’s split and then measuring it, wants the author’s ruling first, since the split is undefined at owner grade.',
  'FINITE', 'the sentence: one route', T((1, 'FAIL', NOZERO % 'the residual’s split')),
  [], ['b158', 'b159'], grade='open, a ruling')
R('RH-47', 'the density and its channel',
  'The balanced window’s location is banked at zero weight, and the recorded crossing near a² ∼ 10 carries no interpretive weight.',
  'FINITE', 'the sentence: one location, one crossing', T((1, 'FAIL', NOZERO % 'the bench’s window parameter')),
  [], ['b163'], grade='a fence')
R('RH-48', 'the identity and its terms',
  'μ is a bench parameter: the record supplies no route for it to enter at complete roster, which is not to say it cannot.',
  'FINITE', 'the sentence: the record’s routes', T((1, 'FAIL', NOZERO % 'a bench parameter')),
  [], ['b191'], grade='a reach note; it re-grades nothing')
R('RH-49', 'the density and its channel',
  'The bench lane’s bearing is explicitly disclaimed: no relation was inferred, constructed or proposed.',
  'FINITE', 'the sentence: one reading', T((1, 'FAIL', NOZERO % 'the bench lane')),
  [], ['b192'], grade='verdict, EXPLICITLY DISCLAIMED')
R('RH-50', 'the archimedean place',
  'The strongest finite-place result does not establish nonvanishing: the finite tail closes and one place, the archimedean, remains.',
  'FINITE', 'the sentence: the finite places and one more', T((1, 'FAIL', NOZERO % 'nonvanishing at the places')),
  [], ['b198'], grade='a read, and a build the read licensed')
R('RH-51', 'the archimedean place',
  'The space is above bench and the split is on the bench; no archimedean value is derived.',
  'FINITE', 'the sentence: one space, one split', T((1, 'FAIL', NOZERO % 'the archimedean place’s space')),
  [], ['b199', 'b201'], grade='a read; no build, as a verdict')
R('RH-52', 'the archimedean place',
  'One sector name was carrying three objects, named the Sonin, the constraint and the compression sectors.',
  'FINITE', 'the sentence: a census of one name', T((1, 'FAIL', NOZERO % 'a name’s objects')),
  [], ['b200', 'b206'], grade='reads and one verdict')
R('RH-53', 'the archimedean place',
  'Both values of c occur at τ = 2π, so the Sonin sector is nonzero at bench grade and no higher; no element is named as the +1 one.',
  'FINITE', 'the sentence: six eigenvalues at three resolutions', T((1, 'FAIL', NOZERO % 'eigenfunction signs at the archimedean place')),
  [G('AlternationShadow', 83)], ['b201', 'b207'], grade='BENCH; the alternation’s two core statements compiled')
R('RH-54', 'the identity and its terms',
  'Term 2’s debt is to write the formalization at all: no file D exists, and the class-richness lemma is carried at cite.',
  'FINITE', 'the sentence: 47 trees, 9,584 files', T((1, 'FAIL', NOZERO % 'a missing formalization')),
  [G('QuotientLemmaShadow', 4)], ['b189'], grade='an absence bounded by its enumerated scope')
R('RH-55', 'the archimedean place',
  'The witness enumeration closed at six sites, 82 candidates and eleven failure kinds, and the archimedean channel is twice the Riemann–Siegel θ′, its sign change at θ’s minimum.',
  'FINITE', 'the sentence: six sites, 82 candidates, 0 ≤ t ≤ 50', T((1, 'FAIL', NOZERO % 'the archimedean channel')),
  [], ['b433', 'b443', 'b444'], grade='a verified source’s statement at K5; enumeration')
R('RH-56', 'prime-side control',
  'The chain’s residual traces to its integration, and at its one outlier to the prime channel alone.',
  'FINITE', 'the sentence: one outlier', T((1, 'FAIL', AGG % 'the prime channel’s growth at one width')),
  [], ['b445', 'b452', 'b453'], grade='bench')
R('RH-57', 'crossing geometry',
  'The instrument’s margin was charted cell by cell on one transform, and the control did not close until its own zero bank was completed, thirty zeros short, every one off the line.',
  'FINITE', 'the sentence: a chart of cells', T((1, 'FAIL', AGG % 'each cell’s value at one window')),
  [], ['b487', 'b506', 'b507'], grade='bench')
# ================================================================ FOUNDATIONS
R('FD-01', 'the Epstein witnesses',
  'Under the Epstein premises, a configuration carrying the off-line Epstein point ρ_E is not Weil-positive.',
  'FAMILY', '∀ Z rhs, EpsteinPremises Z rhs → ρ_E ∈ Z.carrier → ¬ h2_sign_cfg ⟨Z, rhs⟩',
  T((1, 'PASS', 'it names ρ_E’s real part'), (2, 'FAIL', GENERIC + ': it is that configuration')),
  [F(EF + 'Schema.epstein_not_h2_sign_cfg', 'v0.16', 'chi-corr')], ['b590'], grade='INTERFACES on EpsteinPremises')
R('FD-02', 'the Epstein witnesses',
  'Under the Epstein premises, the Epstein configuration’s explicit formula holds at the plateau-ramp window.',
  'FAMILY', '∀ Z rhs, EpsteinPremises Z rhs → ∀ W h, WindowObligations W h → ∀ p ≥ 6, zero sum = rhs', T((1, 'FAIL', IDAGG)),
  [F(EF + 'Schema.PlateauRamp.epstein_ef_at_window', 'v0.20', P_CHI)], ['b602'])
R('FD-03', 'the record',
  'The kernel, used to build, twice closed a statement the corpus had carried open, and a sentence of the barrier keystone was found unable to carry the weight its lemma’s applications put on it.',
  'FINITE', 'the sentence: an arc of nine acts', T((1, 'FAIL', NOZERO % 'the corpus’s barrier keystone')),
  [], ['b413', 'b421', 'b422'], grade='the arc’s one statement; the keystone’s Definition 2.1 carries the author’s ruling at its §10.2')
# ================================================================ METHODOLOGY
R('MT-01', 'the record',
  'The Core terminals print zero-axiom, 614 printed lines and every one zero-axiom, and each is a finite instance, not a theorem at complete roster.',
  'FINITE', 'the sentence: 614 printed lines', T((1, 'FAIL', NOZERO % 'the Core terminals’ prints')),
  [], ['b163', 'b208', 'b604'], grade='counted at content: AXIOM_PRINTS.txt at SIDE-global-section %s' % GS_PIN)
R('MT-02', 'the record',
  'Five Mathlib-facing files are declared interfaces at the classical profile, never load-bearing for the programme’s own claims.',
  'FINITE', 'the sentence: five files', T((1, 'FAIL', NOZERO % 'interface files')),
  [], ['b163'], grade='declared; AXIOM_PRINTS_INTERFACES.txt at SIDE-global-section %s' % GS_PIN)
R('MT-03', 'the record',
  'Every analytic derivation, every bench measurement and the identity itself are not machine-verified: the derivations are checkable by reading and the numbers by re-running.',
  'FINITE', 'the sentence: the record’s derivations and measurements', T((1, 'FAIL', NOZERO % 'what is checked how')),
  [], ['b163'], grade='a statement of scope')
R('MT-04', 'the towers, the junction and the plane',
  'The coherence premise’s finite part is decided true of the built object, and the premise retires to its residue, the one firewall identification H-COH-∞.',
  'FINITE', 'the sentence: the finite part', T((1, 'FAIL', NOZERO % 'the adelic plane')),
  [G('AdelicPlaneShadow', 53)], ['b75'], grade='decided property')
R('MT-05', 'the record',
  'The two priced opens neither block nor are blocked by the locks.',
  'FINITE', 'the sentence: two opens, the locks', T((1, 'FAIL', NOZERO % 'what blocks what')),
  [], ['b163'], grade='a statement of what blocks what')
R('MT-06', 'the towers, the junction and the plane',
  'The towers and the junction were decided independent of the identity and the density, with no shared object and no derivational contact.',
  'FINITE', 'the sentence: one pair decided', T((1, 'FAIL', NOZERO % 'cross-place structure')),
  [], ['b163'], grade='a verdict of the findings pass')
R('MT-07', 'the record',
  'This document is written by the seat it describes, unreviewed, and claims neither soundness nor completeness; where it and a founding act disagree, the act wins.',
  'FINITE', 'the sentence: one document', T((1, 'FAIL', NOZERO % 'the document')),
  [], ['b163', 'b208'], grade='a limit')
R('MT-08', 'the record',
  'The findings pass decided every plausibly touching pair at content, refused one unifying statement as the register sentence, decided five of seven pairs independent and found one dependence.',
  'FINITE', 'the sentence: seven objects, their pairs', T((1, 'FAIL', NOZERO % 'the findings pass')),
  [], ['b163'], grade='the pass’s own record')
R('MT-09', 'the record',
  'The fold of the in-flight register lists thirteen live items with their obstacles in the owning acts’ words, the count reconciling over that register and no wider.',
  'FINITE', 'the sentence: thirteen items', T((1, 'FAIL', NOZERO % 'the register’s items')),
  [], ['b208'], grade='a fold, counted')
R('MT-10', 'the record',
  'The register and the owning act disagree on the dominance second asking, and the disagreement is printed for the author rather than resolved.',
  'FINITE', 'the sentence: one item', T((1, 'FAIL', NOZERO % 'two ledgers')),
  [], ['b168', 'b182', 'b208'], grade='a divergence, not resolved')
R('MT-11', 'the towers, the junction and the plane',
  'The identity consumes values, not the assembled object; von Neumann’s C₀ condition constrains norms only; the archimedean value is undetermined, and applicability is undecided.',
  'FINITE', 'the sentence: two values, one condition', T((1, 'FAIL', NOZERO % 'the assembly and its values')),
  [], ['b196', 'b197'], grade='reads and one verdict each; no Lean')
R('MT-12', 'the towers, the junction and the plane',
  'Term 3, the assembly, gained no route and nothing was constructed; a nonzero Sonin sector at bench grade is not a held unit.',
  'FINITE', 'the sentence: one assembly', T((1, 'FAIL', NOZERO % 'the restricted tensor product')),
  [], ['b195', 'b207'], grade='a live debt')
R('MT-13', 'the record',
  'Neither live debt is blocked on μ: term 2 wants a formalization written and term 3 an object constructed.',
  'FINITE', 'the sentence: two debts', T((1, 'FAIL', NOZERO % 'what blocks what')),
  [], ['b191', 'b208'], grade='a statement of what blocks what, not a re-grade')
R('MT-14', 'the record',
  'Ten of the twelve arcs folded in that span carry no one-statement, the convention post-dating them, and nothing is summarised in their place.',
  'FINITE', 'the sentence: twelve arcs', T((1, 'FAIL', NOZERO % 'the folds')),
  [], ['b412'], grade='a fold refresh')
R('MT-15', 'the record',
  'An eight-act sequence re-derived a standard the corpus had already ruled and did not cite it once.',
  'FINITE', 'the sentence: eight acts', T((1, 'FAIL', NOZERO % 'the record’s acts')), [], ['b371', 'b383', 'b384'], grade='the arc’s one statement')
R('MT-16', 'the record',
  'In nine of seventeen acts a limit, count, absence or version on the record was an artefact of its measurement, and in the four mathematical acts the limit was real.',
  'FINITE', 'the sentence: seventeen acts', T((1, 'FAIL', NOZERO % 'the record’s measurements')), [], ['b385', 'b401', 'b402'], grade='the arc’s one statement')
R('MT-17', 'the record',
  'In every act of the classification arc the work decided what kind of thing something is before asking what follows, and in seven of nine the answer changed what could be concluded.',
  'FINITE', 'the sentence: nine acts', T((1, 'FAIL', NOZERO % 'the record’s classifications')), [], ['b403', 'b411', 'b412'], grade='the arc’s one statement')
R('MT-18', 'the record',
  'The grading discipline, turned outward, held, and the same protocol turned inward found the corpus’s prose claiming more than its terminal compiles.',
  'FINITE', 'the sentence: one arc', T((1, 'FAIL', NOZERO % 'the grading discipline')), [], ['b423', 'b432', 'b434'], grade='the arc’s one statement')
R('MT-19', 'the record',
  'An instrument that had reported every act passing had never been asked to fail by its own rule, and eight deposited sentences asserting a machine check point at nothing.',
  'FINITE', 'the sentence: one instrument, eight sentences', T((1, 'FAIL', NOZERO % 'an instrument and the deposit')), [], ['b454', 'b462', 'b463'], grade='the arc’s one statement')
R('MT-20', 'the record',
  'Every outward reading came back about the reading: the concordance rows no machine-check sentence, a uniformity sits in a coordinate no source fires, and the third party’s formula contains the instrument’s identity.',
  'FINITE', 'the sentence: one arc of readings', T((1, 'FAIL', NOZERO % 'readings of other hands')), [], ['b464', 'b473', 'b474'], grade='the arc’s one statement')
R('MT-21', 'the record',
  'In the bookkeeping arc the span’s mathematics moved little and its bookkeeping a great deal.',
  'FINITE', 'the sentence: one span', T((1, 'FAIL', NOZERO % 'the bookkeeping')), [], ['b475', 'b485', 'b486'], grade='the arc’s one statement, quoted from its trail record')
R('MT-22', 'the record',
  'Every over-ceiling claim the editions corrected was a true finite fact carrying the name of the open obligation on all zeros, and an edition separates the counted object from the open clause.',
  'FINITE', 'the sentence: the editions’ corrections', T((1, 'FAIL', NOZERO % 'the editions’ corrections')),
  [], ['b588'], grade='reading (THE_METHOD_CANON §XX, the census / totality pair)', strike='the navigator’s draft, struck if the author words it')
# ================================================================ CUBIT / TRIVIUM and MATTER / COSMOLOGY
R('CT-01', 'the codes and the substrate',
  'The codes and the substrate were decided independent of the identity and the density, with no shared object.',
  'FINITE', 'the sentence: one pair decided', T((1, 'FAIL', NOZERO % 'the Steane/Fano labelling')),
  [], ['b163'], grade='a verdict of the findings pass; SIDE-substrate-cluster, off the summit path')
R('MC-01', 'the constants and the empirical layer',
  'The constants and the empirical layer were decided independent of the identity and the density, with no derivational contact.',
  'FINITE', 'the sentence: one pair decided', T((1, 'FAIL', NOZERO % 'Ω_b, ΔH₀ and α_t')),
  [], ['b163'], grade='a verdict of the findings pass; empirically anchored tags, not kernels')

# ### the current version's conclusions (CV), each with its lines, the row it lands in and how. 'own': the row is its
# ### conclusion re-read as it stands; 'restates': a sentence restating that row's conclusion; 'superseded': a conclusion a
# ### later compiled row supersedes, carried as a history line beneath that row's table. Exactly one row each (H38c).
CV = [
    ('c01', 12, 13, 'the governing claim', 'RH-01', 'superseded'),
    ('c02', 15, 15, 'the single clause is h2', 'RH-01', 'restates'),
    ('c03', 16, 16, 'h2 is not proved', 'RH-01', 'restates'),
    ('c04', 16, 18, 'the identity stated in a kernel file that does not prove it', 'RH-31', 'restates'),
    ('c05', 18, 20, 'the closure protocol’s step one not triggered', 'RH-32', 'restates'),
    ('c06', 33, 35, 'unreviewed; where this document and an act disagree, the act wins', 'MT-07', 'restates'),
    ('c07', 43, 54, 'the Core terminals print zero-axiom; each a finite instance', 'MT-01', 'own'),
    ('c08', 55, 57, 'the declared interfaces', 'MT-02', 'own'),
    ('c09', 58, 60, 'what is not machine-verified', 'MT-03', 'own'),
    ('c10', 66, 70, 'file E states the identity, does not prove it', 'RH-31', 'own'),
    ('c11', 72, 76, '(I-differ) at every cell; step one not triggered', 'RH-32', 'own'),
    ('c12', 82, 84, 'one route, at the grade barrier', 'RH-33', 'own'),
    ('c13', 86, 90, 'the one-parameter family; the void gate', 'RH-34', 'own'),
    ('c14', 92, 96, 'the freedom physical', 'RH-35', 'own'),
    ('c15', 98, 101, 'no owner-quotable requirement selects', 'RH-36', 'own'),
    ('c16', 103, 106, 'the last read-route closed', 'RH-37', 'own'),
    ('c17', 108, 109, 'fixed only up to a definitional choice', 'RH-38', 'own'),
    ('c18', 115, 120, 'the collapse to one density', 'RH-39', 'own'),
    ('c19', 122, 126, 'the mean-zero kernel; the sufficient condition', 'RH-40', 'own'),
    ('c20', 128, 133, 'the chain conditional on one member', 'RH-41', 'own'),
    ('c21', 139, 145, 'the coherence premise’s finite part decided', 'MT-04', 'own'),
    ('c22', 151, 156, 'no boundary license derives', 'RH-42', 'own'),
    ('c23', 164, 164, 'the mechanism’s remainder, priced', 'RH-43', 'own'),
    ('c24', 165, 165, 'the unlicensed boundary', 'RH-44', 'own'),
    ('c25', 166, 166, 'Route A', 'RH-45', 'own'),
    ('c26', 167, 167, 'Route B', 'RH-46', 'own'),
    ('c27', 169, 169, 'the priced opens and the locks', 'MT-05', 'own'),
    ('c28', 175, 177, 'the towers and the junction INDEPENDENT', 'MT-06', 'own'),
    ('c29', 175, 177, 'the codes and the substrate INDEPENDENT', 'CT-01', 'own'),
    ('c30', 175, 177, 'the constants and the empirical layer INDEPENDENT', 'MC-01', 'own'),
    ('c31', 185, 189, 'this document’s limits', 'MT-07', 'own'),
    ('c32', 191, 195, 'what it can claim: the findings pass', 'MT-08', 'own'),
    ('c33', 197, 201, 'the fences', 'RH-47', 'own'),
    ('c34', 205, 232, 'the fold: thirteen live items', 'MT-09', 'own'),
    ('c35', 234, 250, 'the divergence, item 5', 'MT-10', 'own'),
    ('c36', 252, 259, 'the join: the ε extension and the Mellin route', 'RH-43', 'restates'),
    ('c37', 261, 285, 'the fold’s completeness, counted', 'MT-09', 'restates'),
    ('c38', 296, 305, '(1) μ’s reach', 'RH-48', 'own'),
    ('c39', 307, 315, '(2) the bench lane’s bearing', 'RH-49', 'own'),
    ('c40', 317, 330, '(3) the assembly’s role, the values’ debt', 'MT-11', 'own'),
    ('c41', 332, 340, '(4) the finite places', 'RH-50', 'own'),
    ('c42', 342, 349, '(5) the space above bench', 'RH-51', 'own'),
    ('c43', 351, 359, '(6) the three objects the sector name covered', 'RH-52', 'own'),
    ('c44', 361, 377, '(7) the sign chain and its alternation', 'RH-53', 'own'),
    ('c45', 381, 388, 'term 3, the assembly', 'MT-12', 'own'),
    ('c46', 390, 398, 'term 2, the absent formalization', 'RH-54', 'own'),
    ('c47', 400, 406, 'neither debt blocked on μ', 'MT-13', 'own'),
    ('c48', 417, 428, 'ten arcs with no one-statement', 'MT-14', 'own'),
    ('c49', 429, 429, 'the re-derivation arc', 'MT-15', 'own'),
    ('c50', 430, 430, 'the artefact arc', 'MT-16', 'own'),
    ('c51', 431, 431, 'the classification arc', 'MT-17', 'own'),
    ('c52', 433, 433, 'the governing claim unchanged', 'RH-01', 'restates'),
    ('c53', 437, 437, 'the kernel arc', 'FD-03', 'own'),
    ('c54', 443, 443, 'the external-grading arc', 'MT-18', 'own'),
    ('c55', 444, 444, 'the witness and channel arc', 'RH-55', 'own'),
    ('c56', 446, 446, 'the governing claim unchanged', 'RH-01', 'restates'),
    ('c57', 452, 452, 'the residue and reconciliation arc', 'RH-56', 'own'),
    ('c58', 454, 454, 'the governing claim unchanged', 'RH-01', 'restates'),
    ('c59', 460, 460, 'the deposit-and-instrument arc', 'MT-19', 'own'),
    ('c60', 462, 462, 'the governing claim unchanged; the object column empty', 'RH-01', 'restates'),
    ('c61', 468, 468, 'the external-reading arc', 'MT-20', 'own'),
    ('c62', 470, 470, 'the governing claim unchanged; the object column empty', 'RH-01', 'restates'),
    ('c63', 476, 476, 'the bookkeeping arc', 'MT-21', 'own'),
    ('c64', 477, 477, 'the margin and its control arc', 'RH-57', 'own'),
    ('c65', 479, 479, 'the governing claim unchanged', 'RH-01', 'restates'),
    ('c66', 485, 485, 'the chain and the window arc', 'RH-25', 'superseded'),
    ('c67', 487, 487, 'the governing claim unchanged', 'RH-01', 'restates'),
    ('c68', 493, 493, 'the witness arc', 'FD-01', 'superseded'),
    ('c69', 495, 495, 'the governing claim unchanged; a witness on a control function', 'RH-01', 'restates'),
    ('c70', 497, 497, 'the instances differ (the order-7 B-spline, the smooth bump)', 'RH-27', 'superseded'),
    ('c71', 503, 503, 'the Weil converse arc', 'RH-01', 'superseded'),
    ('c72', 505, 505, 'the object column empty; the ceiling as (R145)(2) words it', 'RH-01', 'restates'),
]

# ### the current version's dated entries, each carried verbatim beneath the table it fed (the author's answer): (first line,
# ### last line, the table, what it is, the rows it fed). The class lines feed no table and are carried in the back matter.
DATED = [
    (45, 52, 'MT', 'the currency mark of 2026-08-26', ['MT-01']),
    (205, 286, 'MT', '§9, added 2026-08-26 -- the fold', ['MT-09', 'MT-10', 'RH-43']),
    (289, 294, 'MT', '§10’s heading and its dated opening, added 2026-08-26', []),
    (296, 315, 'RH', '§10 (1)-(2), added 2026-08-26', ['RH-48', 'RH-49']),
    (317, 330, 'MT', '§10 (3), added 2026-08-26', ['MT-11']),
    (332, 377, 'RH', '§10 (4)-(7), added 2026-08-26', ['RH-50', 'RH-51', 'RH-52', 'RH-53']),
    (379, 388, 'MT', '§10, the two live debts: term 3', ['MT-12']),
    (390, 398, 'RH', '§10, term 2', ['RH-54']),
    (400, 406, 'MT', '§10, the fact about both debts', ['MT-13']),
    (413, 433, 'MT', 'the orientation refresh filed 2026-09-10', ['MT-14', 'MT-15', 'MT-16', 'MT-17', 'RH-01']),
    (435, 437, 'FD', 'the orientation refresh filed 2026-09-11', ['FD-03']),
    (439, 446, 'MT', 'the orientation refresh filed 2026-09-12', ['MT-18', 'RH-55', 'RH-01']),
    (448, 454, 'RH', 'the orientation refresh filed 2026-09-14', ['RH-56', 'RH-01']),
    (456, 462, 'MT', 'the orientation refresh filed 2026-09-21', ['MT-19', 'RH-01']),
    (464, 470, 'MT', 'the orientation refresh filed 2026-09-22', ['MT-20', 'RH-01']),
    (472, 479, 'MT', 'the orientation refresh filed 2026-09-24 (the margin arc and the bookkeeping arc)', ['MT-21', 'RH-57', 'RH-01']),
    (481, 487, 'RH', 'the orientation refresh filed 2026-09-24 (the chain and the window arc)', ['RH-25', 'RH-01']),
    (489, 495, 'FD', 'the orientation refresh filed 2026-09-25 (the witness arc)', ['FD-01', 'RH-01']),
    (497, 497, 'RH', 'the line appended beside the 2026-09-25 refresh', ['RH-27']),
    (499, 505, 'RH', 'the orientation refresh filed 2026-09-25 (the Weil converse arc)', ['RH-01']),
]
CLASS_LINES = (3, 9)   # the class declarations and the built line, dated, feeding no table: carried in the back matter

# ### the three bright registers H38d names, and the cluster ids that carry rows
BRIGHT_REGISTERS = ('prime-side control', 'the Li ladder', 'crossing geometry')


def verdict(row):
    fails = [t for t in row['tests'] if t['r'] == 'FAIL']
    return ('DARK', fails[0]['n']) if fails else ('BRIGHT', None)
