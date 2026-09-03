# -*- coding: utf-8 -*-
"""b309_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED** -- the standing design
### point, carried since b302.

### ### ### **AND THIS ACT IS THE FIRST SINCE b304 WHOSE CAPS ARE NOT ALL ZERO, WHICH IS THE ONE
### ### ### THING A SATISFIABILITY CHECK EXISTS TO CATCH GOING WRONG.**
### Two clauses carry a cap of ONE: a `.lean` module created, and the profile rewritten. ### The
### order's shadow clause permits a build ### **ONLY IF THE STATEMENT IS FINITE-DECIDABLE AND
### CARRIES ITS OWN SCOPE IN ITS OWN STATEMENT**, and b301's lesson is that a sealed cap must not
### forbid an ORDERED build. ### **A CAP OF ONE DOES NOT OBLIGE THE ACT TO WRITE ONE**: if either
### test fails, the cap is simply unused and b307's formula applies -- the act reports the find
### without building it.
### ### **THE DEMAND COLUMN FOR BOTH IS ZERO AT SEAL TIME AND IS RE-MEASURED IN THE CLOSING**, which
### is the only honest thing a spec can say about a build that has not happened yet.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402  ### the counter is READ, never copied

REG = os.path.join(ROOT, 'data', 'b309_registration_2026-09-03.txt')
SPEC = os.path.join(ROOT, 'data', 'b309_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("PLACE-papers files written", 0, 0, "files",
     "F9. ### A computation on the instrument files nothing to the papers repo."
     " ### RE-MEASURED BY G-NOPAPERS against `git status --porcelain` in that repository."),
    ("keystone files written", 0, 0, "files",
     "F9. ### No keystone is written or edited."),
    ("grades moved", 0, 0, "grades",
     "F10. ### A computation moves no grade, and a derivation of a zero moves none either."
     " ### RE-MEASURED BY G-NOMOVE."),
    ("acts re-verdicted", 0, 0, "acts",
     "F10. ### b304's refusal of the scaling part is CONTINUED, not overturned: it refused because"
     " the MODEL folds, and the model still folds. ### RE-MEASURED BY G-NOMOVE."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows",
     "the append-only law, F15. ### RE-MEASURED IN THE CLOSING BY A TRUE-PREFIX CHECK OF"
     " `CORRESPONDENCE.md` AGAINST `git HEAD`."),
    ("aggregations stated", 0, 0, "statements",
     "F8. ### `M-2` IS OWED AND STAYS OWED. ### RE-MEASURED BY G-NOMOVE and by the must-fail"
     " fixtures over this act's own emitted prose."),
    ("routes claimed", 0, 0, "claims",
     "THE ORDER: *NO claim that a nonzero value is a route*, and this act adds that a zero is not"
     " an anti-route either. ### RE-MEASURED BY the must-fail fixtures, which assert whole-line"
     " equality over the bank."),
    ("ad-hoc shell-typed numbers", 0, 0, "count",
     "RULING (3) / `W-ORD-ADHOC-CHECK-FIXTURES`, and F13. ### RE-MEASURED BY G-TOOLNUM."),
    ("float literals in the deciding runner", 0, 0, "tokens",
     "F7 / THE ORDER: *exact arithmetic in every verdict, zero float literals in the deciding"
     " runner*. ### RE-MEASURED BY G-EXACT, whose pattern is inherited from b308_checks AFTER that"
     " pattern's own two defects were found by its own fixtures."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK, F16. ### MEASURED off this registration's own text by the counter"
     " `b300_regspec.count_predictions`, IMPORTED rather than copied."),
    # ### ### **THE TWO THAT ARE NOT ZERO.**
    ("`.lean` modules created", 1, 0, "modules",
     "THE ORDER'S SHADOW CLAUSE: a build is permitted ONLY IF the statement is finite-decidable AND"
     " carries its own scope in its own statement, and the order says to CHECK that rather than"
     " assume it. ### b301: A SEALED CAP MUST NOT FORBID AN ORDERED BUILD. ### The demand is 0 at"
     " seal time and is RE-MEASURED IN THE CLOSING; if either test fails the cap is unused and the"
     " act reports the find without building it (b307's formula)."),
    ("profile files rewritten", 1, 0, "files",
     "the same clause: a module that is built must be PRINTED, or `COMPILED IS NOT CERTIFIED`"
     " (b289's incident). ### RE-MEASURED IN THE CLOSING; and F17 requires the baseline to"
     " regenerate BYTE-IDENTICALLY BEFORE anything is added, which was already shown at step zero"
     " (1.iv) -- 32850 bytes, 470 prints, all zero-axiom."),
]


def main(argv):
    print('=' * 100)
    print('b309_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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

    clauses = []
    for (c, cap, dem, u, frm) in CLAUSES:
        clauses.append({"clause": c, "cap": cap,
                        "demand": (n if dem is None else dem), "units": u, "from": frm})

    spec = {"registration":
            "data/b309_registration_2026-09-03.txt -- b309, THE SCALING TRACE",
            "clauses": clauses}
    d = (json.dumps(spec, indent=1, ensure_ascii=False) + '\n').encode('utf-8')
    open(SPEC + '.tmp', 'wb').write(d)
    os.replace(SPEC + '.tmp', SPEC)

    back = json.load(io.open(SPEC, encoding='utf-8'))
    ok = (len(back['clauses']) == len(clauses)
          and all(str(c.get('from', '')).strip() for c in back['clauses']))
    unsat = [c['clause'] for c in back['clauses'] if c['demand'] > c['cap']]
    nonzero = [c['clause'] for c in back['clauses'] if c['cap'] != 0]
    print()
    print('  spec written and READ BACK : %s  clauses=%d  no empty provenance cell : %s'
          % (os.path.basename(SPEC), len(back['clauses']), ok))
    print('  ### CLAUSES WHOSE DEMAND EXCEEDS THEIR CAP : %d %s'
          % (len(unsat), unsat if unsat else ''))
    print('  ### CAPS THAT ARE NOT ZERO : %s' % (', '.join(nonzero) if nonzero else 'NONE'))
    print('  ### **AND THAT IS THE FIRST NON-ZERO CAP SINCE b304.** ### It exists because the')
    print('  ### order conditions a build on two tests and says to CHECK them rather than assume')
    print('  ### them. ### **A CAP OF ONE DOES NOT OBLIGE THE ACT TO WRITE ONE.**')
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
