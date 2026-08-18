/-
  W-ATTEMPT-2 · GroupRingGlue.lean — THE GLUE'S INTEGER CONTENT, COMPILED
  ======================================================================

  ATTEMPT-track, RELAY-RESIDENT. This is closure-protocol step one run against the
  CONSTRUCTION (never against any sign): the integer half of the glued object's data.

  Vanilla Lean 4, no imports, every theorem closed by `decide` or `rfl`; expected axiom
  profile for every terminal: "does not depend on any axioms".

  ── WHAT THIS MODULE COMPILES ───────────────────────────────────────────────────

  The group-ring ℤ[ℤ/3] as integer triples (coefficients of [0], [1], [2]) with its
  convolution product and the ANTIPODE (star: [c] ↦ [−c]); the place labels of the
  minimal instance K = ℚ(√−23), h = 3:

      c₂ = c₃ = [1] + [2]   (split primes, non-principal conjugate pair)
      c₅ = [0]              (5 inert; the prime above it is principal)

  the COUPLING ELEMENTS c₂·c₃ = 2[0]+[1]+[2] and c₂·c₃·c₅ (equal — c₅ is the identity);
  antipode self-duality of every label and coupling; the class relation
  [𝔭₂][𝔭₃] = [0] (1 + 2 ≡ 0 mod 3, the norm-6 principal witness); and the INTEGER
  character spectrum of antipode-self-dual elements — for (a,b,b) the values are
  ψ₀ = a + 2b and ψ = ψ̄ = a − b (since ω + ω² = −1), so the spectrum of the coupling
  is (4, 1, 1), all entries nonzero (the invertibility avatar).

  ── WHAT THIS MODULE DOES NOT COMPILE, DECLARED ─────────────────────────────────

  NO pairing, NO Fourier/DFT structure (that is the cyclotomic half — DESIGNED, NOT
  BUILT: it needs exact arithmetic in a cyclotomic tower for the compressed-DFT
  entries), NO Hermitian form, NO inertia, and NO SENTENCE OF ANY KIND ABOUT ANY SIGN.
  The analytic identifications (that these integers are the norm-150 coefficients of
  the class-resolved Euler product; that the coupling is the gluing datum) are
  bench-certified at relay with their registrations — cited there, not claimed here.
  This file is not a kernel deposit and nothing in it bears on h2.
-/

namespace GroupRingGlue

/-- an element of ℤ[ℤ/3]: coefficients of [0], [1], [2] -/
structure GR where
  a : Int
  b : Int
  c : Int
deriving DecidableEq, Repr

/-- convolution product on ℤ[ℤ/3] -/
def mul (x y : GR) : GR :=
  ⟨x.a * y.a + x.b * y.c + x.c * y.b,
   x.a * y.b + x.b * y.a + x.c * y.c,
   x.a * y.c + x.b * y.b + x.c * y.a⟩

/-- the antipode: [c] ↦ [−c], i.e. swap the [1] and [2] coefficients -/
def star (x : GR) : GR := ⟨x.a, x.c, x.b⟩

/-- the split-prime label at 2 (and at 3): [1] + [2] -/
def c2 : GR := ⟨0, 1, 1⟩
def c3 : GR := ⟨0, 1, 1⟩
/-- the inert-prime label at 5: [0] (principal) -/
def c5 : GR := ⟨1, 0, 0⟩

/-- integer character values of an antipode-self-dual element (a,b,b):
    ψ₀ = a + 2b; ψ = ψ̄ = a − b (from ω + ω² = −1). -/
def psi0 (x : GR) : Int := x.a + x.b + x.c
def psiSelfDual (x : GR) : Int := x.a - x.b

/- ── the coupling elements ─────────────────────────────────────────────────── -/

theorem coupling_23 : mul c2 c3 = ⟨2, 1, 1⟩ := by decide
theorem coupling_235 : mul (mul c2 c3) c5 = ⟨2, 1, 1⟩ := by decide

/- ── antipode self-duality of every label and of the coupling ──────────────── -/

theorem star_c2 : star c2 = c2 := by decide
theorem star_c3 : star c3 = c3 := by decide
theorem star_c5 : star c5 = c5 := by decide
theorem star_coupling : star (mul c2 c3) = mul c2 c3 := by decide

/- ── the class relation: [𝔭₂][𝔭₃] principal (the norm-6 witness) ───────────── -/

theorem class_relation : (1 + 2) % 3 = 0 := by decide

/- ── the integer character spectrum of the coupling: (4, 1, 1), all nonzero ── -/

theorem spectrum_psi0 : psi0 (mul c2 c3) = 4 := by decide
theorem spectrum_psi : psiSelfDual (mul c2 c3) = 1 := by decide
theorem spectrum_invertible :
    psi0 (mul c2 c3) ≠ 0 ∧ psiSelfDual (mul c2 c3) ≠ 0 := by decide

/- ── the antipode is an involution and an anti-automorphism shadow ──────────── -/

theorem star_involutive (x : GR) : star (star x) = x := rfl

end GroupRingGlue
