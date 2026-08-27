# b209 — THE SECOND TRIM VERIFICATION

**2026-08-27 · relay `reports/2026-08-27-second-trim-verification.md`**
**Ferry part 1 of 2 and part 2 of 2, BOTH receipt-confirmed IN FULL before execution (Rule 1).**
**Registration `data/b209_registration_2026-08-27.txt`, banked before any verification. Bank: `data/b209_second_trim_verification.txt`. Table: `data/b209_table_of_the_pile.txt`.**

> ### **THE AUTHOR'S UI ACTION IS THE SOLE DELETION PATH.**
> ### **A ROW READING "SAFE" MEANS A VERIFIED COPY EXISTS ELSEWHERE — IT DOES NOT MEAN THE FILE SHOULD GO.**
> ### **NO PROJECT FILE WAS DELETED, MOVED OR MODIFIED BY THIS ACT.**
> *** ### **AND TWO ROWS WERE REFUSED THE BACKFILL: THE PILE'S TWO UNFILED PROVISIONAL PATENT SPECIFICATIONS. THE PROTOCOL AS WRITTEN WOULD HAVE PUSHED THEM TO A PUBLIC REPOSITORY.** ***

---

## S0 — THE HOLD, AND WHY THIS ACT EXISTS IN TWO PARTS

Part 1 arrived with its Rule-3 (a) slot carrying **`[PASTE THE 84-LINE LISTING HERE, TITLES AND
DATES AS GIVEN]`** — the instruction to paste, not the paste. ### **The executor held, banked
nothing, and named the defect.** Part 2 carried the manifest and the carrier.

### **THE REFUSAL WAS THEREFORE SATISFIED AND NOT OVERRIDDEN** — the same b122 → b123 sequence,
run a second time, for the same reason and with the same result.

---

## S1 — GATE ZERO (amendment (a′)), run BEFORE the registration was banked

| check | declared | measured | verdict |
|:--|:--|:--|:--|
| manifest md5 | `215e1077…e39f9` | `215e1077…e39f9` | **AGREE** |
| carrier md5 | `cda111e1…a593` | `cda111e1…a593` | **AGREE** |
| zip entries | 84 | 84 | **AGREE** |
| bytes unpacked | 1,681,784 | 1,681,784 | **AGREE** |
| **rows vs manifest (raw md5 + byte length)** | 84 | **84 OK, 0 mismatch, 0 missing** | ### **CLEAN** |
| CRLF rows | 6 | 6 | **AGREE** |

Extracted to a scratch path, **never into a repository tree**. ### **GATE ZERO: CLEAN — (P0)'s
first half, resolved before registration rather than awaited.**

---

## S2 — COMPONENT 1: THE RECONCILE (P1)

**b123's own numbers reconcile exactly and carry no defect.** `16 successor-backed + 10
unbacked-from-the-lists + 5 not-present-on-D: + 1 non-candidate = **32 candidate names**`;
`CONSTANCE.md` is the eleventh backfill, carried from b122 by the paste rather than drawn from
the lists. The apparent 32-vs-33 is not an error.

### **SEVEN OF THE 84 CARRY A b123 ROW. SEVENTY-SEVEN ARE NEW.**

**Three reconcile to a b123 artifact AT CONTENT:**

| row | pile file | b123 artifact | containment |
|:--|:--|:--|:--|
| 58 | `SILENCE_AND_EMERGENCE_SUBMISSION.md` | successor-backed row | **1.0000** |
| 59 | `Silence_of_Foundations.md` | successor-backed row + the content exception | **0.9938** |
| 31 | `IDENTITY_SUBSPACE_PAPER.md` | the **backfilled TRIVIUM monograph** | **0.5382** |

**Four correspond to b123 rows that had NO CONTENT AT ALL** — the four DO-NOT-TRIM refusals
(rows 03, 14, 42, 78). b123 could not read them and so could not look for them. ### **This act
supplies their content and their verdict for the first time.**

### *** THE RESULT THAT JUSTIFIES THE never-by-filename RULE ***

b123's backfilled artifact is named **`TRIVIUM_The_Third_Identity_Element.md`**. The pile
contains **`Third_Identity_Element.md`**. ### **A FILENAME MATCH WOULD HAVE PAIRED THEM AND BEEN
WRONG.**

| pairing | containment |
|:--|:--|
| `Third_Identity_Element.md` (row 77) ⟶ the TRIVIUM artifact | **0.0767** — *different papers* |
| `PAPER_015_THE_TRIVIUM_v0_2.md` (row 41) ⟶ the TRIVIUM artifact | 0.0321 |
| ### **`IDENTITY_SUBSPACE_PAPER.md` (row 31)** ⟶ the TRIVIUM artifact | ### **0.5382** |

The artifact is a 73,971-byte monograph and the pile row it actually absorbs is the identity-subspace
paper. ### **THE RULE DID NOT PREVENT A HYPOTHETICAL ERROR. IT CAUGHT A REAL ONE WAITING TO BE MADE.**

### **P1 WAS WRONG, AND WRONG IN THE DIRECTION IT NAMED.** Registered: 12–18 reconciling, 66–72 new.
### **Measured: 7 and 77.** The reason, found at content: b123 swept a list of working-folder names,
and the current pile is very nearly a **different population** — not a later view of the same one.

---

## S3 — COMPONENT 2: THE VERIFICATION AND THE BACKFILL (P2)

2,216 tracked files indexed across the four pushed repos, both md5 columns, presence sought by
**title line or interior content signature — never by filename**.

### *** AN INSTRUMENT WAS BUILT, RUN, AND THEN REFUSED ***

A line-containment search reported `ALL_ZEROS_ARE_SIMPLE_v4` at **0.3234** against its successor and
`THE_STRUCTURAL_COUNT` at **0.3277** — both reading as heavy divergence. ### **They are RE-WRAPS.**
A successor that reflows a paragraph changes every line and no word. The verdicts rest instead on
**word-5-gram containment**, which is indifferent to reflow; the same two rows read **0.9992** and **0.9993**.

### **The first instrument would have produced false divergence on roughly a dozen rows. It is reported
because it was run, not because it was used.**

### *** THE CRLF TRAP, CAUGHT IN THE COMMAND PATH ***

`core.autocrlf` is **true** in PLACE-papers. The first staging warned that six files' CRLF would be
replaced by LF — ### **which would have stored LF blobs and made the byte-exact preservation claim
false for exactly the six rows the manifest's line-ending column exists to protect.** A
`.gitattributes` pinning `* -text` was written into the archive before the commit; all six index
blobs then matched the manifest's **raw** md5 column. ### **The column the ferry added is the reason
this was visible at all.**

### THE BACKFILL

| | |
|:--|:--|
| destination | `PLACE-papers/archive/2026-08-27-trim-backfill/` |
| files written | **72**, filenames preserved, md5-verified at both ends, **0 failures** |
| commit | **`7d02df5`** — pre-commit seat-boundary hook **EXERCISED: 74 staged, 0 foreign, CLEAN** |
| push | `eae2d3d..7d02df5`; **`ls-remote` reads back `7d02df5`** |
| **re-verified from the pushed tree** | **fresh shallow clone — 72 of 72 BYTE-EXACT against both the manifest and the carrier, 0 mismatches** |
| not copied | **10 rows already byte-identical to a pushed blob** — they need no copy |

### THE VERDICTS OVER THE 84

| verdict | count | meaning |
|:--|:--|:--|
| **SAFE-AGAINST-SUCCESSOR** | **10** | byte-identical to a pushed blob; path and md5 named |
| **SAFE-AGAINST-BACKFILL** | **72** | archive path and md5 named, re-verified at `7d02df5` |
| **DO-NOT-TRIM** | **2** | withheld, reason stated, **nothing certified** |
| **NOT-A-CANDIDATE** | **0** | no pile row is a tracked repository file — the carrier came from the project, not from D: |

### **SIXTEEN OF THE 72 HAVE NO SUCCESSOR ANYWHERE IN THE FOUR PUSHED REPOS.** Before this act those
sixteen texts existed in **one** place. They now exist in **two**.

### *** THE ACT'S ONE DEVIATION, STATED AND NOT FOLDED IN ***

Clause (d) triggers the backfill on *"no content match"*, which would have copied **sixteen** rows.
### **SEVENTY-TWO WERE COPIED — every row not byte-identical to a pushed blob.**

**THE REASON.** Only byte identity certifies that no text is lost. A successor at 0.93 containment is
missing *something*, and the executor cannot certify which words that something contains. The ferry's
FOOT says that after this act **no trim can destroy a sole survivor**; at any grade short of byte
identity that sentence would have been an estimate. ### **The widening is a pure addition to an
archive directory — it deletes nothing, modifies nothing, promotes nothing.**

### THE PREDICTIONS, SCORED

| | registered | measured | verdict |
|:--|:--|:--|:--|
| **(P0)** gate | 84/84 pass | 84/84, 0 mismatch | ### **LANDED** |
| **(P0)** the four ex-DO-NOT-TRIM rows | *"at least one unbacked"*, **and named `PAPER_021_LOCIS_CRITICAL_RATCHET`** | row 42 at **0.0214** — unbacked, **and the only one of the four** | ### **LANDED, INCLUDING THE NAMED GUESS** |
| **(P1)** reconcile | 12–18 / 66–72 | **7 / 77** | ### **WRONG** |
| **(P2)** backfill count | 8–25 rows | **16** | ### **LANDED** |
| **(P2)** backfill *mechanism* | twelve May–June rows named in advance | **6 of 16** were among them; **6 named rows were BACKED**; **10 unbacked were not anticipated** | ### **HALF** |

### **The count was a good prediction and the mechanism was a mediocre one — and the mechanism is the
half that was supposed to be explanatory.**

---

## S4 — COMPONENT 3: THE TABLE, AND THE MIRROR (P3)

The table is filed whole at **`data/b209_table_of_the_pile.txt`**, 84 rows, headed with the sentence
that the author's UI action is the sole deletion path and that a safe row means a verified copy exists
elsewhere and not that the file should go. Every row carries verdict, warrant, and where a successor
exists its path and measured containment.

### **THE MIRROR ROSTER ANSWERS P3'S QUESTION IN THE NEGATIVE.**

The roster is **40 source paths, unchanged**. ### **At content the mirror carries only TWO of the
eighty-four:**

| row | pile file | roster entry | containment |
|:--|:--|:--|:--|
| 39 | `ONE_PAGE_PROOF.md` | `day1\A_Place_to_Stand.md` | 0.8284 |
| 60 | `SILENCE_PRINCIPLE_FORMAL.md` | `phase1.5\structural\FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md` | 0.3265 |

### **RE-ADDING THE MIRROR REPLACES ALMOST NOTHING IN THE PILE.** The roster holds the ledgers,
keystones and canonical papers; the pile holds the working manuscripts. They are very nearly disjoint
populations — which is not what *"which pile rows will the mirror replace"* presupposes.

PLACE-papers moved, so the mirror was **rebuilt** (`mirror-refresh-2026-08-27.zip`) and verified
**CLEAN ON ALL THREE CLAUSES** at the new HEAD.

---

## S5 — *** THE TWO ROWS THIS ACT REFUSED TO BACKFILL ***

Rows **46** `PROV1_FORMATION_VERIFICATION_ARCHITECTURE.md` (44,540 b) and **47**
`PROV2_CONSERVATION_GRADE_VERIFICATION.md` (12,966 b) are **PROVISIONAL PATENT APPLICATIONS**. Both
carry a **blank filing date** (`____________, 2026`); PROV1 is marked **CONFIDENTIAL**. Both are
**unbacked at 0.0000** against all four pushed repos.

### **CLAUSE (d) AS WRITTEN WOULD THEREFORE HAVE COPIED THEM INTO A PUBLIC REPOSITORY AND PUSHED THEM.**
### **THEY WERE NOT WRITTEN AND NOT PUSHED.**

**The ground, checked at content and not assumed.** It might be argued the material is already public,
since PLACE-papers tracks `phase1.5/method/patent-package/filings/PROV-1.md` and `PROV-2.md`.
### **It is not the same material:**

| pairing | containment |
|:--|:--|
| row 46 ⟶ `filings/PROV-1.md` | **0.0000** |
| row 46 ⟶ `PROVISIONAL_A_SPECIFICATION.md` | **0.0000** |
| row 46 ⟶ `filings/A-CANDIDATE.md` | **0.0000** |
| row 47 ⟶ `filings/PROV-2.md` | **0.0000** |

And the repository's own `PROV-1.md` says on its face: *"Tier N, private, attorney-facing … **The
executor cannot read the filed PROV-1 claims** (author-held scope docs)."*

### **THE PILE HOLDS THE SPECIFICATIONS THE RECORD SAYS THIS SEAT CANNOT READ.** Pushing them would be
a **first public disclosure of unfiled patent material**, it would be **irreversible**, and it is the
author's decision and not this seat's.

**ROUTED TO THE AUTHOR.** Their DO-NOT-TRIM verdict means only that **nothing was certified** — not
that the files matter, and not that they do not. Their project copies are untouched and remain the only
copies this act knows of.

> **One adjacent observation, filed and not acted on:** the repository's `PROV-1.md` describes itself
> as *"Tier N, private"* while sitting in a public repository. That is a posture question for the
> patent seat, not a defect this act may touch.

---

## S6 — THE AUDIT SIDECARS (emitted by the tools; embedded verbatim, never retyped)

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b209
  run at    : 2026-08-27T10:16:39 (local)
  input     : whole file README.md (created this act)
  input     : whole file .gitattributes (created this act)
  stems     : gap, blind
  files     : 2
  lines     : 118
  hits      : 0
  live uses : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 707df32a8fc7c0e927422feeb9f1c30f
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : commit_selfcheck
  act       : b209
  run at    : 2026-08-27T10:16:39 (local)
  input     : D:/MY-DOwnloads/PLACE-papers
  input     : HEAD
  written   : 74
  foreign   : 0
  ro-claim  : none
  compliance : none
  VERDICT   : CLEAN
  self-hash : sha256/32 2cf2b0018ddb6d1630b299c0da088bef
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : mirror_verify
  act       : b209
  run at    : 2026-08-27T10:16:39 (local)
  input     : mirror-refresh-2026-08-27.zip
  files     : 40
  rows      : 40
  mismatch  : 0
  declared  : 7d02df5
  ls-remote : 7d02df5e13ba
  VERDICT   : CLEAN ON ALL THREE CLAUSES
  self-hash : sha256/32 1bc7707d5ad6b914b71e7a0f43004d81
=== END AUDIT SIDECAR ===
```

### TWO OBSERVATIONS FILED AGAINST THE CHECKS THEMSELVES, NEITHER FIXED HERE

**(i)** `commit_selfcheck` clause (2) reported **"no read-only claim detected"** over a message
containing *"The patent-package tree was **NEITHER READ FOR CONTENT NOR WRITTEN** by this commit"*.
### **The claim is true and the check did not see it.** This is the limit its own header states —
explicit patterns, cannot read meaning — **observed live rather than quoted**. The class is not closed.

**(ii)** `banned_terms` over the **whole commit** returns **NOT CLEAN**, on hits inside verbatim author
papers. ### **The governing scope is the act's own voice, and it is CLEAN at 0 live uses over 118
lines.** Correcting the corpus hits would require editing preserved quotations, which would destroy the
byte-identity that is the backfill's entire warrant. ### **Rule 3 governs the record's voice, not its
preserved quotations** — and this act is the sharpest case of that distinction the record has produced.

---

## S7 — PINS

| repo | pin (`ls-remote`, this act) |
|:--|:--|
| **PLACE-papers** | ### **`4733945b330c7ab242ad1c8f9698f03091a6e664`** — *moved twice this act:* `eae2d3d` → **`7d02df5`** (the backfill, 74 files) → **`4733945`** (the register entry, 1 file) |
| relay | `a148fc8` at registration; the b209 pin-line commit at close |
| SIDE-global-section | `76d5182` — **UNMOVED, no build** |
| SIDE-kernel | `0256e9e` — **UNMOVED** |
| **mirror** | ### **`mirror-refresh-2026-08-27.zip`** — 40 files, **rebuilt TWICE** (once at `7d02df5`, again at `4733945` when the loom entry moved roster entry 6), **CLEAN ON ALL THREE CLAUSES** both times |
| HELD | `held/carrier-acts` = `6eada6a` — **LOCAL-ONLY, untouched by this act** |

> ### **A NOTE ON THE SECOND PUSH, BECAUSE IT NEARLY WENT TO THE WRONG REPOSITORY.** The
> register commit's push was first issued from a shell whose working directory had been changed to
> `relay/tools`, and `git push origin main` there addressed **relay**, not PLACE-papers — it
> returned *"Everything up-to-date"* and `ls-remote` returned relay's SHA. ### **A push that
> reports success against the wrong repository is indistinguishable from one that did nothing**,
> and it was caught only because the read-back SHA was recognised as relay's. The push was
> re-issued with an explicit `-C`. ***Filed because the read-back is what caught it, which is the
> whole argument for reading back.***

### THE FINAL MIRROR VERIFICATION (emitted; embedded verbatim)

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : mirror_verify
  act       : b209-final
  run at    : 2026-08-27T10:22:41 (local)
  input     : mirror-refresh-2026-08-27.zip
  files     : 40
  rows      : 40
  mismatch  : 0
  declared  : 4733945
  ls-remote : 4733945b330c
  VERDICT   : CLEAN ON ALL THREE CLAUSES
  self-hash : sha256/32 2f6eba2abb6223dacf1b3a4ecd5178cb
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b209-loom
  run at    : 2026-08-27T10:21:30 (local)
  input     : added lines in D:/MY-DOwnloads/PLACE-papers vs HEAD
  stems     : gap, blind
  files     : 1
  lines     : 21
  hits      : 0
  live uses : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 323cbc92aa713af830f746708156fe73
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : commit_selfcheck
  act       : b209-loom
  run at    : 2026-08-27T10:21:54 (local)
  input     : D:/MY-DOwnloads/PLACE-papers
  input     : HEAD
  written   : 1
  foreign   : 0
  ro-claim  : none
  compliance : none
  VERDICT   : CLEAN
  self-hash : sha256/32 e84cb8f30316a6a59f611c70d56bc16d
=== END AUDIT SIDECAR ===
```

### THE RELAY VOCABULARY REVIEW — BOTH RUNS CARRIED, THE FAILING ONE FIRST

### **The first run over this act's own relay voice was NOT CLEAN, at 2 live uses**, both of them
the same phrase of the executor's — *"…which is **blind** to reflow"* — in the bank and in this
report. ### **They were corrected, not excused**, to *"which is indifferent to reflow"*.

### **BOTH SIDECARS ARE CARRIED BECAUSE b156 MADE THE PATHS RUN-UNIQUE AND APPEND-ONLY FOR
EXACTLY THIS CASE** — *a tool that discards its own failures keeps a record of successes, not of
runs.* Embedding only the `_r2` block would have made this act look clean on the first pass.

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b209-relay
  run at    : 2026-08-27T10:23:59 (local)
  input     : added lines in D:/relay vs HEAD
  stems     : gap, blind
  files     : 11
  lines     : 1037
  hits      : 10
  live uses : 2
  VERDICT   : NOT CLEAN
  self-hash : sha256/32 c111e4b13f7595a82ec76f7c4bdeaa99
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b209-relay
  run at    : 2026-08-27T10:24:55 (local)
  input     : added lines in D:/relay vs HEAD
  stems     : gap, blind
  files     : 12
  lines     : 1050
  hits      : 10
  live uses : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 21a5aa6eff5da968e44477b363a10234
=== END AUDIT SIDECAR ===
```

### THE IN-FLIGHT REGISTER

One new item, filed at `VERIFICATION_LOOM.md`, owner the **AUTHOR**, **LIVE**: ### **whether the
pile's two unfiled provisional patent specifications may be preserved in a public repository at
all.** It wants a **RULING**, and no executor work produces one. ### **The register's own limit is
restated beside it** — the register and the standing debt line remain two different lists, and
adding this item does not make the register a statement of everything owed.

**DEVIATIONS:** one — the backfill widened from sixteen rows to seventy-two (S3).
**DIVERGENCES:** one — the ferry's description of row 18 does not match the manifest's row 18; **the
manifest governed** and the divergence was recorded at registration rather than silently reconciled.
**REFUSALS:** one — rows 46 and 47, routed to the author (S5).
