# -*- coding: utf-8 -*-
"""b334_correspondence.py -- TWO ROWS: THE AIM-MAP FOR ZETA WITH ITS CHART; THE EPSTEIN CONTROL CHARTED WITH THE
SOFTNESS OF THE PAIR. ### NO TERMINAL IN EITHER, AND THE REASON.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every value and verdict is
### read from `b334_chart.json` and `b334_grid.json`, never typed. ### **THE HAZARD:** a row that reads as if the
### chart were a proof, as if a size were certified, or as if a grade had been conferred.
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


SCOPE_TAIL = ("**SCOPE: A COMPUTATION ON THE CERTIFIED INSTRUMENTS, A FINITE-REACH CHART OVER AIMS, INTERPRETED BY NOBODY.** A chart is not a "
              "proof; no grade conferred; the softest pair gains a behaviour and not a grade; nothing about the quantifier, which stays unowned; "
              "nothing about h2, totality or the roster. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The "
              "seam's debt item 1 restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. "
              "h2 stands exactly where the deposit left it. NOTHING DEPOSITS.")


def rows():
    ch = load('b334_chart.json')
    g = load('b334_grid.json')
    nav = ch['navigator']
    reach = [b for b in ch['block'] if b['leg'] == 'reaching']
    cov = [b for b in ch['block'] if b['leg'] == 'covered']
    neg = sum(1 for b in reach if b['sign_z'] == '-')
    n_aims = sum(len(r['aims']) for r in g['seeds'])
    n_reached = sum(1 for r in g['seeds'] for q in r['aims'] if q['reached'])
    narrow = '; '.join('%s at gamma %.6f (%+.6f)' % (k, v['gamma'], v['room']) for k, v in sorted(ch['narrowest'].items()))
    cross = '; '.join('a = %g at gamma %.6f (places_q %+.6f)' % (a, gm, p) for (_l, a, gm, p) in ch['crossing']) or 'EMPTY'
    heights = '; '.join('%s -> %s' % (h, v if v else 'NONE') for h, v in ch['contains'].items())
    m1 = "THE AIM-MAP, FOR ZETA: THE ROOM THE ARITHMETIC LEAVES CHARTED OVER AIMS -- THE ARCHIMEDEAN DISTRIBUTION, THE SQUARE, THE MARGIN AND THE PRIME SUM PER AIM, THE NARROWEST POINTS, THE SOFTNESS OF K5 AND K6 (b334)"
    m2 = "THE AIM-MAP, FOR THE EPSTEIN FUNCTION: THE NEGATIVE CONTROL CHARTED OVER THE SAME AIMS -- THE CROSSING REGION AGAINST THE OFF-LINE ZEROS' HEIGHTS (b334)"
    return [
        (m1,
         m1 + ": on the sealed grid (gamma over %d heights from 4 to %.6f; beta over %d abscissae from the line to the first Epstein off-line zero's), "
         "b328's sine-aimed even seed at the reaching widths a = 40, 81 and the covered widths a = 1.3, 1.41 -- lawful by Definition 3.1 and the pole "
         "conditions at every seed built, the phase past 45 degrees at %d of %d aims (every reaching-leg aim off the line; none on the covered leg). "
         "On f = E conv E^# at every (gamma, a), like for like by name: the archimedean distribution by the derived kernel on two transforms and by the "
         "principal-value witness (150); the prime sum by two routes; the places side gated (refine 1 against 4, noise floor, sign certified above ten "
         "drifts); on the covered leg the square on the stable cut at two frames and the remainder by two quadratures, the identity residual printed "
         "per aim; on the reaching leg the square and the remainder NOT REACHED by measurement (the frame's X = 32 against a^2 = 1600, 6561; the eps "
         "evaluator past rho = 100). THE NARROWEST POINTS: %s. **(F1) THE PRIME SUM INSIDE THE MARGIN AT EVERY AIM AT THIS REACH: %s** (places_z "
         "certified negative at %d of %d reaching aims; margin - PR_z positive at %d of %d covered aims) -- **A PASSED TEST OVER A GRID AT THIS REACH "
         "AND NOTHING MORE.** THE SOFTNESS OF THE PAIR: Spearman(s5, s6) over the covered leg = %+.4f; **(F3) K5 AND K6 SOFTEN TOGETHER: %s** -- a "
         "behaviour over aims, not a grade."
         % (len(g['gammas']), max(g['gammas']), len(g['betas']), n_reached, n_aims, narrow, nav['F1'], neg, len(reach),
            sum(1 for b in cov if (b['margin'] - b['PR_z']) > 0), len(cov), ch['spearman_s5_s6'], nav['F3']),
         "**NO TERMINAL, AND THE REASON: A COMPUTATION ON ANALYTIC INSTRUMENTS AT NAMED RESOLUTIONS** -- transforms, a digamma kernel, a principal value, "
         "a stable cut; nothing here is finite-decidable, and a chart is not a proof.",
         "**NO PRINT.** The ledger update went through the writer as an append-only block naming S1 (K5, K6), F7 and b328's block; no findings section "
         "was written or edited.",
         "**NO GRADE: A BEHAVIOUR OVER AIMS, FILED AS THE CLAUSE'S FIRST CHART.** Signs certified by the gate; sizes reported at named resolutions. The "
         "cost census is named as next, then the wave decision.",
         SCOPE_TAIL, "current"),
        (m2,
         m2 + ": the same four for Z_Q (x^2 + xy + 6y^2, disc -23) at every aim -- the archimedean channel by the derived kernel `2 Re psi(1/2 + iu) - "
         "2 log(2 pi / sqrt23)` on two transforms (b325's halved kernel printed beside, unused), the finite side with the representation numbers by two "
         "Lambda_Q routes, the places side gated; the square and the remainder for Z_Q NOT AN INSTRUMENT THE RECORD HAS, said on every line. **THE "
         "CROSSING REGION** (places_q certified POSITIVE with no zero used, b328's forbidden sign): %s. Against the off-line zeros' heights on the grid: "
         "%s. **(F2) THE CROSSING REGION CONTAINS THE BANKED OFF-LINE ZEROS' AIMS: %s.** Crossing members at heights that are not off-line zeros: %s. "
         "**THE NEGATIVE CONTROL CHARTED, AND NOTHING MORE.**"
         % (cross, heights, nav['F2'], ch['elsewhere'] if ch['elsewhere'] else 'NONE'),
         "**NO TERMINAL, AND THE REASON: A COMPUTATION ON ANALYTIC INSTRUMENTS AT NAMED RESOLUTIONS**; a control, not a claim.",
         "**NO PRINT.** Carried in the same ledger block as the zeta chart.",
         "**NO GRADE.** b326's DOES NOT SEE IT on the arc's family and b328's SEES IT at seven of eight cells both stand; this act charts where the "
         "crossing sits over aims at two widths and names the region.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b334 -- THE AIM-MAP. ### THE ROWS.")
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
    g1 = all('NO TERMINAL, AND THE REASON' in r[2] for r in ROWS) and 'A PASSED TEST OVER A GRID AT THIS REACH' in ROWS[0][1] and 'NEGATIVE CONTROL CHARTED' in ROWS[1][1] and all('NO GRADE' in r[4] for r in ROWS)
    print('  both rows say NO TERMINAL with the reason, the zeta row calls the test a passed test at this reach, the Epstein row a control, neither confers a grade : %s' % g1)
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
    print('  last existing row : %d ; rows to append : %d and %d' % (max(nums), start, start + 1))
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
    tails = back.rstrip(chr(10)).split(chr(10))[-2:]
    cells = [G.split_cells(t) for t in tails]
    ok = (got[-1] == start + 1 and all(m in back for m, _s, _t, _p, _g, _sc, _st in ROWS) and C.blank_cells(back) == 0
          and all(len(c) == 6 and all(x.strip() for x in c) for c in cells))
    print('  READ BACK         : last row number is %d ; cells on disk %s (6 required, none blank)' % (got[-1], [len(c) for c in cells]))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
