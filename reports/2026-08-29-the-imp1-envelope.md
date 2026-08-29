# THE IMP-1 ENVELOPE — b243, 2026-08-29

**Scope:** a bounded bench act on the import and the **right-side instruments only**. The corpus's
left side appears in no tool of this act and no face-off quantity is formed. A finite-place-set
object at a finite cutoff decides NOTHING global (b14/b15). `K` is not widened toward any observed
residual. PLACE-papers, HANDOFF, the loom and the mirror untouched. **All ledger filings defer to
the serializing close (b244).** Nothing deposits.

> **b15:** *"**a finite-place-set object at a finite cutoff decides nothing global**."*

---

## The branch: **(PROMOTED)**

All six (cell, axis) pairs within the derived criterion — ### **including `a² = 3` at `NV = 6001`,
the cell that failed b238.** `W-ORD-IMP1-ENVELOPE` is **DISCHARGED**.

### **And the limit in the same breath, not in a footnote: the bound is a rigorous worst case and
it is loose.** Slack runs **2.3× at the tightest cell** and **1.5 million × at the loosest.** A wide
margin means the bound is **conservative**, not that the agreement is tight. ### **VERIFIED-AT-BENCH
is a bench grade. It is not a proof of CC's equation (1) and it moves nothing about `h2`.**

| `a²` | NV | `PR` | residual | BOUND | slack | verdict |
|:--|--:|--:|--:|--:|--:|:--|
| 2 | 4001 | 0.000000000 | 1.216e−13 | 1.836e−07 | 1509831 | within |
| 2 | 6001 | 0.000000000 | 1.230e−13 | 8.162e−08 | 663842 | within |
| 3 | 4001 | 0.106483707 | 4.136e−08 | 1.159e−07 | 2.8 | within |
| **3** | **6001** | 0.106483687 | **2.218e−08** | **5.150e−08** | **2.3** | **within** |
| 4 | 4001 | 0.249319596 | 8.550e−09 | 2.756e−07 | 32.2 | within |
| 4 | 6001 | 0.249319593 | 5.467e−09 | 1.225e−07 | 22.4 | within |

### **The failed cell is resolved, not explained away.** `a² = 3, NV = 6001` carries the **same
residual `2.218e−08` it always did — nothing about the measurement changed.** What changed is the
bound it is compared against: `5.150e−08`, **derived from the bump**, where b238's was `2.133e−08`,
a maximum over three samples of a jittering quantity. ### **b238's diagnosis of itself was exactly
right:** *"A maximum over three samples of a jittering quantity is not an envelope. It is three
samples."*

---

## 1. The envelope — the analytic route

The ferry's first choice and b238's own second route: *"bound `|corr″|` directly and use the
analytic `h²/8` constant, which removes the jitter from the estimate entirely."*

With `φ(t) = exp(−1/(1−t²))` and `C = ∫φ`:

```
w(v)      = φ(v/L)/(L·C)                    ∫w dv = 1 exactly
corr(y)   = Φ(y/L)/(L·C²),   Φ := φ ⋆ φ     ← UNIVERSAL, cell-independent
corr″(y)  = Φ″(y/L)/(L³·C²), Φ″ = φ ⋆ φ″
|dPR|    ≤ (h²/8) · Σⱼ cⱼ · max|corr″|,     cⱼ = 2 log p / p^{k/2}
```

### **One universal function, computed once, and every cell's `corr″` is a scale factor times it.
No maximum over the instrument's own `corr` samples appears anywhere in the derivation.**

**Each constant checked rather than taken.** `φ″` in closed form against a central difference:
max deviation **6.93e−06** — *a derivative typed from calculus is a derivative that can be
mistyped*, and this one was not. `‖Φ″‖∞ = 0.409587060753`, **stable to twelve digits across a
twentyfold range of sample density** — the ferry required the maximum's stability for the *sampled*
route, and it is applied here too ### **so the analytic route does not escape the test by being
analytic.** `C = 0.443993816168079` against b238's own `mpmath.quad` value at dps 40:
**|difference| = 0.000e+00** — b238 computed it as a positive control for a hypothesis it then
refuted; this act uses it as a constant. **The same number, earned twice, for two purposes.**

### Two endpoint facts that look like errors and are not

- ### **`a² = 2`'s prime column is NOT empty.** b238 recorded `PR = 0.000000000` and my first
  draft called the column *empty*. It carries **one term**, `p=2, k=1`, at `x = log 2` — which is
  **exactly `2L` at that cell**, the right endpoint of `corr`'s support, where `corr` and all its
  derivatives vanish. ### **The term exists and its value is zero, and that is a different fact
  from having no term.**
- ### **`a² = 3` carries one term, not two:** `log 3` exceeds `2·log(√3)` by **one ulp**, so
  `left_side`'s own `ln <= 2*L` rejects the `p=3` term. ### **This act mirrors that arithmetic
  rather than correcting it — the envelope must bound the instrument, not the mathematics the
  instrument meant.**

### Two envelopes; the cruder one governs, by registration

| `a²` | `K_glob` | `K_pt` | ratio |
|:--|--:|--:|--:|
| 2 | 6.115845 | 0.000000 | 0.00 |
| 3 | 1.536029 | 0.678584 | 0.44 |
| 4 | 2.294377 | 0.496839 | 0.22 |
| 12 | 0.758862 | 0.187063 | 0.25 |

**(E-glob) governs and (E-pt) is reported and not used**, exactly as registered — because ### **a
sharper bound that happens to be the one that passes is the shape of the thing this act exists to
avoid.** The sharper one is banked so the next act has it. And the one place the cruder envelope is
absurd, said plainly: at `a² = 2` the single evaluation point sits **where `Φ″` is zero**, so
`K_pt = 0` is right and `K_glob = 6.116` applies a global maximum where the function vanishes.
### **That is the whole of the 1.5e6 slack. It is the price of the conservative choice, paid
knowingly.**

---

## 2. The criterion — and why it *cannot* have been widened

`|resid| ≤ K_glob(a²)·h² + F`, `h = 4L/(2NV−2)`, `F = 3.0e−13` — b238's **measured** float floor,
carried unchanged. Test axes `NV ∈ {4001, 6001}`, **b238's own, including the cell that failed**;
a new envelope tested only on axes the old one passed would be worthless.

### **`K` is derived from the bump and from nothing this act has measured. No residual enters its
formula, so it cannot have been widened toward one.** That is a stronger guarantee than b238's
refusal to widen: **b238 could have widened and did not; this criterion has no place a residual
could be put.** Gate 3 tests exactly that — it **recomputes `K` from the bump inside the checks
file, which has never seen a residual**, and requires it to match the banked value at every cell.

**b238's arithmetic gate, carried as the ferry directs, and it passed:** the failed cell needs
`K = 2.218e−08 / (1.831020e−04)² = 0.6616` against b238's banked `0.6363`. ### **The failure
reproduces, and this act does not soften it: b238's envelope was short.** The gate is a HALT — the
run refuses to print a verdict if it fails.

**Assumption A-1 re-run, not cited:** the whole envelope rests on `corr` at the nodes being the
continuous convolution there. `∫φ` by the instrument's own trapezoid at N = 2001, 8001, 32001:
**|error| = 0.000e+00 at every N.** The bump is `C^∞` with every derivative vanishing at ±1, so
Euler–Maclaurin has no boundary terms at any order.

---

## 3. The right-side error spec — filed, on (PROMOTED) only

**The instrument-layer object, for every future face-off to inherit:**

- ### **`A`:** `|dA| ≤ 8.882e−16` — machine epsilon, **independent of `NV`** on the measured range.
  Warrant: b238's S1. **Grade: MEASURED**, re-confirmed by this act's reproduction.
- ### **`PR`:** `|dPR| ≤ K_glob(a²)·h²`, `h = 4L/(2NV−2)`,
  `K_glob(a²) = ‖Φ″‖∞·W(a)/(8·L³·C²)` with `‖Φ″‖∞ = 0.409587060753`, `C = 0.4439938161680794` —
  both properties of the bump alone. **Grade: DERIVED FROM THE BUMP'S DEFINITION** — not measured,
  not fitted, not a function of any residual.
- ### **Floor:** `F = 3.0e−13`, measured by b238 at the cell whose prime column evaluates to zero.
- ### **What the spec does not cover**, said so it is not assumed to: the zero side's truncation at
  1000 ordinates (a different axis from `NV`), and any cell outside the banked six.

**Filings:** IMP-1 → `VERIFIED-AT-BENCH` with error bars, ### **the ledger cell update DEFERRED to
b244** as the ferry directs. `W-ORD-IMP1-ENVELOPE` **discharged**. And one new, small, real
work-order: ### **`W-ORD-ORDINATE-CACHE`** — b238 read its zeta ordinates from a **session temp
directory that no longer exists**; this act reproduced its table from the committed
`zeta_ordinates.npy` instead, and every `A`, `PR`, `Z` and residual matched **to every printed
digit**. ### **A run whose input lives in a temp directory is a run that cannot be repeated. It is
repeatable now.**

---

## Gates

**14 of 14 PASS, CLEAN** — on the second run. Run 1 produced **one REFUSAL, not a false pass**: a
witness read `K IS DERIVED FROM THE BUMP` where the bank writes it with backticks around `K`. **The
gate was right about the corpus and wrong about the bytes** — b234's own species, one level down.
Fixed in the witness, not the check.

The **arbitrary-inputs tautology control**: the criterion's arithmetic step `bound = K·h² + F` is a
tautology on 400 random triples, so it is **not** where the act's content lives — the content is
gate 3, that `K` comes from the bump, which **can** fail and was made to. The scope wall carries
b242's forced repairs forward rather than relearning them: **scope control by `ast` and identifier
matching**, so a left-side token is caught in code and not in a prohibition that names it.

**Term scan CLEAN**, 0 live over 1280 lines.

**The miss of this act's own:** I wrote a sentence into the envelope tool that **its own output
contradicted** — the tool printed `a² = 2` with one prime term and the prose two lines below called
the column *empty*, a claim carried across from b238's `PR = 0.000000000` without checking which of
the two things it meant. Caught by reading the table against the prose **before the envelope was
hashed**; had it not been, a false sentence would have been banked under a sha256 and gated as
authoritative. ### **That is the second time in two acts this seat has put a wrong character into an
artefact about to be hashed. Twice is a habit, and the habit is writing prose *about* a table
instead of *from* it.**

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : check_harness
  act       : b243
  run at    : 2026-08-29T10:16:58 (local)
  input     : 14 checks routed through the harness
  checks    : 14
  pass      : 14
  fail      : 0
  error     : 0
  refused   : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 3c72bb1f6e280275c96bed17a461d336
=== END AUDIT SIDECAR ===
```

**Banked:** `data/b243_registration_2026-08-29.txt` · `data/b243_envelope.txt` (sha256
`5c554f64…10be5164`) · `data/b243_final_run.txt` · `data/b243_imp1_envelope.txt`.

---

### **IMP-1 → VERIFIED-AT-BENCH, LEDGER UPDATE DEFERRED TO b244. RIGHT-SIDE ERROR SPEC FILED.
`W-ORD-IMP1-ENVELOPE` DISCHARGED. `K` NOT WIDENED AND UNABLE TO BE. b238's FAILURE REPRODUCED, NOT
RE-DESCRIBED. LEFT SIDE ABSENT. NOTHING ABOUT `h2` BEYOND THE REGISTER SENTENCE EXACT. NOTHING
DEPOSITS. LOCKS LAST.**
