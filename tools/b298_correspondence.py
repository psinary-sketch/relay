# -*- coding: utf-8 -*-
"""b298_correspondence.py -- THE TWO SIDES OF ONE BOUNDARY, AT ONE CELL.

### **A FILINGS TOOL. ### NO GRADE MOVES. ### NO ACT IS RE-VERDICTED.** ### Every grade below is
### TRANSCRIBED from its owning act's own bank, never decided here.

### ### **THE TWO ROWS ARE WRITTEN SO THE PAIR READS AS A PAIR** ### -- identically zero on the
### member satisfying the object's first condition, nonzero on the relaxed member, ### SAME CELL.
### ### **AND NEITHER ROW OVERSTATES: ### THE PAIR CERTIFIES SHARPNESS AT THAT CELL, NOT THE
### ### EQUIVALENCE IN GENERAL, AND EACH ROW SAYS SO IN ITS OWN TEXT** ### -- because a reader
### meeting one row alone must not be able to read the pair as more than it is.

### ### **THE FUNCTION-SIDE ROW DOES NOT SUPERSEDE ROW 95 (b270's).** ### It restates that
### terminal IN ITS PAIR ROLE and names the row it comes from.

### ### **THE LINE-SCOPED BLANK CHECK IS CARRIED FROM b297, WITH ITS FIXTURE.** ### b297's first
### version used `\\|\\s*\\|` over the whole file; in Python `\\s` matches a newline, so every
### row's closing bar and the next row's opening bar counted as a blank cell and it reported
### ### **111 BLANK CELLS IN A TABLE OF 111 ROWS.** ### The fix is line scoping, and the fixture
### below exercises BOTH polarities so the check is never again trusted on its word.
"""
import io
import os
import re
import sys

SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

ROWS = [
    # ### **MARKER DEFECT, CAUGHT BY THIS TOOL'S OWN READ-BACK ON ITS FIRST RUN:** ### the marker
    # ### read "... in its pair role" while the statement written says "... restated here in its
    # ### PAIR ROLE". ### **A MARKER THAT IS NOT A SUBSTRING OF WHAT IS WRITTEN LEAVES ITS ROW'S
    # ### IDEMPOTENCE GUARD LEANING ON THE OTHER ROW'S.** ### The read-back reported FAIL and the
    # ### marker is now a literal prefix of the statement.
    ("THE BOUNDARY, FUNCTION SIDE (b270/b280",
     "THE BOUNDARY, FUNCTION SIDE (b270/b280, restated here in its PAIR ROLE; **row 95 stands and "
     "is not superseded**): at the cell `(p,n) = (2,2)` every index lands in the ball under the "
     "operator at `k = n`, so **a vector vanishing on the ball kills the pairing** -- the member "
     "satisfying the object's own first condition pairs to **identically zero**.",

     "**TERMINAL, ALREADY PRINTING: `B270.absorb_2_2`** in `Core/BallAbsorptionShadow.lean`, "
     "imported by `AllPrints.lean` and printing since b289. **CITED HERE, NOT REBUILT** -- b289's "
     "own finding was that rebuilding what already exists is the error.",

     "`'B270.absorb_2_2' does not depend on any axioms`, read from `AXIOM_PRINTS.txt` at 438 "
     "prints. **And `B298.ball_agrees_with_b270_2_2` decides that b298's integer-radius ball "
     "EQUALS b270's `m % p^n == 0`, so the two sides of this pair are statements about ONE ball "
     "and not two.**",

     "**DERIVES** (b280), as its owning act left it. **THIS ROW ADDS NO GRADE AND MOVES NONE.** "
     "**SCOPE: the pair certifies SHARPNESS AT THIS CELL, not the equivalence in general** -- "
     "b295's criterion and b296's equivalence quantify over all levels and all places, are NOT "
     "finite, and **nothing in the kernel certifies them**",
     "current"),

    ("THE BOUNDARY, RELAXED SIDE (b298)",
     "THE BOUNDARY, RELAXED SIDE (b298): at the **same cell** `(2,2)`, relax the function-side "
     "radius by one step -- the member `Son(2,2; -1, 0)` instead of `Son(2,2)` -- and the pairing "
     "is **NOT zero**: the witness `w = e_2 - e_6 + e_4 - e_12` has value **4/3**. "
     "**AND THE OBJECT'S OWN SPACE REJECTS THAT WITNESS**, which the terminal decides in its own "
     "statement rather than in a comment.",

     "**TERMINAL, BUILT THIS ACT: "
     "`B298.boundary_value_at_cell_2_2_on_member_radii_neg1_0`** in "
     "`Core/BoundaryValueShadow.lean`, imported by `AllPrints.lean` **in the same commit that "
     "creates it** (b289's scar). Its statement carries the cell `2 2` and the radii `(-1) 0`, and "
     "its second conjunct is `inMember 2 2 0 0 w = false`. **The value is carried without "
     "division: `classSize 2 2 = 3` and `pairTimesClass 2 2 w = 4` are two decided integers.**",

     "`'B298.boundary_value_at_cell_2_2_on_member_radii_neg1_0' does not depend on any axioms`, "
     "with 11 further `B298.*` rows -- six polarity controls, two not-dead witnesses matching "
     "b271's banked `4(N-q)`, a uniformity control, the b270 ball agreement, and **the UNAVAILABLE "
     "arm `ctor_degenerate_2_1`**, which decides that b296's general construction COLLIDES at "
     "`(2,1)` so no analogous terminal is offered there. **426 -> 438 prints, all zero-axiom, the "
     "426 pre-existing byte-identical against `git HEAD`.**",

     "**DERIVED** (b295, b296), as those acts left it; **re-decided here, not discovered here**. "
     "**NOT A ROUTE**: the member weakens the object's FIRST condition and the witness has mass ON "
     "the ball, which that condition forbids outright. **SCOPE: sharpness at this cell only -- "
     "the equivalence in general is NOT certified and this row does not claim it.** M-2 unchanged",
     "current"),
]


def blank_cells(text):
    """### **A WHOLE-TABLE BLANK-CELL AUDIT, LINE-SCOPED (b297's fix, carried).**"""
    n = 0
    for line in text.splitlines():
        if line.startswith('|'):
            n += len(re.findall(r'\|[ \t]*\|', line))
    return n


def blank_check_fixture():
    """### **BOTH POLARITIES ON THE BLANK CHECK ITSELF.**

    ### **POSITIVE:** a table line with a genuine empty cell must be COUNTED.
    ### **NEGATIVE:** two full rows must count ZERO -- and in particular the newline between
    ### them must not be read as a blank cell, which is exactly what b297's first version did.
    """
    pos = blank_cells('| a | b |\n| c |  | d |\n') == 1
    neg = blank_cells('| a | b |\n| c | d |\n') == 0
    return pos, neg


def main():
    txt = io.open(TABLE, encoding='utf-8').read()

    pos, neg = blank_check_fixture()
    print('  BLANK-CHECK FIXTURE : counts a real blank cell: %-5s   stays quiet on full rows: %-5s'
          '  %s' % (pos, neg, 'PASS' if (pos and neg) else '### FAIL ###'))
    if not (pos and neg):
        return 1
    print('  blank cells in the whole table (line-scoped) : %d' % blank_cells(txt))

    present = [m for m, _s, _t, _p, _g, _st in ROWS if m in txt]
    if present:
        print('  ### ROW(S) ALREADY PRESENT -- NOTHING WRITTEN: %s' % present)
        return 0

    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('=' * 100)
    print('b298 -- THE TWO SIDES OF ONE BOUNDARY, AT ONE CELL.')
    print('=' * 100)
    print('  last existing row : %d' % max(nums))
    print('  rows to append    : %d  (numbers %d..%d)' % (len(ROWS), start, start + len(ROWS) - 1))

    blank = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if not str(c).strip()]
    print('  blank cells in the new rows : %d  %s'
          % (len(blank), 'PASS' if not blank else '### FAIL ###'))
    if blank:
        return 1

    # ### THE NO-OVERSTATEMENT GATE: each row must carry its own scope sentence.
    over = [r for r in ROWS if 'not the equivalence in general' not in r[4]
            and 'the equivalence in general is NOT certified' not in r[4]]
    print('  rows carrying their own scope sentence : %d/%d  %s'
          % (len(ROWS) - len(over), len(ROWS), 'PASS' if not over else '### FAIL ###'))
    if over:
        return 1

    # ### AND THE PAIR MUST NAME BOTH TERMINALS, OR IT IS NOT A PAIR.
    joined = ' '.join(r[2] for r in ROWS)
    paired = ('B270.absorb_2_2' in joined
              and 'B298.boundary_value_at_cell_2_2_on_member_radii_neg1_0' in joined)
    print('  both terminals named across the pair   : %s  %s'
          % (paired, 'PASS' if paired else '### FAIL ###'))
    if not paired:
        return 1

    lines = []
    for k, (_mark, stmt, term, prof, grade, status) in enumerate(ROWS):
        lines.append('| %d | %s | %s | %s | %s | %s |'
                     % (start + k, stmt, term, prof, grade, status))
    new = txt.rstrip('\n') + '\n' + '\n'.join(lines) + '\n'
    io.open(TABLE, 'w', encoding='utf-8').write(new)

    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    ok = (got[-len(ROWS):] == list(range(start, start + len(ROWS)))
          and all(m in back for m, _s, _t, _p, _g, _st in ROWS)
          and blank_cells(back) == 0)
    print('  READ BACK         : last %d row numbers are %s' % (len(ROWS), got[-len(ROWS):]))
    print('  blank cells after (line-scoped) : %d' % blank_cells(back))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
