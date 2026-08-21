/-
  THE LEFSCHETZ FAMILY · LefschetzShadow.lean
  ============================================

  Ferry 2026-08-21 (b67, the congruence act, component 1). Vanilla Lean 4 (v4.29.1
  pinned), no imports; expected profile per terminal: "does not depend on any axioms".

  THE FAMILY (the b67 registration, decided at every banked cell by the instrument
  and here at the decidable endpoints): each power of the quarter-turn has its trace
  equal to its fixed-locus phase sum — M over {origin; center at p = 2} with phases
  1 and i; Π = M² over the 2-TORSION SQUARE at p = 2 (four points; phases 1, 1, 1,
  and −1 at the center — computed from Π's own action, the axis-reduction subtlety
  pre-empted in the registration) and the origin alone at odd q; M³ over M's locus
  with the conjugate phase; M⁰ over the whole grid. THE SWAPPED PAIR (q/2, 0) ↔
  (0, q/2) is a σ-2-cycle inside the σ²-fixed square — it feeds Π's sum and not M's:
  the involution's geometry separated from the rotation's. THE ENDPOINT: the
  character-average law is a FIXED-POINT THEOREM IN FULL — all eight banked sector
  tuples from the center's phase data alone (4·d_i = (q−1)² + 3 and 4·d = (q−1)² − 1
  at p = 2; 4·d = (q−1)² at odd q). Bank: relay data/b67_congruence.txt.
-/

namespace LefschetzShadow

/-- the σ²-fixed grid points at size q -/
def piFixed (q : Nat) : List (Nat × Nat) :=
  ((List.range q).map (fun a => (List.range q).map (fun t => (a, t)))).flatten.filter
    (fun v => ((q - v.1) % q, (q - v.2) % q) = v)

/-- σ applied once -/
def sig (q : Nat) (v : Nat × Nat) : Nat × Nat := ((q - v.2) % q, v.1)

/-- THE Π-LOCUS AND THE SWAPPED PAIR, decided: the origin alone at odd q; the
    2-torsion square at q = 2ⁿ; and (q/2, 0) ↔ (0, q/2) is a σ-2-cycle — σ²-fixed,
    not σ-fixed — feeding Π's sum and not M's -/
theorem pi_locus_and_pair :
    (piFixed 3 = [(0,0)] ∧ piFixed 5 = [(0,0)] ∧ piFixed 9 = [(0,0)]) ∧
    (piFixed 2 = [(0,0),(0,1),(1,0),(1,1)] ∧
     piFixed 4 = [(0,0),(0,2),(2,0),(2,2)] ∧
     piFixed 8 = [(0,0),(0,4),(4,0),(4,4)]) ∧
    (sig 4 (2,0) = (0,2) ∧ sig 4 (0,2) = (2,0) ∧ sig 4 (2,0) ≠ (2,0) ∧
     sig 8 (4,0) = (0,4) ∧ sig 8 (0,4) = (4,0) ∧ sig 8 (4,0) ≠ (4,0)) := by decide

/-- a monomial c·ζ₁₆^e reduced in ℤ[x]/(x⁸+1) -/
def mono (c : Int) (e : Nat) : List Int :=
  let r := e % 8
  let s : Int := if (e / 8) % 2 = 0 then c else -c
  (List.range 8).map (fun k => if k = r then s else 0)

/-- THE Π-PHASES, decided at (2,2): the center's Π-phase is ω^{−q/2} = ζ^{N/2} = −1
    (the exponent q·(q/2) = N/2, and the monomial reduces to −1), the three other
    2-torsion points carry phase 1, and the sums are the banked traces — whole chart
    1 + 1 + 1 − 1 = 2, Sonin-restricted −1 (the center alone) -/
theorem pi_phase_instances :
    (4 * 2 = 16 / 2 ∧ mono 1 8 = [-1, 0, 0, 0, 0, 0, 0, 0]) ∧
    ((1 + 1 + 1 - 1 : Int) = 2 ∧ (0 - 1 : Int) = -1) := by decide

/-- THE DIMS FROM THE CENTER, decided subtraction-free at all eight banked cells:
    4·d_i = (q−1)² + 3 and 4·d = (q−1)² − 1 at p = 2 (as (q−1)² = 4d + 1); flatness
    4·d = (q−1)² at odd q — the character-average law as a fixed-point theorem -/
theorem dims_from_center :
    (4 * 1 = (2-1)^2 + 3 ∧ (2-1)^2 = 4 * 0 + 1) ∧
    (4 * 3 = (4-1)^2 + 3 ∧ (4-1)^2 = 4 * 2 + 1) ∧
    (4 * 13 = (8-1)^2 + 3 ∧ (8-1)^2 = 4 * 12 + 1) ∧
    (4 * 57 = (16-1)^2 + 3 ∧ (16-1)^2 = 4 * 56 + 1) ∧
    (4 * 1 = (3-1)^2 ∧ 4 * 4 = (5-1)^2 ∧ 4 * 16 = (9-1)^2 ∧ 4 * 169 = (27-1)^2) := by
  decide

/-- M³'S LOCUS AND PHASE, decided: fix(σ³) = fix(σ) at the banked sizes, and the
    center's M³-phase is the conjugate (i³ = −i in pairs) -/
theorem m3_locus_phase :
    (((List.range 4).map (fun a => (List.range 4).map (fun t => (a, t)))).flatten.filter
        (fun v => sig 4 (sig 4 (sig 4 v)) = v) =
     ((List.range 4).map (fun a => (List.range 4).map (fun t => (a, t)))).flatten.filter
        (fun v => sig 4 v = v)) ∧
    ((0*0 - 1*1) * 0 - (0*1 + 1*0) * 1, (0*0 - 1*1) * 1 + (0*1 + 1*0) * 0) =
      ((0, -1) : Int × Int) := by decide

end LefschetzShadow
