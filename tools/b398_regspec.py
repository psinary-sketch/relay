# -*- coding: utf-8 -*-
"""b398_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b398_registration_2026-09-10.txt')
SPEC = os.path.join(ROOT, 'data', 'b398_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (G)/(K): NOTHING DEPOSITS."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (G)/(K)."),
    ("platform calls of any kind", 0, 0, "calls", "### section (G)."),
    ("numerical computations run", 0, 0, "computations",
     "### section (A)/(I) BAR 2: an act that computes something new has CHANGED THE QUESTION."),
    ("instrument runs", 0, 0, "runs", "### section (G)/(I) BAR 2."),
    ("builds run", 0, 0, "builds", "### section (G)/(I) BAR 2."),
    ("`.lean` files touched", 0, 0, "files", "### section (G)/(K)."),
    ("branches merged, pushed, fetched, created or checked out", 0, 0, "branches",
     "### section (G)."),
    ("repositories cloned", 0, 0, "repositories", "### section (G)."),
    ("rules struck or amended", 0, 0, "rules", "### section (G)/(K)."),
    ("grades moved or conferred", 0, 0, "grades", "### section (G)/(I) BAR 8."),
    ("faces promoted", 0, 0, "faces", "### section (G)/(K)."),
    ("owed rows paid", 0, 0, "rows",
     "### section (E)/(I) BAR 8: a SHARPENING is not a PAYMENT."),
    ("face rows edited in the faces ledger", 0, 0, "rows",
     "### section (G): the OWED PAIR row only."),
    ("prior acts` faces, banks or instruments edited", 0, 0, "files", "### section (G)."),
    ("statements proved", 0, 0, "statements",
     "### section (H): the missing identity is NAMED and NOT ATTEMPTED."),
    ("new mathematics", 0, 0, "statements", "### section (K)."),

    ("pre-lock gates the lock reads", 8, 8, "gates", "### section (A)."),
    ("gates whose subject is this face", 4, 4, "gates", "### section (A)."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates", "### section (A)/(I)."),
    ("readings of the order declared in advance on this face", 7, 7, "readings",
     "### section (A): the place-sets; the seat`s corrected misreading; both halves banked; the "
     "identity the conclusion needs; the family obstruction; the expected verdict; and the "
     "trigger column."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("extract reads left AMBIGUOUS or ABSENT", 0, 0, "reads",
     "### section (A)/(I) BAR 3: `27` reads, `27` ANCHORED."),

    # ---- COMPONENT 1 -----------------------------------------------------------------------------
    ("margins unfolded to their base objects", 2, 2, "margins", "### section (C)."),
    ("place-sets stated before any comparison", 2, 2, "place-sets",
     "### section (A)/(I) BAR 4: `{infinity}` against `{infinity} + {finite}` plus a pole term."),
    ("margins described in the other`s language", 0, 0, "margins", "### section (C)."),
    ("constituents quoted without a file and a line", 0, 0, "constituents",
     "### section (I) BAR 3."),

    # ---- COMPONENT 2 -----------------------------------------------------------------------------
    ("halves of the reading tested", 2, 2, "halves", "### section (D)."),
    ("halves of the reading found BANKED", 2, 2, "halves",
     "### section (A): `K3` at kernel terminals, and `K4` verbatim."),
    ("halves refused rather than tested", 0, 0, "halves",
     "### section (I) BAR 5: a TEST is not a REFUSAL."),
    ("misreadings by this seat, corrected before the lock and printed", 1, 1, "misreadings",
     "### section (A)/(I) BAR 5: `b197`s withdrawal read as covering the premise."),
    ("misreadings buried", 0, 0, "misreadings", "### section (D)."),
    ("verdicts issued", 1, 1, "verdicts",
     "### section (D): one of the order`s three, unsoftened."),
    ("missing statements named and typed", 1, 1, "statements",
     "### section (A)/(I) BAR 6: `(M)`, typed a RESULT."),
    ("missing statements attempted", 0, 0, "statements", "### section (H)."),
    ("exceptions carried rather than dropped", 1, 1, "exceptions",
     "### section (A): `K4`s cutoff window (`b306`)."),

    # ---- COMPONENT 3 -----------------------------------------------------------------------------
    ("branches of the order that fire", 1, 1, "branches",
     "### section (E): neither ASSEMBLES nor DIFFERENT fires, and the act says so."),
    ("owed rows still owed after this act", 1, 1, "rows", "### section (E)/(I) BAR 8."),
    ("refusals quoted beside the sharpening", 1, 1, "refusals", "### section (E)."),

    # ---- COMPONENT 4 -----------------------------------------------------------------------------
    ("next statements named", 1, 1, "statements", "### section (F)."),
    ("next statements attempted", 0, 0, "statements", "### section (F)."),

    # ---- RULING (R23) ----------------------------------------------------------------------------
    ("rulings recorded", 1, 1, "rulings", "### section (B): `(R23)`."),
    ("work-order rows whose trigger reads `none`", 3, 3, "rows", "### section (A)."),
    ("work-order rows left without a trigger or a SHELVED reason", 0, 0, "rows",
     "### section (B)/(I) BAR 7."),
    ("sweeps whose population was not bounded by its own header", 0, 0, "sweeps",
     "### section (A): the discarded shape kept `51` rows and is named with its yield."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 8, 8, "bars", "### section (I)."),
    ("bars with a stated floor", 8, 8, "bars", "### section (I): `b347`s rule."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### section (I): UNPRICED."),
    ("must-fail fixtures", 5, 5, "fixtures", "### section (I): BARS 2, 3, 5, 6 and 7."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (I), counted off this face."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "(`b348`, `b373`)."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("arms taking their population from a name pattern", 0, 0, "arms", "(`b397`)."),
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
    ("keystones edited", 0, 0, "files", "### section (G)."),
    ("correspondence rows edited", 0, 0, "rows", "### section (G): rows are APPENDED."),
    ("claims withdrawn", 0, 0, "claims", "### section (K)."),
    ("clusters reshaped", 0, 0, "clusters", "### section (G)/(K)."),
    ("map head notes touched", 0, 0, "notes", "### section (G)."),
    ("lists closed", 0, 0, "lists", "### section (K): the four stay OPEN."),
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
    print('b398_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b398_registration_2026-09-10.txt -- b398, THE RECONCILIATION BATCHED"),
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
