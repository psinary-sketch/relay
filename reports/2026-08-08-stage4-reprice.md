# THE STAGE-4 RE-PRICE — on measured inputs — 2026-08-08

The ruled boundary. Stage 3 banked; the worker is at the entry to stage 4. **This filing prices;
it does not decide.** Rail at `de621b1` / `2147a03`. Nothing deposits.

---

## §0 — THE MEASURED INPUTS (not modelled)

**Stage 3 (nmax = 1500, dps = 900) completed in ~30 h wall at CPU/wall = 0.997**, and its internal
split is the fact everything below turns on:

| phase | measured | share |
|:--|--:|--:|
| **boundary (pointwise Cauchy evaluation)** | **~26 h** | **~87%** |
| coefficient extraction | ~3.5 h | ~12% |
| recurrence | minutes | <1% |

**The dominant cost is NOT the O(n²) recurrence the original pricing feared. It is the 3002
pointwise evaluations of E(s), each ~40 incomplete-gamma pairs at 900 digits.** Measured
per-value rates across four independent samples: 34.3 · 21.4 · 29.4 · 35.2 s.

**Stage bank at the boundary:** stages 0–3, running minimum **0.682682 at n = 1**, first negative
index **none** through n = 1500 — **far below every prediction window** (the lowest opens at 2872),
so **nothing is adjudicable and no verdict is implied.**

---

## §1 — THE THREE OPTIONS

### (a) CONTINUE AS BUILT

Scaling the measured split — boundary as M·dps, coefficients as M²·dps:

| stage | nmax / dps | projected |
|:--|:--|--:|
| 4 | 3000 / 1600 | **~5 days** |
| 5 | 5000 / 2400 | **~14 days** |
| 6 (registered depth) | 7000 / 3200 | **~29 days** |
| **cumulative to n ≈ 7000** | | **~48 days continuous** |

**Stated as a LOWER BOUND.** mpmath's `gammainc` cost is superlinear in precision, so the true
figure is worse. **Affordable only as a calendar decision the author owns.**

### (b) HALT-AS-SHORTFALL

Files at **n = 1500, positive throughout**. **Explicitly NEVER a null — no window was entered**,
so the run reached a depth at which all three predictions agree and none is distinguished.
**The exclusion by-product keeps its banked reach: real zeros with β > 0.50170 excluded, exact and
phase-free.** The experiment re-opens whenever the platform improves; the dataset, hold-aside and
windows are all already fixed and would carry over unchanged.

### (c) RE-PLATFORM — **AND THE MECHANISM AS FRAMED DOES NOT TRANSFER**

**The ruling priced (c) as *series arithmetic replacing pointwise Cauchy evaluation*. I checked the
function that route depends on before pricing on it, and it is the wrong variable.**

> `acb_hypgeom_gamma_upper_series` — *"sets res to an upper incomplete gamma function where **s is
> a constant and z is a power series**, truncated to length n."*

**The computation needs the series in `s`, the FIRST argument** — Λ(s) = Σ_k r_k[a^{−s}Γ(s,a) +
a^{s−1}Γ(1−s,a)] is expanded about s = 1 with `a` fixed. **Arb's routine supplies the series in the
SECOND argument. It is not the series this object needs.** The route that makes Arb's Keiper–Li
computation fast for ζ is `acb_poly_zeta_series` — **a native ζ-series routine with no Epstein
analogue**; the Epstein Λ's s-series would require derivatives ∫_a^∞ (log t)^m t^{s−1}e^{−t}dt,
which Arb does not supply as a function. **Compounding it: python-flint exposes the scalar
`gamma_upper` but the search surfaced no binding for the `_series` variant at all.**

**So (c) as written is refused on its mechanism, not on its cost.** In its place:

### (c′) RE-PLATFORM AT THE SCALAR LEVEL — the option that survives the check

**Keep the Cauchy method; replace mpmath's `gammainc` with python-flint's `acb.gamma_upper`.**

- It attacks **exactly the measured dominant cost** — the 26 h boundary phase is ~120 000
  incomplete-gamma evaluations at 900+ digits, and Arb is typically 10–100× faster than mpmath at
  high precision.
- **It needs only the binding that is confirmed exposed**, no series machinery, no new mathematics.
- **The algorithm is unchanged**, so the existing gate, chunk format and banked stages remain
  meaningful rather than being invalidated by a rewrite.
- Named costs: the **python-flint dependency (verified ABSENT on this machine, installable)** and a
  **contained edit to `Lam_eps` and the precision plumbing** — not a rewrite of the coefficient
  stage.
- **Honest uncertainty: the speedup factor is not measured, only expected from the library's
  general reputation. A one-hour benchmark at stage-3 precision would price it exactly, and that
  benchmark should precede any commitment.**

---

## §2 — RECOMMENDATION, RECORDED AS SUCH

**(c′), preceded by the benchmark.** Not (c) — its mechanism does not apply to this object. Not
(a) as a first move: **a 5-day stage-4 spend against an undecided platform question is precisely
the sunk-cost shape the power clause exists to prevent**, and the ruling's instinct to refuse
parallel running is right for the reason it gave — machine contention with the build's validation
gates.

**(b) remains the honest fallback and is not a failure state**: a shortfall filed at n = 1500 with
its by-product intact is a real deliverable, and it is what (c′) failing its benchmark should
produce.

---

## §3 — THE GATES, IF A RE-PLATFORM IS RULED

Stated now so the build inherits them rather than negotiating them later:

1. **Known-ground gate on BOTH objects, before any new depth.** The new engine must reproduce
   **ζ's λ₁ at its recorded precision** (0.02309570896612103, rel_err 1.5×10⁻¹⁵) **and stages 0–3's
   banked Epstein values within stated tolerance.** The second is the stronger test and is
   available only because those stages are banked.
2. **The registered experiment does not change because the platform does.** The dataset declaration
   (t ∈ [0.5, 20.0], σ ∈ [0.52, 1.50]), the hold-aside rule, the three windows with their ±15%
   tolerance, the one-period phase extensions, the [5950, 5967] ambiguity strip, and the
   below-windows routing to the low-t/real-zero check **all carry over unchanged.**
3. **Rule 2 from the first production run:** intra-stage banking with the tail guard, and detached
   launch — now the pattern of record on two verified confirmations.

---

## §4 — THE WORKER MEANWHILE

**Continues into stage 4 only if (a) is ruled. Otherwise it stops cleanly at the stage-3 bank on
the ruling.** Either way the detachment evidence keeps its grade: **30 unbroken hours at CPU/wall
0.997**, which stands as the second verified confirmation regardless of what happens to the
validation.

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `3d38757` → this pass's commit |
| relay | `595ef82` → this report's commit |
| kernel `5e668b4` · lv `2f71068` · rail `de621b1` / `2147a03` | unmoved |

**The ruling is the author's.** Census parked at 451 records. Nothing deposits.

## SOURCES

- [`acb_hypgeom.h` — Arb/FLINT documentation](https://flintlib.org/doc/acb_hypgeom.html) — the
  `gamma_upper_series` signature (series in the second argument)
- [python-flint `acb` documentation](https://python-flint.readthedocs.io/en/latest/acb.html) — the
  exposed scalar `gamma_upper`
- [Johansson, *Rigorous high-precision computation of the Hurwitz zeta function and its derivatives*](https://arxiv.org/pdf/1309.2877)
