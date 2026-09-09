# -*- coding: utf-8 -*-
"""b380_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b380_registration_2026-09-08.txt')
SPEC = os.path.join(ROOT, 'data', 'b380_satisfiable.json')

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

    # ---- STEP ZERO AND THE DECLARED READINGS ---------------------------------------------------------
    ("pre-lock gates the lock reads", 8, 8, "gates",
     "### section (A): read by b378's gate run as b380, unmodified."),
    ("gates whose subject is this face", 4, 4, "gates",
     "### section (A): each carrying a sha256 stamp equal to this face."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates", "### section (A)/(H) BAR 1."),
    ("readings of the order declared in advance on this face", 3, 3, "readings",
     "### section (A): what THE SEVEN THAT DECLARE means; where THE RULING'S EVIDENCE FILE goes; and that Component 4's second branch is not a ruling."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("absence claims made without a positive control", 0, 0, "claims",
     "### section (A): the standing clause."),

    # ---- COMPONENT 1: THE PREMISE --------------------------------------------------------------------
    ("premises assumed rather than measured", 0, 0, "premises",
     "### section (B)/(H) BAR 2: the role distribution is printed BEFORE the new method runs."),
    ("statement-based readings reported", 2, 2, "readings",
     "### section (B): b376's strict and broad, because the broad one was run and never adopted."),

    # ---- COMPONENT 2: THE STRUCTURAL PREDICATE -------------------------------------------------------
    ("predicates built from the answer rather than from the rubric", 0, 0, "predicates",
     "### section (C): the rule is derived from the rubric's own sentence and stated before it runs."),
    ("thresholds moved to make the control agree", 0, 0, "thresholds",
     "### section (C): THE THRESHOLD IS A CHOICE AND IT IS DECLARED, NOT DISCOVERED. ### A disagreement is reported, not fitted away."),
    ("polarities the predicate is fixtured in", 3, 3, "polarities",
     "### section (C)/(H) BAR 4: a known synthesiser, a known gatherer, and a document drawing on nothing."),
    ("limits of the predicate left unstated", 0, 0, "limits",
     "### section (C)/(H) BAR 7: four are named, including that the directory stands in for the subject."),
    ("addresses substituted for subjects without saying so", 0, 0, "substitutions",
     "### section (C): the directory-as-subject substitution is named as a weakness, per (R2)."),

    # ---- COMPONENT 3: THE RE-SCORE -------------------------------------------------------------------
    ("prior scores overwritten", 0, 0, "scores",
     "### section (D)/(H) BAR 5: the statement-based score is kept beside the structural one."),
    ("documents carrying fewer than both scores", 0, 0, "documents", "### section (D)/(H) BAR 5."),
    ("controls run against the declarers", 1, 1, "controls",
     "### section (D)/(H) BAR 3: the agreement is the predicate's OWN control and is reported FIRST."),
    ("disagreements on the control reported as defects in the documents", 0, 0, "disagreements",
     "### section (D): a disagreement there is a defect in the PREDICATE, at full prominence."),
    ("monotonicity bars claimed for this act", 0, 0, "bars",
     "### section (D): this is a DIFFERENT method, not a wider one, so a document may move either way and NO monotonicity bar applies."),
    ("quadrant cells printed without both versions beside them", 0, 0, "cells",
     "### section (D)/(H) BAR 6."),

    # ---- COMPONENT 4: THE VERDICT --------------------------------------------------------------------
    ("verdicts on the method", 1, 1, "verdicts",
     "### section (E): one of three, chosen by the printed tables."),
    ("classes ruled in any branch", 0, 0, "classes",
     "### section (E)/(H) BAR 8: a method that works is not a ruling either."),
    ("branches carrying a preference word", 0, 0, "branches", "### section (E)/(H) BAR 8."),

    # ---- THE CLOSING ---------------------------------------------------------------------------------
    ("ruling-evidence files written", 1, 1, "files",
     "### section (A)/(F): consolidated IN THE RELAY BANK, because none existed."),
    ("new tracking documents created in the corpus", 0, 0, "documents",
     "### section (A)/(F): the standing prohibition since b375, and this act creates none."),

    # ---- THE BARS -----------------------------------------------------------------------------------
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (H): RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars",
     "### section (H): UNPRICED, and said so rather than left blank."),
    ("exact bars", 8, 8, "bars",
     "### section (H): stamped-gate, premise, control, polarity, no-overwrite, side-by-side, deafness, no-ruling."),
    ("multi-arm bars", 0, 0, "bars", "### section (H): every bar is marked SINGLE-ARM."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (H): (R2) is law."),
    ("arms whose side is left undeclared", 0, 0, "arms", "### section (H): b352's rule."),

    # ---- WHAT MOVES ON DISK -------------------------------------------------------------------------
    ("relay tools created", 9, 9, "files",
     "the role-structure module (SHARED), the regspec, the extract, the reg gate, the re-score, the verdict, the desk sweeper, the bank writer and this act's gate suite. ### THE LOCK GATE IS b378'S, RUN AS b380."),
    ("shared utilities created", 1, 1, "files",
     "### the role-structure module -- a later act reads role from what a document draws on, without rebuilding the predicate."),
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
    print('b380_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b380_registration_2026-09-08.txt -- b380, THE ROLE AXIS SCORED STRUCTURALLY",
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
