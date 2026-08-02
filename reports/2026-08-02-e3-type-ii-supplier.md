# E-3 sitting 1 — the Type-II supplier theorem: the extremal 24k ladder + the ultraspherical transport — 2026-08-02

E-3 (slate ~1.5, research-reach): converting the fourth supplier row from instance to
setting-theorem — a proved family instance of MacWilliams + extremality ⇒ Duursma-RH, proved by
the programme's own hands. Entry face this sitting: the length-24k extremal ladder beside
Duursma's family results. Mast: the four-vocabulary wall (this move works the SUPPLIER
vocabulary) and the sorted ladder. Mirror pin at open: PLACE-papers = `1d703b0`; lv main =
`14720d9`; SIDE-kernel = `44895f9` (v1.7 = `2957e7d`). Nothing deposits.

## Registered expectation (recorded verbatim BEFORE computation)

**(a)** Duursma-RH HOLDS exactly at every rung of the extremal Type II ladder computed this
sitting (n = 24k, d = 4k+4, k = 1..5) — consistent with the literature's verified range; a
failure at any rung is a first-class finding against the row.

**(b)** The Golay pattern recurs down the ladder: the normalized zeta P/P(0) is NON-integral at
every rung k ≥ 1 (the curve reading stays dead on the extremal ladder), and the [8,4,4]
curve-partner factor (1 + 2T + 2T²) divides NO ladder zeta — the curve-factor structure of the
d = 4 passers (lengths 8, 16) does not reappear under extremality.

**(c)** The theorem attempt: the ultraspherical transport (Duursma's Type IV method) identifies
extremality as the positivity supplier in the orthogonal-polynomial basis at every computed
rung, but the Type II family theorem does NOT close this sitting — the honest expected outcome
is a NARROWED, NAMED obstruction (which step of the Type IV proof fails to transport), not a
proof. Surprise = a closable family instance by our own hands.

---

*(Computation and findings below were produced after the registration above; the instrument and
its double-sourcing are described at the point of use.)*

## Mid-sitting registration (recorded BEFORE the family probe; the ladder was computed first,
## its results below)

The validation rungs' factor structure reads cyclotomic in τ = √2·T (length-8 factor
= τ² + √2τ + 1, the primitive-8th-root quadratic; length-16 cofactor = Φ₂₄(τ)). **Registered
before the d = 4 family probe:** Duursma-RH holds at every W₈^m, m = 1..6, and the τ-cyclotomic
factor pattern extends — each P_{8m} a product of cyclotomic polynomials in τ over ℚ(√2). A
non-cyclotomic factor at some m is the interesting failure; an RH failure at some m is a
first-class finding FOR the row (it would sharpen the supplier from self-duality toward
extremality).

## Mid-sitting registration 2 (recorded BEFORE the n = 24 pencil sweep; the family probe's
## verdict — RH fails exactly at W₈^m, m ≥ 3 — was in hand)

The Gleason pencil at n = 24: W_c = W₈³ + c·g₂₄, c ∈ [−42, 0]; c = −42 is the Golay (extremal),
c = 0 the direct-sum d = 4 point (RH-violating, this sitting's witness). **Registered before the
sweep:** RH holds on a terminal interval [−42, c*] containing the extremal point and fails
beyond a single flip value c* — the supplier has a margin, not a knife-edge at the extremal
point alone.

## The instrument (relay `tools/e3/`)

`duursma_ladder.py` — exact rational arithmetic throughout. Per rung: (1) extremal Type II
enumerator solved in the Gleason basis (W₈, g₂₄), verified against the literature values
A₈ = 759 (n=24), A₁₂ = 17296 (n=48), A₁₆ = 249849 (n=72); (2) the zeta polynomial P(T) solved
from the defining coefficient identity by TWO independent square subsystems (first-rows /
last-rows), compared equal, then the FULL overdetermined system verified monomial-by-monomial
(n+1 equations per rung); (3) structural checks NOT imposed by the solve: P(1) = 1 and the
self-dual FE p_{2g−i} = q^{g−i} p_i — both hold at every rung; (4) **Duursma-RH certified
EXACTLY**: with τ = √2·T and s = τ + 1/τ, the polynomial h(s) ∈ ℚ(√2)[s] of degree g satisfies
Q(τ) = τᵍ h(s), and RH ⟺ all roots of h real in [−2, 2] — decided by Sturm chains over ℚ(√2)
(exact sign logic on a + b√2; recursive on gcd for multiplicity); (5) integrality and
curve-factor tests; (6) mpmath 60-dps root display (display only; the certificate is the Sturm).
Convention pinned empirically: the identity with (xT + y(1−T))ⁿ reproduces P = (1+2T+2T²)/5 on
[8,4,4] and the length-16 factorization (1+2T+2T²)(1−4T⁴+16T⁸) of the prior sitting — the two
prior independent computations serve as cross-session validation of this instrument.

`d4_family.py` — the W₈^m probe with exact cyclotomic factor detection in τ. `pencil24.py` — the
n = 24 Gleason pencil sweep with exact flip bisection.

## RESULT 1 — the extremal 24k ladder: registered (a) and (b) CONFIRMED

| n | d | g | deg P | RH (exact Sturm) | P/P(0) ∈ ℤ[T] | (1+2T+2T²) divides | p_i > 0 all i |
|--:|--:|--:|--:|:--|:--|:--|:--|
| 24 | 8 | 5 | 10 | **HOLDS** | no | no | yes |
| 48 | 12 | 13 | 26 | **HOLDS** | no | no | yes |
| 72 | 16 | 21 | 42 | **HOLDS** | no | no | yes |
| 96 | 20 | 29 | 58 | **HOLDS** | no | no | yes |
| 120 | 24 | 37 | 74 | **HOLDS** | no | no | yes |

Every rung: P(1) = 1, FE exact, all n+1 defining equations verified, numeric roots on
|T| = 1/√2 to one ulp at 60 dps. **(a) CONFIRMED** — RH exact at every rung. **(b) CONFIRMED**
— the Golay pattern persists down the ladder: non-integral at every rung (the curve reading
stays dead under extremality) and the curve-partner factor divides nothing. Found structure not
registered: **every zeta coefficient is strictly positive** at every extremal rung, and
p₀ = A_d / C(n,d) (checked exactly at n = 24: 759/C(24,8) = 1/969).

## RESULT 2 — the family probe: the registration FAILED in the sharpest direction (first-class)

Registered: RH at every W₈^m, m ≤ 6, with extending cyclotomic structure. **Verdict: RH holds
at m = 1, 2 and FAILS EXACTLY at every m = 3, 4, 5, 6** (Sturm-certified; witness quote at m=3:
a root with |T| = 0.9640 vs 1/√2 = 0.7071). The cyclotomic factorization is complete at m ≤ 2
(m=1: τ²+√2τ+1, the primitive-8th-root quadratic; m=2: that times Φ₂₄(τ)) and absent at m ≥ 3.
FE and P(1) = 1 hold at every m — **the MacWilliams involution supplies the functional equation
on the whole family; it never decides RH.**

The retrospective coherence: W₈^m is EXTREMAL exactly when m ≤ 2 (d = 4 = 4⌊n/24⌋+4 requires
n < 24). So in this family **RH holds precisely at the extremal members and fails at every
non-extremal member computed** — extremality tracks RH exactly, both directions, across
everything measured this sitting. The failed registration is the row's sharpening: self-duality
+ Type II alone are NOT the supplier; the supplier is the extremal stratum.

**The n = 24 matched pair** (the witness-pair shape): Golay (extremal, d=8) — RH holds exactly;
W₈³ (d=4, same length, same type, FE verified) — RH fails exactly. One length, one involution,
one FE; extremality flips the verdict. Unlike the E-8 pair, this flip has OBSERVABLE change —
the supplier is bright in this instrument.

## RESULT 3 — the pencil: registration 2 FAILED — knife-edge, not margin

The n = 24 Gleason pencil W_c = W₈³ + c·g₂₄ (c = −42 the Golay, c = 0 the witness): registered
a terminal RH-interval [−42, c*]. **Verdict: RH fails at every sampled non-extremal point,
including c = −10749/256 — within 3/256 of the extremal point.** No margin at the sampled
resolution: the deg-P collapse (18 → 10) at c = −42 is where RH lives. At enumerator-level
grade: the supplier is the stratum itself, knife-edge. (Formal pencil, not a code family;
stated at that grade.)

## RESULT 4 — the transport obstruction, named concretely + the found reduction

Duursma's Type IV theorem (extremal Type IV ⇒ RH, via ultraspherical polynomials — THEOREM at
cite, Discrete Math 268 (2003) 103–127) rides ultraspherical zero-reality. **The concrete
obstruction for Type II, computed exactly at the k = 1 rung:** the Golay h(s) is PARITY-MIXED
(nonzero coefficients at s⁰, s¹, s³, s⁴, s⁵), while every ultraspherical C₅^λ has pure parity —
no proportionality to any member of the classical family is possible. The Type IV mechanism
does not transport as-is. Registered (c) CONFIRMED in shape: named obstruction, not a proof.

**The found reduction (the sitting's structural find):** the Golay h has the Galois-parity
lock — even powers of s carry pure √2-multiples, odd powers pure rationals, so conjugation
√2 ↦ −√2 acts as s ↦ −s. Hence H(s) := h(s)·h^σ(s) ∈ ℚ[s²] is the RATIONAL certificate object
(degree 2g, even), and Type II RH ⟺ H has all roots real in [−2,2]. H(u), u = s², is the Type
II analogue of the ultraspherical target — the family theorem's working surface for the next
face.

## The literature beside (at cite, sighted this sitting)

- Duursma, *Extremal weight enumerators and ultraspherical polynomials*, Discrete Math 268
  (2003) 103–127 — extremal Type IV ⇒ RH, THEOREM. Types I–III: Duursma's conjecture, OPEN.
  (Sighted via [Catalano, RHUMJ 9.2](https://scholar.rose-hulman.edu/rhumj/vol9/iss2/1/) and
  [arXiv:1606.03159](https://arxiv.org/pdf/1606.03159).)
- Chinen — extremal FORMAL weight enumerators outside the classical types where RH FAILS
  ([arXiv:1709.03389](https://arxiv.org/pdf/1709.03389),
  [arXiv:1709.03380](https://arxiv.org/pdf/1709.03380)): extremality ⇒ RH is type-sensitive
  even where it is a theorem-shape — the setting-theorem must name its type.
- Small-genus RH results for self-dual enumerators exist (genus three:
  [arXiv:1811.08246](https://arxiv.org/pdf/1811.08246),
  [SUT J. Math 57.1](https://projecteuclid.org/journals/sut-journal-of-mathematics/volume-57/issue-1/On-the-Riemann-hypothesis-for-self-dual-weight-enumerators-of/10.55937/sut/1622825731.pdf))
  — the genus-by-genus route is live in the literature; our k = 1 rung is g = 5.
- The W₈^m non-extremal failures: not sighted as a documented instance in this sitting's
  search; the exact certificate is ours regardless of priority status.

## Scorecard and status

Registered (a) CONFIRMED · (b) CONFIRMED · family-probe registration FAILED (the finding) ·
pencil registration FAILED (the finding) · (c) CONFIRMED in shape (obstruction named, no
proof). **E-3 the setting-theorem: OPEN — sitting 1 of ~1.5 delivers the entry face complete**:
the ladder certified, the necessity direction PROVED BY EXACT WITNESS (extremality is not
decorative — the involution alone never decides), the knife-edge measured, the transport
obstruction named concretely, and the rational reduction target H(u) found.

**What this opens:** (i) the fourth supplier row sharpens to the TWO-LAYER form — FE free on
the whole fixed locus, the on-circle statement supplied only at the extremal stratum — the same
decomposition as the fifth (graph) row: a cross-row pattern, keystone-Forward candidate at the
next touch (author-ruled; rides with the standing E-15 determinacy flag). (ii) The next E-3
face: the family attempt on H(u) — Duursma's positivity argument re-run against the rational
certificate object, entry at small genus beside the literature's genus-three route. (iii) The
armed W-CHAIN-CURVE length-32 rung (~0.5) sits adjacent, untouched, on the author's board.

## Pin table

| repo | pin |
|:--|:--|
| PLACE-papers | `1d703b0` at open; OPEN_TRAILS addendum this sitting |
| SIDE-lv-conservation | main = `14720d9` — unmoved |
| SIDE-kernel | `44895f9`; v1.7 = `2957e7d` — unmoved |
| relay | this report's commit; instrument at `tools/e3/` |
| rail | untouched this sitting |

Keystone untouched (touches are author-ruled; two flags now standing for its next touch).
Nothing deposits.
