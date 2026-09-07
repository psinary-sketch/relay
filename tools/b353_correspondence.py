# -*- coding: utf-8 -*-
"""b353_correspondence.py -- ONE ROW: THE WIDTH COORDINATE'S MISSING STATEMENT.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every figure is read
### from the act's own records, never typed. ### **THE HAZARD:** a row that reads as if a located statement were
### a proved one, as if a checked hypothesis were a discharged obligation, as if the width coordinate had been
### closed, or as if an absence of reading were an absence of literature.
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

SCOPE_TAIL = ("**SCOPE: A LOCATED STATEMENT IS NOT A PROVED ONE, AND A CHECKED HYPOTHESIS IS NOT A DISCHARGED OBLIGATION.** This act quotes; it verifies no proof and is "
              "forbidden to. THE WIDTH COORDINATE IS NOT CLOSED BY IT, no class is proved or spanned, and the partition b351 left UNDECIDED stays UNDECIDED. H1 being "
              "REFUTABLE against the corpus's arrays is not a finding that the corpus's results are wrong -- it is a finding that the record does not say what its arrays are "
              "meant to be, and that question is routed and not answered here. THE SEARCH IS NOT A SURVEY: one source was read at content, and the absence of a crossing "
              "statement is AN ABSENCE OF READING AND NOT AN ABSENCE OF LITERATURE. Nothing about the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED and THE "
              "CLAUSE HAS NOT MOVED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent "
              "lane carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where the deposit left it. The wave PARKED by the author's "
              "ruling. NOTHING DEPOSITS.")


def rows():
    P = json.load(io.open(os.path.join(D, 'b353_read.json'), encoding='utf-8'))
    src = P['source']
    H = P['hypotheses']
    grid = '; '.join('%s %s / %s' % (h['id'], h['source'], h['corpus']) for h in H)
    m = ("THE LITERATURE DOES CARRY A STATEMENT OF THE SHAPE THE WIDTH COORDINATE WOULD NEED, AND IT IS IN THE CORPUS'S OWN SOURCE, AND IT DOES NOT CLOSE THE COORDINATE: "
         "BOAS-KAC IS AN EXHAUSTION AT EVERY WIDTH, AND AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS (b353, leg 2 of the sortie b352-b353)")
    stmt = (m + ": **A LOCATED STATEMENT IS NOT A PROVED ONE.** THE SOURCE, PINNED: arXiv %s, Connes-Consani, *Weil positivity and Trace formula, the archimedean place*, "
            "sha256 %s, %d bytes, graded %s under the import bar. **ITS PROPOSITION 2, BOAS-KAC:** for f in Cc^infty(R) supported in [-A, A], the Fourier transform being "
            "pointwise positive is EQUIVALENT to f = g * g^* for some g supported in [-A/2, A/2]. **THAT IS STRONGER THAN THE DENSITY STATEMENT THE ORDER ASKED FOR -- it does "
            "not approximate the admissible class by a subfamily, IT EXHAUSTS IT** -- so positivity of the Weil functional on the seed family at half-width carries to the "
            "whole admissible class at full width, with no limit argument and no topology. **AND EVERY CONCLUSION IT GIVES IS AT THE SAME A IT WAS GIVEN**, while the "
            "criterion it serves quantifies over the union of all supports (the source's own line: RH iff sum_v W_v of g conv gbar-sharp is at most zero for ALL g in "
            "Cc^infty(R+*) with the vanishing conditions). **SO THE STRONGEST KIND OF STATEMENT STILL CLOSES NOTHING WHEN IT IS INDEXED BY THE VERY COORDINATE IN QUESTION.** "
            "THE HYPOTHESES, GRADED TWICE AND NEVER MERGED -- against the source's class, then against the corpus's constructed objects: %s. **H1 IS REFUTABLE AGAINST THE "
            "ARRAYS IN THE RECORD'S OWN WORDS** -- f = autocorrelation(seed) is PIECEWISE LINEAR, which is not C^infty and not even C^1 -- though whether the record intends "
            "its arrays as discretisations of smooth functions or as the objects themselves IS A QUESTION THE RECORD DOES NOT SETTLE. **H3 IS UNDECIDABLE FROM THE RECORD AND "
            "THE CORPUS'S OWN TOOL SAYS WHY:** the positive-definiteness test is a scan and *cannot prove one IS beyond the interval scanned*, where the hypothesis is "
            "pointwise. **H4 IS MET ONLY TO A MEASURED TOLERANCE**, at 1e-16 and 1e-17, where the source's conditions are exact. THE MISSING STATEMENT, TYPED: *there is a "
            "bound on the Weil functional over the admissible class at support A that is UNIFORM IN A -- or an argument that non-negativity at every finite A implies it on "
            "the union over all A.* **AND THE SECOND HALF IS NOT AUTOMATIC:** an increasing union carries non-negativity only if the functional is the same functional on each "
            "member, and b334 measured the square and the remainder NOT REACHED at the reaching widths. **SO IT IS A STATEMENT ABOUT AN INSTRUMENT THAT DOES NOT REACH, AND IT "
            "IS UNPRICEABLE FROM BANKED FIGURES** -- no rung, box, cell, frame or aim would scale to it, because the work it names is A PROOF AND NOT A RUN -- **and pricing "
            "the pricing is unpriceable too.** NOT ATTEMPTED. Filed beside it, the phase coordinate's vanishing-transform class as a COVERAGE CLASS and not a failure class, "
            "with b349's own words: *three lawful seeds mean these three did not.*"
            % (src['arxiv'], src['sha256'], src['bytes'], src['grade'], grid))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: A READ THAT GRADES HYPOTHESES SETTLES NOTHING ABOUT THE OBJECT** -- the statement is located and pinned, not proved, and the "
         "coordinate it was read for is exactly the coordinate it leaves open.",
         "**NO PRINT.** Relay tools only. Nothing written to PLACE-papers, so the hook and the mirror are NOT OWED and the suite checks that state rather than assuming it; "
         "nothing in TECHNE-Core; no owner instrument edited; one external source fetched, hashed and pinned, and held in no repository.",
         "**NO GRADE MOVED; NO BAR MOVED.** b349, b351 and b352 stand exactly as banked, and nothing here confers anything about any coordinate.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b353 -- THE WIDTH COORDINATE'S MISSING STATEMENT. ### THE ROW.")
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
          and 'A LOCATED STATEMENT IS NOT A PROVED ONE' in ROWS[0][1]
          and 'NOT AN EXHAUSTION ACROSS WIDTHS' in ROWS[0][0]
          and 'NO GRADE MOVED' in ROWS[0][4]
          and 'UNPRICEABLE FROM BANKED FIGURES' in ROWS[0][1]
          and 'COVERAGE CLASS' in ROWS[0][1]
          and 'ABSENCE OF READING AND NOT AN ABSENCE OF LITERATURE' in ROWS[0][5]
          and 'NOTHING DEPOSITS' in ROWS[0][5])
    print('  the row says NO TERMINAL with the reason, located-not-proved, not across widths, unpriceable, coverage class, absence of reading : %s' % g1)
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
