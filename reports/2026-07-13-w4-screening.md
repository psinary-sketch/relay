# W-4 uncommitted tree — recovered, screened, NOT merged (2026-07-13)

An uncommitted working tree was found at `D:\SIDE-effects` during the gate-1 re-grade. It was
**preserved first, screened second, and left unmerged**: the work is real and the build passes, but
one screen fails, and the failure is an author ruling, not an executor call.

## Preserved

Branch **`w4-recovery-2026-07-13` = `d0c4814`**, pushed to origin. A snapshot, not an endorsement.
The work can no longer be lost.

**File dates:** `Phase15/Module1.lean`, `SIDEEffects.lean` — **2026-05-31**; `Structural.lean`,
`Milestones.lean`, `README.md` — **2026-06-16**. Four to six weeks uncommitted, unpushed, invisible
to CI.

## What the tree is: two work-orders, not one

**1. W-4 (discharge) — done, and done properly.** The four open cases of `to_modular_correct` are
*proved, not deleted*. The induction was restructured: a new `StructuralCoupling.period`, `period_pos`
and `eval_periodic` (`eval n ↔ eval (n % period)`, proved case-by-case via `periodic_lift`,
`Nat.lcm`, `Nat.add_mod`) carry the mathematics, and `to_modular := ofPeriodic sc.period …` is proved
correct by `ofPeriodic_eval` — a classical filter over `ZMod L` with honest `ZMod.val_natCast`
reasoning. Zero `sorry`. The wrong-but-compiling `shifted` definition is gone. `SIDEEffects.lean` now
imports `Phase15.Module1`, so the module is **in the build target** — W-4's third clause.
**Full `lake build`: 8318 jobs, exit 0.** Module1 replays with no `sorry` warning; the only `sorry`
warnings are Milestones' three, the disclosed analytic boundary, unchanged.

**2. W-2 (withdraw) — executed, and never ruled on.** `Structural.lean` drops from **34 declarations
to 3**. Deleted: `Massless`/`mass_gap`, `LSZero`/`no_ls_zero`, `RankMismatch`/`mismatch_absent`/
`bsd_full`, `TwinFinite`/`GoldbachFails`/`SGFinite` and the three `no_conspiracy_*` instantiations,
`ShaGrows`/`sha_bounded`, `artin_from_grh`, `side_exclusion`, `twist_cancels`, `gap_bounds`, and 17
more. Surviving: `formation_seven`, `AddMult.TypeD`, `AddMult.no_type_d`. The two remaining `=> True`
strings are **inside comments** — a *retirement ledger*. The README records a "Phase S.2–S.4 audit"
finding the deleted items were True-valued stubs or opaque-Prop templates.

**Dated 2026-06-16 — four weeks before the salt-check named them.** For the third time in this wave,
the source layer had already found what the paper layer was still asserting.

## The failing screen (3b): `TypeD` is redefined smaller

`StructuralCoupling`'s constructors gained positivity hypotheses — `residue (q) (hq : 0 < q)`,
`divisible (q) (hq : 0 < q)`, `coprime (m) (hm : 0 < m)`. The statements of `to_modular_correct`,
`crt_exhaustiveness`, `TypeD` and `no_type_d_conspiracies` are **textually identical** to the pin, but
they now quantify over a **strictly smaller type**: the same sentence over fewer objects. The standing
screen is explicit — *a narrowed `TypeD` fails even at zero `sorry`* — so it does not pass on an
executor's authority.

**It is not a dodge, and that is the point of the ruling.** The cases are genuinely proved; the
narrowing is what the *new proof route* requires (`period` of a zero-modulus constructor is 0, and
`ofPeriodic` needs `0 < L`). And the pinned claim is **not false** at zero modulus: `residue 0 a`,
`divisible 0`, `coprime 0` denote singletons (`{a}`, `{0}`, `{1}`), and a singleton *is* representable
as a `ModularCoupling` at modulus 0 (`ZMod 0 = ℤ`) — `ModularCoupling` is unchanged in the tree. The
old generality was reachable; the periodicity route simply does not reach it.

## Rulings needed

1. **The narrowing.** *(a)* Accept it — zero-modulus "couplings" are degenerate singletons, not
   couplings in the intended finite-modulus sense — merge, and **name the scope in the Correspondence
   rows** (the exclusion covers positive-modulus structural couplings); rows then upgrade to DERIVES
   at the new pin. *(b)* Restore the pinned generality by handling the degenerate constructors outside
   the periodicity route, then merge with no caveat.
2. **The withdrawal** — the larger of the two. Deleting claim-bearing declarations from a public kernel
   changes what live citations resolve to. Pinned citations (EXCLUSION_ENGINE v2.1 §II/§III quotes
   these at `c66f3c5`) are unaffected; live citations must be re-pointed before the deletion lands.

## Status

**Nothing was merged. SIDE-effects `main` remains at `c66f3c5`.** The papers remain correct to cite the
pin, and the pin still carries `sorryAx`. Screens 2b, 2c, 2d, 3c, 3d and 3e (build) pass; only 3b fails.

Ledgers: OPEN_TRAILS `O.16 addendum` (`230e0ad`); VERIFICATION_LOOM `GATE-1 ADDENDUM II` (`fd5ba3f`).
