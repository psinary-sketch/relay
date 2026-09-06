# -*- coding: utf-8 -*-
"""b344_correspondence.py -- ONE ROW: THE FLOOR PRICED ON ONE AXIS, THE SEAL'S OWN CLOCK, AND THE ROOM'S EDGE.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every number is read from the
### act's records, never typed. ### **THE HAZARD:** a row that reads as if the floor were explained, as if the axes
### held were exonerated, as if the repaired seal reached backwards, or as if a narrower room were a trend.
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

SCOPE_TAIL = ("**SCOPE: ONE AXIS MOVED IS ONE AXIS MOVED; A REPAIRED SEAL TOOL CERTIFIES NOTHING ABOUT THE ACTS SEALED BEFORE IT; A NARROWER ROOM AT A FINER "
              "GRID IS A FINER CHART AND NOT A TREND.** Nothing is concluded about the two axes held, nothing about the floor beyond the sealed rule's own words, "
              "and nothing about totality. The repair does not recover b342's lost timestamp and b342's order arm stays a defective bar. Nothing about the "
              "quantifier, h2, totality or the roster. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 "
              "restated, still unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where the "
              "deposit left it. The wave PARKED by the author's ruling. NOTHING DEPOSITS.")


def figures():
    N = json.load(io.open(os.path.join(D, 'b344_ny.json'), encoding='utf-8'))
    S = json.load(io.open(os.path.join(D, 'b344_seal_clock.json'), encoding='utf-8'))
    M = json.load(io.open(os.path.join(D, 'b344_module.json'), encoding='utf-8'))
    E = json.load(io.open(os.path.join(D, 'b344_edge.json'), encoding='utf-8'))
    v = [r['R_EF'] for r in N['rows']]
    steps = [v[i + 1] - v[i] for i in range(len(v) - 1)]
    ratios = [steps[i] / steps[i + 1] for i in range(len(steps) - 1)]
    r = ratios[-1]
    limit = v[-1] + steps[-1] / (r - 1.0)
    from_512 = limit - v[N['ladder'].index(512)]
    return N, S, M, E, v, ratios, limit, from_512


def rows():
    N, S, M, E, v, ratios, limit, from_512 = figures()
    m = ("THE FLOOR PRICED ON ONE AXIS: THE RESIDUAL MOVES WITH NY AND THE MOVEMENT IS %s, THE STABLE-CUT RANK CONSTANT ACROSS THE LADDER; THE SEAL TOOL "
         "REPAIRED TO CARRY ITS OWN CLOCK WITH EVERY EXISTING SEAL UNCHANGED; AND THE ROOM'S MINIMUM AT THE WIDER REACHING WIDTH BRACKETED (b344)" % N['size'])
    stmt = (m + ": COMPONENT 1 -- the axis NY moved over the sealed ladder %s at the reference frame N = %d, X = %g, with the cut's tau and the taper HELD and "
            "PRINTED at every rung so a later act can price them without re-running this one; the object autocorrelation(mean_zero_variant(1.41)), the one b320 "
            "measured and b339 priced. The stable-cut rank is constant at %d at every rung (free dimension %d, identity control 0), so NY does not move the rank. "
            "The residual under the source's convention runs %s and under the corpus's %s; the span across the ladder is %.6e against b339's floor at this cell "
            "of %+.9f, so by the sealed rule the residual MOVES with NY (largest relative change %.3e against the threshold 1e-3) and the movement is %s. A "
            "reading beside the verdict, labelled and conferring nothing: the increments fall by factors %s, so the residual converges in NY, and from the "
            "corpus's own NY = 512 the remaining travel to the extrapolated limit is %.3e, about a ninth of the floor -- the span is dominated by the "
            "under-resolved rung at NY = 128. COMPONENT 2 -- reg_seal.py repaired by the order's words to write the seal's UTC instant inside the block, "
            "additions-only, digest and cmd_verify untouched; all %d sealed files verified before and after with the same verdict and none rewritten; a fresh "
            "seal carries the clock and verifies, a seal whose clock is altered still verifies (the arm that states the limit rather than hiding it), a seal "
            "whose body is altered still refuses. The rule filed as modules/2026-09/SEAL_CARRIES_ITS_CLOCK.md, committed locally at %s, the remote at %s before "
            "and after, NOT PUSHED. COMPONENT 2b -- the grid extended one unit below b343's edge at a = 81 only, at quarter-unit steps %s: BRACKETED, the "
            "minimum INTERIOR at gamma = %.2f, room %+.9f, its neighbours larger on both sides; every height certified and no crossing on the seventeen-height "
            "grid. The narrowing as measured: b343's minimum %+.9f against this act's %+.9f, a ratio of %.2f."
            % (N['ladder'], N['N'], N['X'], N['ranks'][0], N['rows'][0]['free'],
               ' '.join('%+.9f' % x for x in v), ' '.join('%+.9f' % r['R_ER'] for r in N['rows']),
               N['span_abs_EF'], N['floor'], max(N['rel_EF'], N['rel_ER']), N['size'],
               ' '.join('%.2f' % x for x in ratios), from_512,
               S['sealed_before'], M['committed'], M['remote_after'], E['extension'],
               E['minimum']['gamma'], E['minimum']['room_z'], E['prior_minimum'], E['minimum']['room_z'], E['ratio']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: A MEASUREMENT OF THE INSTRUMENT, A TOOL REPAIR, AND A CHART** -- nothing about the mathematics is decided by any of the three.",
         "**NO PRINT.** Relay tools and one owner instrument edited by the order's words; one TECHNE module, private, local, NOT PUSHED; no file written in the papers repo.",
         "**NO GRADE MOVED; NO BAR MOVED.** Nothing is concluded about the two axes held, and the repaired seal certifies nothing about acts sealed before it.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b344 -- THE FLOOR PRICED, THE SEAL'S OWN CLOCK, AND THE ROOM'S EDGE. ### THE ROW.")
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
    g1 = all('NO TERMINAL, AND THE REASON' in r[2] for r in ROWS) and 'A FINER CHART AND NOT A TREND' in ROWS[0][5] and 'NO GRADE MOVED' in ROWS[0][4] \
        and 'ONE AXIS MOVED IS ONE AXIS MOVED' in ROWS[0][5] and 'NOT PUSHED' in ROWS[0][1]
    print('  the row says NO TERMINAL with the reason, one axis moved, a finer chart and not a trend, no grade moved, not pushed : %s' % g1)
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
