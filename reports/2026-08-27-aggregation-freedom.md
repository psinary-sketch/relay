# b220 — THE AGGREGATION'S FREEDOM

**2026-08-27 · relay `reports/2026-08-27-aggregation-freedom.md`**
**Ferry part 1 of 1, receipt confirmed IN FULL. Registration banked after the owners' read and before the enumeration.**
**Bank: `data/b220_aggregation_freedom.txt` · profile `data/b220_core_print.txt` · index queries `data/audit_b220_index_query.txt` · gates `tools/b220_checks.py`.**

> *** ### **BRANCH (UNDERDETERMINED). The constraints the record imposes on term 2's aggregation
> leave EVERY function from a diagonal cell to `ℝ`** — not a point, not a finite-parameter family.
> ### **And the reason is sharper than "nobody has written it": the one constraint that would pin
> it is `h2` ITSELF, and deriving from it is circular.** ***
>
> ### **b215 offered "a RULING *or* a RESULT" as two open routes. One of the two is closed.**
> ### **No aggregation is adopted, defined, or compiled. File E is byte-identical to HEAD.**

## COMPONENT 1 — THE CONSTRAINTS (P1)

| constraint | owner | grade | demands of the aggregation |
|:--|:--|:--|:--|
| **C-TYPE** | File E, **read at source** | exact — it is the file | ### **NOTHING** |
| **C-NORM** | act 7 §2, ### **read at SOURCE, a first** | proof grade **modulo `ClassRichness`** (citation **UNREAD**) | ### **NOT STATED** |
| **C-WEIL** | act 9 §2 / act 7 §2 | ### **NOT AVAILABLE** | — |
| **C-FINITE** | b17, the staircase | definitional, compiled | ### **admits everything — it *widens*** |

**C-TYPE, read off the type.** `structure QuotientTrace (cell : DiagonalCell) where value : ℝ`.
### **No linearity, no per-place factorization, no positivity, no measurability.** One real per
cell, the cell's whole datum one rational with `1 < a_sq`. *The brief asks whether C-TYPE demands
linearity, factorization, real-valuedness, or none. The answer is **none**.*

**C-FINITE cuts against the enumeration, and that is worth saying plainly.** b17: *"ONE archimedean
bound `a` sets every place's effective cutoff `n_p(a) = #{k ≥ 1 : p^k ≤ a²}` … all places with
`n_p(a) ≥ 1`."* So `n_p(a) = 0` for every `p > a²` — ### **only finitely many places are active.**
### **A finite index set means every candidate assembly converges** — bare sum, weighted sum,
product, regularized sum, limit of truncations. ***Convergence discriminates nothing here.***
*The registration expected this might narrow the family; it widens it, and that registered
expectation was wrong in its direction.*

### *** WHY C-WEIL IS NOT AVAILABLE — TWO INDEPENDENT REASONS ***

**(1) It has no exact statement.** Act 9 §2 displays and proves
`τ_q(p,n,k)·p^{k/2} = (pⁿ − p^k)/(pⁿ − 1)` for `1 ≤ k ≤ n−1`, `0` for `k ≥ n`. What it says
*about* it is one sentence: *"The quotient channel's convergence to Weil's coefficients at the
level limit: PROOF GRADE longhand."* ### **That names no coefficients, no normalization, no
`log p`. It is a LABEL on the theorem, not an exhibited statement.** ***A constraint cannot be
applied if nobody has written down what it says.***

**(2) It is the conclusion.** Act 7 §2 closes: ### ***"Its coefficients against Weil's: part of
`(L-identity)`, NOT ASSUMED."*** — and §3 puts that comparison on the equation's **open** side.
File E's docstring: *"STATED, NOT PROVED, NOT CLAIMED … **Its truth at complete roster is `h2`**."*
### **So requiring the aggregate to reproduce Weil's coefficients is requiring
`T.value + Q.value = W.wInf − W.wPrimes`, which is `h2`.**

**And one further owner statement, listed and then excluded by its own author's warning.** b197
records the shape `Tr_∞ + Σ_p Tr_p` as **withdrawn**, *read-refuted by Theorem 2 of 2310.18423*.
That looks like a constraint and is not — b197's very next sentence: *"the withdrawal is about the
**Sonin** trace summand, not about File E's two-term split … recorded here **so that nobody later
reads it as if it did**."* ### **This act is the "nobody later", and it honoured the warning.**

## THE NAMING HAZARD (d), RESOLVED BEFORE C-WEIL WAS USED

*"Weil's coefficients"* names at least two objects: ### **(1)** the ledger/criterion (b179,
external — File E's `wInf`/`wPrimes`); ### **(2)** the explicit formula's prime-side coefficients
(b10: *"weight ~ `p^{−k/2}`, unit `log p` the period"*) — graded ### **QUESTION**, with b10's own
verdict *"MATCH-IN-SHAPE / NOT; no promotion either way."* ### **The record does not say which the
convergence line means, and neither reading yields a usable constraint** — (2) for want of a
statement, (1) because it *is* `h2`. *The level limit produces `p^{−k/2}` with no `log p` anywhere.*
### **The disambiguation the brief required is exactly what makes that visible.**

## COMPONENT 2 — THE FREEDOM (P2): **(UNDERDETERMINED)**

The admissible set is **all functions from a diagonal cell to `ℝ`**. ### **(FAMILY) does not land,
and it is worth being exact about why: a family needs at least one constraint that EXCLUDES
something, and not one of the four excludes any function.**

> *** ### **WHAT IS NEW HERE, AND IT IS NOT "b215 AGAIN."** b215 and b197 both reported the
> aggregation missing. ### **Neither asked why the obvious derivation is unavailable**, and the
> brief's clause (b) forced that question. ### **The obvious derivation is not a hard one nobody
> has done — it is an UNSOUND one.** It would define `Q.value := W.wInf − W.wPrimes − T.value` and
> then observe the identity holds. ***That observation is the definition.*** ***

**What is wanted now:** ### **a statement about the built object, INDEPENDENT of the
finite-instance identity, determining how `{ p^{−k(p,cell)/2} }_{p ≤ a²}` becomes one real.**
Three candidate sources, ### **each NOT ADOPTED, none written into File E:**

- **(i)** the **restricted-tensor trace** — act 7 §4: *"the infrastructure sorry (the Hilbert `⊗′`)
  is exactly where the forced normalization becomes a THEOREM — **the unit-normalized
  restricted-tensor trace is its statement**."* ### **The most promising named route, and not
  identity-dependent.**
- **(ii)** the diagonal section's **habit** — b17 defines `weight(a) = ∏ Q(p, n_p(a))`, a product.
  ### **A different object from `Q.value`, and a habit is not a constraint** — calling it one would
  be b219's double-name species again.
- **(iii)** an author's **ruling**.

*** ### **AND ONE TEMPTATION NAMED AND REFUSED.** C-NORM's TAIL joint reads *"the `E₁`-unit's
norm-1 forces **factor 1 at inactive places**."* ### **A factor of 1 at almost all places is the
signature of a PRODUCT** — in a sum an inactive term would be `0`. It is very tempting to read this
as forcing a multiplicative aggregation. ### **It does not.** The sentence is about the norm of the
**unit vector** in the restricted tensor product — b197's C₀ condition — ### **a statement about
the SPACE, not about `Q.value`'s assembly.** ***Two objects, one intuition, and the intuition is
not a warrant.*** ***

## COMPONENT 3 — THE SHADOW (P3), A REGISTERED DEVIATION THAT DELIVERED

(P3) conditions a build on the freedom being *"finite-decidable at a fixed cell (a linear-algebra
count)"*. ### **It is not — the freedom is all of `ℝ^(cells)`, which is no count.** So no shadow of
*the freedom* was built. ### **The deviation, registered in advance: a shadow of THE CIRCULARITY.**

`Core/AggregationCircularityShadow.lean` — ### **9 terminals, 9 of 9 at zero axioms.** Core
366 → 375, and `AXIOM_PRINTS.txt` still carries ### **zero** axiom-bearing lines.

| terminal | what it says |
|:--|:--|
| `unique` | the identity determines the quotient value **uniquely** |
| `cweil_determines` | an aggregation satisfies C-WEIL **iff** it returns that forced value — ### **the constraint does not NARROW a family, it PRESCRIBES one member** |
| `cweil_inhabited` | and that aggregation **always exists**, for any `t` and any ledger |
| `cweil_is_the_assumption` | ### **the punchline** — the proof the identity holds is the hypothesis **returned unchanged** (`:= h`) |
| `underdetermined_without_cweil`, `underdetermined_bool` | ### **the negative controls, run first** |

### **The controls are not decoration:** they establish the setup does *not* collapse to one
aggregation on its own, ### **so `cweil_determines` is measuring C-WEIL and not an artifact of the
encoding.** *A uniqueness theorem in a setting where everything is already unique proves nothing.*

**Correspondence row.** ### **CARRIES:** that a constraint of C-WEIL's shape determines its object
uniquely and is satisfiable for any inputs, hence carries no information about the identity.
### **DOES NOT CARRY:** anything about `ℝ` beyond additive cancellation; anything about the
quotient channel, the staircase, places, or levels. ***It is a shadow of the logical shape, not of
the mathematics.***

### *** TWO BUILD DECISIONS, RECORDED BECAUSE BOTH WERE CLOSE ***

**(i) The first version compiled — and was rewritten anyway.** It used `Int` and `omega`, and every
statement proved. Its profile: ### **four of six carried `[propext, Classical.choice, Quot.sound]`,
because `omega` does.** The registration had set the zero-axiom bar and said the file would be
dropped if it missed. ### **It was neither dropped nor accepted — it was REWRITTEN**, on b211's
precedent, as explicit `congrArg`/`Eq.trans` proofs over an abstract additive group. ***And the
rewrite made it honester, not merely cleaner: the abstract version states exactly what the argument
uses — additive cancellation and nothing else — where the `Int` version had helped itself to a
decision procedure over a ring.***

**(ii) The `Int` inhabitant was built and discarded.** The structure needs an inhabitant or every
theorem is vacuous — ### **b215's own shell test.** `intGrp` compiled, but printed
`depends on axioms: [propext]`, inherited from core Lean's `Int.add_assoc`. ### **Core's print is
366 lines with ZERO axiom-bearing entries, and this act declined to be the first to break that bar
for a convenience instance.** `Bool` under XOR was used instead — `ℤ/2`, a genuine group with two
distinct elements — ### **and it is the better witness anyway, since it instantiates the contrast
rather than satisfying it trivially.** *The `ℝ` transfer is stated in the file's prose, not smuggled
in as an axiom.*

## WHAT WAS **NOT** VERIFIED — SAID PLAINLY

### **NO G-CORE IS CLAIMED.** A per-file `lean` sweep over all 88 Core files returned ### **104
profiles, not 375**, with 80 error lines: the `AxiomCheck*.lean` files each import their companion
module and need built oleans on `LEAN_PATH`. ### **That is b218's finding in a new place, and it
means a per-file sweep is the wrong instrument for this repo's Core.** What *was* verified:
### **(i)** the new file prints 9/9 at zero axioms, directly measured; ### **(ii)** `git status`
shows **zero** modifications to any `.lean` file in the repository; ### **(iii)** the 366 prior
profiles were **not** re-measured here and are not claimed to have been. ***A claim of "366/366
unchanged" would have been cheap to type and was not earned.***

## THE INDEX — 5 HIT / 7 NO KEY, AND b219's FINDING REPEATS IN A SECOND LANE

### **All three distinct hits are CONCLUSIONS of acts** (`quotient-trace`, `class-richness`,
`weil-criterion`). ### **All seven misses are OBJECTS AND CONSTRAINTS** — `aggregation`,
`weil coefficients`, `level limit`, `forced normalization`, `volume normalization`,
`operator match`, `quotient lemma`. ### **b219 reported "a lane keyed by its verdicts and not by
its subjects" of the apportionment lane; the term-2 lane is keyed the same way.**
*Smaller point: `quotient lemma` misses while `quotient-trace` hits — the key exists and its own
common name is not an alias of it.*

> *** ### **AND THE QUERY LOOP REPRODUCED b216's WRONG-CWD SPECIES ON ITS FIRST RUN.** Issued as
> `python banked_index.py` from `/d/relay`, where the module does not exist — ### **twelve empty
> lines.** ### **It was caught for one reason: I refused to read an empty output as a result**,
> which is b217's rule applied by hand, one act after b219 recorded the same lane. ***Had the
> twelve been read as twelve misses, this act would have reported a lane-wide absence that is not
> there.*** ***

## THE GATES — 6 of 6 PASS, CLEAN

`core-print-has-no-axiom-bearing-line` · `shadow-adds-nine-zero-axiom-terminals` ·
`file-E-byte-identical-to-HEAD` · `act7-refusal-carried-into-bank` ·
`act9-range-condition-carried` · `shadow-defines-no-aggregation`

Each with a must-fail fixture **and** a must-pass witness, ### **the three states being three
distinct REAL files or paths.** The fixtures fail for the reason the check measures: the zero-axiom
fixture is `AXIOM_PRINTS_INTERFACES.txt`, which genuinely carries **29** axiom-bearing lines; the
untouched-file fixture is a path this act genuinely **did** modify; the quote fixtures are real
owner files that genuinely lack the quote.

## A DISCIPLINE NOTE — TWO OWNERS READ AT CITE FOR NINE DAYS

### **b220 read act 7 and act 9 AT SOURCE for the first time in the record's history.** Every prior
act — b189, b197, b215, b216's index row — carried them as quoted summary lines. Two things only a
source read could find:

- ### **act 9's range condition** `1 ≤ k ≤ n−1`, `0` for `k ≥ n`. ### **The per-place value
  VANISHES for `k ≥ n`**, and every derived line since has dropped it.
- ### **act 7's closing refusal** — *"Its coefficients against Weil's: part of `(L-identity)`, NOT
  ASSUMED."* ### **That is the whole finding, and it was sitting in a report on disk.**

## THE AUDIT SIDECARS (emitted; copied from the sidecar files)

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : check_harness
  act       : b220
  run at    : 2026-08-27T17:19:24 (local)
  input     : 6 checks routed through the harness
  checks    : 6
  pass      : 6
  fail      : 0
  error     : 0
  refused   : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 cfc788c002a7ec677cea8d2a31d08f85
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b220-lean
  run at    : 2026-08-27T17:29:01 (local)
  input     : whole file AggregationCircularityShadow.lean (created this act)
  stems     : gap, blind
  files     : 1
  lines     : 192
  hits      : 0
  live uses : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 c0738fdcaa97f6263c49afd9072e3a1b
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b220-docs
  run at    : 2026-08-27T17:21:21 (local)
  input     : added lines in D:/MY-DOwnloads/PLACE-papers vs HEAD
  stems     : gap, blind
  files     : 2
  lines     : 127
  hits      : 0
  live uses : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 6e4775a2df10bf76daddb108f142a0ab
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : commit_selfcheck
  act       : b220-docs
  run at    : 2026-08-27T17:25:01 (local)
  input     : D:/MY-DOwnloads/PLACE-papers
  input     : HEAD
  written   : 2
  foreign   : 0
  ro-claim  : none
  compliance : none
  VERDICT   : CLEAN
  self-hash : sha256/32 9d41b6fe2d6a04b78ac7bba7b1e82d56
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : mirror_verify
  act       : b220
  run at    : 2026-08-27T17:26:51 (local)
  input     : mirror-refresh-2026-08-27.zip
  files     : 40
  rows      : 40
  mismatch  : 0
  declared  : 84cb910
  ls-remote : 84cb91027b7c
  VERDICT   : CLEAN ON ALL THREE CLAUSES
  self-hash : sha256/32 13aeaeeefd06c6f7e3784fd259f9b8e4
=== END AUDIT SIDECAR ===
```

## WHAT THIS ACT DOES **NOT** ESTABLISH

1. ### **It does not show the identity is false, unprovable, or ill-posed.** It shows the identity
   cannot be used to *define* the aggregation and then be evidence for itself. ### **`h2` is
   untouched and the register sentence is exact.**
2. ### **It does not show no constraint exists** — only that the record holds none today, having
   read the owners the brief named. ### **One owner is UNREAD BY NAME: `ClassRichness`'s citation
   (M16)**, which C-NORM's joint (ii) already depends on.
3. ### **It does not adopt, define, or compile an aggregation.** Three candidates named, each
   marked **NOT ADOPTED**.
4. ### **It does not re-verify Core's 366 prior profiles.**
5. ### **It does not settle what act 9 meant by "Weil's coefficients."** It reports that the
   sentence names none, and stops.

## PINS

| repo | pin | note |
|:--|:--|:--|
| **PLACE-papers** | `a980cbf` → ### **`84cb910`** | chain §26 + the in-flight register; hook CLEAN, 0 foreign; **2 files changed, none created** |
| **SIDE-global-section** | `356010f` → ### **`4969b1b`** | the shadow + the appended print; ### **File E byte-identical, checked** |
| relay | → the b220 pin-line commit | registration, bank, profile, index queries, gates, five sidecars, report |
| SIDE-kernel | `0256e9e` — **UNMOVED** | — |
| mirror | rebuilt at `84cb910`, **CLEAN ON ALL THREE CLAUSES**, 40/40 | — |
| HELD | `6eada6a` — LOCAL-ONLY, untouched | — |

**DEVIATIONS:** ### **one, registered in advance** — the circularity shadow built in place of the
freedom shadow (P3)'s own condition excludes. *A second choice is recorded but is not a deviation:
the `Int` inhabitant was built, compiled, and discarded.*
**DIVERGENCES:** ### **one, with clause (b)** — it instructs that C-WEIL be listed *"with its owner
and grade"*, and ### **its owner refuses it as an assumption**, so it is listed as NOT AVAILABLE
rather than graded. Named at registration, not worked around.
