# `prolate_layer.py` — the prolate substrate, rebuilt and certified

**Banked 2026-08-14.** A partial resurrection of the sitting-11/12 apparatus, and the diagnostic that
found a contradiction inside the banked record.

## Why it exists

The sitting-11/12 instrument was **never banked**. The twenty sittings of 2026-08-13 produced twenty-four
relay reports and no code; nothing under `relay/tools` postdated 2026-08-12. The `δ/L` law was filed
`MEASURED-AT-BANK` with **no bank**.

This file rebuilds the part of that apparatus that can be rebuilt **from primary definitions the executor
can actually read** — the classical Slepian prolate layer — and certifies it against the numbers the relay
reports banked.

## What it computes

The time-and-band limiting operator on `[-1,1]` at the corpus's fixed `c = 2π`:

```
(Q f)(x) = ∫_{-1}^{1} sin(c(x-y)) / (π(x-y)) · f(y) dy
```

Gauss–Legendre quadrature; eigenvalues `λ(n)`; prolate spheroidal wave functions `ξ_n` at
`L²[-1,1]` normalisation. Endpoint values `ξ_n(1)` come from the eigenfunction equation itself,
`ξ_n(1) = (1/λ_n)∫K(1,y)ξ_n(y)dy` — **not extrapolated from the grid.**

`c = 2π` is the corpus's own fixed value (sitting-4 correction: *"Landau–Widom inapplicable — `c = 2π` is
fixed"*), and is what "concentrated in `[-1,1]` in both position and frequency" gives under the
`e^{2πixy}` convention.

## Certification result

| battery row | verdict |
|:--|:--|
| **`λ(n)` themselves** | ### **PASS** — `λ(0) = 0.999942753`, giving `λ(0)²/(1−λ(0)²) = 8733.39` against the corpus's independently banked **8733** (sitting 11, correction 8). Five significant figures. **The prolate eigenvalues are the corpus's `λ(n)`.** |
| `Σ λ(n)` (trace) | `4.000000000000`, matching the analytic `2ac/π` exactly |
| **`Σ λ(n)²`** | ### **FAIL** — computed `3.513674`, banked `2.237484834940` |
| **`Σ λ(n)² ξ_n(1)²`** | ### **FAIL** — computed `0.974748`, banked `2` |
| **`ξ_n(1)`, six values** | ### **FAIL** — `0.01851, 0.11437, 0.43097, 1.03847, 1.70641, 2.19491` against banked `0.02618, 0.60948, 2.41323, 3.52614, 4.09936, 4.57184`. Not a constant factor apart. |
| rail `|ξ_n(1)| ≤ (2π)^{2n+½}` | holds |
| `t(n)`, `Qε(1)`, log-3 spectrum, ω-triple, δ/L table, `C = 0.3448` | ### **UNREACHABLE** — all depend on `Q_ε`; see the boundary below |

The identity target itself is sound: `2(Si(4π)/4π + 1) = 2.237484834942`, confirmed here independently
via `mpmath` to `1.7 × 10⁻¹³`. **The target is right; it is not this operator's `Σλ²`.**

## The diagnosis — and it is not a mismatch with my rebuild

Sweeping `c` and solving for the value that reproduces the banked `Σλ²`:

| | `c` | `Σλ` | `Σλ²` | `λ(0)` | `λ(0)²/(1−λ(0)²)` |
|:--|--:|--:|--:|--:|--:|
| **corpus's fixed `c`** | `2π = 6.2832` | `4.0000` | ### **`3.5137`** | `0.9999428` | ### **`8733`** ✓ |
| **`c` fitting the banked `Σλ²`** | ### **`4.2156`** | `2.6837` | ### **`2.2375`** ✓ | `0.9972254` | ### **`179`** ✗ |

> ### **NO SINGLE `c` SATISFIES BOTH BANKED NUMBERS.** *`c = 2π` reproduces the banked `8733` and refutes
> the banked `Σλ²`. The `c` that reproduces the banked `Σλ²` is `4.2156` — not `2π`, not any natural
> constant — and it refutes the banked `8733` by a factor of 49.*

### **THE CONTRADICTION IS INTERNAL TO THE BANKED RECORD, NOT BETWEEN THE RECORD AND THIS REBUILD.**

Sitting 9's anchor row (i) and sitting 11's correction 8 **cannot both describe the same prolate spectrum.**
Either the symbol `λ(n)` denotes two different families in the same attempt, or one of the two numbers is
wrong. This file does not decide which — it establishes that they disagree.

## Boundary — what this does NOT rebuild

* **Connes–Consani's `Q_ε`** (the ferry's *"eq. (100)"*). The equation is not on disk and was never
  executor-read: `OPEN_TRAILS` records the CC prolate/semilocal line as **"NOT READ — API `429`. Untested."**,
  and sitting 5 banked its CC data explicitly as **`FOUND-AT-SOURCE (NAVIGATOR-VERIFIED AT PDF)`, NOT
  `(EXECUTOR-READ)`**.
* the `Y₊` map, the constrained subspace `ĝ(−i/2) = 0`, the lag-`log 2` form.
* therefore not the log-3 spectrum, the ω-triple, the three negative fractions at `L = 3`, the five-point
  `δ/L` table, or `C = 0.3448`.

**Writing `Q_ε` from a remembered equation number would produce a different operator whose agreement or
disagreement with the banked numbers would be uninterpretable — the false ledger sitting 12 itself refused
to produce.**

## Run

```
python prolate_layer.py 400 700
```

No scipy. `numpy` for the eigenproblem, `mpmath` once for `Si(4π)`.
