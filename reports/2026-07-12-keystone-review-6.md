# Keystone review 6 — Foundations of the SIDE Programme v0.2 (2026-07-12)

**Document:** `phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md` (md5 verified `bce9f724249820bbf9340d0a65fbc0aa` before editing).
**PLACE-papers commit:** `367ea1c` (pushed; `0812542..367ea1c`).
**Pass:** author-ratified F1–F11, finish-first discipline (F-PRE audits ran before any Status cell was written).

## F-PRE — verifications (verbatim `#print axioms`, at pinned tags)

**(i) SIDE-compression v0.1.0 (`e31d719`).** Terminals are **per-instance only** — `compressionHolds X = true` by `decide` for each instance; there is **no general chain-length theorem** (length = formation total under exhaustive catalogue + per-class finite check). **Outcome: instances compiled; the general form is manuscript-resident.**
```
SIDECompression.xi_compression            does not depend on any axioms
SIDECompression.platonic_compression      does not depend on any axioms
SIDECompression.frobenius_compression     does not depend on any axioms
SIDECompression.xi_chain_length_seven     does not depend on any axioms
```
(also `tilings_compression`, `hurwitz_compression` present, same form.)
**⚠ Work-order flagged:** a vanilla-Lean *general* chain-length theorem (`∀ X, exhaustive-catalogue ∧ dark-interfaces ∧ finite-per-class-check → chainLength = formationTotal`) is not yet compiled in `SIDE-compression`; the panel is per-instance `decide`. Recommend adding the quantified theorem so the Correspondence can upgrade from "instances compiled" to "general form compiled."

**(ii) Unconditional per-instance silence theorems (FQN).** SIDE-silence-principle v0.1.0:
```
SIDESilencePrinciple.silence_principle              [propext]
SIDESilencePrinciple.Universal.silence_universal    does not depend on any axioms
SIDESilencePrinciple.product_formula_silent         does not depend on any axioms
SIDESilencePrinciple.distributive_law_silent        does not depend on any axioms
```
MetaKernel's nine-instance panel carries the same two load-bearing instances as `SpectralSilence.product_formula_silent` / `SpectralSilence.distributive_law_silent` (namespace `SpectralSilence`); the standalone public kernel above is the cited, profile-verified home.

**(iii) SieveCeiling + SIDE-kernel terminals (SIDE-kernel `ce5d7bd`, v1.2 = `b1407b2`):**
```
sieve_ceiling                              does not depend on any axioms
proof_dichotomy                            does not depend on any axioms
bright_access_required                     does not depend on any axioms
e_difficulty                               [propext, Quot.sound]
e_difficulty_xi                            [propext, Quot.sound]
SilenceTheorem.silence_universal           does not depend on any axioms   (hypothesis I.is_universal)
ECondition.type_I_has_ostrowski            [propext, Quot.sound]
ProductFormula.conservation_of_spectra     [propext, Classical.choice, Quot.sound]
ostrowski_exhaustive (OstrowskiBridge)     [propext, Classical.choice, Quot.sound]
neg_eq_neg_one_sub_iff (LocalZeta)         [propext, Classical.choice, Quot.sound]
```

## F1 — TECHNE.Core substitution / cut table (every site)

| Site | Was | Now |
|:--|:--|:--|
| §IV.4 Verification panel | "verified computationally in TECHNE.Core across multiple SIDESystem instances" | **substituted** → public `SIDE-compression` v0.1.0 per-instance terminals (`xi_compression` … `frobenius_compression`, axiom-free); general form noted manuscript-resident |
| §VI.2 Step (ii)→(i) | "demonstrated for ξ (RH), Dirichlet L (GRH), and **27+ other systems in TECHNE.Core**" | **cut/rescoped** → "…for RH and GRH; broader application is private computational exploration, not part of the public verification record" |
| §VIII.2 E_DIFFICULTY | "across **27+ systems in TECHNE.Core**" | **rescoped** → "demonstrated for RH and GRH; broader instances private" |
| §IX federation | "TECHNE.Core … **six instances; 2,903 jobs**; … instantiated six times; **self-application**" | **substituted + cut** → `SIDE-compression` v0.1.0 (named terminals); the panel/jobs/self-application counts marked private exploration |
| References (kernel) | "TECHNE.Core … six instances; 2,903 jobs …" | **substituted** → `SIDE-compression` v0.1.0 pointer |

Result: **zero `TECHNE.Core` references remain** (grep-confirmed); no bare counts survive as public claims.

## F2–F9 (summary)
- **F2** "Hedging Section" → "Scope and Open Problems"; caveats preserved and routed to scoped verbs + Correspondence Status; closing epigram ("*Silence is proof*") cut.
- **F3** "cluster keystone"/cluster framing plainened at all three sites (provenance, §VIII intro, §VIII.4 heading).
- **F4** §VI scoped: the four SieveCeiling terminals front-and-centre with v1.2 citation; §VI.1 "Theorem" label now reads "skeleton kernel-verified; full analytic form argument-supported, pending the finished Sieve Ceiling Lemma."
- **F5** §II.1(C) exclusion step finished with the bracket: `T3.T3doubleprime_general_commutation_fails` (countermodel) / `T3.T3prime_shared_witness` (shared witness, Determination-supplied); cross-ref *The Unconditional Surround of ξ*.
- **F6** all v1.1 cites → v1.2 formulation (v1.1 DOI as citable deposit + superseded-profile clause); "22 / 33 theorems", "83 files" replaced by named terminals (`ProductFormula.conservation_of_spectra`, the SieveCeiling four).
- **F7** §II.1(E) "Confirmed experimentally" → "Observed for optical vortices (Kaminer et al., *Nature* 2026), consistent with the structural prediction."
- **F8** count-headings: §II.3 "The domain instantiation panel", §II.4 "Formal status, at three levels", §VII.1 "Translations across the tradition."
- **F9** CP-B-2/CP-B-4, "Phase 2b draft", the RESONANCE R-score removed; TYPE II/III naturalized ("out-of-method-reach", A_METHODOLOGY labels parenthesized); I+D+S glossed at first use (§VI.1).

## F10 — Correspondence (verified; profiles above)

| Claim | Kernel | Theorem | Axiom profile | Status |
|:--|:--|:--|:--|:--|
| Silence Principle — universal form | SIDE-kernel v1.2 | `SilenceTheorem.silence_universal` | axiom-free | Compiled — hypothesis `I.is_universal` |
| Silence per-instance (product formula / distributive law) | SIDE-silence-principle v0.1.0 | `product_formula_silent`; `distributive_law_silent` | axiom-free | Compiled (unconditional) |
| Silence four-step chain | SIDE-silence-principle v0.1.0 | `silence_principle`; `Universal.silence_universal` | `[propext]`; axiom-free | Compiled |
| Mechanism Theorem | SIDE-kernel v1.2 | `ECondition.type_I_has_ostrowski` | `{propext, Quot.sound}` | Compiled |
| E-Difficulty skeleton (4 terminals) | SIDE-kernel v1.2 | `sieve_ceiling` / `proof_dichotomy` / `bright_access_required` / `e_difficulty` | axiom-free (first three); `{propext, Quot.sound}` (`e_difficulty`) | Compiled (skeleton) |
| Conservation / Spectral Inertness | SIDE-kernel v1.2 | `ProductFormula.conservation_of_spectra` | `{propext, Classical.choice, Quot.sound}` | Compiled |
| Mathlib bridges | SIDE-kernel v1.2 | `ostrowski_exhaustive`; `neg_eq_neg_one_sub_iff` | `{propext, Classical.choice, Quot.sound}` | Compiled |
| Compression Theorem | SIDE-compression v0.1.0 | `xi_compression` … `frobenius_compression`, `xi_chain_length_seven` | axiom-free | Instances compiled; **general chain-length form manuscript-resident** |
| Sieve Ceiling Lemma (full) | (none) | — | — | Manuscript-resident (v1.0 draft) |
| E-Difficulty (full analytic form) | (none) | — | — | Research-reach |

## F11 / notes
- Header v0.1 → v0.2 with provenance line; REGISTRY row **1.5f-4 → v0.2, REVIEW** via a row-update block.
- No mathematical content changed; the pass substituted private-platform citations with public kernels, scoped claim-verbs, and finished the (C) exclusion step with the compiled bracket.
- No deposit action taken.

---

## Addendum (2026-07-12) — Compression general-form work-order CLOSED

The vanilla-skeleton work-order flagged in F-PRE(i) is closed: `SIDE-compression` **v0.2.0** adds the general chain-length theorem.

- New module `SIDECompression/ChainLength.lean` (namespace `Compression`, written verbatim from the ratified source): `Compression.compression` — N per-class checks + exhaustiveness ⟹ `∀ x, ¬ violates x` — and `Compression.compression_infinite_objects` (the infinitely-unsaturated regime over `Nat`). Vanilla Lean 4, no Mathlib. No name collisions; the root module gained only the import line. `lake build` green (5 jobs).
- Verbatim `#print axioms` (both as expected):
```
Compression.compression                    does not depend on any axioms
Compression.compression_infinite_objects   does not depend on any axioms
```
- **SHA triple (SIDE-compression):** verified commit `e9a5a368d14aeb63ae970acb84fc135838b9f6d2`; remote tag-object `167f84c5f81e3b381677f91596c2378001952ec4`; remote peeled (`^{}`) `e9a5a368d14aeb63ae970acb84fc135838b9f6d2` — **== verified commit ✓**; origin/main == verified commit ✓. Tag **v0.2.0** annotated.
- FOUNDATIONS updated (PLACE-papers commit `e0c1f69`): the Compression Correspondence row upgraded from "instances compiled; general form manuscript-resident" to **Compiled — SIDE-compression v0.2.0, `Compression.compression` / `Compression.compression_infinite_objects`, axiom-free**; the §IV general-form sentence and the Abstract clause rescoped; provenance sub-line "(general form compiled 2026-07-12)".
