# PASS 2, SITTING 2 — THE TWO-CLAUSE ADJUDICATION · THE COMMON-SOURCE TEST · THE KEYHOLE — 2026-08-09

**Every passage below quoted from source this sitting.** Rail `de621b1` / `2147a03` **unmoved**.
**Nothing deposits.**

---

## §1 — THE TWO-CLAUSE QUESTION: **TWO CLAUSES, ONE PER STRATEGY — AND THE CORPUS SAYS SO**

**VERDICT: TWO CLAUSES. NOT a register correction. NOT a redundancy. "One open premise" STANDS, and
stands correctly, because every site that says it is scoped to a single proof strategy.**

**The deciding passage, quoted verbatim (Ch. 22.7 / Part IV framing):**

> *"The strategy carries its own premise: the conditional (simplicity → RH) is proved, while its
> antecedent — the simplicity of the zeros — is the geometric clause, carried openly (§24.4).
> **Part III's proof does not consume this clause; the two strategies are independent, and each
> closes to a single open clause of its own.**"*

And again, independently:

> *"Both levels use the same catalogue; **each closes to a single open clause of its own**."*

**The canonical statement of the geometric clause, quoted:**

> *"A zero ρ = ½ + iγ is simple iff ξ'(ρ) ≠ 0; by the perpendicular crossing (Re ξ'(ρ) = 0 on the
> line, compiled) this is Im ξ'(ρ) ≠ 0 — **uniform transversality**. This is the geometric clause:
> the derivative-level counterpart of the arithmetic clause (§27.3), and like it an open premise
> carried openly. Its 𝔽_q anchor is Katz–Sarnak monodromy (generic over a family, not universal);
> **its ℚ-obstruction is the missing family — ξ is a single object, with no ensemble to
> equidistribute**."*

**THE STRUCTURE, therefore:**

| | Part III | Part IV |
|:--|:--|:--|
| method | mechanism enumeration | simplicity reduction |
| its open clause | **arithmetic** (§27.3) — the sign, `λ_Z(n) ≥ −λ_A(n)` | **geometric** (§24.4) — uniform transversality, `Im ξ'(ρ) ≠ 0` |
| ℚ-obstruction | the sign does not follow from Λ(n) ≥ 0 | **the missing family** — no ensemble to equidistribute |
| consumes the other's clause? | **no** | **no** |

> **MY SITTING-1 FLAG IS RESOLVED AS NOT-A-DEFECT, and I state that as plainly as I raised it.** I
> filed the geometric clause as a "candidate redundancy" and implied the corpus might be
> miscounting its own openness. **It is not.** The corpus distinguishes the two clauses explicitly,
> assigns each to its strategy, and says in two places that each strategy closes to one clause of
> its own. **The suspicion was worth raising and is wrong.**

**THE ONE REAL OBSERVATION THAT SURVIVES: the two strategies are independent IN METHOD BUT SHARE
THEIR FOUNDATION.** Quoted: *"The last link uses the exhaustive catalogue from Part III; **the two
strategies share this foundation**"* and *"The independence is **in the method** (simplicity
reduction vs. direct per-class exclusion), **not in the foundational infrastructure**."* **The
corpus already says this too.** So "two independent proofs" is true of method and false of
foundation — **exactly the same shape as the five-voice finding, and already disclosed at source.**

---

## §2 — THE COMMON-SOURCE TEST: **N = 2, NOT 3**

Sitting 1 recorded, at provisional grade, that three legs converge on *"the missing ingredient is
multiplicative and the current tools cannot see it."* **Tested at cite, the bases are not
disjoint.**

| leg | evidence base at cite | uses Davenport–Heilbronn? |
|:--|:--|:--|
| **Face E** — *any derivation of the positivity must use the Euler product essentially* | two-witness / Baker–Gill–Solovay relativization **plus** the D–H witness: *"ξ ~_D Z (shared structure) yet definiteness differs (**Z has off-line zeros: Davenport–Heilbronn**)"* | **YES — load-bearing** |
| **The Epstein witness / family probe** | **IS** the D–H fact, plus the corpus's own 2-D census locating ρ ≈ 0.9533+16.290i and ρ ≈ 0.798+29.5518i | **YES — it is the witness** |
| **The codimension diagnosis** | Codimension Dichotomy (`TRIVIUM_IDENTITY_SUBSPACE` Prop 8.16) · von Neumann–Wigner (`SIDE_EXCLUSION` L262, `CONSTANCE` Thm 2) · standard transversality | **NO** |

> **VERDICT: TWO independent evidence bases, not three.** Legs 1 and 2 are **one base** — Face E's
> barrier is *powered by* the Epstein witness; without D–H the relativization has no second witness
> and the barrier is vacuous, **as the Face-E ruling itself states**: *"if it were D-accessible the
> witnesses would be distinguishable and the barrier vacuous."*
>
> **Leg 3 is genuinely independent** — a statement about instrument type versus target codimension,
> resting on transversality theory and eigenvalue-collision genericity, with no arithmetic witness
> in it at all.

**SO THE HONEST NARRATIVE IS: one arithmetic witness (D–H), read twice — once as a fact and once as
a barrier — and one geometric diagnosis, independent of it. "Three independent confirmations" does
not survive; "two bases agreeing" does.** And the agreement is still notable, because the two bases
are of different kinds (arithmetic counterexample vs. geometric type-mismatch).

---

## §3 — THE KEYHOLE (Tier N; a SCREEN, not a route)

**Four NECESSARY conditions on any closing route, each with its certificate. Explicitly
necessary-not-sufficient; explicitly not a claim that such a route exists.**

| # | condition | certificate |
|--:|:--|:--|
| **i** | **uses the Euler product essentially** | Face E, honest restricted theorem (author-adopted; definitional form rejected as ENCODES) |
| **ii** | **is a sign-type / codim-1 instrument** | the codimension diagnosis — a codim-≥2 instrument faces a codim-1 wall; *"a type mismatch, not a strength shortfall"* |
| **iii** | **separates ζ from the Epstein family at the multiplicative place** | the D–H witness + the discreteness results — full specification without the Euler product yields off-line zeros |
| **iv** | **supplies at the multiplicative place what the archimedean channel supplies unconditionally at its own** | the two-channel Li structure: λ_A known unconditionally (Voros 2006); λ_Z is the open side |

**A FIFTH CONDITION, and it sharpens the keyhole more than the other four — added from
`F.2026-07-25`, read at content this sitting:**

> ***"POSITIVITY IS FREE"*** — compiled on the wrong spectrum (`positivity_free_obstruction_is_zeroRealization`)
> and proved to the Voros threshold `N₀(T)` on the right one. **The Conservation seal is orthogonal
> (s-dark). The irreducible obstruction is a ZERO-REALIZING OPERATOR** whose Weil pairing extends
> the certified inequality past `N₀(T)` — *"Hilbert–Pólya with positivity removed as a
> non-obstruction."*

**And its chiasmus (`F.2026-07-27`): the sign season proved *positivity is free without the zeros*;
the inverse-spectral converse (de Branges) proves *the operator is free given the positivity*.**
**"The space is the wall."**

> **CONSEQUENCE FOR THE SCREEN: the obstruction is neither positivity alone nor the operator alone —
> each is free in the other's absence. It is their JOINT realization.** Any route satisfying (i)–(iv)
> must additionally deliver both together, which is precisely what neither season delivered.
>
> **Disclaimer carried from the source, unchanged: *positivity is not proven on the zeros.***

**Cross-linked to the unbarred-territory map (charter item 3), which remains OWED and is not
drawn here.**

---

## §4 — THE COVERAGE FOLD: PARTIAL, AND SAID SO

**65 graded entries swept. 41 auto-tagged; 24 require a hand read and did not get one this
sitting.**

| tag | n |
|:--|--:|
| OUT-OF-TIER: method/instrument filing | 17 |
| OUT-OF-TIER: Tier-N reading, not promoted | 8 |
| TIER-2: closure / compiled negative | 7 |
| **TIER-3-RELEVANT** | **5** |
| TIER-1: consilience / catalogue row | 2 |
| OUT-OF-TIER: correction of record | 2 |
| **UNCLASSIFIED — needs hand read** | **24** |

**The sweep is a keyword pass, not a fold.** It is reported as such because a tag assigned from a
title is exactly the "span, not read" error the loom already names. **The map does NOT yet become
the census it claimed not to be — 24 entries stand between it and that.**

**One entry the sweep surfaced and the map was missing — now added: `F.2026-07-25`, the sign
frontier**, above. **A second, `F.2026-07-27` (the chiasmus), likewise.** Both are TIER-3-RELEVANT
and neither was in sitting 1's map. **The map is therefore now 19 conclusions, not 17, and the
count will move again when the 24 are read.**

---

## §5 — CROSS-PRODUCTS

**COMPUTED (bounded, doubly-sourced): discreteness × the register table's five bars.** The
discreteness result stalls the Berry–Keating/Connes route because *"the spectrum is continuous, not
the discrete `{γ_n}`"*. The pentagon's **R5** is exactly the spectral register (input certified at
Φ; **output = Hilbert–Pólya, no terminal, disclaimed**). **These are the same wall at two
altitudes:** R5's disclaimed output *is* the zero-realizing operator that `F.2026-07-25` names as
the irreducible obstruction. **R4 (positivity) is NOT closed-by-construction — it is
`partialPositivity_finiteRange`, INTERFACES on three named premises, exact to `N₀(T)`.** So the
interaction is: **R4 gives positivity up to a threshold; R5 would give the operator; the obstruction
is that neither reaches the other.** *Consistent with the chiasmus; no new content, and no progress
on the clause.*

**PRICED, NOT RUN:** burial's γ²/δ × the verification-cost inversion (needs the cost model
re-derived at content — the inversion is Tier-N and its own filing warns of elasticity); the
codimension filter × the completable-paths landscape (needs charter item 3 first); h1-complete ×
Face E's toolkit boundary (needs the manuscript leg, charter item 4).

---

## §6 — STOP-AND-HOLD CHECK

**Nothing in this sitting constitutes progress on the clause.** §3's keyhole is a **screen composed
entirely of previously-filed certificates**; its only new content is the observation that
conditions (i)–(iv) must be met *jointly with* the free-positivity/free-operator chiasmus — which is
**a restatement of two existing findings' relation, not a new mathematical fact.** **No route is
claimed. The disclaimer that positivity is not proven on the zeros is carried unchanged.**

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `483bd33` — **unchanged; no paper edited this sitting** |
| relay | → this report's commit |
| **rail `de621b1` / `2147a03`** | **UNMOVED, both clean** |

**Charter items 3 (unbarred territory) and 4 (manuscript leg) remain owed. Nothing deposits.**
