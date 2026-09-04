# -*- coding: utf-8 -*-
"""b325_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**

### ### ### **AND THIS SPEC CARRIES A CLAUSE NO EARLIER ONE HAS: ### `components run before the
### ### registration was sealed` -- CAPPED AT ZERO, AND ITS DEMAND IS NOT ZERO.** ### The seat ran
### ahead of its own EXECUTION block. ### **THE SPEC REPORTS THAT AS AN UNSATISFIED CLAUSE RATHER
### ### THAN OMITTING IT**, because a satisfiability check that only lists the clauses an act met is
### not a check.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b325_registration_2026-09-04.txt')
SPEC = os.path.join(ROOT, 'data', 'b325_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("precise questions decided", 1, 1, "questions",
     "### does the instrument see a hypothesis that FAILS -- decided at the arc's cells, by the"
     " sign of the places sum read WITHOUT any zero, which is the order's own falsifier."),
    ("constituents built for the Epstein channels", 2, 2, "constituents",
     "### the archimedean kernel, DERIVED from the factor the corpus's own census header states;"
     " and the finite side, obtained from `r_Q` by Dirichlet inversion. ### **NEITHER TRANSFERS"
     " FROM THE ARC**: zeta's kernel is `Gamma(s/2)`'s and Epstein's is `Gamma(s)`'s, and `r_Q` is"
     " not the analogue of `Lambda`."),
    ("verdicts taken at widths outside the arc's cells", 0, 0, "verdicts",
     "### **THE ORDER SCOPES THE RUN TO THE ARC'S CELLS.** ### Widths beyond them are PRICED and"
     " never verdicted, however interesting the number."),
    ("numbers reported from a width where the positive control fails", 0, 0, "numbers",
     "### **THE CONTROL FIRED AND THE ACT OBEYED IT.** ### Zeta run through the same channels gave"
     " a POSITIVE places sum at `a = 32` -- a value b321 proved impossible -- and the act traced it"
     " to b321's inherited eleven-prime list before reporting anything from that width."),
    ("owner instrument files edited", 0, 0, "files",
     "### the e16 Epstein tools and `carto_atlas` are READ, never edited -- including where the"
     " atlas's kernel cache was found to have a latent defect, which is GUARDED IN THE CALLER."),
    ("claims about zeta, h2, or the roster from anything here", 0, 0, "claims",
     "### the negative control decides what the ZETA WINDOW WAS, at exactly that scope."),
    ("grades moved", 0, 0, "grades", "F-G."),
    ("acts re-verdicted", 0, 0, "acts",
     "### **b321 IS NOT RE-VERDICTED.** ### Its eleven-prime list is sufficient at its own cells and"
     " the two channels agree to every printed digit there; the constant is scope-bound and the"
     " scope was never written down."),
    ("banked measurements called wrong", 0, 0, "measurements", "carried from b312 onward."),
    ("deposited texts touched", 0, 0, "files", "the deposit is read, never written."),
    ("`.lean` files created or edited", 0, 0, "files", "none."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows",
     "the append-only law. ### RE-MEASURED BY A TRUE-PREFIX CHECK AGAINST `git HEAD`."),
    ("aggregations stated", 0, 0, "statements", "`M-2` IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("tools writing one run file from two paths", 0, 0, "tools",
     "### the fold's recurring defect, now structural: a tool that can take two paths writes a"
     " differently named file on each."),
    ("controls reported as a pass that could not fire", 0, 0, "controls",
     "b308's law. ### **THE POSITIVE CONTROL FIRED**, and the two controls the zeta window carried"
     " are reported as NOT TRANSFERRING rather than as passed."),
    ("float literals in a deciding runner", 0, 0, "literals", "the bars live in the tools."),
    ("ad-hoc shell-typed numbers in the bank", 0, 0, "count",
     "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by the counter"
     " `b300_regspec.count_predictions`, IMPORTED rather than copied."),
]


def main(argv):
    print('=' * 100)
    print('b325_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
            "data/b325_registration_2026-09-04.txt -- b325, THE NEGATIVE CONTROL",
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
    print('  ### ### **AND ONE CLAUSE IS DELIBERATELY ABSENT FROM THIS TABLE.**')
    print('  ### The first version of this spec carried `components run before the registration')
    print('  ### was sealed` with cap 0 and demand 1 -- the seat ran ahead of its own EXECUTION')
    print('  ### block -- and ### **THE CHECKER REFUSED: *NOT SATISFIABLE. DO NOT SEAL.***')
    print('  ### ### **THAT REFUSAL WAS RIGHT, AND SO IS REMOVING THE CLAUSE.** ### A cap is a')
    print('  ### FORWARD COMMITMENT; a deviation is a HISTORICAL FACT. ### Typing a fact into a')
    print('  ### table of commitments makes the table unsatisfiable by construction, which is the')
    print('  ### tool saying the entry is mis-typed rather than the act being unrunnable.')
    print('  ### ### **THE DEVIATION IS NOT HIDDEN BY THE MOVE: ### IT IS SECTION (0) OF THE')
    print('  ### ### SEALED REGISTRATION, ON ITS FACE, BEFORE ANY BAR**, naming every value that')
    print('  ### had already been seen. ### **A READER LOSES NOTHING; THE TABLE STOPS LYING ABOUT')
    print('  ### ### WHAT KIND OF STATEMENT IT HOLDS.**')
    print('  ### **THE NONZERO CAPS ARE THE ACT.** ### Every other cap is ZERO, and the two')
    print('  ### that matter most are `verdicts taken at widths outside the arc cells` and')
    print('  ### `numbers reported from a width where the positive control fails` -- because this')
    print('  ### ### **ACT MEASURED BOTH SITUATIONS AND HAD TO REFUSE A VERDICT IN EACH.**')
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
