# -*- coding: utf-8 -*-
"""b322_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**

### ### ### **THE CAP THAT IS THIS ACT'S OWN: ### `units adopted or replaced` -- ZERO.** ### The act
### is called THE MEMBERSHIP and its whole temptation is to come out of it holding a unit. ### The
### order forbids that in terms: *the derivation and the measurement each stand at their grade until
### one constituent gives way, and if none does the act says so.*
### ### **AND ITS SIBLING: ### `claims that the residual reaches zero` -- ZERO.** ### A falling course
### at five frames is a falling course at five frames, and the branch that reads FALLS is exactly the
### branch that would like to say more than that.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b322_registration_2026-09-04.txt')
SPEC = os.path.join(ROOT, 'data', 'b322_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("units adopted or replaced", 0, 0, "units",
     "### **THE ACT'S OWN CENTRAL CAP, AND THE ONE ITS NAME MOST TEMPTS IT TO BREACH.** ### The"
     " order: *no unit adopted or replaced -- the derivation and the measurement each stand at their"
     " grade until one constituent gives way, and if none does the act says so.*"
     " ### RE-MEASURED BY `G-NOADOPT` against the bank's must-fail lines."),
    ("claims that the residual reaches zero", 0, 0, "claims",
     "### **A FALLING COURSE AT FIVE FRAMES IS A FALLING COURSE AT FIVE FRAMES.** ### The branch"
     " that reads FALLS is the branch that would like to say more. ### RE-MEASURED BY `G-NOLIMIT`."),
    ("bars widened after a value was seen", 0, 0, "bars",
     "carried from b320 and b321. ### RE-MEASURED BY `G-NOWIDEN`, which compares the sealed hash"
     " against a literal written into the gate suite before the ladder was run."),
    ("acts re-verdicted", 0, 0, "acts",
     "### **BOTH SIDES OF THIS QUESTION ARE PRIOR ACTS AND NEITHER IS RE-VERDICTED.** ### b300's"
     " derivation stands at DERIVES-on-IMPORTS; b316's and b319's measurements stand at theirs."),
    ("realizations unfolded", 2, 2, "realizations",
     "### **THE ACT ITSELF.** ### The derived unit and the instrument's, each unfolded to base"
     " objects and NEITHER DESCRIBED IN THE OTHER'S LANGUAGE, which is the order's own condition."),
    ("frames on the domain ladder", 5, 5, "frames",
     "b317's `DOMAIN_AXIS`, unchanged: (1024,8) to (16384,128). ### The same frames b319, b320 and"
     " b321 used, so the courses are comparable row for row."),
    ("routes to the residual's exponent", 2, 2, "routes",
     "### **AND THEY SHARE NO CODE**: a least-squares fit to five measured residuals, and a bound on"
     " `x u(x)` read off the vector. ### (B3) fixes their agreement bar before either is computed."),
    ("claims about h2, the identity's truth, or the complete roster", 0, 0, "claims",
     "nothing is said about h2 beyond the register sentence, exact."),
    ("verdicts on membership taken beyond the branch reached", 0, 0, "verdicts",
     "### `W-ORD-ARCH-MEMBERSHIP` is the order this act addresses, and (B5) fixes its three"
     " branches BEFORE the evidence. ### The act may take the branch the arms reach and no other."),
    ("owner instrument files edited", 0, 0, "files",
     "b316, b319, b205_prolate and the e16 owners are imported, not edited."
     " ### RE-MEASURED BY G-NOEDIT against `git HEAD`."),
    ("grades moved", 0, 0, "grades", "F-G."),
    ("banked measurements called wrong", 0, 0, "measurements", "carried from b312 onward."),
    ("`.lean` files created or edited", 0, 0, "files",
     "back to zero after b319's repair. ### RE-MEASURED BY `git status --short -- *.lean`."),
    ("modules added to the certification file", 0, 0, "modules", "back to zero after b319."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows",
     "the append-only law. ### RE-MEASURED BY A TRUE-PREFIX CHECK AGAINST `git HEAD`."),
    ("PLACE-papers files written", 0, 0, "files", "no hook fires and no mirror moves."),
    ("keystone files written", 0, 0, "files",
     "### **THE ORDER NAMES THE KEYSTONE RE-READ AS FOLLOWING THE FOLD, NOT THIS ACT.**"),
    ("aggregations stated", 0, 0, "statements", "`M-2` IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("float literals in a deciding runner", 0, 0, "literals",
     "the bars live in the tools. ### RE-MEASURED BY G-NOFLOAT."),
    ("controls reported as a pass that could not fire", 0, 0, "controls",
     "b308's law. ### The taper arm can return THE VECTOR and the fit can return a flat course."),
    ("point verdicts taken from a refused axis", 0, 0, "verdicts",
     "the noise-floor gate is in the path, and a refused value has its DIRECTION reported and not"
     " its SIZE, in different columns."),
    ("ad-hoc shell-typed numbers", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by the counter"
     " `b300_regspec.count_predictions`, IMPORTED rather than copied."),
]


def main(argv):
    print('=' * 100)
    print('b322_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
            "data/b322_registration_2026-09-04.txt -- b322, THE MEMBERSHIP",
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
    print('  ### **THREE NONZERO CAPS, AND THEY ARE THE ACT.** ### Two realizations unfolded;')
    print('  ### five frames on the domain ladder; two routes to one exponent. ### **EVERY OTHER')
    print('  ### ### CAP IS ZERO, AND THE TWO THAT MATTER MOST ARE `units adopted or replaced` AND')
    print('  ### ### `claims that the residual reaches zero`** -- the first because the act is named')
    print('  ### for the thing it may not do, and the second because the branch it is likeliest to')
    print('  ### reach is the branch that would like to say more than five frames can carry.')
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
