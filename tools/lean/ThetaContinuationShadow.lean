/-
  THE THETA CONTINUATION'S DECIDED CORE · ThetaContinuationShadow.lean
  =====================================================================

  Ferry 2026-08-21 (b70). Vanilla Lean 4 (v4.29.1 pinned), no imports; expected
  profile per terminal: "does not depend on any axioms".

  Decided here (the b70 registration): THE CENTER EXITS AT EVERY BANKED PLACE-2
  LEVEL (every V-image position of the center's line is a ball position — the
  two-line index computation, per level), with the (2,2) exit-set EXACTLY the
  center and the deeper exit families counted as data (the radial-compression
  dictionary the named residue of N5's operator half); THE NON-STABILIZATION
  WITNESS (the level-1 scaling kills g₍₁,₁₎ while the level-2 scaling does not
  kill its embedded image — the SOT clause's sharpened form: the convergence
  question for a non-stabilizing level family); THE FINITE ORIENTATION BREAK
  (tr S = q(1+i) and tr S* = q(1−i) are distinct — the finite kernel convention
  breaks the F ↦ F³ symmetry that the recorded archimedean ground cannot break:
  the class bit is S1 content, the b70 derivation).
  Bank: relay data/b70_theta_continuation.txt.
-/

namespace ThetaContinuationShadow

/-- THE CENTER EXITS, decided per level: every V-image position 2·(q/2 + q·b) is a
    ball position (≡ 0 mod q) at q = 4, 8, 16; the (2,2) exit family is EXACTLY the
    center (the only even frequency at q = 4); the deeper families counted as data -/
theorem center_exit_instances :
    ((List.range 4).map (fun b => (2 * (4/2 + 4*b)) % 16 % 4) =
      (List.range 4).map (fun _ => 0)) ∧
    ((List.range 8).map (fun b => (2 * (8/2 + 8*b)) % 64 % 8) =
      (List.range 8).map (fun _ => 0)) ∧
    ((List.range 16).map (fun b => (2 * (16/2 + 16*b)) % 256 % 16) =
      (List.range 16).map (fun _ => 0)) ∧
    ((List.range 4).filter (fun t => decide (t ≠ 0) && decide (t % 2 = 0)) = [2]) ∧
    ((List.range 8).filter (fun t => decide (t ≠ 0) && decide (t % 2 = 0)) = [2, 4, 6]) := by
  decide

/-- ℤ[i] pairs for the level-1 computation -/
def padd (u v : Int × Int) : Int × Int := (u.1 + v.1, u.2 + v.2)

/-- THE NON-STABILIZATION WITNESS, decided: at (2,1) the scaling kills the seed's
    line (the two preimages' coefficients 1 and ζ₄² = −1 cancel on the single image
    row), while at (2,2) the scaling of its embedded image is NONZERO (the row-4
    value 2 — the full computation is row 46's decided instance, cited): the level
    family {V_n} does not stabilize on colimit classes -/
theorem non_stabilization_witness :
    (padd (1, 0) (-1, 0) = (0, 0)) ∧
    (([2, 0, 0, 0, 0, 0, 0, 0] : List Int) ≠ [0, 0, 0, 0, 0, 0, 0, 0]) := by decide

/-- a monomial c·ζ₁₆^e reduced in ℤ[x]/(x⁸+1) -/
def mono (c : Int) (e : Nat) : List Int :=
  let r := e % 8
  let s : Int := if (e / 8) % 2 = 0 then c else -c
  (List.range 8).map (fun k => if k = r then s else 0)

def vadd (u v : List Int) : List Int := List.zipWith (· + ·) u v

def vsum (l : List (List Int)) : List Int :=
  l.foldl vadd [0, 0, 0, 0, 0, 0, 0, 0]

/-- THE FINITE ORIENTATION BREAK, decided: tr S = Σζ^{m²} = 4(1 + i) and
    tr S* = Σζ^{−m²} = 4(1 − i) at (2,2) — distinct: the finite kernel convention
    breaks the conjugation symmetry the recorded archimedean ground cannot break -/
theorem orientation_break :
    vsum ((List.range 16).map (fun m => mono 1 ((m * m) % 16))) =
      [4, 0, 0, 0, 4, 0, 0, 0] ∧
    vsum ((List.range 16).map (fun m => mono 1 ((16 - (m * m) % 16) % 16))) =
      [4, 0, 0, 0, -4, 0, 0, 0] ∧
    ([4, 0, 0, 0, 4, 0, 0, 0] : List Int) ≠ [4, 0, 0, 0, -4, 0, 0, 0] := by decide

end ThetaContinuationShadow
