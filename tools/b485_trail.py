# -*- coding: utf-8 -*-
"""b485_trail.py -- THE TRAIL RECORD, APPENDED. ### **APPEND-ONLY, BOM PRESERVED, PREFIX PROVED.**"""
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

R = json.load(io.open(os.path.join(D, 'b485_results.json'), encoding='utf-8'))
SPAN = json.load(io.open(os.path.join(D, 'b485_span.json'), encoding='utf-8'))

ENTRY = """
### b485 — the two records read, and the circulation gate's pass run — filed 2026-09-22

**The gate is DISCHARGED on the current deposit state — and the same pass filed seven findings, five of them in the authority itself.** *The two manifests entered the record by the author's fetch under `(R94)`; **this seat fetched nothing** and **nothing at Zenodo was written**.*

#### Component 0 — the other run, without opening its log

`pid 27508`'s CPU time was **1.75 s**, and **1.75 s** again sixty seconds later: **a delta of zero**.

**And that zero is not a hung run.** `27508` is the `cmd.exe` launcher — `cmd /c b475_detached_run.cmd` — which spends its life waiting on a child and burns no CPU by construction. The process table, read at the same moment and **without opening the log**, shows `lake build Zeta23.ThmDE.Mult` with `lean` at **54.8 s** CPU. The log has been silent because `lake build <module>` writes its marker when a module **ends**, not while it runs.

> **A silent log and an idle launcher are both consistent with progress, and neither is evidence of it — the child's CPU is.**

#### Component 1 — the manifests

Both files recompute **exactly** to the hashes `(R94)` prints, and neither carries a BOM. No mismatch, so nothing is `ABSENT`.

| | `19675356` | `21432399` |
|:--|:--|:--|
| version | **v1.0.1** | **v1.1.0** |
| publication_date | **2026-04-21** | **2026-07-18** |
| concept | 19675355 | 19675355 |
| files | 10 | 11 |
| manuscript, from its own description | not stated | **v5.8** |

**Both carry concept `19675355`** — the concept REGISTRY names for the monograph — **so both are versions of the deposit REGISTRY already governs**, said from their own fields and not inferred from an adjacent id.

#### Component 2 — the two currency writes

**`b395`'s note, drafted ninety acts ago and written nowhere, is now written** — appended to `ERRATA.md` as `E-2026-09-22-1`. It went there and not to `meta/ZENODO_METADATA.md` because that file's own banner freezes its table (*"left unedited on purpose"*), while `ERRATA.md` is the append-only corrections ledger and already carried the precedent: *"a drift repair by appending; the head is not edited, the ledger's own law."*

**And the manifest corrected half the draft on arrival.** The draft reads *"manuscript v5.8 (2026-07-24)"*:

- **`v5.8` — CONFIRMED** by the record's own description.
- **`(2026-07-24)` — REFUTED.** The record published **2026-07-18**; `2026-07-24` belongs to `v1.1.2`.

The draft is **quoted verbatim and the correction stands beside it**, not folded into it. *A draft is not improved in silence.*

#### Component 3 — the gate's pass

| site | monograph | SIDE-kernel | SIDE-lv-conservation |
|:--|:--|:--|:--|
| `README.md` | v1.1.2 **agrees** | v1.5 **agrees** | v0.10.0 **agrees** |
| `SPIRAL_MAP.md` | v1.1.2 **agrees** | v1.5 **agrees** | v0.10.0 **agrees** |
| `REGISTRY.md` *(authority)* | v1.1.2 | v1.5 | v0.10.0 |
| memory — session | v1.1.2 **agrees** | v1.5 **agrees** | NOT STATED |
| memory — executor | **NOT LOCATABLE** per `b481` — recorded, **not reconciled** |

**Cells disagreeing: `0`.** The two new records move none of them, because both are *earlier* versions and neither bears on the current deposit state.

**But the pass filed seven findings, and five are in the authority itself:**

| address | | |
|:--|:--|:--|
| `REGISTRY.md:410` | date `2026-04-28` | the record says **2026-04-21** |
| `REGISTRY.md:410` | no version DOI | the record's is **`…19675356`** |
| `REGISTRY.md:412` | version `v1.1` | the record says **v1.1.0** |
| `REGISTRY.md:412` | date `2026-07-19` | the record says **2026-07-18** |
| `REGISTRY.md:412` | no version DOI | the record's is **`…21432399`** |
| `meta/ZENODO_METADATA.md:22` | attributes `v5.8` to v1.1.1 / 21436278 | the manifest says `v5.8` is **21432399 = v1.1.0** |
| `b395`'s draft | `(2026-07-24)` | the record says **2026-07-18** |

**Rule 5 makes REGISTRY the authority, and every prior pass reconciled other sites *to* it. This is the first time the authority itself has been caught** — because it is the first pass with the records in hand. **An authority is authoritative over the corpus, not over the platform**, and the gate's own words ask for both. Both history rows are **annotated, neither rewritten**.

**And one finding is filed and not fixed, by its target's own law.** `meta/ZENODO_METADATA.md`'s table declares itself *"left unedited on purpose: a ledger of what was true on 2026-07-18"*. **Editing a ledger that declares itself frozen would break a law to repair a fact**, and the law is worth more than the line. Filed at its address; routed to an author's ruling.

#### The gate

**DISCHARGED**, with a dated line at `REGISTRY.md:523` naming this act as its reason and the gate's text otherwise untouched. **The line names its own scope**: the current deposit state, and nothing else — the seven findings are annotated below the history table and left standing. **A gate discharged on one question is not a corpus found clean.**

**Every corpus write is an append or an annotation.** Lines of the old file absent from the new: **`0`** in all three — and git's own `--numstat` reads **`-0`**, because each preserved original still matches. `ERRATA.md` **+16/−0**, `REGISTRY.md` **+15/−0** then **+22/−0**.

#### The expectations

| | verdict |
|:--|:--|
| **(N1)** 19675356 is an earlier version under concept 19675355 | **HELD** — v1.0.1, 2026-04-21 |
| **(N2)** its note is historical, not corrective | **HELD, with the qualification registered in advance** — the note is historical, but `:412` is *wrong on the date*, so something corrective **is** owed there |
| **(N3)** the pass finds no disagreement and the gate is discharged | **SPLIT** — discharged on the table, **refuted on the pass** |

#### Two defects in this act's own instruments

**The index-query gate refused this face twice — on an arm's own *name*, and then on the paragraph explaining the rename.** A gate on raw text fires on the act's own account of what it did not do. The arm was renamed and the explanation written without the token; **the gate was obeyed and not argued with**.

**And the desk tool wrote its row, then crashed.** `corr_row.write_row` **appends and is not idempotent** — despite every desk bank since `b194` heading it *"the idempotent tool"*. A re-run would have written a second row for the same act. A guard now reads the ledger before writing. **A name repeated in fifty headings is not a property.** Routed: the guard belongs in `corr_row.py`, not in one act's copy.

#### What this act does not do

**Nothing at Zenodo is written and nothing deposits.** This seat fetched nothing. `b475`'s log was not opened and its run not polled or stopped. No chain is run. No corpus grade moves; no `d1-1` row is rewritten; no ledger row of `FACES_LEDGER` is touched; row U1 is unedited; no bridge typed; `h2` where the deposit left it; **the four lists stay OPEN**; no claim about RH in either direction.

The span by the tool reads **{span}** — two past the declared fold threshold. The ferry's order stands: **b479, then b482, then the fold.** The desk is at fifty-one, two closed and four minted.
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
    print('b485_trail.py -- THE TRAIL RECORD, APPENDED.')
    print('=' * 96)
    print('  bytes before        : %d' % len(before))
    print('  bytes appended      : %d' % len(add))
    print('  bytes after         : %d' % len(after))
    print('  BOM still present   : %s' % after.startswith(b'\xef\xbb\xbf'))
    print('  PRIOR BYTES A TRUE PREFIX : %s' % after.startswith(before))
    print('  arithmetic closes   : %s' % (len(after) == len(before) + len(add)))
    txt = after.decode('utf-8-sig', 'replace').replace(chr(13), '')
    heads = [l for l in txt.split(NL) if l.startswith('### b485 ')]
    print('  b485 headings in the file : %d ### -- PASS only on 1' % len(heads))
    ok = (after.startswith(before) and after.startswith(b'\xef\xbb\xbf')
          and len(after) == len(before) + len(add) and len(heads) == 1)
    print('  ### %s' % ('PASS' if ok else '### FAIL'))
    print('=' * 96)
    io.open(os.path.join(D, 'b485_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        'before %d appended %d after %d prefix %s bom %s headings %d verdict %s%s'
        % (len(before), len(add), len(after), after.startswith(before),
           after.startswith(b'\xef\xbb\xbf'), len(heads), 'PASS' if ok else 'FAIL', NL))
    return 0 if ok else 2


if __name__ == '__main__':
    sys.exit(main())
