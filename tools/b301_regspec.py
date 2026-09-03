# -*- coding: utf-8 -*-
"""b301_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS ### IMPORTED ### FROM `b300_regspec.py`, NEVER COPIED.** ### That is the
### `ferry_scan.py` design point one act on: it reads the banned stems from the tools that own them
### ### **RATHER THAN COPYING THEM**, so the tools cannot drift apart. ### A second copy of the
### artifact-count counter would be a second thing to keep in step with ruling (1), and ### **THE
### DRIFT WOULD BE INVISIBLE UNTIL THE TWO DISAGREED ON A REGISTRATION.**

### ### **SO THIS FILE OWNS ITS CLAUSES AND OWNS NO ARITHMETIC.** ### Its one measured demand comes
### out of `b300_regspec.count_predictions`, whose fixtures run here before it is trusted.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402  ### the counter is READ, never copied

REG = os.path.join(ROOT, 'data', 'b301_registration_2026-09-02.txt')
SPEC = os.path.join(ROOT, 'data', 'b301_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("ad-hoc shell-typed numbers", 0, 0, "count",
     "RULING (3) / W-ORD-ADHOC-CHECK-FIXTURES (b298); b300 was the first act bound, this is the"
     " second. ### PLANNED ZERO; RE-MEASURED IN THE CLOSING BY `b301_checks.py`'s G-TOOLNUM."),
    ("floats in a deciding runner", 0, 0, "count",
     "FALSIFIER V3: the convergence re-check must run in EXACT RATIONAL ENCLOSURES, because the"
     " quantity at stake is irrational and a float comparison would decide a rounding rather than"
     " the number. ### PLANNED ZERO; RE-MEASURED IN THE CLOSING BY `b301_checks.py`'s G-EXACT,"
     " which reads the runner's own source for float literals and float division."),
    ("`.lean` files moved", 0, 0, "files",
     "THE SHADOW'S OWN EXPECTATION (V8). ### PLANNED ZERO; RE-MEASURED IN THE CLOSING BY"
     " `b301_checks.py`'s G-SHADOW against the kernel repo's working tree."),
    ("PLACE-papers files written", 0, 0, "files",
     "THE SCOPE CLAUSE and V10: term 3's row question is ROUTED, not answered by an edit, so no"
     " hook fires and the mirror does not move. ### PLANNED ZERO; RE-MEASURED IN THE CLOSING BY"
     " `b301_checks.py`'s G-NOPAPERS, with the pre-existing untracked row measured against this"
     " registration's own seal time."),
]


def main(argv):
    print('=' * 100)
    print('b301_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
    print('=' * 100)
    print('  counter source : %s' % os.path.basename(CNT.__file__))
    print('  ITS SELF-TEST, RUN HERE BEFORE IT IS TRUSTED:')
    if not CNT.self_test():
        print('  ### REFUSING TO EMIT A SPEC FROM A COUNTER THAT FAILS ITS OWN FIXTURES.')
        return 2
    print()
    print('  artifact nouns the counter can see : %s' % CNT.NOUNS.replace('|', ', '))
    print('  ### **THAT LIST IS THE WHOLE OF THE REACH, AND IT IS THE SAME LIST b300 USED.**')

    text = io.open(REG, encoding='utf-8').read()
    n, hits = CNT.count_predictions(text)
    print()
    print('  registration : %s' % os.path.basename(REG))
    print('  bytes/lines  : %d / %d' % (len(text.encode('utf-8')), len(text.splitlines())))
    print('  ### ARTIFACT-COUNT PREDICTIONS FOUND : %d' % n)
    for ln, txt in hits:
        print('      line %-4d  %s' % (ln, txt))

    clauses = [{"clause": c, "cap": cap, "demand": dem, "units": u, "from": frm}
               for (c, cap, dem, u, frm) in CLAUSES]
    clauses.append({
        "clause": "artifact counts predicted in this registration",
        "cap": 0, "demand": n, "units": "predictions",
        "from": "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by the"
                " counter `b300_regspec.count_predictions`, IMPORTED rather than copied, whose"
                " near-miss fixture is the ceiling form since **A CEILING IS A PROHIBITION AND NOT"
                " A PREDICTION.**"})

    spec = {"registration": "data/b301_registration_2026-09-02.txt -- b301, THE OBJECT COMPLETED",
            "clauses": clauses}
    d = (json.dumps(spec, indent=1, ensure_ascii=False) + '\n').encode('utf-8')
    open(SPEC + '.tmp', 'wb').write(d)
    os.replace(SPEC + '.tmp', SPEC)

    back = json.load(io.open(SPEC, encoding='utf-8'))
    ok = (len(back['clauses']) == len(clauses)
          and back['clauses'][-1]['demand'] == n
          and all(str(c.get('from', '')).strip() for c in back['clauses']))
    print()
    print('  spec written and READ BACK : %s  clauses=%d  no empty provenance cell : %s'
          % (os.path.basename(SPEC), len(back['clauses']), ok))
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
