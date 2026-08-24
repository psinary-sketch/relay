# THE FIGURE VALUES DOSSIER

## ### **THIS SEAT BREACHED THE DECONFLICTION IT RATIFIED ONE ACT EARLIER — `git add -A` SWEPT IN EIGHT PATENT-SEAT FILES AND PUSHED THEM. REPAIRED NON-DESTRUCTIVELY, HISTORY NOT REWRITTEN, AND A GUARD BUILT AND TESTED AGAINST THE EXACT BREACH.** ### **THE DOSSIER IS BUILT: 8 CONFIRMED-AT-OWNER · 1 DIVERGES · 11 NO-OWNER-FOUND · 8 UNVERIFIED-AS-EXACT · 1 NAME-COLLISION HAZARD · 3 DERIVED CHECKS RUN AND PASSED.** ### **THE THING A RENDERER MUST NOT GET WRONG: THE FILING'S `C₁` AND THE OWNER'S `C⁽¹⁾` ARE DIFFERENT MATRICES OF DIFFERENT SIZES.** CORE UNTOUCHED, THIRTEEN CONSECUTIVE ACTS. NOTHING DEPOSITS.

**Relay report · 2026-08-24 · ferry-executed (part 1 of 1, receipt confirmed in
full, Rule 1) · Rules 3/4/5 · the b148 run-registration banked before any reading
at `28a38d5` · **one breach, repaired** · **one divergence from the ferry's
premise** · nothing deposits.**

---

## §1 — THE BREACH, FIRST

**What happened.** The C3/C4 commit used `git add -A` in PLACE-papers and staged
### **eight untracked files belonging to the patent seat** — seven PZONE figure
SVGs and `PZONE_FIGURES.md`. ***Only two of that commit's ten files were mine.***
Committed and pushed as `49cd156`.

**The ruling breached was ratified one act ago, at b147, by this seat:** *"the
patent seat writes only within the patent-package tree … the research seat owns
the ledgers, the keystones, and HANDOFF; **any edit either seat needs across the
line routes to the author**."* Nothing was routed to anyone.

> ### **AND THE COMMIT MESSAGE MADE IT WORSE.** It ended: *"The patent package was READ, NEVER WRITTEN, per the deconfliction."* ### **That sentence was false at the moment it was written, in the same commit that falsified it.** ***Nothing in the closing sequence compares a commit's self-description against its own file list*** — so a claim of compliance asserted inside the act that breaches passes every check this record owns.

**The repair, chosen non-destructive.** `git rm --cached` on the eight paths →
### **untracked, left on disk byte-for-byte untouched** (md5 set captured before
and after; diff empty). The patent seat's files are back in exactly the state they
were in, and ### **the patent seat keeps the decision about its own work.**
### **The history is not rewritten** — ***a breach repaired by force-push is a
breach the record cannot learn from.***

> ### **THE MECHANISM, WHICH IS THE PART WORTH BUILDING AGAINST.** `git add -A` stages the whole worktree, and I used it safely for many acts ### **because I was the only writer.** ***The deconfliction changed the ground under a habit, and the habit did not notice.*** ### **A command that was safe under one-writer assumptions is not safe under two, and nothing about the command changed to signal it.**

**The guard, built not praised: `tools/place_add.py`.** Refuses `-A` / `--all` /
`.` / `-u` outright; refuses any path under a foreign-seat prefix; stages only
what it is given. ### **Not via `.git/info/exclude`, because both seats share one
clone** and excluding the patent tree would break the *patent* seat's ability to
stage its own work — ### **a guard must constrain the seat that needs
constraining, not the repository.** ***Tested against the exact breach before
entering service, per the nursery convention:*** `-A` **REFUSED** · the patent
path **REFUSED** · my two ledgers **STAGED**.

## §2 — THE DOSSIER

`relay/data/b148_figure_values_dossier.md`, in this seat's tree. ### **It crosses
to the patent seat through the author only — this seat does not deliver it.**

**Sources:** the three filed specifications read at content. ### **The package's
reconstructions were not consulted, not cross-checked against, and are not cited
even where they might agree** — *a reconstruction that agrees adds nothing the
filing did not give, and citing one launders an unreliable source into a verified row.*

| Class | Count |
|:--|--:|
| **CONFIRMED-AT-OWNER** | 8 |
| **DIVERGES** (descriptor only; values confirmed) | 1 |
| **NO-OWNER-FOUND** (filing-only, properly so) | 11 |
| ### **UNVERIFIED-AS-EXACT** (tilde law fired) | ### **8** |
| **Name-collision hazards, full prominence** | 1 |
| **Derived checks run and PASSED** | 3 |

### **THE HIGHEST-CONSEQUENCE FINDING.**

The filing's FIG. 4 labels its 3×3 matrix **`C₁`**. The owner
(`phase2/quantum/TRIVIUM_CODE_VERIFICATION.md`) carries **both** a 3×3 `C` (§3,
weight-1 errors `{E_P, E_T, E_O}`) **and** a 4×4 `C⁽¹⁾` (§4.1, `{I, E_P, E_T,
E_O}`) with different entries. ### **`C₁` and `C⁽¹⁾` are typographically
near-identical and are different matrices of different sizes.** ***A renderer told
"C₁" who checks the owner lands on `C⁽¹⁾` and draws a 4×4 matrix the figure does
not describe.*** **FIG. 4 Matrix A is the 3×3 `C`.**

**Two more things the filing's figure text does not carry:** the owner's matrix is
### **exactly symmetric** where the filing says *"approximately symmetric"*
(**DIVERGES on the descriptor; the values 0.921 / 0.974 / 0.941 are CONFIRMED**,
no resolution attempted); and ### **the entries are conditioned on `δ = 0.3`** —
*they are not universal constants and the figure is unreproducible without the annotation.*

### **TWO PAIRS THAT LOOK LIKE ERRORS AND ARE NOT.** `[[7,1,3]]` is the
**physical** Steane code; `[[7,1,5]]` is the **effective** parameter at `S = 3`
via `d_eff = 2S − 1` — *both CONFIRMED-AT-OWNER, both in the filing, different
objects.* And `Q ≥ 2000` is the **claim limitation** (Claims 3, 12) while
`Q ≈ 2000` appears **only in FIG. 6**, describing the drawn spectrum. ### **A
renderer must not swap either pair.**

### **THREE DERIVED CHECKS — COMPUTATIONS, NOT CITATIONS.**

1. ### **Every filed Fano line XORs to `(0,0,0)` over 𝔽₂, and every point lies on exactly three lines.** The filed incidence structure is a correct PG(2, 𝔽₂).
2. P-ZONE **FIG. 2 and FIG. 3 cross-check exactly** once 1-indexed rows are matched to 0-indexed qubits. *A renderer may draw from either and they agree.*
3. PROV-1's own arithmetic holds: `5,502 + 4,298 + 1,575 = 11,375` exactly; `881/10,494 = 8.4%` exactly; ### **and the filing states its own overhead against itself.** ***One rounding caught: the stated 48% reduction is 47.57% — draw it as ~48%.***

### **A DIVERGENCE FROM THE FERRY'S PREMISE.** ### **The TECHNE drawing conventions are not locatable at content.** Searched across the corpus; `internal/TECHNE_ELEMENTS.md` and `TECHNE_INTAKE.md` exist and carry no drawing standard. ### **No standard was invented.** *If they live in the patent seat's tree, this seat did not locate them.*

## §3 — THE APPROXIMATION-MARK LAW (strikeable, ratified)

### **An approximation mark in a live ledger row is a debt: it resolves to a read, or the row carries `UNVERIFIED` explicitly.** Founding instances: ***"~August 2027"*** (cost: **four months** on a patent wall) and ***"(Wanted-Poster-Technique?)"***.

> ### **WHY A MARK IS WORSE THAN A BLANK.** *A blank cell is visibly missing and gets filled.* ### **A marked cell looks filled.** The caveat is exactly the part a later reader drops — ***because the row still parses, still tabulates, and still answers the question it was asked.***

> ### **AND IT IS NOT A BAN ON APPROXIMATION.** It governs **ledger rows, not source documents**. A filed spec may properly say *"approximately 150mm"*; when that value enters a ledger it enters **flagged**. **First use, the same day: eight dossier values flagged `UNVERIFIED-AS-EXACT`.**

## §4 — SCORING AND AUDITS

### **THE P1 FORK WAS BADLY POSED BY ME, AND NEITHER SEAT CLEANLY LANDS.** I predicted at least one ferry-named value would not appear as stated. ### **Every ferry-named value checked out**, and the closest thing to a miss — `Q ≥ 2000` vs FIG. 6's `Q ≈ 2000` — ### **is not a miss at all, both being in the filing in different roles.** ***Navigator marginally ahead: the genuinely dangerous findings — the `C₁`/`C⁽¹⁾` collision, the `δ = 0.3` condition, the 48% rounding — are all in values the ferry did NOT name.***

```
  stems scanned : gap, blind   |   hits 0   |   live uses 0   |   VERDICT: CLEAN
```
*One live use was caught mid-act in my own dossier and corrected — the b146 windowed matching working as designed.*

**DEVIATIONS:** ### **one, and it is a BREACH rather than a deviation** — recorded above. **DIVERGENCES:** one — the TECHNE conventions.

## §5 — THE RECORD AND PINS

> **PIN LINE (post-push read-back, `ls-remote`, not push output):**
> `relay origin/main = 65f58d2ff32aa879417fe445cc38d06c7282623a` (this act; the
> registration `28a38d5` its ancestor; pushed from `push-figure-values` per
> Rule 4.10) · `PLACE-papers origin/main =
> 084efbe12c18478b44e575b97f43a0c697a354e9` ### **(the CORRECTION commit — the
> breach at `49cd156` and its repair both stand in the log)** ·
> `SIDE-global-section origin/main = dc4c32e56275e1251e0daea094ab4167eee289b9`
> (**UNTOUCHED**; Core **271/271**, rows 1–68; tag `v0.1.0` = peeled
> `706a81b9e329e220a6448b4296e5cc42c9433670`, unmoved) · `SIDE-kernel origin/main =
> 0256e9e1297fcf3bc6bd2a6b15d7c3d986a67164`, deposit `v1.5` = peeled
> `0e5233f011533d09e4799107394c216a915028a1`. **HELD:**
> `6eada6a5ca6368a70b7c5afcbb80224ec16ac3a4`, **NOT an ancestor**; all eight
> HELD-unique paths **ABSENT**, checked per-path.
> **MIRROR:** ### **`mirror-refresh-2026-08-24-s.zip` is the one to load** — both
> clauses CLEAN (build HEAD `084efbe` = `ls-remote` `084efbe`), **12 of 12
> mechanical probes PRESENT.**
> *This pin-line commit's own SHA is stated in the closing message.*

## FOOT

**The author carries the dossier to the patent seat for the batch renders — this
seat does not deliver it. The twenty-eighth seam close at the cadence; the
boundary act and the methodology day at the author's schedule; the locks last.**

**`h2` UNCHANGED. THE REGISTER SENTENCE UNTOUCHED. NOTHING PROMOTED. NOTHING
DEPOSITS. NOTHING CIRCULATES.**
