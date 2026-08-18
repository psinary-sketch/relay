# `W-ATTEMPT-2` · SITTING 22 — THE ARCHIMEDEAN `E₁`
## ### **`(A-third)`, AND THE SPLIT IS THE FINDING: THE CONSTRAINED SECTOR AT `∞` IS EXACTLY THE `+1` EIGENSPACE OF THE TRANSFORM ON THE EVEN SONIN PART (THE `A-yes` HALF, AT MACHINE, WITH THE BANKED FOUR-SECTOR SHAPE EXPLAINED) — WHILE "WEIL'S FAMILY REACHES `E₁`" IS REFUSED STRUCTURALLY, AND THE `σ_max` STATEMENT AND `E₁`-CONTAINMENT ARE NOW MEASURED TO BE DIFFERENT STATEMENTS**

**Relay report · 2026-08-18 (forty-second sitting) · author-called · Fable/proof-search + Opus bench ·
sub-gate declared · the register untouched · nothing deposits · nothing circulates**

> ### **RULE-3 LOG:** *sitting 20's theorems at `5c7279d` ✓ · the keystone draft ✓ ·* ### **the ferry's
> "F_eR² = 1 at CC's eq. (24)": the equation number is NOT banked (grep empty) — NAVIGATOR-ASSERTED,
> carried as such; the IDENTITY was derived longhand first-thing from banked content (`F² = parity`,
> exact at the model and machine on the grid; parity trivial on evens) and that derivation, not the
> citation, is what the registration used.** *The corpus's archimedean anchor: the banked sandwich
> disposition ("the sandwiched form is a NORM", blockage 7). Terms coined: none.*

```
instruments   tools/e16/b32_arch_e1.py (registration banked BEFORE the run) ·
              data/b32_registration_2026-08-18.txt · data/b32_2026-08-18.txt · 220/220 checks
              (float, declared; N ∈ {511, 1023, 2047}; a ∈ {√2, 2, 3})
```

---

## §1 — WHAT LANDED `(A-yes)`: ### **THE `E₁` IDENTITY, AT MACHINE, EVERYWHERE**

1. ### **THE PARITY SPLIT IS EXACT:** *the even Sonin part carries eigenvalues `{+1, −1}` ONLY and the
   odd part `{±i}` only — wrong-sector mass 0 at all nine `(N, a)`, deviations `≤ 10⁻¹⁴`.* ### **AND
   THE BANKED FOUR-SECTOR SHAPE `(n, n, n+1, n)` IS EXPLAINED: the `n+1` sits in the ODD sector; the
   even part is the balanced pair `(n, n)`** *(cross-checked exactly against b20's banked row).*
2. ### **THE PAIRING IS `±‖·‖²` ON THE SECTORS: Rayleigh `+1.000000000000` on the `+1` cluster,
   `−1.000000000000` on the `−1` cluster, real part `0` on the odd control.**
3. ### **DEFINITIONAL = SPECTRAL:** *`rank((1+F)/2)` on the even part equals `d₊` at all nine — the
   T-fixed reading and the eigenspace reading cannot silently diverge; they are one.*

> ### **THE PLACE-UNIFORM SENTENCE, NOW LICENSED AT ITS THREE GRADES:** *"the constrained sector is
> the `E₁` of the local self-dual transform on the Sonin space — POSITIVE BECAUSE `B = ‖·‖²` THERE —
> at every place: PROOF at `p = 2`'s limit (sitting 20), MODEL-EXACT at `p = 3` (the towers), MACHINE
> at `∞` (this sitting, the even part)."* **The diagonal section's constrained-class positivity
> restates place-uniformly: positive because it is the `E₁`-sector at every place, glued. And the
> DOUBLE LIMIT is exactly the gluing of the `E₁`'s at complete roster — the codomain. The keystone
> draft's R4 line is amended accordingly (still DRAFT).**

## §2 — WHAT WAS REFUSED, STRUCTURALLY: ### **"WEIL'S FAMILY REACHES `E₁`" — AND THE NON-CONFLATION IS NOW MEASURED**

*The registered containment reading (largest principal angle, coverage) FAILS at every `a` — angle
`π/2`, coverage `~0` — with the reason measured, not asserted: `W_d` is even but spreads across BOTH
`E₁` and `E₋₁`, and leaks off the Sonin space entirely (ball leak `0.13–0.43`). The smallest
principal angle closes monotonically with degree at every `(a, N)` individually — but its value has
0–2 N-stable digits, below the declared gate: the closing is DATA, the limit value beyond the model's
affordance (b27's own registered limit). The reverse direction mostly has NO domain (soft-faithful
counts 0/1/5; at `a = 2` the single faithful mode is ODD — `GFG` commutes with parity, so `E₁` is
missed structurally).* ### **So sitting 12's `W-exact` (`σ_max → 1` for the SUBSPACE COMPRESSION) and
`E₁`-CONTAINMENT are different statements, and the difference is now measured — the `W-exact` reading
stays exactly what it was banked as, and the `E₁` re-reading of it is WITHDRAWN as refused.**

## §3 — THE MATHLIB COMPANION, SCOPED AS A CONTRIBUTION *(grep-verified at `/d/mathlib4 @ cecd0c4d56`; no code this sitting)*

| file | builds on (verified present) | the statement it must reach | price |
|:--|:--|:--|:--|
| **A — the standard character of `ℚ_p`** | `Padics/AddChar.lean` (characters OF `ℤ_p`, classified — adjacent scaffolding); `Algebra/Group/AddChar`; the `Padics` integer API | `ψ : AddChar ℚ_p Circle`, trivial exactly on `ℤ_p` (the fractional-part construction); the duality `y ↦ ψ(x·y)` | ~1 focused PR |
| **B — Haar + the transform, unitary** | `Padics/ProperSpace` (local compactness); abstract Haar (`Measure/Haar/*`); the fully general `VectorFourier.fourierIntegral` (definition layer READY) | `volume ℤ_p = 1` normalization; `F = fourierIntegral ψ volume`; ### **`F` is an `L²`-isometry with `F⁴ = 1` — REACHED BY THE TOWER ROUTE, NOT LCA PLANCHEREL: `F` acts as the finite DFT on each dense level (the b21 identification), unitary there — the programme's own tower IS the Plancherel proof path for `ℚ_p`** | ~1–2 PRs, gated on A |
| **C — Schwartz–Bruhat** | `Topology/LocallyConstant/*`; `MeasureTheory/Function/ContinuousMapDense` | the space (locally constant, compact support); density in `L²`; `F`-invariance with the level formula — then sitting 20's Q1–Q3 COMPILE (Q2's projections are algebra over `F⁴ = 1`; Q3's SOT lemma is abstract Hilbert space) | ~1 PR |

*Sequenced A → B → C; the contribution is exactly the missing bridge and no more; the programme's two
merged PRs stand as the precedent line (carried at the ferry's cite). What the checkout already
holds that recall had missed: the `ℤ_p`-character classification and `ℂ_p` — neither replaces A–C,
both adjacent.*

## §4 — THE RECORD

*Correspondence rows 59–61 · `FINDINGS` `F.2026-08-18g` · the keystone draft amended (R4; the
place-uniform sentence at its grades; the M4 refusal recorded in the falsifier's own row) · both road
documents' arc lines · the packet current · pins in the closing message.*

**`h2` UNCHANGED. THE REGISTER SENTENCE UNTOUCHED. NOTHING AT COMPLETE ROSTER. NOTHING DEPOSITS.
NOTHING CIRCULATES.**
