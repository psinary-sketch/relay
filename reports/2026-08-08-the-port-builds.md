# (c′) RULED — THE PORT BUILDS — 2026-08-08

Standing law. Rule 2 throughout. Rail at `de621b1` / `2147a03`. Census held aside. **Nothing
deposits.**

---

## §1 — THE RUNNING WORKER STOPPED CLEANLY

**Recorded BEFORE the stop, so the grade rests on a number that was read rather than remembered:**

| | |
|:--|--:|
| PID | 38220 |
| wall | **30.725 h** |
| CPU | 30.642 h |
| **CPU/wall** | **0.9973** |

Stopped at the stage-3 bank. **Its stage-4 partial work — exactly one taylor chunk, 16 of 6002
boundary values — discarded as priced.** Stages 0–3 untouched and archived to
`epstein_li_chunks.mpmath-stage0-3.jsonl` before anything else ran, because they are the port's
ground truth and a gate cannot be run against a bank the build might overwrite.

**The detachment evidence keeps its grade unchanged: 30.7 unbroken hours at CPU/wall 0.9973, the
second verified confirmation.** No mechanism was identified and none is claimed; a future stop
while detached still weakens it.

---

## §2 — THE PORT

`D:\relay\tools\e16\epstein_li_v3.py`. **v2 with the engine swapped and nothing else moved.**

| hot path | was | is |
|:--|:--|:--|
| boundary evaluation of E(s) | `mpmath.gammainc` | `flint acb.gamma_upper` |
| the coefficient phase's inner sum | `mpmath.expjpi` | `flint acb.exp_pi_i` |

Algorithm, chunk format, dataset declaration, staging schedule and the λ recurrence are unchanged.
The λ recurrence is still mpmath — it was <1% of measured cost and is not a hot path.

### Precision plumbing, stated because this is where a port silently loses exactness

Every `arb ↔ mpf` conversion is a **binary mantissa/exponent transfer** —
`x.mid().man_exp()` out, `±arb(man)·2^exp` back. **There is no decimal round-trip anywhere.** Both
directions were verified to give **exactly zero difference** on √2, −1/3, 2⁻⁹⁰⁰, 2⁹⁰⁰, 0 and 1
*before the file was written*. A `.str()`-based conversion was the obvious shortcut and would have
silently capped every banked value at whatever digit count was passed to it; the byte-identity
lesson governs. Working precision is `ctx.prec = mp.prec + 64`.

**The circle's radius is reproduced bit-exactly rather than re-derived.** v2's
`RADIUS = mp.mpf("0.4")` evaluates at module load with dps still 15, so the radius is the *double*
0.4 = 3602879701896397·2⁻⁵³ at every stage. v3 transfers that exact binary value into arb.
Computing `arb(2)/5` instead would have rounded to working precision and moved the geometry — a
difference no test in the suite was aimed at.

### The one declared deviation beyond the engine swap

The coefficient phase reduces its root-of-unity index mod 2N and **memoises** the N distinct
factors. Mathematically identical (exp(πix) has period 2, and the reduction is exact integer
arithmetic); not an algorithm change. **Declared on the file's face and tested directly by G2c′.**
`acb.dft` would collapse the phase to an FFT — that *would* be an algorithm change and is
deliberately **not** taken.

---

## §3 — THE GATES

### G1 — ζ self-test · **PASS**

| | |
|:--|:--|
| ported λ₁ | 0.023095708966121033814 |
| published | 0.023095708966121 — rel_err **1.46409×10⁻¹⁵** |
| the incumbent's own recorded run | 0.023095708966121033 — rel_err **3.52581×10⁻¹⁷** |

Tolerance 2×10⁻¹⁵, declared before the run and set at the incumbent's own standard (its recorded
rel_err was 1.5022×10⁻¹⁵) because the published constant is what limits the comparison. **The port
agrees with the incumbent to every digit the incumbent recorded.** Elapsed 0.2 s.

### G2 — the banked-stage reproduction · **PASS** — the strongest gate, available only because the stages banked

**Stages 0–3 recomputed end-to-end by the ported engine in 0.169 h.** The incumbent spent ~31 h on
the same work.

**G2a — stage summaries against the bank.** All four stages: `min_lambda` and `lambda_last`
**relative difference exactly 0.0** — identical to the last bit of the double — and `argmin` (=1)
and `first_negative` (=None) **EXACT** at every stage.

**G2b — stage 3, value by value.**

| | compared | result |
|:--|--:|:--|
| boundary values | 3002 | worst relative **3.06527×10⁻⁹⁰⁰** at j=1621 · 0 outside 10⁻⁵⁰ |
| coefficients | 1500 | propagated λ error **3.97888×10⁻⁸²** against a 10⁻⁹ ceiling |

**The a-priori certificate had predicted ≤1.961×10⁻⁸² for one engine's error; the measured
two-engine difference is 3.979×10⁻⁸², i.e. 2.03× — the bound is tight to the factor of two you
would expect from adding two independent errors.** That is a stronger result than the gate asked
for: it validates the error analysis, not just the port.

### G2c — the declared deviation · **FAILED AT ITS DECLARED TOLERANCE, and the failure stands**

28 of 60 coefficients outside the declared 10⁻²⁰⁰, worst 2.97×10⁻¹⁰⁷ at m=59.

**The failure was in the test, not the port, and the fault was mine.** I declared 10⁻²⁰⁰ on the
reasoning that "the cancellation loss is small on a small case" — after writing the law that
refutes it into this same file's G2b header. At dps 120 (~140 digits) and m=59 the law predicts
140 − 0.547×59 = 108 correct digits, and 2.97×10⁻¹⁰⁷ is exactly that. **Recorded rather than
patched over, because a threshold that gets relaxed until it passes is worth nothing.**

### G2c′ — the same claim, retested with **no threshold at all** · **PASS**

Arb carries a rigorous error radius, so "are these two computations consistent with the same true
value?" has an exact answer: **do the intervals overlap.** Not tunable, not choosable after seeing
a number, and strictly stronger than any tolerance I could have picked.

| | |
|:--|--:|
| coefficients compared | 60 |
| **intervals disjoint** | **0** (criterion: 0) |
| propagated λ difference | 1.25223×10⁻¹⁰⁶ |
| memoised vs fresh cost | 0.006 s vs 0.026 s |

### G3 — the Rule 2 interrupt gate · **PASS on all four cases**

| case | killed | resumed | byte-identical |
|:--|:--|:--|:--|
| mid-boundary kill | ✓ | ✓ | ✓ |
| mid-coefficient kill | ✓ | ✓ | ✓ |
| hand-injected torn tail | ✓ | ✓ | ✓ |
| cache relabelled to another stage | ✓ | ✓ | ✓ |

Byte identity against an uninterrupted reference run, not a tolerance. **One correction: the first
attempt died in the gate's own comparison helper, which could not parse the torn tail the gate
itself had injected. The worker's loader — the thing under test — handled it correctly throughout;
the harness was fixed, not the worker.**

---

## §4 — THE FINDING THE PORT MADE VISIBLE, AND IT IS NOT A PORT DEFECT

**Building the coefficient phase I put a floor on each coefficient's certified relative accuracy.
G1 killed it at m=77 of 120. Measuring instead of arguing showed the floor was guarding the wrong
quantity — and the measurement led somewhere that matters.**

c_m is extracted as Re(acc_m)/(N·r^m) with r = 0.4. The absolute error of acc_m is ~4N·max|log E|·2⁻ᵖʳᵉᶜ,
independent of m, so

> **|δλ_n| ≤ 4·n·max|f|·2⁻ᵖʳᵉᶜ · (1/r) · (1 + 1/r)ⁿ⁻¹**

— the N cancels — and **extracting Taylor coefficients on a circle of radius r and recombining them
with binomial weights costs (n−1)·log₁₀(1+1/r) digits. At r = 0.4 that is 0.54407 digits per unit
of n.** Against the registered dps schedule:

| stage | nmax | dps registered | dps required | |
|--:|--:|--:|--:|:--|
| 0 | 120 | 120 | 76 | OK (+44) |
| 1 | 300 | 220 | 175 | OK (+45) |
| 2 | 700 | 450 | 393 | OK (+57) |
| 3 | 1500 | 900 | 828 | OK (+72) |
| **4** | **3000** | **1600** | **1645** | **SHORT by 45** |
| **5** | **5000** | **2400** | **2733** | **SHORT by 333** |
| **6** | **7000** | **3200** | **3821** | **SHORT by 621** |
| **7** | **9000** | **4000** | **4910** | **SHORT by 910** |

**The registered precision is adequate exactly through stage 3 and short from stage 4 on. The run
halted for re-pricing at precisely the last stage its own dps schedule could support.**

**This is not a port defect. The incumbent engine had identical exposure and no way to see it,
because mpmath carries no error radius.** Had (a) been ruled, stage 4 would have spent five days
producing a λ whose error bound exceeded the quantity being measured, and nothing in the pipeline
would have said so.

### What the build did about it — declared, not done quietly

1. **A dps floor raises dps only where the certificate forbids the registered value.** Stages 0–3
   are untouched, so every banked value and the whole of G2 stand unchanged.
2. **A hard certificate on the actual run.** No stage banks a λ whose rigorous error bound exceeds
   10⁻⁶; the run refuses and files instead. Measured at stage 3: bound 1.961×10⁻⁸².

**Raising precision is verdict-neutral — it cannot manufacture a first-negative index, whereas
running short can.** The asymmetry of the risk is why the deviation was taken rather than deferred
to a ferry. **It is a deviation from "dps schedule unchanged" and the author's ruling is invited on
it; the alternative was to spend the run producing numbers the certificate would then refuse.**

---

## §5 — PRODUCTION

### THE RESTART COMMAND, VERBATIM, STATED BEFORE LAUNCH

```
powershell -ExecutionPolicy Bypass -File D:\relay\tools\e16\launch_v3.ps1
```

**Re-running that one line after any stop is the whole recovery procedure.** The tail guard
validates v / stage / dps / phase / idx / n, refuses a cache from another stage or precision, drops
a torn tail and recomputes from the last good chunk. No argument has to be remembered and no state
has to be repaired by hand. G3 is the evidence that this is true rather than intended.

**Cadence re-set against the NEW measured per-item cost, not inherited.** The mpmath worker banked
every 16 boundary values because each cost 19–31 s. Flint costs 0.135 s at stage-3 precision, so 16
would bank ~470 times a minute and the fsync would become the run. **Production cadence: 256.** G3
ran at 8 to make interruption likely — a correctness gate does not test a rate, and the two numbers
are chosen separately for that reason.

**Sleep posture verified on both columns, not the AC column alone.** AC: never sleep, never
hibernate. **DC: sleep at 20 min, hibernate at 3 h — and a battery is present.** The run is safe on
mains only.

### The registered experiment carries over UNCHANGED

Dataset t ∈ [0.5, 20.0], σ ∈ [0.52, 1.50] · **census held aside** · three windows with ±15%
tolerance, one-period phase extensions, the seventeen-wide [5950, 5967] ambiguity strip ·
below-all-windows routes to the low-t/real-zero check **before** instrument doubt · completion
protocol: registrations restated verbatim first, then the number, then the verdict mapped, **no
interpretation beyond the mapping**. I-7 to be re-confirmed at both stages in the completion report.

### Projection, on measured rates rather than the benchmark's estimate

| stage | nmax | dps | boundary | λ recurrence | stage total |
|--:|--:|--:|--:|--:|--:|
| 4 | 3000 | 1645 | ~0.41 h | ~0.17 h | ~0.6 h |
| 5 | 5000 | 2733 | ~1.21 h | ~0.86 h | ~2.1 h |
| 6 | 7000 | 3821 | ~2.50 h | ~2.5 h | ~5.0 h |
| **cumulative to the registered depth n ≈ 7000** | | | | | **~8 h** |
| 7 | 9000 | 4910 | ~4.29 h | ~5.6 h | ~10 h |
| **cumulative to n = 9000 as registered** | | | | | **~18 h** |

Boundary cost measured as ~dps^1.154 across four stages. **~48 days became well under one day**,
and that is *with* the raised precision the certificate demands.

---

## §6 — THE SECOND AMDAHL PASS: PRICED, NOT RUN — AND THE RE-PRICE'S EXPECTATION CORRECTED

**Measured against the incumbent's stage-3 split:**

| phase | mpmath | flint | speedup | benchmark had predicted |
|:--|--:|--:|--:|:--|
| boundary | ~26 h | 0.113 h | **230×** | 242× ✓ |
| coefficients | ~3.5 h | 0.008 h | **437×** | 9.0× ✗ |
| λ recurrence | minutes | 0.020 h | unchanged (still mpmath) | — |

**The re-price recorded that the coefficient phase would become dominant after the port. It did
not, and the correction is filed here.** The 9.0× benchmark measured the phase *without*
memoisation; memoising the N distinct roots of unity — the declared deviation, gated by G2c′ —
collapsed it by 437× instead, to 6% of stage-3 cost.

**What became co-dominant instead is the λ recurrence: untouched mpmath, O(n²), and by stage 6
about 45% of the run.** That is the target any *next* optimisation would have to attack, and
**per the standing rule it gets no commitment without its own benchmark.** `acb.dft` on the
coefficient phase is likewise available and likewise unpriced; it is an algorithm change and was
refused here on that ground.

---

## §7 — THE EXCLUSION LADDER

Resumes tightening as stages bank: **n = 3000 → β > 0.50092 · n = 7000 → β > 0.50043.** Exact and
phase-free, and it accrues whether or not any window is entered.

**Stage 3 stands unchanged and nothing is adjudicable yet:** running minimum 0.682682 at n = 1,
no negative index through n = 1500, far below every prediction window (the lowest opens at 2872).
**No verdict is implied and none is available.**

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `f38e9fa` → this pass's commit |
| relay | `581dd7f` → this report's commit |
| kernel `5e668b4` · lv `2f71068` · rail `de621b1` / `2147a03` | unmoved |

Census parked at 451 records. **Nothing deposits.**

---

## §8 — POST-LAUNCH, and one probe that caught its own gap

**Production detached, PID 30664**, stages 0–3 re-run under the ported engine so the production
bank is entirely flint-produced and internally consistent, then 4 → 7. Stages 0–2 banked, each
carrying its own `lam_error_bound` and the `dps_registered` / `dps_raised` pair. Stage 3 running at
**0.135 s/value against the incumbent's 19–31 s**, prec-bumps 0.

**THE MIRROR PROBE FOUND A REAL GAP AND ALSO A FALSE ONE, and both are recorded.** The first probe
returned **eleven ABSENTs against a null path** — it searched for `MIRROR*.md` when the mirror is a
zip, so it searched nothing at all. That is the false-zero shape already on the record and it was
caught by the count being implausible rather than by the tooling. Re-run against the extracted
archive (23 roster files, 2757 KB), **ten of twelve probes FOUND**.

**The two genuine absences were one defect: `launch_v3.ps1` and the propagated-error figure lived
only in this report, which is off-roster.** OPEN_TRAILS *mentioned* that a restart command had been
stated verbatim before launch and did not state it. **That is precisely the I-8 shortfall —
findability from the mention — and it was closed by co-locating the command with its name rather
than by pointing harder.** Re-probe at `cf88ab7`: **twelve of twelve FOUND.**

## PINS AT CLOSE

| repo | pin |
|:--|:--|
| PLACE-papers | `cf88ab7` |
| relay | `ff412ea` → this amendment's commit |
| SIDE-kernel | `5e668b4` unmoved |
| SIDE-lv-conservation | `2f71068` unmoved |
| **rail** | **`de621b1` / `2147a03` unmoved** |
