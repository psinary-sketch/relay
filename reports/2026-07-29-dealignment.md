# DeAlignment — 2026-07-29

`SIDE-structural-error-correction`: the de-alignment condition module added. Single-domain faults cannot
complete a line under the de-alignment condition; decidable over the Fano incidence structure; axiom-free.

## What landed

`SIDEStructuralErrorCorrection/DeAlignment.lean` (new; root import line added to
`SIDEStructuralErrorCorrection.lean`). Vanilla Lean 4, no Mathlib. The module states the **design
condition** — each Fano line's three positions occupy three distinct failure domains — and derives the
**protection theorem** from it: no single-domain failure completes any line, hence none induces a
minimum-weight logical operator of the [[7,1,3]] code. The condition is **decidable** over the finite
incidence structure (`dealignedCheck`), so a realization certifies itself by evaluation
(`fano_dealignment_decidable_example = true`; the collapsed-line realization is refused,
`fano_collapsed_line_rejected = false`). No encoding of the conclusion, no placeholder Props.

Not claimed (on the module's face, deferred to the threat model): protection against arbitrary faults,
correlated faults spanning several domains, states outside the modelled space, or faults in the
verification apparatus itself.

## Build

`lake build` — exit 0. `✔ Built SIDEStructuralErrorCorrection.DeAlignment (60s)`; build completed
successfully (5 jobs). Toolchain `leanprover/lean4:v4.29.0-rc8`; no external packages.

## Axioms — verbatim (`#print axioms`, all four expected axiom-free)

```
'DeAlignment.dealigned_of_lines_injective' does not depend on any axioms
'DeAlignment.no_domain_covers_line' does not depend on any axioms
'DeAlignment.single_domain_fault_not_logical' does not depend on any axioms
'DeAlignment.fano_dealignment_decidable_example' does not depend on any axioms
```

All four **axiom-free** — no deviation.

## SHA triple

- verified commit — `git rev-parse HEAD` — `4ce0534cf8ae5777baa752280e9681146dfab3eb`
- remote main — `git ls-remote origin refs/heads/main` — `4ce0534cf8ae5777baa752280e9681146dfab3eb`
- tag `v0.2.0` peeled — `git ls-remote origin 'refs/tags/v0.2.0^{}'` — `4ce0534cf8ae5777baa752280e9681146dfab3eb`

Annotated tag object `f66785a80c7fdf07ec2d1b04517fb02978b91efa` peels to the verified commit. Triple
consistent; main + tag pushed to `origin` (github.com/psinary-sketch/SIDE-structural-error-correction).

## Scope note

No paper edited this pass. The `STRUCTURAL_ERROR_CORRECTION` Correspondence row and the threat-model
paragraph are a separate ratified pass, per the ruling.
