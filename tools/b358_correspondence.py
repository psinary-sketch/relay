# -*- coding: utf-8 -*-
"""b358_correspondence.py -- TWO ROWS: THE ACT'S OWN, AND RULING (R1)'S APPEND-ONLY CORRECTION.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every count and
### every hash is read from the act's own records, never typed.
### ### **ROW 1 -- THE ACT.** ### THE HAZARD: a row that reads as if the literature had been searched
### exhaustively, as if a located statement had been applied, as if the tail had been closed, or as if
### `EXISTS BUT CIRCULAR` were a discovery rather than a pinning of what the sources say themselves.
### ### **ROW 2 -- RULING (R1).** ### *"The mis-attributing correspondence row is corrected by an
### APPEND-ONLY correction row citing the bank and the index key; the row itself is not edited."* ### THE
### HAZARD: a correction row that reads as if b356 were re-verdicted, or as if a figure had moved. ### **ONE
### WORD IN ONE CELL OF ONE ROW IS WRONG AND EVERYTHING ELSE IN THAT ROW IS RIGHT.**
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

SCOPE_ACT = ("**SCOPE: FIVE ADDRESSES, FOUR FETCHED, AND ONE OF THOSE A DUPLICATE SURFACE.** A statement this act did not look for is NOT COUNTED HERE, and the hints that found "
             "nothing in Coffey may say more about the hints than about Coffey -- an absence of READING is not an absence of LITERATURE, which is the sentence the record's four "
             "incidents earned. NOT A DISCOVERY ABOUT THE LITERATURE: that the Li asymptotic is conditional on RH is written in both sources' own abstracts, and what is new is only "
             "that the record now holds it pinned with the split located at the line. NOT THAT NO UNCONDITIONAL TAIL BOUND EXISTS AND NOT THAT NONE COULD. NOT THAT THE FIVE "
             "UNDECIDABLE GRADES ARE PERMANENT -- H-NGEK is undecidable only because this act's own cap forbade one evaluation, and that evaluation is NAMED AND NOT ORDERED. A "
             "LOCATED STATEMENT IS NOT AN APPLIED ONE, and this act applies none. NO COORDINATE IS CLOSED; THE PARTITION STAYS UNDECIDED; the two faces' equivalence is not compiled. "
             "Nothing about the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED and THE CLAUSE HAS NOT MOVED. NO AGGREGATION IS STATED; M-2 REMAINS "
             "(SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's "
             "record. h2 stands exactly where the deposit left it. The wave PARKED by the author's ruling. NOTHING DEPOSITS.")

SCOPE_R1 = ("**SCOPE: ONE WORD IN ONE CELL, AND EVERYTHING ELSE IN ROW 204 IS RIGHT.** NOT A RE-VERDICT OF b356: its verdict THE BOUNDARY, its figures, its control and its refusals "
            "all stand exactly as banked. NO NUMBER IS AFFECTED. NO GRADE MOVES. NO BAR MOVES. ROW 204 IS NOT EDITED and not one byte of it changes -- the ruling directs a correction "
            "row and this is that row. NOT A CLAIM THAT THE RECORD IS NOW FREE OF TYPED ACT NUMBERS: this one was found by reading the table's tail to number the next row, which is "
            "not a search, and the guard that would find them mechanically is NAMED AND NOT BUILT. Nothing about the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED "
            "and THE CLAUSE HAS NOT MOVED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated. The patent lane carried on "
            "the patent seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where the deposit left it. The wave PARKED. NOTHING DEPOSITS.")


def rows():
    R = json.load(io.open(os.path.join(D, 'b358_read.json'), encoding='utf-8'))
    L = json.load(io.open(os.path.join(D, 'b358_locate.json'), encoding='utf-8'))
    E = json.load(io.open(os.path.join(D, 'b358_reads.json'), encoding='utf-8'))
    S = {s['tag']: s for s in L['sources']}
    nloc = len(R['statements'])
    nsh = len(R['shapes'])
    ncirc = len(R['circular'])
    hyp = R['hypotheses']
    nundec = R['n_undecidable_axis2']

    m1 = ("THE LITERATURE DOES CARRY AN ASYMPTOTIC THAT WOULD CLOSE THE LI FACE'S TAIL, AND IT IS CIRCULAR IN ITS OWN SOURCE'S OWN ABSTRACT: OF %d STATEMENTS LOCATED AND PINNED, "
          "%d MEETS ALL FOUR CONDITIONS LOCKED BEFORE ANY SOURCE WAS OPENED AND IT FIRES AT ALL THREE CIRCULARITY QUESTIONS -- SO THE TAIL IS CLOSED ONLY UNDER THE THING BEING "
          "PROVED (b358)" % (nloc, nsh))
    s1 = (m1 + ": the deposit's finite range is its own sentence, *\"partialPositivity_finiteRange (v0.8.0) certifies lambda_n >= 0 for n up to Voros's detection threshold "
          "N_0(T) approx 2T^2 ... a certificate reaching exactly to where discrimination would begin, and no further; it is not RH\"*, and this act asked what would close the "
          "rest. **THE ONE SHAPE IS VOROS'S (17)**, and its condition is in his abstract: *\"For n -> infinity we obtain that if (and only if) the Hypothesis is true, lambda_n ~ "
          "n(A log n + B)\"*, with the derivation opening *\"all the zeros lie on the critical line, first transform the summation (1) into a Stieltjes integral\"*. **AND THE "
          "SPLIT IS EXACT, WHICH IS SHARPER THAN SAYING THE ASYMPTOTIC ASSUMES RH:** on the decomposition the record already holds (b327), the ARCHIMEDEAN channel has an "
          "unconditional asymptotic with an explicit error term from BOTH sources independently -- Voros's *\"unconditionally. (24)\"* to all orders, and Lagarias's Theorem 5.1 "
          "with an ABSOLUTE implied constant and an explicit index `n >= K(pi)` -- while the ZERO channel has **no unconditional bound at all**, Theorem 6.1 reducing it "
          "unconditionally and bounding it only at *\"If the Riemann hypothesis holds for L(s,pi) then ...\"*. **SO THE ONE PART THAT WOULD CLOSE THE TAIL IS THE PART THE "
          "HYPOTHESIS CONTROLS.** %d of %d located statements are circular and %d are not, and **NOT ONE OF THE THREE NON-CIRCULAR ONES IS A SHAPE**: everything about lambda_n "
          "itself is conditional and everything unconditional is about a part. Bombieri-Lagarias Cor 1(c), quoted inside Voros (*\"rather weak exponential lower bounds lambda_n "
          ">= -c e^(eps n) were shown to imply RH\"*), is the one statement running in the useful direction and it still demands the bound FOR EVERY n. **THE HYPOTHESES ARE GRADED "
          "TWICE AND NEVER MERGED:** on the sources' own objects %d of %d are MET; on the corpus's, %d are MET and **%d are UNDECIDABLE-FROM-THE-RECORD** -- three of them the open "
          "clause under three names, one Bombieri-Lagarias's demand over all n, and one, H-NGEK, undecidable **only because this act's cap forbade one evaluation**, which is named "
          "and not ordered. **THE PRICING, AND IT IS THE FINDING NOT A MISSING NUMBER: THERE IS NO INDEX BEYOND WHICH THE LOCATED SHAPE WOULD ACT**, because it acts only on the "
          "branch its own condition selects; the two banked figures that bracket the size of the demand are n = 300 computed and n approx 1e18 before a violating zero could "
          "register, ONE LABELLED DIVISION giving %.2e, **a distance in index and not a price in wall time.** Sources pinned by sha-256 of the bytes fetched: Voros math/0506326 "
          "`%s`, %d bytes; **Lagarias math/0404394v4 `%s`, %d bytes -- WHICH IS THE RECORD'S OWN b327 PIN, RE-VERIFIED BYTE FOR BYTE**; Coffey math-ph/0505052 `%s` searched and not "
          "quoted. Bombieri-Lagarias 1999 **NOT FETCHED** (HTTP 404), which the faces ledger already recorded as *\"not obtainable by this seat\"*, so its corollary is used at one "
          "remove and said to be. %d reads, %d located on the first run, **%d of %d anchors differing from the hint that found them.**"
          % (ncirc, nloc, nloc - ncirc,
             sum(1 for h in hyp.values() if h['axis1'] == 'MET'), len(hyp),
             sum(1 for h in hyp.values() if h['axis2'] == 'MET'), nundec,
             R['price_ratio'],
             S['S1']['sha256'][:16] + '...', S['S1']['bytes'],
             S['S2']['sha256'][:16] + '...', S['S2']['bytes'],
             S['S3']['sha256'][:16] + '...',
             E['reads'], E['reads'] - E['without_anchor'], E['anchors_differing'], E['reads']))

    m2 = ("A CORRECTION ROW, BY THE AUTHOR'S RULING (R1): ROW 204 SAYS b356 WHERE IT MEANS b354, AND ROW 204 IS NOT EDITED (b358)")
    s2 = (m2 + ": row 204's marker cell reads *\"THE RANK IS NO LONGER AT ITS BOUND -- SO b356'S SIXTH RUNG WAS THE INSTRUMENT'S EDGE\"*. **IT SHOULD READ b354.** b354 ran the sixth "
          "rung at NY = 512 and THAT rung was the instrument's edge; b356 ran it again with the axis raised and is the act that LOCATED the edge, its own frame clearing the bound "
          "with 506 dimensions to spare. **THE BANK AND THE INDEX KEY BOTH READ CORRECTLY**, and this row cites them as the ruling directs: relay `data/b356_the_boundary.txt` says "
          "*\"SO b354's SIXTH RUNG WAS THE INSTRUMENT'S EDGE\"*, and the index key `object-or-boundary` says *\"SO b354'S SIXTH RUNG WAS THE INSTRUMENT'S EDGE, AND THE FIVE-FRAME "
          "PICTURE STANDS WITH ITS EDGE NOW LOCATED AT X = 256 WITH NY = 512\"*. **AND THE REST OF ROW 204 IS RIGHT AND SAYS SO TWO SENTENCES LATER**: *\"b354 found the residual "
          "negative and the rank saturated at the quadrature bound IN THE SAME STEP and separated them nowhere, saying so.\"* **WHERE IT CAME FROM:** the marker is a literal typed "
          "in `tools/b356_correspondence.py`, where every FIGURE is read from `data/b356_raised.json` and every ACT NUMBER is typed -- so G-NUMBERS, which recomputes figures, had "
          "nothing to fire on. Found 2026-09-07 by reading the table's tail to number the next row; declared and routed at relay `data/b357_routed_correspondence_204.txt` and ruled "
          "on by the author in the b358 ferry. **A GUARD THAT EXTRACTS EVERY bNNN TOKEN FROM A ROW AND REQUIRES EACH TO APPEAR IN ITS ACT'S OWN BANK IS NAMED AND NOT BUILT**, and it "
          "belongs beside the anchored-arm work-order: both are the same defect, **A STRING TYPED WHERE IT COULD HAVE BEEN READ.**")

    return [
        (m1, s1,
         "**NO TERMINAL, AND THE REASON: A STATEMENT LOCATED IS NOT A STATEMENT APPLIED** -- no argument was constructed, no bound proved, no source's theorem extended, sharpened or "
         "combined with another, and the shape that exists does not survive the check that was locked before any source was opened.",
         "**PRINT: PLACE-papers.** FACES_LEDGER.md gains an UPDATE BLOCK on row U1 through the writer's `append_block` (the row itself is never rewritten; the grade stays NAMED-ONLY "
         "because a shape that does not survive establishes nothing), and ERRATA.md gains E-2026-09-07-1 by ruling R2. **SO THE HOOK AND THE MIRROR ARE OWED AND THE SUITE CHECKS "
         "THEM.** Relay tools and data otherwise; nothing in TECHNE-Core; **NO OWNER INSTRUMENT EDITED** -- reg_seal.py and ferry_scan.py gain ADDITIVE modes under ruling R3 and "
         "every registration sealed before this act still verifies, checked on five of them.",
         "**NO GRADE MOVED; NO BAR MOVED; NO ACT RE-VERDICTED.** b327's pin is not merely undisturbed but RE-VERIFIED; b340, b341, b345, b351, b353, b355, b356 and b357 stand as "
         "banked. **AND ONE EXPECTATION WAS SCORED AGAINST ITS OWNER:** this seat predicted the circularity would sit in the error term rather than the main term, and it sits in "
         "the abstract, the condition and the first line of the derivation. The navigator's named risk is the one that fired.",
         SCOPE_ACT, "current"),
        (m2, s2,
         "**NO TERMINAL, AND THE REASON: A TYPED ACT NUMBER IN A MARKER IS A SLIP IN A ROW, NOT A CLAIM THE RECORD MADE** -- and the author rules on whether it is more than that.",
         "**PRINT: none by this row.** It is appended to CORRESPONDENCE.md beside the act's own row; **ROW 204 IS NOT TOUCHED** and the table is a true prefix of its own blob above "
         "this act's two rows.",
         "**NO GRADE MOVED; NO BAR MOVED; NO NUMBER AFFECTED; b356 IS NOT RE-VERDICTED.** Its verdict THE BOUNDARY, its control, its rank of 518 against 1024 and its refusals all "
         "stand exactly as banked.",
         SCOPE_R1, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b358 -- TWO ROWS: THE ACT, AND RULING (R1)\'S APPEND-ONLY CORRECTION.')
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
          and 'CIRCULAR IN ITS OWN SOURCE' in ROWS[0][0]
          and 'THE SPLIT IS EXACT' in ROWS[0][1]
          and 'RE-VERIFIED BYTE FOR BYTE' in ROWS[0][1]
          and 'NOT FETCHED' in ROWS[0][1]
          and 'GRADED TWICE AND NEVER MERGED' in ROWS[0][1]
          and 'THE HOOK AND THE MIRROR ARE OWED' in ROWS[0][3]
          and 'NOT A DISCOVERY ABOUT THE LITERATURE' in ROWS[0][5]
          and 'ROW 204 IS NOT EDITED' in ROWS[1][0]
          and 'IT SHOULD READ b354' in ROWS[1][1]
          and 'NAMED AND NOT BUILT' in ROWS[1][1]
          and 'IS NOT RE-VERDICTED' in ROWS[1][4]
          and all('NOTHING DEPOSITS' in r[5] for r in ROWS))
    print('  the rows say NO TERMINAL with reasons, the split, the re-verified pin, the unfetched source, two axes, hook owed, R1 not editing 204 : %s' % g1)
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
    print('  last existing row : %d ; rows to append : %d and %d' % (max(nums), start, start + 1))
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
    cells = [G.split_cells(t) for t in back.rstrip(chr(10)).split(chr(10))[-2:]]
    ok = (got[-1] == start + 1 and all(m in back for m, _s, _t, _p, _g, _sc, _st in ROWS)
          and C.blank_cells(back) == 0
          and all(len(c) == 6 and all(x.strip() for x in c) for c in cells)
          and back.startswith(txt.rstrip(chr(10))))
    print('  READ BACK         : last row number is %d ; cells on disk %s (6 required, none blank)' % (got[-1], [len(c) for c in cells]))
    print('  ### **ROW 204 IS UNTOUCHED AND THE TABLE IS A TRUE PREFIX OF ITSELF ABOVE THESE TWO ROWS** : %s'
          % back.startswith(txt.rstrip(chr(10))))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
