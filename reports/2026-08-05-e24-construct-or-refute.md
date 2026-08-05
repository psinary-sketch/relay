# E-24 — CONSTRUCT-OR-REFUTE ON THE RE-POSED π₀ — 2026-08-05

Author-called. Pins at open: PLACE-papers = `fef15d2` (keystone v0.12, untouched this pass);
relay = `d3571c5`; lv `14720d9`, kernel `44895f9` — unmoved; rail at the post-rename baseline.
Nothing deposits.

## §1 — THE POWER CLAUSE RUNS FIRST, AND IT DECIDES THE DESIGN

The standing law requires the uncertainty and the expected separation stated before the test.
Stated:

- **Measurement uncertainty at accessible windows: ~0.04–0.06** (the height drift at matched
  L = 300 is 0.037; the L-drift across L = 50…1200 is ~0.06).
- **Expected separation from CORRELATION structure:** π₀'s ideal for an m-fold superposition
  of independent GUE spectra is **γ − 1 − log m**, so ζ (m = 1) against a 2-fold object
  differs by **log 2 = 0.693** — ample power.
- **Expected separation from PLACEMENT at fixed R₂: exactly 0.**

**The third line is not an estimate — it is a fact of the definition.** π₀ is computed from
x_j = N(γ_j): the unfolded IMAGINARY PARTS. **The real parts never enter.** Two objects with
identical imaginary-part sequences and entirely different placements — every zero on the
line, or half of them off it — return the same π₀ to every digit. **The test as specified
has zero power for placement, by construction rather than by insufficient data**, and the
power clause's instruction is therefore to say so and re-price rather than to run it and
report a null.

**And running it would have been worse than uninformative.** The Epstein witness's zero set
is not a single GUE-like spectrum (ζ_Q for disc −23, h = 3, is a class-group combination of
L-functions), so its π₀ would very likely differ from ζ's — **by the correlation term
−log m, not by placement.** A separation would have appeared, and it would have measured the
witness's different correlation structure while looking like a placement channel. The
instrument check the ferry demanded before interpretation is the reason the run is not made:
the confound is not merely possible, it is the expected outcome.

## §2 — THE DERIVED FAMILY (analytic), AND TWO FAILED VALIDATIONS (reported)

For any translation-invariant R₂ = 1 − K(r), the same computation that gave c_ideal gives

  **π₀ = −log 2π − 2∫₀^∞ K(r) log r dr**,

with **GUE** (K = sinc²) → **γ − 1 = −0.42278**, **Poisson** (K = 0) → **−log 2π =
−1.83788**, and an **m-fold superposition** (K = (1/m)·sinc²(r/m)) → **γ − 1 − log m**
(−1.11593 at m = 2, −1.52140 at m = 3).

**Validation attempted twice, and it did not succeed; both attempts are reported.** The
first synthetic halved ζ's unfolded positions before merging, which doubled the merged
density — a density artifact (π₀ ≈ −139), not a superposition; discarded. The second built
two disjoint stretches of ζ's zeros decimated by 2 and merged them, giving π₀ = −0.392
(L = 200) and −0.416 (L = 400) — **near the GUE value, not the m = 2 value.** The reason is
in the construction, not the formula: **decimating a GUE spectrum is not the same as
independently thinning it**; every-other-eigenvalue preserves rigidity, so the synthetic is
closer to one rigid spectrum than to two independent ones. (The i.i.d.-surmise route is
excluded for the same class of reason, per the caveat already filed with the height control.)
**The superposition value is therefore DERIVED-BUT-UNVALIDATED here, and is used below only
as the reason a naive Epstein comparison would confound.** A validation would need a genuine
independent pair of GUE spectra, which is a separate build.

## §3 — THE TEMPLATE CLAUSES, GRADED

| clause | verdict | reason |
|:--|:--|:--|
| **(a) square-free-by-symmetry** — is some ζ-side quantity = π₀² by FE-evenness, as lead(H) = p₀² is by self-duality? | **FAILS** | In the toy the identity is a statement about COEFFICIENTS: H = h·h^σ and lead(h) = p₀, so the FE factorization produces the square. π₀ is not a coefficient of anything — it is an asymptotic average — and asymptotic averages have no factorization for a functional equation to act on. |
| **(b) attack-pricing** — is anything measured to scale as π₀⁴? | **FAILS** | Nothing on the ζ side has been measured to scale in any power of π₀; there is no ζ-side quantity known to us that π₀ prices. |
| **(c) window-currency** — is there a ζ-side window whose width is in π₀'s units? | **FAILS** | π₀ is a dimensionless log-ratio average; the one zero-margin boundary ζ has (Λ = 0) has no width to denominate, and no measured window has been expressed in these units. |

**THE CATEGORY NOTE (structural, not a difficulty):** the toy's p₀ is an **exact finite
self-datum defined at every n** — a coefficient one can compute, square, and multiply. π₀
**exists only as a limit of a truncated statistic**, approached from a low-height side with a
1/log γ systematic. The template asks for an algebraic object and π₀ is an analytic
asymptotic; the clause failures above are all one failure wearing three faces.

## §4 — THE VERDICT

**REFUTE-WITH-REASON — the registered branch, and the reason is structural rather than
empirical.** π₀ cannot be the currency: (i) **its definition contains only the imaginary
parts, so its value is constant across placements** — move every zero off the line, keeping
the imaginary parts, and π₀ does not change by a digit — while the currency must price
exactly that register; (ii) its ideal value is a functional of R₂ alone — density-register
data — and the era's certified results place the wall in the pairing register; (iii) all three template
clauses fail, for the single structural reason that π₀ is an asymptotic statistic where the
template requires an algebraic self-datum.

**π₀ is not thereby worthless — it is correctly re-classified.** It stands as what v0.12
already made it: **a shape discriminant**, a one-number reading placing ζ's zeros among
lattice, GUE, and Poisson. That is a real instrument. It is simply not a currency.

## §5 — THE EXCLUDED CLASS, FILED AS THE POSITIVE RESULT

**The currency cannot be a correlation-determined statistic.** More sharply, and this is the
reusable form: **no statistic computed from the imaginary parts alone can serve as the
currency**, because such a statistic takes the same value for every placement of the zeros;
and no functional of R₂ can serve, because R₂ is density-register data.

This narrows the search by a named family, and it is the same wall met from a new side. It
agrees with **E-17's register gap** (ensemble law → the instance's pairing is un-compiled),
with **F.2026-07-31** (the DQPT channel: density register, no bearing on the pairing), and
with **E-10's null** (no coefficient-local correlation with off-line placement). Four
independent approaches, one boundary: **the density register does not reach placement, and
any currency drawn from it inherits that reach — its value is fixed by density-register data
alone, so it is constant across the placements the wall distinguishes.** The currency question re-poses with the
correlation-determined class excluded — and with the requirement now explicit that a
candidate must be a statistic in which the real parts appear.

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `fef15d2` (keystone v0.12 untouched) → this pass's commit |
| SIDE-lv-conservation | main = `14720d9` — unmoved |
| SIDE-kernel | `44895f9`; v1.7 — unmoved |
| relay | this report's commit; instrument `tools/e16/e24_power_and_class.py` |
| rail | `de621b1` / `2147a03` — at the post-rename baseline |

Keystone cargo: this verdict, held. Consolidation DEFERRED. Mirror rebuilt with the standing
check. Nothing deposits.
