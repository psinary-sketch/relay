# -*- coding: utf-8 -*-
"""b497_trail.py -- THE TRAIL RECORD. ### **ONE APPEND; PREFIX PROVED, NOT ASSERTED.**"""
import hashlib
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


def read(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


HEADING = ('### b497 — the b495 build log read: KILLED, not failed; '
           'all three profiles ABSENT; Component 3 STOPPED')

BODY = """
%(heading)s

**(R108) ratified.** The grade cell **may be split**: where a terminal is a biconditional or a
conjunction whose parts grade differently, the cell reads two grades each with its part named —
`DERIVES(→) / INTERFACES(←)`. **The four grades are unchanged; this is a cell form, not a fifth
grade.** No ledger line is rewritten; improvised prose splits are re-celled as they are met, by
appended note. `e_difficulty` is routed to a statement-read act of its own and **this act does not
choose**. And the counts are corrected **from files**: the federation is **44** `SIDE-*`
repositories with a `.git` as K0 read them; the keystone class is **16** under the census's test,
**87** with Day-1's nine and the 62 candidates; the terminal population is **1,021** rows.

**COMPONENT 0.** `pid 7860` **GONE**; no `lake` or `lean` process alive. The log is **%(bytes)d
bytes, %(lines)d lines**. The act proceeds. *(The face declares that the seat read the log's first
eight and last six lines to decide this, and declares what that peek showed — a prediction drawn
from a peek must say so.)*

**COMPONENT 1 — THE LOG, COMMITTED UNCHANGED**, sha256 `%(sha)s`.

| | |
|:--|:--|
| marks (stamped lines) | **%(marks)d** |
| **distinct instants** | **%(instants)d** |
| wall time, from the log's own outer marks | **%(wall).1f s** (%(wallmin).1f min) |
| `lake`'s summed reported durations | **%(summed).1f s** across %(spans)d spans |
| `END` / `EXIT` lines | **%(nends)d**, **%(nonzero)d non-zero** |
| modules built before the kill | **%(built)d**, every one `Mathlib.*` |
| **modules that failed, by name** | **NONE** |

**BOTH EXITS ARE `3221225786` = `0xC000013A` = `STATUS_CONTROL_C_EXIT`.** That is what a Windows
process reports when a console control event reaches it. **The build was KILLED, not broken**, and
the log names no module that failed to compile. A reader who saw the non-zero exit and wrote *"the
build failed"* would have said something **the log does not support**.

**NOT ONE `Zeta23` MODULE WAS REACHED.** The run spent its whole life cloning and compiling
mathlib. **So the log says nothing whatever about whether the 57 vendored modules compile.**

**COMPONENT 2 — ALL THREE PROFILES `ABSENT`.** `#print axioms` output lines anywhere in the log:
**0**. The probe never ran to completion, so there is no axiom string to read — **not a string that
came out wrong. ABSENT IS NOT OTHER.** **(R82) is neither claimed nor refuted by this act**;
b473's and b480's wording is right again: **VOID FOR WANT OF A RUN.**

**COMPONENT 3 WAS NOT RUN.** The order: *"otherwise print which and STOP before Component 3."*
REGISTRY's `SIDE-explicit-formula` row keeps **`PENDING`**, no profile is written beside it, the
terminal table is not regenerated for a profile move, and **no row cites the kernel** — (R106)(3)
stands untouched. **A stop obeyed is a result**; the alternative was to write three profiles into
REGISTRY that no run produced.

**b495's OWED CELLS ARE PAID.** Its (N3) and its (S2) both named this log's module marks, and its
own order forbade reading it, so both were scored **NOT SCORABLE** and routed here. **%(instants)d
distinct instants across %(marks)d marks** — b480's defect, one precomputed instant stamped on
every mark, would have given **one**. The repair is confirmed **on the population the expectation
named**, not on the mechanism-level control b495 had to substitute. (S2) is answered too, and
answered flatly: **no `Zeta23` module was built at all**, so the `FromPNTPlus` ten were not what
`lake` built earliest, nor was anything else of the kernel's.

**(N1) REFUTED** (2 non-zero exits) · **(N2) REFUTED** (all three ABSENT) · **(N3) HELD**.
**The seat's own: (S1) HELD, (S2) HELD, (S3) REFUTED — and refuted with the sign backwards.** The
seat predicted wall time would greatly exceed `lake`'s summed durations, reasoning from the mathlib
clone; **the summed durations are the larger, by %(gap).1f s**, because **`lake` builds in
parallel** — %(spans)d spans summing %(summed).1f s inside %(wall).1f s of wall clock, about
**%(conc).1fx** concurrency. **A sum of per-job durations is not an elapsed time**, and the order
asked for both numbers precisely because they are not the same number.

**The two files b496's face omitted are declared in this face's write list** —
`terminal_table_run.txt` and `terminal_table_diff.json` — so the post-push suite can pass on its
own terms without any glob being widened after the fact.

Nothing compiled and no `lake` command ran; **this act did not relaunch the build** — a re-run is
another act's to order. Nothing fetched; nothing deposits; nothing at Zenodo written; row U1
unedited; `h2` where the deposit left it; the four lists stay OPEN; K1, K2 and K3 not started.
"""


def main():
    R = json.loads(read(os.path.join(D, 'b497_results.json')))
    with open(OT, 'rb') as fh:
        before = fh.read()
    if HEADING in before.decode('utf-8', 'replace'):
        print('### ALREADY PRESENT -- REFUSING A SECOND RECORD.')
        return 2
    body = (BODY % dict(
        heading=HEADING, bytes=R['bytes'], lines=R['lines'], sha=R['sha256'],
        marks=R['marks'], instants=R['distinct_instants'], wall=R['wall_seconds'],
        wallmin=R['wall_seconds'] / 60.0, summed=R['lake_summed'], spans=R['lake_spans'],
        nends=len(R['ends']), nonzero=R['nonzero_exits'], built=len(R['modules_built']),
        gap=R['lake_summed'] - R['wall_seconds'],
        conc=R['lake_summed'] / R['wall_seconds'])).encode('utf-8')
    with open(OT, 'ab') as fh:
        fh.write(body)
    with open(OT, 'rb') as fh:
        after = fh.read()
    bl = before.decode('utf-8', 'replace').replace(chr(13), '').split(NL)
    al = after.decode('utf-8', 'replace').replace(chr(13), '').split(NL)
    removed = len(bl) - sum(1 for a, b in zip(al, bl) if a == b)
    out = dict(bytes_added=len(after) - len(before), prefix=after.startswith(before),
               lines_removed=removed, headings=after.decode('utf-8', 'replace').count(HEADING),
               before_sha=hashlib.sha256(before).hexdigest(),
               after_sha=hashlib.sha256(after).hexdigest())
    msg = ('OPEN_TRAILS.md : %(bytes_added)d bytes added, prefix %(prefix)s, '
           '%(lines_removed)d lines removed, %(headings)d heading' % out)
    print('  ' + msg)
    json.dump(out, io.open(os.path.join(D, 'b497_trail_notes.json'), 'w',
                           encoding='utf-8', newline=NL), indent=1)
    io.open(os.path.join(D, 'b497_trail_notes.txt'), 'w', encoding='utf-8',
            newline=NL).write(msg + NL)
    return 0 if (out['prefix'] and removed == 0 and out['headings'] == 1) else 1


if __name__ == '__main__':
    sys.exit(main())
