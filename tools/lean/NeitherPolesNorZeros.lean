/-
  W-CONSTRUCTION-1 act 4 · NeitherPolesNorZeros.lean — THE VANILLA LEG (zero axioms)
  ==================================================================================

  The two-leg ruling governs: this is the VANILLA leg — finite/combinatorial instances,
  vanilla Lean 4 (v4.29.1 pinned), decide/rfl only, expected profile per terminal:
  "does not depend on any axioms". The analytic statements live on the MATHLIB leg
  (LocalLimit.lean, std3). Nothing at complete roster.

  WHAT THIS MODULE COMPILES:
  (1) POLES EXCLUDED BY CONSTRUCTION, the smallest instances: the ball indicator is
      orthogonal to the Sonin basis at (2,1) and (3,1) — the §10 observation's P-side.
  (2) THE FINDING of the lemma's closure: the unit 3 acts as −1 on Son(2,1)
      (U₃f = −f), so the unit-average annihilates it — the ϑ-tail route's failure,
      compiled; radial Sonin vectors do not exist at (2,1).
  (3) ZEROS' ESCAPE, the smallest instance: the level-2 transform of U·f is NONZERO on
      the integers' ball (the value 8ζ⁴ at ball row 4, exact in ℤ[ζ₁₆]) — the CNU
      escape hypothesis's finite shadow at zero axioms.
-/

import TowerInstance

namespace NeitherPolesNorZeros
open TowerInstance

/- ── (1) the ball indicator ⟂ Son, smallest instances ─────────────────────────── -/

/-- (2,1): ball {0,2} in ℤ/4; Son = span(e₁ − e₃): the dot product is 0 -/
theorem ball_orthogonal_21 :
    (1 * 0 + 0 * 1 + 1 * 0 + 0 * (-1) : Int) = 0 := by decide

/-- (3,1): ball {0,3,6} in ℤ/9; the four Sonin columns are supported off it —
    all four dot products with the ball indicator vanish (columns δ_α⊗(e_j−e_{j+1}),
    α ∈ {1,2}, j ∈ {0,1}: supports {1,4}, {4,7}, {2,5}, {5,8} — disjoint from {0,3,6}) -/
theorem ball_orthogonal_31 :
    ([1, 4, 4, 7, 2, 5, 5, 8].all (fun m => m % 3 != 0)) = true := by decide

/- ── (2) the finding: the unit-average annihilates Son(2,1) ───────────────────── -/

/-- the unit-3 scaling on ℤ/4 (m ↦ 3m mod 4) sends f = e₁ − e₃ to −f:
    (U₃f)(m) = f(3m) gives entries (f 0, f 3, f 2, f 1) = (0, −1, 0, 1) = (−1)·f -/
theorem unit_action_neg :
    [(0 : Int), -1, 0, 1] = [(-1 : Int) * 0, -1 * 1, -1 * 0, -1 * -1] := by decide

/-- hence the unit-average (½(f + U₃f)) is zero: radial Sonin vectors do not exist
    at (2,1) — the ϑ-tail route's failure, compiled -/
theorem unit_average_zero :
    ([(0 : Int), 1, 0, -1].zipWith (· + ·) [(0 : Int), -1, 0, 1] = [0, 0, 0, 0]) := by
  decide

/- ── (3) the escape witness in ℤ[ζ₁₆] ────────────────────────────────────────── -/

/-- the level-2 image of U·f (values f(m″ mod 4) on odd m″, scaled): its transform's
    ball row r = 4 equals 8ζ⁴ ≠ 0 — the escape, exact, zero axioms.
    (Support {1,5,9,13} with +1 and {3,7,11,15} with −1; exponents 4·m″ mod 16.) -/
def escapeRow : Z16 :=
  zsum [(1, 4), (1, 20), (1, 36), (1, 52), (-1, 12), (-1, 28), (-1, 44), (-1, 60)]

theorem escape_witness_nonzero :
    escapeRow = term 8 4 ∧ term 8 4 ≠ zero16 := by decide

end NeitherPolesNorZeros
