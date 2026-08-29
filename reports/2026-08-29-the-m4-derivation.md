# THE M-4 DERIVATION — b250, 2026-08-29

**Scope:** a **derivation at content** with a Core shadow at the audit bar. The statement proved is
b247's, unchanged, in its harder (ii) form. **CONCURRENCY: SOLO.** A finite-place-set object at a
finite cutoff decides NOTHING global (b14/b15). Nothing deposits.

---

## The theorem, and its grade in the same breath

> **At fixed `c = 2π`:** the concentration eigenvalues satisfy `μ_N = O((c^N/N!)²)`; the endpoint
> weights satisfy the **exact identity** `Σ_n λ(n)²ξ_n(1)² = 2`; and the trace series `Σ_n t(n)`
> **converges**, with the explicit tail envelope `Σ_{n>N} t(n) ≤ (2 − S_N)/(1 − β_N)`, valid for
> every `N ≥ 6`.

### **GRADE: DERIVES-on-IMP, on four named foundational imports — and the ferry's best-case target
of "zero imports" is NOT met.** Plancherel, the identity theorem, Schmidt/Eckart–Young, Mercer.
**All TRUSTED-AT-CITE. *None* tooled** — the act looked for the tool and there is none: the
residence tree carries **no Mathlib**, verified twice (a filesystem search, then `Nat.factorial`
failing to resolve when the shadow was compiled). **IMP-3 (Landau–Widom) is not used and is not
needed**; b243's refusal of it at fixed `c` stands.

**And the limit, stated here rather than at the end:** M-4 pays **one term** of a shortfall whose
second object b246/b248 showed is not M-4's. **M-2, M-3, M-5 untouched. `h2` untouched.**

---

## The six steps

| step | | verdict | imports |
|---|---|---|---|
| **S0** | the series identity | **DERIVES** | none |
| **S1** | `λ_n < 1` strictly | DERIVES-on-IMP | Plancherel; identity thm |
| **S2** | the decay | DERIVES-on-IMP | Schmidt/Eckart–Young |
| **S3a** | per-mode endpoint bound | ### **HALTS — NOT DERIVED** | `W-ORD-XI-PERMODE` |
| **S3b** | the summed identity | DERIVES-on-IMP | Mercer |
| **S4** | the envelope | **DERIVES** | none beyond the above |

### S0 — the two names are one object *by derivation*

`qeps_layer`'s docstring **asserts** the collapse. **An assertion that a derivation exists is not
the derivation**, so it is reproduced: differentiating the supplied (85) at `ρ = 1⁺`, the `ρ^{-1/2}`
term and the integrand term both vanish because the range is empty, and **the moving lower limit is
the only surviving Leibniz term** — giving `ε′(1⁺) = Σ_n t(n)`. ### **b247's double-name hazard is
answered the only way it may be: definition against definition, not resemblance.** The reproduction
is checked against its source at their one common point (`ε(1) = 0`) before being differentiated.

### S1 — and a registered prediction of mine that was wrong

`Q = A*A`; `‖Aψ‖ = ‖ψ‖` forces `ψ` band-limited by Plancherel; band-limited plus compactly supported
makes `ψ` an entire function vanishing on `(1,∞)`, hence zero — contradiction. ### **My registration
said "S1 — I EXPECT DERIVES, LONGHAND AND ON ZERO IMPORTS." The longhand is there; the zero is
not.** Two textbook theorems carry it, and under the import bar there is no third category. **The
prediction is reported wrong rather than redefined.**

### S2 — the route improved on the one registered, and is reported as an improvement

The registered route (Jacobi–Anger + the Bessel factorial bound) **costs an import**. The
**exponential's own Taylor series costs none**: the two rank-one factors are elementary integrals of
powers, giving `μ_N ≤ T(N)²` with `T(N) = Σ_{m≥N} (2/(2m+1))c^m/m!`. ### **The theorem rests on the
zero-import bound; Jacobi–Anger only sharpens the constant.**

**The registered range held.** Section (C) banked `k ≥ 9` **before anything was computed** — the
Bessel bound needs `z²/4 < k + 3/2`, i.e. `k > π² − 3/2 = 8.3696…`. The computation returned exactly
`k ≥ 9`. *A range condition predicted before the fact is a prediction; the same range noticed after
would have been bookkeeping.*

**The join overlaps at `k = 9,10` rather than merely abutting — and it is not load-bearing, which is
the part worth saying.** Lemma F.1 is a **truncation certificate, not a tail bound**, so the join is
of certificates of *different species*. **The decay claim uses route (a) alone, which is valid at
every `N` with no range condition whatever.**

### S3 — a halt, predicted in advance, and a find, also registered in advance

**(a) HALTS.** The per-mode polynomial bound on `ξ_n(1)²` needs the Bouwkamp Legendre-coefficient
decay, not at content; both obvious routes go **inverse in `μ_n`**, as b247 already measured.
`W-ORD-XI-PERMODE` filed. ### **The halt was registered before it happened** — *"I EXPECT THE
NAVIGATOR'S ROUTE TO RESIST, AND I SAY SO IN ADVANCE."* **A halt predicted in advance is evidence; a
halt discovered and then declared expected would be nothing.**

**(b) DERIVES, and it re-derives one of the corpus's own pins as a theorem.** Mercer at the two
corners, with the parity `ψ_n(−1) = (−1)ⁿψ_n(1)` **derived from the kernel's own symmetry** rather
than assumed:

> **`Σ_n λ(n)²ξ_n(1)² = c/π + sin(2c)/(2π)`, which at `c = 2π` is EXACTLY 2.**

### **That is the corpus's own banked C0 gate — a pin carried as a *measured number* since b35 — now
a theorem with a proof.** And its `c`-dependence is stated rather than hidden: **the clean `2` needs
`sin(2c) = 0` and is not generic.** The registration fixed the falsifier — *anything but exactly 2
and the route is wrong* — and the control returns `|Σ − 2| = 7.2152e−40`. **The falsifier did not
fire.**

**What (b) does not replace.** S4 needs the sum, not the per-mode bound, so **clause (ii)'s harder
form becomes *unnecessary* rather than *proven*.** ### **S3(a) still halts. The theorem routes around
it; it does not answer it** — and the price is paid in full at S4.

---

## S4 — two envelopes, and the difference is not blurred

- **(FREE)** `Σ_{n>N} t(n) ≤ 2/(1−β_N)` — **measurement-free end to end.** It proves convergence.
  ### **But it does not tend to zero.**
- **(SHARP)** `Σ_{n>N} t(n) ≤ (2 − S_N)/(1−β_N)` — **tends to zero.** Its formula is exact and
  contains no measured quantity; `S_N` is a finite sum of exactly defined terms. **What the
  instrument supplies is its *evaluation*, not its *definition*.**

### **The price of S3(a)'s halt is exactly here:** an envelope both measurement-free *and* tending to
zero would need the per-mode bound S3(a) could not prove. **The halt is not cosmetic, and its cost is
named where it lands.**

| `N` | sharp (0-import) | sharp (1 import) | meas-free (0-imp) | measured tail | holds? |
|--:|--:|--:|--:|--:|--:|
| **6** | **1.15757629e−14** | 1.11558906e−14 | 2.07527387 | 1.11558894e−14 | yes |
| 8 | 9.91250843e−23 | 9.91242848e−23 | 2.00001613 | 9.91242848e−23 | yes |
| 10 | 1.46013869e−31 | 1.46013869e−31 | 2.0 | 1.4601387e−31 | yes |
| 11 | 3.1837636e−36 | 3.1837636e−36 | 2.0 | 3.18448512e−36 | yes |

**The measured column is a CONTROL. No line of the derivation would change if it were deleted.**

### **The range condition first holds at exactly `N = 6`, which is K1's cut.** Both are set by the
same `c` — **not luck, and not claimed as insight** — but it means the record's existing cut needs no
adjustment. And at that cut the envelope is **tight to about 4%, not loose by orders**, in contrast
to S2's bounds, which are loose by many orders and are **printed that way**.

---

## The amendment the act owed the record

**The K1 bar's "unbounded tail" sentences are amended wherever the record carries them — three
reports — with the originals intact, not deleted, not rewritten, not backdated.** Each amendment
says the original **stands as written and was true when written**: b242 derived an envelope and
refused it, and refusing an unproved envelope was correct.

### **`bar_L`'s amber does NOT clear.** It was amber for **two** reasons and only **one** is paid:
the bar still reports **seven computable modes against a definition of eleven**, a bench-precision
fact b249 measured and this act did not remove.

### **And the W-UNION `(nonArchimedean, unbounded)` quadrant is a DIFFERENT OBJECT and was
deliberately not amended** — the record carries "unbounded" in that second, unrelated sense across a
dozen reports, and matching on the bare word would have amended them. **The tool matches on full
sentences.** Gate 12 is a **positive control on that absence**: the phrase is shown *findable* first,
so its want of an amendment means something.

---

## Gates — 14 of 14 CLEAN on the second run, and both first-run failures are disclosed

**They failed in opposite directions, which is the only reason both are worth reporting.**

1. **A real defect in the artefact.** The controls file did not carry the sentence declaring its
   measurements non-premises — the sentence lived only in the *tool's* docstring, not in the emitted
   file a reader sees. ### **The artefact was fixed, not the gate.** Re-running the deterministic
   emitter changed **exactly 4 lines**; the bank was then re-written **last** so the ordering
   reflects reality and **no mtime was forged** (b247's precedent), with **zero changed lines**
   proved by diff.
2. **A defect in the gate.** It hunted the substring `error` in the axiom profile and matched the
   profile's own line for the theorem `deep_cuts_need_the_evaluation_error` — ### **a legitimate name
   containing the word the gate was hunting.** A substring test against free text was never the
   criterion. **The gate was narrowed to Lean's real diagnostic form, not relaxed**; `sorryAx` and
   `Classical.choice` stay exact.

**The tautology control is the gate this act most needed**, and it has two halves: a fabricated tail
one order larger than the envelope **must fail** the same comparison, and the real `N = 11` row
**must fail without the evaluation tolerance**. Both do. ### **That is the arithmetic proof that the
tolerance is load-bearing and not padding added for comfort.**

**Scope wall** matched on code only, with the `ast` stripper b242 was forced into, b243/b246 carried,
and **b248 forgot at its fourth matcher**. This is the fifth matcher and it starts with the stripper.

Term scan **CLEAN, 0 live over 1466 lines.**

### A fourth consecutive print-floor — and this time it was the act's own evaluation

The envelope control **failed at `N = 10, 11` by `7.2e−40`** — **exactly** the deviation of the
instrument's 13-term Mercer sum from the exact `2`. At those depths the tail and the arithmetic error
are the same size, so a finer comparison **tests the arithmetic, not the theorem**. The tolerance is
that measured deviation, **computed and not chosen**. b245 met b38's four decimals; b246 floored at
5e−5; b249 met b242's ten digits. ### **`W-ORD-TE-SPEC`'s pending extension is demonstrated a fourth
time.**

---

## The Core shadow — and what it refuses to carry

`Core/M4EnvelopeShadow.lean`, vanilla Lean 4, `decide` only. ### **The profile is PRINTED AND READ,
never inferred from an exit code** (b227 shipped a file that compiled clean and printed `sorryAx`):

```
'M4EnvelopeShadow.factorial_dominates_geometric'        does not depend on any axioms
'M4EnvelopeShadow.factorial_does_not_dominate_before'   does not depend on any axioms
'M4EnvelopeShadow.envelope_holds_at_cuts'               does not depend on any axioms
'M4EnvelopeShadow.deep_cuts_need_the_evaluation_error'  does not depend on any axioms
'M4EnvelopeShadow.minimax_instances'                    does not depend on any axioms
'M4EnvelopeShadow.range_condition_holds_at_six'         does not depend on any axioms
'M4EnvelopeShadow.range_condition_fails_at_four'        does not depend on any axioms
```

**7 of 7.** It carries **four polarity controls**: that the factorial ratio turns at `m = 6` and
**not before**; that the two deep cuts **genuinely need** the evaluation-error term; and that the
range condition **excludes `N = 4`**. ### **Without those, every theorem above them would be
consistent with "always true".**

### **The shadow does not carry the theorem, and says so in its own header.** Plancherel, Mercer, the
identity theorem and the operator itself are **not in it**. **A shadow that appeared to carry them
would be a lie in Lean**, and the analytic steps are not forced into vanilla `Nat`.

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : check_harness
  act       : b250
  run at    : 2026-08-29T13:11:15 (local)
  input     : 14 checks routed through the harness
  checks    : 14
  pass      : 14
  fail      : 0
  error     : 0
  refused   : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 e81bb66e3836f9a8bea76e3a165d31ab
=== END AUDIT SIDECAR ===
```

---

## Filings

- **Index:** `m4-derivation` and `s2-decay-route` keyed on filing, both queried **NO KEY** before any
  step ran. A **second `rule-modes` row** amends the K1 tail rows rather than rewriting them (b244's
  precedent, where a second `q-orientation` row was added instead of an edit).
- **`W-ORD-XI-PERMODE`** filed — the per-mode polynomial bound on `ξ_n(1)²`, S3(a)'s halt.
- **`W-ORD-TE-SPEC`** extension demonstrated a fourth time.
- **The thirty-seventh seam's debt restated:** term 2's formalization stands, **unpaid and
  untouched**. This act did not go near it.
- **In flight:** M-2…M-5 open, **none closed by this act**. `W-ORD-XI-PERMODE`,
  `W-ORD-ORDINATE-CACHE`, `W-ORD-STAGING-GUARD`, `W-ORD-FILE-E-WORKING-COPY-STALE`,
  `W-ORD-TE-SPEC` open. **`W-ORD-MODE-PRECISION` discharged at b249.**
- **HANDOFF** brought current by demotion, prior content kept, read-back identical.

### The fork at this stop

1. **The third face-off, with M-4 now paid and the junction piece naked.** `resid47` has a theorem
   behind it, so what remains of the shortfall is the archimedean piece **on a converged series**
   plus the junction piece — which names **M-2** again.
2. **The patent session**, which slots here on your word and needs nothing from this act.
3. **M-2, M-3, M-5** as the remaining engine items.

---

### **ONE THEOREM PROVED AT CONTENT, GRADED DERIVES-on-IMP ON FOUR NAMED IMPORTS AND NOT ON ZERO.
S3(a) HALTS AND IS REPORTED AS HALTING. THE CORPUS'S C0 PIN IS NOW A THEOREM. M-4 PAYS *ONE TERM* OF
THE SHORTFALL AND NOT THE SHORTFALL. M-2…M-5 OPEN. `h2` STANDS EXACTLY WHERE THE DEPOSIT LEFT IT.
NOTHING DEPOSITS. LOCKS LAST.**
