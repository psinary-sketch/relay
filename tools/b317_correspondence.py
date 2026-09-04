# -*- coding: utf-8 -*-
"""b317_correspondence.py -- TWO ROWS: THE NUMBER, AND THE LINK IT BROKE.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.**

### ### **THE HAZARD OF THESE TWO ROWS:**
###   ### **ROW ONE REPORTS A PREDICTION THAT SCORED, AND A PREDICTION THAT SCORES READS AS
###     ### CONFIRMED.** ### It is not confirmed. ### The chain it rests on has a link this act
###     measured false, and the grade cell says so before it says anything else.
###   ### **ROW TWO REPORTS A NEGATIVE ABOUT THE CORPUS'S OWN WINDOW, AND THAT READS AS A
###     ### RE-VERDICT OF EVERY ACT THAT USED IT.** ### It is not one. ### Naming two quantities
###     different is a statement about what they are; no act is re-verdicted and no grade moves.
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
    ("THE SOURCE'S COMPRESSED SMEARED TRACE, COMPUTED ON THE OBJECT'S OWN SPACE (b317)",

     "THE SOURCE'S COMPRESSED SMEARED TRACE, COMPUTED ON THE OBJECT'S OWN SPACE (b317): "
     "`Tr(\u03d1(f) S)` of the source's Theorem 4.7, assembled from eq. (61) and Definition 4.4 "
     "alone \u2014 the scaling action integrated against a test function in `d*\u03bb`, which by the "
     "substitution `u = x/\u03bb` is the kernel `K(x,u) = f(x/u)/\u221a(xu)`, compressed by b316's "
     "projector and traced. **THE PROGRAMME NOW HAS AN ARCHIMEDEAN NUMBER COMPUTED ON THE OBJECT'S "
     "OWN SPACE**, at all thirteen cells the corpus banked and along the whole registered cutoff, "
     "for both test functions. Against a bar sealed BEFORE any value at any banked cell existed "
     "(`\\|T\\| \u2264 \\|A\\|/10`, scored on the largest `\\|T\\|` the whole domain sweep "
     "produces), **THE "
     "REGISTERED PREDICTION SCORES AS SMALL AT 13 CELLS OF 13** \u2014 ratios `0.09318` down to "
     "`0.00019`. **AND THE NARROWEST CELL SITS AT 93 PER CENT OF THE BAR**, so the bar was not a "
     "formality.",

     "**NO TERMINAL, AND THE SHADOW WAS EXPECTED TO BE NOTHING AND IS NOTHING** \u2014 quadrature "
     "on a truncated space is not finite-decidable. **ONE FACT HERE IS EXACT AND IS MARKED AS "
     "SUCH**: the control the order names \u2014 a scaling by the identity alone \u2014 returns "
     "`Tr(S)`, the truncation's dimension, as `free - rank` by orthonormality of `Q` rather than by "
     "a quadrature that happened to land; it was re-run at every one of the eight frames. The "
     "substitution is checked by a SECOND, independent code path that never builds a kernel: worst "
     "relative difference `5.931e-06` over `x > 1`, and `5.000e-01` under a deliberately halved "
     "kernel. **A ROUTE AGREEMENT THAT CANNOT FAIL IS NOT A CHECK.**",

     "**NO PRINT. NO UNIT USED ANYWHERE** \u2014 b300's derived archimedean unit is never "
     "constructed, never projected, never traced, because b316 declared the instrument NOT "
     "CERTIFIED for membership. **THE CANCELLATION IS THE BUMP'S OWN, NOT THE COMPRESSION'S**: for "
     "the corpus's integral-one bump the compression removes `98.6%` of an uncompressed trace of "
     "`10.945`, and for the mean-zero variant the SAME compression removes only `55%` of `23.740`. "
     "**A READER GIVEN ONLY THE DIFFERENCES COULD NOT TELL A SMALL OPERATOR FROM A LARGE ONE THAT "
     "NEARLY CANCELS.** Defects declared: the two-route control was first gated over the whole grid "
     "and FAILED at `4.26e-02`, located to the single first node where the kernel's `u`-window holds "
     "`0.750` of a grid point; and the band was first taken over three domain frames where the seal "
     "says five \u2014 both corrected before any verdict, with the superseded numbers discarded.",

     "**THE NUMBER IS NOT CONVERGED AND THE ACT DOES NOT PRETEND IT IS.** **SCOPE: THE REACH IS "
     "EMPTY** \u2014 no cell meets the joint 5% bar fixed before the run \u2014 **AND THE "
     "NOISE-FLOOR GATE REFUSES 8 PAIRS OF 12**, so NO POINT VERDICT IS TAKEN FROM EITHER AXIS; the "
     "scoring is a BAND statement for exactly that reason. The grid-axis drift spike is a RANK STEP "
     "(80\u219279) and not a quadrature error, and it is printed with its rank beside it. The domain "
     "axis is unconverged and `(T1)` changes sign along it at the wide cells. A DESIGN DEFECT OF "
     "THIS ACT'S OWN REGISTRATION: the sealed frame set has the two axes crossing at exactly ONE "
     "frame, so the joint reach test applies at one point and not along a sequence. **IT MAY NOT BE "
     "READ AS b300's** \u2014 `W-ORD-ARCH-MEMBERSHIP` is open. NO ACT IS RE-VERDICTED AND NO GRADE "
     "MOVED. NO AGGREGATION IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. `W2` is "
     "RECORDED and applied at the instrument and nowhere else. h2 stands exactly where the deposit "
     "left it. NOTHING DEPOSITS.",

     "current"),

    ("THE CORPUS'S WINDOW IS NOT THE SOURCE'S TEST-FUNCTION CLASS (b317)",

     "THE CORPUS'S WINDOW IS NOT THE SOURCE'S TEST-FUNCTION CLASS (b317): b316 registered its "
     "prediction on a chain of five links and named each as a way for it to be wrong for a reason "
     "that has nothing to do with the mathematics. Four of the five this act cannot touch. **THE "
     "FIFTH IT MEASURED, AND THE FIFTH IS FALSE.** The source's eq. (54) requires "
     "`\u222b f(\u03c1) \u03c1^{\u00b11/2} d*\u03c1 = 0`; **THE CORPUS'S INTEGRAL-ONE BUMP HAS THAT "
     "MOMENT AT `1.003`, `1.010` AND `1.024`** at `a = 1.5, 2, 3` \u2014 not zero and not near it. "
     "And **FIVE OF THE THIRTEEN CELLS ALSO LEAVE eq. (53)'s SUPPORT CONDITION** `[1/2, 2]`, so "
     "`W_\u221e` is not defined for them by the source's own display. A mean-zero variant built from "
     "three of the corpus's own bumps DOES satisfy both moments, to `2.8e-17`, by construction.",

     "**NO TERMINAL.** **THE CLASS TEST FIRES IN BOTH DIRECTIONS, WHICH IS WHAT MAKES THE NEGATIVE "
     "READABLE**: the variant vanishes on both of the source's moments to machine precision while "
     "the corpus's bump does not, so a class test that everything passes is not what produced this. "
     "Theorem 4.7 itself carries NEITHER condition \u2014 its (83) is stated for all "
     "`f \u2208 C_c^\u221e(R*_+)` \u2014 and that display was located on the same run rather than "
     "smoothed over, so the failure is attributed to eq. (53) and eq. (54) and not to the theorem.",

     "**NO PRINT. NO INSTRUMENT EDITED.** The consequence for the prediction is stated where it "
     "belongs: **A PREDICTION WHOSE NUMBER LANDS WHILE A LINK IT RESTS ON IS MEASURED WRONG HAS NOT "
     "BEEN CONFIRMED BY THE LANDING.** It has produced a number that agrees with a chain containing "
     "a broken link. The entailment the order names is therefore stated at exactly its scope and "
     "then bounded: the source's Theorem 4.7 supplies a DEFINITION for the quantity the corpus's "
     "near-cancellation lacked one for, **BUT THE CORRESPONDENCE CANNOT BE READ AS IDENTIFYING THE "
     "CORPUS'S WINDOW WITH THE SOURCE'S CLASS, BECAUSE THAT IS THE THING THIS ACT REFUSED.** "
     "`W-ORD-WINDOW-CLASS` is filed.",

     "**A MEASUREMENT ABOUT A WINDOW, NOT A VERDICT ON AN ACT.** **SCOPE, AND IT IS THE WHOLE OF "
     "THE ROW'S HONESTY: NO ACT IS RE-VERDICTED AND NO BANKED MEASUREMENT IS CALLED WRONG.** The "
     "corpus's `A` is a one-dimensional integral of a transform against a kernel; "
     "`Tr(\u03d1(f) S)` is a compressed operator trace on a truncation of Sonin's space. **NAMING "
     "TWO QUANTITIES DIFFERENT IS A STATEMENT ABOUT WHAT THEY ARE, NOT A FINDING THAT EITHER WAS "
     "COMPUTED WRONGLY**, and no grade moves. This row says nothing about the identity, about h2, or "
     "about the roster. It does not decide whether a test function inside the source's class exists "
     "that the corpus's channel could be re-formed against \u2014 that is the question it opens and "
     "does not answer. NO AGGREGATION IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED). h2 stands "
     "exactly where the deposit left it.",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b317 -- THE NUMBER\'S ROW, AND THE BROKEN LINK\'S.')
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
    g1 = ('THE REACH IS EMPTY' in r1[4]
          and 'NO POINT VERDICT IS TAKEN' in r1[4]
          and 'NO UNIT USED ANYWHERE' in r1[3]
          and 'CONFIRMED' not in r1[1])
    g2 = ('NO ACT IS RE-VERDICTED AND NO BANKED MEASUREMENT IS CALLED WRONG' in r2[4]
          and 'HAS NOT BEEN CONFIRMED BY THE LANDING' in r2[3]
          and 'BOTH DIRECTIONS' in r2[2])
    print('  row 1 refuses the converged reading and carries the no-unit cap : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 refuses the confirmation and the re-verdict readings : %s  %s'
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
