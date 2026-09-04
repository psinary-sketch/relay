# -*- coding: utf-8 -*-
"""b324_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**

### ### ### **THE CAP THAT CARRIES THIS ACT: ### `verdicts resting on a shared word` -- ZERO.** ###
### The order refuses resemblance ### **BY NAME** ### -- "space", "wall", "margin", "room",
### "silence" -- because an act comparing a deposited corpus with a computational arc will find
### agreement everywhere if a shared word counts. ### Both write English about the same subject.
### ### **AND ITS SIBLING: ### `contacts typed REFINEMENT-OF-DEPOSITED whose claim is not in the
### ### deposit` -- ZERO.** ### The deposit is ms v5.10.2; the keystones this act turns on are
### v5.13 and INTERNAL. ### **A CLAIM THAT LIVES ONLY INTERNALLY CANNOT BE REFINED FROM THE
### ### DEPOSIT**, and the phrase census measures which is which rather than trusting familiarity.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b324_registration_2026-09-04.txt')
SPEC = os.path.join(ROOT, 'data', 'b324_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("precise questions decided", 2, 2, "questions",
     "### **THE WALL and THE MARGIN**, each decided by DEFINITIONS and quotations, each with three"
     " verdict shapes fixed before the evidence and each carrying a registered expectation that"
     " can be refuted by a quotation."),
    ("contacts mapped", 7, 7, "contacts",
     "### the silence keystone, the confinement keystone, the third identity element, spectral"
     " inertness, the seven classes, exhaustive enumeration, and the monograph -- each with a"
     " verdict SAID FIRST / CORROBORATED / UNTOUCHED / IN TENSION, **the last at full prominence**."),
    ("verdicts resting on a shared word", 0, 0, "verdicts",
     "### **THE CAP THIS ACT WOULD MOST EASILY BREACH.** ### The order refuses resemblance BY NAME."
     " ### The operational test: if the argument would survive replacing one side's technical term"
     " with a synonym the other side does not use, it was a resemblance argument."
     " ### RE-MEASURED BY `G-NORESEMBLE`."),
    ("contacts typed REFINEMENT-OF-DEPOSITED whose claim is not in the deposit", 0, 0, "contacts",
     "### The deposit is ms v5.10.2 at `outputs/DEPOSITED-v1.1.2/`, md5-verified against Zenodo;"
     " the residue and balance keystones are v5.13 and INTERNAL. ### RE-MEASURED BY the phrase"
     " census, which counts each phrase in both paths."),
    ("keystones edited other than by an appended cross-reference line", 0, 0, "edits",
     "### **APPEND-ONLY, ORIGINALS VISIBLE.** ### RE-MEASURED BY a TRUE-BYTE-PREFIX test against"
     " the working file AND the blob at HEAD."),
    ("files under `outputs/DEPOSITED-v1.1.2/` written", 0, 0, "files",
     "### **NO DEPOSITED TEXT IS TOUCHED, IN ANY WAY, FOR ANY REASON.** ### RE-MEASURED"
     " MECHANICALLY by `git status` over that path."),
    ("new mathematical results", 0, 0, "results", "no computation runs in this act."),
    ("grades moved", 0, 0, "grades", "F-G."),
    ("acts re-verdicted", 0, 0, "acts",
     "the nine acts of the arc stand at their own grades, and so do the keystones."),
    ("recommendations on the wave's candidate list", 0, 0, "recommendations",
     "### **THE LIST IS TYPED, NOT RANKED.** ### The order says `with no recommendation`, and the"
     " wave is the author's."),
    ("claims about h2 beyond the register sentence", 0, 0, "claims",
     "h2 stands exactly where the deposit left it."),
    ("bars widened after a verdict was seen", 0, 0, "bars",
     "carried from b320 onward. ### RE-MEASURED BY `G-NOWIDEN` against a seal hash written as a"
     " literal into the gate suite before any verdict."),
    ("banked measurements called wrong", 0, 0, "measurements", "carried from b312 onward."),
    ("owner instrument files edited", 0, 0, "files",
     "a reads act edits no instrument. ### RE-MEASURED BY G-NOEDIT against `git HEAD`."),
    ("`.lean` files created or edited", 0, 0, "files", "back to zero after b319's repair."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows",
     "the append-only law. ### RE-MEASURED BY A TRUE-PREFIX CHECK AGAINST `git HEAD`."),
    ("aggregations stated", 0, 0, "statements", "`M-2` IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("float literals in a deciding runner", 0, 0, "literals",
     "the act's numbers are quotations, not computations."),
    ("controls reported as a pass that could not fire", 0, 0, "controls",
     "b308's law. ### The phrase census can return INTERNAL, and both registered expectations can"
     " be refuted by a quotation."),
    ("ad-hoc shell-typed numbers", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by the counter"
     " `b300_regspec.count_predictions`, IMPORTED rather than copied."),
]


def main(argv):
    print('=' * 100)
    print('b324_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
            "data/b324_registration_2026-09-04.txt -- b324, THE KEYSTONES RE-READ",
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
    print('  ### **TWO NONZERO CAPS, AND THEY ARE THE ACT: ### `precise questions decided` = 2')
    print('  ### and `contacts mapped` = 7.** ### Every other cap is ZERO. ### **THE ONE THAT MATTERS')
    print('  ### ### MOST IS `verdicts resting on a shared word`**, because an act comparing a')
    print('  ### deposited corpus with a computational arc finds agreement everywhere if a shared')
    print('  ### word counts -- and the order refuses resemblance BY NAME for exactly that reason.')
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
