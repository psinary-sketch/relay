# -*- coding: utf-8 -*-
"""b394_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b394_registration_2026-09-09.txt')
SPEC = os.path.join(ROOT, 'data', 'b394_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (E)/(I): NOTHING DEPOSITS."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (E)/(I)."),
    ("platform calls of any kind", 0, 0, "calls", "### section (E)/(G)."),
    ("`.lean` files touched", 0, 0, "files", "### section (E)."),
    ("builds run", 0, 0, "builds",
     "### section (F): naming a repository on the drive is not compiling it."),
    ("kernel branches merged, pushed or created", 0, 0, "branches", "### section (E)."),
    ("terminals written", 0, 0, "terminals", "### section (I)."),
    ("statements proved", 0, 0, "statements", "### section (I)."),
    ("new mathematics", 0, 0, "statements", "### section (I)."),

    ("pre-lock gates the lock reads", 8, 8, "gates", "### section (A)."),
    ("gates whose subject is this face", 4, 4, "gates", "### section (A)."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates", "### section (A)/(G)."),
    ("readings of the order declared in advance on this face", 5, 5, "readings",
     "### section (A): the rule is quoted and not improved; four of fifteen reachable and three "
     "taken; one of the three carries no table; the unpropagated species recurs inside the "
     "batch; and the other six are superseded."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("extract reads left without an anchor", 0, 0, "reads", "### section (A): 13 reads."),

    # ---- COMPONENT 1 -----------------------------------------------------------------------------
    ("census keystones on disk", 15, 15, "keystones", "### section (A)."),
    ("keystones whose terminals the drive can reach", 4, 4, "keystones",
     "### section (A)/(G) BAR 2: `b390`'s rule, quoted, with ### **NOTHING ADDED TO IT.**"),
    ("conditions added to the rule", 0, 0, "conditions",
     "### section (A)/(G) BAR 2: an earlier form demanded a correspondence table -- ### **A "
     "CONDITION `b390` NEVER STATED** -- and it was removed before the lock."),
    ("keystones read whole by this act", 3, 3, "keystones", "### section (B)."),
    ("keystones excluded and named with a reason", 11, 11, "keystones",
     "### section (A)/(G) BAR 3: ### **A SELECTION IS NOT A SILENCE.**"),
    ("keystones set aside with their own reason", 1, 1, "keystones",
     "### section (A): `ADDITIVE_MULTIPLICATIVE_CONSPIRACY`, read whole at `b390`."),
    ("buckets reported per subject", 3, 3, "buckets", "### section (B)/(G) BAR 4."),
    ("buckets suppressed because they were empty", 0, 0, "buckets",
     "### section (B)/(G) BAR 4: `b390`'s rule -- an empty bucket is reported with its count."),
    ("bucketed items quoted from only one side", 0, 0, "items",
     "### section (B)/(G) BAR 4: the record`s line AND the keystone`s line."),
    ("grades read off a document with no correspondence table", 0, 0, "grades",
     "### section (A)/(F): ### **A KEYSTONE WITH NO TABLE IS A KEYSTONE WHOSE GRADE LIMB CANNOT "
     "BE READ**, and the component says so."),

    # ---- COMPONENT 2 -----------------------------------------------------------------------------
    ("citations repaired in place", 2, 2, "citations",
     "### section (C): the two corrected-but-unpropagated citations in `GRH_CASCADE`."),
    ("annotations preserving the pre-repair form", 1, 1, "annotations",
     "### section (C)/(G) BAR 5."),
    ("lines deleted from any document", 0, 0, "lines", "### section (C)/(G) BAR 5."),
    ("strings other than the version changed on a repaired line", 0, 0, "strings",
     "### section (C)/(G) BAR 5."),
    ("correspondence tables written, extended or re-graded", 0, 0, "tables",
     "### section (C)/(E)/(G) BAR 6: ### **WRITING A CORRESPONDENCE TABLE IS AUTHORING, NOT "
     "RECONCILING.**"),
    ("grades moved", 0, 0, "grades", "### section (C)/(E)/(I)."),
    ("claims withdrawn", 0, 0, "claims", "### section (C)/(E)/(I)."),
    ("superseded citations repaired", 0, 0, "citations",
     "### section (C): `b391` ruled them a currency item."),
    ("routed repairs left unnamed", 0, 0, "repairs",
     "### section (C)/(G) BAR 6: every routed repair names the ruling it needs."),

    # ---- COMPONENT 3 -----------------------------------------------------------------------------
    ("keystones reconciled after this act", 4, 4, "keystones",
     "### section (D): `b390`'s one plus this act's three, against the census's sixteen, ### "
     "**NOT ROUNDED UP.**"),
    ("repairs made and repairs routed counted together", 0, 0, "counts",
     "### section (D): they are counted ### **SEPARATELY.**"),
    ("figures estimated rather than measured from a recorded clock", 0, 0, "figures",
     "### section (D)."),
    ("ways this sample is unrepresentative, named", 1, 1, "ways",
     "### section (F)/(G) BAR 8: the three are ### **THE REACHABLE ONES**, which is the "
     "population most likely to be in good order."),

    # ---- THE THREE SPECIES -----------------------------------------------------------------------
    ("species the corpus-wide sweep reports", 3, 3, "species",
     "### section (A)/(G) BAR 7: phantom, superseded, corrected-but-unpropagated."),
    ("species summed into one figure", 0, 0, "figures", "### section (G) BAR 7."),
    ("phantoms found in the three subjects", 0, 0, "phantoms",
     "### section (A): ### **AN ABSENCE WITH A PROVED SEARCH BEHIND IT IS A RESULT.**"),
    ("corrected-but-unpropagated instances found", 2, 2, "instances", "### section (A)/(C)."),
    ("superseded citations reported", 6, 6, "citations", "### section (A)/(C)."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 8, 8, "bars", "### section (G)."),
    ("bars with a stated floor", 8, 8, "bars", "### section (G): `b347`'s rule."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### section (G)."),
    ("must-fail fixtures", 4, 4, "fixtures", "### section (G): BARS 2, 3, 4 and 5."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (G), counted off this face."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "(`b348`, `b373`)."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("arms measuring a different thing on a re-run", 0, 0, "arms",
     "every diff arm measures against the PRE-ACT BLOB (`b352`, `b388`-`b393`)."),
    ("new `relay` tool files", 6, 6, "files", "### section (E): the cap counts FILES (`b382`)."),
    ("files staged by `-A`", 0, 0, "commands", "`b381`."),
    ("`.git/hooks/pre-push` copies deleted", 0, 0, "files", "RULING (R16)."),
    ("archive or outputs files touched", 0, 0, "files", "### section (E)."),
    ("prior acts` gate suites re-run at this act`s close", 0, 0, "suites",
     "### section (E): the order`s own instruction -- this act`s commit moves `b393`'s baseline."),

    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("classes ruled", 0, 0, "rulings", "### section (I)."),
    ("documents reclassified or placed in Tier KC", 0, 0, "documents", "### section (E)/(I)."),
    ("registry rows edited", 0, 0, "rows", "### section (E)/(I)."),
    ("the census edited", 0, 0, "files", "### section (E)/(I)."),
    ("standards edited", 0, 0, "files", "### section (E)/(I)."),
    ("correspondence rows edited", 0, 0, "rows", "### section (E)/(I): rows are APPENDED."),
    ("clusters reshaped", 0, 0, "clusters", "### section (E)/(I)."),
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
    print('b394_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b394_registration_2026-09-09.txt -- b394, THE RECONCILIATION BATCHED"),
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
