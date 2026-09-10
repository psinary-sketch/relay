# SIDE-window

**Lemma A, the window arithmetic, the window ladder, the apex at the square, and the inertia count of the
discrete lag form — as decidable statements about small naturals.**

Vanilla Lean 4 (`v4.29.1`). **No Mathlib, no Batteries, no dependencies of any kind.** Every theorem is
closed by `decide` — except `turn_is_square`, which is one core term-mode congruence, and which is
term-mode precisely so that it stays axiom-free. The whole library is checkable by the Lean kernel alone,
and **all 43 terminals are fully axiom-free** — not `{propext, Classical.choice, Quot.sound}`, but *no
axioms at all*.

```
$ lake build && lake env lean AxiomCheck.lean
'SIDEWindow.lemmaA' does not depend on any axioms
... (43 terminals, all the same)
```

## What is in here

| terminal | statement |
|:--|:--|
| `lemmaA` | `primePowersLE 2 = [2]` |
| `lemmaA_count` | exactly one prime power is `≤ 2` |
| `window_prime_free` | `primePowersLT 2 = []` — the window `(1/2, 2)` carries no prime power |
| `window_one_prime` | `primePowersLT 3 = [2]` — the window `(1/3, 3)` carries exactly one |
| `window_four_has_two` | `primePowersLT 4 = [2, 3]` |
| `window_two_is_maximal_prime_free` | nothing below `2`; something below `3` |
| `window_three_is_maximal_one_prime` | count below `3` is `1`; count below `4` is `2` |
| `primePower_counts` | the counting function tabulated on `2 … 10` |
| `primePowers_below_ten` | `[2, 3, 4, 5, 7, 8, 9]` — `6` is absent, being `2 · 3` |
| `isPrime_examples`, `isPrimePower_examples` | the definitions pinned by examples |

## WHAT THIS KERNEL DOES NOT CLAIM

**Read this before citing anything here.** The same list is carried in the module docstring, so it
travels with the source.

* **It proves nothing about ζ, about `h2`, or about any operator inequality.** This is elementary
  counting of prime powers below small bounds. **Nothing here bears on the sign of `W_∞ − W_2`**, and no
  result may be cited as evidence about it.

* **It proves nothing about real intervals.** The corpus states Lemma A as *"for `λ² ∈ (2,3)` the prime
  side has exactly one term, `p^k = 2`"* — a statement quantifying over a real interval. This library
  proves **the arithmetic residue only**: the prime powers `n ≤ 2` are exactly `[2]`. The step from
  `λ² ∈ (2,3)` to the bound `2` is the observation that a prime power is a natural number and a natural
  number `< 3` is `≤ 2`. **That step is one line of ordinary mathematics and it is not formalized here.**

* **The windows are half-vacuous, and saying so is part of the result.** The corpus writes them
  multiplicatively as `(1/2, 2)` and `(1/3, 3)`. Every prime power is `≥ 2 > 1 ≥ 1/L`, so **the lower
  endpoint never binds**: the whole content lives in the upper bound, and the theorems are stated as
  counts below an integer bound, which is what they are.

* **Maximality over real `L` is not proved.** The two maximality terminals establish maximality **at
  integer bounds only**. Extending to real `L` uses that `L ↦ #{prime powers < L}` is a step function
  jumping exactly at prime powers, hence constant between consecutive ones. **That argument is standard
  and is not in this repository.**

* **`IsPrime` here is trial division, defined in this file.** It is not Mathlib's `Nat.Prime`, and no
  lemma about it is imported or assumed.

## The δ/L law is deliberately absent

The corpus's `δ/L` law — Φ's negative fraction on `V` — is a **conjecture with a measured table**. It is
`MEASURED-AT-BANK`, **never proved**, and every window length it has been measured at lies past the
`(1,3]` range that Lemma 5.2's un-run re-derivation would cover.

**Its statement has moved twice in one day, which is the best reason to keep it out of a kernel.** It was
banked as `1 − log 2 / log L` over `L ∈ {2.2 … 4.0}`; on 2026-08-17 it was restated as
`min(1 − log2/logL, log2/logL)` when the lag branch was first measured; and later the same day that too
was superseded by a **sawtooth** whose first two teeth those branches are. **A Lean file carrying a name
for any one of the three would now be citing a superseded statement.**

**It appears in this repository only as a comment.** There is no definition, no statement and no theorem
about it — because a Lean file containing a *name* for it would invite a citation it cannot support. It
stays in `THE_ATTEMPT_RECORD`, where it is graded.

## The ladder (`v0.2`, `SIDEWindow/Ladder.lean`)

`v0.1` proved the prime-free window `(1/2, 2)` and the one-prime window `(1/3, 3)`. `v0.2` adds the rung
above them and the counting function that generates all three.

| terminal | statement |
|:--|:--|
| `window_two_prime` | `primePowersLT 4 = [2, 3]` — the window `(1/4, 4)` carries exactly two |
| `window_four_is_maximal_two_prime` | `W 4 = 2 ∧ W 5 = 3` |
| `the_window_ladder` | `W 2 = 0 ∧ W 3 = 1 ∧ W 4 = 2 ∧ W 5 = 3` — the three windows in one statement |
| `W_table_low` · `W_table_mid` | `W` tabulated on the rungs `2 … 18` |
| `W_flat_at_six` | `W 6 = W 7` — the first composite that is not a prime power is where the count first fails to advance |
| `W_flat_run_at_fourteen` | `W 14 = W 15 = W 16` — the first flat run of two |
| `primePowers_below_eighteen` | `[2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17]` |

### **`W` HAS NOTHING TO DO WITH THE CORPUS'S `W_2` / `W_∞`**

`W n` counts prime powers below `n`. **The name collision is unfortunate and is flagged in the module
docstring as well as here**, because `W_2` and `W_∞` are the corpus's windowed quantities and **nothing in
this repository bears on the sign of `W_∞ − W_2`.**

**`W` is tabulated, not characterized.** No closed form, no asymptotic, no growth statement is proved or
implied — in particular nothing here is a Chebyshev or prime-counting estimate. That the count is constant
between consecutive prime powers is *visible* in the table and is **not** proved as a general statement;
it is exactly the step needed to lift maximality from integer bounds to real `L`, and it is not taken here.

## The apex at the square (`v0.3`, `SIDEWindow/Apex.lean`)

For each prime `p`, the number `p²` plays **two roles at once**, and this file compiles the arithmetic
half of that coincidence.

* **Role 1 — the branch turn.** For the one-prime-`p` lag form, the lag is `log p` and the room is
  `log L − log p`. They are equal exactly when `log L = 2 log p`, i.e. exactly at `L = p²`.
* **Role 2 — the second ladder rung.** The powers of `p` are `p, p², p³, …`; the second is `p²`, and it
  is the next one to enter a growing window.

**They name the same number.**

| terminal | statement |
|:--|:--|
| `turn_is_square` | `p ^ 2 = p * p` — **the only statement here holding for every `p`** |
| `apex_2` … `apex_13` | `pPowersLT p (p^2) = [p]` and `pPowersLE p (p^2) = [p, p²]`, for `p = 2, 3, 5, 7, 11, 13` |
| `apex_counts` | the same six as counts: one rung below the turn, two at or below it |
| `apex_is_the_entry_point` | `W_p(p²) = 1` and `W_p(p²+1) = 2` — the rung count increments exactly as the window passes `p²` |
| `apex_ladder_is_not_window` | `pPowersLT 2 4 = [2]` but `primePowersLT 4 = [2, 3]`, **and the two are unequal** |
| `apex_window_is_larger` | at `p² = 9` and `25` the full window holds `6` and `13` prime powers against the ladder's `1` |
| `isPowerOf_examples` | the single-prime power test pinned by examples |

### **THIS COMPILES THE ARITHMETIC COINCIDENCE ONLY**

* **Role 1 is not formalized.** "Lag equals room exactly at `L = p²`" is a statement about real
  logarithms. **This library contains no logarithms and no reals.** The step is one line of ordinary
  mathematics and a reader who wants it must supply it.
* **Nothing analytic is proved.** That the negative-direction count of `Φ` actually turns at `L = p²` is
  a **measured** statement about a discretized bench. It is not proved here and **nothing here is
  evidence for it.**
* **The general `p` is proved for one fact only.** `turn_is_square` holds for every natural `p`. Every
  other theorem is `decide` on a concrete `p`. **There is no induction and no general statement about all
  primes**, because `decide` cannot give one and this repository imports nothing that could.
* **The ladder is not the window.** `pPowersLT p x` counts powers of `p` alone; a real window holds the
  powers of every prime below `L`. `apex_ladder_is_not_window` states the difference **as a theorem** so
  it cannot be glossed over.

### **EXECUTOR DISCLOSURE — the axiom print caught a tactic, on its first run**

`turn_is_square` was first written `by rw [Nat.pow_succ, Nat.pow_one]`. That compiles, and it is correct,
and **it costs `propext`** — `rw` goes through `Eq.mpr`. **One tactic would have ended this repository's
headline property**, which is that nothing here depends on any axiom at all. It was caught by
`AxiomCheckApex.lean` on its first run and replaced by a term-mode proof,
`congrArg (fun x => x * p) (Nat.one_mul p)`, which is axiom-free. *Kin: the `v0.1` tabulation error caught
by `decide` at build time. **Both times the instrument this repository exists to run is what found it.***

## The inertia count of the discrete lag form (`v0.4`, `SIDEWindow/Sawtooth.lean`)

Let `S_k` be the `M × M` symmetric matrix with `(S_k)_{ij} = 1` exactly when `|i − j| = k` — the
shifted-correlation form at shift `k` on `M` grid points. The claim this module is the arithmetic half of:

| | | |
|:--|:--|:--|
| **(a)** | `i ~ j` only when `i = j ± k`, so `{0,…,M−1}` splits into the `k` residue classes mod `k` and `S_k` acts on each as a **path graph** | ### **COMPILED HERE** |
| **(b)** | `P_m`'s spectrum `2cos(πj/(m+1))` is symmetric about `0`, with nullity `1` iff `m` is odd | ### **NOT COMPILED** |
| **(c)** | hence `#negatives = (M − nullity)/2`, `nullity = #odd-length chains` | arithmetic **compiled**, resting on (b) |

| terminal | statement |
|:--|:--|
| `chains_partition` | the chain lengths sum to `M` — **the decomposition is a partition, checked** |
| `chain_shape` | with `M = qk + s`: `s` chains of length `q+1`, `k − s` of length `q` |
| `nullity_cf_agrees` · `negCount_cf_agrees` | the closed forms match the direct definitions, `q = 1 … 7`, three values of `k` |
| `count_is_exact_halving` | `M` and the nullity share parity, so `(M − nullity)/2` is exact, not truncated |
| `the_teeth` | `q = 1 → M−k`, `q = 2 → k`, `q = 3 → M−2k`, `q = 4 → 2k`, `q = 5 → M−3k`, `q = 6 → 3k` |
| ### **`apex_is_exactly_half`** | ### **at every even `q`, `2 · count = M`** — the apex, at three values of `k` |
| `troughs_are_below_half` | at every odd `q`, strictly below half |
| `bench_predictions_omega_1e3` · `..._2e3` | the **25 integer predictions the bench was tested against**, certified as arithmetic |
| ### **`third_apex_at_L64`** | at `ω = 10⁻³`, `L = 64`: `M = 4159`, `k = 693`, count `= 2079 = (M−1)/2` |

### **WHY (b) IS NOT HERE, AND IT IS RECORDED RATHER THAN GLOSSED**

(b) is a statement about eigenvalues of a real symmetric matrix — spectra, multiplicity, symmetry of a
spectrum. **None of that exists in Lean 4 core; it needs Mathlib.**

> ### **MATHLIB IS NOT BUILT IN THIS ENVIRONMENT:** `Mathlib.olean` is absent, and the local checkout's
> toolchain is `v4.30.0-rc1` against this repository's `v4.29.1`. **Building it is not a half-sitting, and
> inventing a proof of (b) would be worse than leaving it visibly undone.** *It is left visibly undone.*
> If it is ever compiled it goes in a **companion module with its own axiom profile**, so this library's
> headline — *no axioms at all* — stays true of what is actually here.

### **THE MATHLIB COMPANION, PRICED — NOT BUILT** *(2026-08-17)*

**The statement to compile.** For the `M × M` real symmetric `S` with `S_ij ≠ 0` exactly when `|i − j| ∈ K`,
every `k ∈ K` odd: **(i)** index parity is a bipartition, so `D S D = −S` for `D = diag((−1)^i)`, hence
`spec(S) = −spec(S)` and `#pos = #neg`; **(ii)** for `K = {k}` the components are paths and the rank is
`2·Σ⌊m_r/2⌋`. Together: `inertia = (μ, μ, M − 2μ)`.

**What Mathlib supplies** — *verified by grepping the checkout at `D:\mathlib4` (sources only; not built)*:
`Matrix.IsHermitian` *(`Mathlib/LinearAlgebra/Matrix/Hermitian.lean`)* · the self-adjoint spectral
apparatus `LinearMap.IsSymmetric.eigenvalues` *(`Mathlib/Analysis/InnerProductSpace/Spectrum.lean:277`)* ·
the quadratic-form signature `sigPos` / `sigNeg` *(`Mathlib/LinearAlgebra/QuadraticForm/Signature.lean:65,98`)* ·
`SimpleGraph.adjMatrix`, `SimpleGraph.pathGraph`, `SimpleGraph.IsBipartiteWith`.

**What Mathlib does NOT supply** — *same grep*: ### **no tridiagonal determinant or Chebyshev recursion**
*(`grep -rl "tridiagonal" Mathlib/` returns nothing)* · ### **no path-graph spectrum** *(no file under
`Mathlib/Combinatorics/SimpleGraph/` mentions `eigenvalue`)* · **no rank-equals-twice-matching identity.**

> ### **SO THE COMPANION IS NOT A CITATION EXERCISE. BOTH FACTS WOULD HAVE TO BE PROVED.** *(i) is short —
> conjugate by a diagonal sign matrix, then read off the spectrum. **(ii) is the real cost**: the
> zero-diagonal tridiagonal recursion `D_m = −D_{m−2}`, `D_0 = 1`, `D_1 = 0`, giving `det = 0` for odd `m`
> and `±1` for even, and then a rank argument from principal minors.*

**Toolchain and layout.** This library is pinned at `leanprover/lean4:v4.29.1`; the local Mathlib checkout
is `v4.30.0-rc1` and unbuilt. **The entry cost is a Mathlib build (or cache fetch) plus that move, before a
line of the companion is written.** The companion would be a **separate lake package** depending on Mathlib,
importing `SIDEWindow` and never imported by it, with its own `AxiomCheckSpectral.lean` reporting
`{propext, Classical.choice, Quot.sound}` — because Mathlib content will not be axiom-free.
### **That layout is what keeps this library's headline a true statement about what is actually in it.**
*Rough price: (i) about half a sitting; (ii) one to two sittings for the recursion and its rank consequence,
more if the general matching identity is wanted rather than the path case.*

### **THE `v0.5` TARGET, PRICED — ### AND IT MAY NOT NEED MATHLIB AT ALL**

**The 2026-08-17 two-lag measurement found a stronger statement than the one-lag sawtooth:**
### **`NPOS = μ`, the MAXIMUM MATCHING NUMBER of the shift graph** — measured exactly at four two-lag cells,
with the sawtooth falling out as its one-lag evaluation `μ(P_m) = ⌊m/2⌋`.

> ### **AND `μ` IS COMBINATORIAL, SO IT IS DECIDABLE FOR FIXED `M, k` — no reals, no spectra, no Mathlib.**

**The certificate route, which avoids searching for `μ` in the kernel.** Exhibit two objects and check both
by `decide`: a **matching** `P` (pairwise disjoint edges of the graph) and a **vertex cover** `C` (every edge
has an endpoint in `C`) with `|P| = |C| = s`. Then `μ ≥ s` from `P`, and `μ ≤ s` because **the edges of any
matching are disjoint and each needs its own cover vertex** — a one-line pigeonhole, **not König's theorem**,
so nothing has to be imported or proved about bipartite duality.

| piece | cost |
|:--|:--|
| `isMatching` / `isCover` as `Bool` predicates, plus the graph as an edge list | small |
| certificate pairs for concrete `(M, k)` and `(M, k₂, k₃)`, checked by `decide` | small per cell, but the certificates must be **generated outside Lean** and pasted in — the bench already computes them |
| ### **the general lemma `|matching| ≤ |cover|`** | ### **the only non-`decide` part, and the whole risk** |

> ### **THE RISK IS THE AXIOM PROFILE, AND TODAY GAVE THE WARNING.** *`turn_is_square` cost `propext` from a
> single `rw`, caught by the axiom print on its first run.* **An induction over a list to prove
> `|matching| ≤ |cover|` will almost certainly pull in tactics that do the same.** *So `v0.5` is priced as:
> about one sitting for the definitions and the certificates, plus an open question about whether the
> injection lemma can be written in term mode.* ### **If it cannot, the lemma goes in the companion beside
> the spectral input, and the vanilla library keeps only the `decide`-checked certificates — which is still
> a real statement: "here is a matching of size `s` and a cover of size `s` for this graph."**

**And what `v0.5` would still NOT buy:** the step from `μ` to the eigenvalue count is exactly the spectral
input **(b)** above, which is not here. ### **A certified `μ` is a certified combinatorial number, not a
certified inertia.**

### **AND THE OPERATOR IS NOT THE FORM**

The bench measures `A = A_main + c·(ω/2)·S_k` on a codimension-one subspace, not `S_k`. Its counts agree
with `(M − nullity)/2` **to within one offender** at every window measured, from `r = M/k ≈ 1.7` to
`r = 7`. ### **THAT AGREEMENT IS BENCH-GRADE AND IS PROVED NOWHERE.** `A_main` is measured to have 2–3
positive eigenvalues, so it is not negative semidefinite and no comparison theorem applies. **Nothing in
this module is evidence about the operator.**

**Also not proved:** the general `M`, `k` — every theorem is `decide` on concrete values, and the closed
forms are *checked* against the direct definitions on small cases, not *proved* equal in general. And the
passage from a real window `log L` and a real lag `log 2` to the integers `M`, `k` **is the discretization
itself** and is not formalized.

## Provenance

Sized as the smallest real Lean target of the Phase-2 board, built 2026-08-14; the ladder added the same
day as `v0.2`; the apex added 2026-08-17 as `v0.3`; the lag-form inertia count the same day as `v0.4`.

**Self-contained by construction:** every definition and every theorem used is written in this
repository. It imports nothing beyond Lean 4 core, draws on no private repository, and reproduces no
material from anywhere else in the programme. **Nothing here deposits.**

## Build

```
lake build
lake env lean AxiomCheck.lean
lake env lean AxiomCheckLadder.lean
lake env lean AxiomCheckApex.lean
lake env lean AxiomCheckSawtooth.lean
```
