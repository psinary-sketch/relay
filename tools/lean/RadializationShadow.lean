/-
  THE RADIALIZATION ACT'S DECIDED CORE · RadializationShadow.lean
  ================================================================

  Ferry 2026-08-21 (b76). Vanilla Lean 4 (v4.29.1 pinned), no imports; expected
  profile per terminal: "does not depend on any axioms".

  The shell-summing map R (the radialization — the merged construction of the
  theta bridge's step A and N5's radial-compression dictionary) at its decidable
  spine: the valuation is the gcd law (Nat.gcd m N = p^{v(m)}), so every shell
  statement is a gcd statement. P1: the shell partitions at the banked sizes
  (3, 5, 7, 9 cells at n = 1..4, both parities), the seed addresses
  gcd(2ⁿ⁻¹, 2ⁿ) = 2ⁿ⁻¹, and the boundary index re-derived from R's side (the
  doubling image misses the primitive shell; the zero cell is terminal). P2: the
  transfer/shift intertwining as the gcd law over FULL ranges, and the
  ball-boundary transition filter identity — the one shell that doubles into the
  ball is exactly the seed's shell (the deficient weight's address, b61, derived
  from the map's side). P3: the chart theta-object (Σ ζ^{m²} — the quarter-turn's
  diagonal, the banked traces) assembled BY SHELLS at (2,1), (3,1), (2,2) with
  the primitive shell silent beyond the boundary cell — the chart-side identity
  only; no classical identification. P4: the radial coordinate factors through
  the place split (gcd multiplicativity at the composite denominators).
  Bank: relay data/b76_radialization.txt.
-/

set_option maxRecDepth 8192

namespace RadializationShadow

/-- P1: the shell partitions (sizes 3, 5, 7, 9 at n = 1..4; both parities at the
    smallest cells), the seed addresses, and the boundary index from R's side -/
theorem shell_partition_instances :
    (((List.range 16).filter (fun m => decide (Nat.gcd m 16 = 1))).length = 8 ∧
     ((List.range 16).filter (fun m => decide (Nat.gcd m 16 = 2))).length = 4 ∧
     ((List.range 16).filter (fun m => decide (Nat.gcd m 16 = 4))).length = 2 ∧
     ((List.range 16).filter (fun m => decide (Nat.gcd m 16 = 8))).length = 1) ∧
    (((List.range 9).filter (fun m => decide (Nat.gcd m 9 = 1))).length = 6 ∧
     ((List.range 9).filter (fun m => decide (Nat.gcd m 9 = 3))).length = 2) ∧
    (Nat.gcd 1 2 = 1 ∧ Nat.gcd 2 4 = 2 ∧ Nat.gcd 4 8 = 4 ∧ Nat.gcd 8 16 = 8) ∧
    ((List.range 4).filter (fun m => decide (((2*m) % 4) % 2 = 1)) = [] ∧
     (List.range 16).filter (fun m => decide (((2*m) % 16) % 2 = 1)) = [] ∧
     (List.range 64).filter (fun m => decide (((2*m) % 64) % 2 = 1)) = [] ∧
     (2*0) % 64 = 0) := by decide

/-- P2: the transfer/shift intertwining as the gcd law, full ranges at the four
    banked place-2 levels — R carries the p-term transfer to the shift exactly
    on positions -/
theorem transfer_shift_gcd_law :
    ((List.range 4).map (fun m => Nat.gcd ((2*m) % 4) 4) =
      (List.range 4).map (fun m => min (2 * Nat.gcd m 4) 4)) ∧
    ((List.range 16).map (fun m => Nat.gcd ((2*m) % 16) 16) =
      (List.range 16).map (fun m => min (2 * Nat.gcd m 16) 16)) ∧
    ((List.range 64).map (fun m => Nat.gcd ((2*m) % 64) 64) =
      (List.range 64).map (fun m => min (2 * Nat.gcd m 64) 64)) ∧
    ((List.range 256).map (fun m => Nat.gcd ((2*m) % 256) 256) =
      (List.range 256).map (fun m => min (2 * Nat.gcd m 256) 256)) := by decide

/-- P2: the ball-boundary transition — the positions outside the ball whose
    double lands ball-or-zero are exactly the seed's shell (the deficient
    weight's address, from the map's side) at the banked levels -/
theorem ball_boundary_address :
    ((List.range 4).filter (fun m =>
        decide (Nat.gcd m 4 < 2) &&
        (decide (2 ≤ Nat.gcd ((2*m) % 4) 4) || decide ((2*m) % 4 = 0))) =
      (List.range 4).filter (fun m => decide (Nat.gcd m 4 = 1))) ∧
    ((List.range 16).filter (fun m =>
        decide (Nat.gcd m 16 < 4) &&
        (decide (4 ≤ Nat.gcd ((2*m) % 16) 16) || decide ((2*m) % 16 = 0))) =
      (List.range 16).filter (fun m => decide (Nat.gcd m 16 = 2))) ∧
    ((List.range 64).filter (fun m =>
        decide (Nat.gcd m 64 < 8) &&
        (decide (8 ≤ Nat.gcd ((2*m) % 64) 64) || decide ((2*m) % 64 = 0))) =
      (List.range 64).filter (fun m => decide (Nat.gcd m 64 = 4))) := by decide

/-- ℤ[i] pairs; ℤ[ζ₉] six-coordinates (x⁶ = −1 − x³); ℤ[ζ₁₆] eight-coordinates
    (x⁸ = −1) — the banked patterns, local to this module -/
def zpow4 (e : Nat) : Int × Int :=
  match e % 4 with
  | 0 => (1, 0) | 1 => (0, 1) | 2 => (-1, 0) | _ => (0, -1)
def padd (u v : Int × Int) : Int × Int := (u.1 + v.1, u.2 + v.2)
abbrev V6 : Type := Int × Int × Int × Int × Int × Int
def v6add (u v : V6) : V6 :=
  (u.1 + v.1, u.2.1 + v.2.1, u.2.2.1 + v.2.2.1,
   u.2.2.2.1 + v.2.2.2.1, u.2.2.2.2.1 + v.2.2.2.2.1, u.2.2.2.2.2 + v.2.2.2.2.2)
def m9 (e : Nat) : V6 :=
  match e % 9 with
  | 0 => (1, 0, 0, 0, 0, 0) | 1 => (0, 1, 0, 0, 0, 0) | 2 => (0, 0, 1, 0, 0, 0)
  | 3 => (0, 0, 0, 1, 0, 0) | 4 => (0, 0, 0, 0, 1, 0) | 5 => (0, 0, 0, 0, 0, 1)
  | 6 => (-1, 0, 0, -1, 0, 0) | 7 => (0, -1, 0, 0, -1, 0) | _ => (0, 0, -1, 0, 0, -1)
def v16add (u v : List Int) : List Int := List.zipWith (· + ·) u v
def m16 (e : Nat) : List Int :=
  match e % 16 with
  | 0 => [1,0,0,0,0,0,0,0] | 1 => [0,1,0,0,0,0,0,0] | 2 => [0,0,1,0,0,0,0,0]
  | 3 => [0,0,0,1,0,0,0,0] | 4 => [0,0,0,0,1,0,0,0] | 5 => [0,0,0,0,0,1,0,0]
  | 6 => [0,0,0,0,0,0,1,0] | 7 => [0,0,0,0,0,0,0,1] | 8 => [-1,0,0,0,0,0,0,0]
  | 9 => [0,-1,0,0,0,0,0,0] | 10 => [0,0,-1,0,0,0,0,0] | 11 => [0,0,0,-1,0,0,0,0]
  | 12 => [0,0,0,0,-1,0,0,0] | 13 => [0,0,0,0,0,-1,0,0] | 14 => [0,0,0,0,0,0,-1,0]
  | _ => [0,0,0,0,0,0,0,-1]

def thetaP (l : List Nat) : Int × Int :=
  l.foldl (fun acc m => padd acc (zpow4 ((m*m) % 4))) (0, 0)
def theta9 (l : List Nat) : V6 :=
  l.foldl (fun acc m => v6add acc (m9 ((m*m) % 9))) (0, 0, 0, 0, 0, 0)
def theta16 (l : List Nat) : List Int :=
  l.foldl (fun acc m => v16add acc (m16 ((m*m) % 16))) [0, 0, 0, 0, 0, 0, 0, 0]

/-- P3: the chart theta-object assembled BY SHELLS — the quarter-turn's diagonal
    sum grouped by valuation reproduces the banked traces (q(1+i) at place 2, q
    at odd), with the primitive shell SILENT beyond the boundary cell (2,1) —
    the chart-side identity only; no classical identification -/
theorem theta_by_shells :
    (thetaP ((List.range 4).filter (fun m => decide (Nat.gcd m 4 = 1))) = (0, 2) ∧
     thetaP (List.range 4) = (2, 2)) ∧
    (theta9 ((List.range 9).filter (fun m => decide (Nat.gcd m 9 = 1))) =
       ((0, 0, 0, 0, 0, 0) : V6) ∧
     theta9 (List.range 9) = ((3, 0, 0, 0, 0, 0) : V6)) ∧
    (theta16 ((List.range 16).filter (fun m => decide (Nat.gcd m 16 = 1))) =
       [0, 0, 0, 0, 0, 0, 0, 0] ∧
     theta16 ((List.range 16).filter (fun m => decide (Nat.gcd m 16 = 2))) =
       [0, 0, 0, 0, 4, 0, 0, 0] ∧
     theta16 (List.range 16) = [4, 0, 0, 0, 4, 0, 0, 0]) := by decide

/-- P4: the radial coordinate factors through the place split — gcd
    multiplicativity at the composite denominators: the shell of a torus point
    is the product of its per-place shells -/
theorem plane_factorization :
    ((List.range 36).map (fun j => Nat.gcd j 36) =
      (List.range 36).map (fun j => Nat.gcd (j % 4) 4 * Nat.gcd (j % 9) 9)) ∧
    ((List.range 100).map (fun j => Nat.gcd j 100) =
      (List.range 100).map (fun j => Nat.gcd (j % 4) 4 * Nat.gcd (j % 25) 25)) := by
  decide

end RadializationShadow
