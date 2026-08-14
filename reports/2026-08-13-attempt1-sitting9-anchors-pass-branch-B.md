# W-ATTEMPT-1 — SITTING 9: ANCHORS PASS · LOG-2 GATE PASS · **BRANCH B FIRES**

**Relay report · 2026-08-13 · ATTEMPT track · relay-only · sub-gate carried**
### **BOTH PARTS RECEIVED IN FULL (1 of 2, 2 of 2, both `paste ends` markers, items 1–5 closing). RULE 1 SATISFIED. EXECUTED.** **Nothing deposits.**

> ### **THE STANDING INSTRUCTION IS HONOURED ABSOLUTELY: NO SENTENCE ABOUT `W_∞ − W_2`'s SIGN APPEARS IN THIS
> REPORT. The prime-term pass was not reached, and no sign claim is made, implied, or hinted from what was.**

---

## §1 — THE ANCHOR BATTERY: **PASS ON EVERY ROW**

*Stable across `NQ = 400` and `NQ = 700`; identical to all printed digits.*

| row | computed | target | agreement |
|:--|:--|:--|:--|
| **(i)** `Σ λ(n)²` | `2.237484834940` | `2(Si(4π)/4π + 1) = 2.237484834942` | ### **`2.2 × 10⁻¹²`** |
| **(ii)** `Σ λ(n)² ξ_n(1)²` | `1.999999999948` | ### **`2` exactly** | ### **`5.2 × 10⁻¹¹`** |
| **(iii)** `t(n)` | `11.9719 · 8.77574 · 2.20528 · 0.0433983 · 0.000125459` | CC Lemma 5.4, same five | ### **all ≤ `2.7×10⁻⁶` relative; Σ = `22.996476` vs `22.9965`** |
| **(iv)** `Qε(1)` | ### **`0.0`** | `0` identically | ### **exact** |
| **(v)** `\|ξ_n(1)\| ≤ (2π)^{2n+½}` | `0.02618, 0.60948, 2.41323, 3.52614, 4.09936, 4.57184` | rail | ### **holds** |

> ### **SITTING 8's OPEN `t(n)` MISMATCH IS RESOLVED — BY SUPPLY, NOT BY FIT.** *The missing factor was
> `ξ_n(1)²`, exactly as the ferry stated. My sitting-8 weights were correct and incomplete; I compared a
> weight to a weight×endpoint and reported the gap rather than guessing a convention to close it. **The
> refusal to fit was the right call and the supply vindicated it.***

---

## §2 — THE LOG-2 VALIDATION GATE: **PASS**

*Their parameters: `I = [−½log2, ½log2]`, `ω = 1e−3`, normalization `ω/(2ε′(1⁺))`, `M = 694`.*

| mode | computed | CC | parity computed | CC (Remark 6.7) |
|:--|:--|:--|:--|:--|
| `λmax` | ### **`1.051772`** | `1.05158` | ### **EVEN (`+1.0000`)** | even |
| `λ₂` | `0.687924` | `0.686494` | ### **ODD (`−1.0000`)** | ### **odd** |
| `λ₃` | `0.029692` | `0.0289` | EVEN | — |

> ### **THE PARITIES REPRODUCE EXACTLY — EVEN / ODD / EVEN — INCLUDING REMARK 6.7's ODD SECOND MODE, WHICH
> IS THE STRUCTURE SITTING 7's PARITY LEDGER RESTS ON.** *Eigenvalue agreement degrades with mode index
> (`1.8×10⁻⁴`, `2.1×10⁻³`, `2.7×10⁻²`) — the expected signature of finite quadrature and 11-term truncation,
> not of a wrong object.*

### **THE GATE IS PASSED. EXTENSION NUMBERS ARE LICENSED.**

---

## §3 — THE LOG-3 SPECTRUM, WITHOUT THE PRIME TERM

*Same instrument, same `ω`, interval length `log 3 = 1.098612`, `M = 1100`.*

| mode | eigenvalue | parity |
|:--|:--|:--|
| 0 | ### **`1.089917`** | EVEN (`+1.0000`) |
| **1** | ### **`1.039477`** | ### **ODD (`−1.0000`)** |
| 2 | `0.684763` | EVEN |

> ### **EIGENVALUES EXCEEDING `1`: **TWO**. AND THE SECOND IS **ODD**.**
>
> ### **THE ODD MODE RISES FROM `0.687924` AT LENGTH `log 2` TO `1.039477` AT LENGTH `log 3` AND CROSSES `1`
> STRICTLY INSIDE THE BAND.**

## ### **§4 — BRANCH B FIRES, EXACTLY AS PRE-COMMITTED AT SITTING 7**

**Sitting 7 wrote, before any number existed:** *"BRANCH B: `λ₂` crosses `1`. Then an ODD eigenvalue exceeds
the reference, `ĝ(0)=0` is vacuous against it, and the budget is at most one for two offenders."*

> ### **THAT IS WHAT THE COMPUTATION RETURNED.**

**The parity ledger, applied:**

| offender | eigenvalue | parity | can the constraints reach it? |
|:--|:--|:--|:--|
| mode 0 | `1.089917` | EVEN | ### **YES** — `ĝ(i/2)=0` and `ĝ(0)=0` both act on even directions |
| **mode 1** | ### **`1.039477`** | ### **ODD** | ### **`ĝ(0) = ∫g` VANISHES IDENTICALLY ON ODD FUNCTIONS — that condition is VACUOUS here. The budget against this offender is at most ONE.** |

**Sitting 5's necessity bound, checked:** *at most two eigenvalues may exceed the reference, since the
constraint subspace has codimension two.* ### **THERE ARE EXACTLY TWO. THE NECESSARY CONDITION IS AT ITS
BOUNDARY — and it was never sufficient, because codimension two removes two SPECIFIC directions and one of
the two offenders is parity-orthogonal to one of the two conditions.**

### **THE ROUTE'S OPEN QUESTION, NOW LIVE AND DECISIVE — AND NOT RESOLVED NUMERICALLY, AS PRE-COMMITTED**

> ### **DO PROP C.1's ADDITIONAL VANISHING CONDITIONS AT NON-REAL `z ∈ F` ACT NON-TRIVIALLY ON ODD
> DIRECTIONS?** *Prop C.1 licenses any finite `F` without destroying the criterion (sitting 7, at cite). If
> conditions at general `z` see odd data, the budget can be extended and the route survives. **If they are
> all even-type, the odd offender is unreachable and this route closes.***
>
> ### **SITTING 7 NAMED THIS QUESTION BEFORE ANY NUMBER EXISTED TO TEMPT A VERDICT. IT IS NOT ANSWERED HERE
> AND IS NOT GUESSED.**

---

## §5 — WHAT WAS NOT RUN, AND WHY

* ### **THE PRIME-TERM PASS (log-3 WITH `√2 log2·[(ξ′⋆ξ′*)(log2) + ¼(ξ⋆ξ*)(log2)]`): NOT RUN.** *Context exhausted. It is a well-defined next computation on a validated instrument and would only add to the offender count, never subtract.*
* **Lemma 5.2's re-derivation on `(1,3]`: NOT RUN.** *The `Qε` series was evaluated on `(1,3]` as supplied; its validity there is exactly the un-re-derived item, and the numbers above inherit that dependency. **Declared, not buried.***
* **The Fact 6.1 trap stayed armed and untripped** — `τ(λ,α,d,m)` was never used as an input; every number above comes from the series (100).

---

## CLOSING — REVIEW

**No sign step exists to price; nothing proof-shaped emerged.** **Banked to relay only.**

**Returning for the author's word:**
1. ### **ALL FIVE ANCHORS PASS; THE LOG-2 GATE PASSES WITH CORRECT PARITIES. The instrument is validated against CC's own published numbers at five independent points.**
2. ### **AT LENGTH `log 3` THERE ARE TWO EIGENVALUES ABOVE `1`, AND THE SECOND IS ODD (`1.039477`).**
3. ### **BRANCH B FIRES AS PRE-COMMITTED. The pre-commitment was written at sitting 7 with no number in hand and it described what happened.**
4. ### **THE DECIDING QUESTION IS NOW PARITY, NOT MAGNITUDE — whether Prop C.1 conditions at non-real `z` reach odd directions. Unanswered, unguessed.**
5. **Outstanding dependency declared: Lemma 5.2 on `(1,3]` remains un-re-derived and every log-3 number inherits it.**

> ### **THE ATTEMPT HAS ITS FIRST HARD ADVERSE NUMBER, AND IT ARRIVED ON A BRANCH NAMED IN ADVANCE. THAT IS
> THE DISCIPLINE WORKING, NOT THE ATTEMPT FAILING — AND IT IS STILL NOT PROGRESS ON THE CLAUSE.**

**`h2` UNCHANGED. NO SIGN. NOTHING DEPOSITS.**
