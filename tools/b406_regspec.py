# -*- coding: utf-8 -*-
"""b406_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b406_registration_2026-09-10.txt')
SPEC = os.path.join(ROOT, 'data', 'b406_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("deposit actions", 0, 0, "actions", "### (Z)/(K) BAR 14: NOTHING DEPOSITS."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (Z)."),
    ("platform calls of any kind", 0, 0, "calls", "### section (Z)."),
    ("instrument runs", 0, 0, "runs", "### (K) BAR 5."),
    ("kernel builds run", 0, 0, "builds", "### (K) BAR 5: both lanes PARKED."),
    ("`.lean` files touched", 0, 0, "files", "### (K) BAR 5: nothing in the kernel."),
    ("repositories cloned", 0, 0, "repositories", "### section (Z)."),
    ("branches merged, pushed, fetched, created or checked out", 0, 0, "branches",
     "### section (Z): the push branch excepted, under Rule 4.10."),
    ("rules struck, amended or re-ruled", 0, 0, "rules", "### (K) BAR 10."),
    ("grades moved or conferred", 0, 0, "grades", "### (K) BAR 3."),
    ("faces promoted", 0, 0, "faces", "### section (Z)."),
    ("owed rows paid", 0, 0, "rows", "### section (Z)."),
    ("locked faces edited", 0, 0, "faces", "### (K) BAR 4."),
    ("prior acts` banks edited", 0, 0, "files", "### (K) BAR 4."),
    ("banked ferries edited", 0, 0, "files", "### (K) BAR 4; section (G)(d)."),
    ("keystone documents edited", 0, 0, "documents", "### section (Z)."),
    ("rows of FACES_LEDGER.md written", 0, 0, "rows",
     "### (W): the row is READ and not written by this act."),
    ("claims about h2, in either direction", 0, 0, "claims", "### (K) BAR 14."),
    ("coordinates added to the row", 0, 0, "coordinates", "### (K) BAR 7: PRICED, NOT ADDED."),
    ("lists closed", 0, 0, "lists", "### section (Z): the four stay OPEN."),
    ("equivalences compiled", 0, 0, "equivalences", "### section (Z)."),
    ("bridges typed", 0, 0, "bridges", "### (K) BAR 8."),
    ("claims that a witness exists at any site", 0, 0, "claims", "### (K) BAR 8."),
    ("names minted by the seat", 0, 0, "names", "### (K) BAR 6: minting is the author`s."),
    ("entries of row U1 rewritten", 0, 0, "entries", "### (K) BAR 8."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("counts adopted from a ferry without measurement", 0, 0, "counts", "### sections (H), (Z)."),

    # ---- STEP ZERO -------------------------------------------------------------------------------
    ("ferry parts received", 1, 1, "parts", "### section (A): part 1 of 1, receipt IN FULL."),
    ("ferry scan hits", 0, 0, "hits", "### section (A)."),
    ("censuses run at step zero", 2, 2, "censuses", "### section (A): TOTAL MISSING 0 each."),
    ("repositories ahead of origin at step zero", 0, 0, "repositories", "### section (A)."),
    ("readings of the order declared in advance on this face", 8, 8, "readings",
     "### section (A)."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("extract reads left AMBIGUOUS or ABSENT", 0, 0, "reads", "### section (A)."),
    ("index queries recorded before a mark of ABSENT", 3, 3, "queries", "### section (A)."),
    ("values carried from recollection rather than read", 0, 0, "values", "### section (Z)."),

    # ---- COMPONENT 1 -----------------------------------------------------------------------------
    ("sites read for their actual shape", 2, 2, "sites", "### section (B)."),
    ("obstructions written out as a quantifier string", 2, 2, "strings", "### section (B)."),
    ("trivially satisfiable existentials counted as an existential found", 0, 0, "existentials",
     "### section (B): a witness for a trivial existential carries no content to share."),

    # ---- COMPONENT 2 -----------------------------------------------------------------------------
    ("parts the Component 2 answer is scored in", 2, 2, "parts",
     "### section (C): a name for the barrier is not a name for the repair."),

    # ---- COMPONENT 3 -----------------------------------------------------------------------------
    ("third coordinates priced", 1, 1, "coordinates", "### section (D)."),
    ("third coordinates added", 0, 0, "coordinates", "### (K) BAR 7."),
    ("cells counted fillable on this seat`s inference rather than the site`s text", 0, 0, "cells",
     "### section (D): the fill test is strict."),

    # ---- ADDITION ONE ----------------------------------------------------------------------------
    ("clauses stated for the width site in the source`s own symbols", 2, 2, "clauses",
     "### section (E)."),
    ("derivations of whether a shared g can exist", 0, 0, "derivations",
     "### (K) BAR 9: reported NOT ATTEMPTED."),

    # ---- ADDITION TWO ----------------------------------------------------------------------------
    ("standing laws audited for arity", 4, 4, "laws", "### section (F)."),
    ("laws struck, amended or re-ruled by the audit", 0, 0, "laws", "### (K) BAR 10."),

    # ---- ADDITION THREE --------------------------------------------------------------------------
    ("closure predicates printed with their yields", 2, 2, "predicates", "### (K) BAR 2."),
    ("sweeps whose subject is the seal`s own terminals", 1, 1, "sweeps", "### (K) BAR 1."),
    ("sentences about another object repaired", 0, 0, "sentences", "### (K) BAR 1."),
    ("wide-sweep hits hand-read or repaired", 0, 0, "hits", "### (K) BAR 1."),
    ("repairs that change a claim or move a grade", 0, 0, "repairs", "### (K) BAR 3."),

    # ---- ADDITION FOUR ---------------------------------------------------------------------------
    ("clauses appended to FERRY_STANDING", 1, 1, "clauses", "### section (H)."),
    ("version-line bumps in FERRY_STANDING", 0, 0, "bumps", "### (K) BAR 11."),
    ("measured clauses added to FERRY_STANDING by hand", 0, 0, "clauses", "### (K) BAR 11."),
    ("standing sentences promoted that the order did not name", 0, 0, "sentences",
     "### section (H): the second is ROUTED, not promoted."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 14, 14, "bars", "### section (K)."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### (K): this act computes none."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (G2), counted off this face."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "### (K) BAR 12."),
    ("prose-reading arms without a control on the other polarity", 0, 0, "arms", "### (K) BAR 12."),
    ("substring tests for a tool`s verdict", 0, 0, "tests", "### (K) BAR 12: b405`s G-KEY."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("arms taking their population from a name pattern", 0, 0, "arms", "(b397)."),
    ("arms reading a repository state without a named reference", 0, 0, "arms", "(b403)."),
    ("arms demanding a repository state that predates the act", 0, 0, "arms", "(b404)."),
    ("text handles opened for write before the bytes are encoded", 0, 0, "handles",
     "### (K) BAR 13: b405`s zero-byte husk."),
    ("zero-byte husks left by a failed write", 0, 0, "files", "### (K) BAR 13."),
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
    print('b406_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b406_registration_2026-09-10.txt -- b406, THE SITES WITHOUT "
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
