# b214 — THE ORIENTATION BITS

**2026-08-27 · relay `reports/2026-08-27-orientation-bits.md`**
**Ferry part 1 of 1, receipt confirmed IN FULL before execution (Rule 1).**
**Registration `672c9b3`, banked before any transform. Bank: `data/b214_orientation_bits.txt`. Raw run: `data/b214_raw_run.txt`.**

> *** ### **BRANCH (FIXED). `c_k = −(−i)^k` — `ε = −1`, orientation `i^{−k}`. GRADE BENCH.**
> ### **AND b205's `μ₋₂` DISCREPANCY IS DECIDED: `F φ / φ = +1` there, so the instrument's
> `α = +π√2` is the sign satisfying `F φ = c φ` — and the decision is CONVENTION-FREE.** ***

## THE CONVENTION, PINNED AND STATED ONCE

`(F f)(y) = ∫ f(x) e^{+2πixy} dx` — the continuum limit of b19's centered DFT,
`F[j,k] = exp(2πi·m_j·m_k/N)/√N`, positive exponent, self-dual scaling.

### **The keystone does not pick the sign.** `F² = parity, F⁴ = 1` holds for **both** exponents, so
it constrains `F` without choosing the convention. *Adopted here, not derived — and the record
carries both (b19 positive; b71's `χ_∞` conjugate).*

## COMPONENT 1 — THE GATES (P1)

**G-SONIN, reported first.** `F φ` must vanish on `|y| < 1` because `φ` is in the Sonin space —
### **and nothing in the construction forces it to.** The quadrature, the tail and the eigenvalue are
all free to be wrong, and if any is, the number is not small.

| τ = 2π | y = 0.00 | 0.15 | 0.37 | 0.61 | 0.83 |
|:--|:--|:--|:--|:--|:--|
| EVEN | 8.4e-15 | 8.6e-15 | 4.3e-15 | 1.2e-14 | 4.1e-15 |
| ODD | **0.0** | 1.4e-15 | 4.8e-15 | 8.0e-15 | 5.6e-15 |

Against a ratio scale of O(0.2) — relative ~5e-14. **PASS** at the registered 1e-12.

> ### **And one sampled point that is NOT a pass, printed rather than dropped:** `y = 0.97` returns
> 2.0e-4. ### **That point is inside the neighbourhood of `y = 1` my own registration excluded** —
> the tail's IBP expansion is in powers of `1/(aX)` with `a = τ(y−1) → 0` there. ***My sampling
> error, not the object's.***

**G-RATIO at τ = 2π.** `|φ(y)|` printed at every point so the denominator is visibly not near a zero
— b205's lesson, inherited.

- **EVEN** (rank 2, `α = +π`): ratio `= 1.0` at all six `y`; ### **imaginary part ~1e-58** — and the
  registration predicted the even ratio *must* be real before any number was read, so its vanishing
  is a check. Spread 2.87e-12, `||r|−1|` 2.07e-12.
- **ODD** (rank 1, `α = −π`): ratio `= +1.0i` at all six; ### **real part ~1e-54** — likewise
  predicted (*"an odd ratio with a real part is a defect, not a sign"*). Spread 1.42e-11.

**PASS** at the registered 1e-8 by four orders. **G-STAB:** two axis settings agree to ~3e-14; the
IBP tail bound is 2.8e-93, so ### **the tail is not the limiting error and its bound says so.**

## COMPONENT 2 — THE BITS AND THE READ (P2, d)

| rank | family | `c` from `F φ / φ` |
|:--|:--|:--|
| 1 | ODD | ### **`+i`** |
| 2 | EVEN | ### **`+1`** |

With each family's alternation from b211/b212 these **fix every rank**, reconciling with b212's
measured `− + + −`.

**The even bit's expectation landed — and *how* is the point.** The registration predicted `+1`
**from the import chain** (`c = α/π`). ### **This act did not use that chain; it computed `F φ / φ`.
They agree.** *The chain is confirmed by an independent route rather than assumed.*

**The odd bit was not predicted, and the registration said so.** Measured **`+i`** under b19's
convention, **`−i`** under the conjugate.

*** ### **AND THE STRUCTURE IS CLEANER THAN EITHER BIT: `ε = −1` IN BOTH CONVENTIONS. ONLY THE
ORIENTATION FLIPS.** *So `ε` is a fact about the object, and the orientation a fact about the object
**together with** the convention — exactly the split b203 predicted, now visible in the ladder.* ***

**(d) Proposition 5 does NOT decide either bit**, and the reason is structural: `V^∓_n =
n!(±2iπ)^{−n}U_n` relates **formal** series coefficients, while `α` and `c` are Borel-sum / Stokes
data of the **summed** solutions and of the transform. It does corroborate `V^−_0 = V^+_0 = 1` at
source — the μ-independence b211 and b212 leaned on.

## COMPONENT 3 — THE VERDICT, `μ₋₂`, THE SHADOW (P3–P5)

### *** (P4) HALTED FIRST, AND THAT IS THE MOST INSTRUCTIVE THING IN THE ACT ***

G-SONIN returned **~1e-3** where it returns ~1e-15, and the ratio spread was **29**. ### **The gate
fired exactly as designed.**

### **My first diagnosis was WRONG.** I blamed an under-refined root and showed `β = 8.5e-7` there.
### **Re-run at a genuine root (`β = 4.9e-57`, `α = π√2` to 16 digits) the halt persisted unchanged
— my diagnosis was refuted by my own re-run, not confirmed.**

**The real cause was my instrument.** At `τ = 4π`, `Λ = √2`, and the physical transform carries
frequency `τ` and a factor `Λ`. ### **The instrument used frequency `2π` and no factor, which is
correct only at `Λ = 1` — and the ferry's own clause (b) said so: *"at τ = 2π (Λ = 1, no
rescaling)."*** Corrected:

| corrected | G-SONIN | ratio | spread |
|:--|:--|:--|:--|
| `μ₋₂`, `τ = 4π` | **3.7e-19** | ### **1.0** | 1.4e-15 |

### **`c = +1`, so `α = +π√2` is the sign satisfying `F φ = c φ`** — the instrument's, not the
paper's printed `−4.44288293889868`. ### **And it is convention-free**, since the even bit does not
move under conjugation. **b205's discrepancy is DECIDED, not merely sharpened** — reported beside
b205, not folded into it. *RRT's authors are not contacted; b213's ruling stands.*

*τ = 2π spot-checked under the patched code: at `Λ = 1` the patch is a no-op and both bits stand.*

**(P5) The shadow.** Six further terminals in `Core/LadderOrientationShadow.lean`, **zero-axiom on
the first compile**; `AXIOM_PRINTS.txt` **366/366**, Core 360 → 366, **row 86** by the committed tool
from a script file. ### **The constraint was kept: an INSTANCE was added and nothing weakened.**
`alt2_does_not_imply_stepsI` is untouched — *a measurement cannot repeal a theorem* — and
`measured_not_stepsI` **excludes** the other orientation rather than leaving it unused.

## THE AUDIT SIDECARS (emitted; copied from the sidecar files)

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b214-core
  run at    : 2026-08-27T14:41:30 (local)
  input     : whole file LadderOrientationShadow.lean (created this act)
  input     : added lines in D:/SIDE-global-section vs HEAD
  stems     : gap, blind
  files     : 5
  lines     : 333
  hits      : 0
  live uses : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 bc6506445902b45990330078b1831634
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b214-docs
  run at    : 2026-08-27T14:44:43 (local)
  input     : added lines in D:/MY-DOwnloads/PLACE-papers vs HEAD
  stems     : gap, blind
  files     : 2
  lines     : 95
  hits      : 0
  live uses : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 6e97bdd26ad0774c3b0a056de4316560
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : commit_selfcheck
  act       : b214-docs
  run at    : 2026-08-27T14:45:14 (local)
  input     : D:/MY-DOwnloads/PLACE-papers
  input     : HEAD
  written   : 2
  foreign   : 0
  ro-claim  : none
  compliance : none
  VERDICT   : CLEAN
  self-hash : sha256/32 3aeeeb9cffed7ec41630c138448aad27
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : mirror_verify
  act       : b214
  run at    : 2026-08-27T14:45:34 (local)
  input     : mirror-refresh-2026-08-27.zip
  files     : 40
  rows      : 40
  mismatch  : 0
  declared  : 6474a63
  ls-remote : 6474a63de518
  VERDICT   : CLEAN ON ALL THREE CLAUSES
  self-hash : sha256/32 da2987219463357ab42d5d33bf096a95
=== END AUDIT SIDECAR ===
```

**Index (clause (e)):** 8 of 16 hit. The misses now include **`transform convention`** and
**`eigenfunction scale`** — ### **two names b203 minted explicitly and the index still cannot
reach.** Fifth consecutive act to name this queue.

## PINS

| repo | pin | visibility |
|:--|:--|:--|
| **SIDE-global-section** | `2f2c184` → ### **`356010f`** — Core 360 → 366 | PUBLIC |
| **PLACE-papers** | `1dfdd5b` → ### **`6474a63`** — §24 + the register | PRIVATE |
| relay | `672c9b3` → the b214 pin-line commit | PUBLIC |
| SIDE-kernel | `0256e9e` — **UNMOVED** | PUBLIC |
| mirror | rebuilt at `6474a63`, **CLEAN ON ALL THREE CLAUSES** | — |
| HELD | `6eada6a` — **LOCAL-ONLY, untouched** | — |

**DEVIATIONS:** none. **DIVERGENCES:** none with the ferry.

### *** THREE ERRORS OF MY OWN, ALL RECORDED ***

**(i)** The instrument assumed `Λ = 1` and I carried it to `τ = 4π` anyway, **against the ferry's own
clause (b)**. ### **G-SONIN caught it — the gate the ferry called "the strongest available" was the
thing that caught me, which is what it was for.**
**(ii)** My first diagnosis of that halt was wrong, and was **refuted by my own re-run before it was
reported**. ***A plausible diagnosis that survives one test is not a diagnosis.***
**(iii)** I sampled `y = 0.97` inside the neighbourhood my own registration had excluded an hour
earlier. Printed, not dropped.
