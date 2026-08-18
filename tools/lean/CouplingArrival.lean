/-
  W-ATTEMPT-2 · CouplingArrival.lean — THE COUPLING-AS-TRACE IDENTITY WITH THE ARRIVAL LAW
  ========================================================================================

  ATTEMPT-track, RELAY-RESIDENT. Sitting 17. Vanilla Lean 4 (v4.29.1, pinned); imports
  only the sibling GroupRingGlue (itself vanilla, 11/11 axiom-free); decide/rfl only;
  expected axiom profile for every terminal: "does not depend on any axioms".

  WHAT THIS MODULE COMPILES — the finite identities over ℤ[ℤ/3]:
    · the label-norm enumeration at norm 150 = 2·3·25: the ideals of norm 150 in
      K = ℚ(√−23) factor as (𝔭₂ or 𝔭̄₂) · (𝔭₃ or 𝔭̄₃) · (5) — labels {1,2} × {2,1} × {0}
      — and their class counts are (2, 1, 1);
    · THE ARRIVAL LAW (multiplicativity in ℂ[Cl] at the integer level): the norm-150
      label coefficient equals the norm-6 coefficient CONVOLVED with the added place's
      label — (2,1,1) = (c₂·c₃)·c₅ in ℤ[ℤ/3] — the Euler-exact gluing law's integer
      shadow at one more norm;
    · the trace identity at 150: the character spectrum of the norm-150 coefficient is
      (4, 1, 1) — equal to the trace data of the coupling (tr of multiplication-by-
      coefficient = 6 = 4 + 1 + 1), i.e. the class-character TRACE reading, at norm 150
      exactly as at norm 6.

  WHAT IT DOES NOT COMPILE, DECLARED: the identification of these integers with the
  Dirichlet coefficients of the class-resolved Euler product is BENCH-CERTIFIED at relay
  (b14/b15 registrations, banked) and stays bench — this module carries the ℤ[ℤ/3]
  arithmetic only; nothing at complete roster; no ledger, no sign. h2 untouched.
-/

import GroupRingGlue

namespace CouplingArrival
open GroupRingGlue

/-- the label sums of the four norm-150 ideals: {1,2} × {2,1} × {0} mod 3 -/
def norm150sums : List Nat :=
  [(1 + 2 + 0) % 3, (1 + 1 + 0) % 3, (2 + 2 + 0) % 3, (2 + 1 + 0) % 3]

def countc (k : Nat) : Nat := (norm150sums.filter (fun c => c == k)).length

/-- the norm-150 label enumeration has class counts (2, 1, 1) -/
theorem label_norm_150 : countc 0 = 2 ∧ countc 1 = 1 ∧ countc 2 = 1 := by decide

/-- THE ARRIVAL LAW: the norm-150 coefficient IS the norm-6 coefficient convolved with
    the added place's label — (2,1,1) = (c₂·c₃)·c₅ in ℤ[ℤ/3] -/
theorem arrival_multiplicative_150 :
    mul (mul c2 c3) c5 = ⟨(countc 0 : Int), (countc 1 : Int), (countc 2 : Int)⟩ := by
  decide

/-- the trace identity at norm 150: spectrum (4, 1, 1), summing to the trace 6 -/
theorem spectrum_150 :
    psi0 (mul (mul c2 c3) c5) = 4 ∧ psiSelfDual (mul (mul c2 c3) c5) = 1 ∧
    psi0 (mul (mul c2 c3) c5) + 2 * psiSelfDual (mul (mul c2 c3) c5) = 6 := by decide

/-- the added place is dead at its arrival AND identity for the coupling: c₅ = [0] -/
theorem added_place_identity : mul (mul c2 c3) c5 = mul c2 c3 := by decide

end CouplingArrival
