# W-ATTEMPT-1 — SITTING 16, ADDENDUM: **THE ARCH COLUMN PASSES. §3's DIAGNOSIS WAS WRONG.**

**Relay report · 2026-08-13 · ATTEMPT track · relay-only · correction of record**
### **NO FERRY AUTHORIZED NEW WORK. This addendum exists because the report banked minutes earlier contains a false finding, and a wrong record left standing is worse than a slow one.** **Nothing deposits.**

---

## §1 — THE BACKGROUND RUN LANDED

*Route A re-run at extended truncation, against the same atlas rows:*

| `a` | Route A `X = 10⁴` | Route A `X = 10⁶` | atlas `−ARCH` | ### **residual / `f(1)`** |
|:--|:--|:--|:--|:--|
| `1.3` | `+1.8361387` | ### **`+1.8356292`** | `+1.8356255` | ### **`0.000001`** |
| `√2` | `+1.9909107` | ### **`+1.9905249`** | `+1.9905222` | ### **`0.000001`** |
| `2.0` | `+1.7866921` | ### **`+1.7864992`** | `+1.7864979` | ### **`0.000001`** |

> ### **THE ARCH COLUMN PASSES. Agreement to `~1×10⁻⁶` relative to `f(1)` — SIX ORDERS OF MAGNITUDE BETTER
> THAN THE `0.008756` I REPORTED AS A STRUCTURAL RESIDUAL.**

---

## §2 — ### **THE CORRECTION, STATED PLAINLY**

**Sitting 16 §3 concluded:** *"the remainder is `0.008756 × f(1)` … A DIFFERENCE IN THE COEFFICIENT OF `f(1)`
BETWEEN THE TWO CONVENTIONS, AND NOTHING ELSE"* and **"THE ARCH COLUMN DOES NOT PASS."**

### **BOTH SENTENCES ARE WRONG. The entire discrepancy was truncation and quadrature at `X = 80`, and it
vanishes on refinement.**

**What went wrong, exactly.** *My analytic tail `−f(1)·ln((X+1)/(X−1))` is correct for the far tail, and I
verified it accounted for only ~74 % of the gap — then concluded the remainder was structural.* ### **The
unmodelled part was NOT structure: it was Gauss–Legendre node placement near `u = 0`, where the integrand's
numerator and the kernel's pole cancel. Changing `X` changes the node distribution over the WHOLE interval,
including that delicate region — so the `X = 80` run was under-resolving the cancellation, not revealing a
constant.**

> ### **THE PROPORTIONALITY TO `f(1)` — FOUR SIGNIFICANT FIGURES ACROSS THREE ROWS — WAS REAL AND WAS
> MISREAD. The near-zero region's contribution scales with `f(1)`, so a resolution error there is
> proportional to `f(1)` too. A clean proportionality is consistent with a coefficient discrepancy AND with a
> quadrature artefact, and I attributed it to the first without excluding the second.**

**The discipline point, recorded against myself:** *sitting 16 said "diagnosed, not absorbed" and refused to
rescale — that refusal was right and remains right.* ### **But refusing to absorb an artefact is not the same
as identifying it, and I wrote a confident structural conclusion on a two-stage argument whose second stage
had one unexamined alternative. The `X = 10⁷` re-run was already launched — I reported the conclusion without
waiting for the instrument I had myself queued to test it.**

---

## §3 — THE STATE NOW

| item | state |
|:--|:--|
| **PRIME column** | ### **PASSES — exact to six decimals, four live rows** *(unchanged; that result stands)* |
| **ARCH column** | ### **PASSES — `~10⁻⁶` at `X = 10⁶`** *(corrected this addendum)* |
| ### **sitting 16's item-1 gate** | ### **NOW PASSED ON BOTH COLUMNS** |
| **dual-route gate (item 2)** | not run |
| **the ledger (item 3)** | not built |

> ### **THE GATE THAT HAS BLOCKED THE LEDGER FOR FOUR SITTINGS IS OPEN. `W_∞` and `W_2` are both certified
> against the corpus's own bench on the matched family. THE LEDGER AWAITS THE AUTHOR'S WORD — no ferry has
> chartered it since, and this addendum claims no licence to run it.**

---

## CLOSING

**Returning for the author's word:**
1. ### **THE ARCH COLUMN PASSES AT `10⁻⁶`. Sitting 16's "does not pass" and its `0.008756` coefficient-discrepancy finding are BOTH WITHDRAWN.**
2. ### **THE ERROR WAS MINE AND ITS SHAPE IS INSTRUCTIVE: a real proportionality, misattributed to structure when a quadrature artefact produces the same signature. Two causes were named in §3 and I picked the wrong one instead of waiting for the run that separated them.**
3. ### **BOTH COLUMNS ARE NOW CERTIFIED AGAINST AN EXTERNAL BENCH.** *Sitting 11's normalization question — dissolved at sitting 15, re-opened in a different form at 16 — is now closed by measurement.*
4. **The ledger is unbuilt and unchartered. Item 2's dual-route gate remains the next step.**

**`h2` UNCHANGED. NO SIGN. NOTHING DEPOSITS.**
