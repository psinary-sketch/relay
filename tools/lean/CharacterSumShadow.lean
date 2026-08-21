/-
  THE GENERAL CHARACTER-SUM THEOREM · CharacterSumShadow.lean
  ============================================================

  Ferry 2026-08-21 (b57, components 1–2). Vanilla Lean 4 (v4.29.1 pinned), no imports;
  expected profile per terminal: "does not depend on any axioms".

  THE THEOREM (the identity-operator instance of PairingShadow.form_level_lift — row 31's
  named open statement): for commuting order-four local transforms on a tensor product
  over a GENERAL roster (any length) with GENERAL sector dimensions, four times the
  principal-sector dimension equals the sum over the four powers of the products of the
  local traces — values in Gaussian-integer pairs over an abstract coefficient structure
  whose ring laws are NAMED HYPOTHESES (hac/haa/haz/hinv: the additive commutative-group
  laws; hdl/hdr: distributivity; hmnr/hmnl/hnadd/hnn: the negation laws; hmzr/hmzl: zero
  annihilation). No Mathlib; no core Int algebra lemmas (Int.add_comm etc. carry propext
  at this pin — print-checked and routed around); no simp and no ac_rfl (both print
  tainted at this pin — proof by explicit rewrite chains only).

  THE CONJUGATE-PAIR MECHANIZATION (the registered smarter route, the b57 registration):
  reality is NOT proved by expansion — the third-power product is proved to be the
  CONJUGATE of the first-power product (`prod3_eq_conj_prod1`, from conjugation
  multiplicative over pair products), the even powers are real by form, and the
  imaginary parts cancel as I + (−I) in the final assembly. The forty-monomial brute
  expansion never occurs; the step identities reduce to a small reusable rewrite kit
  (dp: difference product; sp: sum product; sh: shuffle; ich/ich': interchanges).

  Quadruple order = THE BANK ORDER (d₁, d₋₁, d_i, d₋ᵢ); rosters are nonempty (a head
  cell plus a list), matching every banked roster.
-/

namespace CharacterSumShadow

variable {A : Type}

/-- Gaussian pair addition over the abstract coefficients -/
def padd (add : A → A → A) (u v : A × A) : A × A :=
  (add u.1 v.1, add u.2 v.2)

/-- Gaussian pair multiplication -/
def pmul (add mul : A → A → A) (neg : A → A) (u v : A × A) : A × A :=
  (add (mul u.1 v.1) (neg (mul u.2 v.2)), add (mul u.1 v.2) (mul u.2 v.1))

/-- Gaussian conjugation -/
def pconj (neg : A → A) (u : A × A) : A × A := (u.1, neg u.2)

/-- t₀ = (d₁ + d₋₁) + (d_i + d₋ᵢ) -/
def sum4 (add : A → A → A) (d : A × A × A × A) : A :=
  add (add d.1 d.2.1) (add d.2.2.1 d.2.2.2)

/-- t₂ = (d₁ + d₋₁) − (d_i + d₋ᵢ) -/
def alt4 (add : A → A → A) (neg : A → A) (d : A × A × A × A) : A :=
  add (add d.1 d.2.1) (neg (add d.2.2.1 d.2.2.2))

/-- Re t₁ = d₁ − d₋₁ -/
def tR (add : A → A → A) (neg : A → A) (d : A × A × A × A) : A :=
  add d.1 (neg d.2.1)

/-- Im t₁ = d_i − d₋ᵢ -/
def tI (add : A → A → A) (neg : A → A) (d : A × A × A × A) : A :=
  add d.2.2.1 (neg d.2.2.2)

/-- the μ₄ pattern-count convolution N′_μ = Σ_k d_{i^k}·N_{i^{−k}μ}, quadruple order
    (N₁, N₋₁, N_i, N₋ᵢ) -/
def conv (add mul : A → A → A) (d m : A × A × A × A) : A × A × A × A :=
  (add (add (mul d.1 m.1) (mul d.2.1 m.2.1)) (add (mul d.2.2.1 m.2.2.2) (mul d.2.2.2 m.2.2.1)),
   add (add (mul d.1 m.2.1) (mul d.2.1 m.1)) (add (mul d.2.2.1 m.2.2.1) (mul d.2.2.2 m.2.2.2)),
   add (add (mul d.1 m.2.2.1) (mul d.2.1 m.2.2.2)) (add (mul d.2.2.1 m.1) (mul d.2.2.2 m.2.1)),
   add (add (mul d.1 m.2.2.2) (mul d.2.1 m.2.2.1)) (add (mul d.2.2.1 m.2.1) (mul d.2.2.2 m.1)))

/-- the pattern-count quadruple over a nonempty roster (head d, tail L) -/
def Nq (add mul : A → A → A) (d : A × A × A × A) : List (A × A × A × A) → A × A × A × A
  | [] => d
  | e :: L => conv add mul d (Nq add mul e L)

/-- the product of the t₀ traces (Gaussian pairs, zero imaginary part) -/
def prod0 (add mul : A → A → A) (neg : A → A) (zero : A)
    (d : A × A × A × A) : List (A × A × A × A) → A × A
  | [] => (sum4 add d, zero)
  | e :: L => pmul add mul neg (sum4 add d, zero) (prod0 add mul neg zero e L)

/-- the product of the t₁ traces -/
def prod1 (add mul : A → A → A) (neg : A → A)
    (d : A × A × A × A) : List (A × A × A × A) → A × A
  | [] => (tR add neg d, tI add neg d)
  | e :: L => pmul add mul neg (tR add neg d, tI add neg d) (prod1 add mul neg e L)

/-- the product of the t₂ traces -/
def prod2 (add mul : A → A → A) (neg : A → A) (zero : A)
    (d : A × A × A × A) : List (A × A × A × A) → A × A
  | [] => (alt4 add neg d, zero)
  | e :: L => pmul add mul neg (alt4 add neg d, zero) (prod2 add mul neg zero e L)

/-- the product of the t₃ traces (t₃ = conj t₁ place-wise) -/
def prod3 (add mul : A → A → A) (neg : A → A)
    (d : A × A × A × A) : List (A × A × A × A) → A × A
  | [] => (tR add neg d, neg (tI add neg d))
  | e :: L => pmul add mul neg (tR add neg d, neg (tI add neg d)) (prod3 add mul neg e L)

/- ── the rewrite kit ──────────────────────────────────────────────────────────── -/

/-- derived: left commutation -/
theorem halc (add : A → A → A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (x y z : A) : add x (add y z) = add y (add x z) := by
  rw [← haa, hac x y, haa]

/-- derived: zero on the left -/
theorem hza (add : A → A → A) (zero : A)
    (hac : ∀ x y, add x y = add y x)
    (haz : ∀ x, add x zero = x)
    (x : A) : add zero x = x := by rw [hac, haz]

/-- derived: neg zero = zero -/
theorem hnzero (add : A → A → A) (neg : A → A) (zero : A)
    (hac : ∀ x y, add x y = add y x)
    (haz : ∀ x, add x zero = x)
    (hinv : ∀ x, add x (neg x) = zero) : neg zero = zero := by
  rw [← hza add zero hac haz (neg zero), hinv]

/-- the shuffle: (w − x) + (y − z) = (w + y) − (x + z) -/
theorem sh (add : A → A → A) (neg : A → A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (hnadd : ∀ x y, neg (add x y) = add (neg x) (neg y))
    (w x y z : A) :
    add (add w (neg x)) (add y (neg z)) = add (add w y) (neg (add x z)) := by
  rw [haa, halc add hac haa (neg x) y (neg z), hnadd, ← haa]

/-- the interchange: (a + b) + (c + d) = (a + c) + (b + d) -/
theorem ich (add : A → A → A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (a b c d : A) :
    add (add a b) (add c d) = add (add a c) (add b d) := by
  rw [haa, halc add hac haa b c d, ← haa]

/-- the cross interchange: (a + b) + (c + d) = (a + d) + (b + c) -/
theorem ich' (add : A → A → A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (a b c d : A) :
    add (add a b) (add c d) = add (add a d) (add b c) := by
  rw [hac c d, ich add hac haa a b d c]

/-- the cancellation: (x + u) + (y − u) = x + y -/
theorem cancel2 (add : A → A → A) (neg : A → A) (zero : A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (haz : ∀ x, add x zero = x)
    (hinv : ∀ x, add x (neg x) = zero)
    (x y u : A) :
    add (add x u) (add y (neg u)) = add x y := by
  rw [haa, halc add hac haa u y (neg u), hinv, haz]

/-- the difference product: (a − b)(p − q) = (ap + bq) − (aq + bp) -/
theorem dp (add mul : A → A → A) (neg : A → A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (hdl : ∀ x y z, mul x (add y z) = add (mul x y) (mul x z))
    (hdr : ∀ x y z, mul (add x y) z = add (mul x z) (mul y z))
    (hmnr : ∀ x y, mul x (neg y) = neg (mul x y))
    (hmnl : ∀ x y, mul (neg x) y = neg (mul x y))
    (hnadd : ∀ x y, neg (add x y) = add (neg x) (neg y))
    (hnn : ∀ x, neg (neg x) = x)
    (a b p q : A) :
    mul (add a (neg b)) (add p (neg q)) =
    add (add (mul a p) (mul b q)) (neg (add (mul a q) (mul b p))) := by
  rw [hdr, hdl, hdl, hmnl, hmnl, hmnr, hmnr, hnn,
      hac (neg (mul b p)) (mul b q),
      sh add neg hac haa hnadd (mul a p) (mul a q) (mul b q) (mul b p)]

/-- the sum product: (a + b)(p + q) = (ap + aq) + (bp + bq) -/
theorem sp (add mul : A → A → A)
    (hdl : ∀ x y z, mul x (add y z) = add (mul x y) (mul x z))
    (hdr : ∀ x y z, mul (add x y) z = add (mul x z) (mul y z))
    (a b p q : A) :
    mul (add a b) (add p q) =
    add (add (mul a p) (mul a q)) (add (mul b p) (mul b q)) := by
  rw [hdr, hdl, hdl]

/-- the subtraction combination: (u − v) − (w − z) = (u + z) − (v + w) -/
theorem subsub (add : A → A → A) (neg : A → A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (hnadd : ∀ x y, neg (add x y) = add (neg x) (neg y))
    (hnn : ∀ x, neg (neg x) = x)
    (u v w z : A) :
    add (add u (neg v)) (neg (add w (neg z))) =
    add (add u z) (neg (add v w)) := by
  rw [hnadd, hnn, hac (neg w) z, sh add neg hac haa hnadd u v z w]

/-- the four-fold collapse: (P+u+R) + (P−u+R) = (P+R) + (P+R) -/
theorem final4 (add : A → A → A) (neg : A → A) (zero : A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (haz : ∀ x, add x zero = x)
    (hinv : ∀ x, add x (neg x) = zero)
    (P u R : A) :
    add (add (add P u) R) (add (add P (neg u)) R) = add (add P R) (add P R) := by
  rw [show add (add P u) R = add (add P R) u by rw [haa, hac u R, ← haa],
      show add (add P (neg u)) R = add (add P R) (neg u) by rw [haa, hac (neg u) R, ← haa],
      cancel2 add neg zero hac haa haz hinv (add P R) (add P R) u]

/- ── the step identities ─────────────────────────────────────────────────────── -/

/-- t₀ step: sum4 is multiplicative through the convolution -/
theorem lemA (add mul : A → A → A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (hdl : ∀ x y z, mul x (add y z) = add (mul x y) (mul x z))
    (hdr : ∀ x y z, mul (add x y) z = add (mul x z) (mul y z))
    (x1 x2 x3 x4 p1 p2 p3 p4 : A) :
    mul (add (add x1 x2) (add x3 x4)) (add (add p1 p2) (add p3 p4)) =
    add (add (add (add (mul x1 p1) (mul x2 p2)) (add (mul x3 p4) (mul x4 p3)))
             (add (add (mul x1 p2) (mul x2 p1)) (add (mul x3 p3) (mul x4 p4))))
        (add (add (add (mul x1 p3) (mul x2 p4)) (add (mul x3 p1) (mul x4 p2)))
             (add (add (mul x1 p4) (mul x2 p3)) (add (mul x3 p2) (mul x4 p1)))) := by
  rw [sp add mul hdl hdr (add x1 x2) (add x3 x4) (add p1 p2) (add p3 p4),
      sp add mul hdl hdr x1 x2 p1 p2, sp add mul hdl hdr x1 x2 p3 p4,
      sp add mul hdl hdr x3 x4 p1 p2, sp add mul hdl hdr x3 x4 p3 p4,
      ich' add hac haa
        (add (add (mul x1 p1) (mul x1 p2)) (add (mul x2 p1) (mul x2 p2)))
        (add (add (mul x1 p3) (mul x1 p4)) (add (mul x2 p3) (mul x2 p4)))
        (add (add (mul x3 p1) (mul x3 p2)) (add (mul x4 p1) (mul x4 p2)))
        (add (add (mul x3 p3) (mul x3 p4)) (add (mul x4 p3) (mul x4 p4))),
      ich' add hac haa (mul x1 p1) (mul x1 p2) (mul x2 p1) (mul x2 p2),
      ich' add hac haa (mul x3 p3) (mul x3 p4) (mul x4 p3) (mul x4 p4),
      ich' add hac haa (add (mul x1 p1) (mul x2 p2)) (add (mul x1 p2) (mul x2 p1))
        (add (mul x3 p3) (mul x4 p4)) (add (mul x3 p4) (mul x4 p3)),
      ich' add hac haa (mul x1 p3) (mul x1 p4) (mul x2 p3) (mul x2 p4),
      ich' add hac haa (mul x3 p1) (mul x3 p2) (mul x4 p1) (mul x4 p2),
      ich add hac haa (add (mul x1 p3) (mul x2 p4)) (add (mul x1 p4) (mul x2 p3))
        (add (mul x3 p1) (mul x4 p2)) (add (mul x3 p2) (mul x4 p1))]

/-- t₂ step: alt4 is multiplicative through the convolution -/
theorem lemD (add mul : A → A → A) (neg : A → A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (hdl : ∀ x y z, mul x (add y z) = add (mul x y) (mul x z))
    (hdr : ∀ x y z, mul (add x y) z = add (mul x z) (mul y z))
    (hmnr : ∀ x y, mul x (neg y) = neg (mul x y))
    (hmnl : ∀ x y, mul (neg x) y = neg (mul x y))
    (hnadd : ∀ x y, neg (add x y) = add (neg x) (neg y))
    (hnn : ∀ x, neg (neg x) = x)
    (x1 x2 x3 x4 p1 p2 p3 p4 : A) :
    mul (add (add x1 x2) (neg (add x3 x4))) (add (add p1 p2) (neg (add p3 p4))) =
    add (add (add (add (mul x1 p1) (mul x2 p2)) (add (mul x3 p4) (mul x4 p3)))
             (add (add (mul x1 p2) (mul x2 p1)) (add (mul x3 p3) (mul x4 p4))))
        (neg (add (add (add (mul x1 p3) (mul x2 p4)) (add (mul x3 p1) (mul x4 p2)))
                  (add (add (mul x1 p4) (mul x2 p3)) (add (mul x3 p2) (mul x4 p1))))) := by
  rw [dp add mul neg hac haa hdl hdr hmnr hmnl hnadd hnn
        (add x1 x2) (add x3 x4) (add p1 p2) (add p3 p4),
      sp add mul hdl hdr x1 x2 p1 p2, sp add mul hdl hdr x3 x4 p3 p4,
      sp add mul hdl hdr x1 x2 p3 p4, sp add mul hdl hdr x3 x4 p1 p2,
      ich' add hac haa (mul x1 p1) (mul x1 p2) (mul x2 p1) (mul x2 p2),
      ich' add hac haa (mul x3 p3) (mul x3 p4) (mul x4 p3) (mul x4 p4),
      ich' add hac haa (add (mul x1 p1) (mul x2 p2)) (add (mul x1 p2) (mul x2 p1))
        (add (mul x3 p3) (mul x4 p4)) (add (mul x3 p4) (mul x4 p3)),
      ich' add hac haa (mul x1 p3) (mul x1 p4) (mul x2 p3) (mul x2 p4),
      ich' add hac haa (mul x3 p1) (mul x3 p2) (mul x4 p1) (mul x4 p2),
      ich add hac haa (add (mul x1 p3) (mul x2 p4)) (add (mul x1 p4) (mul x2 p3))
        (add (mul x3 p1) (mul x4 p2)) (add (mul x3 p2) (mul x4 p1))]

/-- t₁ real step -/
theorem lemB (add mul : A → A → A) (neg : A → A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (hdl : ∀ x y z, mul x (add y z) = add (mul x y) (mul x z))
    (hdr : ∀ x y z, mul (add x y) z = add (mul x z) (mul y z))
    (hmnr : ∀ x y, mul x (neg y) = neg (mul x y))
    (hmnl : ∀ x y, mul (neg x) y = neg (mul x y))
    (hnadd : ∀ x y, neg (add x y) = add (neg x) (neg y))
    (hnn : ∀ x, neg (neg x) = x)
    (x1 x2 x3 x4 p1 p2 p3 p4 : A) :
    add (mul (add x1 (neg x2)) (add p1 (neg p2)))
        (neg (mul (add x3 (neg x4)) (add p3 (neg p4)))) =
    add (add (add (mul x1 p1) (mul x2 p2)) (add (mul x3 p4) (mul x4 p3)))
        (neg (add (add (mul x1 p2) (mul x2 p1)) (add (mul x3 p3) (mul x4 p4)))) := by
  rw [dp add mul neg hac haa hdl hdr hmnr hmnl hnadd hnn x1 x2 p1 p2,
      dp add mul neg hac haa hdl hdr hmnr hmnl hnadd hnn x3 x4 p3 p4,
      subsub add neg hac haa hnadd hnn
        (add (mul x1 p1) (mul x2 p2)) (add (mul x1 p2) (mul x2 p1))
        (add (mul x3 p3) (mul x4 p4)) (add (mul x3 p4) (mul x4 p3))]

/-- t₁ imaginary step -/
theorem lemC (add mul : A → A → A) (neg : A → A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (hdl : ∀ x y z, mul x (add y z) = add (mul x y) (mul x z))
    (hdr : ∀ x y z, mul (add x y) z = add (mul x z) (mul y z))
    (hmnr : ∀ x y, mul x (neg y) = neg (mul x y))
    (hmnl : ∀ x y, mul (neg x) y = neg (mul x y))
    (hnadd : ∀ x y, neg (add x y) = add (neg x) (neg y))
    (hnn : ∀ x, neg (neg x) = x)
    (x1 x2 x3 x4 p1 p2 p3 p4 : A) :
    add (mul (add x1 (neg x2)) (add p3 (neg p4)))
        (mul (add x3 (neg x4)) (add p1 (neg p2))) =
    add (add (add (mul x1 p3) (mul x2 p4)) (add (mul x3 p1) (mul x4 p2)))
        (neg (add (add (mul x1 p4) (mul x2 p3)) (add (mul x3 p2) (mul x4 p1)))) := by
  rw [dp add mul neg hac haa hdl hdr hmnr hmnl hnadd hnn x1 x2 p3 p4,
      dp add mul neg hac haa hdl hdr hmnr hmnl hnadd hnn x3 x4 p1 p2,
      sh add neg hac haa hnadd
        (add (mul x1 p3) (mul x2 p4)) (add (mul x1 p4) (mul x2 p3))
        (add (mul x3 p1) (mul x4 p2)) (add (mul x3 p2) (mul x4 p1))]

/- ── the invariants and the theorem ──────────────────────────────────────────── -/

/-- conjugation is multiplicative over pair products -/
theorem pconj_mul (add mul : A → A → A) (neg : A → A)
    (hmnr : ∀ x y, mul x (neg y) = neg (mul x y))
    (hmnl : ∀ x y, mul (neg x) y = neg (mul x y))
    (hnadd : ∀ x y, neg (add x y) = add (neg x) (neg y))
    (hnn : ∀ x, neg (neg x) = x)
    (u v : A × A) :
    pmul add mul neg (pconj neg u) (pconj neg v) = pconj neg (pmul add mul neg u v) := by
  show (add (mul u.1 v.1) (neg (mul (neg u.2) (neg v.2))),
        add (mul u.1 (neg v.2)) (mul (neg u.2) v.1)) =
       (add (mul u.1 v.1) (neg (mul u.2 v.2)),
        neg (add (mul u.1 v.2) (mul u.2 v.1)))
  rw [hmnl, hmnr, hnn, hmnr, hmnl, ← hnadd]

/-- INVARIANT 0: the t₀ product is (sum4 of the pattern quadruple, 0) -/
theorem inv0 (add mul : A → A → A) (neg : A → A) (zero : A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (haz : ∀ x, add x zero = x)
    (hinv : ∀ x, add x (neg x) = zero)
    (hdl : ∀ x y z, mul x (add y z) = add (mul x y) (mul x z))
    (hdr : ∀ x y z, mul (add x y) z = add (mul x z) (mul y z))
    (hmzr : ∀ x, mul x zero = zero)
    (hmzl : ∀ x, mul zero x = zero)
    (L : List (A × A × A × A)) : ∀ d,
    prod0 add mul neg zero d L = (sum4 add (Nq add mul d L), zero) := by
  induction L with
  | nil => intro d; rfl
  | cons e L ih =>
      intro d
      show pmul add mul neg (sum4 add d, zero) (prod0 add mul neg zero e L) =
           (sum4 add (conv add mul d (Nq add mul e L)), zero)
      rw [ih e]
      show (add (mul (sum4 add d) (sum4 add (Nq add mul e L))) (neg (mul zero zero)),
            add (mul (sum4 add d) zero) (mul zero (sum4 add (Nq add mul e L)))) =
           (sum4 add (conv add mul d (Nq add mul e L)), zero)
      rw [hmzr, hnzero add neg zero hac haz hinv, haz, hmzr, hmzl, haz,
          show sum4 add d = add (add d.1 d.2.1) (add d.2.2.1 d.2.2.2) from rfl,
          show sum4 add (Nq add mul e L) =
            add (add (Nq add mul e L).1 (Nq add mul e L).2.1)
                (add (Nq add mul e L).2.2.1 (Nq add mul e L).2.2.2) from rfl,
          lemA add mul hac haa hdl hdr]
      rfl

/-- INVARIANT 2: the t₂ product is (alt4 of the pattern quadruple, 0) -/
theorem inv2 (add mul : A → A → A) (neg : A → A) (zero : A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (haz : ∀ x, add x zero = x)
    (hinv : ∀ x, add x (neg x) = zero)
    (hdl : ∀ x y z, mul x (add y z) = add (mul x y) (mul x z))
    (hdr : ∀ x y z, mul (add x y) z = add (mul x z) (mul y z))
    (hmnr : ∀ x y, mul x (neg y) = neg (mul x y))
    (hmnl : ∀ x y, mul (neg x) y = neg (mul x y))
    (hnadd : ∀ x y, neg (add x y) = add (neg x) (neg y))
    (hnn : ∀ x, neg (neg x) = x)
    (hmzr : ∀ x, mul x zero = zero)
    (hmzl : ∀ x, mul zero x = zero)
    (L : List (A × A × A × A)) : ∀ d,
    prod2 add mul neg zero d L = (alt4 add neg (Nq add mul d L), zero) := by
  induction L with
  | nil => intro d; rfl
  | cons e L ih =>
      intro d
      show pmul add mul neg (alt4 add neg d, zero) (prod2 add mul neg zero e L) =
           (alt4 add neg (conv add mul d (Nq add mul e L)), zero)
      rw [ih e]
      show (add (mul (alt4 add neg d) (alt4 add neg (Nq add mul e L))) (neg (mul zero zero)),
            add (mul (alt4 add neg d) zero) (mul zero (alt4 add neg (Nq add mul e L)))) =
           (alt4 add neg (conv add mul d (Nq add mul e L)), zero)
      rw [hmzr, hnzero add neg zero hac haz hinv, haz, hmzr, hmzl, haz,
          show alt4 add neg d = add (add d.1 d.2.1) (neg (add d.2.2.1 d.2.2.2)) from rfl,
          show alt4 add neg (Nq add mul e L) =
            add (add (Nq add mul e L).1 (Nq add mul e L).2.1)
                (neg (add (Nq add mul e L).2.2.1 (Nq add mul e L).2.2.2)) from rfl,
          lemD add mul neg hac haa hdl hdr hmnr hmnl hnadd hnn]
      rfl

/-- INVARIANT 1: the t₁ product is (N₁ − N₋₁, N_i − N₋ᵢ) -/
theorem inv1 (add mul : A → A → A) (neg : A → A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (hdl : ∀ x y z, mul x (add y z) = add (mul x y) (mul x z))
    (hdr : ∀ x y z, mul (add x y) z = add (mul x z) (mul y z))
    (hmnr : ∀ x y, mul x (neg y) = neg (mul x y))
    (hmnl : ∀ x y, mul (neg x) y = neg (mul x y))
    (hnadd : ∀ x y, neg (add x y) = add (neg x) (neg y))
    (hnn : ∀ x, neg (neg x) = x)
    (L : List (A × A × A × A)) : ∀ d,
    prod1 add mul neg d L =
      (add (Nq add mul d L).1 (neg (Nq add mul d L).2.1),
       add (Nq add mul d L).2.2.1 (neg (Nq add mul d L).2.2.2)) := by
  induction L with
  | nil => intro d; rfl
  | cons e L ih =>
      intro d
      show pmul add mul neg (tR add neg d, tI add neg d) (prod1 add mul neg e L) =
           (add (conv add mul d (Nq add mul e L)).1
                (neg (conv add mul d (Nq add mul e L)).2.1),
            add (conv add mul d (Nq add mul e L)).2.2.1
                (neg (conv add mul d (Nq add mul e L)).2.2.2))
      rw [ih e]
      show (add (mul (tR add neg d)
                     (add (Nq add mul e L).1 (neg (Nq add mul e L).2.1)))
                (neg (mul (tI add neg d)
                     (add (Nq add mul e L).2.2.1 (neg (Nq add mul e L).2.2.2)))),
            add (mul (tR add neg d)
                     (add (Nq add mul e L).2.2.1 (neg (Nq add mul e L).2.2.2)))
                (mul (tI add neg d)
                     (add (Nq add mul e L).1 (neg (Nq add mul e L).2.1)))) = _
      rw [show tR add neg d = add d.1 (neg d.2.1) from rfl,
          show tI add neg d = add d.2.2.1 (neg d.2.2.2) from rfl,
          lemB add mul neg hac haa hdl hdr hmnr hmnl hnadd hnn,
          lemC add mul neg hac haa hdl hdr hmnr hmnl hnadd hnn]
      rfl

/-- THE CONJUGATE-PAIR THEOREM: the third-power product is the conjugate of the
    first-power product — reality without expansion -/
theorem prod3_eq_conj_prod1 (add mul : A → A → A) (neg : A → A)
    (hmnr : ∀ x y, mul x (neg y) = neg (mul x y))
    (hmnl : ∀ x y, mul (neg x) y = neg (mul x y))
    (hnadd : ∀ x y, neg (add x y) = add (neg x) (neg y))
    (hnn : ∀ x, neg (neg x) = x)
    (L : List (A × A × A × A)) : ∀ d,
    prod3 add mul neg d L = pconj neg (prod1 add mul neg d L) := by
  induction L with
  | nil => intro d; rfl
  | cons e L ih =>
      intro d
      show pmul add mul neg (tR add neg d, neg (tI add neg d)) (prod3 add mul neg e L) =
           pconj neg (pmul add mul neg (tR add neg d, tI add neg d) (prod1 add mul neg e L))
      rw [ih e,
          show ((tR add neg d, neg (tI add neg d)) : A × A) =
            pconj neg (tR add neg d, tI add neg d) from rfl,
          pconj_mul add mul neg hmnr hmnl hnadd hnn]

/-- THE GENERAL CHARACTER-SUM THEOREM (row 31's named open, closed at the abstract
    level): over any nonempty roster with general sector data, the μ₄ character sum of
    the four trace products equals (4·N₁, 0) — four times the principal-sector pattern
    count, real on the face -/
theorem character_sum_general (add mul : A → A → A) (neg : A → A) (zero : A)
    (hac : ∀ x y, add x y = add y x)
    (haa : ∀ x y z, add (add x y) z = add x (add y z))
    (haz : ∀ x, add x zero = x)
    (hinv : ∀ x, add x (neg x) = zero)
    (hdl : ∀ x y z, mul x (add y z) = add (mul x y) (mul x z))
    (hdr : ∀ x y z, mul (add x y) z = add (mul x z) (mul y z))
    (hmnr : ∀ x y, mul x (neg y) = neg (mul x y))
    (hmnl : ∀ x y, mul (neg x) y = neg (mul x y))
    (hnadd : ∀ x y, neg (add x y) = add (neg x) (neg y))
    (hnn : ∀ x, neg (neg x) = x)
    (hmzr : ∀ x, mul x zero = zero)
    (hmzl : ∀ x, mul zero x = zero)
    (d : A × A × A × A) (L : List (A × A × A × A)) :
    padd add (padd add (prod0 add mul neg zero d L) (prod1 add mul neg d L))
             (padd add (prod2 add mul neg zero d L) (prod3 add mul neg d L)) =
    (add (add (Nq add mul d L).1 (Nq add mul d L).1)
         (add (Nq add mul d L).1 (Nq add mul d L).1), zero) := by
  rw [inv0 add mul neg zero hac haa haz hinv hdl hdr hmzr hmzl L d,
      prod3_eq_conj_prod1 add mul neg hmnr hmnl hnadd hnn L d,
      inv2 add mul neg zero hac haa haz hinv hdl hdr hmnr hmnl hnadd hnn hmzr hmzl L d,
      inv1 add mul neg hac haa hdl hdr hmnr hmnl hnadd hnn L d]
  show (add (add (sum4 add (Nq add mul d L))
                 (add (Nq add mul d L).1 (neg (Nq add mul d L).2.1)))
            (add (alt4 add neg (Nq add mul d L))
                 (add (Nq add mul d L).1 (neg (Nq add mul d L).2.1))),
        add (add zero (add (Nq add mul d L).2.2.1 (neg (Nq add mul d L).2.2.2)))
            (add zero (neg (add (Nq add mul d L).2.2.1 (neg (Nq add mul d L).2.2.2))))) = _
  rw [hza add zero hac haz, hza add zero hac haz, hinv,
      show sum4 add (Nq add mul d L) =
        add (add (Nq add mul d L).1 (Nq add mul d L).2.1)
            (add (Nq add mul d L).2.2.1 (Nq add mul d L).2.2.2) from rfl,
      show alt4 add neg (Nq add mul d L) =
        add (add (Nq add mul d L).1 (Nq add mul d L).2.1)
            (neg (add (Nq add mul d L).2.2.1 (Nq add mul d L).2.2.2)) from rfl,
      final4 add neg zero hac haa haz hinv
        (add (Nq add mul d L).1 (Nq add mul d L).2.1)
        (add (Nq add mul d L).2.2.1 (Nq add mul d L).2.2.2)
        (add (Nq add mul d L).1 (neg (Nq add mul d L).2.1)),
      cancel2 add neg zero hac haa haz hinv
        (Nq add mul d L).1 (Nq add mul d L).1 (Nq add mul d L).2.1]

/- ── the banked instances (decided; the general functions at concrete data) ──── -/

/-- concrete Gaussian-integer operations for the decided instances -/
def iadd : Int → Int → Int := Int.add
def imul : Int → Int → Int := Int.mul
def ineg : Int → Int := Int.neg

/-- the six banked rosters' instances of the general statement's shape, decided exactly:
    the μ₄ character sum equals (4·N₁, 0) with N₁ the banked global sector dimension —
    R5: 1; R1: 16; R2: 144; R3: 2304; R4: 12544; EXT: 38025 (the b51/b55/b56 banks) -/
theorem banked_roster_instances :
    (padd iadd (padd iadd (prod0 iadd imul ineg 0 (0,0,1,0) [(1,1,1,1)])
                          (prod1 iadd imul ineg (0,0,1,0) [(1,1,1,1)]))
               (padd iadd (prod2 iadd imul ineg 0 (0,0,1,0) [(1,1,1,1)])
                          (prod3 iadd imul ineg (0,0,1,0) [(1,1,1,1)]))
      = (4 * 1, 0)) ∧
    (padd iadd (padd iadd (prod0 iadd imul ineg 0 (0,0,1,0) [(1,1,1,1),(4,4,4,4)])
                          (prod1 iadd imul ineg (0,0,1,0) [(1,1,1,1),(4,4,4,4)]))
               (padd iadd (prod2 iadd imul ineg 0 (0,0,1,0) [(1,1,1,1),(4,4,4,4)])
                          (prod3 iadd imul ineg (0,0,1,0) [(1,1,1,1),(4,4,4,4)]))
      = (4 * 16, 0)) ∧
    (padd iadd (padd iadd (prod0 iadd imul ineg 0 (2,2,3,2) [(16,16,16,16)])
                          (prod1 iadd imul ineg (2,2,3,2) [(16,16,16,16)]))
               (padd iadd (prod2 iadd imul ineg 0 (2,2,3,2) [(16,16,16,16)])
                          (prod3 iadd imul ineg (2,2,3,2) [(16,16,16,16)]))
      = (4 * 144, 0)) ∧
    (padd iadd (padd iadd (prod0 iadd imul ineg 0 (2,2,3,2) [(16,16,16,16),(4,4,4,4)])
                          (prod1 iadd imul ineg (2,2,3,2) [(16,16,16,16),(4,4,4,4)]))
               (padd iadd (prod2 iadd imul ineg 0 (2,2,3,2) [(16,16,16,16),(4,4,4,4)])
                          (prod3 iadd imul ineg (2,2,3,2) [(16,16,16,16),(4,4,4,4)]))
      = (4 * 2304, 0)) ∧
    (padd iadd (padd iadd (prod0 iadd imul ineg 0 (12,12,13,12) [(16,16,16,16),(4,4,4,4)])
                          (prod1 iadd imul ineg (12,12,13,12) [(16,16,16,16),(4,4,4,4)]))
               (padd iadd (prod2 iadd imul ineg 0 (12,12,13,12) [(16,16,16,16),(4,4,4,4)])
                          (prod3 iadd imul ineg (12,12,13,12) [(16,16,16,16),(4,4,4,4)]))
      = (4 * 12544, 0)) ∧
    (padd iadd (padd iadd (prod0 iadd imul ineg 0 (56,56,57,56) [(169,169,169,169)])
                          (prod1 iadd imul ineg (56,56,57,56) [(169,169,169,169)]))
               (padd iadd (prod2 iadd imul ineg 0 (56,56,57,56) [(169,169,169,169)])
                          (prod3 iadd imul ineg (56,56,57,56) [(169,169,169,169)]))
      = (4 * 38025, 0)) := by decide

end CharacterSumShadow
