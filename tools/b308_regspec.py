# -*- coding: utf-8 -*-
"""b308_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED** -- the standing design
### point, carried since b302. ### A copied counter drifts from the one the ruling names, and the
### drift is invisible because both files still run.

### ### **THIS ACT'S CAPS ARE ALL ZEROS, AND TWO OF THEM ARE NEW.**
###   ### **`float tokens in a deciding path`** -- the order says exact arithmetic in every
###     verdict, and a float that reaches a verdict is not a rounding question, it is a different
###     instrument.
###   ### **`first-level values at unbanked cells`** -- the order scopes this act to a build and
###     its reproduction, and puts the first computation on the new instrument in a LATER act under
###     its own registration. ### **A ZERO CAP HERE IS THE ORDER'S, NOT THIS SEAT'S.**
### ### b301's lesson holds at both: a sealed cap must not forbid an ### ORDERED ### build, and
### neither of these forbids anything the order asked for.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402  ### the counter is READ, never copied

REG = os.path.join(ROOT, 'data', 'b308_registration_2026-09-03.txt')
SPEC = os.path.join(ROOT, 'data', 'b308_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("`.lean` files created", 0, 0, "files",
     "F8 / THE ORDER: nothing is compiled this act."
     " ### RE-MEASURED IN THE CLOSING BY `b308_checks.py`'s G-NOBUILD."),
    ("`.lean` files modified", 0, 0, "files",
     "F8. ### RE-MEASURED IN THE CLOSING."),
    ("profile files rewritten", 0, 0, "files",
     "F8. ### `AXIOM_PRINTS.txt` does not move this act. ### RE-MEASURED IN THE CLOSING AGAINST"
     " `git HEAD`, BYTE-WISE -- not line by line, which is how b298's byte-order mark passed two"
     " checks at once."),
    ("PLACE-papers files written", 0, 0, "files",
     "F9. ### An instrument build files nothing to the papers repo. ### RE-MEASURED BY G-NOPAPERS"
     " against `git status --porcelain` in that repository."),
    ("ad-hoc shell-typed numbers", 0, 0, "count",
     "RULING (3) / `W-ORD-ADHOC-CHECK-FIXTURES`, and F13. ### RE-MEASURED BY G-TOOLNUM."),
    ("aggregations stated", 0, 0, "statements",
     "`M-2` IS OWED AND STAYS OWED. ### RE-MEASURED BY G-NOMOVE and by the must-fail fixtures over"
     " this act's own emitted prose."),
    ("grades moved", 0, 0, "grades",
     "AN INSTRUMENT BUILD MOVES NO GRADE, AND REPRODUCING A BANKED RESULT DOES NOT RAISE IT."
     " ### RE-MEASURED BY G-NOMOVE."),
    ("acts re-verdicted", 0, 0, "acts",
     "AN INSTRUMENT BUILD RE-VERDICTS NOTHING. ### RE-MEASURED BY G-NOMOVE."),
    ("keystone files written", 0, 0, "files",
     "F9. ### No keystone is written or edited; b299's arc keystone is not touched."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows",
     "the append-only law, F15. ### RE-MEASURED IN THE CLOSING BY A TRUE-PREFIX CHECK OF"
     " `CORRESPONDENCE.md` AGAINST `git HEAD`."),
    ("float tokens in a deciding path", 0, 0, "tokens",
     "F6 / THE ORDER: *exact arithmetic in every verdict*. ### RE-MEASURED BY G-EXACT, which scans"
     " the instrument's own source for float literals and float-producing operators and prints the"
     " sites it excuses with its reason."),
    ("first-level values at unbanked cells", 0, 0, "values",
     "F7 / THE ORDER: *NO first-level value computed on the new instrument*, that being a later act"
     " under its own registration. ### RE-MEASURED BY G-NONEW, which requires every printed value"
     " to carry the owning tool that also produces it."),
]


def main(argv):
    print('=' * 100)
    print('b308_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
        "from": "RULING (1), U-1 STRUCK, F16. ### MEASURED off this registration's own text by the"
                " counter `b300_regspec.count_predictions`, IMPORTED rather than copied."})

    spec = {"registration":
            "data/b308_registration_2026-09-03.txt -- b308, THE LOCAL-FIELD INSTRUMENT, ACT ONE",
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
          % (', '.join(nonzero) if nonzero else
             'NONE -- the order builds an instrument and files nothing else'))
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
