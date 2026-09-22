# -*- coding: utf-8 -*-
"""b484_trail.py -- THE TRAIL RECORD, APPENDED. ### **APPEND-ONLY, BOM PRESERVED, PREFIX PROVED.**"""
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

R = json.load(io.open(os.path.join(D, 'b484_results.json'), encoding='utf-8'))
SPAN = json.load(io.open(os.path.join(D, 'b484_span.json'), encoding='utf-8'))

ENTRY = """
### b484 — the currency repair, the quadrature work-order, and the support-edge test — filed 2026-09-22

Three things, and the third refuses an explanation rather than supplying one. *`(R93)` settled the addressee: `(R92)`'s repair belongs here, not to `b479` or `b482`, which run as banked after it.*

#### Component 1 — (R92) executed

`phase1.5/method/INVARIANCE_BARRIERS.md:580` stated the monograph's **current** deposit as `v1.1.1`, version DOI `10.5281/zenodo.21436278`. REGISTRY's governing `d1-1` row carries **`v1.1.2`**, version DOI **`10.5281/zenodo.21539167`** — and REGISTRY is the authority under Rule 5.

| | |
|:--|:--|
| the version word | `v1.1.1` → **`v1.1.2`** |
| the version DOI | `…21436278` → **`…21539167`** |
| the concept DOI `…19675355` | **already agreed — not touched** |
| the Day-1 deposit DOI `…19675356` | a different record, not a currency claim — **not touched** |

**Lines of the old file absent from the new file: `0`** — the original line is preserved **verbatim** in an appended annotation, so the old file's lines are a subset of the new file's. Git's raw counts are printed beside that sentence and not hidden behind it: **`+14 / -1`**, one line modified and an annotation added. **Other lines changed in place: `0`.** BOM and line ending were detected before the write and verified after it.

*Found at `b481`, filed there as a finding rather than fixed silently, repaired here by the ruling that followed — which is the route the circulation gate itself prescribes: **a disagreement found is a finding filed, not a silent fix.***

#### Component 2 — `W-ORD-QUADRATURE-BOUND`, filed

**The corpus holds no error bound for the places-side quadrature.** The chain reports `trunc_bound`, which bounds the truncation of the **zero sum**. `b483` measured the *achieved* two-side agreement at **4.562e-05** (aim plane) and **3.169e-06** (ladder) against a reported `trunc_bound` of **1.290e-12** and **6.421e-11** — **an under-statement of up to seven orders.** Any act citing `trunc_bound` as the chain's floor cites a bound that does not cover the dominant term. **Trigger:** the next opening of the numerical instrument lane, or the next act that cites a chain floor.

By tool over the banked acts, with this act's own stem excluded:

| | |
|:--|--:|
| acts citing `trunc_bound` | **7** — b321, b326, b340, b437, b476, b477, b483 |
| of those, acts **predicating** it as a floor or a chain bound | **1** — **b483** |

**The matcher's lineage, both yields printed.** Version 1 counted *co-occurrence* in a sentence and returned **2**; version 2 required *predication* and returned **1**. The difference is `b477`, whose sentence says the diagonal ran *within the floor* while `trunc_bound` was *printed beside* each cell — **two figures in one sentence and no claim that either is the other.** The residue was hand-read, not discarded, and version 2 was adopted **not because it gave the smaller number** but because predication is what the question asks for.

**The one act that does predicate it is `b483` — which refuted itself in its own Component 3.** The work-order is filed against a defect the record has already caught itself committing, which is the best evidence it is real and not a style note. **The chain is not edited and nothing in it is repaired.**

#### Component 3 — the support-edge test

**The loop has two comparators, not one.** The outer cap `p ** k <= math.exp(L) + PRIME_TOL` admits **with a `1e-12` tolerance**; the inner gate `if ln <= L` — which is what actually adds a term — admits **with no tolerance at all**, in log coordinates. And `L = 2.0 * math.log(a)` exactly, by `carto_atlas.bump` and `b318_square.autocorrelation`. So the deciding comparator is **`math.log(n) <= 2 log a`**, a weak inequality: `n <= a²` *read in logs*.

At the cell, to full precision:

| | |
|:--|--:|
| `a` | `4.123106` |
| `a * a` | **`17.000003087236`** |
| `a*a − 17` | **`+3.087236e-06`** |
| `L − log 17` | **`+1.816021e-07`** |
| outer cap, inner gate | **both admit** |

**So `17` enters the sum at that cell — and not at the edge.** The banks store the cell as the **rounded decimal** `4.123106`, not as `sqrt(17)`, and that rounding leaves the inner gate a margin of `1.816021e-07` in log units — **4.089e+08 times the float's own resolution there.** The edge case is never exercised at this cell, so **the admission owes nothing to the convention.**

**`b400`'s routed discrepancy is the same comparator** — `p^m <= a^2` against `p^m < a^2`, with the code on the weak side, which is `b321`'s stated *rule* and not `b321`'s printed *list*. And `b400` already priced it: ***"It moves no value … an endpoint prime power contributes `0` to (149) under either reading; what differs is a printed membership list."***

#### The verdict: **SEPARATE OBJECTS**

The deciding words are not this act's:

- **`b400`:** *"It moves no value."* **A convention that changes no number cannot be the common cause of three numbers.**
- **this act's arithmetic:** at `a = 4.123106` the prime is strictly inside, so **no inclusion decision is taken at this cell at all** — the convention is not merely harmless here, **it is not consulted**.
- **`b446`, on its own outlier:** *"Not the rung alone (3.605551 = sqrt(13) converged)"* — the record had already refused to read that cell's distinction off its arithmetic form.

`b437`'s rung is a **ladder index**, `b446`/`b447`'s outlier a **decorrelation residual order**, `b483`'s excursion a **Gram signature**. **They share a cell, not a cause.** What they do share is still unexplained, and **this act does not explain it** — naming a common cause the record shows cannot move a number would be worse than leaving the coincidence open. **It is left open.**

#### The expectations

| | the navigator's | verdict |
|:--|:--|:--|
| **(N1)** | the comparator admits the prime at the edge, so 17 enters | **SPLIT** — the conclusion holds, the reason does not |
| **(N2)** | `b400`'s routed discrepancy is the same comparator | **HELD** |
| **(N3)** | at least two of the three trace to that inclusion | **REFUTED** |

*The seat's own calls were on the sealed face before the components ran, and matched all three — including registering `(N1)` as a split on purpose.*

#### And one defect in this act's own census

The matcher's first run scanned `data/b484_*` and returned **`b484` itself** as a mis-scoping act — because the hand-read residue block **quotes** the offending sentence in order to judge it. **A quotation matches the rule that condemns what it quotes.** This is `b481`'s species a second time; the stem is now excluded by name rather than by hoping the run order hides it, and it was declared on the face before the seal. **The species has two instances now and belongs in a tool, not in each act's memory** — routed.

#### What this act does not do

**No chain is run and no entry computed** — `b321_window.py` was read as *text* and never imported; `math.log` on two numbers is arithmetic, not the chain. No lane is opened. `b449`'s and `b483`'s banks are unedited. `b475`'s log is not opened. Nothing is fetched. No corpus grade moves, no REGISTRY row is written, no ledger row is edited; row U1 is unedited; no bridge typed; `h2` where the deposit left it; the four lists stay OPEN; no claim about RH in either direction.

The span by the tool reads **{span}** — one past the declared fold threshold. The ferry's own order is `b479`, then `b482`, **then the fold**. The desk stands at forty-seven, one closed and two minted.
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
    print('b484_trail.py -- THE TRAIL RECORD, APPENDED.')
    print('=' * 96)
    print('  bytes before        : %d' % len(before))
    print('  bytes appended      : %d' % len(add))
    print('  bytes after         : %d' % len(after))
    print('  BOM still present   : %s' % after.startswith(b'\xef\xbb\xbf'))
    print('  PRIOR BYTES A TRUE PREFIX : %s' % after.startswith(before))
    print('  arithmetic closes   : %s' % (len(after) == len(before) + len(add)))
    txt = after.decode('utf-8-sig', 'replace').replace(chr(13), '')
    heads = [l for l in txt.split(NL) if l.startswith('### b484 ')]
    print('  b484 headings in the file : %d ### -- PASS only on 1' % len(heads))
    ok = (after.startswith(before) and after.startswith(b'\xef\xbb\xbf')
          and len(after) == len(before) + len(add) and len(heads) == 1)
    print('  ### %s' % ('PASS' if ok else '### FAIL'))
    print('=' * 96)
    io.open(os.path.join(D, 'b484_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        'before %d appended %d after %d prefix %s bom %s headings %d verdict %s%s'
        % (len(before), len(add), len(after), after.startswith(before),
           after.startswith(b'\xef\xbb\xbf'), len(heads), 'PASS' if ok else 'FAIL', NL))
    return 0 if ok else 2


if __name__ == '__main__':
    sys.exit(main())
