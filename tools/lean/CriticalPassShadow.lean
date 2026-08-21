/-
  THE CRITICAL PASS ACT'S COMPILED CORE · CriticalPassShadow.lean
  ================================================================

  Ferry 2026-08-21 (b72). Vanilla Lean 4 (v4.29.1 pinned), no imports; expected
  profile per terminal: "does not depend on any axioms".

  THE MONOMIAL-TRACE FIXED-PHASE-SUM IDENTITY at FULL GENERALITY (the b72
  registration, D3): for any size, any index map (bijectivity not required), any
  phase assignment into any type with any binary operation and any distinguished
  element, the diagonal sum of the monomial operator equals the fixed-locus phase
  sum. The identity is STRUCTURAL, not algebraic — the proof needs no hypotheses
  on the operation: both sides assemble the same sum in the same order. Row 47's
  decided instances become corollaries: the (2,1) trace re-derived THROUGH the
  lemma in ℤ[i] pairs (the banked discriminator value (2,2)); the (3,1) trace in
  ℤ[ζ₉] six-coordinates (x⁶ = −1 − x³; odd flatness — the origin alone). THE
  GAUGE COVARIANCE at (2,1) (D1's decidable core): conjugation carries the plus
  reading to the minus reading and back, and the breaking holds in BOTH gauges.
  Bank: relay data/b72_critical_pass.txt.
-/

namespace CriticalPassShadow

/-- the diagonal sum over the first n indices -/
def sumR {R : Type} (add : R → R → R) (zero : R) (g : Nat → R) : Nat → R
  | 0 => zero
  | n+1 => add (sumR add zero g n) (g n)

/-- the fixed-locus phase sum over the first n indices -/
def fixSum {R : Type} (add : R → R → R) (zero : R)
    (f : Nat → Nat) (phase : Nat → R) : Nat → R
  | 0 => zero
  | n+1 => add (fixSum add zero f phase n) (if f n = n then phase n else zero)

/-- THE MONOMIAL-TRACE FIXED-PHASE-SUM IDENTITY, general: the monomial operator
    with column j carrying phase j at row f j has diagonal entry
    (if j = f j then phase j else zero); its diagonal sum equals the fixed-locus
    phase sum — any n, any f, any phase, any (R, add, zero), no algebraic
    hypotheses -/
theorem monomial_trace_fixed_phase {R : Type} (add : R → R → R) (zero : R)
    (f : Nat → Nat) (phase : Nat → R) (n : Nat) :
    sumR add zero (fun j => if j = f j then phase j else zero) n
      = fixSum add zero f phase n := by
  induction n with
  | zero => rfl
  | succ n ih =>
    show add (sumR add zero (fun j => if j = f j then phase j else zero) n)
            (if n = f n then phase n else zero)
        = add (fixSum add zero f phase n) (if f n = n then phase n else zero)
    rw [ih]
    cases Nat.decEq (f n) n with
    | isTrue h => rw [if_pos h, if_pos (Eq.symm h)]
    | isFalse h => rw [if_neg h, if_neg (fun hnn => h (Eq.symm hnn))]

/-- ℤ[i] pairs (from the banked pattern) -/
def zpow4 (e : Nat) : Int × Int :=
  match e % 4 with
  | 0 => (1, 0) | 1 => (0, 1) | 2 => (-1, 0) | _ => (0, -1)
def padd (u v : Int × Int) : Int × Int := (u.1 + v.1, u.2 + v.2)
def pscale (s : Int) (u : Int × Int) : Int × Int := (s * u.1, s * u.2)
def pconj (u : Int × Int) : Int × Int := (u.1, -u.2)

/-- the (2,1) quarter-turn σ(a,t) = ((q−t) mod q, a) in flattened coordinates
    j = a·q + t, q = 2 -/
def sigma21 (j : Nat) : Nat := ((2 - j % 2) % 2) * 2 + j / 2
/-- the (2,1) monomial phases q·ζ₄^{a(q−t)} -/
def phase21 (j : Nat) : Int × Int := pscale 2 (zpow4 ((j / 2) * (2 - j % 2)))

/-- ROW 47 AS COROLLARY at (2,1): the chart trace through the general lemma —
    the fixed locus {origin, center} carries phases 2 and 2i, and the trace is
    the banked discriminator value (2, 2) = q(1 + i) -/
theorem row47_corollary_2_1 :
    sumR padd (0, 0) (fun j => if j = sigma21 j then phase21 j else (0, 0)) 4
      = (2, 2) := by
  rw [monomial_trace_fixed_phase padd ((0, 0) : Int × Int) sigma21 phase21 4]
  decide

/-- ℤ[ζ₉] six-coordinates on basis 1, x, …, x⁵ with x⁶ = −1 − x³ -/
abbrev V6 : Type := Int × Int × Int × Int × Int × Int
def v6add (u v : V6) : V6 :=
  (u.1 + v.1, u.2.1 + v.2.1, u.2.2.1 + v.2.2.1,
   u.2.2.2.1 + v.2.2.2.1, u.2.2.2.2.1 + v.2.2.2.2.1, u.2.2.2.2.2 + v.2.2.2.2.2)
def z6 : V6 := (0, 0, 0, 0, 0, 0)
def m9 (e : Nat) : V6 :=
  match e % 9 with
  | 0 => (1, 0, 0, 0, 0, 0) | 1 => (0, 1, 0, 0, 0, 0) | 2 => (0, 0, 1, 0, 0, 0)
  | 3 => (0, 0, 0, 1, 0, 0) | 4 => (0, 0, 0, 0, 1, 0) | 5 => (0, 0, 0, 0, 0, 1)
  | 6 => (-1, 0, 0, -1, 0, 0) | 7 => (0, -1, 0, 0, -1, 0) | _ => (0, 0, -1, 0, 0, -1)
def v6scale3 (u : V6) : V6 :=
  (3 * u.1, 3 * u.2.1, 3 * u.2.2.1, 3 * u.2.2.2.1, 3 * u.2.2.2.2.1, 3 * u.2.2.2.2.2)

/-- the (3,1) quarter-turn in flattened coordinates j = a·q + t, q = 3 -/
def sigma31 (j : Nat) : Nat := ((3 - j % 3) % 3) * 3 + j / 3
/-- the (3,1) monomial phases q·ζ₉^{a(q−t)} -/
def phase31 (j : Nat) : V6 := v6scale3 (m9 ((j / 3) * (3 - j % 3)))

/-- ROW 47 AS COROLLARY at (3,1): the chart trace through the general lemma —
    odd flatness: the fixed locus is the origin alone and the trace is
    3 = (3,0,0,0,0,0) in ℤ[ζ₉] coordinates -/
theorem row47_corollary_3_1 :
    sumR v6add z6 (fun j => if j = sigma31 j then phase31 j else z6) 9
      = ((3, 0, 0, 0, 0, 0) : V6) := by
  rw [monomial_trace_fixed_phase v6add z6 sigma31 phase31 9]
  decide

/-- THE GAUGE COVARIANCE at (2,1), decided: the re-gauge (conjugation — the
    conjugate embedding read of the same symbolic record) carries the plus
    reading (2, 2) to the minus reading (2, −2) and back, and the breaking —
    the two readings' inequality — holds in BOTH gauges: the breaking is
    gauge-invariant, its direction is gauge -/
theorem gauge_covariance_2_1 :
    pconj (2, 2) = ((2, -2) : Int × Int) ∧ ((2, 2) : Int × Int) ≠ (2, -2) ∧
    pconj (2, -2) = ((2, 2) : Int × Int) ∧ ((2, -2) : Int × Int) ≠ (2, 2) := by
  decide

end CriticalPassShadow
