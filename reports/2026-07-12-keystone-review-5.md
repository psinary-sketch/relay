# Keystone review 5 — The Additive–Multiplicative Conspiracy v0.2 (2026-07-12)

**Document:** `phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md` (was `TYPE_D_EXCLUSION.md`; md5 of source verified `6f1228303451a6523a43e8b3e5a32a0e` before editing).
**PLACE-papers commit:** `4924040` (pushed; `1cf60de..4924040`).
**Pass:** author-ratified T1–T9 scope ruling. Complete-read-first; refine-don't-rewrite.

## T1 — the scope ruling (controls everything)
"Structurally proved, analytically open" **retracted** from the Abstract, §VI, and §IX; §IX's "the historical difficulty is not 'we don't know whether they hold'" retracted. Replaced with the **classification thesis**: the three conjectures share one obstruction-shape, their negations differ only in analytic content; the finite-modulus no-conspiracy is compiled; M3/M4/M5 are the entire analytic weight, where the theorems live — not "operational completion." **Status phrase throughout:** "the classification is compiled; the conjectures are open, their shared difficulty located." §II.2/III.2/IV.2 swept: what the negation requires is consistent with all finite-modulus statistics; the compiled exclusion rules out finite-modulus-unexplained couplings only.

## T2 — §VI boundary paragraph
Added: the step from every-finite-modulus consistency to global density is a **local-to-global interchange**; the programme's compiled bracket in `SIDE-lv-conservation` governs exactly this shape — `T3.T3doubleprime_general_commutation_fails` (unrestricted commutation false by explicit countermodel) and `T3.T3prime_shared_witness` (closes under a shared witness); for these conjectures the shared witness *is* the analytic content (M3/M4/M5). Cross-referenced *The Unconditional Surround of ξ* for the same bracket in the RH setting.

## T3 — Milestones honesty (VERBATIM read of `SIDE-effects/SIDEEffects/Milestones.lean`)

The kernel-side wrappers are **already honest** — real types with `sorry` at the analytic boundary, **not** True-typed (so **no kernel work-order needed**):

```
namespace AddMult

theorem twin_primes_infinite :
    ¬(∃ N : ℕ, ∀ p > N, ¬(Nat.Prime p ∧ Nat.Prime (p + 2))) := by
  sorry  -- MILESTONE: Hardy-Littlewood asymptotic

theorem goldbach :
    ∀ n : ℕ, n ≥ 4 → (∃ k : ℕ, n = 2 * k) →
      ∃ p q : ℕ, Nat.Prime p ∧ Nat.Prime q ∧ p + q = n := by
  sorry  -- MILESTONE: circle method or Helfgott-style approach

theorem sophie_germain_infinite :
    ¬(∃ N : ℕ, ∀ p > N, ¬(Nat.Prime p ∧ Nat.Prime (2 * p + 1))) := by
  sorry  -- MILESTONE: sieve density bounds

end AddMult
-- "3 theorems, 3 sorrys, 0 axioms."
```

The paper's §II.5/III.5/IV.5 previously displayed **True-typed wrapper shells** (`… (density_positive : True) : True := trivial`). These are **retired**: each §X.5 now shows the real set-aside form above (statement in full, declared open, analytic requirement named). No `True := trivial` shells remain in the paper.

## T4 — classification-code naturalization
Primary term **"additive–multiplicative conspiracy"**; "(internally classified Type D)" once at first use (Abstract). §I taxonomy introduced by what each class **is** — Closed (TYPE I), Structurally-located-analytically-open (TYPE II), Out-of-method-reach (TYPE III), Cross-domain coupling / additive–multiplicative conspiracy (TYPE D) — A_METHODOLOGY's labels parenthesized once. Compiled identifiers (`no_type_d`, `TypeD`, `no_type_d_conspiracies`, `no_conspiracy_*`) verbatim. Grep-verified: only the single §I `(TYPE D)` label and the first-use `(internally classified Type D)` remain; zero stray prose codes.

## T5 — retitle
Title "The Additive–Multiplicative Conspiracy"; subtitle "One Obstruction-Shape Behind Twin Primes, Goldbach, and Sophie Germain Primes". `git mv` to `ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md`. *(Note: because >50% of the content changed this pass, git recorded the change as delete+create rather than a rename; history is still followable via `git log --follow`.)*

## T6 — kernel citations
SIDE-kernel v1.1 → v1.2 (tag `b1407b2`; v1.1 DOI retained as citable deposit, superseded-profile clause). "The SIDE programme verification layer" → the named repo **`SIDE-effects`** (`c66f3c5`). The Abstract's layer-wide "0 sorry, 0 axioms" (which contradicted §VIII.1's own milestone-`sorry` disclosure) **scoped** to the specific structural theorems (`Module1.no_type_d_conspiracies`, `crt_exhaustiveness`, `no_type_d`); the milestone wrappers each carry one `sorry`, stated in the same list.

## T7 — vocabulary
§VI "closes the gap to the full statement" → "supplies the density lower bound the full statement additionally requires." §VIII.2 heading → "Open formalization problems"; all (high/medium priority) tags stripped. gap/blind grep: zero unexcepted "gap" (Maynard/Zhang "bounded gaps between primes" is standard terminology, not filler); zero "blind."

## T8 — Correspondence (verified on D:)
Kernels audited at SIDE-effects `c66f3c5`; SIDE-kernel `ce5d7bd` (v1.2 = `b1407b2`). Verbatim `#print axioms`:

```
SIDEEffects.Phase15.Module1.no_type_d_conspiracies   [propext, Classical.choice, Quot.sound]
SIDEEffects.Phase15.Module1.crt_exhaustiveness       [propext, Classical.choice, Quot.sound]
AddMult.no_type_d                                    does not depend on any axioms
ECondition.type_I_has_ostrowski                      [propext, Quot.sound]
SilenceTheorem.silence_universal                     does not depend on any axioms  (hypothesis I.is_universal)
AddMult.twin_primes_infinite / goldbach / sophie_germain_infinite   carry sorry (open)
```

| Claim | Kernel | Theorem | Axiom profile | Status |
|:--|:--|:--|:--|:--|
| Finite-modulus no-conspiracy | SIDE-effects `c66f3c5` | `Module1.no_type_d_conspiracies` (via `crt_exhaustiveness`) | `{propext, Classical.choice, Quot.sound}` | Compiled — rules out finite-modulus-unexplained couplings only |
| General exclusion lemma | SIDE-effects `c66f3c5` | `AddMult.no_type_d` | axiom-free (none) | Logic lemma — weight carried by its hypothesis |
| Per-conjecture instantiations | SIDE-effects `c66f3c5` | `no_conspiracy_twins/goldbach/sg` | — (uniformly-True) | Placeholder — retired from claim structure |
| M3 / M4 / M5 | SIDE-effects `c66f3c5` | `AddMult.twin_primes_infinite` / `.goldbach` / `.sophie_germain_infinite` | carries `sorry` | Open — the conjectures' analytic content |
| Mechanism Theorem | SIDE-kernel v1.2 | `ECondition.type_I_has_ostrowski` | `{propext, Quot.sound}` | Compiled |
| Universal Silence | SIDE-kernel v1.2 | `SilenceTheorem.silence_universal` | axiom-free (none) | Compiled — hypothesis `I.is_universal` |

**Flag (queued, NOT edited this pass):** GRH Cascade §VI's ABC passage inherits this scope ruling — a reciprocal edit (naturalize + scope the ABC "no additive–multiplicative conspiracy" claim to the same finite-modulus reading) is queued.

## T9 — header / REGISTRY
Header v0.1 → v0.2 with a provenance line naming the scope ruling. REGISTRY row **p2-27** updated via a row-update block (new title/filename, v0.2, REVIEW); the prior framing-hold note is addressed by the naturalization.

## Notes
- No deposit action taken.
- The scope ruling weakened only claim-verbs; no mathematics was altered.
