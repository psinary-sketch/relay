import Mathlib.Analysis.InnerProductSpace.Projection.Basic
import Mathlib.Analysis.InnerProductSpace.Projection.Submodule

open scoped InnerProductSpace
open Topology Filter

namespace LocalLimit

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]

/-- the `C₄` idempotent attached to a fourth root `lam` (no inverses appear: `lam⁻¹ =
    lam³` when `lam⁴ = 1`). -/
noncomputable def proj4 (F : H →ₗ[ℂ] H) (lam : ℂ) (x : H) : H :=
  (4 : ℂ)⁻¹ • (x + lam ^ 3 • F x + lam ^ 2 • F (F x) + lam • F (F (F x)))

/-- THE FOUR-SECTOR DECOMPOSITION, CLAUSE ONE (the eigen-property), PROVED — the
    former `four_sector_decomposition_stub`'s first half, discharged 2026-08-22
    (b100, the sense build act): for a finite-order `F` (`F⁴ = 1`) and any fourth
    root `lam`, the `C₄` idempotent lands in `ker(F − lam)`. Closed-form spectral
    projections; no sorry. -/
theorem proj4_eigen (F : H →ₗ[ℂ] H) (h4 : ∀ y : H, F (F (F (F y))) = y)
    (lam : ℂ) (hlam : lam ^ 4 = 1) (x : H) :
    F (proj4 F lam x) = lam • proj4 F lam x := by
  unfold proj4
  rw [map_smul, smul_comm]
  congr 1
  rw [map_add, map_add, map_add, map_smul, map_smul, map_smul, h4]
  rw [smul_add, smul_add, smul_add, smul_smul, smul_smul, smul_smul]
  rw [show lam * lam ^ 3 = lam ^ 4 by ring, hlam, one_smul]
  rw [show lam * lam ^ 2 = lam ^ 3 by ring, show lam * lam = lam ^ 2 by ring]
  abel

/-- THE FOUR-SECTOR DECOMPOSITION, CLAUSE TWO (completeness), PROVED — the four
    `C₄` idempotents sum to the identity, so `H = ⊕_{lam⁴=1} ker(F − lam)` as the
    docstring stated. With `proj4_eigen`: the decomposition, discharged. No sorry. -/
theorem proj4_sum (F : H →ₗ[ℂ] H) (x : H) :
    proj4 F 1 x + proj4 F Complex.I x + proj4 F (-1) x + proj4 F (-Complex.I) x = x := by
  unfold proj4
  have hI2 : Complex.I ^ 2 = -1 := Complex.I_sq
  have hI3 : Complex.I ^ 3 = -Complex.I := by rw [pow_succ, hI2]; ring
  have hnI2 : (-Complex.I) ^ 2 = -1 := by rw [neg_pow]; simp [hI2]
  have hnI3 : (-Complex.I) ^ 3 = Complex.I := by rw [pow_succ, hnI2]; ring
  rw [hI2, hI3, hnI2, hnI3]
  norm_num
  module

/-- THE SOT LIMIT OF THE LEVEL COMPRESSIONS, PROVED — the former stub's second
    half, discharged 2026-08-22 (b100): for a MONOTONE family `U` of submodules
    with orthogonal projections, the compressions of a bounded operator `A` to the
    levels converge strongly to the compression on the closure of the supremum.
    Mathlib's `starProjection_tendsto_closure_iSup` supplies the projection
    convergence; the operator step is the three-term split with the `‖P‖ ≤ 1`
    domination. No sorry.

    ### THE SCOPE, STATED SO NO READER OVER-CLAIMS IT (b100, filed at full
    prominence): this discharges the ABSTRACT clause the docstring stated — the
    abstract-lemma-pass debt this file named. It does NOT certify that the
    programme's concrete level family satisfies the MONOTONICITY hypothesis; that
    is a separate, concrete question whose owner is the construction, and b70's
    decided non-stabilization witness bears on it. The abstract lemma is proved;
    its applicability to the concrete family is NOT claimed here. -/
theorem compression_tendsto {ι : Type*} [Preorder ι]
    (U : ι → Submodule ℂ H) [∀ i, (U i).HasOrthogonalProjection]
    [(⨆ i, U i).topologicalClosure.HasOrthogonalProjection]
    (hU : Monotone U) (A : H →L[ℂ] H) (x : H) :
    Filter.Tendsto (fun i => (U i).starProjection (A ((U i).starProjection x))) Filter.atTop
      (nhds ((⨆ i, U i).topologicalClosure.starProjection
            (A ((⨆ i, U i).topologicalClosure.starProjection x)))) := by
  set P := (⨆ i, U i).topologicalClosure with hP
  have h2 : Filter.Tendsto (fun i => (U i).starProjection (A (P.starProjection x)))
      Filter.atTop (nhds (P.starProjection (A (P.starProjection x)))) :=
    Submodule.starProjection_tendsto_closure_iSup U hU _
  have hx : Filter.Tendsto (fun i => (U i).starProjection x) Filter.atTop
      (nhds (P.starProjection x)) :=
    Submodule.starProjection_tendsto_closure_iSup U hU x
  have hxn : Filter.Tendsto (fun i => ‖(U i).starProjection x - P.starProjection x‖)
      Filter.atTop (nhds 0) := tendsto_iff_norm_sub_tendsto_zero.mp hx
  have h1 : Filter.Tendsto (fun i => (U i).starProjection (A ((U i).starProjection x))
      - (U i).starProjection (A (P.starProjection x))) Filter.atTop (nhds 0) := by
    rw [tendsto_zero_iff_norm_tendsto_zero]
    refine squeeze_zero (g := fun i => ‖A‖ * ‖(U i).starProjection x - P.starProjection x‖)
      (fun i => norm_nonneg _) (fun i => ?_) ?_
    · have hlin : (U i).starProjection (A ((U i).starProjection x))
          - (U i).starProjection (A (P.starProjection x))
          = (U i).starProjection (A ((U i).starProjection x - P.starProjection x)) := by
        rw [← map_sub, ← map_sub]
      rw [hlin]
      calc ‖(U i).starProjection (A ((U i).starProjection x - P.starProjection x))‖
          ≤ ‖A ((U i).starProjection x - P.starProjection x)‖ :=
            Submodule.norm_starProjection_apply_le _ _
        _ ≤ ‖A‖ * ‖(U i).starProjection x - P.starProjection x‖ := A.le_opNorm _
    · have := hxn.const_mul ‖A‖
      simpa using this
  have hsum := h1.add h2
  simpa using hsum

end LocalLimit

#print axioms LocalLimit.proj4_eigen
#print axioms LocalLimit.proj4_sum
#print axioms LocalLimit.compression_tendsto
