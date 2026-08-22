/-
  THE THETA-BRIDGE CONTINUATION'S DECIDED CORE · ThetaBridgeShadow.lean
  ======================================================================

  Ferry 2026-08-22 (b85). Vanilla Lean 4 (v4.29.1 pinned), no imports; expected
  profile per terminal: "does not depend on any axioms".

  STEP A'S FORMAL IDENTIFICATION at its finite half (firewall-safe; the
  analytic theta object is NOT built; no analytic identification is asserted).
  THE POINT-COUNT IDENTITY: the chart theta-object at level N is the formal
  rational-point data of the theta series — the exponent fold Σ_m ζ^{m²} equals
  the count-weighted assembly Σ_r c_N(r)·ζ^r with c_N(r) the quadric's point
  count — decided in exact cyclotomic coordinates at N = 9 (six-coords,
  x⁶ = −1 − x³) and N = 16 (eight-coords, List-Int carrier, x⁸ = −1). THE CUSP
  COUNT: c_N(0) = q at every banked cell (decided at all eight N; the classical
  naming of this datum is NAVIGATOR-OPEN at the bank, cited never weighted).
  THE TRANSFORMATION LAW'S FINITE SHADOW at the odd cells: completing the
  square gives Σ_m ζ^{m²+2mk} = ζ^{−k²}·G for every k (G the banked value 3 at
  N = 9) — the odd-cell functional-equation shadow, decided; the place-2 twist
  is the metaplectic frame's territory (rows 39–40), stated not forced; the
  analytic transformation is B–C territory at cite grade and not attempted.
  Bank: relay data/b85_theta_ownership.txt.
-/

set_option maxRecDepth 8192

namespace ThetaBridgeShadow

abbrev V6 : Type := Int × Int × Int × Int × Int × Int
def v6add (u v : V6) : V6 :=
  (u.1 + v.1, u.2.1 + v.2.1, u.2.2.1 + v.2.2.1,
   u.2.2.2.1 + v.2.2.2.1, u.2.2.2.2.1 + v.2.2.2.2.1, u.2.2.2.2.2 + v.2.2.2.2.2)
def v6scale (c : Int) (u : V6) : V6 :=
  (c*u.1, c*u.2.1, c*u.2.2.1, c*u.2.2.2.1, c*u.2.2.2.2.1, c*u.2.2.2.2.2)
def m9 (e : Nat) : V6 :=
  match e % 9 with
  | 0 => (1, 0, 0, 0, 0, 0) | 1 => (0, 1, 0, 0, 0, 0) | 2 => (0, 0, 1, 0, 0, 0)
  | 3 => (0, 0, 0, 1, 0, 0) | 4 => (0, 0, 0, 0, 1, 0) | 5 => (0, 0, 0, 0, 0, 1)
  | 6 => (-1, 0, 0, -1, 0, 0) | 7 => (0, -1, 0, 0, -1, 0) | _ => (0, 0, -1, 0, 0, -1)
def z6 : V6 := (0, 0, 0, 0, 0, 0)

def v16add (u v : List Int) : List Int := List.zipWith (· + ·) u v
def iscale (c : Int) (l : List Int) : List Int := l.map (fun x => c * x)
def m16 (e : Nat) : List Int :=
  match e % 16 with
  | 0 => [1,0,0,0,0,0,0,0] | 1 => [0,1,0,0,0,0,0,0] | 2 => [0,0,1,0,0,0,0,0]
  | 3 => [0,0,0,1,0,0,0,0] | 4 => [0,0,0,0,1,0,0,0] | 5 => [0,0,0,0,0,1,0,0]
  | 6 => [0,0,0,0,0,0,1,0] | 7 => [0,0,0,0,0,0,0,1] | 8 => [-1,0,0,0,0,0,0,0]
  | 9 => [0,-1,0,0,0,0,0,0] | 10 => [0,0,-1,0,0,0,0,0] | 11 => [0,0,0,-1,0,0,0,0]
  | 12 => [0,0,0,0,-1,0,0,0] | 13 => [0,0,0,0,0,-1,0,0] | 14 => [0,0,0,0,0,0,-1,0]
  | _ => [0,0,0,0,0,0,0,-1]

def cnt (N r : Nat) : Nat :=
  ((List.range N).filter (fun m => decide ((m*m) % N = r))).length

/-- THE POINT-COUNT IDENTITY (step A's formal finite half): the exponent fold
    equals the count-weighted assembly — the chart theta-object IS the theta
    series' formal rational-point data at the level — decided at N = 9 and
    N = 16, with the counts totalling N -/
theorem point_count_identity :
    ((List.range 9).foldl (fun acc m => v6add acc (m9 ((m*m) % 9))) z6 =
      (List.range 9).foldl (fun acc r =>
        v6add acc (v6scale (Int.ofNat (cnt 9 r)) (m9 r))) z6) ∧
    ((List.range 16).foldl (fun acc m => v16add acc (m16 ((m*m) % 16)))
        [0,0,0,0,0,0,0,0] =
      (List.range 16).foldl (fun acc r =>
        v16add acc (iscale (Int.ofNat (cnt 16 r)) (m16 r))) [0,0,0,0,0,0,0,0]) ∧
    ((List.range 9).foldl (fun acc r => acc + cnt 9 r) 0 = 9) ∧
    ((List.range 16).foldl (fun acc r => acc + cnt 16 r) 0 = 16) := by decide

/-- THE CUSP COUNT: c_N(0) = q at every banked cell — the count of solutions
    of m² ≡ 0 is exactly q = pⁿ (the zero residue's point count carries the
    banked values' real part; the classical naming NAVIGATOR-OPEN at the bank) -/
theorem cusp_count_instances :
    cnt 4 0 = 2 ∧ cnt 9 0 = 3 ∧ cnt 16 0 = 4 ∧ cnt 25 0 = 5 ∧
    cnt 64 0 = 8 ∧ cnt 81 0 = 9 ∧ cnt 256 0 = 16 ∧ cnt 729 0 = 27 := by decide

/-- THE TRANSFORMATION LAW'S FINITE SHADOW at the odd cell N = 9: for every k,
    Σ_m ζ^{m²+2mk} = ζ^{−k²}·G (G = 3, the banked value) — the completed
    square's identity, the odd functional-equation shadow; the place-2 twist
    is the metaplectic frame's territory, stated not forced -/
theorem transformation_shadow_odd :
    (List.range 9).map (fun k =>
      (List.range 9).foldl (fun acc m => v6add acc (m9 ((m*m + 2*m*k) % 9))) z6) =
    (List.range 9).map (fun k => v6scale 3 (m9 ((9 - (k*k) % 9) % 9))) := by
  decide

end ThetaBridgeShadow
