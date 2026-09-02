# -*- coding: utf-8 -*-
"""b294_correspondence.py -- ONE ROW FOR b294.

### **A FILINGS TOOL. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED.** ### Every grade below is
### TRANSCRIBED from its owning act's own bank, never decided here.

### ### **THE POINT OF THIS FILE, AND THE REASON IT IS A COMMITTED TOOL RATHER THAN A HAND EDIT:**
### ### **THE ROW TABLE BELOW IS THE SINGLE SOURCE OF TRUTH AND THIS RUNNER WRITES THE MARKDOWN.**
### ### **AND NO CELL MAY BE BLANK.** ### A statement with no terminal carries the honest cell
### ### "no terminal, and why" -- drawn from the refusal list, with its reason and its owning act.
### ### **A BLANK CELL WOULD READ AS "NOT YET DONE"; A REFUSAL READS AS "DECIDED AND WHY".**

### ### **AND A DEFECT b289 LEFT AND THIS FILE FIXES: ### b289's TOOL HELD THE WHOLE ARC'S
### ### ROWS, SO RE-RUNNING IT APPENDED ALL NINE AGAIN. ### IT IS NOT IDEMPOTENT AND WAS NOT
### ### BUILT TO BE. ### THIS FILE CARRIES ONLY THIS ACT'S ROW, AND CHECKS BEFORE WRITING
### ### THAT THE ROW IS NOT ALREADY PRESENT.**
"""
import io
import os
import re
import sys

ROOT = r'D:\relay'
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

# ### (statement, terminal-or-refusal, axiom-print cell, grade AS ITS OWNER LEFT IT, status)
# ### ### **THE REFUSAL REASONS ARE THE DELIVERABLE, NOT AN APOLOGY FOR A MISSING ROW.**
ROWS = [
    ("THE FAMILY'S FIRST-LEVEL VALUE (b294): the barrier's zero is a property of the sub-family "
     "where at least one radius is at the diagonal's level or above -- NOT of the whole family. "
     "Zero DERIVED for `a >= 0`; zero COMPUTED for `a < 0, b >= 0` by a second, underived "
     "mechanism; and NONZERO on `Son(p,n; -1,-1)`: `-1` at (2,1)/(3,1)/(5,1), `-2/3` at (2,2), "
     "`-3/4` at (3,2). **The witness has mass ON the ball, which the object's own first condition "
     "forbids -- the member is a RELAXATION of the object's conditions and the nonzero lives in "
     "the part that is not the object.**",
     "**NO TERMINAL, AND WHY:** the per-member vanishing IS finite-decidable, and compiling it "
     "would certify the membership test and the pairing routine, not the barrier's reach -- which "
     "is a statement over all levels and places. **AND THE NONZERO VALUE MUST NOT BE COMPILED: a "
     "terminal reading `the first-level value is -1` would sit beside the barrier's terminals with "
     "no room to carry the sentence that the vector is not a `Son` vector.**",
     "n/a -- refusal. The controls ran instead: b271's banked not-dead witness `<A g_0, g_0> = "
     "4(N-q)` matched at all five cells BEFORE any zero was reported, and empty members reported "
     "CANNOT TEST rather than passing",
     "**THE BARRIER BELONGS TO A SUB-FAMILY** (b294's own verdict). **b280 and b281 are NOT "
     "re-verdicted, extended or weakened -- on the diagonal this act computes zero at every cell, "
     "as they say. No route is claimed; M-2 unchanged**",
     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    # ### IDEMPOTENCE GUARD -- b289's tool had none and duplicated nine rows on a re-run.
    if "THE FAMILY'S FIRST-LEVEL VALUE (b294)" in txt:
        print('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
        return 0
    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('=' * 100)
    print('b289 -- THE CORRESPONDENCE TABLE, BROUGHT CURRENT.')
    print('=' * 100)
    print('  last existing row : %d' % max(nums))
    print('  rows to append    : %d  (numbers %d..%d)' % (len(ROWS), start, start + len(ROWS) - 1))

    # ### NO BLANK CELLS -- CHECKED BEFORE ANYTHING IS WRITTEN.
    blank = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if not str(c).strip()]
    print('  blank cells       : %d  %s' % (len(blank), 'PASS' if not blank else '### FAIL ###'))
    if blank:
        return 1

    # ### EVERY REFUSAL MUST CARRY A REASON.
    refusals = [r for r in ROWS if 'NO TERMINAL' in r[1] or 'NO NEW TERMINAL' in r[1]]
    without = [r for r in refusals if 'AND WHY' not in r[1]]
    print('  refusal rows      : %d, of which without a stated reason: %d  %s'
          % (len(refusals), len(without), 'PASS' if not without else '### FAIL ###'))
    if without:
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
    ok = got[-len(ROWS):] == list(range(start, start + len(ROWS)))
    print('  READ BACK         : last %d row numbers are %s  %s'
          % (len(ROWS), got[-len(ROWS):], 'PASS' if ok else '### FAIL ###'))
    print('  table rows now    : %d' % len(got))
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
