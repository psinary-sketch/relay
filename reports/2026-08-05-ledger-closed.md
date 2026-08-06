# The provenance ledger closed · the two-axis rule · the census at state — 2026-08-05

Pins at open: PLACE-papers `8273013`; relay `24c2b91`; lv `2f71068`; kernel `5e668b4`.
Rail at `de621b1` / `2147a03`, unmoved. Census undisturbed throughout. Nothing deposits.

---

## §1 — NUMBER-FIELD (5): all five closed, and two were extractor artifacts

| # | work-order | route | verdict |
|:--|:--|:--|:--|
| 1 | `d(K) = 2^(r₁+r₂+2)` | numerical check | **CLOSED — and the flag was an artifact.** The sweep's regex **truncated at the first `)`**; the corpus states `d(K) = 2^(r₁+r₂+2) **− 1**`, which checks against both corpus-stated instances: ℚ and imaginary quadratics → **7**, real quadratics → **15** |
| 2 | *formation total = 7 for every Dedekind ζ_K* | internal consistency | **CLOSED.** Consistent with (1): the bijection holds exactly where `d(K) = 7`, and the entry states where it fails — real quadratics at 15, *"eight spectator identities introduced by fundamental unit"* |
| 3 | `Λ(s, χ) = ε(χ)·Λ(1−s, χ̄)` | derivation-at-source | **CLOSED at cite** — classical, and the entry is itself a *correction* of a looser claim (that L(s,χ) "satisfies its own functional equation") |
| 4 | `ξ(s) = ∏_v ζ_v(s)` | derivation-at-source | **CLOSED at cite** — Tate (1950), named in the same sentence |
| 5 | `ξ order ≤ 1 / genus-1 Hadamard` | derivation-at-source | **CLOSED — and the flag was an artifact.** The same sentence records its upgrade from prose to the pinned terminal `exists_norm_completedRiemannZeta₀_le_exp` (v0.4.0); *"pinned"* was simply not in the provenance keyword list |

**Nothing here needed more compute than the census left free**, so no re-pricing was required. **One honesty note on the check itself:** only two instances of `d(K)` are corpus-stated (7 and 15) and both match. I also computed the formula at three further signatures, but those have no corpus values to compare against — **a "match" there would have been my prediction agreeing with my prediction**, and they are not counted as confirmations.

---

## §2 — SPECTRAL-REALIZATION (4): three closed at cite, one label corrected

| # | work-order | verdict |
|:--|:--|:--|
| 1 | `FE = Poincaré duality about s=½ ⟹ the zeros live in a self-dual middle cohomology` | **CLOSED at cite** — the content is stated with it (*"the completed ξ = regularized determinant `det_∞(s − Θ \| H¹)`"*), and Deninger's H¹ is named in the same block |
| 2 | `h = ½ threshold of the Lagarias de Branges chain` | **CLOSED — artifact of the ±2-line window.** The statement sits **five lines above**: *"`\|h\| ≥ ½` is the edge-reached regime (unconditional, on-line — the B3 edge), `\|h\| < ½` the centre approach"* |
| 3 | `h=½ threshold` (second occurrence) | **CLOSED**, same statement |
| 4 | `h=0/conductor-1` | **RE-FILED, and the LABEL CORRECTED rather than the check closed** |

**On (4), following the ferry's rule exactly.** The label names a real degeneracy whose content was
**nowhere stated** — it appears inside a compressed spec list. What the source does not supply is
the degeneracy itself. **Corrected in place, `+0 lines, 0 removed`:**

> *h=0/conductor-1 — label corrected 2026-08-05 to state its content: as h → 0 the Lagarias
> differenced family degenerates to the undifferenced conductor-1 case, i.e. to ζ itself, so the
> deformation route loses its parameter exactly where the wall sits.*

---

## §3 — THE PROVENANCE LEDGER'S FINAL STATE

### **35 genuine work-orders → 27 CLOSED · 2 RE-FILED · 6 REMAINING**

| cluster | closed | re-filed | remaining |
|:--|--:|--:|--:|
| Li/Weil | 10 | 1 | 0 |
| cosmology | 5 | 0 | 0 |
| number-field | 5 | 0 | 0 |
| spectral-realization | 3 | 1 | 0 |
| shape-discriminant | 4 | 0 | 0 |
| unclustered | 0 | 0 | **6** |
| **total** | **27** | **2** | **6** |

The six remaining are the unclustered set: they have **no common route** and must be read
individually. **No defect is claimed against any of the 35.**

### The two-axis distinction, on the ledger's face

> **NUMERICALLY VERIFIED and CORRECTLY LABELLED are different axes, and a formula can pass one
> while failing the other.**

**Both re-filings are exactly that case.** `n ≈ 2γ²/ε` verifies perfectly — **as the e-folding
depth, which is not what it is labelled**. `h=0/conductor-1` names a real thing — **with its
content absent**. **A ledger that merges the two axes reports a mislabelled formula as sound**,
which is why the counts above are given as *closed / re-filed* and never as a single "verified"
total.

### What the pass also established about the sweep itself

**Four of this pass's nine closures were extractor artifacts, not gaps** — and that is a finding
about the instrument, not the corpus. Three distinct mechanisms, now named: **truncation at
punctuation** (the `− 1` lost from `d(K)`), **a keyword list that misses "pinned"**, and **a
proximity window narrower than the corpus's paragraphs** (statements five lines away read as
absent). **The retired occurrence proxy was not the sweep's only weak part**, and the 148-term
haystack should be read with all four failure modes in mind, not one.

---

## §4 — THE CENSUS, AT STATE AND UNDISTURBED

| | |
|:--|:--|
| records banked | **242** |
| completeness | contiguous from **t = 0.5 through t = 17.0**, all seven σ-cells per row |
| σ range | [0.52, 1.50] in seven cells |
| excluded band | t < 0.5 (the pole of Λ at s = 1) |
| status | **running**, never interrupted by this pass |

**Resume command of record (verbatim, safe at any time):**

```
cd /d D:\relay && python tools\e16\epstein_census.py
```

Bank: `D:\relay\tools\e16\epstein_census_bank.jsonl`. **The known off-line zero sits at
t = 16.290 — inside the completed range — and the run's own hit-reporting is the check on that.**

---

## §5 — THE BOARD, RESTATED AT THE HOLD

| | state |
|:--|:--|
| **kernel generalization** | **CLOSED** — docstring landed, kernel `5e668b4`; the generalization repair remains available and not taken |
| **R4's compression sitting** | **ANSWERED** — no bound in the Bombieri–Lagarias family (shapes 2 and 3 confirmed, 1 refuted); vacuous at ζ, where the question is RH. No claim about RH |
| **the census** | **RUNNING** — 242 records, t ≤ 17.0; the arithmetic-side validation it exists to serve remains priced and unrun |
| **head 4's characterization** | **PROPOSED**, narrowed form strictly better on all five faces; ℤ/3 refutation condition standing; promotion still waits on the next terminal compiled |
| **BURIAL** | **PROPOSED-WITH-ONE-FACE**, now derived-twice and measured-once (n = 5.9·γ²/δ); promotion test unrunnable until a second face with an exponent exists |
| **consolidation / wave-edit** | **RUN** — four scope checkpoints landed with stated diffs; provenance ledger closed to 27/2/6 |

**Nothing on the board is decaying.** The two live things are the census and the six unclustered
work-orders; everything else is at rest in a stated state.

---

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `8273013` → this pass's commit |
| relay | `24c2b91` → this report's commit |
| SIDE-lv-conservation | `2f71068` — unmoved |
| SIDE-kernel | `5e668b4` — unmoved |
| rail | `de621b1` / `2147a03` — unmoved and unmoving |

Nothing deposits. **Hold.**
