# The arithmetic-side validation runs — registrations first, then the run — 2026-08-05

Pins at open: PLACE-papers `6022ab0`; relay `ef65269`; lv `2f71068`; kernel `5e668b4`.
Rail at `de621b1` / `2147a03`. Nothing deposits.

**Completion protocol as filed: registrations restated VERBATIM first, then the number, then the
verdict mapped, with no interpretation beyond the mapping.**

---

## §0 — THE REGISTRATIONS, RESTATED VERBATIM BEFORE ANY NUMBER

### The three depth predictions, with their derivations

**(a) THE PRICING'S n ≈ 7000.** Derived from the corrected detection law against **this object's
own background**: `n = (1/log|z_out|)·log(2.5 · S∞(n))` with `1/log|z_out| = 586.4` at
γ = 16.290, δ = 0.4533, and `S∞(n) ≈ n log n` (the archimedean term of a degree-2 L-function,
N = 2). Iterating: 5000 → 6777 → 6973 → **converges to n ≈ 7000**.

**(b) R4'S MEASURED FIRST-NEGATIVE INDEX 3379**, at the *same* γ = 16.290 and δ = 0.4533.

> **IS R4'S SEQUENCE THE SAME OBJECT AS THE VALIDATION'S? NO — THEY ARE TWO CONSTRUCTIONS, AND
> THIS DETERMINES WHAT 3379 IS.** R4's λₙ is that of a **synthetic finite multiset**: 400 on-line
> ζ ordinates with one off-line quadruple *injected*. The validation's λₙ is that of the **actual
> disc −23 Epstein object**, computed from its own functional equation, with its own infinite zero
> set and its own archimedean term. **The backgrounds differ decisively:** R4's is the bounded sum
> over 400 points (scale ~10³, not growing); this object's is `S∞(n) ~ n log n`, which at n = 3379
> is already ~2.7×10⁴ and keeps growing. **So 3379 is a MEASUREMENT ON A DIFFERENT OBJECT, not a
> prediction for this one.** It is carried into the adjudication because the ferry requires all
> three to be compared, and it is labelled for what it is.

**(c) THE LOG-FORM n_det = (γ²/δ)·log(threshold × background) ≈ 5100.** Computed with
`background = 2400`, which is the **truncated-zero c_n scale** — **also not this object's
background.** Of the three, **only (a) was computed with the Epstein object's own background.**
That is recorded as a fact about the derivations, and it does **not** pre-select (a): the
adjudication rule below stands exactly as fixed.

### THE ADJUDICATION RULE, FIXED NOW, BEFORE ANY COMPUTE

**Tolerance: ±15% relative.** The three windows are disjoint:

| prediction | value | window |
|:--|--:|:--|
| (a) the pricing | 7000 | **[5950, 8050]** |
| (b) R4's measurement | 3379 | **[2872, 3886]** |
| (c) the log form | 5100 | **[4335, 5865]** |

- **A landing within tolerance of ONE, with the others outside → that one is SELECTED**, and the
  others are recorded as **superseded with the reason**.
- **A landing BETWEEN them, or OUTSIDE all three → FILES FIRST-CLASS and NO LAW IS SELECTED.**
- **No post-hoc derivation of a fourth prediction.**

### The by-product, registered and not claimed

**If the run yields a measured height–depth pair on this object, it is offered to BURIAL's
criterion as a candidate SECOND face. The criterion decides. No promotion follows from the run.**

---

## §1 — THE CENSUS, PARKED

**Parked at a clean record boundary.** Every record is fsynced individually, so the bank is
consistent at any stop point.

| | |
|:--|:--|
| records banked | **451** |
| complete rows (7 σ-cells) | **64** |
| contiguous, no gap, through | **t = 32.5** |
| partial row at stop | t_lo = 32.5, **2 of 7 cells** — resume completes the other five |
| **fixed dataset** | **t ∈ [0.5, 20.0], σ ∈ [0.52, 1.50] — well inside the completed range; it does not move** |

**Census resume command (verbatim):**

```
cd /d D:\relay && python tools\e16\epstein_census.py
```

---

## §2 — I-7, RE-CONFIRMED AT BOTH STAGES BEFORE THE FIRST COEFFICIENT

- **STAGE 1 (the statistic) — PASSES.** λₙ = Σ_ρ[1 − (1−1/ρ)ⁿ] contains ρ, real parts included;
  perturbing a real part moves it.
- **STAGE 2 (the pipeline) — PASSES.** Every number is computed from `E(s) = s(s−1)Λ(s)` evaluated
  on a circle about s = 1. **No zero location is an input at any point. The census file is never
  read by the validation script.**

**The radius was validated WITHOUT the census.** The Cauchy circle must contain no zero; rather
than look one up, the pipeline computes `c_m` at **two radii (0.4 and 0.25) and compares** —
agreement to **1.6×10⁻⁹** establishes that no zero lies inside either circle, from the function
alone.

---

## §3 — THE MATHEMATICS, SO THE PIPELINE IS CHECKABLE

`E(s) = s(s−1)Λ(s)` is entire, order 1, `E(s) = E(1−s)`, with zeros exactly Λ's nontrivial zeros.
Under `z = 1 − 1/s`:

> `log E(1/(1−z)) − log E(1) = Σ_{n≥1} (λₙ/n) zⁿ`

and with `log E(s) = Σ_m c_m (s−1)^m`, `(s−1) = z/(1−z)`, `[zⁿ] zᵐ(1−z)^{−m} = C(n−1, m−1)`:

> **λₙ = n · Σ_{m=1}^{n} c_m · C(n−1, m−1)**

The binomials are ~2ⁿ while λₙ ~ n log n, so the cancellation costs **~0.3n digits** — the cost
Johansson paid, and the reason the run is staged.

---

## §4 — THE SELF-TEST (known answer, banked before the first Epstein coefficient)

Run on **ζ**, whose λₙ are published — a genuine known-answer check that does not touch the census:

| | computed | published |
|:--|:--|:--|
| λ₁ | **0.02309570896612103** | 0.02309570896612104 |
| λ₂ | 0.09234573522804667 | 0.09234573526903794 |

**Sixteen digits on λ₁.** The run halts before the first Epstein coefficient if this fails.

**First Epstein values, at the pipeline's shallow end:** λ₁…λ₆ = 0.683, 2.469, 4.705, 6.674,
7.958, 8.640 — **all positive and rising**, as the archimedean term requires at shallow n.

---

## §5 — THE RUN, LAUNCHED

**Staged, per-record banked, resume-with-validation.** Stages `(nmax, dps)`:
(120, 120) · (300, 220) · (700, 450) · (1500, 900) · (3000, 1600) · (5000, 2400) ·
**(7000, 3200)** · (9000, 4000) — precision ≈ 0.3n digits plus headroom.

**At each checkpoint the bank records** `nmax`, `dps`, the running minimum of λ, its argmin, and
**the first negative index if one exists**, and the console reports **the sign of the running
minimum**.

**RESTART COMMAND (verbatim, safe to re-run at any time):**

```
cd /d D:\relay && python tools\e16\epstein_li_validation.py
```

Bank: `D:\relay\tools\e16\epstein_li_bank.jsonl`. **Sleep posture:** `STANDBYIDLE` AC index
`0x00000000` — unchanged, no idle sleep.

**STATUS AT THIS REPORT: LAUNCHED AND RUNNING. NO CHECKPOINT HAS YET REPORTED A NEGATIVE λ, AND
NO VERDICT IS AVAILABLE.** The adjudication of §0 is fixed and will be applied to the first
negative index when a stage reports one — **not before, and not to a partial result.**

**The stages beyond 7000 exist so that a null is distinguishable from a shortfall:** if λ stays
positive through n = 9000, that is a result about this object at the depth reached, and it will be
reported as such rather than as a failure of any prediction.

---

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `6022ab0` — unmoved this pass |
| relay | `ef65269` → this report's commit |
| SIDE-lv-conservation | `2f71068` — unmoved |
| SIDE-kernel | `5e668b4` — unmoved |
| rail | `de621b1` / `2147a03` — unmoved |

Nothing deposits.
