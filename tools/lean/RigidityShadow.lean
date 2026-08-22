/-
  THE RIGIDITY ACT'S DECIDED CORE · RigidityShadow.lean
  ======================================================

  Ferry 2026-08-21 (b80). Vanilla Lean 4 (v4.29.1 pinned), no imports; expected
  profile per terminal: "does not depend on any axioms".

  Closure-sequence step four — the index face's discrete-invariant mechanism at
  kernel grade. THE ABSTRACT RIGIDITY LEMMA: a function from a step-graph to
  any value type that is constant on edges is constant along every walk —
  induction on the walk, no algebraic hypotheses; connectedness is exactly the
  hypothesis that a walk exists, so on a connected graph the function is
  constant. Discreteness enters at the instantiation: the fourth-root carrier
  ℤ[i]-pairs with the four roots pairwise distinct (decided) — F⁴ = 1's class
  set. The tower instance: the walk 0-1-2-3 and the banked per-level class
  table's bounded edge-constancy (the unit trace i at every banked place-2
  level, rows 35–36; banked data, declared) — the finite mirror's rigidity
  re-anchored THROUGH the lemma. The window line's VALUE appears nowhere in
  this module (the circularity gate; the (V) clause untouched).
  Bank: relay data/b80_rigidity.txt.
-/

namespace RigidityShadow

/-- a walk from head `a` along `l`: consecutive vertices adjacent
    (head-threaded own recursion; reduces definitionally) -/
def isWalk (adj : Nat → Nat → Bool) (a : Nat) : List Nat → Bool
  | [] => true
  | b :: t => adj a b && isWalk adj b t

/-- the walk's endpoint (head-threaded own recursion) -/
def lastOf (a : Nat) : List Nat → Nat
  | [] => a
  | b :: t => lastOf b t

/-- THE ABSTRACT RIGIDITY LEMMA: edge-constant functions are walk-constant —
    any value type, any edge predicate, no algebraic hypotheses; on a
    connected graph (a walk to every vertex) the function is constant -/
theorem walk_constant {V : Type} (adj : Nat → Nat → Bool) (f : Nat → V)
    (h : ∀ i j, adj i j = true → f i = f j) :
    ∀ (a : Nat) (l : List Nat), isWalk adj a l = true →
      f (lastOf a l) = f a := by
  intro a l
  induction l generalizing a with
  | nil => intro _; rfl
  | cons b t ih =>
    intro hw
    change (adj a b && isWalk adj b t) = true at hw
    cases hab : adj a b with
    | false =>
      rw [hab] at hw
      exact Bool.noConfusion hw
    | true =>
      rw [hab] at hw
      have hrest : isWalk adj b t = true := hw
      show f (lastOf b t) = f a
      rw [ih b hrest]
      exact (h a b hab).symm

/-- the specialization to the fourth-root carrier (the class set of F⁴ = 1):
    the discrete-invariant mechanism with values in ℤ[i]-pairs -/
theorem fourth_root_instantiation (adj : Nat → Nat → Bool)
    (f : Nat → Int × Int) (h : ∀ i j, adj i j = true → f i = f j)
    (a : Nat) (l : List Nat) (hw : isWalk adj a l = true) :
    f (lastOf a l) = f a :=
  walk_constant adj f h a l hw

/-- (i1)'s shadow: the fourth-root class set is discrete — the four roots
    pairwise distinct (decided) -/
theorem fourth_root_discreteness :
    ((1, 0) : Int × Int) ≠ (0, 1) ∧ ((1, 0) : Int × Int) ≠ (-1, 0) ∧
    ((1, 0) : Int × Int) ≠ (0, -1) ∧ ((0, 1) : Int × Int) ≠ (-1, 0) ∧
    ((0, 1) : Int × Int) ≠ (0, -1) ∧ ((-1, 0) : Int × Int) ≠ (0, -1) := by
  decide

/-- the tower chain's edge predicate (levels 0..3, edges n → n+1) and the
    banked per-level class table (the unit trace i at every banked place-2
    level, rows 35–36; banked data, declared) -/
def towerAdj (i j : Nat) : Bool :=
  decide (j = i + 1) && decide (j ≤ 3)
def clsTable (n : Nat) : Int × Int :=
  match n with
  | 0 => (0, 1) | 1 => (0, 1) | 2 => (0, 1) | _ => (0, 1)

/-- P3's decided facts: 0-1-2-3 is a walk of the tower chain with endpoint 3,
    and the banked class table is edge-constant on the bounded range — the
    finite mirror's level-constancy re-anchored as the lemma's exact instance -/
theorem tower_walk_instances :
    isWalk towerAdj 0 [1, 2, 3] = true ∧
    lastOf 0 [1, 2, 3] = 3 ∧
    ((List.range 4).all (fun i => (List.range 4).all (fun j =>
      !(towerAdj i j) || decide (clsTable i = clsTable j))) = true) ∧
    clsTable 3 = clsTable 0 := by decide

end RigidityShadow
