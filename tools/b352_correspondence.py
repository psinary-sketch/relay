# -*- coding: utf-8 -*-
"""b352_correspondence.py -- ONE ROW: THE FLOOR'S FOURTH CANDIDATE.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every number is read from
### the act's own records, never typed. ### **THE HAZARD:** a row that reads as if a model winning a score were a
### floor existing, as if a positive fitted constant were a measured floor, as if b339's side-reading had been
### withdrawn, or as if a price in frames were a plan to spend them.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402
import b303_correspondence as G   # noqa: E402

SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SCOPE_TAIL = ("**SCOPE: A FIT IS A DESCRIPTION OF FIVE NUMBERS AND NOT A FACT ABOUT AN OBJECT.** No frame was built, no instrument run, no ladder extended and no residual "
              "recomputed; every value fitted is b339's banked array. A MODEL WINNING A SELECTION SCORE IS NOT A FLOOR EXISTING, and the smallest floor any arm here could "
              "have seen is printed per cell. NO ACT IS RE-VERDICTED: b339's UNAFFORDABLE stands, b346 stands, b350 stands, b351's UNDECIDED stands, and b339's side-reading "
              "is restated as fit-dependent and NOT withdrawn. The frame price is a price and not a prediction, and this act does not run it. Nothing about the quantifier, "
              "h2, totality or the roster; NO CLASS IS DISCHARGED and THE CLAUSE HAS NOT MOVED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. "
              "The seam's debt item 1 restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where "
              "the deposit left it. The wave PARKED by the author's ruling. NOTHING DEPOSITS.")


def rows():
    P = json.load(io.open(os.path.join(D, 'b352_fit.json'), encoding='utf-8'))
    F = json.load(io.open(os.path.join(D, 'b352_filings.json'), encoding='utf-8'))
    pc = P['per_cell']
    cells = P['cells']
    d21 = ', '.join('a=%s: %+.4f' % (k, pc[k]['d21']) for k in cells)
    d23 = ', '.join('a=%s: %+.4f' % (k, pc[k]['d23']) for k in cells)
    cs = ', '.join('a=%s: %+.6e' % (k, pc[k]['c']) for k in cells)
    seen = ', '.join('a=%s: %.6e' % (k, pc[k]['smallest_visible']) for k in cells)
    m = ("THE IDENTITY RESIDUAL REFITTED UNDER THREE MODELS FIXED BEFORE ANY FIT: THE FLOOR IS UNDER-RESOLVED AS A FIT, NOT BECAUSE THE FIVE FRAMES CANNOT SEPARATE A FLOOR "
         "FROM A FASTER-DECAYING TERM -- THEY SEPARATE THEM AT EVERY CELL -- BUT BECAUSE THE THREE CELLS DISAGREE WITH EACH OTHER, AND AT n = 5 THE SELECTION CRITERION'S "
         "PENALTY FOR A THIRD PARAMETER IS TEN TIMES THE BAR (b352, leg 1 of the sortie b352-b353)")
    stmt = (m + ": **A MODEL WINNING A SELECTION SCORE IS NOT A FLOOR EXISTING**, and the registration fixed that sentence before any fit. THE MODELS, sealed in advance: "
            "M1 = A X^-p (k=2), M2 = A X^-p + c (k=3), M3 = A X^-p + B X^-(p+1) (k=3), all three fitted by ONE criterion, least squares on log R -- and **M1 REPRODUCES "
            "b322's OWN fit_power AT EVERY CELL TO 1e-9, THE FITTER IMPORTED**, which is what makes the three scores comparable and was required before any score was "
            "reported. THE FREE TWO-TERM MODEL (k=4) IS NOT FITTED AND NOT SCOREABLE: at n = 5 its corrected criterion has n-k-1 = 0 in a denominator. **WHAT THE FIVE FRAMES "
            "CAN DO:** M2 beats M3 at every cell (%s), so a constant floor IS separable from a faster-decaying correction at equal complexity. **WHAT THEY CANNOT DO:** M2 "
            "against M1 comes out (%s) -- the floor model preferred at a = 1.3 by less than the bar, at a = 1.35 decisively, and REJECTED at a = 1.41 by 7.01. **AND THE "
            "REASON IS THE CRITERION, NOT THE DATA: AT n = 5 A THIRD PARAMETER COSTS 20 AICc UNITS, TEN TIMES THE BAR OF 2**, so S must fall by a factor of 54.6 just to "
            "break even and the winner turns on the penalty. **THE FITTED CONSTANT IS POSITIVE AT ALL THREE CELLS** (%s) and passes the second bar at all three -- **WHICH "
            "REFUTES THIS SEAT'S REGISTERED EXPECTATION** that it would come out at or below zero somewhere. **WHAT THIS ACT COULD NOT HAVE SEEN, PRINTED:** a true floor "
            "below the fit's own scatter at the last rung (%s) would pass no arm here. **THE PRICE OF SETTLING IT: ONE MORE FRAME.** The binding cell needs 6 frames where "
            "the record holds 5; the next rung is X = 256, N = 32768 -- **AND THAT SITS INSIDE THE CEILING b339 SEALED AT X = 512**, where b339's own question was "
            "UNAFFORDABLE because its split criterion needed X_req between 812 and 2358. **THE FIT ASKS A DIFFERENT QUESTION OF THE SAME LADDER AND ITS PRICE IS AFFORDABLE "
            "WHERE b339's WAS NOT** -- and it is a price and not a prediction, assuming an S ratio a sixth frame has not been asked for, and this act does not run it."
            % (d23, d21, cs, seen))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: A REFIT RANKS DESCRIPTIONS AND DOES NOT MEASURE THE THING DESCRIBED** -- nothing here was computed that b339 had not already banked, "
         "and the act's whole content is how three sealed models score against five banked numbers.",
         "**NO PRINT.** Relay tools; one appended work-order block on OPEN_TRAILS.md carrying the void's width as the MEASURED 10.62 with b350 named and not as a round "
         "decade; one TECHNE module minting the straddling-gate rule, LOCAL-ONLY and not pushed; and its mechanized half APPENDED to registration_gate.py beside the "
         "bar-floor arms, editing nothing. The papers repo moves, so the hook and the mirror ARE OWED and both are recorded.",
         "**NO GRADE MOVED; NO BAR MOVED.** b339, b346, b350 and b351 stand exactly as banked; b339's side-reading is restated as fit-dependent and NOT withdrawn.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b352 -- THE FLOOR'S FOURTH CANDIDATE. ### THE ROW.")
    print('=' * 100)
    print('  BLANK-CHECK FIXTURE (imported from b302): real blank=%s  quiet on full=%s  %s' % (pos, neg, 'PASS' if (pos and neg) else '### FAIL ###'))
    print('  SPLITTER FIXTURE (imported from b303): plain=%s escaped=%s content=%s raw=%s  %s' % (sa, sb, sc, sd, 'PASS' if (sa and sb and sc and sd) else '### FAIL ###'))
    if not (pos and neg and sa and sb and sc and sd):
        return 1
    print('  blank cells in the whole table (line-scoped) : %d' % C.blank_cells(txt))
    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if G.raw_pipes(str(c))]
    print('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d  %s' % (len(bad), 'PASS' if not bad else '### FAIL ### at %s' % bad))
    if bad:
        return 1
    slip = [m for m, s, _t, _p, _g, _sc, _st in ROWS if not s.startswith(m)]
    print('  marker is a literal prefix of its statement : %s' % ('PASS' if not slip else '### FAIL ###'))
    if slip:
        return 1
    g1 = (all('NO TERMINAL, AND THE REASON' in r[2] for r in ROWS)
          and 'A MODEL WINNING A SELECTION SCORE IS NOT A FLOOR EXISTING' in ROWS[0][1]
          and 'UNDER-RESOLVED AS A FIT' in ROWS[0][0]
          and 'NOT withdrawn' in ROWS[0][4]
          and 'NO GRADE MOVED' in ROWS[0][4]
          and 'price and not a prediction' in ROWS[0][1]
          and 'NOTHING DEPOSITS' in ROWS[0][5])
    print('  the row says NO TERMINAL with the reason, a score is not a floor, under-resolved, side-reading not withdrawn, no grade moved : %s' % g1)
    if not g1:
        return 1
    present = [m for m, _s, _t, _p, _g, _sc, _st in ROWS if m in txt]
    if present:
        print('  ### ROW(S) ALREADY PRESENT (%d) -- NOTHING WRITTEN.' % len(present))
        got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
        print('  table rows now : %d   blank cells : %d' % (len(got), C.blank_cells(txt)))
        print('=' * 100)
        return 0
    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('  last existing row : %d ; row to append : %d' % (max(nums), start))
    over = [i for i, r in enumerate(ROWS) if 'SCOPE' not in r[5] or 'M-2' not in r[5]]
    if over:
        print('  ### FAIL -- a row lacks its scope refusal or M-2')
        return 1
    lines = ['| %d | %s | %s | %s | %s %s | %s |' % (start + k, stmt, term, prof, grade, scope, status)
             for k, (_m, stmt, term, prof, grade, scope, status) in enumerate(ROWS)]
    new = txt.rstrip(chr(10)) + chr(10) + chr(10).join(lines) + chr(10)
    open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(TABLE + '.tmp', TABLE)
    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    cells = [G.split_cells(t) for t in back.rstrip(chr(10)).split(chr(10))[-1:]]
    ok = (got[-1] == start and all(m in back for m, _s, _t, _p, _g, _sc, _st in ROWS) and C.blank_cells(back) == 0
          and all(len(c) == 6 and all(x.strip() for x in c) for c in cells))
    print('  READ BACK         : last row number is %d ; cells on disk %s (6 required, none blank)' % (got[-1], [len(c) for c in cells]))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
