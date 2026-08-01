# BUILD-2 checkpoint — LY-REP-A necessary conditions: registered, then computed — 2026-08-01

Second pass of the h2 build slate. Findings-before-interpretation: **the checkable inequality set
below was registered from sources BEFORE any computation ran** (this section authored first; the
results section appended after the runs; the commit carries both, the discipline is the ordering
of authorship within the sitting, stated honestly).

## The registered inequality set (from sources, before computation)

If Riemann's Φ admitted a Newman-class (ferromagnetic/Lee–Yang) representation — LY-REP-A's
object — then Ξ would lie in the Laguerre–Pólya class as the characteristic function of the
represented measure, and the following are NECESSARY, each classical at its cite:

1. **Higher even-cumulant negativity** (from the LP canonical product: for an even LP
   characteristic function e^{−γt²}∏(1−t²/α_j²), the cumulants satisfy κ₂ ≥ 0 and
   **κ₂ₖ ≤ 0 for every k ≥ 2**, with κ₂ₖ = −((2k)!/k)·Σ_j α_j^{−2k}). Checkable on Φ's
   normalized density to honest depth: **κ₄ ≤ 0, κ₆ ≤ 0, κ₈ ≤ 0**. (Newman 1976; the LP
   canonical form; de Bruijn's setting.)
2. **The Turán inequalities** for Ξ's Taylor coefficients b_k (b_k² ≥ b_{k−1}·b_{k+1}) — proved
   unconditionally for Ξ (Csordas–Norfolk–Varga 1986); computed here as a **route-validation
   anchor** (a proved fact the numerics must reproduce, calibrating the instrument).
3. **Honest boundary, registered now:** from Φ alone, only this spectral/cumulant layer is
   accessible. The coupling-level necessary conditions (Lebowitz, GHS on the *representing*
   measure) require the representation itself and are NOT computable from Φ — if the layer-1/2
   checks pass, the outcome is "consistent at the accessible layer," never evidence the
   representation exists. And since RH itself would imply layer 1 (with α_j = the ordinates), a
   PASS cannot distinguish LY-REP-existence from RH-truth: **a PASS is non-discriminating by
   design; only a FAIL would be decisive** (it would refute both). Registered before computing.

**Registered expectation:** all layer-1 and layer-2 checks PASS at the computed depth (the
literature's numerical tradition has never surfaced a violation); the build's value is the
instrument and the honest filing, not a surprise.

## The computation (doubly-sourced)

Two independent routes to the raw even moments m₂ₖ = ∫ u^{2k} Φ(u) du:
- **Route A**: direct quadrature of the theta-series form of Φ (series truncated at n = 40,
  tail provably negligible at the working interval; mpmath dps 40).
- **Route B**: Taylor derivatives of Ξ(t) = ξ(1/2 + it) at t = 0 (mpmath high-precision
  differentiation; m₂ₖ = (−1)^k · Ξ^(2k)(0), no Φ-integral involved).

**Route agreement:** the two routes agree to ≤ 1e−41 relative on every moment m₀…m₈ — the
instrument is calibrated (and the Turán anchor, a proved fact, is reproduced at k = 1, 2, 3).

**THE REGISTERED SET CONTAINED A DERIVATION ERROR — CAUGHT BY THE COMPUTATION, corrected at
grade before filing.** The registration wrote κ₂ₖ ≤ 0 for all k ≥ 2. The computation returned
κ₄ = −4.46e−4 < 0, **κ₆ = +3.46e−5 > 0**, κ₈ = −6.68e−6 < 0 — an apparent violation. Re-derivation
at source (before any interpretation): from the LP canonical product Ξ(t) = Ξ(0)·∏(1 − t²/γ_j²),
log f(t) = −Σ_k (t^{2k}/k)·S₂ₖ matched against Σ_k κ₂ₖ(−1)^k t^{2k}/(2k)! gives
**κ₂ₖ = (−1)^{k+1}·((2k)!/k)·S₂ₖ** — the necessary sign pattern is ALTERNATING
(κ₄ < 0, κ₆ > 0, κ₈ < 0, …), not all-negative; the registration had dropped the (−1)^k. The
measured signs match the CORRECTED necessary pattern exactly, in all three testable places.

**The quantitative tie (a check the correction unlocked):** the corrected identity gives
κ₂ = 2·S₂ with S₂ = Σ_{γ>0} γ^{−2}. Measured κ₂/2 = 0.02310499…; the classical zero-sum
(first 200 zeros + density tail) = 0.02310976… — agreement to the tail estimate's accuracy.
The Φ-cumulants are measuring the zero power-sums, as the identity requires.

## Grade and filing

**Verdict at grade:** the corrected layer-1 necessary conditions **PASS** at depth k ≤ 4
(alternating signs exact; Turán anchor reproduced; the κ₂ tie quantitative). Per the registered
boundary: **a PASS is non-discriminating by design** — it is compatible with both LY-REP-existence
and bare RH-truth, and the coupling-level conditions remain inaccessible from Φ alone. LY-REP-A
stands exactly as filed; no narrowing.

**The pass's first-class findings are two:** (1) the registered-set correction itself — the
discipline (register-then-compute, double-source) caught a wrong registration within the sitting,
the second such catch of the sitting-pair (kin: the W-HALF route-B correction); filed for the
loom's registered-expectation family. (2) The instrument: a calibrated, doubly-sourced
Φ-cumulant/zero-power-sum meter (the κ₂ₖ ↔ S₂ₖ dictionary), reusable for any future depth
extension — the honest deliverable of BUILD-2.

## Pins

- Computation-only pass: no kernel commits, no paper edits; scripts in the session scratchpad,
  key numbers verbatim above. Rail frozen at `11db565` (empty-diff at the slate close). Nothing
  deposits. Next: BUILD-3 (the 𝔽_q phase screen).
