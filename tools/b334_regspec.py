# -*- coding: utf-8 -*-
"""b334_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.** ### Every clause is a forward
### commitment; the spec is emitted BEFORE any seed is built.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b334_registration_2026-09-06.txt')
SPEC = os.path.join(ROOT, 'data', 'b334_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("PLACE-papers files written", 1, 1, "files", "### section (I): FACES_LEDGER.md by one appended block through the writer."),
    ("ledger rows written", 0, 0, "rows", "### section (I): an update block, not a row."),
    ("findings sections edited", 0, 0, "sections", "### section (I): none."),
    ("correspondence rows appended", 2, 2, "rows", "### section (I): the map for zeta with the chart; the Epstein control charted with the softness."),
    ("grades conferred by this act", 0, 0, "grades", "### section (A): a behaviour over aims, not a grade."),
    ("proofs attempted", 0, 0, "proofs", "section (A)."),
    ("new mathematics", 0, 0, "statements", "section (A)."),
    ("numbers reported by one route", 0, 0, "numbers", "### section (E): two routes each; the remainder's two quadratures declared a limit."),
    ("claims about the quantifier", 0, 0, "claims", "### section (K): K8 stays unowned; must-fail fixture."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "### section (K)."),
    ("acts re-verdicted", 0, 0, "acts", "section (A)."),
    ("`.lean` files edited", 0, 0, "files", "none."),
    ("TECHNE files written", 0, 0, "files", "none."),
    ("deposited texts touched", 0, 0, "files", "none."),
    ("owner instrument files edited", 0, 0, "files", "### every instrument imported, never edited."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows", "the append-only law; RE-MEASURED by G-ANCESTOR."),
    ("sealed files edited", 0, 0, "files", "none."),
    ("mirror roster rows changed", 0, 0, "rows", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("aims or widths added after a value", 0, 0, "aims", "### section (D): NO AIM, NO WIDTH IS ADDED OR MOVED AFTER A NUMBER IS SEEN."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by `b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b334_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b334_registration_2026-09-06.txt -- b334, THE AIM-MAP", "clauses": clauses}
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
