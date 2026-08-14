# `prolate_layer.py` — the CC substrate, rebuilt, pinned, and certified

**Banked 2026-08-14. Pins supplied 2026-08-14 (part 2).** ### **15 / 15 reachable battery rows PASS.**

## Why it exists

The sitting-11/12 instrument was **never banked**: the twenty sittings of 2026-08-13 produced twenty-four
relay reports and no code. The `δ/L` law was filed `MEASURED-AT-BANK` with **no bank**. This rebuilds the
substrate from primary definitions and certifies it against the banked numbers. **It is tracked, so it cannot
be lost the way the original was.**

## The convention pins — without which nothing identifies

The first certification pass **failed every CC-facing row** and reported the banked record as
self-contradictory. ### **That report was wrong.** The rebuild was correct; three conventions were missing.
They are the whole difference between "the record contradicts itself" and "15/15 pass".

| pin | content |
|:--|:--|
| **P1** | CC's `λ(n)` are the **EVEN-INDEXED** truncated-Fourier eigenvalues, signed: `λ(n) = (−1)ⁿ√(μ_{2n})`, `c = 2π`. **The concentration eigenvalues this file computes are `λ(n)²`, and CC's sum of squares runs over even indices only.** *Selecta footnote 10: "We are only using the even prolate functions, the sum of squares of eigenvalues including the odd ones is 4."* Remark 4.5: `δ(1) = Σλ(n)² = 2(Si(4π)/4π + 1)`. |
| **P2** | Norm convention, eq. (16): `‖ξ‖² = ∫₀^∞|ξ|²` — half-line, even functions. For an even function supported in `[−1,1]` this is half the full-line norm, so **`ξ_n = √2 · ψ_{2n}`**. |
| **P3** | `ξ_n = P₁φ_n/‖P₁φ_n‖` under P2; `ξ_n^an` via `η_n = Fξ_n = λ(n)·ξ_n^an`. |

## What it computes

The time-and-band limiting operator on `[−1,1]` at the corpus's fixed `c = 2π`,

```
(Q f)(x) = ∫_{-1}^{1} sin(c(x−y)) / (π(x−y)) · f(y) dy
```

by Gauss–Legendre quadrature; then the CC layer under P1–P3. `ξ_n(1)` comes from the eigenfunction equation
itself, `ξ_n(1) = (1/λ_n)∫K(1,y)ξ_n(y)dy` — **not extrapolated from the grid.**

`t(n)` is **not fitted.** Correction 13 states the ε assembly "was computing `Σλ²/(1−λ²)` exactly" and
sitting 9 states "the missing factor was `ξ_n(1)²`". So

```
t(n) = λ(n)² ξ_n(1)² / (1 − λ(n)²)
```

is the corpus's own sentence, written down and evaluated. It reproduces all five CC Lemma 5.4 values.

## Certification: 15 / 15 reachable rows PASS

| row | computed | target | \|Δ\| |
|:--|--:|--:|--:|
| `Σ μ_k` *(all, incl. odd)* | `4.000000000` | `4` — footnote 10 | `8.9e-16` |
| **`Σ λ(n)²`** *(even only)* | `2.237484834` | `2.237484835` — Remark 4.5 | **`5.8e-11`** |
| **`Σ λ(n)² ξ_n(1)²`** | `2.000000000` | `2` exactly | **`3.6e-15`** |
| `ξ_0(1) … ξ_5(1)` | `0.02618, 0.60948, 2.41323, 3.52614, 4.09936, 4.57184` | sitting 9 row (v) | `≤ 5.0e-06` |
| **`t(0) … t(4)`** | `11.9719, 8.77574, 2.20528, 0.0433983, 0.000125459` | CC Lemma 5.4 | **`≤ 3.2e-05`** |
| **`ε′(1⁺) = Σ t(n)`** | `22.9964757` | `22.996476` | **`3.2e-07`** |

**The `8733` row, reclassified and confirmed both ways:** the pre-correction artifact `μ₀²/(1−μ₀²)` = **8733.4**
(the concentration eigenvalue mistaken for `λ(0)`, then squared); the corrected `Σλ²/(1−λ²)` over even indices
= **17491.3**, against sitting 13's `≈ 17491`. **Both reproducible to five figures.**

## Boundary — what is still unreachable

`Q_ε` (**eq. 100**), the `Y₊` map and the lag form are **not on disk**. Therefore the remaining battery rows
are not computable here:

`ε(1) = 0` · `Qε(1) = 0` · the log-2 spectrum · the log-3 no-prime spectrum · the `L = 3` negative fractions ·
the five-point `δ/L` table · `C = 0.3448` · the endpoint machine-zeros.

> **These are exactly the rows the `δ/L` law depends on.** The substrate beneath them is now certified; the
> operator layer above them is still unbuilt. **Supplying eq. (100) verbatim closes the gap — nothing else is
> missing.**

## Run

```
python prolate_layer.py 400 700     # the raw prolate layer
python -c "import prolate_layer as p; [print(r) for r in p.battery()]"
```

`numpy` for the eigenproblem; `mpmath` once for `Si(4π)`. No scipy.
