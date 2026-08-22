/-
  THE CONSTRUCTOR ACT'S DECIDED CORE · ConstructorShadow.lean
  ============================================================

  Ferry 2026-08-22 (b90). Vanilla Lean 4 (v4.29.1 pinned), no imports; expected
  profile per terminal: "does not depend on any axioms".

  The build's finite decidable core (the analytic side lives at its labeled
  grades in the bank and report, never here). AG-1's extension at the odd
  depth-1 cell: the point-count identity at N = 25 in ℤ[ζ₂₅]
  twenty-coordinates (Φ₂₅ = x²⁰+x¹⁵+x¹⁰+x⁵+1) WITH the total 5·e₀ = q — the
  odd Gauss value decided. AG-3's extension: the completed-square shift law at
  N = 25 for every k. AG-6, the silhouette exam (the sanctioned comparison's
  first opening): the six banked deficits reproduced from the object's own
  boundary data (the cusp table), exactly. And the strikeable: N5's
  vector-level identity — the compressed transfer's radialized defect is
  carried entirely by the t = 0 line onto the model's boundary cell (q·e_n),
  the twisted defect member R-silent — decided in integer coefficient lists at
  (2,2) with the b66 banked value reproduced, and at (2,1).
  Bank: relay data/b90_constructor.txt.
-/

set_option maxRecDepth 8192

namespace ConstructorShadow

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
def cnt25 (r : Nat) : Nat :=
  ((List.range 25).filter (fun m => decide ((m*m) % 25 = r))).length

/-- AG-1's extension at (5,1): the point-count identity at N = 25 AND the
    total = 5·e₀ = q (the odd Gauss value, decided in twenty-coordinates);
    the counts total N -/
theorem point_count_identity_25 :
    ((List.range 25).foldl (fun acc m => vadd acc (m25 ((m*m) % 25))) z20 =
      (List.range 25).foldl (fun acc r =>
        vadd acc (iscale (Int.ofNat (cnt25 r)) (m25 r))) z20) ∧
    ((List.range 25).foldl (fun acc m => vadd acc (m25 ((m*m) % 25))) z20 =
      (5 : Int) :: (List.range 19).map (fun _ => (0 : Int))) ∧
    ((List.range 25).foldl (fun acc r => acc + cnt25 r) 0 = 25) := by decide

/-- AG-3's extension: the completed-square shift law at N = 25 for every k —
    Σ_m ζ^{m²+2mk} = ζ^{−k²}·G with G = 5·e₀ the decided total -/
theorem shift_shadow_25 :
    (List.range 25).map (fun k =>
      (List.range 25).foldl (fun acc m => vadd acc (m25 ((m*m + 2*m*k) % 25))) z20) =
    (List.range 25).map (fun k => iscale 5 (m25 ((25 - (k*k) % 25) % 25))) := by
  decide

/-- AG-6, THE SILHOUETTE EXAM (the sanctioned comparison's first opening): the
    six banked deficits reproduced from the object's own boundary data — the
    cusp counts q — through the product law's ledger, exactly:
    ∏(q_v − 1)² = 4·(Σd₁ + deficit) at all six rosters -/
theorem silhouette_exam :
    ((2-1)*(2-1)*(3-1)*(3-1) = 4*(1 + 0)) ∧
    ((2-1)*(2-1)*(3-1)*(3-1)*(5-1)*(5-1) = 4*(5 + 11)) ∧
    ((4-1)*(4-1)*(9-1)*(9-1) = 4*(18 + 126)) ∧
    ((4-1)*(4-1)*(9-1)*(9-1)*(5-1)*(5-1) = 4*(22 + 2282)) ∧
    ((8-1)*(8-1)*(9-1)*(9-1)*(5-1)*(5-1) = 4*(32 + 12512)) ∧
    ((16-1)*(16-1)*(27-1)*(27-1) = 4*(225 + 37800)) := by decide

def nthI (l : List Int) : Nat → Int
  | 0 => match l with | [] => 0 | a :: _ => a
  | n+1 => match l with | [] => 0 | _ :: t => nthI t n
def Vv16 (v : List Int) : List Int :=
  (List.range 16).map (fun j =>
    ((List.range 16).filter (fun m => decide ((2*m) % 16 = j))).foldl
      (fun a m => a + nthI v m) 0)
def shell16 (m : Nat) : Nat :=
  if m = 0 then 4 else
  match Nat.gcd m 16 with
  | 1 => 0 | 2 => 1 | 4 => 2 | 8 => 3 | _ => 4
def Rv16 (v : List Int) : List Int :=
  (List.range 5).map (fun s =>
    ((List.range 16).filter (fun m => decide (shell16 m = s))).foldl
      (fun a m => a + nthI v m) 0)
def Vv4 (v : List Int) : List Int :=
  (List.range 4).map (fun j =>
    ((List.range 4).filter (fun m => decide ((2*m) % 4 = j))).foldl
      (fun a m => a + nthI v m) 0)
def shell4 (m : Nat) : Nat :=
  if m = 0 then 2 else match Nat.gcd m 4 with | 1 => 0 | 2 => 1 | _ => 2
def Rv4 (v : List Int) : List Int :=
  (List.range 3).map (fun s =>
    ((List.range 4).filter (fun m => decide (shell4 m = s))).foldl
      (fun a m => a + nthI v m) 0)

def g20v : List Int := [0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0]
def g22v : List Int := [0,0,1,0,0,0,-1,0,0,0,1,0,0,0,-1,0]
def g10v : List Int := [0,1,0,1]
def g11v : List Int := [0,1,0,-1]

/-- N5'S VECTOR-LEVEL IDENTITY (the strikeable; row 41's residue): at (2,2)
    the transfer of the twisted exit row reproduces the b66 banked value
    2δ₄ − 2δ₁₂ and is R-SILENT, while the t = 0 line's transfer radializes to
    exactly the model's boundary cell q·e_n = 4·e₂; at (2,1) the same with
    2·e₁ and the primitive kill — the compressed transfer's radialized defect
    IS the model's boundary line, decided -/
theorem defect_vector_identity :
    (Vv16 g22v = [0,0,0,0,2,0,0,0,0,0,0,0,-2,0,0,0]) ∧
    (Rv16 (Vv16 g20v) = [0,0,4,0,0]) ∧
    (Rv16 (Vv16 g22v) = [0,0,0,0,0]) ∧
    (Vv4 g10v = [0,0,2,0]) ∧ (Rv4 (Vv4 g10v) = [0,2,0]) ∧
    (Vv4 g11v = [0,0,0,0]) := by decide

end ConstructorShadow
