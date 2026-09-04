# -*- coding: utf-8 -*-
"""b318_correspondence.py -- TWO ROWS: THE SQUARE, AND THE LETTER.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.**

### ### **THE HAZARD OF THESE TWO ROWS:**
###   ### **ROW ONE REPORTS A POSITIVITY THAT HELD, AND A POSITIVITY THAT HOLDS READS AS A THEOREM
###     ### CONFIRMED.** ### It is not one. ### The source already proved it; this act checked that
###     the truncation does not destroy it, and the nonnegativity it reports is ARITHMETIC.
###   ### **ROW TWO REPORTS THAT b317's OBJECT IS NOT THE SOURCE'S, AND THAT READS AS b317 BEING
###     ### WRONG.** ### It is not. ### b317's numbers are correctly computed values of the thing it
###     computed; they are RE-LABELLED, and a re-labelling is not a re-verdict.
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
    ("THE SOURCE'S SQUARE FORM IS NONNEGATIVE ON THE TRUNCATION AND THE CORPUS'S SMEAR IS NOT (b318)",

     "THE SOURCE'S SQUARE FORM IS NONNEGATIVE ON THE TRUNCATION AND THE CORPUS'S SMEAR IS NOT "
     "(b318): the paper says where its positivity lives \u2014 *\u201cthis functional is positive "
     "definite by construction, since when evaluated on f = g\u22c6g\u002a it is the trace "
     "Tr(\u03d1(g) S \u03d1(g)\u002a) of a positive operator\u201d*. That object is a "
     "Hilbert-Schmidt norm squared, and this act computes it on b316's truncation at all thirteen "
     "banked cells over b317's own frames. **CELLS AT WHICH THE SQUARE IS NEGATIVE ANYWHERE: 0. "
     "CELLS AT WHICH b317's SMEAR IS NEGATIVE ANYWHERE: 5.** **AND THE FIRST DIFFERING CONSTITUENT "
     "IS NAMED AND PROVED, NOT ASSERTED**: since \u03d1(f)\u002a\u03d1(f) = \u03d1(f\u002a\u22c6f), "
     "the source's square form is the corpus's smear evaluated at the AUTOCORRELATION of the "
     "window where the corpus evaluates it at the window \u2014 checked by two independent code "
     "paths at three cells, agreeing to `1.9e-06`, `4.2e-06` and `3.4e-05` against a sealed bar of "
     "one per cent.",

     "**NO TERMINAL, BUT ONE STATEMENT HERE IS FINITE-DECIDABLE AND THE ACT SAYS WHICH.** The "
     "square is formed as the Frobenius norm squared of one matrix and **`square_trace` PERFORMS NO "
     "SUBTRACTION ANYWHERE**: every summand is the square of a machine float, so a running sum of "
     "them cannot go below zero. At `N=256, X=8, NY=64` the value is `2.748830149073` and its "
     "nonnegativity is decided as arithmetic. **WHAT IS NOT DECIDABLE IS THAT THIS SUM IS THE "
     "OPERATOR-THEORETIC NORM** \u2014 that rests on the quadrature, the numerical rank and the "
     "truncation, and the two statements are kept apart. b317's under-resolved first grid node is "
     "not reached by this object either: the square's smallest contributing row is `x = 0.66667`, "
     "whose window holds `17.78` points, and the question was asked again rather than inherited.",

     "**NO PRINT. NO UNIT USED ANYWHERE** \u2014 b300's derived archimedean unit is never "
     "constructed, projected or traced. **AND `W_\u221e` IS NOT COMPUTED IN ANY DIRECTION**: both "
     "objects here are trace-side, so neither side of the source's inequality is evaluated. **THE "
     "RANK IS THE GRID-AXIS ERROR, MEASURED**: grid steps that KEEP the rank drift by `2.7e-05` to "
     "`1.2e-04`, and the one step that CHANGES it (80\u219279) drifts by `6.1e-03` to `2.3e-02` "
     "\u2014 two orders of magnitude larger, at every cell and on both objects. b317 named this; "
     "this act measures it. A rank-stable refinement scheme is SPECIFIED in two forms (pin the rank; "
     "or use the source's own eigenvalue-one characterization of S(1,1)) and **NOT BUILT**.",

     "**A POSITIVITY THAT HELD IS NOT A THEOREM CONFIRMED.** **SCOPE: the source already proved "
     "this positivity; what this act checked is that the truncation does not destroy it, and the "
     "check is arithmetic rather than analytic.** **THE REACH IS EMPTY, 0 OF 6** \u2014 (B3) adds "
     "rank stability to b317's sealed five per cent, and every grid step at the reference frame "
     "crosses `80\u219279` while every domain step crosses `80\u2192145`. **THE NOISE-FLOOR GATE "
     "REFUSES 6 PAIRS OF 12**, all of them on the domain axis, so no point verdict is taken from it "
     "and every domain statement is a band statement. IT MAY NOT BE READ AS b300's \u2014 "
     "`W-ORD-ARCH-MEMBERSHIP` is open. `W-ORD-RANK-STABLE-SUBSPACE` is filed. NO ACT IS "
     "RE-VERDICTED AND NO GRADE MOVED. NO AGGREGATION IS STATED. M-2 REMAINS "
     "(SPECIFIED-NOT-STATED) under b310's cap. h2 stands exactly where the deposit left it. NOTHING "
     "DEPOSITS.",

     "current"),

    ("THE CORPUS'S WINDOW IS A CANDIDATE g AND NOT A CANDIDATE f (b318)",

     "THE CORPUS'S WINDOW IS A CANDIDATE g AND NOT A CANDIDATE f (b318): decided by the source's "
     "own Definition 3.1 \u2014 *\u201cf is positive definite when its Fourier transform is "
     "pointwise positive\u201d* \u2014 applied as a scan at every banked cell. **THE MEAN-ZERO "
     "VARIANT IS NOT POSITIVE DEFINITE AT ANY CELL** (`min f\u0302 = -1.3119e-01`), **AND NEITHER "
     "IS THE CORPUS'S INTEGRAL-ONE BUMP** (`-9.8392e-02`): **0 OF 13 FOR BOTH COLUMNS**, so neither "
     "is of the form g\u22c6g\u002a. But Theorem 1 puts its conditions on **g**, not on f \u2014 "
     "support in `[2^-1/2, 2^1/2]` and Fourier transform vanishing at `i/2` **and at 0** \u2014 and "
     "**THE VARIANT SATISFIES BOTH VANISHING CONDITIONS AT 13 OF 13 CELLS AND THEOREM 1's SUPPORT "
     "INTERVAL AT 3 OF 13** (`a = 1.3, 1.35, 1.41`). At those three cells the corpus holds an "
     "admissible g in the source's own sense.",

     "**NO TERMINAL.** **THE CLASS TEST FIRES IN BOTH DIRECTIONS, WHICH IS WHAT MAKES THE NEGATIVE "
     "READABLE**: its fixtures require it to say YES on a genuine autocorrelation and NO on a "
     "function known not to be one by an argument about widths rather than by a measurement. **AND "
     "ITS REACH IS STATED WITH ITS RESULT**: a negative value proves a function is NOT positive "
     "definite; a nonnegative scan does not prove that it is, beyond the interval scanned, and this "
     "act only ever uses the first direction. The minimum is the same number at every cell because "
     "the variant's shape is fixed and only its width changes \u2014 `f\u0302` depends on `tL` "
     "alone \u2014 so the table's last two columns are a consistency check on the scan as well as a "
     "finding.",

     "**NO PRINT. NO INSTRUMENT EDITED** \u2014 `b316_instrument.py` and `b317_smear.py` are owners "
     "and are imported, not modified. **THE CONSEQUENCE FOR b317, STATED WHERE IT BELONGS: b317's "
     "NUMBERS ARE RE-LABELLED AND b317 IS NOT RE-VERDICTED.** b317's column is `Tr(\u03d1(f) S)` on "
     "the truncation, correctly computed at the cells and frames it stated; what it is not is the "
     "source's trace side, because that is the same expression only when f is already an "
     "autocorrelation. **SO b317's NUMBERS CARRY NO POSITIVITY PROMISE FROM THE SOURCE AND NEVER "
     "DID** \u2014 its grade does not move, its prediction score stands as b317 stated it, and "
     "nothing it measured is called wrong.",

     "**A DEFINITIONAL FINDING, AND IT DISSOLVES b317's ANOMALY RATHER THAN RESOLVING IT.** "
     "**SCOPE: THE SIGN CHANGE IS NOT A VIOLATION OF ANYTHING.** The source's positivity is a "
     "statement about `Tr(\u03d1(g) S \u03d1(g)\u002a)`, which stayed positive at every cell and "
     "every frame; `Tr(\u03d1(f) S)` at an f outside the source's class carries no promise from the "
     "paper, and its going negative at `a = 2.4, 2.8, 3.0` contradicts nothing. **THIS ROW DOES NOT "
     "EVALUATE THE SOURCE'S INEQUALITY OR EITHER SIDE OF IT**, and it does not claim either "
     "function is positive definite anywhere. `W-ORD-WINDOW-CLASS` is UPDATED and NOT closed: the "
     "question is no longer whether the window is in the class but WHICH LETTER it is, and what is "
     "owed is the author's decision. NO ACT IS RE-VERDICTED AND NO GRADE MOVED. NO AGGREGATION IS "
     "STATED. M-2 REMAINS (SPECIFIED-NOT-STATED). h2 stands exactly where the deposit left it.",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b318 -- THE SQUARE\'S ROW, AND THE LETTER\'S.')
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
          and 'A POSITIVITY THAT HELD IS NOT A THEOREM CONFIRMED' in r1[4]
          and 'NO UNIT USED ANYWHERE' in r1[3]
          and 'PERFORMS NO SUBTRACTION ANYWHERE' in r1[2])
    g2 = ('THE SIGN CHANGE IS NOT A VIOLATION OF ANYTHING' in r2[4]
          and 'RE-LABELLED AND b317 IS NOT RE-VERDICTED' in r2[3]
          and 'BOTH DIRECTIONS' in r2[2])
    print('  row 1 refuses the theorem reading and carries the no-subtraction fact : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 refuses the re-verdict reading and states the dissolution : %s  %s'
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
