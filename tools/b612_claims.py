# -*- coding: utf-8 -*-
"""b612_claims.py -- THE ACT'S DATA AND ITS RESOLVERS, UNDER (R222)(3): THE CLAIMS OF CLUSTER 1.5E'S SIX PAPERS.

### Every claim is the seat's one-sentence restatement of a paper's sentence, carried with a needle that must occur on the cited line of the
### paper at PLACE-papers a79215a; its grade is the one the paper's own text supports, in the vocabulary of (R19) as (R220)(5) lists it:
### kernel-verified at a pin; theorem-supported; argument-supported; computationally-verified; synthesis-suggested; statement-grade.
### THE GRADING RULE, confirmed by (R222)(1): kernel-verified only where the paper names a terminal (or its file) at a pin and the
### statement read at that pin carries the claim; theorem-supported only where the paper names a theorem of the literature for it;
### computationally-verified only where the paper reports a computation; argument-supported where the paper's text argues the claim;
### synthesis-suggested where it reads a pattern across results; statement-grade where it states without argument. No grade is above the
### paper's own support. A ROUTE is a claim offered as an argument toward RH, simplicity or the open clause; each is read through the
### sieve's five tests in order. A pin RESOLVES when its commit is in the clone and at the remote (a remote tag peeling to it, or the
### remote main containing it). This module writes nothing: `python tools/b612_claims.py` runs the resolvers and prints.
"""
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = 'a79215a'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PAPERS = {
    'CO': ('phase1.5/deep-structure/CONSTANCE.md', '1.5e-1', 191),
    'FR': ('phase1.5/deep-structure/FROBENIUS.md', '1.5e-2', 192),
    'TR': ('phase1.5/deep-structure/TRIVIUM.md', '1.5e-3', 193),
    'TF': ('phase1.5/deep-structure/TRIVIUM_FINDINGS.md', '1.5e-4', 194),
    'TS': ('phase1.5/deep-structure/TRIVIUM_IDENTITY_SUBSPACE.md', '1.5e-5', 195),
    'CN': ('phase1.5/deep-structure/CLASS_NUMBER_ANOMALY.md', '1.5e-6', 196),
}
GRADES = ('kernel-verified', 'theorem-supported', 'argument-supported', 'computationally-verified', 'synthesis-suggested', 'statement-grade')
NEEDS = {'kernel-verified': ('terminal',), 'theorem-supported': ('theorem', 'terminal'), 'computationally-verified': ('computation',),
         'argument-supported': ('argument', 'theorem', 'terminal', 'computation'), 'synthesis-suggested': ('argument', 'theorem', 'terminal',
                                                                                                        'computation', 'reading', 'statement'),
         'statement-grade': ('argument', 'theorem', 'terminal', 'computation', 'reading', 'statement')}

# ### the kernel pins the papers name: key -> (repo, the pin as the paper cites it, the commit it must peel to)
PINS = {
    'frobenius': ('SIDE-frobenius', 'v0.1.0', '2efe9f2'),
    'cna': ('SIDE-class-number-anomaly', 'v0.2', '2203b88a'),
    'mod24': ('SIDE-dirichlet-mod-24', 'v0.1.0', '597b0869'),
    'substrate': ('SIDE-substrate-cluster', 'v0.4', '06b61c3'),
    'bij01': ('SIDE-bijection', 'v0.1', 'dd487e6'),
    'bij020': ('SIDE-bijection', 'v0.2.0', 'a26f6f1'),
    'trivium': ('SIDE-trivium', '1df5bad4', '1df5bad4'),
    'spinor': ('SIDE-spinor', 'v0.1.0', 'b235bc6'),
}
# ### the kernel reads: key -> (pin key, file, line, needle on that line, what the statement says)
KREADS = {
    'g23': ('frobenius', 'SIDEFrobenius/Indicial.lean', 65, 'theorem g_two_three : frobenius_number 2 3 = 1',
            '`SIDEFrobenius.g_two_three : frobenius_number 2 3 = 1`, where frobenius_number a b = a·b − a − b (:63)'),
    'g23min': ('frobenius', 'SIDEFrobenius/Indicial.lean', 68, 'theorem g_two_three_minimal (a b : ℤ)',
               '`SIDEFrobenius.g_two_three_minimal`: for integers 2 ≤ a < b with (a, b) ≠ (2, 3), 2 ≤ frobenius_number a b (:68-:70)'),
    'g23min_stmt': ('frobenius', 'SIDEFrobenius/Indicial.lean', 70, '2 ≤ frobenius_number a b', 'its conclusion'),
    'ind_factor': ('frobenius', 'SIDEFrobenius/Indicial.lean', 29, 'theorem indicial_factor (r : ℚ) : r ^ 2 + r + 1 / 4 = (r + 1 / 2) ^ 2',
                   '`SIDEFrobenius.indicial_factor (r : ℚ) : r² + r + 1/4 = (r + 1/2)²`'),
    'ind_unique': ('frobenius', 'SIDEFrobenius/Indicial.lean', 33, 'r ^ 2 + r + 1 / 4 = 0 ↔ r = -1 / 2',
                   '`SIDEFrobenius.indicial_root_unique (r : ℚ) : r² + r + 1/4 = 0 ↔ r = −1/2` (:32-:33)'),
    'ind_half': ('frobenius', 'SIDEFrobenius/Indicial.lean', 54, 'theorem indicial_forces_half (r : ℚ) (h : r ^ 2 + r + 1 / 4 = 0) :',
                 '`SIDEFrobenius.indicial_forces_half`: from r² + r + 1/4 = 0, −r = 1/2 (:54-:55)'),
    'S_sq': ('frobenius', 'SIDEFrobenius/Indicial.lean', 95, 'theorem S_squared : Smat * Smat = -1 := by',
             '`SIDEFrobenius.S_squared : Smat * Smat = -1`, S = !![0, -1; 1, 0] over ℤ (:91)'),
    'ST_cu': ('frobenius', 'SIDEFrobenius/Indicial.lean', 98, 'theorem ST_cubed : (Smat * Tmat) ^ 3 = -1 := by',
              '`SIDEFrobenius.ST_cubed : (Smat * Tmat) ^ 3 = -1`, T = !![1, 1; 0, 1]; the file says (ST)³ = −I, of order 3 in PSL₂ (:85-:86)'),
    'tri_diag': ('cna', 'SIDEClassNumberAnomaly/Basic.lean', 204, 'theorem triple_identification_diagonal :',
                 '`triple_identification_diagonal : ∀ d ∈ triviumDiscs, (classNumber d = 2 ∧ hammingWeight d = 3 ∧ discMagnitude d = 24) ↔ d = -6`, by `decide` (:204-:207)'),
    'tri_stmt': ('cna', 'SIDEClassNumberAnomaly/Basic.lean', 206, '(classNumber d = 2 ∧ hammingWeight d = 3 ∧ discMagnitude d = 24) ↔ d = -6', 'its statement'),
    'cn_lookup': ('cna', 'SIDEClassNumberAnomaly/Basic.lean', 52, 'def classNumber : Int → Nat',
                  '`classNumber` an encoded table, −6 ↦ 2 and the six others ↦ 1 (:52-:60); the kernel’s honesty note (:196-:202) names its grounding LV-L-4'),
    'm24_phi': ('mod24', 'SIDEDirichletMod24/Basic.lean', 62, 'theorem phi_24_eq_eight :', '`phi_24_eq_eight`: φ(24) = 8 by enumerating gcd with 24 (:62-:67)'),
    'm24_units': ('mod24', 'SIDEDirichletMod24/Basic.lean', 82, 'theorem all_units_order_two_or_one :',
                  '`all_units_order_two_or_one`: each of 1, 5, 7, 11, 13, 17, 19, 23 squares to 1 mod 24 (:82-:90)'),
    'm24_card': ('mod24', 'SIDEDirichletMod24/Basic.lean', 127, 'theorem units_eq_cubit : numUnits = cubitCardinality := by decide',
                 '`units_eq_cubit : numUnits = cubitCardinality`, both defined as 8 (:57, :120); the isomorphism (ℤ/24)* ≅ (ℤ/2)³ is stated in the '
                 'comments at :84 and :124, no declaration states it'),
    'part_card': ('substrate', 'SIDESubstrateCluster/Substrate.lean', 126, 'theorem partition_cardinalities :',
                  '`SIDESubstrateCluster.partition_cardinalities`: the weight classes 1, 2 and 3 have lengths 3, 3 and 1 (:126-:130)'),
    'diag_unp': ('substrate', 'SIDESubstrateCluster/PairingObstruction.lean', 41, 'theorem diagonal_unpaired : inSubstrate (antipode diagonal) = false := by decide',
                 '`SIDESubstrateCluster.diagonal_unpaired : inSubstrate (antipode diagonal) = false`'),
    'obstr': ('substrate', 'SIDESubstrateCluster/PairingObstruction.lean', 64, 'theorem obstruction_theorem :',
              '`SIDESubstrateCluster.obstruction_theorem`: the diagonal is in the substrate and its antipode is not, while e1, e2, e3 and their antipodes are (:64-:70)'),
    'ifb_v01': ('bij01', 'SIDEBijection/Theorem.lean', 134, 'theorem identity_formation_bijection (S : IDSSystem) :',
                '`SIDEBijection.identity_formation_bijection (S : IDSSystem) : ∀ stage : Fin 4, Bijective (S.identityOf stage)` (:134-:135)'),
    'ifb_v01_pf': ('bij01', 'SIDEBijection/Theorem.lean', 137, 'exact ⟨S.distinctness stage, S.noOrphans stage⟩',
                   'closed by the structure’s own fields `distinctness` and `noOrphans`, which an instance supplies'),
    'side_ids': ('bij020', 'SIDEBijection/Theorem.lean', 230, 'def sideIDS : IDSSystem where', '`SIDEBijection.sideIDS : IDSSystem`, the identity map on Fin n at each stage (:230-:236)'),
    'side_form': ('bij020', 'SIDEBijection/Theorem.lean', 231, 'formation := ⟨2, 3, 2, 0⟩', 'its formation tuple'),
    'side_bij': ('bij020', 'SIDEBijection/Theorem.lean', 241, 'theorem sideIDS_bijection :',
                 '`SIDEBijection.sideIDS_bijection : ∀ stage, Bijective (sideIDS.identityOf stage)`, the schema applied to `sideIDS` (:241-:243)'),
    'triv_thm': ('trivium', 'Trivium/Bijection.lean', 256, 'theorem trivium_theorem :',
                 '`Trivium.trivium_theorem : Nonempty (MechanismClass ≃ QuadraticDiscriminant) ∧ Fintype.card MechanismClass = 7 ∧ '
                 'Fintype.card QuadraticDiscriminant = 7` (:256-:259)'),
    'triv_card': ('trivium', 'Trivium/Bijection.lean', 258, 'Fintype.card MechanismClass = 7 ∧', 'its cardinality conjunct; MechanismClass an inductive type of the kernel (:64)'),
    'spinor': ('spinor', 'SIDESpinor/Spinor.lean', 70, 'theorem spinor_forces_half (w : ℂ) (h : Complex.I * w = w) : w = 0 :=',
               '`SIDESpinor.spinor_forces_half (w : ℂ) (h : Complex.I * w = w) : w = 0`'),
}

T1 = 'I-7 @ 847e433; IB Thm 3.1 @ 1d0109f'
T2 = 'detector, epstein @ v0.16 = c404e72; IB Thm 3.7 @ 1d0109f'
EPS = 'an Epstein ζ_Q among them, whose off-line zeros the detector meets at ρ_E'
R1 = ('R1', 'DARK', 2, T2, 'the classes’ exclusions, as the sieve reads them, are conditions on a real σ naming no function, so they hold beside the '
                           'Epstein configuration the detector meets at ρ_E', 'RH-60')
R2 = ('R2', 'NOT A ROUTE', None, '—', 'the papers’ own correction of 2026-08-10: the paths identify the line, sharing one involution, and carry no '
                                     'placement', None)
R3 = ('R3', 'NOT A ROUTE', None, '—', 'a finite range of computed zeros says nothing of the zeros beyond it', 'RH-58')
R4 = ('R4', 'DARK', 2, T2, 'the monodromy is a property of the involution s ↦ 1 − s, shared by every function with this functional equation, ' + EPS, None)
R5 = ('R5', 'DARK', 2, T2, 'the count of real conditions holds for every function real on its symmetry line, ' + EPS + '; CO :2737 marks the step '
                           'for ζ open', None)
R6 = ('R6', 'DARK', 2, T2, 'TS :643 says its analytic results use only the functional equation and the Cauchy–Riemann equations, not the Euler '
                           'product, so they hold unchanged at the Epstein configuration', None)
R7 = ('R7', 'DARK', 2, T2, 'the inventory names no prime-side ingredient, and the Epstein configuration (the sieve’s FD-01) carries an off-line '
                           'point with a functional equation', None)
R8 = ('R8', 'DARK', 2, T2, 'the Frobenius property of {2, 3} is a fact about the integers and names no prime side; the integers an Epstein ζ_Q '
                           'sums over carry it unchanged', None)
R9 = ('R9', 'DARK', 1, T1, 'a statistic over thirty ordinates, |ζ′(ρ)|/√γ, carries no real part of any zero', None)

# ### the claims: id, paper, line, needle (on that line), the claim restated, grade, the support the paper's text names, reason, route, kernel reads
C = [
    # ---------------------------------------------------------------- FROBENIUS (1.5e-2)
    ('FR-01', 'FR', 26, 'Theorem (Frobenius Uniqueness for g = 1)', 'FR states that {2, 3} is the one coprime pair with both entries at least 2 '
     'whose Frobenius number is 1.', 'kernel-verified', 'terminal', 'FR :30 names `g_two_three` and `g_two_three_minimal` at SIDE-frobenius '
     '`2efe9f2`; read at that pin, g(2, 3) = 1 and every other pair 2 ≤ a < b has g(a, b) ≥ 2', None, ['g23', 'g23min', 'g23min_stmt']),
    ('FR-02', 'FR', 32, 'Corollary (Gap-Free Accessibility)', 'FR states that every integer n ≥ 2 is a sum 2a + 3b with a, b ≥ 0.',
     'theorem-supported', 'theorem', 'Sylvester’s formula, named at :20; not among the terminals FR names', None, []),
    ('FR-03', 'FR', 50, 'The indicial identity and its forced double root are machine-checked', 'FR states that the indicial equation of (xp)² '
     'factors as (r + 1/2)² = 0, with the double root r = −1/2.', 'kernel-verified', 'terminal', 'FR :50 names `indicial_factor`, '
     '`indicial_root_unique` and `indicial_forces_half` at `2efe9f2`; read there, r² + r + 1/4 = (r + 1/2)² over ℚ with the one root −1/2; '
     'the Berry–Keating operator itself is not compiled', None, ['ind_factor', 'ind_unique', 'ind_half']),
    ('FR-04', 'FR', 58, 'corresponds to this boundary condition under the Mellin/Berry-Keating correspondence', 'FR states that the critical line '
     'corresponds to the indicial boundary condition at x = 0 under the Mellin and Berry–Keating correspondence.', 'statement-grade',
     'statement', 'stated at :58 without an argument', None, []),
    ('FR-05', 'FR', 75, 'machine-checked at SIDE-frobenius `2efe9f2` (`S_squared`, `ST_cubed`', 'FR states that the modular generators satisfy '
     'S² = −I and, in PSL₂(ℤ), (ST)³ = I.', 'kernel-verified', 'terminal', 'read at `2efe9f2`: S² = −1 and (ST)³ = −1 in SL₂(ℤ), which is '
     '(ST)³ = I in PSL₂(ℤ); FR :75 and :93 write (ST)³ = I as the relation checked', None, ['S_sq', 'ST_cu']),
    ('FR-06', 'FR', 101, 'The substrate-unity claim of this paper', 'FR reads {2, 3} as the one algebraic basis from which the Frobenius, '
     'Berry–Keating and modular appearances derive.', 'synthesis-suggested', 'reading', 'FR :109 keeps the unity a reading', None, []),
    ('FR-07', 'FR', 103, 'These seven discriminants are the seven mechanism classes', 'FR states that the seven discriminants {−1, ±2, ±3, ±6} '
     'are the seven mechanism classes of ξ.', 'statement-grade', 'statement', 'stated with a cross-reference to IDENTITY_FORMATION_BIJECTION '
     'Theorem 5.1', None, []),
    ('FR-08', 'FR', 111, 'A complete proof of the Riemann Hypothesis', 'FR states that it does not establish RH and that its earlier version '
     'overstated what the substrate provides.', 'statement-grade', 'statement', 'the paper’s own scope at :111', None, []),
    # ---------------------------------------------------------------- TRIVIUM (1.5e-3)
    ('TR-01', 'TR', 26, 'becomes ξ(w) = ξ(−w)', 'TR states that in w = s − 1/2 the functional equation reads ξ(w) = ξ(−w), the critical line '
     'being Re(w) = 0.', 'theorem-supported', 'theorem', 'the functional equation, classical', None, []),
    ('TR-02', 'TR', 30, 'holds for every prime simultaneously if and only if σ = 1/2', 'TR states that p^(−σ) = p^(−(1−σ)) holds at every '
     'prime exactly when σ = 1/2.', 'argument-supported', 'argument', 'one line of algebra at :30; TR names no terminal', None, []),
    ('TR-03', 'TR', 34, 'the exponent 1/2 = 2^(−1) is forced by n²', 'TR states that the theta transformation’s exponent 1/2 comes from the n² '
     'in θ through Poisson summation, and that the Mellin transform carries it to the axis σ = 1/2.', 'theorem-supported', 'theorem',
     'Poisson summation and the Gaussian transform, classical, at :34', None, []),
    ('TR-04', 'TR', 74, 'The Trivium is the fixed point of S', 'TR places the Trivium at the fixed point τ = i of S, the order-3 element '
     'fixing e^(2πi/3).', 'theorem-supported', 'theorem', 'the modular group’s fixed points, classical (Serre, named at :67); the '
     'identification with σ = 1/2 is the paper’s', None, []),
    ('TR-05', 'TR', 88, 'Off the critical line, this cancellation fails', 'TR states that ξ(1/2 + it) is real, reading it as the phases of e, '
     'i and π cancelling, and that the cancellation fails off the line.', 'statement-grade', 'statement', 'the realness is classical; the '
     'phase reading and its failure off the line are stated', None, []),
    ('TR-06', 'TR', 104, 'These are the same statement', 'TR states that its Trivium reformulation and RH are the same statement.',
     'statement-grade', 'statement', 'a restatement, stated at :104', None, []),
    ('TR-07', 'TR', 106, 'collectively forbid off-Trivium zeros', 'TR states that the seven mechanism classes of ξ together forbid zeros off '
     'the Trivium, citing the I+D+S paper and ARITHMETIC_HORIZONS V80.', 'statement-grade', 'statement', 'stated with citations; no '
     'argument at :106', R1, []),
    ('TR-08', 'TR', 112, 'are the same algebraic object acting on different carrier objects', 'TR reads the seven mechanism classes, the seven '
     'elements of (ℤ/2)³ from {−1, 2, 3}, the seven Hamming syndromes and the seven Fano points as one algebraic object.',
     'synthesis-suggested', 'reading', 'the cluster keystone’s reading, at :112', None, []),
    # ---------------------------------------------------------------- TRIVIUM_FINDINGS (1.5e-4)
    ('TF-01', 'TF', 22, 'This equation solves to σ = 1/2', 'TF states that the balance p^(−σ) = p^(−(1−σ)) has the one solution σ = 1/2 for '
     'every prime, and names 1/2 the exponential zero.', 'argument-supported', 'argument', 'algebra at :22; the name is the paper’s', None, []),
    ('TF-02', 'TF', 70, 'convergent identification, not independent derivation', 'TF states five derivations of σ = 1/2 and, corrected on '
     '2026-08-10, calls their agreement convergent identification and not independent derivation.', 'synthesis-suggested', 'reading',
     'the convergence reading at :56-:70 with its correction', R2, []),
    ('TF-03', 'TF', 169, 'Every prime splits in exactly 3 or exactly 7 of the seven fields', 'TF states that every prime splits in exactly 3 '
     'or exactly 7 of the seven fields ℚ(√d).', 'argument-supported', 'argument', 'TF :427 calls it a theorem of quadratic reciprocity, '
     'the argument TS :287’s; TF :171 gives the valence-7 primes as ±1 mod 24, where that argument gives 1 mod 24', None, []),
    ('TF-04', 'TF', 241, '**(1,2), (2,3), (3,4), (8,9)**', 'TF states Størmer’s theorem for {2, 3}: the consecutive {2, 3}-smooth pairs are '
     '(1, 2), (2, 3), (3, 4) and (8, 9).', 'theorem-supported', 'theorem', 'Størmer 1897, named at :239', None, []),
    ('TF-05', 'TF', 134, '**{0, 0, 0, 0, 0, 0, 12}**', 'TF states that the Hermitian matrix vv† of the Trivium vector has spectrum '
     '{0, 0, 0, 0, 0, 0, 12}.', 'argument-supported', 'argument', 'a rank-one matrix with ||v||² = 12 (:114)', None, []),
    ('TF-06', 'TF', 211, 'cannot, in principle, determine the location of individual zeros', 'TF states that methods working through averaged '
     'quantities cannot locate individual zeros.', 'statement-grade', 'statement', 'asserted at :211-:213 as structural, without an '
     'argument', None, []),
    ('TF-07', 'TF', 223, 'Therefore the Euler product *never converges where the zeros live*', 'TF states that the Euler product converges '
     'only for Re(s) > 1, so not where the nontrivial zeros lie.', 'theorem-supported', 'theorem', 'classical', None, []),
    ('TF-08', 'TF', 371, 'forbids coincidental zeros away from σ = 1/2', 'TF sets out a six-step architecture ending in the Mechanism Theorem '
     'forbidding zeros off σ = 1/2.', 'synthesis-suggested', 'reading', 'its steps marked done at :363-:369, its weight on the Mechanism '
     'Theorem (:391)', R1, []),
    ('TF-09', 'TF', 391, 'is the load-bearing axiom', 'TF states that the Mechanism Theorem is the load-bearing axiom of its framework and '
     'that the framework fails if it is false.', 'statement-grade', 'statement', 'the paper’s own caveat C1', None, []),
    ('TF-10', 'TF', 421, 'remains a conjecture', 'TF states that its explanation of the 3/4 exponent remains a conjecture.', 'statement-grade',
     'statement', 'the paper’s own caveat C4', None, []),
    ('TF-11', 'TF', 502, 'Numerically verified to 10¹³+ zeros', 'TF records RH as numerically checked to more than 10¹³ zeros.',
     'computationally-verified', 'computation', 'the literature computation, reported', R3, []),
    # ---------------------------------------------------------------- TRIVIUM_IDENTITY_SUBSPACE (1.5e-5)
    ('TS-01', 'TS', 98, 'The exponential balance point is σ₀ = 1/2', 'TS states that n^(−σ) = n^(−(1−σ)) for every n ≥ 2 holds exactly at '
     'σ = 1/2.', 'argument-supported', 'argument', 'the argument at :100', None, []),
    ('TS-02', 'TS', 110, 'by analogy: the additive and multiplicative identities', 'TS states that it calls 1/2 an identity element by analogy, '
     '1/2 being the fixed point of the involution σ ↦ 1 − σ and not an identity in the axiom’s sense.', 'statement-grade', 'statement',
     'the paper’s own scope remark', None, []),
    ('TS-03', 'TS', 116, 'not logically independent: three of them take the involution', 'TS states five convergent constructions of '
     'σ = 1/2 and, corrected, that they are not logically independent, three taking the involution σ ↦ 1 − σ as their definition.',
     'synthesis-suggested', 'reading', 'the convergence reading at :114-:128 with its correction', R2, []),
    ('TS-04', 'TS', 174, 'Parts (a) and (b) are additionally machine-checked at SIDE-frobenius v0.1.0', 'TS states that g(2, 3) = 1 and the '
     'modular relations S² = −I, (ST)³ = I are machine-checked, Størmer’s finiteness staying classical.', 'kernel-verified', 'terminal',
     'read at SIDE-frobenius v0.1.0 = `2efe9f2`: `g_two_three`, and S² = −1, (ST)³ = −1 in SL₂(ℤ), the latter I only in PSL₂(ℤ)', None,
     ['g23', 'S_sq', 'ST_cu']),
    ('TS-05', 'TS', 180, 'The group generated by {−1, 2, 3} in ℚ*/ℚ*² is (ℤ/2)³', 'TS states that {−1, 2, 3} generate (ℤ/2)³ in ℚ*/ℚ*², '
     'giving seven nontrivial quadratic fields.', 'argument-supported', 'argument', 'the argument at :180', None, []),
    ('TS-06', 'TS', 184, 'For P = {2, 3}, the complete list is', 'TS states Størmer’s theorem with the four consecutive pairs for {2, 3}.',
     'theorem-supported', 'theorem', 'Størmer 1897 and Lehmer 1964, named at :186', None, []),
    ('TS-07', 'TS', 194, 'Two independent counts converge', 'TS states that the dimension 7 comes from two counts, the seven fields and the '
     'symmetric Størmer range {−3, …, 3}.', 'argument-supported', 'argument', 'the argument at :194', None, []),
    ('TS-08', 'TS', 238, 'spec(M) = {0, 0, 0, 0, 0, 0, 12}', 'TS states that M = vv† has spectrum {0⁶, 12}.', 'argument-supported', 'argument',
     'the argument at :240', None, []),
    ('TS-09', 'TS', 246, '≈ 0.592 bits', 'TS states the Shannon entropy of the eigenvalue weights 1/7 and 6/7 as about 0.592 bits.',
     'argument-supported', 'argument', 'a direct computation at :248', None, []),
    ('TS-10', 'TS', 285, 'Every prime p > 3 has valence exactly 3 or exactly 7.', 'TS states that every prime p > 3 splits in exactly 3 or '
     'exactly 7 of the seven fields, 7 exactly when (−1/p), (2/p) and (3/p) are all +1.', 'argument-supported', 'argument',
     'the argument at :287', None, []),
    ('TS-11', 'TS', 312, '𝐖⁴ = −Id (not +Id)', 'TS states that the Weil representation’s lift of the Fourier transform satisfies 𝐖⁴ = −Id, '
     'so has order 8.', 'theorem-supported', 'theorem', 'Weil 1964 and Weissman 2023, named at :310', None, []),
    ('TS-12', 'TS', 318, 'Theorem 7.3 (Metaplectic Correspondence)', 'TS states a correspondence between the quarter-twist of the Trivium '
     'vector and the Weil representation on the {2, 3}-smooth sector.', 'synthesis-suggested', 'reading', 'TS :677 names it a '
     'correspondence, not an identification', None, []),
    ('TS-13', 'TS', 326, 'Theorem 7.5 (Möbius Dichotomy)', 'TS states that over the critical line the complex bundle E_ℂ is orientable and the '
     'real bundle E_ℝ is not.', 'argument-supported', 'argument', 'the argument at :328', None, []),
    ('TS-14', 'TS', 359, 'The Möbius monodromy of E_ℝ is supported at σ = 1/2 and only at σ = 1/2', 'TS states that the monodromy sits at '
     'σ = 1/2 alone, since only there the involution s ↦ 1 − s fixes a fiber.', 'argument-supported', 'argument', 'the argument at :361',
     None, []),
    ('TS-15', 'TS', 381, 'Δₜ(t) = t² − t + 1 = Φ₆(t)', 'TS states that the trefoil’s Alexander polynomial is t² − t + 1 = Φ₆(t).',
     'theorem-supported', 'theorem', 'the torus-knot formula, applied at :383', None, []),
    ('TS-16', 'TS', 394, 'IS the functional equation on the Trivium', 'TS reads the trefoil’s Alexander polynomial as the functional '
     'equation acting on the Trivium’s quarter-twist.', 'synthesis-suggested', 'reading', 'a reading at :394', None, []),
    ('TS-17', 'TS', 464, 'Theorem 8.14 (FOCUS)', 'TS states that ξ(1/2 + it) is real for every real t.', 'theorem-supported', 'theorem',
     'Riemann 1859 and Edwards 1974, named at :466', None, []),
    ('TS-18', 'TS', 476, 'Proposition 8.16 (Codimension Dichotomy)', 'TS states that a zero on the critical line is one real condition and a '
     'zero off it two.', 'argument-supported', 'argument', 'the argument at :478; TS :480 reads the second as structurally exceptional',
     R5, []),
    ('TS-19', 'TS', 520, 'Proposition 8.27 (Orthogonal Crossing)', 'TS states that at each simple zero on the line ξ′ is purely imaginary, '
     'so the level curves Re ξ = 0 and Im ξ = 0 cross at right angles.', 'argument-supported', 'argument', 'the argument at :522', None, []),
    ('TS-20', 'TS', 538, 'Theorem 8.29 (Neighborhood Nonvanishing)', 'TS states that along the curve Re ξ = 0 through a simple zero, Im ξ '
     'vanishes at σ = 1/2 alone within some neighborhood.', 'argument-supported', 'argument', 'the argument at :540', None, []),
    ('TS-21', 'TS', 548, 'Theorem 8.30 (Monotonicity Formula)', 'TS states that along that curve V′ₖ(σ) = −|ξ′|²/u_t wherever ξ′ ≠ 0.',
     'argument-supported', 'argument', 'the argument at :554', None, []),
    ('TS-22', 'TS', 558, 'Corollary 8.31 (Fold Criterion)', 'TS states that Vₖ can vanish off the line only where the curve folds, so that '
     'no fold at any zero is equivalent to RH.', 'argument-supported', 'argument', 'the argument at :560; TS :660 grades it a '
     'reformulation', None, []),
    ('TS-23', 'TS', 583, 'is positive at all 109 sample heights', 'TS reports C(t) = (ξ′_ℝ)² − ξ_ℝ ξ″_ℝ positive at 109 heights in [1, 55].',
     'computationally-verified', 'computation', 'a computation, reported', None, []),
    ('TS-24', 'TS', 587, 'verified that the first 12,363,153,093,004 non-trivial zeros', 'TS cites Platt and Trudgian’s computation of the '
     'first 12,363,153,093,004 zeros on the line and simple, and reads it as no fold at those zeros.', 'computationally-verified',
     'computation', 'the literature computation [18]', R3, []),
    ('TS-25', 'TS', 607, 'Every known mechanism for producing zeros of entire functions', 'TS inventories the known mechanisms producing zeros '
     'and finds none that produces a zero off the critical line.', 'synthesis-suggested', 'reading', 'an inventory at :605-:611', R7, []),
    ('TS-26', 'TS', 615, 'converge on the same conclusion', 'TS states that its analytic, topological and structural lines of evidence '
     'converge on every nontrivial zero lying on the critical line.', 'synthesis-suggested', 'reading', 'TS :671 calls them evidence',
     R6, []),
    ('TS-27', 'TS', 643, 'use only the functional equation and Cauchy–Riemann, not the Euler product', 'TS states that its analytic results '
     'of §§8.5-8.7 use only the functional equation and the Cauchy–Riemann equations, not the Euler product.', 'statement-grade',
     'statement', 'the paper’s own account of its means', None, []),
    ('TS-28', 'TS', 660, '| Fold Criterion (= RH) | REFORMULATION |', 'TS grades its fold criterion a reformulation and global family '
     'separation open and equivalent to RH.', 'statement-grade', 'statement', 'the status table at :653-:663', None, []),
    ('TS-29', 'TS', 671, 'These are evidence, not proof', 'TS states that its computations and its inventory are evidence and that the step '
     'from the local result to RH is the open question.', 'statement-grade', 'statement', 'the paper’s methodological note', None, []),
    # ---------------------------------------------------------------- CLASS_NUMBER_ANOMALY (1.5e-6)
    ('CN-01', 'CN', 15, 'exactly six have class number', 'CN states that of the seven fields ℚ(√d), d ∈ {−1, 2, 3, −2, −3, 6, −6}, six have '
     'class number 1 and ℚ(√−6) has class number 2.', 'computationally-verified', 'computation', 'PARI/GP, reported at :41', None, []),
    ('CN-02', 'CN', 49, '**(C1) Cube combinatorics.**', 'CN states that ℚ(√−6) is the vector (1, 1, 1) of (ℤ/2)³, the one vertex of Hamming '
     'weight 3, the weights splitting (3, 3, 1).', 'kernel-verified', 'terminal', 'CN :98 and :132 name `SIDESubstrateCluster.'
     'partition_cardinalities` at SIDE-substrate-cluster v0.4; read at `06b61c3`, the weight classes have lengths 3, 3 and 1; the '
     'identification with ℚ(√−6) is the paper’s', None, ['part_card']),
    ('CN-03', 'CN', 53, 'the natural modulus of Dirichlet characters mod 24', 'CN states that (ℤ/24)* has the structure (ℤ/2)³, verified in '
     'SIDE-dirichlet-mod-24 v0.1.0 = 597b0869.', 'argument-supported', 'terminal', 'read at `597b0869`: φ(24) = 8, each of the eight units '
     'squares to 1 mod 24, and a count equality; the isomorphism stands in the kernel’s comments and follows from the structure of an '
     'abelian group of order 8 and exponent 2, not compiled as a declaration', None, ['m24_phi', 'm24_units', 'm24_card']),
    ('CN-04', 'CN', 62, 'the discriminant doubles to $-24$', 'CN states that since −6 is squarefree and ≡ 2 mod 4, the discriminant of '
     'ℚ(√−6) is −24.', 'theorem-supported', 'theorem', 'the discriminant of a quadratic field, classical', None, []),
    ('CN-05', 'CN', 66, 'three views of the same fact', 'CN reads weight 3, class number 2 and discriminant magnitude 24 as three views of one '
     'property, both 2 and 3 ramifying in ℚ(√−6).', 'synthesis-suggested', 'reading', 'a reading at :59-:66', None, []),
    ('CN-06', 'CN', 82, 'is **not forced**', 'CN states that an element-level canonical bijection between the seven fields and the seven '
     'classes is not forced, a symmetry transitive on the seven objects making any assignment a choice of basis.', 'argument-supported',
     'argument', 'the argument at :82', None, []),
    ('CN-07', 'CN', 82, 'demonstrated at a concrete instance', 'CN states that the abstract Identity-Formation Bijection schema is demonstrated '
     'at the concrete instance sideIDS, formation (2, 3, 2, 0), total 7.', 'kernel-verified', 'terminal', 'CN :82 names SIDE-bijection '
     'v0.2.0 = `a26f6f1`; read there, `sideIDS` carries the formation ⟨2, 3, 2, 0⟩ and the identity map at each stage, and '
     '`sideIDS_bijection` applies the schema to it', None, ['side_ids', 'side_form', 'side_bij']),
    ('CN-08', 'CN', 86, 'the arithmetic shadow of the CSS construction', 'CN reads the class number 2 of ℚ(√−6) as the arithmetic shadow of '
     'the CSS construction’s parity-check dependency.', 'synthesis-suggested', 'reading', 'a reading at :86', None, []),
    ('CN-09', 'CN', 90, 'The cosmological wall reads off the ramification structure', 'CN reads the denominator 81 = 3⁴ of Ω_b = 4/81 as the '
     'ramification of 3 in ℚ(√−6).', 'synthesis-suggested', 'reading', 'a reading at :90', None, []),
    ('CN-10', 'CN', 134, 'it carries **no concrete seven-count**', 'CN states that SIDE-bijection v0.1 = dd487e6 carries the abstract schema '
     'only, bijectivity from assumed per-stage injectivity and surjectivity, with no concrete seven-count.', 'kernel-verified', 'terminal',
     'read at `dd487e6`: `identity_formation_bijection` concludes Bijective (S.identityOf stage) at every stage from the structure’s own '
     'fields; the tag v0.1 is held in the clone only, its commit on the remote main', None, ['ifb_v01', 'ifb_v01_pf']),
    ('CN-11', 'CN', 134, '`SIDE-trivium.trivium_theorem` (`1df5bad4`)', 'CN states that SIDE-trivium’s trivium_theorem exhibits a concrete '
     'MechanismClass ≃ QuadraticDiscriminant with both cardinalities 7.', 'kernel-verified', 'terminal', 'read at `1df5bad4`: Nonempty '
     '(MechanismClass ≃ QuadraticDiscriminant) with both Fintype cardinalities 7, MechanismClass an inductive type of the kernel',
     None, ['triv_thm', 'triv_card']),
    ('CN-12', 'CN', 146, 'is now kernel-verified as `triple_identification_diagonal`', 'CN states that weight 3, class number 2 and '
     'discriminant magnitude 24 hold together for d = −6 alone among the seven Trivium discriminants.', 'kernel-verified', 'terminal',
     'CN :202 names SIDE-class-number-anomaly v0.2 = `2203b88a`; read there, the biconditional over `triviumDiscs` by `decide`, with '
     '`classNumber` an encoded table whose grounding is the open LV-L-4', None, ['tri_diag', 'tri_stmt', 'cn_lookup']),
    ('CN-13', 'CN', 132, '`SIDESubstrateCluster.diagonal_unpaired`', 'CN states that under antipodal pairing in (ℤ/2)³ the weight-3 diagonal '
     'is the one unpaired element.', 'kernel-verified', 'terminal', 'read at SIDE-substrate-cluster v0.4 = `06b61c3`: `diagonal_unpaired` '
     'and `obstruction_theorem`; the tag v0.4 is held in the clone only, its commit the remote’s v0.1.0', None, ['diag_unp', 'obstr']),
    ('CN-14', 'CN', 142, 'is computationally verified in PARI/GP', 'CN states that h(−24) = 2 is checked in PARI/GP and that a Mathlib '
     'derivation is open work.', 'computationally-verified', 'computation', 'PARI/GP, reported', None, []),
    # ---------------------------------------------------------------- CONSTANCE (1.5e-1)
    ('CO-01', 'CO', 18, 'Reclassified → theory-space cluster', 'CO states that its physics readings are proposed and not forced, and that it '
     'was reclassified to the theory-space cluster, leaving a pointer in the Trivium cluster.', 'statement-grade', 'statement',
     'the paper’s role note', None, []),
    ('CO-02', 'CO', 192, 'Six ratios tested. Six match. 100%.', 'CO states that six adjacent-generation mass ratios factor into primes tied to '
     '{2, 3} and three non-adjacent ratios do not.', 'computationally-verified', 'computation', 'the tables at :1308-:1318 and :2460-:2474; '
     ':1315 and :2469 give different values for the u to t ratio', None, []),
    ('CO-03', 'CO', 324, 'We need (a−1)(b−1) = 2', 'CO states that g(a, b) = 1 needs (a − 1)(b − 1) = 2, whose only solutions are (2, 3) and '
     '(3, 2).', 'argument-supported', 'argument', 'the argument at :324', None, []),
    ('CO-04', 'CO', 1162, 'Only k=6 and k=7 produce simultaneous primes in this range', 'CO states that among k = 4 to 17 only k = 6 and '
     'k = 7 make both 2^k + 3 and 2^k + 9 prime.', 'computationally-verified', 'computation', 'a primality check, stated as directly '
     'verifiable', None, []),
    ('CO-05', 'CO', 1284, r'\frac{337}{5} = 67.400 \text{ exactly}', 'CO predicts H₀ from the CMB at exactly 337/5 = 67.400 and locally at '
     'exactly 73.000, falsified if the CMB value departs from 67.400.', 'statement-grade', 'statement', 'a prediction; its derivation at '
     ':2629-:2635 is a reading', None, []),
    ('CO-06', 'CO', 1327, 'Of 51 fundamental parameters tested, 47 factor', 'CO reports that 47 of 51 parameters factor into the fifteen core '
     'primes and that no one of 1000 random fifteen-prime sets matched.', 'computationally-verified', 'computation', 'reported, with '
     'figures at :2476-:2484', None, []),
    ('CO-07', 'CO', 1353, '16 predictions confirmed. 0 falsified.', 'CO tabulates sixteen predictions as confirmed and none as falsified.',
     'statement-grade', 'statement', 'a table of matches at :1334-:1351 without a stated method', None, []),
    ('CO-08', 'CO', 1737, 'remains to be proven', 'CO states that whether the generation count traces to the sector count is open, the '
     'correlation being exact.', 'statement-grade', 'statement', 'the paper’s own scope', None, []),
    ('CO-09', 'CO', 1824, 'also forces zeta zeros to the critical line', 'CO states that the arithmetic fixing the physical constants also '
     'places the zeta zeros on the critical line, through the Frobenius property of {2, 3}.', 'statement-grade', 'statement',
     'stated at :1824 without an argument', R8, []),
    ('CO-10', 'CO', 2097, '~70× more accurately than partial Dirichlet sums', 'CO reports partial Euler products through six primes '
     'approximating the first zero about seventy times more closely than partial Dirichlet sums.', 'computationally-verified',
     'computation', 'a computation, tabulated at :2806-:2809', None, []),
    ('CO-11', 'CO', 2105, 'Making "generically" into "necessarily" for this specific function is equivalent to RH', 'CO states that turning '
     'the codimension argument’s “generically” into “necessarily” for ζ is equivalent to RH.', 'statement-grade', 'statement',
     'the paper’s own scope', None, []),
    ('CO-12', 'CO', 2729, 'A smooth one-dimensional trajectory generically misses codimension-2 sets entirely.', 'CO states that off the line '
     'a zero needs two real conditions in one real parameter and that a smooth trajectory generically misses such a set.',
     'argument-supported', 'argument', 'the argument at :2725-:2729; :2737 marks the step for ξ open', R5, []),
    ('CO-13', 'CO', 2746, 'Differentiate ξ(s) = ξ(1−s) to get', 'CO states that at every zero ρ = 1/2 + iγ, Re ξ′(ρ) = 0.',
     'argument-supported', 'argument', 'the argument at :2746; CO names no terminal for it', None, []),
    ('CO-14', 'CO', 2754, 'The product formula ∏_v |x|_v = 1 is *s-dark*', 'CO states that the product formula is s-dark and that every '
     'constraint on zero locations traces to ℚ’s additive, multiplicative and distributive components.', 'argument-supported',
     'argument', 'a one-line argument at :2754', None, []),
    ('CO-15', 'CO', 2772, 'The barrier grows as √γ', 'CO reports |ζ′(ρ)|/√γ with mean 0.251 and no trend over the first 30 zeros, and reads '
     'the barrier as growing like √γ.', 'computationally-verified', 'computation', 'the table at :2766-:2770', R9, []),
    ('CO-16', 'CO', 2790, 'convergent identification, not independent derivation', 'CO states that its five paths share the involution '
     'σ ↦ 1 − σ and that their agreement is convergent identification, evidence about the line and none about placement.',
     'synthesis-suggested', 'reading', 'the correction of 2026-08-10 at :2788-:2790', R2, []),
    ('CO-17', 'CO', 2888, '`SIDESpinor.spinor_forces_half` is `(w : ℂ) (h : Complex.I * w = w) : w = 0`', 'CO states that '
     'SIDESpinor.spinor_forces_half concludes w = 0 from i·w = w and does not conclude σ = 1/2, the reading at σ = 1/2 resting on two '
     'uncompiled stipulations.', 'statement-grade', 'terminal', 'CO names the terminal without a pin; read at SIDE-spinor v0.1.0 (:70), '
     'its statement is the one CO quotes', None, ['spinor']),
    ('CO-18', 'CO', 2908, "There's nothing to find.", 'CO states that the concentration of the monodromy at σ = 1/2 explains why numerical '
     'searches find no off-line zero, there being none to find.', 'statement-grade', 'statement', 'stated at :2908 without an argument',
     R4, []),
    ('CO-19', 'CO', 2852, '"computed" ≠ "proven."', 'CO states that the remaining step runs from the neighborhood of each zero to the whole '
     'strip, its 24,000 computed points not closing it.', 'statement-grade', 'statement', 'the paper’s own scope at :2850-:2854', None, []),
]

ROUTE_ROWS = {'RH-60': 'DARK, test 2', 'RH-58': 'NOT A ROUTE'}
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
    repo, pin, want = PINS[key]
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
        repo, pin, _w = PINS[pk]
        ls = lines_of(show(f, pin, 'D:/' + repo))
        l = ls[n - 1] if 0 < n <= len(ls) else ''
        out.append((k, needle in l, l))
    return out


def sieve_rows():
    """### the sieve v0.4 rows the routes meet, read at the pin: {id: (verdict, test)}"""
    out = {}
    for l in lines_of(show(SIEVE)):
        m = re.match(r'^\| ((?:RH|FD|CT)-\d\d) \| ', l)
        if m and m.group(1) in ROUTE_ROWS and m.group(1) not in out:   # ### the body row, met first; back-matter rows repeat the id
            c = [x.strip() for x in l.strip().strip('|').split(' | ')]
            out[m.group(1)] = (c[4], c[5])
    return out


def grade_ok(c):
    return c[5] in GRADES and c[6] in NEEDS[c[5]] and (c[5] != 'kernel-verified' or bool(c[9]))


def kv_pins(c):
    """### the pin keys a row's kernel reads stand on"""
    return sorted(set(KREADS[k][0] for k in c[9]))


def main():
    rc = resolve_claims()
    bad = [x for x in rc if not x[1]]
    print('### claims %d ; needles failing %s' % (len(C), [(i, l[:80]) for i, _o, l in bad] or 'NONE'))
    rk = resolve_kernel()
    print('### kernel reads %d ; failing %s' % (len(rk), [(k, l[:80]) for k, ok, l in rk if not ok] or 'NONE'))
    for k in PINS:
        print('### pin %s' % (pin_state(k),))
    print('### grades out of rule: %s' % ([c[0] for c in C if not grade_ok(c)] or 'NONE'))
    print('### routes: %s' % [(c[0], c[8][0], c[8][1], c[8][2], c[8][5]) for c in C if c[8]])
    print('### sieve rows: %s' % sieve_rows())
    from collections import Counter
    print('### grade counts: %s' % dict(Counter(c[5] for c in C)))
    print('### ids unique: %s' % (len(set(c[0] for c in C)) == len(C)))


if __name__ == '__main__':
    main()
