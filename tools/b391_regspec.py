# -*- coding: utf-8 -*-
"""b391_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b391_registration_2026-09-09.txt')
SPEC = os.path.join(ROOT, 'data', 'b391_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (I): nothing deposits."),
    ("deposited artifacts touched", 0, 0, "files", "### section (I)."),
    ("`.lean` files touched", 0, 0, "files", "### section (E)/(I)."),
    ("builds run", 0, 0, "builds", "### section (E)/(I)."),
    ("axiom profiles recomputed", 0, 0, "profiles", "### section (E)/(I)."),
    ("terminals written", 0, 0, "terminals", "### section (I)."),
    ("statements proved", 0, 0, "statements", "### section (I)."),
    ("new mathematics", 0, 0, "statements", "### section (I)."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (E)/(I)."),
    ("platform calls of any kind", 0, 0, "calls",
     "### section (E): this act carries ### **NO WRITE PATH TO THE PLATFORM AT ALL** ### and does "
     "not call it."),

    # ---- STEP ZERO AND THE DECLARED READINGS -----------------------------------------------------
    ("pre-lock gates the lock reads", 8, 8, "gates",
     "### section (A): read by b378`s gate run as b391, unmodified."),
    ("gates whose subject is this face", 4, 4, "gates", "### section (A)."),
    ("face-subject gates accepted without a matching stamp", 0, 0, "gates", "### section (A)/(G)."),
    ("readings of the order declared in advance on this face", 5, 5, "readings",
     "### section (A): the count is 32/13 and not 28/11; the phantom has an origin the corpus "
     "recorded itself; only 24 of the 32 are citations; the widened screen repairs nothing; and "
     "the five clusters are in b390`s bank."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("extract reads left without an anchor", 0, 0, "reads", "### section (A): 15 reads."),

    # ---- COMPONENT 0 -----------------------------------------------------------------------------
    ("clusters reported", 5, 5, "clusters", "### section (B)."),
    ("clusters carried by a quotation", 5, 5, "clusters", "### section (B)."),
    ("clusters reshaped, split, merged, renamed or re-anchored", 0, 0, "clusters",
     "### section (B)/(G) BAR 7: ### **THE RESHAPING IS THE AUTHOR`S AND THIS IS THE READ THAT "
     "PRECEDES IT.**"),

    # ---- COMPONENT 1 -----------------------------------------------------------------------------
    ("phantom instances enumerated from the files", 32, 32, "instances", "### section (A)/(C)."),
    ("documents carrying them", 13, 13, "documents", "### section (A)/(C)."),
    ("counts carried forward from b390 as this act`s own", 0, 0, "counts",
     "### section (A)/(G) BAR 2: b390`s 28/11 appears ### **ONLY AS THE FIGURE BEING "
     "CORRECTED.**"),
    ("instances classified before any edit", 32, 32, "instances", "### section (C)."),
    ("citations repaired", 24, 24, "citations",
     "### section (C)/(G) BAR 4: `v1.2` -> `v0.5.4`, and nothing else on the line."),
    ("provenance entries edited", 0, 0, "entries",
     "### section (C)/(E)/(G) BAR 3: the order`s first exclusion -- ### **THEY STATE WHAT WAS "
     "CITED AT THE TIME.**"),
    ("preserved verbatim block lines edited", 0, 0, "lines",
     "### section (C)/(E)/(G) BAR 3: the order`s second exclusion."),
    ("ledger lines reporting the defect edited", 0, 0, "lines",
     "### section (C)/(E)/(G) BAR 3: this act`s own third exclusion -- ### **REPAIRING A REPORT "
     "OF AN ERROR ERASES THE REPORT** (`b348`)."),
    ("instances excluded, each named with its reason", 8, 8, "instances", "### section (C)."),
    ("strings other than the version changed on a repaired line", 0, 0, "strings",
     "### section (C)/(G) BAR 4: ### **A PHANTOM-VERSION PASS THAT ALSO TIDIES PROSE HAS STOPPED "
     "BEING A PHANTOM-VERSION PASS.**"),
    ("lines deleted from any document", 0, 0, "lines", "### section (C)/(G) BAR 4."),
    ("the replacement version taken on trust rather than read", 0, 0, "versions",
     "### section (C): the paper`s own head and the registry`s row, ### **BOTH READ AT THEIR OWN "
     "LINES.**"),
    ("origins located and quoted with a date", 1, 1, "origins",
     "### section (A)/(C): ### **A DRIFT WITH A SOURCE IS A DIFFERENT FINDING FROM ONE "
     "WITHOUT.**"),

    # ---- COMPONENT 2 -----------------------------------------------------------------------------
    ("screen yields printed", 5, 5, "yields",
     "### section (D)/(G) BAR 6: 196 raw, whole-token, adjacent, numeric, minus transition "
     "notes (`b381`)."),
    ("screen tightenings made after its output was seen", 4, 4, "tightenings",
     "### section (D): every one resting on ### **WHAT THE STRING IS AND NOT ON THE NUMBER IT "
     "PRODUCES** (`b380`)."),
    ("candidates surviving the screen", 4, 4, "candidates", "### section (D)."),
    ("candidates read by hand with a printed verdict", 4, 4, "candidates",
     "### section (D)/(G) BAR 5: ### **A SCREEN THAT OVER-REPORTS BY DESIGN MUST BE MARKED AS A "
     "SCREEN AND ITS RESIDUE READ.**"),
    ("candidates repaired by this component", 0, 0, "candidates",
     "### section (D)/(H) `(E2)`: two are false positives and two are undecidable."),
    ("superseded citations repaired", 0, 0, "citations",
     "### section (D): ### **A VERSION THAT EXISTS BUT IS SUPERSEDED IS A CURRENCY ITEM, NOT A "
     "PHANTOM**, and this act does not touch one."),
    ("superseded citations reported", 66, 66, "citations", "### section (D)."),

    # ---- THE SCOPE BOUNDARY ----------------------------------------------------------------------
    ("bytes written into the standing document-class taxonomy", 0, 0, "bytes",
     "### section (E)/(G) BAR 8: that is `b392`'s scope, and ### **A LEG DOES NOT REACH INTO THE "
     "NEXT LEG`S SCOPE.**"),
    ("deposit rules written", 0, 0, "rules", "### section (E): `b392`'s."),
    ("corpus documents written into outside the classified citation lines", 0, 0, "documents",
     "### section (E), the ledgers excepted."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 8, 8, "bars", "### section (G)."),
    ("bars with a stated floor", 8, 8, "bars", "### section (G): `b347`'s rule."),
    ("numerical bars on a computed quantity", 0, 0, "bars",
     "### section (G): ### **THIS ACT COMPUTES NOTHING ABOUT THE OBJECT.**"),
    ("must-fail fixtures", 4, 4, "fixtures", "### section (G): BARS 2, 3, 4 and 5."),
    ("gate arms declared", "ARMS", "ARMS", "arms",
     "### section (G): counted off this face`s own text by this file -- and ### **THE WILDCARD "
     "MENTION `G-NO*` IS NOT AN ARM** (`b348`)."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "### section (G) (`b348`, `b373`)."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("arms measuring a different thing on a re-run", 0, 0, "arms",
     "### section (G): every diff arm measures against the PRE-ACT BLOB and never within the run "
     "(`b352`, `b388`, `b389`, `b390`)."),
    ("new `relay` tool files", 6, 6, "files", "### section (E): the cap counts FILES (`b382`)."),
    ("files staged by `-A`", 0, 0, "commands", "`b381`."),
    ("untracked run records of earlier acts committed", 0, 0, "files", "### section (E)."),
    ("`.git/hooks/pre-push` copies deleted", 0, 0, "files", "### section (E): RULING (R16)."),
    ("archive or outputs files touched", 0, 0, "files", "### section (E)."),

    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("classes ruled", 0, 0, "rulings", "### section (I)."),
    ("documents reclassified", 0, 0, "documents", "### section (I)."),
    ("grades moved", 0, 0, "grades", "### section (E)/(I)."),
    ("claims withdrawn", 0, 0, "claims", "### section (E)/(I)."),
    ("registry rows edited", 0, 0, "rows", "### section (E)/(I)."),
    ("standards edited", 0, 0, "files", "### section (I)."),
    ("amendments applied", 0, 0, "amendments", "### section (I)."),
    ("correspondence rows edited", 0, 0, "rows", "### section (E)/(I): rows are APPENDED."),
    ("map head notes touched", 0, 0, "notes", "### section (E): `(R18)`'s notes stand."),
    ("lists closed", 0, 0, "lists", "### section (I): the four stay OPEN."),
    ("faces promoted", 0, 0, "faces", "### section (I)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (I)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (I)."),
    ("claims about h2, totality, the roster", 0, 0, "claims",
     "### section (I): ### **NO CLAIM IN EITHER DIRECTION.**"),
    ("posture-lock changes", 0, 0, "changes", "### section (I)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (I): the instrument lane stays parked."),
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
    print('b391_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b391_registration_2026-09-09.txt -- b391, THE PHANTOM VERSION "
                             "AND THE FIVE CLUSTERS"),
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
