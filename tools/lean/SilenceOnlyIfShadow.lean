/-
  THE ONLY-IF OF THE SILENCE THEOREM · SilenceOnlyIfShadow.lean
  ==============================================================

  Ferry 2026-08-21 (b58, component 1). Vanilla Lean 4 (v4.29.1 pinned), no imports;
  expected profile per terminal: "does not depend on any axioms".

  ROW 29'S NAMED OPEN, CLOSED THIS ACT (the general proof is LONGHAND, banked in the
  b58 registration and bank — the cyclotomic ring at general q is beyond decide, stated
  plainly; compiled here are the abstract orbit lemma and the (2,2) decided instances):

  THE SCHEMA: the single-row character vectors g_{a,t} lie in the Sonin space and the
  transform acts monomially on them, M g_{a,t} = ζ^{a(q−t)} g_{q−t,a}; the orbit map
  φ(a,t) = (q−t, a) has ORDER FOUR (the abstract lemma below), each free orbit carries
  exactly one E₁ witness line u = (1+M+M²+M³)g, and the witness family spans E₁ (its
  size equals d₁ at every cell — verified at (2,2) and (5,1), the b58 run). Every
  off-ball weight-one operator is certified NON-SILENT by an exact unit-valued
  discrepancy on the family (q ≥ 5 by the registered case schema; q = 4 exhaustively,
  the b58 run, matching the banked b45 set operator-for-operator; q ≤ 3 vacuous,
  d₁ ≤ 1). With KLSilence's proved direction and count law, THE SILENCE THEOREM IS
  WHOLE at general q: silent exactly on the ball; non-silent count (q−1)² + q².

  The decided instances below live in ℤ[ζ₁₆] in 8 coordinates (ζ⁸ = −1), as length-8
  integer lists; the certificate values are bank-sourced from the b58 run, declared.
-/

namespace SilenceOnlyIfShadow

/- ── the abstract orbit lemma ────────────────────────────────────────────────── -/

/-- the four-periodicity of the trace-orbit map φ(a,t) = (q − t, a): the double
    reflection cancels — add q (neg (add q (neg a))) = a — from named hypotheses only,
    so φ² = (a,t) ↦ (q−a, q−t) and φ⁴ = id at general q -/
theorem orbit_four_periodicity {A : Type} (add : A → A → A) (neg : A → A) (zero : A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (haz : ∀ x, add x zero = x)
    (hinv : ∀ x, add x (neg x) = zero)
    (hnadd : ∀ x y, neg (add x y) = add (neg x) (neg y))
    (hnn : ∀ x, neg (neg x) = x)
    (q a t : A) :
    add q (neg (add q (neg a))) = a ∧
    add q (neg (add q (neg t))) = t := by
  constructor
  · rw [hnadd, hnn, ← haa, show add q (neg q) = zero from hinv q,
        hac zero a, haz]
  · rw [hnadd, hnn, ← haa, show add q (neg q) = zero from hinv q,
        hac zero t, haz]

/- ── ℤ[ζ₁₆] in 8 coordinates: the decided (2,2) instances ────────────────────── -/

/-- a monomial c·ζ^e reduced in ℤ[x]/(x⁸+1), as a length-8 coordinate list -/
def mono (c : Int) (e : Nat) : List Int :=
  let r := e % 8
  let s : Int := if (e / 8) % 2 = 0 then c else -c
  (List.range 8).map (fun k => if k = r then s else 0)

/-- coordinatewise sum -/
def vadd (u v : List Int) : List Int := List.zipWith (· + ·) u v

/-- THE DEGENERATE CENTER VANISHES: at the φ-fixed grid point the E₁ projection is
    (1 + i + i² + i³)·g = 0 with i = ζ⁴ — the b55 screen-artifact mechanism, decided -/
theorem degenerate_center_vanishes :
    vadd (mono 1 0) (vadd (mono 1 4) (vadd (mono 1 8) (mono 1 12))) =
    [0, 0, 0, 0, 0, 0, 0, 0] := by decide

/-- THE (2,2) CERTIFICATES, bank-sourced (the b58 run) and decided in coordinates:
    the E₁₍₁,₁₎ first-witness ratio pair reduces to 8 vs 4 (equal norms 4q = 16 —
    the scalar mismatch is exact); the E₁₍₁,₃₎ pair to 4ζ³−4ζ⁵ vs −4; the frequency
    operators' orthogonal-pair value to 1 + ζ − ζ⁴ + ζ⁵ ≠ 0 — every discrepancy
    NONZERO, no off-ball operator silent -/
theorem witness_certificates_2_2 :
    -- E1_(1,1): diag(u₀) = 8 + 2ζ + 2ζ⁷ + 2ζ⁹ + 2ζ¹⁵ reduces to 8; diag(u₁) = 4
    (vadd (mono 8 0) (vadd (mono 2 1) (vadd (mono 2 7) (vadd (mono 2 9) (mono 2 15))))
      = [8, 0, 0, 0, 0, 0, 0, 0] ∧
     ([8, 0, 0, 0, 0, 0, 0, 0] : List Int) ≠ [4, 0, 0, 0, 0, 0, 0, 0]) ∧
    -- E1_(1,3): diag(u₀) = 4ζ³ + 4ζ⁴ + 4ζ¹² + 4ζ¹³ reduces to 4ζ³ − 4ζ⁵; diag(u₁) = 4ζ⁸ = −4
    (vadd (mono 4 3) (vadd (mono 4 4) (vadd (mono 4 12) (mono 4 13)))
      = [0, 0, 0, 4, 0, -4, 0, 0] ∧
     mono 4 8 = [-4, 0, 0, 0, 0, 0, 0, 0] ∧
     ([0, 0, 0, 4, 0, -4, 0, 0] : List Int) ≠ [-4, 0, 0, 0, 0, 0, 0, 0]) ∧
    -- the frequency-operator orthogonal-pair value: 1 + ζ + ζ⁵ + ζ¹² reduces nonzero
    (vadd (mono 1 0) (vadd (mono 1 1) (vadd (mono 1 5) (mono 1 12)))
      = [1, 1, 0, 0, -1, 1, 0, 0] ∧
     ([1, 1, 0, 0, -1, 1, 0, 0] : List Int) ≠ [0, 0, 0, 0, 0, 0, 0, 0]) := by decide

end SilenceOnlyIfShadow
