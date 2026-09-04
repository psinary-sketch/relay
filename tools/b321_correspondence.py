# -*- coding: utf-8 -*-
"""b321_correspondence.py -- TWO ROWS: THE TWO FURTHER THEOREMS, AND THE WINDOW.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.**

### ### **THE HAZARD OF THESE TWO ROWS:**
###   ### **ROW ONE SAYS TWO MORE THEOREMS HELD, AND THAT READS AS THE INSTRUMENT BEING VINDICATED
###     ### THREE TIMES OVER.** ### It is that, at exactly the scope of three controls. ### But the
###     row must also carry that the identity ### **DID NOT CLOSE THE EXPONENT QUESTION** ### -- the
###     order said it would if it held, it held, and it did not -- because a row reporting only the
###     holding would be reporting the half that flatters.
###   ### ### **ROW TWO SAYS A BALANCE CAME OUT NON-POSITIVE AT TEN OF TEN CELLS, AND THAT IS THE
###     ### MOST DANGEROUS SENTENCE IN THIS RECORD.** ### It reads as arithmetic evidence. ### It is
###     forced by the shape of the computation: the pole term vanishes for lawful `f`, so the places
###     sum IS minus the zero side; the zero side is a sum of `|g-hat|^2` over an ordinate library
###     that contains only zeros ON the line; so the total cannot come out positive. ### **THE ROW
###     ### CARRIES THAT IN ITS STATEMENT CELL AND NOT IN A FOOTNOTE.**
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
    ("TWO FURTHER THEOREMS AS CONTROLS, AND AN EXPONENT THE MEASUREMENT COULD NOT SETTLE (b321)",

     "TWO FURTHER THEOREMS AS CONTROLS, AND AN EXPONENT THE MEASUREMENT COULD NOT SETTLE (b321): "
     "b320 tested the instrument against Theorem 1. This act tests it against two more. **THEOREM "
     "4.7 / (83) IS AN EQUALITY**, `Tr(theta(f) S) = W_8(f) + INT f(rho^-1) eps(rho) d*rho`, so by "
     "cyclicity b320's margin must be exactly minus the remainder integral. Computed with the b313 "
     "FLIPPED COPY -- the source's exponent, on b313's reading of three sites and on no number -- "
     "it gives `0.158890, 0.186482, 0.221284`, and **THE INSTRUMENT WALKS TOWARD EACH**: the "
     "residual along the domain ladder at `a = 1.3` falls `0.896557, 0.306328, 0.112555, 0.047182, "
     "0.023224`, by a factor of two to three at every step and at all three cells. **AND THE "
     "EXPLICIT FORMULA (148) CLOSES AT ALL THIRTEEN CELLS**, residuals `2.2e-09` to `3.6e-05` "
     "against the atlas's own sealed `TOL = 1e-03`, truncation bound never above `1.1e-11`.",

     "**NO TERMINAL, AND NO THEOREM IS PROVED HERE.** The source proved all three. What is "
     "decidable is that computed floats stand in stated relations at named frames. **AND THE "
     "ARCHIMEDEAN TERM IS CONFIRMED BY A SECOND ROUTE SHARING NO CODE WITH THE FIRST**, agreeing to "
     "`6.1e-05` -- which is simultaneously the SIGN test, since reading the source's page-49 "
     "sentence `W_8 = - W_R` the other way would put a factor of `-1` in that column. The window "
     "instrument's own fixture (i) reproduces `carto_atlas.channels(a)` on the atlas's OWN bump to "
     "`1.0e-16`; **A RE-IMPLEMENTATION THAT CANNOT REPRODUCE ITS ORIGINAL IS AN OVERWRITE.**",

     "**THE ORDER SAID THIS ACT CLOSES THE EXPONENT QUESTION BY MEASUREMENT IF THE IDENTITY HOLDS. "
     "IT HELD, AND IT DID NOT.** The corpus's own exponent copy passes every one of the same four "
     "arms at 3 of 3 cells. The two copies differ by `0.000981, 0.001937, 0.003994`; the "
     "instrument's own distance from the equality is `0.023224, 0.020793, 0.018808` -- five to "
     "twenty-four times larger. **AN INSTRUMENT CANNOT DISCRIMINATE BETWEEN TWO CANDIDATES THAT LIE "
     "CLOSER TOGETHER THAN ITS OWN DISTANCE FROM THE ANSWER.** b313 settled the exponent by READING "
     "and said a residue is not a vote; this is not a residue and it is still not a vote. **THE "
     "READING STANDS ALONE, WHERE b313 LEFT IT.** One quadrature defect is declared: the first pair "
     "of routes agreed only to `1.6e-05` against a sealed `1e-06`; **THE BAR DID NOT MOVE, THE "
     "QUADRATURE DID MORE WORK**, and both now integrate on the test function's own grid.",

     "**A CONTROL THAT HOLDS CERTIFIES THE INSTRUMENT, NOT THE OBJECT.** **SCOPE: three theorems, "
     "three covered cells, and the SIZE of the remainder integral certified where the size of no "
     "margin is.** The noise-floor gate REFUSES 3 of 6 and all three are domain frames; the "
     "identity values are RESOLVED and printed in a different column so the distinction cannot be "
     "lost. **NO BAR WAS MOVED, NO CELL DROPPED, NO TOLERANCE LOOSENED**, and the registration's "
     "seal `8a5107e9...` is the one it carried before the first control ran. **NO UNIT IS USED.** "
     "`W-ORD-ARCH-MEMBERSHIP` stays OPEN. NO ACT IS RE-VERDICTED AND NO GRADE MOVED. NO AGGREGATION "
     "IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. h2 stands exactly where the "
     "deposit left it. NOTHING DEPOSITS.",

     "current"),

    ("THE WINDOW OPENED, AND A NON-POSITIVE BALANCE THAT IS FORCED AND NOT MEASURED (b321)",

     "THE WINDOW OPENED, AND A NON-POSITIVE BALANCE THAT IS FORCED AND NOT MEASURED (b321): at the "
     "ten cells above `a = 2^{1/2}` the lawful `f = g conv g^#` is supported past `2`, so the "
     "primes enter through the local distribution. The places sum of Proposition C.1 is "
     "`SUM_v W_v(f) = PR - A`, every sign quoted from an owner, and it comes out **NON-POSITIVE AT "
     "10 OF 10 CELLS**. **AND THAT COUNT IS FORCED BY THE SHAPE OF THE COMPUTATION, NOT MEASURED "
     "FROM THE ARITHMETIC.** Two facts collapse it: **(i) THE POLE TERM VANISHES IDENTICALLY** for "
     "a lawful `f` -- `P = f-tilde(0) + f-tilde(1)` and Theorem 1's own vanishing conditions force "
     "both to zero, worst measured magnitude of order `1e-16` -- so (148) collapses to "
     "`SUM_v W_v = - Z`; and **(ii) `Z` CANNOT BE NEGATIVE**, because `f-hat = \\|g-hat\\|^2` (b320 "
     "measured it, 13 of 13) and the ordinate library holds only zeros ON the line. **SO THE TOTAL "
     "IS NON-POSITIVE BEFORE A SINGLE PRIME IS SUMMED.**",

     "**NO TERMINAL. THE CRITERION IS QUOTED AND NOT PARAPHRASED**: Proposition C.1 / (155), *RH "
     "<=> SUM_v W_v(g * g-bar^#) <= 0 for all g in C_c^8(R*_+) with g-tilde vanishing on a finite "
     "set containing {0,1}*. **WHAT IS DECIDABLE IS THAT THIRTEEN COMPUTED TOTALS ARE NEGATIVE. "
     "WHAT IS NOT IS THAT THIS SAYS ANYTHING ABOUT THE CRITERION**, which quantifies over every "
     "lawful `g`. A zero OFF the line is exactly what would break the sign, and this library "
     "contains none by construction. **A FINITE WINDOW AT A FINITE CUTOFF DECIDES NOTHING GLOBAL** "
     "-- 10000 ordinates, eleven primes, thirteen cells of one family.",

     "**ONE THING HERE IS A REAL MEASUREMENT AND THE ROW SAYS WHICH: THE PRIME SUM CHANGES SIGN "
     "TWICE ALONG THE LADDER** -- positive at `a = 1.5, 1.7`, negative from `1.9` through `2.4`, "
     "positive again at `2.8, 3.0`. That is the lawful `f` oscillating and `log 2` crossing from "
     "its positive core into its negative wing as the cell widens; **IT IS A FACT ABOUT WHERE "
     "`log p` FALLS IN A TEST FUNCTION** and is reported as that and nothing else. **THE PRIME SUM "
     "EXCEEDS THE MARGIN AT NO CELL**, `PR - margin` running `-0.217543` to `-0.706223` across all "
     "thirteen. b320's observation that the margin GROWS toward the boundary is restated as three "
     "numbers and **NOT EXTRAPOLATED**; nothing here reaches past `a = 3`.",

     "**A COUNT THAT COULD NOT HAVE COME OUT THE OTHER WAY IS NOT A RESULT.** **SCOPE: this act "
     "computed the balance on lawful objects and INTERPRETED IT BY NOBODY.** The registration caps "
     "`interpretations of the window's balance` at zero and `claims about h2, the identity's truth, "
     "or the complete roster` at zero, and both are re-measured by the gate suite. **NO WINDOW "
     "CLASS IS DECIDED**; `W-ORD-WINDOW-CLASS` and `W-ORD-ARCH-MEMBERSHIP` stay OPEN. NO ACT IS "
     "RE-VERDICTED AND NO GRADE MOVED. NO AGGREGATION IS STATED. M-2 REMAINS "
     "(SPECIFIED-NOT-STATED). h2 stands exactly where the deposit left it. NOTHING DEPOSITS.",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b321 -- THE TWO FURTHER THEOREMS, AND THE WINDOW.")
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
    g1 = ('IT HELD, AND IT DID NOT' in r1[3]
          and 'NO THEOREM IS PROVED HERE' in r1[2]
          and 'NO BAR WAS MOVED' in r1[4])
    g2 = ('FORCED BY THE SHAPE OF THE COMPUTATION' in r2[1]
          and 'DECIDES NOTHING GLOBAL' in r2[2]
          and 'IS NOT A RESULT' in r2[4])
    print('  row 1 carries the refuted conditional and the unmoved bar : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 says the count is FORCED and decides nothing global : %s  %s'
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
