/-
  THE ADELIC CONSTRUCTION ACT'S DECIDED CORE · AdelicPlaneShadow.lean
  ====================================================================

  Ferry 2026-08-21 (b75). Vanilla Lean 4 (v4.29.1 pinned), no imports; expected
  profile per terminal: "does not depend on any axioms".

  The staged adelic-phase-plane registration RUN at its finite decidable core
  (the plane is an INDEX OBJECT; the real fiber is a formal slot, never entered).
  THE GLUING (G1's index arithmetic): negation — the quarter-turn's only
  nontrivial coordinate map — respects the place split of the constructed
  rational torus. D1 (H-COH-fin): the glued assignment is a character (additivity
  over the full range-square) and the fraction characters transport through the
  tower by the ι exponent. D2, all three candidates: the five banked cross-place
  global dimensions (16, 144, 2304, 12544, 1) re-derived as the plane's
  stationary computation — the diagonal C₄ average of products of the banked
  per-place fixed-phase sums, in ℤ[i] pairs; the visibility mechanism — the
  quarter-turn's diagonal 2-torsion is {origin} at odd q and {origin, center} at
  q = 2ⁿ, with the half-integrality law at odd q (the global center collapses to
  the origin off place 2); the six banked deficits (0, 11, 126, 2282, 12512,
  37800) as the global-minus-local stationary difference, subtraction-free. D3:
  ℚ-triviality located — the finite recombination exponent plus the formal real
  exponent vanishes mod D over full ranges.
  Bank: relay data/b75_adelic_construction.txt.
-/

namespace AdelicPlaneShadow

/-- THE GLUING (G1's decidable core): negation respects the place split at the
    banked composite denominators — the quarter-turn acts componentwise on the
    constructed torus -/
theorem torus_gluing_instances :
    ((List.range 36).map (fun j => ((36 - j) % 36) % 4) =
      (List.range 36).map (fun j => (4 - j % 4) % 4)) ∧
    ((List.range 36).map (fun j => ((36 - j) % 36) % 9) =
      (List.range 36).map (fun j => (9 - j % 9) % 9)) ∧
    ((List.range 100).map (fun j => ((100 - j) % 100) % 25) =
      (List.range 100).map (fun j => (25 - j % 25) % 25)) := by decide

set_option maxRecDepth 8192 in
/-- D1 (H-COH-fin): the glued assignment is a character — additivity of the
    recombination exponent over the FULL 36 × 36 square — and the fraction
    characters transport through the place-2 tower by the ι exponent -/
theorem hcoh_fin_instances :
    ((List.range 1296).map (fun k =>
      ((9*((k / 36) % 4) + 4*((7*(k / 36)) % 9)) % 36
        + (9*((k % 36) % 4) + 4*((7*(k % 36)) % 9)) % 36) % 36) =
      (List.range 1296).map (fun k => (k / 36 + k % 36) % 36)) ∧
    ((List.range 4).map (fun a => (((4*a) % 16)*4) % 64) =
      (List.range 4).map (fun a => (16*a) % 64)) := by decide

/-- ℤ[i] pairs for the stationary sums -/
def cmul (u v : Int × Int) : Int × Int :=
  (u.1*v.1 - u.2*v.2, u.1*v.2 + u.2*v.1)
def cadd (u v : Int × Int) : Int × Int := (u.1 + v.1, u.2 + v.2)
/-- the banked Son fixed-phase-sum tuple (tr M⁰, tr M, tr Π, tr M³): (q−1)²
    at k = 0; the place-2 cells carry (i, −1, −i), the odd cells zeros -/
def son (d : Int) (p2 : Bool) (k : Nat) : Int × Int :=
  match k with
  | 0 => (d, 0)
  | 1 => if p2 then (0, 1) else (0, 0)
  | 2 => if p2 then (-1, 0) else (0, 0)
  | _ => if p2 then (0, -1) else (0, 0)
def rosterSum (cells : List (Int × Bool)) : Int × Int :=
  (List.range 4).foldl (fun acc k =>
    cadd acc (cells.foldl (fun pr c => cmul pr (son c.1 c.2 k)) (1, 0))) (0, 0)

/-- D2, THE LEADING CANDIDATE: the five banked cross-place global dimensions
    re-derived as the plane's stationary computation — the diagonal C₄ average
    of the products of the per-place fixed-phase sums equals 4·D_global at all
    five banked rosters (any odd place silences the k = 1, 2, 3 terms) -/
theorem stationary_dimension_instances :
    rosterSum [(1, true), (4, false), (16, false)] = (4*16, 0) ∧
    rosterSum [(9, true), (64, false)] = (4*144, 0) ∧
    rosterSum [(9, true), (64, false), (16, false)] = (4*2304, 0) ∧
    rosterSum [(49, true), (64, false), (16, false)] = (4*12544, 0) ∧
    rosterSum [(1, true), (4, false)] = (4*1, 0) := by decide

/-- D2, THE ALTERNATE (sharpened to its mechanism): the quarter-turn's diagonal
    2-torsion on the grid is {origin} at every banked odd q and
    {origin, center} at every banked q = 2ⁿ, and 1/2 is invertible-integral at
    odd q — the global center collapses to the origin off place 2 -/
theorem visibility_split_instances :
    ((List.range 3).filter (fun j => decide ((2*j) % 3 = 0)) = [0]) ∧
    ((List.range 5).filter (fun j => decide ((2*j) % 5 = 0)) = [0]) ∧
    ((List.range 9).filter (fun j => decide ((2*j) % 9 = 0)) = [0]) ∧
    ((List.range 27).filter (fun j => decide ((2*j) % 27 = 0)) = [0]) ∧
    ((List.range 4).filter (fun j => decide ((2*j) % 4 = 0)) = [0, 2]) ∧
    ((List.range 8).filter (fun j => decide ((2*j) % 8 = 0)) = [0, 4]) ∧
    ((List.range 16).filter (fun j => decide ((2*j) % 16 = 0)) = [0, 8]) ∧
    (2*2 % 3 = 1 ∧ 3*2 % 5 = 1 ∧ 5*2 % 9 = 1 ∧ 14*2 % 27 = 1) := by decide

/-- D2, THE THIRD CANDIDATE: the six banked deficits as the global-minus-local
    stationary difference, subtraction-free — the global stationary dimension's
    fourfold equals four times the local invariant sum plus the deficit -/
theorem deficit_global_minus_local :
    (1*4 = 4*(1 + 0)) ∧
    (1*4*16 = 4*(5 + 11)) ∧
    (9*64 = 4*(18 + 126)) ∧
    (9*64*16 = 4*(22 + 2282)) ∧
    (49*64*16 = 4*(32 + 12512)) ∧
    (225*676 = 4*(225 + 37800)) := by decide

/-- D3: ℚ-triviality located on the object — the finite characters' product
    exponent plus the formal real character's exponent vanishes mod D over the
    full ranges (the real component cited as the formal marker only) -/
theorem q_triviality_instances :
    ((List.range 36).map (fun a =>
      ((9*(a % 4) + 4*((7*a) % 9)) % 36 + (36 - a % 36)) % 36) =
      (List.range 36).map (fun _ => 0)) ∧
    ((List.range 100).map (fun a =>
      ((25*(a % 4) + 4*((19*a) % 25)) % 100 + (100 - a % 100)) % 100) =
      (List.range 100).map (fun _ => 0)) := by decide

end AdelicPlaneShadow
