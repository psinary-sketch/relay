# -*- coding: utf-8 -*-
"""b316_correspondence.py -- TWO ROWS: THE INSTRUMENT, AND WHAT IT FAILED TO REPRODUCE.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.**

### ### **THE HAZARD OF THESE TWO ROWS:**
###   ### **ROW ONE ANNOUNCES AN INSTRUMENT, AND AN INSTRUMENT READS AS A CAPABILITY.** ### What it
###     is capable of is listed, and ### **WHAT IT IS NOT CERTIFIED FOR IS IN THE SAME CELL**, not
###     in a later act's correction.
###   ### **ROW TWO REPORTS A NON-CONFIRMATION, AND A NON-CONFIRMATION READS AS A REFUTATION.** ###
###     It is not one. ### b300's derivation is on the WHOLE LINE and this is a truncation; the
###     grade cell says so before it says anything else. ### **AND THE CONTROL THAT WOULD HAVE
###     ### SETTLED IT COULD NOT FIRE**, which is stated as a limit and not skipped.
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
    ("A COMPUTABLE TRUNCATION OF THE SOURCE'S OWN ARCHIMEDEAN SPACE (b316)",

     "A COMPUTABLE TRUNCATION OF THE SOURCE'S OWN ARCHIMEDEAN SPACE (b316): `S(1,1)` built from "
     "Definition 4.4 and nothing else, on even functions over `[0, X]` at `N` midpoints, with the "
     "source's inner product (eq. 16), the source's transform normalization (eq. 24), the source's "
     "scaling exponent (eq. 61) and the source's two vanishing conditions (eq. 72) as linear "
     "constraints. **THE FIRST ARCHIMEDEAN INSTRUMENT THE CORPUS HAS WHOSE VECTORS ARE INSIDE THE "
     "OBJECT'S OWN SPACE.** Its dimension at five truncations is `914`, `1904`, `3888`, `3887`, "
     "`5870`, and **IT GROWS WITHOUT BOUND UNDER REFINEMENT, WHICH IS THE SOURCE'S OWN SENTENCE "
     "APPEARING AS A MEASUREMENT** \u2014 the paper calls the space *the well-known infinite "
     "dimensional Sonin's space*. **AND THE SOURCE'S SECOND SENTENCE IS REPRODUCED AND SHARPENED**: "
     "the paper says the scaling action *does not restrict to this subspace*, and the instrument "
     "says WHICH condition breaks \u2014 condition one survives EXACTLY at every dilation tested "
     "(`0.00e+00` at each), and the whole of the failure is in the transform condition, whose "
     "leakage rises monotonically from `0.1352` at `\u03bb = 1.25` to `0.4253` at `\u03bb = 4`.",

     "**NO TERMINAL, AND THE SHADOW WAS EXPECTED TO BE NOTHING AND IS NOTHING** \u2014 an "
     "instrument build and floating-point measurements on a grid; a quadrature is not "
     "finite-decidable. **TWO FACTS HERE ARE EXACT AND ARE MARKED AS SUCH**: a vector supported in "
     "`[0,1]` projects to exactly zero by disjoint support, and condition one survives every "
     "dilation `\u03bb \u2265 1` by an argument about arguments rather than by luck of the grid. "
     "The transform carries a positive control that CAN fail \u2014 the Gaussian is recovered to "
     "`5.551e-16` and, under a deliberately halved normalization, misses by `5.000e-01`. **A "
     "TRANSFORM CHECK THAT CANNOT FAIL IS NOT A CHECK.**",

     "**NO PRINT. NO TRACE COMPUTED AND NO SMEAR ASSEMBLED** \u2014 that is act two under its own "
     "registration, and this act's caps forbid it. **A DEFECT OF THIS ACT'S OWN, DECLARED: THE "
     "FIRST BUILD TIED THE TRANSFORM GRID TO THE FUNCTION GRID**, which made the second condition "
     "weaken as the domain lengthened, and at `X = 64` the instrument admitted a vector b292 had "
     "derived was outside the space. **IT WAS CAUGHT BY THE DISCRIMINATION ARM AND NOT BY "
     "INSPECTION**, every number printed before the repair was discarded, and the components were "
     "re-run from the top. A second defect: a draft claimed the rank equals the constraint count "
     "and the act's own table contradicted it \u2014 **THE TABLE WAS RIGHT AND THE SENTENCE WAS "
     "WRONG.** `W-ORD-ARCH-NORM-READING` is DISCHARGED, by the source's eq. (16) and not by this "
     "act's opinion; its reach is the additive arm only.",

     "**AN INSTRUMENT BUILD, AND ITS LIMITS ARE IN THIS CELL RATHER THAN IN A LATER ACT'S "
     "CORRECTION.** **SCOPE: IT CAN decide exactly that a vector supported in the unit interval is "
     "orthogonal to the space; decide exactly that condition one survives any dilation at or above "
     "one; measure how far a given vector lies outside the space, with a discrimination arm that "
     "fires; measure the scaling leakage; apply the compression as an operator; and accept either "
     "test function. IT CANNOT decide membership (see the next row), converge to a fixed finite "
     "answer under refinement, separate a truncation effect from a construction effect at the "
     "truncations reached, or say anything about the p-adic places \u2014 b285's boundary stands "
     "and b309's zero does not travel.** NO ACT IS RE-VERDICTED AND NO GRADE MOVED. NO AGGREGATION "
     "IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The window ruling W2 is "
     "RECORDED AND UNAPPLIED beyond the single construction-time consequence the order licenses. "
     "h2 stands exactly where the deposit left it. NOTHING DEPOSITS.",

     "current"),

    ("THE PROLATE VECTORS ARE OUTSIDE AND THE ARCHIMEDEAN UNIT IS UNCONFIRMED (b316)",

     "THE PROLATE VECTORS ARE OUTSIDE AND THE ARCHIMEDEAN UNIT IS UNCONFIRMED (b316): the "
     "instrument's mandatory reproduction arm, run against everything the record already owns. "
     "**b292 IS CONFIRMED BY A SECOND AND INDEPENDENT ROUTE** \u2014 the corpus's expansion "
     "vectors `\u03b6_n` pass condition one and fail condition two with residual `1.0000` at "
     "`n = 0,1,2,3` and at every truncation, where b292 derived the same failure from the source's "
     "statement about `\u03c8_n`; **NEITHER IS EVIDENCE FOR THE OTHER, AND THAT IS WHY BOTH ARE IN "
     "THE RECORD.** The source's own worked inner product is RECOVERED to `0.00e+00`. **AND b300's "
     "MEMBERSHIP IS NOT CONFIRMED**: the derived archimedean unit, built on this grid by the "
     "corpus's own solver `b205_prolate`, has residual `0.9455`, `0.8023`, `0.5527`, `0.6033`, "
     "`0.4902` across five truncations \u2014 falling with the domain, not monotone between the "
     "two cells that share one, and nowhere near zero.",

     "**NO TERMINAL.** **THE DISCRIMINATION ARM FIRES, WHICH IS WHAT MAKES THE NEGATIVE READABLE**: "
     "`\u03b6_0` sits at `1.0000` at every cell of the same sweep, so a small number in the unit's "
     "column would have MEANT something. **THE EASY EXPLANATION WAS TESTED AND REFUSED**: replacing "
     "the hard cut at the end of the domain with a smooth taper moves the residual from `0.8023` to "
     "`0.8020`, so it is not an edge artefact. **AND THE CONTROL THAT WOULD HAVE SETTLED THE "
     "CONSTRUCTION COULD NOT FIRE** \u2014 the asymptotic check confirms the decay and the "
     "frequency (`x u` bounded beyond `x = 2`, 60 sign changes against 59 for a sine of the "
     "expected period), but run at two values of the spectral parameter that are NOT eigenvalues it "
     "returns `1.1435` and `1.1558` against the eigenvalue's `1.1323`. **BY b308's LAW A CONTROL "
     "THAT CANNOT FIRE READS AS A PASS, AND IT IS REPORTED AS NOT-A-CHECK.**",

     "**NO PRINT. NO INSTRUMENT EDITED.** The corpus's remainder instrument is deliberately NOT "
     "reproduced here, and the reason is the first half of this row: it expands in vectors this act "
     "has just measured to be outside the space, so reproducing it would be this instrument "
     "computing somebody else's object and calling the agreement a check. **THREE CAUSES REMAIN "
     "CONSISTENT WITH THE UNCONFIRMED RESIDUAL AND THIS ACT CHOOSES NONE**: the truncation is too "
     "short and the missing mass is real; the discretized second condition is not the true one; or "
     "this construction of the unit is not b300's object \u2014 which the asymptotic control cannot "
     "exclude because it cannot discriminate.",

     "**A REPRODUCTION ARM, AND ONE OF ITS FOUR DID NOT CONFIRM.** **SCOPE, AND IT IS THE WHOLE OF "
     "THE ROW'S HONESTY: b300 IS NOT RE-VERDICTED AND IS NOT CALLED WRONG.** b300's derivation is "
     "on the WHOLE LINE; this is a truncation, and b15's law governs \u2014 *a finite-place-set "
     "object at a finite cutoff decides nothing global*. **A TRUNCATION THAT FAILS TO REPRODUCE A "
     "WHOLE-LINE FACT HAS REPORTED SOMETHING ABOUT THE TRUNCATION UNTIL IT IS SHOWN OTHERWISE**, "
     "and this act does not show otherwise. b300's grade does not move. **THE INSTRUMENT IS "
     "DECLARED NOT YET CERTIFIED FOR MEMBERSHIP QUESTIONS AND ACT TWO MAY NOT USE IT FOR ONE**; "
     "`W-ORD-ARCH-MEMBERSHIP` is filed, and until it is settled no quantity computed on this space "
     "may be read as b300's. NO ACT IS RE-VERDICTED AND NO GRADE MOVED. NO AGGREGATION IS STATED. "
     "M-2 REMAINS (SPECIFIED-NOT-STATED). h2 stands exactly where the deposit left it.",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b316 -- THE INSTRUMENT\'S ROW, AND THE REPRODUCTION\'S.')
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
    g1 = ('IT CANNOT decide membership' in r1[4]
          and 'NOT YET CERTIFIED' not in r1[1]
          and 'NO TRACE COMPUTED AND NO SMEAR ASSEMBLED' in r1[3])
    g2 = ('b300 IS NOT RE-VERDICTED AND IS NOT CALLED WRONG' in r2[4]
          and 'decides nothing global' in r2[4]
          and 'NOT-A-CHECK' in r2[2]
          and 'CHOOSES NONE' in r2[3])
    print('  row 1 carries the limits in its own grade cell and forbids the trace : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 refuses the refutation reading and reports the dead control : %s  %s'
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
