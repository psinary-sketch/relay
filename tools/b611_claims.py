# -*- coding: utf-8 -*-
"""b611_claims.py -- THE ACT'S DATA AND ITS RESOLVERS, UNDER (R221)(4): THE CLAIMS OF PHASE 1.2'S FOUR PAPERS.

### Every claim is the seat's one-sentence restatement of a paper's sentence, carried with a needle that must occur on the cited line of the
### paper at PLACE-papers f374bba; its grade is the one the paper's own text supports, in the vocabulary of (R19) as (R220)(5) lists it:
### kernel-verified at a pin; theorem-supported; argument-supported; computationally-verified; synthesis-suggested; statement-grade.
### THE GRADING RULE, the seat's reading and strikeable: kernel-verified only where the paper names a terminal (or its file) at a pin and the
### statement read at that pin carries the claim; theorem-supported only where the paper names a theorem of the literature for it;
### computationally-verified only where the paper reports a computation; argument-supported where the paper's text argues the claim;
### synthesis-suggested where it reads a pattern across results; statement-grade where it states without argument. No grade is above the
### paper's own support. A ROUTE is a claim offered as an argument toward RH, simplicity or the open clause; each is read through the
### sieve's five tests in order. This module writes nothing: `python tools/b611_claims.py` runs the resolvers and prints.
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
SKER = 'D:/SIDE-kernel'
PRE_PP = 'f374bba'
KPIN, KSHA = 'v1.2', 'b1407b2'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

PAPERS = {
    'EA': ('phase1.5/proofs/THE_EXCLUSION_ARCHITECTURE.md', '1.5a-1', 142),
    'ME': ('phase1.5/proofs/MECHANISM_EXCLUSION.md', '1.5a-2', 143),
    'IR': ('phase1.5/proofs/IDS_TO_RH.md', '1.5a-3', 144),
    'IP': ('phase1.5/proofs/INTEGRATED_PROOF.md', '1.5a-4', 145),
}
GRADES = ('kernel-verified', 'theorem-supported', 'argument-supported', 'computationally-verified', 'synthesis-suggested', 'statement-grade')
# ### what each grade needs of the paper's own support (H45b): the support named in the paper's text must be one of these
NEEDS = {'kernel-verified': ('terminal',), 'theorem-supported': ('theorem', 'terminal'), 'computationally-verified': ('computation',),
         'argument-supported': ('argument', 'theorem', 'terminal', 'computation'), 'synthesis-suggested': ('argument', 'theorem', 'terminal',
                                                                                                        'computation', 'reading', 'statement'),
         'statement-grade': ('argument', 'theorem', 'terminal', 'computation', 'reading', 'statement')}

# ### the kernel reads: (key, file at v1.2, line, needle on that line, what the statement says)
KREADS = {
    'conservation_rh': ('Bridge/ConservationBridge.lean', 36, 'theorem riemann_hypothesis',
                        '`ConservationBridge.riemann_hypothesis (h_cons : ConservationHypothesis) : RiemannHypothesis`, its premise '
                        '(:13-:16) every σ with is_xi_zero σ meeting p^(−σ) = p^(−(1−σ)) at every prime'),
    'cons_hyp': ('Bridge/ConservationBridge.lean', 13, 'def ConservationHypothesis : Prop :=', 'the premise ConservationHypothesis'),
    'integration_rh': ('Kernel/Integration.lean', 210, 'theorem rh_from_structural_exhaustiveness',
                       '`techne_kernel_integration.rh_from_structural_exhaustiveness (h : StructuralExhaustiveness) : RiemannHypothesis`, its '
                       'antecedent (:201-:202) ∀ σ, is_xi_zero σ → σ = 1/2'),
    'integration_se': ('Kernel/Integration.lean', 202, '∀ (sigma : Real), is_xi_zero sigma → sigma = 1 / 2', 'the antecedent'),
    'spectral_cannon': ('Kernel/SpectralCannonFull.lean', 58, 'theorem spectral_cannon (t : ℝ) :',
                        '`SpectralCannonFull.spectral_cannon (t : ℝ) : (deriv completedRiemannZeta₀ ⟨1/2, t⟩).re = 0`'),
    'spectral_cannon_stmt': ('Kernel/SpectralCannonFull.lean', 59, '(deriv completedRiemannZeta₀ ⟨1/2, t⟩).re = 0', 'its statement'),
    'formation': ('Kernel/Core.lean', 53, 'theorem formation : 2 + 3 + 2 + 0 = 7 := by decide', '`SIDEKernel.formation : 2 + 3 + 2 + 0 = 7`, by `decide`'),
    'formation_count': ('Kernel/Core.lean', 50, 'theorem formation_count : n1 + n2 + n3 + n4 = 7 := by decide',
                        '`SIDEKernel.formation_count : n1 + n2 + n3 + n4 = 7`, by `decide`'),
    'balance': ('Kernel/Voice1.lean', 22, 'theorem balance_theorem (p : Nat) (hp : Nat.Prime p) (s : Real) :',
                '`balance_theorem p hp s : p^(−s) = p^(−(1−s)) ↔ s = 1/2` for a prime p (:22-:24)'),
    'sep_root': ('Bridge/TheBridgeComplete.lean', 188, 'theorem structural_exhaustiveness_proved :',
                 'the root `structural_exhaustiveness_proved : StructuralExhaustiveness`, the conjunction of the card-7 enumeration, none_produce '
                 'and Ostrowski at :180-:190'),
    'sep_cons': ('Bridge/ConservationBridge.lean', 29, 'theorem structural_exhaustiveness_proved',
                 'the second `structural_exhaustiveness_proved`, of namespace ConservationBridge, conditional on ConservationHypothesis'),
}

T2 = 'detector, epstein @ v0.16 = c404e72; IB Thm 3.7 @ 1d0109f'
T4 = 'forall_upto pair @ v0.3 = 04eda4a; li_nonneg_iff_rh @ v0.9 = e5a5a83'

# ### the claims: id, paper, line, needle (on that line), the claim restated, grade, the support the paper's text names, reason, route
# ### (None or (route id, verdict, test, instrument, reason, the sieve row it meets or None)), kernel reads (keys of KREADS)
C = [
    ('EA-01', 'EA', 48, 'under the conservation clause', 'EA states that every nontrivial zero of ζ lies on Re(s) = 1/2 under the conservation '
     'clause h2, every zero of ξ forcing the Euler balance, with h1 complete and h2 open.', 'kernel-verified', 'terminal',
     'the conditional is the compiled ConservationBridge.riemann_hypothesis at SIDE-kernel v1.2, which EA :542 names at that pin; its premise '
     'is the paper’s h2 in the conservation register; the sieve reads that premise as RH restated (RH-02, ch_iff_rh)', None, ['conservation_rh', 'cons_hyp']),
    ('EA-02', 'EA', 50, 'Exhaustive mechanism enumeration from finite specification', 'EA names its method exhaustive mechanism enumeration from a '
     'finite specification, seven classes none producing an off-line zero, the exclusion conditional on h2.', 'argument-supported', 'argument',
     'argued across EA §§5-10; the conditional is stated at :50',
     ('R1', 'DARK', 2, T2, 'the classes’ compiled exclusions are conditions on a real σ alone (SIDE-kernel v1.5, TheBridgeComplete.lean '
                           ':157-:159) and name no function, so they hold beside the Epstein configuration the detector meets at ρ_E', 'RH-60'), []),
    ('EA-03', 'EA', 70, 'entire function of order 1 satisfying the functional equation', 'EA states that ξ is an entire function of order 1 satisfying '
     'ξ(s) = ξ(1−s).', 'theorem-supported', 'theorem', 'the standard construction, Riemann 1859 and Tate 1950, named at :81', None, []),
    ('EA-04', 'EA', 99, 'Theorem (SIDE Exclusion Principle)', 'EA states the SIDE Exclusion Principle: in a determined system with an exhaustive '
     'mechanism catalogue for a property, if no class produces the property at a point, it does not hold there.', 'argument-supported', 'argument',
     'a five-step syllogism at :101-:107, its weight in the exhaustiveness hypothesis', None, []),
    ('EA-05', 'EA', 130, 'zeros are constrained to occur in quadruples', 'EA states that the functional equation and Schwarz reflection constrain '
     'zeros to quadruples {ρ, 1−ρ, ρ̄, 1−ρ̄}, collapsing to pairs on the critical line.', 'theorem-supported', 'theorem',
     'the functional equation and the reflection principle, standard (:132)', None, []),
    ('EA-06', 'EA', 164, 'exactly two algebraic group structures', 'EA states that ℤ carries two group structures and that the quadratic form '
     'inherits one mechanism class from each.', 'argument-supported', 'argument', 'the group count is algebra; the class-per-structure step '
     'is the paper’s reading (:170)', None, []),
    ('EA-07', 'EA', 178, "By Ostrowski's theorem (1916)", 'EA cites Ostrowski’s theorem: every nontrivial absolute value on ℚ is equivalent to the '
     'real or a p-adic one.', 'theorem-supported', 'theorem', 'Ostrowski 1916, named', None, []),
    ('EA-08', 'EA', 192, 'A fourth class would require a place of ℚ', 'EA states that the transformation stage yields three classes and that a '
     'fourth would require a place of ℚ beyond ∞ and the primes.', 'argument-supported', 'argument',
     'Ostrowski and Tate named; the step “all chains pass through the Mellin transform” is stated as a lemma without its argument', None, []),
    ('EA-09', 'EA', 210, 'structural reading, not a classification theorem', 'EA states that the output stage’s two classes, C₃ and C₇, are a '
     'structural reading rather than a classification theorem.', 'argument-supported', 'argument', 'the paper’s own [ESTABLISHED] and its words at :210',
     None, []),
    ('EA-10', 'EA', 216, 'Conservation of Spectra proves it is s-dark', 'EA states that the product formula is s-dark: |x|_A = 1 gives |x|_A^s = 1 for '
     'every s, so it adds no s-dependent zero-location constraint.', 'argument-supported', 'argument',
     'argued at :216-:222; the compiled `conservation_of_spectra` is named in ME’s inventory without a pin', None, []),
    ('EA-11', 'EA', 240, 'Each mechanism class individually identifies', 'EA states that each of the seven classes identifies σ = 1/2 and fails to '
     'produce a zero at σ ≠ 1/2.', 'argument-supported', 'argument', 'the seven checks at :242-:252, the paper’s own [ESTABLISHED]', None, []),
    ('EA-12', 'EA', 281, 'All ten decompose into combinations of', 'EA states that ten research programmes decompose into combinations of the seven '
     'classes and none introduces an eighth.', 'synthesis-suggested', 'reading', 'a reading of ten programmes, the table at :268-:279', None, []),
    ('EA-13', 'EA', 296, 'crossed a dark interface', 'EA reads every programme that stalled on the way to RH as having crossed a dark interface.',
     'synthesis-suggested', 'reading', 'a retrodiction across programmes', None, []),
    ('EA-14', 'EA', 316, 'generally lack Euler products', 'EA states that Epstein zeta functions satisfy functional equations, generally lack Euler '
     'products, and can carry off-line zeros.', 'theorem-supported', 'theorem', 'Davenport–Heilbronn 1936, named at :331', None, []),
    ('EA-15', 'EA', 331, 'confirmed computationally to 10¹³+ zeros', 'EA states that ζ carries no off-line zero among the first 10¹³ and more of its '
     'zeros, a computation.', 'computationally-verified', 'computation', 'a computational record, cited', None, []),
    ('EA-16', 'EA', 341, 'Theorem 5.1 (Identity-Formation Bijection)', 'EA states the Identity-Formation Bijection: each mechanism class has one '
     'identity element, distinct classes distinct ones, every identity element in some class.', 'argument-supported', 'argument',
     'three lemmas at :351-:359 resting on I, D, S and Thom transversality', None, []),
    ('EA-17', 'EA', 367, 'The critical line is the identity subspace of arithmetic', 'EA reads the critical line as the identity subspace of '
     'arithmetic, where 0, 1 and 1/2 sit symmetric in centred coordinates.', 'synthesis-suggested', 'reading', 'a reading at :367-:369', None, []),
    ('EA-18', 'EA', 387, 'every zero of ξ forces the Euler balance at some prime', 'EA states h2 canonically in equivalent faces: the Euler balance at '
     'some prime, realization-totality at the ξ interface, the R4 positivity face and the Mellin-nonvanishing clause.', 'statement-grade',
     'statement', 'the faces are named; their equivalence is not argued in the paper', None, []),
    ('EA-19', 'EA', 399, 'the seven-class mechanism catalogue is exhaustive', 'EA places the whole logical weight on one claim, that the seven-class '
     'catalogue is exhaustive, which is h2.', 'argument-supported', 'argument', 'the paper’s own assessment at :399-:410', None, []),
    ('EA-20', 'EA', 542, "is the kernel's output", 'EA states that the conditional StructuralExhaustiveness → RH is the kernel’s output and that the '
     'paper argues for the antecedent.', 'kernel-verified', 'terminal',
     '`Integration.lean` named at :540 and the pin v1.2 at :542; the antecedent at that pin is ∀ σ, is_xi_zero σ → σ = 1/2, so the compiled '
     'conditional’s antecedent is RH in the kernel’s encoding', None, ['integration_rh', 'integration_se']),
    ('EA-21', 'EA', 542, '`SIDEKernel.formation` and `SIDEKernel.formation_count` are axiom-free', 'EA states that at SIDE-kernel v1.2 the named '
     'route terminals compile without sorry and that the formation terminals are axiom-free.', 'kernel-verified', 'terminal',
     'each name resolves at v1.2 and its statement is read; the axiom profiles are the paper’s record of 2026-07-10, which REGISTRY :95 carries, '
     'not re-printed in this act; the bare name structural_exhaustiveness_proved resolves to two theorems at v1.2 (TheBridgeComplete.lean :188, '
     'ConservationBridge.lean :29)', None, ['formation', 'formation_count', 'sep_root', 'sep_cons', 'spectral_cannon']),
    ('ME-01', 'ME', 21, 'no off-line zero exists **under the conservation clause `h2`**', 'ME states that no off-line zero exists under the '
     'conservation clause h2, the catalogue’s completeness at the ξ interface, carried openly.', 'kernel-verified', 'terminal',
     'the conditional is ConservationBridge.riemann_hypothesis at v1.2, named at ME :408 and :219', None, ['conservation_rh']),
    ('ME-02', 'ME', 49, 'properties require mechanisms', 'ME states the Mechanism Theorem: in a determined, symmetric system with independent '
     'constraints, no mechanism means no effect.', 'argument-supported', 'argument', 'a five-step derivation from I, D and S at :51-:61', None, []),
    ('ME-03', 'ME', 37, 'validated on 5/5 empirical test cases', 'ME states that I, D and S are grounded in five philosophical traditions, '
     'validated on five test cases and falsifiable.', 'statement-grade', 'statement', 'stated; the traditions and cases are not set out', None, []),
    ('ME-04', 'ME', 93, 'Verified by `native_decide` in Lean', 'ME states that the formation count 2 + 3 + 2 + 0 = 7 is checked in Lean.',
     'kernel-verified', 'terminal', 'at v1.2 the arithmetic compiles by `decide`, not `native_decide` (Core.lean :50, :53), the pin ME :408 names; '
     'the terminal states the arithmetic, not that the classes number seven', None, ['formation', 'formation_count']),
    ('ME-05', 'ME', 111, 'The catalogue is exhaustive by Ostrowski', 'ME states that the catalogue is exhaustive by Ostrowski’s theorem and that '
     'Conservation seals the interfaces.', 'argument-supported', 'argument', 'Ostrowski named for the places; the step from places to every '
     'derivation chain is argued, and ME :113 calls it h2', None, []),
    ('ME-06', 'ME', 127, 'The Euler product is causally responsible', 'ME reads the Epstein comparison as showing the Euler product causally '
     'responsible for zero confinement together with the functional equation.', 'synthesis-suggested', 'reading',
     'a causal reading of a controlled comparison', None, []),
    ('ME-07', 'ME', 137, 'Im(Λ₀(1/2 + it)) = 0', 'ME states FOCUS: the completed zeta function is real on the critical line.', 'argument-supported',
     'argument', 'the four-step derivation at :139; the terminal `focus` is named in the inventory (:349) without a pin', None, []),
    ('ME-08', 'ME', 141, 'codimension 2, generically forbidden', 'ME states that off the line a zero needs Re and Im to vanish together, codimension '
     'two.', 'argument-supported', 'argument', 'argued at :141', None, []),
    ('ME-09', 'ME', 145, "Re(Λ₀'(1/2 + it)) = 0", 'ME states the Spectral Cannon: the derivative of the completed zeta function is purely imaginary '
     'on the critical line.', 'kernel-verified', 'terminal', '`SpectralCannonFull.spectral_cannon` at SIDE-kernel v1.2, named at ME :408; its '
     'statement at that pin is exactly this', None, ['spectral_cannon', 'spectral_cannon_stmt']),
    ('ME-10', 'ME', 149, 'never returns to zero', 'ME states that at a simple zero the level curves cross perpendicularly and that along the curve '
     'Re = 0, |Im| increases and never returns to zero, so no off-line zero lies on it.', 'argument-supported', 'argument', 'argued at :149',
     ('R5', 'DARK', 2, T2, 'the argument uses the functional equation, Schwarz reflection and Cauchy–Riemann alone, all of which an Epstein ζ_Q '
                           'with real coefficients carries, and Epstein functions carry off-line zeros (EA :316, :331)', None), []),
    ('ME-11', 'ME', 151, '"generic" IS "actual"', 'ME states that in a determined system generic behaviour is actual, so codimension-two coincidences '
     'are absent for ξ.', 'argument-supported', 'argument', 'Thom transversality named; the step from a parameter-free map to “generic is actual” '
     'is argued', ('R6', 'DARK', 2, T2, 'an Epstein ζ_Q for a fixed form is equally parameter-free and carries off-line zeros, so the argument '
                                       'meets the Epstein configuration unchanged', None), []),
    ('ME-12', 'ME', 161, 'The identity forces m = R(γ₀)', 'ME states that localizing the explicit formula at a zero forces its multiplicity to equal a '
     'prime-side value, and that computation gives that value 1 at every tested zero.', 'argument-supported', 'argument',
     'argued at :161; the computation is finite',
     ('R4', 'DARK', 4, T4, 'the prime side enters, so test 2 passes, but the value is computed at finitely many zeros and the universal step is the '
                           'localization IP :339 lists as owed, a FINITE check with no ladder to every zero', None), []),
    ('ME-13', 'ME', 163, 'semisimplicity of Frobenius eigenvalues', 'ME sets the trace-formula route beside the function-field case, where the '
     'Lefschetz trace formula yields semisimplicity of Frobenius.', 'synthesis-suggested', 'reading', 'the function-field result is named; the '
     'parallel is a reading', None, []),
    ('ME-14', 'ME', 210, 'One axiom remains in the Lean formalization', 'ME states that the residual axiom all_zeros_simple is the simplicity face of '
     'h2, carried openly.', 'statement-grade', 'statement', 'stated at :210-:219; at SIDE-kernel v1.2 no declaration begins `axiom`, and '
     'all_zeros_simple occurs only in comments (PerpendicularCrossing.lean :173)', None, []),
    ('ME-15', 'ME', 275, 'This is convergent identification, not independent derivation', 'ME states that its five identification paths share the '
     'functional equation’s involution, so they identify the line and carry no weight for placement.', 'argument-supported', 'argument',
     'the paper’s correction of 2026-08-10 at :265 and :275',
     ('R3', 'NOT A ROUTE', None, '—', 'the paper itself withdraws the paths as an argument for placement: they identify the line and do not place '
                                      'a zero', None), []),
    ('ME-16', 'ME', 306, 'No axioms remain', 'ME’s conclusion states that the kernel carries zero sorry and zero axioms and that no axiom remains.',
     'statement-grade', 'statement', 'ME :219 itself names this the superseded W-9 form; kept as the paper states it', None, []),
    ('IR-01', 'IR', 28, 'Independent structures cannot conspire', 'IR states that independent structures cannot conspire, since coupling would '
     'violate their independence.', 'argument-supported', 'argument', 'argued at :30-:42', None, []),
    ('IR-02', 'IR', 54, 'same level as the Axiom of Choice', 'IR states that I, D and S are foundational principles at the level of the axiom of '
     'choice.', 'statement-grade', 'statement', 'stated at :54-:56', None, []),
    ('IR-03', 'IR', 96, '**QED** ∎', 'IR states the Mechanism Theorem by a five-step derivation from I, D and S.', 'argument-supported', 'argument',
     'the steps at :64-:94', None, []),
    ('IR-04', 'IR', 123, '⊥ F₁‚ (independent)', 'IR states that the archimedean and multiplicative structures are independent by six '
     'criteria of history, vocabulary, domain, derivation, machinery and constraint.', 'synthesis-suggested', 'reading',
     'criteria of provenance tabulated at :114-:121', None, []),
    ('IR-05', 'IR', 133, 'Loc ∉ Sym ∪ Card', 'IR states that an off-line zero is a location-type property that neither the symmetry structure nor '
     'the multiplicative structure produces.', 'argument-supported', 'argument', 'the type analysis at :127-:135',
     ('R2', 'DARK', 2, T2, 'with the symmetry structure alone, as an Epstein ζ_Q has it, the same type analysis finds no location-type mechanism, '
                           'yet the Epstein functions carry off-line zeros', None), []),
    ('IR-06', 'IR', 151, 'under the exhaustiveness premise `h2`', 'IR states that the zeros lie on the line under h2, here that the Sym ∪ Card '
     'partition is complete.', 'statement-grade', 'statement', 'the conditional as the paper re-scoped it on 2026-07-19', None, []),
    ('IR-07', 'IR', 165, 'ABC follows', 'IR states that ABC and an arithmetic P ≠ NP follow from I, D and S and that forty and more conjectures are '
     'resolved.', 'statement-grade', 'statement', 'stated; IR :14 says each entry inherits the same conditional', None, []),
    ('IR-08', 'IR', 302, 'by deriving the Mechanism Theorem from I+D+S', 'IR states that the kernel’s output is the conditional StructuralExhaustiveness '
     '→ RH and that the paper argues for its antecedent.', 'kernel-verified', 'terminal', 'the same compiled conditional as EA-20, at the pin '
     'IR :302 names', None, ['integration_rh', 'integration_se']),
    ('IP-01', 'IP', 26, '**necessary** — a manifestation of the CONVERGENCE principle', 'IP states that three approaches, topological, spectral and arithmetic, converge and that their '
     'agreement is necessary.', 'synthesis-suggested', 'reading', 'a convergence reading at :18-:27', None, []),
    ('IP-02', 'IP', 87, 'σ = 1/2 is the unique fixed point', 'IP states that σ = 1/2 is the unique fixed point of the functional equation’s symmetry.',
     'argument-supported', 'argument', 'one line of algebra at :92',
     ('R7', 'DARK', 2, T2, 'the fixed point of s ↦ 1 − s is shared by every function with this functional equation, an Epstein ζ_Q among them, '
                           'so it places no zero on the line', None), []),
    ('IP-03', 'IP', 97, 'THEOREM (Euler Product Balance)', 'IP states that the Euler product’s contributions balance, p^(−σ) = p^(−(1−σ)), only at σ = 1/2.',
     'kernel-verified', 'terminal', '`balance_theorem` of `Voice1.lean`, which EA :538 and :542 name at v1.2 as the balance theorem; its '
     'statement at that pin is this equivalence for a prime p', None, ['balance']),
    ('IP-04', 'IP', 125, 'This is an **exact identity**', 'IP states that the Weil explicit formula is an exact identity between a sum over zeros '
     'and a sum over primes.', 'theorem-supported', 'theorem', 'the Weil explicit formula, named; IP :13 re-scopes the paper’s use of it to '
     'an INTERFACES-with-premises step (conditional convergence)', None, []),
    ('IP-05', 'IP', 137, 'Residue at first zero = 1.0000', 'IP reports the residue at the first zero computed as 1.0000.', 'computationally-verified',
     'computation', 'a single computation, reported', None, []),
    ('IP-06', 'IP', 167, '|Im(ξ)| is strictly monotonically increasing', 'IP states that along the curve Re(ξ) = 0 from a simple zero, |Im(ξ)| '
     'increases strictly.', 'argument-supported', 'argument', 'the argument at :169-:174 rests on its step 3, no critical points on the curve, '
     'which the paper does not give', ('R5', 'DARK', 2, T2, 'the same route as ME-10, using no prime side', None), []),
    ('IP-07', 'IP', 176, 'grows ~100× from σ=0.5 to σ=1 for all 10 zeros', 'IP reports |Im(ξ)| growing about a hundredfold from σ = 0.5 to σ = 1 '
     'along the curves of ten zeros.', 'computationally-verified', 'computation', 'a computation at ten zeros', None, []),
    ('IP-08', 'IP', 298, 'Verified (10 zeros)', 'IP reports simplicity checked at ten zeros and the zero count N(T) matched with error under 0.5.',
     'computationally-verified', 'computation', 'the verification table at :294-:302', None, []),
    ('IP-09', 'IP', 341, 'Prove simplicity unconditionally', 'IP lists as owed the localization argument’s formalization, verification beyond ten '
     'zeros and an unconditional simplicity.', 'statement-grade', 'statement', 'the paper’s own open items at :339-:341', None, []),
    ('IP-10', 'IP', 317, '*this is evidence for the antecedent*', 'IP states that the paths’ independence is evidence for the antecedent h2 and not a '
     'discharge of it.', 'argument-supported', 'argument', 'the paper’s re-scope at :317', None, []),
]

ROUTE_ROWS = {'RH-60': 'DARK, test 2', 'RH-58': 'NOT A ROUTE', 'RH-59': 'DARK, test 1', 'RH-02': 'FACE'}


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


def resolve_kernel():
    """### every kernel read at SIDE-kernel v1.2: [(key, ok, line)]"""
    out = []
    for k, (f, n, needle, _what) in KREADS.items():
        ls = lines_of(show(f, KPIN, SKER))
        l = ls[n - 1] if 0 < n <= len(ls) else ''
        out.append((k, needle in l, l))
    return out


def sieve_rows():
    """### the sieve v0.4 rows the routes meet, read at the pin: {id: (verdict, test)}"""
    t = lines_of(show('phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md'))
    out = {}
    for l in t:
        m = re.match(r'^\| ((?:RH|FD)-\d\d) \| ', l)
        if m and m.group(1) in ROUTE_ROWS and m.group(1) not in out:   # ### the body row, met first; back-matter rows repeat the id
            c = [x.strip() for x in l.strip().strip('|').split(' | ')]
            out[m.group(1)] = (c[4], c[5])
    return out


def grade_ok(c):
    return c[5] in GRADES and c[6] in NEEDS[c[5]] and (c[5] != 'kernel-verified' or bool(c[9]))


# ================================================================================ W-ORD-TAG-REMOTES: the unpushed tags and their citations
LEDGERS = ('FINDINGS.md', 'OPEN_TRAILS.md', 'REGISTRY.md', 'SPIRAL_MAP.md', 'ERRATA.md', 'VERIFICATION_LOOM.md', 'README.md')


def tag_citations(repo, tag):
    """### the ledger lines at the pin naming the repo (with or without its `SIDE-` prefix) and the tag within 40 characters on one line,
    ### the tag a whole version (`v0.1` does not match inside `v0.1.0`)."""
    name = repo[len('SIDE-'):] if repo.startswith('SIDE-') else repo
    rx = re.compile(r'(?:SIDE-)?%s\b[^|\n]{0,40}?\b%s(?![.\d])' % (re.escape(name), re.escape(tag)))
    hits = []
    for f in LEDGERS:
        for i, l in enumerate(lines_of(show(f)), 1):
            if rx.search(l):
                hits.append('%s :%d' % (f, i))
    return hits


def unpushed_tags():
    J = json.load(open(os.path.join(ROOT, 'data', 'b610_census.json'), encoding='utf-8'))
    out = []
    for repo, rt in sorted(J['remotes'].items()):
        for tag, sha in rt.get('local_only') or []:
            out.append(dict(repo=repo, tag=tag, sha=sha, cited=tag_citations(repo, tag)))
    return out


def main():
    rc = resolve_claims()
    bad = [x for x in rc if not x[1]]
    print('### claims %d ; needles failing %s' % (len(C), [(i, l[:80]) for i, _o, l in bad] or 'NONE'))
    rk = resolve_kernel()
    print('### kernel reads %d ; failing %s' % (len(rk), [(k, l[:80]) for k, ok, l in rk if not ok] or 'NONE'))
    print('### grades out of rule: %s' % ([c[0] for c in C if not grade_ok(c)] or 'NONE'))
    print('### routes: %s' % [(c[0], c[8][0], c[8][1], c[8][2], c[8][5]) for c in C if c[8]])
    print('### sieve rows: %s' % sieve_rows())
    from collections import Counter
    print('### grade counts: %s' % dict(Counter(c[5] for c in C)))
    for t in unpushed_tags():
        print('  %-30s %-6s %s cited %s' % (t['repo'], t['tag'], t['sha'], t['cited'] or 'NONE'))


if __name__ == '__main__':
    main()
