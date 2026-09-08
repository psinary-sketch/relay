# -*- coding: utf-8 -*-
"""b367_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.** ### Every clause is a forward
### commitment; the spec is emitted BEFORE the registration is locked and before any read of the kernel.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b367_registration_2026-09-07.txt')
SPEC = os.path.join(ROOT, 'data', 'b367_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (A)/(I): nothing deposits, in every branch."),
    ("network calls for text", 0, 0, "calls", "### section (I): no source is fetched; the pins' ls-remote is the ritual's own."),
    ("deposited artifacts touched", 0, 0, "files", "### section (I)."),
    ("`.lean` files written", 0, 0, "files", "### section (A) CAP: NO Lean file written."),
    ("terminals replaced", 0, 0, "terminals", "### section (A) CAP."),
    ("statements proved", 0, 0, "statements", "### section (A) CAP."),
    ("builds run", 0, 0, "builds", "### section (F) BAR 3: the axiom profile is READ from a printed record."),
    ("bytes of the exclusion kernel changed", 0, 0, "bytes",
     "### section (I): the kernel is READ and not written, proved byte-for-byte against its own committed state."),
    ("routes attempted", 0, 0, "routes", "### section (D): PRICING IS NOT DOING."),
    ("routes chosen or recommended", 0, 0, "routes",
     "### section (E): the recommendation is the author's; the act presents and does not choose."),
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (F): no frame, seed, transform, quadrature, fit, score or series. ### RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars", "### section (F): UNPRICED, and said so rather than left blank."),
    ("exact bars", 3, 3, "bars", "### section (F): the location bar, the ref bar, the no-build bar."),
    ("multi-arm bars", 0, 0, "bars", "### section (F): every bar is marked SINGLE-ARM."),
    ("verdict branches", 3, 3, "branches", "### section (G): located and priced / partly located / not located."),
    ("branches left unclaimed", 0, 0, "branches", "### section (G): a branch not taken is shown unreachable (b350's rule)."),
    ("hint clauses reported without a status", 0, 0, "clauses",
     "### section (B): each of the four is CONFIRMED, CORRECTED with the correction quoted, or NOT LOCATED."),
    ("statements attributed to the kernel without a located quotation", 0, 0, "statements",
     "### section (F) BAR 1: a terminal that cannot be located is reported NOT LOCATED and is never described from the hint."),
    ("quotations reported without the ref they came from", 0, 0, "quotations",
     "### section (F) BAR 2: a quotation without its ref is a quotation from a repository and not from a state."),
    ("axiom profiles taken from a compile rather than a printed record", 0, 0, "profiles",
     "### section (C): if no printed profile covers them, that is reported as NO PRINTED PROFILE."),
    ("routes priced without what they do NOT buy", 0, 0, "routes",
     "### section (D): a route priced only by its cost is a route priced by its easiest half."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (F): (R2) is law and a `.lean` file's lines move; G-BYCONTENT re-measures it with b366's detector."),
    ("dated arms cured by this act", 0, 0, "arms", "### section (I): the three b366 counted stand where b366 left them."),
    ("acts re-verdicted", 0, 0, "acts", "### section (I)."),
    ("grades conferred by a seat", 0, 0, "grades", "### section (I)."),
    ("faces promoted", 0, 0, "faces", "### section (I)."),
    ("faces ledger blocks appended", 1, 0, "blocks",
     "### the closing: only if a row moves; capped at 1, and a read moves none unless what it locates moves one."),
    ("relay tools created", 6, 6, "files",
     "the regspec, the extract, the locator-and-reader, the pricing writer, the correspondence writer and the index writer; plus this act's suite."),
    ("owner instrument files edited", 0, 0, "files", "none."),
    ("shared utilities created", 0, 0, "files", "none. ### b363's and b366's helpers are USED, not extended."),
    ("suites, banks or run files of other acts edited", 0, 0, "files", "### section (I)."),
    ("TECHNE files written", 0, 0, "files", "none by this act."),
    ("PLACE-papers files written", 2, 1, "files",
     "### the closing: OPEN_TRAILS.md for the scaffold trail; FACES_LEDGER.md only if a row moves. ### THE HOOK AND THE MIRROR ARE OWED."),
    ("mirror roster rows changed", 0, 0, "rows", "none by this act."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("equivalences compiled", 0, 0, "compilations", "### section (I)."),
    ("bars moved", 0, 0, "bars", "### section (I)."),
    ("new mathematics", 0, 0, "statements", "### section (I)."),
    ("claims about the mathematics of either statement", 0, 0, "claims",
     "### section (I): whether a statement is an open problem is decided by READING WHAT IT SAYS, and reporting that reading is not grading it."),
    ("coordinates closed", 0, 0, "coordinates", "### section (I)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (I)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "### section (I): the order's own refusal."),
    ("posture-lock changes", 0, 0, "changes", "### section (I)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (I): the instrument lane stays parked."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values",
     "### section (A-PRE): b361's rule, and what this seat already held is declared rather than concealed."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by `b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b367_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    clauses = [{"clause": c, "cap": cap, "demand": (n if (dem is None and c.startswith('artifact counts')) else
                                                    (cap if dem is None else dem)),
                "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": "data/b367_registration_2026-09-07.txt -- b367, THE SCAFFOLD REPAIR",
            "clauses": clauses}
    d = (json.dumps(spec, indent=1, ensure_ascii=False) + chr(10)).encode('utf-8')
    open(SPEC + '.tmp', 'wb').write(d)
    os.replace(SPEC + '.tmp', SPEC)
    back = json.load(io.open(SPEC, encoding='utf-8'))
    ok = (len(back['clauses']) == len(clauses) and all(str(c.get('from', '')).strip() for c in back['clauses']))
    unsat = [c['clause'] for c in back['clauses'] if c['demand'] > c['cap']]
    nonzero = [c['clause'] for c in back['clauses'] if c['cap'] != 0]
    print()
    print('  spec written and READ BACK : %s  clauses=%d  no empty provenance cell : %s'
          % (os.path.basename(SPEC), len(back['clauses']), ok))
    print('  ### CLAUSES WHOSE DEMAND EXCEEDS THEIR CAP : %d %s' % (len(unsat), unsat if unsat else ''))
    print('  ### ### **CAPS THAT ARE NOT ZERO : %d**' % len(nonzero))
    for c in nonzero:
        print('      %s' % c)
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
