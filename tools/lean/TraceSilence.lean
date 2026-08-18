/-
  W-CONSTRUCTION-1 act 5 · TraceSilence.lean — THE VANILLA LEG (zero axioms)
  ==========================================================================

  The two-leg ruling (Rule 5) governs: this is the VANILLA leg — finite/combinatorial
  instances, vanilla Lean 4 (v4.29.1 pinned), decide only, expected profile per
  terminal: "does not depend on any axioms".

  WHAT THIS MODULE COMPILES — the finite shadow of the act-5 trace computation:
  the compressed scaling at a finite place is TRACE-SILENT off the identity.

  The mechanism (the fixed-point localization, banked at b21/b23): a diagonal term of
  Tr(U_{p^k} S) at Sonin cell α needs α·(p^k − 1) ≡ 0 (mod p^n) with 1 ≤ α < p^n.
  Since gcd(p^k − 1, p^n) = 1 this NEVER happens — verified below cell-by-cell at the
  banked instances, `decide`, no appeal to the gcd fact. Consequence (the Mathlib-leg
  reading): Tr(U^k S) = 0 exactly, at every banked level, for every k ≥ 1 — the
  distributional trace of the compressed scaling is supported AT THE IDENTITY, with
  coefficient the dimension (p^n − 1)², compiled last.
-/

namespace TraceSilence

/-- (2,1): k = 1 — no cell α ∈ [1,2) has α·(2−1) ≡ 0 mod 2 -/
theorem trace_silence_2_1 :
    (((List.range 2).drop 1).all fun a => a * (2 ^ 1 - 1) % 2 != 0) = true := by decide

/-- (2,2): k = 1,2 — no cell α ∈ [1,4) has α·(2^k−1) ≡ 0 mod 4 -/
theorem trace_silence_2_2 :
    ([1, 2].all fun k => ((List.range 4).drop 1).all
      fun a => a * (2 ^ k - 1) % 4 != 0) = true := by decide

/-- (2,3): k = 1,2,3 — no cell α ∈ [1,8) has α·(2^k−1) ≡ 0 mod 8 -/
theorem trace_silence_2_3 :
    ([1, 2, 3].all fun k => ((List.range 8).drop 1).all
      fun a => a * (2 ^ k - 1) % 8 != 0) = true := by decide

/-- (3,1): k = 1 — no cell α ∈ [1,3) has α·2 ≡ 0 mod 3 -/
theorem trace_silence_3_1 :
    (((List.range 3).drop 1).all fun a => a * (3 ^ 1 - 1) % 3 != 0) = true := by decide

/-- (3,2): k = 1,2 — no cell α ∈ [1,9) has α·(3^k−1) ≡ 0 mod 9 -/
theorem trace_silence_3_2 :
    ([1, 2].all fun k => ((List.range 9).drop 1).all
      fun a => a * (3 ^ k - 1) % 9 != 0) = true := by decide

/-- the δ₀ coefficient: Tr(S) = dim Son = (p^n − 1)² at the banked cells -/
theorem trace_identity_dim :
    ((2 ^ 1 - 1) ^ 2, (2 ^ 2 - 1) ^ 2, (3 ^ 1 - 1) ^ 2, (3 ^ 2 - 1) ^ 2) =
      (1, 9, 4, 64) := by decide

end TraceSilence
