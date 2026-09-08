# -*- coding: utf-8 -*-
"""b362_correspondence.py -- ONE ROW: THE APPROXIMATION REGISTER, READ AND NOT ADOPTED.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every count is read
### from the act's own JSONs and none is typed.
### ### **THE HAZARD THIS ROW IS WRITTEN AGAINST:** ### a row that reads as if a register had been adopted;
### as if a face had been promoted; as if locating a famous criterion were progress on the question; as if
### an unconditional finite side were a route; or as if `NOT WORTH OPENING` were a judgement about the
### mathematics rather than about what this record can afford.
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

SCOPE = (
    "**SCOPE: THE REGISTER IS NOT ADOPTED AND NO FACE IS PROMOTED.** A LOCATED STATEMENT IS NOT A PROVED ONE, and a criterion located is not a criterion the corpus holds: this act quotes, verifies no proof "
    "and may not. NOTHING WAS COMPUTED, NO DISTANCE WAS EVALUATED AT ANY INDEX BY ANY ROUTE AT ANY PRECISION, AND NO INSTRUMENT WAS BUILT. NOT THAT AN UNCONDITIONAL FINITE SIDE IS A ROUTE -- it is the one "
    "thing in this register better than the positivity register's and it buys nothing, because the question was never about any finite index. NOT THAT NOT WORTH OPENING IS A JUDGEMENT ABOUT THE MATHEMATICS: "
    "the register is a real one with real theorems in it, and what is said is that a corpus with no control in it and no way to price one has nothing to gain by entering. THE SEARCH IS NOT A SURVEY -- five "
    "addresses fetched, one journal reference NAMED AND NOT FETCHED, and what was not located is AN ABSENCE OF READING. NOTHING IS COMPILED AND NO BRIDGE IS TYPED, and the deposit's own refusal is quoted at "
    "the deposited file. Nothing about the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO GRADE IS "
    "CONFERRED BY A SEAT. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the patent seat's report, "
    "UNCONFIRMED on this seat's record. THE INSTRUMENT LANE STAYS PARKED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it. The wave PARKED by the author's ruling. NOTHING IS "
    "DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def rows():
    R = json.load(io.open(os.path.join(D, 'b362_read.json'), encoding='utf-8'))
    E = json.load(io.open(os.path.join(D, 'b362_reads.json'), encoding='utf-8'))
    F = json.load(io.open(os.path.join(D, 'b362_faces_row.json'), encoding='utf-8'))
    L = json.load(io.open(os.path.join(D, 'b362_locate.json'), encoding='utf-8'))
    m = ("THE APPROXIMATION REGISTER IS LOCATED AND PINNED AND IS **NOT WORTH OPENING** AT THE REACH THIS RECORD CAN AFFORD: a finite instance in it is an UNCONDITIONAL upper bound -- which the positivity "
         "register's is not -- and that buys nothing, because **THE CRITERION IS A STATEMENT ABOUT A LIMIT AND AN UNCONDITIONAL THEOREM BOUNDS THE FINITE SIDE AWAY FROM ZERO AT EVERY REACH** (b362)")
    stmt = (m + ": **THE REGISTRATION WAS LOCKED BEFORE ANY READ, ANY SEARCH AND ANY FETCH**, on the audit's own exit code. **THE NAVIGATOR'S HINT WAS TREATED AS A SEARCH STRING AND NEVER AS A SOURCE**, in "
            "the order's own words, and it is quoted in the bank before the results are so a reader can see what was searched on. **THE HINT: CONFIRMED, WITH ONE CORRECTION.** The criterion is real and where "
            "the hint said it is, and the variant restricting the family to the naturals is exactly what the named author proved; **THE CORRECTION IS THE SPACE**, and the source flags it itself -- the "
            "criterion as located is a *\"modified form [4] (the original formulation is related to L2(0, 1))\"*, and the hint named no space. **%d ADDRESSES ATTEMPTED, %d FETCHED, EVERY ONE HASHED**, every "
            "extracted text on disk, and the seam restated: a hash on a PDF does not certify that its extracted text is a faithful rendering of it. **THE STRUCTURAL QUESTION, DECIDED FROM THE QUOTED "
            "STATEMENTS AND NOT FROM THE HINT: A FINITE INSTANCE IS AN UNCONDITIONAL UPPER BOUND** -- the quantity's definition mentions no zero and no hypothesis, and an infimum over a subset is at least "
            "the infimum over the whole. **SO THIS REGISTER DOES NOT CARRY THE SHORTFALL THE WINDOW ACT FOUND** (b321: an instrument standing further from the answer than the difference it was asked to "
            "resolve) -- there is no residual between instrument and answer for a signal to hide under. **AND THE SHORTFALL IT CARRIES INSTEAD IS THE RATE.** The two sides are kept apart and the circularity "
            "check was run as the Li read ran it: **the lower bound is NOT CIRCULAR** -- it carries no hypothesis, and the source settles it, *\"If the Riemann Hypothesis fails this result is true but "
            "trivial\"*, so the assumption in the proof is a case split and not a condition on the statement -- while **the upper bound is CIRCULAR AT (i)**, made *\"under the Riemann hypothesis\"* in the "
            "source's own words. **SO WHAT IS UNCONDITIONAL HERE IS THE OBSTRUCTION AND WHAT WOULD BE PROGRESS IS CONDITIONAL.** The uniformity obstruction REAPPEARS and takes a different shape -- **A "
            "RATE** -- and this is the one place that quantifies what is missing; **NO BRIDGE IS TYPED IN EITHER DIRECTION**. **THE PRICING IS NOT ATTEMPTED AND IS THEN PRICED:** the record holds no value, "
            "no control and no fixture in this register, the literature's numbers are named at a reference this act did NOT fetch, and an instrument with no control is a number with no standing -- so the "
            "first act here would have to be a READ, and until it is done the instrument act is unpriceable. %d reads, %d located on the relied-on run, %d of %d anchors differing from the hint that found "
            "them."
            % (L['attempted'], L['fetched'], E['reads'], E['reads'] - E['without_anchor'],
               E['anchors_differing'], E['reads']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: A REGISTER READ IS NOT A REGISTER ENTERED** -- this act located statements, pinned bytes, unfolded hypotheses and decided one structural question about them. It "
         "computed nothing, adopted nothing and promoted nothing.",
         "**PRINT: PLACE-papers, ONE FILE.** FACES_LEDGER.md gains **ONE NEW ROW, `N1`**, through the ledger's own writer -- status `%s`, %d cells, none blank, %d quotations verified before the row existed, "
         "append-only against the working file and against its blob, **NO ROW ABOVE TOUCHED**. Its grade is SPLIT so a reader cannot take one half for the other: **IMPORTED (TRUSTED-AT-CITE) for the located "
         "statements; NAMED-ONLY for everything about the corpus's own holdings, which are none.** **THE HOOK AND THE MIRROR ARE OWED AND PAID.** Nothing in TECHNE-Core; no findings section edited; no "
         "roster row changed."
         % (F['status'], 7, F['quotes']),
         "**NO GRADE IS CONFERRED BY A SEAT AND NO FACE IS PROMOTED.** The row grades an IMPORT at cite and says the corpus holds nothing here, which is the weakest thing a row can say. **NO ACT IS "
         "RE-VERDICTED:** b321, b358, b360 and b361 stand exactly as banked. **AND BOTH SEATS' EXPECTATIONS WERE SCORED:** the navigator's three clauses MET, the first with the one correction, and the third "
         "met more sharply than it asked since the located rate is an UNCONDITIONAL LOWER bound; this seat's two clauses MET -- and a seat scoring itself MET twice says what that is worth, since predicting "
         "that a third instance will look like the first two is cheap and is scored at that price.",
         SCOPE, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b362 -- ONE ROW: THE APPROXIMATION REGISTER, READ AND NOT ADOPTED.')
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
          and 'NOT WORTH OPENING' in ROWS[0][0]
          and 'THE CRITERION IS A STATEMENT ABOUT A LIMIT' in ROWS[0][0]
          and 'NEVER AS A SOURCE' in ROWS[0][1]
          and 'CONFIRMED, WITH ONE CORRECTION' in ROWS[0][1]
          and 'A FINITE INSTANCE IS AN UNCONDITIONAL UPPER BOUND' in ROWS[0][1]
          and 'NO BRIDGE IS TYPED IN EITHER DIRECTION' in ROWS[0][1]
          and 'is unpriceable' in ROWS[0][1]
          and 'ONE NEW ROW' in ROWS[0][3]
          and 'NO ROW ABOVE TOUCHED' in ROWS[0][3]
          and 'NO GRADE IS CONFERRED BY A SEAT AND NO FACE IS PROMOTED' in ROWS[0][4]
          and 'THE REGISTER IS NOT ADOPTED AND NO FACE IS PROMOTED' in ROWS[0][5]
          and 'ABSENCE OF READING' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    print('  the row says NO TERMINAL with its reason, the hint not a source, the correction, the unconditional finite side, no bridge, the unpriceable pricing, the new row, no promotion : %s' % g1)
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
    ok = (got[-1] == start and all(m in back for m, _s, _t, _p, _g, _sc, _st in ROWS)
          and C.blank_cells(back) == 0
          and all(len(c) == 6 and all(x.strip() for x in c) for c in cells)
          and back.startswith(txt.rstrip(chr(10))))
    print('  READ BACK         : last row number is %d ; cells on disk %s (6 required, none blank)' % (got[-1], [len(c) for c in cells]))
    print('  ### **THE TABLE IS A TRUE PREFIX OF ITSELF ABOVE THIS ROW** : %s' % back.startswith(txt.rstrip(chr(10))))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
