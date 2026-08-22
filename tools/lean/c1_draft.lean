import Mathlib.Analysis.InnerProductSpace.Projection.Basic
import Mathlib.Analysis.InnerProductSpace.Projection.Submodule

open scoped InnerProductSpace
open Topology Filter

namespace C1Draft

variable {H : Type*} [NormedAddCommGroup H] [InnerProductSpace ℂ H]

/-- the C₄ idempotent for a fourth root `lam` (no inverses: `lam⁻¹ = lam³` when
    `lam⁴ = 1`). -/
noncomputable def proj4 (F : H →ₗ[ℂ] H) (lam : ℂ) (x : H) : H :=
  (4 : ℂ)⁻¹ • (x + lam ^ 3 • F x + lam ^ 2 • F (F x) + lam • F (F (F x)))

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

theorem proj4_sum (F : H →ₗ[ℂ] H) (x : H) :
    proj4 F 1 x + proj4 F Complex.I x + proj4 F (-1) x + proj4 F (-Complex.I) x = x := by
  unfold proj4
  have hI2 : Complex.I ^ 2 = -1 := Complex.I_sq
  have hI3 : Complex.I ^ 3 = -Complex.I := by
    rw [pow_succ, hI2]; ring
  have hnI2 : (-Complex.I) ^ 2 = -1 := by rw [neg_pow]; simp [hI2]
  have hnI3 : (-Complex.I) ^ 3 = Complex.I := by
    rw [pow_succ, hnI2]; ring
  rw [hI2, hI3, hnI2, hnI3]
  norm_num
  module

end C1Draft
