# -*- coding: utf-8 -*-
"""b305_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED** -- the standing design
### point, carried since b302.

### ### **AND THIS ACT'S CAPS ARE ALL ZEROS, WHICH IS THE ORDER'S DOING AND NOT THIS SEAT'S.** ###
### b301's lesson was that a sealed cap must not forbid an ### ORDERED ### build; here the order
### says ### *"nothing built"* ### and expects the shadow to be nothing, so zero forbids nothing
### that was asked for. ### **IF THE SHADOW CHECK FINDS SOMETHING BUILDABLE, THE CAP HOLDS AND THE
### ACT REPORTS THE FIND WITHOUT BUILDING IT.**
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402  ### the counter is READ, never copied

REG = os.path.join(ROOT, 'data', 'b305_registration_2026-09-03.txt')
SPEC = os.path.join(ROOT, 'data', 'b305_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("`.lean` files created", 0, 0, "files",
     "THE ORDER: *nothing built*, and the shadow is expected to be nothing."
     " ### RE-MEASURED IN THE CLOSING BY `b305_checks.py`'s G-NOBUILD."),
    ("`.lean` files modified", 0, 0, "files",
     "THE ORDER: nothing built. ### RE-MEASURED IN THE CLOSING."),
    ("profile files rewritten", 0, 0, "files",
     "`AXIOM_PRINTS.txt` does not move this act. ### RE-MEASURED IN THE CLOSING AGAINST"
     " `git HEAD`, BYTE-WISE."),
    ("PLACE-papers files written", 0, 0, "files",
     "G9. ### RE-MEASURED IN THE CLOSING BY G-NOPAPERS, against this registration's own seal"
     " time."),
    ("ad-hoc shell-typed numbers", 0, 0, "count",
     "RULING (3) / `W-ORD-ADHOC-CHECK-FIXTURES`, and G12. ### RE-MEASURED BY G-TOOLNUM."),
    ("aggregations stated", 0, 0, "statements",
     "G5. ### `M-2` IS OWED AND STAYS OWED. ### RE-MEASURED BY G-NOAGG over this act's own"
     " emitted prose."),
    ("analogies to the corpus's objects drawn in Component 1", 0, 0, "analogies",
     "G2, and it is the order's own restriction: a reading made while the comparison is being"
     " drawn is no longer independent of it. ### RE-MEASURED BY G-NOANALOGY, scoped to"
     " Component 1's own text."),
    ("recommendations to build the instrument", 0, 0, "recommendations",
     "THE ORDER: the instrument is PRICED, not built, and a price is not an approval."
     " ### RE-MEASURED BY G-PRICE."),
]


def main(argv):
    print('=' * 100)
    print('b305_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
                " counter `b300_regspec.count_predictions`, IMPORTED rather than copied."})

    spec = {"registration":
            "data/b305_registration_2026-09-03.txt -- b305, WHERE THE ARITHMETIC ENTERS",
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
    print('  ### CAPS THAT ARE NOT ZERO : %s'
          % (', '.join(nonzero) if nonzero else 'NONE -- the order builds nothing this act'))
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
