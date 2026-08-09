# THE FIFTEEN-FILE BASECAMP DIFF + THREE CLOSERS — 2026-08-09

**Report only: no merge, no deletion, no relocation.** Rail `de621b1` / `2147a03` **unmoved, both
clean**. **Nothing deposits.**

---

## §1 — THE DIFF TABLE

**Sixteen files share a name across the boundary. SIMPLICITY was diffed in sitting 4; the remaining
fifteen are below. Four required a rename search before they could be diffed at all** — reported as
"no working copy" by filename, they exist under other names, which the W5 reference-scan rule
predicts and which a filename-only pass would have mis-reported as four missing documents.

| rail | file | rail L | work L | rail date | work date | only-rail | only-work | class |
|:--|:--|--:|--:|:--|:--|--:|--:|:--|
| p1.5 | A_METHODOLOGY | 386 | 408 | 2026-05-27 | 2026-07-28 | 20 | 42 | **(c) MIXED** |
| p1.5 | CLASS_NUMBER_ANOMALY | 104 | 111 | 2026-05-27 | 2026-07-24 | 10 | 17 | **(c) MIXED** |
| p1.5 | FOUNDATIONS_OF_THE_SIDE_PROGRAMME | 325 | 359 | 2026-05-27 | 2026-07-31 | 40 | 74 | **(c) MIXED** |
| p1.5 | INTERFACE_CONSERVATION | 199 | 204 | 2026-05-27 | 2026-07-24 | 11 | 16 | **(c) MIXED** |
| p1.5 | R_CURVE_CRITERION | 237 | 260 | 2026-05-27 | 2026-07-26 | 13 | 36 | **(c) MIXED** |
| p1.5 | SIMPLICITY_OF_RIEMANN_ZEROS *(prior)* | 219 | 257 | 2026-05-27 | 2026-08-09 | 34 | 72 | **(c) MIXED** |
| p1.5 | COMPLEX_ANALYSIS_IS_FORMATION_STRUCTURE → `phase2/formation/COMPLEX_ANALYSIS.md` | 235 | 237 | 2026-05-27 | — | 1 | 3 | **(c) MIXED** *(renamed)* |
| p2 | BSD_VIA_FORMATION_TRANSFER | 255 | 264 | 2026-05-27 | 2026-07-23 | 14 | 23 | **(c) MIXED** |
| p2 | FANO_DERIVATION_OF_LAMBDA | 144 | 137 | 2026-06-10 | 2026-07-23 | 8 | 1 | **(c) MIXED** |
| p2 | INTERFACE_DARKNESS_…_COGNITIVE_VARIABLE | 190 | 190 | 2026-05-27 | 2026-07-31 | 1 | 1 | **(c) MIXED** |
| p2 | **MATTER_AS_ARITHMETIC** | **340** | **102** | 2026-05-27 | 2026-07-19 | **323** | 85 | **(c) MIXED — the outlier** |
| p2 | YANG_MILLS_MONOGRAPH | 230 | 237 | 2026-05-27 | 2026-07-23 | 13 | 20 | **(c) MIXED** |
| p2 | ARITHMETIC_ORIGIN_OF_QUANTUM_CODES → `phase2/quantum/ARITHMETIC_ORIGIN_QECC.md` | 166 | 174 | 2026-05-27 | — | 16 | 24 | **(c) MIXED** *(renamed)* |
| p2 | STRUCTURAL_ERROR_CORRECTION → `phase2/quantum/FORMATION_DISTANCE_AND_SILENCE_AS_PROTECTION.md` | 144 | 147 | 2026-05-27 | — | 5 | 8 | **(c) MIXED** *(retitled)* |
| p2 | TYPE_D_EXCLUSION → `phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md` | 214 | 237 | 2026-05-27 | — | 80 | 103 | **(c) MIXED** *(retitled)* |

### The headline result

> **NOT ONE FILE IS CLASS (a) WORKING-AHEAD. All fifteen are (c) MIXED — every frozen copy carries
> lines that exist nowhere in the working tree.**

**"Normal drift" is not what this is.** The comfortable model — the working tree moves forward, the
rail holds an older prefix — **is refuted for every single file**. The rail is not a stale prefix;
it is a divergent branch with unique content in all fifteen.

### The outlier, and it inverts the assumption

**`MATTER_AS_ARITHMETIC`: rail 340 lines, working 102, with 323 lines existing ONLY in the frozen
copy.** The working file explains itself in its own header:

> *"(REGISTRY row p2-9 carries a 'v1.1 consolidated' label for a **sibling-repo edition**; this
> on-disk file is the **v0.2 lineage** — **the re-sync remains a noted item**.)"*

**For this paper the RAIL IS AHEAD.** The frozen copy is the consolidated v1.1 edition; the working
copy is the older v0.2 lineage, and the corpus already knew, flagging the re-sync as an open item.
**Anyone assuming "working = current" would read the shorter, older document.** That is precisely
the hazard the diff was scheduled to expose before pass 2.

### Two subtleties worth the author's eye

**`FANO_DERIVATION_OF_LAMBDA` is the only file where the rail is LONGER and the working copy has
almost nothing unique** (8 only-rail vs **1** only-work) — a near-pure recovery candidate in
practice even though the classifier reads MIXED on that single line. **`INTERFACE_DARKNESS`** differs
by exactly **one line each way** — likely a header or date, and the cheapest reconciliation on the
board.

**No ruling is proposed here.** The deliverable is the table; **the reading copy per paper is the
author's to rule**, and pass 2 stays closed until it is.

---

## §2 — THE FOUR UNREAD TERMINALS: "45 of 45" NOW CARRIES NO ASTERISK, AND THE ROW MOVED

The four terminals under SURROUND L171, read at pin and **unfolded**:

```lean
def conjugate_re    (σ : ℝ) : ℝ := σ
def reflect_re      (σ : ℝ) : ℝ := 1 - σ        -- Voice2
def reflect         (σ : ℝ) : ℝ := 1 - σ        -- Voice3
def S_action        (σ : ℝ) : ℝ := 1 - σ        -- Voice5
noncomputable def spectral_offset (σ : ℝ) : ℝ := σ - 1 / 2   -- Voice6
def self_adjoint_constraint (σ : ℝ) : Prop := spectral_offset σ = 0
```

> **THREE OF THE FIVE VOICES USE LITERALLY THE SAME MAP.** `reflect_re`, `reflect` and `S_action`
> are each defined as `σ ↦ 1 − σ`. So `symmetries_agree_iff`, `reflect_fixed_iff` and
> `modular_forces_half` are **one arithmetic fact — `1 − σ = σ ↔ σ = ½` — stated three times under
> three names**, not three independent derivations.

> **AND VOICE 6 IS ENCODES-CONCLUSION-SHAPED.** `self_adjoint_constraint σ := (σ − ½ = 0)`, so
> `self_adjoint_forces_half : self_adjoint_constraint σ → σ = ½` **has its conclusion as its
> hypothesis by definition.**

**Only `voice1.balance_theorem` is distinct and substantive** — `p^(−s) = p^(−(1−s)) ↔ s = ½`, a
real statement about prime powers.

**L171 RE-CELLED (SURROUND is non-rail, so it landed).** The maps are now printed in the cell, voice6's
encoding is named, the stipulation is printed — *that each map IS its mechanism class's
characteristic symmetry is carried by the identifier, not compiled* — and the **shortfall is counted
at 2 clauses: (i) the independence of the three reflection voices, (ii) voice6's non-encoding.**
**The C₇ half of that cell — already exemplary — is untouched.**

**This is the sitting's most consequential finding**, and it was reachable only because the ferry
refused to let "45 of 45" stand with four terminals unread.

---

## §3 — THE TWO CLOSERS FILED

**`W-ORD-PROSE-OUTRUNS-ROW`** — the class: *a corrected row sitting beside an uncorrected sentence,
where the row is the audited surface and the prose is not.* **Four sites quoted verbatim**, incl.
CONSTANCE L2885 *"**The identification is exact.**"* — the precise claim the spinor re-cell refuted.
**Trigger: before any of those papers is opened for any other reason, the site is corrected to its
row's corrected reading.** Papers were **not** opened now; the fix rides the next natural edit.

**`READ-VERSUS-SPAN`** — *a block's count is the rows READ, not the span COVERED.* The as-read family
at reading scale, with block 2's **12-vs-6** as the worked example, the one-step propagation
recorded (the next ferry inherited "remaining 7" when it was 13), and the recognition rule: **a count
that equals its span exactly is the suspect case** — reading rarely lands flush with its plan.

---

## §4 — CUMULATIVE DELTA, WITH THE FOUR TERMINALS FOLDED IN

| outcome | cumulative |
|:--|--:|
| **CONFIRMED at grade** | **40** |
| **RE-CELLED under the ruling** | **6** (L271 · L273 · L276 · L281 · SURROUND L170 · **SURROUND L171**) |
| **CORRECTED (factual)** | **4** (PATHS L274 · PATHS L316 · REGISTRY 1.5a-5 · SIMPLICITY profile cell) |
| **STRUCK** | **0** |
| **HELD-AT-RAIL** | **0** |
| **UNVERIFIED, declared** | **0** — *the last one closed this sitting* |
| **WORK-ORDERS with trigger** | **3** (rowgen `if`-bodied defenc · REGISTRY second site *(now closed)* · prose-outruns-row) |

**ROWS STATEMENT-READ — machine checks do not count:**

| | rows |
|:--|--:|
| sittings 1 + 3 | 6 |
| block 1 (pentagon) | 13 |
| block 2 (voices, corrected) | 6 |
| block 3 (PATHS finish + SURROUND) | 26 |
| **this pass — the four terminals under L171** | **+4 terminals within an already-counted row** |
| **total rows read** | **51 of 99** |
| **PATHS + SURROUND** | **45 of 45 — COMPLETE, and now without qualification** |

**Forty-eight rows remain unread**, all outside PATHS and SURROUND.

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | → this pass's commit (SURROUND L171 · VERIFICATION_LOOM ×2) |
| relay | → this report's commit |
| **rail `de621b1` / `2147a03`** | **UNMOVED, both clean — nothing merged, deleted or relocated** |

**Pass 2 stays closed until the author rules the reading copy per paper. Nothing deposits.**
