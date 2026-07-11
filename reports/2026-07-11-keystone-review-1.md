# Keystone review 1 — PATHS v0.2 (2026-07-11)

**Document:** `phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md` ("Paths to the Critical Line — An Open Census of Proof Routes to the Riemann Hypothesis").
**PLACE-papers commit:** `31e2854` (pushed; `a758699..31e2854`).
**Pass:** author-ratified keystone-review pass — repo placement + 2026-07-11 delta + Correspondence table (first instance of the corpus Correspondence standard) + jargon-clarification pass. Cumulative-not-replacing; the census body is unchanged except for the jargon pass and the appended delta/correspondence.

---

## What was done

1. **Placement.** The source `PATHS_TO_THE_CRITICAL_LINE_v0_1.md` was not in the repo (expected). The author copy `D:\MY-DOwnloads\PATHS_TO_THE_CRITICAL_LINE_v0_1.md` (v0.1, 2026-05-29; verified to contain "An Open Census of Proof Routes") was placed at `phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md` and edited there.
2. **§I** heading "Three enumerations, kept distinct" → "The enumerations, kept distinct"; the first sentence now states the three-ness as the finding.
3. **Jargon pass** (define-at-first-use, nothing deleted): VAJRA PLINKO introduced plainly at §IV as "a node-obstruction model (internally, the Resonance Plinko)…"; "Voice-pattern" glossed at first use (§III) as the small-kernel template; "C₈ Stress-Tester (Ξ.9)" given a plain-words clause; "THE FINDINGS" (§VI) replaced with the concrete reference `phase1.5/deep-structure/TRIVIUM_FINDINGS.md` §XII (the Landau Shield / the 2-bit phase layer); "formation count (2,3,2,0)" glossed as the counts of primitive operations, places, entire-function scales, and interfaces. The term "two-leg" was not introduced (checked: 0 occurrences).
4. **§IV citation** for the independence figures added: mean pairwise independence ≈ 0.845 sourced to `internal/CRITICAL_RESOLVE.md` (RESONANCE scoring).
5. **DELTA — 2026-07-11** appended (four items, below).
6. **Correspondence** table appended as the final section before the footer (below).
7. **Header** bumped to v0.2 — 2026-07-11 with a one-line provenance naming this pass.
8. **REGISTRY** row-addition block appended (append-only): `1.5a-5`, v0.2, Conf ○, Status REVIEW, kernel pairing = the Correspondence kernel list.

---

## Verification method (no memory; kernels on D:)

Every axiom profile was read from `#print axioms` run against the kernels as they stand on D:, after building any missing modules. Subagent probes were abandoned (they deferred to background `lake` and returned no result); all audits were run directly. Kernels audited (all pre-built):

| Kernel | Commit | Tag | Tag date |
|:--|:--|:--|:--|
| SIDE-kernel | `ce5d7bd` | v1.2 = `b1407b2` | — |
| SIDE-archimedean | `8019d9d` | v0.1.0 | 2026-05-30 |
| SIDE-frobenius | `2efe9f2` | v0.1.0 | 2026-05-30 |
| SIDE-rcurve | `d5f33b4` | v0.1.0 | 2026-05-30 |
| SIDE-spinor | `b235bc6` | v0.1.0 | 2026-05-30 |
| SIDE-lv-conservation | `c8e3d31` | v0.2.0 | 2026-07-09 |

### Verbatim `#print axioms` output (terminals used)

```
techne_kernel_voice1.balance_theorem                              [propext, Classical.choice, Quot.sound]
PoissonExhaustion.gate_e_exhaustive_derived                       [propext, Classical.choice, Quot.sound]
structural_exhaustiveness_proved                                  [propext, Classical.choice, Quot.sound]
ProductFormula.conservation_of_spectra                            [propext, Classical.choice, Quot.sound]
SIDEKernel.formation                                              (does not depend on any axioms)
CartanBridge.output_stage_card                                    [propext, Classical.choice, Quot.sound]
CartanBridge.formation_n_3_eq_two                                 [propext, Classical.choice, Quot.sound]
SIDEArchimedean.archimedean_forces_half                           [propext, Classical.choice, Quot.sound]
SIDEFrobenius.indicial_forces_half                                [propext, Classical.choice, Quot.sound]
SIDERCurve.monotone_unique_zero                                   [propext, Classical.choice, Quot.sound]
SIDESpinor.spinor_forces_half                                     [propext, Classical.choice, Quot.sound]
SIDELvConservation.T1_completedRiemannZeta_factors_through_mellin [propext, Classical.choice, Quot.sound]
SIDELvConservation.T2b_mellin_exhaustion                          [propext, Classical.choice, Quot.sound]
SIDELvConservation.T3.T3prime_shared_witness                      [propext, Classical.choice, Quot.sound]
SIDELvConservation.T3.T3doubleprime_general_commutation_fails     [propext, Classical.choice, Quot.sound]
SIDELvConservation.T3.T3_perClass_to_combinations                 [propext, sorryAx, Classical.choice, Quot.sound]  ← the single pinned sorry (F.2026-07-09-b)
```

The bracket is exactly as claimed: T3′ (shared witness) and T3″ (countermodel) are both clean `{propext, Classical.choice, Quot.sound}` with no `sorryAx`; the pinned `sorry` sits only at the intermediate `T3.T3_perClass_to_combinations`.

---

## DELTA — 2026-07-11 (as landed)

**(a) Checkpoints 1.2-A/B/C/D executed — all four checkpoint kernels built, tagged `v0.1.0` on 2026-05-30, audited clean** (each terminal `{propext, Classical.choice, Quot.sound}`):
- 1.2-A · II.1 Archimedean — `SIDE-archimedean` (`8019d9d`) · `SIDEArchimedean.archimedean_forces_half`
- 1.2-B · II.3 Frobenius — `SIDE-frobenius` (`2efe9f2`) · `SIDEFrobenius.indicial_forces_half`
- 1.2-C · II.6 Spinor/Information — `SIDE-spinor` (`b235bc6`) · `SIDESpinor.spinor_forces_half`
- 1.2-D · II.5 R-Curve (equivalence) — `SIDE-rcurve` (`d5f33b4`) · `SIDERCurve.monotone_unique_zero` (closure research-reach)

**(b)** `SIDE-lv-conservation` v0.2.0: Mellin factorization (T1) and exhaustion lemmas (T2) compiled; the step-(9) bridge bracketed — unrestricted commutation false by countermodel (T3″), closes under the shared witness (T3′). §V's load-bearing sentence now has a compiled theorem-pair behind its closure step.

**(c)** Cross-reference to the Balance-and-Positivity keystone — REGISTRY row `1.5c-16`, retitle pending (currently "The Single Indefinite Term"): II.2's balance identification measured against the criterion's positivity requirement; the §III Weil-bridge research-reach flag now has a named instrument.

**(d)** Phase-1.1 definition harmonized: an internal refinement of deposited Phase 1 content (route-finishing being one part).

---

## Correspondence (as landed — verified)

| Claim (as stated in the document) | Kernel | Theorem (fully qualified) | Axiom profile | Status |
|:--|:--|:--|:--|:--|
| II.1 Archimedean — FE structure forces σ = 1/2 | SIDE-archimedean v0.1.0 | `SIDEArchimedean.archimedean_forces_half` | `{propext, Classical.choice, Quot.sound}` | Compiled (identification kernel) |
| II.2 Multiplicative — Euler balance identifies σ = 1/2 | SIDE-kernel v1.2 | `techne_kernel_voice1.balance_theorem` | `{propext, Classical.choice, Quot.sound}` | Compiled (Voice1) |
| II.3 Frobenius — indicial root forces σ = 1/2 | SIDE-frobenius v0.1.0 | `SIDEFrobenius.indicial_forces_half` | `{propext, Classical.choice, Quot.sound}` | Compiled (identification kernel) |
| II.5 R-Curve — RH ⟺ V-monotonicity | SIDE-rcurve v0.1.0 | `SIDERCurve.monotone_unique_zero` | `{propext, Classical.choice, Quot.sound}` | Equivalence compiled; closure research-reach |
| II.6 Spinor/Information — orbit collapse forces σ = 1/2 | SIDE-spinor v0.1.0 | `SIDESpinor.spinor_forces_half` | `{propext, Classical.choice, Quot.sound}` | Compiled (identification kernel) |
| "One voice suffices" — per-class exclusion in a closed system | SIDE-kernel v1.2 | `PoissonExhaustion.gate_e_exhaustive_derived` | `{propext, Classical.choice, Quot.sound}` | Compiled |
| Structural exhaustiveness (Route 1) | SIDE-kernel v1.2 | `structural_exhaustiveness_proved` | `{propext, Classical.choice, Quot.sound}` | Compiled |
| Conservation frame — product formula carries no s-dependence | SIDE-kernel v1.2 | `ProductFormula.conservation_of_spectra` | `{propext, Classical.choice, Quot.sound}` | Compiled |
| Conservation companions — Mellin factorization / exhaustion | SIDE-lv-conservation v0.2.0 | `SIDELvConservation.T1_completedRiemannZeta_factors_through_mellin`; `SIDELvConservation.T2b_mellin_exhaustion` | `{propext, Classical.choice, Quot.sound}` | Compiled |
| Conservation bridge — the bracketed theorem-pair (§V closure) | SIDE-lv-conservation v0.2.0 | `SIDELvConservation.T3.T3prime_shared_witness`; `SIDELvConservation.T3.T3doubleprime_general_commutation_fails` | `{propext, Classical.choice, Quot.sound}` | Bracketed; one pinned `sorry` at `T3.T3_perClass_to_combinations` — research-reach |
| Formation count 2 + 3 + 2 + 0 = 7 | SIDE-kernel v1.2 | `SIDEKernel.formation` | axiom-free (none) | Compiled |
| n₃ = 2 (entire-function scales) | SIDE-kernel v1.2 | `CartanBridge.formation_n_3_eq_two` (via `CartanBridge.output_stage_card`) | `{propext, Classical.choice, Quot.sound}` | Count compiled; Stein / Cousin-I pillar (T3) set aside **open** per SIDE-kernel `f18e143` (loom ruling 2026-06-15) |
| II.4 Sieve — σ = 1/2 on average | (none) | — | — | Research-reach; individual-equidistribution barrier (§VI Landau Shield) |
| R-Curve monotonicity closure; Weil-formula simplicity bridge | (none) | — | — | Research-reach (§VII) |

---

## References resolved during the pass

- "THE FINDINGS" → `phase1.5/deep-structure/TRIVIUM_FINDINGS.md` §XII (Landau Shield / Layer-2 the 2-bit phase; the source of §VI's load-bearing sentence).
- Independence figures (mean pairwise ≈ 0.845, all pairs ≥ 0.75) → `internal/CRITICAL_RESOLVE.md` (RESONANCE scoreboard).
- Balance-and-Positivity keystone → REGISTRY `1.5c-16`, currently "The Single Indefinite Term" (retitle pending).

## Gates / honesty notes

- No mathematical claim in the census body was altered; the jargon pass is clarification only.
- The n₃ = 2 count theorem is compiled and clean, but the third-scale mathematical justification (Stein property of ℂ / Cousin-I) is **set aside as open** in SIDE-kernel at `f18e143`; the Correspondence row states this rather than implying the pillar is closed.
- The R-curve closure and the Weil-formula simplicity bridge remain research-reach; rows carry that status, never blank.
- No deposit action was taken; this is a repo/registry pass plus a verified Correspondence table.
