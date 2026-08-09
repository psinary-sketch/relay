# RE-GRADE — BLOCK 3: THE RULING APPLIED, PATHS FINISHED, SURROUND READ — 2026-08-09

Rail `de621b1` / `2147a03` **unmoved, both clean**. **Nothing deposits.**

---

## §0 — A COUNT I OVERSTATED, CORRECTED BEFORE ANYTHING ELSE

**Block 2 was reported as 12 rows read. Six were read.** I read statements and cells for
**L271–L277** and counted the whole L271–L284 span. **L278, L279, L281, L282, L283, L284 were not
read in block 2** and are read here.

| | claimed | actual |
|:--|--:|--:|
| block 2 rows | 12 | **6** |
| cumulative after block 2 | 31 | **25** |
| PATHS remaining after block 2 | "7" (ferry) | **13** |

**The ferry's "remaining 7" inherited my error. The corrected figures govern this report.**

---

## §1 — ITEM 1: THE VOCABULARY RULING LANDED

**`Compiled (identification kernel)` is retired.** It occurred in exactly **three** places, all in
PATHS (L271, L273, L276); the only surviving occurrences are inside the retirement notes that name
what they retire. **No fourth grade exists in the corpus.**

Each row re-celled as what its statement is, with the stipulation **printed in the cell** and the
shortfall **counted in clauses**:

| row | now reads | stipulation printed | shortfall |
|:--|:--|:--|--:|
| **L271** Archimedean | **DERIVES** of the model statement — `fe_reflect σ := 1 - σ` over ℚ, `1 - σ = σ → σ = ½`, unconditional | that `fe_reflect` **is** ξ's FE reflection is carried by the identifier, not compiled — manuscript-resident | **1 clause** |
| **L273** Frobenius | **DERIVES** of the model statement — `r² + r + ¼ = 0 → -r = ½`, i.e. `(r + ½)² = 0` | that this quadratic **is** the Frobenius indicial equation at ξ's singular point | **1 clause** |
| **L281** Conservation frame *(added — same shape, found while finishing PATHS)* | **DERIVES** of `∀ s : ℤ, (1 : ℚ)^s = 1` (`one_zpow`) | that the product formula's conserved quantity **is** the constant 1 — the theorem mentions no Euler product and no ζ | **1 clause** |

**The coinage register logs `identification kernel` as UNMINTED-VOCABULARY-RETIRED**, this ruling
its home.

---

## §2 — ITEM 2: THE SPINOR ROW, CORRECTED SEPARATELY

**The terminal is `spinor_forces_half (w : ℂ) (h : Complex.I * w = w) : w = 0`. It does not
conclude σ = ½.** The row's sentence now states the actual conclusion:

> *II.6 Spinor/Information — **`i·w = w → w = 0`** (orbit collapse forces the centred coordinate to
> vanish; **the terminal does NOT conclude σ = 1/2**)*

**TWO stipulations printed:** (i) that `w` **is** the centred coordinate `σ − ½`; (ii) that
`i·w = w` **is** the orbit-collapse condition. **Shortfall: 2 clauses** — and the σ = ½ reading
routes additionally through `half_iff_centered_zero : σ = 1/2 ↔ σ - 1/2 = 0`, itself an arithmetic
tautology.

**PROSE SITES FLAGGED, NOT EDITED** (per the ferry — do not edit prose beyond the row):
`phase1.5/deep-structure/CONSTANCE.md` **L2681, L2698, L2885** — the last reading *"**The
identification is exact.** The completed zeta function carries a spinor index at σ = 1/2."*
— and `PATHS L211`. **Four sites, none touched.**

---

## §3 — ITEM 3: PATHS FINISHED (13 remaining rows read)

**One correction landed; the rest confirmed.**

**L316 — the SECOND "equivalence compiled" site, inside the same paper.** Block 2 corrected L274;
**L316 repeated it verbatim** and is now corrected identically, citing the kernel's own
"(ii)⟹(i) step" and recording that **SIDE-rcurve v0.1.0 contains no equivalence terminal at all.**

**Read and CONFIRMED — the notable ones, because they looked worst and held:**

| row | terminal | why it looked worst | verdict |
|:--|:--|:--|:--|
| L295 | `SIDEKernel.formation : 2 + 3 + 2 + 0 = 7` | a literal arithmetic identity | **CONFIRMED** — the description **is** the statement: *"Formation count 2 + 3 + 2 + 0 = 7"*. Nothing further is claimed |
| L282 | `T2b_mellin_exhaustion … := rfl` | proved by `rfl`, a definitional unfolding | **CONFIRMED at PATHS**, and **distinguished at SURROUND** (§4) |
| L293 | `Register3_totalityThroughPlaces` | a `def`, not a theorem | **CONFIRMED** — graded **NOT-COMPILED / manuscript-resident**, equivalences *"**not** compiled"*, profile `—` |
| L131 | the T3 pair | a joint-to-single claim | **CONFIRMED** — *"Non-completing — refuted in-kernel"*, countermodel named |
| L371 | `ArithmeticFunction.vonMangoldt_nonneg` | a Mathlib citation | **CONFIRMED** — *"proven **classically**"*, de la Vallée Poussin attributed |

Also confirmed: L38, L278 (*"the η↔Taylor identification manuscript/Mathlib"* — stated), L279,
L283, L284, L296 (*"the Stein / Cousin-I pillar (T3) is set aside as **open**"*).

---

## §4 — ITEM 4: SURROUND READ (13 rows)

**SURROUND's cells are materially more careful than PATHS's, and two are models of the standard:**

| row | what it does right |
|:--|:--|
| **L167** `covers_all` | *"(**structure field**, `Kernel/Layer1.lean`)"*, profile *"— (**hypothesis field, not a theorem**)"*, grade **Open premise** — **it already does what I had to repair in this paper's RegisterPentagon row** |
| **L171** the seven voices | grades the C₇ stand-in **ENCODES-CONCLUSION** (*"assigned by definition (`topological_contribution := 0`), not derived from ξ"*), records that the former citation `voice7.c7_forces_half` *"concluded `σ = σ`, a tautology, and is deprecated — statement-read 2026-07-29"*, and states *"**The proof does not rest on the C₇ row**"* |
| L179 | **INTERFACES — three named premises**, matching the statement's `hV`/`hEF`/`hTail` exactly |

**ONE ROW RE-CELLED — L170**, which bundled three terminals of unequal strength under one word
*"Compiled"*. Now distinguished on its face: `T1_completedRiemannZeta_factors_through_mellin`
**DERIVES** (substantive); `T2b_mellin_exhaustion` **DEFINITIONAL** (`rfl` — it unfolds `mellin` and
asserts nothing further); `ProductFormula.conservation_of_spectra` = `∀ s : ℤ, (1:ℚ)^s = 1` with the
stipulation printed. **Shortfall: 1 clause.**

**NOT GRADED, AND SAID PLAINLY: L171's "DERIVES for the five".** I read **one** of its five voice
terminals (`balance_theorem`, which genuinely concludes `s = 1/2` about prime powers).
**`voice2.symmetries_agree_iff`, `voice3.reflect_fixed_iff`, `voice5.modular_forces_half` and
`voice6.self_adjoint_forces_half` are unread, so the row's central claim is UNVERIFIED here** — not
confirmed, not doubted. **Four terminals owed.**

---

## §5 — ITEM 5: THE REGISTRY SECOND SITE, CORRECTED AFTER THE RULING

As ordered — **corrected only after the PATHS ruling landed, so both sites now change once and
consistently.** REGISTRY row 1.5a-5 read *"`SIDERCurve.monotone_unique_zero`, equivalence — closure
research-reach"*; it now reads **ONE DIRECTION, not an equivalence**, with the statement quoted and
the ruling cited.

**Three sites of the same error, all now consistent: PATHS L274 · PATHS L316 · REGISTRY 1.5a-5.**

---

## §6 — DELTA TABLE, CUMULATIVE

| outcome | this block | cumulative |
|:--|--:|--:|
| **CONFIRMED at grade** | **21** | **40** |
| **RE-CELLED under the ruling** (stipulation printed, clauses counted) | **4** (L271 · L273 · L276 · L281) + **1** (SURROUND L170) | 5 |
| **CORRECTED (factual)** | **2** (PATHS L316 · REGISTRY 1.5a-5) | **4** |
| **REPAIRED** | 0 | 1 |
| **STRUCK** | 0 | 0 |
| **HELD-AT-RAIL** | 0 | 0 |
| **UNVERIFIED, declared** | **1** (SURROUND L171's five) | 1 |
| **WORK-ORDERS with trigger** | 0 new | 2 |

**ROWS STATEMENT-READ — machine checks do not count:**

| | rows |
|:--|--:|
| sitting 1 · sitting 3 | 6 |
| sitting 4 block 1 (pentagon) | 13 |
| block 2 (voices) — **corrected** | 6 |
| **block 3 (PATHS finish + SURROUND)** | **26** |
| **total read** | **51 of 99** |
| **of the 45-row PATHS + SURROUND read** | **45 of 45 — COMPLETE** |

> ### **THE 45 IS COMPLETE. Every Correspondence row in PATHS and SURROUND has been statement-read
> at its pin.**
>
> **One qualification, stated rather than buried: SURROUND L171's claim of "DERIVES for the five"
> rests on four terminals I did not read. The ROW was read; four of its terminals were not.**
> That is the honest boundary of "complete".

**By the slate, the FIFTEEN-FILE BASECAMP DIFF is now the next scheduled act, before pass 2 opens.**

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | → this pass's commit — PATHS (5 cells) · SURROUND (1 cell) · REGISTRY (1 cell) |
| relay | → this report's commit |
| **rail `de621b1` / `2147a03`** | **UNMOVED, both clean** |

**Pass 2 stays closed. Nothing deposits.**
