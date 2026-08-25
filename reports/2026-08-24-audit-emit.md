# b153 — THE AUDIT EMIT ACT

**Registration `0e12bad`, banked before any component.** 2026-08-24.

> ### **AN AUDIT BLOCK IS WRITTEN BY THE TOOL, NOT ABOUT IT. HAND-TYPED
> ### VERDICTS ARE VIOLATIONS.** Minted this act at the conventions lines;
> founding instances **b146**, **b148**, **b151**.

---

## THE ACT'S OWN TEST, REGISTERED IN ADVANCE

The registration wrote, before a line of the tool existed:

> *"this act's own report must carry EMITTED blocks. ### **IF IT CARRIES A
> HAND-TYPED ONE, THE ACT HAS VIOLATED THE CONVENTION IT MINTS, IN THE ACT
> THAT MINTS IT** — which is precisely the b148 shape. The verifier is run
> against this act's own report before it ships."*

### **That sentence is the act in miniature.** b148's breach was not that a rule
was broken but that ### **the breaching act asserted its own compliance.** An act
that mints an authorship convention and then hand-types its own audit block
would be the same shape one level up — and ***the most quotable false pass in
the record***, because it would sit inside the very line forbidding it.

**So the blocks below were not written by me.** They were emitted by the tools
that ran, read off disk, and inserted verbatim by a script that types no verdict
of its own. ### **`tools/audit_verify.py` was run against this report before it
shipped, and its result is stated at the foot — including what it cannot see.**

---

## COMPONENT 1 — THE EMITTER AND THE VERIFIER

| file | what it is |
|:--|:--|
| `tools/audit_emit.py` | a tool that renders a verdict now writes its own block — tool, act, run timestamp, inputs, counts, verdict — and a **sha256/32 self-hash over the block's own body**; sidecar to `data/audit_<act>_<tool>.txt` |
| `tools/audit_verify.py` | reads a **report**, extracts every audit block, requires each to match a sidecar **byte-for-byte** with its self-hash intact |

`--emit` wired into `banned_terms.py`, `mirror_verify.py`, `commit_selfcheck.py`.
*(The wiring went through a **script file** after a heredoc replacement wrote
nothing — the standing fix for that escaping class, applied on sight rather than
after a second failure.)*

### **THE THREE VERDICTS ARE DIFFERENT AND ARE KEPT DIFFERENT:**

- **ORPHAN** — a block in a report matching no sidecar. ### **The b151 shape: a
  verdict no tool produced.** FAIL.
- **TAMPERED** — a block whose self-hash does not recompute. Emitted, then
  edited. FAIL.
- **UNUSED** — a sidecar emitted that no report embeds. ### **NOT a failure.** A
  check may be **run** without being **quoted**, and collapsing that into a
  failure would push the operator toward quoting everything — *which is how a
  report becomes unreadable and its audit blocks become scenery.*

---

## COMPONENT 2 — THE FIXTURES (the nursery convention: a check's first run is part of its construction)

```
 banned_terms.py     dirty exit 1 PASS | clean exit 0 PASS | empty exit 0 PASS
 commit_selfcheck.py 49cd156 exit 1 PASS | 084efbe exit 0 PASS | no-args exit 2 PASS
 mirror_verify.py    real exit 0 PASS | tampered exit 1 PASS | zero-row exit 2 PASS
 audit_verify.py     matched exit 0 PASS | edited->TAMPERED exit 1 PASS | no-blocks exit 0 PASS
  ### FIXTURES: ALL PASS
```

The known-dirty cases are **the record's own**: `49cd156` **is** the b148 breach
commit; `084efbe` **is** its correction. ### **The fixture is not a simulation of
the failure. It is the failure, kept.**

### **AND THE THREE ZEROES ARE DISTINGUISHED RATHER THAN CONFLATED:**

| the zero | the right answer | why |
|:--|:--|:--|
| an empty **file** | **CLEAN**, exit 0 | a real scope of zero lines |
| zero **probes** | **HARD FAILURE**, exit 2 | the verdict was vacuous (b152) |
| a report with no audit **block** | **CLEAN**, exit 0 | it claims nothing |

### **Three different zeroes, three different right answers.** A tool answering
all three the same way would be wrong twice whichever way it chose.

---

## COMPONENT 3 — THE CONVENTION MINTED

Filed at the conventions lines of `VERIFICATION_LOOM.md`, dated, with the
standing-laws annex row added. ### **The three founding instances are one hole
seen three times:**

- **b146** — a scanner **excused a live use** (the per-line exception window) and
  reported CLEAN.
- **b148** — a commit message **asserted its own compliance** in the act that
  breached the deconfliction ruling.
- **b151** — a report **claimed `VERDICT: CLEAN` for a review that was never
  run**, with the banned stem sitting in the text it certified.

### **In every one, the check and the thing checked were the same actor**, and
the record had no mechanism that could tell a **run** from a **claim**.

### **THE FIRST TWO WERE PATCHED AT THEIR SITES. THE THIRD COULD NOT BE**, because
the defect was in no tool: ### **a report's audit block is prose, and prose is
free.** ***The fix is not a better tool but a change of authorship*** — the block
moves from *written by the actor about the tool* to ### **written by the tool and
merely carried by the actor.** What was a **risk** becomes a **violation**, and a
violation is **detectable** where a risk is not: *an embedded block with no
matching sidecar is a fact about files, not a judgement about intent.*

---

## THE AUDITS — EMITTED, NOT TYPED

### **The vocabulary review** (Rule 3), scoped by this act's own diff:

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b153
  run at    : 2026-08-24T20:28:51 (local)
  input     : added lines in D:/MY-DOwnloads/PLACE-papers vs HEAD
  input     : whole file b153_registration_2026-08-24.txt (created this act)
  input     : whole file audit_emit.py (created this act)
  input     : whole file audit_verify.py (created this act)
  input     : EXCLUDED 0 lines whose path contains: patent-package   ### stated, never silent
  stems     : gap, blind
  files     : 4
  lines     : 260
  hits      : 0
  live uses : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 9699b1fe1a0c04aa799a216c461f45c3
=== END AUDIT SIDECAR ===
```

### **The commit self-description check** on the `PLACE-papers` commit:

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : commit_selfcheck
  act       : b153
  run at    : 2026-08-24T20:29:19 (local)
  input     : D:/MY-DOwnloads/PLACE-papers
  input     : (staged)
  written   : 1
  foreign   : 0
  ro-claim  : none
  compliance : none
  VERDICT   : CLEAN
  self-hash : sha256/32 a895085d0704cea84886b56b366e525b
=== END AUDIT SIDECAR ===
```

### **The mirror, both clauses of the stale-build law:**

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : mirror_verify
  act       : b153
  run at    : 2026-08-24T20:32:43 (local)
  input     : mirror-refresh-2026-08-24.zip
  files     : 31
  rows      : 31
  mismatch  : 0
  declared  : 781b8e2
  ls-remote : 781b8e27611d
  VERDICT   : CLEAN ON BOTH CLAUSES
  self-hash : sha256/32 8fd741e007792ba87774685503183f45
=== END AUDIT SIDECAR ===
```

---

## THE REACH, STATED — because a check whose reach is not stated will be trusted beyond it

### **IT CLOSES:** a verdict typed into a report that no tool produced; a sidecar
edited after emission (the self-hash).

### **IT DOES NOT CLOSE:** ***a sidecar fabricated wholesale.*** Nothing here
distinguishes a forged sidecar from a real one, and **a forger can compute a
hash.** The tools' own headers carry this sentence, so ### **the reach travels
with the tool and not only with this report.**

### **SO IT RAISES THE COST OF A FALSE AUDIT FROM ZERO TO DELIBERATE. It does not
make one impossible, and the convention may not be cited as though it did.**

---

## WHAT THIS ACT DID NOT DO

**No mathematics.** No claim advanced, weakened or strengthened. The identity
lane stays closed (b142/b143); **the boundary stays refused and typed** (b151),
and ### **the negative-read fence stands unchanged — nothing in b151 may be cited
as progress toward the license.** Core **271/271**, rows 1–68, **UNTOUCHED**. No
deposit; no circulation beyond relay reports. **HELD (`6eada6a`,
`held/carrier-acts`) LOCAL-ONLY**, ancestry and by-name checks run on the push.
**TECHNE-Core untouched.** The patent seat's tree **read, never written**.

### **AND THE HONEST DEFLATION:** this act built a mechanism against a class of
***dishonest-looking record***, not against being ***wrong***. Every member of the
trilogy was a true statement about nothing, or a false statement about a check —
**none was a mathematical error.** ### **THE RECORD IS NOW HARDER TO MISREAD. IT
IS NOT MORE CORRECT.**

---

## PINS AT CLOSE — by `ls-remote`, never from recall

| repository | pin |
|:--|:--|
| `PLACE-papers` `main` | `781b8e27611d478694e3497f1ee10595ba11b43e` |
| `relay` `main` | **`7034fe488547b21f77f2c69a9560626f8d8a6a6c`** *(the act's commit; this pin line follows it, per the established two-step)* |
| mirror | `mirror-refresh-2026-08-24.zip` — **31 files, roster unchanged, CLEAN ON BOTH CLAUSES** |
| HELD | `held/carrier-acts` = `6eada6a` — **LOCAL-ONLY, unpushed** |

**Load this export:** `mirror-refresh-2026-08-24.zip`.

---

## THE VERIFIER RUN AGAINST THIS REPORT — and what it cannot see

Per the registration, `tools/audit_verify.py` was run against **this file**
before it shipped:

```
  report : 2026-08-24-audit-emit.md
  blocks : 4
    1  MATCHED  audit_b153_banned_terms.txt        (self-hash ok)
    2  MATCHED  audit_b153_commit_selfcheck.txt    (self-hash ok)
    3  MATCHED  audit_b153_mirror_verify.txt       (self-hash ok)
    4  MATCHED  audit_b153-relay_banned_terms.txt  (self-hash ok)
  ### VERDICT: CLEAN
```

### **That transcript is the one thing in this report I typed** — because the
verifier's output is *about* the report and cannot be *inside* the report it
verifies without changing it. ### **It is therefore exactly the shape the
convention forbids, and it is marked as such rather than dressed as an audit
block.** *The reader who wants it checked runs the command; the four blocks it
names are the objects that carry the machine-checkable hashes.* ***A summary of a
check is not the check.***

### **AND THE SECOND VOCABULARY REVIEW**, over this act's **relay-side** writings
— the bank, this report, and the tools themselves:

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b153-relay
  run at    : 2026-08-24T20:34:58 (local)
  input     : whole file b153_audit_emit.txt (created this act)
  input     : whole file 2026-08-24-audit-emit.md (created this act)
  input     : whole file audit_emit.py (created this act)
  input     : whole file audit_verify.py (created this act)
  input     : whole file banned_terms.py (created this act)
  input     : whole file mirror_verify.py (created this act)
  input     : whole file commit_selfcheck.py (created this act)
  stems     : gap, blind
  files     : 7
  lines     : 1076
  hits      : 12
  live uses : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 4785afd6847a331a495233b4a3702f7c
=== END AUDIT SIDECAR ===
```

**Twelve hits, zero live** — and all twelve sit inside `banned_terms.py`'s own
source, where the stems must be spelled to be searched for. ### **The bank, this
report and both new tools carry none.**

**One sidecar will report UNUSED**: the `relay` commit self-description check,
emitted at the commit *after this text is fixed* — **run but not quoted**, which
the tool distinguishes from a failure by design. ### **A check may be run without
being shown, and a convention that punished that would teach the operator to
quote everything until the blocks became scenery.**

*STOP — the ferry's end.*
