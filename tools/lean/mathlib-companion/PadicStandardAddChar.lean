/-
  FILE A of the Mathlib companion (the sitting-22 scope; opened at W-CONSTRUCTION-1 act 2):
  THE STANDARD ADDITIVE CHARACTER OF ℚ_p, WITH CONDUCTOR ℤ_p.

  STATE: STARTED — the construction is real (the p-power fractional part via toZModPow),
  the statements are the file's targets, the hard proofs are `sorry` and SAID SO. The
  campaign's precedent note governs: one statement per PR, the author's own hand in
  review responses. This draft compiles (elaborates) against the local Mathlib build
  (checkout cecd0c4d56, toolchain v4.30.0-rc1); nothing here is claimed proved.

  Target statement: `stdAddChar_eq_one_iff` — ψ is trivial exactly on ℤ_p.
-/
import Mathlib.NumberTheory.Padics.PadicIntegers
import Mathlib.NumberTheory.Padics.RingHoms
import Mathlib.Analysis.SpecialFunctions.Complex.Circle
import Mathlib.Algebra.Group.AddChar

namespace PadicCompanion

variable (p : ℕ) [Fact p.Prime]

/-- the exponent of the fractional part: k = max(0, −v_p(x)) -/
noncomputable def fracExponent (x : ℚ_[p]) : ℕ := (-(x.valuation)).toNat

/-- the p-power fractional part: the rational m / p^k (m the mod-p^k approximation of
    x·p^k ∈ ℤ_p) — the canonical representative of x mod ℤ_p in [0, 1) ∩ ℤ[1/p]. -/
noncomputable def padicFract (x : ℚ_[p]) : ℚ :=
  if _hk : fracExponent p x = 0 then 0
  else
    (((PadicInt.toZModPow (fracExponent p x))
        ⟨x * (p : ℚ_[p]) ^ (fracExponent p x), by
          have hv : x.valuation < 0 := by
            have h1 : ¬(-x.valuation ≤ 0) := fun hle =>
              _hk (by simp [fracExponent, Int.toNat_eq_zero.mpr hle])
            omega
          have hx0 : x ≠ 0 := by
            intro h
            rw [h, Padic.valuation_zero] at hv
            exact absurd hv (lt_irrefl 0)
          have hnn : (0 : ℤ) ≤ -x.valuation := by omega
          have hk : (fracExponent p x : ℤ) = -x.valuation := by
            unfold fracExponent
            exact Int.toNat_of_nonneg hnn
          have hp0 : (p : ℝ) ≠ 0 := by
            exact_mod_cast (Fact.out : p.Prime).ne_zero
          rw [norm_mul, Padic.norm_eq_zpow_neg_valuation hx0, Padic.norm_p_pow,
            ← zpow_add₀ hp0, hk]
          simp⟩).val : ℚ) /
      (p : ℚ) ^ (fracExponent p x)

/-- the defining property: x minus its fractional part is a p-adic integer. -/
theorem padicFract_spec (x : ℚ_[p]) : ‖x - ((padicFract p x : ℚ) : ℚ_[p])‖ ≤ 1 := by
  sorry

theorem padicFract_nonneg (x : ℚ_[p]) : 0 ≤ padicFract p x := by
  unfold padicFract
  split
  · exact le_refl 0
  · positivity

theorem padicFract_lt_one (x : ℚ_[p]) : padicFract p x < 1 := by
  have hppos : (0 : ℚ) < (p : ℚ) ^ fracExponent p x := by
    have := (Fact.out : p.Prime).pos
    positivity
  haveI hne : NeZero (p ^ fracExponent p x) :=
    ⟨pow_ne_zero _ (Fact.out : p.Prime).ne_zero⟩
  unfold padicFract
  split
  · norm_num
  · rw [div_lt_one hppos]
    exact_mod_cast ZMod.val_lt _

theorem padicFract_eq_zero_of_norm_le_one (x : ℚ_[p]) (h : ‖x‖ ≤ 1) :
    padicFract p x = 0 := by
  have hv : 0 ≤ x.valuation := (Padic.norm_le_one_iff_val_nonneg x).mp h
  have hk : fracExponent p x = 0 := by
    unfold fracExponent
    exact Int.toNat_eq_zero.mpr (by omega)
  unfold padicFract
  simp [hk]

/-- THE STANDARD ADDITIVE CHARACTER ψ : ℚ_p → Circle, ψ(x) = e^{2πi·frac_p(x)}. -/
noncomputable def stdAddChar : AddChar ℚ_[p] Circle where
  toFun x := Circle.exp (2 * Real.pi * (padicFract p x : ℝ))
  map_zero_eq_one' := by
    have h0 : padicFract p 0 = 0 :=
      padicFract_eq_zero_of_norm_le_one p 0 (by simp)
    simp [h0]
  map_add_eq_mul' := by sorry

/-- THE FILE'S TARGET: ψ is trivial exactly on the p-adic integers (conductor ℤ_p). -/
theorem stdAddChar_eq_one_iff (x : ℚ_[p]) : stdAddChar p x = 1 ↔ ‖x‖ ≤ 1 := by
  sorry

end PadicCompanion
