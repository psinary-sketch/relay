# -*- coding: utf-8 -*-
"""b319_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**

### ### ### **TWO CAPS THAT WERE ZERO FOR SIXTEEN ACTS ARE NOT ZERO HERE, AND THAT IS THE POINT OF
### ### THE ACT.** ### `modules added to the certification file` and `` `.lean` files created or
### edited `` have been zero since b314 because no act was authorised to repair the kernel-coverage
### defect. ### **THIS ACT'S ORDER PUTS THAT REPAIR IN STEP ZERO**, so the caps are raised to
### exactly what the repair does and no more: ### **ONE `.lean` FILE** ### -- the certification file
### -- and ### **TWENTY-FOUR MODULES**. ### `Core/` modules edited stays at ZERO: the repair adds
### imports and print lines, it does not touch a proof.
### ### **AND `rank-stable schemes built` GOES FROM b318's ZERO TO ONE**, because b318 specified it
### and this act is the build it specified.

### ### **ONE CAP CHANGES SHAPE RATHER THAN VALUE.** ### b317 and b318 capped `archimedean units
### constructed` at zero and re-measured it by refusing any `sonin_unit` call. ### **THIS ACT'S
### ### COMPONENT 3 ORDERS THE UNIT'S RESIDUAL RECOMPUTED**, so the cap becomes `units DEFINED` --
### b316's construction is IMPORTED and evaluated, and no new one is written -- with
### `verdicts on membership` still at zero, which is what the old cap was really protecting.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b319_registration_2026-09-04.txt')
SPEC = os.path.join(ROOT, 'data', 'b319_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("`.lean` files created or edited", 1, 1, "files",
     "### **RAISED FROM ZERO BY THIS ACT'S ORDER.** ### Exactly one: the certification file"
     " `AllPrints.lean`. ### RE-MEASURED BY `G-ONELEAN` against `git status` in the kernel repo."),
    ("`Core/` module files edited", 0, 0, "files",
     "### **AND THIS ONE STAYS AT ZERO**, which is what keeps the repair bookkeeping rather than"
     " mathematics: imports and print lines were added, no proof was touched."),
    ("modules added to the certification file", 24, 24, "modules",
     "### **RAISED FROM ZERO BY THIS ACT'S ORDER**, to exactly what the gate named."),
    ("pre-existing prints changed", 0, 0, "prints",
     "### **THE REPAIR'S OWN CENTRAL CONSTRAINT.** ### The old profile must be a literal byte"
     " PREFIX of the new one. ### RE-MEASURED BY `G-PREFIX` off the repair's log."),
    ("axiom-bearing terminals not reported", 0, 0, "terminals",
     "the profile is banked AS IT PRINTS. ### If a newly-certified terminal bears an axiom it is"
     " reported at full prominence. ### RE-MEASURED BY `G-ASPRINTED`."),
    ("rank-stable schemes built", 1, 1, "schemes",
     "### **RAISED FROM b318's ZERO.** ### b318 specified two and built neither; this act builds"
     " the source's own. ### RE-MEASURED BY `G-SCHEMEBUILT`."),
    ("archimedean units DEFINED", 0, 0, "definitions",
     "### **THE CAP CHANGES SHAPE, NOT PURPOSE.** ### Component 3 orders the unit's residual"
     " recomputed, so b316's construction is IMPORTED and evaluated and no new one is written."
     " ### RE-MEASURED BY `G-UNITIMPORTED` against this act's own tools."),
    ("verdicts on membership", 0, 0, "verdicts",
     "### **WHAT THE OLD CAP WAS REALLY PROTECTING.** ### The residual is a MEASUREMENT reported"
     " beside b316's; the decision stays the membership act's."),
    ("test functions defined", 0, 0, "definitions",
     "b317's variant is IMPORTED from its emitting file and reused; no new one is constructed."),
    ("W_infinity evaluations", 0, 0, "evaluations",
     "carried from b318. ### Neither side of the source's inequality is computed."),
    ("acts re-verdicted", 0, 0, "acts",
     "### **THE ONE THAT MATTERS THIS ACT.** ### A different cut is a different cut. ### b316's,"
     " b317's and b318's numbers stand on theirs, both cuts are reported, and no grade moves."),
    ("banked measurements called wrong", 0, 0, "measurements", "carried from b312, b313, b317."),
    ("grades moved", 0, 0, "grades", "F-G."),
    ("owner instrument files edited", 0, 0, "files",
     "`b316_instrument.py`, `b317_smear.py`, `b318_square.py` and `b315_coverage_gate.py` are"
     " OWNERS and are imported, not edited -- including the gate whose own prose is now stale."
     " ### RE-MEASURED BY G-NOEDIT against `git HEAD`."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows",
     "the append-only law. ### RE-MEASURED BY A TRUE-PREFIX CHECK AGAINST `git HEAD`."),
    ("PLACE-papers files written", 0, 0, "files",
     "nothing in the papers repository is touched, so no hook fires and no mirror moves."),
    ("keystone files written", 0, 0, "files", "no keystone is written or edited."),
    ("aggregations stated", 0, 0, "statements", "`M-2` IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("float literals in a deciding runner", 0, 0, "literals",
     "the threshold and the bars live in the tools. ### RE-MEASURED BY G-NOFLOAT."),
    ("controls reported as a pass that could not fire", 0, 0, "controls",
     "b308's law. ### The threshold's own fixture shows the selection can change its mind."),
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
            "data/b319_registration_2026-09-04.txt -- b319, THE STABLE RANK",
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
    print('  ### **THREE NONZERO CAPS, AND EVERY ONE OF THEM IS THE ORDER SPEAKING.** ### Sixteen')
    print('  ### acts kept `.lean` and the certification file at zero because no act was')
    print('  ### authorised to repair them. ### **THIS ONE IS**, and the caps are raised to exactly')
    print('  ### what the repair does. ### `Core/` modules edited stays at ZERO.')
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
