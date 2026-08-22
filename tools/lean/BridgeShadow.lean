/-
  THE BRIDGE-HALF ACT'S DECIDED CORE · BridgeShadow.lean
  =======================================================

  Ferry 2026-08-22 (b93). Vanilla Lean 4 (v4.29.1 pinned), no imports; expected
  profile per terminal: "does not depend on any axioms".

  The bridge run's finite decidable core (the analytic law lives at its labeled
  grades in the bank and report, never here). THE MIRROR LAWS: the F ↦ F³ image
  of the completed-square shift law — Σ_m ζ^{−(m²+2mk)} = ζ^{+k²}·G for every
  k — decided at N = 9 (G = 3, six-coords) and N = 25 (G = 5, twenty-coords):
  the derived transformation law's finite shadow and its conjugate BOTH hold,
  the finite exercise of row 50's orientation audit on the new law. THE MIRROR
  GAUSS VALUES: Σ_m ζ^{−m²} = q·e₀ at both odd cells — the multiplier itself
  mirror-fixed. THE ROUND TRIP at N = 9: Σ_k Σ_m ζ^{m²+2mk+2kj} = N·ζ^{j²} for
  every j — the double transform, the finite shadow of the multiplier-magnitude
  law |G|² = N (the x^{−1/2}·x^{+1/2} = 1 round trip of the derived law).
  Bank: relay data/b93_bridge_half.txt.
-/

set_option maxRecDepth 8192

namespace BridgeShadow

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

def m25 (e : Nat) : List Int :=
  let r := e % 25
  if r < 20 then (List.range 20).map (fun i => if i = r then (1 : Int) else 0)
  else
    let k := r - 20
    (List.range 20).map (fun i =>
      if i = k ∨ i = k + 5 ∨ i = k + 10 ∨ i = k + 15 then (-1 : Int) else 0)
def vadd (u v : List Int) : List Int := List.zipWith (· + ·) u v
def iscale (c : Int) (l : List Int) : List Int := l.map (fun x => c * x)
def z20 : List Int := (List.range 20).map (fun _ => (0 : Int))

/-- THE MIRROR LAW at N = 9: the F ↦ F³ image of the completed-square shift
    law — for every k, Σ_m ζ^{−(m²+2mk)} = ζ^{+k²}·3 — decided; with row 59's
    original this is the finite exercise of the orientation audit: the law's
    finite shadow and its conjugate both hold -/
theorem mirror_shadow_9 :
    (List.range 9).map (fun k =>
      (List.range 9).foldl (fun acc m =>
        v6add acc (m9 ((9 - (m*m + 2*m*k) % 9) % 9))) z6) =
    (List.range 9).map (fun k => v6scale 3 (m9 ((k*k) % 9))) := by
  decide

/-- THE MIRROR LAW at N = 25: for every k, Σ_m ζ^{−(m²+2mk)} = ζ^{+k²}·5 —
    the conjugated completed square at the odd depth-1 cell, decided in
    twenty-coordinates -/
theorem mirror_shadow_25 :
    (List.range 25).map (fun k =>
      (List.range 25).foldl (fun acc m =>
        vadd acc (m25 ((25 - (m*m + 2*m*k) % 25) % 25))) z20) =
    (List.range 25).map (fun k => iscale 5 (m25 ((k*k) % 25))) := by
  decide

/-- THE MIRROR GAUSS VALUES: Σ_m ζ^{−m²} = q·e₀ at N = 9 and N = 25 — the
    conjugated Gauss value equals the original (+q, the trivial branch): the
    derived law's multiplier is itself mirror-fixed at the banked odd cells -/
theorem mirror_gauss_values :
    ((List.range 9).foldl (fun acc m =>
      v6add acc (m9 ((9 - (m*m) % 9) % 9))) z6 = (3, 0, 0, 0, 0, 0)) ∧
    ((List.range 25).foldl (fun acc m =>
      vadd acc (m25 ((25 - (m*m) % 25) % 25))) z20 =
        (5 : Int) :: (List.range 19).map (fun _ => (0 : Int))) := by
  decide

/-- THE ROUND TRIP at N = 9: for every j, Σ_k Σ_m ζ^{m²+2mk+2kj} = 9·ζ^{j²} —
    the double transform returns the square with the full mass N: the finite
    shadow of the multiplier-magnitude law |G|² = N (the derived law applied
    twice, x^{−1/2}·x^{+1/2} = 1) -/
theorem round_trip_shadow_9 :
    (List.range 9).map (fun j =>
      (List.range 9).foldl (fun acc k =>
        (List.range 9).foldl (fun a m =>
          v6add a (m9 ((m*m + 2*m*k + 2*k*j) % 9))) acc) z6) =
    (List.range 9).map (fun j => v6scale 9 (m9 ((j*j) % 9))) := by
  decide

end BridgeShadow
