/-
  W-ATTEMPT-2 · TowerInstance.lean — THE TOWER'S SMALLEST INSTANCE, COMPILED IN ℤ[ζ₁₆]
  ====================================================================================

  ATTEMPT-track, RELAY-RESIDENT. Sitting 18. Vanilla Lean 4 (v4.29.1, pinned), no
  imports, decide/rfl only; expected axiom profile: "does not depend on any axioms".

  WHAT THIS MODULE COMPILES — the ℚ₂ tower's level-1 → level-2 instance, exactly:
  ℤ[ζ₁₆] is modeled as integer 8-tuples mod Φ₁₆(x) = x⁸ + 1 (the fold ζ⁸ = −1). The
  level-1 Sonin vector f = e₁ − e₃ on ℤ/4 embeds as ι(f) on ℤ/16 (the chart refinement
  m″ = 2m + 8j, values copied), and:
    · ι(f) vanishes on the host's integers' ball {0, 4, 8, 12}          (support side);
    · the host transform's BALL ROWS annihilate ι(f): (4F₁₆ · ιf)(r) = 0 in ℤ[ζ₁₆] for
      r ∈ {0, 4, 8, 12} — so ι(Son(2,1)) ⊂ Son(2,2), THE TOWER COMPATIBILITY, exactly
      (banked exact at all levels by b23; here the smallest instance is KERNEL-CHECKED);
    · the isometry's integer form: ‖ιf‖² = 2·‖f‖² (each level point splits into p = 2
      host points; the Haar masses p^{−n−1} vs p^{−n} cancel the factor — documented);
    · THE PAIRING'S LEVEL STABILITY ON THE NOSE: the raw scaled Grams satisfy
      (ιf)ᵀ(4F₁₆)(ιf) = 4 · fᵀ(2F₄)f — computed exactly: 16ζ⁴ = 4·(4ζ⁴), i.e. 16i = 4·4i
      — b23's "host Gram = 4 · level Gram" at its smallest cell, in the kernel;
    · the fifth law's integer identities at levels 1–4, both primes:
      2(2^{n−1}−1)² = 0, 2, 18, 98 and 3(3^{n−1}−1)² = 0, 12, 192, 2028.

  WHAT IT DOES NOT COMPILE, DECLARED: the (3,·) tower instances need ℤ[ζ₈₁] (degree 54)
  and beyond — THE MATHLIB COMPANION'S SPEC IS EXTENDED to the prime-power cyclotomic
  towers ℚ(ζ_{p^k}) (named, not faked; the bench holds them exactly, b26/b29 banked);
  the identification of the fifth-law integers with the measured Q_gen² is bench
  (b23/b26, exact, banked) — this module carries the arithmetic identities; nothing at
  complete roster; no sign. h2 untouched.
-/

namespace TowerInstance

/-- ℤ[ζ₁₆] as integer 8-tuples: coefficients of ζ⁰..ζ⁷, with ζ⁸ = −1 -/
abbrev Z16 := List Int

def zero16 : Z16 := [0, 0, 0, 0, 0, 0, 0, 0]

def add16 (a b : Z16) : Z16 := List.zipWith (· + ·) a b

/-- c · ζ^e, exponent folded mod 16 with the sign rule ζ⁸ = −1 -/
def term (c : Int) (e : Nat) : Z16 :=
  let e16 := e % 16
  let sgn : Int := if e16 < 8 then 1 else -1
  let pos := e16 % 8
  (List.range 8).map fun j => if j == pos then sgn * c else 0

/-- Σ over a list of (coefficient, exponent) pairs -/
def zsum (l : List (Int × Nat)) : Z16 := l.foldl (fun acc p => add16 acc (term p.1 p.2)) zero16

/-- ι(f): support {2, 6, 10, 14} with values (+1, −1, +1, −1) on ℤ/16 -/
def iotaSupp : List (Int × Nat) := [(1, 2), (-1, 6), (1, 10), (-1, 14)]

/-- support-side ball vanishing: the support avoids {0, 4, 8, 12} -/
theorem support_ball_vanish :
    (iotaSupp.all fun p => decide (p.2 % 4 ≠ 0)) = true := by decide

/-- the host transform's ball row r applied to ι(f): Σ_m v_m ζ^{r·m} -/
def ballRow (r : Nat) : Z16 := zsum (iotaSupp.map fun p => (p.1, r * p.2))

/-- TOWER COMPATIBILITY at the smallest instance: every ball row annihilates ι(f) -/
theorem hat_ball_vanish :
    ballRow 0 = zero16 ∧ ballRow 4 = zero16 ∧ ballRow 8 = zero16 ∧
    ballRow 12 = zero16 := by decide

/-- the isometry's integer form: ‖ιf‖² = 2‖f‖² (masses 2^{−n−1} vs 2^{−n} cancel it) -/
theorem iota_isometry_integer :
    (iotaSupp.foldl (fun acc p => acc + p.1 * p.1) 0) = 2 * ((1 : Int) * 1 + (-1) * (-1)) := by
  decide

/-- the host raw Gram: Σ_{m,m′} v_m v_{m′} ζ^{m·m′} over the support -/
def hostGram : Z16 :=
  zsum ((iotaSupp.flatMap fun p => iotaSupp.map fun q => (p.1 * q.1, p.2 * q.2)))

/-- LEVEL STABILITY ON THE NOSE: hostGram = 16ζ⁴ = 4 · (the level Gram 4ζ⁴ = 4i) -/
theorem gram_level_stability :
    hostGram = term 16 4 ∧ term 16 4 = add16 (add16 (term 4 4) (term 4 4))
      (add16 (term 4 4) (term 4 4)) := by decide

/-- the fifth law's integer identities, both primes, levels 1–4 -/
theorem fifth_law_integers :
    2 * (2 ^ 0 - 1) ^ 2 = 0 ∧ 2 * (2 ^ 1 - 1) ^ 2 = 2 ∧
    2 * (2 ^ 2 - 1) ^ 2 = 18 ∧ 2 * (2 ^ 3 - 1) ^ 2 = 98 ∧
    3 * (3 ^ 0 - 1) ^ 2 = 0 ∧ 3 * (3 ^ 1 - 1) ^ 2 = 12 ∧
    3 * (3 ^ 2 - 1) ^ 2 = 192 ∧ 3 * (3 ^ 3 - 1) ^ 2 = 2028 := by decide

end TowerInstance
