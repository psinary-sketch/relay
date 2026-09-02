# -*- coding: utf-8 -*-
"""b293_correspondence.py -- ONE ROW FOR b293.

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
    ("THE FINITE TWO-RADIUS FAMILY (b293): `Son(p,n; a,b)` defined in the corpus's own p-adic "
     "terms, with dimension `(p^n - p^a)(p^n - p^b)` derived; the corpus's existing space is the "
     "diagonal member `(0,0)`; dilation moves `(a,b) -> (a+1, b-1)` so the SUM is invariant; and "
     "`S` carries `(a,b)` to `(b,a)` by the corpus's own `S^2 = q^2 Pi`.",
     "**NO TERMINAL, AND WHY:** the diagonal identification and the radius arithmetic ARE "
     "finite-decidable -- and a terminal would certify the membership TEST and integer addition, "
     "not the family. **AND THE PART THAT WOULD MATTER -- the transform's behaviour -- IS THE "
     "PART THE TRUNCATION CORRUPTS**, so compiling it would certify the artifact. Refused on its "
     "own merits, not for want of decidability.",
     "n/a -- refusal. The E0 gate ran in exact rational arithmetic instead: 0 dimension "
     "mismatches at five cells, diagonal verified vector by vector in both directions with a "
     "negative control, and the collapsed condition compared to the actual transform both ways",
     "**CONSTRUCTED** (b293's own verdict). **NOTHING ABOUT THE BARRIER, THE COMPRESSION OR M-2 "
     "FOLLOWS -- a family existing is not a route existing**",
     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    # ### IDEMPOTENCE GUARD -- b289's tool had none and duplicated nine rows on a re-run.
    if 'THE FINITE TWO-RADIUS FAMILY (b293)' in txt:
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
