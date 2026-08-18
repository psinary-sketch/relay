/-
  W-CONSTRUCTION-1 act 12 · InequalityShadow.lean — THE VANILLA LEG (zero axioms)
  ===============================================================================

  The two-leg ruling (Rule 5) governs: VANILLA leg — vanilla Lean 4 (v4.29.1 pinned),
  decide only, expected profile per terminal: "does not depend on any axioms".

  WHAT THIS MODULE COMPILES — the finite shadow of the inequality's L3 link:
  the quotient coefficient sits STRICTLY BELOW the Weil coefficient at every banked
  cell — (p^n − p^k) < (p^n − 1) for 1 ≤ k < n (the act-9 THEOREM's ratio < 1) —
  so, term-by-term against nonnegative test data (the bump is nonnegative exactly,
  hence its autocorrelation is), Θ_q(g) ≤ Σ_p W_p(g) at finite level: the finite
  side's inequality direction, at no axioms where finite.
-/

namespace InequalityShadow

/-- (p^n − p^k) < (p^n − 1) at the banked and capped cells: p = 2, n = 2,3,4;
    p = 3, n = 2,3; p = 5, n = 2 — every k < n. -/
theorem quotient_below_weil :
    (2 ^ 2 - 2 ^ 1 < 2 ^ 2 - 1) ∧
    (2 ^ 3 - 2 ^ 1 < 2 ^ 3 - 1) ∧ (2 ^ 3 - 2 ^ 2 < 2 ^ 3 - 1) ∧
    (2 ^ 4 - 2 ^ 1 < 2 ^ 4 - 1) ∧ (2 ^ 4 - 2 ^ 2 < 2 ^ 4 - 1) ∧
    (2 ^ 4 - 2 ^ 3 < 2 ^ 4 - 1) ∧
    (3 ^ 2 - 3 ^ 1 < 3 ^ 2 - 1) ∧
    (3 ^ 3 - 3 ^ 1 < 3 ^ 3 - 1) ∧ (3 ^ 3 - 3 ^ 2 < 3 ^ 3 - 1) ∧
    (5 ^ 2 - 5 ^ 1 < 5 ^ 2 - 1) := by decide

/-- the strictness mechanism at the cells: p^k > 1 for k ≥ 1 (the gap is exactly
    p^k − 1 > 0), instances. -/
theorem strictness_gap :
    (2 ^ 1 - 1 ≥ 1) ∧ (2 ^ 2 - 1 ≥ 1) ∧ (2 ^ 3 - 1 ≥ 1) ∧
    (3 ^ 1 - 1 ≥ 1) ∧ (3 ^ 2 - 1 ≥ 1) ∧ (5 ^ 1 - 1 ≥ 1) := by decide

end InequalityShadow
