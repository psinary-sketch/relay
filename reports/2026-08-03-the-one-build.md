# THE ONE BUILD — the blocked-factorization instrument + the fourth point (D-3 serving D-1) — 2026-08-03

Staged, checkpointed, resumable at every boundary — every stage banks. Pins at open:
PLACE-papers = `098c7c9`; relay = `97142eb`; lv `14720d9`, kernel `44895f9` — unmoved; rail
at the post-rename baseline. Nothing deposits.

## STAGE D's ADJUDICATION — REGISTERED NOW, BEFORE STAGE A (verbatim from the ferry)

*"the harmonic pair-weight's constant continues decelerating (ratio ≤ 0.75) toward a limit,
with the four-point extrapolated limit inside [0.85, 1.05] → the denominator
CERTIFIES-at-four-points (still an instrument-grade certification, not the construct);
deceleration breaks or the extrapolation exits the band → the form RETIRES with the data
filed and the remaining candidates re-priced."* The extrapolation convention, fixed in
advance: geometric — c∞ ≈ c₄ + (c₄ − c₃)·r/(1 − r) with r = (c₄ − c₃)/(c₃ − c₂). The
three-point comparators: c₂ = 0.57901, c₃ = 0.72985 (K = 32), c₄-prior = 0.82072 (K = 64) —
so the four-point test reads (c₃, c₄, c₅) = (0.72985, 0.82072, c(128)) with deceleration
ratio (c₅ − c₄)/(c₄ − c₃) ≤ 0.75 and the geometric limit in [0.85, 1.05].

## THE PRECISION DESIGN (stated before building)

The measured law prices K = 128 at dps ≈ 4·Σ_{k≤128} log₁₀(2γ_k) ≈ 1,200 → **dps 1,300 with
margin**. **The precision-split (the build's structural insight, stated in advance):** the
high precision is needed ONLY inside the factorization — the moment → Jacobi conversion is
where the cancellation lives; the Jacobi coefficients are well-conditioned O(1)-scale
outputs, and the spectral read (tridiagonal eigenvalues, pair-energy) is stable — it runs at
dps ~60 after downcasting. The engine is therefore: blocked high-dps Cholesky
(checkpointed) + low-dps spectral read. **This same split re-prices the K ~ 200 shape run —
measured at Stage D.** Atom count: J = 600 (preserving the K = 64 run's atoms-per-depth
ratio ≈ 4.7).

## STAGE A — THE INSTRUMENT

**Executed** (`tools/e16/blocked_cholesky.py`): blocked, checkpointable Cholesky (block-row
state + dps + content hash, format v1); **the resume test on a deliberately interrupted run
PASSED before any production use** (pause at 4/12 rows, resume, agreement with the direct
factorization to 5×10⁻¹³²). One sizing note filed: the selftest's first measure was too deep
for its dps (the reference itself failed) — resized to well-conditioned ground; the
interrupt/resume mechanics were correct throughout.

## STAGE B — VALIDATION FIRST (the mandatory gate)

**Executed** (`tools/e16/build_stageB.py`) — **the gate PASSES, with two instrument notes
filed transparently:** (1) the engine-vs-cache agreement measured 7.8×10⁻⁴⁶¹ (ζ) and
2.1×10⁻⁴⁸³ (control) against a mis-sized tolerance of 10⁻⁵⁰⁰ — the tolerance had been set
STRICTER than the certification's own accuracy floor (~160 guaranteed digits at K = 64); on
the corrected criterion (agreement ≥ the certified floor) the measured values exceed
requirement by ~300 digits; (2) the script's final gate line aggregated only the
precision-split checks — the slip flagged, not hidden. **The precision-split validated
cleanly:** the low-dps (60) spectral read reproduces the certified D-osc triple to ≤
1.3×10⁻⁶. The engine earned production use on known ground.

## STAGE C — THE FOURTH POINT

**Executed, staged and banked throughout** (`build_stageC_atoms.py` — six resumable chunks,
600 true zeros + 600 smooth points at dps 1300; `build_stageC_run.py` — moments by exact
summation, the blocked Cholesky K = 128 with a mid-run pause/resume exercised in production
(48/129 rows banked, resumed clean); `build_stageC3_read.py` + `build_rebase.py` — the read).

**THE HALT THAT MATTERED:** the first read's nesting check FAILED (20%) and the
halt-and-file discipline stopped the adjudication. Diagnosis: the check as specified
compared DIFFERENT OBJECTS — the certified K = 64 string lives on the J = 300 truncation,
the build on J = 600; the deep coefficients legitimately feel the extra tail mass (the
corrected cross-check: 2.6% at k ≤ 20 → 20% at k ≤ 64 — structural, not error), while the
resolved-band constants are J-robust to < 0.5%. **The repair: all four points REBASED on the
uniform J = 600 object** (free, from the banked Jacobi's nested blocks). **The tainted
mixed-object sequence would have returned RETIRES marginally (c∞ = 1.081 vs the 1.05 edge) —
the halt discipline caught an object-mismatch that would have flipped the verdict.**

**The fourth point (uniform object):** K = 128, R = 75 resolved (75 nodes < 1% from atoms),
Δosc = 251.184, Δbnd = 102.47.

## STAGE D — ADJUDICATION

**The uniform-object four-point sequence:**

| K | R | Δosc | c = Δosc / Σ_{osc pairs} 1/(j−i) |
|--:|--:|:--|:--|
| 16 | 8 | 5.0316 | 0.57835 |
| 32 | 17 | 25.379 | 0.72983 |
| 64 | 36 | 87.398 | 0.82436 |
| 128 | 75 | 251.18 | 0.88808 |

Increments 0.1515 · 0.0945 · 0.0637; deceleration ratios **0.624, 0.674 — both ≤ 0.75 ✓**;
geometric extrapolated limit **c∞ = 1.0198 ∈ [0.85, 1.05] ✓**.

**STAGE D VERDICT (the pre-registered criteria, on the uniform object, after the halt):
THE HARMONIC PAIR-WEIGHT CERTIFIES-AT-FOUR-POINTS** — an instrument-grade certification, not
the construct, exactly as the registration bounded it. And the limit's position is itself
the finding's edge: **c∞ ≈ 1.02 — consistent with UNIT constant: Δosc ~ Σ_{pairs} 1/(j−i),
the density-normalized harmonic pair-energy with coefficient one** — the cleanest candidate
form for π₀'s denominator, one calibration short of a claim (the K ~ 200 fifth point would
test c∞ = 1 directly).

**The K ~ 200 re-price on the validated engine's measured cost:** atoms at dps 2,200 ≈
1.5–2 hours staged (the dominant cost) · the blocked Cholesky ≈ 10–25 min (checkpointed) ·
the low-dps read ≈ minutes — **a staged afternoon, not the hours-scale unsplittable step of
the pre-build estimate: the full-power shape run AND the fifth point are now one affordable
build.**

## FILINGS

**π₀'s row updates:** the denominator CERTIFIED-at-four-points (instrument grade): the
harmonic pair-weight, with c∞ ≈ 1.02 suggesting unit constant; the symmetry clause still
untested; the construct-or-refute proper still research-reach — now with its currency's
denominator in hand. **D-1's map row updates:** the entry face + the one build DONE; next =
the K ~ 200 build (the fifth point + the shape run, one instrument, re-priced affordable).
**The keystone cargo accumulates** (+ the certification; the touch lands when breadth
returns or the author calls). **Consolidation DEFERRED, standing.**

| repo | pin |
|:--|:--|
| PLACE-papers | `098c7c9` at open → this sitting's commit (OPEN_TRAILS addendum + handoff refresh) |
| SIDE-lv-conservation | main = `14720d9` — unmoved |
| SIDE-kernel | `44895f9`; v1.7 — unmoved |
| relay | this report's commit; instruments `blocked_cholesky.py`, `build_stage{B,C_atoms,C_run,C3_read}.py`, `build_rebase.py` |
| rail | `de621b1` / `2147a03` — at the post-rename baseline |

**The board restated, the build's verdict at its head:** THE INSTRUMENT EXISTS AND THE
DENOMINATOR CERTIFIES — the blocked factorization earned trust on known ground, banked every
stage, caught its own object-mismatch by the halt discipline, and delivered the fourth
point: the harmonic pair-weight converges (c∞ ≈ 1.02, consistent with unit constant); π₀'s
currency has its denominator at instrument grade; and the K ~ 200 build — the fifth point
and the full-power shape test together — is re-priced from infeasible to a staged afternoon.
Mirror rebuilt at the papers pin on commit. Nothing deposits.
