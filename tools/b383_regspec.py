# -*- coding: utf-8 -*-
"""b383_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b383_registration_2026-09-09.txt')
SPEC = os.path.join(ROOT, 'data', 'b383_satisfiable.json')

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

    # ---- STEP ZERO, THE AMENDMENT, AND THE DECLARED READINGS -----------------------------------------
    ("pre-lock gates the lock reads", 8, 8, "gates",
     "### section (A): read by b378's gate run as b383, unmodified."),
    ("gates whose subject is this face", 4, 4, "gates",
     "### section (A): each carrying a sha256 stamp equal to this face."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates",
     "### section (A)/(H) BAR 1."),
    ("readings of the order declared in advance on this face", 4, 4, "readings",
     "### section (A): what QUOTED means; what AT CONTENT means; that CORRECT is a listed verdict; and that a price is not a proposal."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("absence claims made without a positive control", 0, 0, "claims",
     "### section (A)/(H) BAR 10: the standing clause."),
    ("amendments arriving before this lock", 1, 1, "amendments",
     "### section (A): the author's amendment to Component 4(ii). ### ITS OWN CONDITIONAL DOES NOT FIRE, so it governs this face too, and the arrival order is MEASURED by the run clocks rather than asserted."),
    ("locked faces edited after the lock", 0, 0, "faces",
     "### section (A): nothing below the lock block moves, ever."),

    # ---- COMPONENT 1: THE STANDARD, QUOTED -----------------------------------------------------------
    ("sources read at content", 3, 3, "sources",
     "### section (B): the document-class taxonomy, the registry's phase attribute section, and the keystone correspondence union."),
    ("tiers quoted with their obligation and their citation rule", 4, 4, "tiers",
     "### section (B)/(H) BAR 3: K, C, N and E, each complete."),
    ("obligations or citation rules paraphrased rather than quoted", 0, 0, "paraphrases",
     "### section (A) READING ONE."),
    ("quoted lines that fail to re-read at their own line number", 0, 0, "lines",
     "### section (B)/(H) BAR 2: a quotation that does not re-read is a HARD FAILURE."),
    ("corpus lines read from the mirror archive", 0, 0, "lines",
     "### section (A)/(H) BAR 4: read at the canonical drive, never the mirror."),

    # ---- COMPONENT 2: THE RECONCILIATION -------------------------------------------------------------
    ("acts the reconciliation covers", 8, 8, "acts",
     "### section (C)/(H) BAR 5: b375 through b382, each with what it asked and a verdict."),
    ("acts given a verdict other than DUPLICATED or ADDS", 0, 0, "acts",
     "### section (C)/(H) BAR 5."),
    ("rows that follow a DUPLICATED verdict with a defence of it", 0, 0, "rows",
     "### section (C): WITHOUT DEFENCE is a bar and not a tone."),
    ("verdicts on the navigator's reading", 1, 1, "verdicts",
     "### section (C)/(H) BAR 6: exactly one of CONFIRMED, CORRECTED or REFUTED, with the deciding line quoted."),
    ("readings adopted on whose reading it is rather than on the standard's words", 0, 0, "readings",
     "### section (C): tested and not adopted on his word, which the order states twice."),

    # ---- COMPONENT 3: THE AUTHOR'S MODEL -------------------------------------------------------------
    ("models banked verbatim", 1, 1, "models",
     "### section (D)/(H) BAR 7: sliced whole, both ends verified unique, no line dropped."),
    ("lines dropped from the banked model", 0, 0, "lines",
     "### section (D): a quotation with holes in it is not a quotation."),
    ("documents ruled under the author's model by this act", 0, 0, "documents",
     "### section (D): the model is RECORDED, not applied."),

    # ---- COMPONENT 4: THE AMENDMENTS -----------------------------------------------------------------
    ("amendments drafted and routed", 4, 4, "amendments",
     "### section (E): the furniture obligation, the cluster unit, the tier sweep, and the reviewer-reservoir request."),
    ("amendments applied", 0, 0, "amendments",
     "### section (E)/(H) BAR 8: NO STANDARD IS EDITED BY THIS ACT."),
    ("standards edited", 0, 0, "standards", "### section (E)/(F)/(H) BAR 8."),
    ("rules restated whose text this act could not read", 0, 0, "rules",
     "### section (E): (iv) is a REQUEST for the rule's location or its text. ### A SEAT CANNOT RESTATE A RULE IT CANNOT READ."),
    ("cluster-to-keystone counts printed without the amendment's rule beside them", 0, 0, "counts",
     "### section (E)/(H) BAR 9: a plurality is never read as an anomaly and an absence is never read as a defect."),
    ("clusters described as owed or deficient", 0, 0, "clusters",
     "### section (E)/(J): the six are RESTATED AS NOT-YET-SYNTHESIZED."),
    ("grades moved or acts re-verdicted by the restatement", 0, 0, "changes",
     "### section (E)/(J): the amendment says neither, and neither happens."),
    ("obligations priced without a figure from the record", 0, 0, "obligations",
     "### section (A) READING FOUR: NAMED UNPRICED rather than estimated."),

    # ---- THE BARS -----------------------------------------------------------------------------------
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (H): RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars",
     "### section (H): UNPRICED, and said so rather than left blank."),
    ("exact bars", 10, 10, "bars",
     "### section (H): stamped-gate, quotation, four-tier, canonical-drive, reconciliation, verdict, verbatim, no-edit, cluster-rule, proved-absence."),
    ("multi-arm bars", 0, 0, "bars", "### section (H): every bar is marked SINGLE-ARM."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (H): (R2) is law."),
    ("arms whose side is left undeclared", 0, 0, "arms", "### section (H): b352's rule."),

    # ---- WHAT MOVES ON DISK -------------------------------------------------------------------------
    ("relay tools created", 6, 6, "files",
     "the extract, the regspec, the reg gate, the four-component writer, the desk-and-bank writer, and this leg's gate suite. ### SIX FILES AND SIX ROLES, counted before the description was written. ### THE LOCK GATE IS b378'S, RUN AS b383."),
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
    print('b383_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b383_registration_2026-09-09.txt -- b383, THE STANDARD READ AND THE SEQUENCE RECONCILED",
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
