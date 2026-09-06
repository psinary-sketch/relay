# -*- coding: utf-8 -*-
"""b332_correspondence.py -- ONE ROW: THE CLAUSE STATED, NO TERMINAL, AND THE REASON.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### The ranking, the
### verdict on the navigator's expectation and the line counts are read from `b332_statement_rows.json`,
### never typed. ### **THE HAZARD:** ### a row in the table of compiled statements that reads as if the
### clause had a compiled form. It has none, and the terminal cell says NO TERMINAL and why, first.
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


def read_records():
    return json.load(io.open(os.path.join(D, 'b332_statement_rows.json'), encoding='utf-8'))


SCOPE_TAIL = ("**SCOPE: A STATEMENT, NOT A RESULT.** The clause is not discharged, not weakened, not replaced; one face of the "
              "obligation and not its compiled equivalence (the deposit's refusal quoted beside it). No proof attempted; no grade "
              "moved or conferred. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt "
              "item 1 restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's "
              "record. h2 stands exactly where the deposit left it. NOTHING DEPOSITS.")


def rows():
    r = read_records()
    rk = ', '.join('%s (%s)' % (k, g) for _o, k, _n, g, _re in r['ranking'])
    top = r['ranking'][0]
    return [
        ("THE CLAUSE STATED: THE OPEN CLAUSE IN THE ARC'S VOCABULARY, EVERY CONSTITUENT UNFOLDED TO ITS OWNER AND GRADED, THE E0 GATE RUN, THE CONSTITUENTS RANKED (b332)",
         "THE CLAUSE STATED: THE OPEN CLAUSE IN THE ARC'S VOCABULARY, EVERY CONSTITUENT UNFOLDED TO ITS OWNER AND GRADED, THE E0 GATE RUN, THE "
         "CONSTITUENTS RANKED (b332): **(S)** for every g in the source's class (Definition 3.1 with Proposition C.1's vanishing set; the "
         "discriminating seeds of b328 inside it), the places sum of the explicit formula keeps the criterion's sign, `SUM_v W_v(g conv g-bar^#) <= 0` "
         "-- the positivity face's realized form, placed as the fourth register's with the deposit's refusal to compile the cross-register "
         "equivalences quoted beside it, the deposit's own words on h2 at its head and the register sentence exact. THE PLACES SUM UNFOLDED as "
         "the arc realized it (the finite places' contribution, b310/b329; the prime sum, b306; the archimedean distribution with its digamma "
         "witness, b315/b320; the compressed square plus the remainder that is the margin, b318/b320/b321), each constituent to a kernel "
         "terminal, a local proposition, or an import under the bar with its owner -- THE E0 GATE HALTS AT K8, the quantifiers over the class "
         "and over the zeros, UNOWNED: the clause itself. THE RANKING under the sealed rule, softest first: %s. **THE NAVIGATOR'S REGISTERED "
         "EXPECTATION (the remainder softest): %s** -- the softest rank is held by %s, %s, because it carries a DEFINED-ONLY grade from b315 "
         "that the remainder does not." % (rk, r['verdict'], top[1], top[2]),
         "**NO TERMINAL, AND THE REASON: ANALYSIS, QUANTIFIED OVER AN INFINITE CLASS AND OVER THE ZEROS.** The statement has no compiled "
         "form; the finite side's counting form (B329, B310) and the pentagon's structure (Register4_positivity) are the only compiled "
         "objects it unfolds to, and neither is the statement.",
         "**NO PRINT.** The statement lives at `FINDINGS.md` anchor `clause-stated` (%+d lines, %d -> %d), as row S1 of the faces ledger, and as "
         "one appended cross-reference line on the arc keystone." % (r['lines_added'], r['lines_before'], r['lines_after']),
         "**A STATEMENT ACT.** Every grade in it is its owner's; the E0 gate's unowned constituent is the clause; the aim-map is named as the act "
         "that would chart the softest constituent's behaviour over aims, and neither it nor this act is the discharge. NO GRADE MOVED.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b332 -- THE CLAUSE STATED. ### THE ROW.")
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
    g1 = 'NO TERMINAL, AND THE REASON' in ROWS[0][2] and 'A STATEMENT, NOT A RESULT' in ROWS[0][5] and 'HALTS AT K8' in ROWS[0][1]
    print('  the row says NO TERMINAL with its reason, a statement not a result, and the gate halting at K8 : %s' % g1)
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
    new = txt.rstrip('\n') + '\n' + '\n'.join(lines) + '\n'
    open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(TABLE + '.tmp', TABLE)
    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    tail = back.rstrip('\n').split('\n')[-1]
    cells = G.split_cells(tail)
    ok = (got[-1] == start and all(m in back for m, _s, _t, _p, _g, _sc, _st in ROWS) and C.blank_cells(back) == 0 and len(cells) == 6 and all(x.strip() for x in cells))
    print('  READ BACK         : last row number is %d ; cells on disk %d (6 required, none blank)' % (got[-1], len(cells)))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
