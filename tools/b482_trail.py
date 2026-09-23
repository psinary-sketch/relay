# -*- coding: utf-8 -*-
"""b482_trail.py -- THE TRAIL RECORD, APPENDED. ### **APPEND-ONLY, BOM PRESERVED, PREFIX PROVED.**"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

R = json.load(io.open(os.path.join(D, 'b482_results.json'), encoding='utf-8'))
SPAN = json.load(io.open(os.path.join(D, 'b482_span.json'), encoding='utf-8'))

ENTRY = """
### b482 — the XiPrime topic read against the corpus statements — filed 2026-09-22

**Twenty-four placement cells, and not one is `SAME OBJECT`.** *And first, a halt.*

#### b479 is not run, because its order is not banked

The order says *"b479 RUNS AS BANKED."* Every ferry file in the bank was searched for `ACT b479` and **not one carries it**. The same search for `ACT b482`, as a **positive control**, finds `b482_ferry.txt` — so the search works and would have found a b479 order had one been banked.

**And three sealed faces say otherwise.** `b480`, `b483` and `b484` each assert that b479 is *"registered by its own ferry."* The claim propagated because **each face copied the last one's sentence**, and a sealed face is exactly the kind of document a later act trusts without re-checking.

> **A seal certifies that the bytes have not changed. It certifies nothing about whether they were true.**

**b479 is not run and its order is not reconstructed from memory.** Re-issue it, or strike the number.

#### Component 1 — the six statements

The clone's HEAD is `fbdc36bbf17d20af3fd0447c6d1a8a02773c9844`; the order's pin is `fbdc36b`. The six are printed verbatim with their hypotheses in `data/b482_components.txt`.

**All six are closed by `sorry`** — the file carries seven `sorry` tokens. **They are challenge statements, not theorems held**, and every sentence of this act that describes them says so, by a bar on the face.

`comparator-xiprime.json` lists **exactly those six**, `definition_names` is **empty**, and the permitted axioms are **`propext`, `Quot.sound`, `Classical.choice`** — the three Lean's own `#print axioms` calls standard, and not a licence for an extra hypothesis.

#### Component 2 — the corpus's own statements, as statements

| | | read at |
|:--|:--|:--|
| **(A)** the geometric clause | *"At every simple zero ρ on the critical line, ξ'(ρ) is purely imaginary."* — `A_Place_to_Stand.md:304` | the **deposited** copy |
| **(B)** `spectral_cannon` | `(t : ℝ) : (deriv completedRiemannZeta₀ ⟨1/2, t⟩).re = 0` — **proved** | SIDE-kernel **v1.5** |
| **(C1)** `transversal_generic_empty` | `(curveDim obstrCodim : ℤ) (hcurve : curveDim = 1) (hcodim : 2 ≤ obstrCodim) : curveDim - obstrCodim < 0` | SIDE-simplicity **v0.1.0** |
| **(C2)** `codim_margin` | `(lost : ℤ) (h0 : 0 ≤ lost) (h3 : lost ≤ 3) : curveDim < numSources - lost` | SIDE-simplicity **v0.1.0** |

**And (C1) and (C2) quantify over `ℤ` and nothing else.** Neither mentions `ξ`, `ζ`, a zero, or a complex number; `curveDim` and `numSources` are integer constants and both are closed by `omega`. **The mathematics they are named for lives in their docstrings**, which the order excludes. *This is a reading of what the statements say, and not a judgement on the repository* — the face said so before the placement ran.

The declaration reader was rehearsed on both polarities before the seal, under `(R70)`: on `xiPrime_over_xi_re_pos` it returned the statement and **not** the docstring, the proof token or the `sorry`.

#### Component 3 — the placement

| declaration | (A) | (B) | (C1) | (C2) |
|:--|:--|:--|:--|:--|
| `xiPrime_zeros_in_open_critical_strip` | TOUCHES | TOUCHES | APART | APART |
| `xiPrime_over_xi_re_pos` | **APART** | **APART** | APART | APART |
| `xiPrime_simple_zeros_on_critical_line` | TOUCHES | TOUCHES | APART | APART |
| …`_cumulative` | TOUCHES | TOUCHES | APART | APART |
| …`_quartic` | TOUCHES | TOUCHES | APART | APART |
| …`_quartic_cumulative` | TOUCHES | TOUCHES | APART | APART |

**24 cells — `SAME OBJECT` 0, `TOUCHES` 10, `APART` 14.**

The deciding clause for the closest pair: the shared term is `ξ'`, **but the quantified set is not** — the clause ranges over **zeros of `ξ`**, the declaration over **zeros of `ξ'`**. *Two different sets of points.*

All twelve cells against (C1) and (C2) are `APART` for one reason: **there is no shared object to be the same as or to touch.** And `xiPrime_over_xi_re_pos` is `APART` from (A) and (B) for a different one — it quantifies over the half-plane `1 ≤ Re s` while both speak of the critical line, so **the regions are disjoint**.

#### The two reverse reads

**What the six state that the corpus does not:** a **positive proportion with a number** — `0.85838`, `0.92919`, and `0.86864`, `0.93432` in the quartic window; **the location of every zero of `ξ'`**; a **half-plane positivity for `ξ'/ξ`**; and a **counting apparatus** (`Ncount`, `Ndist`, `N0simple`, with multiplicity in the denominator). The corpus states no proportion of the zeros of `ξ'` anywhere, at any tag read here.

**What the corpus states that the six do not:** a **pointwise value of `ξ'` at every point of the critical line** — `spectral_cannon`, for *all* `t`, **not only at zeros**, and **proved, not posed**; the **codimension dichotomy for the zeros of `ξ`**; and an **integer margin**.

> **The corpus's one proved statement about `ξ'` is stronger pointwise than anything the six assert about its value; the six assert a quantitative count the corpus never attempts. Neither side subsumes the other, and no cell is `SAME OBJECT`.**

#### The expectations

| | verdict |
|:--|:--|
| **(N1)** at least one declaration is `SAME OBJECT` with the perpendicular-crossing statement | **REFUTED** — zero cells |
| **(N2)** no declaration states uniform transversality, so the geometric clause stays open | **HELD** |
| **(N3)** the six count zeros of `ξ'` rather than bounding one zero's derivative | **HELD of the file's character, false of two of its six members** — registered as a split in advance |

#### What this act does not do

**No Lean is run and no kernel is built** — statements are read as text at their tags. **Nothing is imported**, and the zeta23 artefacts are never committed. **No grade is conferred on any corpus object**: a placement verdict is a relation between two statements, not a judgement on either. Row U1 unedited; no bridge typed; `h2` where the deposit left it; the four lists stay OPEN; no claim about RH in either direction. **The kernel lane closes at this act's end.**

*The span tool reads **{span}** for this act — lower than b485's, because b482's **number** is below it and the tool cannot place an act filed out of number order. Twelve acts have run since the fold. The fold should take its own number's reading.* **The fold is ordered and is not opened here:** the order places it after b479, and b479 has not run.
"""

ENTRY = ENTRY.replace('{span}', str(SPAN['current_span']))


def main():
    before = io.open(OT, 'rb').read()
    tail = before.decode('utf-8-sig', 'replace')[-2:]
    sep = '' if tail.endswith(NL + NL) else (NL if tail.endswith(NL) else NL + NL)
    add = (sep + ENTRY.strip(NL) + NL).encode('utf-8')
    io.open(OT, 'ab').write(add)
    after = io.open(OT, 'rb').read()

    print('=' * 96)
    print('b482_trail.py -- THE TRAIL RECORD, APPENDED.')
    print('=' * 96)
    print('  bytes before        : %d' % len(before))
    print('  bytes appended      : %d' % len(add))
    print('  bytes after         : %d' % len(after))
    print('  BOM still present   : %s' % after.startswith(b'\xef\xbb\xbf'))
    print('  PRIOR BYTES A TRUE PREFIX : %s' % after.startswith(before))
    print('  arithmetic closes   : %s' % (len(after) == len(before) + len(add)))
    txt = after.decode('utf-8-sig', 'replace').replace(chr(13), '')
    heads = [l for l in txt.split(NL) if l.startswith('### b482 ')]
    print('  b482 headings in the file : %d ### -- PASS only on 1' % len(heads))
    ok = (after.startswith(before) and after.startswith(b'\xef\xbb\xbf')
          and len(after) == len(before) + len(add) and len(heads) == 1)
    print('  ### %s' % ('PASS' if ok else '### FAIL'))
    print('=' * 96)
    io.open(os.path.join(D, 'b482_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        'before %d appended %d after %d prefix %s bom %s headings %d verdict %s%s'
        % (len(before), len(add), len(after), after.startswith(before),
           after.startswith(b'\xef\xbb\xbf'), len(heads), 'PASS' if ok else 'FAIL', NL))
    return 0 if ok else 2


if __name__ == '__main__':
    sys.exit(main())
