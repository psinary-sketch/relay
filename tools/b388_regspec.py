# -*- coding: utf-8 -*-
"""b388_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b388_registration_2026-09-09.txt')
SPEC = os.path.join(ROOT, 'data', 'b388_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (L): nothing deposits."),
    ("deposited artifacts touched", 0, 0, "files", "### section (L)."),
    ("`.lean` files touched", 0, 0, "files", "### section (H)/(L)."),
    ("builds run", 0, 0, "builds", "### section (H)/(L)."),
    ("axiom profiles recomputed", 0, 0, "profiles", "### section (H)/(L)."),
    ("terminals written", 0, 0, "terminals", "### section (L)."),
    ("statements proved", 0, 0, "statements", "### section (L)."),
    ("new mathematics", 0, 0, "statements", "### section (L)."),

    # ---- STEP ZERO AND THE DECLARED READINGS -----------------------------------------------------
    ("pre-lock gates the lock reads", 8, 8, "gates",
     "### section (A): read by b378`s gate run as b388, unmodified."),
    ("gates whose subject is this face", 4, 4, "gates",
     "### section (A): each carrying a sha256 stamp equal to this face."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates", "### section (A)/(J)."),
    ("readings of the order declared in advance on this face", 6, 6, "readings",
     "### section (A): six clusters in the table; the map 97 days old and 85 against the "
     "registry`s newest date that has happened; two destinations and no third; 17 Tier-K "
     "declarers of which the table names 6; the federation resolving whole so (F3) is already "
     "refuted; and the pin check wrong twice before it was right."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("absence claims made without a positive control", 0, 0, "claims", "### section (A)/(C)."),

    # ---- COMPONENT 1: THE MAP AS IT STANDS -------------------------------------------------------
    ("prior cluster tables quoted whole before anything moves", 1, 1, "tables",
     "### section (B)/(J) BAR 2."),
    ("standing sentences of the map quoted with their locations", 3, 3, "sentences",
     "### section (B): the three (R17) names."),
    ("ages asserted rather than measured", 0, 0, "figures",
     "### section (A)/(B): AN AGE MEASURED AGAINST A DATE THAT HAS NOT HAPPENED IS NOT AN AGE."),
    ("forward-looking registry dates used as the comparand", 0, 0, "dates",
     "### section (A): they are NAMED rather than used."),

    # ---- COMPONENT 2: THE TWO EMERGENT CLUSTERS --------------------------------------------------
    ("emergent clusters seated", 2, 2, "clusters",
     "### section (C): theory-space and cross-domain, as (R17) names them."),
    ("members added on this seat`s judgement of subject", 0, 0, "members",
     "### section (C)/(J) BAR 3: A CLUSTER ASSEMBLED FROM A SEAT`S SENSE OF WHAT BELONGS IS A "
     "CLUSTER THE AUTHOR NEVER RULED."),
    ("third destinations seated", 0, 0, "clusters",
     "### section (C): a destination that is neither is REPORTED AND NOT SEATED."),
    ("cluster subjects stated in words other than the registry`s", 0, 0, "subjects",
     "### section (C)."),

    # ---- COMPONENT 3: THE ERA`S OUTPUT -----------------------------------------------------------
    ("keystone-class documents the map`s table does not name", 11, 11, "documents",
     "### section (A) reading (4)/(D): the population, FIXED BEFORE THE COMPONENT RUNS."),
    ("assignments made without printed evidence", 0, 0, "assignments",
     "### section (D)/(J) BAR 4: an assignment with no printed evidence is counted UNASSIGNED."),
    ("documents assigned by filename, directory or title resemblance", 0, 0, "documents",
     "### section (D)/(J) BAR 4."),
    ("unassigned outcomes treated as defects", 0, 0, "outcomes",
     "### section (D)/(I): UNASSIGNED IS A STATE, NOT A DEBT."),

    # ---- COMPONENT 4: THE RE-EVALUATION ----------------------------------------------------------
    ("questions asked of each seated cluster", 4, 4, "questions",
     "### section (E): subject, anchor, shape, federation."),
    ("answers carried by recollection rather than a quotation or a live read", 0, 0, "answers",
     "### section (E)/(J) BAR 6."),
    ("clusters split, merged or renamed by this act", 0, 0, "clusters",
     "### section (E)/(J) BAR 8: THE RESHAPING IS THE AUTHOR`S."),

    # ---- COMPONENT 5: THE REFRESH ----------------------------------------------------------------
    ("rows of the prior cluster table deleted", 0, 0, "rows",
     "### section (F)/(J) BAR 5: the superseded table is QUOTED, NOT REMOVED."),
    ("map sections edited outside 4A`s cluster table", 0, 0, "sections",
     "### section (F)/(H): narrower than (R17)`s own boundary."),
    ("columns written without a date", 0, 0, "columns", "### section (F)."),
    ("pins written without the ref they were read at", 0, 0, "pins", "### section (F)/(J) BAR 6."),

    # ---- COMPONENT 6: THE UNREADABLE ROWS --------------------------------------------------------
    ("unreadable rows named with a cause", 23, 23, "rows",
     "### section (G)/(J) BAR 7: the causes group and the group counts sum to 23."),
    ("rows edited", 0, 0, "rows", "### section (G)/(H)/(L)."),
    ("statuses assigned to an unreadable row", 0, 0, "statuses",
     "### section (G): NAMING A CAUSE IS NOT SUPPLYING A STATUS."),

    # ---- THE BARS AND THE ARMS -------------------------------------------------------------------
    ("exact bars", 8, 8, "bars",
     "### section (J): stamped-gate, quotation, move, evidence, preservation, live-read, cause, "
     "no-reshape."),
    ("multi-arm bars", 0, 0, "bars", "### section (J)."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (J): (R2) is law."),
    ("arms whose side is left undeclared", 0, 0, "arms", "### section (J): b352`s rule."),

    # ---- WHAT MOVES ON DISK ----------------------------------------------------------------------
    ("relay tools created", 6, 6, "files",
     "the extract, the regspec, the reg gate, the component writer, the desk-and-bank writer, and "
     "this act`s gate suite. ### SIX FILES AND SIX ROLES. ### THE LOCK GATE IS b378`S, RUN AS "
     "b388."),
    ("shared utilities created", 0, 0, "files", "### NONE."),
    ("owner instrument files edited", 0, 0, "files", "this act licenses none."),
    ("suites, banks or run files of other acts edited", 0, 0, "files", "### section (L)."),
    ("relay tracked files written outside tools and data", 0, 0, "files", "none."),
    ("TECHNE files written", 0, 0, "files", "none by this act."),
    ("TECHNE modules pushed", 0, 0, "pushes", "### the standing refusal."),
    ("SIDE-effects files written", 0, 0, "files", "none by this act."),
    ("SIDE-global-section files written", 1, 1, "files", "### CORRESPONDENCE.md at the closing."),
    ("PLACE-papers files written", 2, 2, "files",
     "### section (H): SPIRAL_MAP.md section 4A`s cluster table, per (R17); and OPEN_TRAILS.md, "
     "appended. ### NO OTHER CORPUS DOCUMENT IS WRITTEN INTO."),
    ("corpus documents written into other than the map and the trails ledger", 0, 0, "documents",
     "### section (H)."),
    ("new tracking documents created", 0, 0, "documents", "### section (L)."),
    ("faces ledger rows moved", 0, 0, "rows", "none by this act."),
    ("mirror roster rows changed", 0, 0, "rows", "### section (H)/(L)."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("open lists closed", 0, 0, "lists", "### section (L): restated OPEN by name."),
    ("citation-question movements", 0, 0, "movements", "### section (L)."),
    ("clusters opened, ranked or prioritised", 0, 0, "clusters", "### section (L)."),
    ("amendments applied", 0, 0, "amendments", "### section (L)."),
    ("archive files touched, moved, renamed or removed", 0, 0, "files", "### section (H)/(L)."),
    ("hook copies deleted in any repository", 0, 0, "files", "### section (H): (R16) rules."),
    ("pins written into a corpus row", 0, 0, "pins",
     "### section (H): the map`s own columns carry pins; NO REGISTRY ROW IS EDITED."),
    ("classes ruled", 0, 0, "classes", "### section (L)."),
    ("documents reclassified", 0, 0, "documents", "### section (L)."),
    ("class lines written", 0, 0, "lines", "### section (L)."),
    ("grades moved", 0, 0, "grades", "### section (L)."),
    ("standards edited", 0, 0, "files", "### section (L)."),
    ("registry rows edited", 0, 0, "rows", "### section (H)/(L)."),
    ("bars moved", 0, 0, "bars", "### section (L)."),
    ("claims about the mathematics of any named subject", 0, 0, "claims", "### section (L)."),
    ("grades conferred by a seat", 0, 0, "grades", "### section (L)."),
    ("faces promoted", 0, 0, "faces", "### section (L)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (L)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (L)."),
    ("claims about h2, totality, the roster", 0, 0, "claims",
     "### section (L): no claim in either direction."),
    ("posture-lock changes", 0, 0, "changes", "### section (L)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (L): the instrument lane stays parked."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values",
     "### section (A)/(E): every quoted line read at its own line number; every ref read live."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count",
     "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration`s own text by "
     "`b300_regspec.count_predictions`, IMPORTED."),
]

def main(argv):
    print('=' * 100)
    print('b388_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b388_registration_2026-09-09.txt -- b388, THE MAP REFRESHED AND THE UNREADABLE ROWS NAMED",
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
