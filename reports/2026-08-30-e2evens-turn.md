# E2even's TURN — b261, 2026-08-30

**Scope:** a derivation at content with bench controls. **CONCURRENCY: SOLO (research seat).**
A finite cell decides NOTHING global (b14/b15); b242 governs — *"a measured rate is not a tail
bound."* The register sentence is unchanged and **nothing deposits.** The patent lane is
independent and was not touched.

**Order of record:** the owners read at content → the index queried → **the registration
TERM-SCANNED (0 live uses, CLEAN) and only then banked** → the run → the diagnostics → the shadow →
the bank → the filings → HANDOFF.

---

## The verdict

### **J2 is REFUTED. `E2even` does not decrease monotonically — it RISES from `0` on `(1, a₀]` and falls only afterwards, with `a₀ ∈ (1.75, 2]`.**

**And b255's ladder starts at `a² = 2` — the first cell after the turn.** The sixteen-cell monotone
stretch is a fact about **where the ladder begins**, not about the function.

*That is not a criticism of b255*, which chose its ladder by affordability and said so, and `a² = 2`
is the smallest cell at which the staircase admits any prime at all. **b255 is not re-verdicted
(b246's rule).**

---

## b260's lesson made a step — and it cost this act nothing

b260 paid a real price: its Rule 3 correction rewrote its registration *after* its run and destroyed
the filesystem evidence of precedence. Its closing lesson was to run the term scan against the
registration **before** the run. The ferry made that a scope clause.

**The registration scanned 0 live uses, VERDICT CLEAN, was banked, and was never touched again. Its
mtime precedes the run's and the gate checks it.** *A lesson that costs one act its evidence and the
next act nothing is a lesson that landed.*

---

## S1 — the dilation reduction: **derives exactly**

`carto_atlas.bump` builds `v = L·t` with `t` a **fixed** grid, and `a` enters **only** through
`L = log a`. `w` is normalized to unit integral, so `w(v) = φ(v/L)/L` with `φ` fixed; and
`dv[0] = 2L/(NV−1)`. Hence

### `corr_a(u) = (1/L)·ψ(u/L)`, with `ψ` **fixed and a-independent**

— and this is **exact on the instrument's own grid, not merely in the continuum**, because the grid
scales with `L` while `NV` does not move. Substituting `u = Ls` in `e2_of_grid`:

### `E2even(a) = 2 ∫₀² ψ(s)·ε_even(aˢ) ds  =  𝔼_{s∼p}[ ε_even(aˢ) ]`,  `p := 2ψ` a probability density

**The entire `a`-dependence sits in the argument `aˢ`. The weight is `a`-independent.**

| control | result |
|:--|--:|
| **(F1)** `L·corr_a` identical across **22 cells** | **1.307e-13** (bar `1e-12`, fixed before any value) |
| abscissa `vc/L` identical | 1.332e-15 |
| reduced form vs the instrument, all 22 cells | **1.334e-13** |
| `∫ψ` over `[−2,2]` | 1.000000000 |

**The two routes agree, so the reduction is the instrument and not a model of it.**

---

## S2 — the kernel's sign: **bench-only, exactly as registered**

`ε_even ≥ 0` at **0 negative samples of 1999. F2 did not fire.** And it stays bench:
`εₙ(ρ) = cₙ ρ^{−1/2} ∫_{1/ρ}^1 ξ̂ₙ(u) ξ̂ₙ(ρu) du` is **an overlap of an oscillating entire function
against its own dilate — not a sum of squares** — and b250's Mercer corners sign only `ε'(1⁺)`.

> **The per-mode table shows why no cheap argument will work: only mode 0 is sign-definite (0
> negatives). Every other even mode takes both signs** — mode 2 at 91, mode 4 at 134, mode 8 at 195.
> **The non-negativity of the sum is a cancellation fact, not a termwise one, and calling it derived
> would be false.** b250's S3(a) wall is the same wall.

### But one thing *is* derived, and it is the hinge: `ε_even(1) = 0` exactly

The owner's own line — *"integrand supported ONLY on u in [ρ⁻¹, 1] → eps(1) = 0"* — and
`per_mode_eps_grids` writes that zero through its own `if hi - lo <= 0: continue`. Measured at the
rebuilt grid's first point: **0.0e+00, exactly.**

---

## S3 — the ferry's monotone-weight step: **refuted, necessarily**

`d/dL[(1/L)ψ(u/L)] = −(1/L²)·d/dr[r·ψ(r)]`, so `corr_a(u)` is non-increasing in `a`
**iff `r·ψ(r)` is non-decreasing.**

**But `r·ψ(r)` vanishes at `r = 0` and at `r = 2` and is positive between — so it must decrease
somewhere.** The refutation is structural, not numerical, and **no choice of bump can repair it: it
follows from the support alone.** Measured: both ends `0.000000e+00`, maximizer `r* = 0.621500`,
**2752 of 4000 samples with `d/dr[r·ψ(r)] < 0`.**

**The direct witness, at a named `u`** (the ferry's own falsifier, firing): at `r = 1.3108`,
`u = 0.7204` — `corr` at `a² = 9` is `0.116152`, at `a² = 16` is `0.132279`. **It increases with `a`.**

*So the ferry's first branch for S4 — conclude by positivity — is closed before it is attempted.*

---

## S4 — the refutation

The second branch is closed too: `d/dL E2even = ∫ p(s)·s·aˢ·ε_even′(aˢ) ds`, and **`ε_even′` changes
sign at the kernel's peak**, so no termwise inspection can conclude. Registered before it was tried.

**The argument that does close, in two lines, using no measured value:**

1. by S1 and S2's hinge, `E2even(a) → 0` as `a → 1⁺` — every `ε_even(aˢ) → ε_even(1) = 0`, and `p` is
   a probability density;
2. `E2even(a) > 0` for `a > 1`.

### **A function that starts at zero and is positive afterwards increases somewhere.**

*The one ingredient that is bench rather than derived is (2)'s strict positivity, and the verdict
carries it.*

**The control — six probe cells, chosen by grid resolution and not by what their values do** (the
finest, `a² = 1.05`, carries **85** grid points):

| `a²` | 1.05 | 1.10 | 1.20 | 1.35 | 1.50 | 1.75 | **2** |
|--:|--:|--:|--:|--:|--:|--:|--:|
| `E2even` | 0.154975 | 0.294741 | 0.526962 | 0.766114 | 0.902826 | 0.992959 | **1.002347** |
| step | — | rise | rise | rise | rise | rise | **rise ← the turn** |

**Six of six strictly smaller than at `a² = 2`, and rising monotonically through the probe. F3 did
not fire.**

### S4b — above the turn: **79 steps, not fifteen**

Sixteen cells could not answer this, and the act says so rather than inheriting the answer: the
kernel oscillates, and `E2even` averages it over a geometric window. **Measured on a dense geometric
ladder `a² = 2..100`, 80 cells: strictly decreasing at every one of 79 steps, 0 rises.**

**And it is still bench. No derivation is claimed, because the kernel it averages is not monotone
and every positivity argument died at S3.**

---

## F4 fired — and the oscillation is the **object**, not the instrument

A registered falsifier fired, and it is reported before anything is made of it. **`ε_even` rises at
448 of 1676 samples past its peak**, largest relative rise `1.101e-02`.

An overlap whose integrand oscillates faster as `ρ` grows is exactly the shape a quadrature failure
takes, so that hypothesis was killed first — **at both axes:**

| axis | sweep | rise count | agreement |
|:--|:--|--:|--:|
| quadrature `NG` | 200 → 400 → 800 → 1600 | **111 at every NG** | ~2e-12 |
| prolate layer `NQ` | 700 → 900 → 1100 | **111 at every NQ** | ~1e-9 |

**And the sweep is shown able to see a failure** — at a deliberately starved `NG = 12` the kernel
moves by **5.674e+00**. *The test is not blunt, so its flatness is evidence.*

### Who oscillates — and a second finding nobody asked for

- **The oscillation is in the *leading* mode.** Mode 0 is the one sign-definite mode and it **still
  rises past its own peak 107 times**. *The comfortable explanation — cancellation between modes —
  is wrong.*
- **`E2even` is effectively a two-mode object on this range.** `|max|` by mode: `0 → 1.199`,
  `2 → 0.282`, `4 → 5.0e-04`, `6 → 1.3e-07`, `8 → 2.2e-13`, `10 → 7.7e-12`. **Not extrapolated
  beyond this range or this truncation.**

---

## The moved axis, declared before any value and priced

b255's `ρ`-grid starts *above* `ρ = 1` and carries ~1.5 points below `a² = 1.05`. **(W1)'s
`np.interp` clamp would therefore have flattened exactly the region the turn lives in — silently.**
This act's grid: **1999 points, dense on `[1,2]`, starting at `ρ = 1` exactly.**

**The cost, printed: G-REPRO against b255 is worst `5.338e-04` at `a² = 2`, falling to `6.5e-06` at
`a² = 64` — largest where b255's grid was coarsest, which is the signature of the repair rather than
of a disagreement.**

---

## The shadow — **11 terminals, zero axioms, 0 errors, profile printed**

`SIDE-global-section/Core/E2EvenMonotoneShadow.lean`, vanilla Lean 4, `decide` only. It carries the
kernel's shape (zero, rise, peak, fall), the six probe cells as integer comparisons, the fifteen
ladder decreases, and the counts.

**Its load-bearing polarity control is `the_ladder_predicate_fails_below_the_turn`** — the ladder's
own decrease predicate *fails* across the turn. **That is the act's finding as arithmetic.** Three
false statements of the same shape were **refused** by the same `decide`, lean exit 1.

### **It does not compile J2 in either direction.** The integral, the prolate overlaps and the autocorrelation are not in `Nat`, and none was forced into it.

---

## Two defects in this act's own harness — both mine, both disclosed

First run: **10 PASS / 1 FAIL / 1 REFUSED, NOT CLEAN** (`audit_b261_check_harness.txt`, `4f9e8c06…`).

1. **The REFUSAL — a summary line that became a datum in the thing it summarized.** The shadow gate
   counts zero-axiom terminals and requires 11; it found 12. **The twelfth was the summary line I had
   appended to the profile, which restated the exact string it was counting.** b213's species,
   arriving through an annotation added for the reader's convenience.
2. **The FAIL — a needle that was *nearly* the sentence**, dropping two words from the middle.
   `contains()` folds whitespace and case; **it does not insert missing words.**

> **That second one is b229's species and the *third consecutive act* caught by it — b229 (a
> substring the target happened to contain), b260 (a phrase only the run printed), b261 (a phrase
> missing two words). The pattern is worth naming rather than re-repairing: a needle typed from
> memory of a sentence is not the sentence, and the habit — not the matcher — is the hazard.**
>
> And it caught me a *fourth* time, inside the same act: the HANDOFF tool's own assert list fired on
> `THE OWNER'S OWN SUPPORT LINE` where the text reads `is the OWNER'S OWN SUPPORT LINE`. **The
> difference that matters is that the assert caught it *before* the write.**

**Re-run after repairs: 12/12 CLEAN.** b260's fixed-point rule is inherited: the bank names only the
failing run and its hash; the shipping sidecar is embedded here, in the report, which no gate reads.

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : check_harness
  act       : b261
  run at    : 2026-08-30T22:44:27 (local)
  input     : 12 checks routed through the harness
  checks    : 12
  pass      : 12
  fail      : 0
  error     : 0
  refused   : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 3510a7c70f82b850cfca15dc62c06826
=== END AUDIT SIDECAR ===
```

---

## Controls

**Tautology control.** (T1) S1's change of variables on 20000 arbitrary tuples: **20000/20000** —
*it is meant to; a substitution that failed on arbitrary data would be an error, not a discovery.*
The reduction's content is not in the substitution but in `ψ` coming out `a`-independent, and **that
was measured (F1), not argued.** (T2) the same pipeline on a **constant** kernel: **0 rises**, every
cell `1.000000000`. **The rise is a property of *this* kernel, not of the machinery.**

**Positive controls.** The sign test finds 3 of 3 on a negative array; the monotone test returns
False on an increasing sequence; a `1e-9` perturbation of `ψ` exceeds the `1e-12` bar; the G-REPRO
comparator against b255's **wrong** column (`E2odd`) deviates by **3.247e-01**, four orders above the
`E2even` match; the probe grid carries **85** points below `a² = 1.05`. In the diagnostics: the
replica matches the instrument at **0.000e+00**, the axis sweep sees a starved-`NG` failure at
**5.674e+00**, and the monotone test correctly returns False on the kernel.

**No instrument was edited.** `b38_act10.py`, `qeps_layer.py`, `carto_atlas.py`, `b255_ladder.py` are
byte-unchanged under `git -C`. The diagnostics file declares its replica — *the same loop with two
axes exposed, because `per_mode_eps_grids` takes no `NG`* — and **nothing from it ships as a value.**

---

## What this act does **not** establish

1. **It does not prove `ε_even ≥ 0`** — bench at 1999 points, and the sum's sign is a *cancellation*
   fact.
2. **It does not prove monotone decrease above the turn** — 79 steps of bench, no derivation.
3. **It does not locate `a₀` beyond `(1.75, 2]`** — no bisection was run and none is claimed.
4. **It does not prove `ε_even → 0`** — a named import, and S5 rests entirely on it.
5. **It says nothing about the limit of the identity.** b15 and b242 govern.
6. **It does not re-verdict b255** (b246's rule).
7. **It does not close M-2**, and does not touch J1's premise.
8. **It does not sign `resid(A)`.** See below.
9. **Nothing about `h2` beyond the register sentence exact. Nothing deposits.**

---

## What the FOOT asked for, and what it got

> *"both terms of resid(A) are then signed by theorem or the exception is named."*

**Neither branch was taken.** J1 signed the junction by theorem; **J2 did not sign `E2even` — it
refuted the monotonicity claim and left the positivity at bench.** There is no resisting step to make
famous, because **the statement is false rather than hard.**

**So b255's (SIGN-EVENT) question is not closed, and it is further from closing than the FOOT
projected.** The arc, honestly: **one term signed by theorem, one term's claim refuted and its sign
still bench.** That is not the arc the FOOT anticipated and the record says so rather than rounding
it up.

---

## Filings

- **Index:** queried before the route was written — `weil criterion` **HIT**, `archimedean
  positivity` **HIT**, both carried at their own acts' grades, neither used as a premise; the reach
  line carried. **`e2even-monotone` / `j2` and `eps-even-oscillates` keyed on this filing.**
- **J2's UNPROMOTED-CANDIDATE status (b256): DISCHARGED — by refutation.**
- **Second row filed: `eps-even-oscillates`** — bench, with the artefact hypothesis tested and killed
  at two axes.
- **J3 — the junction at the level limit — filed as next**, with b260's formula
  `w − τ = w·(pᵏ−1)/(pⁿ−1)` quoted as its object. **Route note: J1's method *does* transfer to J3,
  unlike J2's** — there is a per-term closed form and a shared index set. **But b15 governs: a level
  limit at fixed `p` decides nothing global, and J1's premise travels, so J3 cannot be cleaner than
  J1 is.**
- **New work-order: `W-ORD-EPS-DECAY`** — prove `ε_even(ρ) → 0`. Filed, not run. **It is S5's only
  import.**
- **In flight:** M-2…M-5 open, **none closed.** `W-ORD-B38-HIGHMODE`, `W-ORD-CN-LAW`, the QUOTED-N
  extension, `W-ORD-XI-PERMODE`, `W-ORD-ORDINATE-CACHE`, `W-ORD-STAGING-GUARD`,
  `W-ORD-FILE-E-WORKING-COPY-STALE`, `W-ORD-TE-SPEC`, `W-ORD-TQ-IDENTIFY`, **`W-ORD-EPS-DECAY`
  (new)**.
- **The thirty-seventh seam's debt restated:** term 2's formalization stands, **unpaid and
  untouched.** J2 touches none of its four items — *it concerns the left side's archimedean
  bookkeeping; term 2 is the quotient channel.*
- **HANDOFF** brought current by demotion, prior content kept, read-back identical.
- **The patent lane is independent and untouched** — nothing written or staged under
  `patent-package/` or `PLACE-papers/`, staged by explicit path, no `git add -A`; b256's live b148
  condition re-reported, not resolved; b259's bank left untracked as b259 ruled. **The two uploads
  are noted as done and receipts pending — noted, not verified by this seat.**
- **`PLACE-papers` not touched — no mirror rebuild owed, none claimed, hook not exercised, reported
  either way.**

### The fork at this stop

1. **J3** — the junction at the level limit; J1's method transfers, b15 still governs.
2. **`W-ORD-EPS-DECAY`** — S5's only import.
3. **`W-ORD-TQ-IDENTIFY`** — J1's premise.
4. **M-2's aggregation; M-3; M-5; `W-ORD-CN-LAW`.**
5. **The patent lane**, independent, on your word.

---

### **J2 IS FALSE, AND FALSE FOR A REASON THE OWNER'S OWN SUPPORT LINE ALREADY CONTAINED. `E2even` TURNS AT `a₀ ∈ (1.75, 2]` AND b255's LADDER BEGINS ONE CELL LATER. THE KERNEL OSCILLATES AND THAT IS THE OBJECT, NOT THE INSTRUMENT. `resid(A)` HAS ONE TERM SIGNED BY THEOREM AND ONE TERM'S CLAIM REFUTED — THE (SIGN-EVENT) QUESTION IS NOT CLOSED. NO GRADE MOVED BUT J2's OWN. `h2` STANDS EXACTLY WHERE THE DEPOSIT LEFT IT. NOTHING DEPOSITS. LOCKS LAST.**
