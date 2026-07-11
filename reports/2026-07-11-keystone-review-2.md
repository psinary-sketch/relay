# Keystone review 2 — Unconditional Surround v0.3 (2026-07-11)

**Document:** `phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md` ("The Unconditional Surround of ξ" — a reduction of RH to the coverage premise `covers_all`, in two faces).
**PLACE-papers commit:** `5a03a31` (pushed; `31e2854..5a03a31`).
**Source:** `D:\MY-DOwnloads\REDUCTION_OF_RH_TO_ONE_PREMISE_v0_1.md` (filename stale; header **v0.2**; `covers_all` ×12 — both markers verified). Placed at the target path and edited there.
**Pass:** author-ratified R1–R8 — retitle, kernel-canonical C-index harmonization, §0 positioning, jargon, third face, Correspondence, header/registry, findings. Cumulative-not-replacing; no §§2–5 claim altered.

---

## R1 Retitle
- Title → **"The Unconditional Surround of ξ"**.
- Subtitle → "A reduction of the Riemann Hypothesis to the coverage premise `covers_all`, in two faces".

## R2 C-index harmonization — inventory + fix

Canonical order read from `D:\SIDE-kernel\Bridge\TheBridgeComplete.lean` (`inductive MechanismClass`): **C1 Schwarz · C2 Euler · C3 functional_eq · C4 modular · C5 spectral · C6 cauchy_riemann · C7 hadamard.**

| Site | C-indices as written | vs kernel-canonical | Action |
|:--|:--|:--|:--|
| §3 table | C₁ Schwarz, C₂ Euler, C₃ functional eq, C₄ PSL₂ modular, C₅ spectral, C₆ Cauchy–Riemann, C₇ Hadamard | ✓ all correct | none (semantic names already carried) |
| §4 voice table | V1→C₂, V2→C₁, V3→C₃, V4→C₆, V5→C₄, V6→C₅, V7→C₇ | ✓ all correct | none |
| §6a | "Euler zero-free region **(C₄)**"; "functional-equation transversality **(C₁)**" | ✗ Euler is C₂; functional_eq is C₃ | **fixed** → "(C₂, Euler)" and "(C₃, functional equation)" |
| line 64 | "C₁–C₇ … C₈" | range/counterfactual | none |

The known §3/§6a conflict was exactly these two §6a labels; §3 and §4 were already kernel-canonical. Semantic names are now carried at every C-index use.

## R3 Positioning paragraph (§0)
Added: the monograph argues the *discharge* (two-input Tate for Conservation of Spectra + per-class analyses); this paper deliberately brackets that to establish the *reduction* independently — so surround, discharge, and reduction can be assessed separately.

## R4 Jargon
- "SIDE exclusion principle" defined plainly at first use (§7) and tied to `techne_kernel.SIDE_exclusion` (`Kernel/Layer1.lean`): in a sealed, exhaustively-catalogued system, if `covers_all` holds and no catalogued class produces a given off-line zero, that zero cannot exist.
- §2 companion result named explicitly — **Conservation of Spectra**, with compiled companions (`ProductFormula.conservation_of_spectra`; SIDE-lv-conservation T1/T2).
- §5 "the programme's own census" → cites *Paths to the Critical Line* v0.2 (`phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md`).

## R5 Third face
- §6: added the **positivity** bullet — λ_Z(n) ≥ −λ_A(n) on the Li-channel decomposition, cross-ref Balance-and-Positivity keystone (REGISTRY 1.5c-16, retitle pending).
- §6a: added one cross-ref to `phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md` for the |ζ′(ρ)| territory.

## R7 / R8
- Header bumped to **v0.3 — 2026-07-11** with a provenance line naming the pass.
- REGISTRY row-addition block appended (append-only): `1.5a-6`, v0.3, Conf ○, Status **REVIEW**, kernel pairing = the Correspondence kernel list.
- FINDINGS entry appended: **F.2026-07-11-b** (below).

---

## Verification method (no memory; kernels on D:)

All profiles read from `#print axioms` against the kernels as they stand on D: (all pre-built; probes run directly). Kernels: SIDE-kernel `ce5d7bd` (v1.2 = `b1407b2`); SIDE-lv-conservation `c8e3d31` (v0.2.0); SIDE-archimedean `8019d9d`, SIDE-frobenius `2efe9f2`, SIDE-rcurve `d5f33b4`, SIDE-spinor `b235bc6` (all v0.1.0).

### Verbatim `#print axioms` (terminals cited)

```
techne_kernel.SIDE_exclusion                                     does not depend on any axioms
techne_kernel.ExhaustiveCatalogue.covers_all                     (structure field — the open premise, not a theorem)
techne_kernel_voice1.balance_theorem                             [propext, Classical.choice, Quot.sound]
techne_kernel_voice2.symmetries_agree_iff                        [propext, Classical.choice, Quot.sound]
techne_kernel_voice3.reflect_fixed_iff                           [propext, Classical.choice, Quot.sound]
techne_kernel_voice5.modular_forces_half                         [propext, Classical.choice, Quot.sound]
techne_kernel_voice6.self_adjoint_forces_half                    [propext, Classical.choice, Quot.sound]
techne_kernel_voice7.c7_forces_half                              [propext, Classical.choice, Quot.sound]
ProductFormula.conservation_of_spectra                           [propext, Classical.choice, Quot.sound]
SIDEKernel.formation                                             does not depend on any axioms
CartanBridge.formation_n_3_eq_two                                [propext, Classical.choice, Quot.sound]
SIDEArchimedean.archimedean_forces_half                          [propext, Classical.choice, Quot.sound]
SIDEFrobenius.indicial_forces_half                               [propext, Classical.choice, Quot.sound]
SIDERCurve.monotone_unique_zero                                  [propext, Classical.choice, Quot.sound]
SIDESpinor.spinor_forces_half                                    [propext, Classical.choice, Quot.sound]
SIDELvConservation.T1_completedRiemannZeta_factors_through_mellin [propext, Classical.choice, Quot.sound]
SIDELvConservation.T2b_mellin_exhaustion                         [propext, Classical.choice, Quot.sound]
SIDELvConservation.T3.T3prime_shared_witness                     [propext, Classical.choice, Quot.sound]
SIDELvConservation.T3.T3doubleprime_general_commutation_fails    [propext, Classical.choice, Quot.sound]
SIDELvConservation.T3.T3_perClass_to_combinations                [propext, sorryAx, Classical.choice, Quot.sound]  ← the single pinned sorry
```

---

## R6 Correspondence (as landed — verified)

| Claim (as stated in the document) | Kernel | Theorem / field (fully qualified) | Axiom profile | Status |
|:--|:--|:--|:--|:--|
| `covers_all` — the one open node (§6) | SIDE-kernel v1.2 | `techne_kernel.ExhaustiveCatalogue.covers_all` (structure field, `Kernel/Layer1.lean`) | — (hypothesis field, not a theorem) | Open premise; discharge manuscript-resident; consuming principle `techne_kernel.SIDE_exclusion` compiled |
| SIDE exclusion principle (§7) | SIDE-kernel v1.2 | `techne_kernel.SIDE_exclusion` | axiom-free (none) | Compiled |
| Joint-to-single closure step (§6) | SIDE-lv-conservation v0.2.0 | `SIDELvConservation.T3.T3_perClass_to_combinations` (pin); `...T3.T3doubleprime_general_commutation_fails` (countermodel); `...T3.T3prime_shared_witness` (bridge) | pin `{propext, sorryAx, Classical.choice, Quot.sound}`; countermodel & bridge `{propext, Classical.choice, Quot.sound}` | Bracketed — unrestricted commutation false (T3″), closes under shared witness (T3′); one pinned `sorry` — research-reach |
| §2 Conservation of Spectra | SIDE-kernel v1.2 · SIDE-lv-conservation v0.2.0 | `ProductFormula.conservation_of_spectra`; `SIDELvConservation.T1_completedRiemannZeta_factors_through_mellin`; `SIDELvConservation.T2b_mellin_exhaustion` | `{propext, Classical.choice, Quot.sound}` | Compiled |
| §4 seven voice identifications | SIDE-kernel v1.2 (+ checkpoints) | `techne_kernel_voice1.balance_theorem` (C₂), `voice2.symmetries_agree_iff` (C₁), `voice3.reflect_fixed_iff` (C₃), `voice5.modular_forces_half` (C₄), `voice6.self_adjoint_forces_half` (C₅), `voice7.c7_forces_half` (C₇); checkpoints `SIDEArchimedean.archimedean_forces_half`, `SIDEFrobenius.indicial_forces_half`, `SIDESpinor.spinor_forces_half`, `SIDERCurve.monotone_unique_zero` | `{propext, Classical.choice, Quot.sound}` (all) | Compiled |
| §3 formation count 2+3+2+0 = 7 | SIDE-kernel v1.2 | `SIDEKernel.formation` | axiom-free (none) | Compiled |
| §3 n₃ = 2 | SIDE-kernel v1.2 | `CartanBridge.formation_n_3_eq_two` (via `CartanBridge.output_stage_card`) | `{propext, Classical.choice, Quot.sound}` | Count compiled; Stein/Cousin-I pillar set aside **open** per `f18e143` (loom 2026-06-15) |
| §6a computational claims (\|ζ′(ρ)\|/√γ ≈ 0.251, Lehmer) | (none) | — | — | Research-reach; surveyed in `phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md` |
| RH ⟺ `covers_all`, and its discharge | (none) | — | — | Manuscript-resident (monograph two-input Tate + per-class) |

---

## R8 FINDINGS entry (as landed)

**F.2026-07-11-b — Reduction paper's joint-resultant analysis anticipated the compiled bracket.** §6's prose ("no zero of ξ is a joint resultant of two or more classes that no single class produces," Epstein/Davenport–Heilbronn 1936 the standing witness) is **T3″ in words** — `SIDELvConservation.T3.T3doubleprime_general_commutation_fails` proves the unrestricted ∀∃ ⟹ ∃∀ commutation false, `T3.T3prime_shared_witness` closes it under a shared witness, and the pin `T3.T3_perClass_to_combinations` (`sorryAx`) marks the exact named gap. The §6 reading predates the compiled bracket (lv-conservation v0.2.0, 2026-07-09) — informal analysis anticipated the machine-checked result. Epistemic: ◆ for the correspondence; the node remains the one open premise (⋄, author-gated).

## Gates / honesty notes
- No §§2–5 mathematical claim was altered; §6a two labels were corrected to kernel-canonical indices.
- `covers_all` is the single open node — a hypothesis field, not a theorem; its discharge is manuscript-resident.
- The T3 bracket carries one pinned `sorry` at the joint-to-single step (research-reach); T3′/T3″ themselves are clean.
- n₃ = 2 is compiled but the Stein/Cousin-I pillar is set aside open (`f18e143`).
- No deposit action taken.
