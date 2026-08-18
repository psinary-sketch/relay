/-
  W-ATTEMPT-2 · DiagonalSection.lean — THE SECTION'S DECIDE-REACHABLE CONTENT, COMPILED
  ====================================================================================

  ATTEMPT-track, RELAY-RESIDENT. Closure-protocol step one run against the CONSTRUCTION
  (never against any sign): the exact content of the diagonal section D(a) that vanilla
  Lean's `decide` reaches — the a = √2 cell (the {2:1} factor over ℤ[i]) and the class
  factor (the circulant, its character spectrum, the label-norm trace) over ℤ[ω].

  Vanilla Lean 4 (v4.29.1, pinned), no imports beyond the sibling GroupRingGlue's
  namespace conventions (this file is self-contained); every theorem closed by `decide`
  or `rfl`; expected axiom profile for every terminal: "does not depend on any axioms".

  ── WHAT THIS MODULE COMPILES ───────────────────────────────────────────────────

  (1) THE a = √2 CELL, over ℤ[i] (integer pairs, i² = −1). On G = ℤ/4 the Sonin
      space Son(2,1) is spanned by f = e₁ − e₃. With TF4 := 2·F₄ (the DFT scaled to
      Gaussian integers, TF4[j][k] = i^(jk)):
        · f vanishes on the integers' ball {0, 2}, and so does TF4·f  (membership);
        · TF4·f = 2i·f  — the transform carries the cell to itself EXACTLY, F f = i·f;
        · parity (m ↦ −m) sends f to −f — the compressed parity Π = [−1];
        · the Gram integer  ⟨f, TF4 f⟩ = 4i ≠ 0  (the local Gram G_loc = 2i after the
          1/2 normalization) — the radical at this cell is ZERO;
        · conj(4i) = (−1)·(4i) — the parity-twisted-Hermitian identity  G† = G·Π,
          exact at this cell (the float-era residual ~6e−15, here EXACT).

  (2) THE CLASS FACTOR, over ℤ[ω] (integer pairs, ω² = −1 − ω). With the coupling
      c₂c₃ = 2[0]+[1]+[2] (compiled in GroupRingGlue):
        · the character spectrum χ₀, χ₁, χ₂ of the coupling = (4, 1, 1), computed in
          ℤ[ω] with the imaginary parts landing EXACTLY zero, every value nonzero;
        · the Gram's class factor is the circulant C = [[2,1,1],[1,2,1],[1,1,2]]:
          symmetric, det C = 4 ≠ 0 (the class factor's radical is ZERO), and C IS the
          multiplication-by-coupling matrix, so its spectrum IS the character spectrum;
        · the trace identity: tr C = 6 = 4 + 1 + 1 = χ₀ + χ₁ + χ₂ — the coupling
          spectrum as the CLASS-CHARACTER TRACE (the τ-route; question grade at bench);
        · the label-norm enumeration: the four norm-6 ideal-label sums
          {[1]+[2], [1]+[1], [2]+[2], [2]+[1]} have class counts (2, 1, 1) — the
          coupling's coefficients: the gluing datum IS the class-resolved Euler data,
          at the integer level;
        · the antipode matrix A: A² = 1 and A·C·A = C (antipode-coherence of the Gram).

  ── WHAT NEEDS A MATHLIB COMPANION, NAMED NOT FAKED ─────────────────────────────

  The {3:1} and {2:2} factors need exact arithmetic in ℚ(ζ₉) and ℚ(ζ₁₆) (the glued
  cells: ℚ(ζ₃₆), ℚ(ζ₁₄₄)) — a cyclotomic tower with proved minimal-polynomial
  reduction. That is Mathlib's `NumberTheory.Cyclotomic` / `Polynomial.cyclotomic`
  territory (or a hand-rolled tower with its own reduction lemmas) and is NOT built
  here. The bench instrument b18_attempt2_s5.py holds those entries EXACTLY
  (ℚ(ζ₁₄₄) as Fraction-vectors mod Φ₁₄₄) with its registration banked; this module
  carries the decide-reachable shadow and names the companion.

  ── WHAT THIS MODULE DOES NOT COMPILE, DECLARED ─────────────────────────────────

  NO inertia (carried as banked bench DATA, sitting 2), NO archimedean factor
  (sitting 6's model, bench grade), NO statement about W_∞ − ΣW_𝔭 at complete
  roster, and NO SENTENCE OF ANY KIND ABOUT ANY SIGN. This file is not a kernel
  deposit and nothing in it bears on h2. It certifies properties of a BUILT FINITE
  OBJECT; it moves no register.
-/

namespace DiagonalSection

/-- a Gaussian integer: re + im·i, i² = −1 -/
structure ZI where
  re : Int
  im : Int
deriving DecidableEq, Repr

def ZI.add (x y : ZI) : ZI := ⟨x.re + y.re, x.im + y.im⟩
def ZI.mul (x y : ZI) : ZI := ⟨x.re * y.re - x.im * y.im, x.re * y.im + x.im * y.re⟩
def ZI.neg (x : ZI) : ZI := ⟨-x.re, -x.im⟩
def ZI.conj (x : ZI) : ZI := ⟨x.re, -x.im⟩
def ZI.zero : ZI := ⟨0, 0⟩
def ZI.I : ZI := ⟨0, 1⟩

def zsum : List ZI → ZI := List.foldr ZI.add ZI.zero
def dot (u v : List ZI) : ZI := zsum (List.zipWith ZI.mul u v)
def matvec (M : List (List ZI)) (v : List ZI) : List ZI := M.map (fun r => dot r v)
def smul (c : ZI) (v : List ZI) : List ZI := v.map (ZI.mul c)
def conjv (v : List ZI) : List ZI := v.map ZI.conj

/-- 2·F₄: the DFT on ℤ/4 scaled into ℤ[i] — entries i^(jk) -/
def TF4 : List (List ZI) :=
  [[⟨1,0⟩, ⟨1,0⟩, ⟨1,0⟩, ⟨1,0⟩],
   [⟨1,0⟩, ⟨0,1⟩, ⟨-1,0⟩, ⟨0,-1⟩],
   [⟨1,0⟩, ⟨-1,0⟩, ⟨1,0⟩, ⟨-1,0⟩],
   [⟨1,0⟩, ⟨0,-1⟩, ⟨-1,0⟩, ⟨0,1⟩]]

/-- the exact Sonin basis vector of Son(2,1): f = e₁ − e₃ on ℤ/4 -/
def f : List ZI := [⟨0,0⟩, ⟨1,0⟩, ⟨0,0⟩, ⟨-1,0⟩]

/-- functions on ℤ/4 as a 4-tuple (match-free carrier for the parity action) -/
structure V4 where
  x0 : ZI
  x1 : ZI
  x2 : ZI
  x3 : ZI
deriving DecidableEq, Repr

def V4.toList (v : V4) : List ZI := [v.x0, v.x1, v.x2, v.x3]

/-- f as a 4-tuple -/
def fV : V4 := ⟨⟨0,0⟩, ⟨1,0⟩, ⟨0,0⟩, ⟨-1,0⟩⟩

/-- parity m ↦ −m on ℤ/4: index map 0,3,2,1 -/
def parityV (v : V4) : V4 := ⟨v.x0, v.x3, v.x2, v.x1⟩

def smulV (c : ZI) (v : V4) : V4 :=
  ⟨ZI.mul c v.x0, ZI.mul c v.x1, ZI.mul c v.x2, ZI.mul c v.x3⟩

/- ── (1) the a = √2 cell ───────────────────────────────────────────────────── -/

/-- f vanishes on the integers' ball {0, 2} -/
theorem f_ball_zero : f = [ZI.zero, ⟨1,0⟩, ZI.zero, ⟨-1,0⟩] := by decide

/-- the transform of f, computed exactly: TF4·f = [0, 2i, 0, −2i] — it vanishes on
    the ball {0, 2}, so f lands in Son on the transform side too -/
theorem hat_f_ball_zero : matvec TF4 f = [ZI.zero, ⟨0,2⟩, ZI.zero, ⟨0,-2⟩] := by decide

/-- T-invariance at the cell, exact: TF4·f = 2i·f, i.e. F f = i·f -/
theorem transform_eigen : matvec TF4 f = smul ⟨0,2⟩ f := by decide

/-- fV is f (the tuple and list carriers agree) -/
theorem fV_is_f : fV.toList = f := by decide

/-- the compressed parity at the cell: Π = [−1] -/
theorem parity_f : parityV fV = smulV ⟨-1,0⟩ fV := by decide

/-- the Gram integer ⟨f, TF4 f⟩ = 4i — nonzero: the radical at this cell is zero
    (the local Gram is G_loc = 2i after the 1/2 DFT normalization) -/
theorem gram_cell : dot (conjv f) (matvec TF4 f) = ⟨0,4⟩ := by decide

theorem gram_cell_nonzero : dot (conjv f) (matvec TF4 f) ≠ ZI.zero := by decide

/-- the parity-twisted-Hermitian identity at the cell, exact: G† = G·Π with Π = [−1] -/
theorem twisted_hermitian_cell :
    ZI.conj ⟨0,4⟩ = ZI.mul ⟨0,4⟩ ⟨-1,0⟩ := by decide

/- ── (2) the class factor ──────────────────────────────────────────────────── -/

/-- an Eisenstein integer: a + b·ω, ω² = −1 − ω -/
structure ZW where
  a : Int
  b : Int
deriving DecidableEq, Repr

def ZW.add (x y : ZW) : ZW := ⟨x.a + y.a, x.b + y.b⟩
def ZW.mul (x y : ZW) : ZW := ⟨x.a * y.a - x.b * y.b, x.a * y.b + x.b * y.a - x.b * y.b⟩
def ZW.omega : ZW := ⟨0, 1⟩
def ZW.ofInt (n : Int) : ZW := ⟨n, 0⟩

/-- ω^k for k = 0, 1, 2, 3, 4 (period 3) -/
def wpow : Nat → ZW
  | 0 => ⟨1, 0⟩
  | 1 => ⟨0, 1⟩
  | 2 => ⟨-1, -1⟩
  | n + 3 => wpow n

/-- the coupling c₂c₃ = 2[0] + [1] + [2] (compiled in GroupRingGlue.coupling_23) -/
def coup : Nat → Int
  | 0 => 2
  | 1 => 1
  | _ => 1

/-- the k-th class character applied to the coupling: Σ_c coup(c)·ω^(kc) -/
def chi (k : Nat) : ZW :=
  ZW.add (ZW.mul (ZW.ofInt (coup 0)) (wpow 0))
    (ZW.add (ZW.mul (ZW.ofInt (coup 1)) (wpow (k % 3)))
      (ZW.mul (ZW.ofInt (coup 2)) (wpow ((2 * k) % 3))))

/-- the character spectrum of the coupling is (4, 1, 1) — computed in ℤ[ω], the
    ω-parts landing exactly zero, every value nonzero -/
theorem spectrum_411 : chi 0 = ⟨4, 0⟩ ∧ chi 1 = ⟨1, 0⟩ ∧ chi 2 = ⟨1, 0⟩ := by decide

theorem spectrum_nonzero : chi 0 ≠ ⟨0,0⟩ ∧ chi 1 ≠ ⟨0,0⟩ ∧ chi 2 ≠ ⟨0,0⟩ := by decide

/-- the Gram's class factor: the circulant C[α][β] = coup((β−α) mod 3) — which is
    also EXACTLY the multiplication-by-coupling matrix on ℤ[ℤ/3] -/
structure M3 where
  a : Int
  b : Int
  c : Int
  d : Int
  e : Int
  f : Int
  g : Int
  h : Int
  i : Int
deriving DecidableEq, Repr

def C : M3 := ⟨2, 1, 1, 1, 2, 1, 1, 1, 2⟩

def transpose3 (m : M3) : M3 := ⟨m.a, m.d, m.g, m.b, m.e, m.h, m.c, m.f, m.i⟩

def det3 (m : M3) : Int :=
  m.a * (m.e * m.i - m.f * m.h) - m.b * (m.d * m.i - m.f * m.g)
    + m.c * (m.d * m.h - m.e * m.g)

def trace3 (m : M3) : Int := m.a + m.e + m.i

/-- the class factor is symmetric -/
theorem C_symmetric : transpose3 C = C := by decide

/-- det C = 4 ≠ 0: the class factor's radical is zero -/
theorem C_radical_zero : det3 C = 4 ∧ det3 C ≠ 0 := by decide

/-- THE TRACE IDENTITY: tr C = 6 = χ₀ + χ₁ + χ₂ = 4 + 1 + 1 — the coupling spectrum
    as the class-character trace (the τ-route; the analytic identification with the
    label-norm coefficient of Ẑ is bench-certified at relay, question grade) -/
theorem trace_identity :
    trace3 C = 6 ∧ ZW.add (chi 0) (ZW.add (chi 1) (chi 2)) = ⟨6, 0⟩ := by decide

/-- the label-norm enumeration: the four norm-6 ideal-label sums, with labels
    [𝔭₂] ∈ {1,2} and [𝔭₃] ∈ {2,1} (conjugate pairs), have class counts (2,1,1) —
    exactly the coupling's coefficients -/
def norm6sums : List Nat := [(1+2) % 3, (1+1) % 3, (2+2) % 3, (2+1) % 3]

def countc (k : Nat) : Nat := (norm6sums.filter (fun c => c == k)).length

theorem label_norm_is_coupling :
    countc 0 = 2 ∧ countc 1 = 1 ∧ countc 2 = 1 := by decide

/-- the antipode matrix on ℂ[Cl] coordinates: an involution that fixes the class
    factor — antipode-coherence of the Gram's class part -/
def A : M3 := ⟨1, 0, 0, 0, 0, 1, 0, 1, 0⟩

def mm3 (x y : M3) : M3 :=
  ⟨x.a*y.a + x.b*y.d + x.c*y.g, x.a*y.b + x.b*y.e + x.c*y.h, x.a*y.c + x.b*y.f + x.c*y.i,
   x.d*y.a + x.e*y.d + x.f*y.g, x.d*y.b + x.e*y.e + x.f*y.h, x.d*y.c + x.e*y.f + x.f*y.i,
   x.g*y.a + x.h*y.d + x.i*y.g, x.g*y.b + x.h*y.e + x.i*y.h, x.g*y.c + x.h*y.f + x.i*y.i⟩

theorem antipode_involution : mm3 A A = ⟨1, 0, 0, 0, 1, 0, 0, 0, 1⟩ := by decide

theorem antipode_fixes_class_gram : mm3 A (mm3 C A) = C := by decide

end DiagonalSection
