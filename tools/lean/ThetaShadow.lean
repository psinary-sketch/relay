/-
  THE THETA UNIT'S FINITE CONTENT · ThetaShadow.lean
  ===================================================

  Ferry 2026-08-21 (b61, the theta act). Vanilla Lean 4 (v4.29.1 pinned), no imports;
  expected profile per terminal: "does not depend on any axioms".

  THE IDENTIFICATION'S FINITE-LEVEL CONTENT (the staged Θ_T registration run at its
  fixed statement; the b61 run-registration operationalizes): the record fixes the
  identified model as the bilateral shift with all weights 1 except one deficient
  weight w at the ball boundary (the bench note; w's value downstream); its level-n
  truncation on the chart's shell space (valuations 0..2n) is the truncated shift
  T: shell_j ↦ shell_{j+1}, top ↦ 0. Compiled below, at every banked shell size
  (2n + 1 = 3, 5, 7, 9 across the eight banked cells):

  · THE DEFICIENCY GATE (P2): T*T = Id − P_top and TT* = Id − P_bottom — defect
    exactly (1,1), one rank at each boundary, matching the banked ground (the
    fifth-law rows; the keystone's carried (1,1) line).
  · THE TRACE GATE (P1, the scaling channel): tr(Tᵏ) = 0 for 1 ≤ k ≤ 2n — the
    model is trace-silent off the identity, matching the compiled TraceSilence
    (row 3); the transform channel's chart traces are rows 35–36's compiled values
    (q odd, q(1+i) at the place 2), re-cited not re-proved.
  · THE SEED-DEFECT CORRESPONDENCE (P3, branch (a)): the Sonin-side defect address
    is the BALL-BOUNDARY shell v = n−1, and the imported seed's banked support row
    2^{n−1} has 2-adic valuation exactly n−1 at every banked place-2 level — the
    same address (decided); the seed is the UNIQUE banked line at that address
    (the purity-locus law, rows 33/36, cited).

  THE LIMIT ITSELF STAYS A NAMED OPEN (the SOT limit of the level compressions —
  stated, not proved, in the owner file; never a sorry), as does the operator-level
  defect-vector identity (N5, the run-registration). Bank: relay
  data/b61_theta_unit.txt.
-/

namespace ThetaShadow

/-- the truncated shift on shell coordinates: (Tv)₀ = 0, (Tv)ᵢ = vᵢ₋₁ -/
def Tsh (v : List Int) : List Int := 0 :: v.take (v.length - 1)

/-- its adjoint: (T*v)ᵢ = vᵢ₊₁, (T*v)_top = 0 -/
def Tstar (v : List Int) : List Int := v.drop 1 ++ [0]

/-- the j-th shell basis vector of size d -/
def basis (d j : Nat) : List Int :=
  (List.range d).map (fun k => if k = j then (1 : Int) else 0)

/-- the zero vector of size d -/
def zvec (d : Nat) : List Int := (List.range d).map (fun _ => (0 : Int))

/-- iterated shift application -/
def powApply : Nat → List Int → List Int
  | 0, v => v
  | k + 1, v => Tsh (powApply k v)

/-- own indexing and summation (no core-lemma dependence) -/
def nth : List Int → Nat → Int
  | [], _ => 0
  | a :: _, 0 => a
  | _ :: l, n + 1 => nth l n

def sumList : List Int → Int
  | [] => 0
  | a :: l => a + sumList l

/-- the trace of Tᵏ at size d -/
def trPow (d k : Nat) : Int :=
  sumList ((List.range d).map (fun j => nth (powApply k (basis d j)) j))

/-- THE DEFICIENCY GATE (P2), decided at every banked shell size: T*T = Id − P_top
    and TT* = Id − P_bottom — defect exactly (1,1) at sizes 3, 5, 7, 9 -/
theorem defect_gate_instances :
    ((List.range 3).map (fun j => Tstar (Tsh (basis 3 j))) =
      (List.range 3).map (fun j => if j = 2 then zvec 3 else basis 3 j) ∧
     (List.range 3).map (fun j => Tsh (Tstar (basis 3 j))) =
      (List.range 3).map (fun j => if j = 0 then zvec 3 else basis 3 j)) ∧
    ((List.range 5).map (fun j => Tstar (Tsh (basis 5 j))) =
      (List.range 5).map (fun j => if j = 4 then zvec 5 else basis 5 j) ∧
     (List.range 5).map (fun j => Tsh (Tstar (basis 5 j))) =
      (List.range 5).map (fun j => if j = 0 then zvec 5 else basis 5 j)) ∧
    ((List.range 7).map (fun j => Tstar (Tsh (basis 7 j))) =
      (List.range 7).map (fun j => if j = 6 then zvec 7 else basis 7 j) ∧
     (List.range 7).map (fun j => Tsh (Tstar (basis 7 j))) =
      (List.range 7).map (fun j => if j = 0 then zvec 7 else basis 7 j)) ∧
    ((List.range 9).map (fun j => Tstar (Tsh (basis 9 j))) =
      (List.range 9).map (fun j => if j = 8 then zvec 9 else basis 9 j) ∧
     (List.range 9).map (fun j => Tsh (Tstar (basis 9 j))) =
      (List.range 9).map (fun j => if j = 0 then zvec 9 else basis 9 j)) := by decide

/-- THE TRACE GATE (P1, the scaling channel), decided: tr(Tᵏ) = 0 for every
    1 ≤ k ≤ d − 1 at every banked shell size — the model is trace-silent off the
    identity, as the banked chart is -/
theorem model_trace_silence :
    ((List.range 2).map (fun k => trPow 3 (k + 1)) = List.replicate 2 0) ∧
    ((List.range 4).map (fun k => trPow 5 (k + 1)) = List.replicate 4 0) ∧
    ((List.range 6).map (fun k => trPow 7 (k + 1)) = List.replicate 6 0) ∧
    ((List.range 8).map (fun k => trPow 9 (k + 1)) = List.replicate 8 0) := by decide

/-- THE SEED-DEFECT CORRESPONDENCE (P3), the address half, decided: at place-2 level
    n the imported seed's banked support row is 2^{n−1}, whose 2-adic valuation is
    exactly n − 1 — the ball-boundary shell, the model's Sonin-side defect address —
    at every banked level n = 1, 2, 3, 4 (rows 1, 2, 4, 8) -/
theorem seed_boundary_address :
    (1 = 2 ^ 0 ∧ 1 % 2 ^ 0 = 0 ∧ 1 % 2 ^ 1 ≠ 0) ∧
    (2 = 2 ^ 1 ∧ 2 % 2 ^ 1 = 0 ∧ 2 % 2 ^ 2 ≠ 0) ∧
    (4 = 2 ^ 2 ∧ 4 % 2 ^ 2 = 0 ∧ 4 % 2 ^ 3 ≠ 0) ∧
    (8 = 2 ^ 3 ∧ 8 % 2 ^ 3 = 0 ∧ 8 % 2 ^ 4 ≠ 0) := by decide

end ThetaShadow
