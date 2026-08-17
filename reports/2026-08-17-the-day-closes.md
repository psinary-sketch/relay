# THE DAY CLOSES — ### **A DERIVED LAW, A REFUTED MECHANISM, AND ONE OPEN QUESTION WITH AN ADDRESS**

**Relay report · 2026-08-17 · author-called · the day's close · relay-only for bench · nothing deposits**
**`h2` UNCHANGED. NO SIGN SENTENCE. `WIDEN` PAUSED. RAIL DID NOT MOVE.**

```
PLACE-papers  origin/main : 4de156e8194fa1ed0df15ac25c571f4b79b23ffb   VERIFIED (ls-remote)
SIDE-window   origin/main : ab6f26946852edb4e9fdce287451509819d09d16   VERIFIED · tag v0.4.0 = 1bd2865
relay         origin/main : (this report)                              local +1 HELD
mirror        mirror-refresh-2026-08-17.zip @ 4de156e   ### 22 / 22 COHERENT, three ways
SIDE-effects  afa9ccf — untouched all day
```

---

## §1 — THE THIRD WINDOW · ### **THE SCALING LIMIT IS REFUTED, BY THE DAY'S OWN LAW**

*Hours earlier this day filed a SCALING LIMIT from two windows — `L = 16` and `L = 64`, node-matched
overlaps `0.9847 · 0.9944 · 0.9952 · 0.9927 · 0.9657`. The standing law minted this morning says a law read
off a range is a law about that range.* ### **`L = 256` (`r = 8`) is the cell outside it.**

| pair | node-matched overlaps in `u` | verdict |
|:--|:--|:--|
| `L = 16` vs `L = 64` | `0.9847 · 0.9944 · 0.9952 · 0.9927 · 0.9657` | ### **HOLDS** |
| ### **`L = 64` vs `L = 256`** | ### **none — the node counts do not line up** | ### **DRIFTS** |
| ### **`L = 16` vs `L = 256`** | ### **none** | ### **DRIFTS** |

**And the count does not extend:** `NPOS(A_main)` = `5` at `r = 4`, `8` at `r = 6`, ### **`37` at `r = 8`.**

### **THE MATCHED-PAIR CONTROL, RUN BEFORE THE VERDICT WAS WRITTEN**

*`M` and `r` had grown together in every cell measured — confounded. The corpus's own instrument for exactly
this is the matched-pair collision, and the arithmetic hands one over free:* ### **`L = 16` at `ω = 10⁻³`
and `L = 256` at `ω = 2×10⁻³` have the same `M = 2773`, to the point.**

| `L` | `ω` | `M` | `r` | `NPOS` at floors `0 / 10⁻⁶ / 10⁻⁵ / 10⁻⁴` |
|:--|:--|--:|--:|:--|
| 16 | `1e-3` | ### **2773** | 4.00 | `5 / 5 / 5 / 4` |
| 64 | `1.5e-3` | ### **2773** | 6.00 | `8 / 8 / 8 / 7` |
| ### **256** | `2e-3` | ### **2773** | ### **7.99** | ### **`37 / 35 / 34 / 30`** |

> ### **THREE CELLS AT AN IDENTICAL GRID DIMENSION. THE COUNT IS DRIVEN BY `r`, NOT BY `M`, AND IT SURVIVES
> A FOUR-DECADE THRESHOLD SWEEP.** *The spectrum's scale grows with it too — `|λ_min|` goes
> `5.6×10⁻⁴ → 8.5×10⁻⁴ → 1.9×10⁻²`.* **The reorganisation is a property of the window, not of the grid.**

### **WHAT SURVIVES, SO THE RETRACTION IS NOT OVER-READ**

*Four strong `u`-overlaps DO persist from `L = 64` into `L = 256` —* `0.9642, 0.9609, 0.9400, 0.9174` *— but
at* ### **shifted indices**, *and a NEW leading mode appears at `L = 256` with head mass `0.46` and an
eigenvalue four times the `L = 64` leader, matching nothing there (`0.223`).* **Individual members persist
in shape; the family as a whole reorganises and gains new members.** ### **That is not a scaling limit, and
it is not nothing.**

**INSTRUMENT CAVEAT, DECLARED:** *node-count labelling is unreliable at `r = 8` — near-degenerate
eigenvalues make sign-change counting noisy, and the positive tail runs to `3.6×10⁻⁸`.* ### **The overlaps
are the robust quantity; the count was checked against the floor sweep before it was reported.**

### **AND THE ANTI-ALIGNMENT RULE FAILS ITS THIRD TEST, BY ITS OWN REGISTERED BRANCH**

| | registered | measured |
|:--|:--|:--|
| positive exceptions at `r = 8` | ### **THREE** *(`n ≤ round(r/2)−1`, which reproduced `1` at `r = 4` and `2` at `r = 6`)* | ### **SIX** |
| negative-dominance on `r/2 < n < 3r/2` | HOLDS at `r = 4, 6` | ### **FAILS** — two band members positive |

> *The registered branch read: "if S2 gives anything else, the cos model predicted the `r = 6` change by
> luck, and the rule is filed as an observation about `r = 4` and `r = 6` only."* ### **IT GIVES SIX. THE
> RULE IS SO FILED, AND THE INEQUALITY CANDIDATE IS WITHDRAWN AS A CANDIDATE.**
>
> **A registration correction is worth recording too:** *the block first computed its predicted count from a
> literal `n < r/2`, which at `r = 8.0014` admits `n = 4` and would have said FOUR.* ### **That was caught
> and corrected before any measurement, with the literal count printed beside the registered one so that
> landing three could not later be read as fitting the rule to the answer.** *In the event neither number
> was right, which is what makes having written both down worth something.*

---

## §2 — THE LAW, AT ITS TWO GRADES · ### **AND THEY ARE TWO SENTENCES**

> ### **DERIVED — FOR THE PURE SHIFT-GRAPH FORM.**
> *Read the lag part as a graph on `{0,…,M−1}`: an edge `i ~ i+k` per live lag address.* **Every live `k` is
> odd, so index parity is a bipartition and `D S D = −S` for `D = diag((−1)ⁱ)`; hence the spectrum is
> symmetric and `NPOS = NNEG = (M − nullity)/2`, cycles or no cycles.** ### **And `NPOS = μ`, the MAXIMUM
> MATCHING NUMBER** — classical for forests, and measured to hold exactly at every cell tested including
> four carrying `204`–`700` independent cycles. **The sawtooth is its ONE-LAG EVALUATION**, `μ(P_m) = ⌊m/2⌋`
> and `Σ_r ⌊m_r/2⌋ = (M − #odd chains)/2`. ### **And the count is SILENT ON THE COEFFICIENTS away from a
> measure-zero degeneracy** — registered `2√q·log p` and Weil `4 log p/√q` give `1098` at `L = 9`, the
> degenerate `c₂ = c₃` gives `889`.

> ### **BENCH-GRADE — FOR THE FULL OPERATOR'S AGREEMENT.**
> *The measured count of `A = A_main + Σc_q(ω/2)S_{k_q}` on `V` sits within* ### **ONE offender** *of the
> pure form at every cell from `r = 1.7` to `r = 8`.* **That agreement is proved nowhere.** ### **`A_main` is
> uncontrolled, it is not negative semidefinite, and its positive index is now known to grow sharply with
> `r` — `5, 8, 37` at `r = 4, 6, 8`.**

**The sawtooth's own evidence, for the record:** `r = 1 … 8` without a miss, including the four apexes
`L = 4, 16, 64, 256` — the last two exact (`2079/4158` and `2772/5544`, both `0.500000`).

---

## §3 — THE MECHANISM, NAMED AND THEN LOST · **NO BOUND, AND NOW NO CANDIDATE EITHER**

*The anti-alignment was named with a mechanism —* `R(v_n) ≈ 2(1−1/r)·cos(nπ/r)` *— which reproduced
magnitudes away from its zero crossing (`r = 4, n = 4`: model `−1.500`, measured `−1.476`) and* ### **which
correctly predicted the exception count changing from one to two at `r = 6`, a window it had never seen.**
### **At `r = 8` it predicted three and the measurement gave six.**

> **So the day ends with the mechanism named and NOT carried.** *It describes `r = 4` and `r = 6`. It does
> not describe `r = 8`, and one correct out-of-sample prediction followed by one wrong one is exactly the
> evidential position where a rule is worth writing down and not worth using.*
>
> ### **NO BOUND WAS CLAIMED AT ANY POINT, AND THE TWO MISSING INGREDIENTS NAMED THIS MORNING ARE STILL
> MISSING** — *(a) completeness of the family for `A_main`'s positive part, (b) the cross terms under the
> lag form.* **A third is now added: the family itself is not stable across windows.**

---

## §4 — THE OPEN QUESTION, WITH AN ADDRESS

### **THE `L = 9 = 3²` DOUBLING**

*Adding the log-3 lag moves the count by* ### **`+285` / `+143` offenders at `L = 9`** *and by* ### **`−1` /
`+0` at `L = 12`.** *And `9 = 3²` is exactly the apex condition `SIDE-window` `v0.3` compiles for `p = 3`.*

| reading | what it says | what would show it |
|:--|:--|:--|
| ### **MATCHING-COUNT ACCIDENT** | at `L = 9` the added edges happen to lift the matching to near-perfect (`nullity = 1`); at `L = 12` they connect already-matched vertices. **Nothing about `p²`.** | the doubling appears at windows with no apex coincidence, and fails at some window that has one |
| ### **`p²`-FORCED** | the apex condition `L = p²` is what makes a lag's added edges maximally effective, so the doubling should track apexes | the doubling recurs at every apex window and nowhere else |

**THE DISCRIMINATING CELLS, PRICED:**

1. ### **A WINDOW AT THE log-2 APEX WITH BOTH LAGS LIVE.** *`L` just above `4` — the log-2 lag exactly at
   its own apex, log-3 live.* **If the doubling recurs there it tracks the apex condition; if it does not,
   `L = 9` was a matching-count accident.** *One sitting, the same instrument.*
2. ### **A NON-SQUARE WHOLE RATIO** — *`L = 27`, where `log L / log 3 = 3` exactly: a whole ratio in the
   prime that is not a square.* **The `p²` reading predicts nothing special; the matching-count reading
   predicts whatever the graph gives.** *One sitting, same instrument.*

*Both are cheap, both are pre-registrable, and neither is opened here.*

---

## §5 — THE MATHLIB COMPANION, AND A `v0.5` THAT MAY NOT NEED IT

**The spectral input** *(path spectra symmetric with nullity `1` iff odd)* **is NOT compiled.** *Verified by
grepping the checkout rather than from recall: Mathlib supplies `Matrix.IsHermitian`,
`LinearMap.IsSymmetric.eigenvalues`, the quadratic-form signature `sigPos`/`sigNeg`, `SimpleGraph.adjMatrix`,
`pathGraph`, `IsBipartiteWith` —* ### **and has NO tridiagonal determinant, NO path-graph spectrum, and NO
rank-equals-twice-matching identity.** **Both facts would have to be proved.** *Priced: ~half a sitting for
the bipartite symmetry, one to two for the tridiagonal recursion and its rank consequence, plus a Mathlib
build and the `v4.29.1 → v4.30.0-rc1` move. Separate package, own axiom check reporting the standard three.*

### **AND A `v0.5` TARGET THAT MAY AVOID MATHLIB ENTIRELY**

*`μ` is combinatorial, so it is decidable for fixed `M, k`.* **The certificate route:** exhibit a matching
`P` and a vertex cover `C` with `|P| = |C| = s`, both checked by `decide`. Then `μ ≥ s` from `P`, and
`μ ≤ s` because a matching's edges are disjoint and each needs its own cover vertex — ### **a one-line
pigeonhole, NOT König's theorem**, so no bipartite duality has to be imported.

> ### **THE RISK IS THE AXIOM PROFILE, AND TODAY GAVE THE WARNING:** *`turn_is_square` cost `propext` from a
> single `rw`, caught by the axiom print on its first run.* **An induction to prove `|matching| ≤ |cover|`
> will likely do the same; if it cannot be written in term mode it goes to the companion, and the vanilla
> library keeps only the `decide`-checked certificates — still a real statement.** *And a certified `μ` is a
> certified combinatorial number, not a certified inertia.*

---

## §6 — THE DAY'S CORRECTIONS, EIGHTEEN THROUGH TWENTY-TWO

| # | what it corrected | caught by |
|--:|:--|:--|
| **18** | `δ/L` = `1 − log2/logL` → `min(1 − log2/logL, log2/logL)` | a mechanism control that removed the extra lags and found the departure unchanged — ### ***a baseline that is assumed is not a baseline*** |
| **19** | that minimum → ### **a SAWTOOTH**, both branches being its `q = 1, 2` teeth | measuring at `L = 9, 12, 16, 20`, outside the range the minimum was read off |
| **20** | *"`A_main`'s positive directions are a fixed subspace"* → **L-dependent, the obstacle moves** | the count growing `2 → 4 → 5` at windows the claim had not seen |
| **21** | correction 20's outlook clause: there IS a family, fixed in `u` | a fourfold window separation |
| ### **22** | ### **that family → REFUTED. Two windows were not a scaling limit.** | ### **the third window, and the day's own standing law** |

### **AND THE METHOD LINE, ON ITS THIRD FIRING — THE THIRD CAME AFTER THE LAW EXISTED**

> ### **A LAW READ OFF A RANGE IS A LAW ABOUT THAT RANGE — ONE CELL OUTSIDE IS THE CHEAP DEFENCE.**
>
> *Three claims were made from ranges and three were corrected from outside them: the room branch
> (18, 19), the fixed subspace (20), the scaling limit (22).* **The law was minted after the second.**
> ### **IT CAUGHT THE THIRD, AND THE THIRD WAS MADE AFTER THE LAW EXISTED.**
>
> *A law that fires on its own author the same day it is written is doing the only thing a method law can
> do — and the cost of obeying it, all day, was one extra cell per claim.*

---

## §7 — WHAT THE DAY DOES NOT SAY

* ### **NOTHING ABOUT THE SIGN OF `W_∞ − W_2`. NOTHING ABOUT `h2`. NO OPERATOR INEQUALITY.**
* **`NPOS = μ` is measured, not proved.** *Bipartite symmetry and the halving ARE derived; the matching
  identity is classical for forests and was measured to survive cycles — which is not a proof that it does.*
* ### **NO BOUND on `|NPOS(A) − NPOS(S_k)|`**, and the missing ingredients have grown from two to three.
* **The `(1,3]` debt is unchanged.** *`REGIME-FREE` for the corpus-derivable parts; CC's Lemma 5.2, Prop
  5.5's interval hypothesis, and Lemma F.1 past `ρ ≈ 2.5` remain reads, and its trigger stands.*

---

## CLOSING — FOR THE AUTHOR'S WORD

1. ### **THE THIRD WINDOW REFUTES THE SCALING LIMIT.** *Verified against a matched-pair control at identical
   `M`: the count is driven by `r`, not the grid.* **Correction twenty-two.**
2. ### **THE LAW STANDS AT TWO GRADES, IN TWO SENTENCES.** `DERIVED` for the pure shift-graph form —
   `NPOS = μ`, the sawtooth as its one-lag evaluation, silence on coefficients away from a measure-zero
   degeneracy. `BENCH-GRADE` for the operator — one offender at `r = 1 … 8`, proved nowhere.
3. ### **THE MECHANISM IS NAMED AND NOT CARRIED** — right out-of-sample once, wrong once. No bound, and now
   no candidate.
4. ### **ONE OPEN QUESTION WITH AN ADDRESS** — the `L = 9 = 3²` doubling, two readings named, two
   discriminating cells priced at one sitting each.
5. ### **THE COMPANION IS PRICED; `v0.5` MAY NOT NEED IT.**

### **STILL HELD:** the two `W-CARRIER-BUILD` acts — **committed at `relay` local tip, UNPUSHED, absence from
the public tree re-verified against the remote after this pass's push.** *Release condition unchanged:
counsel's answer, then your word.*

### **THE FOUR STANDING RULINGS, UNMOVED ALL DAY:** `SIDE-effects` repair route *(returned unresolved
2026-08-14)* · day-1 digestion *(landed)* · the two prose rulings *(landed)* · `internal/` + `meta/`
*(ratified `CENSUS-ONLY`)*.

**`h2` UNCHANGED. NO SIGN. `WIDEN` PAUSED. RAIL DID NOT MOVE. NOTHING DEPOSITS.**
