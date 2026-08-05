# The critical mechanism theorem, audited and placed · refusal criteria for heads 1, 2, 4 — 2026-08-05

Pins at open: PLACE-papers `1f4ce51`; relay `bc0b031`; lv main `14720d9` (four modules on an
unlanded working tree); SIDE-kernel `44895f9`. Rail at the post-rename baseline. Nothing deposits.

---

## §1 — THE STATEMENT OF RECORD: A COMPILED TERMINAL, NOT INHERITED PRACTICE

The question was whether the exclusion syllogism the era leans on exists as a compiled object or
only as a practice the corpus repeats. **It exists, twice, and both are on the loom already.**

| name | location | axiom profile | loom row |
|:--|:--|:--|:--|
| `ECondition.type_I_has_ostrowski` — the general exclusion syllogism | `D:\SIDE-kernel\MetaKernel.lean:147` | `[propext, Quot.sound]` | `VERIFICATION_LOOM.md:262` (pass of 2026-06-13) |
| `Interfaces.parametric_mechanism_theorem` — the κ-form | `D:\SIDE-interfaces\Interfaces\ConnectionRequiresStructure.lean:41` | `{propext, Classical.choice, Quot.sound}` | `VERIFICATION_LOOM.md:1594`, pin `v0.2 = 1728796` |

**These are not two copies of one theorem.** The second is the interface calculus's specialization —
*no A-side perturbation moves the B-side observable ⟹ κ = 0* — which is the syllogism applied to a
particular domain and target. The **general** form, and the one the era's arguments invoke, is the
first. The audit below is of the first.

Statement of record as the loom carries it:

> over a finite domain, if no element produces the target and the target requires some element to
> produce it, the target fails

Statement as compiled:

```lean
theorem type_I_has_ostrowski (Domain : Type) [Fintype Domain]
    (target : Prop) (produces : Domain → Prop)
    (h_none : ∀ d, ¬(produces d))
    (h_target : target → ∃ d, produces d) :
    ¬target := by
  intro ht
  obtain ⟨d, hd⟩ := h_target ht
  exact h_none d hd
```

---

## §2 — THE SHORTFALL, MEASURED: ONE CLAUSE IS INERT AND TWO ARE ABSENT

### 2a. The finiteness clause does no work — probed, not inferred

The statement of record opens with *over a finite domain*, and the compiled form carries
`[Fintype Domain]`. **The proof never uses it.** Rather than read this off the tactic block, the
pass probed it: the same conclusion, from the same two hypotheses, with the finiteness assumption
deleted and **no imports at all** (so `Fintype` is not even in scope), compiled under the
lv toolchain and reported

```
'mechanism_without_finiteness' does not depend on any axioms
```

Two consequences, both exact:

1. **The syllogism is valid on any domain whatsoever** — infinite, empty, uncountable. It is modus
   tollens composed with an existential elimination. The word *finite* in the statement of record
   describes the intended application, not a hypothesis the theorem uses.
2. **The recorded axiom profile is attributable entirely to the inert clause.** `[propext,
   Quot.sound]` is what the unused `Fintype` instance argument drags in from Mathlib; with the
   clause removed the profile is **empty**. The loom's row is correct as recorded and now carries a
   sharper reading: those two axioms certify nothing about the theorem's content.

### 2b. The two clauses the era's use needs, and where they actually live

The shortfall is **two clauses**, and they are precisely the two that carry the argumentative load:

**(i) That the enumeration CLOSES.** Not in the theorem. It sits in `rh_classes_complete` and the
`Fintype RH_MechanismClass` instance — and the kernel's own companion document already grades those
honestly, at `phase1.5\spectral\DOMAIN_OSTROWSKI_UNIVERSALITY_v0_1.md:140-142`:

> The `exhaustive` field as written is tautological; the real exhaustiveness lives in the claim that
> the inductive type's constructors are *all* the mechanism classes there are.

Those theorems certify that a seven-constructor inductive type has seven constructors. That is a
fact about a datatype, not about mathematics.

**(ii) That each class genuinely fails to produce.** Also not in the theorem, and MetaKernel's own
comments record its retirement: `[M1 retired] produces_offline (:= False for all 7) and
rh_none_produces (proved not-False)`. The per-class exclusion was withdrawn as hollow and re-sited
as **conditional** in `Bridge/ConservationBridge.lean`, tracked as `ConservationHypothesis` — the
corpus's `h2`.

### 2c. The reading, stated so it cannot be mistaken for a defect claim

**The compiled theorem is a valid schema with zero content about closure, and that is what it is
for.** It is the socket the certificate plugs into; it is not, and was never, the certificate. No
defect is claimed against the theorem. The one place a defect could arise is in reading *over a
finite domain* as though the clause certified the finiteness rather than assumed it — and §4 reports
where that reading has and has not occurred.

---

## §3 — FILED AS THE FIFTH FACE OF HEAD 1

Per the standing instruction at `FINDINGS.md:553` — *a future arrival naming this property from a
new direction files as a FIFTH FACE of this finding, not a fifth finding.* This is exactly such an
arrival, and it is the first one the instruction has had to govern.

**Face name: the exclusion syllogism.** What it adds that the other four do not: the previous four
faces name the property from the side of the *family* (it is enumerable · it completes · N checks
suffice · it is Π₁). This face names it from the side of the *inference* — and reports that the
inference is closure-free. The syllogism is the exact point in every exclusion argument where a
closure certificate would have to be consumed, **and it consumes nothing**. It transports whatever
certificate you hand it and manufactures none.

**The consequence, which is the face's content:** an exclusion argument's strength is exactly its
enumeration's closure certificate and nothing else — the syllogism contributes no strength of its
own. Hence the certificate must be exhibited **at every call site**, because there is no stage
downstream where it could be supplied.

---

## §4 — THE FOUR LOAD-BEARING SITES

| site | closure certificate? | how closure is (or is not) secured |
|:--|:--|:--|
| **Face-E** — the method barrier | **CLOSURE-ASSUMED**, openly declared | T is a *named finite* six-tool toolkit; Tier 2 explicitly not claimed |
| **E-8** — composition operations | **CERTIFICATE-STATED** | closure typed by transport-soundness, deliberately without enumeration |
| **the supplier mechanism column** | **CLOSURE-ASSUMED**, disclaimed at its home cite | an open inductive list; not used to exclude |
| **the toy's per-object routes** | **CERTIFICATE-STATED** — the strongest | closure is a named classification theorem |

### Face-E (`phase1.5\method\INVARIANCE_BARRIERS.md` §3.4, Thm 3.7)

The toolkit is six named tools (functional equation · analytic continuation · order-1 growth ·
Dirichlet-series expansion · von Mangoldt-type counting at form level · codimension-2 transversality).
The paper declares the assumption itself at `:211` — the barrier is *"the **Tier-1** form … where
Tier 1 means the method class is a *named finite* toolkit T of checkable tools, rather than the open
class of all Euler-product-free derivations (that open-class form, Tier 2, is research-frontier and
not claimed here)"* — and repeats it at `:510`.

**There is a genuine closure certificate here, at a different level.** `Derives agree P x := ∀ z,
agree x z → P z` (`:263-269`) closes over arbitrary *compositions* of T's six tools by
transport-soundness. So: **certified closure for what you can build from T; assumed closure for what
belongs to T.**

### E-8 (`D:\SIDE-lv-conservation\SIDELvConservation\CompositionBarrier.lean`)

The only site that states its closure *method* and refuses enumeration on purpose (`:12-18`):

> **we do not enumerate the operations; we type their closure by what they can see.**

The certificate is `DerivesFromCriterion P M := ∀ N, diagAgree M N → P N`. Residual, which the module
itself flags under "ANTI-OVERCLAIM (load-bearing)": the closure is exact **relative to a stipulated
observable layer** inside a 2×2 model world. The assumption has not vanished; it has migrated from
the operation list to the definition of *one-variable data*, and the module says so.

### The supplier mechanism column (keystone §3, `:59-66`)

**Not used to exclude, and its non-closure is stated on the paper's face** (`:207`): *"A closed
prism-catalogue is not claimed and is not available."* Independent corroboration that the list is
open: it has grown 4 rows (v0.2) → 5 (v0.4) → 6 (v0.8, the shadow row). The one exclusion drawn in
that section (`:83`, Rodgers–Tao's zero margin excluding an everywhere-mechanism) rides a cited
theorem, not the column's completeness.

### The toy's per-object routes (D-2b, both compiled units)

Closure is a **named classification theorem**: the Type II self-dual weight enumerators of genus ≤ 5
are exactly three. Its license is itemized — Mallows–Sloane and Gleason uniqueness stipulated at
cite; the genus arithmetic (genus ≡ 1 mod 4, so genera 2, 3, 4 are empty) derived in-kernel. And the
certificate is *structurally* separated from the member checks: unit 1 closes the catalogue without
locating a single root, unit 2 certifies the members without any classification, and the joint-row
rule forbids citing either alone.

---

## §5 — THE REGISTERED EXPECTATION: CONFIRMED, WITH ONE SHARPENING THAT MATTERS

The expectation registered before the survey — *at least one invocation assumes closure without a
stated certificate; if so it files as a named work-order, not a defect claim* — **fires.** Two of
four assume closure.

**But the honest reading is sharper than the expectation anticipated, and the difference is the
finding.** Both closure-assuming sites **disclaim closure at their home cites** — Face-E names its
tier and refuses the open-class form; the supplier column states on the paper's face that no closed
catalogue is claimed or available. So the era does not contain an undisclosed closure assumption.
It contains **one place where a disclaimed assumption is glossed as though it were not**:

**THE WORK-ORDER (one clause, two occurrences).** The keystone reads Face-E beyond its tier at
`INDEX_ARITY_AT_THE_CRITICAL_LINE.md:49` — *"the whole FE-and-growth method class"* — and at `:236`
— *"the Euler-product-free toolkit"* (definite article). Both promote Tier 1 to Tier 2. The keystone
hedges globally at `:207`, so the slippage is **local, not systemic**. The repair is one clause in
each place: *the named six-tool toolkit* in place of *the whole method class*. **Named as a
work-order, riding the keystone's next touch** alongside the voice audit's two drafted moves and
D-2a's paper-sentence correction. Not landed this pass; the keystone takes cargo only on the
author's call.

**The positive result the survey also produced, which was not registered and is filed as found:**
the two certificate-stating sites close by **two different methods** — E-8 types closure by what its
operations can *see* (transport-soundness, no enumeration anywhere), the toy closes by *naming the
members* (a classification theorem). **A closure certificate need not be an enumeration.** That is a
real widening of head 1: the head has until now been read as requiring a list, and E-8 shows a
family can carry a closure certificate with no list at all, by being typed through a bottleneck
every member must pass. Filed as a note under the fifth face, at synthesis grade, forcing nothing.

---

## §6 — REFUSAL CRITERIA FOR HEADS 1, 2, 4

Head 3 already carries one (*each face must state what acts trivially on what; a face that only
asserts absence is not a face of this head*). The remaining three now match its discipline, so the
section has a standing admission test rather than an editor's judgement.

- **HEAD 1** — a face must exhibit **the enumeration AND its closure certificate**. A family
  without a closure certificate is a **catalogue, not a face**. *(Per §5, the certificate may be an
  enumeration-with-completeness or a soundness typing — but it must be exhibited, not assumed.)*
- **HEAD 2** — a face must state **which register it separates from which**, and **by what
  measurable or provable distinction**. A face that only observes that two things differ is not a
  face of this head.
- **HEAD 4** — a face must identify **what is supplied by symmetry at no cost AND what decides**.
  Naming only the free layer is the confusion the head exists to name, not an instance of it.

**Consequence, applied immediately:** under head 1's criterion, the supplier mechanism column is a
**catalogue, not a face** — which is what its own disclaimer already says, and the criterion now
makes that structural rather than editorial.

---

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `1f4ce51` → this pass's commit |
| relay | `bc0b031` → this report's commit |
| SIDE-lv-conservation | main = `14720d9` — unmoved |
| SIDE-kernel | `44895f9` — unmoved |
| rail | `de621b1` / `2147a03` — at the post-rename baseline |

W-LI face 2 still queued. D-2a's row upgrade, D-2c, and the joint rows remain the kernel leg's
open items. Keystone cargo queued, not landed — now including this pass's Face-E work-order.
Consolidation DEFERRED. Nothing deposits.
