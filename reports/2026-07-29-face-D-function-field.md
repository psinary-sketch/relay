# Face D positive control — the function-field analogue — 2026-07-29

Analytical pass, no kernel, no edits. The question: over 𝔽_q(t) / a curve C over 𝔽_q, where the RH analogue
is Weil's theorem, what do the programme's objects become, and is the analogue of `h2` provable there?
Extends existing corpus material — the Frobenius-analogy table (`INTEGRATED_PROOF` §"The Frobenius
Analogy"), the residue's 𝔽_q anatomy (`THE_RESIDUE_OF_RH` §6, `transfer_obstruction_is_the_two_geometric_clauses`),
and §27.3 register 5 — rather than duplicating them. (Corpus has **no** explicit Riemann-Roch / C×C /
Castelnuovo / Arakelov development: 0 hits each.)

## (1) Object-by-object translation

| programme object (number field, ℚ) | function-field analogue (curve C / 𝔽_q) | translates? |
|:--|:--|:--|
| **places of ℚ** (one archimedean + one p-adic per prime) | **closed points of C** (of ℙ¹_{𝔽_q} for 𝔽_q(t)) — each a place with residue field 𝔽_{q^{deg}} | **yes**, and *more uniformly* — all places are now geometric points; there is no distinguished archimedean place |
| **product formula** ∏_v \|x\|_v = 1 | **deg(div f) = 0** — the sum of orders over all closed points of a principal divisor is zero | **yes**, cleaner (it is the degree-zero property of principal divisors; the s-darkness of Chapter 13 is its shadow) |
| **completed zeta ξ(s)** (entire, order 1, infinitely many zeros) | **the numerator polynomial** P(T) of Z(C,T) = P(T)/((1−T)(1−qT)), P(T) = ∏_{i=1}^{2g}(1−α_i T) | **yes — but finite-dimensional**: P is a *polynomial* of degree 2g; ξ is an infinite-order entire function. **This finite-dimensionality is the whole difference.** |
| **critical line** Re(s)=½ | **\|α_i\| = √q** for every Frobenius eigenvalue (equivalently, under T = q^{−s}, the zeros of Z on Re(s)=½) | **yes** — the "critical line" is the circle \|α\|=√q |
| **seven mechanism classes** | **partial.** The additive / FE / multiplicative structures translate (the FE of Z via Poincaré duality; the Euler product via point-counts) — these are the residue's *"two arithmetic clauses [that] transfer cleanly."* The decisive structure is the **extra** one: the **surface C×C** with its correspondences (the graph of Frobenius Γ_Fr, the diagonal Δ) — absent in the number-field mechanism decomposition | **partial — the arithmetic clauses transfer; the geometric structure is new** |
| **`covers_all` / `ConservationHypothesis`** ("every ξ-zero forces the balance / lies on the line") | **"every Frobenius eigenvalue satisfies \|α_i\|=√q"** — i.e. every zero of P sits on the critical line | **yes — and it is a THEOREM** (Weil 1948) |

## (2) THE TEST — is the analogue of ConservationHypothesis a theorem, and via the same positivity?

**Yes — it is Weil's theorem** (the Riemann Hypothesis for curves over finite fields, 1948). And **yes — the
positivity it routes through is exactly `h2`'s positive-forcing clause.**

Weil's proof: on the algebraic surface **C×C**, apply **Riemann–Roch for surfaces** together with the
**Hodge index theorem / Castelnuovo–Severi inequality**. The intersection pairing on divisor classes
(correspondences) has signature (1, ρ−1); applied to the Frobenius graph Γ_Fr and the diagonal Δ, the
**positivity of that intersection form** (a correspondence has non-negative self-intersection in the
primitive part) forces the trace bound that pins **|α_i| = √q**. The forcing *is* the positivity of the
intersection form on C×C — read cohomologically (Mattuck–Tate, then Grothendieck) as the positivity of the
cup-product pairing on H¹.

That this positivity is the function-field counterpart of `h2` is stated in the corpus already, at **§27.3
register 5**: *"Over function fields the two stages coincide on one finite-dimensional object — Weil's 1948
proof runs through the positivity of the intersection pairing on correspondences (the Castelnuovo
inequality; read cohomologically by Mattuck–Tate) — and the proof closes. Over ℚ the realization space is
infinite-dimensional, no positive pairing is known, and the distance between the two stages is this same
premise in its fifth register."* And the residue §6: the 𝔽_q type is *inhabited (Weil)*, the transfer
obstruction to ℚ is *exactly the two geometric clauses — the self-adjoint operator and the positive pairing
(Hilbert–Pólya and Weil positivity)*, the constraint set pinning every property **except the positive
polarization**. So the thing Weil **has** and the number-field case **lacks** is precisely `h2`'s content —
the positive pairing.

## (3) Verdict — form (b): provable over 𝔽_q, by a route with no number-field counterpart

**The analogue is provable (Weil's theorem), but by a route whose central object has no number-field
counterpart. The obstruction is the missing second dimension.**

- **What the route needs:** a **2-dimensional** object — the surface **C×C** — carrying an intersection form
  whose positivity forces the eigenvalue bound. Over 𝔽_q, C is a curve *over a field*, and C×C is a genuine
  algebraic surface with honest intersection theory.
- **Why ℚ lacks it:** `Spec ℤ` is an *arithmetic curve* (1-dimensional), but there is **no honest
  `Spec ℤ × Spec ℤ`** — the base "field with one element 𝔽_1" over which one would take the product does not
  exist as ordinary geometry, so there is no arithmetic surface supplying the requisite intersection-form
  positivity. The second dimension — the one that makes P a *polynomial* on a *surface* and lets Riemann–Roch
  + Hodge-index bite — is absent. This is why over ℚ the realization space is **infinite-dimensional** (ξ is
  order 1 with infinitely many zeros, not a degree-2g polynomial) and **no positive pairing is known**.
- **Arakelov-theoretic substitutes (named, honestly incomplete):** Arakelov geometry *does* give an
  intersection theory on **arithmetic surfaces** — `Spec O_K` compactified with archimedean fibers — and an
  **arithmetic Hodge index theorem** (Faltings; Hriljac). But that is the geometry of *a curve over a number
  field*, **not** of "`Spec ℤ × Spec ℤ`"; it supplies the wrong surface. The programs building the *right*
  missing dimension are exactly the ones the corpus already names as stalling at `h2`: **Connes–Consani** (the
  arithmetic site / 𝔽_1 geometry, reducing RH to a Weil-positivity left open), **Deninger** (a postulated
  cohomology H¹ with a Frobenius-flow — the residue's `XRealization`), **Bost–Connes** (realizes the Euler
  product, the wrong spectrum). None has produced the positive pairing that closes RH over ℚ.

## What this control establishes

**The positive control confirms the reduction and validates `h2` as the right residue.** `h2` is precisely
the **number-field shadow of Weil positivity** — the object the extra dimension (C×C) hands you for free over
𝔽_q, and that `Spec ℤ`, lacking a second dimension, does not. The programme's residue — *"the positive space
on the zeros," "the space is the wall"* — coincides, object for object, with the century-old understood
obstruction: the **missing arithmetic surface / 𝔽_1**. This is strong evidence that `h2` is not an artifact
of the programme's parsing but the genuine wall: the function-field case is a *positive control* that
succeeds by exactly the ingredient the number-field case is missing, and the missing ingredient is `h2`.

**Consequence for the arc (Face D).** Face D's barrier is now sharpened from "Weil positivity over ℚ" to
its precise cause: **the absence of the second dimension (no `Spec ℤ × Spec ℤ`), with Arakelov surfaces the
wrong substitute.** A discharge of Face D requires *constructing* the missing surface/cohomology (Deninger's
H¹ / the arithmetic site) with a *proven* positive polarization — a research-frontier construction, not a
formalization. This matches the arc's register resolution (F.2026-07-29-d) exactly: research-frontier, and
the same wall the whole field faces.

No edits; no kernel; nothing deposited. Extends §27.3 register 5 + the residue §6 𝔽_q anatomy; duplicates
neither.
