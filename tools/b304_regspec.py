# -*- coding: utf-8 -*-
"""b304_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED** -- the standing design
### point, carried since b302.

### ### **AND IT FIRED ON THIS REGISTRATION'S OWN PROSE ON THE FIRST RUN**, exactly as it did at
### b302 (that act's D2). ### The phrase was *"the one Component 1 moves"*, in which a numeral
### governs the word `Component`. ### **THE PHRASE WAS REWRITTEN AND THE COUNTER WAS NOT WIDENED**
### -- widening a counter to let one's own sentence through is how a cap stops being a cap.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402  ### the counter is READ, never copied

REG = os.path.join(ROOT, 'data', 'b304_registration_2026-09-03.txt')
SPEC = os.path.join(ROOT, 'data', 'b304_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("`.lean` files created", 1, 1, "files",
     "THE ORDERED SHADOW: the one-level index-set fact, and only if it is finite-decidable AND"
     " carries its own scope. ### RE-MEASURED IN THE CLOSING BY `b304_checks.py`'s G-KERNEL."),
    ("`.lean` files modified", 1, 1, "files",
     "`AllPrints.lean` must import the module IN THE SAME COMMIT THAT CREATES IT (b289's scar)."
     " ### RE-MEASURED IN THE CLOSING."),
    ("profile files rewritten", 1, 1, "files",
     "`AXIOM_PRINTS.txt`, regenerated from source rather than copied (b298's D3)."
     " ### RE-MEASURED IN THE CLOSING."),
    ("byte-order marks prepended to the profile", 0, 0, "bytes",
     "b298's scar. ### RE-MEASURED BY READING THE FIRST BYTES AS BYTES."),
    ("pre-existing prints altered", 0, 0, "prints",
     "the pre-existing profile must survive BYTE-WISE AS A TRUE PREFIX against `git HEAD`."
     " ### RE-MEASURED IN THE CLOSING."),
    ("PLACE-papers files written", 0, 0, "files",
     "V13. ### RE-MEASURED IN THE CLOSING BY G-NOPAPERS, against this registration's own seal"
     " time."),
    ("ad-hoc shell-typed numbers", 0, 0, "count",
     "RULING (3) / `W-ORD-ADHOC-CHECK-FIXTURES`, and V14. ### RE-MEASURED BY G-TOOLNUM."),
    ("aggregations stated", 0, 0, "statements",
     "V9. ### `M-2` IS OWED AND STAYS OWED. ### RE-MEASURED BY G-NOAGG over this act's own"
     " emitted prose."),
    ("recommendations on the decision card", 0, 0, "recommendations",
     "V8. ### The card is assembled and routed; the choice is the author's."
     " ### RE-MEASURED BY G-CARD."),
    ("float tokens in a deciding runner", 0, 0, "tokens",
     "V14 and the standing exact-arithmetic rule. ### RE-MEASURED BY G-EXACT over the computation"
     " tool's own source and its emitted log."),
]


def main(argv):
    print('=' * 100)
    print('b304_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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

    clauses = [{"clause": c, "cap": cap, "demand": dem, "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    clauses.append({
        "clause": "artifact counts predicted in this registration",
        "cap": 0, "demand": n, "units": "predictions",
        "from": "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by the"
                " counter `b300_regspec.count_predictions`, IMPORTED rather than copied."
                " ### **IT FIRED ONCE ON THIS FILE'S OWN PROSE AND THE PROSE WAS REWRITTEN.**"})

    spec = {"registration":
            "data/b304_registration_2026-09-03.txt -- b304, THE DEMAND'S SHAPE",
            "clauses": clauses}
    d = (json.dumps(spec, indent=1, ensure_ascii=False) + '\n').encode('utf-8')
    open(SPEC + '.tmp', 'wb').write(d)
    os.replace(SPEC + '.tmp', SPEC)

    back = json.load(io.open(SPEC, encoding='utf-8'))
    ok = (len(back['clauses']) == len(clauses)
          and back['clauses'][-1]['demand'] == n
          and all(str(c.get('from', '')).strip() for c in back['clauses']))
    unsat = [c['clause'] for c in back['clauses'] if c['demand'] > c['cap']]
    nonzero = [c['clause'] for c in back['clauses'] if c['cap'] != 0]
    print()
    print('  spec written and READ BACK : %s  clauses=%d  no empty provenance cell : %s'
          % (os.path.basename(SPEC), len(back['clauses']), ok))
    print('  ### CLAUSES WHOSE DEMAND EXCEEDS THEIR CAP : %d %s'
          % (len(unsat), unsat if unsat else ''))
    print('  ### CAPS THAT ARE NOT ZERO (the ordered build\'s room) : %s' % ', '.join(nonzero))
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
