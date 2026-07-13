# W-4 discharged, W-2 withdrawal landed — 2026-07-13

The uncommitted SIDE-effects tree recovered and screened earlier today (see
`2026-07-13-w4-screening.md`) was ruled on by the author — **narrowing accepted** — and has landed.

**New SIDE-effects pin: `a27415d1aa0ce6f6d87c47bb59fd72791190af35`** (merge of
`w4-recovery-2026-07-13` = `d0c4814`; prior pin `c66f3c5`).

## Order of operations

Preserve → screen → rule → **pin-convert** → merge → profile → upgrade.

The pin-conversion came *before* the merge deliberately. The merge deletes 31 declarations from a
public kernel, which changes what live citations resolve to. A sweep of the corpus found:
`BSD_VIA_FORMATION_TRANSFER` and `ADDITIVE_MULTIPLICATIVE_CONSPIRACY` citing the retired declarations
as live kernel text (both pin-converted to `c66f3c5` with retirement notes, PLACE-papers `ee24a8b`);
`YANG_MILLS_MONOGRAPH` already disclosing the retirement in its own words; `EXCLUSION_ENGINE` v2.1
already quoting them at the pin; ledger mentions historical by construction. **The citations moved to
the pin before the ground moved under them.**

## What landed

**W-4 — closed, all three clauses.** The four `to_modular_correct` cases are *proved*, via a
restructured induction (`StructuralCoupling.period` / `period_pos` / `eval_periodic`, with
`to_modular := ofPeriodic …` correct by `ofPeriodic_eval`). The wrong-but-compiling `shifted`
definition is gone. `Module1` is in the build target, so CI can see its `sorry`s — there are none.
Full `lake build`: **8318 jobs, exit 0**.

**W-2 — withdraw option enacted** for the SIDE-effects shells (work done 2026-06-16, four weeks
before the salt-check named them). `Structural.lean`: 34 declarations → 3, with a retirement ledger
in comments. The *replace-with-real-predicates* option stays open only where something still claims
those results; as of today's sweep, nothing does.

## Scope, carried in every upgraded row

**The exclusion holds for positive-modulus structural couplings.** The constructors now carry
positivity hypotheses (`0 < q`, `0 < m`); the degenerate zero-modulus cases are released as singletons
(`{a}`, `{0}`, `{1}`). They were **not false** at the old pin — a singleton *is* representable as a
`ModularCoupling` at modulus 0 — so the generality is recoverable, and restoring it is filed as its own
trail (OPEN_TRAILS O.19). A narrowing accepted *with its scope named in the row* is a different act
from a narrowing that slips through unnamed.

## Profile at the new pin — run under the sharpened rule

```
tree:    git status --porcelain --untracked-files=no → EMPTY
HEAD:    a27415d1aa0ce6f6d87c47bb59fd72791190af35
date:    2026-07-13 18:43:01
command: lake env lean AxiomAudit_w4.lean  (#print axioms)

'…Module1.no_type_d_conspiracies' depends on axioms: [propext, Classical.choice, Quot.sound]
'…Module1.crt_exhaustiveness'     depends on axioms: [propext, Classical.choice, Quot.sound]
'…Module1.to_modular_correct'     depends on axioms: [propext, Classical.choice, Quot.sound]
```

No `sorryAx`. The `Classical.choice` is honestly earned (`Classical.decPred` in `ofPeriodic`), not
inherited from a stub.

**This closes the loop on this morning's near-miss.** The earlier run returned *exactly this string*
and was **not** evidence — it profiled a dirty working tree while the question was about a commit. The
identical string is evidence now, because the state it profiled is a pushed commit and the tree was
clean when it ran. Same output, same command, same terminals; the difference is entirely in what the
tree was. *A profile is a measurement of a tree; a citation is a claim about a commit. They are the
same sentence only when the tree is the commit.*

## Rows upgraded

| Paper | Row | Now |
|---|---|---|
| GRH_CASCADE v0.3.2 | conspiracy exclusion | **DERIVES** at `a27415d`, scope named |
| GRH_CASCADE v0.3.2 | ABC | **DERIVES** at `a27415d`, scope named |
| ADDITIVE_MULTIPLICATIVE_CONSPIRACY v0.2.2 | finite-modulus no-conspiracy | **DERIVES** at `a27415d`, scope named |

## Trails

- **W-4 — CLOSED** (all three clauses, at `a27415d`).
- **W-2** — withdraw option recorded as executed; replace option open only where something still
  claims those results.
- **O.19** — restore the pinned generality (degenerate zero-modulus cases, outside the periodicity
  route).
- **O.20 — federation-wide dirty-tree sweep (standing).** A real, building, sorry-free proof sat four
  to six weeks in an uncommitted tree, invisible to CI, and was found *by accident* during an unrelated
  re-grade. Every `SIDE-*` repository gets `git status`; any dirty tree gets preserve → screen → rule,
  in that order. **A dirty tree in a federation repository is an incident, not a state.**

Ledgers: OPEN_TRAILS `db9d997`; VERIFICATION_LOOM + row upgrades `11cf75e`; pin-conversion `ee24a8b`.
