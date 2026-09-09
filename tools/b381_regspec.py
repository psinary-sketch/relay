# -*- coding: utf-8 -*-
"""b381_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b381_registration_2026-09-09.txt')
SPEC = os.path.join(ROOT, 'data', 'b381_satisfiable.json')

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
     "### section (A): read by b378's gate run as b381, unmodified."),
    ("gates whose subject is this face", 4, 4, "gates",
     "### section (A): each carrying a sha256 stamp equal to this face."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates",
     "### section (A)/(H) BAR 1."),
    ("readings of the order declared in advance on this face", 4, 4, "readings",
     "### section (A): what a head SAYING IT RECORDS means; what CAN FAIL IN BOTH DIRECTIONS means; what SEPARATES means; and that (R14) is recorded and not applied."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("absence claims made without a positive control", 0, 0, "claims",
     "### section (A): the standing clause."),

    # ---- COMPONENT 1: THE CONTROL'S WEAKNESS, AND THE REBUILD ----------------------------------------
    ("weaknesses of the old control asserted rather than measured", 0, 0, "weaknesses",
     "### section (B)/(H) BAR 2: the lowest synthesis reach and the threshold are printed together."),
    ("findings the two facts are reported as", 1, 1, "findings",
     "### section (B): the order says ONE finding, and one is what is written."),
    ("exemplars added, dropped or ranked by this seat's judgement", 0, 0, "exemplars",
     "### section (B)/(H) BAR 3: the rebuild is lexical and positional and every match is taken."),
    ("exemplars carried without a quoted line and a line number", 0, 0, "exemplars",
     "### section (B)/(H) BAR 3: each re-reads out of its own file at its own line."),
    ("documents matching on both sides resolved by preference", 0, 0, "documents",
     "### section (B): a conflict is printed and the document is excluded from BOTH sets."),
    ("readings of the head lexicon reported", 2, 2, "readings",
     "### section (A): the purpose reading this act takes, and the denial reading's yield beside it."),

    # ---- COMPONENT 2: THE UNIT AND THE PREDICATE -----------------------------------------------------
    ("units defined after a score existed", 0, 0, "units",
     "### section (C)/(H) BAR 4: the unit is fixed on this face, before any score."),
    ("kinds of unit the splitter is fixtured on", 3, 3, "kinds",
     "### section (C)/(H) BAR 4: a list item, a table row and a paragraph, plus a heading and a fence."),
    ("predicates built from the answer rather than from the rubric", 0, 0, "predicates",
     "### section (C): the signature is the order's own sentence and is stated before it runs."),
    ("thresholds moved to make the control agree", 0, 0, "thresholds",
     "### section (C): declared here, and a disagreement is reported rather than fitted away."),
    ("source vocabularies invented for this act", 0, 0, "vocabularies",
     "### section (C): a source is b380's, IMPORTED UNCHANGED, so reach and co-location are commensurable."),
    ("limits of the predicate left unstated", 0, 0, "limits",
     "### section (C)/(H) BAR 8: five are named, including the one the order names."),
    ("addresses substituted for subjects without saying so", 0, 0, "substitutions",
     "### section (C): the directory-as-subject substitution is named as a weakness, per (R2)."),

    # ---- COMPONENT 3: THE CONTROL FIRST, AND THE NON-ADOPTION CLAUSE ---------------------------------
    ("corpus-wide numbers printed before the exemplar result", 0, 0, "numbers",
     "### section (D)/(H) BAR 5: a predicate cannot be tuned to a result it has not seen."),
    ("separation checks reported", 2, 2, "checks",
     "### section (A)/(D): the declared threshold, which decides adoption, and the threshold-free check beside it."),
    ("predicates adopted without separating the exemplar set", 0, 0, "predicates",
     "### section (D)/(H) BAR 6: the non-adoption clause binds."),
    ("third features invented after a failure", 0, 0, "features",
     "### section (D): a failure is a result and is reported as one."),
    ("prior scores overwritten", 0, 0, "scores",
     "### section (D)/(H) BAR 7: b380's reach column is kept beside, never replaced."),

    # ---- COMPONENT 4: WHAT THE COLUMNS MEAN ----------------------------------------------------------
    ("statements of what the columns mean", 1, 1, "statements",
     "### section (E): owed whichever way Component 3 goes, so a failure cannot shorten the act."),
    ("classes ruled in any branch", 0, 0, "classes", "### section (E)/(H) BAR 9."),
    ("branches carrying a preference word", 0, 0, "branches", "### section (E)/(H) BAR 9."),

    # ---- (R14) ---------------------------------------------------------------------------------------
    ("rulings recorded verbatim", 1, 1, "rulings",
     "### section (A): (R14), with the download-layer book's status under it restated."),
    ("documents reclassified under (R14)", 0, 0, "documents",
     "### section (A)/(J): the ruling is RECORDED AND NOT APPLIED."),
    ("registry-drift filings closed", 0, 0, "filings",
     "### section (J): it stays open and is the author's, as the ruling itself says."),

    # ---- THE CLOSING ---------------------------------------------------------------------------------
    ("ruling-evidence files updated", 1, 1, "files",
     "### section (F): the file b380 wrote, updated with this act's tables and (R14)."),
    ("new tracking documents created in the corpus", 0, 0, "documents",
     "### section (A)/(F): the standing prohibition since b375, and this act creates none."),

    # ---- THE BARS -----------------------------------------------------------------------------------
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (H): RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars",
     "### section (H): UNPRICED, and said so rather than left blank."),
    ("exact bars", 9, 9, "bars",
     "### section (H): stamped-gate, weakness, no-curation, unit, order, non-adoption, no-overwrite, deafness, no-ruling."),
    ("multi-arm bars", 0, 0, "bars", "### section (H): every bar is marked SINGLE-ARM."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (H): (R2) is law."),
    ("arms whose side is left undeclared", 0, 0, "arms", "### section (H): b352's rule."),

    # ---- WHAT MOVES ON DISK -------------------------------------------------------------------------
    ("relay tools created", 10, 10, "files",
     "the co-location module (SHARED), the regspec, the extract, the reg gate, the exemplar rebuild, the control run, the corpus score, the desk sweeper, the bank writer and this act's gate suite. ### THE LOCK GATE IS b378'S, RUN AS b381."),
    ("shared utilities created", 1, 1, "files",
     "### the co-location module -- a later act splits a document into units and asks which carry two clusters, without rebuilding the splitter."),
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
     "### section (B): every exemplar is selected by a sentence in its own head, quoted."),
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
     "### section (B): b380's reaches are re-read from its banked rows, not recalled."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count",
     "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by "
     "`b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b381_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b381_registration_2026-09-09.txt -- b381, THE CONTROL REBUILT AND CO-LOCATION TESTED",
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
