# W-ATTEMPT-1 — SITTING 5: THE RETRIEVAL BANKS + THE RE-AIM

**Relay report · 2026-08-13 · ATTEMPT track · relay-only · sub-gate carried**
### **THE RETRIEVAL IS NAVIGATOR-SUPPLIED. IT IS BANKED AT THAT GRADE AND NOT AT MINE.** **Nothing deposits.**

---

## §1 — THE GAPS CLOSE — **AT THE GRADE THE SUPPLY CARRIES**

**Supplied by the navigator at `RESEARCH-REPORT` grade: arXiv v1 numbering, quotes verified at PDF, with
the author's own caveats riding — *Selecta renumbers; the 2026 revision calls 6.11 "Theorem 11."***

| item | banked |
|:--|:--|
| `ξ_n`, `ζ_n` | **Prop 4.5, eqs 74/76**; ### **`c = 2π`**, `λ(n) = λ^c_{2n}` |
| the no-support theorem | **Theorem 4.7**, `∀f` quantifier |
| `ε` | series **(84)**; `ε′(1⁺) ≈ 22.9965` (**Lemma 5.4**); six banked `λ(n)` values |
| Sonin | **Def 4.4**, `S(1,1)`; `𝐒` = projection onto the **eigenvalue-1 space of `PP̂P`** |
| the floor with penalty | ### **Theorem 6.11: `W_∞ ≥ Tr − c\|ĝ(0)\|²`, `13 < c < 17`** |
| calibration | ### **Remark 3.9(ii)** — naive estimates fail **inside** `(1/2,2)` |

### ### **THE GRADE, STATED PRECISELY, BECAUSE IT IS NOT MINE TO UPGRADE**

> ### **THESE ARE `FOUND-AT-SOURCE (NAVIGATOR-VERIFIED AT PDF)`, NOT `FOUND-AT-SOURCE (EXECUTOR-READ)`.**
> *The ferry has been wrong once already this session — the `"Weil E2, banked"` pointer did not resolve — and
> the corpus records a prior instance (`draft4.pdf` against `2511.22755`).* **The distinction costs nothing
> to keep and is the only thing standing between a supplied fact and an unchecked one.**

### **TWO ITEMS CORROBORATE INDEPENDENTLY — recorded because corroboration is evidence and assumption is not**

1. ### **The `∀f` quantifier.** *My own sitting-2 read returned* **"Theorem 3 (§4) … `Tr(ϑ(f)𝐒) = W_∞(f) + ∫f(ρ)ϵ(ρ)d*ρ`, `∀f ∈ C_c^∞(ℝ_+^*)`"**. *The supply calls it **Theorem 4.7** with the same quantifier.* ### **Content agrees; the numbering differs exactly as the renumbering caveat predicts. INDEPENDENTLY CORROBORATED.**
2. ### **Sonin's space.** *My sitting-3 read returned the projection onto functions "which, together with their Fourier transform, vanish identically in `[−1,1]`". The supply gives `𝐒` = the **eigenvalue-1 space of `PP̂P`** — vectors fixed by both cut-offs.* ### **THE SAME SUBSPACE, TWO DESCRIPTIONS. INDEPENDENTLY CORROBORATED.**

**Sitting 3's three NOT-FOUNDs and sitting 4's five are re-graded `CLOSED-BY-SUPPLY`** — *not by my reading,
and the truncated-page block of sitting 4 is superseded rather than solved.*

---

## §2 — THEOREM 6.11 SEATED: THE FLOOR, QUANTITATIVELY

> ### **`W_∞(g*⋆g) ≥ Tr(ϑ(g)𝐒ϑ(g)*) − c·|ĝ(0)|²`, with `13 < c < 17`.**
> ### **ON THE `ĝ(0) = 0` CLASS THE PENALTY VANISHES IDENTICALLY AND THE FLOOR IS THE BARE TRACE.**

### **AND THIS RETROSPECTIVELY EXPLAINS SITTING 2's CORRECTION.**

*Sitting 2 found the vanishing condition to be at `i/2` **and `0`** — codimension two, not one — and could say
only that the correction "moves in the attempt's favour."* ### **NOW THE SECOND CONDITION HAS A JOB: `ĝ(i/2) = 0`
kills the pole; `ĝ(0) = 0` kills a penalty of size up to `17·|ĝ(0)|²`. Neither is decoration. The
codimension-two class is exactly the class on which the floor is clean.**

### The floor question's Result B, re-read against the banked spectrum

**`c = 2π ≈ 6.283` — fixed and moderate. Supplied spectrum shape: three appreciable `λ`, cliff at `n ≈ 3`.**

> ### **SITTING 4's CORRECTION SURVIVES AND SITTING 3's HEURISTIC IS PARTIALLY REINSTATED — AND THE TWO ARE
> COMPATIBLE, WHICH IS WORTH SAYING EXACTLY RATHER THAN LETTING ONE QUIETLY WIN.**
>
> * **Sitting 4 was right that Landau–Widom does not apply:** `c = 2π` is fixed, there is no `c → ∞` regime, and the `∼ log c` plunge describes nothing here. ### **CONFIRMED BY THE SUPPLIED `c`.**
> * **Sitting 3 was right that the spectrum has a cliff:** but it is an **empirical feature of the concrete `λ`-list at `c = 2π`**, not an asymptotic transition. ### **REINSTATED AS A FACT ABOUT A FINITE LIST, NOT AS THE MECHANISM SITTING 3 INVOKED.**
>
> ### **NET: the floor is governed by ~3 appreciable eigenvalues. `Result B`'s `∫|M[g](r)|²ρ_𝒮(r)dr` is
> therefore a FINITE-RANK-DOMINATED quantity, not a continuum density problem — which is a materially
> different and easier object than sitting 3 posed.** *The infimum remains undecided; what has changed is
> that it is now a question about a short list.*

---

## §3 — REMARK 3.9(ii) FILED AS CALIBRATION

> ### **NAIVE ESTIMATES FAIL INSIDE `(1/2,2)` — ON THE WINDOW THE FIELD HAS ALREADY PROVEN. THE SONIN
> MECHANISM IS THE ONLY ROUTE EVEN THERE.**

### **SITTING 1's GLUING FAILURE IS RE-GRADED: `EXPECTED-BY-THE-FIELD'S-OWN-REMARK`.**

*Sitting 1 built a concentration/spread argument, found it covered 13.5 % of the band, and filed the
intermediate regime as an obstacle.* ### **Remark 3.9(ii) says that class of argument fails on the EASIER
window. The obstacle was never sitting 1's technique being crude — it is the documented behaviour of naive
estimates in this problem.** *`T8` is annotated at this cite: **the thin margin is not an artefact of the
bench, it is why naive estimation is excluded by the field's own remark.***

> **Recorded without consolation: being wrong in a documented way is still being wrong. The value is that the
> route is now closed by a citation instead of by my own inconclusive bound.**

---

## §4 — THE RE-AIMED TARGET: A FINITE SPECTRAL COMPUTATION

**(a) BOAS–KAC AT `A = 3`.** *`g` on `[3^{−1/2}, 3^{1/2}]`, `f = g*⋆g` on `[1/3, 3]`.* ### **Transfers
verbatim — the factorization is interval-agnostic.** **Grade: `PLAUSIBLE-BY-THEIR-MECHANISM`, supplied.**

**(b) `K_I` HILBERT–SCHMIDT FOR `I = [1/3,3]`.** *By **Thm 3.6**'s own bounded-interval mechanism.* ### **The
mechanism is stated for bounded intervals, and `[1/3,3]` is bounded. `PLAUSIBLE-BY-THEIR-MECHANISM`, now at
cite rather than at hope.**

### **(c) THE OPEN CORE — and it is now ONE finite question**

> ### **§6's TOEPLITZ EIGENVALUE ANALYSIS ON THE WIDER INTERVAL, WITH THE `p = 2` TERM AS A NEW SUMMAND IN
> THE KERNEL.** *The extension is no longer "find an estimate." It is: **compute a spectrum and count.***

**The operator.** `A_I − √2 log 2 · S`, where `A_I` is §6's operator on `I = [1/3,3]` and `S = ½(T_{log 2} + T_{−log 2})`
is the symmetrized translation carrying the single prime term (sitting 1's `(★★)`, unchanged).

### **WHAT "ONLY ONE EIGENVALUE `> 1`" MUST BECOME — written down, with necessity and sufficiency separated**

> ### **NECESSARY: at most TWO eigenvalues of the combined operator exceed the reference level** — because
> the constraint subspace `{ĝ(i/2) = ĝ(0) = 0}` has codimension **two**, and by min–max the constrained
> maximum is `≥ λ₃` of the unconstrained operator. ### **Three or more offenders and the budget is exhausted
> no matter how the constraints are positioned.**
>
> ### **NOT SUFFICIENT, and this is where a naive count would overclaim:** *codimension two removes two
> **specific** directions — the kernels of two **given** functionals — not two arbitrary ones.* ### **SUFFICIENCY
> ADDITIONALLY REQUIRES THE TWO FUNCTIONALS TO BE NON-DEGENERATE AGAINST THE OFFENDING EIGENSPACE.**
> *Interlacing gives `μ₁ ≤ λ₁`, never `μ₁ ≤ 1`, so the count alone proves nothing.*

### **BOTH BRANCHES, PRE-COMMITTED**

> ### **BRANCH A — the count holds at `≤ 2` and the functionals are non-degenerate.** *The extension closes as
> a finite spectral computation.* ### **PROGNOSIS, UNCHANGED FROM SITTING 1 AND NOT SOFTENED BY PROXIMITY: it
> proves the band only. `T2` and `T3` unmoved, permanently. It remains `S5` work, to which `S5`-silence
> applies.**
>
> ### **BRANCH B — widening admits a third offender, or the prime term pushes one up.** *The codimension-two
> budget is exhausted and the extension fails **as stated**.*
> ### **THE SALVAGE, NAMED NOW SO IT CANNOT BE INVENTED LATER AS A RESCUE: further vanishing conditions on `ĝ`
> buy further codimension — but every condition shrinks the admissible class, and a class thin enough to
> carry the count may be too thin to carry Weil positivity's meaning.** ### **THAT TRADE — CODIMENSION BOUGHT
> AGAINST CLASS-RELEVANCE LOST — IS THE REAL BOUNDARY OF THIS ROUTE, AND IT IS THE THING TO WATCH IF BRANCH B
> FIRES.**

**WORKED THIS SITTING: to the statement above and no further.** *The spectrum was not computed. `§6`'s
operator is supplied by name, not read; its kernel, its reference level, and the exact sense of "eigenvalue
`> 1`" are **not in my hands**, and computing against a guessed operator would be worse than not computing.*
### **NAMED NEXT STEP: `§6` at content — the operator's kernel and the exact form of its eigenvalue claim.**

---

## §5 — THE ε-MAP, PRICED FINAL **(NOT RUN)**

**All three sitting-3 conditions now clear at source:** *(i) `ζ_n, ξ_n` at Prop 4.5 · (ii) truncation —
**the cliff at `n ≈ 3` means the series is effectively 3–6 terms** · (iii) `1/(1−λ(n)²)` bounded, already
established at sitting 4 from `1 > λ₀ > λ₁ > ⋯ > 0`.*

> ### **PRICE REVISED DOWN: `~1–1.5 sittings`, from `2–3`.** *The revision is earned, not optimistic — the
> spectral data is **banked** (six `λ` values), the truncation point is **known** (`n ≈ 3`), and
> `ε′(1⁺) ≈ 22.9965` gives an independent check on any implementation.*

> ### **DISCLAIMERS VERBATIM, RIDING UNCHANGED:** *"the bench measures the classical background at a
> precision we can defend; the discriminating regime begins around `n ≈ 10¹⁸` and is unreachable … Nothing
> computed at `n ≤ 300` — or `n ≤ 10⁵` — can be evidence for or against RH. **The instrument is for checking
> the instrument.**"* ### **A FAVOURABLE BUDGET MAP DECIDES NOTHING.**

---

## CLOSING — REVIEW

**Nothing proof-shaped emerged. The closure protocol's first step is not priced; there is no sign step.**
**Banked to relay only.** No `FINDINGS` entry, no register touch, no S-table touch.

**Returning for the author's word:**
1. ### **The retrieval banks at `NAVIGATOR-VERIFIED`, not at executor-read — with two items independently corroborated against my own sittings 2–3, and the numbering discrepancy behaving exactly as the caveat predicts.**
2. ### **Theorem 6.11 gives the second vanishing condition its job: `ĝ(0)=0` kills a penalty up to `17·|ĝ(0)|²`. Sitting 2's codimension-two correction is now explained, not merely recorded.**
3. ### **Sitting 4's correction and sitting 3's heuristic are BOTH right, in different registers — fixed `c` kills Landau–Widom; the cliff is real but empirical. The floor is finite-rank-dominated, which is a materially easier object.**
4. ### **The target is re-aimed to one finite spectral computation — and I have written the necessary condition (`≤ 2` offenders) SEPARATELY from sufficiency (non-degeneracy of the functionals), because the count alone would overclaim.**
5. ### **ε priced down to `~1–1.5` sittings, disclaimers unchanged.**

> ### **THE ATTEMPT IS IN BETTER SHAPE THAN AT ANY PRIOR SITTING AND IS NOT CLOSER TO THE CLAUSE. Both
> statements are true and the second is the one that governs.**

**`h2` UNCHANGED. NO SIGN. NO MECHANISM CLAIMED. NOTHING DEPOSITS.**
