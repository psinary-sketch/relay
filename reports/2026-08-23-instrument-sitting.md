# THE INSTRUMENT SITTING — THE CHECK THAT HAD NEVER BEEN RUN
## ### **THE EIGENBASIS CHECK FIRED. Ψ MOVES BY 4.4e−01 UNDER VARIATION OF THE PROLATE QUADRATURE SIZE — **FOUR ORDERS ABOVE THE 2.774e−05 FLOOR THE RECORD HAS QUOTED SINCE b117** — BECAUSE EVERY PRIOR STABILITY TEST VARIED THE ε GRID OR THE u GRID AND **NQ HAD NEVER BEEN VARIED AT ALL**. **THE ONE-SIGN VERDICT SURVIVES**: max I(L) OVER EVERY CELL AND EVERY BASIS IS −0.0288, STRICTLY NEGATIVE. ### **THE DOMINANCE VERDICT DOES NOT.** AT a² = 2 THE REMAINDER **EXCEEDS** THE TREND AT TWO OF THREE ALTERNATIVE BASES (RATIOS 1.541 AND 1.432 AGAINST 0.756 AT THE RECORDED ONE), SO b119'S RANGE-WIDE DOMINANCE IS **A PROPERTY OF THE RECORDED BASIS AND NOT OF THE MATHEMATICS — AND IT IS WITHDRAWN TO THAT BASIS.** P1 LANDS BRANCH (b) WITH BOTH OFFERED ROUTES CLOSED FOR STATED REASONS; P2'S MODULUS COMPUTES AND CLOSES THE COVERAGE STEP BUT **NOT THE GRADE**; **P3 UPGRADES NOTHING.** BOTH STRIKEABLES RIDE. CORE 271/271. NOTHING DEPOSITS.**

**Relay report · 2026-08-23 · ferry-executed (part 1 of 1, receipt confirmed in
full, Rule 1) · Rules 3/4/5 · the b121 run-registration banked before any
substantive computation, **with two probes disclosed and one added check
registered together with its failure mode** · rigorous-numerics instrument work
· **the reproduce-before-extend gate applied to this act's own tool and passed
before any varied number was read** · the grade-index convention on every
re-grade, shown and never rounded · b38's verdicts fenced · nothing about `h2` ·
nothing deposits · nothing circulates beyond this report.**

> ### **RULE-3 LOG:** *(a) the prolate layer's exact construction read at its
> owner — a Nyström discretization of the sinc kernel, symmetrized, then
> `numpy.linalg.eigh`; **the record's "certified 15/15" is an agreement check
> against banked rows, not an error bound**, and this act is where that
> distinction becomes load-bearing. Also: the dilated-evaluation interpolant
> (b116's isolated noise source); the ε-integral at its rebuilt domain; b117's
> enclosures and floor; b119's split, bounds and ratio table; the licensed
> range. (b) the target grade stated in advance, **with the commitment that
> partials re-grade nothing** — held. (c) both seats registered with transfers.
> (d) independence check run. **VOICE FLAGS: none.** The banned-term review is
> at §5 with its hit table — run, not claimed.*

---

## §1 — COMPONENT 1: THE PROLATE BOUND (P1) — **BRANCH (b)**

**The gate first.** This act's own tool reproduced the banked cells at the
recorded configuration — worst |I(L) reproduced − banked| = **5.88e−07** — before
any varied number was read.

**Both routes P1 offers are closed, each for a stated reason.** ***Direct
evaluation: closed.*** The layer's analytic continuation is not a drop-in
evaluator for the modes on [−1,1] — max discrepancy **3.626e+02** — and the
reason is on the formula's face: the 1/λ factor, which at λ² ~ 1e−16 amplifies
by ~1e8. ***A derivative estimate for the interpolant: closed upstream.*** Such
an estimate needs max|ξ″| of the *true* function; the record holds only
numerical eigenvectors, and bounding *their* error is the very thing at issue.

### **THE UNBOUNDABLE CONSTITUENT, NAMED: THE PROLATE EIGENVECTORS THEMSELVES.** And the standard perturbation route is not merely unavailable but **vacuous**: modes 7–10 sit at λ² = 2.3e−16 … 4.7e−16 with mutual separations down to **4.271e−17**, so a bound scaling as perturbation-over-separation exceeds 1 before it is written.

### **THE ADDED CHECK — REGISTERED WITH ITS FAILURE MODE, AND IT FIRED.**

| NQ | max\|Ψ(NQ) − Ψ(700)\| | Ψ(0) | Ψ(u_max) |
|--:|--:|--:|--:|
| 700 | *(reference)* | −1.165002987 | +0.173014326 |
| 600 | **4.361e−01** | −1.165002987 | +0.088516989 |
| 800 | **3.428e−01** | −1.165002987 | +0.123655930 |
| 900 | **3.095e−01** | −1.165002987 | +0.087496854 |

**Against b117's quoted floor of 2.774e−05.** Ψ(0) is identical across all four —
as the derivation predicts, being basis-invariant. The u-dependent part moves,
and **it does not converge with NQ**, which is the signature of sampling error
rather than of discretization convergence.

***The cause, tested rather than assumed — and my first hypothesis was wrong.***
I supposed the degenerate cluster was responsible. **The truncation test refutes
it:** the spread persists at 11, 10, 9, 8, 7 and **6 modes** (0.388 → 0.237),
where every eigenvalue is well separated. **So it is not the cluster.** The
remaining cause is **the dilated-evaluation interpolant** — the modes are
interpolated linearly on Gauss–Legendre nodes, which cluster at the endpoints
and are sparse exactly where the dilated abscissae fall. ### **b116 identified this interpolant and measured its effect on a derivative *count*; this act measures its effect on the *values*, and it is ~0.4, not ~1e−05. The diagnosis is confirmed and its magnitude was understated by four orders — because the test that would have shown it was never run.**

## §2 — COMPONENT 2: THE CONTINUUM STEP (P2) — coverage closes, grade does not

Measured Lipschitz modulus for I(L): **max |dI/dL| = 0.216675.** Against b119's
60-point mesh (0.026933), Lipschitz × half-mesh = 0.002918 and the worst case
between samples is **−0.056560 — strictly negative**. On a 601-point sweep the
worst case across the continuum is **−0.059191 — strictly negative.**

**So the sampled-to-continuum step closes in form, with room to spare.**
***And it closes at the grade it started, not a higher one: the modulus is
measured from the same samples §1 could not bound. This is a coverage upgrade
conditional on the samples, and not a grade upgrade.*** The distinction was
registered before computing and is held here. **Branch (b) on grade; the
coverage half lands.**

## §3 — COMPONENT 3: THE RE-GRADE (P3) — **nothing upgrades, and one thing comes down**

By the registration's own commitment, P1 and P2 falling short means **the
conditional verdicts stay conditional. Certified-numerics is not reached and is
not claimed.** But the act cannot stop there, because its own measurement bears
on the verdicts it was sent to certify.

### **THE ONE-SIGN VERDICT (b117): SURVIVES.** Across all nine cells and all four bases, **max I(L) = −0.028796** — strictly negative everywhere. The sign is robust to the perturbation that breaks the finer verdict. Its grade is unchanged, and its conditionality is now known to be doing real work.

### **THE DOMINANCE VERDICT (b119): WITHDRAWN TO ITS BASIS.**

| a² = 2 | \|fine\|/\|coarse\| | |
|--:|--:|:--|
| NQ = 600 | **1.541** | ***NOT dominated*** |
| NQ = 700 | 0.756 | dominated *(the recorded basis)* |
| NQ = 800 | **1.432** | ***NOT dominated*** |
| NQ = 900 | 0.107 | dominated |

*At a² = 3, 4, 9 and 48 dominance holds at every basis tested.* b119 reported
dominance at 9 of 9 cells and 60 of 60 sweep points with worst ratio 0.462.
### **At the smallest cell that verdict is a property of the recorded basis and not of the mathematics.** **The downgrade, shown under the convention:** from *holds across the licensed range at enclosure grade conditional on the samples* to ### ***holds at the recorded basis; basis-dependent at the smallest cell; not established range-wide.*** The mechanism it named returns to **candidate** status at a² = 2 and stands at the recorded basis elsewhere.

***What is NOT withdrawn, said so the downgrade is not over-read:*** the split's
exactness is algebra and is untouched; **the sign is untouched**; b115's collapse
and scale-average forms are exact algebra and are untouched; b116's orientation
is untouched. **What is withdrawn is one verdict's range-wide reach.**

**The lane, restated.** ### **The instrument item is now the lane's head, not a side sitting: a stable evaluation of the prolate modes at dilated abscissae.** Until it exists, every Ψ-derived quantity carries a sampling error of order 0.4, and the finer the verdict the less it can bear. **The concrete repair, named:** replace the Gauss-node linear interpolation with an evaluation that does not degrade off-node — a spectral reconstruction from Legendre coefficients, or a direct Nyström evaluation at the dilated points. Both are constructions with their own registrations; **neither is attempted here.** Behind it: the closed-form crown; **the re-rerun revisit, which should be re-staged *behind* the instrument item since it would inherit the same samples**; the boundary, guarded.

## §4 — THE TWO STRIKEABLES

**COMPONENT 4 — THE LEDGER RULING: ADOPTED.** The two-lane reading — the
superlative ledger **inventory and judgment-free as minted**; the banned-stem
list **enforcement as always**; the author-caught totalizer filed to the
inventory lane; ### **the "violation" framing withdrawn as the navigator's mislabel.** ***My b120 refusal is thereby satisfied, not overridden:*** I declined to convert inventory into enforcement and named both readings; you have ruled, and the ruling is reading (B).

**COMPONENT 5 — THE AXIS RULING: ADOPTED BY STAGING.** The graded
transmission-weight axis is drafted into the staged v4.3 increment as an
**additive** axis beside rank; b119 the founding instance; **D.27 and D.30
untouched**; the splice remains one decision at your word. ***And a note the
ruling now requires:*** b119's verdict is downgraded by §3, so **the founding
instance cites a measurement that is basis-dependent at its smallest cell.** The
axis survives that — unequal transmission weighting is visible at **every** basis
tested, only its magnitude moves — **but the draft must not cite the 2.2-to-3.5
factor as fixed, and it does not.**

## §5 — THE BANNED-TERM REVIEW, WITH ITS HIT TABLE

```
  stems scanned : gap, blind
  scope         : this act's added lines + the whole of files it creates
  files scanned : 8
  hits found    : 2   (both the artifact's own "stems scanned" line)
  corrections made : 0
  VERDICT          : CLEAN — no live use in anything this act ships
```

*The two hits are the block above naming its own stems — the self-reference
already filed at b120 as a general lesson. It is classified, not patched again.*

## §6 — THE TAG, GRADE-LABEL, AND SCALE AUDITS

**Tags:** b38's verdicts fenced; the guard unchanged on every location; the
downgrade stated as a downgrade rather than softened; **what is not withdrawn
listed explicitly beside what is.**

**Grades:** P1 **branch (b)**, no bound, the constituent named; P2 **coverage at
the existing grade, not a grade upgrade**; the sign verdict **unchanged,
conditional**; the dominance verdict ### **downgraded and shown**; both rulings **adopted as ratified**. Certified-numerics **not reached and not claimed** anywhere.

**Scale:** ### **the act's central result is a scale correction.** The quoted refinement-stable scale of 2.774e−05 measured stability against the ε grid only; **the prolate-side sampling error is ~0.4**, and every Ψ claim in the record inherits that until the instrument item is done. *This report states 0.4 wherever it states a Ψ-derived margin.*

## §7 — DEVIATIONS

**None.** The added check was registered with its failure mode before it ran.
No divergence.

## §8 — THE RECORD AND PINS

*Relay: the b121 run-registration + bank + instrument + this report.
SIDE-global-section: UNTOUCHED (Core 271/271). PLACE-papers: FINDINGS +
OPEN_TRAILS + the loom's dated line. Mirror: refreshed —
**`mirror-refresh-2026-08-23-j.zip` is the one to load.***

> **PIN LINE (post-push read-back, ls-remote):**
> [PIN-LINE-SPLICE]

## FOOT

**After this act the sixteenth seam close runs at the cadence. ### The re-rerun revisit should be re-staged behind the instrument item, which this act moves to the head of the lane** — the translation table's staging question cannot be answered with verdicts whose samples carry an unbounded error of order 0.4. The closed-form crown stands as the research target; the boundary guarded; the v4.3 splice, now carrying the axis draft, at the author's word; the protocol last.

**`h2` UNCHANGED. THE REGISTER SENTENCE UNTOUCHED. NOTHING PROMOTED.
NOTHING DEPOSITS. NOTHING CIRCULATES.**
