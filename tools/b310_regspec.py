# -*- coding: utf-8 -*-
"""b310_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED** -- the standing design
### point, carried since b302.

### ### ### **THE TWO CAPS THAT MATTER THIS ACT ARE NEW, AND THEY ARE ZERO: ### `branch decisions`
### ### ### AND `verdicts on M-2`.** ### Component 4 touches a branch nobody has settled and a
### specification the corpus owes, and ### **A CAP OF ZERO ON EACH IS THE CHEAPEST HONEST GUARD
### AGAINST THIS ACT'S MOST TEMPTING OVERREACH.** ### Their demand is measured by must-fail
### fixtures over the act's own emitted prose, not by the seat's assurance.
### ### **TWO CAPS ARE ONE, FOR THE SAME REASON AS b309's**: the order's shadow clause permits a
### build only if two tests pass, and b301's lesson is that a sealed cap must not forbid an ORDERED
### build. ### **A CAP OF ONE DOES NOT OBLIGE THE ACT TO WRITE ONE.**
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402  ### the counter is READ, never copied

REG = os.path.join(ROOT, 'data', 'b310_registration_2026-09-03.txt')
SPEC = os.path.join(ROOT, 'data', 'b310_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("PLACE-papers files written", 0, 0, "files",
     "F8. ### RE-MEASURED BY G-NOPAPERS against `git status --porcelain` in that repository."),
    ("keystone files written", 0, 0, "files",
     "F8. ### No keystone is written or edited."),
    ("grades moved", 0, 0, "grades",
     "F9. ### RE-MEASURED BY G-NOMOVE over this act's own emitted prose."),
    ("acts re-verdicted", 0, 0, "acts",
     "F9. ### b309's zero is CARRIED, not re-derived; b304's compact-part zero is GENERALISED, not"
     " overturned. ### RE-MEASURED BY G-NOMOVE."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows",
     "the append-only law, F14. ### RE-MEASURED BY A TRUE-PREFIX CHECK AGAINST `git HEAD`."),
    ("aggregations stated", 0, 0, "statements",
     "`M-2` IS OWED AND STAYS OWED. ### RE-MEASURED BY G-NOBRANCH and the must-fail fixtures."),
    ("branch decisions", 0, 0, "decisions",
     "### **NEW THIS ACT.** ### b262's disjunction is undecided and this act does not decide it."
     " ### b262's own sentence is a statement about what the archimedean side is REQUIRED to do and"
     " expressly NOT a claim that it fails to do it. ### RE-MEASURED BY G-NOBRANCH, whose must-fail"
     " fixtures assert whole-line equality over the bank."),
    ("verdicts on M-2", 0, 0, "verdicts",
     "### **NEW THIS ACT.** ### Component 4 restates the SCOPE of a specification. ### A"
     " specification whose first property is out of reach for ONE CLASS of candidate is not a"
     " specification shown unsatisfiable. ### RE-MEASURED BY G-NOBRANCH."),
    ("routes claimed", 0, 0, "claims",
     "carried from b309: a value is a value, and a zero is neither a route nor an anti-route."),
    ("comparisons to a target", 0, 0, "comparisons",
     "THE ORDER: *NO comparison to any target and no fit*; the corpus's prime sum and b262's mass"
     " are named as CONTEXT ONLY. ### RE-MEASURED BY the must-fail fixtures."),
    ("ad-hoc shell-typed numbers", 0, 0, "count",
     "RULING (3) / `W-ORD-ADHOC-CHECK-FIXTURES`, and F12. ### RE-MEASURED BY G-TOOLNUM."),
    ("float literals in the deciding runner", 0, 0, "tokens",
     "F6. ### RE-MEASURED BY G-EXACT, the pattern inherited from b308_checks AFTER its own two"
     " defects were found by its own fixtures."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK, F15. ### MEASURED off this registration's own text by the counter"
     " `b300_regspec.count_predictions`, IMPORTED rather than copied."),
    ("`.lean` modules created", 1, 0, "modules",
     "THE ORDER'S SHADOW CLAUSE, permitting a build ONLY IF the statement is finite-decidable AND"
     " carries its own scope in its statement, and saying to CHECK that. ### b301: A SEALED CAP MUST"
     " NOT FORBID AN ORDERED BUILD. ### Demand 0 at seal time, RE-MEASURED IN THE CLOSING."),
    ("profile files rewritten", 1, 0, "files",
     "the same clause: a module that is built must be PRINTED, or `COMPILED IS NOT CERTIFIED`"
     " (b289). ### F16 requires the baseline to regenerate BYTE-IDENTICALLY first, and the prefix"
     " check to NORMALISE and to FIND its baseline rather than assume `HEAD` -- b309's (D6), both"
     " halves."),
]


def main(argv):
    print('=' * 100)
    print('b310_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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

    clauses = [{"clause": c, "cap": cap, "demand": (n if dem is None else dem),
                "units": u, "from": frm} for (c, cap, dem, u, frm) in CLAUSES]

    spec = {"registration":
            "data/b310_registration_2026-09-03.txt -- b310, THE SMEAR COLLAPSES",
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
    print('  ### **AND THE TWO CAPS THAT MATTER MOST THIS ACT ARE ZERO AND ARE NEW:**')
    print('  ### `branch decisions` and `verdicts on M-2`. ### Component 4 touches a branch nobody')
    print('  ### has settled and a specification the corpus owes, and a cap of zero on each is the')
    print('  ### cheapest honest guard against this act\'s most tempting overreach.')
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
