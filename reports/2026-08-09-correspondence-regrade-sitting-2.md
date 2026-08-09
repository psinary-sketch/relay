# THE WAVE-WIDE CORRESPONDENCE RE-GRADE — SITTING 2 — 2026-08-09

Slate item 1 continued. **The diff ran. One real defect found; sixty apparent ones were mine.**
Rail at `de621b1` / `2147a03`. **Nothing deposits.**

---

## §1 — EVERY CITED TERMINAL EXISTS AT A REACHABLE PIN

Sitting 1's resolver read working trees and under-resolved. **Rebuilt to go through
`git show <pin>:<file>` for all 90 configured terminals across 14 kernels:**

| check | result |
|:--|--:|
| file unreachable at its cited pin | **0** |
| declaration absent from that file at that pin | **0** |

**Not one Correspondence row cites a terminal that cannot be found where it says it is.** That is a
real negative result and it is the first thing the re-grade was supposed to establish.

---

## §2 — THE SOURCE-ONLY DIFF, AND WHY IT IS SOURCE-ONLY

`rowgen diff` calls `generate()`, which runs `lake env lean` per terminal at a 600 s timeout. **Ninety
terminals across fourteen kernels, most without `.lake` built, is not a sitting** — and worse, build
failures would be indistinguishable from missing terminals.

**Four of the diff's five checks need no build**: `doc`, `body1` and `defenc` all come from
`git show`, so status-vs-docstring contradiction, definition-encoded-graded-DERIVES, stale pin and
missing terminal are all decidable from source. Two small drivers were added —
`tools/rowgen/gen_source_only.py` and `diff_source_only.py` — which run those four and **leave the
axioms field empty by construction.**

> **THE ROUNDED-PROFILE CHECK IS NOT EXERCISED BY THIS SITTING AND MUST NOT BE REPORTED AS PASSING.**
> An absent profile is reported as absent. It needs builds and is queued.

**Result across all twelve papers:**

| | |
|:--|--:|
| rows matched and reported **ok** | **62** |
| status-vs-docstring contradictions | **0** |
| definition-encoded yet graded DERIVES | **0** |
| missing terminals | **0** |
| PIN mismatches | 60 — **see §3** |

---

## §3 — THE SIXTY "STALE PIN" FLAGS ARE MY CONFIG'S FAULT, NOT THE PAPERS'

The diff flagged sixty rows, e.g. *"row cites `1767bd6` but record pin is `2f71068`"*,
*"row cites `f374174` but record pin is `5e668b4`"*.

**Every one of those is an artifact of the config I generated in sitting 1, which stamped each
terminal with its kernel's CURRENT HEAD.** The rows do the correct thing: they cite **the pin at
which the row was verified** — `1767bd6` is lv v0.5.0, `c80bdc2` is v0.6.0, `bc4751e` is v0.5.1,
`f374174` is kernel v1.4. A Correspondence row that says *"verified at pin X"* and still says X is
**doing its job**; it is my record that asserted an arbitrary HEAD.

> **Reporting sixty stale-pin findings would have been a fabricated result, produced by my own
> config and dressed as an audit of the corpus. It is the same error as sitting 1's resolver, in a
> second costume: I imposed the present where the corpus deliberately records the past.**

**The fix for sitting 3 is structural, not cosmetic: the config's pin must be READ FROM THE ROW,
not from HEAD.** Then a genuine stale-pin flag means "the row's pin no longer contains the
terminal", which is worth knowing, instead of "the row is older than today", which is not.

**Discounting the artifact: the four build-free checks return ZERO defects across sixty-two matched
rows.**

---

## §4 — THE ONE REAL DEFECT: A NAMESPACE CARRYING AN AXIOM PROFILE

**`SIDELvConservation.RegisterPentagon` is a NAMESPACE, not a declaration** —
`SIDELvConservation/RegisterPentagon.lean` line 73 is `namespace RegisterPentagon`; the file's
theorems are `RegisterPentagon.goalState_of_h1_h2`, `.R5_input_at_Phi`, `.R2_conservationHypothesis_to_RH`
and so on. It exists at the cited pin `2d86182`, and the kernel's own `AxiomCheck_v0_10_0.lean`
prints axioms **per declaration** — never for the namespace.

**Two papers give it an axiom profile anyway:**

| paper | row |
|:--|:--|
| `SIMPLICITY_OF_RIEMANN_ZEROS.md` | `SIDELvConservation.RegisterPentagon` (faces R1..R5 + goal-state + graded edges) · **`{propext, Classical.choice, Quot.sound}`** · *STRUCTURE compiled* |
| `THE_UNCONDITIONAL_SURROUND.md` | `SIDELvConservation.RegisterPentagon` · **`{propext, Classical.choice, Quot.sound}`** · *Structure compiled* |

**`#print axioms RegisterPentagon` is not a valid query. That profile cannot have been printed, and
under the verification law — no profile that was not printed — the cell is unsourced.**

**WHAT IS NOT WRONG HERE, because the distinction is the whole point of the three-grade rubric.**
The **grade is honest and stays**: both rows say *structure compiled*, both state that the
**cross-register equivalences are NOT compiled**, and SURROUND names the W-2 guard explicitly. **The
defect is confined to one cell.** This is not an over-claim about mathematics; it is a profile
attached to something that cannot have one.

**PROPOSED REPAIR, not applied — this pass reports:** either (a) name a specific declaration and
carry its printed profile (`RegisterPentagon.goalState_of_h1_h2` is the natural choice, since the
goal-state is what the row is about), or (b) replace the cell with **"— (namespace; profiles are
per-declaration)"**. **(a) is better** because it keeps a checkable artifact in the row.

---

## §5 — WHERE SITTING 2 LEAVES IT

**Established:** all 90 cited terminals exist at reachable pins · 0 status-vs-docstring
contradictions · 0 definition-encoded-graded-DERIVES · 0 missing terminals · **1 unsourced profile
cell, in 2 papers.**

**Explicitly not established:** the **rounded-profile check across all 90** (needs builds); the
**per-row statement-read** at PATHS (31 rows) and SURROUND (29), which is the substance of the
re-grade and remains ahead.

**Sitting 3:** rebuild the config to take each row's own pin · run `generate` with builds on the two
kernels that have `.lake` (which covers most cited terminals) and report the rest as unexercised ·
begin the statement-read at PATHS and SURROUND.

**Read at the current standard so far: 3 rows CONFIRMED (sitting 1) + 62 rows machine-checked on
four criteria. The statement-read proper — the part no tool does — stands at 3 of 99.**

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `77a86d4` — **unchanged; no paper edited, the defect is reported not repaired** |
| relay | → this report's commit |
| SIDE-kernel `5e668b4` · lv `2f71068` · **rail `de621b1` / `2147a03`** | unmoved |

**Pass 2 stays closed. Nothing deposits.**
