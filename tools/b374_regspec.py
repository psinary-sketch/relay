# -*- coding: utf-8 -*-
"""b374_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b374_registration_2026-09-08.txt')
SPEC = os.path.join(ROOT, 'data', 'b374_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (H): nothing deposits."),
    ("deposited artifacts touched", 0, 0, "files",
     "### section (D)/(H): the deposited companions are READ, never edited."),
    ("`.lean` files touched", 0, 0, "files", "### section (H)."),
    ("terminals written", 0, 0, "terminals", "### section (H)."),
    ("statements proved", 0, 0, "statements", "### section (E)/(H): a filing is a place in the record, not a result."),
    ("builds run", 0, 0, "builds", "### section (H)."),
    ("axiom profiles recomputed", 0, 0, "profiles", "### section (H)."),
    ("new mathematics", 0, 0, "statements", "### section (E)/(H)."),

    # ---- COMPONENT 1 --------------------------------------------------------------------------------
    ("owner instrument files edited", 0, 0, "files",
     "### section (B)/(F) BAR 1: the hedge audit is run UNMODIFIED; this act licenses no instrument edit."),
    ("instrument stems, grade tokens or tests tuned for this surface", 0, 0, "changes",
     "### section (B): if it fits the corpus badly that is a RESULT, not a reason to adjust it mid-run."),
    ("documents audited that the census does not name and that are not deposited companions", 0, 0,
     "documents", "### section (F) BAR 2: a seat that picked its own keystones would be measuring its own choice."),
    ("census entries dropped rather than reported unresolved", 0, 0, "entries",
     "### section (B)."),
    ("findings reported without a quotation locatable in the file", 0, 0, "findings",
     "### section (F) BAR 3."),
    ("hedges beside a grade token counted together with hedges without one", 0, 0, "counts",
     "### section (B): the instrument's own distinction is kept and the two are counted apart."),
    ("expectations classed IMPORTED rather than UNSOURCED", 0, 0, "classes",
     "### section (B): the predicate cannot see whether an expectation is foreign; the second word would claim what the tool cannot see."),
    ("completeness claimed for the working-note shapes", 0, 0, "claims",
     "### section (B): PREDICATE_ONE_SHAPE -- a shape the sweep does not know will not be found."),
    ("documents graded by this seat", 0, 0, "grades",
     "### section (B)/(H): a hedge is a thing found, not a fault assigned."),
    ("sentences rewritten", 0, 0, "sentences", "### section (H)."),

    # ---- COMPONENT 2 --------------------------------------------------------------------------------
    ("classification words used beyond the four the order ruled", 0, 0, "words",
     "### section (C)/(F) BAR 4: CURRENT, RENAMED, RETIRED, NOT LOCATED, and no fifth."),
    ("external bibliography entries classified against a record they were never in", 0, 0, "entries",
     "### section (C): a sweep that marked every external citation NOT LOCATED would be measuring its own scope."),
    ("entries merged, re-keyed or deleted", 0, 0, "entries",
     "### section (C)/(H): the bibliography's own NAME-IDENTITY LAW forbids it."),
    ("TITLE-UNVERIFIED entries resolved by this seat", 0, 0, "entries", "### section (C)."),
    ("entries rewritten", 0, 0, "entries", "### section (C)/(H): the order's own words."),
    ("glossary objects identified without the identification being reported", 0, 0, "objects",
     "### section (C)/(A-PRE): there is no file named for a glossary; the object is identified by evidence and the identification is reported (b372's precedent)."),
    ("frozen twins edited", 0, 0, "files", "### section (C): the frozen twin is READ and not edited."),

    # ---- COMPONENT 3 --------------------------------------------------------------------------------
    ("figures listed without the ref-window being declared", 0, 0, "figures",
     "### section (D): the window is the SENTENCE and not the document, which is a choice and is declared as one."),
    ("frozen surfaces repaired after being swept", 0, 0, "surfaces",
     "### section (D): they are read, they are counted, and they are not repaired in any leg."),
    ("lists ranked, prioritised or turned into a plan", 0, 0, "lists",
     "### section (D): a list that arrives as a plan has decided something, and this leg decides nothing."),

    # ---- COMPONENT 4 --------------------------------------------------------------------------------
    ("halves of the filing quoted from their own acts", 2, 2, "quotations",
     "### section (E)/(F) BAR 6: the reflection and the self-dual member."),
    ("claims in the filing beyond what its acts state", 0, 0, "claims",
     "### section (E): the order's own words."),
    ("limiting sentences left out of the filing", 0, 0, "sentences",
     "### section (E) BAR 6: the act that derived the reflection also states how far it does not go, and that sentence is quoted IN the filing."),
    ("statements joined that the acts did not join", 0, 0, "statements",
     "### section (E): a construction and a reflection are not one statement because they can be written in one sentence."),
    ("grades conferred, raised or moved", 0, 0, "grades", "### section (E)/(H)."),
    ("bars set by the filing", 0, 0, "bars", "### section (E)."),

    # ---- THE BARS -----------------------------------------------------------------------------------
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (F): RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars",
     "### section (F): UNPRICED, and said so rather than left blank."),
    ("exact bars", 7, 7, "bars",
     "### section (F): unmodified-instrument, scope, quotation, four-word, no-repair, filing, sortie."),
    ("multi-arm bars", 0, 0, "bars", "### section (F): every bar is marked SINGLE-ARM."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (F): (R2) is law."),
    ("arms whose side is left undeclared", 0, 0, "arms", "### section (F): b352's rule."),

    # ---- WHAT MOVES ON DISK -------------------------------------------------------------------------
    ("relay tools created", 11, 11, "files",
     "the regspec, the extract, the reg gate, the hedge sweep, the entry classifier, the figure sweep, "
     "the filing writer, the desk sweeper, the trail writer, the bank writer and this act's gate suite; "
     "plus the correspondence and index writers."),
    ("shared utilities created", 0, 0, "files", "none."),
    ("suites, banks or run files of other acts edited", 0, 0, "files", "### section (H)."),
    ("relay tracked files written outside tools and data", 0, 0, "files", "none."),
    ("TECHNE files written", 0, 0, "files", "none by this act."),
    ("TECHNE modules pushed", 0, 0, "pushes", "### the standing refusal."),
    ("SIDE-effects files written", 0, 0, "files", "none by this act."),
    ("SIDE-global-section files written", 1, 1, "files",
     "### CORRESPONDENCE.md at the closing, and no other."),
    ("PLACE-papers files written", 1, 1, "files",
     "### OPEN_TRAILS.md, appended. ### NO DOCUMENT SWEPT BY THIS LEG IS EDITED."),
    ("faces ledger rows moved", 0, 0, "rows", "none by this act."),
    ("mirror roster rows changed", 0, 0, "rows", "none by this act."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("pins added to any row", 0, 0, "pins", "### section (H): b373's findings are carried, not acted on."),
    ("grades moved", 0, 0, "grades", "### section (H)."),
    ("equivalences compiled", 0, 0, "compilations", "### section (H)."),
    ("bars moved", 0, 0, "bars", "### section (H)."),
    ("claims about the mathematics of any named subject", 0, 0, "claims", "### section (H)."),
    ("faces promoted", 0, 0, "faces", "### section (H)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (H)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (H)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "### section (H)."),
    ("posture-lock changes", 0, 0, "changes", "### section (H)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (H): the instrument lane stays parked."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values",
     "### section (A-PRE): what was located before the lock is declared there."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count",
     "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by "
     "`b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b374_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b374_registration_2026-09-08.txt -- b374, THE DESCRIPTIVE LAYER, "
                            "MEASURED NOT OPINED",
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
