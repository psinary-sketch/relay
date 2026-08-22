/-
  THE ORIENTATION-DEPENDENCE READ'S DECIDED CORE · OrientationShadow.lean
  ========================================================================

  Ferry 2026-08-22 (b104). Vanilla Lean 4 (v4.29.1 pinned), no imports; expected
  profile per terminal: "does not depend on any axioms".

  ℤ[i] is modeled as integer pairs (re, im). Conjugation is F ↦ F³ on the
  instrument's phase, i.e. (a, b) ↦ (a, −b).

  The three decided facts the ledger check needs:

  · `conj_fixes_real_flips_imaginary` — the component law itself, on the
    junction ledger's own summands and total: (1,0) is fixed, (0,−1) ↦ (0,+1),
    and the suspect's value (1,−1) ↦ (1,+1). The REAL part is invariant at 1
    and the imaginary parts exchange — row 57's arithmetic under row 50's map.
  · `twin_conjugate_sum_real` — the conjugate-pair-real-sum mechanism at every
    banked q: q(1+i) + q(1−i) = (2q, 0), imaginary part zero. A conjugate pair
    sums to a real number, and that number is the same from either wing.
  · `real_functionals_agree_on_the_orbit` — the decidable core of the act's
    load-bearing step: the real part and the norm-square, evaluated on a value
    and on its conjugate, AGREE. Any real-valued quantity built equivariantly
    from the ledger data therefore takes the same value on both wings, so an
    identity written in real terms cannot distinguish them. (The general
    statement is the orbit argument in the bank; this is its arithmetic at the
    recorded data.)
  Bank: relay data/b104_orientation_dependence.txt.
-/

set_option maxRecDepth 8192

namespace OrientationShadow

abbrev ZI : Type := Int × Int

def conj (z : ZI) : ZI := (z.1, -z.2)
def add (z w : ZI) : ZI := (z.1 + w.1, z.2 + w.2)
def re (z : ZI) : Int := z.1
def normSq (z : ZI) : Int := z.1 * z.1 + z.2 * z.2

/-- the banked place-2 and odd cell sizes q -/
def qs : List Int := [2, 3, 4, 5, 8, 9, 16, 27]

/-- THE COMPONENT LAW on the junction ledger's own summands and total (row 57):
    the origin's contribution is fixed, the center's exchanges, and the
    suspect's value maps to its conjugate — the real part invariant at 1. -/
theorem conj_fixes_real_flips_imaginary :
    conj (1, 0) = (1, 0) ∧
    conj (0, -1) = (0, 1) ∧
    add (1, 0) (0, -1) = (1, -1) ∧
    conj (add (1, 0) (0, -1)) = (1, 1) ∧
    re (add (1, 0) (0, -1)) = 1 ∧
    re (conj (add (1, 0) (0, -1))) = 1 := by decide

/-- THE CONJUGATE-PAIR REAL SUM at every banked q: q(1+i) + q(1−i) = (2q, 0). -/
theorem twin_conjugate_sum_real :
    qs.all (fun q =>
      decide (add (q, q) (conj (q, q)) = (2 * q, 0))) = true := by decide

/-- REAL FUNCTIONALS AGREE ON THE ORBIT: at the ledger's own values and at
    every banked twin, the real part and the norm-square take the SAME value on
    a point and on its conjugate — so no real-valued equivariant quantity can
    tell the two wings apart. -/
theorem real_functionals_agree_on_the_orbit :
    (re (1, -1) = re (conj (1, -1))) ∧
    (normSq (1, -1) = normSq (conj (1, -1))) ∧
    (normSq (1, -1) = 2) ∧
    qs.all (fun q =>
      decide (re (q, q) = re (conj (q, q)) ∧
              normSq (q, q) = normSq (conj (q, q)))) = true := by decide

end OrientationShadow
