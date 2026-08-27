# b217 — THE CHECK HARNESS

**2026-08-27 · relay `reports/2026-08-27-check-harness.md`**
**Ferry part 1 of 1, receipt confirmed IN FULL. Registration `bcb2928`, banked before the tool.**
**Bank: `data/b217_check_harness.txt` · fixtures `data/b217_fixtures.txt` · retrofit `data/b217_retrofit.txt` · own checks `data/b217_own_checks.txt`.**

> *** ### **THE RULE, FILED: NO ONE-LINE CHECK IS READ UNTIL IT HAS FAILED ON A FIXTURE IN THE
> SAME RUN.** ### **A check that has not been seen to fail has not been seen to work.** ***
>
> ### **And the retrofit changed the tool — which is what a retrofit is for.**

## COMPONENT 1 — THE TOOL (P1)

`relay/tools/check_harness.py`. The fixture runs **first**, and the check is **not run at all** if
the fixture passes. It **asserts its cwd is the declared repo root** (b209's wrong-repo push and
b216's wrong-cwd loop are one species, and this is where it dies). An exception is a **loud ERROR**,
printed whole. A non-bool return is an ERROR. ### **An empty stdout is a FAIL, not a pass** — that
one line is b216's instance. It emits its own audit block.

**Fixtures on the harness itself, both polarities: 12 of 12.** Including the case the ferry named —
**a fixture that wrongly passes, where the harness must REFUSE** — plus errored fixtures, a raising
check, a non-bool check, the empty-stdout case, and the cwd assertion tested by violating it.

> ### **The counts are the harness behaving correctly, not a clean run:** 3 pass, 2 fail, 2 error,
> 4 refused. ### **A harness fixture suite that reports all-pass has not tested the refusal path,
> which is the only path that matters.**

## COMPONENT 2 — THE RETROFIT (P2), AND IT OVERTURNED THE DESIGN

**Three of three reproduced, with their original numbers:**

| instance | reproduced | b213/b216 printed | truth |
|:--|:--|:--|:--|
| b213 fill count | **6** | 6 | 0 |
| b213 placed-file count | **1** | 1 | 0 |
| b216 query loop | **HIT = True** from the wrong cwd | HIT | NO KEY |

**Three of three caught — but not all by the guard the ferry specified.**

- **Instance 3** — a true false *pass* — is caught by the **must-fail fixture alone**. Under the
  harness the wrong-cwd check returns **ERROR**, not the silent pass it was.
- *** ### **Instances 1 and 2 sail straight through it.** Under the must-fail fixture they return
  FAIL — the wrong answer, but **licensed**. ### **The reason is exact: they are false ALARMS, not
  false passes.** Their checks report failure on a correct state *and* on a broken state.
  ### **Failing is all they can do, so a fixture that asks them to fail proves nothing about
  them.** ***

### **So the harness gained a second guard because the retrofit refused to confirm the design:** an
optional **WITNESS** — a state where the check must **PASS**. A check that cannot pass its own
witness has not been shown to discriminate, and is **REFUSED**. Under it, instances 1 and 2 are
refused and the check is not run. And instance 1's **corrected** version passes under both guards —
### **so the harness licenses good checks and refuses bad ones, which is the only test of a guard
that matters.**

> ### **The two guards are mirrors: the fixture proves the check can say NO, the witness proves it
> can say YES, and a check that cannot do both is not a check.**

**A correction to the brief's own wording:** it calls all three *"the three historical false
passes"*. ### **At content only one is.** The distinction is not pedantry — **it is the reason the
must-fail fixture alone would have caught one of three.**

## COMPONENT 3 — THE FILINGS (P3)

The rule is filed as a **dated field** in the loom, in the same form as the audit-authorship
convention. ### **No new document.** The field carries the four founding instances (b142, b213 ×2,
b216), the common shape, the retrofit's discovery, and the reach.

**The reach, filed with it.** ### **It closes:** a check read as passing when it never ran; a check
that cannot discriminate in either direction; a check run from the wrong directory. ### **It does
not close:** a fixture that fails *for the wrong reason* — the harness checks that the fixture
failed, **not why**, and no tool can; a one-liner typed straight into a shell; and **wrong scope,
which is b142's own lesson and remains its own.**

**This act's own checks, run under the harness as the EXECUTION line required: 4 of 4 PASS**, each
with a must-fail fixture *and* a must-pass witness.

> *** ### **And an honest note on those four, because the tool's own header invites it:** three of
> the four fixtures are the same trivial shape (`must_contain='### never'`), which fails for a
> reason unrelated to what the check measures. ### **That is exactly limit (1) in the tool's
> header — and I hit it on the tool's first day of service.** The checks are still better guarded
> than they would have been unguarded, ***and that is the most that should be claimed.*** ***

## THE AUDIT SIDECARS (emitted; copied from the sidecar files)

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : check_harness
  act       : b217-retrofit
  run at    : 2026-08-27T15:27:36 (local)
  input     : 7 checks routed through the harness
  checks    : 7
  pass      : 2
  fail      : 2
  error     : 1
  refused   : 2
  VERDICT   : NOT CLEAN
  self-hash : sha256/32 666eb820195e57f2688d7c3af932e26d
=== END AUDIT SIDECAR ===
```

> ### **That `NOT CLEAN` is correct and is the point:** the retrofit deliberately routes broken
> checks through the harness, so the fails, the error and the refusals **are** the deliverable.

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : check_harness
  act       : b217-own
  run at    : 2026-08-27T15:29:46 (local)
  input     : 4 checks routed through the harness
  checks    : 4
  pass      : 4
  fail      : 0
  error     : 0
  refused   : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 25932b2808be59885319826ad928a54c
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b217-docs
  run at    : 2026-08-27T15:28:29 (local)
  input     : added lines in D:/MY-DOwnloads/PLACE-papers vs HEAD
  stems     : gap, blind
  files     : 1
  lines     : 12
  hits      : 0
  live uses : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 37f4ffa8a3fdfaab548b79bf1799df50
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : commit_selfcheck
  act       : b217-docs
  run at    : 2026-08-27T15:28:58 (local)
  input     : D:/MY-DOwnloads/PLACE-papers
  input     : HEAD
  written   : 1
  foreign   : 0
  ro-claim  : none
  compliance : none
  VERDICT   : CLEAN
  self-hash : sha256/32 10dd98d44a71bed59fe0730595e2f2df
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : mirror_verify
  act       : b217
  run at    : 2026-08-27T15:29:13 (local)
  input     : mirror-refresh-2026-08-27.zip
  files     : 40
  rows      : 40
  mismatch  : 0
  declared  : 2702d0a
  ls-remote : 2702d0a5b3b3
  VERDICT   : CLEAN ON ALL THREE CLAUSES
  self-hash : sha256/32 dad780c7efbed495b4516de387e3ee85
=== END AUDIT SIDECAR ===
```

## PINS

| repo | pin | note |
|:--|:--|:--|
| **PLACE-papers** | `aee890a` → ### **`2702d0a`** | the dated field only; hook CLEAN, 0 foreign; **1 file changed, no file created** |
| relay | `bcb2928` → the b217 pin-line commit | the tool + three data files |
| SIDE-global-section | `356010f` — **UNMOVED** | no build |
| SIDE-kernel | `0256e9e` — **UNMOVED** | — |
| mirror | rebuilt at `2702d0a`, **CLEAN ON ALL THREE CLAUSES**, roster unchanged | — |
| HELD | `6eada6a` — LOCAL-ONLY, untouched | — |

**DEVIATIONS:** none.
**DIVERGENCES:** one, with the ferry's wording — *"the three historical false passes"*; **at content
only one is a false pass**, and that distinction is why the tool now has two guards.
