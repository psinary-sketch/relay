# REPAIRS + THE UNBLOCKED PHASE FERRY — CLOSE

**Relay report · 2026-08-14 · author-called · nothing deposits**
**`h2` UNCHANGED. `WIDEN` PAUSED. RAIL DID NOT MOVE.**

```
PLACE-papers  origin/main : a0c97343e61851540701fb3488c0387fb107ff52   (private)  VERIFIED
SIDE-window   origin/main : ecd5cf736e659b0e961601d7d4d78ae9d4b00b9a   (PUBLIC, NEW)  VERIFIED
SIDE-window   tag v0.1.0  : ecd5cf736e659b0e961601d7d4d78ae9d4b00b9a              VERIFIED
SIDE-spinor   origin/main : 520abe7a6b7d63bff104fd9838f3179d7d1117d0   tree CLEAN
relay         origin/main : (this report)                             local +1 HELD
```

*Every SHA above read back with `git ls-remote`, never from push output.*

---

## §1 — CORRECTION THIRTEEN · `7244fe8`

Correction 12's figure — *"20 scoped hits → 0, across 13 files"* — is **struck visibly, not overwritten**,
and replaced with the measured count: ### **7 hits in 4 files at `9641627` → 1 at `origin/main`**, the one
residual being correction 12's own quotation, classed `PROVENANCE-QUOTATION`. Attributed **EXECUTOR-CAUGHT**.
The table gains row 13; the heading is repaired from "THE ELEVEN CORRECTIONS" to **THIRTEEN** — it had read
*eleven* while already carrying twelve rows.

### **LAW MINTED: CORRECTIONS ARE WRITTEN FROM COUNTS, NEVER FROM A SWEEP'S ACCOUNT OF ITSELF.**

> ### **A PASS CANNOT COUNT ITSELF: it knows what it intended to cover, and that is exactly the quantity the
> count is supposed to check.** *And a correction's figure is the one number a reader has no independent
> reason to doubt — it appears in the place where errors are confessed, so a miscount there borrows the
> credibility the correction was written to earn.* **The count is run afterward, as a separate act, against
> a named ref: "20 hits" is not falsifiable; "7 hits in 4 files at `9641627`" is.** Kin filed: *a magnitude
> is not a definition* · *authority is not accuracy* · *probes take exact strings*.

**The law fired against its own author within the hour** — §3 below.

---

## §2 — CRLF · `83e1c85` · ### THE DEFECT WAS 52 FILES, NOT ONE

`INSTRUMENTS.md` was the symptom; `core.autocrlf=true` with no `.gitattributes` was the disease.

| | |
|:--|:--|
| tracked `.md` with **disk ≠ blob** before | ### **52 of 244** |
| after | ### **0 of 244** |
| what `git add --renormalize .` restaged | ### **`.gitattributes` alone — proving no content moved** |

**What was done:** `.gitattributes` gains `* text=auto eol=lf` so checkout matches storage permanently; the
51 CRLF working copies were rewritten to LF ### **each only where the result equalled its blob EXACTLY,
never guessed — 0 skipped.**

### **NO CONTENT CHANGED ANYWHERE.** *Every blob is bit-identical to what it was; only the bytes on disk
changed, and they changed to match.*

**Mirror rebuilt at `a0c9734` and re-verified three ways — manifest md5 vs committed blob vs disk:**
### **22 / 22 COHERENT.** *The `INSTRUMENTS.md` row that failed the previous build now reproduces.*

---

## §3 — RELAY DESCRIPTION + COUNSEL INVENTORY · `c9ca93c`, `aa7d5f3`

**Description reworded** *(metadata only — nothing published, unpublished, added or removed; exposure
unchanged)*:

> ~~session relay - reports only, no research content~~
> ### **session reports and bench data for the PLACE TO STAND programme; no manuscript or kernel research content**

**Counsel memo §1 gains `relay`** as ### **existing-public fact, not a new act**: public since **2026-07-10**,
**245 reports on the remote at read**, carrying bench numerics — measured tables, eigenvalue computations,
fitted laws with residuals, failed runs kept as failures. ### **If any of the six provisionals is supported
by measurements that also appear in `relay`, that publication is an existing fact with a date, not a decision
still open** — which is what question 2 asks about. No legal characterization offered.

### **THE NEW LAW FIRED AGAINST ITS OWN AUTHOR, SAME DAY.** *The table row was written from the live remote
(245); the prose sentence beneath it still said 244, the count taken before the close report was pushed.*
**Caught by re-reading the numbers against the remote rather than against the paragraph just written, and
corrected in `aa7d5f3`.** ### **In a document prepared for counsel the tolerance for an unchecked number is
zero.**

---

## §4(a) — `SIDE-spinor` → ### FROZEN · `a0c9734`

**THE TWO COMMITS PAST THE PIN, READ BY CONTENT → RULED `KEEP`.**

`4f5848d` and `520abe7` add `SIDESpinor/SpinorLeg.lean` (the metaplectic quarter-twist route to `−1`), its
axiom probe, and one import line: ### **`+76 / −0` across 3 files — PURELY ADDITIVE.** *They do not touch
`Spinor.lean`, therefore touch no declaration the pin cites.* The pin `b235bc6` remains a true ancestor of
`HEAD` and every citation resolves unchanged; the author had already ruled `LAND` on 2026-07-28.

> ### **REVERTING WOULD DELETE A COMPILED SECOND ROUTE TO BUY A COSMETIC EQUALITY OF TWO SHAs.**

**THE 2026-08-10 CORRECTION, SWEPT AT EVERY CITING SITE.** `spinor_forces_half` is
`(w : ℂ) (h : Complex.I * w = w) : w = 0` and **does NOT conclude σ = ½** — σ = ½ additionally requires the
stipulation that `w` IS the centred coordinate `σ − ½`, which no kernel proves.

| site | state |
|:--|:--|
| `CONSTANCE` L2681 · L2698 · L2887 | ### **already carried it** ✓ |
| `PATHS` L211 | qualifier stood 3 lines above at **(a)** but ### **NOT on the bullet a citer copies** — carried inline; closes `W-ORD-PROSE-OUTRUNS-ROW` site 4 |
| ### **`CONSTANCE` L2702** | ### **A FIFTH SITE — *"This identification is exact"*, unqualified, NOT among the four the work-order named.** Struck visibly, qualified in the metaplectic register |

> ### **THE FIFTH SITE IS THE FINDING OF THIS FERRY. The standing law that A WORK-ORDER'S SITE LIST IS A
> FLOOR, NOT A CENSUS fired against the very work-order that would otherwise have closed as complete.**

**`_AuditProbe.lean` — DISPOSITIONED BY CONTENT, DELETED.** 117 bytes, 2026-07-11, printing axioms for
`spinor_forces_half` and `half_iff_centered_zero` — ### **both already printed by the TRACKED
`AxiomCheck.lean`, which covers all nine terminals.** A strict subset of an instrument that already existed,
invisible to every audit by the untracked-artifacts law, and the sole reason the tree was dirty. *Content
recorded above before deletion; nothing lost.*

### **PHASE 1.2 IS FROZEN** — 1.2-A `8019d9d` · 1.2-B `2efe9f2` · 1.2-D `d5f33b4` all `DEPOSIT-PIN` =
`WORKING-HEAD`; ### **1.2-C frozen WITH its exception, written down rather than averaged away.**

---

## §4(b) — CLUSTER ENUMERATION *(enumeration only; no research act)*

**The census's one un-run row, now run.** 29 documents across three clusters.

### **SIMPLICITY — 6 documents**

| doc | version | kernel state |
|:--|:--|:--|
| `SIMPLICITY_OF_RIEMANN_ZEROS` | `v1.1.2` | 17 pin sites, **all resolve** (rowgen) |
| `ALL_ZEROS_SIMPLE` | `v1.1.2` | SCOPE-DROPPED (archival) |
| `CASE_FOR_SIMPLICITY` | `v1.1` | READY |
| `CONVERGENT_ARGUMENTS_SIMPLICITY` | `v0.4.0` | READY |
| `TRACE_FORMULA` · `DERIVATIVE_IMAGINARY_THEOREM` | `v1.1.2` / — | — |

**Kernels cited:** `SIDE-lv-conservation` (20) · `SIDE-kernel` (13) · `SIDE-grh-transfer` (3) · `SIDE-simplicity` (2).
**OPEN CONCLUSION:** ### **simplicity itself is unproved within ZFC** — *"Layer 1 reduces RH to simplicity but
does not address simplicity itself. Within ZFC, simplicity remains open. This is the honest ZFC position."*
The reverse direction (simplicity ⟹ RH) rests on Conservation; the forward direction was already conjectural.

### **SPECTRAL — 10 documents · ### the cluster carrying the open `sorry`s**

| open conclusion | state |
|:--|:--|
| ### **`C₃` theta transformation** `∀ t > 0, Φ(1/t) = √t·Φ t + (√t−1)/2` | ### **OPEN (`sorry`)** — Mathlib has the FE for `Λ`; the Φ-side is not derived |
| ### **`C₆` holomorphic extension to `Re t > 0`** | ### **OPEN (`sorry`)** — needs holomorphy of `evenKernel 0` in `t` |
| **the constants inequality `γ + 2 ≥ ln(4π)`** | ### **NOT PROVED** — wants a sharper `γ` bound than Mathlib carries |
| `C₇` split / the price of the Hadamard input | Appendix E; the Phragmén–Lindelöf route was hunted, not closed |

**Kernels cited:** `SIDE-lv-conservation` (43) · `SIDE-kernel` (38) · `SIDE-grh-transfer` (25) ·
`SIDE-interfaces` (14) · ### **`SIDE-effects` (14 — the scaffold repair still awaits its route ruling)** ·
plus `yang-mills-formation`, `li-map`, `bsd-formation-transfer`, `silence-principle`, `class-number-anomaly`,
`trivium`, `meta`, `dirichlet-mod-24`, `bijection`.

### **STRUCTURAL — 13 documents**

| open conclusion | state |
|:--|:--|
| **Spectral Volume conjecture** `λ = n₁ × n₂ × n₃` | verified for `ξ` (`λ = 12`); ### **not proved in general** |
| **`E_DIFFICULTY_CONJECTURE`** | forward direction established; ### **skeleton kernel-verified only** (`Kernel/Cascade/SieveCeiling.lean`) |
| **TYPE III (P vs NP, CH, Halting)** | ### **classified OUTSIDE the methodology's scope**; whether any can be brought inside is open |

**Kernels cited:** `SIDE-kernel` (23) · `SIDE-compression` (10) · `SIDE-silence-principle` (6) · `SIDE-meta` (2) ·
`SIDE-lv-conservation` (1).

### **EVERY CITED KERNEL EXISTS.** *An initial scan flagged three absent names —* `SIDE-interface-split`,
`SIDE-amenable`, `SIDE-exclusion-applicable`. ### **All three are scanner artifacts of my own regex, not
missing repositories:** `SIDE-amenable` is a defined VOCABULARY term (*"X is SIDE-amenable if it has a finite,
explicit specification…"*), and `SIDE-interface-split` is `SIDE-interfaces` clipped against the Lean
declaration `interface_split`. ### **Reported as a false alarm rather than left as a finding.**

---

## §4(c) — `SIDE-window` `v0.1.0` · ### THE LEMMA A KERNEL, PUBLIC

**`ecd5cf7`, PUBLIC, tagged and frozen at creation (`DEPOSIT-PIN` = `WORKING-HEAD`).** Vanilla Lean 4
`v4.29.1` — **no Mathlib, no Batteries, no dependencies.** Eleven terminals, every one closed by `decide`,
and every one reporting ### **`does not depend on any axioms` — not the standard three, but NONE AT ALL.**

`lemmaA : primePowersLE 2 = [2]` · `window_prime_free : primePowersLT 2 = []` ·
`window_one_prime : primePowersLT 3 = [2]` · the two maximality terminals · `primePowers_below_ten` ·
the counting table · the definitions pinned by examples.

### **WHAT COMPILING LEMMA A DID NOT BUY, IN THE DOCSTRING AND THE README SO IT TRAVELS WITH THE SOURCE**

* ### **NOTHING ABOUT ζ, `h2`, OR ANY OPERATOR INEQUALITY.** *Nothing here bears on the sign of `W_∞ − W_2`.*
* ### **NOTHING ABOUT REAL INTERVALS.** *The corpus states Lemma A over `λ² ∈ (2,3)`; the kernel proves the
  arithmetic residue `primePowersLE 2 = [2]`. The bridge is one line and* ### **is not formalized.**
* ### **THE WINDOWS ARE HALF-VACUOUS** — *every prime power is `≥ 2 > 1 ≥ 1/L`, so the lower endpoint never
  binds.* **The multiplicative framing suggests two constraints; there is one.**
* ### **MAXIMALITY AT INTEGER BOUNDS ONLY.** *Real `L` needs the step-function argument, which is standard
  and is not in the repository.*
* **`IsPrime` is trial division defined in-file**, not Mathlib's `Nat.Prime`.

### **THE `δ/L` LAW IS ABSENT BY DESIGN — comment only. No definition, no statement, no theorem.** *It is
`MEASURED-AT-BANK`, never proved, its two largest rows extrapolating past Lemma 5.2's un-re-derived `(1,3]`.*
### **A Lean file carrying a NAME for it would invite a citation it cannot support.**

**PRE-PUSH CLEARANCE, as the ferry required:** identifier sweep over every tracked file for carrier-spec /
TECHNE / patent terms → ### **ZERO HITS → eligible for PUBLIC.** *The first sweep did trip, on my own
README's disclaimer sentence naming the terms in order to deny them; the line was reworded so the sweep is*
### **clean by construction rather than by exception.**

**EXECUTOR DISCLOSURE:** a tabulation error in `primePower_counts` — prime powers below `9` are
`{2,3,4,5,7,8}` = **6**, not 5 — was written by the executor and ### **caught by `decide` at build time,
before landing.** *The failure mode the kernel exists to catch, caught on its own first build.*

---

## CLOSING — FOR THE AUTHOR'S WORD

### **RETURNED BY THIS PASS**

1. ### **CORRECTION 13 LANDED** and its law minted — then the law immediately caught its own author's
   unchecked `244`.
2. ### **THE CRLF DEFECT WAS 52 FILES, NOT ONE.** Fixed at the root; mirror now 22/22 coherent.
3. ### **A FIFTH PROSE SITE EXISTED THAT THE WORK-ORDER NEVER NAMED** — `CONSTANCE` L2702, repaired.
4. ### **1.2 FROZEN**, 1.2-C with its exception recorded and its two post-pin commits ruled `KEEP` from content.
5. ### **THE CLUSTER ENUMERATION IS RUN** — the census's last un-run row. `SIDE-effects` is cited **14×** in
   spectral alone, which is what makes its route ruling load-bearing.
6. ### **`SIDE-window` `v0.1.0` IS LIVE AND PUBLIC**, axiom-free, with its non-claims travelling in the source.

### **STILL HELD, UNCHANGED**

* ### **THE TWO `W-CARRIER-BUILD` ACTS** — committed locally at `relay` tip, unpushed, absence from the
  public tree re-verified against the remote. **Release condition: counsel's answer, then your word.**

### **THE FOUR RULINGS, RESTATED AND STILL AWAITING YOU**

1. ### **`SIDE-effects` REPAIR ROUTE** — (i) honest `INTERFACES` on named premises *(preferred — preserves
   the citation)* vs (ii) `SHELL` + no-cite guards **verified at every citing site**. ~1–1.5 sittings.
   ### **Now sized by the enumeration: 14 citations in the spectral cluster alone.**
2. ### **DAY-1 DIGESTION SCOPE** — (A) annotations-only *(~1 sitting; the standing recommendation)* vs
   (B) back-matter Correspondence subsections *(~2 sittings)*.
3. ### **THE TWO PROSE RULINGS** — the P1 six-counts opening and the P2 caveat placement; neither ever
   resolved to a corpus locus.
4. ### **`internal/` + `meta/` RATIFICATION** — both stand `REGISTRY-SILENT`, and `internal/` now holds
   counsel-facing material carrying a live inventory of what is already public.

**`h2` UNCHANGED. `WIDEN` PAUSED. RAIL DID NOT MOVE. NOTHING DEPOSITS.**
