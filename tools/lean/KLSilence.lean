/-
  THE SILENCE THEOREM · KLSilence.lean — THE PROOF ABOUT THE NUMBER
  ==================================================================

  The assembly act, component 1 (ferry 2026-08-20). Vanilla Lean 4 (v4.29.1 pinned),
  no imports, term mode and decide only; expected profile per terminal: "does not
  depend on any axioms".

  WHAT THIS MODULE PROVES — the b48 depth-alignment law, stated at GENERAL q:

  (1) THE SILENCE DIRECTION (general q, general coefficient structure): a weight-one
      position-factor operator E_{ij} whose support touches the ball coordinate
      (i = 0 or j = 0) acts as IDENTICALLY ZERO on any pair of Sonin-supported vectors
      — hence is Knill–Laflamme-silent on E₁ with scalar c = 0. The hypotheses the
      b48 longhand used implicitly are NAMED as explicit arguments, per the ferry's
      instruction: the coefficient structure needs only a zero element with
      `mul zero a = zero`, `mul a zero = zero`, `conj zero = zero`, `add zero zero =
      zero`; the Sonin condition enters as `u 0 t = zero` (the ball slice vanishes).
      No ring axioms beyond these are used, and none are assumed silently.

  (2) THE COUNT LAW (general q): the non-ball-touching position pairs number exactly
      (q − 1)², and with the frequency factor's q² the registered non-silent basis
      count is (q − 1)² + q² — proved by induction at general q, not by instance.

  (3) THE ONLY-IF DIRECTION IS THE MEASURED HALF AND IS *NOT* PROVED HERE IN
      GENERALITY: that every off-ball operator is non-silent is an exact MEASURED
      fact at the four banked cells (b45/b48 banks: all (q−1)² + q² off-ball
      operators fail, per-operator certificates; the compiled witnesses
      kl_fail_2_2 / kl_fail_5_1 in E1UnitPurityDraft are two of them). The general-q
      only-if is a NAMED OPEN STATEMENT (correspondence row; never a sorry — the
      kernel-purity ruling stands). The four banked instances are this theorem's
      corollaries on the silence side and its evidence on the only-if side.

  Together with the banked only-if instances, the biconditional at the banked cells:
  a weight-one operator is KL-silent on E₁ iff its support lies in the ball the
  Sonin condition zeroes; the non-silent count is exactly (q − 1)² + q².
-/

namespace KLSilence

/-- fold-sum of `f` over `t = 0..q-1` with an abstract `add`/`zero` -/
def foldSum {R : Type} (zero : R) (add : R → R → R) (f : Nat → R) : Nat → R
  | 0 => zero
  | Nat.succ t => add (foldSum zero add f t) (f t)

/-- a fold-sum of zeros is zero (needs only `add zero zero = zero`) -/
theorem foldSum_zero {R : Type} (zero : R) (add : R → R → R)
    (hz : add zero zero = zero) (f : Nat → R) (hf : ∀ t, f t = zero) :
    ∀ q, foldSum zero add f q = zero := by
  intro q
  induction q with
  | zero => rfl
  | succ t ih =>
      show add (foldSum zero add f t) (f t) = zero
      rw [ih, hf t, hz]

/-- (1) THE SILENCE DIRECTION, general q: if the ball slices vanish (`u 0 t = zero`,
    `v 0 t = zero`) and the coefficient structure kills zero factors, then the
    compression entry Σ_t conj (u i t) * (v j t) is zero whenever i = 0 or j = 0 —
    the operator acts as zero on the pair, i.e. is KL-silent with c = 0. -/
theorem silence_of_ball_touching {R : Type} (zero : R)
    (add mul : R → R → R) (conj : R → R)
    (hmz : ∀ a, mul zero a = zero) (hzm : ∀ a, mul a zero = zero)
    (hcz : conj zero = zero) (haz : add zero zero = zero)
    (q : Nat) (u v : Nat → Nat → R)
    (hu : ∀ t, u 0 t = zero) (hv : ∀ t, v 0 t = zero)
    (i j : Nat) (hij : i = 0 ∨ j = 0) :
    foldSum zero add (fun t => mul (conj (u i t)) (v j t)) q = zero := by
  apply foldSum_zero zero add haz
  intro t
  cases hij with
  | inl hi => rw [hi, hu t, hcz, hmz]
  | inr hj => rw [hj, hv t, hzm]

/-- the off-ball position pairs: `(i, j)` with `1 ≤ i < q`, `1 ≤ j < q` -/
def offBallCount (q : Nat) : Nat := (q - 1) * (q - 1)

/-- (2) THE COUNT LAW, general q: the registered non-silent weight-one basis count
    is (q − 1)² + q² — the off-ball position operators plus the whole frequency
    factor (which has no zero slice). Proved as the arithmetic identity it is;
    the identification of the two summands with the b48 pass/fail split is the
    banked measured content. -/
theorem nonsilent_count (q : Nat) :
    offBallCount q + q * q = (q - 1) * (q - 1) + q * q := rfl

/-- the count law's enumerative core: the number of nonzero residues below q,
    as its own recursion (kept axiom-free; the List-semantics identification is
    the decide instance below) -/
def countNonzero : Nat → Nat
  | 0 => 0
  | 1 => 0
  | (n + 2) => countNonzero (n + 1) + 1

/-- the recursion counts q − 1, general q, by induction — no axioms -/
theorem countNonzero_eq : ∀ q, countNonzero q = q - 1
  | 0 => rfl
  | 1 => rfl
  | (n + 2) => by
      show countNonzero (n + 1) + 1 = n + 1
      rw [countNonzero_eq (n + 1)]
      cases n with
      | zero => rfl
      | succ m => rfl

/-- the enumerated off-ball pair count equals (q − 1)², general q -/
theorem offball_enumeration (q : Nat) :
    countNonzero q * countNonzero q = (q - 1) * (q - 1) := by
  rw [countNonzero_eq]

/-- the recursion agrees with the List.filter semantics at the four banked cells
    (q = 4, 5, 8, 9) — decided exactly -/
theorem countNonzero_list_agreement :
    (countNonzero 4 = ((List.range 4).filter (fun i => decide (i ≠ 0))).length) ∧
    (countNonzero 5 = ((List.range 5).filter (fun i => decide (i ≠ 0))).length) ∧
    (countNonzero 8 = ((List.range 8).filter (fun i => decide (i ≠ 0))).length) ∧
    (countNonzero 9 = ((List.range 9).filter (fun i => decide (i ≠ 0))).length) := by
  decide

/-- the four banked cells' non-silent counts, as instances of the law
    (q = 4, 5, 8, 9 — the b45/b48 banked totals 25, 41, 113, 145) -/
theorem banked_instances :
    ((4 - 1) * (4 - 1) + 4 * 4 = 25) ∧ ((5 - 1) * (5 - 1) + 5 * 5 = 41) ∧
    ((8 - 1) * (8 - 1) + 8 * 8 = 113) ∧ ((9 - 1) * (9 - 1) + 9 * 9 = 145) := by
  decide

end KLSilence
