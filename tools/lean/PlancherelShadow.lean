/-
  THE PLANCHEREL-BY-THE-TOWER UNIT · PlancherelShadow.lean
  =========================================================

  Ferry 2026-08-20. Vanilla Lean 4 (v4.29.1 pinned), imports only sibling Core
  modules; expected profile per terminal: "does not depend on any axioms".

  WHAT THIS MODULE COMPILES — the finite-level Plancherel identity's vanilla reach,
  per the registration's declared scope (b50):

  (1) THE DELTA-BASIS PARSEVAL, exact, at the cells N = 4, 9, 16, 25: for all
      a, b < N the pairing of transformed delta functions
          Σ_{m'} conj(ζ^{a·m'})·ζ^{b·m'}  =  N·δ_{a,b}   in ℤ[ζ_N]
      — the orthogonality core, which IS the computational content of Parseval
      (⟨S e_a, S e_b⟩ = N·⟨e_a, e_b⟩ on the delta basis; constant N = q², the P1
      constant). Decided exactly with the E1UnitPurityDraft sparse machinery. The
      N = 64, 81 instances are the SAME law verified exactly at the banked G1 gates
      (b44/b45/b49, re-verified in b50) — cited, not re-decided here (kernel cost),
      declared in the correspondence row.

  (2) THE E₁-SECTOR SPECIALIZATION, GENERAL q, abstract (the KLSilence pattern —
      hypotheses NAMED, none absorbed): if S acts on u and v as multiplication by q
      (the E₁ relation Su = qu), and the pairing is a fold of conj-products with the
      named scale-compatibility hypotheses, then
          pairing (S u) (S v)  =  q²·pairing u v
      — P1's sector specialization: norms scale by q on E₁, the constant q² forced.

  (3) THE P2 EXPONENT-FORCING, GENERAL p, abstract: (i) if every table entry scales
      by p (the b49-measured M1 law), then every KL-discrepancy entry scales by p²
      — the p² is FORCED by the p, not independent; (ii) if a trace map is additive,
      commutes with the scaling, and multiplies embedded elements by p² (the degree
      hypothesis), then traced discrepancies scale by p⁴. The b49 measured exponents
      (p, p², p⁴) are thereby tied by theorem: one exponent forces the others.

  WHAT IT DOES NOT COMPILE, DECLARED: the GENERAL-q full Parseval (the
  bilinear/Fubini extension from the delta basis over the abstract coefficient
  structure) — a NAMED OPEN STATEMENT in the correspondence, never a sorry; nothing
  at complete roster; nothing about the level-limit; h2 untouched.
-/

import E1UnitPurityDraft
import KLSilence

set_option maxRecDepth 8192
set_option maxHeartbeats 4000000

namespace PlancherelShadow

open E1UnitPurityDraft

/-- the delta-basis pairing Σ_{m' < N} conj(ζ^{a m'})·ζ^{b m'} as a sparse element -/
def deltaPairing (N a b : Nat) : Sp :=
  (List.range N).map fun m' => (1, ((N - (a * m') % N) % N) + b * m')

/-- N·δ_{a,b} as a sparse element -/
def enDelta (N a b : Nat) : Sp := if a == b then [(Int.ofNat N, 0)] else []

/-- (1) the delta-basis Parseval at the four decided cells: every pair (a, b),
    exact in ℤ[ζ_N] — the constant is N = q², the P1 constant -/
theorem parseval_delta_2_1 :
    ((List.range 4).all fun a => (List.range 4).all fun b =>
      isZero 2 4 (subSp (deltaPairing 4 a b) (enDelta 4 a b))) = true := by decide

theorem parseval_delta_3_1 :
    ((List.range 9).all fun a => (List.range 9).all fun b =>
      isZero 3 9 (subSp (deltaPairing 9 a b) (enDelta 9 a b))) = true := by decide

theorem parseval_delta_2_2 :
    ((List.range 16).all fun a => (List.range 16).all fun b =>
      isZero 2 16 (subSp (deltaPairing 16 a b) (enDelta 16 a b))) = true := by decide

theorem parseval_delta_5_1 :
    ((List.range 25).all fun a => (List.range 25).all fun b =>
      isZero 5 25 (subSp (deltaPairing 25 a b) (enDelta 25 a b))) = true := by decide

/-- (2) THE E₁-SECTOR SPECIALIZATION, general q: with the pairing a fold of
    conj-products (KLSilence.foldSum) and the named hypotheses — conj commutes with
    the q-scaling, products of q-scaled elements are q²-scaled, and the fold of
    q²-scaled summands is the q²-scaling of the fold — the pairing of S-images of
    E₁ vectors (Su = scale q u pointwise) is q² times the pairing. -/
theorem e1_sector_specialization {R : Type} (zero : R)
    (add mul : R → R → R) (conj : R → R) (scale : Nat → R → R)
    (q M : Nat) (u v Su Sv : Nat → R)
    (hSu : ∀ t, Su t = scale q (u t)) (hSv : ∀ t, Sv t = scale q (v t))
    (hconj : ∀ k x, conj (scale k x) = scale k (conj x))
    (hmul : ∀ k l x y, mul (scale k x) (scale l y) = scale (k * l) (mul x y))
    (hfold : ∀ (k : Nat) (f g : Nat → R), (∀ t, g t = scale k (f t)) →
        KLSilence.foldSum zero add g M
          = scale k (KLSilence.foldSum zero add f M)) :
    KLSilence.foldSum zero add (fun t => mul (conj (Su t)) (Sv t)) M
      = scale (q * q) (KLSilence.foldSum zero add (fun t => mul (conj (u t)) (v t)) M) :=
  hfold (q * q) (fun t => mul (conj (u t)) (v t))
    (fun t => mul (conj (Su t)) (Sv t))
    (fun t => by
      show mul (conj (Su t)) (Sv t) = scale (q * q) (mul (conj (u t)) (v t))
      rw [hSu t, hSv t, hconj, hmul])

/-- (3i) THE DISCREPANCY EXPONENT IS FORCED, general p: if the four table entries
    scale by p, the KL discrepancy X·G₀₀ − G·X₀₀ scales by p² — under the named
    hypotheses (product of p-scaled elements is p²-scaled; sub commutes with the
    scaling). The b49-measured p² is a THEOREM given the measured p. -/
theorem discrepancy_scaling {R : Type}
    (mul sub : R → R → R) (scale : Nat → R → R) (p : Nat)
    (X G X0 G0 X' G' X0' G0' : R)
    (hX : X' = scale p X) (hG : G' = scale p G)
    (hX0 : X0' = scale p X0) (hG0 : G0' = scale p G0)
    (hmul : ∀ k l x y, mul (scale k x) (scale l y) = scale (k * l) (mul x y))
    (hsub : ∀ k x y, sub (scale k x) (scale k y) = scale k (sub x y)) :
    sub (mul X' G0') (mul G' X0') = scale (p * p) (sub (mul X G0) (mul G X0)) := by
  rw [hX, hG, hX0, hG0, hmul, hmul, hsub]

/-- (3ii) THE TRACE EXPONENT IS FORCED, general p: a trace map commuting with the
    scaling and multiplying embedded elements by p² (the degree hypothesis) sends
    p²-scaled embedded discrepancies to p⁴-scaled ones. -/
theorem trace_scaling {R S : Type}
    (scaleR : Nat → R → R) (scaleS : Nat → S → S)
    (tr : R → S) (embD : R) (D : S) (p : Nat)
    (htr_scale : ∀ k x, tr (scaleR k x) = scaleS k (tr x))
    (hdeg : tr embD = scaleS (p * p) D) :
    tr (scaleR (p * p) embD) = scaleS (p * p) (scaleS (p * p) D) := by
  rw [htr_scale, hdeg]

/-- the P1 constant at the decided cells: N = q² (2² = 4, 3² = 9, 4² = 16, 5² = 25) -/
theorem p1_constant_instances :
    (2 * 2 = 4) ∧ (3 * 3 = 9) ∧ (4 * 4 = 16) ∧ (5 * 5 = 25) := by decide

end PlancherelShadow
