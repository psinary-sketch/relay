# Count-currency pass — deposit-frozen counts vs current state

**Date:** 2026-07-12
**Scope:** every count-claim about the Lean kernel in the PLACE-papers corpus (`grep` over the repo, README, `day1/`), plus the SIDE-kernel repo README.
**Question per site:** what was the count true *of* (which tag/date), what is the current truth, and is the site HISTORICAL (true of its dated referent — leave) or LIVE-STALE (presented as current — fix to named-theorems-over-counts form)?
**Commits:** PLACE-papers `e86799c` (pushed, remote `main` = `e86799c` ✓); SIDE-kernel `7c01c12` (pushed, remote `main` = `7c01c12` ✓).

---

## 1. Current truth (computed, not recalled)

| Fact | Command | Result |
|---|---|---|
| Files, `v1.2` (`b1407b2`) | `git ls-tree -r --name-only v1.2 \| grep '\.lean$'` | `Kernel/` **72** + `Bridge/` **13** + `MetaKernel.lean` **1** = **86**; **128** whole tree (incl. `legacy/` 41 + `lakefile.lean`) |
| Files, `v1.1` (`e0a8ba0`) | same, at `v1.1` | `Kernel/` 70 + `Bridge/` 13 + `MetaKernel.lean` = 84; **83** in `Kernel/`+`Bridge/` — this is the scope the deposit's "83 files" names |
| Files, `v1.0` (`078b3c5`) | same, at `v1.0` | `Kernel/` 69 + `Bridge/` 12 + `MetaKernel.lean` = 82 |
| Declarations, `v1.2` | `git grep -cE '^\s*(theorem\|lemma\|def) ' v1.2 -- Kernel/ Bridge/ MetaKernel.lean` | **575** (`^theorem` alone: 447). At `v1.1`: 589 / 454 |
| Axiom profiles, `v1.2` | verbatim `#print axioms` record, SIDE-kernel `DEPOSIT_v1_2_NOTES.md` (run 2026-07-10) | Route 1 `structural_exhaustiveness_proved`, Route 2 `SpectralCannonFull.spectral_cannon`, Route 3 `ConservationBridge.riemann_hypothesis`, and both `techne_kernel_integration` terminals: exactly `{propext, Classical.choice, Quot.sound}`. `SIDEKernel.formation`, `SIDEKernel.formation_count`, `DomainOstrowski.formation_count`: **axiom-free**. No `sorryAx`, no `Lean.ofReduceBool`, no `_native.*` |
| `native_decide` | `git grep "by native_decide" HEAD -- '*.lean'` | **0 matches** (only a prose comment in `legacy/FmodifProbe.lean:34`) |
| Deposit status | — | Citable kernel deposit is still **v1.1** (DOI 10.5281/zenodo.19937590). **v1.2 is tagged, verified, deposit-ready — NOT deposited.** No fix may imply a v1.2 DOI |

**Three coexisting file-count scopes at v1.1** — 65 (tag annotation), 83 (`Kernel/`+`Bridge/`), 84 (incl. `MetaKernel.lean`), 126 (whole tree). This scope variance is precisely why the corrected form cites *named terminals*, not counts.

**Deposit caveat (F.2026-07-10-c).** At v1.1 as deposited, Route 1 and the formation certificates transitively carried `seven_classes._native.native_decide.ax_1_1`. The deposit's "0 axioms" claim was therefore **not true of its own referent** for those terminals (Routes 2 and 3 and `DomainOstrowski.formation_count` were already clean). v1.2 clears it. Every HISTORICAL site below that says "v1.1 … 0 axioms" inherits this caveat.

---

## 2. Classification table

### LIVE-STALE — fixed

| # | Site | Claim | True of | Current truth | Fix |
|---|---|---|---|---|---|
| 1 | `README.md:7` | "SIDE-kernel (68 files, 0 sorry, 0 axioms)" | Day-1 era (63 core + 5 bridge, Mar–Apr 2026); never true of v1.1 or v1.2 | 86 files at v1.2; axiom profiles as above | Replaced with named terminals + `#print axioms` profiles at `v1.2` (`b1407b2`), citable deposit named as v1.1 |
| 2 | `README.md:12` | "day1/ ← 7 papers + monograph (Zenodo deposit v1.0.2)" | The frozen deposit (monograph v5.4) | `day1/` tree is the **live** line — monograph now v5.6 | Tree line and deposit line separated; new **Deposit note** paragraph states the deposit is frozen at v1.0.2 (DOI 10.5281/zenodo.19938917) and that in-paper counts are historical |
| 3 | `REGISTRY.md:65` | "Live at HEAD `5260498` (verified 2026-06-04): 83 files … ≥358 / 418 theorems" | HEAD `5260498`, 2026-06-04 — a currency-purposed pointer, so staleness is a defect even though it is dated | Tag `v1.2` = `b1407b2` (`main` HEAD `ce5d7bd`) | Refreshed to v1.2: named terminals + axiom profiles first; counts demoted to "for reference only, scope-dependent"; v1.1-deposit caveat recorded |
| 4 | `SPIRAL_MAP.md:27` | "currently carries 83 files … 0 sorry, 0 axioms holds" | HEAD `5260498`, 2026-06-04 | as above | Rewritten as a 2026-07-12 / `v1.2` reconciliation; the **deposit table row (line 25) left frozen** with an explicit caveat on its "0 axioms" |
| 5 | `phase1.5/method/A_METHODOLOGY.md:98` | "*Current federation state:* … 0 sorry, 0 axioms across 83 files" | v1.1 (files), and the axiom half was never true of v1.1 | v1.2 named terminals | Converted to named-terminal form; deposit still cited as v1.1 |
| 6–9 | `phase1.5/proofs/THE_PROOF.md:524`, `IDS_TO_RH.md:296`, `INTEGRATED_PROOF.md:396`, `MECHANISM_EXCLUSION.md:394` | "The kernel contains 360 theorems across 68 files with 0 `sorry` and 0 custom axioms" (present tense, untagged) | Day-1 era; stale even against v1.1 | 575 declarations / 86 files at v1.2 | All four converted to the same named-terminal sentence |
| 10 | SIDE-kernel `README.md:101` | "`Kernel/` — Core formalization (69 files)" | v1.0-era `Kernel/` | 72 at v1.2 | Pinned to tag + pointer to `DEPOSIT_v1_2_NOTES.md` |
| 11 | SIDE-kernel `README.md:96` | "`CSSThreshold.lean` — Steane [[7,1,3]] threshold verified by `native_decide`" | pre-v1.2 | `Bridge/CSSThreshold.lean` uses `by decide` at v1.2 | Corrected (found adjacent to #10; same currency defect class) |

### HISTORICAL — true of a dated/tagged referent; left as-is

| Site | Claim | Referent | Note |
|---|---|---|---|
| `SPIRAL_MAP.md:25` | "SIDE-kernel v1.1 … 83 files, 0 sorry, 0 axioms" | v1.1 deposit row | Files ✓ (83 = `Kernel/`+`Bridge/` at `e0a8ba0`). "0 axioms" **false of its referent** per F.2026-07-10-c → annotated in the footnote below the table rather than edited |
| `phase1.5/method/A_METHODOLOGY.md:19, 340, 400, 525` | "0 sorry, 0 axioms across 83 files" / "SIDE-kernel v1.1 verifies…" | explicitly v1.1 + DOI | Version-tagged citations. Same axiom caveat |
| `phase1.5/spectral/INTERFACE_CONSERVATION.md:320` | "v1.1 … 3 files, 33 theorems, 0 sorry, 0 custom axioms" | v1.1, ProductFormula chain | Its subject (ProductFormula) *was* clean at v1.1 — claim holds |
| `day1/A_Place_to_Stand.md` (§25 tables, lines 107/1519/1608–13/1750) | per-file "0 sorry, 0 axioms"; route terminals | deposit line + in-repo v5.6 | The in-repo monograph has **already been converted to named-terminal form** (no raw file/theorem totals remain). Settled; not re-audited |
| `day1/ONE_PAGE_PROOF.md:42` | "560 Lean 4 declarations in the sorry-free core" | PLACE-papers v1.0.2 deposit (supplementary) | Deposit-frozen. Current: 575 at v1.2 |
| `day1/Seven_Mechanism_Classes.md:213` | "63 files, 135+ theorems … of 587 … zero sorry, zero custom axioms" | v1.0.2 deposit | Deposit-frozen |
| `meta/ZENODO_METADATA.md:17` | "68 files, 360 theorems" | the v1.0.2 deposit description itself | Frozen by definition |
| `meta/VERIFICATION_AND_PROPAGATION.md:12, 34` | "68 files, 360 theorems, 0 sorry, 0 axioms — ✓ confirmed" | dated propagation audit | Audit record of a past state |
| `VERIFICATION_LOOM.md:867` | "0 sorry / 0 axioms across 65 files at `e0a8ba0`" | tag-annotation audit, quoted | Append-only loom entry; already flags the 65-vs-83 scope variance |
| `FINDINGS.md:133, 137, 169, 177` | "SIDE-kernel v1.1: 83 Lean files…" etc. | dated ledger entries | Append-only ledger — never edited |
| `OPEN_TRAILS.md:239` | "83 files / 418+ theorems verified at HEAD `5260498`" | SHA-pinned trail note | Pinned snapshot |
| `heritage/WHAT_YOU_LEARN.md:18, 23, 56, 189` | "68 Lean 4 files. 360 theorems…" | Day-1 archive (`heritage` cull, 2026-06-03) | Archive directory — historical by construction |
| `internal/CONVERGENCE.md:13799` | "68 files (63 core + 5 bridge), 360 theorems" | explicitly "(March 2026)" | Self-dating |
| `internal/SIDE_EFFECTS.md` (several) | "61 files", "v66 kernel" | narrative/fiction, v66-era | Not a verification claim |
| `outputs/v54_deposit_line.md` | 560 declarations, per-file tables | the deposited v5.4 monograph line | Untracked snapshot of the deposit — historical by construction |
| `phase2/*`, `VERIFICATION_LOOM.md` federation rows | "0 sorry, 0 axioms" for SIDE-effects / compression / E-Difficulty | other kernels, commit-pinned | Property claims about *other* kernels, already theorem-named; outside the deposit-count scope |

---

## 3. Open item for the author (not enacted — deposit-facing)

`ERRATA.md` still reads **"[No errata yet.]"**, while F.2026-07-10-c establishes that the *citable* v1.1 kernel deposit's "0 axioms" claim did not hold of Route 1 or the formation certificates (`native_decide` compiler-trust axiom), and that the deposited monograph line (v5.4) claims `by decide` at the formation site where the deposit carries `by native_decide`. That is exactly the kind of correction `ERRATA.md` exists to record as a public audit trail. Two ways to close it, both author's call:

1. **Errata entry** against the v1.0.2 / v1.1 deposits stating the axiom discrepancy and pointing at v1.2 as the remedy; or
2. **Deposit v1.2** to Zenodo (it is tagged, verified and deposit-ready per `DEPOSIT_v1_2_NOTES.md`, behind the `DEPOSIT_VERIFICATION_PROTOCOL` author gate) and let the new version carry the correction, with an errata line pointing to it.

Until one of these lands, the corpus's corrected sites all say "citable deposit remains v1.1" — accurate, but the deposit itself still carries the uncorrected claim.
