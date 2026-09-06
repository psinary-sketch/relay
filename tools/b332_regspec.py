# -*- coding: utf-8 -*-
"""b332_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.** ### Every clause is a forward
### commitment; the spec is emitted BEFORE any write into the papers.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b332_registration_2026-09-06.txt')
SPEC = os.path.join(ROOT, 'data', 'b332_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("PLACE-papers files written", 3, 3, "files", "### section (G): FINDINGS.md, FACES_LEDGER.md through the writer, the arc keystone by one appended line."),
    ("sections appended to FINDINGS.md", 1, 1, "sections", "### section (G): the stable anchor's section; idempotent on a second run."),
    ("ledger rows written", 1, 1, "rows", "### section (G): row S1, through the writer, quotations verified."),
    ("keystone lines appended", 1, 1, "lines", "### section (G): one cross-reference line; the keystone otherwise byte-identical."),
    ("keystone sentences edited or removed", 0, 0, "sentences", "### section (G); RE-MEASURED by G-ADDITIVE on the keystone."),
    ("proofs attempted", 0, 0, "proofs", "### section (A): a statement act."),
    ("grades moved or conferred", 0, 0, "grades", "### section (A): every grade from its emitting act."),
    ("acts re-verdicted", 0, 0, "acts", "section (A)."),
    ("numbers computed by this act", 0, 0, "numbers", "### every number banked by an owner and carried with it."),
    ("`.lean` files edited", 0, 0, "files", "none."),
    ("TECHNE files written", 0, 0, "files", "none."),
    ("deposited texts touched", 0, 0, "files", "the deposit is quoted, never written."),
    ("owner instrument files edited", 0, 0, "files", "### the writer and the owners' tools are imported or read, never edited."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows", "the append-only law; RE-MEASURED by G-ANCESTOR."),
    ("sealed files edited", 0, 0, "files", "none."),
    ("mirror roster rows changed", 0, 0, "rows", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("claims that the clause is discharged, weakened or replaced", 0, 0, "claims", "### section (A); must-fail fixtures on the opposite lines."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by `b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b332_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b332_registration_2026-09-06.txt -- b332, THE CLAUSE STATED", "clauses": clauses}
    d = (json.dumps(spec, indent=1, ensure_ascii=False) + '\n').encode('utf-8')
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
