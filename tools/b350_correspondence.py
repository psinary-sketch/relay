# -*- coding: utf-8 -*-
"""b350_correspondence.py -- ONE ROW: THE FLOOR'S TWO HELD AXES, PRICED.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every number is read from the
### act's own records, never typed. ### **THE HAZARD:** a row that reads as if a priced axis were a moved axis, as if
### a rank-preserving band said the residual was unchanged inside it, as if a cheap ladder made either move free, or
### as if paying a trail's cheaper half discharged it.
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

SCOPE_TAIL = ("**SCOPE: PRICING IS NOT MEASURING, AND A PRICE IS A STATEMENT ABOUT WHAT AN ACT WOULD COST MADE BY AN ACT THAT DOES NOT PERFORM IT.** No frame was built, no "
              "ladder run, no cell evaluated and no axis moved. A RANK-PRESERVING BAND IS A FACT ABOUT THE CUT AND NOT ABOUT THE RESIDUAL: the same subspace kept does not "
              "mean the same residual. Nothing here says what either held axis does to the residual, and the floor is UNEXPLAINED. The trail is RESTATED, NOT DISCHARGED. "
              "Nothing about the quantifier, h2, totality or the roster. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item "
              "1 restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where the deposit left it. "
              "The wave PARKED by the author's ruling. NOTHING DEPOSITS.")


def rows():
    P = json.load(io.open(os.path.join(D, 'b350_price.json'), encoding='utf-8'))
    m = ("THE FLOOR'S TWO HELD AXES PRICED FROM b344'S PRINTED FIGURES WITH NO FRAME BUILT AND NOTHING RE-RUN: THE COST IS THE SAME FOR BOTH AT %s SECONDS OF WALL PER VALUE, "
         "THE THRESHOLD'S RANK-PRESERVING BAND IS FREE AND ABOUT ONE DECADE WIDE, THE TAPER'S ROOM IS NOT PRICEABLE FROM THEM AT ALL -- AND THE FLOOR IS UNEXPLAINED, THE "
         "TRAIL RESTATED AND NOT DISCHARGED (b350)" % ('%.2f' % P['wall_total']))
    stmt = (m + ": **A PRICE SAYS WHAT A MOVE WOULD COST AND WHAT IT WOULD CONFOUND; IT DOES NOT SAY WHAT THE MOVE WOULD SHOW.** **THE COST**, summed from the walls b344 "
            "printed over its sealed ladder %s: %s seconds per value tried, **THE SAME FOR EITHER AXIS**, because a move is a ladder either way -- and what it buys is ONE "
            "value, not a response across an axis. **THE ROOM, WHERE THE PRINTED FIGURES GIVE ONE:** at every rung b344 printed the largest eigenvalue dropped and the "
            "smallest kept, and the intersection across the rungs is **(%s, %s), a factor of %.2f wide**, with the corpus's own tau = %s sitting inside it, free to fall by "
            "%.2f or rise by %.2f with the same eigenvalues kept at every rung and therefore the same rank. **AND THAT IS A FACT ABOUT THE CUT AND NOT ABOUT THE RESIDUAL**, "
            "which the registration fixed before the arithmetic: the same subspace kept does not mean the same residual, b344 printed no residual at a second threshold, and "
            "so the residual's response to the threshold is NOT priced by these figures. **THE TAPER GETS NO ROOM AT ALL:** ALPHA and BETA are printed as constants at every "
            "rung with nothing beside them, no second value, no neighbourhood, no interval, no derivative -- **SO THE ACT SAYS SO RATHER THAN INVENTING ONE, AND PRICES THE "
            "PRICING INSTEAD**: two ladders, %s seconds, **AND EVEN THAT WOULD GIVE A DIFFERENCE AND NOT A ROOM**, because the taper has no analogue of the eigenvalue "
            "interval that gives the threshold one. **WHAT EACH MOVE WOULD CONFOUND, in the sealed words of the act that declined it, located at its registration's lines %s "
            "and %s through the sortie's shared normaliser:** the threshold would confound the RANK with the FLOOR, since moving it moves the stable cut and b343 showed the "
            "rank constant, and b319 records the corpus's threshold sitting 57 times inside that separation; the taper would confound the INSTRUMENT with the OBJECT, since "
            "ALPHA and BETA are the source's own constants and a taper moved is no longer the source's object. **SO THE TWO AXES ARE NOT SYMMETRIC AND THE ASYMMETRY IS NOT "
            "IN THE COST.** **THE VERDICT, BY THE SEALED RULE: THE FLOOR IS UNEXPLAINED** -- the one axis moved does not account for it, and for the two held axes the record "
            "contains NO measurement of the residual at all; the unexplained part is named as the residual's response to the threshold anywhere in its band and to the taper "
            "at any value. **AND THE TRAIL IS RESTATED, NOT DISCHARGED**, by one appended block on OPEN_TRAILS.md: its price half is paid and its measurement half is neither "
            "paid nor attempted, because **A TRAIL IS NOT DISCHARGED BY PAYING THE CHEAPER HALF OF IT.**"
            % (P['ladder'], ('%.2f' % P['wall_total']), ('%.6e' % P['band_lo']), ('%.6e' % P['band_hi']),
               P['band_factor'], ('%.1e' % P['tau']), P['fall_factor'], P['rise_factor'],
               ('%.2f' % P['taper_pricing_cost']), P['reasons'][0]['line'], P['reasons'][1]['line']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: A PRICE IS NOT A MEASUREMENT** -- this act moved nothing, measured nothing, and its whole content is what two moves would cost and "
         "what each would spoil.",
         "**NO PRINT.** Relay tools, plus one append-only block on OPEN_TRAILS.md restating a trail; the papers repo moves, so the hook and the mirror ARE OWED and both are "
         "recorded; nothing in TECHNE-Core; no owner instrument edited and no banked figure recomputed.",
         "**NO GRADE MOVED; NO BAR MOVED.** b344 and b339 stand exactly as banked, and nothing here confers anything about either held axis.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b350 -- THE FLOOR'S TWO HELD AXES, PRICED. ### THE ROW.")
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
          and 'A FACT ABOUT THE CUT AND NOT ABOUT THE RESIDUAL' in ROWS[0][1]
          and 'THE FLOOR IS UNEXPLAINED' in ROWS[0][1]
          and 'RESTATED, NOT DISCHARGED' in ROWS[0][1]
          and 'NO GRADE MOVED' in ROWS[0][4]
          and 'PRICING IS NOT MEASURING' in ROWS[0][5]
          and 'NOTHING DEPOSITS' in ROWS[0][5])
    print('  the row says NO TERMINAL with the reason, a band is about the cut, the floor unexplained, the trail restated, no grade moved : %s' % g1)
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
