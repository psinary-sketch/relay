# THE WAVE-WIDE CORRESPONDENCE RE-GRADE — SITTING 4 — 2026-08-09

**The rail authorization was granted and NOT CONSUMED — it was not needed.** Block 1 of the
statement-read proper is banked: **13 rows read, 11 CONFIRMED, 1 RE-GRADED, 1 repaired.**
Rail at `de621b1` / `2147a03`, **unmoved**. **Nothing deposits.**

---

## §1 — ITEM 1: THE SIMPLICITY REPAIR LANDED, AND THE RAIL WAS NEVER TOUCHED

**Before landing I read the rail's own copy, and it does not contain the row.**

| | |
|:--|:--|
| `PLACE-phase1.5/keystones/SIMPLICITY_OF_RIEMANN_ZEROS.md` | last touched **2026-05-27** (`f862f39`) |
| occurrences of `RegisterPentagon` in it | **0** |
| lines differing from the PLACE-papers copy | **121** |

**The rail's SIMPLICITY is a May snapshot. The cell I was authorized to change exists only in the
working corpus.** So the repair landed in `PLACE-papers` and the rail repos were not opened.

> **THE AUTHORIZATION IS RETURNED UNUSED. No rail baseline moves: `PLACE-phase1.5` stays at
> `de621b1` and `PLACE-phase2` at `2147a03`, both with clean working trees, verified after the
> edit.** There is no break to record, because there was no break.

**The repair, exactly as prepared and verified in sitting 3 — `git diff --numstat` reports `1 1`,
one line:**

| cell | before | after |
|:--|:--|:--|
| terminal | `SIDELvConservation.RegisterPentagon` | `SIDELvConservation.RegisterPentagon.goalState_of_h1_h2` (the goal-state theorem inside the pentagon namespace; faces R1..R5 + graded edges are that namespace's other declarations) |
| profile | `{propext, Classical.choice, Quot.sound}` | same string, now sourced — **printed at `2d86182` by `#print axioms`, 2026-08-09** |
| grade | *STRUCTURE compiled — the five register faces and the goal-state Prop; the cross-register equivalences are **NOT-COMPILED** (compiling them would encode RH-equivalence, the W-2 trap)* | **unchanged, word for word** |

---

## §2 — A COUNT CORRECTION BEFORE THE READ

The ferry sizes the read at **PATHS 31 + SURROUND 29 = 60 rows**. Those are **distinct terminal
counts**, not row counts. Extracted from the Correspondence tables:

| paper | rows carrying a terminal |
|:--|--:|
| PATHS | **32** |
| SURROUND | **13** |
| **total** | **45** |

**The read is 45 rows, not 60.** Reported before the read so the denominator is not quietly
adjusted afterwards.

---

## §3 — BLOCK 1 BANKED: THE REGISTER-PENTAGON EDGES (13 rows)

The pentagon rows were read first because they are the densest cluster and because sitting 3's
repair touched them. **Every statement read at the row's pin, every proof term inspected.**

**THE STRUCTURAL FACT THE READ ESTABLISHES — and it is the reason these rows needed reading rather
than diffing. Five of the R-family theorems are PURE MODUS PONENS:**

```lean
theorem R1_universality_to_goal   (universalityBridge : Register1_… → GoalState 𝒞 s) (h : …) : GoalState 𝒞 s := universalityBridge h
theorem R2_conservationHypothesis_to_RH (kernelBridge : Register2_… → RiemannHypothesis) (h : …) : RiemannHypothesis := kernelBridge h
theorem R4_positivity_to_RH       (liCriterion : Register4_positivity lam → RiemannHypothesis) (h : …) : RiemannHypothesis := liCriterion h
theorem R5_output_HilbertPolya_to_RH (hpBridge : Register5_output_HilbertPolya → RiemannHypothesis) (h : …) : RiemannHypothesis := hpBridge h
theorem R4_channelDecomposition   (lam_additive : ∀ …) … := lam_additive lam_A lam_Z n
```

**`(A → B) → A → B` is function application. These carry no mathematical content whatever** — which
is exactly the Voice7 shell shape the ferry asked to be flagged first-class.

**AND THE PAPER SAYS SO, ROW BY ROW.** This is the finding: the shells are graded as shells.

| row | terminal | paper's grade | verdict |
|:--|:--|:--|:--|
| L290 | `R1_universality_to_goal` | **INTERFACES** — *the universality hypothesis as explicit hypothesis* | **CONFIRMED** |
| L289 | `R4_positivity_to_RH` | **INTERFACES** — *Li's criterion (Bombieri–Lagarias 1999, **not in Mathlib**) as explicit hypothesis* | **CONFIRMED** |
| L291 | `R5_output_HilbertPolya_to_RH` | **INTERFACES — DISCLAIMED** *(HP bridge named; asserted never; closes over 𝔽_q, open over ℚ)* | **CONFIRMED** — stronger than required |
| L288 | `R4_channelDecomposition` | DERIVES *(cross-kernel; **combinatorial stream-level only** — the analytic η↔Taylor-of-log-ξ identification is manuscript-resident)* | **CONFIRMED** — the grade attaches to `LiLinearMap.lam_add`, and the limitation is stated |

**The three content-bearing pentagon theorems, checked against their grades:**

| row | terminal | proof term | grade | verdict |
|:--|:--|:--|:--|:--|
| L286 | `R5_input_at_Phi` | `C5_input_at_Phi` | **DERIVES (native)** | **CONFIRMED** |
| L285 | `goalState_of_h1_h2` | `T3.T3prime_shared_witness 𝒞 s h1 h2` | **DERIVES (native, via `T3.T3prime_shared_witness`)** | **CONFIRMED** — the cell names the exact route the proof takes |
| L292 | `certifiedInput_not_zeroRealizing` | tactic | **INTERFACES** (named premise `NontrivialZeroExistsInStrip`) | **CONFIRMED** — matches the signature |

**Also read and confirmed:** L36/L294 `partialPositivity_finiteRange` — three named hypotheses
(`hV`, `hEF`, `hTail`), conclusion `0 ≤ lam n` for `1 ≤ n ≤ N₀ T`; the docstring itself says *"This
is NOT a proof of RH — the all-n tail is the open gap."* **INTERFACES, three stipulations, honest.**
L35 `goalState_sevenClasses_of_h2` · L47 `lowFinset_mem_iff` · L37 `R1_universality_to_goal` (second
citation) — all consistent with their cells.

---

## §4 — THE ONE RE-GRADE: PATHS L287, DERIVES → INTERFACES

**The row:** *Register pentagon — R2 (ConservationHypothesis) → RiemannHypothesis*, citing
`ConservationBridge.riemann_hypothesis` at SIDE-kernel `0bc21c0`, graded **DERIVES**.

**The statement, read at that pin:**

```lean
/-- The Riemann Hypothesis, conditional on Conservation. Zero sorry. -/
theorem riemann_hypothesis (h_cons : ConservationHypothesis) : RiemannHypothesis :=
  rh_from_structural_exhaustiveness (structural_exhaustiveness_proved h_cons)
```

**It is a genuine derivation — not a shell — but it is CONDITIONAL on a named premise.** Three
independent sources agree that makes it INTERFACES:

1. **The corpus's own rubric**, stated verbatim in the corpus: *"DERIVES / INTERFACES-with-named-premise / NOT-COMPILED."*
2. **README already grades this exact terminal** *"Route 3 — an **INTERFACES** terminal on the open premise `h2`, carried openly."*
3. **The row's own parenthetical** already concedes *"bridge attributed as **named premise** per the federation no-Lake-dep rule."*

> **RE-GRADED: DERIVES → INTERFACES. Shortfall: one clause — the conditionality — which the row
> already disclosed in its parenthetical while its grade word said otherwise.** The whole
> parenthetical is kept; the re-grade and its reason are written into the cell. **PATHS is not a
> rail file, so this landed** under the standing non-rail rule.

**This is the first genuine grade change of the re-grade, and it is a downgrade of the headline
Route-3 row.** It is also the smallest possible one: no mathematics moves, the terminal is unchanged,
and the corpus was already saying INTERFACES in two of three places.

---

## §5 — DELTA TABLE

| outcome | count | detail |
|:--|--:|:--|
| **CONFIRMED at grade** | **11** | 7 pentagon edges (§3) + `partialPositivity_finiteRange` + 3 further pentagon citations |
| **RE-GRADED** | **1** | PATHS L287 `ConservationBridge.riemann_hypothesis`: **DERIVES → INTERFACES**, named premise `ConservationHypothesis`, shortfall 1 clause |
| **REPAIRED (landed)** | **1** | SIMPLICITY L446 profile cell — item 1 |
| **STRUCK** | **0** | |
| **BLOCKED** | **0** | |
| **HELD-AT-RAIL** | **0** | **the authorization was not needed and is returned unused** |

**ROWS STATEMENT-READ TO DATE — machine checks do not count:**

| sitting | rows read |
|:--|--:|
| 1 (the three SIDEDerivative rows) | 3 |
| 3 (the three `spectral_cannon` label rows) | 3 |
| **4 (block 1, the pentagon cluster)** | **13** |
| **total read** | **19** |
| **remaining unread** | **99 − 19 = 80** |

**Of the 45-row PATHS+SURROUND read specifically: 13 done, 32 remain** (PATHS 19 + SURROUND 13).

---

## §6 — WHAT BLOCK 1 SAYS ABOUT THE GROUND

**The densest and most exposed cluster in the corpus — five theorems that are literally function
application, sitting under a Route-3 RH claim — is graded honestly row by row**, with the premises
named, one row disclaimed outright, and the analytic gap stated in the docstring rather than hidden.
**Eleven of thirteen confirmed, one downgrade of one clause, no strikes.**

**That is evidence about the ground, not a verdict on it. Eighty rows are unread**, and pass 2 stays
closed until the delta table covers them.

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | → this pass's commit (SIMPLICITY L446 · PATHS L287) |
| relay | → this report's commit |
| **rail `de621b1` / `2147a03`** | **UNMOVED, both clean — authorization returned unused** |

**Pass 2 stays closed. Nothing deposits.**
