# b219 — WHAT σ_even WEIGHTS

**2026-08-27 · relay `reports/2026-08-27-what-sigma-even-weights.md`**
**Ferry part 1 of 1, receipt confirmed IN FULL. Registration banked before the components ran.**
**Bank: `data/b219_what_sigma_even_weights.txt` · index queries `data/audit_b219_index_query.txt` · gates `tools/b219_checks.py`.**

> *** ### **BRANCH (OTHER). `σ_even`'s weights are NOT norms of the prolate family on `S(1,1)` —
> and the source does not leave it to be inferred. It states that the vectors they weight are
> ### ORTHOGONAL TO `S(1,1)`.** ### **The double-name hazard the brief named in advance is
> REALISED, and the two objects are not merely different: they are orthogonal.** ***
>
> ### **The clause-(d) computation was NOT LICENSED. Nothing was run.**

## COMPONENT 1 — THE DEFINITION (P1)

`σ_even = Σ_{n even} t(n) / Σ_n t(n)`, with `t(n) = λ(n)² ξ_n(1)² / (1 − λ(n)²)` — b109's
constituent table, graded *"THE SOURCES' OWN GRADE, in the functional's own units; EVEN PINNED,
ODD UNPINNED."* The value `0.6165` is b35's.

**Answering the brief's clause (b) in its own order:**

| question | answer |
|:--|:--|
| what is summed | `t(n) = λ(n)² ξ_n(1)² / (1 − λ(n)²)` |
| over what index | ### **CC's ε-series index `n`** — *not* the prolate index |
| with what weights | `λ(n)²/(1 − λ(n)²)`, against the ### **squared point value** `ξ_n(1)²` |
| over which object | ### **THE CONSTRAINED CLASS** |

b35 fixes the index: *"`ξ_n = √2·ψ_{2n}` — CC's epsilon-series index `n` names the n-th EVEN
prolate."* ### **So "even" in `σ_even` is the parity of CC's `n`, i.e. classical index `2n ≡ 0
mod 4`** — b159's sector split of the constrained class, ***not the eigenfunction parity of b211
and b212.***

### *** THE SENTENCE THAT DECIDED THE ACT ***

CC arXiv 2006.13771, quoted at content in `data/b199_archimedean_nonvanishing.txt`:

> *"Note that by construction the vectors ### **`ξ_n` are all ORTHOGONAL TO `S(1,1)`** and so are
> `η_n = F_eR ξ_n` and `ζ_n`."*

### **The read did not have to weigh a resemblance. It found a sentence.**

## COMPONENT 2 — THE VERDICT (P2): **OTHER**, ON TWO INDEPENDENT GROUNDS

**Ground 1 — the wrong family.** RRT **Proposition 7**, re-read at source for this act, is an
explicit dichotomy: *non-classical ⟹ `ψ(Λ) = ±1`* — ### **with no `λ` at all** — *classical ⟹ `ψ`
extends entire and `ψ(Λ) = ±√λ`, where `0 < λ < 1`.* ### **b35's own check clause C2 records
`0 < λ < 1` for every `t(n)` the corpus used.** *A weight built from a `λ` in `(0,1)` is on the
classical branch by the source's own statement, not by resemblance.*

**Ground 2 — the wrong functional.** ### **`ξ_n(1)²` is a squared POINT VALUE.** A norm of the
prolate family is `∫₁^∞ ψ² dx` — exactly the right-hand side of b211/b212's identity. ### **No
constant converts a point value into an integral across a family.**

> ### **The two grounds fail differently — ground 1 is about WHICH FUNCTIONS, ground 2 about WHICH
> FUNCTIONAL OF THEM — and ground 2 holds even if ground 1 were set aside.**

**The other two candidates, disposed of explicitly.** ### **`|α|²` — NO:** b214 measured
`|α| = πΛ` at *every* eigenvalue in *both* families, so `|α|²` is **constant** and the share would
be a counting share; ### **`t(n)` spans five orders of magnitude** (`t(0) = 11.9719` against
`t(4) = 0.000125459`). ### **`|β′|` — NO:** `β′` is a `μ`-derivative of the non-classical problem's
Wronskian determinant; `t(n)` contains neither.

**The corroborations, kept below the argument on purpose.** The interleaving is strict (b210,
b212), so any counting share over the non-classical family is exactly `½`; an `|α|²` weighting
would give `½` too. ### **`σ_even = 0.6165 ≠ 0.5`.** ***The value agrees with the verdict. The
value did not produce it*** — clause (c) required the decision to come from the definition.

**The read-check on banked numbers** (arithmetic only; nothing measured):
`(t₀+t₂+t₄)/Σ = 14.177305/22.9964757 = ` ### **`0.616499`** against the banked `0.6165`.

## COMPONENT 3 — THE COMPUTATION (P3)

### *** **NOT LICENSED BY THE READ. NOTHING WAS RUN.** ***

Clause (d) permits it *"only if (b) shows the weights are norms of the prolate family on `S(1,1)`."*
(b) shows the opposite, twice over.

> *** ### **AND THE TEMPTATION IS NAMED, BECAUSE IT WAS REAL.** The instruments to build a
> norm-weighted rank table over the non-classical family **exist and are banked** —
> `tools/e16/b210_wronskian.py`'s `norm_integral` and `b212_odd.py`'s `norm_integral_parity`
> compute `∫₁^∞ ψ² dx` to `1e-16`, both parities. ### **A table could have been produced in minutes
> and would have looked like an answer.** It would have been a table about a different object than
> `σ_even`, presented under `σ_even`'s name — ### **the double-name species itself, committed by
> the act sent to diagnose it.** ***The licence clause is what stopped it.*** ***

## WHAT WAS FOUND ON THE WAY, AND IS NOT REPAIRED HERE

**(i) The weight formula's citation does not resolve.** The founding warrant names *"CC's Lemma
5.4"* and *"Prop 5.5"*. b169: ### **never read at content anywhere in the record.** b171 checked
the three named works — `2112.05500` (no such labels), `2310.18423` (neither), `2511.22755` (has a
Lemma 5.4, *about truncated matrices and determinants*) — and located the work that **does** carry
the symbols, ### **which was not in the bibliography at all:** `arXiv 2006.13771`, Connes &
Consani. ***The same paper the corpus already reads for the Sonin space — one paper carrying both
objects, which is how two names drift together.*** ### **b219 adds only that this unresolved
citation sits DIRECTLY UNDER the weight formula, raising its priority without discharging it.**

**(ii) Two acts quote CC's displayed equation (14) differently.**

| act | source of the read | denominator |
|:--|:--|:--|
| **b176** | ### **verbatim from the PDF** | `√(1 − λ(n)²)` |
| b171 | an ar5iv/HTML rendering | `(1 − λ(n)²)` |

### **b219 did not open the PDF and does not settle the published text.** What is worth recording:
`t(n) = [λ/√(1−λ²)]² · ξ_n(1)²` — ### **the square of b176's coefficient** — and the step that would
do that squaring is the `ρ → 1⁺` derivative, ***which is precisely the unread "Lemma 5.4."***
### **So the one place the record disagrees with itself is the one place its citation does not
resolve.**

## THE INDEX — 11 HIT / 7 NO KEY, AND THE MISSES ARE ONE LANE

### **All seven misses are the `σ_even` / `t(n)` / CC-equation-(14) lane** (`sigma even`, `t(n)`,
`eps'(1+)`, `concentration eigenvalue`, `classical prolate`, `constrained class`, the warrant
source). ### **Every one of the eleven hits is a CONCLUSION OF AN ACT** — `apportionment-grade`,
`apportionment-family`, `exact-reduction`, `e1-even-bridge` all sit in this same lane and all HIT.
***The things those conclusions are ABOUT have no keys.***

> ### **This is b181's lane limit in a new form: not "a lane with no keys" but** ### **A LANE KEYED
> BY ITS VERDICTS AND NOT BY ITS SUBJECTS.** *A query about what `σ_even` **is** could only miss,
> and a miss reads like a finding.* ### **b216 did not close it** — b216 keyed the prolate arc and
> the term-2 lane.

*** ### **AND A CORRECTION TO THIS ACT'S OWN REGISTRATION.** It recorded *"11 of 12 HIT, the one
miss is `sigma even`."* ### **On the fuller set that is 11 / 7, and the misses are structured
rather than scattered.** The registration understated a **structural** miss as a single missing
word, because it queried the arc's objects and the lane's verdicts and ### **did not query the
lane's own objects.** ***A registration is scored, not admired.*** ***

## THE GATES — 5 of 5 PASS, CLEAN

Each with a must-fail fixture **and** a must-pass witness, and the three states (check / fixture /
witness) are **three distinct real states**, never the same call twice.

| gate | verdict |
|:--|:--|
| `sigma-even-reproduces-from-banked-t` | **PASS** |
| `orthogonality-quote-carried-into-bank` | **PASS** |
| `computation-declared-not-licensed` | **PASS** |
| `no-b219-instrument-was-built` | **PASS** |
| `index-query-sidecar-exists` | **PASS** |

> ### **And the fixtures were built to narrow b217's own limit (1)**, which b217's report recorded
> against itself on its first day of service: *"three of the four fixtures are the same trivial
> shape (`must_contain='### never'`), which fails for a reason unrelated to what the check
> measures."* ### **Here the string-presence fixtures grep THE SAME STRING in a real owner file
> that GENUINELY LACKS IT**, so the fixture fails for the reason the check measures. ***The limit
> is not closed — the harness still cannot tell WHY a fixture failed — it is narrowed by
> construction, and only that is claimed.***

### *** ONE SMALL FAILURE OF THIS ACT'S OWN, RECORDED ***

I first ran `banned_terms.py` and `commit_selfcheck.py` with `--act b219-docs`. ### **Neither tool
takes `--act`; both take `--emit`.** The flag was ### **silently ignored** — the tools ran, printed
correct verdicts, and ### **wrote no sidecar at all.** Caught by listing the sidecar directory
before writing this report, ***not by any tool.*** Re-run with `--emit`, the numbers reproduced
exactly (2 files, 139 lines, 0 live uses).
### **An unrecognised flag accepted in silence is the b217 species wearing different clothes: the
command did not fail, and its output looked exactly like success.**

*And one thing the tools did right, worth naming:* the first `banned_terms` invocation was given no
scope and returned ### **"NO SCOPE — HARD FAILURE"** rather than CLEAN over zero lines. ***That is
b166's failure mode refusing to happen.***

**Two smaller notes, recorded because both look like findings and neither is.**
### **(1)** `audit_verify` exited **255** on a run whose verdict was CLEAN and whose four blocks all
MATCHED. ### **The cause was my own shell truncation** (`Select-Object -First 22`) closing the pipe
under the tool; the tool returns `0`. ***An exit code that looks like failure on a clean run is the
mirror of b217's species, and is worth the same suspicion in the opposite direction.***
### **(2)** `data/audit_b219_index_query.txt` is **hand-authored and carries no emitted block**, so
`audit_verify` lists it under *"UNUSED sidecars — not a failure."* It sits in the emitted-sidecar
namespace by ### **b204's precedent** (`audit_b204_index_query.txt`), which this act followed rather
than invented. *Named because it lands exactly on the tool's own stated reach — "this cannot detect
a sidecar written by hand from scratch."*

## THE AUDIT SIDECARS (emitted; copied from the sidecar files)

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : check_harness
  act       : b219
  run at    : 2026-08-27T16:35:43 (local)
  input     : 5 checks routed through the harness
  checks    : 5
  pass      : 5
  fail      : 0
  error     : 0
  refused   : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 d53b136d6b5619f23a4cbfbf7eb7907a
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : banned_terms
  act       : b219-docs
  run at    : 2026-08-27T16:45:17 (local)
  input     : added lines in D:/MY-DOwnloads/PLACE-papers vs 5f1ce35
  stems     : gap, blind
  files     : 2
  lines     : 139
  hits      : 0
  live uses : 0
  VERDICT   : CLEAN
  self-hash : sha256/32 9eac4a4e6683137f65531e99a60bbebd
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : commit_selfcheck
  act       : b219-docs
  run at    : 2026-08-27T16:45:56 (local)
  input     : D:/MY-DOwnloads/PLACE-papers
  input     : HEAD
  written   : 2
  foreign   : 0
  ro-claim  : none
  compliance : none
  VERDICT   : CLEAN
  self-hash : sha256/32 2bdc0acf4089cfd6e1b1b75893342dd0
=== END AUDIT SIDECAR ===
```

```
=== AUDIT SIDECAR (emitted; do not retype) ===
  tool      : mirror_verify
  act       : b219
  run at    : 2026-08-27T16:44:19 (local)
  input     : mirror-refresh-2026-08-27.zip
  files     : 40
  rows      : 40
  mismatch  : 0
  declared  : a980cbf
  ls-remote : a980cbf8ebe7
  VERDICT   : CLEAN ON ALL THREE CLAUSES
  self-hash : sha256/32 09c772b8bb3c7d04c6ffba4026278f5c
=== END AUDIT SIDECAR ===
```

## WHAT THIS ACT DOES **NOT** ESTABLISH

1. ### **It does not show `σ_even` is wrong, or the apportionment unsound.** `σ_even` is a correct
   share **of its own series**; b107's *CLOSED-AT-BENCH, OPEN-AT-DERIVATION* grade is untouched.
   ### **The finding is about what it is a share OF.**
2. ### **It does not settle CC's published equation (14).** Two record-quotes disagree; the PDF was
   not opened here.
3. ### **It does not repair the `Lemma 5.4 / Prop 5.5` citation.** b169's and b171's finding stands
   where they left it.
4. ### **It does not derive `t(n)` from (14).** The squaring is observed as an algebraic identity
   and ### **is not claimed as the source's derivation.**
5. ### **No sign sentence about the Weil ledger, in any form. Nothing about h2 beyond the register
   sentence exact. Nothing deposits.**

## PINS

| repo | pin | note |
|:--|:--|:--|
| **PLACE-papers** | `5f1ce35` → ### **`a980cbf`** | `THE_IDENTITY_CHAIN.md` §25 + the in-flight register; hook CLEAN, 0 foreign; **2 files changed, no file created** |
| relay | → the b219 pin-line commit | registration, bank, index queries, gates, four sidecars, report |
| SIDE-global-section | `356010f` — **UNMOVED** | ### **no Lean file touched; no shadow was built, and none was warranted** |
| SIDE-kernel | `0256e9e` — **UNMOVED** | — |
| mirror | rebuilt at `a980cbf`, **CLEAN ON ALL THREE CLAUSES**, 40/40, roster unchanged | — |
| HELD | `6eada6a` — LOCAL-ONLY, untouched | — |

**DEVIATIONS:** none.
**DIVERGENCES:** ### **one, with the ferry's FOOT rather than its clauses.** The FOOT names *"the
aggregation's freedom"* as next, and that remains available and untouched. ### **But the ferry's
(P2) also contemplates a crown-act reformulation on branch (NORMS), and branch (NORMS) did not
land — so no reformulation is registered.** *Named, not worked around.*
