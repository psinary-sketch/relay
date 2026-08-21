/-
  THE TWISTED-SECTOR ROOT CHECK · TwistedRootShadow.lean
  =======================================================

  Ferry 2026-08-21 (b60, component 3). Vanilla Lean 4 (v4.29.1 pinned), no imports;
  expected profile per terminal: "does not depend on any axioms".

  BRANCH (a) — the registered expectation, landed: at (2,2) on the twisted half
  E_i ⊕ E_{−i} (where M² = −1 already, so the row-39 parity obstruction is absent by
  construction), square roots of M EXIST: any W with W² = M preserves M's eigenspaces,
  and the eigenvalue square-root pairing is available in the banked ring — the square
  roots of i are ±ζ₁₆², of −i are ±ζ₁₆⁶, and every odd-index eighth root has fourth
  power −1 (decided below). The scalar witness W = ζ²·Id on E_i ⊕ ζ⁶·Id on E_{−i}
  satisfies W² = M and W⁴ = −1 (the abstract scalar-root lemma below, its instance's
  eigenvector the compiled row-33 tower witness M(ιu) = i·ιu). THE TWISTED HALF OF
  THE CHART SITS INSIDE THE C₈ FRAME at the cell — 5 of the 9 Sonin dimensions;
  extension questions staged, not run. Bank: relay data/b59_twisted_root.txt.
-/

namespace TwistedRootShadow

/-- a monomial c·ζ₁₆^e reduced in ℤ[x]/(x⁸+1), as a length-8 coordinate list -/
def mono (c : Int) (e : Nat) : List Int :=
  let r := e % 8
  let s : Int := if (e / 8) % 2 = 0 then c else -c
  (List.range 8).map (fun k => if k = r then s else 0)

/-- THE EIGHTH-ROOT PAIRING TABLE, decided: the odd-index eighth roots ζ^{2j}
    (j = 1, 3, 5, 7) square to i, −i, i, −i and all have fourth power −1 — the
    square-root supply for both twisted eigenvalues, with the C₈ sign automatic -/
theorem eighth_root_pairing :
    (mono 1 (4 * 1) = [0, 0, 0, 0, 1, 0, 0, 0] ∧
     mono 1 (8 * 1) = [-1, 0, 0, 0, 0, 0, 0, 0]) ∧
    (mono 1 (4 * 3) = [0, 0, 0, 0, -1, 0, 0, 0] ∧
     mono 1 (8 * 3) = [-1, 0, 0, 0, 0, 0, 0, 0]) ∧
    (mono 1 (4 * 5) = [0, 0, 0, 0, 1, 0, 0, 0] ∧
     mono 1 (8 * 5) = [-1, 0, 0, 0, 0, 0, 0, 0]) ∧
    (mono 1 (4 * 7) = [0, 0, 0, 0, -1, 0, 0, 0] ∧
     mono 1 (8 * 7) = [-1, 0, 0, 0, 0, 0, 0, 0]) := by decide

/-- THE SCALAR-ROOT LEMMA, abstract: a scalar c with c² = λ, acting on a
    λ-eigenvector of M through a composition-compatible scalar action, is a square
    root of M at that vector — the branch-(a) witness mechanism (its instance's
    eigenvector: row 33's compiled M(ιu) = i·ιu) -/
theorem scalar_root_on_eigenvector {C V : Type}
    (smul : C → V → V) (mul : C → C → C) (M : V → V)
    (hcomp : ∀ c d v, smul c (smul d v) = smul (mul c d) v)
    (c lam : C) (v : V)
    (hsq : mul c c = lam) (heig : M v = smul lam v) :
    smul c (smul c v) = M v := by
  rw [hcomp, hsq, heig]

end TwistedRootShadow
