# Core-terminal statement-read — SIDE-kernel v1.3 (`0bc21c0`) — 2026-07-29

A READ, not an edit. No kernel or paper changed. Built at the pin (Mathlib cached, identical pin/toolchain),
statements read by `#check`/`#print` via `lake env lean`. Kernel restored to `derivative-engine` after.
Grades are read from the STATEMENTS, not the axiom profiles. **One salt-check finding surfaced — Voice 7
(`c7_forces_half`) concludes `σ = σ`, a tautology, not `σ = 1/2`** (STEP TWO / STEP THREE).

## STEP ZERO — the three route terminals: statements and conclusion unfolding (verbatim)

```
structural_exhaustiveness_proved : _root_.StructuralExhaustiveness

SpectralCannonFull.spectral_cannon : ∀ (t : ℝ), (deriv completedRiemannZeta₀ { re := 1 / 2, im := t }).re = 0

ConservationBridge.riemann_hypothesis : ConservationBridge.ConservationHypothesis → RiemannHypothesis

def _root_.StructuralExhaustiveness : Prop :=
Fintype.card MechanismClass = 7 ∧
  (∀ (c : MechanismClass), ¬produces_offline c) ∧
    ∀ (f : AbsoluteValue ℚ ℝ),
      f.IsNontrivial →
        f.IsEquiv Rat.AbsoluteValue.real ∨
          ∃ p, Nat.Prime p ∧ ∃ (x : Fact (Nat.Prime p)), f.IsEquiv (Rat.AbsoluteValue.padic p)

def RiemannHypothesis : Prop :=
∀ (s : ℂ), riemannZeta s = 0 → (¬∃ n, s = -2 * (↑n + 1)) → s ≠ 1 → s.re = 1 / 2

inductive MechanismClass : Type
  MechanismClass.C1_schwarz | C2_euler | C3_functional_eq | C4_modular
  | C5_spectral | C6_cauchy_riemann | C7_hadamard

def produces_offline : MechanismClass → Prop :=
fun x => match x with
  | .C1_schwarz        => ∃ σ, σ ≠ 1 / 2 ∧ σ = 1 - σ
  | .C2_euler          => ∃ σ, σ ≠ 1 / 2 ∧ -σ = -(1 - σ)
  | .C3_functional_eq  => ∃ σ, σ ≠ 1 / 2 ∧ 1 - σ = σ
  | .C4_modular        => ∃ σ, σ ≠ 1 / 2 ∧ 1 - σ = σ
  | .C5_spectral       => ∃ σ, σ ≠ 1 / 2 ∧ σ - 1 / 2 = 0
  | .C6_cauchy_riemann => ∃ σ, σ ≠ 1 / 2 ∧ techne_kernel_voice3b.zero_codimension σ = 1
  | .C7_hadamard       => ∃ σ, hadamard_contrib σ ≠ hadamard_contrib (1 / 2)

completedRiemannZeta₀ : ℂ → ℂ   -- Mathlib
riemannZeta : ℂ → ℂ             -- Mathlib
```

**Answer, per terminal — is the conclusion about Mathlib zeta zeros, or a local predicate?**

1. **`structural_exhaustiveness_proved`** (Route 1, root namespace / `TheBridgeComplete`, **no hypothesis**).
   Conclusion `_root_.StructuralExhaustiveness` is a **LOCALLY-DEFINED predicate**: `MechanismClass` (a local
   7-constructor inductive) has cardinality 7, no class `produces_offline` (a local match on σ-algebra
   conditions), and the Ostrowski trichotomy holds on `AbsoluteValue ℚ ℝ` (Mathlib's rational absolute
   values). **It does NOT mention `riemannZeta` or its zeros.** It is a structural + Ostrowski statement.

2. **`SpectralCannonFull.spectral_cannon`** (Route 2, **no hypothesis**). Conclusion is **directly about
   Mathlib's `completedRiemannZeta₀`**: `(deriv completedRiemannZeta₀ (1/2 + it)).re = 0` — the completed
   zeta's derivative has zero real part on the critical line. It IS about the Mathlib object, but asserts a
   **property** (Re of derivative = 0 on the line), **not** that zeros lie on the line — a sub-RH proposition.

3. **`ConservationBridge.riemann_hypothesis`** (Route 3). Conclusion `RiemannHypothesis` unfolds to Mathlib's
   `RiemannHypothesis` — **`∀ s, riemannZeta s = 0 → (nontrivial) → s.re = 1/2`** — genuinely **about the
   zeros of Mathlib's `riemannZeta`.** It is reached only under the hypothesis `ConservationHypothesis`.

## STEP ONE — hypotheses (verbatim + discharge status)

```
theorem ConservationBridge.riemann_hypothesis : ConservationHypothesis → RiemannHypothesis :=
fun h_cons => rh_from_structural_exhaustiveness (ConservationBridge.structural_exhaustiveness_proved h_cons)

theorem ConservationBridge.structural_exhaustiveness_proved :
  ConservationHypothesis → techne_kernel_integration.StructuralExhaustiveness :=
fun h_cons σ h_zero =>
  Exists.casesOn (conservation_activates_balance h_cons σ h_zero) fun p h =>
    Exists.casesOn h fun hp hbal => (techne_kernel_voice1.balance_theorem p hp σ).mp hbal

def techne_kernel_integration.StructuralExhaustiveness : Prop :=
∀ (sigma : ℝ), is_xi_zero sigma → sigma = 1 / 2

def ConservationBridge.ConservationHypothesis : Prop :=
∀ (σ : ℝ), is_xi_zero σ →
  ∃ p, ∃ (hp : Nat.Prime p),
    techne_kernel_voice1.prime_as_real p hp ^ (-σ) = techne_kernel_voice1.prime_as_real p hp ^ (-(1 - σ))

def techne_kernel_xidef.is_xi_zero : ℝ → Prop :=
fun sigma => ∃ t, riemannZeta { re := sigma, im := t } = 0 ∧
  (¬∃ n, { re := sigma, im := t } = -2 * (↑n + 1)) ∧ { re := sigma, im := t } ≠ 1
```

- **Route 1 (`structural_exhaustiveness_proved`):** NO hypothesis. **All discharged in-kernel**
  (`⟨seven_classes, none_produce, ostrowski_exhaustive_prime⟩`). Unconditional.
- **Route 2 (`spectral_cannon`):** NO hypothesis (∀ t only). **Discharged in-kernel** (Schwarz reflection +
  functional equation). Unconditional.
- **Route 3 (`riemann_hypothesis`):** ONE hypothesis, `ConservationHypothesis` — **(ii) a named premise
  expected from a manuscript.** It is the programme's h2 = the Realization-Totality / Euler-balance premise,
  **monograph §27.3** ("every ξ-zero forces the Euler balance at some prime"). NOT discharged in the kernel;
  carried as the explicit hypothesis. Note `is_xi_zero` is defined over **Mathlib `riemannZeta` zeros**, so
  `techne_kernel_integration.StructuralExhaustiveness` (Route 3's intermediate) is genuinely about the
  Mathlib zeros, and `rh_from_structural_exhaustiveness` lifts `∀σ, is_xi_zero σ → σ=1/2` to Mathlib RH.

## STEP TWO — the Voice terminals + formation (verbatim `#check`)

```
techne_kernel_voice1.balance_theorem : ∀ (p : ℕ) (hp : Nat.Prime p) (s : ℝ),
  techne_kernel_voice1.prime_as_real p hp ^ (-s) = techne_kernel_voice1.prime_as_real p hp ^ (-(1 - s)) ↔ s = 1 / 2
techne_kernel_voice2.symmetries_agree_iff : ∀ (sigma : ℝ),
  techne_kernel_voice2.conjugate_re sigma = techne_kernel_voice2.reflect_re sigma ↔ sigma = 1 / 2
techne_kernel_voice3.reflect_fixed_iff : ∀ (s : ℝ), techne_kernel_voice3.reflect s = s ↔ s = 1 / 2
techne_kernel_voice5.modular_forces_half : ∀ (sigma : ℝ), techne_kernel_voice5.S_action sigma = sigma → sigma = 1 / 2
techne_kernel_voice6.self_adjoint_forces_half : ∀ (sigma : ℝ),
  techne_kernel_voice6.self_adjoint_constraint sigma → sigma = 1 / 2
techne_kernel_voice7.c7_forces_half : ∀ (sigma : ℝ), techne_kernel_voice7.topological_rests sigma → sigma = sigma
SIDEKernel.formation : 2 + 3 + 2 + 0 = 7
SIDEKernel.formation_count : SIDEKernel.n1 + SIDEKernel.n2 + SIDEKernel.n3 + SIDEKernel.n4 = 7
theorem SIDEKernel.formation : 2 + 3 + 2 + 0 = 7 := of_decide_eq_true (id (Eq.refl true))
```

- **voice1 `balance_theorem`**, **voice2 `symmetries_agree_iff`**, **voice3 `reflect_fixed_iff`** — each a
  biconditional `[local algebraic identity] ↔ sigma = 1/2`; the identity forces σ = 1/2, no premise. Real content.
- **voice5 `modular_forces_half`**, **voice6 `self_adjoint_forces_half`** — each `[local constraint] → sigma = 1/2`;
  a genuine forcing (hypothesis is a local predicate; conclusion is σ = 1/2). Real content.
- **voice7 `c7_forces_half`** — **conclusion is `sigma = sigma`, a tautology — NOT `sigma = 1/2`.** The
  statement is `∀ sigma, topological_rests sigma → sigma = sigma`, true for every σ regardless of the
  hypothesis. **This terminal does NOT force σ = 1/2**; its name overstates its statement. *(Finding, below.)*
- **`SIDEKernel.formation` / `formation_count`** — decidable arithmetic (2+3+2+0=7 / n₁+n₂+n₃+n₄=7),
  `of_decide_eq_true (Eq.refl true)`, real content.

*(`prime_as_real`, `rh_from_structural_exhaustiveness`, and `topological_rests` bodies were not separately
printed — repeated `lake env lean` invocations that import Mathlib's RiemannZeta timed out on olean load;
their usage forms are captured verbatim above and the terminals' TYPES are exact.)*

## STEP THREE — grade each terminal (from the statement, not the profile)

| terminal | grade | basis |
|:--|:--|:--|
| `structural_exhaustiveness_proved` (Route 1, root) | **DERIVES** | unconditional; proves the structural three-conjunct (MechanismClass card 7 · ∀c ¬produces_offline · Ostrowski trichotomy). Local + Mathlib-Ostrowski; a real theorem, not about zeta zeros |
| `SpectralCannonFull.spectral_cannon` (Route 2) | **DERIVES** | unconditional; a real property of Mathlib `completedRiemannZeta₀`'s derivative on the line (sub-RH, not off-line exclusion) |
| `ConservationBridge.riemann_hypothesis` (Route 3) | **INTERFACES-on-`ConservationHypothesis`** | conclusion = Mathlib RH (about `riemannZeta` zeros); premise = h2 = the Realization-Totality/Euler-balance premise, **monograph §27.3**, named openly, not discharged |
| `techne_kernel_voice1.balance_theorem` | **DERIVES** | biconditional, algebraic identity ⟺ σ=1/2 |
| `techne_kernel_voice2.symmetries_agree_iff` | **DERIVES** | biconditional ⟺ σ=1/2 |
| `techne_kernel_voice3.reflect_fixed_iff` | **DERIVES** | biconditional ⟺ σ=1/2 |
| `techne_kernel_voice5.modular_forces_half` | **DERIVES** | local constraint → σ=1/2 |
| `techne_kernel_voice6.self_adjoint_forces_half` | **DERIVES** | local constraint → σ=1/2 |
| **`techne_kernel_voice7.c7_forces_half`** | **SHELL / ENCODES-CONCLUSION** | **conclusion `σ = σ` is a tautology; it does NOT force σ=1/2.** The name overstates the statement |
| `SIDEKernel.formation` / `formation_count` | **DERIVES** | decidable arithmetic, axiom-free (`Eq.refl true`) |

## The finding — `voice7.c7_forces_half` is vacuous as a "forces half" claim

`techne_kernel_voice7.c7_forces_half : ∀ (sigma : ℝ), topological_rests sigma → sigma = sigma`. The
conclusion `σ = σ` holds for every σ irrespective of the hypothesis, so the terminal establishes nothing
about σ = 1/2 — it proves `topological_rests σ → True`. **Consequence:** any Correspondence row that cites
`voice7.c7_forces_half` as the C₇ "σ = 1/2 identification" (the "seven voice identifications" rows in
`THE_UNCONDITIONAL_SURROUND` §4 and `SIMPLICITY_OF_RIEMANN_ZEROS`) **overstates it** — six voices force
σ=1/2 (voice1/2/3/5/6), the seventh (C₇/Hadamard) does not, at least not through this terminal. The RH proof
does **not** rest on it: Route 3 goes through `balance_theorem` (voice1), and `structural_exhaustiveness_proved`
uses `produces_offline`'s C₇ case (`hadamard_contrib σ ≠ hadamard_contrib (1/2)`, a distinct non-vacuous
condition), not `c7_forces_half`. So the finding is a **statement-fidelity overstatement in the citing
Correspondence rows**, not a hole in the proof.

**These are RH-rail files.** Per the ruling, the rail's Correspondence rows are written only after the author
reads this. The correction (rescope the C₇ voice row: `c7_forces_half` concludes `σ=σ`, so C₇'s forcing is
carried by `produces_offline`'s Hadamard case / manuscript, not by this terminal) is **held for the author**.

## Summary

- **Route 1** `structural_exhaustiveness_proved` — **DERIVES**, unconditional, conclusion a local structural
  + Ostrowski predicate (not zeta zeros).
- **Route 2** `spectral_cannon` — **DERIVES**, unconditional, conclusion a real property of Mathlib
  `completedRiemannZeta₀`'s derivative on the line (sub-RH).
- **Route 3** `riemann_hypothesis` — **INTERFACES-on-`ConservationHypothesis`** (h2, §27.3), conclusion
  Mathlib RH about `riemannZeta` zeros; the premise named openly, not discharged.
- Voices 1/2/3/5/6 **DERIVE** σ=1/2; **Voice 7 `c7_forces_half` is SHELL** (`σ=σ`) — the one salt-check catch.
- Formation terminals **DERIVE** (decidable arithmetic).

No kernel or paper changed (read only); SIDE-kernel restored to `derivative-engine` (`27a3ae7`). The RH-rail
Correspondence correction for the C₇ voice row is held for the author.
