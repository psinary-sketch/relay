# W-HALF sitting — exact relations verified · the quadratic-register note · the Duursma seed — 2026-08-01

Bounded sitting run beside the builds (no disturbance: separate repos, no lake contention).
Internal-until-fruit: this is a consult note + wonder-seeds; no keystone. All numerics
doubly-sourced (route A = mpmath Euler–Maclaurin; route B = the Knopp–Hasse globally convergent
η-series, independent implementation). **Route-B correction recorded honestly:** the first route-B
run used a mis-transcribed Hasse form and disagreed by a constant ≈1.13 — caught by the
double-sourcing itself (the discipline worked); corrected to the Knopp–Hasse η form; all
comparisons below are from the corrected run, agreement ≤ 1e−16.

## (1) The exact relations — each CLASSICAL-AT-CITE, verified at source

| relation | verification (A vs B) | status |
|:--|:--|:--|
| ζ(0) = −1/2 | exact both routes | CLASSICAL (FE; Bernoulli B₁) |
| ξ(0) = ξ(1) = 1/2 | two-sided limit = 0.5 to 1e−26; closed-form residue composition ½·π^{−1/2}·Γ(½) = ½ | CLASSICAL (Riemann) |
| ζ(−1/2) = −ζ(3/2)/(4π) | both sides agree to 1e−42; routes agree to 3e−19 | CLASSICAL (FE at s = −1/2) |
| trivial zeros ζ(−2n) = 0 as Γ(s/2)-pole compensations | ζ(−2,−4,−6) = 0 both routes; completed Λ₀ = π^{−s/2}Γ(s/2)ζ(s) tends to finite nonzero limits (0.191…, 0.0788…, 0.0610…) | CLASSICAL (the archimedean factor's poles exactly cancelled) |
| Gaussian–Mellin identity ∫₀^∞ e^{−πx²}x^{s−1}dx = ½π^{−s/2}Γ(s/2) | quadrature vs closed form at s = 0.7: 8.6e−32 | CLASSICAL (Tate's local factor) |
| ζ real and negative on (0,1) | five sample points, both routes, all negative, agreement ≤ 2e−16 | CLASSICAL |
| ζ(−n) = −B_{n+1}/(n+1); B₂ = 1/6 | exact at n = 1,2,3,5; denominator 6 = 2·3 | CLASSICAL (Euler; von Staudt–Clausen: the primes p with (p−1) \| 2 are exactly {2,3}) |

## The programme READINGS (Tier N, filed as readings, never claims)

- **Location-vs-value duality of ±1/2**: the value −1/2 at s = 0 / +1/2 for ξ at the endpoints,
  against the location 1/2 of the critical line — the same rational at the value register and the
  location register. A reading; no mechanism asserted.
- **Trivial zeros as the archimedean quadratic's spectrum**: the Gaussian–Mellin identity places
  the trivial zeros as pole-compensations of the Gaussian's Mellin transform — the archimedean
  (single-index, quadratic-kernel) channel owns them; the nontrivial zeros are what remains when
  that channel is stripped. Consistent with the drift/edge anatomy; a reading.
- **Center-equals-weight**: s = 1/2 as the fixed point of the FE ↔ the weight-1/2 of the theta
  garment (the metaplectic altitude of the residue's wanted poster). A reading.
- **The shared fixed-locus topology with Lee–Yang**: the critical line and the unit circle as
  fixed loci of their FE involutions (the LY control's register mapping), now joined by the von
  Staudt–Clausen {2,3} at B₂ — the substrate pair appearing at the first negative-integer value.
  A reading; the {2,3} appearance is a noted coincidence-budget item, not evidence.

## (2) The quadratic-register note (~0.3)

The four-layer quadratic braid, stated once and graded synthesis-not-claim: **the archimedean
Gaussian** (e^{−πx²}, whose Mellin transform is the completed zeta's archimedean factor — verified
above) · **the theta garment at weight 1/2** (θ(z) = Σ e^{πin²z}, the metaplectic altitude; the
C₄ modularity witness of the h1 ledger) · **the weight-3/2 class-number layer** (the Hurwitz
class-number generating function is the weight-3/2 Eisenstein series; H(23) sits over the arc's
disc −23 witness with h(−23) = 3) · **the pairing Q** (a quadratic form on the zeros — the
pair-index space of the keystone). Four quadratic layers, one register; every identification
carries a classical cite; the braid as a whole is a SYNTHESIS reading (Tier C-style orientation),
cross-linked to the Lee–Yang control's fixed-locus row and the 2-bit-phase coordinate (UAC-7).
No claim that the braid derives anything.

## (3) W-DUURSMA — the seed filed, the bounded check RUN

**Registered expectation (recorded before computation): the substrate's own code-zeta satisfies
its RH.** The extended Hamming [8,4,4] over 𝔽₂ — Type II self-dual, the substrate's code garment
([[7,1,3]] Steane's classical parent) — has weight enumerator W = x⁸ + 14x⁴y⁴ + y⁸, d = d⊥ = 4.

**The computation (doubly-sourced, exact rational arithmetic):** the Duursma zeta polynomial
solved from its defining coefficient identity (all 9 monomial equations satisfied, an
overdetermined consistent system):

P(T) = (1 + 2T + 2T²)/5, with P(1) = 1 and the self-dual functional equation p₂ = q·p₀
verified. Roots: T = (−1 ± i)/2. **|T|² = p₀/p₂ = 1/2 = 1/q exactly** (conjugate pair,
negative discriminant) — the zeros lie exactly on |T| = 1/√2.

**DUURSMA-RH HOLDS for the substrate's code — exactly, not numerically.** The expectation
survived. Literature status: the [8,4,4] case is classical in Duursma's own example set
(checkable, and here checked); the general extremal-self-dual conjecture remains open.

**The seed (W-DUURSMA, filed at grade):** a candidate **FOURTH supplier setting — PROPOSED,
never forced**: combinatorial, with the **MacWilliams involution's fixed locus** in the
supplier-role (self-dual code = fixed point of the MacWilliams transform; the FE of the code-zeta
is that involution; the definiteness supplier candidate = the self-duality/Type-II structure).
Joins the supplier table only on the author's ruling; until then it is a seed with one exactly
verified instance and an honest caveat — one instance is an existence proof of the SETTING, not
of a pattern.

## Closing

Seeds + this consult note filed; the builds' checkpoint reports untouched by this sitting;
rail empty-diff at `11db565` verified at the sitting close; nothing deposits.
