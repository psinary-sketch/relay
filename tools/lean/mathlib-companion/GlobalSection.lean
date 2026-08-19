/-
  W-CONSTRUCTION-1 act 3 — GlobalSection.lean: act 1's global object STATED in Lean.
  Mathlib holds the TOPOLOGICAL RestrictedProduct (grep-checked: Topology/Algebra/
  RestrictedProduct, FiniteAdeleRing) but NOT the Hilbert-space restricted tensor
  product — so the object is a DECLARED structure with its existence the single
  labeled infrastructure debt. The one-line consequences are PROVED from the fields.
  Nothing at complete roster; sorries counted, labeled.
-/
import Mathlib.Analysis.InnerProductSpace.Projection.Basic
import Mathlib.LinearAlgebra.PiTensorProduct

open scoped InnerProductSpace

namespace GlobalSection

/- THE RESTRICTED-TENSOR INNER CORE and THE ASSEMBLY: NOT claimed here. Per the
    2026-08-19 ruling (no sorry in a kernel) both former statements moved to the
    working layer (relay/reports/2026-08-19-sorry-ledger-cleared.md, items 2-3)
    until they can enter PROVED. -/

/-- THE GLOBAL SECTION as data: a Hilbert space with a unitary `F` and `parity`,
    `F² = parity`, `parity² = 1` — the abstract shape act 1 proved the restricted
    tensor product carries (the `E₁`-units make `⊗F_v` well-defined; `F² = ⊗Π_v`).
    The CONSTRUCTION of this data as `⊗′_v S̄_v` is the infrastructure debt. -/
structure GlobalSectionData where
  H : Type
  [ncg : NormedAddCommGroup H]
  [ips : InnerProductSpace ℂ H]
  F : H ≃ₗᵢ[ℂ] H
  parity : H ≃ₗᵢ[ℂ] H
  F_sq : ∀ x, F (F x) = parity x
  parity_sq : ∀ x, parity (parity x) = x

attribute [instance] GlobalSectionData.ncg GlobalSectionData.ips

/-- `F⁴ = 1` on the global section — PROVED from the fields, no sorry. -/
theorem F_pow_four (D : GlobalSectionData) (x : D.H) :
    D.F (D.F (D.F (D.F x))) = x := by
  rw [D.F_sq, D.F_sq, D.parity_sq]

/-- the pairing is the squared norm on the fixed sector — PROVED (one line, via the
    LocalLimit abstract theorem's argument), no sorry. -/
theorem inner_F_self_of_fixed (D : GlobalSectionData) (x : D.H) (hx : D.F x = x) :
    ⟪x, D.F x⟫_ℂ = (‖x‖ : ℂ) ^ 2 := by
  rw [hx, inner_self_eq_norm_sq_to_K]
  norm_cast

end GlobalSection

#print axioms GlobalSection.F_pow_four
#print axioms GlobalSection.inner_F_self_of_fixed
