/-
  THE TWISTED-PROJECTOR EXTENSION · TwistedShadow.lean — THE DECIDABLE CORES
  ===========================================================================

  Ferry 2026-08-21 (b53/b54). Vanilla Lean 4 (v4.29.1 pinned), imports sibling Core
  modules only; expected profile per terminal: "does not depend on any axioms".

  (1) THE MIXED-PATTERN COUNTS (b54 P3), decided at the five registered rosters:
      mixed = (the sector-sum enumeration) − (the principal product) — the banked dims,
      the CrossPlaceShadow enumeration, exact integers (1, 16, 112, 2176, 11776).

  (2) THE TOWER-IMPORTED PURE WITNESS (the b53 finding, banked): the vector
      ι(u_i^{(2,1)}) ∈ E_i(2,2) — the tower image of the dead cell's single E_i
      generator — encoded from the b53 construction (h = f − Πf at (2,1):
      h = {3: 2, 1: −2}; u_i[m] = 2·h(m) + ζ₄·(−(Sh)(m)), value-copied through the
      chart refinement with ζ₄ = ζ₁₆⁴), and its two decidable properties:
      · ALL 2×2 minors vanish exactly in ℤ[ζ₁₆] — PURE (the single-row support);
      · it is an exact i-eigenvector: S·w = ζ₁₆⁴·4·w on its support — E_i membership.
      The finding's mechanism (purity imported through ι from the 1×1 boundary shape)
      is banked prose; these are its kernel-checkable cores.
-/

import E1UnitPurityDraft
import CrossPlaceShadow

set_option maxRecDepth 8192
set_option maxHeartbeats 1600000

namespace TwistedShadow

open E1UnitPurityDraft

/-- (1) the mixed-pattern counts at the five registered rosters:
    patternSum − principal product, decided (b54 P3) -/
theorem mixed_pattern_counts :
    (CrossPlaceShadow.patternSum [(0,0,1,0), (1,1,1,1)] - 0 * 1 = 1) ∧
    (CrossPlaceShadow.patternSum [(0,0,1,0), (1,1,1,1), (4,4,4,4)] - 0 * 1 * 4 = 16) ∧
    (CrossPlaceShadow.patternSum [(2,2,3,2), (16,16,16,16)] - 2 * 16 = 112) ∧
    (CrossPlaceShadow.patternSum [(2,2,3,2), (16,16,16,16), (4,4,4,4)] - 2 * 16 * 4 = 2176) ∧
    (CrossPlaceShadow.patternSum [(12,12,13,12), (16,16,16,16), (4,4,4,4)] - 12 * 16 * 4 = 11776) := by
  decide

/-- the tower-imported witness in E_i(2,2), from the b53 construction: support on the
    single position row a = 2 of the (2,2) chart (m = a + 4b), entries in ℤ[ζ₁₆] with
    ζ₄ = ζ₁₆⁴; the (2,1) data: h = {3: 2, 1: −2}, u_i[m] = 2h(m) + ζ₄·(−(Sh)(m)),
    (Sh)(m′) = 2ζ₄^{3m′} − 2ζ₄^{m′}, value-copied to (2a, b + 2j) -/
def towerWitness : Nat → Sp
  | 2  => [(-4, 0), (2, 8), (-2, 0)]    -- m = 2  = (a,b) = (2,0): emb u_i(2,1)[1]
  | 6  => [(4, 0), (-2, 8), (2, 0)]     -- m = 6  = (2,1): emb u_i(2,1)[3]
  | 10 => [(-4, 0), (2, 8), (-2, 0)]    -- m = 10 = (2,2): copy of [1]
  | 14 => [(4, 0), (-2, 8), (2, 0)]     -- m = 14 = (2,3): copy of [3]
  | _  => []

/-- (2a) PURE: every 2×2 minor of the witness's chart matrix vanishes exactly —
    the single-row support makes every minor a product involving a zero row -/
theorem tower_witness_pure :
    ((List.range 4).all fun a1 => (List.range 4).all fun a2 =>
      (List.range 4).all fun b1 => (List.range 4).all fun b2 =>
        if decide (a1 < a2) && decide (b1 < b2) then
        isZero 2 16 (subSp
          (mulSp (towerWitness ((a1 + 4*b1) % 16)) (towerWitness ((a2 + 4*b2) % 16)))
          (mulSp (towerWitness ((a1 + 4*b2) % 16)) (towerWitness ((a2 + 4*b1) % 16))))
        else true) = true := by
  decide

/-- (2b) E_i MEMBERSHIP: S·w = ζ₁₆⁴·4·w — the exact i-eigenvector identity, entrywise
    (S w)(m′) = Σ_m w(m)·ζ^{m m′}, compared with 4·ζ⁴·w(m′) -/
theorem tower_witness_in_Ei :
    ((List.range 16).all fun mp =>
      isZero 2 16 (subSp
        ((List.range 16).foldl (fun acc m =>
          acc ++ (towerWitness m).map (fun p => (p.1, p.2 + m * mp))) [])
        ((towerWitness mp).map (fun p => (4 * p.1, p.2 + 4))))) = true := by
  decide

end TwistedShadow
