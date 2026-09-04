# -*- coding: utf-8 -*-
"""b317_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED** -- the standing design
### point, carried since b302.

### ### **b316's TWO LARGEST CAPS ARE GONE AND THAT IS THE POINT OF THIS ACT.** ### `traces
### computed` and `smears assembled` were b316's central constraint; ### **THIS ACT IS THE ONE THEY
### ### WERE DEFERRING TO**, and it computes both under its own registration and its own bars.
### ### **FOUR CAPS ARE NEW, AND EACH IS A WAY THIS ACT COULD OVERREACH:**
###   ### `archimedean units constructed` -- ### **THE ORDER'S OWN WORDS: NO UNIT IS USED ANYWHERE.**
###     ### b316 declared the instrument NOT CERTIFIED for membership, and an act that quietly built
###     the unit to see where it landed would be using it for exactly that.
###   ### `membership questions decided` -- the same cap from the other side.
###   ### `cells reported whose rank reached NY` -- ### **b316's OWN DEFECT SPECIES, MADE INTO A
###     ### CAP.** ### A saturated constraint set silently under-constrains the space.
###   ### `sides of the source's inequality evaluated` -- capped at ONE. ### The mean-zero column is
###     one side; the archimedean Weil distribution for that variant is a separate computation under
###     its own registration, and an act that produced both would be stating the inequality.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402  ### the counter is READ, never copied

REG = os.path.join(ROOT, 'data', 'b317_registration_2026-09-04.txt')
SPEC = os.path.join(ROOT, 'data', 'b317_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("archimedean units constructed", 0, 0, "units",
     "### **NEW THIS ACT, AND THE ORDER NAMES IT IN ITS FIRST LINE.** ### b300's derived unit is"
     " never built, never projected and never traced. ### RE-MEASURED BY `G-NOUNIT` against the"
     " emitting files -- `sonin_unit` is not called anywhere in this act's tools."),
    ("membership questions decided", 0, 0, "questions",
     "### **NEW THIS ACT.** ### b316 declared the instrument NOT YET CERTIFIED for these."
     " ### RE-MEASURED BY `G-NOMEMBER` against the bank's own must-fail lines."),
    ("cells reported whose rank reached NY", 0, 0, "cells",
     "### **NEW THIS ACT -- b316's DEFECT SPECIES AS A CAP.** ### A saturated constraint set"
     " under-constrains the space without saying so. ### RE-MEASURED BY `G-RANKGUARD` off the run."),
    ("sides of the source's inequality evaluated", 1, 1, "sides",
     "### **NEW THIS ACT, AND CAPPED AT ONE RATHER THAN ZERO.** ### The mean-zero column IS one"
     " side. ### The archimedean Weil distribution for that variant is NOT computed."
     " ### RE-MEASURED BY `G-ONESIDE`."),
    ("owner instrument files edited", 0, 0, "files",
     "carried from b313, b315 and b316. ### RE-MEASURED BY G-NOEDIT against `git HEAD`."),
    ("`.lean` files created or edited", 0, 0, "files",
     "carried from b314. ### RE-MEASURED BY `git status --short -- *.lean` in BOTH repositories."),
    ("modules added to the certification file", 0, 0, "modules",
     "the coverage gate FILES what it finds and repairs nothing. ### RE-MEASURED at HEAD."),
    ("grades moved", 0, 0, "grades", "F-G. ### A computation on a truncation moves no grade."),
    ("acts re-verdicted", 0, 0, "acts",
     "### **THE ONE THAT MATTERS THIS ACT.** ### Naming the corpus's old archimedean values"
     " evaluations of a DIFFERENT quantity says what the two quantities are; it does not find that"
     " either was computed wrongly. ### The registration says so at (8)."),
    ("banked measurements called wrong", 0, 0, "measurements", "carried from b312 and b313."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows",
     "the append-only law. ### RE-MEASURED BY A TRUE-PREFIX CHECK AGAINST `git HEAD`."),
    ("PLACE-papers files written", 0, 0, "files",
     "nothing in the papers repository is touched, so no hook fires and no mirror moves."),
    ("keystone files written", 0, 0, "files", "no keystone is written or edited."),
    ("aggregations stated", 0, 0, "statements", "`M-2` IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("rulings applied beyond their record", 0, 0, "rulings",
     "the author's `W2` is applied AT THE INSTRUMENT -- both test functions are run and reported as"
     " separate columns -- and nowhere else. ### RE-MEASURED BY `G-W2SCOPE`."),
    ("float literals in a deciding runner", 0, 0, "literals",
     "carried from b316. ### Grid parameters, bars and tolerances are declared."
     " ### RE-MEASURED BY G-NOFLOAT, which reads the runner's own source."),
    ("controls reported as a pass that could not fire", 0, 0, "controls",
     "b308's law, carried from b316. ### Every arm in this act is shown ABLE to fire, or is reported"
     " as unable. ### RE-MEASURED BY G-ARMS."),
    ("point verdicts taken from a refused axis", 0, 0, "verdicts",
     "### **THE NOISE-FLOOR GATE IS IN THE PATH.** ### A value the gate refuses may not carry a"
     " verdict, and the scoring is a BAND statement for exactly that reason."),
    ("ad-hoc shell-typed numbers", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by the counter"
     " `b300_regspec.count_predictions`, IMPORTED rather than copied."),
]


def main(argv):
    print('=' * 100)
    print('b317_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
            "data/b317_registration_2026-09-04.txt -- b317, THE TRACE ON THE OBJECT",
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
          % (', '.join(nonzero) if nonzero else 'NONE'))
    print('  ### **b316\'s `traces computed` AND `smears assembled` CAPS ARE GONE, AND THAT IS THIS')
    print('  ### ### ACT.** ### They were b316\'s central constraint and this is the act they were')
    print('  ### deferring to. ### **FOUR CAPS ARE NEW**, and the one capped at ONE rather than')
    print('  ### zero is the source\'s inequality: the mean-zero column IS one side of it.')
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
