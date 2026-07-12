# Keystone review 4 — GRH Cascade v0.3 (2026-07-11)

**Document:** `phase1.5/spectral/GRH_CASCADE.md`.
**PLACE-papers commit:** `8409cb9` (pushed; `688e3ce..8409cb9`).
**Pass:** author-ratified G1–G10 + the Type-D-naturalization amendment (A1–A3). Refine-don't-rewrite; the June reframe's honesty structure preserved. Also touches `THE_UNCONDITIONAL_SURROUND.md` (G8a reciprocal) and `REGISTRY.md` (1.5d-4 update).

## G1 Kernel-citation correction
Everywhere the paper cited "SIDE-kernel v1.1 … 0 sorry, 0 axioms across 83 files" (Abstract, §I(1), §IX.1, §IX.3, References) → **SIDE-kernel v1.2 (tag `b1407b2`)**, route terminals at `{propext, Classical.choice, Quot.sound}`, formation certificates axiom-free; v1.1 Zenodo DOI 10.5281/zenodo.19937590 retained as the citable deposit, with the honest clause that v1.2 supersedes v1.1's axiom profile (v1.1's Route 1 and formation certificates carried `native_decide`; F.2026-07-10-c / -d). All bare file/theorem counts removed in favor of named theorems.

## G2 Abstract conflation
First sentence reworded: "The Riemann Hypothesis — established in the monograph and verified at the architecture level in SIDE-kernel …". The phrase "two-leg" does not appear.

## G3 Register consistency
§I positioning paragraph added (model: Surround §0). Scope-carrying phrasing attached at §IV (Landau-Siegel exclusion inherits the open GRH transfer), §V (Artin unconditional "to the extent GRH is established"), §X ("to the degree GRH is established"). Claims stay; certificates attach.

## G4 Enumeration verification — three-way comparison

| Source | Enumeration (verbatim) |
|:--|:--|
| **Kernel** `SIDE-kernel/Bridge/TheBridgeComplete.lean` (`inductive MechanismClass`) | `C1_schwarz · C2_euler · C3_functional_eq · C4_modular · C5_spectral · C6_cauchy_riemann · C7_hadamard` |
| **SIDE-grh-transfer** `produces_offline_chi` / `c1_chi_exclusion`…`c7_chi_exclusion` | excludes `.C1_schwarz · .C2_euler · .C3_functional_eq · .C4_modular · .C5_spectral · .C6_cauchy_riemann · .C7_hadamard` — **identical to the kernel** |
| **Paper §II.4 / §III.2 (before this pass)** | Mellin transform · Euler product · Gamma factor · functional equation · Hadamard product · explicit formula · balance identity |

**Verdict:** kernel ≡ grh-transfer (no rotation between them). The paper's list was a *different* enumeration — the analytic apparatus rather than the structural mechanism classes. **Harmonized the paper to kernel canon** (C1 Schwarz … C7 Hadamard) with semantic names at every use and per-class kernel cites; the analytic apparatus (Mellin, Gamma, explicit formula) is retained as the machinery the classes act through, not as classes.

## G5 Vocabulary
§IX.2 "close the gap to" → "close the remaining formalization distance — the analytic instantiation of the per-prime balance — to …" (A2). A full `gap`/`blind` grep leaves only Clay "mass gap" and the retired `gapped := True` identifier (both excepted); zero "blind".

## G6 / G7 Internal-address conversion & §IX.2 recast
O.13, LV-H-6/M-6/L-5, CP-B-2/-4, LE-K-6, "Phase S.5a", "Phase S.2–S.4" → plain language ("an open reconciliation tracked in the programme's verification ledger" and kin); every disclosure's content kept. M3–M5 → the twin-prime / Goldbach / Sophie Germain milestones (internal code parenthesized once). §IX.2 heading → "Open formalization problems"; all (high/medium/low priority) tags stripped.

## A1 Type-D naturalization
Prose classification code → **"additive–multiplicative conspiracy"** (adjective "the additive–multiplicative conspiracy exclusion"); "(internally classified Type D)" parenthesized once at first prose use (Status block), then never again — including the §VI "TYPE D conspiracy" and every "Type-D exclusion architecture". Compiled identifiers (`no_type_d_conspiracies`, `IsEmpty TypeD`, file paths) kept verbatim. **A3 grep verified:** zero prose "Type-D"/"TYPE D" outside the single first-use parenthetical, code identifiers, and the Correspondence table.

## G8 Cross-references
(a) §III.3 transport → named the per-class-to-joint bracket in SIDE-lv-conservation (`T3.T3doubleprime_general_commutation_fails`, `T3.T3prime_shared_witness`), cross-ref Surround; **reciprocal added in Surround §6** (dated 2026-07-11). (b) §IV real-character → the pole–Euler unfusion for χ≠χ₀ (`THE_SINGLE_INDEFINITE_TERM_v0_1.md`); §II.4 → Euler-channel localization cross-ref to Surround §2/§6. (c) monograph references → v5.5.

## G9 Correspondence (verified against D: kernels)

Kernels audited at: SIDE-kernel `ce5d7bd` (v1.2 = `b1407b2`); SIDE-grh-transfer `858cbf6` (v0.5.0); SIDE-effects `c66f3c5`; SIDE-bsd-formation-transfer `7425d73` (v0.1.0); SIDE-yang-mills-formation `79e4f45` (v0.1.0). Verbatim `#print axioms`:

```
SIDEGRHTransfer.seven_classes_chi                    [propext, Classical.choice, Quot.sound]
SIDEGRHTransfer.c1_chi_exclusion / c4 / c7           [propext, Classical.choice, Quot.sound]
SIDEGRHTransfer.grh_structural_exhaustiveness_proved [propext, Classical.choice, Quot.sound]
SIDEGRHTransfer.twisted_balance_at_unramified_prime  [propext, Classical.choice, Quot.sound]   (+ _at_half, paired_* — S7 audit, all standard-three)
SIDEEffects.Phase15.Module1.crt_exhaustiveness       [propext, Classical.choice, Quot.sound]
SIDEEffects.Phase15.Module1.no_type_d_conspiracies   [propext, Classical.choice, Quot.sound]
ECondition.type_I_has_ostrowski                      [propext, Quot.sound]
SilenceTheorem.silence_universal                     does not depend on any axioms   (hypothesis: I.is_universal)
ostrowski_exhaustive  (OstrowskiBridge)              [propext, Classical.choice, Quot.sound]
neg_eq_neg_one_sub_iff (LocalZeta)                    [propext, Classical.choice, Quot.sound]
SIDEBSDFormationTransfer.formation_preserved         does not depend on any axioms
SIDEBSDFormationTransfer.both_interfaces_dark        does not depend on any axioms
SIDEBSDFormationTransfer.all_seven_transfer          does not depend on any axioms
SIDEYangMillsFormation.mass_gap_equals_n3_certification   does not depend on any axioms
SIDEYangMillsFormation.silence_boundary_at_output_stage   does not depend on any axioms
```

| Claim | Kernel | Theorem | Axiom profile | Status |
|:--|:--|:--|:--|:--|
| GRH structural exhaustiveness | SIDE-grh-transfer v0.5.0 | `grh_structural_exhaustiveness_proved` (+ `seven_classes_chi`, `c1..c7_chi_exclusion`, `none_produce_chi`, `ostrowski_exhaustive_chi`) | `{propext, Classical.choice, Quot.sound}` | Compiled — structural-exhaustiveness analog; full Mathlib-GRH bridge open |
| Character-insensitive balance | SIDE-grh-transfer v0.5.0 | `twisted_balance_at_unramified_prime`; `twisted_balance_at_half`; `voice1_balance_chi` | `{propext, Classical.choice, Quot.sound}` | Compiled |
| Paired-voice chorus (complex χ) | SIDE-grh-transfer v0.5.0 | `paired_reflection_axis_invariant_iff` (+ 5 more) | `{propext, Classical.choice, Quot.sound}` | Compiled |
| Mechanism Theorem | SIDE-kernel v1.2 | `ECondition.type_I_has_ostrowski` | `{propext, Quot.sound}` | Compiled |
| Universal Silence | SIDE-kernel v1.2 | `SilenceTheorem.silence_universal` | axiom-free (none) | Compiled — hypothesis `I.is_universal` |
| Domain Ostrowski bridge | SIDE-kernel v1.2 | `ostrowski_exhaustive` | `{propext, Classical.choice, Quot.sound}` | Compiled |
| Per-prime balance | SIDE-kernel v1.2 | `neg_eq_neg_one_sub_iff` | `{propext, Classical.choice, Quot.sound}` | Compiled |
| Additive–multiplicative conspiracy exclusion | SIDE-effects `c66f3c5` | `Phase15.Module1.no_type_d_conspiracies` (via `crt_exhaustiveness`) | `{propext, Classical.choice, Quot.sound}` | Compiled; `Milestones` twin/Goldbach/Sophie Germain open `sorry` |
| Landau-Siegel exclusion | (none) | — | — | Classical reduction (trivial-after-GRH) |
| Artin primitive root | (none) | — | — | Classical reduction (Hooley 1967) |
| BSD formation placement | SIDE-bsd-formation-transfer v0.1.0 | `formation_preserved` (+ `both_interfaces_dark`, `all_seven_transfer`) | axiom-free (none) | Verifies the placement, not the theorem |
| Yang-Mills mass-gap placement | SIDE-yang-mills-formation v0.1.0 | `mass_gap_equals_n3_certification` (+ `silence_boundary_at_output_stage`) | axiom-free (none) | Verifies the placement, not the theorem |

References' kernel-federation subsection deduplicated to pointers at this table.

## G10
Header → **v0.3 — 2026-07-11** + provenance; REGISTRY row **1.5d-4 → v0.3**, REVIEW (the row carried v0.1 while the paper read v0.2 — reconciled), kernel pairing = the Correspondence list. Subtitle unchanged (author-retained).

## Notes
- The monograph is cited without an explicit version in most places; the deposited-monograph and Chapter-20 references were set to v5.5.
- No deposit action taken.
