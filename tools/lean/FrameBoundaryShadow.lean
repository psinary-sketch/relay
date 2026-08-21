/-
  THE FRAME-BOUNDARY EXTENSIONS · FrameBoundaryShadow.lean
  =========================================================

  Ferry 2026-08-21 (b68). Vanilla Lean 4 (v4.29.1 pinned), no imports; expected
  profile per terminal: "does not depend on any axioms".

  THE DECIDED CORE (the b68 registration): THE NATIVITY BOUNDARY — the scalar root
  of i is ±ζ_N^{N/8}, requiring 8 | N: native at place-2 depth n ≥ 2 (16, 64, 256);
  NOT native at the boundary cell (2,1) (8 ∤ 4 — the registered refusal, the degree
  witness longhand-cited); never reachable at odd cells even with the banked
  pair-ring i-adjunction (4q² ≡ 4 mod 8). The corrected slogan, the registration's
  own finding: the C₈ frame is native exactly where the live fixed point lives AT
  DEPTH — the boundary cell carries the fixed point but not yet the frame. THE
  PARITY SPLIT AT EVERY CELL: the whole-chart refusal witness is the u-line
  (S u = q u; Π u = u; u ≠ −u) — decided here at the smallest cell of each parity
  ((2,1) in ℤ[i] pairs; (3,1) in ℤ[ζ₉] six-coordinates, x⁶ = −x³ − 1); the general
  u-line law is the banked b57 longhand, cited. THE LIMIT FRAME: the eighth-root
  exponent's constancy and its square (ζ₈² = i in exponent arithmetic) — the
  row-45 boundary phase and the row-40 scalar the same object at the limit; the
  (2,1) refusal dissolves at the limit (depth unbounded).
  Bank: relay data/b68_frame_boundary.txt.
-/

namespace FrameBoundaryShadow

/-- THE NATIVITY ARITHMETIC, decided: 8 | N exactly at place-2 depth ≥ 2; the
    boundary cell (2,1) refuses (8 ∤ 4); the odd cells' banked pair-ring conductor
    4q² ≡ 4 mod 8 never reaches the eighth root -/
theorem nativity_arithmetic :
    (16 % 8 = 0 ∧ 64 % 8 = 0 ∧ 256 % 8 = 0) ∧ ¬(4 % 8 = 0) ∧
    ((4 * 3 * 3) % 8 = 4 ∧ (4 * 5 * 5) % 8 = 4 ∧ (4 * 9 * 9) % 8 = 4 ∧
     (4 * 27 * 27) % 8 = 4) := by decide

/-- ℤ[i] pairs for the (2,1) instance -/
def zpow4 (e : Nat) : Int × Int :=
  match e % 4 with
  | 0 => (1, 0) | 1 => (0, 1) | 2 => (-1, 0) | _ => (0, -1)
def padd (u v : Int × Int) : Int × Int := (u.1 + v.1, u.2 + v.2)

/-- ℤ[ζ₉] in six coordinates (x⁶ = −x³ − 1) for the (3,1) instance -/
def mono9 (c : Int) (e : Nat) : List Int :=
  let r := e % 9
  if r < 6 then (List.range 6).map (fun k => if k = r then c else 0)
  else (List.range 6).map (fun k => if k = r - 6 ∨ k = r - 3 then -c else 0)
def vadd9 (u v : List Int) : List Int := List.zipWith (· + ·) u v

/-- THE u-LINE WITNESSES, decided at the smallest cell of each parity: S u = q u
    exactly ((2,1): the row sums 1 + ζ₄^{2m′} = 2·[2 | m′]; (3,1): the row sums
    1 + ζ₉^{3m′} + ζ₉^{6m′} = 3·[3 | m′]), with Π u = u by the symmetric support
    and u ≠ −u — the whole-chart parity-even refusal witness at every cell (the
    general law the banked b57 longhand, cited) -/
theorem uline_witnesses :
    ((List.range 4).map (fun mp => padd (zpow4 0) (zpow4 (2 * mp))) =
      (List.range 4).map (fun mp => if mp % 2 = 0 then ((2, 0) : Int × Int) else (0, 0))) ∧
    ((List.range 9).map (fun mp => vadd9 (mono9 1 0) (vadd9 (mono9 1 (3 * mp)) (mono9 1 (6 * mp)))) =
      (List.range 9).map (fun mp =>
        if mp % 3 = 0 then ([3, 0, 0, 0, 0, 0] : List Int) else [0, 0, 0, 0, 0, 0])) ∧
    ((4 - 0) % 4 = 0 ∧ (4 - 2) % 4 = 2 ∧ (9 - 0) % 9 = 0 ∧ (9 - 3) % 9 = 6 ∧ (9 - 6) % 9 = 3) ∧
    (((1, 0) : Int × Int) ≠ (-1, 0)) := by decide

/-- THE LIMIT-FRAME ARITHMETIC, decided: the eighth-root exponent's level constancy
    (N/8 ↦ p²·N/8 = N⁺/8) and its square ((N/8)·2 = N/4 — ζ₈² = i in exponent
    arithmetic): the row-45 boundary phase and the row-40 scalar are the same object
    at the limit -/
theorem limit_frame_arithmetic :
    ((16 / 8) * 4 = 64 / 8 ∧ (64 / 8) * 4 = 256 / 8) ∧
    ((16 / 8) * 2 = 16 / 4 ∧ (64 / 8) * 2 = 64 / 4 ∧ (256 / 8) * 2 = 256 / 4) := by
  decide

end FrameBoundaryShadow
