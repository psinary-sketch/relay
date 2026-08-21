/-
  THE COHERENCE ACT'S DECIDED CORE · CoherenceShadow.lean
  ========================================================

  Ferry 2026-08-21 (b71). Vanilla Lean 4 (v4.29.1 pinned), no imports; expected
  profile per terminal: "does not depend on any axioms".

  THE RATIONAL RECIPROCITY THEOREM's decided instances (the b71 registration, D1):
  for rational x the difference between x and the sum of its p-adic fractional
  parts is an integer — the CRT/Bézout recombination, decided over the FULL residue
  range at the banked denominator families (36 = 4·9, 100 = 4·25, 1296 = 16·81, and
  the triple 900 = 4·9·25), with the Bézout data computed longhand in the
  registration; the general-ℚ statement stays longhand there (vanilla ℚ-arithmetic
  is beyond the kit, stated). THE ORIENTATION DISCRIMINATOR at (2,1): the trace
  pair is (2, 2) — the PLUS orientation — and not its conjugate (the (2,2)
  discriminator is b70's decided orientation break). THE CONJUGATE-COMPLEMENT
  SHAPE: a + (D − a) ≡ 0 mod D over the range — the product-law triviality's
  decidable shadow (the forced-conjugate step's arithmetic core).
  Bank: relay data/b71_coherence.txt.
-/

namespace CoherenceShadow

set_option maxRecDepth 8192 in
/-- THE RECIPROCITY INSTANCES, decided over the full ranges: the CRT recombination
    of the p-adic fractional parts returns x mod 1 exactly at the banked
    denominator families -/
theorem reciprocity_instances :
    ((List.range 36).map (fun a => (9*(a % 4) + 4*((7*a) % 9)) % 36) =
      List.range 36) ∧
    ((List.range 100).map (fun a => (25*(a % 4) + 4*((19*a) % 25)) % 100) =
      List.range 100) ∧
    ((List.range 900).map
        (fun a => (225*(a % 4) + 100*(a % 9) + 36*((16*a) % 25)) % 900) =
      List.range 900) ∧
    ((List.range 1296).map (fun a => (81*(a % 16) + 16*((76*a) % 81)) % 1296) =
      List.range 1296) := by decide

/-- ℤ[i] pairs and the fourth-root table for the (2,1) discriminator -/
def zpow4 (e : Nat) : Int × Int :=
  match e % 4 with
  | 0 => (1, 0) | 1 => (0, 1) | 2 => (-1, 0) | _ => (0, -1)
def padd (u v : Int × Int) : Int × Int := (u.1 + v.1, u.2 + v.2)

/-- THE ORIENTATION DISCRIMINATOR at (2,1), decided: the trace Σζ₄^{m²} is (2, 2)
    — the plus orientation's value q(1 + i) — and not the conjugate (2, −2); the
    (2,2) discriminator is b70's decided orientation break, cited -/
theorem orientation_discriminator_2_1 :
    ((List.range 4).map (fun m => zpow4 ((m*m) % 4))).foldl padd (0, 0) = (2, 2) ∧
    ((2, 2) : Int × Int) ≠ (2, -2) := by decide

/-- THE CONJUGATE-COMPLEMENT SHAPE, decided: a + (D − a) ≡ 0 mod D over the full
    range at D = 36 and 100 — the triviality-on-ℚ product shape's arithmetic core
    (the forced-conjugate step's decidable shadow) -/
theorem conjugate_complement_instances :
    ((List.range 36).map (fun a => (a + (36 - a) % 36) % 36) =
      (List.range 36).map (fun _ => 0)) ∧
    ((List.range 100).map (fun a => (a + (100 - a) % 100) % 100) =
      (List.range 100).map (fun _ => 0)) := by decide

end CoherenceShadow
