# -*- coding: utf-8 -*-
"""b392_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b392_registration_2026-09-09.txt')
SPEC = os.path.join(ROOT, 'data', 'b392_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (D)/(H): NOTHING DEPOSITS."),
    ("DOIs minted, claimed or edited", 0, 0, "DOIs", "### section (D)."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (D)/(H)."),
    ("platform calls of any kind", 0, 0, "calls",
     "### section (D)/(F) BAR 6: the platform answered nothing on six routes at b389 and is "
     "### **NOT ASKED AGAIN.**"),
    ("`.lean` files touched", 0, 0, "files", "### section (D)."),
    ("builds run", 0, 0, "builds", "### section (D)."),
    ("terminals written", 0, 0, "terminals", "### section (H)."),
    ("statements proved", 0, 0, "statements", "### section (H)."),
    ("new mathematics", 0, 0, "statements", "### section (H)."),

    ("pre-lock gates the lock reads", 8, 8, "gates", "### section (A)."),
    ("gates whose subject is this face", 4, 4, "gates", "### section (A)."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates", "### section (A)/(F)."),
    ("readings of the order declared in advance on this face", 5, 5, "readings",
     "### section (A): the taxonomy`s load-bearing rule is Tier C`s; the failure and the retired "
     "scheme are both in the record; the corpus`s precedence puts deposits in REGISTRY with "
     "README pointing; 16 records known and 3 listed; and (L2) is at risk of refutation."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),

    ("rulings written", 2, 2, "rulings", "### section (B)/(C): (R19) and (R20)."),
    ("amendments made additively", 2, 2, "amendments",
     "### section (B)/(C)/(F) BAR 2: the prior text preserved byte-for-byte."),
    ("prior lines of the taxonomy edited", 0, 0, "lines", "### section (D)/(F) BAR 2."),
    ("registry rows, lineages or deposit figures edited", 0, 0, "rows", "### section (D)/(F) BAR 2."),
    ("deposit note entries edited or removed", 0, 0, "entries", "### section (D)."),
    ("lines removed from the taxonomy, the registry or the readme", 0, 0, "lines",
     "### section (F) BAR 2."),

    ("guards written into the new class", 1, 1, "guards",
     "### section (B)/(F) BAR 3: ### **THIS CLASS CONFERS NO CITATION LICENSE THE TWO TIERS DO "
     "NOT ALREADY CONFER.**"),
    ("failures quoted beside the guard", 2, 2, "quotations",
     "### section (B)/(F) BAR 3: the June 2026 over-claim and the August 2026 retirement."),
    ("documents reclassified into the new class", 0, 0, "documents",
     "### section (B)/(D)/(F) BAR 4: the ruling`s own words."),
    ("class lines written on any document", 0, 0, "lines", "### section (D)/(F) BAR 4."),
    ("candidates for the new class named", 0, 0, "candidates", "### section (F) BAR 4."),

    ("limbs of the deposit rule written verbatim", 3, 3, "limbs", "### section (C)."),
    ("currency obligations stated as a disjunction", 1, 1, "obligations",
     "### section (C): EITHER at a version a citable claim uses OR carrying a historical note."),
    ("files the rule is written into", 1, 1, "files",
     "### section (C)/(F) BAR 5: `REGISTRY.md`, the source of truth."),
    ("files carrying a pointer at the rule", 1, 1, "files",
     "### section (C)/(F) BAR 5: `README.md`, the front door."),
    ("deposited records the corpus knows of", 16, 16, "records", "### section (A)/(C)."),
    ("records the deposit note lists as citable", 3, 3, "records",
     "### section (A)/(C): and ### **THE THREE MAP ONTO THE THREE LIMBS ONE FOR ONE.**"),
    ("unlisted records", 10, 10, "records", "### section (A)/(C)."),
    ("unlisted records given a limb verdict", 10, 10, "records", "### section (C)/(F) BAR 7."),
    ("records convicted by the matcher without a hand read", 0, 0, "records",
     "### section (C)/(F) BAR 7: the elided-DOI artefact is printed with its record."),
    ("census figures taken from the platform", 0, 0, "figures",
     "### section (C)/(F) BAR 6: every figure is the corpus`s own claim about itself, labelled."),
    ("the two failure shapes added into one count", 0, 0, "counts",
     "### section (A)/(F) BAR 8: a deposit line with no current record is not the same defect as "
     "a record with no note."),

    ("bars declared", 8, 8, "bars", "### section (F)."),
    ("bars with a stated floor", 8, 8, "bars", "### section (F): `b347`'s rule."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### section (F)."),
    ("must-fail fixtures", 4, 4, "fixtures", "### section (F): BARS 2, 3, 6 and 7."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (F), counted off this face."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "(`b348`, `b373`)."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("arms measuring a different thing on a re-run", 0, 0, "arms",
     "every diff arm measures against the PRE-ACT BLOB (`b352`, `b388`-`b391`)."),
    ("new `relay` tool files", 6, 6, "files", "### section (D): the cap counts FILES (`b382`)."),
    ("files staged by `-A`", 0, 0, "commands", "`b381`."),
    ("`.git/hooks/pre-push` copies deleted", 0, 0, "files", "RULING (R16)."),
    ("archive or outputs files touched", 0, 0, "files", "### section (D)."),

    ("grades moved", 0, 0, "grades", "### section (D)/(H)."),
    ("claims withdrawn", 0, 0, "claims", "### section (D)/(H)."),
    ("correspondence rows edited", 0, 0, "rows", "### section (D)/(H): rows are APPENDED."),
    ("clusters reshaped", 0, 0, "clusters", "### section (D)/(H)."),
    ("map head notes touched", 0, 0, "notes", "### section (D)."),
    ("lists closed", 0, 0, "lists", "### section (H): the four stay OPEN."),
    ("faces promoted", 0, 0, "faces", "### section (H)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (H)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (H)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "### section (H)."),
    ("posture-lock changes", 0, 0, "changes", "### section (H)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (H)."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("values carried from recollection rather than read", 0, 0, "values", "### section (A)/(C)."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3)."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED."),
]


def count_arms(text):
    import re
    return len(set(re.findall(r'\bG-[A-Z0-9]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b392_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b392_registration_2026-09-09.txt -- b392, THE TWO RULINGS WRITTEN"),
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
