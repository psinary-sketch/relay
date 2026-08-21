/-
  THE FLATNESS LAW · FlatnessShadow.lean
  =======================================

  Ferry 2026-08-21 (b57, component 3). Vanilla Lean 4 (v4.29.1 pinned), no imports;
  expected profile per terminal: "does not depend on any axioms".

  THE LAW (derived longhand in the b57 registration from the chart Gauss computation and
  the ball-pair inclusion–exclusion — elementary, no quadratic reciprocity):
    tr(S) over ℤ/q² = q (odd q), q(1+i) (q = 2ⁿ, the fold convention i = ζ^{N/4});
    tr(S|Son) = tr(S) − q  and  tr(Π|Son) = 0 (odd) / −1 (q = 2ⁿ),
  whence the linear solve forces the sector dimensions AT EVERY LEVEL:
    odd q:   (d, d, d, d)         with 4·d = (q−1)²           — FLATNESS FORCED;
    q = 2ⁿ:  (d, d, d+1, d)       with 4·d = q(q−2)           — THE UNIT TRACE i,
             the i-sector excess exactly one, carried by the imported seed line
             (the ι-chain of the (2,1) generator; the b57 run, the purity-locus law).
  Compiled here: the trace endpoints and the dim-law instances at all eight banked
  cells, quadruple order (d₁, d₋₁, d_i, d₋ᵢ). The general derivation is bank-resident
  (relay data/b57_row31_depth.txt); the Gauss-sum steps stay longhand there.
-/

namespace FlatnessShadow

/-- the twisted-trace endpoints from the banked dims, as ℤ[i] pairs: t₁ = (d₁−d₋₁) +
    i(d_i−d₋ᵢ) and t₂ = d₁+d₋₁−d_i−d₋ᵢ — exactly 0 and 0 at the four odd cells,
    exactly i and −1 at the four place-2 cells, every banked level -/
theorem trace_endpoints :
    -- odd cells (3,1), (5,1), (3,2), (3,3): t₁ = 0, t₂ = 0
    ((1-1, 1-1) = ((0, 0) : Int × Int) ∧ 1+1-1-1 = (0 : Int)) ∧
    ((4-4, 4-4) = ((0, 0) : Int × Int) ∧ 4+4-4-4 = (0 : Int)) ∧
    ((16-16, 16-16) = ((0, 0) : Int × Int) ∧ 16+16-16-16 = (0 : Int)) ∧
    ((169-169, 169-169) = ((0, 0) : Int × Int) ∧ 169+169-169-169 = (0 : Int)) ∧
    -- place-2 cells (2,1), (2,2), (2,3), (2,4): t₁ = i, t₂ = −1
    ((0-0, 1-0) = ((0, 1) : Int × Int) ∧ 0+0-1-0 = (-1 : Int)) ∧
    ((2-2, 3-2) = ((0, 1) : Int × Int) ∧ 2+2-3-2 = (-1 : Int)) ∧
    ((12-12, 13-12) = ((0, 1) : Int × Int) ∧ 12+12-13-12 = (-1 : Int)) ∧
    ((56-56, 57-56) = ((0, 1) : Int × Int) ∧ 56+56-57-56 = (-1 : Int)) := by decide

/-- the odd-place dim law at the banked odd cells: the tuple is uniform at d with
    4·d = (q−1)² — flatness as the law's instance, full tuples -/
theorem dim_law_odd :
    (((1,1,1,1) : Nat×Nat×Nat×Nat) = (1,1,1,1) ∧ 4 * 1 = (3-1)^2) ∧
    (((4,4,4,4) : Nat×Nat×Nat×Nat) = (4,4,4,4) ∧ 4 * 4 = (5-1)^2) ∧
    (((16,16,16,16) : Nat×Nat×Nat×Nat) = (16,16,16,16) ∧ 4 * 16 = (9-1)^2) ∧
    (((169,169,169,169) : Nat×Nat×Nat×Nat) = (169,169,169,169) ∧ 4 * 169 = (27-1)^2) := by
  decide

/-- the place-2 dim law at the banked cells: the tuple is (d, d, d+1, d) with
    4·d = q(q−2) — the unit trace's excess exactly one, every banked level -/
theorem dim_law_place2 :
    (((0,0,1,0) : Nat×Nat×Nat×Nat) = (0,0,0+1,0) ∧ 4 * 0 = 2*(2-2)) ∧
    (((2,2,3,2) : Nat×Nat×Nat×Nat) = (2,2,2+1,2) ∧ 4 * 2 = 4*(4-2)) ∧
    (((12,12,13,12) : Nat×Nat×Nat×Nat) = (12,12,12+1,12) ∧ 4 * 12 = 8*(8-2)) ∧
    (((56,56,57,56) : Nat×Nat×Nat×Nat) = (56,56,56+1,56) ∧ 4 * 56 = 16*(16-2)) := by
  decide

end FlatnessShadow
