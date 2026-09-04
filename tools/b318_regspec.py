# -*- coding: utf-8 -*-
"""b318_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED** -- the standing design
### point, carried since b302.

### ### **THREE CAPS ARE NEW, AND EACH IS A WAY THIS ACT COULD HAVE CHEATED ITS OWN RESULT:**
###   ### `subtractions inside the square form` -- ### **THE ONE THAT CARRIES THE ACT.** ### The
###     square's nonnegativity is worth stating only because it is a SUM OF SQUARES. ### A version
###     that formed it as `||A||^2 - ||AQ||^2` would be arithmetically equal and would have thrown
###     away the whole claim, because a difference of two large numbers can land anywhere.
###     ### RE-MEASURED BY `G-NOSUB` against the emitting file.
###   ### `W_infinity evaluations` -- b317 computed ONE side of the source's inequality. ### **THIS
###     ### ACT COMPUTES NEITHER.** ### Both of its objects are trace-side.
###   ### `rank-stable schemes built` -- the order says SPECIFIED and NOT built.
### ### **AND ONE CAP IS CARRIED FORWARD SHARPENED:** ### `acts re-verdicted` stays at zero, and the
### registration says at (8) exactly why a RE-LABELLING of b317's numbers is not a re-verdict.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402  ### the counter is READ, never copied

REG = os.path.join(ROOT, 'data', 'b318_registration_2026-09-04.txt')
SPEC = os.path.join(ROOT, 'data', 'b318_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("subtractions inside the square form", 0, 0, "subtractions",
     "### **NEW THIS ACT, AND IT IS THE ONE THAT CARRIES IT.** ### The nonnegativity is a claim"
     " about a SUM OF SQUARES. ### A difference of two large norms would be equal in exact"
     " arithmetic and worthless as evidence. ### RE-MEASURED BY `G-NOSUB` against"
     " `tools/b318_square.py::square_trace`."),
    ("W_infinity evaluations", 0, 0, "evaluations",
     "### **NEW THIS ACT.** ### b317 computed one side of the source's inequality; this act computes"
     " NEITHER. ### Both objects here are trace-side. ### RE-MEASURED BY `G-NOWEIL`."),
    ("rank-stable schemes built", 0, 0, "schemes",
     "### **NEW THIS ACT.** ### The order says the scheme is SPECIFIED and NOT built."
     " ### RE-MEASURED BY `G-NOBUILD318` against the act's own tool list."),
    ("archimedean units constructed", 0, 0, "units",
     "carried from b317. ### b300's unit is never built, projected or traced."
     " ### RE-MEASURED BY `G-NOUNIT` over STRIPPED code -- b317's own lesson."),
    ("membership questions decided", 0, 0, "questions",
     "carried from b317. ### b316 declared the instrument NOT YET CERTIFIED for these."),
    ("acts re-verdicted", 0, 0, "acts",
     "### **THE ONE THAT MATTERS THIS ACT.** ### If b317's smear is not the source's trace side, its"
     " numbers are RE-LABELLED. ### A re-labelling is not a re-verdict, b317's grade does not move,"
     " and nothing b317 measured is called wrong. ### The registration says so at (8)."),
    ("banked measurements called wrong", 0, 0, "measurements", "carried from b312, b313 and b317."),
    ("grades moved", 0, 0, "grades", "F-G. ### A definitional decision moves no grade."),
    ("owner instrument files edited", 0, 0, "files",
     "carried from b313, b315, b316 and b317. ### `b317_smear.py` and `b316_instrument.py` are"
     " OWNERS now and are imported, not edited. ### RE-MEASURED BY G-NOEDIT against `git HEAD`."),
    ("`.lean` files created or edited", 0, 0, "files",
     "carried from b314. ### RE-MEASURED BY `git status --short -- *.lean` in BOTH repositories."),
    ("modules added to the certification file", 0, 0, "modules",
     "the coverage gate FILES what it finds and repairs nothing. ### RE-MEASURED at HEAD."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows",
     "the append-only law. ### RE-MEASURED BY A TRUE-PREFIX CHECK AGAINST `git HEAD`."),
    ("PLACE-papers files written", 0, 0, "files",
     "nothing in the papers repository is touched, so no hook fires and no mirror moves."),
    ("keystone files written", 0, 0, "files", "no keystone is written or edited."),
    ("aggregations stated", 0, 0, "statements", "`M-2` IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("claims that a function is positive definite from a finite scan", 0, 0, "claims",
     "### **(B1)'s OWN REACH.** ### A scan can exhibit a negative value and prove the negative; it"
     " cannot prove the positive beyond the interval scanned, and the act may not say otherwise."),
    ("float literals in a deciding runner", 0, 0, "literals",
     "carried from b316 and b317. ### Bars and frames live in the tools."
     " ### RE-MEASURED BY G-NOFLOAT, which reads the runner's own source."),
    ("controls reported as a pass that could not fire", 0, 0, "controls",
     "b308's law. ### Every arm is shown ABLE to fire, or reported unable. ### The class test has"
     " both polarities in its fixtures. ### RE-MEASURED BY G-ARMS."),
    ("point verdicts taken from a refused axis", 0, 0, "verdicts",
     "the noise-floor gate is in the path, and a value it refuses may not carry a verdict."),
    ("ad-hoc shell-typed numbers", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by the counter"
     " `b300_regspec.count_predictions`, IMPORTED rather than copied."),
]


def main(argv):
    print('=' * 100)
    print('b318_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
            "data/b318_registration_2026-09-04.txt -- b318, THE FORCED SIGN",
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
    print('  ### CAPS THAT ARE NOT ZERO : %s'
          % (', '.join(nonzero) if nonzero else 'NONE -- every cap is zero'))
    print('  ### **b317 CAPPED THE INEQUALITY AT ONE SIDE. ### THIS ACT CAPS IT AT ZERO**, because')
    print('  ### both of its objects are trace-side and `W_infinity` is not computed at all.')
    print('  ### **AND `subtractions inside the square form` IS THE CAP THAT CARRIES THE ACT**: the')
    print('  ### nonnegativity is only worth stating because nothing is subtracted to reach it.')
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
