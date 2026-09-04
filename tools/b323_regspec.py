# -*- coding: utf-8 -*-
"""b323_regspec.py -- THE REGISTRATION'S SATISFIABILITY SPEC, ### **COMPUTED, NOT TYPED.**

### ### **THE COUNTER IS IMPORTED FROM `b300_regspec.py`, NEVER COPIED.**

### ### ### **A FILINGS ACT'S CAPS ARE ALMOST ALL ZERO, AND THAT IS THE HONEST SHAPE OF ONE.** ###
### The single nonzero cap is `acts folded` = 9. ### Everything else the act might do, it may not.
### ### **THE TWO THAT MATTER MOST: ### `grades moved` AND `numbers in the section not already
### ### banked by an act in the arc`.** ### A fold may rearrange the record and may not add to it,
### and neither is left as a promise: the first is a TRUE-PREFIX test on `FINDINGS.md`, the second
### is `F-QUOTE` running as a GENERATOR so that an unverified sentence never reaches the file.
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b300_regspec as CNT  # noqa: E402

REG = os.path.join(ROOT, 'data', 'b323_registration_2026-09-04.txt')
SPEC = os.path.join(ROOT, 'data', 'b323_satisfiable.json')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CLAUSES = [
    ("acts folded", 9, 9, "acts",
     "### **THE ONLY NONZERO CAP, AND IT IS THE ACT.** ### b314 through b322, nine acts, each with"
     " its grade AS ITS OWN ACT LEFT IT, its scope sentence, and an obstacle quoted verbatim from"
     " it. ### RE-MEASURED BY `F-COUNT`, which requires results and obstacles to cover the arc"
     " EXACTLY -- **AN ACT LEFT OUT OF A FOLD IS AN ACT QUIETLY DROPPED FROM THE RECORD.**"),
    ("grades moved", 0, 0, "grades",
     "### **F-G, AND FOR A FOLD IT IS THE CENTRAL ONE.** ### Every grade is carried as its own act"
     " left it. ### RE-MEASURED BY a TRUE-PREFIX test of `FINDINGS.md` against its pre-append"
     " bytes AND against the stored blob at HEAD -- b309's trap is that `core.autocrlf` makes the"
     " working file differ from the blob on a clean tree."),
    ("numbers in the section not already banked by an act in the arc", 0, 0, "numbers",
     "### **A FOLD MAY REARRANGE THE RECORD AND MAY NOT ADD TO IT.** ### RE-MEASURED BY `F-QUOTE`"
     " running as a GENERATOR: a quotation that fails it never reaches `FINDINGS.md` at all."),
    ("quotations not verified against their ORIGINATING act", 0, 0, "quotations",
     "### **b283's LAW.** ### A quotation of a quotation is not a source. ### The mechanical check"
     " is `in the originating file`; the JUDGEMENT that the sentence is that act's own voice is"
     " THIS SEAT'S and the bank declares it as this seat's."),
    ("acts re-verdicted", 0, 0, "acts",
     "### **b314 THROUGH b322 ALL STAND AT THEIR OWN GRADES**, including the two whose sealed bars"
     " b322 found defective -- filing a defect is not re-verdicting the act that declared it."),
    ("new mathematical results", 0, 0, "results", "no computation runs in this act."),
    ("keystone files written", 0, 0, "files",
     "### **THE KEYSTONE RE-READ IS NAMED AS NEXT AND IS NOT DONE HERE**, which is the order's own"
     " sequencing: the fold first, the keystone after it."),
    ("`FINDINGS.md` lines removed or altered", 0, 0, "lines",
     "purely additive, and the check is a byte prefix rather than a sentence about intent."),
    ("mirrors verified on fewer than three clauses", 0, 0, "mirrors",
     "### **A CLEAN CLAUSE 1 ON A STALE BUILD IS EXACTLY AS CLEAN-LOOKING AS A CORRECT ONE**, and"
     " at b182 a build verified CLEAN on both then-existing clauses at 33 files WITHOUT THE FILE IN"
     " IT. ### Clause 3 is the only one that can see a file that never entered the staging"
     " directory."),
    ("mirrors rebuilt BEFORE the commit", 0, 0, "mirrors",
     "### **THE ORDER IS PART OF THE BAR.** ### A mirror built before the commit declares a source"
     " HEAD the push then moves, and clause 2 would be checking a pin that no longer exists."),
    ("bars widened after a value was seen", 0, 0, "bars",
     "carried from b320, b321 and b322. ### RE-MEASURED BY `G-NOWIDEN` against a seal hash written"
     " as a literal into the gate suite."),
    ("banked measurements called wrong", 0, 0, "measurements", "carried from b312 onward."),
    ("owner instrument files edited", 0, 0, "files",
     "nothing in `tools/` outside this act's own files is touched."
     " ### RE-MEASURED BY G-NOEDIT against `git HEAD`."),
    ("`.lean` files created or edited", 0, 0, "files", "back to zero after b319's repair."),
    ("modules added to the certification file", 0, 0, "modules", "back to zero after b319."),
    ("ancestors' correspondence rows rewritten", 0, 0, "rows",
     "the append-only law. ### RE-MEASURED BY A TRUE-PREFIX CHECK AGAINST `git HEAD`."),
    ("aggregations stated", 0, 0, "statements", "`M-2` IS OWED AND STAYS OWED."),
    ("verdicts on M-2", 0, 0, "verdicts", "carried from b310."),
    ("claims about h2 beyond the register sentence", 0, 0, "claims",
     "h2 stands exactly where the deposit left it."),
    ("float literals in a deciding runner", 0, 0, "literals",
     "the fold's numbers are strings quoted from banks, not computed."),
    ("controls reported as a pass that could not fire", 0, 0, "controls",
     "b308's law. ### `F-QUOTE` carries a discrimination arm: an ALTERED quotation is fed to the"
     " same matcher and must come back unfindable."),
    ("ad-hoc shell-typed numbers", 0, 0, "count", "RULING (3). ### RE-MEASURED BY G-TOOLNUM."),
    ("artifact counts predicted in this registration", 0, None, "predictions",
     "RULING (1), U-1 STRUCK. ### MEASURED off this registration's own text by the counter"
     " `b300_regspec.count_predictions`, IMPORTED rather than copied."),
]


def main(argv):
    print('=' * 100)
    print('b323_regspec.py -- THE SATISFIABILITY SPEC. ### THE COUNTER IS IMPORTED, NOT COPIED.')
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
            "data/b323_registration_2026-09-04.txt -- b323, THE FOLD",
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
    print('  ### **ONE NONZERO CAP, AND IT IS THE ACT: ### `acts folded` = 9.** ### Every other')
    print('  ### cap is ZERO, which is what a filings act looks like when its caps are written')
    print('  ### honestly. ### **THE TWO THAT MATTER MOST ARE `grades moved` AND `numbers in the')
    print('  ### ### section not already banked by an act in the arc`** -- a fold may rearrange the')
    print('  ### record and may not add to it, and both are re-measured mechanically.')
    print('=' * 100)
    return 0 if (ok and not unsat) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
