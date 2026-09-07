# -*- coding: utf-8 -*-
"""b351_correspondence.py -- ONE ROW: THE PARTITION QUESTION.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every number is read from the
### act's own record, never typed. ### **THE HAZARD:** a row that reads as if a bounded coordinate were a safe
### margin, as if two closed coordinates were half a classification, as if a price in boxes were a route, or as if
### UNDECIDED were a finding about the object rather than about the record.
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

SCOPE_TAIL = ("**SCOPE: THIS IS A READ, AND A READING IS NOT A RESULT ABOUT THE OBJECT.** No partition was constructed, no class proved silent, no instrument written and "
              "nothing computed beyond one labelled division of two banked counts. A COORDINATE BEING BOUNDED IS NOT THE MARGIN BEING SAFE THERE, and no margin was measured "
              "at any aim. Two closed coordinates are not half a classification, because a classification of a product is not two classifications of two factors. The phase's "
              "finite cut is stated for an EVEN seed, the condition b328 states it under. A price is not a prediction and pricing is not measuring. Nothing about the "
              "quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED and THE CLAUSE HAS NOT MOVED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under "
              "b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands "
              "exactly where the deposit left it. The wave PARKED by the author's ruling. NOTHING DEPOSITS.")


def rows():
    P = json.load(io.open(os.path.join(D, 'b351_read.json'), encoding='utf-8'))
    m = ("THE AIM PLANE'S COORDINATES READ FOR WHETHER THE RECORD CAN BOUND THEM: THE ABSCISSA AND THE SEED'S PHASE ARE BOUNDED BY AN ARGUMENT, THE HEIGHT ONLY BY A "
         "MEASUREMENT AND THE SEED'S WIDTH NOT AT ALL -- SO THE RECORD HOLDS NO FINITE CLASSIFICATION OF THE WAYS THE MARGIN COULD FAIL AND NO PROOF THAT THERE IS NONE, AND "
         "THE VERDICT IS UNDECIDED (b351, leg 3 of the sortie b349-b351)")
    stmt = (m + ": **A BOUND ON THE INSTRUMENT IS NOT A BOUND ON THE COORDINATE**, and the registration fixed those words before one coordinate was read. **THE ABSCISSA IS "
            "CLOSED BY AN ARGUMENT ALREADY IN THE RECORD AND NEVER CITED FOR THIS PURPOSE:** b326's summed bound SUM_{k>=2} r_Q(k) k^(-3/2) = 1.38 < 2 gives \\|Z_Q(s) - 2\\| < 2, "
            "so Z_Q cannot vanish at Re s >= 1.5 nor, by the functional equation, at Re s <= -0.5 -- a statement about ALL zeros and not about the found ones. **THE PHASE IS "
            "CLOSED ALGEBRAICALLY:** for an even seed the quadruple's term is 4 \\|G\\|^2 cos(2 phi), the coordinate lives on a circle, and the sign cuts it at exactly \\|phi\\| = 45 "
            "and 135 -- **the one place in the plane where the order's question has a clean affirmative answer** -- except for the single class \\|G\\| = 0, which the sign "
            "condition cannot see and which b349's own words say three lawful seeds do not close. **THE HEIGHT IS BOUNDED ONLY WHERE THE CENSUS STOPPED:** sixty boxes of "
            "height 2.5 over t in [0.5, 150], the count closing at 180 zeros against a main term of 178.6; above it the record's own phrase is that nobody looked. **AND THE "
            "REASON IS SHARPER THAN REACH: THE ONLY METHOD THERE PRODUCES INSTANCES, AND THE RIEMANN-VON MANGOLDT MAIN TERM SAYS THE INSTANCES NEVER RUN OUT** -- so the price, "
            "%.5f boxes per unit of height and %d further boxes to T = 300, **BUYS INSTANCES WHILE THE MISSING STATEMENT NEEDS A CLASS**, and it is given in boxes because b326 "
            "printed no wall for the census and no wall time was borrowed from other work. **THE WIDTH IS WORSE OFF THAN THE HEIGHT, AND THE REGISTERED EXPECTATION NAMED THE "
            "HEIGHT:** at a = 40 and 81 the square and remainder are NOT REACHED by measurement, the remainder evaluator changes sign and grows by four orders past rho = 100, "
            "and for Z_Q the record's own words are NOT AN INSTRUMENT THE RECORD HAS -- **so the height has a method not yet run higher and the width has NO METHOD AT ALL**, "
            "and the width's missing statement is UNPRICEABLE from banked figures, its pricing unpriceable too. Both other branches are shown unreachable rather than left "
            "unclaimed: (A SHAPE EXISTS) fails its own condition on two coordinates, and (NO FINITE PARTITION) demands an obstruction quoted at an emitting line, which the "
            "record does not hold -- **and section (D) fixed in advance that an absence of a bound is not an obstruction.**"
            % (P['boxes_per_unit'], P['boxes_to_T300']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: UNDECIDED IS A STATEMENT ABOUT THE RECORD AND NOT ABOUT THE OBJECT** -- the aim plane may well admit a finite classification; this act "
         "says only that the record contains neither one nor a proof that there is none.",
         "**NO PRINT.** Relay tools only. No PLACE-papers file moves and nothing is filed, so the hook and the mirror are NOT OWED and the suite checks that state rather than "
         "assuming it; nothing in TECHNE-Core; no owner instrument edited and no banked figure recomputed.",
         "**NO GRADE MOVED; NO BAR MOVED.** b326, b328, b334 and b349 stand exactly as banked, and nothing here confers anything about any coordinate.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b351 -- THE PARTITION QUESTION. ### THE ROW.')
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
          and 'A BOUND ON THE INSTRUMENT IS NOT A BOUND ON THE COORDINATE' in ROWS[0][1]
          and 'UNDECIDED' in ROWS[0][0]
          and 'NO METHOD AT ALL' in ROWS[0][1]
          and 'NO GRADE MOVED' in ROWS[0][4]
          and 'THE CLAUSE HAS NOT MOVED' in ROWS[0][5]
          and 'NOTHING DEPOSITS' in ROWS[0][5])
    print('  the row says NO TERMINAL with the reason, instrument-not-coordinate, UNDECIDED, the width has no method, no grade moved : %s' % g1)
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
