# THE WAVE-WIDE CORRESPONDENCE RE-GRADE — SITTING 1 — 2026-08-09

Slate item 1, the hard blocker on pass 2. Method as ruled: **rowgen diff + constellation mode first,
then statement-read per row under the three-grade rubric.** Rail at `de621b1` / `2147a03`.
**Nothing deposits. No row is re-graded downward this sitting; three are CONFIRMED.**

---

## §1 — SCOPE ESTABLISHED

**Twelve keystone papers carry a Correspondence section**, plus three registers (README, SPIRAL_MAP,
VERIFICATION_LOOM) that carry rows without being keystones.

**Ninety-nine distinct terminals are cited inside those Correspondence sections**, extracted from the
sections themselves rather than from whole files, so module paths and prose backticks do not inflate
the count:

| paper | terminals cited |
|:--|--:|
| PATHS_TO_THE_CRITICAL_LINE | 31 |
| THE_UNCONDITIONAL_SURROUND | 29 |
| SIMPLICITY_OF_RIEMANN_ZEROS | 21 |
| INDEX_ARITY_AT_THE_CRITICAL_LINE | 19 |
| FOUNDATIONS_OF_THE_SIDE_PROGRAMME | 13 |
| GRH_CASCADE | 11 |
| ADDITIVE_MULTIPLICATIVE_CONSPIRACY | 10 |
| INVARIANCE_BARRIERS | 5 |
| EXHAUSTIVENESS_LICENSE | 3 |
| REPARAMETERIZATION_BARRIERS | 2 |
| THE_SUBSTRATE | 1 |

**All 40 SIDE-* kernels are present locally and both critical ones have `.lake` built**, so the
re-grade is executable rather than blocked.

---

## §2 — CONSTELLATION MODE: CLEAN ON TWELVE OF TWELVE

Run across all twelve papers. **Eleven return `0 actionable, 0 provenance, 0 external, 0
historical`.** The keystone returns **3 actionable, 16 external, 4 historical**.

**The three actionable flags are a TOOL-SCOPE ARTIFACT, not a corpus defect, and I checked before
saying so.** Constellation resolves a backticked `FILE.md` against the corpus root it is given;
relay reports live in a **different repository**. All five sampled targets — `w-control-audit`,
`the-sixth-point-completion`, `e25-derive-the-constant`, `w-shape-200`, `e16-hankel-bridge` —
**exist in `D:\relay\reports\`.** Sixteen sibling references were correctly classed EXTERNAL; three
leaked into ACTIONABLE.

> **CONSTELLATION VERDICT: zero real cross-reference defects across the twelve. The instrument
> needs a relay-root argument; that is a work-order on rowgen, not a finding against a paper.**

---

## §3 — THE DIFF COULD NOT HONESTLY BE RUN YET, AND THAT IS THE SITTING'S FIRST REAL FINDING

`tools/rowgen/terminals.json` **configures NINE terminals. The twelve papers cite NINETY-NINE.**

**Coverage: 9%.** And rowgen's own README states the limit plainly — *"The missing-terminal check
covers terminals in the config; to audit **every** terminal a table cites, feed the full cited set
as the config."*

**Its kernel pin is `0bc21c0` = v1.3. The live kernel is `0e5233f` = v1.5 — the config is two
versions stale.**

> **Running `diff` against that config and reporting the result would have audited 9% of the rows
> at a two-version-stale pin and returned a near-clean sheet. That is precisely the manufactured
> confidence this re-grade exists to prevent, and it is the shape the salt-check was instituted to
> catch. The diff is deferred to sitting 2, behind a config that covers what the papers actually
> cite.**

**An expanded config is written: `tools/rowgen/terminals_full.json` — 90 terminals across 14
kernels at current pins**, up from 9 across 2.

**Twelve names are AMBIGUOUS — the same declaration exists in more than one kernel** (`SIDE-kernel`
vs `SIDE-silence-principle` for the five silence terminals; `SIDE-kernel` vs `SIDE-grh-transfer` for
the six `techne_kernel_voice*` terminals; `SIDE-effects` vs `SIDE-kernel` for `SIDE_exclusion`).
**Each must be disambiguated from the row's own repo column, not guessed.** The config records the
ambiguity rather than silently picking one.

---

## §4 — A DEFECT IN MY OWN METHOD, CORRECTED BEFORE IT REACHED A VERDICT

My first resolution pass reported **12 of 99 terminals unresolved**, including three
`SIDEDerivative.*` cited by SIMPLICITY_OF_RIEMANN_ZEROS, and a scan for the namespace across all 40
kernels returned **zero hits**. On that evidence the rows looked like citations to a kernel that
does not exist.

**They are not. My resolver walked checked-out working trees at HEAD; the rows cite a PIN ON
ANOTHER BRANCH** — `SIDE-kernel` branch `derivative-engine` = `27a3ae7`, and the rows say so on
their face: *"held, not deposited."* The branch exists, the commit exists,
`Kernel/DerivativeEngine.lean` exists at it, and all three theorems are there with **0 `sorry`, 0
`native_decide`**.

**The lesson, in the form that generalises: a resolver that reads working trees cannot audit a
corpus that cites pins. Resolution must be `git show <pin>:<file>`, not `os.walk`.** Every
"unresolved" count in this sitting is therefore a **lower bound on resolution**, not evidence of a
missing terminal.

---

## §5 — STATEMENT-READ: THE THREE HARDEST ROWS, ALL CONFIRMED

I read the three that looked worst — the ones whose statements are about a bare complex number
while their row descriptions speak of ξ, transversality and simplicity. **That gap is the salt-check
shape, so they were read first.**

```lean
theorem onLine_doubleZero_iff_imDeriv_zero {z : ℂ} (hRe : z.re = 0) : z = 0 ↔ z.im = 0
theorem no_onLine_double_iff_transversal   {z : ℂ} (hRe : z.re = 0) : z ≠ 0 ↔ z.im ≠ 0
theorem exactly_c1_derives : (List.filter … [c1,…,c7]).length = 1 := by decide
```

**Read literally, the middle two are trivialities about ℂ.** The question is whether the paper
claims more than that — and it does not, because **the kernel's own docstrings declare the
abstraction before the paper ever cites it**:

> *"**Abstract over ℂ, consuming `z.re = 0`; the concrete hypothesis is `spectral_cannon` (@ pin,
> cited).**"*
> *"Uniform transversality … **is** the simplicity conjecture: the derivative h2, **carried openly
> as INTERFACES, not proved here**."*

And the paper's rows match: *"consumes the perpendicular crossing (Re ξ′=0); concrete hypothesis is
`spectral_cannon` @ `691295b`, cross-referenced not re-proven"* and *"**INTERFACES** — the
derivative h2 = the simplicity conjecture, carried openly (named premise, never encoded)."*
`exactly_c1_derives` is graded *"the honest count, **not** an exclusion verdict"* — and the grade
map it counts over independently records C₃ as **NOT-COMPILED** and C₂/C₄–C₇ as **INTERFACES**.

| row | grade | verdict |
|:--|:--|:--|
| `exactly_c1_derives` | DERIVES (count only) | **CONFIRMED** |
| `onLine_doubleZero_iff_imDeriv_zero` | DERIVES (consumes a cited hypothesis) | **CONFIRMED** |
| `no_onLine_double_iff_transversal` | **INTERFACES** | **CONFIRMED** |

**These three are a model of the standard, not a casualty of it: the abstraction is declared at the
kernel, repeated at the paper, and the premise is named rather than encoded.**

**ONE THING NOT CONFIRMED, and it is flagged rather than passed:** the rows give
`{propext, Classical.choice, Quot.sound}` for two theorems whose proofs are two constructive lines
(`Complex.ext`, `not_congr`). **That profile looks over-declared.** Over-declaring axioms is the
safe direction and no claim rests on it, but *"expected to be harmless"* is the reasoning this gate
exists to refuse. **Verifying it needs `#print axioms` at `27a3ae7`, which needs a build at that
branch — queued for sitting 2, not asserted here.**

---

## §6 — WHERE SITTING 1 LEAVES IT

**Done:** scope fixed at 99 terminals across 12 papers · constellation clean on all twelve ·
coverage gap found and the premature diff refused · full config written (90 terminals, 14 kernels)
· resolver defect found and corrected · three rows statement-read and CONFIRMED.

**Sitting 2:** disambiguate the twelve multi-kernel names from their row's repo column · run
`generate` at pins (`git show`-sourced fields need no build; `#check`/`#print axioms` need one) ·
run `diff` against the full config · begin the per-row statement-read at PATHS (31 rows) and
SURROUND (29), which together are 60% of the corpus's rows.

**Not done and not pretended:** **96 of 99 rows are unread at the current standard.** The three
read are the three that looked worst, which is the right order and is not the same as a sample.

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `77a86d4` (unchanged this sitting — no paper edited) |
| relay | → this report's commit |
| SIDE-kernel `5e668b4` (main) · `27a3ae7` (branch `derivative-engine`, read-only) | |
| lv `2f71068` · **rail `de621b1` / `2147a03`** | unmoved |

**Pass 2 stays closed. Nothing deposits.**
