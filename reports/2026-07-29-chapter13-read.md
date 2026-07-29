# Chapter 13 statement-read — the h2 discharge question — 2026-07-29

Same method as the core-terminal statement-read, applied to the manuscript. **READ AND REPORT ONLY; no
edits; RH rail read-only (no authorization sought).** Source: `day1/A_Place_to_Stand.md` Chapter 13
(Conservation of Spectra), its Route-3 discharge discussion (Part V, §25.5), and the Lean premise at
SIDE-kernel v1.3 (`0bc21c0`). *(There is no `phase1.5/spectral/CONSERVATION_OF_SPECTRA*.md`; the fuller
argument is Chapter 13 itself + the `Spectral_Inertness` companion named in §13.4 + §27.3.)*

## (1) What Chapter 13 proves — verbatim

**§13.2 — The s-Darkness Theorem:**
> **Theorem.** The product formula acts independently of the spectral parameter s in the Tate integral
> construction of ξ(s).
>
> *Proof.* The compact group C¹_ℚ = ker(|·|_𝔸) is defined by the product formula: it is the subgroup of
> ideles with adelic norm 1. On this group, |x|_𝔸 = 1 by definition. Therefore |x|_𝔸^s = 1^s = 1 for every
> s ∈ ℂ. The Tate integral M[Φ](s) = ∫ Φ(t) · t^s dt/t takes two inputs: the test function Φ (determined by
> C¹_ℚ, hence s-independent) and the kernel t^s (the sole source of s-dependence). The product formula
> contributes Φ. The spectral parameter s enters only through the kernel.

> **Definition.** A structural constraint is *spectrally inert* (or *s-dark*) if it determines the domain
> geometry of a spectral object but contributes no s-dependent content.

**§13.3 — Consequence:**
> Every constraint on the zero locations of ξ(s) traces to ℚ's field structure acting through the additive
> component (functional equation) and the multiplicative component (Euler product). The product formula —
> the interface between them — is structurally essential and spectrally silent. No force outside ℚ's field
> structure speaks.

The compiled counterpart is `ProductFormula.conservation_of_spectra` (SIDE-kernel, n₄ = 0, κ = 1). Note the
**quantifier content of Chapter 13's theorem: there is none over ξ-zeros.** It is a statement about the
*product formula* (the coupling/interface) — that it introduces no s-dependent content into the Tate
integral — and §13.3's sealing corollary: *no external force* acts on the zeros.

## (2) ConservationHypothesis — verbatim (`Bridge/ConservationBridge.lean`, v1.3 `0bc21c0`)

```lean
def ConservationHypothesis : Prop :=
  ∀ (σ : ℝ), is_xi_zero σ →
  ∃ (p : Nat) (hp : Nat.Prime p),
  (prime_as_real p hp) ^ (-σ) = (prime_as_real p hp) ^ (-(1 - σ))
```
Quantifier content: **∀ ξ-zero, ∃ a prime** at which the Euler balance `p^(-σ) = p^(-(1-σ))` holds — i.e.
`σ = 1 - σ`, hence `σ = 1/2`, *forced at that prime*.

## (3) THE QUESTION — does Chapter 13's theorem ENTAIL ConservationHypothesis?

**No.** Chapter 13 proves the product formula is *s-dark* — a per-place / structural fact about the
coupling (it contributes no s-dependent content), with **no quantifier over ξ-zeros and no claim that any
prime *activates* a balance at any zero**; ConservationHypothesis is a **global, per-zero, positive
forcing** claim (∀ ξ-zero, ∃ an activating prime), and getting from the first to the second requires the
additional step that the multiplicative structure *forces* `σ = 1/2` at every zero — which is exactly the
programme's **open sign/positivity clause**, not established anywhere in Chapter 13.

The monograph says this itself, in its own words (Part V, Route-3 discussion):
> "Chapter 13's Conservation of Spectra Theorem — the s-darkness of the product formula, proved within ZFC
> from Tate's thesis — is the unconditional conservation *certificate* that motivates it, **a distinct
> proposition**." … "Conservation of Spectra — the Chapter 13 theorem — is the **certificate that motivates
> the premise, not the premise's discharge**."

So entailment fails **by the monograph's own account**: Chapter 13 is a distinct, motivating certificate,
explicitly *not* the discharge of ConservationHypothesis.

## (5) The shortfall, both sides quoted, not softened

- **Chapter 13 (§13.2) establishes:** *"The product formula acts independently of the spectral parameter s
  in the Tate integral construction of ξ(s)"* — the interface is s-dark; §13.3: *"No force outside ℚ's field
  structure speaks."* This is a **sealing / negative** fact (nothing external can act) and a
  **domain-geometry** fact about the coupling. Zero quantifiers over zeros; zero claims of activation.
- **ConservationHypothesis demands:** *"∀ σ, is_xi_zero σ → ∃ p hp, (prime_as_real p hp)^(-σ) =
  (prime_as_real p hp)^(-(1-σ))"* — a **positive, per-zero, existential-prime forcing**: at *every* zero,
  *some* prime's Euler balance holds, forcing `σ = 1/2`.
- **The shortfall:** s-darkness + the seal give *"no external force acts on the zeros"* and *"the mechanism
  catalogue is complete"*; they do **not** give *"the multiplicative structure forces σ = 1/2 at every
  zero."* Going from the seal to the forcing is the open clause the monograph localizes precisely (§9 /
  §27.3): *"that this participation forces σ = 1/2 is the one open clause … the inequality λ_Z(n) ≥ −λ_A(n)
  for every n (RH-equivalent) … the all-n tail open,"* with the boundary drawn exactly: *"Λ(n) ≥ 0 yields
  the edge of the strip — the σ = 1 zero-free region — never its center; no classical result crosses to the
  critical line."* The distance from Chapter 13's conclusion to ConservationHypothesis **is** that
  never-crossed distance to the center.

## (4-register) Which frontier is h2 on?

Because entailment does **not** hold, the (4) branch ("entailment holds → name the absent Mathlib objects,
register = formalization-frontier") **does not apply**, and it would be wrong to file h2 as a
formalization-frontier premise. The shortfall is **mathematical, not infrastructural** — the monograph's own
kernel-boundary note is explicit: *"the kernel boundary here is mathematical content, not an engineering
deferral: the premise is not awaiting library infrastructure but discharge."* **h2's register is
research-frontier** (a genuinely open forcing clause), not formalization-frontier. Chapter 13 discharges the
*seal* (s-darkness, no external force); it does not discharge the *forcing*.

## (6) Reconciliation with the h2-sharpening report (relay `e16b615`)

**No contradiction — the two are the same finding at two registers.** e16b615 concluded discharge requires
*"the positive space on the zeros"* (the positivity/realization; the two-channel all-n inequality). This
read concludes Chapter 13 (s-darkness) does not entail ConservationHypothesis because the missing step is
the *positive forcing* — the identical object, seen at the multiplicative place. Chapter 13 is the
**certificate/seal** (register: the coupling is silent); the open clause is the **positive forcing** (register:
the balance is activated / the space is realized on the zeros). Both readings are correct; both name the same
research-frontier residue. The h2-sharpening's five-register §27.3 gathering is precisely why: the
"balance-to-positivity distance at the multiplicative place" and the "spectral-realization distance" are two
of the five registers of the one premise — Chapter 13 sits *before* both.

## For the author — the register question

On the strength of this read: **h2 is a research-frontier premise, not a formalization-frontier one.**
Chapter 13's s-darkness theorem is compiled and is a genuine *seal* (no external force acts on the zeros),
but it is a *distinct proposition* from ConservationHypothesis and does not entail it — the monograph says
so in its own text. The remaining distance is the open positive-forcing clause (λ_Z(n) ≥ −λ_A(n) for all n /
the positive space on the zeros), which no library infrastructure would close. No edits made; RH rail
read-only; nothing deposited.
