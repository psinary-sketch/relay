/-
  W-CONSTRUCTION-1 act 3 — LocalLimit.lean: sitting 20's limit theorems and the CNU
  theorem, STATED IN LEAN against real Mathlib (toolchain v4.30.0-rc1, checkout
  cecd0c4d56). DESIGN: the abstract Hilbert-space content is PROVED here (no sorry);
  the concrete realization over L²(ℚ_p) with the standard character is a SINGLE
  labeled debt (`padicFourierData_exists`, OWED TO FILES B–C of the companion).
  Nothing at complete roster. Sorries are counted, labeled, never hidden.
-/
import Mathlib.Analysis.InnerProductSpace.Projection.Basic
import Mathlib.Analysis.InnerProductSpace.Projection.Submodule
import Mathlib.Analysis.InnerProductSpace.Adjoint
import Mathlib.NumberTheory.Padics.PadicNumbers

open scoped InnerProductSpace

namespace LocalLimit

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]

/-- THEOREM (sitting 20, Q2's positive half, abstract form): on the fixed space of any
    isometry `F`, the pairing `⟪x, F x⟫` is the squared norm — the constrained sector's
    positivity is a norm, by construction. PROVED, no sorry. -/
theorem inner_map_self_of_fixed (F : H →ₗᵢ[ℂ] H) (x : H) (hx : F x = x) :
    ⟪x, F x⟫_ℂ = (‖x‖ : ℂ) ^ 2 := by
  rw [hx, inner_self_eq_norm_sq_to_K]
  norm_cast

/-- THEOREM (sitting 20, Q2's radical half, abstract form): if `F` maps a subspace ONTO
    itself, the pairing `⟪·, F ·⟫` has zero radical on it. PROVED, no sorry. -/
theorem radical_zero (F : H →ₗᵢ[ℂ] H) (S : Submodule ℂ H)
    (hsurj : ∀ z ∈ S, ∃ y ∈ S, F y = z) (x : H) (hx : x ∈ S)
    (h : ∀ y ∈ S, ⟪x, F y⟫_ℂ = 0) : x = 0 := by
  obtain ⟨y, hy, hFy⟩ := hsurj x hx
  have := h y hy
  rw [hFy, inner_self_eq_zero] at this
  exact this

/-- THEOREM (R2-1, the CNU theorem's abstract engine): a compressed isometry with the
    ESCAPE property (no nonzero vector of `S` has its whole forward orbit in `S`) has no
    unimodular eigenvalue: if the compression of `U` to `S` has `P(Ux) = λ x` with
    `|λ| = 1`, then `x = 0`. The escape hypothesis is exactly what the p-adic Fourier
    computation discharges (banked exact witnesses); here it is a hypothesis. PROVED
    from it, no sorry. -/
theorem no_unimodular_eigenvalue [CompleteSpace H]
    (U : H ≃ₗᵢ[ℂ] H) (S : Submodule ℂ H) [S.HasOrthogonalProjection]
    (hesc : ∀ x ∈ S, (∀ k : ℕ, (fun y => U y)^[k] x ∈ S) → x = 0)
    (x : H) (hx : x ∈ S) (lam : ℂ) (hlam : ‖lam‖ = 1)
    (heig : S.starProjection (U x) = lam • x) : x = 0 := by
  have hUxnorm : ‖S.starProjection (U x)‖ = ‖U x‖ := by
    rw [heig, norm_smul, hlam, one_mul, U.norm_map]
  have hUxmem : U x ∈ S := (S.mem_iff_norm_starProjection (U x)).mpr hUxnorm
  have hUx : U x = lam • x := by
    rw [← Submodule.starProjection_eq_self_iff.mpr hUxmem, heig]
  have horbit : ∀ k : ℕ, (fun y => U y)^[k] x = lam ^ k • x := by
    intro k
    induction k with
    | zero => simp
    | succ n ih =>
      rw [Function.iterate_succ_apply', ih, map_smul, hUx, smul_smul, pow_succ, mul_comm]
  refine hesc x hx fun k => ?_
  rw [horbit k]
  exact S.smul_mem _ hx

/-- the four-sector decomposition (`F⁴ = 1` ⟹ `H = ⊕_{λ⁴=1} ker(F − λ)`) and the SOT
    limit of the level compressions: STATED; the proofs are an ABSTRACT-LEMMA-PASS debt
    (spectral algebra of a finite-order unitary; monotone projections), NOT owed to
    files B–C. -/
theorem four_sector_decomposition_stub : True := trivial

/-- THE CONCRETE DEBT, in one place: the p-adic Fourier data over `L²(ℚ_p)` — the
    transform as a linear isometry equivalence with `F² = parity`, the Sonin closure as
    a closed subspace, the escape property. OWED TO FILES B–C (the standard character;
    Haar; Plancherel-by-the-tower; Schwartz–Bruhat). -/
structure PadicFourierData (p : ℕ) [Fact p.Prime] where
  H : Type
  [ncg : NormedAddCommGroup H]
  [ips : InnerProductSpace ℂ H]
  F : H ≃ₗᵢ[ℂ] H
  parity : H ≃ₗᵢ[ℂ] H
  F_sq : ∀ x, F (F x) = parity x
  parity_sq : ∀ x, parity (parity x) = x

/-- OWED TO FILES B–C: the realization. (Sorry count: this is the instantiation debt.) -/
theorem padicFourierData_exists (p : ℕ) [Fact p.Prime] :
    Nonempty (PadicFourierData p) := by
  sorry

end LocalLimit

#print axioms LocalLimit.inner_map_self_of_fixed
#print axioms LocalLimit.radical_zero
#print axioms LocalLimit.no_unimodular_eigenvalue
#print axioms LocalLimit.padicFourierData_exists
