# Tautology-sweep dispositions + rail re-freeze — 2026-07-29

Two closures on the federation tautology sweep (`reports/2026-07-29-tautology-sweep.md`). Author-ruled.

## (1) CLAIMING-bucket dispositions — hygiene, not correction

None of these terminals is cited by any paper (the only ever-cited claiming tautology, `c7_forces_half`,
was repaired earlier). So this is hygiene. All actions logged in `OPEN_TRAILS` (the sweep-dispositions
addendum) so no bucket item closes by label alone (F.2026-07-29-c). **SIDE-kernel `derivative-engine`
`3b2e8d6`, build green (3536 jobs).**

- **(a) Route-D/E `: True` equivalences — renamed, placeholder status now in the name.**
  `SimplicityRouteD.topological_equivalence → topological_equivalence_placeholder`;
  `SimplicityRouteE.energy_positivity_equivalence → energy_positivity_equivalence_placeholder`
  (both `: True := trivial`, uncited, nothing imports them — checked). Docstrings now state what the real
  statements would have to say (Route D: the IVT sign-change / non-crossing characterization; Route E:
  E = F²+F′² > 0 ⇔ all on-line zeros simple). Faithful formalization filed as work-order
  **W-ORD-ROUTE-DE-EQUIV**, trigger *"before any paper cites a Route D or Route E equivalence."*
- **(b) Labeling stubs — deprecated in place, docstrings pointing at the genuine terminals.**
  `TriviumCode.code_n/code_k/code_d` (`7=7/1=1/3=3`) and `interface_dark` (`0=0`) → point at
  `SteaneExemplar.steane_parameters` and `ProductFormula.conservation_of_spectra` / `partition_cardinalities`;
  `Enumera.F6_aperture_denom` (`7=7`) → `SIDEKernel.formation`; `F18_units` (`8=8`) → its genuine sibling
  `F18_totient24 : Nat.totient 24 = 8`. Kept in place (nothing imports them — checked), not removed.
- **(c) `legacy/Foundation4v2.conservation_s_dark : True`** — left as-is (legacy tree, outside the ship
  build); noted as known.
- **(d) DECORATIVE** (`voice4_modular`, `math_passes_level_0`, the `assembly : True` markers) — no action;
  already recorded, uncited, no surviving overclaim.

## (2) Rail re-freeze — new baseline

The RH-rail-untouched invariant took its **first authorized break**: the C₇ repair edited
`THE_UNCONDITIONAL_SURROUND.md` §4 and `PATHS_TO_THE_CRITICAL_LINE.md` (one-line diffs each), both at commit
**`0696797`**, under explicit per-pass author authorization.

- **New frozen rail baseline = `0696797`.** Future rail-untouched checks run `git diff 0696797..HEAD` on the
  five rail files (`THE_RESIDUE_OF_RH`, `A_Place_to_Stand`, `PATHS_TO_THE_CRITICAL_LINE`,
  `THE_UNCONDITIONAL_SURROUND`, `SIMPLICITY_OF_RIEMANN_ZEROS`), expecting empty until the next authorized
  break. **Verified now: `0696797..HEAD` (HEAD = `e045a15`) on the five rail files = `[]`.**
- **Authorized deviations from the historic `67da789` baseline:** SURROUND §4 + PATHS (C₇ repair), both at
  `0696797`. The `67da789` baseline is retired for rail-diff purposes (it now shows those two deviations).
- **Standing rule:** every subsequent RH-rail edit requires the same explicit per-pass author authorization,
  and each break is recorded (OPEN_TRAILS) with its commit and a baseline update.

## Pins

- SIDE-kernel `derivative-engine` — **`3b2e8d6`** (local = remote).
- PLACE-papers `main` — **`e045a15`** (local = remote, clean). **New rail baseline = `0696797`.**

No rail file edited this pass (OPEN_TRAILS only). Nothing deposited.
