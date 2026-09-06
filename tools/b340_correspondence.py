# -*- coding: utf-8 -*-
"""b340_correspondence.py -- ONE ROW: THE LI FAMILY CONTROL AT ITS ARCHIMEDEAN CONSTITUENT.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every number is read from the
### control tool's record, never typed. ### **THE HAZARD:** a row that reads as if the Sonin margin were defined on the
### Li family, or as if a control certified the object.
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

SCOPE_TAIL = ("**SCOPE: A CONTROL AT ONE CONSTITUENT, ON A FAMILY OUTSIDE THE LAWFUL CLASS -- IT CERTIFIES THE INSTRUMENT, NOT THE OBJECT; NO GRADE CONFERRED; "
              "THE SONIN MARGIN IS NOT DEFINED ON THE LI FAMILY.** The zero side and the finite side are not evaluated; the trail W-ORD-LI-FAMILY-CONTROL "
              "stays OWED at those constituents; W-ORD-LI-WEIL-BRIDGE untouched. Nothing about the quantifier, h2, totality or the roster. NO AGGREGATION IS "
              "STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent lane carried on the patent "
              "seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where the deposit left it. The wave PARKED by the author's ruling. NOTHING DEPOSITS.")


def rows():
    J = json.load(io.open(os.path.join(D, 'b340_control.json'), encoding='utf-8'))
    idx = J['indices']
    if J['holds_all']:
        m = "THE LI FAMILY CONTROL, AT ITS ARCHIMEDEAN CONSTITUENT: THE ARCHIMEDEAN DISTRIBUTION ON THE LI FAMILY BY THE DERIVED KERNEL EQUALS THE DEPOSIT'S CHANNEL LESS THE POLE CONSTANT AT ALL %d TABULATED INDICES -- A FOURTH CONTROL AT ONE CONSTITUENT (b340, leg 2 of the sortie b339-b343)" % len(idx)
        head = "a fourth control at its archimedean constituent, the bar holding at all %d indices" % len(idx)
    else:
        G = json.load(io.open(os.path.join(D, 'b340_diagnose.json'), encoding='utf-8'))
        m = "THE LI FAMILY CONTROL, AT ITS ARCHIMEDEAN CONSTITUENT: THE DIFFERING CONSTITUENT AS SEALED -- A QUADRATURE FAILURE OF THE SEALED REFINEMENT ROUTE, THE GATE REFUSING AT ALL %d TABULATED INDICES, WHILE THE IDENTITY I(n) + 1 = lambda_A(n) HOLDS BY THE THETA ROUTE AT EVERY INDEX (b340, leg 2 of the sortie b339-b343)" % len(idx)
        head = ("the differing constituent as sealed: %s -- the drift between the sealed quadratures exceeds the bar at all %d indices; the identity within the bar by the theta route alone at %d of %d; "
                "the diagnostic (a reading, not a verdict) puts the whole drift in the tail panel under the Gauss-Legendre rule (the finite panels agreeing to zero) and the same u route by tanh-sinh within the bar at every "
                "diagnosed index (at n = 130 within %s against the theta route); the bar as sealed NOT MET and not rewritten" % (J['what'], len(idx), J['n_identity'], len(idx), G['parts']['130']['u_ts_vs_theta']))
    return [
        (m,
         m + ": the Li test functions built from the pinned source's (3.2) in the corpus's half-line normalization (Mellin fixture worst %s; the closed form on the "
         "line worst %s), NOT in the lawful class (three of three of Theorem 1's conditions failing, stated with the certifications that apply and those that do "
         "not); I(n) = (1/2pi) INT Re G_n(1/2+iu) h_+(u) du by the derived kernel (b326, b333), two quadratures gated by the noise floor (worst drift %s), at the "
         "balance keystone's indices %s; against lambda_A(n) by the bench's own definitions (two radii agreeing to %s), the pole constant L_n[log s] = 1 carried "
         "as its own column (worst deviation %s), b327's identity as the bar (1e-9 max(1, \\|lambda_A\\|)), re-measured against the source's (4.11) at %s; worst "
         "\\|I(n) + 1 - lambda_A(n)\\| = %s, against the keystone's printed column %s; the finite-range positivity restated at its scope beside the values, the margin "
         "positive at all %d indices, the certificate the deposit's and its premises named and open. %s."
         % (J['worst_f1'], J['worst_f2'], J['worst_drift'], idx, J['radii_worst'], J['pole_worst'], J['routeB_worst'], J['worst_miss'], J['worst_keystone'], len(idx), head[0].upper() + head[1:]),
         "**NO TERMINAL, AND THE REASON: A CONTROL AT ONE CONSTITUENT** -- it certifies the instrument on a family outside the class; nothing about lambda_n for all n is decided.",
         "**NO PRINT.** One instrument tool, one update block on the faces ledger through its writer; the keystone and the bench read, not edited; TECHNE not touched.",
         "**NO GRADE MOVED; NO SONIN MARGIN ON THE LI FAMILY.** L1 keeps its grades with its corroboration extended by the kernel route; F1 keeps MEASURED as a control on the arc's family.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b340 -- THE LI FAMILY CONTROL. ### THE ROW.")
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
    g1 = all('NO TERMINAL, AND THE REASON' in r[2] for r in ROWS) and 'NOT in the lawful class' in ROWS[0][1] and 'NO SONIN MARGIN ON THE LI FAMILY' in ROWS[0][4] and 'CERTIFIES THE INSTRUMENT, NOT THE OBJECT' in ROWS[0][5]
    print('  the row says NO TERMINAL with the reason, not in the lawful class, no Sonin margin on the family, the instrument not the object : %s' % g1)
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
