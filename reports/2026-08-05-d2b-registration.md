# D-2b — REGISTRATION, THE HALT-AND-FILE, AND THE CORRECTED ROUTE — 2026-08-05

Pins at open: PLACE-papers = `7c5d613`; lv main = `14720d9` (LeadLaw on an unlanded working
tree; its olean still building for the axiom profile); kernel `44895f9` — unmoved. Nothing
deposits.

## §1 — HALT-AND-FILE: THE SCOPED ROUTE FAILED ON INSPECTION

Last pass's scoping recommended, for the confinement certificates, "exact rational
root-location by case analysis on explicit factorizations… for the three explicit low-degree
objects." **Checked before building, and for one of the three objects it is wrong.** The
Golay's certificate, cleared to integer form, is

  H_Golay(u) ∝ 676u⁵ − 5408u⁴ + 13832u³ − 12532u² + 3481u − 162,

and the rational-root test over all divisor pairs of (162, 676) returns **NONE**: the
polynomial has no rational roots, hence no factorization into rational linear factors, and
"case analysis on explicit factorizations" cannot reach it. **Filed as a halt: the route was
mine, proposed from the objects' degree without inspecting their factorizations, and it is
withdrawn for that object.**

## §2 — THE CORRECTED ROUTE, VERIFIED BEFORE REGISTRATION

The three objects need three different arguments, and each is exact and rational:

- **e₈** — H(u) = (u − 2)/25: one linear factor, root u = 2 ∈ [0,4]. Trivial.
- **W₈²** — H(u) = (u − 2)(u² − 4u + 1)²/4225: an **explicit rational factorization** (the
  scoped route, valid here). Roots 2 and 2 ± √3, with 0 ≤ 2 − √3 and 2 + √3 ≤ 4 reducing to
  √3 ≤ 2, i.e. 3 ≤ 4. Decidable.
- **Golay** — no rational roots, so: **the IVT sign-alternation route.** Evaluate H at six
  explicit rationals and exhibit five sign changes; the intermediate value theorem then gives
  five distinct roots inside the interval, and degree five gives at most five, so *all* roots
  lie there. **Verified in exact arithmetic before registering:**

| u | H(u) (exact) | sign |
|:--|:--|:--|
| 0 | −162 | − |
| 1/10 | 1851949/25000 | + |
| 1/2 | −1139/8 | − |
| 3/2 | 10407/8 | + |
| 3 | −2823 | − |
| 4 | 6274 | + |

Five alternations on 0 < 1/10 < 1/2 < 3/2 < 3 < 4, all values small integers or small
fractions. (Numerically the roots are 0.0578, 0.3823, 1.0609, 2.6648, 3.8342 — consistent,
and used only as a check on the bracketing, not as evidence.) **Sturm is not needed and is
not built: Sturm is an instrument for repeated use on unknown polynomials; three known
polynomials warrant a proof, not an instrument.**

## §3 — THE REGISTERED STATEMENT (VERBATIM, before compiling)

**What D-2b's statement WILL say.** Under the stipulated data below, the Type II self-dual
weight enumerators of genus ≤ 5 are exactly three — e₈, W₈², and the Golay enumerator — and
for each of the three, the certificate H(u) has all of its roots in the interval [0,4],
which is the confinement condition (Duursma-RH at that genus, transported through the
Galois-locked certificate).

**What it will NOT say:** nothing of ζ, of RH, or of `h2`; no claim that Duursma-RH holds at
any genus beyond 5; no claim that the certificate construction is derived here; and no claim
that the classification's inputs are proved rather than cited.

**Stipulated data, named in advance (the row will print them):** (1) **Mallows–Sloane**, the
bound d ≤ 4⌊n/24⌋ + 4 for Type II codes — a cited theorem, per the DH precedent; (2)
**Gleason uniqueness** at each admissible (n, d), i.e. that the invariant space is spanned as
claimed and the stated enumerator is its unique member with the required vanishing — cited;
(3) **the certificate construction** (that H(u) is the Galois-locked object attached to the
enumerator) — the same stipulation D-2a carries.

**Derived in-kernel:** the genus arithmetic (genus ≡ 1 mod 4 for Type II, so genera 2, 3, 4
are empty); the Mallows–Sloane forcing (that g = 1 admits only m = 1 and g = 5 only m = 2, 3);
and the three confinement certificates by the exact routes of §2.

**Salt-check to run before it counts as DERIVED,** and the halt rule: any unregistered
stipulation surfacing during the build halts and files, as D-2a's did.

## §4 — THE FREE-LAYER FILING (Tier N, cross-linked)

**The formalization inverts the mathematical cost.** In the mathematics, the FREE layer is
cheap — the functional equation is symmetry's gift, given without effort to every member of
the class, failing ones included — and the DECIDING layer is where the work lives, since it
separates the extremal stratum from the interior. **In the formalization the order reverses.**
Certifying the free layer means certifying its whole construction: weight enumerators,
MacWilliams duality, the zeta polynomial's existence and its functional equation — a
programme. Certifying the deciding layer means evaluating explicit rational polynomials at
explicit rational points — an afternoon. **What is free to the mathematician is expensive to
the kernel, and what decides is cheap to check.**

**The corollary, stated as kernel-leg policy:** *certify deciding layers; stipulate free
layers at cite, deliberately.* This is the Davenport–Heilbronn precedent with a structural
reason attached rather than a convenience — the DH datum was stipulated because re-proving it
was disproportionate, and this filing says why that disproportion is systematic: free layers
carry constructions, deciding layers carry arithmetic.

**Cross-links:** the five-world anatomy where the same split recurs (the functional equation
free in the code world · self-adjointness free in the graph world · the square free in the
certificate — each a symmetry's gift, each with the deciding layer elsewhere); the era's
supplier rows; and the recursion note, which found the split *inside* the certificate.

## §5 — THE STATEMENT-VERSUS-CLAIM SHORTFALL AS A MEASURED COLUMN

The Correspondence gains a column, and the register becomes a quantity rather than an
impression a reader forms:

| terminal | shortfall | the two sentences |
|:--|:--|:--|
| D-2a (the lead law) | **one clause** | paper: "since the proof uses **self-duality alone**"; statement: "from the functional equation self-duality supplies, **given Duursma's construction**" |
| D-2b (genus ≤ 5) | *to be measured at its salt-check* | — |
| D-2c (the identity instance) | *to be measured at its salt-check* | — |

Each D-2 row records its shortfall width in clauses, with the exact pair of sentences quoted,
so a reviewer reads the distance rather than estimating it.

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `7c5d613` → this pass's commit |
| SIDE-lv-conservation | main = `14720d9` — unmoved |
| SIDE-kernel | `44895f9`; v1.7 — unmoved |
| relay | this report's commit |
| rail | `de621b1` / `2147a03` — at the post-rename baseline |

W-LI face 2 stays queued behind the kernel leg. Keystone cargo queued, not landed.
Consolidation DEFERRED. Nothing deposits.
