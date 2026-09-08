# -*- coding: utf-8 -*-
"""b361_correspondence.py -- ONE ROW: THE HELD ITEM, DECIDED.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every count is read
### from the act's own JSONs and none is typed.
### ### **THE HAZARD THIS ROW IS WRITTEN AGAINST:** ### a row that reads as if a tail had been closed; as
### if a circularity had been removed; as if a value the source never writes had been quoted from it; as if
### a grade had been conferred; or as if a vacuous condition were an obstruction removed.
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
    "**SCOPE: A DECIDED INDEX CONDITION IS NOT A CLOSED TAIL.** The tail is closed by the ZERO channel, which has NO UNCONDITIONAL BOUND AT ALL, and nothing here touches it. THE CIRCULARITY FINDING IS "
    "UNTOUCHED, in the order's own words: the tail bound asserts the hypothesis, and no decision here changes that. NOT THAT A VALUE IDENTIFIED IS A VALUE QUOTED -- the source writes neither the parameter "
    "nor the constant for this representation and the act says so, printing its route step by step and printing what the route is deaf to. NOT THAT H-CUSP IS DECIDED: Theorem 5.1 is stated for an "
    "irreducible cuspidal representation and the corpus's object is the one the source marks as its exception; b358 graded that question and this act stands on that grade and confers none. NOT THAT A "
    "VACUOUS CONDITION IS AN OBSTRUCTION REMOVED -- a condition that costs nothing to satisfy was never the obstruction. NO GRADE IS CONFERRED BY A SEAT; the row's grade NAMED-ONLY stands. Nothing about the "
    "quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS "
    "(SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. THE INSTRUMENT LANE STAYS "
    "PARKED AND NO FRAME WAS RECOMPUTED. THE POSTURE LOCK IS SEPARATE. h2 stands exactly where the deposit left it. The wave PARKED by the author's ruling. NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT "
    "ZENODO.")


def rows():
    R = json.load(io.open(os.path.join(D, 'b361_read.json'), encoding='utf-8'))
    E = json.load(io.open(os.path.join(D, 'b361_reads.json'), encoding='utf-8'))
    F = json.load(io.open(os.path.join(D, 'b361_faces_row.json'), encoding='utf-8'))
    m = ("THE HELD ITEM IS DECIDED AND THE CONDITION IS VACUOUS: K(pi_triv) = %d, so the index condition on the archimedean channel's absolute-constant asymptotic is satisfied at EVERY index the corpus "
         "computes and its error term collapses to a constant -- **DECIDED FROM THE SOURCE'S OWN DISPLAYED FORMULAE AND NOT FROM ANY VALUE THE SOURCE WRITES**, with the route printed and what the route is "
         "deaf to printed beside it (b361)" % R['K'])
    stmt = (m + ": **THE BRANCH WAS FIXED BY THE ORDER BEFORE THE QUOTATION WAS SEEN AND THE REGISTRATION WAS LOCKED BEFORE ANY READ** -- and the locked face declares what a lock cannot hide, that this seat "
            "had read the item's bank one act ago at b360, with three rules fixed over that: every quotation is the anchor tool's output, the branch is decided from the quoted text alone, and **RECOLLECTION "
            "IS NEVER A SOURCE FOR A VALUE**. The four objects the order named were each located at its own file: the item and its constant at b358 lines 113-114; its grade as its own act left it, MET on the "
            "source axis and UNDECIDABLE-FROM-THE-RECORD on the corpus axis, at lines 94, 97, 107 and 111; the cap clause at line 116, *\"DETERMINED IS NOT COMPUTED, the cap forbids this act from computing "
            "it\"*; and the parking claim at b360's closing line 128, **quoted as a draft's claim and not as a ruling and TESTED rather than inherited**. **BRANCH A, ON FIVE TESTS READ OFF THE ITEM'S OWN "
            "SENTENCE:** no frame, no ladder, no quadrature axis, no transform or quadrature or fit or series, no new measurement -- and it is a bounded evaluation of a NAMED constant. **BAR 2 MET:** the "
            "definition is located at content in the source b358 pinned and quoted -- (2.1), (2.2), (2.3), (5.3) and the same definition restated inside the proof. **THE ROUTE:** N = 1; the source states its "
            "own completed L-function for the trivial representation and states its conductor, *\"using Q(pitriv) = 1.\"*; so the archimedean factor is Gamma_R(s), and (2.2) at N = 1 makes it Gamma_R(s + "
            "kappa_1), which forces kappa_1 = 0 as meromorphic functions; then (5.3) gives K = 0, **the one piece of arithmetic in the act**. **AND THE THING NO SEAT WROTE DOWN:** the source's own "
            "introduction already gives the same asymptotic *\"that for all n >= 1,\"* at (1.12) -- but there *\"the implied constant in the O(1) term depends on pi\"*, while Theorem 5.1's is ABSOLUTE. **THE "
            "INDEX CONDITION WAS ALWAYS THE PRICE OF THE ABSOLUTE CONSTANT, AND NOBODY HAD PUT THE TWO STATEMENTS SIDE BY SIDE, INCLUDING b358**, which quoted (5.1) and not (1.12). %d reads, %d located on "
            "the first run, %d of %d anchors differing from the hint that found them; the rendering pinned at sha256 `%s`, %d bytes, beside b358's pin on the PDF."
            % (E['reads'], E['reads'] - E['without_anchor'], E['anchors_differing'], E['reads'],
               E['source_sha256'][:16] + '...', E['source_bytes']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: AN INDEX CONDITION DECIDED IS NOT A BOUND PROVED** -- this act located a definition, identified a parameter from two of the source's own formulae, and squared a zero. "
         "It constructed no argument, extended no theorem and evaluated no channel.",
         "**PRINT: PLACE-papers, ONE FILE.** FACES_LEDGER.md gains an UPDATE BLOCK on row U1 through the ledger's own writer `append_block` -- **WRITTEN ONLY BECAUSE THE DECISION MOVED THE ROW**, which was "
         "the order's own condition: the row said the bound holds for n >= K(pi), and the record now holds that the condition is VACUOUS for the corpus's object and the error term is a constant. Status "
         "`%s`, %d quotations located before the block existed, append-only against the working file and against its blob, **NO ROW ABOVE EDITED**. **THE HOOK AND THE MIRROR ARE OWED AND PAID**, and the "
         "rebuild EXERCISES THE ROSTER SLOT b360 ADDED -- the first faces update ever to reach the archive. Nothing in TECHNE-Core; no findings section edited; no roster row changed."
         % (F['status'], F['quotes']),
         "**NO GRADE MOVED IN THE LEDGER AND NO GRADE IS CONFERRED BY A SEAT: `NAMED-ONLY` STANDS**, because a vacuous index condition establishes nothing that could lift a naming. **NO ACT IS RE-VERDICTED** "
         "-- an act performing a step a capped act declined is a NEW MEASUREMENT AND NOT A CORRECTION (b345's precedent), and b358's sentence that the corpus has the gamma factor determining the parameters "
         "is true as written; this act adds only that the SOURCE states its own, so the corpus's is not needed and the route through it would have been longer and less safe. **AND BOTH SEATS' EXPECTATIONS "
         "WERE SCORED:** the navigator's first clause MET and its second REFUTED BY A QUOTATION -- the row moved; this seat's first clause MET and its second MET-THEN-CORRECTED, since it predicted the longer "
         "route because its own draft had pointed at it.",
         SCOPE, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b361 -- ONE ROW: THE HELD ITEM, DECIDED.')
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
          and 'THE HELD ITEM IS DECIDED AND THE CONDITION IS VACUOUS' in ROWS[0][0]
          and 'RECOLLECTION IS NEVER A SOURCE FOR A VALUE' in ROWS[0][1]
          and 'TESTED rather than inherited' in ROWS[0][1]
          and 'BAR 2 MET' in ROWS[0][1]
          and 'NOBODY HAD PUT THE TWO STATEMENTS SIDE BY SIDE' in ROWS[0][1]
          and 'WRITTEN ONLY BECAUSE THE DECISION MOVED THE ROW' in ROWS[0][3]
          and 'EXERCISES THE ROSTER SLOT' in ROWS[0][3]
          and 'NO GRADE IS CONFERRED BY A SEAT' in ROWS[0][4]
          and 'NEW MEASUREMENT AND NOT A CORRECTION' in ROWS[0][4]
          and 'A DECIDED INDEX CONDITION IS NOT A CLOSED TAIL' in ROWS[0][5]
          and 'THE CIRCULARITY FINDING IS UNTOUCHED' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    print('  the row says NO TERMINAL with its reason, the lock rule, the draft tested, bar 2, the pair of statements, the row-move condition, the roster slot, no grade, no re-verdict, the tail open : %s' % g1)
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
