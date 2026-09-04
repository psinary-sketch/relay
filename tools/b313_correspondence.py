# -*- coding: utf-8 -*-
"""b313_correspondence.py -- TWO ROWS: THE RESIDUE IS NOT THE EXPONENT, AND WHAT IT IS PART OF.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.**

### ### **THE HAZARD OF THESE TWO ROWS:**
###   ### **ROW ONE REPORTS A NEGATIVE OUTCOME OF A LICENSED CHANGE, AND A ROW LIKE THAT READS AS
###     ### A RETRACTION OF THE CHANGE.** ### It is not one. ### **THE EXPONENT IS FIXED BY THE
###     ### SOURCE'S DEFINITION AND BY NOTHING THE RESIDUE DOES**, and the grade cell says so.
###   ### **ROW TWO REPORTS A PERCENTAGE, AND A PERCENTAGE READS AS AN EXPLANATION OF THAT MUCH OF
###     ### SOMETHING.** ### It is a difference between two columns of one table at six cells, and
###     the row says that before it says the number.
"""
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b302_correspondence as C   # noqa: E402
import b303_correspondence as G   # noqa: E402

SIDE = r'D:\SIDE-global-section'
TABLE = os.path.join(SIDE, 'CORRESPONDENCE.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

ROWS = [
    ("THE RESIDUE IS NOT THE EXPONENT (b313)",

     "THE RESIDUE IS NOT THE EXPONENT (b313): b312 identified the corpus's archimedean remainder "
     "as differing from the source's by a factor of `\u03c1`; **THIS ACT RAN THE CHECK b312 FILED "
     "AND THE RESIDUE DID NOT COLLAPSE.** In a COPY of the instrument \u2014 the owner files "
     "untouched \u2014 the remainder side was recomputed under the source's exponent, everything "
     "else byte-identical. **`resid = Tr \u2212 A \u2212 E2` FELL FROM "
     "(4.0486, 3.3740, 3.0478, 2.5208, 2.4540, 2.3134) TO "
     "(3.7150, 2.9792, 2.6347, 2.0917, 2.0242, 1.8834)** at `a\u00b2 = 2, 3, 4, 8, 9, 12` "
     "\u2014 ratios **0.9176, 0.8830, 0.8645, 0.8298, 0.8249, 0.8141**, a shrinkage of 8% to 19% "
     "with the order of magnitude kept at every cell. **`A` AND `Tr` DO NOT MOVE AT ALL**, "
     "measured and not asserted: neither call path touches the exponent.",

     "**NO TERMINAL, AND THE SHADOW WAS EXPECTED TO BE NOTHING AND IS NOTHING** \u2014 a "
     "floating-point instrument comparison is not finite-decidable, and a terminal over a rounded "
     "number would certify the rounding. **WHAT CARRIES THE ACT INSTEAD IS FOUR MEASURED "
     "CONTROLS**: the transcribed loop reproduces the owner's month-old banked table to "
     "**4.98e-05**, which is that table's own display rounding; the copy with the exponent "
     "RESTORED reproduces the owner at **78 of 78 quantities BITWISE**; the flip is a pointwise "
     "`\u03c1` factor to **5.55e-16**; and the ladder reproduces b264's banked `eps_even` column "
     "to **7.97e-12**. **AND `G-ROUNDTRIP` FIRED ON THE FIRST RUN, ON A REAL DEFECT** \u2014 the "
     "flip was first written as a fragment whose inverse already occurs in `Qeps`, so the copy was "
     "not uniquely invertible; the write is now GATED on the controls rather than reported beside "
     "them.",

     "**NO PRINT. NOTHING COMPILED THIS ACT** \u2014 the profile stands unchanged at 475. **THE "
     "OWNER INSTRUMENT WAS NOT EDITED**: `qeps_layer.py`, `b38_act10.py` and `b264_eps_decay.py` "
     "stand byte-identical to `git HEAD`, checked AFTER the run and not before it. Three copies "
     "carry the flip, 13 declared substitutions, 13 diff lines, each printed in full with its "
     "reason; exactly one per file is the flip and the rest are what a copy needs to BE a copy "
     "\u2014 including **EVERY OUTPUT PATH REDIRECTED, SO THAT RUNNING A COPY CANNOT OVERWRITE AN "
     "OWNER'S BANKED ARTIFACT.** `main()` is never called, because calling it would rewrite the "
     "very table this act reads as its reference.",

     "**A MEASUREMENT, AND A NEGATIVE ONE.** **SCOPE, AND IT IS THE WHOLE OF THE ROW'S HONESTY: "
     "THIS DOES NOT MEAN THE FLIP WAS WRONG.** The exponent is fixed by the source's own "
     "definition of the object the corpus imported and by NOTHING the residue does \u2014 the "
     "standing clause binds in this direction exactly as hard as it would have bound in the other, "
     "and an act that kept a flip only when the residue improved would be tuning an instrument to "
     "an answer. **b312 DECIDED WHICH FUNCTION THE CORPUS'S REMAINDER IS, BY UNFOLDING "
     "DEFINITIONS, AND A RESIDUE IS NOT A VOTE ON THAT.** **NO BANKED NUMBER IS CALLED WRONG AND "
     "NO ACT IS RE-VERDICTED** \u2014 what this act adds is a second column beside the first. The "
     "third and fourth face-offs are NOT re-read: the order attaches a sentence to their "
     "interpretation only on the branch this act did not take, so their numbers stand as banked "
     "and their readings stand unamended. **NOTHING ABOUT THE IDENTITY, `h2`, OR THE ROSTER "
     "FOLLOWS.** NO TARGET WAS NAMED AND NO FIT WAS PERFORMED. NO AGGREGATION IS STATED. M-2 "
     "REMAINS (SPECIFIED-NOT-STATED), UNCHANGED under b310's cap.",

     "current"),

    ("WHAT THE CONVENTION DOES ACCOUNT FOR (b313)",

     "WHAT THE CONVENTION DOES ACCOUNT FOR (b313): the flip is **EXACTLY MULTIPLICATION BY "
     "`\u03c1`**, measured to 5.55e-16 across all 240 grid points, so every consequence is a "
     "one-power shift. **b264's LADDER, RE-RUN UNDER THE FLIP AT ITS OWN REACH WITH THE "
     "NOISE-FLOOR GATE IN THE PATH** (its own `NRES = 7`; even-indexed floor modes 8 and 10, and "
     "what excluding them removes is PRINTED at 1e-11 to 1e-15 rather than called negligible): the "
     "even sector's decay moves from `\u03c1^(\u22123/2)` to `\u03c1^(\u22121/2)` and **b264's "
     "measured leading constant does not move at all** \u2014 `eps_even \u00b7 \u03c1^(3/2)` and "
     "`eps_even \u00b7 \u03c1^(1/2)` agree to 1.09e-11 at every ladder cell. **AND THE BANKED "
     "CROSS-CHECK IS SHOWN INSENSITIVE, AS b312 DERIVED**: `eps'(1+)` is BITWISE identical under "
     "both conventions, and the one-sided difference quotient of `eps` itself converges to the "
     "same limit with the two columns' difference falling linearly in `h`.",

     "**NO TERMINAL.** The insensitivity was DERIVED at b312 and is MEASURED here; the measurement "
     "does not certify the derivation and is not offered as doing so. **WHAT IS MACHINE-CHECKED IS "
     "THE CALL-PATH TABLE**: six quantities computed twice and compared \u2014 `A`, `P`, `PR`, "
     "`Thq`, `Tr`, `eps'(1+)` \u2014 and found unmoved, and nine found moved. **THE SIX THAT DO "
     "NOT MOVE ARE NOT ASSERTED NOT TO MOVE.**",

     "**NO PRINT.** One column is reported that the order did not ask for, and is declared as a "
     "deviation: `A + E2` runs from \u22120.311 to \u22120.430 under the banked convention and "
     "from +0.0225 to \u22120.00028 under the source's. **IT IS PRINTED BECAUSE IT MOVED AND THE "
     "ORDER SAYS TO REPORT WHAT MOVES, AND IT IS EXPLICITLY NOT INTERPRETED** \u2014 for a "
     "MEASURED reason: `A` comes from `carto_atlas.py`, whose header says its sign is *[sign fixed "
     "BY the E2 calibration]* and which declares *No sign claim is made*, so the column compares a "
     "term against the very quantity its sign was calibrated against. **AND ITS DIRECTION IS "
     "STATED SO NOBODY READS IT AS AN IMPROVEMENT: the identity's two right-hand terms nearly "
     "CANCEL, so the residue becomes essentially the whole trace \u2014 the opposite shape from an "
     "identity closing.** Filed as `W-ORD-A-PLUS-E2`.",

     "**AN INSTRUMENT FINDING, ROUTED AND NOT FILED.** **SCOPE: the convention mismatch accounts "
     "for BETWEEN 8% AND 19% OF THE RESIDUE AT SIX CELLS. IT DOES NOT ACCOUNT FOR THE REST, AND "
     "NOTHING HERE SAYS WHAT DOES.** The finding is routed to the author as an **ERRATA-CLASS "
     "CANDIDATE (internal record)** on the `E1` precedent discharged at `E-2026-08-31-1`, where "
     "the sites carrying a superseded clause were left BYTE-IDENTICAL and not rewritten because "
     "**THE RECORD DOES NOT SILENTLY OVERWRITE ITSELF**: the owner files are untouched and the "
     "correction of record is in this act's bank. **AN ERRATUM IS THE AUTHOR'S INSTRUMENT, AND A "
     "SEAT THAT FILES ITS OWN ERRATA IS MARKING ITS OWN WORK** \u2014 `PLACE-papers` is untouched, "
     "at cap zero. What it would affect if filed, stated honestly: every banked number computed "
     "through those three call paths is a computation of the corpus's own function rather than of "
     "the source's \u2014 **A STATEMENT ABOUT WHAT THE NUMBERS ARE COMPUTATIONS OF, NOT A CLAIM "
     "THAT ANY OF THEM IS WRONG.** Two sites already carried the source's convention and nobody "
     "has swept the instrument for others: `W-ORD-CONVENTION-SWEEP` filed. NO GRADE MOVED. NO "
     "AGGREGATION IS STATED. M-2 REMAINS (SPECIFIED-NOT-STATED). h2 stands exactly where the "
     "deposit left it.",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print('b313 -- THE MEASUREMENT\'S ROW, AND THE CONVENTION\'S SHARE.')
    print('=' * 100)
    print('  BLANK-CHECK FIXTURE (imported from b302): real blank=%s  quiet on full=%s  %s'
          % (pos, neg, 'PASS' if (pos and neg) else '### FAIL ###'))
    print('  SPLITTER FIXTURE (imported from b303): plain=%s escaped=%s content=%s raw=%s  %s'
          % (sa, sb, sc, sd, 'PASS' if (sa and sb and sc and sd) else '### FAIL ###'))
    if not (pos and neg and sa and sb and sc and sd):
        return 1
    print('  blank cells in the whole table (line-scoped) : %d' % C.blank_cells(txt))

    bad = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if G.raw_pipes(str(c))]
    print('  cells carrying an UNESCAPED pipe (checked BEFORE writing) : %d  %s'
          % (len(bad), 'PASS' if not bad else '### FAIL ### at %s' % bad))
    if bad:
        return 1

    slip = [m for m, s, _t, _p, _g, _st in ROWS if not s.startswith(m)]
    print('  marker is a literal prefix of its statement : %d/%d  %s'
          % (len(ROWS) - len(slip), len(ROWS), 'PASS' if not slip else '### FAIL ###'))
    if slip:
        return 1

    present = [m for m, _s, _t, _p, _g, _st in ROWS if m in txt]
    if present:
        print('  ### ROW(S) ALREADY PRESENT -- NOTHING WRITTEN: %s' % present)
        got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
        print('  table rows now : %d   blank cells : %d' % (len(got), C.blank_cells(txt)))
        print('=' * 100)
        return 0

    nums = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', txt, re.M)]
    start = max(nums) + 1
    print('  last existing row : %d' % max(nums))
    print('  rows to append    : %d  (numbers %d..%d)' % (len(ROWS), start, start + len(ROWS) - 1))

    blank = [(i, j) for i, r in enumerate(ROWS) for j, c in enumerate(r) if not str(c).strip()]
    print('  blank cells in the new rows : %d  %s'
          % (len(blank), 'PASS' if not blank else '### FAIL ###'))
    if blank:
        return 1

    r1, r2 = ROWS[0], ROWS[1]
    g1 = ('THIS DOES NOT MEAN THE FLIP WAS WRONG' in r1[4]
          and 'NO BANKED NUMBER IS CALLED WRONG' in r1[4]
          and 'NO TARGET WAS NAMED AND NO FIT WAS PERFORMED' in r1[4])
    g2 = ('IT DOES NOT ACCOUNT FOR THE REST' in r2[4]
          and 'ROUTED AND NOT FILED' in r2[4]
          and 'NOT A CLAIM' in r2[4])
    print('  row 1 refuses the retraction reading and the fit reading : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 bounds its percentage and routes rather than files : %s  %s'
          % (g2, 'PASS' if g2 else '### FAIL ###'))
    if not (g1 and g2):
        return 1

    over = [i for i, r in enumerate(ROWS) if 'SCOPE' not in r[4] or 'M-2' not in r[4]]
    print('  rows carrying their own scope refusal and M-2\'s row : %d/%d  %s'
          % (len(ROWS) - len(over), len(ROWS), 'PASS' if not over else '### FAIL ###'))
    if over:
        return 1

    lines = []
    for k, (_mark, stmt, term, prof, grade, status) in enumerate(ROWS):
        lines.append('| %d | %s | %s | %s | %s | %s |'
                     % (start + k, stmt, term, prof, grade, status))
    new = txt.rstrip('\n') + '\n' + '\n'.join(lines) + '\n'
    open(TABLE + '.tmp', 'wb').write(new.encode('utf-8'))
    os.replace(TABLE + '.tmp', TABLE)

    back = io.open(TABLE, encoding='utf-8').read()
    got = [int(m.group(1)) for m in re.finditer(r'^\| (\d+) \|', back, re.M)]
    tail = back.rstrip('\n').split('\n')[-len(ROWS):]
    cellcounts = [len(G.split_cells(ln)) for ln in tail]
    ok = (got[-len(ROWS):] == list(range(start, start + len(ROWS)))
          and all(m in back for m, _s, _t, _p, _g, _st in ROWS)
          and C.blank_cells(back) == 0
          and all(c == 6 for c in cellcounts)
          and all(all(x.strip() for x in G.split_cells(ln)) for ln in tail))
    print('  READ BACK         : last %d row number(s) are %s' % (len(ROWS), got[-len(ROWS):]))
    print('  cells on disk in the appended rows : %s  (6 required each, none blank)' % cellcounts)
    print('  blank cells after (line-scoped)   : %d' % C.blank_cells(back))
    print('  table rows now    : %d  %s' % (len(got), 'PASS' if ok else '### FAIL ###'))
    print('  ### and that means THE CELLS SURVIVED. It does not mean they are true.')
    print('=' * 100)
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
