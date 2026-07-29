# h2 chain completion — the composite register claim under test — 2026-07-29

READ AND REPORT ONLY; no edits; RH rail read-only. The composite claim under test (SURROUND §0):
> "the programme's monograph argues the *discharge* of this premise — **the two-input Tate argument for
> Conservation of Spectra, and the per-class analyses that carry `covers_all` into the strip**."

Each remaining input tested against `ConservationHypothesis` (v1.3 `0bc21c0`):
`∀ σ, is_xi_zero σ → ∃ p hp, (prime_as_real p hp)^(-σ) = (prime_as_real p hp)^(-(1-σ))`.

## (1) Chapter 15 — the per-class theorems, verbatim, and the quantifier structure

Chapter 15 §15.3 states its object plainly: *"Each of the seven mechanism classes is checked in turn for
one thing: whether it produces a zero of ξ off the critical line."* The per-class verdicts, verbatim:

- **C₁ (Schwarz).** *"…relates ξ at s₀ to ξ at s̄₀ — again, different points. **No off-line mechanism.**"*
- **C₂ (Euler balance).** *"p^(−σ) = p^(−(1−σ)) if and only if σ = 1/2. The balance condition identifies the
  critical line. It produces no off-line zeros because the balance explicitly fails at σ ≠ 1/2. **Produces
  on-line identification. No off-line mechanism.**"*
- **C₃ (functional equation).** *"…Off-line, no such coincidence. **Produces on-line zeros. Does not produce
  off-line zeros.**"*
- **C₄ (PSL₂).** *"Both spectral components are confined to σ = 1/2 … **Identifies on-line. Cannot produce
  off-line zeros.**"*
- **C₅ (Self-adjointness).** *"…forces eigenvalues to be real and non-negative, which corresponds to
  σ = 1/2 … **Identifies on-line. Cannot produce off-line zeros.**"*
- **C₆ (Cauchy-Riemann).** *"Couples DERIVATIVES, not values … **No off-line mechanism.**"*
- **C₇ (Hadamard product).** *"…It cannot be the ingredient that enforces RH … **Encodes. Does not produce
  off-line zeros.**"*
- Summary table (§15.3): every row *"Produces off-line zero? **No.**"*

**Quantifier structure — the decisive point.** Each theorem is *"class Cᵢ does not produce an off-line
zero"* — i.e. **∀ C ∈ classes, ¬(C produces an off-line zero)** — quantified **over classes**, not over
ξ-zeros. `ConservationHypothesis` is **∀ ξ-zero, ∃ a prime** at which the balance holds — quantified **over
zeros**, with an existential-prime *forcing*.

**Entailment (alone, or jointly with Chapter 13): NO.** Chapter 15 establishes the per-class *exclusion*
direction; `ConservationHypothesis` (equivalently `covers_all`) is the *coverage/forcing* direction —
*"every off-line zero is produced by some catalogued class"* — the converse quantifier, which the per-class
analyses do not touch. **The missing step is explicit in the monograph** (assembly step (9)): *"The step from
per-class to all-combinations exclusion is then two claims, and honesty separates them"* — the **identity**
(every zero participates, *"sound and classical … shared with Epstein"*) and the **sign** (*"that this
participation forces σ = 1/2 is the one open clause … λ_Z(n) ≥ −λ_A(n) for every n … the all-n tail
open"*). Chapter 15 gives the exclusion over classes; the coverage/forcing over zeros is the open node.
Even C₂ — whose statement `p^(-σ)=p^(-(1-σ)) ⟺ σ=1/2` is the balance biconditional — asserts only that C₂
*"produces on-line identification, no off-line mechanism,"* **not** that every ξ-zero forces that balance at
some prime; the biconditional is the *condition*, not the quantified forcing over the zeros.

## (2) The "two-input Tate argument" — same proposition as Chapter 13, or distinct?

**Same proposition as Chapter 13's s-Darkness Theorem** — not distinct. SURROUND §0 names *"the two-input
Tate argument **for Conservation of Spectra**,"* and that argument is exactly §13.2–§13.3: *"the Tate
integral … takes two inputs: the test function Φ (determined by C¹_ℚ, hence s-independent) and the kernel
t^s (the sole source of s-dependence). The product formula contributes Φ."* The monograph confirms the
identification at §27.3 register 2: *"Chapter 13's Conservation of Spectra Theorem — the s-darkness of the
product formula … is the unconditional conservation certificate that shapes and motivates it, **but does not
discharge it**."* So the "two-input Tate argument" was already tested in the Chapter 13 read (`91b7da9`): it
is the seal, and it does not entail `ConservationHypothesis`. *(Tate also verifies **Determination** — "ξ
assembled from ℚ with no external input" — a distinct role; but SURROUND §0's "for Conservation of Spectra"
is the s-darkness one, and Determination is likewise a sealing/tracing fact, not a per-zero forcing.)*

## (3) §27.3 — the five registers, verbatim, each carried open

> **First:** the *universality hypothesis* carried by the Universal Silence Theorem … *"the hypothesis is
> load-bearing; removing it from the proof of `silence_universal` leaves an unsolved goal."*
> **Second:** `ConservationHypothesis` … *"every ξ-zero forces the Euler balance equation at some prime …
> This proposition is the premise itself, stated at the multiplicative place: Chapter 13's Conservation of
> Spectra Theorem … is the unconditional conservation certificate that shapes and motivates it, **but does
> not discharge it**."*
> **Third:** *"the totality of the realization of mechanisms through places … 'if an off-line zero existed,
> some mechanism would produce it' … **what remains open is not the theorem but this totality premise it
> consumes**."*
> **Fourth:** *"the distance between balance and positivity at the multiplicative place. The catalogue
> certifies balance … while the explicit-formula and Li's-criterion formulations require positivity: λ_n ≥ 0
> for every n … the premise is the inequality λ_Z(n) ≥ −λ_A(n)."*
> **Fifth:** *"the spectral-realization distance … the output-stage claim, that the zeros themselves are the
> spectrum of a self-adjoint operator with a positive pairing, is the Hilbert–Pólya realization, **which
> this programme explicitly disclaims asserting**."*

*"These are one premise in five registers … A reader who discharges any one of them discharges all five.
This is the arithmetic clause."* §27.3 states its own status twice: *"**None of this discharges h2**"* and
*"The premise is RH-equivalent, and this monograph does not obscure that … The premise stands open on the
other side of that line."* **No register asserts discharge; two (2nd, 5th) explicitly assert non-discharge.**
The v5.13 compression names the residue as *"a positive space on the zeros … the space is the wall"* — the
same object as the Chapter 13 read and `e16b615`.

## (4) Corpus-wide discharge search — result: no (iii) discharge claim exists

Grepping every paper for prove/discharge/establish/close applied to
`ConservationHypothesis`/conservation-premise/`covers_all`/`h2`. Every relevant hit, classified:

| hit (verbatim claim) | class |
|:--|:--|
| `SIDE_EXCLUSION.md:23` — *"the Riemann Hypothesis is proved **under the exhaustiveness premise `h2`** (goal ⇐ h1 ∧ h2, only `h2` open)"* | **(ii) reduction** — RH *under* h2, h2 open |
| `THE_LOAD_BEARING_MAP.md:42` — RCURVE *"exhaustiveness premise `h2` — research-reach"* | **(ii)** — open/research-reach |
| `PATHS:313` — goal-state row *"conditional-A (on h2) → **discharge h2** … h2 open"* | **(ii)** — "discharge h2" named as the *open target*, not achieved |
| `BALANCE_AND_POSITIVITY.md:335` — *"Only `T3′` closes it, and only under h1 and h2 — **which are the premise, restated, not a proof of it**"* | **(ii)** — closes *under* the premise |
| Chapter 13 §13.2–13.3 / (9) / §25.5 / §27.3 reg.2 / Chapter 28.1 — s-darkness "certificate that motivates … not its discharge" | **(i) seal** |

**Zero (iii) actual-discharge claims.** The strongest statements are explicit *non-*discharge (*"does not
discharge it," "None of this discharges h2," "not its discharge," "the premise stands open"*). Nothing to
test further.

## (5) The negative, verified — is "Chapter 13 + Chapter 15" ever asserted to close the premise?

**No.** The nearest is assembly step (9): *"**Under that clause** the coincidence is excluded and the
syllogism closes; the proof carries the identity soundly, localizes the sign, and claims no more"* — the
syllogism closes only **under the open sign clause** (λ_Z(n) ≥ −λ_A(n)), not on Chapter 13 + Chapter 15
alone. Chapter 28.1 is explicit: *"Conservation of Spectra from Tate's thesis (Chapter 13) — the certificate
that motivates Route 3's hypothesis, which is itself the one open premise of §27.3, **not its discharge**;
exhaustiveness from Ostrowski (Chapter 15)."* Chapter 15's own §15.3 uses Chapter 13 only as the *seal*
(*"no structural force outside ℚ's field structure acts on the zeros"*). The two are the surround and the
per-class exclusion; the coverage/forcing premise sits open beside them.

## Conclusion (for the author's register decision)

The composite claim — **two-input Tate (= Chapter 13 s-darkness) + the per-class analyses (Chapter 15)** —
does **not** discharge `ConservationHypothesis`. The two-input Tate is the *seal* (a per-place structural
certificate); Chapter 15 is the *exclusion over classes*; **neither, alone or jointly, supplies the
coverage/forcing over ξ-zeros** that `ConservationHypothesis` asserts (∀ zero, ∃ activating prime). The
missing step is the open **arithmetic clause** — the positive forcing / `λ_Z(n) ≥ −λ_A(n)` for all n / *the
positive space on the zeros* — RH-equivalent and research-frontier, exactly as the Chapter 13 read
(`91b7da9`) and `e16b615` concluded, and exactly as the monograph states in its own text at every touch
point. **h2's register is research-frontier, open; the whole corpus is internally consistent that Chapter
13 and Chapter 15 seal and exclude but do not discharge.** No edits; RH rail read-only; nothing deposited.
