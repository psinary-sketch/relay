# b193 — THE RESTRICTED TENSOR CONSTRUCTION, ACT ONE

**Registration `09c1758`, banked after the owner reads, the toolchain feasibility test and the
Mathlib read — ### before any Lean was written, with the gate's weakness declared in advance.**
2026-08-26. Ferry part 1 of 1, receipt confirmed in full.

> ### **A BUILD. THE ACT PRODUCED CONSTRUCTION, NOT ONLY READS.**
> ### **Core is untouched at 304/304, rows 1–79.** *The new work is Interfaces-layer; its row is 80.*

---

### **(v-unvicies) THE RESTRICTED TENSOR CONSTRUCTION, ACT ONE — filed 2026-08-26 (b193)**

> ### **A BUILD. THE ACT PRODUCED CONSTRUCTION, NOT ONLY READS.** ### **Core is untouched at
> 304/304, rows 1–79; the new work is Interfaces-layer and its row is 80.**

### **LAYER ONE IS BUILT AND COMPILED.** `Interfaces/RestrictedTensorLayer1.lean`:
`Ftensor_sq`, `parityTensor_sq`, `tensorFactor` — ### **`[propext, Classical.choice, Quot.sound]`,
re-run at build, no `sorryAx`, zero errors, exit 0.** ### **`F` and `parity` are BUILT from the
factors' via `TensorProduct.congrIsometry`; both identities are THEOREMS on the built object.**

> *** ### **THE GATE, AND THE HONESTY REGISTERED BEFORE IT RAN.** The ferry's known-answer gate —
> *agree with the finite tensor product Mathlib already holds* — ### **is definitional here and
> therefore CANNOT FAIL**, because the layer is built **on** Mathlib's tensor product.
> ### **A GATE THAT CANNOT FAIL IS NOT A GATE, and that was written in the registration before the
> run, not discovered after it.** ### **The gate actually run, which can fail: the two identities
> the corpus's own structure demands, checked on the built object. Both passed.** ***

### **THE TOOLCHAIN, ESTABLISHED BY TEST AND NOT ASSUMED — IT NEARLY HALTED THE ACT.** The first
probe failed with ### **“incompatible header”**; the cause, read at content, is that mathlib4's own
`lean-toolchain` says ### **v4.29.0** while the default is v4.29.1. ### **A version mismatch is not
a missing library.** v4.29.0 is installed; a probe then compiled clean **before** any construction
was attempted.

### **AND A CORRECTION TO b189, WHICH WAS MINE.** b189 read `CanonicalTensor.lean`, found it *real*
and finite-dimensional, and concluded ### **“Mathlib holds the parts and not their combination”**.
### **There is a whole file b189 did not find: `Analysis/InnerProductSpace/TensorProduct.lean`**,
carrying `instInnerProductSpace` (*“⟪ a ⊗ b, c ⊗ d ⟫ = ⟪ a,c ⟫ * ⟪ b,d ⟫”*), `instNormedAddCommGroup`,
and ### **`congrIsometry` — exactly what `F = F_v ⊗ F_w` needs.** ### **b189's sentence was too
strong and it was mine.**

**What is genuinely NOT HELD, now named exactly:** ### **an inner product on an arbitrary-index
`PiTensorProduct`** — Mathlib carries only `InjectiveSeminorm` and `ProjectiveSeminorm` there,
### **seminorms, not an inner product** (so the plan routes around it by iterating binary tensors);
and ### **the `E₁`-unit inclusion isometry facts**, not located and not assumed.

### **THE FALSIFIER, NAMED IN ADVANCE per the codomain precedent:** ### **if the `E₁`-unit
inclusions are not isometries, the construction as planned is RETIRED, not patched** — the colimit
would not be a pre-inner-product space and the completion layer would have nothing to complete.

**The state: five layers, ### one built.** L2 held-but-unbuilt; ### **L3 part-held and carrying the
falsifier's subject**; L4 held; L5 unread. ### **No estimate of effort, no ranking, and no claim
that the construction will succeed.**

> ### **WHAT THIS IS NOT: it is one layer of an INFRASTRUCTURE DEBT, and it bears on `h2` not at
> all.** *The identity is exactly as unproved as it was.*

---

## THE SEATS, SCORED

**EXECUTOR: five for five.**

- **(e1)** the read will correct b189 — ### **lands**, and it is the act's most uncomfortable
  finding because ***b189 was mine.***
- **(e2)** layer 1 buildable now; the rewriting harder than the mathematics — ### **lands**, and
  the proofs were three lines each via `induction_on`. ***The prediction was right and the
  difficulty smaller than expected.***
- **(e3)** later layers' ingredients not assumed — ### **holds**: two located, one part-located,
  one unread, ### **and the NOT-HELD one is named as the falsifier's subject.**
- **(e4)** the known-answer gate is definitional and weak, said **before** running it —
  ### **holds**, and a gate that *can* fail was substituted and run.
- **(e5)** nothing enters **Core** — ### **holds. 304/304, rows 1–79, untouched.**

---

## THE DEVIATIONS — TWO, AND THE FIRST IS A REPEAT

### **I wrote the correspondence row as a `python -c` string inside a double-quoted bash command,
and the shell's backticks ate every code-span** — the terminal names, the file path, the axiom
list, and the word `sorryAx` **all vanished, and the script reported success.**
### **b178 suffered the identical defect and b158's standing rule exists for exactly it.**
Caught by reading the row back; repaired with a Write-tool script; ### **six cells, no blanks,
verified by count and not by eye.**

**And a second, smaller one in the same breath:** the scratch build helper was committed into the
**kernel repo** by a wildcard add. ### **Removed** — the toolchain recipe belongs in the bank and
the Lean file's header, not in the kernel tree.

---

## THE THIRTY-SEVENTH SEAM'S DEBT

### **Term 3's construction is a LIVE PROGRAM with five layers, one built, and its own falsifier
named.** ### **Its next live question: the `E₁`-unit inclusion isometry facts (M20).**
**Term 2's formalization** follows at your schedule — the file that does not exist, and the
class-richness lemma at cite. **M17 · M18 · M19** stand with you · ### **`μ`'s value remains
yours** · M16 · b155's unchased thread · the boundary's two NOT-HELD ingredients · M12 · M11 · M9 ·
the cross-language coupling · the in-flight items · 104 references · ~158 unswept `W-` codes · the
definitional fork · gates 2 and 6 · the seat boundary's form · the Q-route `Ψ` instability ·
b157's six · the three front-door items · the tense hazard · the bra-ket convention · Prop 5.5's
hazard · the methodology day (M1–M20). **Deep items:** the relative identification; the h1/h2
statement drafting.

---

## THE AUDITS — EMITTED, NOT TYPED

**The layer-one build — the axiom profile, re-run at build:**

```
'RestrictedTensorLayer1.Ftensor_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'RestrictedTensorLayer1.parityTensor_sq' depends on axioms: [propext, Classical.choice, Quot.sound]
'RestrictedTensorLayer1.tensorFactor' depends on axioms: [propext, Classical.choice, Quot.sound]
### BUILD EXIT=0
```

```
==============================================================================
BANNED-TERM REVIEW (banned_terms.py, b142) -- RUN, NOT CLAIMED
==============================================================================
  stems scanned    : gap, blind
  scope            : whole file b193_restricted_tensor_one.txt (created this act)
  scope            : whole file RestrictedTensorLayer1.lean (created this act)
  files in scope   : 2
  lines in scope   : 260   ### the act's own voice, not the corpus
  hits found       : 0
  live uses        : 0

  VERDICT          : CLEAN
  ### the verdict reads the LIVE count, not the hit count -- a scope may
  ### carry excepted hits and still be clean, and that is the whole
  ### reason the classes are printed rather than filtered silently.
```

```
==============================================================================
BANNED-TERM REVIEW (banned_terms.py, b142) -- RUN, NOT CLAIMED
==============================================================================
  stems scanned    : gap, blind
  scope            : added lines in D:/MY-DOwnloads/PLACE-papers vs HEAD
  files in scope   : 2
  lines in scope   : 68   ### the act's own voice, not the corpus
  hits found       : 0
  live uses        : 0

  VERDICT          : CLEAN
  ### the verdict reads the LIVE count, not the hit count -- a scope may
  ### carry excepted hits and still be clean, and that is the whole
  ### reason the classes are printed rather than filtered silently.
```

**The index queries:**

```
b193 -- INDEX QUERIES per (c).
  restricted tensor    NO KEY
  the construction     NO KEY
  identity             HIT -> identity
  global section       NO KEY
  hilbert              NO KEY
  tensor product       NO KEY
  boundary license     HIT -> boundary-license
  exact reduction      HIT -> exact-reduction
### ABSENCE FROM THE INDEX IS NOT ABSENCE FROM THE RECORD.
```

**The hook, live in this act's own commit:**

```
--- SEAT-BOUNDARY PRE-COMMIT (b179) ---
  repo             : D:\MY-DOwnloads\PLACE-papers
  staged paths     : 2
  foreign prefixes : phase1.5/method/patent-package/
  foreign hits     : 0
  VERDICT          : CLEAN -- no foreign-seat path staged
  ### and a clean verdict here means ONE thing only: no staged path
  ### begins with a foreign prefix. ### IT IS NOT A REVIEW OF THE COMMIT.
[main 4bbd2b4] b193: term 3's construction begun -- layer one built and compiled; b189's Mathlib read corrected
 2 files changed, 68 insertions(+)
```

**The mirror, all three clauses:**

```
==============================================================================
MIRROR VERIFICATION -- ALL THREE CLAUSES (b142; clause 3 added b183)
  archive: D:/MY-DOwnloads/mirror-refresh-2026-08-26.zip
==============================================================================

--- CLAUSE 1: THE ARCHIVE AGAINST ITS OWN MANIFEST ---
  files in archive (excl MANIFEST) : 40
  rows parsed from MANIFEST        : 40
  md5 / byte mismatches            : 0
  CLAUSE 1 : CLEAN

--- CLAUSE 2: THE BUILD'S SOURCE HEAD AGAINST ls-remote ---
  manifest declares source HEAD    : 4bbd2b4
  ls-remote origin/main              : 4bbd2b455c8870c00ae96375675bf8cd11a35d99
  CLAUSE 2 : CLEAN -- they agree

--- CLAUSE 3: THE ARCHIVE'S CONTENTS AGAINST THE ROSTER ---
  roster entries (source paths) : 40
  archive files (excl MANIFEST) : 40
  in roster, MISSING from archive : 0
  in archive, NOT in roster       : 0
  CLAUSE 3 : CLEAN -- archive and roster agree, name for name

  ### VERDICT: CLEAN ON ALL THREE CLAUSES
  ### NO CLAUSE ALONE IS THE VERIFICATION; THE LAW REQUIRES ALL THREE.
  ### clause 1 is the archive against ITSELF, clause 2 is the pin, and
  ### clause 3 is the archive against the ROSTER -- ### THE ONLY ONE OF THE
  ### THREE THAT CAN SEE A FILE THAT NEVER ENTERED THE STAGING DIRECTORY.
```

---

## PINS AT CLOSE — by `ls-remote`, never from recall

| repository | pin |
|:--|:--|
| `SIDE-global-section` `main` | ### **`56e938ed200cc009867b8569eb43b81b075c1154`** — **layer one, row 80; Core 304/304, rows 1–79 UNTOUCHED** |
| `PLACE-papers` `main` | `4bbd2b455c8870c00ae96375675bf8cd11a35d99` — **2 files, no patent paths** |
| `relay` `main` | `72df2076b4c9a588f707da7f1931d8f6efc0fa43` — **the act; read back by `ls-remote`** |
| mirror | `mirror-refresh-2026-08-26.zip` — **40 files**, rebuilt at `4bbd2b4`, ### **CLEAN ON ALL THREE CLAUSES** |
| HELD | `held/carrier-acts` = `6eada6a` — **LOCAL-ONLY, unpushed** |

> ### **The relay pin above is THIS ACT'S CONTENT COMMIT, read back by ls-remote.** *A pin-filling commit follows it carrying only this substitution.*

**Load this export:** `mirror-refresh-2026-08-26.zip`.

*STOP — the ferry's end.*
