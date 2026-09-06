# -*- coding: utf-8 -*-
"""b336_correspondence.py -- ONE ROW: THE COST CENSUS. NO TERMINAL, AND THE REASON.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### The typed rows and the
### prices are read from the census tool's own table and its run file, never typed here. ### **THE HAZARD:** a row
### that reads as if a grade moved, or a price were a prediction.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402
import b303_correspondence as G   # noqa: E402
import b336_cost as CT            # noqa: E402

SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')
D = os.path.join(ROOT, 'data')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SCOPE_TAIL = ("**SCOPE: A CENSUS ON THE FACES LEDGER, TYPED, NO GRADE MOVED.** A cost is not a grade, not a plan, not a prediction; the pole-constant "
              "row states a relation the record carries and costs zero; the phase-rule addendum refines b328's sentence to the general condition and "
              "edits nothing of b328's. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap, its row unchanged. The seam's "
              "debt item 1 restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands "
              "exactly where the deposit left it. NOTHING DEPOSITS.")


def rows():
    run = io.open(os.path.join(D, 'b336_cost_run.txt'), encoding='utf-8').read()
    m = re.search(r'rows typed (\d+)', run)
    n = m.group(1)
    by_type = {}
    for rid, _h, typ, _w, _p in CT.COST:
        by_type.setdefault(typ, []).append(rid)
    typed = '; '.join('%s: %s' % (t, ', '.join(by_type[t])) for t in CT.TYPE_ORDER + ['ZERO'] if t in by_type)
    priced = [r[0] for r in CT.COST if r[4] not in (CT.NO_PRICE, 'cost zero') and not r[4].startswith("the certificate's")]
    marker = "THE COST CENSUS: A TYPED COST COLUMN ON THE FACES LEDGER THROUGH ITS WRITER, THE SORTED VIEW, THE POLE-CONSTANT ROW L2 (STATED, COST ZERO), THE PHASE-RULE ADDENDUM TO b328's BLOCK -- NO GRADE MOVED (b336, leg 1 of the sortie)"
    return [
        (marker,
         marker + ": for each of the ledger's rows, what moving it ONE grade would take, typed as READ / IMPORT / MEASUREMENT / DERIVATION / "
         "CONSTRUCTION with the record's price quoted at its emitter where the record prices the step -- %s rows typed (%s); the rows the record "
         "prices: %s, by the unit's domain factor (b322, `3.104e+02`, an extrapolation labelled as one), the exponent's ratio (b321, the two "
         "remainder copies apart by between one twenty-fourth and one fifth of the distance to the equality), the instrument's act count "
         "(b321_run, six acts), the crossing widths (b328's seven cells; b334's three aims); every other row `no price in the record`. The column "
         "filed as an append-only block keyed to the row ids (the ledger's own law: rows above are never rewritten), the sorted view emitted to relay "
         "`data/b336_cost_sorted.txt`. Row L2 through the writer: the deposit's archimedean channel on the Li family is the archimedean distribution "
         "plus the pole constant 1, the two margins two evaluations of one distribution and not one functional (FINDINGS), separated by the pole constant (b331) -- STATED, cost zero. The addendum to "
         "b328's block: the quadruple's term `4 \\|G\\|^2 cos 2 phi` is negative only between 45 and 135 degrees, b334's chart sign column cited; "
         "b328's own phases near ninety unaffected. **NO GRADE MOVED.**" % (n, typed, ', '.join(priced)),
         "**NO TERMINAL, AND THE REASON: A CENSUS ACT** -- a typing of what the record says is owed, in the rows' own words; nothing is decided.",
         "**NO PRINT.** One row, two blocks, all through the ledger's writer; no findings section; the papers repo moves by the ledger.",
         "**NO GRADE.** Every existing row byte-identical; a cost is not a grade; a price is not a prediction.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b336 -- THE COST CENSUS. ### THE ROW.")
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
    g1 = 'NO TERMINAL, AND THE REASON' in ROWS[0][2] and 'A CENSUS ACT' in ROWS[0][2] and 'NO GRADE MOVED' in ROWS[0][1] and 'NO GRADE' in ROWS[0][4]
    print('  the row says NO TERMINAL with its reason, a census act, no grade moved : %s' % g1)
    if not g1:
        return 1
    present = [m for m, _s, _t, _p, _g, _sc, _st in ROWS if m in txt]
    if present:
        print('  ### ROW ALREADY PRESENT -- NOTHING WRITTEN.')
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
    tail = back.rstrip(chr(10)).split(chr(10))[-1]
    cells = G.split_cells(tail)
    ok = (got[-1] == start and all(m in back for m, _s, _t, _p, _g, _sc, _st in ROWS) and C.blank_cells(back) == 0 and len(cells) == 6 and all(x.strip() for x in cells))
    print('  READ BACK         : last row number is %d ; cells on disk %d (6 required, none blank)' % (got[-1], len(cells)))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
