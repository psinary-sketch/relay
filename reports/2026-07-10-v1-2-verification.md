# SIDE-kernel v1.2 — verification & tag run (2026-07-10)

**Relay report.** Resumption of an interrupted v1.2 verification run (prior session
lost to a power failure; state reconstructed from remotes). Outcome: **v1.2 verified,
stale tag remediated, re-cut on the verified commit, deposit notes landed. Zenodo
deposit remains author-gated.**

- SIDE-kernel repo: `github.com/psinary-sketch/SIDE-kernel`
- Verified commit (tag `v1.2` target): `b1407b2231c650d6d938cfa649f589fd388f669c`
- Deposit-notes commit (kernel `main` head): `ce5d7bd737f9cfa1364b415449359ec012176b0d`
- PLACE-papers monograph: `day1/A_Place_to_Stand.md` v5.5 (repo HEAD `a980f21`)

---

## R0 — State audit (reconstruction from remotes)

**SIDE-kernel** — `main` up to date with `origin/main` at `b1407b2`; `f18e143`
present as the CartanBBridge T3 set-aside enactment.

**What `b1407b2` is (reconstruction).** It is the *only* commit past `f18e143`, titled
*"AGENTS: junction-safety rule (2026-07-10 incident)"*. It touches **`AGENTS.md` only
(+6 lines)** — an operational junction-safety rule recorded after a 2026-07-10 junction-
recursion incident. **No Lean source, no theorem statement, no axiom profile is affected
by it.** The mathematical content of the tag is therefore identical to `f18e143`.

Working-tree deviation noted: beyond the two expected author `.bak` files
(`Bridge/CartanBBridge.lean.bak_20260616`, `MetaKernel.lean.bak`), two untracked
leftovers from the interrupted prior session were present —
`AxiomAudit_v1_2.lean` (scratch `#print axioms` module) and
`DEPOSIT_v1_2_NOTES.md.PENDING` (draft notes with `PENDING-S3/S4` placeholders).
Both untracked and benign; used only as cross-checks. Everything re-verified fresh.

**Tags at audit time:** both local **and** remote `v1.2` pointed at the stale
`5260498` (annotated-tag object `a51152e`).

**PLACE-papers** — `main` up to date with `origin/main` at `a980f21`
(*"v5.5 scope correction: CartanBBridge T3 set aside"*); tree clean apart from an
untracked `outputs/` directory.

## R1 — Build recovery

Prior session had restored Mathlib sources at `e960b84` with fresh mtimes (rebuild-storm
risk). Applied the mtime fix first —
`find .lake/packages/mathlib -path "*/.lake" -prune -o -type f -print0 | xargs -0 touch -t 202505010000`
— confirmed Mathlib sources re-dated to 2025-05-01 (nested `.lake` correctly pruned).
`lake build` then completed green in one pass: **3593 jobs, exit 0**, "Build completed
successfully". Only linter warnings (unused simp arguments / variables); zero errors,
zero `sorry`. No cache-get fallback needed. (One Mathlib olean,
`Mathlib.NumberTheory.Ostrowski`, sat outside the default target's closure and was built
on demand for the audit import chain — `Bridge/TheBridgeComplete.lean` imports it.)

## R2 — native_decide census

`git grep "by native_decide" HEAD -- '*.lean'` → **0 matches**. The only textual
occurrence of `native_decide` anywhere in the tracked Lean tree is a prose comment,
`legacy/FmodifProbe.lean:34` (`-- Try native_decide or norm_num`) — non-executable.
Corpus-wide the tactic is eliminated.

## R3 — Axiom audit

`lake env lean AxiomAudit_v1_2.lean` (scratch module) at the verified commit, after build.
Fully-qualified names; `structural_exhaustiveness_proved` (bare, `_root_`) is the
TheBridgeComplete Route-1 terminal, disambiguated from the namespaced
`ConservationBridge.structural_exhaustiveness_proved`. Verbatim:

```
'structural_exhaustiveness_proved' depends on axioms: [propext, Classical.choice, Quot.sound]
'SpectralCannonFull.spectral_cannon' depends on axioms: [propext, Classical.choice, Quot.sound]
'ConservationBridge.riemann_hypothesis' depends on axioms: [propext, Classical.choice, Quot.sound]
'techne_kernel_integration.rh_from_structural_exhaustiveness' depends on axioms: [propext, Classical.choice, Quot.sound]
'techne_kernel_integration.structural_exhaustiveness_iff_rh' depends on axioms: [propext, Classical.choice, Quot.sound]
'SIDEKernel.formation' does not depend on any axioms
'SIDEKernel.formation_count' does not depend on any axioms
'DomainOstrowski.formation_count' does not depend on any axioms
```

Every route terminal named in the monograph §25.8 Kernel Concordance table is exactly
`{propext, Classical.choice, Quot.sound}`; all three formation certificates are
axiom-free. No `sorryAx`, no `Lean.ofReduceBool`, no `_native.native_decide.ax_*`.

**Delta from v1.1** (per PLACE-papers `FINDINGS.md` F.2026-07-10-c): at the citable v1.1
deposit (`e0a8ba0`), Route 1 `structural_exhaustiveness_proved` carried
`seven_classes._native.native_decide.ax_1_1`, and `SIDEKernel.formation` /
`SIDEKernel.formation_count` carried `_native.native_decide.ax_1_1` — all three DIRTY.
Routes 2 and 3 and `DomainOstrowski.formation_count` were already clean at v1.1. v1.2
brings the three v1.1-dirty terminals to the standard-three / axiom-free profile; nothing
regressed. **No deviation → no STOP.**

## R4 — Tag remediation (stale-tag discipline)

The stale `v1.2` (local + `origin`, peeling to `5260498` / tag-object `a51152e`,
pre-`native_decide`-elimination, never deposited or cited) was removed and re-cut:

1. `git push origin :refs/tags/v1.2` — remote deleted.
2. `git tag -d v1.2` — local deleted (was `a51152e`).
3. `git tag -a v1.2 -F <msg> b1407b2` — re-cut annotated on the verified commit.
4. `main` was not ahead of `origin` (0/0) — no `main` push needed at this step.
5. `git push origin v1.2` — new tag pushed.

**SHA triple (verified):**

| | SHA |
|---|---|
| Verified commit (`git rev-list -n1 v1.2`) | `b1407b2231c650d6d938cfa649f589fd388f669c` |
| Remote annotated-tag object (`ls-remote refs/tags/v1.2`) | `82c3a1d48a76d9935d18f3804cdd0eff5f4df014` |
| Remote peeled commit (`ls-remote refs/tags/v1.2^{}`) | `b1407b2231c650d6d938cfa649f589fd388f669c` |

Peeled == verified ✓. Old `5260498` / `a51152e` confirmed **gone** from `origin`.

Tag message (verbatim):

> v1.2: native_decide eliminated corpus-wide; every route terminal at {propext,
> Classical.choice, Quot.sound}; formation certificates axiom-free; CartanBBridge T3
> (Cousin-I/Stein) set aside per loom ruling 2026-06-15 — prior placeholder retired.
> No mathematical changes to theorem statements from v1.1 except the T3 retirement.

## R5 — Repo description

`gh repo edit psinary-sketch/SIDE-kernel --description "…"` set and verified to:

> Lean 4 formalization of the SIDE proof of the Riemann Hypothesis. Three verified
> routes; every route terminal at {propext, Classical.choice, Quot.sound}; 0 sorry.
> PLACE TO STAND programme.

## R6 — Deposit notes

`DEPOSIT_v1_2_NOTES.md` written at kernel repo root (SHA triple, full R3 axiom table,
Zenodo description delta incl. the Routes-2/3-already-clean-at-v1.1 sentence, the
T3 set-aside sentence, and the stale-tag deletion note). Committed on `main` *after*
the tag at `ce5d7bd` and pushed (`b1407b2..ce5d7bd`); the tag stays on the verified
commit `b1407b2`, so the SHA triple above points at the tagged commit, not the notes
commit.

## R7 — Ledger landings (this report)

- PLACE-papers `FINDINGS.md`: appended **F.2026-07-10-d** — SIDE-kernel v1.2 tagged and
  deposit-ready.
- PLACE-papers `REGISTRY.md`: appended a 2026-07-10 version-log block (kernel v1.2
  tag/verify landing).

## Deposit gate

**The Zenodo deposit is not performed by this run.** It remains an author-side decision
behind `DEPOSIT_VERIFICATION_PROTOCOL`. This run verified the tree, remediated the stale
tag, and prepared the deposit notes; the upload is the author's to make.

## Follow-up flagged (out of this append-only pass's scope)

`REGISTRY.md:65` still reads *"Live at HEAD `5260498` (verified 2026-06-04)"* — now
doubly stale (that commit is neither HEAD nor a tag target). Recommend refreshing it to
`b1407b2` / v1.2 at the next REGISTRY hand-edit.
