# -*- coding: utf-8 -*-
"""b320_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**

### ### ### **THE CAP THAT WAS ZERO FOR FOUR ACTS IS NOT ZERO HERE, AND IT IS THE ACT.** ###
### `W_infinity evaluations` has been ZERO since b316 named the quantity and refused it. ### **THIS
### ### ACT'S ORDER IS TO COMPUTE IT**, so the cap is raised to the number of cells the act reports
### and no further, and a NEW cap takes over what the old one was really protecting:
### ### **`bars widened after a value was seen` -- CAPPED AT ZERO.** ### The order says the act may
### not widen, tune or re-bar anything to make the control pass. ### **THAT IS THE ONE CAP A
### ### FAVOURABLE RESULT WOULD TEMPT THIS SEAT TO BREACH**, and it is re-measured by `G-NOWIDEN`
### against the sealed registration's own bar values and the tools that carry them.
### ### **AND `windows opened` IS CAPPED AT ZERO**: the uncovered cells are computed and REPORTED,
### and an interpretation of them would be the window act's work done here without its registration.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b320_registration_2026-09-04.txt')
SPEC = os.path.join(ROOT, 'data', 'b320_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("bars widened after a value was seen", 0, 0, "bars",
     "### **THE ONE A FAVOURABLE RESULT WOULD TEMPT THIS SEAT TO BREACH.** ### The order forbids"
     " widening, tuning or re-barring to make the control pass. ### RE-MEASURED BY `G-NOWIDEN`,"
     " which reads the sealed registration's bar values against the constants the tools carry."),
    ("windows opened", 0, 0, "windows",
     "### **NEW THIS ACT.** ### Cells the theorem does not cover are computed and REPORTED AS DATA."
     " ### An interpretation of them is the window act's, under its own registration."
     " ### RE-MEASURED BY `G-NOWINDOW` against the bank's must-fail lines."),
    ("sides of the source's inequality evaluated", 2, 2, "sides",
     "### **RAISED FROM b318's ONE AND b319's ZERO BY THIS ACT'S ORDER.** ### Both sides are"
     " computed: the Weil distribution from (38) and (53), and the square on b319's stable cut."),
    ("archimedean units used", 0, 0, "units",
     "carried from b316 onward. ### b300's unit is not constructed, projected or traced here."
     " ### RE-MEASURED BY `G-NOUNIT` over STRIPPED code."),
    ("verdicts on membership", 0, 0, "verdicts", "`W-ORD-ARCH-MEMBERSHIP` is open and untouched."),
    ("claims to have proved the source's theorem", 0, 0, "claims",
     "### **THE INSTRUMENT IS CHECKED AGAINST A THEOREM IT DID NOT PROVE.** ### If the control"
     " holds, that is a certification of the instrument at exactly that scope."),
    ("acts re-verdicted", 0, 0, "acts",
     "b316, b317, b318 and b319 stand. ### b319's prose-vs-table defect is FILED, not re-verdicted:"
     " its table is right and its measurement stands."),
    ("banked measurements called wrong", 0, 0, "measurements", "carried from b312 onward."),
    ("grades moved", 0, 0, "grades", "F-G."),
    ("owner instrument files edited", 0, 0, "files",
     "b316, b317, b318 and b319's tools are OWNERS and are imported, not edited."
     " ### RE-MEASURED BY G-NOEDIT against `git HEAD`."),
    ("`.lean` files created or edited", 0, 0, "files",
     "back to zero after b319's repair. ### RE-MEASURED BY `git status --short -- *.lean`."),
    ("modules added to the certification file", 0, 0, "modules", "back to zero after b319."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows",
     "the append-only law. ### RE-MEASURED BY A TRUE-PREFIX CHECK AGAINST `git HEAD`."),
    ("PLACE-papers files written", 0, 0, "files", "no hook fires and no mirror moves."),
    ("keystone files written", 0, 0, "files", "no keystone is written or edited."),
    ("aggregations stated", 0, 0, "statements", "`M-2` IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("the corpus's digamma integral read as the source's W_infinity", 0, 0, "readings",
     "### **IT IS CORROBORATION ONLY**, compared afterward through the settled sign chain, with the"
     " chain's links quoted. ### RE-MEASURED BY `G-CORROB`."),
    ("float literals in a deciding runner", 0, 0, "literals",
     "the bars live in the tools. ### RE-MEASURED BY G-NOFLOAT."),
    ("controls reported as a pass that could not fire", 0, 0, "controls",
     "b308's law. ### The class test and the (39)-against-(38) check both carry a failing arm."),
    ("point verdicts taken from a refused axis", 0, 0, "verdicts",
     "the noise-floor gate is in the path."),
    ("ad-hoc shell-typed numbers", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by the counter"
     " `b300_regspec.count_predictions`, IMPORTED rather than copied."),
]


def main(argv):
    print('=' * 100)
    print('b319_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
            "data/b319_registration_2026-09-04.txt -- b320, THE LAWFUL FUNCTION AND THE CONTROL",
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
    print('  ### ### **CAPS THAT ARE NOT ZERO : %d**' % len(nonzero))
    for c in nonzero:
        print('    ### %s' % c)
    print('  ### **ONE NONZERO CAP, AND IT IS THE ACT.** ### `W_infinity` has been capped at zero')
    print('  ### since b316 named it. ### **THIS ORDER IS TO COMPUTE IT**, so the cap is raised to')
    print('  ### BOTH sides and a new cap -- `bars widened after a value was seen` -- takes over')
    print('  ### what the old one was really protecting.')
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
