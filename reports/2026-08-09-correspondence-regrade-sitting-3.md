# THE WAVE-WIDE CORRESPONDENCE RE-GRADE — SITTING 3 — 2026-08-09

**One repair landed, one repair STOPPED at the rail guard, two flags closed by running them, and a
third tooling artifact caught before it was reported.** Rail at `de621b1` / `2147a03`, **unmoved**.
**Nothing deposits.**

---

## §0 — THE RAIL GUARD FIRES, AND IT FIRES ON THE OTHER FILE

**The ferry's closing names PATHS and SURROUND as the rail-touch risk and says "non-rail keystones
land normally". By the actual layout that is inverted.** The rail is two repos, and I read them:

```
PLACE-phase1.5 @ de621b1 — 8 tracked .md, including keystones/SIMPLICITY_OF_RIEMANN_ZEROS.md
                                            and keystones/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md
PLACE-phase2   @ 2147a03 — 9 tracked .md
```

| file | in the rail? |
|:--|:--|
| `PATHS_TO_THE_CRITICAL_LINE.md` | **no** |
| `THE_UNCONDITIONAL_SURROUND.md` | **no** |
| **`SIMPLICITY_OF_RIEMANN_ZEROS.md`** | **YES** — `PLACE-phase1.5/keystones/` |
| **`FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md`** | **YES** |

**I applied the RULE to the ACTUAL rail files rather than enacting the example.** The rule —
*"STOP and report before landing any rail-file edit"* — is what governs; the list of which files
those are is a fact on disk.

> **CONSEQUENCE: item 2's repair to `SIMPLICITY_OF_RIEMANN_ZEROS.md` IS NOT LANDED. It is prepared,
> verified and reported below, awaiting authorization.** The SURROUND half landed, because SURROUND
> is not a rail file. **The rail repos were not touched and both remain at their pins with clean
> working trees.**

---

## §1 — THE STRUCTURAL FIX, AND A THIRD ARTIFACT CAUGHT IN THE ACT

The fix was built as instructed: **pin read from the row.** Re-run, it produced **12 STALE-PIN
flags** — ten in SURROUND, two in PATHS.

**I checked one by hand before reporting any, and all twelve were artifacts.** SURROUND's ten all
cited `691295b`, a **SIDE-kernel** commit, against terminals in SIDE-grh-transfer, SIDE-archimedean,
SIDE-frobenius, SIDE-spinor and SIDE-rcurve. The reason is structural and worth recording:

> **The corpus does not carry per-repo pins in the rows. It carries them in a per-paper AUDIT
> FOOTER** — *"Kernels audited at: SIDE-kernel `ce5d7bd` …; SIDE-archimedean `8019d9d`,
> SIDE-frobenius `2efe9f2`, SIDE-rcurve `d5f33b4`, SIDE-spinor `b235bc6` (all v0.1.0)."*

Verified directly: `SIDEArchimedean.archimedean_forces_half` **is present** at the footer pin
`8019d9d`. The differ had paired one repo's pin with another repo's terminal.

**Third fix, and the one that holds: resolve each terminal against ITS OWN repo's pin — footer
first, in-row second, HEAD last.**

| | sitting 2 | sitting 3, first cut | **sitting 3, correct** |
|:--|--:|--:|--:|
| terminals checked | 62 | 83 | **130** |
| present at a pin the paper offers | — | 71 | **130** |
| **STALE-PIN** | 60 | 12 | **0** |

> **EVERY TERMINAL CITED IN EVERY CORRESPONDENCE TABLE IS PRESENT AT A PIN ITS OWN PAPER OFFERS.**
> The three earlier results — 3 missing, 60 stale, 12 stale — were **all** my tooling. Seventy-five
> apparent findings, zero real. **The third arrived after the second was fixed**, which is why the
> loom line below is a class and not an anecdote.

---

## §2 — ITEM 3: THE BRANCH BUILD RAN, AND IT REFUTES MY OWN SUSPICION

`lake build Kernel.DerivativeEngine` at `SIDE-kernel` branch `derivative-engine` = **`27a3ae7`**
(796 jobs, 355 s), then `#print axioms` **as run at that pin**:

```
'SIDEDerivative.exactly_c1_derives'                  does not depend on any axioms
'SIDEDerivative.onLine_doubleZero_iff_imDeriv_zero'  depends on axioms: [propext, Classical.choice, Quot.sound]
'SIDEDerivative.no_onLine_double_iff_transversal'    depends on axioms: [propext, Classical.choice, Quot.sound]
```

**Sitting 2 flagged these as probably over-declared — two-line constructive proofs carrying a
three-axiom profile. Measured, the rows are exactly right.** `exactly_c1_derives` is axiom-free as
claimed; the other two carry precisely the declared triple (`Complex.ext` reaches `Classical.choice`
through Mathlib).

> **All three flags CLOSE as checked-and-confirmed. My suspicion was wrong and the rows were right —
> which is the outcome a real check is supposed to be able to produce.**

**A note the ferry's own rule earned:** the first `lake env lean` returned **exit code 0** while its
*content* was `error: object file … does not exist`. Verifying content rather than exit codes is
what caught it.

**Kernel restored to `main` @ `5e668b4`, clean. lv restored to `2f71068`, clean. Probe files deleted.**

---

## §3 — ITEM 2: THE REGISTERPENTAGON REPAIR

Printed at the row's own pin `2d86182` (2990-job build, 407 s):

```
'SIDELvConservation.RegisterPentagon.goalState_of_h1_h2' depends on axioms: [propext, Classical.choice, Quot.sound]
'SIDELvConservation.RegisterPentagon.R5_input_at_Phi'    depends on axioms: [propext, Classical.choice, Quot.sound]
```

**The profile STRING the namespace cell carried was correct; its SOURCING was invalid.** The repair
therefore changes what the cell points at, not what it says.

**LANDED — `THE_UNCONDITIONAL_SURROUND.md` (not a rail file):**

| | |
|:--|:--|
| terminal cell was | `SIDELvConservation.RegisterPentagon` |
| terminal cell now | `SIDELvConservation.RegisterPentagon.goalState_of_h1_h2` (the goal-state theorem inside the pentagon namespace) |
| profile cell now | `{propext, Classical.choice, Quot.sound}` — **printed at `2d86182` by `#print axioms`, 2026-08-09** |
| grade cell | **unchanged, word for word** — *Structure compiled — five faces R1..R5 + goal-state + graded edges; the cross-register equivalences are **not** claimed (W-2 guard), and the R3 totality-through-places edge (= `covers_all`) is **NOT-COMPILED** (the open edge)* |

**PREPARED AND STOPPED — `SIMPLICITY_OF_RIEMANN_ZEROS.md` (rail file, `PLACE-phase1.5/keystones/`).**
The identical two-cell change, with the same printed profile, awaits authorization. **Its grade text
would likewise not move.**

---

## §4 — ITEM 4(i): THE SPECTRAL_CANNON LABEL, CHECKED EVERYWHERE IT IS CITED

Every row citing `SpectralCannonFull.spectral_cannon` across all four papers that cite it:

| paper | rows | retired label present? |
|:--|--:|:--|
| PATHS | 1 | **no** — the row states *"label correction only (enacted 2026-07-21): content is derivative-imaginary on the line (perpendicular crossing)"* |
| SIMPLICITY | 2 | **no** — *"perpendicular crossing: Re ξ′(1/2+it) = 0"* and *"derivative-imaginary on the line"* |
| SURROUND | 0 | — |
| INDEX_ARITY | 0 | — |

> **ZERO rows carry the retired "every zero lies on the critical line" label. The 2026-07-21
> correction has fully propagated to the rows. Flag closes; no delta.**

---

## §5 — THE DELTA TABLE

| outcome | count | detail |
|:--|--:|:--|
| **CONFIRMED at grade** | **3** | the SIDEDerivative trio — statement-read in sitting 1, **profiles now printed at pin** |
| **CONFIRMED, label** | **3** | all `spectral_cannon` rows carry the corrected label |
| **REPAIRED (landed)** | **1** | SURROUND's RegisterPentagon row — unsourced-profile cell → named declaration + printed profile; grade unchanged |
| **REPAIRED (STOPPED at rail guard)** | **1** | SIMPLICITY's identical row — prepared, verified, **not landed** |
| **STRUCK** | **0** | |
| **BLOCKED** | **0** | the two builds this sitting were the blockers, and both ran |
| **machine-checked, pin-correct** | **130** | present at a paper-offered pin; 0 stale, 0 missing |

**Statement-read proper (the part no tool does): 3 rows in sitting 1 + 3 label-checked here = 6 of
99. Ninety-three rows remain unread at the current standard.** PATHS (31) and SURROUND (29) are the
bulk and are **not** claimed as read — this sitting checked one pre-flagged property across them,
which is not the same as reading them.

**No downgrade occurred, so no work-order-with-trigger is owed.** The one defect found (sitting 2's
unsourced profile) produced a repair, half landed and half stopped — not a label.

---

## §6 — THE TWO LOOM LINES FILED

**THE IMPOSED-PRESENT ERROR CLASS** — tooling that resolves against HEAD, a working tree, or a pin
borrowed from the wrong repo, where the corpus records a pinned past. Three instances, three
sittings, 75 false findings. **Structural fix: resolve against the terminal's own repo pin as the
paper states it. Recognition rule: WHEN A TOOL REPORTS THE CORPUS IS WRONG IN BULK, THE TOOL IS THE
SUSPECT — verify one flag by hand at source before reporting any.**

**DATA BANKS ARE GITIGNORED AT CREATION, NOT AT COLLISION** — the 204 MB sweep, the rejected push,
the history rewrite, and the bank that was one `git gc` from gone. **The prevention costs one line;
the cure cost a rewrite and a near-loss.**

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | → this pass's commit (SURROUND + VERIFICATION_LOOM only) |
| relay | → this report's commit |
| SIDE-kernel `5e668b4` (main, restored) · lv `2f71068` (restored) | clean |
| **rail `de621b1` / `2147a03`** | **UNMOVED, both clean — no rail file edited** |

**Pass 2 stays closed. Nothing deposits.**
