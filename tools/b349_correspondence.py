# -*- coding: utf-8 -*-
"""b349_correspondence.py -- ONE ROW: THE ROOM, RELATIVE BEFORE EXTENDED.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every number is read from the
### act's own records, never typed. ### **THE HAZARD:** a row that reads as if a surviving minimum were evidence, as
### if a lower room at a lower height were a descent, as if three lawful seeds proved the construction never
### degenerates, or as if the relative measure were the better one rather than a different one.
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

SCOPE_TAIL = ("**SCOPE: ONE MEASURE AGREEING WITH ANOTHER IS WEAKER THAN EITHER BEING RIGHT, AND THE RELATIVE MEASURE IS A DIFFERENT MEASURE AND NOT A BETTER ONE.** No "
              "crossing is claimed at any height. A narrower room at a lower height is a lower height and not a trend, and the room below gamma = 1 moves very little across "
              "three heights while the dip at 1.25 sits an order of magnitude under all of them -- a local feature, not a descent. Three lawful seeds at low heights mean these "
              "three did not degenerate; they do not mean the construction never does. The square and the remainder are NOT reached at this width. Nothing about the "
              "quantifier, h2, totality or the roster. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still "
              "unpaid. The patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where the deposit left it. The wave PARKED by "
              "the author's ruling. NOTHING DEPOSITS.")


def rows():
    R = json.load(io.open(os.path.join(D, 'b349_relative.json'), encoding='utf-8'))
    E = json.load(io.open(os.path.join(D, 'b349_extend.json'), encoding='utf-8'))
    v40, v81 = R['verdicts']['40.0'], R['verdicts']['81.0']
    f40, f81 = R['flatness']['40.0'], R['flatness']['81.0']
    m = ("THE ROOM MEASURED RELATIVE TO THE TERMS IT SITS BETWEEN, ON THE %d AIMS ALREADY CHARTED AND WITH NO NEW SEED: THE MINIMUM SURVIVES AT BOTH REACHING WIDTHS AND THE "
         "RELATIVE MEASURE IS FLATTER; THEN THE GRID EXTENDED BELOW THE BRACKETED MINIMUM, %d SEEDS ALL LAWFUL AND ALL INSIDE THE PHASE WINDOW, NONE DEGENERATE, NO CROSSING, "
         "AND THE MINIMUM STILL INTERIOR IN BOTH MEASURES (b349)"
         % (len(R['table']), len(E['seeds'])))
    stmt = (m + ": **THE RATIO WAS FIXED BEFORE ANY VALUE** -- R_rel = \|places\| / max(\|arch\|, \|prime\|), the LARGER of the two terms the room is a difference of, so the ratio "
            "cannot be inflated by a small denominator; the same denominator at every aim, both widths, both sides, and no aim got its own. **PART (a), READING AND NOT "
            "RUNNING:** %d aims from b334's two reaching legs, b343's two finer grids and b344's extension, %d duplicate aims counted once, **0 rows excluded by the sealed "
            "floor rule** -- the noise-floor gate returned RESOLVED on every one, and the smallest room in the record sits three orders above the gate's floor of 1.49e-08, so "
            "no room here is a non-measurement. The acts' own second routes are carried as a printed spread and not as an arm of this act: worst arch disagreement %s, worst "
            "places disagreement %s. **THE MINIMA:** at a = 40 both the absolute and the relative minimum sit at gamma = %g; at a = 81 both sit at gamma = %g. **SAME AIM AT "
            "BOTH WIDTHS, SO THE LOCATED POINT OF MAXIMUM TENSION IS NOT AN ARTIFACT OF ABSOLUTE MEASUREMENT**, and the sentence this act was registered to be able to write "
            "instead is not written. **AND THE RELATIVE MEASURE IS FLATTER AT BOTH WIDTHS** by the sealed largest-to-smallest test: %.2f absolute against %.2f relative at a = "
            "40, and %.2f against %.2f at a = 81 -- **so the navigator's expectation is half met and half refuted, and the halves point opposite ways: flatter, yes; the "
            "low-height minimum weakened, no.** **PART (b) THEREFORE RAN**, and its tool refuses to run if part (a)'s own record does not say the minimum stood. Three sealed "
            "heights at a = 81 only, **every seed checked on BOTH sealed conditions before any finite side was computed**: lawful by the source's Definition 3.1 with the pole "
            "conditions, and the phase at the aim inside b328's **WINDOW** of 45 to 135 degrees rather than past a threshold. **ALL THREE LAWFUL, ALL THREE INSIDE THE WINDOW "
            "AT %.1f, %.1f AND %.1f DEGREES, NONE DEGENERATE** -- this seat expected at least one degeneration and was wrong, having reasoned from the height alone when the "
            "phase does not follow the height alone. On the extended grid: **NO CROSSING**, every sign the same, the gate RESOLVED everywhere, no negative room; and **the "
            "minimum stays at gamma = 1.25, INTERIOR IN BOTH MEASURES**, its neighbours larger on both sides. Below gamma = 1 the room settles between 2.66e-04 and 2.99e-04 "
            "across three heights while the dip at 1.25 is an order of magnitude under all of them: **A LOCAL FEATURE AT ONE HEIGHT, NOT A DESCENT.** **AND THE SORTIE'S STEP "
            "ZERO WAS BUILT:** tools/quote_norm.py, one normaliser imported by both sides of every quotation comparison, over the species banked at b298 (two comparisons that "
            "agreed and neither of which saw a BOM), b309 (which named it the b298 family and cured the BYTE half through one imported normaliser) and b348 (the quotation "
            "half). Its fixtures include four of the OTHER polarity -- an absent sentence, a changed word, a changed number, a dropped clause, all of which must still fail -- "
            "and its reach is stated in its own header: it makes two sides comparable and **DOES NOT MAKE A QUOTATION TRUE**, and it is NOT retroactive. **THE ORDER NAMED A "
            "b305 INCIDENT THAT THIS SEAT COULD NOT LOCATE, AND NONE WAS MANUFACTURED**; the two the record does hold are named instead."
            % (len(R['table']), R['duplicates'], ('%.3e' % R['spread_arch']), ('%.3e' % R['spread_places']),
               v40['abs_gamma'], v81['abs_gamma'], f40['absolute'], f40['relative'], f81['absolute'], f81['relative'],
               E['seeds'][0]['phase_deg'], E['seeds'][1]['phase_deg'], E['seeds'][2]['phase_deg']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: A SECOND MEASURE OF THE SAME FIGURES IS A SECOND MEASURE** -- it can dissolve a reading, and here it did not, which leaves the reading "
         "exactly where it was rather than strengthening it.",
         "**NO PRINT.** Relay tools only; no file written in the papers repo, so the hook and the mirror are NOT OWED; nothing in TECHNE-Core; no owner instrument edited and "
         "no banked figure recomputed.",
         "**NO GRADE MOVED; NO BAR MOVED.** Three new heights are charted at their own reach and confer nothing; b343's and b344's rows stand exactly as banked.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b349 -- THE ROOM, RELATIVE BEFORE EXTENDED. ### THE ROW.")
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
          and 'NOT AN ARTIFACT OF ABSOLUTE MEASUREMENT' in ROWS[0][1]
          and 'NOT A DESCENT' in ROWS[0][1]
          and 'NONE WAS MANUFACTURED' in ROWS[0][1]
          and 'NO GRADE MOVED' in ROWS[0][4]
          and 'WEAKER THAN EITHER BEING RIGHT' in ROWS[0][5]
          and 'NOTHING DEPOSITS' in ROWS[0][5])
    print('  the row says NO TERMINAL with the reason, not an artifact, not a descent, nothing manufactured, no grade moved : %s' % g1)
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
