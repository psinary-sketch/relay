# b157 — THE FEDERATION ORIENTATION SURVEY

**Registration `046570c`, banked before any work.** 2026-08-25. Ferry part 1 of 1,
receipt confirmed in full before execution. ### **READ-ONLY: no kernel was modified,
built, or tagged; the only writes were to `relay` and to PLACE-papers' own ledgers.**

> ### **43 REPOSITORIES · 2005 THEOREM DECLARATIONS · ZERO DIVERGENCE — AND SIX FINDINGS,
> TWO OF WHICH ARE THIS SURVEY'S OWN FALSE POSITIVES.**

---

## COMPONENT 1 — THE LIVE CENSUS

**43 `SIDE-*` git repositories on `D:`.** Every figure read at run time: local HEAD,
branch, latest tag with peeled SHA, toolchain pin, last commit date, working-tree state,
and remote HEAD by `ls-remote`.

### **THE DIVERGENCES: THERE ARE NONE.** 43 repos · **0** local≠remote · **0** unread
remotes · **0** dirty trees · **3** untagged (`SIDE-constants`, `SIDE-fano-darkness`,
`SIDE-li-map`).

> ***THE EXECUTOR'S REGISTERED PREDICTION (e1) IS WRONG AND IS SCORED WRONG.*** He wrote,
> before the work, that the census would show *"REAL DIVERGENCE, not a clean federation"*,
> on the ground that unpushed local work is the normal residue of a burst-pushed
> federation. ### **The federation is fully synchronised.** *The ground was plausible and
> the fact is otherwise.*

### **AND THE EVEN COUNT WAS COUNTER-CHECKED**, because the registration named the risk —
*a count that comes out even is not evidence the right things were counted*. The first
pass compared each local HEAD against `ls-remote origin HEAD` — **the remote's DEFAULT
branch** — which would agree *by accident* for any repo sitting on another branch. Redone
against `refs/heads/<the repo's own branch>`: ### **all 43 on `main`, none detached, every
local matching its own branch ref.** *The even count survives its counter-check, and the
check is written down because the reader cannot otherwise see that it was run.*

**Toolchain pins** — ### **three of them: 30 at `v4.29.0-rc8`, 11 at `v4.29.1`, 2 at
`v4.30.0-rc2`** (`SIDE-cosmo`, `SIDE-effects`). ***The one census fact with a cost
attached: a federation-wide rebuild would cross it. None is proposed here.***

**The set difference, both directions.** **10 on disk named by no REGISTRY row** —
`SIDE-class-coupling`, `SIDE-coupling`, `SIDE-cubit-axis`, `SIDE-dark-interface`,
`SIDE-formation-arithmetic`, `SIDE-formation-procedure`, `SIDE-meta`, `SIDE-orchestrator`,
`SIDE-residual-bridge`, `SIDE-t7-topology-cmb`. ### **Named, not judged: a kernel no paper
cites is not thereby defective.** **3 named in REGISTRY but absent from disk** — and two
of those are this survey's own artifacts (finding 5).

---

## COMPONENT 2 — THE CONTENT INVENTORY

### THE DEPTH SPLIT, STATED IN THE OPEN

**2005 theorem/lemma declarations across 414 files in 43 repositories.** ### **(e3) lands:
that is not one act's work at the rubric's depth.** The registered remedy was applied —
**scope by depth, not by silence**: ### **6 of 43 repositories read AT CONTENT; 37
ENUMERATED ONLY**, with the split carried **in the table's own last column** so the
boundary travels with the data. ***An unstated truncation would read as coverage.***

### THE SORRY COUNT, AND WHY ITS FIRST VERSION WAS WORTHLESS

A crude line scan reported **158** sorry-bearing lines, **including 15 in
`SIDE-global-section`** — which would have contradicted the kernel-purity ruling *and file
E's own "SORRY COUNT OF THIS FILE: 0"*. ### **It was a regex over documents, not a read of
them** (the b147 lesson, re-earned): it matched **prose mentioning sorry**, file E's own
zero-count line included. Comment-aware:

```
  158  ->  37 apparent sorry tokens outside comments
  SIDE-global-section  ->  ZERO
    SIDE-effects           3   Milestones.lean 32, 49, 63
    SIDE-kernel           32   ALL under legacy/
    SIDE-lv-conservation   2   PinnedGoal.lean:23; T3_StepNineBridge.lean:108
```

*Every survivor is printed with file and line so each can be **read** rather than tallied.*
### **Reach: this strips comments; it does not elaborate Lean. Only a build decides a
sorry, and no repo was built.**

**`SIDE-kernel`'s 32 are outside its build.** `lakefile.lean`'s targets are `Kernel`,
`Bridge`, `MetaKernel` — ### **`legacy` is not among them**, and the built libraries carry
none. *Consistent with the purity ruling, and checked rather than assumed.*

### ### THE SCAFFOLD RULING RE-VERIFIED — AND FOUND SUPERSEDED

The ferry carried: *"`GRH.grh_exclusion` and `LandauSiegel.no_ls_zero` remain
scaffold-pattern — citation-banned"*. ### **They do not remain scaffold-pattern. They are
retired and gone.** `Structural.lean` carries an explicit **RETIREMENT LEDGER** — *"retired
as content-free (True-stub or opaque-Prop)"* — naming both.

***And the repo's own front document has not caught up.*** `AGENTS.md` lists **20**
theorems under "Theorems exported". Checked one by one:

```
  PRESENT (2):  no_type_d, formation_seven
  ### ABSENT (18): all_gapped, mass_gap, all_excluded, sectors_complete, gap_bounds,
      twist_cancels, formation_preserved_grh, grh_exclusion, no_ls_zero,
      no_conspiracy_twins, no_conspiracy_goldbach, no_conspiracy_sg, all_bound,
      sha_bounded, all_mismatch_absent, bsd_full, artin_from_grh, side_exclusion
```

### **The source is the honest party; the front document is the stale one.** The citation
ban is **restated**, is now *strictly redundant* for those two — a terminal that does not
exist cannot be cited — ### **and stands anyway, because a name can return.**

**The two survivors, graded by reading the statement.** `formation_seven : 2+3+2+0 = 7 :=
rfl` — **DERIVES at the instance**, ***and its content is arithmetic: it decides a sum and
says nothing about formation, which the grade must not be read as saying.***
`no_type_d (h : ∀ a, coupling a → modular a) : ¬(TypeD α coupling modular)` — **DERIVES**;
a genuine, elementary logical lemma, honestly stated.

### ### AXIOM-CLEAN, COMPILE-CLEAN, AND CONTENT-FREE ARE COMPATIBLE

```
  def Sha_finite_via_SIDE : Bool := true
  theorem Sha_finite : Sha_finite_via_SIDE = true := by decide
```

### **A definitional tautology: the Bool just set to `true` is `true`.** `bsd_fully_closed`
and `BSD_architecture_fully_closed` share the shape. ***These print zero axioms and compile
cleanly.*** ### **This is the salt-check's justification, not an illustration of it — a
grade taken from an axiom profile or a compile status would have called them clean.**
Graded **SCAFFOLDING-OR-SHELL** by reading the statement. *And SIDE-effects' ledger names
these very declarations, so **the record already knew in one repository what another still
ships**; this survey's contribution is to have read both and set them side by side.*

### ONE FLAG AT FULL PROMINENCE

`Milestones.lean` states three **known-open conjectures at their real types**, each closed
by `sorry` at a marked boundary, each naming the Mathlib infrastructure that would close
it. **SCAFFOLDING-OR-SHELL, and the file says so itself** — *that part is exemplary.*
### **The flag: its status block reads "3 theorems, 3 sorrys, 0 axioms."** ### **"0 axioms"
is true only under the reading "no `axiom` declarations"** — a sorry-closed theorem carries
`sorryAx`. ***In a file whose entire purpose is honesty about what is and is not proved,
that is the one sentence a reader could take the wrong way.***

*(e4) lands — at **document** grade rather than the docstring-versus-statement grade
intended, and the difference is stated rather than smoothed.* ### **Reach: one was FOUND.
37 of 43 repositories were not read, so this is "one found", not "one exists".**

---

## COMPONENT 3 — THE TABLE AND THE FILINGS

**The orientation table is filed at the working loom**, one row per repository: repo ·
citable tag with peeled SHA · HEAD · theorem-declaration count · apparent sorry count ·
REGISTRY reference count · citation status · ### **read depth this act**. ### **It travels
in the mirror without a roster change**, `VERIFICATION_LOOM.md` already being a roster
member — *checked, not assumed.*

**Citation status, from live pins:** **26** where HEAD **is** the citable tag · ### **14
where HEAD is AHEAD of the latest tag** · **3** with no tag at all. ***Named, not judged:
whether any should be re-tagged is deposit-adjacent, and the deposit gates are PARKED. The
executor does not rule and does not recommend.***

### **FINDING 5 — TWO OF THIS SURVEY'S OWN "MISSING REPOSITORIES" WERE ITS OWN FALSE
POSITIVES.** `SIDE-method` names a consult **method** (*"SIDE-method exploratory
consult"*); `SIDE-closure` is a **phrase** in prose. ### **A regex over a document is not a
read of it — twice in one act, once against the sorry count and once against the repository
list.** ***Filed as artifacts, not findings: a survey that reports its own false positives
as findings is worse than no survey.***

*(An unauthenticated probe of all three returned "could not read Username", which
distinguishes neither private-but-existing from absent — the b149 lesson. Re-probed with
the credentials the census already used: "Repository not found". ### **Reach: that is "not
found under these credentials", which does not distinguish nonexistent from existing under
another owner.**)*

### **FINDING 6 — A CURED DEFECT WHOSE FILING WAS NEVER CLOSED.** REGISTRY files the
phantom `SIDE-steane-arithmetic` citation in `A_METHODOLOGY.md` as **"Filed for
correction."** ### **The correction was made** — the paper's own **v0.5.1 (2026-07-13)**
repointed both citations to `SIDE-substrate-cluster`, and the named terminal is real:
`theorem steane_count : SteaneQubit.all.length = 7 := by rfl`, read at content. ### **The
filing is stale, not the paper.** ***Routed; REGISTRY is not edited this act, per the
ferry.*** *A defect ledger that never closes its entries becomes a list of things that
MIGHT be wrong — a different and much less useful object than a list of things that ARE.*

### THE STALE-SNAPSHOT DELTA, IN ONE PARAGRAPH

Measured against the 2026-08-04 prior, ### **the federation has not drifted — it has
consolidated.** All 43 are on `main`, clean, and identical to their remotes, which is *not*
what a burst-pushed federation usually looks like four weeks on. What moved is concentrated
in acts this record already carries: `SIDE-global-section` to **281/281, rows 1–71** across
b154–b156; `SIDE-kernel` to **v1.7**; and the toolchain spread now at **three pins**.
### **Nothing else moved — and the survey's value is largely that it can now say so from
live pins rather than from belief.**

**THE THIRTY-SECOND SEAM'S DEBT:** b156 and this act; the methodology day's returns; route
A's ruling if it comes; ### **the six findings, none acted on here**; and the deep items
reserved for a session with breadth — ### **for which the kernel layer is now oriented.**

---

## THE AUDITS — EMITTED, NOT TYPED

The vocabulary review (Rule 3), scoped by this act's own diff:

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b157
  run at    : 2026-08-25T12:13:21 (local)
  input     : added lines in D:/MY-DOwnloads/PLACE-papers vs HEAD
  input     : whole file b157_registration_2026-08-25.txt (created this act)
  input     : whole file b157_federation_survey.txt (created this act)
  input     : whole file b157_census.py (created this act)
  input     : whole file b157_table.py (created this act)
  input     : EXCLUDED 0 lines whose path contains: patent-package   ### stated, never silent
  stems     : gap, blind
  files     : 5
  lines     : 771
  hits      : 2
  live uses : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 6608cc90e3cdd52b88a05555a808e34f
=== END AUDIT SIDECAR ===
```

The commit self-description check on `PLACE-papers`:

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : commit_selfcheck
  act       : b157
  run at    : 2026-08-25T12:14:36 (local)
  input     : D:/MY-DOwnloads/PLACE-papers
  input     : (staged)
  written   : 2
  foreign   : 0
  ro-claim  : none
  compliance : yes
  VERDICT   : CLEAN
  self-hash : sha256/32 44a327b76e58fa813d5a1eec3e1cffdd
=== END AUDIT SIDECAR ===
```

The mirror, both clauses of the stale-build law, at the new HEAD:

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : mirror_verify
  act       : b157
  run at    : 2026-08-25T12:15:03 (local)
  input     : mirror-refresh-2026-08-25.zip
  files     : 31
  rows      : 31
  mismatch  : 0
  declared  : 3f8676f
  ls-remote : 3f8676fd47e1
  VERDICT   : CLEAN ON BOTH CLAUSES
  self-hash : sha256/32 48b0f9bdc9da95c5c447f9c08139bd7f
=== END AUDIT SIDECAR ===
```

---

## THE GRADE

- **READ AT CONTENT AND GRADED:** SIDE-effects' two survivors (**DERIVES**, with
  `formation_seven`'s arithmetic content named); its three milestone terminals
  (**SCAFFOLDING-OR-SHELL**); the BSD stub family (**SCAFFOLDING-OR-SHELL**);
  `steane_count` (**DERIVES** at the instance).
- **READ AT CONTENT, NOT GRADED:** SIDE-kernel's build targets; SIDE-global-section's
  prints; the Phase15 declarations named present.
- ### **ENUMERATED ONLY, NOT READ: 37 of 43. Their grades are not assigned and must not be
  inferred from the table.**
- ### **NOTHING PROMOTED, DEMOTED, OR RE-GRADED. A SURVEY IS NOT A PREDICATE**, and these
  grades are **readings, not rulings** — ***where one disagrees with a filed ruling, the
  filed ruling wins.***

**Core unchanged at 281/281, rows 1–71.** No kernel modified, built, or tagged. Nothing
about `h2` beyond the register sentence exact — *RH reduced to a single located clause,
reduction machine-verified.* No deposit, no circulation; **HELD (`6eada6a`) LOCAL-ONLY**;
**TECHNE-Core private, untouched, and not enumerated by this survey**; the patent seat's
tree neither read nor written.

---

## THE SEATS, SCORED

**NAVIGATOR: no prediction to score.** The ferry fixed the shape and stated no expected
outcome; ### **none was invented on its behalf, and the seat is recorded as UNSCORED rather
than as landed.**

**EXECUTOR: two wrong, two right — and the wrong ones are the interesting ones.**
**(e1)** real divergence — ### **WRONG**; the federation is fully synchronised.
**(e2)** the scaffold terminals still scaffold-pattern — ### **WRONG, in the favourable
direction: they are RETIRED.** ***Recorded as a miss, because "wrong about which good thing
happened" is still wrong, and scoring it a hit would teach the wrong lesson.***
**(e3)** the inventory exceeds one act — **landed**, and the registered remedy applied.
**(e4)** at least one docstring-vs-statement disagreement — **landed**, at document grade,
with the reach limited to *one found, not one exists*.

### **Net: wrong about the two things predicted from the record's shape, right about the two
predicted from arithmetic.** ***A pattern worth the record, not a score worth defending.***

---

## PINS AT CLOSE — by `ls-remote`, never from recall

| repository | pin |
|:--|:--|
| `PLACE-papers` `main` | `3f8676fd47e1c3a1a474120c3115c8075168d723` |
| `relay` `main` | **`f958040057aa025827758db385bf08ef20cd7405`** *(the act's commit; this pin line follows it, per the established two-step)* |
| `SIDE-global-section` `main` | `83ef81b98ed9bd1a13608659771a9edc62965ba7` — **unchanged; not touched** |
| the other 42 `SIDE-*` | **read only; every pin in the loom's table** |
| mirror | `mirror-refresh-2026-08-25.zip` — rebuilt at the new HEAD, **clean on both clauses** |
| HELD | `held/carrier-acts` = `6eada6a` — **LOCAL-ONLY, unpushed** |

**Load this export:** `mirror-refresh-2026-08-25.zip`.

*STOP — the ferry's end.*
