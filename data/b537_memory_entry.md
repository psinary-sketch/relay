---
name: project-criterion-b533-b536
description: "b533–b536 standing — Weil's criterion compiled in the programme's own kernel, h2_sign ↔ Mathlib RiemannHypothesis; tags v0.1/v0.2; ceiling (R146)(2); written b537 under (R147)(3)"
metadata:
  node_type: memory
  type: project
  originSessionId: 0e414d80-fcb3-4850-8359-5f1a764bc0e3
  modified: 2026-09-25T21:31:45.586Z
---

**The standing after b536 (2026-09-25):** h2_sign (Weil positivity on classK) is equivalent to Mathlib's RiemannHypothesis. Both directions are compiled at the standard three [propext, Classical.choice, Quot.sound] as `SIDEExplicitFormula.B321.h2_sign_iff_rh : h2_sign ↔ RiemannHypothesis`, with no hypothesis.

**The ceiling, (R146)(2), verbatim:** *Weil positivity on classK (h2_sign) is equivalent to Mathlib's RiemannHypothesis, both directions compiled at the standard three (h2_sign_iff_rh, SIDE-explicit-formula v0.2); the deposit's Route 3 clause is RH restated by a compiled ten-line lemma (E-2026-09-25-1).*

**The two tags on SIDE-explicit-formula:**
- v0.1 = baed4df861dac05224f01dad17453648d3d7fe0a (b534's PowerLimit: h2_sign ↔ rh_strip).
- v0.2 = 5c72cad24303f23d92256ebd466d3a3d32424a4b (b536's Seam: h2_sign ↔ RiemannHypothesis).

**Not claimed:** RH proved; h2_sign proved; the earliest Lean formalization of Weil's criterion.

The acts:
- **b533**: PowerWindow.lean, L1–L6, 34/34 std3; row 382.
- **b534**: PowerLimit.lean, 89/89 std3; `h2_sign_iff_rh_strip`; the seam `rh_strip_imp_rh` was left a Prop; row 383.
- **b535** (the update act, (R145)):
  - E-2026-09-25-1 filed, deposit-facing: the kernel's Route 3 premise is RH restated.
  - E-2026-09-25-2: three Zenodo description edits under (R110), fetched back MATCH.
  - The fold "THE WEIL CONVERSE ARC, b526–b534" is in FINDINGS.
  - The (R145)(2) ceiling; rows 384 and 385; tag v0.1.
- **b536** ((R146)):
  - Seam.lean, 6/6 std3. `zeta_zero_re_nonpos` (:25) comes from Mathlib's functional equation; the seam is proved.
  - Row 386 grades six DERIVES; tag v0.2.
  - Prior art: github.com/peter941221/Connes-Weil-RH-Proof. It works on the Weil/Connes side, has five project axioms and does not prove RH. The "first formalization" sentence was entered in corrected form (FINDINGS:4729).
  - Understandings entered at FINDINGS:4751, with item 3 CORRECTED: the b522 witness window is an indicator convolved with a B-spline (b521_tail.py:53), not the ladder's Cox–de Boor family.
- **b537** (R147): mirror `mirror-refresh-2026-09-25-b537.zip` built with this ceiling at its MANIFEST head.
  - Work-orders named: W-ORD-SEAM-UPSTREAM (trigger: the author's word) and W-ORD-REGISTER-DEPTH (trigger: the act after b537 unless the author rules otherwise).

**Why:** (R147)(3) orders this entry so a later session carries the criterion's standing and its limits. An equivalence between two open statements proves neither. `h2` stays where the deposit left it.

**How to apply:**
- Quote the ceiling above; never widen it to "RH proved" or "first in Lean".
- The ledgers on D: remain the currency authority until the author uploads the mirror.
- Next by default is W-ORD-REGISTER-DEPTH: R1, R3 and R5 of §27.3, read against b512's table (relay data/b512_closing.txt:5-7).

See [[project-power-window-b533]], [[project-power-limit-b534]], [[project-bridge-read-b531]].
