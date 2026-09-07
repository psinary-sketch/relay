# -*- coding: utf-8 -*-
"""b350_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b350_registration_2026-09-07.txt')
SPEC = os.path.join(ROOT, 'data', 'b350_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("frames built", 0, 0, "frames", "### section (A): no frame is built and nothing is re-run."),
    ("ladders run", 0, 0, "ladders", "section (A)."),
    ("cells evaluated", 0, 0, "cells", "section (A)."),
    ("axes moved", 0, 0, "axes", "### section (A): pricing an axis is not moving it."),
    ("banked figures re-computed", 0, 0, "figures", "### section (C): b344's printed values are read."),
    ("relay tools created", 2, 2, "files", "the pricing tool and this act's suite."),
    ("owner instrument files edited", 0, 0, "files", "none."),
    ("PLACE-papers files written", 1, 1, "files", "### section (G): OPEN_TRAILS.md, one appended block, only if the trail's state changes."),
    ("TECHNE files written", 0, 0, "files", "none."),
    ("correspondence rows appended", 1, 1, "rows", "### section (G)."),
    ("ERRATA entries opened", 0, 0, "entries", "none."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("bars moved", 0, 0, "bars", "section (A)."),
    ("acts re-verdicted", 0, 0, "acts", "section (A)."),
    ("grades conferred by a seat", 0, 0, "grades", "section (A)."),
    ("proofs attempted", 0, 0, "proofs", "section (A)."),
    ("new mathematics", 0, 0, "statements", "section (A)."),
    ("claims about the residual's response", 0, 0, "claims", "### section (C): not priced by the printed figures."),
    ("claims about the quantifier", 0, 0, "claims", "section (H)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "section (H)."),
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
    print('b350_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b350_registration_2026-09-07.txt -- b350, THE LI CONTROL, RE-RUN", "clauses": clauses}
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
