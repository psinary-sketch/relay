# `qeps_layer.py` — the operator layer: `Q_ε` via eq. (100), `ε` via (85), `ε′(1⁺)` derived

**Banked 2026-08-15. Formulas supplied at content (Selecta / arXiv-v1 numbering).**
### **This is the layer whose absence suspended the `δ/L` law's grade for two sittings.**

## Why it exists

`prolate_layer.py` certifies the CC prolate / `ε` **substrate** (15/15, pins P1–P3) and stops exactly where
the corpus's own record stopped: *"`Q_ε` (eq. 100), the `Y₊` map and the lag form are **not on disk**."*
Eight banked rows depended on that missing operator — `ε(1) = 0`, `Qε(1) = 0`, the log-2 and log-3 spectra,
the `L = 3` fractions, the five-point `δ/L` table, `C = 0.3448`, the endpoint machine-zeros. **This file is
that operator, written from the supplied formulas and tracked, so it cannot be lost the way the sitting-11/12
instrument was.**

> ### **THE LAW IT SITS UNDER: *untracked artifacts are outside the apparatus.*** *The scar that law was
> written for was a stale backup; the `δ/L` instrument was the same law meeting a **missing original**.*

## The formulas, as supplied — verbatim, not paraphrased

```
(b)  ξ_n^an(x)     = (2/λ) ∫₀¹ ξ_n(t) cos(2π t x) dt            [entire]
     (ξ_n^an)′(x)  = −(4π/λ) ∫₀¹ t ξ_n(t) sin(2π t x) dt
     ζ_n(x)        = [λ/√(1−λ²)] ξ_n^an(x)  for x ≥ 1, else 0

(c)  ε(ρ), their (85), ρ ≥ 1:
     ε(ρ) = Σ_n [λ/√(1−λ²)] ⟨ξ_n | θ(ρ⁻¹) ζ_n⟩
     integrand supported ONLY on u ∈ [ρ⁻¹, 1]   ⟹  ε(1) = 0

(d)  Q_ε, their Prop 5.3 / eq. (100), ρ > 1:
     Qε(ρ) = Σ_n [λ²/(1−λ²)] C_n(ρ)
     C_n(ρ) = ρ^{1/2}  ∫_{ρ⁻¹}^{1} [x (ξ^an)′(x)][ρ x (ξ^an)′(ρ x)] dx
             + ρ^{−3/2} (ξ^an)′(ρ⁻¹) ξ^an(1)
             − ρ^{3/2}  ξ^an(1) (ξ^an)′(ρ)
     Qε(1) = 0 identically.
```

## The conventions, pinned — without which nothing identifies

| pin | content |
|:--|:--|
| **P1–P3** | inherited from `prolate_layer` and `README_prolate.md`. `λ(n)` EVEN-INDEXED and signed, `c = 2π`; `‖ξ‖² = ∫₀^∞|ξ|²` so `ξ_n = √2·ψ_{2n}`; `ξ_n^an` via `η_n = Fξ_n = λ(n)·ξ_n^an`. |
| **THE SCALING OPERATOR** | `θ(a) f(x) = a^{1/2} f(x/a)`. ### **NOT chosen — FORCED by the supplied support law:** `θ(ρ⁻¹) ζ_n(u) = ρ^{−1/2} ζ_n(ρu)` is nonzero for `u ≥ ρ⁻¹`, which against `ξ_n` on `[0,1]` gives exactly the stated support `[ρ⁻¹, 1]`. *The alternative convention gives the wrong support and fails `ε(1) = 0`.* |
| **SIGN OF `λ`** | `lam = √(μ_{2n})` unsigned. **Legitimate here because `C_n` is EVEN in `ξ^an`**, so the sign cancels; each `ξ_n` is additionally oriented to `ξ_n(1) > 0` to fix the arbitrary eigenvector sign. |
| **TRUNCATION** | `NTERM = 11` — **Lemma F.1: the first 11 terms are uniform to `10⁻¹¹`.** Not a tuned parameter. |

## The consequence DERIVED here, not assumed

**Differentiating (85) at `ρ = 1`:**

```
ε′(1⁺) = Σ_n [λ²/(1−λ²)] ξ_n(1)²
```

### **— which is exactly the `t(n)` of CC Lemma 5.4, inferred STRUCTURALLY in resurrection part 2 and now
DERIVED from the supplied formula.** *Part 2 had to read `t(n) = λ(n)²ξ_n(1)²/(1−λ(n)²)` off two of the
corpus's own sentences (correction 13's "was computing `Σλ²/(1−λ²)` exactly" and sitting 9's "the missing
factor was `ξ_n(1)²`"). This file obtains the same expression from eq. (85) itself.* **Two independent
routes to one formula; `epsprime1()` implements it.**

## Certification rows this layer passes

| row | computed | target | verdict |
|:--|--:|--:|:--|
| ### **`ε(1)`** | `0` — machine zero | `0` exactly *(the support law)* | ### **PASS** |
| ### **`Qε(1)`** | `0` — machine zero, identically | `0` exactly *(their remark)* | ### **PASS** |
| ### **`ε′(1⁺)`** | ### **`22.9964757`** | `22.996476` — CC Lemma 5.4 | ### **PASS, `Δ = 3.2×10⁻⁷`** |
| `ε′(1⁺)`, third route | `22.99644` — finite differences on `ε` itself | same | ### **PASS** |

> ### **`ε′(1⁺)` IS CONFIRMED BY THREE INDEPENDENT ROUTES:** *the `t(n)` sum · the derivative of (85) ·
> finite differences on `ε`.* **No fitted constant anywhere in this file.**

## Boundary — what this layer does NOT settle

* ### **THE COEFFICIENT OF THE PRIME TERM IS SUPPLIED AT `q = 2` ONLY.** *The `Φ` form carries
  `2√2 log 2 · (η⋆η*)(log 2)` and nothing fixes the generalization to other prime powers.* **See
  `README_battery.md` §boundary and `PLACE-papers` `THE_EULER_SPECIFICATION` §14: the question is not
  adjudicable on this bench.**
* **The quadrature orders (`NQ = 700` prolate nodes, `NG = 400` Gauss points on `[ρ⁻¹,1]`) are convergence
  parameters, not physics.** *Every banked row above was re-checked at coarser and finer settings before
  landing.*
* ### **NOTHING HERE BEARS ON `h2`, ON `W_∞ − W_2`, OR ON ANY OPERATOR INEQUALITY.**

## Run

```
python -c "import qeps_layer as Q; print(Q.eps(1.0), Q.Qeps(1.0), Q.epsprime1())"
python -c "import qeps_layer as Q; print(Q.Qeps([1.5,2.0,3.0]))"
```

`numpy`; `prolate_layer` for the substrate (which uses `mpmath` once, for `Si(4π)`). No scipy.
