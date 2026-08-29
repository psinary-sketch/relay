# THE PRECISION VEIL LIFTED — b249, 2026-08-29

**Scope:** a bounded instrument construction and measurement (K3), discharging
`W-ORD-MODE-PRECISION`. ### **No derivation and no theorem.** The statement measured is b247's,
unchanged. **PARALLEL-OK with b248** — this act wrote only its own relay `data/` files; its filings
defer to b248's close, which carried them. A finite-place-set object at a finite cutoff decides
NOTHING global (b14/b15). Nothing deposits.

---

## The verdict: **BRANCH (PLUNGES)** — M-4 **TRUE-AT-BENCH**

### **And the limit in the same breath: true-at-bench is a bench grade and not a theorem.** It is a
measurement over finitely many modes at one instrument setting. ### **M-4 is not paid, and its
statement still halts at clause (i)'s rate, exactly where b247 left it.**

---

## 1. The instrument — and why the corpus route was *not* reused

The ferry directs the corpus's own instruments first. ### **The corpus route resists, and the reason
is b247's own verdict.** `b205_prolate.py` is a Frobenius/Taylor stepper for the **RRJT exterior ODE
on `[1,∞)`** — its own docstring: *"y_I : the analytic local solution at x = 1 … alpha =
psi(x_0)/y_I(x_0)"*. b247 ruled, definition against definition, that its `α` and the prolate
`ξ_n(1)` are **(DOUBLE-NAME)**. ### **Reusing it here would have been exactly the error this
programme ruled against one act earlier.** The *species* is the precedent; the instrument is not.

**The route chosen: a direct extension of the corpus's own prolate instrument into mpmath** —
Gauss–Legendre nodes by Newton iteration, the corpus's own kernel, symmetric eigendecomposition, at
**dps 120 / NQ 80**, reaching `n = 0…12` on the **even** sub-sequence per pin P1. ### **One thing
changes — the arithmetic** — which is why G-REPRO can catch any error against b242's float64 table.
b242 had already shown the floor did *not* move with quadrature (`n_last = 6` at every NQ from 500
to 1300), so the limit was arithmetic and this route changes precisely that.

**All three gates pass.** G-EQ: max residual of the eigenvalue equation over all returned modes
`< 1e-100`. G-SELF: dps 60 against dps 120, agreeing far below the reported digits.

---

## 2. The measurement — past the veil for the first time

The veil sat at `n = 7`, where b242's float64 measured `4.7e−16` and could not distinguish it from
noise. **Every row from `n = 7` on is new.**

| `n` | `λ(n)²` | `ξ_n(1)` | `t(n)` | partial sum |
|--:|--:|--:|--:|--:|
| 6 | 2.07207356687e−12 | 4.994292243 | 5.1683637761e−11 | 22.99647568387052 |
| 7 | **3.85119077971e−16** | 5.381808728 | 1.11545370551e−14 | 22.99647568387053 |
| 8 | 4.10067955189e−20 | 5.742442256 | 1.35222545244e−18 | 22.99647568387053 |
| 9 | 2.680155263e−24 | 6.081348198 | 9.91196350927e−23 | 22.99647568387053 |
| 10 | 1.13438645849e−28 | 6.402139853 | 4.64955455185e−27 | 22.99647568387053 |
| 11 | 3.24536795265e−33 | 6.707494858 | 1.46010685555e−31 | 22.99647568387053 |
| 12 | **6.49992498821e−38** | 6.999474559 | **3.1844851161e−36** | 22.99647568387053 |

### **`t(n)` plunges and the partial sums settle at `22.996475683870529679`** — against the corpus's
**independently banked `ε′(1⁺)` pin `22.9964757`** (b35, 2026-08-18). **Eight significant digits, and
the pin was not fitted to:** the series was computed from the operator without reference to it.

### And the finding that bears on b247's clause (ii)

`ξ_n(1)` **does** keep growing past the veil — 5.38, 5.74, 6.08, 6.40, 6.71, 7.00 — ### **but only
slowly: every ratio is under 1.2.** So the factor of ~36,000 b247 measured across the certified range
is **utterly dominated** by a `λ²` falling roughly four orders per mode. The "growth dominated" form
of clause (ii), which b247 showed was the only live one, is what the measurement supports.

**The empirical rate is reported as an observation with its window named.** ### **No extrapolation is
banked as a bound** — b242's refusal is the precedent, and **a measured rate is not a tail bound.**

---

## Gates — and a third consecutive print-floor

**12 of 12 PASS, CLEAN on the first run.** But G-REPRO itself **took three forms before it was
right**, and both failures are disclosed:

1. **A constant tolerance is not the ferry's criterion.** The registered criterion is *"within
   float64's own error"*, which is **mode-dependent** — b242's relative error on a `2e−12` eigenvalue
   is ~`1e−4`, not a fixed number. ### **The gate was right to reject a constant.**
2. **The comparison is additionally floored by the printed precision of b242's bank** — ten
   significant digits for `λ²`, nine decimals for `ξ`, and the two have *different* relative floors.
   Collapsing them into one constant is what failed the second form.

### **That is the third consecutive act to meet a bank's print floor:** b245's T-E met b38's four
decimals; b246 floored at 5e−5 for the same reason; b249 met b242's ten digits. ### **`W-ORD-TE-SPEC`
requires a bank's *axes* be named; it does not require its *printed precision* be named — and it
should. Filed for extension.**

The final tolerance is `quad(n) + 10·eps₆₄/λ(n)² + print_floor(n)`, **every term measured or computed
from the bank's own formatting, none chosen.** And the direction is stated: **where the two disagree,
it is b242's value that is the less accurate one** — the new instrument sits inside the old one's
error bars.

Term scan **CLEAN**, 0 live over 868 lines. **PLACE-papers, HANDOFF, the loom and the mirror were not
touched by this act** — they are b248's, which carried this act's filings.

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : check_harness
  act       : b249
  run at    : 2026-08-29T12:33:48 (local)
  input     : 12 checks routed through the harness
  checks    : 12
  pass      : 12
  fail      : 0
  error     : 0
  refused   : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 f1d31427de9266026a0e4d7afb2053d4
=== END AUDIT SIDECAR ===
```

---

### **THE VEIL IS LIFTED AND `t(n)` PLUNGES. `W-ORD-MODE-PRECISION` (K3) DISCHARGED. M-4 IS
TRUE-AT-BENCH — A BENCH GRADE, NOT A THEOREM — AND ITS STATEMENT STILL HALTS AT CLAUSE (i)'s RATE.
THE DERIVATION ACT'S CONFIRMATION IS NOW RECOMMENDED TO THE AUTHOR. M-2…M-5 OPEN. `h2` STANDS
EXACTLY WHERE THE DEPOSIT LEFT IT. NOTHING DEPOSITS. LOCKS LAST.**
