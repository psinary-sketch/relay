# -*- coding: utf-8 -*-
"""b339_correspondence.py -- ONE ROW: THE EXPONENT PRICED UNDER b322's SEALED RULE, UNAFFORDABLE AT THE SEALED CEILING.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every number is read from the
### price tool's record, never typed. ### **THE HAZARD:** a row that reads as if a candidate were preferred, or as if
### the price were a prediction.
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

SCOPE_TAIL = ("**SCOPE: A PRICE UNDER b322's SEALED RULE, AND NO MEASUREMENT AT A NEW DOMAIN -- NO BAR MOVED, NO CANDIDATE PREFERRED, NO GRADE CONFERRED.** "
              "A price is not a prediction; it is an extrapolation of a fitted slope and is labelled as one. Nothing about the quantifier, h2, totality or the "
              "roster. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The patent "
              "lane carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where the deposit left it. The wave PARKED by the "
              "author's ruling. NOTHING DEPOSITS.")


def rows():
    P = json.load(io.open(os.path.join(D, 'b339_price.json'), encoding='utf-8'))
    L = json.load(io.open(os.path.join(D, 'b339_limit.json'), encoding='utf-8'))
    c = P['cells']
    m = "THE EXPONENT PRICED UNDER b322's SEALED RULE: UNAFFORDABLE AT THE SEALED CEILING AT EVERY COVERED CELL, THE PRICE BANKED, NO FRAME BUILT (b339, leg 1 of the sortie b339-b343)"
    cells_txt = '; '.join("a = %s: R(128)/s = %.2f, rate X^%.3f (rms %.3f), X_req = %.0f, ratio %.2f" % (k, c[k]['ratio_now'], c[k]['p'], c[k]['rms'], c[k]['x_req'], c[k]['x_req'] / 128.0)
                          for k in sorted(c, key=float))
    lim_txt = '; '.join("a = %s: m_inf above the source's copy by %.2f s and the corpus's by %.2f s" % (k, L[k]['off_ef'] / c[k]['s'], L[k]['off_er'] / c[k]['s']) for k in sorted(L, key=float))
    return [
        (m,
         m + ": the identity residual R(X) = (W_inf - Tr(X)) - INT under the source's convention along b320's domain ladder (X = 8 to 128, N = 128X, NY = 512), "
         "reproduced from the record at every covered cell (%s), fitted by b322's fit_power; the split criterion R <= s/2 with s the two copies' separation from "
         "b321's bank; the price X_req = 128 (R(128)/(s/2))^(1/p), an extrapolation of a fitted slope and labelled as one; the ceiling X = 512 (N = 65536) sealed "
         "before the price. %s. No cell fits: no frame built, no remainder evaluated at a new domain, the erratum E-2026-09-03-1 untouched. THE SIDE READING on the "
         "same five frames, labelled and not a verdict arm: the margin's limit by its successive differences sits ABOVE BOTH candidates at every cell (%s), so the "
         "residual is descending toward a floor and the price is an under-estimate; the floor is what the next pricing must price. The navigator's (L1) NOT MET at "
         "this ceiling; this seat's (fits at a = 1.41 alone) NOT MET."
         % ('YES' if P['reproduces'] else 'NO', cells_txt, lim_txt),
         "**NO TERMINAL, AND THE REASON: A PRICE, NOT A MEASUREMENT** -- the question stays UNDER-RESOLVED, NOT OPEN, by b322's rule, with the new figure its price at a sealed ceiling.",
         "**NO PRINT.** A price tool, a side-reading tool, one update block on the faces ledger through its writer; nothing edited; TECHNE not touched.",
         "**NO GRADE MOVED; NO CANDIDATE PREFERRED.** The limit sits above both candidates and nearer the larger by exactly their separation, which is arithmetic and not a preference.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b339 -- THE EXPONENT PRICED. ### THE ROW.")
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
    g1 = all('NO TERMINAL, AND THE REASON' in r[2] for r in ROWS) and 'UNAFFORDABLE' in ROWS[0][1] and 'NO CANDIDATE PREFERRED' in ROWS[0][4] and 'not a prediction' in ROWS[0][5]
    print('  the row says NO TERMINAL with the reason, UNAFFORDABLE, no candidate preferred, a price not a prediction : %s' % g1)
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
