# The reading packet — report only, nothing closed or landed — 2026-08-06

Pins at open: PLACE-papers `6173899`; relay `9a6552a`; lv `2f71068`; kernel `5e668b4`.
Rail at `de621b1` / `2147a03`. **Run untouched.** Nothing deposits.

---

## §1 — THE SIX UNCLUSTERED WORK-ORDERS, READ AT ±3 PARAGRAPHS

**Read at corpus scale rather than the sweep's window, three of the six dissolve, two are not
formulas, and one my own probe failed to retrieve.**

### (1) `slack = 2λ₁` — OPEN_TRAILS §1662 — **NOT A GAP**

> *"The proposed n = 1 instance `3γ + 2 ≥ ln(4π)` is **not** the instance. It is **γ + 2 ≥ ln(4π)**
> (slack = 2λ₁ = 0.0461914179, **matching the bench to 15 digits**)…"*

**Its verification is stated in the same parenthesis** — matched to a bench to 15 digits. The
sweep truncated the number at its decimal point and lost the clause. **Route: none needed.
Cost: zero.**

### (2) `jacobiTheta₂` — OPEN_TRAILS §1697 — **NOT A FORMULA**

A **Correspondence table row** naming a Mathlib lemma (`differentiableAt_jacobiTheta₂_snd`) against
its class (C₆, holomorphy on Re z > 0). **Struck: a lemma name is not a quantitative formula.
Cost: zero.**

### (3) `F(t₀)=0 there is ε>0 with F(t₀−ε…` — **NOT RETRIEVED; my probe mis-targeted**

My fragment was too generic and matched a different line (§1437, an unrelated reverted sitting).
**Reported as not retrieved rather than as read** — the item needs its exact line pulled before it
can be routed. **Cost to retrieve: machine-free, one exact search.**

### (4) `KL matrix ≈ c·δ_ij` — FINDINGS §225 — **PROVENANCED ON THE NEXT LINE**

> *"For rate R < C, codewords with nearly orthogonal output distributions exist (KL matrix ≈
> c·δ_ij)."*
> *"**theorem-supported** — ARITHMETIC_ORIGIN_STEANE_CODE_v3 §10.2; COMPLEX_ANALYSIS_IS_FORMATION_STRUCTURE Extension 3."*

**Route: derivation-at-source, MACHINE-FREE.** The grade and both cites sit one line below.
**Cost: a source read, no compute.**

### (5) `V′_k(σ) = −|ξ′|² / u_t along R-curves` — FINDINGS §289 — **PROVENANCED ON THE NEXT LINE**

> *"**theorem-supported** — P22 series; TRIVIUM_The_Third_Identity_Element §8."*

**Route: derivation-at-source, MACHINE-FREE. Cost: a source read.**

### (6) `ξ(ρ) = ξ′(ρ) = 0` — VERIFICATION_LOOM §2582 — **NOT A FORMULA, IT IS A TARGET**

> *"**Target.** Exclude the codimension-2 coincidence **ξ(ρ) = ξ′(ρ) = 0** (a double zero), per
> mechanism class, via the SIDE catalogue one level down (§22.5 line 1483…)"*

A **condition being excluded**, not a quantity asserted, and it carries its source line. **Struck.
Cost: zero.**

### What this says about the sweep, and it is a FIFTH failure mode

**(4) and (5) were flagged because the corpus's own grade vocabulary — `theorem-supported` — was
not in the provenance keyword list**, and the cite format was not either. That is the
keyword-gap mode again, but against **the corpus's grading convention rather than against a
word like "pinned"** — a distinct and more systematic version of it, since every
`*theorem-supported*` line in FINDINGS carries provenance the sweep cannot see.

**None of the six wants compute. Nothing here contends with the running validation.**

---

## §2 — `non-discriminating by design`: THE USE-SITE, AND A DRAFT CRITERION

**The single genuine use-site is OPEN_TRAILS §2476** (the others are the sweep's own entries
discussing the term):

> *"…the registered inequality set contained a derivation error, caught by the computation
> (registration wrote κ₂ₖ ≤ 0 ∀k ≥ 2; measured κ₆ = +3.46e−5; re-derivation at source: the
> LP-necessary pattern is ALTERNATING…); measured signs match the corrected pattern exactly;
> quantitative tie κ₂/2 = Σγ⁻² to tail accuracy; routes agree ≤1e−41; Turán anchor reproduced.
> **Verdict: corrected layer-1 PASS, non-discriminating by design (registered boundary)**…"*

### The DRAFT criterion, extracted from that use rather than composed

> **A test is NON-DISCRIMINATING BY DESIGN when its pass condition is entailed by the construction
> of the object under test — so that the hypothesis and its negation both produce a pass, and the
> outcome carries no information about the hypothesis. "By design" marks that this was REGISTERED
> IN ADVANCE as the layer's boundary, not discovered after the pass.**

**The two options per the coinage register:**

1. **STATE THE CRITERION AT THE USE-SITE** — the sentence above, inserted at §2476, making the
   verdict resolvable where it is read.
2. **RETIRE AND STATE THE VERDICT LONGHAND** — replace with *"layer-1 passes, and the pass is
   uninformative because these conditions are necessary and satisfied by construction; registered
   as such in advance."*

**A THIRD OPTION THE READING TURNED UP, offered because it may be cheaper than either.** The
corpus already has a minted term for this shape: **the ZERO-POWER CLASS** — *an instrument has zero
power when the answer is fixed either by what the statistic omits or by what the pipeline
supplies* (π₀; the Li-Toeplitz pipeline). **"Non-discriminating by design" is the same figure in a
general-hypothesis register rather than the placement register.** If the kinship is ruled genuine,
the term retires **into an existing minted home** and cites it, which costs one clause and adds no
vocabulary. **Stated as a candidate; the kinship is close but not identical and the ruling is
yours.**

---

## §3 — THE EXHIBIT-RECORD CITATION CHECK: **UNCITED** — author's taste, not forced

All 21 mirror files searched.

| probe | hits | where |
|:--|--:|:--|
| `known-ground gate` | **1** | OPEN_TRAILS |
| `hold-aside` | **1** | OPEN_TRAILS |
| `exhibit record` | **1** | OPEN_TRAILS |
| `method canon` | 1 | OPEN_TRAILS |
| `METHOD_CANON` | 9 | OPEN_TRAILS, VERIFICATION_LOOM, REGISTRY |

**The deciding fact: every one of those hits is the OPEN_TRAILS entry that RESTATES the two forms
in full** — *"an engine earns trust on known ground first"*, *"answer it another way, or the
hold-aside is already broken"*, *"sixteen digits"*, the 1.6×10⁻⁹ agreement. **A mirror-only reader
can resolve both standing forms from OPEN_TRAILS without ever reaching the exhibit record.**

**VERDICT: UNCITED.** Nothing in the mirror *depends* on the exhibit record to be resolvable, so
**the resolvability standard does NOT force a roster add** — this is unlike INSTRUMENTS.md, whose
I-7/I-8 content was named in mirror files and stated only in the instrument file. **Adding
THE_METHOD_CANON.md to the roster is a matter of author's taste, and is stated as such.**

**The honest counterweight, so the verdict is not read as "no reason to add it":** the mirror
currently carries the two forms *as an OPEN_TRAILS entry*, which is a ledger of events, not the
method program. A reader looking for the programme's method exhibits will not find them where
method exhibits belong. **That is an argument from placement, not from resolvability — and
placement is taste.**

**No roster change this pass.**

---

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `6173899` — unmoved by this pass |
| relay | `9a6552a` → this report's commit |
| lv `2f71068` · kernel `5e668b4` · rail `de621b1` / `2147a03` | unmoved |

Run reports at stage 4 as ruled. Nothing closed, nothing landed. Nothing deposits.
