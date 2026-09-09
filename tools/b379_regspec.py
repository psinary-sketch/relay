# -*- coding: utf-8 -*-
"""b379_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b379_registration_2026-09-08.txt')
SPEC = os.path.join(ROOT, 'data', 'b379_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (J): nothing deposits."),
    ("deposited artifacts touched", 0, 0, "files", "### section (J): read and counted, never edited."),
    ("`.lean` files touched", 0, 0, "files", "### section (J)."),
    ("terminals written", 0, 0, "terminals", "### section (J)."),
    ("statements proved", 0, 0, "statements", "### section (J)."),
    ("builds run", 0, 0, "builds", "### section (J)."),
    ("axiom profiles recomputed", 0, 0, "profiles", "### section (J)."),
    ("new mathematics", 0, 0, "statements", "### section (J)."),

    # ---- STEP ZERO: THE LOCK GATE INHERITED ---------------------------------------------------------
    ("pre-lock gates the lock reads", 8, 8, "gates",
     "### section (A): the ferry scan, both censuses, the pins, the registration gate, the term scan, the clause spec and the satisfiability audit."),
    ("gates whose subject is this face", 4, 4, "gates",
     "### section (A): each must carry a sha256 stamp equal to this face."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates", "### section (A)/(H) BAR 1."),
    ("lock-gate tools rebuilt rather than inherited", 0, 0, "files",
     "### section (A): b378's gate takes the act and the face as arguments and this act runs it as b379."),

    # ---- WHICH PART OF THE DRAFT IS TAKEN ------------------------------------------------------------
    ("draft components taken", 3, 3, "components",
     "### section (B): the suspect column re-measured; the survivors classified one step further; the other NOT DETERMINABLE document by hand."),
    ("draft components taken without the reading being declared", 0, 0, "components",
     "### section (B): the fourth is NOT taken and the draft said silence would be read that way."),
    ("archive files confirmed by this act", 0, 0, "files",
     "### section (B)/(J): the 86 stay unconfirmed and no claim is made about them."),

    # ---- ADDITION ONE: THE DIRECTION -----------------------------------------------------------------
    ("directions registered before the run", 3, 3, "directions",
     "### section (C): the corrected B+ population is bounded below; the both-axes quadrant can only grow; A?B- and A-B- can only shrink."),
    ("documents that lose a mark in the re-score", 0, 0, "documents",
     "### section (C)/(H) BAR 2: a widened matcher finds more, never fewer. ### A VIOLATION IS A DEFECT IN THE INSTRUMENT AND IS REPORTED AS ONE."),
    ("quadrant cells printed without their prior value beside them", 0, 0, "cells",
     "### section (C)/(H) BAR 4."),
    ("options recommended when the correction is stated", 0, 0, "options",
     "### section (C)/(H) BAR 8: which options it weakens, WITHOUT RECOMMENDING ANY."),
    ("prior figures restated as anything but a lower bound on the corrected one", 0, 0, "figures",
     "### section (C)."),

    # ---- ADDITION TWO: THE ROW CATEGORIES ------------------------------------------------------------
    ("row categories added to the taxonomy", 3, 3, "categories",
     "### section (D): a library name; a corpus document rather than a terminal; a name on a tag and no branch."),
    ("categories invented where the front door already has a word", 0, 0, "categories",
     "### section (D): README already says manuscript-resident or research-reach, and its words are QUOTED rather than replaced."),
    ("categories trusted without fixtures in both polarities", 0, 0, "categories",
     "### section (D)/(H) BAR 5: recognised when present, AND NOT CLAIMED WHEN ABSENT."),
    ("verdicts returned by the category module", 0, 0, "verdicts",
     "### section (D): it returns a CATEGORY and never a verdict. ### A CATEGORY IS NOT AN EXCUSE."),

    # ---- ADDITION THREE: THE TWO FILINGS -------------------------------------------------------------
    ("filings made about the document outside the tree", 2, 2, "filings",
     "### section (E): the version-and-class drift, and the population question."),
    ("registry rows edited", 0, 0, "rows",
     "### section (E)/(F)/(H) BAR 7: under the corpus's own rule the registry is what the others reconcile TO."),
    ("download-layer files written, moved, renamed or removed", 0, 0, "files", "### section (F)."),
    ("sides of the drift quoted without file and line", 0, 0, "sides", "### section (E)/(H) BAR 6."),
    ("precedence rules asserted rather than quoted from the front door", 0, 0, "rules",
     "### section (E): README calls REGISTRY the single source of truth and the precedence source."),
    ("work opened on the document itself", 0, 0, "documents",
     "### section (E): it is not read for content, not classified, not graded, not moved and not repaired."),

    # ---- THE ABSENCE DISCIPLINE, NOW STANDING --------------------------------------------------------
    ("absence claims made without a positive control", 0, 0, "claims",
     "### section (A)/(H) BAR 3: the standing clause, and b378 paid for it."),
    ("searches whose error exit was read as an answer", 0, 0, "searches",
     "### section (A)/(H) BAR 3: an error exit is not an answer."),

    # ---- THE BARS -----------------------------------------------------------------------------------
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (H): RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars",
     "### section (H): UNPRICED, and said so rather than left blank."),
    ("exact bars", 8, 8, "bars",
     "### section (H): stamped-gate, monotonicity, positive-control, side-by-side, category, quotation, no-write, no-ruling."),
    ("multi-arm bars", 0, 0, "bars", "### section (H): every bar is marked SINGLE-ARM."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (H): (R2) is law."),
    ("arms whose side is left undeclared", 0, 0, "arms", "### section (H): b352's rule."),

    # ---- WHAT MOVES ON DISK -------------------------------------------------------------------------
    ("relay tools created", 11, 11, "files",
     "the row-category module (SHARED), the regspec, the extract, the reg gate, the re-score, the survivors, the hand read, the two filings, the desk sweeper, the bank writer "
     "and this act's gate suite. ### THE LOCK GATE IS b378'S, RUN AS b379, AND IS NOT REBUILT."),
    ("shared utilities created", 1, 1, "files",
     "### the row-category module -- a later checker imports it so it stops reporting a category as an absence."),
    ("owner instrument files edited", 0, 0, "files", "this act licenses none."),
    ("suites, banks or run files of other acts edited", 0, 0, "files", "### section (J)."),
    ("relay tracked files written outside tools and data", 0, 0, "files", "none."),
    ("TECHNE files written", 0, 0, "files", "none by this act."),
    ("TECHNE modules pushed", 0, 0, "pushes", "### the standing refusal."),
    ("SIDE-effects files written", 0, 0, "files", "none by this act."),
    ("SIDE-global-section files written", 1, 1, "files", "### CORRESPONDENCE.md at the closing."),
    ("PLACE-papers files written", 1, 1, "files",
     "### section (F): OPEN_TRAILS.md, appended. ### NO CORPUS DOCUMENT IS WRITTEN INTO AT ALL AND REGISTRY.md IS NOT EDITED."),
    ("new tracking documents created", 0, 0, "documents", "### section (J)."),
    ("faces ledger rows moved", 0, 0, "rows", "none by this act."),
    ("mirror roster rows changed", 0, 0, "rows", "none by this act."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("open lists closed", 0, 0, "lists", "### section (J): restated OPEN by name."),
    ("kernels opened without a positive control on the sweep", 0, 0, "kernels",
     "### section (A)/(H) BAR 3."),
    ("pins written by this act", 0, 0, "pins",
     "### section (F): no corpus document is written into, so no row and no pin is written."),
    ("documents selected by their path rather than by their own declaration", 0, 0, "documents",
     "### section (C): the population comes from b376's banked scores, which read content."),
    ("classes ruled", 0, 0, "classes", "### section (J)."),
    ("documents reclassified", 0, 0, "documents", "### section (J)."),
    ("class lines written", 0, 0, "lines", "### section (C)/(J): no declaration is moved."),
    ("grades moved", 0, 0, "grades", "### section (J)."),
    ("equivalences compiled", 0, 0, "compilations", "### section (J)."),
    ("bars moved", 0, 0, "bars", "### section (J)."),
    ("claims about the mathematics of any named subject", 0, 0, "claims", "### section (J)."),
    ("grades conferred by a seat", 0, 0, "grades", "### section (J)."),
    ("faces promoted", 0, 0, "faces", "### section (J)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (J)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (J)."),
    ("claims about h2, totality, the roster", 0, 0, "claims",
     "### section (J): no claim in either direction."),
    ("posture-lock changes", 0, 0, "changes", "### section (J)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (J): the instrument lane stays parked."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values",
     "### section (A-PRE): Component 1's finding was visible before the lock and is declared there."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count",
     "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by "
     "`b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b379_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b379_registration_2026-09-08.txt -- b379, THE APPARATUS AXIS RE-SCORED",
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
