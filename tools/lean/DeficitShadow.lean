/-
  THE DEFICIT CLOSED FORM · DeficitShadow.lean
  =============================================

  Ferry 2026-08-21 (b56, component 1). Vanilla Lean 4 (v4.29.1 pinned), no imports;
  expected profile per terminal: "does not depend on any axioms".

  THE CLOSED FORM (derived longhand in the b56 registration from the b51
  character-average identity and its flat-place collapse — every banked roster
  contains an odd, flat place):

      4 · deficit(S)  =  ∏_v (q_v − 1)²  −  4 · Σ_v d₁(v)

  — the character-average global dimension minus the additive route's sum, in integer
  form. Compiled here: the six banked instances (R5's degenerate zero — the b55
  discriminator's ratified COINCIDENCE — through the extended roster's 37800), and the
  banked local d₁-laws' arithmetic (the even-place formula 2^(2n−2) − 2^(n−1) at
  n = 1..4; the odd flatness d₁ = (q−1)²/4 at the banked odd cells). The bridge
  question and its branch-(c) SPECIFICATION are bank- and trails-resident (b56).
-/

namespace DeficitShadow

/-- the six banked instances of the closed form, integer form, decided exactly -/
theorem closed_form_instances :
    (1 * 4 - 4 * (0 + 1) = 4 * 0) ∧
    (1 * 4 * 16 - 4 * (0 + 1 + 4) = 4 * 11) ∧
    (9 * 64 - 4 * (2 + 16) = 4 * 126) ∧
    (9 * 64 * 16 - 4 * (2 + 16 + 4) = 4 * 2282) ∧
    (49 * 64 * 16 - 4 * (12 + 16 + 4) = 4 * 12512) ∧
    (225 * 676 - 4 * (56 + 169) = 4 * 37800) := by decide

/-- the banked even-place d₁ law's arithmetic: 2^(2n−2) − 2^(n−1) = 0, 2, 12, 56 -/
theorem even_place_d1_law :
    (2^0 - 2^0 = 0) ∧ (2^2 - 2^1 = 2) ∧ (2^4 - 2^2 = 12) ∧ (2^6 - 2^3 = 56) := by decide

/-- the odd flatness instances: d₁ = (q−1)²/4 at the banked odd cells
    (4·d₁ = (q−1)² at (3,1), (5,1), (3,2), (3,3)) -/
theorem odd_flatness_d1 :
    (4 * 1 = 2^2) ∧ (4 * 4 = 4^2) ∧ (4 * 16 = 8^2) ∧ (4 * 169 = 26^2) := by decide

end DeficitShadow
