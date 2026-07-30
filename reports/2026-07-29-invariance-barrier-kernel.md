# invariance_barrier — the two-witness lemma, committed (general form) — 2026-07-29

Author ruled: commit the two-witness lemma in **general form only** — arbitrary invariance class, arbitrary
witness pair, conclusion that the target property is not determined by the class; hypotheses named
(agreement; divergence); **no** ξ/Epstein instantiation (any `agree ξ Z` with a stipulated body is the C₇
pattern, rejected in advance); clause (i) stays manuscript-resident as W-ORD-FACE-E-INDISTINGUISHABILITY.

## What was committed

`Kernel/Cascade/InvarianceBarrier.lean` in **SIDE-kernel** (the repo the sieve/ceiling material lives in —
beside `SieveCeilingSemantic.lean`, whose docstring *"the non-invariance witness is abstract here"* this makes
precise). No imports (core logic only); no zeta, no RH, no Euler product anywhere in the file.

```lean
namespace InvarianceBarrier
universe u
variable {α : Type u}

def DeterminedBy (agree : α → α → Prop) (P : α → Prop) : Prop :=
  ∀ x y, agree x y → (P x ↔ P y)

theorem invariance_barrier
    {agree : α → α → Prop} {P : α → Prop} {x y : α}
    (h_agree : agree x y) (h_diverge : ¬ (P x ↔ P y)) :
    ¬ DeterminedBy agree P :=
  fun h_det => h_diverge (h_det x y h_agree)
end InvarianceBarrier
```

The name carries no RH/zeta content, as ruled. The `¬ (P x ↔ P y)` divergence form is deliberately the
axiom-free one (a truth-value split would need `propext`); this keeps the lemma genuinely axiom-free.

## E0 salt-check (verbatim tool output)

`#check @InvarianceBarrier.invariance_barrier`:
```
@InvarianceBarrier.invariance_barrier : ∀ {α : Type u_1} {agree : α → α → Prop} {P : α → Prop} {x y : α},
  agree x y → ¬(P x ↔ P y) → ¬InvarianceBarrier.DeterminedBy agree P
```
`#check @InvarianceBarrier.DeterminedBy`:
```
@InvarianceBarrier.DeterminedBy : {α : Type u_1} → (α → α → Prop) → (α → Prop) → Prop
```
`#print axioms InvarianceBarrier.invariance_barrier`:
```
'InvarianceBarrier.invariance_barrier' does not depend on any axioms
```
`#print axioms InvarianceBarrier.DeterminedBy`:
```
'InvarianceBarrier.DeterminedBy' does not depend on any axioms
```

**Salt-check verdict: DERIVES, genuinely axiom-free** (not merely within std3 — *no* axioms). 0 sorry, 0
`native_decide`. Not a shell: both named hypotheses are load-bearing (drop either and the term does not
type-check), the conclusion negates a non-trivial ∀-quantified invariance predicate, and `DeterminedBy` is a
real universally-quantified iff, not `True ↔ True`. The mathematical weight sits honestly in the two named
premises; the kernel proves only the relativization skeleton.

## SHA triple (tag v1.6)

```
verified commit = 01e5633a12bf08afe8ed79e5b59f3f0350f5274e
tag-object      = 6fe58c1cd35004095a804ff3531c41a359b321e1
peeled          = 01e5633a12bf08afe8ed79e5b59f3f0350f5274e
peeled == verified : YES   (annotated tag, peels to the verified commit)
```
Branch and tag pushed; local = remote for both (`derivative-engine` = `01e5633`; `v1.6` = `6fe58c1`).
Only the two new files were staged; the pre-existing untracked temp files (`AxiomCheck_PF_v1_5.lean`,
`tmplcvugi_v.lean`) were left untouched, not committed.

## DEVIATION — flagged for ruling (release-tag branch placement)

The lemma is correct, verified, and in the right repo. **But the release tag v1.6 landed on branch
`derivative-engine`, not `main`**, and this is off the established pattern:

- `origin/HEAD → origin/main` (main is the default branch); **v1.3, v1.4, v1.5 all sit on `main`**.
- `derivative-engine` is **4 commits ahead of `main`** (`main`-only = 0). Those 4: `27a3ae7` (derivative-engine
  Phase 2), `75668a0` (Voice7 `c7_forces_half` deprecation), `3b2e8d6` (tautology-sweep hygiene), and my
  `01e5633` (the lemma). **v1.6 therefore bundles 3 unmerged feature commits** plus the lemma.
- The lemma file is standalone — it imports nothing and has **no dependency** on those 3 feature commits, so
  it applies cleanly onto `main`.

I did not force-rewrite the published v1.6 tag or merge branches, as both are hard-to-reverse / your-call
actions. **Recommended correction (awaiting ruling):** cherry-pick `01e5633` (the lemma alone) onto `main`
and cut the release tag there, leaving `derivative-engine`'s feature work to merge on its own schedule — OR,
if `derivative-engine` is now the intended release line, ratify v1.6 where it is. Either is one short pass on
sign-off.

## Pins

- SIDE-kernel `derivative-engine` — `01e5633`, tag **v1.6** = `6fe58c1` (peels to `01e5633`). Local = remote.
  Axiom-free.
- PLACE-papers `main` — `4b81b72` (the SPIRAL_MAP Translation section, item 2). Rail empty vs baseline
  `11db565`.
- Clause (i) remains manuscript-resident (W-ORD-FACE-E-INDISTINGUISHABILITY); no instantiation in the kernel.
  Nothing deposited.
