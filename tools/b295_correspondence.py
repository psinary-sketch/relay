# -*- coding: utf-8 -*-
"""b295_correspondence.py -- ONE ROW FOR b295.

### **A FILINGS TOOL. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED.** ### Every grade below is
### TRANSCRIBED from its owning act's own bank, never decided here.

### ### **AND NO CELL MAY BE BLANK.** ### A statement with no terminal carries the honest cell
### ### "no terminal, and why" -- with its reason and its owning act. ### **A BLANK CELL WOULD
### ### READ AS "NOT YET DONE"; A REFUSAL READS AS "DECIDED AND WHY".**

### ### **THE IDEMPOTENCE GUARD IS KEPT (b293's D4, `W-ORD-CORRESPONDENCE-IDEMPOTENCE`):** ###
### this file carries ONE row and checks before writing that the row is not already present.

### ### ### **AND THE THING THIS ROW MUST DO THAT NO PRIOR ROW HAS HAD TO: ### IT NAMES THE
### ### ### CLAUSE OF ROW 105 IT SUPERSEDES.** ### The append-only law forbids editing row 105,
### and a table whose earlier row carries a superseded reading is a trap unless the later row says
### so in its own text. ### **SO IT SAYS SO.**
"""
import io
import os
import re
import sys

ROOT = r'D:\relay'
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

MARK = "THE SECOND MECHANISM (b295)"

# ### (statement, terminal-or-refusal, axiom-print cell, grade AS ITS OWNER LEFT IT, status)
ROWS = [
    ("THE SECOND MECHANISM (b295): the first-level pairing `<A .,.>` at `k = n` vanishes "
     "IDENTICALLY -- **as a FORM, in both slots** -- on `Son(p,n; a,b)` whenever **`a >= 0` or "
     "`b >= n-1`**. The function-side threshold is the object's own radius and does not move; the "
     "transform-side threshold is `n-1` and moves with the level; **they coincide at level 1 and "
     "nowhere else.** So b294's zero on `Son(p,n; -1,0)` is a DERIVED zero at level 1 and is **not "
     "a zero above it**: `Son(2,2; -1,0)` contains `e_2 - e_6 + e_4 - e_12` with value **4/3**, "
     "`Son(3,2; -1,0)` gives 3/4, `Son(2,3; -1,0)` and `Son(2,3; -1,+1)` give 4/7. **SUPERSEDES "
     "ROW 105's CLAUSE `zero COMPUTED for a < 0, b >= 0 by a second, underived mechanism` AND "
     "NOTHING ELSE IN THAT ROW; row 105's twenty measurements are reproduced here exactly and are "
     "not in question.** **Not a route: every nonzero member weakens the object's FIRST condition "
     "and every witness has mass ON the ball, which that condition forbids outright.**",

     "**NO TERMINAL, AND WHY -- AND BOTH TESTS WERE APPLIED, NOT ONE.** The criterion quantifies "
     "over all levels and all places and is **NOT FINITE**, so b288/b293/b294's refusals carry. "
     "The REFUTATION *is* finite-decidable and passes that test -- and is refused on the second: "
     "a terminal reading ``Son(2,2; -1,0)` pairs to 4/3` would be a TRUE sentence that reads, to "
     "anyone who has not read the scope paragraph, as a crack in the barrier, and **a terminal has "
     "no room for the paragraph.** b294's refusal is the precedent and this member is worse, "
     "because it satisfies the object's transform-side condition exactly.",

     "n/a -- refusal. The controls ran instead: b271's banked not-dead witness `<A g_0, g_0> = "
     "4(N-q)` matched at **6 of 6** cells BEFORE any zero was reported; every `a >= 0` member had "
     "the WHOLE FORM identically zero at **40 of 40**; empty members reported CANNOT TEST (46); "
     "and two exact values with their vectors were **sealed into the registration before any code "
     "existed** and landed **2 of 2**.",

     "**DERIVED for sufficiency** (from b270's pairing, b281's `A`, b293's collapse, b10's "
     "`S_quot`); **NECESSITY MEASURED at 80 live members over six cells with zero exceptions and "
     "NOT DERIVED** (`W-ORD-CRITERION-NECESSITY`). **b280 and b281 are NOT re-verdicted, extended "
     "or weakened -- they are re-measured here on the full form and PASS.** The reflection route "
     "is (ABSENT) at the owners and then REFUTED by exhibition. **No route is claimed; M-2 "
     "unchanged; nothing about `h2` beyond the register sentence.**",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    # ### IDEMPOTENCE GUARD -- b289's tool had none and duplicated nine rows on a re-run.
    if MARK in txt:
        print('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        return 0
    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('=' * 100)
    print('b295 -- THE CORRESPONDENCE TABLE, BROUGHT CURRENT.')
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

    # ### THE SUPERSESSION GATE, NEW HERE: a row that corrects an earlier one must NAME it.
    named = [r for r in ROWS if 'SUPERSEDES' in r[0] and 'ROW 105' in r[0]]
    print('  supersession named in the row text : %d/%d  %s'
          % (len(named), len(ROWS), 'PASS' if len(named) == len(ROWS) else '### FAIL ###'))
    if len(named) != len(ROWS):
        return 1

    lines = []
    for k, (stmt, term, prof, grade, status) in enumerate(ROWS):
        lines.append('| %d | %s | %s | %s | %s | %s |'
                     % (start + k, stmt, term, prof, grade, status))
    new = txt.rstrip('\n') + '\n' + '\n'.join(lines) + '\n'
    io.open(TABLE, 'w', encoding='utf-8').write(new)

    # ### READ BACK -- the tool does not trust its own write.
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
