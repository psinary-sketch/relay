/-
  THE FOURTH VISIT'S DERIVED SHAPE · FourthVisitShadow.lean
  ==========================================================

  Ferry 2026-08-21 (b69, the junction's fourth visit). Vanilla Lean 4 (v4.29.1
  pinned), no imports; expected profile per terminal: "does not depend on any
  axioms".

  THE DERIVED SHAPE (the b69 registration, step 2 — recorded ground and pure
  algebra only; no classical face used): on any ±i-eigenline of the parity-odd
  class, a square-root scalar has FOURTH POWER −1 (the C₈ class equation), and in
  a structure without zero divisors the square roots of an element form exactly
  the conjugate pair {c, −c} once one root exists (the difference-of-squares
  factorization). THEREFORE the phase family of any archimedean boundary scalar
  is THE EIGHTH-ROOT FAMILY — the registered suspect's family is the only
  possible family; the shape is no longer conjectural. What remains is exactly
  S1's two clauses (the class-and-sign selection; the invariance) — branch (β),
  filed in the bank. Decided below: the family instances in ℤ[ζ₁₆] coordinates
  (the i-side exponents {2, 10}, a sign pair; the −i-side {6, 14}, a sign pair).
  Bank: relay data/b69_fourth_visit.txt.
-/

namespace FourthVisitShadow

/-- THE FOURTH POWER: c² = λ and λ² = −1 give c⁴ = −1 — the C₈ class equation at
    named hypotheses -/
theorem root_fourth_power {A : Type} (mul : A → A → A) (negone : A)
    (c lam : A)
    (hsq : mul c c = lam) (hlam : mul lam lam = negone) :
    mul (mul c c) (mul c c) = negone := by
  rw [hsq, hlam]

/-- THE SQUARE-ROOT FAMILY: without zero divisors, two square roots of the same
    element differ by a sign — y² = x² forces y = x or y = −x (the
    difference-of-squares factorization, at named hypotheses) -/
theorem square_root_family {A : Type} (add mul : A → A → A) (neg : A → A) (zero : A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (haz : ∀ x, add x zero = x)
    (hinv : ∀ x, add x (neg x) = zero)
    (hnn : ∀ x, neg (neg x) = x)
    (hdl : ∀ x y z, mul x (add y z) = add (mul x y) (mul x z))
    (hdr : ∀ x y z, mul (add x y) z = add (mul x z) (mul y z))
    (hmnl : ∀ x y, mul (neg x) y = neg (mul x y))
    (hmc : ∀ x y, mul x y = mul y x)
    (hdom : ∀ a b, mul a b = zero → a = zero ∨ b = zero)
    (hcancel : ∀ a b, add a (neg b) = zero → a = b)
    (x y : A)
    (hxy : mul x x = mul y y) :
    y = x ∨ y = neg x := by
  have hfactor : mul (add y (neg x)) (add y x) = zero := by
    rw [hdr, hdl, hdl, hmnl, hmnl, hmc x y,
        haa (mul y y) (mul y x) (add (neg (mul y x)) (neg (mul x x))),
        ← haa (mul y x) (neg (mul y x)) (neg (mul x x)), hinv,
        hac zero (neg (mul x x)), haz, ← hxy, hinv]
  cases hdom _ _ hfactor with
  | inl h => exact Or.inl (hcancel y x h)
  | inr h =>
      refine Or.inr (hcancel y (neg x) ?_)
      rw [hnn]
      exact h

/-- a monomial c·ζ₁₆^e reduced in ℤ[x]/(x⁸+1) -/
def mono (c : Int) (e : Nat) : List Int :=
  let r := e % 8
  let s : Int := if (e / 8) % 2 = 0 then c else -c
  (List.range 8).map (fun k => if k = r then s else 0)

/-- THE FAMILY INSTANCES, decided in ℤ[ζ₁₆] coordinates: the i-side roots are the
    sign pair at exponents {2, 10} (both square to i; ζ₈⁵ = −ζ₈), the −i-side the
    sign pair at {6, 14} (both square to −i; ζ₁₆¹⁴ = −ζ₁₆⁶) — the eighth-root
    family exactly as the abstract lemmas force it -/
theorem family_instances :
    (mono 1 (2 + 2) = [0,0,0,0,1,0,0,0] ∧ mono 1 (10 + 10) = [0,0,0,0,1,0,0,0]) ∧
    (mono 1 (6 + 6) = [0,0,0,0,-1,0,0,0] ∧ mono 1 (14 + 14) = [0,0,0,0,-1,0,0,0]) ∧
    (mono 1 10 = (mono 1 2).map (fun c => -c) ∧
     mono 1 14 = (mono 1 6).map (fun c => -c)) := by decide

end FourthVisitShadow
