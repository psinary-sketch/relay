# W-LI face 2 runs · the triviality pre-screen fails · two notes filed — 2026-08-05

Pins at open: PLACE-papers `576a481`; relay `6b96037`; lv main `2f71068`; kernel `44895f9`.
Rail at the post-rename baseline. Nothing deposits.

---

## §1 — W-LI FACE 2

### 1a. THE NOVELTY CHECK AT CITE — run FIRST, and it fires

**Two verdicts, kept apart.**

**FOUND-AT-CITE — the ζ-side measurement, at depth this pass could not approach.**
Johansson (2013; *Rigorous high-precision computation of the Hurwitz zeta function and its
derivatives*, Numerical Algorithms; implemented in Arb) computed the **Keiper–Li coefficients
λ₀ … λ₁₀₀₀₀₀ rigorously**, with accuracy between roughly 33 000 and 2 900 digits, and **all of
them are positive.** The Riemann Hypothesis is equivalent to the positivity of that sequence, and
an explicit λₙ < 0 would be a disproof.

**This lands on the registered expectation directly.** The registration read: *"the arc's first
measured placement channel, with a known-answer calibration."* **It is not first.** The ζ-side
placement measurement exists in the literature, rigorously, at n = 10⁵ — two orders of magnitude
beyond anything this pass reaches, with certified error bounds this pass does not have. The
correct filing is **FOUND-AT-CITE, and the arc's contribution here is not a measurement of ζ.**

**NOT-LOCATED — the specific composite.** After four searches and a primary-source fetch I did
not locate a stated theorem of the form *"RH ⟺ the Toeplitz matrix of the Cayley moments
(cₙ = Σ_ρ zₙ^ρ, z = 1 − 1/ρ) is positive semidefinite."* The **ingredients are all classical**:
the trigonometric moment problem is solvable iff its Toeplitz matrix is PSD (Toeplitz /
Carathéodory / Herglotz), and Bombieri–Lagarias (1999) derive Li's criterion from a general set
of inequalities for an arbitrary multiset of complex numbers.

**But NOT-LOCATED is the weaker reason not to claim the composite, and the stronger reason is
mathematical: as stated, it is not well-posed.** c₀ = Σ_ρ 1 diverges — ζ has infinitely many
zeros — so the "moment sequence" does not exist without a regularization. What converges is
λₙ = Σ_ρ [1 − zₙ^ρ], the Li coefficient, which is the regularized object and is exactly what the
literature already uses. **The programme should not claim the Toeplitz composite as a
reformulation of Li's criterion**, because the sequence it is a Toeplitz matrix *of* is not
defined. What the instrument below actually builds is the Toeplitz matrix of a **truncated** sum,
which is a different object with a different meaning.

### 1b. THE POWER CLAUSE — stated before the measurements, and it needed correcting

Witness: the programme's located disc −23 off-line zero, β = 0.9533, γ = 16.290, δ = β − ½ =
0.4533. The escaping Cayley modulus is **|z_out| = 1.0017067485**, so log|z_out| = 1.70529×10⁻³
against the asymptotic δ/γ² = 1.70822×10⁻³.

**The ferry's formula is accurate: γ²/δ = 585.4 against the exact e-folding depth 586.4, 0.2%.**
But the e-folding depth is not the detection depth, and the difference is the whole power clause:

| detector | depth needed | why |
|:--|--:|:--|
| magnitude (\|cₙ\| clears 5× background) | **n ≈ 5101** | log(2.5·B)/log\|z_out\| with B = 2400 measured |
| **Toeplitz min-eigenvalue** | **K = 200, i.e. n = 199** | measured, §1d |

**The Toeplitz form is ~26× cheaper in depth than the magnitude form**, and that ratio is the
only operational content the Toeplitz reformulation turned out to have in this pass.

**A background-definition caution, filed because it bit once already.** The earlier face-2 pass
reported detection at n ≈ 2282 using √(2N) ≈ 69 as the noise floor; this pass measures B =
max|cₙ| = 2400. The two differ by 35×, and n_det moves from ~3000 to ~5100 accordingly. **The
"noise floor" is a choice, not a measurement, and the detector's reported depth is only as good
as its statement.** Both numbers are printed here so neither can be quoted without the other.

### 1c. THE ζ ARM HAS NO PLACEMENT POWER — the salt-check, run before its verdict was read

**This is the pass's decisive finding and it is structural, not statistical.**

For unit-modulus points z_j, the Toeplitz matrix is
`T_ab = c_{a−b} = Σ_j z_j^{a−b} = Σ_j (v_j v_j*)_ab` with `v_j = (1, z_j, z_j², …)`. **It is a sum
of rank-one PSD matrices, so it is PSD for every on-line set whatsoever.** The ζ arm's inputs are
built as `0.5 + iγ` — **the real part is imposed, not measured** — so its PSD verdict is a
property of the construction and carries no information about ζ.

Demonstrated as well as proved, with two controls sharing exactly one property with ζ's zeros
(they lie on the line):

| K | ζ arm | 1200 random ordinates | 1200 in arithmetic progression |
|--:|--:|--:|--:|
| 100 | −4.386×10⁻¹¹ | −5.624×10⁻¹¹ | −5.962×10⁻¹¹ |
| 200 | −1.164×10⁻¹⁰ | −1.496×10⁻¹⁰ | −1.275×10⁻¹⁰ |
| 400 | −2.104×10⁻¹⁰ | −2.227×10⁻¹⁰ | −1.729×10⁻¹⁰ |

**A maximally un-ζ-like on-line set gives the same verdict to within a factor of 1.3.** The arm
returns float64 roundoff and nothing else.

**This is the π₀ refutation's shape, in a different register**: there the statistic's definition
omitted the real parts; here the pipeline *supplies* the real parts as input. **Either way the
measured quantity takes the same value for every placement of the zeros, which is the definition
of zero placement power.** W-LI face 1 licensed this channel on the ground that λₙ is computable
*without* placement input — and the implemented pipeline does not do that. **The instrument built
is not the instrument face 1 licensed.**

### 1d. THE WITNESS ARM — the detector calibrates, and calibrates well

The known-answer control fires. Decision rule fixed in advance: detected when the witness arm's
Toeplitz min-eigenvalue is more negative than 100× the ζ arm's measured floor at the same order.

| K | ζ (floor) | witness | ratio | detected |
|--:|--:|--:|--:|:--|
| 140 | −7.91×10⁻¹¹ | −1.33×10⁻¹⁰ | 1.7 | no |
| 180 | −1.63×10⁻¹⁰ | −6.25×10⁻⁹ | 38 | no |
| **200** | −1.16×10⁻¹⁰ | −4.79×10⁻⁸ | **411** | **yes** |
| 400 | −2.10×10⁻¹⁰ | −2.64×10⁻² | 1.3×10⁸ | yes |
| 1200 | −6.66×10⁻¹⁰ | −9.40×10² | 1.4×10¹² | yes |

**Detected at K = 200, consuming c₀ … c₁₉₉.**

**But the control is synthetic, and that limit is load-bearing.** The quadruple is *injected* at
the Epstein witness's measured parameters; the Epstein object's own zeros are not used. **A
synthetic control calibrates the DETECTOR; it does not measure the object.** Running the real
disc −23 arm needs an Epstein zero census (the class-group decomposition into Hecke L-functions
at h = 3) — **a named, priced build, not run this pass.**

### 1e. THE RE-PRICE — and a guess of mine that the data refuted

I wrote into the instrument that halving δ should roughly double the required order, so cost
linear in 1/δ. **The sweep refuted it and the script's gloss is corrected in place:** dropping δ
by 453× (0.4533 → 0.001) cost only 4× in order (K 200 → 800). At δ = 0.001, K·log|z_out| = 0.003
— **no exponential amplification at all.** The detector works because a kernel r^|a−b| with r > 1
fails to be positive-definite **at any r > 1**, not because the signal grows.

Pushing to failure, at fixed K = 1200:

| δ | min-eig | ratio to floor | min-eig/δ |
|--:|--:|--:|--:|
| 10⁻² | −3.09×10⁻¹ | 4.6×10⁸ | −30.9 |
| 10⁻⁴ | −2.08×10⁻⁵ | 3.1×10⁴ | −0.208 |
| 10⁻⁵ | −1.98×10⁻⁷ | 297 | −0.0198 |
| 10⁻⁶ | −1.80×10⁻⁹ | 2.7 | −0.0018 |

**The right-hand column falls by ~10 for each factor 10 in δ, so the signal scales as δ², not δ**
— a second corrected gloss. The detector fails at δ ≈ 3×10⁻⁶, which is exactly where a δ² signal
meets the float64 floor. **The limit is arithmetic precision, and it is bought with precision
rather than depth** (resolution scales as √floor). Nothing structural stops it.

### 1f. VERDICT

**Registered:** *"the witness shows the off-line signature at the predicted depth and ζ does not
— the arc's first measured placement channel, with a known-answer calibration; the witness
failing to show it at reachable depth is an INSTRUMENT verdict, not an object verdict."*

**SPLIT, and both halves file:**

- **The witness half — CONFIRMED, and better than predicted.** Detected at K = 200 where the
  power clause predicted n ≈ 5101 for the magnitude form; the Toeplitz form is 26× cheaper, and
  resolves δ down to 3×10⁻⁶ in float64 with the limit purchasable.
- **The ζ half — REFUTED as a measurement, on two independent grounds.** *At cite:* the ζ-side
  measurement is Johansson's, rigorous, at n = 10⁵, and this channel is not first. *At the
  instrument:* the ζ arm has **zero placement power by construction** — proved structurally and
  demonstrated against two controls. **"ζ does not show the signature" is not a finding; it is
  what the pipeline was built to say.**

**This is an INSTRUMENT verdict throughout and files as such. No claim about ζ is made or
retracted.** The arc's positive residue is a **calibrated detector with a measured resolution
law**, which is worth having and is not what was registered.

**What would make it a ζ instrument:** feed it arithmetic-side λₙ (face 1's licensed route),
which requires ~n digits of working precision — the cost Johansson paid, and the reason his
n = 10⁵ needed ~10¹⁰ bits.

---

## §2 — RIDING LIGHT: THE TRIVIALITY PRE-SCREEN — **FILES AS FAILED**

**Registered:** *"the trivially-closed terminals carry more unclosed clauses — if it holds, the
salt-check gains a cheap pre-screen; if it fails, it files as failed and no screen is adopted."*

The first parser was broken (it mis-tokenized `;`-chained tactics and read a docstring line as a
theorem name); it was fixed before any number was read, and only the fixed run is reported.

**Row-level correlation:** triviality share 0.19 / 0.07 / 0.80 against clause counts 1 / 2 / 3
gives Pearson r = **+0.78 — the predicted direction.** *It supports nothing.* n = 3, and the
correlation is driven entirely by D-2c, which is the same single object as the test below.

**Terminal-level precision, which is decisive.** Across 40 terminals the screen flags 12:

- **RECALL = 1/1** — it catches `ladder_three`, the one terminal the D-2 pass found to be a
  definitional restatement.
- **PRECISION = 1/12 = 0.083.** Excluding three term-mode accessors no reader would mistake for
  content, still 1/9 = 0.111.

**The decisive pair, both flagged TRIVIAL:**

| terminal | tactics | what it is |
|:--|:--|:--|
| `heine_three` | `unfold; ring` | the Heine/Vandermonde identity in **six free variables** |
| `ladder_three` | `field_simp` | a restatement of a definition |

**A screen keyed on tactic shape cannot separate them, because the tactic reports how the goal
was discharged and not what the goal said.** `ring` closing a six-variable polynomial identity
and `field_simp` closing a definitional rearrangement look identical from outside.

**VERDICT: FAILED. No screen is adopted**, exactly as the registration directed. The
high-recall/low-precision shape is *not* filed as a triage either — recall of 1.0 measured on a
single known positive is one data point, and adopting a triage on it would repeat the error the
compiled salt-check was invented to stop.

---

## §3 — THE HEADS-PREDICT-STIPULATION NOTE (Tier N, reading grade)

**The observation.** D-2a's single unclosed premise — Duursma's self-dual functional equation —
is a **free-layer item**: the functional equation is MacWilliams's gift to every self-dual
enumerator, failing members included, which is head 4's property exactly. D-2b's three — Mallows–
Sloane, Gleason uniqueness, the certificate construction — are **certified-closure items**: they
are what makes the catalogue of genus ≤ 5 enumerators close, which is head 1's property exactly.
**So the canonical heads did not merely index these stipulations after the fact; they name the
kind of thing each formalization had to assume — which is a forecast, and forecasting is a
stronger office than indexing.**

**Its test, run immediately against D-2c, and the result is PARTIAL.** D-2c stipulates two
things. The **instance scope** (K = 3, exactly three atoms) is a certified-closure item — head 1
predicts it, and the prediction holds. The **Jacobi link** (that the Hankel-ratio coefficients
are the monic-OP recurrence coefficients) is an identification between two constructions of one
object, and **it maps onto no head cleanly** — it is not a free-layer gift, not a closure
certificate, not a triviality of structure, not a register separation. **One of two stipulations
was forecast; one was not.** The claim therefore stays at **reading grade and is not promoted**,
with its next test named: the stipulations of the next terminal compiled, checked against the
four heads *before* it is written, not after.

---

## §4 — THE RULE-HYGIENE CLAUSE, FILED

**The rule:** *a standing rule that has not fired within a stated number of sittings is reviewed
for redundancy.* The symmetrical guard against machinery outpacing use — the corpus has spent the
week adding rules, and every one of them is a permanent reading cost for whoever comes next.
**Review threshold set at TEN sittings without a firing.** Review means examined for redundancy
against the rules that did fire; it does not mean automatic retirement.

**This week's eight rules, dated, with their firing record as the review's start point:**

| # | rule | filed | last fired |
|--:|:--|:--|:--|
| 1 | the joint-row rule | 2026-08-05 | 2026-08-05 (D-2b's row) |
| 2 | the statement-versus-claim shortfall register | 2026-08-05 | 2026-08-05 (all three D-2 rows) |
| 3 | the D-2 grading rule | 2026-08-05 | 2026-08-05 (D-2a's upgrade) |
| 4 | OVER-HYPOTHESIZED (Correspondence grade) | 2026-08-05 | 2026-08-05 (`type_I_has_ostrowski`) |
| 5 | probe the descriptions, not only the artifact | 2026-08-05 | **2026-08-05, twice** — the manifest, then two false glosses in this pass's own instruments |
| 6 | the compiled salt-check as standing form | 2026-08-05 | 2026-08-05 (D-2a) |
| 7 | the voice rule | 2026-08-05 | 2026-08-05 (keystone v0.14) |
| 8 | refusal criteria for the four canonical heads | 2026-08-05 | 2026-08-05 (the supplier column ruled a catalogue) |

**All eight fired within the week they were filed, so none is yet due.** The clause's value is
prospective, and the start point is now on the record so the first review has something to
measure from. **Rule 5 is the one to watch and the one that most earns its place** — it fired
twice today, the second time against instruments written in this very pass.

---

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `576a481` → this pass's commit |
| relay | `6b96037` → this report's commit |
| SIDE-lv-conservation | main = `2f71068` — unmoved |
| SIDE-kernel | `44895f9` — unmoved; the generalization work-order stays open at the author's call |
| rail | `de621b1` / `2147a03` — at the post-rename baseline |

Instruments: `tools/e16/wli_face2_run.py`, `wli_face2_toeplitz.py`, `wli_face2_resolution.py`,
`tools/audit/triviality_prescreen.py`. The R4 compression question stays registered and unrun.
Consolidation DEFERRED. Nothing deposits.

## SOURCES

- [Johansson, *Rigorous high-precision computation of the Hurwitz zeta function and its derivatives*](https://arxiv.org/pdf/1309.2877) — the Keiper–Li record computation (λ₀…λ₁₀₀₀₀₀)
- [Arb: Efficient Arbitrary-Precision Midpoint-Radius Interval Arithmetic](https://arxiv.org/pdf/1611.02831) — the implementation and its precision cost
- [Li's criterion (Wikipedia)](https://en.wikipedia.org/wiki/Li%27s_criterion) — the criterion and the Bombieri–Lagarias generalization
- [A Li-type criterion for zero-free half-planes of Riemann's zeta function](https://arxiv.org/pdf/math/0507368) — primary source fetched for the composite check
- [Recurrence relations of Li coefficients](https://arxiv.org/pdf/2006.13103)
