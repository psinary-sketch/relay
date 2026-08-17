# `phi_layer.py` — the `η` coordinate: `Φ` on `V`, the negative fractions, the `δ/L` curve

**Banked 2026-08-15. `V`-restriction verified against an independent basis 2026-08-17.**
### **This is the layer the `δ/L` law is measured with.**

## Why it exists

The `δ/L` law counts the directions on which `Φ_L > 0`. Sitting 12 described the matrix in prose — *`Φ ≤ 0
⟺ ηᵀGη ≥ 0`, grid `dim = round(log L/ω)`, lag at `log 2`* — **and never defined it.** This file defines it,
from the supplied `(103)/(105)` quadratic form and the `η` reformulation, and is tracked.

## The formulas, as supplied

```
V     = { η : ∫ e^{−t/2} η(t) dt = 0 }
ξ     = Y₊ ⋆ η,      Y₊(s) = e^{s/2} · 1_{s ≥ 0}
K_I   kernel = Qε(exp|v|) / (2 ε′(1⁺))
N_I   = −2 ε′(1⁺) (Id − K_I)
Φ(η)  = ⟨ξ | N_I ξ⟩ + 2√2 log 2 · (η ⋆ η*)(log 2)
```

**Sitting 11's reading, used verbatim:** *offenders = directions where `Φ > 0` = NEGATIVE eigenvalues of `G`,
with `Φ ≤ 0 ⟺ ηᵀGη ≥ 0`. So `G = −(matrix of Φ)`* — and `negative_fraction` counts the POSITIVE eigenvalues
of the `Φ` matrix.

## The discretization, stated because every number depends on it

| | |
|:--|:--|
| grid | `M = round(log L / ω)`, midpoints `t_j = (j + ½)ω` |
| `Y₊ ⋆ ·` | lower-triangular `Y_{ij} = ω·e^{(t_i − t_j)/2}` for `i ≥ j` — midpoint rule, no trapezoid ends |
| `K_I` | Toeplitz in `Qε(e^{ω|i−j|})`, scaled `ω/(2ε′(1⁺))`; the `Qε` table is cached per `(ω, nmax, NG)` |
| the prime term | autocorrelation at lag `log 2`, placed at address `k = round(log 2 / ω)` |
| ### **`V`** | ### **IMPOSED** — `c_j = e^{−t_j/2}` normalized, `B₀` an orthonormal basis of `c^⊥` from an SVD of `I − cc^T`; the returned matrix is `B₀ᵀ A B₀`, of dimension **`M − 1`** |

> ### **THE ADDRESS IS A ROUNDED INTEGER, AND THAT IS NOT COSMETIC.** *`k_q = round(log q / ω)` means the
> grid preserves an exact arithmetic relation between two lags only for some `ω`.* **Measured 2026-08-17:
> `k₄ = 2k₂` ⟺ `k₄` is even, identically for every `ω`** *(because `|round(2x) − 2·round(x)| ≤ 1` and
> `2·round(x)` is even)*, **and the two `ω` classes give measurably different answers when `log 2` and
> `log 4` are both live.** *See `README_battery.md` and the 2026-08-17 relay report.*

## Certification rows this layer passes

| row | computed | banked | verdict |
|:--|:--|:--|:--|
| ### **the log-3 no-prime spectrum** | `1.089891 / 1.039452 / 0.684735` | `1.089917 / 1.039477 / 0.684763` | ### **PASS, `Δ ≈ 2.6×10⁻⁵`** |
| ### **branch B** | two eigenvalues exceed `1` at `log 3` | pre-committed at sitting 7, landed at 9 | ### **FIRES** |
| parities | even / odd / even | at both windows | ### **PASS** |
| ### **the `L = 3` `ω`-triple, on `V`** | ### **`202/548 · 406/1098 · 811/2196`** | `202/548 · 406/1098 · 811/2196` | ### **PASS EXACTLY, 3/3** |
| the same, unconstrained grid | `203/549 · 407/1099 · 812/2197` | the sitting-12 numbers | ### **reproduces** |
| ### **the `V` basis itself** | Householder basis → `202/548`; **this file's SVD basis → `202/548`** | — | ### **IDENTICAL** |

### **THE LOG-2 GATE IS NOT A CERTIFICATION ROW — IT IS `EXTERNAL-TRANSCRIBED`**

| source | triple |
|:--|:--|
| this instrument *(converged in `ω`)* | `1.052020 / 0.689577 / 0.030814` |
| banked, the 2026-08-15 ferry | `1.05158 / 0.686494 / 0.0289` |
| banked, sitting 9 | `1.051772 / 0.687924 / 0.029692` |

> ### **THE CORPUS'S OWN TWO RECORDS OF THIS TRIPLE DISAGREE WITH EACH OTHER BY `~10⁻³` — the same order by
> which this rebuild differs from both — while the log-3 triple, produced by the same code in the same run,
> reproduces to `2.6×10⁻⁵`.** *Reading: log-3 is the corpus's own numerics; log-2 is a transcribed published
> spectrum.* **Landed as a label in `THE_ATTEMPT_RECORD` §1 (correction 17): `EXTERNAL-TRANSCRIBED`,
> tolerance inter-discretization, and it is the PARITIES that actually reproduce.**

## The law this layer measures, as of 2026-08-17

> ### **negative fraction on `V` = `min( 1 − log2/logL , log2/logL )`** — the smaller of the room and the
> lag. **In counts: `min( k₂ , M − k₂ )`, to within one grid point, at every `L` and every `ω` tested.**
> *Room branch below `L = 4`, lag branch above, apex `½` at exactly `L = 4`.*

**The banked `1 − log2/logL` is the `L ≤ 4` branch** — exact where the corpus measured it (`L = 2.2 … 4.0`,
all at or below the apex) and half of the law. *`THE_ATTEMPT_RECORD` correction 18; `FINDINGS` `F.2026-08-17`.*

## Boundary

* ### **`negative_fraction` IMPOSES `V`; `battery_full.py`'s PART 4 DOES NOT.** *That asymmetry is the
  2026-08-15 finding two, and it is deliberate in `battery_full` — see `README_battery.md`.* **Anything new
  measures through this file, or through `exp1_two_prime.measure`, both of which are on `V`.**
* **The log-3 rows carry the Lemma 5.2 debt.** *Their Prop 5.5 states window length `≤ log 2`; the log-3 use
  is the sitting-11/12 EXTENSION and the `(1,3]` re-derivation is unpaid.* ### **The debt was re-scoped
  2026-08-17: it must now reach `L = 4`, i.e. `ρ = 4 > 3`, where the branch turn happens.**
* ### **NOTHING HERE BEARS ON `h2`, ON `W_∞ − W_2`, OR ON ANY OPERATOR INEQUALITY.** *The negative fraction
  is a bench quantity of a discretized form.*

## Run

```
python -c "import phi_layer as P; print(P.negative_fraction(3.0, 1e-3))"     # (npos, dim, fraction, M)
python -c "import phi_layer as P; A,M = P.phi_matrix(3.0, 2e-3); print(A.shape, M)"
```

`numpy`; `qeps_layer` → `prolate_layer` beneath. The `Qε` table dominates the runtime
(`≈ 55 s` at `ω = 10⁻³`, `L = 7`); it is cached per `(ω, nmax, NG)` within a process, so compute it once at
the largest `nmax` needed and slice.
