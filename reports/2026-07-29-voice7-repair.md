# Voice7 C₇ repair — 2026-07-29

Repair (not relabel) of the C₇ Hadamard voice: the core-terminal statement-read found
`techne_kernel_voice7.c7_forces_half` concludes `σ = σ` — a tautology under a claiming name — while landed
RH-rail Correspondence rows cite it as forcing σ = ½. Author ruled repair; rail-adjacent edits authorized.

## Pre-flight — both repos clean (interrupted attempt made no edits)

- SIDE-kernel: `derivative-engine` `27a3ae7`, only the untracked scratch `AxiomCheck_PF_v1_5.lean`.
- PLACE-papers: `2c4af9f`, no working changes.

## STEP 1 — the Voice7 module, verbatim, and the determination

`D:\SIDE-kernel\Kernel\Voice7.lean` (at HEAD), every declaration:

```lean
namespace techne_kernel_voice7
def topological_contribution (_sigma : Real) : Real := 0     -- the σ-carrying "contribution": a := 0 stand-in
theorem topological_constant (sigma1 sigma2 : Real) :
    topological_contribution sigma1 = topological_contribution sigma2 := by
  unfold topological_contribution; rfl
theorem topological_no_sigma_preference (sigma : Real) :
    topological_contribution sigma = topological_contribution (1 / 2 : Real) := by
  unfold topological_contribution; rfl
def topological_rests (sigma : Real) : Prop := topological_contribution sigma = 0
theorem c7_rests_at_half : topological_rests (1 / 2 : Real) := by
  unfold topological_rests topological_contribution; rfl
theorem c7_rests_everywhere (sigma : Real) : topological_rests sigma := by
  unfold topological_rests topological_contribution; rfl
theorem c7_forces_half (sigma : Real) :
    topological_rests sigma -> sigma = sigma := by
  intro _; rfl
theorem c7_no_placement_force (sigma : Real) :
    topological_contribution sigma = topological_contribution (1 / 2 : Real) :=
  topological_no_sigma_preference sigma
end techne_kernel_voice7
```

**Determination: a genuine σ-neutrality statement IS provable — and already exists.** `topological_contribution := 0` is σ-constant by construction, so "the contribution is constant in σ" is genuinely proved twice: `topological_constant` and `topological_no_sigma_preference`. **But it is σ-neutrality of the definition-encoded stand-in** (`:= 0` *assigns* it), not derived from ξ's Hadamard product — as the module's own 2026-07-22 docstring states. `c7_forces_half` is the one tautology (`σ = σ`). Per the author's corrected branch: **add nothing** (a `c7_sigma_neutral` would over-name the stand-in again); deprecate `c7_forces_half` in place; cite `topological_constant` for the stand-in.

## STEP 2b — the Voice4 the core read left out

**There is no `Kernel/Voice4.lean` module.** The C₄ voice lives in `Bridge/TheBridgeComplete.lean`, verbatim:

```lean
-- Voice 4 (C4): Modular. …
theorem voice4_modular : completedRiemannZeta₀ = completedRiemannZeta₀ := rfl   -- decorative f = f
-- Voice 5 (C₄ Modular): PSL₂(ℤ) S-action fixed point at 1/2
theorem voice4_S_fixed (σ : Real) : 1 - σ = σ ↔ σ = 1 / 2 := by
  constructor <;> intro h <;> linarith                                          -- genuine forcing (used in exclusion, :181)
```
plus the cited kernel terminal `techne_kernel_voice5.modular_forces_half (σ) : S_action σ = σ → σ = 1/2`.

**Determination: C₄'s σ-forcing is DERIVED, not definition-encoded** — carried by `voice4_S_fixed` (`1−σ=σ ↔ σ=½`, load-bearing in the `produces_offline`/exclusion proof at `:181`) and by the cited `voice5.modular_forces_half`. **Anomaly observed (reported, not edited):** `voice4_modular : completedRiemannZeta₀ = completedRiemannZeta₀ := rfl` is a decorative `f = f` tautology — a lesser sibling of `c7_forces_half` — but it is **not** a claiming name (it asserts no σ-forcing) and is **cited by no Correspondence row**. No work-order needed; no C₄ Correspondence row over-states. Noted.

## Verify-at-source catch — W-ORD-C7-WITNESS is CLOSED, not open

The ruling's cell text (and the module's 2026-07-22 docstring) said the faithful C₇ derivation is "the open work-order **W-ORD-C7-WITNESS**." **This is stale.** The corpus (OPEN_TRAILS ~1764) records it **compiled 2026-07-24 as `Voice7Witness.hadamard_does_not_enforce_online`** (SIDE-kernel `Kernel/Voice7Witness.lean`, axiom-free, DERIVES; `691295b`, an ancestor of HEAD). Verified at source — the statement is genuine and non-vacuous:

```lean
theorem hadamard_does_not_enforce_online :
    ¬ ∃ D : Config → Prop, RespectsI hadIndist D ∧ ∀ z, D z ↔ allOnLine z
```
(the Hadamard observable cannot enforce on-line placement — the Epstein countermodel). **W-ORD-C7-WITNESS is closed-by-compile.** I corrected the rows to cite this faithful terminal (DERIVES) rather than propagate the stale "open" framing — this is exactly the second-order lesson (STEP 4) hitting the pass itself.

## Actions taken

**STEP 2 (kernel, `SIDE-kernel` `75668a0`):** `c7_forces_half` **deprecated in place** — docstring names the finding (conclusion `σ=σ`, tautology; claiming name retired; do not cite; faithful content is the compiled `Voice7Witness.hadamard_does_not_enforce_online`; `topological_constant` is the stand-in). Statement + proof unchanged; nothing removed (papers reference it); Voice7 build green.

**STEP 3 (rows, rail-adjacent — author-ruled go; `PLACE` `0696797`):**
- **(a) SURROUND §4** — C₇ recast as **σ-neutral, not a σ=½ identification**; cites `Voice7Witness.hadamard_does_not_enforce_online` (DERIVES) + `topological_constant` (ENCODES-CONCLUSION, stand-in); non-reliance clause added (Route 3 via `balance_theorem`, exhaustiveness via `produces_offline`'s Hadamard case).
- **(b) SIMPLICITY** — **no target.** SIMPLICITY does **not** cite `voice7.c7_forces_half` (its C₇ references are the Hadamard-product structure). My earlier core-read report over-stated this; corrected here. Untouched.
- **(c) PATHS §fixed-point-algebra note** — count fixed **five → four** (C₁/C₃/C₄/C₅; C₇ removed); C₇ named a σ-neutral stand-in with its faithful discriminator compiled; **inherited-error provenance** recorded (the retired §25.5a matrix's C₇ row read "vacuous (constant function)" while its summary counted C₇ among five — the summary was propagated, the row was not).
- **REGISTRY** `1.5a-6` row — C₇ citation corrected to match.

**STEP 4:** OPEN_TRAILS entry "C₇ Hadamard voice: tautological terminal retired; PATHS fixed-point count corrected" (finding, actions, W-ORD-C7-WITNESS closed-by-compile, the STEP-2b `voice4_modular` observation, residual-hygiene trigger). FINDINGS `F.2026-07-29-c` — the standing rule (**a downgrade must produce a repair or a named work-order; a label alone does not close a finding**) + the second-order lesson (**salvaged summaries must be checked against their detail**, with the meta-instance: this pass nearly propagated the stale "open work-order" summary).

## Pins + rail note

- SIDE-kernel `derivative-engine` — **`75668a0`** (local = remote).
- PLACE-papers `main` — **`0696797`** (local = remote, clean).
- **RH rail (authorized deviation):** SURROUND + PATHS now carry a diff vs `67da789` — **by the author's explicit rail-adjacent authorization** for the C₇ correction (each: 1 insertion / 1 deletion). RESIDUE + `A_Place_to_Stand` + SIMPLICITY remain **empty-diff** (untouched). This is the first authorized break of the rail-untouched invariant; reported as authorized, not a violation.

Deprecation not removal (papers referenced `c7_forces_half`; and deprecate-in-place was the author's instruction). No content invented. Nothing deposited.
