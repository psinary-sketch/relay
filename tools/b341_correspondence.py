# -*- coding: utf-8 -*-
"""b341_correspondence.py -- ONE ROW: THE TWO COEFFICIENTS, THE BENCH'S DICTIONARY THE CARRIER, FILED AS AN INTERNAL-RECORD ERRATUM.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every number is read from the
### act's records, never typed. ### **THE HAZARD:** a row that reads as if a bench measurement changed, or as if a
### deposited artifact were affected.
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

SCOPE_TAIL = ("**SCOPE: TWO CONSTANTS IN A VALIDATION DICTIONARY OF AN INTERNAL INSTRUMENT -- NO BENCH MEASUREMENT CHANGES, NO DEPOSITED ARTIFACT IS AFFECTED, "
              "NO OWNER FILE IS EDITED; THE CORRECTION OF RECORD IS THE ERRATA ENTRY AND THE BANK.** Nothing about lambda_n beyond n = 5, nothing about the "
              "quantifier, h2, totality or the roster. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 "
              "restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where the "
              "deposit left it. The wave PARKED by the author's ruling. NOTHING DEPOSITS.")


def rows():
    J = json.load(io.open(os.path.join(D, 'b341_coefficients.json'), encoding='utf-8'))
    L = json.load(io.open(os.path.join(D, 'b341_locate.json'), encoding='utf-8'))
    t3, t5 = J['table']['3'], J['table']['5']
    m = "THE TWO COEFFICIENTS: %s -- BY TWO ROUTES SHARING NO QUADRATURE, WITH KEIPER 1992 LOCATED UNDER THE IMPORT BAR AT n = 3; FILED AS E-2026-09-06-1, INTERNAL RECORD, THE OWNER FILES UNTOUCHED (b341, leg 3 of the sortie b339-b343)" % J['verdict']
    return [
        (m,
         m + ": the bench's KEIPER dictionary (line %d) reads %s and %s at n = 3, 5; the balance keystone's literature column (lines %d, %d) reads %s and %s; "
         "route (A), the bench's own definitions from its file at two radii (agreeing to %s), and route (B), the Li map of log xi by Taylor differentiation at "
         "s = 1, agree to %s and %s and give %s and %s; the dictionary is off by %s and %s (defects in the fourth and third significant figures), the keystone's "
         "column by %s and %s (its own rounding). The literature under the import bar: Keiper 1992 (sha256 %s..., his lambda_n / n) LOCATED at n = 3 and agreeing "
         "with the keystone; at n = 5 its row's mantissa was split by the text layer (a reading beside the rule, agreeing); Maslanka math/0406312 carries no "
         "tabulation at these indices; Coffey math-ph/0505052 prints six-decimal values agreeing with the keystone (readings beside the rule). No located source "
         "agrees with the dictionary. The entry appended to ERRATA after the partition block with its class in its heading; the dictionary's name is not its "
         "provenance (Keiper's coefficients are lambda_n / n); the navigator's (L3) (the bench carries the defect) MET."
         % (J['bench_line'], t3['bench'], t5['bench'], J['keystone_rows']['3']['line'], J['keystone_rows']['5']['line'], t3['keystone'], t5['keystone'],
            J['radii_worst'], t3['dAB'], t5['dAB'], t3['A'][:16], t5['A'][:16], t3['bench_off'], t5['bench_off'], t3['keystone_off'], t5['keystone_off'],
            L['sources']['S1']['sha256'][:8]),
         "**NO TERMINAL, AND THE REASON: A TRANSCRIPTION FILED** -- two constants in a validation dictionary; nothing about the mathematics is decided.",
         "**NO PRINT.** One appended ERRATA entry; the bench, the keystone and FINDINGS read, not edited; no PDF committed; TECHNE not touched.",
         "**NO GRADE MOVED; NO BENCH MEASUREMENT CHANGES.** The dictionary enters no computation; the bench's computed lambda_n are reproduced by two routes.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b341 -- THE TWO COEFFICIENTS. ### THE ROW.")
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
    g1 = all('NO TERMINAL, AND THE REASON' in r[2] for r in ROWS) and 'THE BENCH CARRIES THE DEFECT' in ROWS[0][1] and 'NO BENCH MEASUREMENT CHANGES' in ROWS[0][4] and 'NO DEPOSITED ARTIFACT IS AFFECTED' in ROWS[0][5]
    print('  the row says NO TERMINAL with the reason, the bench carries the defect, no measurement changes, no deposited artifact affected : %s' % g1)
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
    tails = back.rstrip(chr(10)).split(chr(10))[-1:]
    cells = [G.split_cells(t) for t in tails]
    ok = (got[-1] == start and all(m in back for m, _s, _t, _p, _g, _sc, _st in ROWS) and C.blank_cells(back) == 0
          and all(len(c) == 6 and all(x.strip() for x in c) for c in cells))
    print('  READ BACK         : last row number is %d ; cells on disk %s (6 required, none blank)' % (got[-1], [len(c) for c in cells]))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
