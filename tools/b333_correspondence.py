# -*- coding: utf-8 -*-
"""b333_correspondence.py -- ONE ROW: THE ARCHIMEDEAN TERM DERIVED, NO TERMINAL, AND THE REASON.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### The verdict as the
### derivation tool printed it, the diagnostic's worst disagreements and the re-run ranking are read from
### `b333_derive.json`, `b333_diagnose.json` and `b333_rerank.json`, never typed. ### **THE HAZARD:** ### a row
### that reads as if the archimedean term's SIZE were certified, as if the sealed bar had been met, or as if a
### grade beyond the derivation's own had been conferred.
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


def load(n):
    return json.load(io.open(os.path.join(D, n), encoding='utf-8'))


SCOPE_TAIL = ("**SCOPE: A DERIVATION UNDER THE IMPORT BAR, ONE CONSTITUENT'S PROVENANCE.** No grade conferred beyond the derivation's own; "
              "the measurement's grade is not conferred. Nothing about the quantifier, which stays unowned; nothing about the clause, which is "
              "not discharged. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, "
              "still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where "
              "the deposit left it. NOTHING DEPOSITS.")


def rows():
    r = load('b333_derive.json')
    g = load('b333_diagnose.json')
    k = load('b333_rerank.json')
    rk = ', '.join('%s (%s)' % (key, gr) for _o, key, _n, gr, _re in k['ranking'])
    soft = ' and '.join(k['softest'])
    k5 = '; '.join('%s (%s)' % (gr, o) for gr, o, _f in k['k5_grades'])
    marker = "THE ARCHIMEDEAN TERM DERIVED: THE STATED CLAUSE'S CONSTITUENT K5 LIFTED FROM DEFINITION-ONLY TO DERIVATION-ON-IMPORT, A THIRD ROUTE, THE RE-RANK (b333)"
    return [
        (marker,
         marker + ": **THE DERIVATION TOOL'S VERDICT, AS PRINTED, FIRST: %s.** Diagnosed (`tools/b333_diagnose.py`): the act's sealed bar paired the "
         "third route, run on the atlas's bump, with b320's table, and b320 computed that table for its own function `autocorrelation(mean_zero_variant(a))`; "
         "**THE RECORD'S ARCHIMEDEAN NUMBERS ARE NOT TOUCHED** -- the third route ((150) on the real side by mpmath.quad, no corpus code) agrees with the "
         "atlas's own banked channel for the bump at all thirteen cells (worst %.3e) and with b320's two routes applied to the bump (worst %.3e digamma, "
         "%.3e (38)), and (150) on b320's own function agrees with b320's table (worst %.3e / %.3e); the sealed bar, as sealed, is NOT MET and is not "
         "rewritten (a defect on this act's sealed face, declared). THE CHAIN, its own verdict DERIVES-ON-IMPORT: the classical term as the pinned source "
         "states it in its Appendix B -- (150) the principal value at the identity, (151) the Gamma factor with its power of pi and its logarithmic "
         "derivative against the transform, (152)-(153) the digamma kernel h_+, the source's own W_inf = -W_R -- read link by link under the corpus's "
         "conventions (f(x) = x^{-1/2} w(log x); f~(1/2 + i tau) = f-hat(tau); f(1) = w(0); Fourier inversion at zero) to the atlas's "
         "`A = (1/2pi) INT hhat [Re psi(1/4 + iu/2) - log pi] du`: **THE CORPUS'S A IS THE SOURCE'S W_inf = -W_R**, entering (148) as pole + W_inf - PRIME, "
         "the orientation the calibration fixed; the factor-of-two hazard of b325 checked from one identity (h_+ is twice the real part of the logarithmic "
         "derivative of pi^{-s/2} Gamma(s/2); the same rule on the Epstein factor gives b326's kernel). THE RE-RANK under b332's sealed rule, nothing "
         "adjusted, K5's grades %s (MEASURED-ON-FAMILIES not conferred): %s -- **THE NEW SOFTEST: %s**; the navigator's expectation for it was not stated "
         "in the order, this seat's (K5 and K6 tied) %s; the ranking identical with or without the un-conferred grade (%s)."
         % (r['verdict'], g['A_worst']['atlas'], g['A_worst']['dig'], g['A_worst']['w38'], g['B_worst']['dig'], g['B_worst']['w38'],
            k5, rk, soft, k['seat_expectation'], k['ranking_with_families_identical']),
         "**NO TERMINAL, AND THE REASON: A DERIVATION UNDER THE IMPORT BAR WITH ANALYSIS IN IT** -- a principal-value integral and a Gamma "
         "function; nothing here is finite-decidable.",
         "**NO PRINT.** The grade update went through the ledger's writer as an append-only block naming S1 and K5 only; the findings addendum "
         "was appended after the clause-stated section, which is byte-identical.",
         "**THE GRADE IS THE DERIVATION'S OWN: DERIVES-ON-IMPORTS, the imports (150), (151), (152)-(153), W_inf = -W_R; MEASURED-ON-FAMILIES NOT "
         "CONFERRED.** Four routes agreeing on the bump at thirteen cells certify that the routes agree, not the size of the term. The aim-map is named as "
         "next, its target the new softest; neither it nor this act is the discharge.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b333 -- THE ARCHIMEDEAN TERM DERIVED. ### THE ROW.")
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
    g1 = ('NO TERMINAL, AND THE REASON' in ROWS[0][2] and 'VERDICT, AS PRINTED, FIRST' in ROWS[0][1] and 'NEW SOFTEST' in ROWS[0][1]
          and 'NOT MET and is not' in ROWS[0][1] and 'MEASURED-ON-FAMILIES NOT' in ROWS[0][4] and "THE GRADE IS THE DERIVATION'S OWN" in ROWS[0][4])
    print('  the row says NO TERMINAL with its reason, carries the verdict as printed first, the sealed bar not met, the new softest, and confers no grade beyond the derivation\'s : %s' % g1)
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
