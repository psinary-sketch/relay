/-
  W-CONSTRUCTION-1 act 8 · QuotientWeilShape.lean — THE VANILLA LEG (zero axioms)
  ===============================================================================

  The two-leg ruling (Rule 5) governs: VANILLA leg — finite/combinatorial instances,
  vanilla Lean 4 (v4.29.1 pinned), decide only, expected profile per terminal:
  "does not depend on any axioms".

  WHAT THIS MODULE COMPILES — the finite shadow of act 8's structure finding:

  THE QUOTIENT COEFFICIENT'S CLOSED FORM (b36, data grade — verified EXACTLY at all
  seven banked cells, |d| ≤ 2e−7 float; the longhand proof a NAMED LEMMA, not claimed):

      τ_q(p,n,k) · p^{k/2} = (p^n − p^k)/(p^n − 1)   for k < n;   0 for k ≥ n.

  So the quotient channel's weight is the Weil weight times (p^n − p^k)/(p^n − 1),
  which CLIMBS TO 1 as the level deepens: the quotient channel converges to Weil's
  coefficients at the level limit — at the model, said as data + exact arithmetic.

  What decide reaches: (1) the closed form's numerators/denominators at the banked
  cells are the exact integers behind the measured rationals; (2) the climb toward 1,
  cross-multiplied; (3) the k ≥ n support edge — the scaling absorbs everything into
  the ball after n steps (the recurrence closing into the identity).
-/

namespace QuotientWeilShape

/-- the banked cells' exact fractions: (p^n − p^k, p^n − 1) at the seven cells —
    (2,2,1): 2/3 · (2,3,1): 6/7 · (2,3,2): 4/7 · (3,2,1): 6/8 ·
    (2,4,1): 14/15 · (2,4,2): 12/15 · (2,4,3): 8/15 -/
theorem closed_form_integers :
    (2 ^ 2 - 2 ^ 1 = 2) ∧ (2 ^ 2 - 1 = 3) ∧
    (2 ^ 3 - 2 ^ 1 = 6) ∧ (2 ^ 3 - 2 ^ 2 = 4) ∧ (2 ^ 3 - 1 = 7) ∧
    (3 ^ 2 - 3 ^ 1 = 6) ∧ (3 ^ 2 - 1 = 8) ∧
    (2 ^ 4 - 2 ^ 1 = 14) ∧ (2 ^ 4 - 2 ^ 2 = 12) ∧ (2 ^ 4 - 2 ^ 3 = 8) ∧
    (2 ^ 4 - 1 = 15) := by decide

/-- the climb to 1 at k = 1, p = 2 (cross-multiplied): 2/3 < 6/7 < 14/15 < 1 -/
theorem shape_climbs_2 :
    (2 * 7 < 6 * 3) ∧ (6 * 15 < 14 * 7) ∧ (14 < 15) := by decide

/-- the climb at p = 3, k = 1: 6/8 < 24/26 < 1  ((3³−3)/(3³−1) = 24/26) -/
theorem shape_climbs_3 :
    (3 ^ 3 - 3 = 24) ∧ (3 ^ 3 - 1 = 26) ∧ (6 * 26 < 24 * 8) ∧ (24 < 26) := by decide

/-- the k ≥ n support edge: after n steps the scaling lands in the ball — every
    m ∈ ℤ/p^{2n} has p^n·m ≡ 0 mod p^n (banked cells (2,2) and (3,1)): the
    recurrence closes into the identity, and the quotient trace is 0 there
    (b10's banked zeros; this is the mechanism's decide shadow). -/
theorem ball_absorption :
    (((List.range 16).all fun m => (4 * m) % 16 % 4 == 0) &&
     ((List.range 9).all fun m => (3 * m) % 9 % 3 == 0)) = true := by decide

end QuotientWeilShape
