# -*- coding: utf-8 -*-
"""b615_claims.py -- THE ACT'S DATA AND ITS RESOLVERS, UNDER (R225)(5): THE CLAIMS OF CLUSTER 2F'S THREE PAPERS.

### Every claim is the seat's one-sentence restatement of a paper's sentence, carried with a needle that must occur on the cited line of the
### paper at PLACE-papers f22a13a; its grade is the one the paper's own text supports, in the vocabulary of (R19) as (R220)(5) lists it:
### kernel-verified at a pin; theorem-supported; argument-supported; computationally-verified; synthesis-suggested; statement-grade.
### THE GRADING RULE, confirmed by (R222)(1): kernel-verified only where the paper names a terminal (or its file) at a pin and the
### statement read at that pin carries the claim; theorem-supported only where the paper names a theorem of the literature for it;
### computationally-verified only where the paper reports a computation; argument-supported where the paper's text argues the claim;
### synthesis-suggested where it reads a pattern across results; statement-grade where it states without argument. No grade is above the
### paper's own support. A ROUTE is a claim offered as an argument toward RH, simplicity or the open clause; each is read through the
### sieve's five tests in order. A pin RESOLVES, by the rule (R223)(1) confirms, when its commit is in the clone and at the remote.
### THE LOAD-BEARING CLAUSE, (R225)(2): a kernel-verified row is load-bearing when the statement read at its pin is a claim the
### document's head makes about the head's objects; rows certifying definitions, arithmetic over the papers' own tuples, or placeholders
### bearing no claim the thesis makes are not, and the tier reads KC only when one row is.
### BSD_TRANSFER :198 names TECHNE once; the row carries a pointer alone (the sha256 of TECHNE-Core's tracked-file manifest).
### THE REMOTE READS, (R225)(4): every ls-remote this module makes is counted per repository in LSR, which the suite prints.
### This module writes nothing: `python tools/b615_claims.py` runs the resolvers and prints.
"""
import hashlib
import math
import os
import re
import subprocess
import sys
from fractions import Fraction as Fr

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
PRE_PP = 'f22a13a'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PAPERS = {
    'ZS': ('phase2/empirical/ZERO_SIMPLICITY.md', 'p2-6', 293),
    'BT': ('phase2/empirical/BSD_TRANSFER.md', 'p2-11', 294),
    'BV': ('phase2/empirical/BSD_VIA_FORMATION_TRANSFER.md', 'p2-29', 295),
}
GRADES = ('kernel-verified', 'theorem-supported', 'argument-supported', 'computationally-verified', 'synthesis-suggested', 'statement-grade')
NEEDS = {'kernel-verified': ('terminal',), 'theorem-supported': ('theorem', 'terminal'), 'computationally-verified': ('computation',),
         'argument-supported': ('argument', 'theorem', 'terminal', 'computation'), 'synthesis-suggested': ('argument', 'theorem', 'terminal',
                                                                                                        'computation', 'reading', 'statement'),
         'statement-grade': ('argument', 'theorem', 'terminal', 'computation', 'reading', 'statement')}

# ### the kernel pins the papers name with a terminal, each as cited: key -> (repo, the pin as cited, the expected commit, where the paper names it)
PINS = {
    'effects': ('SIDE-effects', 'c66f3c5', 'c66f3c5', 'BV :64'),
    'lv050': ('SIDE-lv-conservation', 'v0.5.0', '1767bd6', 'BV :145, :436'),
    'lv051': ('SIDE-lv-conservation', 'v0.5.1', 'bc4751e', 'BV :145, :436'),
    'k14': ('SIDE-kernel', 'v1.4', 'f374174', 'BV :169'),
}
# ### the pins the papers name with no terminal, resolved for the record and certifying no row
PINS_NT = {
    'bft': ('SIDE-bsd-formation-transfer', '3491766', '3491766', 'BV :472'),
    'bm': ('SIDE-bsd-multiplicity', 'd77ce30', 'd77ce30', 'BV :472'),
    'lv080': ('SIDE-lv-conservation', 'v0.8.0', '6efa9e5', 'BV :436'),
    'k13': ('SIDE-kernel', 'v1.3', '0bc21c0', 'BV :438'),
}
# ### the kernel reads at those pins: key -> (pin key, file, line, needle on that line, what the statement says)
KREADS = {
    'sha': ('effects', 'SIDEEffects/Structural.lean', 213, 'theorem sha_bounded : ¬ShaGrows := by',
            '`BSD.sha_bounded : ¬ShaGrows` (:213), from `all_bound` (:207) over `bounds_sha`'),
    'sha_def': ('effects', 'SIDEEffects/Structural.lean', 199, 'def bounds_sha : Framework → Prop',
                '`bounds_sha` defined by cases, True on each of six frameworks (:199-:205)'),
    'bsd': ('effects', 'SIDEEffects/Structural.lean', 236, 'theorem bsd_full : ¬RankMismatch := by',
            '`BSD.bsd_full : ¬RankMismatch` (:236), from `all_mismatch_absent` (:230)'),
    'bsd_def': ('effects', 'SIDEEffects/Structural.lean', 224, 'def mismatch_absent : MismatchMechanism → Prop',
                '`mismatch_absent` defined by cases, True on each of four mechanisms (:224-:228)'),
    'lv_c7': ('lv050', 'SIDELvConservation/DirichletC7Order.lean', 771, 'theorem exists_norm_completedLFunction_le_exp {N : ℕ} [NeZero N]',
              '`exists_norm_completedLFunction_le_exp`: for a Dirichlet character χ ≠ 1, some A and C bound ‖completedLFunction χ s‖ by '
              'C · exp(A · ‖s‖ · log(‖s‖ + 2)) (:771-:775)'),
    'lv_ft': ('lv051', 'SIDELvConservation/C7FiniteTypeFalse.lean', 68, 'theorem C7_finite_type_false :',
              '`C7_finite_type_false`: no C and A bound ‖completedRiemannZeta₀ s‖ by C · exp(A · ‖s‖) (:68-:69)'),
    'ed': ('k14', 'Kernel/Cascade/SieveCeiling.lean', 309, 'theorem e_difficulty (s : DeterminedSystem) (h_conserved : s.isConserved) :',
           '`e_difficulty`: for a conserved DeterminedSystem, IsDecidable s ↔ Nonempty (DomainOstrowski s) (:309-:310)'),
    'ed_xi': ('k14', 'Kernel/Cascade/SieveCeiling.lean', 349, 'theorem e_difficulty_xi :',
              '`e_difficulty_xi` at ξ’s system, whose docstring reads both sides false there (:346-:349)'),
    'scs': ('k14', 'Kernel/Cascade/SieveCeilingSemantic.lean', 48, 'theorem sieve_ceiling_semantic {onLine : U → Prop}',
            '`sieve_ceiling_semantic`: no r-respecting certificate is extensionally equal to a target that is not r-invariant (:48-:50)'),
}
# ### the pins named without a terminal, read for the record (not a certifying read): key -> (pin key, file, line, needle, what stands there)
NTREADS = {
    'bft_total': ('bft', 'SIDEBSDFormationTransfer/Basic.lean', 67, 'theorem formation_total_seven : formation_total_BSD = 7 := by decide',
                  '`formation_total_seven` by decide over n1_BSD := 2 (:57), the other entries numerals (:59-:63)'),
    'bm_six': ('bm', 'SIDEBSDMultiplicity/Basic.lean', 163, 'theorem six_sha_frameworks : all_sha_frameworks.length = 6 := by decide',
               '`six_sha_frameworks`: a list’s length is 6 by decide (:163)'),
}
# ### names a paper cites without a pin, read for the record where they stand (not a certifying read)
UNPINNED = {
    'transversal_generic_empty': ('SIDE-simplicity', 'main', 'SIDESimplicity/Codimension.lean', 30, 'theorem transversal_generic_empty', 'ZS :54'),
    'six_sha_frameworks': ('SIDE-bsd-multiplicity', 'main', 'SIDEBSDMultiplicity/Basic.lean', 163, 'theorem six_sha_frameworks', 'BV :213'),
    'the retirement of sha_bounded and bsd_full': ('SIDE-effects', 'main', 'SIDEEffects/Structural.lean', 98,
                                                   '(Retired: `bounds_sha := True`, `mismatch_absent := True`', 'BV :64'),
}

T1 = 'I-7 @ 847e433; IB Thm 3.1 @ 1d0109f'
T2 = 'detector, epstein @ v0.16 = c404e72; IB Thm 3.7 @ 1d0109f'
R1 = ('R1', 'DARK', 2, T2, 'the step from the five sources to every zero is the Mechanism Theorem’s Independence, the mechanism enumeration’s '
                          'step at multiplicity, whose compiled exclusions are conditions on a real σ naming no function, so they hold beside the '
                          'Epstein configuration the detector meets at ρ_E; the transversality step uses no property of the Euler product', 'RH-60')
R2 = ('R2', 'DARK', 1, T1, 'a GUE statistic offered toward simplicity: level repulsion is a law of the spacings, a statistic over the ordinates, '
                          'carrying no zero’s real part and no zero’s multiplicity', 'RH-59')
R3 = ('R3', 'DARK', 2, T2, 'the transfer carries the seven classes’ exclusion to Λ(E, s) under h2; the classes’ compiled exclusions are '
                          'conditions on a real σ naming no function, so they hold beside the Epstein configuration, and the Hasse bound the '
                          'transfer adds bounds each Euler factor’s roots and places no zero', 'RH-60')
R4 = ('R4', 'NOT A ROUTE', None, '—', 'a bench fact: a finite range of zeros computed simple, offered as consistency with the codimension '
                                      'argument and recorded at its own grade, the zeros beyond the range left open', 'RH-58')

C = [
    # ---------------------------------------------------------------- ZERO_SIMPLICITY (p2-6)
    ('ZS-01', 'ZS', 12, 'This is a codimension-5 condition on a one-parameter family.', 'ZS states that a double zero of ξ on the critical line '
     'needs five independent real-analytic functions of γ to vanish together, a codimension-5 condition on a one-parameter family.',
     'argument-supported', 'argument', 'the decomposition at :16-:38 and the transversality step at :50-:54', None),
    ('ZS-02', 'ZS', 12, 'classifying zero simplicity as TYPE I (provable)', 'ZS’s abstract states that the codimension and GUE arguments converge '
     'from independent directions and class zero simplicity TYPE I.', 'statement-grade', 'statement', 'the abstract’s summary; the paper’s :119 '
     'says neither mechanism alone is complete', None),
    ('ZS-03', 'ZS', 18, 'has seven mechanism classes in its SIDE formation (2, 3, 2, 0)', 'ZS assigns the completed zeta function the SIDE '
     'formation (2, 3, 2, 0) with seven mechanism classes, defining ξ(s) as π^(−s/2) Γ(s/2) ζ(s).', 'statement-grade', 'statement',
     'stated at :18; the factor s(s − 1)/2 that makes ξ entire, which the Hadamard product at :30 needs, is not in the definition', None),
    ('ZS-04', 'ZS', 20, 'We classify these into additive contributions', 'ZS splits ξ′’s contributions by mechanism class into five additive '
     'ones and two structural constraints.', 'statement-grade', 'statement', 'the classification at :22-:38', None),
    ('ZS-05', 'ZS', 26, 'At σ = 1/2, the balance identity forces each term p⁻ˢ to lie on the unit circle', 'ZS states that at σ = 1/2 each '
     'p^(−s) lies on the unit circle and that f₂ is an absolutely convergent sum of oscillatory terms.', 'statement-grade', 'statement',
     'at σ = 1/2, |p^(−s)| = p^(−1/2), and the prime sum for ζ′/ζ does not converge absolutely there (the claim bank)', None),
    ('ZS-06', 'ZS', 28, '|f₃(γ₁)| ≈ 0.90', 'ZS gives the digamma contribution f₃ = ψ(s/2)/2 − (log π)/2 with |f₃(γ₁)| ≈ 0.90 at the first zero.',
     'computationally-verified', 'computation', 'the claim bank computes |f₃(γ₁)| ≈ 0.8996', None),
    ('ZS-07', 'ZS', 28, 'The digamma function has no zeros in the right half-plane', 'ZS states that the digamma function has no zeros in the right '
     'half-plane, so |f₃(γ)| stays bounded away from zero for every γ > 0.', 'statement-grade', 'statement', 'ψ vanishes at x ≈ 1.4616 on the '
     'positive real axis (the claim bank); |f₃(γ)| stays above 0.82 on (0, 100], its imaginary part positive there', None),
    ('ZS-08', 'ZS', 30, 'f₅(γ): Hadamard sum (from C₅, local-global analytic).', 'ZS takes the Hadamard product’s sum over the other zeros as an '
     'additive contribution dominated by the nearest zeros.', 'statement-grade', 'statement', 'stated at :30', None),
    ('ZS-09', 'ZS', 36, 'This couples the values of', 'ZS reads the functional equation as the constraint ξ′(ρ) = −ξ′(1 − ρ), coupling the values '
     'at ρ and 1 − ρ without an additive contribution.', 'argument-supported', 'argument', 'the derivative of ξ(s) = ξ(1 − s) at :36', None),
    ('ZS-10', 'ZS', 52, 'is equivalent to Φ(γ) ∈ H', 'ZS maps γ to the five contributions in ℂ⁵, a double zero being the curve meeting the '
     'hyperplane where they sum to zero.', 'argument-supported', 'argument', 'the map and the hyperplane at :52', R1),
    ('ZS-11', 'ZS', 54, 'By transversality (Thom 1956), a curve generically misses a codimension-1 surface', 'ZS cites Thom’s transversality '
     '(1956) for the curve generically missing that hyperplane.', 'theorem-supported', 'theorem', 'Thom 1956 named at :54 and :139 for the '
     'generic statement', R1),
    ('ZS-12', 'ZS', 54, 'the manuscript-leg version of the compiled kernel terminal', 'ZS names SIDESimplicity.transversal_generic_empty as the '
     'compiled terminal its transversality argument is the manuscript leg of.', 'statement-grade', 'statement', 'named without a pin; at '
     'SIDE-simplicity main 54ba4f3 it states curveDim − obstrCodim < 0 from curveDim = 1 and 2 ≤ obstrCodim, integer arithmetic '
     '(SIDESimplicity/Codimension.lean :30)', None),
    ('ZS-13', 'ZS', 58, 'generic position is actual position.', 'ZS states that in a determined system with no tunable parameters generic position '
     'is actual position.', 'argument-supported', 'argument', 'argued at :60; the paper’s :119 names this the step that invokes the Mechanism '
     'Theorem', R1),
    ('ZS-14', 'ZS', 60, 'Therefore Φ(ℝ) ∩ H = ∅, and all zeros are simple.', 'ZS concludes from the Mechanism Theorem’s Independence that the five '
     'sources admit no conspiracy, so every zero of ξ is simple.', 'argument-supported', 'argument', 'argued at :60 from the Mechanism Theorem',
     R1),
    ('ZS-15', 'ZS', 64, 'The codimension is 5, not 1.', 'ZS states a codimension margin of 5, weak correlation between two sources leaving 4.',
     'statement-grade', 'statement', 'stated at :64; :106 gives the codimension as 5 − 1 = 4', None),
    ('ZS-16', 'ZS', 80, 'confirmed computationally for the first 10¹³+ zeros (Platt 2017', 'ZS states that ξ′(ρ) ≠ 0 is confirmed computationally '
     'for the first 10¹³ and more zeros, citing Platt (2017), with no double zero observed.', 'computationally-verified', 'computation',
     'a computation of the literature reported at :80, the reference at :129; the claim bank finds ξ′(ρ₁) ≠ 0 at the first zero', R4),
    ('ZS-17', 'ZS', 82, 'The numerical data is consistent with the codimension argument', 'ZS reads the numerical data as consistent with the '
     'codimension argument, the five contributions individually nonzero.', 'statement-grade', 'statement', 'the table at :72-:78 gives one value, '
     '|f₃(γ₁)|, and the other four as > 0 without values', None),
    ('ZS-18', 'ZS', 88, 'has quarter-twist symmetry T with T² = −I', 'ZS states that the Trivium has a quarter-twist symmetry T with T² = −I, the '
     'defining property of spinors.', 'statement-grade', 'statement', 'stated at :88', None),
    ('ZS-19', 'ZS', 93, '| GUE | T² = −I (complex) | 2 | Fermionic |', 'ZS’s table of Dyson’s three ensembles assigns T² = +I to GOE, T² = −I '
     'complex to GUE and T² = −I quaternionic to GSE.', 'statement-grade', 'statement', 'in Dyson’s classification β = 2 is the class with no '
     'antiunitary time-reversal symmetry, and an antiunitary T with T² = −1 gives β = 4, the symplectic class', None),
    ('ZS-20', 'ZS', 96, 'var/mean² = 0.189', 'ZS reports that random perturbation of the Trivium’s dark eigenvalue matrix gives var/mean² = 0.189, '
     'against GUE 0.178, GOE 0.286 and Poisson 1.000.', 'computationally-verified', 'computation', 'reported at :96 without its method or data; '
     'the Wigner surmises give 0.178 for β = 2 and 0.273 for β = 1 (the claim bank)', None),
    ('ZS-21', 'ZS', 98, 'The probability of a double zero (s = 0) is exactly zero under GUE statistics.', 'ZS states that at β = 2 level repulsion '
     'makes the spacing density vanish as s² near 0, so a double zero has probability zero under GUE statistics.', 'argument-supported',
     'argument', 'the level-repulsion law at :98', R2),
    ('ZS-22', 'ZS', 100, "Montgomery's pair correlation conjecture (1973)", 'ZS cites Montgomery’s pair-correlation conjecture and Odlyzko’s '
     'computations matching GUE at height 10²⁰.', 'computationally-verified', 'computation', 'Odlyzko’s computations cited at :100 and :127; '
     'the conjecture itself open', None),
    ('ZS-23', 'ZS', 106, 'giving codimension 5 − 1 = 4', 'ZS’s formation-framework section gives the codimension as 5 − 1 = 4, five contributions '
     'over one parameter.', 'statement-grade', 'statement', 'against :12, :52 and :64, which give codimension 5 for the same condition', None),
    ('ZS-24', 'ZS', 108, 'zero simplicity has infinite formation capacity', 'ZS states that zero simplicity has infinite formation capacity, no '
     'weight-1 perturbation introducing a double zero.', 'statement-grade', 'statement', 'stated at :108 from a companion paper', None),
    ('ZS-25', 'ZS', 117, 'T² = −I forces β = 2, which forces level repulsion, which forbids double zeros', 'ZS lists the GUE argument as its second '
     'mechanism: T² = −I forcing β = 2, level repulsion and no double zero.', 'argument-supported', 'argument', 'argued at :96-:98', R2),
    ('ZS-26', 'ZS', 119, 'Neither mechanism alone is a complete proof', 'ZS states that neither mechanism alone settles simplicity: the codimension '
     'argument needs generic = actual, invoking the Mechanism Theorem, and the GUE argument needs Montgomery’s conjecture.', 'statement-grade',
     'statement', 'the paper’s own scope at :119', None),
    # ---------------------------------------------------------------- BSD_TRANSFER (p2-11)
    ('BT-01', 'BT', 12, 'GRH follows from RH by one observation', 'BT states that GRH follows from RH by one observation, |χ(p)|² = 1 cancelling '
     'the character twist and keeping the formation (2, 3, 2, 0) = 7.', 'statement-grade', 'statement', 'stated at :12', None),
    ('BT-02', 'BT', 14, 'BSD asks: does the SAME transfer work for L(E,s)', 'BT asks whether the same transfer works for L(E, s), Hasse’s bound '
     'replacing |χ(p)|² = 1.', 'statement-grade', 'statement', 'the question at :14', None),
    ('BT-03', 'BT', 21, 'decomposition-dependent: different parsings of the same system yield', 'BT’s Gate 1b note states that the formation tuple '
     'is decomposition-dependent and that the transfer it verifies is of TYPE, not of a raw tuple.', 'statement-grade', 'statement',
     'the note at :20-:25', None),
    ('BT-04', 'BT', 37, 'Λ(E,s) = w_E · Λ(E, 2−s), where w_E = ±1 (root number)', 'BT states the functional equation Λ(E, s) = w_E Λ(E, 2 − s) '
     'with root number ±1 and critical line Re(s) = 1.', 'theorem-supported', 'theorem', 'modularity named at :51 (Wiles et al.)', None),
    ('BT-05', 'BT', 41, "Hasse's theorem: |a_p| ≤ 2√p for all primes p ∤ N.", 'BT cites Hasse’s theorem, |a_p| ≤ 2√p at every prime of good '
     'reduction.', 'theorem-supported', 'theorem', 'Hasse’s theorem named at :41', None),
    ('BT-06', 'BT', 71, 'Λ(E, 1) = 0 forced.', 'BT states that root number −1 makes Λ(E, 1 + it) purely imaginary and forces a zero at s = 1, the '
     'parity phenomenon.', 'argument-supported', 'argument', 'argued at :65-:75 from the functional equation and integral coefficients', None),
    ('BT-07', 'BT', 105, 'This gives 1/2 − σ = σ − 3/2, so σ = 1.', 'BT computes the balance for L(E, s): |α_p p^(−s)| = p^(1/2 − σ) equals its '
     'reflection under s ↦ 2 − s at σ = 1.', 'argument-supported', 'argument', 'the computation at :101-:105 from |α_p| = √p; recomputed in the '
     'claim bank', None),
    ('BT-08', 'BT', 107, 'THIS IS WHERE HASSE ENTERS.', 'BT states that the factorisation with |α_p| = |β_p| = √p needs Hasse’s bound, so balance at '
     'Re(s) = 1 enters at C₄.', 'argument-supported', 'argument', 'the chain at :109-:115', None),
    ('BT-09', 'BT', 127, 'Hasse IS a consequence of modularity (Eichler-Shimura + Deligne).', 'BT states that Hasse’s bound follows from '
     'modularity through Eichler–Shimura and Deligne, so C₅ couples to C₄ for L(E, s).', 'theorem-supported', 'theorem',
     'Eichler–Shimura and Deligne named at :127', None),
    ('BT-10', 'BT', 129, 'the RESONANCE score for BSD is higher than for ξ', 'BT reads the tighter independence as a higher RESONANCE score for BSD '
     'than for ξ.', 'statement-grade', 'statement', 'a reading at :129', None),
    ('BT-11', 'BT', 171, 'All seven transfer.', 'BT states that all seven mechanism classes transfer to L(E, s), Hasse entering at C₄ and '
     'propagating to C₅ and C₇.', 'argument-supported', 'argument', 'the per-class checks at :47-:155', None),
    ('BT-12', 'BT', 173, 'The SIDE proof for ξ applies to L(E,s) with one substitution', 'BT states that the SIDE argument for ξ applies to L(E, s) '
     'with the one substitution |χ(p)|² = 1 → |α_p/√p|² = 1.', 'statement-grade', 'statement', 'stated at :173; the argument for ξ it carries '
     'is the mechanism enumeration the sieve reads at RH-60', R3),
    ('BT-13', 'BT', 179, 'ALL nontrivial zeros of L(E,s) lie on Re(s) = 1.', 'BT states that the formation transfer gives every nontrivial zero of '
     'L(E, s) on Re(s) = 1.', 'argument-supported', 'argument', 'argued from the transfer at :159-:173', R3),
    ('BT-14', 'BT', 183, "The formation transfer doesn't address multiplicity", 'BT states that the transfer addresses the zeros’ location and not '
     'the multiplicity at s = 1, which BSD needs.', 'statement-grade', 'statement', 'stated at :183 and :196', None),
    ('BT-15', 'BT', 190, 'The sorry has narrowed.', 'BT states that after the transfer the remaining content of BSD is the order of vanishing at '
     's = 1 equalling the rank.', 'statement-grade', 'statement', 'stated at :185-:190', None),
    ('BT-16', 'BT', 198, '**TECHNE tool for multiplicity:**', 'BT names a tool of a private library for the multiplicity question, carried here by '
     'pointer alone.', 'statement-grade', 'statement', 'TECHNE-POINTER', None),
    ('BT-17', 'BT', 203, 'Ω (the real period) — from C₁', 'BT traces the BSD formula’s period to C₁, the regulator to C₂, |Ш| to C₄ and the '
     'Tamagawa product to C₅.', 'synthesis-suggested', 'reading', 'a reading at :202-:206', None),
    ('BT-18', 'BT', 210, 'This observation is new.', 'BT states that the BSD formula is a product of seven mechanism-class contributions, each '
     'independently computable, and that this observation is new.', 'statement-grade', 'statement', 'its own list at :203-:206 names four '
     'contributions', None),
    # ---------------------------------------------------------------- BSD_VIA_FORMATION_TRANSFER (p2-29)
    ('BV-01', 'BV', 11, 'Ш-finiteness and full BSD remain open', 'BV’s v0.1.1 re-grade scopes its headline: the formation transfer is what is '
     'machine-verified, Ш-finiteness and full BSD remaining open.', 'statement-grade', 'statement', 'the paper’s claim-status note at :11', None),
    ('BV-02', 'BV', 13, 'are each re-scoped to hold', 'BV’s v0.1.2 pass re-scopes the GRH-for-Λ(E, s) consequence, the Ш-finiteness square and the '
     'rank equality to hold under the open premise h2.', 'statement-grade', 'statement', 'the paper’s note at :13', None),
    ('BV-03', 'BV', 19, 'four unconditionally, three via the Hasse bound', 'BV states that Λ(E, s) keeps ξ’s formation (2, 3, 2, 0) = 7 and that '
     'all seven classes transfer, four unconditionally and three through the Hasse bound.', 'argument-supported', 'argument',
     'the per-class table at :137-:145', None),
    ('BV-04', 'BV', 19, 'What is machine-verified in the federated kernels', 'BV states that the kernels SIDE-bsd-formation-transfer and '
     'SIDE-bsd-multiplicity machine-verify the formation transfer -- the tuple match, root-number parity and the enumerations -- graded closed '
     'scaffolding under the W-5 relabel.', 'statement-grade', 'statement', 'named without a pin and without a terminal at :19; at the head '
     'commits the era annotation names (:472), the tuple is defined as numerals and its sum decided (SIDEBSDFormationTransfer/Basic.lean '
     ':57-:67)', None),
    ('BV-05', 'BV', 33, 'the Shafarevich-Tate group $\\Sha(E/\\mathbb{Q})$ is finite.', 'BV’s Chapter 1 states Ш(E/ℚ) finite for every elliptic '
     'curve over ℚ, headed Theorem 1.', 'statement-grade', 'statement', 'headed Theorem at :31; the paper’s own :11, :25 and :209 keep it open',
     None),
    ('BV-06', 'BV', 37, 'the algebraic rank of $E(\\mathbb{Q})$ equals the analytic rank', 'BV’s Chapter 1 states the algebraic rank equal to the '
     'analytic rank, with the BSD formula, headed Theorem 2.', 'statement-grade', 'statement', 'headed Theorem at :35; the paper’s own :11, '
     ':25 and :263 keep it open', None),
    ('BV-07', 'BV', 45, '(bounded by 16 by Mazur)', 'BV states that the torsion subgroup’s order is at most 16 by Mazur’s theorem.',
     'theorem-supported', 'theorem', 'Mazur 1977 named at :45 and :80', None),
    ('BV-08', 'BV', 57, 'The SIDE Exclusion *form* is machine-checked in vanilla Lean 4', 'BV states that the SIDE Exclusion form is machine-checked '
     'with each framework’s bound and each mismatch’s exclusion entered as := True placeholders, so the theorems are form-level and settle '
     'neither Ш-finiteness nor rank equality.', 'kernel-verified', 'terminal', 'effects', None),
    ('BV-09', 'BV', 64, 'exist in `SIDEEffects/Structural.lean` **at pin `c66f3c5`**', 'BV’s kernel-citation pin places BSD.sha_bounded and '
     'BSD.bsd_full in SIDEEffects/Structural.lean at c66f3c5, retired from the tree on 2026-06-16.', 'kernel-verified', 'terminal', 'effects',
     None),
    ('BV-10', 'BV', 68, 'are **enumeration / form-certificates**', 'BV classes the retired theorems as enumeration or form certificates and the '
     'formation kernel as a placement certificate, neither a certificate for Ш-finiteness or rank equality.', 'statement-grade', 'statement',
     'the claim–certificate calculus it cites, EXCLUSION_ENGINE §VIII.0 (:68)', None),
    ('BV-11', 'BV', 80, '(Mordell 1922)', 'BV states that E(ℚ) is finitely generated, ℤ^r ⊕ T, by Mordell’s theorem.', 'theorem-supported',
     'theorem', 'Mordell 1922 named at :80', None),
    ('BV-12', 'BV', 92, 'The Hasse bound (Hasse 1933)', 'BV cites the Hasse bound |a_p| ≤ 2√p (Hasse 1933), equivalent to a real Sato–Tate angle.',
     'theorem-supported', 'theorem', 'Hasse 1933 named at :92 and :420', None),
    ('BV-13', 'BV', 94, 'By the modularity theorem (Wiles 1995', 'BV cites the modularity theorem for the weight-2 newform and the continuation of '
     'L(E, s) to an entire function.', 'theorem-supported', 'theorem', 'Wiles 1995, Taylor–Wiles and Breuil–Conrad–Diamond–Taylor named at :94',
     None),
    ('BV-14', 'BV', 108, 'rank 0 and rank 1 cases were established by Kolyvagin (1990)', 'BV states that ranks 0 and 1 were settled by Kolyvagin '
     'and by Gross–Zagier with Kolyvagin through Heegner points, higher ranks out of that technique’s reach.', 'theorem-supported', 'theorem',
     'Kolyvagin 1990 and Gross–Zagier 1986 named at :108', None),
    ('BV-15', 'BV', 127, 'Three Ostrowski places: $\\infty$, $p$-adic non-arch, global', 'BV’s four-stage table counts three Ostrowski places, ∞, '
     'p-adic and global, for ξ and for Λ(E, s).', 'statement-grade', 'statement', 'Ostrowski’s theorem gives the archimedean place and one '
     'p-adic place for each prime of ℚ', None),
    ('BV-16', 'BV', 145, '`SIDELvConservation.exists_norm_completedLFunction_le_exp`, SIDE-lv-conservation v0.5.0 = `1767bd6`', 'BV cites '
     'exists_norm_completedLFunction_le_exp at SIDE-lv-conservation v0.5.0 = 1767bd6 for the order ≤ 1 growth input, stated for the completed '
     'Dirichlet L-function.', 'kernel-verified', 'terminal', 'lv050', None),
    ('BV-17', 'BV', 145, '`C7_finite_type_false` (v0.5.1 = `bc4751e`)', 'BV cites C7_finite_type_false at SIDE-lv-conservation v0.5.1 = bc4751e as '
     'a compiled negative giving C₇ concrete content.', 'kernel-verified', 'terminal', 'lv051', None),
    ('BV-18', 'BV', 151, 'five paths are independent and two are coupled through modularity', 'BV states that for Λ(E, s) five paths are '
     'independent and two coupled through modularity, the count kept and the independence narrowed.', 'statement-grade', 'statement',
     'stated at :147-:153', None),
    ('BV-19', 'BV', 157, 'The same structural argument applies to $\\Lambda(E, s)$', 'BV states that the seven classes’ structural argument for ξ '
     'applies to Λ(E, s), the line shifted to Re(s) = 1 by working in w = s − 1.', 'statement-grade', 'statement', 'stated at :157; the '
     'argument it carries is the mechanism enumeration the sieve reads at RH-60', R3),
    ('BV-20', 'BV', 159, '**Consequence (under the open premise `h2`).** All nontrivial zeros', 'BV states, under the open premise h2, that every '
     'nontrivial zero of Λ(E, s) lies on Re(s) = 1.', 'argument-supported', 'argument', 'argued at :155-:161 from the transfer with SIDE '
     'Exclusion, conditional on h2', R3),
    ('BV-21', 'BV', 161, 'not an independent unconditional result', 'BV states that the consequence rests on h2, carried openly, and is not an '
     'independent unconditional result.', 'statement-grade', 'statement', 'the paper’s own scope at :161', None),
    ('BV-22', 'BV', 169, 'the E-Difficulty terminals are de-vacuified', 'BV states that at SIDE-kernel v1.4 = f374174 e_difficulty reads its system '
     'and extracts the Ostrowski, the contentful ceiling in sieve_ceiling_semantic.', 'kernel-verified', 'terminal', 'k14', None),
    ('BV-23', 'BV', 169, 'This D↔E classification is therefore kernel-certified at the structural level', 'BV states that the classification of '
     'location as decidable and of the multiplicity at s = 1 as the E-difficulty residue is therefore kernel-certified at the structural level.',
     'statement-grade', 'statement', 'the terminal at f374174 states an equivalence over an abstract DeterminedSystem and names no L-function and '
     'no multiplicity; at ξ’s system both sides are false (e_difficulty_xi, :349)', None),
    ('BV-24', 'BV', 198, 'Every framework bounds. None produces a growth mechanism.', 'BV states that each of six frameworks bounds Ш, that none '
     'produces a growth mechanism, and that the six are exhaustive.', 'statement-grade', 'statement', 'the table at :189-:196; the '
     'exhaustiveness stated at :198 and :205', None),
    ('BV-25', 'BV', 207, 'Therefore $\\Sha(E/\\mathbb{Q})$ is finite. $\\square$', 'BV’s Chapter 4 closes Ш-finiteness by SIDE Exclusion over the six '
     'frameworks, its marker reading the square as the argument-form under h2 and Ш-finiteness open.', 'argument-supported', 'argument',
     'the exclusion at :200-:207 with the marker at :209', None),
    ('BV-26', 'BV', 213, 'enumerates the six frameworks but certifies each via `bounds_sha := True`', 'BV states that sha_bounded enumerates the six '
     'frameworks and certifies each through bounds_sha := True, a placeholder.', 'kernel-verified', 'terminal', 'effects', None),
    ('BV-27', 'BV', 213, '`six_sha_frameworks` genuinely counts the six frameworks', 'BV states that SIDE-bsd-multiplicity’s six_sha_frameworks '
     'counts the six frameworks without bounding Ш.', 'statement-grade', 'statement', 'named without a pin; at SIDE-bsd-multiplicity main d77ce30 '
     'a list’s length is 6 by decide (SIDEBSDMultiplicity/Basic.lean :163)', None),
    ('BV-28', 'BV', 250, 'The four candidates exhaust the structural sites', 'BV states that its four candidate mismatches exhaust the sites where '
     'rank and analytic order could decouple, each needing a failure of modularity or a Type D conspiracy.', 'statement-grade', 'statement',
     'stated at :250', None),
    ('BV-29', 'BV', 263, 'This equality **is** BSD', 'BV marks the rank-equality square as closing the mismatch form under h2, the equality itself, '
     'BSD, open.', 'statement-grade', 'statement', 'the paper’s marker at :263', None),
    ('BV-30', 'BV', 267, 'enumerates the four candidate mismatches but certifies each via `excluded := True`', 'BV states that bsd_full enumerates '
     'the four mismatches and certifies each through a := True placeholder, which it names excluded.', 'kernel-verified', 'terminal', 'effects',
     None),
    ('BV-31', 'BV', 273, 'The SIDE analysis is rank-independent.', 'BV states that the SIDE analysis is rank-independent, the wall at rank 2 a '
     'property of the Heegner-point technique.', 'statement-grade', 'statement', 'stated at :271-:273', None),
    ('BV-32', 'BV', 279, '**Formation-transfer / placement result** under premise `h2`', 'BV’s rank table gives rank two and above as a '
     'formation-transfer and placement result under h2, full rank equality open.', 'statement-grade', 'statement', 'the table at :275-:279',
     None),
    ('BV-33', 'BV', 291, 'the right side factors into contributions traceable to specific mechanism classes', 'BV reads the BSD formula’s right side '
     'as factoring into contributions traced to mechanism classes.', 'synthesis-suggested', 'reading', 'a reading at :291', None),
    ('BV-34', 'BV', 303, '$C_3$ (Cauchy-Riemann) / $C_6$ (spectral)', 'BV traces Ω to C₁, the regulator to C₂, |Ш| to C₄, the Tamagawa product to '
     'C₅ and the torsion to C₃ or C₆.', 'synthesis-suggested', 'reading', 'the table at :297-:303', None),
    ('BV-35', 'BV', 313, 'admits a factor-by-factor decomposition along mechanism classes', 'BV states that verifying BSD for a given curve admits a '
     'factor-by-factor decomposition along mechanism classes.', 'statement-grade', 'statement', 'stated at :313', None),
    ('BV-36', 'BV', 329, 'inductive BoundingFramework where', 'BV’s Chapter 7 prints the BSD namespace as six bounding frameworks and four mismatch '
     'candidates with two theorems.', 'statement-grade', 'statement', 'the listing is not SIDEEffects/Structural.lean at c66f3c5, whose namespace '
     '(:192-:240) names Framework with descent and padic, MismatchMechanism and mismatch_absent, where the listing has BoundingFramework, '
     'selmer, p_adic, MismatchCandidate and excluded', None),
    ('BV-37', 'BV', 374, 'Compiles under `leanprover/lean4:v4.29.0-rc8`.', 'BV states that the kernel compiles with zero sorry and zero axiom under '
     'leanprover/lean4:v4.29.0-rc8.', 'statement-grade', 'statement', 'SIDE-effects at c66f3c5 names leanprover/lean4:v4.30.0-rc2 in its '
     'lean-toolchain', None),
    ('BV-38', 'BV', 378, 'The kernel certifies the logical engine', 'BV states that the kernel certifies the SIDE-Exclusion syllogism and the '
     'enumerations, the arithmetic of each entry resting on independent literatures.', 'statement-grade', 'statement', 'stated at :378', None),
    ('BV-39', 'BV', 384, 'prescribes working in $w = s - 1$', 'BV works at the critical point s = 1 in the coordinate w = s − 1, the order of '
     'vanishing read at w = 0.', 'statement-grade', 'statement', 'stated at :384-:390', None),
    ('BV-40', 'BV', 402, 'Hilbert modular L-functions all share this architecture', 'BV states that symmetric-square, Rankin–Selberg and Hilbert '
     'modular L-functions share the architecture, which classes transfer left open.', 'statement-grade', 'statement', 'stated at :402', None),
    ('BV-41', 'BV', 406, '(proved by Barnet-Lamb, Geraghty, Harris, Taylor 2011 for non-CM elliptic curves)', 'BV cites the Sato–Tate distribution '
     'for non-CM curves and leaves its link to the classes open.', 'theorem-supported', 'theorem', 'Barnet-Lamb, Geraghty, Harris and Taylor '
     '2011 named at :406', None),
    ('BV-42', 'BV', 472, 'SIDE-bsd-formation-transfer `3491766`, SIDE-bsd-multiplicity `d77ce30`', 'BV’s era annotation records both paired kernels '
     'relabelled as placement scaffolding in their head commits 3491766 and d77ce30, cited as evidence nowhere.', 'statement-grade', 'statement',
     'pins with no terminal named; both commits resolve, each message reading “W-5 scaffolding relabel: withdraw claim-bearing status '
     '(placement skeleton)”', None),
    ('BV-43', 'BV', 476, '(3) Neither Clay problem is proved', 'BV states that neither Clay problem is settled in it, its era annotation adding and '
     'correcting nothing.', 'statement-grade', 'statement', 'the paper’s own sentence at :476-:478', None),
]

ROUTE_ROWS = {'RH-58': 'NOT A ROUTE', 'RH-59': 'DARK, test 1', 'RH-60': 'DARK, test 2'}
SIEVE = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md'
LSR = {}   # ### (R225)(4): the ls-remote calls this process made, per repository


def g(repo, *a):
    if 'ls-remote' in a:
        LSR[repo] = LSR.get(repo, 0) + 1
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    ls = (t or '').split(NL)
    return ls[:-1] if ls and ls[-1] == '' else ls


def paper_lines():
    return {k: lines_of(show(v[0])) for k, v in PAPERS.items()}


def techne_pointer():
    """### the pointer to TECHNE-Core: the sha256 of its tracked-file manifest at HEAD (`git ls-tree -r HEAD`), no body read or printed"""
    r = subprocess.run(['git', '-C', TE, 'ls-tree', '-r', 'HEAD'], capture_output=True)
    return hashlib.sha256(r.stdout.replace(b'\r\n', b'\n')).hexdigest() if r.returncode == 0 else None


def kv_reason(c):
    """### a kernel-verified row's reason: its pin, its resolution and the statements read there"""
    k = c[7]
    repo, pin, _w, _where = PINS[k]
    reads = [v for v in KREADS.values() if v[0] == k]
    st = pin_state(k)
    return '%s %s = commit %s, %s: %s' % (repo, pin, st[3], st[4] or 'NOT AT THE REMOTE', '; '.join('%s %s' % (r[1], r[4]) for r in reads))


def claims():
    """### the claims with each kernel-verified row's reason filled from its pin and the TECHNE row's pointer"""
    p = techne_pointer()
    out = []
    for c in C:
        if c[5] == 'kernel-verified':
            c = c[:7] + (kv_reason(c),) + c[8:]
        elif c[7] == 'TECHNE-POINTER':
            c = c[:7] + ('the TECHNE citation, carried by pointer alone: TECHNE-Core, its tracked-file manifest sha256 %s; no sentence of its body '
                         'carried' % p,) + c[8:]
        out.append(c)
    return out


def resolve_claims():
    """### every claim's needle on its cited line at the pin: [(id, ok, the line)]"""
    P = paper_lines()
    out = []
    for c in C:
        cid, pk, n, needle = c[0], c[1], c[2], c[3]
        l = P[pk][n - 1] if 0 < n <= len(P[pk]) else ''
        out.append((cid, needle in l, l))
    return out


def pin_state(key):
    """### a pin resolves when its commit is in the clone, peels to the expected commit, and is at the remote:
    ### (key, repo, pin, local commit, how the remote holds it or None)"""
    repo, pin, want, _where = PINS[key] if key in PINS else PINS_NT[key]
    path = 'D:/' + repo
    loc = g(path, 'rev-parse', '--verify', '-q', pin + '^{commit}').strip()
    if not loc.startswith(want):
        return (key, repo, pin, loc[:12], None)
    rem = None
    for l in g(path, 'ls-remote', 'origin', 'refs/tags/*').split(NL):
        if l.startswith(loc) and l.endswith('^{}'):
            rem = 'remote tag %s' % l.split('refs/tags/')[1][:-3]
            break
        if l.startswith(loc) and '^{}' not in l and rem is None:
            rem = 'remote tag %s' % l.split('refs/tags/')[1]
    if rem is None:
        head = g(path, 'ls-remote', 'origin', 'refs/heads/main').split('\t')[0].strip()
        if head and subprocess.run(['git', '-C', path, 'merge-base', '--is-ancestor', loc, head], capture_output=True).returncode == 0:
            rem = 'on the remote main %s' % head[:7]
    return (key, repo, pin, loc[:12], rem)


def _read(table, k):
    pk, f, n, needle, _what = table[k]
    repo, pin, _w, _where = PINS[pk] if pk in PINS else PINS_NT[pk]
    ls = lines_of(show(f, pin, 'D:/' + repo))
    l = ls[n - 1] if 0 < n <= len(ls) else ''
    return (k, needle in l, l)


def resolve_kernel():
    """### every kernel read at its pin: [(key, ok, line)]"""
    return [_read(KREADS, k) for k in KREADS]


def resolve_nt():
    """### the pins named without a terminal, read for the record: [(key, ok, line)]"""
    return [_read(NTREADS, k) for k in NTREADS]


def commit_subject(key):
    repo, pin, _w, _where = PINS_NT[key]
    return g('D:/' + repo, 'log', '-1', '--format=%s', pin).strip()


def unpinned_state(name):
    repo, rev, f, n, needle, where = UNPINNED[name]
    ls = lines_of(show(f, rev, 'D:/' + repo))
    l = ls[n - 1] if 0 < n <= len(ls) else ''
    return (name, repo, rev, f, n, bool(ls) and needle in l, g('D:/' + repo, 'rev-parse', '--short=7', rev).strip(), where)


def sieve_rows():
    out = {}
    for l in lines_of(show(SIEVE)):
        m = re.match(r'^\| ((?:RH|FD|CT|MC)-\d\d) \| ', l)
        if m and m.group(1) in ROUTE_ROWS and m.group(1) not in out:
            c = [x.strip() for x in l.strip().strip('|').split(' | ')]
            out[m.group(1)] = (c[4], c[5])
    return out


def grade_ok(c):
    if c[5] not in GRADES or c[6] not in NEEDS[c[5]]:
        return False
    if c[5] == 'kernel-verified':   # ### a certifying row: its pin resolves and every statement read at it stands
        st = pin_state(c[7])
        kr = dict((k, ok) for k, ok, _l in resolve_kernel())
        return bool(st[3]) and bool(st[4]) and all(kr[k] for k, v in KREADS.items() if v[0] == c[7])
    return True


# ================================================================================ THE LOAD-BEARING READING OF THE CLUSTER'S CERTIFYING ROWS
# ### (R225)(2): each kernel-verified row against the thesis the document's head states -- (load-bearing, the kind, the reason)
LOAD = {
    'BV-08': (False, 'placeholder', 'the Shafarevich-Tate and rank exclusion forms over := True placeholders, bearing no claim about Ш or the rank'),
    'BV-09': (False, 'placeholder', 'the placement of the same placeholder theorems at their pin'),
    'BV-26': (False, 'placeholder', 'the six frameworks each certified by bounds_sha := True'),
    'BV-30': (False, 'placeholder', 'the four mismatches each certified by a := True placeholder'),
    'BV-16': (False, 'another object', 'a growth bound for the completed Dirichlet L-function, not for Λ(E, s)'),
    'BV-17': (False, 'another object', 'a refuted finite-type bound for the completed ζ, not a statement about Λ(E, s)'),
    'BV-22': (False, 'another object', 'an equivalence over an abstract DeterminedSystem naming no L-function and no multiplicity'),
}


# ================================================================================ THE CLAIM BANK'S ARITHMETIC
def _is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def arith2f():
    """### the cluster's arithmetic recomputed: [(label, value, the paper's figure, agrees)]"""
    import mpmath
    mpmath.mp.dps = 30
    A = []
    g1 = mpmath.im(mpmath.zetazero(1))
    A.append(('ZS :70 the first ordinate γ₁', mpmath.nstr(g1, 9), '14.134725', abs(g1 - mpmath.mpf('14.134725')) < 1e-6))

    def f3(gm):
        return mpmath.digamma((mpmath.mpf(1) / 2 + 1j * gm) / 2) / 2 - mpmath.log(mpmath.pi) / 2
    v = abs(f3(g1))
    A.append(('ZS :28 |f₃(γ₁)|, f₃ = ψ(s/2)/2 − (log π)/2 at s = 1/2 + iγ₁', mpmath.nstr(v, 5), '0.90', round(float(v), 2) == 0.90))
    x0 = mpmath.findroot(mpmath.digamma, 1.46)
    A.append(('ZS :28 a zero of ψ on the positive real axis', mpmath.nstr(x0, 8), 'no zeros in the right half-plane', False))
    m = min((abs(f3(mpmath.mpf(k) / 100)), k / 100) for k in range(1, 10001))
    mi = min(mpmath.im(f3(mpmath.mpf(k) / 100)) for k in range(1, 10001))
    A.append(('ZS :28 min |f₃(γ)| and min Im f₃(γ) over γ = 0.01, 0.02, ..., 100', '%s at γ = %s ; %s' % (mpmath.nstr(m[0], 4), m[1], mpmath.nstr(mi, 4)),
              'bounded away from zero for all γ > 0', m[0] > 0.5 and mi > 0))
    p2 = 2 ** -0.5
    ps = [p for p in range(2, 100001) if _is_prime(p)]
    sums = []
    for cap in (10 ** 3, 10 ** 4, 10 ** 5):
        sums.append(sum(math.log(p) * p ** -0.5 / (1 - p ** -0.5) for p in ps if p <= cap))
    A.append(('ZS :26 |2^(−s)| at σ = 1/2 ; Σ_p (log p) p^(−1/2)/(1 − p^(−1/2)) over p ≤ 10³, 10⁴, 10⁵', '%.4f ; %.1f, %.1f, %.1f' % (p2, sums[0], sums[1], sums[2]),
              'on the unit circle ; absolutely convergent', False))

    def xi(s):
        return s * (s - 1) / 2 * mpmath.pi ** (-s / 2) * mpmath.gamma(s / 2) * mpmath.zeta(s)
    r1 = mpmath.mpf(1) / 2 + 1j * g1
    d = abs(mpmath.diff(xi, r1))
    A.append(('ZS :80 |ξ′(ρ₁)|, ξ(s) = s(s − 1)/2 · π^(−s/2) Γ(s/2) ζ(s)', mpmath.nstr(d, 6), 'ξ′(ρ) ≠ 0', d > 1e-6))
    w2, w1 = 3 * mpmath.pi / 8 - 1, 4 / mpmath.pi - 1
    A.append(('ZS :96 the Wigner surmises’ normalized spacing variance, β = 2 and β = 1', '%s, %s' % (mpmath.nstr(w2, 4), mpmath.nstr(w1, 4)),
              'GUE 0.178, GOE 0.286', round(float(w2), 3) == 0.178))
    A.append(('ZS :64 and :106 the codimension of the five-term condition', '5 ; 5 − 1 = 4', '5 (:12, :52, :64) ; 4 (:106)', False))
    sig = Fr(1)
    A.append(('BT :103-:105 1/2 − σ = σ − 3/2', 'σ = %s' % sig, 'σ = 1', Fr(1, 2) - sig == sig - Fr(3, 2)))
    return A


def main():
    rc = resolve_claims()
    bad = [x for x in rc if not x[1]]
    print('### claims %d ; needles failing %s' % (len(C), [(i, l[:90]) for i, _o, l in bad] or 'NONE'))
    for k in list(PINS) + list(PINS_NT):
        print('### pin %s' % (pin_state(k),))
    kb = [x for x in resolve_kernel() if not x[1]]
    print('### kernel reads %d ; failing %s' % (len(KREADS), [(k, l[:90]) for k, _o, l in kb] or 'NONE'))
    nb = [x for x in resolve_nt() if not x[1]]
    print('### reads at the pins without a terminal %d ; failing %s ; subjects %s' % (len(NTREADS), [(k, l[:90]) for k, _o, l in nb] or 'NONE',
                                                                                      [commit_subject(k) for k in ('bft', 'bm')]))
    for k in UNPINNED:
        print('### unpinned %s' % (unpinned_state(k)[:7],))
    print('### grades out of rule: %s' % ([c[0] for c in C if not grade_ok(c)] or 'NONE'))
    print('### routes: %s' % [(c[0], c[8][0], c[8][1], c[8][2], c[8][5]) for c in C if c[8]])
    print('### sieve rows: %s' % sieve_rows())
    from collections import Counter
    print('### grade counts: %s' % dict(Counter(c[5] for c in C)))
    print('### ids unique: %s ; load reading covers the certifying rows: %s' % (len(set(c[0] for c in C)) == len(C),
                                                                                sorted(LOAD) == sorted(c[0] for c in C if c[5] == 'kernel-verified')))
    print('### TECHNE pointer: %s' % techne_pointer())
    print('### ls-remote calls this run, per repository: %s' % LSR)
    if '--arith' in sys.argv:
        for a in arith2f():
            print('### %s -- %s ; the paper: %s ; agrees %s' % (a[0], a[1][:300], a[2], a[3]))


if __name__ == '__main__':
    main()
