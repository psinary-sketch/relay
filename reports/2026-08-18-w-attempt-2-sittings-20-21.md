# `W-ATTEMPT-2` · SITTINGS 20–21 — THE LIMIT, AND THE PENTAGON RE-READ
## ### **THE LIMIT'S THREE QUESTIONS: ALL THREE `(survives)`, AT PROOF GRADE — THE CONSTRAINED SECTOR IS POSITIVE-DEFINITE IN THE LIMIT, THE COMPRESSION IS THE STRONG LIMIT OF THE LEVEL COMPRESSIONS, AND ONE REMAINDER IS NAMED EXACTLY — AND THE PENTAGON RE-READ: FOUR FACES DESCRIBE THE ABSENCE, THE FIFTH PREDICATES OVER IT; FILED AS A KEYSTONE DRAFT**

**Relay report · 2026-08-18 (fortieth/forty-first sittings) · author-called · Fable/high effort,
proof-search · sub-gate declared · the register untouched · nothing deposits · nothing circulates**

> ### **RULE-3 LOG:** *the h = 1 sitting at `df3c426` ✓ · the limit registration executed in its OWN
> words ✓ · the pentagon's faces read at their terminals (`RegisterPentagon` at `SIDE-lv-conservation`
> `v0.10.0 = 93c27ec`, as banked at `CARRIER_BUILD §12.1`) ✓ ·* ### **the Mathlib state CHECKED BY GREP,
> NOT RECALL — a local checkout exists (`/d/mathlib4 @ cecd0c4d56`, 2026-04-10) and was grepped.**
> *Terms coined: none.*

---

## §1 — SITTING 20: THE LIMIT AT ONE PLACE *(the registration's three questions, executed; `S̄` = the `L²(ℚ₂)`-closure of the tower's union; every banked input exact at its pin)*

> ### **Q1 — THE TRANSFORM SURVIVES: CLOSED AT PROOF GRADE.** *`F` is unitary on `L²(ℚ₂)`
> (Tate/Plancherel, standard at text — and NOT compiled in Mathlib, per §1.4) and preserves every
> level exactly (banked, b21/b23). A unitary maps the closure of an invariant union to itself:
> `F(S̄) = S̄`, and `F|_S̄` is unitary.* ∎
>
> ### **Q2 — THE RADICAL STAYS ZERO, AND THE STRUCTURE IS THE FOUR-SECTOR DECOMPOSITION: CLOSED.**
> *Radical: if `⟨f, Fg⟩ = 0` for all `g ∈ S̄`, then since `F(S̄) = S̄` we have `f ⟂ S̄` and `f ∈ S̄`,
> so `f = 0`.* ∎ *Structure: `F⁴ = 1` on `S̄`, so the four bounded projections
> `Π_λ = ¼Σ_k λ^{−k}F^k` (`λ ∈ {1, −1, i, −i}`) are orthogonal and sum to `1`:*
> ### **`S̄ = E₁ ⊕ E₋₁ ⊕ Eᵢ ⊕ E₋ᵢ`, with `B(f, f) = ⟨f, Ff⟩ = ‖f‖²` ON `E₁` — THE CONSTRAINED SECTOR
> IS POSITIVE-DEFINITE IN THE LIMIT, AT PROOF GRADE — `−‖f‖²` on `E₋₁`, and the Hermitian part
> vanishing identically on `Eᵢ ⊕ E₋ᵢ` (the twist signature's `(d/4, d/4, d/2)` is exactly this
> decomposition's finite shadow — `ι` is `F`-equivariant, banked exact, so each `E_λ(S̄)` is the
> closure of its level tower).** *Nondegenerate form; persistent half-kernel of the Hermitian part;
> NEITHER PROMOTED INTO THE OTHER — both now proved, one place, at the model's limit.* ∎
>
> ### **Q3 — THE COMPRESSION STAYS FORCED, AND IS THE STRONG LIMIT OF THE LEVEL COMPRESSIONS:
> CLOSED, WITH THE ONE REMAINDER NAMED.** *Ball-vanishing (both sides) is an `L²`-closed condition,
> so `S̄` keeps the Sonin conditions; the banked exact witnesses (a nonzero locally-constant value of
> `(Uf)^` on a positive-measure coset of the ball) live at finite level, hence in `S̄`: `U(S̄) ⊄ S̄`
> — the compression `SUS` is FORCED in the limit.* ∎ *And a small closed theorem beyond the price:
> the level projections `S_n` increase to `S` (dense union), so* ### **`S_n U S_n → S U S` in the
> strong operator topology — the limit's compressed scaling IS the limit of the levels'.** ∎
> ### **THE REMAINDER, NAMED EXACTLY: the SPECTRUM of the contraction `SUS`. SOT convergence does
> not control spectra, and no norm-convergence is banked — that, and only that, stays open from the
> registration's list.**

### §1.4 — THE MATHLIB COMPANION'S SPEC, UPDATED BY GREP *(checkout `cecd0c4d56`, 2026-04-10)*

| need | grep verdict |
|:--|:--|
| `ℚ_p` locally compact + Haar | ### **ASSEMBLY, NOT ABSENCE:** `Padics/ProperSpace.lean` compiled; abstract Haar (`MeasureTheory/Measure/Haar/*`) compiled; no `ℚ_p`-specific measure file |
| the Fourier transform on `ℚ_p` | the ABSTRACT `fourierIntegral` (VectorFourier) exists; ### **no p-adic Fourier file exists (`NumberTheory/Padics/` grep: empty); the self-dual character and the `ℚ_p ≅ ℚ̂_p` identification are MISSING** |
| Plancherel | real/Schwartz-side only (`Analysis/Fourier/LpSpace`); ### **no LCA Plancherel — MISSING** |
| Schwartz–Bruhat | ### **ABSENT entirely (grep: zero hits)** |
| cyclotomic towers | `NumberTheory/Cyclotomic/` present (Basic · PrimitiveRoots · PID · …) — the tower machinery EXISTS |

**Scope, restated: ONE place; the double limit untouched; everything above is about the MODEL'S limit
object, never the ledger.**

## §2 — SITTING 21: THE PENTAGON RE-READ *(each face against the h = 1 finding — the sign mechanism trivial and universal at every finite instance; the difficulty the codomain at complete roster; both branches longhand per face in the keystone draft; summary verdicts here)*

| face | sign statement, or codomain-description in disguise? |
|:--|:--|
| **R1 universality** | ### **codomain-description (totality form):** at every finite instance the sign is free; what fails at the roster is having the OBJECT that holds the totality |
| **R2 conservation** | ### **an ADDRESS statement of the crossing — sign-free content** (the balance is an equality; its model home, the flip channel, is class-resolution structure) |
| **R3 totality (`∀∃⟹∃∀`, the open `sorry`)** | ### **the codomain-absence stated logically — the cleanest case: the repo's own `sorry` sits exactly where the double limit sits** (the diagonal's shadow-instance banked) |
| **R4 positivity** | ### **THE ONE FACE WITH SIGN-CONTENT — AND ITS SIGN-CONTENT ATTACHES TO PRECISELY THE MISSING OBJECT:** the predicate half is satisfied trivially at every finite instance (measured, h = 3 and h = 1); the content half (`λ_Z ≥ −λ_A`) references the `Z` channel, which is the absent codomain (sitting 16) — a sign statement whose SUBJECT is missing |
| **R5 spectral distance** | ### **codomain-description by its own compilation** (`certifiedInput_not_zeroRealizing`) |

> ### **THE RE-READ'S VERDICT, AND THE NON-FUSION LAW READ AGAIN: once the sign mechanism is known
> trivial at every finite instance, the cross-register equivalences' whole content is the
> limit/codomain step — so "compiling the equivalences would encode RH-equivalence" and "the pairing
> has no codomain at complete roster" are ONE statement in two registers. The pentagon cannot be
> fused because fusion IS the construction of the missing codomain.** *Filed as a KEYSTONE DRAFT —
> `phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE.md` — each face's reading anchored in a compiled
> terminal plus a measured fact; every reading individually at question grade; the draft watermark on
> its face; `h2` untouched by every word.*

## §3 — THE RECORD

*Correspondence rows 56–58 · `FINDINGS` `F.2026-08-18f` · the packet current (the limit verdict; the
keystone pointer) · both road documents' arc lines extended · pins below.*

**`h2` UNCHANGED. THE REGISTER SENTENCE UNTOUCHED. NOTHING AT COMPLETE ROSTER. NOTHING DEPOSITS.
NOTHING CIRCULATES.**
