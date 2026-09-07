# -*- coding: utf-8 -*-
"""b360_correspondence.py -- ONE ROW: THE FOLD.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every count is read
### from the act's own JSONs and none is typed.
### ### **THE HAZARD THIS ROW IS WRITTEN AGAINST:** ### a row that reads as if a fold had settled something;
### as if the three rhyming obstructions had been shown to be one; as if locating an instrument's edge had
### explained a floor; as if a roster row made an archive true; or as if the span's closing sentence were a
### claim that no move aimed at the quantifier exists.
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
    "**SCOPE: A FOLD PROVES NOTHING, DISCHARGES NOTHING AND MOVES NO GRADE.** It is a summary of its acts at their own grades; every sentence in it belongs to an act that already banked it, and where the "
    "order's phrasing ran ahead of what the acts support the NARROWER sentence was written and the difference declared on the section's face. NOT THAT THE THREE RHYMING OBSTRUCTIONS ARE ONE PROBLEM -- no "
    "bridge is typed in either direction, and the deposit's own refusal is quoted at the deposited file. NOT THAT AN EDGE LOCATED IS A FLOOR EXPLAINED. NOT THAT A ROSTER ROW MAKES AN ARCHIVE TRUE: carrying "
    "a ledger says nothing about whether what the ledger says is true, and the addition reaches the archive from this rebuild forward and is NOT retroactive. NOT THAT THE SPAN'S CLOSING SENTENCE IS A CLAIM "
    "THAT NO MOVE EXISTS -- it is a statement about what this span put on the board and what it cost, and it opens nothing. Nothing about the quantifier, h2, totality or the roster's correctness; NO CLASS IS "
    "DISCHARGED, THE CLAUSE HAS NOT MOVED, NO COORDINATE IS CLOSED and THE PARTITION STAYS UNDECIDED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 "
    "restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. THE POSTURE LOCK IS SEPARATE AND WAS NOT TOUCHED BY A FOLD. h2 stands exactly where the "
    "deposit left it. The wave PARKED by the author's ruling. NOTHING IS DEPOSITED AND NOTHING WAS WRITTEN AT ZENODO.")


def rows():
    F = json.load(io.open(os.path.join(D, 'b360_fold.json'), encoding='utf-8'))
    E = json.load(io.open(os.path.join(D, 'b360_reads.json'), encoding='utf-8'))
    R = json.load(io.open(os.path.join(D, 'b360_roster.json'), encoding='utf-8'))
    m = ("THE ARC b349-b359 FOLDS INTO ONE STATEMENT, AND THE STATEMENT IS ABOUT WHAT THE CORPUS'S CHECKS CERTIFY RATHER THAN ABOUT THE FLOOR: %d acts filed as one PURELY ADDITIVE section of the findings "
         "document, the span COUNTED off the record rather than taken from the draft, every quotation located at the act that ORIGINATED it and every grade anchored VERBATIM in its own act's bank -- and "
         "**THREE OBSTRUCTIONS THAT RHYME ARE THREE OBSTRUCTIONS, WITH NO BRIDGE TYPED** (b360)"
         % F['n_span'])
    stmt = (m + ": **THE SPAN IS COUNTED, NOT TYPED** -- the emitter reads the last fold section's own filing line off FINDINGS.md (b%d) and finds each act's bank on disk, refusing to emit if the counted "
            "span and the result table disagree; it counted %d and the draft's assertion was never adopted. **F-QUOTE: %d quotations failing.** **F-NOGRADE: %d grade anchors failing** -- the no-grade-moved "
            "claim mechanical, carried forward from b348 as the programme's own memory asks. **F-ADDITIVE: a true prefix-extension of the document and of its committed blob, the section appearing once, %d "
            "lines added and nothing above them edited** (the prefix-of-blob reading is the PRE-PUSH one, which is the reading this act relies on). The extract located **%d of %d reads with 0 without an "
            "anchor, %d anchors differing from the hint that found them**, resolved by its own recorded clock and not by its name (b358's cure). **ADDITION ONE, THE THREE THAT RHYME:** the clause's quantifier "
            "at b332, the height coordinate's enumeration at b351, the width coordinate's union at b353 -- each quoted at the act that originated it and NOT at the faces ledger row that collects them -- with "
            "b358's localization added as a FOURTH ENTRY OF THE SAME KIND and not as a fifth obstruction, and the deposit's own law quoted beside them from the deposited monograph itself: it compiles the "
            "register structure *\"while deliberately **not** compiling the cross-register equivalences\"*. **ADDITION TWO, THE ARC AS ONE STATEMENT**, at the grade the acts support with a scope sentence "
            "beside each clause -- and one clause written NARROWER than the order put it, with the difference declared: the order says the instrument's floor was the quadrature bound; what the acts support is "
            "that b356 located the instrument's EDGE there, and **AN EDGE LOCATED IS NOT A FLOOR EXPLAINED**. **ADDITION THREE, THE DESK**, one list with where each item stands and what would move it, and the "
            "span's own finding filed as a sentence that opens nothing. **AND THE AUTHOR'S RULING EXECUTED:** FACES_LEDGER.md added to the mirror roster, %d rows to %d, appended at the END so no existing slot "
            "changes, every roster path of the committed blob at the same index and every other field identical to it."
            % (F['span_start'] - 1, F['n_span'], F['quotes_failing'], F['grades_failing'], F['lines_added'],
               E['reads'] - E['without_anchor'], E['reads'], E['anchors_differing'], R['before'], R['after']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: A FOLD RESTATES ITS ACTS AT THEIR OWN GRADES** -- it proves nothing, decides nothing and confers nothing, and a section that carries eleven verdicts carries eleven "
         "acts' verdicts and none of its own.",
         "**PRINT: PLACE-papers, ONE FILE.** FINDINGS.md gains the section *THE UNIFORMITY ARC, b349-b359 -- THE FOLD*, APPEND-ONLY, emitted by `tools/b360_fold.py` after F-QUOTE and F-NOGRADE passed. **AND "
         "relay, ONE ROSTER ROW:** `tools/mirror_roster.json` gains FACES_LEDGER.md on the author's ruling, written and read back by `tools/b360_roster.py`. **THE HOOK AND THE MIRROR ARE OWED AND PAID**, the "
         "mirror rebuilt AFTER the commit and the roster change verified in the rebuild. No faces row moves, so the faces writer does not run. Nothing in TECHNE-Core.",
         "**NO GRADE MOVED, AND THAT IS CHECKED AND NOT ASSERTED; NO BAR MOVED; NO ACT RE-VERDICTED; NO COORDINATE CLOSED.** Every grade in the section is the grade its own act wrote, required to appear "
         "verbatim in that act's bank or the section would not have been written. **AND THIS SEAT'S EXPECTATION WAS SCORED AGAINST IT:** it predicted the arc would fold and that the statement would be about "
         "what the corpus's checks certify rather than about the floor -- **MET**, and the floor thread's own last act says the floor question is exactly where b352 left it.",
         SCOPE, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b360 -- ONE ROW: THE FOLD, b349-b359.')
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
          and 'THREE OBSTRUCTIONS THAT RHYME ARE THREE OBSTRUCTIONS, WITH NO BRIDGE TYPED' in ROWS[0][0]
          and 'THE SPAN IS COUNTED, NOT TYPED' in ROWS[0][1]
          and 'AN EDGE LOCATED IS NOT A FLOOR EXPLAINED' in ROWS[0][1]
          and 'FOURTH ENTRY OF THE SAME KIND' in ROWS[0][1]
          and 'appended at the END so no existing slot' in ROWS[0][1]
          and 'APPEND-ONLY' in ROWS[0][3]
          and 'THE HOOK AND THE MIRROR ARE OWED AND PAID' in ROWS[0][3]
          and 'NO GRADE MOVED, AND THAT IS CHECKED AND NOT ASSERTED' in ROWS[0][4]
          and 'A FOLD PROVES NOTHING' in ROWS[0][5]
          and 'no bridge is typed in either direction' in ROWS[0][5]
          and all('NOTHING IS DEPOSITED' in r[5] for r in ROWS))
    print('  the row says NO TERMINAL with its reason, the rhyme unbridged, the span counted, the narrowing declared, the roster appended at the end, the hook and mirror paid, the grades checked : %s' % g1)
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
    print('  ### **THE TABLE IS A TRUE PREFIX OF ITSELF ABOVE THIS ROW** : %s'
          % back.startswith(txt.rstrip(chr(10))))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
