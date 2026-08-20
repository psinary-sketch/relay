# THE PURITY CHECK AT THE BANKED CELLS — REGISTERED AND RUN, ONE ACT
## ### **VERDICT (b): MIXED — AND AT THE TWO DECIDED CELLS, MIXED-FORCED: E₁(3,1) AND E₁(2,2) CONTAIN NO NONZERO SCHMIDT-PURE VECTOR AT ALL (THE UNIQUE (3,1) UNIT IS MIXED; THE (2,2) PENCIL-GCD IS 1 OVER ℚ(ζ₁₆)[t]) — EVERY CANONICAL SPANNING UNIT AT (5,1), (2,3), (3,2) IS MIXED BESIDES — THE OBSTRUCTION HAS A LOCAL RESIDUE, AND THE SPACE-LEVEL TENSOR-SQUARE QUESTION CLOSES NEGATIVELY AT THE BANKED CELLS**

**Relay report · 2026-08-19 (the machine clock reads 2026-08-20 — noted, not forced, the week-close
precedent) · ferry-executed (part 1 of 1, receipt-in-full confirmed before execution, Rule 1) ·
Rules 3/4/5 · exact ℤ[ζ] arithmetic throughout, no floating point anywhere · nothing deposits ·
nothing circulates · `h2` UNCHANGED.** Scope, once: this act registered and executed the per-place
Schmidt-purity check of the banked E₁-units, reports the verdict against the registered branches,
and stops; it makes no claim about the `h2` identity, alters no kernel; the foot restates the
author's two pending rulings without acting on them.

> ### **RULE-3 LOG:** *(a) the minor test (Schmidt-pure ⟺ rank 1 ⟺ every 2×2 minor vanishes) —
> load-bearing, VERIFIED longhand in the registration, with the two exactness directions stated
> (vanishing certified in ℤ[ζ] reduced mod `Φ_N`; non-vanishing certified through the ring
> homomorphism `ζ ↦ g` into `F_ℓ`). (b) the four-sector decomposition from `M⁴ = I` — VERIFIED AT
> CONTENT before dependence: b23 (`M² = Π` brute-forced entry-exact at `n ≤ 3`, `Π² = I`) and b26
> (`R = (1+M+M²+M³)/4` projects onto `E₁`, `tr R = d₁`), the finite-place-closure sittings' own
> banks; re-derived in-run besides (gates G1/G4). (c) "pure fixed vectors are graph-shaped" —
> NOT CITED anywhere in this act; the minor test stands without it, per the ferry's own line.
> DISAGREEMENT REPORTED, NOT SMOOTHED: the ferry's template names "the banked E₁-unit at cell
> (2,1)" — the banked record says d₁(2,1) = 0: NO E₁-unit exists there (the arrival-depth death,
> b23 T4/b26 T4e); the (2,1) minor test ran on the Sonin generator per the no-weight clause.
> Terms coined: the three verdict labels `MIXED-FORCED` / `MIXED-generic` / `NO-UNIT`
> (content-descriptive; the banned-stem grep — the agent-metaphor class of correction
> twenty-four — clean). ORIENTATION RUN: the leaves report at `7142eac`; the week-close board;
> the loom's act-16 consolidation (`THE_GLOBAL_SECTION.md` `v1.0`); the acts narrative `R1-1.0`.*

---

## §1 — THE REGISTRATION (banked BEFORE any arithmetic: `data/b44_registration_2026-08-19.txt`)

The ferry's registration verbatim in content, both branches longhand — **(a)** pure at every cell:
the obstruction confirmed genuinely global, no local residue, boundary-candidate; **(b)** mixed at
some cell: the obstruction partially relocates, each mixed cell's place gains a local address,
debt-candidate into the queue as a named work-order with a trigger; the (2,1) run registered
no-weight — with **the routing deviation recorded inside the registration before computing**
(Rule 4.6):

> **THE DEVIATION:** no per-unit coefficient files exist anywhere in the corpus. The E₁-units are
> banked as (i) a proved-existence CHOICE CLASS (*"the units exist; no canonical choice is
> claimed"* — R1-1.0) and (ii) exact eigen-dims per cell (b20/b22/b23/b26; `SectorArithmetic.lean`
> @ `ab79acd`). The check therefore reads PER CELL on the whole E₁-space, constructed canonically
> in-run as the image of the sector projector `4q·P₁ = (q + S)(1 + Π)` on the Sonin basis —
> entries stay in ℤ[ζ_N] throughout. Second deviation: B13's seventh cell (5,2) carries
> float-only data (no exact eigen-dims banked) and is NOT on the exact roster — declared, not
> silently dropped.

## §2 — THE ROSTER AS READ, WITH PROVENANCE

| cell | place | `N` | dim Son | banked `(d₁, d₋₁, dᵢ, d₋ᵢ)` | provenance of the coefficient data |
|:--|:--|:--|:--|:--|:--|
| (2,1) | 2 | 4 | 1 | (0,0,1,0) | chart + Sonin split: b13 @ `4e01a6f`; dims: b23 / `SectorArithmetic` @ `ab79acd` |
| (3,1) | 3 | 9 | 4 | (1,1,1,1) | same; dims: b26 @ `ab79acd` |
| (2,2) | 2 | 16 | 9 | (2,2,3,2) | same; dims: b23 @ `ab79acd` |
| (5,1) | 5 | 25 | 16 | (4,4,4,4) | same; dims: b20/b22 (sittings 7/9) @ `ab79acd` |
| (2,3) | 2 | 64 | 49 | (12,12,13,12) | same; dims: b23 @ `ab79acd` |
| (3,2) | 3 | 81 | 64 | (16,16,16,16) | same; dims: b26 @ `ab79acd` |

*The units' coefficient data is CONSTRUCTED, not read: `u_{i,j} = 4q·P₁ f_{i,j}`, coefficient
formula `u(m) = q·h(m) + Σ_{m'} h(m')·ζ^{m'm}` with `h = f + Πf` — the projector identity
`4·P₁ = 1 + M + M² + M³ = (1 + M)(1 + Π)` resting on `M⁴ = 1`, verified in-run (G1). Lineage
claims above are from the reads, not recall.*

**The five exactness gates, ALL PASS at ALL SIX CELLS** (the bank holds the lines): **G1** the
geometric-sum identity (`Σ_m ζ^{mt} = 0` for every `t ≠ 0`, reduced mod `Φ_N`) — hence `S² = q²Π`
exactly; **G2** `Π` an involutive permutation; **G3** every `u` vanishes on the ball with zero row
sums (Son membership; `Su = qu` then algebraic, spot-checked directly besides); **G4** the
projector trace `Σ u_{i,j}(i+qj) = 4q·d₁` exactly in ℤ[ζ] — **the banked `d₁` RE-DERIVED at every
cell, not assumed**; **G5** span rank mod `ℓ` = `d₁` — with G4, the spanning set is exactly `E₁`.

## §3 — THE PER-CELL VERDICTS

| cell | `d₁` | verdict | the finding, exact |
|:--|:--|:--|:--|
| (2,1) | 0 | **NO-UNIT** | `(1+Π)f = 0` — the projector image is 0 exactly; the Sonin generator's minor test: all 2×2 minors vanish (1-dim: pure by shape) — **registered no-weight, counted for nothing** |
| (3,1) | 1 | ### **MIXED-FORCED** | the unit is UNIQUE up to scale — and its minor at rows (1,2), cols (0,1) is nonzero in ℤ[ζ₉]: **E₁(3,1) contains no nonzero pure vector; no choice exists to make** |
| (2,2) | 2 | ### **MIXED-FORCED** | every vector is `αu₁ + βu₂` (independence exact; span = E₁ by G4/G5). The minor at rows (1,2), cols (0,2) of the pencil expands `α²A + αβB + β²C` with `A ≠ 0, B = 0, C = 0` (all three decided in ℤ[ζ₁₆]) — purity forces `α = 0`; and `u₂` is itself mixed (rows (1,3), cols (0,1)). Independently: the GCD of all 18 nonzero minor-quadratics in ℚ(ζ₁₆)[t] is 1 — **no nonzero pure vector over ANY field extension** |
| (5,1) | 4 | **MIXED-generic** | all 16 canonical spanning units MIXED, exact witness minors each |
| (2,3) | 12 | **MIXED-generic** | all 48 canonical spanning units MIXED, exact witness minors each |
| (3,2) | 16 | **MIXED-generic** | all 64 canonical spanning units MIXED, exact witness minors each |

*Vanishing patterns and witness indices per unit: the bank (`data/b44_2026-08-19.txt`). At the
three `d₁ > 2` cells the full Segre-intersection question (does ANY pure vector hide in `E₁`?) is
beyond this instrument and DECLARED so — the named work-order at the foot — but no spanning unit
and no tested combination is pure anywhere on the roster.*

## §4 — THE VERDICT AGAINST THE REGISTERED BRANCHES, STATED PLAINLY

> ### **(b) LANDS — MIXED, at every cell that has units at all.** **Which cells and at what
> grade: (3,1) and (2,2) at the FORCED grade — the local address is not merely "the banked unit
> is mixed" but "NO pure unit exists to choose"; (5,1), (2,3), (3,2) at the generic grade — every
> canonical unit mixed, existence at `d₁ > 2` open. (2,1) has no unit and its pure-by-shape
> reading carries the registered zero weight.**
>
> **(a) REFUSED as registered — and more: the leaves report's proved layer argued from "suppose
> the best case: every local unit pure". The best case is FALSE at the banked cells. The
> obstruction is two-layered in the STRONG sense: the `∏`-coupling blocks the sector data
> globally (act 1's proved layer, standing untouched) AND the per-place units are themselves
> never elementary at the decided cells — a local residue exists.**
>
> **The named-step layer's question closes at its cells:** whether `⊗′S̄_v` is a tensor square OF
> SPACES required units choosable as pure tensors; at (3,1) and (2,2) no such choice exists —
> **the gluing data itself is never elementary there. THE RANGE LAW ON THE FACE: a finite-instance
> statement at the banked cells and no wider — deeper tower levels and the level-limit `E₁(S̄_v)`
> are not decided by this act, and nothing about them is claimed.**

**Filing species, per branch (b): debt-candidate — the local addresses enter the queue as a named
work-order. THE MARK IS FILED FLAGGED, NOT CHOSEN: the diamond vocabulary (debt vs boundary) is
the author's pending ruling (the foot); this filing does not preempt it.**

**THE WORK-ORDER, NAMED:** *the Segre intersection at the `d₁ > 2` cells (5,1), (2,3), (3,2) —
decide exactly whether any pure vector exists in `E₁` there (the pencil method generalizes to a
quadric system on `ℙ^{d₁−1}`; exact Gröbner or a structured collapse like (2,2)'s `α²`-collapse).
Trigger: the author's diamond ruling landing, or his word, whichever first.*

## §5 — THE RECORD

*The instrument: `tools/e16/b44_e1_unit_purity.py` + `tools/e16/b44_pencil.py` (registration
banked before the run; register|run per the template). The bank: `data/b44_2026-08-19.txt` —
gates, per-unit verdicts, witness patterns, the pencil block, the independence certificate, the
axiom print. **The Lean draft (ferry step 6, the check landed finite and exact throughout):
`tools/lean/E1UnitPurityDraft.lean` — WORKING LAYER ONLY, NOT KERNEL-PLACED — vanilla Lean 4
(v4.29.1 pinned), no imports, no Mathlib, decide only; NINE terminals, every one "does not depend
on any axioms"** (death_2_1 · unit31_mixed · the four (2,2) pencil terminals · witness51 ·
witness23 · witness32 — the (3,2) instance reaches ℤ[ζ₈₁] sparse; one intermediate propext leak
via getD/prop-ite caught by the axiom print and rewritten match-free — the SectorArithmetic
precedent, disclosed). It decides every cell's arithmetic core, including both halves of the
(2,2) MIXED-FORCED certificate; `d₁` values and basis-independence enter as banked data, declared
in its head. Correspondence rows 175–176. Pins: pre-act `origin/main = 7142eac` (ls-remote,
verified); this act's own pin read back with ls-remote after the push and recorded in the pin
line below.*

> **PIN LINE (post-push read-back, ls-remote):** `relay origin/main = b2163d85990e92fd4696e34c879d3ef78585b083`
> *(this act's commit, VERIFIED by remote read; pre-act tip `7142eac` its parent; pushed from
> `push-e1-unit-purity` per Rule 4.10, the pre-push hook standing; the HELD commit's two files
> verified ABSENT from the pushed tree; no `held/*` ref on the remote. This pin-line commit's own
> SHA is stated in the closing message, per the regress rule.)*

## FOOT — THE AUTHOR'S DESK, RESTATED, NO ACTION TAKEN

· **Ruling 1, currency:** whether the 103 zero-axiom terminals and the five classical-profile
  files become a federation pair (proposed `SIDE-global-section` + `SIDE-global-section-mathlib`,
  on the spinor-calibration precedent) or stay relay-resident. **This act adds one object to that
  desk without moving it: `E1UnitPurityDraft.lean` (nine zero-axiom terminals) sits in the
  working layer awaiting the same ruling — the recommendation is that it ride with the ruling,
  whichever way it goes; kernel placement is not this ferry's act.**
· **Ruling 2, the two monograph sentences:** the v5.13 compression-paragraph line; the §25.8
  live-concordance row downstream of ruling 1. Additions, never corrections.
· **Navigator recommendation, restated, not a ruling:** settle the diamond vocabulary (debt vs
  boundary) before this check's result is filed finally — this report files ONCE with the mark
  FLAGGED, per the ferry's own clause, so the ruling can land on a standing record.

**`h2` UNCHANGED. THE REGISTER SENTENCE UNTOUCHED. NO IDENTITY DECIDED; NO REGISTER MOVED.
NOTHING PROMOTED. NOTHING DEPOSITS. NOTHING CIRCULATES.**
