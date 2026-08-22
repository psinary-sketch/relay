/-
  THE COMPLEX-EXTENSION BUILD ACT'S DECIDED CORE · ExtensionShadow.lean
  ======================================================================

  Ferry 2026-08-22 (b97). Vanilla Lean 4 (v4.29.1 pinned), no imports; expected
  profile per terminal: "does not depend on any axioms".

  The build's finite decidable core (the analytic extension lives at its
  labeled grades in the bank and report, never here). THE PROBE PHASE PATTERN:
  n odd ⟹ n² ≡ 1 (mod 8), n even ⟹ n² ≡ 0 (mod 4) — why the registered
  probe's imaginary part reads the odd-n subseries with one constant phase
  (−i) and the even terms drop out. THE SCHWARZ WITNESS PAIRING: in ℤ/16
  exponents, conjugation e ↦ (16−e) sends the row-40 witness exponents {2, 6}
  to {14, 10} and doubling swaps the square-classes {4, 12} (i ↔ −i)
  coherently, all fourth powers landing at 8 (= −1). THE PRODUCT-1 MIRROR:
  the witness times its conjugate is 1 at both sectors — the
  relative-conjugacy relation's finite shadow; the ζ₈ anchor exponent
  16/8 = 2 is the plus witness exponent (row 48's plus sign, cited). THE
  FINITE BREAKING at level 16: the gaussian fold = 4e₀ + 4e₄ (= 4(1+i), the
  banked place-2 trace shape) while its conjugate fold = 4e₀ − 4e₄ — the fold
  differs from its conjugate: the finite shadow of the archimedean breaking.
  Bank: relay data/b97_complex_extension_build.txt.
-/

set_option maxRecDepth 8192

namespace ExtensionShadow

def m16 (e : Nat) : List Int :=
  match e % 16 with
  | 0 => [1,0,0,0,0,0,0,0] | 1 => [0,1,0,0,0,0,0,0] | 2 => [0,0,1,0,0,0,0,0]
  | 3 => [0,0,0,1,0,0,0,0] | 4 => [0,0,0,0,1,0,0,0] | 5 => [0,0,0,0,0,1,0,0]
  | 6 => [0,0,0,0,0,0,1,0] | 7 => [0,0,0,0,0,0,0,1] | 8 => [-1,0,0,0,0,0,0,0]
  | 9 => [0,-1,0,0,0,0,0,0] | 10 => [0,0,-1,0,0,0,0,0] | 11 => [0,0,0,-1,0,0,0,0]
  | 12 => [0,0,0,0,-1,0,0,0] | 13 => [0,0,0,0,0,-1,0,0] | 14 => [0,0,0,0,0,0,-1,0]
  | _ => [0,0,0,0,0,0,0,-1]
def vadd (u v : List Int) : List Int := List.zipWith (· + ·) u v
def z8 : List Int := [0,0,0,0,0,0,0,0]

/-- THE PROBE PHASE PATTERN: for every n < 256 — n odd ⟹ n² ≡ 1 (mod 8) and
    n even ⟹ n² ≡ 0 (mod 4): the registered probe's imaginary part is the
    odd-n subseries at one constant phase, the even terms real -/
theorem probe_phase_instances :
    (List.range 256).all (fun n =>
      (if n % 2 = 1 then decide ((n*n) % 8 = 1) else decide ((n*n) % 4 = 0))) =
    true := by decide

/-- THE SCHWARZ WITNESS PAIRING in ℤ/16 exponents: conjugation sends the
    witness exponents {2, 6} to {14, 10}; doubling (squaring the root) swaps
    the square-classes 4 ↔ 12 (i ↔ −i) coherently; all four fourth powers
    land at 8 (= −1) — conjugation exchanges the two twisted sectors and
    their square-root witnesses as one operation -/
theorem schwarz_witness_pairing :
    ((16 - 2) % 16 = 14) ∧ ((16 - 6) % 16 = 10) ∧
    ((2*2) % 16 = 4) ∧ ((2*6) % 16 = 12) ∧
    ((2*14) % 16 = 12) ∧ ((2*10) % 16 = 4) ∧
    ((4*2) % 16 = 8) ∧ ((4*6) % 16 = 8) ∧
    ((4*14) % 16 = 8) ∧ ((4*10) % 16 = 8) := by decide

/-- THE PRODUCT-1 MIRROR RELATION: the witness times its conjugate is 1 at
    both twisted sectors ((2+14) ≡ (6+10) ≡ 0 mod 16) — the finite shadow of
    the relative-conjugacy relation; and the ζ₈ anchor exponent 16/8 = 2 IS
    the plus witness exponent (row 48's plus sign, cited never re-derived) -/
theorem mirror_product_one :
    ((2 + 14) % 16 = 0) ∧ ((6 + 10) % 16 = 0) ∧ (16 / 8 = 2) := by decide

/-- THE FINITE BREAKING at level 16: the gaussian fold Σ_m ζ^{m²} equals
    4e₀ + 4e₄ (the banked place-2 trace shape 4(1+i)) while the conjugate
    fold Σ_m ζ^{−m²} equals 4e₀ − 4e₄ — the fold differs from its conjugate:
    the finite shadow, at the even cell, of the extension's archimedean
    breaking (conjugation acting freely off the fixed locus) -/
theorem finite_breaking_16 :
    ((List.range 16).foldl (fun acc m => vadd acc (m16 ((m*m) % 16))) z8 =
      [4,0,0,0,4,0,0,0]) ∧
    ((List.range 16).foldl (fun acc m => vadd acc (m16 ((16 - (m*m) % 16) % 16))) z8 =
      [4,0,0,0,-4,0,0,0]) := by decide

end ExtensionShadow
