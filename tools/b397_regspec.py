# -*- coding: utf-8 -*-
"""b397_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### **AND THE CLAUSES THAT MATTER MOST BOUND A FACE THE ORDER MADE WIDE:** ### one string,
### twenty-four lines, eight exclusions, zero deletions, zero bytes in the next leg's scope.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b397_registration_2026-09-10.txt')
SPEC = os.path.join(ROOT, 'data', 'b397_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (G)/(K): NOTHING DEPOSITS."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (G)/(K)."),
    ("platform calls of any kind", 0, 0, "calls", "### section (G)."),
    ("`.lean` files touched, in any repository", 0, 0, "files", "### section (G)/(K)."),
    ("builds run", 0, 0, "builds",
     "### section (H)/(I) BAR 5: ### **NO BUILD IS RUN TO SETTLE IT.**"),
    ("branches merged", 0, 0, "branches", "### section (C)/(I) BAR 3."),
    ("branches checked out", 0, 0, "branches",
     "### section (C): every read is `git show`, `rev-list` or `ls-tree`."),
    ("branches pushed, fetched or created", 0, 0, "branches", "### section (G)."),
    ("repositories cloned", 0, 0, "repositories", "### section (G)."),
    ("kernel repositories written to", 0, 0, "repositories", "### section (G)."),
    ("rules struck or amended", 0, 0, "rules",
     "### section (D)/(H): the stale instance is ROUTED, and amending is the author`s."),
    ("prior acts` faces, banks or instruments edited", 0, 0, "files", "### section (G)."),
    ("statements proved", 0, 0, "statements", "### section (K)."),
    ("new mathematics", 0, 0, "statements", "### section (K)."),

    ("pre-lock gates the lock reads", 8, 8, "gates", "### section (A)."),
    ("gates whose subject is this face", 4, 4, "gates", "### section (A)."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates", "### section (A)/(I)."),
    ("readings of the order declared in advance on this face", 7, 7, "readings",
     "### section (A): eight of nine landed; the counting trap; the four absent from main; no "
     "printed profile; (F1) not established; the rule`s stale instance; and the board readable."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("extract reads left AMBIGUOUS or ABSENT", 0, 0, "reads",
     "### section (A): `8` reads, `8` ANCHORED."),

    # ---- COMPONENT 1 -----------------------------------------------------------------------------
    ("research branches in the population", 9, 9, "branches",
     "### section (A): from `b395`'s partition, not from a typed roster."),
    ("push branches excluded as mechanical", 2, 2, "branches",
     "### section (A): named, so the classification is visible."),
    ("research branches fully merged into main", 8, 8, "branches", "### section (A)."),
    ("research branches carrying commits main lacks", 1, 1, "branches",
     "### section (A): `SIDE-kernel/derivative-engine`."),
    ("branches whose direction was assumed rather than measured", 0, 0, "branches",
     "### section (A)/(I) BAR 2: ### **BOTH DIRECTIONS COUNTED, `--merged` A THIRD WITNESS.**"),
    ("declarations read on the live branch", 72, 72, "declarations", "### section (A)."),
    ("declarations absent from main", 4, 4, "declarations", "### section (A)."),
    ("declarations absent from main and cited by a keystone", 3, 3, "declarations",
     "### section (A): the disclosure case."),
    ("declarations absent from main and cited by nothing", 1, 1, "declarations",
     "### section (A): `derivGrade`, a `def`."),
    ("printed profiles found on the live ref", 0, 0, "profiles",
     "### section (A)/(I) BAR 5: a `#print axioms` SOURCE script is not a printed profile."),
    ("axiom profiles asserted for the live branch", 0, 0, "profiles",
     "### section (H): every one is `NOT BUILT`."),
    ("unknowns reported as compiled", 0, 0, "unknowns", "### section (I) BAR 5."),
    ("terminals whose citability was tested against the merge base", 0, 0, "terminals",
     "### section (A)/(I) BAR 4: ### **AGAINST `main`, WHERE A READER RESOLVES IT.**"),

    # ---- COMPONENT 2 -----------------------------------------------------------------------------
    ("disclosure rules quoted from the record", 2, 2, "rules",
     "### section (D): `REGISTRY.md:725` and `THE_KEYSTONE_CENSUS.md:233`."),
    ("rows annotated whose terminal is present on main", 0, 0, "rows",
     "### section (D)/(I) BAR 6: ### **A DISCLOSURE OF A CONDITION THAT NO LONGER HOLDS IS A "
     "FALSE STATEMENT IN A STATUS COLUMN.**"),
    ("rows swept and rows repaired reported together as one figure", 0, 0, "figures",
     "### section (D): they are reported ### **APART.**"),
    ("lines deleted from any corpus document", 0, 0, "lines", "### section (D)/(I) BAR 6."),
    ("annotations preserving the pre-edit lines verbatim", 1, 1, "annotations",
     "### section (D): one per edited document."),
    ("rows whose terminal is on no ref, annotated", 0, 0, "rows",
     "### section (D): such a row is ### **ROUTED.**"),
    ("keystone prose rewritten", 0, 0, "documents",
     "### section (H): the rule licenses a STATUS CELL, not a paragraph. ROUTED."),

    # ---- COMPONENT 3 -----------------------------------------------------------------------------
    ("queue items entered with a trigger", 6, 6, "items", "### section (E)."),
    ("queue items entered without a trigger", 0, 0, "items", "### section (E)/(I) BAR 7."),
    ("queue items opened", 0, 0, "items",
     "### section (E): ### **A TRIGGER IS NOT A PLAN AND A QUEUE IS NOT A COMMITMENT.**"),

    # ---- COMPONENT 4 -----------------------------------------------------------------------------
    ("board sources read", 2, 2, "sources",
     "### section (F): the clause anchor and the faces ledger."),
    ("board lines without a file and a line number", 0, 0, "lines", "### section (I) BAR 8."),
    ("new claims made by the board", 0, 0, "claims", "### section (F)."),

    # ---- RULING (R22) ----------------------------------------------------------------------------
    ("rulings recorded", 1, 1, "rulings", "### section (B): `(R22)`."),
    ("instruments swept for their own sake", 0, 0, "instruments",
     "### section (B): `(R22)` parks that lane, and reading for CONTENT is not audit work."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 8, 8, "bars", "### section (I)."),
    ("bars with a stated floor", 8, 8, "bars", "### section (I): `b347`'s rule."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### section (I)."),
    ("must-fail fixtures", 5, 5, "fixtures", "### section (I): BARS 2, 3, 5 and 6."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (I), counted off this face."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "(`b348`, `b373`)."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("arms measuring a different thing on a re-run", 0, 0, "arms",
     "every diff arm measures against the PRE-ACT BLOB (`b352`)."),
    ("new `relay` tool files", 5, 5, "files", "### section (G): the cap counts FILES (`b382`)."),
    ("files staged by `-A`", 0, 0, "commands", "`b381`."),
    ("`.git/hooks/pre-push` copies deleted", 0, 0, "files", "RULING (R16)."),
    ("archive or outputs files touched", 0, 0, "files", "### section (G)."),

    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("classes ruled", 0, 0, "rulings", "### section (K)."),
    ("documents reclassified or placed in Tier KC", 0, 0, "documents", "### section (G)/(K)."),
    ("registry rows edited", 0, 0, "rows", "### section (G)/(K)."),
    ("the census edited", 0, 0, "files", "### section (G)/(K)."),
    ("standards edited", 0, 0, "files", "### section (G)/(K)."),
    ("correspondence tables written or extended", 0, 0, "tables",
     "### section (D): a STATUS CELL is edited; no table is written or extended."),
    ("correspondence rows edited", 0, 0, "rows", "### section (G): rows are APPENDED."),
    ("grades moved", 0, 0, "grades", "### section (K)."),
    ("claims withdrawn", 0, 0, "claims", "### section (K)."),
    ("clusters reshaped", 0, 0, "clusters", "### section (G)/(K)."),
    ("map head notes touched", 0, 0, "notes", "### section (G)."),
    ("lists closed", 0, 0, "lists", "### section (K): the four stay OPEN, with triggers."),
    ("faces promoted", 0, 0, "faces", "### section (K)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (K)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (K)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "### section (K)."),
    ("posture-lock changes", 0, 0, "changes", "### section (K)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (K)."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values", "### section (A)."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3)."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED."),
]


def count_arms(text):
    import re
    return len(set(re.findall(r'\bG-[A-Z0-9]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b397_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
    print('=' * 100)
    print('  counter source : %s' % os.path.basename(CNT.__file__))
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
    measured = dict(ARMS=count_arms(text))
    print()
    print('  ### ### **THE OPEN CLAUSE, MEASURED RATHER THAN TYPED:** ### ARMS %d' % measured['ARMS'])
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f)
                  for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap,
                "demand": (n if (dem is None and c.startswith('artifact counts')) else
                           (cap if dem is None else dem)),
                "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b397_registration_2026-09-10.txt -- b397, THE RECONCILIATION BATCHED"),
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
