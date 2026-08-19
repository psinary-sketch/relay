# THE SORRY LEDGER CLEARED — THE FOUR REMOVED STATEMENTS, VERBATIM, WITH SKETCHES AND WAITS-ON
## ### **THE STANDING RULING (2026-08-19, the author's; the navigator's error owned as correction 28): NO SORRY IS BUILT INTO A KERNEL. A statement we cannot prove stays in the working layer until it can enter proved. "Labeled sorry with an owner" is RETIRED as a device.**

**Relay working-layer record · 2026-08-19 · each removed declaration verbatim, its argument
sketch, and what it waits on · these re-enter kernels only as PROVED theorems (or, at a future
ferry's explicit word, as file-E-style `Prop` DEFINITIONS — not chosen unilaterally here) ·
nothing deposits · nothing circulates**

---

## 1. `LocalLimit.padicFourierData_exists` (was: the B–C broad debt)

**Statement, verbatim:**
```lean
theorem padicFourierData_exists (p : ℕ) [Fact p.Prime] :
    Nonempty (PadicFourierData p) := by sorry
```
**Sketch:** instantiate `PadicFourierData` over `L²(ℚ_p)`: the transform from file B's
`fourier` (now with UNIT 1 proved both branches) extended to an isometry via Plancherel;
`F² = parity` from the transform's composition law; the Sonin closure as the double-vanishing
subspace; the escape property from `general_p_no_fixed_cell` (proved) through the realization.
**Waits on:** file B's remaining units (the transform on the full test space; Plancherel by the
tower — the level-DFT identification as a Lean statement; the isometry extension). The
`PadicFourierData` STRUCTURE (no sorry) remains in the kernel.

## 2. `GlobalSection.globalSectionData_exists` (was: the broad assembly debt)

**Statement, verbatim:**
```lean
theorem globalSectionData_exists : Nonempty GlobalSectionData := by sorry
```
**Sketch (the act-5 path, priced):** (i) index by places, local space = the completed Sonin
limit, unit = the `E₁` vector; (ii) the algebraic restricted tensor product as the colimit of
finite tensors along unit-inclusions; (iii) the inner product (almost-all factors pair
unit-to-unit at 1) and the Hilbert completion. **Waits on:** item 3 below (the inner core), then
one assembly session. The `GlobalSectionData` STRUCTURE (no sorry) remains in the kernel.

## 3. `GlobalSection.restrictedTensor_innerCore_exists` (was: the sharp `⊗′` debt)

**Statement, verbatim:**
```lean
theorem restrictedTensor_innerCore_exists
    (ι : Type) (H : ι → Type) [∀ i, NormedAddCommGroup (H i)]
    [∀ i, InnerProductSpace ℂ (H i)] (unit : ∀ i, H i)
    (hunit : ∀ i, ‖unit i‖ = 1) :
    Nonempty (InnerProductSpace.Core ℂ
      (Submodule.span ℂ {z : PiTensorProduct ℂ H |
        ∃ x : ∀ i, H i, {i | x i ≠ unit i}.Finite ∧
          z = PiTensorProduct.tprod ℂ x})) := by sorry
```
**Sketch:** the pre-inner-product on almost-unit pure tensors by the finite product of local
pairings; well-definedness on the span via multilinearity against a fixed finite support;
positive semidefiniteness from the local Cauchy–Schwarz products. **Waits on:** new Mathlib
territory (no inner product on `PiTensorProduct` exists); 2–3 sessions per the standing order.

## 4. `QuotientCount.offball_scaling_pair_count` (was: file D)

**Statement, verbatim:**
```lean
theorem offball_scaling_pair_count (p n k : ℕ) [Fact p.Prime]
    [NeZero (p ^ (2 * n))] (h1 : 1 ≤ k) (hkn : k < n) :
    (Finset.univ.filter fun mm : ZMod (p ^ (2 * n)) × ZMod (p ^ (2 * n)) =>
      (p : ZMod (p ^ (2 * n))) ^ k * mm.2 = mm.1 ∧ ¬ (p ^ n ∣ mm.1.val)).card
      = p ^ n * (p ^ n - p ^ k) := by sorry
```
**Sketch (the act-9 longhand proof, complete; PLUS the simpler route found at this clearing):**
the pair set is the graph of `m' ↦ p^k·m'` — the filter bijects with
`{m' : p^k·m' off-ball}`, whose complement has `p^{n+k}` elements
(`p^n ∣ p^k·m' ⟺ p^{n−k} ∣ m'`), so the card is `p^{2n} − p^{n+k} = p^n(p^n − p^k)`. **Waits
on:** one Lean session (`ZMod` divisibility counting; the graph bijection). The FILE (file D)
is removed whole — it contained only this statement; the longhand proof lives at
`THE_GLOBAL_SECTION.md v1.0 §2.2` and the act-9 report.

## 5. NOT removed — PROVED at this clearing: `PadicFourier.fourier_indicator_zp_not_mem`

*(Unit 1b — the translation-vanishing; the docstring's one-page argument formalized; see the
kernel and this sitting's report for the print.)*

**THE LEDGER AFTER THE PASS: 0. Every kernel file prints 0 sorries; the statements above live
HERE until they can enter proved.**
