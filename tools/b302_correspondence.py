# -*- coding: utf-8 -*-
"""b302_correspondence.py -- THE ENCLOSURE TERMINAL'S ROW.

### **THIS ROW HAS A TERMINAL, WHICH THE LAST THREE DID NOT**, so the cells that mattered most in
### b299-b301 -- the ones saying NO TERMINAL and NO PRINT -- are replaced here by the profile
### itself, read from the build rather than described.

### ### **AND THE ROW'S OWN HAZARD IS THE OPPOSITE OF THOSE ACTS':** ### a compiled terminal in a
### table of compiled statements reads as certifying whatever the act was about. ### **IT
### CERTIFIES AN ENCLOSURE OF TWO EXPLICIT RATIONALS AND NOTHING ELSE, AND THE STATEMENT CELL SAYS
### SO BEFORE IT SAYS ANYTHING ABOUT WHY THE NUMBER MATTERS -- WHICH IT DOES NOT SAY AT ALL.**

### ### **IDEMPOTENT: THE MARKER IS A LITERAL PREFIX OF THE STATEMENT WRITTEN.**
### ### **THE BLANK-CELL CHECK IS LINE-SCOPED** (b297's fix).
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
    ("THE RATIONAL ENCLOSURE (b302)",

     "THE RATIONAL ENCLOSURE (b302): with denominator `10^20`, the numerators "
     "`70710678118654752440` and `70710678118654752441` satisfy the squaring criterion "
     "`2·lo² < den²` and `den² < 2·hi²`, and their complements are `29289321881345247559` and "
     "`29289321881345247560`. **THAT IS THE WHOLE CONTENT: A DECIDABLE COMPARISON OF NATURAL "
     "NUMBERS.** The module names the denominator and the criterion IN ITS TERMINAL STATEMENTS, "
     "and it mentions no norm, no unit vector, no Hilbert space and no act. **The elementary "
     "equivalence `a/b < 1/√2 ⟺ 2a² < b²` is about real numbers, is NOT proved in the file and is "
     "NOT claimed by it — the reader supplies it and the kernel certifies the integer side.**",

     "`Core/RationalEnclosureShadow.lean` — **11 TERMINALS, ALL ZERO-AXIOM ON THE FIRST COMPILE**: "
     "four polarity controls FIRST (the criterion refuses a too-large lower bound and a too-small "
     "upper bound, and accepts correct ones); **the UNAVAILABLE arm decided rather than described** "
     "(`at_denominator_one_the_enclosure_is_the_whole_unit_interval` — at denominator 1 no sharper "
     "control can exist, and all four facts saying so are decided); three not-dead witnesses; and "
     "the three enclosure terminals. **VANILLA: 0 imports, 0 `native_decide`, `decide` the only "
     "tactic, no division, no floating point.**",

     "**449 PRINTS, 449 ZERO-AXIOM, 0 OTHERWISE (was 438/438/0)**, regenerated from source into "
     "memory and written as bytes. **THE 438 PRE-EXISTING PRINTS SURVIVE AS A TRUE BYTE PREFIX "
     "AGAINST `git HEAD`** — a prefix check over BYTES, not a line comparison, which is the one "
     "check b298's BOM would not have survived. No byte-order mark on the written file; "
     "`git diff --numstat` agrees independently at `AXIOM_PRINTS.txt +11 / -0`. **The module is "
     "imported by `AllPrints.lean` in the same commit that creates it (b289's scar).**",

     "**THE TERMINALS ARE THE KERNEL'S OWN — DECIDED, NOT TRANSCRIBED.** **SCOPE: THIS ROW "
     "CERTIFIES AN ENCLOSURE OF TWO EXPLICIT RATIONALS AND NOTHING ELSE.** It is not evidence "
     "about a norm, a unit, a space or a construction; it does not bear on `W-ORD-ARCH-NORM-"
     "READING`, whose answer decides whether the enclosed number is ever the deviation term at "
     "all. **NOT A ROUTE. NO AGGREGATION IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED), UNCHANGED "
     "BY IT.**",

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
    print('b302 -- THE RATIONAL ENCLOSURE\'S ROW.')
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

    # ### THIS ROW HAS A TERMINAL, SO THE NO-TERMINAL GATE INVERTS: the terminal cell must NAME the
    # ### module and the profile cell must carry the BEFORE AND AFTER COUNTS.
    named = [r for r in ROWS if 'RationalEnclosureShadow.lean' not in r[2]
             or 'was 438/438/0' not in r[3]]
    print('  rows naming their module and their before/after counts : %d/%d  %s'
          % (len(ROWS) - len(named), len(ROWS), 'PASS' if not named else '### FAIL ###'))
    if named:
        return 1

    # ### THE NO-OVERSTATEMENT GATE, IN THIS ROW'S OWN TERMS. ### **A COMPILED TERMINAL IN THIS
    # ### TABLE READS AS CERTIFYING THE ACT; THE GRADE CELL MUST SAY WHAT IT DOES NOT CERTIFY.**
    over = [r for r in ROWS if 'AND NOTHING ELSE' not in r[4]
            or 'M-2 REMAINS (SPECIFIED-NOT-STATED)' not in r[4]]
    print('  rows carrying their own scope refusal : %d/%d  %s'
          % (len(ROWS) - len(over), len(ROWS), 'PASS' if not over else '### FAIL ###'))
    if over:
        return 1

    lines = []
    for k, (_mark, stmt, term, prof, grade, status) in enumerate(ROWS):
        lines.append('| %d | %s | %s | %s | %s | %s |'
                     % (start + k, stmt, term, prof, grade, status))
    new = txt.rstrip('\n') + '\n' + '\n'.join(lines) + '\n'
    open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
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
