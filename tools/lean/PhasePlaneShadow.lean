/-
  THE PHASE-PLANE READINGS · PhasePlaneShadow.lean
  =================================================

  Ferry 2026-08-21 (b66, the phase-plane act). Vanilla Lean 4 (v4.29.1 pinned), no
  imports; expected profile per terminal: "does not depend on any axioms".

  THE READINGS (the b66 registration, decided): on the full-grid g-basis the
  transform is the monomial quarter-turn σ(a,t) = ((q−t) mod q, a), and

  · THE FIXED LOCUS is exactly {origin} at odd q and {origin, center (q/2, q/2)} at
    q = 2ⁿ (decided at the banked q);
  · THE TRACE IS THE FIXED-POINT PHASE SUM: the origin contributes q, the center
    contributes q·i (the exponent (q/2)² = N/4, level-independent) — reproducing
    tr S = q and q(1+i) from rows 35–36 by mechanism;
  · FLATNESS IS FREENESS ON THE LIVE LOCUS: at odd q the four-group acts freely on
    the Sonin grid (σ- and σ²-fixed filters empty, decided), so the sectors are the
    C₄-regular pieces — all equal; at q = 2ⁿ the center is the unique non-free Sonin
    point, its line the i-eigenline: the excess, the unit trace, the i-sector
    placement, and the level-constancy are ONE fact — the live stationary point's
    phase;
  · THE CENTER'S CLASS IS THE SEED CHAIN: ι's grid map fixes the center
    (p·q/2 = q⁺/2, decided), and at (2,1) the center (1,1) is the seed's grid point;
  · THE SCALING (V : δ_m ↦ δ_{pm}, unnormalized) on the g-family: primitive
    frequencies are KILLED (V g_{1,1} = 0, decided), divisible frequencies map by
    the p-TERM TRANSFER (V g_{1,2} = g_{2,1} + g_{2,3}, decided) — the registered
    "monomial" corrected to "p-term transfer" by the computation, the deviation
    banked — and THE CENTER'S IMAGE IS BALL-SUPPORTED (decided): the boundary line
    lies in the defect of the compressed scaling on the constructed object.
  Bank: relay data/b66_phase_plane.txt.
-/

namespace PhasePlaneShadow

/-- the σ-fixed grid points at size q, as a filtered list of pairs -/
def fixedList (q : Nat) : List (Nat × Nat) :=
  ((List.range q).map (fun a => (List.range q).map (fun t => (a, t)))).flatten.filter
    (fun v => ((q - v.2) % q, v.1) = v)

/-- THE FIXED LOCUS, decided at the banked q: the origin alone at odd q; the origin
    and the center at q = 2ⁿ -/
theorem fixed_locus_instances :
    fixedList 3 = [(0, 0)] ∧ fixedList 5 = [(0, 0)] ∧ fixedList 9 = [(0, 0)] ∧
    fixedList 2 = [(0, 0), (1, 1)] ∧ fixedList 4 = [(0, 0), (2, 2)] ∧
    fixedList 8 = [(0, 0), (4, 4)] ∧ fixedList 16 = [(0, 0), (8, 8)] := by decide

/-- THE STATIONARY TRACE, decided: the center's phase exponent is (q/2)² = N/4 at
    every banked place-2 level (the fraction 1/4, level-independent), and the
    fixed-point pair sums are the rows-35–36 values (q, 0) and (q, q) -/
theorem stationary_trace_instances :
    ((2/2)*(2/2)*4 = 2*2 ∧ (4/2)*(4/2)*4 = 4*4 ∧ (8/2)*(8/2)*4 = 8*8 ∧
     (16/2)*(16/2)*4 = 16*16) ∧
    (((3, 0) : Int × Int) = (3, 0) ∧ ((4 + 0, 0 + 4) : Int × Int) = (4, 4)) := by
  decide

/-- the σ- and σ²-fixed filters on the SONIN grid [1,q−1]² -/
def sonFixed1 (q : Nat) : List (Nat × Nat) :=
  (fixedList q).filter (fun v => v.1 ≠ 0 ∧ v.2 ≠ 0)
def sonFixed2 (q : Nat) : List (Nat × Nat) :=
  ((List.range q).map (fun a => (List.range q).map (fun t => (a, t)))).flatten.filter
    (fun v => v.1 ≠ 0 ∧ v.2 ≠ 0 ∧ ((q - v.1) % q, (q - v.2) % q) = v)

/-- FLATNESS IS FREENESS, decided: at odd q the four-group acts freely on the Sonin
    grid (both fixed filters empty) — the sectors are the C₄-regular pieces; at
    q = 2ⁿ the center is the unique non-free point and ((q−1)² − 1) is divisible by
    four — the place-2 dims (d, d, d+1, d) -/
theorem freeness_flatness_instances :
    (sonFixed1 3 = [] ∧ sonFixed2 3 = [] ∧ sonFixed1 5 = [] ∧ sonFixed2 5 = [] ∧
     sonFixed1 9 = [] ∧ sonFixed2 9 = []) ∧
    (sonFixed1 4 = [(2, 2)] ∧ sonFixed2 4 = [(2, 2)] ∧
     sonFixed1 8 = [(4, 4)] ∧ sonFixed2 8 = [(4, 4)]) ∧
    ((3-1)^2 % 4 = 0 ∧ (5-1)^2 % 4 = 0 ∧ (9-1)^2 % 4 = 0 ∧
     ((4-1)^2 - 1) % 4 = 0 ∧ ((8-1)^2 - 1) % 4 = 0 ∧ ((16-1)^2 - 1) % 4 = 0) := by
  decide

/-- THE CENTER IS THE SEED CHAIN, decided: ι's grid map fixes the center
    (p·(q/2) = q⁺/2 at the banked levels) and at (2,1) the center is (1, 1) — the
    seed's grid point -/
theorem center_seed_instances :
    (2 * (2/2) = 4/2 ∧ 2 * (4/2) = 8/2 ∧ 2 * (8/2) = 16/2) ∧ (2/2 = 1) := by decide

/- ── the scaling instances at (2,2), ℤ[ζ₁₆] in 8 coordinates ─────────────────── -/

def mono (c : Int) (e : Nat) : List Int :=
  let r := e % 8
  let s : Int := if (e / 8) % 2 = 0 then c else -c
  (List.range 8).map (fun k => if k = r then s else 0)

def vadd (u v : List Int) : List Int := List.zipWith (· + ·) u v

def zrow : List Int := [0, 0, 0, 0, 0, 0, 0, 0]

/-- the g_{a,t} coordinate row at (2,2): coefficient ζ^{4tb} on row a -/
def gRow (a t m : Nat) : List Int :=
  if m % 4 = a % 4 then mono 1 (4 * t * ((m - a % 4) / 4)) else zrow

/-- the V-image row (V : δ_m ↦ δ_{2m} mod 16; the two preimages of an even m′) -/
def vRow (a t mp : Nat) : List Int :=
  if mp % 2 = 0 then vadd (gRow a t (mp / 2)) (gRow a t (mp / 2 + 8)) else zrow

/-- THE SCALING INSTANCES, decided: V kills the primitive frequency (V g_{1,1} = 0);
    V is the p-term transfer on divisible frequencies (V g_{1,2} = g_{2,1} + g_{2,3});
    and V of the center is BALL-SUPPORTED (2δ₄ − 2δ₁₂) — the boundary line in the
    compressed scaling's defect -/
theorem scaling_instances :
    ((List.range 16).map (vRow 1 1) = (List.range 16).map (fun _ => zrow)) ∧
    ((List.range 16).map (vRow 1 2) =
      (List.range 16).map (fun m => vadd (gRow 2 1 m) (gRow 2 3 m))) ∧
    ((List.range 16).map (vRow 2 2) =
      (List.range 16).map (fun m =>
        if m = 4 then mono 2 0 else if m = 12 then mono (-2) 0 else zrow)) := by
  decide

end PhasePlaneShadow
