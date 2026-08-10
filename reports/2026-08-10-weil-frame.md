# THE THIRD GRADING — THE WEIL-EQUIPPED FRAME — 2026-08-10

**Expectations registered verbatim at `67b168d` BEFORE any read. Grading only; construction
refused. Instrument `v0.3.0` = `89e574d`. Rail `de621b1` / `2147a03` unmoved. Nothing deposits.**

---

## §1 — THE OBJECT AT CITE

**Weil 1952:** RH ⟺ **positive-definiteness of a generalized function arising from the explicit
formula**; and *"for curves over finite fields the corresponding positive-definiteness DOES hold
… Over ℚ, the same criterion is exactly what is open."*

**The form, as the corpus states it:** *"for an even test function `g` with `h` its Fourier
partner … RH is equivalent to the positivity of the left side **for every admissible `g` of the
form `f ⋆ f̃`**."*

**Term census at cite (`F.2026-07-09-a`): six definite, C₂ indefinite.**

---

## §2 — THE IDENTIFICATION, VERIFIED AT CONTENT — **AND IT FAILS**

> ### **THE WEIL FORM IS A PAIRING ON TEST FUNCTIONS, NOT ON CLASSES.**
>
> The criterion quantifies **over functions `f`**; the classes appear only as the variable those
> functions are defined on. **The field is `pair : C → C → P`, on the CLASS OBJECT. A function
> space over an object is not that object.**

| | **A** — `C` = idele classes | **B** — `C` = the test-function space |
|:--|:--|:--|
| `pair` | **FAILS** | **PASSES as target** |
| `arch_independent` | **PASSES** (inherited) | **DOES NOT INHERIT** — no product shape; **not stateable** |
| `finPart` / `archPart` | pass | **unstateable** |
| `act` (R4) | fails (translation) | **PASSES** — the regular representation is **linear in `f`** |
| `arith_action` (Δ4) | **FAILS** | **FAILS**, for a different reason: no Frobenius-lift structure |

> **THE ROOT: the specification grades OBJECTS; the candidate is a form on a space OVER an
> object. The fields that pass and the fields that fail sit on different levels, and no single
> row is available.**

### THE NAME-IDENTITY CHECK FIRES AT THE SHARPEST PLACE IT COULD

> ### **"WEIL POSITIVITY" NAMES TWO DIFFERENT FORMS, AND THE CORPUS HOLDS BOTH**
>
> **(i)** the **explicit-formula** form, on **test functions** (Weil 1952 — this candidate);
> **(ii)** the **Rosati / intersection** form `σ(f·f′) > 0` on **`End(Jac C)`**, i.e. on **classes**
> (Weil 1948 — `F.2026-08-09-c`).
>
> **The `pair` field was written for (ii); the candidate offered is (i).** Over function fields
> they coincide in consequence — **which is why the name is shared, and exactly why the shared
> name is not evidence.**

**E1 REFUTED under B** (inheritance does not carry when the class object changes) · **E2 SPLIT,
and the split is the finding** · **E3 CONFIRMED as verdict, CORRECTED as to reason** (under B the
action is *linear*, not a translation) · **E4 CONFIRMED** — and the reason restated: **the Weil
form's definiteness IS RH, and is therefore precisely what the field must not ask for.**

---

## §3 — FOUND-BEYOND *(two)*

1. **THE SPECIFICATION HAS NO LEVEL FIELD.** It says what structure a carrier must have and
   cannot say **at what level the pairing lives**. **Three gradings, three defects — but this one
   is not a wrong field, it is a MISSING KIND of field.** **Left unrepaired:** reading B is an
   artifact of this grading, not a proposal, so **no candidate forces it and the stopping rule
   governs.**
2. **THE `Δ4`-vs-`(R4)` GAP IS WIDER THAN THE SECOND GRADING SHOWED.** There `(R4)` passed
   *vacuously*; here it passes for a **substantive** reason and `Δ4` still fails. **`Δ4` is
   independent of the reason `(R4)` passes** — which the power-map counterexample alone did not
   establish.

---

## §4 — `F.2026-08-10-m` — THE CONCENTRATION *(coordinate grade)*

| delta | held by | lacking |
|:--|:--|:--|
| **Δ4** | `W(ℤ)` | any archimedean coordinate |
| **Δ1** | the adelic frame | any Frobenius-lift structure |
| **Δ2** | the Weil form — **one level up** | a level-correct home |

> ### **THE COORDINATE: AN ARITHMETIC (FROBENIUS-LIFT-TYPE) ACTION AT THE ARCHIMEDEAN PLACE, WHOSE TRACE CHANNEL WOULD RENDER C₂ DEFINITE.**
>
> ### **AND IT IS NOT NEW — IT IS §27.3's FIFTH REGISTER, IN THE CORPUS'S OWN WORDS:** *"no positive pairing is known … the classical programmes seeking that pairing are seeking exactly this closure."*
>
> **A CONVERGENCE, NOT A DISCOVERY.** An independent route — three gradings against a compiled
> specification — arrives where the monograph already stood. **The corpus's priority is recorded
> with it.**

**THE EQUIVALENCE CAVEAT:** the coordinate names the clause's **location**, not a path to it.
**Weil's criterion has been possessed-as-statement since 1952, and possession is not progress.**

---

## §5 — `F.2026-08-10-n` — THE SURVEY-TO-DELTA CORRESPONDENCE *(Tier N)*

**Borger holds `Δ4` · the frame holds `Δ1` · Deninger POSTULATES the join.** **The arrest map and
the delta decomposition were derived independently and agree term by term.**

> **A SOURCING CORRECTION MADE RATHER THAN GLOSSED: DENINGER IS NOT QUOTED — his text was never
> fetched.** What the corpus holds is **its own characterization** of what his postulated `H¹`
> would have to be (*"a Frobenius-flow generator whose spectrum is the ordinates, a
> Poincaré-duality polarization positive on the FE-even class … the constraint set pins every
> property except the positive polarization"*). **That is the corpus speaking about Deninger, not
> Deninger speaking.** His papers are a **declared omission** of this pass. *An abstract is not a
> source, and neither is a third party's summary — including this corpus's.*

> ### **AGREEMENT ABOUT ANATOMY, SILENCE ABOUT SURGERY.** Two independent decompositions agreeing on how the problem divides is evidence **the division is real** — and **no evidence whatever** that the pieces can be joined. **The third row is a POSTULATE, which is what the field does when it cannot construct. Everyone agrees where the seam is. No one has crossed it.**

## §6 — STOP-AND-HOLD

**Nothing constructed.** The grading returned **a negative identification and a missing field
kind**; the concentration **re-reaches a coordinate the corpus already held**. **`h2` is exactly
where it was.**

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `67b168d` (registration, pre-read) → `9464013` |
| relay | `0bbe6b5` → this report's commit |
| `SIDE-carrier-spec` | tag `v0.3.0` = `89e574d`, PRIVATE — **untouched this pass** |
| **rail `de621b1` / `2147a03`** | **UNMOVED** |

**Nothing deposits.**
