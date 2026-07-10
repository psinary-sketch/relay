# 2026-07-10 — SIDE-kernel v1.1 deposit-gate audit + fix-forward sketch

Session-relay report. Reports only, no research content.

## Correction to Task C of the earlier cascade-delta report

The Task C section of `2026-07-10-cascade-delta-keystone-gatecheck.md` reported "MATCH" for the monograph §25.2 `SIDEKernel.formation` axiom-free claim. That verdict was against the **current working tree of `D:\SIDE-kernel`**, not against the **tagged `v1.1` (the citable Zenodo deposit)**.

**Corrected verdict: tree MATCH / v1.1 tag MISMATCH.** Details below.

## Audit 1 — native_decide textual census (`git grep -n`)

### v1.1 tag

100+ occurrences across 20 Lean source files:

| File | Count | Notable |
|---|---|---|
| `Bridge/CSSThreshold.lean` | 12 | Steane [[7,1,3]] threshold |
| `Bridge/CartanBBridge.lean` | 3 (incl. 2 docstring) | Contains `native_decide` inside a proof body |
| `Bridge/CrossClassExclusion.lean` | 1 | `two_channels : Fintype.card CouplingChannel = 2` |
| `Bridge/FanoSteane.lean` | 20 | Fano incidence + Steane parameters |
| `Bridge/OstrowskiBridge.lean` | 1 | `formation_n2 : Fintype.card TransformationStage = 3` |
| `Bridge/TheBridgeComplete.lean` | 1 | `seven_classes : Fintype.card MechanismClass = 7` |
| `Kernel/Alexander.lean` | 5 | numerical identities |
| `Kernel/Bijection.lean` | 2 | `mech_card`, `id_card` |
| `Kernel/ConstanceSectors.lean` | 12 | ext / Sophie-Germain chains |
| `Kernel/Core.lean` | 2 | `formation_count`, `formation` (**Route 1 chain**) |
| `Kernel/Enumera.lean` | 12 | F1..F20 enumeration checks |
| `Kernel/Frobenius.lean` | 3 | Frobenius-number checks |
| `Kernel/GUECondition.lean` | 1 | `z4_not_z2 : 4 > 2` |
| `Kernel/Ostrowski.lean` | 1 | `places_decomposition : 1 + 1 + 1 = 3` |
| `Kernel/SiegelExclusion.lean` | 2 | conductor/totient |
| `Kernel/Stormer.lean` | 6 | consecutive-smooth pair checks |
| `Kernel/TriviumCode.lean` | 10 | code partition / distance / bounds |

Plus 3 non-executable occurrences at v1.1 (docstrings in Bridge/CartanBBridge, comment in Kernel/RH.lean:31 note, legacy file, README).

### HEAD (current tree)

`git grep -c native_decide HEAD` reports **3 non-executable occurrences only** — `AGENTS.md:75`/`:79`, `README.md:96` (all describing the deprecated tactic in prose), and `legacy/FmodifProbe.lean:34` (a comment). **Zero `by native_decide` tactic uses remain in Lean source.**

## Audit 2 — divergence summary `git diff --stat v1.1..HEAD`

41 files changed, +782/−532. Selected highlights (all Lean source changes are `by native_decide` → `by decide` swaps unless noted):

| File | Δ lines | Nature |
|---|---|---|
| `Bridge/CSSThreshold.lean` | ~26 | 12 tactic swaps |
| `Bridge/CartanBBridge.lean` | 6 | docstring + proof-line swaps |
| `Bridge/CrossClassExclusion.lean` | 2 | tactic swap |
| `Bridge/FanoSteane.lean` | 42 | 20 tactic swaps |
| `Bridge/OstrowskiBridge.lean` | 2 | tactic swap (Route 1 chain) |
| `Bridge/SIDEBridge.lean` | 2 | (unrelated to native_decide) |
| `Bridge/TheBridgeComplete.lean` | 2 | tactic swap on `seven_classes` (**Route 1**) |
| `Kernel/Alexander.lean` .. `Kernel/TriviumCode.lean` | 4..33 each | tactic swaps + minor |
| `Kernel/Core.lean` | 4 | 2 tactic swaps (`formation_count`, `formation`) |
| `Kernel/PerpendicularCrossingProbe.lean` | −141 | removed (duplicate of SpectralCannonFull; §25.8 records the housekeeping) |
| `Kernel/SpectralCannonFull4.lean` → `SpectralCannonFull.lean` | rename | Route 2 file rename |
| `Kernel/SpectralCannonFull4_test.lean` | −5 | scratch test removed |
| `Kernel/StructuralCount.lean` | −180 | (large refactor; unrelated) |
| `MetaKernel.lean` | −80 | (large refactor; unrelated) |
| `Kernel/Cascade/*.lean` | additions | 4 new files (Sieve infrastructure) |
| Root files | +additions | `AGENTS.md`, `.gitignore` additions |

The overwhelming characterization of the source diff is: **`by native_decide` → `by decide` swap in every non-legacy occurrence**, plus route-2 file rename and a couple of unrelated refactors.

## Audit 3 — v1.1 route-terminal transitive axiom check

**Method.** Detached `git worktree add ..\SIDE-kernel-v1.1-audit v1.1` at commit `e0a8ba0`. Same Mathlib pin as HEAD (`e960b84129b3caf423ecf0ea7409a8758a47012c`) so packages could be junction-shared; `.lake/build` created fresh in the worktree (not junctioned) to avoid overwriting HEAD's build artifacts. `lake build`, then `lake build Bridge MetaKernel`, then `lake env lean AxiomAudit.lean` — all succeeded. Worktree removed after audit.

**`#print axioms` output (verbatim):**

```
'structural_exhaustiveness_proved' depends on axioms: [propext,
 Classical.choice,
 Quot.sound,
 seven_classes._native.native_decide.ax_1_1]

'ConservationBridge.riemann_hypothesis' depends on axioms:
 [propext, Classical.choice, Quot.sound]

'SpectralCannonFull.spectral_cannon' depends on axioms:
 [propext, Classical.choice, Quot.sound]

'SIDEKernel.formation' depends on axioms:
 [SIDEKernel.formation._native.native_decide.ax_1_1]

'SIDEKernel.formation_count' depends on axioms:
 [SIDEKernel.formation_count._native.native_decide.ax_1_1]

'DomainOstrowski.formation_count' does not depend on any axioms
```

### Route-by-route verdict (v1.1 tag)

| Terminal | v1.1 axiom profile | Verdict |
|---|---|---|
| Route 1 `structural_exhaustiveness_proved` (top level of `Bridge/TheBridgeComplete.lean`) | `{propext, Classical.choice, Quot.sound, seven_classes._native.native_decide.ax_1_1}` | **DIRTY** at v1.1 |
| Route 2 `SpectralCannonFull.spectral_cannon` (in `Kernel/SpectralCannonFull4.lean` at v1.1) | `{propext, Classical.choice, Quot.sound}` | **CLEAN** at v1.1 |
| Route 3 `ConservationBridge.riemann_hypothesis` | `{propext, Classical.choice, Quot.sound}` | **CLEAN** at v1.1 |
| `SIDEKernel.formation` (bare `2+3+2+0=7` in `Kernel/Core.lean:53`) | `{SIDEKernel.formation._native.native_decide.ax_1_1}` (pure arithmetic, doesn't even need propext/Choice/Quot) | **DIRTY** at v1.1 |
| `SIDEKernel.formation_count` (via `n1..n4` defs in `Kernel/Core.lean:50`) | `{SIDEKernel.formation_count._native.native_decide.ax_1_1}` | **DIRTY** at v1.1 |
| `DomainOstrowski.formation_count` in `MetaKernel.lean:71` | does not depend on any axioms | CLEAN at v1.1 (already used `by decide` at v1.1) |

**Material picture:** Route 1's exposure is transitive via `seven_classes` (line 24 of `Bridge/TheBridgeComplete.lean`), which the terminal explicitly builds into its proof term at line 188–190: `⟨seven_classes, none_produce, ostrowski_exhaustive_prime⟩`. Routes 2 and 3 never touch a native_decide site in their proof-term dependency chain — the only native_decide sites they might have transitively imported (via Bridge/Kernel modules) don't lie on their proof paths at v1.1. So the exposure is precisely: Route 1 + both formation theorems in Core.lean.

## Land — commits pushed to PLACE-papers

Both append-only, UTF-8 no BOM, mirroring the reconciliation and closing landings' style.

- **`FINDINGS.md`**: new entry `### F.2026-07-10-c — Kernel deposit/tree divergence at the formation site (same pattern as the monograph line)` — compact paragraph carrying the audit-verbatim data, the severity calibration (deposit's "0 custom axioms" claim survives because `_native.native_decide.ax_*` are Lean-shipped, but §25.2 and §25.8 concordance items don't verify at v1.1), and the correction to Task C's earlier "MATCH" verdict.
- **`REGISTRY.md`**: new `## Version-log addition — 2026-07-10 (kernel deposit-gate finding; …)` block cross-referencing `F.2026-07-10-c`.
- Commit **`5daa819`** — "Gate finding 2026-07-10: v1.1 kernel deposit carries native_decide at formation site; tree fixed June 11, no re-deposit; v1.2 to ride the v5.5 deposit wave (F.2026-07-10-c)" — diff `2 files changed, 7 insertions(+)`; push `b5e30bd..5daa819  main -> main`.

## Fix-forward sketch (planning; not in ledgers)

Not landed as a FINDINGS entry — this is planning, not a finding. Included in the relay for hand-off.

### What v1.2 contains

The current tree state of `D:\SIDE-kernel`:
- Every `by native_decide` in Lean source replaced with `by decide` (Audit 1 confirms 0 remaining Lean-source occurrences).
- Route 2 file renamed `Kernel/SpectralCannonFull4.lean` → `Kernel/SpectralCannonFull.lean`; scratch test module `SpectralCannonFull4_test.lean` and duplicate `PerpendicularCrossingProbe.lean` removed (housekeeping already flagged in monograph §25.8).
- 4 new files under `Kernel/Cascade/` (Sieve infrastructure); the monograph does not reference these in its axiom claims, so they don't affect route terminals.
- Refactored `Kernel/StructuralCount.lean` (−180 lines) and `MetaKernel.lean` (−80 lines) — content compaction, no new axioms.

### Pre-deposit verification checklist

1. Fresh `lake build` succeeds against the same Mathlib pin (`e960b84…`).
2. `git grep -c "by native_decide" HEAD` returns 0 (Lean sources only — docs may retain prose references).
3. `#print axioms` on:
   - Every route terminal §25.8 names: `structural_exhaustiveness_proved`, `SpectralCannonFull.spectral_cannon`, `ConservationBridge.riemann_hypothesis`, `techne_kernel_integration.rh_from_structural_exhaustiveness`, `techne_kernel_integration.structural_exhaustiveness_iff_rh`, `SIDEKernel.formation`. Each must be `{propext, Classical.choice, Quot.sound}` (or `(none)` for pure-arithmetic `formation`) — matching the monograph's §25.8 table verbatim.
   - Both formation counts (`SIDEKernel.formation`, `SIDEKernel.formation_count`) — expect "does not depend on any axioms".
   - `MetaKernel`'s `DomainOstrowski.formation_count` — expect "does not depend on any axioms" (was already clean at v1.1).
4. Tag `v1.2`, push tag, `git ls-remote origin refs/tags/v1.2 refs/tags/v1.2^{}` to verify tag-object → commit peel matches local `git rev-list -n 1 v1.2`.
5. Zenodo upload of the v1.2 snapshot; new DOI issued; deposit description delta to record.

### Zenodo description delta (draft, ≤2 lines)

> **v1.2 (July 2026).** Eliminates `native_decide` corpus-wide (100+ tactic sites in `Bridge/` and `Kernel/`), replacing with `by decide`; every route terminal in the core now has axiom profile `{propext, Classical.choice, Quot.sound}` — the `Lean.ofReduceBool`-style axioms (`_native.native_decide.ax_*`) present at v1.1 on Route 1 and on `SIDEKernel.formation` are eliminated. Route 2 file rename `Kernel/SpectralCannonFull4.lean` → `Kernel/SpectralCannonFull.lean`; `PerpendicularCrossingProbe.lean` scratch/duplicate removed. No mathematical changes; every theorem statement is byte-identical to v1.1.

### Coordination with monograph v5.5 deposit

Author decision, `DEPOSIT_VERIFICATION_PROTOCOL`-gated: v1.2 kernel deposit and v5.5 monograph deposit ride the same wave, so §25.2's "`decide` … axiom-free" and §25.8's clean concordance table are verifiable against a citable Zenodo record at the moment the paper points to it. The alternative — depositing v5.5 while v1.1 is still the citable kernel — reproduces the F.2026-07-10-a pattern on the outbound direction.

::relay end::
