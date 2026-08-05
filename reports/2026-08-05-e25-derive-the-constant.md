# E-25 — DERIVE THE CONSTANT FROM THE IDENTITY — 2026-08-05

The re-route, author-called. Analytic, with two cheap atom-level checks (no factorization).
Pins at open: PLACE-papers = `25660b2`; relay = `b6808db`; lv `14720d9`, kernel `44895f9` —
unmoved; rail at the post-rename baseline. Nothing deposits.

## §1 — THE TARGET, STATED EXACTLY

Let the band be the resolved indices i = 2 … R−1 (boundary-separated, as measured), and let
β_j = 1/(2γ_j)² be ζ's atoms, β̃_j the smooth-density control's. The measured quantity is

  **c(K) = Δrep / harm**, where **Δrep = Σ_{i<j ∈ band} 2[ log|β_i − β_j| − log|β̃_i − β̃_j| ]**
  and **harm = Σ_{i<j ∈ band} 1/(j−i)**.

**As a statistic of the point process it is BILINEAR, not linear:** with kernel
f(r) = log|r| it is the pair statistic Σ_{i≠j} f(x_i − x_j), whose expectation is
∫∫ f(x−y) R₂(x−y) dx dy — the two-point correlation R₂ enters, and the normalization is the
harmonic pair-weight Σ 1/(j−i). Unfolded (both processes share the density function by
construction, so the density cancels in the difference), with the control's unfolded
positions being exactly the integers, the idealized statistic is

  **Δrep_ideal(L) = 2[ ∫₀^L (L−r)·R₂(r)·log r dr − Σ_{n=1}^{L−1} (L−n)·log n ]**,
  **harm(L) = Σ_{n=1}^{L−1} (L−n)/n**, L = band length.

## §2 — THE ROUTE, AND ITS OBSTACLE NAMED IN ADVANCE

The route is the pair-correlation computation: R₂(r) = 1 − (sin πr/πr)² (Montgomery's
conjecture; the sine-kernel form), with the number-variance/linear-statistic apparatus.
**The obstacle, named before use: log|r| is NOT band-limited, so Montgomery's unconditional
restricted-support theorem does not cover this kernel as stated.** A band-limited truncation
bounds the small-r part but leaves the r ≳ 1 tail, which is where log r has its mass; no
unconditional bracket follows. **Everything derived below is therefore graded
CONDITIONAL-ON-PAIR-CORRELATION.**

## §3 — THE DERIVATION

Split R₂ = 1 − sinc²(r), sinc(r) := sin πr/πr.

**(a) The "1" part against the lattice sum.** Using Stirling for Σ log n and the
Glaisher–Kinkelin asymptotic for Σ n log n,
 ∫₀^L (L−r)log r dr − Σ_{n<L}(L−n)log n = −(L/2)·log 2π + O(log L),
the L log L terms cancelling exactly.

**(b) The sine-kernel part.** With ∫₀^∞ (sin u/u)² log u du = (π/2)(1 − γ − log 2),
 ∫₀^∞ sinc²(r) log r dr = ½(1 − γ − log 2π),
so −∫₀^L (L−r) sinc² log r dr = −(L/2)(1 − γ − log 2π) + O((log L)²), the r·sinc²·log r
piece contributing only (log L)²/(4π²).

**(c) The sum.** The log 2π terms cancel exactly between (a) and (b):

  **Δrep_ideal(L) = L(γ − 1) + O((log L)²)**, and **harm(L) = L(log L + γ − 1) + O(log L)**,

hence the closed form

  **c_ideal(L) = (γ − 1)/(log L + γ − 1) + O((log L)²/L) → 0.**

At the measured band L = 151 this is (−0.4228)/(5.017 − 0.4228) = **−0.092**.

## §4 — THE TWO CHECKS (atoms only)

**Check 1 — VOID, and filed as such.** The first decomposition defined the scale factor
λ from the measured sum itself and then subtracted it; the residual was zero to 50 digits
**by construction**. Circular, no content, discarded — recorded here because a void test
that looks like a triumphant null is exactly the failure the verification law exists to
catch.

**Check 2 — non-circular, decisive.** Build a SURROGATE control from ζ's OWN zeros shifted
by the measured constant offset D (the band mean of γ̃ − γ). The surrogate carries ζ's exact
fluctuation structure and differs from ζ only by the offset:

| R | c measured | c surrogate (offset only) | surrogate's share | residual | D |
|--:|:--|:--|:--|:--|:--|
| 36 | 0.815726 | 0.691327 | **84.8%** | 0.1244 | 1.352 |
| 75 | 0.893994 | 0.726024 | **81.2%** | 0.1680 | 1.153 |
| 118 | 0.932593 | 0.741863 | **79.6%** | 0.1907 | 1.049 |
| 153 | 0.951342 | 0.751349 | **79.0%** | 0.2000 | 0.9969 |

**~80% of the measured c is reproduced by a control that differs from ζ by nothing but a
constant γ-offset** — the smooth-COUNTING zeros sit systematically ≈1.0–1.35 higher in γ
than the true zeros (the S(T)/counting-convention offset), and that offset enters the log-pair
sum through the nonlinear β = 1/(2γ)² map.

## §5 — THE REGISTERED ADJUDICATION

**(i) A closed form IS derived** — c_ideal(L) = (γ − 1)/(log L + γ − 1), limit **0**.
**(ii) Recognition, attempted before interpretation:** the finite-L form is built from γ and
log L; **log 2π appears and cancels exactly** between the Stirling and sine-kernel halves —
a clean cancellation, and the pre-stated basis element that shows up does so only to vanish.
The limit constant is **0**, not 1 and not 1.3.
**(iii) THE ADJUDICATION FIRES ITS THIRD BRANCH — "a value elsewhere files first-class and
re-opens the whole c-sequence reading."** The derived pair-correlation content is 0 (and at
finite L is small and NEGATIVE, ≈ −0.09), while the measured sequence rises 0.58 → 0.95.
**The gap is identified, not merely noted: the measured statistic is ~80% the control's
construction offset.** Consequences, stated without going past the mapping:
- **The c-sequence was not measuring a pair-correlation constant.** The unit-constant
  question as posed rested on a statistic dominated by a deterministic artifact of how the
  control was built.
- **A seventh point would have measured the artifact more precisely.** The re-price's
  economic verdict is superseded by a structural one: the rung was not worth buying at any
  price.
- **What survives:** the residual after the offset surrogate (0.12 → 0.20, rising) is the
  only part of c that could carry fluctuation content — and it matches neither the derived
  −0.09 nor any fitted family. It is not yet a cleanly separated quantity (the constant-offset
  surrogate is a model, not an exact decomposition), and it is filed as such: **an open
  quantity, ungraded, not a measurement of anything until a clean separation exists.**

## §6 — THE FOUR FILINGS

1. **THE POWER-ANALYSIS CLAUSE** (registration discipline, standing): *no discrimination
   test runs until its measurement uncertainty is stated and the predicted separation
   exceeds it.* Credited to the sixth point — whose UNDISCRIMINATED verdict lay inside its
   own systematic, so the test could not have discriminated wherever the point fell.
2. **THE EXTRAPOLATION-DEAD DATUM** (instrument-limitation result): on this meter, **cost
   doubles per rung while separation grows linearly** — the extrapolation path is closed by
   arithmetic, not by taste. Filed in the corpus's own genre: the meter's reach is itself a
   measured quantity (dps ≈ 4·Σ log₁₀(2γ_k); ~195 s/zero at K = 384; J must grow with K).
3. **π₀'s ROW CORRECTED:** the unit-constant reading is **UNSUPPORTED (not refuted)** — its
   support was family (a)'s near-unity limit, and family (a) retired as ladder-dependent;
   E-25 adds that the statistic underlying the whole sequence is offset-dominated. The
   denominator question is not answered negatively; it is **ill-posed as posed** and awaits
   a statistic that isolates fluctuation content.
4. **THE TWO-OF-THREE TAIL AGREEMENT** (0.97969 in 1/K, 0.97624 in 1/R) filed **Tier N,
   unpromoted** — and now adjudicated by E-25: with the target's pair-correlation content
   derived to be 0, the tail agreement is **an artifact-fit** (two variables agreeing on the
   extrapolation of an offset-dominated sequence), carrying no evidence for a unit constant.

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `25660b2` at open → this pass's commit |
| SIDE-lv-conservation | main = `14720d9` — unmoved |
| SIDE-kernel | `44895f9`; v1.7 — unmoved |
| relay | this report's commit; instruments `e25_decompose.py` (VOID, retained as the record), `e25_offset_test.py` |
| rail | `de621b1` / `2147a03` — at the post-rename baseline |

Keystone cargo eight-deep, held. Mirror rebuilt with the standing check. Nothing deposits.
