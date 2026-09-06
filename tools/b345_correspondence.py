# -*- coding: utf-8 -*-
"""b345_correspondence.py -- ONE ROW: THE LI CONTROL, RE-RUN, AND THE FIXTURE THAT COULD NOT SEPARATE.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every number is read from the
### act's own records, never typed. ### **THE HAZARD:** a row that reads as if b340 had been corrected, as if the Li
### family were lawful, as if the trail were paid, as if the deposit's finite-range positivity were this act's, or as
### if a failed fixture had been quietly repaired into passing.
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

SCOPE_TAIL = ("**SCOPE: A CONTROL CERTIFIES THE INSTRUMENT, NOT THE OBJECT; b340's BAR STAYS UNMET AND UNEDITED; AND A FAILED FIXTURE IS TABLED, NOT REPAIRED "
              "INTO PASSING.** The Li family is NOT in the lawful class, so Theorem 1's inequality and the Sonin margin do not apply to it; the zero side and "
              "the finite side are not evaluated, so `W-ORD-LI-FAMILY-CONTROL` stays OWED and is paid at its archimedean constituent only. The deposit's "
              "finite-range positivity is the deposit's, restated at its scope, and positivity in a finite range is not evidence of the kind the criterion "
              "respects. Nothing is priced on the floor's two held axes; the work-order names them and prices nothing. Nothing about the quantifier, h2, "
              "totality or the roster. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still "
              "unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where the deposit left it. "
              "The wave PARKED by the author's ruling. NOTHING DEPOSITS.")


def figures():
    C_ = json.load(io.open(os.path.join(D, 'b345_control.json'), encoding='utf-8'))
    F = json.load(io.open(os.path.join(D, 'b345_filings.json'), encoding='utf-8'))
    return C_, F


def rows():
    K, F = figures()
    kd = K['kernel_diagnostic'] or {}
    fx_clause = (
        "the sealed kernel fixture PASSED (worst `%s` against `%s`, the broken copy failing at `%s`)" % (K['kernel_worst'], K['fix_bar'], K['kernel_broken'])
        if K['kernel_fixture'] else
        ("**THE SEALED KERNEL FIXTURE FAILED AT ITS OWN THRESHOLD AND IS TABLED AS A DEFECTIVE BAR, NOT REPAIRED INTO PASSING.** Section (C) sealed, in one "
         "paragraph, a recurrence to `\\|w\\| >= %d` with the Stirling asymptotic through `B_%d` AND a fixture threshold of `%s`. The first term that truncation "
         "drops leaves the routine a floor: the hand-rolled kernel agrees with mpmath's to `%s`, and the measured miss tracks the first dropped term at every "
         "one of the six sealed points, so what is measured is the truncation's own floor and not a coding defect. At `%s` the fixture rejects the CORRECT copy "
         "as well as the broken one (`%s`), so AT ITS OWN THRESHOLD IT SEPARATES NOTHING. Holding the sealed truncation and carrying only the recurrence to "
         "`\\|w\\| >= %s` brings the same routine to `%s`, which locates the defect in one named half -- the threshold, not the truncation -- and is a DIAGNOSTIC, "
         "not this act's route B and not a value used anywhere. The registration is not edited and the bar is not rewritten; what the bar would have licensed, "
         "that route B's kernel is correct AT THE SEALED TOLERANCE, is NOT CONFERRED, and what is carried instead is a measurement, which is not a met bar"
         % (K['recur_to'], 2 * K['n_bern'], K['fix_bar'], K['kernel_worst'], K['fix_bar'], K['kernel_broken'], kd.get('recur'), kd.get('worst'))))
    m = ("THE LI CONTROL RE-RUN UNDER A BAR WITH THE TAIL RULE FIXED BEFORE ANY VALUE: %s AT %d OF %d TABULATED INDICES BY TWO ROUTES SHARING NO CODE, WITH THE "
         "SEALED KERNEL FIXTURE %s (b345)" % (K['verdict'], K['n_hold'], len(K['indices']), 'MET' if K['kernel_fixture'] else 'TABLED AS A DEFECTIVE BAR'))
    stmt = (m + ": the quantity is the archimedean distribution `I(n) = (1/2 pi) INT Re G_n(1/2 + iu) h_+(u) du` on the Li test family, with the derived kernel "
            "`h_+(u) = Re psi(1/4 + iu/2) - log pi`, at the %d indices the balance keystone tabulates. **THE TAIL PANEL'S QUADRATURE RULE WAS FIXED IN THE "
            "SEALED REGISTRATION BEFORE ANY VALUE, AS TANH-SINH** -- the rule b340's own diagnosis named against the Gauss-Legendre-on-an-infinite-panel that "
            "failed b340's bar -- and no panel of either route uses Gauss-Legendre. ROUTE A is b340's theta route, imported and unedited. ROUTE B is written "
            "fresh, sharing no code: the `u` variable, the transform factor as the complex power `Re[1 - ((s-1)/s)^n]` rather than the cosine identity, a "
            "HAND-ROLLED digamma calling no special function of mpmath, and the phase-multiple panels with the infinite tail. What the two share is named "
            "rather than claimed disjoint: arbitrary-precision arithmetic, elementary functions, and mpmath's quadrature. **THE BAR, THIS ACT'S OWN AND WITH "
            "b340's NUMBERS:** the control holds at index `n` when `\\|I(n) + 1 - lambda_A(n)\\| <= 1e-9 max(1, \\|lambda_A(n)\\|)`, the drift between the routes is "
            "below the same bar, and the noise-floor gate returns RESOLVED. **IT HOLDS AT %d OF %d:** worst identity miss `%s`, worst drift between routes "
            "`%s`, every index RESOLVED, the pole constant `L_n[log s]` carried as its own column and equal to `1` to `%s`, the deposit's channel corroborated "
            "at two radii to `%s` and against the source's (4.11) to `%s`, and the keystone's own printed column reproduced to `%s`. %s. **b340's BAR IS NOT "
            "REWRITTEN AND ITS VERDICT IS NOT RE-VERDICTED** -- a re-run under a new bar is a new measurement, not a correction. **THE FAMILY IS NOT IN THE "
            "LAWFUL CLASS** (three of three of Theorem 1's conditions fail), so Theorem 1's inequality, the Sonin margin, the square on the stable cut, b321's "
            "control bar, b326's per-cell closures and the atlas's zero-side truncation bound DO NOT APPLY; what applies is the kernel identity (b333), the "
            "arrangement `Z = P - PR + A` (b321), and the noise-floor gate as a method. The deposit's finite-range positivity is restated at its scope beside "
            "the values, the margin positive at all %d indices, with the bench's own sentence that positivity in a finite range is not evidence of the kind the "
            "criterion respects. The bridge row L1 updated through the writer to **ONE DISTRIBUTION ON TWO FAMILIES**, with what is measured (the archimedean "
            "constituent, at those indices, at this bar, on this family) and what is not (the zero side, the finite side `S_f`, and the Sonin margin, which is "
            "not defined on this family at all). The author's work-order filed as `%s` on the trails ledger: the floor's two unmoved axes are priceable from "
            "b344's printed figures WITHOUT re-running it, and nothing is priced here."
            % (len(K['indices']), K['n_hold'], len(K['indices']), K['worst_miss'], K['worst_drift'], K['pole_worst'],
               K['radii_worst'], K['routeB_worst'], K['worst_keystone'], fx_clause, len(K['indices']), F['trail_id']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: A CONTROL IS A MEASUREMENT OF THE INSTRUMENT** -- nothing about the mathematics is decided by it, and the family it "
         "runs on is outside the class every theorem here is stated for.",
         "**NO PRINT.** Relay tools only, plus two append-only blocks in the papers repo (FACES_LEDGER.md, OPEN_TRAILS.md), each through or under its own "
         "ledger's discipline; no owner instrument edited; no deposited text touched.",
         "**NO GRADE MOVED; NO BAR MOVED.** b340's bar stays unmet; this act's bar is its own; and the sealed fixture that failed confers nothing.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b345 -- THE LI CONTROL, RE-RUN. ### THE ROW.")
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
          and 'NOT IN THE LAWFUL CLASS' in ROWS[0][1]
          and "b340's BAR IS NOT REWRITTEN" in ROWS[0][1]
          and 'NO GRADE MOVED' in ROWS[0][4]
          and 'A CONTROL CERTIFIES THE INSTRUMENT, NOT THE OBJECT' in ROWS[0][5]
          and 'NOTHING DEPOSITS' in ROWS[0][5])
    print('  the row says NO TERMINAL with the reason, not in the lawful class, b340 not rewritten, no grade moved, a control certifies the instrument : %s' % g1)
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
