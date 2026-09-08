# -*- coding: utf-8 -*-
"""b363_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.** ### Every clause is a forward
### commitment; the spec is emitted BEFORE the registration is locked and before any read of this act.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b363_registration_2026-09-07.txt')
SPEC = os.path.join(ROOT, 'data', 'b363_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (A)/(J): nothing deposits, in every branch."),
    ("network calls to any platform", 0, 0, "calls", "### section (A): this act makes none."),
    ("deposited artifacts touched", 0, 0, "files", "### section (J)."),
    ("quantities computed about the object", 0, 0, "quantities",
     "### section (G): no frame, seed, transform, quadrature, fit, score or series. ### RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("numerical bars on computed quantities", 0, 0, "bars", "### section (G): UNPRICED, and said so rather than left blank."),
    ("exact bars", 3, 3, "bars", "### section (G): the enumeration bar, the fixture bar, the reproduction bar."),
    ("multi-arm bars", 0, 0, "bars", "### section (G): every bar is marked SINGLE-ARM."),
    ("verdict branches", 3, 3, "branches", "### section (H): built / built and narrower than its rule / unaffordable."),
    ("branches left unclaimed", 0, 0, "branches", "### section (H): a branch not taken is shown unreachable (b350's rule)."),
    ("counts predicted for the census in this registration", 0, 0, "counts",
     "### section (B): the count is the act's evidence and a registration that named a figure would score its own draft against itself."),
    ("arms counted from memory rather than located at a bank", 0, 0, "arms",
     "### section (G) BAR 1: an arm not located is reported as not located."),
    ("classification values available", 2, 2, "values", "### section (C): RETIRED BY THE HELPER / NOT RETIRED, each with its reason."),
    ("classifications inferred by a scanner", 0, 0, "classifications",
     "### section (C): DECLARED DATA, arm by arm -- b357's cure, and the right one here."),
    ("species the helper is claimed to reach that it does not", 0, 0, "species",
     "### section (D): a wrong arm and a missing sentence are both named as OUT of reach."),
    ("shared utilities created", 1, 1, "files", "### section (D): the helper, written once, with fixtures in both polarities."),
    ("banked suites edited", 0, 0, "files", "### section (E)/(J): NOT ONE. ### The helper is exercised against COPIES."),
    ("copies whose verdict is adjusted rather than reported", 0, 0, "copies",
     "### section (E): a copy that does not reproduce is reported at full prominence."),
    ("trail entries appended", 1, 1, "entries", "### section (F): one, under its own mark, append-only."),
    ("trail entries attempted", 0, 0, "entries", "### section (F): FILED, NOT RUN. ### Naming a read is not performing one."),
    ("grades opened or moved by the trail entry", 0, 0, "grades", "### section (F)/(J): b358's grade stands and b361's decision stands."),
    ("PLACE-papers files written", 1, 1, "files", "### OPEN_TRAILS.md and no other. ### THE HOOK AND THE MIRROR ARE OWED."),
    ("faces ledger rows appended or rewritten", 0, 0, "rows", "### the closing: the writer runs only if a row moves, and none does."),
    ("relay tools created", 5, 5, "files", "the regspec, the extract, the helper, the census-and-control runner, and this act's suite; plus the ritual pair."),
    ("owner instrument files edited", 0, 0, "files", "none. ### The helper is NEW, not an edit to an existing one."),
    ("TECHNE files written", 0, 0, "files", "none."),
    ("mirror roster rows changed", 0, 0, "rows", "none by this act."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("acts re-verdicted", 0, 0, "acts", "### section (J): b358, b360, b361 and b362 stand as banked."),
    ("equivalences compiled", 0, 0, "compilations", "### section (J): nothing compiled, no bridge typed."),
    ("ledger rows moved", 0, 0, "rows", "### section (J)."),
    ("bars moved", 0, 0, "bars", "### section (J)."),
    ("grades conferred by a seat", 0, 0, "grades", "### section (J)."),
    ("new mathematics", 0, 0, "statements", "### section (J)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (J)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (J)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "### section (J): the order's own refusal."),
    ("`.lean` files edited", 0, 0, "files", "none."),
    ("posture-lock changes", 0, 0, "changes", "### section (J)."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (J): the instrument lane stays parked."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by `b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b363_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    clauses = [{"clause": c, "cap": cap, "demand": (n if (dem is None and c.startswith('artifact counts')) else
                                                    (cap if dem is None else dem)),
                "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    spec = {"registration": "data/b363_registration_2026-09-07.txt -- b363, THE ANCHORED GATE ARMS",
            "clauses": clauses}
    d = (json.dumps(spec, indent=1, ensure_ascii=False) + chr(10)).encode('utf-8')
    open(SPEC + '.tmp', 'wb').write(d)
    os.replace(SPEC + '.tmp', SPEC)
    back = json.load(io.open(SPEC, encoding='utf-8'))
    ok = (len(back['clauses']) == len(clauses) and all(str(c.get('from', '')).strip() for c in back['clauses']))
    unsat = [c['clause'] for c in back['clauses'] if c['demand'] > c['cap']]
    nonzero = [c['clause'] for c in back['clauses'] if c['cap'] != 0]
    print()
    print('  spec written and READ BACK : %s  clauses=%d  no empty provenance cell : %s'
          % (os.path.basename(SPEC), len(back['clauses']), ok))
    print('  ### CLAUSES WHOSE DEMAND EXCEEDS THEIR CAP : %d %s' % (len(unsat), unsat if unsat else ''))
    print('  ### ### **CAPS THAT ARE NOT ZERO : %d**' % len(nonzero))
    for c in nonzero:
        print('      %s' % c)
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
