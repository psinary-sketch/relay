# Held batch — the substrate redundancy resolution (CP3) — **LANDED 2026-07-28 (author-ruled)**

> **Status: LANDED.** All five pieces applied (A–E): the pointer-diffs, the CATALOGOS/AT_REST re-grades, the seam corrections, the spinor-leg branch merge (`SIDE-spinor` main `520abe7`), and the keystone completion. This document is retained as the batch's record. (CARTAN_B/POISSON single-summand pointers remain for a completion sweep.)


*W-SUBSTRATE-UNIFICATION CP3, 2026-07-28. With `THE_SUBSTRATE.md` as the one canonical home, each site that re-derives the {2,3}/(2,3,2,0) core gets a **pointer** to it while **keeping its local one-paragraph statement** — documents stay readable alone, the full derivation lives once. The W-KEYSTONE-LAYER panel re-grades ride in the same batch. **All HELD as one reviewable set; nothing applied; RH rail untouched.***

## A · Redundancy pointers (the ~10-site core-derivation restatement)

The seam read found the "(2,3,2,0)=7, each summand from an independent classification" derivation restated across ten keystones. Each held diff: **keep the local paragraph, append one line — "Full derivation: `THE_SUBSTRATE.md` §(ii)."** No local content is deleted.

| site | what it restates | held diff |
|:--|:--|:--|
| `CATALOGOS.md` §4.1 (L136) + Ch.16 (L521) | the count-7 deduction + the covering tower | pointer to §(i)+(ii); the tower is §(ii).4 |
| `phase2/formation/UNIVERSALITY.md` §2–3 | (2,3,2,0) for ζ_K | pointer to §(ii).5 + §(iii) (the count lifts, the substrate does not) |
| `AT_REST.md` §5 | the (2,3,2,0)=7 panel | pointer to §(ii).5; **+ panel re-grade, section B** |
| `CASE_FOR_TWO.md` (L26, L210, L225) | the summand derivation | pointer to §(ii) |
| `CARTAN_B.md` (L33, L287, L296) | n₃=2 pillar | pointer to §(ii).4 |
| `ENUMERA.md` (L69, L136, L1037) | the seven-fold enumeration | pointer to §(ii).1 |
| `SIDE_EXCLUSION.md` (L51, L109) | the count | pointer to §(ii).5 |
| `POISSON_EXHAUSTION.md` (L18, L265) | n₂=3 from Poisson | pointer to §(ii).4 |
| `A_METHODOLOGY.md` (L359) | the derivation as method | pointer to §(ii) |
| `day1/Seven_Mechanism_Classes.md` (L204) | the seven classes | pointer to §(ii).1–3 *(day-1 / RH-rail — held with extra care)* |

*Also carried to the canonical home (not deleted at source): the cross-system convergences — count=7 (five witnesses), total=81 (two routes, one theorem), the calibration −1 (two disjoint routes), the seven-element set (six presentations) — now presented once, as §(ii)'s multi-instrument standard.*

## B · The panel re-grade (rides from W-KEYSTONE-LAYER)

`CATALOGOS.md` Part III (Ch.9 L285–309) + Ch.16 (L521–530) and `AT_REST.md` §5 (L156–224) assign a formation tuple to a **heterogeneous panel** (Shannon (2,2,2,0), Maxwell (2,3,2,0), DNA, Yang–Mills) and call it "proved universally." *Held diff:* re-grade on **classification × certification**; the tuple column **scoped to the arithmetic tier** (ξ, L-functions); Shannon/Maxwell/genetic-code → **classify-only / per-parsing-scalar** — the three-tier breadth, and exactly what the corpus's own κ/μ data always showed. Control arm dated: "*earlier the tuple was asserted universal across the 21-system panel; superseded — the tuple is substrate-scoped (`THE_SUBSTRATE.md` §(iii)).*"

## C · The seam corrections (from CP1's seam list)

- **STORMER.md stale citation.** `STORMER.md` (L11/L139) cites the terminal `SIDEOmegaB.omega_b_equals_4_over_81` — **this name does not exist on disk**; the actual terminals are the `xi_total`/`xi_visible`/`xi_dark`/`xi_wall_sq`/`xi_77` cluster (`SIDE-cosmo c5cba30`). *Held diff:* repoint the citation to the real terminals (the same fix the HELD_COSMO SITE-1 rewrite already names). A named-terminal-at-pin correction, W-9 class.
- **The Γ₀(4)-torsion erratum.** Any site attributing the order-2/order-3 elements (S, ST) to Γ₀(4) is loose: Γ₀(4) contains neither (c ≢ 0 mod 4; ν₂ = ν₃ = 0); the torsion lives in the ambient PSL₂(ℤ), and χ_θ is 2-adic (no order-3 content). *Held diff:* carry the §8.3 caveat forward wherever the tower is stated — `THE_SUBSTRATE.md` §(ii).4 already states it correctly; the older sites point there.
- **The spinor-leg honesty.** The weight-½ metaplectic identification (W⁴ = −Id) and the Γ₀(4)-equivariance are **open research, not formalized**, and the manuscript `THE_SPINOR_CALIBRATION_v0_1.md` is **absent from disk** (its content survives only in kernel headers). *Held note (not a diff):* the canonical home states this leg OPEN on its face; no site should read the calibration's spinor leg as compiled.

## D · The spinor leg landed (W-REVIEWER-LENS) — the §(ii).4 open item closes

The keystone's one open item is now a **compiled kernel theorem.** `SIDE-spinor` held branch `substrate-spinor-leg` `4f5848d` (`SpinorLeg.lean`): the metaplectic quarter-twist route to −1 — `spinor_signature` (T²=−1), `metaplectic_cocycle` (W⁴=−1 for W²=T), `zeta8_sq_eq_T` + `zeta8_pow_four` (the concrete order-8 witness ζ₈=(1+i)/√2). **`lake build`-clean; axioms audited = the standard three axioms {propext, Classical.choice, Quot.sound}; −1 DERIVED (`Complex.I_sq`, `ring`), salt-check passes.** It is the **second, disjoint route** to the calibration −1 (Route A Frobenius/vanilla-Int vs Route B metaplectic/Mathlib-ℂ; no shared lemma).

*Held diff to the keystone:* `THE_SUBSTRATE.md` §(ii).4 updates — "the spinor leg is **open research, not formalized**" → "**compiled** (`SpinorLeg.lean`, standard three axioms), the second disjoint route to −1"; and the front-matter/closing "the one open item is the spinor leg" → the leg is closed, both −1 routes compiled and visibly disjoint. **Applies when the author lands the `substrate-spinor-leg` branch.**

## E · The reviewer panels + Related Work (W-REVIEWER-LENS)

`THE_REVIEWER_PANELS.md` (five adversarial panels, bounded items run: the GUE ε-stability sweep [β≈1.5, ε-stable, β≈12 refuted]; the Ξ.12 independence matrix [count-7 ≈4.5 independent instruments; −1 three disjoint routes]; the precise Steane uniqueness quantifier; the λ=12 bosonic-string anchor; the classical-vs-new partition). *Held diff to the keystone:* add the **Related Work** section (the components are classical — genus theory, idoneal numbers, Størmer, Serre, Steane/Hamming, ζ(−1)=−1/12, the string critical dimension; the contribution is the unification + certification + the exemplar). The precision fixes (Steane uniqueness per-stage; λ=12 anchor) fold into §(ii).

## The batch, as one ruling

Landing this batch (A + B + C) does three things at once: **the core derivation lives once** (A — the ten sites point to `THE_SUBSTRATE.md`, each still readable alone); **the universal-tuple over-reach is corrected** (B — the panels scoped to the arithmetic tier); **three stale/loose citations are fixed** (C — the phantom `SIDEOmegaB` terminal, the Γ₀(4) torsion, the unformalized spinor leg). None of it touches the RH rail's mathematics — the day-1 pointer (A, `Seven_Mechanism_Classes`) is the only RH-adjacent edit and is a one-line pointer, not a content change. **The author lands it, or any part of it, on one word.**
