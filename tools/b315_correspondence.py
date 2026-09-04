# -*- coding: utf-8 -*-
"""b315_correspondence.py -- TWO ROWS: THE CALIBRATION READ, AND THE RATE UNDER THE FLIP.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.**

### ### **THE HAZARD OF THESE TWO ROWS:**
###   ### **ROW ONE CORRECTS A CAUTION TWO ACTS CARRIED, AND A ROW LIKE THAT READS AS A
###     ### RE-VERDICT.** ### It is not one: their numbers stand, and what falls is a stated REASON,
###     replaced by a stronger one. ### **A CORRECTION THAT REMOVES A CAUTION MUST NOT READ AS A
###     ### LICENCE**, and the grade cell says so before it says anything else.
###   ### **ROW TWO REPORTS A RATE THAT SURVIVES, AND A SURVIVING RATE READS AS REASSURANCE.** ###
###     What it actually reports is a LOSS: the envelope that carried the tail is gone.
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
    ("THE CALIBRATION FIXES A SIGN, AND THE E2 IN IT IS NOT THE REMAINDER (b315)",

     "THE CALIBRATION FIXES A SIGN, AND THE E2 IN IT IS NOT THE REMAINDER (b315): the atlas's "
     "calibration was read AT THE OPERATION, not at the comment. **`A` IS COMPUTED AT "
     "`carto_atlas.py:66` AS AN EXPLICIT INTEGRAL OF THE DIGAMMA KERNEL AGAINST THE TEST FUNCTION, "
     "DIVIDED BY `2\u03c0` \u2014 no free constant, no fitted factor, and nothing from any "
     "remainder in it**; what the calibration settles is the ORIENTATION with which that term "
     "enters the explicit formula, tested at line 117 by `abs(residual) <= TOL` on "
     "`Z \u2212 (P \u2212 PR + A)`. **AND THAT RESIDUAL CONTAINS NO REMAINDER AT ALL**: the `E2` in "
     "the bracket is the name of a REGISTERED CLAIM (`E1`\u2013`E4`, per the file's own first "
     "line), not the archimedean remainder `E2` of b38's identity. **SO THE NEAR-CANCELLATION "
     "`A + E2 \u2248 0` UNDER THE SOURCE'S CONVENTION IS NOT PRODUCED BY THE CALIBRATION: IT "
     "SURVIVES**, worst modulus of `A + E2` equal to `0.022509`, which is 1.13% of the largest modulus of `A` in the table.",

     "**NO TERMINAL, AND THE SHADOW WAS EXPECTED TO BE NOTHING AND IS NOTHING** \u2014 a quotation "
     "is not decidable and a quadrature is not finite-decidable. **THE INDEPENDENCE CHECK RUNS OVER "
     "THE ENCLOSING FUNCTION AND NOT THE ASSIGNMENT LINE**, so a dependence introduced two lines "
     "above would be caught; and **IT IS SHOWN ABLE TO FIND ONE** \u2014 a fixture feeds it a "
     "function whose `A` is built from a variable named `E2` and it reports the dependence. "
     "**WITHOUT THAT ARM, \u201cNO DEPENDENCE FOUND\u201d WOULD BE A SENTENCE ABOUT THE SEARCH.** "
     "Both sites come back clean: `carto_atlas.py:66` in `channels`, `b38_act10.py:47` in "
     "`left_side`.",

     "**NO PRINT. NO INSTRUMENT EDITED** \u2014 the source's convention runs only in b313's copies, "
     "which this act reads and never writes, and no owner's `main()` is called. **AND THE CORPUS'S "
     "OWN EARLIER READS AGREE, WHICH IS WORTH SAYING BECAUSE THIS ACT DID NOT FIND IT FIRST**: b233 "
     "wrote that *the file was committed before any answer; the sign inside it is annotated as "
     "fixed by a calibration \u2014 those are different claims*, and b235 took the restriction *a "
     "sign warranted by a calibration is an instrument fact, not a text.* **THE STEP-ZERO GATE THE "
     "ORDER ASKED FOR WAS ALSO WRITTEN AND RUN, AND IT FAILS**: 24 Core modules carry a print "
     "target the certification file never imports, 91 targets uncertified. Nothing repaired.",

     "**A READ, AND A CORRECTION TO A REASON.** **SCOPE, AND IT IS THE WHOLE OF THE ROW'S HONESTY: "
     "b312's SENTENCE AND b313's CAUTION RESTED ON ONE NAME FOR TWO OBJECTS \u2014 the "
     "double-name species b200 named and b219 realised \u2014 AND NEITHER ACT IS RE-VERDICTED.** "
     "Their numbers stand exactly as banked; **b313's REFUSAL TO INTERPRET THE COLUMN ALSO STANDS, "
     "ON A DIFFERENT AND STRONGER GROUND**: not *it might be the calibration*, but ***no definition "
     "has been stated that would make it mean anything***. **A CORRECTION THAT REMOVES A CAUTION IS "
     "NOT A LICENCE TO INTERPRET**, and `A + E2` is promoted to nothing here as it was there. "
     "`W-ORD-A-PLUS-E2` stands open, unchanged in status and changed in its reason. NO GRADE MOVED. "
     "NO AGGREGATION IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. h2 stands "
     "exactly where the deposit left it.",

     "current"),

    ("THE RATE UNDER THE SOURCE'S EXPONENT: THE ENVELOPE IS LOST, THE CUTOFF ORDER IS NOT (b315)",

     "THE RATE UNDER THE SOURCE'S EXPONENT: THE ENVELOPE IS LOST, THE CUTOFF ORDER IS NOT (b315): "
     "b264's Cauchy\u2013Schwarz-and-Plancherel route was re-run with the corrected exponent. "
     "**EVERY STEP SURVIVES BUT THE PREFACTOR, AND THE PREFACTOR IS THE WHOLE DIFFERENCE**: "
     "Cauchy\u2013Schwarz bounds the INTEGRAL and the exponent multiplies it. **SO "
     "THE MODULUS OF `eps_even^src(ρ)` IS AT MOST `C_even = 132.781908429` — THE SAME "
     "CONSTANT, WITH NO POWER OF `ρ` AT ALL.** The sharp rate keeps its constant and loses "
     "one power: "
     "\u03c1^(\u22121/2)`. And along the CUTOFF, by b264's own dilation route \u2014 cited, not "
     "re-claimed \u2014 **`E2even(a)\u00b7log a \u2192 p(0)\u00b7M_even` HOLDS UNDER BOTH: THE "
     "EVEN SECTOR STILL VANISHES ALONG THE CUTOFF AT THE SAME LEADING ORDER `1/log a`, AND ONLY "
     "THE CONSTANT CHANGES**, because the measure `d\u03c1/\u03c1` absorbs exactly the one power "
     "the flip introduces.",

     "**NO TERMINAL.** The derivation is the bank's and is UNCOMPILED. **CONVERGENCE IS DECIDED BY "
     "b264's OWN TWO-AXIS TEST \u2014 `NG` vs `2NG` AND `EPS_NQ` vs `2 EPS_NQ` at `1e-8` \u2014 NOT "
     "BY A CEILING NUMBER**, because b264's own `(D2)` records that the single axis marked five "
     "cells converged at `~1e-12` **on values wrong by four orders of magnitude**. On the cells "
     "that pass it: **0 violations of the new constant envelope**, and the rate column converges on "
     "`K_even` from below, reaching `1.55948` at `\u03c1 = 100`. The noise-floor gate is in the "
     "path and what it removes is PRINTED, at `1e-11` to `1e-15`.",

     "**NO PRINT.** The measured constants, over the range where the two-axis test passes "
     "(`[1, 157.34]`, 74 points): `M_even = 0.823669` against b264's banked `0.812581`, and "
     "`M_even^src = 2.442961`. **AND A DEFECT OF THIS ACT'S OWN, DECLARED: THE FIRST DRAFT "
     "INTEGRATED TO b264's CEILING NUMBER AND RETURNED `\u22122.89` \u2014 A NEGATIVE VALUE FOR AN "
     "INTEGRAL OF A CURVE POSITIVE EVERYWHERE IT IS TRUSTED**, because three grid points sat "
     "between the last sound cell and the ceiling carrying values near `\u2212100`. **THE CEILING "
     "IS WHERE THE EVALUATOR FAILS, NOT THE LAST PLACE IT WORKS**, and the repair is b264's own "
     "discipline rather than a new one. The bench along the cutoff falls monotonically in both "
     "columns while `L\u00b7E2even` is still RISING, so **it checks the direction and not the "
     "constant**, and a constant read off six pre-asymptotic cells is capped at zero.",

     "**A DERIVATION, AND WHAT IT REPORTS IS A LOSS.** **SCOPE, AND IT IS THE WHOLE OF THE ROW'S "
     "HONESTY: THE NEW ENVELOPE IS NOT MERELY LOOSE, IT IS VACUOUS IN THE LIMIT** \u2014 at its "
     "tightest converged cell it sits about 168 times above the value and, not decaying, gets "
     "looser without bound. b264 used the old envelope to CARRY THE TAIL beyond its node ceiling; "
     "**a constant is not integrable against `d\u03c1/\u03c1`, so under the source's convention the "
     "cutoff constant has a measured body and NO RIGOROUS TAIL BOUND from this route.** The ORDER "
     "is derived and unchanged; the CONSTANT is not certified. `W-ORD-SOURCE-TAIL` filed. **THE "
     "BEARING ON b262's BRANCH IS A BEARING ONLY \u2014 one archimedean OBJECT is not the "
     "archimedean SIDE, the branch remains UNDECIDED, and b242's law governs: *a measured rate is "
     "not a tail bound*.** NO ACT IS RE-VERDICTED AND NO GRADE MOVED. NO AGGREGATION IS STATED. "
     "M-2 REMAINS (SPECIFIED-NOT-STATED). h2 stands exactly where the deposit left it.",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b315 -- THE CALIBRATION\'S ROW, AND THE RATE\'S.')
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
    g1 = ('NEITHER ACT IS RE-VERDICTED' in r1[4]
          and 'NOT A LICENCE TO INTERPRET' in r1[4]
          and 'promoted to nothing' in r1[4])
    g2 = ('NO RIGOROUS TAIL BOUND' in r2[4]
          and 'BEARING ONLY' in r2[4]
          and 'not a tail bound' in r2[4])
    print('  row 1 refuses the re-verdict reading and the licence reading : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 reports the loss and bounds the bearing : %s  %s'
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
