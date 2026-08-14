# W-ATTEMPT-1 — SITTING 6: §6 AT CONTENT — **BLOCKED, SECOND DOOR**

**Relay report · 2026-08-13 · ATTEMPT track · relay-only · sub-gate carried · gloss-refusal at string level**
### **§6 DID NOT OPEN BY EITHER ROUTE. THE SITTING STOPS WHERE THE READ STOPS, PER THE FERRY'S OWN CLOSING RULE.** **Nothing deposits.**

---

## §1 — THE READ: TWO DOORS, BOTH SHUT

| door | result |
|:--|:--|
| **arXiv PDF** (`arxiv.org/pdf/2006.13771`) | ### **FAILED TO PARSE** — *"PDF object structure (streams with FlateDecode filters) … the actual mathematical definitions and theorems from Section 6 are not accessible."* **Same failure mode as `2207.00665` at sitting 2.** |
| **ar5iv HTML**, §6-targeted | ### **TRUNCATED** — *"The provided document excerpt ends mid-document during Section 5, before reaching Section 6 entirely."* |

> ### **SITTING 4 NAMED THE FIX AS "THE PDF OR THE PUBLISHED VERSION." THE PDF HAS NOW BEEN TRIED AND HAS
> FAILED. THE FIX WAS HALF-RIGHT, AND THE HALF THAT REMAINS IS THE PUBLISHED VERSION / SELECTA — WHICH THIS
> EXECUTOR CANNOT REACH.**

### The four requested items

| | requested | result |
|:--|:--|:--|
| **(a)** | the Toeplitz operator's definition, symbol, space, relation to `K_I` | ### **NOT-FOUND-AT-RETRIEVAL** |
| **(b)** | the reference level / the `N_I = −2ε′(1⁺)(Id − K_I)` normalization | ### **NOT-FOUND-AT-RETRIEVAL** |
| **(c)** | the full "only one eigenvalue `> 1`" statement — which `q`, which limit, which eigenvector | ### **PARTIAL — the sentence only** |
| **(d)** | the chain from spectral count to `13 < c < 17` | ### **NOT-FOUND-AT-RETRIEVAL** |

---

## §2 — WHAT DID COME BACK — **FROM THE INTRODUCTION, NOT FROM §6** — AND IT CORRECTS SITTING 5

### **(c), partial, verbatim:**

> *"The key observation in 2. is that, **for `q ∼ 1`, the operator `K_q` has only one eigenvalue `> 1`**."*

**A regime (`q ∼ 1`), not a specified `q`; no limit stated; no eigenvector identified.** *The three things
sitting 5 needed in order to write the analogue count are still the three things missing.*

### ### **THEOREM 6.11 / "THEOREM 11", VERBATIM — AND IT IS NOT WHAT SITTING 5 SEATED**

> *"there exists a finite constant `c` (with `13<c<17`) such that, for any
> **`g ∈ C_c^∞([2^{−1/2}, 2^{1/2}])`** whose Fourier transform vanishes at `i/2` (`ĝ(i/2)=0`) one has
> `W_∞(g*g*) ≥ Tr(ϑ(g)𝐒ϑ(g)*) − c|ĝ(0)|²`"*

> ### **CORRECTION TO SITTING 5, AND IT IS MATERIAL. Sitting 5 wrote the inequality without its hypotheses
> and "seated Theorem 6.11 as the attempt's floor."** ### **THE THEOREM IS STATED ON `[2^{−1/2}, 2^{1/2}]` —
> THE ALREADY-PROVEN WINDOW. IT SAYS NOTHING ABOUT `[3^{−1/2}, 3^{1/2}]`, AND IT IS THEREFORE NOT THE
> EXTENSION'S FLOOR. IT IS A FLOOR ON THE OLD WINDOW.**

**What survives of sitting 5's reading, and it survives intact:** *the theorem's hypothesis is `ĝ(i/2)=0`
**alone**, and the penalty is `c|ĝ(0)|²`.* ### **So `6.11` is a RELAXATION of Theorem 1 — it drops the
`ĝ(0)=0` condition and quantifies what that costs. Imposing `ĝ(0)=0` recovers Theorem 1's clean floor
exactly.** *Sitting 5's "the second vanishing condition has a job" is confirmed, by the theorem's own
structure.*

### **AND IT HANDS THE EXTENSION A CHOICE OF CLASS, WORTH NAMING**

> *Codimension **two** (`ĝ(i/2)=ĝ(0)=0`): clean floor `Tr`, thinner class.*
> *Codimension **one** (`ĝ(i/2)=0` only): floor `Tr − c|ĝ(0)|²`, `c < 17`, **wider class at a quantified
> price**.* ### **`6.11` IS THE PRICE LIST FOR THAT TRADE — on the proven window. Whether the trade exists at
> all on the wider window is unknown, because the theorem does not go there.**

### One discrepancy against the supply, recorded

*Sitting 5's supply placed `ε′(1⁺) ≈ 22.9965` at **Lemma 5.4**; this retrieval places it at **equation (14)**.*
### **Content agrees, location differs. Recorded, not resolved — exactly the class of drift the renumbering
caveat warned of.**

---

## §3 — THE TRANSFER SHAPE: ### **NOT WRITTEN, BY THE FERRY'S OWN RULE**

> ### **THE FERRY'S CLOSING: *"the computation happens only against the read operator, never a guessed one."***
> ### **§6's OPERATOR WAS NOT READ. ITS SYMBOL, ITS SPACE, ITS RELATION TO `K_I`, AND ITS REFERENCE LEVEL ARE
> ALL `NOT-FOUND-AT-RETRIEVAL`. THE TRANSFER SHAPE IS THEREFORE NOT WRITTEN.**

**What I decline to do, said explicitly so the gap is not filled later by drift:** *I will not write "what
changes in the symbol" for a symbol I have not seen, nor rule "finite-rank vs spread-through" for a kernel I
have not seen.* ### **Those two questions are the whole of task 2, and both are answerable only at the
operator.**

**What stands unchanged from sitting 5, and needs no operator:**

> ### **THE NECESSITY/SUFFICIENCY SPLIT.** *Necessary: at most **two** eigenvalues above the reference, since
> the constraint subspace has codimension two and min–max gives `μ₁ ≥ λ₃`. **Not sufficient**: codimension two
> removes two **specific** directions, and interlacing yields `μ₁ ≤ λ₁`, never `μ₁ ≤ 1`. Sufficiency needs the
> two functionals non-degenerate against the offending eigenspace.*
>
> ### **BRANCH-B COST, RESTATED VERBATIM FROM SITTING 5:** *"further vanishing conditions on `ĝ` buy further
> codimension — but every condition shrinks the admissible class, and a class thin enough to carry the count
> may be too thin to carry Weil positivity's meaning."* ### **And `6.11` now sharpens the other direction of
> that same trade: conditions can also be DROPPED for a quantified penalty. The class is a dial, and `6.11`
> prices one click of it on the proven window.**

---

## §4 — ε: HELD, AND ITS SEQUENCING CANNOT BE DECIDED

**Price held at `~1–1.5 sittings`. Not run.**

> ### **THE FERRY MADE ε's PLACE CONDITIONAL ON THE TRANSFER SHAPE — "after §6, if the transfer shape says the
> ε-map informs the kernel's prime-term structure; skipped if it doesn't."** ### **THE TRANSFER SHAPE WAS NOT
> WRITTEN, SO THE CONDITION CANNOT BE EVALUATED. ε IS NOT SCHEDULED AND IS NOT SKIPPED — IT IS BLOCKED BEHIND
> THE SAME DOOR.**

**Reach-theorem disclaimers unchanged: a favourable budget map decides nothing.**

---

## CLOSING — REVIEW

**Nothing proof-shaped emerged. No sign step exists to price.** **Banked to relay only.**

**Returning for the author's word:**
1. ### **§6 IS BLOCKED AT TWO DOORS — ar5iv truncates mid-§5, the PDF does not parse. The attempt has now failed the same retrieval twice by different routes.**
2. ### **A MATERIAL CORRECTION TO SITTING 5: Theorem 6.11 is stated on `[2^{−1/2}, 2^{1/2}]`, the PROVEN window, with `ĝ(i/2)=0` alone. It is not the extension's floor. Sitting 5 seated it as one by quoting the inequality without its hypotheses.**
3. ### **What survives: `6.11` is a relaxation of Theorem 1 that PRICES the `ĝ(0)=0` condition at `c < 17` — the class is a dial, and this is one click of it, on the old window.**
4. ### **THE TRANSFER SHAPE IS NOT WRITTEN, BY THE FERRY'S OWN RULE. I declined to characterize an unread symbol and an unread kernel.**

> ### **THE ROUTE FORWARD IS NOT MATHEMATICAL AND NOT MINE: the published version or Selecta, read by someone
> who can reach it. Six sittings in, the attempt's next step has been a fetch for three consecutive sittings,
> and the last two have failed. That is the state, said without dressing.**

**`h2` UNCHANGED. NO SIGN. NO MECHANISM CLAIMED. NOTHING DEPOSITS.**
