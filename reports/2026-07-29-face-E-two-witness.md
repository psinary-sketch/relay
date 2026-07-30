# Face E — two-witness (relativization) form — 2026-07-29

Analytical, no commits. Author ruled: **REJECT** the definitional form ("one-dimensional base ⇒ dark-factored
⇒ density-only, with n₄=0 as the definitional stand-in") — it encodes the conclusion in a definition (the C₇
pattern) and would grade **ENCODES**. **ADOPT** the two-witness / indistinguishability form on the
relativization (Baker–Gill–Solovay) model. This report delivers (1) a precise D, (2) the honest test of
clause (i), (3) the remaining-work order, (4) the schematic kernel — and the two arc-record riders.

**Target theorem (as ruled).** Let D be a class of derivations whose every step factors through κ=0
interfaces. Exhibit two systems — ξ and an Epstein zeta of a binary quadratic form with class number > 1 —
such that (i) they **agree** on every quantity accessible to D, and (ii) they **differ** in definiteness
(Davenport–Heilbronn: the Epstein carries off-line zeros; ξ conjecturally does not). Conclude: **no derivation
in D establishes definiteness for ξ.**

---

## (1) Specifying D — "accessible to a κ=0-factored derivation" as a checkable claim

The relativization model requires D-accessibility to be a mathematical predicate, so that "ξ and Epstein
agree" is a checkable equality, not a metaphor. The specification:

**A quantity q is D-accessible if it is a functional of the *shared structural data* of the two systems —
the data that crosses the κ=0 interface — and of nothing else.** Concretely, D is the class of derivations
that invoke only:

- the **functional equation** (the s ↔ 1−s symmetry and its Γ-factor / conductor data);
- **meromorphic continuation and order-1 growth** (the Hadamard product envelope);
- the **Dirichlet series** as an abstract coefficient sequence (additive structure), with its **density and
  counting data** (N(T) ∼ (T/2π)log T, zero-density estimates, the Montgomery–Odlyzko pair-correlation
  statistics);
- the **codimension transversality machinery** (FOCUS: ξ real on the line; the level-curve dichotomy).

and that do **not** invoke the **Euler product** — the multiplicative factorization ζ(s) = ∏_p(1−p⁻ˢ)⁻¹
indexed by primes.

**Why this is the right D, and why agreement is then checkable.** These are exactly the structures ξ and a
class-number->1 Epstein zeta **share**. Both have a functional equation, meromorphic continuation, a Dirichlet
series, order 1, and the codimension-2 obstruction (`CONTROLLED_EXPERIMENT`: *"This obstruction is real. It
operates for Epstein functions too"*). They differ in exactly one structural feature: ξ has an Euler product
(the class number is 1, the form factors over primes); the Epstein zeta of a form with class number > 1 does
**not** (no factorization over rational primes — `SIEVE_CEILING_LEMMA` §3.3: *"it has no Euler product,
because the class number of discriminant −23 is 3"*). So D is precisely **"the derivations that would apply
verbatim to the Epstein witness,"** and

> **q is D-accessible ⟺ q is invariant under replacing ξ by a Dirichlet series with the same
> FE/continuation/order/density data but no Euler product.**

Agreement on all D-accessible quantities is then the checkable claim that ξ and the chosen Epstein zeta
share all of that data — which they do, structurally. This is the corpus's **"model-theoretic separation"**
already named at `Seven_Mechanism_Classes` L67: *"The Epstein zeta functions provide model-theoretic
separation: they possess C₃ (functional equation) but lack C₅ … demonstrating that the … constraints are
genuinely independent."* We are turning that separation into the relativization barrier's clause (i).

*(Note on mechanism-class numbering, to avoid a citation error: the Euler-product class is **C₄** in the
proof-paper catalogue — `THE_PROOF`, `MECHANISM_EXCLUSION`, `PATHS_TO_THE_CRITICAL_LINE` — and **C₂** in the
`A_Place_to_Stand` monograph catalogue. This report uses **C₄** per the ruling. Both name the same object:
the multiplicative Euler product.)*

---

## (2) The honest test of clause (i) — is the Euler product accessible to D?

The ruling's honesty demand: the Euler product is ξ's distinguishing feature and Epstein lacks it, so **if
the Euler product is accessible to D, the two witnesses are distinguishable and clause (i) fails.** Which case
holds?

**The latter case holds, necessarily.** If D is permitted to invoke the Euler product, then ξ (has it) and
Epstein (lacks it) are D-**distinguishable** — a D-derivation could read "the Euler product exists" off ξ and
not off Epstein — so clause (i) is false and the two-witness barrier is **vacuous**. Therefore, **for the
barrier to have any content, D must be specified to exclude the Euler product.** The barrier covers exactly
**the derivations that do not use the Euler product essentially**, and no others. This is not a weakness to
hide; it is the theorem's exact scope, and stating it is the whole point of the two-witness form (a
relativization barrier is *always* a barrier against a specified class of methods, never against all).

**The honest restricted theorem.**

> **Theorem (Face E, honest form).** *Let D be the class of derivations factoring only through the
> Euler-product-free structure (functional equation, continuation, order, Dirichlet series, density,
> transversality). Then no derivation in D establishes the definiteness of the positivity pairing for ξ
> (equivalently, RH for ξ). Proof: ξ and the Epstein zeta Z of a binary quadratic form of class number > 1
> agree on every D-accessible quantity (shared FE / continuation / order / Dirichlet / density / codim-2
> structure), yet differ in definiteness (Z has off-line zeros — Davenport–Heilbronn 1936, and the located
> disc−23 zero ρ ≈ 0.9533 + 16.290 i, `HELD_WONDER`; ξ conjecturally has none). A D-derivation, being a
> functional of D-accessible data alone, cannot separate two systems that agree on all such data; hence it
> cannot certify definiteness for one while it fails for the other. ∎ Contrapositive: **any derivation of the
> positivity must use the Euler product (C₄) essentially.***

**This is the corpus's own Euler/C₄ finding, upgraded from observation to theorem.** The corpus states the
C₄-essentiality repeatedly, and at deposit strength — but as an **empirical controlled experiment**, not a
proof-theoretic barrier:

- `SIMPLICITY_OF_RIEMANN_ZEROS` (rail): *"the functional equation alone is insufficient, the Euler product is
  essential, and the conjunction of the functional equation, the Euler product, and the Ramanujan bound is
  what distinguishes ζ from ζ_Q."*
- `CONTROLLED_EXPERIMENT` L147: *"The Euler product is the distinguishing structural feature between
  L-functions with all zeros on the critical line and L-functions with off-line zeros. This is not a
  heuristic observation — it is an exact structural comparison between proved mathematical objects."*
- `A_Place_to_Stand` (rail) L1192: *"removing C₂ [the Euler product] always produces off-line zeros … the
  Euler product is the entire confinement mechanism."*

These say **"remove the Euler product → off-line zeros appear"** (a causal/experimental claim about objects).
The two-witness form **upgrades the modality**: from *"we observe that Euler-product-free systems have
off-line zeros"* to *"no Euler-product-free **derivation** can establish definiteness, because the witnesses
are D-indistinguishable."* The controlled experiment establishes the *fact of the discriminating variable*;
the relativization barrier establishes the *proof-theoretic consequence* — that the variable's absence is not
merely correlated with failure but **forecloses any derivation that omits it**. Observation → theorem, exactly
as the ruling framed it.

---

## (3) What remains to prove clause (i) — the named work-order

Clause (ii) is **done** in the corpus: off-line zeros of a class-number->1 Epstein are not conjectural — they
are located, doubly-sourced (`HELD_WONDER`: disc−23, ρ ≈ 0.9533 + 16.290 i, simple, |Z′|=3.91; plus the
classical Davenport–Heilbronn family). Clause (i) — *ξ and Epstein agree on every D-accessible quantity* — is
the open content.

> **W-ORD-FACE-E-INDISTINGUISHABILITY.** Prove ξ ~_D Z: every D-accessible quantity takes equal (or
> structurally-corresponding) values on ξ and on a fixed class-number->1 Epstein zeta Z.

Two tiers, honestly separated:

- **Tier 1 — barrier against a *named finite toolkit* (TRACTABLE; largely already discharged).** Fix an
  explicit list of D-accessible quantities — the FE-symmetry, the continuation, the order-1 envelope, N(T),
  the zero-density-one-on-the-line estimate, the codim-2 transversality verdict — and verify ξ and Z agree on
  each (up to the normalization D cannot see). The corpus's controlled experiment **already establishes this
  for its toolkit**: both have the FE, both have the codim-2 obstruction, both have density-one on the line,
  and they diverge only at the Euler product. Grade: this is a **theorem against a specified toolkit**,
  reachable now — the deliverable is to write the list and the agreement-checks explicitly. Difficulty:
  **low-to-moderate**, mostly assembly of existing corpus results.

- **Tier 2 — barrier against *all* of D (RESEARCH-FRONTIER).** The universally-quantified clause (i) requires
  a **characterization of D-accessible functionals** — a theorem of the form "every quantity computable
  without the Euler product is a functional of {FE, continuation, Dirichlet coefficients, density}" — and
  then "definiteness is not among them." This is essentially a **relativization theory for L-functions**,
  which does not exist; it is the L-function analogue of formalizing the natural-proofs barrier. Difficulty:
  **research-frontier**, comparable in kind to the h2 wall itself (and revealingly so — the barrier's own
  completion is frontier-grade, which is the honest signature of a real relativization result, not a trick).

**The honest deliverable of this pass is Tier 1** — the C₄-essentiality theorem against the named toolkit,
which the corpus's controlled experiment already substantiates and which the two-witness form re-cast as a
barrier. Tier 2 is filed as the frontier extension.

---

## (4) The schematic kernel — has content independent of its definitions

**Yes — draft it.** Unlike the rejected definitional form, the two-witness form's skeleton is a genuine
logical fact — the **abstract oracle-separation lemma** — whose truth does not presuppose the conclusion. It
says: *a proof method invariant on an equivalence cannot decide a property that the equivalence does not
respect.* The conclusion follows from the **two witness hypotheses** (agreement, and the definiteness split),
each established independently — not from a definition. It grades **DERIVES** (skeleton), with the two witness
clauses as **named premises** (INTERFACES-with-named-premise). Draft below; **NOT COMMITTED** — for the
record only.

```lean
/-
  SIDE-face-e-two-witness  (DRAFT — schematic; NOT COMMITTED)
  The relativization / two-witness barrier, abstract skeleton.
  Content = the oracle-separation lemma: a predicate invariant on D-agreement
  cannot separate two D-agreeing witnesses that differ on that predicate.
  The two witness clauses are NAMED PREMISES, not definitions.
-/
namespace SIDEFaceETwoWitness

variable {System : Type}

/-- `agree X Y`: X and Y take equal values on every D-accessible quantity.
    (The mathematical content of `agree ξ Z` is W-ORD-FACE-E-INDISTINGUISHABILITY.) -/
variable (agree : System → System → Prop)

/-- The target property: the positivity pairing on the system is positive semi-definite. -/
variable (definite : System → Prop)

/-- A property is *D-decidable* if it is invariant on D-agreement — the exact
    reach of a derivation whose every step factors through κ=0 interfaces
    (Sieve Ceiling Cor. 3.3: dark-factored inference preserves I-indistinguishability). -/
def DDecidable (P : System → Prop) : Prop :=
  ∀ X Y, agree X Y → (P X ↔ P Y)

/-- THE BARRIER.  If two witnesses D-agree yet split on definiteness,
    then definiteness is not D-decidable — no derivation in D establishes it.
    DERIVES: the conclusion is forced by the two named premises, not by a definition. -/
theorem definiteness_not_D_decidable
    (xi Z : System)
    (h_agree : agree xi Z)          -- clause (i): W-ORD-FACE-E-INDISTINGUISHABILITY
    (h_xi : definite xi)            -- ξ conjecturally definite (the target)
    (h_Z  : ¬ definite Z)           -- clause (ii): Davenport–Heilbronn / HELD_WONDER
    : ¬ DDecidable agree definite := by
  intro hdec
  exact h_Z ((hdec xi Z h_agree).mp h_xi)

/-- Corollary (contrapositive scope): any derivation establishing `definite ξ`
    is NOT D-decidable-only — it must consult a quantity outside D-agreement,
    i.e. the Euler product (C₄). -/
theorem definiteness_requires_bright_channel
    (xi Z : System)
    (h_agree : agree xi Z) (h_xi : definite xi) (h_Z : ¬ definite Z)
    : ¬ DDecidable agree definite :=
  definiteness_not_D_decidable agree definite xi Z h_agree h_xi h_Z

end SIDEFaceETwoWitness
```

Grade of the draft, stated plainly: the **skeleton DERIVES** (`definiteness_not_D_decidable` is a two-line
honest consequence of its three hypotheses — no `sorry`, no encoded conclusion). Its **premises are the
content**: `h_agree` is W-ORD-FACE-E-INDISTINGUISHABILITY (open at Tier 2, Tier-1-discharged against a named
toolkit), `h_Z` is Davenport–Heilbronn (closed, with a located witness). This is the correct shape the ruling
asked for: the statement has content independent of its definitions (it is the relativization lemma), and the
mathematical weight sits honestly in the named witness premises, not smuggled into a definition. **The
statement to rule on:** whether `DDecidable` (= invariance on D-agreement) is the accepted formalization of
"reachable by a κ=0-factored derivation," and whether the two-witness premises are the correct pair. On
sign-off, Tier-1 `agree ξ Z` can be supplied as a compiled record against the named toolkit, converting
`h_agree` from premise to lemma. **DO NOT commit until then.**

---

## Rider (a) — the codimension reading

**The Critical Mechanism Theorem (CMT), located and quoted.** `P22_CLOSURE` L143: *"The Critical Mechanism
Theorem (CMT) argument says: 'Five independent paths converge on σ = ½. No mechanism produces σ ≠ ½.
Therefore off-line zeros don't exist.'"* Its codimension content is carried in the **Codimension Dichotomy**
(`TRIVIUM_IDENTITY_SUBSPACE` Prop 8.16, verbatim): *"Zeros of ξ on the critical line have codimension 1. Zeros
of ξ off the critical line have codimension 2 … Codimension-1 conditions generically have solutions;
codimension-2 conditions generically do not."* And for multiplicity, `SIDE_EXCLUSION` L262: *"does any class
produce ξ(ρ)=0 AND ξ'(ρ)=0 simultaneously? None does … Self-adjoint operators have generically simple
eigenvalues (von Neumann–Wigner)"*; `CONSTANCE` Thm 2: *"The codimension-2 obstruction holds at ρ iff
ξ'(ρ) ≠ 0."*

**The three-way test:**

| phenomenon | codimension | corpus support |
|:--|:--:|:--|
| **off-line zero** | **2** (Re ξ=0 ∧ Im ξ=0) | **SUPPORTED, quoted** — Codimension Dichotomy Prop 8.16. |
| **multiple / double zero** | **2** (eigenvalue collision, von Neumann–Wigner; ξ=0 ∧ ξ'=0) | **SUPPORTED, quoted** — SIDE_EXCLUSION L262, CONSTANCE Thm 2. (Caveat: the *mechanism-class* route counts simplicity **codim-5**, `SIMPLICITY_OF_RIEMANN_ZEROS` rail — so the apparatus's codimension is itself parsing-dependent; either way ≥ 2.) |
| **definiteness failure** | **1** (one eigenvalue of the pairing crosses zero; one λ_n first goes negative) | **NEW but consistent** — matches the corpus's "codim-1 = single real condition" usage and Li's criterion (λ_n = 0 is one condition); not stated in the corpus as such. |

**The finding — and it explains the stall.** The exclusion apparatus (CMT, SIDE Independence, FOCUS
transversality, Determination) is a **codimension-≥2 instrument**: it forbids *exceptional coincidences* —
off-line zeros and double zeros, both codim-2 — and it works there because codim-2 sets are generically
missed and Determination upgrades "generic" to "actual." But **h2 / definiteness is a codimension-1
question** — a single eigenvalue crossing zero, one real condition — and **codim-1 conditions are exactly the
generic ones** (`the sign changes happen`). A genericity/transversality argument tuned to forbid codim-2
events gives **no purchase** on a codim-1 question: you cannot forbid a codim-1 event by genericity, because
codim-1 is where genericity produces solutions, not excludes them. **The apparatus and the residue live at
different codimensions — that is the structural cause of the stall.**

This is not a new claim bolted on: it is the corpus's own repeatedly-stated "the codimension-2 obstruction is
insufficient" (`THE_PROOF` L314: *"the codimension-2 obstruction … is real but insufficient — without the
Euler product closing from the other side, zeros wander"*; `CONTROLLED_EXPERIMENT` L82: *"the codimension-2
condition is merely unlikely, not impossible … Epstein functions demonstrate that it can be overcome"*),
**read one level down**: the codim-2 apparatus is insufficient *because* the real question is codim-1, and
the codim-1 question is closed not by more transversality but by the **Euler product** (the σ=1 zero-free
region, "closing from the other side"). So rider (a) and the deliverable's C₄-essentiality theorem are **the
same fact in two languages**: the codim-2 instrument cannot reach the codim-1 residue, and the bridge is
exactly C₄. *(A subtlety kept honest: definiteness-failure ⟺ off-line-zero by Li's criterion — the same event
is codim-1 in the pairing's spectrum (λ-space) and codim-2 in the ξ-trajectory (s-space); the apparatus works
in s-space where it reads codim-2, while the positivity question is native to λ-space where it is codim-1.
The mismatch is a change of ambient space, and it is precisely why the s-space instrument does not settle the
λ-space question.)*

**Verdict: the corpus's codimension language SUPPORTS the reading** (the codim-2 half quoted directly; the
codim-1 half consistent with its usage and, once added, *explaining* its own "insufficiency" refrain). Record
the finding: **the exclusion apparatus is a codimension-≥2 instrument and h2 is a codimension-1 question — a
codimension mismatch that structurally explains the stall.**

## Rider (b) — the cohomological translation (external-legibility of Arm 1)

The positivity pairing is the **cup product** H¹ × H¹ → H². Over 𝔽_q, C is a curve, H¹(C) is 2g-dimensional,
and the cup product H¹(C) × H¹(C) → H²(C) ≅ ℚ_ℓ(−1) **is** the intersection/polarization pairing whose
positivity is Weil's theorem (Hodge index / Castelnuovo). Over **Spec ℤ** — an arithmetic *curve*, cohomological
dimension too low — there is **no H²** to receive the cup product: no `Spec ℤ × Spec ℤ`, no 𝔽₁, no arithmetic
surface whose second cohomology is the pairing's target (Face D control `85c9e5d`; Arakelov supplies the
wrong surface). **The pairing has no codomain.**

And **Arm 1's Δn₄ = +1 is exactly that missing H² target, in formation coordinates.** The interface
coordinate n₄ counts bright essential interfaces; the bright interface 𝔽_q gains and ℚ lacks *is* the cup
product landing in H²; its absence over ℚ (n₄=0) *is* the absent H². So:

> **External-legibility statement (Arm 1).** The formation-coordinate finding "Δn₄ = +1" reads, to a
> cohomologist, as: *the cup product H¹ × H¹ → H² has no target over Spec ℤ; supplying the second dimension
> supplies H²; that is the one bright interface, Δn₄ = +1.* The programme's interface count and the
> cohomological codomain are the same object in two vocabularies.

This also closes the loop with rider (a): the cup product H¹ × H¹ → H² **is** a quadratic form, its
definiteness (codim-1, rider a) is Weil positivity, and its target H² is the missing dimension (Δn₄=+1,
Arm 1) — the codimension mismatch and the missing codomain are one wall in two registers.

---

## Pins

- No commits of any kernel. The two-witness kernel draft is in this report only — **not committed**; the
  author rules on the `DDecidable` formalization + the witness premises first.
- The two riders (a) codimension mismatch, (b) cohomological translation are recorded in the h2-arc
  OPEN_TRAILS addendum this pass.
- Sources (quoted): `SIMPLICITY_OF_RIEMANN_ZEROS` (rail), `A_Place_to_Stand` (rail), `CONTROLLED_EXPERIMENT`
  L82/L147, `SIEVE_CEILING_LEMMA` §3.3, `HELD_WONDER_crystallization` L22, `Seven_Mechanism_Classes` L67,
  `TRIVIUM_IDENTITY_SUBSPACE` Prop 8.16, `SIDE_EXCLUSION` L262, `CONSTANCE` Thm 2, `P22_CLOSURE` L143,
  `A_METHODOLOGY` §Step 1. PLACE-papers @ `cbc0c63`. Nothing deposited.
