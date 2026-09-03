# -*- coding: utf-8 -*-
"""b300_correspondence.py -- THE ARCHIMEDEAN LEG'S ROW.

### **A FILINGS TOOL. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED. ### NOTHING COMPILES.**

### ### **THIS ROW HAS NO TERMINAL, AND THE TABLE'S OWN HEADER ALLOWS IT** -- *"No blank cells;
### where a keystone statement has no terminal, the row says so."* ### **SO THE ROW SAYS SO, IN
### BOTH THE TERMINAL CELL AND THE AXIOM-PRINT CELL.** ### The act's subject is an
### infinite-dimensional subspace of `L^2(R)_ev` and an operator identity on it; ### **THERE IS NO
### FINITE OBJECT IN IT TO DECIDE, AND A FINITE STAND-IN WOULD CERTIFY THE STAND-IN.**

### ### **IDEMPOTENT: ### THE MARKER IS A LITERAL PREFIX OF THE STATEMENT WRITTEN** -- b298's own
### read-back caught a marker that was not, which left that row's guard leaning on the other's.
### ### **THE BLANK-CELL CHECK IS LINE-SCOPED** (b297's fix: in Python `\\s` matches a newline, and
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
    ("THE ARCHIMEDEAN LEG (b300)",

     "THE ARCHIMEDEAN LEG (b300): the object's archimedean local space is **constructed from the "
     "source's own Definition 4.4** as `S(1,1) subset L^2(R)_ev` -- two vanishing conditions at "
     "the cutoff `[-1,1]`, with the inner product and its normalization **read at content this "
     "act at CC 2006.13771 eq (16)** -- and the corpus's chosen archimedean unit `u_inf`, "
     "`phi_mu` at the first even negative eigenvalue normalized in `L^2`, **IS IN THAT SPACE**, "
     "derived against BOTH conditions. **The `+1` sector the corpus names is a PROPER subspace of "
     "the space, so the two are DIFFERENT objects.** **AND THE UNIT IS NOT THE INSTRUMENT VECTOR "
     "b291 and b292 placed OUTSIDE the space: two derivations show it is a different vector.**",

     "**NO TERMINAL. THIS ROW IS A DERIVATION OVER AN INFINITE-DIMENSIONAL SPACE, NOT A COMPILED "
     "STATEMENT, AND SAYS SO RATHER THAN LEAVING THE CELL TO BE READ.** The space is cut out by "
     "the vanishing of a function AND OF ITS FOURIER TRANSFORM on an interval; a finite model "
     "replaces that integral by a sum and **certifies the sum**. **THIS ROW ADDS NO TERMINAL AND "
     "CLAIMS NONE.**",

     "**NO PRINT -- THERE IS NOTHING HERE TO PRINT.** This act compiled nothing and moved no "
     "`.lean` file; `AXIOM_PRINTS.txt` stands exactly as b298 left it and is unchanged by this "
     "act. **AN ABSENT PRINT IS RECORDED AS ABSENT, NEVER AS A PASS** (the b280 convention).",

     "**DERIVES-on-IMPORTS, AND THE GRADE NAMES ITS INPUTS** -- CM Lemma 3.1 for condition one "
     "and the evenness; b211's (C3) chain on I8 + I6 + I10 for condition two's eigenrelation, at "
     "b211's own banked grade. **THE SIGN OF `c` IS NEVER USED, SO NO BENCH NUMBER IS "
     "LOAD-BEARING.** **SCOPE: the space is CONSTRUCTED CONDITIONALLY -- the real fiber's "
     "placement in the corpus's adelic object stays open -- and `phi_mu in L^2(R)` is stated by "
     "no owner (`W-ORD-PHI-MU-L2`). It is not a route, it unblocks nothing, and "
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
    print('b300 -- THE ARCHIMEDEAN LEG\'S ROW.')
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

    # ### THE NO-OVERSTATEMENT GATE, IN THIS ROW'S OWN TERMS: the grade cell must name its inputs,
    # ### must carry the construction's conditionality, and must carry M-2 unchanged.
    over = [r for r in ROWS if 'DERIVES-on-IMPORTS' not in r[4]
            or 'CONSTRUCTED CONDITIONALLY' not in r[4]
            or 'M-2 REMAINS (SPECIFIED-NOT-STATED)' not in r[4]]
    print('  rows carrying grade, conditionality and scope : %d/%d  %s'
          % (len(ROWS) - len(over), len(ROWS), 'PASS' if not over else '### FAIL ###'))
    if over:
        return 1

    lines = []
    for k, (_mark, stmt, term, prof, grade, status) in enumerate(ROWS):
        lines.append('| %d | %s | %s | %s | %s | %s |'
                     % (start + k, stmt, term, prof, grade, status))
    new = txt.rstrip('\n') + '\n' + '\n'.join(lines) + '\n'
    dbytes = new.encode('utf-8')
    # ### ENCODE FIRST, WRITE A TEMP, `os.replace` -- the b150 truncation pattern, standing.
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
