# -*- coding: utf-8 -*-
"""b376_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b376_registration_2026-09-08.txt')
SPEC = os.path.join(ROOT, 'data', 'b376_satisfiable.json')

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

    # ---- STEP ZERO ----------------------------------------------------------------------------------
    ("pre-lock gates the lock reads", 7, 7, "gates",
     "### section (A): the ferry scan, both censuses, the pins, the registration gate, the term scan and the satisfiability audit. ### b375 HAD THEM ALL AND READ ONE."),
    ("pre-lock gates left unread by the lock", 0, 0, "gates", "### section (A)/(H) BAR 1."),
    ("lock gates trusted without a two-polarity fixture", 0, 0, "gates",
     "### section (A): a gate that has only ever said yes is not a gate."),
    ("prior locked faces edited", 0, 0, "files",
     "### section (A)/(J): b375's defective first face included."),
    ("claims that the lock gate proves each gate was run against the right thing", 0, 0, "claims",
     "### section (A): it checks that each record CARRIES ITS PASS PHRASE, and says so."),

    # ---- COMPONENT 1 --------------------------------------------------------------------------------
    ("stated definitions quoted verbatim with their location", 1, 1, "definitions",
     "### section (B): the corpus's own prior attempt is quoted, not paraphrased and not outvoted by a count."),
    ("applied tests read from prose rather than from operation", 0, 0, "tests",
     "### section (B): the order's own instruction."),
    ("documents called wrong for a stated/applied difference before their own explanation is sought",
     0, 0, "documents",
     "### section (B): the census may have operationalised what it could and said so."),

    # ---- COMPONENT 2 --------------------------------------------------------------------------------
    ("axes built from quoted words", 2, 2, "axes",
     "### section (C): axis A from the author's rubric as b375's ferry recorded it; axis B from the taxonomy's own Tier K obligation."),
    ("axis predicates without fixtures in both polarities", 0, 0, "predicates",
     "### section (H) BAR 4: each predicate must be able to say no."),
    ("predicates whose deafness is left unstated", 0, 0, "predicates",
     "### section (C): both limits are printed with the counts they qualify."),

    # ---- COMPONENT 3 --------------------------------------------------------------------------------
    ("documents scored on both axes", 349, 349, "documents",
     "### section (D): the whole corpus, independently of the three tests."),
    ("axis scores taking any of the three tests as an input", 0, 0, "scores",
     "### section (D): the three sets are read afterwards for comparison only."),
    ("marks defaulted to the larger side where the text does not decide", 0, 0, "marks",
     "### section (D): NOT DETERMINABLE is a full answer."),
    ("quadrants named evaluatively", 0, 0, "quadrants",
     "### section (D): A+B+, A+B-, A-B+, A-B-. ### A quadrant named THE GOOD ONE would have ruled."),
    ("documents appearing in more than one quadrant", 0, 0, "documents", "### section (H) BAR 5."),

    # ---- COMPONENT 4 --------------------------------------------------------------------------------
    ("tests compared against the axis scores", 3, 3, "tests", "### section (E)."),
    ("differences reported as counts rather than by document", 0, 0, "differences",
     "### section (E)/(H) BAR 6: both directions listed BY DOCUMENT."),
    ("documents called misclassified for appearing in a difference list", 0, 0, "documents",
     "### section (E): it is a document two tests disagree about, not a fault of the document."),

    # ---- COMPONENT 5 --------------------------------------------------------------------------------
    ("populations reported as populations when they are floors", 0, 0, "populations",
     "### section (F): a floor reported as a population is an undercount presented as a census."),
    ("corrected counts replacing the old one silently", 0, 0, "counts",
     "### section (F): both are printed, with the predicate that produced each."),
    ("qualifying documents reported without the sentence that qualifies them", 0, 0, "documents",
     "### section (F)."),

    # ---- COMPONENT 6 --------------------------------------------------------------------------------
    ("options marked preferred, likely, natural or cleanest", 0, 0, "options",
     "### section (G)/(H) BAR 7: those words are a recommendation wearing a description's clothes."),
    ("options stated without what they would oblige", 0, 0, "options",
     "### section (G): an option without its cost is not an option."),
    ("rulings made by this seat", 0, 0, "rulings",
     "### section (G)/(J): the act produces evidence for a ruling and makes none."),

    # ---- THE BARS -----------------------------------------------------------------------------------
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (H): RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars",
     "### section (H): UNPRICED, and said so rather than left blank."),
    ("exact bars", 7, 7, "bars",
     "### section (H): lock-gate, no-write, quotation, polarity, partition, difference-by-document, no-ruling."),
    ("multi-arm bars", 0, 0, "bars", "### section (H): every bar is marked SINGLE-ARM."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (H): (R2) is law."),
    ("arms whose side is left undeclared", 0, 0, "arms", "### section (H): b352's rule."),

    # ---- WHAT MOVES ON DISK -------------------------------------------------------------------------
    ("relay tools created", 10, 10, "files",
     "the regspec, the extract, the reg gate, the lock gate, the prior-attempt reader, the axis scorer, "
     "the test comparison, the desk sweeper, the bank writer and this act's gate suite; the trail block, "
     "the row and the key are written by one of them."),
    ("shared utilities created", 0, 0, "files", "none."),
    ("owner instrument files edited", 0, 0, "files", "this act licenses none."),
    ("suites, banks or run files of other acts edited", 0, 0, "files", "### section (J)."),
    ("relay tracked files written outside tools and data", 0, 0, "files", "none."),
    ("TECHNE files written", 0, 0, "files", "none by this act."),
    ("TECHNE modules pushed", 0, 0, "pushes", "### the standing refusal."),
    ("SIDE-effects files written", 0, 0, "files", "none by this act."),
    ("SIDE-global-section files written", 1, 1, "files", "### CORRESPONDENCE.md at the closing."),
    ("PLACE-papers files written", 1, 1, "files",
     "### OPEN_TRAILS.md, appended. ### NO DOCUMENT SCORED BY THIS ACT IS EDITED."),
    ("new tracking documents created", 0, 0, "documents", "### section (J)."),
    ("faces ledger rows moved", 0, 0, "rows", "none by this act."),
    ("mirror roster rows changed", 0, 0, "rows", "none by this act."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("open lists closed", 0, 0, "lists", "### section (J): restated OPEN by name."),
    ("kernels opened", 0, 0, "kernels", "### section (J): axis B measures the apparatus, not its truth."),
    ("pins resolved", 0, 0, "pins", "### section (J)."),
    ("documents scored from their path", 0, 0, "documents", "### section (J): both axes read content."),
    ("classes ruled", 0, 0, "classes", "### section (J)."),
    ("documents reclassified", 0, 0, "documents", "### section (J)."),
    ("class lines written", 0, 0, "lines", "### section (J)."),
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
    print('b376_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b376_registration_2026-09-08.txt -- b376, THE TWO-AXIS READ",
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
