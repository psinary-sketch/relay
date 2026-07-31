# INVARIANCE_BARRIERS v1.2 — author-ratified R1–R6 (T5 form-level correction foremost) — 2026-07-31

Source verified before editing: `phase1.5/method/INVARIANCE_BARRIERS.md` v1.1.1, md5
`f9cd30f5344a61043a3ec45fafb5b0b9` (exact match), PLACE-papers `e9410a9` local = remote, tree clean.
Standing protocol: mirror current at the same pin (2026-07-31 rebuild, no commits since); rowgen diff
run against the paper's Correspondence table at the standing config (9 terminals incl.
`ConservationBridge.riemann_hypothesis`, pins v1.7 = `2957e7d`): **all 9 rows ok**. One tool transient
recorded honestly: the first diff run returned `ConservationBridge.riemann_hypothesis: MISSING at pin`;
a direct `lake env lean` audit resolved it immediately with the full verbatim profile (`depends on
axioms: [propext, Classical.choice, Quot.sound]`), and the diff re-run returned all-ok — a transient
resolution failure in the tool's lake invocation, not a kernel state change (kernel unmoved at
`44895f9`, v1.7 = `2957e7d`). Refine-not-rewrite honored: Theorem 3.1 and the §3 development untouched.

## R1 — the mathematical fix (foremost)

**What was wrong.** The clause-(i) T5 row displayed ξ_Q with ξ's counting law ("the same
N(T) ∼ (T/2π) log(T/2π) asymptotic"). ξ_Q's completed form carries the **degree-2 gamma factor
(√23/2π)^s Γ(s)**, so its law runs at **N(T) ∼ (T/π) log(cT)** — asymptotically **twice** ξ's rate, a
conductor/degree effect. As displayed, T5 smuggled a constant-level agreement claim that is false.

**Fix per ruling (a) — T5 restated form-level in all three sites.**

Toolkit table row (corrected):

| tool | checkable property | quantity it computes |
|:--|:--|:--|
| **T5 zero-counting law (form-level)** | an order-1 argument-principle counting law N(T) ∼ c·T log T (Riemann–von Mangoldt type); the constant c is an output of T3, not an agreement datum | the form of the zero-counting law; the count to height T only up to the T3-determined constant |

Clause-(i) table row (corrected):

| tool | status | justification |
|:--|:--|:--|
| **T5 zero-counting law (form-level)** | **PROVED-FOR-BOTH** | Both witnesses provably carry a Riemann–von Mangoldt-type law, by the argument principle on the order-1 completion (T3). ξ: N(T) ∼ (T/2π) log(T/2π). ξ_Q: its completed form carries the degree-2 gamma factor (√23/2π)^s Γ(s), so its law runs at N(T) ∼ (T/π) log(cT). The constants differ and are excluded from the agreement clause — T5 asserts the form of the law, not its constant. |

Theorem 3.7's statement now names "T5 Riemann–von Mangoldt-type counting law (form-level; constants
excluded)". The honest sentence is in-text, bolded, immediately after the clause-(i) table: *"the
Epstein witness counts zeros at asymptotically twice ξ's rate … a conductor/degree effect of the
degree-2 gamma factor in its completion"* — no referee can find it unstated.

**Constant-smuggle sweep of the remaining five rows — clean.** T1 (FE centring σ = 1/2: structural
symmetry, shared), T2 (simple pole at s = 1: location/order only, no residue value claimed), T3 (order 1,
genus 1: form), T4 (real coefficients, σ > 1 convergence: form), T6 (codimension 2: structural). Only T5
had carried a constant-level display.

## R2–R5

- **R2**: §4.1 read — the modulo-qualifier lived only in the post-proof paragraphs, not at the statement.
  Attached at the statement site: theorem header now "E-Difficulty Theorem — skeleton closed; full
  dichotomy conjectured", with a scope paragraph between the statement and *Proof* naming the compiled
  skeleton (`e_difficulty`) and the open dichotomy. Body confirms the scope, so the heading is
  "Statement and proof of the skeleton".
- **R3**: §5.1 italic grade note (the κ(σ, distributive-law interface) = 0 identification is
  manuscript-resident, a structural reading, not a theorem of this paper) + a matching Correspondence
  row naming W-ORD-KAPPA-DISTRIBUTIVE. §5.3 one-sentence grade note for the κ(validity,
  natural-language) = 0 premise (manuscript-resident, empirically anchored to the cited cases).
- **R4**: §1.4 heading → "Provenance: the folklore and what is new". §5.4's "7/7" heading stands as
  ruled.
- **R5**: target-venue line out of the Abstract (MSC stays), into back matter as a one-line block beside
  Version history.

## R6 + tracking rule

Version v1.1.1 → **v1.2**, provenance entry leading with the T5 restatement. REGISTRY 1.5h-8 → v1.2,
~10,100 words, note updated.

**OPEN_TRAILS addendum filed** (one consolidation, completion triggers on every row; no orphaned
"conjectured"/"manuscript-resident" cell):

| work-order | status | completion trigger |
|:--|:--|:--|
| `W-ORD-T5-EPSTEIN-COUNT` | NEW | exact ξ_Q counting law with explicit constant (literature-cited or derived + doubly-sourced), feeding the family probe; opens with the family probe or at author call |
| `W-ORD-KAPPA-DISTRIBUTIVE` | NEW (§5.3 κ premise rides as second clause) | derivation/compiled evidence of the κ = 0 reading, or an honest-boundary filing; at author call, adjacent to Tier-2 |
| `W-ORD-E-DIFFICULTY-DICHOTOMY` | NEW row for the long-filed conjecture (no dedicated row existed) | §6.2 Mathlib plan items (1)–(5); item (5) = W-6-EXT-A (own trigger stands); opens when Mathlib gains FirstOrder-proof-object infrastructure, or author ruling |
| `W-ORD-FACE-E-INDISTINGUISHABILITY` | Tier 1 marked DISCHARGED (Theorem 3.7 @ `f48afd7`); Tier 2 trigger attached (was absent) | Tier 2 opens at a workable relativization theory for L-functions, or author ruling |

W-6-EXT-A confirmed already carrying its trigger ("reopens if/when Mathlib gains the Epstein/D-H
ingredient, or by author ruling"). Rider added to W-ORD-CONSTELLATION-BACKLOG recording the +2
intentional-provenance flags from the rename pass.

## Hygiene

Banned-word sweep clean (0 hits). New headings title-law checked. Word count 10,117 (naive split).
Mirror rebuilt post-commit at the new pin.

## Pins

- PLACE-papers: **`0d9a357`** (paper v1.2 + REGISTRY 1.5h-8 + OPEN_TRAILS addendum), pushed, local =
  remote verified. Mirror rebuilt at this pin (`mirror-refresh-2026-07-31.zip`, 20 entries).
- SIDE-kernel unchanged: `44895f9` on main, v1.7 tag = `2957e7d` (the paper's citation pin) unmoved.
- Nothing deposited; deposit set untouched.
