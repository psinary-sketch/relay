# -*- coding: utf-8 -*-
"""b351_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b351_registration_2026-09-07.txt')
SPEC = os.path.join(ROOT, 'data', 'b351_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("partitions constructed", 0, 0, "partitions", "### section (A): the order's ceiling, quoted."),
    ("classes proved silent", 0, 0, "classes", "### section (A): the order's ceiling, quoted."),
    ("new instruments written", 0, 0, "instruments", "section (A)."),
    ("computations beyond what is banked", 0, 0, "computations", "### section (A): every figure in this act is a quotation."),
    ("transforms evaluated", 0, 0, "transforms", "section (E): this act computes nothing."),
    ("rooms computed", 0, 0, "rooms", "section (E)."),
    ("residuals computed", 0, 0, "residuals", "section (E)."),
    ("phases computed", 0, 0, "phases", "section (E)."),
    ("seeds built", 0, 0, "seeds", "section (E)."),
    ("numerical bars on computed quantities", 0, 0, "bars", "### section (E): there is no number for a floor to be the floor of."),
    ("textual bars", 1, 1, "bars", "### section (E): exact match after normalisation, marked SINGLE-ARM."),
    ("coordinates reported", 4, 4, "coordinates", "### section (B): abscissa, height, phase, width -- all four, none merged."),
    ("units reported per coordinate", 3, 3, "units", "section (C): the charted range, the bound state, the class."),
    ("bound states available", 3, 3, "states", "section (C): BOUNDED BY AN ARGUMENT / BOUNDED BY A MEASUREMENT / NOT BOUNDED."),
    ("relay tools created", 2, 2, "files", "the reading tool and this act's suite."),
    ("owner instrument files edited", 0, 0, "files", "none."),
    ("PLACE-papers files written", 0, 0, "files", "### none: this act files nothing, so the hook and the mirror are NOT owed."),
    ("TECHNE files written", 0, 0, "files", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("ledger rows moved", 0, 0, "rows", "### section (H): this act moves none."),
    ("bars moved", 0, 0, "bars", "section (H)."),
    ("acts re-verdicted", 0, 0, "acts", "section (H)."),
    ("grades conferred by a seat", 0, 0, "grades", "section (H)."),
    ("proofs attempted", 0, 0, "proofs", "section (A)."),
    ("new mathematics", 0, 0, "statements", "section (A)."),
    ("claims that a class IS silent", 0, 0, "claims", "### section (F): G-NOSILENCE, with four must-fail fixtures."),
    ("claims about the quantifier", 0, 0, "claims", "section (H)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "section (H)."),
    ("wall times borrowed from different work", 0, 0, "times", "### section (D): a borrowed time is not a price."),
    ("`.lean` files edited", 0, 0, "files", "none."),
    ("deposited texts touched", 0, 0, "files", "none."),
    ("sealed files edited", 0, 0, "files", "none."),
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
    print('b351_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b351_registration_2026-09-07.txt -- b351, THE PARTITION QUESTION", "clauses": clauses}
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
