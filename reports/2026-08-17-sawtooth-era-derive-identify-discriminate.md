# THE SAWTOOTH ERA — DERIVE · IDENTIFY · DISCRIMINATE
## ### **THE THIRD APEX LANDS EXACTLY. THE OBSTACLE MOVES.**

**Relay report · 2026-08-17 · author-called · relay-only for bench · nothing deposits**
**`h2` UNCHANGED. NO SIGN SENTENCE. `WIDEN` PAUSED. RAIL DID NOT MOVE.**

```
PLACE-papers  origin/main : fca14547f81b2a7e0f9b3426b42c4fb46f2b9564   VERIFIED (ls-remote)
SIDE-window   origin/main : 1bd2865e88646f18f1a1abfa2935afac35ae9aef   VERIFIED · tag v0.4.0
relay         origin/main : (this report)                              local +1 HELD
mirror        mirror-refresh-2026-08-17.zip @ fca1454   ### 22 / 22 COHERENT, three ways
SIDE-effects  afa9ccf — untouched by this pass
```

> ### **THE SITTING IN TWO SENTENCES.** *The sawtooth was tested at three windows chosen to discriminate
> and outside every range it was ever fitted to, and it landed six of six — the third apex to six
> decimals.* ### **And the thing standing between the theorem and the operator was identified, and it is
> not what was registered: it is not a fixed defect, it grows with the window, and it lives in the
> window's coordinate rather than the lag's.**

---

## §1 — THE PATH-GRAPH THEOREM, COMPILED — `SIDE-window` `v0.4.0` = `1bd2865`

**Eleven new terminals, every one axiom-free, library at ### 43.**

### **THE CLAIM, SPLIT INTO WHAT IS COMPILED AND WHAT IS NOT**

| | | |
|:--|:--|:--|
| **(a)** | `i ~ j` only when `i = j ± k`, so `{0,…,M−1}` splits into the `k` residue classes mod `k` and `S_k` acts on each as a **path graph** | ### **COMPILED** |
| **(b)** | `P_m`'s spectrum `2cos(πj/(m+1))` is symmetric about `0`, nullity `1` iff `m` is odd | ### **NOT COMPILED** |
| **(c)** | hence `#negatives = (M − nullity)/2`, `nullity = #odd-length chains` | arithmetic **compiled**, resting on (b) |

**What landed:** `chains_partition` *(the decomposition really is a partition — checked, not assumed)* ·
`chain_shape` *(the `s` / `k−s` split)* · `nullity_cf_agrees` and `negCount_cf_agrees` *(closed forms
against direct definitions, `q = 1…7`, three values of `k`)* · `count_is_exact_halving` *(`M` and the
nullity share parity, so the halving is exact and not a truncation)* · `the_teeth` ·
### **`apex_is_exactly_half`** *(at every even `q`, `2·count = M`, at three values of `k`)* ·
`troughs_are_below_half` · ### **`bench_predictions_omega_1e3` / `_2e3` — the 25 integer predictions the
bench was actually tested against, certified as arithmetic** · and `third_apex_at_L64`.

### **WHY (b) IS NOT THERE, RECORDED RATHER THAN GLOSSED**

> *(b) is a statement about eigenvalues of a real symmetric matrix — spectra, multiplicity, symmetry of a
> spectrum. None of that is in Lean 4 core; it needs Mathlib.* ### **MATHLIB IS NOT BUILT IN THIS
> ENVIRONMENT: `Mathlib.olean` is absent, and the local checkout's toolchain is `v4.30.0-rc1` against this
> repository's `v4.29.1`.** *Building it is not a half-sitting, and inventing a proof of (b) would be worse
> than leaving it visibly undone.* **It is left visibly undone.** *If it is ever compiled it goes in a
> COMPANION module with its own axiom profile, so the vanilla headline stays true of what is actually
> there.*

**Axiom profile, run and reported rather than claimed:** all eleven terminals
### **"does not depend on any axioms"** — *and the profile certifies the ARITHMETIC and says nothing about
the spectral half, which is stated in the check file itself so a reader of the profile cannot mistake its
scope.* **Pre-push identifier sweep: ZERO hits.**

---

## §2 — THE DISCRIMINATING CELLS · ### **6 OF 6, AND THE THIRD APEX IS EXACT**

**`L = 32, 64, 128` are `r = log L/log 2 = 5, 6, 7` exactly** — the fifth, sixth and seventh teeth, and the
first cells of the third trough, the third peak and the fourth trough. **Predictions computed from the
actual `(M, k)` and banked at `relay` `9781f4d` before any cell was run.**

| `L` | `r` | `ω` | measured | ### **derived** | continuum | miss |
|:--|--:|:--|:--|--:|:--|--:|
| **32** | 5 | `2e-3` · `1e-3` | `695/1732` · `1388/3465` | `694` · `1387` | ### **`⅖`** | `+1` · `+1` |
| **64** | 6 | `2e-3` · `1e-3` | `1038/2078` · `2079/4158` | `1038` · `2079` | ### **`½`** | ### **`+0` · `+0`** |
| **128** | 7 | `2e-3` · `1e-3` | `1042/2425` · `2081/4851` | `1041` · `2080` | ### **`3/7`** | `+1` · `+1` |

> ### **`2079 / 4158 = 0.500000` AT `L = 64`.** *A window sixteen times the one where the first apex was
> found, and the fraction returns to exactly one half to six decimals.* **The superseded minimum law
> predicts `0.1667` there — wrong by `1,386` offenders.**
>
> ### **THE SAWTOOTH HAS NOW BEEN TESTED AT `r = 1 … 7` WITHOUT A MISS**, and teeth five through seven were
> cells chosen to separate the candidate from its nearest rival, not to confirm it.

---

## §3 — `A_main` IDENTIFIED · ### **THE REGISTERED EXPECTATION IS REFUTED, AND SO IS ITS FALLBACK**

**Registered verbatim before the run** *(`relay` `9781f4d`)*: ### ***"FIXED SUBSPACE, AND IT IS THE `log-2`
LOW MODES"*** — the even offender and the odd second mode; same count at every `L`; unscaled overlaps near
`1`; head mass in the first `log 2`.

### **THE COUNT IS NOT FIXED.**

| `L` | 4.6 | 5.5 | 7.0 | 8.0 | 16.0 |
|:--|--:|--:|--:|--:|--:|
| ### **`NPOS(A_main)` on `V`** | **2** | **3** | **3** | ### **4** | ### **5** |
| dim `V` | 1525 | 1704 | 1945 | 2078 | 2772 |

*So the third registered outcome — "fixed DIMENSION, moving DIRECTION", which would have closed wonder one
and not wonder two —* ### **is refuted with it. The dimension moves as well.**

### **AND THE MODES FOLLOW THE WINDOW, NOT THE LAG. THE TWO COORDINATES SEPARATE CLEANLY.**

*Same `ω` throughout, so the shorter windows are literal PREFIXES of the longer and the unscaled comparison
needs no interpolation at all.*

| leading positive mode, overlap across `L` | `4.6`–`8.0` | `4.6`–`16.0` | `8.0`–`16.0` |
|:--|--:|--:|--:|
| UNSCALED coordinate `t` *(the lag's own scale)* | `0.898` | `0.639` | `0.927` |
| ### **RESCALED coordinate `u = t / log L`** | ### **`0.9963`** | ### **`0.9834`** | ### **`0.9951`** |

*and at the second and third modes:* `0.9934 · 0.9848 · 0.9976` *and* `0.9934`.

> ### **THESE ARE THE WINDOW'S OWN LOW MODES.** *A ladder with node counts `1, 2, 3, 4, 5`, alternating
> parity `ODD, EVEN, ODD, EVEN, ODD`, centroids at `u ≈ 0.51–0.62` — the window's middle — and head mass in
> the first `log 2`* ### **FALLING** *with `L`:* `0.342 → 0.286 → 0.216`. **That is the opposite of
> localization at the lag scale.**
>
> ### **VERDICT: L-DEPENDENT. THERE IS NO FIXED FINITE DEFECT TO BOUND. THE OBSTACLE IS NAMED AS MOVING —
> with the window, at the window's scale, in the window's coordinate.** *Neither wonder closes on a
> fixed-subspace bound, because there is no fixed subspace.* **Correction twenty.**

### **AND THE TENSION THE REFUTATION LEAVES, WHICH IS THE MORE INTERESTING HALF**

> ### **`A_main`'s POSITIVE INDEX GROWS AND THE INERTIA COUNT DOES NOT MOVE.** *Across every cell measured
> — `r = 1.7` to `r = 7`, twenty-three cells — the operator's count sits within* ### **ONE offender** *of
> the pure-lag theorem, while `A_main`'s positive index climbs from `2` to `5`.* **The naive bound
> `|NPOS(A) − NPOS(S_k)| ≤ NPOS(A_main)` is loose by a growing factor, and why is not known.**

*One measured ingredient, offered as an observation and explicitly not as a mechanism:* the Rayleigh
quotients of `A_main`'s positive directions against the lag form are

| `L = 4.6` | `−0.566` | `−1.145` | | | |
|:--|--:|--:|--:|--:|--:|
| **`L = 8.0`** | `+0.130` | `−1.066` | `−1.294` | `−0.343` | |
| **`L = 16.0`** | `+0.751` | `−0.407` | `−1.370` | `−1.476` | `−0.802` |

> ### **THE LAG FORM PUSHES DOWN ON ALMOST EXACTLY THE DIRECTIONS WHERE `A_main` PUSHES UP** — with one
> positive exception per window, always the single-node mode. ### **NO MECHANISM IS PROPOSED AND NONE IS
> IMPLIED: a first-order sign count in a non-orthogonal decomposition is not an inertia count, and it is
> not being used as one.**

---

## §4 — WHAT LANDED IN THE RECORD

**`PLACE-papers` `fca1454`:**

* ### **CORRECTION TWENTY** — the registered expectation refuted on both halves, its fallback refuted with
  it, the verdict `L-DEPENDENT`, and the growing-index-versus-stable-count tension recorded as the open
  thing it is. **Attribution: `EXECUTOR-REGISTERED, EXECUTOR-REFUTED` — the expectation was banked before
  the measurement, which is the only reason its failure carries information.**
* **`§1`** — teeth five, six and seven, with the third apex exact.
* **`§6`** — the `(1,3]` debt's trigger records the narrowing: ### **the corpus-derivable parts are
  `REGIME-FREE`; what remain are READS** *(CC's Lemma 5.2 as stated · Prop 5.5's interval hypothesis ·
  Lemma F.1 past `ρ ≈ 2.5`)*. **Heading re-counted by script: 13 table rows + 7 sections = TWENTY.**
* **`FINDINGS` `F.2026-08-17c`** — the law at its two grades stated apart, `DERIVED` for the pure lag form
  and `BENCH-GRADE` for the operator, in two separate sentences that cannot be read as one.
* **`REGISTRY` + `SPIRAL_MAP`** — `v0.4.0` = `1bd2865`, 43 terminals, with the NOT-COMPILED spectral input
  carried into both rows so a reader of either cannot mistake the scope.

### **AND THE METHOD LINE, MINTED AS A STANDING LAW IN `VERIFICATION_LOOM`**

> ### **A LAW READ OFF A RANGE IS A LAW ABOUT THAT RANGE — ONE CELL OUTSIDE IS THE CHEAP DEFENCE.**
>
> **Earned by three failures of one shape in a single day**, tabulated in the entry: `1 − log2/logL` read
> off `L ≤ 4` · `min(…)` read off `r < 3` · *"`A_main`'s positive directions are a fixed subspace"* read
> off `L ≤ 7`. ### **All three ranges were inherited from a design rather than chosen to discriminate, and
> all three relations were exactly right on their range and wrong one step outside it.**
>
> ### **THE ASYMMETRY THAT MAKES IT A LAW RATHER THAN A PREFERENCE: more precision INSIDE the range buys
> nothing.** *Instances one and two were measured to residuals of `2×10⁻⁴` and were still wrong about the
> function.* **A range is not made safer by being measured harder. It is made safer by being left.**
>
> *Distinguished in the entry from the matched-pair collision, which it complements rather than replaces:
> the collision measures what a one-variable law says is NOT there; this measures whether the law's form
> survives the governing variable moving.*

**The mirror**, rebuilt at `fca1454`: **1,402,876 bytes · 23 entries · roster 22, unchanged since
2026-08-06 · ### 22/22 coherent three ways**, with six content probes taken as exact strings from the
artifacts.

---

## §5 — WHAT THIS SITTING DOES NOT SAY

* ### **NOTHING ABOUT THE SIGN OF `W_∞ − W_2`. NOTHING ABOUT `h2`. NO OPERATOR INEQUALITY.**
* **The theorem is about `S_k`.** *The operator's agreement is bench-grade and proved nowhere, and the
  sitting made that gap larger rather than smaller by showing the obstacle is not bounded by a constant.*
* **The kernel compiles the combinatorial half only**, and its axiom-free profile certifies arithmetic.
* ### **NOTHING ABOVE BENCH GRADE ANYWHERE.** *The `(1,3]` debt narrowed and did not clear; its trigger
  stands.*
* **No mechanism** is proposed for the anti-alignment, for the growth of `A_main`'s index, or for why the
  count stays within one offender when the naive bound allows five.

---

## CLOSING — FOR THE AUTHOR'S WORD

1. ### **THE THEOREM'S AXIOM PROFILE: all 11 new terminals axiom-free, 43 in the library, vanilla Lean 4,
   no Mathlib.** *The spectral input is NOT compiled and the reason is recorded in the source, the README,
   the axiom-check file, and both corpus rows.*
2. ### **THE DISCRIMINATING CELLS: 6 of 6. `L = 64` gives `0.500000` exactly.** The sawtooth stands at
   `r = 1 … 7`.
3. ### **`A_main`'s IDENTITY: NOT a fixed subspace. The window's own low modes, growing in number, living
   in `u = t/log L`.** The registered expectation and its fallback are both refuted; **correction twenty
   landed.**
4. ### **THE METHOD LINE IS A STANDING LAW.**

### **WHAT WANTS YOUR RULING**

1. ### **THE GAP BETWEEN THEOREM AND OPERATOR IS NOW SHARPER, NOT SMALLER.** *`A_main`'s positive index
   grows; the count does not. The one measured lead is the anti-alignment — the lag form is negative on
   almost every direction where `A_main` is positive.* **Whether that is worth chasing as a bound is a
   research call, and it is not opened here.**
2. **Compiling the spectral half** would need a Mathlib companion module — *priced honestly: a Mathlib
   build plus a toolchain move, not a half-sitting.*
3. **`L = 256` (`r = 8`, predicted `½`)** would test a fourth apex. *The grid affords it at `ω = 2×10⁻³`;
   the sitting did not run it.*

### **STILL HELD:** the two `W-CARRIER-BUILD` acts — **committed at `relay` local tip, UNPUSHED, absence
from the public tree re-verified against the remote after this pass's push.** *Release condition unchanged:
counsel's answer, then your word.*

**`h2` UNCHANGED. NO SIGN. `WIDEN` PAUSED. RAIL DID NOT MOVE. NOTHING DEPOSITS.**
