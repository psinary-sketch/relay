# THE SURVEY'S LAST SENTENCE + THE BUILD'S FIRST OBJECT — 2026-08-10

**Rail `de621b1` / `2147a03` unmoved. Nothing deposits.**
**Vocabulary law applied: the prior "declared gap" line is re-recorded throughout as
DECLARED OMISSION; the banned term does not import.**

---

## §1 — BORGER'S SENTENCE, COMPLETED

One bounded fetch, `arXiv:0906.3146`, re-extracted (1182 lines, byte-identical line count to the
prior extraction). The clause I flagged as **the single most relevant unread sentence in the
survey**, read whole:

> *"As a check to see if this could lead to a proof of the Riemann hypothesis for ℤ, one might
> examine the translation of Weil's proof of the Riemann hypothesis for `S` from algebraic
> geometry over `k` to that over `𝔽₁^S`. **But since the current version of our theory says
> nothing about the archimedean place of ℚ, it is hard to imagine this succeeding without
> further ideas. Even so, it should be done.**"*

### THE ANSWER: IT NAMES NOTHING.

**No seventh constraint. No constraint already held. Nothing at all.** *"Further ideas"* is a
deferral, not a specification.

> **The six constraints stand unchanged, and the convergence note gains no sharpest line from
> this sentence — because there was no content in it to gain.** The most relevant unread
> sentence in the survey, read, is an admission of not knowing. **Recorded as the result.**

### TWO CORRECTIONS TO MY OWN PRIOR FRAMING

1. **THE ARREST IS SOFTER IN KIND THAN I FILED IT.** I wrote *"Borger arrests at the archimedean
   place."* Correct as to **where**, overstated as to **kind**. He claims no failure and proves
   no obstruction; he says he cannot imagine success without further ideas — **and then says
   "Even so, it should be done."** **A self-declared un-attempted check with a recommendation to
   attempt it, not a demonstrated barrier.** The roster row is corrected.
2. **THE ARREST IS STATED ABOUT THE FUNCTION-FIELD ANALOGUE.** The sentence sits in his §7
   preview, where the base is a function field and `𝔽₁^S` is the variant; the Weil translation
   there is proposed as *"a check to see if this could lead to"* the ℤ case. **A proxy test, one
   remove from the object.** My prior report did not state this.

### DUROV — CLOSED AS **DECLARED-UNFETCHED**

`arXiv:0704.2030` not fetched. **Requirements entry stationary across two consecutive probes**
(surface-survey close and trio check state the one absence identically) — the shiny-object guard
fires and the item closes. **One line; no synonym-hunting; no substitute source consulted.**

---

## §2 — THE ENRICH-DON'T-STRIP LEARNING (filed `F.2026-08-10`, at cite both ways)

**STRIPPED** → weaker structure → `F_A ⊗_{𝔽₁} ℤ = ℤ[A]`, `ℤ = ℤ[trivial monoid]` → **trivial
descent** → square collapses → and the door shuts at cancellativity (idempotent completion is
trivial). Cause, one line, **categorical not arithmetic**: *"since ℤ is the initial object in the
category of rings."*

**ENRICHED** → Λ-rings are *"an enrichment of the theory of commutative rings"* → **door passed,
the only roster member to reach it** → arrest at *"nothing about the archimedean place."*

> **STRIPPING buys a deeper base and loses the signs. ENRICHING keeps the signs and loses the
> place at infinity. Each school holds what the other lacks; neither holds both.**

**And Borger states the division himself**, describing the stripped school: *"set-theoretically
weaker than a commutative ring, for example a commutative monoid … one could **even aspire to see
the place at infinity by incorporating archimedean information in these structures**."*

### THE QUALIFICATION — LOAD-BEARING; THE LEARNING DOES NOT FILE CLEAN

**Enrichment did not escape the toric terminus.** Deitmar's monoids land on toric varieties;
Borger *"hope[s] to show that **all examples of finite type come from toric varieties**"*, and his
Theorem 0.2 gives every finite-type 𝔽₁-scheme a cyclotomic point and, when proper, a Λ-morphism
`Spec ℤ → X`. **Two opposite moves reach the same objects at finite type.** Filed **with** the
learning, not after it.

### THE CARRIER CONSEQUENCE, printed with it

> **ARCHIMEDEAN-INCLUSIVE FROM THE GROUND UP — the ℝ-at-∞ component is a founding coordinate,
> not an import to defer.**

Three supports at cite: the divisor-group fusion (`aⱼ ∈ ℤ`, `a_∞ ∈ ℝ`, one divisor) · Borger's
arrest · Connes' arrest on the opposite side.

**The two-channel division coordinate** is filed beside it **at OBSERVATION grade** — a statement
about where programmes stop, **not** a claim that combining them is possible, available, or
attempted. Filed at that grade deliberately, because the shape invites an upgrade that is not
earned.

---

## §3 — `W-ORD-CARRIER-SPEC`: `SIDE-carrier-spec` v0.1.0 = `20f1860`

Fresh federation kernel. **Lean 4.29.1, Mathlib `5e932f9`, vanilla Lean, `theorem` never
`lemma`, 0 sorry, 0 native_decide. Built clean on the first attempt, 769 jobs.**

**IT GRADES CANDIDATES. IT DOES NOT CONSTRUCT ONE. It attempts nothing on the clause.**

| field | requirement | source at cite |
|:--|:--|:--|
| `cancel` | cancellativity is the door predicate | `arXiv:1502.05580` Lemma 2.3 (*"simplifiable"*) |
| `neg`, `add_neg` | signed classes | the symmetrization requirement |
| `finPart`, `archPart`, `arch_present` | ℤ finite / **ℝ at ∞, fused and non-deferrable** | `arXiv:2205.01391` |
| `act : E → (C →+ C)` | **endomorphisms, not translations** | `arXiv:2602.15941` |
| `pair`, `pair_add_left/right` | biadditive into an ordered target | the absence itself |

> **THREE OPEN SLOTS, DELIBERATELY NOT FIELDS.** **Requiring definiteness would encode the
> conclusion** — a positive pairing is what the clause needs *proved*, and a spec demanding it as
> input grades every candidate a success. **The W-2 trap in exact form, refused at birth.** The
> *"sees the zeros"* half is an **opaque `Prop` this kernel cannot check**, and says so.

**THEOREM ONE — `no_idempotent_candidate`: no candidate with idempotent addition satisfies the
specification at all.** `(R1)` forces it to the zero object; the zero object cannot supply
`(R3d)`. **Two fields collide; the characteristic-one family is graded out.** Universal form
`signedCompletion_trivial_of_idempotent` stated by its generation property, library-independent.
**DERIVES, and CLASSICAL — what is new is only that it is compiled.**

**Salt-checks from birth:** `spec_satisfiable` (witness `ℤ × ℝ`) · **`witness_degenerate` and
`witness_not_definite` — THE ANTI-ENCODING CHECK: that same witness satisfies every field and its
pairing separates nothing** · `translation_additive_iff_zero` — `(R4)` load-bearing, a
translation is additive **iff `t = 0`**.

**Axiom profiles — eight terminals, none outside the clean profile:**

```
map_eq_zero_of_idempotent                [propext]
signedCompletion_trivial_of_idempotent   [propext]
translation_additive_iff_zero            [propext]
trivial_of_idempotent_of_spec            [propext, Classical.choice, Quot.sound]
no_idempotent_candidate                  [propext, Classical.choice, Quot.sound]
spec_satisfiable                         [propext, Classical.choice, Quot.sound]
witness_degenerate                       [propext, Classical.choice, Quot.sound]
witness_not_definite                     [propext, Classical.choice, Quot.sound]
```

**Three weaknesses declared in the README rather than left to be found.** `.lake` gitignored at
creation, per the standing law.

> **REMOTE HELD.** Committed locally at `20f1860`; **no GitHub repository created, nothing
> pushed.** A new federation repo's visibility is a publication-partition decision and I do not
> take it unilaterally. **Awaiting the author's word.**

---

## §4 — THE INWARD INVENTORY, RIDING BESIDE

Per the E3 precedent, **the corpus's own objects get no exemption.**

| corpus holding | the field it most likely fails |
|:--|:--|
| Chapter 13's divisor ladder, at its levels | **`pair`** — a conservation statement, not a pairing carrier |
| the formation coordinates (Δn₄ = +1) | **the type itself** — a count is not a class object |
| the register pentagon | **`act`** — a map of the premise, not an endomorphism action |
| `h1_complete_at_Phi` | **all data fields** — conditions on ξ at a point, not a space |
| the validated Epstein channel | **`arch_present`**; and the family is Euler-product-free |

> **The inventory's verdict is unchanged by the spec's existence: a certified surround, a proved
> seal, a quantified absence, a mapped premise — and no candidate carrier.** The spec makes that
> **checkable at a named field** instead of arguable in prose. **That is the whole of what it
> adds: not nothing, and not much.**

**No grading has been run.**

---

## §5 — FOUND-BEYOND-REGISTRATION *(NOT EMPTY — one item)*

1. **THE ENRICHED SCHOOL DID NOT ESCAPE THE STRIPPED SCHOOL'S TERMINUS — TORIC VARIETIES BOTH.**
   Not registered, not sought, and **it qualifies the "enrich, don't strip" learning at the exact
   moment that learning is being filed.** Filed with it rather than after it.

## §6 — STOP-AND-HOLD

**Nothing constructed toward the clause.** The specification grades and is proved insufficient by
its own witness; theorem one is classical; the completed sentence names nothing; the two-channel
coordinate is held at observation grade. **No synthesis here constitutes progress on the clause,
and the one design decision taken — archimedean-inclusion from the ground up — is a *modelling*
choice justified by two external arrests, not a mathematical step.**

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `38d9f33` → this pass's commit |
| relay | `a1074ec` → this report's commit |
| **`SIDE-carrier-spec`** | **`20f1860` (v0.1.0, local only — remote held)** |
| **rail `de621b1` / `2147a03`** | **UNMOVED** |

**Nothing deposits.**
