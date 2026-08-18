# `W-ATTEMPT-2` · SITTING 5 — THE CYCLOTOMIC HALF BUILT
## ### **THE SECTION'S PROPERTIES CERTIFIED IN EXACT ARITHMETIC — 55/55 LINES EXACT AT BENCH, 16/16 TERMINALS AXIOM-FREE IN VANILLA LEAN — THE FLOAT-ERA RESIDUALS ARE NOW ZEROS, NOT SMALL NUMBERS**

**Relay report · 2026-08-18 (twenty-fifth sitting) · author-called ("certify what was built") · attempt
work RELAY-ONLY; the formal module relay-resident · closure-protocol step one run against the
CONSTRUCTION, never against any sign · nothing deposits**

> ### **THE CORRECTED STOP IN FORCE (restated): measured properties of constructed objects are DATA at
> bench grade; refused — promotion to `W_∞ − ΣW_𝔭` at complete roster, or register movement. SUB-GATE
> restated. This sitting certifies the BUILT object; it asserts no sign and moves no register.**

```
PLACE-papers  origin/main : f247d85 (UNTOUCHED this sitting)
relay         origin/main : (this report, in the sittings-5/6 batch)     local +1 HELD
instruments   tools/e16/b18_attempt2_s5.py (registration banked BEFORE the run:
              data/b18_registration_2026-08-18.txt) · data/b18_2026-08-18.txt
formal        tools/lean/DiagonalSection.lean + AxiomCheckDiagonalSection.lean (pinned v4.29.1)
```

> ### **RULE-3 LOG:** *the ferry's cited identities checked against bank — sitting 4's `D-yes` and
> punctuated-weight table (`f967f10`) ✓ · the closure protocol (charter `§3`, read verbatim) ✓ · the
> corrected stop ✓ · inertia `(d/4, d/4, d/2)` (sitting 2's banked line) ✓. Terms coined: none. Banned
> check: clean (V.8 spirit-over-letter; no coinage shipped).* ### **ONE DISAGREEMENT FOUND AND FLAGGED,
> NOT SILENTLY RESOLVED: the ferry writes the archimedean window `[a⁻¹, a]`; sitting 4's banked
> registration wrote `[1/a², a²]`. Both radii are run in sitting 6; no convention adjudicated.**

---

## §1 — THE EXACT BENCH: ### **EVERY FLOAT-ERA LINE OF THE SECTION'S CERTIFICATE, RE-LANDED AS AN EXACT ZERO — 55/55**

*The field: `ℚ(ζ₁₄₄)` as Fraction-vectors mod `Φ₁₄₄(x) = x⁴⁸ − x²⁴ + 1` (no floats anywhere in a
certified line; every local DFT has RATIONAL normalization `√N ∈ {2,3,4}`, so every matrix entry is in
the field). The exact basis replacing `b8`'s float SVD basis: in the chart `m = α + pⁿβ`,
`k_(α,j) = δ_α ⊗ (e_j − e_(j+1))` — integer columns; the certified properties are basis-free.*

| certified line *(per factor `(2,1)`, `(3,1)`, `(2,2)` — the diagonal cells at `a ∈ {√2, √3, 2}`)* | float era | ### **exact era (this sitting)** |
|:--|:--|:--|
| the basis lands in `Son` (ball + transform-side ball) | `~1e−16` | ### **EXACT** |
| T-invariance `F K = K M` | closure `~1e−16` | ### **EXACT — residual literally zero** |
| the parity structure | `F² = P` at machine | ### **`M² = Π` EXACT, `Π` a signed permutation, `det Π = ±1`** |
| radical zero | rank by SVD tolerance | ### **`G_loc = (KᵀK)·M`, `det(KᵀK) ∈ {2, 9, 64}` — nonzero INTEGERS, `M` invertible by `M² = Π` ⟹ rank = dim, EXACTLY** |
| twisted-Hermitian | `‖G − (P⊗1)G†‖ = 5.8×10⁻¹⁵` | ### **`G_loc = G_locᵀ` and `conj(G_loc) = G_loc·Π` — EXACT: the twist is an IDENTITY now, not a small residual** |

> ### **AND THE INTEGER `det(KᵀK)` HAS A SHAPE: `2, 9, 64 = 2¹, 3², 4³ = (pⁿ)^(pⁿ−1)`** *— the
> path-Gram determinant per support slot (`KᵀK = I_(pⁿ−1) ⊗ T` with `T` the order-`(pⁿ−1)` difference
> Gram, `det T = pⁿ`). Noted as structure observed in-run, not registered in advance.*

**The class factor (C6), exact in `ℤ[ω]`:** *χ(c₂c₃) = `(4, 1, 1)` with the imaginary parts landing
EXACTLY zero · the Gram's class factor IS the circulant `C = [[2,1,1],[1,2,1],[1,1,2]]` = the
multiplication-by-coupling matrix — symmetric, `det C = 4` · the trace identity `tr C = 6 = 4+1+1`:*
### **the coupling spectrum as the CLASS-CHARACTER TRACE, now exact (the τ-route; question grade).**

**The glued cells (C7):** *dims `(3, 12, 108)` by the exact tensor laws — and the dim-12 cell computed
DIRECTLY glued and checked entry-exact against the tensor assembly:* ### **`K_gᵀ(F₄⊗F₉)K_g = G₂⊗G₃`
entry-exact, glued T-invariance exact, tensor parity `(M₂⊗M₃)² = Π₂⊗Π₃` exact, tensor twist exact, the
full 12×12 section Gram `= G_g ⊗ C` entry-exact, `A² = 1` and `ACA = C` exact** *— the "factor-certified"
mode of sitting 4 is now an exact theorem-shape, verified on the one cell small enough to do both ways.*

**(C8) inertia:** *carried as banked DATA (`(d/4, d/4, d/2)`, sitting 2's run), not re-derived — a
signature is a real-form computation this pass does not repeat; a data row, never a sign datum.*

*Instrument notes: run reproduced end-to-end by the executor after the build (same 55/55). The
registered docstring is byte-identical in the banked registration; the instrument folds typographic
characters to ASCII at print time only — both data files verified 0 non-ASCII bytes (the sibling
`b16`/`b17` files leak cp1252 bytes; this one does not). Runtime 0.6 s; no float fallback anywhere.*

## §2 — THE FORMAL MODULE: ### **16/16 TERMINALS, EVERY ONE "does not depend on any axioms"**

*`tools/lean/DiagonalSection.lean` — vanilla Lean 4 (`v4.29.1`, pinned, invoked directly), decide/rfl
only, compiled with its axiom check:*

> **the `a = √2` cell over `ℤ[i]`:** *`f = e₁ − e₃` vanishes on the ball and so does its transform ·
> `TF4·f = 2i·f` (T-invariance at the cell, an EIGENVECTOR statement) · parity sends `f` to `−f` ·
> the Gram integer `⟨f, TF4 f⟩ = 4i ≠ 0` (radical zero at the cell) · `conj(4i) = (−1)·4i` (the
> parity-twisted-Hermitian identity at the cell)* — **compiled.**
> **the class factor over `ℤ[ω]`:** *`χ(c₂c₃) = (4,1,1)` with ω-parts exactly zero, all nonzero · the
> circulant symmetric, `det C = 4 ≠ 0` · the trace identity `tr C = 6 = χ₀+χ₁+χ₂` · the label-norm
> enumeration: the four norm-6 label sums have class counts `(2,1,1)` = the coupling's coefficients ·
> `A² = 1`, `ACA = C`* — **compiled.**

### **WHAT NEEDS A MATHLIB COMPANION, NAMED NOT FAKED:** *the `{3:1}` and `{2:2}` factors need exact
`ℚ(ζ₉)`/`ℚ(ζ₁₆)` arithmetic (glued: `ℚ(ζ₃₆)`, `ℚ(ζ₁₄₄)`) — Mathlib's `NumberTheory.Cyclotomic` /
`Polynomial.cyclotomic` territory, or a hand-rolled tower with proved reduction. NOT built here; the
bench holds those entries exactly with its registration banked; the module carries the decide-reachable
shadow and names the companion on its face.*

*(One method note, kept for the record: fallback-pattern `match` definitions pull `propext` into
`decide` terminals; rewritten match-free — field projections and exhaustive structures — after which
every terminal is axiom-free.)*

## §3 — WHAT THIS SITTING CLOSES

1. ### **CLOSURE-PROTOCOL STEP ONE, AGAINST THE CONSTRUCTION, IS NOW RUN AT THE PAIRING LEVEL** *—
   sitting 2 compiled the integer shadow (`ℤ[ℤ/3]`); this sitting certifies the PAIRING's properties:
   exact where `decide` reaches, exact-bench (with the companion named) where the tower is needed.
   There is no float left under any certified property of the built section at the three diagonal
   cells.*
2. ### **THE FOUR REGISTERED PROPERTIES ARE IDENTITIES, NOT RESIDUALS:** *radical zero · the
   parity-twisted-Hermitian `G† = G·Π` · T-invariance `FK = KM` with `M² = Π` · the spectrum-as-trace
   `(4,1,1)`.*
3. **NOT touched:** *the archimedean factor (sitting 6's model, next) · inertia (data) · any sentence
   about any sign · the register.*

**`h2` UNCHANGED. THE REGISTER SENTENCE UNTOUCHED. NO PROMOTION TO `W_∞ − ΣW_𝔭` AT COMPLETE ROSTER.
NOTHING DEPOSITS.**
