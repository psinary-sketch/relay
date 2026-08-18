/-
  W-CONSTRUCTION-1 act 7 · NormalizationForced.lean — THE VANILLA LEG (zero axioms)
  =================================================================================

  The two-leg ruling (Rule 5) governs: VANILLA leg — finite/combinatorial instances,
  vanilla Lean 4 (v4.29.1 pinned), decide only, expected profile per terminal:
  "does not depend on any axioms".

  WHAT THIS MODULE COMPILES — the finite shadow of the normalization question's
  LEVEL joint (act-7 item 2): which per-level normalization is compatible with the
  tower's banked on-the-nose Gram factor?

  The banked input (TowerInstance, cited, not recompiled): the tower inclusion at
  (2,1)→(2,2) scales the Gram by EXACTLY 4 = 2² (the `16ζ⁴ = 4·4ζ⁴` theorem).
  The candidates: normalize by DIMENSION (p^n − 1)² — act 5's registered choice —
  or by VOLUME p^{2n}. The shadow decides between them at the banked cells:

  · the VOLUME ratio per level is exactly p² — it MATCHES the banked Gram factor
    (volume_factor_2, volume_factor_3);
  · the DIMENSION ratio at the smallest cell is 9 ≠ 4 — it does NOT match
    (dim_ratio_not_gram);
  · under the volume normalization the identity coefficient (p^n − 1)²/p^{2n}
    CLIMBS toward 1 (identity_coeff_climbs_2/_3, cross-multiplied exact) — the
    act-5 divergence caveat dissolves in the volume convention.

  (The p = 3 Gram factor is instrument-grade (b21/b23), not vanilla-compiled; the
  p = 3 rows here are the volume/dimension arithmetic only, and the module says so.)
-/

namespace NormalizationForced

/-- the volume ratio per level is exactly p², p = 2: 16 = 4·4 and 64 = 4·16 —
    the match with the banked Gram factor 4 (TowerInstance, cited). -/
theorem volume_factor_2 :
    (2 ^ (2 * 2) = 2 ^ 2 * 2 ^ (2 * 1)) ∧ (2 ^ (2 * 3) = 2 ^ 2 * 2 ^ (2 * 2)) := by
  decide

/-- the volume ratio per level is exactly p², p = 3: 81 = 9·9. -/
theorem volume_factor_3 : (3 ^ (2 * 2) = 3 ^ 2 * 3 ^ (2 * 1)) := by decide

/-- the DIMENSION ratio at the smallest cell is 9, NOT the banked Gram factor 4:
    the dimension normalization is not Gram-compatible at finite level. -/
theorem dim_ratio_not_gram :
    ((2 ^ 2 - 1) ^ 2 ≠ 2 ^ 2 * (2 ^ 1 - 1) ^ 2) ∧ ((2 ^ 2 - 1) ^ 2 = 9) := by decide

/-- under the volume normalization the identity coefficient (p^n−1)²/p^{2n} climbs,
    p = 2 (cross-multiplied exact): 1/4 < 9/16 < 49/64, each < 1. -/
theorem identity_coeff_climbs_2 :
    (1 * 16 < 9 * 4) ∧ (9 * 64 < 49 * 16) ∧ (49 < 64) := by decide

/-- and p = 3: 4/9 < 64/81 < 1. -/
theorem identity_coeff_climbs_3 : (4 * 81 < 64 * 9) ∧ (64 < 81) := by decide

end NormalizationForced
