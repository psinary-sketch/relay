# The recursion note · E-21 the additive hunt · E-20 face 2 the asymptotic audit — 2026-08-03

The ferry's three moves. Pins at open: PLACE-papers = `68eb945`; relay = `4f6081d`; lv
`14720d9`, kernel `44895f9` — unmoved; rail at the post-rename baseline. Precision ≥
certification depth per the filed instrument note. Nothing deposits.

## Registered expectations (VERBATIM from the ferry, recorded BEFORE computation)

**E-21:** *"the constant term's SIGN structure is extremality-decided (negative attack
extinguished exactly on the stratum) and its magnitude follows a recognizable combinatorial
n-law; the null branch names the first unrecognized constant as the honest edge."*

**E-20 face 2:** *"MATCH within truncation error (the identification's strongest audit
passed); a TENSION cell files first-class either way — mismatch would reconfigure the
intertwiner and is equally reportable."*

## MOVE 1 — THE RECURSION NOTE (filed; rides to the keystone's next touch)

**The lead law's proof used self-duality alone.** lead(H) = p₀² needs exactly two inputs —
Duursma's P(0) formula and the self-dual functional equation — and neither mentions
extremality: **the law holds for every self-dual code, failing members included** (the
computed W₈^m failures all carry it; the pencils carry it at every δ). So the double zero of
the top coefficient along any stratum pencil is **the symmetry layer's universal gift**: the
MacWilliams involution alone plants the defect's square in the certificate's leading datum.
Selection therefore lives ENTIRELY in the additive half — the flip polynomials' constants —
and the free-vs-deciding anatomy has recursed one level deeper, now INSIDE the certificate:

| level | free (symmetry gives it to every member) | deciding (the stratum earns it) |
|:--|:--|:--|
| the code world (v0.6) | the functional equation (MacWilliams) | the on-circle confinement |
| the graph world (v0.4) | spectral reality (self-adjointness) | the Ramanujan margin |
| **the certificate (this note)** | **the lead square p₀² and its double zero (FE + P(0))** | **the additive constants' sign structure (E-21's hunt)** |

Grade: the lead law at proof grade (two lines, this programme); the recursion reading at
note grade; the cross-world parallels at their standing cites. Rides to the keystone's next
natural touch.

## MOVE 2 — E-21: THE ADDITIVE HUNT

**Mid-hunt registration (recorded BEFORE the decisive n = 40 interpolation; the n = 24, 32
data was in hand):** the k = 3 constant-term coefficients — Ñ₃(0) = −(5/2)·lead(H_ext)² at
n = 24 and −3·lead(H_ext)² at n = 32 — follow the LINEAR-IN-GENUS law coeff = −(g_pencil +
11)/8 (equivalently −(n + 16)/16), predicting **Ñ₃(0) = −(7/2)·lead(H_ext40)² at n = 40.**
The prediction's failure files the coefficient as the first unrecognized constant (the
registered null branch).

**Instruments:** `tools/e3/additive_hunt.py` + the decisive-test run (exact interpolation
throughout; every N reconstructed from ~45 rational samples and verified on all of them).

**The data (entry = the shallowest flipping floor minor near the stratum):**

| n | genus (pencil/ext) | entry k | Ñ_k(0) / lead(H_ext)^{k−1} | flip root (δ) |
|--:|:--|:--|:--|:--|
| 24 | 9 / 5 | 2 | **−1** | ≈ 3.172 |
| 24 | (k=3 series) | 3 | **−5/2** | ≈ 7.164 (k=3 window) |
| 32 | 13 / 9 | 3 | **−3** | ≈ 1.272 |
| 40 | 17 / 13 | 3 | **−7/2** — PREDICTED before computation (mid-hunt registration), CONFIRMED EXACTLY | ≈ 0.1755 |

(The n = 40 δ = 1 scan's "no entry" was a WINDOW artifact, disambiguated by the small-δ
probe: the flip region exists but has narrowed below δ = 1/4 — the null branch fired for the
window, not the law.)

**THE ADDITIVE LAW (the registered deliverable — it LANDS, with a predictive confirmation):**
at the k = 3 entry minor,

  **Ñ₃(0) = −((n + 16)/16) · lead(H_ext)² = −((n + 16)/16) · p₀(ext)⁴**

— exact at three lengths, the third PREDICTED from the first two and confirmed; equivalently
coeff = −(g_pencil + 11)/8, linear in the genus. With the lead law (lead = p₀², proved),
every constant in the law is closed-form in the code's own data. The k = 2 instance at
n = 24 (coeff −1) is the series' short first entry (k = 2 does not flip at n ≥ 32).
**Registered CONFIRMED in both clauses:** the SIGN structure is extremality-decided (the
attack is negative at every measured entry, extinguished on the stratum by the proved double
zero), and the magnitude follows a recognized combinatorial n-law — predictively verified.

**The found sharpening (not registered):** the flip windows COLLAPSE super-geometrically
across n (δ-roots 7.16 → 1.27 → 0.176 at k = 3) — the selection knife-edge sharpens with
genus; the failing interior hugs the stratum ever more tightly. The honest edge, named: the
HIGHER coefficients of the flip polynomials (beyond the constant term) remain unrecognized —
the full additive recipe is the remaining family question, now with its constant term
closed.

## MOVE 3 — E-20 FACE 2: THE ASYMPTOTIC AUDIT

**Instrument** (`tools/e16/asymptotic_audit.py`; source A at dps 250 to depth 12; source B's
depth-6 attempt hit the precision floor — the filed instrument note's second demonstration:
extraction precision must exceed certification depth; source B's budget supports depth 5,
where face 1's cross-source agreement stands).

**THE NODE TEST (the audit's core): the depth-12 string's Gauss nodes against the actual
zeros' β_j = 1/(2γ_j)²:**

| j | rel. difference | reading |
|--:|:--|:--|
| 1 | 1.0×10⁻²⁴ | the lowest zero regenerated to full working depth |
| 2 | 7.4×10⁻¹⁵ | |
| 3 | 1.2×10⁻¹⁰ | |
| 4 | 4.2×10⁻⁶ | |
| 5 | 1.4×10⁻⁴ | |
| 6 | 7.4×10⁻³ | the individually-resolved range ends |
| 7–12 | 6%…99% | tail-cluster representatives (Gauss lumping of the accumulation — the CORRECT behavior for a determinate measure with an accumulation point, not error) |

**VERDICT: the registration CONFIRMED — MATCH within truncation error, and the truncation
error now has a measured PROFILE:** the depth-d string resolves ~d/2 individual zeros at
steeply graded precision and summarizes the rest as effective tail masses. The roundtrip
zeros → moments → string → spectrum demonstrably converges — the determinacy (free, by
bounded support) seen in action. **No TENSION cell.** The trend cells: α_k and the
β-recurrence decay toward 0 overall with small local oscillations — the oscillation is
spectral-gap fine structure, not a violation of any at-cite constraint (no cite predicts
monotonicity; the naive monotone check in the instrument was a strawman and is graded as
such). **The Lagarias H(t)-growth ↔ zero-density cell remains OPEN at cite** — it lives in
the string's continuum limit, beyond a depth-12 truncation whose tail nodes summarize rather
than resolve; that continuum comparison is the face's named next rung (priced on call).

## CLOSING — pins, slate, board

**The slate re-printed:** E-21 — **RUN: THE ADDITIVE LAW LANDS with a predictive
confirmation** (Ñ₃(0) = −((n+16)/16)·p₀⁴, exact at three lengths, the third predicted before
computation; the sign structure extremality-decided; the flip windows collapsing
super-geometrically — the knife-edge sharpening with genus); the higher flip-coefficients =
the scoped remainder · E-20 — **face 2 RUN: the node-test audit passed, no tension; the
continuum-limit cell the next rung** · E-3 — the residue law: multiplicative half proved,
additive constant now lawful; the full flip-polynomial recipe the remaining family question ·
the recursion note FILED (rides the keystone's next touch) · E-7b (two cells; the string
audit-clean twice over) · E-1 · E-2 · E-4 · E-5 · E-11 · E-12 · E-16 (d(t) exponent;
Polymath15-rigorous rung) · LY-REP-A · Face-E Tier 2 · the ξ-sweep. **Consolidation
DEFERRED, standing.**

**The board restated, the two verdicts at its head:** THE ADDITIVE LAW — the selection
recipe's constant term is closed-form in the code's own data (−((n+16)/16)·p₀⁴), verified by
a registered prediction; selection lives in the additive half and its first coefficient is
now lawful. THE ASYMPTOTIC AUDIT — the string regenerates the zeros it encodes with a
measured convergence profile (10⁻²⁴ at the edge, individually-resolved through ~d/2), no
tension anywhere; the identification stands twice-audited with the continuum limit as its
next test.

| repo | pin |
|:--|:--|
| PLACE-papers | `68eb945` at open → this sitting's commit (OPEN_TRAILS addendum) |
| SIDE-lv-conservation | main = `14720d9` — unmoved |
| SIDE-kernel | `44895f9`; v1.7 — unmoved |
| relay | this report's commit; instruments `tools/e3/additive_hunt.py`, `tools/e16/asymptotic_audit.py` |
| rail | untouched — at the post-rename baseline |

Keystone untouched (the next touch carries: the recursion note · the additive law · the
audit profile). Mirror rebuilt at the papers pin on commit. Nothing deposits.
