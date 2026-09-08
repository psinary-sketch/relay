# -*- coding: utf-8 -*-
"""b373_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.** ### Every clause is a forward
### commitment; the spec is emitted BEFORE the registration is locked and before any write of this act.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b373_registration_2026-09-08.txt')
SPEC = os.path.join(ROOT, 'data', 'b373_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (H): nothing deposits."),
    ("deposited artifacts touched", 0, 0, "files",
     "### section (C)/(H): outputs/DEPOSITED-v1.1.2 is FROZEN and a deposited companion edited here no longer matches what was deposited."),
    ("`.lean` files touched", 0, 0, "files", "### section (H)."),
    ("terminals written", 0, 0, "terminals", "### section (H)."),
    ("statements proved", 0, 0, "statements", "### section (H)."),
    ("builds run", 0, 0, "builds", "### section (H)."),
    ("axiom profiles recomputed", 0, 0, "profiles", "### section (H)."),
    ("new mathematics", 0, 0, "statements", "### section (H)."),

    # ---- (R9) --------------------------------------------------------------------------------------
    ("price parts reported separately", 3, 3, "parts",
     "### section (B): one row, the whole set, and the split between tool and judgement."),
    ("pins taken from a current head", 0, 0, "pins",
     "### section (B)/(H): (R9)'s own prohibition, re-measured by a must-fail arm."),
    ("pins written that are not byte-equal to a sha in the writing act's own banked pins record", 0, 0,
     "pins", "### section (F) BAR 1: sourced ONLY from the act that wrote the row."),
    ("rows re-anchored by line number rather than by content", 0, 0, "rows",
     "### section (B): (R2) is law."),
    ("failure reasons collapsed into one", 0, 0, "reasons",
     "### section (B) BAR 5: four named reasons, reported separately, partitioning the unpinned set."),
    ("rows left unpinned without a stated reason", 0, 0, "rows", "### section (F) BAR 5."),
    ("claims that a row is TRUE at the pin this act wrote", 0, 0, "claims",
     "### section (B)/(H): the pin is the ref the writing act was working against, which is not the ref at which the row's claim was true."),
    ("kernels opened to check a row at its new pin", 0, 0, "kernels",
     "### section (H): adding a pin dates a claim; it does not verify one."),
    ("marks written into a row rather than into this act's record", 0, 0, "marks",
     "### section (A): (R8)'s discipline, unreversed by (R9)."),

    # ---- THE SCOPE OF THE EDIT ----------------------------------------------------------------------
    ("archived files edited", 0, 0, "files",
     "### section (C): an archive that changes is not an archive."),
    ("append-only ledger entries edited", 0, 0, "entries",
     "### section (C): FINDINGS.md, ERRATA.md, OPEN_TRAILS.md and FACES_LEDGER.md carry rows already dated by the act that wrote them. ### OPEN_TRAILS.md gains an APPENDED block, which is not an edit to an entry."),
    ("excluded rows left unlisted or uncounted", 0, 0, "rows",
     "### section (C): the exclusion is a report, not a silence."),
    ("new columns added to a table", 0, 0, "columns",
     "### section (C)/(H): an edit whose blast radius exceeds its warrant is not smaller for being tidy."),
    ("new pin conventions invented by this seat", 0, 0, "conventions",
     "### section (C): the shape is one already present in the papers."),
    ("originals edited without a verbatim copy banked first", 0, 0, "originals",
     "### section (F) BAR 3: (R4), preserve by quotation, repair by edit."),
    ("edited files differing from their blob anywhere but at the edited lines", 0, 0, "files",
     "### section (F) BAR 3."),

    # ---- THE STATUS COLUMN ---------------------------------------------------------------------------
    ("grades moved by this seat", 0, 0, "grades",
     "### section (D)/(F) BAR 6: a seat that regrades is a seat that decided what was verified."),
    ("grade tokens in the papers repository differing from their committed blob", 0, 0, "tokens",
     "### section (F) BAR 6."),
    ("declarations re-classified by this act", 0, 0, "declarations",
     "### section (D)/(H): the retired-and-absent set is the record's own, from b367, b368, b369 and b372."),
    ("status-column instances found but not carried to a named carrier", 0, 0, "instances",
     "### section (D): each one listed, the paper or ledger that carries it named."),
    ("consequences acted on rather than routed", 0, 0, "consequences",
     "### section (D): routed to the author."),
    ("completeness claimed for the grade sweep", 0, 0, "claims",
     "### section (D): PREDICATE_ONE_SHAPE -- the shapes matched are printed and no completeness is claimed."),
    ("rows that state their own retirement counted as defective", 0, 0, "rows",
     "### section (D): treating them alike would report a corrected row as a defective one."),

    # ---- THE INSTRUMENT ------------------------------------------------------------------------------
    ("owner instrument files edited", 1, 1, "files",
     "### section (E): tools/b304_hooks.py, licensed by this order and named on the face BEFORE the edit; any other instrument moving is a failure of the run."),
    ("caveats deleted along with the falsehood", 0, 0, "caveats",
     "### section (E): a correction that deletes the caveat is a worse file."),
    ("guards moved without their exerciser following", 0, 0, "guards",
     "### section (E): no guard moves in this act."),

    # ---- THE BARS ------------------------------------------------------------------------------------
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (F): RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars",
     "### section (F): UNPRICED, and said so rather than left blank."),
    ("exact bars", 7, 7, "bars",
     "### section (F): sourcing, no-head, preservation, frozen-surface, unknown-ref, no-regrade, instrument."),
    ("multi-arm bars", 0, 0, "bars", "### section (F): every bar is marked SINGLE-ARM."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (F): (R2) is law."),
    ("arms whose side is left undeclared", 0, 0, "arms",
     "### section (F): b352's rule, and b370's incident (vi)."),

    # ---- WHAT MOVES ON DISK --------------------------------------------------------------------------
    ("relay tools created", 11, 11, "files",
     "the regspec, the extract, the reg gate, the pin locator, the pin writer, the status sweep, the desk sweeper, the trail writer, the bank writer, the correspondence writer and the index writer; plus this act's gate suite."),
    ("shared utilities created", 0, 0, "files", "none."),
    ("suites, banks or run files of other acts edited", 0, 0, "files", "### section (H)."),
    ("relay tracked files written outside tools and data", 0, 0, "files", "none."),
    ("TECHNE files written", 0, 0, "files", "none by this act."),
    ("TECHNE modules pushed", 0, 0, "pushes", "### the standing refusal."),
    ("SIDE-effects files written", 0, 0, "files", "none by this act."),
    ("SIDE-global-section files written", 1, 1, "files",
     "### CORRESPONDENCE.md at the closing, and no other."),
    ("SIDE-kernel files written", 0, 0, "files", "it is not opened at all by this act."),
    ("faces ledger rows moved", 0, 0, "rows", "none by this act."),
    ("mirror roster rows changed", 0, 0, "rows", "none by this act."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("equivalences compiled", 0, 0, "compilations", "### section (H)."),
    ("bars moved", 0, 0, "bars", "### section (H)."),
    ("claims about the mathematics of any named subject", 0, 0, "claims", "### section (H)."),
    ("grades conferred by a seat", 0, 0, "grades", "### section (H)."),
    ("faces promoted", 0, 0, "faces", "### section (H)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (H)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (H)."),
    ("federation-wide surface sweeps opened", 0, 0, "sweeps", "### section (H)."),
    ("leg 2 components begun", 0, 0, "components",
     "### section (H): the hedge audit, the glossary, the bibliography, the count-and-ref sweep and the functional-equation filing belong to b374."),
    ("claims about h2, totality, the roster", 0, 0, "claims",
     "### section (H): the order's own refusal."),
    ("posture-lock changes", 0, 0, "changes", "### section (H)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (H): the instrument lane stays parked."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values",
     "### section (A-PRE): the price measurement and the one verified chain are declared there."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count",
     "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by "
     "`b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b373_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
    print('=' * 100)
    print('  counter source : %s' % os.path.basename(CNT.__file__))
    print('  ITS SELF-TEST, RUN HERE BEFORE IT IS TRUSTED:')
    if not CNT.self_test():
        print('  ### REFUSING TO EMIT A SPEC FROM A COUNTER THAT FAILS ITS OWN FIXTURES.')
        return 2
    text = io.open(REG, encoding='utf-8').read()
    n, hits = CNT.count_predictions(text)
    print()
    print('  registration : %s' % os.path.basename(REG))
    print('  bytes/lines  : %d / %d' % (len(text.encode('utf-8')), len(text.splitlines())))
    print('  ### ARTIFACT-COUNT PREDICTIONS FOUND : %d' % n)
    for ln, txt in hits:
        print('      line %-4d  %s' % (ln, txt))
    clauses = [{"clause": c, "cap": cap,
                "demand": (n if (dem is None and c.startswith('artifact counts')) else
                           (cap if dem is None else dem)),
                "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": "data/b373_registration_2026-09-08.txt -- b373, THE PINS AND THE STATUS "
                            "COLUMN",
            "clauses": clauses}
    d = (json.dumps(spec, indent=1, ensure_ascii=False) + chr(10)).encode('utf-8')
    open(SPEC + '.tmp', 'wb').write(d)
    os.replace(SPEC + '.tmp', SPEC)
    print()
    print('  clauses emitted : %d' % len(clauses))
    nz = [c for c in clauses if c['demand']]
    print('  ### ### **CLAUSES WITH A NON-ZERO DEMAND : %d**' % len(nz))
    for c in nz:
        print('      %-62s demand %-4s cap %s' % (c['clause'][:62], c['demand'], c['cap']))
    print('  written : %s' % os.path.basename(SPEC))
    print('=' * 100)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
