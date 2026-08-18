/-
  W-ATTEMPT-2 · StaircaseAddresses.lean — THE PRIME-POWER-ADDRESS LAW, COMPILED
  ============================================================================

  ATTEMPT-track, RELAY-RESIDENT. Sitting 17 (the identities compiled). Vanilla Lean 4
  (v4.29.1, pinned), no imports, decide/rfl only; expected axiom profile for every
  terminal: "does not depend on any axioms".

  WHAT THIS MODULE COMPILES — the finite identity: over the place set {2, 3, 5} and the
  integer squared-bound grid A = a² ∈ [1, 145], with the staircase n_p(A) = #{k ≥ 1 :
  p^k ≤ A} (the diagonal's cutoff law, = the T1 boundary "p^k enters at a = √(p^k)"):

    · THE ADDRESS LAW: the diagonal's cell changes at A exactly when A is a prime power
      p^k of a place in the set — every punctuation address is a prime-power address
      (the sawtooth's teeth, the arrival edges, the deepening steps: one address law).
    · THE WEIGHT-DEATH LAW: the fifth-law mass Q²(p, n) = p(p^{n−1} − 1)² is alive at
      bound A exactly when A ≥ p² — every place enters DEAD at its arrival (n = 1) and
      its weight channel first lives at the SECOND power's arrival.
    · THE PRIME-FREE WINDOW: no address lies in [1, 2) ∪ (1, 2) grid-form — A = 1 is
      prime-power-free; the first address is A = 2 (CC's (1/2, 2) window boundary, the
      T1 row's own derivation, here as integer arithmetic).
    · the apex instances L ∈ {4, 16, 64} of the banked two-branch law are prime-power
      addresses (cross-reference: the lag-form sawtooth's peaks at L = 2^{2m}; the
      identification of the two axes is a READING at content, banked at the sitting-16
      table — this module compiles only the address arithmetic, not the identification).

  WHAT IT DOES NOT COMPILE, DECLARED: nothing at complete roster (the place set is
  {2,3,5}, the grid is finite); no statement about any ledger, any sign, or the
  Hypothesis; the class-death instances live in SectorArithmetic.lean (they need the
  banked eigen-dims); the SIDE-window apex/window terminals are cross-referenced in
  intent, not imported. h2 is untouched by every line.
-/

namespace StaircaseAddresses

/-- the staircase: n_p(A) = #{k ∈ [1, 8] : p^k ≤ A} (k ≤ 8 suffices for A ≤ 145) -/
def stair (p A : Nat) : Nat :=
  (List.range 8).foldl (fun acc k => if p ^ (k + 1) ≤ A then acc + 1 else acc) 0

/-- the diagonal's cell at bound A over the place set {2, 3, 5} -/
def cell (A : Nat) : Nat × Nat × Nat := (stair 2 A, stair 3 A, stair 5 A)

/-- A is a prime-power address of the place set -/
def isAddr (A : Nat) : Bool :=
  ([2, 3, 5].any fun p => (List.range 8).any fun k => p ^ (k + 1) == A)

/-- the address-law checker over the grid [2, 145] -/
def addrLawOK : Bool :=
  ((List.range 144).map (· + 2)).all fun A =>
    (decide (cell A ≠ cell (A - 1))) == isAddr A

/-- THE ADDRESS LAW: the cell changes at A ⟺ A is a prime-power address (grid [2,145]) -/
theorem address_law : addrLawOK = true := by decide

/-- the fifth-law mass Q²(p, n) = p(p^{n−1} − 1)²  (n = 0: no live factor, mass 0) -/
def Qsq (p n : Nat) : Nat :=
  match n with
  | 0 => 0
  | Nat.succ m => p * (p ^ m - 1) ^ 2

/-- every place enters DEAD: Q²(p, 1) = 0 for each place -/
theorem arrival_dead : Qsq 2 1 = 0 ∧ Qsq 3 1 = 0 ∧ Qsq 5 1 = 0 := by decide

/-- the weight-death checker: Q²(p, n_p(A)) > 0 ⟺ p² ≤ A, over the grid and the places -/
def weightLawOK : Bool :=
  ((List.range 145).map (· + 1)).all fun A =>
    [2, 3, 5].all fun p => (decide (0 < Qsq p (stair p A))) == decide (p ^ 2 ≤ A)

/-- THE WEIGHT-DEATH LAW: the weight channel of p lives at A ⟺ A ≥ p² -/
theorem weight_death_law : weightLawOK = true := by decide

/-- the prime-free window: A = 1 carries no address; the first address is A = 2 -/
theorem prime_free_window : isAddr 1 = false ∧ isAddr 2 = true := by decide

/-- the banked two-branch apexes L = 4, 16, 64 are prime-power addresses (instances) -/
theorem apexes_are_addresses :
    isAddr 4 = true ∧ isAddr 16 = true ∧ isAddr 64 = true := by decide

/-- the first live full weight on {∞,2,3}: both finite channels alive first at A = 9 -/
theorem full_weight_first_alive :
    (0 < Qsq 2 (stair 2 9) ∧ 0 < Qsq 3 (stair 3 9)) ∧
    ¬(0 < Qsq 2 (stair 2 8) ∧ 0 < Qsq 3 (stair 3 8)) := by decide

end StaircaseAddresses
