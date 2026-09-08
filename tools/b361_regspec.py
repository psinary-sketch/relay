# -*- coding: utf-8 -*-
"""b361_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b361_registration_2026-09-07.txt')
SPEC = os.path.join(ROOT, 'data', 'b361_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (A): nothing deposits, in every branch."),
    ("network calls to any platform", 0, 0, "calls", "### section (A): this act makes none. ### RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("deposited artifacts touched", 0, 0, "files", "### section (H): the records are immutable at their versions."),
    ("objects located and quoted", 4, 4, "objects", "### section (B): the item, its grade, the cap clause, the draft's parking claim."),
    ("objects paraphrased rather than located", 0, 0, "objects", "### section (B): a thing not located is reported as not located."),
    ("quotations typed from recollection", 0, 0, "quotations", "### section (A-PRE): every quotation is the anchor tool's output."),
    ("values supplied from recollection", 0, 0, "values", "### section (D) BAR 2: recollection is never a source for a value."),
    ("branch tests", 2, 2, "branches", "### section (C): DECIDE / HALT, fixed before any file is opened."),
    ("branches left unclaimed", 0, 0, "branches", "### section (F): the branch not taken is shown unreachable (b350's rule)."),
    ("instrument frames built or recomputed", 0, 0, "frames", "### section (C)/(H): the instrument lane stays parked."),
    ("ladders run", 0, 0, "ladders", "### section (C)."),
    ("quadrature axes moved", 0, 0, "axes", "### section (C)."),
    ("transforms, quadratures, fits or series evaluated", 0, 0, "evaluations", "### section (C)."),
    ("new measurements made", 0, 0, "measurements", "### section (C): a substitution from a located definition is not a measurement."),
    ("stated substitutions permitted", 1, None, "steps", "### section (C)/(D) BAR 3: at most one, printed with its route and what the route is deaf to."),
    ("numerical bars on computed quantities", 0, 0, "bars", "### section (D): UNPRICED, and said so rather than left blank."),
    ("exact bars", 3, 3, "bars", "### section (D): the quotation bar, the definition bar, the route bar."),
    ("multi-arm bars", 0, 0, "bars", "### section (D): every bar is marked SINGLE-ARM."),
    ("constants evaluated without their definition located at content", 0, 0, "constants",
     "### section (D) BAR 2: a definition inferred from the shape of something else is not a definition."),
    ("PLACE-papers files written", 0, None, "files",
     "### section (E): the faces ledger IF AND ONLY IF the decision moves the row; the hook and the mirror follow that."),
    ("faces ledger rows rewritten", 0, 0, "rows", "### section (E): an update names the row it bears on; nothing above is edited."),
    ("relay tools created", 5, 5, "files", "the regspec, the extract, the reader, the correspondence and the suite."),
    ("owner instrument files edited", 0, 0, "files", "none."),
    ("TECHNE files written", 0, 0, "files", "none."),
    ("mirror roster rows changed", 0, 0, "rows", "none by this act."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("routed items opened", 0, 0, "items", "none but the one the order names."),
    ("equivalences compiled", 0, 0, "compilations", "### section (H): nothing compiled, no bridge typed."),
    ("acts re-verdicted", 0, 0, "acts", "### section (H): b345's precedent -- a new step is not a correction."),
    ("grades conferred by a seat", 0, 0, "grades", "### section (A)/(H)."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("ledger rows moved", 0, 0, "rows", "### section (H)."),
    ("bars moved", 0, 0, "bars", "### section (H)."),
    ("proofs attempted", 0, 0, "proofs", "### section (H)."),
    ("new mathematics", 0, 0, "statements", "### section (H)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (H)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (H)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "### section (H): the order's own refusal."),
    ("changes to the circularity finding", 0, 0, "changes", "### section (H): it stands untouched in either branch."),
    ("`.lean` files edited", 0, 0, "files", "none."),
    ("posture-lock changes", 0, 0, "changes", "### section (H): the posture lock is separate."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by `b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b361_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b361_registration_2026-09-07.txt -- b361, THE HELD ITEM, QUOTED THEN BRANCHED",
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
