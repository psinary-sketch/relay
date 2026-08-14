# THE FOUR RULINGS EXECUTE — CLOSE · ### AND ONE CONFLICT RETURNED UNRESOLVED

**Relay report · 2026-08-14 · author-called · nothing deposits**
**`h2` UNCHANGED. `WIDEN` PAUSED. RAIL DID NOT MOVE.**

```
PLACE-papers  origin/main : 388c7e7ef6d151c441ac371624e78805d7400c57   (private)  VERIFIED
SIDE-window   origin/main : ecd5cf7  (PUBLIC, tag v0.1.0)              VERIFIED
SIDE-spinor   origin/main : 520abe7  tree CLEAN, FROZEN                VERIFIED
relay         origin/main : (this report)                              local +1 HELD
mirror        22 / 22 rows COHERENT at 388c7e7
```

---

## §1 — ### ITEM 1 STOPPED. THE RULING CANNOT BE EXECUTED AS WRITTEN.

**Four of five items are done. This one is returned, per the ferry's own instruction:
*"conflicts, if any emerge mid-execution, STOP and return rather than resolve unilaterally."***

### **THE RULING WAS: restate `grh_exclusion` and `no_ls_zero` as INTERFACES-on-named-premise.**

### **THE FACTS, READ BEFORE ANYTHING WAS TOUCHED:**

**(1) THE TWO TERMINALS DO NOT EXIST ON ANY LIVE BRANCH.** Not on `w-ladder-skeleton` (the current head),
not on `main`, not on `origin/main`. They exist only at the **tag** `phase-1.5-module-1-v2`.

**(2) WHERE THEY DO EXIST, THEY ARE ALREADY EXACTLY THE SHAPE THE RULING ASKS FOR.** At the tag:

```lean
theorem grh_exclusion (balance_forces_half sigma_ne_half : Prop)
    (_h_balance : balance_forces_half)
    (h_implies : balance_forces_half → ¬sigma_ne_half) :
    ¬(OffLineGRH balance_forces_half sigma_ne_half) := ...
```

### **That IS an interface on named premises.** *Its mathematical content is taken as explicitly named `Prop`
hypotheses and discharged by the supplied implication — the construction route (i) describes.*

**(3) AND A PRIOR AUDIT ALREADY EXAMINED THAT EXACT SHAPE AND REJECTED IT.** The live `Structural.lean`
header says so in the corpus's own words:

> *"A Phase S.2–S.4 audit found those skeletons were either True-valued stubs (e.g. `gapped := fun _ => True`)
> or **opaque-Prop templates (a theorem taking its conclusion's content as a `Prop` hypothesis and discharging
> by the supplied implication)**. They compiled with 0 sorry and 0 axioms but **said nothing about their named
> problems**, so they have been retired here."*

**(4) THE WITHDRAWAL WAS EXECUTED TWO MONTHS AGO AND LANDED.** `OPEN_TRAILS` L1574: *"W-2 — withdraw option
**EXECUTED** for the `SIDE-effects` shells (2026-06-16; **landed on `main` 2026-07-13**). `Structural.lean`:
34 declarations → 3."*

> ### **SO BOTH ROUTES THE RULING CHOSE BETWEEN WERE ALREADY RESOLVED — BY A THIRD ACT, TWO MONTHS AGO.**
> *Route (i) would **re-create** the construction a prior audit retired for saying nothing. Route (ii)'s
> no-cite guarding is what withdrawal already achieved by removing the declarations outright.*

### **THE BOARD ITEM THAT GENERATED THIS RULING WAS STALE IN TWO SEPARATE WAYS.** *It read
`grh_exclusion` / `no_ls_zero` at `fun _ => True`.* **Neither was ever `fun _ => True`** — that was the
`TypeD` skeleton — **and both had been retired outright before the board was written.** *The only live
`fun _ => True` strings in the repository are inside comments describing what was retired.*

### **WHAT IS ACTUALLY LIVE, AND IT IS NOT WHAT THE RULING ADDRESSES**

**The citing-site census, run by scan and not recall:**

| finding | |
|:--|:--|
| ### **manuscripts citing `grh_exclusion` / `no_ls_zero`** | ### **ZERO.** *No paper cites either terminal. The 14 spectral-cluster hits are `SIDE-effects` citations generally, none to these two.* |
| ledger mentions | `OPEN_TRAILS` L1550, L1574 · `VERIFICATION_LOOM` L1428 — **all three record the retirement itself**, correctly |
| ### **the one live residue** | ### **`VERIFICATION_LOOM` L106–L107 — two Correspondence rows still listing both terminals as *"⊘ scaffold-pattern"*, as though they were present-but-weak.** *They are absent.* |

### **THAT IS THE REAL DEFECT AND IT IS A ONE-LINE REPAIR — but it is "correct two stale ledger rows", not
"restate two terminals", so I have not made it.** *Returning it rather than quietly substituting a different
repair for the ruled one.*

**THE BRANCH'S 6 UNTRACKED FILES, DISPOSITIONED BY CONTENT READ — REPORTED, NOT DELETED:**
all six are **post-retirement** artifacts. `Structural.lean.bak/.bak2/.bak3` (2026-06-16) each carry
**3 declarations and neither retired terminal** — they are intermediate save-states *of the withdrawal
itself*. `README.md.bak`, `Milestones.lean.bak`, `AxiomCheckM1.lean` likewise superseded. ### **No unique
content in any of them. They are safe to delete on your word — held because the branch's fate is part of
what is being returned.**

### **THE QUESTION THAT ACTUALLY NEEDS YOUR RULING NOW:**

> ### **1.5's headline is not "which repair route" — it is "the repair already happened; does the branch
> `w-ladder-skeleton` merge to `main`, and do the two stale loom rows get corrected?"**

---

## §2 — RULING 2: DAY-1 DIGESTION, ANNOTATIONS-ONLY ✓

**All nine Day-1 documents gained a dated, provenance-kept `ERA ANNOTATION (2026-08-14)`** in back matter,
in the exact form of the 2026-08-12 precedent.

| paper | era finding landed |
|:--|:--|
| `A_Place_to_Stand` | **sign-face registers** — arrangements IDENTICAL, no convention gap; `W_∞` not sign-definite; the `−2` orphan solved as `W_pole` |
| `Exhaustive_Enumeration` | **the two-kinds windows, NOW COMPILED** — `SIDE-window` `v0.1.0`, with its four non-claims carried |
| `ONE_PAGE_PROOF` | **the S-table `v0.1 → v0.3`** — `S4` → multiplicative; `S1` → `S1a/S1b/S1c`; `S3` → `S3a/S3b`; `VACUOUS` ratified |
| `Seven_Mechanism_Classes` | **placement-mute** — placement tracks the object's own monoid, not the ambient ring |
| `Silence_of_Foundations` | **the `S5`-silence naming** — *blindness names a defect of the instrument; silence names a property of the reading* |
| `Spectral_Inertness` | **the same, in the instrument register** — non-separating-over-`S5` is the exact analogue of `κ = 0` |
| `Third_Identity_Element` | **the monoid finding** — a **second, independent** reason to keep element-level assignments off the canonical shelf |
| `Which_Structure_Confines` | **the monoid finding at Epstein** — `Z_Q` at `h > 1` has **no generating monoid at all**; the shard has no monoid to carry a product |
| `HELD_F7_two_clause_reframe` | ### **that the era did NOT move it** — filed so later activity elsewhere is not mistaken for movement here |

### **ADDITIVE, PROVEN FROM THE DIFF — not asserted:**

| check | result |
|:--|:--|
| seven of nine papers | ### **`+6 / −0`** |
| the only `day1/` deletions | ### **the two ruled relocations, and nothing else** (19 lines `P1`, 1 line `P2`) |
| `§25.8` Kernel Concordance | ### **UNTOUCHED — md5 `6cda8b6…` identical before and after**, 33 lines |
| `ERRATA.md` | ### **UNTOUCHED.** *Nothing published was wrong.* |
| `DEPOSITED` / `LIVE` divergence note | ### **UPDATED** in `REGISTRY` with all of the above |

---

## §3 — RULING 3: THE TWO PROSE EDITS ✓

**`P1` — the monograph opens on its claim.** *"How This Monograph Is Organized"* moved from the head of
Part I to back matter as ### **Appendix H**; the vacated site now carries the one-sentence claim and a
pointer. ### **All EIGHT paragraphs verified BYTE-IDENTICAL after the move** — relocative, not rewritten.
*A stranger now meets the argument before the architecture, which was the whole of the ruling.*

**`P2` — the caveat meets the table.** `Third_Identity`'s non-canonicity caveat lifted out of the **Theorem
statement** — where it sat as a parenthetical — and placed **directly under the class ↔ field table it
qualifies.** ### **476 bytes, verbatim, exactly one occurrence, verified sitting under the table.**

---

## §4 — RULING 4: `internal/` + `meta/` RATIFIED `CENSUS-ONLY` ✓

REGISTRY's *"one line, awaiting the author's ruling"* is now **a ruling with its scope note**: counted in
every census · **no `REGISTRY` row** · **never published** · ### **provenance preserved in full — census-only
is not archival and not deletion.**

> ### **AN ABSENCE THAT IS RULED CANNOT BE MISTAKEN FOR AN OVERSIGHT BY THE NEXT SURVEY.** *And it is now
> load-bearing: `internal/` holds the counsel-facing disclosure documents, for which "out of release scope,
> provenance preserved, never published" is exactly the right disposition.*

---

## §5 — RULING 5: THE PROSE SITES ✓ · ### AND THE LIST WAS A FLOOR, AGAIN

`CONSTANCE` L2702 and `PATHS` L211 re-cut to the **standing qualifier form** —
`**[Qualified: …]** *[corrected 2026-08-14 · convergent-identification ruling]*` — matching L2681 / L2698 /
L2887 exactly rather than approximately.

### **THE EXTRA SCAN FOUND THREE MORE SITES THE WORK-ORDER NEVER NAMED:**

| site | what it said |
|:--|:--|
| ### **`SPIRAL_MAP` L98** | the federation table's `SIDE-spinor` row: *"orbit collapse at σ=1/2"* |
| ### **`meta/W1_DESCRIPTION_DRAFTS` L159** | the same phrase in ### **outward-facing description text** — the register where an unqualified claim travels furthest |
| ### **`THE_UNCONDITIONAL_SURROUND` L171** | `spinor_forces_half` listed among *"independent checkpoints"* under a row reading *"five voices force it"* — ### **the heading's verb governs the five `SIDE-kernel` voices; the checkpoint list inherited it without earning it** |

**All repaired.** *`W-ORD-PROSE-OUTRUNS-ROW` named four sites; ### **seven existed.***

> ### **THE OPERATIONAL FORM, FILED IN THE LOOM: WHEN A CORRECTED ROW OUTRUNS ITS PROSE, SCAN FOR THE
> TERMINAL'S IDENTIFIER *AND* FOR THE CLAIM'S PHRASING — SEPARATELY.** *L98 and L159 never use the word
> "exact"; L2702 never names the terminal. **Each is invisible to the other's scan**, which is why one scan
> closed the order as complete and two did not.*

---

## CLOSING — FOR THE AUTHOR'S WORD

### **DONE:** rulings **2, 3, 4, 5** — landed, pushed, remote SHA read back, mirror rebuilt and 22/22 coherent.

### **RETURNED UNRESOLVED:** ruling **1**. *The repair it orders was already performed, by a different route,
two months ago; executing it as written would re-create a construction a prior audit retired for saying
nothing about its named problems.* ### **Nothing in `SIDE-effects` was touched.**

### **STILL HELD:** the two `W-CARRIER-BUILD` acts — committed at `relay` tip, unpushed, absence from the
public tree re-verified against the remote. **Release condition: counsel, then your word.**

### **QUEUED AS THE NEXT EXECUTOR SITTINGS, per your closing**

1. **Phase 1.1 — annotations verify** *(re-read the nine new notes against their sources at content)*
2. **Phase 1.1 — Apostol Ch. 11 page-level** *(executor-runnable; needs library access; supports a negative,
   so it cannot manufacture a merge)*
3. **Phase 1.5 — the fifteen-file basecamp re-sync** *(`D:\PLACE-phase1.5\keystones` vs `PLACE-papers`,
   matched by ### **TITLE-LINE CONTENT, never by filename** — the method the ferry fixed, and it matters)*

**`h2` UNCHANGED. `WIDEN` PAUSED. RAIL DID NOT MOVE. NOTHING DEPOSITS.**
