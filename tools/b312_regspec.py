# -*- coding: utf-8 -*-
"""b312_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED** -- the standing design
### point, carried since b302.

### ### **EVERY CAP IS ZERO THIS ACT.** ### The order is reads and a decision at definitions.
### ### **TWO OF THE CAPS ARE NEW AND BOTH GUARD THE SAME TEMPTATION**, which is the one this act
### actually met: an act that finds a discrepancy in an instrument the corpus has computed with for
### a month will want to say what it means. ### **IT MAY NOT.**
###   ### **`banked measurements called wrong`** ### -- this act compared two WRITTEN DEFINITIONS
###     and ran no computation. ### **A VERDICT ON A MEASUREMENT NEEDS AN INSTRUMENT THIS ACT DOES
###     ### NOT HAVE**, and the cap is what keeps the finding from quietly becoming one.
###   ### **`entailments run on a non-SAME verdict`** ### -- Component 3 is ordered on `SAME` only,
###     and a weakened version of it would be the same drift in softer words.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402  ### the counter is READ, never copied

REG = os.path.join(ROOT, 'data', 'b312_registration_2026-09-03.txt')
SPEC = os.path.join(ROOT, 'data', 'b312_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("`.lean` modules created", 0, 0, "modules",
     "THE SHADOW IS EXPECTED TO BE NOTHING: a quotation is not decidable and a comparison of two"
     " analytic definitions is not finite-decidable."),
    ("profile files rewritten", 0, 0, "files",
     "the same clause. ### RE-MEASURED IN THE CLOSING against `git HEAD`, NORMALISED and with the"
     " baseline FOUND rather than assumed -- b309's (D6), both halves."),
    ("PLACE-papers files written", 0, 0, "files",
     "F-I. ### RE-MEASURED BY G-NOPAPERS against `git status --porcelain` in that repository."),
    ("keystone files written", 0, 0, "files", "no keystone is written or edited."),
    ("grades moved", 0, 0, "grades",
     "F-D. ### A decision at definitions moves no grade, and this one moves none even though it"
     " found something."),
    ("acts re-verdicted", 0, 0, "acts",
     "F-D. ### EVERY BANKED ACT STANDS WHERE ITS OWN ACT LEFT IT."),
    ("banked measurements called wrong", 0, 0, "measurements",
     "### **NEW THIS ACT, AND THE ONE THAT MATTERS.** ### The finding is about two written"
     " definitions. ### RE-MEASURED BY G-NOREVERDICT, whose must-fail fixtures assert whole-line"
     " absence of the sentences a verdict on a measurement would produce."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows",
     "the append-only law. ### RE-MEASURED BY A TRUE-PREFIX CHECK AGAINST `git HEAD`."),
    ("aggregations stated", 0, 0, "statements",
     "`M-2` IS OWED AND STAYS OWED. ### RE-MEASURED BY the must-fail fixtures."),
    ("branch decisions", 0, 0, "decisions",
     "carried from b310. ### b262's disjunction is undecided and this act does not decide it."),
    ("verdicts on M-2", 0, 0, "verdicts",
     "carried from b310. ### The cap travels with the act."),
    ("archimedean numbers computed", 0, 0, "numbers",
     "### THE ORDER: *NO archimedean number computed*. ### RE-MEASURED BY G-NOARCHNUM, which checks"
     " STRUCTURALLY that the act's three new tools contain no arithmetic at all."),
    ("entailments run on a non-SAME verdict", 0, 0, "entailments",
     "### **NEW THIS ACT.** ### The order runs Component 3 on `SAME` only and says so in its own"
     " words. ### RE-MEASURED BY G-NOENTAIL."),
    ("rulings applied", 0, 0, "rulings",
     "the author's `W2` is RECORDED and NOT acted on, which is the ruling's own instruction."
     " ### RE-MEASURED BY G-RULING."),
    ("ad-hoc shell-typed numbers", 0, 0, "count",
     "RULING (3) / `W-ORD-ADHOC-CHECK-FIXTURES`. ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by the counter"
     " `b300_regspec.count_predictions`, IMPORTED rather than copied."),
]


def main(argv):
    print('=' * 100)
    print('b312_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
    spec = {"registration": "data/b312_registration_2026-09-03.txt -- b312, THE REMAINDER",
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
             'NONE -- the order reads and decides, and builds nothing'))
    print('  ### **TWO CAPS ARE NEW AND BOTH GUARD THE SAME TEMPTATION: `banked measurements')
    print('  ### called wrong` and `entailments run on a non-SAME verdict`.** ### This act found a')
    print('  ### discrepancy in an instrument the corpus computes with, and the whole discipline of')
    print('  ### the act is that finding one is not the same as pricing one.')
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
