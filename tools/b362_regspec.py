# -*- coding: utf-8 -*-
"""b362_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**
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

REG = os.path.join(ROOT, 'data', 'b362_registration_2026-09-07.txt')
SPEC = os.path.join(ROOT, 'data', 'b362_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("deposit actions", 0, 0, "actions", "### section (A)/(K): nothing deposits, in every branch."),
    ("deposited artifacts touched", 0, 0, "files", "### section (K): the records are immutable at their versions."),
    ("quantities computed", 0, 0, "quantities", "### section (A) THE CAP: no computation. ### RE-MEASURED by G-NOCOMPUTE on STRIPPED code."),
    ("distances evaluated", 0, 0, "values", "### section (A) THE CAP: no value of the criterion's quantity at any index, by any route."),
    ("instruments built", 0, 0, "instruments", "### section (A) THE CAP: every tool here locates, pins, quotes or prints."),
    ("numerical bars on computed quantities", 0, 0, "bars", "### section (H): UNPRICED, and said so rather than left blank."),
    ("exact bars", 3, 3, "bars", "### section (H): the quotation bar, the pin bar, the unfolding bar."),
    ("multi-arm bars", 0, 0, "bars", "### section (H): every bar is marked SINGLE-ARM."),
    ("verdict branches", 3, 3, "branches", "### section (I): worth opening / no usable statement located / located but not worth opening."),
    ("branches left unclaimed", 0, 0, "branches", "### section (I): a branch not taken is shown unreachable (b350's rule)."),
    ("hints treated as sources", 0, 0, "hints", "### section (B): the navigator's hint is a search string and never a citation."),
    ("statuses available for the hint", 3, 3, "statuses", "### section (B): CONFIRMED / CORRECTED / NOT LOCATED."),
    ("sources quoted at first hand without a hash", 0, 0, "sources", "### section (C) BAR 2: every quoted source is fetched and hashed."),
    ("statements used to decide the structural question without their hypotheses unfolded", 0, 0,
     "statements", "### section (H) BAR 3: LOCATED-BUT-NOT-UNFOLDED is reported and is not used."),
    ("proofs verified", 0, 0, "proofs", "### section (C): the cap forbids constructing an argument, so no proof is verified."),
    ("work-orders opened", 0, None, "orders", "### section (C): only where an internal verification is tool-reachable, and naming one is not performing one."),
    ("registers adopted", 0, 0, "registers", "### section (A)/(K): the register is NOT adopted by this act."),
    ("faces promoted", 0, 0, "faces", "### section (A)/(K)."),
    ("faces ledger rows appended", 1, 1, "rows", "### section (G): ONE, through the writer, graded before the reading."),
    ("faces ledger rows rewritten", 0, 0, "rows", "### section (G): rows above are never rewritten."),
    ("grades conferred by a seat", 0, 0, "grades", "### section (G)/(K): the row carries NAMED-ONLY, or the import's own grade for the import and nothing else."),
    ("bridges typed between the rhyming obstructions", 0, 0, "bridges", "### section (E)/(G): none, in either direction."),
    ("equivalences compiled", 0, 0, "compilations", "### section (K): the deposit's own refusal is quoted at the deposited file."),
    ("circularity questions asked of each located statement", 3, 3, "questions", "### section (E): b358's three, carried by reference and quoted."),
    ("conditional and unconditional results merged", 0, 0, "merges", "### section (E): kept apart, and a result assuming the hypothesis is marked at full prominence."),
    ("pricings attempted", 0, 0, "pricings", "### section (F): NOT attempted; if it cannot be given, the pricing is priced."),
    ("PLACE-papers files written", 1, 1, "files", "### FACES_LEDGER.md and no other. ### THE HOOK AND THE MIRROR ARE OWED."),
    ("relay tools created", 5, 5, "files", "the regspec, the locate, the extract, the row writer and the suite; plus the ritual pair."),
    ("owner instrument files edited", 0, 0, "files", "none."),
    ("TECHNE files written", 0, 0, "files", "none."),
    ("mirror roster rows changed", 0, 0, "rows", "none by this act."),
    ("findings sections edited", 0, 0, "sections", "none."),
    ("HANDOFF.md edits", 0, 0, "edits", "none."),
    ("correspondence rows appended", 1, 1, "rows", "the closing."),
    ("index keys appended", 1, 1, "keys", "the closing."),
    ("ERRATA entries opened", 0, 0, "entries", "none by this act."),
    ("acts re-verdicted", 0, 0, "acts", "### section (K)."),
    ("ledger rows moved", 0, 0, "rows", "### section (K)."),
    ("bars moved", 0, 0, "bars", "### section (K)."),
    ("new mathematics", 0, 0, "statements", "### section (K)."),
    ("coordinates closed", 0, 0, "coordinates", "### section (K)."),
    ("claims about the quantifier", 0, 0, "claims", "### section (K)."),
    ("claims about h2, totality, the roster", 0, 0, "claims", "### section (K): the order's own refusal."),
    ("`.lean` files edited", 0, 0, "files", "none."),
    ("posture-lock changes", 0, 0, "changes", "### section (K): the posture lock is separate."),
    ("locked or sealed files edited", 0, 0, "files", "none."),
    ("frames recomputed", 0, 0, "frames", "### section (K): the instrument lane stays parked."),
    ("aggregations stated", 0, 0, "statements", "M-2 IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by `b300_regspec.count_predictions`, IMPORTED."),
]


def main(argv):
    print('=' * 100)
    print('b362_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b362_registration_2026-09-07.txt -- b362, THE APPROXIMATION REGISTER, READ UNDER A CAP",
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
