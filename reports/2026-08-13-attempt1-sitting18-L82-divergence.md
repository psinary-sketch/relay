# W-ATTEMPT-1 — SITTING 18: `Tr(ϑ(f)PP̂P)` — **THE BLOCKAGE'S NEW NAME LANDS ALONE**

**Relay report · 2026-08-13 · ATTEMPT track · relay-only · sub-gate carried**
### **DIAGNOSTIC COMPLETE BEFORE ANY CHARACTERIZATION, per the law in force.** **Nothing deposits.**

---

## §1 — THE BUILD, PROLATE-FREE AS CHARTERED

**Kernel assembled exactly as specified, with no prolate data anywhere:**
`k₁(x,y) = sin(2π(x−y))/(2π(x−y)) + sin(2π(x+y))/(2π(x+y))`, and
`PP̂P = 1_{x≥1}[δ(x−y) − k₁(x,y)]1_{y≥1}`, smeared by `(ϑ(ρ)ξ)(v) = ρ^{−1/2}ξ(ρ⁻¹v)`.

### **THE FALSIFIABLE-GATE LAW IS SATISFIED BY CONSTRUCTION:** *this side is a 2-D sinc trace; the other is
1-D quadratures against δ and the (151) form. **No shared construction.*** *The circularity sitting 17
refused is genuinely gone.*

---

## §2 — ### **THE CONVERGENCE DIAGNOSTIC: `N` PASSES, `X` FAILS**

*(continuous part, run first as the oscillatory-region check)*

| `a` | `X = 20` | `X = 40` | `N`-spread at fixed `X` |
|:--|:--|:--|:--|
| `√2` | `−2.8177852 / −2.8177695 / −2.8177410` | `−3.4927710 / −3.4928853 / −3.4928757` | ### **`~4×10⁻⁵`** |
| `√3` | `−1.7995347 / −1.7997650 / −1.7997567` | `−2.2257562 / −2.2257406 / −2.2257046` | ### **`~2×10⁻⁴`** |

> ### **QUADRATURE RESOLUTION IS FINE — `N = 300 → 800` moves nothing. THE TRUNCATION `X` IS NOT: doubling
> `X` shifts the value by `−0.675` (`√2`) and `−0.426` (`√3`), i.e. ### `Δ ≈ −0.97 per ln X` and `−0.61 per
> ln X`. THE ASSEMBLED TRACE DIVERGES LOGARITHMICALLY IN THE TRUNCATION.**

---

## §3 — ### **THE DIAGNOSIS, CARRIED TO ITS ARITHMETIC**

**The `δ(x−y)` half of the kernel is not optional and I computed its contribution analytically:**
*`δ(x/ρ − x)` as a distribution in `ρ` gives `δ(ρ−1)/x`, so the identity piece contributes*
### **`f(1)·ln X`** *— itself logarithmically divergent, with the OPPOSITE sign.*

> ### **SO THE TRACE IS FINITE ONLY IF THE TWO DIVERGENCES CANCEL, WHICH REQUIRES THE CONTINUOUS PART'S
> `ln X` COEFFICIENT TO EQUAL `f(1)`.**
>
> | `a` | required (`= f(1)`) | ### **measured** |
> |:--|:--|:--|
> | `√2` | `1.4427` | ### **`0.974`** |
> | `√3` | `0.9102` | ### **`0.615`** |
>
> ### **THEY DO NOT CANCEL. THE COEFFICIENTS DISAGREE BY ~32 % IN BOTH ROWS — CLOSE ENOUGH TO SHOW THE
> MECHANISM IS THE RIGHT ONE, FAR ENOUGH TO SHOW THE ASSEMBLY IS WRONG.**

**What that means, stated without dressing:** ### **`PP̂P` on `[1,∞)` is not trace-class as I have assembled
it, and the smearing by `ϑ(f)` is not rescuing it. Either the diagonal-integral discretization mishandles the
distributional piece, or the trace in their (82) is a regularized object whose regularization I have not
reproduced.** *Both are live; neither is decided.*

> ### **AND THE CONSISTENT ~32 % IN BOTH ROWS IS A SIGNATURE, NOT NOISE — it is the kind of structured
> residual that sitting 16 taught me to distrust as a "finding" and to treat as an unresolved diagnostic.
> **I am not naming a cause.**

---

## §4 — WHAT DID NOT RUN, AND WHY

| item | state |
|:--|:--|
| **the real gate** (sinc-`L` vs `D + W_∞`) | ### **NOT RUN — `L` does not converge, so there is no left-hand side to compare** |
| **floor by subtraction, (82)** | ### **NOT RUN — depends on `L`** |
| **floor cross-route** (`W_∞ + E`) | ### **NOT RUN** |
| ### **the ledger** | ### **NOT RUN — sixth consecutive sitting** |

**The ferry allowed exactly this outcome: *"or the blockage's new name lands alone."*** ### **It lands alone.**

---

## §5 — CHECKPOINT-5, UPDATED

**Add to §2.2's correction table:** *nothing — no prior conclusion is overturned this sitting.*
**Add to §2.3's non-results:** ### **`Tr(ϑ(f)PP̂P)` via (82) — ATTEMPTED, DIVERGENT AS ASSEMBLED. The
blockage is no longer "unbuilt"; it is "built and not trace-class," which is a different and more specific
state.**

**THE BLOCKAGE'S NEW NAME:** ### ***the `ln X` coefficient mismatch — measured `0.974` and `0.615` against
required `1.4427` and `0.9102`.*** *One number per row, reproducible, and the whole of what stands between
this arc and a two-sided gate.*

---

## CLOSING

**Returning for the author's word:**
1. ### **THE BUILD IS PROLATE-FREE AND THE FALSIFIABLE-GATE LAW IS SATISFIED — the two sides share no construction. The circularity is genuinely fixed.**
2. ### **`N`-CONVERGENCE PASSES AT `10⁻⁵`; `X`-TRUNCATION DIVERGES LOGARITHMICALLY.**
3. ### **DIAGNOSED TO ITS ARITHMETIC: the identity piece contributes `+f(1)·ln X`, the continuous piece `−0.97·ln X` (`√2`), and cancellation requires equality. The gap is ~32 % in both rows.**
4. ### **I NAME NO CAUSE. Two candidates are live — distributional discretization vs an unreproduced regularization in (82) — and sitting 16's lesson is that a structured residual is not a finding until its diagnostic is finished.**
5. **The ledger is unrun for a sixth sitting; `h2` is exactly where it was.**

**`h2` UNCHANGED. NO SIGN. NOTHING DEPOSITS.**
