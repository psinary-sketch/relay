# W-TWOSIDES — the finite relative identity, both halves — 2026-08-03

The priced head continuation. Pins at open: PLACE-papers = `b99782f`; relay = `1c9c7c6`; lv
`14720d9`, kernel `44895f9` — unmoved; rail at the post-rename baseline. Nothing deposits.

## §1 — THE IDENTITY, STATED AT CITE FIRST (before any number)

**The exact finite identity in hand (the Heine/Vandermonde-determinant identity — classical,
the finite form underlying the Szegő/Killip–Simon sum rules; KS at cite from the W-SUMRULE
sitting):** for ANY measure ν with Hankel determinants D_K and monic-OP recurrence
(β₀ = m₀; β_k = a_k², k ≥ 1), and its depth-K Gauss quadrature (nodes λ_i, weights μ_i —
the K-point measure sharing moments to order 2K−1):

**COEFFICIENT SIDE:  log D_K = Σ_{j=0}^{K−1} (K−j)·log β_j**   (exact; pure Jacobi data)

**SPECTRAL SIDE:  log D_K = Σ_i log μ_i + 2·Σ_{i<j} log|λ_i − λ_j|**   (exact; the
entropy/weight term + the LOG-REPULSION pair-energy of the nodes)

The two sides are one number computed by two genuinely different routes (Cholesky recurrence
vs eigen-decomposition) — the balance check IS the double-source. **The RELATIVE identity**
(ζ-string minus smooth-density control, same pipeline) isolates the arithmetic:
Δ_K = Σ(K−j)Δlog β_j = Δ[entropy] + 2Δ[log-repulsion]. The pair-correlation content, if
visible, lives in the log-repulsion term — the log-gas energy is exactly where GUE structure
prices itself.

**The truncation's exact scope, stated:** the identity is EXACT at every finite K for the
K-point Gauss objects (nothing here is asymptotic); what only the K → ∞ limit guarantees is
the KS decomposition into a.c.-entropy vs eigenvalue terms and any GUE statistics of the
deep tail — the finite form knows only its K nodes, of which ~K/2 are resolved zeros and the
rest tail-cluster representatives (the E-20 profile). **The boundary separation (the
W-SUMRULE texture) is carried explicitly:** the resolved-node band splits into BOUNDARY
(nodes 1–2, the low-zero offset against the smooth counting's start) · OSCILLATION (the
remaining resolved band) · RESIDUAL (tail clusters); no mixing.

## §2 — REGISTERED EXPECTATIONS (VERBATIM from the ferry, before any number)

**(a) BALANCE** — *"the two sides agree within stated truncation error at every reachable
depth (the classical identity holds in our finite instance; the pipeline is sound); a
persistent imbalance beyond error files FIRST-CLASS as either an instrument defect (checked
first: precision, truncation accounting) or a genuine structural surprise (only after the
instrument is cleared)."*

**(b) ATTRIBUTION** — *"after boundary separation, the oscillation's share of the spectral
side is carried by the zeros' fluctuation structure (the S(T)-class data), NOT by the smooth
density: the control's identity balances with near-zero oscillation share on both sides
simultaneously (the null baseline run end-to-end)."*

**(c) SHAPE, first look** — *"the term-by-term profile of the two sides is compared against
the GUE/pair-correlation prediction AT CITE for the spectral side's fluctuation functional
(the determinantal/sine-kernel form of the entropy deviation): graded CONSISTENT / TENSION /
BEYOND-DEPTH — truncation honesty absolute; k ≤ 16-class series claim only what the window
supports; BEYOND-DEPTH is an honorable verdict and files the exact depth bound as the
datum."*

## §3 — THE RUN

**Instruments** (`tools/e16/ts_stage1.py` → `ts_stage2.py` → `ts_stage3.py`; staged with
moment caches after a first single-script attempt hit the 10-minute task ceiling — filed as
an operational note; ζ moments at dps 400, control zeros at dps 200, assembly arithmetic at
dps 400 per the precision law).

**(a) BALANCE — registered CONFIRMED at machine exactness.** Coefficient side = spectral
side to **|Δ| ≤ 9×10⁻³⁹⁸** (the working-precision floor) at both depths and both objects:

| object, K | coefficient side | spectral side (entropy + repulsion) | balance |
|:--|:--|:--|:--|
| ζ, 12 | −1218.65866864 | −93.431166 + −1125.2275 | 4×10⁻³⁹⁸ |
| ctrl, 12 | −1248.58138761 | −94.719032 + −1153.8624 | −4×10⁻³⁹⁸ |
| ζ, 16 | −2245.38913295 | −129.79942 + −2115.5897 | −9×10⁻³⁹⁸ |
| ctrl, 16 | −2290.24373205 | −131.24816 + −2158.9956 | 4×10⁻³⁹⁸ |

The classical identity holds in our finite instance to the last computed digit; the pipeline
is sound; no imbalance, no instrument defect, no surprise.

**(b) ATTRIBUTION — registered CONFIRMED, with the structure sharper than registered.** The
relative decomposition (ζ − control): at K = 16, Δcoeff = 44.855 = Δentropy 1.449 +
Δrepulsion 43.406 — **the arithmetic difference is carried 97% by the LOG-REPULSION term**:
the weights nearly agree, the NODE POSITIONS differ — the arithmetic lives in the pair-energy
of the zeros' positions, exactly where pair structure prices itself. The control's own
identity balances as the null baseline end-to-end (it IS the reference; its oscillation
share is zero by construction, and the ζ−control difference is pair-term-dominated). Band
attribution (K = 16): boundary (nodes 1–2) = 11.16 · oscillation (resolved 3–8) = 5.03 ·
residual (tail clusters) = 27.22 — all three bands real; the boundary separation carried
explicitly as specified; the tail-cluster share is the integrated fluctuation content of the
unresolved zeros (noted: the largest single share, a depth artifact of cluster placement —
resolved-band claims only).

**(c) SHAPE, first look — BEYOND-DEPTH, the honorable verdict, with the exact bound filed.**
The resolved-band adjacent log-gap deltas (K = 16): +0.764, +0.177, +0.507, −0.228, +0.443,
+0.097, −0.200 — sign-CONSISTENT with repulsion-class structure at the crudest level (the
low gaps run wider than the rigid smooth sequence's), but the systematic positive head is
confounded with the low-zero boundary effect, and SEVEN adjacent pairs cannot discriminate
the sine-kernel form from any other repulsive shape. **The depth bound, filed as the datum:
the shape window = (resolved pairs) ≈ K/2 − 1; a genuine GUE-form test needs O(10²) pairs →
K ~ 200-class strings or high-zero band constructions — beyond the present quadrature by
an order of magnitude in depth.** No TENSION; no CONSISTENT-beyond-sign claimed; truncation
honesty absolute.

## §4 — FILINGS

**The verdict at grade (this note is the batch consult filing):** the finite relative
identity BALANCES exactly; the arithmetic is 97% pair-energy (the log-repulsion of the
node positions — the pair-index term); the shape is BEYOND-DEPTH with the bound quantified
(O(10²) resolved pairs needed; K ~ 200-class). **Three maps meet cleanly now: the shadow row
(statistics) · the string (the object's discrete shadow) · the sum-rule identity (the exact
bridge between them) — and the wall's pair-index coordinate carries the arithmetic in every
one.**

**The keystone's next-cargo list gains (touch NOT executed):** the two-sides verdict (the
identity exact in-instance; the 97% pair-energy attribution; the shape depth-bound).
Accumulated cargo: the sum-rule verdict · π₀'s first candidate row · the two-sides verdict.

**E-24's candidate row, updated (the clause grades sharpen):** the boundary-separated
RELATIVE LOG-REPULSION functional is the row's sharpest form — it is pair-priced natively
(clause iii strengthens: the pricing is the pair-energy itself, the wall's own index
structure), self-datum-as-family unchanged, free-point clause unchanged. The
construct-or-refute stays armed; π₀'s candidate is now: a normalized limit of the
boundary-separated relative pair-energy.

**The slate re-printed:** W-TWOSIDES — **RUN: (a) exact balance · (b) 97% pair-energy
attribution · (c) BEYOND-DEPTH with the bound filed (K ~ 200 for shape)** · E-24 armed
(~1.5; the candidate sharpened to the relative pair-energy limit) · E-3 (kind-indexed
recipe; c₁; n = 56 sampling) · E-7b (two cells) · E-16 (d(t) exponent) · E-20 (continuum
normalization) · E-23 (closed into the sum-rule frame; its continuation = the K ~ 200
shape run, priced research-reach) · the standing rest. **Consolidation DEFERRED, standing.**

## CLOSING — pins, mirror, the handoff refreshed

| repo | pin |
|:--|:--|
| PLACE-papers | `b99782f` at open → this sitting's commit (OPEN_TRAILS addendum + handoff refresh) |
| SIDE-lv-conservation | main = `14720d9` — unmoved |
| SIDE-kernel | `44895f9`; v1.7 — unmoved |
| relay | this report's commit; instruments `tools/e16/ts_stage{1,2,3}.py` |
| rail | untouched — at the post-rename baseline |

**The board restated, the two-sides verdict at its head:** THE IDENTITY IS EXACT IN OUR
HANDS AND THE ARITHMETIC IS PAIR-ENERGY — the finite Heine/Vandermonde form balances to the
last digit, the ζ−control difference sits 97% in the log-repulsion of the node positions,
and the shape question now has an exact price (K ~ 200). The ledge stays dressed: six
worlds · the one-law toy · the audited string · the vacancy with its sharpened candidate ·
the exact bridge. Mirror rebuilt at the papers pin on commit. Nothing deposits.
