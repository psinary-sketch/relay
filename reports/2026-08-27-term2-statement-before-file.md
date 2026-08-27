# b215 — TERM 2, THE STATEMENT BEFORE THE FILE

**2026-08-27 · relay `reports/2026-08-27-term2-statement-before-file.md`**
**Ferry part 1 of 1, receipt confirmed IN FULL — queued while b214 was in flight and started after b214 closed.**
**Registration `ee8e375`, banked before the statement. Bank: `data/b215_term2_statement_before_file.txt`.**

> *** ### **BRANCH (HALT) AT (b).** The missing sentence is ### **THE AGGREGATION** — how the
> quotient channel's per-place, per-level values become the **single real `Q.value`** at a
> diagonal cell. ### **It wants a RULING or a RESULT. It does not want a read.** ***
>
> ### **No file D was written. File E is untouched. Nothing was weakened — and `ClassRichness` was
> not discharged by `trivial`, because no statement was written at all.**

## COMPONENT 1 — THE STATEMENT, ATTEMPTED (P1)

### **The attempt was made rather than the halt asserted.** Term 2's object, written out as far as
the owners carry it, each line with its owner and grade:

| line | owner and grade |
|:--|:--|
| `cell : a_sq : ℚ, 1 < a_sq` | File E — **exists** |
| `k(p, cell)` — the per-place cutoff | the staircase / diagonal section, **recorded** (`D-yes, f967f10`) |
| `τ_q = (pⁿ − p^k)/((pⁿ − 1)·p^{k/2})` | **PROVED longhand** (act 9); zero-axiom Core shadow held |
| `limₙ τ_q = p^{−k/2}` | **THEOREM** at the level limit |
| volume normalization | **FORCED** (act 7) |
| `ClassRichness : Prop` | **premise, at cite** — an opaque Prop parameter, which is what "at cite" means |
| ### **`Q.value : ℝ`** | ### **??? — THE AGGREGATION** |

*** ### **Every line above the rule has an owner and a grade. The line below it has neither.** The
per-place values exist and the cell determines each place's cutoff — ### **but no statement in the
record says how the family `{p^{−k(p,cell)/2}}_p` becomes one real.** ***

**The candidates the record does not choose between**, listed so the absence is concrete: a bare sum
over `p`; a sum with Weil's weights; a product; a restricted or regularized sum; a limit of finite
truncations. File E's identity compares `Q` against a ledger whose prime side is itself one real, so
the shape is *plausibly* a weighted sum — ### **and the weight is exactly what is unstated.**
***Plausible is not stated, and I stopped there.***

> ### **The halt is not this act's discovery.** b197 recorded it: *"WHAT IS NOT STATED — AND IT IS
> THE AGGREGATION … BUT NO STATEMENT ASSEMBLES THE CHANNEL'S PER-PLACE VALUES INTO THE SINGLE REAL
> `Q.value` AT THE CELL."* ### **My registration said so before the attempt, and the attempt agrees
> with the registration.**

**It wants a RULING** (the combination rule over places is a definitional choice about the built
object) **or a RESULT** (a derivation showing the staircase and the forced normalization *force* one
rule). ### **Not a read — b197 read, b215 read again, two acts have now looked.**

### **AND NO AGGREGATION WAS INVENTED.** The registration named that temptation before the attempt.
Writing one would be **making the author's definition** — and it would compile, pass the shell test,
and be ***a shell wearing a theorem's clothes.***

## (P2) THE SHELL TEST — RUN, AND ON THE CURRENT FILE E TOO

`structure QuotientTrace (cell : DiagonalCell) where value : ℝ` ### **is inhabited by `⟨0⟩` at every
cell. By the ferry's own test it is a SHELL.**

> ### **And that is a fact about the file as it stands, not a criticism of it.** File E's own header
> says *"THIS FILE STATES; IT DOES NOT PROVE"* and calls its constituents *"DATA PARAMETERS"*.
> ### **The shell test does not convict File E — it measures exactly the distance file D was
> supposed to close, and shows that nothing has closed it.**

## COMPONENT 2 — THE BUILD: NOT REACHED

Gated on (b), which halted. No `Interfaces/QuotientTrace.lean`, no File E edit, **G-CONSUME not run
because there is nothing to consume.**

### *** AND A SECOND, INDEPENDENT OBSTACLE — MEASURED, NOT ASSUMED ***

### **The Interfaces layer cannot be compiled in this environment.**

`lean Interfaces/FiniteInstanceIdentity.lean` → *"error: unknown module prefix 'Mathlib'"*. Both
halves of the reason were checked:

- Mathlib **is** present (`/d/mathlib4/Mathlib`) and its `.lake/build/lib` exists — ### **but
  `Mathlib/Data/Real/Basic.olean` is ABSENT. It is not built.**
- ### **Toolchain mismatch:** `/d/mathlib4` pins **`v4.30.0-rc1`**; the repo pins **`v4.29.1`**.
  Oleans are toolchain-specific, ### **so even a fully built Mathlib could not be imported.**

### **So the EXECUTION line's *"a claimed compile reported only from its own printed axiom profile"*
could not have been satisfied for an Interfaces file even if (b) had passed.** The `Core` layer is
unaffected — vanilla Lean, no imports, which is why b211, b212 and b214 could build and print.

### ### **Term 2 is blocked by TWO things, and only one of them is mathematical.**

## COMPONENT 3 — THE FILINGS: THREE DEBTS, NOT ONE

| # | debt | owner | status |
|:--|:--|:--|:--|
| 1 | **the file** | the author (ruling) or a future act (result) | **BLOCKED on the aggregation** |
| 2 | **the lemma** — `ClassRichness` | its own item | ### **two parts: (2a) its citation is UNREAD (M16); (2b) undischarged. You cannot discharge what you have not read.** |
| 3 | ### **the toolchain** — new at b215 | an **environment repair**, not the author's ruling | blocks *any* Interfaces-grade construction |

**The thirty-seventh seam's debt restated:** term 2's formalization **is** that debt, and this act
does not pay it. ### **It names why it cannot be paid, and by whom** — which is what the FOOT asked
for as the alternative outcome. **Locks last.**

## THE AUDIT SIDECARS (emitted; copied from the sidecar files)

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b215-docs
  run at    : 2026-08-27T14:54:48 (local)
  input     : added lines in D:/MY-DOwnloads/PLACE-papers vs HEAD
  stems     : gap, blind
  files     : 1
  lines     : 36
  hits      : 0
  live uses : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 25bfb71a8bee7f7f3191d30265b60ae0
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : commit_selfcheck
  act       : b215-docs
  run at    : 2026-08-27T14:55:24 (local)
  input     : D:/MY-DOwnloads/PLACE-papers
  input     : HEAD
  written   : 1
  foreign   : 0
  ro-claim  : none
  compliance : none
  VERDICT   : CLEAN
  self-hash : sha256/32 fa8a1bed97b9a9d88ff76d2d4a88aa4d
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : mirror_verify
  act       : b215
  run at    : 2026-08-27T14:55:46 (local)
  input     : mirror-refresh-2026-08-27.zip
  files     : 40
  rows      : 40
  mismatch  : 0
  declared  : aee890a
  ls-remote : aee890a45658
  VERDICT   : CLEAN ON ALL THREE CLAUSES
  self-hash : sha256/32 889e8a018bbd061a352dee0bbda1dc65
=== END AUDIT SIDECAR ===
```

**Index (clause (f)):** 4 of 8 hit, and ### **the four misses are every object this act is about** —
`class richness`, `file D`, `quotient trace`, `weil ledger`. `class richness` has missed in every
query **since b188**. ### **Sixth consecutive act to name the index-coverage queue. A queue six acts
have named and none has run is not a backlog — it is a decision nobody has made.**

## PINS

| repo | pin | visibility |
|:--|:--|:--|
| **PLACE-papers** | `6474a63` → ### **`aee890a`** — the register only | PRIVATE |
| relay | `ee8e375` → the b215 pin-line commit | PUBLIC |
| SIDE-global-section | `356010f` — ### **UNMOVED, no build** | PUBLIC |
| SIDE-kernel | `0256e9e` — UNMOVED | PUBLIC |
| mirror | rebuilt at `aee890a`, **CLEAN ON ALL THREE CLAUSES** | — |
| HELD | `6eada6a` — LOCAL-ONLY, untouched | — |

**DEVIATIONS:** none — ### **and the one I registered against myself did not occur: no aggregation
was invented.** **DIVERGENCES:** none with the ferry. ### **The ferry predicted this outcome and the
act confirms it.**
