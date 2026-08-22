/-
  THE VALUE ACT'S DECIDED CORE · ValueShadow.lean
  ================================================

  Ferry 2026-08-21 (b81). Vanilla Lean 4 (v4.29.1 pinned), no imports; expected
  profile per terminal: "does not depend on any axioms".

  Closure-sequence step five — the sign mechanism's two-fixed-point ledger at
  its decidable core. THE EQUAL-MAGNITUDE LEMMA: the quarter-turn is linear, so
  its linearization at every fixed point is the one matrix J = [[0,−1],[1,0]];
  det(I − J) = 2, point-independent — stationary weights cannot differ between
  the origin and the center; the finite twin: both banked contributions carry
  magnitude exactly q (equal pair-norms) at every banked place-2 cell. THE
  FINITE LEDGER: (q,0) + (0,q) = (q,q) — the banked trace q(1+i) — with the
  balance components equal, the plus orientation's instance. THE LEDGER SUMS AT
  UNIT NORMALIZATION: the plus orientation gives (1,1), the conjugate gives
  (1,−1) = √2·e^{−iπ/4}'s exact ℤ[i] value, norm² = 2, the two sums
  conjugation-swapped and distinct. The ARCHIMEDEAN reading of the conjugate
  sum is CONDITIONAL — the decomposition clause (named) and [UNDER H-COH-∞] —
  and lives in the bank and report, never in this kernel; the balance (row 44)
  is the TARGET, consumed nowhere (the circularity gate).
  Bank: relay data/b81_value.txt.
-/

namespace ValueShadow

/-- THE EQUAL-MAGNITUDE LEMMA's arithmetic: det(I − J) = 2 for the
    quarter-turn's (point-independent) linearization, and the finite twin —
    equal pair-norms for the two banked contributions at every banked place-2
    cell -/
theorem equal_magnitude_lemma :
    ((1 - 0)*(1 - 0) - (0 - (-1))*(0 - 1) = (2 : Int)) ∧
    ((2:Int)*2 + 0*0 = 0*0 + 2*2) ∧ ((4:Int)*4 + 0*0 = 0*0 + 4*4) ∧
    ((8:Int)*8 + 0*0 = 0*0 + 8*8) ∧ ((16:Int)*16 + 0*0 = 0*0 + 16*16) := by
  decide

/-- THE FINITE TWIN: the two-point ledger sums to the banked trace with the
    balance components equal — (q,0) + (0,q) = (q,q) at the four banked
    place-2 cells (the plus orientation's instance of the one ledger law) -/
theorem finite_twin_instances :
    ((2:Int) + 0, (0:Int) + 2) = ((2:Int), (2:Int)) ∧
    ((4:Int) + 0, (0:Int) + 4) = ((4:Int), (4:Int)) ∧
    ((8:Int) + 0, (0:Int) + 8) = ((8:Int), (8:Int)) ∧
    ((16:Int) + 0, (0:Int) + 16) = ((16:Int), (16:Int)) := by decide

def pconj (u : Int × Int) : Int × Int := (u.1, -u.2)

/-- THE LEDGER SUMS at unit normalization: the plus orientation's sum (1,1)
    and the conjugate orientation's sum (1,−1) — the exact ℤ[i] value of
    √2·e^{−iπ/4} — with norm² = 2, conjugation-swapped and distinct (the
    archimedean reading of the conjugate sum is conditional and bank-resident) -/
theorem ledger_sum_conjugate :
    ((1:Int) + 0, (0:Int) + 1) = ((1:Int), (1:Int)) ∧
    ((1:Int) + 0, (0:Int) + (-1)) = ((1:Int), (-1:Int)) ∧
    ((1:Int)*1 + (-1:Int)*(-1) = 2) ∧
    pconj (1, 1) = ((1, -1) : Int × Int) ∧
    ((1, 1) : Int × Int) ≠ (1, -1) := by decide

end ValueShadow
