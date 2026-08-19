/-
  FILE B of the Mathlib companion (opened at the NEXT ERA's first sitting — the
  campaign's standing order governs: one theorem per PR-sized unit; sorries counted
  with owners; the author's hand on review):
  THE p-ADIC FOURIER TRANSFORM ON TEST FUNCTIONS OF ℚ_p.

  DESIGN: the character is a PARAMETER carrying exactly the two properties FILE A
  PROVED (`stdAddChar` an `AddChar ℚ_[p] Circle`; `stdAddChar_eq_one_iff` the
  conductor) — the honest interface, minimal plumbing; file A supplies the instance.
  The Haar measure is a parameter with its invariance class. Mathlib's
  `NumberTheory/Padics/AddChar.lean` is a DIFFERENT object (ℤ_p-characters into
  ultrametric algebras, for Mahler transforms; grep-checked) — no collision.

  UNIT 1 (this sitting): the transform's definition + THE SELF-DUALITY ANCHOR — the
  transform of the indicator of ℤ_p is μ(ℤ_p)·(the indicator of ℤ_p). The member
  branch rides the conductor theorem; the non-member branch rides the translation
  argument with the explicit witness x₀ = p^(m−1).
-/
import Mathlib.MeasureTheory.Measure.Haar.Basic
import Mathlib.MeasureTheory.Integral.Bochner.Set
import Mathlib.NumberTheory.Padics.ProperSpace
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Algebra.Group.AddChar

open MeasureTheory

namespace PadicFourier

variable (p : ℕ) [Fact p.Prime]
variable [MeasurableSpace ℚ_[p]] [BorelSpace ℚ_[p]]
variable (ψ : AddChar ℚ_[p] Circle) (hψ : ∀ x : ℚ_[p], ψ x = 1 ↔ ‖x‖ ≤ 1)
variable (μ : Measure ℚ_[p]) [μ.IsAddHaarMeasure]

/-- the closed unit ball — ℤ_p inside ℚ_p, as the transform's reference set. -/
def zpSet : Set ℚ_[p] := {x : ℚ_[p] | ‖x‖ ≤ 1}

/-- THE TRANSFORM (file B's object): `F f (y) = ∫ f(x) ψ(xy) dμ(x)`. -/
noncomputable def fourier (f : ℚ_[p] → ℂ) (y : ℚ_[p]) : ℂ :=
  ∫ x, f x * (ψ (x * y) : ℂ) ∂μ

/-- UNIT 1a (the member branch — PROVED): for `y ∈ ℤ_p` the transform of the
    indicator of ℤ_p at `y` is `μ(ℤ_p)` — the character is identically 1 on the
    integration set (the CONDUCTOR theorem, file A's target, via `‖xy‖ ≤ ‖x‖‖y‖`). -/
theorem fourier_indicator_zp_mem (hψ : ∀ x : ℚ_[p], ψ x = 1 ↔ ‖x‖ ≤ 1)
    (y : ℚ_[p]) (hy : ‖y‖ ≤ 1) :
    fourier p ψ μ ((zpSet p).indicator 1) y = (μ.real (zpSet p) : ℂ) := by
  unfold fourier
  have hset : ∀ x : ℚ_[p], (zpSet p).indicator (1 : ℚ_[p] → ℂ) x * (ψ (x * y) : ℂ)
      = (zpSet p).indicator (1 : ℚ_[p] → ℂ) x := by
    intro x
    by_cases hx : x ∈ zpSet p
    · have hxy : ‖x * y‖ ≤ 1 := by
        rw [norm_mul]
        exact mul_le_one₀ hx (norm_nonneg _) hy
      rw [(hψ (x * y)).mpr hxy]
      simp [Set.indicator_of_mem hx]
    · simp [Set.indicator_of_notMem hx]
  simp_rw [hset]
  have hzp : MeasurableSet (zpSet p) := by
    have hball : zpSet p = Metric.closedBall (0 : ℚ_[p]) 1 := by
      ext x
      simp [zpSet, Metric.mem_closedBall, dist_eq_norm]
    rw [hball]
    exact measurableSet_closedBall
  have hconst : ((zpSet p).indicator (1 : ℚ_[p] → ℂ))
      = (zpSet p).indicator (fun _ => (1 : ℂ)) := rfl
  rw [hconst, MeasureTheory.integral_indicator_const (1 : ℂ) hzp]
  have hclose : (μ.real (zpSet p)) • (1 : ℂ) = ((μ.real (zpSet p)) : ℂ) := by
    rw [Complex.real_smul, mul_one]
  exact hclose

/-- UNIT 1b (the non-member branch): for `‖y‖ > 1` the transform of the indicator of
    ℤ_p at `y` VANISHES — the translation argument: with `‖y‖ = p^m`, the witness
    `x₀ = p^(m−1) ∈ ℤ_p` has `‖x₀y‖ = p > 1`, so `ψ(x₀y) ≠ 1`; Haar invariance under
    `x ↦ x + x₀` (which preserves ℤ_p) gives `I = ψ(x₀y)·I`, hence `I = 0`.
    SORRY — owner: FILE B, THIS UNIT (the set-integral translation plumbing; the
    mathematics is written in this docstring and is one page). -/
theorem fourier_indicator_zp_not_mem (hψ : ∀ x : ℚ_[p], ψ x = 1 ↔ ‖x‖ ≤ 1)
    (y : ℚ_[p]) (hy : 1 < ‖y‖) :
    fourier p ψ μ ((zpSet p).indicator 1) y = 0 := by
  sorry

end PadicFourier

#print axioms PadicFourier.fourier_indicator_zp_mem
#print axioms PadicFourier.fourier_indicator_zp_not_mem
