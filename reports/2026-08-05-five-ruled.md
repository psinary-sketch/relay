# All five ruled — the census running, the kernel docstring, head 4, R4, the wave-edit opened — 2026-08-05

Pins at open: PLACE-papers `5b93b55`; relay `99d514c`; lv `2f71068`; kernel `44895f9`.
Rail at the post-rename baseline. Nothing deposits.

---

## §1 — THE CENSUS WORKER (running, detached)

**Object.** Disc −23 Epstein zeta of the principal form `x² + xy + 6y²`, h(−23) = 3.
**Ground truth only: HELD ASIDE, and it never enters the arithmetic-side computation it exists
to validate.**

**Method.** `Λ(s) = (√23/2π)^s Γ(s) Z_Q(s)`, computed by the incomplete-gamma expansion
`Λ(s) = Σ_k r_Q(k)[a_k^{−s}Γ(s,a_k) + a_k^{s−1}Γ(1−s,a_k)] − 1/s − 1/(1−s)`, `a_k = 2πk/√23`.
Γ's poles cancel the trivial zeros, so **winding of Λ counts nontrivial zeros**. The census is
**2-D by construction** — a critical-line scan would impose the real part and reproduce exactly
the defect I-7 stage 2 forbids.

**Rule 2 compliance, each item verified before launch:**

| requirement | how it is met |
|:--|:--|
| per-record flushing | one JSON line per cell, `flush()` + `os.fsync()` on every write |
| resume-with-validation | every banked line re-parsed on start; missing fields or non-finite values **discard the record and re-run its cell** |
| self-test banked first | the functional equation checked before any cell is walked, banked as record 0, and the run **halts** if it fails |
| sleep posture | `powercfg` `STANDBYIDLE` AC index `0x00000000` — no idle sleep |
| restart command stated **before** launch | yes — below, verbatim |

**RESTART COMMAND (verbatim, safe to re-run at any time):**

```
cd /d D:\relay && python tools\e16\epstein_census.py
```

Bank: `D:\relay\tools\e16\epstein_census_bank.jsonl`.

**Pre-launch validation, run and passed:** functional-equation relative error **0.0**;
`r_Q(1..12) = [2,0,0,2,0,4,0,4,2,0,0,4]` (correct); **|Λ| at the known off-line zero
0.9533 + 16.290i = 4.5×10⁻¹⁴**. **Status at report time: running, 94 records banked.**

**One scale caveat recorded now rather than later:** |Λ| is uniformly tiny in the strip because
Γ decays like `e^{−πt/2}` — at t ≈ 16 the ambient scale is ~10⁻¹¹. **Winding is scale-free and
unaffected**, but the banked `minmod` field must be read as a *relative* proximity indicator,
not an absolute one.

---

## §2 — THE KERNEL DOCSTRING (landed)

**Pin: `44895f9` → `5e668b4`. Pushed; local = remote verified by full hash
(`5e668b49f058cea2af66e55d3263206d3cf8d1bb`).**

`ECondition.type_I_has_ostrowski` now carries the inertness record: `[Fintype Domain]` unused,
probed not inferred; the syllogism valid on any domain; the recorded profile attributable to the
instance argument; **no defect claimed and none exists**; and the statement deliberately left
unchanged, with the generalization repair recorded as available and not taken.

**Statement unchanged. Docstring only** — `git diff --stat` = 1 file, 20 insertions, 1 deletion.
Module rebuilt (619 jobs, green) and **the profile re-printed after the edit:
`[propext, Quot.sound]` — unchanged.** No other kernel edit rode along.

---

## §3 — HEAD 4'S TEST: the narrowed form is BETTER, and it is NOT PROMOTED

*The free layer is what an order-2 symmetry supplies — its fixed locus or its invariants.*

| face | verdict under the narrowed form |
|:--|:--|
| **FE free** | **PASSES** — the MacWilliams involution is order 2; the fixed locus is the free gift |
| **self-adjointness free** | **PASSES CLEANLY — and this is the narrowing's gain.** `A ↦ Aᵀ` is an involution and self-adjointness is its fixed locus. Under the loose "quadratic" form this face passed only under a strained reading; under the narrow form it is exact |
| **the square free** | **PASSES, and the narrowing explains WHY it is a square:** `H = h·hᵒ` is the **norm under the order-2 conjugation**, so `lead(H) = p₀²` is a norm, not a coincidence of degree |
| **the formalization-cost inversion** | **NOT WELL-POSED** — a meta-face about the economics of certifying free layers; unchanged |
| **centre-equals-weight** | **PASSES** — minted as an instance: σ = ½ is the FE involution's fixed point |

**The ℤ/3 refutation condition stands unrefuted.**

**THE NEXT-TERMINAL LEG COULD NOT RUN.** The registered promotion test is *the next terminal
compiled, checked before it is written* — and **no new terminal was compiled this pass**: item 2
is a docstring, and the census worker is an instrument, not a theorem. **So the head is HELD at
PROPOSED.** Four faces passing on a re-run of the same faces is not the test that was registered,
and the narrowing's real gain — that the weakest face became exact and the square acquired a
reason — is recorded as evidence for the narrowed form **over the loose one**, not as promotion.

---

## §4 — R4'S COMPRESSION SITTING: RUN, AND ANSWERED

### The first thing the sitting had to settle: what the question is about

**About ζ alone the question is VACUOUS.** ζ's zeros are not adjustable, so *"λₙ ≥ 0 for n ≤ N
implies λₙ ≥ 0 for all n"* is, for the actual ζ, either trivially true (RH holds → every N works)
or false past the first negative index (RH fails). **It is not a compression question; it is RH.**

**About the Bombieri–Lagarias family** — arbitrary multisets closed under the symmetry, which is
the generality in which Li's criterion is *proved* — **the question has content.**

### The counterexample-shape, exhibited

Base: 400 on-line ordinates. Perturbation: one off-line quadruple at γ = 16.290, displacement δ.

| δ | first n with λₙ < 0 | n·δ/γ² |
|--:|--:|--:|
| 0.4533 | **3379** | 5.77 |
| 0.1 | **15868** | 5.98 |
| 0.01 | > 40000 (search cap) | — |
| 10⁻³ … 10⁻⁵ | > 40000 | — |

**The multiplier is constant at ≈ 5.9**, so the first negative index is `≈ 5.9·γ²/δ` — the
detection law, confirmed on the object it predicts. **It is unbounded in 1/δ.**

### The verdict on the three pre-stated outcome-shapes

| shape | verdict |
|:--|:--|
| **(1) a bound exists** | **REFUTED** in the Bombieri–Lagarias family |
| **(2) a counterexample-shape exists** | **CONFIRMED, exhibited above** |
| **(3) no such bound can exist** | **CONFIRMED** — (2) holds for every N, since the construction is parameterised by δ and the first negative index is unbounded in 1/δ |

**The maximal-caution clause is NOT triggered: outcome (1) is refuted, not confirmed.**

**SCOPE, which is the whole of the result's honesty.** This settles the question in the generality
in which Li's criterion is proved. **It says nothing about ζ**, whose zeros are not adjustable —
and about ζ alone the question was never a compression question. **No claim about RH is made or
implied.** The compression table's R4 cell closes **by construction**, completing it at five
barred, with the bar's scope stated: barred in the family, vacuous at the object.

---

## §5 — THE WAVE-EDIT / CONSOLIDATION: OPENED, ONE DOCUMENT CHECKPOINTED

**The rail rule is inverted for this pass only, and stated:** the closing check is a **STATED DIFF
per paper**, checkpointed per document — **not empty-diff**.

### Checkpoint 1 — the cosmology propagation repair — **LANDED**

| document | diff |
|:--|:--|
| FINDINGS.md | **+1 line, 0 removed, 0 figures changed** |
| OPEN_TRAILS.md | **+1 line, 0 removed, 0 figures changed** |

A standing note now carries `Ω_b = 4/81`'s status into each ledger that restates it: the tuple
**forces** the arithmetic value, the **identification with Ω_b is PERMITTED** — a chosen physical
reading, not a derivation — its components are **not derived**, and the formula form is **the
definitional model** with its Lean-formalizability open. **Any restatement in that ledger is to be
read against the note.** This closes the gap at ledger granularity rather than editing ~34 sites,
which is the cheaper correct repair for a propagation gap.

### NOT EXECUTED THIS PASS, and said plainly rather than left to be inferred

**Four scope items and the remaining work-orders are untouched:** proofs-cluster consolidation ·
simplicity-cluster annotation · substrate code-garment enrichment · method-program exhibit fold ·
and the **35 provenance work-orders** in their five clusters. **Nothing was landed without its
diff reported, and nothing else was landed.** The per-document checkpoint structure is in place
for whoever continues; the Li/Weil cluster remains the cheapest to close, since this era's
instruments already evaluate S_n and E_quad directly.

---

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `5b93b55` → this pass's commit |
| relay | `99d514c` → this report's commit |
| SIDE-lv-conservation | main = `2f71068` — unmoved |
| **SIDE-kernel** | **`44895f9` → `5e668b4`** — docstring only; profile re-printed unchanged; local = remote verified |
| rail | `de621b1` / `2147a03` — **freeze lifted for this pass only; rail documents untouched, so both remain at baseline** |

Census running and resumable by the command in §1. Consolidation opened, one document
checkpointed. Nothing deposits.
