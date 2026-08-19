/-
  THE NEXT ERA, opening sitting · OddPInstances.lean — THE VANILLA LEG (zero axioms)
  ==================================================================================

  The two-leg ruling (Rule 5) governs: VANILLA leg — vanilla Lean 4 (v4.29.1 pinned),
  decide only, expected profile per terminal: "does not depend on any axioms".

  WHAT THIS MODULE COMPILES — the odd-p instances of the all-p theorems (theorem-first:
  the general statement is PROVED on the Mathlib leg, `general_p_no_fixed_cell`; these
  are its decide shadows at the new cells, extending TraceSilence's p = 2, 3):

  · trace silence at (5,1), (5,2), (7,1): no cell α ∈ [1, p^n) has α(p^k−1) ≡ 0 mod p^n;
  · the Sonin dimensions and the ball-pair inclusion–exclusion at (7,1), (7,2).
-/

namespace OddPInstances

/-- (5,1): k = 1 — and (5,2): k = 1,2 — no fixed cell. -/
theorem trace_silence_5 :
    ((((List.range 5).drop 1).all fun a => a * (5 ^ 1 - 1) % 5 != 0) &&
     ([1, 2].all fun k => ((List.range 25).drop 1).all
       fun a => a * (5 ^ k - 1) % 25 != 0)) = true := by decide

/-- (7,1): k = 1 — no fixed cell. -/
theorem trace_silence_7 :
    (((List.range 7).drop 1).all fun a => a * (7 ^ 1 - 1) % 7 != 0) = true := by decide

/-- the Sonin dimension's inclusion–exclusion at the odd cells:
    (5,1): 16 = 25−10+1 · (7,1): 36 = 49−14+1 · (7,2): 2304 = 2401−98+... -/
theorem sonin_dims_odd :
    (5 ^ 2 - 2 * 5 + 1 = (5 - 1) ^ 2) ∧ (7 ^ 2 - 2 * 7 + 1 = (7 - 1) ^ 2) ∧
    (7 ^ 4 - 2 * 7 ^ 2 + 1 = (7 ^ 2 - 1) ^ 2) := by decide

end OddPInstances
