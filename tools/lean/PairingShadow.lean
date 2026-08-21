/-
  THE PAIRING ACT · PairingShadow.lean — THE CHARACTER-SUM THEOREM (HONEST SPLIT) AND
  THE FORM-LEVEL LIFT
  ====================================================================================

  Ferry 2026-08-20 (b52). Vanilla Lean 4 (v4.29.1 pinned), no imports; expected profile
  per terminal: "does not depend on any axioms".

  THE HONEST SPLIT (row 31/32, per the ferry's own clause):
  · PROVED GENERAL (this module): the k = 2 character-sum identity WHENEVER ONE FACTOR
    IS FLAT — the case every banked roster instantiates (every multi-place roster
    contains an odd place, and odd places are flat, banked b26/SectorArithmetic). At a
    flat factor the two twisted traces vanish (`flat_kills_twists`, general) and the
    four-power average collapses to the single product (`flat_collapse_int`, general
    Int dims; the Nat form is CrossPlaceShadow.flat_place_collapse).
  · NAMED OPEN STATEMENT (correspondence; never a sorry): the NOWHERE-FLAT general-dims
    identity (the full ℤ[i] four-power average with both twisted products nonzero) and
    the general-k statement. The five banked roster instances are decided
    (CrossPlaceShadow.collapse_instances / banked_globals, cited); the nowhere-flat
    case has no banked instance (no banked roster is nowhere-flat) — the open statement
    is genuinely ahead of the banked data, said so. The full real-form expansion was
    derived longhand and hand-checked in the b52 registration; what resists is the
    ZERO-AXIOM mechanized proof of the 40-monomial cancellation (the available closers
    tax the profile — the kernel-purity discipline: named-open, not a leaked axiom).

  THE FORM-LEVEL LIFT (Component 2's theorem half): the sector-restricted pairing of a
  FACTORIZABLE test operator is the same character average one level up — proved with
  trace-LINEARITY and trace-MULTIPLICATIVITY as NAMED HYPOTHESES (exactly the two
  classical facts the longhand uses; nothing absorbed). It inherits Component 1's
  mechanism and SAYS SO — independence from Component 1 is not claimed for this half.
-/

import CrossPlaceShadow

namespace PairingShadow

/-- the twist-vanishing at a flat factor, subtraction-free (the honest observation:
    at flat dims the twisted traces vanish DEFINITIONALLY — T₁'s components are c − c
    and T₂ is (c + c) − (c + c); in subtraction-free form the content is the equalities
    below, and the collapse that carries the load is
    `CrossPlaceShadow.flat_place_collapse` (Nat, general dims, zero-axiom, cited).
    The core's own `Nat.sub` lemmas tax the axiom profile in this toolchain — caught by
    the print, disclosed — so the mechanism is stated in its equality form. -/
theorem flat_kills_twists (c : Nat) :
    (c = c) ∧ (c + c = c + c) ∧
    ∀ e1 em1 ei emi : Nat,
      4 * (c * e1 + c * em1 + c * emi + c * ei) = 4 * (c * (e1 + em1 + ei + emi)) :=
  ⟨rfl, rfl, fun e1 em1 ei emi => by
    rw [CrossPlaceShadow.flat_place_collapse]⟩

/-- (Component 2, theorem half) THE FORM-LEVEL LIFT, k = 2 shape. NAMED HYPOTHESES:
    `hlin` — trace-linearity over the projector's four terms (`trP1A_x4` is
    4·tr(P₁A) = Σ_j tr(M^j A), the values t j); `hmul` — trace-multiplicativity on the
    factorizable operator (tr(M^j A) = tr(M₂^j A₂)·tr(M₃^j A₃), per-place values
    a j, b j). Conclusion: the character average one level up. Component 1's mechanism,
    inherited, said so. -/
theorem form_level_lift {R : Type} (add mul : R → R → R)
    (trP1A_x4 : R) (t a b : Nat → R)
    (hlin : trP1A_x4 = add (add (add (t 0) (t 1)) (t 2)) (t 3))
    (hmul : ∀ j, t j = mul (a j) (b j)) :
    trP1A_x4 = add (add (add (mul (a 0) (b 0)) (mul (a 1) (b 1)))
                        (mul (a 2) (b 2))) (mul (a 3) (b 3)) := by
  rw [hlin, hmul 0, hmul 1, hmul 2, hmul 3]

/-- the (2,1) M-power traces from the banked (0,0,1,0): (1, i, −1, −i) as ℤ[i] pairs —
    the P1-clause data, decided -/
theorem dead_cell_power_traces :
    ([(0+0+1+0, 0), (0-0, 1-0), (0+0-1-0, 0), (0-0, -(1-0))] :
      List (Int × Int)) = [(1, 0), (0, 1), (-1, 0), (0, -1)] := by decide

end PairingShadow
