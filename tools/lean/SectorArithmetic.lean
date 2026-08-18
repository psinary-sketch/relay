/-
  W-ATTEMPT-2 · SectorArithmetic.lean — THE FLATNESS SOLVER AND THE TWIST SIGNATURE
  =================================================================================

  ATTEMPT-track, RELAY-RESIDENT. Sitting 17. Vanilla Lean 4 (v4.29.1, pinned), no
  imports, decide/rfl only; expected axiom profile: "does not depend on any axioms".

  WHAT THIS MODULE COMPILES — two finite identity families over ℤ:

  (c) THE FLATNESS THEOREM-SHAPE FOR ODD p (the p = 3 instances, n = 1..4): from
      M² = Π (certified) the eigenvalues lie in {1, −1, i, −i} and the four trace
      equations determine the dims. With the MEASURED inputs tr M = 0 (rational — the
      field-intersection argument ℚ(ζ_{3^{2n}}) ∩ ℚ(i) = ℚ forces Im tr M = 0; stated
      here, compiled at the instance level) and tr Π = 0 (Π fixed-point-free at odd q),
      the unique solution is FLAT: d_λ = (3ⁿ − 1)²/4 each. The solver and its
      uniqueness (the four equations hold and pin the solution) are compiled per level.

  (d) THE TWIST SIGNATURE: with the BANKED exact eigen-dims of the six certified factors
      ((2,1) = (0,0,1,0) · (3,1) = (1,1,1,1) · (2,2) = (2,2,3,2) · (2,3) = (12,12,13,12)
      · (3,2) = (16,16,16,16) · (5,1) = (4,4,4,4) — sittings 7/9/10, exact arithmetic,
      relay pins 36345da/8129e0f), the glued real-sector counts give the pairing's
      signature at every banked staircase cell: (pos, neg, zero) = (d/4, d/4, d/2)
      EXACTLY, with the pre-cell {2:1} the whole-zero block (0, 0, d) — and pos = neg
      at every cell. The a = √2 cell's operator instance is already compiled
      (DiagonalSection.twisted_hermitian_cell); this is the combinatorial signature law
      across the cells the exact benches certified.

  WHAT IT DOES NOT COMPILE, DECLARED: the eigen-dims enter as BANKED DATA (their exact
  derivation is the b20/b22/b23/b26 registrations, banked before their runs); nothing at
  complete roster; no sign of anything ledger-side. h2 untouched.
-/

namespace SectorArithmetic

/- ── (c) the flatness solver ─────────────────────────────────────────────────── -/

/-- the four trace equations' unique solution:
    d₁ = (dim + trΠ + 2·reM)/4, d₋₁ = (dim + trΠ − 2·reM)/4,
    dᵢ = (dim − trΠ + 2·imM)/4, d₋ᵢ = (dim − trΠ − 2·imM)/4 -/
def solve (dim trPi reM imM : Int) : Int × Int × Int × Int :=
  ((dim + trPi + 2 * reM) / 4, (dim + trPi - 2 * reM) / 4,
   (dim - trPi + 2 * imM) / 4, (dim - trPi - 2 * imM) / 4)

/-- the equations hold at the solution (the verification half of uniqueness) -/
abbrev solves (dim trPi reM imM d1 dm1 di dmi : Int) : Prop :=
  d1 + dm1 + di + dmi = dim ∧ d1 + dm1 - di - dmi = trPi ∧
  d1 - dm1 = reM ∧ di - dmi = imM

/-- FLATNESS at p = 3, n = 1..4: with tr M = 0 and tr Π = 0 (measured, exact), the
    solution is (q, q, q, q) with q = (3ⁿ−1)²/4 — and it solves the system -/
theorem flat_n1 : solve 4 0 0 0 = (1, 1, 1, 1) ∧ solves 4 0 0 0 1 1 1 1 := by decide
theorem flat_n2 : solve 64 0 0 0 = (16, 16, 16, 16) ∧ solves 64 0 0 0 16 16 16 16 := by
  decide
theorem flat_n3 : solve 676 0 0 0 = (169, 169, 169, 169) ∧
    solves 676 0 0 0 169 169 169 169 := by decide
theorem flat_n4 : solve 6400 0 0 0 = (1600, 1600, 1600, 1600) ∧
    solves 6400 0 0 0 1600 1600 1600 1600 := by decide

/-- the p = 2 contrast at its banked instances: tr M = i, tr Π = −1 give the banked
    non-flat dims (n = 1, 2, 3): (0,0,1,0) · (2,2,3,2) · (12,12,13,12) -/
theorem p2_instances :
    solve 1 (-1) 0 1 = (0, 0, 1, 0) ∧ solve 9 (-1) 0 1 = (2, 2, 3, 2) ∧
    solve 49 (-1) 0 1 = (12, 12, 13, 12) := by decide

/- ── (d) the twist signature at the banked cells ─────────────────────────────── -/

/-- eigen-dims as exponent-indexed 4-tuples: component e ↔ eigenvalue i^e -/
abbrev E4 := Nat × Nat × Nat × Nat

def e21 : E4 := (0, 1, 0, 0)   -- (2,1): d_i = 1 (i = i^1)
def e31 : E4 := (1, 1, 1, 1)
def e22 : E4 := (2, 3, 2, 2)   -- (2,2): (d₁,dᵢ,d₋₁,d₋ᵢ) = (2,3,2,2) at e = 0,1,2,3
def e23 : E4 := (12, 13, 12, 12)
def e32 : E4 := (16, 16, 16, 16)
def e51 : E4 := (4, 4, 4, 4)

def get (t : E4) (e : Nat) : Nat :=
  if e % 4 == 0 then t.1 else if e % 4 == 1 then t.2.1
  else if e % 4 == 2 then t.2.2.1 else t.2.2.2

/-- glued sector mass at total eigen-exponent e over one or more factors, ×3 (ℂ[Cl]) -/
def sig1 (a : E4) (e : Nat) : Nat := 3 * get a e
def sig2 (a b : E4) (e : Nat) : Nat :=
  3 * ((List.range 4).foldl (fun acc x => acc + get a x * get b ((e + 4 - x) % 4)) 0)
def sig3 (a b c : E4) (e : Nat) : Nat :=
  3 * ((List.range 4).foldl (fun acc x =>
    acc + get a x * ((List.range 4).foldl (fun ac y =>
      ac + get b y * get c ((e + 8 - x - y) % 4)) 0)) 0)

/-- the signature law at every banked staircase cell: (pos, neg, zero) = (d/4, d/4, d/2)
    — pos at e = 0, neg at e = 2, zero at e ∈ {1, 3} — and the pre-cell is (0, 0, d) -/
theorem precell_all_zero : sig1 e21 0 = 0 ∧ sig1 e21 2 = 0 ∧
    sig1 e21 1 + sig1 e21 3 = 3 := by decide

theorem sig_cell_3 :   -- {2:1,3:1}, d = 12
    sig2 e21 e31 0 = 3 ∧ sig2 e21 e31 2 = 3 ∧
    sig2 e21 e31 1 + sig2 e21 e31 3 = 6 := by decide

theorem sig_cell_4 :   -- {2:2,3:1}, d = 108
    sig2 e22 e31 0 = 27 ∧ sig2 e22 e31 2 = 27 ∧
    sig2 e22 e31 1 + sig2 e22 e31 3 = 54 := by decide

theorem sig_cell_8 :   -- {2:3,3:1}, d = 588
    sig2 e23 e31 0 = 147 ∧ sig2 e23 e31 2 = 147 ∧
    sig2 e23 e31 1 + sig2 e23 e31 3 = 294 := by decide

theorem sig_cell_9 :   -- {2:3,3:2}, d = 9408
    sig2 e23 e32 0 = 2352 ∧ sig2 e23 e32 2 = 2352 ∧
    sig2 e23 e32 1 + sig2 e23 e32 3 = 4704 := by decide

theorem sig_cell_5_fourplace :   -- {2:2,3:1,5:1}, d = 1728: the ×16 flat arrival
    sig3 e22 e31 e51 0 = 432 ∧ sig3 e22 e31 e51 2 = 432 ∧
    sig3 e22 e31 e51 1 + sig3 e22 e31 e51 3 = 864 := by decide

theorem sig_cell_9_fourplace :   -- {2:3,3:2,5:1}, d = 150528
    sig3 e23 e32 e51 0 = 37632 ∧ sig3 e23 e32 e51 2 = 37632 ∧
    sig3 e23 e32 e51 1 + sig3 e23 e32 e51 3 = 75264 := by decide

/-- the flat-arrival law at the instance: gluing the flat (5,1) multiplies every sector
    mass of {2:2,3:1} by exactly dim Son(5,1) = 16 -/
theorem arrival_multiplies_16 :
    sig3 e22 e31 e51 0 = 16 * sig2 e22 e31 0 ∧
    sig3 e22 e31 e51 2 = 16 * sig2 e22 e31 2 ∧
    sig3 e22 e31 e51 1 = 16 * sig2 e22 e31 1 ∧
    sig3 e22 e31 e51 3 = 16 * sig2 e22 e31 3 := by decide

/-- pos = neg at every banked cell (the symmetry half of the signature law) -/
theorem pos_eq_neg_all :
    sig2 e21 e31 0 = sig2 e21 e31 2 ∧ sig2 e22 e31 0 = sig2 e22 e31 2 ∧
    sig2 e23 e31 0 = sig2 e23 e31 2 ∧ sig2 e23 e32 0 = sig2 e23 e32 2 ∧
    sig3 e22 e31 e51 0 = sig3 e22 e31 e51 2 ∧
    sig3 e23 e32 e51 0 = sig3 e23 e32 e51 2 := by decide

/-- the constrained-class dims at the banked cells (T-fixed ∧ antipode-fixed = the e = 0
    sectors × 2), with the DEATH at the pre-cell and the REVIVAL at a² = 3 -/
def classDim1 (a : E4) : Nat := 2 * get a 0
def classDim2 (a b : E4) : Nat := (sig2 a b 0 / 3) * 2

theorem class_death_and_revival :
    classDim1 e21 = 0 ∧ classDim2 e21 e31 = 2 ∧ classDim2 e22 e31 = 18 ∧
    classDim2 e23 e32 = 1568 := by decide

end SectorArithmetic
