/-
  THE CROSS-PLACE ACT · CrossPlaceShadow.lean — THE SECTOR-DIMENSION PRODUCT FORMULA
  ===================================================================================

  Ferry 2026-08-20 (b51). Vanilla Lean 4 (v4.29.1 pinned), no imports; expected
  profile per terminal: "does not depend on any axioms".

  WHAT THIS MODULE COMPILES — the b51 branch-(a) survivor at theorem shape:

  (1) THE FLAT-PLACE COLLAPSE, general dims: over the four-element eigenvalue group
      {1, −1, i, −i}, the two-place sector-sum dimension Σ_{λμ=1} d(λ)·e(μ) pairs each
      μ with the forced λ = μ⁻¹; if one place is FLAT (all four dims equal c), the sum
      is c·(e₁ + e₋₁ + eᵢ + e₋ᵢ) = c · dim — the mechanism behind the b51 collapse
      D_global = (1/4)·∏ dims on any roster containing an odd (flat) place. Stated
      with the four compatible pairs enumerated explicitly ((1,1), (−1,−1), (i,−i),
      (−i,i)); general natural-number dims.

  (2) THE COLLAPSE INSTANCES at the five registered rosters (banked dims): the direct
      pattern enumeration over all sign patterns with unit product equals ∏ dims / 4 —
      decided exactly (R1: 16·4 = 64; R2: 144·4 = 576; R3: 2304·4 = 9216;
      R4: 12544·4 = 50176; R5: 1·4 = 4).

  WHAT IT DOES NOT COMPILE, DECLARED: the general character-sum identity over μ₄ (the
  ℤ[i]-valued four-term average) — bench-verified exactly at every registered roster
  (b51, with the trace products vanishing by flatness); its general statement is a
  NAMED OPEN STATEMENT in the correspondence. The leaves distinction stands: this is
  COMPATIBILITY structure (a character-average of products), not factorization.
-/

namespace CrossPlaceShadow

/-- (1) the flat-place collapse, general dims: the four compatible pairs (λ, λ⁻¹),
    flat place contributing c at every forced eigenvalue -/
theorem flat_place_collapse (c e1 em1 ei emi : Nat) :
    c * e1 + c * em1 + c * emi + c * ei = c * (e1 + em1 + ei + emi) := by
  rw [Nat.mul_add, Nat.mul_add, Nat.mul_add, Nat.add_right_comm]

/-- eigenvalues as exponents of i (0:1, 2:−1, 1:i, 3:−i); a pattern is compatible when
    the exponent sum vanishes mod 4 -/
def patternSum (dims : List (Nat × Nat × Nat × Nat)) : Nat :=
  let exp : Nat → Nat
    | 0 => 0 | 1 => 2 | 2 => 1 | _ => 3
  let pick : Nat → (Nat × Nat × Nat × Nat) → Nat
    | 0, (a, _, _, _) => a | 1, (_, b, _, _) => b
    | 2, (_, _, c, _) => c | _, (_, _, _, d) => d
  let rec go : List (Nat × Nat × Nat × Nat) → Nat → Nat
    | [], acc => if acc % 4 == 0 then 1 else 0
    | d :: rest, acc =>
        (List.range 4).foldl (fun s j =>
          s + pick j d * go rest ((acc + exp j) % 4)) 0
  go dims 0

/-- helper: the product of total dims over a roster -/
def dimProd (dims : List (Nat × Nat × Nat × Nat)) : Nat :=
  dims.foldl (fun s (a, b, c, d) => s * (a + b + c + d)) 1

/-- (2) the collapse at the five registered rosters, banked dims, decided exactly:
    4 · D_global = ∏ dims (R1, R2, R3, R4, R5 of the b51 registration) -/
theorem collapse_instances :
    (4 * patternSum [(0,0,1,0), (1,1,1,1), (4,4,4,4)] = dimProd [(0,0,1,0), (1,1,1,1), (4,4,4,4)]) ∧
    (4 * patternSum [(2,2,3,2), (16,16,16,16)] = dimProd [(2,2,3,2), (16,16,16,16)]) ∧
    (4 * patternSum [(2,2,3,2), (16,16,16,16), (4,4,4,4)] = dimProd [(2,2,3,2), (16,16,16,16), (4,4,4,4)]) ∧
    (4 * patternSum [(12,12,13,12), (16,16,16,16), (4,4,4,4)] = dimProd [(12,12,13,12), (16,16,16,16), (4,4,4,4)]) ∧
    (4 * patternSum [(0,0,1,0), (1,1,1,1)] = dimProd [(0,0,1,0), (1,1,1,1)]) := by
  decide

/-- the banked global dimensions themselves, decided (16, 144, 2304, 12544, 1) -/
theorem banked_globals :
    (patternSum [(0,0,1,0), (1,1,1,1), (4,4,4,4)] = 16) ∧
    (patternSum [(2,2,3,2), (16,16,16,16)] = 144) ∧
    (patternSum [(2,2,3,2), (16,16,16,16), (4,4,4,4)] = 2304) ∧
    (patternSum [(12,12,13,12), (16,16,16,16), (4,4,4,4)] = 12544) ∧
    (patternSum [(0,0,1,0), (1,1,1,1)] = 1) := by
  decide

end CrossPlaceShadow
