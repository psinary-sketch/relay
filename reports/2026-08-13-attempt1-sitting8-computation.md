# W-ATTEMPT-1 — SITTING 8: THE COMPUTATION

**Relay report · 2026-08-13 · ATTEMPT track · relay-only · sub-gate carried · validated-at-a-point law governing**
### **THE VALIDATION GATE WAS NOT PASSED, SO NO EXTENSION NUMBER IS BANKED — BY THE FERRY'S OWN INSTRUCTION.** **Nothing deposits.**

---

## §1 — WHAT RAN, AND IT RAN CLEANLY

**The prolate layer was built independently rather than taken on supply.** *Sinc-kernel concentration
operator on `[−1,1]`, `c = 2π`, Gauss–Legendre discretization, `n = 400` nodes.*

> ### **CONVERGENCE CHECK: `|ev(400) − ev(600)| = 6.0 × 10⁻¹⁴` over the first eight eigenvalues.** *The
> instrument is converged at the prolate level.*

| `n` | `λ_n` | | `n` | `λ(n) = λ_{2n}` | `λ(n)²/(1−λ(n)²)` |
|--:|:--|:-:|--:|:--|:--|
| 0 | `0.9999427534` | | 0 | ### **`0.9999427534`** | ### **`8733.39`** |
| 1 | `0.9975617082` | | 1 | `0.9593903454` | `11.5675` |
| 2 | `0.9593903454` | | 2 | `0.2746660266` | `0.0815972` |
| 3 | `0.7217515555` | | 3 | `0.0034782381` | `1.2098 × 10⁻⁵` |
| 4 | `0.2746660266` | | 4 | `7.4656 × 10⁻⁶` | `5.574 × 10⁻¹¹` |

**Slepian count `2c/π = 4.0000`.**

### ### **SHAPE CROSS-CHECK: PASSES.** Sitting 5's supplied description — *"three appreciable `λ`, cliff at `n ≈ 3`"* — is reproduced exactly: `λ(0), λ(1), λ(2)` appreciable (`0.99994, 0.95939, 0.27467`), then the cliff (`0.00348`). **An independent construction lands on the supplied spectrum's shape.**

---

## §2 — ### **A CORRECTION TO SITTING 4, AND IT IS THE SITTING'S MOST USEFUL OUTPUT**

**Sitting 4 banked, as its "one real gain":** *"`1 > λ₀(c) > λ₁(c) > ⋯ > 0`, so `1/(1−λ(n)²) ≤ 1/(1−λ₀²) < ∞`
uniformly — **the factor is bounded, the danger sitting 3 flagged does not arise**, and the series is benign."*

> ### **THE COMPUTED VALUE IS `λ(0) = 0.9999427534`, SO THE FIRST COEFFICIENT IS `λ(0)²/(1−λ(0)²) ≈ 8733`.**
>
> ### **BOUNDEDNESS IS NOT SMALLNESS. Sitting 4's inference was formally valid and practically empty — it
> read "finite" and wrote "benign."** *The `n = 0` term of eq (100) carries a weight three orders of
> magnitude above the `n = 1` term (`11.57`) and roughly `750×` its size.*
>
> ### **CONSEQUENCE FOR THE SERIES: convergence of `Qε` cannot rest on the weights. It must rest entirely on
> `C_n(ρ)` being correspondingly small — and `Qε` is, to a first approximation, GOVERNED BY `C_0` ALONE
> unless `C_0` is itself tiny.** *That is a structural statement about the kernel and it was invisible until
> the number existed.*

**Sitting 4's gain is downgraded from `CLEARS` to `FORMALLY TRUE, MATERIALLY MISLEADING`.** *The tertiary
quote it rested on was accurate; the reading drawn from it was not.*

---

## §3 — WHY THE COMPUTATION STOPPED: **`C_n` WAS NOT SUPPLIED**

> **The ferry states:** *"`Qε(ρ) = Σ_n [λ(n)²/(1−λ(n)²)]·C_n(ρ)`, **`C_n` as quoted above**"*.
> ### **THERE IS NO `C_n` ABOVE. The paste references a quotation it does not contain.**

**Without `C_n` there is no `Qε`; without `Qε` there is no `K_I` kernel `(Qε)(exp|v|)/2ε′(1⁺)`; without `K_I`
there is no Toeplitz matrix; and therefore §2's validation, §3's Lemma 5.2 re-derivation, and §4's three
spectra all have no object to act on.** ### **The chain breaks at its first link, and every downstream task
is blocked by the same single omission.**

**`ξ_n^an` is likewise described but not defined** — *"the analytic continuation of the normalized prolate
restriction"* is a characterization, not a formula, and the continuation is exactly the delicate part.

---

## §4 — THE ANCHOR CHECK: ### **INCONCLUSIVE, AND THE REASON MATTERS**

**Supplied anchors:** `Qε(1) = 0` exactly; per-term `t(0) = 11.9719 … t(4) = 0.000125459` summing toward
`ε′(1⁺) ≈ 22.9965`.

**Against my computed weights** (eq-(14) form `λ/(1−λ²)`): `n=0: 8733.9 · n=1: 12.057 · n=2: 0.297 ·
n=3: 0.00348 · n=4: 7.47×10⁻⁶`.

> ### **`t(0) = 11.9719` DOES NOT MATCH MY `n=0` WEIGHT (`8733.9`) AND SITS NEAR MY `n=1` WEIGHT (`12.057`).
> `t(4) = 1.25×10⁻⁴` SITS ABOUT `17×` ABOVE MY `n=4` WEIGHT (`7.47×10⁻⁶`).**
>
> ### **I DO NOT READ THIS AS EITHER SIDE BEING WRONG. I READ IT AS THE `c`-CONVENTION NOT BEING PINNED BY
> THE SUPPLY** — the bandwidth parameter admits several standard normalizations (`[−1,1]` vs `[−½,½]`;
> `sin(c(x−y))` vs `sin(c(x−y)/2)`), and `t(n)` may carry an additional factor beyond the weight.
> ### **THE OFFSET-BY-ONE APPEARANCE IS EXACTLY WHAT A CONVENTION MISMATCH LOOKS LIKE, AND GUESSING WHICH
> CONVENTION CLOSES THE GAP WOULD BE FITTING THE INSTRUMENT TO THE ANSWER.**

---

## §5 — THE GATE, AND WHAT IT FORBIDS

> **The ferry set the gate:** *"no extension number is banked unless this reproduces."*
> ### **THE LOG-2 VALIDATION COULD NOT BE RUN AT ALL — there is no `K_I` to diagonalize. `λmax ≈ 1.05158`,
> `λ₂ ≈ 0.686494`, `λ₃ ≈ 0.0289` and the even/odd parities are NEITHER CONFIRMED NOR CONTRADICTED.**
>
> ### **THEREFORE: NO LOG-3 SPECTRUM. NO CROSSING COUNT. NO ODD-MODE VERDICT. NO `γ` FOR THE LOG-3 CASE. NO
> BRANCH LANDED.** *Tasks 2, 3, 4 and 5 are not attempted rather than attempted-and-failed, and the
> distinction is recorded.*

**The trap stayed armed and untripped:** *Fact 6.1's `τ(λ,α,d,m)` approximation is log-2-specific output and
was never used as an input. There was no temptation to use it, because there was no computation to feed.*

**Sitting 7's parity ledger rides unchanged and is unaffected by the block:** ### **`ĝ(0) = ∫g` is vacuous on
odd directions, so the budget against an odd offender is at most one.** *That result needed no `Qε` and needs
none now.*

---

## CLOSING — REVIEW

**Nothing proof-shaped emerged. No sign step exists to price.** ### **NO SENTENCE ABOUT `W_∞ − W_2`'s SIGN
APPEARS IN THIS REPORT OR ANYWHERE ELSE — the question was never reached.** **Banked to relay only.**

**Returning for the author's word:**
1. ### **THE PROLATE INSTRUMENT IS BUILT AND CONVERGED (`6×10⁻¹⁴`), and independently reproduces the supplied spectrum's SHAPE — three appreciable, cliff at `n = 3`.**
2. ### **SITTING 4's "GAIN" IS CORRECTED BY THE NUMBERS: `λ(0)²/(1−λ(0)²) ≈ 8733`. Bounded is not benign, and `Qε`'s convergence must live entirely in `C_n`.**
3. ### **THE COMPUTATION IS BLOCKED BY ONE OMISSION: `C_n` is referenced as "quoted above" and is not in the paste.** *Every downstream task fails at that single link.*
4. ### **THE ANCHOR CHECK IS INCONCLUSIVE ON A CONVENTION AMBIGUITY, NOT ON A DISAGREEMENT — and I declined to guess the convention that would close it.**

> ### **WHAT IS NEEDED IS SMALL AND EXACT: `C_n(ρ)`'s formula, and the `c`-normalization pinned well enough
> that `t(0) = 11.9719` is reproducible. With those two, §2–§5 run in one sitting on the instrument that now
> exists.**

**`h2` UNCHANGED. NO SIGN. NO MECHANISM CLAIMED. NOTHING DEPOSITS.**
