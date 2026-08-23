# THE PROLATE REPAIR ACT — THE REPAIR FAILS, AND TAKES ITS OWN DIAGNOSIS WITH IT
## ### **BOTH REGISTERED ROUTES FAIL G2, AND THE ACT HALTS PER ITS OWN REGISTRATION. THE NQ EXCURSION DOES NOT COLLAPSE UNDER ANY EVALUATION SCHEME TRIED — 4.361e−01 WITH THE ORIGINAL INTERPOLANT, **1.056e+07** WITH THE NYSTRÖM EXTENSION, **4.109e−01** WITH SPECTRAL RECONSTRUCTION, 3.684e−01 WITH A SPLIT-INTEGRAL DIAGNOSTIC. ### **SO THE INTERPOLANT CANNOT BE THE WHOLE CAUSE, BECAUSE REPLACING IT CHANGES NOTHING — AND b121'S DIAGNOSIS IS RE-OPENED.** THE NYSTRÖM ERROR TRACKS **MACHINE-EPSILON OVER λ** EXACTLY, THE HAZARD I NAMED AT REGISTRATION. AND THE SHARPEST FACT CUTS AGAINST THE ACT'S OWN PREMISE: **Ψ(0) IS DERIVED AND KNOWN, AND ONLY THE ORIGINAL INTERPOLANT RETURNS IT** — EVERY REPLACEMENT IS WRONG WHERE THE ANSWER IS CERTAIN. NOTHING IS RE-RUN, NOTHING RE-GRADED, THE WITHDRAWAL FENCE STANDS. CORE 271/271. NOTHING DEPOSITS.**

**Relay report · 2026-08-23 · ferry-executed (part 1 of 1, receipt confirmed in
full, Rule 1) · Rules 3/4/5 · the b124 run-registration banked before any
computation, **with routes, gates and both seats' expectations, and the fresh
draw fixed at NQ = 1100 in advance** · the reproduce-before-extend gate binding
· the floor-axis law on every floor · the grade-index convention on every
re-grade · b38's verdicts fenced · nothing about `h2` · nothing deposits.**

> ### **RULE-3 LOG:** *(a) the prolate layer at its owner — the Nyström discretization, the symmetrization, the `eigh` call; b121's finding verbatim; b119's split machinery **at its withdrawn-to-basis status**; b117's enclosures; the licensed range. **And a provenance fact found at the owner read and recorded before any build: the layer already uses the Nyström extension at x = 1**, under its own comment *"from the eigenfunction equation, not from the grid"* — the primary route generalized a step the layer already trusts. (b) both routes fixed in advance; **the route taken and the route not taken both recorded** — in the event both were taken, because the first failed. (c) the gates in order, **G2 binding and a failure halting the act**. (d) both seats registered with transfers. **VOICE FLAGS: none.** The banned-term review is at §5 with its hit table — run, not claimed.*

---

## §1 — COMPONENT 1: THE REPAIR AND THE GATES (P1) — **BRANCH (b)**

**The primary route was built.** xi_n(z) = (1/λ_n)·Σ_j w_j K(z, x_j) xi_n(x_j) —
for any abscissa, inside the interval or outside, **no interpolant anywhere.**
At a node it returns the node value *exactly*, by the eigen-equation. **That
exactness is the whole reason to prefer it, so it was tested first — and it
failed:** max node discrepancy **3.631e+02**.

### **THE CAUSE, MEASURED PER MODE, AND IT IS THE HAZARD I NAMED AT REGISTRATION: THE RELATIVE ERROR TRACKS MACHINE-EPSILON DIVIDED BY λ.**

| n | λ²ₙ | max\|err\| | rel err |
|--:|--:|--:|--:|
| 0 | 9.999e−01 | 2.553e−14 | 1.5e−14 |
| 3 | 3.478e−03 | 3.323e−12 | 9.4e−13 |
| 5 | 5.820e−09 | 2.787e−07 | 6.1e−08 |
| 6 | 2.072e−12 | 1.669e−03 | 3.3e−04 |
| 7 | 4.746e−16 | 1.089e+02 | **0.999** |
| 8 | 3.281e−16 | 3.631e+02 | **1.001** |
| 10 | 2.298e−16 | 2.590e+01 | **1.037** |

**The extension is exact in theory and its numerical error is ε/λ** — excellent
where λ is not at the floor, worthless at the four modes where it is. *I wrote at
registration that the division was "the place the repair can fail, and if it does
the residual will show at the small modes." **It did, and it did there.***
**G2 on this route: 1.056e+07. Fails.**

**The fallback was then built** — spectral reconstruction, **no division by λ
anywhere.** A reading of the original code licensed it and is recorded: the
original uses `left=0.0, right=0.0`, so **the modes are never extrapolated**;
they are evaluated inside [−1,1] and taken zero outside, which is exactly where
a Legendre series is excellent. ### **It fails at the same four modes by a different mechanism** — node error 1.5e−11 at n=0 rising to **83** at n=8. There is no λ to divide by; the failure is that **those eigenvectors are not smooth functions at all.** They are numerical null-space noise, and no polynomial series reproduces noise. **G2: 4.109e−01 against the broken 4.361e−01 — a collapse of 0.03 orders. Fails.**

### **G2 FAILS ON BOTH REGISTERED ROUTES. THE ACT HALTS PER THE REGISTRATION.**

**Two further diagnostics ran, to satisfy the G2 clause's requirement that the
residual's cause be named.** ***I record that these exceed the two registered
routes: they are diagnostics, not candidate repairs, and neither is adopted.***
**(A) Restrict to the evaluable modes** — if the null-adjacent four are the
cause, excluding them should restore stability. **It does not:** 3.643e−01 at
eleven modes, 2.795e−01 at seven, **2.105e−01 at six**, where every eigenvalue is
well separated. **(B) The discontinuous-integrand hypothesis** — the integrand
jumps at |x| = e^−u because of the zero-fill, and a Gauss rule on a jump
converges slowly and non-monotonically, which would explain every route.
Integrating the smooth subinterval with its own rule: **3.684e−01. Not the cause
either.**

> ### ***AND THE FACT THE FOUR ROUTES TOGETHER FORCE, WHICH CUTS AGAINST THIS ACT'S OWN PREMISE.***
> Ψ(0) is **derived, exactly**: A_n(0) = 1 for every mode, e_n(0) = 0 exactly,
> so Ψ(0) = N_even − σ_even·N = **−1.165002987**, and b121 confirmed it at every
> NQ.
>
> | route | Ψ(0) | |
> |:--|--:|:--|
> | original interpolant | **−1.165002987** | ### **EXACT** |
> | spectral | −0.705202223 | wrong |
> | split-integral | −0.479634 | wrong |
> | spectral, 7 modes | −0.315502 | wrong |
>
> **At u = 0 the dilation is the identity and `np.interp` returns the node values
> themselves — the original is exact there, and every replacement re-approximates
> what was already exact.** ***So the replacements are not uniformly better than
> the thing they replace. They are better nowhere that has been demonstrated, and
> worse at the one point where the answer is known.***

## §2 — COMPONENTS 2, 3, 4: NOT PERFORMED

The registration binds: **a G2 failure halts the act.** ### **P2, P3 and P4 are not answered.** Nothing is re-profiled, the one-sign verdict is not re-run, and the dominance question is not re-asked — **there are no repaired samples to re-run them on, and running them on unrepaired samples is the exact error this act was sent to correct.**

***And P4's "no third asking" clause is therefore not spent.*** The question was
never asked on repaired samples, because there are none. **The one asking the
paste allows remains available** — stated explicitly so no later act believes the
allowance was consumed by a halt.

## §3 — THE FILINGS

**b119's dominance verdict keeps its withdrawn-to-basis status exactly.** The
keystone's withdrawal fence stands unchanged; **no restoration record is
written**; the mechanism's status line is untouched. **b117's one-sign verdict
keeps its grade.**

### **AND ONE THING IS NEWLY OPEN THAT WAS THOUGHT SETTLED.** b121 named the dilated-evaluation interpolant as the cause of the 0.4 excursion, on the strength of a truncation test. ***Three independent replacements for that interpolant exhibit the same excursion.*** It may still contribute; **it cannot be the whole of it.** The instability's source is **unlocated and re-opened as a named item.**

**The lane:** the instrument item **stays at the head and is now harder than
b121 left it** — not *"replace a known-bad component"* but ***"find what four
replacements did not change."*** The closed-form crown stands; the re-rerun
revisit stays behind the instrument item and inherits nothing new.

## §4 — THE SEATS

**My P1 expectation — the repair lands, large collapse — MISSED.** I predicted
qualitative collapse and declined to name an order; the collapse was 0.03 orders
on one route and **negative seven** on the other. P2 and P3 are **unscored**, the
components not having run. ***My P4 decline-to-predict is scored as correct in
posture and empty in content:*** the question was not reached, so the decline
cost nothing and proved nothing. The navigator's low-confidence-either-way on
dominance was the right posture for a question that turned out not to be askable.

### **The one thing this act got right in advance was the hazard: the division by λ, named at registration as "the place the repair can fail," failed exactly there and exactly that way.**

## §5 — THE AUDITS

**THE BANNED-TERM REVIEW, WITH ITS HIT TABLE**

```
  stems scanned : gap, blind
  scope         : this act's added lines + the whole of files it creates
  files scanned : 7
  hits found    : 2   (both the artifact naming its own stems)
  corrections made : 0
  VERDICT          : CLEAN
```

**Tags:** the withdrawal fence untouched; b38's verdicts fenced; the
not-adopted diagnostics marked as diagnostics; the unspent P4 allowance stated.
**Grades:** both routes **branch (b)**; the per-mode error **measured**; the
diagnostics **not adopted**; **nothing re-graded in either direction**.
**Scale and floor-axis:** every excursion quoted **with the axis varied (NQ)**;
the multi-axis floor is *not* quoted, because G2 failed and a floor measured on
broken samples would be a number without a meaning.

## §6 — DEVIATIONS

**One, disclosed:** two diagnostics beyond the two registered routes were run,
to satisfy the G2 clause's own requirement that the residual's cause be named.
**Both are recorded as diagnostics, neither is adopted, and neither succeeded.**
No divergence.

## §7 — THE RECORD AND PINS

*Relay: the b124 run-registration + bank + two instruments + this report.
SIDE-global-section: UNTOUCHED (Core 271/271). PLACE-papers: OPEN_TRAILS + the
loom's dated line. Mirror: refreshed — **`mirror-refresh-2026-08-23-m.zip` is the
one to load.***

> **PIN LINE (post-push read-back, ls-remote):**
> `SIDE-global-section origin/main = dc4c32e56275e1251e0daea094ab4167eee289b9`
> (**UNTOUCHED**; Core **271/271**; tag `v0.1.0` = peeled
> `706a81b9e329e220a6448b4296e5cc42c9433670`, unmoved) · `PLACE-papers
> origin/main = a80ae1c89daccb98b97ae1e2926b1fceca285cfe` (parent `e8d7e43`) ·
> `relay origin/main = 2b23c36d2d3d1b4a681de41cc48f5311543f03e5` (this act — the
> registration `5b1bb00` then the act commit, the chain continuous from
> `2b602fe`; pushed from `push-prolate-repair` per Rule 4.10, hook
> content-verified; **HELD ancestry clean** — `6eada6a` at its pinned SHA, NOT an
> ancestor; **carrier files ABSENT from the pushed tree by name, count 0**) ·
> `SIDE-kernel origin/main = 0256e9e`, deposit `v1.5` = peeled `0e5233f`.
> **MIRROR:** `mirror-refresh-2026-08-23-m.zip` built at PLACE-papers `a80ae1c`
> and verified by content (22 files, 0 md5 mismatches; this act's record and
> **both** new conventions lines present inside). *This pin-line commit's own SHA
> is stated in the closing message, per the regress rule.*

## FOOT

**The seventeenth seam close runs at the cadence. ### The re-rerun revisit cannot draft on repaired ground, because there is none** — it stays behind the instrument item, which is now the harder problem of finding a cause that four evaluations did not move. The closed-form crown stands as the research target; the boundary guarded; the desk holds the archival-split and v4.3-splice rulings; the protocol last. The restart kit one document plus the newest mirror.

**`h2` UNCHANGED. THE REGISTER SENTENCE UNTOUCHED. NOTHING PROMOTED.
NOTHING DEPOSITS. NOTHING CIRCULATES.**
