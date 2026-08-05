# Roster · the λₙ decomposition registered · the census repriced · the formula sweep — 2026-08-05

Pins at open: PLACE-papers `3c1a8d5`; relay `fb97935`; lv main `2f71068`; kernel `44895f9`.
Rail at the post-rename baseline. Nothing deposits.

---

## §1 — INSTRUMENTS.md JOINS THE MIRROR ROSTER (author-called)

Added to the build. **The manifest's roster line is now DERIVED at build time**, not authored:
the script stores the previous build's roster beside itself and diffs the roster this build
actually assembled.

```
ROSTER CHANGE, THIS BUILD (2026-08-05): 21 files.
  ADDED:   INSTRUMENTS.md
This line is computed at build time by diffing the assembled roster against the
previous build's, not carried forward as authored text.
```

**Two defects found and fixed in the building of it, both instances of the description rule.**
(1) The first run had no stored roster, so it reported **all 21 files as ADDED** — true of the
diff, false of the world. Fixed with a bootstrap guard that says no previous roster was recorded
rather than inventing a change. (2) The state file was then seeded with the real 20-file roster
at its real date (2026-08-04), so the rebuilt manifest reports the one genuine change.

**Verified in the mirror, not the repo** — five exact strings drawn from I-7's own text, probed
against the extracted zip:

| probe | in zip |
|:--|--:|
| `I-7 — THE PLACEMENT SCREEN` | 1 |
| `I-7's SECOND RUN` | 1 |
| `STAGE-2 TEST (the pipeline) — SUBSTITUTION` | 1 |
| `1200 copies of a single ordinate` | 1 |
| `n_det = (γ²/δ) × log(threshold × background)` | 1 |

**The screen reaches the reviewer mirror.** 22 files in the zip (21 + manifest).

---

## §2 — THE λₙ DECOMPOSITION, READ AT SOURCE — THE MAP HOLDS, THE BAR DOES NOT

Source: **Lagarias, *Li coefficients for automorphic L-functions***, Ann. Inst. Fourier 57 (2007)
1689–1740; arXiv math/0404394.

**The decomposition, at cite.** λₙ(π) = **S∞(n, π∨) − S_fin(n, π∨) + δ(π∨)** — an archimedean
term from the local factor at infinity, a finite term from the Euler product over primes.

- **Archimedean, unconditional (Thm 5.1):** S∞(n, π) = **(N/2)·n log n + C₁(π)·n + O(1)**, with
  C₁(π) = (N/2)(γ − 1 − log 2π) + ½ log Q(π). **It depends only on the Γ-factor and the
  conductor** — no arithmetic enters.
- **Finite, unconditional (Thm 6.1):** S_fin(n, π) = **λₙ(√n, π∨) + O(n log n)** — the *incomplete*
  Li coefficient at height **√n**.
- **Finite, under RH:** S_fin = **O(√n log n)**. Without RH the incomplete term "will sometimes be
  very large, **of size exponential in n**."

**THE MAP ONTO HEAD 2 HOLDS, and cleanly.** The archimedean term is the density/drift half —
smooth, positive, growth-carrying, knowing only what the functional equation supplies (which also
makes it a head-4 free-layer object). The finite term is the arithmetic oscillation, and it is
exactly where off-line zeros appear, exponentially. **This is the corpus's own density-mean /
arithmetic-oscillation decomposition, in the literature, for λₙ.**

**BUT THE REGISTERED INFERENCE DOES NOT FOLLOW, and this is the pass's finding.** The
registration read: *if the map holds, the R4 compression question reduces to bounding the
arithmetic oscillation, which head 2's screen says the density register cannot supply — so R4's
cell comes back BARRED BY ARGUMENT.*

**The reduction is real:** λₙ ≥ 0 for all n ⟺ S_fin(n) ≤ S∞(n) + δ for all n, and since S∞ is
known unconditionally, **the compression question is exactly a question about the arithmetic
term.** That much is established.

**The bar is not.** Checking λₙ ≥ 0 for n ≤ N gives S_fin(n) ≤ S∞(n) for n ≤ N — **finitely many
constraints on the arithmetic term itself.** That is not a density→placement inference, so
**head 2's screen does not apply to it**: the data on both sides of the implication live in the
arithmetic register. What would bar it is a statement that finite arithmetic data cannot control
infinite arithmetic data — which is **head 1** (certified closure), and head 1 is precisely the
head that says R4 is the one register where the question is *askable*. **The reduction sharpens
R4; it does not close it.**

**A THIRD OUTCOME, which the registration did not name, and which files as found.** Neither
branch fires as written: the map holds (so not branch b) and the bar fails (so not branch a).
Branch b's alternative clause — *"the arithmetic part is bounded by known results"* — is
**half-true in a way that matters**: it is bounded, **but only under RH** (O(√n log n)).
Unconditionally it is tied to an incomplete Li coefficient and can be exponentially large. **A
bound that assumes RH cannot be used to establish a criterion for RH**, so the clause does not
close the question either.

**THE SHARPEST THING THE CITE GIVES, and it corrects last pass's filing.** Unconditionally
S_fin(n) = λₙ(**√n**) + O(n log n): **λₙ at depth n is governed by zeros up to height √n.** So
verifying λₙ ≥ 0 for n ≤ 10⁵ probes off-line zeros only to height **γ ≈ √(10⁵) ≈ 316** — and, run
through the detector's corrected law (n ≈ (γ²/δ)·log(background)), only to **γ ≈ 65 at δ = 0.5**.
**Direct verification of ζ's zeros on the line has reached height ~10¹³.** Johansson's range is
therefore a *far weaker* constraint on off-line zeros than direct zero-checking already provides.

**F.2026-08-05-j is corrected accordingly:** the claim that "outcome-shape 2 now has 10⁵
certified-positive coefficients standing against it" **overstated the constraint.** The honest
statement is that the Li range constrains a height band already excluded by direct computation,
so it adds **essentially nothing** against a counterexample-shape. Outcome-shapes 1 and 3 remain
untouched, as filed.

**The sitting stays REGISTERED AND UNRUN**, with its job now stated: prove or refute that finite
constraints on S_fin control it globally — a head-1 question, not a head-2 one.

---

## §3 — THE VALUABLE CENSUS EXPERIMENT, PRICED PROPERLY (pricing only)

**The experiment.** Li-type coefficients for the disc −23 Epstein object computed **from its
functional equation and Taylor data alone** — Λ_Q(s) = (√23/2π)^s Γ(s) Z_Q(s), Λ_Q(s) = Λ_Q(1−s)
— with the zero census held aside as ground truth and **never entering the computation**.

**I-7 CHECKED AT BOTH STAGES BEFORE ANY COMPUTE IS AUTHORIZED — and this is the first proposal in
the family to pass both.**

| stage | test | result |
|:--|:--|:--|
| 1 — the statistic | perturb the real parts; does λₙ move? | **PASSES.** λₙ = Σ_ρ[1 − (1−1/ρ)ⁿ] contains ρ, real parts included (face 1) |
| 2 — the pipeline | substitute the object's data; does the verdict change? | **PASSES.** The pipeline reads Λ_Q's Taylor coefficients; a different object's Taylor data gives a different answer, and **no zero location is an input at any point** |

**Predicted negativity depth, stated in advance from the corrected law.** With the located witness
(γ = 16.290, δ = 0.4533, 1/log|z_out| = 586.4) against the archimedean background
S∞(n) ≈ n log n (N = 2), solving n = 586.4·log(2.5·n log n) converges to

> **n ≈ 7000** — the depth at which λₙ for the Epstein object should first go negative.

**Cost.** Taylor coefficients of log Λ_Q at s = 1 to order 7000, then the O(n²) Li recurrence,
all at working precision ~n digits (Johansson's scaling: n = 10⁵ needed 2 900–33 000 digits and
~10¹⁰ bits). Estimate: **~10⁴ digits of working precision, ~5×10⁷ high-precision operations —
order of days of compute**, dominated by the recurrence rather than by the Epstein evaluations.
The census itself (T = 100, ~4.7 h) is a small fraction of the total.

**A limit on the reach, and it is worth stating because it cuts against the instrument's headline
number.** The 26× Toeplitz depth economy **does not transfer to this experiment.** The Toeplitz
detector needs cₙ = Σ_ρ zⁿ, and c₀ diverges — on the arithmetic side the computable object is λₙ
itself. Only differences cₙ − c_m = λ_m − λ_n are available, and a Toeplitz matrix built from
c₀…c_{K−1} needs the divergent c₀. **So the arithmetic-side experiment is back to the sign
detector at n ≈ 7000, not K ≈ 270.** Whether a Toeplitz-type test can be reconstructed from
differences alone is an open sub-question, not assumed either way.

**Why it is nonetheless the only experiment in the family worth opening:** it is the only one in
which **a known-answer object is measured by a pipeline that never sees an answer** — which is
exactly what would license the arithmetic-side channel on ζ. **Named, priced, NOT RUN. Author's
call.**

---

## §4 — THE FORMULA-PROVENANCE SWEEP

Instrument: `tools/audit/formula_provenance_sweep.py`. Five living documents swept.

**240 distinct quantitative formulas; 183 (76%) carry a verification provenance within ±2 lines;
57 (24%) carry none.** The instrument's own limits are printed above its output: proximity is a
proxy, so a formula checked in a relay report three paragraphs away reads as unprovenanced. **The
output is a work-order list to be read by hand, not a verdict.**

**The seed's neighbourhood is the largest cluster.** VERIFICATION_LOOM §2142–2183 — the Li/Weil
analysis block — contributes six of the flagged formulas, including the §2165 line corrected this
week. **The correction made this week is the first verification that block has ever had.**

**Work-orders, ranked by what they carry:**

| # | formula | where | note |
|--:|:--|:--|:--|
| 1 | `E_quad(n) = 4 − 2(rⁿ+r⁻ⁿ)cos(nφ)`, `n ≈ 2γ²/ε` | LOOM §2161–2165 | the seed; the depth clause corrected this week, the rest of the block still unchecked |
| 2 | `S_n = wⁿ + w⁻ⁿ`, `w = 1−1/ρ` | LOOM §2168, §2183 | the Cayley identity the whole block rests on |
| 3 | `λ_n ≥ 0 is the Weil functional on the Li test function` | LOOM §2170 | a structural identification, checkable at cite — **and §2 above is that check, partially** |
| 4 | `Ω_b = n₁^n₃ / n₂^(n₁+n₃) = 4/81` | LOOM §987, FINDINGS §421, OPEN_TRAILS §196 | a physics-side numeric claim appearing in three places with no check recorded at any |
| 5 | `d(K) = 2^(r₁+r₂+2)`, `total = 7 for every ζ_K` | FINDINGS §49–53 | arithmetic claims over number fields |
| 6 | `δ ≈ 2×10⁻²³ at 50 digits` | INSTRUMENTS §204 | **filed this morning; closed below** |

### §4a — The first work-order closed in the same pass, and it corrects my own filing

INSTRUMENTS recorded the detector's precision limit as *purchasable as √floor — at 50 digits the
same order reaches δ ≈ 2×10⁻²³.* **The 2×10⁻²³ was extrapolated from a scaling law that had never
itself been checked.** The sweep flagged it; I checked it.

**Measured, by changing precision by a known factor (float32 vs float64, ε ratio 5.37×10⁸):**

- **Claim (i) — floor ∝ ε: MEASURED AND WRONG AS FILED.** The floor moved by 2.44×10⁷ against a
  predicted 5.37×10⁸, giving **floor ∝ ε^0.846**, not ε¹.
- **Claim (ii) — δ_min ∝ √floor: NOT MEASURABLE BY THIS DESIGN.** At K = 400 the float32 arm
  cannot detect even the gross witness (δ = 0.4533 needs a signal of 0.0264 against a float32
  floor of 5.1×10⁻³, and the rule demands 100×), so δ_min is not bracketed and no exponent can be
  fitted. **The exponent ½ stands on the separately *measured* δ² signal law, not on this test.**

**Composing: δ_min ∝ ε^(0.846 × 0.5) = ε^0.423**, which re-derives the 50-digit figure as

> **δ ≈ 9×10⁻²¹, not 2×10⁻²³ — the filed figure was optimistic by a factor of ~440.**

**The correction is itself weakly grounded and is filed with that caveat:** two precisions give
one exponent with no error bar, and the law is being applied ~34 orders of magnitude outside the
range it was measured in. **Both the old figure and the new one are extrapolations; only the
δ² signal law and the float64 floor are measurements.** INSTRUMENTS is corrected to say so.

**The sweep's own verdict on itself:** it found 57 candidates, of which the one I could check
turned out to be genuinely defective. That is one confirmed positive out of one examined, which
is not a precision estimate — and by the standard applied to the triviality pre-screen two passes
ago, **no claim is made about the list's hit rate.** The list files as work-orders.

---

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `3c1a8d5` → this pass's commit |
| relay | `fb97935` → this report's commit |
| SIDE-lv-conservation | main = `2f71068` — unmoved |
| SIDE-kernel | `44895f9` — unmoved; the generalization work-order still open at the author's call |
| rail | `de621b1` / `2147a03` — at the post-rename baseline |

R4 registered and unrun. Consolidation DEFERRED. Nothing deposits.

## SOURCES

- [Lagarias, *Li coefficients for automorphic L-functions*](https://ar5iv.labs.arxiv.org/html/math/0404394) — the archimedean/finite decomposition, Thms 5.1 and 6.1
- [Johansson, *Rigorous high-precision computation of the Hurwitz zeta function and its derivatives*](https://arxiv.org/pdf/1309.2877)
- [Coffey / Li-coefficient asymptotics, Selberg class](https://www.sciencedirect.com/science/article/pii/S0022314X10002428)
