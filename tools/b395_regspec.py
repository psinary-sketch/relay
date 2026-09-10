# -*- coding: utf-8 -*-
"""b395_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b395_registration_2026-09-09.txt')
SPEC = os.path.join(ROOT, 'data', 'b395_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (G)/(K): NOTHING DEPOSITS."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (G)/(K)."),
    ("platform calls of any kind", 0, 0, "calls", "### section (G)/(D)."),
    ("`.lean` files touched", 0, 0, "files", "### section (G)."),
    ("builds run", 0, 0, "builds",
     "### section (H): naming a repository the drive holds is not building it."),
    ("repositories cloned", 0, 0, "repositories",
     "### section (C)/(G): the route that reaches `0` further is not taken."),
    ("kernel branches fetched, merged, pushed or created", 0, 0, "branches", "### section (G)."),
    ("terminals written", 0, 0, "terminals", "### section (K)."),
    ("statements proved", 0, 0, "statements", "### section (K)."),
    ("new mathematics", 0, 0, "statements", "### section (K)."),

    ("pre-lock gates the lock reads", 8, 8, "gates", "### section (A)."),
    ("gates whose subject is this face", 4, 4, "gates", "### section (A)."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates", "### section (A)/(I)."),
    ("readings of the order declared in advance on this face", 7, 7, "readings",
     "### section (A): the ceiling was an artefact of a predicate; the partition; the four "
     "routes; the federation read live; (R21)`s target row; the two records found by content; "
     "and the two anchorless clusters."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("extract reads left AMBIGUOUS", 0, 0, "reads",
     "### section (A): ### **AMBIGUOUS AND ABSENT ARE TWO ANSWERS AND ARE NOT ONE** (`b393`)."),

    # ---- COMPONENT 1 -----------------------------------------------------------------------------
    ("keystones in the population this act reads", 11, 11, "keystones",
     "### section (B): `b394`'s eleven, taken from its own record and not retyped."),
    ("matchers whose yield is printed per keystone", 3, 3, "matchers",
     "### section (B)/(I) BAR 2: `b381`'s rule, and `b394`'s own shape is one of the three."),
    ("keystones whose yield changed when the matcher was widened", 9, 9, "keystones",
     "### section (A)/(I) BAR 2: ### **A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE.**"),
    ("places in the partition", 2, 2, "places", "### section (B)/(I) BAR 3."),
    ("keystones landing in more than one place", 0, 0, "keystones", "### section (I) BAR 3."),
    ("keystones landing in no place", 0, 0, "keystones", "### section (I) BAR 3."),
    ("keystones readable without a clone", 10, 10, "keystones",
     "### section (A): ### **`(L1)` ASKED FOR FOUR AND THE MEASUREMENT IS TEN.**"),
    ("keystones naming no terminal at all", 1, 1, "keystones", "### section (A): `ENUMERA`."),
    ("keystones placed ON THE DRIVE without a demonstrated local HEAD", 0, 0, "keystones",
     "### section (B)/(I) BAR 4: ### **DEMONSTRATED, NOT ASSERTED.**"),
    ("non-repository tokens counted as terminals", 0, 0, "tokens",
     "### section (B): the residue is hand-read and named apart."),

    # ---- COMPONENT 2 -----------------------------------------------------------------------------
    ("routes priced", 4, 4, "routes",
     "### section (C)/(I) BAR 5: the order`s three, and one it did not pose."),
    ("routes reaching zero", 2, 2, "routes",
     "### section (C): ### **A ROUTE THAT REACHES ZERO IS REPORTED AS REACHING ZERO.**"),
    ("routes padded to avoid reporting a null", 0, 0, "routes", "### section (I) BAR 5."),
    ("routes refuted by the measurement", 1, 1, "routes",
     "### section (C): accepting the ceiling, which was not there to accept."),
    ("routes taken beyond the read this act already ran", 0, 0, "routes", "### section (C)."),

    # ---- COMPONENT 3 -----------------------------------------------------------------------------
    ("deposited records addressed", 2, 2, "records", "### section (D)."),
    ("historical notes drafted", 1, 1, "notes", "### section (D)."),
    ("historical notes written anywhere", 0, 0, "notes",
     "### section (D)/(G): ### **DRAFTED AND NOT WRITTEN.**"),
    ("deposited versions recovered", 0, 0, "versions",
     "### section (H): `19675356`'s is recorded nowhere and the platform is not called."),
    ("answers substituted for the one that was asked", 0, 0, "answers",
     "### **A HALT REPORTED IS WORTH MORE THAN AN ANSWER SUBSTITUTED.**"),

    # ---- ADDITION ONE, RULING (R21) --------------------------------------------------------------
    ("cluster rows re-anchored", 1, 1, "rows", "### section (E): `Simplicity / RH cascade`."),
    ("cluster rows touched other than that one", 0, 0, "rows", "### section (E)/(I) BAR 6."),
    ("members dropped from the re-anchored row", 0, 0, "members",
     "### section (E)/(I) BAR 6: the prior anchor is ### **RETAINED AND NOT DEMOTED.**"),
    ("lines deleted from SPIRAL_MAP.md", 0, 0, "lines", "### section (E)/(I) BAR 6."),
    ("blocks appended preserving the pre-edit row verbatim", 1, 1, "blocks",
     "### section (E): `b388`'s own precedent in that document."),
    ("preserved quotations edited", 0, 0, "quotations",
     "### section (E): line `258` is `b388`'s record and ### **(R4) PRESERVES BY QUOTATION.**"),
    ("clusters reshaped, split, merged or renamed", 0, 0, "clusters", "### section (E)/(F)/(K)."),
    ("anchors invented", 0, 0, "anchors", "### section (F)."),

    # ---- ADDITION TWO, THE LIVE READ -------------------------------------------------------------
    ("federation names the corpus carries", 77, 77, "names",
     "### section (A): found by content across the tree, not from a typed roster."),
    ("names the drive holds as git repositories", 43, 43, "names", "### section (A)."),
    ("names the account resolves unauthenticated", 43, 43, "names", "### section (A)."),
    ("controls run before any figure is read off the survey", 2, 2, "controls",
     "### section (A)/(I) BAR 7: a positive that must resolve and a negative that must not."),
    ("negatives banked without a re-read", 0, 0, "negatives",
     "### section (A)/(I) BAR 7: ### **ONE READ IS NOT A MEASUREMENT.**"),
    ("negatives reported as ABSENT rather than ABSENT-OR-PRIVATE", 0, 0, "negatives",
     "### section (A)/(H)."),

    # ---- ADDITION THREE --------------------------------------------------------------------------
    ("anchorless clusters read from their members` own text", 2, 2, "clusters", "### section (F)."),
    ("syntheses written", 0, 0, "syntheses", "### section (F): a synthesis is authoring."),
    ("verdicts issued on either anchorless cluster", 0, 0, "verdicts",
     "### section (F): ### **DECIDED BY NOBODY**, and routed to the author."),

    # ---- THE OWN CORRECTION ----------------------------------------------------------------------
    ("figures of a prior act corrected by this one", 1, 1, "figures",
     "### section (A)/(I) BAR 8: `b394`'s eleven-unreachable."),
    ("prior locked faces edited", 0, 0, "faces",
     "### section (I) BAR 8: ### **BOTH FIGURES PRINTED; THE LOCKED FACE UNTOUCHED.**"),
    ("defective predicates left unnamed", 0, 0, "predicates", "### section (A)/(I) BAR 8."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 8, 8, "bars", "### section (I)."),
    ("bars with a stated floor", 8, 8, "bars", "### section (I): `b347`'s rule."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### section (I)."),
    ("must-fail fixtures", 5, 5, "fixtures", "### section (I): BARS 2, 3, 4, 6 and 8."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (I), counted off this face."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "(`b348`, `b373`)."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("arms measuring a different thing on a re-run", 0, 0, "arms",
     "every diff arm measures against the PRE-ACT BLOB (`b352`)."),
    ("new `relay` tool files", 6, 6, "files", "### section (G): the cap counts FILES (`b382`)."),
    ("files staged by `-A`", 0, 0, "commands", "`b381`."),
    ("`.git/hooks/pre-push` copies deleted", 0, 0, "files", "RULING (R16)."),
    ("archive or outputs files touched", 0, 0, "files", "### section (G)."),

    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("classes ruled", 0, 0, "rulings", "### section (K)."),
    ("documents reclassified or placed in Tier KC", 0, 0, "documents", "### section (G)/(K)."),
    ("registry rows edited", 0, 0, "rows", "### section (G)/(K)."),
    ("the census edited", 0, 0, "files", "### section (G)/(K)."),
    ("standards edited", 0, 0, "files", "### section (G)/(K)."),
    ("correspondence tables written, extended or re-graded", 0, 0, "tables", "### section (K)."),
    ("correspondence rows edited", 0, 0, "rows", "### section (G)/(K): rows are APPENDED."),
    ("grades moved", 0, 0, "grades", "### section (K)."),
    ("claims withdrawn", 0, 0, "claims", "### section (K)."),
    ("map head notes touched", 0, 0, "notes", "### section (G)."),
    ("lists closed", 0, 0, "lists", "### section (K): the four stay OPEN."),
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
    print('b395_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b395_registration_2026-09-09.txt -- b395, THE RECONCILIATION BATCHED"),
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
