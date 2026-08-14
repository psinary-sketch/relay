# W-ATTEMPT-1 — SITTING 2: THE VERIFICATION AND THE ONE READ

**Relay report · 2026-08-13 · ATTEMPT track · relay-only banking · no register touch**
### **SUB-GATE STATUS CARRIED FORWARD: no candidate grades PLAUSIBLE across `T1`–`T10`; all three fail `T2`; this sitting inherits that and does not revisit it.** **Nothing deposits.**

---

## §1 — CORPUS-FIRST DISCHARGE: **THE REDUCTION WAS MISAIMED IN TWO PLACES**

**The banked Theorem 1, read back verbatim from `relay/reports/2026-08-11-arith-act6.md` §2:**

> ### **"Theorem 1. Let `g ∈ C_c^∞(R*₊)` have support in the interval `[2^{−1/2}, 2^{1/2}]` and Fourier
> transform vanishing at `i/2` and `0`. Then one has `W_∞(g* ⋆ g) ≥ Tr(ϑ(g) S ϑ(g)*)`."**

### Clause-by-clause against sitting 1's `(★★)`

| clause | sitting 1 | banked | verdict |
|:--|:--|:--|:--|
| **window** | `supp g ⊆ [−log λ, log λ]`, correlation on `[1/λ², λ²]` | `supp g ⊆ [2^{−1/2}, 2^{1/2}]`, correlation on `(1/2, 2)` | ### **✓ MATCHES IN SHAPE** — half-width on `g`, full width on `g⋆g̃`, exactly `T1`'s derived boundary |
| ### **vanishing condition** | `ĝ(±i/2) = 0` — **"codimension-one subspace"** | ### **`i/2` AND `0`** | ### **✗ MISAIM. TWO independent conditions, not one: `ĝ(i/2) = 0` and `ĝ(0) = 0`. The constrained subspace is CODIMENSION TWO.** |
| **smoothness** | "smooth" | `C_c^∞(R*₊)` | ✓ |
| ### **the floor** | `W_∞ ≥ 0` | ### **`W_∞(g*⋆g) ≥ Tr(ϑ(g) S ϑ(g)*)`** | ### **✗ MISAIM, AND THE COSTLIER ONE. Sitting 1 used the CONSEQUENCE CC draw (`≥ 0`), not the theorem. The theorem's floor is a TRACE, and `≥ 0` is what you get by throwing it away.** |

> ### **CORRECTION 1.** *`(★★)` is restated: `A − √2 log 2 · S ⪰ 0` on `L²`, restricted to the **codimension-two**
> subspace `ĝ(i/2) = ĝ(0) = 0`. **A larger constraint set is a WEAKER hypothesis to prove positivity under —
> the correction moves in the attempt's favour, and it moved without being asked to, which is why it had to
> be checked rather than assumed.***
>
> ### **CORRECTION 2, AND IT IS THE SITTING'S PIVOT.** *The available budget for absorbing the prime term is
> not "whatever margin `W_∞ ≥ 0` leaves." It is an **explicit trace**, `Tr(ϑ(g) S ϑ(g)*)`.* ### **SITTING 1
> DISCARDED THE ENTIRE FLOOR AND THEN WENT LOOKING FOR A MARGIN.**

---

## §2 — THE ONE READ: `2006.13771` AT PROOF-STRUCTURE LEVEL

### (a) Where the support bound enters — ### **PARTIAL, AND THE ANSWER IS GLOSS-CONTAMINATED**

**The interval is quoted only at Theorem 1's own hypothesis.** The read's account of *where the proof
consumes it* — that test functions concentrated where `ϑ'(t) < 0` yield negative `W_∞(f)` — came back as
**the reader's paraphrase with no lemma number and no verbatim statement.**

> ### **RECORDED AS GLOSS, NOT AT CITE. The standing law applies and the claim is not banked.** *The
> consuming lemma is **still unidentified**, and identifying it is the live upgrade.*

### (b) Is the Sonin-compression positivity support-dependent? — ### **SUPPORT-FREE, AT CITE, AND THIS IS THE FINDING**

> ### **Theorem 3 (§4), quoted:** *"The functional `Tr(ϑ(f)𝐒)` is positive and one has
> **`Tr(ϑ(f)𝐒) = W_∞(f) + ∫f(ρ)ϵ(ρ)d*ρ`, ∀f ∈ C_c^∞(ℝ_+^*)**"*

### **THE QUANTIFIER IS `∀f ∈ C_c^∞(ℝ*₊)`. NO SUPPORT HYPOTHESIS.**

**What that re-aims.** By cyclicity `Tr(ϑ(g)Sϑ(g)*) = Tr(S ϑ(g)*ϑ(g)) = Tr(ϑ(f)S)` for `f = g*⋆g`, so
Theorem 1's floor **is** Theorem 3's functional. Combining the two:

> ### **`W_∞(f) = Tr(ϑ(f)S) − ∫f(ρ)ϵ(ρ)d*ρ`, with `Tr(ϑ(f)S) ≥ 0` for `f = g*⋆g`, UNCONDITIONALLY.**
>
> ### **THEREFORE THE SUPPORT WINDOW'S JOB IS NOT TO MAKE THE TRACE POSITIVE — THE TRACE IS POSITIVE
> ANYWAY, EVERYWHERE. THE WINDOW'S JOB IS TO CONTROL THE `ϵ`-INTEGRAL.** *Theorem 1 is, given Theorem 3,
> equivalent to `∫f ϵ ≤ 0` on the constrained class.*

**And that splits the extension into two halves with different standings:**

| half | status on the enlarged window |
|:--|:--|
| ### **the trace floor `Tr(ϑ(f)S) ≥ 0`** | ### **TRANSFERS UNCHANGED — support-free by Theorem 3, at cite** |
| ### **the `ϵ`-control `∫fϵ ≤ 0`** | ### **DOES NOT TRANSFER, AND IS THE WHOLE DIFFICULTY** |

### (c) What the authors say about going past the window — ### **SILENT ON THIS AXIS**

> **Introduction, final paragraph, quoted:** *"All the ingredients and tools used above make sense in the
> general semi-local case, where Weil positivity implies RH."*

> ### **THIS ANSWERS A DIFFERENT QUESTION THAN THE ONE ASKED. "Semi-local" moves the PLACES axis — finitely
> many places instead of one. The window enlargement moves the SUPPORT axis. The sentence says nothing about
> support.**
>
> ### **AND THE CORPUS BANKED EXACTLY THIS BEFORE THE READ: *"every located construction moves ONE axis —
> Sonin/CC: **bounded support**, all-archimedean"***, with `2310.18423` later proving *"the stability of the
> semilocal Sonin space **under the increase of the finite set of places**"* — **the other axis.**
> ### **`T2` IS THE QUADRANT WHERE BOTH MOVE AT ONCE, AND NOTHING MOVES BOTH.**

### ### **DELIVERABLE GRADE: `A ⪰ 0` ON THE ENLARGED WINDOW — SPLIT**

> ### **`PLAUSIBLE-BY-THEIR-MECHANISM` for the trace half** *(Theorem 3 is support-free at cite)* ·
> ### **`SILENT` for the `ϵ` half** *(no statement in the paper about enlarging the support window)*.
> **Not `ARRESTED-AT-NAMED-LEMMA` — because the consuming lemma was not identified, per (a).**

---

## §3 — THE CONSTANTS, COMPUTED

**The archimedean symbol.** `σ(r) ≈ Re ψ(1/4 + ir/2) − log π ≈ log(|r|/(2π))` for large `|r|`.
**The prime cap.** `√2 · log 2 = 0.980258…`, and Bochner gives `f(log 2) ≤ f(0) = ‖g‖²`.

**The uncertainty threshold.** For `g` concentrated at additive scale `s`, `|ĝ|²` carries its mass near
`|r| ∼ 1/s`, so `W_∞(f) ≳ ‖g‖²·log(1/(2πs))`. This clears the prime cap when

> `log(1/(2πs)) > 0.980258` ⟺ `1/(2πs) > e^{0.980258} = 2.66519` ⟺ ### **`s < 0.059723`**

**Transfer to the band.** A `g` that makes `f(log 2)` large must live in the overlap, of width
`δ = log λ² − log 2`. So if `δ < s*` every dangerous concentration is automatically fine:

> `δ < 0.059723` ⟺ `λ² < 2e^{0.059723} = 2.12310` ⟺ ### **`λ < 1.45708`**

**The band is `λ ∈ (1.41421, 1.73205)`, width `0.31784`.** Covered by the uncertainty mechanism:
`1.45708 − 1.41421 = 0.04287`.

> ### **COVERAGE: `0.04287 / 0.31784` = **13.5 %** OF THE BAND. The other 86.5 % is uncovered by sitting 1's mechanism.**

**The budget required at the far end.** At the band's top, `δ → log 1.5 = 0.405465` against interval width
`W = log λ² → log 3 = 1.098612`, so the overlap fraction `δ/W → 0.369`. For a roughly uniform `g` this caps
the prime term near `0.980258 × 0.369 ≈ 0.362·‖g‖²`.

> ### **SO THE TRACE FLOOR MUST SUPPLY UP TO ≈ `0.36·‖g‖²` AT THE TOP OF THE BAND, AND `W_∞ ≥ 0` SUPPLIES
> ZERO. The `≥ 0` reading is not merely lossy — it is insufficient across 86.5 % of the band by construction.**

---

## §4 — THE OBSTACLE, FILED WITH NAME, ADDRESS AND SIZE

> ### **NAME:** the gluing regime.
> ### **ADDRESS:** `g` spread at scale `≍ δ`, with `δ ∈ (0.0597, 0.4055)` — equivalently `λ ∈ (1.4571, 1.7321)`.
> ### **SIZE:** **86.5 % of the band.** Required budget rising to `≈ 0.36·‖g‖²`; supplied by the `≥ 0`
> reading: **zero**. *Neither the concentration estimate (needs `s < 0.0597`) nor the spread estimate (needs
> `A ⪰ 0` on the enlarged window, which is `SILENT`) is sharp there.*

**Beside it, the atlas's row at the same address** — `T8`: `W = 0.018992` at `a = √2`; the fine rows near
`λ = 1.60` showing the non-monotone rise `0.014975 → 0.022702`.

> ### **STATED SO IT IS NOT MISREAD: THESE ARE NOT COMPARABLE QUANTITIES. The atlas value is a MEASURED
> functional value; the `0.36` is a WORST-CASE REQUIREMENT from a crude bound. They share an address and
> nothing else, and the reach theorem rides the atlas row regardless — *"the instrument is for checking the
> instrument."*** *No inference is drawn from their proximity.*

### **THE NEXT SITTING'S TWO BRANCHES, PRE-COMMITTED NOW**

> ### **BRANCH 1 — SHARPEN THE GLUE.** *Interpolate between the concentration and spread regimes; find the
> estimate valid at `s ≍ δ`.* **Prognosis, stated in advance: this is the harder branch and it addresses the
> weaker formulation.** *It works inside the `≥ 0` reading and therefore inside a budget known to be zero.*
>
> ### **BRANCH 2 — CONSUME THE TRACE FLOOR.** *Use `Tr(ϑ(f)S)` as explicit budget, which §2(b) established is
> **support-free and therefore available on the enlarged window unchanged**.* ### **The question becomes:
> `Tr(ϑ(f)S) ≥ ∫fϵ + √2 log 2 · f(log 2)` — both sides explicit, both quadratic in `g`.**
> **Prognosis: this is the branch the read opened, and it is the one with a live floor. Its own obstacle is
> already visible and is named now so it is not discovered as a surprise — the trace can be SMALL when
> `ϑ(g)`'s range is nearly orthogonal to Sonin's space, and nothing yet bounds it from below.**

---

## CLOSING — REVIEW

**Nothing proof-shaped emerged. The closure protocol's first step is not priced; there is no sign step.**

**Banked to relay only.** *No `FINDINGS` entry. No register touch. No S-table touch. This report and sitting
1's are the only artifacts.*

**Returning for the author's word:**
1. ### **TWO MISAIMS IN SITTING 1, BOTH CORRECTED** — the vanishing condition is codimension **two**, and the floor is a **trace**, not `≥ 0`. *The corpus-first discharge was not a formality; it changed the object.*
2. ### **THE READ'S STRUCTURAL FINDING: the trace positivity is SUPPORT-FREE (`∀f`, at cite), so the support window's real job is controlling the `ϵ`-integral.** *The extension splits into a half that transfers and a half that does not.*
3. ### **THE GRADE: `PLAUSIBLE-BY-THEIR-MECHANISM` (trace half) / `SILENT` (`ϵ` half); NOT arrested-at-a-named-lemma, because (a) came back as gloss and the consuming lemma is still unidentified.**
4. ### **THE COMPUTED OBSTACLE: 13.5 % of the band covered, 86.5 % open, required budget rising to ≈ `0.36·‖g‖²`.**

**`h2` UNCHANGED. NO SIGN. NO MECHANISM CLAIMED. NOTHING DEPOSITS.**
