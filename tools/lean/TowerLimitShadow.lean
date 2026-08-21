/-
  THE TOWER-LIMIT CONSTRUCTION'S DECIDED CORE · TowerLimitShadow.lean
  ====================================================================

  Ferry 2026-08-21 (b65, the tower-limit construction act). Vanilla Lean 4 (v4.29.1
  pinned), no imports; expected profile per terminal: "does not depend on any axioms".

  THE CONSTRUCTION (the b65 registration, longhand): the embedding is MONOMIAL on the
  g-basis — ι(g_{a,t}) = g⁺_{pa,pt} — and the normalized transform intertwines exactly,
  M⁺∘ι = ι∘M, on all of Son (S⁺∘ι = p·ι∘S). The algebraic colimit is therefore the
  g-span over the limit grid (classes (a,t) ~ (pa,pt), i.e. p-power-denominator
  fraction pairs), the four sectors are ι-stable on the nose, and every finite-side
  deliverable lives on the algebraic colimit — the completion is never leaned on (it
  stays at the row-21 interface declaration, untouched).

  Decided here, at the smallest instance and in exact arithmetic:
  · the monomial embedding instance ι(g_{1,1}) = g⁺_{2,2} (the fiber-constancy of the
    embedded coefficient is the content: 8·(b mod 2) ≡ 8·b mod 16);
  · the intertwining instance S⁺(g⁺_{2,2}) = 4i·g⁺_{2,2} (= p·ι(S g_{1,1}));
  · the limit-grid fraction constancy a/q = pa/q⁺ and the eighth-root exponent
    constancy N/8 ↦ p²·N/8 = N⁺/8 (the boundary phase ζ₈'s level-independence);
  · the register arithmetic: the norm transport q⁺ = p·q (the p-register's constant
    class norms) and the p²-register's collapse (2ⁿ < 4ⁿ).
  Bank: relay data/b65_tower_limit.txt.
-/

namespace TowerLimitShadow

/-- a monomial c·ζ₁₆^e reduced in ℤ[x]/(x⁸+1), as a length-8 coordinate list -/
def mono (c : Int) (e : Nat) : List Int :=
  let r := e % 8
  let s : Int := if (e / 8) % 2 = 0 then c else -c
  (List.range 8).map (fun k => if k = r then s else 0)

/-- coordinatewise sum -/
def vadd (u v : List Int) : List Int := List.zipWith (· + ·) u v

def zrow : List Int := [0, 0, 0, 0, 0, 0, 0, 0]

/-- the ι-image of g_{1,1} by the embedding rule (the level-1 coefficient exponent 2b,
    b = b″ mod 2, embedded by p² = 4) -/
def iotaRow (m : Nat) : List Int :=
  if m % 4 = 2 then mono 1 (8 * ((m - 2) / 4 % 2)) else zrow

/-- g⁺_{2,2} at (2,2) by its own formula (coefficient exponent q·t·b = 8b″) -/
def gPlusRow (m : Nat) : List Int :=
  if m % 4 = 2 then mono 1 (8 * ((m - 2) / 4)) else zrow

/-- THE MONOMIAL EMBEDDING INSTANCE, decided: ι(g_{1,1}) = g⁺_{2,2} — the embedded
    coefficient is constant on each j-fiber (8·(b mod 2) ≡ 8·b mod 16), which is
    exactly the (L1) law's content at the smallest instance -/
theorem embedding_instance :
    (List.range 16).map iotaRow = (List.range 16).map gPlusRow := by decide

/-- one transform row on g⁺_{2,2}: (S v)(m′) = ζ^{2m′} − ζ^{6m′} + ζ^{10m′} − ζ^{14m′} -/
def sRow (mp : Nat) : List Int :=
  vadd (mono 1 (2 * mp)) (vadd (mono (-1) (6 * mp))
    (vadd (mono 1 (10 * mp)) (mono (-1) (14 * mp))))

/-- THE INTERTWINING INSTANCE, decided: S⁺ g⁺_{2,2} = 4i·g⁺_{2,2} — the (L2) law
    S⁺∘ι = p·ι∘S at the smallest instance (ι(S g_{1,1}) = 2i·g⁺_{2,2}, and p = 2) -/
theorem intertwining_instance :
    (List.range 16).map sRow =
    (List.range 16).map (fun m =>
      if m % 4 = 2 then mono 4 (4 + 8 * ((m - 2) / 4)) else zrow) := by decide

/-- THE CONSTANCIES, decided: the limit-grid fraction a/q = pa/q⁺ (as a·q⁺ = pa·q, the
    banked place-2 instances) and the eighth-root exponent N/8 ↦ p²·N/8 = N⁺/8 across
    the banked levels — the boundary phase ζ₈ is level-independent in exact exponent
    arithmetic -/
theorem constancy_instances :
    (1 * 4 = 2 * 2 ∧ 1 * 8 = 2 * 4 ∧ 3 * 8 = 6 * 4 ∧ 5 * 16 = 10 * 8) ∧
    ((16 / 8) * 4 = 64 / 8 ∧ (64 / 8) * 4 = 256 / 8) := by decide

/-- THE REGISTER ARITHMETIC, decided: the norm transport q⁺ = p·q at the instance (the
    p-register's class norms constant, q/pⁿ = 1 at the place 2), and the p²-register's
    collapse on the same pairing (2ⁿ < 4ⁿ at the banked levels) -/
theorem register_arithmetic :
    (4 = 2 * 2 ∧ 2 / 2 = 1 ∧ 4 / 4 = 1 ∧ 8 / 8 = 1 ∧ 16 / 16 = 1) ∧
    (2 ^ 1 < 4 ^ 1 ∧ 2 ^ 2 < 4 ^ 2 ∧ 2 ^ 3 < 4 ^ 3 ∧ 2 ^ 4 < 4 ^ 4) := by decide

end TowerLimitShadow
