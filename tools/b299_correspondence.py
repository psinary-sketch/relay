# -*- coding: utf-8 -*-
"""b299_correspondence.py -- THE ARC KEYSTONE'S ROW.

### **A FILINGS TOOL. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED. ### NOTHING COMPILES.**

### ### **THE ROW THIS ACT WRITES HAS NO TERMINAL, AND THAT IS THE WHOLE DIFFICULTY.** ### The
### table's own header allows it -- ### *"No blank cells; where a keystone statement has no
### terminal, the row says so."* ### **SO THE ROW SAYS SO, IN BOTH THE TERMINAL CELL AND THE
### AXIOM-PRINT CELL, AND IT CITES ROWS 112-113 RATHER THAN RESTATING THEM.** ### A row for a
### document sitting in a table of compiled statements is the one row a reader could mistake for
### a terminal, and the cells are written against exactly that misreading.

### ### **THE BLANK-CELL CHECK IS LINE-SCOPED, CARRIED FROM b297 THROUGH b298, WITH ITS FIXTURE
### ### IN BOTH POLARITIES.** ### b297's first version used `\\|\\s*\\|` over the whole file; in
### Python `\\s` matches a newline, so it reported ### **111 BLANK CELLS IN A TABLE OF 111 ROWS.**

### ### **IDEMPOTENT: ### the marker is a literal PREFIX of the statement written** -- b298's own
### read-back caught a marker that was not, which left that row's guard leaning on the other's.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
DOCPATH = 'phase2/method/THE_TWO_RADIUS_FAMILY_AND_THE_ANNIHILATION_BOUNDARY.md'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROWS = [
    ("THE ARC KEYSTONE (b299)",

     "THE ARC KEYSTONE (b299): the arc `b283`-`b296` and the two filing acts after it are stated "
     "as one support-layer document, `PLACE-papers/" + DOCPATH + "` -- four object-groups, then "
     "what is machine-checked and what is not, then what none of it says. **Every sentence of "
     "substance in it is a quotation verified verbatim against the act that ORIGINATED it, by "
     "the runner that GENERATED it.** **IT STATES GRADES AND CONFERS NONE.**",

     "**NO TERMINAL. THIS ROW IS A DOCUMENT, NOT A COMPILED STATEMENT, AND SAYS SO RATHER THAN "
     "LEAVING THE CELL TO BE READ.** The arc's one machine-checked terminal is **row 113** "
     "(`B298.boundary_value_at_cell_2_2_on_member_radii_neg1_0`) with its function-side pair at "
     "**row 112** (`B270.absorb_2_2`). **THIS ROW ADDS NO TERMINAL AND CITES THOSE TWO RATHER "
     "THAN RESTATING THEM.**",

     "**NO PRINT -- THERE IS NOTHING HERE TO PRINT.** This act compiled nothing and imported "
     "nothing; `AXIOM_PRINTS.txt` stands at **438 prints, 438 zero-axiom, 0 otherwise**, exactly "
     "as b298 left it and unchanged by this act. **AN ABSENT PRINT IS RECORDED AS ABSENT, NEVER "
     "AS A PASS** (the b280 convention).",

     "**TRANSCRIBED, NOT CONFERRED** -- every grade in the document is its owning act's, quoted "
     "with that act's own scope beside it. **SCOPE: the document is SUPPORT-VOICE at working "
     "HEAD; it amends no deposited text, it is not a route, and it states no aggregation. "
     "M-2 REMAINS (SPECIFIED-NOT-STATED), UNCHANGED BY IT.**",

     "current"),
]


def blank_cells(text):
    """### **A WHOLE-TABLE BLANK-CELL AUDIT, LINE-SCOPED (b297's fix, carried through b298).**"""
    n = 0
    for line in text.splitlines():
        if line.startswith('|'):
            n += len(re.findall(r'\|[ \t]*\|', line))
    return n


def blank_check_fixture():
    """### **BOTH POLARITIES ON THE BLANK CHECK ITSELF.**

    ### **POSITIVE:** a table line with a genuine empty cell must be COUNTED.
    ### **NEGATIVE:** two full rows must count ZERO -- and in particular the newline between them
    ### must not be read as a blank cell, which is exactly what b297's first version did.
    """
    pos = blank_cells('| a | b |\n| c |  | d |\n') == 1
    neg = blank_cells('| a | b |\n| c | d |\n') == 0
    return pos, neg


def main():
    txt = io.open(TABLE, encoding='utf-8').read()

    pos, neg = blank_check_fixture()
    print('=' * 100)
    print('b299 -- THE ARC KEYSTONE ROW.')
    print('=' * 100)
    print('  BLANK-CHECK FIXTURE : counts a real blank cell: %-5s   stays quiet on full rows: %-5s'
          '  %s' % (pos, neg, 'PASS' if (pos and neg) else '### FAIL ###'))
    if not (pos and neg):
        return 1
    print('  blank cells in the whole table (line-scoped) : %d' % blank_cells(txt))

    # ### THE MARKER MUST BE A LITERAL PREFIX OF WHAT IS WRITTEN, OR THE GUARD GUARDS NOTHING.
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

    # ### THE NO-TERMINAL GATE. ### **A ROW WITH NO TERMINAL MUST SAY SO IN THE TERMINAL CELL AND
    # ### IN THE AXIOM-PRINT CELL**, per the table's own header. ### A silent cell here is the one
    # ### a reader would fill in for themselves, and they would fill it in wrong.
    quiet = [r for r in ROWS if 'NO TERMINAL' not in r[2] or 'NO PRINT' not in r[3]]
    print('  rows with no terminal SAY SO in both cells : %d/%d  %s'
          % (len(ROWS) - len(quiet), len(ROWS), 'PASS' if not quiet else '### FAIL ###'))
    if quiet:
        return 1

    # ### AND THE NO-OVERSTATEMENT GATE, IN THIS ROW'S OWN TERMS: it must carry M-2 unchanged and
    # ### must not read as conferring a grade.
    over = [r for r in ROWS if 'TRANSCRIBED, NOT CONFERRED' not in r[4]
            or 'M-2 REMAINS (SPECIFIED-NOT-STATED)' not in r[4]]
    print('  rows carrying their own scope sentence     : %d/%d  %s'
          % (len(ROWS) - len(over), len(ROWS), 'PASS' if not over else '### FAIL ###'))
    if over:
        return 1

    lines = []
    for k, (_mark, stmt, term, prof, grade, status) in enumerate(ROWS):
        lines.append('| %d | %s | %s | %s | %s | %s |'
                     % (start + k, stmt, term, prof, grade, status))
    new = txt.rstrip('\n') + '\n' + '\n'.join(lines) + '\n'
    d = new.encode('utf-8')
    # ### ENCODE FIRST, WRITE A TEMP, `os.replace` -- the b150 truncation pattern, standing.
    open(TABLE + '.tmp', 'wb').write(d)
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
