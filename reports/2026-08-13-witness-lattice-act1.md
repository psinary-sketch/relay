# W-WITNESS-LATTICE — ACT 1: THE ENUMERATION

**Relay report · 2026-08-13 · author-called · strand 9 · QUESTION-FIT, both branches longhand**
**Consequence line: the lattice's empty cells constrain any mechanism that would decide the sign — it constructs none.**
**Corpus-first per canon XV. Every cell cited or measured. Stopped at no claimed sign result — none arose. Nothing deposits.**

---

## §0 — THE AXES, FIXED BEFORE THE POPULATION

**The rows are not this act's invention.** The grading axes are the S-table's own specs, sealed at
`phase2/method/THE_EULER_SPECIFICATION.md` v0.1 (2026-08-12), read before any object was placed:

| axis | the spec, as sealed |
|:--|:--|
| **S1** | factorization-existence — every `n > 1` factors into primes, uniquely up to order |
| **S2** | index-completeness — the places of `ℚ` are exactly one archimedean and one `p`-adic per prime |
| **S3** | analytic form + FE — `ξ` built adelically over that roster; Poisson/Mellin pipeline |
| **S4** | coefficient law — the Dirichlet coefficients are **totally multiplicative** |
| **S5** | local address structure — positions `k log p`, weights `log p · p^{−k/2}` |
| **S6** | domain of validity — the product converges **exactly** for `Re s > 1` |
| **PLACEMENT** | all-on-line / known off-line zeros / unknown |

**Grades used** (corpus vocabulary, plus one declared addition):
`COMPILED` (terminal + pin + profile) · `MEASURED` (computed at bank) · `AT-CONTENT` (quoted at cite) ·
`STANDARD-AT-TEXT` (textbook, named not fetched) · **`LIT-CITED`** (external theorem named, *not held in
corpus* — declared here because the population reaches past the corpus) · `UNKNOWN` · **`VACUOUS`**
(the spec is not stateable of this object — declared, see §3).

---

## §1 — THE POPULATION, GRADED AT CITE

`✓` present · `✗` absent · `—` vacuous · `?` unknown. **No cell is inferred.**

| # | object | S1 | S2 | S3 | S4 | S5 | S6 | PLACEMENT |
|:--|:--|:-:|:-:|:-:|:-:|:-:|:-:|:--|
| 1 | **ζ(s)** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | on-line for all `10¹³+` computed; **universal statement OPEN (`h2`)** |
| 2 | **Dirichlet `L(s,χ)`** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | all computed on-line; **GRH open** |
| 3 | **Hecke `L`** | ✓ | **?** | ✓ | **✗** | ✓ | ✓ | all computed on-line; open |
| 4 | **Automorphic `L` (Δ, Δ×Δ̃)** | ✓ | **?** | ✓ | **✗** | ✓ | ✓ | all computed on-line; open |
| 5 | **Epstein `Z_Q`, `h = 1`** | ✓ | ✓ | ✓ | **✗** | ✓ | ✓ | on-line ⟸ GRH for `ζ·L(s,χ_D)` |
| 6 | **Epstein `Z_Q`, `h > 1`** (disc `−23`, `h = 3`) | **✗** | ✓ | ✓ | **✗** | ✓ | — | ### **OFF-LINE ZEROS EXIST** |
| 7 | **Davenport–Heilbronn `f(s)`** | ✓ | ✓ | ✓ | **✗** | ✓ | — | ### **OFF-LINE ZEROS EXIST** |
| 8 | **Selberg class `S`** (all axioms) | ✓ | ? | ✓ | ✓ | ✓ | ✓ | **"Yes, by axiomatization" — NOT A WITNESS (§2.4)** |
| 9 | **Hurwitz `ζ(s,a)`**, `a` rational `≠ 1, ½` | ✓ | ✓ | ✓ | **✗** | ✓ | — | off-line — **`LIT-CITED`, not corpus-held** |
| 10 | **Partial Euler product `E_k(s)`** | ✓ | **✗** | **✗** | ✓ | ✓ | ✓ | ### **NO ZEROS AT ALL** (§3.4) |
| 11 | **Beurling generalized primes** | ? | ? | ? | ? | ? | ? | ### **ROW WHOLLY UNKNOWN — corpus-absent (§4)** |
| 12 | **Random Dirichlet series** | ✓ | ✓ | **✗** | **✗** | ✓ | — | off-line |

### The cell citations (every one)

**Rows 1–2, 12 · S1–S6 and the record.** S-table seals as above; the placement column from
`day1/Which_Structure_Confines.md` §The Complete Record (`6b18d69…`), whose rows are ζ *"Yes (10¹³+
computed)"*, Dirichlet *"Yes (all computed; GRH)"*, random Dirichlet *"No"*. **S2 is `COMPILED`** —
Ostrowski as completeness theorem, terminal `structural_exhaustiveness_proved`, SIDE-kernel
**v1.5 = `0e5233f`**, profile `{propext, Classical.choice, Quot.sound}`. **S3 is `COMPILED + DEPOSITED`**
(`Spectral_Inertness` `db5ab3d…`). **S5 is `AT-CONTENT + MEASURED`** (`BALANCE_AND_POSITIVITY` §I).

**Row 6 · the disc `−23` witness, the act's densest cell.**
*S1 `✗`* — `Which_Structure_Confines` §Epstein at cite: *"the lattice lacks unique factorization"*; *"The
ring of integers `O_K` … has unique factorization if and only if its class number is 1."*
*S2 `✓`, S3 `✓`, S5 `✓`* — `THE_EULER_SPECIFICATION` §3: same roster; *"built from `Q(m) → θ_Q → ξ_Q` by
**the same Mellin pipeline**"*; addresses `r_Q(n)` at positions `log n`.
*S5 `MEASURED`* — `r_Q = [2,0,0,2,0,4,…]`, disc `−23`, `h = 3`, **all `≥ 0`**, computed at bank
(`VERIFICATION_LOOM`, coefficient-ledger table).
*S4 `✗`* — verbatim: *"When `h > 1`, the Dirichlet series coefficients of `Z_Q` are **not multiplicative**,
so the series **does not factor into an Euler product**."*
*PLACEMENT* — theorem: Davenport–Heilbronn 1936; Voronin 1976 for the Epstein case. Pinned instance
**`ρ ≈ 0.9533 + 16.290i`, SIMPLE, doubly-sourced** (Ch. 17.3; `HELD_WONDER`). **`COMPILED` as a stipulated
cited datum:** `allOnLine .epstein = False` in `Voice7Witness.hadamard_does_not_enforce_online`,
SIDE-kernel `Kernel/Voice7Witness.lean`, **axiom-free**, pin `691295b` — *read this act at the file*.

> **THE ANTI-OVERCLAIM RIDES THE CELL, IN THE KERNEL'S OWN WORDS.** *The module states it: the off-line
> fact is a* ***"STIPULATED CITED DATUM … consumed here, never reproved."*** **The `COMPILED` grade attaches
> to the countermodel architecture, NOT to the analytic placement fact.** *Recorded so the pin is never
> read as the programme having proved Epstein's off-line zeros.*

**Row 7 · Davenport–Heilbronn.** *S3 `✓`* by construction, *S4 `✗`* — *"it is a linear combination of
L-functions"* (`Which_Structure_Confines` §Corroboration). *S5* — ledger *"sign-neutral (period-sum 0)"*
(`VERIFICATION_LOOM`). *PLACEMENT* — D–H 1936, explicit zeros Titchmarsh 1986; **`COMPILED` as stipulated
datum** `allOnLine .dh = False`, `SieveCeilingWitness.dh_witness` / `dh_sieve_ceiling`, read this act.

**Rows 3–4 · S4 `✗` is MEASURED, not assumed — see §2.2.** Placement from the Complete Record
(*"Yes (all computed)"*) and the ledger table (Δ, Δ×Δ̃ *"TRUE (GRH)"*).

**Row 5 · Epstein `h = 1`.** `THE_EULER_SPECIFICATION` §3, deposited side: *"every `ζ_Q = (w/h)·Σ_χ χ̄(A)
L_K(s,χ)` — **a combination of `h` Hecke Euler products** (`h = 1` the degenerate single term,
`ζ(s)L(s,χ_D)`)."* Placement inherits GRH for its two factors.

**Row 9 · Hurwitz.** **Corpus holds `HurwitzZetaEven` / `evenKernel` only as FE-and-order machinery**
(`OPEN_TRAILS` O.18, the C₃/C₆ discharge; the `AbstractFuncEq` route) — **never as a zero-placement
object.** The placement cell is therefore `LIT-CITED` and carries no corpus weight.

**Row 10 · partial Euler product.** **Corpus-held and measured:** `phase1.5/deep-structure/CONSTANCE.md`
defines `Eₖ(s) = ∏_{p ≤ pₖ} (1 − p⁻ˢ)⁻¹` against `Dₖ(s)` and measures both at `γ₁ ≈ 14.135` (`~70×` at
`k = 6`). *S4 `✓`* — the coefficient stream is the indicator of `pₖ`-smooth `n`, totally multiplicative.
*PLACEMENT* — a **finite** product of factors `(1 − p⁻ˢ)⁻¹`, each nowhere zero: `STANDARD-AT-TEXT`.

---

## §2 — THE REGISTERED EXPECTATIONS, BOTH BRANCHES

### 2.1 — (E1) CONFIRMED, with **three** corpus-held witnesses and one at literature

**Every located object with off-line zeros fails `S4`.** Rows 6, 7, 12 — corpus-held, each at cite, two of
them carrying compiled countermodel terminals. Row 9 agrees at `LIT-CITED` and is **not counted**.

> ### **N = 3 IN-CORPUS, NOT ONE. The localization is carried by three independent constructions —
> a lattice with `h > 1`, an engineered character combination, and a random series — that share no
> machinery beyond the missing coefficient law.**

**The honest deduction of that count:** the corpus's Complete Record lists seven classes, but four of them
(ζ, Dirichlet, Hecke, automorphic) are on-line rows and carry E1 vacuously. **Only three rows are located
off-line, and all three fail `S4`.** No row is off-line with `S4` present.

### 2.2 — (E2) DID NOT FIRE — **but the search found a defect in the spec it was testing**

**No object in the population has `S4` and off-line zeros.** The registered refutation did not occur.

**FOUND-BEYOND-REGISTRATION, filed first-class, brought to the author before anything is built on it:**

> ### **`S4` AS SEALED IS STRICTLY STRONGER THAN "HAS AN EULER PRODUCT", AND THE GAP IS POPULATED.**

`S4`'s sealed statement is **total** multiplicativity. **Ramanujan Δ has an Euler product and is not
totally multiplicative** — and the corpus already banked the numbers that decide it:

> `τ = [1, −24, 252, −1472, …]` (`VERIFICATION_LOOM`, ledger table, *"classical values verified"*)
> **`τ(2)² = (−24)² = 576`  ·  `τ(4) = −1472`  ·  `576 ≠ −1472`.**

**`MEASURED`, from the corpus's own stream, at zero fetch cost.** Those values were banked to grade a
*ledger sign*; they settle the *coefficient law* as a by-product. **This is canon XV's
`possession-precedes-recognition` line firing a fifth time — the datum was held, in another coordinate.**

**What it does and does not do.**

* **It does NOT refute the localization.** E2's refuting shape is *`S4` present **and** off-line*. Δ is the
  mirror — *`S4`-as-sealed absent **and** on-line* — and the localization never claimed that `S4`'s absence
  *forces* escape, only that it permits it. **No refutation. The stop is not triggered.**
* **It DOES show the sealed row cannot be the carrier as written.** Rows 3, 4 and 5 all fail `S4`-as-sealed
  and all stay on-line. **The predicate that separates the on-line rows from rows 6/7/12 is
  multiplicativity (an Euler product of some degree), not total multiplicativity (degree one).**
* **The witness cannot see the difference.** Epstein `h > 1` fails *both* readings, so **the disc `−23`
  witness under-resolves `S4`** — it localizes to the coefficient law without distinguishing which
  coefficient law. **Δ is what separates them, and Δ is already in the corpus.**

> ### **AUTHOR-RULED, NOT EXECUTOR-PATCHED.** *Per the standing discipline — "correcting a field of the
> specification is an author-ruled change, not an executor's patch" — `S4`'s statement is **not** amended
> here. The defect is filed with its witness and its measurement, and the S-table stands as sealed until
> the author rules.*

### 2.3 — The `S2` cell that is empty by ABSENCE

**`S2`'s seal is `ℚ`-only.** The compiled terminal reads *"the places of **`ℚ`**"*. Hecke and automorphic
`L`-functions live over a number field `K`; the Ostrowski analogue is classical but **the corpus's compiled
seal does not transport to it, and no `K`-version is held.** Rows 3, 4 (and 8) carry `?` at `S2` for that
reason and for no other. **Empty by ABSENCE — nobody here has built it — not by theorem.**

### 2.4 — The row that must not be counted

**Selberg class `S` is a definition, not a witness.** Its placement cell reads *"Yes (by axiomatization)"* —
the class is *defined* by the axioms whose sufficiency is at issue, and its Euler-product axiom is an input.
**Counting it among the witnesses would be circular.** It is carried in the lattice because the corpus's own
Complete Record carries it, and it is **excluded from every count in §2.1 and §3.**

---

## §3 — THE EMPTY-CELL READING *(the act's deliverable)*

### 3.1 — The cell that matters: **`S4` present ∧ off-line zeros**

### **EMPTY. AND ITS EMPTINESS IS `UNDETERMINED`, NOT `ABSENCE` — the distinction is the finding.**

Registering this cell as "nobody has constructed one" would be an error, and the corpus said why before
this act ran, in `THE_EULER_SPECIFICATION` §3, quoted:

> *"a multiplicative-side positive control would be an Euler-product-bearing object with a known off-line
> zero — **that is, a counterexample to RH**."*

> ### **THE CELL IS EMPTY EXACTLY BECAUSE RH/GRH IS OPEN. Filling it is not a construction task; it is
> the negation of the problem. No amount of searching can move it, and no failure to find one is evidence
> of anything.**

**CONSEQUENCE, and it is the act's consequence line made concrete:** ### **there is no positive control on
the multiplicative side, and there cannot be one over `ℚ`.** *Any proposed mechanism for how `S4` constrains
placement is therefore untestable by the one experiment that would test it — the lattice permits mechanisms
to be **stated** and refuses to let them be **calibrated**.*

### 3.2 — `S6` where `S4` fails: **`VACUOUS`, a fourth emptiness kind**

The charter provides THEOREM / ABSENCE / UNDETERMINED. **Rows 6, 7, 9, 12 need a fourth.** `S6` is a
property *of the Euler product* — its domain of convergence. Where there is no product there is no domain,
and the cell is not empty for want of a fact: **the spec is not stateable of the object.**
**Declared as `VACUOUS` and flagged as an addition to the charter's three, for the author's word.**

### 3.3 — What the populated cells forbid

Reading across, three constraints on any sign-deciding mechanism — **each a restriction, none a route:**

1. **It must act on multiplicativity, not total multiplicativity** (§2.2) — else Δ, Hecke and Epstein `h=1`
   are outside its reach while sitting on the line.
2. **It cannot be calibrated** (§3.1) — the only object that would test it would settle RH.
3. **It cannot be an `S5`-only instrument.** Already filed and unchanged by this act:
   *"the cartography bench is an `S5` instrument, and nothing else … It has no access to `S4`"*
   (`THE_EULER_SPECIFICATION`, FOUND-BEYOND item 2). **The lattice adds no reach to the bench.**

### 3.4 — The `(S4 ∧ ¬S3)` row, and what it says

**`E_k` has `S4` and no functional equation — and its zero set is empty.** It is not a counterexample and not
a control; it is a boundary marker:

> ### **`S4` ALONE MANUFACTURES NO PLACEMENT QUESTION. The zeros whose placement is at issue are produced
> by `S3`; `S4` is the law that binds addresses that `S3`'s symmetry has already made into a zero set.**

*Consistent with the sealed placement-capacity column — `S4` "carries no address of its own" — and sharper
than it: `S4` also carries no zero of its own.*

---

## §4 — THE BEURLING CORNER: **PRICED, NOT RUN** — and the corpus-first result is itself the finding

### **CORPUS-FIRST RESULT: ABSENT. Zero hits across the corpus for `generalized prime`, `generalised prime`, `Beurling prime`, `Beurling generalized`, `g-prime`.**

**The one near-collision, and it is a trap worth naming:** the corpus *does* carry **Beurling–Nyman** — the
BN distance, its unconditional ceiling (Báez-Duarte–Balazard–Landreau–Saias, improved Burnol), and the
E-7b Gram-determinant work. ### **That is a different object entirely** — a functional-analytic RH
equivalent, not a generalized-prime system. **A name-identity trap of exactly the kind the corpus has
armed before; flagged so act 2 does not walk into it.**

### Why the corner is worth act 2 — stated from the lattice, not from enthusiasm

**Beurling systems keep `S1` and `S4` by construction while varying `S5`'s addresses continuously.** Placed
against §3.1, that yields the corner's actual value:

> ### **A BEURLING SYSTEM WITH AN EULER PRODUCT AND OFF-LINE ZEROS WOULD POPULATE THE `S4`-PRESENT ∧
> OFF-LINE CELL **WITHOUT** BEING A COUNTEREXAMPLE TO RH — because it fails `S2` instead.** *It is not over
> `ℚ`; its places are not Ostrowski's roster.*
>
> ### **THAT IS PRECISELY WHY IT IS THE NEAREST THING TO A CONTROLLED EXPERIMENT ARITHMETIC OFFERS: it is
> the only known way to breach the untestability of §3.1, and it pays for the breach in `S2`.**

**Whether the price is acceptable is the act-2 question, and it is not answered here.**

### The pricing

| item | state | price |
|:--|:--|:--|
| **What is known about Beurling-system zeros** | ### **NOT HELD, AND NOT ASSERTED FROM MEMORY.** Candidate leads exist in the executor's memory (Diamond–Montgomery–Vorhauer-type constructions; the PNT-holds-RH-fails family) but are **unverified, uncited, and deliberately left ungraded** — writing them into a cell would violate the act's own rule | **~1 act**, external retrieval, subject to the standing block risk |
| **Whether `S1` survives** | definitional in the literature's setup; **not verified at cite** | rides the above |
| **Can the bench compute there?** | ### **IN FORM, YES — and this is a real answer.** The bench *is* an `S5` address instrument (`PR = 2 log p · p^{−k/2} · w(log p^k)`); Beurling varies exactly those addresses, so the prime-side sum generalizes syntactically by `log p → log p_j` | **~0.5 act** to state the substitution; **the `S4`-blindness of §3.3(3) is inherited unchanged** |

> ### **THE BENCH'S LIMIT CUTS BOTH WAYS HERE.** *It can compute in the Beurling setting because that
> setting is an `S5` deformation — and for the same reason it still cannot see the row the carrier localizes
> to. **Act 2 must not be chartered as "point the bench at Beurling and read off the carrier."*** *Filed now,
> before the charter is written.*

---

## CLOSING

**Banked** at `relay/reports/2026-08-13-witness-lattice-act1.md`.
**Pins read this act, at file, not from memory:** SIDE-kernel `Kernel/Voice7Witness.lean`
(`hadamard_does_not_enforce_online`, axiom-free, `691295b`) · `Kernel/Cascade/SieveCeilingWitness.lean`
(`dh_witness`, `allOnLine .dh = False`) · S-table `phase2/method/THE_EULER_SPECIFICATION.md` v0.1 ·
canon XV/XVI `phase1.5/method/THE_METHOD_CANON.md` · `EXECUTOR_RULES.md` Rule 1.
**Mirror:** per standing checks — this report is the mirror surface; no keystone touched, no REGISTRY row
written, no SPIRAL translation row filed.

**Three items return for the author's word:**
1. ### **`S4`'s seal is stronger than the property doing the work** (§2.2) — witness Δ, measured from banked `τ`. **Spec unamended; author-ruled.**
2. ### **`VACUOUS` proposed as a fourth emptiness kind** (§3.2), against the charter's three.
3. ### **The Beurling corner's real value is that it breaches §3.1's untestability by paying in `S2`** (§4) — act-2 charter shape, not run.

**`h2` UNCHANGED. NO MECHANISM PROPOSED. NO SIGN. NOTHING DEPOSITS.**
