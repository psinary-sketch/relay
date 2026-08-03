# The shadow row joins · E-7b face 4 (three coordinates) · genus-9 face 3 (the mechanism extraction) · I-5 gains the criticality criterion — 2026-08-03

The ferry's ruling + two moves + one watch. Pins at open: PLACE-papers = `877bafb`; relay =
`46eb2a8`; lv `14720d9`, kernel `44895f9` — unmoved; rail at the post-rename baseline.
Nothing deposits.

## Registered expectations (VERBATIM from the ferry, recorded BEFORE work)

**Move 2 (E-7b face 4):** *"the Hamiltonian coordinate DERIVES as a third statement-level
alphabet; the measurement equivalence stays OPEN as the one normal-form cell; full collapse
files first-class with maximal caution."*

**Move 3 (genus-9 face 3):** *"the distinguishing datum is NAMEABLE at this genus (the
stratum is small enough); deliverable = the candidate mechanism at grade or the named
obstruction sharpened; either files to the self-similarity note and E-7b's dictionary."*

## MOVE 1 — THE RULING EXECUTED: THE SHADOW ROW JOINS

(Filings executed first, before the moves — the details in the "MOVE 1 EXECUTED" block
below, placed with the closing for the ledger cross-references.)

## MOVE 2 — E-7b FACE 4: THE THREE-COORDINATE INTERTWINER

**The three coordinatizations beside the one form (the Weil pairing, face 3's parent):**
prime-Gram (BN/Vasyunin entries) · zero-Hankel (the moment forms, s_{i+j+1}) ·
canonical-Hamiltonian (H(t) ⪰ 0, E-18's carrier candidate).

**The cells, statement level:**

| cell | content | grade |
|:--|:--|:--|
| prime ↔ zero | the explicit formula (face 3) | THEOREM-AT-CITE |
| zero ↔ Hamiltonian | Krein–de Branges inverse spectral theory: a spectral measure ↔ a canonical system | THEOREM-AT-CITE |
| prime ↔ Hamiltonian | the composition of the two | DERIVED |

**Registered clause 1 CONFIRMED: the Hamiltonian coordinate DERIVES as a third
statement-level alphabet** — and the derivation is sharper than expected, because the zero
side hands it a free gift: **the zero-moment measure ν = Σ β_j δ_{β_j} has BOUNDED support
(β_j ≤ β₁), so its moment problem is DETERMINATE unconditionally** — no Carleman condition
needed (the E-15 dictionary's caveat discharges itself at this coordinate). Classical
Stieltjes theory then converts the Hankel data to Jacobi/three-term-recurrence parameters
(exact formulas: ratios of consecutive Hankel minors), and Krein's string correspondence
converts those to A canonical Hamiltonian. **So at MEASUREMENT level, two of the three
coordinates are already equivalent at cite-grade:** zero-Hankel ↔ (the Krein string of ν) —
minors ↔ Jacobi parameters ↔ string data, unconditional.

**The cells, measurement level:**

| cell | content | grade |
|:--|:--|:--|
| zero-Hankel ↔ Krein-string Hamiltonian | minors → Jacobi parameters → string (Stieltjes; Krein); determinacy FREE (bounded support) | DERIVED-AT-CITE |
| the Krein string of ν ≟ ξ's dB-Hamiltonian | whether the moment-built canonical system IS E-18's carrier candidate (the dB/Lagarias system for ξ) | **OPEN — the found identification cell (this face's discovery)** |
| prime-Gram ↔ zero-Hankel (determinant sequences) | face 3's cell, unchanged | **OPEN — the one normal-form cell (as registered)** |
| prime-Gram ↔ Hamiltonian | reduces to the row above | OPEN (by reduction) |

**VERDICT: the registration CONFIRMED in both clauses — and the face SHARPENS the map:** the
three alphabets all exist at statement level; at measurement level the open territory
COLLAPSES TO ONE NORMAL-FORM CELL (prime-Gram ↔ Jacobi parameters — the prime-side
determinant sequence has no exhibited translation into recurrence data), plus one found
identification question (is the moment-string ξ's own dB-Hamiltonian?). No full collapse; no
first-class claim. **E-7b's dictionary after four faces:** one Weil form · three alphabets ·
two measurement-equivalent coordinates (zero, flow) with determinacy free · one normal-form
cell open (prime) · one identification open (string ≟ dB). The question is now exactly two
cells wide.

## MOVE 3 — GENUS-9 FACE 3: THE MECHANISM EXTRACTION

**Instrument** (`tools/e3/mechanism.py`, exact throughout): the pencil's zeta coefficients
are AFFINE in c (the defining system's matrix is c-independent — only the enumerator side
moves), so H(u)'s coefficients are quadratic in the defect ε = c + 42 = A₄, and every Hankel
minor is an exact rational function of ε: D_k(ε) = Ñ_k(ε)·L(ε)^{a_k−k²}·ε^{m_k},
reconstructed by exact interpolation from 46 rational samples and verified on all of them
(the interpolants reproduce every flip measured in the earlier sittings).

**THE EXTRACTED STRUCTURE — the registered datum LANDS, NAMEABLE:**

1. **The top coefficient collapses as the defect squared, exactly:**
   L(ε) = lead(H) = ε²/112911876. The genus drop at the stratum is this double zero, made
   algebraic.
2. **The reduced flip polynomials are LOW degree:** floor k=2: Ñ quadratic; reality k=3: Ñ
   cubic; floor k=3: quartic; reality k=4: quintic — the entire signature structure of the
   genus-9 interior is governed by explicit low-degree algebraic curves in the defect.
   The floor-k=2 law in full: Ñ(ε) = −1/938961 − (124889/9977399586)·ε
   + (9337595/2304779304366)·ε², negative exactly on ε ∈ (−0.083, 3.172) — every earlier
   measured flip and ordering entry is reproduced by these polynomials' sign tables.
3. **The constant terms are extremal-certificate data with a negative sign:** Ñ_{k=2}(0) =
   −1/938961 = −lead(H_Golay) exactly (the k=3 constants likewise negative). To leading
   order in the defect, positivity is attacked by the NEGATIVE of the extremal certificate's
   own leading datum; at ε = 0 the attack is cancelled by the L-collapse (the ε² powers) —
   **the extremal certificate is the residue of the pencil's certificate at the defect's
   double zero.**
4. **The burial law (the control, n=32 — genus 13):** the same-layer minor k=2 never flips
   across the whole pencil; the defect's signature entry point recedes to k=3 (negative at
   δ=1, positive at δ ≥ 3). **Higher genus buries the defect's signature one minor deeper**
   — the toy-side echo of the ζ-meter's depth-burial of the Lehmer shadow: in both worlds,
   proximity to the wall hides from shallow sections of the pair-form.

**VERDICT: the registration CONFIRMED — the distinguishing datum is NAMEABLE at this genus,
and it is the defect itself, entering the certificate at two exact places:** multiplicatively
as the collapsing top coefficient (ε², the genus drop) and additively through low-degree
reduced polynomials whose ε⁰ terms are negated extremal-certificate data. **Candidate
mechanism, at instance grade (n = 24, genus 9):** stratum positivity survives as the ε → 0
residue — the defect's negative leading contribution is exactly extinguished by the degree
collapse, and off the stratum it is not. What is NOT yet proved: that this residue structure
is the general-n mechanism (the burial law says its ENTRY POINT moves with genus; the shape's
persistence is the open general claim). **Files to the self-similarity note** (the pair-form's
sections are algebraic in the wall-distance parameter; the wall is the parameter's double
zero) **and to E-7b's dictionary** (the defect as the local coordinate; minors as sections —
the same grammar as the pencils at ζ).

## MOVE 4 — I-5 GAINS THE CRITICALITY CRITERION

Executed: `phase1.5/method/INSTRUMENTS.md` I-5 gains the criticality criterion (one line,
dated, author-ruled): watch entries additionally screen for universality-class / zero-margin
results touching arithmetic spectra; quarterly cadence unchanged.

## MOVE 1 EXECUTED (the ruling's filings)

FINDINGS **F.2026-08-03** landed (the sixth world joins as the SHADOW ROW — distinct
row-kind; the epistemic completion: five proved suppliers + one observed silhouette; the
belief-sentence: the field's confidence = observation of Q's statistical shadow, never of a
proof; two-darknesses binding). SPIRAL translation row landed (JOINED as SHADOW ROW,
author-ruled 2026-08-03). Keystone takes the row at its next natural touch with the riding
annotations (now four + this row).

## CLOSING — pins, slate, board

**The slate re-printed:** E-3 — **genus-9 face 3 RUN: the mechanism candidate extracted at
instance grade (the defect-residue structure; the burial law)**; the general-n persistence =
the remaining open claim (research-reach, priced on call) · E-7b — **face 4 RUN: the
question is now exactly two cells wide** (prime-Gram ↔ Jacobi normal form; the Krein string
of ν ≟ ξ's dB-Hamiltonian); determinacy free at the zero coordinate · E-1 (v2 + sharpened dB
row) · E-2 · E-4 · E-5 · E-11 · E-12 · E-16 (Polymath15-rigorous rung; the d(t) exponent) ·
LY-REP-A · Face-E Tier 2 · the ξ-sweep · the consolidation ruling (author's, open).

**The board restated, the two verdicts at its head:** THE MECHANISM HAS A NAME AT GENUS 9 —
the extremality defect enters the certificate as an exact double zero of the top coefficient
plus negated-extremal-data corrections; the stratum's positivity is the residue at that
double zero; higher genus buries the entry point deeper (the burial law — the toy's echo of
the Lehmer shadow). THE INTERTWINER IS TWO CELLS WIDE — three alphabets at statement level,
zero↔flow measurement-equivalent with determinacy free, prime-side normal form and the
string≟dB identification the two open cells. The shadow row is in the ledgers; the keystone
carries six worlds at its next touch.

| repo | pin |
|:--|:--|
| PLACE-papers | `877bafb` at open → this sitting's commit (FINDINGS + SPIRAL + I-5 + OPEN_TRAILS) |
| SIDE-lv-conservation | main = `14720d9` — unmoved |
| SIDE-kernel | `44895f9`; v1.7 — unmoved |
| relay | this report's commit; instrument `tools/e3/mechanism.py` |
| rail | untouched — at the post-rename baseline |

Keystone untouched (the next natural touch now carries: the shadow row · the four riding
annotations · the mechanism/residue note). Mirror rebuilt at the papers pin on commit.
Nothing deposits.
