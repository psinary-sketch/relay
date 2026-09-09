# -*- coding: utf-8 -*-
"""b393_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b393_registration_2026-09-09.txt')
SPEC = os.path.join(ROOT, 'data', 'b393_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (E)/(I): NOTHING DEPOSITS."),
    ("DOIs minted, claimed or edited", 0, 0, "DOIs", "### section (E)."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (E)/(I)."),
    ("platform calls of any kind", 0, 0, "calls",
     "### section (E)/(G) BAR 8: the platform is ### **NOT CALLED AT ALL.**"),
    ("`.lean` files touched", 0, 0, "files", "### section (E)."),
    ("builds run", 0, 0, "builds", "### section (E)."),
    ("terminals written", 0, 0, "terminals", "### section (I)."),
    ("statements proved", 0, 0, "statements", "### section (I)."),
    ("new mathematics", 0, 0, "statements", "### section (I)."),

    ("pre-lock gates the lock reads", 8, 8, "gates", "### section (A)."),
    ("gates whose subject is this face", 4, 4, "gates", "### section (A)."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates", "### section (A)/(G)."),
    ("readings of the order declared in advance on this face", 6, 6, "readings",
     "### section (A): the anchor question was never asked; the test and its cost; (L1) at risk; "
     "the screen conflated two things and was repaired; both records superseded and one "
     "unaskable; and the record holds one of three limbs."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("extract reads left without an anchor", 0, 0, "reads", "### section (A): 15 reads."),

    # ---- COMPONENT 1 -----------------------------------------------------------------------------
    ("clusters surfaced", 5, 5, "clusters", "### section (B)."),
    ("clusters carried by a quotation from the act that found them", 5, 5, "clusters",
     "### section (B)/(G) BAR 2."),
    ("clusters printed in this act`s closing message", 5, 5, "clusters",
     "### section (B)/(G) BAR 2: ### **A FINDING THAT REACHES ONLY THE BANK IS A FINDING THE "
     "NAVIGATOR HAS NOT SEEN**, which is the whole reason this act exists."),
    ("distinct verdicts the anchor question returns", 4, 4, "verdicts",
     "### section (A)/(G) BAR 3: ANCHOR OVERTAKEN, MEMBERSHIP ONLY, ANCHOR NOT A CENSUS "
     "KEYSTONE, NO ANCHOR NAMED."),
    ("verdicts summed into one figure", 0, 0, "figures",
     "### section (G) BAR 3: ### **THREE OF THE FOUR ARE WAYS OF NOT ANSWERING THE QUESTION AND "
     "ONLY ONE IS AN ANSWER TO IT.**"),
    ("clusters reshaped, split, merged, renamed or re-anchored", 0, 0, "clusters",
     "### section (E)/(G) BAR 4."),

    # ---- COMPONENT 2 -----------------------------------------------------------------------------
    ("records priced", 2, 2, "records", "### section (C)."),
    ("remediations priced per record", 2, 2, "remediations",
     "### section (C)/(G) BAR 5: a historical note, or a new version deposited."),
    ("remediations recommended", 0, 0, "recommendations",
     "### section (C)/(G) BAR 5: ### **THE CHOICE IS THE AUTHOR`S**, and a price is not a "
     "recommendation."),
    ("figures about the records taken from the platform", 0, 0, "figures",
     "### section (C)/(F): the platform has answered nothing since b389 and is not asked."),
    ("versions inferred where the corpus records none", 0, 0, "versions",
     "### section (F): ### **AN UNRECORDED VERSION IS NOT A VERSION THIS ACT CAN INFER.**"),

    # ---- COMPONENT 3 -----------------------------------------------------------------------------
    ("limbs the class`s obligation is split into", 3, 3, "limbs",
     "### section (D)/(G) BAR 6: grade, placement, coverage."),
    ("limbs the record already answers", 1, 1, "limbs",
     "### section (D): `b387`'s 162 rows answer GRADE and nothing else."),
    ("documents placed in `Tier KC`", 0, 0, "documents",
     "### section (D)/(E)/(G) BAR 7: `(R19)`'s own boundary."),
    ("candidates for `Tier KC` named", 0, 0, "candidates", "### section (D)/(G) BAR 7."),
    ("cheap-sweep figures reported as verdicts rather than floors", 0, 0, "figures",
     "### section (D): ### **A HEADING IS NOT A TABLE READ.**"),

    # ---- THE SCOPE BOUNDARY ----------------------------------------------------------------------
    ("keystones reconciled by this act", 0, 0, "keystones",
     "### section (E)/(I): that is `b394`'s, and ### **A LEG DOES NOT REACH INTO THE NEXT LEG`S "
     "SCOPE.**"),
    ("corpus documents edited", 0, 0, "documents",
     "### section (E)/(G) BAR 8, the two ledgers excepted: ### **THIS ACT READS, MEASURES AND "
     "PRICES; IT REPAIRS NOTHING.**"),
    ("bytes written into the standing taxonomy", 0, 0, "bytes", "### section (E)."),
    ("bytes written into the deposit rule", 0, 0, "bytes", "### section (E)."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 8, 8, "bars", "### section (G)."),
    ("bars with a stated floor", 8, 8, "bars", "### section (G): `b347`'s rule."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### section (G)."),
    ("must-fail fixtures", 4, 4, "fixtures", "### section (G): BARS 2, 3, 5 and 6."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (G), counted off this face."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "(`b348`, `b373`)."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("arms measuring a different thing on a re-run", 0, 0, "arms",
     "every diff arm measures against the PRE-ACT BLOB (`b352`, `b388`-`b392`)."),
    ("new `relay` tool files", 6, 6, "files", "### section (E): the cap counts FILES (`b382`)."),
    ("files staged by `-A`", 0, 0, "commands", "`b381`."),
    ("`.git/hooks/pre-push` copies deleted", 0, 0, "files", "RULING (R16)."),
    ("archive or outputs files touched", 0, 0, "files", "### section (E)."),

    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("classes ruled", 0, 0, "rulings", "### section (I)."),
    ("documents reclassified", 0, 0, "documents", "### section (I)."),
    ("grades moved", 0, 0, "grades", "### section (E)/(I)."),
    ("claims withdrawn", 0, 0, "claims", "### section (E)/(I)."),
    ("registry rows edited", 0, 0, "rows", "### section (E)/(I)."),
    ("standards edited", 0, 0, "files", "### section (I)."),
    ("correspondence rows edited", 0, 0, "rows", "### section (E)/(I): rows are APPENDED."),
    ("map head notes touched", 0, 0, "notes", "### section (E)."),
    ("lists closed", 0, 0, "lists", "### section (I): the four stay OPEN."),
    ("faces promoted", 0, 0, "faces", "### section (I)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (I)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (I)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "### section (I)."),
    ("posture-lock changes", 0, 0, "changes", "### section (I)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (I)."),
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
    print('b393_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b393_registration_2026-09-09.txt -- b393, THE FIVE CLUSTERS SURFACED"),
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
