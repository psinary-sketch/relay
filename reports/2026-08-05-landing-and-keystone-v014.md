# The lv working tree lands · the keystone touch taken (v0.14) — 2026-08-05

Author-called. Pins at open: PLACE-papers `3d794fd`; relay `898bdaa`; lv main `14720d9`;
kernel `44895f9`. Rail at the post-rename baseline. Nothing deposits.

---

## §1 — THE LANDING, VERIFIED RATHER THAN ASSUMED

**lv main moves for the first time since the ratified pass: `14720d9` → `2f71068`.**

Eight modules: `FieldLayer`, `LeadLaw`, `SaltCheck_LeadLaw`, `TwoSidesIdentity`, `Genus5`,
`Genus5Confinement`, and the two axiom-check drivers. `.lp.log` (a lake build log) added to
`.gitignore` rather than committed.

**The verification the ferry required, executed in that order:**

1. **The build artifacts were DELETED.** Every `.olean`, `.ilean`, `.trace` and hash for the eight
   modules was removed before rebuilding, so the post-landing build is a genuine recompilation of
   the landed source and not a cache read. (Mathlib stayed cached; only our modules recompiled.)
2. **The library rebuilt green** — 8273 jobs, `Build completed successfully`, with no
   `declaration uses 'sorry'` warning anywhere.
3. **All 27 terminal profiles RE-PRINTED at the landed pin**, from the committed state with a
   clean working tree — not carried forward from the working-tree reading.
4. **Compared.** **Every profile is byte-identical to the working-tree reading. No halt
   condition fired.**
5. **Pushed, and local = remote verified by full hash** — `2f71068ac356a15a3f43fea073aa8fe4ae4fbf23`
   on both sides.

**The landed profiles, in full.**

| module | terminals | profile |
|:--|:--|:--|
| `FieldLayer` | `top_coeff_of_expansion`, `norml_top` | the standard three |
| `LeadLaw` | `v_monic`, `v_natDegree`, `leadingCoeff_hOf`, `ptTop_eq_p_zero`, `lead_law_of_top_coeff`, `lead_law` | the standard three |
| `LeadLaw` | `norml_top_eq_ptTop` | `[propext, Quot.sound]` |
| `SaltCheck_LeadLaw` | `expansion_exists_of_palindromic`, `hg_is_load_bearing` | the standard three |
| `Genus5` | `genus_mod_four`, `genus_one_forces`, `genus_five_forces`, `classification` | `[propext, Quot.sound]` |
| `Genus5Confinement` | `e8_confined`, `quad_confined`, `w16_confined`, `golay_five_roots_in_interval`, `golay_confined` | the standard three |
| `TwoSides` | `heine_one`, `heine_two`, `heine_three`, `ladder_three`, `two_sides_balance`, `heine_three_degenerate`, `vandermonde_square_is_load_bearing` | the standard three |

---

## §2 — THE THREE ROWS, REPINNED TO THE LANDED LINE

All three now carry `SIDE-lv-conservation main = 2f71068` and print their shortfall in the Status
cell. The Correspondence preamble records that these three were re-printed **at the landed pin,
after the landing, not carried from the working tree** — the provenance of the numbers is part of
the numbers.

| row | premises | shortfall |
|:--|:--|:--|
| the lead law | **one** (Duursma's FE) | **one clause** |
| the genus ≤ 5 theorem, both units jointly | three (Mallows–Sloane · Gleason uniqueness · the certificate construction) | **two clauses** |
| the two-sides identity instance | one at cite (the Jacobi link) + declared instance scope | **three clauses** |

**D-2c's row states its finding on its face**, in the row itself rather than in a report a reader
might not reach:

> **the compiled ladder is closed by `field_simp` alone — it restates the Hankel-ratio definition
> and does NOT supply a second route, so this terminal certifies the SPECTRAL side only and the
> two-route claim is not certified by it.** The machine-exactness figures in §3 stand as computed
> and doubly-sourced in the relay record, which is a different warrant from this row.

**The genus row replaced its predecessor rather than joining beside it.** That row previously read
`(none — computational record + classification)`; it now names a kernel, and the computational
record (Sturm over ℚ, the ℚ(√2) cross-check, the instrument) stands beside the terminal instead of
in place of one.

---

## §3 — KEYSTONE v0.14: ONE PASS, FOUR CARGOES

**(1) D-2a's paper-sentence correction.** §3 read *"since the proof uses self-duality alone"*; it
now reads *"since the proof uses only **the functional equation that self-duality supplies, given
Duursma's construction of the zeta polynomial**"*. One clause, and it closes exactly the clause
the shortfall measured.

**(2) The identity sentence qualified.** §3's two-sides verdict keeps its machine-exactness
figures and gains the warrant distinction: the exactness *stands as computed and doubly-sourced in
the relay record*, and then, stated separately, **what the kernel certifies** — the spectral side
at K = 3 in six free variables, with the coefficient side explicitly not certified as a second
route. The measurement and the terminal are two different warrants for two different claims, and
the paper now says which is which.

**(3) The PROVENANCE block (voice move 1).** Placed after §3, before *"Read together, the halves
interlock"*. It holds, verbatim in the words they were withdrawn in: the sum-rule withdrawal
passage, the two-sides share withdrawal passage, and the c-sequence VOID notice — plus the
control-matching law's one-line cause. The body now states only the corrected figures — Z₉ =
0.0507, Q₉ = 0.0951, the 92% share, the VOID mark — each with a `(provenance)` pointer.
**Nothing deleted; the same sentences moved.**

**(4) The undecided pair moved to the Forward (voice move 2).** The shape discriminant's anchors
table and ζ's measured value stay in §3, where measurements belong. The *reading* — "the GUE
anchor is derived from pair correlation, so proximity is consistency and never evidence; the
channel falsifies and cannot confirm" against "this is where ζ sits among the three pictures" —
moves to the Forward's open items as the undecided pair it is, with **what would decide it**
stated: an independent placement-sensitive statistic, which the arc has now shown the density
register cannot supply. §3 keeps a one-line pointer.

**Version bumped once, to v0.14. No figure changed anywhere in the version.** The voice rule and
the free-writing law both observed: the body states the case, corrections live in PROVENANCE and
the version history, the undecided pair lives in the Forward, and kernel citations live in
Correspondence.

**Verified by exact-string probe** against the document after editing: nine present-checks, plus a
position check confirming the interpretive pair now occurs exactly once and sits **after** the
Forward's open-items marker rather than in §3.

---

## §4 — THE COMPILED SALT-CHECK, FILED AS THE STANDING FORM

Until this pass the salt-check was prose: the executor read the statement back, asked whether the
hypotheses could be met and whether each did work, and wrote the answer into a report. D-2a's
upgrade did it in the kernel instead.

- **`expansion_exists_of_palindromic`** — non-vacuity, and generically: at genus 1 **every**
  palindromic normalized sequence admits an expansion, and palindromy is what the functional
  equation supplies, so the witnesses are of the shape the theorem's own hypotheses produce.
- **`hg_is_load_bearing`** — **the OVER-HYPOTHESIZED test's compiled counterpart.** That grade,
  minted the same day, says a statement carrying an unused hypothesis understates its proof, and
  its test is *delete the hypothesis and recompile*. Here the test is carried out in advance and
  **left in the repository as a theorem** rather than performed once and reported.

**Why the compiled form is better, stated once.** A prose salt-check is re-performed by every
reader who doubts it and is lost when the report scrolls past. A compiled one is checked by the
build on every future pass, travels with the module, and fails loudly if a later edit makes the
premise vacuous or the hypothesis idle.

**The standing instruction: where a terminal's premises can be exhibited, exhibit them — a
salt-check that can compile should compile.** Where they cannot (a cited datum, a declared
instance scope), the prose form stands and the reason it could not compile is stated.

---

## PINS

| repo | pin |
|:--|:--|
| PLACE-papers | `3d794fd` → this pass's commit (keystone v0.14) |
| relay | `898bdaa` → this report's commit |
| **SIDE-lv-conservation** | **main = `2f71068`** — landed this pass; local = remote verified by hash; 27 profiles re-printed at the pin |
| SIDE-kernel | `44895f9` — unmoved; the generalization work-order **stays open at the author's call** (docstring recommended) |
| rail | `de621b1` / `2147a03` — at the post-rename baseline |

W-LI face 2 still queued. Consolidation DEFERRED. Nothing deposits.
