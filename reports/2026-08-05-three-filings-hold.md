# The sweep's failure modes · the h = 0 degeneration · the census dataset fixed — 2026-08-05

Pins at open: PLACE-papers `1fed4b1`; relay `c6abe04`; lv `2f71068`; kernel `5e668b4`.
Rail at `de621b1` / `2147a03`. Census undisturbed. Nothing deposits. **Hold at the close.**

---

## §1 — THE SWEEP'S FOUR FAILURE MODES, ON THE LEDGER'S FACE

| # | mode | how it was found | what it does to a count |
|:--|:--|:--|:--|
| 1 | **truncation at punctuation** | `d(K) = 2^(r₁+r₂+2` — the regex stopped at the first `)`, losing the `− 1` that makes the formula correct | flags a correct formula as unprovenanced, and shows a reader a fragment that is *false as printed* |
| 2 | **keyword-list gaps** | `ξ order ≤ 1 / genus-1 Hadamard` — the sentence records a **pin**, and "pinned" was not among the provenance words | flags provenanced material as unprovenanced |
| 3 | **proximity window narrower than the corpus's paragraphs** | both `h = ½ threshold` entries — the statement sits **five lines above**, outside a ±2-line window | flags resolvable material as unresolvable |
| 4 | **the retired occurrence proxy** | Mallows 8× / Gleason 8× / Hankel-ratio 6×, content zero — repetition read as holding | credits an unresolvable name as held; **runs backwards** |

**THIS PASS'S COUNT: four of nine closures were extractor artifacts, not gaps.**

**THE STANDING CAVEAT, which is the deliverable: the 35 and the 148 measure the EXTRACTOR as much
as the CORPUS.** Neither number is a property of the corpus alone, and neither should be quoted as
one. **No re-run is authorized** — a re-run would produce a fourth number with its own artifacts,
and the caveat is worth more than a better count. Any future use of either figure carries all four
modes with it.

---

## §2 — THE h = 0 DEGENERATION, FILED (Tier N, cross-linked, NOT promoted)

**The fact.** As h → 0 the Lagarias differenced family degenerates to the undifferenced
conductor-1 case — to ζ itself — so **the deformation route loses its parameter exactly at the
wall.** Set beside:

| pencil | parameter | where the object sits | where the good behaviour is |
|:--|:--|:--|:--|
| **h-pencil** (Lagarias differenced family) | h | at **h = 0** | on the region **\|h\| ≥ ½** (edge-free, unconditional) — *away from the object* |
| **t-pencil** (de Bruijn–Newman) | t | at **t = 0** (Λ_dBN = 0 ⟺ RH) | Λ ≥ 0 is a theorem; ζ sits at **zero margin** — *at the boundary* |
| **c-pencil** (the toy's Gleason direction) | position on the stratum | at the **extremal point** | confinement certified **exactly on the extremal stratum with exact failure off it** — *at the object* |

### Are the three one fact re-encountered, or three instances?

**THE NAMED CRITERION DOES NOT EXIST, so the question is left UNDECIDED — as instructed.**
"The knife-edge anatomy" occurs **once in the corpus**, at INDEX_ARITY §330, applied to the
h-pencil (*"a third pencil with the knife-edge anatomy"*) **with no criterion stated anywhere.**
There is nothing to decide with.

**What the nearest STATED criterion gives, marked as a substitute and not the named one.** The
two-kinds split (F.2026-08-02-b): *unconditional-geometry* (supplied everywhere, margin exists, no
selection) versus *extremal-selection* (certified exactly on the extremal stratum with exact
failure off it).

- **c-pencil → extremal-selection**, by that definition exactly.
- **t-pencil → zero margin**, which the split already pins to the selection kind (Rodgers–Tao).
- **h-pencil → NEITHER KIND AS STATED.** Its structure is certified **away from** the object, not
  at it; the split has no cell for that.

**The observation that does real work, and it argues against "one fact": THE ORIENTATIONS ARE
INVERTED.** For the c-pencil the good behaviour is **at** the knife-edge and fails off it; for the
h-pencil it is **away** from the critical value and the object sits where it is absent. On any
criterion sensitive to orientation these are not the same fact.

**So: "one fact re-encountered" is NOT supported — and "three instances" is NOT established
either**, because the criterion that would establish it is undefined. **Left undecided, with the
reason named.** Not promoted.

### The work-order this produced, filed rather than acted on

**"The knife-edge anatomy" is a term used in a keystone whose criterion is stated nowhere** — an
I-8 locality failure found in the course of trying to use it. Two options, neither taken:
**define the criterion** (and the orientation question becomes decidable), or **retire the phrase**
and describe each pencil in its own words.

---

## §3 — THE CENSUS DATASET, FIXED FOR THE EXPERIMENT

### Completed range at the next natural boundary

**312 cells banked · 44 complete rows (7 σ-cells each) · contiguous from t = 0.5 with NO GAP,
complete through t = 22.5.** σ ∈ [0.52, 1.50] in seven cells; t < 0.5 excluded (the pole of Λ at
s = 1).

### The census located the known off-line zero, blind

```
[hit] sigma[0.94,1.08] t[16.0,16.5] winding=+1.000 minmod=2.70e-12
```

**Integer winding +1.000 in exactly the box containing 0.9533 + 16.290i** — found by walking cells
in order, not by seeding at a known answer. **It is the only hit in the completed range**, so
σ ∈ [0.52, 1.50], t ∈ [0.5, 22.5] contains exactly one off-line zero of the principal form. (The
programme's other recorded disc −23 off-line zero, 0.798 + 29.55i, lies above the completed range
and has not been reached.)

### THE DATASET DECLARATION

> **The arithmetic-side validation will run against t ∈ [0.5, 20.0], σ ∈ [0.52, 1.50] — complete,
> contiguous, and FIXED.**

Chosen at a round boundary **inside** the completed range so it does not move while the census
continues past it. **It contains the located off-line zero at t ≈ 16.29**, which is the ground
truth the experiment needs. The census keeps running beyond 20.0; **the dataset does not grow with
it.**

### I-7 confirmed at both stages, before any compute is authorized

- **Stage 1 (the statistic) — PASSES.** λₙ = Σ_ρ[1 − (1−1/ρ)ⁿ] contains ρ, real parts included.
- **Stage 2 (the pipeline) — PASSES.** The computation reads Λ_Q's functional equation and Taylor
  data; **no zero location is an input at any point**, and the census above is held aside and
  never enters it.

**THE VALIDATION REMAINS PRICED AND UNRUN.** This is the dataset declaration only. Predicted
negativity depth stands at **n ≈ 7000**, stated in advance; cost order-of-days at ~10⁴ digits.

---

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `1fed4b1` → this pass's commit |
| relay | `c6abe04` → this report's commit |
| SIDE-lv-conservation | `2f71068` — unmoved |
| SIDE-kernel | `5e668b4` — unmoved |
| rail | `de621b1` / `2147a03` — unmoved |

Six unclustered work-orders stay listed and unread. Head 4 proposed, ℤ/3 condition standing.
BURIAL proposed-with-one-face, derived-twice and measured-once. Nothing deposits. **Hold.**
