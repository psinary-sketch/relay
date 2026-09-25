#### `W-ORD-SEAM-UPSTREAM` — OPEN, named not started, filed b537 on `(R147)`(4)

**Trigger: the author`s word.** Starts from `SIDE-explicit-formula/SIDEExplicitFormula/Seam.lean:25` at `v0.2` = `5c72cad24303f23d92256ebd466d3a3d32424a4b`:

```
theorem zeta_zero_re_nonpos : ∀ z : ℂ, riemannZeta z = 0 → z.re ≤ 0 → ∃ n : ℕ, z = -2 * (n + 1) := by
```

`zeta_zero_re_nonpos` is a Mathlib-shaped lemma about zeta`s trivial zeros, priced for an upstream contribution in Mathlib`s form. Nothing is sent upstream by this entry.

#### `W-ORD-REGISTER-DEPTH` — OPEN, named not started, filed b537 on `(R147)`(4)

**Trigger: the act after b537, unless the author rules otherwise.** R1, R3, R5 of §27.3 read for statability in SIDE-explicit-formula and, where statable, the closure of their equivalence to RH, against b512`s table — relay `data/b512_closing.txt:5-7`:

```
forms : R1 NOT STATABLE ; R2 NOT STATABLE ; R3 NOT STATABLE ; R4 STATABLE ; R5 NOT STATABLE ; LI2 NOT STATABLE ; LI STATABLE ; CELL STATABLE ; RH STATABLE ; H2 STATABLE
implications : H2 -> RH STATABLE-NOT-COMPILED ; RH -> H2 STATABLE-NOT-COMPILED ; RH -> LI STATABLE-NOT-COMPILED ; LI -> RH STATABLE-NOT-COMPILED ; H2 -> LI STATABLE-NOT-COMPILED ; LI -> H2 STATABLE-NOT-COMPILED ; H2 -> CELL COMPILED ; CELL -> H2 STATABLE-NOT-COMPILED ; RH -> CELL STATABLE-NOT-COMPILED ; CELL -> RH STATABLE-NOT-COMPILED ; LI -> CELL STATABLE-NOT-COMPILED ; CELL -> LI STATABLE-NOT-COMPILED
weakest : ['CELL'] -- a statement about derivability, not a theorem
```

**The ruling`s words, verbatim** (relay `data/b537_ferry.txt`, hard wrap normalised): *"(4) Two work-orders are named, not started: W-ORD-SEAM-UPSTREAM — zeta_zero_re_nonpos (Seam.lean) is a Mathlib-shaped lemma about zeta's trivial zeros and is priced for an upstream contribution in Mathlib's form, trigger: the author's word; W-ORD-REGISTER-DEPTH — R1, R3, R5 of §27.3 read for statability in SIDE-explicit-formula and, where statable, the closure of their equivalence to RH, against b512's table, trigger: the act after this one unless the author rules otherwise."*
