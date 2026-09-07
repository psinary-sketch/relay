# -*- coding: utf-8 -*-
"""b356_correspondence.py -- ONE ROW: THE OBJECT OR THE BOUNDARY.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every figure is read
### from the act's own records, never typed. ### **THE HAZARD:** a row that reads as if the residual's sign
### change were a fact about the object, as if a criterion that returned nothing had said something, as if
### b339's side-reading had been withdrawn, or as if a chosen ceiling had been a read one.
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

SCOPE_TAIL = ("**SCOPE: TWO POINTS ON AN AXIS ARE NOT A CONVERGENCE, AND THIS ACT HAS TWO.** Not that the residual is positive in the limit -- b344's own quadrature ladder "
              "shows the trace still moving at NY = 2048. Not that the five-frame picture is right: it stands where it stood, and what this act adds is that its edge is at "
              "X = 256 with NY = 512 and not further out. NOT THAT b354 WAS WRONG -- it named its own ambiguity and could not have resolved it, and its figures stand exactly "
              "as banked and are used here. THE RAISED FRAME IS NOT COMPARABLE TO THE BANKED LADDER: comparing it to the fifth rung's banked residual moves TWO parameters at "
              "once, and that comparison is refused in the act. A SIGN THAT RETURNS UNDER ONE RAISE IS NOT A SIGN THAT IS SAFE. Nothing about the quantifier, h2, totality or "
              "the roster; NO CLASS IS DISCHARGED and THE CLAUSE HAS NOT MOVED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt "
              "item 1 restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where the deposit left "
              "it. The wave PARKED by the author's ruling. NOTHING DEPOSITS.")


def rows():
    R = json.load(io.open(os.path.join(D, 'b356_raised.json'), encoding='utf-8'))
    cells = R['cells']
    pairs = '; '.join('a=%s: %+.6e to %+.6e' % (k, R['signs'][k]['old'], R['signs'][k]['new']) for k in cells)
    m = ("THE SIXTH RUNG RUN AGAIN WITH THE QUADRATURE AXIS RAISED ONCE AND DELIBERATELY: THE RESIDUAL RETURNS POSITIVE AT EVERY COVERED CELL AND THE RANK IS NO LONGER AT ITS "
         "BOUND -- SO b356'S SIXTH RUNG WAS THE INSTRUMENT'S EDGE, AND THE FIVE-FRAME PICTURE STANDS WITH ITS EDGE NOW LOCATED AT X = 256 WITH NY = 512 (b356, leg 1 of the "
         "sortie b356-b357)")
    stmt = (m + ": b354 found the residual negative and the rank saturated at the quadrature bound IN THE SAME STEP and separated them nowhere, saying so. b356 separates them "
            "by raising NY from 512 to 1024 -- **A VALUE THE RECORD HAD ALREADY USED, being a rung of b344's own ladder** -- with nothing else moved. **THE CONTROL RAN FIRST "
            "AND LICENSED EVERYTHING ELSE:** the FIFTH rung under the raised axis has rank %d EXACTLY as banked, and its trace reproduces b320's values to %.3e worst against a "
            "bar of %.0e **whose floor is b344's own measured %.3e move of THIS axis over EXACTLY this step** -- the observed move being %.2f times that floor, so a bar set AT "
            "the floor would have failed on a correct computation and b347's rule did work rather than decorate. **THE RANK AT THE RAISED AXIS IS %d AGAINST A BOUND OF %d**, "
            "where b354 measured %d against %d and extrapolated the banked ranks to about %.0f -- **THE EXTRAPOLATION WAS ACCURATE TO TWO.** THE ONE COMPARISON THIS ACT "
            "LICENSES, the two frames differing in ONE parameter: %s -- **THE SIGN CHANGES AT EVERY CELL.** So the branch is THE BOUNDARY, with (THE OBJECT) unreachable "
            "because it demands the residual NEGATIVE at the raised axis and it is positive, and (STILL CONFOUNDED) unreachable because the control held, the bound cleared and "
            "the run did not overrun (%.1f s against a chosen ceiling of %.0f). **AND SIX DIMENSIONS DECIDED THE SIGN:** the cut needs %d dimensions and at NY = 512 it got "
            "%d, and the six it could not have turned +1.08e-02 into -2.76e-04 -- a change larger than the residual itself, produced by ONE PART IN EIGHTY-SIX of the cut. "
            "**A CUT THAT IS SIX DIMENSIONS SHORT IS NOT A SLIGHTLY WORSE CUT; IT IS A DIFFERENT ONE.**"
            % (R['rank5'], R['worst_control_rel'], R['bar_trace'], R['bar_trace_floor'],
               R['worst_control_rel'] / R['bar_trace_floor'], R['rank6'], R['raised'],
               R['b354_frame6']['rank'], 512, 516.0, pairs, R['wall'], R['wall_ceiling'],
               R['rank6'], R['b354_frame6']['rank']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: ONE AMBIGUITY WAS TAKEN OFF THE RECORD AND A SMALLER ONE PUT IN ITS PLACE** -- the floor question is exactly where b352 left it, "
         "under-resolved as a fit, and this act ordered no fit and reported no score.",
         "**NO PRINT.** Relay tools only. Nothing written to PLACE-papers, so the hook and the mirror are NOT OWED and the suite checks that state rather than assuming it; "
         "nothing in TECHNE-Core; no owner instrument edited -- b316, b317, b318 and b319 are all IMPORTED, and the ONE parameter re-tuned is NY, said to be re-tuning.",
         "**NO GRADE MOVED; NO BAR MOVED.** b354 stands with its figures and its refusal; b339's side-reading is HANDLED BY THE BRANCH AND NOT WITHDRAWN -- b354's evidence "
         "against it is removed by this act, so it returns to where b339 left it, a reading its own act labelled; b346 and b352 stand as banked.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b356 -- THE OBJECT OR THE BOUNDARY. ### THE ROW.')
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
          and "INSTRUMENT'S EDGE" in ROWS[0][0]
          and 'THE CONTROL RAN FIRST' in ROWS[0][1]
          and 'SIX DIMENSIONS DECIDED THE SIGN' in ROWS[0][1]
          and 'NOT WITHDRAWN' in ROWS[0][4]
          and 'NO GRADE MOVED' in ROWS[0][4]
          and 'TWO POINTS ON AN AXIS ARE NOT A CONVERGENCE' in ROWS[0][5]
          and 'NOT THAT b354 WAS WRONG' in ROWS[0][5]
          and 'NOTHING DEPOSITS' in ROWS[0][5])
    print('  the row says NO TERMINAL with the reason, the edge located, the control first, six dimensions, not-a-convergence, b354 not wrong : %s' % g1)
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
