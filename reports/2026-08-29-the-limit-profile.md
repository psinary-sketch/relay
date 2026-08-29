# THE LIMIT PROFILE — b255, 2026-08-29

**Scope:** a bounded bench act. **CONCURRENCY: SOLO.** A finite cell decides NOTHING global
(b14/b15), **no finite ladder decides the limit**, and b242 governs the arithmetic — *"a measured
rate is not a tail bound."* **No fit, no slope, nothing extrapolated.** Nothing deposits.

**Order of record:** **the pricing first** (costs only, no balance value kept) → the ladder read off
the budget → the meanings hashed (`2c7faef1…7864`) → the registration → the run → the verdict. The
ferry's rule was *"the ladder chosen by affordability, never by what its values do"* — **the order on
disk is what makes that checkable rather than asserted.**

---

## The branch: **(MIXED)** — and the split is the finding

| `a²` | 2→3 | →4 | →8 | →9 | →12 | →16 | →20 | →25 | →32 | →36 | →45 | →50 | →64 | →81 | →100 |
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|
| step in `\|resid\|` | + | − | + | − | + | − | + | − | − | − | − | − | − | − | − |

### **Alternating grow/shrink up to `a² = 20`, then eight consecutive shrinks to `a² = 100`** —
`1.001813` down to `0.486920`, more than halving. Two stretches, two answers.
**(RELAXES) is not taken, because the banked rule forbids reading an oscillating stretch as a
relaxation with an excuse.**

---

## The structural finding: the junction is a sawtooth locked to b17's staircase

| `a²` | staircase (2,3,5) | junction | stepped? | moved |
|--:|:--|--:|:--|:--|
| 2 | [1,0,0] | 0.000000 | — | — |
| 3 | [1,1,0] | 0.106484 | STEP | rise |
| 4 | [2,1,0] | 0.087341 | STEP | **fall** |
| 8 | [3,1,1] | 0.244027 | STEP | rise |
| 9 | [3,2,1] | 0.135021 | STEP | **fall** |
| 12 | [3,2,1] | 0.195843 | no | rise |
| 16 | [4,2,1] | 0.210241 | STEP | rise |
| 20 | [4,2,1] | 0.251769 | no | rise |
| 25 | [4,2,2] | 0.161759 | STEP | **fall** |
| 32 | [5,3,2] | 0.085424 | STEP | **fall** |
| 36 | [5,3,2] | 0.089435 | no | rise |
| 45 | [5,3,2] | 0.096564 | no | rise |
| 50 | [5,3,2] | 0.099877 | no | rise |
| 64 | [6,3,2] | 0.091219 | STEP | **fall** |
| 81 | [6,4,2] | 0.071182 | STEP | **fall** |
| 100 | [6,4,2] | 0.076658 | no | rise |

### **Between staircase steps the junction rises — six transitions, six rises, no exceptions. At
steps it falls at six of nine, and on the upper ladder (`a² ≥ 20`) at all four steps while rising at
all five non-steps.**

**The mechanism, read off the columns and not assumed:** `PR` rises smoothly toward 1 while `Θ_q`
rises in **jumps**, gaining a whole level each time the staircase steps. **So the junction widens
when only `PR` moves and snaps shut when `Θ_q` catches up.** That is why the lower ladder oscillates
and the upper does not — below `a² = 20` the sawtooth's amplitude is comparable to `E2even`'s fall
per step; above it the sawtooth has shrunk while `E2even` keeps falling.

**`E2even` by contrast falls monotonically at all sixteen cells** — `1.001813` → `0.410262`, fifteen
steps, one sign.

---

## My registered expectation was backwards, and it is reported first

The hashed meanings file banked *"(RELAXES) on the lower ladder and I do not predict the upper."*
### **That is the reverse of what happened: the lower ladder is the oscillating one, and the upper —
the stretch I explicitly declined to predict — is the clean one.** **I named the right direction and
the wrong stretch, and the stretch was the part I had six cells of evidence about.**

The falsifier as banked **did not fire** — it asked only whether `|residual|` decreases across the
new cells, which it does. ### **But a falsifier that does not fire is not a prediction confirmed.
Mine was wrong in its content and my falsifier was too coarse to catch it, and both are my fault and
not the ladder's.**

---

## No sign-event — and the reason is structural

Registered in advance as *"the outcome I most want to catch"*, so catching it could not look like a
discovery made to order. **It did not occur: all thirty-two entries are negative.** And
`resid(A) = −(E2even + junction)` with **both terms positive at every cell — a sum of two positives
cannot cross zero.** `Θ_q` approaches `PR` from below and never reaches it (`0.928192` against
`1.004851` at `a² = 100`). **A statement about this ladder and nothing else.**

---

## The reach, priced before the ladder was fixed

- **(W1) The ε `ρ`-grid ended at `a² = 12.001` and failed *silently*** — `np.interp` clamps to
  `ee[-1]` rather than raising, so **every cell past 12 would have carried a wrong `E2` with no error
  raised.** Rebuilt to `ρ_max = 100.001`, `EPS_NRHO 240 → 445`.
- **(W2) `Θ_q`'s `scaling_matrix` is dense `N = p^(2n)`:** `a² = 100` → `N = 4096`, ~22 s;
  **`a² = 128` → `N = 16384`, 2.1 GB, ≥1690 s for `p = 2` alone — refused on cost**, and the refusal
  recorded before any value existed.
- **(W3)/(W4)** `left_side` 384 MB / ~5 s per cell; `trace_modes` ~0.1 s.

**The ferry's target was `a² ~ 50–100 if afforded`. It is afforded and the ladder reaches 100.**
One pricing conclusion had to be rewritten: I drafted the wall at `n(2) = 6` and the timing said
`a² = 64` costs tens of seconds. **The conclusion was rewritten to follow the table, which is the
only direction that rewriting may go.**

**The cell-species, said:** `S4 = (2,3,5)` is fixed, so `a² = 49` activates no new prime and **`7`
never enters** — the ladder measures powers of a fixed prime set, not a growing place set. **b14's
double limit is untouched in its first coordinate.**

---

## The G-REPRO debt — registered before it was paid, and paid

Rebuilding the grid changes `E2` for the six banked cells too, so the meanings file fixed a `1e-4`
band **before the rebuild ran**. ### **Worst deviation against b254: `5.64e-06`, inside the band by
a factor of eighteen.** **b254 is not re-verdicted (b246's rule).**

---

## Gates — 14 of 14 CLEAN

**Term scan CLEAN on the second pass:** the first found **two live uses of a banned stem in this
act's own bank**, and they were **replaced rather than excepted.**

**The tautology control had to separate two things that look alike:** the residual's **negativity
*is* forced** once both terms are positive — restatement, and the bank says so rather than counting
it — while the **staircase correlation is not**, so the sawtooth is a fact about the operator and not
about the formula.

Two gates failed first, and both were **my own meaningless negative conjuncts** — demanding the
*absence* of phrases the files legitimately carry. ### **Negation does not make a vacuous conjunct
meaningful; that is the decorative-gate defect wearing a minus sign.**

**PLACE-papers was NOT touched, so the hook was not exercised and the mirror not rebuilt — reported
either way.**

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : check_harness
  act       : b255
  run at    : 2026-08-29T15:25:08 (local)
  input     : 14 checks routed through the harness
  checks    : 14
  pass      : 14
  fail      : 0
  error     : 0
  refused   : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 0e06b95a3665886f5c7834e2b4ae85ed
=== END AUDIT SIDECAR ===
```

---

## Filings

- **Index:** `limit-profile` keyed on filing; queried **NO KEY** first.
- **The profile filed at its grade under R-III's meaning** — no deficit language.
- **The thirty-seventh seam's debt restated:** term 2's formalization stands, **unpaid and
  untouched.**
- **In flight:** M-2…M-5 open, **none closed**. `W-ORD-B38-HIGHMODE`, `W-ORD-CN-LAW`, the QUOTED-N
  extension, `W-ORD-XI-PERMODE`, `W-ORD-ORDINATE-CACHE`, `W-ORD-STAGING-GUARD`,
  `W-ORD-FILE-E-WORKING-COPY-STALE`, `W-ORD-TE-SPEC`.
- **HANDOFF** brought current by demotion, prior content kept, read-back identical.

### The fork at this stop

1. **M-2's finite-place address and the aggregation** — RULE Q's aggregation is **still UNSTATED**,
   and the junction now has a sixteen-cell profile it did not have.
2. **M-3** (class richness).
3. **M-5** (the missing transport).
4. **`W-ORD-CN-LAW`** — derive the `C/n` form.
5. **The patent session**, on your word.

---

### **THE ONE-SIGNED DISTANCE HAS A PROFILE ALONG THE DIRECTION `h2` LIVES IN: OSCILLATING BELOW
`a² = 20`, FALLING AT EVERY STEP ABOVE IT, AND DRIVEN BY A JUNCTION SAWTOOTH LOCKED TO THE
STAIRCASE. MEASURED OVER SIXTEEN CELLS AND NEVER EXTRAPOLATED. M-2…M-5 OPEN. `h2` STANDS EXACTLY
WHERE THE DEPOSIT LEFT IT. NOTHING DEPOSITS. LOCKS LAST.**
