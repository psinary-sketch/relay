# W-INFORMATION — the information-theoretic horizon, first sitting (orient + state)

*2026-07-28. Read-first done at source: `E_DIFFICULTY_THEOREM.md` (v1.0.3), `phase2/formation/COMPRESSION.md`, the `SIDE-compression` kernel (`ChainLength.lean`), the E-Difficulty terminals (`e_difficulty` at `{propext, Quot.sound}`, `proof_dichotomy`, `sieve_ceiling_semantic`, `dh_witness`; FINDINGS L177), and the substrate-scoping finding. This sitting ORIENTS and STATES; it draws no compose-vs-restate conclusion — that is the run. Work-plan priced and HELD. Nothing deposits.*

## What the two conjectures claim, at current grade

**The E-Difficulty Theorem.** For a determined system X with I+D+S structure and a universal property P: **P is decidable ⟺ a domain Ostrowski exists for the P-mechanism catalogue** (a finite mechanism-class enumeration + a certificate it is exhaustive). Forward (Ostrowski→decidable) is the SIDE method; reverse (decidable→Ostrowski) is the substantive content — any proof of P contains an implicit mechanism-class enumeration, because dark interfaces force placement-information through per-class bright paths. *Grade:* the **skeleton is compiled** — `e_difficulty` at `{propext, Quot.sound}`, de-vacuified 2026-07-19 (v1.4 `f374174`), "reads its system, DERIVES"; the **full dichotomy** (the reverse direction's Mathlib-dependent κ-machinery) is a **separate research-reach item**, a conjecture with partially-formalized machinery.

**The Compression Theorem.** Under an exhaustive catalogue with per-class finite checks, deriving a universal conclusion over (possibly infinitely many) objects consumes exactly **N per-class checks + one exhaustiveness application — chain length = the formation total N, not the object count.** Corollary of E-Difficulty: the SIDE method is the *minimum-difficulty* proof. *Grade:* the **structural skeleton is compiled axiom-free** (`compression`, `compression_infinite_objects`, `SIDE-compression`) — it certifies the architecture (N checks suffice, independent of |α|); discharging `Exhaustive`/`ClassClear` for a concrete system is manuscript content.

## What the scoped calculus changes about the statements

The substrate-scoping finding (W-REDERIVE-1) makes **Shannon's boundary a theorem-shaped precondition, not an aside.** Both conjectures are stated for "determined systems with I+D+S structure" — but the formation *front-end* is now known to be **substrate-scoped** (the formation *tuple* exists only on an arithmetic substrate; axiomatically-forced systems like Shannon carry none). This forces a precondition question the original statements left implicit: **does E-Difficulty need the arithmetic substrate, or only a finite mechanism catalogue?** The *tuple* (I-bis Step 2) is arithmetic-scoped; the *catalogue / domain-Ostrowski* (I-bis Step 3) may be broader — a determined system can have a finite mechanism enumeration without a prime substrate. The arc must resolve whether E-Difficulty's precondition is "arithmetic substrate" (narrow) or "finite mechanism catalogue" (broad) — Shannon is exactly the test case that separates them.

## The honest question — and the orienting hypothesis (to be tested, not concluded)

**Do the difficulty-kinds typology + the escape-kinds + the missing-object duals COMPOSE into E-Difficulty's predicted structure, or does E-Difficulty need re-statement against the mature typology?**

*Orienting hypothesis (a target for the run, not a verdict):* E-Difficulty was stated (May 2026) before the three-kind typology matured, and its **ladder (THEOREM > SEARCH > FORCED-OR-UNDERDETERMINED > NONE) is precisely the Kind-B (search/termination) axis** — decidability and catalogue-completeness are the *search* shape. **Kind A (pairing/chiasmus)** and **Kind C (height-comparison)** are different shapes: RH's difficulty is whether a positive pairing binds, not whether an enumeration terminates; ABC's is bounding one height by another. So the likely finding is that E-Difficulty **captures one axis** (search/decidability) exactly and **needs re-statement** as one face of the mature typology, not the universal theory of determined-system difficulty. The escape-kinds (horizon/infinitude) and the absence-duals would then refine *within* each kind. **This is the hypothesis the run tests — the read points here, the work confirms or refutes.**

## The work-plan (priced; HELD for the run order)

- **W-INFO-1 (~0.5).** Map the E-Difficulty ladder against the difficulty-kinds at statement grade: is Kind B = the ladder? Do Kind A / Kind C fit the decidability-Ostrowski frame or fall outside it? Verdict: compose vs re-state, per kind.
- **W-INFO-2 (~0.5).** The precondition question: read I+D+S structure vs the mechanism-catalogue requirement — does E-Difficulty need the arithmetic substrate (via the tuple) or only a finite catalogue? Shannon as the separating test case.
- **W-INFO-3 (~0.5).** The Compression Theorem × the missing-object duals: does "chain length = N" connect to the absence-type (Kind A missing-carrier vs Kind B missing-measure)? Does the minimum-difficulty claim survive re-statement?
- **W-INFO-4 (research-reach, ~2+).** The full E-Difficulty dichotomy — the reverse direction's Mathlib-dependent κ-machinery, currently conjectural. The deep item; filed to the ripe list on the run's order.
- **Synthesis.** After 1–3: the one-line verdict — E-Difficulty composes with the typology (and how), or is re-stated as the Kind-B/decidability face with the typology broader.

*No conclusion is drawn here. The read is done; the orienting hypothesis is on the record; the run is ordered by the author.*
