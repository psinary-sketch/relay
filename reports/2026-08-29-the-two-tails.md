# THE TWO TAILS — b246, 2026-08-29

**Scope:** a bounded bench act on banked per-mode data plus one derivation-by-quotation.
### **b245's branch is not revised** — a banked rule is not re-verdicted because a later act
explains it; this was a new question under its own registration. No face-off was run and no column
recomputed. A finite-place-set object at a finite cell decides NOTHING global (b14/b15). Nothing
deposits.

---

## The verdict: **(TWO OBJECTS)** — and it fails wide, not narrowly

The question: are `resid47` and `D_dict` the even- and odd-sector tails of **one** mode series?

| test | band | result |
|:--|:--|:--|
| **T-1** identity | 5e−5 floor | ### **FAIL** — by 1.76 … 2.62 |
| **T-2** recomposition | 5e−5 floor | ### **FAIL** — by 0.43 … 1.22 |
| **T-3** the ratio | [1.673, 1.785] | ### **FAIL** — 4.35 … 5.85 |
| **T-4** cell-profile | monotone, max/min ≤ 1.5 | ### **FAIL** — not monotone |
| **T-5** (executor's own) | 1e−3 | ### **FAIL** — at five of six cells |

### **The two terms stay separately owned. M-4 covers `resid47` and not the other term, and the
sentence *"paying M-4 pays the whole bench shortfall"* may not be written.**

**Both seats' expectations were registered and both are reported.** The navigator's was
**(ONE OBJECT)** — not borne out. The executor's was **(TWO OBJECTS)**, *"and I expect it to fail
wide, not narrowly"* — borne out, and **for the reason banked before the run**: *"b242 measured the
ε per-mode series converged by mode 6 while the trace series was still at 0.257 at mode 6. The two
series do not have comparable tails."*

---

## Why the answer is two — structurally, not just by the bands

- `resid47` = `Tr_full(7) − A − E2full` — a shortfall of the **trace** series, which b242 measured
  **still at 0.257 at mode 6** and not converging.
- `−D_dict` = `2·E2 − Δ₋ + PR − Θ_q` = ### **`E2full + E2even + (PR − Θ_q)`** — sector arithmetic
  on the **ε** series, plus the finite-place pairing.

And the ε series is **converged by mode 6**: its per-mode terms fall 8.17e−01, 6.74e−01, 1.85e−01,
4.04e−03, 1.35e−05, 1.56e−08, 7.90e−12, then **3.90e−16**.

### **So `−D_dict` is not a tail of anything. It is a sector combination of a converged series, and
a converged series has no tail.** The measured ε tail beyond K1 is **1e−18 to 5e−13 — fifteen orders
below `D_dict`.** That is read off the printed `(R2)` columns, not asserted.

**Three readings were registered in advance**, not one, so the one-object hypothesis got its best
shot and no reading could be promoted after its numbers were seen: (R1) the trace tail beyond K1 —
**primary**; (R2) the ε tail beyond K1; (R3) the full ε sectors.

### The near-miss — reported as a miss

(R3) gives T-3 ratios **1.676, 1.665, 1.647, 1.599, 1.591, 1.572** against the band [1.673, 1.785]:
### **inside at `a² = 2` and nowhere else**, drifting 12% low by `a² = 12`. The coincidence is
explained rather than left to be guessed: **at `a² = 2` both `PR` and `Θ_q` vanish**, so
`(L−R)/resid47` and `E2full/E2even` are two different quantities that happen to fall within 0.2% of
each other — **and they diverge as soon as the finite places turn on.** (R3) is an **alternate** and
may not be promoted to primary after its numbers are seen.

---

## The one clean cross-check of this arc — and it passed

`D_dict` computed **independently** from b242's per-mode arrays by parity, against b38's banked
`D_dictated` column of 2026-08-18:

| `a²` | computed today | b38 banked (2026-08-18) |
|:--|--:|--:|
| 2 | −2.681241965 | −2.681242 |
| 12 | −1.790997295 | −1.790997 |

### **Agreement at every cell to ~1e−6, which is b38's printed precision** — an eleven-day-old bank,
a different code path. ### **That is the cross-check b245's T-E was trying to be**, and it worked
here for one reason: **the axes were matched and printed before any number was compared** —
`W-ORD-TE-SPEC` honoured in form. The b38/K1 mismatch (NMODE 10 against 7) was named in the run's
own header rather than discovered in a diagnostic afterwards.

**The double name was computed and kept apart, not chosen between:** `Dneg_raw` (the raw odd-trace
slice, `b36_act8.py:172`) runs 1.617848 → 0.693004; `Δ₋` (the odd ε mask, §17/§19's definition) runs
0.677615 → 0.354973. The ferry's *"(raw odd slice − masked odd series)"* is reported under its own
name **`SECTOR_SPLIT_DIFF`**, because ### **it is not `D_dict`, and calling it so would be the
double-name species b241 caught.**

---

## T-5 — both halves

Registered because it was noticed while reading, and **a finding that arrives before the
registration belongs in the registration**: `|resid47 + 2A| ≤ 1e−3`. It holds at `a² = 2`
(2.53e−04) and **fails at all five others** by ~0.5. The registration said *"I expect it to fail at
the larger cells, because nothing I know makes it a law."* ### **It was worth registering precisely
so it could be killed in public rather than remembered as a hunch.**

---

## The miss of this act's own — and the tautology gate caught it

### **The definitions file declares the shortfall identity as `resid47 + D_dict = L − R`. That is
false; the true identity is `resid47 − D_dict = L − R`:**

```
resid47 − D_dict = (Tr − A − E2) − [(Θq − PR) + (Δ₋ − 2·E2)]
                 = (Tr + E2 − Δ₋ − Θq) − (A − PR)  =  L − R
```

The tautology control tested the `+` form on 400 random tuples, it did not hold, and **the gate
failed** — ### **the first time in this arc a harness caught a defect in a *claim* rather than in a
*string*.** ### **The banked definitions file is not edited** — b244's precedent governs: *"editing
a banked registration to match what the act later did is the precise species this corpus guards
against."* The error is disclosed in the bank and the correction written into the gate's own
docstring.

### **It changes no verdict**, said plainly rather than left to be assumed: T-2 was implemented
exactly as the **ferry** worded it (`resid47 + D_dict`), and under **both** signs the test fails
wide — 1.30 vs 0.08 with `+`, 6.66 vs 0.08 with the true `−`.

---

## Filings

**The five-term ledger does not collapse.** `E2` is now shown to sit on a **converged** series and
has no tail to be anyone's; `resid47` is separately owned on the trace series; `Δ₋` and `Θ_q` stay
ruled (b244); `PR` stands. ### **M-4's scope is narrowed by measurement: it covers `resid47` and not
`−D_dict`.**

**The b247 route note — filed, not run.** `b247 — THE M-4 STATEMENT AND ROUTE`, asset list
**started and not verified**: act 15's derived pair geometry (File E's own owner line cites it); the
Wronskian norm-slope identity (indexed, grade **DERIVED AT CONTENT on named imports, not a proof
from nothing**); b242's measured decay; Lemma F.1; and ### **Slepian–Widom decay as candidate IMP-3
under the import bar, verified-where-tooled only — nothing in this corpus has read it at content
and this act does not pretend otherwise.** ### **That is a list of named assets, not a route.**

**In flight:** M-2…M-5 open, none closed. `W-ORD-MODE-PRECISION`, `W-ORD-ORDINATE-CACHE`,
`W-ORD-STAGING-GUARD`, `W-ORD-FILE-E-WORKING-COPY-STALE`, `W-ORD-TE-SPEC` open — the last
**honoured in form here but still open as a tool**, since being obeyed once by hand is not the same
as being in the command path (b179's lesson). The thirty-seventh seam's debt restated: four items,
the file **open**, the lemma **open**, the toolchain **discharged**, the ledger's statement
**complete at cell level** — unpaid and untouched.

---

## Gates

**15 of 15 PASS, CLEAN** — on the second run, the first having caught the sign error above. Every
fixture is annotated with **why it fails**, and none is `not check`: an absent hash rather than a
reversed mtime; a real file's real imports rather than a negated absence; the trace tail (non-zero)
rather than the ε tail (machine zero). **Gate 9 is a positive control on an absence** — the
forbidden sentence is shown *findable* in the definitions file, so its absence from the bank means
something.

Term scans **CLEAN**, 0 live over 1267 lines. **PLACE-papers, the loom and the mirror were not
touched**, so the hook did not run and no mirror rebuild was required.

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : check_harness
  act       : b246
  run at    : 2026-08-29T11:41:59 (local)
  input     : 15 checks routed through the harness
  checks    : 15
  pass      : 15
  fail      : 0
  error     : 0
  refused   : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 0c2f9b124a2d96a89101eead53c7980f
=== END AUDIT SIDECAR ===
```

---

### **THE BENCH SHORTFALL IS TWO OBJECTS ON TWO SERIES, BY MEASUREMENT. M-4 COVERS ONE OF THEM.
b245's BRANCH UNREVISED. M-2…M-5 OPEN. THE AUTHOR'S FORK AT THIS STOP: THE PATENT SESSION, WHICH
SLOTS HERE ON YOUR WORD AND NEEDS NOTHING FROM THIS ACT; b247 (M-4's STATEMENT AND ROUTE); AND
`W-ORD-MODE-PRECISION` (K3). `h2` STANDS EXACTLY WHERE THE DEPOSIT LEFT IT. NOTHING DEPOSITS.
LOCKS LAST.**
