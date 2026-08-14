# W-ATTEMPT-1 — SITTING 16: THE COLUMNS — **PRIME EXACT · ARCH DIAGNOSED, NOT PASSED**

**Relay report · 2026-08-13 · ATTEMPT track · relay-only · sub-gate carried**
### **DEBTS: parity ledger UN-DERIVED; Lemma 5.2 `(1,3]` UN-RUN (`L ≤ 3`). Bench-grade values carry the reach-theorem disclaimer.** **Nothing deposits.**

---

## §1 — THE MATCHED FAMILY, QUOTED FROM THE CORPUS'S OWN TOOL

**`carto_atlas.py`, header verbatim:**
> *"Explicit formula, even test function, standard normalisation:
> `sum_gamma hhat(gamma) = hhat(i/2) + hhat(-i/2) - PRIME + ARCH` **[sign fixed BY the E2 calibration]**"*

**`bump(a)`:** `v = linspace(−L, L, 4001)`, `L = log a`, `w = exp(−1/(1−(v/L)²))` on `|v/L| < 1`, normalized
`∫w dv = 1`. ### **The sign convention is therefore FIXED BEFORE COMPARING: `ARCH` is negative in their
ledger, so Route A's `W_∞` is tested against `−ARCH`.**

---

## §2 — ### **THE PRIME COLUMN: EXACT AT EVERY LIVE ROW**

| `a` | Route A `W_2` | atlas `PRIME` | ratio |
|:--|:--|:--|:--|
| `1.3` | `+0.0000000` | `+0.0000000` | *(both 0 — prime-silent)* |
| `√2` | `+0.0000000` | `+0.0000000` | *(both 0 — prime-silent)* |
| `1.5` | `+0.0006550` | `+0.0006550` | ### **`1.000000`** |
| `1.6` | `+0.0271022` | `+0.0271022` | ### **`1.000000`** |
| `√3` | `+0.1065151` | `+0.1065151` | ### **`1.000000`** |
| `2.0` | `+0.2493196` | `+0.2493196` | ### **`1.000000`** |

> ### **FOUR LIVE ROWS, EXACT TO SIX DECIMALS. Two prime-side formulas — CC's `W_2` as I coded it from their
> normalization, and the atlas's `2 log p · p^{−k/2} · corr(log p^k)` written months earlier — agree with no
> free parameter.** **THE PRIME COLUMN PASSES.**

---

## §3 — ### **THE ARCH COLUMN: DOES NOT PASS — AND THE RESIDUAL HAS EXACT STRUCTURE**

| `a` | Route A `W_∞` | atlas `−ARCH` | ratio |
|:--|:--|:--|:--|
| `1.3` | `+1.8999575` | `+1.8356255` | `1.035046` |
| `√2` | `+2.0392243` | `+1.9905222` | `1.024467` |
| `1.5` | `+2.0390302` | `+1.9974029` | `1.020841` |
| `1.6` | `+2.0036360` | `+1.9677247` | `1.018250` |
| `√3` | `+1.9396023` | `+1.9088771` | `1.016096` |
| `2.0` | `+1.8108483` | `+1.7864979` | `1.013630` |

**The ratio drifts monotonically — so it is neither a constant offset nor a constant proportion. Diagnosed
in two stages, per the ferry's instruction.**

### **STAGE 1 — the truncation tail, computed exactly, not estimated**

*Beyond `f`'s support the integrand is `−2f(1)/(x − 1/x)`, so the omitted tail past `X` is exactly
`−f(1)·ln((X+1)/(X−1))`.*

### **STAGE 2 — the remainder is EXACTLY PROPORTIONAL TO `f(1)`**

| `a` | `f(1)` | remaining after tail | ### **remaining / `f(1)`** |
|:--|:--|:--|:--|
| `1.3` | `1.9058` | `+0.0166845` | ### **`0.008755`** |
| `√2` | `1.4427` | `+0.0126327` | ### **`0.008756`** |
| `2.0` | `0.7213` | `+0.0063170` | ### **`0.008757`** |

> ### **THREE ROWS, FOUR SIGNIFICANT FIGURES, ACROSS A FACTOR OF `2.6` IN `f(1)`. THE RESIDUAL IS
> `0.008756 × f(1)` — A DIFFERENCE IN THE COEFFICIENT OF `f(1)` BETWEEN THE TWO CONVENTIONS, AND NOTHING
> ELSE.**
>
> ### **DIAGNOSED, NOT ABSORBED, AND NOT RESOLVED.** *Two candidate causes, neither eliminated this sitting:
> (a) the archimedean constant `(log 4π + γ) = 3.108242` in CC's (151) versus whatever constant the atlas's
> `ψ`-kernel integral effectively carries — the gap would be `3.108242 − 3.099486`; (b) discretization in one
> of the two instruments.* ### **I decline to adopt either, and I decline to rescale by `0.008756` to force
> the column — that is exactly the fitting the discipline forbids.**

### **VERDICT: THE ARCH COLUMN DOES NOT PASS AT ANY TOLERANCE I WOULD STATE IN ADVANCE.** *A `1.4–3.5 %`
disagreement with exact proportional structure is a live discrepancy, not noise.*

---

## §4 — THE GATE AND THE LEDGER: **NOT REACHED**

**The ferry gated the ledger on items 1–2 passing. `§3` does not pass, so — as at sittings 13, 14 and 15 —
### THE DUAL-ROUTE GATE WAS NOT RUN AND THE LEDGER WAS NOT BUILT.** *Outcomes (α)/(β)/(γ) unreached for a
fourth consecutive sitting.*

**A long-running extended-truncation re-run (`X = 10⁷`, 20000 nodes) was launched to isolate stage 1
independently and did not finish within this sitting.** *Its result, when it lands, tests only the tail term;
the proportional residual of `§3` is untouched by it.*

---

## CLOSING — REVIEW

**Nothing proof-shaped emerged. No sign step exists to price.** **Banked to relay only.**

**Returning for the author's word:**
1. ### **THE PRIME COLUMN PASSES EXACTLY — four live rows to six decimals, two independent formulas, no free parameter. The prime side of this instrument is now cross-validated against the corpus's own bench.**
2. ### **THE ARCH COLUMN FAILS, WITH EXACT STRUCTURE: after the analytic truncation tail, the remainder is `0.008756 × f(1)` to four significant figures across three rows. A coefficient discrepancy, isolated and unexplained.**
3. ### **I DID NOT ABSORB IT.** *Rescaling by the measured constant would have produced a passing column and a corrupted instrument.*
4. **The gate blocks the ledger for the fourth sitting; the single named next step is resolving the `f(1)`-coefficient discrepancy at content — CC's (151) constant against the atlas's `ψ`-kernel normalization.**

> ### **THE INSTRUMENT IS NOW HALF-CERTIFIED AGAINST AN EXTERNAL BENCH: the prime side exactly, the
> archimedean side not at all. That is a sharper position than four sittings of "not yet compared," and it
> names one number as the whole of what stands between here and a validated floor.**

**`h2` UNCHANGED. NO SIGN. NOTHING DEPOSITS.**
