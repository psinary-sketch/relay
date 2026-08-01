# The negatives keystone — Tier-K keystone candidate, drafted, checkpointed, HELD for the author's read — 2026-07-31

The queue's remaining item, run under the arc charter. Vocabulary per the author's rider (standing law): "flagship" is retired from class/ledger use — it was a presentation-role word from the day's exhibit list, never a taxonomy tier; the taxonomy is complete at K/C/N. This document files as what it is: a **Tier-K keystone candidate (DRAFT — HELD)** in the RH/h2 proofs cluster — "the negatives keystone" as the short handle. (The rider arrived after the first commit landed; this corrected language rides the follow-up commit, recorded honestly.) Rail frozen at `11db565` — empty-diff verified at
close. Nothing deposits. The draft is **HELD**: `phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE.md` (retitled 2026-08-01, was SIX_NEGATIVES_THREE_SUPPLIERS.md) v0.1,
REGISTRY **1.5a-7** (DRAFT — HELD for the author's read; free-writing law observed — the status lives in
the ledgers, no process scaffolding in the paper body).

**Title (retitled 2026-08-01 per the composite title law; author retitles at will):** *Index Arity at the Critical Line — Instrument Limits, Positivity Suppliers, and the Pair-Index Space on the Zeros.* (Was "The Six Negatives and the Three Suppliers" — counts-as-enframing.) Title law checked:
objects and conditions, no achieved property.

## Read-first executed

The six negatives at their pins (statement-reads at source, quoted below) · the Lee–Yang control report
(`e9d4c52`) · SURROUND §6/§6a · THE_RESIDUE_OF_RH §6 · the Face-E Tier-1 report · the escape-kind
invariant at source (held branch) · title law + Placement law + free-writing law (D4 row of the
interface-harvest taxonomy: conclusions in the document, status in the ledger).

## The spine as drafted (§2 of the paper)

Six negatives, one shape — **a finite certificate together with a certified global escape** — each at its
pin:

| # | terminal | pin | statement-read (compressed) | E0 profile (verbatim runs below) |
|:--|:--|:--|:--|:--|
| N1 | `C7_finite_type_false` | lv v0.10.0 = `93c27ec` (DOI 10.5281/zenodo.21539068) | no (C, A) bounds ‖Λ₀(s)‖ ≤ C·exp(A‖s‖); bracketed to the true maximal-type bound, not edited away | the standard three axioms |
| N2 | `T3.T3doubleprime_general_commutation_fails` | lv v0.10.0 | unrestricted ∀∃ ⟹ ∃∀ over (𝒞, s) false; witnessed at s = 3; Determination does real work in T3′ | the standard three axioms |
| N3 | `RegisterPentagon.certifiedInput_not_zeroRealizing` | lv v0.10.0 | certified {n²} input fails zero-realization under one named classical premise (nontrivial zero in the open strip) | the standard three axioms |
| N4 | `RegisterPentagon.escape_kind_discriminates` / `horizon_kind_shared` | lv **held branch** `4df797a` (held, not landed — status explicit; derivative-engine citation precedent) | sign wall escapes at N₀(T), derivative wall at raw infinitude; horizon-kind shared by the sign wall and its threshold | axiom-free (both) |
| N5 | `InvarianceBarrier.derivability_barrier` | kernel v1.7 = `2957e7d` | general form; assumes nothing of ξ; manuscript instance = Theorem 3.7 of INVARIANCE_BARRIERS | axiom-free |
| N6 | `SieveCeilingWitness.dh_witness` + the located disc −23 zero | kernel v1.7; residue §5 | agreeing pair with the DH off-line datum honestly stipulated; own-instrument zero doubly-sourced (0.9533 + 16.290i, simple) | axiom-free (kernel part); manuscript-resident (computation) |

## Checkpoint (charter §5, per cited terminal)

- **Statement-reads**: run at source for all six (N1–N4 from the lv files — N1–N3 verified
  **tag-identical** between v0.10.0 and the held HEAD before citing at the tag; N4 exists only on the
  held branch, cited as such; N5/N6 statement-reads from the v1.7 records).
- **E0 salt-check, verbatim** (lv combined audit `AxiomCheck_v0_10_0.lean` + a scratch escape-kind
  audit; kernel from the v1.7-pinned records):

```
'SIDELvConservation.C7_finite_type_false' depends on axioms: [propext, Classical.choice, Quot.sound]
'SIDELvConservation.T3.T3doubleprime_general_commutation_fails' depends on axioms: [propext, Classical.choice, Quot.sound]
'SIDELvConservation.RegisterPentagon.certifiedInput_not_zeroRealizing' depends on axioms: [propext, Classical.choice, Quot.sound]
'SIDELvConservation.RegisterPentagon.escape_kind_discriminates' does not depend on any axioms
'SIDELvConservation.RegisterPentagon.horizon_kind_shared' does not depend on any axioms
'InvarianceBarrier.derivability_barrier' does not depend on any axioms
'SieveCeilingWitness.dh_witness' does not depend on any axioms
'ConservationBridge.riemann_hypothesis' depends on axioms: [propext, Classical.choice, Quot.sound]
```

  One tool note, recorded honestly: the first escape-kind audit failed on a **stale olean** (the
  held-branch module had not been rebuilt this session — unknown-constant, not a missing theorem);
  `lake build SIDELvConservation.ZeroActingPairing` rebuilt green (**2991 jobs**) and the audit then
  returned both terminals axiom-free. Build artifacts only (`.lake`); **no lv commit, no kernel commit**.
- **rowgen diff** on the paper's Correspondence table (8-terminal config incl. the held-branch pins):
  **all rows ok** — no missing terminal, no rounded profile, no stale pin, no status-vs-docstring
  contradiction. (Tool notes, recorded honestly: a first run mis-resolved the three lv v0.10.0 terminals
  — executor config error, short names inside the `SIDELvConservation` namespace — compounded by lake-lock
  contention with the concurrent module build; names fully qualified in config AND in the paper's table
  cells, rerun sequential, all-ok. The kernel `ConservationBridge` transient recurred once in the bad run
  and resolved in the clean run, consistent with the v1.2 pass's finding.)
- **rowgen constellation** on the draft: **0 flags in every class** (and REGISTRY/SPIRAL_MAP stay 0
  actionable with the new row).

## The mirror and the frame as drafted (§3–§4)

The three-supplier table (𝔽_q intersection form, PROVED · ferromagnetic pair coupling, PROVED · ℚ named
absence, boundary-tight by Rodgers–Tao) with the **index-arity sort** as the bridge: every ζ-side
positivity single-index and provably edge-reaching; both proved suppliers pair-index; the residue = the
pair-index space = Q. The negatives are the failing side of the same sort — each certificate
single-index/finite-range, each certified escape located at the pair-index boundary. The honest frame on
the paper's face: **not a discharge** (§27.3 named, `h2` open, reduction compiled); **not a no-prism
claim** (two-darknesses: catalogued instruments stop, never no-instrument-exists; open prisms named —
LY-REP-A, the 𝔽₁/arithmetic-surface programs incl. Connes–Consani, the R4 finite-range tail). Lineage
credited entire: Davenport–Heilbronn · Titchmarsh · Pólya · Newman · Rodgers–Tao · Weil · Lee–Yang ·
Asano · Borcea–Brändén · Connes–Consani.

## Filed

- Paper: `phase1.5/proofs/SIX_NEGATIVES_THREE_SUPPLIERS.md` v0.1 (~2,700 words), banned-word clean,
  headings title-law checked, Correspondence (12 rows, no blank Status) + Placement in back matter,
  narrative front per the format doctrine.
- REGISTRY 1.5a-7 (DRAFT — HELD); FINDINGS F.2026-07-31-c (the one-shape finding at grade); OPEN_TRAILS
  arc addendum (UAC-4(d)'s completing research now at the author's-read gate).
- Mirror rebuilt at the pass commit; rail empty-diff at `11db565` verified at close (five rail papers,
  zero output).

## Pins

- PLACE-papers: **`da3d33a`** (paper + REGISTRY + FINDINGS + OPEN_TRAILS), pushed, local = remote
  verified. Mirror rebuilt at this pin.
- SIDE-kernel `44895f9` (v1.7 = `2957e7d`) and SIDE-lv-conservation (v0.10.0 = `93c27ec`; held branch
  `4df797a`) **uncommitted-to and unmoved** — citation-only.
- HELD complete for the author's read; nothing deposits.
