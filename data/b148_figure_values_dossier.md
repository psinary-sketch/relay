# THE FIGURE VALUES DOSSIER

### Every load-bearing value in the required figure set, verified against its corpus owner at content

**Research seat · 2026-08-24 · relay `reports/2026-08-24-figure-values.md`, registration `b148`.**
### **THIS FILE LIVES IN THE RESEARCH SEAT'S TREE. IT CROSSES TO THE PATENT SEAT THROUGH THE AUTHOR ONLY.**

---

## 0. THE WARNING THAT GOES ON THIS DOSSIER'S FACE

> ### **A WELL-FORMED FIGURE CAN BE FALSE.** *A drawing that is clean, labelled, symmetric and professional is not thereby correct, and a renderer working from a plausible reconstruction will produce exactly that: a confident, wrong figure.*
>
> ### **VALUES TRAVEL ONLY FROM THIS DOSSIER OR FROM THE FILED SPECIFICATION. NEVER FROM THE PACKAGE'S RECONSTRUCTIONS.**
>
> *The reconstructions were not consulted in building this dossier, not cross-checked against, and are* ### **not cited even where they might agree** — *because a reconstruction that agrees with the filing adds nothing the filing did not already give, and citing one launders an unreliable source into a verified row.*

**Ground truth for figure content:** the filed specifications at
`D:\MY-DOwnloads\P_ZONE_PROVISIONAL_FILING.pdf`, `P_FANO_WPT_PROVISIONAL_FILING.pdf`,
`PROV1_FILING.pdf`, read at content this act.

**Rubric:** **CONFIRMED-AT-OWNER** (both quoted) · **DIVERGES** (both quoted, divergence
stated, ### **no resolution attempted — resolution is the author's or counsel's**) ·
**NO-OWNER-FOUND** (the value rests on the filing alone, said plainly).

> ### **NO-OWNER-FOUND IS NOT A FAILURE.** A provisional may properly contain engineering values no research document owns. ***The rows exist to tell a reviewer which values have a second source and which do not.*** That is this dossier's whole function.

### **ON THE FORMAT STANDARD.** The ferry directs that the **TECHNE drawing conventions** be cited as the format standard to inherit. ### **THEY ARE NOT LOCATABLE AT CONTENT** in `PLACE-papers` — searched for drawing/figure convention language across the tree; `internal/TECHNE_ELEMENTS.md` and `internal/TECHNE_INTAKE.md` exist but carry no drawing standard. ***No standard is invented here.*** **If they live in the patent seat's tree, this seat did not locate them and the author should point the renderer at them directly.**

---

## 1. P-ZONE (`P_ZONE_PROVISIONAL_FILING.pdf`) — FIG. 1–7

### 1.1 The two code parameters, which are DIFFERENT OBJECTS

> ### **THIS IS THE HIGHEST-CONSEQUENCE DISTINCTION IN THE ZONE FIGURES AND A RENDERER MUST NOT COLLAPSE IT.**

| Value | Role in the filing | Where | Verdict |
|:--|:--|:--|:--|
| **`[[7,1,3]]`** | the ***underlying physical*** Steane CSS code | FIG. 7 solid curve *"Standard [[7,1,3]] decoder (d = 3)"*; §6 *"The underlying physical code is the Steane [[7,1,3]] CSS code"* | **CONFIRMED-AT-OWNER** — `phase1.5/method/DESIGN_PRINCIPLE_MINIMAL_COMPUTE.md:11`: *"The [[7,1,3]] skeleton — the code itself, forced. n=7 (the formation total), k=1 (2·4−7), d=3"* |
| **`[[7,1,5]]`** | the ***effective*** parameters under the formation-block error model | FIG. 5 *"[[7,1,5]] formation-block code encoder"*; Claim 5; Embodiment 9.1 | **CONFIRMED-AT-OWNER** — `FINDINGS.md:483`: *"d_eff = 5 for the Trivium, via SEC formula d_eff = 2S − 1"* |

**`d_eff = 2S − 1`, at `S = 3` → `d_eff = 5`.** Filing FIG. 1 Box (5): *"Output: Protection Parameters [[n,k,d_eff=2S−1]]"*; §7.4: *"For S = 3, the method tolerates up to 2 corrupted stages, achieving effective distance d_eff = 5."* → **CONFIRMED-AT-OWNER** (`FINDINGS.md:483`; `clusters/CUBIT_TRIVIUM_CLUSTER_SYNTHESIS_2026-05-19.md:112` *"E1. Effective distance d_eff = 5 (vs. naive d = 3)"*).

### 1.2 FIG. 4 — the Knill–Laflamme matrices. ### **READ THIS ROW BEFORE DRAWING FIG. 4.**

**Filing, verbatim:** *"Matrix A is labeled 'Weight-1 Knill-Laflamme matrix **C₁**': a 3×3 grid with diagonal entries 1.000 and **approximately symmetric** off-diagonal entries (0.921, 0.974, 0.941). Matrix B … 'Weight-2 … C₂': a 3×3 grid with rank-deficient structure. Matrix C … 'Weight-3 … C₃': a 1×1 grid with single entry 1."*

**Owner, verbatim** (`phase2/quantum/TRIVIUM_CODE_VERIFICATION.md` §3): *"The K-L matrix for weight-1 stage errors {E_P, E_T, E_O} was computed **at δ = 0.3**"*, giving

```
C = ( 1.000  0.921  0.974
      0.921  1.000  0.941
      0.974  0.941  1.000 )     Eigenvalues: {2.891, 0.086, 0.024}. All positive.
```

**The three entries: CONFIRMED-AT-OWNER.** And three things the filing does not say, which the renderer needs:

1. ### **THE OWNER'S MATRIX IS EXACTLY SYMMETRIC AS WRITTEN.** The filing says *"approximately symmetric"*; the owner writes `C₁₂ = C₂₁ = 0.921`, `C₁₃ = C₃₁ = 0.974`, `C₂₃ = C₃₂ = 0.941`. ### **DRAW IT SYMMETRIC.** *DIVERGES on the descriptor, not on the values — and no resolution is attempted here.*
2. ### **THE ENTRIES ARE CONDITIONED ON `δ = 0.3`, WHICH THE FILING'S FIGURE TEXT DOES NOT CARRY.** *These are not universal constants.* **Annotate the figure with `δ = 0.3` or the numbers are unreproducible from the drawing.**
3. ### **A NAME COLLISION THAT WILL MISLEAD A RENDERER WHO CHECKS THE OWNER.** ***The filing's `C₁` and the owner's `C^{(1)}` are typographically near-identical and are DIFFERENT MATRICES OF DIFFERENT SIZES.*** The owner's `C^{(1)}` (§4.1) is **4×4**, for `{I, E_P, E_T, E_O}`, with entries `1.000 / 0.977 / 0.944 / 0.997 / 0.921 / 0.974 / 0.941` and eigenvalues `{3.877, 0.090, 0.030, 0.003}`. ### **A renderer told "C₁" who searches the owner lands on `C^{(1)}` and draws a 4×4 matrix the figure does not describe.** **FIG. 4 Matrix A is the 3×3 `C`, not `C^{(1)}`.** *Flagged at full prominence per the registration: this is a matrix-entry-class hazard, the first thing a reviewer checks.*

### 1.3 FIG. 2 / FIG. 3 — the Trivium vector, the stages, and an internal cross-check that PASSES

**Filing FIG. 3:** `v = (i√3, i√2, i, 0, 1, √2, √3) ∈ ℂ⁷`, seven rows at indices `n = −3 … +3`; stage brackets `{Row2, Row6} = Stage 1 (Primitive)`, `{Row1, Row5, Row7} = Stage 2 (Transformation)`, `{Row3} = Stage 3 (Output)`, `Row4` marked *"silent interface"*.

**Filing FIG. 2:** Stage 1 qubits `{1,5}` dim 2 · Stage 2 qubits `{0,4,6}` dim 3 · Stage 3 qubit `{2}` dim 1 · *"Index 3, v₃ = 0 (silent interface qubit)"*; interfaces `I₁₂` and `I₂₃` both labelled `κ = 0 (silent)`.

> ### **CROSS-CHECK RUN, AND IT PASSES.** FIG. 3's rows are 1-indexed and FIG. 2's qubits are 0-indexed: Row2→q1, Row6→q5 = Stage 1 `{1,5}` ✓ · Row1→q0, Row5→q4, Row7→q6 = Stage 2 `{0,4,6}` ✓ · Row3→q2 = Stage 3 `{2}` ✓ · Row4→q3 = the silent interface ✓. ### **THE TWO FIGURES ARE MUTUALLY CONSISTENT.** *A renderer may draw them from either and they will agree.*

**Verdict: CONFIRMED-AT-OWNER** — `clusters/CUBIT_TRIVIUM_CLUSTER_SYNTHESIS_2026-05-19.md:130`: *"v = (i√3, i√2, i, 0, 1, √2, √3) ∈ ℂ⁷, with ‖v‖² = 12, **quarter-twist v₍₋ₙ₎ = i·vₙ**, and spec(vv†) = {0⁶…}"*; also `day1/Third_Identity_Element.md:136` and `internal/TECHNE_ELEMENTS.md:98`.

> ### **THE QUARTER-TWIST `v₍₋ₙ₎ = i·vₙ` IS OWNED BUT IS NOT STATED IN FIG. 3'S TEXT.** *If the figure is to show it, it is an addition to the filed description and that is the author's or counsel's call, not the renderer's.*
> **`‖v‖² = 12` is likewise owner-only — NOT in the filing's figure text.**

### 1.4 The formation tuple, and FIG. 1 / 6 / 7

- **Formation `(2, 3, 2, 0)` at `σ = 1/2`, `S = 3` non-empty stages** — filing §5.5/§6 and Embodiment 9.1. **CONFIRMED-AT-OWNER**: `clusters/MATTER_COSMOLOGY_CLUSTER_SYNTHESIS_2026-05-19.md:20` *"ℤ → {2, 3} → Størmer wall → tuple (2, 3, 2, 0) → 4/81"*.
- **FIG. 1** five boxes, left→right, labels verbatim as filed (Input `S` → Mechanism Class Enumeration → Functional Stage Decomposition `(n₁,…,n_k)` → Identity Vector `v ∈ ℂⁿ` → Output `[[n,k,d_eff=2S−1]]`). **NO NUMERALS beyond the formula.**
- **FIG. 6** decoding pipeline, five blocks; syndrome vector `s = (s₁, s₂, s₃)`; ### **"64-Entry Syndrome Lookup Table"** — **NO-OWNER-FOUND** for the 64 as a figure value; it is the `2⁶` syndrome space of the Steane code and the filing states it directly. *Said plainly: this rests on the filing.*
- **FIG. 7** axes `0–0.5` (physical error rate per stage) and `0–1` (logical protection probability); solid = *"Standard [[7,1,3]] decoder (d = 3)"*; dashed = *"Formation-block decoder (d_eff = 5)"*; ### **vertical reference line at error rate = 0.2**. **NO-OWNER-FOUND** for the `0.2` crossover annotation — filing-only. ***The filing says the line "illustrates the crossover region"; it does not assert a computed crossover at 0.2.*** **Draw it as illustrative.**
- **FIG. 5** encoder: 8 horizontal lines, top = *"Logical input qubit"*, lines 2–8 = *"Ancilla qubit |0⟩"*; Hadamards on ancillas **2, 3, 4** at the first timestep; **six** CNOTs implementing `X_a, X_b, X_c`.

---

## 2. P-FANO-WPT (`P_FANO_WPT_PROVISIONAL_FILING.pdf`) — FIG. 1–11

### 2.1 The Fano coordinates and lines — ### **VERIFIED ARITHMETICALLY, NOT BY PATTERN MATCH**

**Filing FIG. 2, verbatim:** `P₁=(1,0,0) P₂=(0,1,0) P₃=(0,0,1) P₄=(1,1,0) P₅=(1,0,1) P₆=(0,1,1) P₇=(1,1,1)`;
`L₁={P₁,P₂,P₄} L₂={P₁,P₃,P₅} L₃={P₁,P₆,P₇} L₄={P₂,P₃,P₆} L₅={P₂,P₅,P₇} L₆={P₃,P₄,P₇} L₇={P₄,P₅,P₆}`.

> ### **CHECK RUN: every line's three points XOR to `(0,0,0)` over 𝔽₂ — ALL SEVEN COLLINEAR — and every point lies on EXACTLY THREE lines.** ### **THE FILED INCIDENCE STRUCTURE IS A CORRECT PG(2, 𝔽₂).** *This is a derived check on the filed values, not a citation.*

**Verdict: CONFIRMED — internally, by construction.** The filing also notes the standard diagram draws **one curved line** (the circle through three points): that is `L₇ = {P₄,P₅,P₆}` in this labelling, being the only line of three non-basis points. ***That identification is this dossier's inference from the filed coordinates, not the filing's words*** — **flagged as such.**

### 2.2 The engineering constants — ### **THE TILDE LAW FIRES ON MOST OF THESE**

| Value | Filing wording, verbatim | Status |
|:--|:--|:--|
| **`Q ≥ 2000`** | *"each resonator has loaded quality factor Q ≥ 2000"* (preferred embodiment; **Claims 3 and 12**); *"The Q target of ≥ 2000"* | ### **THE CLAIM LIMITATION. Exact as filed.** |
| **`Q ≈ 2000`** | FIG. 6 only: *"half-power width approximately 3.4 kHz (corresponding to Q ≈ 2000)"* | ### **DESCRIBES THE DRAWN SPECTRUM, not the claim.** ***Both forms are correct in their places and a renderer must not swap them.*** |
| **`Δf_grad ≈ 4.14·f_v/Q`** | *"The gradient zone (transition from peak to skirt) has effective width Δf_grad **≈** 4.14·f_v/Q, where the constant 4.14 derives from the Lorentzian profile geometry between the 10-dB and 3-dB points combined with interference physics between adjacent modes"* | **The relation is APPROXIMATE; the constant `4.14` is exact as filed.** **NO-OWNER-FOUND** — filing-only, with its derivation stated in prose. |
| **`≈ 14 kHz`** | *"Q ≥ 2000 yields Δf_grad ≈ 14 kHz"* | ### **UNVERIFIED-AS-EXACT (tilde law).** Annotate as approximate. |
| **peak separation `≈ 25 kHz`** | *"separated by approximately 25 kHz"* | ### **UNVERIFIED-AS-EXACT (tilde law).** |
| **half-power width `≈ 3.4 kHz`** | *"half-power width approximately 3.4 kHz"* | ### **UNVERIFIED-AS-EXACT (tilde law).** |
| **substrate `≈150 mm × 150 mm`; pitch `≈35 mm`** | *"dimensions approximately 150mm × 150mm … coil-to-coil center pitch approximately 35mm"* | ### **UNVERIFIED-AS-EXACT (tilde law).** **NO-OWNER-FOUND.** |
| **FIG. 6 axis `6.7–6.9 MHz`** | verbatim | exact as filed |
| **comparators `Qi: Q≈100 · AirFuel: Q≈200–300 · Witricity: Q≈950`** | verbatim, all with `≈` | ### **UNVERIFIED-AS-EXACT (tilde law); third-party figures, NO-OWNER-FOUND.** ***These are competitor claims and should be drawn as cited comparisons, not as measurements.*** |

### 2.3 The VNA κ-extraction — ### **CONFIRMED VERBATIM**

**Filing FIG. 5, the six-step flowchart:** sweep `f₁−Δf` to `f₇+Δf` → record `|S₂₁(f)|²` → identify peaks `f₁…f₇` → compute `max_f |S₂₁(f)|²` → ### **compute `κ(mode_v) = |S₂₁(f_v)|² / max_f |S₂₁(f)|²` for each `v ∈ {1,…,7}`** → output the κ vector. **Ports 1 and 2, standard 50-ohm coax.**

**The κ definition itself is owned in the filing's own §1** (*"an interface … carries a conservation strength κ ∈ [0,1] … κ = 0 indicates the interface transmits zero information about P"*, P-ZONE) — **CONFIRMED**, and the WPT filing's `|S₂₁|²` ratio is its **measurement realisation**, not a second definition. *A renderer should not label the VNA quantity "the definition of κ".*

### 2.4 FIG. 1, 3, 4, 7

- **FIG. 1**: seven planar spiral inductors `C₁…C₇`; ### **`C₇` at the centroid, `C₁…C₆` at the vertices of a regular hexagon**; each labelled with its mode frequency `f₁…f₇` **and its `(𝔽₂)³` coordinate**.
- **FIG. 3**: transmitter chain — power source → ### **CSS encoder via the Steane `[[7,1,3]]` stabilizer structure** → seven-channel driver bank (seven PAs) → seven coupled resonators.
- **FIG. 4**: receiver chain — seven matched resonators → detector bank → ADCs → DSP with syndrome computation and ### **64-entry lookup** → output conditioning.
- **FIG. 7**: two stacked waveforms, shared time axis; lower trace shows ### **channel `C₃` deliberately detuned at `t = T₀`** with transient then recovery. **No numerals.**

---

## 3. PROV-1 (`PROV1_FILING.pdf`) — Figures 1–13 at §13

### 3.1 The circuit counts — ### **ALL FOUR CONFIRMED, AND THE FILING'S OWN ARITHMETIC CHECKS OUT**

**Filing, verbatim:** *"(k = 3 stages of **5,502**, **4,298**, and **1,575** constraints respectively), the largest single proof drops from **10,494** to 5,502 constraints—a **48%** reduction. The decomposed total (**11,375** constraints) exceeds the monolithic total (10,494)…"*
**Figure 2, verbatim:** *"Left: single circuit, 10,494 constraints, one trusted setup. Right: three sub-circuits (5,502 + 4,298 + 1,575 = 11,375 constraints) … **8.4% constraint overhead** buys independent upgradeability, parallel proving, and failure isolation."*

> ### **ARITHMETIC VERIFIED THIS ACT:** `5,502 + 4,298 + 1,575 = 11,375` ✓ exactly as stated · `11,375 > 10,494` ✓ **the filing states its own overhead against itself** · `881 / 10,494 = 8.395%` → **8.4% ✓** · `(10,494 − 5,502)/10,494 = 47.57%` → ### **"48%" IS ROUNDED, and the figure should say ~48% or 47.6%, not assert 48% as exact.**

**NO-OWNER-FOUND** for all five counts: these are engineering measurements of a circuit implementation and no research document owns them. ***Said plainly, and it is not a defect.***

### 3.2 The κ spectrum and the zone layout

- **Figure 3**: κ axis `0 → 1` with ### **DARK (0) · GRADIENT (0.01–0.3) · MODERATE (0.3–0.7) · BRIGHT (0.7–1.0)**. **NO-OWNER-FOUND** for the band edges — filing-only. ***Note the bands are not a partition: `0` and `(0, 0.01)` are not covered by any named band.*** **Draw the boundaries exactly as the filing states them; do not silently extend a band to cover what no band covers.**
- **Figure 5**: seven qubits in three zones ### **(2-3-2)**, strong intra-zone / weak inter-zone coupling, **`d_eff = 5`**. **CONFIRMED-AT-OWNER** (as §1.1).
- **Figure 7**: three zones (2-3-2), separate power domains, separate clock domains, EM shielding; annotated ### **"formation d_eff = 5 at 0% overhead vs TMR d = 2 at 200% overhead"**. **NO-OWNER-FOUND** for the TMR comparison figures — filing-only.
- **Figure 9**: six systems all producing ### **formation (2,3,2,0) = 7**. **CONFIRMED-AT-OWNER** (as §1.4). *The tuple sums to 7 with the fourth entry 0 — consistent with `S = 3` non-empty stages and the 2-3-2 zone layout.*
- **Figures 1, 4, 6, 8, 10, 11** carry structure and labels, **no load-bearing numerals** beyond those above.

---

## 4. SUMMARY

| Class | Count |
|:--|--:|
| **CONFIRMED-AT-OWNER** | 8 |
| **DIVERGES** (descriptor only, values confirmed) | 1 — FIG. 4 *"approximately symmetric"* vs the owner's exactly symmetric matrix |
| **NO-OWNER-FOUND** (filing-only, properly so) | 11 |
| ### **UNVERIFIED-AS-EXACT (tilde law fired)** | ### **8** |
| **Name-collision hazards flagged at full prominence** | 1 — `C₁` (filing, 3×3) vs `C^{(1)}` (owner, 4×4) |
| **Derived checks run and PASSED** | 3 — the Fano incidence; the FIG. 2/FIG. 3 stage cross-check; PROV-1's constraint arithmetic |

### **THE THREE THINGS A RENDERER MUST NOT GET WRONG**

1. ### **`[[7,1,3]]` IS THE PHYSICAL CODE; `[[7,1,5]]` IS THE EFFECTIVE ONE.** *FIG. 5 draws the `[[7,1,5]]` encoder; FIG. 7's solid curve is the `[[7,1,3]]` decoder.*
2. ### **FIG. 4 MATRIX A IS THE OWNER'S 3×3 `C`, NOT THE 4×4 `C^{(1)}` — AND IT IS SYMMETRIC, AT `δ = 0.3`.**
3. ### **EIGHT VALUES CARRY APPROXIMATION MARKS IN THE FILING ITSELF.** *Drawing them as exact would state something the filing does not.*

---

## Provenance

Read at content 2026-08-24 from the three filed PDFs named in §0, by full-text
extraction with **every verdict taken from the surrounding passage, not from a
pattern hit** (*a regex is not a read* — b147). Corpus owners located by content
search and read at their passages. ### **The package's reconstructions were not
consulted.** The TECHNE drawing conventions were **not locatable** and none was
invented. **Nothing deposits. Nothing circulates. Nothing here bears on `h2`.**
