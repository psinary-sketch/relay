/-
  THE MONOTONICITY ACT'S DECIDED CORE · TowerMonotoneShadow.lean
  ===============================================================

  Ferry 2026-08-22 (b101). Vanilla Lean 4 (v4.29.1 pinned), no imports; expected
  profile per terminal: "does not depend on any axioms".

  THE CONCRETE HALF OF THE SENSE DEBT: is the programme's level family MONOTONE
  as a family of subspaces? The two sides of the Sonin condition, transported
  along the recorded embedding ι (the chart refinement m″ = p·m + p^{2n+1}·j,
  values copied), reduce to index arithmetic, decided here at the banked
  truncation pairs (2,1)→(2,2), (2,2)→(2,3) and (3,1)→(3,2):

  · `ball_pullback` (the support side): an image index lies in the level-(n+1)
    ball exactly when its source lies in the level-n ball — so ι of a
    ball-vanishing vector is ball-vanishing.
  · `inner_sum_rule`: on a level-(n+1) ball row every j-term of the embedding's
    inner sum is 1 (the exponent folds to 0), so that sum is p, not 0.
  · `transform_index_shift`: the transform exponent transports under the scale
    map, (r·p·m) mod N_{n+1} = p²·(((r/p)·m) mod N_n) — N_{n+1} = p²·N_n, which
    is why the factor is p² (the run-registration's prose said p; the
    instrument caught it before any Lean was written, and the corrected form is
    the one decided here).
  · `quotient_in_ball`: a level-(n+1) ball row's index divided by p lands in the
    level-n ball — where the level-n transform vanishes.

  Together: ι(Son(p,n)) ⊆ Son(p,n+1) at the banked pairs — THE FAMILY IS
  MONOTONE. (b70's decided witness V_{n+1}∘ι ≠ ι∘V_n is a statement about the
  OPERATORS and is untouched by this: operator incompatibility and subspace
  monotonicity are different statements, and only the second is what the
  compression lemma's hypothesis asks for.)
  Bank: relay data/b101_monotonicity.txt.
-/

set_option maxRecDepth 8192

namespace TowerMonotoneShadow

/-- the banked truncation pairs as (p, n): the pair is level n → level n+1 -/
def pairs : List (Nat × Nat) := [(2, 1), (2, 2), (3, 1)]

def Nlev (p n : Nat) : Nat := p ^ (2 * n)
def Nlev1 (p n : Nat) : Nat := p ^ (2 * n + 2)
def ballMod (p n : Nat) : Nat := p ^ n
def ballMod1 (p n : Nat) : Nat := p ^ (n + 1)
def step (p n : Nat) : Nat := p ^ (2 * n + 1)

/-- the level-(n+1) ball rows -/
def ballRows (p n : Nat) : List Nat :=
  (List.range (Nlev1 p n)).filter (fun r => decide (r % ballMod1 p n = 0))

/-- THE SUPPORT SIDE: an image index `p·m + step·j` lies in the level-(n+1) ball
    exactly when `m` lies in the level-n ball — so ι carries ball-vanishing
    vectors to ball-vanishing vectors -/
theorem ball_pullback :
    pairs.all (fun pn =>
      let p := pn.1; let n := pn.2;
      (List.range (Nlev p n)).all (fun m =>
        (List.range p).all (fun j =>
          decide (((p * m + step p n * j) % Nlev1 p n) % ballMod1 p n = 0)
            == decide (m % ballMod p n = 0)))) = true := by decide

/-- THE INNER-SUM RULE: on every level-(n+1) ball row the embedding's j-exponent
    folds to zero, so each of the p terms is 1 and the inner sum is p -/
theorem inner_sum_rule :
    pairs.all (fun pn =>
      let p := pn.1; let n := pn.2;
      (ballRows p n).all (fun r => decide ((r * step p n) % Nlev1 p n = 0)))
    = true := by decide

/-- THE TRANSFORM INDEX SHIFT: the exponent transports under the scale map,
    with factor p² because N_{n+1} = p²·N_n -/
theorem transform_index_shift :
    pairs.all (fun pn =>
      let p := pn.1; let n := pn.2;
      (ballRows p n).all (fun r =>
        (List.range (Nlev p n)).all (fun m =>
          decide ((r * p * m) % Nlev1 p n
                  = p ^ 2 * (((r / p) * m) % Nlev p n))))) = true := by decide

/-- THE QUOTIENT LANDS IN THE BALL: a level-(n+1) ball row divided by p is a
    level-n ball row — where the level-n transform vanishes -/
theorem quotient_in_ball :
    pairs.all (fun pn =>
      let p := pn.1; let n := pn.2;
      (ballRows p n).all (fun r => decide ((r / p) % ballMod p n = 0)))
    = true := by decide

end TowerMonotoneShadow
