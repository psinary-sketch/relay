# Three light filings: BURIAL proposed · the R4 chiasmus · the sweep clustered — 2026-08-05

Pins at open: PLACE-papers `d340532`; relay `8b9494a`; lv main `2f71068`; kernel `44895f9`.
Rail at the post-rename baseline. No compute beyond reading recorded numbers. Nothing deposits.

---

## §1 — BURIAL, PROPOSED AS A CANONICAL HEAD — and its own criterion refuses three of four faces

**The property.** Placement information about height γ sits at depth ~γ²: to learn where a zero
at height γ is, an instrument must reach a depth that grows as the square of that height.

**REFUSAL CRITERION (filed with the head, as head 3's discipline requires):** *a face must state
the height it reaches, the depth it requires, and the measured or derived relation between them;
a face asserting only "it gets harder" is refused.*

**THE REGISTERED TEST — *do the four exponents agree, or is the quadratic coincidental?* — RUN
AGAINST THE RECORDED NUMBERS, AND IT IS NOT RUNNABLE AS POSED.** Only one of the four candidate
faces has a recorded exponent. That is the finding, and it is the criterion working on its first
use rather than a defect in the proposal.

| candidate face | height reached | depth required | relation, as recorded | verdict |
|:--|:--|:--|:--|:--|
| **the Li/√n law** | γ | n ≈ (γ²/δ)·log(background) | **exponent 2, DERIVED — and twice**: from the detector's corrected depth law, and independently from Lagarias' unconditional S_fin(n) = λₙ(√n) | **ADMITTED** |
| the Lehmer shadow | the collided pair at t = −0.1 | a depth-12 meter | **a bare ratio — 54× past reach at 1.4% contrast.** No relation between the two is recorded | **REFUSED** |
| the toy's receding minor | genus g | entry minor index | *"higher genus buries the defect's entry one minor deeper"* — **linear, and in a different variable** (minor per genus, not depth per height) | **REFUSED as non-commensurable** |
| the Hankel flip-depth d(t) | pencil parameter t → 0⁻ | flip depth d(t) | *"validated at t = −5..−50, monotone toward the knife-edge, blind at reachable depth for t = −0.1, −0.3"* — **monotone, no exponent** | **REFUSED** |

**So the answer to the registered test is neither "they agree" nor "the quadratic is
coincidental": three of the four faces do not report an exponent at all, and one of those three
reports a linear law in a variable that is not height.** The comparison the test asked for cannot
be made from the recorded numbers, and re-deriving them was excluded by the registration.

**CONSEQUENCE, applied by the head's own analogy.** Head 1's criterion says a family without a
closure certificate is a catalogue, not a face. By the same standard, **BURIAL with one admissible
face is a CONJECTURE WITH ONE INSTANCE, not a head, and it is filed as proposed and NOT
PROMOTED.** What it gains from this pass is a precise work-order per refused candidate:

- **Lehmer shadow** — record the depth a meter of reach R requires, so the 54× ratio becomes a
  relation rather than a distance.
- **toy's receding minor** — express the minor index against a height-like variable, so the
  linear-in-genus law can be compared with a quadratic-in-height one, or shown not to be
  comparable at all.
- **Hankel flip-depth** — fit d(t) against t on the recorded t = −5..−50 range; the data exists
  and the exponent does not.

**The one admitted face is worth stating on its own**, because it is doubly-derived and the two
derivations are independent: the detector's law n_det = (γ²/δ)·log(threshold × background) comes
from the Cayley geometry, and Lagarias' S_fin(n) = λₙ(√n) + O(n log n) comes from the explicit
formula. **Two routes, one exponent.** That is the whole evidential basis for BURIAL at present.

---

## §2 — THE R4 CHIASMUS AND THE COST INVERSION (Tier N, method-canon candidate, NOT promoted)

### (a) The chiasmus: one property, two sides, askable and unclosable

R4 is the single open cell of the compression table, and **both facts about it — that the question
can be asked there and that it cannot be closed there — are the same property seen from opposite
sides.**

- **Certified closure makes the question POSABLE.** R4 is the only Π₁-native register: the only
  one that hands you a sequence you can index and check. Without that, "do finitely many force
  all?" has no *finitely many* to speak of. R1, R3 quantify over totalities; R2's index set is
  not computable; R5 is Σ over a function-space. **Enumerability is the precondition of the
  question.**
- **The absence of a closure certificate keeps it OPEN.** The compression bound would itself be a
  closure certificate for the λ-family — a finite check forcing an infinite statement. There is
  none, and F.2026-08-05-k showed the reduction to the arithmetic term does not supply one.

**Cross-link, and it is the same figure at a lower altitude: "the space is the wall."** There the
object that would supply the positivity is the object whose absence is the obstruction. Here the
property that makes the question askable is the property whose absence keeps it open. **Head 1 is
the common term** — certified closure is doing both jobs, which is why R4 is simultaneously the
only place to ask and no place to answer.

### (b) The cost inversion, with both numbers at cite

**R4 is the CHEAPEST SUFFICIENT and LOWEST-TYPE register, and the COSTLIEST VERIFICATION CHANNEL.**

| | reach | cost |
|:--|:--|:--|
| **Li positivity** (R4's channel) | height **γ ≈ √n**; at Johansson's n = 10⁵ that is **γ ≈ 316** — and through the corrected depth law, γ ≈ 65 at δ = 0.5 | 33 000–2 900 digits, **~10¹⁰ bits** |
| **direct zero verification** | height **~10¹³** | classical, and vastly cheaper per unit height |

**Ten orders of magnitude of reach, in favour of the channel that is logically more expensive and
computationally cheaper.** The register that is cheapest to *state* and lowest to *type* is the
one that costs the most to *check per unit of height*, and by a wide margin.

**Cross-link: the free-layer inversion, the same shape at a different altitude.** D-2 found that
the layer symmetry supplies free is *expensive* to certify — it carries its whole construction —
while the deciding layer compiles from explicit rational data. **Logical cheapness and
computational cheapness run opposite ways in both cases**, which is why the kernel-leg policy
(certify deciding layers, stipulate free layers at cite) and the verification-channel choice
(check zeros directly, hold Li positivity as a datum) are the same decision made twice.

**Method-canon candidate. NOT promoted** — it is a reading of two recorded results, and it earns
promotion only if a third instance of the inversion appears that was not constructed to fit it.

---

## §3 — THE PROVENANCE SWEEP, SORTED BY CLUSTER

Instrument: `tools/audit/sweep_clusters.py`. Clusters assigned by file, line range and keyword, so
counts are derived rather than eyeballed.

**56 flagged. 21 STRUCK as not formulas — reported first, because a work-order list that quietly
carries its own false positives is the defect it exists to catch.** 35 genuine work-orders remain.

| cluster | n | verification route |
|:--|--:|:--|
| **Li/Weil analysis block** (LOOM §2142–2183, OPEN_TRAILS §2157) | **11** | derivation-at-source (Bombieri–Lagarias; Lagarias 2007) **+ numerical check** — the Cayley/moment instruments built this week evaluate S_n and E_quad directly, so this cluster is the cheapest to close |
| **Cosmology / formation constants** | 5 | **numerical check** (the constants have measured counterparts) + dimensional check |
| **Number-field / Dedekind arithmetic** | 5 | **numerical check on small fields** + derivation-at-source |
| **Spectral-realization / Hilbert–Pólya** | 4 | derivation-at-source — each is an identification at cite, not a computed quantity |
| **Shape discriminant / era measurements** | 4 | **cite-adjacent repair only** — these ARE provenanced in relay reports; the sweep flags them because a ±2-line proximity proxy cannot see three paragraphs away |
| unclustered | 6 | read individually; no common route |

**Two corrections to the ferry's framing, both from the counts.**

**(i) The cosmology block is not the second-largest cluster.** Measured: Li/Weil 11, cosmology 5,
number-field 5. Cosmology ties for second rather than taking it, and **the largest class of all is
the 21 struck non-formulas** — the sweep's own noise, which no reading of the output should hide.

**(ii) `4/81` is restated far more than "across three documents", and its open status is recorded
once.** A direct count gives **34 line-locations across the three living ledgers** — 5 in
OPEN_TRAILS, 4 in FINDINGS, 25 in VERIFICATION_LOOM. And its status is not unrecorded: LOOM
§978–987 already says the components are *"NOT derived — pending source-paper clarification"* and
that the formula form *"is the definitional model"*, with the open question of whether the
counting justification is Lean-formalizable or *"irreducibly definitional"*.

**So the cosmology block is not a verification gap; it is a PROPAGATION gap** — the constant is
restated 34 times and its openness is recorded once, so a reader meeting any of the other 33
occurrences meets a number without its caveat. **That is the description rule's own shape**: text
true where it was written, restated where its qualification is not. Filed as such, and it changes
the work-order: the route is not "check the number" but **"carry the caveat to the restatements,
or cite §978–987 from them."**

**No defect is claimed against any of the 35. No reverification was run this pass.** The list
exists so the wave-edit and the cosmology bundle each inherit a ready work-order set with its
route named.

---

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `d340532` → this pass's commit |
| relay | `8b9494a` → this report's commit |
| SIDE-lv-conservation | main = `2f71068` — unmoved |
| SIDE-kernel | `44895f9` — unmoved; the generalization work-order still open |
| rail | `de621b1` / `2147a03` — at the post-rename baseline |

R4 registered and unrun. The census experiment priced and unrun. Consolidation DEFERRED.
Nothing deposits.
