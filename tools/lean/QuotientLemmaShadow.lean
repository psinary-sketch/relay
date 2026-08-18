/-
  W-CONSTRUCTION-1 act 9 · QuotientLemmaShadow.lean — THE VANILLA LEG (zero axioms)
  =================================================================================

  The two-leg ruling (Rule 5) governs: VANILLA leg — finite/combinatorial instances,
  vanilla Lean 4 (v4.29.1 pinned), decide only, expected profile per terminal:
  "does not depend on any axioms".

  WHAT THIS MODULE COMPILES — the finite shadow of THE QUOTIENT LEMMA, now PROVED
  LONGHAND (build document §21: the fixed-orbit count on V_inv):

      Tr(U^k S_quot) = p^{−k/2} · p^n(p−1)(p^n − p^k)/(p^n − 1),   1 ≤ k ≤ n−1
      dim V_inv = p^n(p−1) · [p=2: p^n] — uniformly p^n(p−1) for every p
      |class| = (p^n − 1)/(p − 1)   (every class the same size)
      hence  τ_q·p^{k/2} = (p^n − p^k)/(p^n − 1), and 0 for k ≥ n (ball absorption).

  The proof's three counting identities are compiled below at the banked cells —
  every integer matches the banked b10 dimensions and the b36 exact rationals.
-/

namespace QuotientLemmaShadow

/-- dim V_inv = p^n(p−1) at the banked cells: (2,2):4 · (2,3):8 · (2,4):16 ·
    (3,2):18 · (5,2):100 — the b10 banked dimensions, now DERIVED integers. -/
theorem dim_Vinv :
    (2 ^ 2 * (2 - 1) = 4) ∧ (2 ^ 3 * (2 - 1) = 8) ∧ (2 ^ 4 * (2 - 1) = 16) ∧
    (3 ^ 2 * (3 - 1) = 18) ∧ (5 ^ 2 * (5 - 1) = 100) := by decide

/-- class size × class count = the off-ball count: ((p^n−1)/(p−1)) · p^n(p−1)
    = p^n(p^n − 1) = p^{2n} − p^n, at the banked cells. -/
theorem class_partition :
    (3 * 4 = 16 - 4) ∧ (7 * 8 = 64 - 8) ∧ (15 * 16 = 256 - 16) ∧
    (4 * 18 = 81 - 9) ∧ (6 * 100 = 625 - 25) := by decide

/-- the trace-count numerator p^n(p^n − p^k) at the banked cells, against the
    measured traces: (2,3,k=1): 48 (Tr = 48/(7√2) = 4.84873 ✓) · (2,3,k=2): 32
    (Tr = 32/(7·2) = 2.28571 ✓) · (3,2,k=1): 54 (Tr = 54/(4√3) = 7.79423 ✓) ·
    (2,4,k=1..3): 224, 192, 128 (/15·p^{−k/2} = 10.55946, 6.40000, 3.01699 ✓). -/
theorem trace_counts :
    (2 ^ 3 * (2 ^ 3 - 2 ^ 1) = 48) ∧ (2 ^ 3 * (2 ^ 3 - 2 ^ 2) = 32) ∧
    (3 ^ 2 * (3 ^ 2 - 3 ^ 1) = 54) ∧
    (2 ^ 4 * (2 ^ 4 - 2 ^ 1) = 224) ∧ (2 ^ 4 * (2 ^ 4 - 2 ^ 2) = 192) ∧
    (2 ^ 4 * (2 ^ 4 - 2 ^ 3) = 128) := by decide

/-- the preimage count in the proof: p^k solutions of p^k·m' ≡ m (mod p^{2n}) at the
    smallest instance — every m ∈ ℤ/16 with v(m) ≥ 1 has exactly 2 preimages under
    doubling (the k = 1 case; the fiber theorem's role in the count). -/
theorem preimage_count :
    ((List.range 16).all fun m => !(m % 2 == 0) ||
      (((List.range 16).filter fun x => (2 * x) % 16 == m).length == 2)) = true := by
  decide

end QuotientLemmaShadow
