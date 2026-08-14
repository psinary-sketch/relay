# W-ATTEMPT-1 — SITTING 3: THE ε READ · THE AXIS · THE FLOOR

**Relay report · 2026-08-13 · ATTEMPT track · relay-only · sub-gate status carried**
### **GLOSS-REFUSAL ENFORCED: the read was instructed to return "NOT FOUND" rather than paraphrase. It returned THREE. Those three are recorded as gaps, not filled.** **Nothing deposits.**

---

## §1 — ε AT CONTENT

### What came back at cite

> ### **Equation (14), §4:** *"`ϵ(ρ) = Σ λ(n)/(1−λ(n)²) ⟨ξ_n ∣ ϑ(ρ^{−1}) ζ_n⟩`"*
> with *"refer to Section 4 for the notations and the precise definition of the vectors `ζ_n, ξ_n` in terms
> of **prolate functions**."*

### What came back NOT FOUND — recorded as gaps

| question | result |
|:--|:--|
| a single displayed closed-form definition of `ε` | ### **NOT FOUND** — (14) is a **spectral series**, not a closed form |
| any statement of `ε`'s **sign** | ### **NOT FOUND** |
| any statement that `ε` is explicitly computable | ### **NOT FOUND** |

### The sign, DERIVED — and it reverses sitting 2's framing

**From the two quoted theorems, with `f = g*⋆g` and `Tr(ϑ(g)Sϑ(g)*) = Tr(ϑ(f)S)` by cyclicity:**

> Theorem 1: `W_∞(f) ≥ Tr(ϑ(f)S)` · Theorem 3: `Tr(ϑ(f)S) = W_∞(f) + ∫fϵ`
> ### **⟹ `∫f(ρ)ϵ(ρ)d*ρ ≤ 0` ON CC's CONSTRAINED CLASS.**

> ### **SO ε IS NOT A COST THERE — IT IS A BENEFIT, AND THEOREM 1 IS EXACTLY THE STATEMENT THAT IT IS ONE.**
> *Sitting 2 wrote "the window's job is to control the `ϵ`-integral." **Sharpened: the window's job is to keep
> `∫fϵ` NON-POSITIVE.** The extension's question is not "does the cost stay small" but **"does the benefit
> survive, or does it flip sign past the window."***

**Grade: `DERIVED` from two at-cite theorems. Not quoted, and not banked as CC's own statement.**
*The partial ordering `λ(n) ∈ (0,1) ⟹ λ(n)/(1−λ(n)²) > 0` makes the coefficients positive, but
`⟨ξ_n ∣ ϑ(ρ^{−1}) ζ_n⟩` is sign-indefinite, so **no sign follows from inspecting (14)** — consistent with the
NOT FOUND.*

### Size grade: ### **COMPUTABLE-NUMERICALLY, CONDITIONALLY** — and the bench extension **PRICED, NOT RUN**

*(14) is a series in **prolate spheroidal** data: eigenvalues `λ(n)` and vectors `ζ_n, ξ_n`. Prolate
eigenfunctions and eigenvalues are standard numerics.* ### **Conditions on the price, named in advance:**
*(i) the `ζ_n, ξ_n` definitions in §4 must be read at content — **they were not read this sitting**; (ii) the
series' truncation error must be controlled, and `λ(n) → 0` fast is help for convergence but the
`1/(1−λ(n)²)` factor must be checked near `λ(n) → 1`; (iii) `Tr(ϑ(f)S)` needs its own quadrature.*

> ### **THE PRICE: ~1 sitting to read §4's definitions at content; ~1–2 sittings to build and validate the
> two quadratures.** **DELIVERABLE IF RUN: a budget map of FLOOR (`Tr`) vs COST (`∫fϵ`) across the band's
> test-function family — realization grade.**
>
> ### **AND THE DISCLAIMERS RIDE IT UNCHANGED: the reach theorem (*"the instrument is for checking the
> instrument"*) and `S5`-silence. A budget map is a map. It could not decide the extension even if every
> number came out favourable.**

---

## §2 — THE AXIS IDENTIFICATION: ### **UNRESOLVED — INSUFFICIENT TEXT**

**What the sitting has:** the one semilocal sentence, quoted last sitting — *"All the ingredients and tools
used above make sense in the general semi-local case, where Weil positivity implies RH."*

### **IT CONTAINS NO PRIME-PLACE TERMS. The `{∞, 2}` semilocal trace formula's `p = 2` contribution is not
stated in any text reached, so `SAME-OBJECT-TWO-AXES` / `KIN` / `DISTINCT` CANNOT BE RULED AT CITE.**

> ### **THE CANDIDATE, NAMED AND NOT ASSERTED:** *the ledger's band term is `2·log 2·2^{−1/2}·f(log 2)` — the
> ordinary Weil explicit-formula term at `p = 2`. A semilocal trace formula at `{∞, 2}` would carry a `p = 2`
> contribution of that same classical shape.* ### **THAT IS A RESEMBLANCE OF FORM, AND THE NAME-IDENTITY
> DISCIPLINE FORBIDS PROMOTING IT WITHOUT A TEXT.** **Filed `KIN`-CANDIDATE, UNADJUDICATED. No merge.**

**Route priced, not run:** `2310.18423` (*"stability of the semilocal Sonin space under the increase of the
finite set of places"* — the places axis, already banked) and Connes 1999's trace formula, **for the
semilocal prime-place terms in their own notation.** ~1 sitting.

**Standing correction retained from sitting 2:** *semilocal moves the **places** axis; the window moves the
**support** axis; `T2` is where both move and nothing moves both.*

---

## §3 — THE FLOOR QUESTION, STATED AND WORKED

### 3.1 — The three subspaces, explicit

| | |
|:--|:--|
| ### **SONIN'S SPACE `𝒮`** | ### **AT CITE, quoted:** *"the orthogonal projection `𝐒` of the Hilbert space `L²(ℝ)_ev` of square integrable even functions on the subspace of functions, **which, together with their Fourier transform, vanish identically in the interval `[−1,1]`**"* — i.e. `𝒮 = {h ∈ L²(ℝ)_ev : h ≡ 0 on [−1,1] and ĥ ≡ 0 on [−1,1]}` |
| **`ϑ(g)`'s range** | `ϑ(g) = ∫ g(λ) ϑ(λ) d*λ`, the scaling-action average |
| **the constraint subspace** | `ĝ(i/2) = ĝ(0) = 0` — **codimension two** (sitting 2's correction) |

### 3.2 — The question, posed exactly

> ### **Is `inf { ‖P_𝒮 ϑ(g)‖ : g admissible, normalized }` ZERO or POSITIVE?**
> *Zero ⟹ the floor can vanish and Branch 2 dies as stated, needing `ε`-control instead. Positive ⟹ the floor
> is guaranteed and the extension reduces to comparing two computable constants.*

### 3.3 — What was established this sitting

**RESULT A (pointwise positivity of the floor).** *For every admissible `g ≠ 0`, `ϑ(g)𝐒 ≠ 0`.*

**Argument.** Mellin transform diagonalizes the scaling action: on the Mellin side `ϑ(g)` acts as
**multiplication by `M[g]`**. For `g ∈ C_c^∞(ℝ*₊)`, `M[g]` is **entire**, so it vanishes only on a discrete
set — hence `ϑ(g)` is injective, and `ϑ(g)𝐒 = 0` would force `𝐒 = 0`, false. ∎
### **GRADE: MINE, from `STANDARD-AT-TEXT` ingredients. Elementary, and it settles only the pointwise case.**

**RESULT B (the reduction of the infimum).** *Writing the floor as
`Tr(ϑ(g)𝐒ϑ(g)*) = Tr(𝐒 ϑ(g)*ϑ(g) 𝐒) = ‖ϑ(g)𝐒‖²_{HS}`, and passing to the Mellin side, the floor takes the
form* `∫ |M[g](r)|² ρ_𝒮(r) dr` *where `ρ_𝒮` is the spectral density of `𝐒` in the Mellin representation.*

> ### **THEREFORE: THE INFIMUM IS ZERO IF AND ONLY IF ADMISSIBLE `g` CAN PUSH `|M[g]|²` INTO A REGION WHERE
> `ρ_𝒮` IS ARBITRARILY SMALL. THE FLOOR QUESTION IS A LOWER-BOUND QUESTION FOR ONE EXPLICIT SPECTRAL DENSITY.**

### 3.4 — ### **THE QUESTION IS NOT RESOLVED, AND HERE IS THE MISSING INGREDIENT**

> ### **NO LOWER BOUND ON `ρ_𝒮(r)` OVER THE SPECTRAL RANGE ADMISSIBLE `g` CAN REACH WAS FOUND OR DERIVED.**
> *And there is a structural reason to expect the question to be delicate rather than easy: `𝒮` is the
> orthogonal complement of the **prolate concentrated subspace** — functions living inside `[−1,1]` in both
> position and frequency — and the prolate eigenvalues `λ(n)` (the same `λ(n)` appearing in `ε`'s series
> (14)) **decay rapidly**, so `ρ_𝒮` has a sharp transition rather than a flat floor.*

> ### **HEURISTIC, FLAGGED AS HEURISTIC AND NOT BANKED: `g` whose Mellin mass sits in the prolate-dominant
> region would have a small Sonin component, pointing toward `inf = 0`.** *This is exactly the danger sitting
> 2 named in advance — "the trace can be SMALL when `ϑ(g)`'s range is nearly orthogonal to Sonin's space" —
> and it is now **located** (`ρ_𝒮`'s transition) without being **decided**.*

### 3.5 — Both branches, pre-committed with prognoses

> ### **IF `inf = 0`:** *Branch 2 dies **as stated** — the floor cannot be used as an unconditional budget.*
> **It does not die entirely:** *the floor may still be bounded below **on the constrained codimension-two
> subspace**, which is a strictly smaller family than "all normalized `g`". **That refinement is the salvage
> and is named now so it is not invented later as a rescue.***
>
> ### **IF `inf > 0`:** *the extension reduces to comparing two constants — the floor `c₀` against
> `√2 log 2 · f(log 2) + ∫fϵ`.* ### **AND THE HONEST PROGNOSIS: even then it proves the band only, moves
> nothing on `T2` or `T3`, and remains `S5` work.** *The pre-refusal from sitting 1 stands unamended.*

---

## CLOSING — REVIEW

**Nothing proof-shaped emerged. The closure protocol's first step is not priced; there is no sign step.**

**Banked to relay only.** No `FINDINGS` entry, no register touch, no S-table touch.

**Returning for the author's word:**
1. ### **THE ε VERDICT: form is a PROLATE SPECTRAL SERIES (eq. 14), not a closed form; sign NOT FOUND in text but DERIVED `≤ 0` on CC's class — so ε is a BENEFIT there, and the extension's real question is whether that benefit SURVIVES or FLIPS past the window.**
2. ### **THE AXIS RULING: UNRESOLVED — insufficient text. The `p = 2` resemblance is filed `KIN`-CANDIDATE and NOT merged. Route priced at ~1 sitting.**
3. ### **THE FLOOR QUESTION: reduced to a lower bound on one explicit spectral density `ρ_𝒮`; pointwise positivity proved; the infimum UNDECIDED, with the delicacy located at the prolate transition.**
4. **The bench extension priced (~2–3 sittings) and NOT run, with the reach and `S5`-silence disclaimers riding it unchanged.**

> ### **THE ATTEMPT PROCEEDS WHERE THE MATHEMATICS SAYS: the next honest step is §4 of `2006.13771` at
> content — `ζ_n`, `ξ_n`, and any lower bound CC state for the trace. Three of this sitting's four gaps close
> at that one address, and none of them closes by thinking harder about what is already held.**

**`h2` UNCHANGED. NO SIGN. NO MECHANISM CLAIMED. NOTHING DEPOSITS.**
