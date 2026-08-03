# W-LINK the one-law test · E-20 face 4 the constant identified · the p₀-translation table — 2026-08-03

The ferry's three moves. Pins at open: PLACE-papers = `3d63bd2`; relay = `b9e68b9`; lv
`14720d9`, kernel `44895f9` — unmoved; rail at the post-rename baseline. Out-of-sample
predictions stated BEFORE computing. Nothing deposits.

## Registered expectations (VERBATIM from the ferry)

**W-LINK:** *"YES — w(n) is c-law-determined and the collapse reduces to c₁'s scale law (two
mysteries, one address); then the out-of-sample double test: predict BOTH c₁(56) and w(56)
from the fitted laws, THEN compute the n=56 stratum and adjudicate."* Candidate recognitions
for the ×8, stated before the n = 56 data: 2³ per length-step · 8^(Δg/4) ·
polynomial-corrected geometric. *"Null branch: the collapse has a second driver — named,
first-class."*

**E-20 face 4:** *"the constant IDENTIFIES as the density normalization within the
oscillation band [1.00, 1.31] — the first quantitative cell of the identification; the
opaque branch files the measured constant as a standing datum with its precision."*

**The p₀-translation table:** question grade, internal-until-fruit; no forcing.

## MOVE 1 — W-LINK: THE ONE-LAW TEST

**The in-sample n = 48 data lands, and it discovers a SCOPE BOUNDARY (filed before the
predictions):** the n = 48 flip polynomial has **degree 2, not 4**, and its constant couples
to the FIRST power of the extremal lead with a new coefficient — **c₀ = −(21/2)·lead(H_ext48)
exactly** (the same denominator appears on both sides: −168/D vs 16/D). The cause is
structural, not a law-failure: extremal-48 is a **DOUBLE-STEP stratum** (d = 12: A₄ = A₈ = 0;
genus collapse Δ8), while the entire calibrated family (24, 32, 40) is single-step (d = 8;
Δ4) — and the single-step family is COMPLETE at three members (4⌊n/24⌋+4 = 8 exactly for
24 ≤ n ≤ 40). The additive law −((n+16)/16)·p₀⁴ is a SINGLE-STEP-family law; the double-step
kind has its own coupling (exponent 1; coefficient −21/2 at its first member). **The
one-law test's first half adjudicates YES in structure:** w(48) = 0.00795 is EXACTLY the
positive root of the measured quadratic (1 + 44670.04·ε − 5631802.6·ε² = 0 at ε = 0.007956)
— **the window IS c-law-determined, and the collapse reduces to the coefficient scale ratio
w ≈ r₁/|r₂|** (two mysteries, one address, as registered — with the address now carrying a
stratum-kind index).

**THE n = 56 PREDICTIONS, REGISTERED BEFORE COMPUTATION (n = 56 is double-step, d = 12 —
the same kind as 48, its second member; one in-family calibration point, so the predictions
carry candidate laws, stated):**
1. **deg Ñ(56) = 2** (the double-step kind's degree).
2. **c₀(56) = −(25/2)·lead(H_ext56)** — exponent 1 (the kind's coupling) with the candidate
   coefficient law −(n−6)/4 (which gives −21/2 at 48 ✓).
3. **r₁(56) ≈ 3.6×10⁵**, band [2.5×10⁵, 4.7×10⁵] — the ×8-per-length-step scale candidate
   (the registered recognitions: 2³ per step · 8^(Δg/4) · polynomial-corrected geometric).
4. **w(56) ≈ 1.0×10⁻³** primary (the c-law route: w ≈ r₁/|r₂| with r₁ ×8, r₂ ×64), wide
   bracket [2×10⁻⁴, 1.2×10⁻³] (the accelerating-ratio alternative gives ≈ 2.6×10⁻⁴).

**THE n = 56 ADJUDICATION (instrument `tools/e3/n56_test.py`; genus-29 certificates):**

- **Prediction 4 (the window) — CONFIRMED:** w(56) ∈ (0.0007841, 0.0007842) by exact-sign
  bisection (no interpolation involved) — **inside the registered bracket [2×10⁻⁴,
  1.2×10⁻³], within 22% of the primary 1.0×10⁻³** (the c-law route with the ×8/×64 scale
  guess). The w-series now runs 7.1638 · 1.2718 · 0.17549 · 0.00795 · 0.000784 (ratios 5.6 ·
  7.2 · 22.1 · 10.1 — the ratio RETREATS at the within-kind step 48 → 56, consistent with
  the 40 → 48 jump being partly the stratum-kind crossing).
- **Predictions 1–3 (degree, c₀-coupling, r₁) — NOT ADJUDICABLE this sitting, flagged:** the
  n = 56 polynomial reconstruction used 10 samples, and the returned "degree 9" is the
  always-fits fallback (degree + 1 = sample count — the verification is vacuous there); the
  no-L-divisibility and the non-clean c₀ ratio inherit the same unreliability. **The full
  ~40-sample interpolation at genus 29 is the priced follow-up; no verdict is claimed on
  these cells.** (An instrument lesson filed: degree-discovery requires samples ≫ candidate
  degree — the earlier strata used 45+.)

**THE ONE-LAW VERDICT at its earned grade: YES IN STRUCTURE, with a stratum-kind index.**
The window is c-law-determined (verified exactly at n = 48: the bisected window IS the
measured polynomial's root) and the collapse reduces to coefficient scale ratios (w ≈
r₁/|r₂| at the double-step kind; the c₃/c₄ balance at the single-step kind) — two mysteries,
one address, as registered — and the address carries a stratum-kind index discovered
in-sample (single-step: degree 4, lead²-coupling, the −((n+16)/16) law; double-step: degree
2 at its first member, lead¹-coupling, −21/2). The out-of-sample window confirms; the
out-of-sample coefficients await proper sampling. The ×8 recognition candidates stand
registered, unadjudicated. The null branch (a second driver) did NOT fire on the window; the
40 → 48 ratio jump is attributed to the kind-crossing at this sitting's grade.

## MOVE 2 — E-20 FACE 4: THE CONSTANT

**Instrument** (`tools/e16/constant_control.py`; the control = synthetic zeros from the
SMOOTH Riemann–von Mangoldt counting main term, same construction end-to-end: β̃ = 1/(2γ̃)²,
moments from 3000 points + tail at dps 150, Jacobi at dps 220 per the precision law — the
precision-floor note fired once more on the first pass at dps 60/depth 12 and was corrected).

**VERDICT: the registration CONFIRMED — the constant IDENTIFIES as the DENSITY
NORMALIZATION.** The smooth-density control reproduces the tracking constant almost exactly:

| | mean of α_k/β_k | oscillation |
|:--|:--|:--|
| ζ (measured, k = 3..16) | ≈ 1.12 | ±0.15 (band [1.00, 1.31]) |
| smooth-density control (k = 3..10) | **1.1157** | **±0.0015** |

The ≈1.12 carries NO arithmetic content — it is the counting function's normalization,
reproduced by a measure that knows only the density. **The identification's first
quantitative cell passes, and the decomposition it yields is the finding:** the string
diagonal's MEAN is density (identified); ζ's arithmetic lives in the OSCILLATION about it —
**two orders of magnitude larger in ζ (±0.15) than in the smooth control (±0.0015)**. The
oscillation amplitude is a new measured object: the arithmetic signal in the string's
diagonal — the zeros' fluctuations against their own density, seen in the Hamiltonian
coordinate. (Its structure — GUE-shaped? — is an obvious unpriced continuation, noted for
the board.)

## MOVE 3 — THE p₀-TRANSLATION TABLE

**(Question grade; internal-until-fruit; no forcing.) The toy template, stated once:**
p₀ is (i) a NORMALIZED SELF-DATUM of the object's own extremal structure (the first zeta
coefficient = A_d/((q−1)C(n,d)), the minimal-weight count in its natural normalization);
(ii) its SQUARE IS FREE from symmetry (lead(H) = p₀², the two-line FE theorem); (iii) the
ATTACK SCALES as p₀⁴ (the additive law's currency); (iv) the WINDOW is priced in p₀'s
currency (the flip polynomials' denominators stay C(n,4)-adjacent).

| ζ-candidate | (i) self-datum | (ii) free square | (iii) attack scaling | (iv) currency | grade |
|:--|:--|:--|:--|:--|:--|
| the BN distance d_N | a distance to a target, not a datum of ζ's own extremal structure | — | — | its ceiling is zero-indexed (BDBLS) | **PARTIAL** (wall-distance yes; self-datum no) |
| Λ's flow coordinate t | a deformation parameter, external to the object | — | — | the pencil's own coordinate | **PARTIAL** (the wall at 0 ✓; not a self-datum) |
| the string mass 4s₁ = Σ 1/γ² = 0.0231049931 (computed, both routes) | ✓ the meter's own FIRST MOMENT — a normalized self-datum of the zero structure, the closest analogue of "the certificate's first coefficient" | not exhibited | not exhibited | the moment currency ✓ (the Hankel/Jacobi data are s₁'s family) | **PARTIAL-leaning-FITS** on (i), (iv); (ii)–(iii) open |
| γ₁ (the lowest zero) | the spectral EDGE — the toy's β₁-analogue, a different role than p₀ | — | — | — | **FAILS** (right object, wrong slot) |
| the N(T) normalization (the density) | the counting law, not a single datum | — | — | ✓ the currency in which the burial/depth laws are written (the meter's reach, the Lehmer shadow's address) | **PARTIAL** ((iv) only) |
| *the FE-evenness itself (found row, READING)* | — | **✓ THE CLAUSE THAT TRANSLATES CLEANLY: the functional equation makes ξ a function of u = z² — the symmetry's free square IS the u-coordinate at ζ**, exactly parallel to lead = p₀² being MacWilliams' free gift | — | — | **FITS clause (ii) alone** |

**The table's honest yield:** no single candidate fits the whole template — but the clauses
distribute: (ii) translates cleanly (FE-evenness = the free square, a READING worth its row);
(i) has s₁ as the nearest self-datum; (iv) has the density normalization. **The front-runner
is a composite, which is itself the finding at question grade: p₀'s true ζ-analogue — a
single normalized wall-distance self-datum whose square is symmetry-free and whose powers
price the attack — is NOT among the classical coordinates; the table names the vacancy.**
The vacancy is the p₀-translation question's sharpened form, and it rides the Forward
unchanged.

## CLOSING — pins, slate, board

**The slate re-printed:** W-LINK — **RUN: one law in structure (the window = the flip
polynomial's root; the collapse = coefficient scale ratios), the stratum-kind index
discovered (single-step vs double-step, with their distinct couplings), the out-of-sample
window CONFIRMED at n = 56 (0.000784, in-bracket), the coefficient cells awaiting proper
sampling (priced follow-up)** · E-20 — **face 4 RUN: the tracking constant IDENTIFIES as the
density normalization (control mean 1.1157 vs measured ≈1.12); the arithmetic signal = the
oscillation, 100× the control's — a new measured object; its GUE-shape question the unpriced
continuation** · the p₀-translation table — **OPENED: the free-square clause translates
(FE-evenness), s₁ the nearest self-datum, the density the currency — and the composite names
a VACANCY: p₀'s true ζ-analogue is not among the classical coordinates** · E-3 (the additive
recipe per stratum-kind; c₁ opaque) · E-7b (two cells) · E-16 (d(t) exponent) · the rest
standing. **Consolidation DEFERRED, standing.**

**The board restated, the one-law verdict at its head:** TWO MYSTERIES, ONE ADDRESS — the
collapse and the coefficient contest are one object (the flip polynomial), its root the
window, its scale-laws the collapse, its couplings indexed by stratum-kind; the out-of-sample
window landed in-bracket at the fifth stratum. Beside it: the string's diagonal mean is
density (identified by control) and its oscillation is arithmetic — the meter now separates
the two; and the p₀-translation table names the vacancy the classical coordinates leave.

| repo | pin |
|:--|:--|
| PLACE-papers | `3d63bd2` at open → this sitting's commit (OPEN_TRAILS addendum) |
| SIDE-lv-conservation | main = `14720d9` — unmoved |
| SIDE-kernel | `44895f9`; v1.7 — unmoved |
| relay | this report's commit; instruments `tools/e3/n56_test.py`, `tools/e16/constant_control.py` |
| rail | untouched — at the post-rename baseline |

Keystone untouched this sitting (the next touch's cargo accumulates: the one-law verdict ·
the density/oscillation decomposition · the vacancy row). Mirror rebuilt at the papers pin
on commit. Nothing deposits.
