# -*- coding: utf-8 -*-
"""b409_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b409_registration_2026-09-10.txt')
SPEC = os.path.join(ROOT, 'data', 'b409_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("deposit actions", 0, 0, "actions", "### (Z)/(K) BAR 13: NOTHING DEPOSITS."),
    ("bytes written at Zenodo, in any branch", 0, 0, "bytes", "### section (Z)."),
    ("platform calls of any kind", 0, 0, "calls", "### section (Z)."),
    ("files under `outputs/` touched", 0, 0, "files", "### (K) BAR 5: DEPOSITED, excluded."),
    ("instrument runs", 0, 0, "runs", "### section (Z)."),
    ("kernel builds run", 0, 0, "builds", "### section (Z): both lanes PARKED."),
    ("`.lean` files touched", 0, 0, "files", "### section (Z)."),
    ("axiom profiles read or inferred", 0, 0, "profiles", "### section (Z)."),
    ("repositories cloned", 0, 0, "repositories", "### section (Z)."),
    ("branches merged, pushed, fetched, created or checked out", 0, 0, "branches",
     "### section (Z): the push branch excepted, under Rule 4.10."),
    ("class symbols renumbered, in any document", 0, 0, "symbols", "### (K) BAR 4/(Z)."),
    ("schemes assigned by guess or by provenance", 0, 0, "schemes", "### (K) BAR 2/BAR 3."),
    ("folds run", 0, 0, "folds", "### section (Z)."),
    ("rules struck, amended, widened or re-ruled", 0, 0, "rules", "### section (Z)."),
    ("grades moved or conferred", 0, 0, "grades", "### (K) BAR 11."),
    ("new grades minted", 0, 0, "grades", "### (K) BAR 10: the restatement carries the original`s."),
    ("faces promoted", 0, 0, "faces", "### section (Z)."),
    ("owed rows paid", 0, 0, "rows", "### section (Z)."),
    ("sites entered in row U1", 0, 0, "sites", "### section (E) COMPONENT 5."),
    ("coordinates added to the row", 0, 0, "coordinates", "### section (E)."),
    ("lists closed", 0, 0, "lists", "### (K) BAR 11: a freeze is not a closure."),
    ("rows retired", 0, 0, "rows", "### (K) BAR 11."),
    ("locked faces edited", 0, 0, "faces", "### section (Z)."),
    ("prior acts` banks edited", 0, 0, "files", "### section (Z): b408 is CORRECTED, not edited."),
    ("banked ferries edited", 0, 0, "files", "### section (Z)."),
    ("registry rows edited", 0, 0, "rows", "### section (Z)."),
    ("correspondence rows edited", 0, 0, "rows", "### section (Z): rows are APPENDED."),
    ("FERRY_STANDING clauses added", 0, 0, "clauses", "### section (Z)."),
    ("in-place repairs of any sentence", 0, 0, "repairs", "### (W)/(Z)."),
    ("bridges typed", 0, 0, "bridges", "### section (D)."),
    ("routes proposed, priced or opened on a bright verdict", 0, 0, "routes", "### (K) BAR 8."),
    ("theorems reported as applying where a condition is unchecked", 0, 0, "theorems",
     "### section (D)."),
    ("claims about h2, in either direction", 0, 0, "claims", "### (K) BAR 13."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("counts adopted without measurement", 0, 0, "counts", "### section (Z)."),
    ("run records read from a directory listing", 0, 0, "records", "### (K) BAR 12."),
    ("arms trusted because a previous act trusted them", 0, 0, "arms", "### (K) BAR 12."),

    # ---- STEP ZERO -------------------------------------------------------------------------------
    ("ferry parts received", 1, 1, "parts", "### section (A): part 1 of 1, receipt IN FULL."),
    ("ferry scan hits", 0, 0, "hits", "### section (A)."),
    ("act numbers claimed by an unclosed ferry", 0, 0, "numbers", "### section (A): A1."),
    ("censuses run at step zero", 2, 2, "censuses", "### section (A): TOTAL MISSING 0 each."),
    ("repositories ahead of origin at step zero", 0, 0, "repositories", "### section (A)."),
    ("readings of the order declared in advance on this face", 6, 6, "readings",
     "### section (A)."),
    ("readings taken silently", 0, 0, "readings", "### section (A)."),
    ("extract reads left AMBIGUOUS or ABSENT", 0, 0, "reads", "### section (A)."),
    ("index queries recorded before a mark of ABSENT or ROUTED", 3, 3, "queries",
     "### section (A), each read from the VERDICT LINE under A2."),
    ("values carried from recollection rather than read", 0, 0, "values", "### section (Z)."),

    # ---- COMPONENT 1 / (R25) ---------------------------------------------------------------------
    ("independent witnesses to the canonical index", 2, 2, "witnesses", "### section (A)/(B)."),
    ("pin windows printed with their yields", 2, 2, "windows", "### (K) BAR 1."),
    ("counts of the sweep reported alone", 0, 0, "counts", "### (K) BAR 1."),
    ("head notes written to a SCHEME UNDECLARED document", 0, 0, "notes", "### (K) BAR 3."),
    ("lines added per declared document", 1, 1, "lines", "### (K) BAR 4."),
    ("matcher fixtures, both polarities", 2, 2, "fixtures", "### (K) BAR 6."),
    ("shared instruments newly created", 1, 1, "instruments",
     "### (W) KIND 9: (R25) requires the matcher; NOT counted against the act-tool cap."),

    # ---- COMPONENT 2 -----------------------------------------------------------------------------
    ("artefact hits read whole under their own scheme", 2, 2, "hits", "### section (C)."),
    ("positive controls on the channel search", 1, 1, "controls", "### (K) BAR 7."),
    ("verdicts on the global class as a channel", 1, 1, "verdicts", "### section (C)."),

    # ---- COMPONENT 3 -----------------------------------------------------------------------------
    ("movements of the original proof examined at content", 3, 3, "movements", "### section (D)."),
    ("verdicts on the relativization", 1, 1, "verdicts", "### section (D)."),
    ("hypotheses the original did not need, printed with the verdict", 0, None, "hypotheses",
     "### (K) BAR 9: MEASURED -- printed if the relativization needs one."),
    ("sections appended to the keystone", 0, None, "sections",
     "### (W) KIND 11: MEASURED -- one if and only if the verdict is RELATIVIZES."),

    # ---- COMPONENTS 4 AND 5 ----------------------------------------------------------------------
    ("spine arms proposed", 3, 3, "arms", "### section (E) COMPONENT 4."),
    ("spine arms written", 0, 0, "arms", "### section (E): PROPOSED, NOT BUILT."),
    ("freeze marks appended to row U1", 1, 1, "marks", "### section (E) COMPONENT 5."),
    ("entries added to row U1", 0, 0, "entries", "### section (E)."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 13, 13, "bars", "### section (K)."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### (K): this act computes none."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (G2), counted off this face."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "### (K) BAR 12."),
    ("prose-reading arms without a control on the other polarity", 0, 0, "arms", "### (K) BAR 12."),
    ("prose-reading arms that match before folding markup away", 0, 0, "arms", "### (K) BAR 12."),
    ("substring tests for a tool`s verdict", 0, 0, "tests", "### (K) BAR 12: A2, inherited."),
    ("inherited arms not re-pointed at this act", 0, 0, "arms", "### (K) BAR 12: b408`s eight."),
    ("arms demanding a number a previous act happened to produce", 0, 0, "arms",
     "### (K) BAR 12: b408`s G-REFUTED."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("text handles opened for write before the bytes are encoded", 0, 0, "handles",
     "### (K) BAR 12: b405`s zero-byte husk."),
    ("new `relay` act-tool files", 6, 6, "files", "### (W) KIND 8."),
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
    print('b409_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b409_registration_2026-09-10.txt -- b409, THE SITES WITHOUT "
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
