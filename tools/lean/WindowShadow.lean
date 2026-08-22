/-
  THE WINDOW EXISTENCE ACT'S DECIDED CORE · WindowShadow.lean
  ============================================================

  Ferry 2026-08-21 (b79). Vanilla Lean 4 (v4.29.1 pinned), no imports; expected
  profile per terminal: "does not depend on any axioms".

  Closure-sequence step three's finite decidable core (the firewall's first
  computing act — the archimedean readings are BENCH at their declared pin and
  live in the instrument and bank, NOT here; this module holds only the derived
  finite anchors). P-C: the truncated line is the i-sector excess — row 47's
  identity 4·d_i = (q−1)² + 3 with the excess on the +i side and the even sides
  balanced, at the four banked place-2 cells. P-A: the excess/seed row's shell
  address is the ball-boundary/deficient address v = n−1 (the gcd law) at every
  banked truncation — the address the model's deficient weight occupies (b61,
  decided there). The gauge pair: the plus-gauge class value and its conjugate
  are distinct and conjugation-swapped — the arithmetic shadow of the relative
  conjugacy; the conditional reading [UNDER H-COH-∞] lives in the bank and
  report, never in this kernel.
  Bank: relay data/b79_window_existence.txt.
-/

namespace WindowShadow

/-- P-C, DERIVED: the i-sector excess at the four banked place-2 cells — the
    banked tuples satisfy 4·d_i = (q−1)² + 3, the excess sits on the +i side
    (d_i − d_{−i} = 1), and the even sides are balanced (d₁ = d₋₁ with
    4·d₁ = q(q−2)) -/
theorem excess_sector_instances :
    (4*1 = 1*1 + 3 ∧ 1 = 0 + 1 ∧ (0 : Nat) = 0 ∧ 4*0 = 2*0) ∧
    (4*3 = 3*3 + 3 ∧ 3 = 2 + 1 ∧ (2 : Nat) = 2 ∧ 4*2 = 4*2) ∧
    (4*13 = 7*7 + 3 ∧ 13 = 12 + 1 ∧ (12 : Nat) = 12 ∧ 4*12 = 8*6) ∧
    (4*57 = 15*15 + 3 ∧ 57 = 56 + 1 ∧ (56 : Nat) = 56 ∧ 4*56 = 16*14) := by
  decide

/-- P-A, DERIVED: the excess/seed row's shell address is v = n−1 at every
    banked place-2 truncation — gcd(2ⁿ⁻¹, 2ⁿ) = 2ⁿ⁻¹, the ball-boundary
    transition and the model's deficient address (rows 54, 41) -/
theorem line_address_instances :
    Nat.gcd 1 2 = 1 ∧ Nat.gcd 2 4 = 2 ∧ Nat.gcd 4 8 = 4 ∧ Nat.gcd 8 16 = 8 ∧
    ((List.range 4).filter (fun m =>
        decide (Nat.gcd m 4 < 2) &&
        (decide (2 ≤ Nat.gcd ((2*m) % 4) 4) || decide ((2*m) % 4 = 0))) =
      (List.range 4).filter (fun m => decide (Nat.gcd m 4 = 1))) ∧
    ((List.range 16).filter (fun m =>
        decide (Nat.gcd m 16 < 4) &&
        (decide (4 ≤ Nat.gcd ((2*m) % 16) 16) || decide ((2*m) % 16 = 0))) =
      (List.range 16).filter (fun m => decide (Nat.gcd m 16 = 2))) := by decide

def pconj (u : Int × Int) : Int × Int := (u.1, -u.2)

/-- The gauge pair, DERIVED arithmetic: the plus-gauge class value (0,1) = +i
    and its conjugate (0,−1) = −i are distinct and conjugation-swapped — the
    finite shadow of the relative conjugacy (the conditional reading carries
    its tag in the bank and report, not here) -/
theorem gauge_reading_pair :
    pconj (0, 1) = ((0, -1) : Int × Int) ∧
    pconj (0, -1) = ((0, 1) : Int × Int) ∧
    ((0, 1) : Int × Int) ≠ (0, -1) := by decide

end WindowShadow
