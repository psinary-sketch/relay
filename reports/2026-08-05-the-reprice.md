# THE RE-PRICE — before any seventh point — 2026-08-05

The registration's own clause honored: UNDISCRIMINATED re-prices, it does not auto-spend.
Banked data + one calibration build. Pins at open: PLACE-papers = `4eef74a`; relay =
`b8ec6be`; lv `14720d9`, kernel `44895f9` — unmoved; rail at the post-rename baseline.
Nothing deposits.

## (1) THE ERROR BAR — registered HALF-CONFIRMED, with a sharper fact

The J-systematic, measured by re-deriving the shared ladder from the J = 960 and J = 1,200
objects:

| K | R | c(J=960) | c(J=1200) | \|Δ\| | \|Δ\| / own increment |
|--:|--:|:--|:--|:--|:--|
| 16 | 8 | 0.578133 | 0.578066 | 6.6×10⁻⁵ | — |
| 32 | 17 | 0.729832 | 0.729836 | 3.4×10⁻⁶ | 2×10⁻⁵ |
| 64 | 36 | 0.825489 | 0.825790 | 3.0×10⁻⁴ | 0.3% |
| 128 | 74/75 | 0.886588 | 0.882448 | **4.14×10⁻³** | 7.3% |
| 200 | 118 | 0.932074 | 0.930494 | 1.58×10⁻³ | 3.3% |
| 256 | 153 | — | 0.949762 | (no J-pair) | — |

**Registered:** *"the systematic is comparable to the prediction separation at the tail…in
which case NO added rung discriminates until J grows with K."* **Measured: NOT comparable to
the separation** (0.0041 vs 0.0182 — a factor of 4.4) — **but exactly comparable to the
DISCRIMINATION MARGIN the sixth point achieved (0.00416).** The sharper fact: **the sixth
point's UNDISCRIMINATED verdict lay entirely inside the systematic — that measurement could
not have discriminated wherever the point fell.** The clause's operative half stands: J must
grow with K, or the added rung buys nothing.

## (2) THE LADDER-DEPENDENCE CHECK — registered CONFIRMED; a front-runner retires

Increment ratios under the index-geometric assumption: 0.6322 · 0.5905 · 0.848 · 0.401 —
across ladder steps ×2, ×2, ×2, ×1.5625, ×1.28. **The "constant ratio" was read across
DOUBLINGS; the fit treats unequal steps as equal.** Intrinsic restatement: a constant ratio
across doublings *is* a power law A/K^p (2^−p = ratio), and the three doublings give
inconsistent exponents p = 0.6615 · 0.7601 · 0.2378; the power law at their mean (p = 0.553)
predicts the 200→256 increment ratio 0.4558 against 0.401 observed. **VERDICT: family (a)
does not survive intrinsic restatement — it is the power law seen through a doubling ladder,
and its implied limit 0.9927 was a ladder artifact.** The W-CONVLAW runner-up, which carried
the near-unity limit, is retired.

## (3) THE ASYMPTOTIC-WINDOW FIT — the registered clustering FAILS, first-class

Drop rule, pre-committed before fitting: drop R < 30, or J-systematic > 20% of the point's
own increment. Dropped: K = 16 (R = 8), K = 32 (R = 17). Surviving tail: K = 64, 128, 200,
256. Tail limits in the intrinsic variables: **1/K → 0.97969 · 1/R → 0.97624 · 1/logK →
1.3178.** **Spread 0.342 — NO clustering near 1.01–1.02.** Per the registration, this
**kills the pre-asymptotic-transient reading** and files first-class: two variables agree
near 0.977, the third lands at 1.32, and nothing in the data selects between them.

## (4) THE CALIBRATION STANDARD — registered CONFIRMED

Standard: the smooth control with ONE atom displaced by a known amount (atom 60, +0.30 of
its local gap), run end-to-end through the identical pipeline; in the resolved band the
nodes are the atoms to <1%, so the exact Δosc is computable from the atom positions.

| K | R | measured Δosc | exact Δosc | bias (c-units) | bias / 0.0182 |
|--:|--:|:--|:--|:--|:--|
| 64 | 36 | 0.0011189 | 0 (atom outside band) | 1.06×10⁻⁵ | 0.06% |
| 128 | 74 | −0.2275161 | −0.2611459 | 1.21×10⁻⁴ | 0.67% |
| 200 | 119 | −1.6427639 | −1.6521589 | 1.85×10⁻⁵ | 0.10% |
| 256 | 153 | −2.3373018 | −2.3422675 | 7.15×10⁻⁶ | 0.04% |

**The pipeline's bias is ≤ 0.7% of the prediction separation at every ladder point** — the
measurement chain is trustworthy at this resolution; no c-sequence verdict re-opens on
pipeline grounds. **Scope, stated:** this calibrates the chain (moments → blocked Cholesky →
eigen → band → statistic) against an exact answer for a known displacement; it does not
calibrate sensitivity to global fluctuation structure. (The K = 64 row doubles as a null
check: the displaced atom sits outside that band, exact = 0, measured 1.1×10⁻³ raw = 1.06×10⁻⁵
in c-units — the noise floor.)

## (5) THE RE-PRICE OF K = 384 — the gate PASSES, the price does not

**The contest has changed:** family (a) is retired (item 2), so the surviving intrinsic
families are **1/K (limit 0.980)** and **1/logK (limit 1.318)** — i.e. *does c settle near
0.98, or keep climbing toward ~1.32?*

**Predicted separation at K = 384: 0.018** (1/K → 0.953099; 1/logK → 0.971101).
**Measured uncertainty: ~0.004** (J-systematic, dominant) **+ ~0.0001** (calibration bias,
negligible). **Separation exceeds uncertainty by ≈ 4.4× — the statistical gate PASSES; K =
384 would discriminate.**

**But the price, computed from the measured cost curve, does not pass a sanity test:** the
precision law puts K = 384 at **dps ≈ 4,300**; the measured zetazero cost (1.1 s at dps 620 ·
4.7 s at 1,300 · 24 s at 2,100 · 54 s at 2,700 — scaling near dps^2.7) projects **≈ 195
s/zero**, and holding the J/R ratio that made the systematic tolerable requires **J ≈ 1,800**
atoms: **≈ 97 hours of atom generation alone**, plus a few hours of factorization — **four to
five days of continuous machine time.** (K = 512 buys separation 0.027 at a still steeper
price.)

**THE RE-PRICE VERDICT: K = 384 is statistically justified and economically prohibitive at
this ladder. The recommendation — the author's call — is the re-route the ferry named:
derive the limit from the sum-rule identity rather than measure it.** The measurement path's
cost now doubles with each rung while the separation grows only linearly; the identity path
is a research-reach derivation with no compute wall. Priced separately; not run here.

## (6) THE FOUR CHEAP FILINGS (executed; the ledger entries carry them)

1. **The #4 role, re-derived:** the programme's exclusion apparatus is a codimension-≥2
   instrument by construction (the Codimension Dichotomy, `TRIVIUM_IDENTITY_SUBSPACE`
   Prop 8.16: on-line zeros are codim 1, off-line codim 2), and `h2` is a codimension-1
   question — **SIDE cannot supply codim-1, and no sharpening of it will.** What this era
   added in that role's place: the demonstration that the missing kind can be **BUILT** —
   the selection-kind supplier constructed, certified, and dissected at toy scale (the
   genus ≤ 5 theorem; the lead law; the residue mechanism).
2. **The codimension/arity unification (UAC entry):** codim-1 = a sign condition on a
   continuum = pair-index definiteness — **one condition seen in two views**; the
   codimension language and the arity language name the same wall from the geometric and
   the index side.
3. **The conditional meta-theorem, with its naming test:** the RH/Yang–Mills
   one-meta-theorem reading (FINDINGS, the DomainOstrowski structure) is **conditional on
   the agreement relation being GROUP-generated rather than merely FAMILY-generated** — the
   test is to NAME THE GROUP; until it is named, the meta-theorem is a family resemblance,
   not a theorem.
4. **The Ξ.10 trigger moved:** the Inversion Analyzer's trigger now fires **before any
   moment-positivity citation** — coordinate first, positivity second (this arc cited
   Hamburger/Stieltjes/Hankel positivity repeatedly without the coordinate check; the
   trigger's new position makes that check mandatory upstream).

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `4eef74a` at open → this pass's commit |
| SIDE-lv-conservation | main = `14720d9` — unmoved |
| SIDE-kernel | `44895f9`; v1.7 — unmoved |
| relay | this report's commit; instruments `reprice_123.py`, `calibration_std.py` |
| rail | `de621b1` / `2147a03` — at the post-rename baseline |

Keystone cargo unchanged (seven-deep, held). Mirror rebuilt with the standing check.
Nothing deposits.
