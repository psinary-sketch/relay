/-
  THE METAPLECTIC SQUARE-ROOT CHECK · MetaplecticRootShadow.lean
  ===============================================================

  Ferry 2026-08-21 (b59, component 3). Vanilla Lean 4 (v4.29.1 pinned), no imports;
  expected profile per terminal: "does not depend on any axioms".

  THE QUESTION (the metaplectic companion wonder's first hard datum): at the banked
  cell (2,2), does an operator W on the chart exist with W² = M and W⁴ = −1?

  THE CONSTRAINT (derived in the b59 registration): W² = M forces W⁴ = M² = Π (the
  parity; S² = q²Π banked), so W⁴ = −1 forces Π = −1 on the whole chart — and the
  chart's parity-even sector obstructs. ONE witness decides it: the u-line
  (u = 1_{qℤ}, the b57 longhand) has S u = 4u (decided below in ℤ[ζ₁₆] coordinates,
  all 16 rows), so M u = u; parity fixes u and u ≠ −u (decided). The abstract
  obstruction lemma then closes BRANCH (b): NO such W exists on the chart — the
  spectral constraint that fails is the parity constraint, witnessed on the
  parity-even sector. The −1-fourth-power condition HOLDS exactly on the twisted
  ±i sectors (M² = −1 there; row 33's compiled tower witness M(ιu) = i·ιu): the C₈
  frame lives on the twisted sectors only — the frame boundary is the parity split.
-/

namespace MetaplecticRootShadow

/-- a monomial c·ζ₁₆^e reduced in ℤ[x]/(x⁸+1), as a length-8 coordinate list -/
def mono (c : Int) (e : Nat) : List Int :=
  let r := e % 8
  let s : Int := if (e / 8) % 2 = 0 then c else -c
  (List.range 8).map (fun k => if k = r then s else 0)

/-- coordinatewise sum -/
def vadd (u v : List Int) : List Int := List.zipWith (· + ·) u v

/-- the row-m′ value of S applied to the ball indicator u = Σ_b δ_{4b}:
    Σ_b ζ^{4·b·m′} -/
def gaussRow (mp : Nat) : List Int :=
  vadd (mono 1 0) (vadd (mono 1 (4 * mp)) (vadd (mono 1 (8 * mp)) (mono 1 (12 * mp))))

/-- THE u-LINE IS AN EXACT +1-EIGENVECTOR: S u = 4·u at (2,2) — every one of the 16
    coordinate rows decided in ℤ[ζ₁₆] (the geometric sum collapses to 4 on the ball
    rows and to 0 off them), hence M u = u with M = S/4 -/
theorem u_gauss_eigen :
    (List.range 16).map gaussRow =
    (List.range 16).map (fun mp =>
      if mp % 4 = 0 then ([4, 0, 0, 0, 0, 0, 0, 0] : List Int)
      else [0, 0, 0, 0, 0, 0, 0, 0]) := by decide

/-- the u-line's entry list at (2,2): the indicator of the ball {0, 4, 8, 12} -/
def uList : List Int := [1,0,0,0, 1,0,0,0, 1,0,0,0, 1,0,0,0]

/-- own list indexing (no core-lemma dependence) -/
def nth : List Int → Nat → Int
  | [], _ => 0
  | a :: _, 0 => a
  | _ :: l, n + 1 => nth l n

/-- PARITY FIXES u AND u ≠ −u: the parity permutation m ↦ −m mod 16 preserves the
    ball indicator, and the indicator differs from its negation — the two decided
    facts the obstruction needs -/
theorem parity_and_sign :
    ((List.range 16).map (fun m => nth uList ((16 - m) % 16)) = uList) ∧
    uList ≠ uList.map (fun c => -c) := by decide

/-- THE SQUARE-ROOT OBSTRUCTION, abstract: if W² fixes u (the decided M u = u
    instance) and W⁴ sends u to −u (the −1 fourth-power condition) while −u ≠ u
    (decided), there is no such W — branch (b), the parity constraint named -/
theorem square_root_obstruction {V : Type} (w : V → V) (neg : V → V) (u : V)
    (h2 : w (w u) = u) (h4 : w (w (w (w u))) = neg u) (hne : neg u ≠ u) : False :=
  hne (h4.symm.trans ((congrArg (fun x => w (w x)) h2).trans h2))

end MetaplecticRootShadow
