# -*- coding: utf-8 -*-
"""b257 COMPONENT 1 -- write the eight TECHNE-Core module drafts + INDEX.

### b158's RULE, WHICH THIS FILE EXISTS TO OBEY: **WRITE SCRIPT FILES, NOT SHELL STRINGS.**
### Two heredoc attempts at this content died on quoting before this file was written.
### ### **TECHNE-Core IS PRIVATE AND LOCAL-ONLY. ### THIS TOOL WRITES; IT DOES NOT PUSH.**
"""
import io
import os

M = r'D:\MY-DOwnloads\TECHNE-Core\modules\2026-08'

HDR = ("*TECHNE module draft \u00b7 extracted 2026-08-29 (research seat, b257) \u00b7 "
       "**PRIVATE, TECHNE-Core, local-only**. Owning-act citations are to the `relay` record. "
       "**Grade-honest: a module states the grade its owning act carries and confers none.** "
       "Nothing deposits.*\n\n---\n\n")

SIGNEDNESS_BLOCK = u"""SIGNEDNESS (S\u00b7I\u00b7D\u00b7E+S) \u2014 TECHNE module, canonical draft
(conversation layer 2026-08-29, author-ratified on paste).
PURPOSE: formulaic discernment of sign structure in a measured
or derived family. S \u2014 SYMMETRY: classify the quantity's sign
behavior under the family's own symmetries (parity, F-sectors,
s \u2194 1\u2212s). I \u2014 INDEPENDENCE: the tautology control as
primitive \u2014 FORCED sign (holds on arbitrary inputs; algebraic;
testifies to nothing) vs EARNED sign (holds only on the
operator; content); reference implementation: b254's
two-halves control. D \u2014 DETERMINATION: locate the sign's owner
and grade (measured-only \u2192 envelope \u2192 derivation \u2192 compiled),
upgraded only via discriminators registered before the number.
E \u2014 EXHAUSTIVENESS: sign-event sweeps across cells/
realizations/axes with positive controls; every no-sign-event
claim carries its STRUCTURAL reason, not just the absence.
+S \u2014 CLOSURE: Ostrowski-style domain-closure standing \u2014 is the
signedness stable under the completions the domain admits
(level limit, \u03b5-limit, field closure)? OUTPUT: a Signedness
Certificate \u2014 forced/earned \u00b7 owner \u00b7 grade \u00b7 closure status.
CLIENTS IN CORPUS: the balance profile (b254/b255), the crown
act's \u03bb_n \u2265 0, Weil positivity, the DESI w = \u22121 commitment,
and Loci's Ratchet \u2014 subsumed as the module's monotone special
case (a ratchet = earned one-signedness along an axis + a
no-sign-event certificate)."""

FILES = {}

FILES['SIGNEDNESS.md'] = u"""# SIGNEDNESS (S\u00b7I\u00b7D\u00b7E+S)

""" + HDR + u"""## Provenance

**The author's conversation-layer draft, 2026-08-29, author-ratified on paste.** It is reproduced
**verbatim** below. b256 recorded this quotation as **OWED**; b257 pays it by citation, and b256 is
not rewritten.

## The canonical draft \u2014 verbatim

```
""" + SIGNEDNESS_BLOCK + u"""
```

---

## Notes on the client list \u2014 checked by b256, recorded beside the text, not edited into it

The author's text stands as written. These are the research seat's checks against the corpus:

| client | status at check |
|:--|:--|
| the balance profile (b254/b255) | **live** \u2014 this seat's own banks |
| Weil positivity | **live** \u2014 `BALANCE_AND_POSITIVITY`, the explicit-formula family |
| Loci's Ratchet | real, but in `archive/2026-08-27-trim-backfill/PAPER_021_LOCIS_CRITICAL_RATCHET.md`, **no live REGISTRY row** |
| DESI `w = \u22121` | real \u2014 14 documents on a word-boundary match, **all in `archive/`** |
| the crown act's `\u03bb_n \u2265 0` | ### **UNCONFIRMED AT THE ONE DOCUMENT READ.** `reports/2026-08-24-crown-opening.md` carries `\u03bb_n` as a **divisor** \u2014 *"every route the record has tried goes through `(1/\u03bb_n)\u222bK`"* \u2014 not as a stated positivity. **Not found where this seat looked; that is not the same as absent.** |

### **Two of the five clients live in `archive/`, not in live keystone rows.** An extraction routing
them onward is routing from the archive, and that is said rather than discovered later.

## The I limb's reference implementation, at content

b254's two-halves control is the module's own worked example, and it is the reason the **I** limb is
primitive rather than decorative:

- **FORCED half** \u2014 the composition `L \u2212 R = (E2 \u2212 \u0394\u208b) + (PR \u2212 \u0398_q)` holds on
  **arbitrary inputs**; it is algebraic restatement and testifies to nothing. b254 labelled it so
  **before** the run.
- **EARNED half** \u2014 the residual's *sign* takes **both** values on arbitrary inputs, so
  *"uniformly negative at twelve entries"* is a property of the **operator**, not of the formula.

### **A control carrying only the forced half would establish that the act proved nothing, without
establishing that anything it did claim has content.**
"""

FILES['BANKED_MEANINGS_ENGINE.md'] = u"""# The banked-meanings engine

""" + HDR + u"""## The rule

**Every branch, band and threshold is written and hashed before any number exists.** The run
selects a branch; it does not author one.

## The two limbs

1. **HASH** \u2014 the meanings file is emitted by a deterministic tool and its `sha256` and byte count
   are banked in the registration. The run may not alter it; the hash is re-checked at the gates.
2. **TIMESTAMP** \u2014 the order on disk is `meanings \u2192 registration \u2192 run \u2192 verdict`, and a gate
   asserts that ordering by `mtime`.

### **Neither limb alone is the engine.** A hash without an ordering proves the file is unchanged
but not that it preceded the numbers; an ordering without a hash proves precedence but not
immutability.

## The order-of-operations law

### **A file that must precede the numbers is written by a tool that computes no numbers.**

b255 is the strict case: the ladder had to be chosen by *affordability*, so the **pricing tool
computed costs only and kept no balance value** \u2014 timing and matrix sizes, every result bound to
`_`. A gate then confirmed the pricing bank carries none of the words a balance would need.
### **The order on disk is what makes "chosen by cost, not by values" checkable rather than
asserted.**

## Owning acts

- **b238** \u2014 the discriminator registered *before* measuring, so a refutation *"cannot later be
  dressed as a"* prediction. The registered half-order edge hypothesis was refuted, as registered.
- **b240** \u2014 the first face-off: meanings banked before the columns were computed.
- **b245** \u2014 the precedent that makes the hash load-bearing: a banned stem was found **inside the
  hash-gated meanings file**, and the whole chain was re-emitted and re-run to prove exactly three
  changed lines. ### **A meanings file edited after a number is seen is not a meanings file.**
- b251, b252, b254, b255 \u2014 the engine in routine use.

## What it costs, and why that is the point

b254's registered *"real finding"* was conditioned on the two `\u0394\u208b` realizations **flipping**
the branch. They did not. ### **The condition was not met, so the claim was not made** \u2014 the
engine's value is precisely that it makes an unfired condition visible instead of quietly reachable.
"""

FILES['IMPORT_LEDGER.md'] = u"""# The import ledger

""" + HDR + u"""## The rule

**Every classical fact is either reproduced longhand or named as an import and graded. There is no
third category.**

## The grades

| grade | meaning |
|:--|:--|
| `DERIVES` | reproduced longhand in the act, zero imports |
| `DERIVES-on-IMP` | derived, resting on named imports |
| `TRUSTED-AT-CITE` | named with its source, not reproduced |
| `VERIFIED-WHERE-TOOLED` | a tool checked it \u2014 **and the tool is named** |

## The verification column

Every import carries a column saying whether a tool verified it. ### **The phrase
"verified-where-tooled" may not do silent work.**

b250 is the worked case. Its theorem rests on four imports \u2014 Plancherel, the identity theorem,
Schmidt/Eckart\u2013Young, Mercer \u2014 and the act **looked for the tool and there was none**: the
residence tree carries no Mathlib. That was established twice, independently: a filesystem search,
and then `Nat.factorial` failing to resolve when the shadow compiled. ### **So all four are
TRUSTED-AT-CITE and NONE is verified, and the act says "not tooled" four times rather than glossing
it once.**

## The import count is a result, not a footnote

b250 registered a best-case target of **zero imports** and did not meet it. ### **The shortfall is
four textbook theorems, named \u2014 and the act reports the target as missed rather than redefining
the target.** Its S1 step was registered as "DERIVES, longhand and on zero imports"; the longhand
was there and the zero was not, and **the prediction is reported wrong rather than redefined.**

## Owning acts

- **b232 / b233** \u2014 the verification column and the prints-are-the-verdict law (b227's `sorryAx`
  fall-through; b231's eight axiom-bearing terminals).
- **b247** \u2014 the import bar as stated: every external fact named with its sourcing, explicit.
- **b250** \u2014 the four-import ledger and the twice-verified absence of a tool.
"""

FILES['HARNESS_LORE.md'] = u"""# Harness lore

""" + HDR + u"""*Each line is a rule, and each rule is a scar. The incident is cited because a rule
without its incident is a preference.*

## 1. A must-fail fixture must fail for a **structurally different reason**

A fixture that is the negation of its own check asserts nothing.

- **b244** \u2014 gate 2's fixture was *the exact negation of its own check* \u2014 decorative. Replaced
  with a comparison against a real file's stripped code.

## 2. Pure conjunctions only

- **b251** \u2014 gate 4 read `(A and B and C and D) or E`, and `and` binds tighter than `or`, so a
  true `E` carried the whole thing. ### **A gate that passes on one disjunct asserts only that
  disjunct.**
- **b255** \u2014 two gates carried *negated* conjuncts demanding the **absence** of phrases the files
  legitimately contain. ### **Negation does not make a vacuous conjunct meaningful.**

## 3. The tautology control

**An identity that cannot fail cannot testify.** Every decomposition is tested on arbitrary inputs;
if it holds there, it is ALGEBRAIC-RESTATEMENT and carries no weight \u2014 and the act says so
*before* the run, not after the gate catches it.

- **b246** \u2014 the tautology gate caught a **sign error in that act's own definitions file**.
- **b251 / b254** \u2014 the two-halves form: the restatement half *and* the content half.

## 4. Positive controls on absences

**An absence reported by an untested matcher is a silence, not a finding.** Show the matcher finding
something before trusting it to find nothing.

- **b248** \u2014 gate 6 showed a sentence *findable* in the registration so its absence from the bank
  meant something.
- **b256** \u2014 SIGNEDNESS was shown present **only** in that act's own files, so the absence was
  real rather than a failure to look.

## 5. A matcher must read code, not prose \u2014 and not itself

The recurring family, in four variants:

- **b242** \u2014 forced into an `ast` comment/docstring stripper.
- **b248** \u2014 a scope check matched `left_side` **inside a comment**, at its fourth matcher,
  written without the stripper b242 had been forced into.
- **b253** \u2014 a matcher hit an owner's name **inside a data string** \u2014 a correspondence cell
  quoting it as prose. ### **The fix tested what the rule means (imports and calls), not mentions.**
- **b258** \u2014 a matcher searched a file for a regex whose **literal text sat in that same file**,
  and **matched its own pattern definition.** Fixed by testing import lines, which cannot self-match.

## 6. QUOTED-N

**Any quoted partial sum carries its `N` and its precision, or it is UNGRADED.**

- **b253** \u2014 the law, minted. b251's `\u0394_2real` became quotable only as
  `(N = 11, float64 modes, suspect above n = 6)`. ### **The law governs future quotation, not past
  verdicts.**

## 7. Provenance-stamped absences

A "not found" carries **where you looked**. b256's `\u03bb_n \u2265 0` check names the single document
read, so the absence is bounded rather than global.

## 8. The unauthenticated-probe rule

**A privacy premise is checked by an unauthenticated probe, not taken on report.**

- **b257** \u2014 the seat re-ran the navigator's probes rather than accepting them: `PLACE-papers`
  404, `TECHNE-Core` 404 \u2014 ### **and found, unbidden, that `relay` and `SIDE-global-section`
  answer 200.**
- **b258** \u2014 the probes were **not** re-run, by instruction, and the prior verdict was cited.
  ### **A gate that banned the string `HTTP nnn` could not tell citing from running; the criterion
  moved from the prose to the act.**

## 9. ### A guard minted after an incident audits the past it was minted against

**b258's finding.** The pre-push hook's clause (iv) was minted 2026-08-23 *"on b126's finding that
six of these sit UNTRACKED in the working tree where a single `git add -A` would carry them onto
main."* ### **b258 measured it: six of them were already on public `main`, put there by `df2f54d`
on 2026-08-18 \u2014 five days before the clause existed.**

### **So the first duty of a new guard is to audit the history it was written against.** A guard
that only looks forward will describe as a risk what is already a fact.

## 10. ### Closed-by-default disclosure: enumerations private, counts public

**b258's rule, fixed at registration before the sweep ran.** `relay` is public; an enumeration of
patent-object SHAs and file lists is disclosure-adjacent. ### **An act that measured an exposure
risk by creating one would be a joke.**

- **The enumeration** \u2014 per-commit SHAs, file lists, the cited-commit list \u2014 goes to the
  **private** tree.
- **The public bank** carries **counts, method, reconciliation and a pointer.** Counts are not
  disclosure; a file list of patent objects is.
- ### **The rule is fixed BEFORE the sweep, so the act defaults to the closed side before it knows
  what it will find** \u2014 and a gate then checks the SHA list is *absent* from the public bank and
  *present* in the private one.
"""

FILES['DISCRIMINATOR_PROTOCOL.md'] = u"""# The discriminator protocol

""" + HDR + u"""## The rule

### **A discriminator is registered before the number, or it is not a discriminator.**

A test proposed after the measurement can always be chosen to fit it. Registration in advance is
what converts a test into evidence.

## The form

1. State the question so that **two named outcomes are possible**.
2. State **what each outcome would mean**, before either is seen.
3. State the **falsifier** \u2014 the observation that would make the registering seat wrong.
4. Bank it, hashed and timestamped (see `BANKED_MEANINGS_ENGINE.md`).
5. Report the outcome **in the banked words**, including when the falsifier fires.

## The worked case \u2014 b247's A-2

b247 faced two candidate objects and had to say, in advance, what would distinguish them.
### **A-2 was registered as a double-name hazard before any measurement: two names for what might
be one object, or one name for what are two.** The ruling that followed \u2014 `\u03b1` and
`\u03be_n(1)` are **(DOUBLE-NAME)** \u2014 is load-bearing precisely because the criterion predated the
comparison.

The species recurred at b250 (the two functionals), b251 (the envelope refused for the wrong
series), and b252 (`t(n)` versus `tr[n]`). ### **Each refusal was possible only because b247 had
registered what the distinction would look like.**

## Honesty conditions

- **A falsifier that does not fire is not a prediction confirmed.** b255's falsifier asked only
  whether the residual decreased across the new cells; it did, ### **while the registered
  expectation was still backwards about which stretch was clean** \u2014 and the act reported both.
- **A halt predicted in advance is evidence; a halt discovered and then declared expected is
  nothing.** (b250's S3(a).)
- **An expectation inferred rather than stated is marked INFERRED** when it is attributed to another
  seat.
"""

FILES['FACE_OFF_PROTOCOL.md'] = u"""# The face-off protocol

""" + HDR + u"""## The shape

A face-off computes two sides of a stated identity at a bench and asks what accounts for their
difference. ### **It is a measurement, not a verdict on the identity.**

## The order, and it is not negotiable

1. **MEANINGS FIRST** \u2014 branches, bands and the indictment order banked and hashed before any
   number. See `BANKED_MEANINGS_ENGINE.md`.
2. **THE INDICTMENT ORDER** \u2014 the suspects listed in advance, so the run cannot reorder them once
   a number is seen. ### **The form of the identity is listed LAST, always.**
3. **THE SIDES** \u2014 computed under the standing rulings, each term from **its own owner**,
   imported as a module and never re-implemented (`G-INDEP`, structural rather than asserted).
4. **THE BARS** \u2014 `G-STAB` across registered axes plus a fixed number of refinements.
5. **THE BRANCH** \u2014 selected by the banked criteria, reported in the banked words.

## The arc, b240\u2013b255

| act | branch | what it settled |
|:--|:--|:--|
| **b240** | first face-off at bench | the columns computed together for the first time |
| **b245** | (DISSONANT-BEYOND) | the ruled combination computed; the T-E mis-specification caught |
| **b251** | (IMPOSTER-NAMED) | `resid47` re-attributed: **it was never a residue** |
| **b254** | (IMBALANCED) | the two-term balance, under both `\u0394\u208b` realizations |
| **b255** | (MIXED) | the profile along the cutoff axis, sixteen cells |

## The standing prohibitions

- ### **A bench result is not evidence against the identity.** b15 governs: a finite-place-set
  object at a finite cutoff decides **nothing global**. No act has produced evidence against
  `T + Q = W_\u221e \u2212 W_primes`, and citing a face-off's branch as any would be a misreading.
- **No deficit language** where a ruling has said the residue is an artefact of the pairing.
- **A banked branch is not re-verdicted because a later act explains it** (b246's rule). b252 showed
  b251's inputs were partly noise; **b251's branch still stands as banked**, and the fact is filed.
- **An executor does not settle a definition** (b237). Where two constructions compete, **compute
  both and choose neither** (b246), and route the choice.
"""

FILES['DECISION_CARD_FORMAT.md'] = u"""# The decision-card format

""" + HDR + u"""## What a card is

A card is the smallest artefact that lets an author rule without re-deriving the act. ### **It
presents a decision; it does not take one.**

## The four fields

| field | content |
|:--|:--|
| **OPTIONS** | the named alternatives, mutually exclusive, each stated in the words its own owner uses |
| **STAKES** | what changes downstream under each option \u2014 stated symmetrically, and *before* any preference |
| **FACTS** | what is measured or quoted, with owners and grades; **no fact is stated that the act did not establish** |
| **ONE-LINE RULE** | the single sentence the author can strike or ratify |

## The standing conditions

- ### **A card is assembled only when the texts ask for one.** b248's card was conditional on a
  reading the owners did not force, and **no card was manufactured** \u2014 *an executor does not
  manufacture a card for a ruling the texts did not ask for.*
- ### **The disclosed consequence goes in the STAKES field before the verdict is drafted, never
  after.** b248 banked, before drafting, that one reading would have cut the shortfall by 45\u201350%,
  **and banked its own draft verdict in the same file.** Reporting a verdict against the direction
  of a named crime is the easy half; banking the draft first is the hard half.
- **When the executor cannot choose, the card says so and halts.** b253's R-label match was
  **halted as ambiguous and routed**, with both candidate readings quoted and **what turns on the
  difference** stated \u2014 under one reading the numbers are a deficit owed, under the other the
  residue of a pairing error.

## What a card may never do

Confer a grade. Promote a candidate. Resolve a divergence it was written to expose. Present the
executor's preference as a fact.
"""

FILES['RENDER_AS_E0.md'] = u"""# Render-as-E0 \u2014 drawing at scale as a specification check

""" + HDR + u"""## The rule

### **Drawing a specification at scale is a check on the specification, not an illustration of it.**

A figure forces every quantity the text left implicit: counts, targets, which line carries what. A
specification that cannot be drawn without inventing a value has an underdetermined clause, and the
drawing is what surfaces it.

## The worked case \u2014 Q-2 (patent seat, 2026-08-29)

Drawing P-ZONE's encoder circuit as filed produced this, recorded in the patent seat's own
`exports/2026-08-29/SEALE-PZONE-2026/NEW_MATTER_TRACE.md`:

> **Q-2 SHARPENED THIS ACT.** Six CNOTs cannot fully implement three weight-4 generators \u2014
> each would need three, so nine. **The filed count and the filed generators are not
> jointly satisfiable**, and under the drawn reading **the eighth qubit line carries no
> gate at all**, which is visible on the sheet. Drawn as filed and referred, not corrected.

### **The find is a joint-unsatisfiability of two separately-filed facts, and only the drawing
exposed it.** Both are filed verbatim; neither is wrong alone.

**Q-2 was promoted to item six of the counsel list by author ruling** \u2014 `COUNSEL_ITEMS.md`,
patent seat, maintained from 2026-08-29.

## The discipline the case demonstrates

- ### **Drawn as filed and referred, not corrected.** The drawing does not repair the
  specification; it makes the question visible and routes it.
- **New matter is traced.** Every drawn element is marked FILED / ROUTED / ILLUSTRATOR, so what the
  figure adds beyond the filing is legible rather than smuggled.
- **The illustrator's own additions carry a class of their own**, distinct from filed content.

*Cross-seat citation. This module records the method; the patent seat owns the artefacts, and the
research seat did not write them.*
"""

FILES['INDEX.md'] = u"""# modules/2026-08 \u2014 index

""" + HDR + u"""## The month's extraction

Eight module drafts, extracted 2026-08-29 from the b234\u2013b255 arc plus the cross-seat Q-2 find.

| module | what it fixes | owning acts |
|:--|:--|:--|
| `SIGNEDNESS.md` | sign structure, formulaically discerned | author's draft 2026-08-29; b254/b255 |
| `BANKED_MEANINGS_ENGINE.md` | meanings hashed before numbers | b238, b240, b245, b251\u2013b255 |
| `IMPORT_LEDGER.md` | every classical fact named and graded | b232, b233, b247, b250 |
| `HARNESS_LORE.md` | ten rules, each with its incident | b227, b242, b244, b246, b248, b251, b253, b255, b256, b258 |
| `DISCRIMINATOR_PROTOCOL.md` | registered before the number | b247 (A-2), b250, b255 |
| `FACE_OFF_PROTOCOL.md` | meanings-first; indictment order | b240\u2013b255 |
| `DECISION_CARD_FORMAT.md` | options / stakes / facts / one-line rule | b244, b248, b253 |
| `RENDER_AS_E0.md` | drawing at scale as a spec check | patent seat, Q-2, 2026-08-29 |

---

## Provisional relevance \u2014 **stated as AIM. No claim language is drafted here.**

> ### **This table records where a module might bear, if results hold. It is not a claim, not a
> filing position, and confers nothing.** Claim language is counsel's and the author's.

| module | relevance | grade of the relevance |
|:--|:--|:--|
| `BANKED_MEANINGS_ENGINE.md` | **PROV-1 / PROV-2 continuation** \u2014 a verification-process limb | **AIM** |
| `HARNESS_LORE.md` | **PROV-1 / PROV-2 continuation** \u2014 the gate architecture | **AIM** |
| `IMPORT_LEDGER.md` | **TECHNE umbrella** \u2014 provenance grading | **AIM** |
| `DISCRIMINATOR_PROTOCOL.md` | **PROV-TECHNE-2 candidate** | **AIM** |
| `FACE_OFF_PROTOCOL.md` | **PROV-TECHNE-2 candidate** | **AIM** |
| `SIGNEDNESS.md` | **PROV-TECHNE-2 candidate** \u2014 certificate output shape | **AIM** |
| `DECISION_CARD_FORMAT.md` | **TECHNE umbrella** | **AIM** |
| `RENDER_AS_E0.md` | **continuation material**, cross-seat; the artefacts are the patent seat's | **AIM** |

### Standing conditions on this index

- ### **No module confers a grade on the results it cites.** Each states the grade its owning act
  already carries.
- ### **TECHNE-Core is PRIVATE and was NOT pushed by the act that wrote these files.** Local-only.
- **Two of `SIGNEDNESS.md`'s named clients live in `archive/`, and one was unconfirmed at the single
  document checked** \u2014 recorded in that module beside the author's text, which is not edited.
- **The two-clone divergence stands unresolved:** this is `TECHNE-Core` (`22739c9`); a second clone
  `TECHNE_Core` (`6e8638a`) shares the root commit `065ccfd` but has diverged. **Reported at b257,
  not resolved.**
"""


def main():
    for name, body in FILES.items():
        io.open(os.path.join(M, name), 'w', encoding='utf-8', newline='\n').write(body)
        print("  written: %-30s %6d bytes" % (name, len(body.encode('utf-8'))))
    print("\nmodules in %s: %d" % (M, len(os.listdir(M))))


if __name__ == '__main__':
    main()
