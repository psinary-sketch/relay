# -*- coding: utf-8 -*-
"""b296_correspondence.py -- ONE ROW FOR b296.

### **A FILINGS TOOL. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED.** ### Every grade below is
### TRANSCRIBED from its owning act's own bank, never decided here.

### ### **AND NO CELL MAY BE BLANK.** ### A statement with no terminal carries the honest cell
### ### "no terminal, and why". ### **A BLANK CELL WOULD READ AS "NOT YET DONE"; A REFUSAL READS
### ### AS "DECIDED AND WHY".**

### ### **THE IDEMPOTENCE GUARD IS KEPT** ### (`W-ORD-CORRESPONDENCE-IDEMPOTENCE`, b293's D4):
### one row, and a check before writing that the row is not already present.

### ### **THIS ROW ### COMPLETES ### ROW 106 RATHER THAN SUPERSEDING ANY CLAUSE OF IT.** ### b295
### left the criterion sufficient and its necessity measured; b296 derives the necessity and the
### threshold's source. ### **NOTHING IN ROW 106 BECOMES FALSE, AND THE ROW SAYS SO IN ITS OWN
### TEXT RATHER THAN LEAVING A READER TO COLLATE.**
"""
import io
import os
import re
import sys

ROOT = r'D:\relay'
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

MARK = "THE ASYMMETRY AND ITS SHARPNESS (b296)"

# ### (statement, terminal-or-refusal, axiom-print cell, grade AS ITS OWNER LEFT IT, status)
ROWS = [
    ("THE ASYMMETRY AND ITS SHARPNESS (b296): the operator reads its SECOND slot by pointwise "
     "evaluation on the ball (scale `p^n`) and its FIRST slot only through the fiber sums of the "
     "reduction `Z/p^{2n} -> Z/p^{2n-1}` -- one step coarser than pointwise. **EACH THRESHOLD IS "
     "THE DISTANCE FROM THAT SLOT'S CONDITION'S OWN BASE SCALE TO THE SCALE AT WHICH THE OPERATOR "
     "READS IT**: distance `0` on the function side (level-free), distance `(2n-1)-n = n-1` on the "
     "transform side (level-carrying). So the asymmetry is not between the two conditions but "
     "between the two ways the operator reads its two slots -- **b281's `A != A^T` turned into a "
     "number.** And b295's criterion becomes an EQUIVALENCE: the form vanishes identically on "
     "`Son(p,n; a,b)` **if and only if** `a >= 0` or `b >= n-1`, necessity witnessed by ONE vector "
     "per cell, `h = e_{p^{n-1}} - e_{p^{n-1}+p^{2n-2}} + e_{p^n} - e_{p^n+p^{2n-1}}`, with "
     "`<A h, h> = 2 p^{n-1}(p-1)/(p^n-1)`. **COMPLETES ROW 106; SUPERSEDES NO CLAUSE OF IT.** "
     "**Not a route: every nonzero member weakens the object's FIRST condition and every witness "
     "has mass ON the ball, which that condition forbids outright.**",

     "**NO TERMINAL, AND WHY -- AND BOTH TESTS WERE APPLIED, NOT ONE.** The equivalence "
     "quantifies over all levels and all places in BOTH directions and is **NOT FINITE**, so "
     "b288/b293/b294/b295's refusals carry. The reading-scale measurement *is* finite-decidable "
     "and passes that test -- and is refused on the second: a terminal reading `the smallest "
     "modulus is p^{2n-1} at (2,2)` would certify a rank comparison at one cell while sitting in "
     "the kernel looking like a statement about the operator at every level, **and the sentence "
     "that bounds it is a whole derivation.** The witness values are worse, for b295's reason "
     "unchanged, and these members sit closer to the object than b294's did.",

     "n/a -- refusal. The controls ran instead: b271's banked `<A g_0, g_0> = 4(N-q)` matched at "
     "**6 of 6** cells before any zero was reported; the reading scale was measured **with no "
     "reference to `b`** and equalled the predicted `2n-1` at **6 of 6**, with both polarities "
     "firing (`p^{2n-2}` fails, `p^{2n}` works but is not minimal); every `a >= 0` member had the "
     "WHOLE FORM identically zero at **40 of 40**; **6 of 6** registered values landed exactly "
     "(5 by the general construction, 1 by a registered fallback where the construction collides "
     "at `(2,1)` and the general arm reported UNAVAILABLE, never a pass); coverage **30 of 30** "
     "live members; both negative polarities **6/6**; 46 empty members reported CANNOT TEST.",

     "**DERIVED** -- sufficiency at b295, necessity and the threshold's source at b296, each "
     "hypothesis used exactly once in the construction. **NECESSITY IS NOW DERIVED, NOT MEASURED** "
     "(`W-ORD-CRITERION-NECESSITY`, DISCHARGED). **What remains measured and not derived is that "
     "the reading scale's derivation and its measurement agree outside the six cells** "
     "(`W-ORD-READING-SCALE-GENERAL`). **b280 and b281 are NOT re-verdicted, extended or weakened "
     "-- they are re-measured here on the full form and PASS.** **CONSEQUENCE: on the object's own "
     "space the annihilation is ONE-SIDED -- the function-side condition alone gives an "
     "identically zero form at all six cells, the transform-side condition alone only at the three "
     "`n = 1` cells.** **No route is claimed; M-2 unchanged; nothing about `h2` beyond the "
     "register sentence.**",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    if MARK in txt:
        print('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        return 0
    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('=' * 100)
    print('b296 -- THE CORRESPONDENCE TABLE, BROUGHT CURRENT.')
    print('=' * 100)
    print('  last existing row : %d' % max(nums))
    print('  rows to append    : %d  (numbers %d..%d)' % (len(ROWS), start, start + len(ROWS) - 1))

    blank = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if not str(c).strip()]
    print('  blank cells       : %d  %s' % (len(blank), 'PASS' if not blank else '### FAIL ###'))
    if blank:
        return 1

    refusals = [r for r in ROWS if 'NO TERMINAL' in r[1] or 'NO NEW TERMINAL' in r[1]]
    without = [r for r in refusals if 'AND WHY' not in r[1]]
    print('  refusal rows      : %d, of which without a stated reason: %d  %s'
          % (len(refusals), len(without), 'PASS' if not without else '### FAIL ###'))
    if without:
        return 1

    # ### THE RELATION-TO-PRIOR-ROW GATE, kept from b295 and INVERTED here: b295's row superseded
    # ### a clause of row 105; this one completes row 106 and supersedes nothing. ### **EITHER WAY
    # ### THE ROW MUST SAY WHICH, BECAUSE A TABLE READ OUT OF ORDER IS THE HAZARD.**
    named = [r for r in ROWS if 'ROW 106' in r[0]
             and ('COMPLETES' in r[0] or 'SUPERSEDES' in r[0])]
    print('  relation to the prior row named in the text : %d/%d  %s'
          % (len(named), len(ROWS), 'PASS' if len(named) == len(ROWS) else '### FAIL ###'))
    if len(named) != len(ROWS):
        return 1

    lines = []
    for k, (stmt, term, prof, grade, status) in enumerate(ROWS):
        lines.append('| %d | %s | %s | %s | %s | %s |'
                     % (start + k, stmt, term, prof, grade, status))
    new = txt.rstrip('\n') + '\n' + '\n'.join(lines) + '\n'
    io.open(TABLE, 'w', encoding='utf-8').write(new)

    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    ok = got[-len(ROWS):] == list(range(start, start + len(ROWS))) and MARK in back
    print('  READ BACK         : last %d row numbers are %s  %s'
          % (len(ROWS), got[-len(ROWS):], 'PASS' if ok else '### FAIL ###'))
    print('  table rows now    : %d' % len(got))
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
