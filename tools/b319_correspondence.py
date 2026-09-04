# -*- coding: utf-8 -*-
"""b319_correspondence.py -- TWO ROWS: THE STABLE RANK, AND WHAT THE ACT OWED ITSELF.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.**

### ### **THE HAZARD OF THESE TWO ROWS:**
###   ### **ROW ONE ANNOUNCES A RANK THAT HOLDS STILL, AND THAT READS AS CONVERGENCE.** ### It is
###     not. ### The grid axis converged; the domain axis did not and its gate refuses it. ### And
###     the subspace CHANGED, so the values on it changed too.
###   ### **ROW TWO REPORTS A DEFECT DISCHARGED AND A BAR THAT CANNOT BE MET.** ### The first reads
###     as a mathematical result and is bookkeeping; the second reads as a failure of the instrument
###     and is a failure of the act's own sealed bar.
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
    ("THE SUBSPACE BY THE SOURCE'S EIGENVALUE-ONE CHARACTERIZATION, AND A RANK THAT HOLDS STILL "
     "(b319)",

     "THE SUBSPACE BY THE SOURCE'S EIGENVALUE-ONE CHARACTERIZATION, AND A RANK THAT HOLDS STILL "
     "(b319): b318 measured that the instrument's grid-axis error was its own rank discretization "
     "and filed two schemes SPECIFIED and NOT BUILT. This act builds the source's own. The paper's "
     "(81) reads `P P\u0302 P = \u03a3 \u03bb(n)\u00b2 \\|\u03b6\u2099><\u03b6\u2099\\| + R` with *R the "
     "orthogonal projection on Sonin's space*, and page 28 says `S(1,1)` **IS** the eigenvalue-one "
     "eigenspace \u2014 so the spectrum is `{\u03bb(n)\u00b2}` together with `1`, and an eigenvalue "
     "is DIMENSIONLESS. On the free coordinates the sandwich is `M = I \u2212 (hy/h) C\u1d40C`. "
     "**ON THE GRID AXIS AT X = 32 THE SELECTED DIMENSION IS 69, 69, 69, 69 ACROSS "
     "N = 2048...16384, WHERE b316's SCHEME GAVE 80, 80, 79, 79** \u2014 rank changes: b316 one, "
     "this act zero. **AND THE DRIFT FELL WITH IT**: `8.6e-05` to `4.5e-04` where b318 measured "
     "`6.1e-03` to `2.3e-02`.",

     "**NO TERMINAL, AND ONE STATEMENT HERE IS FINITE-DECIDABLE AND THE ROW SAYS WHICH**: the rank "
     "is `#{k : \u03c3\u00b2 > \u03c4}`, a count of machine floats against a fixed constant, and "
     "whether two frames give the same count is decidable in the same sense. **WHAT IS NOT "
     "DECIDABLE IS THAT THE COUNT IS THE DIMENSION OF THE SOURCE'S EIGENSPACE.** The derivation of "
     "the discretization constant is falsifiable and was falsified-tested: a projection sandwich has "
     "its spectrum in `[0,1]`, and the measured range is `[7.964e-34, 1.000000]`. **AND THE "
     "THRESHOLD, FIXED BEFORE ANY SPECTRUM WAS SEEN, LANDED IN A MEASURED VOID**: largest admitted "
     "`~2.0e-07`, smallest excluded `5.624e-06 ... 5.643e-06`, itself stable to four digits under "
     "refinement.",

     "**NO PRINT FROM THE INSTRUMENT WORK. NO NEW TEST FUNCTION AND NO NEW UNIT DEFINED** \u2014 "
     "b317's variant and b316's unit are imported and measured. **THE SUBSPACE CHANGED AND THE ROW "
     "SAYS SO RATHER THAN CALLING THIS A REPRODUCTION OF VALUES**: the stable cut STRICTLY CONTAINS "
     "b316's (`only grid` 9 to 12 at every frame, `only stable` 0), so the square and smear are "
     "numbers on a larger space \u2014 the smear is negative at 3 cells here where b318 found 5. The "
     "structural findings survive: square never negative, the square-equals-smear-of-the-"
     "autocorrelation identity re-proved at `3.3e-06` to `2.6e-05` against a sealed one per cent, "
     "\u03b6\u2099 residual `1.0000` on both cuts at all eight frames, the source's worked inner "
     "product at `2.22e-16`. **b316, b317 AND b318 ARE NOT RE-VERDICTED**: a different cut is a "
     "different cut and both are printed.",

     "**A RANK THAT HOLDS STILL IS NOT CONVERGENCE.** **SCOPE: THE GRID HALF OF THE REACH IS "
     "ATTAINED AND THE DOMAIN HALF IS NOT.** Every grid drift is 60 to 600 times inside the sealed "
     "bar with the rank constant; **the noise-floor gate REFUSES all six domain pairs**, so no point "
     "verdict is taken from that axis and every domain statement is a band statement. The domain "
     "rank must grow because the space does (`20, 37, 69, 133, 262`). **THE UNIT'S RESIDUAL IS "
     "REPORTED AS A MEASUREMENT WITH NO VERDICT**: `0.4395` constant across all four grid "
     "refinements on the stable cut, where the grid cut drifts `0.8084...0.7880` \u2014 it now holds "
     "still, and it is still nowhere near zero. `W-ORD-ARCH-MEMBERSHIP` is open and blocking; "
     "nothing computed on this space may be read as b300's. NO ACT RE-VERDICTED, NO GRADE MOVED. NO "
     "AGGREGATION IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. h2 stands exactly "
     "where the deposit left it. NOTHING DEPOSITS.",

     "current"),

    ("THE KERNEL-COVERAGE DEFECT DISCHARGED, AND A REACH BAR THAT CANNOT BE MET (b319)",

     "THE KERNEL-COVERAGE DEFECT DISCHARGED, AND A REACH BAR THAT CANNOT BE MET (b319): b315 wrote "
     "the coverage gate, ran it in the state where it FIRES, and repaired nothing; b316, b317 and "
     "b318 each re-ran it and each left it open. **THIS ACT REPAIRED IT, AND THE REPAIR IS A BUILD.** "
     "The profile was first regenerated from source and compared **TO THE GIT BLOB, NOT THE WORKING "
     "FILE** \u2014 `33195` bytes each, byte-for-byte identical; the working file is 475 bytes "
     "longer, one per line, which is `core.autocrlf` and not the kernel. Ten Core modules had no "
     "compiled artefact at all; all ten compiled, 0 build errors. Twenty-four imports and ninety-one "
     "print lines were appended. **PRINTS 475 \u2192 566, AND THE OLD PROFILE IS A LITERAL BYTE "
     "PREFIX OF THE NEW ONE.** **AXIOM-BEARING TERMINALS AMONG THE 91 NEWLY CERTIFIED: 0**, read off "
     "the printed file. The gate now PASSES.",

     "**NO NEW TERMINAL WAS PROVED BY ANY OF THIS.** Every one of the ninety-one was already "
     "compiling; the defect was that the certification file never printed them. **THAT IS "
     "BOOKKEEPING THE RECORD OWED ITSELF AND NO MATHEMATICAL CLAIM RESTS ON IT.** A repair that "
     "cannot first reproduce the thing it is about to change is an overwrite, which is why the "
     "baseline ran before the edit; and the edit was append-only in both regions so the pre-existing "
     "block keeps its ORDER as well as its bytes by construction. The gate's own fixtures still show "
     "it can fail \u2014 a gate that has just been made to pass is exactly the gate whose fixtures "
     "have to be re-read.",

     "**AND THE REACH IS STILL EMPTY, 0 OF 6, BECAUSE THE BAR THIS ACT SEALED IS DEFECTIVE.** (B3) "
     "requires the rank CONSTANT across each step of BOTH axes; on the domain axis that is "
     "**UNSATISFIABLE BY THE NATURE OF THE OBJECT**. The second scheme was tried as the order "
     "requires: **on the grid axis pinning selects the IDENTICAL index set** \u2014 it is the same "
     "subspace reached by a weaker argument \u2014 and **on the domain axis it admits a direction at "
     "eigenvalue-distance `1.000e+00` from one**, manufacturing constancy by calling out-of-space "
     "directions in. **IT IS REFUTED, NOT DEFERRED.** `W-ORD-REACH-BAR` is filed. One further "
     "defect is declared: the registration was sealed with a banned stem in it and then RE-SEALED, "
     "with the superseded hash written into the seal block.",

     "**A DEFECT DISCHARGED IS NOT A RESULT, AND A BAR THAT CANNOT BE MET IS THE ACT'S OWN FAULT.** "
     "**SCOPE: the coverage repair proves nothing mathematical**, and the empty reach is reported "
     "under the bar AS WRITTEN rather than reinterpreted after the fact \u2014 the registration is "
     "sealed and this act does not edit it. What the next act should seal instead is stated as a "
     "PROPOSAL and not as a change: rank constancy as a condition on the grid axis only, with the "
     "domain axis carrying a convergence bar and no rank condition. `W-ORD-KERNEL-COVERAGE` is "
     "DISCHARGED; `W-ORD-RANK-STABLE-SUBSPACE` is discharged on the grid axis; "
     "`W-ORD-ARCH-MEMBERSHIP` and `W-ORD-WINDOW-CLASS` stay OPEN. NO ACT IS RE-VERDICTED AND NO "
     "GRADE MOVED. NO AGGREGATION IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED). h2 stands exactly "
     "where the deposit left it.",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b319 -- THE STABLE RANK\'S ROW, AND THE REPAIR\'S.')
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
    g1 = ('A RANK THAT HOLDS STILL IS NOT CONVERGENCE' in r1[4]
          and 'THE SUBSPACE CHANGED AND THE ROW SAYS SO' in r1[3]
          and 'NO VERDICT' in r1[4])
    g2 = ('A DEFECT DISCHARGED IS NOT A RESULT' in r2[4]
          and 'THE BAR THIS ACT SEALED IS DEFECTIVE' in r2[3]
          and 'BOOKKEEPING THE RECORD OWED ITSELF' in r2[2])
    print('  row 1 refuses the convergence reading and owns the changed subspace : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 refuses the result reading and owns the defective bar : %s  %s'
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
