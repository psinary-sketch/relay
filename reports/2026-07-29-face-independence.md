# h2 arc — face-independence test — 2026-07-29

Analytical. The arc was constituted with four discharge faces — **A** analytic/Li tail, **B** spectral/
Hilbert–Pólya, **C** totality/coverage, **D** 𝔽_q/Weil positivity. Independence tested per I+D+S: for each
pair, (i) independent (a discharge of one would not discharge the other), (ii) equivalent (same object,
different vocabulary), or (iii) nested (one strictly implies the other).

## The pair matrix

| pair | verdict | reasoning |
|:--|:--|:--|
| **A ↔ D** | **(ii) equivalent** | Li positivity (`λ_n ≥ 0` ∀n, i.e. `λ_Z(n) ≥ −λ_A(n)`) **is** Weil positivity in the number-field register. Bombieri–Lagarias: `λ_n` is the Weil-explicit-formula sum on the Li kernel, so `λ_n ≥ 0` is the positivity of the Weil functional. D is the *geometric* form of the same positivity — the intersection-form positivity on C×C (Face D control `85c9e5d`). A analytic, D geometric; one clause. |
| **B ↔ D** | **(ii) equivalent / one face** | The 𝔽₁ / arithmetic-site program (Connes–Consani) builds **D's** missing surface *precisely to supply* **B's** operator; Deninger's postulated H¹ *is* both the Frobenius-flow realization (B) and the polarization carrier (D); the Connes trace formula = the Riemann–Weil explicit formula unifies them. The residue names them "two geometric clauses (Hilbert–Pólya **and** Weil positivity)," but the chiasmus shows each is *free given the other* and they cross at **one object** — the positive space on the zeros. |
| **A ↔ B** | **(ii) equivalent (co-dependent)** | The residue's two individually-free clauses (`residue_irreducible`): realization (B) and inequality (A/D). Positivity is free without the zeros (A free); the operator is free given the positivity (B free, de Branges); only the **conjunction** is RH. Neither is independent; each discharged (given the other's freeness) yields RH. |
| **C ↔ A** | **(ii) equivalent (C reduces)** | `covers_all` / the T3 quantifier-commutation is the SIDE-native register; its *residual* content — the **sign** half that forces σ=½ — *is* the positivity clause (SURROUND §6, §27.3: `covers_all` = R3 = R4-positivity = `λ_Z ≥ −λ_A`). The coverage apparatus (exhaustive catalogue + joint-to-single) is real machinery, but the open residue it leaves = A/D. |
| **C ↔ B** | **(ii) equivalent (via A/D)** | C reduces to the positivity (A/D); A/D ↔ B (the two facets of one object). So C ↔ B through the shared object. Coverage is the SIDE vocabulary of the same premise. |
| **C ↔ D** | **(ii) equivalent (via A)** | C's residue = the positivity = A = D. The 𝔽_q positive control (D) is exactly the register where `covers_all`'s sign-forcing is a *theorem* (the intersection-form positivity), and the ℚ obstruction is the missing second dimension — the same wall C's commutation leaves open. |

**No pair is (i) independent.** Every face, discharged, yields RH; a discharge of any is a discharge of all
(§27.3: *"a reader who discharges any one of them discharges all five"*).

## Count of genuinely independent faces = **ONE**

The four "faces" are **four attack registers on one wall**:
- **A** — analytic (Li-coefficient) register;
- **B** — spectral (Hilbert–Pólya operator) register;
- **C** — coverage / totality (SIDE-native) register;
- **D** — geometric (𝔽_q / Weil intersection-form) register;

and the one wall is **the positive space on the zeros = Weil positivity's number-field shadow** — a positive
self-adjoint operator realizing the ζ-ordinates with a positive pairing (the residue's characterized object,
Deninger's H¹ / `XRealization`).

**The arc's structure is corrected** (which is the point): it was constituted as "four discharge faces," any
a partial attack surface; the honest structure is **one irreducible residue, four vocabularies.** The
correction *strengthens* the arc — it is not four separate long shots but one wall approachable from four
sides, and only a full discharge of the one object (both clauses of `residue_irreducible` jointly) wins. The
checkpoint discipline and stopping rule are unchanged; the "four faces" of the OPEN_TRAILS entry now read as
four *registers*, per the dated addendum.

## The Face D convergence claim — the arc's most citable finding to date

**The SIDE reduction's residue coincides, object for object, with the Weil-positivity shadow, and the
reduction to it is machine-verified.** The programme derived its residue independently (the seven-class
exclusion → the one open sign clause → `covers_all` → the positive space on the zeros); the Face D positive
control (`85c9e5d`) shows this residue *is* the number-field shadow of Weil's intersection-form positivity —
the object the extra dimension (C×C) supplies for free over 𝔽_q and that `Spec ℤ`, lacking a second
dimension, does not. And the reduction `ConservationHypothesis → RiemannHypothesis` is compiled
(`ConservationBridge.riemann_hypothesis`, `{propext, Classical.choice, Quot.sound}`). **An independently-
derived residue landing on the century-old understood obstruction, with the reduction to it checked by
compiler** — that is the arc's most citable finding, recorded in the OPEN_TRAILS addendum.

## Rider — internal-consistency fix (authorized rail edit)

rowgen constellation caught `THE_UNCONDITIONAL_SURROUND.md` L106 and the REGISTRY `1.5a-5` row citing *Paths
to the Critical Line* **v0.2** while the file is **v0.6**. Both fixed to v0.6 (one-line diffs) under the same
per-pass authorization as the C₇ repair. **New rail baseline = `11db565`** (supersedes `0696797`);
authorized deviations to date: (1) SURROUND §4 + PATHS C₇ repair `0696797`; (2) SURROUND L106 citation
currency `11db565`.

## Pins

- PLACE-papers `main` — **`2e83999`** (local = remote, clean). Rail empty vs the new baseline `11db565`.
- Rider commit (new baseline) — `11db565`. Face-independence outcome — OPEN_TRAILS addendum (`2e83999`).
- No kernel edited. Nothing deposited.
