# b211 — THE ALTERNATION DERIVED

**2026-08-27 · relay `reports/2026-08-27-alternation-derived.md`**
**Ferry part 1 of 1, receipt confirmed IN FULL before execution (Rule 1).**
**Registration `fbdb37a`, banked before the derivation was written out. Bank: `data/b211_alternation_derived.txt`.**

> *** ### **THE VERDICT: BRANCH (DERIVES).**
> ### **`α(μ_k) · β′(μ_k) = ∫₁^∞ ψ² dx`, `c₀ = +1`, DERIVED AT CONTENT.**
> ### **THE SONIN SECTOR IS NONZERO AT DERIVATION GRADE ON NAMED IMPORTS.** ***
>
> b207 had it at **bench grade over six measured eigenvalues**. This act has it over the **whole
> even family**, conditional on eleven named imports. ### **That is a lift. It is not a proof from
> nothing.** *Core 327 → 339, every terminal zero-axiom.*
>
> ### **IT IS A FACT ABOUT THE SONIN SECTOR. IT IS NOT A CLAIM THAT THE SONIN SECTOR IS WHAT TERM
> 3 NEEDS.** ***The naming ruling stands with the author, untouched.***

---

## COMPONENT 1 — THE DERIVATION (P1)

Seven steps, longhand in the bank. The spine:

**Step 0.** `(x²−1)f″ + 2xf′ = [(x²−1)f′]′` — the operator is **formally self-adjoint with weight
one**, read off its own definition rather than assumed.

**Steps 1–2.** `[p·W(u,v)]′ = (ν−μ)uv`, recovered with its sign, not adopted from the brief. In the
limit `ν → μ`: ### **`[p·W(u,u̇)]′ = u²` — and that square is the entire source of the positivity
this act rests on.**

**Step 3.** At `x = 1` the boundary term vanishes **twice over**: `p(1) = 0`, *and* `ẏ_I(1) = 0`
because `y_I(1) ≡ 1` carries no `μ`. ### **Either alone suffices** — recorded because the brief
asked for both and they turn out to be independently sufficient.

**Step 4.** At `∞` it vanishes because `V₀^± = 1` carries no `μ`, giving `ψ̇ = O(1/x²)` against
`p = O(x²)`, so `B = O(1/x) → 0`.

**Step 5.** `β = p·W(ψ,y_I)` is **constant in `x`** — which is why the connection point is free.

> ### **A detail worth keeping:** at `x₀ = √2`, `p = 1` *exactly*, so `β = W(ψ,y_I)(√2) = F`, the
> paper's determinant, with no factor at all. ### **RRT's connection point is not arbitrary — it is
> the point where the weight is one.**

**Step 6.** At an eigenvalue `ψ = α y_I`, the two pieces combine and **the arbitrary evaluation
point cancels** — as it must, since `β` is `x`-independent. ### **That cancellation is an internal
check of the algebra and it passes.**

### ### **`α(μ_k)·β′(μ_k) = ∫₁^∞ ψ²_{μ_k} dx`.  `c₀ = +1`.**

**Checked against b210.** b210 measured `s = +1` at all twelve eigenvalues across `τ = 2π, 4π, 6π`.
### **The derived `c₀` is `+1`. They agree, and in the same convention** — RRT §4.2.2's `β` *is* the
instrument's `β`, and the paper's `D_τ` `ψ` is `−sin(τx)/x`, which *is* the instrument's `ψ`.

*** ### **AND THAT FORCES A CORRECTION ON b210's OWN REGISTRATION, CARRIED HERE RATHER THAN LEFT IN
PLACE.** b210 registered that the paper's `ψ` is `−sin(2πΛx)/(πx)` and therefore differs from the
instrument's by a factor `1/π`. ### **That is the `W_Λ` object. The `D_τ` object — which is what the
instrument implements — is `−sin(τx)/x` exactly, and §4.2.2 says so.** ### **Nothing b210 computed
changes**, because both sides are quadratic in `ψ` and b210 registered that invariance in advance.
***The framing was wrong and is corrected; the result is not touched.*** ***

---

## COMPONENT 2 — THE GRADES (P2)

| # | consequence | grade | on |
|:--|:--|:--|:--|
| **C1** | every zero of `β` is simple | ### **DERIVES** | the identity alone |
| **C2** | `sign(α_k)` alternates | ### **DERIVES** | premise (ii): `β` entire of order ≤ ½ |
| **C3** | both values of `c` occur | ### **DERIVES** | b203's chain (I8 + I6 + I10) |
| **C4** | ### **the Sonin sector is nonzero** | ### **DERIVES** | I9, I7, I6, C3 |

### *** C1 IS THE PAPER'S OWN OPEN CONJECTURE ***

RRT §4.2.2, quoted: *"We **conjecture** that the zeros of `F` are simple. (This is supported by some
numerical experiments.)"* ### **For the even family and on the premises named, this act derives it.**

> ### **AND IT IS NOT LEMMA 2(ii).** The ferry's clause (a) called the simplicity import *"what the
> derivation will re-prove"* — but the source carries **two different simplicities**. Lemma 2(ii) is
> that the **eigenspace** is one-dimensional: a *proved lemma*, which this derivation does **not**
> use and does **not** re-prove, and which remains an import inside C3. ### **The one derived is the
> determinant-zero simplicity, which the source leaves open.** *The divergence was flagged at
> registration and is discharged here by reporting it, not by picking one.*

### THE IMPORTS — every one re-read at its source document **in this act**

`I1` RRT §4.2.2 · `I2` Prop 6(i) Borel-summable · `I3` Prop 6(ii) · `I4` Prop 7 · `I5` §4.2.3 ·
`I6` Lemma 2(ii) · `I7` Lemma 2(iii) · `I8` CM Thm 2.6(i) · `I9` CM Cor 3.2 · `I10` `F²=1` on evens
(**owned by neither paper**) · `I11` b206's positive rescaling.

> `I11` deserves a line: b206 *derived* `α^D = πΛ·α^W` from the variable passage without having
> §4.2.3, which states `|α^D| = π√2` at `Λ = √2` directly. ### **A derivation confirmed at source by
> a sentence it did not use.**

### WHAT DOES **NOT** DERIVE — named, not filled by plausibility

- ### **THE ODD FAMILY IS NOT TREATED.** `β`'s zeros are the **even**-family eigenvalues.
- ### **The uniformity in `μ` of the asymptotic remainder** is an **import** (`I2` + `I1`), not an
  elementary estimate. Differentiating an asymptotic expansion in `μ` term by term with a uniform
  remainder is licensed by the source's summability, and that is said rather than passed over.
- ### **Nothing here says WHICH eigenvalue carries `c = +1`.** b207 knew one of six was in the
  sector and could not say which; ### **this act knows infinitely many are and still cannot say
  which** — that is b205's discrepancy, untouched.

---

## COMPONENT 3 — THE SHADOW AND THE FILINGS (P3)

**`Core/SignTransferShadow.lean`** — vanilla Lean 4 v4.29.1, no imports. ### **12 terminals, every
one *"does not depend on any axioms"*, printed from its own run.** `AXIOM_PRINTS.txt` regenerated by
`AllPrints.lean` in full: ### **339 lines, 339 zero-axiom, 0 otherwise. Core 327 → 339.**
Correspondence **row 84**, six cells, none blank, written by the committed tool **from a script file
and not a shell string** (b158's rule; b178 and b193 are why), **verified by read-back**.

Polarity controls first — `control_neg` shows `0 < x·y` **genuinely selects**, without which the
transfer theorem would be untested — and `transfer_nonvacuous` exhibits an inhabitant satisfying
**both** hypotheses, ### **so the theorem is not vacuously true.**

### **What it is NOT, on the file's own face:** not the derivation, and ### **not the analytic
half** — that `β′` alternates at consecutive simple zeros of a real-analytic function is **not
finite-decidable** and is deliberately **not in Core**. And it is **not a duplicate of row 83**
(b207): that shows a *global sign error* cannot destroy "both values occur"; this shows the
*transfer between the two factors*. ### **C3 uses both, and neither implies the other.**

### *** THE PRINT DECIDED THE FILE'S SHAPE, FOR THE SECOND ACT RUNNING ***

The first draft defined the witness as `fun i => if i % 2 = 0 then 1 else -1` and proved its two
properties with `simp`. ### **The print came back `depends on axioms: [propext]` on two terminals** —
inherited from the tactic, not from anything the statement needed. The repair: define `flip` by
**recursion**, after which it alternates **definitionally** (`fun _ => rfl`). ### **Cheaper, truer to
the hypothesis it must satisfy, and zero-axiom.**

> b207 recorded the same species one act ago with `Int.mul_neg`. ### **The standing inference is not
> that the executor writes bad Lean — it is that THE PRINT IS PART OF THE FILE'S CONSTRUCTION, NOT A
> CHECK RUN ON A FINISHED FILE**, and an act that prints only at the end has already shipped
> whatever shape the tactic chose for it. ***The note is in the file it changed.***

### THE FILINGS

- **M22 — ANSWERED-IN-PART, both parts named.** *Do both values of `c` occur?* ### **Answered: they
  do, alternately, at derivation grade.** *What is the absolute sign at a named eigenvalue?*
  ### **Still open** — it is b205's discrepancy.
- **The identity chain** — §22 added, with the import list and the four graded consequences.
- **The simplicity import** — marked **discharged-by-derivation**, but ### **only the
  determinant-zero simplicity**; RRT Lemma 2(ii) remains an import and is used in C3. ***Listed
  separately so the discharge cannot be read wider than it is.***
- **The in-flight register** — the alternation route **DISCHARGED** by the act specified to
  discharge it; the Sonin sector **LIFTED** bench → derivation; ### **the odd family added as a new
  LIVE item, not treated and named as the next question**; the `μ₋₂` discrepancy **untouched**.
- **The thirty-seventh seam's debt** — term 2's formalization stands, unpaid and untouched. The six
  rulings and b209's rows 46/47 stand with the author. ### **Locks last.**

---

## THE AUDIT SIDECARS (emitted by the tools; embedded verbatim from the sidecar files)

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b211-core
  run at    : 2026-08-27T12:03:11 (local)
  input     : whole file SignTransferShadow.lean (created this act)
  input     : added lines in D:/SIDE-global-section vs HEAD
  stems     : gap, blind
  files     : 4
  lines     : 219
  hits      : 0
  live uses : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 5dc9c58b94c5dd6ee66eed1f228d5f19
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b211-docs
  run at    : 2026-08-27T12:07:59 (local)
  input     : added lines in D:/MY-DOwnloads/PLACE-papers vs HEAD
  stems     : gap, blind
  files     : 2
  lines     : 119
  hits      : 0
  live uses : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 897a8971c8fb68ce3c1316ee007b3bab
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : commit_selfcheck
  act       : b211-docs
  run at    : 2026-08-27T12:08:24 (local)
  input     : D:/MY-DOwnloads/PLACE-papers
  input     : HEAD
  written   : 2
  foreign   : 0
  ro-claim  : none
  compliance : none
  VERDICT   : CLEAN
  self-hash : sha256/32 f02963843d7a1ca3c8ef64b566e8b618
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : mirror_verify
  act       : b211
  run at    : 2026-08-27T12:08:50 (local)
  input     : mirror-refresh-2026-08-27.zip
  files     : 40
  rows      : 40
  mismatch  : 0
  declared  : 9e75ffa
  ls-remote : 9e75ffa22d5b
  VERDICT   : CLEAN ON ALL THREE CLAUSES
  self-hash : sha256/32 df9ef166c653e3ac782022806e3dfbda
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b211-relay
  run at    : 2026-08-27T12:10:54 (local)
  input     : added lines in D:/relay vs HEAD
  stems     : gap, blind
  files     : 7
  lines     : 642
  hits      : 8
  live uses : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 a84817482a32128d702b962fbf981e2b
=== END AUDIT SIDECAR ===
```

> ### **These five were copied out of the sidecar files, not retyped.** b210's report retyped its
> blocks with **invented timestamps** and `audit_verify.py` returned `TAMPERED` on all three.
> ***The lesson was one act old and it was applied.***

### THE INDEX QUERIES (clause (e)) — `data/audit_b211_index_query.txt`

**9 of 14 hit.** The five misses are `alpha`, `beta`, `psi`, `wronskian` — and now **`alternation`**,
which is notable: ### **an object with its own act (b207) and its own kernel file
(`Core/AlternationShadow.lean`) is still not reachable in the index by its name.** Absence from the
index is not absence from the record. ### **Filed again for the index-coverage repair queue, which
two consecutive acts have now named without running.**

---

## PINS

| repo | pin (`ls-remote`) |
|:--|:--|
| **SIDE-global-section** | `76d5182` → ### **`bb99f59`** — *moved: Core 327 → 339, all zero-axiom* |
| **PLACE-papers** | `e689418` → ### **`9e75ffa`** — §22 + the register; hook CLEAN, 0 foreign |
| relay | `fbdb37a` (registration) → the b211 pin-line commit |
| SIDE-kernel | `0256e9e` — **UNMOVED** |
| **mirror** | rebuilt at `9e75ffa`, **CLEAN ON ALL THREE CLAUSES** |
| HELD | `held/carrier-acts` = `6eada6a` — **LOCAL-ONLY, untouched** |

**DEVIATIONS:** none.
**DIVERGENCES:** two, both flagged at registration and both **discharged here rather than left
standing** — the ferry's conflation of RRT's two simplicities, and b210's mis-statement of which
normalization the instrument matches.
