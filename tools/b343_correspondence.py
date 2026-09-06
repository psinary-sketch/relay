# -*- coding: utf-8 -*-
"""b343_correspondence.py -- ONE ROW: THE MAP'S NEXT REACH -- A FINER CHART AND A MEASUREMENT OF THE INSTRUMENT.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every number is read from the
### act's records, never typed. ### **THE HAZARD:** a row that reads as if a chart were a proof, or as if the floor
### were explained.
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

SCOPE_TAIL = ("**SCOPE: A CHART OVER THIRTEEN HEIGHTS AT TWO WIDTHS, AND A MEASUREMENT OF THE INSTRUMENT AT THREE FRAMES -- A FINER CHART IS A FINER CHART, AND "
              "NO GRADE IS CONFERRED.** The reaching widths are outside the square's and the eps evaluator's reach, so neither was evaluated there; the frames "
              "establish only what section (D)'s sealed reading rule allows, and the floor's other candidates are untouched. Nothing about the quantifier, h2, "
              "totality or the roster. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still "
              "unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where the deposit left it. The "
              "wave PARKED by the author's ruling. NOTHING DEPOSITS.")


def rows():
    Cj = json.load(io.open(os.path.join(D, 'b343_crossing.json'), encoding='utf-8'))
    F = json.load(io.open(os.path.join(D, 'b343_frames.json'), encoding='utf-8'))
    per, fr = Cj['per_width'], F['frames']
    nar = '; '.join('a = %s the room narrowest at gamma = %.2f, %+.9f' % (a, per[a]['narrowest']['gamma'], per[a]['narrowest']['room_z']) for a in sorted(per, key=float))
    m = "THE MAP'S NEXT REACH: %s ON THE FINER GRID BETWEEN gamma = 2 AND 8 AT BOTH REACHING WIDTHS; AND THE IDENTITY RESIDUAL AT ONE AIMED SEED ACROSS THREE GRID-AXIS FRAMES, A MEASUREMENT OF THE INSTRUMENT (b343, leg 5 of the sortie b339-b343)" % Cj['verdict'].upper()
    return [
        (m,
         m + ": the aim-map's quantities at the thirteen sealed heights 2.0, 2.5 ... 8.0 at a = 40 and a = 81, by b334's own code imported and not edited -- the "
         "archimedean distribution on two transforms with the (150) witness, the prime sum by two routes, the noise-floor gate on every sign; %s; the two heights "
         "shared with b334's coarse grid (gamma = 4 and 8, both widths) reproduce its banked values to %s. The residual against the frame at the aimed seed "
         "a = 1.41, gamma = 33.650101: the square on b319's stable cut at N = %s with X = 32 and NY = 512 fixed, the remainder under both conventions each named "
         "per E-2026-09-03-1's standing clause; the stable-cut rank %s, the residual under the source's convention %s. %s The draft's expectation that the "
         "residual grows with rank CANNOT BE SCORED on the axis the draft names, which holds the rank fixed and grows the grid; it is scored NOT APPLICABLE."
         % (nar, ('%.3e' % Cj['shared_worst']), [r['frame'][0] for r in fr],
            ('constant at %d' % fr[0]['rank']) if F['rank_constant'] else ('moved: %s' % sorted(set(r['rank'] for r in fr))),
            ' '.join('%+.9f' % r['R_EF'] for r in fr),
            ("unchanged across two doublings of N at fixed domain and rank (largest relative change %.3e), so the grid resolution at fixed domain is NOT the origin of b339's floor, and the floor's other candidates -- the fixed NY, the cut's tau, the taper -- are untouched."
             % max(F['rel_EF'], F['rel_ER'])) if F['unchanged'] else
            ("changed across the doublings (largest relative change %.3e); the size is reported and nothing is concluded about b339's floor." % max(F['rel_EF'], F['rel_ER']))),
         "**NO TERMINAL, AND THE REASON: A CHART AND AN INSTRUMENT MEASUREMENT** -- nothing about the mathematics is decided by either.",
         "**NO PRINT.** One instrument tool in two modes, one crossing reader, one update block on the faces ledger through its writer; every instrument imported; TECHNE not touched.",
         "**NO GRADE MOVED. K6 STAYS MEASURED-AT-COVERED-CELLS.** A finer chart is a finer chart; the residual's behaviour against the frame prices K6's instrument and confers nothing.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b343 -- THE MAP'S NEXT REACH. ### THE ROW.")
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
    g1 = all('NO TERMINAL, AND THE REASON' in r[2] for r in ROWS) and 'A FINER CHART IS A FINER CHART' in ROWS[0][5] and 'NO GRADE MOVED' in ROWS[0][4]
    print('  the row says NO TERMINAL with the reason, a finer chart is a finer chart, no grade moved : %s' % g1)
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
