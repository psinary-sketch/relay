# -*- coding: utf-8 -*-
"""b357_correspondence.py -- ONE ROW: WHAT THE LEDGERS SAY THE CHECKS CERTIFY.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every count is read
### from `data/b357_read.json`, never typed. ### **THE HAZARD:** a row that reads as if a ledger had been
### caught saying something FALSE, as if the membership question had been decided, as if an erratum had
### been OPENED, or as if a hand-picked twelve had been a census.
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

SCOPE_TAIL = ("**SCOPE: TWELVE PASSAGES THIS SEAT CHOSE ARE NOT A CENSUS OF FOUR LEDGERS.** Nothing mechanical enumerated the candidates, so a row that says the wider "
              "sentence and was not looked for is NOT COUNTED HERE. Not that any ledger says something FALSE -- the wider sentence is not necessarily false, and what is "
              "wrong in the three is the WARRANT and not the claim. NOT THAT THE MEMBERSHIP QUESTION IS DECIDED: whether the piecewise-linear object is in a class defined "
              "over smooth functions is b355's H1, graded REFUTABLE and ROUTED, and it stands exactly there. NOT THAT THE CORRECTION IS MADE -- it is DRAFTED and ROUTED and "
              "five passages still read as they read. NOT THAT A SEAT WHICH JUST CAUGHT ITS OWN SCANNER GROUPING BY A WORD IS RELIABLE BELOW ITS OWN STATED FLOOR. Nothing "
              "about the quantifier, h2, totality or the roster; NO CLASS IS DISCHARGED and THE CLAUSE HAS NOT MOVED. NO AGGREGATION IS STATED; M-2 REMAINS "
              "(SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on "
              "this seat's record. h2 stands exactly where the deposit left it. The wave PARKED by the author's ruling. NOTHING DEPOSITS.")


def rows():
    R = json.load(io.open(os.path.join(D, 'b357_read.json'), encoding='utf-8'))
    E = json.load(io.open(os.path.join(D, 'b357_reads.json'), encoding='utf-8'))
    n = len(R['rows'])
    nl = len(R['ledgers'])
    fault = R['attribution_fault']
    memo = R['membership_only']
    where = ', '.join('%s:%d' % (r['ledger'], r['line']) for r in R['wider'])
    m = ("THE LEDGERS DO SAY MORE THAN THE CHECKS ESTABLISHED, IN ALL FOUR OF THEM, AND WHAT IS WRONG IS THE WARRANT AND NOT THE CLAIM: %d OF %d PASSAGES ASSERT THAT THE "
         "CORPUS'S OWN TEST FUNCTIONS ARE IN THE SOURCE'S CLASS, %d OF THEM CREDITING THE DEFINITION 3.1 SCAN WITH ESTABLISHING IT -- AND THE SCAN CANNOT FAIL ON AN OBJECT "
         "BUILT AS AN AUTOCORRELATION (b357, leg 2 of the sortie b356-b357)"
         % (R['n_wider'], n, len(fault)))
    stmt = (m + ": the four ledgers read are FINDINGS.md, FACES_LEDGER.md, CORRESPONDENCE.md and tools/banked_index.py, and the statuses were sealed to three and no others "
            "BEFORE any row was read. **%d ROWS LOCATED AND CLASSIFIED, %d UNCLASSIFIED**, splitting %d WIDER / %d NARROWER / %d SILENT, and the wider ones are at %s -- "
            "**EVERY LEDGER REACHED**, which is what made the erratum owed rather than optional. **THE TWO FINDINGS ARE KEPT APART, AS THE SEAL REQUIRED:** (1) THE "
            "ATTRIBUTION FAULT, %d rows, crediting the scan by a parenthetical or by the preposition *by*; (2) MEMBERSHIP ASSERTED WITH NO WARRANT NAMED, %d rows carrying "
            "the same summarised parenthetical. **THE CONSEQUENCE, STATED ONCE: CLASS MEMBERSHIP IN THIS FAMILY RESTS ON THE CONSTRUCTION, AND THE SCAN CONFIRMS IT RATHER "
            "THAN TESTING IT** -- for a true autocorrelation the transform is a squared modulus, so positivity is automatic and what the scan discriminates is arithmetic "
            "that has gone wrong, which is exactly what b320's own wide-minus-narrow control at min f-hat = -5.85e-01 shows and why the scan is not vacuous. **AN "
            "INDEPENDENT TEST WOULD REQUIRE AN OBJECT NOT BUILT AS AN AUTOCORRELATION; NO ACT HAS NEEDED ONE AND NONE IS ORDERED HERE.** So the branch is SOME ROWS SAY IT "
            "by the mixture rule sealed before the reading, with (NO ROW SAYS THE WIDER SENTENCE) unreachable because %d say it and (THE ROWS ARE SILENT) unreachable "
            "because only %d of %d is. **AND THE ACT MADE A FRESH INSTANCE OF ITS OWN SUBJECT:** its first run split the five wider rows by GREPPING THIS SEAT'S OWN "
            "COMMENTARY FOR THE WORD *ATTRIBUTION* and mis-grouped 2 of 5 -- b348's use-and-mention species, in an act about a check that confirms rather than tests -- so "
            "**THE GROUPING IS NOW DECLARED DATA, ROW BY ROW**, the superseded run is kept UNEDITED at data/b357_read_run_SUPERSEDED_LEXICAL_GROUPING.txt, and the verdict, "
            "the twelve statuses and the five wider rows are IDENTICAL in both runs. **THE READING'S ONE BAR WAS EXACT AND SINGLE-ARM:** every classified row located by "
            "tools/anchor_from_file.py at its own ledger or reported UNCLASSIFIED, %d of %d located; across the act's %d extract reads, **%d ANCHORS DIFFER FROM THE HINT "
            "THAT FOUND THEM** -- anchors this seat would have mistyped."
            % (n, len(R['unclassified']), R['n_wider'], R['n_narrower'], R['n_silent'], where,
               len(fault), len(memo), R['n_wider'], R['n_silent'], n,
               n, n, E['reads'], E['anchors_differing']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: A WORDING IS NOT A MEASUREMENT** -- no banked number is affected, no check is demoted, no act is re-verdicted, and the question "
         "this relabelling raises about the objects themselves is b355's H1, still routed and still undecided.",
         "**NO PRINT.** Relay tools only. Nothing written to PLACE-papers, so the hook and the mirror are NOT OWED and the suite checks that state rather than assuming it; "
         "nothing in TECHNE-Core from this leg. **NOTHING IS WRITTEN TO ERRATA.md:** the entry is DRAFTED AND ROUTED at data/b357_errata_draft.txt, and the author opens.",
         "**NO GRADE MOVED; NO BAR MOVED; NO ROW EDITED.** Not one byte of FINDINGS.md, FACES_LEDGER.md, CORRESPONDENCE.md or tools/banked_index.py changed except this "
         "act's own appended row and key. b320, b328, b332, b334, b343, b344, b349, b355 and b356 stand exactly as banked, and every check that passed still passed.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b357 -- WHAT THE LEDGERS SAY THE CHECKS CERTIFY. ### THE ROW.')
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
          and 'WHAT IS WRONG IS THE WARRANT AND NOT THE CLAIM' in ROWS[0][0]
          and 'CANNOT FAIL ON AN OBJECT' in ROWS[0][0]
          and 'THE TWO FINDINGS ARE KEPT APART' in ROWS[0][1]
          and 'AN INDEPENDENT TEST WOULD REQUIRE AN OBJECT NOT BUILT AS AN AUTOCORRELATION' in ROWS[0][1]
          and 'NONE IS ORDERED HERE' in ROWS[0][1]
          and "use-and-mention species" in ROWS[0][1]
          and 'DECLARED DATA' in ROWS[0][1]
          and 'DRAFTED AND ROUTED' in ROWS[0][3]
          and 'NOTHING IS WRITTEN TO ERRATA.md' in ROWS[0][3]
          and 'NO ROW EDITED' in ROWS[0][4]
          and 'NOT A CENSUS' in ROWS[0][5]
          and 'NOTHING DEPOSITS' in ROWS[0][5])
    print('  the row says NO TERMINAL with the reason, warrant-not-claim, the two findings apart, the consequence once, the incident, the erratum not opened, not-a-census : %s' % g1)
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
