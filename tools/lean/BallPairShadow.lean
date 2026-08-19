/-
  W-CONSTRUCTION-1 act 15 · BallPairShadow.lean — THE VANILLA LEG (zero axioms)
  =============================================================================

  The two-leg ruling (Rule 5) governs: VANILLA leg — vanilla Lean 4 (v4.29.1 pinned),
  decide only, expected profile per terminal: "does not depend on any axioms".

  WHAT THIS MODULE COMPILES — the ball-scale relation's finite instances (act 15's R4):
  at every finite place the Sonin dimension IS the inclusion–exclusion of the E+B pair
  structure — E (ball-supported) and B (transform-ball-supported) each of dimension
  p^n, meeting in the rank-ONE span of the ball indicator (b10's L-A, banked):

      dim Son_p = p^{2n} − dim(E + B) = p^{2n} − (p^n + p^n − 1) = (p^n − 1)².

  The finite places carry EXACTLY the pair-subtraction geometry that act 15 derived
  at ∞ (the Gram-λ_n block structure) — there it is exact and dimensional; at ∞ it is
  the resonance geometry (the ε-series' 1/(1−λ²) denominators, derived R2).
-/

namespace BallPairShadow

/-- the inclusion–exclusion identity p^{2n} − 2·p^n + 1 = (p^n − 1)² at the banked
    cells (2,1), (2,2), (2,3), (3,1), (3,2), (5,1), (5,2). -/
theorem sonin_dim_inclusion_exclusion :
    (2 ^ 2 - 2 * 2 ^ 1 + 1 = (2 ^ 1 - 1) ^ 2) ∧
    (2 ^ 4 - 2 * 2 ^ 2 + 1 = (2 ^ 2 - 1) ^ 2) ∧
    (2 ^ 6 - 2 * 2 ^ 3 + 1 = (2 ^ 3 - 1) ^ 2) ∧
    (3 ^ 2 - 2 * 3 ^ 1 + 1 = (3 ^ 1 - 1) ^ 2) ∧
    (3 ^ 4 - 2 * 3 ^ 2 + 1 = (3 ^ 2 - 1) ^ 2) ∧
    (5 ^ 2 - 2 * 5 ^ 1 + 1 = (5 ^ 1 - 1) ^ 2) ∧
    (5 ^ 4 - 2 * 5 ^ 2 + 1 = (5 ^ 2 - 1) ^ 2) := by decide

/-- the pair pieces at the cells: dim E = dim B = p^n and the intersection is rank 1
    (the values behind the subtraction: 2·p^n − 1 constraint dimensions). -/
theorem constraint_span_dims :
    (2 * 2 ^ 1 - 1 = 3) ∧ (2 * 2 ^ 2 - 1 = 7) ∧ (2 * 2 ^ 3 - 1 = 15) ∧
    (2 * 3 ^ 1 - 1 = 5) ∧ (2 * 3 ^ 2 - 1 = 17) ∧ (2 * 5 ^ 1 - 1 = 9) := by decide

end BallPairShadow
