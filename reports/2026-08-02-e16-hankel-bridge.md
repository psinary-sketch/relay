# E-16 — THE HANKEL BRIDGE: the toy's mechanism carried to ζ · E-7b's entry face — 2026-08-02

The ferry's E-16 (~1.0) with E-7b's entry face riding behind (~0.4). Pins at open:
PLACE-papers = `70b5531`; relay = `de478a4`; lv `14720d9`, kernel `44895f9` — unmoved; rail at
the post-rename baseline. Nothing deposits.

## Registered expectations (VERBATIM from the ferry, recorded BEFORE computation)

**(a)** *"at t = 0, PSD to every reachable depth (RH-consistent)"* — ξ's Hankel forms from the
power sums of the reciprocal squared zeros, finite truncations at increasing depth.

**(b)** *"at t < 0, the signature FLIPS at some finite depth d(t) — the flip-depth as the new
detection instrument, compared head-to-head with the cumulant bracket's k > 12 stall."*

**(c)** *"d(t) grows as t → 0⁻ (the knife-edge measured in the wall's own form)."*

*"Any registration failing files first-class."*

## §1 — THE CLASSICAL SPINE AT CITE

| row | statement | grade |
|:--|:--|:--|
| **Hermite** | a real polynomial has all roots real ⟺ the Hankel matrix of its root-power sums is PSD (signature counts distinct real roots) | CLASSICAL-AT-CITE (the toy dissection's §-instrument; face-3 report) |
| **Hamburger** | a sequence is the moment sequence of a positive measure on ℝ ⟺ all Hankel matrices [m_{i+j}] are PSD | CLASSICAL-AT-CITE |
| **Stieltjes** | …of a positive measure on [0, ∞) ⟺ additionally the shifted Hankels [m_{i+j+1}] are PSD — the INTERVAL/positivity clause in moment language | CLASSICAL-AT-CITE |
| **Jensen–Pólya** | RH ⟺ hyperbolicity of all Jensen polynomials of ξ (all degrees d, all shifts n) — the reality layer as the WHOLE wall for ζ (the face-3 structural note: ζ fuses what the toy separates) | CLASSICAL-AT-CITE |
| **Griffin–Ono–Rolen–Zagier** | for each degree d, the Jensen polynomials are hyperbolic for all sufficiently large shifts n — via Hermite-polynomial approximation of the high-shift regime ([PNAS 116 (2019) 11103–11110](https://www.pnas.org/doi/10.1073/pnas.1902572116), [arXiv:1902.07321](https://arxiv.org/abs/1902.07321)) | THEOREM-AT-CITE |

**THE LADDER SORT, stated:** GORZ is the **drift/edge half of the reality layer** — hyperbolicity
proved in the high-shift (large-n) regime, where the Hermite asymptotic dominates; the
**low-shift centre** (small n, all d — where the actual zeros' pair structure lives) is the
standing wall. This is the edge-vs-centre anatomy again: the provable half is the
asymptotic/edge half (single-index-flavored, drift-dominated), the open half is the centre —
the same sort that placed single-index positivity at σ = 1 and the pair-index content at the
critical line.

**THE E-8 COMPATIBILITY NOTE (the barrier respected):** the Hankel form does not COMPOSE
one-variable data into a pair form — it INTRODUCES the pair structure directly: the matrix
[s_{i+j}] is pair-indexed from birth ((i,j) ↦ s_{i+j}), and its positivity is a genuinely
two-variable statement (a quadratic form on coefficient vectors). The composition barrier
(`composition_barrier`, lv `14720d9`) bars transport-sound COMPOSITION of criterion-layer
data into a carrier; direct introduction is the other route, and the toy wall is its worked
instance: at genus ≤ 5 the introduced pair form (Hermite–Hankel over the certificate) is
POSITIVE and proves confinement. The barrier and the bridge are compatible: the bridge pays
the pair-index cost up front instead of trying to compose it from one-variable pieces.

## §2 — THE COMPUTATION

**Instrument** (`tools/e16/hankel_bridge.py`): H_t's even Taylor moments by quadrature
(mpmath, dps 150 and 220 — the two-precision double-source; s-agreement ≤ 5×10⁻¹⁴⁵ at every
t); power sums s_k = Σ_j (2γ_j)⁻²ᵏ of the reciprocal squared zeros via the log-series
recurrence; the two Hankel layers [s_{i+j+1}] (reality/Hamburger) and [s_{i+j+2}]
(positivity/Stieltjes — the toy's interval clause in moment language); leading principal
minors after sign-preserving diagonal scaling; a minor's sign accepted only where both
precisions agree. **Independent cross-check at t = 0:** the integral route against explicit
zero-sums over the first 300 zeros (mpmath.zetazero) — agreement 4.3×10⁻⁵ at k = 2 shrinking
to 3.4×10⁻¹⁸ at k = 6, exactly the J-truncation tail's predicted profile: both routes
validated (s₂ = 2.3232874×10⁻⁶, s₃ = 2.2527177×10⁻⁹, …).

**The flip-depth table (resolved depth 12 at every t):**

| t | reality layer d(t) | positivity layer d(t) |
|--:|:--|:--|
| 0 | no flip (PSD through 12) | no flip (PSD through 12) |
| −0.1 | no flip through 12 | no flip through 12 |
| −0.3 | no flip through 12 | no flip through 12 |
| −5 | **9** | 9 |
| −15 | **6** | 5 |
| −30 | **5** | 4 |
| −50 | **4** | 4 |

**Verdicts against the registrations:**

- **(a) CONFIRMED.** At t = 0 both Hankel layers are PSD to every resolved depth —
  RH-consistent, and the deepest PSD certificate of ξ's moment forms this programme has
  computed.
- **(b) SPLIT — the informative outcome, filed first-class.** The flip-depth instrument
  WORKS: it detects the t < 0 non-reality at d = 9, 6, 5, 4 for t = −5, −15, −30, −50 —
  strictly out-reaching the cumulant meter's regime (the flip at t = −5 reads moment data to
  order z³⁸, and detects; the κ-bracket stalled at k > 12 seeing nothing anywhere). But at
  the REGISTERED targets t = −0.1, −0.3 there is NO flip within resolved depth 12: in the
  knife-edge region both instruments are blind at reachable depth. The head-to-head verdict:
  **the Hankel meter strictly dominates the cumulant meter where either sees at all, and the
  small-|t| non-reality (guaranteed by Rodgers–Tao) hides in the DEEP TAIL** — the complex
  pairs at small |t| sit at heights where thousands of real zeros lie above them in the
  β-ordering, beyond any low-depth quadratic form's power to localize. The certified
  zero-information floor of the arity step has a measured cousin here: depth is the price of
  seeing, and the knife-edge region prices itself out of reach.
- **(c) CONFIRMED in the reachable window.** d(t) grows monotonically as t → 0⁻:
  4 → 5 → 6 → 9 → beyond-12 — the knife-edge measured in the wall's own (pair-form) shape.
  The extrapolation "d(t) → ∞ as t → 0⁻" is a READING consistent with the data and with
  Rodgers–Tao; stated at that grade.
- **Found texture (not registered):** at t = −15, −30 the POSITIVITY layer flips one step
  shallower than the reality layer — the interval clause is the more sensitive detector,
  echoing the toy wall's channel anatomy (the interval layer fails first away from the
  wall). The toy's two-layer structure is visible at ζ in the meter's own readings.

## §3 — THE SELF-SIMILARITY NOTE (Tier N)

**(Tier N; READING wherever it exceeds the cites.)** The wall's one object appears at three
altitudes, and it is the same shape at each:

1. **Q on the zeros** (the arc's object): the pair-index positive form on the zero set —
   `h2`'s content, the named absence over ℚ.
2. **The Weil pairing** (the proved world upstairs): the intersection form on C×C — the
   pair-index positivity that closes the wall over 𝔽_q.
3. **The Hankel form on power sums** (this sitting's bridge, one level DOWN): [s_{i+j}] —
   pair-indexed from birth, PSD exactly when the reality clause holds; the toy wall's
   certificate carries it EXPLICITLY (face 3: the reality layer), and ξ's own moment data
   carries it at ζ (this sitting's §2).

The three are not analogies stacked loosely: each is a positive quadratic form whose index
set is PAIRS of the layer's natural coordinate (zeros × zeros; correspondences ×
correspondences; (i,j) ↦ s_{i+j}), and in every proved world the wall closes exactly where
such a form is exhibited positive. The toy is the DISSECTED instance of direct
pair-introduction: at genus ≤ 5 the introduced form is proved positive (confinement follows);
at genus 9 the dissection shows where it breaks off-stratum and by which channel. The
self-similarity claim itself — one object, three altitudes — is a READING at Tier N; the
constituent statements are at their own grades (theorems, certificates, computations).
Keystone-Forward candidate, riding with the adopted fifth vocabulary at the keystone's next
natural touch = E-16's landing.

## §4 — E-7b's ENTRY FACE

**The question (~0.4, riding behind; QUESTION grade, internal-until-fruit):** are BN-attainment
and Λ = 0 one extremal problem in two coordinates?

| cell | content | grade |
|:--|:--|:--|
| BN ⟺ RH | d_N → 0 ⟺ RH (Nyman–Beurling; Báez-Duarte's countable strengthening) | THEOREM-AT-CITE |
| Λ ≤ 0 ⟺ RH; Λ ≥ 0 | Newman's equivalence; Rodgers–Tao | THEOREM-AT-CITE |
| BN ⟺ Λ = 0 **through RH** | trivially yes (both ⟺ RH) | THEOREM-AT-CITE (uninformative — the question is the direct route) |
| **direct BN ↔ dBN translation** (a map between the approximation coordinate N/λ and the flow coordinate t, not passing through RH) | **NOT SIGHTED** in this sitting's searches — no literature statement linking the two coordinates found | **OPEN CELL, named** |
| **quantitative bridge** (does the BN decay rate bound Λ, or Λ's value bound the BN rate?) | not sighted | **OPEN CELL, named** |
| the structural resemblance | both ceilings are unconditional floors met with zero margin (BDBLS/Burnol; Rodgers–Tao); both say "the object sits at the exact boundary of achievability"; the SHAPE is one template | READING (the fifth vocabulary's frame; not a theorem) |
| a candidate mediating object | the E-16 bridge itself: the Hankel/moment forms are a third coordinate (moment-space) touching both — the flow moves the moments (dBN side); the moments' PSD boundary is a closure/approximation statement (BN-flavored side) | READING, Tier N — the entry face's yield; unpriced continuation |

**Verdict at the entry face:** the two template-complete candidates are equivalent only
through RH at current cite; the direct translation is an OPEN QUESTION with two named empty
cells, and the moment coordinate (this sitting's bridge) is the candidate mediator.
Internal-until-fruit.

## THE KEYSTONE TOUCH (E-16's landing = the next natural touch, executed — the computation
## landed clean)

Keystone v0.6 → **v0.7**, one pass, three folds: (1) the fifth vocabulary ADOPTED in place of
its proposal — EXTREMAL-SELECTION, the two-kinds split as content; §3 pattern note and the
Forward's count updated to five vocabularies. (2) The Hankel bridge into the Forward (the
flip-depth instrument, the deep-tail finding, the two-layer texture, the Tier-N
self-similarity note) + one computational-record Correspondence row. (3) The E-16 paragraph
placed beside the E-3 state. No kernel terminal touched; pins verified unmoved at git level.

## CLOSING — pins, slate, board

**The slate re-printed:** E-1 (v2) · E-2 armed (~1.5) · E-3 (genus ≤ 5 PROVED · genus 9
dissected · the mechanism the arc's target) · E-4 armed (~1) · E-5 armed (~0.4) · E-7b entry
face DONE this sitting (two named open cells; the moment coordinate the candidate mediator;
research-reach continuation unpriced) · E-11 armed (~1.0) · E-12 priced-on-motivation ·
**E-16 RUN — (a) confirmed, (b) split first-class (instrument validated, knife-edge region
deep-tail-blind), (c) confirmed in the reachable window; the flip-depth curve d(t) = the new
measured object; continuation candidates: deeper resolution at t = −0.3 (research-reach,
priced on call) · the d(t) curve refined between −5 and −0.3** · W-FLOW-METER full hunt
(superseded in part by the Hankel meter's strict dominance where either sees) · LY-REP-A ·
Face-E Tier 2 · the ξ-sweep.

**The board restated, the flip-depth verdict at its head:** THE HANKEL METER WORKS — the
toy's pair-form carried to ζ detects the pencil's non-reality at d = 9, 6, 5, 4 for
t = −5, −15, −30, −50, strictly dominating the cumulant bracket; d(t) grows monotonically
toward t = 0⁻ (the knife-edge in the wall's own shape); and at t = −0.1, −0.3 the
Rodgers–Tao-guaranteed non-reality hides in the deep tail beyond resolved depth 12 — the
knife-edge region prices itself out of low-depth sight. At t = 0, ξ's moment forms are PSD to
every resolved depth, both layers. Five vocabularies stand; the keystone carries them at
v0.7.

| repo | pin |
|:--|:--|
| PLACE-papers | `70b5531` at open → this sitting's commit (keystone v0.7 + OPEN_TRAILS addendum) |
| SIDE-lv-conservation | main = `14720d9` — unmoved |
| SIDE-kernel | `44895f9`; v1.7 — unmoved |
| relay | this report's commit; instrument `tools/e16/hankel_bridge.py` |
| rail | untouched — at the post-rename baseline |

Mirror rebuilt at the papers pin on commit. Nothing deposits.
