# -*- coding: utf-8 -*-
"""b326_correspondence.py -- TWO ROWS: THE REACH, AND THE KERNEL THE CLOSURE DECIDED.

### ### **THE NOTATION GUARD AND THE BLANK-CELL AUDIT ARE IMPORTED, NEVER COPIED.**

### ### **THE HAZARD OF THESE TWO ROWS:**
###   ### ### **ROW ONE SAYS THE INSTRUMENT DOES NOT SEE A FAILING HYPOTHESIS TO `a = 400`, AND THAT
###     ### READS AS A VERDICT ON THE METHOD.** ### It is a verdict on ONE FAMILY of lawful test
###     functions (and one declared aimed family) at one reach, with the reason named from the
###     numbers; the family that could see it is priced in the same row.
###   ### ### **ROW TWO SAYS THE PRIOR ACT'S KERNEL WAS HALF, AND THAT READS AS b325 IMPEACHED.** ###
###     b325's verdict at the arc's cells stands and is stronger; what is withdrawn is a PRICE, by a
###     measurement b325 could not make. ### And this act declares three failings of its own in the
###     same breath.
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
    ("THE REACH: THE EPSTEIN ZEROS COMPUTED, BOTH WINDOWS EXTENDED, THE FORMULA CLOSED FOR BOTH, "
     "AND THE INSTRUMENT STILL DOES NOT SEE IT (b326)",

     "THE REACH: THE EPSTEIN ZEROS COMPUTED, BOTH WINDOWS EXTENDED, THE FORMULA CLOSED FOR BOTH, "
     "AND THE INSTRUMENT STILL DOES NOT SEE IT (b326): the Epstein function's zeros on the line "
     "were computed to T = 150 by the corpus's own argument-principle census run at Re s = 1/2 -- "
     "**146 ZEROS, EVERY ONE AGREED BY AN INDEPENDENT SECOND ROUTE**, every box holding exactly its "
     "sign-change count -- and a completeness census over sigma in [0.52, 1.50] located "
     "**SEVENTEEN OFF-LINE ZEROS, FIFTEEN OF THEM UNBANKED**, closing the count at 180 against a "
     "main term of 178.6. Both windows were extended with every prime and every representation "
     "number to a = 400: **ZETA KEEPS THE PERMITTED SIGN AT ALL TWENTY-SIX CELLS; SO DOES THE "
     "EPSTEIN FUNCTION.** The explicit formula closes for zeta at 26 of 26 and for the Epstein "
     "function, with every located zero, at 21 of 21 cells below the library's ceiling. "
     "**VERDICT: DOES NOT SEE IT** -- at the arc's family to a = 400, and at a declared aimed "
     "family too.",

     "**NO TERMINAL, AND THE REASON IS NAMED FROM THE NUMBERS.** On f = g conv g^# the failing "
     "function's zero side is a sum of squares over its on-line zeros plus the off-line four-term "
     "sums, and **THOSE SUMS COME OUT POSITIVE** for a seed whose transform keeps its sign across "
     "the off-line real part -- +1.29 of 25.4 at a = 1.3, negligible beyond. The places sum is "
     "minus that zero side: the permitted sign, for the same reason zeta's is. Aimed at the banked "
     "off-line height (cos(omega v) on every bump, omega = 16.290216), the off-line terms carry 92 "
     "to 98 per cent of the zero side and carry it positive; the places sum is MORE negative, not "
     "less. **THE FAMILY THAT COULD SEE THE FAILURE NEEDS A SIGN CHANGE ACROSS beta AND 1 - beta**, "
     "and is priced at one act, not built.",

     "**AND THE ENTAILMENT, AT EXACTLY ITS SCOPE.** On this instrument, at this reach, the "
     "finite-instance places sum on the arc's family does NOT discriminate a holding hypothesis "
     "from a failing one: both take the permitted sign at every cell to a = 400. **SO THE ZETA "
     "WINDOW AT THIS REACH IS NOT A PASSED TEST; IT IS A TEST THIS FAMILY CANNOT FAIL**, and the "
     "arc's *could not have come out otherwise* is restated as true of the library at the arc's "
     "cells and, on this family, true of the method to a = 400. The navigator's expectation -- "
     "SEES IT near the priced crossing, zeta negative throughout -- is REFUTED in its first half "
     "(the crossing was an artefact, row 165) and MET in its second. The ceiling: T = 150, a = "
     "400, n = 160002; the five narrowest cells beyond it for the Epstein function.",

     "**A REGISTRATION SEALED BEFORE ANY RUN, AND THREE OF ITS OWN ESTIMATES CAUGHT BY ITS OWN "
     "GATES.** **SCOPE: a computation on the explicit-formula instrument, which transfers; NOT "
     "on the source's inequality or the object's decomposition, which do not -- Gamma(s) against "
     "Gamma(s/2).** The registered precision was sixty digits short and the registered gate fired "
     "before a zero was located; the registered truncation list omitted the archimedean u-range, "
     "measured and added; the closure tool's first run aliased zeta's ordinates and is kept under "
     "its own name. NO CLAIM ABOUT ZETA, h2, OR THE ROSTER. NO GRADE MOVED. NO ACT RE-VERDICTED. "
     "NO AGGREGATION IS STATED; M-2 REMAINS (SPECIFIED-NOT-STATED) under b310's cap. NOTHING "
     "DEPOSITS.",

     "current"),

    ("THE KERNEL THE CLOSURE DECIDED: b325's EPSTEIN ARCHIMEDEAN CHANNEL WAS HALF, AND ITS PRICED "
     "CROSSING IS WITHDRAWN (b326)",

     "THE KERNEL THE CLOSURE DECIDED: b325's EPSTEIN ARCHIMEDEAN CHANNEL WAS HALF, AND ITS PRICED "
     "CROSSING IS WITHDRAWN (b326): a derivation written into this act's registration BEFORE any "
     "run gave the Epstein kernel as 2 Re(gamma_Q'/gamma_Q) = 2 Re psi(1/2 + i u) - 2 log(2 pi / "
     "sqrt23) -- exactly as zeta's atlas kernel is 2 Re(gamma_R'/gamma_R) -- and named b325's "
     "kernel_q as one half of it. **THE EXPLICIT FORMULA DECIDED IT:** with the derived kernel the "
     "Epstein function closes at 21 of 21 cells below the ceiling; with b325's it fails at 21 of "
     "21, **AND AT EVERY ONE THE RESIDUAL EQUALS THE MISSING HALF TO WITHIN THE BAR** (+2.2495 "
     "against 2.249540 at a = 3; +0.3915 against 0.391483 at a = 22). Every Epstein archimedean "
     "channel and places sum b325 banked was formed on the halved kernel; **THE CROSSING IT PRICED "
     "AT a ~ 22 WAS THE HALVED CHANNEL'S ARTEFACT** -- the true places sum there is -0.374, and the "
     "+0.017 reappears under b325's kernel and nowhere else.",

     "**b325 IS NOT RE-VERDICTED.** Its DOES NOT SEE IT at the arc's cells stands and is stronger "
     "-- the true places sums are twice as negative -- and what is withdrawn is a PRICE it attached "
     "to widths beyond its cells, by the measurement it reported as blocked: the closure on the "
     "Epstein function's own zero library. Its sealed registration is not edited; the defect is "
     "filed against it as a sealed-bar-found-defective row for the next fold, and the internal "
     "confinement keystone gains an appended line correcting b325's block above it, the original "
     "visible.",

     "**AND THE LIBRARY THE ORDER NAMED DID NOT CLOSE, WHICH IS HOW THE COMPLETENESS CENSUS WAS "
     "FORCED.** With the on-line zeros and the two banked off-line ones alone the formula fails at "
     "15 cells (-2.3e-03 at a = 3 against a bar of 2.2e-04); the fourth link -- the library's "
     "completeness -- was walked, and the census's own winding over the whole right half-strip "
     "found fifteen off-line zeros above the height the corpus's census had reached, each agreed "
     "by both routes. With them the formula closes. **THE CORPUS'S CENSUS IS NOT CALLED WRONG**: it "
     "banked what lay below t = 33 and it was right.",

     "**A CONSTANT IS SCOPE-BOUND AND ITS SCOPE IS WRITTEN DOWN -- NOW IN THE LORE, WITH ITS "
     "GATE.** **SCOPE: the ordered edit replaces b321_window's eleven-prime tuple by a generator "
     "to the reach, with the scope in the header; its fixtures pass 8 of 8 and fixture (i) is still "
     "bit-for-bit against the atlas.** The lore's self-test carries the rule in both polarities. "
     "NO GRADE MOVED. NO ACT RE-VERDICTED. NO AGGREGATION IS STATED; M-2 REMAINS "
     "(SPECIFIED-NOT-STATED). The seam's debt item 1 restated, still unpaid. The patent lane "
     "carried on the patent seat's report, UNCONFIRMED on this seat's record. h2 stands exactly "
     "where the deposit left it. NOTHING DEPOSITS.",

     "current"),
]


def main():
    txt = io.open(TABLE, encoding='utf-8').read()
    pos, neg = C.blank_check_fixture()
    sa, sb, sc, sd = G.split_fixture()
    print('=' * 100)
    print("b326 -- THE REACH.")
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
    # ### **THE TWO GUARDS THAT MATTER FOR THESE TWO ROWS**, and they are guards against the two
    # ### readings the rows most invite: that a family verdict is a method verdict, and that a
    # ### withdrawn price is a re-verdicted act.
    g1 = ('DOES NOT SEE IT' in r1[1]
          and 'NOT A PASSED TEST' in r1[3]
          and 'priced at one act, not built' in r1[2]
          and 'REFUTED in its first half' in r1[3])
    g2 = ('MISSING HALF' in r2[1]
          and 'b325 IS NOT RE-VERDICTED' in r2[2]
          and 'CENSUS IS NOT CALLED WRONG' in r2[3]
          and 'NOTHING DEPOSITS' in r2[4])
    print('  row 1 carries DOES NOT SEE IT, the entailment, the priced family and the refutation : %s  %s'
          % (g1, 'PASS' if g1 else '### FAIL ###'))
    print('  row 2 carries the missing half, b325 unmoved, the census unblamed : %s  %s'
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
