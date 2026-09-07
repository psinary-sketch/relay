# -*- coding: utf-8 -*-
"""b358_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.** ### Every clause is a forward
### commitment; the spec is emitted BEFORE any file of the act is written.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b358_registration_2026-09-07.txt')
SPEC = os.path.join(ROOT, 'data', 'b358_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("arguments constructed", 0, 0, "arguments", "### section (A), THE CAP: reads and a pricing only."),
    ("bounds proved", 0, 0, "bounds", "### section (A), THE CAP."),
    ("computations beyond what is banked", 0, 0, "computations", "### section (A), THE CAP. ### RE-MEASURED by G-CAP on STRIPPED code."),
    ("series summed, integrals taken, fits made", 0, 0, "operations", "section (A)."),
    ("pricings permitted", 1, None, "pricings", "### section (E) Bar 3: labelled, from banked figures, and NOT attempted. ### Zero if no shape is located."),
    ("conditions a statement must meet to be a SHAPE", 4, 4, "conditions", "### section (B): main term, error term, index, hypotheses."),
    ("grades available per hypothesis", 3, 3, "grades", "### section (C): MET / REFUTABLE / UNDECIDABLE-FROM-THE-RECORD."),
    ("axes each hypothesis is graded on", 2, 2, "axes", "### section (C): the source's objects and the corpus's, NEVER MERGED."),
    ("merged grades", 0, 0, "grades", "### section (C): the two axes are reported apart."),
    ("circularity questions asked of each statement", 3, 3, "questions", "### section (D): (i) named, (ii) equivalent-or-implied, (iii) THE ERROR TERM."),
    ("verdict branches", 3, 3, "branches", "section (F)."),
    ("numerical bars on computed quantities", 0, 0, "bars", "### section (E): this act computes nothing."),
    ("exact bars", 3, 3, "bars", "### section (E): the import bar, the anchor bar, the pricing; each SINGLE-ARM with its floor."),
    ("sources quoted without a sha-256 of the bytes fetched", 0, 0, "sources", "### section (E) Bar 1."),
    ("quotations used without being located by the anchor tool", 0, 0, "quotations", "### section (E) Bar 2."),
    ("coordinates closed", 0, 0, "coordinates", "### section (F): in EVERY branch."),
    ("partition decisions", 0, 0, "decisions", "### section (F): the partition stays UNDECIDED."),
    ("faces equivalences compiled", 0, 0, "compilations", "### section (F)."),
    ("relay tools created", 3, 3, "files", "the extract, the read, and this act's suite."),
    ("owner instrument files edited", 0, 0, "files", "### none: reg_seal.py and ferry_scan.py gain ADDITIVE modes under ruling R3, and every banked seal still verifies."),
    ("PLACE-papers files written", 2, 2, "files", "### FACES_LEDGER.md (the uniformity row, through its writer) and ERRATA.md (ruling R2). ### THE HOOK AND THE MIRROR ARE OWED."),
    ("TECHNE files written", 0, 0, "files", "none."),
    ("correspondence rows appended", 2, 2, "rows", "### this act's row, and ruling R1's APPEND-ONLY correction row."),
    ("correspondence rows edited", 0, 0, "rows", "### RULING R1: the mis-attributing row itself is NOT edited."),
    ("faces ledger rows appended", 1, 1, "rows", "### the closing: the uniformity row's update, NAMED-ONLY unless a shape exists."),
    ("ERRATA entries filed", 1, 1, "entries", "### RULING R2: the routed entry, in the section the partition assigns it."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("frame recomputes", 0, 0, "runs", "### RULING R4: THE INSTRUMENT LANE IS PARKED. ### RE-MEASURED by G-RULINGS."),
    ("anchored-arm helpers built", 0, 0, "helpers", "### RULING R4: available mechanical work, UNSCHEDULED."),
    ("ledger rows moved", 0, 0, "rows", "section (I)."),
    ("bars moved", 0, 0, "bars", "section (I)."),
    ("grades conferred by a seat", 0, 0, "grades", "section (I)."),
    ("acts re-verdicted", 0, 0, "acts", "section (I)."),
    ("proofs attempted", 0, 0, "proofs", "section (A)."),
    ("new mathematics", 0, 0, "statements", "section (A)."),
    ("claims about the quantifier", 0, 0, "claims", "section (I)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "section (I)."),
    ("`.lean` files edited", 0, 0, "files", "none."),
    ("deposited texts touched", 0, 0, "files", "### none: the deposit is READ."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("mirror roster rows changed", 0, 0, "rows", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by `b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b357_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
    print('=' * 100)
    print('  counter source : %s' % os.path.basename(CNT.__file__))
    print('  ITS SELF-TEST, RUN HERE BEFORE IT IS TRUSTED:')
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
    clauses = [{"clause": c, "cap": cap, "demand": (n if dem is None else dem), "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": "data/b358_registration_2026-09-07.txt -- b358, THE LI ASYMPTOTICS, READ UNDER A CAP", "clauses": clauses}
    d = (json.dumps(spec, indent=1, ensure_ascii=False) + chr(10)).encode('utf-8')
    open(SPEC + '.tmp', 'wb').write(d)
    os.replace(SPEC + '.tmp', SPEC)
    back = json.load(io.open(SPEC, encoding='utf-8'))
    ok = (len(back['clauses']) == len(clauses) and all(str(c.get('from', '')).strip() for c in back['clauses']))
    unsat = [c['clause'] for c in back['clauses'] if c['demand'] > c['cap']]
    nonzero = [c['clause'] for c in back['clauses'] if c['cap'] != 0]
    print()
    print('  spec written and READ BACK : %s  clauses=%d  no empty provenance cell : %s' % (os.path.basename(SPEC), len(back['clauses']), ok))
    print('  ### CLAUSES WHOSE DEMAND EXCEEDS THEIR CAP : %d %s' % (len(unsat), unsat if unsat else ''))
    print('  ### ### **CAPS THAT ARE NOT ZERO : %d**' % len(nonzero))
    for c in nonzero:
        print('      %s' % c)
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
