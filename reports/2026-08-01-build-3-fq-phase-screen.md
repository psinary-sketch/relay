# BUILD-3 checkpoint — the 𝔽_q phase screen, concrete curves — 2026-08-01

Third pass of the h2 build slate. **Registered prediction (recorded before computation, per
UAC-7's falsifiable form): for every tested curve, the phase layer is BRIGHT — the pairing-form's
eigen-sign pair (the 2-bit phase layer) is (+,+), computed from the point counts alone with no
auxiliary choice: 0 hidden bits; and the discriminant a² − 4q < 0 concretely, not by citing
Hasse.**

## The computation (three concrete curves, counts doubly-sourced)

The proved-supplier instance in miniature: on ℤ[F] ⊆ End(E), the degree form
deg(m + nF) = m² + a·mn + q·n² — the positive-definite quadratic form whose definiteness is the
intersection-form supplier's rank-2 shadow. Route A: brute-force point count over 𝔽_q → a.
Route B (independent): brute-force count over 𝔽_{q²} checked against q² + 1 − (a² − 2q).

| curve | #E(𝔽_q), a (A) | 𝔽_{q²} consistency (B) | a² − 4q | Gram det, trace | eigen-signs | \|α\| vs √q | form min |
|:--|:--|:--|:--|:--|:--|:--|:--|
| y² = x³ + x + 1 / 𝔽₅ | 9, a = −3 | 27 = 27 ✓ | −11 < 0 | 2.75 > 0, 6 > 0 | **(+,+)** | 2.236068 = 2.236068 | 1 |
| y² = x³ + 2x + 1 / 𝔽₇ | 5, a = 3 | 55 = 55 ✓ | −19 < 0 | 4.75 > 0, 8 > 0 | **(+,+)** | 2.645751 = 2.645751 | 1 |
| y² = x³ + 3x + 5 / 𝔽₁₁ | 9, a = 3 | 135 = 135 ✓ | −35 < 0 | 8.75 > 0, 12 > 0 | **(+,+)** | 3.316625 = 3.316625 | 1 |

## Verdict at grade

**The registered prediction SURVIVED on all three instances.** The brightness is concrete: one
integer datum (the count) determines the entire definiteness structure — discriminant negative,
both eigen-signs positive, |Frobenius eigenvalue| = √q, form minimum 1 — with **no residual sign
or orientation choice anywhere in the computation**. That is "0 hidden bits" operationalized: the
2-bit phase layer (the eigen-sign pair) is an output, never an input.

**Scope, honestly:** three small prime-field elliptic curves are instances, not the theorem; the
theorem (positive-definiteness of the degree form on End°) is classical (Deuring/Weil), and the
build's contribution is the SCREEN — the checklist form of UAC-7 now has a worked template: any
proposed ℚ-construction of the positive space can be asked to exhibit its counting datum and show
its sign pair as an output. Over ℚ the corresponding bits are exactly what `h2` withholds — the
screen's ℚ-column stays empty by the arc's own standing content. `W-ORD-FQ-PHASE-SCREEN`'s
computation half is discharged at this depth; the standing-checklist half now has its template
(the work-order stays open for the checklist filing at the author's call).

## Pins

- Computation-only; no kernel commits, no paper edits, nothing deposits. The slate's three
  passes are complete (1+4 kernel HELD at lv `5a14205`; 2 and 3 computational, reports filed);
  rail empty-diff at `11db565` verified at the slate close.
