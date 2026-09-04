# -*- coding: utf-8 -*-
"""b316_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED** -- the standing design
### point, carried since b302.

### ### **EVERY CAP IS ZERO. ### THREE ARE NEW.**
###   ### `traces computed` and `smears assembled` -- ### **AN INSTRUMENT THAT WORKS WILL TEMPT ITS
###     ### BUILDER TO POINT IT AT SOMETHING**, and pointing it is act two, under its own
###     registration, with its own baseline and its own controls.
###   ### `controls reported as a pass that could not fire` -- ### **THE ONE THIS ACT NEARLY
###     ### BREACHED.** ### The asymptotic control on the derived archimedean unit returns almost
###     the same number at a non-eigenvalue as at the eigenvalue. ### b308's law makes that a
###     NOT-A-CHECK, and a cap makes it a thing the suite re-measures rather than a thing the
###     author remembered to say.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402  ### the counter is READ, never copied

REG = os.path.join(ROOT, 'data', 'b316_registration_2026-09-04.txt')
SPEC = os.path.join(ROOT, 'data', 'b316_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("traces computed", 0, 0, "traces",
     "### **THE ORDER'S CENTRAL CONSTRAINT.** ### The trace is act two, under its own registration."
     " ### RE-MEASURED BY G-NOTRACE against the emitting files."),
    ("smears assembled", 0, 0, "smears",
     "the same constraint at the other end: no test function is integrated against anything in this"
     " act. ### The instrument ACCEPTS either and COMPUTES WITH NEITHER."),
    ("owner instrument files edited", 0, 0, "files",
     "carried from b313 and b315. ### RE-MEASURED BY G-NOEDIT against `git HEAD`, NORMALISED."),
    ("`.lean` files created or edited", 0, 0, "files",
     "carried from b314. ### RE-MEASURED BY `git status --short -- *.lean` in BOTH repositories."),
    ("modules added to the certification file", 0, 0, "modules",
     "the coverage gate FILES what it finds and repairs nothing. ### RE-MEASURED at HEAD."),
    ("grades moved", 0, 0, "grades", "F-G. ### An instrument build moves no grade."),
    ("acts re-verdicted", 0, 0, "acts",
     "### **THE ONE THAT MATTERS THIS ACT.** ### A truncation that fails to reproduce b300's"
     " whole-line membership has NOT re-verdicted b300, and the registration says so at (8)."),
    ("banked measurements called wrong", 0, 0, "measurements", "carried from b312 and b313."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows",
     "the append-only law. ### RE-MEASURED BY A TRUE-PREFIX CHECK AGAINST `git HEAD`."),
    ("PLACE-papers files written", 0, 0, "files",
     "nothing in the papers repository is touched, so no hook fires and no mirror moves."),
    ("keystone files written", 0, 0, "files", "no keystone is written or edited."),
    ("aggregations stated", 0, 0, "statements", "`M-2` IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("rulings applied that were to be recorded", 0, 0, "rulings",
     "the author's `W2` is RECORDED. ### The order licenses ONE construction-time consequence -- the"
     " instrument accepts either test function -- and nothing beyond it."),
    ("float literals in a deciding runner", 0, 0, "literals",
     "### **NEW THIS ACT, AND THE ORDER NAMES IT.** ### Grid parameters and tolerances are not"
     " findings. ### RE-MEASURED BY G-NOFLOAT, which reads the runner's own source."),
    ("controls reported as a pass that could not fire", 0, 0, "controls",
     "### **NEW THIS ACT, AND IT IS THE ONE THIS ACT NEARLY BREACHED.** ### b308's law. ### The"
     " asymptotic control on the derived unit CANNOT DISCRIMINATE an eigenvalue from a"
     " non-eigenvalue, and is reported as NOT-A-CHECK rather than as a pass."
     " ### RE-MEASURED BY G-NOTACHECK against the emitting run."),
    ("ad-hoc shell-typed numbers", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by the counter"
     " `b300_regspec.count_predictions`, IMPORTED rather than copied."),
]


def main(argv):
    print('=' * 100)
    print('b316_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
            "data/b316_registration_2026-09-04.txt -- b316, THE ARCHIMEDEAN INSTRUMENT, ACT ONE",
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
          % (', '.join(nonzero) if nonzero else
             'NONE -- the act builds an instrument and measures with it'))
    print('  ### **THREE CAPS ARE NEW.** ### `traces computed` and `smears assembled` are the')
    print('  ### order\'s central constraint and the whole reason act two exists separately.')
    print('  ### **AND `controls reported as a pass that could not fire` IS THE ONE THIS ACT')
    print('  ### ### NEARLY BREACHED**, which is why it is a cap and not a remark.')
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
