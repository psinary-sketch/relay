# -*- coding: utf-8 -*-
"""b487_trail.py -- THE TRAIL RECORD, APPENDED. ### **APPEND-ONLY, BOM PRESERVED, PREFIX PROVED.**"""
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

R = json.load(io.open(os.path.join(D, 'b487_results.json'), encoding='utf-8'))
SPAN = json.load(io.open(os.path.join(D, 'b487_span.json'), encoding='utf-8'))

ENTRY = """
### b487 — the errata renumber, and the Zenodo description drafts — filed 2026-09-22

**The id collision is resolved by append, the guard is now in the tool, and three of twelve description sentences rest on an erratum.**

#### Component 1 — (R97) executed

**`b469`'s entry keeps `E-2026-09-22-1`**, having been filed earlier. **`b485`'s becomes `E-2026-09-22-2`** by a dated line appended beneath it, stating the renumber and its reason. Two dated correction pointers are appended — to b485's trail record and to its bank.

| write | | lines of the old file absent from the new |
|:--|--:|--:|
| `ERRATA.md` | +995 bytes | **0** |
| `OPEN_TRAILS.md` (pointer) | +334 bytes | **0** |
| `data/b485_the_two_records.txt` | +275 bytes | **0** |

**No existing line is edited and no id is rewritten in place.** BOM and prefix proved on all three. **b486's fold cites b469's entry, so its clause (6) is correct as written and was not touched.**

**And the guard is now in the tool, not in an act.** `tools/errata_append.py` **refuses a duplicate id before it writes**, with both controls exercised before it touched the ledger: **a duplicate it must refuse** (code 2, file unchanged) and **a fresh id it must accept** (code 0, file grew). *An arm that cannot refuse is not a guard.*

#### Component 2 — the three descriptions, read

**Nothing fetched.** Each source is named: the monograph's from `relay data/b359_fetch_F2.json` (the record's own fetched JSON, banked at b359, read by the 2026-09-14 act b455); the kernel's from `.zenodo.json` at tag `v1.5`; lv's from `README.md` at `v0.10.0`, per b462's precedent.

**Twelve sentences assert a machine check, a compiled proof, or a verified claim** — six, three and three.

**And the screen's first version would have missed this act's central row.** It caught `compile`, `verified` and `machine-check` and **not `proves`** — so the kernel's *"The kernel proves that no off-line zero exists by exhaustively excluding every mechanism class"* scored as **no claim at all**, when it is precisely the sentence `E-2026-09-14-1` was filed against. The order asked for a machine check, a compiled proof, **or a verified claim**, and a kernel saying it *proves* something is the third. Widened; **both yields printed — ten, then twelve.**

#### Component 3 — the drafts

| record | sent | erratum | disposition |
|:--|--:|:--|:--|
| 21539167 | 5 | NO ERRATUM | left as it stands |
| 21539167 | 9 | NO ERRATUM | left as it stands |
| 21539167 | 10 | NO ERRATUM | left as it stands |
| **21539167** | **14** | **E-2026-09-14-1** | **replacement drafted** |
| **21539167** | **15** | **E-2026-09-22-1** | **replacement drafted** |
| 21539167 | 16 | NO ERRATUM | left as it stands |
| **21520474** | **2** | **E-2026-09-14-1** | **replacement drafted** |
| 21520474 | 3, 4 | NO ERRATUM | left as they stand |
| 21539068 | 8, 12, 17 | NO ERRATUM | left as they stand |

**Three rest on an erratum; nine are left as they stand**, each with its reason — and one reason is the erratum's own: monograph sentence 5 is the **manuscript's** claim, and `E-2026-09-14-1` says *"Whether the manuscript proves the catalogue's exhaustiveness is untouched by this entry."*

**Every replacement is drawn from its erratum's own words and nothing wider, and names a terminal in full.** Two name **`structural_exhaustiveness_proved`**. The third names **`conservation_s_dark`** — **and says in the same sentence that the concordance records it as a `SHELL`, a stand-in** — because a replacement that named a shell without saying so would be worse than the sentence it replaces.

**The drafts are banked and NOT applied. Nothing at Zenodo is written.** The author applies them at the platform; the act after fetches each description back and banks it **before any record says the edit was made**.

#### The expectations

| | verdict |
|:--|:--|
| **(N1)** monograph ≥ 2, kernel ≥ 1 resting on an erratum | **HELD** — 2 and 1 |
| **(N2)** lv carries none | **HELD on the population that matters** — lv carries **three** check-asserting sentences, but **neither erratum names lv among its affected deposits**, so **none rests on an erratum**. The face registered this split in advance. |
| **(N3)** every replacement names a terminal by its full name | **HELD** — three of three |

#### And a finding about the span tool

It still names **b474** as the last fold and reads **13** — because it looks for a fold in `FINDINGS.md`, and **b486 filed its fold record to `OPEN_TRAILS.md` alone**. **By filing, the span since b486's fold is one: this act.** The tool is not edited, per `(R96)`, and the figure is printed with what it means. **Routed** — either a fold writes a `FINDINGS` section as b331's generator did, or the tool is taught the trail, and that is a ruling's choice.

#### What this act does not do

**Nothing fetched and nothing at Zenodo written.** Nothing compiled. No corpus grade moved; no existing ERRATA line edited; row U1 unedited; no bridge typed; **`h2` where the deposit left it**; the four lists stay OPEN; no claim about RH in either direction.

*The span by the tool reads **{span}** — see the finding above for what that figure counts.*
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
    print('b487_trail.py -- THE TRAIL RECORD, APPENDED.')
    print('=' * 96)
    print('  bytes before        : %d' % len(before))
    print('  bytes appended      : %d' % len(add))
    print('  bytes after         : %d' % len(after))
    print('  BOM still present   : %s' % after.startswith(b'\xef\xbb\xbf'))
    print('  PRIOR BYTES A TRUE PREFIX : %s' % after.startswith(before))
    print('  arithmetic closes   : %s' % (len(after) == len(before) + len(add)))
    txt = after.decode('utf-8-sig', 'replace').replace(chr(13), '')
    heads = [l for l in txt.split(NL) if l.startswith('### b487 ')]
    print('  b487 headings in the file : %d ### -- PASS only on 1' % len(heads))
    ok = (after.startswith(before) and after.startswith(b'\xef\xbb\xbf')
          and len(after) == len(before) + len(add) and len(heads) == 1)
    print('  ### %s' % ('PASS' if ok else '### FAIL'))
    print('=' * 96)
    io.open(os.path.join(D, 'b487_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        'before %d appended %d after %d prefix %s bom %s headings %d verdict %s%s'
        % (len(before), len(add), len(after), after.startswith(before),
           after.startswith(b'\xef\xbb\xbf'), len(heads), 'PASS' if ok else 'FAIL', NL))
    return 0 if ok else 2


if __name__ == '__main__':
    sys.exit(main())
