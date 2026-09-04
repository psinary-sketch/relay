# -*- coding: utf-8 -*-
"""b313_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED** -- the standing design
### point, carried since b302.

### ### **EVERY CAP IS ZERO. ### TWO ARE NEW AND THEY ARE THIS ACT'S TWO REAL RISKS:**
###   ### **`owner instrument files edited`** ### -- the order says the owner instrument is NOT
###     edited and a copy carries the flip. ### **THE WHOLE CORPUS COMPUTES WITH THOSE FILES.**
###   ### **`comparisons to a target, and fits`** ### -- an act that flips a sign, looks at a
###     residue and keeps the flip because the residue improved is TUNING. ### **THIS ACT'S FLIP IS
###     ### LICENSED AT DEFINITIONS BEFORE ANY NUMBER IS READ, AND THE CAP IS WHAT KEEPS THE BANK
###     ### READABLE AS THAT ACT AND NOT THE OTHER ONE.**
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402  ### the counter is READ, never copied

REG = os.path.join(ROOT, 'data', 'b313_registration_2026-09-03.txt')
SPEC = os.path.join(ROOT, 'data', 'b313_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("owner instrument files edited", 0, 0, "files",
     "### **NEW THIS ACT, AND THE ORDER'S CENTRAL CONSTRAINT.** ### RE-MEASURED BY"
     " G-OWNER-UNTOUCHED against `git`, NORMALISED for line endings, AFTER the run rather than"
     " before it -- a file is edited by running things, not by planning to."),
    ("`.lean` modules created", 0, 0, "modules",
     "THE SHADOW IS EXPECTED TO BE NOTHING: a floating-point instrument comparison is not"
     " finite-decidable, and a terminal over a rounded number certifies the rounding."),
    ("profile files rewritten", 0, 0, "files",
     "the same clause. ### RE-MEASURED IN THE CLOSING against `git HEAD`, NORMALISED and with the"
     " baseline FOUND rather than assumed -- b309's (D6), both halves."),
    ("PLACE-papers files written", 0, 0, "files",
     "the ERRATA-class finding is ROUTED, not filed by this seat. ### RE-MEASURED BY G-NOPAPERS."),
    ("keystone files written", 0, 0, "files", "no keystone is written or edited."),
    ("grades moved", 0, 0, "grades",
     "F-G. ### A second column beside the first moves no grade."),
    ("acts re-verdicted", 0, 0, "acts",
     "F-G. ### b38's, b240's, b264's numbers stand as banked, at their own grades."),
    ("banked measurements called wrong", 0, 0, "measurements",
     "carried from b312 and re-measured here. ### **WHAT MAY CHANGE IS WHAT A BANKED NUMBER IS A"
     " COMPUTATION OF, WHICH IS AN INSTRUMENT STATEMENT AND NOT A RE-VERDICT.**"),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows",
     "the append-only law. ### RE-MEASURED BY A TRUE-PREFIX CHECK AGAINST `git HEAD`."),
    ("aggregations stated", 0, 0, "statements",
     "`M-2` IS OWED AND STAYS OWED. ### RE-MEASURED BY the must-fail fixtures."),
    ("branch decisions", 0, 0, "decisions",
     "carried from b310. ### b262's disjunction is undecided and this act does not decide it."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("comparisons to a target, and fits", 0, 0, "comparisons",
     "### **NEW THIS ACT.** ### THE ORDER: *NO comparison to any target and no fit*. ### No banked"
     " target, prime sum, mass or asymptote is named as something the new column is near or far"
     " from. ### RE-MEASURED BY G-NOFIT, whose must-fail fixtures assert whole-line absence of the"
     " sentences a fit would have produced."),
    ("rulings applied", 0, 0, "rulings",
     "the author's `W2` is RECORDED and NOT acted on. ### RE-MEASURED BY G-RULING."),
    ("ad-hoc shell-typed numbers", 0, 0, "count",
     "RULING (3) / `W-ORD-ADHOC-CHECK-FIXTURES`. ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by the counter"
     " `b300_regspec.count_predictions`, IMPORTED rather than copied."),
]


def main(argv):
    print('=' * 100)
    print('b313_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b313_registration_2026-09-03.txt -- b313, THE EXPONENT",
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
             'NONE -- the act computes a second column and changes nothing'))
    print('  ### **TWO CAPS ARE NEW: `owner instrument files edited` and `comparisons to a')
    print('  ### target, and fits`.** ### The first guards the instrument the whole corpus computes')
    print('  ### with; the second guards the difference between this act and a tuning exercise,')
    print('  ### which is the only way a LICENSED flip can still be dishonestly reported.')
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
