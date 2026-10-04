# -*- coding: utf-8 -*-
"""b614_claims.py -- THE ACT'S DATA AND ITS RESOLVERS, UNDER (R224)(4): THE CLAIMS OF CLUSTER 2D'S EIGHT PAPERS.

### Every claim is the seat's one-sentence restatement of a paper's sentence, carried with a needle that must occur on the cited line of the
### paper at PLACE-papers e7b444e; its grade is the one the paper's own text supports, in the vocabulary of (R19) as (R220)(5) lists it:
### kernel-verified at a pin; theorem-supported; argument-supported; computationally-verified; synthesis-suggested; statement-grade.
### THE GRADING RULE, confirmed by (R222)(1): kernel-verified only where the paper names a terminal (or its file) at a pin and the
### statement read at that pin carries the claim; theorem-supported only where the paper names a theorem of the literature for it;
### computationally-verified only where the paper reports a computation; argument-supported where the paper's text argues the claim;
### synthesis-suggested where it reads a pattern across results; statement-grade where it states without argument. No grade is above the
### paper's own support. A ROUTE is a claim offered as an argument toward RH, simplicity or the open clause; each is read through the
### sieve's five tests in order. A pin RESOLVES, by the rule (R223)(1) confirms, when its commit is in the clone and at the remote.
### No paper of the cluster names TECHNE. This module writes nothing: `python tools/b614_claims.py` runs the resolvers and prints.
"""
import math
import os
import re
import subprocess
import sys
from fractions import Fraction as Fr

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'e7b444e'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PAPERS = {
    'CS': ('phase2/physics/COSMOLOGICAL_SIEVE_CEILING.md', 'p2-8', 269),
    'MA': ('phase2/physics/MATTER_AS_ARITHMETIC.md', 'p2-9', 270),
    'ST': ('phase2/physics/STORMER.md', 'p2-10', 271),
    'HC': ('phase2/physics/HODGE_CONSERVATION.md', 'p2-15', 272),
    'PO': ('phase2/physics/PRIME_ORDER.md', 'p2-25', 273),
    'FA': ('phase2/physics/FANO_DERIVATION_OF_LAMBDA.md', 'p2-30', 274),
    'YM': ('phase2/physics/YANG_MILLS_MONOGRAPH.md', 'p2-31', 275),
    'UF': ('heritage/UNIFICATION_OF_FORCES.md', 'p2-26', 276),
}
GRADES = ('kernel-verified', 'theorem-supported', 'argument-supported', 'computationally-verified', 'synthesis-suggested', 'statement-grade')
NEEDS = {'kernel-verified': ('terminal',), 'theorem-supported': ('theorem', 'terminal'), 'computationally-verified': ('computation',),
         'argument-supported': ('argument', 'theorem', 'terminal', 'computation'), 'synthesis-suggested': ('argument', 'theorem', 'terminal',
                                                                                                        'computation', 'reading', 'statement'),
         'statement-grade': ('argument', 'theorem', 'terminal', 'computation', 'reading', 'statement')}

# ### the kernel pins the papers name with a terminal, each as cited: key -> (repo, the pin as cited, the expected commit, where the paper names it)
PINS = {
    'omegab': ('SIDE-omega-b', '9c80279', '9c80279', 'ST :249, :257; MA :181'),
    'cosmo': ('SIDE-cosmo', 'c5cba30', 'c5cba30', 'MA :183'),
    'kernel': ('SIDE-kernel', '5e668b4', '5e668b4', 'ST :223'),
    'trivium': ('SIDE-trivium', '1aac3a9', '1aac3a9', 'ST :228'),
    'bridge': ('SIDE-residual-bridge', 'v0.1', 'b473d4b', 'FA :113'),
    'effects': ('SIDE-effects', 'c66f3c5', 'c66f3c5', 'YM :405'),
    'effects2': ('SIDE-effects', 'a27415d', 'a27415d', 'YM :405'),
    'ymf': ('SIDE-yang-mills-formation', 'v0.1.1', '73e9e2c', 'YM :405'),
}
# ### the kernel reads at those pins: key -> (pin key, file, line, needle on that line, what the statement says)
KREADS = {
    'omegab': ('omegab', 'SIDEOmegaB/Theorem.lean', 130, 'theorem omega_b_equals_4_over_81 :',
               '`SIDEOmegaB.omega_b_equals_4_over_81 : arithmeticSubstrate.omega = ⟨4, 81⟩` by decide (:130-:132)'),
    'omegab_def': ('omegab', 'SIDEOmegaB/Theorem.lean', 114, 'def arithmeticSubstrate : Formation :=',
                   'the tuple defined as numerals, n1 := 2, n2 := 3, n3 := 2, n4 := 0 (:114-:118)'),
    'omegab_num': ('omegab', 'SIDEOmegaB/Theorem.lean', 101, 'numerator   := f.n1 ^ f.n3', 'Formation.omega’s numerator n1^n3 (:101)'),
    'xi_def': ('cosmo', 'SIDECosmo/FormationPhaseSpace.lean', 53, 'def xi : FormationTuple := ⟨2, 3, 2, 0, by omega⟩', 'xi defined as ⟨2, 3, 2, 0⟩ (:53)'),
    'xi_total': ('cosmo', 'SIDECosmo/FormationPhaseSpace.lean', 59, 'theorem xi_total : total_slots xi = 81 := by decide',
                 '`xi_total : total_slots xi = 81` by decide (:59), total_slots f = trans^(prim + output) (:22)'),
    'xi_visible': ('cosmo', 'SIDECosmo/FormationPhaseSpace.lean', 60, 'theorem xi_visible : visible_slots xi = 4 := by decide',
                   '`xi_visible : visible_slots xi = 4` by decide (:60)'),
    'kn1': ('kernel', 'Kernel/Core.lean', 34, 'def n1 : Nat := 2', 'n1 defined := 2 (:34), the other entries as numerals'),
    'kcount': ('kernel', 'Kernel/Core.lean', 50, 'theorem formation_count : n1 + n2 + n3 + n4 = 7 := by decide',
               '`formation_count : n1 + n2 + n3 + n4 = 7` by decide (:50); `formation : 2 + 3 + 2 + 0 = 7` (:53)'),
    'card': ('trivium', 'Trivium/CardDerived.lean', 48, 'theorem mechanism_class_card_derived :',
             '`mechanism_class_card_derived : Fintype.card MechanismClass = ({-1, 2, -2, 3, -3, 6, -6} : Finset Int).card` (:48-:49)'),
    'card7': ('trivium', 'Trivium/CardDerived.lean', 44, 'theorem quadratic_discriminant_card_value :',
              '`quadratic_discriminant_card_value`: that image’s card is 7 by decide (:44-:45)'),
    'w1': ('bridge', 'SIDEResidualBridge/Bridge.lean', 77, 'theorem three_weight1_eq_14 :',
           '`three_weight1_eq_14 : fracEq (fadd (fadd weight1Contrib weight1Contrib) weight1Contrib) (14, 1) = true` by decide (:77-:78), weight1Contrib := (14, 3) (:57)'),
    'mg': ('effects', 'SIDEEffects/Structural.lean', 56, 'theorem mass_gap : ¬Massless := by',
           '`YangMills.mass_gap : ¬Massless` (:56), from `all_gapped` (:49) over `gapped` defined True on each sector (:43)'),
    'mg_def': ('effects', 'SIDEEffects/Structural.lean', 43, 'def gapped : Sector → Prop', '`gapped` defined by cases, True on each of four sectors (:43-:47)'),
    'mg_ret': ('effects2', 'SIDEEffects/Structural.lean', 73, 'Retired: `gapped := True` on four sectors', 'the placeholder recorded as retired (:73)'),
    'ymf': ('ymf', 'SIDEYangMillsFormation/Basic.lean', 69, 'theorem yang_mills_total_eight : formation_total = 8 := by decide',
            '`yang_mills_total_eight : formation_total = 8` by decide (:69) over n1 := 3 (:56), n2 := 3, n3 := 2, n4 := 0'),
    'ymf_n1': ('ymf', 'SIDEYangMillsFormation/Basic.lean', 56, 'def n1 : Nat := 3', 'n1 defined := 3 (:56)'),
}
# ### names a paper cites without a pin, read for the record where they stand (not a certifying read)
UNPINNED = {
    'xi_wall_sq': ('SIDE-cosmo', 'main', 'SIDECosmo/FormationPhaseSpace.lean', 63, 'theorem xi_wall_sq', 'ST :11, :139'),
    'partition_cardinalities': ('SIDE-substrate-cluster', 'main', 'SIDESubstrateCluster/Substrate.lean', 126, 'theorem partition_cardinalities', 'FA :31, :76'),
    'stab_order_24': ('SIDE-substrate-cluster', 'main', 'SIDESubstrateCluster/StabRefutation.lean', 63, 'theorem stab_order_24', 'FA :31, :64'),
    'catalogue_is_doubleton': ('SIDE-substrate-cluster', 'main', 'SIDESubstrateCluster/MuClassifier.lean', 62, 'theorem catalogue_is_doubleton', 'FA :97'),
    'omegaLambda_mu_shifted': ('SIDE-residual-bridge', 'main', 'SIDEResidualBridge/Bridge.lean', 87, 'theorem omegaLambda_mu_shifted', 'FA :143, :145'),
    'PrimeMosaic.lean': ('SIDE-constants', 'main', 'PrimeMosaic.lean', 1, '', 'PO :57, :107'),
}

T2 = 'detector, epstein @ v0.16 = c404e72; IB Thm 3.7 @ 1d0109f'
R1 = ('R1', 'DARK', 2, T2, 'the exhaustiveness the paper credits to Conservation of Spectra and Tate’s thesis is the mechanism enumeration’s, whose '
                          'compiled exclusions are conditions on a real σ naming no function, so they hold beside the Epstein configuration the detector '
                          'meets at ρ_E', 'RH-60')
R2 = ('R2', 'DARK', 2, T2, 'the criterion the paper names, Ostrowski’s classification of places, is the enumeration’s exhaustiveness step, whose compiled '
                          'exclusions name no function and hold beside the Epstein configuration', 'RH-60')

C = [
    # ---------------------------------------------------------------- COSMOLOGICAL_SIEVE_CEILING (p2-8)
    ('CS-01', 'CS', 8, 'This file (v1.0, April 2026) is the oldest in the physics set', 'CS states that its 2026-07-19 re-grade re-scopes three headline '
     'claims to grade and changes no mathematics, κ value or formation count.', 'statement-grade', 'statement', 'the paper’s own claim-status note', None),
    ('CS-02', 'CS', 12, 'Flatness proves that the observational interface', 'CS states that the Spite plateau’s flatness shows the observational interface '
     'universal and not bright, and that the lithium problem’s resolution is stellar depletion.', 'argument-supported', 'argument', 'the argument at '
     ':98-:102 and the two-plateau comparison at :110-:123', None),
    ('CS-03', 'CS', 22, '**Discrepancy:** 0.49 dex, a factor of 3.1', 'CS reports the BBN prediction A(⁷Li) = 2.69 ± 0.04 dex against the Spite plateau’s '
     '2.20 ± 0.10 dex, a discrepancy of 0.49 dex, a factor of 3.1.', 'computationally-verified', 'computation', 'the cited values at :20-:21; '
     '10^0.49 ≈ 3.09 in the claim bank', None),
    ('CS-04', 'CS', 34, '**Formation of BBN:** (2, 3, 2, 0) = 7.', 'CS assigns BBN the formation (2, 3, 2, 0) = 7.', 'statement-grade', 'statement',
     'the table at :36-:41; the era annotation at :253-:254 reads the tuple as a modeling premise entering the flagship kernel by definition', None),
    ('CS-05', 'CS', 43, 'This is the same formation as ξ(s), the Shannon channel, and the genetic code.', 'CS reads BBN’s formation as the one ξ(s), the '
     'Shannon channel and the genetic code share.', 'synthesis-suggested', 'reading', 'a reading at :43', None),
    ('CS-06', 'CS', 62, '**The composite interface is dark for primordial ⁷Li**', 'CS gives κ < 0.65 for the composite observational interface, from '
     'per-stage values < 0.7, ~0.95 and ~0.95.', 'statement-grade', 'statement', 'the per-stage values stated at :59-:61 without a method; the '
     'composite is their product', None),
    ('CS-07', 'CS', 72, 'Selberg (1942) proved 40%. Conrey (1989) proved 41.6%.', 'CS states that sieve methods give density results for the zeros of ζ '
     'on the critical line and not that every zero lies on it, citing Selberg (1942) and Conrey (1989).', 'theorem-supported', 'theorem',
     'Selberg 1942 and Conrey 1989, named; Selberg’s theorem gives a positive proportion and Conrey’s more than two fifths, so the figures 40% '
     'and 41.6% and a record near 100% do not match the results cited', None),
    ('CS-08', 'CS', 72, 'is the sieve-ceiling conjecture, not a theorem', 'CS grades as conjecture the reading that no sieve method can bridge density to '
     'placement, the Sieve Ceiling Lemma standing as the structural result.', 'statement-grade', 'statement', 'the paper’s own claim-status note '
     'at :72; the Lemma is not stated in this paper', None),
    ('CS-09', 'CS', 74, 'the Euler product interface has κ = 0 for zero placement', 'CS states that sieve methods operate through the Euler product, '
     'whose interface has κ = 0 for zero placement.', 'statement-grade', 'statement', 'stated at :74', None),
    ('CS-10', 'CS', 96, '**Theorem (Informal).** A universal dark interface preserves the flatness', 'CS states that a universal dark interface keeps a '
     'plateau flat while offsetting its absolute value, flatness evidencing universality and not brightness.', 'argument-supported', 'argument',
     'the argument at :98-:102', None),
    ('CS-11', 'CS', 121, 'Both produced by universal stellar processing.', 'CS reads the second lithium plateau of Mucciarelli and colleagues (2022), at '
     'A(Li) ≈ 1.0 dex in early red giants, as the controlled experiment for the mechanism.', 'argument-supported', 'argument',
     'the comparison table at :112-:119', None),
    ('CS-12', 'CS', 140, 'No new physics is required at the current level of precision.', 'CS assesses the residual of 0.1-0.15 dex as within reach of '
     'pre-main-sequence depletion and 3D NLTE corrections.', 'synthesis-suggested', 'reading', 'an assessment across the sources tabled at '
     ':133-:138', None),
    ('CS-13', 'CS', 146, '**TYPE II — graduated decidable.**', 'CS classifies the lithium problem TYPE II, a Science-Statement whose warrant is '
     'observational registration.', 'statement-grade', 'statement', 'the paper’s own claim-status note at :148', None),
    ('CS-14', 'CS', 154, 'STAREVOL models with diffusion + rotation + parametric turbulence reproduce the Spite plateau flatness', 'CS cites STAREVOL '
     'models of Nguyen and colleagues (2024) reproducing the plateau’s flatness and depletion, and models of Corazza and colleagues (2025) '
     'reproducing both plateaux.', 'computationally-verified', 'computation', 'model computations, cited at :154-:156', None),
    ('CS-15', 'CS', 174, 'The sieve ceiling is a theorem in analytic number theory.', 'CS scopes its sieve-ceiling theorem to the Sieve Ceiling Lemma, '
     'the density-to-E-Difficulty framing conjecture-grade and its kernel terminals W-6 shells.', 'statement-grade', 'terminal',
     'kernel terminals named by role at :174, not by name or pin', None),
    ('CS-16', 'CS', 184, 'is substantially accounted for by recognizing that the Spite plateau', 'CS states that the lithium problem is substantially '
     'accounted for by stellar depletion, with a named residual of 0.1-0.15 dex, about 15%, carried as a standing candidate for new physics.',
     'argument-supported', 'argument', 'the residual analysis at :129-:140', None),
    ('CS-17', 'CS', 188, 'universality is not brightness', 'CS draws the lesson that a universal observational interface’s flat value is not to be '
     'read as the true value.', 'synthesis-suggested', 'reading', 'a reading at :188', None),
    ('CS-18', 'CS', 240, 'PROTECTIVE-SILENT (I-12a)', 'CS’s era annotation of 2026-08-21 reads the paper’s universal dark interface as of the '
     'protective-silent species.', 'synthesis-suggested', 'reading', 'a dated era annotation', None),
    # ---------------------------------------------------------------- MATTER_AS_ARITHMETIC (p2-9)
    ('MA-01', 'MA', 14, 'selecting the Arithmetic class at 0.13σ and excluding the others by 18.6σ to 351σ', 'MA states that the baryon density selects '
     'the Arithmetic class, Ω = 4/81, at 0.13σ against Planck 2018 and excludes the other three classes at 18.6σ to 351σ.',
     'computationally-verified', 'computation', 'the distances at :61-:71, recomputed in the claim bank', None),
    ('MA-02', 'MA', 28, '**Classes B and D: the second component remains STIPULATED.**', 'MA states that the second component of classes B and D is '
     'stipulated, the n₂ theorem not reaching them.', 'statement-grade', 'statement', 'the in-place narrowing at :27-:28', None),
    ('MA-03', 'MA', 30, '**Theorem (n₂ = 3).** Connected reductive symmetry groups admit exactly three-level covering towers', 'MA states that '
     'connected reductive symmetry groups admit exactly three-level covering towers, giving n₂ = 3.', 'theorem-supported', 'theorem',
     'Chevalley–Steinberg named at :30; the count read from it is the programme’s (CORPUS_CATALOGOS Theorem 7.4)', None),
    ('MA-04', 'MA', 32, '**Theorem (n₃ = 2).** Every output of a determined entire-function system has exactly two structural scales',
     'MA states that every output of a determined entire-function system has exactly two structural scales, local and global, giving n₃ = 2.',
     'theorem-supported', 'theorem', 'Hadamard factorization and Cartan’s Theorem B named at :32; the count is cited to a programme Theorem 5.1', None),
    ('MA-05', 'MA', 34, '**Theorem (n₄ = 0).** Universal interfaces are spectrally inert.', 'MA states that universal interfaces are spectrally inert, '
     'giving n₄ = 0.', 'theorem-supported', 'theorem', 'Schur’s lemma named at :34; the count is cited to a programme Corollary 6.2', None),
    ('MA-06', 'MA', 45, "Class A's tuple is theorem-forced for every Dedekind zeta function", 'MA states that Class A’s tuple is forced for every '
     'Dedekind zeta function.', 'statement-grade', 'statement', 'cited to FORMATION_UNIVERSALITY_v3 Theorem 1, its argument not in this paper', None),
    ('MA-07', 'MA', 53, 'n_1^{n_3}}{n_2^{n_1+n_3}}', 'MA defines Ω = n₁^{n₃}/n₂^{n₁+n₃} for each class, the numerator counting primitive-accessible '
     'configurations and the denominator the place-assignment phase space.', 'argument-supported', 'argument', 'the counting reading at :55', None),
    ('MA-08', 'MA', 73, 'is a forward derivation with zero free parameters', 'MA states that the chain from ℤ through {2, 3}, the Størmer wall and the '
     'tuple (2, 3, 2, 0) to 4/81 is a forward derivation with zero free parameters.', 'statement-grade', 'statement', 'the formula’s form rests on '
     'the counting reading at :55 and the tuple’s components on cited programme results (:30-:34)', None),
    ('MA-09', 'MA', 85, 'The dark/visible ratio 77/4 = 19.25 matches Planck', 'MA reports the dark-to-visible ratio 77/4 = 19.25 against Planck’s '
     '19.28, within 0.17%.', 'computationally-verified', 'computation', 'recomputed in the claim bank', None),
    ('MA-10', 'MA', 89, 'Cosmic flatness is the algebraic identity of phase-space exhaustion.', 'MA reads cosmic flatness as the identity '
     'Ω_b × 81/4 = 1, consistent with Planck’s Ω_K = −0.0007 ± 0.0019.', 'argument-supported', 'argument', 'the identity at :87, which takes '
     'Ω_b = 4/81 as given', None),
    ('MA-11', 'MA', 99, "By Ostrowski's theorem, ℚ has exactly three places", 'MA states that ℚ has exactly three places by Ostrowski’s theorem, '
     'archimedean, p-adic and a global coherence.', 'statement-grade', 'theorem', 'Ostrowski’s theorem named; it gives the archimedean place and '
     'one p-adic place for each prime p, so the theorem named does not carry the count three', None),
    ('MA-12', 'MA', 101, 'The cosmological visible/dark boundary is the structural boundary', 'MA reads the cosmological visible/dark boundary as the '
     'boundary between primitive-accessible and place-requiring configurations.', 'synthesis-suggested', 'reading', 'a reading at :97-:105', None),
    ('MA-13', 'MA', 111, 'the GL(3, 𝔽₂) orbit decomposition under the parabolic stabilizer', 'MA reads the Hamming-weight partition (3, 3, 1) of the '
     'seven nonzero elements of (ℤ/2)³ as a GL(3, 𝔽₂) orbit decomposition under the stabilizer of the diagonal.', 'statement-grade', 'statement',
     'FA :25 refutes the orbit reading, the diagonal’s stabilizer having order 24 and acting transitively on the six other elements; recomputed '
     'in the claim bank', None),
    ('MA-14', 'MA', 123, '= \\frac{\\Omega_b}{12}', 'MA states that the split decomposition gives Ω_total = 244/243, a flatness deviation of 1/243 = '
     'Ω_b/12.', 'computationally-verified', 'computation', 'the arithmetic at :117-:123, recomputed in the claim bank', None),
    ('MA-15', 'MA', 125, 'a specific cosmological prediction of magnitude Ω_b/12 ≈ 0.41%', 'MA predicts a cosmological component of magnitude '
     'Ω_b/12 ≈ 0.41%.', 'statement-grade', 'statement', 'a prediction', None),
    ('MA-16', 'MA', 127, 'The 1/12 echoes ζ(−1) = −1/12', 'MA reads the 1/12 as echoing ζ(−1) = −1/12 in zeta regularization.', 'synthesis-suggested',
     'reading', 'a reading at :127', None),
    ('MA-17', 'MA', 145, 'Gravity acts on matter; arithmetic determines matter.', 'MA reads matter content as set by ℤ-arithmetic and not by the '
     'gravitational, gauge or probabilistic substrate.', 'synthesis-suggested', 'reading', 'a reading at :143-:147', None),
    ('MA-18', 'MA', 181, '`omega_b_equals_4_over_81` DERIVES the 4/81 arithmetic from the def-carried', 'MA’s era annotation reads '
     'omega_b_equals_4_over_81 at SIDE-omega-b 9c80279 as deriving 4/81 from a tuple carried by definition.', 'kernel-verified', 'terminal',
     'omegab', None),
    ('MA-19', 'MA', 183, 'SIDE-cosmo `c5cba30` — the `xi_*` cluster the same', 'MA’s era annotation reads the xi_* cluster at SIDE-cosmo c5cba30 as '
     'deriving its counts from a tuple carried by definition.', 'kernel-verified', 'terminal', 'cosmo', None),
    ('MA-20', 'MA', 188, 'anchored at its stated sigma regardless of every kernel grade above', 'MA’s era annotation holds the cited density fraction '
     'anchored at its stated σ whatever the kernel grades.', 'statement-grade', 'statement', 'a dated era annotation', None),
    # ---------------------------------------------------------------- STORMER (p2-10)
    ('ST-01', 'ST', 17, 'with zero free parameters and zero physics input', 'ST states that Ω_b = 4/81 = 0.04938 follows from the generators {2, 3} of ℤ '
     'and Størmer’s theorem with zero free parameters, 0.13σ from Planck 2018.', 'statement-grade', 'statement', 'the chain at :21-:27; ST :143 '
     'lists the cosmos as a determined system over ℤ as an assumption, not derived', None),
    ('ST-02', 'ST', 22, 'the consecutive {2, 3}-smooth pairs are exactly (1,2), (2,3), (3,4), (8,9)', 'ST states by Størmer’s theorem that the '
     'consecutive {2, 3}-smooth pairs are exactly (1, 2), (2, 3), (3, 4) and (8, 9), the wall being 9.', 'theorem-supported', 'theorem',
     'Størmer 1897, named; the list recomputed in the claim bank', None),
    ('ST-03', 'ST', 23, '{1, 2, 3, 4, 6, 8, 9} — exactly 7 numbers', 'ST counts seven {2, 3}-smooth numbers up to the wall: 1, 2, 3, 4, 6, 8 and 9.',
     'computationally-verified', 'computation', 'the enumeration, recomputed in the claim bank', None),
    ('ST-04', 'ST', 58, 'This equality is not coincidental', 'ST reads the count 7 as the formation total of ξ(s), and the equality as not coincidental.',
     'synthesis-suggested', 'reading', 'the era annotation at :230-:232 reads the tuple as decomposition-dependent, a modeling premise', None),
    ('ST-05', 'ST', 66, 'wall² = n₂^(n₁+n₃) when n₁ = n₃', 'ST states that wall² = n₂^(n₁+n₃) when n₁ = n₃, 3² × 3² = 81 for (2, 3, 2, 0).',
     'argument-supported', 'argument', 'the derivation at :159-:163, taking the wall as n₂^n₁', None),
    ('ST-06', 'ST', 78, 'Dark = 81 − 4 = 77 = 7 × 11', 'ST writes the dark sector as 81 − 4 = 77 = 7 × 11.', 'computationally-verified', 'computation',
     'arithmetic', None),
    ('ST-07', 'ST', 87, '**The dark sector per formation unit is 11.**', 'ST reads 11, the first prime above the wall, as the dark sector per formation '
     'unit.', 'synthesis-suggested', 'reading', 'a reading at :80-:87', None),
    ('ST-08', 'ST', 93, 'holds **only** for {2, 3}', 'ST reports that among generator pairs of primes up to 13 the formula dark = formation count × '
     'first unreachable prime holds for {2, 3} alone.', 'computationally-verified', 'computation', 'the table at :95-:101, which lists pairs with '
     '2; every pair of primes up to 13 recomputed in the claim bank', None),
    ('ST-09', 'ST', 118, '| Dark/visible = 77/4 | 19.250 | Combined: 19.284 |', 'ST reports dark/visible 77/4 = 19.250 against a combined 19.284 at '
     '0.03σ, and ΔH₀ = 2Ω_bH₀ = 6.65 km/s/Mpc against 6.14 ± 0.97 at 0.53σ.', 'computationally-verified', 'computation', 'the table at :117-:119; '
     'the five datasets are not listed', None),
    ('ST-10', 'ST', 124, 'framework predicts null (κ = 0 for dark sector)', 'ST predicts a null result for direct dark-matter detection and w = −1 for '
     'dark energy.', 'statement-grade', 'statement', 'predictions at :122-:124', None),
    ('ST-11', 'ST', 139, 'the final arithmetic step is **kernel-verified**', 'ST cites the xi_* cluster in SIDE-cosmo’s FormationPhaseSpace.lean for '
     'the final arithmetic step 4/81 = visible/total.', 'statement-grade', 'terminal', 'named without a pin; the names stand at SIDE-cosmo main '
     'c5cba30, :59-:63, and MA :183 names that pin', None),
    ('ST-12', 'ST', 143, '| The cosmos is a determined system over ℤ | **Assumption** (not derived) |', 'ST lists the cosmos as a determined system '
     'over ℤ as an assumption, not derived.', 'statement-grade', 'statement', 'the paper’s own status table', None),
    ('ST-13', 'ST', 145, 'The remaining open step is the structural justification of why total = n₂^(n₁+n₃)', 'ST states that the remaining open step is '
     'the structural justification of total = n₂^(n₁+n₃).', 'statement-grade', 'statement', 'the paper’s own scope; its status table at :142 marks '
     'the same justification as done by Independence and Silence', None),
    ('ST-14', 'ST', 175, 'The product rule for independent selections gives total = n₂^(n₁+n₃).', 'ST argues total = n₂^(n₁+n₃) from Independence '
     'applied to place-assignment, interfaces contributing a factor 1 by Silence.', 'argument-supported', 'argument', 'the argument at :169-:175',
     None),
    ('ST-15', 'ST', 188, 'The cosmos inherits its formation structure from ℤ, not from SU(3) × SU(2) × U(1).', 'ST reads the cosmos as inheriting its '
     'formation structure from ℤ and not from the Standard Model’s gauge group.', 'synthesis-suggested', 'reading', 'a reading at :188', None),
    ('ST-16', 'ST', 223, 'at SIDE-kernel `5e668b4`, `SIDEKernel.formation` and `formation_count` print', 'ST’s era annotation reads '
     'SIDEKernel.formation and formation_count at SIDE-kernel 5e668b4: the sum derives and the tuple enters by definition.', 'kernel-verified',
     'terminal', 'kernel', None),
    ('ST-17', 'ST', 228, 'image, SIDE-trivium `1aac3a9`', 'ST’s era annotation names a derived count for the seven classes, CardDerived at SIDE-trivium '
     '1aac3a9.', 'kernel-verified', 'terminal', 'trivium', None),
    ('ST-18', 'ST', 257, '`SIDEOmegaB.omega_b_equals_4_over_81` exists at `SIDE-omega-b/SIDEOmegaB/Theorem.lean:130`', 'ST’s dated ruling records '
     'omega_b_equals_4_over_81 at SIDE-omega-b 9c80279, Theorem.lean :130, for the final arithmetic step to 4/81.', 'kernel-verified', 'terminal',
     'omegab', None),
    ('ST-19', 'ST', 11, 'name does not exist on disk', 'ST’s v1.0.1 note says the name omega_b_equals_4_over_81 does not exist on disk, a note the dated '
     'ruling at :254-:259 supersedes.', 'statement-grade', 'statement', 'superseded at :254-:259; the name stands at 9c80279', None),
    # ---------------------------------------------------------------- HODGE_CONSERVATION (p2-15)
    ('HC-01', 'HC', 16, 'For RH, the E gap was closed by Conservation of Spectra', 'HC states that for RH the E condition was closed by Conservation of '
     'Spectra, the product formula being s-dark and n₄ = 0.', 'statement-grade', 'statement', 'stated at :16', R1),
    ('HC-02', 'HC', 24, '**Hodge Conservation Theorem.** Every algebraic-geometric structure that exists at codimension p ≥ 2', 'HC states that every '
     'structure present at codimension p ≥ 2 and absent at p = 1 acts on ker(cl) and not on coker(cl).', 'argument-supported', 'argument',
     'the inventory N1–N5 at :36-:74 and the search at :76-:88; HC :125 calls the exhaustiveness one of evidence and search', None),
    ('HC-03', 'HC', 38, 'CH^p(X) is infinite-dimensional in general (Mumford, 1968)', 'HC cites Mumford (1968) for CH^p(X) infinite-dimensional at '
     'p ≥ 2 and reads it as enlarging the domain of cl.', 'theorem-supported', 'theorem', 'Mumford 1968, named', None),
    ('HC-04', 'HC', 46, 'At p = 1: Griff¹(X) = 0 (Lefschetz).', 'HC states that the Griffiths group vanishes at p = 1 and can be nontrivial at p ≥ 2, '
     'citing Lefschetz, Griffiths (1969) and Clemens (1983).', 'theorem-supported', 'theorem', 'the results named at :46', None),
    ('HC-05', 'HC', 48, 'modulo the Abel-Jacobi kernel', 'HC defines the Griffiths group as homologically trivial cycles modulo algebraically trivial '
     'ones, modulo the Abel-Jacobi kernel.', 'statement-grade', 'statement', 'the standard definition is homologically trivial cycles modulo '
     'algebraically trivial ones, with no Abel-Jacobi quotient', None),
    ('HC-06', 'HC', 62, 'is a complex torus that may lack a polarization', 'HC gives the intermediate Jacobian at p ≥ 2 as a complex torus that may lack '
     'a polarization.', 'statement-grade', 'statement', 'a standard definition, stated', None),
    ('HC-07', 'HC', 88, '**No N6 found.** ∎', 'HC reports five candidates for a sixth codimension-dependent structure searched and eliminated.',
     'argument-supported', 'argument', 'the eliminations at :78-:86', None),
    ('HC-08', 'HC', 98, '**Step 3 (Monotonicity).**', 'HC states that the obstructions to surjectivity of cl at p ≥ 2 are a subset of those at p = 1.',
     'statement-grade', 'statement', 'stated at :98, resting on Step 2', None),
    ('HC-09', 'HC', 104, '**The Hodge Conjecture holds.** ∎', 'HC concludes the Hodge Conjecture from five steps, the last the Mechanism Theorem.',
     'argument-supported', 'argument', 'the steps at :94-:102; the caveats at :125-:133 rest the exhaustiveness of N1–N5 on search and name the '
     'Mechanism Theorem a foundational commitment', None),
    ('HC-10', 'HC', 119, 'interfaces between structures are filters', 'HC reads the product formula and the codimension increase as instances of one '
     'principle, interfaces as filters.', 'synthesis-suggested', 'reading', 'the comparison at :110-:117', None),
    ('HC-11', 'HC', 125, 'The claim is supported by evidence and search, not by a classification theorem.', 'HC states that the exhaustiveness of '
     'N1–N5 rests on evidence and search, not on a classification theorem.', 'statement-grade', 'statement', 'the paper’s own caveat', None),
    ('HC-12', 'HC', 127, "Conservation of Spectra's exhaustiveness is proved by Tate's thesis", 'HC credits the exhaustiveness on the RH side to Tate’s '
     'thesis, the classification of all places.', 'statement-grade', 'theorem', 'Tate’s thesis named; the step from it to the exhaustiveness of '
     'the mechanism classes is not argued here', R1),
    ('HC-13', 'HC', 133, 'This is the same foundational commitment as for RH.', 'HC states that its argument uses the Mechanism Theorem, the same '
     'foundational commitment as the RH argument.', 'statement-grade', 'statement', 'the paper’s own caveat', R1),
    ('HC-14', 'HC', 141, "Voisin's counterexamples to the integral Hodge conjecture use torsion.", 'HC states that counterexamples to the integral '
     'Hodge conjecture use torsion and that no rational counterexample has been found.', 'statement-grade', 'statement', 'stated at :141', None),
    ('HC-15', 'HC', 149, 'The standard conjectures are no longer required as the sole path to E closure.', 'HC states that the standard conjectures '
     'become independent validation rather than the sole path to E closure.', 'statement-grade', 'statement', 'stated at :147-:149', None),
    # ---------------------------------------------------------------- PRIME_ORDER (p2-25)
    ('PO-01', 'PO', 11, 'are arithmetic expressions in two and three', 'PO states that the dimensionless constants of physics are arithmetic '
     'expressions in two and three.', 'statement-grade', 'statement', 'the chapter’s claim; PO :99 calls whether two and three must organize the '
     'constants open', None),
    ('PO-02', 'PO', 17, 'Eleven appear in sequence — 5, 7, 11, 13, 17, 19, 29, 31, 41', 'PO states that 2^a + 3^b yields the primes 5 to 41 and then, '
     'past a stretch with no prime, 137 and 337.', 'statement-grade', 'computation', 'an enumeration reported without its range; the claim bank '
     'finds 43 = 2⁴ + 3³, 59, 67, 73, 83, 89, 97, 113 and 131 of that form between 41 and 137', None),
    ('PO-03', 'PO', 19, 'Twenty-three is a difference of powers, 2⁵ − 3².', 'PO states that 23 and 53 are not of the form 2^a + 3^b and enter as '
     '2⁵ − 3² and 2·3³ − 1.', 'computationally-verified', 'computation', 'recomputed in the claim bank', None),
    ('PO-04', 'PO', 25, 'a verification kernel walks the whole set, confirms every element prime', 'PO states that a kernel confirms every element of '
     'its fifteen-prime set prime and that exactly 23 and 53 are not of the form 2^a + 3^b.', 'statement-grade', 'terminal', 'PrimeMosaic.lean '
     'named without a kernel or pin (:57, :107); the file stands at SIDE-constants main, which carries no tag', None),
    ('PO-05', 'PO', 27, 'Each is a Sophie Germain prime', 'PO states that 23 and 53 are Sophie Germain primes, their children 47 and 107 prime.',
     'computationally-verified', 'computation', 'recomputed in the claim bank; :27 and :54 call 47 and 107 the first primes outside the set, '
     'where 37 and 43 are smaller primes outside it', None),
    ('PO-06', 'PO', 29, '(a−1)(b−1) = 2 has the one solution', 'PO states that among coprime pairs at least two only {2, 3} leaves the single integer 1 '
     'unreachable by non-negative combinations.', 'argument-supported', 'argument', 'the equation (a−1)(b−1) = 2 at :29; recomputed in the '
     'claim bank', None),
    ('PO-07', 'PO', 49, '| 337 | 2⁸ + 3⁴ = 16² + 9² | jump prime · terminus |', 'PO writes 337 = 2⁸ + 3⁴ = 16² + 9², a prime, as its terminus.',
     'computationally-verified', 'computation', 'recomputed in the claim bank', None),
    ('PO-08', 'PO', 67, 'Fed the measured α, this is 1.087×10⁻¹²²', 'PO gives the leading term Λ₀ = 11α/12¹¹² = 1.087 × 10⁻¹²² from the measured α, '
     'about one percent from the observed central value.', 'computationally-verified', 'computation', 'recomputed in the claim bank from CODATA α',
     None),
    ('PO-09', 'PO', 75, 'c_5 = -\\tfrac{352}{27} = -8\\,c_1', 'PO states the coefficients c₁ = 44/27, c₃ = 4/9, c₅ = −352/27 = −8c₁, c₆ = −337/27 and '
     'c₁c₃ = 176/243.', 'computationally-verified', 'computation', 'the arithmetic recomputed in the claim bank', None),
    ('PO-10', 'PO', 81, 'It is the closure of a six-coefficient fit', 'PO states that its residual of 2.2 × 10⁻¹⁴ measures the convergence of a '
     'six-coefficient fit to the observed value, not agreement to fourteen places.', 'statement-grade', 'statement', 'the paper’s own scope', None),
    ('PO-11', 'PO', 83, 'is a question neither the arithmetic kernel nor the numerical trace can answer', 'PO states that whether the coefficients’ '
     'simplicity is forced or merely available is open.', 'statement-grade', 'statement', 'the paper’s own scope', None),
    ('PO-12', 'PO', 89, 'The Weinberg angle is 3/13 + α/16 − α²/10', 'PO gives the Weinberg angle 3/13 + α/16 − α²/10, the strong coupling '
     '2/17 + α/29 + α²/50, and the bases 1836 = 12·3²·17, 207 = 3²·23 and 3480 = 2³·3·5·29.', 'computationally-verified', 'computation',
     'the factorizations and values recomputed in the claim bank; the α-series values cited, not formalized (:93)', None),
    ('PO-13', 'PO', 91, 'The anomalies of the mosaic are the numbers of the second-generation lepton.', 'PO reads the two primes outside the sum form, 23 '
     'and 53, as the numbers of the muon.', 'synthesis-suggested', 'reading', 'a reading at :91', None),
    ('PO-14', 'PO', 93, 'a decision procedure cannot evaluate α', 'PO states that the arithmetic of every base and coefficient is checked and the '
     'α-series values are cited and not formalized.', 'statement-grade', 'terminal', 'TerminusParameters.lean named without a pin (:107); it '
     'stands at SIDE-constants main, untagged', None),
    ('PO-15', 'PO', 107, 'The mosaic arithmetic is machine-checked in PrimeMosaic.lean', 'PO names PrimeMosaic.lean, TerminusLambda.lean and '
     'TerminusParameters.lean, with 0 sorry and 0 axioms, and a Python reproduction of the error trace.', 'statement-grade', 'terminal',
     'files named without a kernel or pin; they stand at SIDE-constants main, which carries no tag', None),
    # ---------------------------------------------------------------- FANO_DERIVATION_OF_LAMBDA (p2-30)
    ('FA-01', 'FA', 19, 'The prediction is 0.82σ from observation.', 'FA derives Ω_Λ = 14Ω_b = 56/81 = 0.6914 against Planck’s 0.6854 ± 0.0073, '
     '0.82σ.', 'computationally-verified', 'computation', 'recomputed in the claim bank; the factor 14 from the embedding’s assignment (:117)', None),
    ('FA-02', 'FA', 25, 'It is not a $\\mathrm{GL}(3, \\mathbb{F}_2)$ orbit decomposition', 'FA states that the partition (3, 3, 1) is the Hamming-weight '
     'grading and not a GL(3, 𝔽₂) orbit decomposition, the diagonal’s stabilizer having order 24 and acting transitively on the six other '
     'elements.', 'argument-supported', 'argument', 'the argument at :64; recomputed in the claim bank', None),
    ('FA-03', 'FA', 31, 'kernel-verified in `SIDESubstrateCluster.partition_cardinalities`', 'FA names partition_cardinalities, cyc_weight_invariant, '
     'stab_order_24 and orbit_transitive_on_six as kernel checks of the grading.', 'statement-grade', 'terminal', 'named without a pin; the '
     'names stand at SIDE-substrate-cluster main 2e76426', None),
    ('FA-04', 'FA', 50, '$13.903$ | $14 = 7 \\cdot 2$ | 0.70%', 'FA reports observed Ω_DM/Ω_b = 5.381 against 16/3 and Ω_Λ/Ω_b = 13.903 against 14, '
     'differences of 0.89% and 0.70%.', 'computationally-verified', 'computation', 'recomputed from the Planck values at :41-:43', None),
    ('FA-05', 'FA', 54, 'The difference $58/3 - 77/4 = 1/12$', 'FA states that the two dark-sector decompositions differ by 58/3 − 77/4 = 1/12.',
     'computationally-verified', 'computation', 'recomputed in the claim bank', None),
    ('FA-06', 'FA', 95, 'They receive $w = -1$, the equation of state of a cosmological constant.', 'FA assigns w = −1 to the weight-1 elements as the '
     'farthest from the diagonal and w = 0 to the weight-2 elements.', 'statement-grade', 'statement', 'FA :244 calls the assignment a structural '
     'choice, its first-principles derivation a reach', None),
    ('FA-07', 'FA', 97, 'compatible with the substrate closes to a doubleton', 'FA states that the equation-of-state catalogue closes to a doubleton '
     'by Möbius parity, a sign convention selecting one member.', 'statement-grade', 'terminal', 'catalogue_is_doubleton, M1_tracks_mu and '
     'M2_tracks_neg_mu named without a pin; they stand at SIDE-substrate-cluster main', None),
    ('FA-08', 'FA', 113, 'is kernel-verified at vanilla Lean 4 in `SIDE-residual-bridge v0.1` via `three_weight1_eq_14`', 'FA cites three_weight1_eq_14 '
     'at SIDE-residual-bridge v0.1 for three weight-1 contributions of 14/3 Ω_b summing to 14 Ω_b.', 'kernel-verified', 'terminal', 'bridge', None),
    ('FA-09', 'FA', 131, '\\frac{4}{81} \\cdot \\frac{61}{3} = \\frac{244}{243}', 'FA gives Ω_total = 244/243 in the split decomposition, a flatness '
     'deviation of 1/243 = Ω_b/12 ≈ 0.41%.', 'computationally-verified', 'computation', 'recomputed in the claim bank', None),
    ('FA-10', 'FA', 141, 'This is a falsifiable sub-percent prediction.', 'FA states the deviation Ω_b/12 as a falsifiable prediction within reach of '
     'coming CMB surveys.', 'statement-grade', 'statement', 'a prediction', None),
    ('FA-11', 'FA', 143, 'is kernel-verified at vanilla Lean 4 in `SIDE-residual-bridge`, each theorem closed by `decide`', 'FA names a ten-theorem '
     'chain in SIDE-residual-bridge, from three_weight1_eq_14 to omegaLambda_mu_shifted.', 'statement-grade', 'terminal', 'named without a pin; '
     'six of the ten stand at the tag v0.1 cited at :113 and all ten at main 5aa5ab7', None),
    ('FA-12', 'FA', 145, 'this is a $1.38\\sigma$ offset', 'FA states that carrying the diagonal into the dark-energy sector gives Ω_Λ = 169/243 ≈ 0.6955, '
     '1.38σ from Planck.', 'computationally-verified', 'computation', 'recomputed in the claim bank', None),
    ('FA-13', 'FA', 155, 'Deviation 0.49σ.', 'FA gives Ω_DM = 64/243 ≈ 0.2634 against Planck’s 0.2653 ± 0.0039, 0.49σ.', 'computationally-verified',
     'computation', 'recomputed in the claim bank', None),
    ('FA-14', 'FA', 157, 'the substrate derivation produces flatness as an arithmetic consequence of the partition structure', 'FA reads cosmic '
     'flatness in the uniform decomposition, (4/81)(81/4) = 1, as an arithmetic consequence of the partition.', 'argument-supported', 'argument',
     'the identity at :157, which takes Ω_b = 4/81 as given', None),
    ('FA-15', 'FA', 161, 'A positive detection at any nonzero gauge charge refutes the framework.', 'FA predicts no direct dark-matter detection through '
     'a Standard Model gauge coupling.', 'statement-grade', 'statement', 'a prediction', None),
    ('FA-16', 'FA', 183, 'The substrate is the source.', 'FA reads ξ(s) and the cosmological energy budget as inheriting their structure from (ℤ/2)³.',
     'synthesis-suggested', 'reading', 'a reading at :181-:183', None),
    ('FA-17', 'FA', 193, '\\Lambda = \\frac{11 \\alpha}{12^{11/2}}', 'FA records a heritage formula for Λ, 11α/12^{11/2} times a series less 337α⁶/27, '
     'and routes its own Λ through Ω_Λ = 14Ω_b.', 'statement-grade', 'statement', 'the heritage note at :187-:199; 11α/12^{11/2} ≈ 9.3 × 10⁻⁸ in '
     'the claim bank, not of order 10⁻¹²², where PO :65 writes 12¹¹²', None),
    ('FA-18', 'FA', 244, 'is a structural choice that matches observation', 'FA states that the equation-of-state assignment is a structural choice whose '
     'first-principles derivation is a reach.', 'statement-grade', 'statement', 'the paper’s own scope', None),
    ('FA-19', 'FA', 248, 'the connection has not been established beyond magnitude coincidence', 'FA states that the link between its 1/12 and '
     'ζ(−1) = −1/12 stands at magnitude alone.', 'statement-grade', 'statement', 'the paper’s own scope', None),
    # ---------------------------------------------------------------- YANG_MILLS_MONOGRAPH (p2-31)
    ('YM-01', 'YM', 14, '**What is compiled:** the **SIDE-Exclusion form** and the **four-sector enumeration**', 'YM states that what compiles is the '
     'exclusion form and the four-sector enumeration, its formation placement a scaffolding over stipulated data.', 'statement-grade', 'terminal',
     'the kernels named by repository at :14; their pins at :405', None),
    ('YM-02', 'YM', 15, '**What is open:** the **physical gap Δ > 0 (the Clay theorem)**', 'YM states that the physical Yang-Mills mass gap Δ > 0 is '
     'open, per-sector positivity entering by definition.', 'statement-grade', 'statement', 'the paper’s own claim-status note', None),
    ('YM-03', 'YM', 16, 'turns on assigning **quantization as a third primitive class**', 'YM states that its count (3, 3, 2, 0) = 8 against ξ’s 7 '
     'turns on quantization as a third primitive class, a decomposition choice.', 'statement-grade', 'statement', 'the paper’s own claim-status '
     'note', None),
    ('YM-04', 'YM', 17, 'classifies YM **in-method (TYPE II)**', 'YM states that the E-Difficulty skeleton classifies Yang-Mills TYPE II, at '
     'manuscript level until W-6 discharges.', 'statement-grade', 'statement', 'the paper’s own claim-status note', None),
    ('YM-05', 'YM', 49, 'The classification is complete by Bott periodicity', 'YM states that every spectral contribution lies in one of four '
     'topological sectors, a classification complete by Bott periodicity and a codimension constraint.', 'argument-supported', 'argument',
     'the argument at :108-:118', None),
    ('YM-06', 'YM', 103, '| Vortex | π₁(Z(SU(N))) = ℤ_N | Center charge |', 'YM classifies the vortex sector by π₁ of the center Z(SU(N)), given as '
     'ℤ_N.', 'statement-grade', 'statement', 'the center is discrete, so π₁ of it is trivial; center vortices are classed by π₁(SU(N)/ℤ_N) = ℤ_N',
     None),
    ('YM-07', 'YM', 118, 'The homotopy groups of SU(N) are completely computed (Bott periodicity theorem).', 'YM states that the homotopy groups of '
     'SU(N) are completely computed by Bott periodicity.', 'statement-grade', 'theorem', 'Bott periodicity named; it computes the stable '
     'homotopy groups, πₖ(SU(N)) for k < 2N, not every homotopy group', None),
    ('YM-08', 'YM', 141, 'Each entry is a known result of quantum field theory.', 'YM assigns each sector its mechanism for Δ > 0: asymptotic freedom, '
     'the gluon condensate, string tension and the dual Meissner effect.', 'statement-grade', 'theorem', 'the mechanisms named with their '
     'literature (:136-:139, :321); that each yields Δ > 0 is the per-sector positivity the paper enters by definition (:15)', None),
    ('YM-09', 'YM', 152, 'Asymptotic freedom proves β(g) < 0 for all g > 0', 'YM excludes four candidate mechanisms for Δ = 0.', 'argument-supported',
     'argument', 'the table at :147-:152', None),
    ('YM-10', 'YM', 165, 'under the per-sector positivity that is entered as a placeholder', 'YM concludes Δ > 0 at the level of the exclusion form, '
     'under per-sector positivity entered as a placeholder.', 'statement-grade', 'statement', 'the paper’s re-scoped conclusion', None),
    ('YM-11', 'YM', 195, 'which corresponds to **quantization itself**', 'YM reads the origin of AG(3, 𝔽₂), absent from PG(2, 𝔽₂), as quantization.',
     'synthesis-suggested', 'reading', 'a reading; :199 calls the count a decomposition choice', None),
    ('YM-12', 'YM', 207, 'Yang-Mills produces a formation-block code with parameters [[8, 1, 5]]', 'YM states code parameters [[8, 1, 5]] under '
     'formation-block errors and [[8, 1, 3]] per component, a subcode of the CSS code [[8, 3, 3]] from the extended Hamming code [8, 4, 4].',
     'argument-supported', 'argument', 'the derivation at :211-:229; the era annotation at :440-:443 grades the parameters as subcode derivations, '
     'not an independent Knill–Laflamme run', None),
    ('YM-13', 'YM', 221, 'the effective distance under formation-block errors equals exactly 2S − 1', 'YM states the Tightness Theorem, d_eff = 2S − 1 '
     'for rank-1 codespaces, giving d_eff = 5 at S = 3.', 'statement-grade', 'statement', 'cited to the formation calculus, not argued here', None),
    ('YM-14', 'YM', 251, 'Lattice QCD predicts the lightest glueball state', 'YM cites the lightest glueball at 1.73 ± 0.09 GeV, a string tension near '
     '0.19 GeV² and deconfinement near 155 MeV as experimental anchors for Δ > 0.', 'computationally-verified', 'computation', 'lattice '
     'computations and measurements, cited at :251-:261', None),
    ('YM-15', 'YM', 298, 'theorem mass_gap : ¬Massless := by', 'YM prints its kernel code: `gapped` True on four sectors, mass_gap : ¬Massless, and '
     'sectors_complete.', 'statement-grade', 'terminal', 'the code quoted at :277-:311 without a pin; YM :405 names the pins', None),
    ('YM-16', 'YM', 315, 'is the *form* of the exclusion, not a derivation from Yang-Mills dynamics', 'YM states that the kernel checks the exclusion '
     'syllogism and the sector enumeration, not the physical mass gap.', 'statement-grade', 'statement', 'the paper’s own scope', None),
    ('YM-17', 'YM', 323, 'is the same as the structure of the Riemann hypothesis', 'YM states that its architecture, a verified surround and a manuscript '
     'criterion, is that of the RH argument, kernel arithmetic the surround and the manuscript’s Ostrowski the criterion.', 'statement-grade',
     'statement', 'stated at :323', R2),
    ('YM-18', 'YM', 341, 'establishes that the mass gap exists by SIDE exclusion', 'YM’s reaches say the structural argument establishes that the mass '
     'gap exists, a constructive argument remaining.', 'statement-grade', 'statement', 'stated at :341, beside the claim-status note at :15 that calls '
     'the physical mass gap open', None),
    ('YM-19', 'YM', 371, 'not the physical mass-gap theorem itself', 'YM states that it supplies the structural form and constraint of the Clay '
     'deliverable, not the mass-gap theorem.', 'statement-grade', 'statement', 'the paper’s re-scoped context note', None),
    ('YM-20', 'YM', 405, 'pins `c66f3c5` / `a27415d`', 'YM cites SIDE-effects Structural.lean at c66f3c5 and a27415d for the mass_gap placeholder, '
     '`gapped` True on each sector, retired at the later pin.', 'kernel-verified', 'terminal', 'effects', None),
    ('YM-21', 'YM', 405, '`SIDE-yang-mills-formation` v0.1.1 = `73e9e2c`', 'YM cites SIDE-yang-mills-formation v0.1.1 = 73e9e2c as a formation-level '
     'placement skeleton over stipulated data.', 'kernel-verified', 'terminal', 'ymf', None),
    ('YM-22', 'YM', 442, 'subcode-derivations under the formation-block model', 'YM’s era annotation grades its code parameters as subcode derivations, '
     'not an independent Knill–Laflamme run.', 'statement-grade', 'statement', 'a dated era annotation', None),
    # ---------------------------------------------------------------- UNIFICATION_OF_FORCES (p2-26, heritage)
    ('UF-01', 'UF', 24, 'the forces are unified **arithmetically**', 'UF states that the forces are unified arithmetically, in the prime structure of '
     'their constants.', 'statement-grade', 'statement', 'REGISTRY :276 files the paper DEFUNCT, its framing retired', None),
    ('UF-02', 'UF', 36, 'spans from t₄₆ = 134.757 to t₄₇ = 138.116', 'UF places m_π⁰ = 134.98 MeV, α⁻¹ = 137.036, m_t/m_c = 135.98 and '
     '100·m_H/m_Z = 137.35 between the 46th and 47th ordinates of ζ’s zeros, 134.757 and 138.116.', 'computationally-verified', 'computation',
     'the ordinates recomputed in the claim bank', None),
    ('UF-03', 'UF', 60, '\\alpha^{-1} = 137.036 = t_{46} + \\frac{19}{28}', 'UF writes α⁻¹ = t₄₆ + (19/28)(t₄₇ − t₄₆).', 'computationally-verified',
     'computation', 'recomputed in the claim bank', None),
    ('UF-04', 'UF', 88, 'is a **unification hub**', 'UF reads the interval between the 46th and 47th ordinates as a unification hub.',
     'synthesis-suggested', 'reading', 'a reading at :86-:88', None),
    ('UF-05', 'UF', 157, '66.74 = t_{15} + \\frac{1370}{1653}', 'UF writes G × 10¹² = 66.74 = t₁₅ + (1370/1653)(t₁₆ − t₁₅), with 1370 = 2 × 5 × 137.',
     'computationally-verified', 'computation', 'recomputed in the claim bank', None),
    ('UF-06', 'UF', 174, '**The prime factorization is forced**', 'UF reads the 137 in 1370 as forced and not numerology.', 'statement-grade',
     'statement', 'stated at :167-:176', None),
    ('UF-07', 'UF', 211, 'q - p = 289 - 152 = 137', 'UF writes the weak mixing angle’s interpolation as 152/289, with q − p = 137.',
     'computationally-verified', 'computation', 'recomputed in the claim bank', None),
    ('UF-08', 'UF', 383, '137 = 2^7 + 3^2 = 128 + 9', 'UF writes 137 = 2⁷ + 3² and 337 = 2⁸ + 3⁴ and reads them as twinned.',
     'computationally-verified', 'computation', 'arithmetic; the twinning a reading', None),
    ('UF-09', 'UF', 517, '**The gauge structure GUARANTEES P-factored physics.**', 'UF states that the gauge structure guarantees P-factored physics '
     'through the spectral action and zeta regularization.', 'statement-grade', 'statement', 'the pathway at :498-:515, stated without derivation',
     None),
    ('UF-10', 'UF', 575, '**Fine-tuning is dissolved**', 'UF states fine-tuning, the hierarchy problem and the cosmological-constant problem dissolved.',
     'statement-grade', 'statement', 'stated at :561-:654', None),
    ('UF-11', 'UF', 644, '\\Lambda = \\frac{11\\alpha}{12^{11/2}}', 'UF gives its TERMINUS formula for Λ, 11α/12^{11/2} times a series less 337α⁶/27.',
     'statement-grade', 'statement', '11α/12^{11/2} ≈ 9.3 × 10⁻⁸ in the claim bank, not of order 10⁻¹²², where PO :65 writes 12¹¹²', None),
    ('UF-12', 'UF', 695, 'Gap 202 = 2 × 101, and 101 ∉ P.', 'UF predicts 6H₀ absent from cosmological data, its index 202 = 2 × 101 with 101 outside '
     'its prime set.', 'statement-grade', 'statement', 'a prediction', None),
    ('UF-13', 'UF', 719, 'After testing 122 constants across 27 orders of magnitude', 'UF reports 122 constants tested with no failure.',
     'statement-grade', 'statement', 'reported without the data', None),
    ('UF-14', 'UF', 797, 'is consciousness a prime-detection system?', 'UF asks whether consciousness is a prime-detection system.', 'statement-grade',
     'statement', 'speculation, so marked at :806', None),
    ('UF-15', 'UF', 893, 'P < 10⁻³⁶⁶', 'UF states a probability below 10⁻³⁶⁶ against its pattern arising by chance.', 'statement-grade', 'statement',
     'stated without its computation', None),
]

ROUTE_ROWS = {'RH-60': 'DARK, test 2'}
SIEVE = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md'


def g(repo, *a):
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


def kv_reason(c):
    """### a kernel-verified row's reason: its pin, its resolution and the statements read there"""
    k = c[7]
    repo, pin, _w, _where = PINS[k]
    reads = [v for v in KREADS.values() if v[0] == k] + ([v for v in KREADS.values() if v[0] == 'effects2'] if k == 'effects' else [])
    st = pin_state(k)
    return '%s %s = commit %s, %s: %s' % (repo, pin, st[3], st[4] or 'NOT AT THE REMOTE', '; '.join('%s %s' % (r[1], r[4]) for r in reads))


def claims():
    """### the claims with each kernel-verified row's reason filled from its pin"""
    return [c if c[5] != 'kernel-verified' else c[:7] + (kv_reason(c),) + c[8:] for c in C]


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
    repo, pin, want, _where = PINS[key]
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


def resolve_kernel():
    """### every kernel read at its pin: [(key, ok, line)]"""
    out = []
    for k, (pk, f, n, needle, _what) in KREADS.items():
        repo, pin, _w, _where = PINS[pk]
        ls = lines_of(show(f, pin, 'D:/' + repo))
        l = ls[n - 1] if 0 < n <= len(ls) else ''
        out.append((k, needle in l, l))
    return out


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
        return bool(st[3]) and bool(st[4]) and all(kr[k] for k, v in KREADS.items() if v[0] == c[7] or (c[7] == 'effects' and v[0] == 'effects2'))
    return True


# ================================================================================ THE CLAIM BANK'S ARITHMETIC
def _smooth(n, ps):
    for p in ps:
        while n % p == 0 and n > 1:
            n //= p
    return n == 1


def _is_prime(n):
    return n > 1 and all(n % d for d in range(2, int(n ** 0.5) + 1))


def arith2d():
    """### the cluster's arithmetic recomputed: [(label, value, the paper's figure, agrees)]"""
    import mpmath
    mpmath.mp.dps = 30
    ob, sb = 0.04930, 0.00066
    A = []
    sig = {k: abs(float(v) - ob) / sb for k, v in (('A', Fr(4, 81)), ('B', Fr(9, 32)), ('C', Fr(1, 27)), ('D', Fr(1, 4)))}
    A.append(('MA :68-:71 σ-distances A, B, C, D', '%.2f, %.1f, %.1f, %.1f' % (sig['A'], sig['B'], sig['C'], sig['D']), '0.13, 351, 18.6, 304',
              round(sig['A'], 2) == 0.13 and round(sig['B']) == 351 and round(sig['C'], 1) == 18.6 and round(sig['D']) == 304))
    pr = (0.2653 + 0.6854) / ob
    A.append(('MA :85 Planck (Ω_DM + Ω_Λ)/Ω_b and 77/4 against it', '%.3f ; %.2f%%' % (pr, 100 * (pr - 19.25) / pr), '19.28 ; 0.17%',
              round(pr, 2) == 19.28 and round(100 * (pr - 19.25) / pr, 2) in (0.17, 0.18)))
    tot = Fr(4, 81) * (1 + Fr(58, 3))
    A.append(('MA :119-:123 and FA :131-:137 Ω_b(1 + 58/3), its excess over 1, Ω_b/12', '%s ; %s ; %s' % (tot, tot - 1, Fr(4, 81) / 12), '244/243 ; 1/243 ; 1/243',
              tot == Fr(244, 243) and tot - 1 == Fr(4, 81) / 12))
    pairs = [(n, n + 1) for n in range(1, 10 ** 6) if _smooth(n, (2, 3)) and _smooth(n + 1, (2, 3))]
    A.append(('ST :22 consecutive {2,3}-smooth pairs below 10⁶', str(pairs), '(1,2), (2,3), (3,4), (8,9)', pairs == [(1, 2), (2, 3), (3, 4), (8, 9)]))
    sm = [n for n in range(1, 10) if _smooth(n, (2, 3))]
    A.append(('ST :23 {2,3}-smooth numbers up to 9', str(sm), '{1, 2, 3, 4, 6, 8, 9}', sm == [1, 2, 3, 4, 6, 8, 9]))
    rows, match = [], []
    for p in (2, 3, 5, 7, 11, 13):
        for q in (2, 3, 5, 7, 11, 13):
            if q <= p:
                continue
            cp = [(n, n + 1) for n in range(1, 10 ** 5) if _smooth(n, (p, q)) and _smooth(n + 1, (p, q))]
            wall = max(x for pr_ in cp for x in pr_) if cp else 1
            fc = sum(1 for n in range(1, wall + 1) if _smooth(n, (p, q)))
            nxt = next(r for r in range(wall + 1, 10 ** 4) if _is_prime(r) and not _smooth(r, (p, q)))
            dark = wall ** 2 - p ** 2
            rows.append('{%d,%d}: wall %d, total %d, visible %d, dark %d, FC %d, first prime %d, FC×prime %d' % (p, q, wall, wall ** 2, p ** 2, dark, fc, nxt, fc * nxt))
            if dark == fc * nxt:
                match.append((p, q))
    A.append(('ST :93-:101 every pair of primes up to 13: dark = wall² − p₁² against FC × first non-smooth prime above the wall', '; '.join(rows),
              'only {2, 3}', match == [(2, 3)]))
    sums = sorted(set(2 ** a + 3 ** b for a in range(0, 12) for b in range(0, 8)))
    sp = [n for n in sums if _is_prime(n) and n <= 337]
    between = [n for n in sp if 41 < n < 137]
    A.append(('PO :17 primes of the form 2^a + 3^b (a, b ≥ 0) up to 337', str(sp), '5, 7, 11, 13, 17, 19, 29, 31, 41, then 137 and 337',
              not between))
    A.append(('PO :19 23 and 53 of the form 2^a + 3^b ; 2⁵ − 3², 2·3³ − 1', '%s, %s ; %d, %d' % (23 in sums, 53 in sums, 2 ** 5 - 9, 2 * 27 - 1),
              'neither ; 23, 53', 23 not in sums and 53 not in sums and 2 ** 5 - 9 == 23 and 2 * 27 - 1 == 53))
    P15 = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 53, 137, 337)
    outside = [n for n in range(2, 47) if _is_prime(n) and n not in P15]
    A.append(('PO :27 2·23+1 and 2·53+1 prime', '%s, %s' % (_is_prime(47), _is_prime(107)), '47 and 107 prime', _is_prime(47) and _is_prime(107)))
    A.append(('PO :27, :54 the primes below 47 outside the set', str(outside), '47 and 107 "the first primes outside the Core"', not outside))
    sol = [(a, b) for a in range(2, 50) for b in range(a + 1, 50) if math.gcd(a, b) == 1 and (a - 1) * (b - 1) // 2 == 1]
    A.append(('PO :29 coprime pairs 2 ≤ a < b < 50 leaving exactly one unreachable integer', str(sol), '{2, 3} alone', sol == [(2, 3)]))
    A.append(('PO :49, UF :383-:384 337 = 2⁸ + 3⁴ = 16² + 9², prime ; 137 = 2⁷ + 3²', '%s ; %s' % (2 ** 8 + 81 == 337 == 16 ** 2 + 81 and _is_prime(337), 128 + 9 == 137),
              'yes ; yes', 2 ** 8 + 81 == 337 and _is_prime(337) and 128 + 9 == 137))
    al = mpmath.mpf('0.0072973525643')
    lam0 = 11 * al / mpmath.mpf(12) ** 112
    A.append(('PO :65-:67 11α/12¹¹² (CODATA 2018 α)', mpmath.nstr(lam0, 4), '1.087×10⁻¹²²', abs(lam0 / mpmath.mpf('1.087e-122') - 1) < 0.001))
    her = 11 * al / mpmath.mpf(12) ** mpmath.mpf(5.5)
    A.append(('FA :193, UF :644 11α/12^{11/2}', mpmath.nstr(her, 4), 'of order 10⁻¹²² by UF :640-:641', her < 1e-100))
    c1, c3 = Fr(44, 27), Fr(4, 9)
    A.append(('PO :75 coefficients: 44 = 2²·11 ; −8c₁ ; c₁c₃', '%s ; %s ; %s' % (44 == 4 * 11, -8 * c1, c1 * c3), '; −352/27 ; 176/243 = 2⁴·11/3⁵',
              -8 * c1 == Fr(-352, 27) and c1 * c3 == Fr(176, 243) and 176 == 16 * 11 and 243 == 3 ** 5))
    wa = 3 / 13 + float(al) / 16 - float(al) ** 2 / 10
    sa = 2 / 17 + float(al) / 29 + float(al) ** 2 / 50
    A.append(('PO :89 3/13 + α/16 − α²/10 ; 2/17 + α/29 + α²/50 ; 1836, 207, 3480', '%.5f ; %.5f ; %s %s %s' % (wa, sa, 12 * 9 * 17, 9 * 23, 8 * 3 * 5 * 29),
              'the Weinberg angle and α_s ; 12·3²·17, 3²·23, 2³·3·5·29', 12 * 9 * 17 == 1836 and 9 * 23 == 207 and 8 * 3 * 5 * 29 == 3480))
    s = [(0.6854, 0.0073, Fr(56, 81), 0.82, 'FA :19 Ω_Λ = 56/81'), (0.2653, 0.0039, Fr(64, 243), 0.49, 'FA :155 Ω_DM = 64/243'),
         (0.6854, 0.0073, Fr(169, 243), 1.38, 'FA :145 Ω_Λ = 169/243')]
    for obs, err, v, paper, lab in s:
        d = abs(float(v) - obs) / err
        A.append(('%s against Planck' % lab, '%.4f, %.2fσ' % (float(v), d), '%.2fσ' % paper, round(d, 2) == paper))
    r1, r2 = 0.2653 / ob, 0.6854 / ob
    A.append(('FA :49-:50 Ω_DM/Ω_b, Ω_Λ/Ω_b and their differences from 16/3, 14', '%.3f, %.3f ; %.2f%%, %.2f%%' % (r1, r2, 100 * (r1 - 16 / 3) / r1, 100 * (14 - r2) / r2),
              '5.381, 13.903 ; 0.89%, 0.70%', round(r1, 3) == 5.381 and round(r2, 3) == 13.903))
    A.append(('FA :54, :127 58/3 − 77/4', str(Fr(58, 3) - Fr(77, 4)), '1/12', Fr(58, 3) - Fr(77, 4) == Fr(1, 12)))
    # ### the stabilizer of the diagonal in GL(3, F2), its order and its orbits on the six other nonzero vectors
    import itertools
    vecs = [v for v in itertools.product((0, 1), repeat=3) if any(v)]
    mats = [m for m in itertools.product(vecs, repeat=3)]

    def ap(m, v):
        return tuple(sum(m[j][i] * v[j] for j in range(3)) % 2 for i in range(3))
    gl = [m for m in mats if len(set(ap(m, v) for v in vecs)) == 7]
    stab = [m for m in gl if ap(m, (1, 1, 1)) == (1, 1, 1)]
    orb = set(ap(m, (1, 0, 0)) for m in stab)
    A.append(('MA :111, FA :25 |GL(3, 𝔽₂)|, the diagonal’s stabilizer, the orbit of (1,0,0) under it', '%d, %d, %d' % (len(gl), len(stab), len(orb)),
              '168, 24, 6 (FA) ; an orbit decomposition (3, 3, 1) (MA)', len(gl) == 168 and len(stab) == 24 and len(orb) == 6))
    t = [mpmath.im(mpmath.zetazero(k)) for k in (15, 16, 46, 47, 2, 3)]
    A.append(('UF :36 the 46th and 47th ordinates', '%s, %s' % (mpmath.nstr(t[2], 7), mpmath.nstr(t[3], 7)), '134.757, 138.116',
              abs(t[2] - mpmath.mpf('134.757')) < 0.001 and abs(t[3] - mpmath.mpf('138.116')) < 0.001))
    a_ = t[2] + mpmath.mpf(19) / 28 * (t[3] - t[2])
    g_ = t[0] + mpmath.mpf(1370) / 1653 * (t[1] - t[0])
    w_ = t[4] + mpmath.mpf(152) / 289 * (t[5] - t[4])
    A.append(('UF :60, :157, :208 t₄₆ + (19/28)Δ ; t₁₅ + (1370/1653)Δ ; t₂ + (152/289)Δ', '%s ; %s ; %s' % (mpmath.nstr(a_, 7), mpmath.nstr(g_, 6), mpmath.nstr(w_, 6)),
              '137.036 ; 66.74 ; 23.12', abs(a_ - 137.036) < 0.01 and abs(g_ - 66.74) < 0.01 and abs(w_ - 23.12) < 0.01))
    A.append(('UF :160-:161, :220 1370 = 2 × 5 × 137, 1653 = 3 × 19 × 29, 289 − 152', '%d, %d, %d' % (2 * 5 * 137, 3 * 19 * 29, 289 - 152), '1370, 1653, 137',
              2 * 5 * 137 == 1370 and 3 * 19 * 29 == 1653 and 289 - 152 == 137))
    A.append(('CS :22 10^0.49', '%.3f' % (10 ** 0.49), '3.1', round(10 ** 0.49, 1) == 3.1))
    return A


def main():
    rc = resolve_claims()
    bad = [x for x in rc if not x[1]]
    print('### claims %d ; needles failing %s' % (len(C), [(i, l[:90]) for i, _o, l in bad] or 'NONE'))
    for k in PINS:
        print('### pin %s' % (pin_state(k),))
    kb = [x for x in resolve_kernel() if not x[1]]
    print('### kernel reads %d ; failing %s' % (len(KREADS), [(k, l[:90]) for k, _o, l in kb] or 'NONE'))
    for k in UNPINNED:
        print('### unpinned %s' % (unpinned_state(k)[:7],))
    print('### grades out of rule: %s' % ([c[0] for c in C if not grade_ok(c)] or 'NONE'))
    print('### routes: %s' % [(c[0], c[8][0], c[8][1], c[8][2], c[8][5]) for c in C if c[8]])
    print('### sieve rows: %s' % sieve_rows())
    from collections import Counter
    print('### grade counts: %s' % dict(Counter(c[5] for c in C)))
    print('### ids unique: %s' % (len(set(c[0] for c in C)) == len(C)))
    if '--arith' in sys.argv:
        for a in arith2d():
            print('### %s -- %s ; the paper: %s ; agrees %s' % (a[0], a[1][:300], a[2], a[3]))


if __name__ == '__main__':
    main()
