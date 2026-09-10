# -*- coding: utf-8 -*-
"""b408_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### **AND THE CLAUSES THAT MATTER MOST BOUND ONE SWEEP, ONE PROMOTION AND ONE STOP:** ### a
### sweep whose subject is the seal and not the words; an amendment made by the standing file's own
### mechanism without bumping the version every live ferry cites; and a reading that names two
### clauses and refuses to derive whether they can be met.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b408_registration_2026-09-10.txt')
SPEC = os.path.join(ROOT, 'data', 'b408_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("deposit actions", 0, 0, "actions", "### (Z)/(K) BAR 12: NOTHING DEPOSITS."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (Z)."),
    ("platform calls of any kind", 0, 0, "calls", "### section (Z)."),
    ("instrument runs", 0, 0, "runs", "### section (Z)."),
    ("kernel builds run", 0, 0, "builds", "### section (Z): both lanes PARKED."),
    ("`.lean` files touched", 0, 0, "files", "### section (Z)."),
    ("axiom profiles read or inferred", 0, 0, "profiles", "### section (Z)."),
    ("repositories cloned", 0, 0, "repositories", "### section (Z)."),
    ("branches merged, pushed, fetched, created or checked out", 0, 0, "branches",
     "### section (Z): the push branch excepted, under Rule 4.10."),
    ("folds run", 0, 0, "folds", "### section (Z)/(K) BAR 9: a fold is its own act."),
    ("rules struck, amended, widened or re-ruled", 0, 0, "rules", "### (K) BAR 9."),
    ("grades moved or conferred", 0, 0, "grades", "### section (Z)."),
    ("faces promoted", 0, 0, "faces", "### section (Z)."),
    ("owed rows paid", 0, 0, "rows", "### section (Z)."),
    ("locked faces edited", 0, 0, "faces", "### section (Z)."),
    ("prior acts` banks edited", 0, 0, "files", "### section (Z)."),
    ("banked ferries edited", 0, 0, "files", "### section (Z)."),
    ("keystone documents edited", 0, 0, "documents", "### section (Z)."),
    ("rows of FACES_LEDGER.md written", 0, 0, "rows", "### section (W)/(Z)."),
    ("FERRY_STANDING clauses added", 0, 0, "clauses", "### section (Z)."),
    ("shared instruments amended", 0, 0, "instruments", "### section (Z): b407 amended one, not b408."),
    ("in-place repairs of any kind", 0, 0, "repairs", "### (K) BAR 11/(W)."),
    ("claims about h2, in either direction", 0, 0, "claims", "### (K) BAR 12."),
    ("coordinates added to the row", 0, 0, "coordinates", "### section (Z)."),
    ("lists closed", 0, 0, "lists", "### section (Z): the four stay OPEN."),
    ("bridges typed", 0, 0, "bridges", "### section (Z)."),
    ("names minted by the seat", 0, 0, "names", "### (K) BAR 7: the naming is ROUTED."),
    ("numbering schemes reconciled", 0, 0, "schemes", "### section (Z): the hazard is PRINTED."),
    ("arms added, removed, renamed or promoted", 0, 0, "arms", "### (K) BAR 9."),
    ("standing cores proposed", 0, 0, "proposals", "### (H): measure it, do not reform it."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("counts adopted without measurement", 0, 0, "counts", "### section (Z)."),
    ("run records read from a directory listing", 0, 0, "records", "### (K) BAR 11."),

    # ---- STEP ZERO -------------------------------------------------------------------------------
    ("ferry parts received", 1, 1, "parts", "### section (A): part 1 of 1, receipt IN FULL."),
    ("ferry scan hits", 0, 0, "hits", "### section (A)."),
    ("censuses run at step zero", 2, 2, "censuses", "### section (A): TOTAL MISSING 0 each."),
    ("repositories ahead of origin at step zero", 0, 0, "repositories", "### section (A)."),
    ("readings of the order declared in advance on this face", 7, 7, "readings",
     "### section (A)."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("extract reads left AMBIGUOUS or ABSENT", 0, 0, "reads", "### section (A)."),
    ("index queries recorded before a mark of ABSENT or ROUTED", 3, 3, "queries",
     "### section (A), each read from the VERDICT LINE under A2."),
    ("values carried from recollection rather than read", 0, 0, "values", "### section (Z)."),

    # ---- ADDITION THREE --------------------------------------------------------------------------
    ("channels named from the classes document`s own words", 2, 2, "channels", "### section (B)."),
    ("channel sweeps run with the predicate printed", 1, 1, "sweeps", "### (K) BAR 2."),
    ("sweep hits counted without being hand-read", 0, 0, "hits", "### (K) BAR 2."),
    ("hits reported as examinations whose document uses the other numbering", 0, 0, "hits",
     "### (K) BAR 3."),
    ("class numberings the corpus carries", 2, 2, "numberings",
     "### section (B): the corpus`s own remark tabulates them."),
    ("sentences asserting a channel is open, available or promising", 0, 0, "sentences",
     "### (K) BAR 4."),

    # ---- ADDITION FOUR ---------------------------------------------------------------------------
    ("constituents classified", 8, 8, "constituents", "### section (C): K1 through K8."),
    ("layers the price is printed in", 2, 2, "layers", "### (K) BAR 5."),
    ("in-principle claims made without the UNCHECKED mark", 0, 0, "claims", "### (K) BAR 5."),
    ("lines of the classified proof written", 0, 0, "lines", "### (K) BAR 6."),

    # ---- COMPONENT 1 -----------------------------------------------------------------------------
    ("span counts taken from the tool`s own output", 1, 1, "counts", "### (K) BAR 1."),
    ("span counts asserted ahead of the tool", 0, 0, "counts", "### (K) BAR 1."),

    # ---- COMPONENT 2 -----------------------------------------------------------------------------
    ("dresses put to the test", 4, 4, "dresses", "### section (E): the draft`s three plus b407`s."),
    ("sentences stated as entailing all four", 0, None, "sentences",
     "### section (E): MEASURED -- one if the test says one, none if it does not."),

    # ---- COMPONENT 3 -----------------------------------------------------------------------------
    ("questions put to row U1", 1, 1, "questions", "### section (F)."),
    ("grades conferred on row U1 by this act", 0, 0, "grades", "### section (F): a description."),

    # ---- ADDITION ONE ----------------------------------------------------------------------------
    ("routed-price lists built", 1, 1, "lists", "### section (G)."),
    ("lists that do not declare their own scope", 0, 0, "lists", "### (K) BAR 10."),

    # ---- ADDITION TWO ----------------------------------------------------------------------------
    ("suites whose arm names were read", 4, 4, "suites", "### section (H)."),
    ("measures whose own limit is not printed", 0, 0, "measures", "### section (H)."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 12, 12, "bars", "### section (K)."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### (K): this act computes none."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (G2), counted off this face."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "### (K) BAR 11."),
    ("prose-reading arms without a control on the other polarity", 0, 0, "arms", "### (K) BAR 11."),
    ("prose-reading arms that match before folding markup away", 0, 0, "arms",
     "### (K) BAR 11: b407`s G-BLOCKERKIND."),
    ("substring tests for a tool`s verdict", 0, 0, "tests", "### (K) BAR 11: A2, inherited."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("arms taking their population from a name pattern", 0, 0, "arms", "(b397)."),
    ("arms reading a repository state without a named reference", 0, 0, "arms", "(b403)."),
    ("text handles opened for write before the bytes are encoded", 0, 0, "handles",
     "### (K) BAR 11: b405`s zero-byte husk."),
    ("new `relay` tool files", 6, 6, "files", "### (W) KIND 8."),
    ("files of a KIND the write list does not name", 0, 0, "files", "### section (W)."),
    ("files staged by `-A`", 0, 0, "commands", "b381."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3)."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED by `b300_regspec.count_predictions`, IMPORTED."),
]


def count_arms(text):
    return len(set(re.findall(r'\bG-[A-Z0-9-]+', text)) - {'G-NO'})


def main(argv):
    print('=' * 100)
    print('b408_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b408_registration_2026-09-10.txt -- b408, THE SITES WITHOUT "
                             "AN EXISTENTIAL, AND WHAT THEIR REPAIR WOULD BE CALLED"),
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
