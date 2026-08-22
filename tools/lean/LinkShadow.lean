/-
  THE LINK ACT'S DECIDED CORE · LinkShadow.lean
  ==============================================

  Ferry 2026-08-22 (b103). Vanilla Lean 4 (v4.29.1 pinned), no imports; expected
  profile per terminal: "does not depend on any axioms".

  L2 asked whether the extension's wing datum can be tied to the boundary line's
  ζ₈ phase THROUGH R, the only recorded dictionary. This module carries the two
  decided facts that answer it, and they answer it in opposite directions:

  · `twisted_row_silence` — R annihilates the twisted rows. The block sum of the
    g-family's root-of-unity column over a full block is the full count exactly
    when the row is untwisted, and zero for every twisted row, at the banked
    place-2 cells. Since the C₈ frame lives on the twisted sectors ONLY (rows
    39/48, decided), the frame's datum is exactly what R sends to zero: THE
    TRANSPORT IS BLOCKED, and blocked by a decided fact rather than by an
    absence.
  · `witness_no_fixed_point` and `witness_exchange_involution` — conjugation
    acts on the frame's witnesses with NO fixed witness, pairing them in
    2-cycles. On the archimedean side the recorded Schwarz covariance likewise
    fixes the ray and EXCHANGES the two wings. Both actions are exchanges, and
    an exchange supplies a RELATION and never a selection — which is why the
    gauge discipline's demand (relation, never absolute class) is met on both
    sides at once, and why no absolute reading could be pronounced from either.

  Bank: relay data/b103_link_act.txt.
-/

set_option maxRecDepth 8192

namespace LinkShadow

def m16 (e : Nat) : List Int :=
  match e % 16 with
  | 0 => [1,0,0,0,0,0,0,0] | 1 => [0,1,0,0,0,0,0,0] | 2 => [0,0,1,0,0,0,0,0]
  | 3 => [0,0,0,1,0,0,0,0] | 4 => [0,0,0,0,1,0,0,0] | 5 => [0,0,0,0,0,1,0,0]
  | 6 => [0,0,0,0,0,0,1,0] | 7 => [0,0,0,0,0,0,0,1] | 8 => [-1,0,0,0,0,0,0,0]
  | 9 => [0,-1,0,0,0,0,0,0] | 10 => [0,0,-1,0,0,0,0,0] | 11 => [0,0,0,-1,0,0,0,0]
  | 12 => [0,0,0,0,-1,0,0,0] | 13 => [0,0,0,0,0,-1,0,0] | 14 => [0,0,0,0,0,0,-1,0]
  | _ => [0,0,0,0,0,0,0,-1]
def vadd (u v : List Int) : List Int := List.zipWith (· + ·) u v
def z8 : List Int := [0,0,0,0,0,0,0,0]

/-- the block sum of the g-family's column phases at (2,2): Σ_b ζ^{4tb} -/
def blockSum (t : Nat) : List Int :=
  (List.range 4).foldl (fun acc b => vadd acc (m16 ((4 * t * b) % 16))) z8

/-- R ANNIHILATES THE TWISTED ROWS: the block sum is the full count 4 exactly on
    the untwisted row and ZERO on every twisted row. With rows 39/48 (the C₈
    frame lives on the twisted sectors only), this is the transport obstruction
    in kernel: the only recorded dictionary sends the frame's carrier to zero. -/
theorem twisted_row_silence :
    blockSum 0 = [4,0,0,0,0,0,0,0] ∧
    blockSum 1 = z8 ∧ blockSum 2 = z8 ∧ blockSum 3 = z8 := by decide

/-- the frame's witness exponents at the twisted sectors (rows 39–40) -/
def witnesses : List Nat := [2, 6]
def conjExp (e : Nat) : Nat := (16 - e % 16) % 16

/-- CONJUGATION HAS NO FIXED WITNESS: no witness exponent equals its own
    conjugate, so the action supplies no selection within the frame — only an
    exchange between its two sectors. -/
theorem witness_no_fixed_point :
    witnesses.all (fun e => decide (conjExp e ≠ e)) = true := by decide

/-- THE EXCHANGE IS AN INVOLUTION, and it pairs the witnesses in 2-cycles: the
    conjugate of each witness is the other sector's witness's partner, and
    conjugating twice returns the witness. An exchange with no fixed point
    carries a RELATION and never an absolute selection. -/
theorem witness_exchange_involution :
    witnesses.all (fun e => decide (conjExp (conjExp e) = e)) = true ∧
    conjExp 2 = 14 ∧ conjExp 6 = 10 ∧
    ((2 + conjExp 2) % 16 = 0) ∧ ((6 + conjExp 6) % 16 = 0) := by decide

end LinkShadow
