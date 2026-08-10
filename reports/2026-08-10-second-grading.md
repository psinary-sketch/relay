# THE SECOND GRADING + STRAND 1 BANKS — 2026-08-10

**Expectations E1–E4 registered VERBATIM and committed at `61e052c` BEFORE any read.**
**Instrument: `SIDE-carrier-spec` v0.2.0 = `2051c52`. Rail `de621b1` / `2147a03` unmoved.**
**Nothing deposits.**

---

## §1 — THE GRADED ROW: THE ADELIC FRAME

Read at source in its kernel home — `SIDE-lv-conservation/SIDELvConservation/T2_SDarkness.lean`
(`T2b_mellin_exhaustion`, `T2c_phi_side_predicates_are_s_dark`) and Chapter 13 — **not from
summary.**

| field | verdict |
|:--|:--|
| `cancel`, `neg` | **PASSES** — a group with signed structure |
| `finPart` | **PASSES**, richer than the ladder's |
| **`arch_independent`** | **PASSES — compiled witness.** The product formula constrains only the **principal** elements sitting diagonally inside the group, not the ambient group |
| `components_faithful` | **AMBIGUOUS — the instrument's fault**, see §3 |
| `act` | **FAILS** — the idele class action is translation; decided mechanically |
| `pair` | **FAILS** — no pairing present at all |

**E1 CONFIRMED**, witness compiled (`frame_shape_arch_independent`), with the exclusivity also
compiled (`arch_independent_excludes_factoring`).

**E2 CONFIRMED, with two reasons kept apart.** The frame **fails `pair` on presence** — that is
the field verdict. **The s-dark seal is a second, independent reason:**
`T2c_phi_side_predicates_are_s_dark` says a Φ-side predicate cannot select among values of `s`,
so a pairing written there **would not separate by zero location even if supplied.** *Compiled in
`SIDE-lv-conservation`, cited here, deliberately NOT re-compiled in the specification, and the
two reasons recorded separately rather than merged.*

**E3 CONFIRMED, decided mechanically** — and recorded without satisfaction, since it puts the
corpus's own frame exactly where Connes' sits. **E4 CONFIRMED.**

---

## §2 — THE COMPLEMENTARITY HYPOTHESIS DID NOT SURVIVE

**On trial:** *finite structure without freedom (ladder) · freedom without pairing (frame) — so
the absence is the JOIN.*

> **REFUTED, AND THE REFUTATION IS COMPILED.** `frame_shape_has_both`: **one object has the
> finite component group fully realised AND the archimedean coordinate independent.** No tension
> between `Δ1` and finite structure for a join to resolve.
>
> **The two rows are not complementary — they are STRICTLY ORDERED.** The frame passes everything
> the ladder passes and one field more. **The ladder is not the frame's complement; it is its
> DEGENERATION** — the product-formula locus sitting diagonally inside it, where the free
> archimedean coordinate has been collapsed onto the finite data.

### THE DELTA RE-PRICES

| # | item | state |
|--:|:--|:--|
| **Δ1** | archimedean independence | **DISCHARGED** — a known object has it, compiled |
| **Δ2** | a bilinear pairing target | **STANDS — now the concentrated absence** |
| **Δ3** | sign / torsion carriage | **STANDS**, significance at question grade |
| **Δ4** | **an ARITHMETICALLY MEANINGFUL endomorphism action** | **NEW.** Both canonical objects act by **translations**; power maps pass abstractly in both and carry no arithmetic. The ladder's `SPLIT` had concealed this; the frame's clean failure exposes it |

---

## §3 — FOUND-BEYOND-REGISTRATION *(NOT EMPTY — two items)*

1. **A THIRD INSTRUMENT DEFECT: `finPart`'s CODOMAIN IS UNCONSTRAINED, SO A CANDIDATE CAN CHOOSE
   ITS OWN VERDICT.** For the frame, `components_faithful` **fails** if `finPart` is the valuation
   vector (roots of unity in `ℤ_p^×` have trivial valuation *and* trivial archimedean absolute
   value) and **passes** if it is the full finite idele class. **The specification does not fix
   which.** Found by grading, not by inspection — as the first two were. **LEFT UNREPAIRED**, per
   the standing ruling that a field correction is author-ruled, and per the stopping rule below.
2. **THE LADDER IS INSIDE THE FRAME.** Not registered, not sought. **The two gradings were never
   independent tests, and the apparent complementarity was an artifact of grading a thing and
   then grading the thing it sits inside.**

---

## §4 — STRAND 1 BANKS

**Banked:** spec `v0.2.0` (twenty terminals, none outside the clean profile) · two graded rows ·
the re-priced delta · the survey's closed record with its one **DECLARED OMISSION** · four
question-grade filings · **three instrument defects, all found by grading and none by inspection.**

> ### **STATE: SPECIFIED. UNGRADED CANDIDATES EXHAUSTED IN-CORPUS. NEXT ACT IS CONSTRUCTION — research-reach, author-ruled, NOT to be manufactured.**

**THE META-WORK STOPPING RULE IS IN FORCE: no further specification refinement without a
candidate that forces it.** The third defect is filed and left standing *under* that rule. Two of
three defects were found by grading and none by staring at the specification — **that is the
evidence for the rule, and it is why the rule now binds.**

---

## §5 — THE BRAID ROTATES *(presented for the author's ruling; NO recommendation ranked, per the order)*

| | option | scope and state |
|:--|:--|:--|
| **(a)** | **STRAND 3's named debt** — the five-path *"independent"* correction at its in-corpus sites | **bounded**; unblocks the publishable reduction. **The deposited-surface instance stays parked behind the posture clause** |
| **(b)** | **STRAND 2's registered experiment** — the second census object (non-principal classes of −23) | **the power clause is owed before any compute**, and is unrun |
| **(c)** | **The constant's background law** — why 10.14 vs 5.9 | registered, unrun |
| **(d)** | **Rest**, with everything banked | pins clean, mirror verified, nothing outstanding that decays |

**No ranking is offered and none is implied by the order above, which is the order received.**

---

## §6 — STOP-AND-HOLD

**No progress on the clause and none claimed.** This pass **discharged one delta item, refuted
the hypothesis it was asked to test, added a delta item, and exposed a third defect in the
instrument** — all four are statements about known objects or about the instrument. **`Δ2` is
untouched and is the whole of the absence.**

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `61e052c` (registration, pre-read) → this pass's commit |
| relay | `84aca14` → this report's commit |
| **`SIDE-carrier-spec`** | **tag `v0.2.0` = `2051c52` unmoved; head advances with this grading; PRIVATE** |
| **rail `de621b1` / `2147a03`** | **UNMOVED** |

**Nothing deposits.**
