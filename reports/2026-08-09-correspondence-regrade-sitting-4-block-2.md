# RE-GRADE — SITTING 4, BLOCK 2 — 2026-08-09

**PATHS L271–L284, the "forces σ = ½" voice cluster.** 12 rows read. **1 corrected and landed, 3
re-grade candidates HELD on a vocabulary question, 8 confirmed.** Rail `de621b1` / `2147a03`
**unmoved**. **Nothing deposits.**

---

## §1 — THE STATEMENTS, WITH EVERY DEFINITION UNFOLDED

This is the cluster README summarises as *"five DERIVE σ = ½"*, so the statements matter more here
than anywhere else in the corpus. **Unfolded to their ℚ/ℝ/ℂ content:**

```lean
def fe_reflect        (σ : ℚ) : ℚ := 1 - σ
def indicial_reflect  (r : ℚ) : ℚ := -1 - r
def focus_codim       (σ : ℚ) : ℕ := if σ = 1 / 2 then 1 else 2

archimedean_forces_half (σ : ℚ) (h : fe_reflect σ = σ) : σ = 1 / 2      -- i.e. 1 − σ = σ → σ = ½
indicial_forces_half    (r : ℚ) (h : r ^ 2 + r + 1 / 4 = 0) : -r = 1 / 2 -- i.e. (r + ½)² = 0 → −r = ½
spinor_forces_half      (w : ℂ) (h : Complex.I * w = w) : w = 0          -- i.e. i·w = w → w = 0
balance_theorem (p : ℕ) (hp : p.Prime) (s : ℝ) : p ^ (-s) = p ^ (-(1 - s)) ↔ s = 1 / 2
monotone_unique_zero {V : ℝ → ℝ} (hV : StrictMono V) (ha : V a = 0) (hb : V b = 0) : a = b
C5_input_at_Phi : C5_input Phi                                           -- via Mathlib hasSum_int_evenKernel
```

**Three of the five "forces half" terminals are arithmetic identities over ℚ or ℂ.** Nothing in
`archimedean_forces_half`, `indicial_forces_half` or `spinor_forces_half` mentions ξ, a zeta
function, or a zero. **`spinor_forces_half` does not even conclude σ = ½ — it concludes `w = 0`**;
the link to the critical line is a separate theorem, `half_iff_centered_zero (σ : ℝ) : σ = 1/2 ↔
σ − 1/2 = 0`, which is itself an arithmetic tautology.

**Two are substantive within their scope:** `balance_theorem` is a real statement about prime powers
whose conclusion genuinely *is* `s = 1/2`; `C5_input_at_Phi` discharges against Mathlib's
`hasSum_int_evenKernel` and its docstring separates input from output explicitly.

**WHERE THE MATHEMATICS ACTUALLY SITS: in the naming.** That `fe_reflect` *is* the functional
equation's reflection, that `indicial_reflect` *is* the Frobenius indicial map, that `w` *is* the
centred coordinate — **each is a modelling assumption carried by the identifier, not by the
statement.** That is a legitimate way to build an identification kernel. It is not a derivation
about ξ, and the rows must say which.

---

## §2 — WHAT THE ROWS SAY, AND THE VOCABULARY PROBLEM

| row | description cell | grade cell |
|:--|:--|:--|
| L271 | *"II.1 Archimedean — **the FE structure forces σ = 1/2**"* | **Compiled (identification kernel)** |
| L273 | *"II.3 Frobenius — **the indicial root forces σ = 1/2**"* | **Compiled (identification kernel)** |
| L276 | *"II.6 Spinor/Information — **orbit collapse forces σ = 1/2**"* | **Compiled (identification kernel)** |
| L272 | *"II.2 Multiplicative — Euler balance identifies σ = 1/2"* | Compiled (Voice1) |
| L277 | C₅ split, *output-stage disclaimed* | Input compiled; output disclaimed |

> **`identification kernel` IS NOT DEFINED ANYWHERE IN THE CORPUS.** A corpus-wide search returns
> the string **only inside these grade cells themselves** — no definition, no gloss, no entry. It is
> also **not one of the three rubric grades** (DERIVES / INTERFACES-with-named-premise /
> ENCODES-CONCLUSION-or-SHELL). **It is pre-rubric vocabulary that the re-grade has now reached.**

**This is simultaneously an I-8 shortfall — a term named and never stated, findable only by reading
the cells that use it — and a rubric gap.**

**RE-GRADE CANDIDATES, HELD, NOT LANDED (L271 · L273 · L276).** My proposal is
**INTERFACES-on-named-premise**, the premise being the modelling identification (*"`fe_reflect` is
the FE reflection"* etc.), shortfall **one clause** each. **I held rather than landed because this
is a vocabulary ruling, not a factual correction**: if `identification kernel` is a sanctioned
fourth grade meaning *"models the structure and identifies the fixed point"*, then these rows are
already honest and what they need is a definition, not a re-grade. **Converting three rows on my own
reading of an undefined word would be exactly the over-reach the rubric exists to prevent.**
**The author's ruling is asked for: define the term, or fold these into INTERFACES.**

---

## §3 — THE ONE CORRECTION, LANDED: PATHS L274

| | |
|:--|:--|
| description | *"II.5 R-Curve — **RH ⟺ V-monotonicity (equivalence)**"* |
| cited terminal | `SIDERCurve.monotone_unique_zero` |
| grade was | ***"Equivalence compiled**; closure research-reach"* |

**The terminal is not an equivalence.** It is
`StrictMono V → V a = 0 → V b = 0 → a = b` — one implication. **And the kernel's own comment above
it says so:**

> *"## T1 — the engine: strict monotonicity ⟹ at most one zero. **This is the decisive (ii)⟹(i)
> step.** A strictly monotone V is injective, so it vanishes at most once."*

**I also enumerated every theorem in `SIDERCurve/Criterion.lean` at its pin: `monotone_unique_zero`,
`monotonicity_formula`, `beta_V_re`, `singular_repulsion`, `online_zero_codim_one`,
`offline_zero_codim_two`, `second_zero_breaks_monotone`. There is NO equivalence terminal in the
kernel at all.**

> **CORRECTED AND LANDED (PATHS is non-rail): "Equivalence compiled" → "ONE DIRECTION compiled, not
> the equivalence", quoting the kernel's own `(ii)⟹(i)` comment and recording that SIDE-rcurve
> v0.1.0 contains no equivalence terminal. Shortfall: one clause — the converse direction.
> "Closure research-reach" is kept.**

**This is a factual mismatch, not a vocabulary choice, which is why it landed where §2's three
did not.** Note it is **repeated elsewhere** — REGISTRY's row 1.5a-5 also reads *"`monotone_unique_zero`,
equivalence — closure research-reach"*. **That second site is NOT corrected here** (out of block
scope) and is flagged for the sweep.

**A neighbouring shape, noted not filed:** `online_zero_codim_one : zero_codim true = 1 := rfl` is
**definition-encoded** — `zero_codim` is *defined* to be 1 on `true`. `focus_codim σ := if σ = 1/2
then 1 else 2` is the same shape, which makes `archimedean_identifies_half` a tautology by
construction. **Neither is cited by a PATHS row, so neither is a finding here** — but rowgen's
`defenc` flag does **not** catch `if`-bodied definitions, only literal constants. **Work-order on
the instrument, with its trigger: extend `defenc` to conditional bodies before the next diff pass.**

---

## §4 — DELTA TABLE, CUMULATIVE

| outcome | this block | cumulative |
|:--|--:|--:|
| **CONFIRMED at grade** | **8** | **19** |
| **RE-GRADED / CORRECTED (landed)** | **1** (L274) | **2** |
| **RE-GRADE CANDIDATES — HELD** | **3** (L271 · L273 · L276, vocabulary ruling) | **3** |
| **REPAIRED (landed)** | 0 | 1 |
| **STRUCK** | 0 | 0 |
| **HELD-AT-RAIL** | 0 | 0 |
| **WORK-ORDERS opened with trigger** | **2** (defenc-on-`if`; the REGISTRY "equivalence" second site) | 2 |

**ROWS STATEMENT-READ — machine checks do not count:**

| | rows |
|:--|--:|
| sitting 1 (SIDEDerivative) | 3 |
| sitting 3 (`spectral_cannon` labels) | 3 |
| sitting 4 block 1 (pentagon) | 13 |
| **sitting 4 block 2 (voice cluster)** | **12** |
| **total read** | **31 of 99** |
| **of the 45-row PATHS+SURROUND read** | **25 of 45** — PATHS 7 remain, SURROUND 13 remain |

---

## §5 — ITEMS 2 AND 3

**THE RAIL-VS-WORKING DIVERGENCE FILED** to the census as **§H**, with the finding stated as a
finding: two documents share a name and differ by **121 lines**, and nothing in the corpus says
which one a reader gets. **The fifteen-file basecamp diff is promoted to a hard slate position —
after the 45-row read, before pass 2 opens** — because pass 2's reading copy per paper must be
ruled, not assumed. **Not run this sitting.** Scope caution recorded on its face: **sixteen files
share names across the boundary; one has been diffed; the other fifteen are the diff.**

**ONE LOOM LINE FILED — *a shell and a disclosed interface are the same term; the difference lives
in the row*** — with block 1's pentagon cluster as the worked example, and the corollary that
matters for the remaining 68 rows: **do not grade a terminal by reading its proof term. A thin proof
under an honest row is compliant; a thick proof under a row that overstates it is not.**

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | → this pass's commit (PATHS L274 · OPEN_TRAILS §H · VERIFICATION_LOOM) |
| relay | → this report's commit |
| **rail `de621b1` / `2147a03`** | **UNMOVED, both clean** |

**Pass 2 stays closed. Nothing deposits.**
