# -*- coding: utf-8 -*-
"""b329_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.** ### Every clause is a forward
### commitment; the spec is emitted BEFORE any build runs.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b329_registration_2026-09-05.txt')
SPEC = os.path.join(ROOT, 'data', 'b329_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("`.lean` modules created", 1, 1, "files", "### section (7): the order's own build clause; the baseline at (1)(vi) ran before this cap was written."),
    ("`.lean` files edited other than the new module and AllPrints.lean", 0, 0, "files", "### section (7)."),
    ("AllPrints.lean edits", 1, 1, "edits", "### section (7): one append-only edit, import after the last import, prints at the end."),
    ("profile files rewritten", 1, 1, "files", "### section (7): AXIOM_PRINTS.txt regenerated from source, the banked profile a true byte prefix."),
    ("axioms in any terminal", 0, 0, "axioms", "### section (3): zero-axiom target at the audit bar."),
    ("sorry / native_decide / axiom / lemma / import in the module", 0, 0, "forms", "### section (3): measured by the kernel tool with comments stripped."),
    ("theorems without a citing act", 0, 0, "theorems", "### section (3): every docstring names b304, b309 or b310."),
    ("new mathematics", 0, 0, "statements", "### section (3): a bar that resists is declared NOT MET, not proved by new means."),
    ("PLACE-papers files written", 1, 1, "files", "### section (7): FACES_LEDGER.md through the writer's append_block."),
    ("ledger rows written other than through the writer", 0, 0, "rows", "### section (3)."),
    ("deposited texts touched", 0, 0, "files", "the deposit is read, never written."),
    ("owner instrument files edited", 0, 0, "files", "### b302's byte checks imported, never edited."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows", "the append-only law; RE-MEASURED by G-ANCESTOR."),
    ("grades moved", 0, 0, "grades", "section (2)."),
    ("acts re-verdicted", 0, 0, "acts", "section (2)."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("claims about the archimedean place", 0, 0, "claims", "### section (2)(B): the mechanism does not type there."),
    ("sealed files edited", 0, 0, "files", "none."),
    ("mirror roster rows changed", 0, 0, "rows", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("float literals anywhere in this act", 0, 0, "literals", "### section (3): exact arithmetic in every verdict."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by `b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b329_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b329_registration_2026-09-05.txt -- b329, THE FINITE-SIDE SEAL", "clauses": clauses}
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
    print('  ### each non-zero cap is the order\'s own build clause, and the baseline ran before it was written.')
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
