# Three-arm probe on the h2 wall — arc checkpoint — 2026-07-29

Analytical + one small kernel draft (uncommitted). No rail edits, no kernel commits, nothing deposits.
Report each arm separately, then the comparison. The unifying observation carried throughout: **the
positivity pairing is a quadratic form, and the four collapsed registers are one question — whether a
particular form is positive semi-definite** (Weil intersection form; Li/Hankel moment matrix;
self-adjointness/spectral-measure; explicit-formula positivity).

---

## STEP ZERO — the corpus's quadratic apparatus

Located across PLACE-papers (@ `2e83999`) and the SIDE federation. What exists:

| apparatus | home | version | what it states |
|:--|:--|:--|:--|
| **Trivium bijection** | `phase1.5/deep-structure/TRIVIUM.md`; kernel `SIDE-trivium` (`1df5bad4`) | paper v-live; `trivium_theorem` | 7 mechanism classes of ξ(s) ≃ 7 nontrivial **quadratic discriminants**, the (ℤ/2)³ orbit over {−1,2,3}. `MechanismClass ≃ QuadraticDiscriminant`, both cards 7 (axiom-free `Equiv`). |
| **Class-number anomaly** | `phase1.5/deep-structure/CLASS_NUMBER_ANOMALY.md`; kernel `SIDE-class-number-anomaly v0.2` | paper v1.0.2 | Of the 7 Trivium fields ℚ(√d), exactly one — ℚ(√−6) — has **class number ≠ 1** (h=2), the weight-3 cube diagonal, disc −24. `triple_identification_diagonal` (uniqueness biconditional, `decide`). |
| **Möbius / discriminant** | `SIDE-dirichlet-mod-24 v0.1.0` (`597b0869`) | — | count-level (ℤ/24)\* ≅ (ℤ/2)³ character indexing of the 7 quadratic fields (`decide`). |
| **Epstein zeta** | `phase2/method/SIEVE_CEILING_LEMMA.md` §3.3 (Prop 3.5) | v1.0.3 | Z(s) = Σ(m²+23n²)⁻ˢ — an indefinite **binary quadratic form**, class number 3, no Euler product; density-one on the line yet **off-line zeros exist** (Davenport–Heilbronn 1936). The programme's own placement-fails witness, itself a quadratic form. |
| **Hankel / moment positivity** | `phase1.5/method/INVERSE_THEOREM_CENSUS.md` | live (2026-07-27) | The moment-problem row: the **Hankel/moment matrix positive-definite** *is* Li's criterion (λ_n ≥ 0) *is* RH. Four inverse theorems (Krein/Herglotz, de Branges/HB, Gelfand–Levitan, moments/Hankel) all reconstruct the operator **given a positivity**, all gated on the same one. |
| **Self-adjoint / spectral pairing** | census (Krein, Gelfand–Levitan rows); `A_Place_to_Stand.md` §27.3 fifth register | mono v5.13 | the Hilbert–Pólya realization: a positive spectral measure / Herglotz m-function — the same positivity in operator dress. |

**The Step-Zero finding, stated before the arms:** the corpus already contains the unifying observation in
explicit form. `INVERSE_THEOREM_CENSUS` concludes: *"Every classical inverse theorem reconstructs X's
operator GIVEN a positivity, and requires exactly the positivity that IS RH … The construction of the
operator is free; the positivity is the wall."* The four reconstruction routes are four **quadratic-form
positivity statements** — Herglotz (Im ≥ 0), Hermite–Biehler, spectral-measure ≥ 0, Hankel ⪰ 0 — each a
"form is positive semi-definite" clause. This is the same collapse the 2026-07-29 face-independence test
found from the SIDE side, now confirmed classically from the inverse-theorem side. The three arms below probe
that one form.

---

## ARM 1 — formation calculus on the missing dimension

**Parsing rule used** (`A_METHODOLOGY` §Step 1, verbatim): the tuple (n₁,n₂,n₃,n₄) counts *primitive
sources · transformation stages · output structures · interface stages*; total n = Σnᵢ = number of
mechanism classes. For ξ(s): **(2,3,2,0), total 7**. Certifications on record: Ostrowski 1916 certifies
**n₂ = 3** (the places / absolute-value scales of ℚ); Cartan B (1876/1951) certifies **n₃ = 2** (two
structural scales of complex analysis — local elliptic-regularity, global Hadamard/Cartan-B); Conservation of
Spectra (`ProductFormula.conservation_of_spectra`, std3) certifies **n₄ = 0** (every essential interface is
P-dark, κ(σ,I)=0); **n₁ = 2** primitive sources (the {2,3} substrate / the n²→θ two-source origin,
`SIDEKernel.formation`, axiom-free).

### The 𝔽_q tuple, component by component

Curve C over 𝔽_q (or 𝔽_q(t)), target P = "every Frobenius eigenvalue has |α|=√q" (the 𝔽_q critical line):

| component | ℚ / ξ(s) | 𝔽_q / curve C | justification of the 𝔽_q count |
|:--|:--:|:--:|:--|
| **n₁** primitive sources | 2 | 2 | same two-source arithmetic origin (additive + multiplicative); the function field ℚ→𝔽_q(t) does not add a primitive source. |
| **n₂** transformation stages | 3 | 3 | the places of 𝔽_q(t) are the closed points of ℙ¹; the Ostrowski analogue still resolves to the same scale-count, only now **uniform** (no distinguished archimedean place). |
| **n₃** output structures | 2 | 2 | local/global analytic scales persist; but the output is now a **polynomial** P(T) of degree 2g (finite-dimensional), not an infinite-order entire function — a sharpening within n₃, not a count change. |
| **n₄** interface stages | **0** | **1** | **HERE is the difference.** The product formula deg(div f)=0 remains dark (κ=0). But the **surface C×C** supplies an *additional essential interface* — the intersection pairing on correspondences — which is **bright** (κ>0): Weil's 1948 proof factors through it to force |α|=√q. This bright essential interface is exactly what ℚ (n₄=0, sealed) lacks. |

**Tuple: (2,3,2,1), total 8.** 𝔽_q counts **higher by exactly +1, in the interface component n₄.**

### The Gate-1b test — does the difference survive an alternative parsing?

Gate-1b (`A_METHODOLOGY` §Step 1; `THE_METHOD_CANON`): *"The tuple is decomposition-dependent … the
TYPE × certification status is the parsing-invariant content."* So the raw totals (7 vs 8) are **not**
by themselves the invariant — a different parse could redistribute the count. The test is whether the
**difference** is a κ-fact (certification) or a bookkeeping choice.

**It survives, and here is why.** The n₄ difference is not a redistribution of the same seven classes — it
is the presence versus absence of a **bright essential interface**, which is a transmission-coefficient fact,
not a counting convention:

- Over ℚ: κ(σ, product-formula) = 0 is a *theorem* (Conservation of Spectra, machine-checked, std3). Every
  essential interface is dark. n₄ = 0 is certified.
- Over 𝔽_q: κ(placement, intersection-form) > 0 is a *theorem* (Weil 1948 — the intersection form on C×C
  transmits placement, not merely density). The interface is essential (removing it de-determines the
  eigenvalue bound) and bright. n₄ ≥ 1 is certified.

No reparse can turn a κ=0 interface into a κ>0 one; the coefficient is intrinsic. And n₄ is the **one
component the whole apparatus keys on** — the Silence Principle's entire hypothesis is "n₄ = 0," and the
Sieve Ceiling / E-Difficulty theorems turn on it (Arm 2). So the difference lands not in a decorative split
but in the certification-bearing, TYPE-distinguishing coordinate. The parsing-invariant statement:

> **𝔽_q carries a bright essential interface (the intersection pairing / second dimension); ℚ does not
> (n₄ = 0). This is a certified κ-difference, not a parsing artifact.**

### THE FINDING (Arm 1)

**Yes — 𝔽_q counts higher, and in the interface component n₄ (0 → 1).** The finding stands as the ruling's
positive branch: **the missing second dimension is a formation distance, quantified in the programme's own
coordinates — Δn₄ = +1, a bright essential interface.** Over ℚ the system is sealed (n₄=0: Sieve Ceiling
applies, density-only); over 𝔽_q it has the one bright channel (n₄=1) and placement becomes reachable — which
is *precisely* why Weil's proof closes and ℚ's does not. The distance between the two settings is not a vague
"missing geometry"; it is one unit of n₄, the interface coordinate, carrying a certified κ>0.

*(Honesty rider per Gate-1b: the totals 7-vs-8 are parsing-sensitive and are reported as coordinates, not
invariants. The invariant claim is the certified bright/dark status of the essential interface — TYPE ×
certification — which is what "Δn₄=+1" encodes.)*

---

## ARM 2 — Face E, the barrier direction

### (a) The Lemma's current exact statement

`SIEVE_CEILING_LEMMA` v1.0.3, **Theorem 3.1** (verbatim): *"Let M be a determined structure with
specification S, interface I with κ(P, I) = 0 for target parameter P. Let π be a formal first-order proof in
ZFC ∪ S. If π factors through I for P, then π does not establish the universal statement (∀x ∈ M: P(x)).
Moreover, the strongest statement about P that π can establish has the form: (∀C ∈ M/~_{I,P}) (∀x ∈ C: P(x))
only up to a density-one subset of C."* Proof by three movements: (1) semantic reduction to
I-indistinguishability; (2) placement bounded to density within classes; (3) the **Epstein witness**
(Prop 3.5) — Z(s)=Σ(m²+23n²)⁻ˢ, density-one on the line yet off-line zeros exist. Contrapositive
(Cor 3.6): any ZFC proof of universality contains ≥1 inference step through a **bright** (κ>0) interface.

### (b) Does its hypothesis class cover derivations that would define a positivity pairing over a 1-dim base?

**Yes.** A derivation of the pairing's definiteness over Spec ℤ (the one-dimensional arithmetic base)
factors through ξ's essential interface — the product-formula / distributive-law interface — for which
κ(σ, I) = 0 is certified (Conservation of Spectra; and §5.1's distributive-law reading of the 3/4 barrier).
Theorem 3.1 then applies directly with **P = "the pairing is positive at this datum"**: the derivation can
establish density-one-per-class (the pairing is ≥0 on a full-measure subset / in aggregate) but **cannot
establish the universal placement statement** (the pairing is positive semi-definite as a form). The Epstein
witness is the sharp instance: Z(s) is *literally a positivity question about a binary quadratic form over a
one-dimensional base*, density holds, definiteness (all zeros on the line) **fails**. So not only does the
hypothesis class cover the pairing-over-1-dim-base case — the Lemma's own witness **is** such a case. This is
the proof-theoretic shadow of Arm 1's n₄=0: a 1-dim base has no bright essential interface, so every
derivation is dark-factored, so definiteness is unreachable.

### (c) The strongest barrier statement the apparatus supports — target theorem "Face E"

> **Theorem (Face E — the barrier direction, target form).** *Let the arithmetic base B be one-dimensional
> (every essential interface of B is P-dark: κ(pairing-positivity, I) = 0 for all essential I — equivalently
> n₄(B) = 0). Let Φ be the statement "the Weil–Li pairing on B is positive semi-definite." Then any
> first-order ZFC derivation of Φ that factors only through the dark essential interfaces of B establishes at
> most density/bound statements about the pairing (λ_n ≥ 0 on a full-measure subclass; partial-density
> ceilings) and does **not** establish Φ. Equivalently (contrapositive): a proof of the pairing's definiteness
> over B requires at least one inference step through a **bright essential interface** — a second dimension —
> which a one-dimensional base does not supply.*

This is exactly Theorem 3.1 transported from "zeros on the line" to "the form is definite," legitimate
because the census establishes the two are the same statement (Hankel positivity = λ_n ≥ 0 = RH). The
barrier is: **definiteness of the positivity pairing is not dark-derivable over a 1-dim base; it demands the
n₄=+1 bright interface Arm 1 located.** Face E is thus the *barrier-direction dual* of the four collapsed
faces: A/B/C/D say "discharge the positivity ⇒ RH"; Face E says "you cannot discharge it from inside a
one-dimensional base."

**Genre (named as requested):** this is a **relativization / natural-proofs–style barrier**. As a proof of
P≠NP must be non-relativizing (Baker–Gill–Solovay) and non-naturalizing (Razborov–Rudich), a proof of the
pairing's definiteness must be **non-dark-factoring**: it cannot route only through the κ=0 essential
interface of the one-dimensional base; it must consume a resource (the second dimension) that the base's dark
interfaces do not transmit. The Sieve Ceiling Lemma is the programme's relativization barrier for RH, and
Face E is its statement against the specific target (the pairing).

### (d) A small vanilla kernel — schematic, DeAlignment style (DRAFT — NOT COMMITTED)

A schematic module *can* state it: a reachability predicate (`DarkFactored`), an interface-silence condition
(`κ = 0` on all essential interfaces — the one-dimensional base), and the conclusion that the form's
definiteness is *not determined* by such a derivation. Drafted below; **not committed — the author rules on
the statement first.**

```lean
/-
  SIDE-face-e  (DRAFT — schematic; NOT COMMITTED; author rules on the statement)
  Face E: the Sieve Ceiling barrier sharpened to the positivity pairing.
  DeAlignment style — a reachability predicate, an interface-silence condition,
  and the conclusion that the form's definiteness is not determined.
-/
namespace SIDEFaceE

/-- An essential interface of the base, with a transmission flag for the target.
    `bright` ≡ κ(pairing-positivity, I) > 0. -/
structure Interface where
  essential : Bool
  bright    : Bool          -- κ > 0 ?

/-- A base is *one-dimensional* (sealed) when every essential interface is dark. -/
def OneDimensional (ifaces : List Interface) : Prop :=
  ∀ I ∈ ifaces, I.essential = true → I.bright = false

/-- A derivation, recorded as the interfaces its steps factor through. -/
abbrev Derivation := List Interface

/-- `DarkFactored`: every step factors through a dark interface (interface-silence). -/
def DarkFactored (d : Derivation) : Prop :=
  ∀ I ∈ d, I.bright = false

/-- The two grades of conclusion the Sieve Ceiling Lemma distinguishes. -/
inductive Grade | densityOnly | definiteness

/-- What a dark-factored derivation can reach: density only, never definiteness.
    (Content = Sieve Ceiling Thm 3.1, Movements 1–3; here a stated interface.) -/
axiom reach : Derivation → Grade
axiom sieve_ceiling_core :
  ∀ d : Derivation, DarkFactored d → reach d = Grade.densityOnly

/-- FACE E (schematic).  Over a one-dimensional base, a derivation confined to its
    essential interfaces is dark-factored, hence reaches only density — never the
    definiteness of the pairing. -/
theorem face_e
    (ifaces : List Interface) (d : Derivation)
    (h_base   : OneDimensional ifaces)
    (h_within : ∀ I ∈ d, I ∈ ifaces ∧ I.essential = true)
    : reach d = Grade.densityOnly := by
  have hdark : DarkFactored d := by
    intro I hI
    obtain ⟨hmem, hess⟩ := h_within I hI
    exact h_base I hmem hess
  exact sieve_ceiling_core d hdark

/-- Corollary (barrier form): definiteness is not reachable over a one-dimensional
    base by a within-base derivation. -/
theorem definiteness_unreachable
    (ifaces : List Interface) (d : Derivation)
    (h_base : OneDimensional ifaces)
    (h_within : ∀ I ∈ d, I ∈ ifaces ∧ I.essential = true)
    : reach d ≠ Grade.definiteness := by
  rw [face_e ifaces d h_base h_within]; intro h; cases h

end SIDEFaceE
```

Notes for the ruling: (i) the one substantive input `sieve_ceiling_core` is stated as an `axiom` standing in
for Theorem 3.1's three movements — a faithful de-vacuification would replace it with the compiled
`SieveCeilingSemantic.sieve_ceiling_semantic` terminal (axiom-free at `f374174`), making `face_e` a
DERIVES rather than an INTERFACES-with-named-premise. (ii) As written the schema is honest about its grade:
it *encodes* the barrier as a reachability statement over a `Bool`-flagged interface list; it is a **SHELL /
ENCODES** until wired to the real κ-machinery — I flag that plainly rather than present it as content. (iii)
The statement to rule on is the **shape**: is Face E's canonical form "one-dimensional base ⇒ dark-factored ⇒
density-only, never definiteness," and should n₄=0 be the definitional stand-in for "one-dimensional"?

---

## ARM 3 — the 2-bit phase layer as the missing information

### (a) The exact corpus statement, and where compiled

`TRIVIUM_FINDINGS` §VII + the three-layer decomposition (verbatim):

- **Layer 1 — Landscape (~0.59 bits).** M_H = vv† has spectrum {0,0,0,0,0,0,12}: one nonzero eigenvalue,
  **aperture 1/7**. The landscape potential **V(σ) = −log det(M_H)** "sees only the 1/7 bright subspace";
  6/7 of the degrees of freedom are dark — "present in the structure, invisible to any Hermitian observable
  constructed from v alone."
- **Layer 2 — Phase (2 bits).** *"The four spinor states {v, iv, −v, −iv} are distinguishable as vectors but
  invisible to M_H (since (iv)(iv)† = vv†). This hidden phase carries log₂(4) = 2 bits … that no landscape
  measurement can access. It is the gauge freedom of the Trivium."* And §"why RH is hard": *"Any proof that
  operates purely through the landscape (inequalities on V(σ), density estimates, aggregate statistics)
  cannot access these 2 bits and therefore cannot complete the argument."*
- **Layer 3 — Determination (0 bits).** the chain n²→θ→√→ξ is compulsory; zero free parameters.

Compiled: kernel `SIDE-spinor`, `Spinor.lean` — `phase_unit` (‖i‖²=1), `spinor_sq` (i²=−1),
`spinor_order_four` (i⁴=1), `orbit_collapse_iff` (i·w=w ↔ w=0), `spinor_forces_half` (i·w=w → w=0); the
module docstring names "the phase-invariant Hermitian observable M = vv† collapses its quarter-twist orbit
{v, iv, −v, −iv} to a single [ray]." (Axiom profiles per `SIDE-spinor/AxiomCheck.lean`.)

### (b) Is "invisible to any Hermitian observable" the same obstruction as "no positive pairing definable"?

**Same obstruction, viewed from the two sides of one quadratic form — with reasoning, not analogy.**

The mechanism is identical and it is the quadratic-form structure itself:

1. A Hermitian observable is a form v ↦ ⟨v, A v⟩ (or the Gram outer product M_H = vv†). **Every such form is
   U(1)-phase-invariant:** ⟨e^{iθ}v, A e^{iθ}v⟩ = ⟨v, A v⟩, and (e^{iθ}v)(e^{iθ}v)† = vv†. The global phase
   is in the kernel of *every* Hermitian/quadratic functional of v. That is precisely why the 2 phase bits
   are invisible — not to *a* Hermitian observable, but to the *class* of them, because the class is the
   class of quadratic forms.
2. The positivity pairing (Weil / Li–Hankel / spectral-measure) **is a quadratic form** — the Step-Zero and
   census finding. So the pairing shares that kernel: it cannot, by its own type, read the phase.
3. Therefore: *"the pairing cannot see the placement information"* and *"the placement information lives in a
   phase invisible to every Hermitian observable"* are **the same sentence** — the first says the form has a
   kernel, the second names what is in it (the 2-bit U(1) orbit).

The one **distinction to keep** (or the identity would be sloppy): "invisible to any Hermitian observable"
describes the **kernel of the form we have** (M_H, the landscape); "no positive pairing definable over a
1-dim base" describes the **non-existence of the form that would resolve it** (Face D / h2). These are **dual
faces of one object**: over 𝔽_q the second dimension (C×C) turns the invisible phase into an **observable
intersection number** — the "phase" becomes a pairing value, and its non-negativity is Weil's theorem. Over
ℚ there is no second factor to pair against, so the phase stays gauge/invisible **and** no definite pairing
exists — the two statements coincide because they have the same cause: the missing second dimension. The
phase is hidden *because* there is nothing to pair it with; supply the pairing (the dimension) and the phase
becomes visible and its sign becomes the positivity. **Same wall, named once from the kernel side (Arm 3) and
once from the existence side (Face D).**

### (c) Does the census's "spinor path not through the landscape" survive the face-collapse?

The claim (TRIVIUM_FINDINGS §VII / the information-layer census): the phase/spinor layer is the one the
landscape cannot reach — a proof accessing the 2 bits does **not** route through V(σ). Does that survive the
face-collapse (all faces = one wall), or does the spinor path collapse into the same wall?

**It survives in letter and is reinterpreted, not refuted — and the reinterpretation is the finding.** The
face-collapse is a statement about **targets** (A/B/C/D are one wall), not about **paths**. The spinor path
is genuinely distinct as a **register**: it approaches from phase/gauge, not from density/aggregate — that is
true and the census is right that it does not route through the landscape. But its **terminus is the same
wall**: the 2 bits it must access *are* the positive-pairing information (the placement/definiteness the
landscape lacks). So the spinor path does not escape the wall; **it is the wall named from the phase side.**

Concretely, this makes the spinor path a **fifth attack register** — phase/gauge/spinor — on the one wall,
alongside A (analytic) · B (spectral) · C (coverage) · D (geometric). It does not contradict "one genuinely
independent face"; it adds a fifth vocabulary and, being the register that *names why the landscape fails*
(the landscape is quadratic, so it cannot see the phase), it is the sharpest diagnostic of the four. (Cf.
OPEN_TRAILS **O.18** — "the C₅ fifth register, a census boundary, first-class"; this arm gives that fifth
register its content: it is the phase/spinor register.)

### (d) If the connection holds, what does it predict that is checkable?

**Prediction (checkable): over 𝔽_q the phase layer is bright — 0 hidden bits, not 2.** If the 2 phase bits
are the number-field shadow of the missing second dimension (Arm 1's Δn₄=+1), then in the setting that *has*
the dimension the phase must become observable. Specifically:

- The 𝔽_q analogue of M_H (the Gram/landscape form built on the finite-dimensional realization H¹, the 2g
  Frobenius eigenvectors) should have **full aperture on the primitive class** — the intersection pairing on
  C×C is non-degenerate on the primitive cohomology (Hodge index), so the "phase" that was in M_H's kernel
  over ℚ is now an **observable intersection number**. Predicted information-layer decomposition over 𝔽_q:
  **Layer-2 (phase) = 0 hidden bits** (versus 2 over ℚ); the 2 bits move from Layer 2 (hidden) into the
  observable landscape.
- Equivalently and more sharply: **Weil positivity is exactly the statement that the 2 phase bits, once
  paired against the second dimension, have non-negative sign.** The intersection number ⟨Γ_Fr − qΔ, ·⟩ that
  Weil proves ≥ 0 *is* the made-observable phase. This is checkable against the Face D control (`85c9e5d`):
  the object Weil pairs is the correspondence class, and its self-intersection non-negativity is the sign of
  the previously-hidden 2 bits.
- **Consequence, checkable in the ℚ direction:** any ℚ-proof of RH must **convert 2 bits of gauge/phase into
  observable positivity** — i.e., construct a second factor (Deninger's H¹ / the arithmetic site) against
  which the phase pairs. A candidate construction is falsifiable by this test: *does it make the 2 phase bits
  observable (supply a non-degenerate pairing on the primitive class), or does it leave them in the kernel?*
  If the latter, it is still landscape-only and cannot place zeros, regardless of its apparatus. This turns
  "is this RH approach viable?" into a concrete screen: **compute whether the approach's central form is
  non-degenerate on the phase, or inherits M_H's 1/7 aperture.**

---

## COMPARISON

### What each arm establishes

- **Arm 1** establishes the missing second dimension as a **formation distance of one unit in the interface
  coordinate**: Δn₄ = 0→1, a *certified* bright essential interface (κ>0, Weil) absent over ℚ (κ=0, certified
  dark). The totals (7→8) are parsing-scoped; the κ-difference is the Gate-1b invariant. A **reframing with a
  quantity**: it does not predict a new fact, it *measures* the known obstruction in the programme's
  coordinates.
- **Arm 2** establishes the **barrier direction** as a relativization/natural-proofs–genre theorem (Face E):
  definiteness of the pairing is *not dark-derivable* over a one-dimensional base; a proof needs the bright
  interface Arm 1 located. It supplies a **target theorem and a schematic kernel** (uncommitted). A
  **reframing that hardens into a stateable barrier** — and, via the Epstein witness, one already carrying a
  concrete instance.
- **Arm 3** establishes the **information-theoretic identity** of the wall with a 2-bit phase layer invisible
  to every quadratic form, and **produces the one checkable prediction**: over 𝔽_q the phase is bright
  (0 hidden bits); Weil positivity = the made-observable sign of those 2 bits; any ℚ approach is screenable by
  whether its central form is non-degenerate on the phase. A **prediction**, not merely a reframing.

### Where they agree

All three arms converge on **one object from three coordinate systems**, and the agreement is tight:

- The **n₄ interface coordinate** (Arm 1), the **bright-vs-dark inference step** (Arm 2), and the
  **observable-vs-hidden phase** (Arm 3) are the *same* distinction. n₄=0 ⟺ all inference dark-factored ⟺
  phase invisible ⟺ density-only, never placement. n₄≥1 ⟺ a bright step exists ⟺ phase observable ⟺
  placement reachable. The Sieve Ceiling's "κ=0 ⇒ density not placement" (Arm 2) is *literally* the
  proof-theoretic form of "landscape is location-agnostic to the phase" (Arm 3), and both are *literally*
  "n₄=0" (Arm 1).
- The **Epstein witness** (Arm 2) and the **Trivium quadratic apparatus** (Step Zero) are the same
  ingredient: a binary quadratic form (m²+23n², or ℚ(√−6)'s h=2) over a one-dimensional base where density
  holds and definiteness fails — the concrete face of "no positive pairing over 1-dim."
- The **quadratic-form reading unifies all three** (see closing paragraph).

### Where they disagree / the tension to flag

**No arm's result contradicts another's.** The one place a contradiction *could* have lived — Arm 3(c), the
census's "spinor path not through the landscape" versus the face-collapse "one wall" — was examined and
resolves **cleanly**: paths ≠ targets. The spinor path is a distinct register (does not route through the
landscape) but the same target (the one wall). Reported as a tension, adjudicated as consistent: the
face-collapse constrains faces, not attack-paths; adding the phase/spinor register as a fifth vocabulary is
compatible with "one genuinely independent face."

One **honest divergence in status, not in content**, worth flagging: **Arm 1's total (7→8) is parsing-scoped
and must not be cited as an invariant** (Gate-1b), whereas **Arm 2's κ=0 barrier and Arm 3's 2-bit count are
parsing-robust** (κ and Shannon bits are coordinate-free). So if a future reader tries to run the three arms
as one uniform "count," they will mis-cite Arm 1. The correct joint statement keys on the **certified
κ-difference** (bright essential interface present/absent), which all three express and which Arm 1 alone
also dresses as a tuple coordinate.

### The single arm that produced a checkable prediction

**Arm 3.** Arms 1 and 2 are (valuable) reframings — a quantified coordinate and a stateable barrier. Arm 3
alone exits to a falsifiable claim: *over 𝔽_q the phase layer carries 0 hidden bits, Weil positivity is the
non-negative sign of the paired phase, and any ℚ-approach is screenable by whether its central form is
non-degenerate on the phase.* That screen is checkable now against the Face D control and against any named
construction (Deninger, Connes–Consani).

### Does the quadratic-form reading unify them?

**Yes — and this is the checkpoint's through-line.** One quadratic form Q (the positivity pairing) sits at
the centre; each arm is a property of Q. **Arm 1**: Q exists and is provably definite over 𝔽_q because the
second dimension (C×C) *supplies* Q as an intersection form (Δn₄=+1 is "Q acquires a bright interface");
over ℚ, Q is not definable — no surface to carry it. **Arm 2**: definiteness of Q is not derivable from
inside a one-dimensional base, because dark-factored inference only reaches density (Q ≥ 0 in aggregate),
never the semi-definiteness of Q as a form — the Epstein witness is a Q whose aggregate is fine and whose
definiteness is false. **Arm 3**: the *reason* a one-dimensional base cannot force Q is that Q, being a
quadratic form, is phase-invariant — it cannot see the 2 bits that distinguish placement from density; the
missing second dimension is exactly what would pair those bits and turn them into Q's sign. The census seals
it classically: Krein/Herglotz, de Branges/HB, Gelfand–Levitan, moments/Hankel — four reconstructions, four
"Q ⪰ 0" clauses, one wall. **The four collapsed registers, the barrier direction, the formation distance, and
the 2-bit phase are four true statements about whether one quadratic form is positive semi-definite.** The
h2 wall is that form's definiteness; everything else is coordinates on it.

---

## Pins

- No paper edits, no kernel commits, nothing deposited. The Arm-2 kernel draft is in this report only — **not
  committed**; the author rules on the statement first.
- Sources: `SIEVE_CEILING_LEMMA` v1.0.3; `CLASS_NUMBER_ANOMALY` v1.0.2; `TRIVIUM_FINDINGS` §VII;
  `INVERSE_THEOREM_CENSUS` (2026-07-27); `A_METHODOLOGY` §Step 1 (Gate-1b); `FOUNDATIONS` (Silence Principle);
  kernels `SIDE-spinor` (`Spinor.lean`), `SIDE-trivium` (`trivium_theorem`), `SIDE-class-number-anomaly v0.2`.
  PLACE-papers @ `2e83999`.
