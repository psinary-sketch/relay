# -*- coding: utf-8 -*-
"""b320_correspondence.py -- TWO ROWS: THE LAWFUL FUNCTION, AND THE CONTROL THAT FAILED FIRST.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.**

### ### **THE HAZARD OF THESE TWO ROWS:**
###   ### **ROW ONE SAYS A CLASS TEST PASSED AT EVERY CELL, AND THAT READS AS A DISCOVERY.** ### It
###     is a check that the corpus's seed, squared in the source's convention, lands in the source's
###     class -- which is what a square is FOR. ### The row carries the failing arm beside it.
###   ### **ROW TWO SAYS A CONTROL HOLDS, AND THAT READS AS A RESULT ABOUT THE OBJECT.** ### It is a
###     result about the INSTRUMENT. ### The source proved the theorem; this act checked that the
###     instrument does not contradict it where it speaks. ### **AND THE ROW MUST CARRY THAT THE
###     ### FIRST RUN SAID `FAILS`**, because a row reporting only the second run would be a true
###     sentence assembled to give a false impression.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402
import b303_correspondence as G   # noqa: E402

SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROWS = [
    ("THE SEED SQUARED IN THE SOURCE'S CONVENTION, AND THE CELLS THE SOURCE'S THEOREM COVERS (b320)",

     "THE SEED SQUARED IN THE SOURCE'S CONVENTION, AND THE CELLS THE SOURCE'S THEOREM COVERS "
     "(b320): b318 found NEITHER of its test functions positive definite, `0 of 13`, and read that "
     "as the corpus's window being a candidate `g` and not a candidate `f`. **THIS ACT SETTLES IT "
     "BY MEASUREMENT.** The adjoint is written once from the source's own involution of the "
     "convolution C*-algebra, `g#(rho) = conj(g(rho^-1))` against the MULTIPLICATIVE measure "
     "`d*mu`, which in `v = log rho` makes the product the autocorrelation with transform "
     "`\\|g-hat\\|^2`. Tested by the source's Definition 3.1 -- positive definite iff `f-hat >= 0` "
     "pointwise -- **`f = g conv g#` IS POSITIVE DEFINITE AT 13 OF 13 CELLS**, minima `-4.6e-17` "
     "to `+5.9e-18` against a sealed `-1e-09` floor. **AND THEOREM 1's COVERED CELLS ARE NAMED FROM "
     "THE CHECK AND NOT FROM THE WISH: 1.3, 1.35, 1.41.** The support condition is the only one "
     "that bites; the two vanishing conditions hold at EVERY cell to `1.4e-17`..`5.7e-16`.",

     "**NO TERMINAL. ### ONE STATEMENT HERE IS FINITE-DECIDABLE AND THE ROW SAYS WHICH**: whether "
     "a finite array of floats has a minimum above a fixed floor is decidable; **that this array is "
     "the transform of the source's product is not**, and rests on the derivation in (1a). **AND "
     "THE CLASS TEST CAN FAIL, WHICH IS THE ONLY REASON ITS PASSING IS WORTH PRINTING**: the same "
     "code path, on b318's wide-minus-narrow fixture -- a function known not to be a square by an "
     "argument about widths -- returns `min f-hat = -5.85e-01`. **A CLASS TEST EVERYTHING PASSES IS "
     "NOT ONE.**",

     "**NO PRINT FROM ANY OF THIS. NO NEW UNIT AND NO NEW SPACE**: b317's seed, b318's product and "
     "b319's stable subspace are imported and measured. **THE CLASS RESULT IS ABOUT THE SQUARE AND "
     "NOT ABOUT THE WINDOW**: the window itself passes Definition 3.1 at NO cell, its square at "
     "every one, and the row states both. The two vanishing conditions are quadratures and are "
     "tested at `1e-09` absolute rather than at strict equality, a bar sealed before any value.",

     "**A SQUARE LANDING IN THE CLASS OF SQUARES IS NOT A DISCOVERY.** **SCOPE: this fixes WHICH "
     "CELLS the source's theorem speaks at, and nothing else.** **NO WINDOW IS OPENED** -- the ten "
     "uncovered cells are computed and printed as data with no claim, and the inequality holding "
     "there is not evidence for anything, because outside the hypotheses there is no conclusion to "
     "be evidence for. **NO UNIT IS USED ANYWHERE IN THIS ACT.** `W-ORD-WINDOW-CLASS` and "
     "`W-ORD-ARCH-MEMBERSHIP` stay OPEN. NO ACT IS RE-VERDICTED AND NO GRADE MOVED. NO AGGREGATION "
     "IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. h2 stands exactly where the "
     "deposit left it. NOTHING DEPOSITS.",

     "current"),

    ("BOTH SIDES OF THE SOURCE'S INEQUALITY, AND A CONTROL THAT FAILED BEFORE IT HELD (b320)",

     "BOTH SIDES OF THE SOURCE'S INEQUALITY, AND A CONTROL THAT FAILED BEFORE IT HELD (b320): "
     "b317, b318 and b319 built, squared and chose a space; **NONE OF THEM COMPUTED THE FUNCTIONAL "
     "ON THE LEFT OF THE SOURCE'S INEQUALITY.** This act computes it from (53) and (38) directly, "
     "its principal-value constant MEASURED and not remembered -- `C_R = 2.415093331442` from two "
     "Gaussian widths agreeing to `4.7e-10`, landing on `gamma + log(2 pi) = 2.415092731311`, which "
     "this act did not put in. **AND THIS ACT'S FIRST REPORTED VERDICT WAS FAILS.** The "
     "registration's (B6) fixed a link order before any value existed -- normalizations, adjoint "
     "factor, transform convention, principal value, sign chain, rank -- so the failure named a "
     "constituent instead of licensing a hunt. Links (1)-(3) came back clean (the assembly "
     "reproduces the source's (39) to `4.7e-10` away from the singularity) and **LINK (4), THIS "
     "ACT'S OWN IMPLEMENTATION OF (38), WAS NAMED.** After the repair: **W_inf >= SQUARE at all "
     "three covered cells, margins `+0.2714`, `+0.2855`, `+0.3098`, and at 27 of 27 instrument "
     "frames.**",

     "**NO TERMINAL, AND NO THEOREM IS PROVED HERE.** The source proved Theorem 1. What is "
     "decidable is that two computed floats stand in an order at named frames; what is NOT is that "
     "either float is the quantity the theorem names. **THE DEFECT AND ITS FIXTURE ARE BOTH "
     "STATED**: (38) subtracts `phi(0)` on a neighbourhood of FIXED radius `R`, this act's code "
     "subtracted it only across the test function's support, and the dropped term is exactly "
     "`-2.9465` at `a = 1.3` against a measured discrepancy of `+2.9448`. The old fixture measured "
     "`C_R` at two widths that were BOTH wrong in the same way and agreed with each other; **AN "
     "AGREEMENT BETWEEN TWO INSTANCES OF THE SAME MISTAKE IS NOT A FIXTURE.** A second defect in "
     "the same function survived the first repair and printed `1.9e9`; two new fixtures now fail "
     "without each repair, and a SECOND AND INDEPENDENT ROUTE to the same quantity was built.",

     "**NO BAR WAS MOVED, NO CELL WAS DROPPED, NO TOLERANCE WAS LOOSENED, AND THE REGISTRATION WAS "
     "NOT RE-SEALED** -- its hash is the same `6f1c1e13...` it carried before the failing run and "
     "it verifies intact. The act's order forbade widening, tuning or re-barring to make the "
     "control pass; what made it pass was a defect fix in this act's own code. **THE REACH IS "
     "NON-EMPTY FOR THE FIRST TIME IN THIS ARC, 3 OF 3**, under the bar CORRECTED IN THIS ACT'S "
     "REGISTRATION BEFORE ANY VALUE, per b319's own proposal. **AND THE REGISTERED EXPECTATION IS "
     "HALF REFUTED**: the margin was expected to SHRINK toward the boundary cell and it GROWS.",

     "**A CONTROL THAT HOLDS CERTIFIES THE INSTRUMENT, NOT THE OBJECT.** **SCOPE: the sign of every "
     "margin is certified at every frame; the SIZE of every margin is certified at none.** The "
     "noise-floor gate REFUSES 3 of 6 values and all three are domain frames -- the domain axis "
     "still climbs at the largest frame computed, and climbs TOWARD the left-hand side; no "
     "extrapolation to a limit this act did not compute is offered. **NO WINDOW IS OPENED. NO UNIT "
     "IS USED.** The archimedean Weil distribution is keyed here for the first time. NO ACT IS "
     "RE-VERDICTED AND NO GRADE MOVED. NO AGGREGATION IS STATED. M-2 REMAINS "
     "(SPECIFIED-NOT-STATED). h2 stands exactly where the deposit left it. NOTHING DEPOSITS.",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b320 -- THE LAWFUL FUNCTION'S ROW, AND THE CONTROL'S.")
    print('=' * 100)
    print('  BLANK-CHECK FIXTURE (imported from b302): real blank=%s  quiet on full=%s  %s'
          % (pos, neg, 'PASS' if (pos and neg) else '### FAIL ###'))
    print('  SPLITTER FIXTURE (imported from b303): plain=%s escaped=%s content=%s raw=%s  %s'
          % (sa, sb, sc, sd, 'PASS' if (sa and sb and sc and sd) else '### FAIL ###'))
    if not (pos and neg and sa and sb and sc and sd):
        return 1
    print('  blank cells in the whole table (line-scoped) : %d' % C.blank_cells(txt))

    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if G.raw_pipes(str(c))]
    print('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d  %s'
          % (len(bad), 'PASS' if not bad else '### FAIL ### at %s' % bad))
    if bad:
        return 1

    slip = [m for m, s, _t, _p, _g, _st in ROWS if not s.startswith(m)]
    print('  marker is a literal prefix of its statement : %d/%d  %s'
          % (len(ROWS) - len(slip), len(ROWS), 'PASS' if not slip else '### FAIL ###'))
    if slip:
        return 1

    present = [m for m, _s, _t, _p, _g, _st in ROWS if m in txt]
    if present:
        print('  ### ROW(S) ALREADY PRESENT -- NOTHING WRITTEN: %s' % present)
        got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
        print('  table rows now : %d   blank cells : %d' % (len(got), C.blank_cells(txt)))
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

    r1, r2 = ROWS[0], ROWS[1]
    # ### **THE TWO GUARDS THAT MATTER FOR THESE TWO ROWS**, and they are guards against the two
    # ### readings the rows most invite: that a class test everything passes says something, and
    # ### that a control which HOLDS is a result about the object.
    g1 = ('A CLASS TEST EVERYTHING PASSES IS NOT ONE' in r1[2]
          and 'NO WINDOW IS OPENED' in r1[4]
          and 'NO UNIT' in r1[4])
    g2 = ('NO THEOREM IS PROVED HERE' in r2[2]
          and "THIS ACT'S FIRST REPORTED VERDICT WAS FAILS" in r2[1]
          and 'NO BAR WAS MOVED' in r2[3])
    print('  row 1 carries the failing arm and refuses the window : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 states the FIRST verdict and that no bar moved : %s  %s'
          % (g2, 'PASS' if g2 else '### FAIL ###'))
    if not (g1 and g2):
        return 1

    over = [i for i, r in enumerate(ROWS) if 'SCOPE' not in r[4] or 'M-2' not in r[4]]
    print('  rows carrying their own scope refusal and M-2\'s row : %d/%d  %s'
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
    tail = back.rstrip('\n').split('\n')[-len(ROWS):]
    cellcounts = [len(G.split_cells(ln)) for ln in tail]
    ok = (got[-len(ROWS):] == list(range(start, start + len(ROWS)))
          and all(m in back for m, _s, _t, _p, _g, _st in ROWS)
          and C.blank_cells(back) == 0
          and all(c == 6 for c in cellcounts)
          and all(all(x.strip() for x in G.split_cells(ln)) for ln in tail))
    print('  READ BACK         : last %d row number(s) are %s' % (len(ROWS), got[-len(ROWS):]))
    print('  cells on disk in the appended rows : %s  (6 required each, none blank)' % cellcounts)
    print('  blank cells after (line-scoped)   : %d' % C.blank_cells(back))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
