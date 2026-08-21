/-
  THE PRODUCT LAW'S CONVERSION · ProductLawShadow.lean
  =====================================================

  Ferry 2026-08-21 (b64, the junction's third visit). Vanilla Lean 4 (v4.29.1
  pinned), no imports; expected profile per terminal: "does not depend on any
  axioms".

  THE THIRD VISIT'S CONVERSION (branch (γ), the b64 registration): the registered
  suspect e^{−iπ/4} holds IFF the cross-parity balance m₁ − m₋₁ = m₋ᵢ − m_i > 0
  holds in the identity limit — the CONJUGATE TWIN of the derived finite place-2
  balance (the whole-chart pair (1, 1): tr S = q(1 + i), rows 35–36). Compiled here,
  the conversion's algebraic core:

  · THE CONJUGATE-BALANCE LEMMA (abstract, named hypotheses): the finite unit
    (1 + i) times any conjugate-balanced pair (a, −a) is real — (1+i)(a − ai) = 2a.
  · THE FINITE PLACE-2 BALANCE INSTANCE (decided): the whole-chart pair (1, 1),
    its conjugate (1, −1), and (1 + i)·(1 − i) = 2 — the law's finite twin exact.

  The identity-limit VALUES stay S1's (the named step); nothing here evaluates
  anything archimedean. Bank: relay data/b62_third_visit.txt (the ferry-named bank).
-/

namespace ProductLawShadow

/-- THE CONJUGATE-BALANCE LEMMA: (1 + i) · (a, −a) = (a + a, 0) over an abstract
    coefficient structure at named hypotheses — the finite unit times any
    conjugate-balanced pair is real; the suspect's law form reduced to the balance -/
theorem conjugate_balance_real {A : Type} (add mul : A → A → A) (neg : A → A)
    (zero one : A)
    (hac : ∀ x y, add x y = add y x)
    (hinv : ∀ x, add x (neg x) = zero)
    (hone : ∀ x, mul one x = x)
    (hnn : ∀ x, neg (neg x) = x)
    (a : A) :
    (add (mul one a) (neg (mul one (neg a))),
     add (mul one (neg a)) (mul one a)) = ((add a a, zero) : A × A) := by
  rw [hone, hone, hnn, hac (neg a) a, hinv]

/-- the concrete pair operations for the decided instance -/
def pmul (u v : Int × Int) : Int × Int :=
  (u.1 * v.1 - u.2 * v.2, u.1 * v.2 + u.2 * v.1)
def pconj (u : Int × Int) : Int × Int := (u.1, -u.2)

/-- THE FINITE PLACE-2 BALANCE, decided: the whole-chart pair is (1, 1) (the chart
    Gauss computation, tr S = q(1+i), rows 35–36 — equality with the PLUS sign);
    its conjugate is (1, −1); (1 + i)(1 − i) = 2 — the product law's finite twin
    exact and real; and the contrast (1 + i)·i = −1 + i, NOT real — a single-class
    unit (the Sonin i) fails the law, as the derivation says it must -/
theorem finite_balance_instance :
    pconj (1, 1) = (1, -1) ∧
    pmul (1, 1) (1, -1) = (2, 0) ∧
    pmul (1, 1) (0, 1) = (-1, 1) := by decide

end ProductLawShadow
