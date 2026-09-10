# -*- coding: utf-8 -*-
"""b405_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### **AND THE CLAUSES THAT MATTER MOST BOUND ONE RULING, ONE COLUMN AND ONE REFUSAL:** ### a
### ruling executed inside a column law it does not amend; a column whose cells may be filled from
### one place only; and a clause quoted verbatim and tested rather than improved.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b405_registration_2026-09-10.txt')
SPEC = os.path.join(ROOT, 'data', 'b405_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("deposit actions", 0, 0, "actions", "### section (Z)/(K) BAR 14: NOTHING DEPOSITS."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (Z)."),
    ("platform calls of any kind", 0, 0, "calls", "### section (Z)."),
    ("instrument runs", 0, 0, "runs", "### section (Z)/(K) BAR 4."),
    ("kernel builds run", 0, 0, "builds", "### (K) BAR 4: the lane is PARKED."),
    ("`.lean` files touched", 0, 0, "files", "### (K) BAR 4."),
    ("repositories cloned", 0, 0, "repositories", "### section (Z)."),
    ("branches merged, pushed, fetched, created or checked out", 0, 0, "branches",
     "### section (Z): the push branch excepted, under Rule 4.10."),
    ("rules struck or amended", 0, 0, "rules", "### section (Z)."),
    ("column laws amended", 0, 0, "laws", "### section (B): the law is OBEYED, not amended."),
    ("grades moved or conferred", 0, 0, "grades", "### section (Z)."),
    ("faces promoted", 0, 0, "faces", "### section (Z)."),
    ("owed rows paid", 0, 0, "rows", "### section (Z)."),
    ("locked faces edited", 0, 0, "faces", "### section (Z)."),
    ("prior acts` banks edited", 0, 0, "files", "### section (Z)."),
    ("keystone documents edited", 0, 0, "documents", "### section (Z)."),
    ("claims about h2, in either direction", 0, 0, "claims", "### (K) BAR 15."),
    ("coordinates closed", 0, 0, "coordinates", "### section (Z)."),
    ("lists closed", 0, 0, "lists", "### section (Z): the four stay OPEN."),
    ("equivalences compiled", 0, 0, "equivalences", "### section (Z)."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),

    # ---- STEP ZERO -------------------------------------------------------------------------------
    ("ferry parts received", 1, 1, "parts", "### section (A): part 1 of 1, receipt IN FULL."),
    ("ferry scan hits", 0, 0, "hits", "### section (A)."),
    ("censuses run at step zero", 2, 2, "censuses", "### section (A): TOTAL MISSING 0 each."),
    ("repositories ahead of origin at step zero", 0, 0, "repositories", "### section (A)."),
    ("readings of the order declared in advance on this face", 9, 9, "readings",
     "### section (A)."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("extract reads left AMBIGUOUS or ABSENT", 0, 0, "reads", "### (K) BAR 2."),
    ("values carried from recollection rather than read", 0, 0, "values", "### section (Z)."),

    # ---- THE PIN ---------------------------------------------------------------------------------
    ("kernel terminals quoted whole", 2, 2, "terminals", "### section (A) reading (3)."),
    ("kernel terminals quoted from a working tree instead of a pin", 0, 0, "terminals",
     "### (K) BAR 1."),
    ("pins printed as both a tag and a commit", 1, 1, "pins", "### (K) BAR 1."),
    ("axiom profiles read from a printed file", 1, 1, "profiles",
     "### section (A) reading (4): the tracked transcript at the pin."),
    ("axiom profiles inferred rather than read or reported UNREAD", 0, 0, "profiles",
     "### (K) BAR 3."),

    # ---- COMPONENT 1 -----------------------------------------------------------------------------
    ("sites of row U1 read whole from the committed blob", 6, 6, "sites",
     "### section (A) reading (1)."),
    ("tests put to each site", 3, 3, "tests", "### section (C) COMPONENT 1."),
    ("table cells printed without their deciding quote", 0, 0, "cells",
     "### section (C): the deciding sentence is printed beside EVERY cell."),

    # ---- COMPONENT 2 -----------------------------------------------------------------------------
    ("refusal clauses quoted verbatim", 1, 1, "clauses", "### (K) BAR 8."),
    ("refusal clauses summarised instead of quoted", 0, 0, "clauses", "### (K) BAR 8."),
    ("questions put to the refusal clause", 1, 1, "questions", "### section (C) COMPONENT 2."),
    ("entries restated by Component 2", 0, 0, "entries", "### section (C) COMPONENT 2."),

    # ---- COMPONENT 3 -- (R24) --------------------------------------------------------------------
    ("coordinates added to the row", 2, 2, "coordinates", "### section (B): KIND and WITNESS."),
    ("new columns added to the ledger", 0, 0, "columns", "### section (B)/(K) BAR 7."),
    ("table lines whose column count changes", 0, 0, "lines", "### (K) BAR 7."),
    ("KIND cells written", 6, 6, "cells", "### section (C) COMPONENT 3."),
    ("WITNESS cells written", 6, 6, "cells", "### section (C) COMPONENT 3."),
    ("cells filled from the navigator`s paragraph or from another site", 0, 0, "cells",
     "### (K) BAR 5."),
    ("new measurements taken to fill a cell", 0, 0, "measurements", "### section (B): (R24)."),
    ("touched ledger cells carrying their prior text as a TRUE PREFIX", 2, 2, "cells",
     "### (K) BAR 7."),
    ("untouched ledger cells BYTE-IDENTICAL to the pre-act blob", 5, 5, "cells", "### (K) BAR 7."),
    ("content lost in any edited file", 0, 0, "lines", "### (K) BAR 7."),

    # ---- ADDITION ONE ----------------------------------------------------------------------------
    ("clauses a shared witness is declared to have", 2, 2, "clauses",
     "### section (D): h1 and h2, from the theorem itself."),
    ("bridges typed between any two of the six", 0, 0, "bridges", "### (K) BAR 6."),
    ("sentences asserting the compiled shape holds at an instance", 0, 0, "sentences",
     "### (K) BAR 6."),
    ("navigator candidate witnesses scored against the sites` own text", 2, 2, "candidates",
     "### section (D)."),
    ("navigator candidate witnesses accepted without scoring", 0, 0, "candidates",
     "### section (D)."),

    # ---- ADDITION TWO ----------------------------------------------------------------------------
    ("branch rules fixed before the read", 1, 1, "rules", "### section (E)."),
    ("branches of Addition Two taken", 1, 1, "branches", "### section (E)."),
    ("clauses of the finite-side terminal read and labelled", 3, 3, "clauses",
     "### section (A) reading (5): the docstring`s own (a), (b), (c)."),

    # ---- THE DRAFT`S ADDITION --------------------------------------------------------------------
    ("routes priced", 1, 1, "routes", "### section (F)."),
    ("routes taken", 0, 0, "routes", "### section (F): a route priced is not a route taken."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 15, 15, "bars", "### section (K)."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### section (K): this act computes none."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (G), counted off this face."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "### (K) BAR 11 (b348, b400, b404)."),
    ("prose-reading arms without a control on the other polarity", 0, 0, "arms", "### (K) BAR 11."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("arms taking their population from a name pattern", 0, 0, "arms", "(b397)."),
    ("arms reading a repository state without a named reference", 0, 0, "arms", "### (K) BAR 12."),
    ("arms whose control is taken at a different moment from the treatment", 0, 0, "arms",
     "### (K) BAR 12."),
    ("arms demanding a repository state that predates the act", 0, 0, "arms", "### (K) BAR 13."),
    ("new `relay` tool files", 6, 6, "files", "### (K) BAR 10/(W) KIND 8."),
    ("files of a KIND the write list does not name", 0, 0, "files", "### (K) BAR 9."),
    ("files staged by `-A`", 0, 0, "commands", "b381."),
    ("SIDE-lv-conservation files written", 0, 0, "files",
     "### (W): read at a tag, not touched, and not on the roster."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3)."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED."),
]


def count_arms(text):
    return len(set(re.findall(r'\bG-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b405_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    print('  ### ### **THE OPEN CLAUSE, MEASURED RATHER THAN TYPED:** ### ARMS %d'
          % measured['ARMS'])
    CLAUSES[:] = [(c, measured.get(cap, cap), measured.get(dem, dem), u, f)
                  for (c, cap, dem, u, f) in CLAUSES]
    clauses = [{"clause": c, "cap": cap,
                "demand": (n if (dem is None and c.startswith('artifact counts')) else
                           (cap if dem is None else dem)),
                "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": ("data/b405_registration_2026-09-10.txt -- b405, "
                             "THE ROW-S LAW, RESTATED; THE COUNTERMODEL, READ WHOLE"),
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
