# -*- coding: utf-8 -*-
"""b370_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b370_registration_2026-09-08.txt')
SPEC = os.path.join(ROOT, 'data', 'b370_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (I): nothing deposits."),
    ("deposited artifacts touched", 0, 0, "files", "### section (I)."),
    ("`.lean` files touched", 0, 0, "files", "### section (I)."),
    ("terminals written", 0, 0, "terminals", "### section (I)."),
    ("statements proved", 0, 0, "statements", "### section (I)."),
    ("builds run", 0, 0, "builds", "### section (I)."),
    ("axiom profiles computed", 0, 0, "profiles", "### section (I)."),
    ("new mathematics", 0, 0, "statements",
     "### section (A)/(D): the order says so before the act could be tempted to."),

    ("grades moved", 0, 0, "grades",
     "### section (C) BAR 2: F-NOGRADE makes the claim mechanical, not a promise."),
    ("acts re-verdicted", 0, 0, "acts",
     "### section (I): a correction is not a re-verdict and the table says which is which."),
    ("grade strings not found verbatim in their own act's bank", 0, 0, "strings",
     "### section (C) BAR 2: or the section is not written."),
    ("obstacle quotations taken from a later act's summary", 0, 0, "quotations",
     "### section (C): b360's rule -- each is located in the bank that ORIGINATED it."),
    ("existing sections of FINDINGS.md edited", 0, 0, "sections",
     "### section (C) BAR 1: the additive bar, true prefix of the file AND of its blob."),
    ("ledger rows moved", 0, 0, "rows", "### section (C)/(I)."),
    ("fold sections appended", 1, 1, "sections", "### section (C): one, purely additive."),
    ("acts folded", 9, 9, "acts",
     "### section (C): the span the counter reads, and the fold is not written if it disagrees."),
    ("spans typed rather than counted", 0, 0, "spans", "### section (A) BAR 3."),

    ("owner instrument files edited", 1, 1, "files",
     "### section (B): the span counter, named on this face BEFORE the edit; any other instrument moving is still a failure."),
    ("tools that write under another act's stem by default", 0, 0, "tools",
     "### section (B): the default path writes nothing at all."),
    ("foreign run pointers changed by a default-mode run", 0, 0, "pointers",
     "### section (B) BAR 4: hashed, run, compared -- proved by a fixture, not promised by a docstring."),
    ("fixtures exercising only the passing polarity", 0, 0, "fixtures",
     "### section (B): the fixture also confirms the emit path DOES write, so an arm that passes because nothing runs is impossible."),
    ("run files already written under the foreign stem, recovered", 0, 0, "files",
     "### section (B): they stay where they are, named as artifacts of a defect and not of the act whose stem they carry."),

    ("statements about the clause's shape reported", 2, 2, "statements",
     "### section (D): the order's own two -- the approximation register, and the archimedean half's grade."),
    ("results about the object produced by this act", 0, 0, "results",
     "### section (D): a fold produces none."),
    ("acts in the span presented as progress on the clause", 0, 0, "acts",
     "### section (D): seven produced no result about the object at all, and the fold says so."),

    ("lore modules minted", 3, 3, "modules",
     "### section (E): the order names them; each filed as its own file."),
    ("lore modules pushed", 0, 0, "pushes",
     "### section (E): committed locally, as every module since b330."),
    ("mechanizable halves left unstated", 0, 0, "halves",
     "### section (E): the durability split is mechanizable in part and the act says which part."),

    ("desk items closed by this act", 0, 0, "items", "### section (F): marks, not verdicts."),
    ("owed items named", 2, 2, "items",
     "### section (F): the count claim, and the hook's non-durability."),
    ("durable hook fixes built", 0, 0, "fixes", "### section (F): priced and not built."),
    ("repositories audited", 0, 0, "repositories",
     "### section (F)/(I): Component 5 is NAMED and PRICED."),
    ("public surfaces read for correctness", 0, 0, "surfaces", "### section (F)/(I)."),
    ("axiom profiles opened for the next arc's first target", 0, 0, "profiles",
     "### section (F): precisely the read that would settle it, and precisely what this act may not do."),

    ("quantities computed about the object", 0, 0, "quantities",
     "### section (G): RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars",
     "### section (G): UNPRICED, and said so rather than left blank."),
    ("exact bars", 4, 4, "bars", "### section (G): additive, no-grade-moved, span, read-only."),
    ("multi-arm bars", 0, 0, "bars", "### section (G): every bar is marked SINGLE-ARM."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (G): (R2) is law."),
    ("arms whose side is left undeclared", 0, 0, "arms", "### section (G): b352's rule."),

    ("relay tools created", 8, 8, "files",
     "the regspec, the extract, the fold emitter, the lore minter, the desk sweeper, the bank writer, the correspondence writer and the index writer; plus this act's suite."),
    ("shared utilities created", 0, 0, "files", "none."),
    ("suites, banks or run files of other acts edited", 0, 0, "files", "### section (I)."),
    ("TECHNE files written", 3, 3, "files", "### section (E)."),
    ("SIDE-effects files written", 0, 0, "files", "none by this act."),
    ("PLACE-papers files written", 2, 1, "files",
     "### FINDINGS.md gains the fold; OPEN_TRAILS.md only if an item's state moves. ### THE HOOK AND THE MIRROR ARE OWED."),
    ("faces ledger rows moved", 0, 0, "rows", "### a fold moves none."),
    ("mirror roster rows changed", 0, 0, "rows", "none by this act."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("equivalences compiled", 0, 0, "compilations", "### section (I)."),
    ("bars moved", 0, 0, "bars", "### section (I)."),
    ("claims about the mathematics of any named subject", 0, 0, "claims", "### section (I)."),
    ("grades conferred by a seat", 0, 0, "grades", "### section (I)."),
    ("faces promoted", 0, 0, "faces", "### section (I)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (I)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (I)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "### section (I): the order's own refusal."),
    ("posture-lock changes", 0, 0, "changes", "### section (I)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (I): the instrument lane stays parked."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values", "### section (A-PRE)."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count",
     "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by `b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b370_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b370_registration_2026-09-08.txt -- b370, THE FOLD, b361 THROUGH b369",
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
