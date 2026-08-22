/-
  THE EPSILON INVENTORY ACT'S DECIDED CORE · DeterminationShadow.lean
  ====================================================================

  Ferry 2026-08-22 (b87). Vanilla Lean 4 (v4.29.1 pinned), no imports; expected
  profile per terminal: "does not depend on any axioms".

  THE DETERMINATION LEMMA (the lemma discipline on its face: the conclusion is
  UNIQUENESS-ON-RECORDED-DATA, NEVER EXISTENCE): any two objects satisfying the
  constructor's gates AG-1 through AG-3 agree on all recorded data, because the
  gates pin the object's values on the recorded coverage. The general form —
  two functions each agreeing with one spec on a coverage agree with each other
  there — holds for any types with no algebraic hypotheses. The banked-coverage
  instance: the eight banked cells with N = q² (decided) are the recorded
  coverage, and the specialization to that coverage is the campaign's
  restatement: THE GATES DEFINE THE OBJECT; THE BUILD DECIDES NON-EMPTINESS;
  EXISTENCE IS THE SOLE ANALYTIC QUESTION.
  Bank: relay data/b87_epsilon_inventory.txt.
-/

namespace DeterminationShadow

/-- THE DETERMINATION LEMMA, general: two functions each agreeing with one
    spec on a coverage agree with each other on that coverage — any types, no
    algebraic hypotheses; uniqueness on the coverage, never existence -/
theorem determination {A V : Type} (f g spec : A → V) (covered : A → Bool)
    (hf : ∀ a, covered a = true → f a = spec a)
    (hg : ∀ a, covered a = true → g a = spec a) :
    ∀ a, covered a = true → f a = g a := by
  intro a h
  rw [hf a h, hg a h]

/-- the recorded coverage: the eight banked levels -/
def bankedN (N : Nat) : Bool :=
  decide (N = 4) || decide (N = 9) || decide (N = 16) || decide (N = 25) ||
  decide (N = 64) || decide (N = 81) || decide (N = 256) || decide (N = 729)

/-- the banked coverage's arithmetic: every banked level is a square, N = q²,
    with q the banked boundary value (the cusp datum's table) — decided -/
theorem banked_coverage_instance :
    (2*2 = 4 ∧ 3*3 = 9 ∧ 4*4 = 16 ∧ 5*5 = 25 ∧
     8*8 = 64 ∧ 9*9 = 81 ∧ 16*16 = 256 ∧ 27*27 = 729) ∧
    (bankedN 4 = true ∧ bankedN 9 = true ∧ bankedN 16 = true ∧
     bankedN 25 = true ∧ bankedN 64 = true ∧ bankedN 81 = true ∧
     bankedN 256 = true ∧ bankedN 729 = true ∧ bankedN 5 = false) := by decide

/-- THE DETERMINATION AT THE BANKED COVERAGE: any two objects whose recorded
    data agree with one spec at every banked level (the AG-1/AG-2/AG-3 pinning)
    agree with each other at every banked level — uniqueness on recorded data;
    the build decides non-emptiness; existence is the sole analytic question -/
theorem determination_at_banked {V : Type} (f g spec : Nat → V)
    (hf : ∀ N, bankedN N = true → f N = spec N)
    (hg : ∀ N, bankedN N = true → g N = spec N) :
    ∀ N, bankedN N = true → f N = g N :=
  determination f g spec bankedN hf hg

end DeterminationShadow
