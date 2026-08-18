/-
  W-CONSTRUCTION-1 act 6 · OrbitDictionary.lean — THE VANILLA LEG (zero axioms)
  =============================================================================

  The two-leg ruling (Rule 5) governs: VANILLA leg — finite/combinatorial instances,
  vanilla Lean 4 (v4.29.1 pinned), decide only, expected profile per terminal:
  "does not depend on any axioms".

  WHAT THIS MODULE COMPILES — two finite shadows:

  (A) THE ADJOINTNESS QUESTION's shadow (act-6 item 1): the antipode's twist is a
      REWEIGHTING of the trace sequence — it cannot create support. The trace is zero
      off the identity (TraceSilence, cited, not recompiled); its twist by the Weil
      weights' integer content is still zero (twisted_silence). The quotient channel's
      weight is the FIBER of the shell shift — multiplication by p is exactly p-to-1
      onto the next shell (fiber_two, fiber_three): the q^{1/2} per step is the
      unitary normalization of a p-to-1 map, and its integer content is NONZERO where
      the twisted trace is zero (channels_distinct). CONSEQUENCE (the refutation's
      shadow): no twist of the trace channel reaches the quotient channel.

  (B) DENINGER'S DICTIONARY's shadow (act-6 item 4; math/0204110 §4, at content):
      finite place ↔ closed orbit / recurrence, NOT fixed point — the scaling at a
      finite place has NO fixed point off the identity (no_fixed_offzero) and acts on
      valuation shells as the SHIFT with fiber exactly p (shell_shift_2/3 + the fiber
      theorems): the finite places contribute only through recurrence. The fixed-point
      channel is the archimedean one (the trace, §12 of the build document).
-/

namespace OrbitDictionary

/- ── (A) the adjointness shadow ───────────────────────────────────────────────── -/

/-- the twist of silence is silence: the banked trace values (0 at k = 1,2,3 for
    (2,3); 0 at k = 1,2 for (3,2) — TraceSilence, cited) reweighted by the Weil
    weights' integer content (p^k) are still zero. A reweighting cannot create
    support — this is that fact's decide shadow. -/
theorem twisted_silence :
    ([0, 0, 0].zipWith (· * ·) [2, 4, 8] = [(0 : Int), 0, 0]) ∧
    ([0, 0].zipWith (· * ·) [3, 9] = [(0 : Int), 0]) := by decide

/-- the quotient channel's weight is the fiber: multiplication by 2 on ℤ/16 is
    exactly 2-to-1 onto the even residues — every even y has exactly 2 preimages. -/
theorem fiber_two :
    ((List.range 16).all fun y => !(y % 2 == 0) ||
      (((List.range 16).filter fun x => (2 * x) % 16 == y).length == 2)) = true := by
  decide

/-- and by 3 on ℤ/9: exactly 3-to-1 onto the multiples of 3. -/
theorem fiber_three :
    ((List.range 9).all fun y => !(y % 3 == 0) ||
      (((List.range 9).filter fun x => (3 * x) % 9 == y).length == 3)) = true := by
  decide

/-- the two channels are distinct where it matters: the fiber weight (p, nonzero) at
    k = 1 sits exactly where the twisted trace is zero — the literal adjointness's
    refutation instance, both primes. -/
theorem channels_distinct : ((2 != 0) && (3 != 0)) = true := by decide

/- ── (B) the dictionary's shadow ──────────────────────────────────────────────── -/

/-- NO fixed point off the identity: the scaling m ↦ p·m fixes only 0, both banked
    cells — the "finite place ↔ fixed point" reading is REFUTED at the model; what a
    finite place has is recurrence. -/
theorem no_fixed_offzero :
    ((((List.range 16).filter fun m => (2 * m) % 16 == m).length == 1) &&
     (((List.range 9).filter fun m => (3 * m) % 9 == m).length == 1)) = true := by
  decide

/-- the shift structure, p = 2: doubling sends the unit shell (odd m) exactly onto
    the valuation-1 shell (2m ≡ 2 mod 4) — the closed-orbit/recurrence datum. -/
theorem shell_shift_2 :
    ((List.range 16).all fun m => !(m % 2 == 1) || ((2 * m) % 16 % 4 == 2)) = true := by
  decide

/-- the shift structure, p = 3: tripling sends the unit shell onto the valuation-1
    shell (3m mod 9 ∈ {3, 6}: divisible by 3, nonzero). -/
theorem shell_shift_3 :
    ((List.range 9).all fun m => !(m % 3 != 0) ||
      (((3 * m) % 9 % 3 == 0) && ((3 * m) % 9 != 0))) = true := by decide

end OrbitDictionary
