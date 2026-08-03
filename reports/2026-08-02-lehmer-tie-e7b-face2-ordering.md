# W-LEHMER-TIE · E-7b face 2 (the determinant coordinate) · genus-9 face 2 (the ordering check) · the consolidation question — 2026-08-02

The ferry's three moves + one presentation. Pins at open: PLACE-papers = `bf1373b`; relay =
`db8914a`; lv `14720d9`, kernel `44895f9` — unmoved; rail at the post-rename baseline. Nothing
deposits.

## Registered expectations (VERBATIM from the ferry, recorded BEFORE any reading or computation)

**Move 1 (W-LEHMER-TIE):** *"YES to both — d(t)'s deep-tail = the Lehmer shadow; the
simplicity-diagonal cross-link filed (E-14's address). Null branch files the alternative
texture first-class."* (The two questions: does the depth-12 window's spectral reach fall
short of the first Lehmer pair's height; does a targeted enrichment — zero-sums weighted
toward the pair's height band — pull the flip into reachable depth at t = −0.1.)

**Move 2 (E-7b face 2):** *"the mediator exists at least as a derived map on the moment side;
full equivalence expected OPEN (the honest cell)."*

**Move 3 (genus-9 face 2):** *"YES — the ordering is structural, filed to the self-similarity
note; NO files the divergence as the worlds' first anatomical difference, equally valuable."*

## MOVE 1 — W-LEHMER-TIE

**The cite:** Csordas–Smith–Varga, *Lehmer pairs of zeros, the de Bruijn–Newman constant Λ,
and the Riemann Hypothesis* ([Constr. Approx. 10 (1994)](https://link.springer.com/article/10.1007/BF01205170))
— close pairs force lower bounds on Λ; the Polymath15/Rodgers–Tao machinery runs on the same
anatomy (close pairs collide first under the backward flow). The small-|t| non-reality's
address at cite: the close-pair (Lehmer) population.

**Part A — the pair table** (`tools/e16/lehmer_scan.py`; first 1500 zeros, γ ≤ 1980.9):
closest pair γ = 1977.174‖1977.271 (gap 0.0975, model t_c = −0.0048); **43 pairs
model-collided by t = −0.1** (two-body estimate t_c = −Δγ²/2); the LOWEST collided pair:
n = 212, γ = 415.019‖415.455 (gap 0.436, t_c = −0.0952).

**Part B — the reach question: registered YES, decisively.** The depth-12 Hankel window's
band is γ₁..γ₁₂ = [14.13, 56.45]; the first collided pair sits at γ ≈ 415 — a **54× shortfall
in β** past the reach edge, with 211 real zeros above it in the β-ordering. The E-16
deep-tail finding is quantified: the meter's window ends at γ ≈ 56 and the nearest
non-reality (model) lives at γ ≈ 415.

**Part C — the enrichment question: registered YES, with the visibility threshold measured
(MODEL grade throughout: the t = −0.1 pair is the two-body model γ_mid ± iδ, δ = 0.0977;
doubly-sourced by window family, controls mandatory).** Windowed Hankel forms centered on the
pair's band (`tools/e16/enrich2.py`):

| window scale σ (local gaps ≈ 1.5γ-units) | flip depth (model) | t = 0 control |
|:--|:--|:--|
| 0.3–0.5, lorentzian | **2** | PSD ✓ |
| 1, lorentzian / gaussian | **2 / 3** | PSD ✓ |
| 2, gaussian | 9 | PSD ✓ |
| 3+, any | none ≤ 14 | PSD ✓ |
| (0.3–0.5, gaussian — flagged) | 2 | control FLIPS — numerical floor; row excluded |

**The tie's verdict: d(t)'s deep tail = the Lehmer shadow, at model grade.** The obstruction
decomposes into LOCATION (the pair sits 54× past the untargeted meter's reach) and CONTRAST
(δ is 6.5% of the local gap — visibility requires sub-gap targeting, σ ≲ 1 local gap, where
the flip appears at depth 2–3 with clean controls; at σ ≳ 2–3 the pair is invisible at any
reachable depth). Band-targeted enrichment pulls the flip from beyond-depth-12 to depth 2–3:
the deep-tail blindness is INFORMATION LOCATION plus FAINTNESS, not intrinsic invisibility.

**The simplicity-diagonal cross-link (E-14's address), filed:** Lehmer pairs are
near-coincidences — the pair register's DIAGONAL-LIMIT, exactly where E-14 sorted simplicity
(double zero = pair coincidence; the diagonal stratum). The flip-depth meter's darkness at
small |t| lives on the simplicity diagonal: the wall's knife-edge region and the diagonal's
near-degenerate pairs are one address. The sorted ladder gains a measured annotation: the
k = 2 diagonal is not only simplicity's home — it is where the dBN pencil's near-boundary
non-reality hides from every low-depth pair-form.

## MOVE 2 — E-7b FACE 2: THE DETERMINANT COORDINATE

**The two determinant sequences, laid side by side:**

- **BN side (at cite):** the Báez-Duarte–Balazard-line distance is a Gram-determinant object —
  dist² to a span is a ratio of consecutive Gram determinants (classical linear algebra), and
  the Gram entries of the dilation system have the closed **Vasyunin cotangent-sum form**
  ([the Vasyunin-sum literature](https://www.wseas.org/multimedia/journals/mathematics/2020/b505106-037.pdf),
  [Bettin–Conrey period-function account, arXiv:1111.0931](https://arxiv.org/pdf/1111.0931)):
  G_{k,l} = ∫₀^∞ {1/kt}{1/lt} dt computed by Vasyunin's formula. RH ⟺ the Gram-ratio sequence
  → 0. THEOREM-AT-CITE.
- **Moment side (this arc's object):** the ξ-moment Hankel determinants D_d = det[s_{i+j+1}].
  **DERIVED this sitting (the registered mediator, landed):** D_d IS a Gram determinant — of
  the monomial system {1, x, …, x^{d−1}} under the bilinear form ⟨f, g⟩_ν = Σ_j β_j f(β_j)g(β_j)
  (the zero-measure ν = Σ β_j δ_{β_j}; ⟨x^i, x^j⟩_ν = s_{i+j+1} exactly). RH ⟺ this form is
  positive semidefinite on all polynomials (⟺ every D_d ≥ 0). DERIVED — elementary, but it
  makes the two sides the SAME KIND of object: each coordinate is a Gram-determinant sequence
  of a bilinear form built from ζ's data, with RH as a definiteness/limit statement about it.

**The one-form question (each cell graded):**

| cell | content | grade |
|:--|:--|:--|
| the candidate bilinear form | on the moment side: ⟨f, g⟩_ν over the zero measure; on the BN side: the L² pairing on (0,∞) restricted to the dilation span | each THEOREM-AT-CITE / DERIVED in its own coordinate |
| coordinate map 1 (moment) | polynomials → L²(ν): p ↦ (p(β_j))_j with weight β_j — the Hankel sequence as Gram | **DERIVED (this sitting)** |
| coordinate map 2 (BN) | dilations → the Mellin line: ρ_θ ↦ its Mellin transform, where ζ enters the Gram entries (Vasyunin) | THEOREM-AT-CITE (the machinery); the map stated |
| the intertwiner (one form, two coordinate systems?) | a unitary carrying the dilation span's pairing to the zero-measure pairing, matching the two determinant sequences | **OPEN — the honest cell.** The two forms both see RH as definiteness-in-the-limit, but the BN form lives on the PRIME/dilation side (Mellin, arithmetic entries — cotangent sums) and the moment form on the ZERO side (spectral entries — power sums); an intertwiner would be an explicit prime-side ↔ zero-side dictionary at the bilinear-form level — the explicit-formula shape, not exhibited as a Gram-equivalence anywhere sighted |

**VERDICT: UNRESOLVED at grade** — not ONE-PROBLEM (no intertwiner exhibited), not
TWO-PROBLEMS (the derived Gram-reading makes them the same KIND, and both ceilings are
zero-margin floors); the registered expectation CONFIRMED in both clauses: the mediator
exists as a derived map on the moment side, the full equivalence is the named OPEN cell. The
sharpened continuation (unpriced): the intertwiner candidate is the explicit formula read as
a Gram-equivalence — prime-indexed Gram entries (Vasyunin cotangent sums) against
zero-indexed Gram entries (power sums), the wall's pair-index form sitting between the two
coordinatizations. Internal-until-fruit.

## MOVE 3 — GENUS-9 FACE 2: THE ORDERING CHECK

**Instrument** (`tools/e3/ordering.py`, exact over ℚ throughout — power sums of H(u)'s roots
by Newton, fraction Gaussian-elimination determinants): three Hankel layers per member —
reality (Hamburger [m_{i+j}]) · floor (Stieltjes [m_{i+j+1}], u ≥ 0) · ceiling (Hausdorff top
[4m_{i+j} − m_{i+j+1}], u ≤ 4); first-negative-minor depth per layer.

| member | RH | reality | floor (u≥0) | ceiling (u≤4) |
|:--|:--|:--|:--|:--|
| extremal n=32 | holds | PSD | PSD | PSD |
| pencil c = 0, −10, −21 | fails | PSD | PSD | **3** |
| pencil c = −30 | fails | PSD | PSD | **6** |
| pencil c = −35 | fails | 4 | **3** | 4 |
| pencil c = −41 | fails | 3 | **2** | 3 |
| pencil c = −41.9 | fails | 2 | **2** | 3 |
| pencil c = −43 (beyond) | fails | 3 | 4 | **2** |
| pencil c = −50 (beyond) | fails | 8 | 8 | **2** |

**Registered YES — CONFIRMED, with a refinement.** In the reality-escape channel (near the
stratum — the regime the ζ-meter can exhibit, since ζ has no ceiling clause): the
positivity-side layer flips AT OR BEFORE the reality layer's depth in every member (3 < 4,
2 < 3, 2 = 2) — exactly the ζ-meter's found texture (5 < 6 at t = −15, 4 < 5 at −30, ties at
−5, −50). **The ordering is structural across the two worlds: filed to the self-similarity
note** (to ride into the keystone at its next touch). The refinement the toy adds: the
CEILING layer — the clause ζ's formulation does not possess — is the far channel's detector
(the interval-escape members are caught ONLY by it: reality and floor stay PSD) and dominates
beyond the Golay point. The toy sees with three eyes where ζ sees with two; the third eye is
exactly the extra dimension the toy wall separates.

## MOVE 4 — THE CONSOLIDATION QUESTION (presented; author-owned; no action taken)

**The inventory (one paragraph).** The selection/Hankel arc, accumulated across this day's
sittings: the fifth vocabulary EXTREMAL-SELECTION adopted with the two-kinds split and the
Rodgers–Tao pinning (F.2026-08-02-b); the genus ≤ 5 theorem (the programme's own, rational
H(u) certificates); the genus-9 dissection (two-layer confinement, channeled interior,
knife-edge, no sign test decides) with the ordering check now cross-world (this sitting); the
Hankel bridge at ζ (the flip-depth instrument d(t), validated and monotone, the deep-tail
finding at small |t|, the Lehmer tie at model grade); the W-SELECT table (two
template-complete zero-margin extremizer candidates); E-7b's determinant coordinate (both
candidates Gram-determinant sequences; the mediator derived; the intertwiner the named open
cell); the self-similarity note (one pair-index object at three altitudes, direct
pair-introduction the barrier-respecting route).

**The two dispositions, stated for the author's ruling (no action taken):**
1. **A second proofs-cluster keystone NOW** ("the selection arc" / the Hankel-bridge paper):
   crystallizes the arc while it is sharp, becomes citable at its pins, and gives the fifth
   vocabulary a home of its own beside INDEX_ARITY.
2. **The wave-edit fold LATER**: the arc's rows continue accumulating in INDEX_ARITY's
   Forward + the ledgers until the next wave-edit, keeping the arc unfragmented and avoiding
   a second document whose scope overlaps the first.

**The honest trade:** a keystone crystallizes and cites — but freezes scope at today's edge
and risks splitting one wall across two papers; the wave-edit keeps the arc unfragmented —
but leaves the fifth vocabulary and the bridge citable only through ledger rows until the
wave. **Author-owned; your ruling whenever appetite says.**

## CLOSING — pins, slate, board

**The slate re-printed:** E-1 (v2) · E-2 armed (~1.5) · E-3 (genus ≤ 5 PROVED · genus 9
dissected, ordering now cross-world · mechanism the arc's target) · E-4 armed (~1) · E-5
armed (~0.4) · E-7b (entry face + determinant coordinate DONE; the intertwiner = the named
open cell; the explicit-formula-as-Gram-equivalence the sharpened continuation, unpriced) ·
E-11 armed (~1.0) · E-12 priced-on-motivation · E-16 (run; the Lehmer tie now filed at model
grade; continuation candidates: the true-flow check of the two-body model against Polymath15
effective-H_t machinery [research-reach], the enrichment made rigorous [research-reach]) ·
W-LEHMER-TIE DONE this sitting (~0.6 as priced) · W-FLOW-METER full hunt (superseded where
the Hankel meter sees) · LY-REP-A · Face-E Tier 2 · the ξ-sweep. **The consolidation question
stands presented — author-owned.**

**The board restated, the tie's verdict at its head:** THE DEEP TAIL HAS AN ADDRESS —
d(t)'s small-|t| blindness is the Lehmer shadow (model grade): the first collided pair at
t = −0.1 sits at γ ≈ 415, 54× past the untargeted meter's reach, at 6.5% contrast against
its local gap; band-targeted enrichment at σ ≲ 1 local gap pulls the flip to depth 2–3
(controls clean); and the shadow's address IS the simplicity diagonal (E-14) — the knife-edge
region and the pair register's diagonal-limit are one place. The ordering of the layers is
structural across the worlds (positivity sees first where reality fails; the toy's ceiling
is the third eye ζ lacks). BN and dBN are both Gram-determinant sequences (the mediator
derived); the intertwiner is the named open cell.

| repo | pin |
|:--|:--|
| PLACE-papers | `bf1373b` at open → this sitting's commit (OPEN_TRAILS addendum) |
| SIDE-lv-conservation | main = `14720d9` — unmoved |
| SIDE-kernel | `44895f9`; v1.7 — unmoved |
| relay | this report's commit; instruments `tools/e16/lehmer_scan.py`, `tools/e16/enrich2.py`, `tools/e3/ordering.py` |
| rail | untouched — at the post-rename baseline |

Keystone untouched this sitting (the ordering result and the Lehmer annotation ride the
self-similarity note to the next touch). Mirror rebuilt at the papers pin on commit. Nothing
deposits.
