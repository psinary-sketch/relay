/-
  FILE D of the Mathlib companion (opened at W-CONSTRUCTION-1 act 9):
  THE QUOTIENT LEMMA'S CORE COUNT.

  STATE: STATED, one labeled sorry. The lemma is PROVED LONGHAND (build document
  THE_GLOBAL_SECTION.md §21: the fixed-orbit count on V_inv — the class structure
  (p^{n−1} units per class, size (p^n−1)/(p−1), count p^n(p−1)), the preimage count
  (p^k per admissible m), and the assembly). Its finite shadow is VANILLA-LEG at zero
  axioms (QuotientLemmaShadow.lean — every integer matches the banked b10/b36 values).
  THE OWNER of this file's single sorry: the longhand proof's formalization.

  Consequence once formalized: the quotient trace's closed form
  τ_q(p,n,k)·p^{k/2} = (p^n − p^k)/(p^n − 1) → 1, i.e. the quotient channel converges
  to Weil's coefficients at the level limit — at proof grade end to end.
-/
import Mathlib.Data.ZMod.Basic

namespace QuotientCount

/-- THE CORE COUNT (proved longhand, build document §21): the number of pairs
    (m, m') in ℤ/p^{2n} with p^k·m' = m and m off-ball (¬ p^n ∣ m.val) is exactly
    p^n(p^n − p^k), for 1 ≤ k < n. The sorry STANDS; owner: the longhand proof's
    formalization. -/
theorem offball_scaling_pair_count (p n k : ℕ) [Fact p.Prime]
    [NeZero (p ^ (2 * n))] (h1 : 1 ≤ k) (hkn : k < n) :
    (Finset.univ.filter fun mm : ZMod (p ^ (2 * n)) × ZMod (p ^ (2 * n)) =>
      (p : ZMod (p ^ (2 * n))) ^ k * mm.2 = mm.1 ∧ ¬ (p ^ n ∣ mm.1.val)).card
      = p ^ n * (p ^ n - p ^ k) := by
  sorry

end QuotientCount

#print axioms QuotientCount.offball_scaling_pair_count
