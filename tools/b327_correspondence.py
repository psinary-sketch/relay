# -*- coding: utf-8 -*-
"""b327_correspondence.py -- TWO ROWS: THE FACES LEDGER BUILT, AND THE BRIDGE READ.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### The verdict
### words are read from `data/b327_bridge.json`, never typed from memory of the run.

### ### **THE HAZARD OF THESE TWO ROWS:** ### a ledger of every face side by side reads as a map of a
### route; it is a map of the premise. ### And `DIFFERENT` twice on the bridge reads as the bridge closed
### in the negative; it is the bridge typed more sharply and STILL OWED.
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


def rows():
    b = json.load(io.open(os.path.join(D, 'b327_bridge.json'), encoding='utf-8'))
    q1, q2 = b['q1'], b['q2']
    return [
        ("THE FACES LEDGER BUILT: EVERY FACE OR EQUIVALENCE THE CORPUS HAS MET, ONE ROW EACH, WITH ITS GRADE "
         "AND ITS OWED BRIDGES, AND NO EQUIVALENCE COMPILED (b327)",

         "THE FACES LEDGER BUILT: EVERY FACE OR EQUIVALENCE THE CORPUS HAS MET, ONE ROW EACH, WITH ITS GRADE "
         "AND ITS OWED BRIDGES, AND NO EQUIVALENCE COMPILED (b327): `PLACE-papers/FACES_LEDGER.md`, a "
         "cross-reference instrument at the papers root, class line ROUTED as the sibling ledgers', purpose "
         "*it certifies nothing*, the deposit's refusal to compile the cross-register equivalences quoted in "
         "its head. **THIRTEEN ROWS**: the pentagon's five faces as the deposit states them, the "
         "finite-instance identity, the Sonin margin, the Li margin, the spectral-realization wall, the "
         "fixed-point silence, the two-radius family, the Epstein negative control at b326's result with its "
         "family finding, and the live row. **EVERY QUOTED CLAIM WAS VERIFIED AGAINST ITS EMITTING FILE BY THE "
         "ROW-WRITER BEFORE IT WAS WRITTEN**; the cascade section carries one of STATED / OWED / NONE for all "
         "78 pairs, with three owed bridges cross-filed to the trails ledger by ID.",

         "**NO TERMINAL. A LEDGER, NOT A RESULT.** The row-writer `tools/b327_faces_row.py` refuses a "
         "duplicate id, a raw pipe, a blank cell, a struck clause or banned stem, and an unverified quotation; "
         "it read the file back after every write. Its quotation guard fired once during the seeding -- a "
         "mis-typed pin fragment on the R4 row -- and the row was appended after the correction, so R4 sits "
         "after F7 in file order; the ledger is append-only and the incident is on the record, not tidied.",

         "**THE GRADES ARE THE OWNING ACTS'.** PROVED names a kernel terminal at a pin (the finite-range "
         "certificate, the boundary marker, the conservation conditional, the split's linearity); MEASURED "
         "names the act and its number (b320, b321, b324, b325, b326, b309, b310, b293); IMPORTED names the "
         "pinned source; NAMED-ONLY is the corpus's own naming (R3; the wall under its internal name). **NO "
         "ROW IS PROMOTED BY ITS NEIGHBOURS.** The census `b327_faces_census.py` counts what is missing from "
         "the ledger by name, for this ledger and no other.",

         "**SCOPE: A CROSS-REFERENCE INSTRUMENT. IT CERTIFIES NOTHING AND COMPILES NOTHING.** NO GRADE MOVED; "
         "NO FACE PROMOTED; NO EQUIVALENCE STATED OR IMPLIED. Deposited texts read at the verified copy and "
         "not touched. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The "
         "seam's debt item 1 restated, still unpaid. h2 stands exactly where the deposit left it. NOTHING "
         "DEPOSITS.",

         "current"),

        ("THE LI-TO-WEIL BRIDGE READ: THE ARCHIMEDEAN CHANNEL IS THE ARCHIMEDEAN PLACE PLUS THE POLE CONSTANT, "
         "THE TWO MARGINS ARE NOT ONE FUNCTIONAL, AND THE BRIDGE STAYS OWED (b327)",

         "THE LI-TO-WEIL BRIDGE READ: THE ARCHIMEDEAN CHANNEL IS THE ARCHIMEDEAN PLACE PLUS THE POLE CONSTANT, "
         "THE TWO MARGINS ARE NOT ONE FUNCTIONAL, AND THE BRIDGE STAYS OWED (b327): under the import bar, the "
         "source is Lagarias, *Li coefficients for automorphic L-functions*, arXiv:math/0404394v4, pinned by this "
         "act by hash (Bombieri-Lagarias 1999, which it restates, was not obtainable). **THE IDENTIFICATION, "
         "IMPORTED:** lambda_n = S_inf(n) - S_f(n) + 1, the archimedean place, the finite places, and the pole "
         "at s = 0; the norm of the Li test function G_n(s) = 1 - (1 - 1/s)^n under the Weil scalar product is "
         "2 Re(lambda_n). **THE MAP, DERIVED AS A SEALED BAR AND CORROBORATED:** the deposit's Li map on its own "
         "f_A = log s + log Gamma(s/2) - (s/2) log pi gives lambda_A(n) = S_inf(n) + 1 for every n; measured by "
         "two routes (the bench's own functions, executed from its file; the source's closed form (4.11)) at "
         "n <= 30 to 1.3e-251, radii agreeing to 2e-250, the SAME arm failing by exactly 1 at every n. "
         "**QUESTION ONE: %s. QUESTION TWO: %s.**" % (q1, q2),

         "**NO TERMINAL, AND NO THEOREM.** Question one: the deposit's archimedean channel is the archimedean "
         "place PLUS the pole-at-zero constant -- the `log s` term of its own split, the source's *contribution "
         "from the pole at s = 0*; the gamma-factor part is the archimedean term exactly, normalizations "
         "reconciled with nothing left over. Question two: the Li margin's second term is the finite places "
         "(lambda_Z = -S_f); the Sonin margin's second term is the compressed square Tr(theta(g) S theta(g)*), "
         "*not a zero channel* (b324), and the arc measures the Weil functional on its family separately as the "
         "zero side (b321). **ONE DISTRIBUTION ON TWO FAMILIES -- 2 Re(Gamma_R'/Gamma_R), the atlas's kernel -- "
         "NOT ONE FUNCTIONAL.**",

         "**THE BRIDGE STAYS OWED AND IS TYPED MORE SHARPLY:** `W-ORD-LI-WEIL-BRIDGE` -- a relation between the "
         "compressed square on the Sonin family and the finite-place channel on the Li family, or its "
         "impossibility. The order's *if SAME* branch did not fire; at scope, the deposit's finite-range "
         "certificate says nothing about the Sonin margin on the Li family, whose members have no compact "
         "support and lie outside Theorem 1's class. The fourth control -- the formula closed on the Li family "
         "through the corpus's channels -- is priced at one act and not run (`W-ORD-LI-FAMILY-CONTROL`). One "
         "incidental finding, filed not edited: the bench's own literature dict disagrees with the balance "
         "keystone's literature column at n = 3 and n = 5 (a typed fixture; the computation matches the "
         "keystone's column to fourteen digits).",

         "**SCOPE: A READ AND A DERIVED MAP WITH ITS CORROBORATION. NOTHING ABOUT h2, THE IDENTITY'S TRUTH, OR "
         "THE ROSTER FOLLOWS.** The equivalence the deposit withholds is not stated or implied. NO GRADE MOVED; "
         "NO ACT RE-VERDICTED. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED). The patent lane "
         "carried on the patent seat's report, UNCONFIRMED on this seat's record. NOTHING DEPOSITS.",

         "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b327 -- THE FACES LEDGER, THE BRIDGE, AND TWO NOTES. ### THE ROWS.")
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
    slip = [m for m, s, _t, _p, _g, _st in ROWS if not s.startswith(m)]
    print('  marker is a literal prefix of its statement : %d/%d  %s' % (len(ROWS) - len(slip), len(ROWS), 'PASS' if not slip else '### FAIL ###'))
    if slip:
        return 1
    present = [m for m, _s, _t, _p, _g, _st in ROWS if m in txt]
    if present:
        print('  ### ROW(S) ALREADY PRESENT -- NOTHING WRITTEN: %d' % len(present))
        got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
        print('  table rows now : %d   blank cells : %d' % (len(got), C.blank_cells(txt)))
        print('=' * 100)
        return 0
    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('  last existing row : %d' % max(nums))
    print('  rows to append    : %d  (numbers %d..%d)' % (len(ROWS), start, start + len(ROWS) - 1))
    blank = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if not str(c).strip()]
    print('  blank cells in the new rows : %d  %s' % (len(blank), 'PASS' if not blank else '### FAIL ###'))
    if blank:
        return 1
    r1, r2 = ROWS[0], ROWS[1]
    g1 = ('NO EQUIVALENCE COMPILED' in r1[1] and 'it certifies nothing' in r1[1] and 'NO ROW IS PROMOTED' in r1[3])
    g2 = ('BRIDGE STAYS OWED' in r2[1] and 'NOT ONE FUNCTIONAL' in r2[2] and 'did not fire' in r2[3] and 'NOTHING DEPOSITS' in r2[4])
    print('  row 1 carries the refusal, the purpose, and no promotion : %s  %s' % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 carries the bridge owed, not one functional, the branch that did not fire : %s  %s' % (g2, 'PASS' if g2 else '### FAIL ###'))
    if not (g1 and g2):
        return 1
    over = [i for i, r in enumerate(ROWS) if 'SCOPE' not in r[4] or 'M-2' not in r[4]]
    print('  rows carrying their own scope refusal and M-2\'s row : %d/%d  %s' % (len(ROWS) - len(over), len(ROWS), 'PASS' if not over else '### FAIL ###'))
    if over:
        return 1
    lines = ['| %d | %s | %s | %s | %s | %s |' % (start + k, stmt, term, prof, grade, status)
             for k, (_m, stmt, term, prof, grade, status) in enumerate(ROWS)]
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
