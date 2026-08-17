# SIDE-EFFECTS CLOSE-OUT + THE RESEARCH TURN — CLOSE

**Relay report · 2026-08-14 · author-called · nothing deposits**
**`h2` UNCHANGED. NO SIGN SENTENCE. `WIDEN` PAUSED.**

```
PLACE-papers  origin/main : f638cf166120e3c4f995d0641a9fc49ff41e6e7e   (private)  VERIFIED
SIDE-window   origin/main : 612d223f0eea74e61a6f1a38133d2ee415ce01a8   (PUBLIC)   VERIFIED
SIDE-window   tag v0.2.0  : 612d223  (v0.1.0 = ecd5cf7 still live)                VERIFIED
SIDE-effects              : w-ladder-skeleton a0dc376 — TREE NOW CLEAN, unmerged
mirror                    : 22 / 22 rows COHERENT at f638cf1
relay         origin/main : (this report)                              local +1 HELD
```

---

## §1 — SIDE-EFFECTS CLOSE-OUT

### **(a) THE TWO STALE ROWS, CORRECTED**

`VERIFICATION_LOOM` L106–107 now say what is true: `grh_exclusion` and `no_ls_zero` are ### **RETIRED by the
`W-2` withdrawal** *(executed 2026-06-16; landed on `main` 2026-07-13; `Structural.lean` 34 declarations → 3)*,
present only at the historical tag `phase-1.5-module-1-v2`, and ### **cited by zero manuscripts.**

> ### **BOTH ROWS SAID `⊘ scaffold-pattern` FOR TWO MONTHS AFTER THE DECLARATIONS WERE DELETED.** *A `⊘`
> grade reads as "present, and weak" — it tells a reader a terminal exists and does not carry its claim. The
> truth was stronger and simpler: **the terminals were withdrawn outright, and the withdrawal is the repair.***

### **THE DEFECT CLASS, FILED WITH THEM:** ### **A STATUS COLUMN CAN GO STALE IN THE DIRECTION OF
UNDERSTATING A REPAIR — AND THAT DIRECTION IS THE ONE NOBODY RE-READS.** *An overstated claim invites
challenge. An understated one looks like ordinary caution, and sits.* **Found while preparing a ruling that
assumed these rows were current** — which is how the whole `SIDE-effects` detour began.

### **(b) THE SIX SAVE-STATES, DELETED**

`AxiomCheckM1.lean` · `README.md.bak` · `Milestones.lean.bak` · `Structural.lean.bak` / `.bak2` / `.bak3`
— **23,947 bytes total**, all content-verified as post-retirement duplicates of the landed withdrawal
*(each `Structural.lean.bak*` carries 3 declarations and neither retired terminal)*.
### **`SIDE-effects`' working tree is clean for the first time since April.**

### **(c) THE MERGE QUESTION — PREPARED, NOT RULED**

| | |
|:--|:--|
| shape | ### **CLEAN FAST-FORWARD** — `main` has nothing the branch lacks |
| commits | `59c6ec3` (skeleton) · `a0dc376` (root-wiring) |
| ### **what merging ADDS to the public default branch** | ### **exactly 149 lines: `SIDEEffects/ExhaustivenessLicense.lean` (148) + one `import` line. Nothing is modified, nothing removed.** |
| `sorry` / `fun _ => True` / `:= True` in the added file | ### **ZERO** |
| axioms | axiom-free *(re-verified post-wiring at `a0dc376`)*; core Lean only, no Mathlib, no `native_decide` |

**What the file is:** a four-grade ladder of exhaustiveness licenses — `theorem_` (Ostrowski-class) >
`search` (Hodge-class) > `forcedOrUnderdetermined` (T7-class) > `none` — with `Grade.rank` a **function**, the
order **derived** from it, the ladder facts **proved**, and each corpus instance's grade ### **computed by
`decide`/`rfl`, never asserted.**

> ### **AND THE POINT THAT DECIDES THE RECOMMENDATION: THIS FILE ALREADY DOES, CORRECTLY, THE EXACT THING
> RULING 1 ASKED ME TO DO TO THE RETIRED TERMINALS.** *`EDifficultyTop` — the E-Difficulty biconditional —
> is carried as a **named premise**, labelled* `INTERFACES` *in its own docstring, and* ### **never proved
> here.** *That is route (i) executed properly: content named as a hypothesis, with the bridge declared open,
> in a file where the surrounding grades are computed rather than stipulated.*

### ### **RECOMMENDATION: MERGE.**

**Four reasons, and one honest reservation.**

1. ### **It is purely additive to a public branch** — 149 lines, zero modifications, zero deletions.
2. ### **It carries no scaffold of the retired kind** — no `sorry`, no `True`-stub, no opaque-Prop template.
3. ### **It is the corrective example.** *The repository's public face currently records a withdrawal — what
   was taken away. This adds what the discipline builds when applied properly, in the same repository, which
   is the more useful thing for a stranger to find.*
4. ### **The non-default-branch disclosure rule stops applying to it.** *Every citation to a terminal on
   `w-ladder-skeleton` must currently carry a checkout instruction; merging retires that obligation instead
   of propagating it.*

**THE RESERVATION, STATED RATHER THAN BURIED:** ### **the branch was `HELD` deliberately, and I do not know
what the hold was for.** *The commit messages say "Branch held" without saying against what. If the hold was
awaiting the E-Difficulty bridge — the one open premise in the file — then merging publishes a ladder whose
top rung is still open, which the docstring discloses but a casual reader may not weigh.* ### **THAT IS THE
AUTHOR'S CALL AND IT IS WHY THIS RETURNS AS A RECOMMENDATION RATHER THAN AN ACT.**

---

## §2 — EXPERIMENT TWO: ### CONFIRMED · the lattice capstone

*Full grading appended as an ADDENDUM to `phase2/method/THE_EULER_SPECIFICATION.md`.*

**One object. Two decompositions. `K = ℚ(√−23)`, `h = 3`** — ### **the corpus's own witness**, the field
whose class-number-3 Epstein `Z_Q` this programme located an off-line zero in, by its own instrument.

| | **BASIS A — Epstein / forms** | **BASIS B — Hecke / class characters** |
|:--|:--|:--|
| recombination | `Σ_Q Z_Q = w · ζ_K` | ~~`Π_ψ L(s,ψ) = ζ_K`~~ **[struck 2026-08-17, correction twenty-three: false at `h > 1` — the product is `ζ_H`, the Hilbert class field's zeta; `ζ_K` is the `ψ₀`-factor. Counterexample at this witness's own field: `2` splits into two non-principal primes, so the coefficient of `2^{−s}` is `2` in `ζ_K` and `(1+ω+ω²)·2 = 0` in the product. See `THE_ATTEMPT_RECORD` correction twenty-three; per-piece grades unchanged.]** |
| ### **`S1b` (monoid)** | ### **`VACUOUS`** | ### **PRESENT** |
| ### **`S4` (multiplicativity)** | ### **ABSENT** | ### **PRESENT** |
| ### **placement, at cite** | ### **OFF-LINE ZEROS KNOWN** *(Davenport–Heilbronn 1936; Voronin 1976; and this corpus's own located zero)* | ### **NONE KNOWN; GRH OPEN** |

> ### **THE PATHOLOGY LIVES EXACTLY IN THE MONOID-BREAKING BASIS.** *Same field, same `𝒪_K`, same class
> number, same analytic pipeline. The two decompositions differ in one thing — whether the pieces respect the
> monoid — and the off-line zeros appear precisely where they do not.*

### **WHY THIS IS AN UPGRADE AND NOT A REPETITION.** *The 2026-08-13 finding was graded `OURS`,
question-grade, because it compared `Z_Q` **across** to `ζ_K` — and a sceptic may always answer that two
different objects may simply behave differently.* ### **HOLDING THE OBJECT FIXED AND VARYING ONLY THE
DECOMPOSITION REMOVES THAT ANSWER.** **The registered refutation condition — one Hecke row with off-line
zeros at cite — did not fire.**

**FOUR LIMITS, NAMED:** it is ### **not a theorem** *(one field, one grading, structural not general)* ·
### **"no known off-line zeros" is not "no off-line zeros"** — *GRH is open for these `L(s,ψ)`, so the
asymmetry is between a **proved presence** and an **open absence**, and reading it as two proved facts
overstates it by exactly one open problem* · **nothing about ζ, nothing about `h2`** · ### **the mechanism is
exhibited, not explained** — *why breaking the monoid should move zeros off the line is the question this
leaves open.*

---

## §3 — EXPERIMENT THREE: `SIDE-window` `v0.2.0` = `612d223`

**Nine new terminals, all axiom-free; the kernel is now 20.** The two-prime window `(1/4, 4)`;
`window_four_is_maximal_two_prime : W 4 = 2 ∧ W 5 = 3`; `the_window_ladder` in one statement; `W` tabulated
on rungs `2 … 18` with its flat steps isolated (`W 6 = W 7`, and the first flat run `W 14 = W 15 = W 16`).

### **EVERY TABULATED VALUE WAS INDEPENDENTLY RECOMPUTED OUTSIDE LEAN BEFORE LANDING — 17/17 AGREE.**
*The `v0.1` build caught one of my arithmetic slips with `decide`; this time the cross-check ran first.*

> ### **`W` HAS NOTHING TO DO WITH `W_2` / `W_∞`** — flagged in the module docstring **and** the README,
> because the collision is real and a reader skimming for `W` would land wrong. ### **`W` IS TABULATED, NOT
> CHARACTERIZED**: no closed form, no asymptotic, no growth statement, nothing Chebyshev-shaped. *That the
> count is constant between consecutive prime powers is **visible in the table and not proved** — and that is
> exactly the step that would lift maximality from integer bounds to real `L`.*

---

## §4 — EXPERIMENT ONE: ### THE MEASUREMENT COULD NOT RUN

### **THE SITTING-12 INSTRUMENT WAS NEVER BANKED.**

*The twenty sittings of 2026-08-13 produced **twenty-four relay reports and not one line of code or data**.
Nothing under `relay/tools` postdates 2026-08-12. `find` over the whole relay tree for anything written on
2026-08-13 returns **reports only**.*

**The matrix `G` whose negative eigenvalues the `δ/L` law counts is *described* — `Φ ≤ 0 ⟺ ηᵀGη ≥ 0`, grid
`dim = round(log L / ω)`, lag at `log 2`, `ω = 10⁻³` — and ### never defined.**

> ### **A LAW FILED AT `MEASURED-AT-BANK` HAS NO BANK.** *`δ/L` cannot be re-measured, re-fitted, extended to
> new `L`, or checked — by anyone, including its author.*
>
> ### **I DID NOT RECONSTRUCT `G` FROM PROSE.** *A reconstruction would be a **different operator**, and its
> agreement or disagreement with the banked numbers would be uninterpretable — the "stable, plausible, and
> false ledger" sitting 12 itself refused to produce when it declined the `ζ_n` transport under time
> pressure. **Declining the same way, for the same reason.***
>
> ### **THE LOOM'S OWN LAW COVERS THIS AND HAD NEVER BEEN POINTED AT IT: *untracked artifacts are outside the
> apparatus.* The scar it was written for was a stale backup. This is the same law meeting a MISSING
> ORIGINAL** — *and the missing original is load-bearing for the era's headline law.*

### **WHAT THE SITTING DID INSTEAD: COMPUTED THE REGISTERED PREDICTIONS EXACTLY, BEFORE ANY INSTRUMENT EXISTS**

*A room for lag `ℓ` has fraction `1 − ℓ/log L` — the sitting-12 law at `ℓ = log 2`. The ferry's `E1-union`
combines rooms "suitably … additively".* ### **THAT PHRASE IS THREE DIFFERENT PREDICTIONS, so all three are
registered rather than one chosen silently:**

| `L` | rooms *(stated rule)* | ### single-lag | ### U1 nested | ### U2 independent | ### U3 additive |
|:--|:--|--:|--:|--:|--:|
| 3.2 | `log 2` | 0.40408 | 0.40408 | 0.40408 | 0.40408 |
| 3.6 | `log 2` | 0.45887 | 0.45887 | 0.45887 | 0.45887 |
| 4.0 | `log 2` | 0.50000 | 0.50000 | 0.50000 | 0.50000 |
| 4.4 | `log 2, 2log 2` | 0.53216 | 0.53216 | 0.56226 | 0.59649 |
| 5.0 | `log 2, 2log 2` | 0.56932 | 0.56932 | 0.62904 | 0.70797 |
| 6.0 | `log 2, 2log 2` | 0.61315 | 0.61315 | 0.70069 | 0.83944 |
| 9.5 | `log 2, 2log 2, log 3` | 0.69211 | 0.69211 | 0.90748 | ### **1.00000** |

### **THREE DESIGN FINDINGS, ALL RETURNED UNRESOLVED**

1. ### **`U1` (nested) IS IDENTICAL TO THE EXISTING LAW AT EVERY `L`.** *If the rooms nest — which "the
   portion of the window in which the lag has room to act" implies, since the largest room contains all the
   others — then the union **is** the largest room, and `E1-union` is not a generalization at all.* **It
   predicts nothing new, ever.** *That cannot be the intended reading, and it is the one the geometry gives.*
2. ### **THE FIRST THREE `L` VALUES TEST NOTHING.** *Under the stated rule `L = 3.2, 3.6, 4.0` carry ONE
   room, so all three readings collapse. **The design only discriminates from `L = 4.4`** — three of seven
   points are spent confirming the old law.*
3. ### **THE LAG RULE AND THE ARITHMETIC DISAGREE.** *The rule admits `log 3` "once `L > 9`". The prime-power
   reading — one room per prime power `p^k < L`, which is what `SIDE-window` now compiles — puts **`3` in the
   window as soon as `L > 3`**, with `9 = 3²` entering at `L > 9`.* **Both tables are computed and banked.**
   *Under the prime-power rule `U3` already saturates at `L = 5.0`.* ### **The discrepancy is named, not
   silently resolved — resolving it is choosing the experiment.**

### **NO MEASURED NUMBER APPEARS ANYWHERE IN THIS SECTION. NOTHING WAS FABRICATED TO FILL THE TABLE.**

---

## CLOSING — FOR THE AUTHOR'S WORD

1. ### **CLOSE-OUT DONE** — rows corrected, save-states gone, tree clean. **MERGE RECOMMENDED**, with the
   hold's original purpose named as the one thing I cannot check.
2. ### **EXPERIMENT TWO CONFIRMED** — the lattice has its capstone, and the upgrade from question-grade is
   structural: the object is held fixed.
3. ### **EXPERIMENT THREE LANDED** — `v0.2.0`, 20 axiom-free terminals, cross-checked before landing.
4. ### **EXPERIMENT ONE BLOCKED** — and the blockage is worth more than the measurement would have been:
   ### **the era's headline law is unreproducible, and nobody had noticed.**

### **WHAT I WOULD PUT NEXT, IF ASKED**

> ### **BANK THE INSTRUMENT BEFORE EXTENDING THE LAW.** *Re-deriving `G` from the mathematics — not from the
> reports' prose — and checking it reproduces the five banked points at `L = 2.2 … 4.0` would turn `δ/L` back
> into a measurable quantity and make Experiment One runnable as designed.* **Until then the two-prime room
> cannot be entered, because the one-prime room's instrument no longer exists.**

### **STILL HELD:** the two `W-CARRIER-BUILD` acts — committed at `relay` tip, unpushed, absence from the
public tree re-verified. **Release condition: counsel, then your word.**

**`h2` UNCHANGED. NO SIGN. `WIDEN` PAUSED. NOTHING DEPOSITS.**
