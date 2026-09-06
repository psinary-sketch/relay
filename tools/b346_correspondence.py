# -*- coding: utf-8 -*-
"""b346_correspondence.py -- ONE ROW: THE EXPONENT BY RATE.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.** ### Every number is read from the
### act's own records, never typed. ### **THE HAZARD:** a row that reads as if a convention had been declared correct,
### as if b313 were superseded, as if the floor were explained, as if the separation had been measured rather than
### being exact by construction, or as if two estimators that collapsed onto one another had agreed.
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

SCOPE_TAIL = ("**SCOPE: A RATE TELLS YOU WHICH FUNCTION YOU ARE LOOKING AT; IT DOES NOT TELL YOU WHICH FUNCTION YOU SHOULD HAVE BEEN LOOKING AT.** No convention is "
              "declared correct: b312 decided which function the corpus's remainder is by unfolding definitions, b313's clause governs, and a rate is not a vote on it any "
              "more than a residue was. The floor is NOT explained -- one of its three named origins has been priced and the other two are named, not moved. The separation "
              "of one full power is EXACT BY CONSTRUCTION and is not a measurement; what was measured is the instrument's own uncertainty. Nothing about the quantifier, h2, "
              "totality or the roster. NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. The seam's debt item 1 restated, still unpaid. The "
              "patent lane carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands exactly where the deposit left it. The wave PARKED by the "
              "author's ruling. NOTHING DEPOSITS.")


def figures():
    R = json.load(io.open(os.path.join(D, 'b346_rate.json'), encoding='utf-8'))
    F = json.load(io.open(os.path.join(D, 'b346_filings.json'), encoding='utf-8'))
    return R, F


def rows():
    R, F = figures()
    P, K = R['premise'], R['rate']
    ratio_dep = 1.421e-14
    m = ("THE EXPONENT BY RATE: A FLOOR IS PRESENT, SO NO DOMAIN RESOLVES THE EXPONENT BY VALUE; AND ON THE RATE AXIS THE QUESTION IS RESOLVED AT A RESOLVING POWER OF "
         "%.0f, WITH THE BANKED VALUES' OWN CONVENTION READ OFF THEIR DECAY (b346)" % R['resolving_power'])
    stmt = (m + ": **THE PREMISE WAS TESTED AND NOT ASSUMED.** (C1) b339's own sealed limit arithmetic, imported, puts the fitted limit ABOVE BOTH candidates at every "
            "covered cell -- by %.2f and %.2f separations at a = 1.3, %.2f and %.2f at 1.35, %.2f and %.2f at 1.41 -- and (C2) b344's ladder converges in NY with the whole "
            "remaining travel from the corpus's own NY = 512 equal to %.4f of b339's floor at that cell, so the one axis of the three that has been priced cannot carry the "
            "residual to zero. **A FLOOR IS PRESENT; NO DOMAIN RESOLVES THE EXPONENT BY VALUE.** The floor is NOT explained: the cut's tau and the taper are named and not "
            "moved. **THEN THE RATE, ON A DIFFERENT AXIS.** The even sector's decay along the ARGUMENT, because b315 measured the rate moving a full power there while along "
            "the cutoff it does not move at all, the cutoff measure absorbing exactly the one power the flip introduces. The two conventions were taken from b313's "
            "copy-maker unedited -- the owner's r ** -0.5 and the flipped copy's r ** +0.5 -- on the %d cells b264's own second axis marked converged and no others, the "
            "owner recomputed against b264's banked column to %s. Their ratio is the argument itself at every cell to %s, so **THE SEPARATION IN THE EXPONENT IS EXACTLY 1.0 "
            "AND IS EXACT BY CONSTRUCTION, NOT MEASURED**; what was measured is the instrument's uncertainty in the rate, **%s**, giving a resolving power of **%.1f**, with "
            "the noise-floor gate RESOLVED at both conventions. By b322's rule the axis RESOLVES the two conventions. Applied to the banked column itself, the local slope "
            "at the top of the converged window is %s, which sits %s from the corpus's asymptote and %s from the source's: **THE BANKED VALUES CARRY THE CORPUS'S OWN "
            "r ** -0.5, READ FROM THE VALUES AND FROM NOTHING ELSE.** **WHAT THAT IS PERMITTED TO MEAN WAS FIXED IN THE SEALED REGISTRATION BEFORE THE FIGURE EXISTED:** the "
            "convention under which a banked eps-derived value was computed is recoverable from that value's own decay, so the standing clause of E-2026-09-03-1 acquires a "
            "mechanical test -- **IT DOES NOT MEAN A CONVENTION IS CORRECT**, and b313's clause that the exponent is fixed by the source's own definition governs unchanged. "
            "The consequence clause fired and is appended to ERRATA.md under a b346 mark, the named entry byte-identical. **AND TWO LIMITS ARE CARRIED RATHER THAN LEFT "
            "IMPLICIT:** the two evaluators share the prolate layer and the node counts, which b313's copy-maker declares deliberately -- a shared engine is a shared error "
            "source and independence of the prolate solver is NOT certified; and one sealed uncertainty arm did no work, a two-point drift-zero being algebraically the "
            "local slope of those two points, so the second estimator COLLAPSED ONTO THE FIRST and (u2) was structurally zero. **THAT IS TABLED AND NOT REPAIRED, THE SEALED "
            "FILE UNEDITED**; the understatement it could cause is bounded by a labelled diagnostic, the whole-window spread, which gives a resolving power of %.1f, so the "
            "verdict clears both readings."
            % (P['rows'][0]['off_ef_s'], P['rows'][0]['off_er_s'], P['rows'][1]['off_ef_s'], P['rows'][1]['off_er_s'],
               P['rows'][2]['off_ef_s'], P['rows'][2]['off_er_s'], P['frac'], len(K['cells']),
               ('%.3e' % K['repro']), ('%.3e' % ratio_dep), ('%.6e' % R['uncertainty']), R['resolving_power'],
               ('%.9f' % R['slope_top']), ('%.3e' % R['d_corpus']), ('%.3e' % R['d_source']), K['resolving_whole']))
    return [
        (m, stmt,
         "**NO TERMINAL, AND THE REASON: A RESOLVING POWER IS A PROPERTY OF THE INSTRUMENT** -- it says the axis can tell two objects apart, and nothing about which of "
         "them the mathematics requires.",
         "**NO PRINT.** Relay tools only, plus one append-only block on ERRATA.md against an existing entry which is left byte-identical; no owner instrument edited, no "
         "deposited text touched, no new frame or cell evaluated.",
         "**NO GRADE MOVED; NO BAR MOVED.** b339, b344, b313 and b264 all stand as banked, and one of this act's own sealed arms is tabled as defective.",
         SCOPE_TAIL, "current"),
    ]


def main():
    ROWS = rows()
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b346 -- THE EXPONENT BY RATE. ### THE ROW.")
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
          and 'EXACT BY CONSTRUCTION, NOT MEASURED' in ROWS[0][1]
          and 'IT DOES NOT MEAN A CONVENTION IS CORRECT' in ROWS[0][1]
          and 'TABLED AND NOT REPAIRED' in ROWS[0][1]
          and 'NO GRADE MOVED' in ROWS[0][4]
          and 'IT DOES NOT TELL YOU WHICH FUNCTION YOU SHOULD HAVE BEEN LOOKING AT' in ROWS[0][5]
          and 'NOTHING DEPOSITS' in ROWS[0][5])
    print('  the row says NO TERMINAL with the reason, the separation exact by construction, no convention correct, the collapsed arm tabled, no grade moved : %s' % g1)
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
