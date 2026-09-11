# -*- coding: utf-8 -*-
"""b410_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC. ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### **AND THE CLAUSES THAT MATTER MOST BOUND A CLASSIFICATION, A COUNT AND THREE ARMS:** ### a
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

REG = os.path.join(ROOT, 'data', 'b410_registration_2026-09-10.txt')
SPEC = os.path.join(ROOT, 'data', 'b410_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    # ---- THE STANDING NOTHINGS -------------------------------------------------------------------
    ("deposit actions", 0, 0, "actions", "### (Z)/(K) BAR 14: NOTHING DEPOSITS."),
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
    ("class symbols renumbered, in any document", 0, 0, "symbols", "### section (Z)."),
    ("instrument numbers assigned, moved or reconciled", 0, 0, "numbers",
     "### (K) BAR 9: the `I-7` collision is ROUTED, not resolved."),
    ("folds run", 0, 0, "folds", "### section (Z)."),
    ("rules struck, amended, widened or re-ruled", 0, 0, "rules",
     "### section (Z): (R26)-(R28) are the AUTHOR`S and are EXECUTED, not minted."),
    ("grades moved or conferred", 0, 0, "grades", "### (K) BAR 10."),
    ("new grades minted", 0, 0, "grades", "### (K) BAR 10."),
    ("kappa values measured or certified", 0, 0, "values", "### (K) BAR 6."),
    ("channels opened", 0, 0, "channels", "### (K) BAR 6."),
    ("routes proposed, priced or opened on a bright verdict", 0, 0, "routes", "### (K) BAR 6."),
    ("faces promoted", 0, 0, "faces", "### section (Z)."),
    ("owed rows paid", 0, 0, "rows", "### section (Z)."),
    ("sites entered in row U1", 0, 0, "sites", "### section (Z): the register is FROZEN at six."),
    ("rows of `FACES_LEDGER.md` written", 0, 0, "rows", "### section (Z)."),
    ("lists closed", 0, 0, "lists", "### section (Z)."),
    ("rows retired", 0, 0, "rows", "### section (Z)."),
    ("locked faces edited", 0, 0, "faces", "### section (Z)."),
    ("prior acts` banks edited", 0, 0, "files",
     "### section (Z): b409 is CORRECTED on two counts, not edited."),
    ("banked ferries edited", 0, 0, "files", "### section (Z)."),
    ("registry rows edited", 0, 0, "rows", "### section (Z)."),
    ("correspondence rows edited", 0, 0, "rows", "### section (Z): rows are APPENDED."),
    ("FERRY_STANDING clauses added", 0, 0, "clauses", "### section (Z)."),
    ("in-place repairs of any sentence", 0, 0, "repairs",
     "### (W)/(Z): the doubled apostrophe is OBSERVED and NOT repaired."),
    ("bridges typed", 0, 0, "bridges", "### section (Z)."),
    ("theorems reported as applying where a condition is unchecked", 0, 0, "theorems",
     "### section (C)."),
    ("claims about h2, in either direction", 0, 0, "claims",
     "### (K) BAR 14: the keystone`s own identification is QUOTED, never asserted."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("counts adopted without measurement", 0, 0, "counts", "### section (Z)."),
    ("run records read from a directory listing", 0, 0, "records", "### (K) BAR 13."),
    ("arms trusted because a previous act trusted them", 0, 0, "arms", "### (K) BAR 13."),
    ("expectations scored over a set this face does not name", 0, 0, "expectations",
     "### (R26), the author`s: an expectation over an unnamed set is UNSCORABLE."),
    ("scores averaged to one word where premise and conclusion differ", 0, 0, "scores",
     "### (R27), the author`s."),

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
    ("values carried from recollection rather than read", 0, 0, "values", "### section (Z)."),
    ("predecessor claims corrected without editing the predecessor", 2, 2, "claims",
     "### section (A): b409`s closing census file, and its unread continuation."),

    # ---- COMPONENT 1 -----------------------------------------------------------------------------
    ("imports classified under Definition 2.5", 4, 4, "sentences", "### section (C)."),
    ("independent instruments the classification is run under", 2, 2, "instruments",
     "### (K) BAR 2: Definition 2.5 AND the standing screen `I-7`."),
    ("imports whose verdict the two instruments disagree on", 0, None, "sentences",
     "### (K) BAR 2: MEASURED, and printed either way."),
    ("verdicts on whether 3.1-H applies to the reduction", 1, 1, "verdicts", "### section (C)."),

    # ---- COMPONENT 2 AND ADDITION ONE ------------------------------------------------------------
    ("rows of the calibration family enumerated", 0, None, "rows",
     "### section (D): MEASURED from the section, not predicted."),
    ("certificates named for a calibration row", 0, None, "certificates",
     "### section (D): MEASURED."),
    ("compiled terminals claimed for section 9", 0, 0, "terminals",
     "### (K) BAR 10: its Correspondence row reads `(none)`."),
    ("registers the corollary is restricted to", 2, 2, "registers", "### ADDITION ONE."),
    ("candidate counts printed for those registers", 2, 2, "counts", "### ADDITION ONE."),

    # ---- COMPONENT 3 -----------------------------------------------------------------------------
    ("gate arms built under (R26)-(R28)", 3, 3, "arms", "### section (E)."),
    ("built arms carrying fixtures in BOTH polarities", 3, 3, "arms", "### (K) BAR 3."),
    ("built arms run retroactively against their own incident`s bank", 3, 3, "arms",
     "### (K) BAR 3: an arm that would not have caught its own incident is NOT BUILT."),
    ("built arms that fail to fire on their own incident", 0, 0, "arms", "### (K) BAR 3."),

    # ---- COMPONENT 4 AND ADDITION TWO ------------------------------------------------------------
    ("routed documents hand-read", 0, None, "documents",
     "### section (F): MEASURED, the sample stated before the count."),
    ("buckets the routed documents are sorted into", 3, 3, "buckets", "### section (F)."),
    ("prices printed for the density question", 1, 1, "prices", "### ADDITION TWO."),
    ("density-register statements the record already holds", 0, None, "statements",
     "### ADDITION TWO: MEASURED."),

    # ---- THE APPARATUS ---------------------------------------------------------------------------
    ("bars declared", 14, 14, "bars", "### section (K)."),
    ("numerical bars on a computed quantity", 0, 0, "bars", "### (K): this act computes none."),
    ("gate arms declared", "ARMS", "ARMS", "arms", "### section (G2), counted off this face."),
    ("`G-NO*` arms reading raw prose", 0, 0, "arms", "### (K) BAR 13."),
    ("prose-reading arms without a control on the other polarity", 0, 0, "arms", "### (K) BAR 13."),
    ("prose-reading arms that match before folding markup away", 0, 0, "arms", "### (K) BAR 13."),
    ("substring tests for a tool`s verdict", 0, 0, "tests", "### (K) BAR 13: A2, inherited."),
    ("inherited arms not re-pointed at this act", 0, 0, "arms", "### (K) BAR 13."),
    ("arms demanding a number a previous act happened to produce", 0, 0, "arms",
     "### (K) BAR 13."),
    ("arms naming their reference by address rather than content", 0, 0, "arms",
     "### (K) BAR 13: b409`s own late defect."),
    ("arms written by address rather than content", 0, 0, "arms", "RULING (R2)."),
    ("text handles opened for write before the bytes are encoded", 0, 0, "handles",
     "### (K) BAR 13: b405`s zero-byte husk."),
    ("backslashes written through a quoted heredoc", 0, 0, "backslashes",
     "### (K) BAR 13: this act`s survey met it AGAIN and built the boundary from `chr(92)`."),
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
    print('b410_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": ("data/b410_registration_2026-09-10.txt -- b410, THE FOUR IMPORTS CLASSIFIED, THE FAMILY "
                             "READ WHOLE, THE THREE ARMS BUILT, AND THE DENSITY REGISTER PRICED"),
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
