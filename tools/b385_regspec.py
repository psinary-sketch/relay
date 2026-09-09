# -*- coding: utf-8 -*-
"""b385_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b385_registration_2026-09-09.txt')
SPEC = os.path.join(ROOT, 'data', 'b385_satisfiable.json')

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

    # ---- STEP ZERO AND THE DECLARED READINGS -----------------------------------------------------
    ("pre-lock gates the lock reads", 8, 8, "gates",
     "### section (A): read by b378's gate run as b385, unmodified."),
    ("gates whose subject is this face", 4, 4, "gates",
     "### section (A): each carrying a sha256 stamp equal to this face."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates", "### section (A)/(H) BAR 1."),
    ("readings of the order declared in advance on this face", 4, 4, "readings",
     "### section (A): the search ran before the lock and LOCATED the rule; the ANNEX is not a subject cluster; confirming means against the blob and the content; and an item already done is reported as already done."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("absence claims made without a positive control", 0, 0, "claims", "### section (A)."),
    ("prior absence claims this act refutes", 1, 1, "claims",
     "### section (A)/(H) BAR 5: b383's. ### A SEAT REPORTS ITS OWN PRIOR ERROR RATHER THAN LETTING A LATER RESULT QUIETLY REPLACE IT."),

    # ---- COMPONENT 1: THE TRAIL ENTRIES ----------------------------------------------------------
    ("trail entries written", 6, 6, "entries",
     "### section (B)/(H) BAR 2: one per cluster the census counted."),
    ("clusters dropped from the entries", 0, 0, "clusters", "### section (B)/(H) BAR 2."),
    ("entries missing the many-to-many rule", 0, 0, "entries",
     "### section (B)/(H) BAR 2: several keystones, one, or none yet; NOT OWED, NOT DEFICIENT."),
    ("clusters opened, ranked or prioritised", 0, 0, "clusters",
     "### section (B)/(G): a trail entry is not a plan and certainly not a synthesis."),
    ("clusters described as owed or deficient", 0, 0, "clusters", "### section (B)/(J)."),

    # ---- COMPONENT 2: THE RULE -------------------------------------------------------------------
    ("verdicts on the rule", 1, 1, "verdicts",
     "### section (C): LOCATED, and the search's terms and control are printed."),
    ("paraphrase clauses scored", 3, 3, "clauses",
     "### section (C)/(H) BAR 4: each marked ACCURATE, NARROWED or OVER-STATED with the rule's own words beside it."),
    ("clauses given more than one mark or none", 0, 0, "clauses", "### section (H) BAR 4."),
    ("rules restated into any document", 0, 0, "rules",
     "### section (C): the rule is QUOTED, and no standard is edited."),
    ("quoted lines that fail to re-read at their own line number", 0, 0, "lines",
     "### section (H) BAR 3."),

    # ---- COMPONENT 3: THE THREE ------------------------------------------------------------------
    ("items given exactly one disposition", 3, 3, "items",
     "### section (D)/(H) BAR 7: DONE, ROUTED or ALREADY DONE BY THE RECORD. ### NONE PARTLY."),
    ("items partly done", 0, 0, "items", "### section (D)/(H) BAR 7."),
    ("archive files removed, moved or renamed", 0, 0, "files",
     "### section (D)/(F)/(H) BAR 6: the removal is the AUTHOR'S and b378 said so first."),
    ("archive files confirmed without a digest verdict and a content verdict", 0, 0, "files",
     "### section (D)/(H) BAR 6."),
    ("confirmations decided by filename", 0, 0, "confirmations",
     "### section (D)/(H) BAR 6: the filename comparison is PRINTED AND UNUSED."),
    ("guard behaviours changed", 0, 0, "behaviours",
     "### section (D): only the comment that documents the install path is corrected, under (R4)."),
    ("mirror roster rows added where the file is already present", 0, 0, "rows",
     "### section (D): if the roster already carries it, the item is REPORTED DONE BY THE RECORD."),

    # ---- COMPONENT 4: THE ROUTING ----------------------------------------------------------------
    ("citation questions answered", 0, 0, "questions",
     "### section (E)/(H) BAR 8: ROUTED AND NOT ANSWERED."),
    ("options recommended, ranked or preferred", 0, 0, "options",
     "### section (E)/(H) BAR 8: A QUESTION WITH A PREFERRED ANSWER IS AN ANSWER."),
    ("options supplied by this seat rather than by the standard's own practice", 0, 0, "options",
     "### section (E): the standard's three ruled borderlines, and no fourth."),
    ("failures the tiers exist to prevent, quoted beside the options", 1, 1, "quotations",
     "### section (E): the order asks for it by name."),

    # ---- THE BARS -----------------------------------------------------------------------------------
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (H): RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars",
     "### section (H): UNPRICED, and said so rather than left blank."),
    ("exact bars", 8, 8, "bars",
     "### section (H): stamped-gate, entry, quotation, scoring, refutation, confirmation, three-item, no-recommendation."),
    ("multi-arm bars", 0, 0, "bars", "### section (H): every bar is marked SINGLE-ARM."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (H): (R2) is law."),
    ("arms whose side is left undeclared", 0, 0, "arms", "### section (H): b352's rule."),

    # ---- WHAT MOVES ON DISK -------------------------------------------------------------------------
    ("relay tools created", 6, 6, "files",
     "the extract, the regspec, the reg gate, the four-component writer, the desk-and-bank writer, and this act's gate suite. ### SIX FILES AND SIX ROLES, counted before the description was written. ### THE LOCK GATE IS b378'S, RUN AS b385."),
    ("shared utilities created", 0, 0, "files",
     "### NONE. ### This leg reads three standing documents and reconciles eight acts to them; it builds no instrument."),
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
     "### section (B): the three sources are named by the order itself."),
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
     "### section (B): every quoted line is re-read out of its own file at its own line number."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count",
     "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by "
     "`b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b385_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b385_registration_2026-09-09.txt -- b385, THE SIX ON THE TRAILS AND THE RULE FOUND",
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
