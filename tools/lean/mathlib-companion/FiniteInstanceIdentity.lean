/-
  FILE E of the Mathlib companion (opened at W-CONSTRUCTION-1 act 16):
  THE FINITE-INSTANCE IDENTITY — THE CLOSURE PROTOCOL'S STEP-ONE OBJECT.

  ### THE REGISTER SENTENCE, QUOTED UNCHANGED: "h2 IS THE SINGLE OPEN PREMISE."

  THIS FILE STATES; IT DOES NOT PROVE. This states the identity whose truth at
  complete roster is h2; at finite instance it is checkable; nothing here proves it.

  THE CONSTITUENTS AND THEIR OWNERS (the ledger's addresses, labeled):
  · the ε-regularized archimedean E₁-trace — owner: the ε-lemma's bookkeeping (its
    geometry now DERIVED, act 15: the pair structure whose block inverses are the
    ε-denominators) and files B–C's L²(ℚ_p) for the finite factors;
  · the volume-normalized quotient trace — owner: FILE D (the fixed-orbit count,
    proved longhand act 9, its formalization file D's labeled sorry) with the volume
    normalization forced (act 7, modulo the class-richness lemma at cite);
  · the restricted-tensor assembly — owner: INFRASTRUCTURE (the Hilbert ⊗′; the sharp
    missing lemma stated in GlobalSection.lean);
  · Weil's ledger — the atlas's certified columns at the cell, in the CC sign
    convention (the act-12 dictionary).

  SORRY COUNT OF THIS FILE: 0 — and, per the 2026-08-19 ruling, EVERY kernel file's.
  The constituents are DATA PARAMETERS (Props over supplied structures), NOT sorried
  declarations; their realizations live in the WORKING LAYER as recorded statements
  (relay/reports/2026-08-19-sorry-ledger-cleared.md) until they can enter proved.
-/
import Mathlib.Data.Real.Basic
import Mathlib.Data.Rat.Defs

namespace FiniteInstanceIdentity

/-- a banked diagonal cell: the window a² > 1. -/
structure DiagonalCell where
  a_sq : ℚ
  one_lt : 1 < a_sq

/-- the ε-regularized archimedean E₁-trace on the constrained class at a cell.
    OWNER: the ε-lemma's bookkeeping (geometry derived, act 15) + files B–C. -/
structure ArchimedeanE1Trace (cell : DiagonalCell) where
  value : ℝ

/-- the volume-normalized quotient trace at a cell.
    OWNER: file D (the count) + the forced volume normalization (act 7). -/
structure QuotientTrace (cell : DiagonalCell) where
  value : ℝ

/-- Weil's ledger at the cell: `W_∞` (CC convention, the act-12 dictionary) and the
    prime sum, the atlas's certified columns. -/
structure WeilLedger (cell : DiagonalCell) where
  wInf : ℝ
  wPrimes : ℝ

/-- ### THE FINITE-INSTANCE IDENTITY (STATED, NOT PROVED, NOT CLAIMED):
    the built object's trace equals Weil's ledger on the constrained class at the
    cell. Its truth at complete roster is `h2`; at finite instance it is checkable;
    nothing here proves it. The register moves only via the closure protocol's four
    steps in order — this file is step one's OBJECT (the formal statement), not its
    discharge. -/
def finiteInstanceIdentity {cell : DiagonalCell}
    (T : ArchimedeanE1Trace cell) (Q : QuotientTrace cell)
    (W : WeilLedger cell) : Prop :=
  T.value + Q.value = W.wInf - W.wPrimes

end FiniteInstanceIdentity

#print axioms FiniteInstanceIdentity.finiteInstanceIdentity
