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

## (4) Rider — the zero-cross note (~0.5, folded into this sitting)

**The geometry, stated and verified.**
- **The zero-cross:** the trivial zeros lie on the real ray (σ < 0, t = 0), the nontrivial zeros
  in the strip with the critical line as target; the two lines meet at s = 1/2 and are
  perpendicular (the FE involutions' axes). CLASSICAL.
- **The right-triangle family** (right angle at 1/2, one leg along each zero-line, vertices at
  −2n and 1/2 + iγ): **CONDITIONAL-ON-RH and stated as such** — the nontrivial vertex sits on
  the line only if RH.
- **The unconditional four-fold symmetry:** for any zero ρ, the set {ρ, 1−ρ, ρ̄, 1−ρ̄} consists
  of zeros — the ρ-rectangle centered at 1/2. Verified at ρ₁ (all four |ζ| ≈ 6e−31, mpmath at
  30 dps). **RH is the degeneration of every rectangle to the cross**: Re ρ = 1/2 ⟺ 1−ρ = ρ̄
  (verified exactly at ρ₁: the four-point orbit collapses to two). UNCONDITIONAL as the symmetry,
  the degeneration statement being RH itself.
- **The FE-transport table for the negative evens** (CLASSICAL-AT-CITE, doubly-verified): ζ(1−2n)
  = −B₂ₙ/(2n) exact at n = 1…6; the Euler partners ζ(2n) = (−1)^{n+1}B₂ₙ(2π)^{2n}/(2(2n)!)
  verified at n = 1, 2; and **von Staudt–Clausen puts {2,3} in every denominator** — 6 | den(B₂ₙ)
  for all n (verified: 6, 30, 42, 30, 66, 2730), since p − 1 | 2n holds for p = 2, 3 always. The
  substrate pair on the whole negative-even street, as classical arithmetic.

**The two readings (Tier N, graded READINGS, never claims):**
- **(a) Counting-requires-collinearity** — the author's form of Hilbert–Pólya: a spectrum is a
  line; RH says the zeros are countable-along-a-line the way ℕ and the primes are. The explicit
  formula is named as the existing exact triangulation between the two countings (primes ↔ zeros,
  across the Euler product), and **Weil positivity is the triangulation's one open property** —
  Q, the wall in one more vocabulary. A reading; the explicit formula is classical, the
  identification of its open property with the arc's Q is the arc's own standing content
  (residue paper §5–6).
- **(b) The baby-Q reading** — the right angle at 1/2 is orthogonality under the plane's
  positive-definite form: the **rank-2 solved instance** of the definiteness question, with
  Pythagoras as the diagonalized pairing. The wall is the same statement in infinite rank.
  Cross-linked to the Lee–Yang control's fixed-locus row and the quadratic-register note (§2
  above). A reading — rank-2 solves nothing in infinite rank; the value is the vocabulary.

**The boundary paragraph (filed beside the readings so the seed never outgrows its
certificate).** The universality question — "does this geometry mean anything beyond ζ?" — is
answered by the corpus's own scoping results, at their homes: the substrate-scoped calculus
(CONCLUSIONS_OF_RECORD: *"Across determined systems there is no universal formation tuple. What
is invariant is classification × certification"*) scopes every substrate-flavored observation to
its system; the Silence Principle's own scope clause (Seale 2026a) bounds what κ-readings
transport; and the modular-register seed is carried at its compiled witness (the h1 ledger's
`C4_modularity_at_Phi` with the theta witness, lv v0.6.0), not at the readings' level. The
ferry's three handles (complete-for-substrate · seed-of-the-modular-register · silent-beyond)
are mapped to these three homes — recorded explicitly, since the handles do not appear verbatim
in the corpus and verify-at-source requires the mapping be stated, not assumed.

## (5) Rider 2 — the wave-field and duality note (~0.5, folded into this sitting)

**The wave decomposition (CLASSICAL, cited).** The explicit formula (Riemann–von Mangoldt–Weil)
is the prime field's spectral decomposition: ψ(x) = x − Σ_ρ x^ρ/ρ − log 2π − ½log(1−x⁻²) — each
zero ρ = β + iγ a frequency γ with amplitude x^β; **RH is the uniform √x envelope** (every
amplitude exactly x^{1/2}). **The energy reading (Tier N):** single-index positivity (Λ(n) ≥ 0,
Φ > 0) is amplitude/one-point data — edge-reaching, as compiled; the pair-index object is the
field's ENERGY form; **Montgomery's pair correlation is the measured two-point function** —
density register, exactly the classification the DQPT screen received (F.2026-07-31: measured
statistics of located zeros, no bearing on the pairing); **Weil positivity is the energy's
positive sign** — placement register. The index-arity sort in field language; cross-linked to the
keystone (INDEX_ARITY_AT_THE_CRITICAL_LINE). A reading over classical objects, each at its cite.

**The −1/2 non-vanishing (verified at source, factor by factor).** FE:
ζ(−1/2) = 2^{−1/2}·π^{−3/2}·sin(−π/4)·Γ(3/2)·ζ(3/2); every factor nonzero — the sine sits a
half-step off its even lattice (sin(−π/4) = −√2/2), Γ(3/2) = √π/2, ζ(3/2) = 2.6123… in the Euler
zone; product = ζ(−1/2) to 5e−32. **The reading (Tier N):** the only real-zero mechanism on the
real axis is the sine lattice s = −2n; −1/2 is protected by the same single-index (Euler-zone)
mechanism that holds the σ = 1 edge. A reading; the factorization is classical.

**The duality-indexing paragraph (CLASSICAL, cited; boundary on its face).** Primes ⟺ zeros is
an exact dual pair (the explicit formula, unconditional); twisted counting ⟺ the L(s,χ) zero
sets (the GRH cascade's conductor lattice — GRH_CASCADE, corpus); dilations ⟺ the scaling-flow
spectrum (Berry–Keating xp / Connes' trace-formula reading — **graded READING**, the one
speculative row, marked). The boundary sentence on its face: **the duality is unconditional; the
rectangles are unconditional; the cross-collinear triangulation — every frequency on the line —
IS RH.** Nothing in the note moves the wall; it names the wall in field vocabulary.

## (6) Rider 3 — the gauge note (~0.4, folded into this sitting)

**The gauge theorem, verified numerically (CLASSICAL-AT-CITE: Riemann–von Mangoldt; the
Γ-argument derivation).** Two independent routes to the smooth counting term:
- **(a) the angle-sum over the trivial lattice**: Im log Γ(¼ + iT/2) = −γT/2 − arctan(2T) +
  Σ_k [T/(2k) − arctan(T/(2k+½))] (Weierstrass product) — the arctan lattice at the half-shifted
  even integers, Stirling-free, summed to convergence;
- **(b) the digamma density**: N'(T) = (1/2π)·Re ψ(¼ + iT/2) − log π/(2π), integrated.

At T = 50, 100, 150 the two routes agree to ≤ 8e−4 (quadrature-limited), match the asymptotic
(T/2π)log(T/2π) − T/2π + 7/8 to ≤ 1e−3, and bracket the true zero-counts (mpmath zetazero) with
S(T) ≈ +0.58, −0.002, −0.75 — |S| < 1 as classical. **The trivial lattice's harmonic shadow IS
the mean density of the nontrivial zeros** — verified, both routes, at cite.

**The readings (Tier N):**
- **(a) Triangles-compute-the-count** — the right-triangle family (rider 1), angle-summed at the
  trivial vertices, is exactly the winding's smooth part: each trivial lattice point contributes
  its arctan view-angle of the height T, and the constant lattice density integrates to the
  log-density. The zero-cross geometry computes the gauge. A reading over a classical identity.
- **(b) Gauge-vs-fluctuation = drift-vs-oscillation** — N(T) = smooth + S(T) mapped onto the
  residue anatomy: the archimedean/trivial side gauges the count (understood, single-place,
  single-index kin — the digamma is the archimedean local term of the explicit formula, at
  cite); **S(T) is the oscillation's counting face, the pair-interaction term — where the wall
  lives.** Cross-linked to the keystone's index-arity sort and the wave-field energy note
  (rider 2, §5).

**Boundary sentence, on the face:** the gauge half is theorem; the fluctuation half's positivity
is the arc's open clause; no narrowing claimed.

## (7) Rider 4 — the out-formation note (the sitting's closing rider, ~0.3)

**The two-channel reading (Tier N).** The zero-cross as complementary out-formation sources: the
trivial/archimedean lattice out-forms the DENSITY register — its harmonic shadow is the mean law,
at gauge-theorem grade (rider 3's two verified routes); the nontrivial line out-forms the
ARITHMETIC register — the explicit formula carrying the prime fluctuations; the exchange sits at
s = 1/2. Cross-link flag, recorded per verify-at-source: the named vocabulary home
`MA_AND_PROGRAMME_OUT_FORMATION` was **not located** in the repo or the download-layer listing at
that handle — the cross-link is carried as the author's pointer, flagged for the author to supply
the home; the reading stands on its own Tier-N grading meanwhile.

**The archimedean-instance claim-shape — a NAMED CANDIDATE for the INVARIANCE_BARRIERS
calibration family (PROPOSED; the author rules at the IB v1.2 read; NOT added to the paper).**
The candidate row: *"the archimedean interface carries κ > 0 for the density register and κ = 0
for the placement register"* — the harmonic shadow as the bright half, S(T) as the dark half; the
Sieve Ceiling's hypothesis shape instantiated at the archimedean place. Would-be verification
path, stated with the candidate: the bright half's certificate is the gauge note's two verified
routes (the trivial lattice computes the mean density); the dark half's certificate is the
existing barrier corpus (single-index/edge results + the compiled negatives — placement does not
cross). The row waits at the IB read gate; nothing lands in the paper now.

**The export-dock reading (Tier N, one paragraph).** The negative street as arithmetic's
out-formation into physics: ζ(−1/2)-type values in Casimir-energy regularization and ζ(−1) = −1/12
in the classical regularization literature (CLASSICAL-AT-CITE to the physics literature), with the
Bernoulli/{2,3} denominators as the street's arithmetic (verified in rider 1). Corpus-cite flag,
recorded honestly: no dedicated corpus home for "the −1/12 calibration" was located; the nearest
corpus Casimir occurrences (heritage/UNIFICATION_OF_FORCES.md) are **group-theoretic Casimir
invariants — a different Casimir**, noted precisely to avoid a false link. Reading only; physics
grades untouched.

## Closing — the sitting CLOSES with this rider

Seeds + this consult note (riders 1–4 folded in) filed and CLOSED; the builds' checkpoint
reports untouched by this sitting; rail empty-diff at `11db565` verified at the sitting close;
nothing deposits.

**The author-gate board, restated once at the close:** (1) the INVARIANCE_BARRIERS v1.2 read —
now with the archimedean-instance candidate row waiting at that gate; (2) the retitled keystone
read (INDEX_ARITY_AT_THE_CRITICAL_LINE v0.1.1, 1.5a-7, DRAFT–HELD); (3) the title-law sweep's
four live flags (THE_PROOF · MECHANISM_EXCLUSION · THREE_PROOFS · SPECTRAL_CANNON); (4) the
Duursma fourth-supplier ruling (PROPOSED, one exact instance); (5) the held QWantedPoster branch
disposition (lv `word-pairing-interface` = `5a14205`, held, not landed).

**Post-close flag resolution (2026-08-01, the fourth-supplier ruling; verify-first).** Of the two
carried-pointer flags: the -1/12 calibration cross-link **RESOLVES** to
phase2/physics/FANO_DERIVATION_OF_LAMBDA.md (the 1/12-Residual section verified at source; the
named _v0_1 suffix is the header version, the filename is unversioned). The out-formation home
MA_AND_PROGRAMME_OUT_FORMATION_v0_1.md was **verified-ABSENT** at the named download-layer handle,
and THE_SUBSTRATE lambda = 12 = (26-2)/2 note was **not located** at source — both stay open as
carried pointers, checks recorded. The W-DUURSMA seed GRADUATED to the keystone supplier table
(v0.2) by the same ruling; the sitting stays CLOSED.

**Final pointer resolution (2026-08-01, content-first search; both flags CLOSED).** (1) The
out-formation home: content keys (the note title, moonshine peeps, Fletcher, the door/moonlight
etymology character) searched across the repo AND the download layer — zero hits. Flag CLOSED
**ABSENT-VERIFIED**, project-mirror provenance noted: the June-5-2026 working note ("Ma and the
Programme's Vocabulary of Structural Silence") survives in the reviewer's project mirror only;
restoration to the repo is the author's call (the recovered-registration precedent). The rider-4
cross-reference stands as the author's pointer to that provenance. (2) The lambda note: found by
content at its ACTUAL home — THE_REVIEWER_PANELS.md L45: lambda = 12 = (D-2)/2 with D = 26, the
bosonic-string anchor, recorded there as a checked literature anchor (the ferry's handle named
THE_SUBSTRATE; the corrected home is recorded, verify-then-link honored). Flag CLOSED
**RESOLVED-with-corrected-home**: the export-dock cross-link now stands on THREE homes —
FANO_DERIVATION_OF_LAMBDA.md (the 1/12-Residual section), THE_REVIEWER_PANELS.md L45 (the
bosonic-string anchor), and OPEN_TRAILS L133 (the standing wonder: whether the cosmological 1/12
is structurally the zeta-regularization/bosonic-Casimir -1/12 — the corpus had the -1/12 home
after all, as a filed wonder). Board unchanged at four gates.
