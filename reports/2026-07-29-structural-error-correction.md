# Structural Error Correction — S1–S7 pass — 2026-07-29

The paper pass on the STRUCTURAL ERROR CORRECTION keystone, per author ratification, points S1–S7.
Refine-not-rewrite; the four-domain survey and its claim-status scoping are untouched. Every claim-verb
scoped to what the kernel proves.

## Keystone located (before editing)

- **Path:** `phase2/quantum/ERROR_CORRECTION.md`
- **Header version before:** v1.0.1 (2026-07-19) → **now v1.1 (2026-07-29)**
- **REGISTRY row:** **p2-16** (`Structural Error Correction`, P-ZONE filed 64/065,864) → version v1.1, status **REVIEW**
- (p2-34 `Formation Distance and the Silence-as-Protection Chain` is a distinct paper — not this pass.)

## What the pass added (S1–S5)

- **S1 — scope sentence** (abstract, governing): the compiled result is the **de-alignment condition** —
  the seven Fano lines are the minimum-weight logical operators of the [[7,1,3]] code, so three faults on
  a line complete an operator no syndrome sees, and *if each line's three positions occupy three distinct
  failure domains, no single-domain failure can complete a line*. Stated as the condition under which
  single-domain correlation is defeated — **not** that the structure protects per se. §5's "protection is
  derived" reading pointed to the compiled anchor (the condition), the four-domain thesis kept at
  manuscript grade.
- **S2 — threat model** (§8): (i) multi-domain correlated faults; (ii) model-space escape / the leakage
  analogue (needs a separate legality check with reset path); (iii) faults in the verifier itself. Plus:
  the condition *converts* a distance-3 scheme's exposure to domain-correlated noise; without it, two
  co-located positions + one further fault suffice.
- **S3 — seven design conditions** (§7.1): de-alignment · automorphism rotation (collineations, group
  order 168) · model-space legality checking · repeated-agreement verification · non-co-aligned outer
  layers · per-line joint-failure instrumentation (seven counters) · isolation+audit of the
  non-transversal step — each condition-plus-consequence, none a possessed property.
- **S4 — Correspondence** (§9): below, pinned to v0.2.1.
- **S5 — jargon** defined at first use (minimum-weight logical operator, failure domain, transversal,
  leakage analogue); vocabulary sweep clean (the provenance line's own meta-reference tripped the screen
  and was fixed — `7f1d3b4`).

## S4 — the verified Correspondence table

All DeAlignment rows pinned to `SIDE-structural-error-correction` v0.2.1, commit
`6a4f4829cf219839f33c6af9d665687b93af772e` (independently verified: remote main and the peeled v0.2.1 tag
both at `6a4f482`, six theorems present). `[propext]` written as such, not rounded.

| Claim | Kernel | Theorem | Axiom profile | Status |
|:---|:---|:---|:---|:---|
| No single-domain failure completes a de-aligned line | SESC v0.2.1 `6a4f482` | `DeAlignment.no_domain_covers_line` | axiom-free | DERIVES |
| The protection theorem, over any line family | v0.2.1 `6a4f482` | `DeAlignment.single_domain_fault_not_logical` | axiom-free | DERIVES |
| One-position-per-domain implies de-alignment | v0.2.1 `6a4f482` | `DeAlignment.dealigned_of_lines_injective` | axiom-free | DERIVES |
| The condition is certifiable by evaluation | v0.2.1 `6a4f482` | `DeAlignment.fano_dealignment_decidable_example` | axiom-free | DERIVES |
| The check refuses a collapsed line (the certificate has teeth) | v0.2.1 `6a4f482` | `DeAlignment.fano_collapsed_line_rejected` | axiom-free | DERIVES |
| The line family used is the Fano plane (every pair of distinct positions on exactly one line, by evaluation) | v0.2.1 `6a4f482` | `DeAlignment.fano_two_design` | `[propext]` | DERIVES |
| The [[7,1,3]] Steane parameters | SIDE-cosmo `c5cba30` | `SteaneExemplar.steane_parameters` | `{propext, Quot.sound}` | DERIVES |
| The Knill–Laflamme conditions | SIDE-cosmo `c5cba30` | `SteaneExemplar.knill_laflamme_t1` | `{propext, Classical.choice, Quot.sound}` | DERIVES |
| Formation Distance theorem, d_eff ≥ 2S−1 (§3) | none (manuscript) | proof sketch only | n/a | manuscript-resident |
| The four-domain silence-as-protection pattern (§4–5) | none (manuscript) | survey | n/a | manuscript-resident |

## S6 — patent-adjacent note (for the author; NOT in the paper)

**Incidence-de-aligned assignment combined with periodic automorphism rotation is the specific mechanism**
— de-align each Fano line's three positions across three distinct failure domains (defeating single-domain
correlation), and rotate the assignment periodically through the plane's collineation group (order 168) so
no fixed physical bias accumulates against one logical operator. **Its first half — the de-alignment
condition — now carries a compiled certificate at v0.2.1** (`6a4f482`, the six DeAlignment terminals). The
rotation half is a design condition, not yet compiled. **Flag for attorney review ahead of the P-ZONE
calendar gate (2027-05-14):** the mechanism is P-ZONE-adjacent (P-ZONE 64/065,864), and the compiled first
half is now a citable reduction-to-practice for it.

## S7 — title finding (author call; NOT retitled)

The current title claims **protection** rather than naming the condition:
> STRUCTURAL ERROR CORRECTION — *From Arithmetic to Biology: Silence as Protection*

"Silence as **Protection**" reads as a possessed property, against the pass's scope discipline (the
compiled result is the *condition*, not protection per se). **Two alternatives that name the condition
(STOP short of retitling — the author picks):**
1. **STRUCTURAL ERROR CORRECTION — The De-Alignment Condition: When Single-Domain Correlation Is Defeated**
2. **STRUCTURAL ERROR CORRECTION — From Arithmetic to Biology: Silence, Stages, and the De-Alignment Condition**

(1) leads with the compiled condition; (2) keeps the four-domain survey scope and only swaps "as
Protection" for "the De-Alignment Condition." Author rules; no retitle made this pass.

## Pins

- PLACE-papers `main` — `7f1d3b4` (local = remote; core RH rail empty-diff, `67da789..HEAD` = `[]`).
- Kernel — `SIDE-structural-error-correction` v0.2.1 — `6a4f4829cf219839f33c6af9d665687b93af772e`.
- Steane rows — `SIDE-cosmo` main — `c5cba30`.

No paper other than `ERROR_CORRECTION.md` (p2-16) edited; REGISTRY p2-16 row updated to v1.1 / REVIEW.
