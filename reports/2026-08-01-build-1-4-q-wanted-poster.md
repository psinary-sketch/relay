# BUILD-1+4 checkpoint — the Q wanted-poster kernel + the Δn₄ row — 2026-08-01

First pass of the h2 build slate (order as ruled: 1+4 arm the screen the others report into).
Charter §5 discipline run; findings-before-interpretation observed (the screen's validation was
designed to be falsifiable: a wrong candidate had to FAIL). Kernel lands **HELD** on the
SIDE-lv-conservation held branch `word-pairing-interface` = **`5a14205`** (child of `4df797a`;
pushed for preservation per the preserve-no-merge precedent — held, NOT landed, not on the release
line, nothing deposits). PLACE-papers untouched this pass; rail frozen at `11db565` (empty-diff
verified at the sitting close, recorded in the companion consult-note commit).

## What was built

**`SIDELvConservation/QWantedPoster.lean`** (new module, imports the held-branch typed
specification `ZeroActingPairing` — it layers on the existing interface rather than duplicating):

1. **`QConstraint`** — the wanted-poster constraint set enumerated: pair-index carrier ·
   positive-on-FE-even (**the unpinned clause** — residue §6: "pins every property except the
   positive polarization") · realizes-target-spectrum · carries-ledger-trace ·
   distinct-from-certified-input. Every constraint's docstring sources its rail/monograph
   derivation: THE_RESIDUE_OF_RH v1.1 §6, monograph §27.3 register 5, SURROUND v0.4 §6/§6a, the
   Face-D control, the Lee–Yang control, `certifiedInput_not_zeroRealizing` in-repo.
2. **`CandidateProfile` + `screen`** — the finite model-level summary and the conformance
   conjunction. ANTI-OVERCLAIM carried in the module header: profiles are Boolean summaries;
   passing the screen constructs nothing; the existence of a conforming instance over ℚ remains
   exactly the disclaimed clause (pentagon precedent — STRUCTURE compiled, never the equivalence).
3. **The validation — the screen earns its grade by discriminating:**
   - `intersectionFormProfile` (Weil's route, Face-D control) → **PASS** (`rfl`).
   - `lyCouplingProfile` (the circle theorem, Lee–Yang control) → **PASS** (`rfl`).
   - `certifiedInputProfile` (the known-wrong candidate: the certified `{n²}` input) → **FAIL**
     (`rfl`) — and `certifiedInput_fails_on_realization` compiles the exact failure shape: the
     positivity and ledger clauses TRUE, the realization clause FALSE — "positivity is free; the
     obstruction is realization" at profile level, with the FALSE warranted by the in-repo
     compiled negative under its named premise.
   - `screen_discriminates` — the conjunction, one term.
4. **BUILD-4, riding:** `formationTuple_Fq = (2,3,2,1)`, `formationTuple_Q = (2,3,2,0)`;
   **`delta_n4_count`** (DERIVES, `decide`): the first three coordinates agree and n₄ differs by
   exactly one. **`DeltaN4Row`** carries the cohomological reading (the absent-H² codomain) as a
   named-premise **slot** — a `Prop` field, never asserted; grade INTERFACES, the identification
   never forced. `deltaN4Row_of_reading` discharges the count clause now; the reading waits.

## E0 salt-check (verbatim)

Build green (**2992 jobs**). All seven terminals:

```
'SIDELvConservation.QWantedPoster.screen_discriminates' does not depend on any axioms
'SIDELvConservation.QWantedPoster.screen_passes_intersectionForm' does not depend on any axioms
'SIDELvConservation.QWantedPoster.screen_passes_lyCoupling' does not depend on any axioms
'SIDELvConservation.QWantedPoster.screen_fails_certifiedInput' does not depend on any axioms
'SIDELvConservation.QWantedPoster.certifiedInput_fails_on_realization' does not depend on any axioms
'SIDELvConservation.QWantedPoster.delta_n4_count' does not depend on any axioms
'SIDELvConservation.QWantedPoster.deltaN4Row_of_reading' does not depend on any axioms
```

0 sorry, 0 native_decide. Statement-reads: the module builds directly against the held-branch
`ZeroActingPairing` (its four typed clauses re-read at source this sitting) and the v0.10.0
`certifiedInput_not_zeroRealizing` (statement re-read in the keystone pass, unchanged).

## Grade, stated plainly

The screen is **model-level structure** (DERIVES for the discrimination theorems as compiled;
the PASS rows are literature-anchored assignments of proved instances' shapes, not re-proofs; the
FAIL row is warranted by a compiled negative). BUILD-1's deliverable — a conformance screen that
provably discriminates the two proved suppliers from a known-wrong candidate — is met. What it
does NOT do: construct Q, narrow the residue, or upgrade any INTERFACES row. W-ORD-DELTA-N4-H2's
count half is discharged (`delta_n4_count`); its reading half remains the open INTERFACES slot,
as filed.

## Pins

- SIDE-lv-conservation held branch `word-pairing-interface` = `5a14205` (pushed, held, not landed).
- Release lines unmoved: lv v0.10.0 = `93c27ec`; SIDE-kernel `44895f9`, v1.7 = `2957e7d`.
- Next per the slate order: BUILD-2 (LY-REP-A necessary conditions — inequality set registered
  before computation), then BUILD-3 (the 𝔽_q phase screen).
