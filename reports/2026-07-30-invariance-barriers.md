# Invariance Barriers in Analytic Number Theory v1.1 — the Sieve Ceiling revision (retitle + Tier-1 fold-in) — 2026-07-30

Executes the author's ruling of 2026-07-30: title *"Invariance Barriers in Analytic Number Theory"*,
subtitle *"Witness Pairs, Method Classes, and the Euler Product"*, candidate-5 opening (the paper leads with
what the exclusions achieved — reduction, localization, convergence — and presents the barriers as the
instruments that made the localization exact). Same theorems, positive arc. Authorities:
`reports/2026-07-29-face-E-tier1.md` (assembled theorem, per-clause statuses, novelty calibration) and
`reports/2026-07-30-v1.7-derivability-barrier.md` (compiled schema, §4b derivability precision).
Refine-not-rewrite honored: Theorem 3.1 and its development are untouched as the spine.

## Standing protocol (run first)

- **Mirror-refresh**: `mirror-refresh-2026-07-30/` rebuilt at session start to source `29013d6`
  (superseding the same-day export @ `6c280fd`; delta OPEN_TRAILS only), and rebuilt again after the paper
  commit to source `f48afd7` (delta SIEVE_CEILING_LEMMA v1.1 + REGISTRY p2-3 row). 19 files flat + MANIFEST,
  zip 20 entries, local = remote verified at both pins.
- **Pre-pass rowgen**: `generate` over the paper's cited terminal set at SIDE-kernel v1.7 = `2957e7d` —
  all 8 exist, profiles verbatim below; `constellation` over the pre-revision paper — **0 flags**.
  Source verified v1.0.3 and read complete before editing.

## The revision (PLACE-papers `f48afd7`, pushed, local = remote)

- **S1** Title/subtitle per the ruling. **Filename NOT renamed** — `SIEVE_CEILING_LEMMA.md` stays; the
  spec says the rename is the author's call, reported not assumed. REGISTRY p2-3 carries the new title
  against the old filename; say the word and a `git mv` + REGISTRY/backlink pass executes it.
- **S2** Abstract + new §1.1 ("The reduction, the localization, and the convergence") open on the three
  achievements: RH reduced to the single clause `h2` with the reduction compiled
  (`ConservationBridge.riemann_hypothesis`, the standard three axioms); the residue localized ("the space
  is the wall", residue paper cited as Seale 2026g — new reference); the residue's object-for-object
  coincidence with the Weil-positivity number-field shadow as evidence the localization is faithful.
  Barriers presented as targeting results throughout; the opening does not touch limitation until the
  achievements are on the table.
- **S3** Face E Tier 1 folded in as **§3.4**, the worked instance of Theorem 3.1 (existing §3 numbering
  undisturbed; the assembled theorem lands as **Theorem 3.7**): named six-tool T with the checkable-property
  table, Euler product excluded by construction, self-duality constraint stated (principal/ambiguous class,
  Q ≅ Q⁻¹, ξ_Q self-dual); witness pair ξ and ξ_Q of the principal form of discriminant −23 (h = 3);
  clause-(i) agreement table, all six PROVED-FOR-BOTH with citations, stronger density estimates explicitly
  scoped OUT with the honest reason (T not widened); clause (ii) Davenport–Heilbronn 1936 with the two-part
  citation (181–185 & 307–312) and the two programme-located zeros (0.953+16.29i, 0.798+29.55i, cited to the
  residue paper §5); Theorem 3.7 with per-clause status attached and the three status words defined in-text.
  **The §4b precision stated plainly and flagged as the most easily-missed point**: the raw invariance form
  at (ξ, Z) needs ¬(P ξ ↔ P Z) ⟺ P ξ ⟺ RH, so the paper uses the derivability corollary, which assumes
  nothing about ξ's truth — one agreeing counter-witness suffices; "T does not *derive* P(ξ)", not "T does
  not *determine* P".
- **S4** Novelty calibration as new **§1.4** in the introduction (old §1.4 → §1.5): ninety-year folklore
  credited as the report does (Davenport–Heilbronn 1936; Potter–Titchmarsh 1935; Titchmarsh's book;
  Bombieri–Hejhal 1995; Voronin 1975; Bombieri 2000) — new = T-specification, BGS witness-pair framing,
  machine-checked schema. Stated before a referee can.
- **S5** Correspondence section added (back matter, standard five columns, 12 rows, no blank Status).
  Verified table below.
- **S6** Placement section added (back matter, adjacent to Correspondence, per the constellation standard
  F.2026-07-29-e): constellation order explicit — principal results are the reduction + localization; this
  paper supplies the method-limitation instruments and is read alongside the residue paper, the
  Unconditional Surround, and the monograph; "what this paper does not claim" enumerated (no RH proof, no
  h2 discharge, folklore-not-discovery, Euler-product necessity not sufficiency, dichotomy still conjecture,
  Tier 2 not claimed).
- **S7** Jargon/law pass: work-rail notes naturalized into prose (the kernel-gate and cross-ref italic
  blocks in §4.1/§5.2/§5.4/§8; dated re-scope stamps dropped from body text, kept in Version history);
  banned-word sweep clean (0 hits before and after); clause-status vocabulary (PROVED-FOR-BOTH / PROVED /
  DERIVES) and "Tier 1/Tier 2" defined at first use; axiom-phrasing law observed ("the standard three
  axioms" written in full); title-law check on every heading (new headings name objects/conditions).
- **S8** Version v1.0.3 → **v1.1** with a provenance entry naming this pass; changelogs moved to a
  back-matter Version history block (front matter now title/byline/version-line only, per
  F.2026-07-29-e). REGISTRY p2-3: new title, v1.1, words ~9,600, **status REVIEW**.

### Repairs made in-pass (reported, not silent)

1. **Proposition 3.5 witness display corrected**: the text displayed `Z(s) = Σ (m² + 23n²)^{−s}` and called
   the form "indefinite". The discriminant−23 principal form is the positive-definite `m² + mn + 6n²`
   (disc(m²+23n²) = −92, and the form is positive-definite, not indefinite). Display corrected to match the
   authority report's witness; the surrounding claim (h(−23) = 3, no Euler product) was already correct.
   Noted in the v1.1 changelog.
2. **§6 refreshed to the v1.7 compiled state**: new §6.1 lists the four compiled layers (semantic core,
   dichotomy + scaffolding forms, witness architecture, barrier schema); the old "The programme has executed
   this elevation for RH (SIDE-kernel v1.0, 0 sorry, 0 axioms)" — a stale published-line boast — re-scoped
   to the compiled reduction-under-`h2`. The formalization-plan list stays as §6.2 (remaining components).
3. **TECHNE.Core naming removed from §6** (private repo named in a public-facing paper, claim not
   verifiable from D:) — replaced by the compiled-layer statement above.

## Correspondence table (verified on D:, rowgen `generate` at v1.7 = `2957e7d`, 2026-07-30)

| terminal | `#print axioms` (verbatim) | defenc |
|:--|:--|:--|
| `proof_dichotomy` | does not depend on any axioms | false |
| `sieve_ceiling` | does not depend on any axioms (docstring: SCAFFOLDING) | false |
| `bright_access_required` | does not depend on any axioms (docstring: SCAFFOLDING) | false |
| `e_difficulty` | depends on axioms: [propext, Quot.sound] | false |
| `SieveCeilingSemantic.sieve_ceiling_semantic` | does not depend on any axioms | false |
| `SieveCeilingWitness.dh_witness` | does not depend on any axioms | false |
| `InvarianceBarrier.invariance_barrier` | does not depend on any axioms | false |
| `InvarianceBarrier.derivability_barrier` | does not depend on any axioms | false |
| `ConservationBridge.riemann_hypothesis` | depends on axioms: [propext, Classical.choice, Quot.sound] | false |

The paper's Correspondence rows carry these profiles verbatim; the two SCAFFOLDING-docstringed base
terminals are graded "Scaffolding" in the paper's Status column (never DERIVES), matching the rowgen
status-vs-docstring rule. Clause-(i) tools and clause-(ii) divergence are manuscript-resident/literature
rows; the full dichotomy row is research-reach. No blank Status cells.

## Rider (a) — `hadObs_blind` → `hadObs_dark` (SIDE-kernel `44895f9`, pushed, local = remote)

Word-law hygiene, authorized. References checked first: **no paper cites the former name** (PLACE-papers +
relay grep clean); in-kernel references were two (the `hadamard_does_not_enforce_online'` use and the
`AxiomCheck_C7Witness.lean` audit line), both updated. Rename target `hadObs_dark` describes the situation
in the module's own vocabulary (constant reading = the κ = 0 dark case) rather than substituting a synonym;
the docstring records the former name and date. Statement and proof unchanged. `lake build` green
(**3595 jobs**); audit re-run byte-identical modulo the identifier — all four Voice7Witness declarations
"does not depend on any axioms", including the rail-cited `hadamard_does_not_enforce_online`. Post-v1.7
commit on main; **v1.7 tag = `2957e7d` unmoved** (verified by rev-parse after push).

## Rider (b) — post-commit rowgen over the revised paper

- **constellation** (corpus root + revised paper): **0 flags**.
- **rowgen diff** (paper Correspondence table vs records at pins, all 9 configured terminals incl.
  `ConservationBridge.riemann_hypothesis`): **all rows `ok`** — no status-vs-docstring, no rounded profile,
  no stale pin, no missing terminal, no defenc-graded-DERIVES.
- Reverse-direction note (due diligence, not a new flag source): the corpus files citing this paper at
  "v1.0" (FOUNDATIONS ×3, INTERFACE_DARKNESS ×1, one 2026-05-19 cluster synthesis) were stale before this
  pass and are exactly the filed `W-ORD-CONSTELLATION-BACKLOG` ground; the retitle adds a title-staleness
  dimension to those same rows. Queued pass unchanged.

## Pins

- PLACE-papers: `f48afd7` (paper v1.1 + REGISTRY p2-3), pushed, local = remote. Mirror rebuilt at this pin
  (zip ready for the author's Project upload).
- SIDE-kernel: `44895f9` (rename), pushed, local = remote; v1.7 tag = `2957e7d` unmoved, still the paper's
  citation pin.
- Filename question open for the author: keep `SIEVE_CEILING_LEMMA.md` or `git mv` to follow the new title.
- Nothing deposited; deposit set untouched.
