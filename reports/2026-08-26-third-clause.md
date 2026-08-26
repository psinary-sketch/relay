# b183 — THE THIRD CLAUSE AND THE ROSTER REPAIR

**Registration `cd942e0`, banked after the load-bearing reads and the pre-merge comparison,
before the reconciliation and before the clause was written — with the merge's direction fixed in
advance and its cross-language hazard registered before the thing that carries it was built.**
2026-08-26. Ferry part 1 of 1, receipt confirmed in full.

> ### **TOOL AND CONFIGURATION WORK. NO MATHEMATICAL CLAIM.** *Nothing opened, closed, or
> reopened. Core unchanged at 304/304, rows 1–79.*

---

## THE DIVERGENCE — THE FERRY'S PREMISE, CORRECTED AT CONTENT

The ferry calls `mirror_roster.json` **the decorative artifact**. ### **At content it was not
decorative: the builder OVERWRITES IT AT THE END OF EVERY BUILD**, with the staged archive names,
as its previous-build state for the manifest's *ROSTER CHANGE* line.

> ### **THE FILE WAS PLAYING TWO ROLES AT ONCE — IT LOOKED LIKE THE BUILDER'S INPUT AND IT WAS
> THE BUILDER'S OUTPUT.** ### **That, and not neglect, is why b182's row vanished.**
>
> *** ### **HAD THIS NOT BEEN CAUGHT, THE FIRST BUILD AFTER THE MERGE WOULD HAVE OVERWRITTEN THE
> SOURCE-PATH ROSTER WITH STAGED NAMES, AND THE BUILD AFTER THAT WOULD HAVE LOOKED FOR 34 FILES
> THAT DO NOT EXIST AT THOSE PATHS.** ### **An input a process overwrites is not an input; it is
> a scratch pad with a misleading name.** ***
>
> **The repair the ferry asked for was still the right one** — ### **but it needed a step the
> ferry could not have known to name**, and it was found only by reading the builder **to the
> end** rather than to the part I was editing.

---

## COMPONENT 1 — THE SINGLE ROSTER

**The pre-merge comparison, run and reported before any merge**, as required: both artifacts held
**34 entries** but were ### **not two copies of one list** — the `.ps1` held **source paths**
(27 of 34 with a directory, `README.md` appearing **twice**), the JSON held **staged archive
names** including `2026-08-24-ledger-split__README.md`, ### **which is the builder's
post-collision rename and is not a path in the repository.**

**Direction: `ps1 → json`.** ### **The artifact carrying more information survives** — paths
determine staged names, staged names do not determine paths. ### **And a second, empirical
ground from inside this act:** my first comparison script parsed the PowerShell array from Python
and ### **got it wrong — harvesting apostrophes out of the comments and reporting 39 entries,
nineteen of them prose fragments**, including a duplicate basename of `",\n  "`.
### **A roster every non-PowerShell reader must parse PowerShell to read is a roster that will be
misread. That is not a hypothetical risk; it is a measurement taken inside this act.**

- `mirror_roster.json` is now **the single source of truth** — 34 source paths in roster order,
  with ### **three self-describing fields in the file itself** (`_authority`, `_what_these_are`,
  `_history`), because ### **anyone who read the old file read a different kind of list and had
  no way to know.**
- `mirror_build.ps1` **no longer carries a roster** — it reads the JSON, ### **with the roster's
  history preserved in comments** (*deleting the reason a row exists is how a roster becomes a
  list nobody dares touch*), and it **throws** on a missing roster and on an empty one.
- **The roles are split:** previous-build state moved to `mirror_prevbuild.json`.

### **Nothing was deleted, and each file now declares its own role in its own text — no file is
left looking authoritative that is not.**

---

## COMPONENT 2 — THE THIRD CLAUSE

**Clause 3: the archive's contents against the roster.** Every roster entry present; every
archive entry rostered; ### **any mismatch a hard failure.** It replicates the builder's
flat-naming rule exactly, including the unresolved-collision error.

**Fixture-tested before service — both polarities plus the zero case — 5 of 5 as expected:**

| fixture | result |
|:--|:--|
| ### **the b182 instance replayed** — roster 34, archive 33 | ### **HARD FAILURE**, names the missing file — *and this exact archive **passed clauses 1 and 2** at b182* |
| an archive file the roster does not list | **HARD FAILURE**, named |
| a clean build | **CLEAN** |
| ### **the zero case** — empty roster, empty archive | ### **HARD FAILURE** — *the trap it closes: **emptiness matches emptiness and reads as success*** |
| no roster on disk | **HARD FAILURE** — a verification with no roster is not a verification |

### **The informative fixtures are the clean build and the zero case: a clause that failed
everything would also “catch” b182.**

> ### **THE CLAUSE'S LIMIT, REGISTERED AS (e1) BEFORE IT WAS BUILT SO THE ADMISSION COSTS
> SOMETHING:** ### **it replicates the builder's naming rule in a SECOND LANGUAGE.** The builder
> is PowerShell; the clause is Python. ### **If one is edited and not the other they drift, and
> this clause would then fail a good build or pass a bad one.** ### **THIS ACT CREATED THAT
> COUPLING; IT DID NOT CLOSE IT.** The mitigation is only that it fails closed.

**The live run:** rebuilt from the reconciled roster, ### **CLEAN ON ALL THREE CLAUSES at 34
files**, HEAD agreeing with `ls-remote`, ### **and the roster verified to have survived the
build.** The verdict line was also repaired — it still read *“the law requires both”* after a
third clause existed, and ### **a check that miscounts its own clauses is a check misreporting
itself.**

---

## COMPONENT 3 — THE FILINGS

### **The stale-build law now has FOUR instances:** b130 (built a commit early) · b144 (a flat
namespace collision dropped a file) · b182 (a roster edit the builder never read) · **b183 (the
same artifact was also the build's output — the *why* of b182)**. ### **The common shape is not
staleness, and calling it “the stale-build law” has been quietly misleading for four instances.**

> *** ### **THE SPECIES, NAMED: A CHECK THAT PASSES BECAUSE ITS SCOPE EXCLUDES THE DEFECT.**
> ### **It passes BECAUSE it is blinkered, not despite it** — which is why adding effort to such
> a check never finds the fault, and why the only repair is to widen the scope. ***
>
> **Relatives already in the record, which is how a species is established rather than coined:**
> b167's scanner printing CLEAN over an empty scope · b179's hook clearing an empty staged set ·
> b180's index returning eight misses that carried no information · b148's commit message
> asserting compliance in the same commit that falsified it.
> ### **The pattern: THE SCOPE IS THE VERDICT'S SILENT PREMISE, AND A VERDICT THAT DOES NOT PRINT
> ITS SCOPE CANNOT BE AUDITED.** **Filed as M7.**

---

## THE SEATS, SCORED

**NAVIGATOR:** one roster, a third clause, the filings — all delivered.

**EXECUTOR: three land, one holds, one is untestable and says so.**

- **(e1)** the clause creates a new cross-language coupling rather than closing the class —
  ### **holds**, and it is in the tool's header, the bank and this report.
- **(e2)** the zero case would have been the one to slip — ### **untestable as registered, and I
  say so rather than claim it: the ferry named the zero case explicitly, so I cannot know whether
  I would have missed it. The credit is the ferry's.** What the record does show is that b167 and
  b179 both had to add empty-scope failures after the fact.
- **(e3)** the b182 instance caught by clause 3 while still passing 1 and 2 — ### **lands.**
- **(e4)** the JSON rewrite changes the file's **meaning**, not only its content — ### **lands.**
- **(e5)** Core: nothing enters — ### **holds.**

### **And the thing no prediction caught: that the roster file was the builder's own output.**
***I registered the merge's direction correctly and for the right reasons, and still did not
know, when I wrote it, that the merge as first implemented would have destroyed itself on the
next build.***

---

## THE HOOK — REPORTED, NOT CLAIMED

### **The hook did not run this act, and that is not a skipped step.** The seat-boundary hook
guards `PLACE-papers`; ### **this act committed only to `relay`**, so there was no PLACE-papers
commit for it to run on. ### **PLACE-papers HEAD is unchanged at `dc3f80b`** — the mirror was
rebuilt from the same source, not from new content. ***Reporting an unexercised guard as
unexercised is cheaper than manufacturing a commit to exercise it.***

---

## THE THIRTY-SEVENTH SEAM'S DEBT

### **The cross-language naming-rule coupling, new this act and unclosed.** ### **The six
formerly-untracked in-flight items (b182)**, including the engineering queue's named item.
**104 remaining references; ~158 unswept `W-` codes; the definitional fork; gates 2 and 6's
reviewable attempts; the seat boundary's operational form; the Q-route `Ψ` instability; b157's
six findings; the three front-door items; the tense hazard; the bra-ket convention; Prop 5.5's
hazard; the methodology day (M1–M7).** **Deep items:** the relative identification; the h1/h2
statement drafting. ### **The boundary program's CP-1 stands runnable at your schedule.**

---

## THE AUDITS — EMITTED, NOT TYPED

**The pre-merge comparison, corrected run:**

```
==========================================================================
b183 -- THE TWO ROSTER ARTIFACTS, COMPARED BEFORE THE MERGE
==========================================================================
  tools/mirror_build.ps1   (the one the builder READS) : 34 entries
  tools/mirror_roster.json (the one nothing reads)     : 34 entries

--- MEMBERSHIP, BY BASENAME ---
  in ps1 but not json : NONE
  in json but not ps1 : ['2026-08-24-ledger-split__README.md']
  duplicate basenames in ps1 : ['README.md']

--- THE STRUCTURAL DIFFERENCE, WHICH IS THE REAL ONE ---
  ### ps1 carries REPO-RELATIVE PATHS : 27 of 34 entries have a directory
  ### json carries BARE BASENAMES     : 0 of 34 have a directory
  example ps1  : phase2\method\ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md
  example json : OPEN_TRAILS-archive-1-seam-records-through-nineteenth.md

  ### SO THE JSON IS **LOSSY**: it cannot say WHERE a file lives, and two
  ### roster paths sharing a leaf would be indistinguishable in it -- which
  ### is a collision the builder's own comments say it already guards against.
  ### THE MERGE THEREFORE RUNS ps1 -> json, NOT json -> ps1:
  ### THE ARTIFACT CARRYING MORE INFORMATION IS THE ONE THAT SURVIVES.
```

**Clause 3's fixtures:**

```
==========================================================================
b183 -- CLAUSE 3, FIXTURE-TESTED IN BOTH POLARITIES PLUS THE ZERO CASE
==========================================================================
### run BEFORE the clause enters service, per the nursery convention.

--- POLARITY 1 -- THE b182 INSTANCE: roster 34, archive 33, program absent
    ### this exact archive PASSED clauses 1 and 2 at b182.
    result: HARD FAILURE  (as expected)
   in roster, MISSING from archive : 1
   MISSING : THE_BOUNDARY_CONSTRUCTION_PROGRAM.md
   ### CLAUSE 3 : NOT CLEAN -- HARD FAILURE.

--- POLARITY 2 -- a clean build: archive matches the roster exactly
    result: CLEAN         (as expected)
   in roster, MISSING from archive : 0
   CLAUSE 3 : CLEAN -- archive and roster agree, name for name

--- ZERO CASE -- an empty roster against an empty archive
    ### the trap: emptiness matches emptiness and reads as success
    result: HARD FAILURE  (as expected)
   ### CLAUSE 3 : HARD FAILURE -- THE ROSTER IS EMPTY.

--- POLARITY 1b -- an archive file the roster does not list
    result: HARD FAILURE  (as expected)
   in roster, MISSING from archive : 0
   EXTRA   : SMUGGLED.md
   ### CLAUSE 3 : NOT CLEAN -- HARD FAILURE.

--- MISSING ROSTER -- no roster file on disk
    result: HARD FAILURE  (as expected)
   ### CLAUSE 3 : HARD FAILURE -- ROSTER NOT FOUND at D:\relay\tools\__no_such_roster__.json

==========================================================================
### FIXTURES PASSED: 5 of 5
### THE INFORMATIVE ONES ARE POLARITY 2 AND THE ZERO CASE:
### a clause that failed everything would also 'catch' b182.
```

**The live verification, all three clauses:**

```
==============================================================================
MIRROR VERIFICATION -- BOTH CLAUSES OF THE STALE-BUILD LAW (b142)
  archive: D:/MY-DOwnloads/mirror-refresh-2026-08-26.zip
==============================================================================

--- CLAUSE 1: THE ARCHIVE AGAINST ITS OWN MANIFEST ---
  files in archive (excl MANIFEST) : 34
  rows parsed from MANIFEST        : 34
  md5 / byte mismatches            : 0
  CLAUSE 1 : CLEAN

--- CLAUSE 2: THE BUILD'S SOURCE HEAD AGAINST ls-remote ---
  manifest declares source HEAD    : dc3f80b
  ls-remote origin/main              : dc3f80b10b40b2454572828bae54f10aee4ac77a
  CLAUSE 2 : CLEAN -- they agree

--- CLAUSE 3: THE ARCHIVE'S CONTENTS AGAINST THE ROSTER ---
  roster entries (source paths) : 34
  archive files (excl MANIFEST) : 34
  in roster, MISSING from archive : 0
  in archive, NOT in roster       : 0
  CLAUSE 3 : CLEAN -- archive and roster agree, name for name

  ### VERDICT: CLEAN ON ALL THREE CLAUSES
  ### NO CLAUSE ALONE IS THE VERIFICATION; THE LAW REQUIRES ALL THREE.
  ### clause 1 is the archive against ITSELF, clause 2 is the pin, and
  ### clause 3 is the archive against the ROSTER -- ### THE ONLY ONE OF THE
  ### THREE THAT CAN SEE A FILE THAT NEVER ENTERED THE STAGING DIRECTORY.
```

```
==============================================================================
BANNED-TERM REVIEW (banned_terms.py, b142) -- RUN, NOT CLAIMED
==============================================================================
  stems scanned    : gap, blind
  scope            : whole file b183_third_clause.txt (created this act)
  scope            : whole file mirror_verify.py (created this act)
  scope            : whole file mirror_build.ps1 (created this act)
  files in scope   : 3
  lines in scope   : 516   ### the act's own voice, not the corpus
  hits found       : 0
  live uses        : 0

  VERDICT          : CLEAN
  ### the verdict reads the LIVE count, not the hit count -- a scope may
  ### carry excepted hits and still be clean, and that is the whole
  ### reason the classes are printed rather than filtered silently.
```

---

## PINS AT CLOSE — by `ls-remote`, never from recall

| repository | pin |
|:--|:--|
| `PLACE-papers` `main` | `dc3f80b10b40b2454572828bae54f10aee4ac77a` — ### **unchanged; this act touched no papers** |
| `SIDE-global-section` `main` | `755227818c020983fc3f99dca768a3706f1835be` — **unchanged; Core 304/304, rows 1–79** |
| `relay` `main` | `@@RELAY@@` — **the act; read back by `ls-remote`** |
| mirror | `mirror-refresh-2026-08-26.zip` — **34 files**, ### **CLEAN ON ALL THREE CLAUSES** |
| HELD | `held/carrier-acts` = `6eada6a` — **LOCAL-ONLY, unpushed** |

**Load this export:** `mirror-refresh-2026-08-26.zip`.

*STOP — the ferry's end.*
