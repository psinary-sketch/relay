# -*- coding: utf-8 -*-
"""b321_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**

### ### ### **THE CAP THAT IS NEW HERE, AND IT IS THE ACT: ### `interpretations of the window's
### ### balance` -- CAPPED AT ZERO.** ### b320 capped `windows opened` at zero because its order
### forbade the window. ### **THIS ACT'S ORDER OPENS IT**, so that cap is raised to the number of
### cells above the boundary and a narrower one takes over what it was really protecting: ### the
### act may COMPUTE and PRINT the balance and may not say what it MEANS.
### ### **AND `bars widened after a value was seen` STAYS AT ZERO**, re-measured by `G-NOWIDEN`
### against a seal hash written as a literal into the gate suite.
### ### **`claims about h2, the identity's truth, or the complete roster` IS ALSO ZERO**, because a
### window act is exactly the act that would be tempted to reach for one.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b321_registration_2026-09-04.txt')
SPEC = os.path.join(ROOT, 'data', 'b321_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("bars widened after a value was seen", 0, 0, "bars",
     "### **CARRIED FROM b320 AND STILL THE ONE A FAVOURABLE RESULT WOULD TEMPT THIS SEAT TO"
     " BREACH.** ### RE-MEASURED BY `G-NOWIDEN`, which compares the sealed hash against a literal"
     " written into the gate suite before the first control was run."),
    ("interpretations of the window's balance", 0, 0, "readings",
     "### **NEW THIS ACT, AND IT REPLACES b320's `windows opened`.** ### The order says the window"
     " numbers are a measurement `interpreted by nobody in this act`. ### The act may compute and"
     " print the balance; it may not say what it means. ### RE-MEASURED BY `G-NOREAD`."),
    ("claims about h2, the identity's truth, or the complete roster", 0, 0, "claims",
     "### **A WINDOW ACT IS EXACTLY THE ACT THAT WOULD REACH FOR ONE.** ### The order forbids all"
     " three by name. ### RE-MEASURED BY the bank's must-fail lines."),
    ("theorems the instrument is tested against", 3, 3, "theorems",
     "### **RAISED FROM b320's ONE.** ### Theorem 1 (b320), Theorem 4.7 and the explicit formula"
     " (148). ### **BEING TESTED AGAINST A THEOREM IS NOT PROVING IT** and the next clause holds"
     " that line."),
    ("claims to have proved any of them", 0, 0, "claims",
     "### The source proved all three. ### A control that holds certifies the INSTRUMENT at exactly"
     " the scope of the control and nothing else."),
    ("cells above the boundary reported", 10, 10, "cells",
     "### **THE WINDOW ITSELF.** ### Ten of the thirteen atlas cells fail Theorem 1's support"
     " condition; b320 printed them as data with no claim, and this act reports their balance."),
    ("remainder instruments used", 1, 1, "files",
     "### `tools/e16/b313f_qeps_layer.py`, THE b313 FLIPPED COPY, on b313's READING of three source"
     " sites and on no number. ### The owner file is untouched and the other copy's value is"
     " printed beside it."),
    ("owner instrument files edited", 0, 0, "files",
     "b316-b320's tools and the e16 owners are imported, not edited."
     " ### RE-MEASURED BY G-NOEDIT against `git HEAD`."),
    ("archimedean units used", 0, 0, "units",
     "carried from b316 onward, and back to zero after b319's order forced one."
     " ### RE-MEASURED BY `G-NOUNIT` over STRIPPED code."),
    ("verdicts on membership", 0, 0, "verdicts", "`W-ORD-ARCH-MEMBERSHIP` is open and untouched."),
    ("acts re-verdicted", 0, 0, "acts", "b316 through b320 stand."),
    ("banked measurements called wrong", 0, 0, "measurements", "carried from b312 onward."),
    ("grades moved", 0, 0, "grades", "F-G."),
    ("`.lean` files created or edited", 0, 0, "files",
     "back to zero after b319's repair. ### RE-MEASURED BY `git status --short -- *.lean`."),
    ("modules added to the certification file", 0, 0, "modules", "back to zero after b319."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows",
     "the append-only law. ### RE-MEASURED BY A TRUE-PREFIX CHECK AGAINST `git HEAD`."),
    ("PLACE-papers files written", 0, 0, "files", "no hook fires and no mirror moves."),
    ("keystone files written", 0, 0, "files", "no keystone is written or edited."),
    ("aggregations stated", 0, 0, "statements", "`M-2` IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("float literals in a deciding runner", 0, 0, "literals",
     "the bars live in the tools. ### RE-MEASURED BY G-NOFLOAT."),
    ("controls reported as a pass that could not fire", 0, 0, "controls",
     "b308's law. ### Each control carries an arm that fails on a deliberately broken input."),
    ("point verdicts taken from a refused axis", 0, 0, "verdicts",
     "the noise-floor gate is in the path, and a refused value has its SIGN reported and not its"
     " SIZE, in two different columns."),
    ("quantities reported as two routes that share an evaluator", 0, 0, "quantities",
     "### **THE ONE THIS ACT DECLARES IN ADVANCE.** ### There is exactly one implementation of the"
     " source's (84) in this corpus, so the remainder integral is ONE route with two quadratures"
     " and (B1d) says so before the value exists."),
    ("ad-hoc shell-typed numbers", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by the counter"
     " `b300_regspec.count_predictions`, IMPORTED rather than copied."),
]


def main(argv):
    print('=' * 100)
    print('b321_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
            "data/b321_registration_2026-09-04.txt -- b321, THE WINDOW OPENED",
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
    print('  ### **THREE NONZERO CAPS, AND TOGETHER THEY ARE THE ACT.** ### Two more theorems as')
    print('  ### controls; the ten cells above the boundary REPORTED; and ONE remainder instrument,')
    print("  ### the b313 flipped copy, chosen on b313's reading of three source sites and on no")
    print('  ### number this act computes. ### **AND EACH RAISED CAP HANDS ITS PROTECTION TO A')
    print('  ### ### NARROWER ONE**: `claims to have proved any of them` at zero, `interpretations')
    print("  ### of the window's balance` at zero, and the other copy's value printed beside.")
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
