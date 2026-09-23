# -*- coding: utf-8 -*-
"""b486_trail.py -- THE TRAIL RECORD, APPENDED. ### **APPEND-ONLY, BOM PRESERVED, PREFIX PROVED.**"""
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

R = json.load(io.open(os.path.join(D, 'b486_results.json'), encoding='utf-8'))
SPAN = json.load(io.open(os.path.join(D, 'b486_span.json'), encoding='utf-8'))

ENTRY = """
### b486 — the fold, eleven acts filed since b474 — filed 2026-09-22

**The span's mathematics moved little and its bookkeeping moved a great deal.** Eleven acts, in filing order; **seven of them record a defect of their own instruments**, and every one of those was caught by an arm, a control, or a rehearsal this record already had.

**Both span readings, per `(R96)`:** **11 by filing**; the tool reads **12** by number order, because it counts `b486` itself and cannot place an act filed out of number order. **Neither is wrong and the tool is not edited.**

#### Component 1 — the span, act by act

| | act | what it did, from its own closing bank |
|--:|:--|:--|
| 1 | **b475** | the axiom run launched, detached and serialized; closed **RUNNING** |
| 2 | **b478** | six sites against eight E0 constituents — **two sites bear on nothing the table grades, three constituents no site touches** |
| 3 | **b476** | the compression experiment registered, nothing computed; two of the order's own premises corrected |
| 4 | **b480** | the b475 log read as a snapshot — 169 of 188 modules, **every EXIT 0**; `(R82)` **NOT YET DECIDABLE** |
| 5 | **b477** | the Gram run launched detached; closed **RUNNING** |
| 6 | **b481** | the circulation gate read — the `(c')` job **ABSENT**, the bar **CAPABILITY**, **zero** of four sites disagree |
| 7 | **b483** | the Gram log read to its end — `(F1)` **FIRES**, `(F2)` **THRESHOLD-DEPENDENT**, `(F3)` **NOT MET** |
| 8 | **b484** | `(R92)` executed; **7** acts cite `trunc_bound`, **one** predicates it; verdict **SEPARATE OBJECTS** |
| 9 | **b485** | both manifests verified — `19675356` = **v1.0.1**, `21432399` = **v1.1.0**; the gate **DISCHARGED**, **seven** findings filed |
| 10 | **b482** | the XiPrime placement — **24 cells, `SAME OBJECT` 0**; and the b479 halt proved |
| 11 | **b479** | the seven classes — **TOUCHES: C2, C7**; **APART: C1, C3, C4, C5, C6** |

**A fold decides nothing new.** Every line is quoted from the act's own bank; no verdict is re-scored and none is invented.

#### Component 2 — the (R31) digest block, 2026-09-22

**The clause's coordinates, as the record holds them at b485.** Each clause names the act it is cited from.

1. **The six sites reduce to conditions on the test function, on the data of the representation, and on the instrument's truncation**, with (i) and (ii) the same object as K8 — *b478*.
2. **The class boundary at `a = √2`, reached by two routes** — *b110* · **[cited from outside the span]**
3. **zeta23's explicit formula contains b321's identity**, and the grade is `DERIVES, CONDITIONAL` on a profile that has not run — *b468r, b470, b480*.
4. **The compression register ran and takes NO GRADE**; its blocker is measured as the places-side quadrature bound, filed as `W-ORD-QUADRATURE-BOUND` — *b483, b484*.
5. **The circulation gate is DISCHARGED on the current deposit state**, with the authority's own five findings standing — *b485*.
6. **The eight unanchored sentences, under `E-2026-09-22-1`** — *b469, from b464* · **[cited from outside the span]**

**All six are said by a cited act** — checked needle by needle over **every banked file** before the block was written.

**And the check's first run was wrong, over the wrong population.** It searched the span plus five named acts and reported that **no act says** clauses (2) or (6) — which would have struck them from the digest. Both are said; the acts are simply older than the span. **A halt proved over the wrong population is not a halt.**

**The needles' own yields are printed.** Five discriminate — `K8` (21 acts), `sqrt 2` (61), `W-ORD-QUADRATURE-BOUND` (4), `E-2026-09-22-1` (5), `unanchored` (3). Five are permissive — `sites`, `conditional`, `no grade`, `DISCHARGED`, `five` — matching **85 to 264 acts each**. **A filter that keeps most of the corpus proves nothing**, so the block rests on the discriminating ones.

#### Component 3 — the two ledgers

**The navigator's — thirteen rulings in the span, not twelve.**

`(R84)` the h2 lane open · `(R85)` a face names each tool's write pattern · `(R86)` the numerical lane at b476's price · `(R87)` the signature read on `−G` · `(R88)` b477 stands, the word `[procedural]` · `(R89)` a disk-reading act may open · `(R90)` the gate's trigger struck · `(R91)` a face may carry its act's stem glob · `(R92)` the currency claim repaired · `(R93)` its addressee is b484 · `(R94)` the manifests by the author's fetch · `(R95)` a metadata edit is not a re-issue · `(R96)` b479 re-issued, the fold counts by filing.

**`(R88)` is named separately because it is not in a ferry file** — it was banked as `b477_r88_standing_order.txt`, and a count over ferries alone would have dropped it silently.

**The seat's — seven acts whose own closing records a defect of their own.**

`b480` a batch `FOR` block stamps one instant on every line · `b481` two files the sealed face's write list did not cover, **arm not weakened** · `b483` a predicate read backwards, and two word anchors eaten as backspace bytes · `b484` the census found **itself** · `b485` a gate fired on an arm's *name*, the desk tool wrote its row then crashed, an arm fired on the word "deposit" · `b482` an arm read live git inside its predicate, so it could not fail · `b479` a `def` and a `theorem` do not mean the same by `:=`.

**And one row that is not a defect of any act:** the **b479 closing reached the navigator truncated**. That is a *delivery* failure, not a fault in the act — its bank is whole on disk and its trail record is whole. **A message that did not arrive is not a record that was not made.**

#### One finding this fold makes about an act it folds

**`ERRATA.md` carries `E-2026-09-22-1` twice.** `b469` filed it under `(R77)` — *"Deposited sentences that assert a machine check, name no terminal…"*, the very entry clause (6) cites. `b485` appended a **second** entry under the same id, and **b485's suite had no arm that would have looked**.

**The fold reports it and does not renumber it.** ERRATA is append-only and its ids are cited elsewhere, so a renumber is a ruling's business and not a fold's. **Routed.**

#### What closed, and what was minted

**Closed in the span: 7** — the gate's absent trigger `(R90)`; the write-list granularity `(R91)`; the currency claim `(R92)`; the capability bar, by `(R94)` supplying a route rather than a ruling; b395's note, written at last — *and its id collided*; the compression register, run and closed at **no grade**; and the unbanked b479 order, re-issued by `(R96)`.

**Minted in the span: 19**, and one more by this fold.

#### What this fold does not do

**No expectations registered and none invented.** Nothing compiled. No corpus grade moved and no verdict re-scored. No ERRATA line written or renumbered. Row U1 unedited; no bridge typed; **`h2` where the deposit left it**; **the four lists stay OPEN**; no claim about RH in either direction.

*The next span begins at the act after this one.*
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
    print('b486_trail.py -- THE TRAIL RECORD, APPENDED.')
    print('=' * 96)
    print('  bytes before        : %d' % len(before))
    print('  bytes appended      : %d' % len(add))
    print('  bytes after         : %d' % len(after))
    print('  BOM still present   : %s' % after.startswith(b'\xef\xbb\xbf'))
    print('  PRIOR BYTES A TRUE PREFIX : %s' % after.startswith(before))
    print('  arithmetic closes   : %s' % (len(after) == len(before) + len(add)))
    txt = after.decode('utf-8-sig', 'replace').replace(chr(13), '')
    heads = [l for l in txt.split(NL) if l.startswith('### b486 ')]
    print('  b486 headings in the file : %d ### -- PASS only on 1' % len(heads))
    ok = (after.startswith(before) and after.startswith(b'\xef\xbb\xbf')
          and len(after) == len(before) + len(add) and len(heads) == 1)
    print('  ### %s' % ('PASS' if ok else '### FAIL'))
    print('=' * 96)
    io.open(os.path.join(D, 'b486_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        'before %d appended %d after %d prefix %s bom %s headings %d verdict %s%s'
        % (len(before), len(add), len(after), after.startswith(before),
           after.startswith(b'\xef\xbb\xbf'), len(heads), 'PASS' if ok else 'FAIL', NL))
    return 0 if ok else 2


if __name__ == '__main__':
    sys.exit(main())
