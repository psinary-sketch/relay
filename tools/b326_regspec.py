# -*- coding: utf-8 -*-
"""b326_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**

### ### **EVERY CLAUSE HERE IS A FORWARD COMMITMENT.** ### b325 learned that a historical fact typed
### into this table makes it unsatisfiable by construction; this act's ordering statement is a
### fact about what has NOT happened yet (`instrument values seen before this seal : 0`), and the
### spec is emitted BEFORE any instrument of the act runs, so it is a commitment and not a record.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b326_registration_2026-09-04.txt')
SPEC = os.path.join(ROOT, 'data', 'b326_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("instrument values seen before this seal", 0, 0, "values",
     "### section (0): the registration is sealed before any instrument of this act runs; the only"
     " numbers seen are b325's banked ones and a timing probe unrelated to any cell."),
    ("owner instrument files edited", 1, 1, "files",
     "### `b321_window.py` -- the eleven-prime constant replaced by the full prime set with the"
     " scope written into the header, BY THE NAVIGATOR'S ORDER. ### No other owner file."),
    ("families beyond the arc's, declared", 1, 1, "families",
     "### the AIMED family of section (6): the same seed and square, each bump multiplied by"
     " `cos(omega v)` with `omega` the refined banked off-line height; reported on its own line."),
    ("verdict branches other than the three registered", 0, 0, "branches",
     "### SEES IT, DOES NOT SEE IT, PARTIAL -- the order's own three, applied to the arc's family."),
    ("prior-act banked constituents found defective, re-measured and reported beside the original",
     2, 2, "constituents",
     "### section (1): the Epstein kernel's normalization and, if it follows, the crossing b325"
     " priced. ### The closure decides; the sealed b325 file is not edited."),
    ("claims about zeta, h2, or the roster", 0, 0, "claims",
     "### the zeta window's extension is a CONTROL and its result is reported as such."),
    ("grades moved", 0, 0, "grades", "F-G."),
    ("acts re-verdicted", 0, 0, "acts",
     "### b325's `DOES NOT SEE IT` at the arc's cells stands whichever kernel closes."),
    ("deposited texts touched", 0, 0, "files", "the deposit is read, never written."),
    ("`.lean` files created or edited", 0, 0, "files", "none."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows",
     "the append-only law. ### RE-MEASURED BY A TRUE-PREFIX CHECK AGAINST `git HEAD`."),
    ("aggregations stated", 0, 0, "statements", "`M-2` IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("tools writing one run file from two paths", 0, 0, "tools",
     "### structural since b324: a tool that can take two paths writes a differently named file"
     " on each; the long computation writes its bank once and is not re-run after the push."),
    ("controls reported as a pass that could not fire", 0, 0, "controls",
     "b308's law. ### the zeta control CAN fire (it did at b325); the route-B agreement CAN fail;"
     " the box winding CAN exceed the sign count; each is shown able."),
    ("float literals in a deciding runner", 0, 0, "literals", "the bars live in the tools."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count",
     "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("sealed files edited", 0, 0, "files",
     "### b325's sealed registration included, whatever section (1) finds."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by the counter"
     " `b300_regspec.count_predictions`, IMPORTED rather than copied."),
]


def main(argv):
    print('=' * 100)
    print('b326_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
            "data/b326_registration_2026-09-04.txt -- b326, THE REACH",
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
    print('  ### **THE NONZERO CAPS ARE THE ACT.** ### One ordered edit of an owner tool; one')
    print('  ### declared family beyond the arc\'s; and at most two prior-act constituents that the')
    print('  ### closure may find defective -- ### **A CAP ON WHAT THE ACT MAY REPORT, NOT A')
    print('  ### ### PREDICTION THAT IT WILL.**')
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
