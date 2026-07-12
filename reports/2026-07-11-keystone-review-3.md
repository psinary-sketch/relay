# Keystone review 3 — Simplicity v1.1 (2026-07-11)

**Document:** `phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md` ("Simplicity of Riemann Zeros — A Reduction and Convergent Arguments").
**PLACE-papers commit:** `688e3ce` (pushed; `5a03a31..688e3ce`).
**Pass:** author-ratified S1–S8. Refine-don't-rewrite; complete-read-first. Also touches `phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md` (S6 reciprocal cross-ref) and `REGISTRY.md` (S1 row correction).

---

## S1 Version reconciliation
- File located by content ("Simplicity of Riemann Zeros") and REGISTRY row 1.5b-6. **Header before edit: `*v0.1, May 2026*`** — the interim anomaly (the file's own footer identified the consolidated lineage as v1.0, May 16 2026).
- Header → **`v1.1 — 2026-07-11`** with a provenance line; footer version note → v1.1.
- REGISTRY row 1.5b-6: **v1.0 → v1.1** noted in an append-only row-correction block; the v0.1-header anomaly is recorded there, not in the paper.

## S2 Heading
- "Chapter 4 — Three Convergent Approaches" → **"Chapter 4 — Convergent Approaches from Analysis, Arithmetic, and Statistics"**; the in-text "How This Document Is Organized" reference adjusted.

## S3 C-symbol inventory + harmonization

Kernel-canonical order (read from `D:\SIDE-kernel\Bridge\TheBridgeComplete.lean`, `inductive MechanismClass`): **C1 Schwarz · C2 Euler · C3 functional_eq · C4 modular · C5 spectral · C6 cauchy_riemann · C7 hadamard.**

**Scheme A — Chapter 2 mechanism-class decomposition (harmonized to kernel):**

| Ch. 2 as written (before) | physical content | kernel-canonical (after) |
|:--|:--|:--|
| f₁ ↔ C₁ | digamma / Gamma-factor / Poisson (reality architecture) | **C₁ Schwarz reflection** |
| f₂ ↔ C₂ | reality / functional equation | **C₃ functional equation** |
| f₃ ↔ C₃ | prime-side / Euler product | **C₂ Euler** |
| f₅ ↔ C₅ | modular (Γ₀(4) spectral expansion) | **C₄ modular** (C₅ spectral realization enters here) |
| f₆ ↔ C₆ | Hadamard product | **C₇ Hadamard** |
| coupling C₄ | Cauchy–Riemann | **C₆ Cauchy–Riemann** |
| coupling C₇ | balance constraint p^{−σ}=p^{−(1−σ)} | **C₂ Euler balance** |

*Residual flagged for author confirmation:* the source's derivative-level decomposition does not bijate onto the seven kernel classes — it double-counts Euler (the Euler-product additive contribution **and** the balance coupling both map to C₂) and folds the spectral class (C₅) into the Γ₀(4) modular contribution. This is a source-side accounting artifact; it was **preserved, not rewritten** (per refine-don't-rewrite), with the kernel-canonical names/indices attached and the C₅-via-modular note added in-text.

**Scheme B — Chapter 5–7 (and the abstract's mirror) C1/C2/C3 → plain words:** this scheme (C1 = functional equation, C2 = Euler product, C3 = Ramanujan bound) is **not** the mechanism-class enumeration; converted to plain words throughout. Occurrences removed: abstract (2 clauses), Ch. 5 (2), Ch. 6 comparison table (3 rows), Ch. 6 "what the experiment confirms" list (4), Ch. 6 body ("lack C2"), Ch. 8 ("C2 is essential"). **No C-symbols survive outside Chapter 2.** (Verified: `grep` for C-symbols returns only Ch. 2 lines.)

## S4 Verb scoping
- **Ch. 3 trace formula:** "…establishes simplicity" → "…*argues for* simplicity along this route" + an explicit clause that it is a structural argument by analogy with the function-field theorem, not itself a proved theorem, and that the number-field explicit formula does not supply the same closure the Lefschetz trace formula supplies over 𝔽_q. Mathematics unchanged; only the claim-verb scoped.
- **Ch. 7 GRH transfer:** cross-referenced to the SIDE-grh-transfer kernel (v0.5.0, `SIDEGRHTransfer/GRHBridge.lean`) and scoped to what its terminal actually establishes — read from `D:\SIDE-grh-transfer`: `grh_structural_exhaustiveness_proved` proves the **structural-exhaustiveness form** for a Dirichlet-character pair (`seven_classes_chi`, `none_produce_chi`, `ostrowski_exhaustive_chi`), the χ-twisted mirror of Route 1's `structural_exhaustiveness_proved` — **not GRH itself**. The sentence now says so.

## S5 Instrument citations — found/not-found table

| Number | Claim | Source found | Cited at point of use |
|:--|:--|:--|:--|
| β ≈ 12.32 | RMT super-repulsion fit | `phase1.5/simplicity/THREE_PROOFS.md` | yes (Ch. 4) |
| 0.251 ± 0.055 | \|ζ′(ρ)\|/√γ persistence | `phase1.5/simplicity/ALL_ZEROS_SIMPLE.md` | yes (Ch. 2) |
| 0.037 | Hadamard product evaluation | `phase1.5/simplicity/THREE_PROOFS.md` | yes (Ch. 4) |
| 0.024 | phase-sum minimum | `phase1.5/simplicity/THREE_PROOFS.md` | yes (Ch. 4) |

**All four sources found; no open instrument-citation items.** No citations invented; no work-note placeholders added.

## S6 Mutual-light cross-references
- Ch. 1 VK-band + Ch. 2 persistence ↔ Surround §6a: cross-ref added at the Ch. 2 persistence finding; **reciprocal added in `THE_UNCONDITIONAL_SURROUND.md` §6a** (one sentence, dated 2026-07-11).
- Ch. 6 Epstein ↔ Surround §6a one-jaw reading ↔ compiled countermodel: named plainly — "the unrestricted joint-resultant commutation … fails as a theorem by an explicit countermodel (SIDE-lv-conservation `T3.T3doubleprime_general_commutation_fails`)".
- All monograph citations **v5.4 → v5.5**; the *Conservation of Spectra Refined* reference gains its compiled companions (SIDE-kernel `ProductFormula.conservation_of_spectra`; SIDE-lv-conservation T1/T2).

## S7 Correspondence (verified against D: kernels)

Kernels audited at: SIDE-kernel `ce5d7bd` (v1.2 = `b1407b2`); SIDE-simplicity `54ba4f3` (v0.1.0); SIDE-grh-transfer `858cbf6` (v0.5.0); SIDE-lv-conservation `c8e3d31` (v0.2.0). Verbatim `#print axioms`:

```
SpectralCannonFull.spectral_cannon                            [propext, Classical.choice, Quot.sound]
PerpendicularCrossing.perpendicular_gradients                 [propext, Classical.choice, Quot.sound]
PerpendicularCrossing.proved_infrastructure                   [propext, Classical.choice, Quot.sound]
PerpendicularCrossing.simplicity_from_trace_structure         does not depend on any axioms
PerpendicularCrossing.multiplicity_from_identity              does not depend on any axioms
SIDESimplicity.transversal_generic_empty                      [propext, Quot.sound]
SIDESimplicity.codim_exceeds_curve                            [propext, Quot.sound]
SIDESimplicity.codim_margin                                   [propext, Quot.sound]
SIDESimplicity.margin_fails_at_threshold                      [propext, Quot.sound]
SIDESimplicity.no_tuning                                      does not depend on any axioms
SIDEGRHTransfer.grh_structural_exhaustiveness_proved          [propext, Classical.choice, Quot.sound]
ProductFormula.conservation_of_spectra                        [propext, Classical.choice, Quot.sound]  (prior session)
SIDELvConservation.T1_completedRiemannZeta_factors_through_mellin  [propext, Classical.choice, Quot.sound]
SIDELvConservation.T2b_mellin_exhaustion                      [propext, Classical.choice, Quot.sound]
SIDELvConservation.T3.T3doubleprime_general_commutation_fails [propext, Classical.choice, Quot.sound]
SIDEKernel.formation                                          does not depend on any axioms
CartanBridge.formation_n_3_eq_two                             [propext, Classical.choice, Quot.sound]
```

| Claim | Kernel | Theorem (fully qualified) | Axiom profile | Status |
|:--|:--|:--|:--|:--|
| Ch. 1 — perpendicular crossing: Re ξ′(½+it) = 0 | SIDE-kernel v1.2 | `SpectralCannonFull.spectral_cannon` | `{propext, Classical.choice, Quot.sound}` | Compiled |
| Ch. 1 — perpendicular gradients at simple zeros | SIDE-kernel v1.2 | `PerpendicularCrossing.perpendicular_gradients` (+ `proved_infrastructure`) | `{propext, Classical.choice, Quot.sound}` | Compiled |
| Ch. 1 — reduction RH ⟺ off-line non-intersection | (none) | — | — | Manuscript-resident (ZFC-level) |
| Ch. 2 — transversality generically empty | SIDE-simplicity v0.1.0 | `SIDESimplicity.transversal_generic_empty` (+ `codim_exceeds_curve`, `codim_margin`, `no_tuning`) | `{propext, Quot.sound}`; `no_tuning` axiom-free | Compiled (structural core; the analytic identification of the five contributions is manuscript-resident) |
| Ch. 3 — trace-formula multiplicity-one structure | SIDE-kernel v1.2 | `PerpendicularCrossing.simplicity_from_trace_structure`; `multiplicity_from_identity` | axiom-free (none) | Structural implication compiled; full trace closure is an argument, research-reach |
| Ch. 4 — Hadamard / ℚ-independence / RMT super-repulsion | (none) | — | — | Research-reach / computational (`THREE_PROOFS.md`, `ALL_ZEROS_SIMPLE.md`) |
| Ch. 5 — Conservation of Spectra | SIDE-kernel v1.2 · SIDE-lv-conservation v0.2.0 | `ProductFormula.conservation_of_spectra`; `T1_completedRiemannZeta_factors_through_mellin`; `T2b_mellin_exhaustion` | `{propext, Classical.choice, Quot.sound}` | Compiled |
| Ch. 6 — Epstein one-jaw / joint-resultant fails by countermodel | SIDE-lv-conservation v0.2.0 | `SIDELvConservation.T3.T3doubleprime_general_commutation_fails` | `{propext, Classical.choice, Quot.sound}` | Compiled (countermodel) |
| Ch. 7 — GRH transfer (structural exhaustiveness for χ) | SIDE-grh-transfer v0.5.0 | `SIDEGRHTransfer.grh_structural_exhaustiveness_proved` | `{propext, Classical.choice, Quot.sound}` | Compiled — structural-exhaustiveness form, not GRH |
| Ch. 2/3/7 — seven-mechanism count 2+3+2+0 = 7 | SIDE-kernel v1.2 | `SIDEKernel.formation` | axiom-free (none) | Compiled |
| Ch. 2 — n₃ = 2 output scales | SIDE-kernel v1.2 | `CartanBridge.formation_n_3_eq_two` | `{propext, Classical.choice, Quot.sound}` | Count compiled; Stein/Cousin-I pillar set aside **open** (`f18e143`) |

## S8 Jargon
Scanned for phase labels, "loom", "two-leg", work-notes: none present in the body. Two clean-ups: the v1.1 provenance line reworded off "keystone-review pass" → "v1.1 pass (2026-07-11)"; Chapter 8 "Davenport-Heilbronn epistemic witness" → "evidential witness".

## Gates / honesty notes
- No mathematical claim weakened; Ch. 3 and Ch. 7 changes are claim-verb scoping only.
- The Ch. 2 C-index harmonization preserves the source's (imperfect) 7-class accounting and flags the Euler double-count / spectral-fold residual for author confirmation rather than rewriting it.
- SIDE-grh-transfer establishes structural-exhaustiveness transfer to χ, not GRH; the Correspondence and Ch. 7 both say so.
- No deposit action taken.
