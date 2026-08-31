# THE JUNCTION'S DIVERGENCE — b262, 2026-08-31

**Scope:** a derivation at content with bench controls. **CONCURRENCY: SOLO (research seat).**
A finite cell decides NOTHING global (b14/b15); b242 governs — *"a measured rate is not a tail
bound."* The register sentence is unchanged and **nothing deposits.** The patent lane is
independent and was not touched.

**Order of record:** owners read at content → **`needle_extract.py` built, because the ferry made
needle-extraction a scope clause** → index queried → **registration TERM-SCANNED (0 live uses) then
banked** → the run → *(API drop)* → **resume from disk** → the repairs → the shadow → the bank →
the filings → HANDOFF.

---

## The verdict

### **J3: the junction DIVERGES along the cutoff limit.** `PR − Θ_q` runs `0.374669` at `a² = 1e2` to `19.708927` at `a² = 1e8`, doubling per decade — **over ALL primes, not over `S4`.**

The growth is carried entirely by the primes with `n_p(a) = 1`, i.e. `a < p ≤ a²`, **from which
`Θ_q` receives NOTHING**, because act 9's `tau_q` vanishes at `k = n`. So

### **`Θ_q / PR → 0` and `J / PR → 1`: the junction is asymptotically the entire prime side.**

---

## The resume, declared

An API drop cut the prior session mid-repair. State was recovered **from disk**:

| artefact | state |
|:--|:--|
| `b262_registration_2026-08-31.txt` | **intact**, term scan CLEAN (0 live uses), 19275 bytes, mtime preceding the run's |
| `b262_run.txt` | **intact**, 164 lines, ending in its own closing banner |
| `b262_rows.json` | parses, six cells, all flags present |
| half-written files | **none** |

Never written when the drop came: the bank, filings, checks, handoff tool, report, shadow.

> **And one thing the ferry asked for that I must report as absent: the registration carries NO
> banked hash line.** b255 hashed its meanings file and re-checked it at its gates; this act did
> not. So the `sha256` I can quote now is **recorded at resume and proves nothing about what the
> file held before the drop.** The surviving evidence — an mtime ordering and a term scan — is real
> and **weaker**. `W-ORD-REG-HASH` is filed for it. *A hash taken afterwards is a description; a
> hash banked at writing time is proof.*

---

## What made J3 askable at all

**b260's closed form makes the entire junction pure arithmetic.** With
`w·φ = (2 log p / L)·ψ(u/L)·2 sinh(u/2)/(p^{n_p} − 1)`, there is no `quotient_basis`, no
`scaling_matrix`, no dense `p^{2n}` matrix — **no cost wall.**

**b255 refused `a² = 128` on cost. This act reached `a² = 1e8` in 18 seconds** — and it is b260's
result that bought that, not any new instrument.

**The G-REPRO ran first**, before any all-primes value existed: the closed form reproduces b260's
*instrument* at all sixteen `S4` cells to **2.598e-14**. Had it not, every number below would have
been void.

---

## S1 — the partition, with a precision the ferry's wording needs

`T_top := {k = n_p}` and `T_fixed := {k < n_p}` **are** the partition — disjoint and exhaustive.
**The `n_p = 1` family is not a third class; it is a *subset* of `T_top`.** A three-way split would
double-count. *Declared in the registration, not silently corrected in the table.*

The identity making `T_top` simple — `(p^{n/2} − p^{−n/2})/(p^n − 1) = p^{−n/2}` — is **a
tautology**: cross-multiplied it reads `p^n − 1 = p^n − 1`. It held 20000/20000 on arbitrary
`(p,n)`, which is what a tautology does. **It simplifies; it establishes nothing.**

## S2 — the fixed levels die, and this *is* act 9's level limit

`φ = (p^k−1)/(p^{n_p}−1) → 0` with exact rate `(p^k−1)/a²` up to one factor of `p`. Exhibited at
`(p,k) = (2,1)`: `φ·a² → 1` to six figures. At bench, `T_fixed` decays **0.090425 → 0.004814**
across seven decades.

> **A sharper bound this act found only by repairing a bad control:** `φ` is increasing in `k`, so
> on `k ≤ n−1` its supremum is `(p^{n−1}−1)/(p^n−1)`, which is **`< 1/p`** — cleared of division,
> `p(p^{n−1}−1) < p^n − 1`, i.e. `p > 1`. **Sharper than the envelope the registration used**, and
> the shadow compiles it *and its sharpness* (the bound does not improve to `1/(p+1)`).

## S3 — the top levels, and where the growth lives

`F₁(a) = Σ_{a<p≤a²} (2 log p/L)·p^{−1/2}·ψ(log p/L)`. By I-1 and the substitution `t = e^{Ls}`,
`F₁ ~ 2∫₁² a^{s/2} ψ(s) ds`. Since **ψ vanishes to infinite order at `s = 2`** with
`ψ(2−r) ~ exp(−2/r)`, the saddle of `Lr/2 + 2/r` sits at `r* = 2/√L` with value `2√L`:

### `F₁(a) ~ 2a·exp(−2√(log a))` — growth, sub-exponentially damped but unbounded.

`m = 2` is `O(1)` by Mertens and **measures 0.004–0.007 across seven decades — bounded, as
derived**; `m ≥ 3` is `≤ 1.6e-04`.

| `a²` | J(a) | T_top | T_fixed | m=1 | m=2 | m≥3 |
|--:|--:|--:|--:|--:|--:|--:|
| 1e2 | 0.374669 | 0.284244 | 0.090425 | 0.277103 | 0.007141 | 0.000000 |
| 1e3 | 0.549193 | 0.492421 | 0.056772 | 0.487489 | 0.004904 | 0.000028 |
| 1e4 | 1.150252 | 1.118335 | 0.031917 | 1.114605 | 0.003567 | 0.000163 |
| 1e5 | 2.268694 | 2.248878 | 0.019816 | 2.244544 | 0.004226 | 0.000108 |
| 1e6 | 4.645790 | 4.633377 | 0.012413 | 4.628665 | 0.004668 | 0.000044 |
| 1e7 | 9.551566 | 9.543861 | 0.007705 | 9.539401 | 0.004399 | 0.000061 |
| **1e8** | **19.708927** | 19.704113 | 0.004814 | 19.699799 | *(repair (b))* | |

**Every column behaves as derived** — `T_fixed` decays, `m=2` stays bounded, `m≥3` is negligible,
`m=1` carries all the growth. *That is what makes this a control rather than a coincidence.*

The ratio `F₁/(2a·e^{−2√L})` runs `0.288 … 0.426` with per-decade factors `1.100, 1.285, 1.057,
1.031, 0.993, 0.966` — **flattening, not diverging. And it is not banked as a fit, a slope, or a
limit.** b242 is quoted against my own number.

---

## The scope wall — what this costs every earlier number in the corpus

| `a²` | S4: `n_p=1` count | ALL: `n_p=1` count | S4 J | ALL J |
|--:|--:|--:|--:|--:|
| 4 | 1 | 1 | 0.087341 | 0.087341 |
| 9 | 1 | 2 | 0.135021 | 0.135061 |
| 25 | **0** | 6 | 0.161759 | 0.245498 |
| 49 | **0** | 11 | 0.099238 | 0.217410 |
| 100 | **0** | 21 | 0.076658 | **0.374669** |

### **At `a² ≥ 25` the bench set has ZERO primes with `n_p = 1`. The family that decides J3 is absent from EVERY cell this corpus has computed above `a² = 25`.**

**This is not a defect in b255, b260 or b261.** Each fixed its place set and said so at every use;
b255 wrote the limit itself — *"it measures the powers of a fixed prime set along the cutoff axis,
not a growing place set."* **They declared the wall; this act measures what is on the other side of
it.** b246's rule stands: nothing is re-verdicted. But the wall is now on the record rather than
latent — at `a² = 100` the bench junction is `0.0767` and the true one is **nearly five times
larger**, and the ratio widens.

---

## The label, settled by definitions

The index query returned act 9's label, so it had to be faced rather than filed past.

| | which indices move |
|:--|:--|
| **(L-A) act 9's level limit** | FIX `p`. FIX `k`. LET `n → ∞`. |
| **(L-B) this act's cutoff limit** | LET `a² → ∞` — moving *every* `n_p` **and growing the index set**. |

### **Verdict: DISTINCT OBJECTS WITH A STATED RELATION. Not a double-name.** (L-A) is the restriction of (L-B) to a fixed index.

**S2 concerns (L-A) and *confirms* it. S3 concerns (L-B)'s newly-admitted top levels, which no
level limit ever sees** — because (L-A) holds `k` fixed while (L-B) lets it track the cutoff.

> **So the aggregate diverges precisely because the dominant terms are the ones act 9's level limit
> never reaches. Both statements are true and they do not meet.**
>
> **A new species is named: the double-*limit* error.** b219's is two *objects* under one word;
> this is two *limits* under one word, and the corpus had no name for it.

---

## S5 — the meaning for `h2`, with its reach bounded

Under RULE Q the finite-place half of the left side is `−Θ_q`, and the adopted right-side prime term
is `PR`. **If the identity holds along this direction, the archimedean side must absorb a divergent
quantity.** That is the finite-place shadow's first asymptotic statement.

**Four misreadings, refused explicitly:**

1. **It is not evidence against the identity.** A divergent junction matched by a divergent
   archimedean side is a consistent identity; nothing here measures the match.
2. **It is not a statement about b14's double limit.** b15 governs.
3. **It does not move `h2`.** `h2` stands exactly where the deposit left it.
4. **It does not say `Θ_q` is the wrong object.** It says `Θ_q` does not track `PR`; whether it is
   *meant* to is (L-identity), the undecided thing (b228).

---

## The shadow — **11 terminals, zero axioms, 0 errors, profile printed**

`Core/JunctionLimitShadow.lean`, vanilla Lean 4, `decide` only. It compiles the partition counts,
the fixed-level decay as exact integer arithmetic, **the sharp bound `φ < 1/p` cleared of division**,
and **the scope wall as arithmetic** — every `S4` prime has `p² ≤ 100` while `11 ≤ 100 < 11²`, with
`13, 47, 97` shown too so it is not one exceptional prime.

Its load-bearing polarity control is `top_level_fraction_is_one`: at the top level the numerator does
**not** stand still. *Without it, S2 would read as "every term dies" — the exact false reading J3
corrects.* Three false statements of the same shape were **refused**, lean exit 1.

### **It does not compile J3.** The verdict rests on PNT and a saddle-point asymptotic; neither is in `Nat` and neither was forced into it.

---

## Four defects — two the ferry named, two found while repairing them. All mine.

**`b262_run.txt` is preserved unchanged with all four in it.** The repairs live in a separate
artefact. *A run silently corrected leaves no evidence that it was wrong.*

**(a) The I-1 grade line contradicted itself inside one banked file.** Line 95: *"VERIFIED-AT-BENCH
on `[1e2, 1e7]`"*. Line 161: *"NOT VERIFIED — TRUSTED-AT-CITE"*. **Both cannot be true.** The first
was an unconditional string; the second collapsed a per-range fact into one bit. **The measurement
was right and both reports of it were wrong, in opposite directions.** Corrected grade:
**VERIFIED-AT-BENCH on `[1e3, 1e7]`, NOT VERIFIED at `1e2`** (`θ(100)/100 = 0.837`, outside the 10%
bar fixed in the registration), **TRUSTED-AT-CITE above.** *The bar was not moved and the cell was
not dropped* — and the consequence is stated: that cell's number stands as arithmetic but may not be
read through the asymptotic.

**(b) A refusal that was asserted rather than priced.** Line 64 declared `1e8` unaffordable — **a
hard-coded string. Nothing priced it**, and the run's own measured `3.0e-06 s`/prime contradicted
it. **The refusal was not merely unpriced, it was false.** *A refusal invented to look disciplined
is the same crime wearing the opposite coat.* Repaired by pricing: projected `95 MB + 41 MB`, `~16
s`, against a `2048 MB` ceiling declared before the attempt; **actual 0.8 s + 18.2 s. The estimate
was sound.** Then run as control. *Disclosed: the `1e2..1e7` values were already seen when the
extension was authorised — the extension is on the ferry's order and on price, and saying so is the
only evidence left.*

**(c) The printed output and the banked file disagreed.** The repair script emitted a literal `%d`
and mutated it afterwards; `rec` prints before it appends, so the console showed `%d` and the file
showed `164`. **That breaks the corpus's own authority rule** — *a compile is reported only from its
printed profile* — because a console reader and a record reader would not have seen the same run.
**b261's species again.**

**(d) A "discriminator" that was a theorem.** The control tested `φ < 1/2` and I annotated it *"it
must fail sometimes"*. **It read 20000/20000. The annotation was wrong** — `φ < 1/p ≤ 1/2` is a
theorem. **So it was a tautology wearing a discriminator's label, the exact failure the tautology
control exists to catch; the control caught it and my prose misread the result**, blaming the bound
rather than the claim. Replaced with `φ < 1/3` (fails 921/20000). **The defect paid for itself:
running it down produced the sharp bound `φ < 1/p` that S2 and the shadow now carry.**

---

## Gates — 12/12 CLEAN on the first run, and CLEAN again after a Rule 3 rename

**The first run was 12/12 CLEAN** (`audit_b262_check_harness.txt`, `f655222c…`). Then the
banned-term scan caught something the gates could not: **one of the gate *names* carried a Rule 3
stem** — `…-hash-gap-disclosed`. **The scan's scope is the act's own voice, and a gate name is this
act's voice as much as its prose is.** Renamed to `…-hash-omission-disclosed`; **the check, the
fixture and the witness are untouched**, and the re-run is the shipping one below. The superseded
sidecar is on disk and `audit_verify` reports it UNUSED, which is correct and not a failure.

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : check_harness
  act       : b262
  run at    : 2026-08-31T00:07:58 (local)
  input     : 12 checks routed through the harness
  checks    : 12
  pass      : 12
  fail      : 0
  error     : 0
  refused   : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 4d56702ce782a9cfecab063b239c035b
=== END AUDIT SIDECAR ===
```

**Term scan: CLEAN — 0 live uses across 13 files / 2687 lines of this act's own voice.**

**`W-ORD-NEEDLE-EXTRACT` discharged — with a sharper diagnosis than its title.** "Typed needles" is
only half the b229/b260/b261 species. **The other half is that a pure conjunction of six
`contains()` calls reports ONE BIT and names no conjunct** — and in all three acts that debugging
cost is what produced the repeat. `verify_all` now returns the harness's `(verdict, detail)` pair and
**names every missing needle**; the conjunction stays pure. The gate table reads *"5 of 5 needles
present"* instead of *"bool"*.

### **And the evidence it worked: b262's gates came back 12/12 CLEAN on the first run — the first act in four with no needle defect.**

---

## What this act does **not** establish

1. **It does not prove `J → ∞` without imports.** I-1 verified-at-bench on `[1e3,1e7]` only; I-2
   trusted-at-cite. The verdict is **DERIVED-ON-IMPORTS**.
2. **It does not bank a rate.** b242.
3. **It does not discharge `W-ORD-TQ-IDENTIFY`**, which every number inherits.
4. **It says nothing about b14's double limit.** b15 governs.
5. **It is not evidence for or against the identity.** R-III governs the vocabulary.
6. **It does not measure the archimedean side.** That is J4's.
7. **It does not re-verdict b255, b260 or b261.** The scope wall limits what their numbers may be
   *asked*, not what they *say*.
8. **It does not prove `ψ(2−r) ~ exp(−2/r)`** — used at reading grade inside I-2.
9. **Nothing about `h2` beyond the register sentence exact. Nothing deposits.**

---

## Filings

- **Index:** `quotient trace` **HIT** — and the hit returned act 9's level-limit label, **which is
  exactly the object clause (2) demanded be settled. The query did its job: it put the label in
  front of the act before the act could contradict it by accident.** `weil criterion` **HIT**. Reach
  line carried; neither used as a premise. **`junction-limit`/`j3`, `bench-scope-wall` and
  `double-limit-species` keyed.**
- **J4 — `eps_even`'s decay (`W-ORD-EPS-DECAY`), the archimedean twin — filed as next**, with its
  route note: b250's per-mode tools are the assets; **b261's oscillation finding is its first fact,
  not a side note**; and **J3's method does *not* transfer** — `eps_even` has no closed form and is
  not arithmetic. The honest first step is a statement-read on `eps`, not a ladder.
- **New work-order `W-ORD-REG-HASH`** — bank the registration's hash *in* the registration.
- **In flight:** M-2…M-5 open, **none closed.** `W-ORD-B38-HIGHMODE`, `W-ORD-CN-LAW`, the QUOTED-N
  extension, `W-ORD-XI-PERMODE`, `W-ORD-ORDINATE-CACHE`, `W-ORD-STAGING-GUARD`,
  `W-ORD-FILE-E-WORKING-COPY-STALE`, `W-ORD-TE-SPEC`, `W-ORD-TQ-IDENTIFY`, `W-ORD-EPS-DECAY`,
  **`W-ORD-REG-HASH` (new)**. **Discharged this act: `W-ORD-NEEDLE-EXTRACT`.**
- **The thirty-seventh seam's debt restated:** term 2's formalization stands, **unpaid and
  untouched.** J3 touches none of its four items.
- **HANDOFF** brought current by demotion, prior content kept, read-back identical.
- **The patent lane is independent and untouched.** Nothing written or staged under
  `patent-package/` or `PLACE-papers/`; staged by explicit path, no `git add -A`; b256's live b148
  condition re-reported; b259's bank left untracked. **The two uploads are noted DONE and receipts
  PENDING — carried on the ferry's word, not verified by this seat.**
- **`PLACE-papers` not touched — no mirror rebuild owed, none claimed, hook not exercised, reported
  either way.**

### The fork at this stop

1. **J4** — the archimedean twin, with its route note already written.
2. **`W-ORD-TQ-IDENTIFY`** — the premise J1 and J3 both inherit.
3. **`W-ORD-REG-HASH`.**
4. **M-2's aggregation; M-3; M-5; `W-ORD-CN-LAW`.**
5. **The patent lane**, independent, on your word.

---

### **THE JUNCTION DIVERGES, AND IT DIVERGES ON THE PRIMES THE QUOTIENT CHANNEL NEVER SEES. act 9's LEVEL LIMIT IS CONFIRMED AND IS A DIFFERENT LIMIT FROM THIS ONE — THE AGGREGATE GROWS PRECISELY BECAUSE ITS DOMINANT TERMS LIE OUTSIDE THAT LIMIT'S REACH. THE BENCH SET COULD NOT HAVE SEEN ANY OF IT. THE ARCHIMEDEAN SIDE MUST ABSORB A DIVERGENT QUANTITY, AND J4 ASKS WHETHER IT CAN. NO GRADE MOVED BUT J3's OWN. `h2` STANDS EXACTLY WHERE THE DEPOSIT LEFT IT. NOTHING DEPOSITS. LOCKS LAST.**
