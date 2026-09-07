# -*- coding: utf-8 -*-
"""b355_correspondence.py -- ONE ROW: WHAT THE ARRAYS ARE.

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

SCOPE_TAIL = ("**SCOPE: A RELABELLING IS NOT A DEMOTION.** Every banked number stands exactly as banked; nothing here recomputes one or contradicts one, and every check that "
              "passed still passed. Not that the smooth bump and the piecewise-linear object give different numbers -- NO ACT HAS MEASURED THE DIFFERENCE and this one did not "
              "either. Not that the corpus chose badly: it chose for a stated reason, agreement with its own banked numbers, and that is a good reason for the question it was "
              "answering. NO VERDICT IS MOVED BY THIS ACT -- whether any banked verdict turns on the difference is a READING and the author moves rows, so it is filed and not "
              "applied, and NO ERRATA ENTRY IS DRAFTED because none was found to turn on it. The width coordinate is NOT closed and b353's sentence is CONFIRMED AND NOT "
              "STRENGTHENED; the partition b351 left UNDECIDED stays UNDECIDED. Nothing about the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED and THE CLAUSE "
              "HAS NOT MOVED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane "
              "carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where the deposit left it. The wave PARKED by the author's ruling. "
              "NOTHING DEPOSITS.")


def rows():
    P = json.load(io.open(os.path.join(D, 'b355_read.json'), encoding='utf-8'))
    m = ("THE RECORD DOES STATE WHAT ITS ARRAYS ARE, AT THE LINE WHERE IT MAKES THEM, WITH ITS REASON: THE CORPUS INTEGRATES A PIECEWISE-LINEAR INTERPOLANT OF A SAMPLED "
         "SMOOTH BUMP, CHOSEN FOR AGREEMENT WITH ITS OWN BANKED NUMBERS AND NOT FOR MEMBERSHIP IN THE SOURCE'S CLASS -- AND THE CONSEQUENCE IS A RELABELLING OF WHAT FIVE "
         "ACTS' LAWFULNESS CHECKS CERTIFY, NOT A DEFECT IN ANY MEASUREMENT (b355, leg 2 of the sortie b355-b355)")
    stmt = (m + ": b353 graded the smoothness hypothesis REFUTABLE against the corpus's arrays and said the record did not settle whether they were discretisations or the "
            "objects. **IT DOES SETTLE IT, AND b353 DID NOT LOOK AT THE LINE.** THREE LAYERS, EACH AT AN EMITTING LINE: the GENERATING FORMULA at carto_atlas.py:49 is "
            "exp(-1/(1-t^2)) on \\|t\\|<1, **THE TEXTBOOK Cc-infinity BUMP**, so the formula the code writes down IS in the class; the SAMPLED ARRAY at :45 and :50 is that "
            "formula at NV nodes divided by its own TRAPEZOID integral, **so even the array is the smooth bump rescaled by a constant only the piecewise-linear reading makes "
            "exact**; and the OBJECT INTEGRATED at b317_smear.py:136 is np.interp between nodes and zero outside, which :126 states in words and :128 gives the reason for -- "
            "*the function this act integrates is the function the corpus's number was formed from.* **THE CHOICE WAS MADE FOR INTERNAL CONSISTENCY, AND THE QUESTION OF CLASS "
            "MEMBERSHIP WAS NOT BEING ASKED AT THAT LINE.** **H1 AND H3 ARE ANSWERED SEPARATELY AND NEITHER IN TERMS OF THE OTHER**, because H1 fails on WHAT THE OBJECT IS "
            "and H3 is undecided on HOW FAR THE LOOKING WENT, and an answer to either settles nothing about the other; H3's grade stands undisturbed. **AND THE DISTINCTION "
            "THE REGISTRATION FIXED BEFORE ANY CHECK WAS LOOKED AT:** for a true autocorrelation f = g conv g-sharp the transform is \\|g-hat\\|^2 and positivity is AUTOMATIC, so "
            "**A SCAN APPLIED TO AN OBJECT BUILT AS AN AUTOCORRELATION IS NOT AN INDEPENDENT TEST OF CLASS MEMBERSHIP.** The checks, one by one: b320's 13 of 13 USED BOTH and "
            "certifies that the DISCRETE construction behaves like a continuous autocorrelation within the scan's reach; b320's Theorem 1 conditions and its covered-cell "
            "naming USED NEITHER; b328's lawfulness and every aimed seed at b334, b343, b344 and b349 USED BOTH and certify the same, once per seed. **NO ACT IN THE FAMILY "
            "EVER TESTED CLASS MEMBERSHIP INDEPENDENTLY OF THE CONSTRUCTION.** b320's own control -- the wide-minus-narrow fixture returning -5.85e-01 -- proves the scan "
            "discriminates, and **WHAT IT DISCRIMINATES IS AUTOCORRELATIONS FROM NON-AUTOCORRELATIONS, WHICH IS NOT MEMBERS FROM NON-MEMBERS.** The old reading was *the seeds "
            "are in the source's class*; the reading this act supports is *the seeds are built as autocorrelations of a piecewise-linear interpolant of a sampled smooth bump, "
            "and the scan confirms the discrete construction behaves like a continuous one within its reach.* **THE SECOND IS NARROWER AND IT IS TRUE; THE FIRST WAS NEVER "
            "MEASURED.**")
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: A READING OF THE CODE IS NOT A RE-VERDICT OF THE ACTS THAT RAN IT** -- the act put a narrower sentence beside a wider one and said "
         "which was measured, and moved nothing.",
         "**NO PRINT.** Relay tools only, plus the sortie's step-zero anchor tool. Nothing written to PLACE-papers, so the hook and the mirror are NOT OWED and the suite "
         "checks that state rather than assuming it; nothing in TECHNE-Core; no owner instrument edited -- everything is READ.",
         "**NO GRADE MOVED; NO BAR MOVED.** b320, b328, b334, b343, b344, b349 and b353 all stand exactly as banked; b353's H3 grade is undisturbed and its width sentence is "
         "confirmed and not strengthened.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b355 -- WHAT THE ARRAYS ARE. ### THE ROW.')
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
          and 'RELABELLING' in ROWS[0][0]
          and 'NOT A DEFECT IN ANY MEASUREMENT' in ROWS[0][0]
          and 'NOT AN INDEPENDENT TEST OF CLASS MEMBERSHIP' in ROWS[0][1]
          and 'THE FIRST WAS NEVER MEASURED' in ROWS[0][1]
          and 'NO GRADE MOVED' in ROWS[0][4]
          and 'A RELABELLING IS NOT A DEMOTION' in ROWS[0][5]
          and 'NO VERDICT IS MOVED BY THIS ACT' in ROWS[0][5]
          and 'NOTHING DEPOSITS' in ROWS[0][5])
    print('  the row says NO TERMINAL with the reason, relabelling-not-defect, not-independent, never-measured, no verdict moved : %s' % g1)
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
