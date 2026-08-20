/-
  THE LEAVES QUESTION · TensorSquareShadow.lean — THE VANILLA LEG (zero axioms)
  =============================================================================

  The two-leg ruling (Rule 5) governs: VANILLA leg — vanilla Lean 4 (v4.29.1 pinned),
  decide only, expected profile per terminal: "does not depend on any axioms".
  THE KERNEL-PURITY RULING governs: no sorry; only proved decide instances.

  WHAT THIS MODULE COMPILES — the finite content the leaves-question answer names:

  (1) THE INTERLEAVING INDEX LAW — the arithmetic core of the local tensor square
      (B13: Son(p,n) = V₁ ⊗ W₁ with the transform interleaving the factors): under
      the index splitting m = a + pⁿ·b of ℤ/p^{2n}, the DFT exponent factors as
          m·m′ ≡ a·a′ + pⁿ·(a·b′ + a′·b)   (mod p^{2n})
      — the transform couples the two factors ONLY through the middle bilinear term
      (the p^{2n}·b·b′ term dies mod p^{2n}). Compiled at (2,1), (3,1), (2,2), (5,1):
      every index tuple, exact.

  (2) THE SECTOR-PATTERN COUNT — the combinatorial core of the PROVED obstruction:
      over k places each carrying both ±1 sectors, the global E₁ (the ∏λ_v = +1
      sector sum, act 1's banked finding) admits 2^{k−1} sign patterns, of which the
      tensor-square diagonal (⊗′E₁,v) sees exactly ONE (all-plus): the strict gap
      2^{k−1} > 1 for every k ≥ 2 — the mixed patterns ((−1)(−1) = +1, …) are the
      part of the constrained sector that NO placewise tensor structure carries.
      (The nonemptiness of the −1 sectors at the banked cells is instrument-banked:
      b33 at ∞; the finite four-sector data — cited, not recompiled.)
-/

namespace TensorSquareShadow

/-- (1) the interleaving index law at the banked cells — every tuple, exact. -/
theorem interleaving_index_law :
    (((List.range 2).all fun a => (List.range 2).all fun b =>
       (List.range 2).all fun a' => (List.range 2).all fun b' =>
        ((a + 2*b) * (a' + 2*b')) % 4 == (a*a' + 2*(a*b' + a'*b)) % 4) &&
     ((List.range 3).all fun a => (List.range 3).all fun b =>
       (List.range 3).all fun a' => (List.range 3).all fun b' =>
        ((a + 3*b) * (a' + 3*b')) % 9 == (a*a' + 3*(a*b' + a'*b)) % 9) &&
     ((List.range 4).all fun a => (List.range 4).all fun b =>
       (List.range 4).all fun a' => (List.range 4).all fun b' =>
        ((a + 4*b) * (a' + 4*b')) % 16 == (a*a' + 4*(a*b' + a'*b)) % 16) &&
     ((List.range 5).all fun a => (List.range 5).all fun b =>
       (List.range 5).all fun a' => (List.range 5).all fun b' =>
        ((a + 5*b) * (a' + 5*b')) % 25 == (a*a' + 5*(a*b' + a'*b)) % 25)) = true := by
  decide

/-- (2) the sector-pattern gap: ∏ = +1 patterns number 2^{k−1}; the all-plus diagonal
    is ONE of them — strict for every k ≥ 2 (instances k = 2, 3, 4; signs encoded as
    bits, product +1 ⟺ even bit-sum). -/
theorem sector_pattern_gap :
    ((((List.range 4).filter fun s => (s % 2 + s / 2 % 2) % 2 == 0).length == 2) &&
     (2 > 1) &&
     (((List.range 8).filter fun s =>
        (s % 2 + s / 2 % 2 + s / 4 % 2) % 2 == 0).length == 4) &&
     (4 > 1) &&
     (((List.range 16).filter fun s =>
        (s % 2 + s / 2 % 2 + s / 4 % 2 + s / 8 % 2) % 2 == 0).length == 8) &&
     (8 > 1)) = true := by decide

end TensorSquareShadow
