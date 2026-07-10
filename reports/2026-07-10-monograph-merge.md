# 2026-07-10 — monograph merge + One Premise insertion

Session-relay report. Reports only, no research content.

## Task 1 — closing landing (D:\MY-DOwnloads\PLACE-papers)

Outcome: **applied cleanly** (not gated, not already-applied).

- Script: `D:\MY-DOwnloads\closing-landing-apply\Apply-ClosingLanding.ps1`
- Gate output: `Gates passed: verdict landing present, closing landing not yet applied.`
- Fragments appended to `FINDINGS.md`, `OPEN_TRAILS.md`, `SPIRAL_MAP.md`, `REGISTRY.md`
- Commit: `3eaacf4` — "Closing landing 2026-07-09: T3-pair compiled; O.13 closed; the one premise specified by the compiler"
- Push: `ce1cbcb..3eaacf4  main -> main`

## Task 2 (Steps A/B/C) — monograph sync + One Premise insert

### Step A — canonical file verification (all pass)

| Check | Result |
|---|---|
| Newest match | `D:\MY-DOwnloads\A_Place_to_Stand_v5_4_CANONICAL.md` (single copy) |
| md5 | `c8ec9b46c6afdcb7e6d227191e392a40` ✓ |
| Line count | `2064` ✓ |
| Line 9 | `**v5.4, May 2026**` ✓ |

### Step A — diff --stat (repo v5.3 → canonical v5.4)

```
1 file changed, 13 insertions(+), 75 deletions(-)
```

Two-line summary:
1. Header/footer bump (April → May, v5.3 → v5.4), §25.5 kernel counts rewritten for v1.1 (adds `CartanBBridge`, DOI references, Mathlib-API notes), 13 U+0304 conjugate glyphs reverted to bare `ξ(s)̄` form.
2. Three large removals: `## How This Monograph Is Organized`, `§25.5a The Completable-Path Matrix`, `§25.8 Kernel Concordance`; also removes the `CrossClassExclusion.lean` row and rewrites §25.2 back to `native_decide`.

### Step A — sanity gate

**Fired first pass.** Repo v5.3 contained four commits (`e307749`, `55c9974`, `6c28469` on 2026-06-11; `dbf01c3` on 2026-05-19) postdating v5.4 and load-bearing. Halted and reported inline; user confirmed the two lines are divergent (not a fast-forward) and directed a three-way merge:

- Canonical v5.4 as base.
- Port §25.8 Kernel Concordance (whole section).
- Port §25.2 `native_decide` → `decide` (with axiom-free note).
- Port Route 2 rename to `SpectralCannonFull.lean` (transitively inside §25.8).
- Port U+0304 mojibake fix (8 lines, each `ξ(...)̄` broken form → `$\overline{...}$`).
- Header stays at `v5.4, May 2026` pending v5.5 pass completion.

### Step B — merge verification (all six checks pass)

| Check | Result |
|---|---|
| (a) §25.8 heading | line 1616: `## 25.8 Kernel Concordance` |
| (b) `decide` policy | line 1519: `**The Formation Count.** \`decide\` verifies 2 + 3 + 2 + 0 = 7 (the canonical \`SIDEKernel.formation\`, axiom-free)` |
| (c) SpectralCannonFull | 2 references (§25.8 row + housing paragraph) |
| (d) mojibake residue | 0 broken `ξ(...)̄` forms remain |
| (e) header v5.4 | line 9: `**v5.4, May 2026**` |
| (f) v5.4-only content survived | line 107 DOI 10.5281/zenodo.19937590; line 1497 `CartanBBridge` block preserved |

### Step B — merge commit

- SHA: `668d22e`
- Message: `merge: monograph reconciled — deposited v5.4 line + four June repo fixes (25.8 concordance, decide policy, SpectralCannonFull, mojibake); header stays v5.4 pending v5.5 pass`
- diff --stat: `1 file changed, 4 insertions(+), 47 deletions(-)`
- Push: `3eaacf4..668d22e  main -> main`

### Step C — One Premise section insertion

**Section number assigned:** **§27.3 The One Premise** — placed as a new subsection of Chapter 27 ("The Research Path"), between §27.2 ("What the Programme Produced") and the chapter's closing `---`. Rationale: Chapter 27 is Part VI's correction-record chapter (its §27.1 "The Research Arc" contains the 24-item correction narrative and its §27.2 lists what the programme produced); §27.3 concludes the chapter by counting the one premise that remains. Heading level `##` matches the sibling convention of Part VI subsections (`## 25.1`, `## 26.1`, etc.). Draft's header block (Target placement / Status), cross-reference list, and italic provenance footer all omitted. Body inserted verbatim.

**Four cross-reference locations (chapter-level):**

| # | Chapter / section | Line | Sentence appended |
|---|---|---|---|
| 1 | Chapter 19, §19.1 step (9) — SIDE syllogism / combination argument | 1140 | "The combination argument of this step is examined at kernel level, and its exact remaining content stated, in §27.3." |
| 2 | Chapter 25, §25.7 — `ConservationHypothesis` paragraph | 1612 | "The formalization of this interface, and the theorem-pair that brackets its remaining content, are presented in §27.3; kernel: SIDE-lv-conservation." |
| 3 | Chapter 14 — universality-hypothesis paragraph (Silence Principle / `silence_universal`) | 797 | "This hypothesis is one of four names of a single premise; see §27.3." |
| 4 | Chapter 26, §26.1 — 18 → 12 → 5 → 1 → 0 axiom-journey narrative | 1652 | "The method's continuation past the Day-1 kernel — aimed at the Route 3 interface — is reported in §27.3: two targets closed, the third pinned to a goal state and bracketed by a theorem-pair." |

Cross-reference #5 (Zenodo description) skipped per instructions.

### Step C — verification (all four pass)

| Check | Result |
|---|---|
| Section present exactly once | `grep -c '^## 27.3 The One Premise$'` → **1** |
| Four cross-refs present | All four unique sentences located at the expected line numbers |
| "Target placement" / "Cross-reference insertions" absent | `grep -c` → **0** |
| No new "gap" occurrences | Canonical v5.4 had 2 ("mass gap" line 1735, "codimension gap" line 1768); merged file also 2 → **0 new** |

### Step C — commit

- SHA: `c8882f3`
- Message: `v5.5 pass (1/3): insert The One Premise section (Part VI) + four cross-references; written from SIDE-lv-conservation v0.2.0 verdict (F.2026-07-09-m/-n). No mathematical changes; version header unchanged pending pass completion.`
- diff --stat: `1 file changed, 29 insertions(+), 4 deletions(-)`
- Push: `668d22e..c8882f3  main -> main`

## Commit SHAs (in order)

| Task | SHA | Message summary |
|---|---|---|
| 1 (closing landing) | `3eaacf4` | Closing landing 2026-07-09: T3-pair compiled; O.13 closed |
| 2 Step B (merge) | `668d22e` | merge: monograph reconciled — deposited v5.4 + four June repo fixes |
| 2 Step C (One Premise) | `c8882f3` | v5.5 pass (1/3): insert The One Premise section + four cross-references |

## Warnings

- CRLF warnings emitted by git during each `add` (`warning: in the working copy of '…', LF will be replaced by CRLF the next time Git touches it`). Cosmetic — repo carries a mixed-EOL history and this is Windows.
- Version header remains **v5.4, May 2026**. Bump to v5.5 deferred to end of pass (edits 2/3 and 3/3 still pending), per task spec.
- One outstanding discrepancy from the sanity-gate reconciliation, resolved but noteworthy: Chapter 15's §25.5a "Completable-Path Matrix" and the `CrossClassExclusion.lean` bridge-table row are absent from the deposited v5.4 line (deliberate deposit-side removals) and were **not** re-added during the merge, since they were part of v5.4's own edit round and the merge policy was "deposit as base + four postdating fixes only." If the deposit removals were unintentional, that content is available in repo history at `ca7178b` and will need a separate port.

::relay end::

---

## Addendum — 2026-07-10 (reconciliation landing appended to ledgers)

Ledger fragments appended to `D:\MY-DOwnloads\PLACE-papers\{FINDINGS.md, REGISTRY.md}` in the same append-only style as the landing scripts (UTF-8 no BOM, via `[System.IO.File]::AppendAllText` with `UTF8Encoding($false)`; no existing content modified). Existing tail-lines of both ledgers were verified pre-append and confirmed intact post-append.

- `FINDINGS.md`: new entry `### F.2026-07-10-a — Monograph line divergence discovered and reconciled` — one compact paragraph, records the v5.3/v5.4 divergence, the three-way merge at `668d22e`, the §27.3 insertion at `c8882f3`, and the flag on the deposit-side removals (recoverable at `ca7178b`). Ends with the lesson: repo is canonical for text, deposits are snapshots. Epistemic: ◆ for the reconciliation; ⋄ for the flagged removals pending author verdict.
- `REGISTRY.md`: new `## Version-log addition — 2026-07-10 (reconciliation landing; fold into VERSION LOG table at next hand edit)` block with a single `| 2026-07-10 | … |` row summarising the same, cross-referencing `F.2026-07-10-a`.

Commit and push:

- Commit SHA: **`c5adc14`**
- Message: `Reconciliation landing 2026-07-10: monograph divergence discovered, merged (668d22e), One Premise inserted (c8882f3); deposit-side removals flagged for author confirmation`
- diff --stat: `2 files changed, 7 insertions(+)`
- Push: `c8882f3..c5adc14  main -> main`

::relay addendum end::

---

## Addendum 2 — 2026-07-10 (§27.3 editorial trim)

Surgical three-edit trim to §27.3 to remove internal work-tracking vocabulary from the published section.

**Edits applied (only these three):**

1. Sentence ending "stated at T1's witness; its formalization is the named successor target (T4)." → ends at "stated at T1's witness." (deleted from the semicolon through "(T4)").
2. "one named discharge path within the programme (T4) and three classical faces outside it" → "a discharge path within the programme — the per-class constraints instantiated at the fixed witness — and three classical faces outside it".
3. In the Chapter 26 §26.1 cross-reference sentence: "two targets closed, the third pinned" → "two statements closed, the third pinned".

**Verification grep — §27.3 and all four cross-reference sentences:**

| String | §27.3 | Ch. 14 xref (line 797) | Ch. 19 xref (line 1140) | §25.7 xref (line 1612) | §26.1 xref (line 1652) |
|---|---|---|---|---|---|
| `T4` | 0 | 0 | 0 | 0 | 0 |
| `successor` | 0 | 0 | 0 | 0 | 0 |
| `target` | 0 | 0 | 0 | 0 | 0 |
| `work order` | 0 | 0 | 0 | 0 | 0 |
| `trail` | 0 | 0 | 0 | 0 | 0 |
| `scheduled` | 0 | 0 | 0 | 0 | 0 |
| `FINDINGS` | 0 | 0 | 0 | 0 | 0 |
| `F.2026` | 0 | 0 | 0 | 0 | 0 |

All 40 cells zero. Trim complete.

**Other tracker-adjacent vocabulary in §27.3 (noted, not changed):**

- `verdict` (1 occurrence): "Both directions are compiler verdicts." Naming what the compiler ruled — technical use, but adjacent to programme-ledger vocabulary. Worth author's eye for the v5.5 pass 2/3 or 3/3.
- `bench` (1): "The Li channel bench has, additionally, *measured* the premise to n = 60." Programme jargon for the Li computational apparatus. Slightly tracker-flavored; could be rephrased as "the Li channel computation" or similar without loss.
- `instrument` (2): "The measurements are an instrument, not an argument." and "produced by the discipline's hardest instrument, the compiler". Metaphor for measuring apparatus, reads clean.
- `T1`, `T2`, `T3′`, `T3″`: theorem labels used in prose. These are mathematical labels for the four compiled theorems of SIDE-lv-conservation, not work-tracking labels. Reads clean but reader-facing; could be replaced with descriptive names ("the Mellin factorization theorem", "the shared-witness bridge", "the countermodel") in a later pass if a general reader is the target.

**Commit and push:**

- Commit SHA: **`da36b20`**
- Message: `v5.5 pass (1/3, trim): remove internal work-tracking vocabulary from §27.3 — the section states what remains mathematically, not the programme's task labels. Editorial only.`
- diff --stat: `1 file changed, 3 insertions(+), 3 deletions(-)`
- Push: `c5adc14..da36b20  main -> main`

::relay addendum 2 end::

---

## Addendum 3 — 2026-07-10 (v5.5 pass 2/3: C-index harmonization)

Zero mathematical changes. Labels harmonized to a single canonical assignment; semantic names carried at every use.

### Canonical authority

Checked `D:\SIDE-kernel\Bridge\TheBridgeComplete.lean` lines 19–22:

```
inductive MechanismClass where
  | C1_schwarz | C2_euler | C3_functional_eq
  | C4_modular | C5_spectral | C6_cauchy_riemann | C7_hadamard
```

The kernel has an explicit fixed order in its Lean source, so per the task rule "text follows kernel, not vice versa" that assignment is canonical. The monograph's §15.2 table would have been the fallback authority; it was inconsistent with the kernel and had to be rewritten. **Authority used: kernel (`TheBridgeComplete.lean:19-22`).**

### Canonical assignment

| Index | Semantic name | Stage |
|---|---|---|
| C₁ | Schwarz reflection / real coefficients | Primitive |
| C₂ | Euler / multiplicative (product balance) | Primitive |
| C₃ | Functional equation | Transformation |
| C₄ | Modular / PSL₂ symmetry | Transformation |
| C₅ | Spectral self-adjointness | Transformation |
| C₆ | Cauchy-Riemann | Output |
| C₇ | Hadamard product | Output |

### Step 1 — Inventory before touching anything

90 C-index occurrences across the monograph. Three distinct assignments were interleaved: the kernel-canonical order (call it **B**), a rotated order used in §15.2's table and derivative sections (call it **A**), and one section (§15.1 stage diagram + §29 late passages) that already matched the kernel. The three known conflict sites were spread as follows:

**Sites already canonical (Assignment B) before this pass — 34 occurrences:**

| Location | Lines | Nature |
|---|---|---|
| §15.1 stage diagram (code fence) | 838, 841, 844 | Stage table |
| §15.5 line 937 | 937 | "local analyticity (C₆)" |
| §19.2 line 1164 | 1164 | Transformation-stage triple (C₃, C₄, C₅) |
| §25.2 Voice/C table | 1511–1517 | 7 rows |
| §25.5 produces_offline table | 1574–1580 | 7 rows |
| §29 output-independence passage | 1809, 1811, 1812, 1816, 1818 | multiple refs to (C₆, C₇) + (C₁ Schwarz, C₂ Euler) |

**Sites in Assignment A (needed re-mapping) — 56 occurrences:**

| Location | Lines | Old (A) → new (B) mapping |
|---|---|---|
| §15.1 prose line 816 | 816 | `C₁` (archimedean/FE) → **C₃**; `C₂` (unique fact./Euler) → **C₂** (unchanged) |
| §15.1 Stage 2 list | 819–821 | C₁→C₃, C₅→C₄, C₆→C₅ |
| §15.1 Stage 3 list | 826–827 | C₃→C₆, C₇→C₇ (unchanged) |
| §15.2 table | 857–863 | 6 rows renumbered (C₇ unchanged) |
| §15.3 per-class analysis | 871–895 | 7 blocks reordered (C₁ FE → C₃; C₂ Real → C₁; C₃ CR → C₆; C₄ Euler → C₂; C₅ PSL₂ → C₄; C₆ Spectral → C₅; C₇ Hadamard unchanged) |
| §15.3 intra-section forward-ref line 881 | 881 | `see C₆ below` → `see C₅ below` |
| §15.3 "Could C_ produce" lines | 883, 891 | `Could C₅ (Modular) produce` → `Could C₄ produce`; `Could C₆ (Spectral) produce` → `Could C₅ produce` |
| §15.3 line 899 "Why both constraints" | 899 | `(C₁)` (FE) → **(C₃, functional equation)**; `(C₄)` (Euler) → **(C₂, Euler product)** |
| §15.3 summary table | 905–911 | 6 rows renumbered |
| §15.6 eleven-programme table | 951–961 | 11 rows, all reassignments completed |
| §16.6 five-paths table | 1030–1034 | 5 rows renumbered |
| §17 Epstein prose | 1065, 1067 | Euler `C₄` → **C₂** (three occurrences); FE `C₁` → **C₃** |
| §18 codimension | 1093 | FE `C₁` → **C₃** |
| §19.2 Epstein paragraph | 1166 | Euler `C₄` → **C₂** (four occurrences on same line) |
| §19.4 One Voice Suffices | 1186 | Euler `C₄` → **C₂** |
| §22.5 R-curve derivative bullets | 1359–1365 | 7 bullets renumbered |
| Line 1426 output-stage-classes ref | 1426 | `C₃` (CR) → **C₆**; C₇ unchanged |
| §29 Epstein experiment ref | 1814 | FE `C₁` → **C₃**; Euler `C₄` → **C₂** |
| §29 archimedean-as-transformation ref | 1820 | `C₁` (archimedean/FE) → **C₃** |

**Semantic-ambiguous / range-references (no edit needed) — no ambiguous cases:**

| Location | Lines | Nature |
|---|---|---|
| Generic range `C₁–C₇` or `C₁,...,Cₙ` | 103, 597, 963, 1155 | 4 occurrences of the ordered-range shorthand — no specific-index claim |

No occurrence was flagged as semantically ambiguous. Every non-range C-index reference had a clear semantic anchor in the surrounding text.

### Step 3 — Semantic-name coverage

Every C-index reference now appears with its semantic name on first use in each section (e.g. `C₄ (Modular/PSL₂)` in §15.1 line 820, `C₃ (FE)` in §15.6 table, `C₂ (Euler/multiplicative)` in §17 line 1065). Bare references (`C₁`, `C₂` etc.) survive only inside tables that already gave the semantic name in the class column, inside compact table rows where the semantic column is adjacent (e.g. `| Voice1 | C₂ | balance_theorem…` in §25.2 Voice/C table, where "balance_theorem" is the semantic anchor), inside inline range shorthand, or in immediately-following sentences within a paragraph that already established the pairing.

Stage diagram (§15.1 code fence, lines 838–844) required no edit — its inline semantic labels `C₁ Schwarz, C₂ Euler; C₃ FE, C₄ PSL₂, C₅ Spectral; C₆ Cauchy-Riemann, C₇ Hadamard` were already canonical.

### Step 4 — Verification

Total occurrence count unchanged: **90 → 90.**

Before/after counts per canonical class, based on paired-with-semantic-name occurrences (`C_N (…semantic…)` form):

| Canonical index | Semantic anchor | Occurrences (paired form) |
|---|---|---|
| C₁ | Schwarz reflection / real coefficients | 6 |
| C₂ | Euler / multiplicative | 8 |
| C₃ | Functional equation | 9 |
| C₄ | Modular / PSL₂ | 8 |
| C₅ | Spectral self-adjointness | 12 |
| C₆ | Cauchy-Riemann | 12 |
| C₇ | Hadamard | (retained across every mapping) |

Stale-A residue check (must all be zero — old Assignment-A phrases that would indicate incomplete migration):

| Search pattern | Result |
|---|---|
| `C₁ (Functional eq)` or `C₁ (functional…` | **0** |
| `C₁ … archimedean … transformation` (as index claim) | **0** |
| `C₂ (Real coefficients)` | **0** |
| `C₃ (Cauchy-Riemann)` | **0** (present only as canonical C₆) |
| `C₄ (Euler…` | **0** |
| `C₅ (PSL₂…` | **0** |
| `C₆ (Spectral…` | **0** (canonical C₆ is Cauchy-Riemann) |
| `C₆ Spectral` (bare) | **0** |

Canonical-B pattern check (should all be > 0):

| Search pattern | Count |
|---|---|
| `C₄ (Modular` or `C₄ Modular` or `C₄ (PSL` | 8 |
| `C₅ (Spectral`, `C₅ Spectral`, `C₅ (spectral` | 12 |

Spot-check on the three previously-known conflict sites:

| Site | Before | After |
|---|---|---|
| §15.1 prose (lines 816–827) | Mixed A/B (C₁ = archimedean/FE in prose; C₁ = Schwarz in the code fence) | All B (C₃ = FE in prose; C₁ = Schwarz in the diagram) — consistent |
| §15.1 stage diagram (lines 838–844) | B (already canonical) | B (unchanged) |
| Chapter 25 produces_offline (lines 1574–1580) | B (already canonical) | B (unchanged) |

All three sites now agree on canonical B.

### Commit and push

- Commit SHA: **`2a69d77`**
- Message: `v5.5 pass (2/3): C-index harmonization — one canonical assignment (authority stated in relay report), semantic names carried at every use. Zero mathematical changes.`
- diff --stat: `1 file changed, 60 insertions(+), 60 deletions(-)`
- Push: `da36b20..2a69d77  main -> main`

::relay addendum 3 end::

---

## Addendum 4 — 2026-07-10 (v5.5 pass 3/3: count purge + micro-items + version bump + pass landing)

Final edit of the v5.5 pass. Zero mathematical changes.

### PART 1 — Count-purge inventory (before)

Bare drifting counts of kernel content in `day1/A_Place_to_Stand.md`:

| Line | Section | Original phrasing (counts in **bold**) |
|---|---|---|
| 107 | On This Work → Formal verification | "…across **83 active Lean files.**" |
| 1497 | §25.5 Current counts (v1.1, May 2026) | "**560+ theorems, lemmas, and definitions** in the sorry-free core (Kernel/ with **409**, Bridge/ with **97** in v1.0 plus CartanBBridge.lean added in v1.1, MetaKernel.lean with **54**), totaling **83 active Lean files.**" |
| 1505 | §25.2 The Product Formula | "**Three files, 33 theorems.**" |
| 1521 | §25.2 The Perpendicular Crossing Probe | "**Three theorems and two lemmas** proving that the derivative…" |
| 1538 | §25.4 The Product Formula Chain | "…from prime powers (**6 theorems**), to general integers (**8 theorems**), to rationals with the conservation certificate (**8 theorems**). Total: **22 theorems**…" |
| 1723 | §27.2 The Lean kernel | "**560 theorems, lemmas, and definitions** in the sorry-free core (Kernel + Bridge + MetaKernel)…" |

No arXiv-abstract counts appear in the file. §25.8 Kernel Concordance uses named theorems with axiom profiles, not raw counts — reviewed and left as-is.

### PART 1 — Count-purge replacements (after)

| Line | Form used | Replacement |
|---|---|---|
| 107 | (a) named-theorem | "The sorry-free core (`Kernel/`, `Bridge/`, `MetaKernel.lean`) carries three independent route terminals — `structural_exhaustiveness_proved` (Route 1), `SpectralCannonFull.spectral_cannon` (Route 2), and `ConservationBridge.riemann_hypothesis` (Route 3) — each depending only on `{propext, Classical.choice, Quot.sound}` (see §25.8 Kernel Concordance)." |
| 1497 | (a) named-theorem, deposit-tagged | Rewritten as "**Deposit (v1.1, May 2026, DOI 10.5281/zenodo.19937590):** the three route terminals … plus the perpendicular-crossing chain (…), the product-formula chain (…), the seven Voice files, and MetaKernel.lean — compile against Mathlib at 0 sorry and 0 custom axioms; see §25.8 Kernel Concordance." The CartanBBridge substance was preserved. |
| 1505 | (a) named-theorem | "Three files — `ProductFormula_Prime.lean`, `ProductFormula_Int.lean`, `ProductFormula_Rat.lean` — proving …" |
| 1521 | (a) named-theorem | "`Kernel/PerpendicularCrossing.lean` proves that the derivative … satisfies … (the differentiated functional equation, `deriv_fe`) and Re(ξ'(1/2 + it)) = 0 for all real t (the spectral cannon `SpectralCannonFull.spectral_cannon` — perpendicular crossing on the critical line)." |
| 1538 | (a) named-theorem, terminal per stage | "…from prime powers (`ProductFormula_Prime.lean`, terminating in `prod_prime_power_absValues`) through general integers (`ProductFormula_Int.lean`, terminating in `prod_int_absValues`) to rationals with the conservation certificate (`ProductFormula_Rat.lean`, terminating in `prod_rat_absValues` and `conservation_certificate`)…" |
| 1723 | (a) named-theorem | "The sorry-free core (`Kernel/`, `Bridge/`, `MetaKernel.lean`) compiles the three route terminals — `structural_exhaustiveness_proved`, `SpectralCannonFull.spectral_cannon`, `ConservationBridge.riemann_hypothesis` — at zero unproved assertions and zero custom axioms; each depends only on `{propext, Classical.choice, Quot.sound}` (§25.8 Kernel Concordance)." |

Form (a) at every site. Form (b) not needed — none of the sites required a magnitude to serve the reader beyond what the named theorems + module citations convey.

### PART 2 — §27.3 micro-edits

- **(2a)** "The Li channel bench has, additionally, *measured* the premise to n = 60" → "The Li channel computation has, additionally, *measured* the premise to n = 60".
- **(2b)** T-labels get descriptive aliases on first mention:
  - `**(T1)** the completed zeta function factors…` → `**the Mellin factorization theorem (T1)** — the completed zeta function factors…`
  - `**(T2)** the two-input exhaustion…` → `**the exhaustion lemmas (T2)** — the two-input exhaustion…`
  - `a concrete two-predicate countermodel is compiled as a theorem (T3″)` → `a concrete two-predicate instance is compiled as a theorem — the countermodel (T3″)`
  - `the bridge closes by exhibiting that shared witness (T3′), in one line` → `the bridge closes by exhibiting that shared witness — the shared-witness bridge (T3′), in one line`
- **(2c)** Whole-file "gap" audit:
  - Line 1779 "mass gap" (Yang-Mills, Clay problem) — EXCEPTED, left as-is.
  - Line 1812 "no codimension gap between on-line and off-line" — replaced with "no codimension margin between on-line and off-line".
  - No verbatim bibliography title contained "gap"; no other unexcepted "gap" remained.

### PART 3 — Version bump

- Line 9 header: `**v5.4, May 2026**` → `**v5.5, July 2026**`.
- Footer (near line 2057): `*v5.4, May 2026*` → `*v5.5, July 2026*`, plus a provenance sentence appended directly below the footer version line: *"v5.5 (July 2026): adds §27.3 The One Premise; harmonizes mechanism-class indices to the kernel enumeration (TheBridgeComplete.lean); replaces kernel counts with named theorems. No mathematical changes from v5.4."* Placed adjacent to the footer version line rather than in an "On This Work" version-history section, which the file does not carry.

### PART 4 — Whole-file pass-completion verification

| Check | Result |
|---|---|
| (i) §27.3 present exactly once | `grep -c '^## 27.3 The One Premise$'` → **1** |
| (i) four cross-refs intact | 1 + 1 + 1 + 1 = **4** (Ch. 14, Ch. 19 step (9), §25.7, §26.1) |
| (ii) C-index canonical: C₁ paired with Schwarz/real coefficients | ✓ (lines 857, 871, 905, 1030, 1359, 1818) |
| (ii) C-index canonical: C₃ paired with FE | ✓ (lines 816, 819, 859, 875, 907, 951–961, 1030, 1067, 1093, 1361, 1814, 1820) |
| (ii) C-index canonical: C₆ paired with CR | ✓ (lines 826, 862, 893, 910, 951–953, 1034, 1364, 1426, 1811, 1816) |
| (iii) unexcepted "gap" | **0** (only "mass gap" at line 1779 remains — excepted) |
| (iv) T4 / successor / work order / FINDINGS / F.2026 in body | **0** each |
| (v) bare drifting kernel counts | **0** — all six pre-pass sites now cite named theorems + modules |
| (vi) header + footer v5.5 | header line 9 "**v5.5, July 2026**" ✓; footer "*v5.5, July 2026*" ✓ |

### Commits and pushes (this addendum)

- `day1/A_Place_to_Stand.md` — commit **`e8114be`**, "v5.5 pass (3/3): count purge (named theorems over counts), codimension-margin fix, §27.3 micro-edits, version bump v5.4 → v5.5. Pass complete; no mathematical changes across the pass." — diff `1 file changed, 14 insertions(+), 12 deletions(-)`; push `2a69d77..e8114be  main -> main`.
- PART 5 pass-completion landing (append-only UTF-8 no BOM to ledgers):
  - `FINDINGS.md`: new entry `### F.2026-07-10-b — v5.5 pass complete` (compact paragraph with the three commit SHAs `c8882f3`/`da36b20`, `2a69d77`, `e8114be`; kernel-enumeration authority; count-purge summary; version bump; Zenodo deposit gated on DEPOSIT_VERIFICATION_PROTOCOL).
  - `REGISTRY.md`: new `## Version-log addition — 2026-07-10 (pass-completion landing; fold into VERSION LOG table at next hand edit)` row cross-referencing `F.2026-07-10-b`.
  - Commit **`9da9b47`** — "Pass-completion landing 2026-07-10: v5.5 complete (three edits, SHAs in F.2026-07-10-b)" — diff `2 files changed, 7 insertions(+)`; push `e8114be..9da9b47  main -> main`.

### v5.5 pass summary (three edits total)

| Edit | Commit | Content |
|---|---|---|
| 1/3 | `c8882f3` (+ trim `da36b20`) | §27.3 The One Premise inserted in Part VI with four cross-references |
| 2/3 | `2a69d77` | C-index harmonization to kernel enumeration (`TheBridgeComplete.lean:19-22`) |
| 3/3 | `e8114be` | Count purge, "codimension margin" fix, §27.3 micro-edits, version bump v5.4 → v5.5 |
| landing | `9da9b47` | F.2026-07-10-b + REGISTRY row appended to ledgers |

v5.5 pass complete. **Zenodo deposit of v5.5 is a separate author decision, gated on DEPOSIT_VERIFICATION_PROTOCOL — not landed by this pass.**

::relay addendum 4 end::
