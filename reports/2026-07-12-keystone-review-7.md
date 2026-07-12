# Keystone review 7 — EXCLUSION ENGINE v2.1: **E0 SALT-CHECK FAILED. PASS HALTED.**

**Date:** 2026-07-12
**Source:** `phase1.5/method/EXCLUSION_ENGINE.md` v2.0, md5 `b942ee7ab693285ffd372bff99d3a7bf` ✓ (verified before reading; file read complete; **not edited**)
**Status:** **No v2.1 commit was made.** E0 is a gate that runs *before* any Correspondence row is written. It failed — not on one terminal, but on nearly every terminal the paper cites as content. E1–E6 are held pending your ruling. Reasons below; the decision is yours, not mine to enact.

---

## 0. The finding, in one paragraph

The paper's rigorous spine is the distinction it draws in §III: *"The kernel writes `MismatchMechanism` where it has substance and `fun _ => True` where it does not. That distinction **is** the boundary."* **That distinction does not exist in the source.** The kernel writes `fun _ => True` in *both* places. `MismatchMechanism` — the paper's named exemplar of substance — is discharged over `mismatch_absent : MismatchMechanism → Prop | .phantom_zeros => True | .degenerate_reg => True | .tamagawa => True | .period_value => True`. It is the same shell as `TwinFinite`, which the paper correctly identifies as vacuous. The mechanism-bearing/non-mechanism-bearing boundary — the thing the keystone exists to state — is not visible in the Lean at any pin I audited. Every claim below is verified by me directly against source, not taken from a subagent.

**Scope discipline, stated up front.** This census covers the terminals *this paper cites*: the method/meta layer (`Voice3b`, `TypeLevel`, `Layer1`, `MetaKernel`, `Cascade/SieveCeiling`) and the application kernels (SIDE-effects, the two BSD kernels, SIDE-interfaces). **It does NOT cover, and does not impugn, the RH proof core** — Routes 1–3 (`structural_exhaustiveness_proved`, `SpectralCannonFull.spectral_cannon`, `ConservationBridge.riemann_hypothesis`) were audited on 2026-07-10 and stand at `{propext, Classical.choice, Quot.sound}`. Those are conditional theorems of the known architecture and are not implicated here. What failed is the *method layer that claims to justify the architecture*, and the *application kernels that claim to extend it*.

---

## 1. Method

Pins (committed state read via `git show <pin>:<path>`; working trees ignored where dirty):

| Repo | Pin | Tree |
|---|---|---|
| SIDE-kernel | tag `v1.2` = `b1407b2` | dirty (4 files) → read at pin |
| SIDE-effects | HEAD `c66f3c5` | dirty (11 files) → read at pin |
| SIDE-interfaces | tag `v0.2` = `1728796` | clean |
| SIDE-bsd-formation-transfer | tag `v0.1.0` = `7425d73` | clean |
| SIDE-bsd-multiplicity | tag `v0.1.0` = `97f30bd` | clean |

Gate applied per terminal: **(a)** statement read against the paper's claim; **(b)** screen for `True`-typed conclusions, uniformly-`True` predicate instantiation, `X = X`, fabricated witnesses, `decide` over hand-written tables; **(c)** hypotheses named — especially any hypothesis that *is* the mathematical claim; **(d)** `#print axioms`.

**On (d):** axiom profiling was **not run for the failing terminals, and that is deliberate.** A tautology's axiom profile is a clean-looking number that certifies nothing — `theorem meta_kernel_summary : True := trivial` will report a pristine profile. Where (a)–(c) fail, (d) is not evidence, and running it would launder the failure. Profiles stand where they were earned: the three RH route terminals at v1.2.

---

## 2. THE SALT-CHECK TABLE — the federation's index card

**Legend.** **CONTENT** = says what the paper says it says. **SHELL** = well-formed but the mathematical claim is assumed as a hypothesis or written in by hand. **TAUTOLOGY** = provable with the subject matter deleted. **ABSENT** = the cited declaration does not exist at the pin.

### SIDE-kernel @ `v1.2`

| Terminal | file:line | Paper's claim | Source | Verdict |
|---|---|---|---|---|
| `determination_bridge` | `Kernel/Voice3b.lean:132` | "The Determination condition is proven and Lean-verified… the D of SIDE" | `theorem determination_bridge (sigma : Real) (h_codim2 : zero_codimension sigma = 2) (_h_determined : True) : Not (sigma = 1/2)` | **SHELL — WORK-ORDER.** The determination hypothesis is the proposition `True`, underscore-prefixed and never used. Strip it and what remains is the contrapositive of an `if-then-else` guard. Determination is not transmitted; it is stipulated. |
| `determination_collapse` | `Kernel/TypeLevel.lean:17` | same | `(tlc : TypeLevelConstraint X P) (x : X) : P x := tlc.holds_for_spec x`, where the structure's only field is `∀ x, P x` | **SHELL — WORK-ORDER.** It is `(∀x, P x) → ∀x, P x` — a record projection. `Formation.lean:32` concedes in-source: *"This is TRIVIALLY VALID LOGIC. The content is in the instantiation."* The ξ catalogue that would supply the content is never constructed (file ends at an explicit "INSTANTIATION BOUNDARY"). |
| `SIDE_exclusion` (the Layer1 schema) | `Kernel/Layer1.lean:30` | "the exclusion schema itself is the proven engine… formalized in `Kernel/Layer1.lean` at 0 sorry" | catalogue + none-produces ⟹ `¬P x`. 0 sorry ✓ | **CONTENT (schema) — CITABLE with caveat.** The logic is valid and the 0-sorry claim is true. But `MechanismClass` carries no obligation tying `produces` to `P`, and the file's only instantiation is over an **empty catalogue** with the unsatisfiable predicate `n > 100 ∧ n < 50`. A valid schema with no non-vacuous instance. Cite as schema; do not cite as engine. |
| `e_difficulty` | `Kernel/Cascade/SieveCeiling.lean:266` | "the rigorous spine"; decidable ⟺ domain-Ostrowski | `IsDecidable s ↔ Nonempty (DomainOstrowski s)`, with `def IsDecidable (_s : DeterminedSystem)` — **the system argument is discarded** — and the Ostrowski witness built by `List.replicate s.classes accesses_bright` rather than extracted from the proof. Conservation hypothesis `_h_conserved` unused. | **TAUTOLOGY — WORK-ORDER.** Both sides are unconditionally provable for every `s`. The paper's rigorous spine asserts nothing about any system. |
| `sieve_ceiling` | `…/SieveCeiling.lean:203` | the ceiling | True by definition: `maxStatement π := if π.factorsDark then density_one_per_class else universal`, then proved by unfolding it. `density_one_lt_universal` is `by decide` on `1 < 2`. | **TAUTOLOGY — WORK-ORDER.** |
| `dh_witness` (Davenport–Heilbronn) | `…/SieveCeilingWitness.lean:43` | the DH separation | `def iIndist (_ _ : Config) : Prop := True` over a 2-element enum with the answer hand-written | **TAUTOLOGY — WORK-ORDER.** Proves: no constant predicate equals a non-constant one. |
| `type_I_has_ostrowski` | `MetaKernel.lean:145` | the logical engine of SIDE Exclusion | Sound modus tollens ✓ | **CONTENT (thin) — CITABLE.** Caveat: `[Fintype Domain]` is never used — the exhaustiveness/E-condition the programme rests on is decorative; the theorem holds verbatim for infinite domains. |
| `silence_universal` | **`Kernel/SilenceTheorem.lean:74`**, not MetaKernel | cited as MetaKernel's | Genuine: constant action ⇒ factoring measurement constant | **CONTENT — CITABLE, but relocate the citation.** Caveats: the `essential` field is never used (so it says nothing about essentiality) and both instances are over `Unit`. |
| "the nine instance theorems" | — | cited by the work-order | **ABSENT.** MetaKernel has 16 theorems, none grouped as nine. The per-domain instances were **deleted as hollow** — in-source: *"[M1 retired] … the hollow Ostrowski instance: its target was (exists c, False), NOT a statement about zeta, so rh_exclusion proved (not False) and **said nothing about the zeros**"*; *"[M1 retired] ym_massless … the Yang-Mills mass gap is an OPEN Clay Millennium Problem; **it is NOT proved here**."* | **ABSENT — cite nothing.** Also present: `theorem meta_kernel_summary : True := trivial`; `math_passes_level_0 : X = X`; `eliminative_is_ostrowski : X = X`; the E-condition formalized as `∀ d : Domain, d = d` ("placeholder for 'checked'"). |
| `LSZero`, `RankMismatch`, `MismatchMechanism`, `Massless`, `TwinFinite` | — | §II: "the kernels make this literal" | **0 hits, all five, at v1.2.** They live in SIDE-effects. | **ABSENT from this repo.** |

### SIDE-effects @ `c66f3c5` — §II/§III's four exemplars

| Terminal | file:line | Source (verbatim) | Verdict |
|---|---|---|---|
| `Massless` / `mass_gap` | `Structural.lean:43-57` | `def gapped : Sector → Prop \| .perturbative => True \| .instanton => True \| .vortex => True \| .monopole => True`; `Massless := ∃ s, ¬(gapped s)`; `mass_gap : ¬Massless` by `cases <;> trivial` | **TAUTOLOGY.** Unfolds to `¬∃ s, ¬True`. The physics is entirely in the `--` comments. |
| `LSZero` | `Structural.lean:132` | `def LSZero (balance_forces_half : Prop) (sigma_gt_3_4 : Prop) : Prop := balance_forces_half ∧ sigma_gt_3_4` | **SHELL.** σ, 1, 3/4 appear only in the identifier and docstring. Two free `Prop` variables. |
| `RankMismatch` / `MismatchMechanism` | `Structural.lean:221-238` | `mismatch_absent \| .phantom_zeros => True \| .degenerate_reg => True \| .tamagawa => True \| .period_value => True`; `theorem bsd_full : ¬RankMismatch` | **TAUTOLOGY — and this is the one that breaks §III.** The paper's named exemplar of *substance* is the same `fun _ => True` shape as its named exemplar of *vacuity*. |
| `TwinFinite` | `Structural.lean:166-170` | `def TwinFinite := TypeD Nat (fun _ => True) (fun _ => True)` — source comment: *"Structural placeholder"* | **TAUTOLOGY — paper's description CONFIRMED VERBATIM.** (`GoldbachFails` and `SGFinite` are character-for-character identical.) |
| `Structural.lean` "front is closed" | — | 0 sorry ✓, 0 `axiom` ✓ — **but 17 of 20 theorems are vacuous** (uniformly-`True` predicates, or `Prop`-variable tautologies where the hypothesis *is* the mathematics, e.g. `artin_from_grh (hooley_thm : grh → artin) (h : grh) : artin := hooley_thm h` — modus ponens with Hooley assumed) | **TRUE-BUT-EMPTY.** "0 sorry" here is not evidence of content; there is nothing in the file to prove. |
| `no_type_d_conspiracies`, `crt_exhaustiveness` | `Phase15/Module1.lean` | **The one place with real content** — a genuine 6-constructor `StructuralCoupling` over `ZMod q`, real `eval`, 2 of 6 induction cases genuinely discharged | **CONTENT (partial) — HONEST OPEN ROW.** But it rests on `to_modular`, which is 3/6 `sorry` and whose `shifted` case is a **knowingly-wrong total definition** (`\| .shifted _k inner => to_modular inner`, ignoring the shift; admitted in the file header). And **no import connects it to `no_conspiracy_twins`** — the real machinery and the problem-named theorems are in different files with no dependency edge. |

### SIDE-interfaces @ `v0.2` — **the one repo that carries real mathematics**

| Terminal | file:line | Source | Verdict |
|---|---|---|---|
| `kappa` | `Interfaces/Kappa.lean:15` | `(Finset.univ.image (fun a => \|P (f a) - P (f a0)\|)).max'` | **CONTENT — CITABLE.** κ is genuinely *computed from structure*, not a hand-set enum. This is real. |
| `rank_decomposition`, `interface_split` | `ConservationProfile.lean:38,108` | honest `Finset` partition / `card_lt_card` proofs | **CONTENT — CITABLE.** |
| `connection_requires_structure` | `ConnectionRequiresStructure.lean:22` | hypothesis `h_bimodality : ∀ x, P.kvec x < 45/100 ∨ 75/100 ≤ P.kvec x` | **SHELL — WORK-ORDER.** `h_bimodality` **is** the E-Difficulty dichotomy. The theorem assumes what §IV says it establishes; the 0.45/0.75 thresholds are underived magic numbers. |
| — | — | **Structural gap:** `ConservationProfile.kvec` is a *free real vector*, never linked to the computed `kappa`. There is no lemma `P.kvec x = kappa (…)`. `IsDark`/`kappa_invariance` are dead code; the advertised `dark_iff_invariant` is still a "deferred to v0.2" comment **at v0.2**. | The κ definition and the dichotomy theorems are **two disjoint islands**. §IV's "its κ-machinery is formalized" is defensible **only** for the definition of κ and the parametric-mechanism lemma — *not* for the dichotomy. |

### The BSD kernels — §III's exemplars of "genuine per-class content"

| Terminal | file:line | Source (verbatim) | Verdict |
|---|---|---|---|
| `all_seven_transfer` | `SIDE-bsd-formation-transfer` `Basic.lean:109` | `def transfers : MechanismClass → Bool \| .sqrt_mechanism => true \| … \| .hadamard => true`; `theorem all_seven_transfer : ∀ c, transfers c = true := by intro c; cases c <;> decide` | **TAUTOLOGY.** "Carrying the seven classes onto Λ(E,s)" is `true` written seven times. **`Λ(E,s)` does not exist in the repo** — no ℂ, no L-function, no curve. |
| `bsd_decomposition` ("delivers location") | same, `Basic.lean:205-212` | `def location_transferred : Bool := true`; `theorem bsd_decomposition : location_transferred = true ∧ … := by decide` | **TAUTOLOGY — `true = true`.** No statement anywhere that any zero of anything lies anywhere. |
| `BSD_three_layers` | `SIDE-bsd-multiplicity` `Basic.lean:315-327` | `structure BSDResultLayer where multiplicity_equals_rank : Bool` … `def BSD_status := { multiplicity_equals_rank := true, … }` … `theorem BSD_three_layers : BSD_status.multiplicity_equals_rank = true := by decide` | **TAUTOLOGY — the strongest form of the pattern.** A `Bool` field *named after the conjecture*, assigned `true` by hand, then "proved" to equal `true`. |
| "derives both ranks from one specification" | — | `same_spec_determines_both := true` inside a record literal. `RankPair` (holding `algebraic_rank`, `analytic_rank`) is **declared and never used again**. `framework_bounds_sha : ShaFinitenessFramework → Bool := fun _ => true`. | **ABSENT.** No theorem in the repo relates an algebraic rank to an analytic rank. |

---

## 3. Paper-vs-source disagreements requiring your ruling

| § | Paper says | Source at the pins |
|---|---|---|
| I | "The Determination condition is **proven and Lean-verified**" | `determination_bridge`'s determination hypothesis is `True` (unused); `determination_collapse` is `(∀x,Px) → ∀x,Px`. The Misreadings appendix bullet — *"Determination is proven, not an open seam"* — is **contradicted by the terminals the same paper cites for it**. |
| II | "the kernels make this literal" (LSZero / RankMismatch / Massless / TwinFinite) | All four are shells or tautologies. The reframing is literal in *name* only. |
| III | "`MismatchMechanism` where it has substance and `fun _ => True` where it does not — **that distinction IS the boundary**" | Both are `fun _ => True`. **The boundary the keystone exists to state is not in the Lean.** |
| III | formation-transfer "carries the seven classes onto Λ(E,s) and **delivers location**"; multiplicity "**closes ord = rank**" | `def location_transferred : Bool := true`; `multiplicity_equals_rank := true`. Neither is derived; both are typed in. |
| IV | "Its κ-machinery is formalized… its sieve-ceiling skeleton is formalized" | κ: **yes, genuinely** (cite it). Sieve-ceiling: `e_difficulty` is a tautology. Dichotomy: assumed as `h_bimodality`, over a vector never linked to κ. |
| VII | "SIDE-effects with **7 real sorry, all in `Phase15/Module1.lean`**" | **10 real sorry**: 7 in Module1 + **3 in `Milestones.lean`** — the very file §III relies on for the Hardy–Littlewood milestone. The paper cites that sorry in §III and omits it from its own census in §VII. |
| VII | "a static audit… returns **clean health** with two localized exceptions and no others" | The audit instrument cannot see the exceptions. `SIDEEffects.lean` imports only `Structural` + `Milestones`; `Module1` is **not in the build target**, so `lake build` never elaborates it and the CI sorry-count (which greps the build log) **structurally cannot see Module1's 7 sorries**. CI reports 3. "Clean health" is an artifact of a blind instrument. |

**E3's 7-vs-3 reconciliation, answered:** neither is the repo total. 7 = Module1-only; 3 = Milestones-only (= what CI sees, because Module1 isn't built). **Repo total at `c66f3c5` is 10.** History: 3 (v0.1) → 12 (`444b9a2`, Phase15 lands) → 10 (`c31e1de`, "sorry 9 → 7", correctly scoped to Module1). Note the pin commit `c66f3c5`'s own purpose was *"strip '19 theorems' and '7 sorries' count anchors"* — the counts were already under dispute inside the repo.

---

## 4. Why I halted instead of writing v2.1

E0's rule is mechanical: a terminal failing (a)–(c) gets a work-order row, not a citation row. Applied honestly here, that rule does not produce a v2.1 of this paper — it produces a **retraction of §II and §III's examples, the §I Determination claim, the §IV sieve-ceiling half, the §VII census, and one bullet of the Misreadings appendix**. That is not "refine, don't rewrite." It is a different paper, and which paper it should be is an author's call about the programme's claims, not an editorial call I should make inside a commit.

Two further reasons to stop rather than proceed:

1. **The kernels' own comments are more honest than the paper.** The `[M1 retired]` annotations show someone already found the hollow instances and removed them, writing plainly that the RH Ostrowski instance *"said nothing about the zeros"* and that Yang–Mills *"is NOT proved here."* SIDE-effects' `Milestones.lean` header is candid that its statements are the real types proved by `sorry`. The BSD formation-transfer README concedes *"the kernel encodes the conclusion at each class."* **The source layer has been telling the truth; the paper layer has not caught up.** A v2.1 that adds a Correspondence table without correcting the prose would put the dishonesty in a new place, not remove it.
2. **The programme's deposited RH core is not implicated, and it must not be dragged into this by a sloppy fix.** Routes 1–3 stand. Precision about *what* failed protects what didn't.

## 5. Recommendation, and the decision I need from you

**Recommended: v2.1 as an honest-boundary paper.** Keep the spine — universal exclusion-reframer, Π-fragment reach, the mechanism-bearing *idea* — and restate §II/§III with the truth this census establishes: *the boundary is real as a methodological claim, but as of the current federation **it is not yet formalized**; what the kernels currently encode at the application layer is the conclusion, not the derivation.* That paper is publishable, defensible, and — unusually — more interesting than v2.0, because the honest version of §III ("here is where we mistook encoding for proving, and here is the standard that caught it") is a genuine methodological contribution. The salt-check itself becomes the paper's exhibit.

**The alternative** — refit the kernels first (give `MismatchMechanism`, `Massless`, `LSZero` real predicates; derive the bimodality thresholds; connect `kvec` to `kappa`; discharge `to_modular`) and then write the Correspondence — is the larger, better, slower path. It is a wave of kernel work-orders, not an editorial pass.

**What I did not do:** no edit to `EXCLUSION_ENGINE.md`; no v2.1; no REGISTRY row; no version bump. E1's IP deposit-gate (the REGISTRY block) and E5's jargon glosses are independent of the salt-check and can land immediately on your word — say so and they will.

**Open question I could not settle from source, and would not guess at:** whether the vacuous application kernels were ever *intended* as claim-bearing artifacts or as scaffolding that the papers then over-read. The `[M1 retired]` cleanup suggests the latter. That distinction changes the tone of the correction, and it is yours to state.
