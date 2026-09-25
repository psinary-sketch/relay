## E-2026-09-25-1 — The deposited kernel`s Route 3 premise is equivalent to RH by a ten-line lemma the kernel itself contains (DEPOSIT-FACING; RETAINED AT MONOGRAPH v1.1.2 AND SIDE-kernel v1.5) — DRAFT, NOT FILED

**Drafted 2026-09-25 (b532), on the author`s ruling (R142)(3), from the read banked at b531 (relay `data/b531_premise.txt`, `data/b531_components.txt`); TO BE FILED ON THE AUTHOR`S WORD AT THE PASTE AFTER.
### NO DEPOSIT ACTION IS TAKEN OR IMPLIED BY THIS ENTRY. NOTHING WAS WRITTEN AT ZENODO.
### THE RECORDS ARE IMMUTABLE AT THEIR VERSIONS AND ARE NOT ALTERED BY IT.**

**Affected deposits.** *A Place to Stand*, Zenodo v1.1.2 ([10.5281/zenodo.21539167](https://doi.org/10.5281/zenodo.21539167)) — the monograph and the record description; SIDE-kernel v1.5, tag `v1.5` = commit `0e5233f` ([10.5281/zenodo.21520474](https://doi.org/10.5281/zenodo.21520474)) — the record description.

**What the kernel says, in its own words.** `Bridge/ConservationBridge.lean` at `0e5233f`: *"def ConservationHypothesis : Prop := ∀ (σ : ℝ), is_xi_zero σ → ∃ (p : Nat) (hp : Nat.Prime p), (prime_as_real p hp) ^ (-σ) = (prime_as_real p hp) ^ (-(1 - σ))"*. `Kernel/Voice1.lean` at `0e5233f`: *"theorem balance_theorem (p : Nat) (hp : Nat.Prime p) (s : Real) : (prime_as_real p hp) ^ (-s) = (prime_as_real p hp) ^ (-(1 - s)) <-> s = 1 / 2"*.

**The two lemmas, at their pins.** (1) RH from the premise: `ConservationBridge.riemann_hypothesis` (three lines, through `structural_exhaustiveness_proved` and `balance_theorem`), SIDE-kernel `0e5233f`. (2) The premise from RH: `techne_kernel_integration.structural_exhaustiveness_from_rh` (Kernel/Integration.lean) followed by `balance_theorem` at the prime 2, SIDE-kernel `0e5233f`; compiled as one theorem, `ch_iff_rh`, in SIDE-explicit-formula at this act`s commit.

**The premise is RH restated.** In the kernel`s own words: the premise says that for every real part σ of a nontrivial zero, *"(prime_as_real p hp) ^ (-σ) = (prime_as_real p hp) ^ (-(1 - σ))"* at some prime, and the kernel proves that equation *"<-> s = 1 / 2"*. So the premise says every such real part is ½.

**The terminal`s grade against each claim** (a grade is a relation between a terminal and a named claim, (R40)): against "R2 implies RH", DERIVES (`FACES_LEDGER.md` row R2); against RH, INTERFACES on the named premise (`OPEN_TRAILS.md:5523`) — and that INTERFACES grade on "the open premise h2, carried openly" does not distinguish the premise from the conclusion; against "h2_sign → RH", ENCODES-CONCLUSION (b531).

**The deposited sentences that rest on it** (b532, relay `data/b532_rows.txt`, each with a replacement drafted from this entry`s words):
- **monograph v1.1.2 (A_Place_to_Stand.md)** — 10 sentence(s): M-02, M-04, M-09, M-13, M-14, M-18, M-20, M-22, M-23, M-24
  - `M-02`: *"The Lean 4 kernel formalizes three independent routes to σ = 1/2, each compiled with zero unproved assertions: Route 1 (structural exhaustiveness via `structural_exhaustiveness_proved`), Route 2 (codimension analysis via `SpectralCannonFull.spectral_cannon`), Route 3 (Conservation of Spectra via `ConservationBridge.riemann_hypothesis`)."*
  - `M-04`: *"The five registers of the single premise the proof routes through — the universality hypothesis of `silence_universal`, the ConservationHypothesis of Route 3, the totality of realization through places, the balance-to-positivity distance at the multiplicative place, and the spectral-realization distance — are gathered as one in §27.3."*
  - `M-09`: *"**Route 3 — Conservation.** `Bridge/ConservationBridge.lean` defines `ConservationHypothesis` as the proposition that every ξ-zero forces the Euler balance equation at some prime — the Lean expression of the programme's one counted premise (§27.3), stated at the multiplicative place."*
  - `M-13`: *"`ConservationHypothesis` in `ConservationBridge.lean` is the programme's one counted premise (§27.3) — open, and as of kernel v1.3 stated identically in kernel and prose (every ξ-zero forces the Euler balance at some prime)."*
  - `M-14`: *"The kernel's Route 3 closes the chain from the premise to `RiemannHypothesis` in Lean directly."*
  - `M-18`: *"The method's continuation past the Day-1 kernel — aimed at the Route 3 interface — is reported in §27.3: two statements closed, the third pinned to a goal state and bracketed by a theorem-pair."*
  - `M-20`: *"Second: the proposition named `ConservationHypothesis` in the kernel's Route 3 (§25.5, §25.7) — every ξ-zero forces the Euler balance equation at some prime."*
  - `M-22`: *"This proposition is the premise itself, stated at the multiplicative place: Chapter 13's Conservation of Spectra Theorem — the s-darkness of the product formula — is the unconditional conservation *certificate* that shapes and motivates it, but does not discharge it; the premise's current research home is the Balance-and-Positivity analysis in the programme corpus, and its ledger is this section."*
  - `M-23`: *"The Lean kernel formalizes three routes to σ = 1/2: the structural route via `Bridge.StructuralExhaustiveness`, the codimension route via the Spectral Cannon chain, and the Conservation route via `ConservationBridge.riemann_hypothesis` taking `ConservationHypothesis` to `RiemannHypothesis`."*
  - `M-24`: *"The manuscripts prove the mathematics that connects them: Conservation of Spectra from Tate's thesis (Chapter 13) — the certificate that motivates Route 3's hypothesis, which is itself the one open premise of §27.3, not its discharge; exhaustiveness from Ostrowski (Chapter 15), the Mechanism Theorem from I+D+S (Chapter 10)."*
- **kernel record 21520474 as b493 banked it (listing line 36)** — 1 sentence(s): K-01
  - `K-01`: *"The seven-class catalogue and its exhaustiveness structure; the seven Voice files carrying the per-class exclusion algebra; the product-formula conservation chain (prime, integer, and rational levels); the perpendicular-crossing chain; the formation count; and three independent route terminals: structural_exhaustiveness_proved (the catalogue conjunction), SpectralCannonFull.spectral_cannon (the de…"*
- **Zenodo 21520474 as b499 fetched it back** — 2 sentence(s): Z21520474-01, Z21520474-02
  - `Z21520474-01`: *"SIDE-kernel: the machine-verified architecture of the SIDE reduction of the Riemann Hypothesis to a single located clause."*
  - `Z21520474-02`: *"The seven-class catalogue and its exhaustiveness structure; the seven Voice files carrying the per-class exclusion algebra; the product-formula conservation chain (prime, integer, and rational levels); the perpendicular-crossing chain; the formation count; and three independent route terminals: structural_exhaustiveness_proved (the catalogue conjunction), SpectralCannonFull.spectral_cannon (the de…"*
- **Zenodo 21539167 as b499 fetched it back** — 1 sentence(s): Z21539167-01
  - `Z21539167-01`: *"A skeptic can run lake build at the pinned kernel commit (SIDE-kernel v1.5 = 0e5233f) and #print axioms at the named route theorems (structural_exhaustiveness_proved; SpectralCannonFull.spectral_cannon; ConservationBridge.riemann_hypothesis — the third is the compiled implication from the named interface ConservationHypothesis, whose mathematics is the manuscript's Chapter 13 territory and whose l…"*

**What is not corrected.** The monograph`s own Appendix G already says *"the premise remains RH-equivalent and open"*; this entry does not dispute it and adds that, for register 2, the equivalence is a ten-line lemma inside the kernel. Every other route terminal, every figure and every other register is untouched.

**Status.** DRAFT. Retained at monograph v1.1.2 and SIDE-kernel v1.5 when filed. Whether any Zenodo description is edited under (R110) is the author`s ruling.
