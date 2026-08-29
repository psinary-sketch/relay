# THE LEFT MODE AXIS — b242, 2026-08-29

**Scope:** a bounded bench act on the **left side's instruments only**. The right side appears in
no tool of this act and no residual against it is computed anywhere; `A` enters solely as the
constant inside `resid47 := Tr_full − A − E2N`, as the registration declared in advance. A finite-
place-set object at a finite cell decides NOTHING global (b14/b15). No grade moves. `RULE M-1`
unamended, File E untouched. PLACE-papers, HANDOFF, the loom and the mirror untouched.
**All ledger filings defer to the serializing close (b244).** Nothing deposits.

> **b14:** *"a **finite-place-set object at a finite model cutoff** — the complete roster is the
> double limit and **STAYS OPEN whatever this act shows**."*
> **b15:** *"**a finite-place-set object at a finite cutoff decides nothing global**."*

**PART 0, done first as the header directs:** relay's pending commit `b34a41d` (the b241 bank) was
pushed from a `push-*` branch per Rule 4.10, read back by `ls-remote` at
`b34a41de243bb53db1993bf5f849db67c97bf285`, and the HELD carrier files verified **absent** from the
pushed tree. The record is whole at HEAD.

---

## The branch: **(SLOW)** — and both registered expectations were wrong

Convergence is **measured** on the certified range — every ratio < 1 at every cell — and **an
envelope is beyond reach at these instruments.** The obstruction is priced.
### **`bar_L` is HELD, NOT CERTIFIED. M-4 is NOT paid at bench. `W-ORD-LEFT-MODE-AXIS` is
DISCHARGED**, as the ferry directs on every branch.

- **The ferry seat** leaned **(BOUNDED)** — inferred by me from its FOOT, not quoted. Not borne out.
- **I registered (BOUNDED-BY-FLOOR)** — a branch the ferry did not name, admitted in advance at
  registration (C) precisely so finding it could not be confused with inventing it. ### **Also not
  borne out, and the way it failed is the sentence worth keeping: I predicted the arithmetic floor
  would BOUND the series. It does not. A floor hides a tail; it does not bound one.** The modes
  below the eigenvalue floor are not small — they are **unresolvable**, and an unresolvable term is
  an obstruction, not a bound. I wrote "`bar_L` is still certifiable." It is not.

---

## 1. The measurement — moving the two axes apart

b240's step moved `NQ` and `NMODE` **together**. This act moved them separately, which is its whole
reason to exist.

**The positive controls came first**, because a "slow" verdict from a method that cannot see fast
convergence is worthless. `Σ λ²ₙ ξₙ(1)² → 2.0` **exactly** (b38's own gate): errors 2.0e+00,
1.6e+00, 4.3e-02, 1.3e-04, 1.2e-07, 5.2e-11, 3.3e-15. `Σ t(n) → 22.9964757`: same shape.
### **Both converge super-exponentially and the method sees it — and both flatten at a floor from
mode 6–7. The controls found the floor before the trace series was looked at.**

**Axis 1, pure truncation** (`a² = 2`, NQ held at 700):

| NMODE | `tr[n]` | `Tr_full` | `E2N` | `resid47` |
|--:|--:|--:|--:|--:|
| 5 | +0.327495 | +3.124023 | 1.679428378 | +3.435122 |
| 6 | +0.288754 | +3.412777 | 1.679428394 | +3.723876 |
| 7 | +0.256926 | +3.669703 | 1.679428394 | +3.980802 |
| 8 | **+0.051278** | +3.720981 | 1.679428394 | +4.032080 |
| 9 | **+0.003358** | +3.724339 | 1.679428394 | +4.035438 |
| 10 | **+0.013137** | +3.737476 | 1.679428394 | +4.048575 |
| 11 | **+0.012775** | +3.750251 | 1.679428394 | +4.061350 |

### **The two channels behave completely differently.** `E2N` is **converged by mode 6** —
increments 4.0e-03, 1.4e-05, 1.6e-08, then zero, exactly as its `λ²/(1−λ²)` weight predicts.
`tr[n]` is not: it falls **slowly** across the certified modes and then goes **non-monotone**
(0.0513 → 0.0034 → **0.0131**, a fourfold rise). A term that rises is not a decaying series.
`resid47` **grows monotonically at every one of the six cells** and shows no trend toward zero.

**Axis 2, pure quadrature** (NMODE held at 10): `Tr_full` at `a²=2` runs 3.743342, 3.737476,
**3.913311**, 3.899090, 3.855349 — increments 5.9e-03, **1.8e-01**, 1.4e-02, 4.4e-02.
### **It does not converge in NQ either, and its largest step is in the middle of the range.**

### The finding that re-reads b240's own bar

`bar_L := 4 × max(|dL|(NV), |dL|(mode))`, and its mode limb was one step of `(700,10) → (900,11)`.
Separated:

- the **NQ** 700→900 step alone, NMODE held: **1.7584e−01**
- b240's whole `|dL|(mode)`: **1.8632e−01**
- the **NMODE** 10→11 step alone, NQ held: **1.2775e−02**

### **b240's "mode refinement" is ~94% quadrature and ~6% truncation. The bar named for the mode
axis was measuring the quadrature axis.** b240 said the mixing was there — *"a step that moves NQ
and NMODE together so it mixes quadrature with truncation"* — but not the proportion, and the
proportion is the point: the work-order it filed asked for the mode-sum tail to be bounded, and the
number that provoked it was almost entirely something else.

---

## 2. The eigenvalue floor — hazard H-c, named before it was met

| n | 4 | 5 | 6 | **7** |
|:--|--:|--:|--:|--:|
| `λ²ₙ` | 7.47e−06 | 5.82e−09 | 2.07e−12 | **4.75e−16** |
| digits gained | 2.67 | 3.11 | 3.45 | 3.64 |

### **The certified ceiling and the arithmetic ceiling are not the same number.** Lemma F.1
certifies **eleven** terms; float64 carries **seven**. `qeps_layer` takes 11 and four of them are
below the floor. That is not a defect in the lemma — the lemma is about the series, the floor is
about the arithmetic.

**And the obvious fix is dead:** at NQ = 500, 700, 900, 1100, 1300 → `n_last = 6` at **every one**.
`λ²[6]` does not move at all across a factor of 2.6 in NQ. ### **More quadrature buys no modes.**

The grid confirms H-c to the column — NQ-spread of the truncated trace:

| `a²` | NM=4 | NM=5 | NM=6 | NM=7 | **NM=8** | NM=9 | NM=10 |
|:--|--:|--:|--:|--:|--:|--:|--:|
| 2 | 4.5e−04 | 8.0e−04 | 4.5e−04 | 7.0e−04 | **1.5e−01** | 1.7e−01 | 1.8e−01 |
| 12 | 1.4e−04 | 7.1e−04 | 5.8e−04 | 1.0e−03 | **4.3e−02** | 5.9e−02 | 6.1e−02 |

### **The jump is at NM=8 — the column at which mode n=7, the first below the floor, enters the
sum.** Stable at ~5e−04 to its left; **61× to 249×** worse to its right. The prediction was
registered as falsifiable and the measurement could have refuted it.

---

## 3. The envelope — derived, printed, and then refused

Banked at `data/b242_envelope.txt`, sha256 `0ce32e54…e9d4f0c7`; the confirming run prints that hash
into its own output **and** refuses to execute unless the envelope is older on disk. Either limb
alone is forgeable.

Measured ratios on the certified range (`a²=2`): 0.8975, 0.6113, 0.6944, 0.8690, 0.8817, **0.8898**.
### **The ratio is rising across the last four certified modes at every cell.**

| `a²` | tail(r_last) | b240's `bar_L` | tail / `bar_L` |
|:--|--:|--:|--:|
| 2 | 2.073985 | 0.745264 | **2.78** |
| 8 | 0.645073 | 0.267192 | 2.41 |
| 12 | 0.578951 | 0.203446 | **2.85** |

### **It is not banked as an envelope, and three reasons are given, any one sufficient:**
(i) the ratio is **rising** — a geometric envelope needs a ratio bounded away from 1, and seven
points cannot distinguish "converging to ~0.89" from "rising to 1"; (ii) the extrapolation is
unverifiable **in principle** at this instrument, since the modes that would test it are below the
float64 floor and more quadrature does not reach them; (iii) **no owner proves the trace series
converges at all** — §20(b)'s *"whose low-mode terms decay slowly"* is a description, not a
convergence theorem. ### **An envelope on an unproven-convergent series is a guess with a formula
on it. This act could have banked one. It declined.**

### The direction, disclosed — and the consequence *not* drawn

The refused extrapolation points the same way at all six cells: **2.4× to 2.9× `bar_L`.** If the
series continues as its certified part decays, `bar_L` is not merely uncertified — ### **it is too
small**, and a bar that is too small is the direction that makes a separation look *more*
significant than it is. ### **This act does not draw the consequence for any face-off branch and
may not** — its scope forbids the right side. **It is routed to b244 as a named precondition,
stated at full size rather than buried**, because an executor who measures a bar and hides which way
it moves has not reported the measurement.

---

## 4. The hypotheses, judged

- **H1** (resid47 dominated by the withheld eleventh ε mask) — **REFUTED**, re-measured not cited:
  `E2n[10]` = 5.6e−18 … 9.0e−15 against a `resid47` of 2.31…4.06. And **the face b241 did not
  measure**: the withheld eleventh **trace** mode `tr[10]` = 0.012775 … 0.002418 — larger by fifteen
  orders, still ~0.3% of `resid47`. **Neither face dominates anything.**
- **H2** (resid47 is the trace series' truncation remainder) — **REFUTED BY MEASUREMENT.** The
  refutation was registered in advance as a sign argument and then **checked at source**:
  `tr[n] ≥ 0` at every mode and all six cells, so more modes only *increase* `Tr_full` and `resid47`
  — already positive — only grows. §25(a)'s import is re-verified rather than leaned on.
- **H3** (resid47 is the unperformed divergent-part subtraction — M-4's unpaid size) —
  **SUPPORTED**; it was my registered hypothesis and its registered prediction ("flattens or grows,
  no trend toward zero, at all six") holds. **Supported is not proved:** the measurement rules out
  H1 and H2 and is consistent with H3; it does not establish H3 against every alternative.
- **H4** (scale/normalization mismatch, §25(c)'s failed model transport) — **NOT SETTLED, and not
  claimed to be**, exactly as registered.

---

## 5. The obstruction, priced in the units it would be paid in

### **The binding resource is WORKING PRECISION, not quadrature density.** At the measured ~3.45
decimal digits per further mode (and still rising): +9 modes → ~48 dps; +20 → ~85 dps. For a tail
below 0.01 from each cell's own ratio: `a²=2` needs ~46 further modes (**~175 dps**); `a²=12` ~34
(**~134 dps**). ### **That is a prolate eigensolver in extended precision — a different instrument,
not a refinement of this one.** `prolate_layer.prolate` is a float64 eigendecomposition and no NQ
makes it a bignum one.

**The cheaper partial move, named because it costs nothing today: truncate the trace at NMODE = 7.**
It removes the floor-mode noise entirely (NQ-spread 5e−04 instead of 6e−02…1.8e−01). ### **It does
not bound the tail** — the tail becomes explicit and unmeasured instead of implicit and
contaminated. **That is an improvement in candour, not in accuracy**, and is offered as nothing
more. Not adopted here: changing the base axis is a **ruling**, and RULE M-1 binds C2 to the
instrument as it stands. **Routed to b244.**

---

## Gates

**15 of 15 PASS, CLEAN — on the fourth run.** The scope-wall gate failed twice, for two different
reasons, and both are reported because a reader cannot tell which kind a silent gate was:

- **Run 1 — a genuine breach.** `b242_mode_axis.py` unpacked `A, P, PR = B38.left_side(...)`,
  **binding** the prime column in a left-side-only tool. Never used, no residual formed — ### **and
  the gate was still right.** Repaired **in the code**, not in the gate.
- **Run 2 — a false hit, of a species the corpus has named twice.** The gate matched `PR` inside
  **"S*PR*EAD"** and **"*PR*ICED"** (b164: *"retrieval by string is not retrieval by object"*), and
  matched the tools' own **scope declarations**, which name the forbidden objects in order to forbid
  them (b142: *"a scanner with no scope control does not report the rule — it reports the corpus"*).
  Repaired by giving the gate **scope control and object matching** — docstrings and comments
  stripped by `ast`, tokens matched as identifiers — ### **and not by weakening the rule.**

The **arbitrary-inputs tautology control** the ferry requires: this act's truncation axis rests on
one algebraic step — that partial sums are cumulative sums — and gate 7 shows that step is a
**tautology** on 400 random arrays, so it is *not* where the act's content lives. The content is the
empirical gate `trace_modes(NMODE=5) == trace_modes(NMODE=11)[:5]`, which **can** fail and passed at
`0.00e+00`. Two absences positively controlled. Term scan **CLEAN**, 0 live over 2004 lines.

Also reported: **two `%d` format arguments attached to the wrong `rec()` call, in two tools, the
second after the first was fixed.** The first crashed a run; the second printed a literal `%d` into
the envelope file and ### **would have been hashed and gated as the banked envelope** had it not
been caught before the hash was taken. **A tool that crashes announces itself; a tool that prints a
wrong character does not.**

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : check_harness
  act       : b242
  run at    : 2026-08-29T09:59:16 (local)
  input     : 15 checks routed through the harness
  checks    : 15
  pass      : 15
  fail      : 0
  error     : 0
  refused   : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 8eae1189aecfe724a2618ca94c29ed99
=== END AUDIT SIDECAR ===
```

**Banked:** `data/b242_registration_2026-08-29.txt` · `data/b242_left_mode_axis.txt` ·
`data/b242_mode_axis_run.txt` · `data/b242_floor_grid.txt` · `data/b242_envelope.txt` ·
`data/b242_confirm_run.txt`, with resumable axis points in `data/b242_axis_points.json` and
`data/b242_floor_points.json`.

---

### **`bar_L` HELD, NOT CERTIFIED. M-4 NOT PAID AT BENCH AND NOT RE-PRICED AS STRUCTURAL.
`W-ORD-LEFT-MODE-AXIS` DISCHARGED. NO RIGHT-SIDE OBJECT COMPUTED. NO GRADE MOVED. NO ENVELOPE
BANKED THAT THE MEASUREMENT DID NOT SUPPORT. M-2…M-5 OPEN. FILINGS DEFER TO b244. NOTHING ABOUT
`h2` BEYOND THE REGISTER SENTENCE EXACT. NOTHING DEPOSITS. LOCKS LAST.**
