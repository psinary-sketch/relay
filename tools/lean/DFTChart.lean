/-
  W-CONSTRUCTION-1 act 14 · DFTChart.lean — THE VANILLA LEG (zero axioms)
  =======================================================================

  The two-leg ruling (Rule 5) governs: VANILLA leg — vanilla Lean 4 (v4.29.1 pinned),
  decide only, expected profile per terminal: "does not depend on any axioms".

  WHAT THIS MODULE COMPILES — the DFT chart's integer core at small N:
  the orthogonality sums behind F² = parity. On the N-grid, (F²)[m,m′] is
  (1/N)·Σ_k ω^{k(m+m′)}; the sum is N·δ (parity) because the fiber map k ↦ k·r mod N
  is UNIFORM: for r coprime to N it hits every residue exactly once (so the ζ-sum is
  1+ζ+…+ζ^{N−1} = 0 in ℤ[ζ_N]), and for r ≡ 0 it hits 0 exactly N times (the sum is
  N). The fiber-count identities below are that statement's integer content, at
  N = 3, 5, 7 — decide, no axioms. (The ζ-reading rides in this comment; the compiled
  content is the counts.)
-/

namespace DFTChart

/-- N = 5: for r ∈ {1,2,3,4} the map k ↦ k·r mod 5 hits each residue exactly once;
    for r = 0 it hits 0 five times. -/
theorem orthogonality_5 :
    (([1, 2, 3, 4].all fun r => (List.range 5).all fun i =>
        ((List.range 5).map (fun k => k * r % 5)).count i == 1) &&
     (((List.range 5).map (fun k => k * 0 % 5)).count 0 == 5)) = true := by decide

/-- N = 3: the same fiber uniformity. -/
theorem orthogonality_3 :
    (([1, 2].all fun r => (List.range 3).all fun i =>
        ((List.range 3).map (fun k => k * r % 3)).count i == 1) &&
     (((List.range 3).map (fun k => k * 0 % 3)).count 0 == 3)) = true := by decide

/-- N = 7: the same. -/
theorem orthogonality_7 :
    (([1, 2, 3, 4, 5, 6].all fun r => (List.range 7).all fun i =>
        ((List.range 7).map (fun k => k * r % 7)).count i == 1) &&
     (((List.range 7).map (fun k => k * 0 % 7)).count 0 == 7)) = true := by decide

/-- the parity involution's index core: negation mod N is an involution fixing 0,
    N = 3, 5, 7 — the F² = parity target's index map. -/
theorem parity_involution :
    (((List.range 5).all fun m => (5 - (5 - m % 5) % 5) % 5 == m % 5) &&
     ((List.range 3).all fun m => (3 - (3 - m % 3) % 3) % 3 == m % 3) &&
     ((List.range 7).all fun m => (7 - (7 - m % 7) % 7) % 7 == m % 7)) = true := by
  decide

end DFTChart
