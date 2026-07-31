# Epstein family probe — the discrete-switch question at the multiplicative place — 2026-07-31

Analytical pass, author-ruled go; no kernel commits, no rail edits, report-first. Protocol: PLACE-papers
`0d9a357` local = remote, tree clean; mirror current at the same pin; rowgen constellation on the cited
arc papers (INVARIANCE_BARRIERS, SIMPLICITY_OF_RIEMANN_ZEROS, THE_RESIDUE_OF_RH) — 0 flags each.

## The registered prediction (verbatim, recorded before looking)

> *the reviewer predicts the clause is DISCRETE — present exactly when the Euler product is (h = 1),
> absent otherwise; no gradation. The alternative worth finding: a genuine coordinate along which the
> clause "switches on."*

**Outcome, stated up front: the prediction SURVIVED, with one precision.** The clause is discrete —
and the graded structure that does exist in the family lives one register down, in the **density**
layer (off-line zero counts, counting constants), never in the **placement** layer (the clause itself).
The family realizes the paper's own density/placement dichotomy internally. Detail below.

## (1) The family: strata by class number

Throughout: D < 0 a fundamental discriminant, K = ℚ(√D), h = h(D), w_D the unit count (6 for D = −3,
4 for D = −4, else 2). The dictionary is classical: forms of discriminant D ↔ ideal classes of K;
for the form Q with class A_Q, the Epstein zeta is the partial class zeta up to units,
ζ_Q(s) = w_D · ζ(s, A_Q), and the partial zeta decomposes over class-group characters:

ζ(s, A) = (1/h) Σ_χ χ̄(A) · L_K(s, χ),

where each **Hecke L-function L_K(s, χ) carries an Euler product**. So *every* ζ_Q in the family is a
finite linear combination of h Euler products — and h = 1 is the degenerate single-term case. The
whole family sits inside the Bombieri–Hejhal linear-combination class. That is the probe's structural
frame.

| stratum | examples (D) | Euler product for ζ_Q? | off-line zeros | T5 counting law (completed ξ_Q) |
|:--|:--|:--|:--|:--|
| **h = 1** | −3, −4, −7, −8, −11, −19, −43, −67, −163 (the Heegner list, complete) | **YES** — precisely: ζ_Q(s) = w_D · ζ_K(s) = w_D · ζ(s) · L(s, χ_D), a product of two Euler-product L-functions (e.g. D = −4: r_Q(n) = 4(d₁(n) − d₃(n)), ζ_Q = 4 ζ(s)L(s, χ₋₄)) | none known; **RH-expectation holds** — the zero set is the union of ζ's and L(s, χ_D)'s zeros, so the clause here is exactly GRH for the two factors (conjectural; the arc's own object, no new row) | N(T) = (T/π) log(√\|D\| · T/(2πe)) + O(log T) — degree 2, conductor \|D\| |
| **h = 2** | −15, −20, −24, −35, −40, −51, −52, … | **NO** — two-term combination; by genus theory both terms factor into *Dirichlet* L-functions: e.g. D = −15, principal Q = x² + xy + 4y²: ζ_Q(s) = ζ(s)L(s, χ₋₁₅) + L(s, χ₋₃)L(s, χ₅) (the non-principal class takes the minus sign) | **Davenport–Heilbronn 1936 applies** (h ≥ 2): infinitely many zeros off the line, including in σ > 1; the genus-factored shape is exactly the DH/BH construction territory | same form: (T/π) log(√\|D\| · T/(2πe)) + O(log T) |
| **h = 3** | −23 (the arc's witness), −31, −59, … | **NO** — three-term combination: principal ζ_Q = (w/3)[ζ(s)L(s, χ₋₂₃) + 2 Re L_K(s, χ)], the cubic-character Hecke L being the weight-1 level-23 cusp-form L-function (itself Euler-product-carrying; the *combination* is not) | DH applies; the programme has located two simple off-line zeros of ξ_Q(−23) (0.953 + 16.29i, 0.798 + 29.55i; residue paper §5) | same form; \|D\| = 23 |
| **h ≥ 4** | −39 (h=4), −47 (h=5), … | **NO** — h-term combinations | DH applies throughout | same form |

**The T5 coordinate across the family (the R1 datum, now placed).** The leading counting rate is
**(T/π) log T for every stratum** — it is fixed by the degree (2) of the completion, not by h; the
conductor |D| enters only inside the logarithm (second-order constant). Two consequences, both clean:
(i) the counting coordinate distinguishes ξ (degree 1, (T/2π) log T) from *every* member of the family
equally — the "twice the rate" of the v1.2 correction is family-uniform; (ii) **the T5/conductor
coordinate is orthogonal to the switch** — it varies smoothly with |D| while the clause flips on
Euler-product presence, and it cannot see h at leading order. The candidate "genuine coordinate along
which the clause switches on" is NOT the counting constant. (Exact constants per stratum: the filed
`W-ORD-T5-EPSTEIN-COUNT` — this probe confirms its scope and feeds it the family table.)

## (2) The switch question — Bombieri–Hejhal 1995 as the hinge

BH 1995 (*On the distribution of zeros of linear combinations of Euler products*, Duke Math. J. 80)
studies exactly the right family: F(s) = Σ_j b_j f_j(s), the f_j Euler products sharing a functional
equation. Their two-sided result, in the probe's terms:

- **On-line, density one:** under standard hypotheses on the components (verified for the relevant
  Dirichlet/Hecke combinations in their paper's cases), **almost all** zeros of F lie on the critical
  line and are simple — the combination *inherits* the on-line density of its Euler-product parts.
- **Off-line, never zero:** yet for a genuine combination (more than one b_j ≠ 0), off-line zeros
  exist and their count to height T is **≫ T** — infinitely many, a linear-in-T family, against a
  total N(T) ∼ cT log T. (Refinements after BH — Fujii's and later work on Epstein zeros off the
  line — sharpen the ≍ T count; exact constants are the work-order below, not asserted here.)

**What the BH family says about discrete-vs-graded.** Take the two-term slice F_{a,b} = a·f + b·g,
(a, b) leaving a pure point (b → 0):

- The **clause** ("all zeros on the line") is **discrete on the family**: it fails — with ≫ T off-line
  zeros — at *every* point with a·b ≠ 0, however small b/a; and it holds (conjecturally, = GRH of the
  components) *exactly at* the pure points. There is no intermediate stratum: no combination with
  "finitely many" off-line zeros, no parameter value where the clause is "partly" true. The onset at
  b = 0 is a discontinuous endpoint, not a graded transition.
- What **is** graded: the *quantities* of failure. The off-line count's constant c(a, b) and the
  heights at which off-line zeros first appear vary continuously with the coefficients and degenerate
  as (a, b) approaches a pure point — the off-line zeros thin and retreat upward, but never vanish.
  The gradation is real and lives entirely in the **density register**.

The class-number strata embed into this picture with h as the term count: h = 1 is the pure point;
h ≥ 2 is off-axis. And h itself is *not* a graded coordinate for the clause either — h = 2 and h = 17
are clause-equivalent (both fail identically); h counts terms, it does not tune proximity.

## (3) The corpus tie-in — the outcome in arc coordinates

**Discrete.** So, in the arc's coordinates:

- **h2's content is binary at the multiplicative place.** The clause = the Euler product's presence,
  full stop. There is no family coordinate — not class number, not conductor, not the BH coefficients —
  along which the positive space on the zeros "switches on" gradually. The wall is not approachable
  along the Epstein family: every deformation away from the product loses the clause entirely and at
  once.
- **The family is a wall-shape confirmation.** The two-witness barrier's structure is maximal exactly
  as Theorem 3.7 states it: agreement on everything form-level (T1–T6, now including form-level T5),
  divergence precisely and only on the clause. The probe adds: this is not an artifact of the chosen
  witness — it is the uniform shape of the whole stratified family.
- **The graded layer confirms the paper's dichotomy from inside the family.** What varies continuously
  (counting constants, off-line densities, conductor data) is all **density**; what switches
  discretely (the clause) is **placement**. The family probe thus lands the density/placement
  distinction — Theorem 3.1's own axis — as an empirical shape of the Epstein family, with the T5
  coordinate explicitly orthogonal to the switch.
- **Had it been graded** the report would have named the coordinate and the next probe on it; the
  honest remnant of that branch is the density-layer question (how c(a, b) → 0 as the pure point is
  approached), filed below as a work-order — a density-register research item, not a clause opening.

## (4) Tracking rule — work-orders

- **`W-ORD-EPSTEIN-OFFLINE-DENSITY`** (NEW) — the graded layer, made exact: (i) the off-line count
  constant for Epstein strata (N_off(T) ≍ T; the constant's dependence on D and h; consult Fujii and
  the post-BH refinements, then derive or cite); (ii) the BH-slice behavior c(a, b) → 0 as b → 0
  (rate, and the height of the lowest off-line zero as a function of b/a); (iii) verify which BH
  on-line-density hypotheses are unconditional for the genus-factored h = 2 strata. Completion: the
  three constants/rates stated with citations or derivations, filed as a density-register table
  beside the T5 table. **Trigger:** at author call; adjacent to `W-ORD-T5-EPSTEIN-COUNT` (which this
  probe feeds: the family counting table above is its input, exact per-stratum constants its output).
- **`W-ORD-T5-EPSTEIN-COUNT`** — confirmed in scope, fed (family-uniform leading rate (T/π) log T;
  conductor-in-the-log second order; exact constants per stratum remain its deliverable).
- **h = 1 clause-truth** (GRH for ζ · L(s, χ_D)) — used as "RH-expectation holds"; this is the arc's
  own standing object, not a probe-surfaced residue; **no new row** (disposition stated so the cell is
  not orphaned).

## Pins

- No paper edits, no kernel commits, no rail edits. PLACE-papers `0d9a357` throughout; SIDE-kernel
  `44895f9`, v1.7 = `2957e7d` unmoved.
- Successor act (same session, next commit): the h2-arc OPEN_TRAILS dated addendum recording the
  outcome and that the registered prediction survived.
