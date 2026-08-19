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
import Mathlib.MeasureTheory.Group.Integral
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

/-- UNIT 1b (the non-member branch — PROVED, the era's ruling: no sorry in a kernel):
    for `‖y‖ > 1` the transform of the indicator of ℤ_p at `y` VANISHES — the
    translation argument: with `m = −v(y) ≥ 1`, the witness `x₀ = p^(m−1) ∈ ℤ_p` has
    `‖x₀y‖ = p > 1`, so `ψ(x₀y) ≠ 1`; Haar invariance under `x ↦ x + x₀` (which
    preserves ℤ_p) gives `I = ψ(x₀y)·I`, hence `I = 0`. -/
theorem fourier_indicator_zp_not_mem (hψ : ∀ x : ℚ_[p], ψ x = 1 ↔ ‖x‖ ≤ 1)
    (y : ℚ_[p]) (hy : 1 < ‖y‖) :
    fourier p ψ μ ((zpSet p).indicator 1) y = 0 := by
  haveI : μ.IsAddRightInvariant := inferInstance
  have hy0 : y ≠ 0 := by
    intro h
    rw [h, norm_zero] at hy
    linarith
  have hp1 : (1 : ℝ) < (p : ℝ) := by exact_mod_cast (Fact.out : p.Prime).one_lt
  have hp0 : (p : ℝ) ≠ 0 := by positivity
  set v : ℤ := y.valuation with hv
  have hvneg : v < 0 := by
    by_contra hnn
    push_neg at hnn
    have hle : ‖y‖ ≤ 1 := (Padic.norm_le_one_iff_val_nonneg y).mpr hnn
    linarith
  set m : ℕ := (-v).toNat with hm
  have hm1 : 1 ≤ m := by omega
  have hmv : (m : ℤ) = -v := Int.toNat_of_nonneg (by omega)
  set x₀ : ℚ_[p] := (p : ℚ_[p]) ^ (m - 1) with hx₀
  have hx₀mem : ‖x₀‖ ≤ 1 := by
    rw [hx₀, Padic.norm_p_pow]
    calc (p : ℝ) ^ (-((m - 1 : ℕ) : ℤ)) ≤ (p : ℝ) ^ (0 : ℤ) := by
          apply zpow_le_zpow_right₀ (le_of_lt hp1)
          omega
      _ = 1 := zpow_zero _
  have hx₀y : 1 < ‖x₀ * y‖ := by
    have hxy : ‖x₀ * y‖ = (p : ℝ) ^ (1 : ℤ) := by
      rw [norm_mul, hx₀, Padic.norm_p_pow, Padic.norm_eq_zpow_neg_valuation hy0,
        ← zpow_add₀ hp0]
      congr 1
      have hcast : ((m - 1 : ℕ) : ℤ) = (m : ℤ) - 1 := by
        omega
      rw [hcast]
      omega
    rw [hxy, zpow_one]
    exact hp1
  have hcirc : ψ (x₀ * y) ≠ 1 := fun h1 => (not_le.mpr hx₀y) ((hψ _).mp h1)
  have hchar : (ψ (x₀ * y) : ℂ) ≠ 1 := by
    intro h
    exact hcirc (Subtype.coe_injective (by simpa using h))
  have hind : ∀ x : ℚ_[p], (zpSet p).indicator (1 : ℚ_[p] → ℂ) (x + x₀)
      = (zpSet p).indicator (1 : ℚ_[p] → ℂ) x := by
    intro x
    by_cases hx : x ∈ zpSet p
    · have hmem : x + x₀ ∈ zpSet p :=
        le_trans (Padic.nonarchimedean _ _) (max_le hx hx₀mem)
      simp [Set.indicator_of_mem, hx, hmem]
    · have hnot : x + x₀ ∉ zpSet p := by
        intro hmem
        apply hx
        have hxe : x = (x + x₀) + (-x₀) := by ring
        have hb : ‖(x + x₀) + (-x₀)‖ ≤ 1 :=
          le_trans (Padic.nonarchimedean _ _)
            (max_le hmem (by rwa [norm_neg]))
        rw [hxe]
        exact hb
      simp [Set.indicator_of_notMem, hx, hnot]
  have hadd : ∀ x : ℚ_[p], (ψ ((x + x₀) * y) : ℂ) = (ψ (x * y) : ℂ) * (ψ (x₀ * y) : ℂ) := by
    intro x
    have hsplit : (x + x₀) * y = x * y + x₀ * y := by ring
    rw [hsplit, AddChar.map_add_eq_mul]
    push_cast
    ring
  have key : fourier p ψ μ ((zpSet p).indicator 1) y
      = (ψ (x₀ * y) : ℂ) * fourier p ψ μ ((zpSet p).indicator 1) y := by
    unfold fourier
    calc ∫ x, (zpSet p).indicator (1 : ℚ_[p] → ℂ) x * (ψ (x * y) : ℂ) ∂μ
        = ∫ x, (zpSet p).indicator (1 : ℚ_[p] → ℂ) (x + x₀) * (ψ ((x + x₀) * y) : ℂ) ∂μ :=
          (MeasureTheory.integral_add_right_eq_self
            (μ := μ) (fun x => (zpSet p).indicator (1 : ℚ_[p] → ℂ) x * (ψ (x * y) : ℂ)) x₀).symm
      _ = ∫ x, (ψ (x₀ * y) : ℂ) * ((zpSet p).indicator (1 : ℚ_[p] → ℂ) x * (ψ (x * y) : ℂ)) ∂μ := by
          simp_rw [hind, hadd]
          congr 1
          funext x
          ring
      _ = (ψ (x₀ * y) : ℂ) * ∫ x, (zpSet p).indicator (1 : ℚ_[p] → ℂ) x * (ψ (x * y) : ℂ) ∂μ :=
          MeasureTheory.integral_const_mul ((ψ (x₀ * y) : ℂ))
            (fun x => (zpSet p).indicator (1 : ℚ_[p] → ℂ) x * (ψ (x * y) : ℂ))
  have hzero : (1 - (ψ (x₀ * y) : ℂ)) * fourier p ψ μ ((zpSet p).indicator 1) y = 0 := by
    rw [sub_mul, one_mul]
    rw [← key]
    ring
  rcases mul_eq_zero.mp hzero with h | h
  · exact absurd (by linear_combination -h : (ψ (x₀ * y) : ℂ) = 1) hchar
  · exact h

end PadicFourier

#print axioms PadicFourier.fourier_indicator_zp_mem
#print axioms PadicFourier.fourier_indicator_zp_not_mem
