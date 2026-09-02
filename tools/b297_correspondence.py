# -*- coding: utf-8 -*-
"""b297_correspondence.py -- THE TABLE, BROUGHT CURRENT FOR THE ARC.

### **A FILINGS TOOL. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED.** ### Every grade below is
### TRANSCRIBED from its owning act's own bank, never decided here.

### ### **WHAT THIS TOOL FOUND BEFORE IT WROTE ANYTHING, AND IT IS THE REASON IT EXISTS:** ###
### the table covered b283, b284, b285-b287, b288, b293, b294, b295 and b296 -- and carried
### ### **ZERO MENTIONS OF b289, b290, b291 OR b292.** ### Four acts of the arc had no row.
### **"CURRENT" WAS A WORD THE PRIOR ACTS USED WITHOUT ANYONE COUNTING.**

### ### **THE IDEMPOTENCE GUARD IS KEPT** ### (`W-ORD-CORRESPONDENCE-IDEMPOTENCE`, b293's D4):
### the tool checks EVERY row's marker before writing, and re-running it writes nothing.
### ### **AND NO CELL MAY BE BLANK.** ### A statement with no terminal carries the honest cell
### "no terminal, and why". ### **A BLANK CELL WOULD READ AS "NOT YET DONE"; A REFUSAL READS AS
### "DECIDED AND WHY".**
"""
import io
import os
import re
import sys

SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

# ### (marker, statement, terminal-or-refusal, axiom-print cell, grade AS ITS OWNER LEFT IT, status)
ROWS = [
    ("THE CONSOLIDATION (b289)",
     "THE CONSOLIDATION (b289): the arc's own shadows were compiled and were NOT in the standing "
     "profile -- `Core/BallAbsorptionShadow.lean` (b270) and `Core/AbsorptionFunctionalShadow.lean` "
     "(b271) were built and printed by their own acts and were **never imported by "
     "`AllPrints.lean`**, so `AXIOM_PRINTS.txt` had never carried them and their `.olean` files "
     "were not in the build cache. **The index core of every barrier statement in the arc sat "
     "outside the file that certifies the kernel.**",

     "**TERMINAL -- AND IT IS A REPAIR, NOT A NEW STATEMENT.** The two existing shadows were "
     "imported and the certification file regenerated. No new terminal was created and no "
     "mathematics was added; what changed is which already-compiled terminals the kernel's own "
     "profile can see.",

     "**CORE PRINTS 404 -> 426, ALL 426 ZERO-AXIOM** (was 404/404/0). The finding is a COUNT that "
     "any later act can re-run, which is why it is stated as one.",

     "**FILED** -- a filings act with one kernel repair. **No grade moved; no act re-verdicted.** "
     "`W-ORD-PRINT-COVERAGE` filed alongside: **25 `Core` modules remain outside the "
     "certification file, and that sweep is STILL NOT RUN**",
     "current"),

    ("THE ARCHIMEDEAN READS (b290, b291)",
     "THE ARCHIMEDEAN READS (b290, b291): the source's first obligation is **(ABSENT)** -- it does "
     "not say whether the second family's transform vanishes on the interval -- and the swap is "
     "**(PARTIAL)**, needing a step the source *uses* and does not *state*. b291 then found that "
     "step stated in one plain English sentence immediately after equation (69), where b290's "
     "search had looked for symbols: **the reflection `F_eR : S(lambda,mu) -> S(mu,lambda)` "
     "promotes to DERIVES-on-IMPORT, the corpus's archimedean member `S(1,1)` is self-dual, and "
     "the source's second paired family is REFUTED -- it is not in the Sonin space.**",

     "**NO TERMINAL, AND WHY:** these are READS OF A THIRD-PARTY SOURCE and derivations on its "
     "imported sentences. **A terminal cannot certify what a paper says**, and the corpus's rule "
     "is that an import is graded as an import. The one derivation on top of the import (the "
     "reflection) is an archimedean statement, and **b285's typing verdict governs: no finite-side "
     "structural fact types at `infinity`.**",

     "n/a -- refusal. The controls ran instead: b290's search was run in symbolic form and "
     "recorded its own miss; **b291 ran the plain-language arm and found what the symbolic arm "
     "could not reach.** That correction is a correction to a FACT -- the step was found -- and "
     "b290's (PARTIAL) is not re-verdicted.",

     "**(ABSENT)** and **(PARTIAL)** as b290 left them; **DERIVES-on-IMPORT** for the reflection "
     "and **(REFUTED)** for the cross-pairing as b291 left them. **Nothing constructed, nothing "
     "adopted, M-2 owed**",
     "current"),

    ("THE IDENTIFICATION (b292)",
     "THE IDENTIFICATION (b292): the corpus's archimedean instrument vectors and the source's are "
     "**(SAME OBJECT)** up to a nonzero scalar -- derived from two defining equations that are one "
     "equation in two notations. **Therefore b291's refutation reaches the corpus's own "
     "instruments: `zeta_n` IS NOT IN `S(1,1)`.**",

     "**NO TERMINAL, AND WHY:** the identification rests on an imported definition from a "
     "third-party source, and **a terminal would carry the corpus's name over a step whose "
     "premise is someone else's sentence.** The elementary identity underneath is finite, but "
     "certifying it would certify the algebra and not the identification.",

     "n/a -- refusal. The control that matters ran instead: **the resemblance was named and "
     "refused first** -- both vectors are built from prolate functions by authors citing the same "
     "literature with overlapping letters, and **that resemblance appears nowhere in the "
     "derivation**, which runs on two displayed equations and one elementary identity.",

     "**(SAME OBJECT)**, as b292 left it. **AND NO MEASUREMENT IS DISTURBED** -- the vectors sit "
     "outside the object's space and every banked number stands. **Nothing about the identity, "
     "`h2`, or the complete roster follows; M-2 owed**",
     "current"),

    ("THE FOLD (b297)",
     "THE FOLD (b297): the arc b283-b296 folded into `FINDINGS.md` as one dated section -- "
     "fourteen acts, 36 quotations verified verbatim against the acts that ORIGINATED them, the "
     "arc's corrections to its own readings filed as corrections to FACTS and not as re-verdicts, "
     "the kernel plan filed with its refusals, and the keystone material assembled. **NO GRADE "
     "MOVED. NO ACT RE-VERDICTED. NO NEW MATHEMATICS. NO KEYSTONE CREATED.**",

     "**NO TERMINAL, AND WHY:** a filings act has nothing to certify. It moves no grade and "
     "states no mathematics, so **there is no proposition for a terminal to be about.** The "
     "kernel plan it files names one candidate that passes both tests -- the existence statement "
     "on a relaxed member, whose terminal would NAME THE MEMBER in its own statement and so carry "
     "its scope inherently -- and **that build is the author's call and is not made here.**",

     "n/a -- refusal. The gates ran instead, all mechanical: **F-QUOTE** 36 quotations 0 "
     "unfindable with a discrimination arm that reports an altered quotation unfindable; "
     "**F-COUNT** 14 acts reconciled exactly; **F-NOGRADE** `FINDINGS.md` **+194 / -0**, purely "
     "additive; **F-NOKEYSTONE** 0 files under any keystone path; **F-NOSHADOW** 0 `.lean` files "
     "moved.",

     "**FILED.** The results in the fold are **their owning acts'**, transcribed at the grades "
     "those acts left them. **M-2 remains (SPECIFIED-NOT-STATED); the seam's debt item 1 remains "
     "unpaid; `h2` stands exactly where the deposit left it**",
     "current"),
]


def blank_cells(text):
    """### **A WHOLE-TABLE BLANK-CELL AUDIT, LINE-SCOPED.**

    ### ### **DEFECT FIXED ON THIS TOOL'S FIRST RUN, AND IT IS THE SPECIES THIS RECORD KEEPS
    ### ### FILING:** ### the first version used `\\|\\s*\\|` over the WHOLE FILE. ### In Python
    ### `\\s` matches a newline, so every row's closing `|` and the next row's opening `|` counted
    ### as a blank cell, and the check reported ### **111 BLANK CELLS IN A TABLE OF 111 ROWS** --
    ### a number whose exact agreement with the row count is the only reason it was caught.
    ### ### **A CHECK THAT REPORTS A WRONG NUMBER IS WORSE THAN NO CHECK, BECAUSE IT IS BELIEVED.**
    """
    n = 0
    for line in text.splitlines():
        if line.startswith('|'):
            n += len(re.findall(r'\|[ \t]*\|', line))
    return n


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    print('  blank cells in the whole table (line-scoped) : %d' % blank_cells(txt))
    present = [m for m, _s, _t, _p, _g, _st in ROWS if m in txt]
    if present:
        print('  ### ROW(S) ALREADY PRESENT -- NOTHING WRITTEN: %s' % present)
        return 0
    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('=' * 100)
    print('b297 -- THE CORRESPONDENCE TABLE, BROUGHT CURRENT FOR THE ARC.')
    print('=' * 100)
    print('  last existing row : %d' % max(nums))
    print('  rows to append    : %d  (numbers %d..%d)' % (len(ROWS), start, start + len(ROWS) - 1))

    # ### THE COVERAGE CHECK THIS TOOL EXISTS FOR: which arc acts had no mention at all.
    arc = ['b283', 'b284', 'b285', 'b286', 'b287', 'b288', 'b289',
           'b290', 'b291', 'b292', 'b293', 'b294', 'b295', 'b296']
    before = [a for a in arc if a not in txt]
    print('  arc acts with NO mention BEFORE this tool : %d  %s' % (len(before), before))

    blank = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if not str(c).strip()]
    print('  blank cells       : %d  %s' % (len(blank), 'PASS' if not blank else '### FAIL ###'))
    if blank:
        return 1

    refusals = [r for r in ROWS if 'NO TERMINAL' in r[2]]
    without = [r for r in refusals if 'AND WHY' not in r[2]]
    print('  refusal rows      : %d, of which without a stated reason: %d  %s'
          % (len(refusals), len(without), 'PASS' if not without else '### FAIL ###'))
    if without:
        return 1

    lines = []
    for k, (_mark, stmt, term, prof, grade, status) in enumerate(ROWS):
        lines.append('| %d | %s | %s | %s | %s | %s |'
                     % (start + k, stmt, term, prof, grade, status))
    new = txt.rstrip('\n') + '\n' + '\n'.join(lines) + '\n'
    io.open(TABLE, 'w', encoding='utf-8').write(new)

    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    after = [a for a in arc if a not in back]
    ok = (got[-len(ROWS):] == list(range(start, start + len(ROWS)))
          and all(m in back for m, _s, _t, _p, _g, _st in ROWS)
          and not after)
    print('  READ BACK         : last %d row numbers are %s' % (len(ROWS), got[-len(ROWS):]))
    print('  arc acts with NO mention AFTER  : %d  %s  %s'
          % (len(after), after, 'PASS' if not after else '### FAIL ###'))
    print('  blank cells in the whole table  : %d' % blank_cells(back))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
