# `W-ATTEMPT-2` — THE CORRESPONDENCE TABLE (CLOSURE-PROTOCOL STEP TWO, DRAFTED)
## ### **EVERY CLAIM OF SITTINGS 1–6 · ITS KERNEL OR BENCH · ITS TERMINAL · ITS AXIOM PROFILE · ITS GRADE — WITH THE NON-CLAIMS AS ROWS, AND NO BLANK CELLS**

**Relay report · 2026-08-18 · drafted at the author's call · ### THIS IS STEP TWO OF THE CLOSURE
PROTOCOL RUN AGAINST THE CONSTRUCTION (never against any sign). ON THE TABLE'S FACE: step three —
EXTERNAL REVIEW BY PEOPLE ABLE TO REJECT — is the AUTHOR'S ACT, not the executor's; step four — the
register — is LAST, and nothing here anticipates it. Nothing deposits.**

*Pointers a stranger can run: every bench row is `cd D:\relay\tools\e16 && python <instrument> register`
(the banked registration) then `... run` (the banked measurement; data files in `D:\relay\data\`).
Every formal row is `cd D:\relay\tools\lean && lean <Module>.lean -o <Module>.olean && LEAN_PATH=.
lean AxiomCheck<Module>.lean` at pinned toolchain `v4.29.1` (`D:\elan\toolchains\
leanprover--lean4---v4.29.1\bin\lean.exe`). Non-default-branch disclosure: every row whose run did not
land its registered default branch says so in its status cell; there are three such rows, marked ◆.*

## §1 — THE CLAIMS

| # | claim | kernel / instrument | terminal / bank | axiom profile | grade & status |
|--:|:--|:--|:--|:--|:--|
| 1 | witness data: 2, 3 split non-principal; 6 principal; `[𝔭₂][𝔭₃] = [0]` | `b14_attempt2.py` (in-run asserts) + `GroupRingGlue.lean` `class_relation` | `data/b14_2026-08-18.txt` · axiom check | Lean: no axioms; bench: exact integer asserts | **VERIFIED** (arithmetic witness) |
| 2 | antipode self-duality of every label and coupling | `GroupRingGlue.lean` `star_c2/c3/c5`, `star_coupling` | `AxiomCheckGlue` print-out | **does not depend on any axioms** | **COMPILED** |
| 3 | the coupling `c₂c₃ = 2[0]+[1]+[2]`; `c₅` identity | `GroupRingGlue.lean` `coupling_23`, `coupling_235` | `AxiomCheckGlue` | **no axioms** | **COMPILED** |
| 4 | the `T7` discriminator: coupling character spectrum `(4,1,1)`, unequal, all nonzero | `GroupRingGlue.lean` `spectrum_*` + exact `ℤ[ω]` in `DiagonalSection.lean` `spectrum_411` | both axiom checks | **no axioms** | **COMPILED** (exact, both routes) |
| 5 | the analytic identification: `(4,1,1)` = the norm-6 (and norm-150 at `{∞,2,3,5}`) label-norm coefficients of `Ẑ` — the Euler-exact gluing law | `b14`/`b15` registrations + the label-norm enumeration `label_norm_is_coupling` (Lean, integer shadow) | `data/b14_2026-08-18.txt`, `data/b15_2026-08-18.txt` · axiom check | enumeration: **no axioms**; identification: bench | **BENCH-CERTIFIED; the identification itself QUESTION-GRADE, not a theorem** |
| 6 | τ-Gram radical ZERO at the minimal instance (rank 12/12) | float: `b14`; **exact: `b18_attempt2_s5.py` C4** | `data/b18_2026-08-18.txt` (55/55) | exact rational/cyclotomic (no floats) | **CERTIFIED-EXACT** (float-era → identity) |
| 7 | twisted-Hermitian `G† = G·Π` (the `F² = parity` twist) | float: `b14` (`5.8e−15`); **exact: `b18` C5; cell instance `twisted_hermitian_cell` (Lean)** | `data/b18_2026-08-18.txt` · axiom check | exact; Lean cell: **no axioms** | **CERTIFIED-EXACT** |
| 8 | `H²` = `ℂ[Cl]`: dim 3 = `h`, antipode-invariant dim 2 | `b14` + `det C = 4 ≠ 0` exact (`b18` C6, `C_radical_zero` Lean) | `data/b14_2026-08-18.txt` · axiom check | class factor: **no axioms** | **BENCH + EXACT CLASS FACTOR** |
| 9 | the six local model laws incl. `Son = V₁⊗W₁` (`S = P₁⊗Q₁`), dims `(pⁿ−1)²` | `b8`–`b13` (float, 7 cells certified) + exact dims in `b18` C1/C7a | e16 data files 2026-08-17/18 | bench float + exact dims | **BENCH-CERTIFIED; tensor square derived longhand then certified** |
| 10 | `n ≥ 2` live-flow instance: laws re-measured at the glued object, nothing inherited (the range law) | `b15_attempt2_s2.py` | `data/b15_2026-08-18.txt` | bench float | **MEASURED** |
| 11 | `T2`-partial: exact commutation, exact compose-identity, both axes local-multiplicative; `ℂ[Cl]` CUTOFF-SILENT (the class resolution lives on the place axis) | `b16_attempt2_s3.py` | `data/b16_2026-08-18.txt` ◆ *(one unpacking bug patched mid-run; clean re-run banked — disclosed)* | bench float | **MEASURED — `T2` AT THE MODEL ONLY (scope guard held)** |
| 12 | the archimedean axis = the DIAGONAL of the towers; SIDE-window's rungs its staircase | `b16` (cell-by-cell) | `data/b16_2026-08-18.txt` | bench | **MEASURED-AT-CITE-MATCH** |
| 13 | the diagonal `D(a)` defined (staircase `n_p(a)`); the coupling cutoff-silent so the section keeps the class structure | `b17_attempt2_s4.py` registration | `data/b17_registration_2026-08-18.txt` | definition + bench | **DEFINED-THEN-MEASURED** |
| 14 | `D-YES` on the finite side: T-invariance at every diagonal cell, both place sets | float: `b17`; **exact: `b18` C2/C7c (`FK = KM`, `M² = Π`)** | `data/b17_2026-08-18.txt`, `data/b18_2026-08-18.txt` | exact at the three cells; float at the rest | **CERTIFIED-EXACT at the measured cells; scope: the model, finite place sets** |
| 15 | the punctuated-weight law: the section's weight dies at each place-arrival; `Q(2,3)·Q(3,2) = 6√6` exact | `b17` + the exact factor law `Q(p,n) = √p(p^(n−1)−1)` (banked, longhand) | `data/b17_2026-08-18.txt` | bench + exact closed form | **MEASURED, closed form exact** |
| 16 | the trace observation: `(4,1,1)` = class-character TRACE of `Ẑ`'s label-norm coefficient (the τ-route) | `trace_identity` (Lean: `tr C = 6 = χ₀+χ₁+χ₂`) + `b18` C6d | axiom check · `data/b18_2026-08-18.txt` | trace identity: **no axioms** | **IDENTITY COMPILED; the OBSERVATION stays QUESTION-GRADE** |
| 17 | sitting 5: the section's full exact certificate (C1–C8), 55/55 | `b18_attempt2_s5.py` | `data/b18_registration_2026-08-18.txt` + `data/b18_2026-08-18.txt` | exact rational/cyclotomic | **CERTIFIED-EXACT, 55/55; reproduced by the executor end-to-end** |
| 18 | sitting 5: the decide-reachable formal content (16 terminals) | `DiagonalSection.lean` | `AxiomCheckDiagonalSection` print-out | **16/16 "does not depend on any axioms"** ◆ *(first compile pulled `propext` via fallback-pattern matches; rewritten match-free — disclosed)* | **COMPILED at pinned `v4.29.1`** |
| 19 | sitting 6: the archimedean factor modeled — invariance structural at machine, radical zero at full rank, parity-twist at machine, raw Hermitian residual large (the twist does real work) | `b19_attempt2_s6.py` | `data/b19_registration_2026-08-18.txt` + `data/b19_2026-08-18.txt` ◆ *(the registered `Q`-stability clause did NOT land — the weight channel is truncation-dominated; disclosed in its row below)* | bench float | **MEASURED — `ext-partial`, the registered prediction** |
| 20 | sitting 6: the hard two-sided window `[λ, Λ]` holds NO Sonin vector at any `a ≤ 2`, and its transient vectors at `a = 3` DIE UNDER REFINEMENT (`19 → 14 → 9` as `N` doubles) — the uncertainty principle's address at the real place, with a measured decay | `b19` (W2 columns) | `data/b19_2026-08-18.txt` | bench float | **MEASURED; the continuum statement AT CITE (Paley–Wiener/uncertainty); the registered death-under-refinement clause CONFIRMED** |
| 21 | sitting 6: the archimedean weight channel `Q_∞` is ALIVE at every `a` but TRUNCATION-DOMINATED in raw form (`~N^(3/2)`; equal-dim rows exactly equal, so at fixed `N` it is a pure function of the ball's grid occupancy — the model's own staircase) | `b19` (M4 column) | `data/b19_2026-08-18.txt` | bench float | **MEASURED — MODEL-ARTIFACT NAMED; a refined statistic is future work, not run** |
| 22 | the Mathlib companion for the cyclotomic tower (`ℚ(ζ₉)`, `ℚ(ζ₁₆)`, glued `ℚ(ζ₁₄₄)`) | named in `DiagonalSection.lean` head + `b18` docstring | the module's face | n/a | **NAMED, NOT BUILT — not faked** |

## §2 — THE NON-CLAIMS, AS ROWS *(each with the place it is refused in writing)*

| # | non-claim | where the refusal is written | status |
|--:|:--|:--|:--|
| N1 | **NO sentence about the sign of `W_∞ − ΣW_𝔭`** — not measured, not implied, not derivable from any row above | every registration's head; the corrected stop (sitting 3, verbatim); this table's face | **REFUSED IN WRITING, EVERYWHERE** |
| N2 | **NO complete roster**: every object is a finite place set at a finite cutoff; the complete roster is the DOUBLE LIMIT and stays open whatever the model shows | `b14` checkpoint 3 (the overclaim pre-refused); restated at every sitting | **OPEN, SAID PLAINLY** |
| N3 | **`T2` at the model only** — whether the class-relations coupling is THE support↔place coupling is not settleable at the model | sitting 3's scope guard; `b16` registration | **OPEN** |
| N4 | **inertia is model data, never `h2`** — `(d/4, d/4, d/2)` is the parity-twist's signature on a finite constructed object | `b14`/`b15` guards; `b18` C8 (carried, not re-derived) | **DATA ROW ONLY** |
| N5 | **the analytic identifications are question-grade** — the coupling-as-label-norm-coefficients and the trace observation are bench-certified matches, not theorems | rows 5 and 16 above, on their face | **QUESTION GRADE** |
| N6 | **the archimedean factor's model is a MODEL** — the centered-DFT grid with declared truncation artifacts; nothing at `∞` is exact in this attempt | `b19` registration | **DECLARED** |
| N7 | **no register movement** — the register sentence is untouched by sittings 1–6 in their entirety | every report's foot | **UNTOUCHED** |

## §3 — THE PROTOCOL'S REMAINING STEPS, ON THE FACE

> ### **STEP THREE — EXTERNAL REVIEW, BY PEOPLE OUTSIDE THIS PROGRAMME WITH THE ABILITY TO REJECT — IS
> THE AUTHOR'S ACT.** *A programme cannot referee itself, and this one has been wrong before and
> recorded it (twenty-five corrections).* ### **STEP FOUR — THE REGISTER — IS LAST, NEVER IN
> ANTICIPATION.** *This table is step two run against the CONSTRUCTION; there is no sign step, and
> "PRICE: NOT APPLICABLE" remains the correct output for step one against a sign.*

**`h2` UNCHANGED. THE REGISTER SENTENCE UNTOUCHED. NOTHING DEPOSITS.**
