/-
  THE PURITY CHECK AT THE BANKED CELLS · E1UnitPurityDraft.lean — WORKING-LAYER DRAFT
  ====================================================================================

  DRAFT ONLY — NOT KERNEL-PLACED. Kernel placement touches the currency question at
  the author's desk (ferry 2026-08-19, foot); this file exists so the ruling has a
  compiled object to rule on. Vanilla Lean 4 (v4.29.1 pinned), no imports, no Mathlib,
  decide only; expected axiom profile per terminal: "does not depend on any axioms".

  WHAT THIS MODULE COMPILES — the b44 verdicts' finite exact content (registration
  data/b44_registration_2026-08-19.txt, banked before the run; report
  reports/2026-08-19-e1-unit-purity.md):

  The model at cell (p,n): N = p^(2n), q = p^n, chart m = a + q·b (b13, banked).
  The E₁-space at each cell is the image of the sector projector
      4q·P₁ = (q + S)(1 + Π)   on Son(p,n)
  (S the unnormalized DFT, S² = q²Π — b23/b26 banked, re-verified exactly in b44 G1;
  P₁ the +1-sector projector since M = S/q has M⁴ = 1). The spanning vector u_{i,j}
  is 4q·P₁ applied to the Sonin basis vector f_{i,j} = e_i ⊗ (e_j − e_0); writing
  h = f + Πf (an integer function with ≤ 4 support points), its m-th coefficient is
      u(m) = q·h(m) + Σ_{m'} h(m')·ζ^{m'·m}   ∈ ℤ[ζ_N]   — encoded below verbatim.

  Arithmetic: sparse monomial lists over ℤ[x]/(x^N−1), reduced mod Φ_{p^k} only at
  the zero test (Φ_{p^k}(x) = Σ_{i<p} x^{i·N/p}; for the leading block c = p−1 the
  monomial folds to −Σ_{i≤p−2} x^{i·N/p + r}). A 2×2 minor is a difference of two
  products of entries; Schmidt-purity ⟺ all 2×2 minors vanish (rank ≤ 1) — the
  registration's identity (a), longhand there.

  THE THEOREMS (each `decide`, each exact):
  · (2,1)  death_2_1        — (1+Π)f = 0: the projector image is 0; d₁(2,1) = 0
                              (the banked arrival-depth death, re-derived in-kernel).
  · (3,1)  unit31_mixed     — THE UNIQUE unit (d₁ = 1, banked b26) has a nonvanishing
                              2×2 minor: E₁(3,1) contains NO nonzero pure vector.
  · (2,2)  pencilA_nonzero, pencilCross_zero, pencilC2_zero, u2_mixed —
           for the basis u₁ = u_{1,1}, u₂ = u_{1,2} of E₁(2,2) (independence and
           d₁ = 2: b44 G4/G5, banked b23), the minor at rows (1,2), cols (0,2) of
           αu₁ + βu₂ expands as α²·A + αβ·B + β²·C (the determinant's quadratic-form
           expansion, longhand in the report) with A ≠ 0, B = 0, C = 0 — so purity
           forces α = 0 — and u₂ itself has a nonvanishing minor at rows (1,3),
           cols (0,1): E₁(2,2) contains NO nonzero pure vector over ANY extension.
  · (5,1), (2,3), (3,2)  witness51 / witness23 / witness32 — the canonical spanning
           unit u_{1,1} at each remaining banked cell has a nonvanishing 2×2 minor
           (the generic unit is mixed; the full Segre intersection at d₁ > 2 is
           declared open in the report, not decided here).

  WHAT IT DOES NOT COMPILE, DECLARED: d₁ values and basis-independence enter as
  BANKED DATA (b23/b26; b44 gates G4/G5, exact); the quadratic-form expansion of the
  pencil minor is longhand in the report; nothing at complete roster; no sign;
  h2 untouched.
-/

namespace E1UnitPurityDraft

/-- sparse ℤ[x]/(x^N−1): list of (coefficient, exponent) monomials, uncombined -/
abbrev Sp := List (Int × Nat)

def mulSp (a b : Sp) : Sp :=
  a.foldl (fun acc p => acc ++ b.map fun q => (p.1 * q.1, p.2 + q.2)) []

def subSp (a b : Sp) : Sp := a ++ b.map fun p => (-p.1, p.2)

/-- reduce mod Φ_{p^k}: dense coefficient list on the power basis
    x^(c·(N/p)+r), c ≤ p−2, r < N/p (length N − N/p); Bool tests only
    (the getD/prop-ite propext leak of the SectorArithmetic precedent avoided) -/
def phiRed (p N : Nat) (v : Sp) : List Int :=
  let Np := N / p
  (List.range (N - Np)).map fun k =>
    v.foldl
      (fun s q =>
        let e := q.2 % N
        if e == k then s + q.1
        else if (e / Np == p - 1) && (e % Np == k % Np) then s - q.1
        else s)
      0

def isZero (p N : Nat) (v : Sp) : Bool := (phiRed p N v).all (· == 0)

/-- u(m) = q·h(m) + Σ_(c,m')∈h c·ζ^(m'·m), h = f + Πf as a monomial list -/
def entry (qq N : Nat) (h : Sp) (m : Nat) : Sp :=
  let hv : Int := (h.filter fun p => p.2 % N == m % N).foldl (fun s p => s + p.1) 0
  (if hv == 0 then [] else [(Int.ofNat qq * hv, 0)]) ++ h.map fun p => (p.1, p.2 * m)

/-- 2×2 minor from the four chart coefficients u(m₁₁), u(m₂₂), u(m₁₂), u(m₂₁) -/
def minor (u : Nat → Sp) (m11 m22 m12 m21 : Nat) : Sp :=
  subSp (mulSp (u m11) (u m22)) (mulSp (u m12) (u m21))

/- ── (2,1): h = f_{1,1} + Πf_{1,1} = 0 — the projector image is 0, d₁ = 0 ── -/

def h21 : Sp := [(1, 3), (-1, 1), (1, 1), (-1, 3)]

theorem death_2_1 :
    ((List.range 4).all fun m =>
      ((h21.filter fun p => p.2 % 4 == m).foldl (fun s p => s + p.1) 0) == 0) = true := by
  decide

/- ── (3,1): N = 9, q = 3; h = {4:1, 1:−1, 5:1, 8:−1}; chart (a,b) ↦ a + 3b;
      witness minor rows (1,2), cols (0,1): u(1)u(5) − u(4)u(2) ≠ 0 in ℤ[ζ₉] ── -/

def h31 : Sp := [(1, 4), (-1, 1), (1, 5), (-1, 8)]
def u31 : Nat → Sp := entry 3 9 h31

theorem unit31_mixed : isZero 3 9 (minor u31 1 5 4 2) = false := by decide

/- ── (2,2): N = 16, q = 4; u₁ from h₁ = {5:1, 1:−1, 11:1, 15:−1},
      u₂ from h₂ = {9:1, 1:−1, 7:1, 15:−1}; chart (a,b) ↦ a + 4b.
      Pencil minor at rows (1,2), cols (0,2): coefficients on (α², αβ, β²).
      u₂'s own witness at rows (1,3), cols (0,1). ── -/

def h22a : Sp := [(1, 5), (-1, 1), (1, 11), (-1, 15)]
def h22b : Sp := [(1, 9), (-1, 1), (1, 7), (-1, 15)]
def uA : Nat → Sp := entry 4 16 h22a
def uB : Nat → Sp := entry 4 16 h22b

theorem pencilA_nonzero : isZero 2 16 (minor uA 1 10 9 2) = false := by decide

theorem pencilCross_zero :
    isZero 2 16 (subSp
      (mulSp (uA 1) (uB 10) ++ mulSp (uB 1) (uA 10))
      (mulSp (uA 9) (uB 2) ++ mulSp (uB 9) (uA 2))) = true := by decide

theorem pencilC2_zero : isZero 2 16 (minor uB 1 10 9 2) = true := by decide

theorem u2_mixed : isZero 2 16 (minor uB 1 7 5 3) = false := by decide

/- ── (5,1): N = 25, q = 5; h = {6:1, 1:−1, 19:1, 24:−1}; chart (a,b) ↦ a + 5b;
      witness rows (1,2), cols (0,1): u(1)u(7) − u(6)u(2) ── -/

def h51 : Sp := [(1, 6), (-1, 1), (1, 19), (-1, 24)]
def u51 : Nat → Sp := entry 5 25 h51

theorem witness51 : isZero 5 25 (minor u51 1 7 6 2) = false := by decide

/- ── (2,3): N = 64, q = 8; h = {9:1, 1:−1, 55:1, 63:−1}; chart (a,b) ↦ a + 8b;
      witness rows (1,2), cols (0,1): u(1)u(10) − u(9)u(2) ── -/

def h23 : Sp := [(1, 9), (-1, 1), (1, 55), (-1, 63)]
def u23 : Nat → Sp := entry 8 64 h23

theorem witness23 : isZero 2 64 (minor u23 1 10 9 2) = false := by decide

/- ── (3,2): N = 81, q = 9; h = {10:1, 1:−1, 71:1, 80:−1}; chart (a,b) ↦ a + 9b;
      witness rows (1,2), cols (0,1): u(1)u(11) − u(10)u(2) ── -/

def h32 : Sp := [(1, 10), (-1, 1), (1, 71), (-1, 80)]
def u32 : Nat → Sp := entry 9 81 h32

theorem witness32 : isZero 3 81 (minor u32 1 11 10 2) = false := by decide

/- ══════════════════════════════════════════════════════════════════════════════════
   EXTENSION (2026-08-20, the Protection Act, step 4) — THE KL-FAILURE WITNESSES
   ══════════════════════════════════════════════════════════════════════════════════

   b45's Tier-1 verdict (β): E₁ is NOT a distance-≥2 code in the factor-block model —
   at every cell with d₁ ≥ 2 the Knill–Laflamme detection condition P·E·P = c(E)·P
   fails, first witness E = E_{1,1}⊗1 at Gram entry (0,1). The decidable core encoded
   here: with basis u₀ = u_{1,1}, u₁ = u_{1,2} (independence banked, b44/b45), Gram
   entries G_{rs} = Σ_m conj(u_r(m))·u_s(m), and X_{rs} = Σ_t conj(u_r(1+qt))·u_s(1+qt)
   (the E_{1,1}⊗1 compression), the cross-multiplied discrepancy
       X_{01}·G_{00} − G_{01}·X_{00}   ≠ 0   in ℤ[ζ_N]
   — which refutes X = c·G for every scalar c, hence refutes the KL condition, exactly.
   Conjugation is ζ ↦ ζ^{-1} on monomials. Encoded at (2,2) and (5,1); the (2,3)/(3,2)
   witnesses and b46's Segre–Macaulay certificates (rank 364/816 mod ℓ) are DECLARED
   beyond sensible decide reach and live in the banks. Framing data (d₁, basis
   identity) enters banked, declared in the head. -/

set_option maxRecDepth 8192

def conjSp (N : Nat) (a : Sp) : Sp := a.map fun p => (p.1, (N - p.2 % N) % N)

/-- normalize: reduce mod Φ, re-express as sparse monomials on the power basis -/
def redSp (p N : Nat) (v : Sp) : Sp :=
  let d := phiRed p N v
  (List.zip (List.range d.length) d).filterMap fun q =>
    if q.2 == 0 then none else some (q.2, q.1)

/-- Gram entry Σ_{m<N} conj(u m)·(v m), normalized -/
def gramE (p N : Nat) (u v : Nat → Sp) : Sp :=
  redSp p N ((List.range N).foldl (fun acc m => acc ++ mulSp (conjSp N (u m)) (v m)) [])

/-- E_{1,1}⊗1 compression entry Σ_{t<q} conj(u (1+qt))·(v (1+qt)), normalized -/
def xE11 (p N q : Nat) (u v : Nat → Sp) : Sp :=
  redSp p N ((List.range q).foldl
    (fun acc t => acc ++ mulSp (conjSp N (u (1 + q * t))) (v (1 + q * t))) [])

/- (2,2): u₀ = uA (h22a), u₁ = uB (h22b) — b44's own pencil basis -/
theorem kl_fail_2_2 :
    isZero 2 16 (subSp
      (mulSp (xE11 2 16 4 uA uB) (gramE 2 16 uA uA))
      (mulSp (gramE 2 16 uA uB) (xE11 2 16 4 uA uA))) = false := by decide

/- (5,1): u₀ = u_{1,1} (h51), u₁ = u_{1,2} (h51b) — the b45 greedy basis, identity banked -/
def h51b : Sp := [(1, 11), (-1, 1), (1, 14), (-1, 24)]
def u51b : Nat → Sp := entry 5 25 h51b

theorem kl_fail_5_1 :
    isZero 5 25 (subSp
      (mulSp (xE11 5 25 5 u51 u51b) (gramE 5 25 u51 u51))
      (mulSp (gramE 5 25 u51 u51b) (xE11 5 25 5 u51 u51))) = false := by decide

end E1UnitPurityDraft
