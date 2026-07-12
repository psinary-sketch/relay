# Core-terminal statement-read -- 2026-07-12

Gate (a)-(c) of the E0 salt-check, run on the RH core at pin SIDE-kernel v1.2
(peeled tag SHA b1407b2231c650d6d938cfa649f589fd388f669c, verified by rev-list and
ls-remote refs/tags/v1.2^{}). This closes next-wave gate 2 of the 2026-07-12
federation salt-check loom entry: the core's axiom audit (2026-07-10) had run (d)
only; this read runs (a)-(c) -- statements read against monograph Ch. 25 claims.

**Result: THE CORE HOLDS.** CONFIRM on four of five terminals; two citation-site
findings on Route 3, neither of them a defect in what compiles.

- **Integration pair** (`rh_from_structural_exhaustiveness`, `structural_exhaustiveness_iff_rh`):
  CONFIRM; grade **DERIVES**. The chapter itself discloses the premise as a direct
  restatement of RH on the sigma-coordinate; the XiDef bridge to Mathlib's
  `RiemannHypothesis` is sound. Verified at pin: the propositional
  `StructuralExhaustiveness` def is retained ("for backward compatibility",
  Integration.lean:201) and is what the two terminals take; the newer
  `StructuralExhaustivenessData` 4-field structure sits alongside it and is
  instantiated from compiled theorems -- it is not what the terminals quantify over.
- **Route 1** (`structural_exhaustiveness_proved`, TheBridgeComplete.lean:188): CONFIRM;
  grade **DERIVES** with row-notes -- the identifier is root-namespace (the file declares
  no namespace; the chapter's "Bridge." prefix is directory-style, and a *different*
  conditional theorem at ConservationBridge.lean:29 shares the bare name), and the C6/C7
  conjuncts exclude over definition-encoded functions (`hadamard_contrib := 0`;
  `zero_codim`, an if-then-else on sigma = 1/2), disclosed in the chapter's own table.
- **Route 2** (`SpectralCannonFull.spectral_cannon`): CONFIRM; grade **DERIVES**. Genuine
  Mellin-level Schwarz reflection on `completedRiemannZeta_0`; the discharge claim holds.
  Axiom form at pin: standard 3 (propext, Classical.choice, Quot.sound).
- **Route 3** (`ConservationBridge.riemann_hypothesis`): signature confirms; grade
  **INTERFACES**. *Finding 1 -- quantifier mismatch:* prose (Ch. 25.5, line 1582) says balance
  "at some prime," the pinned def (ConservationBridge.lean:13-15) is the universal form, so the
  compiled conditional is **weaker** than the chapter describes; `PoissonExhaustion.BalanceContradiction`
  (:43-47) already uses the existential, so the kernel is internally inconsistent about the
  quantifier. The proof uses only p = 2 today, so the existential form still closes.
  *Finding 2 -- discharge pointer:* Ch. 25.5/25.7 point at Chapter 13 (s-darkness of the product
  formula), while the corpus's newest keystone (BALANCE_AND_POSITIVITY, dfbcd57) locates the premise
  as one register of the open joint, sharpest form RH iff lambda_Z(n) >= -lambda_A(n). The INTERFACES
  naming obligation is met; the pointer is stale. **W-7** filed under OPEN_TRAILS O.16.

## The gate fired on its own draft

Recorded because it is the point of the gate. The draft of this read carried an
"incidental" finding that Ch. 25.2 still reads "`native_decide` verifies 2+3+2+0 = 7"
and owes a monograph edit. **False at the pin.** The live monograph (v5.6) line 1541
already reads "`decide` verifies 2 + 3 + 2 + 0 = 7 (the canonical `SIDEKernel.formation`,
axiom-free)", and line 1658 already asserts zero `axiom` / `sorry` / `native_decide` across
`Kernel/`, `Bridge/`, `MetaKernel.lean` -- both true at v1.2. The `native_decide` wording
survives only in the **deposited v5.4 line** (a frozen artifact, not a live site), where it is
accurate about the v1.1 deposit and is already covered -- along with that deposit's "zero custom
axioms" claim -- by ERRATA `E-2026-07-12-1` and FINDINGS `F.2026-07-10-c`. No monograph edit is
owed. A read that had trusted its own draft would have filed a phantom work-order against a line
that was corrected this morning: the wave's failure mode arriving from the opposite direction.

Ledger changes this run: `VERIFICATION_LOOM.md` (entry appended, gate 2 closed),
`OPEN_TRAILS.md` (W-7 inserted into O.16). Gate 1 (wave-wide Correspondence re-grade)
remains open; the five core rows are done.
