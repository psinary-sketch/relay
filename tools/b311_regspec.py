# -*- coding: utf-8 -*-
"""b311_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED** -- the standing design
### point, carried since b302.

### ### **EVERY CAP IS ZERO THIS ACT**, which is the order's doing: it is reads and a definitional
### decision. ### **THREE OF THE CAPS ARE NEW AND EACH GUARDS A DIFFERENT WAY THIS ACT COULD DRIFT:**
###   ### **`archimedean numbers computed`** ### -- the order forbids one, and the temptation is
###     real: the source hands over `13 < c < 17`, `c = 4γ/log 2` and an explicit `τ(ρ)`, and
###     ### **QUOTING A NUMBER IS NOT COMPUTING ONE, BUT THE LINE IS EASY TO CROSS.**
###   ### **`finite-side results transported`** ### -- b285's hazard register exists because the
###     words survive the crossing when the objects do not.
###   ### **`rulings applied`** ### -- the author's `W2` is to be RECORDED and not acted on, which
###     is the ruling's own instruction, and a cap is cheaper than a resolution.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402  ### the counter is READ, never copied

REG = os.path.join(ROOT, 'data', 'b311_registration_2026-09-03.txt')
SPEC = os.path.join(ROOT, 'data', 'b311_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("`.lean` modules created", 0, 0, "modules",
     "THE SHADOW IS EXPECTED TO BE NOTHING: a quotation is not decidable and a definitional"
     " decision about an infinite-dimensional Hilbert space is not finite-decidable."),
    ("profile files rewritten", 0, 0, "files",
     "the same clause. ### RE-MEASURED IN THE CLOSING against `git HEAD`, NORMALISED and with the"
     " baseline FOUND rather than assumed -- b309's (D6), both halves."),
    ("PLACE-papers files written", 0, 0, "files",
     "F-C. ### RE-MEASURED BY G-NOPAPERS against `git status --porcelain` in that repository."),
    ("keystone files written", 0, 0, "files", "no keystone is written or edited."),
    ("grades moved", 0, 0, "grades",
     "F-F. ### A read moves no grade, and a decision at definitions moves none either."),
    ("acts re-verdicted", 0, 0, "acts",
     "F-F. ### b310's finite-side sentence is TESTED FOR TRANSPORTABILITY, not overturned; b292's"
     " and b300's archimedean rows are carried at their own grades."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows",
     "the append-only law, F-K. ### RE-MEASURED BY A TRUE-PREFIX CHECK AGAINST `git HEAD`."),
    ("aggregations stated", 0, 0, "statements",
     "`M-2` IS OWED AND STAYS OWED. ### RE-MEASURED BY the must-fail fixtures."),
    ("branch decisions", 0, 0, "decisions",
     "carried from b310. ### b262's disjunction is undecided and this act does not decide it."),
    ("verdicts on M-2", 0, 0, "verdicts",
     "carried from b310. ### The cap travels with the act, not with the component that provoked"
     " it."),
    ("archimedean numbers computed", 0, 0, "numbers",
     "### **NEW THIS ACT.** ### THE ORDER: *NO archimedean number computed*. ### Every archimedean"
     " quantity named is the SOURCE'S, at the source's grade, and QUOTING a number is not"
     " COMPUTING one. ### RE-MEASURED BY G-NOARCHNUM over the act's own prose and by G-TOOLNUM,"
     " which would have no committed producer to point at for a computed one."),
    ("finite-side results transported", 0, 0, "transports",
     "### **NEW THIS ACT.** ### b285's HAZARD REGISTER: the words BALL, LEVEL, TOWER, UNIT, SECTOR,"
     " SCALE survive the crossing where the objects do not. ### RE-MEASURED BY G-QUARANTINE, whose"
     " must-fail fixtures assert whole-line absence of the sentences a transport would produce."),
    ("rulings applied", 0, 0, "rulings",
     "### **NEW THIS ACT.** ### The author's `W2` is RECORDED VERBATIM, attributed, marked"
     " strikeable, and NOT acted on -- which is the ruling's own instruction. ### RE-MEASURED BY"
     " G-RULING."),
    ("ad-hoc shell-typed numbers", 0, 0, "count",
     "RULING (3) / `W-ORD-ADHOC-CHECK-FIXTURES`, and F-I. ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK, F-L. ### MEASURED off this registration's own text by the counter"
     " `b300_regspec.count_predictions`, IMPORTED rather than copied."),
]


def main(argv):
    print('=' * 100)
    print('b311_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
            "data/b311_registration_2026-09-03.txt -- b311, THE IDENTITY'S NEIGHBOURHOOD",
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
    print('  ### **THREE CAPS ARE NEW: `archimedean numbers computed`, `finite-side results')
    print('  ### transported`, `rulings applied`.** ### Each guards a different way this act could')
    print('  ### drift, and each is measured over the act\'s own prose rather than trusted.')
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
