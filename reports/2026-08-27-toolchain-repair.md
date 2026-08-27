# b218 — THE TOOLCHAIN REPAIR

**2026-08-27 · relay `reports/2026-08-27-toolchain-repair.md`**
**Ferry part 1 of 1, receipt confirmed IN FULL. Registration `50ef731`, banked after the survey and before the repair.**
**Bank: `data/b218_toolchain_repair.txt` · gates `data/b218_gates.txt` · print `data/b218_interfaces_print.txt`.**

> *** ### **BRANCH (RESTORED). The Interfaces layer compiles at the repo's OWN pin (v4.29.1) and
> all 29 of 29 banked profiles are reproduced EXACTLY.** ### **Core prints 366/366 byte-identically
> before and after. THE PIN WAS NOT MOVED AND NOT ONE REPOSITORY FILE WAS CHANGED.** ***
>
> ### **And my registered expectation of (HALT) was wrong.**

## COMPONENT 1 — THE SURVEY (P1), BEFORE ANYTHING WAS FETCHED

### *** THE FINDING THAT RESHAPED THE ACT ***

`SIDE-global-section` has **no `lakefile`, no `lake-manifest.json`, no `.lake`**. ### **It has never
been a lake package** — it pins a Lean *toolchain* and declares **no Mathlib dependency at all**.
Its siblings `SIDE-archimedean` and `SIDE-kernel` carry all three.

### **So the ferry's clause (a) names two artifacts that do not exist, and clause (c)'s *"the
equivalent the manifest names"* has no manifest. That, and not a missing cache, is why b215 found
the layer uncompilable.**

**The Mathlib trees, read for what they hold** — ### **none fully built when the act began:**

| tree | head | toolchain |
|:--|:--|:--|
| `/d/mathlib4` | `cecd0c4d56` | v4.30.0-rc1 |
| `/d/mathlib4-e960b84-tmp` | `e960b84129` | v4.29.0-rc8 |
| ### **`SIDE-archimedean/.lake/packages/mathlib`** | **`5e932f97dd`** | ### **v4.29.1 — the repo's own pin** |
| `/d/mathlib-cache` | — | **104,092 `.ltar` files** |

**The federation snapshot, superseding 2026-08-04.** 43 `SIDE-*` + 2 `PLACE-*`, all on `main`, all
clean. ### **A three-way split: ~28 on `v4.29.0-rc8`, 10 on `v4.29.1`, 2 on `v4.30.0-rc2`.** All but
three carry a tag. *The ferry is right that pins move — and they have moved apart.*

### *** TWO CORRECTIONS I MADE TO MYSELF INSIDE THE SURVEY ***

**(i)** I concluded *"Mathlib has never pinned v4.29.1"* from `/d/mathlib4`'s toolchain history
alone. ### **Wrong** — a v4.29.1 checkout exists, vendored in a sibling. ***One clone is not the
project, and a survey that reads one tree has surveyed one tree.***

**(ii)** A one-line probe of the form `[ -f a ] || [ -f b ] && echo yes || echo NO` groups wrongly
and reported **`lakefile=yes manifest=yes` for a repo with neither**. ### **That is b217's species,
on the day after the rule was filed, in the act whose own clause (e) requires the harness.** Caught
because the next check contradicted it; facts re-established one check at a time.
***The rule is one day old and the habit is older.***

## COMPONENT 2 — THE REPAIR AND THE GATES (P2)

**The path taken needed no new pin and no repo file.** I verified **first** that the sibling's
`.lake/` is gitignored with zero tracked files and a clean worktree — so populating it touches
nothing tracked. Then `lake exe cache get` at `MATHLIB_CACHE_DIR=D:\mathlib-cache`:
### **"No files to download … Completed successfully!"** — the local cache held everything. Then the
17 imports fetched **by name, enumerated from the files themselves**, and the layer compiled by
`LEAN_PATH`. ### **No checkout of `/d/mathlib4`'s newer head was made, as clause (c) forbids.**

| gate | verdict |
|:--|:--|
| **G-CORE** | ### **PASS** — 366/366, **byte-identical** to the bank *and* before-vs-after |
| **G-BUILD** | ### **PASS** — all six Interfaces files compile at v4.29.1 |
| **G-PROFILE** | ### **PASS** — **29 printed, 29 banked, zero missing, zero extra, zero differences** |

### **Not one profile rounded — including the four `[propext]`-only terminals of `LocalLimit`, which
are exactly the rows a rounding would have flattened into the three-axiom majority.**

> *** ### **And one failure that was my tool choice, not the object:** the first G-BUILD ran from
> Git Bash and every file returned *"unknown module prefix 'Mathlib'"*. ### **`LEAN_PATH` with
> Windows paths and `;` does not survive Git Bash's path mangling.** From PowerShell the same
> command compiled and printed. ### **Recorded because it looked exactly like b215's finding and
> was not it — and because it errored loudly rather than passing silently, which is why it cost
> minutes and not an act.** ***

**(e) Every gate under the b217 harness**, with a must-fail fixture **and** a must-pass witness:
### **5 checks, 5 pass, 0 fail, 0 error, 0 refused** — G-CORE, G-BUILD, G-PROFILE, pin-unmoved,
repo-untouched. *The harness's first service on an act that is not its own.*

## COMPONENT 3 — THE PRINTS AND THE FILINGS (P3)

The federation snapshot is filed as a **dated field** in the loom, superseding 2026-08-04.

**b215's DEBT 3 — the toolchain — is DISCHARGED as a blocker to printing.** A claimed compile can
now be reported from its own printed axiom profile for an Interfaces-grade construction.

*** ### **And the discharge is narrow and says so: the build is reproducible ONLY with that
external `LEAN_PATH`. The repo still declares nothing, and a fresh clone still cannot build its own
Interfaces layer.** A smaller item replaces the old one — give the repo a lakefile and a manifest as
its siblings have — ### **a structural change with its own Provenance, not made here, wanting a
ruling.** ***

**Term 2's other two debts are untouched:** the **file** (blocked on the aggregation) and the
**lemma** (`ClassRichness`, citation unread, in two parts). ### **Term 2 is now blocked by two
things rather than three.**

## THE AUDIT SIDECARS (emitted; copied from the sidecar files)

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : check_harness
  act       : b218
  run at    : 2026-08-27T16:18:02 (local)
  input     : 5 checks routed through the harness
  checks    : 5
  pass      : 5
  fail      : 0
  error     : 0
  refused   : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 f11d86d70fe1ffef99b0040551ad767e
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b218-docs
  run at    : 2026-08-27T16:18:39 (local)
  input     : added lines in D:/MY-DOwnloads/PLACE-papers vs HEAD
  stems     : gap, blind
  files     : 1
  lines     : 29
  hits      : 0
  live uses : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 c6b6ade3044663700c80a85f51de92a7
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : commit_selfcheck
  act       : b218-docs
  run at    : 2026-08-27T16:19:19 (local)
  input     : D:/MY-DOwnloads/PLACE-papers
  input     : HEAD
  written   : 1
  foreign   : 0
  ro-claim  : none
  compliance : none
  VERDICT   : CLEAN
  self-hash : sha256/32 b1b8de10c027538380e8119189735bb3
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : mirror_verify
  act       : b218
  run at    : 2026-08-27T16:19:33 (local)
  input     : mirror-refresh-2026-08-27.zip
  files     : 40
  rows      : 40
  mismatch  : 0
  declared  : 5f1ce35
  ls-remote : 5f1ce35782db
  VERDICT   : CLEAN ON ALL THREE CLAUSES
  self-hash : sha256/32 bed62e0020b97dce813a958da0b16fc1
=== END AUDIT SIDECAR ===
```

## PINS

| repo | pin | note |
|:--|:--|:--|
| **PLACE-papers** | `2702d0a` → ### **`5f1ce35`** | the federation field + the register; hook CLEAN |
| relay | `50ef731` → the b218 pin-line commit | bank, gates, print |
| **SIDE-global-section** | `356010f` — ### **UNMOVED, and the pin unmoved** | *no file changed; worktree 0 entries* |
| SIDE-kernel | `0256e9e` — UNMOVED | — |
| mirror | rebuilt at `5f1ce35`, **CLEAN ON ALL THREE CLAUSES** | — |
| HELD | `6eada6a` — LOCAL-ONLY, untouched | — |

**DEVIATIONS:** none — the three alternatives named at registration (add a lakefile, move the pin,
vendor the modules) were **all left untaken, as registered**, and the repair needed none.
**DIVERGENCES:** one, with clause (a) — it names a lakefile and manifest the repo does not have.
Named at registration and not worked around.
