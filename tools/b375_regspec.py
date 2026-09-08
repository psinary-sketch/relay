# -*- coding: utf-8 -*-
"""b375_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b375_registration_2026-09-08_reissued.txt')
SPEC = os.path.join(ROOT, 'data', 'b375_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (J): nothing deposits."),
    ("deposited artifacts touched", 0, 0, "files",
     "### section (C)/(J): the deposited companions are READ and counted, never edited."),
    ("`.lean` files touched", 0, 0, "files", "### section (J)."),
    ("terminals written", 0, 0, "terminals", "### section (J)."),
    ("statements proved", 0, 0, "statements", "### section (J)."),
    ("builds run", 0, 0, "builds", "### section (J)."),
    ("axiom profiles recomputed", 0, 0, "profiles", "### section (J)."),
    ("new mathematics", 0, 0, "statements", "### section (J)."),

    # ---- THE THREE TESTS ----------------------------------------------------------------------------
    ("tests for KEYSTONE reported side by side", 3, 3, "tests",
     "### section (A-PRE)/(B): the author-ruled taxonomy's Tier K, the order's rubric, and the existing census's own test. ### THREE TESTS, ONE WORD."),
    ("tests reconciled by this seat", 0, 0, "reconciliations",
     "### section (B): where the three disagree, THE DISAGREEMENT IS THE PRODUCT."),
    ("declared classes overwritten", 0, 0, "classes",
     "### section (B)/(J): a declared tier is QUOTED, never overwritten."),
    ("declared classes translated into the order's vocabulary", 0, 0, "translations",
     "### section (B): the order's class is a SEPARATE column, computed from the order's own rubric."),
    ("declarations of NOT PLACED overridden", 0, 0, "declarations",
     "### section (B): a declaration of NOT PLACED is a declaration."),

    # ---- COMPONENT 1 --------------------------------------------------------------------------------
    ("classification words used beyond the four the order ruled", 0, 0, "words",
     "### section (C)/(H) BAR 3: KEYSTONE, SUPPORT, LEDGER, OTHER, and no fifth."),
    ("documents classified from their path rather than their content", 0, 0, "documents",
     "### section (B)/(C): the order says from content and never from a path, twice."),
    ("documents defaulted to SUPPORT when their own text does not decide", 0, 0, "documents",
     "### section (C): defaulting to the larger class would manufacture the census's own answer; such a document is OTHER with the reason stated."),
    ("READ bases without a sentence quoted from the document", 0, 0, "bases",
     "### section (H) BAR 4."),
    ("directory-versus-content disagreements absorbed rather than reported", 0, 0, "disagreements",
     "### section (B)/(C): reported at full prominence and NOT reclassified."),

    # ---- COMPONENT 2 --------------------------------------------------------------------------------
    ("clusters enumerated from directory names alone", 0, 0, "clusters",
     "### section (D): the order forbids it; the sources are the documents themselves and the registry's own rows."),
    ("keystones assigned to a cluster by resemblance", 0, 0, "assignments",
     "### section (D)/(J): an unassignable keystone is UNASSIGNED."),
    ("clusters with no keystone reported as a hole in the sweep", 0, 0, "clusters",
     "### section (D): a cluster with no keystone is a FINDING and is reported as one."),

    # ---- COMPONENT 3 --------------------------------------------------------------------------------
    ("integration columns averaged into one status", 0, 0, "statuses",
     "### section (E): a single INTEGRATION STATUS would hide the only thing the four columns are for."),
    ("cells inferred rather than read", 0, 0, "cells",
     "### section (E)/(J): NOT DETERMINABLE FROM THE DOCUMENT is a full answer."),
    ("column (d) cells carrying a summary rather than an anchor", 0, 0, "cells",
     "### section (H) BAR 5: located by the anchor tool and listed by anchor, not summarized."),
    ("kernels opened to check a citation", 0, 0, "kernels",
     "### section (E)/(J): the column records what the document NAMES; checking is a different act."),

    # ---- COMPONENT 4 --------------------------------------------------------------------------------
    ("owner instrument files edited", 0, 0, "files",
     "### section (F)/(H) BAR 6: b374's audit is used UNMODIFIED; this act licenses no instrument edit."),
    ("instrument stems, grade tokens or tests tuned for this surface", 0, 0, "changes",
     "### section (F)."),
    ("documents pronounced to fail the rubric", 0, 0, "pronouncements",
     "### section (F)/(J): the measurement is the product; the disposition is the author's."),
    ("control populations omitted", 0, 0, "populations",
     "### section (F): the SUPPORT population is measured so the difference between the layers is measured rather than assumed."),
    ("comparisons made on raw totals alone", 0, 0, "comparisons",
     "### section (F): b374's rule -- per thousand sentences as well as raw."),
    ("documents repaired", 0, 0, "documents", "### section (F)/(J): repair nothing."),

    # ---- COMPONENT 5 --------------------------------------------------------------------------------
    ("questions listed that this act could have answered", 0, 0, "questions",
     "### section (G): the list is checked against the act's own components so it cannot become a place to put work not done."),
    ("questions listed without what would answer them", 0, 0, "questions",
     "### section (G): each paired with a read, a ruling, or a kernel check."),

    # ---- THE BARS -----------------------------------------------------------------------------------
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (H): RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars",
     "### section (H): UNPRICED, and said so rather than left blank."),
    ("exact bars", 7, 7, "bars",
     "### section (H): no-write, declaration, four-word, evidence, anchor, unmodified-instrument, open-lists."),
    ("multi-arm bars", 0, 0, "bars", "### section (H): every bar is marked SINGLE-ARM."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (H): (R2) is law."),
    ("arms whose side is left undeclared", 0, 0, "arms", "### section (H): b352's rule."),

    # ---- WHAT MOVES ON DISK -------------------------------------------------------------------------
    ("relay tools created", 10, 10, "files",
     "the regspec, the extract, the reg gate, the population classifier, the cluster enumerator, the "
     "integration reader, the rubric measurement, the desk sweeper, the bank writer and this act's "
     "gate suite; the trail block, the row and the key are written by one of them."),
    ("shared utilities created", 0, 0, "files", "none."),
    ("suites, banks or run files of other acts edited", 0, 0, "files", "### section (J)."),
    ("relay tracked files written outside tools and data", 0, 0, "files", "none."),
    ("TECHNE files written", 0, 0, "files", "none by this act."),
    ("TECHNE modules pushed", 0, 0, "pushes", "### the standing refusal."),
    ("SIDE-effects files written", 0, 0, "files", "none by this act."),
    ("SIDE-global-section files written", 1, 1, "files",
     "### CORRESPONDENCE.md at the closing, and no other."),
    ("PLACE-papers files written", 1, 1, "files",
     "### OPEN_TRAILS.md, appended. ### NO DOCUMENT CLASSIFIED BY THIS ACT IS EDITED."),
    ("new tracking documents created", 0, 0, "documents",
     "### section (J): the census does not create one on its own authority; where it should live is ROUTED."),
    ("faces ledger rows moved", 0, 0, "rows", "none by this act."),
    ("mirror roster rows changed", 0, 0, "rows", "none by this act."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("open lists closed", 0, 0, "lists",
     "### section (H) BAR 7: the four b373 and b374 produced are restated OPEN by name."),
    ("pins added to any row", 0, 0, "pins", "### section (J)."),
    ("grades moved", 0, 0, "grades", "### section (J)."),
    ("equivalences compiled", 0, 0, "compilations", "### section (J)."),
    ("bars moved", 0, 0, "bars", "### section (J)."),
    ("claims about the mathematics of any named subject", 0, 0, "claims", "### section (J)."),
    ("grades conferred by a seat", 0, 0, "grades", "### section (J)."),
    ("faces promoted", 0, 0, "faces", "### section (J)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (J)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (J)."),
    ("claims about h2, totality, the roster", 0, 0, "claims",
     "### section (J): the order says this act makes no claim about h2 in either direction."),
    ("posture-lock changes", 0, 0, "changes", "### section (J)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (J): the instrument lane stays parked."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values",
     "### section (A-PRE): the three tests were located before the lock and are declared there."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count",
     "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by "
     "`b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b375_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b375_registration_2026-09-08_reissued.txt -- b375, THE KEYSTONE AND CLUSTER "
                            "CENSUS",
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
