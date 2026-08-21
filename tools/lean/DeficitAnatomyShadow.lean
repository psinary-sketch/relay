/-
  THE DEFICIT ANATOMY IDENTITY · DeficitAnatomyShadow.lean
  =========================================================

  Ferry 2026-08-21 (b59, component 2). Vanilla Lean 4 (v4.29.1 pinned), no imports;
  expected profile per terminal: "does not depend on any axioms".

  THE IDENTITY (derived longhand in the b59 registration from rows 35–37 and nothing
  else): with x_v = (q_v − 1)² and c₂(S) the number of place-2 cells,
      4·deficit(S) = ∏_v x_v − Σ_v x_v + c₂(S)
  — since 4·d₁ = x at odd places (row 36's flatness) and 4·d₁ = x − 1 at place-2 cells
  (row 36's unit-trace solve), so 4·Σd₁ = Σx − c₂. Every banked roster has c₂ = 1 and
  two or three cells; the six banked values reproduce exactly (0, 11, 126, 2282,
  12512, 37800 — the registration's longhand targets). Compiled: the six instances
  decided; the bookkeeping shapes at the banked arities proved abstractly at named
  hypotheses (odd-only and one-place-2, two and three places) and the assembled
  neg-form at arity two; ARBITRARY arity stays longhand in the registration (the
  bookkeeping sum), stated plainly.

  THE LOG-SHAPE READING (synthesis grade, carried in the wanted-poster row, not
  here): product-minus-sum is the exponential/logarithm mismatch signature — the
  junction's missing invariant is trace-of-log-shaped.
-/

namespace DeficitAnatomyShadow

/-- the six banked rosters' anatomy instances, decided exactly in the
    subtraction-free form ∏x + c₂ = 4·deficit + Σx (c₂ = 1 at every banked roster):
    R5, R1, R2, R3, R4, EXT -/
theorem banked_instances :
    (1 * 4 + 1 = 4 * 0 + (1 + 4)) ∧
    (1 * 4 * 16 + 1 = 4 * 11 + (1 + 4 + 16)) ∧
    (9 * 64 + 1 = 4 * 126 + (9 + 64)) ∧
    (9 * 64 * 16 + 1 = 4 * 2282 + (9 + 64 + 16)) ∧
    (49 * 64 * 16 + 1 = 4 * 12512 + (49 + 64 + 16)) ∧
    (225 * 676 + 1 = 4 * 37800 + (225 + 676)) := by decide

section Abstract

variable {A : Type}

/-- odd-only, two places: 4(d₁ + d₂) = x₁ + x₂ from the flatness law's shape -/
theorem odd_only_two (add mul : A → A → A) (four : A)
    (hdl : ∀ x y z, mul x (add y z) = add (mul x y) (mul x z))
    (x1 x2 d1 d2 : A)
    (h1 : mul four d1 = x1) (h2 : mul four d2 = x2) :
    mul four (add d1 d2) = add x1 x2 := by
  rw [hdl, h1, h2]

/-- odd-only, three places -/
theorem odd_only_three (add mul : A → A → A) (four : A)
    (hdl : ∀ x y z, mul x (add y z) = add (mul x y) (mul x z))
    (x1 x2 x3 d1 d2 d3 : A)
    (h1 : mul four d1 = x1) (h2 : mul four d2 = x2) (h3 : mul four d3 = x3) :
    mul four (add (add d1 d2) d3) = add (add x1 x2) x3 := by
  rw [hdl, hdl, h1, h2, h3]

/-- one place-2 (head) and one odd place: 4(d₁ + d₂) + 1 = x₁ + x₂ from the
    unit-trace solve's shape (4d₁ + 1 = x₁) -/
theorem place2_two (add mul : A → A → A) (four one : A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (hdl : ∀ x y z, mul x (add y z) = add (mul x y) (mul x z))
    (x1 x2 d1 d2 : A)
    (h1 : add (mul four d1) one = x1) (h2 : mul four d2 = x2) :
    add (mul four (add d1 d2)) one = add x1 x2 := by
  rw [hdl, h2, ← h1, haa, hac x2 one, ← haa]

/-- one place-2 (head) and two odd places -/
theorem place2_three (add mul : A → A → A) (four one : A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (hdl : ∀ x y z, mul x (add y z) = add (mul x y) (mul x z))
    (x1 x2 x3 d1 d2 d3 : A)
    (h1 : add (mul four d1) one = x1) (h2 : mul four d2 = x2)
    (h3 : mul four d3 = x3) :
    add (mul four (add (add d1 d2) d3)) one = add (add x1 x2) x3 := by
  rw [hdl, hdl, h2, h3, ← h1,
      show add (add (add (mul four d1) x2) x3) one
         = add (add (add (mul four d1) one) x2) x3 from by
        rw [haa (add (mul four d1) x2) x3 one, hac x3 one,
            ← haa (add (mul four d1) x2) one x3,
            haa (mul four d1) x2 one, hac x2 one, ← haa (mul four d1) one x2]]

/-- THE ASSEMBLED ANATOMY at arity two: ∏x − Σx + 1 = ∏x − 4Σd — the deficit's
    product-minus-sum form, from the place-2 bookkeeping -/
theorem anatomy_assembled (add mul : A → A → A) (neg : A → A) (zero four one : A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (haz : ∀ x, add x zero = x)
    (hinv : ∀ x, add x (neg x) = zero)
    (hnadd : ∀ x y, neg (add x y) = add (neg x) (neg y))
    (x1 x2 sd : A)
    (hsum : add (mul four sd) one = add x1 x2) :
    add (add (mul x1 x2) (neg (add x1 x2))) one =
    add (mul x1 x2) (neg (mul four sd)) := by
  rw [← hsum, hnadd, ← haa (mul x1 x2) (neg (mul four sd)) (neg one),
      haa (add (mul x1 x2) (neg (mul four sd))) (neg one) one,
      hac (neg one) one, hinv, haz]

end Abstract

end DeficitAnatomyShadow
