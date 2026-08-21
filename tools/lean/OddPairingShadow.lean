/-
  THE ODD-PART PAIRING · OddPairingShadow.lean
  =============================================

  Ferry 2026-08-21 (b63, the epsilon-minus act, part B's derivable core). Vanilla
  Lean 4 (v4.29.1 pinned), no imports; expected profile per terminal: "does not
  depend on any axioms".

  THE γ₂ DISCHARGE AS LOCATION (the b63 registration, step B2): for a real
  PARITY-ODD vector, the transform pairing ⟨f, Sf⟩ is PURELY IMAGINARY — derived
  from S* = Π∘S (the kernel's conjugation is the kernel at the negated argument —
  the same recorded ground as F² = parity) and Π's commutation with S; the even
  twin is real by the same chain. The real-valuedness that blocked the eighth root
  in the junction act (γ₂) was therefore a property of the EVEN CLASS, not of the
  functional — the odd class carries imaginary pairings by derivation.

  Compiled: the abstract odd/even pairing lemmas at named hypotheses; the decided
  finite instances at the (2,1) chart (the seed's pairing 4i, conj-antisymmetric;
  the even contrast δ₀'s pairing 1, conj-symmetric); the odd weights' class
  equation ((±i)² = −1, decided); the odd collapse shape i·a + (−i)·b = i(a − b)
  at named hypotheses (the odd twin of the even collapse m₁ − m₋₁).
  Bank: relay data/b61_epsilon_minus.txt (the ferry-named bank).
-/

namespace OddPairingShadow

/- ── the abstract pairing lemmas ─────────────────────────────────────────────── -/

/-- THE ODD-PAIRING LEMMA: with the adjoint relation S* = Π∘S, Π–S commutation, and
    parity-oddness, the transform pairing is conj-antisymmetric — purely imaginary -/
theorem odd_pairing_imaginary {V A : Type}
    (inner : V → V → A) (S Pi : V → V) (vneg : V → V) (conj neg : A → A) (f : V)
    (hswap : conj (inner f (S f)) = inner (S f) f)
    (hadj : inner (S f) f = inner f (Pi (S f)))
    (hcomm : Pi (S f) = S (Pi f))
    (hodd : Pi f = vneg f)
    (hlin : S (vneg f) = vneg (S f))
    (hneg : inner f (vneg (S f)) = neg (inner f (S f))) :
    conj (inner f (S f)) = neg (inner f (S f)) := by
  rw [hswap, hadj, hcomm, hodd, hlin, hneg]

/-- THE EVEN TWIN: parity-evenness makes the same pairing conj-symmetric — real;
    the junction act's γ₂ located as the even class's property -/
theorem even_pairing_real {V A : Type}
    (inner : V → V → A) (S Pi : V → V) (conj : A → A) (f : V)
    (hswap : conj (inner f (S f)) = inner (S f) f)
    (hadj : inner (S f) f = inner f (Pi (S f)))
    (hcomm : Pi (S f) = S (Pi f))
    (heven : Pi f = f) :
    conj (inner f (S f)) = inner f (S f) := by
  rw [hswap, hadj, hcomm, heven]

/- ── the decided finite instances at (2,1), N = 4, ℤ[i] pairs ────────────────── -/

def zpow4 (e : Nat) : Int × Int :=
  match e % 4 with
  | 0 => (1, 0) | 1 => (0, 1) | 2 => (-1, 0) | _ => (0, -1)

def padd (u v : Int × Int) : Int × Int := (u.1 + v.1, u.2 + v.2)
def pneg (u : Int × Int) : Int × Int := (-u.1, -u.2)
def pconj (u : Int × Int) : Int × Int := (u.1, -u.2)
def pmul (u v : Int × Int) : Int × Int :=
  (u.1 * v.1 - u.2 * v.2, u.1 * v.2 + u.2 * v.1)

/-- the seed u = δ₁ − δ₃ at (2,1): (Su)(1) = ζ − ζ³ = 2i, (Su)(3) = −2i; the pairing
    ⟨u, Su⟩ = (Su)(1) − (Su)(3) = 4i, and conj(4i) = −4i — PURELY IMAGINARY, decided;
    the even contrast ⟨δ₀, Sδ₀⟩ = 1, conj-symmetric — real, decided -/
theorem seed_pairing_instances :
    (padd (zpow4 1) (pneg (zpow4 3)) = (0, 2)) ∧
    (padd (zpow4 3) (pneg (zpow4 9)) = (0, -2)) ∧
    (padd (0, 2) (pneg (0, -2)) = (0, 4)) ∧
    (pconj (0, 4) = pneg (0, 4)) ∧
    (zpow4 0 = (1, 0) ∧ pconj (1, 0) = (1, 0)) := by decide

/-- the odd weights' class equation: (±i)² = −1 — the two odd classes' defining
    arithmetic, decided in pairs -/
theorem odd_weights_table :
    pmul (0, 1) (0, 1) = (-1, 0) ∧ pmul (0, -1) (0, -1) = (-1, 0) := by decide

/- ── the odd collapse shape ──────────────────────────────────────────────────── -/

/-- THE ODD COLLAPSE: i·(a, 0) + (−i)·(b, 0) = (0, a − b) over an abstract
    coefficient structure at named hypotheses — the transform-weighted odd sum is
    i(m_i − m₋ᵢ), the odd twin of the even collapse m₁ − m₋₁ -/
theorem odd_collapse {A : Type} (add mul : A → A → A) (neg : A → A) (zero one : A)
    (hmzl : ∀ x, mul zero x = zero)
    (hmzr : ∀ x, mul x zero = zero)
    (hone : ∀ x, mul one x = x)
    (hmnl : ∀ x y, mul (neg x) y = neg (mul x y))
    (hnz : neg zero = zero)
    (haz : ∀ x, add x zero = x)
    (hza : ∀ x, add zero x = x)
    (a b : A) :
    (add (mul zero a) (neg (mul one zero)),
     add (mul zero zero) (mul one a)) = ((zero, a) : A × A) ∧
    (add (mul zero b) (neg (mul (neg one) zero)),
     add (mul zero zero) (mul (neg one) b)) = ((zero, neg b) : A × A) ∧
    (add zero zero, add a (neg b)) = ((zero, add a (neg b)) : A × A) := by
  refine ⟨?_, ?_, ?_⟩
  · rw [hmzl, hmzr, hnz, hza, hmzl, hza, hone]
  · rw [hmzl, hmzr, hnz, hza, hmzl, hza, hmnl, hone]
  · rw [haz]

end OddPairingShadow
