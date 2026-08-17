# `battery_full.py` — the full certification battery: substrate + operator + `η` layer

**Banked 2026-08-15. One row's behaviour re-classified 2026-08-17 and it is documented here rather than
silently repaired.**

## Why it exists

**One command that reproduces every banked number the instrument can reach, and reports the ones that do
not, with their diagnosis.** *The `δ/L` law spent two sittings at `SUSPENDED-PENDING-INSTRUMENT` because no
such command existed; the point of this file is that the next reader runs one thing and sees the whole state.*

```
python battery_full.py
```

`numpy`; `prolate_layer` (+`mpmath` once) → `qeps_layer` → `phi_layer`. Runtime is dominated by PART 4's
`Qε` table at `ω = 10⁻³` up to `nmax = 1386`.

## What each part covers

| part | content | source of the targets |
|:--|:--|:--|
| **1** | the prolate / `ε` substrate, 15 rows, pins P1–P3 | `prolate_layer.battery()`; `README_prolate.md` |
| **2** | the operator layer — `ε(1)`, `Qε(1)`, `ε′(1⁺)` | eq. (100) / (85); `README_qeps.md` |
| **3** | the `K_I` spectra at `L = 2` and `L = 3`, with parities | sitting 9; CC's published log-2 spectrum |
| **4** | the `η` layer — offender counts, the `δ/L` table, `C`, the endpoint machine-zero | sitting 12; `README_phi.md` |

## The rows, and their verdicts

### **PART 1–2 — SUBSTRATE AND OPERATOR: ALL PASS**

| row | computed | target | `\|Δ\|` |
|:--|--:|--:|--:|
| `Σ μ_k` *(all, incl. odd)* | `4.000000000` | `4` — footnote 10 | `8.9e-16` |
| `Σ λ(n)²` *(even only)* | `2.237484834` | `2.237484835` — Remark 4.5 | `5.8e-11` |
| `Σ λ(n)² ξ_n(1)²` | `2.000000000` | `2` exactly | `3.6e-15` |
| `ξ_0(1) … ξ_5(1)` | `0.02618 … 4.57184` | sitting 9 row (v) | `≤ 5.0e-06` |
| `t(0) … t(4)` | `11.9719, 8.77574, 2.20528, 0.0433983, 0.000125459` | CC Lemma 5.4 | `≤ 3.2e-05` |
| ### **`ε(1)`** · ### **`Qε(1)`** | ### **`0`, machine zero, both** | `0` exactly | — |
| ### **`ε′(1⁺)`** | ### **`22.9964757`** | `22.996476` | `3.2e-07` |

### **PART 3 — THE SPECTRA: ONE PASS, ONE DISAGREEMENT REPORTED AS SUCH**

| window | computed | banked | verdict |
|:--|:--|:--|:--|
| ### **`log 3`** | `1.089891 / 1.039452 / 0.684735` | `1.089917 / 1.039477 / 0.684763` | ### **PASS, `Δ ≈ 2.6×10⁻⁵`** |
| `log 2` | `1.052020 / 0.689577 / 0.030814` | `1.05158 / 0.686494 / 0.0289` *(this ferry)* · `1.051772 / 0.687924 / 0.029692` *(sitting 9)* | ### **`EXTERNAL-TRANSCRIBED`** — see below |
| parities | even / odd / even | at both windows | ### **PASS** |

> ### **THE `log 2` ROW IS NOT A FAILURE AND IT IS NOT A PASS.** *The corpus's own two records of the triple
> disagree with each other by `~10⁻³`, the same order by which the rebuild differs from both, while the
> `log 3` triple from the same code in the same run reproduces to `2.6×10⁻⁵`.* **Landed as a label in
> `THE_ATTEMPT_RECORD` §1 (correction 17): a transcribed published spectrum, tolerance inter-discretization,
> and the parities are what actually reproduce.** *The script still prints it beside its target; it is the
> label, not the code, that carries the grade.*

### **PART 4 — THE `η` LAYER: TWO ROWS THAT NEED READING BEFORE THEY ARE BELIEVED**

| row | result |
|:--|:--|
| `L = 2.5`, `3.0` | ### **MATCH** — `224/916`, `407/1099` |
| `L = 2.2`, `3.5` | off by one — ### **degenerate boundary cluster at `5×10⁻⁶`; the `±1` is grid noise** |
| ### **`L = 4.0`** | ### **`692`, NOT `693`** — `0.49928`, not exactly one half, at a boundary separated by `1.2×10⁻²`. **A real miss, and correction 17 strikes the claim it supported.** |
| `C` on `V` | ### **`0.34451`** *(banked `0.34481`)* — **and `0.88648` without `V`, which is why `V` is required for this row** |
| endpoint machine-zero | `|c·v|` on `V` at machine precision *(banked `2.73e-17`)* | ### **PASS** |

## ### THE ONE THING A READER MUST KNOW BEFORE USING PART 4

> ### **PART 4's OFFENDER COUNTS ARE TAKEN ON THE FULL GRID. `V` IS NOT IMPOSED ON THEM.**
>
> **`C` in the same part IS computed on `V` and requires it.** *One file, one constraint, two different
> answers to whether it was applied — and that asymmetry is not a bug in this file: it is what makes this
> file reproduce the banked record, because* ### **the banked record was taken the same way.**
>
> **The proof is in the denominators.** *Sitting 12's report says "all on `V`" on its face, and its own
> fractions are* `97/788`, `224/916`, `407/1099`, `561/1253`, `693/1386` — ### **every denominator is
> `M = round(log L/ω)` exactly, and no `V`-restricted count can have `dim = M`.** *On `V` the dimension is
> `M − 1` and the counts are one lower: at `L = 3`, `202/548 · 406/1098 · 811/2196`.*
>
> ### **THIS IS DELIBERATELY LEFT IN PLACE.** *Repairing it would break the file's job, which is to
> reproduce the bank as it stands. **New measurement goes through `phi_layer.negative_fraction` or
> `exp1_two_prime.measure`, both of which impose `V`.*** *`THE_ATTEMPT_RECORD` §1 carries the
> `V`-consistency note; `FINDINGS` `F.2026-08-17` carries the re-measurement.*

## What the battery has since been superseded on

**PART 4 prints `1 − log2/logL` as "predicted".** ### **That formula is the `L ≤ 4` branch of the law, not
the law.** *Measured 2026-08-17 over `L ∈ {3.2, 3.6, 4.2, 4.6, 5.5, 7.0}` at three `ω`, one lag, on `V`:*

> ### **negative fraction = `min( 1 − log2/logL , log2/logL )`; in counts, `min( k₂ , M − k₂ )` to within one
> grid point.** *Room branch below `L = 4`, lag branch above, apex `½` at exactly `L = 4`.*

**Every `L` in the battery's own table is at or below the apex, which is why the battery never saw the
turn.** *`THE_ATTEMPT_RECORD` correction 18; `FINDINGS` `F.2026-08-17`;
`reports/2026-08-17-experiment-one-two-prime-room.md`.*

## Boundary

* ### **THE PRIME COEFFICIENT IS SUPPLIED AT `q = 2` ONLY** (`2√2 log 2`). *The two candidate
  generalizations —* `2√q·log p` *and the Weil weight* `4 log p/√q` *— agree there and nowhere else, and*
  ### **changing every coefficient by up to `2.5×` moves the measurement by at most two offenders in
  `1,945`.** **A quantity insensitive to a parameter cannot measure it: the coefficient question is not
  adjudicable on this bench.** *`THE_EULER_SPECIFICATION` §14.*
* **The `ω`-class effect.** *When `log 2` and `log 4` are both live, the answer depends on whether
  `k₄ = 2k₂` — equivalently, identically, on whether `k₄` is even.* ### **A grid artifact of rendering
  `log 4 = 2 log 2`, isolated 2026-08-17 and confined to that pair.**
* **Lemma 5.2's `(1,3]` re-derivation is unpaid**, and it was re-scoped 2026-08-17 to cover `L = 4` —
  ### **`ρ = 4 > 3`, outside the range and outside even the extended range the two largest banked rows
  already sat beyond.**
* ### **NOTHING IN THIS BATTERY BEARS ON `h2`, ON THE SIGN OF `W_∞ − W_2`, OR ON ANY OPERATOR INEQUALITY.**
