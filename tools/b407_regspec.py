# -*- coding: utf-8 -*-
"""b407_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b407_registration_2026-09-10.txt')
SPEC = os.path.join(ROOT, 'data', 'b407_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("deposit actions", 0, 0, "actions", "### (Z)/(K) BAR 13: NOTHING DEPOSITS."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (Z)."),
    ("platform calls of any kind", 0, 0, "calls", "### section (Z)."),
    ("instrument runs", 0, 0, "runs", "### section (Z)."),
    ("kernel builds run", 0, 0, "builds", "### section (Z): both lanes PARKED."),
    ("`.lean` files touched", 0, 0, "files", "### section (Z)."),
    ("axiom profiles read or inferred", 0, 0, "profiles", "### section (Z)."),
    ("repositories cloned", 0, 0, "repositories", "### section (Z)."),
    ("branches merged, pushed, fetched, created or checked out", 0, 0, "branches",
     "### section (Z): the push branch excepted, under Rule 4.10."),
    ("rules struck, amended, widened or re-ruled", 0, 0, "rules", "### (K) BAR 9."),
    ("grades moved or conferred", 0, 0, "grades", "### section (Z)."),
    ("faces promoted", 0, 0, "faces", "### section (Z)."),
    ("owed rows paid", 0, 0, "rows", "### section (Z)."),
    ("locked faces edited", 0, 0, "faces", "### section (Z)."),
    ("prior acts` banks edited", 0, 0, "files", "### section (Z)."),
    ("banked ferries edited", 0, 0, "files", "### section (Z)."),
    ("keystone documents edited", 0, 0, "documents", "### section (Z)."),
    ("FERRY_STANDING clauses added", 0, 0, "clauses", "### section (W): b406 added A2, not b407."),
    ("in-place repairs of any kind", 0, 0, "repairs", "### (K) BAR 12/(W)."),
    ("claims about h2, in either direction", 0, 0, "claims", "### (K) BAR 13."),
    ("coordinates added to the row", 0, 0, "coordinates", "### section (Z)."),
    ("lists closed", 0, 0, "lists", "### section (Z): the four stay OPEN."),
    ("equivalences compiled", 0, 0, "equivalences", "### section (Z)."),
    ("bridges typed", 0, 0, "bridges", "### (K) BAR 6."),
    ("names minted by the seat", 0, 0, "names", "### section (Z)."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("counts adopted without measurement", 0, 0, "counts", "### section (Z)."),
    ("run records read from a directory listing", 0, 0, "records", "### (K) BAR 12."),

    # ---- STEP ZERO -------------------------------------------------------------------------------
    ("ferry parts received", 1, 1, "parts", "### section (A): part 1 of 1, receipt IN FULL."),
    ("ferry scan hits", 0, 0, "hits", "### section (A)."),
    ("censuses run at step zero", 2, 2, "censuses", "### section (A): TOTAL MISSING 0 each."),
    ("repositories ahead of origin at step zero", 0, 0, "repositories", "### section (A)."),
    ("readings of the order declared in advance on this face", 7, 7, "readings",
     "### section (A)."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("extract reads left AMBIGUOUS or ABSENT", 0, 0, "reads", "### section (A)."),
    ("index queries recorded before a mark of NOT AN INSTANCE or ROUTED", 3, 3, "queries",
     "### section (A), each read from the VERDICT LINE under A2."),
    ("values carried from recollection rather than read", 0, 0, "values", "### section (Z)."),

    # ---- COMPONENT 1 -----------------------------------------------------------------------------
    ("tests run on the six sites for an interface", 2, 2, "tests",
     "### section (B): the strict Definition-2.2 test and the loose split test."),
    ("counts of the six reported alone", 0, 0, "counts",
     "### (K) BAR 1: both are printed, never the kinder one."),
    ("transmission coefficients measured, asserted or inferred", 0, 0, "coefficients",
     "### (K) BAR 2."),

    # ---- COMPONENT 2 -----------------------------------------------------------------------------
    ("prices of a prior act tested by the harder question", 1, 1, "prices", "### section (C)."),
    ("prices protected because they were this seat`s", 0, 0, "prices", "### (K) BAR 7."),

    # ---- COMPONENT 3 -----------------------------------------------------------------------------
    ("smallest statements named for the repair", 1, 1, "statements", "### section (D)."),
    ("blockers named without saying which kind they are", 0, 0, "blockers", "### (K) BAR 8."),

    # ---- ADDITION ONE ----------------------------------------------------------------------------
    ("limbs of (R20) named as the one that would be widened", 1, 1, "limbs", "### section (E)."),
    ("limbs of (R20) actually widened", 0, 0, "limbs", "### (K) BAR 9: ROUTED, not ruled."),

    # ---- ADDITION TWO ----------------------------------------------------------------------------
    ("guards built for the stale-record species", 1, 1, "guards", "### section (F)."),
    ("options priced before the choice was made", 2, 2, "options", "### section (F)."),
    ("existing bytes of run_clock.py changed", 0, 0, "bytes", "### (K) BAR 10: purely additive."),
    ("existing callers of run_clock moved", 0, 0, "callers", "### (K) BAR 10."),
    ("fixtures on the new function, both polarities", 2, 2, "fixtures", "### section (F)."),

    # ---- ADDITION THREE --------------------------------------------------------------------------
    ("hypotheses of Theorem 3.1 put to the halt, each quoted", 5, 5, "hypotheses",
     "### section (G)."),
    ("verdicts on the halt", 1, 1, "verdicts", "### section (G): one of three, and named."),
    ("resemblances reported as instances", 0, 0, "resemblances", "### (K) BAR 4."),
    ("rows of FACES_LEDGER.md written", 0, None, "rows",
     "### (K) BAR 5: MEASURED -- nothing is filed unless the verdict is INSTANCE."),

    # ---- ADDITION FOUR ---------------------------------------------------------------------------
    ("questions answered from the documents` own words", 2, 2, "questions", "### section (H)."),
    ("disclaimers read as their converse", 0, 0, "disclaimers", "### (K) BAR 6."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 13, 13, "bars", "### section (K)."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### (K): this act computes none."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (G2), counted off this face."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "### (K) BAR 12."),
    ("prose-reading arms without a control on the other polarity", 0, 0, "arms", "### (K) BAR 12."),
    ("substring tests for a tool`s verdict", 0, 0, "tests", "### (K) BAR 12: A2, inherited."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("arms taking their population from a name pattern", 0, 0, "arms", "(b397)."),
    ("arms reading a repository state without a named reference", 0, 0, "arms", "(b403)."),
    ("arms demanding a repository state that predates the act", 0, 0, "arms", "(b404)."),
    ("text handles opened for write before the bytes are encoded", 0, 0, "handles",
     "### (K) BAR 12: b405`s zero-byte husk."),
    ("new `relay` tool files", 6, 6, "files", "### (K) BAR 11/(W) KIND 8."),
    ("shared instruments amended", 1, 1, "instruments", "### (W) KIND 9: additively."),
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
    print('b407_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b407_registration_2026-09-10.txt -- b407, THE SITES WITHOUT "
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
