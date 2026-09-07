# -*- coding: utf-8 -*-
"""b352_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b352_registration_2026-09-07.txt')
SPEC = os.path.join(ROOT, 'data', 'b352_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("frames built", 0, 0, "frames", "### section (A): a REFIT from figures already banked."),
    ("instruments run", 0, 0, "instruments", "section (A)."),
    ("residuals recomputed", 0, 0, "residuals", "### section (H): G-NOREBUILD, byte-equal to b339's banked array."),
    ("ladders extended", 0, 0, "ladders", "section (A)."),
    ("acts re-verdicted", 0, 0, "acts", "### section (J): b339, b346, b350 and b351 all stand."),
    ("models fitted", 3, 3, "models", "### section (C): M1 (k=2), M2 (k=3), M3 (k=3), forms fixed before any fit."),
    ("models fitted with four or more parameters", 0, 0, "models", "### section (C): unscoreable at n = 5, and stated rather than fitted."),
    ("fitting criteria", 1, 1, "criteria", "### section (D): one criterion for all three, least squares on log R."),
    ("numerical bars", 2, 2, "bars", "### section (E): both carry the object's floor of 5e-10 absolute."),
    ("bars whose floor is unstated", 0, 0, "bars", "section (E)."),
    ("relay tools created", 3, 3, "files", "the extract, the fit, and this act's suite."),
    ("owner instrument files edited", 1, 1, "files", "### section (G): registration_gate.py gains the straddle arm by APPENDED code."),
    ("PLACE-papers files written", 1, 1, "files", "### section (G): one appended work-order block."),
    ("TECHNE files written", 1, 1, "files", "### section (G): the straddling-gate module, LOCAL-ONLY and not pushed."),
    ("TECHNE files pushed", 0, 0, "files", "none, as every module since b330."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("ledger rows moved", 0, 0, "rows", "### section (J): this act moves none."),
    ("bars moved", 0, 0, "bars", "section (J)."),
    ("grades conferred by a seat", 0, 0, "grades", "section (J)."),
    ("proofs attempted", 0, 0, "proofs", "section (A)."),
    ("new mathematics", 0, 0, "statements", "section (A)."),
    ("side-readings withdrawn", 0, 0, "readings", "### section (F): b339 labelled it its own seat's, and this act does not overturn it."),
    ("claims that a fit is a fact about the object", 0, 0, "claims", "### section (J): a fit describes five numbers."),
    ("claims about the quantifier", 0, 0, "claims", "section (J)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "section (J)."),
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
    print('b352_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b352_registration_2026-09-07.txt -- b352, THE FLOOR'S FOURTH CANDIDATE", "clauses": clauses}
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
