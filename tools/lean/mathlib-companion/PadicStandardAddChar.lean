/-
  FILE A of the Mathlib companion (the sitting-22 scope; opened at W-CONSTRUCTION-1 act 2):
  THE STANDARD ADDITIVE CHARACTER OF ℚ_p, WITH CONDUCTOR ℤ_p.

  STATE: COMPLETE at act 5 — ZERO sorries. The spec, the additivity (via the
  p-power-denominator integrality bridge), and the target are PROVED; the terminal
  prints the classical profile {propext, Classical.choice, Quot.sound} for all three,
  no sorryAx. The campaign's precedent note governs the PR path: one statement per PR,
  the author's own hand in review responses. Compiled against the local Mathlib build
  (checkout cecd0c4d56, toolchain v4.30.0-rc1).

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

/-- the membership: in the nontrivial case, x * p^k is a p-adic integer (named so the
    definition and the theorems share one proof term). -/
theorem mul_pow_mem (x : ℚ_[p]) (hk : fracExponent p x ≠ 0) :
    ‖x * (p : ℚ_[p]) ^ fracExponent p x‖ ≤ 1 := by
  have hv : x.valuation < 0 := by
    have h1 : ¬(-x.valuation ≤ 0) := fun hle =>
      hk (by simp [fracExponent, Int.toNat_eq_zero.mpr hle])
    omega
  have hx0 : x ≠ 0 := by
    intro h
    rw [h, Padic.valuation_zero] at hv
    exact absurd hv (lt_irrefl 0)
  have hnn : (0 : ℤ) ≤ -x.valuation := by omega
  have hke : (fracExponent p x : ℤ) = -x.valuation := by
    unfold fracExponent
    exact Int.toNat_of_nonneg hnn
  have hp0 : (p : ℝ) ≠ 0 := by
    exact_mod_cast (Fact.out : p.Prime).ne_zero
  rw [norm_mul, Padic.norm_eq_zpow_neg_valuation hx0, Padic.norm_p_pow,
    ← zpow_add₀ hp0, hke]
  simp

/-- the p-power fractional part: the rational m / p^k (m the mod-p^k approximation of
    x*p^k in Z_p) -- the canonical representative of x mod Z_p in [0, 1) with p-power
    denominator. -/
noncomputable def padicFract (x : ℚ_[p]) : ℚ :=
  if hk : fracExponent p x = 0 then 0
  else
    (((PadicInt.toZModPow (fracExponent p x))
        ⟨x * (p : ℚ_[p]) ^ (fracExponent p x), mul_pow_mem p x hk⟩).val : ℚ) /
      (p : ℚ) ^ (fracExponent p x)

/-- the defining property: x minus its fractional part is a p-adic integer. -/
theorem padicFract_spec (x : ℚ_[p]) : ‖x - ((padicFract p x : ℚ) : ℚ_[p])‖ ≤ 1 := by
  by_cases hk : fracExponent p x = 0
  · rw [padicFract, dif_pos hk]
    push_cast
    rw [sub_zero, Padic.norm_le_one_iff_val_nonneg]
    have h1 := Int.toNat_eq_zero.mp hk
    omega
  · rw [padicFract, dif_neg hk]
    haveI hne : NeZero (p ^ fracExponent p x) :=
      ⟨pow_ne_zero _ (Fact.out : p.Prime).ne_zero⟩
    set k := fracExponent p x with hkdef
    set y : ℤ_[p] := ⟨x * (p : ℚ_[p]) ^ k, mul_pow_mem p x hk⟩ with hy
    set m : ℕ := ((PadicInt.toZModPow k) y).val with hm
    have hker : y - (m : ℤ_[p]) ∈ Ideal.span {(p : ℤ_[p]) ^ k} := by
      rw [← PadicInt.ker_toZModPow]
      rw [RingHom.mem_ker, map_sub, map_natCast, hm]
      rw [ZMod.natCast_rightInverse _]
      exact sub_self _
    have hnorm : ‖y - (m : ℤ_[p])‖ ≤ (p : ℝ) ^ (-(k : ℤ)) :=
      (PadicInt.norm_le_pow_iff_mem_span_pow _ _).mpr hker
    have hpk0 : ((p : ℚ_[p]) ^ k) ≠ 0 := by
      apply pow_ne_zero
      exact_mod_cast (Fact.out : p.Prime).ne_zero
    have hx_eq : x - (((m : ℚ) / (p : ℚ) ^ k : ℚ) : ℚ_[p]) =
        ((y : ℚ_[p]) - (m : ℚ_[p])) * ((p : ℚ_[p]) ^ k)⁻¹ := by
      push_cast [hy]
      field_simp
    rw [hx_eq, norm_mul, norm_inv, Padic.norm_p_pow]
    have hyq : ‖(y : ℚ_[p]) - (m : ℚ_[p])‖ ≤ (p : ℝ) ^ (-(k : ℤ)) := by
      have : ((y - (m : ℤ_[p]) : ℤ_[p]) : ℚ_[p]) = (y : ℚ_[p]) - (m : ℚ_[p]) := by
        push_cast
        ring
      rw [← this]
      exact_mod_cast hnorm
    calc ‖(y : ℚ_[p]) - (m : ℚ_[p])‖ * ((p : ℝ) ^ (-(k : ℤ)))⁻¹
        ≤ (p : ℝ) ^ (-(k : ℤ)) * ((p : ℝ) ^ (-(k : ℤ)))⁻¹ := by
          apply mul_le_mul_of_nonneg_right hyq
          positivity
      _ = 1 := mul_inv_cancel₀ (zpow_ne_zero _ (by
          exact_mod_cast (Fact.out : p.Prime).ne_zero))

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

/-- every fractional part is a p-power fraction a / p^k. -/
theorem padicFract_denpow (x : ℚ_[p]) :
    ∃ (a : ℤ) (k : ℕ), padicFract p x = (a : ℚ) / (p : ℚ) ^ k := by
  unfold padicFract
  split
  · exact ⟨0, 0, by simp⟩
  · rename_i hk
    exact ⟨((((PadicInt.toZModPow (fracExponent p x))
        ⟨x * (p : ℚ_[p]) ^ (fracExponent p x), mul_pow_mem p x hk⟩).val : ℕ) : ℤ),
      fracExponent p x, by push_cast; rfl⟩

/-- THE BRIDGE: a rational with p-power denominator that is p-adically integral is an
    integer (the p-adic bound forces p^K to divide the numerator). -/
theorem int_of_denpow_of_norm_le_one (d : ℚ) (A : ℤ) (K : ℕ)
    (hd : d = (A : ℚ) / (p : ℚ) ^ K) (hn : ‖((d : ℚ) : ℚ_[p])‖ ≤ 1) :
    ∃ n : ℤ, d = (n : ℚ) := by
  have hp0Q : (p : ℚ) ≠ 0 := by
    exact_mod_cast (Fact.out : p.Prime).ne_zero
  have hp0P : (p : ℚ_[p]) ≠ 0 := by
    exact_mod_cast (Fact.out : p.Prime).ne_zero
  have hcast : ((A : ℤ) : ℚ_[p]) = ((d : ℚ) : ℚ_[p]) * (p : ℚ_[p]) ^ K := by
    rw [hd]
    push_cast
    field_simp
  have hA : ‖((A : ℤ) : ℚ_[p])‖ ≤ (p : ℝ) ^ (-(K : ℤ)) := by
    rw [hcast, norm_mul, Padic.norm_p_pow]
    calc ‖((d : ℚ) : ℚ_[p])‖ * (p : ℝ) ^ (-(K : ℤ))
        ≤ 1 * (p : ℝ) ^ (-(K : ℤ)) := by
          apply mul_le_mul_of_nonneg_right hn
          positivity
      _ = (p : ℝ) ^ (-(K : ℤ)) := one_mul _
  obtain ⟨B, hB⟩ := (Padic.norm_int_le_pow_iff_dvd A K).mp hA
  refine ⟨B, ?_⟩
  rw [hd, hB]
  push_cast
  field_simp

/-- THE STANDARD ADDITIVE CHARACTER ψ : ℚ_p → Circle, ψ(x) = e^{2πi·frac_p(x)}. -/
noncomputable def stdAddChar : AddChar ℚ_[p] Circle where
  toFun x := Circle.exp (2 * Real.pi * (padicFract p x : ℝ))
  map_zero_eq_one' := by
    have h0 : padicFract p 0 = 0 :=
      padicFract_eq_zero_of_norm_le_one p 0 (by simp)
    simp [h0]
  map_add_eq_mul' := by
    intro x y
    show Circle.exp (2 * Real.pi * (padicFract p (x + y) : ℝ)) =
      Circle.exp (2 * Real.pi * (padicFract p x : ℝ)) *
        Circle.exp (2 * Real.pi * (padicFract p y : ℝ))
    rw [← Circle.exp_add, Circle.exp_eq_exp]
    obtain ⟨a₁, k₁, h₁⟩ := padicFract_denpow p (x + y)
    obtain ⟨a₂, k₂, h₂⟩ := padicFract_denpow p x
    obtain ⟨a₃, k₃, h₃⟩ := padicFract_denpow p y
    have hp0Q : (p : ℚ) ≠ 0 := by
      exact_mod_cast (Fact.out : p.Prime).ne_zero
    set d : ℚ := padicFract p (x + y) - padicFract p x - padicFract p y with hdd
    have hA : d = ((a₁ * p ^ (k₂ + k₃) - a₂ * p ^ (k₁ + k₃) - a₃ * p ^ (k₁ + k₂) : ℤ) : ℚ) /
        (p : ℚ) ^ (k₁ + k₂ + k₃) := by
      rw [hdd, h₁, h₂, h₃]
      push_cast
      field_simp
      ring
    have tri : ∀ (u v : ℚ_[p]), ‖u‖ ≤ 1 → ‖v‖ ≤ 1 → ‖u + v‖ ≤ 1 := fun u v hu hv =>
      le_trans (Padic.nonarchimedean u v) (max_le hu hv)
    have hnorm : ‖((d : ℚ) : ℚ_[p])‖ ≤ 1 := by
      have e : ((d : ℚ) : ℚ_[p]) =
          ((x - ((padicFract p x : ℚ) : ℚ_[p])) + (y - ((padicFract p y : ℚ) : ℚ_[p]))) +
            (-((x + y) - ((padicFract p (x + y) : ℚ) : ℚ_[p]))) := by
        rw [hdd]
        push_cast
        ring
      rw [e]
      apply tri
      · exact tri _ _ (padicFract_spec p x) (padicFract_spec p y)
      · rw [norm_neg]
        exact padicFract_spec p (x + y)
    obtain ⟨n, hn⟩ := int_of_denpow_of_norm_le_one p d _ _ hA hnorm
    refine ⟨n, ?_⟩
    have hreal : (padicFract p (x + y) : ℝ) =
        (padicFract p x : ℝ) + (padicFract p y : ℝ) + (n : ℝ) := by
      have hq : padicFract p (x + y) = padicFract p x + padicFract p y + (n : ℚ) := by
        rw [hdd] at hn
        linarith
      exact_mod_cast hq
    rw [hreal]
    ring

@[simp] theorem stdAddChar_apply (x : ℚ_[p]) :
    stdAddChar p x = Circle.exp (2 * Real.pi * (padicFract p x : ℝ)) := rfl

/-- THE FILE'S TARGET: ψ is trivial exactly on the p-adic integers (conductor ℤ_p). -/
theorem stdAddChar_eq_one_iff (x : ℚ_[p]) : stdAddChar p x = 1 ↔ ‖x‖ ≤ 1 := by
  constructor
  · intro h
    rw [stdAddChar_apply] at h
    have hexp : Circle.exp (2 * Real.pi * (padicFract p x : ℝ)) = Circle.exp 0 := by
      rw [Circle.exp_zero]
      exact h
    obtain ⟨m, hm⟩ := Circle.exp_eq_exp.mp hexp
    have hpi : (0 : ℝ) < 2 * Real.pi := by positivity
    have hf : (padicFract p x : ℝ) = (m : ℝ) := by
      have h2 : 2 * Real.pi * (padicFract p x : ℝ) = 2 * Real.pi * (m : ℝ) := by
        rw [hm]
        ring
      exact mul_left_cancel₀ (ne_of_gt hpi) h2
    have hfq : padicFract p x = (m : ℚ) := by exact_mod_cast hf
    have hm0 : m = 0 := by
      have h1 : (0 : ℚ) ≤ (m : ℚ) := hfq ▸ padicFract_nonneg p x
      have h2 : ((m : ℚ) : ℚ) < 1 := hfq ▸ padicFract_lt_one p x
      have h1' : (0 : ℤ) ≤ m := by exact_mod_cast h1
      have h2' : m < 1 := by exact_mod_cast h2
      omega
    have h0 : padicFract p x = 0 := by
      rw [hfq, hm0]
      norm_num
    have hs := padicFract_spec p x
    rw [h0] at hs
    simpa using hs
  · intro h
    rw [stdAddChar_apply, padicFract_eq_zero_of_norm_le_one p x h]
    simp

end PadicCompanion

/- the profile print (the classical profile expected: propext, Classical.choice, Quot.sound) -/
#print axioms PadicCompanion.padicFract_spec
#print axioms PadicCompanion.stdAddChar
#print axioms PadicCompanion.stdAddChar_eq_one_iff
