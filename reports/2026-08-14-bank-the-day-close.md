# BANK THE DAY — CLOSE

**Relay report · 2026-08-14 · author-called · commits only, no new content**
**Nothing deposits. `h2` UNCHANGED. `WIDEN` PAUSED.**

> ### **THE DAY IS BANKED. Everything the forced restart left uncommitted is now in a commit, and every
> remote SHA below was read back from the remote — never taken from push output.**

---

## §1 — `PLACE-papers` (PRIVATE) — THREE COMMITS, PUSHED, VERIFIED

| # | SHA | commit |
|--:|:--|:--|
| (i) | `ef1e944` | `[MECH-PASS 2026-08-13]` W-WITNESS-LATTICE strand (9) clause-bearing face CLOSED; Euler spec `v0.3`; attempt record `v1.0`; carrier build `v0.2` |
| (ii) | `5cd4896` | `[MECH-PASS 2026-08-14a]` `S5`-silence terminology repair: 7 scoped hits → 1 classed residual, 4 files |
| (iii) | `32760a2` | `[2026-08-14b]` disclosure timeline + cover page into `internal/` (REGISTRY-SILENT pending ruling) |

```
local  HEAD                : 32760a2cce0b0d967402a13cd474492b77a607b8
git ls-remote refs/heads/main: 32760a2cce0b0d967402a13cd474492b77a607b8   VERIFIED
```

### **THE ONE PLACE THE SLICING NEEDED SURGERY, RECORDED BECAUSE IT WAS NOT FREE**

`FINDINGS.md` carried **both** slices: the strand-(9) close (49 added lines) **and** one `S5` repair site at
**L1369**. Committing it whole would have put the terminology act inside the research act.

**What was done:** L1369 was reverted to its `HEAD` wording for commit (i) — a **single-line, byte-exact**
substitution, asserted in advance to differ from `HEAD` by *nothing but* `` `S5`-blindness `` → `` `S5`-silence ``,
and refused if it differed by more. Commit (i) was then verified **additions-only** (`+49 / −0`, zero terminology
tokens in its diff). The file was restored from a pre-surgery copy and the repair committed in (ii).

### **PROOF THE SURGERY LEFT NOTHING BEHIND:** all **9** touched files were md5'd before any staging and
re-checked after all three commits — ### **9/9 MATCH**, and `git status` reports the tree clean. The bank
records exactly the bytes that were on disk when the day ended.

---

## §2 — `relay` (PUBLIC) — 32 PUSHED, 2 HELD BY AUTHOR RULING

```
git ls-remote refs/heads/main : 6285c75bbd96ac312923c906ddc47ac96774a501   VERIFIED
reports on the remote          : 244   (212 before + 32)
```

**Commit `6285c75` — 32 reports:** 24 attempt-1 sittings (2–20 with their ADDENDA, the TRUNCATED-HOLD, the
branch-B anchors pass, the one-prime extension writeup, the CLOSES board — **the failures banked as written**:
sitting 18's `L82` divergence, 19's HS-grid failure, 10's `ω` instability, 6's blocked §6) · 5 witness-lattice ·
1 closeout census · 1 item-6 compliance + phase map · 1 post-restart state audit.

### **THE TWO HELD, AND WHY THE FERRY WAS NOT EXECUTED VERBATIM HERE**

The ferry said *"add + commit the 33 reports, push."* Two of them — `2026-08-13-carrier-build-act1.md` and
`act2.md` — describe **`SIDE-carrier-spec`'s `R1`–`R4` / `Δ2` / `Δ4` fields and its two compiled no-gos**
(`no_idempotent_candidate`; the mono-collapse law and its `(iv′)` break-the-mono constraint).

### **`SIDE-carrier-spec` IS PRIVATE. `relay` IS PUBLIC. AND WHETHER WIDENING THAT REPOSITORY — OR
CIRCULATING MATERIAL DESCRIBING IT — CONSTITUTES A DISCLOSURE AFFECTING PATENTABILITY IS THE OPEN QUESTION
NOW BEFORE COUNSEL**, assembled in the very document committed at `32760a2` this same pass.

*Raised before the push, not after.* **Author-ruled 2026-08-14: hold the two.** They are **committed locally
and unpushed** at the tip of local `main` — banked so the work is neither lost nor re-derived, uncirculated so
the decision stays open. `origin/main` deliberately stops one commit behind local.

**Verified after the push:** both files ### **ABSENT from the remote tree**, by direct `git cat-file` against
the remote SHA. **Release condition: counsel's answer, then the author's word.**

*The precedent that made this a question and not a refusal: the technique-spec report — the other half of the
same counsel question — has been public in `relay` since `a4dad08`, and the dossier itself records that much of
the federation has been public since May 2026.*

---

## §3 — `SIDE-spinor` — REPORT-ONLY LINE, ### NO GIT ACT

| reading | value |
|:--|:--|
| `HEAD` | `520abe7`, `main`, `0/0` against `origin/main` |
| deposit pin | tag `v0.1.0` → commit `b235bc6` — ### **`HEAD` is 2 commits ahead** |
| tree | DIRTY: one untracked file |
| the file | `_AuditProbe.lean` · 117 B · ### **created AND last written 2026-07-11 16:06:37** |

A three-line `#print axioms` probe against `SIDESpinor.spinor_forces_half` and
`SIDESpinor.half_iff_centered_zero`. ### **It predates the interrupted ferry by five weeks. It is not ferry
debris, and it was not touched.** No `add`, no `commit`, no `clean`, no checkout. ### **Awaiting the freeze
ruling, exactly as instructed.**

---

## §4 — THE MIRROR, REBUILT — AND ONE ROW THAT DOES NOT RECONCILE

`D:\MY-DOwnloads\mirror-refresh-2026-08-14.zip` · source `HEAD` **`32760a2`** · 22 files flat ·
roster unchanged since 2026-08-06.

### **THE MIRROR WAS WITHHELD ON 2026-08-14's AUDIT BECAUSE ITS MANIFEST WOULD HAVE STAMPED `9641627` OVER
2026-08-13 CONTENT. THAT DEFECT IS GONE:** the manifest now reads `32760a2`, and `FINDINGS.md` /
`OPEN_TRAILS.md` carry `last-commit 5cd4896 2026-08-14`.

**Every row was checked three ways — manifest md5 vs the committed blob vs the bytes on disk:**

| result | rows |
|:--|--:|
| content identical to the committed blob | ### **22 / 22** |
| manifest md5 reproducible from the repository | ### **21 / 22** |

### **THE ONE ROW, NAMED RATHER THAN SMOOTHED — `INSTRUMENTS.md`.** Its committed blob is 36,524 bytes with
**0 CRLF**; the working copy is 36,526 bytes with **exactly 2 CRLF**. ### **The content is identical modulo
line endings** — `git status` is clean because git normalizes on comparison — ### **but the manifest's md5 is
computed from disk bytes, so a reviewer checking that row against `git show` gets a MISMATCH on a file that
has not diverged.**

> ### **THIS IS A FALSE-POSITIVE GENERATOR INSIDE A VERIFICATION INSTRUMENT**, and therefore the loom's own
> class: *a false negative in a verification instrument is worse than no instrument, since it invites a repair
> of something that is not broken.* Here it is the mirror image — a false **positive**, inviting a
> reconciliation of two identical files. ### **NOT REPAIRED: this ferry is commits-only, and normalizing two
> line endings is a content change. FILED FOR THE AUTHOR.**

---

## §5 — COMPLIANCE RE-RUN ### AGAINST THE PUBLISHED BRANCH

*Case-insensitive census over every tracked `.md`, scoped terms* `` `S5`-blindness `` *·* `instrument-blindness`
*·* `bench-blind`.

| ref | scanned | OLD-term | NEW-term |
|:--|--:|:--|--:|
| `9641627` *(the branch as it stood)* | 240 | ### **7 hits in 4 files** | 0 |
| ### **`origin/main` = `32760a2`** *(read from the fetched remote ref)* | 244 | ### **1 hit in 1 file** | 11 |

### **THE ONE RESIDUAL, LOCATED ON THE PUBLISHED BRANCH:** `phase2/method/THE_ATTEMPT_RECORD.md:66` —
correction twelve's **own entry**, quoting the term it repaired, because a correction record that cannot name
what it repaired is not a record. ### **EXCEPTION CLASS: `PROVENANCE-QUOTATION`. By design.**

> ### **`CIRCULATION-CLEAN` IS NOW TRUE OF THE PUBLISHED BRANCH AND NOT ONLY OF THE DISK. That was the point
> of the exercise, and it is met.**

### **THE FIGURE THAT DOES NOT CHECK OUT — FLAGGED, NOT REPAIRED, NOT RESTATED**

Correction twelve records this sweep as ### **"20 scoped hits → 0, across 13 files."** The tracked evidence
does not reproduce it: **7 hits in 4 files** at `9641627`, and `relay`'s only old-term occurrences are the
compliance reports **quoting** the term. The commit message carries the **checked** figure; the attempt
record's line is ### **left exactly as written** — repairing it would be new content, which this ferry excludes.

*The corpus's own laws this sits under:* **a magnitude is not a definition** · **authority is not accuracy** ·
**verification probes take exact strings, never paraphrases.** ### **The number was written from the sweep's
own account of itself rather than from a count. AUTHOR'S CALL WHETHER TO CORRECT IT IN PLACE OR STRIKE-VISIBLY.**

---

## §6 — ONE MORE THING THE PUSH MADE INACCURATE

`relay`'s GitHub description reads ### **"session relay - reports only, no research content."** With 244
reports now public — including twenty attempt-1 sittings carrying their numerics, the `δ/L` measurements, and
the witness-lattice separations — ### **that description is no longer true, and it is the first thing a
stranger reads.** Not changed by this pass (a repository setting is outside a commits-only ferry). **Filed.**

---

## CLOSING — WHAT RETURNS FOR THE AUTHOR'S WORD

**REMOTE SHAs, READ BACK FROM THE REMOTE:**

```
PLACE-papers  origin/main : 32760a2cce0b0d967402a13cd474492b77a607b8   (private)
relay         origin/main : 6285c75bbd96ac312923c906ddc47ac96774a501   (public, 244 reports)
relay         local  main : one commit ahead — the two HELD carrier-build acts
```

### **NEW SINCE THE AUDIT, EACH WANTING A WORD**

1. ### **RELEASE THE TWO CARRIER-BUILD ACTS?** Held pending counsel. Committed, safe, uncirculated.
2. ### **CORRECTION TWELVE'S "20 → 0 ACROSS 13 FILES"** — the count is 7 in 4. Correct in place, or strike-visibly?
3. **`INSTRUMENTS.md`'s two stray CRLF** — normalize, or leave and annotate the mirror instrument?
4. **`relay`'s repository description** — no longer true of its contents.

### **THE FOUR STANDING RULINGS, UNMOVED BY THIS PASS**

1. ### **`SIDE-effects` REPAIR ROUTE** — (i) honest `INTERFACES` on named premises *(preferred — preserves the
   citation)* vs (ii) `SHELL` + no-cite guards **verified at every citing site**. ~1–1.5 sittings.
2. ### **DAY-1 DIGESTION SCOPE** — (A) annotations-only *(~1 sitting; the standing recommendation)* vs
   (B) back-matter Correspondence subsections *(~2 sittings)*.
3. ### **THE TWO PROSE RULINGS** — the P1 six-counts opening and the P2 caveat placement; neither ever resolved
   to a corpus locus.
4. ### **`internal/` + `meta/` RATIFICATION** — both stand `REGISTRY-SILENT`. ### **Now load-bearing:
   `internal/` holds counsel-facing material as of `32760a2`.**

**`h2` UNCHANGED. `WIDEN` PAUSED. RAIL DID NOT MOVE. NOTHING DEPOSITS.**
