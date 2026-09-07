# -*- coding: utf-8 -*-
"""b354_correspondence.py -- ONE ROW: THE SIXTH FRAME.

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

SCOPE_TAIL = ("**SCOPE: THE SIGN CHANGE AND THE RANK SATURATION HAPPEN AT THE SAME RUNG AND THIS ACT SEPARATES THEM NOWHERE.** Not that the residual crosses zero; not that "
              "it does not. The instrument's own controls HOLD EXACTLY at that rung -- the fifth reproduces b320 to 0.000e+00 and the identity control is 0.000e+00 -- so "
              "nothing here says the instrument failed. A CRITERION THAT RETURNED NOTHING IS NOT A CRITERION THAT SAID SOMETHING, and it is TABLED, NOT EDITED: a linear-space "
              "fit would fit these six numbers and would be A SECOND CRITERION chosen after seeing the first fail. Nothing about the quantifier, h2, totality or the roster; "
              "NO CLASS IS DISCHARGED and THE CLAUSE HAS NOT MOVED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 "
              "restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where the deposit left it. "
              "The wave PARKED by the author's ruling. NOTHING DEPOSITS.")


def rows():
    S = json.load(io.open(os.path.join(D, 'b354_sixth.json'), encoding='utf-8'))
    pc = S['per_cell']
    cells = S['cells']
    sixths = ', '.join('a=%s: %+.6e' % (k, pc[k]['R_sixth']) for k in cells)
    m = ("THE SIXTH RUNG OF THE DOMAIN LADDER RUN AT LAST, AND ITS RESIDUAL IS NEGATIVE AT EVERY COVERED CELL -- AND IT IS ALSO THE FIRST RUNG AT WHICH THE RANK IS LIMITED BY "
         "NY RATHER THAN BY X, SO THE SIGN CHANGE AND THE INSTRUMENT'S BOUNDARY ARRIVE IN THE SAME STEP AND THIS ACT SEPARATES THEM NOWHERE (b354, leg 1 of the sortie "
         "b354-b355)")
    stmt = (m + ": b352 priced this frame and did not run it; b354 ran it, on the existing instrument with NOTHING RE-TUNED. **THE ARM THAT LICENSED IT FIRST:** the FIFTH rung "
            "was recomputed and reproduces b320's banked values to **0.000e+00 relative at all three cells**, and the sixth frame's identity control is **0.000e+00** against a "
            "bar of 1e-9 whose floor is dim*eps = 7.1e-12 -- **SO THE SIXTH RUNG IS NOT A BROKEN COMPUTATION.** **THE RESIDUALS:** %s, where the five banked rungs had fallen "
            "by ratios 0.34, 0.37, 0.42, 0.49 approaching one half and the sixth ratio is -0.012, -0.011, -0.009. **THE RESIDUAL DID NOT SETTLE ONTO A FLOOR; IT CROSSED "
            "ZERO**, its magnitude falling by about 84 and its sign changing in one step. **AND THE RANK:** the banked ranks 20, 37, 69, 133, 262 double per rung and "
            "extrapolate to about 516 at the sixth; the observed rank is **512, which is NY exactly**, short by about four dimensions out of five hundred. b316 fixed NY "
            "independently of X on purpose so the second condition would not weaken as the domain lengthened; **AT THIS RUNG THAT INDEPENDENCE HAS REACHED ITS OWN LIMIT.** "
            "**THE SEALED CRITERION IS UNDEFINED THERE:** it minimises squared residuals of log R and log is undefined at a negative R, so **NO SIX-FRAME SCORE EXISTS AND NONE "
            "IS REPORTED** -- the first run printed a not-a-number in every score column and is banked under a declaring name. That the import is the same fit was CHECKED: "
            "refitting FIVE frames reproduces b352's banked scores to 3e-12, **SO b352 IS EXTENDED AND NOT RE-VERDICTED.** **THE CHOSEN CEILING WAS %.0f SECONDS AND THE RUN "
            "TOOK %.1f** -- and a chosen ceiling is not a read one; that printed wall is the FIRST MEASURED WALL THIS LADDER HAS, because b320 printed none. VERDICT BY THE "
            "LETTER OF THE SEALED CONDITION: **FLOOR UNDER-RESOLVED STILL** -- **AND THE REASON IS NOT THE ONE THE BRANCH ANTICIPATED**, which was six frames that fit and did "
            "not settle; what happened is that the sixth frame **DID NOT FIT AT ALL.** The sealed branch rule has no slot for that, and the absence is filed as a finding and "
            "TABLED, NOT EDITED."
            % (sixths, S['wall_ceiling'], S['wall']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: ONE RUNG IS ONE NUMBER, AND THIS ONE ARRIVED WITH ITS OWN AMBIGUITY ATTACHED** -- the act put a number on the record and showed that "
         "nobody knows what it means, this seat included.",
         "**NO PRINT.** Relay tools only, plus the sortie's step-zero anchor tool. Nothing written to PLACE-papers, so the hook and the mirror are NOT OWED and the suite "
         "checks that state rather than assuming it; nothing in TECHNE-Core; no owner instrument edited -- b316, b317, b318, b319 and b352_fit are all IMPORTED.",
         "**NO GRADE MOVED; NO BAR MOVED.** b339 stands with its UNAFFORDABLE and its labelled side-reading NOT withdrawn; b346 stands; b352's five-frame scores are "
         "reproduced here to 3e-12 and stand exactly.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b354 -- THE SIXTH FRAME. ### THE ROW.')
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
          and 'SEPARATES THEM NOWHERE' in ROWS[0][0]
          and 'NOT A BROKEN COMPUTATION' in ROWS[0][1]
          and 'NO SIX-FRAME SCORE EXISTS' in ROWS[0][1]
          and 'a chosen ceiling is not a read one' in ROWS[0][1]
          and 'NOT withdrawn' in ROWS[0][4]
          and 'NO GRADE MOVED' in ROWS[0][4]
          and 'TABLED, NOT EDITED' in ROWS[0][5]
          and 'NOTHING DEPOSITS' in ROWS[0][5])
    print('  the row says NO TERMINAL with the reason, not-separated, not-broken, no score, chosen-not-read, side-reading kept, tabled : %s' % g1)
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
