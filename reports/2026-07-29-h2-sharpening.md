# h2 sharpening — 2026-07-29

An analytical pass on the programme's one counted premise, `h2`. No edits to any paper or kernel. Sources:
`Bridge/ConservationBridge.lean` at SIDE-kernel **v1.3 = `0bc21c0`** (statement read at the pin);
`phase1.5/proofs/THE_RESIDUE_OF_RH.md`; `day1/A_Place_to_Stand.md` §9 / §27.3 (RH rail — read only).

## (1) h2's precise formal content

**The Lean declaration, verbatim** (`Bridge/ConservationBridge.lean`, v1.3 `0bc21c0`):

```lean
def ConservationHypothesis : Prop :=
  ∀ (σ : ℝ), is_xi_zero σ →
  ∃ (p : Nat) (hp : Nat.Prime p),
  (prime_as_real p hp) ^ (-σ) = (prime_as_real p hp) ^ (-(1 - σ))
```

consumed by the one terminal that carries it as a hypothesis:

```lean
theorem riemann_hypothesis (h_cons : ConservationHypothesis) : RiemannHypothesis
```

In words: *for every real σ, if σ is (the real part of) a ξ-zero, then at SOME prime p the balance
`p^(-σ) = p^(-(1-σ))` holds* — equivalently `σ = 1 - σ`, i.e. `σ = 1/2`, forced at that prime. The
existential (`∃ p`) is the **W-7 weakening** (2026-07-16): the def moved from the universal form (`∀ p`,
balance at every prime) to `∃ p` (at some prime), which makes `riemann_hypothesis` a strictly *stronger*
theorem (weaker hypothesis, same conclusion) and matches the monograph's own "at some prime" (§25.5).

**The manuscript sentence it corresponds to** (`A_Place_to_Stand.md`, Route-3 chapter):

> "`ConservationHypothesis` … the proposition that every ξ-zero forces the Euler balance equation at some
> prime — the Lean expression of the programme's one counted premise (§27.3), stated at the multiplicative
> place."

§27.3 is titled *The Realization-Totality Premise: Every ξ-Zero Forces the Euler Balance*, and states h2 as
**one premise in five registers**: (i) the universality hypothesis of `silence_universal`; (ii) the
`ConservationHypothesis` of Route 3; (iii) the totality of realization through places; (iv) the
balance-to-positivity distance at the multiplicative place; (v) the spectral-realization distance. The
Lean `ConservationHypothesis` is register (ii); the residue paper sharpens (iii)–(v).

**What the conclusion asserts.** `riemann_hypothesis`'s conclusion is Mathlib's `RiemannHypothesis` (about
the zeros of Mathlib's `riemannZeta`), reached from the local `StructuralExhaustiveness` via
`rh_from_structural_exhaustiveness`. So h2 is exactly the hypothesis whose discharge turns a compiled
implication into Mathlib-RH; nothing else is open on that edge.

## (2) What a discharge would require — sufficient conditions

The residue paper's `residue_irreducible` (§7) decomposes h2 into **a conjunction of two individually-free
clauses over the ζ-zeros**, whose *join* is the whole of RH:

> "clause 1 (zero-realization) is free — a positive self-adjoint operator with a discrete spectrum exists
> (the certified input), but it does not realize the ζ-zeros; clause 2 (the inequality) is free to a
> threshold — the two-channel inequality is certified to `N₀(T)`, but not for all `n`; only the
> conjunction is RH … Neither clause alone is hard; their join is the whole of RH."

Each sufficient condition, classified:

| # | sufficient statement (any one discharges h2) | kind |
|:--|:--|:--|
| S1 | **Li's criterion**: λ_n ≥ 0 for all n (Li 1997 / Bombieri–Lagarias 1999) | **known-open** — RH-equivalent (it *is* RH) |
| S2 | **The two-channel all-n tail**: λ_Z(n) ≥ −λ_A(n) for all n > N₀(T) ≈ 2T² (λ_A known unconditionally, Voros 2006; the finite range n ≤ N₀(T) compiled — `blTerm_nonneg_of_onLine`, `certifiedPartialInhabitant`) | **novel** — the residual after the compiled range; not a named classical problem |
| S3 | **Hilbert–Pólya realization**: a positive self-adjoint operator whose spectrum is the ζ-ordinates | **known-open** — Hilbert–Pólya (~1914) |
| S4 | **Weil positivity over ℚ**: the positive polarization on the FE-even class (the `𝔽_q`→ℚ transfer; `transfer_obstruction_is_the_two_geometric_clauses` isolates exactly this + S3) | **known-open** — Weil positivity; Connes–Consani reduce RH to it |
| S5 | **Deninger's H¹ realization**: the postulated cohomology, typed as `XRealization` on the held branch | **novel** — postulated, unbuilt |

The chiasmus (residue §6) ties S2 and S3 together: the sign season proved *positivity is free without the
zeros* (`positivity_free_obstruction_is_zeroRealization` — the certified structure is positive-definite but
realizes the wrong spectrum `{n²}`); the inverse-spectral converse proves *the operator is free given the
positivity* (de Branges, multiplication on `B(E)` once `E ∈ HB`). They cross at one object — **the positive
space on the zeros** — which neither supplies. *The space is the wall.*

## (3) The SMALLEST sufficient statement

The weakest thing that would discharge h2 is **the existence of the positive space on the zeros** — a
positive self-adjoint operator whose spectrum realizes the ζ-ordinates (`no_asset_realizes_zeroSpectrum`
records that no current programme asset does). It has two faces, the same object seen two ways:

- **Spectral face (S3):** the realization clause — Hilbert–Pólya. **Known-open**, a century old (~1914). The
  positivity and self-adjointness are already free (certified input); only the *realization of the right
  spectrum* is missing.
- **Analytic face (S2):** the all-n tail of the two-channel inequality, n > N₀(T) ≈ 2T². **Novel, unknown
  difficulty.** The threshold N₀(T) is **rigid** — the `γ²` of `|ρ|²`, forced by the functional equation;
  "no mollifier moves it within the Li framework." Its escape-kind is the FE-forced detection horizon
  (`escape_kind_discriminates`), distinct from the derivative wall's raw-infinitude escape.

**Verdict on the smallest statement.** It is **known-open on its spectral face (Hilbert–Pólya)** and **a
novel statement of unknown difficulty on its analytic face (the rigid-threshold tail)** — and it is **not
plausibly-provable by any present asset.** The realization-candidate map (residue §8) shows every route
stalls at *exactly this clause*: Deninger postulates the cohomology, Connes–Consani reduce RH to a Weil
positivity left open, Bost–Connes realize the Euler product (the wrong spectrum); physically every proposal
is *permitted, not forced* (Berry–Keating `H=xp` gives the average counting, the primon gas is input-side,
quantum-chaos is a statistical surrogate, the trapped-ion experiments *measure* the zeros from a ζ-engineered
drive). The programme's own arithmetic-forces-*code* results reach the substrate, not the spectrum: **the
forced-code → forced-spectrum distance is this wall.** No weaker sufficient statement than "the positive
space on the zeros" is available — h2 *is* that object, and the corpus's honest position is that it is a
research-reach realization, not a shortfall a known technique closes.

## (4) Every place h2 is carried — each open, each named

Confirmed against `THE_LOAD_BEARING_MAP.md` (the h2-reach subgraph, "no premise carried implicitly") and
the Correspondence tables. Every site names h2 explicitly:

| site | how h2 is carried | named openly? |
|:--|:--|:--|
| **kernel** `Bridge/ConservationBridge.lean` | `ConservationHypothesis` as the explicit hypothesis of `riemann_hypothesis` | **yes** — the premise itself, `(h_cons : ConservationHypothesis)` |
| **MONO** `day1/A_Place_to_Stand.md` | §27.3 (the one open premise, five registers); §25.5/§25.8 Route 3 `riemann_hypothesis(h_cons)`; §9 "the one open clause … the sign" | **yes** — "one counted premise", disclaimed at §27.3 |
| **SURR** `THE_UNCONDITIONAL_SURROUND.md` | `covers_all` "the one open node" (§6); `h1_complete_at_Phi` "only h2 open" | **yes** — "Open premise" row |
| **SIMP** `SIMPLICITY_OF_RIEMANN_ZEROS.md` | `h1_complete_at_Phi` "only h2 open"; the derivative-h2 (geometric clause) `no_onLine_double_iff_transversal` INTERFACES | **yes** — "the single carried-open premise" |
| **PATHS** `PATHS_TO_THE_CRITICAL_LINE.md` | Route 3 conditional-A on h2; R4 positivity→RH INTERFACES on Li's criterion; R5-output HP **DISCLAIMED**; `certifiedInput_not_zeroRealizing` (h2 candidate #4) | **yes** — "discharge h2", disclaimed |
| **RESIDUE** `THE_RESIDUE_OF_RH.md` | the residue *is* h2's registers (iii)–(v); `residue_irreducible`; §7 disclaimer "Nothing here is proven on the zeros; the fifth register is held open" | **yes** — the disclaimer stands |
| **RCURVE** `R_CURVE_CRITERION.md` | effective dominance = h2 (the 2026-07-19 claim-status correction names it the programme's single open premise) | **yes** — "carried openly" |
| **GRH** `GRH_CASCADE.md` | Universal Silence INTERFACES on `I.is_universal` (register (i)) | **yes** — "named here" |
| **FOUND** `FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md` | Universal Silence INTERFACES on `I.is_universal` | **yes** — "the premise is a manuscript result, named here" |
| **BALPOS** `BALANCE_AND_POSITIVITY.md` | the two-channel Li finite-range certificate; the all-n tail open | **yes** — "not RH; the all-n tail open" |
| **DOM** `DOMAIN_OSTROWSKI_UNIVERSALITY.md` | downstream-of-h2 (RH/GRH terminals compose under h2) | **yes** — h2-reach map |
| **CONCLUSIONS_OF_RECORD** | G1 (completeness on h2), G4 (the chiasmus register) named as open | **yes** — "named as open, not smoothed" |

**Finding:** every carry-site names h2 openly; none carries it implicitly. This confirms the load-bearing
map's result at the h2 edge — the two-leg architecture's honesty is structural, not rhetorical.

## Summary

h2 = `ConservationHypothesis` = *every ξ-zero forces the Euler balance at some prime* (register (ii) of the
five-register §27.3 premise). Its discharge requires the existence of **the positive space on the zeros** —
a positive self-adjoint operator realizing the ζ-ordinates (S3, Hilbert–Pólya, known-open) whose pairing
extends the certified two-channel inequality past the rigid threshold N₀(T) ≈ 2T² (S2, novel,
unknown-difficulty). The two clauses are individually free; only their conjunction is RH. No weaker
sufficient statement exists, and no present asset is forced to supply it. Every corpus site carries h2
openly.

No paper or kernel changed this pass (analytical read). SIDE-kernel remains at the read pin `0bc21c0`
(to be restored to `derivative-engine` at the close of the separate statement-read).
