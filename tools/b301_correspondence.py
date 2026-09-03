# -*- coding: utf-8 -*-
"""b301_correspondence.py -- THE OBJECT COMPLETED'S ROW.

### **A FILINGS TOOL. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED. ### NOTHING COMPILES.**

### ### **THIS ROW HAS NO TERMINAL, AND THE TABLE'S OWN HEADER ALLOWS IT** -- *"No blank cells;
### where a keystone statement has no terminal, the row says so."*
### ### **AND THIS ROW IS THE ONE A READER IS MOST LIKELY TO MISREAD, SO ITS CELLS ARE WRITTEN
### ### AGAINST THAT MISREADING:** ### a row saying an OBJECT IS CONSTRUCTED, in a table of
### compiled statements, beside a term-3 row that says DECLARED, NOT CONSTRUCTED. ### **THE GRADE
### CELL CARRIES THE CONDITIONALITY, THE OPEN REQUIREMENTS AND THE FACT THAT THE OTHER ROW DOES
### NOT MOVE.**

### ### **IDEMPOTENT: THE MARKER IS A LITERAL PREFIX OF THE STATEMENT WRITTEN.**
### ### **THE BLANK-CELL CHECK IS LINE-SCOPED** (b297's fix: `\\s` matches a newline in Python, and
### the whole-file form reported 111 blank cells in a table of 111 rows).
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROWS = [
    ("THE OBJECT COMPLETED (b301)",

     "THE OBJECT COMPLETED (b301): the construction restated with every constituent in one table. "
     "**FINITE p:** `S-bar_p` the `L^2(Q_p)`-closure of the `Son` tower (b279, CONSTRUCTED), unit "
     "`u_p = 4q P_1 f_(1,1)` at level `ell(p) = 2 if p = 2 else 1` — **the exceptional place is "
     "the law's own zero, `d_1(2,1) = 0`**. **AT INFINITY:** `S(1,1)` from CC Definition 4.4 with "
     "its inner product read at content at eq (16), and `u_inf = phi_mu` at the first even "
     "negative eigenvalue, **IN that space** (b300). **Four of the product's eight requirements "
     "MET, three OPEN with what is missing named, one not asked of this product at all.** "
     "**The convergence condition was RE-CHECKED in exact rationals, not cited.**",

     "**NO TERMINAL. THIS ROW IS A CONSTRUCTION RESTATEMENT OVER INFINITE-DIMENSIONAL SPACES, NOT "
     "A COMPILED STATEMENT, AND SAYS SO RATHER THAN LEAVING THE CELL TO BE READ.** The shadow "
     "check did find one finite-decidable candidate — the rational enclosure of `1 - 1/sqrt(2)` — "
     "and **THIS ACT'S OWN SEALED REGISTRATION CAPPED `.lean` FILES MOVED AT ZERO, SO IT IS FILED "
     "(`W-ORD-ENCLOSURE-TERMINAL`) AND NOT BUILT.**",

     "**NO PRINT -- THERE IS NOTHING HERE TO PRINT.** This act compiled nothing and moved no "
     "`.lean` file; `AXIOM_PRINTS.txt` stands exactly as b298 left it. **AND ONE THING IS SAID "
     "BECAUSE THE RE-CHECK COULD BE MISREAD: b226's terminal `c0_deviation_is_zero` IS A "
     "CONDITIONAL AND REMAINS TRUE — what one reading of the archimedean normalization would move "
     "is whether its HYPOTHESIS holds, not the theorem. NO COMPILED TERMINAL IS DISTURBED.**",

     "**TRANSCRIBED, NOT CONFERRED** — every grade in the table is its owning act's, pulled from "
     "that act's file. **SCOPE: THE OBJECT IS CONSTRUCTED CONDITIONALLY — on the level-limit "
     "premise, on b226's OWED generic odd place, on a ruling as to which inner product the "
     "archimedean normalization is, and on the real fiber's placement (N-OPEN-B). IT IS NOT A "
     "ROUTE, NO AGGREGATION IS STATED, AND THE IDENTITY CHAIN'S TERM-3 ROW DOES NOT MOVE BY THIS "
     "ACT — it names the restricted tensor product, and the re-scope is a ruling, not a row edit. "
     "M-2 REMAINS (SPECIFIED-NOT-STATED), UNCHANGED BY IT.**",

     "current"),
]


def blank_cells(text):
    """### **A WHOLE-TABLE BLANK-CELL AUDIT, LINE-SCOPED (b297's fix, carried since).**"""
    n = 0
    for line in text.splitlines():
        if line.startswith('|'):
            n += len(re.findall(r'\|[ \t]*\|', line))
    return n


def blank_check_fixture():
    """### **BOTH POLARITIES ON THE BLANK CHECK ITSELF.**"""
    pos = blank_cells('| a | b |\n| c |  | d |\n') == 1
    neg = blank_cells('| a | b |\n| c | d |\n') == 0
    return pos, neg


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = blank_check_fixture()
    print('=' * 100)
    print('b301 -- THE OBJECT COMPLETED\'S ROW.')
    print('=' * 100)
    print('  BLANK-CHECK FIXTURE : counts a real blank cell: %-5s   stays quiet on full rows: %-5s'
          '  %s' % (pos, neg, 'PASS' if (pos and neg) else '### FAIL ###'))
    if not (pos and neg):
        return 1
    print('  blank cells in the whole table (line-scoped) : %d' % blank_cells(txt))

    slip = [m for m, s, _t, _p, _g, _st in ROWS if not s.startswith(m)]
    print('  marker is a literal prefix of its statement : %d/%d  %s'
          % (len(ROWS) - len(slip), len(ROWS), 'PASS' if not slip else '### FAIL ###'))
    if slip:
        return 1

    present = [m for m, _s, _t, _p, _g, _st in ROWS if m in txt]
    if present:
        print('  ### ROW(S) ALREADY PRESENT -- NOTHING WRITTEN: %s' % present)
        print('=' * 100)
        return 0

    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('  last existing row : %d' % max(nums))
    print('  rows to append    : %d  (numbers %d..%d)' % (len(ROWS), start, start + len(ROWS) - 1))

    blank = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if not str(c).strip()]
    print('  blank cells in the new rows : %d  %s'
          % (len(blank), 'PASS' if not blank else '### FAIL ###'))
    if blank:
        return 1

    quiet = [r for r in ROWS if 'NO TERMINAL' not in r[2] or 'NO PRINT' not in r[3]]
    print('  rows with no terminal SAY SO in both cells : %d/%d  %s'
          % (len(ROWS) - len(quiet), len(ROWS), 'PASS' if not quiet else '### FAIL ###'))
    if quiet:
        return 1

    # ### THE NO-OVERSTATEMENT GATE, IN THIS ROW'S OWN TERMS. ### **A ROW SAYING AN OBJECT IS
    # ### CONSTRUCTED MUST CARRY THE CONDITIONALITY AND MUST SAY THE OTHER ROW DOES NOT MOVE.**
    over = [r for r in ROWS if 'CONSTRUCTED CONDITIONALLY' not in r[4]
            or 'TERM-3 ROW DOES NOT MOVE' not in r[4]
            or 'M-2 REMAINS (SPECIFIED-NOT-STATED)' not in r[4]]
    print('  rows carrying conditionality, the row-question and scope : %d/%d  %s'
          % (len(ROWS) - len(over), len(ROWS), 'PASS' if not over else '### FAIL ###'))
    if over:
        return 1

    lines = []
    for k, (_mark, stmt, term, prof, grade, status) in enumerate(ROWS):
        lines.append('| %d | %s | %s | %s | %s | %s |'
                     % (start + k, stmt, term, prof, grade, status))
    new = txt.rstrip('\n') + '\n' + '\n'.join(lines) + '\n'
    dbytes = new.encode('utf-8')
    open(TABLE + '.tmp', 'wb').write(dbytes)
    os.replace(TABLE + '.tmp', TABLE)

    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    cells = back.rstrip('\n').split('\n')[-1].strip().strip('|').split('|')
    ok = (got[-len(ROWS):] == list(range(start, start + len(ROWS)))
          and all(m in back for m, _s, _t, _p, _g, _st in ROWS)
          and blank_cells(back) == 0
          and len(cells) == 6 and all(c.strip() for c in cells))
    print('  READ BACK         : last %d row number(s) are %s' % (len(ROWS), got[-len(ROWS):]))
    print('  cells on disk in the appended row : %d  (6 required, none blank)' % len(cells))
    print('  blank cells after (line-scoped)   : %d' % blank_cells(back))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
