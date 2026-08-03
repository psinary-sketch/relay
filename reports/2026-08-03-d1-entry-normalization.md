# D-1's ENTRY FACE — the normalization sub-problem — 2026-08-03

Pins at open: PLACE-papers = `0793a63`; relay = `2eddf0c`; lv `14720d9`, kernel `44895f9` —
unmoved; rail at the post-rename baseline. Nothing deposits.

## §1 — THE SUB-PROBLEM, STATED EXACTLY (before any number)

Find N(K) such that Δosc(K)/N(K) is K-stable, where Δosc(K) = the OSCILLATION band of the
boundary-separated relative pair-energy (ζ − control) of the depth-K string (the band:
resolved nodes 3..R(K); the boundary: pairs touching nodes 1–2; the convention of the
W-TWOSIDES/W-SHAPE sittings). **Pipeline note (stated in advance):** the two prior
calibration points came from two pipelines (K = 16 from the full-measure integral route;
K = 64 from the 300-atom truncated objects); for internal consistency all three points are
RE-DERIVED here in the uniform truncated-object pipeline — the Jacobi coefficients NEST, so
K = 16 and 32 come free from the existing K = 64 caches (`shape_jacobi_{zeta,ctrl}.txt`,
dps 700). The re-derived values supersede the ferry's nominal calibration pair for this
sub-problem.

**The candidate normalizations, TABLED BEFORE COMPUTING, with their two-point scalings** (the
old-pipeline pair Δosc = 5.03 at R = 8, 87.01 at R = 36 gives the raw exponent
p = log(17.3)/log(4.5) ≈ 1.90 — between per-gap (p = 1) and per-pair (p = 2); predictions
carried per form):

| form | N(K) | the two-point constants (old pair) | prediction |
|:--|:--|:--|:--|
| (a) per-pair | C(R−2, 2) | 0.335 → 0.155 (drifting ÷2.2) | if the drift is the K=16 window's smallness, (a) stabilizes between 32 and 64 |
| (b) per-gap | R − 2 | 0.838 → 2.56 (growing ×3) | not stable unless the growth is boundary contamination |
| (c) per log-window | log(R−2) | 2.81 → 24.7 | expected unstable (tabled for completeness) |
| (d) harmonic pair-weight (density-normalized) | Σ_{osc pairs} 1/(j−i) | computed in-run | the log-corrected intermediate between (a) and (b) |

**The stability criterion, stated in advance:** a form is K-STABLE iff its three constants'
max/min ≤ 1.25 (a 25% band — sized to the window noise of the smallest point).

## §2 — REGISTERED EXPECTATION (VERBATIM from the ferry, before computation)

*"exactly one candidate normalization is K-stable across the three points (the currency's
denominator identified); the null (none stable, or several indistinguishable) files the
spread as the datum and re-prices the fourth point."*

## §3 — THE THIRD POINT AND THE ADJUDICATION

**Executed** (`tools/e16/d1_normalization.py`; all three points from the nested Jacobi
caches, one pipeline, dps 700).

**The pipeline-consistent triple:** Δosc = 5.037 (R = 8) · 25.379 (R = 17) · 87.012 (R = 36)
— (the K = 16 value re-derives to 5.037 vs the old-pipeline 5.03: the two pipelines agree at
this point to 0.15%, a free cross-check).

| form | c(16) | c(32) | c(64) | max/min | stable (≤ 1.25)? |
|:--|:--|:--|:--|:--|:--|
| (a) per-pair | 0.336 | 0.242 | 0.155 | 2.17 | no |
| (b) per-gap | 0.840 | 1.692 | 2.559 | 3.05 | no |
| (c) per log-window | 2.81 | 9.37 | 24.7 | 8.78 | no |
| (d) harmonic pair-weight | 0.579 | 0.730 | 0.821 | 1.42 | no |

**VERDICT: the registered NULL branch fires — none of the tabled forms is K-stable at the
pre-stated criterion.** The spread, filed as the datum:
1. **The running exponent DECLINES:** p(16→32) = 1.77, p(32→64) = 1.51 — the scaling is not
   a fixed power; it is falling from near-per-pair toward the per-gap–harmonic regime as the
   window grows.
2. **The convergence candidate:** form (d)'s constants decelerate (increments +0.151, +0.091;
   deceleration ratio 0.60) — the signature of convergence toward ≈ 0.9–1.0 from below. The
   harmonic pair-weight (the density-normalized form) is the FRONT-RUNNER AT NULL GRADE:
   three points cannot certify convergence, and the criterion was stated in advance —
   nothing promotes.
3. **The fourth point, re-priced:** K = 128 (R ~ 70) needs dps ≈ 1,200 with a 128×128
   factorization — **the fourth point rides D-3 (the blocked-factorization instrument); the
   normalization sub-problem and the full-power shape test now share one instrument build.**

## §4 — THE CLAUSE CHECK AND FILINGS

**The clause check rides the null (nothing promoted past its grade):** with no winner at
criterion, the template's three clauses are checked against the FRONT-RUNNER-AT-NULL-GRADE
only as candidacy notes — the harmonic pair-weight form is density-normalized (the currency
clause's shape ✓ as candidacy), pair-priced natively (the pricing clause ✓ as candidacy),
and its FE-point behavior untested at this depth (the symmetry clause: OPEN). **π₀'s
candidate row updates to: the relative pair-energy under the harmonic pair-weight
normalization, front-runner at null grade, convergence uncertified, the fourth point riding
D-3.** The construct-or-refute proper stays research-reach with this face's verdict as its
entry datum.

## CLOSING — pins, mirror, the handoff refreshed

**D-1's row in the direction map updates:** the entry face RUN; the null branch fired at the
pre-stated criterion; the spread filed (the declining exponent; the harmonic form's
decelerating constants); **the fourth point priced INTO D-3 — the mast candidate's next step
and the heavy instrument are now one build.** Keystone cargo accumulates (+ the
normalization verdict; touch not executed). **Consolidation DEFERRED, standing.**

| repo | pin |
|:--|:--|
| PLACE-papers | `0793a63` at open → this sitting's commit (D-1 row update + addendum) |
| SIDE-lv-conservation | main = `14720d9` — unmoved |
| SIDE-kernel | `44895f9`; v1.7 — unmoved |
| relay | this report's commit; instrument `tools/e16/d1_normalization.py` |
| rail | `de621b1` / `2147a03` — at the post-rename baseline |

Mirror rebuilt at the papers pin on commit. Nothing deposits.
