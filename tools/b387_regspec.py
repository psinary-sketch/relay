# -*- coding: utf-8 -*-
"""b387_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b387_registration_2026-09-09.txt')
SPEC = os.path.join(ROOT, 'data', 'b387_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (J): nothing deposits."),
    ("deposited artifacts touched", 0, 0, "files", "### section (J)."),
    ("`.lean` files touched", 0, 0, "files", "### section (F)/(J)."),
    ("builds run", 0, 0, "builds", "### section (F)/(J)."),
    ("axiom profiles recomputed", 0, 0, "profiles",
     "### section (F): the profiles in the rows are READ AS TEXT, NEVER RE-RUN."),
    ("kernels opened", 0, 0, "kernels",
     "### section (G): this act reads what a row SAYS; it does not open a kernel."),
    ("terminals written", 0, 0, "terminals", "### section (J)."),
    ("statements proved", 0, 0, "statements", "### section (J)."),
    ("new mathematics", 0, 0, "statements", "### section (J)."),

    # ---- STEP ZERO AND THE DECLARED READINGS -----------------------------------------------------
    ("pre-lock gates the lock reads", 8, 8, "gates",
     "### section (A): read by b378`s gate run as b387, unmodified."),
    ("gates whose subject is this face", 4, 4, "gates",
     "### section (A): each carrying a sha256 stamp equal to this face."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates",
     "### section (A)/(H) BAR 1."),
    ("readings of the order declared in advance on this face", 6, 6, "readings",
     "### section (A): nine of fourteen carry a table; the predicate was wrong twice before it "
     "was right; the union`s named carrier for MONO is ungraded; ENGINE`s table is a work-order "
     "instrument; the located rows number 162; and the seat`s memory has no prior blob."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("absence claims made without a positive control", 0, 0, "claims",
     "### section (A)/(B): every document with no table is reported WITH ITS NEAR-MISSES."),

    # ---- COMPONENT 1: THE SET --------------------------------------------------------------------
    ("keystones the union names", 14, 14, "documents",
     "### section (B): taken from the union`s own keystone-set line, read by the anchor tool."),
    ("keystones looked for on the canonical drive", 14, 14, "documents",
     "### section (B)/(H) BAR 2: all fourteen, located or reported absent."),
    ("documents selected by a predicate over the corpus rather than named by the union",
     0, 0, "documents", "### section (B): THE SET IS THE RECORD`S AND NOT A PREDICATE`S."),
    ("tables located by heading rather than by shape", 0, 0, "tables",
     "### section (B)/(H) BAR 2: (R2), by content and never by address."),
    ("disagreements between the union`s list and the disk that are reconciled", 0, 0,
     "disagreements",
     "### section (B)/(H) BAR 3: REPORTED AND NOT RECONCILED. ### The union is not corrected."),
    ("correspondence tables edited", 0, 0, "tables", "### section (F)/(J)."),

    # ---- COMPONENT 2: THE COUNT ------------------------------------------------------------------
    ("front-door status vocabulary quotations, at their own line numbers", 5, 5, "quotations",
     "### section (C): THE CATEGORIES ARE THE CORPUS`S AND NOT THIS ACT`S."),
    ("categories invented by this seat that the corpus has no word for", 0, 0, "categories",
     "### section (C)."),
    ("documents whose category counts do not sum to their row count", 0, 0, "documents",
     "### section (C)/(H) BAR 4: A PARTITION THAT DOES NOT SUM IS NOT A PARTITION."),
    ("rows counted INTERFACES without their premise printed", 0, 0, "rows",
     "### section (C)/(H) BAR 5: a row whose premise cannot be named is counted UNREADABLE."),
    ("unreadable rows assigned to a category", 0, 0, "rows",
     "### section (C)/(H) BAR 6: AN UNREADABLE ROW FORCED INTO A CATEGORY IS A FABRICATED COUNT."),
    ("rows edited", 0, 0, "rows", "### section (C)/(F)/(J)."),
    ("statuses corrected", 0, 0, "statuses",
     "### section (C): where a row`s status looks wrong to this seat, THAT IS NOT THIS ACT`S TO SAY."),
    ("grades moved", 0, 0, "grades", "### section (J)."),

    # ---- COMPONENT 3: THE BEARING ----------------------------------------------------------------
    ("answers stated as a count with its scope named", 1, 1, "answers",
     "### section (D): which tables, which documents, which rows."),
    ("standard borderline dispositions quoted at their own line numbers", 3, 3, "dispositions",
     "### section (D): CATALOGOS, UNIVERSALITY, THE_SUBSTRATE."),
    ("options recommended, ranked or preferred", 0, 0, "options",
     "### section (D)/(H) BAR 7: A BEARING THAT LEANS IS A RECOMMENDATION."),
    ("citation-question movements", 0, 0, "movements",
     "### section (D)/(J): RESTATED AS AWAITING THE AUTHOR AND NOT MOVED."),
    ("classes ruled", 0, 0, "classes", "### section (J)."),

    # ---- COMPONENT 4: THE MEMORY -----------------------------------------------------------------
    ("prior blobs of the memory file that exist", 0, 0, "blobs",
     "### section (A) reading (6)/(E): the home repository has NO COMMITS and MEMORY.md is NOT "
     "TRACKED. ### The comparison uses a byte-for-byte artifact and NAMES IT AS ONE."),
    ("shortened hooks whose dropped tail is left unchecked", 0, 0, "hooks",
     "### section (E)/(H) BAR 8: every tail checked against the file its entry points at."),
    ("index pointers that resolve to no file", 0, 0, "pointers",
     "### section (E)/(H) BAR 8: an entry pointing at no file is itself a loss."),
    ("memory entries deleted", 0, 0, "entries", "### section (F): NO ENTRY IS DELETED."),
    ("memory topic files rewritten", 0, 0, "files",
     "### section (F): NO TOPIC FILE IS REWRITTEN. ### A restoration APPENDS."),
    ("comparisons asserted without being printed", 0, 0, "comparisons",
     "### section (E): an assurance without the comparison is the thing this component refuses."),

    # ---- THE BARS AND THE ARMS -------------------------------------------------------------------
    ("exact bars", 8, 8, "bars",
     "### section (H): stamped-gate, set, disagreement, partition, premise, unreadable, "
     "no-recommendation, memory."),
    ("multi-arm bars", 0, 0, "bars", "### section (H)."),
    ("arms of this suite written by address against the living record", 0, 0, "arms",
     "### section (H): (R2) is law."),
    ("arms whose side is left undeclared", 0, 0, "arms", "### section (H): b352`s rule."),
    ("positive arms that read their subject through strip_prose", 0, 0, "arms",
     "### section (H): b386`s defect, made a bar."),

    # ---- WHAT MOVES ON DISK ----------------------------------------------------------------------
    ("relay tools created", 6, 6, "files",
     "the extract, the regspec, the reg gate, the four-component writer, the desk-and-bank "
     "writer, and this act`s gate suite. ### SIX FILES AND SIX ROLES. ### THE LOCK GATE IS "
     "b378`S, RUN AS b387."),
    ("shared utilities created", 0, 0, "files",
     "### NONE. ### This act reads and counts; it builds no instrument for other acts."),
    ("owner instrument files edited", 0, 0, "files", "this act licenses none."),
    ("suites, banks or run files of other acts edited", 0, 0, "files", "### section (J)."),
    ("relay tracked files written outside tools and data", 0, 0, "files", "none."),
    ("TECHNE files written", 0, 0, "files", "none by this act."),
    ("TECHNE modules pushed", 0, 0, "pushes", "### the standing refusal."),
    ("SIDE-effects files written", 0, 0, "files", "none by this act."),
    ("SIDE-global-section files written", 1, 1, "files", "### CORRESPONDENCE.md at the closing."),
    ("PLACE-papers files written", 1, 1, "files",
     "### section (F): OPEN_TRAILS.md, appended. ### NO CORPUS DOCUMENT IS WRITTEN INTO, README, "
     "REGISTRY, THE_LOAD_BEARING_MAP AND THE_DOCUMENT_CLASS_TAXONOMY INCLUDED."),
    ("new tracking documents created", 0, 0, "documents", "### section (J)."),
    ("faces ledger rows moved", 0, 0, "rows", "none by this act."),
    ("mirror roster rows changed", 0, 0, "rows", "### section (F)/(J)."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("open lists closed", 0, 0, "lists", "### section (J): restated OPEN by name."),
    ("clusters opened, ranked or prioritised", 0, 0, "clusters", "### section (J)."),
    ("amendments applied", 0, 0, "amendments", "### section (J): the three stay routed."),
    ("archive files touched, moved, renamed or removed", 0, 0, "files", "### section (F)/(J)."),
    ("hook copies deleted in any repository", 0, 0, "files",
     "### section (F): (R16) rules they stay."),
    ("pins written by this act", 0, 0, "pins", "### section (F)."),
    ("documents reclassified", 0, 0, "documents", "### section (J)."),
    ("class lines written", 0, 0, "lines", "### section (J)."),
    ("standards edited", 0, 0, "files", "### section (J)."),
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
     "### section (A): every quoted line is read out of its own file at its own line number."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count",
     "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration`s own text by "
     "`b300_regspec.count_predictions`, IMPORTED."),
]

def main(argv):
    print('=' * 100)
    print('b387_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b387_registration_2026-09-09.txt -- b387, WHAT THE KEYSTONES' TABLES ACTUALLY CARRY",
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
