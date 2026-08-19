/-
  THE h2 LINE, overlooked item 3 · H1Mechanism.lean — THE VANILLA LEG (zero axioms)
  =================================================================================

  The two-leg ruling (Rule 5) governs: VANILLA leg — vanilla Lean 4 (v4.29.1 pinned),
  decide only, expected profile per terminal: "does not depend on any axioms".

  WHAT THIS MODULE COMPILES — the h = 1 sign mechanism's decide core (b31, 95/95,
  relay df3c426; the instance nearest RH proper in the federation):

  Over ℚ (class number 1) the coupling is the SCALAR a_N = 1 — exactly one ideal of
  norm N, the generator unique up to units (mutual divisibility in the positives) —
  and the constrained form collapses to B(v,v) = ‖v‖²·a_N = ‖v‖²: A SUM OF SQUARES.
  The h = 3 contrast (K = ℚ(√−23): the coupling spectrum (4,1,1) at norm 6/150) is
  CITED, not compiled here: the class structure organizes, never signs (charter
  §8(iii)). NOTHING AT COMPLETE ROSTER: these are the banked cells' shadows.
-/

namespace H1Mechanism

/-- one ideal per norm over ℚ, the integer core: in the positives, mutual
    divisibility pins the generator — #{m ∈ [1..N] : m ∣ N ∧ N ∣ m} = 1 at the
    banked norms N = 6, 36, 150 (so a_6 = a_36 = a_150 = 1: the coupling scalar). -/
theorem one_ideal_per_norm :
    ((((List.range 7).drop 1).filter fun m => (6 % m == 0) && (m % 6 == 0)).length == 1) &&
    ((((List.range 37).drop 1).filter fun m => (36 % m == 0) && (m % 36 == 0)).length == 1) &&
    ((((List.range 151).drop 1).filter fun m => (150 % m == 0) && (m % 150 == 0)).length == 1)
      = true := by decide

/-- the collapsed form is a sum of squares: at the banked sample vectors (integer
    coordinates on the {2:1,3:1}-cell shapes) B(v,v) = Σ vᵢ² > 0 for v ≠ 0 —
    the sign at h = 1 is the positivity of a sum of squares, at no axioms. -/
theorem h1_form_sum_of_squares :
    ([[1, 0], [0, 1], [1, 1], [2, -1], [3, 2], [-1, 4]].all fun v =>
      (v.foldl (fun s x => s + x * x) 0 > 0)) = true := by decide

end H1Mechanism
