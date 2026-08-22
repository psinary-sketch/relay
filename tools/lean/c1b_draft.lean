import Mathlib.Analysis.InnerProductSpace.Projection.Basic
import Mathlib.Analysis.InnerProductSpace.Projection.Submodule

open scoped InnerProductSpace
open Topology Filter

namespace C1bDraft

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]

/-- THE SOT LIMIT OF THE LEVEL COMPRESSIONS (the abstract clause): for a monotone
    family `U` of submodules with orthogonal projections, the compressions of a
    bounded operator `A` to the levels converge strongly to the compression on the
    closure of the supremum. -/
theorem compression_tendsto {ι : Type*} [Preorder ι]
    (U : ι → Submodule ℂ H) [∀ i, (U i).HasOrthogonalProjection]
    [(⨆ i, U i).topologicalClosure.HasOrthogonalProjection]
    (hU : Monotone U) (A : H →L[ℂ] H) (x : H) :
    Tendsto (fun i => (U i).starProjection (A ((U i).starProjection x))) atTop
      (𝓝 ((⨆ i, U i).topologicalClosure.starProjection
            (A ((⨆ i, U i).topologicalClosure.starProjection x)))) := by
  set P := (⨆ i, U i).topologicalClosure with hP
  have h2 : Tendsto (fun i => (U i).starProjection (A (P.starProjection x))) atTop
      (𝓝 (P.starProjection (A (P.starProjection x)))) :=
    Submodule.starProjection_tendsto_closure_iSup U hU _
  have hx : Tendsto (fun i => (U i).starProjection x) atTop (𝓝 (P.starProjection x)) :=
    Submodule.starProjection_tendsto_closure_iSup U hU x
  have hxn : Tendsto (fun i => ‖(U i).starProjection x - P.starProjection x‖) atTop (𝓝 0) :=
    tendsto_iff_norm_sub_tendsto_zero.mp hx
  have h1 : Tendsto (fun i => (U i).starProjection (A ((U i).starProjection x))
      - (U i).starProjection (A (P.starProjection x))) atTop (𝓝 0) := by
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

end C1bDraft
