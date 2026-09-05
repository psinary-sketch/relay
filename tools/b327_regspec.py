# -*- coding: utf-8 -*-
"""b327_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**
### ### **EVERY CLAUSE HERE IS A FORWARD COMMITMENT** (b325's lesson: a historical fact typed into this
### table makes it unsatisfiable by construction). ### The spec is emitted BEFORE any instrument runs.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b327_registration_2026-09-05.txt')
SPEC = os.path.join(ROOT, 'data', 'b327_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("instrument values seen before this seal", 0, 0, "values",
     "### section (0): the source's byte count, hash and page count are READS that pin an artefact and decide nothing."),
    ("grades moved", 0, 0, "grades", "F-G. ### section (1)."),
    ("faces promoted", 0, 0, "faces", "### section (1): a ledger row carries its own act's grade and no other's."),
    ("equivalences compiled, stated or implied", 0, 0, "equivalences",
     "### the deposit's refusal, quoted in the ledger's head; RE-MEASURED by G-NOEQUIV."),
    ("computations run", 2, 2, "computations",
     "### section (3): the corroboration of the derived map at n <= 30; section (4): the Fano count. ### A CAP, NOT A PREDICTION."),
    ("controls run", 0, 0, "controls", "### the fourth control is priced and not run, section (3)."),
    ("deposited texts touched", 0, 0, "files", "the deposit is read, never written."),
    ("`.lean` files created or edited", 0, 0, "files", "none."),
    ("owner instrument files edited", 0, 0, "files", "none; the bench is imported, not edited."),
    ("ledger rows written other than through the writer", 0, 0, "rows",
     "### section (2): every row goes through b327_faces_row.py or is not written."),
    ("blank cells in the ledger", 0, 0, "cells", "### section (2): NAMED-ONLY where nothing more is held; RE-MEASURED by the writer's read-back."),
    ("quoted fragments not verified against the emitter", 0, 0, "fragments",
     "### section (2): the writer verifies before writing; RE-MEASURED by G-QUOTE."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows", "the append-only law; RE-MEASURED by G-ANCESTOR."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("trails opened beyond the three named", 0, 0, "trails", "### section (5): W-ORD-LI-WEIL-BRIDGE, W-ORD-DISCRIMINATING-FAMILY, W-ORD-LI-FAMILY-CONTROL."),
    ("mirror roster rows changed", 0, 0, "rows", "### the new ledger is not added to the roster; that is the author's."),
    ("HANDOFF.md edits", 0, 0, "edits", "### the census counts it; nothing writes it."),
    ("tools writing one run file from two paths", 0, 0, "tools",
     "### structural since b324: two paths, two files."),
    ("result values typed into a deciding runner", 0, 0, "values", "### the bars live in the tools."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("sealed files edited", 0, 0, "files", "none."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by `b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b327_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    clauses = [{"clause": c, "cap": cap, "demand": (n if dem is None else dem),
                "units": u, "from": frm} for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": "data/b327_registration_2026-09-05.txt -- b327, THE FACES LEDGER, THE BRIDGE, AND TWO NOTES",
            "clauses": clauses}
    d = (json.dumps(spec, indent=1, ensure_ascii=False) + '\n').encode('utf-8')
    open(SPEC + '.tmp', 'wb').write(d)
    os.replace(SPEC + '.tmp', SPEC)
    back = json.load(io.open(SPEC, encoding='utf-8'))
    ok = (len(back['clauses']) == len(clauses)
          and all(str(c.get('from', '')).strip() for c in back['clauses']))
    unsat = [c['clause'] for c in back['clauses'] if c['demand'] > c['cap']]
    nonzero = [c['clause'] for c in back['clauses'] if c['cap'] != 0]
    print()
    print('  spec written and READ BACK : %s  clauses=%d  no empty provenance cell : %s'
          % (os.path.basename(SPEC), len(back['clauses']), ok))
    print('  ### CLAUSES WHOSE DEMAND EXCEEDS THEIR CAP : %d %s' % (len(unsat), unsat if unsat else ''))
    print('  ### ### **CAPS THAT ARE NOT ZERO : %d**' % len(nonzero))
    for c in nonzero:
        print('    ### %s' % c)
    print('  ### **THE ONE NONZERO CAP IS THE ACT\'S TWO COMPUTATIONS** -- the corroboration of a derived')
    print('  ### map and a count of Fano lines -- ### **A CAP ON WHAT THE ACT MAY RUN, NOT A PREDICTION.**')
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
