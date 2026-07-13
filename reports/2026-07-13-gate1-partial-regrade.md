# Gate-1 partial re-grade — 2026-07-13

Next-wave **gate 1** of the 2026-07-12 federation salt-check (re-grade every keystone's
Correspondence rows under the three-grade rubric, at pins), enacted for the three keystones read
this session. Gate 2 (core-terminal statement-read) closed 2026-07-12.

**Rubric.** DERIVES = the kernel proves the content from structure (the only grade that may back a
proved mark). INTERFACES = a conditional whose premise is a *named* manuscript result. SHELL /
ENCODES-CONCLUSION = Boolean set true, predicate uniformly `True`, hypothesis that *is* the claim,
`X = X`, fabricated witness — a work-order, never a citation.

**Pins.** SIDE-kernel `v1.2` (`b1407b2`); SIDE-grh-transfer `858cbf6` (v0.5.0); SIDE-effects
`c66f3c5`; SIDE-silence-principle `v0.1.0`; SIDE-compression `v0.2.0` (= `e9a5a36`);
SIDE-bsd-formation-transfer `7425d73` (v0.1.0); SIDE-yang-mills-formation `79e4f45` (v0.1.0).

---

## The catch: a clean axiom profile on a terminal that cannot have one

`SIDEEffects.Phase15.Module1.no_type_d_conspiracies` was cited in **two keystones** — GRH_CASCADE
(conspiracy-exclusion row *and* ABC row) and ADDITIVE_MULTIPLICATIVE_CONSPIRACY (finite-modulus row)
— carrying the profile `{propext, Classical.choice, Quot.sound}`. **That profile cannot hold at
`c66f3c5`.** The chain, read at the pin:

```
no_type_d_conspiracies
  └─ crt_exhaustiveness  :=  ⟨to_modular sc, fun n => to_modular_correct sc n⟩
       └─ to_modular_correct — induction, six cases:
            residue      DISCHARGED
            divisible    DISCHARGED
            coprime      sorry
            conjunction  sorry
            disjunction  sorry
            shifted      sorry
```

Four of six cases are `sorry`, so the terminal carries `sorryAx` transitively. A clean profile was
**reported** for a terminal that cannot have one, and two papers carried it as evidence. All three
citing rows are corrected: the axiom cell now records the `sorryAx` dependency and states that the
previously reported clean profile was incorrect at this pin; the status cell keeps what is true —
the *statement* is compiled and content-bearing (`TypeD` is a genuine subtype over
`StructuralCoupling`, not a `True`-stub) while the *proof* is partial (work-order W-4).

**Method of reproduction.** Source-level dependency read at the pin (the six-case induction, the four
`sorry` branches, and both construction sites, `Module1.lean:121–167`). A confirming `#print axioms`
run was also launched; it had not finished elaborating at the time of writing — **because
`Module1.lean` is not in the build target**, so the module and its Mathlib dependencies must compile
from source to be profiled at all. That is W-4's third clause, and it is the mechanism of the
failure: *the profile could not have been run when it was reported.* The same blindness produced the
"10 real sorry, not 7" census correction of 2026-07-12. The source chain is definitive regardless;
no citation rests on the pending run.

**This is the second laundering catch at the paper layer.** The first (2026-07-12) was profiling
*shells* — a clean profile of a statement that asserts nothing. This one is the inverse: a clean
profile reported for a statement that is real but **unproved**. Both defeat the instrument the same
way. Hence the standing rule added to the loom: **a reported axiom profile must carry the run that
produced it** — pin, date, command.

## Confirmations (the re-grade is not all casualties)

- **SIDE-grh-transfer twisted balance and the paired-voice chorus — DERIVES.** Genuine Mathlib
  content (prime-unit norm-one; honest unramified hypothesis). This is the real character-side
  mathematics of the cascade.
- **`grh_structural_exhaustiveness_proved` — DERIVES**, with a row-note the kernel itself discloses:
  χ and χ̄ are typed-but-unused parameters of the composite terminal. The character content is
  carried by the twisted-balance and paired-voice rows; `voice1_balance_chi` contains no character at
  all (signature-level real algebra). Cited with the note, not without it.
- **SIDE-compression `Compression.compression` — DERIVES as schema**: N per-class checks plus
  exhaustiveness yield the universal conclusion, chain length N independent of object count. Content
  enters at instantiation, and the row now says so.
- **Mechanism Theorem and the two Mathlib bridges — DERIVE** (the Mechanism Theorem keeps its
  standing note: `[Fintype Domain]` is never used, so the exhaustiveness is decorative).
- **`SilenceTheorem.silence_universal` — INTERFACES**, under the named hypothesis `I.is_universal`.

## Casualties

- **The four sieve-ceiling rows** (`sieve_ceiling`, `proof_dichotomy`, `bright_access_required`,
  `e_difficulty` + `e_difficulty_xi`) in FOUNDATIONS: "Compiled (skeleton)" → **work-order rows
  (W-6)**. The 2026-07-12 work-order, now enforced at the paper layer. Their axiom profiles stay in
  the table as read, with the row stating why a clean profile of a statement that asserts nothing
  certifies nothing.
- **BSD formation-placement and Yang-Mills mass-gap-placement rows** in GRH_CASCADE: **PULLED as
  citations** per author ruling, retained as audit record, graded SHELL — work-order (W-5 family).
  BSD's `formation_preserved` is `decide` over hand-assigned constants — it *records* the formation
  assignment rather than deriving it. Yang-Mills' `mass_gap_equals_n3_certification` proves that a
  `Bool` defined as `true` equals `true`.
- **The silence-principle model rows** in FOUNDATIONS: regraded **Model-level**. `isSilent I :=
  (I.kappa_x100 == 0)`, decided over hand-defined instances whose `kappa_x100` is set to 0 by hand —
  honest as a model, silent about arithmetic. The s-darkness content is bound by SIDE-kernel's
  product-formula chain, and the rows now point there.
- **Pin correction:** FOUNDATIONS' audit line named SIDE-compression `e31d719` (v0.1.0 — the *initial*
  commit) while its Compression row cited v0.2.0. Corrected to `e9a5a36` (v0.2.0).

## Status

Gate 1 stands at **three keystones re-graded** — FOUNDATIONS v0.2.1, GRH_CASCADE v0.3.1,
ADDITIVE_MULTIPLICATIVE_CONSPIRACY v0.2.1 — of the full keystone set; the remainder queue for
per-cluster reads. Row edits: PLACE-papers `7bb65cb`. Loom entry: `0e58b81`.
