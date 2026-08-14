# RESURRECTION PART 2 — THE PINS LAND · ### 15/15 PASS · ### AND YESTERDAY'S HEADLINE FINDING IS WITHDRAWN

**Relay report · 2026-08-14 · author-called · relay-only for bench · nothing deposits**
**`h2` UNCHANGED. NO SIGN SENTENCE.**

```
PLACE-papers  origin/main : e3048e3b2310c4b4a7d01074f71ac7b9d902d550   VERIFIED
mirror        22 / 22 rows COHERENT at e3048e3
relay         origin/main : (this report)                    local +1 HELD
```

---

## §0 — ### THE CORRECTION FIRST, BECAUSE IT IS MINE

**Yesterday I reported that the banked record contradicted itself** — *"no single `c` satisfies both",
"the contradiction is internal to the banked record, not between the record and the rebuild"* — and I dropped
the `δ/L` law's grade on that basis.

### **THAT FINDING IS WITHDRAWN. THE RECORD DID NOT CONTRADICT ITSELF. I WAS MISSING THREE CONVENTION PINS.**

Both banked numbers were right about their own objects the whole time. So was the rebuild. **What was missing
was the map between them.**

> ### **THE FAILURE MODE, NAMED SO IT IS RECOGNIZABLE: A CONVENTION MISMATCH PRESENTS EXACTLY AS A
> CONTRADICTION IN THE SOURCE.** *And it is **indistinguishable from the true finding until the pin arrives** —
> which is precisely why "the record contradicts itself" is a conclusion an executor should reach last, not
> first. I reached it in one pass.*
>
> **Kin, read in the direction I failed to read it: `AUTHORITY IS NOT ACCURACY`.** *The corpus wrote that law
> against trusting a source's standing. It applies with equal force to the executor's own instrument.*

---

## §1 — THE PINS, AND WHAT THEY UNLOCKED

| pin | content |
|:--|:--|
| **P1** | CC's `λ(n)` are the ### **EVEN-INDEXED** truncated-Fourier eigenvalues, signed: `λ(n) = (−1)ⁿ√(μ_{2n})`, `c = 2π`. ### **The concentration eigenvalues the rebuild computes are `λ(n)²` — and CC's sum runs over even indices ONLY.** |
| **P2** | Norm eq. (16): `‖ξ‖² = ∫₀^∞|ξ|²`, half-line on even functions ⟹ ### **`ξ_n = √2 · ψ_{2n}`** |
| **P3** | `ξ_n = P₁φ_n/‖P₁φ_n‖`; `ξ_n^an` via `η_n = Fξ_n = λ(n)·ξ_n^an` |

### **THE TELL I HAD IN HAND AND MISREAD.** *My trace came out at exactly `4.000000000000`. Selecta footnote
10 says* ### **"the sum of squares of eigenvalues including the odd ones is 4."** *The number that looked like
my operator's trace was CC's full sum of squares. **The pin was legible in my own output and I read it as a
coincidence.***

---

## §2 — THE BATTERY RE-RUN: ### 15 / 15 REACHABLE ROWS PASS

| row | computed | target | `\|Δ\|` |
|:--|--:|--:|--:|
| `Σ μ_k` *(all, incl. odd)* | `4.000000000` | `4` — footnote 10 | `8.9e-16` |
| ### **`Σ λ(n)²`** *(even only)* | `2.237484834` | `2.237484835` — Remark 4.5 | ### **`5.8e-11`** |
| ### **`Σ λ(n)² ξ_n(1)²`** | `2.000000000` | `2` exactly | ### **`3.6e-15`** |
| `ξ_0(1) … ξ_5(1)` | `0.02618, 0.60948, 2.41323, 3.52614, 4.09936, 4.57184` | sitting 9 row (v) | `≤ 5.0e-06` |
| ### **`t(0) … t(4)`** | `11.9719, 8.77574, 2.20528, 0.0433983, 0.000125459` | CC Lemma 5.4 | ### **`≤ 3.2e-05`** |
| ### **`ε′(1⁺) = Σ t(n)`** | `22.9964757` | `22.996476` | ### **`3.2e-07`** |

### **`t(n)` WAS NOT FITTED, AND THIS MATTERS.** *Correction 13 states the assembly "was computing
`Σλ²/(1−λ²)` exactly"; sitting 9 states "the missing factor was `ξ_n(1)²`.* ### **`t(n) = λ(n)²ξ_n(1)²/(1−λ(n)²)`
is the corpus's own sentence, written down and evaluated** — *and it reproduces all five CC values to six
figures on the first evaluation. No search, no adjustment.*

### **CORRECTION FIFTEEN CONFIRMED NUMERICALLY, BOTH HALVES**

| | computed | banked |
|:--|--:|--:|
| the pre-correction artifact `μ₀²/(1−μ₀²)` | ### **`8733.4`** | `≈ 8733` ✓ |
| the corrected `Σλ²/(1−λ²)` *(even)* | ### **`17491.3`** | sitting 13's `≈ 17491` ✓ |

*The artifact **and** its supersession are both reproducible to five figures. The reference rows are re-stated
against the corrected record; the labelled artifact is never a target again.*

**Instrument banked with its pins: `relay/tools/e16/prolate_layer.py` + `README_prolate.md`.**

---

## §3 — WHAT IS STILL UNREACHABLE, AND IT IS NOW ONE THING

`Q_ε` — ### **eq. (100)** — the `Y₊` map and the lag form are **still not on disk.** The pins fixed the
*identification*; they did not supply the *operator*.

**Therefore still not computable:** `ε(1) = 0` · `Qε(1) = 0` · the log-2 spectrum · the log-3 no-prime
spectrum · the `L = 3` negative fractions · the five-point `δ/L` table · `C = 0.3448` · endpoint machine-zeros.

> ### **THOSE EIGHT ROWS ARE EXACTLY THE ONES `δ/L` DEPENDS ON.** *The substrate beneath them is now certified
> to `10⁻¹⁵` in places. The operator layer above them is unbuilt.*

**`δ/L` grade: stays `SUSPENDED-PENDING-INSTRUMENT`** — ### **but for the narrow and correct reason, which is
that the operator layer is missing, NOT that the record is inconsistent.** *The inconsistency claim is
withdrawn.*

---

## §4 — EXPERIMENT ONE: ### STILL NOT RUN, SAME GATE

**It measures the negative fraction of `Φ`, which is the `Q_ε`-derived form.** The corrected design is right
— the lag schedule `log q @ L > q` is the arithmetic reading and repairs the discrepancy flagged two passes
ago — **but the thing it would measure with does not exist yet.**

### **NO MEASURED NUMBER APPEARS IN THIS REPORT.**

---

## §5 — THE APOSTOL RIDER: ### BLOCKED, AND I WILL NOT MANUFACTURE IT

**Apostol is not on disk** — `find` over `D:` returns nothing. The corpus already records this: *"Apostol
Ch. 11 page-level — executor-runnable; **needs library access**"*, and the Euler spec carries *"the page-level
Apostol Ch. 11 upgrade is outstanding."*

> ### **I CAN NAME A CHAPTER AND A LIKELY THEOREM FROM RECALL. I WILL NOT PUT ONE IN THE S-TABLE OR THE
> BIBLIOGRAPHY.** *The rider's whole purpose is to **retire a tertiary citation**. Replacing it with an
> unverified number while labelling it "read at content" would launder an unchecked claim onto the audited
> surface —* ### **strictly worse than leaving the tertiary citation standing and visible.**
>
> **Kin: *a retrieval gloss is not the source* · *verification probes take exact strings, never paraphrases*.**

**What would close it:** the book, or a page image of §11's Euler-product theorem. *One sitting once the
source is in hand.*

---

## CLOSING — FOR THE AUTHOR'S WORD

1. ### **MY CONTRADICTION FINDING IS WITHDRAWN** — corrected in `THE_ATTEMPT_RECORD` at the correction it
   damaged, not quietly.
2. ### **15 / 15 REACHABLE BATTERY ROWS PASS.** The prolate/ε substrate is certified, including all five
   `t(n)` and `ε′(1⁺)`.
3. ### **CORRECTION FIFTEEN CONFIRMED** — artifact `8733.4`, corrected `17491.3`, both to five figures.
4. ### **ONE THING IS MISSING AND IT IS NAMEABLE: eq. (100).** *Supply `Q_ε` verbatim and the remaining eight
   rows, the `δ/L` grade restoration, and Experiment One all follow in a single sitting.*
5. ### **THE APOSTOL RIDER IS BLOCKED ON THE BOOK**, and is reported blocked rather than filled in.

### **STILL HELD:** the two `W-CARRIER-BUILD` acts — committed at `relay` tip, unpushed, absence re-verified.

**`h2` UNCHANGED. NO SIGN. NOTHING DEPOSITS.**
