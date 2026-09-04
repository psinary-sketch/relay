# -*- coding: utf-8 -*-
"""b315_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED** -- the standing design
### point, carried since b302.

### ### **EVERY CAP IS ZERO. ### TWO ARE NEW AND THEY GUARD THE SAME TEMPTATION:**
###   ### `.lean` files created or edited, and modules added to the certification file.
###   ### **AN ACT THAT FINDS NINETY-ONE UNCERTIFIED TERMINALS WILL WANT TO CERTIFY THEM**, and
###     certifying them is a build -- under its own registration, with its own baseline and its own
###     controls. ### **A FILINGS ACT THAT QUIETLY BECAME A BUILD WOULD BE THE LARGEST SCOPE BREACH
###     ### THIS SESSION HAS HAD AVAILABLE TO IT.**
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402  ### the counter is READ, never copied

REG = os.path.join(ROOT, 'data', 'b315_registration_2026-09-03.txt')
SPEC = os.path.join(ROOT, 'data', 'b315_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("owner instrument files edited", 0, 0, "files",
     "### **THE ORDER'S CENTRAL CONSTRAINT.** ### The source's convention runs only in b313's"
     " COPIES. ### RE-MEASURED BY G-NOEDIT against `git HEAD`, NORMALISED, AFTER the run."),
    ("`.lean` files created or edited", 0, 0, "files",
     "carried from b314. ### RE-MEASURED BY `git status --short -- *.lean` in BOTH repositories."),
    ("modules added to the certification file", 0, 0, "modules",
     "the coverage gate FILES what it finds. ### RE-MEASURED against `AllPrints.lean` at HEAD."),
    ("grades moved", 0, 0, "grades", "F-G. ### A read and a re-derivation move no grade."),
    ("acts re-verdicted", 0, 0, "acts",
     "### **THE ONE THAT MATTERS THIS ACT.** ### b312's and b313's numbers stand; ONE STATED"
     " REASON is corrected. ### RE-MEASURED BY the must-fail fixtures."),
    ("banked measurements called wrong", 0, 0, "measurements", "carried from b312 and b313."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows",
     "the append-only law. ### RE-MEASURED BY A TRUE-PREFIX CHECK AGAINST `git HEAD`."),
    ("PLACE-papers files written", 0, 0, "files",
     "nothing in the papers repository is touched, so no hook fires and no mirror moves."),
    ("keystone files written", 0, 0, "files", "no keystone is written or edited."),
    ("aggregations stated", 0, 0, "statements", "`M-2` IS OWED AND STAYS OWED."),
    ("branch decisions", 0, 0, "decisions",
     "the bearing on b262 is a BEARING. ### One archimedean object is not the archimedean side."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("constants read off pre-asymptotic cells", 0, 0, "constants",
     "### **NEW THIS ACT.** ### The cutoff bench runs at `log a` in about [0.35, 1.24] and does"
     " NOT reach the regime. ### **A CONSTANT READ OFF IT WOULD BE A FIT WEARING A DERIVATION'S"
     " CLOTHES.** ### RE-MEASURED BY G-NOFIT."),
    ("rulings applied that were to be recorded", 0, 0, "rulings",
     "the author's `W2` is RECORDED and NOT acted on."),
    ("ad-hoc shell-typed numbers", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by the counter"
     " `b300_regspec.count_predictions`, IMPORTED rather than copied."),
]


def main(argv):
    print('=' * 100)
    print('b315_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
            "data/b315_registration_2026-09-03.txt -- b315, THE CALIBRATION AND THE RATE",
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
             'NONE -- the act reads and re-derives, and changes nothing'))
    print('  ### **ONE CAP IS NEW: `constants read off pre-asymptotic cells`.** ### The cutoff')
    print('  ### bench does not reach the regime it derives, and a constant read off it would be')
    print('  ### a fit wearing a derivation s clothes.')
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
