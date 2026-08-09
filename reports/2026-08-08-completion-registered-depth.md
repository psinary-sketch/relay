# THE ARITHMETIC-SIDE VALIDATION REACHES ITS REGISTERED DEPTH — COMPLETION PROTOCOL — 2026-08-08

Rail at `de621b1` / `2147a03`. Census held aside throughout. **Nothing deposits.**

**The completion protocol governs: registrations restated verbatim FIRST, then the number, then the
verdict mapped, and no interpretation beyond the mapping.**

---

## §0 — STATE, BEFORE ANYTHING IS READ FROM IT

**Stage 6 BANKED at the registered depth n ≈ 7000.** The worker then **HALTED at stage 7**, which is
beyond the registered depth. Both facts are established below before the protocol runs; the halt
does not touch stage 6.

| | |
|:--|:--|
| stage-6 record | present, `nmax=7000, dps=3821` (registered 3200, raised by certificate) |
| stage-6 wall | 14.129 h · **total banked wall 18.92 h** across seven stages |
| certified λ error bound | **2.7645×10⁻¹⁰**, within the 10⁻⁶ ceiling |
| min certified coefficient accuracy | 86 bits at m = 7000 |
| worker | **PID 30664 ABSENT** — halted, see §5 |

---

## §1 — THE REGISTRATIONS, VERBATIM, BEFORE THE NUMBER

**THE THREE DEPTH PREDICTIONS, as recorded before any compute:**

> **(a) n ≈ 7000** — the corrected detection law against **this object's own background**,
> `n = 586.4·log(2.5·S∞(n))` with `S∞(n) ≈ n log n`, iterating to 7000. **(b) R4's measured 3379**
> at the same γ, δ — **and the same-object question is ANSWERED: NO. They are two constructions.**
> … **So 3379 is a MEASUREMENT ON A DIFFERENT OBJECT, not a prediction for this one**, carried into
> the adjudication because all three must be compared and labelled for what it is. **(c) the log
> form ≈ 5100** — computed with `background = 2400`, the truncated-zero c_n scale, **also not this
> object's background.** **Of the three, only (a) used the Epstein object's own background —
> recorded as a fact about the derivations, and it does NOT pre-select (a).**

**THE ADJUDICATION RULE, verbatim:**

> **THE ADJUDICATION RULE, FIXED BEFORE COMPUTE: tolerance ±15%, windows disjoint — (a) [5950,
> 8050] · (b) [2872, 3886] · (c) [4335, 5865].** A landing within tolerance of ONE with the others
> outside SELECTS it and the others are recorded as superseded with the reason; **a landing BETWEEN
> them or OUTSIDE all three FILES FIRST-CLASS and NO LAW IS SELECTED; no post-hoc fourth
> prediction.**

**THE PHASE-LAG EXTENSION, registered 2026-08-06, before data:**

> **ADJUDICATION NOTE, stated now so it cannot be post-hoc: a first negative index falling within
> ONE PERIOD ABOVE window (a)'s upper edge — i.e. in (8050, 8152] — reads as (a)-WITH-PHASE-LAG,
> not as a miss.** The extension is **one-sided and upward only**, since a phase lag delays first
> negativity and cannot advance it. **AND A COLLISION THE RULE CREATES, CAUGHT BEFORE DATA RATHER
> THAN AFTER:** applying the same one-period extension uniformly gives (b) → [2872, 3988] and
> (c) → [4335, **5967**], and **(c)-extended now OVERLAPS window (a)'s lower edge of 5950 in the
> interval [5950, 5967]. A landing in that 17-wide interval is AMBIGUOUS between (c)-with-phase-lag
> and (a)-on-time, and therefore FILES FIRST-CLASS AS AMBIGUOUS, selecting neither.**

Measured period at the located zero: **102.5** (β = 0.9533, γ = 16.290, |z_out| = 1.00170675,
arg = 0.061321).

---

## §2 — THE NUMBER

> ### **FIRST NEGATIVE INDEX = 5938**

Running minimum **−232200.84664800408 at n = 6968** · λ_last(7000) = 179172.9824938239 ·
sign of running minimum **NEGATIVE**.

### Verification, because the whole verdict rests on one integer 12 units from indeterminacy

**Recomputed independently from the banked coefficients**, not read from the worker's summary:

| n | λ_n | sign | \|λ\|/bound |
|--:|:--|:--|--:|
| 5936 | +2238.97344765 | pos | 8.1×10¹² |
| **5937** | **+983.131156275** | **pos** | 3.6×10¹² |
| **5938** | **−102.856784807** | **NEG** | 3.7×10¹¹ |
| 5939 | −1013.72162831 | NEG | 3.7×10¹² |
| 5950 | +1239.31305675 | pos | 4.5×10¹² |

**The sign at 5938 is certified by a margin of 3.7×10¹¹ times the stage's error bound** — and the
bound at n = 5938 is smaller than the stage figure by a further factor of ~10⁻⁵⁷⁸, since it scales
as (1+1/r)ⁿ. **An independent coarse scan of 5000 → 5930 from the banked coefficients returned
positive at every grid point**, and stages 5 and 6 are two independent full scans that agree on
first-negativity being absent below 5938.

**The crossing is narrow and that is the registered signature, not an anomaly:** λ runs
88085 (5900) → 13017 (5930) → +983 (5937) → **−103** (5938) → −2602 (5945) → +1239 (5950) →
42526 (5967). First negativity was registered as **amplitude crossing × phase alignment**, and a
brief excursion is what an amplitude barely exceeding its background produces.

**One stated limitation of the worker's own scan, which my recomputation does not share:** it casts
λ to float64 before testing the sign, so a negative λ of magnitude below ~10⁻³⁰⁸ would read as
non-negative. Given step sizes of order 10³ through this region the risk is nil, but it is a
property of the instrument and is recorded rather than assumed away.

---

## §3 — THE VERDICT, MAPPED

| prediction | base window | contains 5938? | extended | contains 5938? |
|:--|:--|:--|:--|:--|
| (a) n ≈ 7000 | [5950, 8050] | **no** | [5950, 8152] (upward only) | **no** |
| (b) 3379 | [2872, 3886] | no | [2872, 3988] | no — **refuted at stage 5** |
| **(c) ≈ 5100** | [4335, 5865] | no | **[4335, 5967]** | **YES** |
| ambiguity strip | | | [5950, 5967] | **no** |

> ### **(c) IS SELECTED, WITH PHASE LAG. (a) AND (b) ARE SUPERSEDED.**

**Three facts about this mapping, which are part of it and not commentary on it:**

**1 — THE SELECTION DEPENDS ENTIRELY ON THE PRE-REGISTERED EXTENSION. On the base windows alone,
5938 falls in the gap between (c)'s upper edge 5865 and (a)'s lower edge 5950 — and the registered
rule for that case is "FILES FIRST-CLASS and NO LAW IS SELECTED".** The extension that resolves it
was registered on 2026-08-06, before data, with its period measured at 102.5 and its one-sidedness
argued from the physics (lag delays, cannot advance). **Applying it is legitimate precisely because
it was fixed in advance; that it is load-bearing here is the reason it was worth fixing in
advance.**

**2 — THE RESULT IS TWELVE INDICES FROM INDETERMINACY.** 5938 sits **+73 above (c)'s base upper
edge** and **−12 below (a)'s base lower edge**. Had it been 12 higher it would have landed in the
[5950, 5967] ambiguity strip and **filed as AMBIGUOUS, selecting neither.** Against the point
predictions it is **+16.4% on (c)'s 5100** and **−15.2% on (a)'s 7000** — outside ±15% on both, by
1.4 and 0.2 points respectively. **This is a narrow selection and must never be quoted as a wide
one.**

**3 — THE PREDICTION DERIVED FROM THIS OBJECT'S OWN BACKGROUND IS THE ONE SUPERSEDED.** The
registrations recorded that **only (a) used the Epstein object's own background**, and recorded
equally that this **"does NOT pre-select (a)"**. It did not. (a) is superseded by 12 indices out of
5938 — 0.2%. **That is the mapping's output and no more is drawn from it here.**

**No interpretation beyond the mapping is offered. No post-hoc fourth prediction is proposed.**

---

## §4 — THE EXCLUSION BY-PRODUCT, AND A RUNG THAT MUST NOT BE QUOTED

**The ladder rests on POSITIVITY, so it terminates where positivity terminates: n = 5937.**

**The registered rung "n = 7000 → β > 0.50043" IS NOT REACHED AND MUST NOT BE QUOTED.** λ is
negative at 5938, so positivity through 7000 is false and the bound derived from it does not exist.

**The last rung actually attained and banked: n = 5000 → every real zero with β > 0.50055 excluded,
exact and phase-free.** A slightly tighter bound is derivable from positivity through 5937 by the
recorded formula; **I have not run it, and it is therefore not stated as a number.**

---

## §5 — THE HALT AT STAGE 7, DIAGNOSED, NOT REPAIRED

Stage 7 is **beyond the registered depth** and was carried only so that a null would stay
distinguishable from a shortfall. **The run did not return a null, so that purpose is spent.**

```
ValueError: Exceeds the limit (4300 digits) for integer string conversion
  epstein_li_v3.py line 232, in bank_line — f.write(json.dumps(rec) + "\n")
```

**Python 3.12 caps int→str at 4300 digits. The chunk format serialises mpf mantissas as exact
integers, and at stage 7's prec 16378 bits a mantissa is ~4930 digits.** It fired on the **first
chunk write of stage 7**, so **zero stage-7 values are banked and nothing is torn**; stages 0–6 are
untouched.

**THE CAUSE IS MINE AND I STATE IT PLAINLY: at the REGISTERED dps 4000 the mantissa is ~4020 digits
and this would not have fired. My dps floor raised stage 7 to 4910 and put it over the limit.** The
floor was right about the mathematics — the certificate genuinely forbids dps 4000 at n = 9000 —
but I did not check that raising precision would collide with a serialisation limit, and the
collision was discoverable before launch rather than after.

**The fix is one line — `sys.set_int_max_str_digits(...)` at module scope — and it is NOT applied.**
No improvised repair; stage 7 is past the registered depth and restarting it is a ruling, not an
executor's call. **Restarting as-is will re-crash identically at the same point**, which is stated
so that the standing restart command is not run in the belief that it will simply resume.

**Exact resume point: stage 7, nmax 9000, dps 4910, zero values banked — a restart begins that
stage from its first boundary value.** Stages 0–6 reload from bank and are not recomputed.

---

## §6 — THE RUN, END TO END

| stage | nmax | dps (reg → used) | wall | first negative |
|--:|--:|:--|--:|:--|
| 0–3 | ≤1500 | unchanged | 0.215 h | none |
| 4 | 3000 | 1600 → 1645 | 0.874 h | none |
| 5 | 5000 | 2400 → 2733 | 3.701 h | none — **(b) refuted** |
| 6 | 7000 | 3200 → 3821 | 14.129 h | **5938** |
| | | | **18.92 h total** | |

The incumbent engine's projection for the same depth was **~48 days**.

**I-7 re-confirmation is NOT included in this report and is owed** — the registered protocol calls
for it at both stages in the completion report, and I have not run it. It is the one registered
item outstanding.

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `8527bad` → this pass's commit |
| relay | `2f396cd` → this report's commit |
| SIDE-kernel `5e668b4` · lv `2f71068` · **rail `de621b1` / `2147a03`** | unmoved |

Census held aside at 451 records, never consulted. **Nothing deposits.**
