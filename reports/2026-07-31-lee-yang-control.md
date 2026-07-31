# W-ORD-LEE-YANG-CONTROL — the h2 arc's second positive control — 2026-07-31

Analytical pass; no kernel commits, no rail edits (rail frozen at `11db565`, empty-diff check at close).
Read-first executed: THE_RESIDUE_OF_RH §§2/5/6 anatomy · SURROUND §6/§6a · the Face-D control's grammar
(`reports/2026-07-29-face-D-function-field.md`) · SPIRAL_MAP §Translation (the Lee–Yang row) · monograph
§27.3 register 5 (via the Face-D quotation, verbatim) · the two-darknesses rule (charter §4; OPEN_TRAILS
prism-search/no-prism distinction). Charter §5 checkpoint discipline: not triggered — no terminal touched;
this is a comparison, not a compile. PLACE-papers `3ab8a76` local = remote at open.

## The registered expectation (verbatim, before any analysis landed)

> *the shortfall re-lands on edge-vs-centre as SINGLE-INDEX vs PAIR-INDEX positivity — ζ's existing
> one-sign structure (Λ(n) ≥ 0) is single-index and reaches exactly the σ=1 edge (Hadamard–de la Vallée
> Poussin); the circle theorem's definiteness supplier is pair-index (J_ij ≥ 0 under Asano closure); the
> pair-index object ζ lacks is Q — the positive space on the zeros.*

**Outcome up front: CONFIRMED, at grade, with one honest sharpening** (the zero-margin note, §2 row 6):
the translation's two ABSENT rows are both pair-index objects; every EXISTS row on the ζ side is
single-index; and the single-index/pair-index split lands exactly on the residue paper's edge-vs-centre
anatomy. No surprise was found; the sharpening is that any hypothetical ζ-side supplier would have to be
boundary-tight, where the Ising supplier has slack.

## (1) The proved instance, stated precisely

**Setup.** n Ising spins σ_i ∈ {±1}; ferromagnetic pair couplings J_ij ≥ 0; uniform field h. The
partition function Z = Σ_σ exp(β Σ_{i<j} J_ij σ_i σ_j + βh Σ_i σ_i), written in the fugacity z = e^{−2βh},
is (up to a positive prefactor) a degree-n polynomial P(z) with positive coefficients, built from the
bond weights A_ij = e^{−2βJ_ij}; ferromagnetism J_ij ≥ 0 is exactly 0 < A_ij ≤ 1.

**The theorem (Lee–Yang 1952, part II).** All zeros of P lie on the unit circle |z| = 1.

**Where the definiteness enters.** In the all-one-sign PAIR-coupling condition, twice over:
- **Base case:** the two-spin bond polynomial p(z₁, z₂) = 1 + A(z₁ + z₂) + z₁z₂ has the Lee–Yang
  property (non-vanishing when |z₁|, |z₂| < 1) **precisely because |A| ≤ 1** — i.e. because the one bond
  is ferromagnetic. The definiteness supplier is a condition on a *pair*.
- **Closure:** **Asano contraction** (Asano 1970) glues bonds — it preserves the Lee–Yang property while
  identifying variables pairwise, assembling the many-body multi-affine polynomial from two-spin pieces;
  diagonal restriction yields P. The **modern reading (Borcea–Brändén 2009)**: the Lee–Yang property is a
  stability property, and the linear operators preserving it are completely characterized (the symbol
  criterion) — the circle theorem sits inside a classified stability-preserver calculus.

**What the positivity buys.** Line confinement **proved, not conjectured**: the zeros are confined to
|z| = 1, the fixed locus of z ↦ 1/z̄ — the involution induced by the spin-flip symmetry h ↔ −h, the model's
functional equation. In the angle variable z = e^{iθ}, confinement = reality of zeros.

**The mapping of registers, stated once.** Unit circle ↔ critical line via the FE-symmetric point: each
is the fixed locus of its functional-equation involution (z ↦ 1/z from spin flip; s ↦ 1−s from ξ's FE),
with z = 1 (h = 0) ↔ s = 1/2; in the angle/height variables (z = e^{iθ}; s = 1/2 + it) both statements
read "the zeros are real." Shared target class: **Laguerre–Pólya** — Ξ ∈ LP is RH's function-class form,
and the Ising P(e^{iθ}) is a finite LP instance.

## (2) The translation table, clause by clause

Grades: **EXISTS** / **EXISTS-WEAKER** / **ABSENT** — with ABSENT read under the two-darknesses rule: *no
such object is known / catalogued* (the prism-search posture), never "none exists."

| Lee–Yang ingredient | ζ counterpart | grade | notes / cites |
|:--|:--|:--|:--|
| Partition polynomial with positive coefficients — Z(z) = ∫ z^{N(σ)} dμ(σ), μ ≥ 0 | Riemann's Fourier representation: Ξ(t) = ∫ Φ(u) cos(ut) du with **Φ(u) > 0** (even, super-exponentially decaying) | **EXISTS** | Φ > 0 classical; this is Pólya's setting |
| The spin measure's **product structure** — μ = ⊗ᵢ μᵢ over sites, the many-body structure the couplings act on | Φ's measure is **one-variable**: a positive measure with no site decomposition | **EXISTS-WEAKER** | a positive measure exists; the multi-site structure the LY machinery acts on does not |
| **Ferromagnetic pair couplings J_ij ≥ 0 — the definiteness supplier** | **THE ABSENT OBJECT**: a Lee–Yang-class (ferromagnetic) representation of Ξ — Φ realized as the distribution of a Newman-class ferromagnetic system, which would confine the zeros by the LY machinery | **ABSENT** (as a known object) | Newman 1976 defines the class; no such representation of Ξ is known — a catalogued prism, tried and not supplied |
| Single-site / coefficient positivity (the z-coefficients of P are ≥ 0) | **Λ(n) ≥ 0** — the prime ledger's one-sign structure, **single-index** | **EXISTS** — and reaches **exactly the σ = 1 edge** (Hadamard–de la Vallée Poussin; the residue paper's compiled `edge_drift_nonneg` / sign-neutral break) | the proved reach of single-index positivity is the edge, no further |
| **Asano closure** — the pair-gluing operation that preserves confinement, assembling the global theorem from two-spin pieces | No known ζ analogue: no closure operation assembles Ξ's global positivity from verified local pieces (Euler factors are σ > 1 data; and the Bombieri–Hejhal family shows FE-and-growth combination does **not** preserve confinement) | **ABSENT** | the probe report (`2026-07-31-epstein-family-probe.md`): combinations lose the clause discretely |
| Target-class membership: P confined ⟺ real zeros in θ (finite LP) | Ξ ∈ LP ⟺ RH; **de Bruijn–Newman**: Λ_dBN ≥ 0 (Rodgers–Tao), read as the **zero-margin sharpening** — LP membership, if true, is boundary-tight | **EXISTS-WEAKER** | Pólya · Newman 1976 · de Bruijn · Rodgers–Tao. **The zero-margin note:** the Ising instance has slack (strict ferromagnetism sits strictly interior at the base case); ζ has none — any hypothetical ζ-side supplier must be *exactly* boundary-tight. A reading, stated at grade. |

## (3) The shortfall location — against the registered expectation

**Confirmed, in the residue paper's own anatomy.** The rows sort cleanly by index-arity:
- ζ's **EXISTS** positivities are **single-index** — Λ(n) ≥ 0 (one index n), Φ(u) > 0 (one variable) —
  and the proved reach of single-index positivity is **exactly the σ = 1 edge** (drift positivity;
  compiled, with its sign-neutral break, in the residue anatomy §2).
- The **ABSENT** rows are both **pair-index** — the coupling matrix J_ij (indexed by pairs) and the Asano
  operation (which glues pairs). The **centre** is carried by the zero-oscillation E, and the only shape
  that reaches it is the positivity of a quadratic — pair-index — form on the zeros (residue §5): **Q,
  the positive space on the zeros.** The circle theorem is the proved demonstration that a pair-index
  one-sign structure is precisely the kind of object that buys line confinement.
- So the shortfall re-lands on **edge-vs-centre = single-index vs pair-index**, as registered.

**In the arc's coordinates (graded INTERFACES, never forced):** the absent pair coupling = Q's
definiteness; and across the wall's vocabularies the same identification reads once more — the pairing
that over 𝔽_q lands in H²(C×C) and over ℚ has no codomain (Δn₄'s missing target) is, in the
statistical-mechanics vocabulary, the coupling structure with no known carrier. The three-way
identification is a reading across vocabularies — INTERFACES, stated, not derived; nothing here forces it.

## (4) The filed conclusion — the third positive-control coordinate

**The statistical-mechanics face joins the wall's vocabularies.** The supplier-role of the definiteness
now has three named occupants, two of them theorems:

| setting | the definiteness supplier | status |
|:--|:--|:--|
| curves over 𝔽_q | the intersection form on C×C (Hodge index / Castelnuovo) | **PROVED** (Weil 1948; Face-D control) |
| ferromagnetic Ising | the pair-coupling one-sign structure J_ij ≥ 0, under Asano closure | **PROVED** (Lee–Yang 1952; this control) |
| ζ over ℚ | **the named absence** — Q, the positive space on the zeros (`h2`) | OPEN; the arc's object |

Grade of the coordinate: synthesis-level orientation (Tier-C style) over constituent theorems that are
proved in their own fields; the ζ-column is the arc's standing residue, restated in one more vocabulary,
not narrowed by this pass. Two-darknesses: this control **adds a catalogued prism** — the
ferromagnetic-representation route, recorded as tried-and-not-supplied — and claims nothing structural.

**Dated residue filed: LY-REP-A** (kin W-6-EXT-A / C5-DIST-A): whether Φ admits a Newman-class
ferromagnetic representation is a genuine open research question (a positive answer would supply Q — it
is an h2 route, so it lives on the arc's face map as a prism, not as a separate track; the zero-margin
note binds it: any such representation must be boundary-tight). Reopens by author ruling or on new
structure; no new work-order beyond the arc (disposition stated so the cell is not orphaned).

**W-ORD-LEE-YANG-CONTROL: CLOSED at this filing** — completion condition met (proved instance ·
translation table · shortfall location, in the Face-D grammar).

## Pins and closing checks

- PLACE-papers at open `3ab8a76`; the arc addendum + FINDINGS entry land in the companion commit
  (recorded there). SIDE-kernel untouched (`44895f9`, v1.7 = `2957e7d`); nothing deposits.
- Rail empty-diff at `11db565`: verified at close (the five rail papers unchanged; check recorded in the
  companion commit message).
