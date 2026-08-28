# THE ARRANGEMENT AND THE IMPORT BAR — b233, 2026-08-28

**Scope:** reads, a settlement-by-citation or a routed ruling, and one bench computation touching
only the import's own two sides. ### **The corpus's left side (T, Q) appears nowhere in the
computation.** Nothing about the h2 identity beyond the register sentence exact. Nothing deposits.

**The ruling carried (import bar), the author's:** *"Imports are verified ourselves where we have
the tools, not only trusted. The import ledger gains a verification column — VERIFIED-INTERNALLY /
VERIFIED-AT-BENCH / TRUSTED-AT-CITE … Sourcing stays explicit in every grade."*

---

## The two verdicts

1. ### **THE ARRANGEMENT: branch (iii). The texts underdetermine it.** Routed to the author, **no
   arrangement chosen**, the identity's statement marked **ONE-RULING-FROM-COMPLETE**.
2. ### **IMP-1 AT BENCH: the registered pass-criterion failed at every cell and every axis.**
   IMP-1 is **not** graded VERIFIED-AT-BENCH; it is held at **TRUSTED-AT-CITE** with a work-order.
   *The two sides do agree to ~2e−8 relative — but not under the criterion this act registered
   before it looked, and **a criterion rewritten after the numbers is not a criterion**.*

---

## 1. The arrangement

With both columns defined — `wPrimes = PR` (b229), `wInf = −A` (b232) — File E's right side is
`−A − PR`; CC's places-sum is `−A + PR`. They differ in the prime term's sign.

### **File E names its fields and writes its operator. It nowhere states the operator's intent.**

- **(i) the minus as File E's own knowing convention** — needs a quotation. ### **(ABSENT).**
  Searched at content: File E whole (66 lines); the chain's every `wInf`/`wPrimes` line; **every
  occurrence of `wPrimes` in `relay/reports` — 15 lines, 8 files**; the acts narrative.
  *Positive control: those searches returned all 15 lines and File E's own three texts.*
- **(ii) File E intends CC's sum** — needs File E's **text** to license `wPrimes = −PR` or
  `wInf + wPrimes`. ### **It licenses neither**: it writes a minus and calls the field "the prime
  sum".
- **(iii) underdetermined** — ### **the verdict.**

> ### **The strongest evidence for (ii) is an owner's sentence that is not a licence.** The acts
> narrative §25(c): *"L1+L2+L3 assemble to `object ≤ W_∞ + Σ_p W_p` (**the primes enter
> POSITIVELY** via L3) — **not the dictated `W_∞ − Σ_p W_p`**."* The corpus's own banked links
> assemble to CC's form. ### **That is evidence about the mathematics, not a licence to rewrite a
> stated object** — amending File E's operator on an inference would be changing a stated object to
> make an assembly work. And the sentence's second half — *"fails numerically in BOTH conventions"*
> — is a comparison coming out and ### **was not consulted.**

**The diagnosis, stated and not adopted.** File E's minus is exactly right under **Day-1's**
convention (`A − PR` — the corpus's own `LEFT` column, computed under that very name at §20(a)) and
names **no object the corpus computes** under CC's. b232 found the corpus carries two `W_∞`s;
### **b233 finds that File E may carry one of each.**

**The ruling asked for** — *which of File E's two texts governs, the docstring or the operator?* —
with three outcomes at `THE_IDENTITY_CHAIN` §36 and **none recommended**.

---

## 2. The bench

CC's equation (1), both sides, at the ### **diagonal a² cells 2, 3, 4** *(the (2,1)/(3,1)/(2,2)
provenance pairs; the species is said — diagonal a², not local (p,n))*.

**G-ZEROS:** `mpmath.zetazero`, **N = 1000 registered before the first number**, computed fresh.
### **Control against the banked ordinates: max deviation 0.000e+00 — CONTROL PASSES** (the script
halts on its failure rather than reporting anyway).
**G-SIDES:** `b38_act10.left_side`, **imported unmodified** — chosen over `carto_atlas.channels`
because ### **the two are for different test functions** (`w` vs `corr = w ⋆ w`; b38 carries the
squares that are the autocorrelation transform's signature), and b229/b232 adopted from b38.
**G-STAB:** five axis settings.

| diagonal a² | Z (zeros) | P (pole) | A (arch) | PR (primes) | residual | tail bound |
|--:|--:|--:|--:|--:|--:|--:|
| 2 | 0.018987400 | 2.009515028 | −1.990527627 | 0.000000000 | 1.216e−13 | 7.195e−21 |
| 3 | 0.008592123 | 2.023976118 | −1.908900329 | 0.106483707 | 4.136e−08 | 3.159e−26 |
| 4 | 0.002474817 | 2.038292259 | −1.786497854 | 0.249319596 | 8.550e−09 | 1.072e−27 |

> ### **The registered criterion — "the truncation tail, not the mathematics, bounds the residual" —
> failed 15 of 15 cell-axis pairs.** The tail bounds came out at 1e−21…1e−27 because `ĥ²` decays
> super-exponentially. ### **I registered the one error source that turned out to be negligible.**
>
> ### **The grade follows the criterion, not the impression.** The one move that would have
> delivered a clean VERIFIED-AT-BENCH — replacing the tail bound with a budget fitted to what came
> out — is the move this programme exists to refuse. ### **No axis was tuned and the bar was not
> moved.**

**The failure diagnosed — and the diagnosis partly refutes itself.** The residual is **invariant
under the zero truncation** (identical at N = 500/750/1000) and falls with the places-side grid.
Hypothesis: the prime column's `np.interp` is linear, so `O((Δv)²)`, ratio ≈ 4 per doubling.
Result, NV = 2001→16001: a²=2 **1.00, 1.00, 1.00** (flat at ~1.2e−13; its prime column is **empty**,
`PR = 0` exactly); a²=3 **2.39, 3.28, 9.07**; a²=4 **2.08, 2.18, 2.43**. ### **Confirmed in
direction — the places-side quadrature dominates — and refuted in its exponent: the order is between
first and second**, because `corr` is itself a discrete convolution scaled by `dv`. ### **And the
diagnostic does not rescue the verdict:** at the finest grid the a²=3 residual is still 1.4e−9,
fifteen orders above its tail bound. **The criterion was the wrong criterion — that is this act's
finding about its own method.**

**A third corroboration of b232, unsought:** the table gives `A = −1.9905…` at diagonal a² cell 2, so
`−A = +1.9905…`, and the narrative §25(c) quotes **`W_∞^CC = 1.99`** at that same cell.

---

## 3. The ledger, the amendment, the note

**The verification column** (`THE_IDENTITY_CHAIN` §35.1): **IMP-1 → TRUSTED-AT-CITE**, work-order
`W-ORD-IMP1-BUDGET` (re-run with a correct error budget **registered in advance**).
**IMP-2 → TRUSTED-AT-CITE** — its load is a **labelling**, not reachable by a residual — work-order
### **`W-ORD-IMP2-TAU`, which is genuinely tool-reachable**: compute CC's own eq. (53)
`𝒲_∞(f) = −∫ f(ρ^{−1}) τ(ρ) d*ρ` with (39)'s τ, principal value at ρ = 1, and compare to `−A`.
*Filed, not run.* ### **The bar's first use produced a non-promotion. That is the bar working.**

**§34.5 — the amendment.** b232 described the instrument's arrangement as *"committed before any
answer"*. ### **The docstring itself appends `[sign fixed BY the E2 calibration]`**, which
`SIGN_ARRANGEMENT` §1's quotation does not carry. Assessed against the texts and no number: ### **it
qualifies b232's step 2 without overturning the verdict** — CC's eq (1) fixes the orientation on its
own, the arrangement was used only to match term classes, and b232's corroboration never used it.
**But my sentence was stronger than its source; the originals stand unedited above the amendment.**

**The {2,3} cross-arc note, at PATTERN grade, no promotion.** The week's towers ran on the
substrate's own two primes (b223's p = 2,3; b224's local (p,n) cells (2,1),(3,1),(2,2); the diagonal
a² bench cells 2^a·3^b). The **2-exceptionality** is already compiled (`SectorNonvanishingShadow`:
odd `4d = (q−1)²` against place-2 `4d = q(q−2)`, with *"the death at (2,1) is the law's OWN value"*).
FINDINGS' own `{2,3} substrate-unity signature` entry is quoted whole; `F2_gap_free :
frobeniusNumber 2 3 = 1` located in `Kernel/Enumera.lean` with the two contrast terminals.
### **An absence with its positive control: no compiled `−1/2` was located** — the same method found
the three Frobenius terminals next door — ### **so the `−1/2` is FINDINGS' Berry–Keating indicial
exponent, listed as a Phase-1.1 reading, not a kernel result.** *A pattern is a reason to look, never
a reason to believe.*

---

## 4. Gates and scans

**b233's gates: 14 of 14 PASS, CLEAN — on the second run.** The first returned **13 PASS, 1
REFUSED** by b217's **witness** guard: the inadmissibility gate asked the narrative for *"fails
numerically in BOTH conventions"*, which the **source carries line-wrapped**, so the exact substring
is absent there though present in the bank's own quotation. ***b227's species, third act running.***

**PLACE-papers term scan CLEAN** (354 lines). ### **Relay term scan NOT CLEAN — 2 live uses, and
both are inside a verbatim quotation of the corpus's own sentence** (*"The assembly gap, also
named"*, the narrative §25(c), quoted in the registration and the bank). The tool's declared
exceptions cover quoted kernel identifiers, Clay/bibliography citations, retired terms in correction
records, and its own rule text — ### **none covers verbatim owner-quotation.** ### **I kept the
quotations and am reporting the scan as it stands: an executor does not invent an exception to a
rule the author set, and wrapping the phrase in backticks to satisfy the regex would be gaming a
check rather than passing it.** *Routed as an observation: whether verbatim owner-quotation deserves
a declared exception is the author's call. Both sidecars carried.*

**SGS untouched** — this act edits nothing in the kernel.

---

### **What this act did not do:** ### **no arrangement chosen; no axis tuned; no bar moved.** No
number was consulted in settling the arrangement — and the arrangement was not settled. File E
quoted, not edited. The corpus's left side appears nowhere in the computation. ### **Nothing about
h2 beyond the register sentence exact. Nothing deposits. Locks last.**
