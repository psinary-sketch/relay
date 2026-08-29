# THE RESIDUAL LEDGER — b241, 2026-08-29

**Scope:** READS and derivations-by-quotation. ### **No side was assembled, no identity evaluated,
no column compared.** A finite-place-set object at a finite cell decides NOTHING global (b14/b15),
and no part of this act discharges, weakens, or moves `h2` or the register sentence. No grade moves;
no sign was inserted; no orientation was chosen; **no correction executed**. `RULE M-1` is unamended
and File E is untouched. Nothing deposits.

> ### **THE CEILING, QUOTED FROM ITS OWNERS:**
> **b14:** *"a **finite-place-set object at a finite model cutoff** — the complete roster is the
> double limit and **STAYS OPEN whatever this act shows**."*
> **b15:** *"**a finite-place-set object at a finite cutoff decides nothing global**."*

---

## The act in one paragraph

b240 asked **where** its separation lives and answered with five terms. b241 asks **who owns each
term, by whose text.** ### **Two of the five reconcile or stand by text, two route, and no
correction executes.** The three sharpest findings are all about **warrants**, not values — and two
of them are about b240's own:

1. ### **b240's registration cited the wrong sibling.** It attributed to `b38_act10.py` a `resid47`
   formula that `b36_act8.py` contains. **Cost in digits: 8.9e−15. Cost in warrant: the relation the
   whole decomposition rests on was never checked against the file it names.**
2. ### **b240's "8.9e−16 reproduction" is a tautology.** Its diagnostics *define* `resid` as the
   residue and then verify a sum that reduces to `x = x`. ### **The check tested nothing** — and
   this act proves it rather than asserting it, by passing the same check on random numbers.
3. ### **The orientation question has no owner at all** — and the index said so before this executor
   could talk himself into an answer.

### **What did not change: the dominant term is still `resid47`, and its owner is M-4, which was
already open. This act found no new engine item.**

---

## 1. The sibling read — **(HOLDS AMENDED)**

`b38_act10.py`'s construction of `A` (line 47) is **one quadrature**:

```python
A = float(np.trapezoid(GU ** 2 * C.kernel(U), U) / (2.0 * math.pi))
```

The ferry asked for *"every channel it sums, subtracts, or regularizes with."* ### **The answer is an
absence and is reported as one: NONE.** It does not mention `Tr_full`, `E2`, `resid47`, or the ε
layer, and receives none of them. ### **So there is no such thing as "`A`'s internal `E2`" — `A` has
no internal structure.** The `E2` sits in b38's *separate* residual line, which is where the question
actually lives:

```python
E2N    = float(E2n.sum())                              # ten per-mode masks
E2full = e2_of_grid(a, corr, vc, L, rr, ee_full)       # computed, then unused here
resid  = TrN - A - E2N
```

with `NMODE = min(NMODE, xi.shape[1])` → **10** and `qeps_layer.py:41  NTERM = 11`. The sibling
writes it differently — `b36_act8.py:184  resid47 = Tr_full - (A + E2)`, the **full** ε.

**b240's registration asserted:** *"`b38_act10` computes `resid = Tr_full - A - E2_full` (its own
`resid47` column)."* ### **That gloss is false of `b38_act10.py` and true of `b36_act8.py`.**

> ### **THE TRUE RELATION, QUOTED:** `A = Tr_full − E2N − resid47`, with
> `E2N := Σ_{n<NMODE} e2_of_grid(a, corr, vc, L, rr, ee_modes[n])`, `NMODE = 10` of `NTERM = 11` —
> **not** `E2full`, which is the binding C2 uses and the binding b240 named.

**Does the amendment move a number?** Measured, not assumed (`data/b241_sibling_read.txt`):
`max |E2full − E2N| = 8.993e−15`, `max |resid_b38 − resid_b36| = 8.882e−15`. ### **The eleventh mode
contributes machine zero at every cell, so the amendment moves no column — it moves the warrant.
That it cost 8.9e−15 this time is luck, not method.**

---

## 2. The E2 ownership — **ONE OBJECT, and no correction executes**

Tested by definition, not by value: both are `e2_of_grid` at the same cell with the same `corr`,
`vc`, `L`, `rr`, differing in **one argument**. And b38's own mask-algebra gate certifies the eleven
per-mode masks sum to the full ε at 8.88e−16. ### **They are one object at two mode truncations.**

File E's own b239 binding settles the naming, and its under-specification is the evidence:

> `E2` — the ε-regularization term (`b38_act10.e2_of_grid`)

### **File E binds a FUNCTION and names no grid argument — precisely the distinction the two sibling
files make differently.** The record's own definition treats the ε-channel as one thing.

**But the correction the ferry provided for is not forced, and the act says so rather than executing
one.** Count the occurrences across the equals sign: `L := (Tr_full + E2 + Δ₋) + Θ_q` carries `E2`
**once**; `R := A − PR` carries it **zero** times. ### **There is no double-count across the equals
sign.**

The `2·E2` is produced by substituting `Tr_full = A + E2 + resid47` — and **that substitution is
vacuous.** `resid47` is *defined* as the residue, so the identity holds for any quantity in the slot:
put `5·E2` there, define `resid' := Tr_full − A − 5·E2`, and it holds just as exactly.
### **A decomposition whose last term is defined as the leftover carries no information about the
decomposed quantity's content.**

> ### **So b240's suspect 2, first limb — *"`Tr_full` already carries an `E2` by the instrument's own
> arithmetic"* — does not follow from the arithmetic it cites.** b240 already reported that limb's
> **size** was wrong; this act reports that its **argument** was circular. Both belong on the record.

**What the owners say is actually wrong with C2's input** is not a double-count. §20(b): *"the model
trace is an 11-mode band-limited truncation … **it is NOT the REGULARIZED trace** CC's theorem
equates to `W_∞ + ∫fε` (the divergent-part subtraction is exactly the trace-class bookkeeping already
owed to the ε-lemma)."* ### **That is M-4, already open. `resid47` is M-4's unpaid size at the bench,
not a new item.**

### The corroboration discovered after: b240's decomposition check is a tautology

`b240_diagnostics.py:74-75` sets `resid = Tr − A − E2` then forms
`pred = 2E2 + Dm + resid + Thq + PR`. Substituting:

```
pred      = 2E2 + Dm + (Tr − A − E2) + Thq + PR = Tr + E2 + Dm + Thq − A + PR
Lft − Rgt = (Tr + E2 + Dm + Thq) − (A − PR)     = Tr + E2 + Dm + Thq − A + PR
```

### **The two are the same expression. The check is `x = x`, and the reported 8.882e−16 is float
re-association noise.** b240's bank read *"the prediction registered before the run is the arithmetic
the run produced"* — the run produced no arithmetic to confirm it. **The prediction was genuinely
registered in advance and that credit stands; what it was tested against was its own restatement.**
Gate 6 demonstrates this by running b240's algebra on 500 arbitrary tuples, where it passes.

---

## 3. The `resid47` reading — **governing reading named from the texts**

b37's *"resid47: 0 by construction (substitution at content)"* is quoted with its construction, and
the construction is an **absence**: ### **`b37_act9.py` contains no trace function and calls none.**
Its `left_side` returns `A, PR` and nothing else; its docstring states *"The archimedean trace is
substituted at content (CC Thm 4.7, banked statement)."* ### **So "0 by construction" means there is
no raw trace to differ from the theorem's value, because the theorem's value stands in its place.
`resid47` is not measured and found zero — it is absent, and printed as zero.**

**Does that apply to C2's raw-channel binding? No — the two are mutually exclusive**, which is
stronger than "different". File E's own binding settles it (line 60):

> `Tr_full` — the prolate mode trace (`b38_act10.trace_modes`)

### **The ruling bound the raw mode-trace function by name. An act cannot both substitute a channel
at content and compute it raw.** ### **The RAW reading governs, and under it `resid47` is not zero.**
b240's sentence on this point — *"that is the SUBSTITUTED reading, NOT the bench one"* — is
**confirmed by the owners**, and that is said as plainly here as the dissents are.

---

## 4. The Q-orientation — **(UNDERDETERMINED). Dossier routed. Nothing chosen.**

Every owner sentence the ferry named was read. **File E's operator** (line 107,
`T.value + Q.value = W.wInf - W.wPrimes`) fixes the form but leaves `Q.value` a bare data parameter.
**§19's comparison**, **`b36_act8.py:175`** (`RIGHT = (Tr_full + E2 - Dneg) - Thq`), **§20(c)'s
closed form**, and the corpus's recurring `(Θ_q − PR)` pairing all orient `Θ_q` **with the prime
side's minus**. **§18** fixes the template and declines to settle the comparison with Weil's.
**b235's `sign-atlas`** settles the *ledger* side only.

### **And then the index — queried because the b160 gate is in the path — produced the sentence that
decides the component:**

> **`quotient-trace`** (act 9 / b197 / b215): *"### **THE AGGREGATION IS UNSTATED**: no statement
> assembles the per-place values into the single real `Q.value` at a cell (b197, re-confirmed b215)."*

### **That is the exact step every sentence above is missing. They orient `Θ_q` inside their own
comparisons; none assembles `Θ_q` into `Q.value`. Those are two different claims** — and the
registration separated them **in advance**, at section (C)(d), precisely because the second is the
one that would be needed and the first is the one that is easy to mistake for it.

**File E's own testimony corroborates it in line count:** b239 wrote a twenty-six-line documented
binding into the `T` field and left the `Q` field at two lines, exactly as opened. ### **The record
bound one field and not the other.**

| candidate | texts bearing | what it entails |
|:--|:--|:--|
| **O1** `Q.value := −Θ_q` | §19; `b36_act8.py:175`; §20(c); the `(Θ_q − PR)` pairing; File E's `+Q` | the finite-place content becomes `Θ_q ≟ Σ_p W_p` — exactly the one open item §19 names on that side |
| **O2** `Q.value := +Θ_q` | ### **none** — b240 adopted it as a declared *abstention* | the content becomes `Θ_q ≟ −Σ_p W_p`, against §20(c)'s convergence |
| **O3** `Q.value` a data parameter | File E's actual state; `quotient-trace`'s "aggregation unstated" | the face-off's `Q` column is an executor's binding, not the record's |

### **Disclosure, and this act owes it most plainly here: O1 shrinks the residual, and that is not
why it is listed first** — it is listed first because it carries the most owner texts.
### **And no orientation on the list closes the separation:** b240's V2 stays 19×–24× the combined
bar, V3 stays 8.6×–19×, and `resid47` is untouched by every orientation. **An orientation chosen to
help the columns meet would have to make them meet, and none of these does.**

**A second orientation question, found while reading and filed not decided:** `Δ₋` has two
realizations under one name — `b36_act8.py:172`'s odd raw-trace slice against §17/§19's odd ε-mask
series. §19's row fixes the **definition**, and ### **b240 bound `Δ₋` correctly.** What is not fixed
is its **sign** in `T`: act 8 subtracts it, C2 adds it, §19 reads *"our object's trace = this − Δ₋"*.
### **Filed, not executed — it rides the same decision card.**

---

## 5. The ledger restated, and the hope judged

**The ferry's registered hope:** the surviving residual concentrates in the `Θ_q`-vs-`PR` pair.
**The executor's expectation, banked at registration section (E) before any verdict was composed:**
**DISSENT** — concentrating in `resid47` and `2·E2`.

### **The hope is not borne out; the registered dissent is. And the act does not get to enjoy that,
because it was registered before its VERDICT, not before its EVIDENCE** — the banked columns were
already in front of the executor, and the registration's section (0) says so.

### **The cell that settles it:** at `a² = 2` the pair is **identically zero** (both vanish because
`corr` vanishes at `u = 2L`) — ### **and that cell carries the largest separation of the six,
8.085046. A pair that is zero where the residual is largest is not where the residual concentrates.**
At its best cell (`a² = 12`) the pair totals 1.232825 of 5.851371 — **21.07%**, its maximum.

| term | range over six cells | status after b241 |
|:--|:--|:--|
| `2·E2` | 1.950128 … 3.358857 | ### **STANDING.** One object, two names, two truncations (8.99e−15 apart); no double-count across the equals sign; b240's mechanism argument withdrawn as circular |
| `Δ₋` | 0.354973 … 0.677615 | ### **ROUTED (new).** Definition correct and correctly bound; **sign** contradicted by `b36_act8.py:175` and §19's row |
| `resid47` | 2.313445 … 4.048575 | ### **RECONCILED-BY-TEXT.** Raw reading governs; not zero; **M-4's unpaid size, not a new item**. Largest single term at every cell |
| `Θ_q` | 0.000000 … 0.518491 | ### **ROUTED.** Orientation underdetermined; aggregation unstated; dossier O1/O2/O3 filed |
| `PR` | 0.000000 … 0.714334 | ### **STANDING**, and the one term with a settled orientation — b235's atlas, eight cells agreeing, `A − PR` |

### **One reconciled-by-text, two routed, two standing. None by preference.** ### **The corrected
per-cell realization statement is not printed, because no correction executed** — the texts identify
one object and locate the real defect at M-4; they do not force a correction to C2. And amending C2
would be amending a ruling: *"AN EXECUTOR DOES NOT SETTLE A DEFINITION"* (b237).

**The second face-off's preconditions:** this act's two reconciliations (delivered); ### **two new
ruling-items this act adds and the ferry did not anticipate** — the Q-orientation decision card and
`Δ₋`'s sign, neither an executor's to make; the two bounded bench acts `W-ORD-LEFT-MODE-AXIS` and
`W-ORD-IMP1-ENVELOPE`, both standing and neither discharged; and M-2 still open, so a per-cell
face-off remains a per-cell statement. ### **A second face-off run before the two items are ruled
would inherit the same suspect 3 it inherited last time.**

---

## 6. Two misses of my own, both caught by instruments

### **MISS 1 — I nearly reported the Q-orientation as FIXED BY TEXT.** I reached §4 with five owner
sentences assembled and was drafting *"fixed by text, stated by citation."* What stopped it was the
`banked_index` query, run because `registration_gate.py` puts the b160 convention in the path —
**not because I doubted the reading.** ### **The species, named: five sentences that orient an object
inside their own comparisons are not one sentence that defines it.** ### **And the aggravating fact:
the reading I was about to adopt is the one that shrinks the residual.** That is b229's named crime
approached from the direction hardest to see — not by inserting a sign to help, but by
**accumulating warrant for a sign that happens to help.** ### **The gate earned its keep this act,
and it earned it against this executor and not a hypothetical one.**

### **MISS 2 — I read the wrong File E first and quoted it into a draft.**
`relay/tools/lean/mathlib-companion/FiniteInstanceIdentity.lean` is **stale by both 2026-08-28
amendments** — it carries neither b235's convention repair nor b239's RULE M-1 binding. Caught by
diffing against the residence copy. ### **It carries the exact sentence b235 ruled was the defect**
(*"in the CC sign convention"*), which under `wInf − wPrimes` names `−A − PR`, *"an object the corpus
does not compute."* ### **And the drift runs the wrong way against the residence ruling's own words**
— *"new construction-era work lands here first and moves to the residence by tag, never by drift"* —
so the residence is **ahead** of the working copy, the one direction no check fires on.
**Filed as `W-ORD-FILE-E-WORKING-COPY-STALE`; not repaired, because syncing a kernel-adjacent Lean
file between layers is out of a READS act's scope. The other four files in that directory are not
audited here and may carry the same drift.**

### **And the registration names the stale path**, because it was written before the drift was found.
### **It is left exactly as banked** — editing a banked registration to match what the act later did
is the species this corpus guards against, and a wrong path disclosed is worth more than a right path
back-dated.

---

## Gates

**15 of 15 PASS, CLEAN — and NOT on the first run**, which is reported because b240's was.
Run 1 produced **two harness REFUSALS, neither a false pass**: gate 6 returned `np.False_` (not a
bool), and gate 15's fixture **passed** because it pointed at the checks file itself, which contains
the phrase as a string literal — ### **b213's exact species, a check re-matching text the executor
had just written, caught by the witness/fixture guard rather than by me.** Both are recorded in the
tool rather than silently patched.

### **Two absences are positively controlled**, as the ferry required: gate 4 aims the "no trace
function" test at `b38_act10.py`, where it must fail; gate 5 aims the "combines no channel" test at
act 8's assembly line, where it must fail. Gate 6 demonstrates the tautology on 500 arbitrary tuples
with an independent-`resid` fixture that must fail.

Term scan **CLEAN**, 0 live over 1264 lines of this act's own voice — ### **after a repair: I wrote
the banned stem `blind` nine times in my own voice and the scan caught it.** The repair was confined
to this act's own new files; no pre-existing line was touched.

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : check_harness
  act       : b241
  run at    : 2026-08-29T09:25:19 (local)
  input     : 15 checks routed through the harness
  checks    : 15
  pass      : 15
  fail      : 0
  error     : 0
  refused   : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 480102ca05e80501bceda241fb654780
=== END AUDIT SIDECAR ===
```

**Banked:** `data/b241_registration_2026-08-29.txt` · `data/b241_residual_ledger.txt` ·
`data/b241_sibling_read.txt` · `tools/e16/b241_sibling_read.py` · `tools/b241_checks.py`.
**Pins:** nothing pushed, nothing tagged, PLACE-papers untouched, no mirror rebuild required.

---

### **NO SIGN INSERTED. NO ORIENTATION CHOSEN. NO CORRECTION EXECUTED. RULE M-1 UNAMENDED. FILE E
UNTOUCHED. NO GRADE MOVED. NO VARIANT PROMOTED. M-2…M-5 STAND OPEN. NOTHING ABOUT `h2` BEYOND THE
REGISTER SENTENCE EXACT. NOTHING DEPOSITS. NOTHING CIRCULATES. LOCKS LAST.**
