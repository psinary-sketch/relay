# Four filings and one pricing — 2026-08-05

Pins at open: PLACE-papers `059d6d9`; relay `1090907`; lv main `2f71068`; kernel `44895f9`.
Rail at the post-rename baseline. Nothing deposits.

---

## §1 — I-7's SECOND RUN, FILED — with its operational form corrected before filing

**The concern, stated once and then built through.** The ferry's proposed operational form for
the second stage was: *perturb the inputs' real parts and re-run; if the statistic does not move,
the instrument has no placement power.* **I tested that form against the case it was written for
before filing it as standing, and it does not catch it.**

Toeplitz min-eigenvalue at K = 400, ζ arm, real parts perturbed by η:

| η | min-eig | moved? |
|--:|--:|:--|
| 0 | −2.104×10⁻¹⁰ | — |
| 10⁻⁹ | −7.62×10⁻¹¹ | no (below the floor) |
| 10⁻⁷ | −1.674×10⁻⁶ | **yes** |
| 10⁻⁵ | −2.441×10⁻⁴ | **yes** |
| 10⁻¹ | −11.08 | **yes** |

**Twelve orders of magnitude. The perturbation test PASSES the Li-Toeplitz pipeline.**

**Why, and this is the filing's content: perturbing the inputs tests the STATISTIC; substituting
the object tests the PIPELINE.** The statistic's placement sensitivity was never in doubt — that
is what makes it a candidate at all. What failed is that **no perturbation of those inputs is
ever taken from the object**: they are constructed at 1/2.

**So the screen is filed with two tests, one per stage, each with the case it catches:**

- **STAGE 1 (the statistic) — PERTURBATION.** Move the real parts. If the statistic does not
  move, its definition cannot bear on placement. *Catches π₀.*
- **STAGE 2 (the pipeline) — SUBSTITUTION.** Replace the object's data with **arbitrary data of
  the same class**. If the verdict does not change, the pipeline is reading its own construction.
  *Catches the Li-Toeplitz pipeline.*

The controls recorded as the form's worked example, at K = 400:

| input set | min-eig | ratio to ζ |
|:--|--:|--:|
| ζ's 1200 banked ordinates | −2.104×10⁻¹⁰ | 1 |
| 1200 uniform random ordinates | −1.804×10⁻¹⁰ | 0.86 |
| 1200 in arithmetic progression | −1.729×10⁻¹⁰ | 0.82 |
| **1200 copies of a single ordinate** | −3.157×10⁻⁹ | 15 |

**Even 1200 copies of one number return the same verdict** — which is the substitution control's
design rule, now filed with it: *choose the substitute as far from the object as the class
allows, because the degenerate case is the most informative.*

**And the cheapest check of all, filed above both: read the licence against the build.** Face 1
licensed the channel because λₙ is computable *without* placement input; the pipeline built used
placement input. One sentence, compared, before any compute is spent.

Filed to `phase1.5/method/INSTRUMENTS.md` under I-7.

---

## §2 — JOHANSSON'S DATUM, FILED (CLASSICAL-AT-CITE)

**λ₀ … λ₁₀₀₀₀₀ computed rigorously, with certified error bounds, all positive.** Fredrik
Johansson, *Rigorous high-precision computation of the Hurwitz zeta function and its
derivatives*, Numerical Algorithms (2015); arXiv:1309.2877; implemented in Arb. Accuracy between
roughly 33 000 and 2 900 digits; the computation manipulated on the order of 10¹⁰ bits.

**Held as a corpus datum with its citation: the unconditional verification range of Li
positivity is n ≤ 10⁵.**

**Explicitly not evidence for RH.** A verification range is a statement about what has been
checked, not about what is true beyond it. The corpus's own Π₁ filing (F.2026-08-05-b) already
carries the direction of inference that *does* hold — a false Π₁ statement has a finite
counterexample — and this datum's honest content is the dual one: **10⁵ coefficients have been
checked and none is the counterexample.** It bounds where a counterexample can be, and nothing
more.

---

## §3 — THE R4 LINK MADE

The registered-and-unrun compression question — *does non-negativity of finitely many λₙ force
non-negativity of all?* — **now names Johansson's family as its data set.**

**The link, stated as the finding it is:** the single OPEN cell in the five-register compression
table and the subject's best-verified sequence are **the same object**. R4 is open because it is
the only Π₁-native register — the only one handing you a sequence you can index and check — and
Johansson's computation is what indexing-and-checking that sequence has actually produced, to
n = 10⁵ with certified bounds.

**What the link changes about the question, and what it does not.** It changes the question's
*starting position*: outcome-shape 2 (a counterexample-shape) now has 10⁵ certified-positive
coefficients standing against it, so any construction must live beyond that range or explain why
it does not appear within it. It changes nothing about outcome-shapes 1 and 3 — a bound either
exists or provably cannot, and no amount of verified range bears on either.

**Still UNRUN, still priced for breadth.** The registration's three pre-named outcome-shapes and
its prerequisite list stand unaltered; this pass adds one line to it — the data set — and nothing
else. Recorded as an amendment to the registration at relay
`reports/2026-08-05-r1-cell-and-split.md` §3, and in OPEN_TRAILS beside the queue line.

---

## §4 — THE INSTRUMENT'S OPERATIONAL CONTENT, FILED AS A SPEC SHEET

Refused as a ζ measurement, retained as a calibrated detector. Filed to INSTRUMENTS.

- **DEPTH ECONOMY — 26×, measured.** Toeplitz detects the witness at **K = 200** (moments
  c₀…c₁₉₉); the magnitude form needs **n ≈ 5101**. **This ratio is the reformulation's entire
  operational yield.**
- **RESOLUTION LAW — signal ∝ δ².** Fails at **δ ≈ 3×10⁻⁶**, exactly where a δ² signal meets the
  float64 floor. **Purchasable as √floor** — at 50 digits the same order reaches δ ≈ 2×10⁻²³.
- **HEIGHT DEPENDENCE — γ².** Floor δ ≈ 3×10⁻⁶ at γ = 16.29; 1.1×10⁻⁴ at γ = 100; 1.1×10⁻² at
  γ = 1000.
- **THE DEPTH FORMULA, CORRECTED.** γ²/δ is the **e-folding** depth and is accurate as such:
  585.4 against the exact 586.4, 0.2%. The **detection** depth carries a log factor:

  > **n_det = (γ²/δ) × log(threshold × background)** — checks as 586.4 × log 6000 = **5101**

  **The omission sits in two places in the corpus**, not one: the ferry that stated γ²/δ as the
  detection depth, and **VERIFICATION_LOOM §2165**, where the crossing against λ_A ~ (n/2)log n is
  given as n ≈ 2γ²/ε — the crossing condition n·δ/γ² = log((n/2)log n) carries the same log factor
  on its right. **One formula corrects both.** The corpus's own line had it first and had it the
  same way, which is worth recording: this is not an imported error.
- **THE REGULARIZATION NOTE, which bounds what the reformulation can be.** c₀ = Σ_ρ 1 **diverges**
  — so the sequence whose Toeplitz matrix this is does not exist without regularization, and the
  regularized object is **λₙ itself**. **The yield is depth economy, not a new object.** The
  truncated sequence the instrument actually builds is a third thing, whose relation to λₙ is set
  by the truncation height.

---

## §5 — THE EPSTEIN ZERO CENSUS, PRICED (named, not run)

**Object.** The disc −23 Epstein zeta of the principal form x² + xy + 6y², h(−23) = 3 — a
degree-2 L-function of conductor 23. Davenport–Heilbronn guarantees off-line zeros; the programme
has one located (β = 0.9533, γ = 16.290, doubly sourced).

**The census must be 2-D.** Argument-principle winding over rectangles covering σ ∈ [0.3, 1.7],
t ∈ [0, T]. **A critical-line scan is not an option**, because it would impose the real part and
reproduce exactly the defect §1 just diagnosed. **This is the whole reason the census is the only
route to a measurement of placement rather than a calibration of a detector.**

**Cost, stated in advance** (0.1 × 0.5 cells, ~200 boundary evaluations per winding integral,
~30 ms per Epstein evaluation at 30 digits via the Bessel-K expansion):

| T | zeros N(T) | cells | evaluations | wall clock (mpmath) |
|--:|--:|--:|--:|--:|
| 100 | 106 | 2 800 | 5.6×10⁵ | **~4.7 h** |
| 1 000 | 1 795 | 28 000 | 5.6×10⁶ | ~47 h |
| 10 000 | 25 274 | 280 000 | 5.6×10⁷ | ~467 h |

A compiled implementation, or the ζ·L + Hecke-character decomposition
ζ_{Q₁} = ⅓[ζ·L(·,χ₋₂₃) + L(·,ψ) + L(·,ψ̄)], would cut these by one to two orders. **The T = 100
census is a day's compute and contains the known witness.**

**Detector reach the census would buy:**

| γ | δ_min, float64 | δ_min at 50 digits |
|--:|--:|--:|
| 16.29 | 3×10⁻⁶ | 2.0×10⁻²³ |
| 100 | 1.1×10⁻⁴ | 7.6×10⁻²² |
| 1 000 | 1.1×10⁻² | 7.6×10⁻²⁰ |

**THE PRICING'S HONEST CONCLUSION, which is not the one the framing invites.** Once the census
exists, its real parts *are* the placement measurement — and feeding them to the Toeplitz detector
tells you what the census already told you. **The census does not make the truncated-zero detector
a measurement; it makes the detector redundant.**

**The version that is worth the money is a different one, and it is the one to open if any:** use
the census as **ground truth** to validate the *arithmetic-side* channel end to end — compute the
Epstein analogue of λₙ from its Dirichlet coefficients, with no zero locations as input, and check
whether it detects the DH zeros at the depth the resolution law predicts. **That is the only
experiment in this family that would license the arithmetic-side channel on ζ**, because it is the
only one where a known-answer object is measured by a pipeline that never sees an answer.
Prerequisite beyond the census: the Bombieri–Lagarias arithmetic form for a degree-2 L-function,
and working precision on the order of n digits — the cost Johansson paid, and the reason his
n = 10⁵ needed ~10¹⁰ bits.

**Named, priced, NOT RUN. Author's call to open, and the recommendation is that if it opens it
opens as the ground-truth validation and not as the detector feed.**

---

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `059d6d9` → this pass's commit |
| relay | `1090907` → this report's commit |
| SIDE-lv-conservation | main = `2f71068` — unmoved |
| SIDE-kernel | `44895f9` — unmoved; the generalization work-order still open at the author's call |
| rail | `de621b1` / `2147a03` — at the post-rename baseline |

Instrument: `tools/audit/i7_second_run_and_epstein_price.py`. Consolidation DEFERRED.
Nothing deposits.

## SOURCES

- [Johansson, *Rigorous high-precision computation of the Hurwitz zeta function and its derivatives*](https://arxiv.org/pdf/1309.2877)
- [Arb: Efficient Arbitrary-Precision Midpoint-Radius Interval Arithmetic](https://arxiv.org/pdf/1611.02831)
